# Hannig2018 Extraction Notes

**Citation:** S. Hannig, J. Mielke, J. A. Fenske, M. Misera, N. Beev, C. Ospelkaus, P. O. Schmidt, "A highly stable monolithic enhancement cavity for second harmonic generation in the ultraviolet," *Review of Scientific Instruments* **89**, 013106 (2018), DOI: `10.1063/1.5005515`. Affiliations: ¹Physikalisch-Technische Bundesanstalt (PTB), Braunschweig; ²Institut für Quantenoptik, Leibniz Universität Hannover.

**Source available:** publisher PDF copied on 2026-05-13 to ignored path `downloads/literature/task-e/013106_1_online.pdf`. The article is Creative Commons CC-BY 4.0 (per the published copyright line on page 1), so the PDF **is admissible** for commit under the project's mixed-licence policy if the steward chooses to mirror it; this scaffold defers that decision to the steward.

## Why this paper

Identified in the third Task-E scout pass (2026-05-13) as the **closest published "long uninterrupted CW operation at ~UV wavelength in a Brewster-cut BBO bow-tie cavity"** result available. The paper reports **130 h uninterrupted operation without decay in output power at 313 nm**, using a Brewster-cut BBO crystal in a bow-tie power-enhancement cavity that is architecturally a direct relative of the Friedenauer 2006 / Hemmerling 2011 cavities. The cavity geometry is also explicitly stated to be "suitable for all UV wavelengths reachable with BBO" — i.e. transferable to the 280 nm Mg⁺ stage.

The 313 nm result is *adjacent-wavelength* to the 280 nm Mg⁺ target: 313 nm sits deeper into the BBO transparency window (well above the 215 nm UV onset, and farther from it than 280 nm), so the 130 h figure represents an *upper-wavelength* operational anchor rather than a tight 280 nm bound. The paper itself does not report a 280 nm operation lifetime. Still, this is one of the cleanest published examples of "no decay over multi-day BBO-cavity CW operation in the UV" and the PTB-Schmidt group is the same lineage that produced Hemmerling 2011 and Kraus 2022.

## Extraction targets

When the structured pass is run, extract:

1. Cavity architecture: bow-tie geometry, mirror radii of curvature, finesse, free spectral range, beam waist at BBO.
2. Crystal: Brewster-cut β-BaB₂O₄ dimensions, vendor (if stated), phase-matching geometry (Type-I, critical), operating temperature.
3. Pump wavelength (626 nm for 313 nm Doppler cooling of ²⁷Al⁺ logic ion is the Schmidt-group target; verify in body).
4. Fundamental input power, intracavity power, and 313 nm UV output power.
5. **130 h uninterrupted operation at 313 nm** — full operating envelope (intracavity intensity at BBO, gas environment of the cavity enclosure, any active stabilisation against environmental drift).
6. **Robustness to vibration**: 1 g acceleration with <10 % in-lock output-power variation; 30 min at 3 g_rms; relevant for transportable-setup readiness (orthogonal to Task E but directly relevant to the next-gen 500 mW workplan).
7. **Stabilisation electronics**: STEMlab 125-14 (Red Pitaya) digital PI controller acting on a fast-piezo-mounted mirror. The PID runs in the FPGA with D set to zero for cavity locking. The modified application source is publicly available, but §IV.C.1 explicitly states that the board hardware is not open source; source availability alone does not establish licence coverage for every modified file.
8. Authors' own comparison vs commercial monolithic UV-SHG modules (the paper notes that at the time of writing "no single-crystal monolithic ring cavities or modules are available for UV generation below 350 nm").

## Mapping to Task E quantities

- **Q1 (intrinsic CW damage threshold at 280 nm):** not directly addressed; 313 nm operation does not bound 280 nm intrinsic threshold.
- **Q2 (operational lifetime under CW UV):** **strongest contribution.** 130 h at 313 nm with no observed power decay is a clean upper-wavelength CW-BBO operational-lifetime anchor. Combined with Kondo1998 / Kubota1998 at 266 nm (1000 h with 5×10⁻⁵ %/h cavity-loss-rate increase), Hannig2018 brackets the 280 nm wavelength regime from above.
- **Q3 (mechanism):** not addressed beyond "no decay observed".
- **Q4 (institutional context):** PTB Braunschweig (Schmidt group) — same institutional lineage as Hemmerling2011, Kraus2022. The Schmidt-group operational record on Brewster-cut BBO UV cavities is a relevant `[I]` corroboration candidate; this paper is one of the most-cited public-record artefacts of that lineage.

## Status

`SCAFFOLD` — bibliographic record confirmed against the publisher PDF, abstract and §I (Introduction) read, with a targeted controller and lock-performance review of §§IV–V on 2026-09-15. No full structured numerical extraction yet. The 130 h figure, the 313 nm wavelength, and the architecture-family attribution are confirmed; details of intracavity power, beam waist, crystal vendor, and the cavity gas environment still require a full extraction pass.

## Controller reference check (2026-09-15)

For the [public SHG catalogue's planned electronics section](../../../docs/components/shg-designs.html#cavity-lock-electronics), the publisher text distinguishes:

- **§IV.B–C, pp. 013106-5–6:** Hänsch–Couillaud sensing, FPGA PI control, two fast input and two output channels at 125 MS/s and nominal 14-bit resolution, remote/local interfaces, controller additions and eightfold output amplification. The piezo connection includes a 21.2 kHz low-pass filter.
- **§IV.D.2, p. 013106-7:** the 155 ns controller group delay suggests a few-MHz maximum closed-loop bandwidth. This is a delay-based estimate, not the measured bandwidth of the complete piezo/cavity system.
- **§V.A–C, pp. 013106-7–8:** 130 h uninterrupted lock; a broad resonance near 17 kHz sets the lock-bandwidth upper limit, probably from the mirror/piezo/holder; a separate vertical acceleration test retains lock up to about 1 g with output fluctuations at the 10% level.

The public code in ref. 67 was checked at
[`Julia-F/RedPitaya`, commit `7938c27`](https://github.com/Julia-F/RedPitaya/tree/7938c27fc030ca5d8d13b1731f559e33585458f1)
(26 May 2016). `COPYING` lists BSD-covered directories using names such as
`Applications` and `FPGA`, while the modified files are under `apps-free/pid2`
and `fpga/rtl`. The inspected `pid.c` and `red_pitaya_pid2.v` headers carry
author/copyright notices without resolving that path-scope discrepancy.
This check does not establish comprehensive code licence coverage or match
the snapshot to laboratory firmware. No source code is imported.

The laboratory's planned use is a Steward-provided intention. The published
performance applies to Hannig's 313 nm cavity and establishes no hardware
association or performance for the archived SHG designs. See the
[work record](../../../logbook/2026-09-15-shg-cavity-lock-electronics.md).

## Extraction passes

- **2026-05-13 (assistant under steward direction, SCAFFOLD).** Created bibliographic scaffold from the publisher PDF (now in hand under `downloads/literature/task-e/`). Confirmed authorship, journal, volume, year, DOI, abstract, and §I reference to the Friedenauer-class architecture lineage. Filed by the third scout pass in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../../../logbook/2026-05-04-bbo-cw-uv-lidt-task.md).
- **2026-09-15 (assistant under steward direction, targeted review).** Checked §§IV–V for the public controller planning reference and corrected the blanket “open-source” description. `extracted.yaml` remains a scaffold; no project parameters or gate states changed.
