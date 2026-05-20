---
layout: default
title: Architectures
description: Doubling-stage UV source architectures for mg-plus-uv-chain — the Friedenauer 2006 reference baseline, the next-generation 500 mW @ 280 nm parameter-optimisation target, and two alternative-topology sketches (IC-VECSEL with intracavity LBO; phase-locked Ti:S comb single-pass tripled for far-red-detuned Raman).
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. Architecture pages here describe a published baseline, a parameterised next-generation target, and two alternative-topology sketches. None is a build commitment, and none has been admitted to Phase 4 architecture scoring (G1 still open).</p>

<p class="eyebrow">Architectures</p>

# Architectures

Four architecture stories live here. The first two share the same
physics — a CW two-stage SHG chain 1118 nm → 559 nm → 280 nm — and the
same architecture-neutral primitives in [`/src/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/);
what differs between them is *where each one sits in the project
lifecycle*. The latter two are alternative-topology sketches landed on
2026-05-08; together with the next-generation Friedenauer-topology
workplan they form the slate-of-three under consideration for the future
Phase 4 architecture comparison.

| Page | What it is | Status |
|---|---|---|
| [Friedenauer 2006](friedenauer-2006.html) | The published all-solid-state architecture: 2 W Yb fibre at 1118 nm → LBO → BBO → 0.275 W at ~ 280 nm. The reference baseline our recomputation [validates against](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py). | **Reference baseline** — extraction and cross-check live; one open `L_passive` definitional gap to close. |
| [Next-generation](next-gen.html) | A parameterised target: ≥ 500 mW UV at 280 nm via the same two-stage SHG topology, with the input pump, IC reflectivities, and crystal geometry derived from the architecture-neutral primitives. | **In design** — workplan drafted ([`logbook/2026-05-08-next-gen-500mW-workplan.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md)); not yet executed. |
| [IC-VECSEL alternative](ic-vecsel-alternative.html) | An alternative topology: intracavity-doubled VECSEL (1118 nm + intracavity LBO → 559 nm direct) feeding a free-space PDH-locked BBO ring inside a sealed, temperature-controlled 19" rack envelope. Sized for cooling + repumping at ~ 50 mW UV; Raman handled by the parallel pulsed pathway. | **Sketch** — [logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-ic-vecsel-alternative-topology.md) carries full Charter §9 statements; promotion gated by G1 + G2 closure and a new `shg_intracavity.py` architecture-neutral primitive. |
| [Pulsed-Raman alternative](pulsed-raman-alternative.html) | An alternative-topology sketch for the *Raman task only*: phase-locked mode-locked Ti:Sapphire frequency comb single-pass tripled to ~ 290–320 nm, operated tens of nm red-detuned. Pulsed peak intensity supplies Ω_R; Γ_sc suppressed by ~ 10⁶ vs Δ_ref. | **Sketch — CHARTER §3 out-of-scope.** [`CHARTER.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) §3 line 105 lists pulsed UV explicitly out of scope; promotion to a Phase 4 candidate requires either a Council-3 Charter exception or explicit "parallel Raman sub-project" status, plus the multi-operating-point review (Δ ≫ Δ_ref). |
| [Requirements specification](requirements.html) | Shared requirements artefact for the slate above: per-architecture entries with task served, measurement plane, wavelength / detuning, output power or pulse energy, duration, environment, beam quality, linewidth / phase noise, degradation allowance, and evidence artefact. | **Living spec** — established 2026-05-08; all `REQ-NG-###`, `REQ-IC-###`, `REQ-PR-###` IDs traceable from architecture pages and logbook entries. |
| [BBO coating-run rationale](bbo-coating-run.html) | Public-facing explainer for the 2026-05-20 BBO ring coating-run work program. Walks through the cavity impedance-match math, shows how Friedenauer's procured M1' input coupler sits ~ 0.57 pp below the impedance-matched optimum at the published operating point (forfeiting ~ 3.6 % UV buildup), and explains the per-mirror loss-budget allocation, material recommendation, LIDT framing, and the cleanliness clause that drives the spec sheets. | **Closed** — work program executed and frozen on 2026-05-20; five vendor-facing pages live under [`logbook/2026-05-20-bbo-coating-run-wp/specs/`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/logbook/2026-05-20-bbo-coating-run-wp/specs). |

## Task-allocation sketch (for the slate of alternatives)

The next-generation workplan and the two alternative sketches imply different task allocations, summarised below:

| UV task | Friedenauer 2006 baseline | Next-gen workplan | IC-VECSEL + Pulsed-Raman pair |
|---|---|---|---|
| Doppler cooling | Single CW chain @ 280 nm | Single CW chain @ 280 nm | IC-VECSEL CW chain @ 280 nm (~ 50 mW, Δ_ref) |
| Repumping | Same CW chain | Same CW chain | IC-VECSEL CW chain |
| Photoionisation | Separate dye laser (per [Kief20]) | Separate VECSEL @ 1140 nm or equivalent | Separate VECSEL @ 1140 nm (per [Guth21] outlook) |
| Coherent Raman | Same CW chain | Same CW chain | Pulsed Ti:S comb @ ~ 290–320 nm (far-red-detuned, ≪ Γ_sc) |
| Total cavity-locks | 2 (LBO + BBO) | 2 | 1 (BBO PDH) + comb-internal locks |
| Operating points | One (Δ_ref = 40 GHz) | One (Δ_ref) | **Two** (Δ_ref for cooling/repumping; Δ ≫ Δ_ref for Raman) |

---

## Why a slate, not a single committed architecture

The CHARTER's anti-seeding clause ([Principles → Anti-seeding](../principles.html))
forbids architecture-family-specific simulation in `/src/` until G1
closes (the 14 GHz unlockable-domain attribution). This means
architecture work happens at three layers:

1. **Architecture-neutral primitives** in `/src/` — admissible pre-G1;
   used by all four pages here.
2. **Architecture-specific recomputation in `/notebooks/diagnostic/`** —
   admissible because notebooks are not in `/src/` and the cross-check
   *validates* the neutral primitives rather than committing to a
   build. Phase E and the Friedenauer recompute live here.
3. **Architecture-specific design exploration in
   `/notebooks/exploration/`** — admissible by the same boundary; Phase
   NG-* of the next-gen workplan and the alternative-topology sketches
   all live here once they reach the parameter-sweep stage.

Phase 4 architecture *comparison and scoring* is gated by G1, G2, G3.
G3 closed 2026-05-01; G1 and G2 are open. Until they close, all four
pages are inputs to a future scoring decision, not outputs of one. The
two alternative-topology sketches additionally depend on architecture-
neutral primitives (`shg_intracavity.py` for the IC-VECSEL alternative;
`pulsed_raman_kicks.py` for the pulsed-Raman alternative) that have not
yet been written; landing those primitives is a prerequisite for any
parameter-sweep exploration of the alternatives.

---

## How the four relate

The next-generation target uses Friedenauer 2006 as the **validation
anchor**: any cascade computation that fails to reproduce Friedenauer's
0.275 W BBO output (Phase E currently agrees to 1.5 %) does not get to
make recommendations about parameters that go beyond it. The
[Friedenauer page](friedenauer-2006.html) is therefore both *the
reference baseline* and *the test that any successor architecture must
keep passing on its CW SHG stages*.

The two alternative-topology sketches **decompose the CHARTER §1.5
≥ 500 mW indicative anchor** into a two-architecture task split:

- The [IC-VECSEL alternative](ic-vecsel-alternative.html) handles
  cooling and repumping at ~ 50 mW UV at the locked Δ_ref = 40 GHz
  operating point — well below the single-architecture 500 mW figure.
- The [pulsed-Raman alternative](pulsed-raman-alternative.html) handles
  coherent Raman at a separate far-red-detuned operating point, where
  Γ_sc is suppressed by ~ 10⁶ relative to Δ_ref and Ω_R is supplied by
  pulsed peak intensity rather than CW intensity.

The single-architecture [next-gen workplan](next-gen.html) remains the
load-bearing pre-G2 deliverable: its parameter-optimisation effort is
needed regardless of whether the eventual build is single-architecture
(next-gen workplan as-is) or two-architecture (IC-VECSEL + pulsed-Raman).
The slate-of-three is presented for steward and Council-3 deliberation,
not as a decision in advance of G1 / G2 closure.

The task-split disposition is in turn gated by the [Council-3 trigger filed
2026-05-09](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-09-council-3-trigger-task-split-success-criterion.md);
until that trigger is disposed, the IC-VECSEL alternative + pulsed-Raman
alternative pair sits as forward-looking sketches only, not as Phase 4
candidates.

---

## Traceability matrix — architecture parameters → Level 0 / Level 1 (P5)

Every parameter feeding into Phase 4 scoring traces back to a Level 0
(reference triple, locked at G3) or Level 1 (loss-budget-derived, source-
side-mapped) parent. The table below makes that lineage explicit so
sensitivity analyses on any architecture parameter can identify the
binding upstream constraint.

| Parameter | Architecture | Level 0 / 1 parent | If this drifts, what breaks? |
|---|---|---|---|
| `P_UV` = 500 mW (nominal) | Next-gen | Level 1 — UV power after loss budget | Raman Ω_R (overhead consumed); loss-budget headroom |
| `P_UV` = 50 mW (cooling + repump) | IC-VECSEL | Level 1 — same, under task split | Detection SNR, cooling rate |
| `P_visible` = 500 mW @ 559 nm | IC-VECSEL | Level 1 — derived from `P_UV` / η_BBO | Visible-stage scaling envelope; go/no-go thresholds |
| Δ_ref = 40 GHz | All CW chains | Level 0 — locked at G3 | Γ_sc, AC Stark shift |
| Δ ≈ 100 THz (~ 30 nm red) | Pulsed-Raman | Level 0 — tightened detuning at separate operating point | Ω_R (must be recovered by peak intensity) |
| Ω_R / 2π = 400 kHz | All | Level 0 — locked at G3 | Gate speed, scattering / gate |
| Γ_sc = 2.0 × 10⁴ s⁻¹ | All CW | Level 0 — locked at G3 | Gate fidelity |
| `S_φ(f) ≤ −101 dBc/Hz` | All | Level 0 — locked at G3 | Gate infidelity |
| `Δν_source` ≤ 500 kHz | All CW | Level 1 — absolute linewidth | Detection SNR, long-term drift |
| M² ≤ 1.2 | All | Level 1 — beam quality | Ion-side waist, Ω_R uniformity |
| `L_passive` per stage | Next-gen, IC-VECSEL | Level 1 — impedance match | Buildup, UV output, thermal load |
| `T_oven` stability | Next-gen, IC-VECSEL | Level 1 — thermal-load envelope | Phase-matching drift, output stability |
| `P_pump` ≤ 10 W | Next-gen | Level 1 — thermal-load envelope (`constraints/loss-budget.md` §3.1) | Crystal damage, coating degradation |
| Sealed-envelope class (UHV / N₂ purge / rough vacuum) | IC-VECSEL | Level 1 — UV robustness (G2-dependent) | Degradation rate, lifetime |
| `f_rep` jitter, `f₀` lock residual | Pulsed-Raman | Level 1 — timing stability | Motional dephasing |
| `τ_pulse`, `λ_fund` | Pulsed-Raman | Level 1 — derived from Δ, Ω_R | Conversion efficiency, spectral overlap |

Per-parameter detailed specs live in the [requirements
specification](requirements.html); per-architecture full Charter §9 /
Coastline / Sail / G1-G2-G3 statements live in each architecture page's
backing logbook entry.

---

## Phase 4 axis readiness checklist (P4)

The six fixed Phase 4 scoring axes (CHARTER §5.2, [`docs/principles.md`](../principles.html))
are not yet populated for the slate. The table below records each
axis × architecture cell with a draft state and the data source needed
to land a final score. **The slate is not opened for Phase 4 scoring
until every cell carries at least a draft value with citation.**

| Axis | Next-gen 500 mW | IC-VECSEL alternative | Pulsed-Raman alternative | Data source |
|---|---|---|---|---|
| **1 Raman capability** | TBD — depends on NG-C (IC reflectivity sweep) and NG-D (crystal geometry) results at 500 mW | N/A under task split — Raman task is offloaded; CW chain serves cooling + repumping only | TBD — depends on `pulsed_raman_kicks.py` primitive + multi-level ²⁵Mg⁺ model (`REQ-PR-009`) | Simulation in `/notebooks/exploration/`; literature ([Burd16] for CW; Monroe-group ultrafast extractions for pulsed) |
| **2 Phase coherence** | TBD — depends on rack-output linewidth and RIN (`REQ-NG-003`) | TBD — depends on PDH residual phase noise (`REQ-IC-003` adjacent) and IC-VECSEL inherent linewidth | TBD — depends on f_rep / f₀ lock residuals (`REQ-PR-006`) and timing-jitter spectrum (`REQ-PR-007`) | Phase 2 baseline measurement (CW); vendor + bench-test (pulsed) |
| **3 UV robustness** | TBD — bounded by NG-E loss-budget anchoring + G2-closure outcome | **Better** — sealed envelope is architectural mitigation for surface-contamination LIDT; atmosphere-class-A or B per [Burk21] | **Worse** — pulsed peak fluence may accelerate degradation; mitigation requires larger spot or lower rep rate | G2-closure measurement campaign + [Brow19] / [Burk21] / [Turc22] envelope |
| **4 Thermal / nonlinear load** | TBD — depends on NG-D (crystal geometry sweep and walk-off penalty factor) at 500 mW | **Lower** — 50 mW UV target reduces thermal stress at the BBO output; 500 mW visible target inside the [Burd16] envelope only if `REQ-IC-003` activates | **Lower** — no buildup cavities mean no IC mode-matching thermal load; pulsed average power modest (≤ 0.5 W UV) | Simulation in `/notebooks/exploration/`; ABCD stability budget |
| **5 Tunability / modularity** | TBD — depends on operational tuning range at the 500 mW operating point | **Good** — VECSEL mode-hop-free range (~ 1 GHz piezo, ~ 10 GHz etalon) carries through; 50 mW headroom allows operational tuning | **Excellent** — comb-tooth selection allows GHz-scale fine tuning; coarse Ti:S range 870–960 nm | Literature ([Burd23], [Span25]); vendor specs (Ti:S) |
| **6 Complexity** | TBD — count of cavity locks, BOM, alignment surfaces at the 500 mW recommendation point | TBD — sealed envelope + thermal-isolation engineering offsets cavity-count reduction; needs explicit BOM count | TBD — comb lock + tripler + dispersion management; offsets buildup-cavity removal | Component count + BOM analysis |

**Status legend:** `Better` / `Worse` / `Lower` / `Higher` are *qualitative* indicators relative to the [Friedenauer 2006 baseline](friedenauer-2006.html); each must be replaced with a quantitative score before Phase 4 scoring is admissible. `TBD` cells block slate opening per the recommendation in the [2026-05-08 review](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-architecture-review-tightening-specs.md) §4.3.

---

## Deferred items from the 2026-05-08 review

The review's priority items P7–P9 require implementation work that is
not in scope for the spec-tightening pass landed 2026-05-09:

| Item | Scope | Why deferred |
|---|---|---|
| **P7 — NG-B forward map with hard 10 W pump ceiling + Yb-fibre vs VECSEL ASE bifurcation** | Notebook implementation in `/notebooks/exploration/` | Requires the next-gen workplan's Phase NG-A (LBO `L_passive` gap) to land first; the tightening is captured in the requirements page (`REQ-NG-001`, `REQ-NG-002`) and as a Phase plan item in [`logbook/2026-05-08-next-gen-500mW-workplan.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md). |
| **P8 — Thermal-isolation FEA + thermal-resistance budget for IC-VECSEL** | Mechanical / thermal CAD + FEA simulation | Requires CAD-layer work outside the documentation pass; the spec target is captured in [`REQ-IC-004`](requirements.html#req-ic-004--thermal-isolation-150-c-lbo-oven-vs-gain-mirror-peltier) (target: gain-mirror drift < 1 mK with LBO oven at full power). |
| **P9 — Timing-jitter budget + lock-architecture choice for pulsed-Raman** | Literature extraction (Monroe-group ultrafast Raman papers `[Haye10]` / `[Camp10]` / `[Mizr13]` / `[Inle14]`) + lock-architecture spec | Requires the literature extraction batch flagged in [`logbook/2026-05-08-pulsed-raman-alternative-topology.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-pulsed-raman-alternative-topology.md) §11. The spec hooks live at [`REQ-PR-006`](requirements.html#req-pr-006--repetition-rate--ceo-lock-residuals) and [`REQ-PR-007`](requirements.html#req-pr-007--timing-jitter-spectrum). |

The `TBD` flags in the Phase 4 axis readiness checklist above point at these deferred items where applicable; closing the deferred items is what closes the corresponding `TBD` cells.
