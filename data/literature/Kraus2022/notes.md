# Kraus2022 Extraction Notes

**Citation:** B. Kraus, F. Dawel, S. Hannig, J. Kramer, C. Nauk, P. O. Schmidt, "Phase-stabilized UV light at 267 nm through twofold second harmonic generation," *Optics Express* **30**, 44992-45003 (2022), DOI: `10.1364/OE.471450`. Affiliations: ¹Physikalisch-Technische Bundesanstalt (PTB), Braunschweig; ²DLR Institut für Satellitengeodäsie und Inertialsensorik, c/o Leibniz Universität Hannover; ³Institut für Quantenoptik, Leibniz Universität Hannover.

**Source available:** publisher PDF copied on 2026-05-13 to ignored path `downloads/literature/task-e/oe-30-25-44992.pdf`. The article is published under the Optica Open Access Publishing Agreement (per the page-1 copyright line), so the PDF **is admissible** for commit under the project's mixed-licence policy if the steward chooses to mirror it; this scaffold defers the decision.

## Why this paper

Identified in the third Task-E scout pass (2026-05-13) as an **architectural-alternative reference** for the UV-stage dossier. The paper reports phase-stabilised CW UV generation at 267.4 nm for the ²⁷Al⁺ optical-clock probe transition via **twofold single-pass SHG** (1069.6 nm fibre laser → 10 mm PPLN waveguide → 534.8 nm → 50 mm DKDP → 267.4 nm) — i.e. *no enhancement cavities at all*, and using a different non-linear crystal (DKDP, non-critical phase matching) than the BBO-cavity Friedenauer-class baseline.

Relevance to Task E and the broader dossier:

- **Architectural alternative.** Single-pass with PPLN waveguide + DKDP is a structurally different topology from the Friedenauer-class single-source-quadrupling-with-two-bow-tie-cavities baseline. The UV output power is much lower (>50 µW vs Friedenauer's 275 mW), but the *phase stability* is `<5×10⁻¹⁷` at 1 s (and `1×10⁻¹⁸` electronics-limited) — the relevant metric for the Al⁺ clock target. Maps to `KD-UV280-006` (alternative crystal at 280 nm) and to the alternative-topology slate (`logbook/2026-05-08-ic-vecsel-alternative-topology.md`, `logbook/2026-05-08-pulsed-raman-alternative-topology.md`).
- **DKDP at 267 nm as a CW operating regime.** Deuterated KDP allows non-critical Type-I phase matching at ~100 °C for the 534.8 → 267.4 nm process, avoiding walk-off. The 50 mm crystal length and ~32 µm focus waist correspond to an intracavity-equivalent intensity that is *much* lower than a cavity-enhanced BBO single-pass would carry; the operating regime is therefore in a different LIDT bracket than the BBO-cavity baseline.
- **Hannig as bridging author.** Hannig (PTB) co-authors both Hannig 2018 (BBO at 313 nm, 130 h CW stability) and this Kraus 2022 (DKDP at 267 nm). The PTB-Schmidt-group hardware lineage now spans both BBO-cavity and DKDP-single-pass UV-generation routes.

## Extraction targets

When the structured pass is run, extract:

1. **Source chain**: fibre laser at 1069.6 nm (vendor / model), output power (~1 W into the PPLN waveguide).
2. **PPLN stage** (1069.6 → 534.8 nm): HC Photonics waveguide, 10.3 mm length, AR-coated both wavelengths, intrinsic conversion efficiency ~125 % W⁻¹ at 45(20) °C, output power >0.2 W at 534.8 nm.
3. **DKDP stage** (534.8 → 267.4 nm): 50 mm length, non-critical Type-I phase matching at ~100 °C, d_eff ≈ 0.43 pm/V, temperature tuning bandwidth 3.2 K·cm, optimum focus waist 32 µm (Boyd-Kleinman), calculated single-pass conversion 0.15 % W⁻¹, output power >50 µW at 267.4 nm.
4. **Phase-stability characterisation**: fractional frequency instability `<5×10⁻¹⁷` at 1 s by beat-note against an independent FHG setup (cavity-enhanced waveguide + cavity FHG); in-loop electronics-limited instability `1×10⁻¹⁸` at 1 s. Method: back-reflection through the entire setup with active path-length stabilisation.
5. Cross-reference to ²⁷Al⁺ clock transition wavelength (267 nm), Hg⁺ at 282 nm (close to the Mg⁺ 280 nm Doppler target), In⁺ at 237 nm, Hg lattice clock at 266 nm — useful as a wider-field framing for the UV-clock-laser application landscape.

## Mapping to Task E quantities

- **Q1 (intrinsic CW damage threshold at 280 nm):** indirect. DKDP, not BBO. Low operating intensity (single-pass, 50 mm crystal).
- **Q2 (operational lifetime under CW UV):** not the headline figure (this paper measures phase stability, not lifetime); no quoted operating-hours-without-decay number from a casual abstract read.
- **Q3 (mechanism):** not addressed; the DKDP non-critical-Type-I route avoids walk-off so the mechanism set is different (DKDP is hygroscopic — `KD-UV280-009` gas-environment dependence is acutely relevant).
- **Q4 (institutional context):** PTB Braunschweig (Schmidt group). Same lineage as Hemmerling 2011, Hannig 2018. The DKDP-single-pass route is the *current* PTB-Schmidt-group choice for the ²⁷Al⁺ clock; this is useful context for understanding which architectures the institutional record bears on.

## Status

`SCAFFOLD` — bibliographic record confirmed against the publisher PDF, abstract and §1-2 (Introduction, Crystal selection) read. The DKDP single-pass architecture and the phase-stability headline are confirmed; full power-trace, environmental-stability, and DKDP-specific operating-condition details require a §3-4 read.

## Extraction passes

- **2026-05-13 (assistant under steward direction, SCAFFOLD).** Created bibliographic scaffold from the publisher PDF (now in hand under `downloads/literature/task-e/`). Confirmed authorship, journal volume/issue/year/DOI, abstract, and §2 (Crystal selection) architecture statement: 1069.6 nm fibre laser → 10.3 mm PPLN waveguide → 534.8 nm → 50 mm DKDP → 267.4 nm, both stages single-pass. Headline phase-stability result confirmed: <5×10⁻¹⁷ at 1 s (beat-note); 1×10⁻¹⁸ at 1 s (in-loop electronics-limited). Filed by the third scout pass in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../../../logbook/2026-05-04-bbo-cw-uv-lidt-task.md).
