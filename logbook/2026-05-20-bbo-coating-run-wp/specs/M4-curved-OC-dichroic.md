# Coating spec — M4' curved output coupler (dichroic)

**Build:** Next-generation BBO ring cavity, 559 → 280 nm CW SHG
(AG Schätz, Universität Freiburg).
**Reference architecture:** Friedenauer et al., *Appl. Phys. B* 84, 371 (2006).
**Sheet status:** **FROZEN at BC-F closure (2026-05-20).** Ready to send as part of the [coating-run package](coating-run-cover-letter.md).
**Differentiated element:** dual-wavelength dichroic stack — please
read the cover letter §B (material recommendation) and §F
(G2-conditional service-life clauses) before quoting.

---

## Geometry

| Field | Value |
|---|---|
| Role | Concave dichroic output coupler — high-reflects the cavity 559 nm fundamental on the front face and transmits the 280 nm second harmonic through the substrate; back face AR @ 280 nm |
| Geometry | **Concave, radius of curvature ROC = 50 mm** (= 2 f for f = 25 mm) |
| ROC tolerance | ± vendor-standard (typically ≤ 1 % on R); please confirm in quote |
| Substrate diameter | Ø 12.7 × 6.35 mm |
| **AOI** | **13.7° ± 1.5° p-pol** (chosen procurement band — see cover letter §A) |
| Polarization | p-pol (TM) |
| **Substrate** | **Heraeus Herasil** (UV-grade fused silica) — **mandatory** on this element because 280 nm transits the substrate to exit the cavity. Ordinary FS is *not* acceptable on M4' |
| Surface quality (both surfaces) | scratch / dig ≤ 10 / 5 per MIL-PRF-13830B |
| Surface figure (concave front, planar back) | ≤ λ/10 P–V @ 633 nm over the clear aperture (both surfaces) |
| Clear aperture | ≥ 8 mm (centred); coatings + figure valid over CA |
| Centring (decentre of optical axis vs mechanical) | ≤ 5 arcmin |

---

## Coating specification

### Front face (concave) — dichroic: HR @ 559 nm + HT @ 280 nm in the same stack

| Spec | Value | Notes |
|---|---|---|
| Wavelength 1 | 559 nm | Cavity fundamental (intracavity reflection) |
| Wavelength 2 | 280 nm | Second harmonic (transmitted out) |
| **R @ 559 nm (front face, minimum)** | **R ≥ 99.910 %** (T ≤ 900 ppm) **over the full AOI band 12.2°–15.2° p-pol** | Dichroic stack allocation: 900 ppm from the 1 500 ppm summed mirror-loss budget (3:1 Friedenauer-class dichroic-vs-HR ratio); coating must hold spec across the band |
| **T @ 280 nm (front face, minimum)** | **T ≥ 95.0 %** **over the full AOI band 12.2°–15.2° p-pol** | Tighter than Friedenauer's published floor (T > 94 %); modern dichroics typically deliver T ≥ 97 % — vendor encouraged to quote actual achievable T |
| AOI / pol for spec | 13.7° ± 1.5° p-pol | Specified *over the band*, not only at the nominal |

### Back face (planar) — AR @ 280 nm

| Spec | Value | Notes |
|---|---|---|
| AR target | R_AR ≤ 0.5 % @ 280 nm at AOI 13.7° p-pol | Narrow-band centred at 280 nm; bandwidth ~ 5 nm typical IBS catalog |
| AR bandwidth | Narrow-band centred at 280 nm | The CW chain is locked at Δ_ref = 40 GHz (~ 0.01 nm at 280 nm); broadband 250–300 nm AR is *not* required (cover letter §D) |
| Broadband AR upgrade option | (Optional) 250–300 nm broadband AR available at incremental cost; please quote as alternative line item if vendor offers |

---

## LIDT — specified per surface

| Surface | Spec | Notes |
|---|---|---|
| **Front face — dual-WL dichroic** | **CW LIDT ≥ 250 kW/cm² @ 559 nm** AND **≥ 5 kW/cm² @ 280 nm**, simultaneously, 1/e² spot ≥ 100 μm, surface | Binding LIDT case of the build. Front face carries the intracavity 559 nm load + the transmitted 280 nm load in the same dichroic coating layers. The requested LIDT values sit **~ 4 × above the worst-case 559 nm operating peak** (~ 65 kW/cm²) and **~ 8 × above the worst-case 280 nm transit peak** (~ 0.6 kW/cm²); these are *vendor-acceptance margins on the requested LIDT spec*, **not** literature-supported service-life margins. The literature-supported service-life envelope is **G2-conditional** and discussed separately in cover letter §F — on the 280 nm axis, our operating fluence sits ~ 1.15 × *above* the nearest CW UV operational benchmark (Kondo / Kubota 1 000-hour 266 nm point), so service-life expectation is *order-of-magnitude match*, not margin |
| **Back face — planar AR @ 280** | **CW LIDT ≥ 5 kW/cm² @ 280 nm**, surface | Vendor-acceptance margin ~ 8 × over the ~ 0.6 kW/cm² outgoing 280 nm peak. Service-life expectation as above |

---

## Quantity

| Item | Count |
|---|---|
| **Pieces per role** | **N = 4** |
| Total deliverable on this page | 4 pieces of M4' |
| Yield | 4 full BBO-ring sets (one for the build + three forward-stock) |

---

## Material recommendation (please read in conjunction with cover letter §B)

The M4' dichroic stack is the most-differentiated coating in this run.
The recommended material tier:

1. **Default (baseline):** IBS-deposited **HfO₂ / SiO₂** multilayer.
2. **Acceptable alternative:** IBS-deposited **ZrO₂ / SiO₂** multilayer
   — no coating-physics preference between HfO₂ and ZrO₂ at this
   fluence regime; vendor design choice.
3. **Upgrade tier (please quote as alternative):** **LaF₃ / MgF₂ on
   CaF₂ substrate** — fluoride multilayer, longest UV service life
   for forward-looking evacuated-cavity operation (current build is
   atmospheric, so this is optional).
4. **Excluded materials:** **Nb₂O₅** and **TiO₂** — bandgap too low
   for our 559 nm screening tier per Brown2019 / BC-D §C.1.
5. **No silica cap.** Brown2019: thin SiO₂ caps (1–5 μm) give zero
   measurable LIDT improvement under particulate contamination.

---

## Notes for the coating house

- **Quote against the default (HfO₂ / SiO₂) as the primary line
  item.** ZrO₂ / SiO₂ is acceptable if it is your existing
  validated design at this wavelength.
- **AOI band is binding.** A dichroic stack that meets all four spec
  rows (R ≥ 99.91 % @ 559, T ≥ 95 % @ 280, plus the AOI tolerance)
  *only at the nominal 13.7°* but drops outside spec at 12.2° or
  15.2° **fails this spec**. The ± 1.5° band is a *chosen procurement
  spec*, informed by a photogrammetric survey of fielded BBO doublers
  in our lab — not a bench-measured build-variation result. See
  cover letter §A.
- **Cleanliness on delivery is load-bearing.** MIL-STD-1246C
  Class 100 or better, double-bagged in cleanroom-grade packaging.
  Brown2019: particulate contamination drops LIDT by 3–6 orders of
  magnitude — this clause dominates any coating-stack choice. Cover
  letter §G is the procurement-acceptance condition.
- **G2-conditional service-life clauses** (cover letter §F): if
  the M4' fails worse than expected, the upgrade tier (LaF₃ / MgF₂
  on CaF₂) may be re-spec'd. Please indicate quote validity if
  re-quoting that alternative would be needed.
