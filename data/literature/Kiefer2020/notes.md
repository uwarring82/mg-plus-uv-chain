# Kiefer2020 Extraction Notes

**Citation:** P. Kiefer, *"Playing tricks to phonons - Floquet engineering in a two-dimensional array of trapped ions,"* Ph.D. dissertation, Albert-Ludwigs-Universität Freiburg (defended 2020-03-03), 158 pp. Supervisors: Prof. Dr. Tobias Schätz (1st), Prof. Dr. Giuseppe Sansone (2nd).

**Source used:** AG Schätz internal copy of the deposited dissertation PDF; held at [Kiefer2020.pdf](Kiefer2020.pdf) (not committed to repository).

## Why this thesis

Kiefer2020 is the **dissertation in which the AG Schätz / `mg-plus-uv-chain` VECSEL platform first appears as a built and characterised laser at the 1118 nm Friedenauer fundamental**. Section 3.3 ("Laser system for generation of ultraviolet radiation") is the in-house implementation of the NIST + Tampere VECSEL design referenced in [Burd2016](../Burd2016/) and refined in [Burd2023](../Burd2023/). The vendor-part chain that first appears here — Vexlum gain mirror, Layertec outcoupler, LightMachinery etalon, Newlight Photonics BRF, Ostech 40 W 808 nm pump, Arroyo TECs, HighFinesse WSU-30 wavemeter — propagates through [Guth2021](../Guth2021/), [Spanke2023](../Spanke2023/), and [Spanke2025](../Spanke2025/) and is the practical evidence for the steward direction recorded on 2026-05-08 (`logbook/2026-05-08-vecsel-seed-lasers.md`).

The science focus of the dissertation is Floquet engineering with ²⁵Mg⁺ in a 2-D triangular three-site array; this extraction is restricted to the laser-system and beam-setup chapters (§3.3, §3.4) — the Floquet-physics chapters (§1–§2, §4–§7) are out of scope for `mg-plus-uv-chain` literature work.

## What this extraction is for (and what it isn't)

- **It is** a Phase 1 literature artefact: an `[S]`-tier (thesis) capture of the in-house VECSEL + SHG-chain implementation parameters at the 1118 nm operating point, with vendor / part-number specificity.
- **It is** the in-house reference that anchors the Burd2016 and Burd2023 design-principles to a wavelength-matched, ²⁵Mg⁺-targeted, *operational* system.
- **It is not** an architecture-family-specific simulation. No `/src/` change is implied. The anti-seeding clause (`docs/principles.md` §5.1) is unaffected.
- **It is not** a build commitment or a Phase 4 scoring input. Source-class scoping is upstream of axis-1 (Raman capability) and axis-2 (phase coherence) scoring.
- **It is not** a complete extraction of the dissertation. Floquet engineering, ion-trap apparatus, control system, and experimental-method chapters are not extracted.

## Extraction Scope (2026-05-08 pass)

The 2026-05-08 pass extracts §3.3 and §3.4 of the dissertation:

- **§3.3.1 VECSEL — Source in the near-infrared regime.** Cooling block + gain mirror (Vexlum, 3×3×0.3 mm CVD diamond heat spreader, TE-Tech HP-199 Peltier + Mikros 02749 microchannel water cooling, invar carrier), outcoupler (Layertec custom, R = 97.5(3) % at 1118 nm, RoC = 200(2) mm, glued onto a Physik Instrumente P-080.311 ring piezo), 128 mm linear cavity (g = 0.36, TEM₀₀ 1/e² = 370 µm on chip / 620 µm on outcoupler), pump (Ostech dst11-DILAS 40 W 808 nm VBG-stabilised, OzOptics focuser to 320 µm spot at 17 mm working distance), frequency-selective elements (Newlight BIR0030 quartz BRF, LightMachinery OP-3167-1000 YAG etalon FSR 82.3 GHz nominal at 1064.15 nm), aluminium enclosure on invar baseplate.
- **Characterization:** P_out = 4.5(1) W single-mode at maximum pump (P*_pump,ts = 2.25(5) W multi-mode threshold; single-mode threshold 3.7(5) W); optical-to-optical efficiency 28.2(3) % multi-mode / 12.4(3) % single-mode. Emission range 1116–1122 nm covering 4λ_D2 ≈ 1118.5 nm and 4λ_D1 ≈ 1121.4 nm. Coarse tuning 0.12–0.15 nm/K via gain-chip temperature; fine tuning by BRF + etalon temperature (25–70 °C range). Linewidth quoted as ≈ 50(10) kHz from a similar setup ([Burd2016](../Burd2016/) [46]) — not measured directly. Long-term passive frequency drift < 50 MHz over ≈ 1 hour.
- **§3.3.2 Harmonic generation and frequency stabilization.** LBO bow-tie ring cavity (Hänsch-Couillaud-locked, critically phase-matched by temperature) for NIR → 559 nm; alternative PPLN waveguides limited to ≈ 500 mW visible vs > 1 W from LBO. BBO ring cavity for 559 nm → 280 nm. Reference [110] in §3.3.2 cites [Friedenauer2006](../Friedenauer2006/) — i.e. the SHG topology is the Friedenauer baseline, ported onto the in-house VECSEL seed. Iodine Doppler-free saturation spectroscopy + HighFinesse WSU-30 wavemeter (350–1120 nm, 4-channel switch) for frequency lock; AOM-bridged 10 MHz gaps between iodine line and target wavelength.
- **§3.4 Optical beam setup.** Four AOMs (Intraaction ASM-2202B3 / ASM-1202LA3) on four-axis tilt stages, single-pass η ≈ 80 % / double-pass > 60 %; first AOM after final SHG serves as TEM Messtechnik Noise Eater intensity stabilisation. Doppler cooling at typical operating power ≈ 30 mW near λ_D2; photoionisation by separate dye laser (Rhodamin 6G + 532 nm pump) + BBO ring cavity.

## Extraction Passes

- **2026-05-08 (assistant under steward direction, DRAFT).** Initial VECSEL+SHG-focused extraction of §3.3 + §3.4. Status `DRAFT` (not yet steward-signed-off).

## Review Notes

- **In-house origin point.** This is where the AG Schätz VECSEL story starts. The Burd2016 reference [46] in §3.3.1 frequency-stability discussion makes the lineage explicit: NIST + Tampere collaboration design → in-house Freiburg build with Vexlum gain mirrors. The 50(10) kHz linewidth quoted is from the NIST setup, not measured in Kiefer2020.
- **SHG topology = Friedenauer2006.** Reference [110] in §3.3.2 is Friedenauer 2006. The LBO bow-tie ring + BBO ring + Hänsch-Couillaud locking topology is the Friedenauer baseline ported onto the in-house VECSEL seed — operational evidence that the VECSEL seed-class direction and the LBO+BBO doubling-chain topology are independent choices that compose well.
- **Vendor-part stability across theses.** The same intracavity BRF (Newlight BIR0030), etalon (LightMachinery OP-3167-1000), gain-mirror vendor (Vexlum), pump diode (Ostech 40 W 808 nm), and wavemeter (HighFinesse WSU-30) reappear in [Guth2021](../Guth2021/), [Spanke2023](../Spanke2023/), and [Spanke2025](../Spanke2025/). What evolves is the thermal-management, cavity-length, and control-electronics layers — not the optical-element BOM.
- **Linewidth not measured here.** First in-house quantitative VECSEL linewidth measurement is in [Guth2021](../Guth2021/) (1.207(12) MHz iodine-locked at 100 ms; 1.635(13) MHz free-running). [Spanke2025](../Spanke2025/) reduces this to 101(8) kHz locked (with isolation box) — a five-fold improvement that brings the in-house system into Burd2023-class linewidth (< 100 kHz at 940 nm).
- **PPLN waveguide caveat.** §3.3.2 notes that the in-house PPLN waveguides do *not* show the wavelength-dependent efficiency rolloff at 4 λ_D1 ≈ 1121 nm that LBO does — but they cap at ≈ 500 mW visible. For the LBO + BBO baseline at the 25Mg+ D₂ operating point, this is irrelevant; for the D₁ operating point, it would matter.

## Downstream Dossier Links

- `KD-UV280-015` (VECSEL pump option). Kiefer2020 is added as an `[S]`-tier in-house operational reference alongside the `[P]`-tier Burd2016 + Burd2023 design-principles cluster. Kiefer2020 + Guth2021 + Spanke2023 + Spanke2025 together form the in-house chain that demonstrates the Burd2023 design principles transferred to the 1118 nm ²⁵Mg⁺ operating point.

## Cross-Reference to Steward Direction

This extraction lands as part of the same 2026-05-08 batch as [Spanke2023](../Spanke2023/), [Spanke2025](../Spanke2025/), and [Guth2021](../Guth2021/), all in service of the steward direction recorded in [`logbook/2026-05-08-vecsel-seed-lasers.md`](../../../logbook/2026-05-08-vecsel-seed-lasers.md). The components-page surface for the seed-laser layer lives at [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md).
