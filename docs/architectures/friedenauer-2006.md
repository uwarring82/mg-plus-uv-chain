---
layout: default
title: Friedenauer 2006 — architecture summary
description: As-published architecture summary of Friedenauer et al., Appl. Phys. B 84, 371 (2006). The reference baseline against which the next-generation 500 mW UV target is validated.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Reference baseline — AG Schätz stewardship. This page summarises an externally published architecture; it is not an endorsement of any particular design choice for the next-generation build.</p>

<p class="eyebrow">Architecture · reference baseline</p>

# Friedenauer 2006 — all-solid-state CW 1118 → 559 → 280 nm

The Friedenauer 2006 architecture is the project's reference baseline.
It is the only fully published all-solid-state CW two-stage SHG chain
at the relevant wavelengths, and we use it to validate every layer of
the architecture-neutral numerics stack in [`/src/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/).

**Citation.** A. Friedenauer *et al.*, *High power all solid state laser
system near 280 nm*, Appl. Phys. B **84**, 371 (2006).
DOI [10.1007/s00340-006-2274-2](https://doi.org/10.1007/s00340-006-2274-2).

---

## At a glance

| Stage | Wavelengths | Crystal | Phase matching | Reported output |
|---|---|---|---|---|
| Pump | 1118 nm | Yb fibre laser, 2 W, < 200 kHz linewidth | — | 1.8 W into LBO cavity |
| LBO ring cavity | 1118 → 559 nm | LBO α-cut, 18 mm, NCPM @ ~ 94 °C | Type-I, NCPM | 0.95 W stable, η ≈ 53 % |
| BBO ring cavity | 559 → 280 nm | BBO Brewster-cut, 4 × 4 × 10 mm, ~ 50 °C | Type-I critical, θ = 44.4° | 0.275 W, η ≈ 29 % |
| Cascade | 1118 → 280 nm | — | — | **0.275 W UV, η_total ≈ 15.2 %** |

Each cavity is locked via Hänsch–Couillaud polarisation analysis with a
piezo-driven mirror (Friedenauer M2 / M2'). The 559 nm fundamental for
the BBO stage is also the absolute frequency anchor: ~ 10 mW is split
off to an iodine cell and locked to the R(53)28-3 transition at
559.271 nm.

For the per-component breakdown of every mirror, coating, and crystal
in the chain, see the [components inventory](../components/friedenauer-baseline.html).

---

## What the cross-check tells us

Phase E of the [numerics-expansion workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-07-numerics-expansion-workplan.md)
re-computes the cascade from first principles using only the
architecture-neutral primitives plus the parameter values in
[`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml).
The recompute notebook lives at
[`notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py).

| Quantity | Paper | Recomputed (first run) | Discrepancy |
|---|---|---|---|
| LBO 559 nm output | 0.950 W | 0.702 W | −26.1 % |
| BBO 280 nm output | 0.275 W | 0.271 W | −1.5 % |
| Overall η (1118 → 280) | 15.2 % | 8.0 % | −47.6 % (compounded) |

**The BBO stage matches to 1.5 %.** This validates the depleted-regime
cavity solver, the Eckardt-anchored `d_eff = 1.44 pm/V`, the Eimerl
walk-off `ρ = 83.1 mrad`, and the cascade composition end-to-end.

**The LBO gap is dominated by an `L_passive` definitional ambiguity.**
The paper reports `T_IC = 0.025` for the LBO input coupler; the recompute
treated this as the bare passive loss, but the value is most plausibly
the *impedance-matched* IC transmission already containing the nonlinear
conversion load (`T_IC ≈ L_passive + (1 − L_passive)·η_nl`). The true
passive loss is then ~ 0.015–0.020, raising the circulating power and
recovering most of the 26 %. Phase NG-A of the [next-generation
workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md)
closes this before any next-gen parameter sweep runs.

---

## What the architecture established

Reading the paper as a list of *resolved* and *open* facts:

**Resolved (paper-stated, multiply-confirmed).**

- Two-stage SHG topology is sufficient for 1118 → 280 nm at the > 250 mW UV
  output level on a few watts of pump.
- Hänsch–Couillaud polarisation locking is adequate for both cavities.
- LBO Type-I NCPM at ~ 94 °C (calculated 89 °C; the 5 °C shift is
  attributed to imperfect oven–crystal heat contact) is operationally
  stable.
- Iodine R(53)28-3 polarisation spectroscopy at 559.271 nm provides an
  absolute frequency anchor.

**Operationally bounded (effect predictable, mechanism not isolated).**

- UV power fluctuates within ±2 % of the mean; sub-microsecond drops <
  4 %; > 7 % drops less than once per minute.
- A 2 K ambient temperature swing causes a ~ 10 % oscillation
  unisolated; ~ 5 % when the crystal oven is thermally isolated.
- The output polarisation reaches steady state ~ 2 hours after the
  non-PM fibre is mechanically fixed.

**Underdetermined (mechanism unresolved in the paper).**

- A 14-GHz frequency band between 1118.339 nm and 1118.409 nm in which
  the BBO cavity could not be locked. Reproduced across "several
  lasers, cavities, and crystals" — but all the crystals tested were
  from a single vendor (Crystals of Siberia). This is the binding
  constraint that holds [G1](../principles.html#kill-gates-coastline)
  open and gates Phase 4 architecture scoring.

---

## What the paper does **not** report

These remain open extraction items in
[`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)
and are inputs to Phase NG-A through NG-E of the
[next-gen workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md):

- Exact BBO cut-angle tolerance and coating-vendor identity.
- Direct CW LIDT at 280 nm.
- Source-side RIN and phase-noise spectra.
- Ion-side loss budget.
- BBO `d_eff` at 559 nm Type-I (paper attributes all crystal data to
  SNLO; we use Eckardt 1990's numbers).
- BBO walk-off `ρ` at the Type-I phase-matching angle (we use Eimerl
  1987 plus Sellmeier-derived indices).
- Refractive indices `n_LBO(1118)` and `n_BBO_o(559)` (Sellmeier).

---

## What the next generation must beat

The next-generation target is ≥ 500 mW UV — an indicative anchor from
[CHARTER §1.5](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md).
At Friedenauer's η_total ≈ 0.15, that is ~ 3.3 W of 1118 nm pump (~ 2 ×
the Friedenauer pump). The next-gen workplan asks how much of the gap
can be closed *not* by buying more pump but by tightening the loss
budget, choosing IC reflectivities matched to the new pump scale, and
re-checking the Boyd–Kleinman optimum at the new operating point.

See [Architectures → Next-generation](next-gen.html) for the framing
and the [logbook workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md)
for the formal phase plan.
