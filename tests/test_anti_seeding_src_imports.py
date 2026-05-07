"""
test_anti_seeding_src_imports.py
================================

Mechanical enforcement of CHARTER §5.1 anti-seeding clause:
no production module under /src/ may import from ``data.literature``.

This prevents architecture-specific parameter values from leaking into
the generic pre-G1 simulation code. Kept separate from
``test_diagnostic_surrogate_imports.py`` (which serves the CHARTER §5.1
clause-d diagnostic-surrogate purpose) so the two enforcement
mechanisms remain cleanly isolated.

Invocation:  pytest tests/test_anti_seeding_src_imports.py
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"

_IMPORT_PATTERNS = [
    re.compile(r"^\s*import\s+(?:src\.)?data\.literature\b", re.MULTILINE),
    re.compile(r"^\s*from\s+(?:src\.)?data\.literature\b", re.MULTILINE),
    re.compile(r"^\s*import\s+\.data\.literature\b", re.MULTILINE),
    re.compile(r"^\s*from\s+\.data\.literature\b", re.MULTILINE),
]


def _python_files_in_src() -> list[Path]:
    if not SRC_DIR.exists():
        return []
    return list(SRC_DIR.rglob("*.py"))


def test_no_production_imports_from_data_literature() -> None:
    """
    CHARTER §5.1: production simulation code in /src/ must not import
    from data.literature.

    A failure of this test means an architecture-specific import path has
    leaked into production code, which violates the anti-seeding intent of
    G1 and triggers Architect veto per CHARTER §5.1.
    """
    offenders: list[tuple[Path, str]] = []

    for py_file in _python_files_in_src():
        try:
            text = py_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for pattern in _IMPORT_PATTERNS:
            match = pattern.search(text)
            if match is not None:
                rel = py_file.relative_to(REPO_ROOT)
                offenders.append((rel, match.group(0).strip()))
                break

    if offenders:
        lines = [
            "Production code imports from data.literature — "
            "this violates CHARTER §5.1 anti-seeding and triggers Architect veto.",
            "",
            "Offending imports:",
        ]
        for path, statement in offenders:
            lines.append(f"  {path}: {statement}")
        lines.append("")
        lines.append(
            "Resolution: move architecture-specific imports to /notebooks/; "
            "/src/ must remain wavelength-, material-, and architecture-neutral."
        )
        pytest.fail("\n".join(lines))
