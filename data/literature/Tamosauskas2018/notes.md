# Tamosauskas2018 Extraction Notes

**Citation:** G. Tamošauskas, G. Beresnevičius, D. Gadonas, A. Dubietis, *Optical Materials Express* **8**, 1410-1418 (2018), DOI: `10.1364/OME.8.001410`.

**Source used:** open-access PDF (OSA Open Access Publishing Agreement), provided in-conversation 2026-05-04. The OA licence permits redistribution with attribution; nonetheless, the convention in this dossier is to **not** commit publisher PDFs to the repository and instead carry forward the structured extraction.

## Why this paper

Task A in [`logbook/2026-05-04-bbo-alternative-references.md`](../../../logbook/2026-05-04-bbo-alternative-references.md). Designated as the modern Sellmeier reference for BBO: refined three-oscillator dispersion equations valid over the entire BBO transparency range (0.188 – 5.2 µm), substantially extending the Eimerl 1987 anchor range (212.8 – 1064 nm) at both ends. The paper combines direct refractive-index measurements from the literature (Chen 2012 book, Kato 1986 fitting rule down to 204.8 nm) with indirect refractive-index extraction from Light Conversion Ltd.'s database of > 600 phase-matching curves and the authors' own SFG measurements 0.8 – 5.2 µm. The intended use here is to **cross-validate** the Eimerl-anchored derived quantities for the 559 → 280 nm Type-I problem, not to replace them.

## What's extracted

The extraction in [`extracted.yaml`](extracted.yaml) captures:

1. **The refined three-oscillator Sellmeier coefficients** (Eq. 1) for both `n_o` and `n_e`, with explicit functional form `n²(λ) = 1 + Σ A_i λ²/(λ² − C_i)` (three oscillators each: two in the UV at C ~ 10⁻² µm² and one in the IR at C ~ 60 µm² for the ordinary, ~ 263 µm² for the extraordinary). Validity range 0.188 – 5.2 µm.
2. **Derived 559 / 280 nm indices, θ_PM, and walk-off ρ** for direct cross-check against the Eimerl-anchored values:
   - `n_o(559) = 1.67186` vs Eimerl 1.67276 (Δ = −9 × 10⁻⁴)
   - `n_e(559) = 1.55314` vs Eimerl 1.55394 (Δ = −8 × 10⁻⁴)
   - `n_o(280) = 1.74445` vs Eimerl 1.74454 (Δ = −1 × 10⁻⁴)
   - `n_e(280) = 1.60391` vs Eimerl 1.60514 (Δ = −1.2 × 10⁻³)
   - `θ_PM(559→280, Type I) = 44.28°` vs Eimerl 44.21° (Δ = +0.07°)
   - `ρ(280 nm at θ_PM) = 83.8 mrad` vs Eimerl 83.1 mrad (Δ = +0.7 mrad)
3. **The predicted `n_o = n_e` crossover at 4.62 µm** (BBO becomes positive-uniaxial above this wavelength), experimentally verified in the paper via crossed-polarizer transmittance (Fig. 4). Eimerl 1987 Sellmeier extrapolation predicts the crossover at 5.75 µm and Chen 2012 book at 5.66 µm — both deviating from the 4.62 µm value that Tamošauskas verified directly. Not relevant to 559 → 280 nm but a useful cross-set discriminant for any mid-IR architecture work.
4. **A cross-set discrepancy entry** logging the ~8 × 10⁻⁴ uniform offset between Tamošauskas Eq. (1) and Eimerl 1987 Table I direct measurements in the visible. Tamošauskas reports their fit matches the Chen 2012 book Table direct measurements to better than 4 × 10⁻⁵, so the discrepancy is between the Eimerl 1987 anchor measurements and the Chen 2012 book anchor measurements, not in the fit.

## What this changes in the dossier

- **`KD-UV280-005` Section C** gains `[P:Tamosauskas2018]` as a parallel Sellmeier anchor alongside `[P:Eimerl1987]`. The two are *both* recorded — not one replacing the other — because:
  - The two sets agree on the operationally relevant derived quantities (θ_PM, ρ) at the 0.1° / 1 mrad level, well below crystal-cut tolerances.
  - The two sets disagree on absolute indices at the ~10⁻³ level in the visible. This affects Fresnel reflection coefficients, cavity ABCD eigenmode calculations (only weakly), and intracavity power balance — all sub-percent effects on conversion efficiency.
  - The Tamošauskas set is more recent and validated against a wider data set; it is the appropriate primary reference *if a single set must be chosen*. Both are kept here because the Eimerl set has the longer track record and provides a useful sanity-check.
- The `cross_check_notes` block in `data/literature/Eimerl1987/extracted.yaml` is updated to reference the Tamošauskas comparison.
- The §5 Phase 1 evidence-table BBO row's Sellmeier-derived cells (n_o, n_e at 559 and 280; θ_PM; walk-off) carry the Eimerl values as the central numbers with the Tamošauskas values noted as cross-set bracketing.

## What this does **not** change

- The factor-2.17 BBO BK-discrepancy diagnosis in [`notebooks/2026-05-01-friedenauer-bk-recalculation.py`](../../../notebooks/2026-05-01-friedenauer-bk-recalculation.py) §5/§7 is unaffected: the walk-off at 280 nm is 83 ± 1 mrad whether you use Eimerl or Tamošauskas, and the discrepancy is at the cavity-vs-single-pass-BK figure-of-merit level, not at the walk-off-estimate level.
- The d_eff value: Tamošauskas does not measure or report nonlinear coefficients. The d_eff anchor is `[P:Eckardt1990]`, and that is unaffected by which Sellmeier set is used (Eckardt's d_eff extraction depends on the phase-matching geometry, not on the absolute indices, so the < 4 × 10⁻⁴ Sellmeier-set difference at 1064 nm propagates into a < 0.5% change in the Eckardt-extracted `|d_22|`).

## Caveats

1. **The visible-band Sellmeier offset.** Whether Tamošauskas's `n_o(559) = 1.6719` or Eimerl's `n_o(559) = 1.6728` is closer to truth requires a direct measurement at 559 nm — neither paper anchors directly at this wavelength. The Tamošauskas set is anchored to Chen 2012 book Table at adjacent wavelengths (546 nm, 632 nm); Eimerl anchors to its own prism measurements at 546.07 nm. Both anchor sets are themselves prism measurements; the disagreement is between the underlying measurement sets rather than the fits.
2. **Three-oscillator vs Eimerl's two-oscillator form.** Tamošauskas Eq. (1) uses a different functional form than Eimerl Eq. (1). The three-oscillator form has two free oscillators in the UV (which share the burden of fitting the deep-UV behaviour where Eimerl's single-UV-pole form would have to extrapolate). For the 559 → 280 nm problem this means the Tamošauskas form is the more honest interpolation; for the 1064 → 532 nm problem (where the Eimerl set is anchored directly via prism measurements), the Eimerl form is the more direct read.
3. **Open-access status.** The OA licence (CC BY 4.0 via OSA's open-access agreement) does in principle allow redistribution. The dossier convention to keep the PDF outside the repository is for *consistency* across the literature folder — most papers in this dossier are not OA, and uniform handling avoids accidental commits when later non-OA references are added.

## Status

`DRAFT` — Sellmeier coefficients populated and cross-checked at the index level (~8 × 10⁻⁴ uniform offset against Eimerl Table I in the visible), at the derived-PM-angle level (0.07° agreement), and against Tamošauskas's own published cross-check vs Chen 2012 book Table direct measurements (their stated 4 × 10⁻⁵ accuracy is consistent with our recompute).

## Extraction passes

- **2026-05-04 (assistant under steward direction, DRAFT).** Initial full extraction. Captured Eq. (1) Sellmeier coefficients, derived 559 / 280 nm quantities, the 4.62 µm `n_o = n_e` crossover, and the cross-set offset diagnostic against Eimerl 1987 Table I. Companion d_eff extraction (Task B) at [`data/literature/Eckardt1990/`](../Eckardt1990/) was completed in the same session; the two together discharge tasks A and B of [`logbook/2026-05-04-bbo-alternative-references.md`](../../../logbook/2026-05-04-bbo-alternative-references.md).
