---
layout: default
title: Pulsed-Raman alternative — phase-locked Ti:Sapphire comb, single-pass tripled to ~ 290–320 nm, far-red-detuned
description: Architecture sketch — a phase-locked mode-locked Ti:Sapphire frequency comb, single-pass tripled to ~ 290–320 nm and operated tens of nm red-detuned from the 25Mg+ 3P3/2 line, supplying coherent Raman beams via pulsed peak intensity. Pairs with the IC-VECSEL alternative under a two-architecture task split.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page is an architecture sketch, not a build commitment. Phase 4 architecture scoring is gated by G1 / G2; promotion of this candidate additionally requires Council-3 review of the multi-operating-point question (Δ ≫ Δ_ref).</p>

<p class="eyebrow">Architecture · sketch</p>

# Pulsed-Raman alternative — phase-locked Ti:Sapphire comb, single-pass tripled

**Status:** SKETCH (logbook entry [`logbook/2026-05-08-pulsed-raman-alternative-topology.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-pulsed-raman-alternative-topology.md) carries the full Charter §9 trigger questions, Coastline / Sail labels, and G1-G2-G3 boundary statements; this page is the public surface).

**Charter compliance — load-bearing scope conflict.** [`CHARTER.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) §3 line 105 explicitly lists *"Pulsed UV systems (the stroboscopic / fs-comb discussion with Leibfried is a distinct project)"* as **out of scope** for `mg-plus-uv-chain`. This sketch sits across that Charter line and **cannot be promoted to a Phase 4 architecture-comparison candidate without one of:** (i) a Council-3 Charter exception that rewrites §3, or (ii) explicit re-classification as a **parallel Raman sub-project** that links to `mg-plus-uv-chain` via shared ²⁵Mg⁺ infrastructure but lives outside this repository's Charter scope. Until one of those is resolved, the sketch is logged as a forward-looking artefact only — not as a Phase 4 input.

**Reference triple — conditional.** The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is *preserved* as the **CW-chain operating point**. This option proposes a *separate* Raman pathway at a *different* operating point — Δ ≫ Δ_ref, by ~ tens of nm to the red of resonance — where Γ_sc is suppressed by ~ 10⁶ relative to the locked reference and Ω_R is supplied by pulsed peak intensity rather than CW intensity. Under the asymmetric-erosion-protection rule, *tightenings* (lower scattering, larger detuning) are permitted; **promotion** to a Phase 4 candidate requires both the CHARTER §3 scope question above *and* Council-3 review of the multi-operating-point question to be resolved. Anti-seeding clause is in force — no `/src/architecture/` code follows.

---

## Concept

For the **coherent-Raman task only**, deploy a **phase-locked mode-locked Ti:Sapphire frequency-comb oscillator** at ~ 870–960 nm fundamental, single-pass *tripled* to ~ 290–320 nm — *tens of nanometres red-detuned* from the ²⁵Mg⁺ ³P₃/₂ line. The comb's enormous peak intensity drives two-photon Raman transitions at heavily suppressed scattering, while the existing CW chain (in either of the [Friedenauer-topology next-gen](next-gen.html) form or the [IC-VECSEL alternative](ic-vecsel-alternative.html) form) handles Doppler cooling, repumping, and photoionisation at the locked Δ_ref = 40 GHz operating point unchanged.

This is the architectural pattern pioneered by the Monroe group on Yb⁺ qubits — phase-locked mode-locked Ti:S combs delivering ultrafast Raman kicks — adapted to ²⁵Mg⁺ with the wavelength rescaled and the detuning chosen to suppress spontaneous emission.

## Stroboscopic linkage to existing in-group toolbox

The Ti:S repetition rate (or its sub-/super-harmonic) chosen commensurate with motional-mode frequencies delivers controllable Raman kicks at the rep rate — Floquet engineering of motional modes via *laser-pulse-train* modulation. This is the conceptual cousin of [[Kief20]](../references.html#kief20)'s Floquet engineering via *trapping-potential* modulation: same physics, different actuator.

## The physics that makes it work

- **Spontaneous-emission scattering scales as 1/Δ².** Going from Δ_ref = 40 GHz to Δ ≈ 100 THz reduces Γ_sc by ~ (100 THz / 40 GHz)² ≈ 6 × 10⁶ at fixed Rabi frequency. The reference-triple Γ_sc target = 2.0 × 10⁴ s⁻¹ is therefore *exceeded by orders of magnitude* at the new operating point — provided Ω_R can still be reached.
- **Two-photon Rabi frequency scales as Ω_R ∝ I/Δ.** Preserving Ω_R while moving from Δ_ref to Δ_far requires peak intensity ~ 2500× higher than CW. Ti:S oscillator at ~ 80 MHz × ~ 100 fs delivers exactly this duty-cycle amplification (~ 10⁵).
- **Single-pass SHG + SFG to ~ 290–320 nm in BBO is precedented at this peak-intensity scale.** [[Eime87]](../references.html#eime87) and [[Turc22]](../references.html#turc22) LIDT envelopes accommodate the pulsed regime with appropriate spot-size design. Buildup cavities are not needed — single-pass conversion is sufficient.

## Topology

```
[ EXISTING CW CHAIN — preserved unchanged ]
   VECSEL @ 1118 nm  ->  LBO  ->  BBO  ->  ~ 280 nm CW
   (Friedenauer-topology next-gen OR IC-VECSEL alternative)
   Handles cooling + repumping + photoionisation at Δ_ref = 40 GHz.


[ NEW PULSED RAMAN CHAIN — separate optical path, separate envelope ]

  ┌──────────────────────────────────────────────────┐
  │  TI:SAPPHIRE MODE-LOCKED OSCILLATOR              │
  │  ~ 870 - 960 nm fundamental                      │
  │  ~ 80 - 100 MHz repetition rate                  │
  │  ~ 100 fs pulse duration                         │
  │  ~ 1 - 2 W average power                         │
  │  Pumped by 532 nm DPSS                           │
  └─────────────────────────┬────────────────────────┘
                            │
                            ▼  Carrier-envelope-offset (f0)
                            ▼  + repetition-rate (f_rep) lock
                            │
  ┌─────────────────────────┴────────────────────────┐
  │  SINGLE-PASS THIRD-HARMONIC GENERATION           │
  │  Stage 1: SHG in BBO (or LBO) -> 435 - 480 nm    │
  │  Stage 2: SFG with residual fundamental in BBO   │
  │           -> ~ 290 - 320 nm                       │
  │  No buildup cavities                             │
  └─────────────────────────┬────────────────────────┘
                            │
                            ▼  Beam shaping / AOM gating
                            │
                  ~ 0.1 - 0.5 W average UV
                  ~ 290 - 320 nm
                  Tens of GW/cm² peak intensity
                  ~ tens of nm red-detuned from 25Mg+ 3P3/2
                            │
                            ▼
                       ²⁵Mg⁺ ions
                       Two-photon Raman transitions
                       Stroboscopic motional-state control
```

The Yb-fibre alternative (1030–1118 nm fundamental, *quadrupled* to ~ 257–280 nm) exists as a fallback that maximally reuses the existing 1118 nm BOM, but the Ti:S route at 870–960 nm → tripled to 290–320 nm is the natural fit for the *tens-of-nm-red-detuned* operating point and matches the Monroe-group precedent most directly.

## Ti:S operating point — nominal + sensitivity envelope (P2 from 2026-05-08 review)

The earlier framing left the Ti:S parameters as ranges (~ 870–960 nm fundamental, ~ 80–100 MHz rep rate, ~ 100 fs pulse, ~ 1–2 W average). Ranges this wide are not falsifiable — they cannot be plugged into a peak-intensity / conversion-efficiency calculation. Tightened operating point:

| Parameter | Nominal | Lower | Upper | Notes |
|---|---|---|---|---|
| λ_fund | 920 nm | 870 nm | 960 nm | Tripled to ~ 307 nm at nominal (~ 27 nm red-detuned from ²⁵Mg⁺ ³P₃/₂); tripled to ~ 290 / 320 nm at the bounds (~ 10 / 40 nm red-detuned) |
| f_rep | 80 MHz | 80 MHz | 100 MHz | Sets the duty-cycle amplification |
| τ_pulse | 100 fs | 50 fs | 150 fs | Transform-limited; sets peak intensity at fixed pulse energy |
| P_avg | 1.5 W | 1.0 W | 2.0 W | Average IR power before tripler |

**Derived quantities at nominal** (λ = 920 nm, f_rep = 80 MHz, τ = 100 fs, P_avg = 1.5 W):

- Pulse energy `E_pulse = P_avg / f_rep ≈ 19 nJ`.
- Peak intensity at w₀ = 20 µm focus: `I_peak ≈ E_pulse / (τ_pulse · π w₀²) ≈ 60 GW/cm²`.
- Single-pass third-harmonic efficiency at 920 nm → 307 nm in BBO: bounded by `pulsed_shg_single_pass.py` primitive (open follow-up); plausible η_SHG ≈ 30 %, η_SFG ≈ 20 % give average UV ≈ 90 mW.

**Detuning constraint.** *"Tens of nanometres red-detuned"* tightens to: **Δλ ≥ 20 nm** (≈ 70 THz from the ³P₃/₂ line) is the minimum acceptable red shift; the preferred target is **Δλ ≈ 30 nm** (≈ 100 THz). At the lower bound λ_fund = 870 nm, the tripled output sits at ≈ 290 nm = ~ 10 nm red-detuned, which is *insufficient* under this rule and forces λ_fund ≥ 880 nm (tripled ≥ 293 nm).

**Single-pass tripling efficiency floor.** The current "0.1–0.5 W average UV" is an assertion, not a derived bound. Defining the **minimum acceptable UV average power** to drive the Raman Ω_R per gate at the chosen detuning and waist is `REQ-PR-008`. If the single-pass route falls short of that minimum, fallback options activate: Yb-fibre quadrupled at 1030 nm (lands at 257 nm = blue-detuned, wrong sign for this option's premise), or OPA-assisted tripling at lower peak intensity. Both fallbacks add complexity and need their own architecture sketches.

## What it changes vs the existing CW chain

| Element | [Friedenauer 2006](friedenauer-2006.html) | [Next-gen workplan](next-gen.html) | [IC-VECSEL alternative](ic-vecsel-alternative.html) | This sketch |
|---|---|---|---|---|
| Source class | Yb-fibre CW | VECSEL CW | IC-VECSEL CW | **Mode-locked Ti:S comb** |
| Operating point | Δ_ref = 40 GHz | Δ_ref = 40 GHz | Δ_ref = 40 GHz | **Δ ≈ tens of nm red (~ 100 THz)** |
| Output regime | CW | CW | CW | **Pulsed (~ 100 fs, ~ 80 MHz)** |
| Doubling-chain pattern | LBO ring + BBO ring (HC) | Same | IC-LBO + BBO (PDH) | **Single-pass SHG + SFG** |
| Buildup cavities | 2 | 2 | 1 | **0** |
| Atomic role | All UV tasks | All UV tasks | Cooling + repumping only | **Coherent Raman only** |
| Replaces existing chain? | — | No | Cooling + repumping pathway | **No — runs in parallel** |

## Status

| Item | State |
|---|---|
| Architecture sketch logged | ✅ done — [logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-pulsed-raman-alternative-topology.md) |
| Monroe-group ultrafast-Raman literature extraction | ⏳ open follow-up — proposed labels `[Haye10]` `[Camp10]` `[Mizr13]` `[Inle14]` |
| `pulsed_raman_kicks.py` architecture-neutral primitive in `/src/` | ⏳ open follow-up |
| `pulsed_shg_single_pass.py` (or pulsed-regime extension of existing primitive) | ⏳ open follow-up |
| Notebook exploration of Ti:S → tripled at the red-detuned operating point | ⏳ open follow-up |
| **Multi-level ²⁵Mg⁺ pulse-train model — Phase 4 acceptance prerequisite** | ⏳ open — scaling-argument prose (1/Δ², duty-cycle) is *not* sufficient. Acceptance requires a multi-level ²⁵Mg⁺ model with both ³P₁/₂ and ³P₃/₂ addressed simultaneously by the ~ 3 THz comb spectral envelope, validated against a Monroe-group Yb⁺ benchmark before being applied to ²⁵Mg⁺. |
| Council-3 deliberations | ⏳ requested if and when promotion to Phase 4 candidate is desired: (i) CHARTER §3 scope question, (ii) multi-operating-point question |
| Phase 4 candidate-slate opening | ⏳ gated by G1 + G2 closure + the two Council-3 deliberations above |

## G2-failure impact (P1 from 2026-05-08 review)

Pulsed peak fluence at the BBO output is comparable to or higher than the CW intensity at the next-gen chain output; G2 (UV-induced degradation) is *not* sidestepped by going pulsed and may in fact be tightened. Impact bounds if G2 closes worse than hoped:

| If G2 closes at … | Impact on the pulsed-Raman alternative | Mitigation already in design | Fallback |
|---|---|---|---|
| ≤ 5 %/100 h UV-output drop | Marginal — UV stays within Raman-Ω_R envelope for ~ 1000 h; maintenance interval comparable to next-gen | Tight focus + clean optics; rack-internal cleanliness | None needed |
| 10–20 %/100 h | Tight — pulsed peak fluence likely accelerates surface contamination; need larger spot size or lower rep rate | Larger BBO waist (relaxes peak fluence at fixed Ω_R); lower repetition rate (lowers average power) | Move to OPA-assisted tripling at lower peak intensity |
| > 20 %/100 h | Architecture failure-mode envelope exceeded; pulsed peak fluence is the dominant accelerator | Replacement of single-pass BBO tripler with cavity-enhanced visible + single-pass UV, or full alternative architecture | Architecture withdrawn |

(Note: the entire G2-failure-impact analysis here is contingent on the CHARTER §3 scope question being resolved per the [Council-3 trigger](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-09-council-3-trigger-task-split-success-criterion.md). Until that trigger disposes, the analysis is forward-looking only.)

## Boundaries (what this page is **not**)

- **Not Phase 4 architecture scoring.** Gated by G1 + G2 + Council-3 sign-off on the multi-operating-point question.
- **Not architecture-family-specific code in `/src/`.** All numerical work for this candidate lives in `/notebooks/exploration/` per CHARTER §5.1, and depends on architecture-neutral primitives that have *not yet been written* (`pulsed_raman_kicks.py`).
- **Not a build commitment.** The sketch is exploration only.
- **Not a replacement for the CW chain.** Doppler cooling, repumping, and photoionisation continue on the CW pathway at the locked Δ_ref operating point.
- **Not a closure of G2.** Pulsed peak fluence at the BBO output is comparable to or higher than CW intensity; G2 (UV-induced degradation) closure may in fact be *tightened* by going pulsed.

## See also

- [IC-VECSEL alternative](ic-vecsel-alternative.html) — the parallel CW pathway that handles cooling + repumping under the two-architecture task split.
- [Next-gen 500 mW workplan](next-gen.html) — the Friedenauer-topology single-architecture pre-G2 deliverable; remains the load-bearing parameter-optimisation effort.
- [Friedenauer 2006 baseline](friedenauer-2006.html) — the published all-solid-state CW reference.
- [Components → Seed lasers (VECSEL)](../components/seed-lasers.html) — the CW seed-laser source-class steward direction.
- [References](../references.html) — alphabetical literature index (Monroe-group ultrafast-Raman extractions are a flagged follow-up).
- [Logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-pulsed-raman-alternative-topology.md) — full Charter §9 / Coastline / Sail / G1-G2-G3 statements.
