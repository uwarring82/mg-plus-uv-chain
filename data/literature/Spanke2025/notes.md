# Spanke2025 Extraction Notes

**Citation:** T. Spanke, *"Die nächste Generation von Festkörperlasern für die Manipulation von gefangenen Ionen / Next Generation of Solid State Lasers for the Manipulation of Trapped Ions,"* Master thesis, Studiengang Elektro- und Informationstechnik (Sensorsystemtechnik), Hochschule Karlsruhe University of Applied Sciences. Work performed at AG Schätz / Faculty of Mathematics and Physics, University of Freiburg, 01.01.2025–30.06.2025 (the thesis title page lists "31.06.2025", which is a typo). Referees: Prof. Dr.-Ing. Christian Karnutsch (HKA), Prof. Dr. Harald Sehr (HKA); on-site supervisors: Prof. Dr. Tobias Schätz, Dr. Ulrich Warring.

**Source used:** AG Schätz internal copy of the deposited thesis PDF; held at [Spanke2025.pdf](Spanke2025.pdf) (not committed to repository).

## Why this thesis

Spanke2025 builds the **"neXt VECSEL"** (= VECSEL Nr.6 in in-house numbering) — a complete ground-up redesign of the in-house VECSEL platform with three headline outcomes:

1. **5× linewidth improvement** to 101(8) kHz wavemeter-locked at short timescales (free-running 110(4) kHz with the noise/temperature isolation enclosure), bringing the in-house build into [Burd2023](../Burd2023/)-class linewidth performance for the first time at the 1118 nm operating point.
2. **≈ 15–16× volume reduction** to an A4-sheet footprint (260 × 177 mm) housing the VECSEL cavity + optical isolator + λ/2 + PBS + 2 fibre couplers in a single aluminium enclosure.
3. **~ 10× cost reduction** of the TEC control infrastructure: a custom Raspberry-Pi-based controller replaces 4× Arroyo TECSource units (~ €2000–4000 each → sub-€500), delivering long-timescale TEC Allan deviation 0.08 mK (surpassing the Arroyo manufacturer spec of < 4 mK/h).

Volume reduction is achieved by **removing the active water-cooling loop entirely**: the gain chip is passively radiated through the aluminium housing with Peltier control on the chip itself. This is the systems-level extension of the [Spanke2023](../Spanke2023/) lesson that further refinement of active water cooling had diminishing returns.

The neXt system is the first AG Schätz in-house build to satisfy the **seed-laser linewidth budget** set in [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md) (target ≤ 100 kHz; floor ≈ 200 kHz Friedenauer parity; ceiling 50 kHz Burd2016 stretch). The 101(8) kHz locked, with-box short-timescale figure is at the wavemeter resolution limit, so it is an *upper bound* — true linewidth is likely lower and would need delayed self-heterodyne interferometry to characterise (suggested in the thesis Outlook §5).

## What this extraction is for (and what it isn't)

- **It is** a Phase 1 literature artefact: an `[S]`-tier (thesis) capture of the neXt VECSEL hardware, frequency stability, tuning behaviour, and turnkey reproducibility.
- **It is** the in-house operational reference for *Burd2023-class linewidth* at the 1118 nm Friedenauer fundamental — i.e. the experimental underwriting of the steward direction recorded 2026-05-08 (`logbook/2026-05-08-vecsel-seed-lasers.md`).
- **It is not** a build commitment or a Phase 4 scoring input.
- **It is not** a SHG-chain extraction. The LBO and BBO cavity efficiencies are unchanged from [Guth2021](../Guth2021/); a re-measurement of those cavities driven by the 5× narrower neXt seed would be a natural next experiment (open follow-up).
- **It is not** a complete extraction of the thesis. Beam-profile measurement methods (Section 5.2 Attachment / Comparison of beam-profile measurement methods), engineering drawings, and gain-chip interlock circuit details are not extracted in full.

## Extraction Scope (2026-05-08 pass)

The 2026-05-08 pass extracts the body of the thesis:

- **§1 Introduction + Personal contribution.** Motivation (replace dye-laser-based 280 nm system; replace fibre lasers with manufacturer-discontinued supply chain); design objectives (compact for 19" rack; commercial-dye-laser-class linewidth; turnkey operation; mechanical-adjustment-free wavelength selection); scope (complete redesign of existing VECSEL platform); explicit acknowledgement of NIST [16] = [Burd2016](../Burd2016/) origin.
- **§2.1 Components of the optical setup.**
  - **§2.1.1** VECSEL theory; semiconductor-laser classification (edge- vs surface-emitting; VCSEL vs VECSEL); gain-chip structure (window layer + multiple QWs + DBR; resonant-periodic-gain microcavity); thermal effects on emission (Δλ/ΔT ≈ 0.15 nm/°C).
  - **§2.1.2** BRF (Lyot filter) at Brewster angle ~ 57°; rotation tuning; temperature tuning.
  - **§2.1.3** Etalon (Light Machinery OP-3167-1000, 1.004 mm × 5 mm dia, FSR 82.3 GHz at 1064 nm spec, **measured 72 GHz at 1118 nm in §3.1.2**); temperature tuning rate ~ 10.8 pm/°C.
  - **§2.1.4** Piezo mirror (Thorlabs PK44LA2P2); 0–150 V; piezo gain measured 78.41(41) MHz/V (matching Spanke2023) on one branch and 93.91(333) MHz/V on a second mode.
  - **§2.1.5** Gain chip — Vexlum VL1120 family; emission 1119–1124 nm at 10–45 W pump (output 2.6–3.8 W); gain-chip temperature stabilised by Peltier + heat sink + (in Nr.4) closed-loop water cooling.
  - **§2.1.6** Frequency stability theory: Allan deviation; wavemeter / lock control bandwidth limit (PID system control rate 0.1 s).
  - **§2.1.7** VECSEL Nr.4 — the legacy reference system (Spanke2023 + Guth2021 + Kiefer2020 platform on a 19" rack); set up in parallel for comparison; Invar (FeNi36) plate, BRF, etalon, water-cooled gain chip, Arroyo 7154 4-channel TECs, OsTech pump.
  - **§2.1.8** VECSEL Nr.6 (neXt) — A4-sheet footprint aluminium enclosure; passive radiation thermal management; intra-cavity assembly on removable aluminium pieces for assembly outside the housing; Vexlum gain chip + Light Machinery etalon + Light Machinery BRF; Thorlabs OI-3-1118-HP optical isolator; gas fittings included for future dry-N₂ purge.
- **§2.2 Data acquisition.** InfluxDB (time-series database); wavemeter; photodiode laser-power readout.
- **§2.3 Control systems.** Frequency lock to wavemeter via PID + piezo (control bandwidth limited to 1/(0.1 s) = 10 Hz); temperature stabilisation; thermoelectric cooling (Peltier theory); PID control loop; temperature tuning. Custom Raspberry-Pi-based 4-channel TEC controller replaces Arroyo TECSource; sub-€500 cost vs ~ €2000–4000 per-channel Arroyo; supports network connectivity.
- **§3.1 Tunability results.**
  - **§3.1.1** BRF temperature scan 20–35 °C; mode jump at 33 °C; nominal operating T_BRF = 24 °C.
  - **§3.1.2** Etalon temperature scan 20–35 °C; FSR 72 GHz measured at 1118 nm; etalon thermal-tuning span ~ 10 GHz before mode-hop.
  - **§3.1.3** Outcoupling-mirror piezo gain 78.41(41) MHz/V; mode-hop-free 1 GHz across 0–150 V piezo travel.
- **§3.2 Stability results.**
  - **§3.2.1** Temperature stability: TEC2 Allan deviation 20 mK at short timescales → 0.08 mK at long timescales (24 h measurement; surpasses Arroyo spec of < 4 mK/h).
  - **§3.2.2** Free-running frequency stability — without isolation box: 1.3(0.06) MHz at short → 4.7(0.6) MHz at long. *With isolation box*: 110(4) kHz at short → 2.7(0.2) MHz at long. The isolation box reduces 1–100 Hz acoustic noise by ≈ 3 dB average.
  - **§3.2.3** Locked frequency stability with isolation box: 101(8) kHz / 172(14) kHz / 140(30) kHz at short / mid / long timescales. Wavemeter resolution 100 kHz is the measurement floor at short timescales — true linewidth likely lower.
- **§3.3 Turnkey operation.** After overnight off-state (pump laser only, TECs maintained) + 1 h thermalisation, frequency returns to within 250 MHz of previous value — well within the 1 GHz piezo correction range. Single-mode operation re-established without user intervention.
- **§4 Discussion.** Improvements summarised: 5× linewidth (vs Spanke2023 baseline); 10× cost reduction in TEC controllers; same usability (mimics Arroyo network interface for the higher-level control software). Tunability covers all ²⁵Mg⁺ transitions after frequency-quadrupling (279.5–281 nm window).
- **§5 Outlook.** Suggested next steps: (i) delayed self-heterodyne interferometry to measure linewidth below wavemeter resolution; (ii) replace Thorlabs isolator with more compact Newport 05-1064 to fit λ/2 between isolator and PBS; (iii) decouple pump-fibre mount from BRF/etalon assembly to streamline alignment; (iv) deploy dry-air or inert-gas purge through the existing gas fittings; (v) intracavity-loss monitoring via photodiodes on Raspberry-Pi ADC channels; (vi) piezo-driven mirrors for automated alignment.
- **Appendix A Assembly and adjustment.** Step-by-step neXt VECSEL build procedure; optical-path alignment with red laser pointer; pump-spot adjustment via 8 A pump (≈ 2 W) and gain-chip tilting.

## Extraction Passes

- **2026-05-08 (assistant under steward direction, DRAFT).** Initial VECSEL-focused extraction. Status `DRAFT` (not yet steward-signed-off).

## Review Notes

- **First in-house Burd2023-class linewidth.** The 101(8) kHz wavemeter-locked figure brings the in-house 1118 nm system into the same linewidth class as Burd2023 (< 100 kHz at 940 nm). For the steward direction recorded 2026-05-08 (VECSEL as seed-laser source class), this is the *experimental* underwriting at the wavelength-matched, ²⁵Mg⁺-targeted operating point — not just the *literature* underwriting from Burd2023 / Burd2016.
- **The isolation box matters.** Going from 1.3 MHz (no box) to 110 kHz (with box) — a 12× improvement — at fixed cavity is a ≈ 3 dB acoustic reduction. The takeaway is that in-laboratory acoustic + thermal pickup was the dominant noise source at short timescales; the box closes that channel.
- **Wavemeter resolution is now the linewidth-measurement bottleneck.** The 101(8) kHz / 110(4) kHz / 140(30) kHz numbers all sit at or near the 100 kHz wavemeter resolution. Any further linewidth narrowing or characterisation needs delayed self-heterodyne (or a beat-note against another reference). This is a measurement-infrastructure follow-up, not a laser follow-up.
- **Passive thermal management works.** Removing the water-cooling loop *did not degrade* short-term stability and reduced volume by ≈ 16×. Combined with [Spanke2023](../Spanke2023/)'s observation that water-cooling refinement had diminishing returns, this is the systems-level proof that the seed-laser layer can run on passive radiation + per-element TECs alone, without per-laser water plumbing. For `mg-plus-uv-chain` build planning, this materially changes the rack-space and infrastructure assumptions for the seed-laser layer.
- **Cost compression of the controller.** Replacing 4× Arroyo TECSource (~ €2000–4000 each → sub-€500 total) is a > 10× cost reduction in the TEC-control infrastructure of the seed-laser layer. The Raspberry-Pi-based controller is a forward-compatible platform: it has additional ADC channels and compute headroom for future automation (intracavity-loss monitoring, automated alignment). The vendor-supplied Arroyo network protocol is mimicked, so higher-level control software needs no migration.
- **SHG follow-up not yet measured.** The Guth2021 LBO + BBO cavities (LBO v3 87(6) % at 1.27 W IR; BBO 10.0(11) % at 780 mW visible) have not been re-measured with the neXt seed. Re-measuring with a 5× narrower seed would test the Burd2023 design principle directly: does the narrower seed reduce the cavity-locked-output amplitude noise via the frequency-noise-to-amplitude-noise transfer function? This is an *open* experimental question.

## Downstream Dossier Links

- `KD-UV280-015` (VECSEL pump option). Spanke2025 is added as an `[S]`-tier in-house operational reference. With [Kiefer2020](../Kiefer2020/), [Guth2021](../Guth2021/), and [Spanke2023](../Spanke2023/), it forms the four-thesis chain of the in-house VECSEL platform — Kiefer2020 (origin) → Guth2021 (first quantitative numbers + LBO/BBO build) → Spanke2023 (water-cooling fix) → Spanke2025 (neXt redesign with 5× linewidth + 16× volume + 10× cost improvements).

## Cross-Reference to Steward Direction

This extraction lands as part of the same 2026-05-08 batch as [Kiefer2020](../Kiefer2020/), [Guth2021](../Guth2021/), and [Spanke2023](../Spanke2023/), all in service of the steward direction recorded in [`logbook/2026-05-08-vecsel-seed-lasers.md`](../../../logbook/2026-05-08-vecsel-seed-lasers.md). The components-page surface for the seed-laser layer lives at [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md). Spanke2025's 101(8) kHz locked linewidth is the experimental anchor for the "target ≤ 100 kHz" *Sail* recommendation in that page's seed-laser linewidth budget table.
