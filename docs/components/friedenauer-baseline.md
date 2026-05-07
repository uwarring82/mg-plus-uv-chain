---
layout: default
title: Components — Friedenauer 2006 baseline
description: Optical components inventory mirroring the LBO and BBO doubling stages of Friedenauer et al., Appl. Phys. B 84, 371 (2006). Phase 1 literature artefact with paper-stated provenance per row.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page reproduces optical-component data from a published source as a navigational/working inventory; it is not an endorsement, re-derivation, or vendor recommendation.</p>

<p class="eyebrow">Components inventory</p>

# Friedenauer 2006 — Optical Components List (LBO and BBO Doubling Stages)

**Status:** Phase 1 literature artefact, DRAFT (2026-05-07).
**Scope:** Reproduces the two SHG ring-cavity stages of the all-solid-state CW chain
1118 nm → 559 nm (LBO) → near-280 nm (BBO) as described in
[`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)
and [`notes.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/notes.md).
**Provenance contract:** every row cites either a paper-stated value
(`P` = direct quotation, `T` = paper-stated transitive equivalence) or marks the
field as `OPEN` when the paper does not specify it. No vendor catalog matching
is attempted at this stage; downstream procurement work belongs in
[KD-2026-XXX-uv-280nm](../KD-2026-XXX-uv-280nm.html) and is out of
scope under the Phase 1 anti-seeding clause
([Principles](../principles.html)).
**Conventions:** SI throughout; reflectivities/transmissions in fractional
units (1 = 100 %); concave radius of curvature R taken as 2 f under the
normal-incidence convention (paper reports focal length, not R).
**Future expansion (planned).** This inventory will grow with: photographs and
sketches per item (added under `docs/assets/components/friedenauer-baseline/`),
inline links to function-principle references, and vendor / SKU links once
KD-UV280-005/-007 procurement work is unblocked. Each addition must preserve
the per-row provenance tier — vendor links sit alongside, not in place of,
paper-stated specifications.

**See also.** [Optical-components inventory](inventory.html) — actual on-shelf
stock (mirrors, output couplers, sub-assemblies, BBO crystals from Raicol /
A-Star / Castech) keyed to the LBO and BBO roles described below, with a
glossary of cavity / nonlinear-optics terminology and a per-item verification
trail (Qty checked / Initials / Date).

---

## A. Pump conditioning at 1118 nm (pre-LBO)

| Item | Function | Paper-stated specification | Location | Source |
|---|---|---|---|---|
| A1 | Yb-doped fibre laser | λ = 1.118 μm, P ≈ 2.0 W, linewidth < 200 kHz, piezo scan range 80 GHz at 20 kHz bandwidth | Abstract; §2 | P |
| A2 | ASE handling | Suppression of broadband ASE peaked between 1060 nm and 1100 nm (~1.2 W); paper does not name a specific filter component | §2 | OPEN — paper reports the ASE budget but not the conditioning element |
| A3 | Optical isolator @ 1118 nm | T ≈ 0.90, isolation ≈ 30 dB; isolator designed for 1064 nm and used off-design at 1118 nm | §2 | P |
| A4 | Mode-matching optics into LBO cavity | Matches the BK-derived intracavity waist `w0_LBO_BK_optimum` = 27.3 μm at the LBO crystal centre | §3 (implied; component count not enumerated) | OPEN |
| A5 | LBO incoupling power point | P_LBO_in = 1.80 W after A2 and A3 | §2; Table 1 | P |

---

## B. LBO ring cavity (1118 nm → 559 nm)

Total cavity length L_cav = 0.400 m, FSR = 750 MHz, full folding angle 10° at the
focusing-mirror waist.

### B.1 Cavity mirrors

| ID | Geometry | Coatings (paper-stated) | Reflectivity / transmission | Source |
|---|---|---|---|---|
| M1 (input coupler) | Plane | AR on outside of cavity | R = 0.975 @ 1118 nm | P (§3; Table 1) |
| M2 (HR, mounted on piezo) | Plane | HR @ 1118 nm | R > 0.9998 @ 1118 nm | P (§3; Table 1) |
| M3 (focusing HR) | Concave, f = 25 mm (R = 50 mm) | HR @ 1118 nm | R > 0.9998 @ 1118 nm | P focal length (§3); R derived under normal-incidence convention |
| M4 (focusing output coupler, "zero-lens" shape) | Concave, f = 25 mm (R = 50 mm); AR on convex side @ 559 nm | HR @ 1118 nm; HT @ 559 nm | R > 0.999 @ 1118 nm; T > 0.95 @ 559 nm | P (§3; Table 1) |

Focusing-mirror geometric separation d = 62 mm, tuned onto the plateau of the
cavity stability region so that the realised intracavity waist matches the
Boyd–Kleinman optimum (§3; cross-referenced under
`LBO_BK_waist_realisation` in [`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)).

### B.2 Piezo and mount

| Item | Function | Paper-stated specification | Source |
|---|---|---|---|
| B2.1 | Stacked piezo on M2 | Thorlabs AE020304D04 stacked piezo glued to a lead disk; lead disk lowers loaded mount resonance and damps vibration | P (§3) |
| B2.2 | M2 mount loaded resonance | ≈ 18 kHz; bounds the achievable Hänsch–Couillaud servo bandwidth | P (§3) |

### B.3 LBO crystal

| Field | Value | Source |
|---|---|---|
| Material / cut | Type-I α-cut LBO, noncritical phase matching, θ = 90°, φ = 0° | P (§3) |
| Length | 18 mm (paper notes this is the *optimised* length under the cavity loss budget, not a vendor stock dimension) | P (§3) |
| Cross-section | Not specified by the paper | OPEN |
| Coatings | AR @ both fundamental (1118 nm) and harmonic (559 nm) | P (§3) |
| Effective nonlinearity | d_eff = 0.84 pm/V at 1118 nm (paper attributes to SNLO) | P (§3) |
| NCPM temperature (calc.) | 89 °C | P (§3) |
| NCPM temperature (observed optimum) | 94 °C; authors attribute the shift to imperfect oven–crystal heat contact | P (§3) |
| Vendor | Not specified by the paper for this crystal | OPEN |

### B.4 LBO crystal oven

| Item | Specification | Source |
|---|---|---|
| Set-point | ~94 °C operating optimum | P (§3) |
| Stability | ±0.020 K | P (§3) |
| Mechanical / vendor | Not specified by paper | OPEN |

### B.5 LBO Hänsch–Couillaud locking optics

| Item | Function | Paper-stated specification | Source |
|---|---|---|---|
| B5.1 | Polarization analyser path | Hänsch–Couillaud polarization scheme for cavity-length lock (Hänsch & Couillaud, Opt. Commun. 35, 441 (1980), reference [6]) | P (§3) |
| B5.2 | Piezo servo loop | Drives M2 piezo (B2.1) within the ~18 kHz mount-resonance ceiling | P (§3) |
| B5.3 | Quarter-wave plate / PBS / balanced photodetectors | Standard HC polarization optics — paper does not enumerate the individual elements | OPEN |

### B.6 Stage output

| Field | Value | Source |
|---|---|---|
| Stable 559 nm output | 0.95 W (Abstract also quotes ~1 W rounded) | P (§3; Abstract; Table 1) |
| LBO doubling efficiency | η_LBO > 0.527 (relative to power available in front of the cavity, not corrected for coupling, Fresnel, or output-coupler losses) | P (§3; Table 1) |

### B.7 559 nm pickoff for iodine reference

| Item | Function | Paper-stated specification | Source |
|---|---|---|---|
| B7.1 | Pickoff to iodine spectroscopy | ~10 mW split off at 559 nm | P (§2; Fig. 1) |
| B7.2 | Iodine vapour cell + polarization spectroscopy | Locks the 1118 nm laser to the I₂ R(53)28-3 hyperfine transition at 559.271 nm; provides the absolute frequency anchor that both ring cavities are then slaved to via Hänsch–Couillaud | P (§2) |

---

## C. Mode-matching from LBO output to BBO cavity

| Item | Function | Paper-stated specification | Source |
|---|---|---|---|
| C1 | 559 nm collimation / relay | Couples the 559 nm output of the LBO stage into the BBO ring cavity at P_BBO_in = 0.95 W | P (Table 1) |
| C2 | Mode-matching telescope | Matches the BK-derived BBO intracavity waist `w0_BBO_BK_optimum` = 19.4 μm | P (§3) (waist value); telescope element count not enumerated → OPEN |

---

## D. BBO ring cavity (559 nm → near 280 nm)

Total cavity length L_cav = 0.470 m, full folding angle 27.4° (chosen to
compensate astigmatism induced by the Brewster-cut BBO crystal). The paper
states explicitly that the BBO cavity layout is identical to the LBO cavity
*except* in mirror reflectivities and folding angle, so the focusing-mirror
focal length is inherited as a paper-stated transitive equivalence.

### D.1 Cavity mirrors

| ID | Geometry | Coatings (paper-stated) | Reflectivity / transmission | Source |
|---|---|---|---|---|
| M1' (input coupler) | Plane | AR on outside | R = 0.984 @ 559 nm | P (Table 1) |
| M2' (HR, on piezo) | Plane | HR @ 559 nm | R > 0.9993 @ 559 nm | P (§3; Table 1) |
| M3' (focusing HR) | Concave, f = 25 mm (R = 50 mm) | HR @ 559 nm | R > 0.9993 @ 559 nm | T (paper-stated equivalence to LBO M3 focal length) |
| M4' (focusing output coupler) | Concave, f = 25 mm (R = 50 mm); HT on outside @ 280 nm | HR @ 559 nm; HT @ 280 nm | R > 0.998 @ 559 nm; T > 0.94 @ 280 nm | P reflectivities / transmissions (§3; Table 1); T focal length |

Focusing-mirror geometric separation d' = 59.4 mm (Table 1).

### D.2 Piezo and mount

| Item | Function | Paper-stated specification | Source |
|---|---|---|---|
| D2.1 | Piezo on M2' for HC lock of the BBO ring cavity | Paper does not separately specify the BBO-stage piezo model; uses the same Hänsch–Couillaud locking scheme as the LBO stage | P locking scheme (§3); piezo model OPEN |

### D.3 BBO crystal

| Field | Value | Source |
|---|---|---|
| Material / cut | Brewster-cut BBO | P (§3) |
| Dimensions | 4 mm × 4 mm × 10 mm (transverse × transverse × length) | P (§3) |
| Phase-matching | Type I, 559 nm → 280 nm; cut angle not given | OPEN — flagged in [`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) `open_extraction_items` |
| Coatings | Brewster faces; explicit coating type / vendor not given | OPEN |
| Effective nonlinearity at 559 nm | Not given by Friedenauer 2006 | OPEN — must come from KD-UV280-005 / SNLO |
| Walk-off angle ρ at the Type-I PM angle | Not given by Friedenauer 2006 | OPEN — must come from KD-UV280-005 / Sellmeier |
| Manufacturer (relevant for unlockable-domain history) | Crystals of Siberia (paper-stated for the crystals tested under §4 unlockable-domain observation) | P (§4) |

### D.4 BBO crystal oven

| Item | Specification | Source |
|---|---|---|
| Set-point | ~50 °C; chosen to prevent water condensation on polished hygroscopic BBO surfaces | P (§3) |
| Stability | Not numerically specified for the BBO oven (paper only states a value for LBO) | OPEN |
| Mechanical / vendor | Not specified | OPEN |

### D.5 BBO Hänsch–Couillaud locking optics

| Item | Function | Source |
|---|---|---|
| D5.1 | HC polarization-analyser path on the BBO ring | P (§3): same locking scheme as LBO |
| D5.2 | Piezo servo loop on M2' | P (§3) (scheme); piezo model OPEN (D2.1) |

### D.6 Stage output

| Field | Value | Source |
|---|---|---|
| UV output near 280 nm | 0.275 W after projection / collimation | P (Abstract; §3; Table 1; §6) |
| BBO doubling efficiency | η_BBO = 0.289 | P (Table 1) |
| TEM₀₀ projection fraction | ≈ 0.95 (astigmatic output projected onto a Gaussian TEM₀₀ mode) | P (§3) |
| Overall 1118 → near-280 nm efficiency | 0.152 | P (§6) |

---

## E. Behavioural / environmental constraints (relevant to mount and enclosure choices)

These are not optical components but they constrain the optomechanical design
that hosts the components above; recorded here so the BOM is read together
with them.

| Field | Value | Source |
|---|---|---|
| UV power fluctuation | within ±2 % of mean | P (§5) |
| UV regular μs-scale drops | < 4 % | P (§5) |
| UV large drops | > 7 %, less than once per minute | P (§5) |
| UV environmental temperature sensitivity (unisolated) | ~10 % output oscillation per 2 K ambient swing | P (§5) |
| UV environmental temperature sensitivity (thermally isolated) | ~5 % residual | P (§5) |
| Polarization drift settling time (non-PM fibre on Yb amplifier) | ~7200 s if fibre fixed | P (§2) |
| Proposed polarization-drift mitigation | Active heat-sink temperature stabilization with a Peltier element | P (§5) |
| 14-GHz unlockable domain | 1118.339 nm – 1118.409 nm (BBO cavity cannot lock); reproduced across several lasers, cavities, and crystals (all crystals: Crystals of Siberia) | P (§4) — see `unlockable_domain_width_consistency` cross-check note in [`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) |

---

## F. Open items inherited from the extraction

These are propagated from the `open_extraction_items` list in
[`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml); a procurement-grade BOM cannot close
without them and they belong to KD-UV280-005 / -007 Section C, not to this
literature artefact:

- Exact BBO cut angle and coating vendor.
- Direct CW LIDT value at 280 nm.
- Source-side RIN and phase-noise spectra.
- Ion-side loss budget.
- BBO d_eff at 559 nm (Type I).
- BBO walk-off angle ρ at the 559 → 280 nm Type-I phase-matching angle.
- Refractive indices n_LBO(1118), n_BBO_o(559) (Sellmeier).

---

## G. What this list is NOT

- It is **not** a vendor BOM. No catalog SKUs, no prices, no lead times.
- It is **not** a re-optimisation of the Friedenauer architecture. The 18 mm
  LBO length, the 62 mm focusing-mirror separation, and the 27.3 μm waist are
  reproduced as-reported; under the Phase 1 anti-seeding clause this artefact
  must not perform Boyd–Kleinman re-optimisation
  ([Principles](../principles.html), §5.1).
- It is **not** an architecture-family-specific simulation input for `/src/`.
  Architecture-specific simulation remains gated by G1
  ([Status](../status.html)).
- It is **not** independent evidence; every row inherits the source-tier P
  ranking of [`extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml)
  and the `OPEN` rows mark precisely the gaps that the paper alone cannot close.
