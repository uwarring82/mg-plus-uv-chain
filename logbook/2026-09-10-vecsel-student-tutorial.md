# VECSEL student notebook: principles and frequency noise

**Date:** 2026-09-10\
**Steward:** Ulrich Warring\
**Status:** Teaching notebook implemented; local and fresh-runtime checks pass.\
**Starting revision:** `1ffe916383179f4cf02e1d497d936968f752c0c5`

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No.
- Affects success criteria or gate state? No.

## Teaching scope

[Tutorial 5](../docs/tutorials/05-vecsel-principles-noise.html) provides a
standalone VECSEL introduction with five original figures and saved parameter
overrides. Students can read it on Pages, download the executed notebook or
open it in Colab from the [student guide](../docs/tutorials/index.md).

The lesson covers the gain mirror (pump, quantum wells, standing-wave overlap,
DBR and thermal contact), external-cavity feedback, ideal birefringent and
etalon filters, fixed-mode path-length sensitivity, and technical frequency
noise from mechanics, temperature, pump power and actuator electronics.
A synthetic PSD budget leads to field coherence and the special white-noise
Lorentzian linewidth limit. Exercises connect changes in components and noise
to the plots, then ask what measurements could replace the teaching inputs.

**Pre-G1, exploratory, not promoted.** The wavelength illustrates the magnesium
seed band. Other numerical inputs are chosen examples, not measurements or
accepted hardware specifications. The notebook derives ideal filter and
coherence relations and cites Burd 2016/2023, Lee–Moriya–Hastie 2023 and
Di Domenico–Schilt–Thomann 2010. It does not simulate semiconductor growth,
solve mode competition or predict this laboratory's linewidth.

The noise conventions are explicit: one-sided PSD, ordinary Fourier frequency,
complex transfer functions, independent-input PSD addition, and coherent
addition of the thermal and fast paths driven by the same pump fluctuation.
The white floor is illustrative, not an inferred fundamental linewidth.
Integrated RMS frequency variation is not labelled FWHM. Colored-noise
coherence uses a stated 1 Hz–1 MHz integration band.

The companion [VECSEL narrative](../docs/tutorials/vecsel-systems.md) now
separates laser-frequency feedback from a following SHG-cavity lock. The
latter suppresses relative detuning, not absolute seed noise. An 18 kHz
historical actuator scale does not determine linewidth or UV RIN. Related
Henry-factor and path-length statements are narrowed to their assumptions;
historical in-house measurement values retain their evidence labels.

**RC-04 traceability:** commit `480428b` partially addresses
[RC-04](2026-09-09-repository-review-task-card.md#rc-04--next--repair-phase-noise-and-servo-interpretations)
in `vecsel-systems.md`: linewidth/PSD definitions and the following-cavity
servo interpretation now have explicit assumptions and worked examples.
`phase-noise-budget.md`, `friedenauer-baseline.md` and `bc-g-results.md` were
untouched by that commit. The four-document claim audit, harmonic-phase and
path-length checks, and measurement-dependent conclusions remain open;
this is partial progress, not RC-04 acceptance.

## Runtime and provenance

The fifth notebook retains the existing shared-code pin `3466c32`. Its new
teaching inputs and formulas are embedded in the notebook, so the older
checkout need only supply existing shared code and installation metadata.
No new YAML file or uncommitted module is required by an isolated copy.
The four earlier source files and eight rendered outputs remain unchanged.
All five pins agree; RC-06 now says “all tutorial pins” rather than “four”.
Pin freshness enforcement remains planned, with Ulrich accountable.

The renderer accepts a source-level description so the new page carries its
exploratory status instead of the default architecture-neutral description.
The opt-in Colab checker accepts `--stem 05` and verifies inline parameter
inputs as well as the earlier YAML loaders. It remains outside the core test
suite. The manifest generator handles a tutorial absent from its historical
baseline using null before-fields and accepts a selected tutorial/environment.

[The new manifest](../data/review/2026-09-10/vecsel-tutorial-manifest.json)
records exact source/tool/input and output hashes and printed results.
[The environment record](../data/review/2026-09-10/vecsel-environment.txt)
records Python 3.13.7, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.1 and the
resolved rendering tools. A fresh temporary environment was used after reads
of packages in the existing `.venv` stalled; that environment was not modified.
The RC-07 manifest is refreshed solely for its recorded renderer hash; its
numerical results and rendered analysis outputs remain unchanged.

## Validation

- All lesson cells and embedded checks pass: unit/periodic filter transmission,
  exact-versus-linear resonance shift, ideal feedback identity, zero-delay
  coherence and an independent white-noise integral limit.
- The five figure outputs were visually inspected. Notebook and HTML outputs
  are byte-identical on a second render.
- Black, isort and Ruff pass on the new notebook and changed Python tools.
  Edited tutorial front matter and local Markdown links validate.
- The published notebook has **19 cells: 10 code and 9 Markdown**; all ten
  code cells have execution counts. The fresh-runtime checker appends one
  validation code cell, so its reported **20 cells** describes the augmented
  check notebook. That extra cell verifies the imported module location,
  pinned Git revision and saved pump-noise parameter override. The check
  passes outside any checkout; all five PNGs exactly match the local render.
  Two preliminary attempts encountered GitHub connection resets (HTTP/2 and
  a process-local HTTP/1.1 retry). The successful run uses the normal command
  and unchanged bootstrap; no persistent Git configuration was changed.
- No `src/` or core-test changes. The core suite was not rerun for this
  teaching-only addition. No gate acceptance or replacement specification
  is implied.

Reproduce from the repository root with notebook dependencies installed:

```sh
python scripts/render_tutorials.py 05
python scripts/check_colab_tutorials.py --stem 05
python -m scripts.review.tutorial_manifest --stem 05 --environment data/review/2026-09-10/vecsel-environment.txt > data/review/2026-09-10/vecsel-tutorial-manifest.json
python -m scripts.review.rc07_manifest > data/review/2026-09-10/manifest.json
```

The isolated check exercises fetching the pin, installing dependencies and
executing with saved parameter overrides. It is not a claim of execution
inside Google's hosted service or a signed-in Colab UI.
