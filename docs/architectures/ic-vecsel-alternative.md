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

## Visible-power go/no-go boundaries (P3 from 2026-05-08 review)

The ~ 500 mW @ 559 nm visible target is **derived**, not free: `P_visible = P_UV_target / η_BBO`. Bounding η_BBO at the in-house operating point gives explicit go/no-go thresholds that the IC-VECSEL must clear before the architecture is admissible:

| BBO efficiency η_BBO | Required P_visible (for 50 mW UV) | Status of the IC-VECSEL output requirement |
|---|---|---|
| 30 % (optimistic, [Burk21]-style hard fluoride + tight waist) | 167 mW | **Inside [Burd16] envelope** (~ 30–80 mW) → modest scaling; viable |
| 20 % (optimistic-conservative midpoint) | 250 mW | **At [Burd16] envelope upper edge** → still viable but no headroom |
| 10 % ([Guth21] in-house operational) | 500 mW | **~ 5–10× beyond [Burd16] envelope** → scaling is the load-bearing question |
| 7 % ([Frie06] published) | 714 mW | **~ 10× beyond [Burd16] envelope** → conservative-case requirement |

**Decision rule (binding for the architecture's admissibility):**

- If the IC-VECSEL **cannot deliver > 250 mW visible** at 559 nm at the operating point: the architecture **fails even at the optimistic (η_BBO = 20 %) BBO efficiency**.
- If the IC-VECSEL **cannot deliver > 170 mW visible**: the architecture **fails even at the most-optimistic plausible (η_BBO = 30 %) efficiency** and is therefore **not admissible** as a Phase 4 candidate.
- The 500 mW visible figure is the **conservative-case** target consistent with the demonstrated in-house [Guth21] BBO efficiency; until a higher BBO efficiency is *measured*, the conservative target binds.

These thresholds are the go/no-go numbers the open `shg_intracavity.py` notebook exploration must compute against. **Until the primitive lands and a sweep at the 1118 nm intracavity-doubled operating point reports the achievable visible output with sensitivity envelope, the ~ 500 mW visible figure is unfalsifiable** and the architecture cannot be promoted to a Phase 4 candidate. See `REQ-IC-001` and `REQ-IC-003` in the [requirements specification](requirements.html) for the formal spec hooks.

## G1 inheritance and G2-failure impact (P1 from 2026-05-08 review)

**G1 inheritance.** This sketch holds the BBO ring + 559 nm input geometry topologically equivalent to the [Friedenauer 2006 baseline](friedenauer-2006.html); the 14 GHz unlockable-domain anomaly (CHARTER §8.1) is therefore **inherited unchanged** at the BBO stage. The IC-VECSEL replaces the Yb-fibre + external LBO ring upstream, which removes one cavity-locking surface from the G1 search space, but the BBO-stage anomaly carries forward. G1 closure remains a Phase 2 discriminant-scan task, not a simulation task.

**G2-failure impact.** The sketch's sealed-envelope atmosphere control is a *candidate* G2 mitigation, not a closure. If G2 closes at a worse-than-hoped degradation rate, the impact on this architecture is bounded as follows:

| If G2 closes at … | Impact on the IC-VECSEL alternative | Mitigation already in design | Fallback |
|---|---|---|---|
| ≤ 5 %/100 h UV-output drop | Marginal — sealed envelope absorbs most of the stress; 50 mW UV cooling target stays viable for ≥ 1000 h between maintenance | Atmosphere class A (UHV) or B (N₂ purge) per [Burk21] | None needed |
| 10–20 %/100 h | Manageable — sealed envelope insufficient on its own; need hard-fluoride coatings + tighter waist + reduced visible drive | Promote atmosphere class to A; relax `REQ-IC-001` only if `REQ-IC-003` escape clause activates | Increase visible drive to compensate; accept shorter BBO-mirror life |
| > 20 %/100 h | Architecture failure-mode envelope exceeded; UV output drops below 40 mW within < 200 h | Architectural change required (e.g. switch to single-pass UV with build-up only at 559 nm) | Architecture withdrawn; cooling falls back to next-gen Friedenauer-topology chain |

The sealed envelope reduces the *probability* of the higher-rate scenarios but does not eliminate them; G2 closure measurement is what bounds the actual rate.

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
