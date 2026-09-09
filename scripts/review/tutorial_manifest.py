"""Map tutorial inputs and outputs to the reviewed baseline and environment.

Run from the repository root: python -m scripts.review.tutorial_manifest
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

BASELINE = "9a498165532e029e1ba0706d380f760402dd7584"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _printed(nb: dict) -> list[str]:
    return [
        "".join(output.get("text", []))
        for cell in nb["cells"]
        for output in cell.get("outputs", [])
        if output.get("output_type") == "stream" and output.get("name") == "stdout"
    ]


def manifest() -> dict:
    """Return exact input/output hashes and before/after printed results."""
    inputs = sorted(
        [
            *Path("notebooks/tutorials").glob("*.py"),
            *Path("notebooks/tutorials").glob("*.yaml"),
            *Path("src").glob("*.py"),
            Path("scripts/render_tutorials.py"),
            Path(__file__).relative_to(Path.cwd()),
            Path("data/review/2026-09-09/environment.txt"),
        ]
    )
    tutorials = []
    for source in sorted(Path("notebooks/tutorials").glob("*.py")):
        nb_path = Path("docs/tutorials") / f"{source.stem}.ipynb"
        html_path = nb_path.with_suffix(".html")
        before = subprocess.check_output(
            ["git", "show", f"{BASELINE}:{nb_path}"], text=True
        )
        before_html = subprocess.check_output(
            ["git", "show", f"{BASELINE}:{html_path}"]
        )
        tutorials.append(
            {
                "source": str(source),
                "ipynb": str(nb_path),
                "html": str(html_path),
                "before_ipynb_sha256": hashlib.sha256(before.encode()).hexdigest(),
                "after_ipynb_sha256": _sha(nb_path),
                "before_html_sha256": hashlib.sha256(before_html).hexdigest(),
                "after_html_sha256": _sha(html_path),
                "before_printed_results": _printed(json.loads(before)),
                "after_printed_results": _printed(json.loads(nb_path.read_text())),
            }
        )
    return {
        "baseline_revision": BASELINE,
        "inputs_sha256": {str(path): _sha(path) for path in inputs},
        "tutorials": tutorials,
        "comparison_note": (
            "Baseline notebooks have no embedded plots (plain Agg backend). "
            "Inline rendering now includes the figures; printed results "
            "compare scalars and hashes identify all outputs."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(manifest(), indent=2))
