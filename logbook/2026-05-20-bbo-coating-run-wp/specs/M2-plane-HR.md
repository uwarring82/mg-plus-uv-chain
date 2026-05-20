# Coating spec — M2' plane HR (piezo seat)

**Build:** Next-generation BBO ring cavity, 559 → 280 nm CW SHG
(AG Schätz, Universität Freiburg).
**Reference architecture:** Friedenauer et al., *Appl. Phys. B* 84, 371 (2006).
**Sheet status:** DRAFT (2026-05-20) — pending steward sign-off at BC-F closure.

---

## Geometry

| Field | Value |
|---|---|
| Role | Plane high-reflector, long-arm side, **piezo-mounted for Hänsch–Couillaud servo lock** |
| Geometry | **Plane**, Ø 12.7 × 6.35 mm |
| AOI | **~ 0° ± 1°** p-pol |
| Polarization | p-pol (TM) |
| Substrate | **Heraeus Herasil** (UV-grade FS) — ordinary UV-grade FS equivalent acceptable as lead-time fallback; preference is Herasil |
| Surface quality (both surfaces) | scratch / dig ≤ 10 / 5 per MIL-PRF-13830B |
| **Flatness** | **≤ λ/10 P–V @ 633 nm over the clear aperture** — **load-bearing**: this is the HC servo seat; flatness keeps the loaded-mount resonance reproducible across the run |
| Clear aperture | ≥ 8 mm (centred); coating + flatness valid over CA |
| Wedge / parallelism | ≤ 5 arcmin |

---

## Coating specification

**Front face — high reflector @ 559 nm:**

| Spec | Value | Notes |
|---|---|---|
| Wavelength | 559 nm | Cavity fundamental |
| **R (front face, minimum)** | **R ≥ 99.970 %** (equivalently T ≤ 300 ppm) | Single-WL HR at near-normal incidence; allocation 300 ppm from the 1 500 ppm summed mirror-loss budget |
| Tolerance | — (R is a *minimum*; vendor-delivered higher R is welcome and never a failure mode) | |
| AOI / pol for spec | 0° p-pol | Plane mirror; ± 1° AOI band acceptable |

**Back face — anti-reflection @ 559 nm:**

| Spec | Value |
|---|---|
| AR target | R_AR ≤ 0.5 % @ 559 nm at AOI ~ 0° |

---

## LIDT

| Spec | Value | Notes |
|---|---|---|
| **CW LIDT @ 559 nm** | **≥ 500 kW/cm² CW, 1/e² spot ≥ 100 μm**, surface (front face) | ~ 3 × margin over the worst-case 559 nm intracavity intensity at the 1.5 W operating scenario (~ 150–190 kW/cm² peak on the plane mirrors). G2-conditional service-life envelope detailed in cover letter §F |

---

## Quantity

| Item | Count |
|---|---|
| **Pieces per role** | **N = 4** |
| Total deliverable on this page | 4 pieces of M2' |
| Yield | 4 full BBO-ring sets (one for the build + three forward-stock) |

---

## Notes for the coating house

- **Material class.** Per BC-D §C.1: silica / alumina / hafnia /
  tantala admissible; **niobia and titania excluded**. **No silica
  cap layer required** (Brown2019: thin caps give zero LIDT
  improvement under particulate contamination).
- **Piezo seat — flatness.** This optic is glued onto a stacked
  piezo (Thorlabs AE020304D04-class or equivalent) for the
  Hänsch–Couillaud servo. The loaded-mount resonance frequency
  needs to be reproducible across the build, which requires the
  flatness spec above to be maintained over the full CA.
- **Deposition method.** **IBS (ion-beam sputtering)** required.
- **Cleanliness on delivery:** MIL-STD-1246C Class 100 or better
  (see cover letter §G).
