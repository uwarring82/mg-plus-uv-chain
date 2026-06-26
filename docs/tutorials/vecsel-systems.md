---
layout: default
title: Tutorial — VECSEL systems for 1118 nm and 1141 nm
description: How the in-house VECSEL seed lasers work — gain-mirror properties, the intracavity Lyot + etalon filtering hierarchy, and the parameter sensitivities that set the achievable linewidth. Covers the ~1120 nm Doppler-cooling/detection/Raman seed (→ 280 nm) and the ~1140 nm photoionisation seed (→ 285 nm). Pedagogical; architecture-neutral; pre-G1 admissible.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local pedagogical material — AG Schätz stewardship. This tutorial explains how the in-house VECSEL seed lasers work and which parameters limit their linewidth; it is not a build commitment, a vendor recommendation, or a Phase 4 scoring input. The source-class direction it teaches is recorded separately in the <a href="../components/seed-lasers.html">seed-lasers components page</a>.</p>

<p class="eyebrow">Tutorial · seed-laser systems</p>

# VECSEL systems — 1118 nm and 1141 nm

**Status:** TUTORIAL (pedagogical surface, 2026-06-26). Synthesises the in-house thesis lineage ([Kief20] · [Guth21] · [Span23] · [Span25]) and the NIST + Tampere design literature ([Burd16] · [Burd23]) into a single explanation of how the seed lasers work and what limits their linewidth.

**Charter compliance.** This page is a pedagogical tutorial over published in-house and external literature. It does **not** introduce architecture-family-specific simulation in `/src/` (anti-seeding clause, [principles §5.1](../principles.html)); it does **not** advance or close **G1**, **G2**, or **G3**; and it leaves the reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) unaffected. Every quantitative claim is provenance-linked to an extraction under [`data/literature/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/).

---

## What this tutorial covers

The project runs **two** VECSEL seed lasers, distinguished by the trapped-ion task they serve. Both are frequency-**quadrupled** (two cascaded second-harmonic stages) from the near-infrared seed to the deep ultraviolet:

| Seed (this tutorial) | × 4 → UV | ²⁵Mg⁺ task | Gain chip | In-house lineage | NIST/Tampere analogue |
|---|---|---|---|---|---|
| **~1118 nm** ("near 1120 nm") | **280 nm** (D lines) | Doppler cooling · detection · repump · stimulated Raman | GaInAs/GaAs | "VECSEL Nr.4" → "neXt VECSEL Nr.6" ([Kief20]→[Guth21]→[Span23]→[Span25]) | IC system, 1117 nm ([Burd16]) |
| **~1141 nm** ("near 1140 nm") | **285 nm** | Resonance-enhanced photoionisation (isotope-selective loading) | GaInAs/GaAs, **red-detuned** gain chip | second in-house VECSEL, under construction at [Guth21] §4 | VC system, 1141 nm ([Burd16]) |

The quadrupling map is exact arithmetic on the ²⁵Mg⁺ structure:

- **280 nm cooling/detection.** The 3s ²S₁/₂ → 3p ²P₃/₂ (D2) line sits at ≈ 279.6 nm, so the seed runs at **4 λ_D2 ≈ 1118.5 nm**; the 3p ²P₁/₂ (D1) line at ≈ 280.4 nm needs **4 λ_D1 ≈ 1121.4 nm**. A single gain chip emitting across **1116–1122 nm** ([Kief20], gain-bandwidth tuning) reaches both — this is why "near 1120 nm" is the right way to name it: one laser covers the whole 280 nm manifold.
- **285 nm photoionisation.** Neutral Mg has a 3s² ¹S₀ → 3s3p ¹P₁ resonance at ≈ 285.2 nm; the second VECSEL runs at **4 × 285.2 ≈ 1141 nm** to drive the first (resonant) step of a 1+1 resonance-enhanced multiphoton ionisation, the isotope-selective loading scheme of [[Kjae00]](../references.html#kjae00).

The rest of the tutorial is three sections, in the order the physics builds:

1. **[Gain properties](#1-gain-properties-the-semiconductor-gain-mirror)** — what the semiconductor gain mirror provides and how temperature moves it.
2. **[Intracavity filtering](#2-intracavity-filtering--single-frequency-selection)** — how a broadband gain medium is forced onto one longitudinal mode.
3. **[Parameter sensitivities → linewidth](#3-parameter-sensitivities--linewidth-limitations)** — which knobs convert into frequency noise, and the in-house record of closing them.

> **Prerequisite framing.** *Why* a VECSEL (the class-A argument, the source-class steward direction) is on the [seed-lasers components page](../components/seed-lasers.html); this tutorial assumes it and goes inside the device. *What happens after* the seed — the LBO + BBO doubling chain — is the [SHG numerics tutorial series](index.html).

---

## 1. Gain properties: the semiconductor gain mirror

<p class="classification classification--coastline">Coastline · the gain medium and its thermal behaviour are fixed, measurable device properties testable against [Kief20] §3.3.1 and [Burd16] §2.</p>

A VECSEL gain mirror is a single epitaxial semiconductor chip that is *both* the amplifier and one cavity end mirror. Reading it from the substrate outward:

- A monolithic **distributed Bragg reflector (DBR)** — many GaAs/AlGaAs quarter-wave pairs — forms the high-reflectivity cavity end.
- On top of the DBR, multiple **quantum wells** are placed at the **antinodes** of the intracavity optical standing wave. This *resonant periodic gain* (RPG) arrangement maximises the overlap between the carriers and the field. [Burd23]'s 940 nm chip uses 24 QWs; the in-house 1118 nm chip is a [Kief20] Vexlum flip-chip GaInAs/GaAs structure.
- A **CVD-diamond heat spreader** (3.0 × 3.0 × 0.3 mm, [Kief20]) is bonded to the chip to pull heat out laterally, and the stack sits on a Peltier-stabilised, water-cooled copper carrier.

The chip is **optically pumped** by a multimode fibre-coupled diode at ≈ 808 nm ([Kief20]: Ostech 40 W, 808 nm, volume-Bragg-grating-stabilised; [Burd16]: 807 nm, 21 W). The pump is absorbed in the barriers; carriers relax into the wells and provide gain at a wavelength set by the well composition and width.

### Three gain properties that matter downstream

**Broad gain bandwidth → tunability.** The quantum-well gain spectrum is tens of nanometres wide. For the 1118 nm chip the *useful* single-mode emission spans **1116–1122 nm** ([Kief20]), which is exactly what lets one device cover both ²⁵Mg⁺ D lines (4 λ_D2 ≈ 1118.5 nm and 4 λ_D1 ≈ 1121.4 nm). The 1141 nm photoionisation chip is the **same material system with a red-detuned well design** ([Guth21] §4) — a deliberate composition shift, not a different technology.

**Short carrier lifetime → class-A dynamics.** Semiconductor carrier lifetime (~ns) is far shorter than the cavity photon lifetime of the long external resonator. The laser is therefore *photon-lifetime-dominated* (class-A): **no relaxation-oscillation resonance** and a **structurally suppressed ASE pedestal**. This is the gain-*dynamics* property that makes the VECSEL spectrally clean — and it is the reason the seed's intrinsic (quantum-limited) linewidth is tiny, so that the *measured* linewidth is set by technical noise (Section 3), not by the gain itself. ([Burd23] §1–2; restated on the [components page](../components/seed-lasers.html).)

**Gain-peak temperature sensitivity → the load-bearing thermal constraint.** The quantum-well gain peak **red-shifts with temperature** at roughly **0.12–0.15 nm/K** (gain-chip temperature, [Kief20]). Two consequences:

- *It is a tuning knob.* Coarse wavelength setting is done by the gain-chip TEC set-point.
- *It is the dominant disturbance.* The chip's efficiency depends on the detuning between the gain peak and the chip's own micro-cavity (sub-cavity) resonance; both move with temperature, and any drift in pump-deposited heat moves the operating point. This is why the 1141 nm VC gain mirror is run **cold (8 °C)** in [Burd16], and why thermal management — diamond spreader, dual-stage cooling, low-drift TECs — is treated as a first-class design layer rather than an afterthought. It is also the entry point for most of the linewidth-limiting sensitivities in Section 3.

One more gain property bridges directly to linewidth: the **linewidth-enhancement (Henry α) factor**. In any semiconductor gain medium, carrier-density fluctuations modulate the refractive index as well as the gain, so **amplitude noise is partly converted into phase/frequency noise**, broadening the line by a factor (1 + α²). [Kief20] names the Henry factor as the high-frequency intensity-to-frequency-noise coupler. Keep it in mind: it is the mechanism by which *pump* and *thermal* amplitude disturbances become *frequency* noise.

```
  808 nm pump (multimode diode, VBG-stabilised)
        │
        ▼
  ┌───────────────────────────────────────────────┐
  │  GAIN MIRROR (= amplifier + cavity end mirror) │
  │  AR surface ─ QWs at standing-wave antinodes   │
  │             ─ monolithic GaAs/AlGaAs DBR       │
  │             ─ CVD-diamond heat spreader        │
  │             ─ Peltier + water-cooled Cu carrier│
  │   GaInAs/GaAs:  1118 nm  (red-detuned: 1141 nm)│
  └───────────────────────────────────────────────┘
        gain bandwidth ~ tens of nm  →  needs filtering (Section 2)
```

---

## 2. Intracavity filtering — single-frequency selection

<p class="classification classification--coastline">Coastline · the filter free spectral ranges and the cavity mode spacing are fixed by component geometry; testable against [Kief20] §3.3.1 part numbers and [Span25] re-measurements.</p>

The gain medium is broadband and the external cavity is long, so left alone the laser would run multi-mode. **Single-frequency operation is engineered by a nested hierarchy of filters**, each with a narrower free spectral range (FSR) and higher selectivity than the last. The rule is simple: the *combined* round-trip loss difference between the chosen mode and every competitor must exceed what the homogeneously-broadened gain can equalise.

The 1118 nm cavity is a **linear (I-shaped) resonator, L ≈ 128 mm** ([Kief20]), so its longitudinal-mode spacing is

> FSR_cavity = c / (2L) ≈ 3×10⁸ / (2 × 0.128) ≈ **1.17 GHz**.

The filter stack, from coarsest to finest:

| Stage | Element (in-house part) | Free spectral range / passband | Tuned by |
|---|---|---|---|
| Gain | GaInAs/GaAs quantum wells | tens of nm | gain-chip temperature (0.12–0.15 nm/K) |
| **Coarse** | **Birefringent (Lyot) filter / BRF** — Newlight BIR0030 quartz, at Brewster angle θ_B ≈ 57° | sub-nm passband (~100s of GHz) | filter rotation + temperature |
| **Medium** | **YAG etalon** — LightMachinery OP-3167-1000, 1.004 mm thick | **FSR ≈ 72 GHz at 1118 nm** (nominal 82.3 GHz at 1064 nm; re-measured 72 GHz in [Span25]) | etalon temperature |
| **Fine** | **Cavity length** — PZT-actuated output coupler (PI P-080.311 ring piezo) | selects one mode of the 1.17 GHz comb | PZT voltage (≈ 78 MHz/V, [Span23]) |

**How the birefringent (Lyot) filter works.** A birefringent plate between the Brewster-angled intracavity surfaces rotates the polarisation by a wavelength-dependent amount; only wavelengths that emerge with the original polarisation pass the Brewster surfaces without loss. Tilting/rotating the plate slides this transmission comb. The BRF is the *coarse* wavelength selector — it picks the sub-nanometre window (e.g. the D2 versus D1 region) and, because it works through the Brewster loss, it also fixes the cavity's linear polarisation. (Newlight BIR0030, mounted at θ_B ≈ 57° on a goniometer, temperature-stabilised; [Kief20].)

**How the etalon works.** The uncoated YAG étalon is a weak Fabry–Pérot whose 72 GHz transmission peaks sit *inside* the BRF passband. Temperature-tuning its optical thickness walks one étalon peak onto the desired cavity mode and suppresses the étalon's neighbours. It is the *medium* selector — between the BRF's ~100s-of-GHz window and the cavity's 1.17 GHz comb.

**How the cavity (PZT) works.** Even after BRF + étalon, several 1.17 GHz cavity modes can sit under the combined passband. Final selection is by **cavity length**: the PZT moves the output coupler so that exactly one longitudinal mode coincides with the filter maximum and wins the gain competition. The PZT also provides the *finest continuous tuning* — a mode-hop-free span of ~100 MHz at fixed BRF/étalon temperature ([Span23], 78 MHz/V).

Putting the ranges together gives the **mode-selection budget**:

> gain (tens of nm) ⊃ BRF (sub-nm) ⊃ étalon (72 GHz) ⊃ **single cavity mode** (1.17 GHz spacing).

Coordinated tuning of all three stages yields a **mode-hop-free range of several 100 GHz** ([Guth21] §3.1) — comfortably more than the few-GHz span needed to sit anywhere on the ²⁵Mg⁺ manifold, and far beyond the ~100 GHz of the legacy Yb-fibre laser it replaced.

> **Design cost of each element.** Every intracavity surface adds loss and risks a *spurious étalon* (an unwanted Fabry–Pérot between parallel faces) that would corrupt the mode selection. The standard mitigations appear throughout the literature: Brewster mounting (BRF), uncoated/temperature-controlled faces (YAG étalon), AR coatings, and — in the [Burd23] 1252 nm build — a 2° wedge between diamond facets. The filtering that buys single-frequency operation is therefore also a loss budget the cavity must afford, which feeds back into linewidth via the next section.

```
   GAIN MIRROR ──┐  linear cavity, L = 128 mm  ┌── OUTPUT COUPLER
                 │  FSR = c/2L ≈ 1.17 GHz       │  R = 97.5 % @ 1118 nm
   [ BRF / Lyot @ Brewster ]  coarse: sub-nm    │  RoC = 200 mm, on PZT
   [ YAG étalon, 1.004 mm  ]  medium: 72 GHz     │
   [ PZT cavity length     ]  fine: 1 mode, ~100 MHz mode-hop-free
                 └──────────────► single-frequency 1118 nm out → LBO → BBO → 280 nm
```

---

## 3. Parameter sensitivities → linewidth limitations

<p class="classification classification--coastline">Coastline · the linewidth budget criterion (Δν_seed ≪ min(Δν_atomic, Δν_lock)) is a Level-1 derived optical constraint; the binding term is the doubling-cavity lock bandwidth, not the atomic linewidth.</p>

This is the section the rest of the tutorial builds toward. The headline:

> **The VECSEL's intrinsic (Schawlow–Townes) linewidth is negligible; its measured linewidth is set entirely by technical perturbations of the cavity optical length.** Reducing the linewidth is therefore an exercise in finding and suppressing length-noise sources — which is exactly the story of the in-house thesis lineage.

### 3.1 Why the seed is technical-noise-limited

The fundamental (quantum) limit, the Schawlow–Townes linewidth, scales as Δν_ST ∝ (Δν_c)² / P_out and is broadened by the Henry factor to Δν_ST·(1 + α²). For a class-A VECSEL the cavity is long (so the cavity linewidth Δν_c is small), the circulating power is high, and the ASE pedestal is suppressed — together these push the intrinsic linewidth to the sub-kHz scale. **Every linewidth the project has actually measured (MHz down to ~100 kHz) is orders of magnitude above this floor**, so the floor is not the constraint. What *is* the constraint is technical frequency noise, and all technical frequency noise enters through one door:

> A cavity of optical length L resonates at ν = q·c/(2L). Hence **δν/ν = − δL/L**: *any* perturbation that changes the optical path length L shifts the frequency. Linewidth is the time-averaged spread of those shifts.

### 3.2 The sensitivity ledger

Each row is a physical parameter that modulates L (or, via the Henry factor, modulates amplitude that becomes frequency noise). They are ordered roughly by the timescale on which they dominate.

| Sensitivity | Mechanism (how it moves the frequency) | Evidence / in-house handling |
|---|---|---|
| **Mechanical / acoustic** (mount vibration, PZT-driver noise) | Direct δL of the 128 mm cavity; PZT gain 78 MHz/V means driver and acoustic noise couple straight to ν | Invar baseplate + ceramic-pedestal enclosure ([Kief20]); passive thermal-radiation, A4 footprint, noise-isolation box ([Span25]) |
| **Intracavity-element temperature** (gain chip, étalon, BRF) | Gain peak 0.12–0.15 nm/K; étalon/BRF passband centres drift → frequency *pulling* of the selected mode | TEC stability < 0.004 K/h ([Kief20] Arroyo) → **0.08 mK** TEC stability ([Span25] custom controller) |
| **Pump power / pump RIN** | Pump fluctuation → heat-load change on the gain chip → optical-path + gain-peak shift; residual amplitude noise → frequency noise via Henry α | VBG-stabilised pump suppresses fibre-multimode beating ([Kief20]); copper cooling sleeve on the pump-fibre output, −14 °C at 22.4 W ([Span23]) |
| **Cooling-water / chiller cycling** | The chiller's on/off thermal cycle modulates gain-chip temperature → large, periodic frequency swing | **The decisive in-house finding:** the legacy Neslab chiller drove ≈ **200 MHz peak-to-peak** oscillation; replacing it with an Alphacool PC-water loop removed it, a **factor-5** short-term improvement ([Span23]) |
| **Ambient temperature / humidity / air currents** | Slow drift of baseplate length and of the cavity air path's refractive index | Dry-N₂ purge of the enclosure ([Burd23] design parameter); temperature-isolation box ([Span25]) |
| **Absolute-frequency reference drift** (long τ) | The *lock* that holds ν, not the laser itself: wavemeter drift ~ 10 MHz/day; iodine lock bounded by the 125 kHz photodiode bandwidth | Doppler-free iodine saturation spectroscopy + HighFinesse wavemeter, calibrated daily ([Kief20] · [Guth21]) |

The single most instructive entry is the **chiller cycle**: a mundane piece of facility plumbing produced a 200 MHz frequency oscillation — three orders of magnitude larger than the target linewidth — purely by modulating gain-chip temperature. It is the cleanest illustration of "linewidth limitation = cavity-length (here, gain-temperature) sensitivity."

### 3.3 The in-house record: closing the sensitivities one by one

Each thesis in the lineage attacked the then-dominant sensitivity. Read the table as a sensitivity-reduction narrative, not just a scoreboard (Allan deviation at τ = 100 ms unless noted):

| Build | Linewidth @ τ = 100 ms | Dominant limitation addressed | Source |
|---|---|---|---|
| **[Kief20]** (origin, "Nr.4") | not measured directly (cited ~ 50 kHz from [Burd16]); passive drift < 50 MHz / hour | first build: established the platform, vendor parts, thermal architecture | [Kief20] §3.3.1 |
| **[Guth21]** | **1.635(13) MHz** free-run · **1.207(12) MHz** iodine-locked | *first quantitative in-house linewidth measurement* — set the baseline to beat | [Guth21] §3.2 |
| **[Span23]** | **~ 300–400 kHz** free-run (**factor-5**) | cooling-water chiller cycling + pump-fibre thermal load | [Span23] |
| **[Span25]** ("neXt", "Nr.6") | **101(8) kHz** locked (with isolation box) | residual mechanical + thermal drift; passive thermal radiation; custom 0.08 mK TEC | [Span25] |

[Span25] is the first in-house build to reach the **[Burd23] sub-100-kHz linewidth class** at the actual 1118 nm operating point — i.e. the design principles transferred end-to-end, in Freiburg, on a ²⁵Mg⁺-targeted laser.

### 3.4 What the linewidth has to beat (and why it is *not* the atomic linewidth)

A common mistake is to size the seed linewidth against the ²⁵Mg⁺ natural linewidth, Γ/2π ≈ **41.8 MHz**. That is the wrong target. The binding criterion is

> **Δν_seed ≪ min( Δν_atomic , Δν_cavity-lock-bandwidth )**,

and the smaller term is the **doubling-cavity locking bandwidth ≈ 18 kHz** (the loaded-piezo resonance of the LBO ring, [[Frie06]](../references.html#frie06)). The reason is that the seed is quadrupled inside two *resonant* SHG cavities: seed frequency noise faster than a cavity's lock bandwidth is converted into **amplitude** noise on the harmonic (frequency-to-amplitude conversion). The job of the seed linewidth is to keep that conversion small, not merely to resolve the atomic line. The project's operating budget follows from this:

| Budget point | Value | Status |
|---|---|---|
| Target | ≤ 100 kHz | met by [Span25] (101 kHz) |
| Friedenauer-parity floor | ≈ 200 kHz | exceeded since [Span23] |
| Stretch ceiling | 50 kHz ([Burd16] 1141 nm parity) | open |

So the 41.8 MHz atomic linewidth is met with enormous margin by *any* of the builds; the engineering effort documented in Section 3.3 is all about the ~18 kHz lock-bandwidth term and the frequency-to-amplitude conversion it governs. *(Budget values per the [seed-lasers components page](../components/seed-lasers.html) and the [2026-05-08 steward-direction logbook entry](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-vecsel-seed-lasers.md).)*

---

## 4. The two systems, side by side

<p class="classification classification--sail">Sail · the 1141 nm photoionisation system is documented from [Burd16] and the [Guth21] §4 build note; the in-house device is a build-in-progress and its as-built parameters are not yet pinned.</p>

| | **1118 nm — cooling / detection / Raman** | **1141 nm — photoionisation** |
|---|---|---|
| Seed wavelength | 4 λ_D2 ≈ 1118.5 nm · 4 λ_D1 ≈ 1121.4 nm | ≈ 1141 nm (4 × 285.2 nm) |
| Gain chip | GaInAs/GaAs, emission 1116–1122 nm | GaInAs/GaAs, **red-detuned** well design |
| UV output | **280 nm** | **285 nm** |
| Doubling route | LBO ring → 559 nm → BBO ring → 280 nm (Friedenauer topology, Hänsch–Couillaud locks) | [Burd16] VC: intracavity LBO → 571 nm → BBO → 285 nm |
| Atomic target | ²⁵Mg⁺ 3s→3p (D2/D1) | **neutral Mg** 3s² ¹S₀ → 3s3p ¹P₁ (285.2 nm) |
| Role | Doppler cooling, state detection, repump, stimulated-Raman gates | resonance-enhanced (1+1) two-photon photoionisation for **isotope-selective loading** ([[Kjae00]](../references.html#kjae00)) |
| Operating point (analogue) | [Guth21]: f = 268.001790(5) THz for ground-state cooling | [Burd16]: ~ 1 mW at 285 nm at the trap, 26 µm waist, single ²⁵Mg⁺ in ~ 10 s |
| In-house status | running (Nr.4); redesigned (Nr.6, [Span25]) | second VECSEL under construction at [Guth21] §4 |

The two lasers share the **entire architecture** — gain-mirror family, the BRF + étalon + PZT filter stack, the diamond-spreader thermal design, and the LBO + BBO quadrupling topology. They differ only in the gain-chip well composition (which sets ~1118 vs ~1141 nm) and the downstream UV wavelength (280 vs 285 nm). That commonality is the practical core of the source-class steward direction: building a second VECSEL for photoionisation reuses the first one's engineering wholesale.

---

## 5. Open questions

- **1118 nm gain-mirror respecification.** The closest demonstrated gain mirror is [Burd16]'s 1117 nm IC chip; a build-specific 1118 nm mirror is an MBE-growth procurement question, with the Tampere ORC group (Guina) the natural collaboration anchor. *(See the [seed-lasers components page](../components/seed-lasers.html) open questions.)*
- **RIN at the lock bandwidth.** The binding noise number for the linewidth budget is the relative-intensity-noise spectral density *at the ~18 kHz doubling-cavity lock bandwidth*. It is not published for the in-house build ([Kief20] · [Guth21] open items); the Henry-α conversion of this RIN into frequency noise is the un-measured link in Section 3.
- **1141 nm in-house photoionisation VECSEL.** Documented as under construction at [Guth21] §4 and modelled on the [Burd16] VC system; its as-built linewidth, output power, and 285 nm conversion are not yet in the extracted record. This tutorial will be updated when an extraction lands.
- **G2 independence.** None of the above closes **G2**: UV-induced degradation at the 280 nm / 285 nm BBO output is independent of the seed-laser source class.

---

## See also

- [Components — Seed lasers (VECSEL)](../components/seed-lasers.html) — the source-class steward direction and the *why-a-VECSEL* (class-A) argument this tutorial assumes.
- [SHG enhancement-cavity tutorials](index.html) — what happens to the seed downstream: the LBO + BBO doubling chain numerics.
- [References](../references.html) — the literature index ([Burd16] · [Burd23] · [Kief20] · [Guth21] · [Span23] · [Span25] · [Frie06] · [Kjae00]).
- [`data/literature/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/) — the canonical `extracted.yaml` artefacts every number on this page is drawn from.
- [Principles](../principles.html) — Coastline / Sail vocabulary; anti-seeding clause; the constraint hierarchy this tutorial sits inside.
