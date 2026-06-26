---
layout: default
title: Components — Seed lasers (VECSEL)
description: Seed-laser layer of mg-plus-uv-chain. Design principles per Burd 2023 (J. Opt. Soc. Am. B 40, 773); wavelength-adjacent ²⁵Mg⁺ demonstration per Burd 2016. Source-class direction recorded 2026-05-08.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page records a source-class direction (VECSEL seed lasers) and the literature-anchored design principles guiding it; it is not a build commitment, vendor recommendation, or Phase 4 scoring input.</p>

<p class="eyebrow">Components · seed-laser layer</p>

# Seed lasers — VECSEL source class

**Status:** STEWARD DIRECTION (2026-05-08). Literature artefact landed; components-page surface drafted; no architecture-specific code.

**Source-class direction:** for current and future builds of `mg-plus-uv-chain`, the seed laser is a **VECSEL** (vertical-external-cavity surface-emitting laser). Design principles per [Burd 2023](https://doi.org/10.1364/JOSAB.475467); wavelength-adjacent ²⁵Mg⁺ demonstration per [Burd 2016](https://doi.org/10.1364/OPTICA.3.001294). Steward direction recorded in [`logbook/2026-05-08-vecsel-seed-lasers.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-vecsel-seed-lasers.md).

**Scope of this page.** The seed-laser layer feeds the LBO + BBO doubling chain described in [Friedenauer 2006 components](friedenauer-baseline.html). This page covers the seed itself — the device that produces the 1118 nm fundamental — not the doubling chain downstream.

**Charter compliance.** This page is a Phase 1 components surface; it is not architecture-family-specific simulation and does not close G1, G2, or G3. The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is unaffected.

---

## What VECSEL means in this project

A **VECSEL** is a semiconductor disk laser with the gain medium implemented as quantum wells in a single epitaxial chip and the laser cavity closed by an external partially-reflecting mirror. The semiconductor chip carries an integrated distributed Bragg reflector on one side, so the cavity is *external* on the other side. Optically pumped by a multimode 808 nm diode, the active region emits at a wavelength set by the quantum-well composition. With intracavity wavelength-selecting elements (birefringent filter, etalon) and a piezo-tuned cavity length, the laser can run on a single longitudinal mode with sub-100 kHz linewidth.

Two acronyms appear interchangeably in the literature:

- **VECSEL** — *Vertical-External-Cavity Surface-Emitting Laser.*
- **OPSL** / **OPSDL** — *Optically Pumped Semiconductor (Disk) Laser.* Used in industry; same device class.

The relevant design context for `mg-plus-uv-chain` is the trapped-ion-laboratory implementation of the NIST + Tampere ORC collaboration described in Burd 2016 (²⁵Mg⁺ at 280 nm and 285 nm) and Burd 2023 (⁹Be⁺ at 235 nm and 313 nm).

---

## Design principles (Burd 2023 anchor)

The principles below are stated in Burd 2023 §1-§2 and transferred verbatim to `mg-plus-uv-chain`. Each is labelled *Coastline* (testable design constraint inherited from the paper) or *Sail* (adaptive guidance scaled to the local operating point).

### Class-A laser dynamics *Coastline*

A long external cavity (≈ 125 mm) and short semiconductor carrier lifetime put the VECSEL in the **photon-lifetime-dominated** regime. Consequences:

- No relaxation oscillation.
- Suppressed amplified-spontaneous-emission (ASE) pedestal — a structurally narrower spectrum than fibre or tapered-amplifier sources.
- Low intensity noise — the principal noise drivers are environmental (mechanical, thermal) rather than dynamical.

This is the load-bearing reason VECSELs are preferred to Yb-fibre seeds for the present application. Friedenauer 2006 §2 reported 1.2 W of ASE in front of the LBO cavity ([`Friedenauer2006::P_ASE`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)); a VECSEL seed eliminates this budget and the corresponding ASE-handling components.

### Single-frequency narrow linewidth *Coastline*

The seed-laser linewidth `Δν_seed` must satisfy:

`Δν_seed  <<  min( Δν_atomic , Δν_cavity_lock_bandwidth )`

so that frequency noise is not converted to amplitude noise by the resonant SHG cavities. Burd 2023 makes this criterion explicit (§1: *"considerably less than the linewidths of relevant atomic transitions and sufficiently narrow that frequency fluctuations will not be converted to significant amplitude fluctuations by subsequent resonant frequency-doubling stages"*) and meets it with intracavity birefringent-filter + 1 mm YAG-etalon mode selection plus a PZT-tuned cavity length.

For `mg-plus-uv-chain`:

| Anchor | Value | Source |
|---|---|---|
| Atomic Γ / 2π (²⁵Mg⁺ 3p) | ≈ 41.8 MHz | natural linewidth |
| LBO cavity locking bandwidth | ≈ 18 kHz | Friedenauer 2006, loaded piezo resonance ([`Friedenauer2006::LBO_M2_piezo_resonance_loaded`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)) |
| Friedenauer Yb-fibre seed | < 200 kHz | Friedenauer 2006, §2 |
| Burd 2023 940 nm VECSEL | < 100 kHz | Burd 2023, §2 |
| Burd 2016 1141 nm VECSEL | < 50 kHz (HC error signal) | Burd 2016, §2 |
| **Operating budget (this project)** | **target ≤ 100 kHz; Friedenauer parity floor ≈ 200 kHz; stretch ceiling 50 kHz** *Sail* | derived in [`logbook/2026-05-08-vecsel-seed-lasers.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-vecsel-seed-lasers.md) |

The *binding* term is the cavity-locking bandwidth, not the atomic linewidth. The cavity itself filters above its bandwidth, so seed linewidth above the loaded piezo resonance is acceptable provided the ratio `Δν_seed / Δν_cavity_lock_bandwidth` is bounded.

### Compact, integrated cavity *Sail*

Burd 2023 uses a linear (I-shape) external cavity ≈ 125 mm long with a 200 mm-RoC concave output coupler at ~ 2 % transmission. The 940 nm and 1252 nm builds share this geometry; only the gain mirror differs. For `mg-plus-uv-chain`, the cavity geometry is a downstream design choice; what is inherited is the principle that a **compact, semiconductor-bandwidth-defined cavity** with intracavity etalon + BRF + PZT is the canonical implementation, not a Ti:Sapphire-style large-footprint solid-state laser.

### Gain-mirror thermal management *Coastline*

Heat sinking is the dominant constraint that sets max output power and spectral cleanliness. Burd 2023 implements two distinct thermal architectures:

- **Flip-chip** (940 nm): semiconductor structure flipped onto a multi-crystal diamond heat spreader bonded to the DBR; substrate removed by lapping + wet etch; IBS AR coating on the exposed semiconductor surface; soldered to a TEC-stabilised water-cooled copper heatsink.
- **Top-emitting intra-cavity** (1252 nm): single-crystal diamond heat spreader liquid-capillary-bonded to the active region; 2° wedge between diamond facets to suppress spurious etalons; IBS AR on the diamond top face; copper heatsink with a central opening for the intracavity beam.

Both choices remain in scope as candidates for a 1118 nm `mg-plus-uv-chain` build. The Tampere ORC group (Guina) is the natural collaboration anchor for gain-mirror MBE growth at the 1118 nm wavelength.

### Environmental purge *Sail*

Dry-N₂ purge inside the VECSEL enclosure improves frequency stability and output power at moisture-sensitive wavelengths. Burd 2023 §2 documents this as a design parameter, not an afterthought. For `mg-plus-uv-chain`, the seed-laser enclosure should plan for dry-N₂ purge from the outset.

---

## Wavelength coverage and the 1118 nm operating point

Burd 2023 demonstrates VECSELs at **940 nm** (GaInAs/GaAs gain mirror) and **1252 nm** (GaInNAs/GaAs gain mirror with nitrogen-incorporation bandgap-bowing). Burd 2016, from the same NIST + Tampere collaboration, demonstrates VECSELs at **1117 nm** and **1141 nm**.

The mg-plus-uv-chain Friedenauer baseline runs at **1118 nm**. This sits inside the demonstrated GaInAs/GaAs envelope (Burd 2016, 1117 nm). The 1118 nm operating point is therefore *demonstrated-adjacent*, but a specific 1118 nm gain mirror would still need to be respecified for the build — this is a future collaboration question, not solved by Burd 2023 alone.

| Wavelength | Demonstrated by | Material system |
|---|---|---|
| 940 nm | Burd 2023 (system A) | GaInAs/GaAs, 24 QWs |
| 1117 nm | Burd 2016 (IC system) | GaInAs/GaAs |
| **1118 nm** | **target — demonstrated-adjacent at 1117 nm** | GaInAs/GaAs (extrapolation; build-specific) |
| 1141 nm | Burd 2016 (VC system) | GaInAs/GaAs |
| 1252 nm | Burd 2023 (system B) | GaInNAs/GaAs (nitrogen-extended) |

---

## What VECSEL replaces, what it preserves

VECSEL is the **seed-laser source class** decision. The choice is independent of:

- the **doubling-chain topology** (LBO + BBO per Friedenauer 2006 stays as the reference baseline; alternatives PPLN-MgO, PPKTP, single-pass UV with build-up only at 559 nm are out of scope for the current iteration of the [next-gen workplan](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-next-gen-500mW-workplan.md));
- the **cavity-locking scheme** (Hänsch-Couillaud per Friedenauer 2006 stays as the candidate; PDH used by Burd 2023 on the PPKTP first stage is a topology-dependent choice that does not transfer);
- the **architecture-comparison framework** (Phase 4 scoring axes 1-6 remain frozen; VECSEL is an input to those axes, not a re-opening of them).

What VECSEL replaces:

| Friedenauer 2006 (Yb-fibre baseline) | VECSEL direction (this page) |
|---|---|
| 2 W Yb-fibre laser at 1118 nm | Single-frequency VECSEL at 1118 nm (tbd build-specific gain mirror) |
| Linewidth < 200 kHz | Linewidth < 100 kHz (Burd 2023 940 nm parity) |
| 1.2 W ASE at 1060-1100 nm | Effectively no ASE pedestal (class-A regime) |
| Polarisation-drift failure mode (CHARTER §5.4.5) | Different failure-mode envelope: gain-mirror thermal management; intracavity-element stability |
| ASE-handling components in front of LBO cavity | Front-end conditioning chain shrinks (no ASE filter; isolator can be respecified for narrower bandwidth) |
| 1064 nm-design isolator at ~ 90 % T at 1118 nm | Custom 1118 nm isolator (build-specific; out of scope for this page) |

---

## Open questions

- **1118 nm gain-mirror specification.** Burd 2016 IC system at 1117 nm is the closest demonstrated point; the 1 nm offset is well within MBE growth tolerances but the specific gain mirror is a build-specific procurement question. Resolution depends on collaboration with Tampere ORC (Guina); not on this page.
- **Continuous-tuning range.** Burd 2023 reports "several GHz" mode-hop-free tuning by simultaneous etalon + PZT slide. The Friedenauer ²⁵Mg⁺ system uses an iodine reference (R(53)28-3 at 559.271 nm, [`Friedenauer2006::iodine_reference_transition`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)) — the seed laser must hand off to a stable absolute reference once the mode-hop-free range is exhausted. Same architecture as Burd 2023, which uses an iodine-locked fibre laser at 626 nm for the 313 nm system.
- **RIN spectrum.** Burd 2023 makes the class-A claim qualitatively but does not publish a RIN spectrum. [Burd 2016 §2](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burd2016/extracted.yaml) reports `< -75 dBc/Hz` above 10 kHz at 280 nm. Comparison to Friedenauer 2006's `< -130 dB/Hz` at 2-10 MHz is partial (different frequency bands). RIN at the doubling-stage cavity-locking bandwidth is the binding number; not yet measured for the candidate VECSEL build.
- **G2-blocking dependencies.** UV-induced degradation at the 280 nm BBO output is independent of the seed-laser source class and remains G2-blocked; a VECSEL seed does not close G2 even though it removes the upstream Yb-fibre polarisation-drift failure mode.

---

## See also

- [Tutorial — VECSEL systems (1118 nm and 1141 nm)](../tutorials/vecsel-systems.html) — how the seed lasers work: gain-mirror properties, the intracavity Lyot + étalon filtering hierarchy, and the parameter sensitivities that set the achievable linewidth.
- [`logbook/2026-05-08-vecsel-seed-lasers.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-08-vecsel-seed-lasers.md) — steward-direction logbook entry that this page surfaces.
- [`data/literature/Burd2023/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burd2023/) — `extracted.yaml` + `notes.md`, design-principles literature artefact (DRAFT).
- [`data/literature/Burd2016/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Burd2016/) — wavelength-adjacent ²⁵Mg⁺ companion paper.
- [Friedenauer 2006 components](friedenauer-baseline.html) — the Yb-fibre seed + LBO + BBO baseline this VECSEL direction sits upstream of.
- [Optical-components inventory](inventory.html) — on-shelf stock for the doubling chain (LBO + BBO mirrors, crystals, sub-assemblies).
- [Architectures → Next-generation 500 mW](../architectures/next-gen.html) — the doubling-chain workplan that takes any seed-laser source as a fixed input.
- [Principles](../principles.html) — Coastline / Sail vocabulary; anti-seeding clause; asymmetric erosion protection.
