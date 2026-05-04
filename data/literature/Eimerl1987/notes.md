# Eimerl1987 Extraction Notes

**Citation:** D. Eimerl, L. Davis, S. Velsko, E. K. Graham, A. Zalkin, *Journal of Applied Physics* **62**, 1968-1983 (1987), DOI: `10.1063/1.339536`.

**Source used:** local user-library PDF, provided in-conversation 2026-05-04 by the steward; **not committed to repository** (AIP / *J. Appl. Phys.* © 1987; this repository is publicly licensed under CC / MIT per [`/LICENSES.md`](../../../LICENSES.md), so redistribution of the publisher PDF is not allowed). The PDF was used only to extract structured facts; the structured extraction (this folder) is what the repository carries forward.

## Why this paper

Friedenauer 2006 footnote [7] states "All crystal data taken from SNLO program by Sandia National Laboratories." SNLO's BBO data are themselves grounded in the upstream peer-reviewed measurement record; **Eimerl, Davis, Velsko, Graham & Zalkin (1987)** is the most-cited primary source for the BBO Sellmeier coefficients, effective nonlinear coefficients, walk-off, and bulk-thermal properties used across the field. Citing it directly (as `[P:Eimerl1987]`) in `KD-UV280-005 Section C` discharges the dossier rule "Every Section C must cite ≥ 1 peer-reviewed primary [P] source where available" while keeping the chain of provenance to the original measurement record rather than to derived software (SNLO).

## Extraction scope

**Captured in this pass (2026-05-04):**

1. **Crystallography.** R3c space group of low-temperature β-BaB₂O₄, hexagonal cell parameters (a = 12.547 Å, c = 12.736 Å), density (3.840 g/cm³). The R3c space group is what restricts the allowed nonlinear coefficients to `d_11`, `d_31`, `d_33`, `d_15`, with Kleinman symmetry equating `d_15 = d_31`.
2. **Linear optical constants — Table I (direct measurements).** Refractive indices at 13 wavelengths (405 nm to 1014 nm) by minimum-deviation prism spectrometry. Captured in full as the `BBO_refractive_indices_table_I` parameter (with units converted from Å to nm).
3. **Sellmeier coefficients — Table II.** All three sets reproduced in Table II are captured: the "this work" Eimerl 1987 set (`BBO_sellmeier_*_eimerl1987`, the recommended set), the Chen 1985 set (recorded as `BBO_sellmeier_alternative_chen1985` and explicitly **DEPRECATED** because Eimerl 1987 Table VI shows it predicts the 1064→532 Type-I PM angle 3° low), and the Kato 1986 set (recorded as `BBO_sellmeier_alternative_kato1986` and noted as a useful sanity-check comparator).
4. **Thermo-optic coefficients.** Wavelength-averaged values (Eqs. 2-3) are captured; the per-wavelength Table IV measurements at 1014, 579, 405 nm informed the averaging but are not separately committed (the dispersion is comparable to measurement precision).
5. **Transparency window.** 200-3000 nm clear range, 215 nm UV onset, 100%/cm extinction at 200 nm. 280 nm is well inside the window (~65 nm above onset).
6. **Damage threshold.** The 1064 nm / 1 ns / one-on-one bulk threshold of 13.5 J/cm² (inclusion-free regions). Captured **with the explicit caveat** that this is **not** a CW-UV LIDT; the CW-UV photo-induced surface degradation regime is what governs operational lifetime at 280 nm and is not measured in Eimerl 1987.
7. **Nonlinear coefficients.** `d_11` = 1.6 ± 0.4 pm/V (Eq. 14, measured relative to `d_36(KDP)` = 0.39 pm/V). The `|d_22 / d_11|` and `|d_31 / d_11|` < 0.05 bounds (Eqs. 15-16) that pin the d_eff formula. The Type-I `d_eff = d_31 sin θ - d_11 cos θ cos(3φ)` formula (Eq. 17, geometry per Fig. 25).
8. **Thermomechanical.** Anisotropic thermal expansion (α₁₁ = 4×10⁻⁶/K, α₃₃ = 36×10⁻⁶/K) and thermal conductivity (κ₁₁ = 0.08 W/m/K, κ₃₃ = 0.8 W/m/K) — both 9–10× anisotropic — and fracture toughness (150 kPa·m^(1/2)). Relevant to CHARTER §1.5 thermal-load envelope at the UV stage.
9. **Static dielectric constants.** K₁₁ = 6.7, K₃₃ = 8.1, tan δ < 0.001.

**Derived in this pass (computed in `python3` cross-check, recorded as separate parameters with explicit `DERIVED` provenance):**

- `n_o(559 nm)` = 1.67276 and `n_e(559 nm)` = 1.55394 from `BBO_sellmeier_*_eimerl1987`.
- `n_o(280 nm)` = 1.74454 and `n_e(280 nm)` = 1.60514 from same Sellmeier set.
- `theta_PM_559_to_280nm_typeI` = 0.7716 rad = **44.21°**, by solving `n_e(2ω, θ) = n_o(ω)` at λ_fund = 559 nm.
- `rho_walkoff_280nm_typeI` = 0.0831 rad = **83.1 mrad**, via `tan ρ = (1/2) n_e²(2ω, θ) sin(2θ) [1/n_e²(2ω) − 1/n_o²(2ω)]`. The original notebook used 85 mrad as a literature-typical estimate; the Eimerl-anchored value is within 2 mrad and is now used directly.
- `BBO_d_eff_typeI_559_to_280nm` = **1.15 pm/V central** (range 1.09–1.20 across azimuth; ±25% from the d_11 measurement uncertainty), computed at θ_PM = 44.21° with optimum azimuth `|cos(3φ)| = 1`.

**Cross-check that validates the Sellmeier-coefficient interpretation.** The printed Table II column header for the `C` coefficient reads "μm⁻²" but that is dimensionally inconsistent with Eq. (1) `n² = A + B/(λ² + C) + Dλ²`. The canonical interpretation — `C` in μm² with the negative sign as printed — is what reproduces the paper's own Table I direct measurements (RMS deviation < 4×10⁻⁴ over the 13 wavelengths) and Table VI calculated phase-matching angles (1064→532 Type-I: my recompute 22.88° vs paper's calc 22.9° / exp 22.7°; 532→266 Type-I: my 47.43° vs paper's 47.5° calc / 47.3° exp). The Table II column-header units string is therefore a typesetting / OCR artefact, not a physical convention; the extraction commits the physically-correct interpretation and flags this in the parameter notes.

## Out-of-scope at this commit

The full elastic-constants tensor (Table X, all six independent stiffness components plus the dc/dT thermoelastic terms), the threshold-power figures-of-merit calculations across the harmonic-generation processes (Figs. 26-32), the OPA phase-matching curves (Figs. 19-24), the noncritical phase-matching wavelengths for Nd:YAG harmonics (Table IX), and the electro-optic Pockels-cell estimates (Eq. 24, half-wave voltage at 1064 nm) are not currently used by KD-UV280-005 or by the Friedenauer-baseline BK / ABCD recomputation. They are deliberately not extracted in this pass to keep the dossier focused; if a downstream entry (e.g. KD-UV280-002 SFG, or a future thermal-fracture analysis) needs them, the source PDF can be re-consulted in a targeted re-read.

## Status

`DRAFT` — values populated and cross-checked against the paper's own internal consistency (Table I ↔ Table II ↔ Table VI). Promotion DRAFT → final review remains a steward check. The `BBO_d_eff_typeI_559_to_280nm`, `theta_PM_559_to_280nm_typeI` and `rho_walkoff_280nm_typeI` derived parameters are now sufficient to drive the BBO BK / ABCD recomputation in `notebooks/2026-05-01-friedenauer-bk-recalculation.py` against an Eimerl-anchored Sellmeier set rather than against a literature-typical estimate.

## Extraction passes

- **2026-05-04 (assistant under steward direction, SCAFFOLD).** Created bibliographic record. Awaiting PDF provision for the next pass.
- **2026-05-04 (assistant under steward direction, DRAFT).** Full extraction from the steward-provided PDF. Promoted SCAFFOLD → DRAFT. See `extraction_passes` in `extracted.yaml` for the per-pass scope.

## Cross-references

- [`docs/KD-2026-XXX-uv-280nm.md`](../../../docs/KD-2026-XXX-uv-280nm.md) — KD-UV280-005 Section C now cites `[P:Eimerl1987]` with populated values rather than a SCAFFOLD marker; the §5 Phase 1 evidence-table BBO row inherits the values.
- [`notebooks/2026-05-01-friedenauer-bk-recalculation.py`](../../../notebooks/2026-05-01-friedenauer-bk-recalculation.py) — §8 item 2 ("BBO d_eff at 559 nm Type-I — must come from KD-UV280-005 Section C / Sellmeier") is now closed; §8 item 4 (the apparent factor-2.17 BBO BK discrepancy) now uses `rho_walkoff_280nm_typeI` (83.1 mrad) directly, which does not change the order-of-magnitude conclusion that the paper's reported 19.4 µm waist corresponds to a cavity-specific (not single-pass-BK) optimisation criterion.
- [`logbook/2026-05-04-bbo-alternative-references.md`](../../../logbook/2026-05-04-bbo-alternative-references.md) — task draft for surfacing alternative-reference candidates (Tamošauskas et al. 2018 modern Sellmeier, Eckardt et al. 1990 absolute-d_eff calibration, etc.) that would tighten the Eimerl 1987 anchor.

## Schema note

The `BBO_sellmeier_no_eimerl1987` and `BBO_sellmeier_ne_eimerl1987` entries (and the two alternative-set entries) use a **YAML mapping** as the `value` field — `{A, B, C, D}` for the Sellmeier coefficients. This is a slight extension of the `extracted.yaml` schema, which to date uses scalars or lists. The mapping form keeps each Sellmeier set as a single semantically-coherent parameter rather than four loosely-linked scalars; downstream consumers should access as `param['value']['A']`, `param['value']['B']`, etc. The same pattern is used for the Table I direct measurements and the Table III Nd:YAG-harmonic indices (parallel-array layout: `wavelengths_nm`, `n_o`, `n_e`).
