"""Render the RC-07 source notebooks from the repository root."""

from scripts.render_tutorials import REPO_ROOT, render

SOURCES = [
    "notebooks/2026-05-01-friedenauer-bk-recalculation.py",
    "notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py",
    "notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py",
    "notebooks/exploration/2026-09-10-rc07-recalculation.py",
]

if __name__ == "__main__":
    raise SystemExit(
        render(
            source_paths=[REPO_ROOT / p for p in SOURCES],
            output_dir=REPO_ROOT / "docs/review",
            description="Dated pre-G1 exploratory recalculation; no design approval.",
            repo_links=True,
        )
    )
