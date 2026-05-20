# BC-A · Loss-model normalisation gate + constants freeze — running log

**Phase:** BC-A of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20
**Status:** CLOSED 2026-05-20 — BC-B unblocked

This log accumulates entries as BC-A executes. Each entry is dated and
sub-headed by deliverable so a future reader can trace which evidence
landed when. Numerical outputs live in [`constants.md`](constants.md); this
file records the *reasoning* and the *open items* trail.

---

## 2026-05-20 · Kickoff

Workplan endorsed for BC-A start after a four-round review pass (v0 → v3),
ending at reviewer #2's "ready to start BC-A" verdict. The blocking
issues identified across the review rounds are listed in
[`workplan.md`](workplan.md); they are *not* repeated here. This log
opens with the assumption that v3 of `workplan.md` is the binding
description.

**BC-A scope recap** (from `workplan.md` §4 Phase BC-A):

- **Deliverable A** — geometry + material constants table.
- **Deliverable B** — three-row `L_passive` separation
  (`L_mirror_T_at_spec_limit` / `L_passive_PHE` / `T_loss_VENDOR_max`).
- **Deliverable C** — literature gap call: path 1 (targeted literature
  pass) or path 2 (Phase-E-anchored fallback). Vendor pre-inquiry is
  inadmissible inside this WP.
- **Deliverable D** — circulating-power and peak-intensity envelope, two
  scenarios × the `L_total_VENDOR_grid` BC-A chooses.
- **Deliverable E** — NG-D geometry-sweep consistency check (confirm
  the parent next-gen WP has not invalidated the frozen Friedenauer
  geometry).

**Acceptance gates** (recap):

1. [`constants.md`](constants.md) exists with all five deliverables.
2. Loss-anchor evidence pass has chosen path 1 or path 2 and recorded
   the choice.
3. `L_passive_PHE` pinned with an uncertainty band — not carried as a
   symbol.
4. No code committed during BC-A.

**Charter-compliance reminders.**
- `constants.md` is the **sole γ authority** for the WP (Reviewer
  Finding 5 v2→v3). BC-B consumes γ from there; γ is *not* recomputed in
  the BC-B notebook.
- BC-B's acceptance is now a **one-equation forward test** on `P_UV`,
  with `T_IC_opt ≈ 0.022` reported as a finding (not a check). BC-A
  must therefore pin γ *and* close the L joint with γ, so that the
  forward test in BC-B is uniquely defined.
- Path-2 fallback uses the additive decomposition
  `L_total = L_nonmirror_PHE + Σ T_loss_VENDOR_max`
  (Reviewer #2 finding 1, v2→v3). `L_nonmirror_PHE` carries the crystal
  Brewster scatter + BBO bulk absorption + oven-window AR + scatter
  floors and is *inherited* from Friedenauer — i.e., not a coating-run
  variable.

**Plan of attack.**

1. Read Phase E notebook
   ([`notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](../../notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py))
   end-to-end. Extract the γ_SHG_BBO it uses and the L_passive it
   inferred. Note the cross-check residual.
2. Read the architecture-neutral primitives
   ([`/src/enhancement_cavity.py`](../../src/enhancement_cavity.py),
   [`/src/shg_single_pass.py`](../../src/shg_single_pass.py),
   [`/src/boyd_kleinman.py`](../../src/boyd_kleinman.py)) to confirm the
   exact function signatures BC-B will consume.
3. Pin material constants from the literature dossier:
   `d_eff` (Eckardt 1990), walk-off `ρ` and refractive indices
   (Eimerl 1987 with Tamosauskas 2018 cross-check).
4. Build `constants.md` with Deliverables A and B populated.
5. Run the literature-gap evidence pass (Deliverable C). Default to
   path 1; fall back to path 2 if path 1 returns empty.
6. Compute the intensity envelope (Deliverable D) — back-of-envelope
   from the pinned γ, the BBO geometry, and a circulating-power formula
   that uses only architecture-neutral relations.
7. Check NG-D status (Deliverable E) against the parent next-gen WP.
8. Append a closure entry to this log; sign BC-A off.

Each step is appended below as a dated sub-section.

---

## 2026-05-20 · BC-A executed and closed (single calendar day)

### Step 1 — Phase E re-run, γ pinned

Ran [`notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](../../notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py)
end-to-end against the current `/src/` primitives on 2026-05-20. The
notebook is unchanged since 2026-05-07; output is reproducible and
matches the §10 summary of the parent next-gen workplan.

Pinned values (full table → [`constants.md`](constants.md) §A3):

- `γ_SHG_BBO_PHE` (central) = **1.4914 × 10⁻⁴ W⁻¹**
- d_eff bracket: 1.30 (low) → 1.60 pm/V (high), corresponding to γ
  range 1.2155 × 10⁻⁴ → 1.8412 × 10⁻⁴ W⁻¹.
- BK quantities at the Friedenauer geometry: ξ = 1.413, β = 18.02,
  `h_m = 0.0330` (deeply walk-off-limited; this is the dominant
  difference between LBO NCPM and BBO Type-I focusing).

**Observation.** Phase E's standalone BBO row reproduces the published
P_UV = 0.275 W within 1.5 % at the impedance-match shortcut assumption
`L_loss_BBO = T_IC = 0.016`. The cascade row only agrees to 47 % overall
(0.143 vs 0.152) because the **LBO stage carries a separate −26 %
residual** (open `L_passive` definition gap at the LBO stage, flagged as
NG-A in the parent workplan). The LBO discrepancy does *not* affect
this WP — BC-A is BBO-only and operates on the validated BBO row.

### Step 2 — L_passive_PHE pinned

The v3 workplan acceptance requires `L_passive_PHE` to be a *pinned
number with uncertainty band*, not the impedance-match shortcut Phase E
used (`L = T_IC = 0.016`). BC-A ran the forward solve
`harmonic_output_W(P_in = 0.95, T_IC = 0.016, L, γ = γ_PHE) − 0.275 = 0`
via Brent on `L`. Result:

- **`L_passive_PHE = 15 288 ppm ≈ 1.53 %`** at γ central.
- Sensitivity to γ ±1.5 % (the Phase E validation residual): L_PHE
  shifts by ±100 ppm (~0.6 % on L).
- Sensitivity to d_eff bracket: L_PHE ranges 14 025 → 16 621 ppm
  across d_eff 1.30 → 1.60 pm/V (±9 %). **d_eff is the binding
  uncertainty axis.**

The 1.53 % matches reviewer #3 v3-round's reverse-engineering exactly
("L ≈ 1.53%"); reviewer #2 v2-round's earlier ~1.14 % estimate was
slightly off because that reviewer's γ differed from Phase E's by a
factor that BC-A's full re-run resolves.

### Step 3 — Three-row L_passive separation

Per workplan §4 BC-A Deliverable B (and v3 reviewer Finding 2):

| Row | Symbol | Value |
|---|---|---|
| B.1 (upper envelope from R-floors) | `L_mirror_T_at_spec_limit` | 3 400 ppm |
| B.2 (Phase-E-forward-solve) | `L_passive_PHE` | **15 288 ppm** |
| B.3 (vendor coating ceiling) | `T_loss_VENDOR_max` | 1 133 ppm/mirror, summed 3 400 ppm (path 2) |
| Derived: B.2 − B.1 | `L_nonmirror_PHE` | **11 888 ppm** |

The ~ 3.4 × gap between B.2 and B.1 is the **non-mirror passive loss**
that the new build inherits from the Friedenauer architecture (BBO
Brewster scatter + bulk absorption + oven-window AR + scatter floors).
This is the reviewer-validated argument for separating the rows
explicitly: a vendor spec that asked for `T_loss_VENDOR ≤ L_passive_PHE`
would let the mirrors consume the entire round-trip budget and leave
zero allowance for the non-mirror axis. BC-A operates on the additive
decomposition `L_total = L_nonmirror_PHE + Σ T_loss_VENDOR_max` per
workplan v3 Finding 1.

### Step 4 — T_IC_opt finding (not a check)

At `(P_in = 0.95 W, L = L_PHE, γ = γ_PHE)`, BC-A's forward solver gives:

- `T_IC_opt = 0.0217` (2.17 %) — ~ 0.6 pp above Friedenauer's published
  `T_IC = 0.016`. **Friedenauer ran ~ 0.6 pp below the impedance-matched
  optimum** at their γ. This is the v3 workplan finding that BC-B
  carries forward (not a pass/fail check; per the workplan v3 fix to
  the inconsistent v2 acceptance).
- `P_UV` at the optimum `T_IC_opt = 0.0217` would have been 0.285 W
  vs the published 0.275 W (= +3.6 % buildup forgone by ordering the
  closest-available rather than the optimum coating).
- This matches reviewer #3 v3-round's reverse-engineering of "T_IC_opt
  ≈ 0.0217" exactly.

### Step 5 — Literature gap call (Deliverable C)

Targeted scan of the local
[`data/literature/`](../../data/literature/) tree on 2026-05-20 for
an IBS HR coating-loss numerical anchor at 559 nm. **Result: no
extracted-form anchor in the dossier.** Closest candidates have PDFs
locally staged but remain SCAFFOLD-only:

- [`Hannig2018`](../../data/literature/Hannig2018/notes.md) — PTB
  monolithic 626 → 313 nm BBO ring SHG. Same architecture family as
  Friedenauer. PDF available, CC-BY-4.0.
- [`Kraus2022`](../../data/literature/Kraus2022/notes.md) — PTB twofold
  UV SHG cavity to 267 nm. Direct architectural analogue of Friedenauer.
  PDF available, Optica OAPA.
- [`Shaw2021`](../../data/literature/Shaw2021/notes.md) — CW UV SHG to
  261.5 nm; useful but not closest match.
- [`Turcicova2022`](../../data/literature/Turcicova2022/notes.md) — BBO
  LIDT review; LIDT-only, not HR coating loss.

**Path-2 (Phase-E-anchored) adopted as BC-A's operating choice.**
Setting `T_loss_VENDOR_max = 1 133 ppm/mirror` (Σ = 3 400 ppm) commits
to a coating run at the Friedenauer R-floor and accepts that buildup
headroom exists *only* on the mirror axis (the non-mirror axis is held
fixed at `L_nonmirror_PHE`). **Path-1 candidates Hannig2018 and
Kraus2022 are queued as a follow-up extraction task**; if either lands
during the BC-F calendar window, BC-A constants tighten and BC-B is
re-run. If not, the WP closes at the path-2 baseline and the
procurement KD inherits a "vendor pre-inquiry for measured-R on past
UV SHG cavity runs" follow-up. **Vendor contact remains inadmissible
inside this WP** per workplan §4 BC-A Deliverable C.

### Step 6 — Intensity envelope (Deliverable D)

Computed inline with the forward solver at `L_total = 15 288 ppm`
(path-2 baseline) and a `tight-mirrors` upgrade point at
`L_total = 12 488 ppm` (200 ppm/mirror IBS upper-class). Full table →
[`constants.md`](constants.md) §D.

**Highlights for §6 Q1 deliberation:**

- 0.5 W → ~ 100–130 mW UV (well below §1.5 ≥ 500 mW indicative).
- 1.5 W → ~ 565–670 mW UV (at or just above indicative).
- `T_IC_opt` separation between the two scenarios is **0.5 pp**
  (0.0191 → 0.0243) — *exactly* the typical IBS single-run tolerance,
  making §6 Q2 (one variant vs two) a genuinely borderline call.
- Peak intensities at the BBO waist: 4–10 MW/cm² CW; on the curved
  mirrors: 60–150 kW/cm² CW; outgoing 280 nm on the M4' back-face AR:
  bracketed at the same BC-D row. **All values below BC-D's still-pending
  LIDT comparison** but in the regime where margin matters.

### Step 7 — NG-D consistency check (Deliverable E)

Status check against the parent next-gen workplan: NG-D is
**"⏳ pending NG-A"** as of 2026-05-20. No NG-D output exists that
challenges the Friedenauer-frozen geometry; BC-A proceeds. Re-checked
at BC-F closure per workplan §4.

### Step 8 — Acceptance gate review

Workplan §4 BC-A acceptance criteria checked one-by-one — all four
gates pass; full table → [`constants.md`](constants.md) §G.

**BC-A closed 2026-05-20.** Calendar: single working day (workplan
estimate: 1 day; actual: ~ matches). No /src/ change; no notebook
commit; no vendor contact; no MEMORY.md update. The WP folder now
contains [`workplan.md`](workplan.md), this log, and
[`constants.md`](constants.md).

**BC-B is unblocked** and opens against [`constants.md`](constants.md)
§F as its sole γ / L source.

### Open items handed forward

- **Path-1 follow-up (queued, optional).** Extract Hannig2018 and
  Kraus2022 cavity-finesse / mirror-R rows into their `extracted.yaml`.
  ~ 0.5–1 day each. Tightens `T_loss_VENDOR_max` below the 1 133 ppm
  Friedenauer floor if landed before BC-F.
- **n_e(280 nm) refinement.** Currently 1.565 (approximate, Eimerl
  extrapolation); a Tamosauskas-driven update may sub-1 % shift γ.
  Routed through `constants.md` first, BC-B re-run downstream.
- **d_eff bracket tightening.** The d_eff 1.30–1.60 pm/V range is the
  binding uncertainty on `L_PHE`. A post-2020 d_eff measurement would
  tighten this; out of scope of BC-A but a candidate task-E entry.

---
