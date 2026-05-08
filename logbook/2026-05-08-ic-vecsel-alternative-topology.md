# Alternative next-gen topology — IC-VECSEL with intracavity LBO + free-space PDH-locked BBO in a sealed 19" rack envelope

**Steward:** Ulrich Warring
**Date:** 2026-05-08
**Status:** SKETCH (architecture exploration; no build commitment, no `/src/` code)

## Header (Charter §9 trigger questions)

- **Affects Level 0 parameter?** no — reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is unaffected.
- **Affects Level 1 parameter?** no — UV target ≥ 500 mW @ 280 nm and source linewidth budget unchanged. This sketch explores *one alternative topology* for reaching those targets.
- **Affects success criterion?** no.

This entry sits **alongside** the [next-gen 500 mW workplan](2026-05-08-next-gen-500mW-workplan.md), which optimises parameters *within* the Friedenauer two-cavity topology. The present sketch proposes a **different topology** — to be evaluated as a Phase 4 architecture-comparison candidate once G1 and G2 close. The anti-seeding clause (`docs/principles.md` §5.1) is in force throughout: no `/src/architecture/` code follows from this sketch.

---

## 1 · Concept in one sentence

Replace the three-cavity Friedenauer chain (Yb-fibre seed → LBO ring → BBO ring) with **two cavities only** — an **intracavity-doubled VECSEL** whose linear cavity contains an LBO crystal producing 559 nm directly out of the gain-mirror cavity, plus a **free-space PDH-locked BBO ring** in tight integration — all sealed inside a temperature-controlled, evacuated-or-inert-gas-purged 19" rack envelope.

## 1a · Task scope and revised power target *(steward direction 2026-05-08)*

This option is sized for **cooling and repumping only**. The Raman-task power requirement is offloaded to the [pulsed-Raman alternative](2026-05-08-pulsed-raman-alternative-topology.md) (a separate far-red-detuned mode-locked-comb pathway), so the UV power target for *this* chain shrinks from the CHARTER §1.5 indicative anchor (≥ 500 mW for the all-in-one chain) to the cooling-and-repumping-only requirement of **~ 50 mW @ ~ 280 nm**.

The reduced target materially relaxes the design envelope:

- Intracavity LBO output near **50–100 mW @ 559 nm** is sufficient to feed the BBO ring; at this scale the IC-VECSEL operates inside the [Burd16] envelope (~ 30–80 mW visible direct from the IC topology) rather than ~ 10× beyond it. The previous-version output-scaling concern is largely retired.
- Intracavity power circulation is correspondingly lower; thermal coupling between the LBO oven and the gain-mirror Peltier eases.
- The BBO buildup-cavity demand drops; conversion need is ~ 50 mW UV / ~ 100 mW visible ≈ 50 % visible-to-UV at modest enhancement, well within typical Friedenauer-class BBO performance.
- Combined with the sealed envelope, the ≤ 50 mW operating point sits comfortably below typical CW BBO LIDT bounds ([Eime87], [Turc22]) and within the surface-contamination-limited regime where [Burk21]-style atmosphere control is the effective lever.

In Charter terms this is *not* a relaxation of the reference triple — Level 0 (Δ_ref, Ω_R, Γ_sc) and Level 1 (UV at experiment input, beam quality, source linewidth) for the cooling-and-repumping task are unaffected. What changes is the **task allocation between architectures**: cooling+repumping → this CW chain at ~ 50 mW; Raman → pulsed-comb chain at the red-detuned operating point. The 500 mW anchor of CHARTER §1.5 was a single-architecture figure; the slate-of-three approach decomposes it.

## 2 · Topology sketch

```
[ TEMPERATURE-CONTROLLED, VACUUM / N2 / Ar-PURGED 19-INCH RACK ENVELOPE ]

  808 nm pump fibre
        │
        ▼
  ┌──────────────────────────────────────────┐
  │  IC-VECSEL CAVITY (single cavity)        │
  │                                          │
  │  Vexlum gain mirror ──┐                  │
  │       (1118 nm)        │                 │
  │                        │                 │
  │  ┌───────────────┐     │                 │
  │  │ BRF (Newlight)│     │                 │
  │  └───────────────┘     │                 │
  │  ┌───────────────┐     │                 │
  │  │ Etalon (LM)   │     │                 │
  │  └───────────────┘     │                 │
  │  ┌───────────────┐     │                 │
  │  │ Intracavity   │  high-IR                │
  │  │ LBO crystal   │  circulation           │
  │  │ Type-I NCPM   │  (~ 100 W class)       │
  │  │ ~ 150 °C oven │     │                 │
  │  └───────────────┘     │                 │
  │  ┌───────────────┐     │                 │
  │  │ Dichroic OC:  │     │                 │
  │  │ HR @1118 nm   │     │                 │
  │  │ HT @559 nm    │     │                 │
  │  └───────────────┘                       │
  │       │                                  │
  │       ▼                                  │
  │  ~ 0.5 – 1 W @ 559 nm direct out         │
  └───────┼──────────────────────────────────┘
          │
          ▼   Optical isolator (visible, vacuum-compatible)
          │
          ▼   EOM — PDH sideband generator @ 10 – 50 MHz
          │
  ┌───────┼──────────────────────────────────┐
  │  FREE-SPACE BBO RING BUILDUP CAVITY      │
  │                                          │
  │  Brewster-cut β-BBO, Type-I CPM          │
  │  Hard fluoride coatings ([Burk21])       │
  │  PDH lock — error signal from cavity     │
  │  reflection, demodulated against EOM     │
  │  drive frequency                         │
  └────────────────────┼─────────────────────┘
                       ▼
                ~ 50 mW @ ~ 280 nm
                (cooling + repumping target;
                 Raman task moves to pulsed alternative)
```

## 3 · What carries over from the steward direction

- VECSEL is the seed-laser source class per the steward direction recorded 2026-05-08 ([logbook entry](2026-05-08-vecsel-seed-lasers.md), components page [`docs/components/seed-lasers.md`](../docs/components/seed-lasers.md)).
- Class-A laser dynamics, intracavity BRF + 1 mm YAG etalon + PZT mode selection, diamond-bonded Vexlum gain mirror — all per [Burd23] design principles.
- In-house BOM continuity from [Kief20] / [Guth21] / [Span23] / [Span25]: Vexlum gain mirror, Newlight BIR0030 BRF, LightMachinery OP-3167-1000 etalon, Ostech 808 nm pump.
- Dry-gas (or vacuum) purge of the laser envelope per [Burd23] §2 and [Burk21].

## 4 · What changes vs the Friedenauer baseline and the existing next-gen workplan

| Element | [Frie06] baseline | Existing [next-gen workplan](2026-05-08-next-gen-500mW-workplan.md) | This alternative sketch |
|---|---|---|---|
| Task scope | All UV tasks (cooling, repumping, Raman, photoionisation) | All UV tasks | **Cooling + repumping only; Raman handled by [pulsed alternative](2026-05-08-pulsed-raman-alternative-topology.md)** |
| UV power target | ~ 0.275 W (as published) | ≥ 500 mW (Charter §1.5 anchor) | **~ 50 mW (cooling + repumping only)** |
| Seed → visible | Yb-fibre 1118 nm → LBO ring (HC-locked) | VECSEL 1118 nm → LBO ring (HC-locked) | **IC-VECSEL with intracavity LBO; no external visible buildup cavity** |
| Visible → UV | BBO ring (HC-locked) | BBO ring (HC-locked) | **BBO ring (PDH-locked, EOM-modulated)** |
| Cavity count | 3 | 3 | **2** |
| Stage-to-stage coupling | Fibre | Free space | **Free space, tightly integrated** |
| Atmosphere | Lab air | Lab air (TEC-stabilised) | **Vacuum or N2 / Ar purge** |
| Form factor | Optical table | A4 + 19" rack ([Span25]) | **Single sealed 19" rack box** |

## 5 · Coastline claims *(testable design constraints inherited from precedent)*

- **Intracavity-doubled VECSEL at this wavelength is precedented.** [Burd16] demonstrated an IC-VECSEL at 1117 nm producing 558.5 nm intracavity-doubled output (then externally to 280 nm) in the same NIST + Tampere collaboration that anchors [Burd23]. The IC topology is not exotic; the 1 nm offset to 1118 nm is well within the gain-mirror MBE tolerance.
- **PDH on a deep-visible BBO cavity is precedented and higher-bandwidth than HC.** [Burd23] §3 used PDH on the first-stage PPKTP enhancement cavity at 940 nm precisely because the dispersive PDH error signal survives depleted-pump conditions that stress the polarisation-sensitive Hänsch-Couillaud signal. The cost is one EOM at 559 nm and demodulation electronics.
- **UV-induced contamination is mitigated by atmosphere control.** [Burk21] demonstrated stable deep-UV enhancement-cavity operation in UHV with hard fluoride mirror coatings; [Brow19] showed surface contamination is the dominant LIDT precursor, not bulk-crystal LIDT ([Eime87] [Turc22]). Sealing the envelope closes this channel architecturally.

## 6 · Sail recommendations *(adaptive guidance, contextual to this sketch)*

- **Type-I non-critical phase-matched (NCPM) LBO at ≈ 150 °C** inside the VECSEL cavity — eliminates walk-off and matches the high intracavity beam-quality requirement; thermal load handled by an isolated oven mount that does not couple back into the gain-mirror Peltier.
- **Hard fluoride mirror coatings** on the BBO ring per [Burk21]; oxide IBS coatings degrade faster under deep-UV.
- **Raspberry-Pi-based controller** ([Span25] precedent) handles VECSEL TECs *and* BBO PDH demodulation in software at the < 100 kHz cavity-lock bandwidth — extending the [Span25] cost / integration profile.
- **Rough vacuum (1–10 mbar)** preferred over inert-gas purge if vacuum-compatible EOM and isolator are sourced; otherwise N2 or Ar purge with clean-gas plumbing through the rack envelope.

## 7 · Tradeoffs vs the existing next-gen workplan

**Pros**

- **One fewer cavity-lock loop** — the external LBO buildup cavity goes away; only the BBO cavity is locked.
- **No fibre between stages** — eliminates the 20–25 % fibre-coupling loss observed in [Guth21] Table 8.
- **Tight integration in single envelope** — reduces inter-stage alignment drift, mechanical-noise pickup, and air-path contamination.
- **G2 mitigation is architectural, not just operational** — the sealed envelope addresses UV-induced degradation at the design level rather than via cleanliness procedures.

**Cons / open questions**

- **Intracavity-LBO ↔ gain-mirror thermal coupling.** Both elements share one cavity; the LBO oven (~ 150 °C, NCPM Type-I) and the gain-mirror Peltier (~ 20 °C) need careful thermal isolation. No precedent in the in-house chain; needs notebook simulation before sweeping.
- **Visible-output scaling — largely retired at the 50 mW UV target.** [Burd16] IC-VECSEL at 1117 nm produced ~ 30–80 mW visible (chain-configuration-dependent). Reaching ~ 0.5–1 W direct intracavity-doubled output at 559 nm would have extended [Burd16] performance by ~ 10× — but with the cooling-and-repumping-only task allocation (§1a), the visible-stage requirement collapses to ~ 50–100 mW @ 559 nm, comfortably inside the [Burd16] envelope. This was the dominant open-question concern in the pre-task-scoping sketch and is now relaxed.
- **PDH at 559 nm adds RF.** EOM drive at 10–50 MHz and demodulation electronics inside the rack envelope add RF-noise-pickup risk; shielding and grounding need design.
- **Vacuum / purge plumbing in 19" rack.** Sealed envelope adds feedthrough complexity (pump fibre, PDH error-signal cable, TEC controllers, gas line). N2 / Ar flow is simpler but consumes gas.
- **Phase 4 axis 6 (complexity)** trades *cavity count* for *envelope complexity* — net axis-6 score not obvious without explicit scoring.

## 8 · Anti-seeding clause / G1-G2-G3 boundaries

- **No `/src/architecture/` code.** All numerics for this alternative live in `/notebooks/exploration/` per CHARTER §5.1. The architecture-neutral primitive set (`shg_cascade.py`, `enhancement_cavity.py`, `boyd_kleinman.py`) covers the BBO stage; **intracavity SHG would need a new architecture-neutral primitive** (e.g. `shg_intracavity.py`) before any parameter sweep on this candidate is meaningful.
- **G1 (14 GHz unlockable resonance).** Independent of topology choice; this sketch does not advance G1 closure.
- **G2 (UV-induced degradation).** The sealed envelope is a *candidate* G2 mitigation, but G2 closure requires *measurement* in Phase 2, not architecture choice. This sketch does not close G2.
- **G3 (reference triple).** Locked 2026-05-01; unaffected.
- **Phase 4 architecture comparison.** This candidate joins the slate alongside the existing-next-gen Friedenauer-topology + the named alternatives (PPLN-MgO, PPKTP, single-pass UV with buildup only at 559 nm). Slate is opened *after* G1 and G2 close.

## 9 · Where this sits in the project

- **Not** a replacement for the [next-gen 500 mW workplan](2026-05-08-next-gen-500mW-workplan.md). That workplan optimises *parameters within* the Friedenauer two-cavity topology at the all-tasks ≥ 500 mW UV target and remains the load-bearing pre-G2 deliverable for the single-architecture path.
- **Is** an alternative-topology candidate that, paired with the [pulsed-Raman alternative](2026-05-08-pulsed-raman-alternative-topology.md), decomposes the CHARTER §1.5 ≥ 500 mW indicative anchor into a two-architecture task split (cooling + repumping ~ 50 mW here; Raman ~ 500 mW-equivalent peak intensity at the red-detuned point in the pulsed pathway).
- **Status:** SKETCH. Promotion to a full architecture-comparison entry waits on (i) the new `shg_intracavity.py` primitive landing in `/src/`, (ii) at least one notebook in `/notebooks/exploration/` exercising the IC-VECSEL parameter envelope at 1118 nm against 559 nm output (now at the relaxed ~ 50–100 mW visible target), and (iii) Phase 4 candidate-slate opening (G1 + G2 closed).

## 10 · Open follow-ups

- Compute the 1118 nm Type-I NCPM phase-matching temperature for LBO from [Eime87] Sellmeier coefficients; verify ~ 150 °C is in range and check temperature sensitivity.
- Survey commercial 559 nm broadband EOMs (Qubig, Eospace, Jenoptik, custom RTP) for vacuum-compatible packaging and PDH-class modulation depth.
- Survey hard-fluoride-coating vendors at 559 nm input + 280 nm output ([Burk21] cited supplier as a starting point).
- Specify the **architecture-neutral primitive `shg_intracavity.py`** requirements; this is a `/src/` follow-up that respects the anti-seeding clause (it is *neutral* to architecture choice — it computes intracavity SHG given input parameters, not specific to IC-VECSEL topology).
- Cross-reference this sketch from the Phase 4 candidate-slate landing whenever that opens.

## 11 · References

This sketch leans on the cluster of literature already in [`docs/references.html`](../docs/references.html). Citation labels follow the index convention.

- **[Burd16]** — wavelength-adjacent IC-VECSEL precedent at 1117 nm.
- **[Burd23]** — design-principles anchor (class-A dynamics, intracavity BRF + etalon + PZT).
- **[Burk21]** — UHV deep-UV enhancement cavity with hard fluoride coatings.
- **[Brow19]** — surface contamination as dominant LIDT precursor.
- **[Eime87]** — BBO Sellmeier and thermo-optic data for phase-matching computation.
- **[Frie06]** — baseline architecture being departed from.
- **[Guth21]** — in-house operational reference for the fibre-coupling loss (20–25 %) eliminated here.
- **[Kief20] · [Span23] · [Span25]** — in-house in-house VECSEL platform and the [Span25] passive-thermal-management precedent.
- **[Turc22]** — BBO LIDT review.
