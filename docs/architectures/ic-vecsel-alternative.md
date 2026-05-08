---
layout: default
title: IC-VECSEL alternative — intracavity LBO + free-space PDH-locked BBO in a sealed 19" rack envelope
description: Architecture sketch — an intracavity-doubled VECSEL (1118 nm + intracavity LBO -> 559 nm direct) feeding a free-space PDH-locked BBO ring inside a sealed, temperature-controlled 19" rack envelope. Sized for cooling + repumping at ~ 50 mW UV; Raman handled by a parallel pulsed-comb pathway.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page is an architecture sketch, not a build commitment. Phase 4 architecture scoring is gated by G1 / G2; this candidate is an <em>input</em> to a future scoring decision, not an output of one.</p>

<p class="eyebrow">Architecture · sketch</p>

# IC-VECSEL alternative — intracavity LBO + free-space PDH-locked BBO

**Status:** SKETCH (logbook entry [`logbook/2026-05-08-ic-vecsel-alternative-topology.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-ic-vecsel-alternative-topology.md) carries the full Charter §9 trigger questions, Coastline / Sail labels, and G1-G2-G3 boundary statements; this page is the public surface).

**Charter compliance.** Reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is unaffected. **Level 1 is affected conditionally**: the chain's ~ 50 mW UV output is below the CHARTER §1.5 ≥ 500 mW indicative anchor and is **valid only as a paired task allocation** with the [pulsed-Raman alternative](pulsed-raman-alternative.html) (or an equivalent off-board Raman pathway). Without that pairing, this sketch underdelivers Level 1. Anti-seeding clause (`docs/principles.md` §5.1) is in force — no `/src/architecture/` code follows from this sketch.

---

## Concept

Replace the three-cavity Friedenauer chain (Yb-fibre seed → external LBO ring → external BBO ring) with **two cavities only**: an **intracavity-doubled VECSEL** whose linear cavity contains an LBO crystal producing 559 nm directly out of the gain-mirror cavity, plus a **free-space PDH-locked BBO ring** in tight integration. Everything sits inside a temperature-controlled, evacuated-or-inert-gas-purged 19" rack envelope.

## Task scope and revised power target

This option is sized for **cooling and repumping only**. The Raman task moves to the parallel [pulsed-Raman alternative](pulsed-raman-alternative.html) operating at a far-red-detuned point. The **UV** power target for *this* chain shrinks accordingly to **~ 50 mW @ ~ 280 nm**, well below the CHARTER §1.5 ≥ 500 mW indicative anchor (which assumed a single-architecture all-tasks chain).

The visible-stage requirement does **not** shrink proportionally. The BBO buildup cavity at the in-house operating point converts only ~ 10 % of input visible to UV: [[Guth21]](../references.html#guth21) §3.4 measured 78(5) mW UV from 780(15) mW visible (10.0(11) %); [[Frie06]](../references.html#frie06) reports ≥ 100 mW UV from 1.4 W visible (~ 7 %). To deliver 50 mW UV the BBO ring must therefore see **~ 500 mW @ 559 nm** at its input. The implied stage-by-stage budget for this sketch is:

| Stage | Power |
|---|---|
| IC-VECSEL direct output (intracavity-doubled) | ~ 500 mW @ 559 nm |
| Free-space coupling to BBO ring (no fibre loss) | ~ 500 mW @ 559 nm |
| BBO ring output at ~ 10 % visible-to-UV | **~ 50 mW @ ~ 280 nm** |

The visible-output-scaling question therefore **remains** the dominant open-question concern for the IC-VECSEL topology at this operating point. [[Burd16]](../references.html#burd16) reported ~ 30–80 mW direct visible from the 1117 nm IC topology; extending this to ~ 500 mW is a ~ 5–10× scaling step that is the principal numerical target of the open `shg_intracavity.py` notebook exploration. At the W-class intracavity IR circulation consistent with [[Span25]](../references.html#span25) gain-mirror operating points, ~ 500 mW direct intracavity-doubled visible appears achievable in principle (industrial DPSS-green intracavity-LBO at 532 nm at multi-W is mature in adjacent fields) — but is **not directly demonstrated** for the 1118 nm operating point.

What does relax at the 50 mW UV target:

- The UV-side operating point ≤ 50 mW sits comfortably below typical CW BBO LIDT bounds ([[Eime87]](../references.html#eime87), [[Turc22]](../references.html#turc22)) and within the surface-contamination-limited regime where [[Burk21]](../references.html#burk21)-style atmosphere control is the effective lever.
- BBO mirror coatings, crystal length, and waist can be chosen for *operational longevity* rather than peak conversion efficiency.
- Sensitivity to BBO efficiency is high: if hard-fluoride coatings + tighter waist push the BBO to 20–30 % visible-to-UV (a 2–3× improvement above the [Guth21] / [Frie06] envelope), the IC-VECSEL visible target relaxes to ~ 170–250 mW — inside the [Burd16] precedent envelope.

In Charter terms this is *not* a relaxation of the reference triple — Level 0 and Level 1 for the cooling-and-repumping task are unaffected. What changes is the **task allocation between architectures**: cooling+repumping → this CW chain at ~ 50 mW UV (~ 500 mW visible); Raman → pulsed chain at the red-detuned operating point. The 500 mW UV anchor of CHARTER §1.5 was a single-architecture figure; the slate-of-three approach decomposes it.

## Topology

```
[ TEMPERATURE-CONTROLLED, VACUUM / N2 / Ar-PURGED 19-INCH RACK ENVELOPE ]

  808 nm pump fibre
        │
        ▼
  ┌──────────────────────────────────────────┐
  │  IC-VECSEL CAVITY (single cavity)        │
  │  Vexlum gain mirror @ 1118 nm  ┐         │
  │  Newlight BIR0030 BRF          │         │
  │  LightMachinery YAG etalon     │         │
  │  Intracavity LBO Type-I NCPM   │         │
  │       (~ 150 °C oven)          │         │
  │  Dichroic OC: HR @1118, HT @559│         │
  │  PZT-tuned cavity length       │         │
  │       │                                  │
  │       ▼  ~ 500 mW @ 559 nm direct out    │
  │          (BBO ~ 10 % visible-to-UV       │
  │           per [Guth21] / [Frie06])       │
  └───────┼──────────────────────────────────┘
          │
          ▼   Optical isolator (visible)
          ▼   EOM (PDH sideband generator)
          │
  ┌───────┼──────────────────────────────────┐
  │  FREE-SPACE BBO RING BUILDUP CAVITY      │
  │  Brewster-cut β-BBO Type-I CPM           │
  │  Hard fluoride coatings ([Burk21])       │
  │  PDH-locked (EOM at ~ 10–50 MHz)         │
  └────────────────────┼─────────────────────┘
                       ▼
                 ~ 50 mW @ ~ 280 nm
                 Cooling + repumping only
```

## What it inherits from the steward direction

- VECSEL is the seed-laser source class per the [steward direction recorded 2026-05-08](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-vecsel-seed-lasers.md) and the [seed-lasers components page](../components/seed-lasers.html).
- Class-A laser dynamics, intracavity BRF + 1 mm YAG etalon + PZT mode selection — all per [[Burd23]](../references.html#burd23) design principles.
- In-house BOM continuity from [[Kief20]](../references.html#kief20) / [[Guth21]](../references.html#guth21) / [[Span23]](../references.html#span23) / [[Span25]](../references.html#span25).

## What it changes vs the Friedenauer baseline + the existing next-gen workplan

| Element | [Friedenauer 2006 baseline](friedenauer-2006.html) | [Next-gen 500 mW workplan](next-gen.html) | This sketch |
|---|---|---|---|
| Task scope | All UV tasks | All UV tasks | **Cooling + repumping only** |
| UV target | ≈ 0.275 W (as published) | ≥ 500 mW | **~ 50 mW** |
| Cavity count | 3 (fibre seed + LBO + BBO) | 3 (VECSEL seed + LBO + BBO) | **2 (IC-VECSEL + BBO)** |
| Visible-cavity locking | HC | HC | **(none — intracavity SHG)** |
| BBO-cavity locking | HC | HC | **PDH (EOM-modulated)** |
| Stage-to-stage coupling | Fibre | Free space | **Free space, tightly integrated** |
| Atmosphere | Lab air | Lab air | **Vacuum or N2 / Ar purge** |
| Form factor | Optical table | A4 + 19" rack | **Single sealed 19" rack box** |

## Status

| Item | State |
|---|---|
| Architecture sketch logged | ✅ done — [logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-ic-vecsel-alternative-topology.md) |
| `shg_intracavity.py` architecture-neutral primitive in `/src/` | ⏳ open follow-up |
| Notebook exploration of intracavity-LBO output | ⏳ open follow-up — **baseline ~ 500 mW @ 559 nm at the BBO input** (assumes [Guth21] ~ 10 % BBO efficiency); sensitivity case ~ 170–250 mW visible **only after** measured BBO efficiency 20–30 % is demonstrated. |
| 1118 nm Type-I NCPM LBO temperature from [[Eime87]](../references.html#eime87) Sellmeier | ⏳ open follow-up |
| 559 nm vacuum-compatible EOM vendor short list | ⏳ open follow-up |
| Hard-fluoride-coating vendor short list at 559 / 280 nm | ⏳ open follow-up |
| Phase 4 candidate-slate opening | ⏳ gated by G1 + G2 closure |

## Boundaries (what this page is **not**)

- **Not Phase 4 architecture scoring.** Gated by G1 + G2.
- **Not architecture-family-specific code in `/src/`.** All numerical work for this candidate lives in `/notebooks/exploration/` per CHARTER §5.1.
- **Not a build commitment.** The sketch is exploration only; build/buy decisions sit downstream.
- **Not a UV-degradation analysis.** G2-dependent; the sealed envelope is a *candidate* G2 mitigation but does not close G2.
- **Not a replacement for the [next-gen 500 mW workplan](next-gen.html).** That workplan optimises parameters within the Friedenauer two-cavity topology at the single-architecture all-tasks ≥ 500 mW target. This sketch is an alternative-topology candidate paired with the pulsed-Raman alternative under a two-architecture task split.

## See also

- [Pulsed-Raman alternative](pulsed-raman-alternative.html) — the parallel pathway that handles the Raman task at the far-red-detuned operating point.
- [Friedenauer 2006 baseline](friedenauer-2006.html) — the architecture being departed from.
- [Next-gen 500 mW workplan](next-gen.html) — the Friedenauer-topology parameter-optimisation pre-G2 deliverable.
- [Components → Seed lasers (VECSEL)](../components/seed-lasers.html) — the seed-laser source-class steward direction this sketch sits inside.
- [References](../references.html) — alphabetical literature index.
- [Logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-ic-vecsel-alternative-topology.md) — full Charter §9 / Coastline / Sail / G1-G2-G3 statements.
