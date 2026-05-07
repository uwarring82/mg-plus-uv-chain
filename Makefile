# Makefile for mg-plus-uv-chain
#
# Targets:
#   tutorials      Render notebooks/tutorials/*.py into executed .ipynb +
#                  HTML under docs/tutorials/, ready for GitHub Pages.
#   tutorials-one  Render a single tutorial (use STEM=NN; e.g.
#                  `make tutorials-one STEM=03`).
#   test           Run the pytest suite.
#   help           This message.
#
# `tutorials` requires `pip install -e .[notebooks]` (jupytext, nbconvert,
# nbclient, ipykernel).

.PHONY: help tutorials tutorials-one test

help:
	@grep -E '^[a-z\-]+:' Makefile | sed 's/:.*//' | sed 's/^/  /'

tutorials:
	python scripts/render_tutorials.py

tutorials-one:
	@if [ -z "$(STEM)" ]; then echo "Usage: make tutorials-one STEM=NN" >&2; exit 1; fi
	python scripts/render_tutorials.py $(STEM)

test:
	python -m pytest -q
