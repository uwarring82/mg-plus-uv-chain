"""Import, inspect and publish the AG Schaetz SHG drawing catalogue.

SPDX-License-Identifier: MIT

Raw DWGs are never modified. ODA exports stay separate from reconstructed
previews. Cached Inventor block references are rendered as explicitly
unverified previews; this script is not a DWG fidelity certification tool.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import math
import platform
import struct
import subprocess
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DATA = Path("data/designs/shg")
ASSETS = Path("docs/assets/shg")
CATALOGUE = DATA / "catalogue.yaml"
SCHEMA = DATA / "catalogue.schema.json"
PREVIEW_NOTICE = (
    "UNVERIFIED PREVIEW | AG Schaetz | CERN-OHL-S-2.0 | "
    "CAD symbols/placement may differ"
)


def sha256(data: bytes) -> str:
    """Return a SHA-256 digest for provenance checks."""
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    """Serialize metadata deterministically without non-finite numbers."""
    return (
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    ).encode()


def gzip_bytes(data: bytes) -> bytes:
    """Compress without a filename or timestamp in the gzip header."""
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="wb", filename="", mtime=0) as stream:
        stream.write(data)
    return out.getvalue()


def artifact(path: Path, root: Path = ROOT) -> dict[str, Any]:
    """Describe a repository file with size and content digest."""
    data = (root / path).read_bytes()
    return {"path": path.as_posix(), "sha256": sha256(data), "bytes": len(data)}


def load_catalogue(root: Path = ROOT) -> dict[str, Any]:
    """Read the sole editable catalogue record."""
    return yaml.safe_load((root / CATALOGUE).read_text())


def save_catalogue(catalogue: dict[str, Any], root: Path = ROOT) -> None:
    """Write canonical YAML without sorting the curated design order."""
    (root / CATALOGUE).write_text(
        yaml.safe_dump(catalogue, allow_unicode=True, sort_keys=False, width=92)
    )


def archive_name(info: zipfile.ZipInfo) -> tuple[str, str]:
    """Recover UTF-8 bytes stored in a ZIP name without its UTF-8 flag."""
    encoding = "utf-8" if info.flag_bits & 0x800 else "cp437"
    raw = info.filename.encode(encoding)
    try:
        name = raw.decode("utf-8")
    except UnicodeDecodeError:
        name = info.filename
    return name, raw.hex()


def ingest(archive: Path, root: Path = ROOT) -> None:
    """Copy the registered DWGs verbatim and capture archive provenance."""
    catalogue = load_catalogue(root)
    payload = archive.read_bytes()
    catalogue["archive"] = {
        "filename": archive.name,
        "sha256": sha256(payload),
        "bytes": len(payload),
        "excluded": [".DS_Store", "__MACOSX"],
    }
    entries = {}
    with zipfile.ZipFile(io.BytesIO(payload)) as source:
        for info in source.infolist():
            if info.filename.lower().endswith(".dwg"):
                original, raw_name = archive_name(info)
                key = unicodedata.normalize("NFC", Path(original).name)
                if key in entries:
                    raise ValueError(f"Duplicate normalized archive name: {key}")
                entries[key] = (info, original, raw_name)
        expected = {
            unicodedata.normalize("NFC", d["original_filename"])
            for d in catalogue["designs"]
        }
        if set(entries) != expected:
            raise ValueError("Archive drawings do not match the explicit ID registry")
        for design in catalogue["designs"]:
            key = unicodedata.normalize("NFC", design["original_filename"])
            info, original, raw_name = entries[key]
            data = source.read(info)
            path = DATA / "raw" / f"{design['id']}.dwg"
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and destination.read_bytes() != data:
                raise ValueError(f"Refusing to replace different source: {path}")
            destination.write_bytes(data)
            design["source"] = {
                **artifact(path, root),
                "dwg_header": data[:6].decode("ascii"),
                "archive_entry": original,
                "archive_name_bytes_hex": raw_name,
                "zip_utf8_flag": bool(info.flag_bits & 0x800),
                "zip_modified_local": datetime(*info.date_time).isoformat(),
                "timestamp_timezone": "unspecified",
                "original_filename": Path(original).name,
            }
    save_catalogue(catalogue, root)


def convert(oda: Path, destination: Path, root: Path = ROOT) -> None:
    """Run a local ODA export without its optional audit/repair operation."""
    destination.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(oda),
            str(root / DATA / "raw"),
            str(destination),
            "ACAD2018",
            "DXF",
            "0",
            "0",
            "*.dwg",
        ],
        check=True,
        timeout=600,
    )


def inspect_sources(reader: Path, root: Path = ROOT) -> None:
    """Read source DWGs with LibreDWG, preserving source-side metadata.

    Compressed JSON preserves the complete reader object graph. Compact
    reports retain counts, original date encodings and reader warnings.
    Unknown proxies remain opaque; this is not a rendering reference.
    """
    catalogue = load_catalogue(root)
    version = subprocess.check_output(
        [str(reader), "--version"], text=True
    ).splitlines()[0]
    with tempfile.TemporaryDirectory(prefix="shg-source-read-") as temporary:
        for design in catalogue["designs"]:
            target = Path(temporary) / "source.json"
            run = subprocess.run(
                [
                    str(reader),
                    "-O",
                    "JSON",
                    "-o",
                    str(target),
                    str(root / design["source"]["path"]),
                ],
                capture_output=True,
                text=True,
                timeout=180,
            )
            if run.returncode:
                raise RuntimeError(
                    f"Source reader failed for {design['id']}: {run.stderr}"
                )
            decoded = json.loads(target.read_text())
            header = decoded["HEADER"]
            summary = {
                "design_id": design["id"],
                "source_sha256": design["source"]["sha256"],
                "reader": version,
                "exit_code": run.returncode,
                "stderr": run.stderr.strip(),
                "source_entity_counts": dict(
                    sorted(
                        Counter(
                            obj["entity"]
                            for obj in decoded["OBJECTS"]
                            if "entity" in obj
                        ).items()
                    )
                ),
                "source_object_counts": dict(
                    sorted(
                        Counter(
                            obj["object"]
                            for obj in decoded["OBJECTS"]
                            if "object" in obj
                        ).items()
                    )
                ),
                "header_units": header.get("INSUNITS"),
                "original_header_dates": {
                    key: header.get(key) for key in ("TDUCREATE", "TDUUPDATE")
                },
                "date_encoding": (
                    "[Julian day, milliseconds within day], "
                    "source TDU fields; retained verbatim"
                ),
                "summary_dates": {
                    key: decoded.get("SummaryInfo", {}).get(key)
                    for key in ("TDCREATE", "TDUPDATE")
                },
                "source_application": decoded.get("AppInfo", {}).get("appinfo_name"),
                "source_classes": [
                    {"dxfname": item.get("dxfname"), "appname": item.get("appname")}
                    for item in decoded.get("CLASSES", [])
                ],
                "reference_rendering_status": "not_a_rendering_reference",
            }
            path = DATA / "processed" / design["id"] / "source-inspection.json"
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_bytes(json_bytes(summary))
            design["source_inspection"] = artifact(path, root)
            graph_path = path.parent / f"{design['id']}.dwg.json.gz"
            graph_bytes = target.read_bytes()
            (root / graph_path).write_bytes(gzip_bytes(graph_bytes))
            design["source_json"] = {
                **artifact(graph_path, root),
                "uncompressed_bytes": len(graph_bytes),
                "uncompressed_sha256": sha256(graph_bytes),
                "licence": "CERN-OHL-S-2.0",
                "format": "LibreDWG JSON object graph (gzip compressed)",
                "interpretation": "Unknown proxy payloads remain opaque",
            }
            print(f"{design['id']}: source reader exit {run.returncode}", flush=True)
    save_catalogue(catalogue, root)


def proxy_block(entity: Any, doc: Any) -> Any:
    """Return an existing cached block named by a proxy's hard pointer."""
    for tag in entity.acdb_proxy_entity:
        if tag.code == 340:
            target = doc.entitydb.get(tag.value)
            if target is not None and target.dxftype() == "BLOCK_RECORD":
                return doc.blocks.get(target.dxf.name)
    return None


def cached_insert_point(payload: bytes, bit_count: int) -> tuple[float, float, float]:
    """Decode only the collection's observed unit-transform proxy variant.

    Three DWG bit-coded doubles hold the insertion point. The exact trailing
    identity-transform signature must match; any unfamiliar encoding fails
    closed. This restricted reverse-engineered decoding remains unverified
    against an independent CAD renderer and is never used for fabrication.
    """
    bits = "".join(f"{value:08b}" for value in payload)
    if bit_count > len(bits):
        raise ValueError("Truncated proxy payload")
    cursor = 0
    coordinates = []
    for _ in range(3):
        tag = bits[cursor : cursor + 2]
        cursor += 2
        if tag == "00":
            if cursor + 64 > bit_count:
                raise ValueError("Truncated proxy coordinate")
            raw = bytes(int(bits[i : i + 8], 2) for i in range(cursor, cursor + 64, 8))
            value = struct.unpack("<d", raw)[0]
            cursor += 64
        elif tag == "01":
            value = 1.0
        elif tag == "10":
            value = 0.0
        else:
            raise ValueError("Unsupported bit-double tag")
        if not math.isfinite(value):
            raise ValueError("Non-finite proxy coordinate")
        coordinates.append(value)
    if bits[cursor:bit_count] != "11101010010":
        raise ValueError("Unsupported cached-block transformation")
    return tuple(coordinates)


def resolve_cached_blocks(doc: Any) -> list[dict[str, Any]]:
    """Expose cached blocks at decoded source coordinates, retaining viewports.

    The original proxy data and direct DXF export stay unchanged. Native
    viewport scaling/clipping is handled by ezdxf after block exposure.
    Unsupported block transforms stop processing rather than inventing poses.
    """
    placements = []
    for owner in doc.layouts:
        for entity in list(owner):
            if entity.dxftype() != "ACAD_PROXY_ENTITY":
                continue
            block = proxy_block(entity, doc)
            if block is None or not len(block):
                continue
            payload = b""
            bit_count = None
            for tag in entity.acdb_proxy_entity:
                if tag.code == 161:
                    bit_count = tag.value
                elif tag.code == 310 and bit_count is not None:
                    payload += tag.value
            if bit_count is None:
                raise ValueError(f"Missing proxy object data: {entity.dxf.handle}")
            insert = cached_insert_point(payload, bit_count)
            exposed = owner.add_blockref(block.name, insert, dxfattribs={"layer": "0"})
            viewport_handle = None
            for tag in entity.acdb_proxy_entity:
                candidate = doc.entitydb.get(tag.value) if tag.code == 330 else None
                if candidate is not None and candidate.dxftype() == "VIEWPORT":
                    viewport_handle = candidate.dxf.handle
            placements.append(
                {
                    "proxy_handle": entity.dxf.handle,
                    "exposed_handle": exposed.dxf.handle,
                    "viewport_handle": viewport_handle,
                    "block": block.name,
                    "owner_layout": owner.name,
                    "method": "decoded_cached_block_origin_unit_transform",
                    "insert_native": list(insert),
                    "transform_validation": "restricted_signature_unverified",
                }
            )
    if "*IDW_BlockReferenceLayer" in doc.layers:
        doc.layers.get("*IDW_BlockReferenceLayer").on()
        doc.layers.get("*IDW_BlockReferenceLayer").thaw()
    return placements


def layout_content(sheet: Any) -> tuple[bool, str]:
    """Decide if a sheet contains drawable content beyond viewport frames.

    Called after cached block exposure. Empty INSERT blocks do not qualify.
    Unresolved proxies alone do not establish renderable content.
    """
    from ezdxf import bbox
    from ezdxf.addons.drawing import Frontend, RenderContext
    from ezdxf.addons.drawing.recorder import Recorder

    context = RenderContext(sheet.doc)
    entities = [
        e
        for e in sheet
        if e.dxftype() not in {"VIEWPORT", "ACAD_PROXY_ENTITY"}
        and not e.dxf.get("invisible", 0)
        and context.resolve_all(e).is_visible
    ]
    bounds = bbox.extents(entities)
    if bounds.has_data:
        return True, "renderable_paper_content_or_reconstructed_cached_view"
    # Frontend applies viewport clipping, status and layer visibility, and
    # does not draw the viewport frame itself. Geometry outside the view
    # therefore cannot make an otherwise empty sheet qualify.
    recorder = Recorder()
    Frontend(context, recorder).draw_layout(sheet)
    if recorder.player().bbox().has_data:
        return True, "viewport_displays_renderable_model_content"
    proxies = any(e.dxftype() == "ACAD_PROXY_ENTITY" for e in sheet)
    if proxies:
        return False, "unresolved_proxy_content_requires_reference_review"
    return False, "empty_layout_or_viewport_only"


def inspect_document(doc: Any) -> dict[str, Any]:
    """Extract entity inventories, annotations and unresolved features."""
    annotations = []
    dimensions = []
    for entity in doc.entitydb.values():
        kind = entity.dxftype()
        if kind in {"TEXT", "MTEXT", "ATTRIB", "ATTDEF"}:
            raw = entity.dxf.get("text", "")
            annotations.append(
                {
                    "handle": entity.dxf.handle,
                    "owner_handle": entity.dxf.owner,
                    "entity_type": kind,
                    "layer": entity.dxf.layer,
                    "text": entity.plain_text() if kind == "MTEXT" else raw,
                    "raw_text": raw,
                    "evidence_tag": "D",
                }
            )
        if kind == "DIMENSION":
            try:
                measurement = float(entity.get_measurement())
            except (TypeError, ValueError, NotImplementedError):
                measurement = None
            dimensions.append(
                {
                    "handle": entity.dxf.handle,
                    "text_override": entity.dxf.get("text", ""),
                    "measurement_native": measurement,
                }
            )
    return {
        "entity_counts": dict(
            sorted(Counter(e.dxftype() for e in doc.entitydb.values()).items())
        ),
        "model_entity_counts": dict(
            sorted(Counter(e.dxftype() for e in doc.modelspace()).items())
        ),
        "layouts_before_reconstruction": [
            {
                "name": s.name,
                "entity_counts": dict(sorted(Counter(e.dxftype() for e in s).items())),
            }
            for s in doc.layouts
        ],
        "external_references": [
            {
                "block": b.name,
                "path": b.block.dxf.get("xref_path", ""),
                "status": "unresolved",
            }
            for b in doc.blocks
            if b.block.is_xref
        ],
        "dimension_entities": dimensions,
        "dimension_comparison_status": (
            "native_dimensions_only"
            if dimensions
            else "unavailable_annotations_are_exploded_text_and_lines"
        ),
        "annotations": annotations,
        "dxf_header_dates": {
            "TDCREATE": doc.header.get("$TDCREATE"),
            "TDUPDATE": doc.header.get("$TDUPDATE"),
            "status": "converter_output_not_original_dwg_dates",
        },
    }


def process_exports(
    directory: Path, root: Path = ROOT, only: set[str] | None = None
) -> None:
    """Archive direct DXF exports and generate recorded preview derivatives."""
    import ezdxf
    import pymupdf
    from ezdxf.addons.drawing import Frontend, RenderContext, config, layout, svg
    from ezdxf.addons.drawing import pymupdf as pdf_backend
    from ezdxf.math import BoundingBox2d

    class CachedViewFrontend(Frontend):
        """Honor the source's proxy-to-viewport association for cached views."""

        def draw_viewport(self, viewport: Any) -> None:
            original_visibility = []
            for item in report["preview_placements"]:
                if item["owner_layout"] != "Model":
                    continue
                entity = doc.entitydb[item["exposed_handle"]]
                original_visibility.append((entity, entity.dxf.get("invisible", 0)))
                entity.dxf.invisible = int(
                    item["viewport_handle"] != viewport.dxf.handle
                )
            try:
                super().draw_viewport(viewport)
            finally:
                for entity, visibility in original_visibility:
                    entity.dxf.invisible = visibility

    catalogue = load_catalogue(root)
    catalogue["processing"] = {
        "date": "2026-09-14",
        "python": platform.python_version(),
        "oda_file_converter": "27.1.0",
        "output": "ACAD2018 ASCII DXF; audit=0",
        "ezdxf": ezdxf.__version__,
        "pymupdf": pymupdf.VersionBind,
        "script": artifact(Path("scripts/shg_designs.py"), root),
        "reference_rendering": {
            "status": "unverified",
            "engine": None,
            "reason": "No independent authoring-engine reference available",
        },
    }
    for design in catalogue["designs"]:
        ident = design["id"]
        if only is not None and ident not in only:
            continue
        source = directory / f"{ident}.dxf"
        if not source.exists():
            raise FileNotFoundError(source)
        raw_dxf = source.read_bytes()
        outdir = DATA / "processed" / ident
        (root / outdir).mkdir(parents=True, exist_ok=True)
        compressed = outdir / f"{ident}.dxf.gz"
        (root / compressed).write_bytes(gzip_bytes(raw_dxf))
        design["dxf"] = {
            **artifact(compressed, root),
            "uncompressed_sha256": sha256(raw_dxf),
            "uncompressed_bytes": len(raw_dxf),
            "content_type": "application/gzip",
            "format": "ASCII DXF AC1032 (gzip compressed)",
        }
        doc = ezdxf.readfile(source)
        report = inspect_document(doc)
        source_report = (
            json.loads((root / design["source_inspection"]["path"]).read_text())
            if "source_inspection" in design
            else None
        )
        report.update(
            {
                "design_id": ident,
                "source_sha256": design["source"]["sha256"],
                "dxf_sha256": sha256(raw_dxf),
                "fidelity": "unverified",
                "source_entity_counts": (
                    source_report["source_entity_counts"] if source_report else None
                ),
                "source_count_status": (
                    "independent_reader_counts_not_visual_validation"
                    if source_report
                    else "not_available"
                ),
                "unsupported_native_solids": report["entity_counts"].get("3DSOLID", 0),
                "warnings": [
                    "Inventor semantics beyond the observed proxy variant are opaque.",
                    "Restricted proxy-origin decoding and viewport clipping are used; "
                    "fidelity is unverified.",
                    "AIGDT unavailable: engineering symbols may appear as letters.",
                    "No independent CAD rendering; not certified machining drawings.",
                    "ODA may reset DXF header dates; they are not original DWG dates.",
                ],
            }
        )
        if source_report:
            before = source_report["source_entity_counts"]
            report["entity_count_deltas"] = {
                kind: report["entity_counts"].get(kind, 0) - count
                for kind, count in before.items()
                if kind != "UNKNOWN_ENT"
                and report["entity_counts"].get(kind, 0) != count
            }
            report["proxy_count_comparison"] = {
                "source_unknown_entities": before.get("UNKNOWN_ENT", 0),
                "dxf_proxy_entities": report["entity_counts"].get(
                    "ACAD_PROXY_ENTITY", 0
                ),
                "note": "Reader type names differ; equal counts do not prove fidelity",
            }
        design["units"] = {
            "insunits_code": doc.units,
            "native": "mm" if doc.units == 4 else "OPEN",
            "metres_per_unit": 0.001 if doc.units == 4 else None,
            "evidence": "DXF $INSUNITS and independent source-reader INSUNITS",
            "source_reader_code": (
                source_report["header_units"] if source_report else None
            ),
        }
        report["preview_placements"] = resolve_cached_blocks(doc)
        previews = []
        assets = ASSETS / ident
        (root / assets).mkdir(parents=True, exist_ok=True)
        cfg = config.Configuration(
            background_policy=config.BackgroundPolicy.WHITE,
            color_policy=config.ColorPolicy.BLACK,
        )
        for index, sheet in enumerate((s for s in doc.layouts if s.name != "Model"), 1):
            qualifies, reason = layout_content(sheet)
            record = {
                "id": f"sheet-{index:02d}",
                "name": sheet.name,
                "qualifies": qualifies,
                "reason": reason,
                "fidelity": "unverified",
                "svg": None,
                "pdf": None,
                "png": None,
            }
            if qualifies:
                paper = sheet.dxf_layout.dxf
                width = paper.get("paper_width", 420)
                height = paper.get("paper_height", 297)
                if paper.get("plot_rotation", 0) % 2:
                    width, height = height, width
                record["paper_size_native"] = [width, height]
                render_box = BoundingBox2d([(0, 0), (width, height)])
                for fmt in ("svg", "pdf"):
                    backend = (
                        svg.SVGBackend()
                        if fmt == "svg"
                        else pdf_backend.PyMuPdfBackend()
                    )
                    CachedViewFrontend(
                        RenderContext(doc), backend, config=cfg
                    ).draw_layout(sheet)
                    page = layout.Page(width, height, margins=layout.Margins.all(6))
                    settings = layout.Settings(crop_at_margins=True)
                    target = assets / f"sheet-{index:02d}.{fmt}"
                    output = (
                        backend.get_string(
                            page, settings=settings, render_box=render_box
                        ).encode()
                        if fmt == "svg"
                        else backend.get_pdf_bytes(
                            page, settings=settings, render_box=render_box
                        )
                    )
                    if fmt == "svg":
                        document = ET.fromstring(output)
                        namespace = "http://www.w3.org/2000/svg"
                        viewbox_width = float(document.attrib["viewBox"].split()[2])
                        notice = ET.SubElement(
                            document,
                            f"{{{namespace}}}text",
                            {
                                "x": str(viewbox_width * 0.017),
                                "y": str(viewbox_width * 0.009),
                                "font-size": str(viewbox_width * 0.0045),
                                "fill": "#333",
                                "font-family": "sans-serif",
                            },
                        )
                        notice.text = PREVIEW_NOTICE
                        output = ET.tostring(
                            document, encoding="utf-8", xml_declaration=True
                        )
                    if fmt == "pdf":
                        # Remove volatile metadata and add a visible derivative notice.
                        pdf = pymupdf.open(stream=output, filetype="pdf")
                        pdf.set_metadata(
                            {
                                "title": f"{ident} - {sheet.name}",
                                "author": "AG Schaetz",
                                "subject": "CERN-OHL-S-2.0; unverified preview",
                                "creator": "scripts/shg_designs.py",
                            }
                        )
                        pdf[0].insert_text(
                            (20, 12),
                            PREVIEW_NOTICE,
                            fontsize=6,
                        )
                        stable_id = sha256(
                            (design["source"]["sha256"] + sheet.name).encode()
                        )[:32]
                        pdf.xref_set_key(-1, "ID", f"[<{stable_id}><{stable_id}>]")
                        output = pdf.tobytes(no_new_id=True, garbage=4, deflate=True)
                    (root / target).write_bytes(output)
                    record[fmt] = artifact(target, root)
                pdf = pymupdf.open(root / record["pdf"]["path"])
                png = assets / f"sheet-{index:02d}.png"
                pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(root / png)
                record["png"] = artifact(png, root)
            previews.append(record)
        design["previews"] = previews
        report["layouts"] = previews
        report["model_space"] = {
            "status": "cached_views_represented_on_sheets",
            "native_3d_model_verified": False,
        }
        report_path = outdir / "inspection.json"
        (root / report_path).write_bytes(json_bytes(report))
        design["inspection"] = artifact(report_path, root)
        print(
            f"{ident}: {len(previews)} layouts; "
            f"{len(report['annotations'])} annotations",
            flush=True,
        )
    save_catalogue(catalogue, root)


def safe_file(root: Path, relative: str) -> Path:
    """Reject artifact paths escaping the repository root."""
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes repository: {relative}")
    return path


def validate(catalogue: dict[str, Any], root: Path = ROOT) -> None:
    """Validate schema, identities, provenance and every linked artifact."""
    schema = json.loads((root / SCHEMA).read_text())
    Draft202012Validator(schema).validate(catalogue)
    ids = [d["id"] for d in catalogue["designs"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate design IDs")
    for design in catalogue["designs"]:
        if (
            design["hardware_association"]["status"] == "confirmed"
            and not design["hardware_association"]["bench_evidence"]
        ):
            raise ValueError(f"Bench evidence required for {design['id']}")
        for record in [
            design["source"],
            design["dxf"],
            design["inspection"],
            design["source_inspection"],
            design["source_json"],
        ] + [
            p[fmt]
            for p in design["previews"]
            for fmt in ("svg", "pdf", "png")
            if p[fmt]
        ]:
            payload = safe_file(root, record["path"]).read_bytes()
            if sha256(payload) != record["sha256"] or len(payload) != record["bytes"]:
                raise ValueError(f"Artifact checksum mismatch: {record['path']}")
        for key in ("dxf", "source_json"):
            record = design[key]
            content = gzip.decompress((root / record["path"]).read_bytes())
            if (
                sha256(content) != record["uncompressed_sha256"]
                or len(content) != record["uncompressed_bytes"]
            ):
                raise ValueError(f"{key} content mismatch: {design['id']}")


def generated_files(catalogue: dict[str, Any]) -> dict[Path, bytes]:
    """Generate identical public records for Jekyll and programmatic clients."""
    return {
        Path("docs/_data/shg.yml"): yaml.safe_dump(
            catalogue, allow_unicode=True, sort_keys=False, width=92
        ).encode(),
        ASSETS / "catalogue.json": json_bytes(catalogue),
    }


def publish_records(check: bool = False, root: Path = ROOT) -> None:
    """Write generated records, or fail if they differ from canonical YAML."""
    catalogue = load_catalogue(root)
    validate(catalogue, root)
    outputs = generated_files(catalogue)
    outputs[ASSETS / "catalogue.schema.json"] = (root / SCHEMA).read_bytes()
    for path, data in outputs.items():
        destination = root / path
        if check:
            if not destination.exists() or destination.read_bytes() != data:
                raise ValueError(f"Stale generated catalogue: {path}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)


def main() -> None:
    """Execute a single explicit import, conversion, processing or sync step."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("ingest").add_argument("archive", type=Path)
    conversion = commands.add_parser("convert")
    conversion.add_argument("--oda", required=True, type=Path)
    conversion.add_argument("--output", required=True, type=Path)
    processing = commands.add_parser("process")
    processing.add_argument("exports", type=Path)
    processing.add_argument(
        "--only", help="Comma-separated design IDs for a bounded rerender"
    )
    commands.add_parser("inspect-source").add_argument(
        "--reader", required=True, type=Path
    )
    commands.add_parser("site")
    commands.add_parser("check")
    args = parser.parse_args()
    if args.command == "ingest":
        ingest(args.archive)
    elif args.command == "convert":
        convert(args.oda, args.output)
    elif args.command == "process":
        process_exports(
            args.exports, only=set(args.only.split(",")) if args.only else None
        )
    elif args.command == "inspect-source":
        inspect_sources(args.reader)
    else:
        publish_records(check=args.command == "check")


if __name__ == "__main__":
    main()
