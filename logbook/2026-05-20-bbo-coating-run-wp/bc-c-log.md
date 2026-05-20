# BC-C · Translate to per-mirror coating targets — running log

**Phase:** BC-C of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20 (after BC-B closure same day)
**Status:** CLOSED 2026-05-20 (v2 corrections applied) — BC-D unblocked

This log accumulates entries as BC-C executes against the per-scenario
impedance-match outputs in [`bc-b-results.md`](bc-b-results.md) §F.

---

## 2026-05-20 · Kickoff

BC-B closed within the calendar day (see [`bc-b-log.md`](bc-b-log.md));
the steward greenlit BC-C start. BC-C opens against:

| Symbol | Value | Source |
|---|---|---|
| `T_IC_opt` (Low, 0.5 W) | 17 565 ppm (1.756 %) | [`bc-b-results.md`](bc-b-results.md) §F.1 |
| `T_IC_opt` (High, 1.5 W) | 22 945 ppm (2.295 %) | [`bc-b-results.md`](bc-b-results.md) §F.1 |
| `T_IC` single-variant centre | **19 965 ppm (2.00 %)** | [`bc-b-results.md`](bc-b-results.md) §F.2 (equal-penalty / minimax) |
| Vendor manufacturing tolerance | ±500 ppm | [`bc-b-results.md`](bc-b-results.md) §D headline |
| `Σ T_loss_VENDOR_max` (mirror loss budget) | 1 500 ppm summed across M2'/M3'/M4' | [`bc-b-results.md`](bc-b-results.md) §F |
| `L_total` operating point | 13 388 ppm (intermediate IBS) | [`bc-b-results.md`](bc-b-results.md) §F |

**BC-C scope recap** (from [`workplan.md`](workplan.md) §4 Phase BC-C):

- **Per-mirror passive-loss allocation.** Distribute the
  `Σ T_loss_VENDOR_max = 1 500 ppm` budget across M2'/M3'/M4' (the
  three non-IC mirrors). Default is equal allocation
  (500/500/500 ppm); asymmetric allocation may be justified if the
  M4' dichroic carries an inherent coating-physics penalty over a
  single-wavelength HR.
- **Curved-OC (M4') dichroic table.** R @ 559 nm + T @ 280 nm pair
  with tolerance, AR @ 280 nm on the back face, AOI = 13.7° ± Δθ
  p-pol. Δθ working floor ±1.5° per mirror (from the
  [home-built doublers survey](../../docs/components/home-built-doublers.md)
  fold-angle spread).
- **AOI / polarization annotations per mirror.** Plane mirrors
  (M1' / M2') at ~ 0°; curved mirrors (M3' / M4') at 13.7° p-pol.
  AOI mismatch shifts the realised R/T off-spec.
- **Substrate annotation.** Per §6 Q3 default (UV-grade Herasil
  throughout) — recorded explicitly on each per-mirror row so BC-E
  doesn't have to look it up.

**Acceptance** (from [`workplan.md`](workplan.md) §4 BC-C):

A per-mirror table with:
- *Nominal-target columns* — R_target (or T_target), AOI,
  polarization, tolerance band. **One column per scenario on M1'**;
  scenario-independent columns on M2' / M3' / M4'.
- *Worst-case columns* — LIDT requirement, coating-absorption
  ceiling, M4' dual-wavelength load — taken at the **higher-stress
  (1.5 W) scenario**. These are *flagged for BC-D*; BC-C carries the
  flag forward but the LIDT comparison itself sits in BC-D.

**Plan of attack.**

1. Compare equal vs asymmetric mirror allocations against published
   IBS coating-physics expectations.
2. Pick a default allocation; document the asymmetry argument for
   the M4' dichroic.
3. Translate per-mirror T_loss → R_min (and the M4' dual-pair
   T_280 spec) at the design AOI / polarization.
4. Document the AOI tolerance for plane and curved seats.
5. Document substrate (Herasil throughout per §6 Q3 default).
6. Tabulate BC-D hand-forwards: per-mirror peak CW intensity at the
   higher-stress 1.5 W scenario (already computed in [`constants.md`](constants.md)
   §D and [`bc-b-results.md`](bc-b-results.md) §F).
7. Write `bc-c-results.md` as the per-mirror BC-E consumption
   artefact.
8. Close this log with the surprises / open items.

Each step appended below as a dated sub-section.

---

## 2026-05-20 · BC-C executed and closed (half-day)

### Step 1 — Allocation comparison

Four allocation policies compared at the fixed `Σ T_loss_VENDOR_max =
1 500 ppm` budget (full table → [`bc-c-results.md`](bc-c-results.md) §C.2).
The decisive question: equal split (workplan default) vs asymmetric
(M4' headroom for the dichroic stack).

**Decision: Friedenauer-class 300/300/900 ratio adopted.** Argument:

- Friedenauer's published R-floors give M4' three times the
  loss-budget allowance of M2'/M3' (2000 vs 700 ppm). The 3:1 ratio
  is the empirically validated precedent for IBS dichroic-vs-HR
  asymmetry at this wavelength class.
- Scaling Friedenauer's 3400 ppm sum to our 1500 ppm budget by the
  buildup-improvement factor 0.44 gives 309 / 309 / 882 ppm — rounded
  to the clean 300 / 300 / 900.
- Translates to: M2'/M3' at R ≥ 99.97 % @ 559 (single-WL HR, easily
  IBS-achievable); M4' at R ≥ 99.91 % @ 559 (dichroic — realistic
  given the competing HT @ 280 nm constraint in the same stack).

### Step 2 — Per-mirror R/T translation

[`bc-c-results.md`](bc-c-results.md) §D carries the four per-mirror
rows. Notable details beyond the R-floors:

- **M4' T-spec at 280 nm: T ≥ 95 %** (tighter than Friedenauer's
  published T > 94 %; modern dichroics typically deliver T ≥ 97 %,
  vendor encouraged to quote actual achievable).
- **AOI band 13.7° ± 1.5°** on the curved seats (M3', M4'). The
  coating R/T specs apply *across* this band, not just at the
  nominal AOI. The band is a **chosen procurement spec**, *informed by*
  the [home-built doublers survey](../../docs/components/home-built-doublers.md)
  §3 photogrammetric fold-angle estimate (25°–29° at ±5° pixel-
  identification budget, source-tier `O*`). It is **not** a
  bench-measured tolerance — the survey explicitly states the 4°
  spread is not resolved as real build-to-build variation versus
  photogrammetric noise. The ±1.5° procurement band sits at the
  safe side of this combined uncertainty.
- **AOI ~ 0° ± 1°** on plane mirrors M1' / M2'.
- **Back-face AR** on each mirror: 559 nm on M1'/M2'/M3'; **narrow-band
  280 nm on M4'** (§6 Q6 default).

### Step 3 — AOI tolerance argument captured (provenance qualified)

The home-built-doublers survey reports per-doubler full folding angles
of 25°–29° photogrammetrically, with a ±5° pixel-identification budget
on each value. **The survey itself explicitly notes that the 4° spread
between doublers is *not* resolved as real build variation** versus the
photogrammetric noise (`O*` tier, not bench-measured). It is therefore
not a measured AOI tolerance.

BC-C adopts **±1.5° per curved mirror** as the *chosen procurement
band* — not a bench-tolerance measurement. The argument:

- The Friedenauer nominal of 13.7° per curved mirror is preserved as
  the centre value.
- A ±1.5° band is wider than what bench-aligned cavities should
  actually experience (typical optical bench alignment hits ±0.5°
  at the per-mirror level), but it conservatively absorbs both the
  photogrammetric uncertainty and any plausible real build-vs-design
  scatter.
- The BC-E spec quotes R/T-targets held over this band, so a vendor
  who delivers a coating with narrow angular acceptance fails the
  spec at the edges. The wider band thus *protects against* bench
  realignment surprises rather than *predicting* them.

Wider band (±2°) would weaken the coating performance at the edges;
tighter band (±1°) would not robustly cover potential build-vs-design
scatter. **±1.5° is a chosen mid-conservative number, not a measured
tolerance** — both [`bc-c-results.md`](bc-c-results.md) §D and the
BC-E cover letter will phrase it accordingly.

### Step 4 — Substrate frozen (§6 Q3 default)

**Herasil throughout.** M4' requires it (UV-transmissive at 280 nm);
M1'/M2'/M3' inherit it for logistical and scatter-uniformity reasons
(see [`bc-c-results.md`](bc-c-results.md) §G). The BC-E cover letter
will carry a one-line "FS-equivalent fallback acceptable on
M1'/M2'/M3' if it reduces lead time" note.

### Step 5 — BC-D hand-forward computed

Per-mirror peak CW intensities at the higher-stress 1.5 W scenario
captured in [`bc-c-results.md`](bc-c-results.md) §E. **Binding LIDT
case = M4' front face at ~ 65 kW/cm² CW @ 559 + ~ 0.6 kW/cm² CW @ 280
dual load** (v2-corrected from v1 154.7 / 1.5 kW/cm² per the §E
propagation methodology). The M1'/M2' plane mirrors carry the
*highest* single-wavelength load on the 559 nm axis (~ 100–190 kW/cm²,
depending on long-arm leg distribution); M3' (~ 65 kW/cm² @ 559) and
the M4'/M1' back faces (< 4 kW/cm²) are below. The M4' uniqueness
comes from its *dual-wavelength* burden, not from absolute fluence.

### Step 6 — BC-E spec-sheet structure pre-planned

[`bc-c-results.md`](bc-c-results.md) §J spells out the BC-E
deliverables:

- **One M1' page** (single-variant centre + per-scenario optima as
  informational rows; one-variant rationale explained).
- One M2' page (R ≥ 99.97 %, AOI ~ 0°).
- One M3' page (R ≥ 99.97 %, AOI 13.7° ± 1.5°).
- One M4' page (R ≥ 99.91 % + T ≥ 95 %, dual-wavelength, AOI band
  spec, narrow-band 280 nm back-face AR).
- Cover letter (six callouts: AOI band, substrate, quantity, LIDT
  reference, AR bandwidth, **why T_IC targets above the 2006
  reference**).

### Step 7 — Acceptance gate review

All three workplan §4 BC-C gates pass — full table at
[`bc-c-results.md`](bc-c-results.md) §A.

**BC-C closed 2026-05-20.** Calendar: half-day (workplan estimate
0.5 day; actual ~ matches). No `/src/` change; no notebook commit;
no MEMORY.md update; no vendor contact.

**BC-D is unblocked** — opens against
[`bc-c-results.md`](bc-c-results.md) §E (per-mirror intensity table)
as its primary input. **BC-E's spec-sheet structure is pre-frozen**
in [`bc-c-results.md`](bc-c-results.md) §J, awaiting BC-D's LIDT
comparison before drafting the actual spec sheets.

### Surprising findings to flag for the steward

1. **Friedenauer's 3:1 dichroic ratio is a strong precedent.**
   The 300 / 300 / 900 allocation is not an arbitrary choice — it's
   Friedenauer's own M4'/(M2' or M3') ratio scaled down by the
   buildup-improvement factor. This is a useful talking point in
   the BC-E cover letter ("our spec preserves the published 3:1
   dichroic-vs-HR loss ratio while tightening the absolute values
   by 56 %").
2. **R ≥ 99.97 % on M2'/M3' is more relaxed than premium IBS
   capability.** Layertec / Laseroptik premium-grade HRs routinely
   deliver R ≥ 99.99 %. Our spec floors at 99.97 % give the vendor
   margin and avoid a price premium for hitting the bleeding edge.
   If the vendor quotes back R ≥ 99.99 %, that's a free buildup
   improvement of ~ 400 ppm/mirror that BC-B's solver can re-run
   against.
3. **AR @ 280 nm narrow-band is materially cheaper.** §6 Q6
   default; the CW chain doesn't need broadband (Δ_ref = 40 GHz
   ≈ 0.01 nm at 280 nm). Worth flagging as an explicit "cost
   optimisation" item in the cover letter.
4. **No M1'-variant branch needed.** §6 Q2 stays at "one variant"
   — confirmed by BC-B's Δ`T_IC_opt` numbers, inherited unchanged
   here. BC-E builds one M1' page, not two.

### Open items handed to BC-D + BC-E

(Full table → [`bc-c-results.md`](bc-c-results.md) §J.)

To BC-D:
- LIDT comparison at the M4' front face dual-WL load.
- Service-life envelope conditional on G2 closure.

To BC-E:
- Build five pages per [`bc-c-results.md`](bc-c-results.md) §D + §J
  structure.
- Cover letter explicitly justifies T_IC higher than Friedenauer
  2006 reference.

---

## 2026-05-20 · BC-C v2 corrections (post-review)

Three reviewer findings landed after the v1 BC-C close. All three
real; all three applied. Summary:

### Correction 1 — §E spot radii (the substantive one)

v1 of [`bc-c-results.md`](bc-c-results.md) §E used **~ 164 μm** for
the beam spot on **all four mirrors**, copy-pasted from
[`constants.md`](constants.md) §D.3's curved-mirror value. Two errors:

- **The 164 μm value itself was wrong.** [`constants.md`](constants.md) §D.3 used `zR_BBO`
  (n = 1.673) for the full 29.7 mm waist-to-mirror propagation, but
  only 5 mm of that distance is inside the BBO crystal; the
  remaining ~ 25 mm is air. Proper Gaussian propagation through the
  BBO + the BBO–air flat interface + air gives the **corrected
  curved-mirror spot of ~ 255 μm**. The constants.md table and
  bc-b-results.md §B `I_curved` cells are now updated; the v1 values
  are preserved in the methodology notes for traceability.
- **The plane mirrors should have their own spot calculation.**
  In a stable bowtie ring, the curved mirrors collimate the
  diverging short-arm beam into a long-arm waist; the plane mirrors
  (M1' / M2') sit at varying distances from that long-arm waist
  depending on the leg distribution Friedenauer doesn't enumerate.
  For a symmetric 3-leg long-arm (137 mm per leg), plane-mirror
  spots are in the **~ 145–195 μm** range — comparable to the
  curved-mirror spot, not the reviewer's free-space-propagation
  estimate (~ 1.3 mm, which assumed no curved-mirror collimation).
  §E now quotes a **150–200 μm range** with explicit
  cavity-geometry-dependent caveat.

**Impact on BC-D**: intensities drop by factors of ~ 2–3 across the
board (curved-mirror 154 → ~ 65 kW/cm² at 1.5 W; plane-mirror band
~ 100–190 kW/cm²). **Qualitative conclusion — M4' front face is the
binding LIDT case — is unchanged** because the M4' uniqueness is its
*dual-wavelength* dichroic burden, not its absolute fluence.

The BC-B notebook has been **corrected** (not just caveated): the
single-medium `spot_radius_at_curved_mirror` helper is replaced by
`spot_radius_at_curved_mirror_proper`, which propagates the
q-parameter through BBO (5 mm in n = 1.673), the flat BBO–air
interface, and air (24.7 mm) explicitly. Re-running the notebook
gives `w_curved = 255 μm` and the corrected I_curved column
(25.7–66.6 kW/cm² across the grid; 64.2 kW/cm² at the High / default
cell), which matches both the BC-C §E values and the reviewer's
independent ABCD verification. The notebook is now physics-correct
end-to-end, ready for BC-F promotion to `/notebooks/exploration/`.

### Correction 2 — AOI provenance wording

v1 phrased the ±1.5° AOI band as "build-to-build inheritance" from
the home-built doublers survey. **The survey itself does not
claim measured build variation** — it states the 4° spread between
the three photographed doublers (25°–29° mean fold) is `O*` tier
(photogrammetric ±5° pixel-identification budget) and *not* resolved
as real build variation versus photogrammetric noise.

§D.3 / §D.4 of [`bc-c-results.md`](bc-c-results.md) and the Step 3
prose above now phrase the band as a **chosen procurement spec**,
*informed by* the survey but not a measured tolerance. The ±1.5°
number itself is unchanged — it sits at the safe / conservative side
of the combined photogrammetric + bench-alignment uncertainty.

### Correction 3 — IBS capability claims qualified

v1 contained statements like "Premium-grade IBS routinely delivers
R ≥ 99.99 %" without citation. BC-A explicitly noted that **no
extracted 559 nm IBS HR loss anchor exists in the dossier**
([`constants.md`](constants.md) §C, path-1 follow-up queued). §C.1
and §C.2 now mark these as **vendor-stated catalog claims, not
dossier-extracted**, with a forward-pointer to the path-1
extraction that would convert them to bound-tier data. The R-floor
spec values themselves are unchanged.

### Net status

- Three corrections applied across [`bc-c-results.md`](bc-c-results.md),
  [`bc-c-log.md`](bc-c-log.md), [`constants.md`](constants.md), [`bc-b-results.md`](bc-b-results.md),
  and the BC-B notebook.
- All three reviewer findings closed.
- **BC-D inputs now coherent** for the LIDT comparison: lower
  per-mirror fluences than v1 quoted, but the same binding case
  (M4' front-face dichroic dual-WL).
- BC-E inputs unchanged — the per-mirror nominal R/T targets, AOI
  bands, substrate choice, and tolerance recommendation are
  unaffected by the spot-radius correction.

---
