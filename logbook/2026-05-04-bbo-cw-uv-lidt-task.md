# BBO CW-UV LIDT and operational-lifetime literature task — 2026-05-04

## Header (Charter §9 trigger question)

- **Affects Level 0 parameter?** no — task is a literature-search scope, not a Level 0 change
- **Affects Level 1 parameter?** *potentially*, depending on outcome — a tight CW-UV LIDT bound at 280 nm could constrain the §1.5 Level 1 *thermal-load envelope* and *intracavity intensity at the UV crystal* parameters. If the literature search converges on a tight bound, the constraint enters Level 1 via the [§1.5 asymmetric erosion-protection rule](../CHARTER.md) (tightening permitted with documented rationale). Logged here so future readers can trace the chain when it happens.
- **Affects success criterion?** no — this task does not change §6 success criteria; it informs the design-space envelope they get evaluated against.

## Stance attribution

- Task draft: assistant under steward direction
- Steward sign-off: pending

## Context

This is the **residual task E** carried over from [`logbook/2026-05-04-bbo-alternative-references.md`](2026-05-04-bbo-alternative-references.md), now opened as its own logbook entry because:

1. The CW-UV LIDT literature is *structurally different* from the Sellmeier / `d_eff` literature handled by tasks A and B. Tasks A and B had a single canonical primary source each (Eimerl 1987, Eckardt 1990, Tamošauskas 2018) — the dispersion equations and the nonlinear-coefficient measurements are mature, well-cited corners of the field with a small number of definitive papers. CW-UV-degradation work is not like that: there is no "canonical" CW-UV LIDT paper for BBO at 280 nm, and most published damage thresholds are *pulsed* (ns or shorter). CW operational lifetime data tends to be embedded in *application papers* (e.g. trapped-ion experiment papers reporting "we replace the BBO every X months") rather than dedicated damage studies.
2. The figure of merit is **operational lifetime under realistic CW intensities and gas environments**, not a single CW-LIDT W/cm² threshold. The intrinsic single-shot damage threshold is well above any CW operating condition; what matters is *time to degradation* — surface, bulk, or coating-mediated — under continuous exposure at ~10–100 W/cm² intracavity intensities, which is what the §5 Phase 1 evidence-table cell captures and what the Friedenauer-baseline architecture actually runs at.
3. This task touches **three dossier entries**, not one. Most of the LIDT discussion belongs in `KD-UV280-005` Section C (the headline number for the §5 Phase 1 evidence-table). The gas-environment / hygroscopic dimension belongs in `KD-UV280-009`. The mechanism (UV-induced colour-centre formation, photo-darkening, surface degradation) belongs in `KD-UV280-011`. Splitting the task to a separate logbook entry lets the three dossier entries pull from one shared candidate-reference list.

## Scope clarification

The task seeks evidence on three operationally distinct quantities, not one:

### Q1 — Intrinsic CW damage threshold at 280 nm

The CW intensity at which *prompt* surface or bulk damage occurs in fresh, high-quality BBO at 280 nm. Likely well above any operating condition in a Friedenauer-class system (where the intracavity intensity is ~10–100 W/cm²); a literature value here primarily sets the headroom for higher-intensity architectures rather than constraining the current baseline.

### Q2 — Operational lifetime under CW UV

Time-to-degradation curves under continuous 280 nm exposure at fixed intensity, fluence, and gas environment. This is what *actually* governs the Friedenauer-class baseline's maintenance schedule (Friedenauer 2006 itself does not report a lifetime; the original MPQ Garching apparatus and its Freiburg descendants would have institutional records here, see Q4). The relevant axes are:

- Intensity (W/cm² intracavity)
- Cumulative fluence (J/cm²·hours)
- Gas environment (ambient air, dry N₂, dry O₂, dry-gas-purged sealed enclosure)
- Surface preparation (Brewster-cut polish quality, AR-coating presence and condition)
- Crystal vendor / growth lot

### Q3 — Mechanism

What *kind* of degradation dominates under CW UV — photo-induced colour-centre absorption (bulk), surface photodissociation in the presence of trace water, coating delamination, or polishing-defect-mediated catastrophic damage. Mechanism affects which mitigations (dry-gas housing, periodic re-polishing, vendor switching, coating swap) are effective and which are not. Belongs in `KD-UV280-011 Section C` (mechanism) and feeds back into `KD-UV280-005 Section C` (operational threshold) and `KD-UV280-009 Section C` (gas environment).

### Q4 — Institutional [I] context

The Friedenauer 2006 baseline apparatus was originally built at MPI für Quantenoptik (Garching, Hänsch / Schätz collaboration) and the steward's group at AG Schätz / Albert-Ludwigs-Universität Freiburg is its descendant. Operational-lifetime records from the original MPQ apparatus and from the present-day Freiburg setup are likely the *highest-quality* CW-UV-LIDT-at-280-nm evidence available, but they are institutional rather than peer-reviewed. The dossier admits these as `[I]` tier per the [Section C source-tier rule](../docs/KD-2026-XXX-uv-280nm.md), provided the entry is classified Underdetermined unless external corroboration is found. This task should explicitly seek out the institutional record alongside the published literature, and document both clearly.

## Candidate references

Bibliographic details are this assistant's best recollection from training corpus and may have errors; the steward should verify before requesting PDFs. Ranked by expected payoff for `KD-UV280-005` Section C.

### A. CW-UV degradation studies on BBO in the 200–300 nm range

The closest literature to a "canonical" CW-UV-LIDT BBO paper is around the 200–300 nm Nd:YAG harmonic range. Candidates the steward may want to scout:

1. **Roth, Tzankov, Petrov 2005-era studies on BBO at 213 nm.** *Optical Materials* or *Applied Physics B* range. Frame: 5th-harmonic-of-Nd:YAG CW operation with explicit lifetime characterisation.
2. **Yoshida, Fujita, Nakatsuka et al. (mid-2000s) on UV-induced absorption in BBO.** *Japanese Journal of Applied Physics* or *Optics Communications* range. Frame: photo-induced absorption mechanism studies, not lifetime per se but informative for Q3.
3. **Cabrera-Granado, Díaz-Caballero et al. work on CW UV degradation in nonlinear crystals at 213 / 266 nm.** Frame: harmonic-of-1064 CW operations.
4. **Nikogosyan 2005 compendium chapter on BBO** — *Nonlinear Optical Crystals: A Complete Survey*, Springer. Already on the [task A/B candidate list](2026-05-04-bbo-alternative-references.md) as `[S:Nikogosyan2005]`. Will likely have a damage-and-degradation summary section that points to primary sources for both pulsed and CW regimes.

### B. Operational-lifetime evidence from trapped-ion / quantum-optics groups using BBO at 280 nm

The class of groups operating Mg⁺ / Be⁺ trapped-ion systems with BBO-at-280-nm cooling lasers is small enough that scouring their published apparatus papers should yield maintenance-schedule information. Candidate group + paper threads:

1. **Friedenauer 2006 itself (MPQ Garching → Freiburg lineage).** Already in the dossier as `[P:Friedenauer2006]`. Reports stability observations (fluctuations within 2%, microsecond drops < 4%, and 10% temperature-driven oscillations over 2 K environmental change) but does *not* state a crystal-replacement schedule or long-term lifetime figure. The institutional [I] record for this apparatus and its successors should be pursued separately (see Q4 above).
2. **NIST / Boulder ion-trap group** (Wineland and successors). Published cooling-laser apparatus details for ²⁵Mg⁺ over multiple decades; some papers may report BBO replacement intervals.
3. **University of Innsbruck (Blatt, Roos)** Be⁺ / Ca⁺ work — adjacent UV crystal use, may have transferable observations.
4. **University of Sussex / Oxford / NPL** quantum-computing groups using ²⁵Mg⁺ or ²⁴Mg⁺ — the more recent (2015+) experimental papers may have explicit BBO-related supplementary material.
5. **AG Schätz Freiburg internal records** — `[I]` tier; the steward's institutional access route. Highest-priority pursuit because directly relevant to the Friedenauer-baseline maintenance history.

### C. Coating-side degradation literature (feeds KD-UV280-008 / -012, not -005)

The dossier already has `KD-UV280-008` (UV mirror coatings — HR, OC, AR specifications and degradation) and `KD-UV280-012` (UV mirror coating degradation under CW exposure) as scaffolded entries. CW-UV coating-degradation literature is typically more developed than crystal-bulk CW-UV degradation; standard candidates are:

1. **Stolz, Genin et al. (LLNL / Spica) UV-coating CW-damage studies** — laser-damage-symposium proceedings, mostly pulsed but sometimes extended to high-repetition-rate / quasi-CW.
2. **Gallais, Commandré et al. UV coating studies.**
3. **Vendor application notes from Layertec, FEEFO, Lambda Research Optics, EKSMA Optics** — `[S]` tier; useful as supplementary but not as Section C primary anchors.

This task should *not* attempt to populate `KD-UV280-008` / `-012`; it should only flag references that crossover into the BBO-at-280-nm context. Coating-only literature search is its own future task.

### D. CLBO comparison literature (feeds KD-UV280-006 / -009)

CW-UV-degradation studies on CLBO at 266 nm and 213 nm are *more developed* than on BBO at 280 nm because CLBO is the workhorse for the Nd:YAG 5th harmonic in the deep-UV. The CLBO literature is the closest analogue and provides:

1. **A point of comparison** for the BBO operational-lifetime numbers when they emerge.
2. **A potential alternative crystal** — `KD-UV280-006` (CLBO at 280 nm) is currently SCAFFOLD; if the BBO CW-UV-LIDT picture turns out unfavourable, CLBO becomes more attractive.
3. **Mechanistic insight transferable to BBO** — both are borate crystals; some surface-degradation mechanisms (water-mediated, OH-incorporation) are shared.

Candidates: Sasaki et al. (Osaka group) on CLBO; Yoshimura, Takei et al. on CLBO durability under CW UV. This task should capture the CLBO citations alongside the BBO ones since they share the bibliographic search path.

### E. Single-source CW-UV-LIDT compendium / vendor sheets

Candidates: SNLO documentation; vendor catalogues from Crystals of Siberia, CASTECH, EKSMA Optics, FEEFO. `[S]` tier — admissible as secondary but not as Section C anchors. Useful primarily for *bracketing* the bulk-LIDT number.

## Acceptance criteria for closing this task

This logbook entry is closed when **all** of the following are true:

1. At least **one** peer-reviewed `[P]` source is cited in `KD-UV280-005 Section C` for either Q1 (CW intrinsic threshold at 280 nm) or Q2 (operational-lifetime curve under realistic conditions). If no peer-reviewed source exists for Q1/Q2 specifically at 280 nm, the entry uses adjacent-wavelength `[P]` sources (e.g. 213, 266 nm) with explicit extrapolation rationale.
2. The institutional `[I]` record from MPQ Garching / AG Schätz Freiburg is either (a) extracted into a dedicated `data/literature/AG-Schatz-internal/` folder following the conventions in `data/literature/<key>/notes.md`, or (b) explicitly deferred with a documented reason. If included, the dossier entry classification per the [Section C `[I]`-only rule](../docs/KD-2026-XXX-uv-280nm.md) is Underdetermined unless external corroboration is found.
3. `KD-UV280-005` Section C "TODO: cite peer-reviewed CW LIDT measurements at 280 nm" bullet is replaced with the populated constraint. The `KD-UV280-009` Section C entry on gas-environment dependence either gains a populated `[P:]` constraint or pings back to this logbook entry as the deferred task.
4. The §5 Phase 1 evidence-table BBO row's "CW LIDT @ 280 nm (W/cm²)" cell either tightens (if A/B/C above produce a value) or splits into "intrinsic / operational lifetime" with separate citations.
5. `KD-UV280-011` is upgraded from SCAFFOLD to POPULATING if mechanism-level literature (Q3) is captured.

## Steward decision queue

This logbook entry is a *task draft*, not a closed gate. The steward decides:

- (a) Which of A / B / C / D to pursue first. Recommendation: **A in parallel with B** (A gives the published CW-UV-LIDT anchor; B gives the operational-lifetime corroboration from quantum-optics application papers). C and D are lower priority and can be deferred.
- (b) Whether to attempt institutional access at AG Schätz Freiburg / MPQ Garching for the Q4 institutional `[I]` record, and on what timeline. If yes, whether the resulting record is committed to the repository (with the same publisher-copyright-style discipline applied to redacting any unpublished data not cleared for release) or kept local.
- (c) Whether to split the resulting work across `KD-UV280-005` (LIDT headline number), `KD-UV280-009` (gas environment), and `KD-UV280-011` (mechanism), or to keep it concentrated under `-005` with cross-references.

## Cross-references

- [`logbook/2026-05-04-bbo-alternative-references.md`](2026-05-04-bbo-alternative-references.md) — parent task list; this entry handles the residual task E that was carved out.
- [`docs/KD-2026-XXX-uv-280nm.md`](../docs/KD-2026-XXX-uv-280nm.md) — KD-UV280-005 Section C "TODO: cite peer-reviewed CW LIDT measurements at 280 nm" is the binding open item. KD-UV280-009 (hygroscopic / environmental) and KD-UV280-011 (UV-induced degradation) are co-targets.
- [`data/literature/Eimerl1987/extracted.yaml`](../data/literature/Eimerl1987/extracted.yaml) — already records that Eimerl 1987's 13.5 J/cm² damage threshold is *not* a CW-UV LIDT (parameter `BBO_damage_threshold_1064nm_1ns`). This task is the formal forward-pointer to closing that explicit caveat.
- [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml) — `open_extraction_items` includes "No direct CW LIDT value at 280 nm is reported"; this task is the dossier-side closure path for that item too.
