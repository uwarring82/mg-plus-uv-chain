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
| [Pulsed-Raman alternative](pulsed-raman-alternative.html) | An alternative-topology sketch for the *Raman task only*: phase-locked mode-locked Ti:Sapphire frequency comb single-pass tripled to ~ 290–320 nm, operated tens of nm red-detuned. Pulsed peak intensity supplies Ω_R; Γ_sc suppressed by ~ 10⁶ vs Δ_ref. | **Sketch** — [logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-pulsed-raman-alternative-topology.md) carries full Charter §9 statements; promotion *additionally* requires Council-3 review of the multi-operating-point question (Δ ≫ Δ_ref). |

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
