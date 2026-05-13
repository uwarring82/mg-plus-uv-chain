# Shaw2021 Extraction Notes

**Citation:** J. C. Shaw, S. Hannig, D. J. McCarron, "Stable 2 W continuous-wave 261.5 nm laser for cooling and trapping aluminum monochloride," *Optics Express* **29**, 37140-37155 (2021), DOI: `10.1364/OE.441741`. Affiliations: ¹Department of Physics, University of Connecticut; ²Agile Optic GmbH, Braunschweig.

**Source available:** publisher PDF copied on 2026-05-13 to ignored path `downloads/literature/task-e/oe-29-23-37140.pdf`. The article is published under the OSA / Optica Open Access Publishing Agreement (per the page-1 copyright line), so the PDF **is admissible** for commit under the project's mixed-licence policy if the steward chooses to mirror it; this scaffold defers the decision.

## Why this paper

Identified in the third Task-E scout pass (2026-05-13) as a **high-payoff adjacent-wavelength CW DUV operational result on CLBO** (Task E branch D, "CLBO comparison literature"). The paper reports:

- **2.75 W peak / 2 W stable steady-state CW output at 261.5 nm** with >13 h stability, via two cascaded SHG cavities (LBO then CLBO) from a 1046 nm ECDL → fibre amplifier source.
- "Largely unexplored high-intensity regime in CLBO for continuous-wave DUV light" (abstract verbatim) — i.e. this is one of the cleanest published CLBO-at-DUV CW-power-scaling demonstrations on record, directly relevant to the CLBO arm of the alternative-crystal dossier.
- Monolithic aluminium-housing bow-tie cavity (manufactured by Agile Optic GmbH, co-author Hannig's company; same hardware lineage as Hannig 2018 at PTB).

The 261.5 nm result is *adjacent-wavelength* to the 280 nm Mg⁺ target: 261.5 nm sits ~ 47 nm above the BBO UV-onset (215 nm), so for the BBO arm the operating point is somewhat *closer* to the absorption edge than 280 nm is. For the CLBO arm, the operating point bracket is direct (CLBO is fielded across 213-280 nm in adjacent DUV applications). The paper does not report a CW-lifetime in the calendar-time sense (only 13 h stability) and is not a damage-threshold study, but the *output stability under multi-watt CW DUV* is a directly transferable bracket for the alternative-crystal dossier entries.

## Extraction targets

When the structured pass is run, extract:

1. Cavity architecture: bow-tie geometry, mirror ROCs, finesse, beam waist at LBO and CLBO crystals, monolithic-housing description and breadboard vibration damping (Sorbothane).
2. **LBO stage** (1046 nm → 523 nm): crystal dimensions, vendor, phase-matching geometry, temperature, fundamental input power, intracavity power, 523 nm output power.
3. **CLBO stage** (523 nm → 261.5 nm): crystal dimensions, vendor, phase-matching geometry (likely critical Type-I), temperature, intracavity 523 nm power, 261.5 nm output power and time-stability curve.
4. **2 W steady-state @ 261.5 nm over 13 h**: full operating envelope (intracavity intensity at CLBO, gas environment of the cavity housing, any active-stabilisation parameters), and the time-trace of output power if the body contains it.
5. **Source-laser chain**: homebuilt ECDL at 1046 nm, IPG YAR-10-1050-LP-SF fibre amplifier (~10.75 W output, M² ~ 1.05). Useful reference for VECSEL-class source-laser comparisons.
6. **Hyperfine-structure spectroscopy** results on AlCl A¹Π|v'=0, J'=1⟩ — out of scope for Task E / KD-UV280-* but useful for citation completeness.
7. Reference [17] in Shaw 2021 (cited as "similar previous design") — likely Hannig 2018; cross-validate against this scaffold's `Hannig2018/`.

## Mapping to Task E quantities

- **Q1 (intrinsic CW damage threshold):** not directly addressed for BBO; for CLBO, the "largely unexplored high-intensity regime" framing suggests no prior CW DUV high-intensity CLBO LIDT anchor was available — Shaw 2021 itself becomes the operating-point anchor at 261.5 nm / 2 W.
- **Q2 (operational lifetime):** 13 h continuous 2 W stable operation is shorter than Kondo1998 / Kubota1998's 1000 h frame, but is at substantially higher CW DUV output power. Becomes a power-and-time bracket on the CLBO arm.
- **Q3 (mechanism):** not addressed.
- **Q4 (institutional context):** UConn (McCarron group) and Agile Optic GmbH (Hannig). Hannig is the bridge author with the PTB Schmidt-group hardware lineage (Hannig 2018, Kraus 2022).

## Status

`SCAFFOLD` — bibliographic record confirmed against the publisher PDF, abstract and §1-2 (Introduction, Laser System) read. The 2 W / 13 h / 261.5 nm headline and the LBO + CLBO double-cavity architecture are confirmed; full crystal-geometry and operating-condition details require a §2-3 read.

## Extraction passes

- **2026-05-13 (assistant under steward direction, SCAFFOLD).** Created bibliographic scaffold from the publisher PDF (now in hand under `downloads/literature/task-e/`). Confirmed authorship, journal volume/issue/year/DOI, abstract, and §1-2 architecture statement (1046 nm ECDL + IPG YAR-10-1050-LP-SF amplifier → LBO bow-tie → 523 nm → CLBO bow-tie → 261.5 nm). Headline result confirmed: 2.75 W peak / 2 W steady-state at 261.5 nm over 13 h, "largely unexplored high-intensity regime in CLBO for CW DUV". Filed by the third scout pass in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../../../logbook/2026-05-04-bbo-cw-uv-lidt-task.md).
