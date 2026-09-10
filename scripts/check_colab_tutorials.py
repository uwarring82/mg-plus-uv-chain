"""Opt-in fresh-runtime checks for the four Colab tutorial notebooks.

Run from the repository root with the notebook dependencies installed:
    python scripts/check_colab_tutorials.py

Creates a temporary environment, installs ipykernel, then executes each
notebook outside any checkout. Its setup cell must fetch the pinned public
repository and install its own scientific dependencies. Requires network
access; deliberately separate from pytest collection and the core suite.
This checks the bootstrap path, not Google's hosted runtime or sign-in UI.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import jupytext
import nbformat
from jupyter_client.kernelspec import KernelSpecManager
from nbclient import NotebookClient

REPO_ROOT: Path = Path(__file__).resolve().parent.parent


def main() -> None:
    """Execute each notebook and report runtime provenance and cell counts."""
    with TemporaryDirectory(prefix="mg-uv-colab-check-") as scratch:
        root = Path(scratch)
        environment = root / "environment"
        subprocess.run([sys.executable, "-m", "venv", str(environment)], check=True)
        python = environment / (
            "Scripts/python.exe" if os.name == "nt" else "bin/python"
        )
        subprocess.run(
            [str(python), "-m", "pip", "install", "--quiet", "ipykernel"], check=True
        )
        kernels = root / "kernels"
        spec = kernels / "python3"
        spec.mkdir(parents=True)
        (spec / "kernel.json").write_text(
            json.dumps(
                {
                    "argv": [
                        str(python),
                        "-m",
                        "ipykernel_launcher",
                        "-f",
                        "{connection_file}",
                    ],
                    "display_name": "Student runtime check",
                    "language": "python",
                    "env": {
                        "PYTHONPATH": "",
                        "MPLBACKEND": "module://matplotlib_inline.backend_inline",
                        "TMPDIR": str(root),
                        "TEMP": str(root),
                    },
                }
            )
        )
        for source in sorted((REPO_ROOT / "notebooks/tutorials").glob("*.py")):
            work = root / source.stem
            work.mkdir()
            nb = jupytext.read(source)
            experiments = {
                "01": ("crystal", "d_eff_pm_per_V", 1.68),
                "02": ("cavity", "loss_per_pass", 0.01),
                "03": ("cavity", "power_in_W", 2.0),
                "04": ("transport", "efficiency", 0.50),
            }
            section, key, value = experiments[source.name[:2]]
            load_cell = next(
                c.source for c in nb.cells if "params = yaml.safe_load(f)" in c.source
            )
            override_check = (
                f"\nparameter_overrides = {{{section!r}: {{{key!r}: {value!r}}}}}\n"
                f"exec({load_cell!r})\n"
                f"assert params[{section!r}][{key!r}] == {value!r}\n"
                "print('Saved parameter override applied successfully')"
            )
            nb.cells.append(
                nbformat.v4.new_code_cell(
                    "import src.enhancement_cavity as checked_module\n"
                    "import platform, scipy, numpy\n"
                    "module_path = Path(checked_module.__file__).resolve()\n"
                    "assert module_path.is_relative_to(REPO_ROOT.resolve()), "
                    "(str(module_path), str(REPO_ROOT))\n"
                    "revision = subprocess.check_output(['git', '-C', "
                    "str(REPO_ROOT), 'rev-parse', 'HEAD'], text=True).strip()\n"
                    "assert revision == REFERENCE_REVISION\n"
                    "print('Checked runtime:', platform.python_version(), "
                    "numpy.__version__, scipy.__version__)" + override_check
                )
            )
            print(f"Fresh runtime: {source.name}", flush=True)
            client = NotebookClient(
                nb,
                timeout=600,
                kernel_name="python3",
                resources={"metadata": {"path": str(work)}},
            )
            client.create_kernel_manager()
            client.km.kernel_spec_manager = KernelSpecManager(
                kernel_dirs=[str(kernels)]
            )
            client.execute()
            print(f"PASS: {source.name}; {len(nb.cells)} cells", flush=True)
            for output in nb.cells[-1].get("outputs", []):
                if output.get("name") == "stdout":
                    print(output["text"].strip(), flush=True)
            rendered = REPO_ROOT / "docs/tutorials" / (source.stem + ".ipynb")
            reference = nbformat.read(rendered, as_version=4)

            def figures(notebook: nbformat.NotebookNode) -> list[str]:
                return [
                    hashlib.sha256(o["data"]["image/png"].encode()).hexdigest()
                    for c in notebook.cells
                    for o in c.get("outputs", [])
                    if "image/png" in o.get("data", {})
                ]

            assert len(figures(nb)) == len(figures(reference)) > 0
            print(
                f"Figures: {len(figures(nb))}; "
                f"exact PNG match: {figures(nb) == figures(reference)}",
                flush=True,
            )


if __name__ == "__main__":
    main()
