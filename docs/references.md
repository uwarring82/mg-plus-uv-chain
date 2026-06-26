---
layout: default
title: References — literature index
description: Alphabetical literature index for mg-plus-uv-chain. Each entry carries a short citation label, source-tier marker, link to the extraction artefact under data/literature/, and a three-sentence content + relevance summary.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page is a reference index, not an architecture-comparison or build commitment. The Coastline / Sail vocabulary applies to <em>claims</em>; this page indexes external evidence and does not by itself add new claims.</p>

<p class="eyebrow">Project · references</p>

# References — literature index

**Status:** Living index. Entries land here when an extraction artefact is committed under [`data/literature/<key>/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/) and is past SCAFFOLD status. Last touched 2026-05-08.

**Charter compliance.** This page does not affect Level-0 or Level-1 binding parameters; it does not advance or close G1 / G2 / G3; it does not introduce architecture-family-specific simulation. The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is unaffected.

## How to use this page

- Each entry is keyed by a six-character **citation label** in the form `[Auth4YY]` (first four letters of first author's surname + two-digit year). Labels are unique within this index. Use them as inline shorthand in logbook entries and notebooks: e.g. `[Burd23]` rather than `Burd2023` once the link to this index is established.
- The **source-tier marker** matches the convention in [`data/literature/<key>/extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/): `[P]` peer-reviewed primary literature, `[S]` secondary (theses, reviews, preprints, OSA proceedings, internal reports).
- Each entry carries three sentences: what the work is (content), what it reports (key findings), and why `mg-plus-uv-chain` cites it (relevance).
- Bibliographic detail and numerical extractions live in the per-entry `extracted.yaml` and `notes.md` files linked from each entry.

## Source-tier legend

| Tier | Meaning |
|---|---|
| `[P]` | Peer-reviewed primary literature (journal article with DOI, after editorial peer review). |
| `[S]` | Secondary or grey literature (theses, review articles, preprints, conference proceedings, internal reports). |

Use `[P]` evidence for *Coastline* claims (testable design constraints) wherever available; `[S]` evidence is admissible for *Sail* recommendations (adaptive guidance) and for in-house operational references.

## Index by topic

For readers who want a topical entry-point rather than alphabetical, the index below cross-references the alphabetical list:

- **VECSEL seed lasers (1118 nm and adjacent).** [Burd16] · [Burd23] · [Kief20] · [Guth21] · [Span23] · [Span25]
- **Doubling-chain topology (LBO + BBO at 280 nm).** [Frie06] · [Kief20] · [Guth21] · [Burk21]
- **BBO material properties (d_eff, Sellmeier, thermal).** [Eime87] · [Ecka90] · [Tamo18]
- **BBO LIDT and long-term reliability.** [Kond98] · [Kubo98] · [Kuma15] · [Turc22] · [Brow19]
- **²⁵Mg⁺ atomic system + multi-purpose laser architecture.** [Hemm11] · [Hume10] · [Kjae00]

---

## Alphabetical list

### [Brow19] Brown et al. 2019 — Physical origin of early failure for contaminated optics &nbsp; <span style="font-size:0.85em">`[P]`</span>

A. Brown, D. Bernot, A. Ogloza, K. Olson, J. Thomas, J. Talghader, *Sci. Rep.* **9**, 635 (2019). DOI: [10.1038/s41598-018-37337-5](https://doi.org/10.1038/s41598-018-37337-5). Folder: [`Brown2019/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Brown2019/).

Investigates the physical origin of early failure in optical components under high-fluence laser exposure, isolating contamination-induced absorption sites as the dominant precursor to catastrophic damage. Shows that even sub-monolayer particulate or hydrocarbon films lower local LIDT by orders of magnitude through localised absorption and thermally-driven stress. **Relevance:** informs the cleanliness budget and surface-handling protocols for the 280 nm BBO output stage where surface-contamination LIDT, not bulk crystal LIDT, is the dominant failure-mode envelope.

### [Burd16] Burd et al. 2016 — VECSEL systems for the generation and manipulation of trapped ²⁵Mg⁺ ions &nbsp; <span style="font-size:0.85em">`[P]`</span>

S. C. Burd, D. T. C. Allcock, T. Leinonen, J. P. Penttinen, D. H. Slichter, R. Srinivas, A. C. Wilson, R. Jördens, M. Guina, D. Leibfried, D. J. Wineland, *Optica* **3**, 1294–1300 (2016). DOI: [10.1364/OPTICA.3.001294](https://doi.org/10.1364/OPTICA.3.001294). Folder: [`Burd2016/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burd2016/).

Demonstrates two NIST + Tampere VECSEL systems for trapped ²⁵Mg⁺: a 1117 nm **I-cavity ("IC")** VECSEL that is **externally frequency-quadrupled** (fibre-coupled waveguide doubler → 559 nm, then BBO build-up cavity → 280 nm) for Doppler cooling, repumping, and Raman; and a 1141 nm **V-cavity ("VC")** VECSEL that is **intracavity-doubled to 571 nm** and then **externally doubled** (BBO) → 285 nm for photoionisation. Reports ≈ 50 kHz linewidth (VC, from the Hänsch–Couillaud error signal) and < 20 kHz frequency deviation (IC), ASE-suppressed output, and operational use as both Doppler-cooling and photoionisation lasers. **Relevance:** the wavelength-adjacent ²⁵Mg⁺ companion to [Burd23] — closest published demonstration to the 1118 nm Friedenauer fundamental, anchoring the gain-mirror feasibility envelope for the in-house build.

### [Burd23] Burd et al. 2023 — VECSEL systems for QIP with trapped ⁹Be⁺ ions &nbsp; <span style="font-size:0.85em">`[P]`</span>

S. C. Burd, J.-P. Penttinen, P.-Y. Hou, H. M. Knaack, S. Ranta, M. Mäki, E. Kantola, M. Guina, D. H. Slichter, D. Leibfried, A. C. Wilson, *J. Opt. Soc. Am. B* **40**, 773–781 (2023). DOI: [10.1364/JOSAB.475467](https://doi.org/10.1364/JOSAB.475467). Folder: [`Burd2023/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burd2023/).

Documents two NIST + Tampere VECSEL chains for ⁹Be⁺ — 940 nm → 470 nm (PPKTP) → 235 nm (BBO) and 1252 nm → 626 nm (PPLN waveguide) → 313 nm (BBO) — with class-A laser dynamics (long external cavity + short carrier lifetime → photon-lifetime-dominated regime) suppressing relaxation oscillations and the ASE pedestal. Reports < 100 kHz seed linewidth, intracavity birefringent filter + 1 mm YAG etalon + PZT mode-selection scheme, diamond-bonded gain mirrors with two distinct thermal architectures, and > 8 months of operational stability with < 10 % power drift. **Relevance:** the named **design-principles anchor** for the seed-laser layer of `mg-plus-uv-chain` (steward direction recorded 2026-05-08); principles transfer verbatim to the 1118 nm operating point, with [Burd16] supplying the wavelength-adjacent demonstration.

### [Burk21] Burkley et al. 2021 — Stable high-power deep-UV enhancement cavity in UHV with fluoride coatings &nbsp; <span style="font-size:0.85em">`[P]`</span>

J. S. B. von Milczewski et al., arXiv:[2105.14977](https://arxiv.org/abs/2105.14977) (2021). Folder: [`Burkley2021/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burkley2021/).

Demonstrates a high-power deep-UV enhancement cavity operated under ultra-high vacuum with hard fluoride mirror coatings, addressing the air-induced contamination LIDT failure mode that limits CW deep-UV cavities. Reports stable multi-watt operation at 280-nm-class power in cleanliness-controlled environment over extended duration. **Relevance:** candidate failure-mitigation reference for the 280 nm BBO output stage; UV-induced surface degradation is one of the G2-blocking design questions and this is the closest published demonstration of long-term clean-environment operation at the relevant wavelength.

### [Ecka90] Eckardt et al. 1990 — Absolute and relative nonlinear optical coefficients of KDP, KD*P, BBO, LiIO₃, MgO:LiNbO₃, and KTP &nbsp; <span style="font-size:0.85em">`[P]`</span>

R. C. Eckardt, H. Masuda, Y. X. Fan, R. L. Byer, *IEEE J. Quantum Electron.* **26**, 922–933 (1990). DOI: [10.1109/3.55534](https://doi.org/10.1109/3.55534). Folder: [`Eckardt1990/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Eckardt1990/).

Provides an internally-consistent set of effective nonlinear coefficients (d_eff) for KDP, KD*P, β-BBO, LiIO₃, MgO:LiNbO₃, and KTP, all measured by phase-matched second-harmonic generation under a unified methodology. Reports d_eff values to ≈ 10 % accuracy and resolves long-standing discrepancies among prior single-crystal measurements. **Relevance:** the canonical reference for d_eff(BBO) and the comparison-crystal d_eff values used throughout `mg-plus-uv-chain` for SHG-conversion-efficiency calculations and architecture-comparison numerics.

### [Eime87] Eimerl et al. 1987 — Optical, mechanical, and thermal properties of barium borate &nbsp; <span style="font-size:0.85em">`[P]`</span>

D. Eimerl, L. Davis, S. Velsko, E. K. Graham, A. Zalkin, *J. Appl. Phys.* **62**, 1968–1983 (1987). DOI: [10.1063/1.339536](https://doi.org/10.1063/1.339536). Folder: [`Eimerl1987/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Eimerl1987/).

Comprehensive material-property reference for β-BaB₂O₄ (BBO) covering Sellmeier coefficients, thermo-optic dn/dT, thermal-expansion tensor, transmission, Mohs hardness, and walk-off as a function of wavelength. Reports the foundational set of BBO material constants used throughout the field. **Relevance:** the BBO Sellmeier and thermal-property data source for any walk-off, phase-matching, or acceptance-bandwidth analysis at 280 nm in `mg-plus-uv-chain`; primary input to the LBO+BBO chain numerics.

### [Frie06] Friedenauer et al. 2006 — High-power all-solid-state laser system near 280 nm &nbsp; <span style="font-size:0.85em">`[P]`</span>

A. Friedenauer, F. Markert, H. Schmitz, L. Petersen, S. Kahra, M. Herrmann, Th. Udem, T. W. Hänsch, T. Schätz, *Appl. Phys. B* **84**, 371–373 (2006). DOI: [10.1007/s00340-006-2274-2](https://doi.org/10.1007/s00340-006-2274-2). Folder: [`Friedenauer2006/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/).

Documents a high-power all-solid-state CW laser system delivering ≥ 100 mW at 280 nm via a 2 W Yb-fibre seed at 1118 nm → LBO bow-tie ring-cavity SHG to 559 nm → BBO ring-cavity SHG to 280 nm, with both doubling stages Hänsch-Couillaud-locked. Reports operating parameters of the topology including cavity geometries, lock bandwidths (≈ 18 kHz loaded piezo resonance), 1.2 W ASE budget peaked between 1060–1100 nm, the iodine-referenced absolute frequency anchor at 559.271 nm, and the polarisation-drift failure mode of the Yb-fibre seed. **Relevance:** the **reference baseline architecture** for `mg-plus-uv-chain` — every successor build extends or replaces components of this Friedenauer chain, and the Charter §1.5 indicative anchor (≥ 500 mW at 280 nm) is set against this baseline.

### [Guth21] Guth 2021 — Assembling and benchmarking the next generation of solid-state laser systems for trapped ²⁵Mg⁺ &nbsp; <span style="font-size:0.85em">`[S]`</span>

L. Guth, *Master's thesis*, Faculty of Mathematics and Physics, University of Freiburg (August 2021). Supervisor: Prof. Dr. Tobias Schätz. Folder: [`Guth2021/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Guth2021/).

First MSc in the AG Schätz VECSEL chain after [Kief20]; delivers the first quantitative in-house VECSEL linewidth measurement at 1118 nm (1.207(12) MHz iodine-locked Allan deviation at τ = 100 ms) and the modular LBO + BBO frequency-doubling cavities. LBO cavity v3 achieves 87(6) % NIR → visible conversion at 1.27(4) W coupled IR (vs v2's 56(4) %); BBO cavity delivers 78(5) mW at 280 nm from 780(15) mW visible (10.0(11) % efficiency, stability not yet characterised). **Relevance:** the in-house operational reference for the LBO + BBO chain at the actual `mg-plus-uv-chain` operating point; numerically underwrites the seed-laser linewidth budget and the Phase NG-A LBO `L_passive` gap-closure target.

### [Hemm11] Hemmerling et al. 2011 — A single laser system for ground-state cooling of ²⁵Mg⁺ &nbsp; <span style="font-size:0.85em">`[P]`</span>

B. Hemmerling, F. Gebert, Y. Wan, D. Nigg, I. V. Sherstov, P. O. Schmidt, *Appl. Phys. B* **104**, 583–590 (2011). DOI: [10.1007/s00340-011-4472-9](https://doi.org/10.1007/s00340-011-4472-9). Folder: [`Hemmerling2011/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Hemmerling2011/).

Demonstrates that a single 280 nm fibre-laser-based system can support both Doppler cooling and stimulated-Raman ground-state cooling of ²⁵Mg⁺ via in-time AOM frequency shifting between detuned beam paths. Reports operational parameters including detunings, intensity allocation, and ground-state-cooling fidelity for the multi-purpose laser architecture. **Relevance:** the architectural prior in the Schätz / Schmidt lineage for the multi-purpose laser-system role that the `mg-plus-uv-chain` VECSEL build inherits; sets the *minimum-laser-count* design point that the project's loss-budget allocation defends.

### [Hume10] Hume 2010 — Two-species ion arrays for quantum logic spectroscopy &nbsp; <span style="font-size:0.85em">`[S]`</span>

D. B. Hume, *Ph.D. thesis*, University of Colorado / NIST Boulder (2010), 129 pp. Folder: [`Hume2010/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Hume2010/).

NIST dissertation documenting two-species (²⁵Mg⁺ + ²⁷Al⁺) ion-trap experiments and the supporting laser-system architecture for quantum logic spectroscopy of the ²⁷Al⁺ optical clock transition. Reports operational implementation of the UV laser systems used for ²⁵Mg⁺ Doppler cooling and gate operations. **Relevance:** external (non-Schätz) thesis documenting the same ²⁵Mg⁺ atomic system from a different laboratory — useful for cross-checking ²⁵Mg⁺ operating parameters and architectural choices, and as an independent reference for the multi-purpose-laser architecture.

### [Kief20] Kiefer 2020 — Floquet engineering in a 2-D array of trapped ²⁵Mg⁺ ions &nbsp; <span style="font-size:0.85em">`[S]`</span>

P. Kiefer, *Ph.D. dissertation*, Albert-Ludwigs-Universität Freiburg (defended 2020-03-03), 158 pp. Supervisors: Prof. Dr. Tobias Schätz, Prof. Dr. Giuseppe Sansone. Folder: [`Kiefer2020/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Kiefer2020/).

AG Schätz dissertation on Floquet engineering with ²⁵Mg⁺ in a 2-D triangular three-site array; §3.3 ("Laser system for generation of UV radiation") is where the in-house VECSEL platform first appears as a built and characterised laser at 1118 nm. Documents the Vexlum gain mirror + Layertec outcoupler (R = 97.5(3) %, RoC = 200 mm) + Newlight BIR0030 BRF + LightMachinery OP-3167-1000 etalon + LBO bow-tie + BBO ring chain, with P_out = 4.5(1) W single-mode at maximum pump (12.4(3) % single-mode optical-to-optical efficiency) and emission range 1116–1122 nm. **Relevance:** the **origin point** of the AG Schätz VECSEL+SHG platform for ²⁵Mg⁺ at 280 nm — vendor-part-number-level ground truth that propagates through [Guth21] / [Span23] / [Span25].

### [Kjae00] Kjaergaard et al. 2000 — Isotope-selective loading via resonance-enhanced two-photon ionisation &nbsp; <span style="font-size:0.85em">`[P]`</span>

N. Kjaergaard, L. Hornekær, A. M. Thommesen, Z. Videsen, M. Drewsen, *Appl. Phys. B* **71**, 207–210 (2000). DOI: [10.1007/s003400000296](https://doi.org/10.1007/s003400000296). Folder: [`Kjaergaard2000/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Kjaergaard2000/).

Demonstrates resonance-enhanced two-photon photoionisation of neutral magnesium for isotope-selective loading of ²⁵Mg⁺ into a Paul trap. Reports the relevant atomic transitions, intensity / frequency requirements, and the isotope-selectivity ratio achievable in practice. **Relevance:** the photoionisation-laser reference for ²⁵Mg⁺ ion-loading — separate beam path from the Doppler/Raman cooling chain, but a load-bearing input to the architectural decision of how many independent VECSELs the lab needs to operate (cf. [Hemm11] multi-purpose architecture).

### [Kond98] Kondo et al. 1998 — Long-term reliability of a 266 nm CW frequency-quadrupled BBO solid-state laser &nbsp; <span style="font-size:0.85em">`[P]`</span>

K. Kondo, M. Oka, H. Wada, T. Fukui, N. Umezu, K. Tatsuki, S. Kubota, *Opt. Lett.* **23**, 195–197 (1998). DOI: [10.1364/OL.23.000195](https://doi.org/10.1364/OL.23.000195). Folder: [`Kondo1998/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Kondo1998/).

Demonstrates extended-duration CW operation of a 266 nm BBO frequency-quadrupled solid-state laser, characterising degradation mechanisms and operational lifetime under various surface-handling and environmental conditions. Reports the long-term reliability data closest in wavelength to the 280 nm `mg-plus-uv-chain` output. **Relevance:** primary long-term-reliability evidence for CW BBO at deep UV — informs the 280 nm BBO failure-mode analysis in CHARTER §5.4 (LIDT ceiling, surface-degradation phenomenology, vendor-handling sensitivity).

### [Kubo98] Kubota et al. 1998 — Efficient 213 nm and 266 nm generation in Czochralski-grown β-BBO &nbsp; <span style="font-size:0.85em">`[P]`</span>

S. Kubota, H. Masuda, H. Kikuchi, K. Kondo, M. Oka, K. Tatsuki, T. Okamoto, N. Umezu, T. Fukui, H. Wada, K. Morita, in *OSA TOPS Vol. 17 — Diode Pumped Solid State Lasers: Applications and Issues*, M. W. Dowley (ed.), pp. 79–83 (Optical Society of America, 1998). DOI: [10.1364/DLAI.1998.FC4](https://doi.org/10.1364/DLAI.1998.FC4). Folder: [`Kubota1998/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Kubota1998/).

Compares Czochralski-grown to flux-grown β-BBO for 213 nm and 266 nm second-harmonic generation, characterising efficiency and damage-threshold differences between the two crystal-growth routes. Reports growth-method-dependent material quality at deep UV, with Czochralski growth offering improved homogeneity and crystal-orientation control at the cost of growth-time and yield. **Relevance:** BBO supplier and crystal-quality reference for the 280 nm output stage — informs procurement decisions on growth method when ordering the next BBO crystal.

### [Kuma15] Kumar et al. 2015 — High-power, high-rep-rate β-BBO performance for picosecond UV at 266 nm &nbsp; <span style="font-size:0.85em">`[P]`</span>

S. Chaitanya Kumar, J. Canals Casals, J. Wei, M. Ebrahim-Zadeh, *Opt. Express* **23**, 28091–28103 (2015). DOI: [10.1364/OE.23.028091](https://doi.org/10.1364/OE.23.028091). Folder: [`Kumar2015/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Kumar2015/).

Documents single-pass picosecond 266 nm SHG performance in β-BBO at high repetition rate, with measured LIDT and degradation-rate data across operating conditions including pulse energy, beam profile, and surface preparation. Reports the high-rep-rate / pulsed-regime BBO LIDT phenomenology. **Relevance:** pulsed-regime BBO LIDT data — out-of-regime for the CW `mg-plus-uv-chain` operating point, but supplies useful scaling-bound context on the surface-damage budget envelope and on the LIDT-vs-pulse-duration extrapolation.

### [Span23] Spanke 2023 — Benchmarking a solid-state laser for the manipulation of trapped ions &nbsp; <span style="font-size:0.85em">`[S]`</span>

T. Spanke, *Bachelor thesis*, Faculty of Mathematics and Physics, University of Freiburg (March 2023). Supervisor: Prof. Dr. Tobias Schätz; advisor: Dr. Ulrich Warring. Folder: [`Spanke2023/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Spanke2023/).

AG Schätz BSc that benchmarks the in-house "VECSEL Nr.4" (the [Kief20] / [Guth21] platform) and delivers two specific thermal-management improvements: replacement of the legacy Neslab water chiller with an Alphacool PC-water-cooling loop (eliminates chiller-cycle-driven ≈ 200 MHz peak-to-peak frequency oscillations) and a copper cooling sleeve on the pump-fibre output holder (-14 °C at 22.4 W pump). Net **factor-5 short-term frequency-stability improvement** to 300–400 kHz Allan deviation free-running (vs ≈ 1.6 MHz baseline in [Guth21]). **Relevance:** documents the dominant thermal-noise drivers of the in-house VECSEL and the engineering responses that closed them; the operational reference for the short-term free-running stability budget at 1118 nm prior to the [Span25] redesign.

### [Span25] Spanke 2025 — Next generation of solid-state lasers for the manipulation of trapped ions &nbsp; <span style="font-size:0.85em">`[S]`</span>

T. Spanke, *Master thesis*, Hochschule Karlsruhe University of Applied Sciences, work performed at AG Schätz / University of Freiburg (01.01.2025–30.06.2025). Folder: [`Spanke2025/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Spanke2025/).

Builds the "neXt VECSEL" (= Nr.6) — a ground-up redesign of the in-house platform with passive thermal radiation, A4-sheet footprint (≈ 16× volume reduction), Thorlabs PK44LA2P2 piezo, Thorlabs OI-3-1118-HP isolator, and a custom Raspberry-Pi-based 4-channel TEC controller (sub-€500 vs ≈ €2000–4000 per Arroyo TECSource channel). Achieves **101(8) kHz wavemeter-locked Allan deviation** at short timescales (with noise/temperature isolation enclosure) — the first in-house build in [Burd23] linewidth class at 1118 nm — and TEC long-timescale stability of 0.08 mK. **Relevance:** the **experimental underwriting** at the actual `mg-plus-uv-chain` operating point (1118 nm, ²⁵Mg⁺-targeted) of the seed-laser direction recorded 2026-05-08; demonstrates the [Burd23] design principles transferred end-to-end.

### [Tamo18] Tamosauskas et al. 2018 — Transmittance and phase matching of BBO in the 3–5 µm range &nbsp; <span style="font-size:0.85em">`[P]`</span>

G. Tamosauskas, G. Beresnevicius, D. Gadonas, A. Dubietis, *Opt. Mater. Express* **8**, 1410–1418 (2018). DOI: [10.1364/OME.8.001410](https://doi.org/10.1364/OME.8.001410). Folder: [`Tamosauskas2018/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Tamosauskas2018/).

Material-property characterisation of BBO transmittance and phase matching in the 3–5 µm mid-infrared range, applied to mid-IR pulse characterisation. Reports BBO optical constants and phase-matching curves for IR generation outside the `mg-plus-uv-chain` deep-UV operating band. **Relevance:** secondary BBO material-property reference — less directly applicable than [Eime87] for the 280 nm operating point, but cited as a Sellmeier cross-check for the wavelength-extension tail and as evidence that BBO Sellmeier behaviour is well-characterised across the full transparency window.

### [Turc22] Turčičová et al. 2022 — LIDT of β-BBO and CLBO: overview &nbsp; <span style="font-size:0.85em">`[S]`</span>

H. Turčičová, O. Novák, J. Mužík, D. Štěpánková, M. Smrž, T. Mocek, *Opt. Laser Technol.* **149**, 107876 (2022). DOI: [10.1016/j.optlastec.2022.107876](https://doi.org/10.1016/j.optlastec.2022.107876). Folder: [`Turcicova2022/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Turcicova2022/).

Review article surveying laser-induced damage threshold (LIDT) measurements for β-BBO and CLBO across pulse durations, wavelengths, and growth routes, with vendor / handling caveats. Reports the compiled LIDT data and identifies high-variance regimes in the literature where measurements disagree by factors of 2–10. **Relevance:** the canonical LIDT review used to set the 280 nm BBO surface-damage budget in `mg-plus-uv-chain` and to size the conservative-vs-aggressive operating-point trade space at the BBO output stage.

---

## See also

- [Phase 1 dossier](KD-2026-XXX-uv-280nm.html) — decision-keyed inventory that draws on this literature index.
- [Components — Friedenauer baseline](components/friedenauer-baseline.html) — components surface centred on [Frie06].
- [Components — Seed lasers (VECSEL)](components/seed-lasers.html) — components surface centred on the VECSEL cluster ([Burd16] · [Burd23] · [Kief20] · [Guth21] · [Span23] · [Span25]).
- [Principles](principles.html) — Coastline / Sail vocabulary; source-tier conventions; anti-seeding clause.
- [`data/literature/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/) — canonical extraction artefacts (`extracted.yaml` + `notes.md`) for every entry above.
