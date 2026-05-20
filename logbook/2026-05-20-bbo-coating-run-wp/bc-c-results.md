# BC-C · Per-mirror coating targets — handoff to BC-D + BC-E

**Phase:** BC-C output ([`workplan.md`](workplan.md) §4 Phase BC-C)
**Status:** **FROZEN at BC-F closure (2026-05-20).** Values pinned; consumed by BC-D / BC-E. See [`closure.md`](closure.md).
**Authoritative for:** per-mirror R / T targets, AOI / polarization
annotations, substrate choice, per-mirror mirror-loss allocation,
beam-load hand-forwards to BC-D, per-mirror tolerance bands.

**Source.** [`bc-b-results.md`](bc-b-results.md) §F (per-scenario
`T_IC_opt`, single-variant centre 19 965 ppm, `Σ T_loss_VENDOR_max = 1 500 ppm`)
plus [`constants.md`](constants.md) §D (intensity envelope at the
1.5 W higher-stress scenario).

---

## A · Acceptance gate summary

| Gate (workplan §4 BC-C) | Required | Achieved | Status |
|---|---|---|---|
| Per-mirror table, one row per mirror | M1' / M2' / M3' / M4' | Four rows in §D below | ✅ |
| Nominal-target columns: per-scenario on M1', scenario-independent on M2'/M3'/M4' | R/T + AOI + pol + tolerance | §D rows + §C allocation table | ✅ |
| Worst-case columns at higher-stress scenario | LIDT requirement, dual-WL load, coating-absorption ceiling **flagged** for BC-D | §E hand-forward table | ✅ flagged (LIDT comparison itself is BC-D) |

---

## B · Inputs consumed from upstream

| From [`bc-b-results.md`](bc-b-results.md) §F | Value used here |
|---|---|
| `T_IC_opt` Low scenario (0.5 W) | 17 565 ppm (1.756 %) |
| `T_IC_opt` High scenario (1.5 W) | 22 945 ppm (2.295 %) |
| Single-variant centre (equal-penalty / minimax) | **19 965 ppm (2.00 %)** |
| Vendor manufacturing tolerance | ±500 ppm |
| `Σ T_loss_VENDOR_max` (mirror-loss budget) | 1 500 ppm summed across M2'/M3'/M4' |
| `L_total` operating point | 13 388 ppm |
| BC-E spec-sheet count | **1 M1' page** + 1 M2' + 1 M3' + 1 M4' + cover letter (§6 Q2 resolved → one variant) |

From [`constants.md`](constants.md) §A1 / §D:
- Beam waist `w₀ = 19.4 μm` at the BBO crystal centre.
- Spot radius at the curved mirrors `w(d′/2) ≈ 255 μm` (corrected; see §E methodology note for the BBO + air propagation rationale).
- Higher-stress (1.5 W) scenario at the chosen `L_total = 13 388 ppm`:
  `P_circ = 65.4 W` (intracavity 559 nm), `P_UV = 0.633 W`.

---

## C · Per-mirror passive-loss allocation

### C.1 · Why asymmetric, and how much

The workplan §4 BC-C default is equal allocation
(500/500/500 ppm). The asymmetry argument permitted by the workplan
("M4' dichroic typically delivers higher loss than a single-wavelength
HR, so the default allocation may need asymmetric weighting") is
load-bearing here:

- **M2'** is a *plane HR @ 559 nm at AOI ≈ 0°* — single-wavelength,
  near-normal incidence — the **easiest coating physics** of the
  four mirrors. Vendor catalog data (e.g. Layertec / Laseroptik /
  ATFilms specifications, **vendor-stated, not extracted into the
  dossier as of 2026-05-20**) suggests R ≥ 99.99 % (≤ 100 ppm) is
  routinely achievable on this seat at premium grade. Marked as
  **non-binding expectation** until a 559 nm IBS HR loss anchor lands
  in [`data/literature/`](../../data/literature/)
  ([`constants.md`](constants.md) §C path-1 follow-up).
- **M3'** is a *curved HR @ 559 nm at AOI 13.7° p-pol* — single-WL
  but with off-design AOI and curved-substrate physics. Slightly
  harder than M2'; vendor catalog data suggests R ≥ 99.97 % is
  achievable on premium-grade IBS, but same **non-binding
  expectation** caveat applies.
- **M4'** is a *curved dichroic: HR @ 559 nm AND HT @ 280 nm in
  the same stack at AOI 13.7° p-pol*. Two competing optical
  requirements force the design space; the 559-nm reflectivity loss
  on a dichroic is typically 3–5× larger than on a dedicated
  single-WL HR (Friedenauer's published M4' / M2' ratio of 2 000 / 700
  ppm is the **only extracted-tier data point** confirming this
  ratio in the dossier).

**Friedenauer-class precedent** (from [`constants.md`](constants.md) §B):

| Mirror | Friedenauer R-spec floor | Equivalent T-loss ceiling |
|---|---|---|
| M2' | R > 99.93 % | T < 700 ppm |
| M3' | R > 99.93 % | T < 700 ppm |
| M4' | R > 99.8 % | T < 2 000 ppm |
| **Sum** | — | **3 400 ppm** = `L_mirror_T_at_spec_limit` |

Friedenauer's M4' / M2' (or M3') ratio = **2 000 / 700 ≈ 2.9×**,
i.e. ~ 3:1 favouring the dichroic. We inherit this ratio and scale
down by the buildup-improvement factor `1 500 / 3 400 ≈ 0.44` to
land at the new total.

### C.2 · Allocation comparison (Σ = 1 500 ppm fixed)

| Policy | M2' (ppm) | M3' (ppm) | M4' (ppm) | Notes |
|---|---|---|---|---|
| Equal split (workplan default) | 500 | 500 | 500 | Under-uses M2' capability; under-budgets M4' |
| Slight M4' headroom | 400 | 400 | 700 | Compromise; partial Friedenauer ratio |
| **Friedenauer-class ratio — recommended** | **300** | **300** | **900** | Preserves Friedenauer 3:1 ratio; matches the empirically validated dichroic-vs-HR loss asymmetry |
| Aggressive M4' headroom | 250 | 250 | 1 000 | More headroom on M4' but tighter M2'/M3' may not be vendor-quotable economically |

**Recommended allocation: 300 / 300 / 900 ppm** (M2' / M3' / M4'),
matching Friedenauer's 3:1 dichroic-vs-HR ratio. Translates to:

| Mirror | T-loss ceiling | R-spec floor |
|---|---|---|
| M2' | ≤ 300 ppm | **R ≥ 99.970 %** @ 559 nm, AOI ≈ 0° |
| M3' | ≤ 300 ppm | **R ≥ 99.970 %** @ 559 nm, AOI 13.7° p-pol |
| M4' | ≤ 900 ppm at 559 nm | **R ≥ 99.910 %** @ 559 nm, AOI 13.7° p-pol (plus the T @ 280 nm spec in §D.4) |

All three R-floors are within **vendor-stated catalog capability** at
the design AOI/polarization (Layertec / Laseroptik / ATFilms / MLD
public catalogs cite ≥ 99.99 % HR @ visible wavelengths as a routine
deliverable; vendor catalog claims are *not* extracted into the
dossier as of 2026-05-20 and the path-1 follow-up in
[`constants.md`](constants.md) §C is the canonical place such an
anchor would land). The BC-E sheets quote these floors as **minimum**
R values; a vendor who commits to better R is welcome (BC-B noted
that lower loss shifts `T_IC_opt` and BC-B recomputes accordingly,
but lower loss is never a *failure mode*). **If a vendor pushes back
on the M4' R ≥ 99.910 % spec**, BC-B / BC-C re-open at the steward's
discretion — that pushback would itself be the loss-anchor data the
dossier currently lacks.

---

## D · Per-mirror specification table

Single-row-per-mirror summary, structured to map directly to the four
BC-E spec sheets.

### D.1 · M1' — plane input coupler (impedance-matched)

| Field | Value | Notes |
|---|---|---|
| Role | Plane input coupler, long-arm side, scenario-coupled | — |
| Geometry | Plane substrate, Ø 12.7 × 6.35 mm | Friedenauer-class form factor; alt sizes admissible if matched to mount |
| AOI | **~ 0° (normal incidence on long arm)** | Plane mirror in the bowtie ring's long arm |
| Polarization | p-pol (matching cavity polarization basis) | — |
| **T_IC target (single-variant centre, §6 Q2 resolved)** | **T = 19 965 ppm (2.00 %), or equivalently R = 98.0035 %** | Equal-penalty centre; both scenarios pay −0.68 % UV vs their optima |
| Tolerance | **± 500 ppm** (= ± 0.05 pp) | IBS-realistic; worst case ~ −1 % UV in either scenario |
| Per-scenario optima (informational; for the BC-E cover letter) | Low: 17 565 ppm (1.756 %); High: 22 945 ppm (2.295 %) | Quoted on the M1' page; vendor can target centre or per-scenario depending on quote economics (steward call at BC-E) |
| Back-face | **AR @ 559 nm**, R_AR ≤ 0.5 % at AOI ≈ 0° | Friedenauer §D.1 ("AR on outside") |
| Substrate | **Herasil (UV-grade FS)** | §6 Q3 default: uniform Herasil across all four mirrors (procurement simplification + UV-safe back-face) |
| Surface quality | scratch / dig ≤ 10/5 | Cavity-grade |
| Flatness | ≤ λ/10 @ 633 nm over the clear aperture | Standard plane-cavity-mirror grade |
| Wedge | ≤ 5 arcmin | Avoids back-face reflection alignment ambiguity |

### D.2 · M2' — plane HR (piezo seat for Hänsch–Couillaud servo)

| Field | Value | Notes |
|---|---|---|
| Role | Plane HR, long-arm side, piezo-mounted for HC lock | Friedenauer §D.2 |
| Geometry | Plane, Ø 12.7 × 6.35 mm | Matches piezo-mount footprint (cf. Thorlabs AE020304D04 + lead disk) |
| AOI | ~ 0° | Same plane as M1' |
| Polarization | p-pol | — |
| **R-spec floor (front face)** | **R ≥ 99.970 %** @ 559 nm, AOI 0° p-pol | Allocation 300 ppm per §C.2 |
| Tolerance on T-loss | ≤ 300 ppm absolute (= R ≥ 99.97 %) | Single-WL HR — well within premium IBS capability |
| Back-face | **AR @ 559 nm**, R_AR ≤ 0.5 % | Standard back-face AR |
| Substrate | **Herasil** | §6 Q3 default |
| Surface quality | scratch / dig ≤ 10/5 | — |
| Flatness | **≤ λ/10 @ 633 nm over CA** | Piezo seat — keeps loaded-resonance frequency reproducible across the run (workplan §3 fix) |
| Wedge | ≤ 5 arcmin | — |

### D.3 · M3' — curved HR (focusing mirror @ 559 nm)

| Field | Value | Notes |
|---|---|---|
| Role | Concave focusing HR, short-arm side, at the BBO waist | Friedenauer §D.1 |
| Geometry | **Concave, ROC = 50 mm** (= 2 f for f = 25 mm) | Friedenauer-frozen geometry |
| ROC tolerance | ± vendor-standard (≤ 1 % on R typical) | — |
| Clear aperture | ≥ 8 mm (centred) | Beam radius at the substrate ≈ 255 μm (corrected per §E); CA must cover with margin for alignment tolerance |
| AOI | **13.7° ± 1.5° p-pol** | **Chosen procurement band** centred at Friedenauer's nominal 13.7° per-curved-mirror AOI. The ±1.5° tolerance is *informed by* the [home-built doublers survey](../../docs/components/home-built-doublers.md) §3 photogrammetric fold-angle spread (mean folds 25°–29° at ±5° pixel-identification budget, source-tier `O*`) — i.e., consistent with typical bench-build variation but **not a bench-measured tolerance**. The band is set conservatively wider than the pixel-budget would strictly require, to absorb both photogrammetric uncertainty and realistic bench-alignment scatter. |
| Polarization | p-pol (TM) at the curved seat | Brewster-cut BBO + bowtie ring → p-pol everywhere |
| **R-spec floor** | **R ≥ 99.970 %** @ 559 nm, **specified over the AOI band 12.2°–15.2°** | Allocation 300 ppm; coating must hold spec across the chosen procurement-AOI window (see §D.3 AOI provenance note below) |
| Tolerance on T-loss | ≤ 300 ppm absolute | Single-WL HR at oblique incidence — vendor-achievable IBS class |
| Back-face | **AR @ 559 nm**, R_AR ≤ 0.5 %, on the convex side | Standard back-face AR; convex side is the substrate's outside |
| Substrate | **Herasil** | §6 Q3 default |
| Surface quality | scratch / dig ≤ 10/5 | — |
| Surface figure | **≤ λ/10 P-V over CA at 633 nm** | Irregularity over the full CA matters at the focus; centre-only figure not sufficient |
| Wedge / centring | Decentre of optical axis vs mechanical ≤ 5 arcmin | Standard centring spec for curved cavity mirrors |

### D.4 · M4' — curved output coupler dichroic

| Field | Value | Notes |
|---|---|---|
| Role | Concave dichroic output coupler — HR @ 559 nm front face + HT @ 280 nm in same stack; AR @ 280 nm back face | Friedenauer §D.1 |
| Geometry | **Concave, ROC = 50 mm** | Friedenauer-frozen |
| ROC tolerance | ± vendor-standard (≤ 1 %) | — |
| Clear aperture | ≥ 8 mm | Same beam-radius argument as M3' |
| AOI | **13.7° ± 1.5° p-pol** | Same chosen procurement band as M3' (see M3' AOI note above); dichroic stack must hold both R @ 559 nm and T @ 280 nm specs across the band |
| Polarization | p-pol | — |
| **R-spec at 559 nm, front face** | **R ≥ 99.910 %** @ 559 nm, specified over **12.2°–15.2°** AOI band | Allocation 900 ppm per §C.2 (Friedenauer-class 3:1 dichroic ratio) |
| Tolerance on 559 nm T-loss | ≤ 900 ppm absolute (≤ 1 000 ppm courtesy band acceptable) | Realistic IBS dichroic capability at 559 + HT @ 280 in same stack |
| **T-spec at 280 nm, front face (dichroic transmission)** | **T ≥ 95.0 %** @ 280 nm, AOI 13.7° p-pol | Tighter than Friedenauer's published floor (T > 94 %); modern dichroics typically deliver T ≥ 97 %, vendor encouraged to quote actual achievable T |
| **Back-face** | **AR @ 280 nm, narrow-band, centred at 280 nm**, R_AR ≤ 0.5 % at AOI 13.7° | §6 Q6 default: narrow-band (the CW chain is locked at Δ_ref = 40 GHz; no broadband need) |
| Substrate | **Herasil (UV-grade, UV-transmissive at 280 nm)** | §6 Q3 default; mandatory on M4' because 280 nm transits the substrate |
| Surface quality | scratch / dig ≤ 10/5 (both surfaces) | — |
| Surface figure (front concave) | ≤ λ/10 P-V over CA | — |
| Surface figure (back planar AR) | ≤ λ/10 P-V over CA | — |
| Wedge / centring | Decentre ≤ 5 arcmin | — |

---

## E · Beam loads at the higher-stress (1.5 W) scenario — hand-forward to BC-D

BC-C **flags** these loads; BC-D performs the LIDT comparison against
published CW thresholds. All values at the L_total = 13 388 ppm /
1.5 W operating point ([`bc-b-results.md`](bc-b-results.md) §F).

**Propagation methodology** (corrected from v1 draft of this file):
the spot radii below are computed via the Gaussian q-parameter from
the BBO short-arm waist (w₀ = 19.4 μm in BBO, n = 1.673), propagated
explicitly through the BBO crystal (5 mm in BBO from waist to exit
face), the BBO–air interface (`flat_interface` ABCD), then through air
to each mirror. The earlier v1 draft used a single Rayleigh range
(zR_BBO = 3.54 mm) for the full propagation, which underestimated
the curved-mirror spot. The corrected curved-mirror spot is
~ **255 μm** in air at d′/2 from the BBO waist, not the ~ 164 μm
quoted in v1 of this file. [`constants.md`](constants.md) §D.3 has
been updated in lockstep — both files now carry the corrected
~ 255 μm value with the v1 figure preserved in the methodology
notes for traceability.

For the **plane mirrors M1' / M2'**, the spot size is *not* a free-space
propagation result — after the curved mirror M4' (or M3') focuses the
beam back to a long-arm waist, the long-arm spot at each plane mirror
depends on where the plane mirror sits relative to that long-arm
waist. For a symmetric 3-leg bowtie (L_leg ≈ 137 mm per long-arm
section) the long-arm waist sits ~ 150–200 mm from each curved
mirror, with plane-mirror spots in the **~ 145–195 μm** range. Exact
values depend on Friedenauer's actual long-arm leg distribution,
which the paper does not enumerate.

| Mirror | Surface | λ | Power on optic | Spot radius | **Peak CW intensity** | BC-D action |
|---|---|---|---|---|---|---|
| M1' | front (inside cavity) | 559 nm | ≈ 65 W intracavity reflected fraction (R = 0.980) | ~ 150–200 μm (long-arm leg distribution dependent) | **~ 100–190 kW/cm²** | LIDT vs IBS-HR / IC at 559 nm |
| M1' | back (outside cavity) | 559 nm | 1.5 W input (mode-matched) | ~ 150–200 μm | ~ 2–4 kW/cm² | AR LIDT at 559 nm (low; far below threshold) |
| M2' | front (HR @ 559) | 559 nm | 65 W intracavity | ~ 150–200 μm | **~ 100–190 kW/cm²** | LIDT vs IBS-HR at 559 nm |
| M3' | front (curved HR @ 559) | 559 nm | 65 W intracavity | ~ 250 μm | **~ 65 kW/cm²** | LIDT vs IBS-HR at 559 nm and at oblique AOI |
| M4' | front (curved dichroic) | 559 nm + 280 nm dual | 65 W @ 559 + 0.63 W @ 280 transit | ~ 250 μm | **~ 65 kW/cm² @ 559** + **~ 0.6 kW/cm² @ 280 transit** | **Dual-wavelength LIDT** vs IBS-dichroic at 559 + 280; the binding case among the four mirrors |
| M4' | back (AR @ 280) | 280 nm | 0.63 W outgoing | ~ 250 μm | **~ 0.6 kW/cm² @ 280** | LIDT vs IBS-AR at 280 nm; binding axis for 280 nm degradation (G2 inheritance) |

**Headline for BC-D.** The binding LIDT case is **M4' front face
at the 559 nm intracavity + 280 nm transit dual-wavelength load**
(~ 65 kW/cm² @ 559 + ~ 0.6 kW/cm² @ 280, CW). The dichroic stack
carries both wavelengths in the same coating layers, so the BC-D
comparison against published thresholds (Burkley2021 SCAFFOLD-tier,
Turcicova2022) must consider the combined load, not each
wavelength separately.

The **plane mirrors M1'/M2' carry the highest 559 nm intensity**
(~ 100–190 kW/cm², because the long-arm waist focuses tighter than
the short-arm-mirror spot in a symmetric bowtie). This is a
single-wavelength load and the IBS-HR LIDT envelope at 559 nm is
high — comfortably above this range for premium-grade dielectric
coatings (BC-D quantifies the margin against the dossier).

**At the lower-stress (0.5 W) scenario** the intracavity intensities
scale by P_circ ratio: ~ 28.5/65 = 0.44× → all 559 nm fluences drop
to ~ 44 % of the 1.5 W column above. The 280 nm outgoing scales by
P_UV ratio: 0.12/0.63 = 0.19× → ~ 19 %. Both comfortably below the
1.5 W case; **worst-case spec is the 1.5 W column above**.

**Uncertainty bands.** The spot-radius estimates carry an envelope
of order ± 30 % due to Friedenauer's under-specified long-arm leg
distribution. The intensity envelope is therefore approximate, and
BC-D should treat the values as **order-of-magnitude inputs** to the
LIDT margin calculation, not as bench-measured numbers. The
qualitative conclusion that **M4' is the binding LIDT case** is
robust under this envelope (the M4' uniqueness comes from its
*dual-wavelength* burden, not from quantitative-fluence
considerations).

---

## F · §6 Q6 (AR @ 280 nm bandwidth) — narrow-band recommended

[`workplan.md`](workplan.md) §6 Q6 asked: narrow-band AR (single
wavelength centred at 280 nm) vs broadband AR (250–300 nm). BC-C
adopts the **narrow-band default**:

- The CW chain is locked at `Δ_ref = 40 GHz` ≈ 0.01 nm at 280 nm —
  far smaller than even a narrow-band AR bandwidth (~ 5 nm typical).
- The pulsed-Raman alternative architecture (which would need
  broadband) does **not** share components with this CW build per
  [`docs/architectures/`](../../docs/architectures/) (Council-3 task
  split, [next-gen workplan](../2026-05-08-next-gen-500mW-workplan.md)).
- Narrow-band AR is cheaper to spec and easier for the coating house
  to hit at the design AOI.

If the broadband alternative ever needs to be re-evaluated, the BC-E
sheet for M4' carries a footnote ("vendor may quote broadband
250–300 nm AR as an upgrade option at incremental cost").

---

## G · §6 Q3 (substrate uniformity) — Herasil throughout

The workplan §6 Q3 default is **uniform UV-grade Herasil substrate
across all four mirrors**. BC-C inherits the default verbatim:

- M4' *requires* Herasil (UV-transmissive at 280 nm for the back-face
  AR + dichroic substrate).
- M1' / M2' / M3' only see 559 nm and could use ordinary FS, but
  uniform Herasil is:
  - **logistically simpler** (single substrate inventory; no bench
    mix-ups);
  - **scatter-uniform** (same bulk material; no spurious dichroic-
    stack absorption asymmetries);
  - **negligible cost premium** at IBS-cavity-grade pricing.

The BC-E cover letter carries a one-line note that the vendor may
substitute ordinary UV-grade fused silica (Heraeus equivalent) on
M1' / M2' / M3' if doing so reduces lead time, but Herasil remains
the preferred default.

---

## H · Tolerance and what the BC-E sheets need to call out

The single most important thing BC-E must communicate to the coating
house is the tolerance regime:

- **M1' (impedance-matched IC):** `T = 19 965 ± 500 ppm`. The
  ±500 ppm corresponds to ±0.05 pp absolute and is matched to
  realistic IBS metrology. UV-output penalty at the band edge:
  ~ −1 % in either scenario (per [`bc-b-results.md`](bc-b-results.md) §D).
- **M2' / M3' / M4' (R-spec):** Floor specs (R ≥ X %), not
  centre + tolerance. Vendor commits to *at least* the floor;
  better is welcome. **No upper bound on R** — buildup-helpful, not
  buildup-harmful.
- **M4' T_280 spec:** Floor (T ≥ 95 %), same logic as the
  R-specs. Vendor encouraged to quote actual achievable T (typically
  97–98 % for IBS dichroics).
- **AOI band:** 13.7° ± 1.5° on the curved seats. **Specified over
  the band**, not just at the nominal AOI. This is the load-bearing
  fix from the home-built-doublers survey.

---

## I · Findings handed forward

1. **§6 Q2 already-resolved one M1' variant** is the right call —
   confirmed numerically at BC-B and unchanged here.
2. **300 / 300 / 900 ppm mirror-loss allocation** chosen over the
   workplan's equal-split default. Friedenauer's published 3:1
   dichroic-vs-HR ratio is the precedent.
3. **Narrow-band AR @ 280 nm** on M4' (§6 Q6 default).
4. **Uniform Herasil substrate** across all four mirrors (§6 Q3
   default).
5. **M4' front face is the binding LIDT case** for BC-D — dual-
   wavelength load at **~ 65 kW/cm² CW @ 559 + ~ 0.6 kW/cm² CW @ 280**
   transit (corrected from v1 154.7 / 1.5 kW/cm² per §E methodology
   note). BC-D consumes this from §E above.
6. **AOI band spec (±1.5°)** is the load-bearing M4' coating-physics
   detail. Without it, the dichroic stack's reflectivity and
   transmission would slip off-target across realistic bench-alignment / AOI
   fold-angle variation.

---

## J · Open items handed to BC-D and BC-E

**To BC-D:**
- Compare the §E intensities against the dossier LIDT envelopes
  (Burkley2021 SCAFFOLD-tier 280 nm UV cavity-mirror data;
  Turcicova2022 BBO LIDT review).
- Quantify the LIDT margin at the M4' front-face dual-wavelength
  load (the binding axis).
- Provide a service-life envelope conditional on G2 closure
  (UV-induced degradation rate, currently OPEN).

**To BC-E:**
- Build five per-mirror pages from §D: M1' / M2' / M3' / M4' + cover
  letter. The cover letter must explicitly justify why the new spec
  targets a **higher T_IC** than the Friedenauer-2006 reference
  (per [`bc-b-log.md`](bc-b-log.md) finding 3.6 % buildup forgone).
- The M1' page carries:
  - One single-variant centre row (19 965 ppm ± 500 ppm) as the
    primary spec, *plus*
  - The two per-scenario optima (17 565 / 22 945 ppm) as informational
    rows on the same page, with a sentence explaining the
    one-variant rationale (equal-penalty centring, ~ −0.68 % UV vs
    either optimum).
- Cover-letter clauses to include:
  - **AOI band** (13.7° ± 1.5° on curved seats; ~ 0° ± 1° on plane).
  - **Substrate** (Herasil throughout, with FS-equivalent fallback
    on M1'/M2'/M3' if lead time is the binding constraint).
  - **Quantity** (N = 4 per role, yielding 4 full sets, per §6 Q5
    default; the procurement KD downstream may revise).
  - **LIDT margin** (referenced to BC-D's analysis; G2 OPEN
    qualifier).
  - **Bandwidth on the AR @ 280 nm** (narrow-band default; broadband
    upgrade option).

---

## K · Charter compliance

- **§5.1 anti-seeding.** BC-C produces tabulated specifications, not
  architecture-family-specific code. No commit to `/src/`.
- **γ authority.** [`constants.md`](constants.md) consulted as the
  single γ / L source.
- **Result class.** *Sail* — advisory until vendor quotes return
  and a procurement KD closes. The BC-D LIDT comparison and the
  BC-E spec-sheet drafting are downstream phases; BC-C is the
  per-mirror translation layer between BC-B's cavity-level result
  and BC-E's vendor-facing artefacts.
