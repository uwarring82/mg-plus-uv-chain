---
layout: default
title: Architectures
description: Two doubling-stage UV source architectures — the Friedenauer 2006 baseline as published, and the next-generation 500 mW @ 280 nm target derived from the CHARTER §1.5 indicative anchor.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. Architecture pages here describe a published baseline and a parameterised next-generation target; neither is a build commitment, and neither has been admitted to Phase 4 architecture scoring (G1 still open).</p>

<p class="eyebrow">Architectures</p>

# Architectures

Two architecture stories live here. They share the same physics — a CW
two-stage SHG chain 1118 nm → 559 nm → 280 nm — and the same
architecture-neutral primitives in [`/src/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/).
What differs is *where each one sits in the project lifecycle*.

| Page | What it is | Status |
|---|---|---|
| [Friedenauer 2006](friedenauer-2006.html) | The published all-solid-state architecture: 2 W Yb fibre at 1118 nm → LBO → BBO → 0.275 W at ~ 280 nm. The reference baseline our recomputation [validates against](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py). | **Reference baseline** — extraction and cross-check live; one open `L_passive` definitional gap to close. |
| [Next-generation](next-gen.html) | A parameterised target: ≥ 500 mW UV at 280 nm via the same two-stage SHG topology, with the input pump, IC reflectivities, and crystal geometry derived from the architecture-neutral primitives. | **In design** — workplan drafted ([`logbook/2026-05-08-next-gen-500mW-workplan.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md)); not yet executed. |

---

## Why these two and not more

The CHARTER's anti-seeding clause ([Principles → Anti-seeding](../principles.html))
forbids architecture-family-specific simulation in `/src/` until G1
closes (the 14 GHz unlockable-domain attribution). This means
architecture work happens at three layers:

1. **Architecture-neutral primitives** in `/src/` — admissible pre-G1;
   used by both pages here.
2. **Architecture-specific recomputation in `/notebooks/diagnostic/`** —
   admissible because notebooks are not in `/src/` and the cross-check
   *validates* the neutral primitives rather than committing to a
   build. Phase E and the Friedenauer recompute live here.
3. **Architecture-specific design exploration in
   `/notebooks/exploration/`** — admissible by the same boundary; Phase
   NG-* of the next-gen workplan will live here.

Phase 4 architecture *comparison and scoring* is gated by G1, G2, G3.
G3 closed 2026-05-01; G1 and G2 are open. Until they close, both pages
are inputs to a future scoring decision, not outputs of one.

---

## How the two relate

The next-generation target uses Friedenauer 2006 as the validation
anchor: any cascade computation that fails to reproduce Friedenauer's
0.275 W BBO output (Phase E currently agrees to 1.5 %) does not get to
make recommendations about parameters that go beyond it. The
[Friedenauer page](friedenauer-2006.html) is therefore both *the
reference baseline* and *the test the next-gen exploration must keep
passing*.
