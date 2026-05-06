# Hemmerling2011 Extraction Notes

**Citation:** B. Hemmerling, F. Gebert, Y. Wan, D. Nigg, I. V. Sherstov, and P. O. Schmidt, "A Single Laser System for Ground-State Cooling of ²⁵Mg⁺," *Applied Physics B* **104**, 583-590 (2011), DOI: `10.1007/s00340-011-4472-9`. Affiliations: ¹QUEST Institute for Experimental Quantum Metrology, PTB Braunschweig (Hemmerling, Gebert, Wan, Nigg, Sherstov, Schmidt), ²Institut für Quantenoptik, Leibniz Universität Hannover (Schmidt), ³Universität Innsbruck (Nigg, present address).

**Source used:** open-access arXiv preprint copied on 2026-05-06 to ignored path `downloads/literature/task-e/Hemmerling2011_arxiv_open.pdf` (arXiv:`1010.5664v2`, 22 Feb 2011).

## Scaffold author-list correction

The Task E scaffold (committed in `74d4e86`) noted that the scout-pass author guess "included U. Warring among the authors". Direct read of the arXiv PDF on 2026-05-06 confirms **U. Warring is NOT on this paper**. The actual author list is Hemmerling, Gebert, Wan, Nigg, Sherstov, and Schmidt (PTB Braunschweig / Hannover / Innsbruck). The Steward has no direct authorship on this paper; the scaffold note speculating co-authorship is corrected here. The architecture is the closest published descendant of Friedenauer 2006 (PTB Schmidt-group ↔ MPQ Schaetz-group lineage, with Friedenauer 2006 cited as ref [25]).

## Why this paper

Identified in the second scout pass as a trapped-ion application paper directly relevant to the Friedenauer-class architecture. The `[P]`-tier value for Task E goes well beyond the architecture corroboration: the paper reports **explicit CW UV-induced damage on UV-grade fused-silica optical components** (AOM-cathetus prism / mirror surfaces) at intensities of 32-64 W / cm² over a few hours, with a re-design solution that avoids foci near optical surfaces. This is the most direct published CW UV (~280 nm) damage threshold on fused-silica and dielectric mirror surfaces in a Friedenauer-class architecture, and it is in the operationally relevant intensity range for `KD-UV280-008` and `KD-UV280-012`.

## Extraction Scope

The 2026-05-06 pass extracts:

- §1 introduction: Mg⁺ trap motivation and prior-art reference list including Friedenauer2006 [25].
- §2.1 solid-state laser system for magnesium: full architecture chain (Yb-fiber Koheras Boostik Y10 at 1118.21 nm, <70 kHz linewidth, 1 W → LBO 4×4×18 mm³ NCPM Type I bow-tie cavity → ~450 mW @ 559 nm → 9.2 GHz EOM (Laser 2000 NFO-4851-M) → BBO 3×3×10 mm³ Brewster-cut critical Type I bow-tie cavity → ~60 mW @ 280 nm). Both cavities Hänsch-Couillaud locked.
- §2.1 detail on the AOM double-pass setup and the **CW UV-induced damage observation**: ~5 mW UV beam focused to 50-70 μm waist at prism / mirror surfaces produced 32-64 W / cm² intensity; degradation of beam shape and significant transmission decrease over a few hours; attributed to UV-induced damage on the first reflecting surfaces hit. Cited prior-art reference [29] = Negres et al. 2010 (Opt. Express 18, 19966) on UV-ns-irradiation damage of fused silica. Re-design avoiding foci near optical surfaces (Fig. 2).
- §2.1 ionization laser: Toptica DL pro at 1140 nm, frequency-quadrupled via two cascaded SHG cavities (LiNbO3·MgO doped from HG Photonics, then BBO from Castech) PDH-locked, ~300 µW at 285 nm.
- §2.2 ion trap: linear Paul trap, 23.81 MHz RF, 7 W RF power, helical resonator, ω_axial ≈ 2π × 1.9 MHz, ω_radial ≈ 2π × 2.3 MHz.
- §2.3 state initialization: Doppler cooling at saturation intensity ~250 mW / cm² (relatively low intensity cf. the surface-damage threshold).
- §3-4 ground-state cooling: ⟨n⟩ = 0.03 ± 0.01 axial, 0.02 ± 0.01 after off-resonant correction.

## Extraction Passes

- **2026-05-06 (assistant under steward direction, DRAFT).** Initial full-body extraction. Author-list correction logged. Status promoted from `SCAFFOLD` to `DRAFT`.

## Review Notes

- **The CW UV surface-damage observation is the headline Task-E result.** §2.1 paragraph 5 reports that two AOM double-pass configurations — one using a polarization-rotated retro-reflection through a 90° polarization rotation, and one using a cat's-eye / right-angle prism — both showed UV-induced damage on the *first reflecting surfaces hit by the laser beam*. The damaged surfaces were UV-grade fused silica AOM crystals, mirror surfaces, and a right-angle-prism cathetus (= the right-angle face). Operating intensity: ~5 mW focused to 50-70 µm waist = 32-64 W / cm². Degradation timescale: a few hours. **Implication: UV-grade fused silica components are vulnerable to surface degradation at ~30-60 W / cm² CW intensity at 280 nm; this is in the same operational range as the Friedenauer-class intracavity intensities and one should expect the same vulnerability on cavity mirrors, prisms, and AR-coated windows.**
- **Mitigation by avoiding foci near optical surfaces.** The re-designed AOM double-pass (Fig. 2) uses lenses to translate beams without focusing near any reflecting surface. Operating intensity at the AOM crystal is presumably similar in W / cm² but the *focus* is in the AOM itself rather than at a glass / air or glass / coating interface. **Implication: surface damage thresholds are significantly lower than bulk damage thresholds; designing optical layouts so that focused spots sit inside crystals rather than on reflecting surfaces is a directly transferable mitigation lever.**
- **Architecture matches Friedenauer 2006 with refinements.** Same fundamental wavelength (1118 nm), same intermediate (559 nm), same target (280 nm); same Hänsch-Couillaud locking on both cavities; same crystal types (LBO, BBO); same Type-I phase matching; same Brewster-cut BBO. Differences vs Friedenauer 2006: smaller LBO (4×4×18 mm³ vs Friedenauer's 4×4×18 mm³ — actually the same); smaller BBO (3×3×10 mm³ vs Friedenauer's 4×4×10 mm³); 60 mW UV output vs Friedenauer's 275 mW (Hemmerling uses lower input pump power, 1 W vs 2 W at 1118 nm); novel 9.2 GHz EOM between cavities for Doppler / Raman switching.
- **Vendor information for Friedenauer-class crystals.** LBO from Castech (Crystals Inc., China); BBO from Döhrer Elektrooptik (Germany). Different vendors than Friedenauer 2006's Crystals of Siberia. **Useful for the §5 Phase 1 vendor-comparison concern in `KD-UV280-005`.**
- **No operational-lifetime data on the BBO cavity itself.** The paper reports that the cavities are Hänsch-Couillaud locked and gives output powers, but does not state a long-term-stability number, a degradation-rate observation, or a maintenance-schedule note for the BBO doubling cavity. This is a missing institutional `[I]` record for `KD-UV280-005` Section C.
- **EOM thermal-deflection observation.** When driven at >1.3 W RF power, the EOM crystal exhibits significant beam deflection on switching, attributed to thermal effects in the EOM crystal. Operationally interesting but not directly relevant to BBO-stage damage.
- **The 285 nm photoionization stage.** Implements 285 nm via cascaded SHG of a 1140 nm diode laser through LiNbO3·MgO and BBO buildup cavities. ~300 µW at 285 nm sustained for routine operation. No degradation issues noted at this lower power level.

## Downstream Dossier Links

- `KD-UV280-001`: single-source quadrupling demonstrated. Hemmerling2011 corroborates the Friedenauer 2006 architecture family at 60 mW UV output, with refinements (EOM, Hänsch-Couillaud on both cavities).
- `KD-UV280-005`: BBO at 280 nm — phase-matching, walk-off, damage threshold. Hemmerling2011 contributes BBO crystal vendor (Döhrer Elektrooptik) and dimension (3×3×10 mm³ Brewster-cut Type I) datapoints distinct from the Friedenauer Crystals of Siberia samples.
- `KD-UV280-008`: cavity-mirror / AR-coating selection. Hemmerling2011 contributes the **CW UV-induced damage threshold on UV-grade fused silica surfaces at 32-64 W / cm² over a few hours** — a directly transferable Section C constraint for surface choices.
- `KD-UV280-009`: gas-environment dependence. No direct contribution; the paper does not specify cavity gas environment beyond "vacuum chamber" for the ion-trap side.
- `KD-UV280-011`: UV-induced BBO degradation mechanism. Hemmerling2011 contributes the surface-damage observation on fused silica (not on BBO directly), reinforcing the operational distinction between bulk and surface failure modes (cf. Kondo1998, Kubota1998).
- `KD-UV280-012`: AR-coating durability. Hemmerling2011 directly motivates the "design beam path to avoid foci near reflecting surfaces" rule, applicable to cavity HRs, AR-coated windows, and prisms.
