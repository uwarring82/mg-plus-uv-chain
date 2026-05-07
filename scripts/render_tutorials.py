"""
render_tutorials.py — Phase F notebook-rendering pipeline.

Converts the jupytext-paired .py tutorial sources under
``notebooks/tutorials/`` into executed .ipynb notebooks and rendered
.html pages under ``docs/tutorials/`` so GitHub Pages can serve them as
a static, reproducible page set.

The HTML output uses nbconvert's ``basic`` template — which in
nbconvert 7 still emits a complete ``<html>``/``<head>``/``<body>``
document with embedded JupyterLab CSS variables that don't resolve
outside JupyterLab. The script extracts the ``<body>`` content via
regex and prepends Jekyll front matter so the ``notebook`` layout
(``docs/_layouts/notebook.html``) provides the site chrome.
Cell-level styling lives in ``docs/assets/notebook.css`` and targets
nbconvert 7's ``jp-*`` class names.

A normalisation pass (``_normalize_for_idempotency``) strips volatile
fields — random per-read cell IDs from jupytext, ``iopub`` execution
timestamps from nbclient, the language-info Python version, and the
kernelspec display name — so re-running the script against unchanged
sources produces byte-identical output. This makes a
``git diff --exit-code docs/tutorials`` check viable for CI.

Usage
-----
    python scripts/render_tutorials.py            # render all tutorials
    python scripts/render_tutorials.py 03         # render just 03-*.py

Run from the repo root. The kernel cwd is forced to the repo root so
the in-notebook path-walking finds ``pyproject.toml`` and adds the repo
to ``sys.path`` (nbconvert's CLI does not expose a kernel-cwd flag, so
the script calls ``nbclient.NotebookClient`` directly with
``resources['metadata']['path']``).

This script lives in ``/scripts/`` rather than ``/src/`` so it stays
clear of CHARTER §5.1 anti-seeding enforcement.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import jupytext
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

REPO_ROOT = Path(__file__).resolve().parent.parent
TUTORIALS_SRC = REPO_ROOT / "notebooks" / "tutorials"
TUTORIALS_OUT = REPO_ROOT / "docs" / "tutorials"


def render(stem_filter: str | None = None) -> int:
    """Render all (or a filtered subset of) tutorial .py files."""
    TUTORIALS_OUT.mkdir(parents=True, exist_ok=True)

    sources = sorted(TUTORIALS_SRC.glob("*.py"))
    if stem_filter:
        sources = [p for p in sources if p.stem.startswith(stem_filter)]
    if not sources:
        print(f"No tutorials matched filter {stem_filter!r}", file=sys.stderr)
        return 1

    # Headless matplotlib for any plotting cells.
    os.environ.setdefault("MPLBACKEND", "Agg")

    n_ok = 0
    for src in sources:
        out_ipynb = TUTORIALS_OUT / f"{src.stem}.ipynb"
        out_html = TUTORIALS_OUT / f"{src.stem}.html"

        print(f"[1/3] {src.name}: jupytext .py -> .ipynb")
        nb = jupytext.read(src)

        print(f"[2/3] {src.name}: execute (kernel cwd = repo root)")
        # Normalise cell IDs *before* execution so the IDs that leak into
        # the rendered HTML cell anchors are deterministic too.
        _normalize_cell_ids(nb)
        client = NotebookClient(
            nb,
            timeout=600,
            kernel_name="python3",
            resources={"metadata": {"path": str(REPO_ROOT)}},
        )
        client.execute()
        _normalize_post_execute(nb)
        with out_ipynb.open("w", encoding="utf-8") as fh:
            nbformat.write(nb, fh)

        print(f"[3/3] {src.name}: nbconvert basic -> Jekyll-wrapped .html")
        exporter = HTMLExporter()
        exporter.template_name = "basic"
        full_html, _resources = exporter.from_notebook_node(nb)
        # nbconvert 7's "basic" template still emits a full <html><head><body>
        # document; we want only the body content so the Jekyll "notebook"
        # layout wraps it. Extract <body>...</body>; if extraction fails, fall
        # back to the full document (defensive — shouldn't happen).
        body_match = re.search(
            r"<body[^>]*>(.*?)</body>", full_html, flags=re.S
        )
        body = body_match.group(1).strip() if body_match else full_html

        title = _extract_title(nb, default=src.stem)
        front_matter = (
            "---\n"
            f"layout: notebook\n"
            f"title: {title}\n"
            f"description: Tutorial notebook ({src.stem}). "
            f"Architecture-neutral; uses /src/ primitives only.\n"
            "---\n\n"
        )
        out_html.write_text(front_matter + body, encoding="utf-8")

        print(f"  -> {out_ipynb.relative_to(REPO_ROOT)}")
        print(f"  -> {out_html.relative_to(REPO_ROOT)}")
        n_ok += 1

    print(f"Rendered {n_ok}/{len(sources)} tutorial(s).")
    return 0


def _extract_title(nb, default: str) -> str:
    """Pull the first H1 from the notebook for the Jekyll title."""
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        for line in cell.source.splitlines():
            m = re.match(r"^#\s+(.+?)\s*$", line)
            if m:
                # Quote any colons so YAML stays valid
                return f'"{m.group(1)}"'
    return f'"{default}"'


def _normalize_cell_ids(nb) -> None:
    """Replace jupytext-generated random cell IDs with deterministic ones.

    nbformat 4.5+ requires cell IDs to be unique within a notebook. The
    `cell-NNNN` scheme keyed on cell index satisfies that and produces
    byte-identical output across runs. Cell IDs leak into the rendered
    HTML as anchor IDs, so normalising before execution keeps both the
    .ipynb and the .html idempotent.
    """
    for i, cell in enumerate(nb.cells):
        cell["id"] = f"cell-{i:04d}"


def _normalize_post_execute(nb) -> None:
    """Strip post-execution volatile fields so renders are idempotent."""
    for cell in nb.cells:
        # iopub execution timestamps from nbclient
        if "metadata" in cell and "execution" in cell["metadata"]:
            del cell["metadata"]["execution"]
    # Python version varies with the build environment
    if "language_info" in nb.metadata:
        nb.metadata["language_info"].pop("version", None)
    # Kernelspec display_name is required by nbformat.validate, so we
    # canonicalise it to a fixed value rather than stripping it (typical
    # variants observed: "Python 3", "Python 3 (ipykernel)").
    if "kernelspec" in nb.metadata:
        nb.metadata["kernelspec"]["display_name"] = "Python 3"


if __name__ == "__main__":
    filter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    sys.exit(render(filter_arg))
