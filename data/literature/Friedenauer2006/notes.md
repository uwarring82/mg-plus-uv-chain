# Friedenauer2006 Extraction Notes

**Citation:** A. Friedenauer et al., *Applied Physics B* **84**, 371-373 (2006), DOI: `10.1007/s00340-006-2274-2`.

**Source used:** local user-library PDF, not committed to the repository (Springer-Verlag © 2006; this repository is publicly licensed under CC / MIT per [`/LICENSES.md`](../../../LICENSES.md), so redistribution of the publisher PDF is not allowed). The PDF was provided in-conversation on 2026-05-04 for direct verification of the 2026-05-04 extraction pass; it is **not** committed to the repo.

## Extraction Scope

This extraction supports KD-UV280-013, the reference-baseline entry for the Charter v1.0 source comparison. It records values that are explicitly reported in the paper or directly tied to the paper's summary table.

The extraction is a Phase 1 literature artefact only. It is not architecture-family-specific simulation and does not close G1, G2, or G3.

## Extraction Passes

- **2026-05-01 (Codex, DRAFT).** Initial extraction of Sections 2-6 + Table 1. Captures source, two SHG cavity geometries (lengths, focusing-mirror separations, folding angles, mirror reflectivities, BK-derived waists), conversion efficiencies, stability/temperature observations, the 14-GHz unlockable domain, and the iodine reference.
- **2026-05-04 (assistant under steward direction, DRAFT).** Targeted re-read of §3 to fill gaps surfaced by [`/notebooks/2026-05-01-friedenauer-bk-recalculation.py`](../../../notebooks/2026-05-01-friedenauer-bk-recalculation.py) §8:
  - **§8 item 3 (cavity mirror radii)** — closed. `LBO_focusing_mirror_focal_length` = 25 mm directly extracted from §3 ("two curved mirrors of focal length f = 25 mm are used"). `BBO_focusing_mirror_focal_length` = 25 mm extracted by paper-stated equivalence ("the layout of the second cavity is similar to the first, differing only in the reflectivities of the mirrors and the folding angle"). Both values now suffice to drive `src.abcd.cavity_eigenmode_q` against this geometry.
  - **§8 item 5 (d_eff)** — partially closed. `deff_LBO_at_1118` = 0.84 pm/V extracted from §3 (paper attributes to SNLO). `deff_BBO_at_559_typeI` is **not** given by Friedenauer 2006 and remains pending; this is now an explicit `open_extraction_items` entry.
  - **Alternative-crystal context** — added `deff_alternatives_KNB_at_1118`, `deff_alternatives_LNB_at_1118`, `T_NCPM_KNB_alternative`, `T_NCPM_MgOLNB_alternative` to record why the authors chose LBO over the higher-d_eff niobates (NCPM-temperature constraint).
  - **Cavity locking and servo bandwidth** — added `cavity_locking_scheme` (Hänsch-Couillaud, ref [6]) used for both cavities, plus `LBO_M2_piezo_model` (Thorlabs AE020304D04 stacked piezo on a lead disk) and `LBO_M2_piezo_resonance_loaded` ≈ 18 kHz (bounds the achievable servo bandwidth).
  - **Provenance entries** — added `LBO_BK_waist_realisation` (the 27.3 µm waist was *realised* by tuning the focusing-mirror separation onto the cavity's stability plateau, not as a free parameter) and `LBO_optimum_crystal_length_origin` (the 18 mm length is *optimised against the cavity loss budget*, not vendor stock). These provenance entries matter when re-running the optimisation under alternative loss budgets in Phase 3.
  - **`unlockable_domain_width_consistency` cross-check** — confirmed against the original PDF that the 14 GHz width and the 1118.339 nm to 1118.409 nm bounds (Δλ = 70 pm → Δν ≈ 16.8 GHz) are stated verbatim in §4 in adjacent sentences. The discrepancy is **in the source paper itself**, not an extraction error. Cross-check note updated accordingly.

## Review Notes

- The paper gives enough information to resolve the baseline output, conversion efficiencies, cavity dimensions, mirror reflectivities, crystal dimensions, stability observations, and the 14-GHz unlockable domain. After the 2026-05-04 pass, it now also gives focusing-mirror focal lengths (LBO direct, BBO transitive) and `d_eff` for LBO at 1118 nm.
- The paper does not provide the exact BBO cut angle, coating vendor, UV coating lifetime, 280-nm CW LIDT, RIN spectrum, phase-noise spectrum, BBO d_eff at 559 nm, BBO walk-off angle ρ, refractive indices, or an ion-side loss budget. The Sellmeier-derived constants (n_LBO(1118), n_BBO_o(559), ρ_BBO at the 559→280 nm Type-I phase-matching angle) and BBO d_eff are the binding upstream uncertainties for the BK / ABCD recomputation; they belong in `KD-UV280-005` and `KD-UV280-007 Section C`.
- The 14-GHz anomaly remains mechanistically unresolved in the paper. For CHARTER §8.1, Friedenauer2006 is evidence for the observed domain, not attribution.
- The same-vendor note for the tested crystals is captured as vendor/batch sensitivity, but it is not enough by itself to infer a vendor-specific mechanism.

## Downstream Dossier Links

- KD-UV280-001: establishes that a single-source 1118 -> 559 -> near-280 nm quadrupling route produced 275 mW CW UV.
- KD-UV280-005: contributes BBO use case, BBO crystal dimensions, 50 degC operating condition, and vendor/batch sensitivity note.
- KD-UV280-010: primary evidence for the 14-GHz unlockable domain.
- KD-UV280-013: baseline parameter extraction.
- KD-UV280-015: evidence for the 1118-nm Yb fibre pump, linewidth, polarization drift, and proposed heat-sink stabilization mitigation.
