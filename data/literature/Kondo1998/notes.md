# Kondo1998 Extraction Notes

**Citation:** K. Kondo, M. Oka, H. Wada, T. Fukui, N. Umezu, K. Tatsuki, and S. Kubota, *Optics Letters* **23**, 195-197 (1998), DOI: `10.1364/OL.23.000195`.

**Source used:** local user-library PDF, copied on 2026-05-06 to ignored path `downloads/literature/task-e/Kondo1998_OpticsLetters_user.pdf`; **not committed to the repository** (Optical Society of America © 1998; this repository is publicly licensed under CC / MIT per [`/LICENSES.md`](../../../LICENSES.md), so redistribution of the publisher PDF is not allowed).

## Why this paper

This is the highest-payoff peer-reviewed candidate from Task E for `KD-UV280-005` and `KD-UV280-009`: a CW 266 nm BBO reliability study with reported >1000 h operation and an explicit degradation-rate vs UV power density curve. It is adjacent-wavelength evidence (266 nm vs the 280 nm Friedenauer-class target), not a direct 280 nm measurement, but it is much closer to the Q2 operational-lifetime question than pulsed single-shot LIDT values, and it is the publication of record for the Sony / Cz-grown BBO programme.

## Extraction Scope

The 2026-05-06 pass extracts the full body of the three-page Letter: cavity geometry, Boyd-Kleinman focusing and walk-off parameters, BBO crystal specifications, operating powers, the round-trip-loss reliability metric and its empirical degradation-rate fit vs UV power density, the comparison with the prior Oka 1995 short-waist experiment, the RIN spectrum, and the two cleanliness controls (N₂ purge; sealed-cavity recommendation).

The extraction is a Phase 1 literature artefact only. Specifically, it does **not** convert the 266 nm reliability evidence into a 280 nm constraint. The adjacent-wavelength mapping decision belongs in `KD-UV280-005 Section C` and must be made explicit there with the search-boundary clause introduced in the [task-E logbook](../../../logbook/2026-05-04-bbo-cw-uv-lidt-task.md) acceptance criteria.

## Extraction Passes

- **2026-05-06 (assistant under steward direction, DRAFT).** Initial full-body extraction from the user-provided PDF. Sections covered: introduction (prior-art context), cavity setup (Fig. 1), round-trip-loss reliability framework (Eqs. 1-3, Figs. 2-3), degradation-rate vs UV power density fit (Fig. 4), RIN measurement (Fig. 5), beam-waist comparison with Oka 1995 (Fig. 6), and cleanliness controls. Bibliographic references resolved against the references list. Status promoted from `SCAFFOLD` to `DRAFT`.

## Review Notes

- **Wavelength caveat.** The headline >1000 h reliability result is at 266 nm, not 280 nm. The mechanism the authors propose (UV-electric-field-driven defect / polarization disordering) is a wavelength-scaling argument the steward must evaluate before the result is mapped onto `KD-UV280-005`.
- **Degradation-rate fit.** Fig. 4 reports `δ̇_cav = 2.806 × 10⁻⁶ × (P_UV/A)^0.566` with R = 0.98272, where the abscissa is UV power density in W/cm² and the ordinate is the round-trip-loss degradation speed in % / hour. The sub-linear exponent (0.566) is what the abstract paraphrases as "proportional to the strength of the UV optical electric field" (since |E| ∝ √I). The fit is captured both as the symbolic relation and as the two anchor data points reported in the text (the w0 = 46 μm and the prior w0 = 23 μm operating points).
- **Three-sample reproducibility.** The >1000 h operation was reproduced "three times in different samples", but the paper does not specify the supplier or growth lots beyond the Czochralski-method statement. The vendor / batch metadata that `KD-UV280-005` Section C wants from `Kubota1998` is not present here.
- **Beam-position rotation.** The "100 mW for >5000 h if we change beam location on the BBO surface" remark is an operational-protocol claim, not a continuous-operation lifetime. Fixed-beam reproducible reliability is 1200 h.
- **Cleanliness controls.** Two distinct controls are reported: (i) N₂ purge at 0.4 L/min during operation; (ii) recommendation that a hermetically sealed cavity would remove the need for the N₂ purge. Oil vapor from mechanical components is named as the dominant contamination source and is explicitly cited as degrading both BBO and mirror coatings.
- **Adjacent-wavelength bibliographic chain.** The paper cites Eckardt 1990 (already extracted as [`Eckardt1990/`](../Eckardt1990/)) for `d_eff` = 1.642 pm/V at 266 nm, used to compute γ_SH = 4.952 × 10⁻⁵ W⁻¹ via Boyd-Kleinman. This is *not* the 559 → 280 nm `d_eff` needed by `KD-UV280-005`; it is the 532 → 266 nm value at the Sony operating angle. Do not import it into 280 nm Section C without an explicit phase-matching-angle conversion.
- **Reference [3] (Oka 1995).** The previous-experiment baseline (w0 = 23 μm, 100 mW for 400 h, 1 W for 8 h, degradation rate 1.35 × 10⁻⁴ % / h) is an `[S]`-tier secondary citation in this extraction. If the steward wants the Oka 1995 numbers as `[P]`, that paper needs its own folder.

## Downstream Dossier Links

- `KD-UV280-005`: BBO at 280 nm — phase-matching, walk-off, damage threshold. Kondo1998 contributes adjacent-wavelength CW operational-lifetime evidence (266 nm at 100 mW UV, w0 = 46 μm, ξ = 0.1434, B = 14.67) and the empirical degradation-rate-vs-UV-power-density fit. Cleanliness controls (N₂ purge, sealed cavity) cross-link to `KD-UV280-009`.
- `KD-UV280-009`: BBO surface degradation and gas-environment dependence. Kondo1998 contributes the explicit oil-vapor / N₂-purge / sealed-cavity narrative and the operational protocol of moving the beam spot.
- `KD-UV280-011`: UV-induced BBO degradation mechanism. Kondo1998 contributes the authors' two competing hypotheses (UV-field-driven disordering of spontaneous polarization vs avalanche-breakdown crystal defects) and the sub-linear empirical scaling that distinguishes the strong-field regime from a thermal-load regime.
