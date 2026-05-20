# Coating spec — M3' curved HR (focusing mirror)

**Build:** Next-generation BBO ring cavity, 559 → 280 nm CW SHG
(AG Schätz, Universität Freiburg).
**Reference architecture:** Friedenauer et al., *Appl. Phys. B* 84, 371 (2006).
**Sheet status:** **FROZEN at BC-F closure (2026-05-20).** Ready to send as part of the [coating-run package](coating-run-cover-letter.md).

---

## Geometry

| Field | Value |
|---|---|
| Role | Concave focusing high-reflector, short-arm side, at the BBO waist |
| Geometry | **Concave, radius of curvature ROC = 50 mm** (= 2 f for f = 25 mm) |
| ROC tolerance | ± vendor-standard (typically ≤ 1 % on R); please confirm in quote |
| Substrate diameter | Ø 12.7 × 6.35 mm |
| **AOI** | **13.7° ± 1.5° p-pol** (chosen procurement band — see cover letter §A) |
| Polarization | p-pol (TM) |
| Substrate | **Heraeus Herasil** (UV-grade FS) — ordinary UV-grade FS equivalent acceptable as lead-time fallback; preference is Herasil |
| Surface quality (both surfaces) | scratch / dig ≤ 10 / 5 per MIL-PRF-13830B |
| **Surface figure (concave face)** | **≤ λ/10 P–V @ 633 nm over the clear aperture** — irregularity over the full CA matters at the focus; centre-only figure is *not* sufficient |
| Clear aperture | ≥ 8 mm (centred); coating + figure valid over CA |
| Centring (decentre of optical axis vs mechanical) | ≤ 5 arcmin |

---

## Coating specification

**Front face (concave) — high reflector @ 559 nm:**

| Spec | Value | Notes |
|---|---|---|
| Wavelength | 559 nm | Cavity fundamental |
| **R (front face, minimum)** | **R ≥ 99.970 %** (T ≤ 300 ppm) **over the full AOI band 12.2°–15.2° p-pol** | Single-WL HR at oblique incidence; allocation 300 ppm from the 1 500 ppm summed mirror-loss budget. Coating must hold spec across the chosen AOI band, not only at 13.7° |
| Tolerance | — (R is a *minimum*; higher R welcome) | |
| AOI / pol for spec | 13.7° ± 1.5° p-pol | Specified *over the band*, not only at the nominal |

**Back face (convex side) — anti-reflection @ 559 nm:**

| Spec | Value |
|---|---|
| AR target | R_AR ≤ 0.5 % @ 559 nm at AOI 13.7° p-pol |

---

## LIDT

| Spec | Value | Notes |
|---|---|---|
| **CW LIDT @ 559 nm** | **≥ 250 kW/cm² CW, 1/e² spot ≥ 100 μm**, surface (front face) | ~ 4 × margin over the worst-case 559 nm intracavity intensity at the curved-mirror seat (1.5 W scenario: ~ 65 kW/cm² peak). G2-conditional service-life envelope detailed in cover letter §F |

---

## Quantity

| Item | Count |
|---|---|
| **Pieces per role** | **N = 4** |
| Total deliverable on this page | 4 pieces of M3' |
| Yield | 4 full BBO-ring sets (one for the build + three forward-stock) |

---

## Notes for the coating house

- **Material class.** Per BC-D §C.1: silica / alumina / hafnia /
  tantala admissible at single-WL 559 nm HR; **niobia and titania
  excluded**. **No silica cap layer** required.
- **AOI band — critical detail.** The ± 1.5° band on the spec is a
  *chosen procurement band*, *informed by* a photogrammetric survey
  of fielded BBO doublers in our lab (see cover letter §A for the
  full provenance). **It is not a bench-measured build-variation
  result.** A coating that meets R ≥ 99.97 % only at 13.7° but
  drops to e.g. 99.93 % at 15.2° **fails this spec**.
- **Deposition method.** **IBS (ion-beam sputtering)** required.
- **Cleanliness on delivery:** MIL-STD-1246C Class 100 or better
  (see cover letter §G).
