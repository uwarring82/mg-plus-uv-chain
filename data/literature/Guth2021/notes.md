# Guth2021 Extraction Notes

**Citation:** L. Guth, *"Assembling and Benchmarking the Next Generation of Solid-State Laser Systems for Controlling Trapped Magnesium Ions,"* Master's thesis, Faculty of Mathematics and Physics, University of Freiburg, August 2021. Supervisor: Prof. Dr. Tobias Schätz.

**Source used:** AG Schätz internal copy of the deposited thesis PDF; held at [Guth2021.pdf](Guth2021.pdf) (not committed to repository).

## Why this thesis

Guth2021 is the **first MSc in the AG Schätz VECSEL-platform sequence after [Kiefer2020](../Kiefer2020/)**, and it does two operationally-important things: (i) produces the **first quantitative in-house VECSEL linewidth measurement** at the 1118 nm Friedenauer fundamental — 1.207(12) MHz iodine-locked at τ = 100 ms — and (ii) builds the **modular LBO + BBO frequency-doubling cavities** ("version 2" and "version 3") that achieve 87(6) % IR → visible conversion at 1.27 W coupled IR and 10.0(11) % visible → UV at 780 mW visible. The thesis is the in-house operational reference for the SHG chain that downstream `mg-plus-uv-chain` work points at.

The VECSEL itself is the prototype that [Kiefer2020](../Kiefer2020/) first describes (Vexlum gain mirror, NIST + Tampere design family). Guth2021 sets up the system in production form — Doppler-cooling laser at f = 268.001790(5) THz tuned to ²⁵Mg⁺, with 25Mg⁺ ions cooled near motional ground state using this VECSEL as the replacement for a defective Yb-fibre laser. A second VECSEL at λ = 1140 nm was being built in parallel as a photoionisation laser (red-detuned gain chip).

## What this extraction is for (and what it isn't)

- **It is** a Phase 1 literature artefact: an `[S]`-tier (thesis) capture of the VECSEL output power, linewidth, and tuning range; the LBO + BBO cavity geometries, conversion efficiencies, and Allan-deviation stabilities; and the iodine + wavemeter + beat-note frequency-locking implementations.
- **It is** the in-house operational reference for the SHG chain: when downstream architecture work needs in-house numbers for the Friedenauer-topology LBO + BBO chain at 1118 nm, this is the artefact to point at.
- **It is not** a build commitment or a Phase 4 scoring input.
- **It is not** a complete extraction of the thesis. Beam-profile measurement methods (Section 5.2 Attachment), gain-chip interlock details (Section 5.1), and beam-shaping optics are not extracted.

## Extraction Scope (2026-05-08 pass)

The 2026-05-08 pass extracts the body of the thesis:

- **§2.1 Vertical External-Cavity Surface-Emitting Laser as an Infrared Source.** VECSEL theory (gain chip GaInAs/GaAs, DBR, multiple QWs, strain-compensation layers, semiconductor heterostructure thermal physics: Δλ/ΔT ≈ 0.15 nm/°C); laser-head setup adapted from NIST [33]; assembly + adjustment; output beam shaping; frequency tunability via gain-chip + BRF + etalon temperatures and PZT cavity-length voltage.
- **§2.2 Frequency Multiplication via Second Harmonic Generation.** Theory of SHG (deff, phase matching, Boyd-Kleinman optimum focusing, build-up cavities); cavity geometries (bow-tie ring for LBO, ring for BBO); length stabilisation by Hänsch-Couillaud locking; "evolution" from cavity v2 to v3; assembly + adjustment.
- **§2.3 Frequency Stabilization.** Overlapping Allan deviation theory; wavemeter lock (HighFinesse, internal drift ≈ 10 MHz/day); Doppler-free iodine spectroscopy at f_b ≈ 536.0396 THz (benchmark manifold) and f_std ≈ 536.0409 THz (standard manifold); optical beat-note method; observed unresolved 56(4) MHz beat-note modulation between fibre laser and VECSEL (root cause not found within thesis).
- **§3 Results.** §3.1 thermalisation (three-phase model: gain chip 0–10 min, etalon 9–80 min, thermalised > 80 min; output drops to 80 % of peak after etalon phase). §3.2 frequency stability with Allan deviations comparing free-run / wavemeter-locked / iodine-locked at τ = 100 ms / 1 s / 100 s. §3.3 LBO cavity comparison (v3 vs v2: 87(6) % vs 56(4) % efficiency; figure of merit x' = 0.0008(2) vs 0.054(4) /√W). §3.4 generation of UV light (78(5) mW @ 280 nm from 780(15) mW visible — 10.0(11) % BBO efficiency).
- **§4 Discussion + Outlook.** Comparison to fibre laser (Tab. 8): VECSEL meets the atomic-linewidth requirement (≪ 41 MHz) but is ≈ 40 % broader than the fibre laser at 100 ms; tunability several × 100 GHz exceeds fibre; output power 2.8 W after laser head (vs 3 W fibre after fibre). Material cost ≈ €20,000 (moderate). VECSEL is operational replacement for the lapsed Koheras/Menlo Yb-fibre supply chain. Future BBO-cavity stability characterisation listed as open follow-up.

## Extraction Passes

- **2026-05-08 (assistant under steward direction, DRAFT).** Initial VECSEL+SHG-focused extraction. Status `DRAFT` (not yet steward-signed-off).

## Review Notes

- **First quantitative in-house VECSEL linewidth.** The 1.207(12) MHz iodine-locked figure is about 12× broader than Burd2016 / Burd2023 940 nm VECSELs. The in-house first build did not reach the Burd-class < 100 kHz performance — and that gap is the engineering target of [Spanke2025](../Spanke2025/), which delivers 101(8) kHz locked with the noise/temperature isolation box.
- **LBO v3 vs v2 jump = passive-loss reduction.** The figure of merit x' = L / (2 √E) decreases by ≈ 70× from v2 (0.054(4)/√W) to v3 (0.0008(2)/√W), translating into 87 % vs 56 % NIR → visible conversion at ~ 1.3 W coupled IR. This is the in-house operational benchmark for Phase NG-A (LBO `L_passive` gap closure in [`logbook/2026-05-08-next-gen-500mW-workplan.md`](../../../logbook/2026-05-08-next-gen-500mW-workplan.md)): cavity-build practice can produce sub-percent passive losses on the LBO ring at 1118 nm.
- **BBO cavity not yet stability-characterised.** The 78(5) mW @ 280 nm from 780 mW visible (10.0(11) %) is the only BBO-stage figure given. The thesis explicitly defers passive-loss and Allan-deviation characterisation to future work — this is an open follow-up that any downstream `mg-plus-uv-chain` work using the 280 nm BBO output should be aware of.
- **Beat-note modulation unresolved.** The 56(4) MHz width modulation observed in the VECSEL ↔ fibre-laser optical beat-note rules out optical beat-note locking until root cause is found. Candidates flagged in the thesis are SHG-cavity PZT noise and high-frequency VECSEL amplitude/frequency noise; neither was diagnosed.
- **Operational tip carried forward.** The recommendation to keep TECs and water-cooling active when the VECSEL is not in use (only the pump laser is switched off) is an operational practice that minimises warm-up thermalisation and is reused in [Spanke2023](../Spanke2023/) and [Spanke2025](../Spanke2025/).
- **SHG topology is Friedenauer2006.** The LBO bow-tie ring + BBO ring + Hänsch-Couillaud locking topology is the Friedenauer baseline ([Friedenauer2006](../Friedenauer2006/)), reproduced with the VECSEL substituted for the Yb-fibre seed. This thesis is the *operational* validation that the VECSEL seed-class direction and the LBO+BBO doubling-chain topology compose well — a literature artefact for the steward direction recorded 2026-05-08.

## Downstream Dossier Links

- `KD-UV280-015` (VECSEL pump option). Guth2021 is added as an `[S]`-tier in-house operational reference. Together with [Kiefer2020](../Kiefer2020/) (origin point), [Spanke2023](../Spanke2023/) (water-cooling fix), and [Spanke2025](../Spanke2025/) (next-generation neXt redesign), it forms the four-thesis chain that demonstrates the Burd2023 design principles transferred to the 1118 nm ²⁵Mg⁺ operating point.

## Cross-Reference to Steward Direction

This extraction lands as part of the same 2026-05-08 batch as [Kiefer2020](../Kiefer2020/), [Spanke2023](../Spanke2023/), and [Spanke2025](../Spanke2025/), all in service of the steward direction recorded in [`logbook/2026-05-08-vecsel-seed-lasers.md`](../../../logbook/2026-05-08-vecsel-seed-lasers.md). The components-page surface for the seed-laser layer lives at [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md).
