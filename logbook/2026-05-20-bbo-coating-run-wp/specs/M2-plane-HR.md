# Coating spec — M2' plane HR (piezo seat)

**Build:** Next-generation BBO ring cavity, 559 → 280 nm CW SHG
(AG Schätz, Universität Freiburg).
**Reference architecture:** Friedenauer et al., *Appl. Phys. B* 84, 371 (2006).
**Sheet status:** **FROZEN at BC-F closure (2026-05-20); substrate amended and RE-FROZEN at BC-G close (2026-05-21).** Ready to send as part of the [coating-run package](coating-run-cover-letter.md). BC-G changed the M2′ blank from the default Ø 12.7 × 6.35 mm to **Ø 6.35 × 2.0 mm** on servo-bandwidth grounds — see [`bc-g-results.md`](../bc-g-results.md).

---

## Geometry

| Field | Value |
|---|---|
| Role | Plane high-reflector, long-arm side, **piezo-mounted for Hänsch–Couillaud servo lock** |
| Geometry | **Plane**, **Ø 6.35 × 2.0 mm** (reduced-mass servo blank — *not* the Ø 12.7 × 6.35 mm of the other seats; see Notes + [`bc-g-results.md`](../bc-g-results.md)) |
| AOI | **~ 0° ± 1°** p-pol |
| Polarization | p-pol (TM) |
| Substrate | **Heraeus Herasil** (UV-grade FS) — ordinary UV-grade FS equivalent acceptable as lead-time fallback; preference is Herasil |
| Surface quality (both surfaces) | scratch / dig ≤ 10 / 5 per MIL-PRF-13830B |
| **Flatness** | **≤ λ/10 P–V @ 633 nm over the clear aperture** — **load-bearing**: this is the HC servo seat; flatness keeps the loaded-mount resonance reproducible across the run |
| Clear aperture | **≥ 4 mm** (centred); coating + flatness valid over CA. The cavity beam at this plane seat is only ~ 0.15–0.20 mm radius, so CA is set by handling, not clipping |
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
- **Piezo seat — reduced mass for servo bandwidth.** This optic is
  glued (no lead disk, no added mass) directly onto a **PI P-887.31**
  PICMA® stack (7 × 7 mm face) for the Hänsch–Couillaud servo. The
  Ø 6.35 × 2.0 mm blank (≈ 0.14 g) (i) fits the 7 × 7 mm actuator
  face without overhang and (ii) drops the moving mass ~ 13× below the
  default Ø 12.7 × 6.35 mm blank (≈ 1.77 g), raising the loaded mount
  resonance from ~ 31 kHz to ~ 43 kHz (rigid) and lifting the servo
  unity-gain bandwidth ~ 1.5× over the Friedenauer baseline. Going
  **smaller than Ø 6.35 mm on P-887.31 is not worthwhile** — the
  actuator's own effective mass (~ 1.6 g) saturates the resonance near
  45 kHz. Flatness ≤ λ/10 over CA (above) keeps the loaded-mount
  resonance reproducible across the build. Full derivation:
  [`bc-g-results.md`](../bc-g-results.md).
- **Alternative blank (Tier 2 — build-item, not coating-item).** If the
  build elects a shorter, stiffer **P-885.11-class** stack (5 × 5 mm
  face) for higher bandwidth (~ 2.5× Friedenauer, UGF ~ 10 kHz), spec
  the blank at **Ø 5.0 × 1.5 mm** instead (Ø 4.5–5.0 mm to keep centring
  margin on the 5 × 5 face). The actuator/mount swap is a procurement /
  build-KD decision; the vendor can quote either blank size on this run.
- **Deposition method.** **IBS (ion-beam sputtering)** required.
- **Cleanliness on delivery:** MIL-STD-1246C Class 100 or better
  (see cover letter §G).
