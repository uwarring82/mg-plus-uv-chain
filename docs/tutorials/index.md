---
layout: default
title: "Student tutorials"
description: "Read, run and extend five optics notebooks: single-pass SHG, cavity buildup, input coupling, cascades and VECSEL frequency noise. Student exercises and contribution guide."
---

# Learn the optics, run the notebooks, contribute

These tutorials are an entry point for students joining the UV-source project.
You can read every worked notebook in your browser, run it in Google Colab, change its inputs,
and contribute an explanation, calculation or test. Start with basic Python
(functions, arrays and plotting), optical power and Gaussian beams. The first
notebook introduces the nonlinear-optics notation as it is used.

**Start here:** read [Tutorial 1](01-shg-single-pass.html), then follow
[Run in Google Colab](#run-in-google-colab) and complete its first exercise below.
You do not need an account or software installation to read the worked pages.
The project website displays saved results; the Colab links open interactive
notebooks in your browser.

## Five worked notebooks

Tutorials 1–4 form the SHG sequence; Tutorial 5 is a standalone introduction
to the VECSEL seed. Each has equations, plots and saved parameter overrides.
The first four use YAML inputs; Tutorial 5 bundles its example inputs in cells.
The examples are teaching models, not accepted specifications for a
particular cavity. Tutorial 5 is **pre-G1, exploratory, not promoted**.

| Step | Read online | Run in your browser | Notebook file | What you will learn |
|---|---|---|---|---|
| 1 | [Single-pass SHG](01-shg-single-pass.html) | [Open in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/01-shg-single-pass.ipynb) | <a href="01-shg-single-pass.ipynb" download>Download .ipynb</a> | Convert a focusing factor into a power prediction; distinguish small-signal and depleted conversion. |
| 2 | [Passive cavity buildup](02-enhancement-cavity-buildup.html) | [Open in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/02-enhancement-cavity-buildup.ipynb) | <a href="02-enhancement-cavity-buildup.ipynb" download>Download .ipynb</a> | Sum returning field amplitudes and relate round-trip loss to the optimum input coupling. |
| 3 | [Optimal input coupler](03-optimal-input-coupler.html) | [Open in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/03-optimal-input-coupler.ipynb) | <a href="03-optimal-input-coupler.ipynb" download>Download .ipynb</a> | Include nonlinear depletion and test sensitivity to uncertain loss and conversion strength. |
| 4 | [Two-stage cascade](04-cascade-shg.html) | [Open in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/04-cascade-shg.ipynb) | <a href="04-cascade-shg.ipynb" download>Download .ipynb</a> | Track power through both stages and the relay; distinguish calibration from independent validation. |
| 5 | [VECSEL principles and frequency noise](05-vecsel-principles-noise.html) | [Open in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/05-vecsel-principles-noise.ipynb) | <a href="05-vecsel-principles-noise.ipynb" download>Download .ipynb</a> | Explore the chip, cavity and filters; connect technical noise to frequency PSD and coherence. |

Notebook files need the repository's `src/` modules. Tutorials 1–4 also use
[`notebooks/tutorials/NN-params.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/notebooks/tutorials)
inputs. The Colab setup cell fetches these automatically from reviewed revision
`3466c32` and installs the required packages in the runtime. For local work,
clone the repository as described below.

The [VECSEL systems tutorial](vecsel-systems.html) is a complementary reading
track on the seed lasers, gain mirrors, spectral filters and linewidth. It is
a narrative companion to [Tutorial 5](05-vecsel-principles-noise.html). Its
[references](../references.html) and the [seed-laser component record](../components/seed-lasers.html)
connect the models to the group's sources.

## Run in Google Colab

1. Click **Open in Colab** beside a tutorial and sign in to Google if prompted.
2. Use **File → Save a copy in Drive** to keep your own editable notebook.
3. Use a standard Python CPU runtime, then **Runtime → Run all**. The first
   code cell downloads the public code and inputs and installs dependencies.
   These calculations do not require a GPU or a Drive mount.
4. Edit the **Your experiment** cell and run that cell and the cells below
   it again. For Tutorial 1, try:

   ```python
   parameter_overrides = {"crystal": {"d_eff_pm_per_V": 1.68}}
   ```

   Use `{}` to return to the bundled defaults. The other notebooks provide
   their own examples. Tutorial 5 uses `{"noise": {"pump_rin_asd_per_sqrtHz": 2e-7}}`
   to reduce the illustrative pump-noise ASD tenfold. Entering changes in this
   cell preserves them when
   you save or download the notebook.
5. Save your copy with your observations, or use **File → Download → Download
   .ipynb** to share it for review. Include the parameter changes and the
   question you investigated.

Colab runtimes are temporary: files edited only in the runtime are not saved
with the notebook. Keep your experiment in cells and save the notebook before
leaving. Google describes notebook sharing, downloads and runtime persistence
in its [Colab FAQ](https://research.google.com/colaboratory/faq.html).

The code and default inputs are pinned, while Colab's Python and installed
package versions can change. Record those versions when reporting a numerical
difference. For existing local checkouts, setup uses the checkout's code.

## Optional: run locally

Use Python 3.11 or later. The September numerical review was run with Python
3.13.7; its [recorded environment](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/review/2026-09-09/environment.txt)
is available for exact-environment comparisons. Installing the dependencies
below provides a working setup, rather than a promise of identical package
versions on every computer.

From a terminal on macOS or Linux:

```sh
git clone https://github.com/uwarring82/mg-plus-uv-chain.git
cd mg-plus-uv-chain
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[notebooks,test]' jupyterlab
git switch -c student/shg-exercises
python -m jupytext --to ipynb notebooks/tutorials/01-shg-single-pass.py
python -m jupyterlab notebooks/tutorials/01-shg-single-pass.ipynb
```

On Windows, create the environment with `py -3 -m venv .venv` and activate
it with `.venv\Scripts\Activate.ps1` in PowerShell; use the remaining `python`
commands in that environment. An existing repository checkout can start at
the environment step. Select the kernel belonging to this environment.

[JupyterLab installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
and [Jupytext conversion commands](https://jupytext.readthedocs.io/en/latest/using-cli.html)
are documented by their maintainers. You can also open the converted notebook
in an editor with Jupyter support.

Run all cells from a fresh kernel once before making changes. Keep the
notebook inside the cloned repository so it can find the example inputs.
Use the same `parameter_overrides` cell as in Colab, restart the kernel and
run all cells again. You can also edit the local YAML inputs; record both the
original and changed values, and clear overrides when comparing YAML defaults.
For another tutorial, substitute its filename and matching `NN-params.yaml`.

If an import fails, check the selected kernel and that the editable install
used that same Python. If the YAML file is missing, check the notebook's
location inside the clone. Running all cells after a restart avoids results
that depend on forgotten cell execution order.

## First exercises

For each exercise, write your prediction **before** running it. Hand in the
changed input, one labelled plot or table, and a short explanation of what
agrees with your prediction and what still needs checking. Use the units in
the YAML labels; the notebook converts them to SI for the calculations.

| Notebook | Experiment | Check your reasoning |
|---|---|---|
| 1 | Double `crystal.d_eff_pm_per_V` while retaining all other inputs. Compare γ and harmonic power at low and high pump power. | γ should increase fourfold. The fourfold power scaling applies in the small-signal limit; use the depleted model to check that harmonic power stays below input power. |
| 2 | Keep `cavity.gamma_shg` at zero. Locate the maximum for losses 0.01 and 0.02; evaluate at the exact match as well as on the plotted grid. | The passive optimum is T=L. At match, buildup is 1/L: 100 and 50 respectively. Explain why a coarse grid may miss that value. |
| 3 | Set `cavity.power_in_W` to 0.1, 1 and 2 W, leaving γ and passive loss fixed. Compare numerical optimum T with the small-signal approximation. | Plot the discrepancy and evaluate γ times the circulating power. Explain when the small-signal assumption is no longer adequate. |
| 4 | Change `transport.efficiency` from 0.95 to 0.50. Compare fixed couplers with couplers re-optimized for the changed input to stage 2. | Stage 2 input equals stage 1 harmonic output times transport efficiency. Explain why final output need not scale linearly with that efficiency. |

The synthetic parameter changes isolate model behaviour; they do not describe
changing one property of a real crystal independently of all its other
properties. For extensions, always state which inputs were held fixed and
which were refitted or re-optimized.

For Tutorial 5, halve the cavity length, shift the etalon passband, and reduce
pump noise. Predict how the cavity FSR, mode weights and noise PSD change.
Explain why a following SHG cavity does not narrow the seed laser itself.

## Contribute your first improvement

A useful contribution can be small: clarify an equation, add an informative
plot, reproduce a limiting case, or report a failure with the inputs needed
to reproduce it. No new physics result is required.

For a first contribution from Colab, send your saved notebook to your
supervisor or attach it to a GitHub issue, with the question, changed inputs
and result. A maintainer can help turn it into a source change. For a PR:

1. Work on a branch in your clone. For a pull request without repository write
   access, fork the repository on GitHub and push your branch to that fork.
2. Edit the tutorial's `.py` source and its YAML inputs. If you worked in the
   notebook editor, export your edited notebook back to the canonical source:

   ```sh
   python -m jupytext --to py:percent --output notebooks/tutorials/01-shg-single-pass.py notebooks/tutorials/01-shg-single-pass.ipynb
   ```

3. Regenerate the affected public tutorial from the repository root and check
   your diff. This updates the executed `.ipynb` and `.html` under `docs/tutorials/`:

   ```sh
   python scripts/render_tutorials.py 01
   git diff --stat
   git status --short
   ```

   Commit the source, relevant inputs and generated pair together. The working
   `.ipynb` beside the source is a local editing copy; it need not be committed.
   Check for unrelated changes before submitting. If shared numerical code
   changes, run `python -m pytest -q` and include a meaningful regression check.
4. Open a pull request with the question, input values and units, expected
   behaviour, observed result and reproduction command. Cite the source and
   equation for a new formula. Include the Python version and any limitations.
   Ulrich Warring reviews contributions before they become part of the main
   record. A [GitHub issue](https://github.com/uwarring82/mg-plus-uv-chain/issues)
   with a reproducible example is equally useful if you are not ready for a PR.

The [project conventions](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CONVENTIONS.md)
cover units and commit format. Shared functions in `src/` remain independent
of particular builds. Put a study of a specific material or cavity in
`notebooks/exploration/`, marked **pre-G1, exploratory, not promoted**; a student
exercise does not adopt a procurement target or close a project gate.
Notebook code is covered by the repository's MIT software declaration;
consult the [licence map](../LICENSE.html) for document and figure scope.

### Ideas for future student projects

These are suggested starting points, not assigned work or accepted results.

- **Explain numerical accuracy:** compare grid maxima with the continuous
  optimizer and show how grid spacing affects the answer.
- **Make sensitivity visible:** plot γ and passive loss assumptions separately,
  then explain why a loss fitted at one operating point is correlated with γ.
- **Improve the teaching:** add a units walkthrough, an annotated energy-flow
  diagram or an explanation of an initially surprising exercise result.
- **Bridge to measurements:** propose the circulating-power, throughput or
  beam-profile measurements that would distinguish a model fit from validation;
  arrange any experimental work with the supervisor.

The [September review notebooks](../review/) are a next step after the four
tutorials: they show corrections, provenance records and the limits of fitting
published data. The earlier claim that the cascade comparison independently
validated BBO conversion to 1.5% is superseded; the
[dated impact report](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-09-10-rc07-recalculation.md)
explains the distinction between calibration and validation.

## Sources

- [Tutorial sources and parameter files](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/notebooks/tutorials)
- [Theory references](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/tutorials/REFERENCES.md)
- [Render pipeline](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/scripts/render_tutorials.py)
- [Current calculations](../calculations.html) and [project status](../status.html)
