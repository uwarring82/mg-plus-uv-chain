"""Contracts for SHG provenance, proxy decoding and catalogue generation.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import copy
import gzip
import json
import zipfile
from pathlib import Path

import pytest
import yaml

from scripts import shg_designs as shg


def test_catalogue_and_generated_files_are_current() -> None:
    """Every published record must point to the exact archived file bytes."""
    shg.publish_records(check=True)


def test_confirmation_requires_bench_evidence() -> None:
    catalogue = copy.deepcopy(shg.load_catalogue())
    catalogue["designs"][0]["hardware_association"]["status"] = "confirmed"
    with pytest.raises(ValueError, match="Bench evidence required"):
        shg.validate(catalogue)


def test_duplicate_design_ids_are_rejected() -> None:
    catalogue = copy.deepcopy(shg.load_catalogue())
    catalogue["designs"][1]["id"] = catalogue["designs"][0]["id"]
    with pytest.raises(ValueError, match="Duplicate design IDs"):
        shg.validate(catalogue)


def test_checksum_detects_source_record_corruption() -> None:
    catalogue = copy.deepcopy(shg.load_catalogue())
    catalogue["designs"][0]["source"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="checksum mismatch"):
        shg.validate(catalogue)


def test_paths_cannot_escape_repository(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="escapes repository"):
        shg.safe_file(tmp_path, "../external-file")


def test_legacy_zip_filename_is_recovered_losslessly() -> None:
    original = "SHG/befestigung durchfu\u0308hrungen.dwg"
    entry = zipfile.ZipInfo(original.encode("utf-8").decode("cp437"))
    restored, raw_hex = shg.archive_name(entry)
    assert restored == original
    assert bytes.fromhex(raw_hex) == original.encode("utf-8")


def test_ingest_preserves_bytes_and_refuses_replacement(tmp_path: Path) -> None:
    base = tmp_path / shg.DATA
    base.mkdir(parents=True)
    (tmp_path / shg.CATALOGUE).write_text(
        yaml.safe_dump(
            {"designs": [{"id": "SHG-901", "original_filename": "example.dwg"}]}
        )
    )
    archive = tmp_path / "example.zip"
    original = b"AC1032\x00original opaque drawing"
    with zipfile.ZipFile(archive, "w") as output:
        output.writestr("SHG/example.dwg", original)
        output.writestr("SHG/.DS_Store", b"discard")
    shg.ingest(archive, root=tmp_path)
    stored = base / "raw/SHG-901.dwg"
    assert stored.read_bytes() == original
    assert not (base / "raw/.DS_Store").exists()
    stored.write_bytes(b"different existing drawing")
    with pytest.raises(ValueError, match="Refusing to replace"):
        shg.ingest(archive, root=tmp_path)


def test_gzip_is_deterministic_and_lossless() -> None:
    content = b"0\nSECTION\n2\nENTITIES\n0\nENDSEC\n0\nEOF\n"
    encoded = shg.gzip_bytes(content)
    assert shg.gzip_bytes(content) == encoded
    assert gzip.decompress(encoded) == content
    assert encoded[4:8] == b"\0\0\0\0"


def test_proxy_position_uses_stored_origin_not_view_center_guess() -> None:
    # SHG-001 source proxy 1DB: coordinates independently exposed in its DXF.
    point = shg.cached_insert_point(
        bytes.fromhex("00001000200af130000004000c0ffc3c0ba900"), 145
    )
    assert point == pytest.approx((-10327.000007629395, -10239.500007629395, 0.0))
    assert shg.cached_insert_point(bytes.fromhex("aba900"), 17) == (0.0, 0.0, 0.0)


def test_unfamiliar_or_truncated_proxy_transforms_fail_closed() -> None:
    with pytest.raises(ValueError):
        shg.cached_insert_point(b"\0", 145)
    with pytest.raises(ValueError, match="Unsupported cached-block"):
        shg.cached_insert_point(bytes.fromhex("aba980"), 17)


def test_default_viewport_alone_does_not_qualify() -> None:
    ezdxf = pytest.importorskip("ezdxf")
    drawing = ezdxf.new()
    sheet = drawing.layouts.get("Layout1")
    sheet.add_viewport((100, 100), (200, 200), (0, 0), 200, status=1)
    assert shg.layout_content(sheet) == (False, "empty_layout_or_viewport_only")
    sheet.add_line((0, 0), (20, 20))
    assert shg.layout_content(sheet)[0]


def test_metadata_formats_carry_the_same_records() -> None:
    catalogue = shg.load_catalogue()
    generated = shg.generated_files(catalogue)
    assert json.loads(generated[shg.ASSETS / "catalogue.json"]) == catalogue
    assert yaml.safe_load(generated[Path("docs/_data/shg.yml")]) == catalogue


def test_viewport_requires_visible_model_content() -> None:
    ezdxf = pytest.importorskip("ezdxf")
    drawing = ezdxf.new()
    sheet = drawing.layouts.get("Layout1")
    viewport = sheet.add_viewport((100, 100), (200, 200), (0, 0), 200, status=2)
    line = drawing.modelspace().add_line((1000, 1000), (1020, 1020))
    assert not shg.layout_content(sheet)[0]
    line.dxf.start, line.dxf.end = (0, 0), (20, 20)
    assert shg.layout_content(sheet)[0]
    viewport.dxf.status = -1
    assert not shg.layout_content(sheet)[0]
    viewport.dxf.status = 2
    drawing.layers.new("hidden-model").off()
    line.dxf.layer = "hidden-model"
    assert not shg.layout_content(sheet)[0]


def test_generated_data_staleness_is_rejected(tmp_path: Path, monkeypatch) -> None:
    catalogue = shg.load_catalogue()
    (tmp_path / shg.DATA).mkdir(parents=True)
    (tmp_path / shg.SCHEMA).write_bytes((shg.ROOT / shg.SCHEMA).read_bytes())
    shg.save_catalogue(catalogue, tmp_path)
    # Hash validation has its own tests; isolate the generated-data contract.
    monkeypatch.setattr(shg, "validate", lambda *args: None)
    shg.publish_records(root=tmp_path)
    (tmp_path / shg.ASSETS / "catalogue.json").write_text("{}\n")
    with pytest.raises(ValueError, match="Stale generated catalogue"):
        shg.publish_records(check=True, root=tmp_path)
