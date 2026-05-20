# BC-B · Impedance match per scenario — running log

**Phase:** BC-B of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20 (after BC-A closure same day)
**Status:** CLOSED 2026-05-20 — BC-C unblocked

This log accumulates entries as BC-B executes against the constants
pinned in [`constants.md`](constants.md) §F by BC-A.

---

## 2026-05-20 · Kickoff

BC-A closed within the calendar day (see [`bc-a-log.md`](bc-a-log.md));
the steward greenlit BC-B start. BC-B opens against:

- `γ_SHG_BBO_PHE = 1.4914 × 10⁻⁴ W⁻¹` ([`constants.md`](constants.md) §A3)
- `L_passive_PHE = 15 288 ppm` (= L_total path-2 baseline)
- `L_nonmirror_PHE = 11 888 ppm` (held fixed)
- Vendor mirror ceiling `Σ T_loss_VENDOR_max` = the swept axis

**BC-B scope recap** (from [`workplan.md`](workplan.md) §4 Phase BC-B):

- **Deliverable 1** — Notebook `notebooks/2026-05-20-bbo-ic-impedance-match.py`
  inside this folder. Consumes `γ` from [`constants.md`](constants.md);
  does **not** re-derive γ.
- **Deliverable 2** — Per `(P_in_559, L_total_VENDOR_grid)` point:
  `T_IC_opt` (in ppm + pp), `P_circ`, peak intensity at the BBO waist,
  `P_UV`, and two sensitivity columns:
  - *Manufacturing tolerance.* UV drop at `T_IC_opt ± 0.5 pp` and
    `± 1.0 pp`, plus a finer band at `± 500 ppm` / `± 1000 ppm`
    (the regime where IBS metrology is actually challenged — risks
    table v3 fix).
  - *Physics tolerance.* UV drop at `γ ± 1.5 %`.
- **Deliverable 3** — A consumption table for BC-C (per scenario:
  one nominal `T_IC` target + a tolerance band the vendor can quote
  against; per scenario: a per-mirror Σ `T_loss_VENDOR_max` budget the
  M2'/M3'/M4' specs must collectively hit).

**Acceptance gates** (workplan §4 BC-B):

1. **Forward cross-check.** At `(P_in = 0.95 W, T_IC = 0.016)` with the
   BC-A-pinned `(L_PHE, γ_PHE)`, notebook reproduces `P_UV = 0.275 W`
   within 5 %. One-equation forward test.
2. **Optimum-finding (reported, not pass/fail).** `T_IC_opt(0.95 W)` at
   the same `(L_PHE, γ_PHE)` ≈ 0.022; reports that Friedenauer ran
   below the optimum.
3. **Grid table.** 2 × {L_total grid points} with both sensitivity
   columns; suitable for BC-C consumption.

**L_total grid choice.** Four points across the achievable IBS class:

| Point | Σ T_loss (mirror sum) | L_total | Description |
|---|---|---|---|
| (i) | 3 400 ppm (R-floor) | 15 288 ppm | Path-2 baseline (Friedenauer-class) |
| (ii) | 1 500 ppm (500 ppm/mirror) | 13 388 ppm | Intermediate IBS class |
| (iii) | 600 ppm (200 ppm/mirror) | 12 488 ppm | IBS upper-class (constants.md §D.2) |
| (iv) | 300 ppm (100 ppm/mirror) | 12 188 ppm | Cavity-finesse-grade IBS (aspirational) |

Each scenario × each L_total grid point = 8 cells in the main table.

**Plan of attack.**

1. Write the notebook (jupytext py:percent, mirroring Phase E layout).
2. Run forward cross-check (gate 1) inline.
3. Run optimum-finding (gate 2).
4. Run the 2 × 4 grid (gate 3 main table).
5. Run both sensitivity columns.
6. Distill the BC-C consumption table.
7. Close this log with the §6 Q2 implication call.

Each step appended below as a dated sub-section.

---

## 2026-05-20 · BC-B executed and closed (single calendar day)

### Step 1 — Notebook scaffolded

[`notebooks/2026-05-20-bbo-ic-impedance-match.py`](notebooks/2026-05-20-bbo-ic-impedance-match.py)
written as a jupytext py:percent file mirroring the Phase E layout.
Sections 1–10: constants loader (consumes BC-A `constants.md` §F),
gate-1 forward cross-check, gate-2 optimum-finding, beam-geometry
helper, main grid, manufacturing-tolerance sensitivity,
γ ± 1.5 % + d_eff full bracket sensitivity, §6 Q2 Δ`T_IC_opt` test,
BC-C consumption distillation, acceptance summary. All compute paths
use only the architecture-neutral primitives in
[`/src/enhancement_cavity.py`](../../src/enhancement_cavity.py) and
[`/src/shg_single_pass.py`](../../src/shg_single_pass.py); γ is
imported as a numeric constant, *not* recomputed.

### Step 2 — Acceptance gate 1 (forward cross-check) — PASS

At `(P_in = 0.95 W, T_IC = 0.016, L = 15 288 ppm, γ = 1.4914e-4)`:

```
P_UV computed = 0.2750 W
P_UV published = 0.2750 W
Residual = −0.00 %   PASS (5 % gate)
```

The −0.00 % residual is *exact to display precision* because BC-A
pinned `L_passive_PHE` by inverting precisely this forward relation.
The cross-check is therefore a tautology — its real meaning is that
the BC-A → BC-B handoff is internally consistent, which is the
binding test the workplan acceptance was actually after.

### Step 3 — Acceptance gate 2 (T_IC_opt finding) — reported

At `(P_in = 0.95 W, L = L_PHE, γ = γ_PHE)`:

```
T_IC_opt        = 0.02169   (2.17 %)
T_IC published  = 0.01600   (1.60 %)
Gap             = +0.57 pp  → Friedenauer ran below the optimum
P_UV at T_opt   = 0.2848 W  → +3.57 % buildup forgone vs published 0.275 W
P_circ at T_opt = 43.80 W
```

Exact match to BC-A's reviewer back-of-envelope ("T_IC_opt ≈ 0.0217").
This is a finding, not a check — the v3 workplan fix to the v2
inconsistent acceptance held up under the actual numbers.

### Step 4 — Acceptance gate 3 (main grid) — populated

2 scenarios × 4 `L_total` grid points = 8 cells, full table at
[`bc-b-results.md`](bc-b-results.md) §B.

**Headline:** At the recommended default `L_total = 13 388 ppm`
(intermediate IBS, 500 ppm/mirror):
- **Low scenario (0.5 W in)**: `T_IC_opt = 17 565 ppm = 1.756 %`, `P_UV = 0.121 W`
- **High scenario (1.5 W in)**: `T_IC_opt = 22 945 ppm = 2.295 %`, `P_UV = 0.633 W`

### Step 5 — Manufacturing tolerance sensitivity

Four bands: ±500 ppm, ±1 000 ppm, ±0.5 pp (=5 000 ppm),
±1.0 pp (=10 000 ppm). Full results → [`bc-b-results.md`](bc-b-results.md) §D.

**Headline:** UV penalty at ±500 ppm is < 0.05 % in all 8 cells; at
±1 000 ppm < 0.15 %. The reviewer-flagged ±0.5 pp is **absurdly loose**
(3.7–4.8 % UV penalty on the Low scenario; the realistic IBS metrology
sits at ±500 ppm).

**Recommendation to BC-E:** quote `T_IC ± 500 ppm` on the M1' coating
spec sheet (with ±0.05 pp in parentheses). The BC-E spec is therefore
tighter than the workplan's earlier ±0.5 pp working figure but matches
the real coating-house capability.

### Step 6 — Physics tolerance sensitivity

γ ± 1.5 % shifts `T_IC_opt` by **±55–105 ppm** — an order of magnitude
*smaller* than the ±500 ppm manufacturing band, so γ is not the
binding axis. The d_eff bracket (1.30–1.60 pm/V) shifts `T_IC_opt` by
**±700 ppm (Low) / ±1 400 ppm (High)** — comparable to or larger than
the manufacturing tolerance. **d_eff is the binding physics
uncertainty axis** at the recommended tolerance.

Full table → [`bc-b-results.md`](bc-b-results.md) §E.

### Step 7 — §6 Q2 resolution (load-bearing finding)

Δ`T_IC_opt` between the 0.5 W and 1.5 W scenarios:

| `L_total` ppm | Δ`T_IC_opt` (pp) |
|---|---|
| 15 288 | 0.518 |
| 13 388 | **0.538** ← default |
| 12 488 | 0.547 |
| 12 188 | 0.550 |

**Stable at ~ 0.52–0.55 pp across all four `L_total` grid points** —
*well below* the 1 pp threshold for the §6 Q2 default "one variant"
recommendation. **A single M1' variant does *not* cover both optima
within the ±500 ppm manufacturing band** (the optima sit ~ 5 400 ppm
apart, well outside any single ±500 ppm band centred between them).
**The one-variant branch is acceptable on UV-penalty grounds**: at
the equal-penalty centre 19 965 ppm, both scenarios pay ~ −0.68 %
UV vs their respective optima, and the worst case across the
±500 ppm vendor metrology band stays below ~ −1.0 % in either
scenario. This is the v3 workplan's 1 pp branch rule applied to
the actual numbers — penalty-acceptable, not optimum-overlap.

§6 Q2 therefore **resolves to "one variant"** — confirming the v3
workplan default in the limit of actual numbers. The two-variant
branch is *not* needed; BC-C / BC-E carry one M1' page.

### Step 8 — BC-C consumption table distilled

[`bc-b-results.md`](bc-b-results.md) §F lays out the single per-scenario
row downstream consumers (BC-C / BC-E) need:

| Scenario | `T_IC_opt` | Vendor tolerance | `Σ T_loss_VENDOR_max` budget |
|---|---|---|---|
| Low (0.5 W) | 17 565 ppm | ±500 ppm | 1 500 ppm summed |
| High (1.5 W) | 22 945 ppm | ±500 ppm | 1 500 ppm summed |

Single-variant centre point recommendation: **19 965 ppm (≈ 2.00 %)
±500 ppm** — the *equal-penalty* centre where Low and High both pay
−0.68 % UV vs their respective optima. Note the v1 draft of this log
quoted "20 500 ppm biased toward High" with penalties (−1.7 %, −0.6 %);
both numbers were incorrect. The reviewer-verified numbers (and the
re-run BC-B notebook) show that *biasing toward High actually increases
the maximum penalty* — the Low side has a sharper impedance-match peak
at lower depletion, so moving away from its optimum costs more than
the symmetric move toward High saves. The correct policy is
equal-penalty centring (= minimax across the two scenarios), which
lands at 19 965 ppm.

### Step 9 — Acceptance gate review

All three workplan §4 BC-B gates pass; full table →
[`bc-b-results.md`](bc-b-results.md) §A.

**BC-B closed 2026-05-20.** Calendar: single working day (workplan
estimate: 1 day; actual: ~ matches). No `/src/` change; notebook lives
in WP folder pending BC-F promotion; no MEMORY.md update.

**BC-C is unblocked.** BC-C opens against
[`bc-b-results.md`](bc-b-results.md) §F (per-scenario `T_IC_opt`,
tolerance, mirror-loss budget) as its sole BC-B-derived input.

### Surprising findings to flag for the steward

1. **§6 Q2 default validated by the numbers.** Δ`T_IC_opt` = 0.52 pp
   across all `L_total` points — comfortably below the 1 pp branch
   threshold. One M1' variant, not two.
2. **±0.5 pp was a strawman; ±500 ppm is the right band.** The whole
   review-round discussion of `T_IC ± 0.5 pp` (= ±5 000 ppm) was
   anchored to the wrong metrology regime; IBS houses actually quote
   ±100–500 ppm, and the BC-E sheet should match.
3. **d_eff is the only physics axis that competes with manufacturing
   tolerance.** γ ± 1.5 % is ~ 10 × smaller than the d_eff bracket
   at the same operating point. A post-2020 d_eff anchor is the
   highest-value optional follow-up (task-E queue).
4. **Friedenauer left ~ 3.6 % UV on the table** — confirmed at exactly
   the BC-A back-of-envelope value. The BC-E cover letter should
   *explicitly* justify the new spec targeting a higher transmission
   than the 2006 reference; this is the steward-conversation point
   reviewer #1 v3-round flagged.

### Open items handed to BC-C

- **Per-mirror allocation** of the `Σ T_loss_VENDOR_max = 1 500 ppm`
  budget across M2' / M3' / M4'. Default equal (500/500/500); BC-C may
  re-weight asymmetrically to give the M4' dichroic more headroom on
  its dual-wavelength load.
- **Single centre point vs per-scenario centres on the M1' page.**
  §F gives both; steward call at BC-E.
- **Tolerance courtesy band.** Recommendation ±500 ppm; BC-E may quote
  ±750 ppm to vendors as a courtesy (still <0.1 % UV penalty). Not
  load-bearing.

---
