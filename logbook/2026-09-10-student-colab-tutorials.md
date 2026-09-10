# Student tutorials with Google Colab access

**Date:** 2026-09-10\
**Steward:** Ulrich Warring\
**Status:** Student entry point implemented; four notebooks pass fresh-runtime checks.\
**Baseline:** `3466c3262aa72af93f10a3699c48782d401548f8`

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No.
- Affects success criteria or gate state? No.

## What changed

The [tutorial index](../docs/tutorials/index.md) now introduces the existing
four notebooks to students, with an Open in Colab link for each, a reading
order, one guided exercise per notebook, and routes to contribute a saved
notebook, issue or pull request. Local installation is optional. The obsolete
1.5% cascade-validation claim is removed from the index and replaced by the
current calibration/validation distinction. The cascade’s old fixed percentage
summary is replaced by power accounting at the calculated operating points;
this identity does not require weak depletion or matched couplers. Coupler
sensitivity prose now refers to the actual sweep instead of promising fixed
percentage errors.

Each canonical tutorial source includes a setup cell. Outside a project
checkout it clones the public repository into a temporary runtime directory,
checks out reviewed revision `3466c32`, installs that revision's declared
packages with the kernel's Python, and locates its source and YAML inputs.
An existing local checkout uses its own code. No Drive mount or accelerator
is required. Runtime package versions are not pinned by this bootstrap;
the source/input pin and environment versions are separate provenance facts.

Each notebook also provides `parameter_overrides`, applied after loading the
YAML defaults. Students can save parameter changes inside their notebook
instead of relying on files that disappear with a Colab runtime. The guide
explains saving a copy and downloading work. The setup and override cells
are retained in the published `.ipynb` files, not only in the HTML.

The README and landing page identify the student guide. Existing software
licensing is retained; the licence map records the tutorial narrative/output
assignment question under D6. This publication does not adopt new optical
specifications or clear D1/D2.

When the shared model or default inputs change, maintainers should update
the four `REFERENCE_REVISION` pins to the reviewed code revision and rerun
the opt-in check. The pinned model revision is intentionally separate from
the commit publishing the tutorial notebooks.

## Validation

- All four tutorials execute through the normal render pipeline. Their
  saved numerical outputs and eight embedded figures are exactly unchanged
  from the baseline. All eight notebook/HTML files reproduce byte-for-byte
  on a second render.
- [The opt-in runtime check](../scripts/check_colab_tutorials.py) creates a
  temporary virtual environment, installs ipykernel, and runs each notebook
  in a fresh kernel outside any checkout. All four fetch the pinned revision,
  install their dependencies and complete successfully. Assertions verify
  that the imported code belongs to the fetched checkout at the expected
  revision, and that the example parameter override takes effect.
- The tested environment resolves to Python 3.13.7, NumPy 2.5.3 and SciPy
  1.18.1. Its eight figure PNGs exactly match the published local renders.
- The four Colab URLs target valid committed notebook paths. Local guide
  links and front matter validate. Scoped Black/isort/Ruff checks pass for
  the new runtime checker; no `/src/` or core-test implementation changes.
- The RC-07 manifest is refreshed because it records tutorial 4's source and
  generated outputs. RC-07 numerical results remain unchanged. Earlier
  manifests remain recoverable at their recorded commits.

Reproduce the runtime check from the repository root using the existing
notebook environment; it downloads public code and packages:

```sh
.venv/bin/python scripts/check_colab_tutorials.py
.venv/bin/python scripts/render_tutorials.py
.venv/bin/python -m scripts.review.rc07_manifest > data/review/2026-09-10/manifest.json
```

This is a local test of the fresh-runtime execution path, not a claim of
execution on Google's hosted service. Browser control was unavailable in
this session, so a signed-in Colab run remains a separate end-user check.
Google's [Colab FAQ](https://research.google.com/colaboratory/faq.html) documents
loading GitHub notebooks, saving copies and runtime persistence.
