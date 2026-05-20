# BC-D · LIDT and substrate constraints — handoff to BC-E

**Phase:** BC-D output ([`workplan.md`](workplan.md) §4 Phase BC-D)
**Status:** **FROZEN at BC-F closure (2026-05-20).** Values pinned; consumed by BC-E. See [`closure.md`](closure.md).
**Authoritative for:** per-mirror LIDT margin at the 1.5 W scenario,
material-class recommendation for the M4' dichroic stack, substrate
confirmation, surface-quality + flatness floor.

**Source.** [`bc-c-results.md`](bc-c-results.md) §E (per-mirror peak
intensities at the 1.5 W higher-stress scenario), plus the dossier
notes for [`Brown2019`](../../data/literature/Brown2019/notes.md),
[`Burkley2021`](../../data/literature/Burkley2021/notes.md),
[`Turcicova2022`](../../data/literature/Turcicova2022/notes.md),
[`Kondo1998`](../../data/literature/Kondo1998/notes.md), and
[`Kubota1998`](../../data/literature/Kubota1998/notes.md).

---

## A · Acceptance gate summary

| Gate (workplan §4 BC-D) | Required | Achieved | Status |
|---|---|---|---|
| Per-mirror peak CW intensity at the design point | Plane + curved + per-surface for M4' | Inherited from [`bc-c-results.md`](bc-c-results.md) §E; restated in §B below | ✅ |
| Comparison to published CW LIDT envelopes at 559 nm and 280 nm | Brown2019 / Burkley2021 / Turcicova2022 / Kondo–Kubota (honest dossier state) | §C analysis | ✅ |
| Substrate requirements | UV-grade mandatory on M4'; uniform Herasil per §6 Q3 | §D confirmation | ✅ |
| Surface quality + flatness envelope | scratch / dig ≤ 10/5; flatness ≤ λ/10 @ 633 nm | §E restated for BC-E | ✅ |
| Scenarios exceeding LIDT margins flagged | de-rate or escalate | **No fatal exceedance** at 1.5 W; **the 280 nm axis sits ~ 1.15 × *above*** the closest CW UV operational benchmark (Kondo / Kubota 266 nm 1 000-h point) — this is the **binding constraint**, not a margin. G2-conditional escalation paths in §F.2. | ✅ flagged |

---

## B · Per-mirror peak CW intensities at the 1.5 W scenario

Inherited from [`bc-c-results.md`](bc-c-results.md) §E (after the v2
spot-radius correction). Restated here for self-contained reference:

| Mirror | Surface | λ | Peak CW intensity | Spot avg (Gaussian peak/2) |
|---|---|---|---|---|
| M1' | front (intracavity reflection) | 559 nm | ~ 100–190 kW/cm² | ~ 50–95 kW/cm² |
| M1' | back (input side) | 559 nm | ~ 2–4 kW/cm² | ~ 1–2 kW/cm² |
| M2' | front (HR @ 559 nm) | 559 nm | ~ 100–190 kW/cm² | ~ 50–95 kW/cm² |
| M3' | front (curved HR @ 559 nm, AOI 13.7°) | 559 nm | ~ 65 kW/cm² | ~ 33 kW/cm² |
| **M4'** | **front (curved dichroic, AOI 13.7°)** | **559 nm + 280 nm dual** | **~ 65 kW/cm² @ 559 + ~ 0.6 kW/cm² @ 280** | ~ 33 kW/cm² @ 559 + ~ 0.3 kW/cm² @ 280 |
| M4' | back (AR @ 280 nm) | 280 nm | ~ 0.6 kW/cm² | ~ 0.3 kW/cm² |

The plane-mirror range (100–190 kW/cm²) carries the leg-distribution
uncertainty BC-C §E flagged — actual value at each mirror depends on
where it sits relative to the long-arm waist.

---

## C · LIDT margin analysis

### C.1 · 559 nm axis — all four mirrors (screening comparison)

**Important: Brown2019 thresholds below are at 1070 nm CW**, not at
559 nm. The workplan and Brown2019's own notes both record that
*absolute* thresholds are not portable across wavelengths — only the
mechanism (thermal free-carrier breakdown from contamination heating)
and the *material-bandgap ranking* are. The table below is therefore
a **screening comparison** — useful for ranking materials and for
order-of-magnitude reassurance that we are not approaching the
visible-light damage envelope — **not** a literal LIDT pass/fail at
559 nm.

| Material (Brown2019 1070 nm CW runaway — *screening only*) | 1070 nm Threshold | Ratio vs our M1'/M2' worst case (190 kW/cm² at 559 nm) |
|---|---|---|
| Silica (Eg ~ 9 eV) | > 17 800 kW/cm² (no damage at highest tested) | > 94 × |
| Alumina (Eg ~ 8.7 eV) | 6 300 kW/cm² | 33 × |
| Hafnia (Eg ~ 5.8 eV) | 3 800 kW/cm² | 20 × |
| Tantala (Eg ~ 4.3 eV) | 1 600 kW/cm² | 8.4 × |
| Niobia (Eg ~ 3.4 eV) | ~ 200 kW/cm² (extrapolated from Fig. 4) | ~ 1 × |
| Titania (Eg ~ 3 eV) | ~ 100 kW/cm² | < 1 × |

**Wavelength scaling caveat.** Brown2019 thresholds are at 1070 nm.
The mechanism is wavelength-scalable, but **absolute thresholds may
drop at 559 nm** because contamination absorption is typically higher
at shorter wavelengths. The ratios above are therefore a *screening
upper bound* on the 559 nm threshold, not the threshold itself. With
that qualifier:

- **Materials with > 20 × screening ratio (silica, alumina, hafnia)**
  carry adequate headroom for both worst-case visible-fluence axes
  even under wavelength-scaling pessimism.
- **Tantala** (8.4 × screening) is acceptable for low-fluence seats
  but is the marginal case — usable but not preferred.
- **Niobia and titania** (≤ 1 × screening) **must be avoided** —
  even pessimistic wavelength scaling does not yield a coating-class
  recommendation for these materials at the 559 nm flux levels here.

No measured 559 nm IBS HR coating-LIDT anchor exists in the dossier
(BC-A §C path-1 follow-up); the screening above is the strongest
statement currently supported.

### C.2 · 280 nm axis — M4' front transit + M4' back AR

The 280 nm load on the M4' coating stack and back-face AR is the
**binding axis** for the WP. Compare against the closest-wavelength
CW UV data points in the dossier:

| Benchmark | Wavelength | Fluence | Outcome | Comparison to our 600 W/cm² peak |
|---|---|---|---|---|
| [`Kondo1998`](../../data/literature/Kondo1998/notes.md) / [`Kubota1998`](../../data/literature/Kubota1998/notes.md) — Sony Cz-BBO operational lifetime | 266 nm | 260 W/cm² CW (UV power density) | **1 000 h with 5 × 10⁻⁵ %/h cavity-loss-rate increase** | Our ~ 300 W/cm² avg is **~ 1.15 × *above*** their fluence; expect a service-life on the *same order of magnitude* as their 1 000 h envelope, *not* a comfortable margin below it |
| [`Hannig2018`](../../data/literature/Hannig2018/notes.md) — PTB 626 → 313 nm BBO ring SHG | 313 nm | not extracted (PDF staged) | **130 h CW, no power decay observed** | Different wavelength (313 vs 280 nm) and unextracted fluence; service-life comparison qualitative only |
| [`Burkley2021`](../../data/literature/Burkley2021/notes.md) — PTB / Lebedev 244 nm UHV cavity | ~ 244 nm | 5 W intracavity (spot size, finesse, mirror fluence **not yet extracted**; PDF staged) | **Oxide (HfO₂/Al₂O₃/SiO₂) degrades within minutes in UHV (10⁻⁸ mbar)**; fluoride (MgF₂/LaF₃/CaF₂) survives 10 W for hours in O₂-rich (10⁻⁴–1 mbar O₂) | **No numerical fluence comparison admissible until Burkley2021 is extracted past SCAFFOLD.** What we *do* inherit: the mechanism (UV-driven oxide-coating degradation + hydrocarbon contamination, accelerated under UHV) and the qualitative material ranking (fluoride > oxide at UV). The "below the Burkley-failure regime" claim is **not** supported by the current dossier state |
| [`Turcicova2022`](../../data/literature/Turcicova2022/notes.md) — BBO bulk CW (Nikogosyan compendium) | not specified, probably DUV | 1–10 kW/cm² CW | (Bulk LIDT, not coating) | Our 280 nm transit at 0.6 kW/cm² is below this bulk threshold |

**Order-of-magnitude finding (revised).** Our 280 nm M4' transit
fluence (~ 600 W/cm² peak / ~ 300 W/cm² avg) **sits ~ 1.15 × above**
the Kondo / Kubota 1 000-hour 266 nm CW operating point on bulk BBO.
This is **the closest-wavelength CW UV operational benchmark in the
dossier**, and our scenario sits on the same order of magnitude
(not below). The 280 nm axis is therefore the **binding LIDT axis
of this WP**, with service-life uncertainty dominated by:

1. The single-data-point nature of the Kondo / Kubota benchmark
   (extrapolating one operational lifetime to a coating problem is
   informative but not definitive).
2. The wavelength offset 266 nm → 280 nm (small but unmeasured;
   slightly *favours* our build by photon-energy scaling).
3. **Burkley2021 SCAFFOLD status** — the most directly comparable
   *coating* data point is not yet extracted to a numerical fluence
   in the dossier. Full extraction is the highest-leverage BC-D
   follow-up (queued as path-1 in [`constants.md`](constants.md) §C).
4. **G2-OPEN.** No measured 280 nm coating-lifetime at our specific
   fluence-and-class regime in the dossier.

**Honest service-life envelope at 1.5 W:** *same order of magnitude
as the Kondo / Kubota 1 000-hour benchmark, plausibly somewhat
shorter*. Conditional clauses in §F.2 below cover the failure-mode
escalation paths.

### C.3 · Material-ranking recommendation for M4' dichroic stack

Anchored in [`Brown2019`](../../data/literature/Brown2019/notes.md)
bandgap scaling + [`Turcicova2022`](../../data/literature/Turcicova2022/notes.md)
§4.3 deposition ranking:

**For the 559 nm HR + 280 nm HT dichroic stack on M4'**, the
recommended composition is a single coherent policy with one default
and two alternative tiers:

1. **Default (baseline):** **IBS-deposited HfO₂ / SiO₂ multilayer.**
   HfO₂ (Eg = 5.8 eV) as the high-index layer, SiO₂ (Eg = 9 eV) as
   the low-index. This is the standard PTB-class dichroic stack at
   this wavelength and the inferred Friedenauer-2006 composition.
   Vendor catalogs at all four shortlisted houses (Layertec /
   Laseroptik / ATFilms / MLD) offer this stack as a stock design.
2. **Acceptable alternative:** **ZrO₂ / SiO₂ multilayer** (ZrO₂
   Eg = 5.0 eV). Comparable bandgap and Brown2019-screening tier to
   HfO₂; admissible if a vendor's existing dichroic design uses
   ZrO₂ instead of HfO₂. **No coating-physics preference** between
   HfO₂ and ZrO₂ at this fluence regime.
3. **Upgrade tier (forward-looking):** **Fluoride multilayer**
   (LaF₃ / MgF₂ on CaF₂ substrate, per Burkley2021's UHV-survival
   data). LaF₃ (Eg ≈ 11 eV) and CaF₂ are the best-LIDT choice for
   pure-UV intracavity operation. Currently *not* required because
   our M4' carries 280 nm only as a transit beam (not intracavity)
   and our operating environment is laboratory atmosphere; flagged
   as the escalation path if G2 closes worse than Burkley's
   oxide-class data.
4. **Excluded materials:** **Nb₂O₅ and TiO₂.** Brown2019 screening
   places them below the ~ 1 × headroom band even for the visible
   axis; not acceptable in any layer.
5. **Deposition method:** **IBS (ion-beam sputtering)** explicitly —
   Turcicova2022 §4.3 ranks IBS > magnetron > e-beam > pulsed-laser-
   deposition for damage tolerance. The BC-E sheet specifies IBS as
   the required process.
6. **Cap-layer recommendation:** **No silica cap**. Brown2019 shows
   thin SiO₂ caps (1–5 μm) give zero measurable LIDT improvement
   under particulate contamination; don't pay the cost premium.
7. **Operating environment (forward-looking note):** Burkley2021's
   oxide-vs-fluoride difference is mechanism-driven (oxygen
   depletion of the high-index oxide under UV in UHV).
   **Recommendation: operate the BBO ring in laboratory atmosphere
   or O₂-rich purge — *not* UHV**. The current build is
   atmospheric, so this is forward-looking only.

**Cover-letter sentence for BC-E:** "The M4' dichroic stack default is
**IBS-deposited HfO₂ / SiO₂ multilayer**; **ZrO₂ / SiO₂** is acceptable
as a vendor-design alternative. **LaF₃ / MgF₂ on CaF₂** is the
upgrade-tier option for the longest UV service life, available on
quote. **Nb₂O₅ and TiO₂ are excluded.** No silica cap required."

### C.4 · Service-life envelope (G2-conditional)

| Mirror | Service-life envelope at 1.5 W scenario | Conditional on |
|---|---|---|
| M1' / M2' (plane HRs) | > 1 000 h, < 1 %/100 h loss-rate increase expected | Premium IBS deposition; no niobia / titania |
| M3' (curved HR @ 559) | > 1 000 h, < 1 %/100 h | Same |
| **M4' (curved dichroic)** | **Order of magnitude of the Kondo / Kubota 1 000-hour benchmark at 1.5 W, plausibly somewhat shorter**; **> 1 000 h at 0.5 W**; monotonic loss-rate increase | IBS deposition + atmospheric or O₂-rich operation + recommended material stack (§C.3). The 280 nm fluence sits ~ 1.15 × *above* the Kondo / Kubota benchmark, so service life is order-of-magnitude *match*, not margin below. Burkley2021 numerical fluence comparison **not admissible** until extraction past SCAFFOLD — see §C.2 |
| M4' back AR @ 280 | > 1 000 h | Same |

**G2 inheritance.** Quantitative service-life numbers above are
**bracketed**, not measured. G2 (UV-induced degradation rate at 280 nm
on the new build's coating-class) remains OPEN per CHARTER §1.5; the
absolute service-life claim is conditional on G2 closure and on the
actual vendor coating quality. The BC-E cover letter carries this
qualifier.

---

## D · Substrate confirmation (Herasil throughout)

BC-C §G chose UV-grade Herasil substrate across all four mirrors.
BC-D confirms this is the right LIDT-aware choice:

| Argument | Source | Verdict |
|---|---|---|
| M4' substrate must be UV-transmissive at 280 nm | Standard optics — 280 nm transits the M4' substrate to exit the cavity | **Mandatory** Herasil (or equivalent UV-grade FS) on M4' |
| Bulk absorption at 280 nm in UV-grade fused silica | Heraeus Suprasil 300 specifies < 50 ppm/cm @ 280 nm | Acceptable; Herasil-class meets this |
| Stray-light + scatter uniformity argument across all four mirrors | [`bc-c-results.md`](bc-c-results.md) §G | Uniform Herasil avoids substrate-class scatter mismatch |
| Bench mix-up prevention | Logistical | Single substrate inventory simplifies build verification |
| Cost premium for Herasil over ordinary UV-grade FS | Negligible at cavity-grade IBS pricing | Accept |

**Conclusion.** Herasil throughout — confirmed. BC-E sheets quote
"Heraeus Herasil or equivalent UV-grade fused silica" as the substrate
spec on all four pages, with a one-line "FS-equivalent acceptable on
M1' / M2' / M3' if it reduces lead time" footnote on those three pages
only (NOT on M4').

---

## E · Surface-quality and flatness envelope (BC-E spec floor)

Standard cavity-grade IBS coating-substrate specifications that the
BC-E sheets must explicitly state:

| Spec | Value | Source |
|---|---|---|
| Scratch / dig | **≤ 10 / 5** per MIL-PRF-13830B | Cavity-grade floor; consistent across all four mirrors |
| Flatness (front face, P–V at 633 nm) | **≤ λ/10 over the clear aperture** | Standard plane-mirror grade for M1', M2'; the cavity ABCD stability is mildly sensitive to substrate flatness on the plane mirrors. **M2' flatness is binding** for the HC servo seat (loaded-mount resonance reproducibility) |
| Surface figure (curved face, irregularity over CA) | **≤ λ/10 P–V** | M3' / M4' curved-mirror tolerance; centre-only figure is *not* sufficient for the BC-E spec — irregularity over CA matters at the focus |
| Wedge (plane mirrors) | ≤ 5 arcmin | Prevents back-face ghost ambiguity |
| Centring (curved mirrors) | Decentre of optical axis vs mechanical ≤ 5 arcmin | Standard centring for curved cavity mirrors |
| Clear aperture | ≥ 8 mm (centred) on all four mirrors | Beam radius ≤ 255 μm; CA gives ~ 30 × margin for alignment tolerance |
| Cleanliness on delivery | MIL-STD-1246C Class 100 or better, double-bagged in cleanroom-grade packaging | Brown2019: particulate contamination drops LIDT 3–6 orders of magnitude — handle accordingly |

The cleanliness-on-delivery row is **non-standard for vendor catalogs**
but is the load-bearing detail from Brown2019; the BC-E cover letter
calls it out explicitly.

---

## F · Open items handed forward

### To BC-E:

- The per-mirror LIDT paragraphs in §C.1 / §C.2 are short enough to
  paste into the BC-E spec sheets as the "LIDT (CW)" row, with the
  measured-vs-extrapolated qualifier carried through.
- The material-ranking sentence in §C.3 belongs in the cover letter,
  not the per-mirror sheets — vendors will quote against whatever
  dichroic-design they have already validated.
- The cleanliness-on-delivery clause (§E final row) is the
  load-bearing handling specification; BC-E quotes it in the
  cover letter as a procurement-acceptance condition.

### To the procurement KD (downstream of this WP):

- **G2 measurement is the binding service-life follow-up.** Until G2
  closes, all service-life numbers are bracket estimates. The first
  candidate measurement would be the M4' loss-rate increase under
  the 1.5 W operating scenario, monitored over 100+ h.
- **Burkley2021 numerical extraction.** The dossier carries Burkley2021
  as SCAFFOLD; full extraction (intracavity power, mirror finesse,
  spot size at the mirrors, time-to-failure curves) would tighten
  the BC-D service-life envelope on M4'. Queued as a follow-up
  task-E entry; not blocking the BC-E spec sheets.
- **Hannig2018 numerical extraction.** Same as Burkley2021 — the
  130-hour 313 nm CW result is a useful but unextracted operational-
  lifetime data point.

### G2 conditional clauses:

- The §C.4 service-life envelope assumes the M4' coating performance
  matches Friedenauer's published Sony / Crystals-of-Siberia-class
  operating lifetime under the same UV fluence regime.
- If G2 closes at a value worse than Burkley's *fluoride-class* data,
  the M4' coating must be re-specced toward LaF₃ / MgF₂ / CaF₂
  multilayers (currently flagged as "vendor design alternative" not
  as the BC-E default).
- If G2 closes at a value worse than Burkley's *oxide-class* data
  (i.e., M4' degrades within minutes-to-hours at the 1.5 W
  scenario), the **WP closes with the 0.5 W scenario only** as
  build-viable; the 1.5 W scenario becomes architecturally untenable
  without crystal / oven re-engineering.

---

## G · Charter compliance

- **§5.1 anti-seeding.** BC-D produces a tabulated LIDT analysis
  consuming dossier-extracted numbers; no architecture-family-
  specific code, no commit to `/src/`.
- **G2 inheritance.** Explicitly OPEN per CHARTER §1.5; all
  service-life numbers above are conditional. The BC-E cover letter
  carries this qualifier verbatim.
- **G1 inheritance.** The 14-GHz unlockable domain (Friedenauer §4)
  is inherited from the crystal + cavity-geometry choice ([`workplan.md`](workplan.md) §7)
  and is **not** introduced by the coating choices. BC-D therefore
  has no G1 impact.
- **Result class.** *Sail* — advisory until vendor quotes return
  and the procurement KD closes downstream.

---

## H · Findings handed forward

1. **No fatal LIDT exceedances** at the 1.5 W operating point. The
   559 nm axis carries ≥ 8 × screening-tier ratios against
   wavelength-pessimistic Brown2019 thresholds (§C.1). **The 280 nm
   axis is the binding case** — our M4' fluence sits ~ 1.15 × *above*
   the Kondo / Kubota 266 nm 1 000-hour CW operational benchmark, so
   the 280 nm result is *not* a margin but rather an
   *order-of-magnitude match* to a measured 1 000-hour data point.
2. **M4' front face is the binding LIDT case.** Conditional service
   life at 1.5 W: **same order of magnitude as the Kondo / Kubota
   1 000-hour benchmark, plausibly somewhat shorter**; at 0.5 W,
   comfortably above that benchmark. The numerical bracket is
   dossier-uncertainty-dominated — Burkley2021 numerical extraction
   would tighten it materially.
3. **Material ranking for the M4' dichroic stack:** IBS-deposited
   HfO₂ or ZrO₂ (high-index) + SiO₂ (low-index) at minimum; avoid
   niobia / titania. LaF₃ / MgF₂ / CaF₂ fluoride alternatives are
   acceptable upgrade options if vendor design allows.
4. **Operating environment recommendation:** atmospheric or
   O₂-rich; avoid UHV per Burkley2021's oxide-vs-fluoride
   mechanism. (Current build is atmospheric; this is a forward-
   looking note for any future evacuated-cavity variant.)
5. **Cleanliness on delivery is load-bearing** per Brown2019 (3–6
   orders of magnitude LIDT drop under particulate contamination).
   BC-E cover letter carries this as an explicit procurement-
   acceptance condition.
6. **G2 closure is the binding follow-up** for absolute service-life
   numbers. Current BC-D envelope is bracket-tier, not measurement-
   tier.

---

## I · BC-E unblocked

BC-E now has all per-mirror inputs frozen:

- **BC-C §D**: per-mirror R/T-targets, AOI bands, substrate choice,
  ROC / CA / surface-quality / wedge / flatness floors.
- **BC-D §C / §E** (this file): LIDT margin paragraph per mirror,
  material-ranking recommendation, cleanliness-on-delivery clause.
- **BC-B §F**: M1' centre point (19 965 ppm ± 500 ppm) + per-scenario
  optima as informational rows.
- **BC-A §F**: cover-letter justification for `T_IC` higher than the
  Friedenauer-2006 reference (3.6 % buildup forgone).

BC-E's job is now mechanical: assemble five pages (M1' / M2' / M3' /
M4' + cover letter) by mapping the per-mirror tables in
[`bc-c-results.md`](bc-c-results.md) §D (D.1–D.4 are structured to
map directly to four spec-sheet pages per the §D intro), with the
open-items hand-forward in §J of that file capturing the items the
cover letter must echo.
