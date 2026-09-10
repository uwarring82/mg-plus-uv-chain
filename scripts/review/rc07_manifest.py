"""Print the RC-07 input/output manifest from the repository root."""

import hashlib
import json
import subprocess
from pathlib import Path

from scripts.review.render_rc07 import SOURCES

BASELINE = "4404074d5114ecf7515a2cbd71910c16c036359d"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest() -> dict:
    """Record exact source hashes and all changed executed outputs."""
    inputs = [Path(s) for s in SOURCES] + [
        Path("notebooks/tutorials/04-cascade-shg.py"),
        Path("notebooks/tutorials/04-params.yaml"),
        Path("scripts/render_tutorials.py"),
        Path("scripts/review/render_rc07.py"),
        Path("scripts/review/rc07_manifest.py"),
        Path("scripts/review/cavity_fits.py"),
        Path("data/literature/Friedenauer2006/extracted.yaml"),
        Path("data/review/2026-09-09/environment.txt"),
        Path("tests/test_rc07_recalculation.py"),
        *sorted(Path("src").glob("*.py")),
    ]
    outputs = sorted(Path("docs/review").glob("*.ipynb")) + [
        Path("docs/tutorials/04-cascade-shg.ipynb")
    ]
    records = []
    for nb_path in outputs:
        nb = json.loads(nb_path.read_text())
        records.append(
            {
                "notebook": str(nb_path),
                "notebook_sha256": sha(nb_path),
                "html": str(nb_path.with_suffix(".html")),
                "html_sha256": sha(nb_path.with_suffix(".html")),
                "printed_results": [
                    "".join(o.get("text", []))
                    for c in nb["cells"]
                    for o in c.get("outputs", [])
                    if o.get("name") == "stdout"
                ],
                "figures": sum(
                    "image/png" in o.get("data", {})
                    for c in nb["cells"]
                    for o in c.get("outputs", [])
                ),
            }
        )
    prior = {}
    for path in inputs:
        result = subprocess.run(
            ["git", "show", f"{BASELINE}:{path}"], capture_output=True
        )
        if result.returncode == 0:
            prior[str(path)] = hashlib.sha256(result.stdout).hexdigest()
    return {
        "baseline_revision": BASELINE,
        "provenance": "Inputs and outputs are filed together; "
        "hashes specify the changed tree.",
        "input_sha256": {str(p): sha(p) for p in inputs},
        "baseline_input_sha256": prior,
        "results_json_sha256": sha(Path("data/review/2026-09-10/rc07-results.json")),
        "outputs": records,
        "comparison": "Numerical before/after cases are in rc07-results.json. "
        "Historical review notebooks had no committed rendered baseline; "
        "the May IC sweep replays frozen inputs rather than new targets.",
    }


if __name__ == "__main__":
    print(json.dumps(manifest(), indent=2))
