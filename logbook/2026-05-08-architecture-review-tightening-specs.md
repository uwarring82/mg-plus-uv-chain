# Review: Three next-generation architectures — comments and spec-tightening recommendations

**Steward:** Ulrich Warring  
**Reviewer:** (assistant agent review)  
**Date:** 2026-05-08  
**Scope:** `docs/architectures/next-gen.md`, `docs/architectures/ic-vecsel-alternative.md`, `docs/architectures/pulsed-raman-alternative.md`, plus their logbook back surfaces.

---

## Executive summary

All three architecture documents are well-framed against the CHARTER §1.5 constraint hierarchy and correctly respect the anti-seeding clause, G1/G2/G3 boundaries, and Coastline / Sail labelling.  
**However, they remain sketches — most quantitative targets are stated as ranges or order-of-magnitude estimates rather than as bounds with confidence intervals.  For Phase 4 scoring to be falsifiable, every parameter that feeds into the six fixed axes must carry an explicit (lower, nominal, upper) triple, a sensitivity derivative, and a traceability link to Level 0 / Level 1.**

This review groups findings by architecture and then by cross-cutting theme.

---

## 1 · Next-generation 500 mW workplan (`docs/architectures/next-gen.md`)

### 1.1 What is strong
- Correctly treats the 500 mW figure as *indicative*, not load-bearing; binding form is the Level-0 reference triple.
- Anti-seeding boundary is explicit: all work stays in `/notebooks/`, no `/src/architecture/` code.
- Phase E cross-check (BBO 1.5 % residual) is the right validation anchor.
- NG-A through NG-G phase plan is logically ordered and effort estimates are realistic (~7 focused days).

### 1.2 Review comments and tightening recommendations

#### R1.1 — Pump-power forward map (NG-B) needs a *hard upper bound*, not just a grid
> Current text: *"Plot of required input pump (1118 nm) vs UV target output, for a grid of cascade efficiencies η_cascade ∈ [0.10, 0.30]".*

**Tighten:** The thermal-load envelope in `constraints/loss-budget.md` §3.1 already caps max pump at ≤ 10 W (fundamental).  The NG-B deliverable should state:
- **Absolute ceiling:** P_pump ≤ 10 W at 1118 nm.  If the forward map crosses 10 W before reaching 500 mW UV, the architecture is thermally non-viable under the locked thermal envelope.
- **Derating curve:** P_pump vs. η_cascade with the 10 W line drawn as a **kill contour**.  Phase 4 axis 4 (thermal / nonlinear load) can then read this directly.
- **ASE budget assumption:** Friedenauer’s 1.2 W ASE becomes relevant if the pump source stays Yb-fibre.  The VECSEL steward direction (2026-05-08) removes ASE, but the forward map should state which seed class it assumes.  **Recommendation:** run NG-B twice — once with Yb-fibre ASE load (Friedenauer-class), once with VECSEL (ASE ≈ 0), and document the delta.

#### R1.2 — IC reflectivity sweep (NG-C) must include *manufacturing tolerance* and *degradation drift*
> Current text: *"sensitivity bracket: T_IC ± 0.5 pp, L_passive ± 0.5 pp, γ_SHG ± 20 %".*

**Tighten:**
- The ±0.5 pp bracket is a *simulation* sweep width, not a *coating-run* tolerance.  NG-E must convert this into vendor-specific numbers: if IBS coating repeatability is ±2 pp (typical for Tamosauskas2018-class runs), the sensitivity envelope widens significantly.
- **Add a time-dependent term:** R_in degrades under UV exposure (CHARTER §8.6).  The sensitivity envelope should include a *drift* scenario: R_in(t=0) matched, R_in(t=100 h) shifted by ΔR from coating degradation.  This couples NG-C directly to G2.
- **Acceptance criterion:** The table should identify the *smallest* pump that hits 500 mW UV *at the upper bound* of the tolerance envelope, not at nominal.  This prevents an optimistic nominal point from masking a Conservative-scenario failure.

#### R1.3 — Crystal-geometry sweep (NG-D) must bound *temperature-drift sensitivity*
> Current text: *"checking sensitivity to crystal-temperature drift"* (one line, no numbers).

**Tighten:**
- Friedenauer 2006 reports a 2 K ambient swing → ~10 % oscillation (5 % with thermal isolation).  The next-gen geometry sweep should define:
  - **Max acceptable oven-temperature drift:** ΔT_oven ≤ X K such that UV output stays within Y % of target.
  - **Thermal-lensing figure of merit:** dn/dT and thermal-expansion contributions to effective focal length at the new pump scale; this is an input to the ABCD stability budget.
- **BBO walk-off-aware BK optimum** is mentioned but not quantified.  The sweep should report the *walk-off penalty factor* h_m(β>0) / h_m(β=0) at each length, so Phase 4 axis 4 can score it.

#### R1.4 — Loss-budget anchoring (NG-E) must produce a *binding item* statement
> Current text: *"A defensible upper bound on cascade efficiency given realistic coatings; a notation of which loss-budget item is binding at 500 mW UV."*

**Tighten:**
- The deliverable should be a **ranked list** of loss contributions at the recommendation point, with the largest contributor flagged as the *binding constraint*.  Example format:
  ```
  L_passive_total = L_mirror_HR + L_mirror_OC + L_crystal_abs + L_scatter
  Binding item at 500 mW UV: L_mirror_OC (43 % of total loss)
  ```
- If no single item is binding (i.e., all are comparable), state that explicitly — it means the architecture is *robust* against any one vendor failure but leaves less headroom for overall improvement.

#### R1.5 — Synthesis (NG-F) must state *confidence intervals*, not single-point numbers
> Current text: *"Pump power required at 1118 nm (with 80 % confidence interval)."*

**Tighten:**
- Define what "80 % confidence" means: is it the envelope over all NG-C/D/E tolerance combinations (Monte-Carlo-style), or the worst-case among the ±brackets (corner-case)?  **Recommendation:** report both:
  - **Statistical 80 % CI:** from Monte-Carlo over normally distributed parameter uncertainties.
  - **Corner-case bound:** from simultaneous worst-case parameter drift (conservative for procurement).
- The *open-items list* must explicitly flag which `data/literature/` entries are binding.  Example: *"BBO d_eff from Eckardt 1990 is binding for γ_SHG; if a new measurement shifts this by > 5 %, NG-F re-runs."*

#### R1.6 — Missing: explicit G1-inheritance statement
The next-gen workplan re-uses Friedenauer cavity geometry (LBO ring + BBO ring).  The 14-GHz unlockable domain (CHARTER §8.1) is therefore **inherited unchanged** unless the geometry changes.  Add a paragraph:
> *"G1 risk inheritance: because this workplan holds the two-stage SHG topology fixed, the 14-GHz anomaly is carried forward from Friedenauer 2006 §4.  NG-D may test whether alternative crystal lengths or temperatures shift the anomaly, but G1 closure remains a Phase 2 discriminant-scan task, not a simulation task."*

---

## 2 · IC-VECSEL alternative (`docs/architectures/ic-vecsel-alternative.md`)

### 2.1 What is strong
- Task-scope split (cooling + repumping only, Raman → pulsed chain) is a clear decomposition of the CHARTER §1.5 indicative anchor.
- Sealed-envelope atmosphere control is architecturally coherent with G2 mitigation.
- PDH choice for BBO stage is well-motivated by Burd23 precedent.

### 2.2 Review comments and tightening recommendations

#### R2.1 — The ~500 mW @ 559 nm visible target is the *critical unverified assumption*; it needs a failure-mode boundary
> Current text: *"[Burd16] reported ~30–80 mW direct visible … extending this to ~500 mW is a ~5–10× scaling step."*

**Tighten:**
- The 500 mW visible target is not a free parameter — it is **derived** from the UV target and the BBO visible-to-UV efficiency.  The document should state the exact derivation with bounds:
  ```
  P_visible_min = P_UV_target / η_BBO_max
  P_visible_max = P_UV_target / η_BBO_min
  ```
  At η_BBO ∈ [7 %, 30 %] (from Frie06 / Guth21 lower bound to Burk21-style hard-fluoride upper bound), this gives:
  - P_visible ∈ [167 mW, 714 mW] for P_UV = 50 mW.
- **Add a decision boundary:** If the IC-VECSEL cannot deliver > 250 mW visible (the upper end of Burd16 precedent), the architecture fails *even at the optimistic BBO efficiency*.  If it cannot deliver > 170 mW, it fails at the conservative efficiency.  These are **go / no-go numbers** for the sketch.
- The `shg_intracavity.py` primitive (§10 open follow-up) should compute this explicitly: given intracavity IR power P_circ, LBO nonlinearity, and cavity parameters, what is the extracted visible power?  Until this primitive exists, the ~500 mW figure is **unfalsifiable**.

#### R2.2 — Thermal isolation between LBO oven and gain-mirror needs a *quantified spec*
> Current text: *"the LBO oven (~150 °C, NCPM Type-I) and the gain-mirror Peltier (~20 °C) need careful thermal isolation."*

**Tighten:**
- Specify the **thermal resistance budget:** R_th_oven→mirror ≤ X K/W such that mirror temperature drift < Y K under Z W of oven dissipation.
- Reference: Burd23 §2 does not address an intracavity crystal oven (Burd23 uses external PPKTP).  The thermal-load envelope from `constraints/loss-budget.md` §3.1 (max crystal ΔT ≤ 15 K) applies to the BBO stage, but the *intracavity* LBO oven is a new thermal boundary not covered by the existing constraint file.
- **Add a Level-1 thermal spec:** ΔT_gain_mirror ≤ 2 K under full oven load, to preserve the < 100 kHz linewidth budget (dn/dT of the semiconductor cavity).

#### R2.3 — PDH locking needs a *bandwidth and residual-noise spec*
> Current text: *"PDH lock — error signal from cavity reflection, demodulated against EOM drive frequency."*

**Tighten:**
- The document should state the **loop-bandwidth target** relative to the BBO cavity linewidth and the expected mechanical-noise spectrum.  Friedenauer’s HC lock bandwidth was ~18 kHz (loaded piezo).  PDH should match or exceed this.
- Specify **residual phase noise** at the error point: S_φ,res(f) ≤ ? dBc/Hz in the 100 Hz–10 kHz band (where acoustic noise dominates).  This is an input to Phase 4 axis 2.
- The EOM spec (10–50 MHz) is a range, not a choice.  Tighten to a **single modulation frequency** with justification: e.g. 30 MHz, chosen to be ≫ cavity linewidth (~1 MHz) and ≪ photodiode / cable bandwidth limit (~100 MHz).

#### R2.4 — Sealed-envelope atmosphere spec needs *pressure / purity / flow-rate* numbers
> Current text: *"Vacuum or N2 / Ar purge"* and *"Rough vacuum (1–10 mbar) preferred"* (in logbook).

**Tighten:**
- Define **three atmosphere classes** with explicit specs:
  | Class | Pressure | Gas purity | O₂ / H₂O content | Rationale |
  |---|---|---|---|---|
  | A — UHV | < 10⁻⁶ mbar | — | < 1 ppm | Matches Burk21 hard-fluoride longevity |
  | B — Inert purge | 1 atm | 99.999 % N₂ | < 1 ppm H₂O, < 10 ppm O₂ | Simple plumbing, continuous flow |
  | C — Rough vacuum | 1–10 mbar | — | Outgassing-limited | Middle ground; requires pump |
- The document should state which class is the **design target** and which are **fallbacks**.  G2 closure (UV degradation) depends on this choice; the sealed envelope is a *candidate* mitigation, but without a specified atmosphere class it cannot be scored on Phase 4 axis 3.

#### R2.5 — Task-allocation interface with pulsed-Raman alternative needs *timing / switching* specs
The IC-VECSEL delivers cooling + repumping; the pulsed chain delivers Raman.  But cooling and Raman are often interleaved in an experimental sequence.  The documents do not state whether the two chains are **simultaneously on** or **switched**.

**Tighten:**
- Add an **operational-mode table**:
  | Mode | CW chain state | Pulsed chain state | Duration | Transition time |
  |---|---|---|---|---|
  | Doppler cooling | ON (50 mW UV) | OFF / standby | 1–10 ms | < 1 μs (AOM) |
  | Raman gate | OFF / idle | ON (pulsed) | 0.5–5 μs | < 1 μs (AOM) |
  | Detection | ON (50 mW UV) | OFF | 100 μs–1 ms | < 1 μs |
- If both chains can be simultaneously on, specify **cross-talk budget:** scattered 280 nm CW light into the pulsed path must not saturate the comb detector; scattered comb light into the CW path must not degrade the BBO cavity lock.

---

## 3 · Pulsed-Raman alternative (`docs/architectures/pulsed-raman-alternative.md`)

### 3.1 What is strong
- The physics case (1/Δ² suppression of Γ_sc, duty-cycle amplification of Ω_R) is clearly stated and quantified.
- Explicitly flags the multi-operating-point question as a Council-3 issue.
- Correctly notes that G2 is not sidestepped and may be tightened by pulsed peak fluence.

### 3.2 Review comments and tightening recommendations

#### R3.1 — Ti:S parameters are under-specified; need a **single nominal point** with bounds
> Current text: *"~870–960 nm fundamental; ~80–100 MHz repetition rate; ~100 fs pulse duration; ~1–2 W average power."*

**Tighten:**
- These ranges are too wide to compute anything falsifiable.  Define a **nominal operating point** and a **sensitivity envelope**:
  | Parameter | Nominal | Lower bound | Upper bound |
  |---|---|---|---|
  | λ_fund | 920 nm | 870 nm | 960 nm |
  | f_rep | 80 MHz | 80 MHz | 100 MHz |
  | τ_pulse | 100 fs | 50 fs | 150 fs |
  | P_avg | 1.5 W | 1.0 W | 2.0 W |
- Then compute the **derived quantities** at nominal:
  - E_pulse = P_avg / f_rep ≈ 19 nJ
  - I_peak (focused to w₀ = 20 μm) ≈ E_pulse / (τ_pulse · π w₀²) ≈ 60 GW/cm²
  - Third-harmonic conversion efficiency (single-pass) — needs `pulsed_shg_single_pass.py` primitive
- The **wavelength range 870–960 nm** maps to third-harmonic 290–320 nm.  But the ²⁵Mg⁺ ³P₃/₂ line is at ~279.6 nm; 320 nm is ~40 nm red-detuned, 290 nm is ~10 nm red-detuned.  The document says *"tens of nanometres red-detuned"* — tighten to **Δλ ≥ 20 nm** (≈ 70 THz detuning) as the minimum acceptable red shift, with a preferred target of Δλ ≈ 30 nm (≈ 100 THz).

#### R3.2 — The spectral-envelope / D₁+D₂ simultaneous-addressing question needs a *decision boundary*
> Current text: *"A ~100 fs pulse at ~870 nm has a transform-limited spectral width of ~8 nm = ~3 THz — wider than the ²⁵Mg⁺ fine-structure splitting (~2.75 THz)."*

**Tighten:**
- This is flagged as an *open physics question*.  It is actually a **specification question** with two possible answers:
  1. **Feature:** Both ³P₁/₂ and ³P₃/₂ paths contribute constructively to the Raman transition.  Requires explicit two-path interference calculation; the effective dipole moment changes.
  2. **Constraint:** D₁ scattering is unwanted; spectral filtering before the ion is required.  Adds loss and complexity.
- The document should state a **decision rule:** If the two-path calculation (Phase 3 simulation) shows constructive interference with < 2× increase in Γ_sc, treat as feature; otherwise, require spectral pre-filtering to < 1 THz bandwidth and document the loss.
- Add to open follow-ups: *"Multi-level Raman prefactor at Δ ≈ 100 THz including both ³P₁/₂ and ³P₃/₂ paths — compute whether the far-detuned limit simplifies to a single effective dipole or retains two-path structure."*

#### R3.3 — Timing-jitter spec is missing; it is the pulsed equivalent of linewidth
> Current text mentions *"repetition-rate noise translates to Raman-pulse-arrival-time noise"* but gives no numbers.

**Tighten:**
- Define the **timing-jitter budget** analogous to the CW phase-noise budget:
  - For a π-pulse gate with τ_gate = 0.5 μs and two pulses separated by T_rep = 12.5 ns (80 MHz), the relative pulse-to-pulse timing jitter δt must satisfy δt / T_rep < 10⁻³ for < 10⁻⁴ infidelity (draft; needs verification).
  - This translates to **repetition-rate phase noise:** S_φ,rep(f) in the 1 kHz–1 MHz band.
- Specify the **lock architecture:** f-2f + f_rep locked to a GPS-disciplined Rb clock?  To a trap RF drive?  The choice affects the timing-jitter spec by orders of magnitude.

#### R3.4 — Single-pass tripling efficiency must be bounded
> Current text: *"~0.1–0.5 W average UV"* (after tripling).

**Tighten:**
- The 0.1–0.5 W range is an assertion, not a derived bound.  With P_avg = 1.5 W at 920 nm and plausible single-pass SHG+SFG efficiencies (η_SHG ≈ 30 %, η_SFG ≈ 20 % for femtosecond pulses), the UV output is ~90 mW.  The document should:
  - State the **efficiency assumptions** explicitly.
  - Define the **minimum acceptable UV average power** to reach the Raman Ω_R target at the chosen detuning and focus.  This is the go / no-go number.
  - If the minimum is > 0.5 W, the Ti:S + single-pass route is **non-viable** and the fallback (Yb-fibre quadrupled, or OPA-assisted tripling) must be activated.

#### R3.5 — Multi-operating-point governance needs a *precedent check*
> Current text: *"Promotion of this sketch to a Phase 4 architecture-comparison candidate requires Council-3 review of the multi-operating-point question."*

**Tighten:**
- The CHARTER §3 non-goals originally said: *"Pulsed UV systems (the stroboscopic / fs-comb discussion with Leibfried is a distinct project)"*.  This was a v1.0 exclusion.  The present sketch re-opens that door.
- Add a **governance clause:** Before Council-3 deliberation, the Steward should:
  1. Confirm in writing that the v1.0 non-goal on pulsed systems is *superseded* by this sketch, or that the sketch is a *separate project* branching from the Charter.
  2. Verify that the reference-triple anchoring rule (CHARTER §5.2) allows scoring at Δ_ref for the CW chain and at Δ_far for the pulsed chain as *two separate axis-1 scores* that are not directly compared.
  3. Document whether the "single-source-derived beam pair preferred" clause (CHARTER §3 Preserved) applies per-task (CW chain supplies its own beam pair; pulsed chain supplies its own) or per-system (the project as a whole must preserve common-mode rejection for each task).

---

## 4 · Cross-cutting themes (all three architectures)

### 4.1 Traceability matrix: Architecture parameters → Level 0 / Level 1

Every parameter in all three sketches should be traceable.  The following table is **missing** from all three documents and should be added as a common appendix:

| Parameter | Architecture | Level 0 / 1 parent | If this drifts, what breaks? |
|---|---|---|---|
| P_UV = 500 mW (nominal) | Next-gen | Level 1: UV power after loss budget | Raman Ω_R if overhead consumed |
| P_UV = 50 mW (cooling+repump) | IC-VECSEL | Level 1: same, but task-split | Detection SNR, cooling rate |
| Δ_ref = 40 GHz | All CW | Level 0: locked at G3 | Γ_sc, AC Stark shift |
| Δ ≈ 100 THz | Pulsed Raman | Level 0: tightened detuning | Ω_R (must be recovered by peak intensity) |
| Ω_R / 2π = 400 kHz | All | Level 0: locked at G3 | Gate speed, scattering / gate |
| Γ_sc = 2.0×10⁴ s⁻¹ | All CW | Level 0: locked at G3 | Gate fidelity |
| S_φ(f) ≤ −101 dBc/Hz | All | Level 0: locked at G3 | Gate infidelity |
| Δν_source ≤ 500 kHz | All CW | Level 1: absolute linewidth | Detection SNR, long-term drift |
| M² ≤ 1.2 | All | Level 1: beam quality | Ion-side waist, Ω_R uniformity |
| L_passive per stage | Next-gen, IC-VECSEL | Level 1: impedance match | Buildup, UV output, thermal load |
| T_oven stability | Next-gen, IC-VECSEL | Level 1: thermal-load envelope | Phase-matching drift, output stability |
| P_pump ≤ 10 W | Next-gen | Level 1: thermal-load envelope | Crystal damage, coating degradation |
| Sealed-envelope class | IC-VECSEL | Level 1: UV robustness (G2) | Degradation rate, lifetime |
| f_rep jitter | Pulsed Raman | Level 1: timing stability | Motional dephasing |
| τ_pulse, λ_fund | Pulsed Raman | Level 1: derived from Δ, Ω_R | Conversion efficiency, spectral overlap |

### 4.2 Missing: explicit G2-degradation-rate inheritance
All three architectures mention G2 but do not quantify how a *failed* G2 closure (i.e., degradation rate higher than expected) affects each architecture.

**Tighten:** Add a **G2-failure impact table** to each architecture page:

| Architecture | If G2 closes at X %/100 h | Mitigation | Fallback |
|---|---|---|---|
| Next-gen 500 mW | UV output drops below 500 mW at t = 100 h; operating lifetime unacceptable | Tighten L_passive budget; reduce crystal intensity; improve coatings | Reduce UV target to 300 mW; accept shorter maintenance interval |
| IC-VECSEL | At 50 mW UV, degradation is slower; 20 % drop → 40 mW still viable for cooling | Sealed envelope is primary mitigation; hard-fluoride coatings secondary | Increase visible drive to compensate; accept shorter BBO mirror life |
| Pulsed Raman | Pulsed peak fluence may *accelerate* degradation; G2 failure is more severe | Larger spot size in BBO; lower rep rate; longer pulse | Move to OPA-assisted tripling at lower peak intensity |

### 4.3 Missing: Phase 4 axis pre-scoring readiness check
The six fixed Phase 4 scoring axes (CHARTER §5.2, `docs/principles.md`) should be populated with **draft scores** or at least **score ranges** for each architecture before the slate opens.  Currently none of the three documents do this.

**Tighten:** Add a **Phase 4 readiness checklist** to each architecture page:

| Axis | Next-gen | IC-VECSEL | Pulsed Raman | Data source |
|---|---|---|---|---|
| 1 Raman capability | TBD (NG-C/D) | N/A (task split) | TBD (pulsed primitive) | Simulation / literature |
| 2 Phase coherence | TBD | TBD (PDH residual noise) | TBD (rep-rate lock jitter) | Measurement / vendor spec |
| 3 UV robustness | TBD (NG-E + G2) | Better (sealed envelope) | Worse (peak fluence) | G2 protocol |
| 4 Thermal / nonlinear load | TBD (NG-D) | Lower (50 mW target) | Lower (no cavities) | Simulation |
| 5 Tunability / modularity | TBD | Good (VECSEL mode-hop range) | Excellent (comb tooth selection) | Literature |
| 6 Complexity | TBD | TBD (envelope engineering) | TBD (comb lock + tripler) | Component count |

**Recommendation:** Do not open the Phase 4 candidate slate until every cell in this table has at least a *draft value with citation*.

### 4.4 Missing: Steward decision on the 500 mW indicative anchor under task split
The CHARTER §1.5 and §6.1 lock in ≥ 500 mW CW UV as a single-architecture success criterion.  The IC-VECSEL + pulsed-Raman split decomposes this into ~50 mW CW + ~0.1–0.5 W pulsed.

**Tighten:** The task split is architecturally coherent, but it changes the **success-criterion interpretation**.  Under CHARTER §9 success-criterion change protocol, this requires Council-3 deliberation + Integrator sign-off.  Add an explicit logbook trigger:
> *"Does this task-split alter CHARTER §6.1 (CW output ≥ 500 mW at 280 nm, sustained for ≥ 8 h)?  Yes — it replaces the single-architecture criterion with a multi-architecture criterion.  This triggers Council-3 deliberation under §9."*

---

## 5 · Recommended immediate actions (priority order)

| Priority | Action | Owner | Effort | Blocks |
|---|---|---|---|---|
| P1 | Add G1-inheritance and G2-failure-impact paragraphs to all three architecture pages | Steward | 0.5 h | Nothing |
| P2 | Define the (nominal, lower, upper) parameter triple for the pulsed-Raman Ti:S operating point (λ, τ, f_rep, P_avg) | Steward / lit. extraction | 0.5 h | Pulsed primitive spec |
| P3 | Define the IC-VECSEL visible-power go/no-go boundaries (170 mW / 250 mW / 500 mW) linked to BBO efficiency bounds | Steward | 0.5 h | `shg_intracavity.py` primitive |
| P4 | Populate the Phase 4 axis readiness checklist with draft scores for all three architectures | Steward | 1 h | NG-A through NG-E for next-gen; literature for alternatives |
| P5 | Write the cross-cutting traceability matrix (§4.1) as a shared table in `docs/architectures/index.md` | Steward | 1 h | Nothing |
| P6 | File a logbook entry triggering Council-3 deliberation on the multi-operating-point / task-split success-criterion question | Steward | 0.5 h | Phase 4 slate opening |
| P7 | Tighten NG-B forward map with hard 10 W pump ceiling and ASE-class bifurcation | Notebook author | 0.5 day | NG-A |
| P8 | Add thermal-isolation spec (R_th, ΔT_budget) to IC-VECSEL sketch | Notebook author | 0.5 day | Thermal simulation |
| P9 | Add timing-jitter budget and lock-architecture spec to pulsed-Raman sketch | Notebook author | 0.5 day | Literature extraction |

---

## 6 · Conclusion

The three architecture sketches are intellectually sound and correctly positioned within the project's governance framework.  **The gap between sketch and build-ready specification is primarily one of numerical tightening:** every range needs a nominal point with confidence bounds, every qualitative claim needs a quantitative test, and every open question needs a decision boundary.  The recommendations above, if implemented, would bring all three architectures to the point where Phase 4 scoring can be executed falsifiably against the six fixed axes — which is the stated purpose of the pre-G2 exploratory phase.

The highest-leverage single action is **P6** (Council-3 trigger on task-split success criteria), because it governs whether the IC-VECSEL + pulsed-Raman pair is even admissible as a Phase 4 candidate.  The next-highest is **P3** (IC-VECSEL visible-power go/no-go), because it identifies whether the sketch has a fatal scaling gap before any procurement begins.
