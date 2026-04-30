"""
test_diagnostic_surrogate_imports.py
=====================================

Mechanical enforcement of CHARTER §5.1 diagnostic-surrogate exception clause (d):

    "no import path into production simulation code (prevents accidental reuse)"

This test fails the build if any production module under /src/ (excluding
/src/diagnostic_surrogates_archive/ itself) imports from the diagnostic
surrogates archive subtree.

Per CHARTER §5.1 (v0.9 Integrator mechanical-enforcement clause), the
Integrator confirms this enforcement at G1 closure. This test is the
mechanism that confirmation refers to.

Invocation:  pytest tests/test_diagnostic_surrogate_imports.py
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
ARCHIVE_DIR_NAME = "diagnostic_surrogates_archive"

# Patterns that indicate an import from the archive subtree
_IMPORT_PATTERNS = [
    re.compile(r"^\s*import\s+(?:src\.)?diagnostic_surrogates_archive\b", re.MULTILINE),
    re.compile(r"^\s*from\s+(?:src\.)?diagnostic_surrogates_archive\b", re.MULTILINE),
    re.compile(r"^\s*import\s+\.diagnostic_surrogates_archive\b", re.MULTILINE),
    re.compile(r"^\s*from\s+\.diagnostic_surrogates_archive\b", re.MULTILINE),
]


def _python_files_in_src_excluding_archive() -> list[Path]:
    """Yield all .py files under /src/ except those inside the archive subtree."""
    if not SRC_DIR.exists():
        return []
    archive = SRC_DIR / ARCHIVE_DIR_NAME
    return [
        p
        for p in SRC_DIR.rglob("*.py")
        if archive not in p.parents and p != archive
    ]


def test_no_production_imports_from_diagnostic_surrogates_archive() -> None:
    """
    CHARTER §5.1 (d): production simulation code in /src/ must not import
    from /src/diagnostic_surrogates_archive/.

    A failure of this test means a diagnostic-surrogate import path has
    leaked into production code, which violates the anti-bias intent of
    G1 and triggers Architect veto per CHARTER §5.1.
    """
    offenders: list[tuple[Path, str]] = []

    for py_file in _python_files_in_src_excluding_archive():
        try:
            text = py_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            # Unreadable file: surface as a separate test concern, not here.
            continue

        for pattern in _IMPORT_PATTERNS:
            match = pattern.search(text)
            if match is not None:
                rel = py_file.relative_to(REPO_ROOT)
                offenders.append((rel, match.group(0).strip()))
                break  # one finding per file is enough

    if offenders:
        lines = [
            "Production code imports from /src/diagnostic_surrogates_archive/ — "
            "this violates CHARTER §5.1 (d) and triggers Architect veto.",
            "",
            "Offending imports:",
        ]
        for path, statement in offenders:
            lines.append(f"  {path}: {statement}")
        lines.append("")
        lines.append(
            "Resolution: either remove the import, or — if the work is "
            "genuinely production-grade — promote the archived module out "
            "of the surrogate subtree under Council-3 deliberation per "
            "CHARTER §9 (architectural decision)."
        )
        pytest.fail("\n".join(lines))
