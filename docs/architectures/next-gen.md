---
layout: default
title: Next-generation UV source — 500 mW @ 280 nm via two SHG stages
description: Parameterised target architecture for ≥ 500 mW CW UV at 280 nm via the same two-stage SHG topology as Friedenauer 2006, with pump power, IC reflectivities, crystal geometry, and loss-budget recommendations derived from the architecture-neutral primitives in /src/.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page describes a *parameterised* target, not a build commitment. Phase 4 architecture scoring is gated by G1 / G2; recommendations on this page are <em>inputs</em> to a future scoring decision, not <em>outputs</em> of one.</p>

<p class="eyebrow">Architecture · in design</p>

# Next-generation UV source — 500 mW @ 280 nm via two SHG stages

## Target

The CHARTER §1.5 indicative anchor is **≥ 500 mW CW UV at ~ 280 nm** at
the source output. Friedenauer 2006 demonstrated 0.275 W on the same
two-stage topology; the next generation needs roughly 1.8 × that UV
output.

The binding form remains the Level-0 row (`Δ_ref = 40 GHz`,
`Ω_R/2π = 400 kHz`, `Γ_sc = 2.0 × 10⁴ s⁻¹`) locked at G3 closure on
2026-05-01. The 500 mW figure is *indicative*, not load-bearing — but
this exploration shows whether it is reachable without forcing the build
into a corner of parameter space we cannot defend.

## Topology held fixed (for this iteration)

This page treats the **two-stage SHG topology** (LBO 1118 → 559 nm
followed by BBO 559 → 280 nm) as a fixed input. Alternative topologies
(PPLN-MgO, PPKTP, single-pass UV with build-up only at 559 nm) sit
outside the current workplan and will be evaluated in a separate
follow-up. The reason for fixing topology now: the Phase E cross-check
gives us a 1.5 %-accurate stake in the LBO+BBO chain, and the
per-component literature is dense enough to anchor a defensible
exploration.

## Design space (free parameters)

What the next-gen workplan sweeps:

- **Input pump power at 1118 nm.** Friedenauer used 1.8 W into the LBO
  cavity. The pump-vs-target forward map (workplan Phase NG-B) bounds
  the required pump as a function of the cascade efficiency we can
  achieve.
- **IC reflectivities** for both stages. Tutorial 03 showed how the
  optimal IC transmission scales with input power and round-trip loss;
  Phase C's exact one-way-coupling factorisation extends this to the
  cascade. Phase NG-C re-optimises both stages at the new pump scale.
- **Crystal geometry** — length `L` and waist `w0` per stage. Phase
  NG-D sweeps `L ∈ [10, 25] mm` for LBO and the equivalent envelope for
  BBO, recomputing the Boyd–Kleinman optimum at each length and
  checking sensitivity to crystal-temperature drift.
- **Passive round-trip loss `L_passive`** per stage. Phase NG-E anchors
  the achievable loss budget against IBS-coating literature
  (Tamosauskas2018, Burkley2021, Brown2019) so the recommendations sit
  on real coating-run capability rather than wishful numbers.

## Approach

Parameter sweeps run in [`/notebooks/exploration/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/)
using only the architecture-neutral primitives in
[`/src/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/):
`shg_single_pass.py` (γ_SHG from Boyd–Kleinman `h_m`), `enhancement_cavity.py`
(Polzik–Kimble impedance match with the exact `−L · η_nl` cross term and
the depleted-regime solver), `shg_cascade.py` (one-way-coupling
factorisation). Every sweep is sanity-checked against the Phase E
Friedenauer cross-check (BBO 1.5 % residual must be preserved); a sweep
that breaks the cross-check pauses for resolution rather than continuing
on a corrupted baseline.

The deliverable is **a parameterised recommendation set** — pump power,
IC reflectivities per stage, crystal length and waist per stage, loss
budgets, and a sensitivity envelope around each value — *not* a build
decision. Build/buy decisions sit downstream and depend on G1 and G2
closures.

## Status

| Item | State |
|---|---|
| Architecture-neutral numerics stack ready | ✅ done — Phases A–C of the [numerics-expansion workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-07-numerics-expansion-workplan.md) |
| Friedenauer cross-check at BBO stage | ✅ 1.5 % residual ([Phase E](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py)) |
| Tutorials live on the site | ✅ done — [Tutorials](../tutorials/) |
| Workplan drafted | ✅ done — [`logbook/2026-05-08-next-gen-500mW-workplan.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md) |
| Phase NG-A · LBO `L_passive` gap closed | ⏳ pending |
| Phase NG-B · pump-vs-UV forward map | ⏳ pending NG-A |
| Phase NG-C · IC reflectivity sweep | ⏳ pending NG-A, NG-B |
| Phase NG-D · crystal-geometry sweep | ⏳ pending NG-A |
| Phase NG-E · loss-budget anchoring | ⏳ pending NG-C |
| Phase NG-F · synthesis + sensitivity | ⏳ pending NG-A through NG-E |
| Phase NG-G · documentation surface | ⏳ pending NG-F |

## Boundaries (what this page is **not**)

- **Not Phase 4 architecture scoring.** That is gated by G1 + G2.
- **Not architecture-family-specific code in `/src/`.** Phase NG-* lives
  exclusively in `/notebooks/`. The mechanical anti-seeding scan
  ([`tests/test_anti_seeding_src_imports.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/tests/test_anti_seeding_src_imports.py))
  enforces this on every test run.
- **Not a build commitment.** The recommendation set is parameterised;
  build/buy decisions are explicitly downstream.
- **Not an alternative-topology study.** That is a separate workplan
  after NG-G.
- **Not a UV-degradation analysis.** G2-dependent; a separate workplan.

See [Architectures → Friedenauer 2006](friedenauer-2006.html) for the
reference baseline this page must keep agreeing with.
