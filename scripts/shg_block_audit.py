"""Account for omitted SHG blocks using published source JSON and DXF exports.

SPDX-License-Identifier: MIT
Run as: python -m scripts.shg_block_audit [--check]
Requires the shg extra. Does not convert or modify any drawing.
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
from collections import Counter
from pathlib import Path
from typing import Any

from scripts import shg_designs as shg

OUTPUT = shg.DATA / "block-audit.json"
STORAGE_FIELDS = {"index", "handle", "ownerhandle", "size", "bitsize"}


def content_fingerprint(entities: list[dict[str, Any]]) -> str:
    """Compare decoded content in source order, excluding storage bookkeeping.

    Geometry, text, styles and other references are retained. This detects
    this collection's repeated template payload, not general CAD equivalence.
    """
    payload = [
        {k: v for k, v in e.items() if k not in STORAGE_FIELDS} for e in entities
    ]
    return shg.sha256(json.dumps(payload, sort_keys=True, allow_nan=False).encode())


def compare_blocks(graph: dict[str, Any], doc: Any) -> dict[str, Any]:
    """Match block records by preserved handle; anonymous names are not unique."""
    from ezdxf.tools.text import plain_mtext

    objects = {o["handle"][2]: o for o in graph["OBJECTS"]}
    headers = [o for o in objects.values() if o.get("object") == "BLOCK_HEADER"]
    dxf_blocks = {int(b.block_record.dxf.handle, 16): b for b in doc.blocks}
    mapping = []
    omitted = []
    accounted: Counter[str] = Counter()
    for header in headers:
        handle = header["handle"][2]
        block = dxf_blocks.get(handle)
        mapping.append(
            {
                "source_handle": f"{handle:X}",
                "source_name": header["name"],
                "dxf_name": block.name if block is not None else None,
            }
        )
        if block is not None:
            continue
        member_handles = [ref[-1] for ref in header.get("entities", [])]
        entities = [objects[h] for h in member_handles]
        boundary_handles = [header[k][-1] for k in ("block_entity", "endblk_entity")]
        counts = Counter(e["entity"] for e in entities)
        counts.update(objects[h]["entity"] for h in boundary_handles)
        # A removed header alone cannot explain a deficit if its members survive.
        if any(f"{h:X}" in doc.entitydb for h in member_handles + boundary_handles):
            raise ValueError(f"Partially retained omitted block {handle:X}")
        accounted.update(counts)
        backlinks = [r[-1] for r in header.get("inserts", [])]
        explicit_inserts = [
            o["handle"][2]
            for o in objects.values()
            if o.get("entity") in {"INSERT", "MINSERT"}
            and o.get("block_header", [None])[-1] == handle
        ]
        omitted.append(
            {
                "source_handle": f"{handle:X}",
                "source_name": header["name"],
                "member_handles": [f"{h:X}" for h in member_handles],
                "boundary_handles": [f"{h:X}" for h in boundary_handles],
                "entity_counts_including_boundaries": dict(sorted(counts.items())),
                "content_sha256": content_fingerprint(entities),
                "mtext_labels": [
                    {"handle": f"{e['handle'][2]:X}", "text": plain_mtext(e["text"])}
                    for e in entities
                    if e.get("entity") == "MTEXT"
                ],
                "insert_backlinks": [
                    {"handle": f"{h:X}", "present_in_source_graph": h in objects}
                    for h in backlinks
                ],
                "explicit_source_insert_handles": [f"{h:X}" for h in explicit_inserts],
            }
        )
    return {
        "block_name_mapping": mapping,
        "omitted_blocks": omitted,
        "accounted_entity_deficit": dict(sorted(accounted.items())),
        "reference_limit": (
            "Backlinks and explicit INSERTs checked in decoded graph only; "
            "opaque Inventor proxy references and rendered visibility unverified"
        ),
    }


def generate() -> dict[str, Any]:
    """Audit every drawing with a reported source-to-DXF entity deficit."""
    import ezdxf

    catalogue = shg.load_catalogue()
    results = []
    for design in catalogue["designs"]:
        inspection = json.loads((shg.ROOT / design["inspection"]["path"]).read_text())
        delta = inspection.get("entity_count_deltas", {})
        if not delta:
            continue
        graph = json.loads(
            gzip.decompress((shg.ROOT / design["source_json"]["path"]).read_bytes())
        )
        dxf = gzip.decompress((shg.ROOT / design["dxf"]["path"]).read_bytes())
        # DXF CRLFs must be normalized as they are by readfile's text stream.
        doc = ezdxf.read(io.StringIO(dxf.decode("utf-8"), newline=None))
        report = compare_blocks(graph, doc)
        deficit = {kind: -value for kind, value in delta.items()}
        if report["accounted_entity_deficit"] != deficit:
            raise ValueError(f"Omitted blocks do not explain {design['id']} deficit")
        results.append(
            {
                "design_id": design["id"],
                "source_json_sha256": design["source_json"]["sha256"],
                "dxf_sha256": design["dxf"]["sha256"],
                "inspection_sha256": design["inspection"]["sha256"],
                "matches_full_reported_deficit": True,
                **report,
            }
        )
    return {
        "schema_version": "1.0.0",
        "licence": "CC-BY-4.0",
        "method": "Preserved-handle block matching, decoded content and backlink audit",
        "tool": shg.artifact(Path("scripts/shg_block_audit.py")),
        "ezdxf_version": ezdxf.__version__,
        "scope": "Every catalogue drawing with an entity_count_deltas entry",
        "interpretation": (
            "D3 is a repeated sheet border; FC is a repeated historical title block. "
            "This identifies the omitted content; it does not certify fidelity."
        ),
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = generate()
    payload = shg.json_bytes(report)
    destination = shg.ROOT / OUTPUT
    if args.check:
        if destination.read_bytes() != payload:
            raise ValueError(f"Stale block audit: {OUTPUT}")
    else:
        destination.write_bytes(payload)
    print(
        f"Accounted for complete entity deficits in {len(report['results'])} drawings"
    )


if __name__ == "__main__":
    main()
