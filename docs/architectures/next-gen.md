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
follow-up. The reason for fixing topology now: **the Phase E
cross-check validates the BBO stage to 1.5 %**, and the per-component
literature is dense enough to anchor a defensible exploration.

**LBO passive-loss definition still open.** The Phase E cross-check
also exposed a −26 % residual on the LBO stage (0.702 W computed vs
0.950 W published) that is most likely a definitional gap between the
paper-stated `T_IC = 0.025` (impedance-matched, including nonlinear
load) and the bare passive loss `L_passive`. **Phase NG-A must close
this gap to ≤ 5 % residual before any 500 mW recommendation derived
from a swept LBO parameter set is admissible** — every LBO sweep is
otherwise anchored to a wrong loss number. Until NG-A lands, the
1.5 % stake belongs to the BBO stage only, not to the full LBO + BBO
chain.

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
| BBO ring coating-run procurement spec | ✅ done — [BBO coating-run rationale](bbo-coating-run.html) (2026-05-20). Procurement-side detail of this next-gen build; froze a five-page vendor-facing spec package at the equal-penalty M1' centre `T_IC = 19 965 ± 500 ppm` and surfaced the finding that Friedenauer's published M1' input coupler sits ~ 0.57 pp below the impedance-matched optimum at the published operating point (3.6 % UV buildup forgone). |

## G1 inheritance and G2-failure impact (P1 from 2026-05-08 review)

**G1 inheritance.** This workplan holds the two-stage SHG topology fixed (LBO ring + BBO ring); the 14 GHz unlockable-domain anomaly (CHARTER §8.1) is therefore **inherited unchanged** from [Friedenauer 2006](friedenauer-2006.html) §4. NG-D may test whether alternative crystal lengths or temperatures shift the anomaly, but G1 closure remains a Phase 2 discriminant-scan task, not a simulation task. Until G1 closes, the workplan recommendations are inputs to a future scoring decision, not outputs of one.

**G2-failure impact.** The 500 mW UV target is the most exposed of the three architectures to a worse-than-hoped G2 outcome, because it operates at the highest UV intensity at the BBO output. Impact bounds:

| If G2 closes at … | Impact on next-gen 500 mW | Mitigation already in design | Fallback |
|---|---|---|---|
| ≤ 5 %/100 h UV-output drop | Acceptable — UV stays above 475 mW for ≥ 100 h; maintenance interval ~ months | Tight L_passive budget; high-LIDT BBO; rack-internal cleanliness | None needed |
| 10–20 %/100 h | Tight — UV drops below 400 mW within ~ 100 h; maintenance interval shrinks to ~ weeks | Tighten L_passive budget per NG-E; reduce crystal intensity; hard-fluoride coatings | Reduce UV target to 300 mW; accept shorter maintenance interval |
| > 20 %/100 h | Architecture failure-mode envelope exceeded; 500 mW figure not sustainable | Architectural change required | Reduce UV target to 200 mW; or switch to alternative-topology slate (IC-VECSEL + pulsed-Raman, gated on Council-3 task-split disposition) |

G2 closure measurement bounds the actual rate. Until G2 closes, the workplan delivers a *parameterised recommendation*, not a sustained-power commitment.

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
