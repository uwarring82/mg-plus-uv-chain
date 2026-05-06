---
layout: default
title: KD-2026-XXX — CW UV source architectures and crystal/coating evidence at 280 nm
description: Phase 1 literature dossier in Kompass-Dossier format. 15 ledger entries with Section A/B/C and §8 outcome classification.
---

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
| KD-UV280-001 | Quadrupling architecture (Friedenauer baseline family) | §4.1 | Operationally bounded | POPULATING |
| KD-UV280-002 | Sum-frequency mixing architectures | §4.2 | TBD | SCAFFOLD |
| KD-UV280-003 | Hybrid architectures (dual-source / OPA-based) | §4.3 | TBD | SCAFFOLD |
| KD-UV280-004 | Direct deep-UV sources (AlGaN diodes, deep-UV VECSEL) | §4.4 | TBD | SCAFFOLD |
| KD-UV280-005 | BBO at 280 nm — phase-matching, walk-off, damage threshold | §5 P1, §8.4 | Operationally bounded | POPULATING |
| KD-UV280-006 | CLBO at 280 nm — competing crystal characterisation | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-007 | LBO at relevant SHG/SFG stages | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-008 | UV mirror coatings — HR, OC, AR specifications and degradation | §5 P1, §8.6 | TBD | SCAFFOLD |
| KD-UV280-009 | Hygroscopic and environmental constraints (BBO, CLBO) | §5 P1 | TBD | SCAFFOLD |
| KD-UV280-010 | 14-GHz unlockable resonance domain — published evidence | §8.1 | Underdetermined | POPULATING |
| KD-UV280-011 | UV-induced BBO degradation and gas-environment dependence | §8.2, §8.4 | TBD | SCAFFOLD |
| KD-UV280-012 | UV mirror coating degradation under CW exposure | §8.6 | TBD | SCAFFOLD |
| KD-UV280-013 | Friedenauer 2006 baseline parameter extraction | §1 baseline | Resolved | DRAFT |
| KD-UV280-014 | Phase-locked dual-source phase-noise literature | §4 (counter-obs.) | TBD | SCAFFOLD |
| KD-UV280-015 | Pump source options — Yb-fibre vs. VECSEL near 1118 nm | §3 open | Operationally bounded | POPULATING |

---

## Crystal and coating evidence table

Per CHARTER §5 Phase 1 row (v0.8 Architect-stress-test recommendation): a dedicated table covering BBO, CLBO, LBO-relevant stages, coating degradation modes, hygroscopic and environmental constraints, and vendor / batch sensitivity. The table is the Phase 1 deliverable's central artefact.

| Crystal / coating | SHG/SFG stage | d_eff (pm/V) | Phase-match type | Walk-off ρ (mrad) | CW LIDT @ 280 nm (W/cm²) | Hygroscopic? | Vendor/batch sensitivity | Notes / citations |
|---|---|---|---|---|---|---|---|---|
| BBO | 559 → 280 (SHG) | **1.44 (1.30–1.60) [P:Eckardt1990] derived; ±10%** (Eimerl-anchored 1.15 retained as historical lower bound) | Type-I, θ_PM = 44.21° (Eimerl) / 44.28° (Tamošauskas) — agreement 0.07° | 83.1 (Eimerl) / 83.8 (Tamošauskas) — agreement 0.7 mrad | **operational-lifetime split**: intrinsic 280 nm CW LIDT not measured anywhere in the published literature (acceptance criterion #1 negative result, see [task-E logbook](../logbook/2026-05-04-bbo-cw-uv-lidt-task.md)); operational-lifetime adjacent-wavelength anchor at **266 nm: cavity-loss-increase rate 5×10⁻⁵ % / hour at 260 W / cm² average UV power density, > 1200 h fixed-beam reliability across three Sony Cz-BBO samples** [P:Kondo1998]+[P:Kubota1998]; quasi-CW corroboration at 266 nm with > 8 h 3 % rms power stability [P:Kumar2015]; 280 nm-specific **surface-damage threshold on auxiliary fused-silica components 32-64 W / cm²** over a few hours [P:Hemmerling2011]. Mechanism: degradation rate scales as `\|E\|` (sub-linear in intensity), thermal → multiphoton transition between CW and pulsed regimes, UV-driven (not green-driven) failure mode | mild surface; protected by AR coatings + dry-N₂ purge per Kubota1998 / Kondo1998 | Same-vendor batch / cut sensitivity reported for the 14-GHz unlockable domain; all tested Friedenauer crystals came from Crystals of Siberia. Eckardt 1990 used a three-sample mix (two Stanford-grown + one Fujian = the same crystal Eimerl used) with 4 % reproducibility, ruling out vendor sensitivity at this level. Hemmerling 2011 (Döhrer Elektrooptik BBO) and Hume 2010 (NIST Mg-Raman) document additional vendors but do not directly compare them. Sony Cz-BBO (Kondo / Kubota 1998) is internal growth, not commercial. | [P:Friedenauer2006] §4; [P:Eckardt1990] for d_eff central anchor; [P:Eimerl1987] for Sellmeier + d_11 + thermomechanical; [P:Tamosauskas2018] for refined-Sellmeier cross-check; [P:Kondo1998] + [P:Kubota1998] joint Sony-programme citation for the 266 nm operational-lifetime anchor; [P:Kumar2015] for the 266 nm thermally-quasi-CW data and the temperature-mitigation lever; [P:Hemmerling2011] for the only 280 nm-specific CW UV surface-damage threshold; [S:Turcicova2022] for the BBO LIDT-vs-pulse-duration compendium and the AR-coating LIDT-lowering bracket. |
| BBO | 1118+376 → 280 (SFG) | TBD — distinct config from Type-I SHG; recompute from [P:Eckardt1990] tensor + [P:Eimerl1987] / [P:Tamosauskas2018] Sellmeier when this architecture family is reactivated | TODO (Type-I or Type-II depending on polarization budget) | TBD — recompute when needed | TODO | mild surface | TODO | TODO: cite |
| CLBO | 559 → 280 (SHG) | TODO | TODO | TODO | TODO | strongly hygroscopic | TODO — known temperature/humidity sensitivity | TODO: cite |
| CLBO | 1064+376 → 280 (SFG) | TODO | TODO | TODO | TODO | strongly hygroscopic | TODO | TODO: cite |
| LBO | 1118 → 559 (SHG, intermediate) | TODO | TODO | TODO | n/a (visible stage) | low | TODO | TODO: cite |
| HR coating @ 280 nm | UV cavity mirror | n/a | n/a | n/a | adjacent-wavelength bound at 244 nm: fluoride (CaF₂) HR stable to 10 W intracavity in UHV, 20 W at 10⁻⁴ to 1 mbar O₂ on multi-hour timescales [P:Burkley2021]; oxide (SiO₂) HR requires ≥ 0.67 mbar O₂ for stable operation [P:Burkley2021 / Cooper2018]; bandgap-LIDT material ranking silica > alumina > hafnia > tantala > niobia > titania under contamination [P:Brown2019] | not directly applicable to coatings; substrate (CaF₂, fused silica) hygroscopy is mild | TODO — vendor variability is the §8.6 partition concern; deposition-method ranking IBS > magnetron > e-beam > pulsed laser per [S:Turcicova2022] | [P:Burkley2021] for fluoride-vs-oxide head-to-head; [P:Brown2019] for bandgap-LIDT scaling; [S:Turcicova2022] for deposition-method ranking |
| OC coating @ 280 nm | UV cavity output | n/a | n/a | n/a | adjacent-wavelength evidence: AR-coat damage on the UV-exit face is the consistent first failure mode at 244 / 266 / 280 nm with translate-to-fresh-spot recovery [P:Kondo1998]+[P:Kumar2015]+[P:Burkley2021]; at 244 nm, ~ 1-2 % / hour total power loss attributable to OC-coating damage, recoverable [P:Burkley2021] | n/a | TODO — see HR row | [P:Kondo1998]+[P:Kumar2015]+[P:Burkley2021] joint multi-wavelength evidence on UV-exit-face AR-coat failure mode |
| AR coating @ 280 nm | UV-passing optics | n/a | n/a | n/a | 280 nm-specific CW UV surface-damage threshold on UV-grade fused-silica AOM crystal / right-angle prism / dielectric mirror surfaces: **32-64 W / cm² over a few hours** [P:Hemmerling2011]; multilayer HfO₂ + Al₂O₃ + SiO₂ AR coating LIDT ~ 1 GW / cm² (likely non-premium crystal, [S:Turcicova2022]); dual-wavelength AR-coat LIDT 20 % lower than single-wavelength AR-coat per [S:Turcicova2022] | n/a | TODO — see HR row | [P:Hemmerling2011] for the 280 nm-specific surface-damage threshold (no adjacent-wavelength caveat); [S:Turcicova2022] for the multilayer AR-coat LIDT bracket |

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
- [P:Friedenauer2006] Existence proof for the Yb-fibre-pumped quadrupling variant: 2 W single-frequency at 1118 nm → LBO ring cavity (950 mW at 559 nm, > 52.7 % conversion) → Brewster-cut BBO ring cavity (275 mW near 280 nm, 28.9 % conversion). Overall efficiency 15.2 %. Structured extraction: [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml).
- [P:Friedenauer2006] At 275 mW source-side, the Friedenauer demonstration is **below** the §2 indicative ≥ 500 mW target. Reaching ≥ 500 mW within this family requires either higher pump power (constrained by §1.5 thermal-load envelope) or improved per-stage efficiency (constrained by crystal/coating evidence in KD-UV280-005, -008).
- [P:Friedenauer2006] Second SHG (559 → 280, BBO) is the lower-efficiency stage (28.9 % vs > 52.7 % for the first), consistent with prediction B-2 that the UV stage is the binding one for thermal load and degradation. (Direct degradation-rate evidence is logged in KD-UV280-011, not this entry.)
- [P:Hemmerling2011] **Architecture-family corroboration (PTB Braunschweig).** Yb-fibre at 1118.21 nm (Koheras Boostik Y10, < 70 kHz linewidth, 1 W) → LBO 4×4×18 mm³ NCPM Type-I bow-tie cavity → ~ 450 mW at 559 nm → BBO 3×3×10 mm³ Brewster-cut critical Type-I bow-tie cavity → ~ 60 mW at 280 nm. Same essential architecture as Friedenauer 2006 with refinements (9.2 GHz EOM between cavities, Hänsch-Couillaud locking on both); different crystal vendors (LBO from Castech, BBO from Döhrer Elektrooptik vs. Friedenauer's Crystals of Siberia). Structured extraction: [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml).
- [P:Burd2016] **VECSEL-pumped architecture-family corroboration (NIST Boulder).** Two distinct VECSEL designs: (i) externally-quadrupled VECSEL at 1117 nm IR (3 W) → fiber-coupled QPM lithium niobate waveguide doubler → 559 nm (260 mW) → BBO buildup cavity → 280 nm (23 mW); (ii) intracavity-doubled VECSEL at 1141 nm with intracavity LBO → 571 nm (1.2 W per output beam) → BBO buildup cavity → 285 nm. Linewidth 50 kHz comparable to Yb-fibre (cf. Friedenauer 2006 < 200 kHz, Hemmerling2011 < 70 kHz). The conclusion identifies the LiNbO₃ waveguide doubler — **not** the BBO 280 nm stage — as the bottleneck for power scaling in this architecture; this is a divergence from the Friedenauer-class assumption that the UV stage is binding (cf. prediction B-2). Structured extraction: [`data/literature/Burd2016/extracted.yaml`](../data/literature/Burd2016/extracted.yaml). Couples to `KD-UV280-015`.
- [S:Hume2010] NIST Boulder Wineland-group thesis documents two parallel chains for the same Mg⁺ system: a Yb-fibre + LBO + BBO Mg-Raman chain at 1120 nm (essentially identical to Friedenauer 2006 with a 2 nm fundamental-wavelength shift) and a dye-laser + BBO Mg-Doppler chain at 560 nm. Architecture-only documentation; no operational lifetime numbers. `[S]`-tier source supporting the architecture-family lineage. Structured extraction: [`data/literature/Hume2010/extracted.yaml`](../data/literature/Hume2010/extracted.yaml).
- [P:Kjaergaard2000] **Pre-Friedenauer prior-art (Aarhus, year 2000).** Single-mode tunable CW dye laser pumped by Ar⁺ → SHG in 5-mm BBO external bow-tie cavity → 280 nm (Mg⁺ Doppler) and 285 nm (Mg photoionization, ~ 2 mW). Establishes that BBO-doubled CW UV at 280-285 nm was operating in Mg-ion labs by 2000, predating the Friedenauer Yb-fibre architecture by 6 years. Structured extraction: [`data/literature/Kjaergaard2000/extracted.yaml`](../data/literature/Kjaergaard2000/extracted.yaml).
- TODO: cite alternative quadrupling demonstrations at higher output power than the 60-275 mW range covered by Friedenauer 2006, Hemmerling 2011, and Burd 2016.
- TODO: cite quadrupling demonstrations using CLBO at the UV stage instead of BBO.

**Outcome classification:** **Operationally bounded** — single-source quadrupling is demonstrated to be a viable family by Friedenauer 2006, but the ≥ 500 mW target is not yet covered by published demonstration; Yb-fibre pump bound is established, VECSEL-pump and alternative-UV-crystal bounds remain to be cited. Status: **POPULATING** (Section C incomplete).

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
- [P:Friedenauer2006] BBO is used at the 559 → ~280 nm SHG stage with a Brewster-cut crystal of dimensions 4 mm × 4 mm × 10 mm operated at ~ 50 °C (selected to keep polished hygroscopic surfaces above the dew point). The Boyd–Kleinman optimum waist (1/e² intensity radius) is reported as 19.4 μm. The paper does **not** report the cut angle, the coating vendor, or a CW LIDT figure at 280 nm. Structured extraction: [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml) (parameters `crystal_BBO_type`, `BBO_crystal_size`, `T_BBO_operating`, `w0_BBO_BK_optimum`).
- [P:Friedenauer2006] BBO ring-cavity reflectivities at the 559 nm fundamental: input coupler 98.4 %, HR mirrors > 99.93 %, output coupler > 99.8 % at fundamental and > 94 % transmission at 280 nm. Cavity geometry: 470 mm round-trip, 59.4 mm focusing-mirror separation, 27.4° full folding angle (chosen to compensate astigmatism from the Brewster cut). Stage doubling efficiency 28.9 % (cf. > 52.7 % for the LBO first stage).
- [P:Friedenauer2006] Vendor / batch sensitivity flag (couples to KD-UV280-010): all BBO crystals tested for the Friedenauer apparatus came from **Crystals of Siberia**. The 14-GHz unlockable domain was reproduced across crystals from this single vendor. This is a same-vendor observation, not yet a vendor-discriminating result.
- [P:Eimerl1987] **BBO crystal structure and allowed nonlinear coefficients.** Single-crystal X-ray diffraction confirms the low-temperature β-BaB₂O₄ phase as space group R3c, which restricts the allowed nonlinear coefficients to `d_11`, `d_31`, `d_33`, `d_15` (Kleinman symmetry equates `d_15 = d_31`, leaving two relevant components). Bounds: `|d_22 / d_11| < 0.05` and `|d_31 / d_11| < 0.05` at 1064 nm SHG. Hexagonal lattice constants `a = 12.547(6) Å`, `c = 12.736(9) Å`; density 3.840 g/cm³. Structured extraction: [`data/literature/Eimerl1987/extracted.yaml`](../data/literature/Eimerl1987/extracted.yaml) (parameters `BBO_phase`, `BBO_lattice_a`, `BBO_lattice_c`, `BBO_density`, `BBO_d22_over_d11_bound`, `BBO_d31_over_d11_bound`).
- [P:Eimerl1987] **Sellmeier coefficients (`n_o(λ)`, `n_e(λ)`) — primary anchor.** The "this work" Sellmeier set, valid 212.8 – 1064 nm, with form `n² = A + B/(λ² + C) + Dλ²` (λ in µm): `n_o`: A = 2.7405, B = 0.0184 µm², C = −0.0179 µm², D = −0.0155 µm⁻²; `n_e`: A = 2.3730, B = 0.0128 µm², C = −0.0156 µm², D = −0.0044 µm⁻². The set reproduces the paper's own Table I direct prism measurements to RMS < 4×10⁻⁴ and the Table VI calculated PM angles for 1064→532 (Type I) and 532→266 (Type I) to within 0.05°. **Note:** the paper's Table II column header for `C` reads "µm⁻²" but that is dimensionally inconsistent with Eq. (1); the `C` in µm² interpretation (with the negative signs as printed) is the one that reproduces the rest of the paper. Alternative sets from Chen 1985 (deprecated — predicts `θ_PM(1064→532, I)` 3° low) and Kato 1986 (close agreement with Eimerl, useful sanity-check) are also recorded. Structured extraction: parameters `BBO_sellmeier_no_eimerl1987`, `BBO_sellmeier_ne_eimerl1987`, plus `BBO_sellmeier_alternative_chen1985`, `BBO_sellmeier_alternative_kato1986`.
- [P:Eimerl1987] **Effective nonlinear coefficient at 559 → 280 nm Type-I — historical lower-bound.** Tensor anchor `d_11 = 1.6 ± 0.4 pm/V` (Eimerl 1987 Eq. 14, measured relative to `d_36(KDP) = 0.39 pm/V`). The Type-I `d_eff` formula (Eq. 17) is `d_eff = d_31 sin θ − d_11 cos θ cos(3φ)`. Evaluated at the derived θ_PM, this gives `|d_eff(559→280, Type I)| = 1.15 pm/V central` (range 1.09–1.20 across azimuth, ±25% from the d_11 measurement uncertainty). **This value is now superseded as the central anchor by the Eckardt 1990 measurement (next bullet)**, but it is retained here as the historical lower bound and as a check on the upgrade. Structured extraction: parameters `BBO_d11_eimerl1987`, `BBO_d_eff_formula_typeI`, `BBO_d_eff_typeI_559_to_280nm`.
- [P:Eckardt1990] **Effective nonlinear coefficient at 559 → 280 nm Type-I — central anchor.** Tensor anchor `|d_22| = 2.2 pm/V` (Eckardt 1990 Section IV; ±10% absolute accuracy, ±4% reproducibility across 12 measurements on three samples). `d_22` in Eckardt's axis convention refers to the same physical R3c tensor element as `d_11` in Eimerl 1987's convention; the difference is which crystallographic axis is called *x*. The headline finding: `|d_22|` from this work is **37% higher** than Eimerl 1987's `|d_11|`, with overlap only at the very edge of Eimerl's ±25% uncertainty envelope. The Eckardt-convention Type-I formula (Table I) is `d_eff = d_31 sin(θ + ρ) − d_22 cos(θ + ρ) sin(3φ)`, with the modern `θ → θ + ρ` walk-off correction. Evaluated at the derived θ_PM = 44.21° and ρ = 4.76° with optimum azimuth `|sin(3φ)| = 1`, this gives `|d_eff(559→280, Type I)| = 1.44 pm/V central` (range 1.30–1.60 across azimuth and ±10% absolute accuracy). The conversion-efficiency-at-fixed-intensity ratio is `(1.44/1.15)² = 1.57` — i.e., the Eckardt anchor implies ~57% more conversion at the BBO stage than the Eimerl anchor would have predicted, consistent with the ~50% conversion efficiencies achieved at the LBO stage in modern Friedenauer-class systems. The d_36(KDP) reference used by Eckardt is 0.38 pm/V (vs Eimerl's 0.39 pm/V); the 2.6% difference in the calibration cannot account for the 37% revision and the discrepancy is intrinsic to the BBO measurement. Caveat: Eckardt measures at 1064 nm SHG, not 559 nm SHG; transfer to the 559 → 280 nm operating point assumes weak `d_22` dispersion to 559 nm, the same assumption Eimerl makes. Structured extraction: [`data/literature/Eckardt1990/extracted.yaml`](../data/literature/Eckardt1990/extracted.yaml) (parameters `BBO_d_eff_eckardt1990_at_1064_to_532_typeI`, `BBO_d22_eckardt1990`, `d36_KDP_eckardt1990`, `BBO_d_eff_formula_eckardt`, `BBO_d_eff_typeI_559_to_280nm_eckardt`). Cross-check note in `data/literature/Eimerl1987/extracted.yaml` `cross_check_notes.d_eff_eckardt1990_vs_eimerl1987`.
- [P:Tamosauskas2018] **Refined Sellmeier set, valid 0.188 – 5.2 µm — modern cross-check anchor.** Three-oscillator dispersion equations (Eq. 1) for both `n_o` and `n_e`, anchored to a much wider data set than Eimerl 1987: direct refractive-index measurements from the Chen 2012 book (0.254 – 2.325 µm), the Kato 1986 fitting rule down to 204.8 nm, indirect refractive-index extraction from Light Conversion Ltd.'s database of > 600 phase-matching curves, and the authors' own SFG measurements 0.8 – 5.2 µm. Form: `n²(λ) = 1 + Σᵢ Aᵢ λ²/(λ² − Cᵢ)` with three oscillators (two in the UV at C ~ 10⁻² µm², one in the IR at C ~ 60 / 263 µm²). At the 559 → 280 nm operating point, the Tamošauskas Sellmeier yields `n_o(559) = 1.6719`, `n_e(559) = 1.5531`, `n_o(280) = 1.7445`, `n_e(280) = 1.6039` — about 10⁻³ lower than Eimerl in the visible; at 280 nm the n_o offset narrows to ~10⁻⁴ while n_e remains ~10⁻³ lower. Derived `θ_PM(559→280, Type I) = 44.28°` and `ρ = 83.8 mrad`, agreeing with the Eimerl-derived values within 0.07° / 1 mrad respectively despite the absolute-index disagreement: the Type-I PM condition `n_e(2ω, θ) = n_o(ω)` is sensitive to index *differences*, not absolute values, and the difference is similar in both sets. The Eimerl and Tamošauskas Sellmeier sets are kept as **parallel anchors** — neither replaces the other; downstream sensitivity studies should use both as bracketing values. The 4.62 µm `n_o = n_e` crossover predicted by the Tamošauskas set (and verified experimentally in Fig. 4 of the paper) deviates from the Eimerl-extrapolated 5.75 µm crossover, which is a useful cross-set discriminant for any future mid-IR architecture work but not relevant to the 280 nm operating point. Structured extraction: [`data/literature/Tamosauskas2018/extracted.yaml`](../data/literature/Tamosauskas2018/extracted.yaml) (parameters `BBO_sellmeier_no_tamosauskas2018`, `BBO_sellmeier_ne_tamosauskas2018`, `BBO_sellmeier_validity_range_tamosauskas2018`, plus derived 559 / 280 nm values). Cross-check note in `data/literature/Eimerl1987/extracted.yaml` `cross_check_notes.sellmeier_tamosauskas2018_vs_eimerl1987`.
- [P:Eimerl1987] **DERIVED — Type-I phase-matching angle and walk-off at 559 → 280 nm.** From the Eimerl 1987 Sellmeier set: `θ_PM(559→280, Type I) = 44.21°` and `ρ(280 nm extraordinary at θ_PM) = 83.1 mrad` (4.76°). Cross-check: the same Sellmeier set reproduces the paper's directly measured PM angles for 1064→532 (Type I) and 532→266 (Type I) to better than 0.05°. A prior notebook estimate of 85 mrad is confirmed within ~2 mrad against the Eimerl-anchored value; [`notebooks/2026-05-01-friedenauer-bk-recalculation.py`](../notebooks/2026-05-01-friedenauer-bk-recalculation.py) now uses the Eimerl value directly. The apparent factor-2.17 BBO BK discrepancy in the notebook's §5/§7 summary is therefore not driven by an inaccurate walk-off estimate, and the cavity-specific (non-single-pass-BK) optimisation criterion remains the most likely explanation. Structured extraction: parameters `theta_PM_559_to_280nm_typeI`, `rho_walkoff_280nm_typeI`. Friedenauer 2006 does not state the BBO PM angle directly but operates a Brewster-cut crystal whose cut angle is consistent with this derived value.
- [P:Eimerl1987] **Transparency and bulk damage threshold (caveat).** Clear transmission window 200–3000 nm (4 mm sample); UV edge onset 215 nm; 100%/cm extinction at 200 nm. Therefore 280 nm sits ~65 nm above the UV onset, well inside the transparency window. Bulk damage threshold under 1064 nm / 1 ns / one-on-one irradiation: 13.5 J/cm² in inclusion-free regions of the sample tested, dropping to ~4 J/cm² at inclusion sites — the bulk threshold is largely controlled by sample quality. **NB: this is _not_ a CW-UV LIDT.** The CW-UV photo-induced surface degradation regime that governs operational lifetime at 280 nm is _not_ measured by Eimerl 1987 and remains the binding open extraction item for this entry. Structured extraction: parameters `BBO_transparency_range`, `BBO_uv_edge_onset`, `BBO_damage_threshold_1064nm_1ns`.
- [P:Eimerl1987] **Thermomechanical and thermo-optic constants — feeds CHARTER §1.5 thermal-load envelope.** Strongly anisotropic thermal conductivity (`κ_11 = 0.08`, `κ_33 = 0.8` W/m/K — 10×) and thermal expansion (`α_11 = 4×10⁻⁶`, `α_33 = 36×10⁻⁶` /K — 9×); fracture toughness `K_c = 150 kPa·m^(1/2)`. Eimerl 1987 derives a thin-plate fracture temperature ~10× higher than KDP / LiNbO₃ / LiIO₃ — BBO is unusually robust against thermally-induced fracture. Wavelength-averaged thermo-optic coefficients `dn_o/dT = −16.6×10⁻⁶ /K`, `dn_e/dT = −9.3×10⁻⁶ /K`. The κ-anisotropy directly affects heat-extraction geometry from the Brewster-cut UV-stage crystal and cannot be approximated by an isotropic value when the §1.5 thermal-load budget is tightened. Structured extraction: parameters `BBO_thermal_conductivity_kappa11/33`, `BBO_thermal_expansion_alpha11/33`, `BBO_fracture_toughness`, `BBO_dnodT_averaged`, `BBO_dnedT_averaged`.
- [S:SNLO] (Sandia National Laboratories, SNLO nonlinear-optics code; cited by Friedenauer 2006 footnote [7]) Documented as the secondary computational tool through which the primary measurement record is most often consulted in lab settings. Admissible per the dossier's `[S]` rule but not the sole basis for any constraint here; the Eimerl 1987 [P] anchors above carry that role. SNLO is software, not a paper, and therefore is not given a `data/literature/<key>/` folder; cited inline only.
- **Search-boundary statement (acceptance criterion #2 of [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../logbook/2026-05-04-bbo-cw-uv-lidt-task.md)).** Three scout passes (2026-05-04 / -05) and full extraction of the available candidate cluster (six papers, 2026-05-06) found **no peer-reviewed CW operational-lifetime measurement of BBO at 280 nm** in the published literature. The closest published anchors are at 266 nm (Sony Cz-BBO programme reported jointly in `[P:Kondo1998]` + `[P:Kubota1998]` and re-extracted from a different angle in `[P:Kumar2015]`) and at 244 nm (Yb-quadrupling-cavity oxide-vs-fluoride coating study `[P:Burkley2021]`). Adjacent-wavelength evidence is therefore admitted to Section C below, but the search-boundary clause and adjacent-wavelength caveat is binding: the cited values are **not** direct 280 nm CW LIDT measurements, and a port to the Friedenauer-class operating point requires phase-matching-angle and `d_eff` adjustment plus a mechanism continuity argument.
- [P:Kondo1998] + [P:Kubota1998] **>1000 h CW reliability of Cz-BBO at 266 nm (Sony programme — joint citation).** Authorship overlap, identical operating point (532 → 266 nm Type-I SHG, 100 mW UV from 500 mW green, w₀ = 46 μm in 6-mm BBO at 47.5° cut, three Cz-BBO samples, 0.4 L / min N₂ purge, identical d_eff = 1.642 pm / V and γ_SH = 5 × 10⁻⁵ W⁻¹) confirm the two papers report the same Sony Research Center experiment in two venues; **treat as one programme citation, not two independent measurements.** Headline reliability number: round-trip cavity-loss-increase rate `5 × 10⁻⁵ % / hour at 260 W / cm² average UV power density` over > 1200 h fixed-beam operation, reproduced across three Cz-grown BBO samples. The empirical fit `δ̇_cav [%/h] = 2.806 × 10⁻⁶ × (P_UV / A [W / cm²])^0.566` (R = 0.98272) gives a sub-linear scaling consistent with `δ̇_cav ∝ |E|` rather than `∝ I`. Lifetime extrapolation: 2000 h to 0.1 % loss-increase under input-power compensation. Structured extractions: [`data/literature/Kondo1998/extracted.yaml`](../data/literature/Kondo1998/extracted.yaml) (journal article: cavity geometry, RIN < −130 dB / Hz at 2-10 MHz, N₂-purge / sealed-cavity protocol) and [`data/literature/Kubota1998/extracted.yaml`](../data/literature/Kubota1998/extracted.yaml) (proceedings: full Cz-BBO characterisation, CW + pulsed regimes, unified `p(E) = C exp(−K / E)` damage-probability model). **Adjacent-wavelength caveat: this is a 266 nm result, not a 280 nm result.**
- [P:Kondo1998] + [P:Kubota1998] **Cz-BBO crystal characterisation (Sony programme).** Linear absorption at 213 nm (e-pol) = 6 % / cm; exponential absorption tail terminates around 230 nm (likely intrinsic / LO-phonon); long-wavelength Rayleigh scattering at 266 nm = 2 % / cm (o-pol) and 1 % / cm (e-pol); two-photon-absorption coefficient at 266 nm β = 0.9 cm / GW; thermal conductivity 1.07 W / m / K perpendicular to c-axis and 1.55 W / m / K parallel. Czochralski-grown 2-inch-diameter / 1-inch-high boules from Sony's in-house programme, polished to 0.2 nm-rms roughness; the Sony Cz samples have much lower point-defect density than typical flux-grown BBO per HeNe tomographic test. **The vendor-comparison TODO below is NOT closed by Kondo1998 + Kubota1998 — Sony BBO is internal Cz growth, not Crystals of Siberia / CASTECH / EKSMA / FEEFO.**
- [P:Kumar2015] **BBO at 266 nm in the thermally quasi-CW regime (80 MHz / 20 ps).** Single-pass FHG of 1064-nm picosecond Yb-fibre laser; 10-mm-long BBO at 47.56° Type-I phase-matching with d_eff = 1.75 pm / V (Nikogosyan-derived, consistent with Kondo1998's 1.642 pm / V within Sellmeier convention noise) and walk-off ρ = 85 mrad. Walk-off-limited effective length L_eff = 1.1 mm (loose focus, w_SH = 55 μm) or 0.4 mm (tight focus, 19 μm); temperature-acceptance bandwidth ΔT = 33 °C (vs Sellmeier-predicted 5.3 °C, attributable to the same walk-off-limited L_eff). Walk-off compensation (10 + 10 mm) achieves 35 % single-pass FHG efficiency (2.9 W UV from 8.2 W green). The thermal relaxation time τ = 53 μs (using ρ = 3.85 × 10⁶ g / m³, C_p = 0.49 J / g / K, K = 1.6 W / m / K) is much longer than the 12.5 ns inter-pulse interval, so the BBO experiences a pulse-train-averaged thermal load. Direct surface-temperature measurement: BBO core rises 21.8 → 27.9 °C at 1.7 W UV; UV-only contribution exceeds green-only contribution by ~ 4× at the operating point. **Output-face temperature 50 % higher than input-face — direct evidence that UV (not green) drives the thermal gradient and the failure mode (cf. `KD-UV280-011`).** Structured extraction: [`data/literature/Kumar2015/extracted.yaml`](../data/literature/Kumar2015/extracted.yaml). **Adjacent-wavelength caveat: 266 nm, not 280 nm; thermally quasi-CW, not strict CW.**
- [S:Turcicova2022] BBO + CLBO LIDT review (`source_tier: S`; cannot stand alone in Section C, must accompany a `[P]` anchor). Bibliographic-hub harvest: BBO LIDT scatter spans two orders of magnitude (0.1 - 10 GW / cm²) for pulse durations 10 ps - 10 ns; DUV LIDT lower than visible / NIR; vendor-catalogue values explicitly flagged as unreliable; S-on-1 LIDT can be ~ 2 × lower than 1-on-1 LIDT; BBO has ~ 20 % lower LIDT than CLBO. Multi-layer AR-coating LIDT lowering and IBS-vs-other-deposition ranking captured in `KD-UV280-008` and `-012`. Structured extraction: [`data/literature/Turcicova2022/extracted.yaml`](../data/literature/Turcicova2022/extracted.yaml).
- TODO: cite vendor-comparison studies (Crystals of Siberia vs CASTECH vs EKSMA / FEEFO) at 280 nm. Sony Cz-BBO (Kondo / Kubota), Castech LBO and Döhrer-Elektrooptik BBO (Hemmerling 2011), and the Sony / Hume Mg-Raman chain are documented but cannot substitute for a vendor-comparison study at the 280 nm operating point.

**Outcome classification:** **Operationally bounded** — Brewster-cut BBO at the 559 → 280 nm stage is operationally established (Friedenauer 2006), with cavity geometry, operating temperature, and BK-optimum waist documented; the upstream peer-reviewed material constants are now anchored to a three-paper set: `[P:Eckardt1990]` for the `d_eff` central value (with `[P:Eimerl1987]` retained as the historical lower bound), `[P:Eimerl1987]` and `[P:Tamosauskas2018]` as parallel Sellmeier anchors (consistent on derived `θ_PM = 44.21°` and `ρ ≈ 83 mrad` to within 0.1° / 1 mrad despite ~10⁻³ index-level disagreement), and `[P:Eimerl1987]` for the thermomechanical anisotropies. The Eckardt-anchored `|d_eff| ≈ 1.44 pm/V central` (range 1.30–1.60) revises the bare Eimerl-anchored value upward by `(1.44/1.15)² = 1.57×` in conversion-efficiency at fixed intensity, consistent with modern Friedenauer-class observations. **CW-UV LIDT at 280 nm remains the only binding open item**; tasks A and B of [`logbook/2026-05-04-bbo-alternative-references.md`](../logbook/2026-05-04-bbo-alternative-references.md) are now dispatched, leaving task E (CW-UV LIDT) as the residual literature-search task. Status: **POPULATING** — pending only the CW-UV LIDT anchor.

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
- **Search-boundary statement.** The published CW deep-UV coating-lifetime data is concentrated near 244 nm (Yb-quadrupling cavities for hydrogen 1S-2S spectroscopy) and 286 nm (Steinert thesis on Ba⁺) rather than at 280 nm itself. Adjacent-wavelength evidence is admitted with explicit mechanism-continuity arguments; the cited absolute thresholds depend on the wavelength-dependent coating-material absorption and on the photodecomposition cross-section of any operating-environment hydrocarbons.
- [P:Burkley2021] **Direct fluoride-vs-oxide head-to-head test at 244 nm CW intracavity (ETH Zürich).** Fused-silica (oxide) and CaF₂ (fluoride) input couplers tested in the same enhancement cavity. Fluoride results: stable up to **10 W intracavity at 10⁻⁸ mbar UHV** for 1-hour timescales (~ 4 % / hour drop after UV-conditioning at 10⁻³ mbar O₂ + 16 W intracavity for several hours); stable up to **20 W intracavity at 10⁻⁴ to 1 mbar O₂** for multi-hour timescales (4-hour stability at 16 W demonstrated at 10⁻³ mbar). Oxide results: drops by 50 %  / hour at 9-10 W in UHV, requires ≥ 0.67 mbar O₂ for stable operation per the Cooper 2018 prior-art baseline. Mechanism distinguished as **hydrocarbon contamination, not surface oxygen depletion** (fluoride coatings have no oxide layer and so cannot be affected by oxygen depletion). UV-ozone cleaning revives oxide via in-situ ozone / atomic oxygen generation; fluoride additionally benefits from radiation desorption per Heber et al. **Operational rule for 280 nm cavity design:** prefer fluoride coatings on CaF₂ substrates if UHV is required; otherwise use oxide coatings with continuous low-pressure O₂ purge ≥ 0.67 mbar. Cavity-hardware checklist (indium-seal vacuum windows, UHV-compatible PZT, peek screws, stainless / copper / aluminum only) is wavelength-independent. Structured extraction: [`data/literature/Burkley2021/extracted.yaml`](../data/literature/Burkley2021/extracted.yaml).
- [P:Brown2019] **Bandgap-dependent CW coating breakdown under contamination.** Carbon-microparticle-contaminated half-wave coatings of six oxide film types tested at 1070 nm CW (17 kW Yb-fibre laser, 0.5-1 mm spot). LIDT scales monotonically with film bandgap: titania (E_g = 3 eV) fails at 105 kW / cm²; silica (E_g = 9 eV) does not damage at the highest tested 17.8 MW / cm². Material-selection ranking for damage resistance under realistic (non-UHV, non-clean-room) contamination: **silica > alumina > hafnia > tantala > niobia > titania.** Free-carrier-absorption mechanism: Drude-Lorentz `α_FC ∝ 1 / ω²`, so the breakdown threshold becomes more aggressive at deep-UV wavelengths than at 1070 nm by ~ 16 × (in absorption coefficient at fixed N) — the contamination-driven CW breakdown mechanism is **more** demanding at 280 nm than at 1070 nm. Capping layers up to 5.5 μm thick give **no measurable improvement** because contaminant evaporation completes in < 1 ms while heat diffuses through the cap on the same timescale. **Operational rule for 280 nm cavity design:** prefer top-surface materials with the highest available bandgap (silica or alumina); avoid titania / niobia near the surface. Structured extraction: [`data/literature/Brown2019/extracted.yaml`](../data/literature/Brown2019/extracted.yaml).
- [P:Hemmerling2011] **CW UV surface damage at 280 nm — Friedenauer-class architecture (PTB).** UV-grade fused-silica AOM crystal surfaces, dielectric mirror surfaces, and right-angle-prism cathetus all degraded under CW UV at intensities **32-64 W / cm²** (5 mW UV beam focused to 50-70 μm waist) over **a few hours** in a 280 nm Mg⁺ laser system architecturally identical to Friedenauer 2006. Damage observed only on the *first reflecting surfaces* hit by the laser, suggesting a threshold above which the effect emerges. Mitigation by re-design to avoid foci near reflecting surfaces (Hemmerling 2011 Fig. 2). **This is the cleanest published 280 nm-specific CW UV surface-damage threshold available**; the wavelength caveat does NOT apply since this measurement is at 280 nm. Structured extraction: [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml).
- [S:Turcicova2022] BBO AR-coated for FHG (532 + 266 nm) using HfO₂ + Al₂O₃ + SiO₂ multilayer: LIDT ~ 1 GW / cm² (likely non-premium-grade crystal). Dual-wavelength AR-coating LIDT is comparable to AR @ 266 nm-only and 20 % lower than AR @ 532 nm-only. Deposition-method ranking: ion beam sputtering (IBS) > magnetron sputtering > electron beam evaporation > pulsed laser deposition; mixture coatings (e.g. ZrO₂-SiO₂ gradient) outperform discrete-layer coatings. `[S]`-tier: must accompany a `[P]` anchor (Burkley2021 or Brown2019).
- TODO: cite vendor-specific coating data sheets (Layertec, LaserOptik, EKSMA) for HR / OC / AR coatings at 280 nm with documented IBS deposition, S-on-1 LIDT, and lifetime curves under representative CW flux.
- TODO: cite Steinert 2024 thesis (Ba⁺ at 286 nm) for the closest-wavelength HfO₂ → Al₂O₃ swap precedent and the ozone-flush-mount design.

**Outcome classification:** **Operationally bounded** — the bandgap-dependent contamination mechanism (Brown 2019), the fluoride-vs-oxide CW deep-UV head-to-head (Burkley 2021), the 280 nm-specific surface-damage threshold (Hemmerling 2011, 32-64 W / cm² at fused silica), and the multi-layer-AR-coating LIDT lowering (Turcicova 2022) jointly constrain coating-material selection for the Friedenauer-class cavity. Vendor-specific coating LIDT data and the closest-wavelength HfO₂ / Al₂O₃ thesis precedent (Steinert 2024) remain TODO. Status: **POPULATING**.

---

### KD-UV280-009 — Hygroscopic and environmental constraints (BBO, CLBO)

**Charter ref:** §5 Phase 1.

#### Section A — Claim
BBO has mild surface hygroscopic behaviour requiring dry-gas housing for long-term stability; CLBO is strongly hygroscopic and requires heated dry-gas environment for operation.

#### Section B — Predictions
- Documented surface-degradation protocols for BBO under ambient-humidity exposure.
- Documented heated-housing requirements for CLBO with operating temperature ≥ 100 °C and dry-gas purge.

#### Section C — Constraints
- This entry is a **co-target** of the residual task E in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../logbook/2026-05-04-bbo-cw-uv-lidt-task.md): the gas-environment / hygroscopic dimension of CW-UV operation at 280 nm sits here, while the headline LIDT number is in `KD-UV280-005` and the mechanism is in `KD-UV280-011`. The same adjacent-wavelength caveat applies: gas-environment evidence comes from 244 nm (Burkley 2021) and 266 nm (Kondo / Kubota 1998, Kumar 2015) studies; mechanism continuity arguments are required for any port to 280 nm.
- [P:Kubota1998] **Slight hygroscopy of BBO mitigated by AR coatings + dry-N₂ purge.** "Although BBO is slightly hygroscopic, polished surfaces may be protected from humidity by applying anti-reflection coating layers" (Kubota 1998 introduction). Operational protocol in the Sony reliability test: AR coatings + 0.4 L / min dry-N₂ flow on the BBO crystal during operation. Friedenauer 2006's 50 °C operating temperature ("to keep polished hygroscopic surfaces above the dew point") is a different mitigation lever — neither paper measures the degradation rate as a function of relative humidity directly.
- [P:Kondo1998] **Dry-N₂ purge protocol and sealed-cavity recommendation.** The Sony 1200-h reliability test was performed with 0.4 L / min N₂ flow purging the external resonant cavity. Authors identify "residual oil vapor from the mechanical components inside the external cavity" as the dominant contamination source that "gradually and seriously degrades both mirrors and BBO crystal." Conclusion: "A hermetically sealed external cavity is highly desirable for long-term operation without a nitrogen gas purge." **Operational protocol for 280 nm:** N₂ purge or sealed enclosure + scrupulous oil-vapor exclusion is the documented baseline.
- [P:Burkley2021] **Oxygen-pressure phase boundary at 244 nm.** Fluoride coatings on CaF₂ substrates: stable at 10⁻⁴ to 1 mbar O₂ at 15-20 W intracavity for hours; stable at 10⁻⁸ mbar UHV at 10 W intracavity after UV-conditioning. Oxide coatings on SiO₂ substrates: require ≥ 0.67 mbar O₂ for stable operation (Cooper 2018 prior-art baseline). Mechanism: hydrocarbon contamination + oxygen-driven photo-cleaning via in-situ ozone / atomic-oxygen generation; the same mechanism applies to BBO surfaces. **Operational implication for 280 nm: dry-N₂ purge alone (per Kondo 1998) may be sub-optimal vs continuous low-pressure O₂ purge; the trade-off needs explicit evaluation.**
- [P:Kumar2015] **Temperature-mitigation lever (independent of gas-environment lever).** Operating BBO at elevated temperature (100-200 °C) reduces TPA by `β(22 °C) / β(200 °C) = 3.55 ×` (3.9 → 1.1 cm / GW at 266 nm) and dynamic colour-centre density by 69 % at 200 °C. Long-term stability at 200 °C: 3 % rms power stability over 8+ hours, 1.5 W → 1 W slow decline over 16 hours. **Operational lever for 280 nm: heating the BBO to 100-200 °C (Friedenauer's 50 °C is far below this envelope) is a complementary mitigation to dry-gas purging that does not require sealing the cavity.** Adjacent-wavelength caveat applies: the temperature-scaling exponent of TPA in BBO is mechanism-driven (Maxwell-Boltzmann population of multiphoton-excitable defect states) and should transfer to 280 nm with the same functional form.
- [P:Brown2019] **Cleanliness rationale.** Particulate carbon and steel contamination drops LIDT by 3-6 orders of magnitude vs pristine optics. Field-deployment LIDT is dominated by contamination, not by the intrinsic film LIDT. The free-carrier breakdown mechanism is more aggressive at deep-UV wavelengths (Drude-Lorentz `α_FC ∝ 1 / ω²`). **Operational rationale for 280 nm: the cleanliness protocols required by Kondo / Kubota (oil-vapor exclusion) and Burkley (UV-ozone in-situ cleaning) are not optional add-ons but are intrinsic to the operating-lifetime budget.** Cleanroom-grade handling protocols + inert-gas purge + (where possible) oxygen co-purge are jointly load-bearing.
- TODO: cite quantitative humidity-vs-degradation-rate measurements on BBO at 280 nm (none retrieved in the 2026-05-06 cluster).
- TODO: cite CLBO environmental-control protocol references (Sasaki, Yoshimura et al.; Nishioka 2005 SS-TSSG growth and water-resistance correlation).

**Outcome classification:** **Operationally bounded** — the gas-environment dimension is constrained by three complementary mitigation levers (dry-N₂ purge per Kondo / Kubota 1998, low-pressure O₂ purge per Burkley 2021, elevated operating temperature per Kumar 2015) and a contamination-rationale anchor (Brown 2019). Direct humidity-vs-degradation-rate measurements at 280 nm and CLBO-comparison environmental-control data are still TODO. Status: **POPULATING**.

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
- [P:Friedenauer2006] §4 reports a frequency region around the BBO ring-cavity locking range where the cavity could not be locked. Reported quantities: width ~ 14 GHz; wavelength bounds at the 1118 nm fundamental: 1118.339 nm (lower) and 1118.409 nm (upper). *Cross-check note:* the 70 pm wavelength span at 1118 nm corresponds to ~ 16.8 GHz under the standard Δν = c·Δλ/λ² conversion, not 14 GHz; the discrepancy is logged in [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml) `cross_check_notes.unlockable_domain_width_consistency` for Steward direct-PDF resolution. This entry treats the width and the bounds as separately reported quantities until that resolution.
- [P:Friedenauer2006] §4 reproduction conditions: the unlockable domain was observed across **several lasers, several cavities, and several crystals**. All crystals tested for this observation came from **Crystals of Siberia**. The vendor commonality is a recorded constraint, not yet a vendor-attributed mechanism.
- [P:Friedenauer2006] §4 explicit consequence statement: the domain "imposes restrictions for two-photon stimulated Raman transitions via detuned levels." This is the original Charter §1.5 Level 0 motivation for treating the 14-GHz region as operationally forbidden until G1 closes.
- [P:Friedenauer2006] §4 does **not** identify a mechanism. The paper records the observation but does not assign a candidate explanation among (refractive-index temperature drift / birefringence coupling / photochemical or colour-centre formation / impurity or growth defect). Per CHARTER §8 preamble, this is the canonical *Underdetermined* state at v1.0.
- TODO: hunt for **at least one** subsequent CW UV cavity-locking paper reporting a similar phenomenon; if found, the citation chain may suggest a candidate mechanism.
- TODO: cite candidate-mechanism background papers (BBO colour-centre formation, photorefractive effects, polarisation-coupling instabilities) **without** asserting attribution — Phase 2 discriminant scans (CHARTER §8.1) are the binding attribution mechanism, not literature search.

**Outcome classification:** **Underdetermined** at the literature level — Friedenauer 2006 establishes the observation but no mechanism is assigned, and no corroborating literature has yet been collected. This is a *literature-level* Underdetermined; the Charter §8.1 G1 outcome classification is determined by Phase 2 discriminant scans, not by this dossier entry. Status: **POPULATING** (corroborating-literature TODOs remain open).

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
- This entry is the **mechanism-side co-target** of the residual task E in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../logbook/2026-05-04-bbo-cw-uv-lidt-task.md). Same adjacent-wavelength caveat as `KD-UV280-005`: mechanism evidence is at 266 nm (Sony Cz-BBO programme, Kumar 2015) and the functional form is wavelength-scalable; absolute coefficients depend on the BBO transparency-edge structure (cf. Kubota 1998 absorption-tail-near-230 nm).
- [P:Kubota1998] **Two-mechanism damage-probability model `p(E) = C exp(−K / E)`.** Eqs. 6-7 fit the same functional form to the CW (266 nm, 260 W / cm² average UV intensity) and pulsed (266 nm, 31 MW / cm² peak) regimes with disjoint parameter sets. CW: C₂ = 2.1 × 10⁻¹⁷, K₂ = 50 kV / mm (corresponding to 550 W / cm²). Pulsed: C₁ = 3.5-6.5 × 10⁻¹¹ (sample-dependent), K₁ = 7 MV / m (corresponding to 11 MW / cm²). The ratio `C₂ / C₁ ≈ 10⁻⁶` at fixed |E| is interpreted as evidence of a **transition from thermal excitation (CW low-power regime) to multiphoton excitation (pulsed high-power regime)** in the electron-supply step of the local-avalanche optical-breakdown chain. Sample-to-sample variation (factor 2 in C₁ at constant K₁ across two pulsed samples) suggests C reflects scattering-centre density and K reflects an intrinsic field threshold.
- [P:Kubota1998] **HeNe tomographic image after pulsed 266 nm operation (Fig. 5).** Increased crystal defects observed along the *generated UV* propagation direction, **not** along the input *532 nm* direction. Authors conclude damage is induced primarily by the 266 nm UV, ruling out the green pump as the dominant degradation actor. **The cleanest published single-paragraph evidence that UV (not visible pump) drives BBO surface failure** in Friedenauer-class quadrupling-cavity operation. Anchored in `[P:Kubota1998]` (Sec. Discussion, Fig. 5) and corroborated by `[P:Kumar2015]` (Sec. 6, asymmetric heating: output-face temperature 50 % higher than input-face).
- [P:Kondo1998] **Sub-linear |E|-scaling of degradation rate.** Empirical Fig. 4 fit `δ̇_cav [%/h] = 2.806 × 10⁻⁶ × (P_UV / A [W / cm²])^0.566` (R = 0.98272) gives a sub-linear exponent (0.566) consistent with Kubota 1998's "approximately the 0.5th power of the generated UV power density" framing — i.e., `δ̇ ∝ |E|`, not `∝ I`. Authors propose two candidate mechanisms: (i) UV optical-electric-field disorders the spontaneous-polarisation direction of the BBO, increasing scattering loss; or (ii) UV field increases crystal defects via avalanche breakdown, also increasing scattering loss. Both are bulk / surface-defect models; neither is uniquely identified by the data.
- [P:Kumar2015] **Temperature-dependent TPA and colour-centre formation.** TPA coefficient at 266 nm: β(22 °C) = 3.9 cm / GW, β(100 °C) = 2.0 cm / GW, β(200 °C) = 1.1 cm / GW. Defect-absorption cross-section σ_4ω = 8 × 10⁻¹⁷ cm². Relative colour-centre density at the maximum tested 45.7 MW / cm² UV intensity reduces by 44 % at 100 °C and 69 % at 200 °C compared to room temperature. **The coupled TPA / colour-centre formation is the proximate microscopic mechanism behind the Kubota / Kondo CW-degradation observations.** Direct surface-temperature measurement decouples green-only (1.3 K rise per 8.3 W incident green) from UV-only (1.3 K rise per 1.2 W generated UV) contributions; UV-driven heating is ~ 4 × stronger per unit power. Asymmetric thermal gradient with output face 50 % hotter than input face confirms UV-driven mechanism.
- [S:Turcicova2022] **Mechanism vocabulary anchor.** Intrinsic mechanisms: electrostriction, hyper-sound generation by stimulated Brillouin scattering, electron impact ionisation, photoionisation. Extrinsic mechanisms: laser-induced heating via absorbing inclusions, surface-polishing residuals, sub-micron polishing-material inclusions, residual scratches that intensify the local optical-electric field. Dynamic-colour-centre lifetime in BBO is on the 1-100 ms scale; centres bleach between pulses at < 100 Hz repetition rate but accumulate at higher rates. Manenkov 2014 (Optical Engineering 53, 010901) is the canonical theoretical reference. `[S]`-tier: must accompany a `[P]` mechanism anchor (Kubota 1998 + Kumar 2015).
- TODO: cite Negres et al. 2010 (Opt. Express 18, 19966) — the prior-art reference Hemmerling 2011 cites for the fused-silica UV-damage threshold framing; not retrieved in the 2026-05-06 cluster but available via the Hemmerling reference chain.
- TODO: cite institutional UV-degradation working notes 2026-04 as [I] when they exist.

**Outcome classification:** **Operationally bounded** — UV-driven (not green-driven) failure mechanism is established by the joint Sony Kondo / Kubota 1998 + Kumar 2015 evidence; the empirical degradation-rate scaling `δ̇ ∝ |E|` and the unified `p(E) = C exp(−K / E)` damage-probability model bracket the operational regime; the thermal-excitation → multiphoton-excitation transition explains the 10⁶ scaling between CW and pulsed regimes; temperature-dependent TPA / colour-centre formation provides the proximate microscopic mechanism. Open items: institutional [I] record from MPQ Garching / AG Schätz Freiburg, and a direct mechanism-continuity argument from 266 nm (Sony) to 280 nm (Friedenauer-class). Status: **POPULATING**.

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
- This entry shares its primary evidence cluster with `KD-UV280-008` (HR / OC / AR coating selection) but tracks coating *durability over time* under CW exposure, distinct from the up-front coating *selection* question.
- [P:Kondo1998] **BBO AR-coat damage as the dominant failure mode in Friedenauer-class operation.** Fig. 6 (HeNe microscope image, 160× magnification) shows elliptical damage trace on the BBO AR-coat surface after 100 mW UV operation at w₀ = 23 μm (the prior Oka 1995 short-waist condition). The ellipse elongation is along the BBO walk-off direction (ρ = 4.88°). At the Sony 1200-h reliability point with w₀ = 46 μm, no such damage is seen — i.e., the AR-coat is the *first failure mode to manifest* when intensity is increased above ~ 200 W / cm². **Operational implication for 280 nm: the AR-coat lifetime, not the BBO bulk lifetime, is the binding constraint at the design intensity.**
- [P:Kumar2015] **AR-coat exit-face damage at 266 nm — same failure mode at the thermally-quasi-CW operating point.** Long-term operation at 200 °C, 1.5 → 1 W UV over 16 hours: "AR coating damage on the exit face of the crystal after sufficiently long-term operation at high power. The improvement in long-term stability could be attributed to the reduced two-photon absorption coefficient, and hence the dynamic color center formation, at high temperatures." **No damage in the BBO bulk** — failure is consistently localised at the UV-exit-face AR coating, recoverable by translating the crystal to a fresh spot. This is the *same failure mode* as Kondo 1998's BBO surface degradation at the same wavelength.
- [P:Burkley2021] **AR-coat damage on the CLBO doubling-cavity output coupler at 244 nm.** Slow degradation (1-2 % / hour total power loss) over 12 hours of > 1 W operation is attributed to "damage on the 244 nm coating of the output coupler, visible by eye upon inspection. The power can be recovered by moving to a new spot on the output coupler." **The translate-to-fresh-spot recovery protocol is identical to Kondo 1998 and Kumar 2015** — a robust three-paper agreement on the failure mode and its mitigation across 244, 266, and (transitively) 280 nm.
- [P:Hemmerling2011] **CW UV surface damage on auxiliary fused-silica components in a 280 nm Mg⁺ system.** Reported at 32-64 W / cm² over a few hours on first reflecting surfaces. **This is the only published 280 nm-specific CW UV surface-damage threshold available** — adjacent-wavelength caveat does NOT apply. Mitigation: re-design layouts so that focused spots are inside crystals, not at glass / air or glass / coating interfaces. Cf. `KD-UV280-008` for the same paper's contribution to coating-material selection.
- [P:Brown2019] **Bandgap-dependent durability under contamination.** The capping-layer-ineffectiveness result rules out simple silica-overcoat protection of low-bandgap films; multi-μm overcoats only become effective at mm-thick scales (i.e. via the bulk substrate, not the coating). Material-selection ranking under contamination: silica > alumina > hafnia > tantala > niobia > titania. **For 280 nm AR coatings, this argues against multi-layer stacks with low-bandgap top layers.**
- [S:Turcicova2022] **AR-coating LIDT lowering for multi-wavelength stacks.** BBO AR-coated for 532 + 266 nm dual-wavelength using HfO₂ + Al₂O₃ + SiO₂ multilayer: LIDT ~ 1 GW / cm² (likely non-premium-grade crystal). The dual-wavelength AR LIDT was the same as AR @ 266 nm-only and 20 % lower than AR @ 532 nm-only; multi-layer coatings are more delicate than single-layer counterparts due to interlayer-adhesion sensitivity. **Operational implication: the Friedenauer-class 559 + 280 nm dual-wavelength AR is intrinsically more vulnerable than a 280-nm-only AR.** Also: deposition method matters (IBS > magnetron > e-beam > pulsed laser); mixture coatings (ZrO₂ / SiO₂ gradient) outperform discrete-layer coatings at 355 nm.
- TODO: cite swap-test or witness-mirror methodology papers (Brown 2015 protocol — laser conditioning of contaminated optics — is a candidate but not yet extracted; if pursued, create `data/literature/Brown2015/`).
- TODO: cite institutional coating records as [I] when they exist.

**Outcome classification:** **Operationally bounded** — UV-exit-face AR-coat damage is the consistent first failure mode across three CW deep-UV studies (244, 266, 280 nm) with a translate-to-fresh-spot recovery protocol; bandgap-dependent durability and multi-wavelength-AR-coating LIDT lowering provide the material-selection rationale. Witness-mirror / swap-test methodology and institutional coating records remain TODO. Status: **POPULATING**. Couples to §8.6 partition method validation in Phase 2.

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
- [P:Friedenauer2006] Yb-fibre 1118 nm pump (2006-era commercial source): 2 W single-frequency at 1118 nm with linewidth < 200 kHz, accompanied by 1.2 W broadband ASE peaked between 1060 and 1100 nm (not resonant with the SHG cavity mode). Tunable via piezo-controlled optical path length over an 80 GHz scan range with 20 kHz actuator bandwidth. Optical isolator (designed for 1064 nm) provides ~ 90 % transmission at 1118 nm with ~ 30 dB isolation. Structured extraction: [`data/literature/Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml).
- [P:Friedenauer2006] Polarisation drift behaviour for the fibre-amplifier source: settling time ~ 2 hours after amplifier turn-on if the non-PM fibre is mechanically fixed; residual drift attributed to heat-sink temperature changes can degrade isolator transmission. Mitigation candidate proposed by the authors: active heat-sink temperature stabilisation using a Peltier element. This characterises **one** failure mode of family 1 not present in (or attenuated in) VECSEL alternatives, per CHARTER §3 *open-for-redesign* pump-laser source row.
- [P:Hemmerling2011] **Yb-fibre at 1118.21 nm — Koheras Boostik Y10 / Menlo Systems "orange one-1".** 1 W output, line width < 70 kHz (specified). Half the output power of the Friedenauer 2006 source, sufficient to drive the Friedenauer-class architecture to 60 mW UV at 280 nm. Documents that commercial Yb-fibre lasers at the 1118 nm operating point have been available with < 70 kHz linewidth since at least 2010. Structured extraction: [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml).
- [S:Hume2010] NIST Boulder Wineland-group thesis describes the Mg-Raman 1120 nm Yb-fibre laser as "similar to the Al⁺ laser systems" — i.e., a home-built Yb-doped fibre amplifier pumped with 4 W laser-diodes at 976 nm, with a master at 1120 nm. The 2 nm offset from Friedenauer's 1118 nm is operationally insignificant for the LBO + BBO chain. `[S]`-tier source. Structured extraction: [`data/literature/Hume2010/extracted.yaml`](../data/literature/Hume2010/extracted.yaml).
- [P:Burd2016] **VECSEL CW single-frequency near 1117 / 1141 nm — primary `[P]`-tier anchor for the VECSEL pump option.** Two architectures characterised: (i) externally-frequency-quadrupled VECSEL at 1117 nm IR (3 ± 0.1 W, slope efficiency 19 ± 1 %) — externally doubled in fiber-coupled QPM lithium niobate waveguide → 559 nm (260 mW) → BBO buildup cavity → 280 nm (23 mW); (ii) intracavity-frequency-doubled VECSEL with intracavity LBO at 1141 nm IR → 571 nm (1.2 W per output beam) → BBO buildup cavity → 285 nm. Linewidth 50 ± 10 kHz from electronic Hänsch-Couillaud error signal (comparable to fiber laser and ECDL by three-cornered-hat measurement). RIN at 280 nm < −75 dBc / Hz above 10 kHz. **In this architecture the LiNbO₃ waveguide doubler — not the BBO 280 nm stage — is the bottleneck for power scaling**, a divergence from the Friedenauer-class assumption. Polarisation-drift behaviour is not characterised in this paper but is intrinsically attenuated relative to Yb-fibre by the absence of a non-PM fibre delivery stage. Structured extraction: [`data/literature/Burd2016/extracted.yaml`](../data/literature/Burd2016/extracted.yaml). Couples to `KD-UV280-001`.
- TODO: cite contemporary Yb-fibre amplifier vendor specs (NKT, IPG, Toptica) at 1118 nm with > 5 W single-frequency, post-2010 — the Hemmerling 2011 source is at 1 W; the Friedenauer 2006 source is at 2 W; reaching the §2 indicative ≥ 500 mW UV target needs higher pump power.
- TODO: cite Wilson et al. SPIE 9349 (2015) — referenced from Burd 2016 for the BBO buildup-cavity design details that are not given in the Burd 2016 paper itself.
- TODO: cite literature directly comparing VECSEL polarisation behaviour vs Yb-fibre polarisation drift in the context of intracavity SHG.

**Outcome classification:** **Operationally bounded** — Yb-fibre 1118 nm pump bounded by Friedenauer 2006 (2 W) + Hemmerling 2011 (1 W) + Hume 2010 (NIST 1120 nm). VECSEL-near-1118 nm bound established by `[P:Burd2016]` at NIST Boulder (3 W IR at 1117 nm via externally-doubled architecture; 23.6 W IR at 1141 nm via intracavity-doubled architecture). Both architectures reach the 280 nm UV operating point with comparable linewidth (≤ 70 kHz). Direct VECSEL-vs-Yb-fibre polarisation-drift comparison and post-2010 Yb-fibre vendor specs at higher single-frequency power remain TODO. Status: **POPULATING**.

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
