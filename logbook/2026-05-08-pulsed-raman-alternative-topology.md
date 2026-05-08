# Alternative next-gen topology — phase-locked femtosecond comb, single-pass tripled to ~ 290–320 nm, far-red-detuned Raman beams

**Steward:** Ulrich Warring
**Date:** 2026-05-08
**Status:** SKETCH (architecture exploration; no build commitment, no `/src/` code)

## Header (Charter §9 trigger questions)

- **Affects Level 0 parameter?** *Conditional.* The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is preserved as the **Doppler-cooling-chain operating point** and is not moved by this sketch. This option proposes a **separate Raman pathway** running at a *different* operating point (Δ ≫ 40 GHz, by ~ tens of nm to the red of resonance) where Γ_sc is *suppressed* relative to the locked reference and Ω_R is supplied by pulsed peak-intensity rather than CW intensity. Under the asymmetric-erosion-protection rule (`docs/principles.md`), tightenings (lower scattering, larger detuning) are permitted; but **promotion** of this sketch to a Phase 4 architecture-comparison candidate requires Council-3 review of the multi-operating-point question (one chain at Δ_ref, another at Δ ≫ Δ_ref).
- **Affects Level 1 parameter?** Yes (informational only). Source-side requirement shifts from CW UV power to *pulsed peak intensity per pulse × repetition rate* with different beam-quality and timing-jitter constraints. The CW chain ([Frie06] baseline; [next-gen workplan](2026-05-08-next-gen-500mW-workplan.md); [IC-VECSEL alternative](2026-05-08-ic-vecsel-alternative-topology.md)) handles Doppler cooling, repumping, photoionisation; the pulsed chain handles only coherent Raman.
- **Affects success criterion?** No, if the sketch is read as a candidate that *meets* the locked reference-triple targets via a different physics regime (lower Γ_sc, larger Δ, comparable Ω_R). Yes, if the Council-3 deliberation chooses to *redefine* the reference triple as multi-operating-point.

This entry is the third in the 2026-05-08 architecture-sketch slate — see also the [next-gen 500 mW workplan](2026-05-08-next-gen-500mW-workplan.md) (Friedenauer-topology parameter optimisation) and the [IC-VECSEL + free-space PDH-locked BBO alternative](2026-05-08-ic-vecsel-alternative-topology.md). The anti-seeding clause (`docs/principles.md` §5.1) is in force throughout: no `/src/architecture/` code follows from this sketch.

---

## 1 · Concept in one sentence

For the **coherent-Raman task only**, deploy a **phase-locked mode-locked Ti:Sapphire frequency-comb oscillator** at ~ 870–960 nm fundamental, single-pass *tripled* (or *quadrupled* with a 1118 nm Yb-fibre oscillator alternative) to land at ~ 290–320 nm — *tens of nanometres red-detuned* from the ²⁵Mg⁺ ³P₃/₂ line — exploiting the comb's enormous **peak intensity** to drive two-photon Raman transitions at suppressed scattering, while leaving the existing CW chain to handle Doppler cooling, repumping, and photoionisation untouched.

This is the architectural pattern pioneered by the Monroe group on Yb⁺ qubits — phase-locked mode-locked Ti:S combs delivering ultrafast Raman kicks — adapted to ²⁵Mg⁺ with the wavelength rescaled and the detuning chosen to suppress spontaneous emission. The **stroboscopic** framing connects to the [Kief20] Floquet-engineering toolbox: a pulsed Raman drive at a frequency commensurate with motional-mode frequencies delivers controllable kicks at the repetition rate (or its sub-/super-harmonics), opening Floquet-style coherent control on the motional state without retuning the CW chain.

## 2 · Topology sketch

```
[ EXISTING CW CHAIN (cooling, repumping, photoionisation) ]   <-- preserved unchanged
   VECSEL @ 1118 nm  ->  LBO  ->  BBO  ->  ~ 280 nm CW
   (Friedenauer-topology baseline OR IC-VECSEL alternative)


[ NEW PULSED RAMAN CHAIN -- separate optical path, separate envelope ]

  ┌──────────────────────────────────────────────────┐
  │  TI:SAPPHIRE MODE-LOCKED OSCILLATOR              │
  │  ~ 870 - 960 nm fundamental                      │
  │  ~ 80 - 100 MHz repetition rate                  │
  │  ~ 100 fs pulse duration                         │
  │  ~ 1 - 2 W average power                         │
  │  Pumped by 532 nm DPSS (Verdi or equivalent)     │
  └─────────────────────────┬────────────────────────┘
                            │
                            ▼
       ┌── Carrier-envelope-offset stabilisation (f0)
       │   AND repetition-rate lock (f_rep)
       │   to a hyperfine / motional reference
       │
                            │
                            ▼
  ┌──────────────────────────────────────────────────┐
  │  SINGLE-PASS THIRD-HARMONIC GENERATION           │
  │                                                  │
  │  Stage 1: SHG in BBO (or LBO) ->  ~ 435 - 480 nm │
  │  Stage 2: SFG with residual fundamental in BBO   │
  │           ->  ~ 290 - 320 nm                      │
  │                                                  │
  │  No buildup cavities -- pulsed peak intensity    │
  │  delivers nonlinear conversion in a single pass  │
  └─────────────────────────┬────────────────────────┘
                            │
                            ▼
       ┌── Beam shaping / AOM gating / polarisation
       │
                            ▼
                  ~ 0.1 - 0.5 W average UV
                  ~ 290 - 320 nm
                  Tens of GW/cm^2 peak intensity
                  ~ tens of nm red-detuned from ^25Mg+ 3P3/2
                            │
                            ▼
                  ~25Mg+ ions in the trap
                  Two-photon Raman transitions
                  Stroboscopic motional-state control
```

The Yb-fibre alternative (1030–1118 nm fundamental, *quadrupled* to ~ 257–280 nm or *tripled* to a longer wavelength via OPO/OPA staging) exists as a fallback that maximally reuses the existing 1118 nm BOM, but the Ti:S route at 870–960 nm → tripled to 290–320 nm is the natural fit for the *tens-of-nm-red-detuned* operating point and matches the Monroe-group precedent most directly.

## 3 · What carries over from the steward direction

- VECSEL stays the seed-laser source class for the **CW chain** (steward direction 2026-05-08; [Burd23] anchor). The pulsed Raman chain is *additional*, not a replacement.
- Spanke2025-class compact rack envelope and Raspberry-Pi controller architecture transfer to the Ti:S envelope: the comb oscillator + tripler + lock electronics fit a 19" rack with the same passive-thermal-management precedent.
- Charter idiom (§9 trigger questions, Coastline / Sail labels, anti-seeding clause, G1 / G2 / G3 boundaries) carries through.

## 4 · What changes vs the existing CW chain and the two preceding sketches

| Element | [Frie06] baseline | [Next-gen workplan](2026-05-08-next-gen-500mW-workplan.md) | [IC-VECSEL alternative](2026-05-08-ic-vecsel-alternative-topology.md) | This sketch (pulsed Raman) |
|---|---|---|---|---|
| Source class | Yb-fibre CW | VECSEL CW | IC-VECSEL CW | **Mode-locked Ti:S comb** |
| Operating point | Δ_ref = 40 GHz | Δ_ref = 40 GHz | Δ_ref = 40 GHz | **Δ ≈ tens of nm to the red (~ 100 THz)** |
| Output regime | CW | CW | CW | **Pulsed (~ 100 fs, ~ 80 MHz)** |
| Doubling-chain pattern | LBO ring + BBO ring (HC) | Same | IC-LBO + BBO (PDH) | **Single-pass SHG + SFG** |
| Buildup cavities | 2 | 2 | 1 | **0** |
| Atomic role | Doppler cooling, repumping, photoionisation, CW Raman | Same | Same | **Coherent Raman only** |
| Replaces existing chain? | — | No | No | **No — runs in parallel** |

## 5 · Coastline claims *(testable design constraints inherited from precedent)*

- **Mode-locked-comb Raman gates are precedented for trapped-ion qubits.** The Monroe group has demonstrated phase-locked mode-locked Ti:S drives for spin–motion entanglement and Raman gates on ¹⁷¹Yb⁺ qubits across multiple papers (see §11 — *extraction follow-up*). The architectural pattern (mode-locked oscillator + carrier-envelope offset stabilisation + pair of repetition-rate-locked pulses or comb-tooth pair separated by the qubit splitting) translates to ²⁵Mg⁺ with the wavelength rescaled.
- **Spontaneous-emission scattering scales as 1/Δ².** Going from Δ_ref = 40 GHz to Δ ≈ 100 THz reduces Γ_sc by ~ (100 THz / 40 GHz)² ≈ 6 × 10⁶ at fixed Rabi frequency. The reference-triple Γ_sc target = 2.0 × 10⁴ s⁻¹ is therefore *exceeded by orders of magnitude* at the new operating point — provided Ω_R can still be reached, which is the binding constraint and the reason pulsed operation is needed.
- **Two-photon Rabi frequency scales as Ω_R ∝ I / Δ.** Going from CW intensity I_CW at Δ_ref to peak intensity I_peak at Δ_far while preserving Ω_R requires I_peak / I_CW ≈ Δ_far / Δ_ref ≈ 2500. This is comfortably accessible with ~ 100 fs pulse duration at ~ 80 MHz rep rate from a Ti:S oscillator (peak intensity is duty-cycle-amplified by ~ 1 / (rep rate × pulse duration) ≈ 1.25 × 10⁵).
- **Single-pass SHG + SFG to ~ 290–320 nm in BBO / LBO is precedented at this peak-intensity scale.** [Eime87] and [Turc22] LIDT envelopes accommodate the pulsed regime with appropriate spot-size design. Buildup cavities are not needed for the comb route — single-pass conversion is sufficient given the peak intensity available.

## 6 · Sail recommendations *(adaptive guidance, contextual to this sketch)*

- **Ti:Sapphire mode-locked oscillator** as the fundamental source — Coherent Mira / Vitara, Spectra-Physics Mai Tai, or fibre-laser equivalents (Yb-fibre at 1030 nm with frequency-doubled output to 515 nm pumping a Ti:S-style stage; or a turnkey Yb-fibre at 1118 nm pulsed for fundamental-wavelength continuity with the in-house BOM, *quadrupled* if a deeper-UV operating point is acceptable).
- **Carrier-envelope-offset (f₀) stabilisation + repetition-rate (f_rep) lock** to a hyperfine reference *or* directly to a motional-mode frequency for stroboscopic operation. Standard f-2f interferometry on a broadened comb plus a phase-detector lock loop closes f₀; f_rep is locked to an RF reference derived from the trap drive or from an independent atomic reference.
- **Single-pass tripler in BBO** (Stage 1 SHG, Stage 2 SFG with residual fundamental) — no buildup cavities. Both stages critically phase-matched; spot-size and crystal-length chosen to avoid LIDT under peak fluence.
- **Stroboscopic operation** — repetition rate (or its sub-/super-harmonic) chosen commensurate with motional-mode frequencies to deliver controllable Raman kicks at the rep rate, connecting to the [Kief20] Floquet-engineering toolbox.
- **AOM gating in the visible** before the final SFG stage to switch the comb on/off without disturbing the lock, preserving phase coherence between gate operations.

## 7 · Tradeoffs vs the other two architecture sketches

**Pros**

- **Spontaneous-emission scattering essentially eliminated.** Γ_sc drops by ~ 10⁶ at the new operating point — the binding fidelity bottleneck of CW Raman is removed *architecturally*.
- **No SHG buildup cavities.** Single-pass tripling means no Hänsch-Couillaud or PDH locks on the doubling chain; the only locks are on the comb itself (f₀, f_rep).
- **Stroboscopic kicks connect to existing in-group toolbox.** [Kief20] Floquet engineering of motional modes via *trapping-potential* modulation translates conceptually to Floquet-style coherent control via *laser-pulse-train* modulation — same physics, different actuator.
- **Decoupled from the CW chain.** The CW Doppler / repumping / photoionisation system runs at the locked Δ_ref = 40 GHz operating point; the pulsed Raman pathway is additive, not replacing.

**Cons / open questions**

- **Adds a separate laser system** — Ti:S oscillator + 532 nm DPSS pump + tripler + lock electronics is non-trivial bench- and procurement-wise. Cost ~ €100k-class for the oscillator + pump alone before the lock and tripler.
- **Reference-triple operating-point question** — the sketch operates at Δ ≫ Δ_ref. Promotion to architecture-comparison candidate requires Council-3 review of the multi-operating-point definition (does the project commit to a single Δ_ref, or does it support a multi-channel definition?).
- **Mode-locked Raman is precedented for Yb⁺, less so for Mg⁺.** The wavelength rescaling is straightforward in principle; the literature for Mg⁺-specific demonstrations is thinner (extraction follow-up — see §11).
- **Pulse-train timing-jitter coupling to motional dephasing.** Repetition-rate noise translates to Raman-pulse-arrival-time noise, which couples to motional-state phase. Lock bandwidth and noise floor need explicit specification — different from CW linewidth budgeting.
- **Optical-comb spectral envelope.** A ~ 100 fs pulse at ~ 870 nm has a transform-limited spectral width of ~ 8 nm = ~ 3 THz — wider than the ²⁵Mg⁺ fine-structure splitting (~ 2.75 THz between D₁ and D₂). Both fine-structure components are addressed simultaneously unless filtered. Whether this is a feature (selectively addressing both ³P₁/₂ and ³P₃/₂ with engineered ratios) or a problem (uncontrolled scattering through D₁) is an open physics question.
- **Phase 4 axis 1 (Raman capability)** — this candidate would score highly here if the operating-point question is resolved, since pulsed Raman is the canonical regime for low-scattering coherent gates. Other axes (axis 6 complexity, axis 4 thermal/nonlinear load) may score worse.

## 8 · Anti-seeding clause / G1-G2-G3 boundaries

- **No `/src/architecture/` code.** All numerics for this alternative live in `/notebooks/exploration/` per CHARTER §5.1. The architecture-neutral primitive set (`shg_cascade.py`, `enhancement_cavity.py`, `boyd_kleinman.py`) does *not* cover pulsed single-pass SHG + SFG; **a new architecture-neutral primitive** (`pulsed_raman_kicks.py` and / or `pulsed_shg_single_pass.py`) is required before any parameter sweep on this candidate is meaningful.
- **G1 (14 GHz unlockable resonance).** Independent of topology choice; this sketch does not advance G1 closure.
- **G2 (UV-induced degradation).** Pulsed peak fluence at the BBO output is comparable to or higher than CW intensity at the existing chain output; G2 closure is *not* sidestepped by going pulsed and may in fact be tightened. This sketch does not close G2.
- **G3 (reference triple).** Locked 2026-05-01; this sketch operates the Raman chain at a *different* point but **does not propose moving the locked reference**. Promotion to candidate slate requires Council-3 review of the multi-operating-point question — separate from G3.
- **Phase 4 architecture comparison.** This candidate joins the slate alongside the [next-gen workplan](2026-05-08-next-gen-500mW-workplan.md) Friedenauer-topology and the [IC-VECSEL + PDH-locked BBO alternative](2026-05-08-ic-vecsel-alternative-topology.md). Slate is opened *after* G1 and G2 close, with Council-3 confirmation of the operating-point question for this entry.

## 9 · Where this sits in the project

- **Not** a replacement for the CW Doppler / repumping / photoionisation chain. The existing CW pathway (current Friedenauer-topology baseline, or either of the two CW alternatives) handles those tasks at Δ_ref = 40 GHz unchanged.
- **Is** an additional channel for the *coherent Raman* task, operating at a separate far-red-detuned point with pulsed peak intensity supplying Ω_R.
- **Is** a candidate that links the project's CW seed-laser direction (Burd23-style VECSEL) to an existing Raman-task literature lineage (Monroe-style ultrafast comb gates) — currently unrepresented in `data/literature/` and flagged as an extraction follow-up.

## 10 · Open follow-ups

- **Extraction follow-ups for Monroe-group ultrafast Raman literature** (proposed citation labels in [Auth4YY] format pending steward sign-off, see §11 below). These are the missing `[P]`-tier anchors for this sketch.
- **`pulsed_raman_kicks.py` architecture-neutral primitive** specification: input parameters (pulse energy, pulse duration, repetition rate, beam waist, detuning, motional frequency, pulse-pair phase), outputs (Ω_R per pulse, accumulated phase per pulse train, residual Γ_sc per gate). Respects the anti-seeding clause — neutral to architecture choice.
- **`pulsed_shg_single_pass.py` architecture-neutral primitive** if not already covered by the existing `shg_single_pass.py` in CW formulation: pulsed-regime extension with peak-intensity-dependent depletion and LIDT bound.
- **Notebook exploration** in `/notebooks/exploration/`: compute the ²⁵Mg⁺ Raman-pulse-train Ω_R / Γ_sc scaling at the Ti:S → tripled operating point; compare to the locked reference triple; identify whether the spectral-envelope simultaneous addressing of D₁ + D₂ is a feature or a constraint.
- **Council-3 deliberation request** if and when promotion to architecture-comparison candidate is desired: the multi-operating-point question deserves an explicit Charter clarification.

## 11 · References

This sketch leans on the cluster of literature already in [`docs/references.html`](../docs/references.html), plus a Monroe-group cluster that is **not yet extracted** and is logged here as an extraction follow-up.

**Currently in the references index.** Citation labels per the index convention.

- **[Burd23]** — design-principles anchor (class-A dynamics; intracavity BRF + etalon + PZT). Carries through unchanged for the CW chain that runs in parallel with this pulsed Raman path.
- **[Burd16]** — wavelength-adjacent ²⁵Mg⁺ VECSEL companion; preserved as the CW source class.
- **[Frie06]** — CW baseline; preserved as the CW chain's reference architecture.
- **[Eime87]** · **[Turc22]** — BBO Sellmeier and LIDT envelopes for the single-pass tripler design.
- **[Kief20]** — Floquet engineering with ²⁵Mg⁺ motional modes via trapping-potential modulation; conceptual cousin of the stroboscopic pulse-train Raman drive proposed here.
- **[Hemm11]** — multi-purpose laser-system architectural prior; relevant because this sketch *adds* a Raman-task laser without consolidating into the multi-purpose CW chain.

**Extraction follow-up — Monroe-group ultrafast Raman literature** (proposed labels; not yet committed to `data/literature/`).

- **`[Haye10]`** — D. Hayes et al., *Phys. Rev. Lett.* **104**, 140501 (2010), "Entanglement of Atomic Qubits Using an Optical Frequency Comb" — seminal demonstration of comb-driven two-photon Raman transitions on ¹⁷¹Yb⁺.
- **`[Camp10]`** — W. C. Campbell et al., *Phys. Rev. Lett.* **105**, 090502 (2010), "Ultrafast Gates for Single Atomic Qubits" — single-pulse-pair gate operations.
- **`[Mizr13]`** — J. Mizrahi et al., *Phys. Rev. Lett.* **110**, 203001 (2013), "Ultrafast Spin-Motion Entanglement and Interferometry with a Single Atom" — most directly relevant to stroboscopic motional-state control.
- **`[Inle14]`** — I. V. Inlek et al., *Phys. Rev. A* **90**, 042316 (2014), "Quantum Gates with Phase Stabilization over Communication Links" — phase stability and lock architecture for comb Raman.

(Final selection and labels will be confirmed once the relevant papers are downloaded and extracted under `data/literature/<key>/`.)
