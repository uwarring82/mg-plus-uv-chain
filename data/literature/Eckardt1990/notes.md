# Eckardt1990 Extraction Notes

**Citation:** R. C. Eckardt, H. Masuda, Y. X. Fan, R. L. Byer, *IEEE Journal of Quantum Electronics* **26**, 922-933 (1990), DOI: `10.1109/3.55534`.

**Source used:** local user-library PDF, provided in-conversation 2026-05-04 by the steward; **not committed to repository** (IEEE © 1990; this repository is publicly licensed under CC / MIT per [`/LICENSES.md`](../../../LICENSES.md), so redistribution of the publisher PDF is not allowed).

## Why this paper

Task B in [`logbook/2026-05-04-bbo-alternative-references.md`](../../../logbook/2026-05-04-bbo-alternative-references.md). Designated as the modern absolute-`d_eff` calibration reference for BBO. Eckardt et al. 1990 measure `d_eff(1064 → 532 nm Type I)` directly and then reduce to `|d_22|` using the Type-I phase-matching formula. Their result, `|d_22| = 2.2 pm/V`, is **37% higher** than Eimerl 1987's `|d_11| = 1.6 ± 0.4 pm/V` (the same physical tensor element under different axis conventions), at overlap with only the very edge of Eimerl's ±25% uncertainty envelope. This is the binding upgrade to the BBO conversion-efficiency calculation in `KD-UV280-005` Section C and to any Friedenauer-baseline BK / ABCD recomputation that uses `d_eff`.

## What's extracted

The extraction in [`extracted.yaml`](extracted.yaml) captures:

1. **The headline BBO numbers.** `d_eff(1064 → 532 nm, Type I)` = 1.94 ± 0.07 pm/V (4% reproducibility, ±10% absolute accuracy). `|d_22|` = 2.2 pm/V derived using `|d_31| << |d_22|`. The ratio to `d_36(KDP)` is 5.7 in this work vs 4.1 in Eimerl 1987 — the upward revision is **not** explained by the KDP reference choice (Eckardt uses 0.38 vs Eimerl's 0.39, a 2.6% difference).
2. **The Eckardt-convention d_eff formula** (Table I): `d_eff = d_31 sin(θ + ρ) − d_22 cos(θ + ρ) sin(3φ)`. Two refinements over Eimerl 1987 Eq. (17): (a) the `θ → θ + ρ` walk-off correction (modern convention; from the anisotropic Green's-function treatment in their Appendix), and (b) `sin(3φ)` instead of `cos(3φ)` because of a 30° azimuth offset in the choice of crystallographic *x*-axis. Both formulas refer to the same physical tensor element.
3. **The d_36(KDP) = 0.38 ± 0.005 pm/V calibration reference.** Used to anchor all the absolute measurements in this paper.
4. **Operating-point context for the BBO measurement** (Table II): `θ_PM(1064 → 532, I) = 22.8°`, `ρ = 3.19°`, `n_o(1064) = 1.6545`, `n_e(1064) = 1.5392`, `n_o(532) = 1.6742`, `n_e(532) = 1.5547`. These indices are from Chen 1986 (Eckardt's Ref. 19), not from Eimerl 1987; cross-check with `data/literature/Eimerl1987/extracted.yaml` Sellmeier yields agreement at the < 4 × 10⁻⁴ level on the indices and < 0.05° on `θ_PM`.
5. **Cross-reference d_eff for KD*P, LiIO₃, 5% MgO:LiNbO₃, KTP.** Captured for downstream entries (KD-UV280-006 etc.) but not promoted to KD-UV280-005 anchors.

## What this changes in the dossier

- **`KD-UV280-005` Section C** now carries `[P:Eckardt1990]` as the **central** `d_eff` anchor, with `[P:Eimerl1987]` retained for the Sellmeier set and the tensor-component bounds (`|d_31/d_22| < 0.05`, etc.).
- The §5 Phase 1 evidence-table BBO `d_eff` cell is revised upward from 1.15 (1.10–1.20) pm/V (Eimerl-only) to **1.44–1.58 pm/V** (Eckardt + Eimerl bound on `d_31/d_22`), depending on whether the walk-off correction `θ → θ + ρ` is applied. With walk-off correction (Eckardt's modern convention): central `1.44 pm/V`. Without (the bare Eimerl Eq. 17): central `1.58 pm/V`. Consensus value used in `KD-UV280-005`: **1.44 pm/V central, range 1.30–1.60**, with ±10% from the Eckardt absolute accuracy and a small additional contribution from the `|d_31/d_22| < 0.05` azimuth uncertainty.
- The conversion-efficiency at fixed intensity is `(d_eff/d_eff_old)² = 1.59` higher with the Eckardt anchor (and walk-off correction) than with the bare Eimerl 1987 anchor. This is consistent with the ~50% conversion efficiencies achieved at the LBO stage in modern Friedenauer-class systems.
- The `BBO_d_eff_typeI_559_to_280nm` parameter in `data/literature/Eimerl1987/extracted.yaml` **is not changed** (it correctly records the Eimerl-anchored value); a new parameter `BBO_d_eff_typeI_559_to_280nm_eckardt` is added there or here for the Eckardt-anchored value, with the cross-reference logged in Eimerl's `cross_check_notes`.

## Caveats

1. **Eckardt measures at 1064 nm SHG, not 559 nm SHG.** Transfer to the 559 → 280 nm Type-I configuration assumes the dispersion of `d_22` from 1064 to 559 nm is small. This is the same assumption Eimerl 1987 makes; the upgrade Eimerl → Eckardt is an *absolute calibration* upgrade, not a *per-wavelength dispersion* upgrade. Closing the residual dispersion-assumption uncertainty would require either a direct measurement at 559 → 280 nm or a Miller's-δ-style scaling argument from the linear susceptibilities.
2. **Sign of d_31 in BBO is not determined.** Eckardt explicitly flags this as "unknown for BaB2O4". The d_eff formula at the optimum azimuth is dominated by the d_22 term, so the d_31-sign uncertainty contributes < 5% to `|d_eff|` and does not change the conversion-efficiency conclusion.
3. **The BBO sample mix:** two of the three samples were grown at Stanford (different from the Fujian crystal Eimerl 1987 used), the third was the same Fujian crystal Eimerl used. The 12-measurement reproducibility of ±3.6% across the three samples means the upward revision is not driven by a vendor / batch sensitivity.

## Status

`DRAFT` — values populated and cross-checked against Eckardt 1990's own internal consistency (Table II ↔ Table III via the d_eff formula). Cross-set comparison with Eimerl 1987 Sellmeier and Tamošauskas 2018 Sellmeier indicates the d_eff revision is not driven by phase-matching-geometry uncertainty.

## Extraction passes

- **2026-05-04 (assistant under steward direction, DRAFT).** Initial full extraction. Captured BBO d_eff and d_22 with provenance, the Eckardt-convention formula and 30° azimuth-axis offset, the d_36(KDP) calibration, and the BBO operating-point context. Cross-reference d_eff values for KD*P, LiIO3, MgO:LiNbO3, KTP captured for downstream entries.
