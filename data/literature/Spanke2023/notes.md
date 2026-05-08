# Spanke2023 Extraction Notes

**Citation:** T. Spanke, *"Benchmarking a Solid State Laser for the Manipulation of Trapped Ions,"* Bachelor thesis, Faculty of Mathematics and Physics, University of Freiburg, March 2023. Supervisor: Prof. Dr. Tobias Schätz; advisor: Dr. Ulrich Warring.

**Source used:** AG Schätz internal copy of the deposited thesis PDF; held at [Spanke2023.pdf](Spanke2023.pdf) (not committed to repository).

## Why this thesis

Spanke2023 is the **AG Schätz bachelor thesis that benchmarks the operational in-house VECSEL — locally called "VECSEL Nr.4" — and delivers two specific thermal-management improvements** that together produce a factor-≈5 reduction in short-term free-running frequency stability vs the [Guth2021](../Guth2021/) baseline: (i) replacement of the legacy Neslab RTE-111 water chiller with a PC-water-cooling loop based on Alphacool components (eliminates the chiller's cooling-cycle modulation that previously drove ≈ 200 MHz peak-to-peak periodic frequency oscillations), and (ii) redesign of the pump-fibre output holder with a copper cooling sleeve and copper cooling cable to the base plate (reduces the holder's temperature delta at 22.4 W pump from ≈ 35 °C to ≈ 21 °C, preventing pump-spot drift on the gain chip). The thesis is the operational reference for the *thermal-noise floor* of the 1118 nm in-house VECSEL prior to the [Spanke2025](../Spanke2025/) neXt redesign.

## What this extraction is for (and what it isn't)

- **It is** a Phase 1 literature artefact: an `[S]`-tier (thesis) capture of the thermal-noise drivers of the in-house VECSEL Nr.4 frequency stability and the engineering responses that closed them.
- **It is** the in-house operational reference for the *short-term* free-running frequency-stability budget at 1118 nm.
- **It is not** a build commitment or a Phase 4 scoring input.
- **It is not** a SHG-chain extraction. The LBO and BBO cavities are not re-characterised; those numbers come from [Guth2021](../Guth2021/) §3.3 (LBO 87(6) % at 1.27 W IR; BBO 10.0(11) % at 780 mW visible).
- **It is not** a complete extraction of the thesis. Datasheet appendices (etalon LightMachinery test report, BRF Newlight specs) are summarised inline above; engineering drawings (fibre-coupler helper bracket) are not extracted.

## Extraction Scope (2026-05-08 pass)

The 2026-05-08 pass extracts the body of the thesis:

- **§2 Methods.** VECSEL operating principle (ref. NIST [16], Vexlum gain chip GaInAs/GaAs at 1118 nm, gain chip VL1120_4477_842), pump laser (Ostech 40 W 808 nm Nr.4, mfg linewidth 0.3 nm @ 25 °C, conversion chart for current → optical output), optical assembly (Brewster-window output, 250 mm collimating lens, 1 % photodiode pickoff, dual-path fibre-coupler split with monitor + experiment paths), VECSEL setup (FeNi36 Invar baseplate, BRF, etalon, piezo, water-cooled gain-chip mount), gain-chip assembly (peltier-cooled copper heat sink with closed-loop water cooling), birefringent filter (Newlight Photonics BIR0030, datasheet incl. Sellmeier coefficients and birefringence at 1064 nm), etalon (LightMachinery OP-3167-1000 1.004 mm YAG, FSR 82.3 GHz, temperature-tuning slope 10.8 pm/°C), piezo mirror, optical processing (high-finesse wavemeter Fizeau-interferometer-based), temperature stabilisation (Arroyo Instruments 7154-04-08 TEC MultiSource, 4 channels), Allan deviation theory.
- **§3 Results.**
  - **§3.1 Tunability.** BRF temperature scan (24 °C nominal, mode jump at 33 °C); etalon temperature scan (~ 10 GHz frequency tunability via thermal range); outcoupling-mirror piezo gain 78.41(41) MHz/V (one branch) and 93.91(333) MHz/V (a second mode).
  - **§3.2.1 Watercooling loop.** Old chiller drove 200 MHz peak-to-peak frequency oscillations synchronous with chiller compressor cycle (Fig. 19). Replacement loop: Alphacool Eisstation 40 DC-LT + DC-LT 3600 pump + NexXxoS UT60 radiator + 2× Noctua NF-A4x20 + Keyestudio W5500 Ethernet fan controller. Best configuration (piezo terminated to 50 Ω, flow 150 l/h, fan duty 50 %): Allan deviation 308.5(98) kHz / 159.2(51) kHz / 488.5(312) kHz at short / mid / long timescales. 24-hour measurement: 473.2 / 335.4 / 937.8 kHz. Long-term variance is far below the 100 MHz piezo correction range. Operating limit: 22.4 A pump current (~ 22.4 W) takes the radiator to 41 °C — too warm for the gain-chip Peltier to hold T_GC = 25 °C.
  - **§3.2.2 Pump fiber output.** Holder thermal probe shows ΔT = 20 °C at 13 W pump rising to 35 °C at 22.5 W with the old steel coupler. New coupler + copper cooling sleeve + copper cooling cable: ΔT = 21 °C at 22.4 W pump (14 °C reduction). Most heat is radiated from the cooling cable into the cavity rather than transferred to the housing — heat-transfer-cable length variation has no measurable effect. Frequency-stability comparison before/after fibre-coupler replacement (Fig. 26): short and mid timescales essentially unchanged; long-timescale slightly worse but within run-to-run variation.
- **§4 Discussion and Outlook.** Headline: short-term stability 700 kHz typical (400 kHz with fine tuning) — factor-5 improvement over [Guth2021](../Guth2021/) free-running. Mid-term 300 kHz consistently — improvement from 700 kHz. New water cooling adds no further noise such as vibrations. Larger radiator listed as future work for > 20 W continuous pump.
- **§5 Attachment.** Fiber-coupler helper bracket (3D-printed); etalon datasheet (LightMachinery test report 2020); BRF datasheet (Newlight BIR0030); references; declaration; acknowledgements (Schätz, Warring, Müller, Denter, lab colleagues).

## Extraction Passes

- **2026-05-08 (assistant under steward direction, DRAFT).** Initial VECSEL+SHG-focused extraction. Status `DRAFT` (not yet steward-signed-off).

## Review Notes

- **Headline operational fact.** Short-term free-running frequency stability of the in-house VECSEL improved by ~ 5× (1.6 MHz → 300–400 kHz) by replacing one chiller and reworking one fibre-holder. The bottleneck of the system at this point is *thermal*, not *acoustic* or *optical*.
- **The chiller was driving the laser frequency.** Fig. 19 shows the old chiller's compressor cycle modulating the gain-chip TEC current (because the water-temperature setpoint oscillates) and the laser frequency (≈ 200 MHz peak-to-peak). This is a textbook lesson on water-cooling-loop design for narrow-linewidth seed lasers.
- **Pump-fibre output holder is a noise source.** The 35 °C delta-T at 22.4 W pump moves the pump spot on the gain chip — reducing output power and likely contributing to higher-order noise. The 14 °C reduction with the copper cooling sleeve is significant.
- **Long-term drift is within the piezo range.** Long-term Allan variance is far below the 100 MHz piezo correction limit, so the laser can run free for several hours and still be steered by piezo. Iodine or wavemeter lock is needed only for absolute-frequency reference and *longer*-term operation.
- **Outlook informs Spanke2025.** Future work listed in §4 — larger radiator for > 20 W continuous pump — was not pursued in incremental form. [Spanke2025](../Spanke2025/) instead removed water cooling for the gain chip entirely in the neXt VECSEL (passive radiation only) and cut volume by ~ 16×. The thermal-management lesson from Spanke2023 is that further refinement of active water cooling has diminishing returns; the larger system-level move is to redesign the thermal management end-to-end.

## Downstream Dossier Links

- `KD-UV280-015` (VECSEL pump option). Spanke2023 is added as an `[S]`-tier in-house operational reference. Together with [Kiefer2020](../Kiefer2020/), [Guth2021](../Guth2021/), and [Spanke2025](../Spanke2025/), it forms the four-thesis chain of the in-house VECSEL platform.

## Cross-Reference to Steward Direction

This extraction lands as part of the same 2026-05-08 batch as [Kiefer2020](../Kiefer2020/), [Guth2021](../Guth2021/), and [Spanke2025](../Spanke2025/), all in service of the steward direction recorded in [`logbook/2026-05-08-vecsel-seed-lasers.md`](../../../logbook/2026-05-08-vecsel-seed-lasers.md). The components-page surface for the seed-laser layer lives at [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md).
