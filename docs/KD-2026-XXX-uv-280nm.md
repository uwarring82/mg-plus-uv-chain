# Kompass-Dossier: CW UV Source Architectures and Crystal/Coating Evidence at 280 nm

**Document:** `docs/KD-2026-XXX-uv-280nm.md`
**Version:** v0.2-populating
**Date opened:** 2026-05-01
**Steward:** Ulrich Warring (Albert-Ludwigs-Universität Freiburg, AG Schätz)
**Status:** POPULATING — scaffold defined; KD-UV280-013 populated from Friedenauer2006; other citation slots pending Phase 1 literature work.
**Schema:** Kompass-Dossier, Section A/B/C with §8 outcome classification (Resolved / Operationally bounded / Underdetermined).
**Charter reference:** [CHARTER §5 Phase 1 row](../CHARTER.md), [§4 architecture families](../CHARTER.md), [§8 open boundaries](../CHARTER.md).

---

## Endorsement Marker

Local candidate framework. This dossier collects published evidence for design-space coordinates; it does not endorse specific values without independent verification per [endorsement.md](../endorsement.md). Per CHARTER §1.5, all numerical extractions feed Level 2 source specifications via the Level 0 → Level 1 → Level 2 derivation chain.

External coastlines cited as constraints, not replicated:
- Boyd–Kleinman theory (J. Appl. Phys. **39**, 3597, 1968)
- Crystal manufacturer datasheets and SNLO (Sandia)
- Peer-reviewed laser physics literature

---

## Scope

**Domain:** CW UV laser source architectures producing ≥ 500 mW at 280 nm for trapped ²⁵Mg⁺ work; nonlinear-crystal candidates and their UV-induced degradation; mirror-coating performance and degradation at 280 nm.

**Boundary conditions:**
- CW operation only (pulsed / fs-comb sources are out of scope per CHARTER §3 non-goals).
- All-solid-state architectures only (no dye, no flashlamp-pumped solid-state).
- Wavelength range: 1064–1118 nm fundamental and harmonics; 280 nm UV. Sum-frequency partner wavelengths (e.g. 376 nm, 559 nm, 591 nm) included as needed.
- Crystal scope: BBO, CLBO, LBO at minimum; other UV nonlinear crystals admitted if literature warrants.
- Coating scope: HR and OC coatings in the UV; AR coatings on UV-passing optics.

**Selection mode:** REQUEST-driven (each entry corresponds to a Charter-flagged literature gap).

**Source requirements:**
- Every Section C must cite ≥ 1 peer-reviewed primary [P] source where available.
- Manufacturer datasheets are admissible as secondary [S] sources but cannot be the sole basis for a Section C constraint.
- Where institutional record (e.g. UV-degradation working notes) is the only source, it is flagged as [I] and the entry is classified Underdetermined unless external corroboration is found.
- Vendor / batch sensitivity must be captured per CHARTER §5 Phase 1 row.

**Per CHARTER §5.1 anti-seeding clause:** This dossier is *literature collection*, not architecture-family-specific simulation. It is unblocked pre-G1 and may inform Phase 0.5 tightening, Phase 2 measurement protocols, and Phase 4 scoring without itself constituting a candidate architecture commitment.

---

## Cross-references

| If you want… | Look at… |
|---|---|
| Charter §4 architecture families | Entries KD-UV280-001 through -004 |
| Charter §5 Phase 1 crystal/coating evidence table | Section "Crystal and coating evidence table" below |
| Charter §8.1 14-GHz unlockable domain | Entry KD-UV280-010 |
| Charter §8.2/§8.4 BBO degradation, gas-environment dependence | Entry KD-UV280-011 |
| Charter §8.6 mirror coating UV degradation | Entry KD-UV280-012 |
| Friedenauer 2006 baseline parameter extraction | Entry KD-UV280-013 |
| Phase-locked dual-source phase-noise literature | Entry KD-UV280-014 |

---

## Entry Index

| Entry ID | Title | Charter §ref | Outcome class | Status |
|---|---|---|---|---|
| KD-UV280-001 | Quadrupling architecture (Friedenauer baseline family) | §4.1 | TBD | SCAFFOLD |
| KD-UV280-002 | Sum-frequency mixing architectures | §4.2 | TBD | SCAFFOLD |
| KD-UV280-003 | Hybrid architectures (dual-source / OPA-based) | §4.3 | TBD | SCAFFOLD |
| KD-UV280-004 | Direct deep-UV sources (AlGaN diodes, deep-UV VECSEL) | §4.4 | TBD | SCAFFOLD |
| KD-UV280-005 | BBO at 280 nm — phase-matching, walk-off, damage threshold | §5 P1, §8.4 | TBD | SCAFFOLD |
| KD-UV280-006 | CLBO at 280 nm — competing crystal characterisation | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-007 | LBO at relevant SHG/SFG stages | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-008 | UV mirror coatings — HR, OC, AR specifications and degradation | §5 P1, §8.6 | TBD | SCAFFOLD |
| KD-UV280-009 | Hygroscopic and environmental constraints (BBO, CLBO) | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-010 | 14-GHz unlockable resonance domain — published evidence | §8.1 | TBD | SCAFFOLD |
| KD-UV280-011 | UV-induced BBO degradation and gas-environment dependence | §8.2, §8.4 | TBD | SCAFFOLD |
| KD-UV280-012 | UV mirror coating degradation under CW exposure | §8.6 | TBD | SCAFFOLD |
| KD-UV280-013 | Friedenauer 2006 baseline parameter extraction | §1 baseline | Resolved | DRAFT |
| KD-UV280-014 | Phase-locked dual-source phase-noise literature | §4 (counter-obs.) | TBD | SCAFFOLD |
| KD-UV280-015 | Pump source options — Yb-fibre vs. VECSEL near 1118 nm | §3 open | TBD | SCAFFOLD |

---

## Crystal and coating evidence table

Per CHARTER §5 Phase 1 row (v0.8 Architect-stress-test recommendation): a dedicated table covering BBO, CLBO, LBO-relevant stages, coating degradation modes, hygroscopic and environmental constraints, and vendor / batch sensitivity. The table is the Phase 1 deliverable's central artefact.

| Crystal / coating | SHG/SFG stage | d_eff (pm/V) | Phase-match type | Walk-off ρ (mrad) | CW LIDT @ 280 nm (W/cm²) | Hygroscopic? | Vendor/batch sensitivity | Notes / citations |
|---|---|---|---|---|---|---|---|---|
| BBO | 559 → 280 (SHG) | TODO | TODO (Type-I) | TODO | TODO | mild surface | Same-vendor batch/cut sensitivity reported for the 14-GHz unlockable domain; all tested crystals came from Crystals of Siberia. | [P:Friedenauer2006] §4; full material values still TODO |
| BBO | 1118+376 → 280 (SFG) | TODO | TODO | TODO | TODO | mild surface | TODO | TODO: cite |
| CLBO | 559 → 280 (SHG) | TODO | TODO | TODO | TODO | strongly hygroscopic | TODO — known temperature/humidity sensitivity | TODO: cite |
| CLBO | 1064+376 → 280 (SFG) | TODO | TODO | TODO | TODO | strongly hygroscopic | TODO | TODO: cite |
| LBO | 1118 → 559 (SHG, intermediate) | TODO | TODO | TODO | n/a (visible stage) | low | TODO | TODO: cite |
| HR coating @ 280 nm | UV cavity mirror | n/a | n/a | n/a | TODO | TODO | TODO — vendor variability is the §8.6 partition concern | TODO: cite |
| OC coating @ 280 nm | UV cavity output | n/a | n/a | n/a | TODO | TODO | TODO | TODO: cite |
| AR coating @ 280 nm | UV-passing optics | n/a | n/a | n/a | TODO | TODO | TODO | TODO: cite |

*Table populated incrementally during Phase 1 work. Each cell gets a citation when the value is added; cells lacking citation are not admitted as Phase 4 inputs.*

---

## Ledger Entries

Each entry follows the Section A / B / C structure:
- **Section A** — claim or design-space coordinate the entry establishes.
- **Section B** — predicted observations / what would be required to confirm or reject.
- **Section C** — constraints from cited literature (each constraint with citation key).

Each entry closes with an **Outcome classification** per CHARTER §8 preamble: **Resolved** / **Operationally bounded** / **Underdetermined** / **TBD** (until evidence is collected).

---

### KD-UV280-001 — Quadrupling architecture (Friedenauer baseline family)

**Charter ref:** §4.1.
**Architecture family:** Single-source 1118 → 559 → 280 (or alternative pump → SHG → SHG).

#### Section A — Claim
Single-source quadrupling is a viable CW route to ≥ 500 mW at 280 nm using fibre-laser or VECSEL pumps and intra-cavity SHG at both stages.

#### Section B — Predictions
- ≥ 1 published demonstration of CW quadrupling delivering ≥ 200 mW at 280 nm in a comparable apparatus.
- Evidence that the second SHG (559 → 280) is the binding stage for thermal load and degradation, not the first (1118 → 559).
- Pump-source candidates with sufficient brightness and spectral purity at 1118 nm.

#### Section C — Constraints
TODO: cite Friedenauer 2006; cite alternative quadrupling demonstrations; cite VECSEL-pumped quadrupling literature.

**Outcome classification:** TBD pending Phase 1 literature collection.

---

### KD-UV280-002 — Sum-frequency mixing architectures

**Charter ref:** §4.2.
**Architecture family:** Dual-source SFG to 280 nm. Variants: 1064+376 → 280, 532+591 → 280, others.

#### Section A — Claim
Dual-source SFG architectures can reach ≥ 500 mW at 280 nm with potentially lower per-stage UV stress than quadrupling, at the cost of phase-coherence engineering between the two sources.

#### Section B — Predictions
- Published CW SFG demonstrations at 280 nm or comparable UV with ≥ 100 mW output.
- Quantification of relative phase-noise floor with state-of-the-art OPLLs at the relevant wavelengths.
- Comparison of intra-cavity intensity at the SFG stage vs. quadrupling second-SHG stage.

#### Section C — Constraints
TODO: cite SFG-to-UV demonstrations; cite OPLL phase-noise demonstrations at relevant power and wavelength.

**Outcome classification:** TBD.

---

### KD-UV280-003 — Hybrid architectures (dual-source / OPA-based)

**Charter ref:** §4.3.

#### Section A — Claim
Hybrid architectures combining a doubled fibre/VECSEL source with a mixed/OPA arm offer flexibility in detuning agility and per-stage UV stress; their adoption is bounded by combined complexity and phase-coherence robustness.

#### Section B — Predictions
- Examples of doubled-OPA or doubled+SFG hybrid CW UV sources.
- Documented modular-upgrade benefits vs. integrated quadrupling.

#### Section C — Constraints
TODO: cite hybrid CW UV-source demonstrations.

**Outcome classification:** TBD.

---

### KD-UV280-004 — Direct deep-UV sources (AlGaN diodes, deep-UV VECSEL)

**Charter ref:** §4.4.

#### Section A — Claim
Direct CW deep-UV semiconductor sources do not yet meet the §2 specifications (≥ 500 mW, single-frequency, narrow linewidth, Raman-mode suitability) at 280 nm; treated as literature-only at v1.0 per CHARTER §4.

#### Section B — Predictions
- State-of-the-art AlGaN diode CW power at ≤ 285 nm should be < 100 mW with multi-mode behaviour.
- Deep-UV VECSEL development should not yet be at the > 500 mW CW single-frequency point at 280 nm.
- Either source type would need substantial line-narrowing engineering for Raman-mode use.

#### Section C — Constraints
TODO: cite recent AlGaN UV diode performance survey; cite deep-UV VECSEL development status.

**Outcome classification:** TBD — expected to close as Underdetermined or Operationally bounded for v1.0; revisit in v1.x if technology maturity changes.

---

### KD-UV280-005 — BBO at 280 nm — phase-matching, walk-off, damage threshold

**Charter ref:** §5 Phase 1, §8.4.

#### Section A — Claim
BBO is the established UV-stage crystal at 280 nm for CW SHG and SFG, with well-characterised phase-matching but degradation behaviour that depends on intensity, gas environment, and (per CHARTER §8.4) factors beyond the intrinsic crystal threshold.

#### Section B — Predictions
- Published Type-I phase-matching angle, d_eff, and walk-off angle at 280 nm are well-determined.
- CW LIDT at 280 nm is reported to depend on gas environment, exposure history, and surface preparation, not just intrinsic bulk threshold.
- Vendor/batch variability is documented in the literature and institutional record.

#### Section C — Constraints
TODO: cite Boyd–Kleinman parameters for BBO; cite SNLO data; cite published CW LIDT measurements; cite Friedenauer 2006 §4 batch-variability observation.

**Outcome classification:** TBD.

---

### KD-UV280-006 — CLBO at 280 nm — competing crystal characterisation

**Charter ref:** §5 Phase 1.

#### Section A — Claim
CLBO is a competitive crystal candidate at 280 nm with potentially different damage and walk-off behaviour than BBO, but is strongly hygroscopic and requires environmental control.

#### Section B — Predictions
- Higher d_eff than BBO at comparable wavelengths in some configurations.
- Documented damage behaviour distinct from BBO under CW UV exposure.
- Published environmental-control protocols (heated housing, dry-gas atmosphere) are required for stable operation.

#### Section C — Constraints
TODO: cite CLBO crystal data sources; cite environmental-control protocol references; cite UV CW degradation studies.

**Outcome classification:** TBD.

---

### KD-UV280-007 — LBO at relevant SHG/SFG stages

**Charter ref:** §5 Phase 1.

#### Section A — Claim
LBO is the standard intermediate-stage crystal for 1064/1118 → 532/559 SHG; it has low UV stress at this wavelength and is not the binding crystal for the design.

#### Section B — Predictions
- Published d_eff, phase-match type, and walk-off at 1064 → 532 (and 1118 → 559) are well-determined.
- LBO does not show the same UV degradation modes as BBO/CLBO at 280 nm because the intermediate wavelength is in the visible.

#### Section C — Constraints
TODO: cite SNLO LBO parameters; cite intermediate-stage SHG demonstrations.

**Outcome classification:** TBD.

---

### KD-UV280-008 — UV mirror coatings — HR, OC, AR specifications and degradation

**Charter ref:** §5 Phase 1, §8.6.

#### Section A — Claim
UV mirror coatings at 280 nm degrade under CW exposure (reflectivity drift, scatter-loss increase, absorption-induced thermal lensing) on timescales relevant to source stability budgets, and contribute to the §6.5 degradation budget independently of the crystal.

#### Section B — Predictions
- Published vendor specifications report reflectivity > 99.9 % HR and < 0.5 % AR at 280 nm.
- CW degradation under sustained UV flux is documented in the literature with timescales of hundreds to thousands of hours depending on coating composition.
- Vendor/batch variability is significant and is the basis for the §8.6 partition requirement.

#### Section C — Constraints
TODO: cite vendor coating specifications; cite published UV-coating degradation studies; cite Layertec/Laseroptik/EKSMA technical notes.

**Outcome classification:** TBD.

---

### KD-UV280-009 — Hygroscopic and environmental constraints (BBO, CLBO)

**Charter ref:** §5 Phase 1.

#### Section A — Claim
BBO has mild surface hygroscopic behaviour requiring dry-gas housing for long-term stability; CLBO is strongly hygroscopic and requires heated dry-gas environment for operation.

#### Section B — Predictions
- Documented surface-degradation protocols for BBO under ambient-humidity exposure.
- Documented heated-housing requirements for CLBO with operating temperature ≥ 100 °C and dry-gas purge.

#### Section C — Constraints
TODO: cite BBO surface-degradation literature; cite CLBO environmental-control papers; cite manufacturer recommendations.

**Outcome classification:** TBD.

---

### KD-UV280-010 — 14-GHz unlockable resonance domain — published evidence

**Charter ref:** §8.1.

#### Section A — Claim
The 14-GHz unlockable resonance domain reported in Friedenauer 2006 §4 is not, at v1.0, mechanistically attributed; published evidence in the broader CW SHG / cavity-locking literature should be searched for similar reports and candidate mechanisms.

#### Section B — Predictions
- Friedenauer 2006 §4 reports the domain across multiple crystals from one manufacturer.
- Subsequent literature may report similar phenomena in other UV cavities; if so, the mechanism should be in the citation chain.
- Candidate mechanisms (per CHARTER §8.1 discriminant set): refractive-index temperature drift, birefringence coupling, photochemical / colour-centre formation, impurity / growth defect.

#### Section C — Constraints
TODO: cite Friedenauer 2006 §4 in detail; cite other CW UV cavity reports of similar locking instabilities; cite candidate-mechanism papers (BBO colour-centre, photorefractive effects, polarisation-coupling).

**Outcome classification:** TBD — Phase 2 G1 attribution is the binding closure; this entry collects the literature *prior* to attribution.

---

### KD-UV280-011 — UV-induced BBO degradation and gas-environment dependence

**Charter ref:** §8.2, §8.4.

#### Section A — Claim
BBO under CW UV exposure exhibits degradation (output power loss, mode-quality distortion, phase-noise increase, polarisation drift) whose rate depends on gas environment (N₂ vs O₂ vs dry air) and on cumulative exposure history.

#### Section B — Predictions
- Published CW degradation studies in BBO at 280 nm or comparable UV.
- Documented gas-environment dependence (with at least one paper comparing N₂, O₂, and dry-air protocols).
- Reported degradation timescales of hundreds to thousands of hours under realistic CW flux.

#### Section C — Constraints
TODO: cite published BBO CW UV degradation studies; cite gas-environment dependence references; cite institutional UV-degradation working notes 2026-04 as [I].

**Outcome classification:** TBD.

---

### KD-UV280-012 — UV mirror coating degradation under CW exposure

**Charter ref:** §8.6.

#### Section A — Claim
UV mirror coatings degrade under CW exposure independently of crystal degradation; the resulting reflectivity drift and absorption-induced thermal lensing shift the cavity impedance match and contribute to §6.5 degradation budget.

#### Section B — Predictions
- Published swap-test or witness-mirror studies isolating coating contribution.
- Vendor-batch variability quantification.
- Documented timescales for coating reflectivity drift under representative CW flux.

#### Section C — Constraints
TODO: cite coating-degradation studies; cite swap-test or witness-mirror methodology papers; cite institutional coating records as [I] where applicable.

**Outcome classification:** TBD — couples to §8.6 partition method validation in Phase 2.

---

### KD-UV280-013 — Friedenauer 2006 baseline parameter extraction

**Charter ref:** §1 baseline, §2 Friedenauer column.

#### Section A — Claim
The Friedenauer 2006 architecture (1118 → 559 → 280, source-side 275 mW, 15.2 % overall efficiency, 14-GHz unlockable domain) is the v1.0 reference baseline; this entry extracts the parameters into a structured form.

#### Section B — Predictions
- The paper reports source-side power, conversion efficiency, drift envelope, polarisation-drift behaviour, and the 14-GHz anomaly.
- Crystals, coating specs, and pump details are documented and extractable into `data/literature/Friedenauer2006/extracted.yaml` per the `data/README.md` schema.

#### Section C — Constraints
- [P:Friedenauer2006] Architecture route: commercial Yb fibre laser at 1118 nm followed by two external SHG ring cavities, first LBO for 1118 → 559 nm and then Brewster-cut BBO for 559 → near 280 nm. Structured extraction: [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml).
- [P:Friedenauer2006] Fundamental source: 2 W at 1118 nm, linewidth < 200 kHz; the same source also emits 1.2 W broadband ASE peaked between 1060 nm and 1100 nm. After polarization control and an optical isolator, the reported incoupling power to the first SHG cavity is 1.8 W.
- [P:Friedenauer2006] First SHG stage: 18-mm type-I alpha-cut LBO crystal, noncritical phase matching; calculated phase-match temperature 89 °C, observed optimum 94 °C, oven control within 20 mK. Reported stable 559-nm output is 950 mW, with >52.7% cavity conversion efficiency.
- [P:Friedenauer2006] Second SHG stage: Brewster-cut BBO crystal of size 4 mm × 4 mm × 10 mm, heated to about 50 °C to protect polished hygroscopic surfaces. The paper reports 275 mW UV output near 280 nm and 28.9% conversion efficiency for this stage.
- [P:Friedenauer2006] Overall output and efficiency: 275 mW near 280 nm, corresponding to 15.2% overall conversion efficiency from 1118 nm to near 280 nm.
- [P:Friedenauer2006] Cavity technical parameters are tabulated in the paper: LBO/BBO cavity lengths 400 mm / 470 mm, focusing-mirror separations 62 mm / 59.4 mm, full folding angles 10° / 27.4°, input-coupler reflectivities 97.5% / 98.4%, HR mirror reflectivities >99.98% / >99.93%, and output-coupler fundamental reflectivities >99.9% / >99.8%.
- [P:Friedenauer2006] 14-GHz unlockable domain: the paper reports a frequency region between 1118.409 nm and 1118.339 nm where the BBO cavity could not be locked. The effect was reproduced using several lasers, cavities, and crystals, with all crystals from the same manufacturer (Crystals of Siberia). The authors state that this domain restricts two-photon Raman transitions via detuned levels.
- [P:Friedenauer2006] Stability observations: UV output fluctuated within 2% of the mean; microsecond-scale drops smaller than 4% were observed; drops larger than 7% occurred less than once per minute. Environmental temperature changes of 2 K produced output changes as large as 10%, reduced to 5% with improved thermal isolation of the crystal oven.
- [P:Friedenauer2006] Pump-source operational constraint: after amplifier turn-on, output polarization drifts fall off over about two hours if the non-polarization-maintaining fibre is fixed; remaining polarization changes are attributed to heat-sink temperature changes and can reduce isolator transmission. The authors propose active heat-sink temperature stabilization as a mitigation.

**Outcome classification:** Resolved — Friedenauer2006 baseline parameters have been extracted into the Phase 1 structured literature-data schema. Review status remains DRAFT pending steward check against the PDF.

---

### KD-UV280-014 — Phase-locked dual-source phase-noise literature

**Charter ref:** §4 counter-observation (Scout/peer input v0.3).

#### Section A — Claim
Modern phase-locked dual-source CW architectures can achieve sub-Hz relative linewidth; this is the substrate for the v0.3 Scout counter-observation that dual-source SFG (CHARTER §4 family 2) should not be ruled out by inheritance from Friedenauer-baseline framing.

#### Section B — Predictions
- Documented OPLL / OPLL-like demonstrations at IR / visible wavelengths with sub-Hz residual linewidth.
- Loop bandwidth of 100 kHz – 1 MHz with residual phase noise < −100 dBc/Hz in the gate-critical band (CHARTER §1.5 Level 0/1 — phase-noise budget).
- Mean-time-between-lock-loss compatible with the 8-hour sustained operation success criterion (§6.1).

#### Section C — Constraints
TODO: cite OPLL phase-noise demonstration papers; cite fibre-laser OPLL state-of-the-art; cite institutional dual-source experience if any.

**Outcome classification:** TBD — feeds Phase 4 axis 2 scoring directly.

---

### KD-UV280-015 — Pump source options — Yb-fibre vs. VECSEL near 1118 nm

**Charter ref:** §3 (open for redesign — pump-laser source).

#### Section A — Claim
Both Yb-doped fibre lasers and VECSEL systems are viable single-frequency CW pumps at or near 1118 nm; trade-offs include linewidth, RIN, polarisation drift (Friedenauer 2006 §5 issue), and vendor availability.

#### Section B — Predictions
- Yb-fibre amplifiers at 1118 nm with > 5 W single-frequency output are commercially available.
- VECSEL systems near 1118 nm exist with comparable power but different noise / drift characteristics.
- Polarisation-drift behaviour differs between architectures (active Peltier control for fibre vs. intrinsic VECSEL stability).

#### Section C — Constraints
TODO: cite Yb-fibre amplifier vendor specs (NKT, IPG, Toptica); cite VECSEL papers near 1118 nm; cite Friedenauer 2006 §5 polarisation-drift discussion.

**Outcome classification:** TBD.

---

## Population protocol

This dossier is populated by Phase 1 work. Each entry transitions through:

1. **SCAFFOLD** (current) — section structure defined; citation slots empty.
2. **POPULATING** — at least one citation in Section C; Outcome classification still TBD.
3. **DRAFT** — Section C complete to the steward's satisfaction; Outcome classification proposed (Resolved / Operationally bounded / Underdetermined).
4. **REVIEWED** — Outcome classification confirmed; entry usable as Phase 4 input.

The crystal/coating evidence table is populated row-by-row in parallel with the entries; cells without citation are not admitted to Phase 4 scoring.

Per CHARTER §5.1: this dossier is *literature collection*, not architecture-family-specific simulation. It is unblocked pre-G1 and may proceed in parallel with Phase 0.5 closure and Phase 2 baseline measurement.

Per CHARTER §9 trigger question: dossier population that *changes* a §1.5 Level 0/1 parameter triggers the reclassification rule and a Council-3 deliberation. Dossier population that merely *informs* parameter-tightening within the asymmetric erosion protection (tightening allowed with documented rationale) is logged in `/logbook/` with cross-reference to the relevant entry.

---

## References (master list)

*Per `single-25Mg-plus/REFERENCES.md` pattern. Each entry to be filled with citation key, full citation, DOI, role in this dossier, and which entries it informs.*

```yaml
- key: "Friedenauer2006"
  citation: "A. Friedenauer et al., Applied Physics B 84, 371 (2006)"
  doi: "10.1007/s00340-006-2274-2"
  informs: ["KD-UV280-001", "KD-UV280-005", "KD-UV280-010", "KD-UV280-013", "KD-UV280-015"]
  role: "v1.0 reference baseline; reports 1118 → 559 → 280 quadrupling, 275 mW source-side, 14-GHz unlockable domain (§4), polarisation drift of fibre amplifier heat sink (§5)."

- key: "BoydKleinman1968"
  citation: "G. D. Boyd and D. A. Kleinman, J. Appl. Phys. 39, 3597 (1968)"
  doi: "10.1063/1.1656831"
  informs: ["KD-UV280-005", "KD-UV280-006", "KD-UV280-007"]
  role: "Foundational SHG focusing theory; cited as external coastline per endorsement.md."

# TODO: add entries for each citation as they are added to Section C of any ledger entry.
```

---

*Dossier version: v0.2-populating — 2026-05-01. Steward to assign final KD number and increment to v0.x as entries populate.*
