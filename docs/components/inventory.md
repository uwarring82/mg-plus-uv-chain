---
layout: default
title: Optical-components inventory — SHG/FHG shelf
description: Inventory of optical components for the LBO and BBO doubling stages, keyed to the Friedenauer 2006 baseline. Working artefact with verification trail.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local lab inventory — AG Schätz stewardship. Items listed here are pre-existing stock identified from photographs and vendor documentation; their fitness for any specific build is conditional on later inspection (coating verification, scratch/dig, batch consistency).</p>

<p class="eyebrow">Inventory</p>

# Optical-components inventory — SHG/FHG shelf

**Last updated:** 2026-05-07 (initial inventory pass; BBO crystals added the same day from vendor documentation).
**Status:** DRAFT. Working inventory; line-item readings need bench verification before procurement decisions.
**Source documents (referenced for traceability; not committed to repo because they include personal contact data and pricing):**

- Shelf photograph, 2026-05-07 (original 4087 × 3441 px).
- Raicol Crystals *Certificate of Compliance & Tests No. 6331*, 08 Jun 2025.
- EKSMA Optics *Order Confirmation No. 4100143296*, 15 Apr 2025 (delivered Jun 2025).
- A-Star vendor labels (photographed 2026-05-07; PO BL170229 / SO AS171206-01).
- Castech vendor label (photographed 2026-05-07; G8115-2 / Crystal ID 2-21577).
- Raicol *Quotation PQ250167*, 04 Jul 2025 (expired; reference for restocking only).

**Scope.** Maps each identified box / loose item to its likely role in either the **LBO ring cavity** (1118 nm → 559 nm; conventionally labelled here at the coating-stated 1120 nm / 560 nm) or the **BBO ring cavity** (559 nm → near 280 nm) of the [Friedenauer 2006 baseline](friedenauer-baseline.html). The seed-laser layer that feeds the LBO cavity is documented separately under [Seed lasers (VECSEL)](seed-lasers.html); items on this page are downstream of that seed.

---

## Glossary

This document uses the terms and abbreviations listed below. Each entry links to a publicly available reference (Wikipedia or the original-paper DOI) where one exists, so the page is self-contained for readers approaching from outside the laser-cavity world.

**Cavity / mirror terminology**

- **IC** — *Input coupler.* Partial reflector through which the pump beam enters the resonator; reflectivity is chosen to impedance-match the cavity round-trip loss.
- **OC** — *Output coupler.* Partial reflector that lets the desired output (here, the second harmonic) escape the cavity. Often a dichroic: HR at the fundamental, HT at the harmonic.
- **HR** — *High reflector.* [Dielectric mirror](https://en.wikipedia.org/wiki/Dielectric_mirror) with reflectivity typically > 99 %.
- **AR** — *Anti-reflection.* [Multilayer coating](https://en.wikipedia.org/wiki/Anti-reflective_coating) that suppresses surface reflection at a chosen wavelength.
- **PR** — *Partial reflector.* Mirror with intentional sub-unity reflectivity, used as IC or OC.
- **AOI** — *Angle of incidence.* Angle between the beam and the local surface normal; coatings are designed for a specific AOI and degrade off-design.
- **FSR** — *[Free spectral range](https://en.wikipedia.org/wiki/Free_spectral_range).* Frequency spacing between adjacent longitudinal cavity modes; equals `c / L` for a ring of round-trip path `L`.
- **TEM₀₀** — *Fundamental [transverse mode](https://en.wikipedia.org/wiki/Transverse_mode)* — the lowest-order Gaussian cavity mode.
- **HC lock** — *[Hänsch–Couillaud](https://doi.org/10.1016/0030-4018(80)90069-3) polarisation lock* (Opt. Commun. **35**, 441 (1980)). Locks a laser to a passive resonator using polarisation analysis of the reflected light.
- **piezo / PZT** — *[Piezoelectric actuator](https://en.wikipedia.org/wiki/Piezoelectricity).* Displaces a cavity mirror by sub-nm steps for frequency lock or scanning.

**Nonlinear-optics terminology**

- **SHG** — *[Second-harmonic generation](https://en.wikipedia.org/wiki/Second-harmonic_generation).* Frequency doubling: ω + ω → 2ω in a noncentrosymmetric crystal.
- **FHG** — *Fourth-harmonic generation.* ω → 4ω, here implemented as two cascaded SHG stages (1118 nm → 559 nm → 280 nm).
- **CW** — *[Continuous-wave](https://en.wikipedia.org/wiki/Continuous_wave) operation* (non-pulsed).
- **PM** / **NCPM** — *[Phase matching](https://en.wikipedia.org/wiki/Nonlinear_optics#Phase_matching) / noncritical phase matching.* The fundamental and harmonic phase velocities match in the crystal. NCPM removes spatial walk-off and is tuned by temperature; critical PM is tuned by crystal angle. Friedenauer 2006: LBO stage NCPM, BBO stage critical.
- **Type-I PM** — Both fundamental photons polarised parallel (`o + o → e` in a negative-uniaxial crystal). Used in both Friedenauer stages.
- **Brewster cut** — Crystal end-faces cut at [Brewster's angle](https://en.wikipedia.org/wiki/Brewster%27s_angle) so that p-polarised light has zero Fresnel reflection. The BBO Brewster cut at 59.1° external corresponds to the Type-I `θ = 44.4°` internal phase-matching angle for 559 → 280 nm.
- **`d_eff`** — *Effective nonlinear coefficient.* The d-tensor projected onto the field polarisations of the chosen interaction; sets SHG conversion efficiency together with phase matching, focusing, and crystal length.
- **Sellmeier equation** — *[Empirical dispersion fit](https://en.wikipedia.org/wiki/Sellmeier_equation)* `n²(λ) = 1 + Σ Bᵢ λ² / (λ² − Cᵢ)`. Drives both refractive indices and the PM angle.
- **Boyd–Kleinman** — *Focusing analysis for SHG* — [G. D. Boyd & D. A. Kleinman, J. Appl. Phys. **39**, 3597 (1968)](https://doi.org/10.1063/1.1656831). Gives the optimum confocal parameter relative to crystal length.

**Crystal materials and substrates**

- **LBO** — *[Lithium triborate](https://en.wikipedia.org/wiki/Lithium_triborate)* (LiB₃O₅). Borate nonlinear crystal used here for 1118 → 559 nm SHG; broad transparency, modest `d_eff`, very high LIDT.
- **BBO** — *[β-Barium borate](https://en.wikipedia.org/wiki/Barium_borate)* (β-BaB₂O₄). Borate nonlinear crystal used here for 559 → 280 nm SHG; large `d_eff`, hygroscopic surfaces.
- **FS** — *[Fused silica](https://en.wikipedia.org/wiki/Fused_quartz).* Generic UV-grade amorphous SiO₂ substrate.
- **Herasil** — Heraeus fused-silica grade.
- **SQ2** / **Suprasil** — Heraeus high-purity FS grades; UV-transmissive.
- **BK7** / **N-BK7** — Schott [borosilicate crown](https://en.wikipedia.org/wiki/Crown_glass_(optics)) glass; transparent in visible/NIR but **not UV-transmissive at 280 nm**.

**Source / pump terminology**

- **ASE** — *[Amplified spontaneous emission](https://en.wikipedia.org/wiki/Amplified_spontaneous_emission).* Broadband background output from a fibre amplifier; non-resonant with the SHG cavity but contributes thermal load and isolator stress.
- **UV** — *Ultraviolet.* Here meaning the ~ 280 nm output of the FHG chain.

**Coating / measurement terminology**

- **IBS** — *[Ion-beam sputtering](https://en.wikipedia.org/wiki/Sputter_deposition).* Coating-deposition technique producing the lowest-loss dielectric stacks; standard for cavity-grade HRs > 99.9 %.
- **Scratch / dig** — *[Surface-quality specification](https://en.wikipedia.org/wiki/Optical_flat#Surface_quality)* per MIL-PRF-13830B; lower numbers = better surface.
- **Flatness λ/N** — Surface flatness relative to a reference wavelength (commonly 633 nm). Smaller `λ/N` = flatter.
- **`r` / `R`** — Radius of curvature. For a concave mirror at normal incidence the focal length is `f = R / 2`. Sign conventions vary by vendor (concave = negative on some labels, positive on others).

**Provenance tags used in the tables below**

- `O` — label observed directly from photo / vendor document, high confidence.
- `O*` — label partially obscured / handwritten / partial reading; flagged.
- `OPEN` — cannot be read from the source material.

---

## Reading conventions (operational)

The terms above are general-purpose. The following are document-specific:

- **Coating wavelength offset.** Most LBO-stage items are labelled at 1120 nm; Friedenauer runs at 1118 nm. The 2 nm offset is well within typical coating bandwidth, but the [14-GHz unlockable domain](friedenauer-baseline.html) (Friedenauer §4) sits inside this offset range and should be considered before fielding any pre-existing 1120 nm coating.
- **AOI must match cavity folding angle.** Friedenauer LBO = 5° per mirror at 10° full fold; BBO = 13.7° per mirror at 27.4° full fold. Coatings specified at 0° or 12° / 15° AOI may not be drop-in for the Friedenauer geometry — coating R/T/phase response shifts with AOI off-design.
- **Verification trail.** The last three columns of every component table (`Qty checked`, `Initials`, `Date`) are filled in by the person doing the physical verification. `Date` in `YYYY-MM-DD`. An em dash (`—`) means "not yet checked". The first verification pass is scheduled for the week of 2026-05-11. Initials should be added at the same time as the count so a single audit pass produces a self-consistent triple.
- **German handwriting on legacy boxes.** `Einkoppler` = input coupler, `Umlenker` = fold/turn mirror, `Resonator` = resonator, `verlustarm` = low-loss, `Beschichtung Vorrat` = coating-stock reserve. Where the reading is partial, the row is tagged `O*` and the uncertainty is called out.

---

## A. Items keyed to the **LBO stage** (1118 / 1120 nm — 559 / 560 nm)

LBO ring (Friedenauer Table 1) needs: M1 plane IC R = 97.5 % @ 1118 nm; M2 plane HR > 99.98 % @ 1118 nm (piezo-mounted); M3 concave HR f = 25 mm (R = 50 mm) > 99.98 % @ 1118 nm; M4 concave OC f = 25 mm > 99.9 % @ 1118 nm + > 95 % HT @ 559 nm. Folding angle 10° (5° per focusing mirror).

| ID | Box / vendor | Reading | Likely Friedenauer role | Notes | Source-tier | Qty checked | Initials | Date |
|---|---|---|---|---|---|---|---|---|
| I-A1 | Layertec, clear box, batch G0605020 | 6 × FS Ø 12.7 × 6.35 mm, r = 50 mm, HR ≥ 99.98 % @ 1120 nm cav; handwritten "M3 (alt!) Umlenker LBO" | **LBO M3 / M4 focusing mirrors (concave, prior generation)** — geometry (Ø 12.7, R = 50 mm) is an exact match to Friedenauer f = 25 mm focusing mirrors | "alt!" = older set; verify R-value at 1118 nm and surface scratch/dig before reuse | O | — | — | — |
| I-A2 | Layertec, clear box, batch G0605020 | 6 × quartz cavities, 75 mm; HR 99 % @ 1120 nm / 0°; handwritten "LBO Umlenker" | **LBO M2 plane HR @ 1120 nm** (or generic 1120 nm cavity HR); R = 99 % is *too low* for the Friedenauer M2 spec (> 99.98 %), so these are most likely steering/relay HRs, not the cavity end-mirror | Use as steering optics around the 1120 nm leg; do not use as M2 unless higher-R coating run is procured | O* | — | — | — |
| I-A3 | Layertec, clear box, batch G0605020 | 2 × FS substrates, r = 50 mm cav, HR @ 1120 nm; "LBO Umlenker" | LBO focusing pair candidate; only 2 pcs → likely a backup pair to I-A1 | Verify coating run is identical to I-A1 before mixing | O* | — | — | — |
| I-A4 | Layertec, clear box, batch G0605020 | 2 × Pumpspiegel quartz substrates, HR @ 1120 nm / 0°; "Pumpspiegel" = pump-side mirror | LBO **pump-side dichroic / M2 candidate** if reflectivity meets > 99.98 %; label values not fully legible | OPEN | O* | — | — | — |
| I-A5 | Laseroptik, Art-Nr. S-00018, red box | 12 × SQ2 Ø 12.7 × 6.35 mm, plan; PR @ 1120 nm AOI 15° R = 98.5 %; rear AR @ 1120 nm AOI 15°; ref B080212 / B050203 | **LBO M1 (input coupler) candidate** — R = 98.5 % is 1.0 percentage point higher than Friedenauer's 97.5 %, so coupling is tighter (lower IC transmission); needs impedance-matching analysis under the actual cavity loss budget | AOI = 15° → fold angle = 30° per pair, **does not match Friedenauer 10° fold**; usable only with a re-designed plane segment of the cavity, *not* a drop-in for the focusing-mirror seat | O | — | — | — |
| I-A6 | Laseroptik, Art-Nr. S-00018, red box | 12 × SQ2 Ø 12.7 × 6.35 mm, plan; PR @ 1120 nm AOI 15° R = 96 %; rear AR @ 1120 nm AOI 15°; same ref as I-A5 | LBO M1 candidate with **looser coupling** (R = 96 %, vs 97.5 % paper-stated); useful for source powers higher than 1.8 W (more aggressive coupling tolerates more pump) | Same AOI mismatch as I-A5 | O | — | — | — |
| I-A7 | Laseroptik, red, "Umlenker 1120 über Kristall" (deflector at 1120 nm over crystal) | Specifications partially obscured | **LBO M3/M4 focusing mirror at the crystal waist** (semantic match to "Umlenker über Kristall") | Recover label content before use | O* | — | — | — |
| I-A8 | Newport, "HT 560 / HR 1120 ... R > 99 % ... 694 nm? ... M3 ... 13-0852" | Mixed-band dichroic; likely HT @ 560 nm + HR @ 1120 nm at some AOI | **LBO M4 (output coupler) candidate** if HT @ 560 nm value is high enough — Friedenauer requires T > 95 % @ 559 nm; vendor part 13-0852 (Newport catalog code) | The "694 nm" annotation suggests this was originally specced for a different project (Ti:S or ruby line); reverify HT @ 560 nm spec | O* | — | — | — |

---

## B. Items keyed to the **BBO stage** (559 / 560 nm — 280 nm)

BBO ring (Friedenauer Table 1) needs: M1' plane IC R = 98.4 % @ 559 nm; M2' plane HR > 99.93 % @ 559 nm (piezo-mounted); M3' concave HR f = 25 mm > 99.93 % @ 559 nm; M4' concave OC f = 25 mm > 99.8 % @ 559 nm + > 94 % HT @ 280 nm. Folding angle 27.4° (13.7° per focusing mirror) → AOI ≈ 13.7° at the curved seats; AOI = 0° at the plane mirrors.

| ID | Box / vendor | Reading | Likely Friedenauer role | Notes | Source-tier | Qty checked | Initials | Date |
|---|---|---|---|---|---|---|---|---|
| I-B1 | Laseroptik, red, top row | 5 × FS Ø 12.7 × 6.35 mm, plan; R = 97 % @ 560 nm / 12° P-pol; rear AR @ 560 nm / 12° P-pol | **BBO M1' input coupler candidate** — R = 97 % is 1.4 pp lower than Friedenauer's 98.4 % (looser coupling) | 12° AOI close to Friedenauer's 13.7° per-curved-mirror geometry but these are *plane*; usable as the IC plane mirror with cavity re-balancing | O | — | — | — |
| I-B2 | Laseroptik, red, top row | 5 × FS Ø 12.7 × 6.35 mm, plan; R = 96 % @ 560 nm / 12° P-pol; rear AR | Same role as I-B1, **even looser coupling** (R = 96 %) | Useful if downstream BBO loss budget is higher than Friedenauer's | O | — | — | — |
| I-B3 | Laseroptik, red, top row | 5 × FS Ø 12.7 × 6.35 mm, plan; R = 94 % @ 560 nm / 12° P-pol; rear AR | Same as I-B1/B2; **R = 94 %** — most aggressive coupling | Tolerates more 559 nm pump; would over-couple at 0.95 W input | O | — | — | — |
| I-B4 | Laseroptik, red, "Einkoppelspiegel R = 97 %", ~6 BK7 Ø 12.7 mm plan | BBO IC plane, R = 97 % @ (likely) 560 nm | Equivalent role to I-B1 on BK7 substrate | Substrate is BK7 not FS — verify UV transmission at 280 nm if the OC role is considered | O* | — | — | — |
| I-B5 | Schlipf / MPI Garbsen, red | "R = 90 % Einkoppler für 560 nm; HR 560 nm / 0°; 4 FS Ø 12.7 + 3 BK7 Ø 12.7", plan | BBO **strong-coupling IC** (R = 90 %, much looser than Friedenauer); plus a HR plane @ 560 nm / 0° — **direct M2' candidate** | Stewardship origin "Schlipf/MPI Garbsen" — flag for vendor-batch traceability if used | O | — | — | — |
| I-B6 | Laseroptik, red, IBS coating | FS Ø 12.7, plan, IBS HR @ 560 nm / 15° AOI; substrate ref LZH 11427 | **BBO M2' plane HR candidate**; IBS = ion-beam sputtered → typically the lowest-loss coating method, suitable for the > 99.93 % spec | Verify R-value (label does not state percentage explicitly in transcription) | O* | — | — | — |
| I-B7 | Laseroptik, red, B080225 / B080227 | 12 × FS Ø 12.7 × 6.35 mm plan; PR @ 560 nm R = 98.5 % AOI 15° P-pol; rear AR @ 560 nm AOI 15° | **BBO M1' input coupler — closest match to Friedenauer's 98.4 % spec** | AOI = 15° vs Friedenauer 13.7° on curved mirrors and 0° on plane mirrors → a small AOI mismatch; bandwidth typically forgiving | O | — | — | — |
| I-B8 | Laseroptik, Art-Nr. S-00018, red, "Einkoppler 560" | 6 × SQ2 Ø 12.7, **r = 50 mm** (concave); rear AR @ 560 nm AOI 15° | **BBO M3' / M4' focusing-mirror seat IC** — concave R = 50 mm matches f = 25 mm Friedenauer geometry; SQ2 OK at 559 nm | Verify front-surface coating spec (label reads "Einkoppler"; reflectivity not transcribed) | O* | — | — | — |
| I-B9 | Laseroptik, Art-Nr. S-00129, red, "IBS HR @ 560 nm (P-pol) AOI 15°" | 6 × SQ2 Ø 12.7, r = 50 mm; ref e090803 | **BBO M3' (curved HR) candidate** — focal R = 50 mm + IBS HR @ 560 nm matches Friedenauer's curved-HR seat directly | AOI 15° vs 13.7° per-mirror Friedenauer fold → ~1.3° off; bandwidth typically tolerates | O | — | — | — |
| I-B10 | Laseroptik, three clear boxes side-by-side | 3 boxes of round optics; PR @ 560 nm AOI 15°, with R = 96 % / 97 % / 98.5 % across the three; rear AR @ 560 nm AOI 15°; ref B080211 / B050206 | **BBO M1' coupling-strength sweep set** — same coating run, three different reflectivities; ideal for impedance-match optimisation in a built ring | The R = 98.5 % box overlaps with I-B7 (different ref number); verify they are not duplicate stock | O | — | — | — |
| I-B11 | LO Laseroptik, red, "R = 98 ± 0.5 % für 560 nm / 0° verlustarm" | 3 × BK7 Ø 12.7 × 6.35 mm; AR rear | **BBO M2' plane HR candidate** at AOI 0° — but R = 98 % is *too low* for Friedenauer's M2' (> 99.93 %); usable as a *steering HR*, not a cavity end-mirror | The "verlustarm" (low-loss) language suggests scatter/abs is low even if R is moderate | O | — | — | — |
| I-B12 | LO Laseroptik, red, "R = 80 % für 560 nm / 0°; HR 560 nm / 45° + AR" | 1 × BK7 + 2 × BK7 Ø 25 × 6.35 mm | **BBO output pickoff** (R = 80 % @ 0°) for a 559 nm sampling tap, plus HR @ 45° steering optics for the 559 nm transport line between LBO and BBO | Useful for mode-matching diagnostics and the 10 mW pickoff to the iodine cell (Friedenauer §2 / Fig. 1) | O | — | — | — |

### B.1 BBO output couplers (HR @ 559 nm + HT @ 280 nm) — these are the *most differentiated* items

BBO M4' specifically requires high reflectivity at 559 nm and high transmission at 280 nm in the same coating stack — a non-trivial dichroic. The shelf has several variants:

| ID | Box / vendor | Reading | Likely Friedenauer role | Notes | Source-tier | Qty checked | Initials | Date |
|---|---|---|---|---|---|---|---|---|
| I-B13 | Laseroptik, red, fourth row | "HR 560 nm HT 280 nm / 0°; rear AR 280 nm / 0°"; **7 × Herasil Ø 12.7 × 6.35 mm r = -75 mm; 2 × Herasil r = -150 mm; 1 × Herasil r = -50 mm** | **BBO M4' output coupler — three curvature options** (75 / 150 / 50 mm). The r = -50 mm element is the **direct geometric match to Friedenauer's f = 25 mm focusing-mirror role** as the curved OC | Herasil substrate = Heraeus FS, low absorption in UV; AOI = 0° → use only as a plane element of the ring or in a re-designed end-mirror seat, **not as the curved focusing OC at 13.7° AOI** | O | — | — | — |
| I-B14 | LO Laseroptik, red | "HR 560 nm HT 280 nm / 0° verlustarm; 3 × Herasil r = -196 mm; 3 × Herasil r = -148 mm" | **BBO M4' OC, low-loss, longer-ROC variants** — useful for a longer cavity / different waist than Friedenauer's | r = 148 / 196 mm gives a softer focus → larger waist → less peak intensity at the BBO crystal; appropriate for higher-power 559 nm than Friedenauer's 0.95 W | O | — | — | — |
| I-B15 | Laseroptik, Art-Nr. S-00597, red | "L080227, HR 560, HT 280, 15°; rear AR 280 nm; 12 × SQ2 Ø 12.7 × 6.35 mm, r = ±50 mm" (the ± likely means concave on one face) | **BBO M4' OC at 15° AOI, R = 50 mm** — closest single match to Friedenauer's curved OC seat (concave focal R = 50 mm, ≈ Friedenauer's 13.7° per-curved-mirror geometry) | **Highest-priority candidate for the BBO M4' role.** Verify HT @ 280 nm value | O | — | — | — |
| I-B16 | Laseroptik, Art-Nr. S-00597, red | "uncoated; MPI Q" | Spare uncoated SQ2 substrates labelled MPI Q (Quantenoptik) | Useful for in-house re-coating runs; not directly a cavity element | O | — | — | — |
| I-B17 | LO Laseroptik, red, "HR 560 nm T < 0.1 % / 0° verlustarm" | 3 × Herasil r = -196 mm; 3 × Herasil r = -148 mm | **BBO M2' / M3' HR with R > 99.9 %** (T < 0.1 % means R > 99.9 %) — meets Friedenauer's > 99.93 % spec for the cavity HRs | Curvature ≠ Friedenauer's 50 mm, so these are *not* drop-in M3'; use as plane HRs (for the M2' role) by mounting the curve in a non-imaging position | O | — | — | — |
| I-B18 | Thorlabs, white box w/ barcode | "AR 280, HT 560" | UV exit window or projection optic | Use on the **outboard side of the BBO M4'** to project the 280 nm output beam (cf. Friedenauer §3 "TEM₀₀ projection") | O | — | — | — |
| I-B19 | Laseroptik, L-04575, red, "HR 560 nm HT 1120 nm / 45° p" | 4 × N-BK7 Ø 25 × 6.35 mm; batch 26029o1 | **Critical 1120 / 560 nm dichroic separator** at 45° p-pol — separates 560 nm from leakage 1120 nm at the LBO output before launching into the BBO ring | Essential for keeping residual 1120 nm out of the BBO ring, where it would saturate the HC photodetector and cause locking artefacts | O | — | — | — |

### B.2 BBO crystals — Brewster-cut Type-I, 4 × 4 × 10 mm³, θ = 44.4°

**Crystal-stage role.** Friedenauer 2006 specifies a Brewster-cut BBO of 4 × 4 × 10 mm at ~ 50 °C oven temperature for Type-I 559 → 280 nm SHG. The paper does **not** state the cut angle; `θ = 44.4°` here is the Sellmeier-derived Type-I PM angle for 559 → 280 nm in BBO and is a literature-standard value, **not** a Friedenauer-stated number. All three vendor lots below are nominally compatible with the Friedenauer crystal role — they differ in vintage (UV bulk-absorption / colour-centre risk), QC paper trail, and crystal-azimuth (`φ`) convention.

**Procurement-document policy.** Primary procurement documents (vendor certificates of compliance, order confirmations, internal Freiburg POs, prices) are **not committed** to the repository — they include personal contact details and pricing. They are referenced by document title and date here for traceability only.

**On the `φ` orientation.** For Type-I BBO SHG (point group 3m, ooe interaction) the effective nonlinearity has the form `d_eff ≈ d_31 sin θ − d_22 cos θ sin 3φ`. With `|d_22|` ≈ 2.2 pm/V and `|d_31|` ≈ 0.04 pm/V, the second term dominates: at `θ = 44.4°` and `φ = 90°` the geometric factor `cos θ · |sin 3φ|` reaches ~ 0.71, while at `φ = 0°` it vanishes. **A φ = 0° orientation gives ~ 50× lower d_eff than φ = 90°** — i.e., ~ 2500× lower SHG efficiency. The Castech φ = 0° item below should therefore be treated as a coating-test substrate, not as an SHG-active crystal, **unless its φ convention differs from the textbook reference frame** (vendor frame conventions vary).

| ID | Vendor / lot | Specification | Quantity | Documents | Likely Friedenauer role | Notes | Source-tier | Qty checked | Initials | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| I-B20 | **Raicol Crystals** Cert. No. 6331; serials 25016301 / 25016302 / 25016303; manufactured Q2 2025 | BBO 4 × 4 × 10 mm³, T1 SHG 559 → 280 nm, **θ = 44.4° (±18'), φ = 90° (±18')**, B-CUT (Brewster, 59.1° external), uncoated; S1 + S2 polished; parallelism < 30 arcsec; perpendicularity < 10 arcmin; flatness < λ/8 @ 633 nm; scratch / dig < 10 / 5 (all certificate flags `V` = compliant) | 3 pcs | Raicol *Certificate of Compliance & Tests No. 6331* (08 Jun 2025); EKSMA Optics *Order Confirmation* (15 Apr 2025, exp. dispatch 10 Jun 2025) — likely the same physical 3 pcs delivered through EKSMA as Raicol distributor; verify on receipt | **BBO crystal — primary candidate (newest stock; full QC trail; matches Friedenauer 4 × 4 × 10 mm and Brewster-cut spec)** | Hygroscopic — keep desiccated; verify bulk transmission at 280 nm before installation. Vendor is **Raicol**, not Friedenauer's "Crystals of Siberia" (§4) — the 14-GHz unlockable-domain history does **not** transfer to this lot, which is good (re-tests the §4 mechanism on independent crystal stock) | O | — | — | — |
| I-B21 | **A-Star** PO BL170229, SO AS171206-01; manufactured 2017-11-13 | BBO Type-I, **θ = 44.4°**, 4 × 4 × 10 mm; coating state and `φ` not stated on the photographed label | 4 pcs (2 boxes × 2 pcs) | Photographed vendor labels, 2026-05-07 | **BBO crystal — backup / aged stock** | ~ 8 years storage at first use; check the entrance face for grey-tracking / colour-centre clouding before use; coating state ambiguous — verify uncoated vs AR-coated. Friedenauer §4 unlockable-domain history specifically attributed only to Crystals-of-Siberia stock; A-Star is a third independent vendor | O | — | — | — |
| I-B22 | **Castech** lot G8115-2, Crystal ID 2-21577; manufactured 2009-07-02 | BBO 1 pc, **θ = 44.4°, φ = 0°** (note: vendor-stated, orthogonal azimuth to I-B20), 4 × 4 × 10 mm³, **2 faces polished** (cf. I-B20's S1 + S2); handwritten "Beschichtung Vorrat" (= coating-stock reserve) on the bag | 1 pc | Photographed vendor label, 2026-05-07 | **Coating-test substrate — not a drop-in SHG crystal in its labelled φ orientation** (see "On the `φ` orientation" note above) | The handwritten "Beschichtung Vorrat" is consistent with a substrate set aside for in-house coating-process tests, not an active doubler. Before any SHG use: confirm the vendor's `φ` reference frame (Castech may not use the same `+x` convention as Raicol), inspect for grey-tracking after ~ 17 years storage, and verify the unpolished-face state | O* | — | — | — |

#### B.2 — pending procurement (not in inventory)

- **Raicol Quotation PQ250167 (04 Jul 2025)** — quote for 3 ea + 10 ea additional `BBO 4 × 4 × 10 mm³ T1 SHG 560 → 280 nm θ = 44.4° B-CUT uncoated`, S1 + S2 polished. Quote expired 05 Jul 2025; not ordered. Reference for restocking decision when KD-UV280-005 / -007 procurement is unblocked. Pricing not transcribed.

---

## C. **Pre-built / packaged sub-assemblies** (highest leverage)

| ID | Box / item | Reading | Likely Friedenauer role | Notes | Source-tier | Qty checked | Initials | Date |
|---|---|---|---|---|---|---|---|---|
| I-C1 | Orange box (lower right of shelf) | "Resonator SHG Spiegelsatz R = 12°; Einkoppel 96 %; 2 × Konkavspiegel HR 560 nm HT 280 nm r = -150 mm; 1 × Planspiegel" | **Complete BBO ring cavity mirror set** — IC at 96 % + two curved HR-560/HT-280 (r = 150 mm) + one plane HR | Curvature r = 150 mm is **3 × Friedenauer's 50 mm**, so this kit lays out a much larger / softer-focus BBO ring; would be re-purposed if the build target moves away from Friedenauer's tight geometry | O | — | — | — |
| I-C2 | Mounted hardware area, red anodized parts labelled M1 / M2 / M3 / M4 | Complete ring-cavity *mirror mount* set with steering knobs; visible piezo lead on one mount | **Drop-in mechanical chassis** for either the LBO or the BBO ring | The piezo-loaded mount can host the M2 / M2' role (Hänsch–Couillaud servo seat, cf. Friedenauer's Thorlabs AE020304D04 + lead disk) | O | — | — | — |
| I-C3 | Laseroptik, red, "Spiegelsatz; M2 in extrabox" | "Mirror set; M2 stored separately" | **Curated mirror set** missing the M2 mirror, which is in a separate box | Identify the matching M2 sub-box before assembly | O* | — | — | — |
| I-C4 | Laseroptik, red, "Resonator: unbeschichtet & Einkoppel" | "Resonator: uncoated + input coupler" — uncoated cavity substrates plus a coated IC | Spare-substrate kit + coupling element for a **fresh cavity build**; IC reflectivity not legible in transcription | OPEN value | O* | — | — | — |
| I-C5 | Loose hardware on shelf | Mirror mounts (multiple), fibre-coupled element (with cable visible — likely a fibre-launched alignment beam or photodiode), VIS-band cylindrical filter | Generic alignment / diagnostic stock | Photograph each on inspection day; not directly mapped to a Friedenauer role | O* | — | — | — |

---

## D. Cross-reference: Friedenauer requirement → best on-shelf match

| Role | Friedenauer spec | Best on-shelf match | Gap |
|---|---|---|---|
| LBO M1 (plane IC @ 1118 nm, AOI ~5°) | R = 97.5 % | I-A5 (R = 98.5 %, 15° AOI) or I-A6 (R = 96 %, 15° AOI) | **AOI mismatch** (15° vs 5°); reflectivities bracket the target |
| LBO M2 (plane HR @ 1118 nm, AOI ~5°) | R > 99.98 % | None directly; I-A2 / I-A4 are HR @ 1120 / 0° but reflectivity not high enough or unread | **Open** — would need a > 99.98 % @ 1120 / 0° (or near-0°) HR coating run |
| LBO M3 (concave HR @ 1118 nm, R = 50 mm, AOI ~5°) | R > 99.98 %, f = 25 mm | I-A1 (R ≥ 99.98 %, R = 50 mm — direct match) | Verify "alt!" (older) status before reuse |
| LBO M4 (concave OC, R = 50 mm, AOI ~5°) | R > 99.9 % @ 1118; T > 95 % @ 559 | I-A8 (Newport HT 560 / HR 1120, but AOI / curvature unconfirmed) | **Likely open** — the LBO OC is the rarest spec; verify I-A8 or specify a coating run |
| BBO M1' (plane IC @ 559 nm, AOI ~0°) | R = 98.4 % | **I-B7** (R = 98.5 %, 15° AOI; closest match) or I-B10 (R = 98.5 % box of the sweep set) | AOI 15° is acceptable for a plane mirror tilted slightly; closest directly usable item |
| BBO M2' (plane HR @ 559 nm, AOI ~0°) | R > 99.93 % | I-B17 (R > 99.9 %, AOI 0°) | Borderline (99.9 % vs 99.93 %); acceptable for a first iteration |
| BBO M3' (concave HR @ 559 nm, R = 50 mm, AOI ~13.7°) | R > 99.93 %, f = 25 mm | **I-B9** (IBS HR, R = 50 mm, AOI 15°) — direct match | AOI 15° vs 13.7° is a 1.3° offset; bandwidth-tolerant |
| BBO M4' (concave OC, R = 50 mm, AOI ~13.7°) | R > 99.8 % @ 559; T > 94 % @ 280 | **I-B15** (HR 560 / HT 280, 15° AOI, r = ±50 mm) — direct match | Highest-priority candidate; verify HT @ 280 |
| LBO–BBO transport: 559 nm separation from 1118 nm leakage | (not specified in Friedenauer; standard practice) | **I-B19** (HR 560 / HT 1120 / 45° p, Ø 25) | Drop-in |
| BBO output projection (280 nm exit) | (not specified; standard practice) | **I-B18** (Thorlabs AR 280 / HT 560) | Drop-in |
| 559 nm pickoff for I₂ lock | ~10 mW from 0.95 W → R ≈ 99 % beam-splitter | I-B12 (R = 80 % BS) is too aggressive; **gap** — pickoff fraction needs ~1 % not ~20 % | Open; standard low-pickoff plate would be added on procurement |
| BBO crystal (Brewster-cut Type-I, 4 × 4 × 10 mm, ~ 50 °C oven) | dimensions stated; cut angle **not** given by Friedenauer — Sellmeier-standard `θ = 44.4°` adopted | **I-B20** (Raicol 2025, 3 pcs, full QC, φ = 90°) — direct primary; I-B21 (A-Star 2017, 4 pcs) — backup, age check needed; I-B22 (Castech 2009, φ = 0°) — coating-substrate, **not** SHG-active in labelled orientation | Closes the Friedenauer "exact BBO cut angle" open-extraction item by adopting Sellmeier-standard θ = 44.4° (literature value, not paper-stated). Independent vendor stock (Raicol, A-Star) breaks the Crystals-of-Siberia provenance link relevant to the §4 14-GHz domain |

---

## E. What this inventory does NOT establish

- **Coating measurement.** Reflectivities are *as labelled*. Coatings can drift over years of storage; for cavity-grade use, R, T, and scatter must be re-measured on a spectrophotometer plus a cavity ring-down before commitment.
- **Surface quality.** Scratch / dig, contamination, and UV-induced colour-centre damage are not visible in the photo and must be inspected at the bench before any item is mounted.
- **Stock count.** The "5 ×", "12 ×", "6 ×" etc. counts are box-stated, not photo-confirmed.
- **AOI-correct curved-mirror coatings.** Many coatings on this shelf are 0° AOI, but Friedenauer's curved-mirror seats sit at 13.7° AOI per mirror (BBO) or 5° AOI per mirror (LBO). For curved seats this matters: a coating designed at 0° will have noticeably different R / T / phase at 13.7°. Re-measurement at the design AOI is mandatory.
- **Wavelength offset.** Most LBO-stage items here are labelled at 1120 nm; Friedenauer runs at 1118 nm. The 2 nm offset is well within typical coating bandwidth, but the 14 GHz unlockable domain (Friedenauer §4) sits inside this offset range and should be considered when fielding any pre-existing 1120 nm coating in a new build.
- **Substrate UV-grade for 280 nm.** SQ2 / Herasil / Heraeus FS are UV-grade; BK7 and N-BK7 are *not* — items built on BK7 (e.g., I-B11, I-B12, I-B19) cannot serve as a 280 nm-transmissive surface.
- **BBO crystal aging.** The A-Star (2017) and Castech (2009) lots have spent multiple years in storage; UV-induced grey-tracking, surface haze from residual humidity, and bulk colour-centre formation all degrade SHG performance even without exposure. Inspect both faces under bright illumination, and pre-screen each piece by measuring 280 nm bulk transmission against the freshly QC'd Raicol pieces (I-B20) before fielding.
- **`φ` convention is not standardised between vendors.** Raicol's certificate states `φ = 90°` and the Castech bag states `φ = 0°`; without each vendor's reference-frame definition (which crystallographic direction is `+x`?) these may or may not actually correspond to different physical orientations. Resolve before assigning a SHG-active vs coating-substrate role to I-B22.
- **BBO crystal procurement provenance is not in the repo.** Vendor certificates, order confirmations, and price quotes are referenced in B.2 but not committed (pricing + personal contact data). The vendor cert / serial numbers in the table are sufficient to re-look-up the originals.

---

## F. Reading uncertainties

The following items in the photograph have **partially obscured / handwritten labels** and would benefit from a higher-resolution close-up shot or a physical inspection of the box label:

- I-A4 ("Pumpspiegel" — pump-side mirror reflectivity not transcribable).
- I-A7 ("Umlenker 1120 über Kristall" — full coating spec hidden behind another box).
- I-A8 (Newport 13-0852 — multi-line spec partially obscured; mention of "694 nm" suggests a non-Friedenauer history).
- I-B6 (IBS HR @ 560 nm — explicit R % not in transcription).
- I-B8 (Einkoppler 560 — coupling reflectivity not in transcription).
- I-B16 (uncoated SQ2 with "MPI Q" annotation — origin clear, role optional).
- I-C3 / I-C4 (Spiegelsatz packages — composition list partial).
- I-C5 (loose hardware — mount manufacturer / model not transcribed).

---

## G. Suggested next actions (out of scope of this inventory file)

1. Photograph each box label individually at high resolution; replace `O*` rows with verified text.
2. For the **highest-leverage matches** — I-A1 (LBO M3/M4), I-B9 (BBO M3'), I-B15 (BBO M4'), I-B19 (LBO→BBO dichroic), I-C2 (mount chassis), I-C1 (BBO mirror kit) — bench-verify R / T at the *Friedenauer* wavelengths (1118, 559, 280 nm) using a spectrophotometer.
3. Identify the **gap items** flagged in section D (LBO M2 > 99.98 %, LBO M4 OC) and add them to the [KD-2026-XXX-uv-280nm](KD-2026-XXX-uv-280nm.html) procurement queue.
4. Cross-link verified items into the per-row vendor column of [Friedenauer 2006 components inventory](friedenauer-baseline.html), preserving the source-tier annotation (vendor link sits *alongside*, not in place of, the paper-stated specification).
5. **BBO crystal verification pass:** for I-B20 / I-B21 / I-B22, in addition to a count: (a) inspect both faces under bright illumination for grey-track / haze / chips, (b) measure bulk transmission at 280 nm and 559 nm and compare against the Raicol freshly-QC'd pieces, (c) confirm `φ`-convention with each vendor's data sheet before assigning the Castech piece to either an SHG-active or coating-substrate role, (d) record the verification triple (`Qty checked` / `Initials` / `Date`) in the B.2 table.
