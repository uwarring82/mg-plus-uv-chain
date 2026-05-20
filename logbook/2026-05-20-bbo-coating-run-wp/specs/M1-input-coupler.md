# Coating spec — M1' input coupler

**Build:** Next-generation BBO ring cavity, 559 → 280 nm CW SHG
(AG Schätz, Universität Freiburg).
**Reference architecture:** Friedenauer et al., *Appl. Phys. B* 84, 371 (2006).
**Sheet status:** **FROZEN at BC-F closure (2026-05-20).** Ready to send as part of the [coating-run package](coating-run-cover-letter.md).
**Quote required by:** TBD (see cover letter §H).

---

## Geometry

| Field | Value |
|---|---|
| Role | Plane input coupler — long-arm side of bowtie ring |
| Geometry | **Plane**, Ø 12.7 × 6.35 mm |
| AOI | **~ 0° ± 1°** p-pol |
| Polarization | p-pol (TM) |
| Substrate | **Heraeus Herasil** (UV-grade fused silica) — ordinary UV-grade FS equivalent (e.g. Heraeus Suprasil 300) acceptable as a lead-time fallback; preference is Herasil |
| Surface quality (both surfaces) | scratch / dig ≤ 10 / 5 per MIL-PRF-13830B |
| Flatness | ≤ λ/10 P–V @ 633 nm over the clear aperture |
| Clear aperture | ≥ 8 mm (centred); coating + flatness valid over CA |
| Wedge / parallelism | ≤ 5 arcmin |

---

## Coating specification (primary)

**Front face — partial reflector @ 559 nm:**

| Spec | Value | Notes |
|---|---|---|
| Wavelength | 559 nm | Brewster-cut BBO Type-I 559 → 280 nm SHG ring; 559 nm = pump |
| **T (transmission, centre)** | **T = 19 965 ppm = 2.00 %** (equivalently R = 98.00 %) | Impedance-matched against the new-build cavity loss budget |
| **Tolerance** | **± 500 ppm absolute** (= ± 0.05 pp) | IBS-realistic; UV-output penalty < 0.05 % at the band edge |
| AOI / pol for spec | 0° p-pol | Plane mirror; ± 1° AOI band acceptable |

**Back face — anti-reflection @ 559 nm:**

| Spec | Value |
|---|---|
| AR target | R_AR ≤ 0.5 % @ 559 nm at AOI ~ 0° |

---

## Per-scenario informational rows (NOT a vendor-spec, FYI only)

The new-build cavity will operate at one of two 559 nm input scenarios
upstream of M1'. The single-variant centre above (19 965 ppm) is the
**equal-penalty** (minimax) centre across both scenarios — each pays
~ −0.68 % UV vs its respective impedance-matched optimum, with worst
case ~ −1 % across the ± 500 ppm vendor band. Per-scenario optima:

| Upstream scenario | P_in_559 | M1' T_IC optimum (informational) |
|---|---|---|
| Low (LBO at Friedenauer baseline) | 0.5 W | 17 565 ppm (1.756 %) |
| High (LBO at 1.5 × Friedenauer) | 1.5 W | 22 945 ppm (2.295 %) |

Vendors may quote against the 19 965 ± 500 ppm centre as the binding
spec; the per-scenario rows are provided for context only. See cover
letter §C for why a single coating variant is acceptable instead of
two scenario-matched variants.

---

## LIDT

| Spec | Value | Notes |
|---|---|---|
| **CW LIDT @ 559 nm** | **≥ 500 kW/cm² CW, 1/e² spot ≥ 100 μm**, surface (front face) | ~ 3 × margin over the worst-case 559 nm intracavity intensity at the 1.5 W operating scenario (~ 150 kW/cm² peak). G2-conditional service-life envelope detailed in cover letter §F |
| Back-face AR LIDT @ 559 nm | ≥ 50 kW/cm² CW (Gaussian) | Margin over the ~ 4 kW/cm² mode-matched input intensity |

LIDT comparison against published thresholds: see
[`bc-d-results.md`](../bc-d-results.md) §C.1 (Brown2019 screening
ratios) for the 559 nm material-class screening.

---

## Quantity

| Item | Count |
|---|---|
| **Pieces per role** | **N = 4** per role |
| Total deliverable on this page | 4 pieces of M1' |
| Yield | 4 full BBO-ring sets (one for the build + three forward-stock) |

This sheet specifies **one M1' variant** (§6 Q2 resolved at BC-B);
no per-scenario variant split is required.

---

## Notes for the coating house

- **Material class.** Per BC-D §C.1 (Brown2019 bandgap-screening):
  silica / alumina / hafnia / tantala are all admissible for the
  single-WL 559 nm HR / IC role; **niobia and titania are excluded**.
- **Vendor catalog R-spec.** Quote your standard catalog R ± δR for the
  closest match to T = 19 965 ppm at AOI 0° p-pol. If your nearest stock
  match falls outside the ± 500 ppm band, please quote a custom run.
- **No upper bound on R.** Achieved R higher than 98.00 % (T lower
  than 19 965 ppm) is acceptable — it shifts the cavity impedance-match
  point but is never a failure mode. Confirm the delivered R; we
  re-compute the operating point against it.
- **Cleanliness on delivery:** MIL-STD-1246C Class 100 or better,
  double-bagged in cleanroom-grade packaging (see cover letter §G).
- **Deposition method.** **IBS (ion-beam sputtering)** required.
