# BBO coating-run inquiry — work program (DRAFT for deliberation)

**Steward:** Ulrich Warring
**Date opened:** 2026-05-20
**Status:** **DRAFT — for deliberation. No action taken; no notebooks committed; no vendor contact.**
**Folder:** [`logbook/2026-05-20-bbo-coating-run-wp/`](.)
**Companion folders (planned, not yet created):**
`specs/` (per-mirror coating spec sheets), `notebooks/` (impedance-match sweeps once the WP is endorsed).

---

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — the Phase 0.5 reference triple
  `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}`
  ([CHARTER §1.5](../../CHARTER.md)) is independent of BBO mirror coatings.
- **Affects Level 1 parameter?** no — the UV-power-at-experiment-input and
  source-linewidth budgets are unchanged. The two input-power scenarios
  considered here (0.5 W and 1.5 W at 559 nm into the BBO ring) **bracket the
  upstream LBO-output uncertainty**, not the §1.5 UV anchor itself: by
  Manley–Rowe, P_UV ≤ P_in_559, and at Friedenauer-class η_BBO ≈ 0.29 the
  two scenarios yield roughly **~ 0.15 W UV** (low anchor, well below the
  ≥ 500 mW indicative) and **~ 0.4–0.7 W UV** (high anchor, at or just
  above the indicative depending on the impedance-matched efficiency BC-B
  computes). This WP does not propose a new §1.5 anchor and does not
  *guarantee* delivery of 500 mW UV from either scenario — its scope is
  coatings, and the upstream LBO output is the binding determinant.
- **Affects success criterion?** no.

This WP therefore does **not** require Council-3 deliberation. It is **steward
exploration** in the sense of CHARTER §5.1: parameter optimisation on a
*frozen* (Friedenauer 2006 §D) cavity geometry, executed only through the
architecture-neutral primitives already in `/src/`. No new architecture-
family-specific code is introduced.

---

## 1 · Goal

Produce a **short list of optical components and their coating specifications**
for the 559 → 280 nm BBO ring cavity, at two design points — input powers of
**~ 500 mW** and **~ 1.5 W at 559 nm** into the BBO ring — with the rest of
the cavity geometry held identical to
[Friedenauer 2006 §D (BBO ring)](../../docs/components/friedenauer-baseline.md#d-bbo-ring-cavity-559-nm--near-280-nm).
The deliverable is a vendor-ready spec sheet per mirror, suitable for
inquiries to coating houses.

**Two scenarios because:** Friedenauer ran 0.95 W of 559 nm into the BBO ring
and obtained 0.275 W UV. The next-gen workplan
([`logbook/2026-05-08-next-gen-500mW-workplan.md`](../2026-05-08-next-gen-500mW-workplan.md))
explores raising the upstream LBO output; whatever 559 nm power that workplan
ends up recommending plausibly lies between ≈ 0.5 W (a conservative fall-back
if the LBO stage cannot be improved) and ≈ 1.5 W (a 1.5–1.6 × Friedenauer
push, plausible with a higher-power Yb pump and an impedance-rematched LBO).
The two scenarios therefore **bracket the upstream LBO-output uncertainty**,
not the §1.5 UV anchor itself — at Friedenauer-class BBO efficiency the
0.5 W scenario lands at ~ 150 mW UV (well below the ≥ 500 mW indicative)
and the 1.5 W scenario lands at ~ 400–700 mW UV (impedance-matched
efficiency rises with pump, so the upper anchor sits at or just above
the indicative). The 0.5 W scenario buys us a coating-run that still
works if the upstream stays at the Friedenauer baseline; the 1.5 W
scenario buys us a coating-run that does not waste buildup if the
upstream stretches.

**Optimal IC transmission for the BBO ring scales with input power** —
`T_IC_opt` *rises* with `P_in` because nonlinear depletion adds to the
round-trip loss the coupling must match. A coating designed at
`T_IC_opt(0.5 W)` therefore sits *too low* in transmission at 1.5 W,
leaving the cavity **under-coupled** (intrinsic + nonlinear loss exceeds
the coupling-port loss) and forfeiting buildup. This is why one coating
spec cannot serve both scenarios optimally — and why §6 Q2 holds the
M1' variant-count decision open until BC-B quantifies the gap.

**Reviewer-validated BC-A motivation.** Reverse-engineering Friedenauer's
published triangle (`P_in = 0.95 W`, `T_IC = 0.016`, `P_UV = 0.275 W`)
with the Phase-E-pinned γ via the exact forward model gives
`L_passive_PHE ≈ 1.1–1.5 %` (≈ 11 000–15 000 ppm; reviewer back-of-envelope,
BC-A pins the precise number), compared to the upper envelope on summed
mirror transmission loss from the §3 R-floors
(`L_mirror_T_at_spec_limit ≈ 3 400 ppm`). The ~ 3–4 × gap is exactly
the hazard BC-A is structured to surface — non-mirror passive loss
(crystal Brewster scatter, BBO bulk absorption at 559 nm, oven-window AR)
is substantial and must be folded into `L_passive_PHE` before any
vendor-facing T_IC number is quoted. Furthermore, at the same
`(L_passive_PHE, γ_SHG_BBO_PHE)`, the impedance-matched optimum
`T_IC_opt(0.95 W) ≈ 0.022` — *not* Friedenauer's 0.016. The published
`T_IC = 0.016` was the coating Friedenauer procured, not the optimum at
their γ; BC-B carries this distinction forward as a finding rather than
a check.

**Not the goal:**

- Not a re-optimisation of the cavity geometry (length, focal length, fold
  angle, crystal length, intracavity waist). Those are inherited verbatim
  from Friedenauer 2006 §D — this WP is *coatings-only*.
- Not a build commitment. Spec sheets are inputs to a future procurement
  decision (KD-UV280-005 / -007), not the decision itself.
- Not a Phase 4 architecture scoring exercise — G1 / G2 still gate that.
- Not a vendor-selection exercise. The same spec sheets will go to several
  coating houses; choosing among quotes is downstream.
- Not an LBO-stage coating exercise. The LBO stage has its own loss-budget
  questions ([NG-A in the next-gen WP](../2026-05-08-next-gen-500mW-workplan.md))
  and a separate inquiry would be opened if needed.

---

## 2 · Geometry held fixed (Friedenauer 2006 §D, paper-stated values + one Sellmeier-derived completion)

| Parameter | Value | Source |
|---|---|---|
| Cavity total length L_cav | 0.470 m | Friedenauer Table 1 |
| Folding angle (full) | 27.4° (13.7° per curved mirror) | Friedenauer §3 |
| Focusing-mirror focal length f | 25 mm (R = 50 mm, concave) | Friedenauer §3 |
| Focusing-mirror separation d' | 59.4 mm | Friedenauer Table 1 |
| Intracavity waist w0 at BBO centre | 19.4 μm (BK-optimum for L_BBO = 10 mm) | Friedenauer §3 |
| BBO crystal | Brewster-cut Type-I, 4 × 4 × 10 mm³ — dimensions and cut paper-stated; **θ = 44.4° is Sellmeier-derived, *not* Friedenauer-stated** (§D.3 of [`friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md#d3-bbo-crystal) flags the cut angle as OPEN; 44.4° comes from the Eimerl 1987 / Tamosauskas 2018 Type-I PM condition at 559 → 280 nm) | Friedenauer §3 (dimensions, cut); Eimerl 1987 / Tamosauskas 2018 (θ) |
| BBO oven set-point | ~ 50 °C (condensation prevention) | Friedenauer §3 |
| AOI at plane mirrors M1', M2' | ~ 0° (long-arm side) | Friedenauer §3 (implied by bowtie topology) |
| AOI at curved mirrors M3', M4' | 13.7° p-pol | Friedenauer §3 |

**Implication.** Walk-off, h_m (Boyd–Kleinman focusing factor), and γ_SHG are
held at their Friedenauer-validated values (Phase E cross-check: BBO stage
agrees to 1.5 %). Only `T_IC`, the curved-OC dichroic pair (R @ 559 / T @ 280),
the HR reflectivities, and the substrate / LIDT / surface-quality
requirements are *free*.

---

## 3 · The four mirrors (Friedenauer roles, restated)

The BBO ring is a four-mirror bowtie with two plane and two curved elements
([Friedenauer §D.1 components page](../../docs/components/friedenauer-baseline.md#d1-cavity-mirrors)):

| ID | Role | Friedenauer-stated coating | What this WP must specify |
|---|---|---|---|
| **M1'** | Plane input coupler | R = 0.984 @ 559 nm; AR on outside | `T_IC` at each design point + tolerance; AR @ 559 on outside; AOI 0°; substrate; LIDT @ 559 nm CW |
| **M2'** | Plane HR (piezo-mounted, HC servo seat) | R > 0.9993 @ 559 nm | R_HR ≥ R_min @ 559 nm (front coating); AOI 0°; substrate; LIDT @ 559 nm CW; flatness ≤ λ/10 @ 633 nm over the clear aperture (HC servo seat — flatness keeps the loaded-mount resonance reproducible across the run); back-face AR @ 559 nm |
| **M3'** | Curved HR (focusing) | R > 0.9993 @ 559 nm; concave R = 50 mm | R_HR ≥ R_min @ 559 nm; concave R = 50 mm; AOI 13.7° p-pol; substrate; LIDT at *intracavity* peak intensity |
| **M4'** | Curved output coupler (focusing dichroic) | R > 0.998 @ 559 nm + T > 0.94 @ 280 nm; concave R = 50 mm | R @ 559 + T @ 280 dichroic pair with tolerance, specified over a **chosen procurement band AOI = 13.7° ± Δθ** p-pol (Δθ working floor ≈ ±1.5° per mirror — *informed by* the [home-built doublers survey](../../docs/components/home-built-doublers.md) §3 photogrammetric fold-angle estimate of 25°–29° at ±5° pixel-budget; the survey itself does *not* resolve this as bench-measured build-to-build variation, so the procurement band sits at the conservative side of the combined photogrammetric + alignment uncertainty); back-face **AR @ 280 nm** ; UV-grade substrate (Herasil / SQ2); ROC = 50 mm with vendor-spec tolerance; clear aperture, wedge / centring per vendor template; surface figure over CA; **LIDT specified per surface** — front concave dichroic carries the dual-wavelength CW load (intracavity 559 nm + transmitted 280 nm); back planar AR carries 280 nm CW transmission only |

The "what this WP must specify" column is the WP deliverable.

---

## 4 · Phase plan

### Phase BC-A · Loss-model normalisation gate and constants freeze (~ 1 day)

**Why.** This is the **load-bearing phase** of the WP. Before any vendor-
facing number is trusted, the loss model must be normalised so that
Friedenauer's published triangle — `R_IC = 0.984` (`T_IC = 0.016`),
`P_in_559 = 0.95 W`, `P_UV = 0.275 W` — is reproducible at one self-
consistent set of (`L_passive`, `γ_SHG`) values. Conflating *passive
mirror+scatter loss*, *Phase-E inferred effective loss*, and *vendor-
achievable coating loss target* into a single `L_passive` symbol is the
single biggest way this WP can produce spec sheets that quote the wrong
T_IC. BC-A separates the three rows explicitly and forces every downstream
phase to cite which row it is using.

**Deliverable A — geometry and material constants table.**
A markdown table (`constants.md` in this folder) transcribing every
Friedenauer §D geometry constant used downstream (the §2 rows above) plus
the material constants the impedance-match analysis consumes:

- `d_eff` for BBO at 559 → 280 nm (Eckardt 1990, sense convention noted).
- Walk-off ρ at the Type-I PM angle (Eimerl 1987 with Tamosauskas 2018 as
  the second-set cross-check, per the Sellmeier dossier).
- Refractive indices `n_o(559)`, `n_e(280)` (same two-set pair).
- `γ_SHG_BBO` for the Friedenauer geometry — **pinned with provenance**:
  numerical value (the Phase E result, ≈ 1.49 × 10⁻⁴ W⁻¹ subject to BC-A
  re-extraction), the Phase E notebook path
  ([`notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py)),
  the 1.5 % validation residual against published Friedenauer BBO output,
  and the date of the validation run. **`constants.md` is the sole γ
  authority for this WP** — BC-B consumes γ from this table and does
  *not* re-derive it. If a future iteration of the dossier updates γ
  (Sellmeier refresh, Eckardt re-extraction, …), the update lands in
  `constants.md` first and BC-B is re-run.

**Deliverable B — three-row `L_passive` separation.**
A second table that explicitly distinguishes:

| Row | Symbol | Definition | Value at Friedenauer 0.95 W / 0.984 R_IC corner | Source |
|---|---|---|---|---|
| **B.1** Maximum mirror-transmission loss permitted by the Friedenauer R-specs | `L_mirror_T_at_spec_limit` | Sum over the three non-IC mirrors of (1 − R_min_spec): (1 − 0.9993) + (1 − 0.9993) + (1 − 0.998) ≈ 3 400 ppm — the **upper envelope** on summed mirror transmission loss *if every mirror sat exactly at the published R-floor*. Actual R may be higher → actual T-loss may be lower. Does **not** include crystal Brewster scatter, BBO bulk absorption at 559 nm, oven-window AR, or other non-mirror passive contributions. | ≤ 3 400 ppm (upper envelope on mirror-T contribution only) | Friedenauer Table 1 R-values, stated as **lower bounds** ("> 0.998", "> 0.9993") |
| **B.2** Phase-E-inferred round-trip passive loss | `L_passive_PHE` | The round-trip passive loss the Phase E solver requires (at the BC-A-pinned `γ_SHG_BBO_PHE`) to reproduce **`P_UV = 0.275 W`** at Friedenauer's published `(P_in = 0.95 W, T_IC = 0.016)`. Reviewer back-of-envelope at WP opening: **`L_passive_PHE ≈ 1.5 %` (≈ 15 000 ppm)** — to be pinned to ≤ 5 % residual by BC-A's re-run of the Phase E notebook. This includes everything the cavity sees except the IC: mirror T-loss + crystal Brewster scatter + BBO bulk absorption + oven-window AR + scatter floors. | ≈ 15 000 ppm (pin precisely in BC-A) | [Phase E notebook](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py) |
| **B.3** Vendor-achievable coating-loss **ceiling** (= upper bound on per-mirror T-loss) | `T_loss_VENDOR_max` (per mirror) | The **maximum** allowable per-mirror transmission loss the vendor must commit to deliver across the M2'/M3'/M4' set at the design AOI and polarization. BC-B sizes the cavity loss budget on the **summed** vendor-ceiling value; lower achieved loss shifts `T_IC_opt` and is recomputed (not ignored). | **OPEN at WP opening** — the dossier carries no IBS HR coating-loss anchor at 559 nm (see "Literature gap" below); BC-A closes this | — |

**The point.** B.1 (upper envelope from the published R-floors) and B.2
(Phase-E-inferred actual operating loss) must be compared. At the
Friedenauer corner with the Phase-E γ pinned, **B.2 ≫ B.1** is expected
(reviewer back-of-envelope: ~ 15 000 ppm vs ~ 3 400 ppm, a ~ 4 × gap).
The gap is the **non-mirror passive loss budget** (crystal Brewster
scatter, BBO bulk absorption at 559 nm, oven-window AR, …) plus the
fact that Friedenauer's R-specs are lower bounds (actual mirrors may
have R higher than the spec floor — *reducing* B.1's contribution and
*increasing* the implied non-mirror share of B.2). BC-A surfaces this
gap explicitly so the downstream impedance match in BC-B operates on
**B.2 (`L_passive_PHE`)** as the binding loss, not on B.1.

**Vendor spec direction (corrected).** The vendor R-spec (sheet generated
in BC-E) requires per-mirror transmission **no worse than** a maximum
`T_loss_VENDOR_max` — equivalently, R **no lower than** a minimum
`R_VENDOR_min`. Lower vendor-delivered loss is *good for buildup* but is
**not** a free win: it shifts the impedance match, so BC-B recomputes
`T_IC_opt` for whatever loss the vendor commits to. The BC-E sheet
therefore states the R-spec as a minimum (with optional finer-grade
upgrade language) and the impedance-match table in BC-B carries
`T_IC_opt(L_total)` evaluated at both the ceiling and the
vendor-committed loss point.

**Deliverable C — literature gap call (anti-seeding-clean).**
The reviews of the v0 draft surfaced that the v0 BC-A citations were
wrong: `Tamosauskas2018` in this repo is the BBO Sellmeier reference,
not an IBS HR coating-loss source; `Burkley2021` is deep-UV cavity-
mirror lifetime in UHV at ~244 nm and remains `SCAFFOLD` (no numerical
extraction); `Brown2019` is 1070 nm CW contamination-driven breakdown
(mechanism portable, thresholds not). The dossier therefore carries **no
explicit IBS HR coating-loss anchor at 559 nm** as of 2026-05-20. BC-A
closes this gap in one of two admissible ways (vendor pre-inquiry is *not* admissible inside this WP; see the boundary statement after path 2):

1. **Targeted literature pass** — scout for an explicit IBS HR
   coating-loss numerical anchor in the visible (Layertec / Laseroptik
   measured-loss publications, ATFilms / MLD measured-loss papers,
   Tamosauskas-group or related). Promote to `data/literature/<key>/`
   with the standard `extracted.yaml + notes.md` pair. **Preferred path.**
2. **Phase-E-anchored only** — split `L_passive_PHE` into its mirror and
   non-mirror contributions, hold the non-mirror part fixed in the new
   build, and let the vendor mirror-ceiling carry the headroom (if any):
   - `L_nonmirror_PHE ≡ L_passive_PHE − L_mirror_T_at_spec_limit`
     (≈ 15 000 − 3 400 ≈ 11 600 ppm at WP opening; BC-A pins precisely).
     Holding `L_nonmirror_PHE` constant assumes the new build inherits
     Friedenauer's crystal Brewster scatter + BBO bulk absorption +
     oven-window AR + scatter floors. Reasonable for a same-vendor,
     same-cut crystal class (Raicol 2025 inherits Friedenauer's BBO
     geometry; oven and Brewster faces unchanged).
   - `T_loss_VENDOR_max` (per mirror, the BC-E spec target) is then
     declared at or *below* the Friedenauer mirror-T spec-limit
     (≤ ~ 1 100 ppm per mirror, summed to ≤ ~ 3 400 ppm), giving
     a new-build operating loss `L_total = L_nonmirror_PHE +
     Σ T_loss_VENDOR_max` that is at most Friedenauer-class and
     potentially tighter if the vendor commits to better than the
     spec-limit. BC-B sweeps `T_IC_opt(L_total)` over the vendor-ceiling
     grid. **Fallback if path 1 returns empty.** Honest baseline; leaves
     buildup headroom *only* on the mirror axis (the non-mirror axis is
     inherited from Friedenauer and not improvable without crystal /
     oven re-engineering, which is out of WP scope).

**Not admissible at this WP-internal phase: vendor contact.** A vendor
pre-inquiry is an external action that belongs to a separate
procurement KD (KD-UV280-005 / -007); it cannot run inside BC-A without
violating the §9 acceptance criterion that **no vendor inquiry is sent
during this WP**. If path 1 returns empty and path 2 is judged
insufficient by the steward at BC-F closure, the WP closes with a
"vendor pre-inquiry recommended" follow-up handed to the procurement KD.

The chosen path is logged in `constants.md` under "Loss-anchor evidence
pass." This is the gate BC-B must wait for.

**Deliverable D — circulating-power and peak-intensity envelope.**
For each (scenario, `L_total_VENDOR_grid` candidate, where
`L_total = L_nonmirror_PHE + Σ T_loss_VENDOR_max` per the path-2
decomposition above), a back-of-envelope
table of:

- Circulating 559 nm power inside the BBO ring at the impedance-matched
  point.
- Peak CW intensity at the BBO crystal waist (w₀ = 19.4 μm at 559 nm).
- Peak CW intensity on the curved-mirror coatings (M3' / M4', evaluated
  at the focal beam-radius on the coating surface).
- Outgoing 280 nm CW intensity through the M4' substrate.

This is the row the steward needs to see *before* deliberating §6 Q1 (the
0.5 / 1.5 W pair): at impedance-matched T_IC, 1.5 W input could circulate
~ 50–150 W of 559 nm through a 19.4 μm waist (rough back-of-envelope, to
be pinned by BC-A), giving multi-MW/cm² CW intensities at the BBO faces.
Whether that is benign or hazardous is what BC-D quantifies; whether the
steward wants the WP to design at that intensity is what §6 Q1 asks.

**Deliverable E — NG-D geometry-sweep consistency check.**
A one-paragraph note confirming that
[NG-D](../2026-05-08-next-gen-500mW-workplan.md) (the crystal-geometry
sweep in the parent next-gen workplan) **has not concluded that
deviating from Friedenauer's (`L_BBO = 10 mm`, `w₀ = 19.4 μm`,
`f = 25 mm`) buys efficiency outweighing the cost of re-quoting these
coatings at a different curvature.** NG-D's status at WP opening is
"⏳ pending NG-A" — i.e., the sweep has not been run. The note records
this and commits BC-A to re-checking at BC-F closure; if NG-D lands in
the interim and recommends a different `f`, this WP pauses at BC-F until
the recommendation is reconciled.

**Acceptance.**
- `constants.md` exists, with the geometry, material, three-row
  `L_passive`, intensity envelope, and NG-D consistency check.
- The loss-anchor evidence pass has chosen one of paths 1 / 2 above
  (vendor pre-inquiry is explicitly inadmissible inside this WP) and
  recorded the choice.
- `L_passive_PHE` is extracted from Phase E and pinned to a number with
  an uncertainty band, **not** carried forward as a symbol.
- No code committed yet.

**Effort.** ~ 1 day (was 0.5 day in v0; the loss-model normalisation gate
and the literature pass make it a full day).

### Phase BC-B · Impedance match per scenario (~ 1 day)

**Why.** Generate the per-scenario `T_IC_opt` at the BBO IC, plus the UV
output and the sensitivity envelopes used by BC-C / BC-E.

**Unit convention used throughout BC-B (and the rest of the WP).**
Reflectivities and transmissions are stated as fractions (1 = 100 %).
**`pp` means *percentage points absolute*** — `T_IC ± 0.5 pp` is
`T_IC ± 0.005` in fractional units, i.e. `± 5000 ppm`. Where a sensitivity
bracket needs sub-percentage-point resolution it is stated in `ppm`
explicitly. The vendor spec sheets in BC-E quote the tolerance in `ppm`
(coating-house native unit), with the percentage-point equivalent in
parentheses.

**Deliverables.**
- One exploration notebook, `notebooks/2026-05-MM-bbo-ic-impedance-match.py`
  inside this folder (kept local until WP closes; promoted to
  `/notebooks/exploration/` at BC-F closure, with a cross-link added to
  `notebooks/README.md` and `docs/components/friedenauer-baseline.md` at
  closure so future readers can find the authoritative `γ_SHG_BBO` value
  the WP rests on — addresses reviewer-flagged discoverability question B).
- Direct call to `enhancement_cavity.optimal_input_coupler` (already in
  `/src/`, exact `−L · η_nl` cross term; depleted-regime solver) using the
  `γ_SHG_BBO` value **pinned in BC-A's `constants.md`** — *not* re-derived
  inside BC-B.
- For each (`P_in_559`, `L_total_VENDOR_grid`) point of the BC-A grid
  (where `L_total = L_nonmirror_PHE + Σ T_loss_VENDOR_max` is the
  total round-trip passive loss the cavity actually sees):
  - `T_IC_opt` (the BBO-stage IC transmission, in `ppm` and percentage
    points)
  - Circulating 559 nm power and peak intensity at the BBO waist
  - UV output at 280 nm
  - **Two sensitivity columns:**
    - *Manufacturing tolerance.* UV-output drop when `T_IC` lands at
      `T_IC_opt ± 0.5 pp` **and at `T_IC_opt ± 1.0 pp`** — the wider
      bracket catches the realistic IBS coating-run repeatability flagged
      by reviewers (typical batch-to-batch drift can be 1–2 pp absolute
      depending on vendor metrology).
    - *Physics tolerance.* UV-output drop when `γ_SHG_BBO` is ±1.5 % off
      the BC-A pinned value (the Phase E validation residual). Reporting
      both columns prevents BC-C from over-specifying the manufacturing
      tolerance against a physics uncertainty of comparable size.

**Acceptance.**
1. **Forward cross-check (the binding test).** At Friedenauer's published
   operating point (`P_in_559 = 0.95 W`, `T_IC = 0.016`) with the BC-A-
   pinned `(L_passive_PHE, γ_SHG_BBO_PHE)` constants, the notebook
   reproduces the published `P_UV = 0.275 W` **within 5 %**. This is a
   one-equation cross-check on the forward model; it fixes `L_passive_PHE`
   (the row B.2 value) jointly with the pinned γ.
2. **Optimum-finding (reported, not pass/fail).** At the same
   `(L_passive_PHE, γ_SHG_BBO_PHE)`, the notebook *also* reports
   `T_IC_opt(0.95 W)` — the impedance-matched IC transmission. Reviewer
   back-of-envelope expects this ≈ 0.022 (not 0.016), exposing that
   **Friedenauer ran slightly below the impedance-matched optimum** at
   the published `T_IC = 0.016`. This is a finding to surface in BC-A's
   `constants.md`, not a pass/fail check on BC-B — Friedenauer ordered the
   closest available coating, not necessarily the optimum at their γ.
3. A 2 × {however-many `T_loss_VENDOR_max` points BC-A chose} table of
   `T_IC_opt` and `P_UV` with the two sensitivity columns (manufacturing
   tolerance ±0.5 pp / ±1.0 pp, physics tolerance ±1.5 % on γ), evaluated
   at both the vendor-ceiling loss and a representative vendor-committed
   lower loss (per Finding 3 sign correction). Suitable for BC-C consumption.

### Phase BC-C · Translate to per-mirror coating targets (~ 0.5 day)

**Why.** A spec sheet is per *mirror*, not per *cavity*. This phase converts
the impedance-match result (`T_IC`, `L_total_VENDOR_grid` and its mirror
allocation Σ`T_loss_VENDOR_max`) into per-mirror reflectivity targets.

**Scenario-dependence note.** Only the **M1' IC reflectivity is scenario-
dependent at the nominal-target level** — `T_IC_opt(0.5 W) ≠ T_IC_opt(1.5 W)`.
The nominal **R-targets for M2' / M3' / M4' are scenario-independent**
(they are all HR / dichroic, not impedance-matched), but their
**LIDT margins, coating-absorption tolerance, and the M4' dual-wavelength
load are scenario-dependent** and must be **worst-case-specified across
the two scenarios** in BC-D. The BC-C deliverable separates these two
classes so the spec sheets in BC-E carry one column for the M1' R-target
per scenario and one (worst-case) column for the M2'/M3'/M4' LIDT.

**Deliverables.**
- Per-mirror passive-loss allocation. Given the BC-A
  Σ`T_loss_VENDOR_max` mirror budget (the mirror-only share of
  `L_total_VENDOR_grid`), allocate the per-mirror ceiling across
  M2' / M3' / M4' so that the per-mirror R-spec is well-defined. Default
  split: equal per-mirror allocation, unless BC-A's literature pass
  recommends otherwise (e.g. M4' dichroic typically delivers higher
  loss than a single-wavelength HR, so the default allocation may need
  asymmetric weighting).
- Curved OC (M4') dichroic table: R @ 559 nm + T @ 280 nm + back-face AR
  @ 280 nm, all specified over a **chosen procurement band AOI =
  13.7° ± Δθ p-pol** with Δθ working floor ≈ ±1.5° per mirror. The band
  is *informed by* the home-built-doublers
  [survey](../../docs/components/home-built-doublers.md) §3 (25°–29°
  photogrammetric mean folds at ±5° pixel-identification budget,
  source-tier `O*`), but the survey explicitly does *not* resolve
  the spread as bench-measured build-to-build variation — the
  procurement band is therefore a conservative choice, not a measured
  tolerance. The Friedenauer "T > 0.94 @ 280 nm" is a *floor*, not a
  spec; the BC-E sheet quotes the vendor-achievable T as the spec
  with a tolerance band.
- Polarization and AOI annotations per mirror — p-pol at 13.7° for the
  curved seats, 0° at the plane seats; coatings designed for the wrong AOI
  will read off-spec at the design AOI.

**Acceptance.** A per-mirror table: one row per mirror, with:
- *nominal-target columns* — R_target (or T_target), AOI, polarization,
  tolerance band — **one column for each scenario on M1'**, and a
  scenario-independent column on M2' / M3' / M4'; and
- *worst-case columns* — LIDT requirement, coating-absorption ceiling,
  M4' dual-wavelength load — taken at the higher-stress scenario (1.5 W
  at WP opening, subject to §6 Q1).

### Phase BC-D · LIDT and substrate constraints (~ 0.5 day)

**Why.** A coating spec without a fluence margin is a coating spec without a
service life. Fold in the intracavity peak fluence and the published
CW LIDT envelopes.

**Deliverables.**
- Per-mirror peak CW intensity at the design point (highest in each
  scenario): plane intensities at M1' / M2', focused intensities at M3' / M4',
  per-surface for M4' (front concave dichroic vs back planar AR). The
  back-of-envelope values from BC-A Deliverable D feed directly into this row.
- Comparison to published CW LIDT envelopes at 559 nm and at 280 nm using
  the *honest* dossier state:
  - [`Burkley2021`](../../data/literature/Burkley2021/notes.md) — deep-UV
    cavity-mirror lifetime in UHV, oxide vs fluoride coatings at ~ 244 nm
    (closest published wavelength to 280 nm; status `SCAFFOLD`, numerical
    extraction OPEN — BC-D triggers the extraction if the 1.5 W scenario
    sits close to the survival envelope).
  - [`Brown2019`](../../data/literature/Brown2019/notes.md) — CW
    contamination-driven breakdown at 1070 nm (mechanism + bandgap scaling
    portable, **absolute thresholds not transferable** to 280 nm; used here
    to argue silica > alumina > hafnia > tantala material ranking on the
    M4' dichroic).
  - [`Turcicova2022`](../../data/literature/) and any post-2020 UV-LIDT
    paper confirmed in the dossier.
  - **Not used:** `Tamosauskas2018` (BBO Sellmeier reference, *not* an
    IBS coating-loss / LIDT source — correcting the mis-citation in the v0
    draft of this WP).
- Substrate requirements: UV-grade (Herasil / SQ2) is **mandatory** for M4'
  (the curved OC) because 280 nm passes through it; the M1' / M2' / M3' seats
  see only 559 nm and could in principle use ordinary FS, but a uniform
  UV-grade choice is recommended for stray-light and procurement
  homogeneity.
- Surface quality envelope (scratch / dig ≤ 10/5 for cavity-grade) and
  flatness (≤ λ/10 @ 633 nm) — vendor-standard, but the spec sheet must
  state them.

**Acceptance.** A LIDT-and-substrate paragraph per mirror, attached to the
BC-C row. Scenarios that exceed published LIDT margins are flagged and
either de-rated, or referred back to the steward.

### Phase BC-E · Spec-sheet drafting (~ 1 day)

**Why.** A coating-house inquiry needs one page per mirror, structured the
way coating houses read it.

**Deliverables (inside `specs/`):**
- `M1-input-coupler.md` — one page; one column per scenario.
- `M2-plane-HR.md` — one page.
- `M3-curved-HR.md` — one page (R = 50 mm; AOI 13.7° p-pol).
- `M4-curved-OC-dichroic.md` — one page; the most differentiated of the four.
- `coating-run-cover-letter.md` — a one-page summary tying the four mirrors
  to the BBO ring application (CW 559 → 280 nm SHG, Friedenauer-2006
  geometry, two power scenarios, target lifetime, environmental conditions).

Per page (template):

```
Element ID / role           : M{n}' (Friedenauer-2006 BBO ring, role X)
Substrate                   : <material>, Ø 12.7 × 6.35 mm
Geometry                    : plane / concave ROC = 50 mm
ROC tolerance (curved only) : ± <vendor-spec> mm (M3' / M4' only)
Clear aperture              : ≥ <N> mm (centred; coating + flatness valid over CA)
Wedge / parallelism         : ≤ <vendor-spec> arcmin (plane); centring spec
                              for curved (decentre of optical axis vs mechanical)
Surface figure              : ≤ λ/10 @ 633 nm peak-to-valley over CA
                              (curved seats: irregularity over CA, not just centre)
Coating wavelength(s)       : 559 nm and (M4' only) 280 nm
AOI                         : 0° (plane) / 13.7° ± 1.5° p-pol (curved)
Reflectivity / transmission : R_target ± Δ (ppm) at <λ, AOI, pol>
                              (M4' also: T_target ± Δ at 280 nm + AR on back)
LIDT (CW)                   : ≥ <value> W/cm² at <λ>, 1/e²; specified
                              per surface for M4' (front dichroic vs back AR)
Surface quality             : scratch/dig ≤ 10/5
Flatness                    : ≤ λ/10 @ 633 nm
Quantity                    : <N> pcs per variant per coating run + <M> spares
                              (explicit: "per variant" if the M1' sheet
                              names two scenarios; "total across variants"
                              otherwise — cover-letter restates the
                              quantity math so the vendor cannot misread)
Notes                       : two scenarios at the same coating run
                              (or two separate runs if R-bands do not overlap)
```

**Acceptance.** Five short pages under `specs/` that a coating-house engineer
can read in 5 min, with explicit tolerance bands and LIDT margins. The
cover letter explains why two scenarios exist and how the vendor should
respond (one run that hits both within tolerance, or a price-per-run for
each).

### Phase BC-F · Steward review and freeze (~ 0.5 day)

**Why.** Spec sheets get *one* round of review with the steward (and any
co-investigator on the BBO ring) before they are sent. Coating runs are
expensive; mid-quote revisions burn vendor goodwill.

**Deliverables.**
- A closure entry in this folder (`closure.md`) recording the frozen specs,
  the open items deferred to vendor-quote time (e.g. exact bandwidth
  achievable at the design AOI), and the next decision gate
  (KD-UV280-005 / -007 procurement).
- Cross-links added to
  [`docs/components/inventory.md`](../../docs/components/inventory.md) and
  [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md)
  pointing at the new spec sheets.

**Acceptance.** Steward sign-off on the spec sheets. **This WP closes here.**
The act of *sending* the inquiry to a vendor is a separate decision (and
arguably belongs to a procurement KD), not part of this WP.

---

## 5 · Effort sketch

| Phase | Deliverable | Effort | Dependencies |
|---|---|---|---|
| BC-A | Loss-model normalisation gate + constants freeze | **1 day** (was 0.5; loss-anchor literature pass + γ pinning) | none |
| BC-B | Impedance-match sweep (notebook) | 1 day | BC-A |
| BC-C | Per-mirror coating targets | 0.5 day | BC-B |
| BC-D | LIDT + substrate constraints | 0.5 day | BC-A |
| BC-E | Spec-sheet drafting | 1 day | BC-C, BC-D |
| BC-F | Review + freeze | 0.5 day | BC-E |
| **Total** | | **~ 4.5 days focused** | |

Realistic calendar window: **one week** with normal task-switching overhead.
If BC-A's path-1 literature pass requires promoting a new
`data/literature/<key>/` entry (extracted.yaml + notes.md), add ~ 0.5 day.
Vendor pre-inquiry is not admissible inside this WP and therefore does
not contribute to the calendar.

---

## 6 · Open design questions for steward decision (eight; Q1–Q6 want answers before BC-A starts, Q7–Q8 can be deferred to BC-F closure)

1. **The two input-power points.** Are 0.5 W and 1.5 W the right pair, or
   should the upper anchor sit higher (2 W) or lower (1.2 W)? The choice
   determines whether one coating run can serve both scenarios within
   tolerance, or whether two runs are needed. BC-A Deliverable D pre-
   computes the circulating-power and peak-intensity envelope so this
   question can be deliberated in physical terms (multi-MW/cm² CW at the
   crystal faces, vs published LIDT) rather than abstract power numbers.
2. **One coating run or two? (Revised default.)** Only the nominal M1'
   R-target is scenario-dependent; M2'/M3'/M4' nominal R/T-targets are
   not. **Default path: hold the M1' spec at a single variant and
   re-decide after BC-B** based on whether `T_IC_opt(0.5 W)` and
   `T_IC_opt(1.5 W)` separate by more than ~ 1 pp (i.e., more than a
   typical single coating-run tolerance). If they do, branch to two M1'
   variants in BC-C; if they don't, the same M1' coating serves both
   scenarios at non-optimal but acceptable buildup on whichever scenario
   isn't the centre point. This default is more resource-efficient than
   committing to two variants up front; the worst-case-two-variants path
   remains the fallback if the steward wants to insure against the
   branch.
3. **Substrate uniformity.** Use Herasil throughout (slightly costlier on
   M1'/M2'/M3' but simplifies procurement and prevents bench mix-ups),
   or split substrates by role (FS for the 559-only mirrors, Herasil
   only for M4')? Default recommendation: **uniform Herasil**, on the
   logistic-simplicity argument from reviewer #2.
4. **Coating-house shortlist.** Out of scope of this WP — the spec sheet
   will be addressed to several houses (Laseroptik, Layertec, MLD, ATFilms,
   Manx Precision Optics, and any house the steward names). Naming the
   shortlist is a procurement-KD task.
5. **Spare quantity.** Coating runs amortise across quantity (chamber
   setup, not substrate, dominates cost). **Quantity is *per mirror role* —
   N pieces of M1' + N pieces of M2' + N pieces of M3' + N pieces of M4'
   yields N full build-sets, not N pieces total.** Reviewer-flagged math
   in v1 was contradictory ("N = 8 = one full set for the build, one full
   set as forward stock" is internally inconsistent — N = 8 per role
   gives 8 full sets, vastly over-stocking). **Default recommendation:
   N = 4 pieces per role**, yielding **4 full sets** — one for the
   build, three as forward stock against coating-run rejections,
   build-time damage, and a future replacement cycle. This is the
   customary spare-stock convention for cavity-grade IBS runs. N = 2
   (only one spare set) is too tight given that a single defective piece
   blocks the build; N = 6 is admissible if the steward wants extra
   margin against batch attrition. **Conditioning on Q2:** if the M1'
   sheet ends up specifying two variants (Q2 branch), the M1' page reads
   "N = 4 *per variant* (8 pieces of M1' total)"; the M2'/M3'/M4' pages
   stay at "N = 4 (single variant)". The cover-letter restates the math
   explicitly so the vendor cannot misread quantity-per-page as
   quantity-total.
6. **AR @ 280 nm on the M4' back face — single-band or broadband?** Friedenauer
   leaves this open. A narrow-band AR is easier to spec and cheaper; a
   broadband 250–300 nm AR costs more but tolerates source drift. Default
   recommendation: **narrow-band, centred at 280 nm** — the CW chain is
   locked at `Δ_ref = 40 GHz` and does not share these components with
   the pulsed-Raman alternative (reviewer #2 point).
7. **Is the 1.5 W scenario aspirational or binding?** (Reviewer #3 point.)
   If the upstream LBO next-gen WP later recommends an intermediate
   value such as 1.0 W, BC-B can interpolate, but the 1.0 W point will
   operate off the M1' R-optimum. Steward decision: are 0.5 W / 1.5 W
   the two coating-run scenarios *committed*, or should BC-A add a
   third anchor at 1.0 W to give the vendor a three-point R-target band
   for the M1' page? Default recommendation: keep the two-point pair
   and treat any intermediate operating point as an interpolation that
   sacrifices ≤ X % of buildup (X to be quantified by BC-B).
8. **BC-B notebook discoverability after closure.** (Reviewer #3 point B.)
   `γ_SHG_BBO` itself is **not** recomputed by BC-B — `constants.md`
   inside this folder is the sole γ authority for the WP, pinned in
   BC-A from the Phase E result. The BC-B notebook is the only place the
   **impedance-match arithmetic that consumes γ** is exercised
   end-to-end for the two scenarios. At BC-F closure the notebook is
   promoted from this folder to `/notebooks/exploration/`. A
   back-reference from
   [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md)
   §D.6 and from `notebooks/README.md` is added at the same time so
   future readers can find both `constants.md` (the γ authority) and the
   notebook (the impedance-match arithmetic that depends on it). Steward
   sign-off needed on the closure cross-link list (i.e., "any additional
   surfaces that should also carry a back-reference?").

---

## 7 · Charter compliance and gate inheritance

- **§1.5 Levels 0 / 1 untouched.** The two scenarios bracket **the
  upstream LBO-output uncertainty**, not the §1.5 ≥ 500 mW UV anchor —
  by Manley–Rowe, `P_UV ≤ P_in_559`, so the 0.5 W scenario lands well
  below the §1.5 indicative and the 1.5 W scenario lands at or just
  above it (impedance-matched efficiency dependent; BC-B quantifies).
  This WP does not propose a new §1.5 anchor and does not guarantee
  500 mW UV delivery from either scenario. The binding Level-0 row
  (`Ω_R`, Δ, `S_φ(f)`) is unaffected.
- **§5.1 anti-seeding.** All BC-B work uses architecture-neutral primitives
  in `/src/` (`enhancement_cavity.optimal_input_coupler`,
  `shg_single_pass.gamma_shg_coefficient`). No architecture-specific
  preset, no new constant in `/src/parameters.py`. Notebook lives inside
  this WP folder during the draft and is promoted to
  `/notebooks/exploration/` at BC-F closure. The mechanical scan in
  [`tests/test_anti_seeding_src_imports.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/tests/test_anti_seeding_src_imports.py)
  must continue to pass.
- **G1 inheritance.** The 14 GHz unlockable domain (Friedenauer §4) is
  inherited from the Friedenauer **crystal choice and cavity geometry**,
  *not* introduced by the coating choices. (Friedenauer §4 attributes the
  anomaly to crystals from Crystals of Siberia at the §3 geometry; the
  on-shelf Raicol 2025 / A-Star 2017 stock breaks the crystal-provenance
  link but inherits the geometry.) This WP does not advance or close G1.
  The spec sheets carry a one-line note that the BBO ring inherits this
  anomaly from the reference architecture.
- **G2 inheritance.** UV-induced degradation rates at 280 nm are
  uncharacterised (G2 still OPEN). BC-D therefore uses *published* CW LIDT
  envelopes plus a conservative margin; spec sheets carry a note that
  service-life claims are pending G2 closure.
- **G3 unaffected.** The reference triple is independent of mirror coatings.
- **Coastline / Sail.** This WP is *Sail* — exploratory parameter
  optimisation on a chosen architecture. The Friedenauer-geometry constants
  used as inputs are *Coastline* (anchored to a published source). The
  spec sheets are advisory until vendor quotes return and a procurement KD
  closes.

---

## 8 · Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| BC-B forward cross-check fails — `P_UV` at Friedenauer's published `(P_in, T_IC)` deviates > 5 % from 0.275 W at the BC-A-pinned `(L_passive_PHE, γ_SHG_BBO_PHE)` | Low | Phase E already validates the BBO model to 1.5 %; the corner cross-check is a one-equation forward test, not a joint constraint on `T_IC_opt`. Failure pauses BC-B for re-extraction of either `L_passive_PHE` (the joint variable BC-A fits) or γ (which would update `constants.md` first); not for sweep work on a corrupted baseline |
| `T_IC_opt(0.95 W, L_passive_PHE, γ_PHE)` differs from Friedenauer's published 0.016 by more than the ±0.5 pp coating tolerance | **Expected** (reviewer back-of-envelope: T_IC_opt ≈ 0.022) | Not a failure mode — surfaces that Friedenauer ran below the impedance-matched optimum. BC-A's `constants.md` records the gap; BC-C uses BC-B's T_IC_opt as the spec target, *not* the Friedenauer published value |
| The 1.5 W scenario exceeds CW LIDT on the curved OC | Medium | BC-D flags this; spec sheet either de-rates to a lower UV target or specifies a higher-LIDT coating run (longer schedule, higher cost) |
| Single coating run cannot meet both M1' impedance targets within tolerance | Medium | BC-C explicitly handles this branch — produce two M1' variants in the spec sheet; vendor quotes one run with two coatings |
| LBO-stage upstream output never reaches 1.5 W of 559 nm | Medium | The 0.5 W scenario provides the fall-back coating spec; the 1.5 W spec stays on-shelf until upstream NG workplan converges |
| Vendor metrology drift on `T_IC` exceeds the buildup-tolerant band | Low at ±0.5 pp (= ±5000 ppm; very loose); higher at the ±500–1000 ppm regime where IBS metrology is actually challenged | BC-B reports UV-output sensitivity at both ±0.5 pp and ±1.0 pp absolute, and adds a finer-resolution band at ±500 ppm / ±1000 ppm so the BC-E sheet can quote a vendor-capability-matched tolerance rather than an overly-loose absolute spec |
| Spec sheet drifts during quote round-trips | Low | BC-F explicitly forbids mid-quote spec changes; if a vendor pushes back, the WP re-opens at BC-C, not at BC-E |
| Anti-seeding violation through accidental commit to `/src/` | Low | Notebook stays inside this WP folder during BC-B; promotion to `/notebooks/exploration/` happens only at BC-F closure |

---

## 9 · Acceptance criteria for "done"

WP closes when:

1. Phase BC-B notebook reproduces Friedenauer's published `P_UV = 0.275 W`
   **within 5 %** at the published operating point (`P_in = 0.95 W`,
   `T_IC = 0.016`) using the BC-A-pinned `(L_passive_PHE, γ_SHG_BBO_PHE)`
   constants. This is a one-equation forward test on the model; `T_IC_opt`
   at the same `(L, γ)` is reported as a finding (expected ≈ 0.022,
   indicating Friedenauer ran below the impedance-matched optimum) but
   is *not* a pass/fail criterion. The earlier "reproduce T_IC = 0.016
   within 0.5 pp *and* P_UV within 5 %" formulation was internally
   inconsistent with the Phase E γ value — reviewer Finding 1, v2 fix.
2. Five spec sheets under `specs/` (M1', M2', M3', M4', cover letter) carry
   explicit reflectivity / transmission targets, tolerance bands, AOI,
   polarization, substrate, LIDT margin, quantity, and the two-scenario
   column structure.
3. `closure.md` records the frozen spec set, the open items deferred to
   vendor-quote time, and a cross-link from
   [`docs/components/inventory.md`](../../docs/components/inventory.md) §B
   and [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D.1.
4. The mechanical anti-seeding scan still passes
   ([`tests/test_anti_seeding_src_imports.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/tests/test_anti_seeding_src_imports.py),
   142/142 last green).
5. **No vendor inquiry has been sent.** Sending an inquiry is a separate
   procurement decision (KD-UV280-005 / -007), not part of this WP.

---

## 10 · Out of scope

- LBO-stage coatings (handled in a separate inquiry if and when the
  next-gen WP indicates an LBO coating-run is needed).
- Cavity geometry re-optimisation (held at Friedenauer §D values; see
  [next-gen WP Phase NG-D](../2026-05-08-next-gen-500mW-workplan.md) for
  geometry sweeps).
- Architecture-family scoring (G1 / G2 gated).
- Vendor selection, quote evaluation, ordering, and inspection on receipt
  (downstream procurement KD).
- 280 nm UV-degradation modelling (G2-dependent; separate workplan).
- Phase-noise budget flow to the Raman gate (Phase 0.5 territory).
- BBO crystal procurement (handled in
  [`docs/components/inventory.md`](../../docs/components/inventory.md) §B.2,
  with the Raicol 2025 lot already on shelf).

---

## 11 · Pre-conditions (state at WP opening)

- [`/src/`](../../src/) carries `enhancement_cavity.optimal_input_coupler`
  with the depleted-regime solver and the exact `−L · η_nl` cross term
  (numerics-expansion workplan Phase C, closed).
- Phase E Friedenauer cross-check at the BBO stage: agreement to 1.5 %.
- [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md)
  §D enumerates the geometry constants this WP freezes.
- [`docs/components/inventory.md`](../../docs/components/inventory.md) §B
  enumerates on-shelf mirrors that may or may not meet the new spec —
  the inquiry covers what *isn't* on the shelf.
- CHARTER §1.5 reference triple locked; G3 closed; G1, G2 OPEN.

---

## 12 · See also

- [`logbook/2026-05-08-next-gen-500mW-workplan.md`](../2026-05-08-next-gen-500mW-workplan.md) — the parent workplan; this BBO coating-run inquiry is a *narrowing* of NG-C and NG-E to the BBO stage and to a vendor-ready spec sheet.
- [`docs/architectures/next-gen.md`](../../docs/architectures/next-gen.md) — the architectures page that the parent workplan feeds.
- [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D — the BBO-stage geometry and coating values held fixed here.
- [`docs/components/inventory.md`](../../docs/components/inventory.md) §B — on-shelf mirrors keyed to the same Friedenauer roles; the spec sheets will be compared against this inventory at BC-F.
- [`docs/components/home-built-doublers.md`](../../docs/components/home-built-doublers.md) — three currently fielded BBO ring cavities at the same Friedenauer-equivalent geometry; service-life data from these doublers (if and when measured) would anchor BC-D's LIDT margin.
- [`logbook/2026-05-13-home-built-doublers-survey.md`](../2026-05-13-home-built-doublers-survey.md) — companion lab-asset survey.
