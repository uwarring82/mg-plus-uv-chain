---
layout: default
title: Calculations
description: Boyd–Kleinman recalculation against the Friedenauer 2006 baseline; Phase 0.5 load-bearing findings; what the architecture-neutral utilities prove.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. All work on this page is pre-G1 / exploratory. It validates the architecture-neutral utilities against a published baseline and surfaces open questions for the Phase 1 dossier; it does not seed Phase 4 architecture-family scoring.</p>

<p class="eyebrow">Calculations and findings</p>

# What the recomputation tells us so far.

**Review update — 2026-09-10:** the corrected SHG/cavity utilities now feed a [conditional cascade and coating recalculation](review/2026-09-10-rc07-recalculation.html). [All four review notebooks](review/index.html) are executed and the [impact report](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-09-10-rc07-recalculation.md) distinguishes fixed losses from refitted losses. May tables below are historical; Raman/noise budgets, material/measurement validation and any revised procurement targets remain open.

This page collects the substantive computational results to date. Each result is anchored to either the Friedenauer 2006 structured extraction or to a cited literature constant; results without a primary citation are flagged as such.

---

## Boyd–Kleinman reproduction of the Friedenauer baseline *Coastline*

<p class="classification classification--coastline">Coastline · testable by re-running the notebook and comparing outputs to the YAML extraction</p>

**Source notebook:** [`notebooks/2026-05-01-friedenauer-bk-recalculation.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/2026-05-01-friedenauer-bk-recalculation.py) (jupytext percent format; opens directly in VSCode/JupyterLab).

**Source data:** [`data/literature/Friedenauer2006/extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) (57 structured parameters; 4 explicit gaps).

**Question.** Does the architecture-neutral [`src.boyd_kleinman`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/boyd_kleinman.py) module reproduce the BK-derived optimum waists Friedenauer 2006 reports for the LBO and BBO doubling stages?

### LBO 1118 → 559 nm — NCPM, no walk-off

| Quantity | Paper | Recomputed | Δ |
|---|---|---|---|
| BK σ-optimum w₀ | 27.3 μm | 26.2 μm | −3.9 % |

The difference remains a few percent and is not attributed solely to refractive-index uncertainty without a verified operating-temperature Sellmeier calculation (the notebook used an order-of-magnitude figure pending Sellmeier-derived citation in [KD-UV280-007 Section C](KD-2026-XXX-uv-280nm.html#kd-uv280-007--lbo-at-relevant-shgsfg-stages)).

### BBO 559 → 280 nm — Type-I, walk-off-limited

**Historical May calculation (superseded by the correction below):**

| Quantity | Paper | Recomputed | Δ |
|---|---|---|---|
| BK σ-optimum w₀ (β = 0, no walk-off) | 19.4 μm | 13.6 μm | −30 % |
| BK σ-optimum w₀ (β = 18.4 with literature ρ ≈ 85 mrad) | 19.4 μm | ≈ 42 μm | +117 % |

**Correction — 2026-09-09.** The walk-off kernel was missing its divisor ξ.
With the review's diagnostic inputs B=18.0166, L=10 mm, n₁=1.67276 and
vacuum wavelength 559 nm, the corrected calculation gives an optimum waist
**19.346 µm**, close to the reported 19.4 µm. The old ≈42 µm discrepancy
therefore does not support the proposed enhancement-cavity explanation.
At the fixed ξ=1.41317 anchor, hₘ changes from 0.03304955 to 0.03924301.
The accompanying SHG-prefactor correction divides K by n₁; together they
scale γ by **0.709844** with the other inputs fixed. This is not a new
coating specification or a validation of the fitted cavity losses.


### Five data gaps recorded in May (status requires RC-07 follow-through)

1. **Sellmeier coefficients for LBO at 1118 nm** — to lock n_LBO beyond order-of-magnitude. Belongs in [KD-UV280-007 Section C](KD-2026-XXX-uv-280nm.html#kd-uv280-007--lbo-at-relevant-shgsfg-stages).
2. **Sellmeier coefficients and walk-off for BBO at 559 → 280 nm Type-I** — the binding uncertainty for the BBO BK analysis. Belongs in [KD-UV280-005 Section C](KD-2026-XXX-uv-280nm.html#kd-uv280-005--bbo-at-280-nm--phase-matching-walk-off-damage-threshold).
3. **Cavity mirror radii of curvature** — missing from the YAML extraction at this commit, but recoverable from the paper itself (Friedenauer 2006 reports e.g. f = 25 mm for the LBO cavity's curved focusing mirrors). Re-reading §3 / Table 1 unblocks `src.abcd.cavity_eigenmode_q` against this geometry.
4. **Friedenauer's BBO BK criterion** — single-pass vs. enhancement-cavity figure of merit. Resolution belongs in [KD-UV280-005](KD-2026-XXX-uv-280nm.html#kd-uv280-005--bbo-at-280-nm--phase-matching-walk-off-damage-threshold).
5. **`d_eff` for both crystals** — needed for any conversion-efficiency recomputation.

---

## September 10 cascade and coating comparison

At the reported couplers, fitting each stage’s passive loss to its published
output reproduces 275 mW cascade UV by construction. With corrected γ,
fitted LBO/BBO losses are **13,059 / 13,191 ppm**; optimizing the fitted
cascade predicts **278.446 mW**, under unity transport and complete extraction.
This is calibration and a conditional extrapolation, not independent validation.

Under the May additive loss-transfer assumptions, the equal-penalty M1 centre
moves from **1.9965% to 1.6841%**. At 1.5 W input, generated UV stays near
**0.632 W**, but circulating power rises from **65.37 to 77.49 W**. Unmeasured
mirror/non-mirror loss allocation and material/extraction assumptions materially
shift that centre. The [full comparison](review/2026-09-10-rc07-recalculation.html)
and [impact assessment](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-09-10-rc07-recalculation.md)
qualify the result. The May coating specifications remain unchanged.

---

## Phase 0.5 load-bearing findings *Coastline*

<p class="classification classification--coastline">Coastline · derived from the locked constraint files; testable by inspection of constraints/loss-budget.md</p>

These come out of the constraint extraction ([`raman-requirements.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/constraints/raman-requirements.md), [`loss-budget.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/constraints/loss-budget.md), [`phase-noise-budget.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/constraints/phase-noise-budget.md)) and propagate into Phase 4 axis weighting.

### Raman power headroom

Direct calculation of the required ion-side single-beam power for the Nominal scenario (Δ = 40 GHz, Ω_R/2π = 400 kHz, w₀ = 20 μm) gives ≈ 130 μW per beam. With a pessimistic 18 % source-to-ion transmission (two-AOM-per-beam delivery), this corresponds to **≈ 1.4 mW source-side** — three orders of magnitude below the headline ≥ 500 mW target.

> **Implication for Phase 4.** Axis 1 (Raman capability) is intensity-easy for *any* candidate architecture meeting the stability requirements. The binding scoring axes are expected to be axes 2–4 (phase coherence, UV robustness, thermal/nonlinear load), with raw power as a non-binding input. This weighting implication is recorded in the [G3 closure logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-01-gate-g3-closure.md) for the Phase 4 pre-scoring deliberation.

### 14-GHz unlockable resonance domain

Friedenauer 2006 §4 reports a frequency region (≈ 14 GHz wide; bounds 1118.339 to 1118.409 nm at the 1118 nm fundamental) where the BBO ring cavity could not be locked. Reproduced across several lasers, several cavities, and several BBO crystals — **all from one vendor** (Crystals of Siberia). The paper assigns no mechanism among the candidate set (refractive-index temperature drift / birefringence coupling / photochemical or colour-centre formation / impurity or growth defect).

<p class="classification classification--gate">Status — literature-level Underdetermined · G1 attribution gated on Phase 2 discriminant scans, not on dossier population.</p>

The dossier entry is [KD-UV280-010](KD-2026-XXX-uv-280nm.html#kd-uv280-010--14-ghz-unlockable-resonance-domain--published-evidence). A cross-check note in [`extracted.yaml::cross_check_notes`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) flags that the reported width (14 GHz) and the wavelength bounds (Δλ = 70 pm) are not numerically consistent under Δν = c·Δλ/λ² at 1118 nm (which gives 16.8 GHz); downstream entries cite the width and the bounds as separately reported quantities pending direct-PDF resolution.

### K_Raman prefactor uncertainty

The single-intermediate-level Raman prefactor used in `constraints/raman-requirements.md` §2.3 is **K ≈ 138 MHz** (verified by direct atomic-data calculation: dipole moment from Γ/2π = 41 MHz at 280 nm; intensity-to-Rabi coupling at w₀ = 20 μm). The full multi-level model (³P₁/₂ + ³P₃/₂ paths, Clebsch–Gordan coefficients) may shift this by a factor of 2–5.

**Why this does not invalidate the reference triple.** Even with a ×5 error, Raman power requirements remain ≪ 500 mW source-side. The headroom finding above survives any plausible K_Raman correction. Tightening is expected from Phase 1 atomic-data work.

---

## Architecture-neutral utilities — what they prove *Coastline*

<p class="classification classification--coastline">Coastline · historical May test snapshot; current check recorded below</p>

**Current check (2026-09-10):** 261 tests pass, 96.18% coverage including branches,
in the recorded Python 3.13.7 environment. CI enforcement remains RC-06.
The following table is the historical May snapshot across four test files.

| Module | Tests | What it validates |
|---|---|---|
| `src/boyd_kleinman.py` | 22 | Closed-form analytic limit `arctan²(ξ) / ξ` to 12 decimals; classic σ-optimised optimum reproduces ξ_opt ≈ 2.84, h_m,max ≈ 1.068; walk-off and absorption monotonically reduce h; bounded `h_m_optimum` never extrapolates to negative ξ (regression for the previously-failing notebook path). |
| `src/abcd.py` | 31 | Elementary matrices, compose semantics, Gaussian-beam q at the waist (q = i z_R; w(z_R) = √2 w₀; R(z_R) = 2 z_R); thin-lens imaging; concentric (g = 1) and confocal (g = 0) limits; eigenmode self-consistency under round trip. |
| `src/parameters.py` | 24 | CODATA constants; ²⁵Mg⁺ atomic placeholders; G3 lock helpers; defence-in-depth test for gate re-engagement when `G3_INTEGRATOR_ACKNOWLEDGED` is revoked. |
| `tests/test_diagnostic_surrogate_imports.py` | 1 | Charter §5.1 mechanical-enforcement test: production code may not import from `/src/diagnostic_surrogates_archive/`. Currently silent because the archive is empty. |

These utilities are **architecture-neutral by construction** — no crystal preset, no architecture-family branch, no wavelength shortcut. Per Charter §5.1 they are reviewable by any stance and are unblocked pre-G1. None of the calculations on this page is a Phase 4 input.

---

[← Home](index.html) · [← Principles](principles.html) · [Status →](status.html)
