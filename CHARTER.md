# Charter — UV Source Redesign for ²⁵Mg⁺ Detection, Cooling, and Coherent Control

**Working title.** `mg-plus-uv-chain` (alternative: `uv-source-redesign`)
**Steward.** Ulrich Warring (Albert-Ludwigs-Universität Freiburg, AG Schätz)
**Date opened.** 2026-04-30
**Charter version.** v1.0 (FROZEN — all four signatures applied; repository initialised at this version)
**Visibility.** Public from day one (decision recorded 2026-04-30)

---

## 0. Endorsement marker

This document is a *coastline* under local stewardship (AG Schätz, Universität Freiburg). It cites external coastlines — laser physics, Boyd–Kleinman theory, crystal manufacturer data, published source designs — as constraints rather than replicating them. Endorsement scope: local. Harbour epistemology applies: this is a map of a chosen design space, not a claim about underlying physics beyond what is already endorsed elsewhere.

Council-3 ADM-EC governs major architectural decisions (Guardian / Architect / Integrator vetoes apply).

---

## 1. Purpose

To redesign the all-solid-state CW laser source producing radiation near 280 nm for trapped ²⁵Mg⁺ work. The source must support three operational modes:

1. **Detection** of ²⁵Mg⁺ on the ³S₁/₂ → ³P₁/₂ and ³P₃/₂ transitions.
2. **Doppler cooling** on the same transitions.
3. **Two-photon stimulated Raman transitions** for coherent spin–motion control (qubit gates, motional-mode manipulation, sideband cooling diagnostics).

The Raman mode introduces tighter constraints than detection/cooling alone: higher single-beam intensity at controlled detunings, accessible detuning regions free of unlockable resonances, and preservation of common-mode phase-noise rejection between the two Raman beams.

The reference baseline is Friedenauer et al., *Appl. Phys. B* **84**, 371 (2006), produced in the same group lineage twenty years prior. The redesign incorporates intervening progress in fibre and VECSEL laser sources, nonlinear crystal options, cavity-locking schemes, and UV-induced degradation diagnostics.

The repository is simultaneously a *design artefact* (the new source) and a *reproducible record* (data, simulations, decisions, dead ends).

---

## 1.5 Constraint hierarchy (Architect insertion, v0.4)

The previous §2 listed source-side targets without an explicit upstream layer. Architect mandate: source specifications must be derived from task constraints, not asserted in isolation. Three nested levels apply.

### Level 0 — Task constraints (non-negotiable, ion-side)

Raman coupling requirements for ²⁵Mg⁺ spin–motion control:

- Detuning window Δ from ³P₁/₂ and ³P₃/₂ — admissible range
- Target two-photon Rabi frequency Ω_R (envelope, not point value)
- Acceptable spontaneous-scattering rate Γ_sc per gate
- Allowable relative phase-noise spectral density S_φ(f) between Raman beams
- Beam geometry at the ion: waist, propagation directions, k-vector projections onto motional modes

Detection and Doppler cooling impose looser intensity / linewidth constraints; the Raman mode is the binding case.

### Level 1 — Derived optical constraints (between source and ion)

- Required single-beam intensity at the ion to reach target Ω_R at chosen Δ
- Required UV power at the experiment input *after* the optical loss budget (source → ion)
- Beam quality (M² envelope)
- Frequency agility / tuning continuity across the admissible Δ range
- **Absolute UV-source linewidth bound (v0.8 external-Verifier addition).** Detection and Doppler cooling require source linewidth comfortably below the natural transition linewidth (~40 MHz for ²⁵Mg⁺ ³P levels) — order-of-magnitude bound at v0.8: ≤ 1 MHz at 280 nm. Raman common-mode rejection makes *relative* phase noise the binding case for the gate, but the *absolute* linewidth is binding for detection / cooling SNR and for any frequency referencing within the optical loss chain. Tightened by Phase 0.5 against detection / cooling requirements and against the absolute-noise floor under common-mode rejection.
- Cavity impedance-matching condition: input coupler reflectivity R_in matched to total round-trip loss (linear absorption + scatter + nonlinear conversion at design power); output coupler transmission T_out specified at the harmonic wavelength; HR coating reflectivity and UV damage threshold at all relevant wavelengths. Reflectivity values are not free parameters — they are derived from the loss budget per stage.
- **Thermal-load envelope** (Architect-touching, v0.6 Scout-driven). Maximum acceptable pump power into the most-stressed nonlinear stage; maximum acceptable crystal/coating temperature rise above ambient; minimum acceptable conversion efficiency consistent with the thermal budget. Numerical envelope set by Phase 0.5 in coordination with the §8.2 degradation protocol. Without this bound, "constraint-class" efficiency in §2 remains formally unbounded — a candidate architecture with very low efficiency could appear to satisfy §6.1 (8 h stability) only under unrealistic cooling assumptions.

### Level 2 — Source constraints (§2)

The figures in §2 are *derivations* from Levels 0 and 1, not free choices. The 500 mW headline is retained as an indicative anchor; its binding form is the §2 row coupling Ω_R, Δ, and S_φ(f).

**Stall mitigation (Guardian note; expanded by Integrator at v0.9).** Phase 0.5 (§5) extracts Level 0 numbers. Where exact values are not yet fixed experimentally, *envelopes* and *scenarios* are admissible — but the envelope must be locked before Phase 4 begins.

If even precise envelopes cannot be fixed at Phase 0.5 closure, the deliverable may instead specify a **labelled bounded-scenario set**: *Conservative / Nominal / Aggressive* triples consistent with the Level 0 / Level 1 corridors. Phase 4 scoring must then be performed *at minimum on the Conservative scenario*; Nominal and Aggressive may be scored as sensitivity tests. This codifies the v0.7 envelope-not-operating-points clause into an executable process — Phase 4 cannot start with unconstrained or hand-wavy Level 0 envelopes.

---

## 2. Target specifications (Level 2; derived from §1.5)

| Quantity | Friedenauer 2006 | Target | Status |
|---|---|---|---|
| UV power at 280 nm (CW), source side | 275 mW | ≥ 500 mW (indicative; binding form below) | Locked, indicative |
| Coupled Raman specification (binding) | not formulated | Ω_R envelope at chosen Δ envelope, with S_φ(f) bound and M² envelope, derived per §1.5 Level 0 → Level 1 | **Open — set by Phase 0.5** |
| Long-term stability | ≈ 5 % with thermal isolation; 10 % drift / 2 K | RIN, polarisation, drift envelopes (1 h / 8 h / week), upstream-anchored to §1.5 Level 0 | **Open — set by Phase 0.5** |
| Tunability across ²⁵Mg⁺ transitions (³S₁/₂ → ³P₁/₂, ³P₃/₂) | yes, but with one 14-GHz unlockable domain | resolved, or characterised, attributed and documented | Locked |
| Raman-mode suitability (two-beam architecture, common-mode noise rejection, accessible detunings free of unlockable domains) | partially blocked by §4 of Friedenauer 2006 | full Raman map: usable detuning regions, noise budget, beam-pair generation scheme | Locked |
| Overall conversion efficiency (1118 → 280, or equivalent) | 15.2 % | TBD — treated as a *thermal-management constraint* coupled to §8.2/§8.4, not a free parameter | Derived, constraint-class |
| Architecture | quadrupling 1118 → 559 → 280 | open (see §4) | Open |

---

## 3. Preserved vs. replaced

This needs to be set explicitly so EC has an anchor.

**Preserved (default; revisit only if literature dossier shows otherwise):**
- ²⁵Mg⁺ as the target ion species
- Detection and Doppler cooling at the ³S₁/₂ → ³P₁/₂ and ³P₃/₂ lines near 280 nm
- Two-photon stimulated Raman capability for spin–motion control (single-source-derived beam pair preferred unless dual-source architectures demonstrate equivalent or better noise performance)
- All-solid-state architecture (no dye lasers, no flashlamp pumping)

**Open for redesign:**
- Pump-laser source (e.g. 1118 nm fibre laser, VECSEL systems, or other CW solid-state options)
- Intermediate wavelength(s)
- Crystal choice at every stage
- Cavity geometry, locking scheme, polarisation handling
- Cavity mirror coating specifications: input coupler reflectivity R_in (impedance-matched to per-stage loss budget per §1.5 Level 1), output coupler transmission T_out at harmonic, HR coating reflectivity, and certified UV damage threshold at design fluence
- Environmental control (gas atmosphere around UV crystal)
- Beam-pair generation method for Raman (post-source AOM split, dual-AOM, phase-locked dual-source, etc.)

**Out of scope (non-goals):**
- Pulsed UV systems (the stroboscopic / fs-comb discussion with Leibfried is a distinct project)
- Replacement of trap or vacuum apparatus
- Industrial productisation
- Any architecture requiring radioactive, controlled, or export-restricted components

---

## 4. Architecture decision boundary

The repository considers all CW routes to ≥ 500 mW at 280 nm. Candidate families for the literature dossier:

1. **Quadrupling (Friedenauer baseline).** Single source → 2× SHG. Variants: alternative pump (fibre, VECSEL), alternative crystals (CLBO at the UV stage), Brewster vs. AR-cut, intra- vs. extra-cavity.
2. **Sum-frequency mixing.** Two sources combined to 280 nm. Examples: 1064 + 376 → 280; 532 + 591 → 280; 559 + 559 → 280 (degenerate case = quadrupling).
3. **Hybrid architectures.** Dual sources (fibre and/or VECSEL), one doubled and one mixed; or doubled OPA outputs.
4. **Direct deep-UV sources.** AlGaN diodes, deep-UV VECSELs, optically pumped semiconductor lasers. Treated as literature-only candidates at v0.3; elevation to active candidate requires documented evidence of meeting all §2 specifications including Raman-mode suitability.

**Raman constraint on architecture choice.** Single-source quadrupling preserves common-mode phase-noise rejection between the two Raman beams (split downstream by AOMs from one ²⁵Mg-resonant output). Dual-source SFG and hybrid architectures break this rejection unless an active phase-lock is added. The architecture-comparison table (Phase 4) must score this explicitly.

**Counter-observation (Scout/peer input, v0.3).** Modern phase-locked dual-source architectures can achieve sub-Hz relative linewidth and may offer detuning flexibility, modular upgrades, and reduced UV stress per stage. Phase coherence is increasingly engineerable; UV-induced degradation in nonlinear crystals is not, in the same sense. This observation is recorded as a design-bias check, not as a thesis: Phase 4 scoring must weigh it without privileging family 1 by inheritance from this Charter's framing.

**Design-bias check (Guardian flag, v0.3).** The existence of a Friedenauer 2006 baseline and a "preferred unless" wording under §3 must not produce evidence-weighting bias toward family 1 in Phase 4. The single-source preference under §3 is a default for noise-rejection inheritance; it is not an architecture-selection bias. The Phase 4 rubric must apply identical evidence standards across all four families.

A falsifiable comparison table (Phase 4) will reduce these to a recommendation.

---

## 5. Phases and deliverables

| Phase | Deliverable | Owner | Status |
|---|---|---|---|
| 0 — Charter | This document; repo scaffold | Steward | **DRAFT** |
| 0.5 — Constraint extraction (Architect insertion, v0.4) | `constraints/raman-requirements.md`, `constraints/loss-budget.md`, `constraints/phase-noise-budget.md` — numerical envelopes for §1.5 Level 0 and Level 1. *Phase 0.5 locks numerical envelopes, not final operating points* (v0.7 Architect clarification). **Reference operating point requirement (v0.8 external-Verifier refinement):** at least one concrete reference triple {Δ_ref, Ω_R,ref, Γ_sc,ref} consistent with the envelopes. **Bounded-scenario-set fallback (v0.9 Integrator):** if precise envelopes cannot be fixed, deliver a Conservative / Nominal / Aggressive scenario set per §1.5. Numeric anchor for Δ at v0.8: order ~10 GHz to ~100 GHz from ³P_{1/2,3/2}. | Steward | TODO |
| 1 — Literature dossier | `KD-2026-XXX-uv-280nm.md` (Kompass-Dossier format), including a dedicated **crystal/coating evidence table** covering BBO, CLBO, LBO-relevant stages, coating degradation modes, hygroscopic and environmental constraints, and vendor / batch sensitivity (v0.8 Architect-stress-test recommendation; addresses crystal-choice centrality without restructuring phase architecture) | Steward | TODO |
| 2 — Baseline | Measurement protocol + first-pass data on the existing chain; discriminant scans for §8.1; degradation tuple per §8.2 | Steward | TODO |
| 3 — Simulation framework | Boyd–Kleinman cavity model (including impedance-matching with full per-stage loss budget — linear absorption, scatter, nonlinear conversion, coating contributions); damage/degradation model; parameter sweeps; ≥ 90 % test coverage | Steward | TODO |
| 4 — Architecture comparison | Falsifiable comparison table against fixed scoring axes (below); recommendation | Council-3 | TODO |
| 5 — Build and validation | Procurement, assembly, validation against §2 targets | Steward | TODO |
| 6 — Publication | Manuscript (technical report or peer-reviewed venue; venue selected before phase entry) + Zenodo deposit + tagged release | Steward | TODO |

Phase ordering: Phase 0.5 precedes the architecture comparison gate (Phase 4) absolutely. Phases 1, 2, 3 may run in parallel or interleave once Phase 0.5 envelopes are locked.

### 5.1 Kill-gates (Architect insertion, v0.4)

Hard gates that block downstream phases:

- **G1 (between Phase 2 and Phase 3).** The 14-GHz unlockable domain (§8.1) must be either *attributed* (mechanism identified) or explicitly classified *Underdetermined* per §8 outcome classification. **Architecture-family-specific** Phase 3 simulation does not begin until G1 closes.

   *Anti-seeding clause (v0.6 Scout-driven; v0.7 Architect refinement).* G1 blocks any architecture-family-specific simulation. No Boyd–Kleinman optimisation, impedance-matching computation, or parameter sweep on any candidate architecture (including the Friedenauer quadrupling baseline) may be committed to `/src/` before G1 closes. Pre-G1 exploratory notebooks are permitted in `/notebooks/` provided they carry a `pre-G1, exploratory, not promoted` header and remain unpromoted. **Architecture-neutral shared infrastructure may be committed to `/src/` pre-G1** provided it is genuinely architecture-agnostic — examples: SI-units handling, generic ABCD cavity utilities, generic Boyd–Kleinman functions without architecture presets, test fixtures, plotting utilities. Commits classified by the Steward as architecture-neutral are reviewable by any stance; if disputed, the commit is reverted and the question routed to Council-3. This prevents implicit baseline bias from entering the simulation codebase before the architecture comparison is structurally open, while not blocking neutral tooling.

   *Diagnostic surrogate exception (v0.8 external-Architect refinement; retirement-path wording per Architect re-confirmation; mechanical enforcement per v0.9 Integrator).* If §8.1 attribution requires architecture context — e.g. cavity geometry, coating stack, intra-cavity intensity profile — one or more *diagnostic surrogate architectures* may be instantiated in `/src/` pre-G1, subject to: (a) explicit `diagnostic-surrogate, not-candidate` header in every file; (b) registration in `/logbook/` as surrogate, with stated hypothesis under test; (c) absolute exclusion from Phase 4 scoring — surrogates may not be promoted to candidates; (d) at G1 closure, retirement into `/notebooks/archive/` or `/src/diagnostic_surrogates_archive/`, with no import path into production simulation code (prevents accidental reuse). The "no import path" rule (d) is **mechanically enforced** by an automated test in `/tests/` that fails the build if any production module imports from `/src/diagnostic_surrogates_archive/`. The Integrator confirms this enforcement at G1 closure. This makes the rule mechanically testable rather than culturally enforced, which is essential once the repository is public. Abuse (surrogate evolves toward a candidate, or import path leaks) triggers Architect veto.
- **G2 (between Phase 2 and Phase 4).** The degradation protocol (§8.2) must produce reproducible exposure-history dependence on the existing chain. A non-reproducible protocol cannot be carried into Phase 5.
- **G3 (between Phase 0.5 and Phase 4).** Raman requirement envelopes (§1.5 Level 0) must be numerically stated before architecture scoring begins. No exceptions.

### 5.2 Phase 4 fixed scoring axes (Architect insertion, v0.4)

Axes are declared before evaluation. *No axis may be introduced or removed during Phase 4*; weights are also frozen at Phase 4 entry to prevent path-dependent comparison.

1. **Raman capability (primary axis).** Achievable Ω_R as a function of Δ; detuning continuity (presence/absence of forbidden domains).
2. **Phase coherence.** Intrinsic (single-source-derived) vs. engineered (phase-locked); robustness under thermal and mechanical drift.
3. **UV robustness.** Degradation rate per §8.2 protocol; sensitivity to gas environment, humidity, exposure history. Crystal contribution and **coating contribution** (§8.6) must be partitioned in scoring, not aggregated.
4. **Thermal / nonlinear load.** Intensity at the most-stressed crystal; expected lifetime under operating conditions; coupling between efficiency (§2) and thermal gradients.
5. **Tunability and modularity.** Detuning agility; ability to upgrade or replace stages without full rebuild.
6. **Complexity and maintainability.** Component count; alignment-degree-of-freedom count; documented failure modes and recovery paths.

Weights are set in a Phase 4 pre-scoring deliberation logged in `logbook/`. The "engineerable phase coherence vs. non-engineerable UV degradation" tension (raised in Architect / Verifier reviews) maps onto axes 2 and 3 explicitly.

**Weight transparency clause (v0.6 Scout-driven).** The pre-scoring deliberation must apply identical evidentiary standards to all axes. No axis may receive zero weight without a documented justification of irrelevance to §1.5 Level 0. Axis 1 (Raman capability) holds primary status by Level 0 derivation; other weights are set by evidentiary impact on Level 1, not by stance preference. Weight changes during Phase 4 are forbidden (per the axis-fixing rule above); weight revision between Phase 4 entries (revisits) requires Council-3 deliberation logged in `/logbook/`. This clause exists to prevent a favoured architecture from being protected by weight manipulation.

**Reference-triple anchoring (Integrator insertion, v0.9).** Architecture scoring on axes 1–4 must, at minimum, be computed at the Phase 0.5 reference triple {Δ_ref, Ω_R,ref, Γ_sc,ref} (or, if the bounded-scenario-set fallback applies, at the Conservative scenario triple). Broader envelope-based scoring is admissible as supplementary evidence but cannot substitute for the reference-anchor computation. This prevents asymmetric comparisons in which one architecture is evaluated at a friendly operating point and another at a harsh one — a known failure mode in Raman-source comparisons.

### 5.3 Gate closure protocol (Integrator insertion, v0.9)

Each kill-gate (G1, G2, G3) closes via a logbook entry following a fixed template:

- **Gate ID** (G1, G2, or G3)
- **Date and Steward signature**
- **Evidence artefacts**: for G1, Phase 2 discriminant-scan reports (§8.1) and outcome classification (Resolved / Operationally bounded / Underdetermined); for G2, reproducibility evidence for the §8.2 degradation protocol; for G3, the Phase 0.5 reference triple {Δ_ref, Ω_R,ref, Γ_sc,ref} or the Conservative-scenario triple from the bounded-scenario fallback
- **Council-3 acknowledgement**: Integrator confirmation is mandatory for closure; Architect or Guardian may flag and request review before closure is final
- **Mechanical-enforcement attestations** where applicable (e.g. for G1, confirmation that the diagnostic-surrogate import-path test in `/tests/` is passing)

Architecture-specific work in `/src/architecture/` and downstream phase deliverables may not proceed past a gate until an **Integrator-acknowledged** logbook entry exists for that gate. Closure is not retroactive — entries must be filed before dependent work begins.

A logbook template `logbook/_templates/gate-closure.md` will be committed at v1.0 cut to standardise these entries.

---

## 6. Success criteria (falsifiable)

The redesign succeeds iff *all* of the following hold at first stable release:

1. CW output ≥ 500 mW at 280 nm, sustained for ≥ 8 h continuous operation.
2. Drift envelope satisfies the budget set during Phase 2 (currently TBD).
3. Tunability across ²⁵Mg⁺ transitions with no unlockable frequency domain, *or* the unlockable domain characterised, attributed, and documented.
4. Raman-mode validated by **beam-parameter sufficiency argument evaluated against §1.5 Level 0 constraints**: documented beam parameters (power, detuning map, relative phase-noise / common-mode rejection, mode quality) together with computed Ω_R at the chosen Δ, demonstrated to exceed the Level 0 target by safety factor S ≥ 2. All parameters traceable to either direct measurement (Phase 2 or 5) or simulation validated against measurement (Phase 3 cross-checked against Phase 2). Ion-based experimental demonstration is downstream of this Charter and outside its scope (cf. §3 non-goals on trap apparatus); a future trap-side validation would constitute a separate project.
5. UV-power degradation rate ≤ X %/100 h under specified operating environment (X to be set in Phase 2).
6. Repository public, FAIR-compliant, with all raw data, processed data, simulation source, and decision log published under the chosen licenses.
7. Reproducibility: an informed laboratory can reproduce the design rationale, parameter choices, simulations, protocols, and validation logic from the repository alone. Physical rebuild remains contingent on component availability and local implementation; this is acknowledged explicitly rather than promised.

Failure of any criterion classifies the project as *Divergent* (Council-3 protocol) — archived honestly rather than retro-fitted.

---

## 7. FAIR and version-control commitments

- Public GitHub repository, MIT or Apache-2.0 for code, CC-BY-4.0 for documents (license decision pending).
- `CITATION.cff` with all contributors and ORCID identifiers.
- Zenodo concept-DOI on first stable tagged release (mirroring the CCUF v1.0.0 / Zenodo workflow).
- `parameters.py` as SI-units contract layer (mirroring `single-25Mg-plus` v1.0.0).
- `CONVENTIONS.md` matching the AG Schätz norm.
- All measurement data: raw and processed separated; metadata schema declared in `data/README.md`.
- All design decisions logged with rationale, alternatives considered, and reversibility flag.

---

## 8. Open boundaries (live, must not be quietly closed)

**Outcome classification (Architect insertion, v0.4).** Each open boundary closes into one of three states, propagated into Phase 4 scoring:

- **Resolved** — mechanism identified, attribution evidence-based.
- **Operationally bounded** — effect predictable and characterised, mechanism not isolated.
- **Underdetermined** — discriminant set ran, no attribution achieved (this is itself a documented result, not a failure).

The classification is mirrored from the Breakwater Claim Analysis Ledger 3-value vocabulary (COMPATIBLE / UNDERDETERMINED / INCONSISTENT) where applicable.

1. **14-GHz unlockable resonance domain.** Friedenauer 2006 §4. Reproduced across crystals from one manufacturer, never explained. The original paper notes this "imposes restrictions for two-photon stimulated Raman transitions via detuned levels" — for the present redesign this is therefore not merely a tunability annoyance but a Raman-mode constraint that must be characterised regardless of architecture chosen.

   *Discriminant experiment set (Phase 2 mandate).* The "characterised, attributed, and documented" clause of §6.3 requires *attribution* attempts, not merely reproduction. Minimum discriminant scans: (i) cavity scan vs. crystal temperature — refractive-index / coating hypothesis; (ii) scan vs. input polarisation — birefringence-coupling hypothesis; (iii) scan vs. intra-cavity intensity — photochemical / colour-centre formation hypothesis; (iv) scan vs. crystal manufacturer batch and cut — impurity / growth hypothesis. Inability to discriminate is itself a documented result, not a failure.
2. **UV-induced BBO degradation, gas-environment dependence.** Active diagnostic in the current chain (UV-degradation working notes 2026-04). N₂ vs O₂ vs dry-air decision still open. Carries forward into the new design.

   *Operational definition (Phase 2 mandate).* "Degradation" must be defined as a tuple — {output-power loss, mode-quality distortion **including time-resolved M² profiling**, phase-noise increase, polarisation drift} — measured time-resolved with documented exposure history. Single-number degradation rates without protocol attribution are not acceptable inputs to §6.5. The protocol itself is part of the deliverable, not an implementation detail. Time-resolved M² is mandatory: UV-induced damage frequently manifests as beam distortion (thermal lensing, photorefractive effects) before total power failure.
3. **Stability budget.** §2 placeholder; quantified in Phase 2.
4. **Damage threshold model.** CW LIDT in BBO at 280 nm is observed in the institutional record (UV-degradation working notes 2026-04) and reported in published literature (to be cited in the literature dossier) to depend on factors beyond the intrinsic crystal threshold — candidate mechanisms include colour-centre formation, hygroscopic surface effects, and gas-environment dependence. The Charter does not endorse any specific mechanism; it commits to the measurement protocol and operational definition (§8.2) sufficient to set the §6.5 threshold. The Raman mode raises peak intensity at the crystal and tightens this concern.
5. **Polarisation drift of the fibre amplifier heat sink.** Friedenauer 2006 §5; possibly resolved by active Peltier control. Carries forward as a candidate, not a default. VECSEL pump options may avoid this failure mode altogether.
6. **Mirror coating UV-induced degradation.** HR and OC coatings at 280 nm are known in the literature and institutional record to degrade under UV exposure: reflectivity drift, scatter-loss increase, and absorption-induced thermal lensing. Effects: shifted impedance match (drives §1.5 Level 1 coupling away from optimum over time); coupled to §8.2 degradation tuple but mechanistically distinct from crystal degradation.

   *Partition requirement (Phase 2/5 mandate).* The §6.5 degradation budget must partition crystal contribution vs. coating contribution. Methods: swap-test (substitute fresh coatings, measure recovery) or witness-mirror in beam path. Vendor / batch effects analogous to §8.1 apply: coatings from different runs of the same vendor are not equivalent objects.

   *Method validation (v0.6 Scout-driven).* The chosen partition method must itself be validated in Phase 2 *before* its results are admitted as inputs to §6.5. Validation criteria: (a) for swap-test, evidence that disassembly/reassembly does not introduce alignment-state confounders that mimic or mask coating effects; (b) for witness-mirror, evidence that the witness experiences fluence, incidence angle, polarisation, and gas environment representative of the intra-cavity coatings under test. If neither method validates, this boundary closes as *Underdetermined* per the §8 preamble rather than producing artefactual data that contaminates §6.5.

   *Outcome classification* per §8 preamble: applies (Resolved / Operationally bounded / Underdetermined).

---

## 9. Governance

- **Deliberative body.** Council-3 ADM-EC.
- **Stances and vetoes.** Guardian (clarity / ethics), Architect (structure / logic), Integrator (process / flow). Each veto must cite the violated Core Function.
- **Chart-Transition Protocol** (Constitution v0.4) applied to deliberations crossing stance boundaries.
- **Council-3 scope.** Council-3 deliberation applies to *architectural decisions*: architecture-family selection, success-criterion changes, phase-structure changes, Charter version transitions. *Routine experimental tactics* within an agreed protocol — alignment, calibration, measurement-batch decisions — do not require pre-deliberation but are recorded in the logbook for retrospective audit. The boundary between architectural and routine is itself reviewable by any stance.
- **Reclassification rule (Architect insertion, v0.4).** Any "routine" decision that changes a §1.5 Level 0 or Level 1 constraint is automatically reclassified as architectural and triggers Council-3 deliberation. This protects the constraint hierarchy from silent erosion under operational pressure.
- **Logbook trigger question (v0.6 Scout-driven).** Each logbook entry header must answer the question: *"Does this entry alter, relax, or tighten any §1.5 Level 0 or Level 1 parameter?"* If yes, the entry is auto-flagged as architectural and Council-3 deliberation is invoked. This is a one-line audit mechanism — friction-light but closes the self-reporting gap in the reclassification rule.
- **Erosion protection (Integrator insertion, v0.9).** Logbook entries flagged under the trigger question above require explicit Council-3 deliberation *and* Integrator review *before* the change takes effect. The protection is asymmetric: Level 0 envelopes may be **tightened** based on new evidence with documented rationale; Level 0 envelopes may **not be relaxed** without a Council-3 decision logged in `/logbook/` and explicit Integrator sign-off. This prevents post-hoc goalpost movement under operational pressure when performance proves harder than expected.
- **Success-criterion change protocol (Integrator insertion, v0.9).** Any change to §6 success criteria — particularly the ≥ 500 mW figure (§6.1), the 8 h sustained operation (§6.1), the drift envelope (§6.2), the §1.5 Level 0 reference triple flowing into §6.4, or the X %/100 h degradation rate (§6.5) — requires Council-3 deliberation with explicit stance attribution and **Integrator sign-off**. Steward-only changes to success criteria are forbidden. This places §6 at the same governance level as architecture selection and as Level 0/1 erosion. The protocol is symmetric for tightening and relaxation: both require Council-3 + Integrator. (Tightening to lock in a stronger-than-expected result is a meaningful change and deserves the same audit trail as relaxation.)
- **Logbook.** All architectural decisions recorded in `logbook/YYYY-MM-DD-<topic>.md` with stance attribution where applicable.

---

## 10. Repository scaffold (proposed)

```
mg-plus-uv-chain/
├── README.md
├── CHARTER.md                         ← this file
├── CONVENTIONS.md
├── CITATION.cff
├── LICENSE                            ← code
├── LICENSE-DOCS                       ← documents (CC-BY-4.0)
├── endorsement.md                     ← Coastline Template v2.0: Endorsement Marker / External Constraints / Novel Boundaries
├── docs/
│   ├── KD-2026-XXX-uv-280nm.md        ← literature dossier
│   ├── architecture-comparison.md
│   ├── stability-budget.md
│   └── degradation-protocol.md
├── constraints/                       ← Architect insertion, v0.4: immutable Level 0/1 reference objects
│   ├── raman-requirements.md          ← §1.5 Level 0
│   ├── loss-budget.md                 ← §1.5 Level 1
│   └── phase-noise-budget.md          ← §1.5 Level 0/1 boundary
├── src/
│   ├── parameters.py                  ← SI-units contract
│   ├── boyd_kleinman.py
│   ├── cavity_model.py
│   ├── damage_model.py
│   └── architecture/
│       ├── quadrupling.py
│       ├── sfg.py
│       └── hybrid.py
├── tests/                             ← target: ≥ 90 % coverage
├── data/
│   ├── README.md                      ← metadata schema
│   ├── baseline/                      ← measurements on existing chain
│   └── literature/                    ← parameters extracted from cited works
├── notebooks/                         ← exploratory; promoted to src/ when stable
└── logbook/
    └── 2026-04-30-kickoff.md
```

---

## 11. Risks acknowledged at kickoff

- **Scope creep into a general "Mg⁺ apparatus redesign" project.** Mitigated by §3 preserved/replaced and §4 architecture boundary.
- **Public-from-day-one premature commitments.** Mitigated by tagging early commits as `v0.x-draft` and clear endorsement marker stating coastline status.
- **Decision opacity if Council-3 deliberations are not logged.** Mitigated by mandatory logbook entries.
- **Reinventing existing knowledge.** Mitigated by literature-dossier-first ordering and by referencing existing institutional documents (bonding/UHV draft, UV-degradation diagnostic) rather than rewriting them.
- **Premature architecture bias from Friedenauer-baseline framing.** Mitigated by §4 design-bias check and by symmetric Phase 4 scoring across all four candidate families.
- **Efficiency-thermal coupling under-recognised.** Conversion efficiency is a thermal-management constraint, not just a performance metric. Low efficiency at 500 mW UV implies high pump power and thermal gradients in nonlinear crystals, coupling directly to §8.2 degradation. Mitigated by treating efficiency as constraint-class in §2 and by Phase 4 axis 4 (thermal / nonlinear load).

---

## 12. Sign-off block (to be filled before v1.0)

- [x] Guardian (clarity / ethics): *approved for v1.0; no outstanding Guardian veto*
- [x] Architect (structure / logic): *re-confirmed at v0.8, 2026-04-30; diagnostic-surrogate exception, reference-triple requirement, and absolute-linewidth Level-1 placement accepted; stress-test passed for CLBO/BBO, dual-source SFG, quadrupling-retained scenarios; no structural veto for v1.0*
- [x] Integrator (process / flow): *passed at v0.9; six process/flow refinements applied (§5.3 gate closure, §9 erosion protection and success-criterion change protocol, §1.5 + Phase 0.5 scenario fallback, §5.1 mechanical-enforcement test, §5.2 reference-triple anchoring); no veto*
- [x] Steward: *Ulrich Warring — approved for v1.0 cut, 2026-04-30*

End of Charter v1.0.

---

## 13. Charter version transitions

This Charter is itself subject to Chart-Transition Protocol (Constitution v0.4) when stance vetoes or substantive review signals are involved in a v_n → v_{n+1} cycle. Sequence is recorded for path-dependence accountability.

| From | To | Date | Trigger | Stances invoked | Items deferred |
|---|---|---|---|---|---|
| — | v0.1 | 2026-04-30 | Initial Guardian draft | Guardian | n/a |
| v0.1 | v0.2 | 2026-04-30 | Steward edits (names removed; VECSEL added; Raman / coherent-control scope) | Guardian | n/a |
| v0.2 | v0.3 | 2026-04-30 | Scout horizon signals + peer-review consolidation | Guardian (clarity / epistemic-modesty self-correction at §8.4) | Architect-domain items: power↔Rabi-rate coupling; Phase 0.5; kill-gates; stability upstream constraint; fast-path protocol |
| v0.3 | v0.4 | 2026-04-30 | Architect mandates + Verifier consolidation | Architect (structure: §1.5 hierarchy; Phase 0.5; kill-gates G1–G3; Phase 4 fixed scoring axes; §6.4 traceability; §6.7 reformulation; §8 outcome classification; §8.2 M² mandate; §9 reclassification rule; /constraints/ scaffold; §11 efficiency coupling) | Constitution-level: fast-path protocol (Constitution v0.4 open item #2). Generic-template scope expansion (post-v1.0). |
| v0.4 | v0.5 | 2026-04-30 | Steward-initiated cavity-coating addition | Guardian (applied); Architect re-pass requested | Architect re-validation of expanded design space; Integrator review |
| v0.5 | v0.6 | 2026-04-30 | Scout horizon signals (operational tightening, no new boundary) | Guardian (4 items applied); Architect-touching (1 item: thermal-load envelope, flagged) | Architect re-pass on §1.5 thermal-load envelope and §8.6 partition validation; Integrator review |
| v0.6 | v0.7 | 2026-04-30 | **Architect formal sign-off** + minor G1 edit + 2 non-blocking refinements | Architect (sign-off); Guardian (registered) | Integrator review (sole remaining pass at the time) |
| v0.7 | v0.8 | 2026-04-30 | External Architect-Verifier-Integrator probe; two blocking findings (G1 deadlock; Phase 0.5 ill-posedness) plus one Verifier addition (absolute linewidth bound) | external Architect (R1: diagnostic surrogate exception; R2: Phase 0.5 reference operating point); external Verifier (G2: absolute UV linewidth bound); Guardian (registered) | (closed below at re-confirmation) |
| v0.8 | v0.8 (Architect-confirmed) | 2026-04-30 | Architect re-pass on v0.8 structural responses + stress test | Architect (re-confirmed; minor wording fix on surrogate retirement path; Phase 1 deliverable expanded to include crystal/coating evidence table per stress-test recommendation) | Integrator pass (sole remaining); G3 absorbed as Phase 1 evidence-table refinement |
| v0.8 (confirmed) | v0.9 | 2026-04-30 | **Integrator pass** with six concrete process/flow refinements (no structural reopening) | Integrator (gate closure protocol §5.3; Level 0/1 erosion protection §9; Phase 0.5 Conservative/Nominal/Aggressive scenario set §1.5 + Phase 0.5 row; diagnostic-surrogate mechanical-enforcement test §5.1; Phase 4 reference-triple anchoring §5.2; success-criterion change protocol §9); Guardian (registered) | Final Integrator confirmation on v0.9 text; Guardian sign-off; Steward sign-off; v1.0 cut |
| v0.9 | **v1.0 (FROZEN)** | 2026-04-30 | All four signatures applied; repository initialisation | Guardian (sign-off); Architect (sign-off, carried from v0.8); Integrator (sign-off); Steward (sign-off — Ulrich Warring) | Constitution v0.4 fast-path protocol open item carried into `/logbook/2026-04-30-kickoff.md` for resolution at Constitution level (does not block Charter) |

### 13.1 Convergence and termination (Guardian note, retained at v0.9)

Nine revision cycles. v0.6 was the last v0.x absorbing structural additions; v0.7 was Architect clarification; v0.8 admitted two Architect-Verifier blocking findings under the §13.1 carve-out; v0.9 absorbed six Integrator process/flow refinements without structural reopening. Further signals after v0.9 are held for v1.x. Absolute termination: v1.0.

### 13.2 Path to v1.0 (final pass — three sign-offs)

All structural and process-flow edits are now in. The remaining steps are signature-only:

1. **Final Integrator confirmation.** Review v0.9 Charter text and confirm the six v0.9 edits are correctly applied and consistent with the Integrator review intent.
2. **Guardian sign-off.** Confirm no clarity / ethics issues remain. (Guardian observation: the §8.4 epistemic-modesty self-correction at v0.3 closed the only substantive Guardian concern; subsequent revisions have maintained the pattern. No outstanding Guardian veto.)
3. **Steward sign-off.** This is the Steward's act and cannot be substituted. Closes v0.9 → v1.0 transition.
4. **v1.0 cut.** Repository scaffold initialised with: README.md (1-page navigational summary pointing into Charter sections by use case), CHARTER.md (this document, frozen at v1.0), CONVENTIONS.md, CITATION.cff, LICENSE, LICENSE-DOCS, endorsement.md (Coastline Template v2.0), `parameters.py` SI contract, `/constraints/` placeholders, `/tests/` with the diagnostic-surrogate import-path test, `/logbook/_templates/gate-closure.md`, and `logbook/2026-04-30-kickoff.md` documenting the nine-cycle deliberation history. First commit tagged v1.0; Zenodo concept-DOI registered.

After v1.0: Phase 0.5 (constraint extraction) begins. Repository goes public. Work proceeds.

### 13.2 v1.0 cut completed (2026-04-30)

All four signatures applied. Repository scaffold initialised at `mg-plus-uv-chain/`. Charter frozen at v1.0 — further changes require a documented v1.x revision under Council-3.

**Steward decisions locked at v1.0 cut (2026-04-30):**

- **Repository name:** `mg-plus-uv-chain`
- **Code license:** MIT
- **Document license:** CC-BY-4.0
- **Constitution v0.4 fast-path protocol:** v1.0 ships with the open item flagged in `/logbook/2026-04-30-kickoff.md`; closure deferred to Constitution-level work, does not block the Charter.

**Next:** Phase 0.5 (constraint extraction) begins. See `/logbook/2026-04-30-kickoff.md` for the canonical record of the nine-cycle deliberation history that produced this Charter.
