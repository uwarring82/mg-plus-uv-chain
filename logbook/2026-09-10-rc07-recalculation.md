# RC-07 — Cascade, fitted loss and coating-target recalculation

**Date:** 2026-09-10  
**Steward:** Ulrich Warring  
**Baseline:** `4404074d5114ecf7515a2cbd71910c16c036359d`  
**Status:** Recalculation and conditional impact assessment filed. D1 acceptance, material/loss measurements and any D4 specification amendment remain open.  
**Scope:** [RC-07](2026-09-09-repository-review-task-card.md#rc-07--next--recalculate-affected-results-and-revise-their-claims), following the [numerical foundations](2026-09-09-numerical-foundations.md).

## Charter §9 trigger questions

- **Affects Level 0 parameters?** No; locked Raman parameters are unchanged.
- **Affects Level 1 parameters?** No binding value is amended. This report calculates the implications for the historical May coating targets and records what needs disposition.
- **Affects success criteria?** No.
- **Changes Charter, gate state or prior sign-off?** No. No D1 acceptance is inferred from the corroborating checks or instruction to continue the calculations.

## Result and interpretation

Correcting γ while keeping the old BBO loss predicts **228.872 mW**, compared
with the published 275 mW at 0.95 W input and T=0.016. Refitting loss to that
same point reduces it from the May **15,288 ppm** to **13,191 ppm**. Under the
May assumptions for transferring this loss budget to the new build, the
single-variant equal-penalty IC centre moves from **1.9965% to 1.6841%**.

At the 1.5 W design input, refitting restores almost the same predicted UV
output, but circulating power rises **18.5%**, from **65.37 to 77.49 W**.
The approximately unchanged UV output therefore does not preserve the old
visible-light coating-intensity margins. None of these fitted quantities is
an independent measurement of the new cavity or the received Agile mirrors.

## Inputs and comparisons

The [new analysis source](../notebooks/exploration/2026-09-10-rc07-recalculation.py)
reads the same [Friedenauer extraction](../data/literature/Friedenauer2006/extracted.yaml)
as the May diagnostic. Crystal lengths, reported waists, input powers,
reported harmonic powers, coupler reflectivities and LBO d_eff are unchanged.
The main comparison deliberately retains the diagnostic's material inputs:
LBO indices 1.605/1.620, BBO indices 1.67276/1.565, BBO walk-off 83.1 mrad,
and BBO d_eff=1.44 pm/V, bracketed by 1.30–1.60 pm/V. These choices isolate
the code correction; they are not new Sellmeier or nonlinear-coefficient
measurements. The index limitations below remain material.

The old SHG normalization is reconstructed algebraically: evaluating the
corrected kernel at B√ξ restores the old missing-ξ kernel, and multiplying
corrected K by n₁ restores the old missing-index prefactor. Both sides use
the corrected cavity solver. This isolates the SHG change; it is not a
reproduction of the old solver's invalid-domain behaviour. The reconstructed
BBO γ is 1.491391914×10⁻⁴ W⁻¹, consistent with the rounded May pin
1.4914×10⁻⁴. The coating comparison uses the **actual rounded May pins**.

| Quantity | Old normalization | Corrected normalization |
|---|---:|---:|
| LBO γ (W⁻¹) | 3.56026136×10⁻⁴ | 2.21823138×10⁻⁴ |
| BBO γ, central (W⁻¹) | 1.49139191×10⁻⁴ | 1.05865670×10⁻⁴ |
| BBO γ, d_eff low/high (W⁻¹), corrected | — | 8.62813379×10⁻⁵ / 1.30698358×10⁻⁴ |
| BBO hₘ at the reported 19.4 µm waist | ≈0.03305 | 0.03924309675 |
| BBO optimum waist with retained inputs | historical ≈42 µm | 19.3456934 µm |

The small difference from yesterday's hₘ=0.03924301048 is from evaluating
ξ and B from the full geometry rather than rounded diagnostic anchors
ξ=1.41317, B=18.0166. It is not another normalization change.

The May BK notebook is re-executed with corrected explanatory text. Its
≈42 µm discrepancy and inferred ≈2.5 mrad effective walk-off are superseded.
The LBO waist discrepancy remains an input/geometry question; it is not
assigned solely to refractive-index uncertainty without a verified
operating-temperature Sellmeier calculation.

## Cascade and fitted loss

For a nonlinear cavity, impedance matching is T=L+(1−L)η. Consequently,
setting passive loss L equal to the paper's T does not follow from a claim
that the coupler was impedance matched. The original diagnostic also mixed
separately optimized per-stage outputs with a fixed-coupler cascade summary.
The new calculation keeps those operating points separate.

The following retains the original **comparison assumption L=T**; these
losses are not measured. Stage powers use their reported input powers:
1.80 W for LBO and 0.95 W for BBO.

| Prediction | Old normalization | Corrected normalization |
|---|---:|---:|
| LBO at reported T=0.025 | 0.648004 W | 0.530296 W |
| LBO, T optimized at the same assumed L | 0.701753 W | 0.556772 W |
| BBO at reported T=0.016 | 0.259917 W | 0.215167 W |
| BBO, T optimized at the same assumed L | 0.270933 W | 0.221121 W |
| Cascaded UV, both reported couplers | 0.143327 W | 0.0820418 W |
| Cascaded UV, both couplers optimized | 0.167435 W | 0.0903407 W |

Cascade transport is assumed one, as in the original diagnostic. The
reported equal 0.95 W values at the LBO output and BBO input are not an
independent, precise relay-throughput measurement.

Next, fit L **at each actual reported coupler**, holding γ fixed, to match
0.950 W LBO output and 0.275 W BBO output. The solve is

$$
\epsilon_{\rm ext}\,P_h(P_{\rm in},T,L,\gamma)=P_{\rm measured}.
$$

The main comparison assumes ε_ext=1 and no UV feedback. Generated harmonic
power, extracted power and power delivered onward coincide only under these
assumptions. The fit rejects unattainable output values; endpoint agreement
within 3×10⁻¹² relative output is treated as numerical equivalence to the
physical boundary, consistent with the forward solver's tolerance.

| Fitted result | Old normalization | Corrected normalization |
|---|---:|---:|
| LBO passive loss | 15,840.59 ppm | 13,059.29 ppm |
| LBO matched T at the reported input | 3.41044% | 2.73358% |
| BBO passive loss | 15,287.57 ppm | 13,191.25 ppm |
| BBO matched T at the reported input | 2.16915% | 1.85283% |
| Cascade at reported couplers | 0.275000 W | 0.275000 W |
| Cascade with both couplers optimized | 0.298532 W | 0.278446 W |

The equal 275 mW entries are **calibration closure**. They do not validate
material constants, establish ±1.5% uncertainty in γ, or demonstrate that
Friedenauer actually had these passive losses. Independent circulating-power,
linear-cavity loss, mode-matching and extraction measurements are needed to
separate those quantities. Optimizing the fitted cascade is a conditional
extrapolation away from the calibration point.

## Coating comparison at the May default budget

The May construction subtracts a **3,400 ppm mirror-loss envelope** from the
fitted total loss, then adds a **1,500 ppm proposed mirror budget**. We retain
that additive construction for direct comparison. Three cases distinguish
normalization from recalibration:

| Case | γ (W⁻¹) | Reference total loss | Residual called “non-mirror” in May | New-build default total loss |
|---|---:|---:|---:|---:|
| Frozen May inputs | 1.4914×10⁻⁴ | 15,288 ppm | 11,888 ppm | 13,388 ppm |
| Corrected γ, old loss fixed | 1.05865670×10⁻⁴ | 15,288 ppm | 11,888 ppm | 13,388 ppm |
| Corrected γ, refitted loss | 1.05865670×10⁻⁴ | 13,191.25 ppm | 9,791.25 ppm | 11,291.25 ppm |

The residual is a **model-dependent allocation**, not a measured
non-mirror loss. The R floors bound non-reflected power; they do not measure
transmission alone or determine the actual mirror contribution. Transferring
the residual unchanged to a different crystal, oven and cavity is another
assumption.

| Case | Input | T optimum | Circulating power | Generated UV | Worst penalty at historical 1.9965% ±0.05 pp |
|---|---:|---:|---:|---:|---:|
| Frozen May | 0.5 W | 1.7565% | 28.466 W | 0.12051 W | 0.970% |
| Frozen May | 1.5 W | 2.2945% | 65.373 W | 0.63326 W | 0.946% |
| Corrected γ, old loss | 0.5 W | 1.6539% | 30.232 W | 0.09655 W | 1.952% |
| Corrected γ, old loss | 1.5 W | 2.0861% | 71.906 W | 0.54461 W | 0.178% |
| Corrected γ, refitted loss | 0.5 W | 1.4815% | 33.749 W | 0.12029 W | 4.317% |
| Corrected γ, refitted loss | 1.5 W | 1.9358% | 77.488 W | 0.63220 W | 0.112% |

Each penalty is relative to that row's own optimum. The equal-relative-penalty
centre across the two pump scenarios is **1.996472% / 1.849107% / 1.684123%**
for the three cases, respectively. The corrected/refitted centre costs
0.6796% at either scenario endpoint before manufacturing tolerance.
The full JSON includes all eight scenario/loss-grid rows per case and
±500 ppm, ±1,000 ppm, ±0.5 pp and ±1 pp tolerance sweeps.

### Sensitivities rather than confidence intervals

Jointly refit loss whenever d_eff or extraction changes. Treating γ and its
fitted L as independent error bars would discard their calibration correlation.

| d_eff | Assumed UV extraction | Refit BBO loss | Default equal-penalty T |
|---|---:|---:|---:|
| 1.30 pm/V | 100% | 11,985 ppm | 1.5126% |
| 1.30 pm/V | 95% | 11,440 ppm | 1.4708% |
| 1.44 pm/V | 100% | 13,191 ppm | 1.6841% |
| 1.44 pm/V | 95% | 12,610 ppm | 1.6395% |
| 1.60 pm/V | 100% | 14,469 ppm | 1.8723% |
| 1.60 pm/V | 95% | 13,849 ppm | 1.8247% |

The 95% extraction row is a hypothetical **whole-path** efficiency, not a
claim that a front-face T floor, an AR reflectivity or the Agile reports
establish that number. Multiply each sensitivity row's generated UV by its
assumed extraction to obtain external UV power. Residual mode mismatch and
pump entrance losses are still absorbed into this simplified calibration.

Two further effects are recorded separately, not combined into a statistical band:

- At central d_eff, assigning **0 / 1,500 / 3,400 ppm** of the fitted old
  total to mirrors gives default centres **1.9545% / 1.8334% / 1.6841%**.
  These are loss-allocation scenarios, not measured mirror losses. They show
  why subtracting the R-floor envelope does not uniquely predict a new-build T.
- The harmonic index **1.565 is approximate and is not a verified angular
  effective index at phase match**. The relation Δk=2k₁−k₂ implies
  n₂,eff=n₁ at collinear wave-vector match; the optimized Gouy mismatch adds
  a small correction. A sensitivity using n₂=1.67276 gives
  γ=9.90458×10⁻⁵ W⁻¹, fitted loss 12,794.86 ppm and centre **1.6271%**.
  This is not a new Sellmeier extraction or an acceptance of that simplified
  operating point. LBO operating-temperature indices also remain unresolved.

The cavity model multiplies round-trip survival factors. Using products for
0.0007/0.0007/0.002 old mirror losses and 0.0003/0.0003/0.0009 new losses,
then refitting the residual survival, gives a new total **11,312.55 ppm**
and centre **1.68577%**, versus the additive 11,291.25 ppm / 1.68412%.
This small composition correction is far below the unmeasured loss-allocation
and material sensitivities; both constructions are retained in the output.

## Intensity and specification impact

At the default budget and 1.5 W input, the spherical Gaussian approximation
uses w₀=19.4 µm and a curved-mirror radius **254.702 µm**, from propagation
through 5 mm of BBO, q_air=q_BBO/n at a flat exit, then 24.7 mm of air.
These are beam-normal Gaussian peak intensities 2P/(πw²). Brewster-surface
and oblique-mirror astigmatism, actual long-arm positions and layer fields
are not solved here. Taking the pre-conversion circulating power at every
fundamental mirror gives a conservative power proxy within this model.

| Proxy at 1.5 W | Frozen May | Corrected γ, refitted loss |
|---|---:|---:|
| BBO waist, green peak | 11.058 MW/cm² | 13.107 MW/cm² |
| Curved mirror, green peak | 64.153 kW/cm² | 76.042 kW/cm² |
| Plane mirror, assuming w=200–150 µm | 104.05–184.97 kW/cm² | 123.33–219.25 kW/cm² |
| UV peak **if its radius equals the green curved-mirror radius** | 621.44 W/cm² | 620.40 W/cm² |

The last row is deliberately conditional: the generated UV spatial mode and
walk-off profile are not established by the fundamental spot calculation.
It cannot validate a coating-lifetime estimate or a per-surface UV margin.

| Historical May item | Consequence / disposition |
|---|---|
| M1 centre 19,965±500 ppm and ≈1% worst-case penalty | Central refit predicts up to **4.32%** low-scenario penalty in that historical band; new centre is conditional on the unresolved inputs above. Record for D4; do not silently replace the supplier target. |
| “Higher R is never a failure mode” in M1 notes | Not a general model result: lower T can increase mismatch and T=0 admits no pump. Acceptance must use the actual operating point and required output, not monotonic preference for R. |
| M2/M3/M4 loss allocation 300/300/900 ppm | Unchanged historical targets. The model does not independently validate their allocation or prove new-build non-mirror loss equals the fitted residual. |
| M1/M2 visible LIDT margin | Green intensity proxy rises 18.5%. At a requested 500 kW/cm² threshold, the ratio to the plane-mirror worst proxy falls from ≈2.70 to ≈2.28; this is a requested-threshold ratio, not a measured damage margin. |
| M3/M4 visible LIDT margin | For the M4 requested 250 kW/cm² threshold, the ratio changes from ≈3.90 to ≈3.29. No threshold or service-life requirement is relaxed. |
| M4 UV transmission, back-face AR and UV LIDT | Require whole-path extraction and UV spot evidence; a nearly unchanged generated-power proxy does not validate lifetime or simultaneous-wavelength damage margins. |
| Geometry, quantity and received Agile stock | No new evidence here changes geometry or receipt facts. No supplier defect is inferred from a model correction. |

Dated notices in the work package and sheets link here while preserving
historical fields and sign-offs. The public coating explainer corrects the
missing k₁ and factor of two in b, and distinguishes its historical tables
from the current calculation. No new coating specification is adopted.

## Reproduction and evidence

The [results JSON](../data/review/2026-09-10/rc07-results.json) stores full-precision
inputs, cases, sensitivity grids, environment and input hashes. The
[output manifest](../data/review/2026-09-10/manifest.json) maps the edited
notebooks, renderer, data and HTML/notebook artifacts to this baseline and
records printed outputs. The [recorded environment](../data/review/2026-09-09/environment.txt)
from the preceding correction is reused: Python 3.13.7, NumPy 2.5.3, SciPy
1.18.1 and pytest 9.1.1. No new dependency is needed.

```sh
PYTHONPATH=. MPLBACKEND=Agg .venv/bin/python notebooks/exploration/2026-09-10-rc07-recalculation.py
.venv/bin/python -m scripts.review.render_rc07
.venv/bin/python scripts/render_tutorials.py 04
.venv/bin/python -m scripts.review.rc07_manifest > data/review/2026-09-10/manifest.json
.venv/bin/python -m pytest --cov=src --cov-report=term-missing -q
```

**261 tests pass; source coverage is 96.18% including branches.** Nine new
analysis tests recover passive loss from an independently constructed field
balance (including zero-loss and non-unit extraction), reject unattainable
fits and invalid extraction, and compare the equal-penalty solution with a
1,001-point independent transmission scan. No `/src/` implementation or
locked parameter changes in this set. Scoped Black/isort/Ruff checks cover
the new analysis, tests and modified rendering code; this is not RC-06's
repository-wide lint/type/CI completion.

All five rendered notebook/HTML pairs are byte-identical on a second run,
as is the results JSON; the comparison includes the complete output file
inventory, including newly generated files. All five embedded figures were
visually inspected. Executed notebooks contain no error or stderr outputs.

The three historical notebooks are re-executed with dated context; the
May IC sweep deliberately replays its frozen inputs. A fourth notebook
contains the current comparisons. Tutorial 4 removes the obsolete numerical
parable and its claim that one BBO agreement validates the material constants.
A successful historical replay is not acceptance of historical physics.

**Remaining work:** D1 steward acceptance; independent loss/mode-matching,
whole-path extraction, angular/temperature-dependent index and beam-profile
checks; then D4 disposition of any replacement procurement targets. D2 and
the Raman/noise branches of RC-07 remain separate. This report completes the
stated conditional SHG/cascade recalculation, not hardware validation or the
entire repository review.
