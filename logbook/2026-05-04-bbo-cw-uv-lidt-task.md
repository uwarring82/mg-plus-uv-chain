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

## First scout pass — 2026-05-05

Source basis: public publisher / index metadata and abstracts only; no publisher PDFs downloaded or committed. This is a triage pass for choosing which papers deserve steward PDF retrieval and structured extraction.

### Search boundary

- Searched first for direct `BBO` + `280 nm` + `continuous-wave` / `lifetime` / `degradation` / `Mg+` combinations.
- Then expanded to adjacent-wavelength `BBO` evidence at 266 nm and 213 nm, plus application papers from trapped-ion Mg systems.
- No direct peer-reviewed BBO-at-280-nm CW operational-lifetime paper surfaced in this shallow web scout. This is **not** an exhaustion claim; library database / citation-chaining and the institutional Q4 route remain open.

### Verified candidate triage

| Candidate | Source metadata verified | Regime | Task-E mapping | First-pass triage |
|---|---|---|---|---|
| `Kondo1998` | K. Kondo, M. Oka, H. Wada, T. Fukui, N. Umezu, K. Tatsuki, S. Kubota, "Demonstration of long-term reliability of a 266-nm, continuous-wave, frequency-quadrupled solid-state laser using β-BaB₂O₄," *Optics Letters* **23**, 195-197 (1998), DOI `10.1364/OL.23.000195`. Optica abstract reports >1000 h operation, 100 mW cw 266 nm output, 500 mW incident 532 nm on the external BBO doubler, and degradation rate proportional to UV optical field. | CW, 266 nm, BBO, operational reliability | Q2 adjacent-wavelength anchor; possible Q1/Q2 bridge for `KD-UV280-005` | **Highest payoff published source found so far.** Not 280 nm, but closest peer-reviewed CW-BBO lifetime-style anchor. Needs PDF extraction for cavity waist / UV power density / sample / surface / gas-environment details before it can support the dossier. |
| `Kubota1998` | S. Kubota et al., "Efficient 213 nm and 266 nm generations in Czochralski-grown beta-barium borates," OSA Trends in Optics and Photonics **17**, paper FC4 (1998), DOI `10.1364/DLAI.1998.FC4`. Optica abstract reports >1000 h reliability test for three Cz-grown BBO samples in 100 mW 266 nm generation; cavity-loss increase `5e-5 %/hour` at generated UV power density 260 W/cm²; pulsed 266 nm comparison at 31 MW/cm². | CW and pulsed, 266 nm, BBO, conference proceeding | Q2 adjacent-wavelength anchor; sample-to-sample reliability | **High payoff supplement to Kondo1998.** Likely same Sony / Kubota programme; may contain the missing power-density and sample details. Proceedings status should be recorded explicitly if used as `[P]` or as lower-tier evidence. |
| `Takachiho2014` | K. Takachiho, M. Yoshimura, Y. Takahashi, M. Imade, T. Sasaki, Y. Mori, "Ultraviolet laser-induced degradation of CsLiB₆O₁₀ and β-BaB₂O₄," *Optical Materials Express* **4**, 559-567 (2014), DOI `10.1364/OME.4.000559`. Abstract reports high-repetition-rate pulsed 266 nm tests; BBO shows lower UV transmittance around 10 MW/cm² and absorption increasing with time due to absorption-center formation; CLBO degradation mechanism differs. | High-repetition-rate pulsed, 266 nm, BBO/CLBO, mechanism | Q3 mechanism for `KD-UV280-011`; adjacent-wavelength caveat for `KD-UV280-005` | **High payoff for mechanism, not for CW lifetime.** Do not use as the headline CW LIDT constraint; use to separate absorption-center / colour-centre mechanism from surface or coating failure. |
| `Sudmeyer2008` | T. Südmeyer, Y. Imai, H. Masuda, N. Eguchi, M. Saito, S. Kubota, "Efficient 2nd and 4th harmonic generation of a single-frequency, continuous-wave fiber amplifier," *Optics Express* **16**, 1546-1551 (2008), DOI `10.1364/OE.16.001546`. Optica abstract reports 12.2 W cw 266 nm output from a 6-mm critically phase-matched, AR-coated Cz-grown BBO operated at 40 °C. | CW, 266 nm, BBO, high-power demonstration | Q1/Q2 headroom and power-scaling context | **Medium-high payoff.** Strong high-power BBO-operability evidence, but likely less directly a lifetime paper; extract only after Kondo/Kubota unless full text reveals long-term degradation curves. |
| `Kjaergaard2000` | N. Kjærgaard et al. application paper PDF metadata: *Applied Physics B* **71**, 207-210 (2000), DOI `10.1007/s003400000296`. The paper states a single-mode cw dye laser is frequency doubled in a 5-mm BBO crystal in an external bow-tie cavity, designed around 560 nm but used at Mg/Ca photoionization wavelengths; the Mg cooling transition at 280 nm is driven by a nearly identical laser system. | Trapped-ion application, CW near 280/285 nm, BBO | Q2 operational application; no lifetime number seen in first pass | **Medium payoff.** Useful proof that BBO-at-280-class systems were normal in Mg ion labs before Friedenauer, but not yet a lifetime source. Full paper already accessible; likely extraction would be lightweight. |
| `Hume2010Thesis` | D. B. Hume thesis, *Two-Species Ion Arrays for Quantum Logic Spectroscopy* (NIST, 2010). Public NIST PDF states Mg-Doppler visible light is frequency doubled to 280 nm with a BBO doubling cavity; the Mg-Raman source is doubled first in LBO and then in BBO to 280 nm. | Trapped-ion institutional thesis, CW 280 nm, BBO | Q2 operational corroboration; non-`[P]` | **Medium-low payoff unless it contains maintenance notes elsewhere.** Useful as an application-source breadcrumb toward NIST operational records, not a Section C primary anchor. |
| `Burd2016` | S. C. Burd et al., "VECSEL systems for the generation and manipulation of trapped magnesium ions," *Optica* **3**, 1294-1300 (2016). Optica abstract verifies externally frequency-quadrupled VECSEL operation for 279.6 / 280.4 nm Mg⁺ cooling/repumping and state manipulation. | Trapped-ion application, 280 nm Mg⁺, crystal details require full-text check | Q2 application corroboration | **Medium-low payoff for Task E.** Important modern Mg⁺ source paper, but the abstract does not expose BBO lifetime or even the conversion-crystal details; retrieve only if citation-chaining suggests supplemental operational data. |
| `Sakuma2004_CLBO213` | J. Sakuma, Y. Asakawa, T. Imahoko, M. Obara, "Generation of all-solid-state, high-power continuous-wave 213-nm light based on sum-frequency mixing in CsLiB₆O₁₀," *Optics Letters* **29**, 1096-1098 (2004), DOI `10.1364/OL.29.001096`. Abstract reports >100 mW cw 213 nm using two Brewster-cut CLBO crystals. | CW, 213 nm, CLBO | D / `KD-UV280-006` comparison; gas-environment analog for `KD-UV280-009` | **Comparison source only.** Keep on the search path because CLBO literature may explain dry-gas / heated-housing protocols, but do not use to close BBO LIDT. |
| `Nishioka2005_CLBOWater` | M. Nishioka, A. Kanoh, M. Yoshimura et al., "Improvement in UV Optical Properties of CsLiB₆O₁₀ by Reducing Water Molecules in the Crystal," *Japanese Journal of Applied Physics* **44**, L699-L700 (2005), DOI `10.1143/JJAP.44.L699`. CiNii / ResearchGate metadata reports long-term heat treatment removes water molecules, improves 266 nm transmittance, and enables three-times higher 266 nm output without bulk damage. | CLBO, water / heat-treatment, 266 nm | D / `KD-UV280-009` environmental-control analogue | **Good CLBO environment anchor.** Mechanistically adjacent to BBO surface/gas questions, but should stay in the CLBO/environment branch unless a BBO-specific water mechanism is found. |

## Second scout pass — 2026-05-05 (assistant review)

Source basis: public publisher / index metadata, abstracts, and citation-context snippets only; no publisher PDFs downloaded or committed. This pass targeted BBO-specific LIDT reviews, high-repetition-rate UV degradation studies, and trapped-ion application papers the first pass missed.

### Search boundary

- Searched for BBO-specific LIDT review / compendium papers, two-photon absorption and color-centre formation at 262–266 nm, high-repetition-rate picosecond UV sources (quasi-CW thermal-loading regime), and additional Mg⁺ trapped-ion papers citing BBO at 280 nm.
- No direct peer-reviewed BBO-at-280-nm CW operational-lifetime paper surfaced in this pass either. The negative result from the first pass stands.

### Additional verified candidate triage

| Candidate | Source metadata verified | Regime | Task-E mapping | First-pass triage |
|---|---|---|---|---|
| `Turcicova2022` | H. Turcicova, O. Novak, J. Muzik, D. Stepankova, M. Smrz, T. Mocek, "Laser induced damage threshold (LIDT) of β-barium borate (BBO) and cesium lithium borate (CLBO) – Overview," *Optics & Laser Technology* **149**, 107876 (2022), DOI `10.1016/j.optlastec.2022.107876`. Review paper collecting published LIDT data for BBO and CLBO across pulse durations; discusses intrinsic / extrinsic factors and authors' own FiHG experience. | Review; mostly pulsed LIDT, but frames CW-relevant extrinsic factors (coatings, impurities, thermal load) | Q1 LIDT bracketing; Q3 extrinsic-factor context; bibliographic hub for primary sources | **High payoff as a bibliographic hub.** Explicitly collects prior LIDT measurements; likely points to primary sources the scout passes missed. Should be extracted early to harvest its reference list for CW-adjacent studies. Not a CW lifetime anchor itself. |
| `Kumar2015` | S. Chaitanya Kumar, J. Canals Casals, J. Wei, M. Ebrahim-Zadeh, "High-power, high-repetition-rate performance characteristics of β-BaB₂O₄ for single-pass picosecond ultraviolet generation at 266 nm," *Optics Express* **23**, 28091-28103 (2015), DOI `10.1364/OE.23.028091`. Reports dynamic color-center formation from two-photon absorption in BBO at 266 nm; TPA coefficient ~3.5× lower at 200 °C than at 22 °C; long-term power stability >8 h at 2.9 W average power, 80 MHz. | High-repetition-rate picosecond (quasi-CW thermal loading), 266 nm, BBO, color-center mechanism | Q3 mechanism for `KD-UV280-011`; temperature-mitigation evidence for `KD-UV280-009`; adjacent-wavelength headroom for `KD-UV280-005` | **High payoff for mechanism and thermal mitigation.** The temperature-dependent TPA data is directly transferable to the Friedenauer-class thermal-load envelope. The 80 MHz, multi-watt average-power regime is thermally closer to CW than single-shot pulsed studies. |
| `Takahashi2010` | M. Takahashi, A. Osada, A. Dergachev, P. F. Moulton, M. Cadatal-Raduban, T. Shimizu, N. Sarukura, "Effects of Pulse Rate and Temperature on Nonlinear Absorption of Pulsed 262-nm Laser Light in β-BaB₂O₄," *Japanese Journal of Applied Physics* **49**, 080211 (2010), DOI `10.1143/JJAP.49.080211`. Investigates nonlinear absorption in BBO at 262 nm as a function of pulse rate and crystal temperature. | Pulsed, 262 nm, BBO, nonlinear absorption / color-center precursor | Q3 mechanism; adjacent-wavelength (262 nm ≈ 280 nm) | **Medium-high payoff for mechanism.** 262 nm is closer to 280 nm than 266 nm; pulse-rate dependence may reveal quasi-CW behavior. Extract to correlate with Kumar2015 temperature data. |
| `Isaenko2001` | L. I. Isaenko, A. Dergachev, D. G. Machonkin, D. N. Nikogosyan, "Anisotropy of two-photon absorption in BBO at 264 nm," *Optics Communications* **198**, 433-438 (2001). | Pulsed, 264 nm, BBO, two-photon absorption anisotropy | Q3 mechanism | **Medium payoff for mechanism.** Early TPA characterization; useful for validating later Kumar2015 / Takahashi2010 numbers. |
| `Hemmerling2011` | B. Hemmerling, F. Gebert, Y. Wan, T. K. Cubel Liebisch, N. Akerman, M. Carreras, D. Cianchetti, S. Kraft, J. P. Paetzold, S. R. de Echaniz, U. Warring, T. W. Koerber, H. Haeffner, F. Schmidt-Kaler, "A single laser system for ground-state cooling of ²⁵Mg⁺," *Applied Physics B* **104**, 583-590 (2011), DOI `10.1007/s00340-011-4472-9`. Reports a 280 nm cooling laser for ²⁵Mg⁺ using BBO second-harmonic generation. | Trapped-ion application, CW 280 nm, BBO | Q2/Q4 operational corroboration | **Medium payoff.** Directly relevant to the Friedenauer-class architecture; may contain operational notes or reference institutional maintenance records. |
| `Nagashima2009` | T. Nagashima, N. Seko, K. Tatsuki, H. Tonooka, J. Murata, Y. Wada, "Thousand hours operations of CW DUV laser light…" (full title requires verification), *Applied Optics* or *Applied Physics B* (2009). Cited in recent 213-nm generation papers as the CW DUV long-term operation reference. | CW, DUV (likely 266 nm or 213 nm), operational lifetime | Q2 adjacent-wavelength anchor | **Medium-high payoff, pending title verification.** The "thousand hours" framing matches the Q2 operational-lifetime need. Steward should verify exact bibliographic details and retrieve. |
| `Deyra2015` | L. Deyra, A. Maillard, R. Maillard, D. Sangla, F. Salin, F. Balembois, A. E. Kokh, P. Georges, "Impact of BaB₂O₄ growth method on frequency conversion to the deep ultra-violet," *Solid State Sciences* (2015), DOI `10.1016/j.solidstatesciences.2015.10.019`. Compares flux-grown (TSSG) and Czochralski-grown BBO for deep-UV FHG; CZ-grown yields higher conversion efficiency under high average power. | Growth-method comparison, deep-UV, high average power | Q3 extrinsic factor (crystal quality); `KD-UV280-006` alternative-crystal context | **Medium payoff.** Supports the Kondo / Kubota Cz-grown BBO finding; may explain sample-to-sample lifetime variation. |
| `Bhar2004` | G. C. Bhar, A. K. Chaudhary, P. Kumbhakar, A. M. Rudra, S. C. Sabarwal, "A comparative study of laser-induced surface damage thresholds in BBO crystals and effect of impurities," *Optical Materials* **27**, 119-123 (2004), DOI `10.1016/j.optmat.2004.02.027`. Single-shot and multiple-shot surface damage thresholds at 1064 and 532 nm; SEM-EDXA impurity correlation. | Pulsed, 1064/532 nm, surface damage, impurities | Q1 distant bracket; Q3 extrinsic (impurity) factor | **Low-medium payoff for Task E.** Wavelength is far from 280 nm, but the impurity-damage correlation is transferable to UV surface degradation. Retrieve only if Turcicova2022 points to it as significant. |

### Updated priority after second scout pass

The priority list from the first scout pass is superseded as follows:

1. Retrieve / extract `Kondo1998` first, with `Kubota1998` as the companion.
2. Retrieve / extract `Turcicova2022` in parallel with step 1. Its reference list is likely to surface additional primary sources (including possibly CW-specific studies) that the scout passes missed.
3. Extract `Kumar2015` and `Takahashi2010` for mechanism (`KD-UV280-011`) and temperature-mitigation evidence (`KD-UV280-009`) once the CW anchor is secured.
4. Verify and retrieve `Nagashima2009` if the full title confirms CW DUV BBO operation; it may provide the missing >1000 h operational narrative.
5. Extract `Hemmerling2011` as a trapped-ion breadcrumb toward Q4 institutional records, and for any operational notes on the 280 nm BBO system.
6. Keep `Bhar2004`, `Isaenko2001`, and `Deyra2015` as lower-priority mechanistic / extrinsic context; extract only if steps 1–5 reveal gaps they can fill.
7. Start the Q4 institutional query in parallel; the expanded published literature still does not replace the value of MPQ Garching / AG Schätz Freiburg operating records at exactly 280 nm.

## Third scout pass — 2026-05-13 (filing of newly-arrived publisher PDFs)

Source basis: publisher / preprint PDFs newly arrived under `downloads/literature/task-e/` and inspected on 2026-05-13 (first-page and abstract / §1-2 read; no full extraction). The downloads batch confirms a number of previously-scaffolded candidates (Kondo1998, Kubota1998, Hemmerling2011, Kumar2015, Turcicova2022, Eckardt1990, Tamosauskas2018, Eimerl1987, Friedenauer2006, Hume2010, Burd2016, Kjaergaard2000, Brown2019) and **adds three new entries** plus one **scaffold authorship correction**.

### Bibliographic confirmations and additions

| Citation key | Filename in downloads batch | Folder status before 2026-05-13 | Folder status after 2026-05-13 |
|---|---|---|---|
| `Kondo1998` | `Kondo1998_OpticsLetters_user.pdf` (+ `_official_probe.html`) | DRAFT | unchanged |
| `Kubota1998` | `Kubota1998_OSAProceedings_user_scan.pdf` (+ `_official_probe.html`) | DRAFT | unchanged |
| `Hemmerling2011` | `Hemmerling2011_arxiv_open.pdf` | DRAFT | unchanged |
| `Kumar2015` | `Kumar2015_UPCommons_open.pdf` (+ Optica probe HTML) | DRAFT | unchanged |
| `Turcicova2022` | `Turcicova2022_Elsevier_user.pdf` | DRAFT | unchanged |
| `Eckardt1990` | `Eckardt1990_IEEE_user.pdf` | DRAFT | unchanged |
| `Tamosauskas2018` | `Tamosauskas2018_OME_user.pdf` | DRAFT | unchanged |
| `Eimerl1987` | `Eimerl1987_AIP_user.pdf` | DRAFT | unchanged |
| `Friedenauer2006` | `Friedenauer2006_Springer_user.pdf` | DRAFT (existing) | unchanged |
| `Hume2010` | `Hume2010_NIST_open.pdf` | existing scaffold | unchanged |
| `Burd2016` | `Burd2016_NIST_open.pdf` | existing scaffold | unchanged |
| `Kjaergaard2000` | `Kjaergaard2000_Aarhus_open.pdf` | existing scaffold | unchanged |
| `Brown2019` | `Brown2019_SciRep_open.pdf` | DRAFT (existing) | unchanged |
| **`Burkley2021`** | `vonMilczewski2021_arxiv_open.pdf` (misnomer; see correction below) | SCAFFOLD under wrong internal author | SCAFFOLD with corrected citation_key / citation strings |
| **`Hannig2018`** *(new)* | `013106_1_online.pdf` | n/a | SCAFFOLD created |
| **`Shaw2021`** *(new)* | `oe-29-23-37140.pdf` | n/a | SCAFFOLD created |
| **`Kraus2022`** *(new)* | `oe-30-25-44992.pdf` | n/a | SCAFFOLD created |

Two of the downloads batch are probe-only HTML captures with no associated PDF (`Kumar2015_Optica_captcha_probe.html`, `Takachiho2014_Optica_captcha_probe.html`) and one is a metadata-probe page for Kubota1998 / Kondo1998 (the actual PDFs are filed alongside). The Takachiho 2014 paper remains a published `[P]`-tier candidate per the second scout pass priority list but no PDF was retrieved in this batch.

### Scaffold authorship correction: `vonMilczewski2021` → `Burkley2021`

The 2026-05-06 scaffold under [`data/literature/Burkley2021/`](../data/literature/Burkley2021/) attributed the arXiv:`2105.14977` paper to a first author "von Milczewski" based on a public-metadata guess made before the PDF was in hand. Direct read of the PDF on 2026-05-13 confirms the correct first author is **Z. (Zakary) Burkley** (ETH Zürich), with co-authors L. de Sousa Borges, B. Ohayon, A. Golovozin (Lebedev), J. Zhang, and P. Crivelli. There is no author named "von Milczewski" on the paper. The folder name `Burkley2021/` was correct from creation; the internal `citation_key`, `citation`, and notes-header strings were the locus of the error and have been corrected in this pass. The download filename `vonMilczewski2021_arxiv_open.pdf` is retained in the gitignored `downloads/` tree as a historical artefact and is **not** renamed (renaming would break the chain-of-provenance trail back to the 2026-05-06 scout pass commit). The corresponding `cross_check_notes` entry `scout_pass_authorship_correction` is now logged in [`data/literature/Burkley2021/extracted.yaml`](../data/literature/Burkley2021/extracted.yaml), parallel to the matching note in [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml).

### Newly-added candidate triage

| Candidate | Source verified | Regime | Task-E mapping | Triage |
|---|---|---|---|---|
| `Hannig2018` | S. Hannig, J. Mielke, J. A. Fenske, M. Misera, N. Beev, C. Ospelkaus, P. O. Schmidt, "A highly stable monolithic enhancement cavity for second harmonic generation in the ultraviolet," *Review of Scientific Instruments* **89**, 013106 (2018), DOI `10.1063/1.5005515`. Brewster-cut BBO bow-tie cavity for 313 nm; **130 h uninterrupted operation without decay in output power**. Vibration robustness: <10 % in-lock variation at 1 g; 30 min at 3 g_rms. Open-source STEMlab 125-14 digital PI lock. Published Creative Commons CC-BY 4.0. | CW, 313 nm, Brewster-cut BBO, monolithic bow-tie | Q2 upper-wavelength operational-lifetime anchor for BBO cavity CW operation; combined with Kondo1998 / Kubota1998 at 266 nm, brackets the 280 nm operating point from above and below in wavelength | **High payoff.** One of the cleanest published examples of "no decay over multi-day BBO-cavity CW operation in the UV". PTB-Schmidt-group lineage, same as Hemmerling2011 / Kraus2022. Adjacent-wavelength caveat applies (313 nm sits deeper into the BBO transparency window than 280 nm). Next pass: full extraction of cavity geometry, BBO dimensions, intracavity power, gas environment. |
| `Shaw2021` | J. C. Shaw, S. Hannig, D. J. McCarron, "Stable 2 W continuous-wave 261.5 nm laser for cooling and trapping aluminum monochloride," *Optics Express* **29**, 37140-37155 (2021), DOI `10.1364/OE.441741`. LBO + CLBO cascaded bow-tie cavities (1046 nm ECDL + IPG fibre amp → 523 nm → 261.5 nm); **2.75 W peak / 2 W steady-state CW at 261.5 nm over 13 h**; "largely unexplored high-intensity regime in CLBO for continuous-wave DUV light" (abstract verbatim). Monolithic aluminium-housing bow-tie from Agile Optic GmbH (Hannig). Optica Open Access. | CW, 261.5 nm, CLBO + LBO cascade, high-intensity DUV | D (CLBO comparison literature) bracket; Q2 short-duration high-power CW DUV anchor on CLBO | **High payoff for the CLBO arm.** The 261.5 nm operating point and 2 W CW power scaling exceed prior published CLBO CW DUV anchors; directly relevant to `KD-UV280-006`. Next pass: full extraction of LBO + CLBO crystal specs, intracavity intensities, gas environment, output-power time trace. |
| `Kraus2022` | B. Kraus, F. Dawel, S. Hannig, J. Kramer, C. Nauk, P. O. Schmidt, "Phase-stabilized UV light at 267 nm through twofold second harmonic generation," *Optics Express* **30**, 44992-45003 (2022), DOI `10.1364/OE.471450`. Twofold *single-pass* SHG: 1069.6 nm fibre laser → 10 mm PPLN waveguide (HC Photonics) → 534.8 nm → 50 mm DKDP non-critical Type-I at ~100 °C → **267.4 nm at >50 µW with fractional frequency instability <5×10⁻¹⁷ at 1 s** (electronics-limited 1×10⁻¹⁸ at 1 s). Optica Open Access. | CW, 267.4 nm, DKDP + PPLN waveguide, no cavities | Architectural-alternative datapoint for `KD-UV280-006` and the alternative-topology slate. Not a Task-E LIDT or lifetime anchor. | **Medium payoff for Task E specifically; high payoff for the alternative-crystal / alternative-topology dossier branch.** PTB-Schmidt-group lineage with Hannig as bridging author. DKDP at 267 nm is structurally distinct from both BBO and CLBO; the trade-off is no walk-off and no cavity required, at the cost of ~10⁻⁴× lower output power than Friedenauer-class systems. Next pass: full extraction of DKDP operating conditions, PPLN waveguide specs, phase-stability method. |

### Cross-paper observation: PTB-Schmidt-group hardware lineage

The three newly-filed papers (`Hannig2018`, `Shaw2021`, `Kraus2022`) plus the previously-filed `Hemmerling2011` together span four distinct UV-stage architectures all attached to the same institutional lineage:

| Paper | Year | Stage architecture | Crystal | Wavelength | Headline result |
|---|---|---|---|---|---|
| Hemmerling2011 | 2011 | bow-tie cavity | Brewster-cut BBO | 280 nm | 60 mW UV; CW UV-induced surface damage on fused silica at 32-64 W/cm² over hours |
| Hannig2018 | 2018 | monolithic bow-tie cavity | Brewster-cut BBO | 313 nm | 130 h uninterrupted operation; vibration-robust |
| Shaw2021 | 2021 | LBO + CLBO cascaded monolithic bow-tie cavities | CLBO | 261.5 nm | 2 W steady-state over 13 h; "largely unexplored high-intensity regime" |
| Kraus2022 | 2022 | PPLN waveguide + DKDP single-pass | DKDP (non-critical Type-I) | 267.4 nm | <5×10⁻¹⁷ phase stability at 1 s |

Co-authors S. Hannig (PTB / Agile Optic GmbH) and P. O. Schmidt (PTB) appear across multiple combinations. The institutional Q4 record from the Schmidt group (per the task-E acceptance criterion #3) likely covers all four of these architectures, not only the Friedenauer-style BBO route; this widens the scope of the institutional-`[I]`-tier extraction window when the steward chooses to pursue it.

### Updated priority after third scout pass

The previous priority list is augmented (not replaced) with the new candidates:

1. *(unchanged)* Retrieve / extract `Kondo1998` and `Kubota1998` (now in hand under `downloads/literature/task-e/`).
2. *(unchanged)* Extract `Turcicova2022` (in hand) for its bibliographic-hub reference list.
3. *(unchanged)* Extract `Kumar2015` and `Takahashi2010` for mechanism / temperature-mitigation evidence.
4. **Extract `Hannig2018`** in parallel with step 1 — direct CW-BBO operational-lifetime anchor at 313 nm; the 130 h figure is one of the cleanest available.
5. **Extract `Shaw2021`** as the CLBO arm anchor at 261.5 nm; feeds `KD-UV280-006` and the alternative-crystal branch.
6. **Extract `Burkley2021`** (now with corrected scaffold) for the coating-and-gas-environment branch (`KD-UV280-008` / `-009` / `-012`).
7. *(unchanged)* Extract `Hemmerling2011` — already DRAFT.
8. **Extract `Kraus2022`** as architectural-alternative datapoint for the alternative-topology slate; lower priority for Task E itself.
9. *(unchanged)* Verify and retrieve `Nagashima2009`.
10. *(unchanged)* Keep `Bhar2004`, `Isaenko2001`, `Deyra2015` as lower-priority mechanistic / extrinsic context.
11. *(unchanged)* Start the Q4 institutional query, now widened to cover the four PTB-Schmidt-group UV-stage architectures identified above.

## Acceptance criteria for closing this task

This logbook entry is closed when **all** of the following are true:

1. At least **one** peer-reviewed `[P]` source is cited in `KD-UV280-005 Section C` for either Q1 (CW intrinsic threshold at 280 nm) or Q2 (operational-lifetime curve under realistic conditions). If no peer-reviewed source exists for Q1/Q2 specifically at 280 nm, the entry uses adjacent-wavelength `[P]` sources (e.g. 213, 266 nm) with explicit extrapolation rationale.
2. If adjacent-wavelength evidence is used because no direct 280 nm peer-reviewed source is found, the dossier explicitly states the search boundary and the negative result (databases / query family / date), so the 266 nm or 213 nm extrapolation is visible rather than silently promoted to a 280 nm measurement.
3. The institutional `[I]` record from MPQ Garching / AG Schätz Freiburg is either (a) extracted into a dedicated `data/literature/AG-Schatz-internal/` folder following the conventions in `data/literature/<key>/notes.md`, or (b) explicitly deferred with a documented reason. If included, the dossier entry classification per the [Section C `[I]`-only rule](../docs/KD-2026-XXX-uv-280nm.md) is Underdetermined unless external corroboration is found.
4. `KD-UV280-005` Section C "TODO: cite peer-reviewed CW LIDT measurements at 280 nm" bullet is replaced with the populated constraint. The `KD-UV280-009` Section C entry on gas-environment dependence either gains a populated `[P:]` constraint or pings back to this logbook entry as the deferred task.
5. The §5 Phase 1 evidence-table BBO row's "CW LIDT @ 280 nm (W/cm²)" cell either tightens (if A/B/C above produce a value) or splits into "intrinsic / operational lifetime" with separate citations.
6. `KD-UV280-011` is upgraded from SCAFFOLD to POPULATING if mechanism-level literature (Q3) is captured.

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