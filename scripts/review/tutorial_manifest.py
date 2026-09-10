"""Map tutorial inputs and outputs to the reviewed baseline and environment.

Run from the repository root: python -m scripts.review.tutorial_manifest
"""

from __future__ import annotations

import argparse
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


def manifest(
    stem: str = "",
    environment: Path = Path("data/review/2026-09-09/environment.txt"),
) -> dict:
    """Return exact input/output hashes and before/after printed results."""
    sources = sorted(
        p for p in Path("notebooks/tutorials").glob("*.py") if p.stem.startswith(stem)
    )
    if not sources:
        raise ValueError(f"No tutorial matches prefix {stem!r}")
    inputs = sorted(
        [
            *sources,
            *Path("notebooks/tutorials").glob("*.yaml"),
            *Path("src").glob("*.py"),
            Path("scripts/render_tutorials.py"),
            Path("scripts/check_colab_tutorials.py"),
            Path("pyproject.toml"),
            Path(__file__).relative_to(Path.cwd()),
            environment,
        ]
    )
    tutorials = []
    for source in sources:
        nb_path = Path("docs/tutorials") / f"{source.stem}.ipynb"
        html_path = nb_path.with_suffix(".html")
        baseline_paths = subprocess.check_output(
            ["git", "ls-tree", "--name-only", BASELINE, "--", str(nb_path)],
            text=True,
        ).splitlines()
        before = before_html = None
        if str(nb_path) in baseline_paths:
            before = subprocess.check_output(["git", "show", f"{BASELINE}:{nb_path}"])
            before_html = subprocess.check_output(
                ["git", "show", f"{BASELINE}:{html_path}"]
            )
        tutorials.append(
            {
                "source": str(source),
                "ipynb": str(nb_path),
                "html": str(html_path),
                "before_ipynb_sha256": (
                    hashlib.sha256(before).hexdigest() if before is not None else None
                ),
                "after_ipynb_sha256": _sha(nb_path),
                "before_html_sha256": (
                    hashlib.sha256(before_html).hexdigest()
                    if before_html is not None
                    else None
                ),
                "after_html_sha256": _sha(html_path),
                "before_printed_results": (
                    _printed(json.loads(before)) if before is not None else None
                ),
                "after_printed_results": _printed(json.loads(nb_path.read_text())),
            }
        )
    return {
        "baseline_revision": BASELINE,
        "environment_record": str(environment),
        "inputs_sha256": {str(path): _sha(path) for path in inputs},
        "tutorials": tutorials,
        "comparison_note": (
            "Baseline notebooks have no embedded plots (plain Agg backend). "
            "Inline rendering now includes the figures; printed results "
            "compare scalars and hashes identify all outputs. Null before fields "
            "mean a tutorial did not exist at the baseline."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stem", default="", help="Optional tutorial prefix")
    parser.add_argument(
        "--environment",
        type=Path,
        default=Path("data/review/2026-09-09/environment.txt"),
        help="Recorded environment used for the selected rendered outputs",
    )
    args = parser.parse_args()
    print(json.dumps(manifest(args.stem, args.environment), indent=2))
