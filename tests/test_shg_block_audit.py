"""Regression contracts for the SHG template-block investigation.

SPDX-License-Identifier: MIT
"""

import json
from pathlib import Path

import pytest

from scripts import shg_block_audit as audit
from scripts import shg_designs as shg


def test_recorded_audit_covers_all_conversion_deficits() -> None:
    report = json.loads((shg.ROOT / audit.OUTPUT).read_text())
    assert shg.load_catalogue()["block_audit"] == shg.artifact(audit.OUTPUT)
    designs = {d["id"]: d for d in shg.load_catalogue()["designs"]}
    expected = set()
    for design in shg.load_catalogue()["designs"]:
        inspection = json.loads((shg.ROOT / design["inspection"]["path"]).read_text())
        if inspection.get("entity_count_deltas"):
            expected.add(design["id"])
    assert {r["design_id"] for r in report["results"]} == expected
    for result in report["results"]:
        design = designs[result["design_id"]]
        for key in ("source_json", "dxf", "inspection"):
            assert result[f"{key}_sha256"] == design[key]["sha256"]
    assert report["tool"] == shg.artifact(Path("scripts/shg_block_audit.py"))


def test_content_fingerprint_retains_geometry_and_ignores_storage_fields() -> None:
    a = [{"entity": "LINE", "handle": [0, 1, 10], "start": [0, 0, 0]}]
    b = [{"entity": "LINE", "handle": [0, 1, 11], "start": [0, 0, 0]}]
    assert audit.content_fingerprint(a) == audit.content_fingerprint(b)
    b[0]["start"] = [1, 0, 0]
    assert audit.content_fingerprint(a) != audit.content_fingerprint(b)


def test_block_audit_regenerates_from_published_artifacts() -> None:
    pytest.importorskip("ezdxf", reason="Install .[test,shg] for CAD block audit")
    assert audit.generate() == json.loads((shg.ROOT / audit.OUTPUT).read_text())
