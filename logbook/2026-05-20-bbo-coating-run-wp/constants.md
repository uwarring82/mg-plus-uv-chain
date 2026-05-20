# BC-A · Frozen constants for the BBO coating-run WP

**Phase:** BC-A output ([`workplan.md`](workplan.md) §4 Phase BC-A)
**Status:** DRAFT (2026-05-20) — values pinned; pending steward sign-off at BC-F
**Authoritative for:** `γ_SHG_BBO`, `L_passive_PHE`, the three-row `L_passive`
separation, the intensity envelope feeding BC-D, and the NG-D consistency
check.

**Compute environment.** All numerical values below are produced from
the architecture-neutral primitives in
[`/src/enhancement_cavity.py`](../../src/enhancement_cavity.py) and
[`/src/shg_single_pass.py`](../../src/shg_single_pass.py), consuming the
material constants tabulated in §A2 below. The forward solver is the
exact `−L · η_nl` cross-term solver (Polzik–Kimble-class, depleted
regime, Brent root-finder); no small-signal approximation is used. No
new code is committed by BC-A.

---

## A1 · Geometry constants held fixed (Friedenauer 2006 §D)

| Symbol | Value | Source |
|---|---|---|
| `L_cav_BBO` | 0.470 m | Friedenauer Table 1 |
| Full folding angle | 27.4° (13.7° per curved mirror) | Friedenauer §3 |
| Focusing-mirror focal length `f` | 25 mm (R = 50 mm, concave) | Friedenauer §3 |
| Focusing-mirror separation `d'` | 59.4 mm | Friedenauer Table 1 |
| Intracavity waist `w_0` at BBO | 19.4 μm (BK-optimum for L_BBO = 10 mm) | Friedenauer §3 |
| BBO dimensions / cut | Brewster-cut Type-I, 4 × 4 × 10 mm³ | Friedenauer §3 (paper-stated) |
| BBO Type-I PM angle θ | 44.4° (Sellmeier-derived; **not** Friedenauer-stated) | Eimerl 1987 / Tamosauskas 2018 |
| BBO oven set-point | ~ 50 °C | Friedenauer §3 |
| AOI plane mirrors M1', M2' | ~ 0° p-pol | Friedenauer §3 (bowtie topology) |
| AOI curved mirrors M3', M4' | 13.7° p-pol | Friedenauer §3 |

## A2 · Material constants consumed by the cavity solver

| Symbol | Value | Source / tier | Notes |
|---|---|---|---|
| `λ_pump` (559 nm) | 559 × 10⁻⁹ m | — | Fundamental at BBO stage |
| `λ_harmonic` (280 nm) | 279.5 × 10⁻⁹ m | — | Half of pump |
| `n_o(559 nm)` (BBO ordinary) | 1.67276 | [`Eimerl1987`](../../data/literature/Eimerl1987/notes.md) Sellmeier | Cross-checked against [`Tamosauskas2018`](../../data/literature/Tamosauskas2018/notes.md): Δn ≈ 9 × 10⁻⁴, sub-percent on γ |
| `n_e(280 nm)` (BBO extraordinary) | 1.565 (approximate) | Eimerl Sellmeier extrapolation | Phase E open item; ≤ few-% on γ |
| Walk-off `ρ` at θ_PM | 83.1 mrad | [`Eimerl1987`](../../data/literature/Eimerl1987/notes.md) | Tamosauskas cross-check: ρ = 83.8 mrad (Δρ = 0.7 mrad, sub-1 %) |
| `d_eff` (BBO, 559→280, Type-I) | 1.44 pm/V (central; range 1.30–1.60 pm/V) | [`Eckardt1990`](../../data/literature/Eckardt1990/notes.md) | The dominant γ-uncertainty axis |

## A3 · γ_SHG_BBO — pinned

Computed in [`/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](../../notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py)
(Phase E), confirmed by BC-A re-run on 2026-05-20:

| Bracket | `d_eff` | `γ_SHG_BBO` (W⁻¹) |
|---|---|---|
| Low | 1.30 pm/V | 1.2155 × 10⁻⁴ |
| **Central (PINNED for this WP)** | **1.44 pm/V** | **1.4914 × 10⁻⁴** |
| High | 1.60 pm/V | 1.8412 × 10⁻⁴ |

Auxiliary Boyd–Kleinman quantities at the Friedenauer BBO geometry
(`L = 10 mm`, `w_0 = 19.4 μm`, `λ = 559 nm`, `n = 1.67276`):

| Quantity | Value |
|---|---|
| `ξ` (focusing parameter, L/b) | 1.413 |
| `β` (walk-off parameter) | 18.02 |
| `h_m` (Boyd–Kleinman factor with walk-off) | 0.0330 |

**This file is the sole γ authority for this WP.** BC-B consumes
`γ_SHG_BBO = 1.4914 × 10⁻⁴ W⁻¹` from this table and does *not* re-derive
it. If a future iteration updates γ (Sellmeier refresh, Eckardt
re-extraction, or a new d_eff anchor), the update lands here first and
BC-B is re-run.

---

## B · Three-row `L_passive` separation

| Row | Symbol | Definition | Value (Friedenauer corner) | Source |
|---|---|---|---|---|
| **B.1** | `L_mirror_T_at_spec_limit` | Sum over M2'/M3'/M4' of (1 − R_min_spec): (1−0.998) + (1−0.9993) + (1−0.9993) | **3 400 ppm** (upper envelope; actual loss ≤ this if mirrors sit above the R-floor) | Friedenauer Table 1 R-values, stated as `> 0.998` / `> 0.9993` lower bounds |
| **B.2** | `L_passive_PHE` | Round-trip passive loss the forward solver requires at (`P_in = 0.95 W`, `T_IC = 0.016`, `γ = γ_PHE`) to reproduce `P_UV = 0.275 W` | **15 288 ppm ≈ 1.53 %** (pinned by BC-A; 14 025 / 16 621 ppm at the d_eff low/high bracket) | BC-A inline forward-solve, 2026-05-20 (see `bc-a-log.md`) |
| **B.3** | `T_loss_VENDOR_max` (per mirror) | Maximum per-mirror transmission loss the vendor must commit to deliver | **set at Friedenauer R-floor: 1133 ppm per mirror** (= 3400 / 3 if equal-allocated); BC-C may re-weight, e.g. asymmetric for the M4' dichroic | Path-2 baseline (see §C below) |

Derived quantities used downstream:

- `L_nonmirror_PHE ≡ L_passive_PHE − L_mirror_T_at_spec_limit = 11 888 ppm`
  — the non-mirror passive loss (BBO Brewster scatter + bulk absorption
  + oven-window AR + scatter floors) **inherited from Friedenauer**.
  Held fixed for the new build under the path-2 assumption that the
  Raicol 2025 / A-Star 2017 BBO class and the oven plumbing remain
  Friedenauer-equivalent.
- `L_total_VENDOR_grid ≡ L_nonmirror_PHE + Σ T_loss_VENDOR_max`
  — the total round-trip passive loss BC-B's impedance match consumes.
  Default operating point at BC-A closure: `L_total = 15 288 ppm`
  (mirrors at the Friedenauer R-floor).
- `T_IC_opt(P_in = 0.95 W, L = L_PHE, γ = γ_PHE) = 0.0217`
  — the impedance-matched IC transmission at the Friedenauer corner.
  Friedenauer ran at the procured `T_IC = 0.016`, i.e. **about 0.6 pp
  below the impedance-matched optimum** at their γ. This is the finding
  BC-B carries forward (per the v3 workplan acceptance), not a check.

**Sensitivity of L_PHE to γ:** ±1.5 % on γ (the Phase E validation
residual) shifts `L_PHE` by ±100 ppm (~0.6 % on L). **Sensitivity to
the d_eff bracket** (1.30 → 1.60 pm/V) shifts `L_PHE` from 14 025 ppm
to 16 621 ppm (±9 % on L). The d_eff bracket is the binding
uncertainty axis.

---

## C · Loss-anchor evidence pass — path-2 adopted; path-1 candidates queued

**Chosen path:** path 2 (Phase-E-anchored). Vendor pre-inquiry inadmissible
inside this WP (workplan §4 BC-A Deliverable C "not admissible" clause).

**Why not path 1 at WP opening.** A targeted scan of the local dossier
on 2026-05-20 turned up **no IBS HR coating-loss numerical anchor at
559 nm in extracted form**. The strongest candidates have PDFs locally
staged but are SCAFFOLD-only:

| Candidate | Status | Why it would close the gap |
|---|---|---|
| [`Hannig2018`](../../data/literature/Hannig2018/notes.md) — PTB monolithic BBO ring SHG, 626 → 313 nm | SCAFFOLD | Same SHG-ring topology family as Friedenauer; visible-IR cavity finesse and coating-class numbers are exactly what BC-A needs. PDF locally staged (`013106_1_online.pdf`), CC-BY-4.0 |
| [`Kraus2022`](../../data/literature/Kraus2022/notes.md) — PTB twofold UV SHG to 267 nm | SCAFFOLD | Twofold SHG cavity directly analogous to Friedenauer; reports cavity finesses and the IBS coating regime. PDF locally staged (`oe-30-25-44992.pdf`), Optica OAPA |
| [`Shaw2021`](../../data/literature/Shaw2021/notes.md) — 2 W CW 261.5 nm AlCl cooling laser | SCAFFOLD | CW UV SHG cavity; not the closest match but useful |
| [`Turcicova2022`](../../data/literature/Turcicova2022/notes.md) — BBO LIDT review | DRAFT (secondary literature) | LIDT data, **not** HR coating-loss; informs BC-D but not BC-B |

**Path-1 follow-up queued** (out of BC-A scope, ~ 0.5–1 day each):
extract Hannig2018 and Kraus2022 cavity-finesse / mirror-R rows into
their `extracted.yaml`. If either lands during the BC-F calendar
window, BC-A's `T_loss_VENDOR_max` is tightened below the 1 133 ppm
per-mirror Friedenauer floor; BC-B is re-run on the new ceiling. If
neither lands, the WP closes at the path-2 baseline and the procurement
KD inherits a "vendor pre-inquiry to obtain measured-R for past UV SHG
cavity runs" follow-up.

**Path-2 declaration (operative).** `T_loss_VENDOR_max = 1 133 ppm`
per mirror (= 3 400 ppm summed, equal-allocated; BC-C may re-weight).
This sets `L_total_VENDOR_grid = 15 288 ppm` at the Friedenauer corner,
i.e., the new build operates at *exactly* the Friedenauer-class loss
under the path-2 assumption. Headroom for buildup improvement exists
only on the mirror axis — if the vendor commits to better than the
R-floor, BC-B's `T_IC_opt` shifts and BC-C re-allocates.

---

## D · Circulating-power and peak-intensity envelope

Computed inline in `bc-a-log.md` (forward solver with the BC-A-pinned
γ and L). Two `L_total` grid points: the path-2 baseline (mirrors at
the Friedenauer R-floor) and an optimistic "tight mirrors" point
(200 ppm per mirror = 600 ppm summed mirror loss, plausible IBS
upper-class). Friedenauer's 0.95 W point is included as the validation
corner.

### D.1 · At `L_total = 15 288 ppm` (path-2 baseline)

| `P_in_559` | `T_IC_opt` | `P_circ` (559 nm intracavity) | `P_UV` | Peak `I` at BBO waist | Peak `I` at curved mirror |
|---|---|---|---|---|---|
| **0.50 W (low scenario)** | 0.0191 (1.91 %) | 26.2 W | **0.102 W UV** | 4.4 MW/cm² | ~ 26 kW/cm² |
| 0.95 W (Friedenauer corner) | 0.0217 (2.17 %) | 43.8 W | 0.285 W UV | 7.4 MW/cm² | ~ 43 kW/cm² |
| **1.50 W (high scenario)** | 0.0243 (2.43 %) | 61.7 W | **0.565 W UV** | 10.4 MW/cm² | ~ 60 kW/cm² |

### D.2 · At `L_total = 12 488 ppm` (tight-mirrors path)

| `P_in_559` | `T_IC_opt` | `P_circ` | `P_UV` | Peak `I` at BBO waist |
|---|---|---|---|---|
| 0.50 W | 0.0169 (1.69 %) | 29.7 W | 0.131 W UV | 5.0 MW/cm² |
| 0.95 W | 0.0196 (1.96 %) | 48.5 W | 0.349 W UV | 8.2 MW/cm² |
| 1.50 W | 0.0223 (2.23 %) | 67.2 W | 0.669 W UV | 11.4 MW/cm² |

### D.3 · Beam geometry (Gaussian, BBO TEM₀₀ at 559 nm)

| Quantity | Value |
|---|---|
| Rayleigh range `z_R` at BBO (in BBO, n = 1.673) | 3.54 mm |
| Rayleigh range `z_R` in air (= air-equivalent for cavity-arm propagation) | 2.12 mm |
| Distance waist → curved mirror | ~ 29.7 mm (= d′/2) |
| Spot radius at curved mirror — v1 estimate (zR_BBO for full propagation) | ~ 164 μm |
| Spot radius at curved mirror — **corrected (proper BBO + air propagation)** | **~ 255 μm** |

**Methodology note.** The v1 spot-radius value (~ 164 μm) used `zR_BBO` for the
full waist-to-mirror propagation, which is incorrect because only 5 mm of the
29.7 mm distance is in BBO; the remaining ~ 25 mm is air. Proper propagation
through the BBO crystal (q-parameter in n = 1.673), then through the flat
BBO–air interface, then through air to the curved mirror, gives the corrected
**~ 255 μm** spot radius. The v1 value is preserved here for traceability;
[`bc-c-results.md`](bc-c-results.md) §E uses the corrected value for the
BC-D hand-forward.

### D.4 · Headlines for steward deliberation (workplan §6 Q1)

- **The 0.5 W scenario delivers ~ 100–130 mW UV** at impedance-matched
  optimum — well below the §1.5 indicative ≥ 500 mW UV anchor. It is a
  *coating run that still works* if the upstream LBO stays at the
  Friedenauer baseline.
- **The 1.5 W scenario delivers ~ 565–670 mW UV** — at or just above the
  §1.5 indicative anchor. It is a *coating run that does not waste
  buildup* if the upstream LBO stretches to 1.5 × Friedenauer.
- **`T_IC_opt` separation between the two scenarios is 0.5 pp** (0.0191 →
  0.0243 at path-2 baseline) — *exactly* the typical IBS coating-run
  tolerance. Whether a single coating run can serve both scenarios
  within tolerance is therefore a **borderline call**; workplan §6 Q2
  (default "one variant, branch after BC-B") needs the steward to
  affirm or revise after seeing this row.
- **Peak intensities at the BBO waist are 4–10 MW/cm² CW** — below
  reported BBO bulk LIDT envelopes but in the regime where the M3'/M4'
  curved-mirror coatings see ~ 26–60 kW/cm² (corrected from the v1
  ~ 60–150 kW/cm² figure; v1 used the unphysical zR_BBO-for-full-
  propagation spot radius — see §D.3 methodology note) and the M4' back-face AR
  sees the outgoing 280 nm load. BC-D quantifies these against published
  LIDT.

---

## E · NG-D geometry-sweep consistency check

[NG-D in the next-gen workplan](../2026-05-08-next-gen-500mW-workplan.md)
sweeps crystal length and waist for both stages. At BC-A opening
(2026-05-20), NG-D status in
[`docs/architectures/next-gen.md`](../../docs/architectures/next-gen.md)
is **"⏳ pending NG-A"** — the sweep has not been run. The Friedenauer
geometry (`L_BBO = 10 mm`, `w_0 = 19.4 μm`, `f = 25 mm`) held fixed by
this WP is therefore *unchallenged* by any NG-D output at WP opening.

**Commitment.** This consistency check is **re-evaluated at BC-F
closure**. If NG-D lands in the interim and recommends a different
`f` or `w_0`, this WP **pauses at BC-F** until the recommendation is
reconciled — the curved-mirror ROC = 50 mm spec is the load-bearing
geometry-binding choice in the BC-E sheets, and a different `f` would
invalidate the M3'/M4' substrate purchase.

---

## F · Pinned-value summary for downstream consumption

The single table BC-B and BC-D need to consume:

| Symbol | Value | Used by |
|---|---|---|
| `γ_SHG_BBO_PHE` | 1.4914 × 10⁻⁴ W⁻¹ | BC-B impedance match |
| `L_passive_PHE` | 15 288 ppm (1.53 %) | BC-A internal cross-check; downstream BC-B baseline |
| `L_mirror_T_at_spec_limit` | 3 400 ppm | B.1 row of the loss-budget split |
| `L_nonmirror_PHE` | 11 888 ppm | Inherited fixed contribution under path 2 |
| `T_loss_VENDOR_max` (per mirror, summed = 3400 ppm) | 1 133 ppm | BC-C per-mirror allocation; BC-E spec target |
| `L_total_VENDOR_grid` (default = `L_passive_PHE`) | 15 288 ppm | BC-B sweep operating point |
| `T_IC_opt(0.95 W, L_PHE, γ_PHE)` | 0.0217 | Forward-cross-check reference (finding, not pass/fail) |
| `P_UV_published(0.95 W, T_IC = 0.016, L_PHE, γ_PHE)` | 0.275 W (within 1.5 % at L_loss = T_IC; exact at L_PHE = 15 288 ppm) | BC-B forward cross-check acceptance |

---

## G · Sign-off

| Gate (per workplan §4 BC-A acceptance) | Status |
|---|---|
| `constants.md` exists with geometry, material, three-row `L_passive`, intensity envelope, NG-D check | ✅ |
| Loss-anchor evidence pass chose path 1 or 2 (vendor pre-inquiry inadmissible) | ✅ path 2 (with path-1 candidates queued) |
| `L_passive_PHE` extracted from Phase E and pinned with uncertainty band | ✅ 15 288 ppm ±100 ppm (γ axis); 14 025–16 621 ppm (d_eff axis) |
| No code committed during BC-A | ✅ (`/src/` untouched; only this folder gained `bc-a-log.md` + `constants.md`) |

**BC-A is ready for BC-B consumption.** BC-B opens against the F-row
table above.
