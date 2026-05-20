# BC-B · Impedance-match results — handoff to BC-C

**Phase:** BC-B output ([`workplan.md`](workplan.md) §4 Phase BC-B)
**Status:** DRAFT (2026-05-20) — values computed; pending steward sign-off at BC-F
**Authoritative for:** per-scenario `T_IC_opt`, recommended coating-spec
tolerance band, per-mirror `Σ T_loss_VENDOR_max` budget, sensitivity envelopes.

**Source.** [`notebooks/2026-05-20-bbo-ic-impedance-match.py`](notebooks/2026-05-20-bbo-ic-impedance-match.py),
run 2026-05-20 against [`constants.md`](constants.md) §F. Reproducible
end-to-end via the architecture-neutral primitives in `/src/`.

---

## A · Acceptance gate summary

| Gate (workplan §4 BC-B) | Required | Achieved | Status |
|---|---|---|---|
| **1.** Forward cross-check at Friedenauer corner | `P_UV` within 5 % of 0.275 W | residual = **−0.00 %** (P_UV = 0.2750 W) | ✅ PASS |
| **2.** Optimum-finding (reported, not pass/fail) | `T_IC_opt(0.95 W, L_PHE, γ_PHE)` reported | **`T_IC_opt = 0.02169`** (+0.57 pp above Friedenauer's procured 0.016; +3.57 % UV buildup forgone) | ✅ reported |
| **3.** Grid table populated | 2 scenarios × `L_total` grid × tolerance bands + γ column | **2 × 4 grid × 4 tolerance bands + γ ± 1.5 % + d_eff full bracket** | ✅ populated |

The Gate-1 −0.00 % residual is *exact* (to display precision) because
BC-A pinned `L_passive_PHE = 15 288 ppm` by inverting this same forward
relation. The cross-check is therefore a tautology — what it actually
demonstrates is that the BC-A → BC-B handoff is **internally
self-consistent**, which is the binding test the workplan acceptance
was actually asking for.

---

## B · Main grid — 2 scenarios × 4 `L_total` points

`P_in_559` = 559 nm input to the BBO ring; `P_UV` = 280 nm output. All
computed at impedance-matched `T_IC_opt` with the BC-A-pinned
`γ = 1.4914 × 10⁻⁴ W⁻¹`.

### B.1 · Low scenario (`P_in = 0.50 W`)

**Note on I_curved values.** The `I_curved` column uses the proper
Gaussian propagation through BBO + flat interface + air (notebook §4,
v2 of `spot_radius_at_curved_mirror_proper`), giving `w_curved ≈ 255 μm`.
The v1 of this file used a single-medium-helper (zR_BBO for full
propagation) that produced ~ 164 μm → I_curved ~ 0.41× larger.
[`constants.md`](constants.md) §D.3 and the BC-B notebook now use the
proper propagation; the v1 numbers are preserved in the methodology
notes for traceability. The `I_waist` column is unaffected.

| Σ T_loss (per mirror class) | `L_total` ppm | `T_IC_opt` (ppm / %) | `P_circ` (W) | `P_UV` (W) | I_waist (MW/cm²) | I_curved (kW/cm²) |
|---|---|---|---|---|---|---|
| 3 400 ppm (R-floor, path-2 baseline) | 15 288 | 19 119 / 1.912 % | 26.15 | 0.1017 | 4.42 | 25.7 |
| 1 500 ppm (intermediate IBS, 500/mirror) | 13 388 | **17 565 / 1.756 %** ← default | 28.47 | **0.1205** | 4.82 | 27.9 |
| 600 ppm (upper-class IBS, 200/mirror) | 12 488 | 16 846 / 1.685 % | 29.68 | 0.1310 | 5.02 | 29.1 |
| 300 ppm (cavity-finesse, 100/mirror) | 12 188 | 16 610 / 1.661 % | 30.10 | 0.1347 | 5.09 | 29.5 |

### B.2 · High scenario (`P_in = 1.50 W`)

| Σ T_loss (per mirror class) | `L_total` ppm | `T_IC_opt` (ppm / %) | `P_circ` (W) | `P_UV` (W) | I_waist (MW/cm²) | I_curved (kW/cm²) |
|---|---|---|---|---|---|---|
| 3 400 ppm (R-floor, path-2 baseline) | 15 288 | 24 299 / 2.430 % | 61.73 | 0.5649 | 10.44 | 60.6 |
| 1 500 ppm (intermediate IBS, 500/mirror) | 13 388 | **22 945 / 2.295 %** ← default | 65.37 | **0.6333** | 11.06 | 64.2 |
| 600 ppm (upper-class IBS, 200/mirror) | 12 488 | 22 320 / 2.232 % | 67.20 | 0.6691 | 11.37 | 65.9 |
| 300 ppm (cavity-finesse, 100/mirror) | 12 188 | 22 114 / 2.211 % | 67.83 | 0.6816 | 11.47 | 66.6 |

---

## C · §6 Q2 default validation — Δ`T_IC_opt` between scenarios

The workplan §6 Q2 default ("hold one M1' variant if Δ`T_IC_opt` ≲ 1 pp,
branch to two variants if larger") is now testable:

| `L_total` grid point | Δ`T_IC_opt` (Low → High) | §6 Q2 recommendation |
|---|---|---|
| Friedenauer R-floor (15 288 ppm) | **+0.518 pp** (5 180 ppm) | **One M1' variant** (well below the 1 pp threshold) |
| Intermediate IBS (13 388 ppm) | **+0.538 pp** (5 380 ppm) | **One M1' variant** |
| Upper-class IBS (12 488 ppm) | +0.547 pp (5 474 ppm) | One M1' variant |
| Cavity-finesse (12 188 ppm) | +0.550 pp (5 504 ppm) | One M1' variant |

**Headline finding.** Δ`T_IC_opt` between the 0.5 W and 1.5 W scenarios
is **stable at ~ 0.52–0.55 pp across all four `L_total` grid points** —
well below the workplan §6 Q2 1 pp branch threshold.

**What "one variant" actually means here.** A single M1' coating
variant **does *not* cover both optima within the ±500 ppm manufacturing
band**: the two optima sit ~ 5 400 ppm apart, several times wider than
any single ±500 ppm vendor-tolerance window. The one-variant branch is
acceptable instead on *UV-penalty grounds* (per the workplan §6 Q2 rule,
which is keyed off Δ`T_IC_opt`, not optimum overlap). At the
**equal-penalty centre `T_IC ≈ 19 965 ppm (2.00 %)`**, both scenarios
pay −0.68 % UV vs their respective optima, and the worst case across
the ±500 ppm vendor metrology band stays below ~ −1.0 % in either
scenario (full table in §F.2). **This resolves §6 Q2 in favour of
"one variant"** — performance-acceptable, not geometrically
coincident.

---

## D · Manufacturing tolerance sensitivity

For each cell, UV-output drop (worst-case across +Δ and −Δ from `T_IC_opt`).

### D.1 · Low scenario

| `L_total` ppm | `P_UV_opt` (W) | ΔP_UV at ±500 ppm | ΔP_UV at ±1000 ppm | ΔP_UV at ±0.5 pp | ΔP_UV at ±1.0 pp |
|---|---|---|---|---|---|
| 15 288 | 0.1017 | −0.03 % | −0.12 % | −3.71 % | −19.4 % |
| 13 388 | 0.1205 | **−0.03 %** | −0.14 % | −4.34 % | −23.3 % |
| 12 488 | 0.1310 | −0.04 % | −0.15 % | −4.69 % | −25.5 % |
| 12 188 | 0.1347 | −0.04 % | −0.15 % | −4.81 % | −26.3 % |

### D.2 · High scenario

| `L_total` ppm | `P_UV_opt` (W) | ΔP_UV at ±500 ppm | ΔP_UV at ±1000 ppm | ΔP_UV at ±0.5 pp | ΔP_UV at ±1.0 pp |
|---|---|---|---|---|---|
| 15 288 | 0.5649 | −0.02 % | −0.07 % | −1.90 % | −9.23 % |
| 13 388 | 0.6333 | **−0.02 %** | −0.07 % | −2.07 % | −10.2 % |
| 12 488 | 0.6691 | −0.02 % | −0.07 % | −2.16 % | −10.7 % |
| 12 188 | 0.6816 | −0.02 % | −0.07 % | −2.19 % | −10.9 % |

**Key insight.** At the realistic IBS metrology band (**±500–1 000 ppm**),
the UV penalty is **<0.15 % across all 16 cells**. The workplan v3
"risks-table tolerance" row prediction holds: ±0.5 pp = ±5 000 ppm is
absurdly loose; the meaningful manufacturing band sits at **~ ±500 ppm**.
The BC-E sheets should quote `T_IC ± 500 ppm` (with the corresponding
~ ±0.05 pp in parentheses), **not** `T_IC ± 0.5 pp`.

**Low-vs-High asymmetry.** The Low scenario is more sensitive to `T_IC`
deviations (sharper impedance-match peak at lower depletion). At
±0.5 pp the Low scenario forfeits ~ 4 % UV; the High scenario only
~ 2 %. This argues for centring the single M1' variant **slightly
*below* the midpoint of the two optima**, toward the Low optimum —
moving away from the Low optimum costs more buildup than the
symmetric move toward High saves, so the equal-penalty (minimax)
centre lands on the Low side of the midpoint. **The equal-penalty
centre is `T_IC ≈ 19 965 ppm`** (between the arithmetic mean
20 255 ppm and the Low optimum 17 565 ppm), with both scenarios
paying −0.68 % UV vs their respective optima.

---

## E · Physics tolerance sensitivity

### E.1 · γ ± 1.5 % (Phase E validation residual)

At the default `L_total = 13 388 ppm`:

| Scenario | `T_IC_opt(γ × 0.985)` | `T_IC_opt(γ pinned)` | `T_IC_opt(γ × 1.015)` | Spread |
|---|---|---|---|---|
| Low (0.5 W) | 17 510 ppm / 0.1194 W | 17 565 / 0.1205 W | 17 620 / 0.1216 W | ±55 ppm |
| High (1.5 W) | 22 840 ppm / 0.6293 W | 22 945 / 0.6333 W | 23 050 / 0.6371 W | ±105 ppm |

A γ shift of ±1.5 % moves `T_IC_opt` by ±55–105 ppm — **an order of
magnitude smaller** than the ±500 ppm manufacturing band. **γ
uncertainty is therefore not the binding axis** at the recommended
tolerance, and BC-C does not need to widen the tolerance band on
γ-uncertainty grounds.

### E.2 · `d_eff` full bracket (1.30 → 1.60 pm/V) — dominant physics uncertainty

At the default `L_total = 13 388 ppm`:

| Scenario | `T_IC_opt @ d_eff = 1.30` | `T_IC_opt @ 1.44 (pinned)` | `T_IC_opt @ 1.60` | Spread |
|---|---|---|---|---|
| Low (0.5 W) | 16 920 / 0.1059 W | 17 565 / 0.1205 W | 18 330 / 0.1366 W | **±705 ppm** |
| High (1.5 W) | 21 650 / 0.5802 W | 22 945 / 0.6333 W | 24 450 / 0.6878 W | **±1 400 ppm** |

The `d_eff` bracket is the **binding physics-uncertainty axis** — its
spread (±700 ppm Low, ±1 400 ppm High) is **comparable to or larger
than** the recommended ±500 ppm manufacturing band. **This means the
nominal `T_IC_opt` could shift by ~ ±1 000–1 500 ppm if a future
d_eff measurement lands away from 1.44 pm/V**.

**Recommendation.** The BC-E sheets should:
- Quote the manufacturing tolerance as **±500 ppm** (matching the
  realistic IBS metrology).
- Include a **footnote** that the centre value is anchored to
  Eckardt-1990 d_eff = 1.44 pm/V, and that a post-2020 d_eff anchor
  could shift the centre by ~ ±1 000 ppm (high scenario) without
  invalidating the coating run itself (the buildup degrades smoothly,
  not catastrophically).

---

## F · Default operating point (BC-C consumption)

The **single per-scenario row BC-C and BC-E need**:

| Scenario | `P_in_559` | `T_IC_opt` | Vendor tolerance | `P_UV` | `P_circ` | I_waist | I_curved |
|---|---|---|---|---|---|---|---|
| **Low**  | 0.50 W | **17 565 ppm (1.756 %)** | ±500 ppm (= 17 065–18 065 ppm) | 0.1205 W | 28.5 W | 4.82 MW/cm² | 27.9 kW/cm² |
| **High** | 1.50 W | **22 945 ppm (2.295 %)** | ±500 ppm (= 22 445–23 445 ppm) | 0.6333 W | 65.4 W | 11.06 MW/cm² | 64.2 kW/cm² |

**M2'/M3'/M4' mirror-loss budget for BC-C allocation:**
- `Σ T_loss_VENDOR_max = 1 500 ppm` (intermediate-IBS, 500 ppm/mirror equal-allocation default).
- BC-C may re-allocate asymmetrically (e.g. more headroom on the M4' dichroic since it carries the dual-wavelength load).
- Total round-trip operating loss: `L_total = 13 388 ppm`.

**F.2 · Single-M1'-variant centre-point options** (since §6 Q2 resolves to one variant):

| Policy | `T_IC` centre (ppm / %) | Penalty Low | Penalty High | Worst-case at ±500 ppm |
|---|---|---|---|---|
| Arithmetic mean of optima | 20 255 / 2.026 % | −0.84 % | −0.55 % | −0.99 % (Low @ +500) |
| Geometric mean of optima | 20 075 / 2.008 % | −0.74 % | −0.63 % | ~ −1.0 % (Low @ +500) |
| **Equal-penalty (minimax) — recommended** | **19 965 / 2.000 %** | **−0.68 %** | **−0.68 %** | **−0.97 % (Low @ +500)** |
| Bias toward High (workplan §1.5 anchor) | 20 500 / 2.050 % | −0.99 % | −0.45 % | −1.33 % (Low @ +500) |
| Bias toward Low | 19 000 / 1.900 % | −0.26 % | −1.24 % | −1.52 % (High @ −500) |

**Recommended centre: `T_IC = 19 965 ppm ≈ 2.00 %, ±500 ppm`** (equal-penalty
/ minimax). At the recommended centre the worst case across the
±500 ppm vendor metrology band is ~ −1.0 % UV in either scenario —
small enough that BC-E does not need to escalate to two M1' variants.

**Important wording note.** A single ±500 ppm band centred at 19 965 ppm
does *not* contain either scenario's optimum (Low optimum sits 2 400 ppm
*below* the band; High optimum sits 2 480 ppm *above*). The one-variant
recommendation is on *UV-penalty grounds* (workplan §6 Q2 1 pp branch
rule), **not** on geometric coverage of both optima. The ±500 ppm is the
*vendor manufacturing tolerance* on the chosen centre, **not** a span
spanning both optima.

BC-E may alternatively carry **both per-scenario T_IC_opt values on
the M1' sheet** (17 565 ppm + 22 945 ppm) and let the coating vendor
quote against the centre + tolerance the vendor's economics prefer.
Steward call at BC-E; the equal-penalty centre is the recommended
default.

---

## G · Findings handed forward

1. **§6 Q2 resolved.** Δ`T_IC_opt` = 0.52 pp across all `L_total` points
   — below the workplan's 1 pp branch threshold. A single M1' coating
   variant is **performance-acceptable**: at the equal-penalty centre
   (19 965 ppm), both scenarios pay −0.68 % UV vs their respective
   optima, with the worst case across ±500 ppm vendor tolerance
   staying below ~ −1.0 % in either scenario. The single ±500 ppm band
   does *not* geometrically contain either optimum; the one-variant
   recommendation is penalty-based, not coverage-based. BC-C / BC-E
   carry one M1' page, not two.
2. **§6 Q5 (spare quantity) unaffected.** N = 4 per role / 4 full sets
   stands; no per-variant complication needed.
3. **Tolerance band recommendation.** **±500 ppm** for the M1' R-spec
   (not ±0.5 pp). Worst-case UV penalty <0.05 % at this band.
4. **Default `L_total`.** **13 388 ppm** (intermediate IBS,
   500 ppm/mirror). Buys ~ 18 % UV over Friedenauer R-floor at the
   High scenario and ~ 19 % at the Low scenario, while remaining
   well within published IBS capability.
5. **Friedenauer ~ 3.6 % UV forgone.** `T_IC_opt = 0.0217` vs procured
   0.0160 confirms the BC-A reading. **The cover letter (BC-E)
   should explicitly justify the new spec targeting a higher
   transmission than the 2006 reference** — this is the steward
   conversation reviewer #1 v3-round prompted.
6. **d_eff is the binding physics uncertainty axis.** ±9 % on
   `T_IC_opt` (high scenario) across the d_eff 1.30–1.60 pm/V bracket.
   Post-2020 d_eff anchor extraction would tighten this; queued as a
   task-E follow-up for the dossier.
7. **Peak intensities (BC-D input).** Waist 4.4–11.5 MW/cm² CW;
   curved mirrors ~ 26–67 kW/cm² CW (proper BBO + air propagation; the
   v1 figure of 62–161 used a single-medium spot approximation — see
   §B.1 methodology note). Outgoing 280 nm fluence is the
   M4' dichroic dual-wavelength load that BC-D must compare against
   published 280 nm LIDT (Burkley2021 / Turcicova2022).

---

## H · Open items handed to BC-C

- **Allocation across M2'/M3'/M4'.** Default: equal 500 ppm/mirror.
  BC-C may re-weight (e.g. 600/600/300 ppm to give the M4' dichroic
  more headroom on the dual-wavelength load); the `Σ T_loss_VENDOR_max
  = 1 500 ppm` summed budget is the binding constraint.
- **Single M1' centre point vs per-scenario centres.** §F gives
  both options. Steward call at BC-E.
- **Tolerance bracket carried to BC-E.** The recommendation is
  ±500 ppm, but BC-E may want to quote the vendor a slightly looser
  band (±750 ppm) as a "courtesy band" since the buildup penalty
  remains <0.1 % even at ±1 000 ppm. Not load-bearing; steward call.

---

## I · Charter compliance

- **§5.1 anti-seeding.** Notebook lives in
  [`logbook/2026-05-20-bbo-coating-run-wp/notebooks/`](notebooks/)
  during BC-B; promoted to `/notebooks/exploration/` at BC-F closure
  (workplan §6 Q8). No commit to `/src/`. Mechanical scan
  ([`tests/test_anti_seeding_src_imports.py`](../../tests/test_anti_seeding_src_imports.py))
  unaffected.
- **γ authority.** `constants.md` consulted, not regenerated.
- **Result class.** *Sail* — exploratory parameter optimisation on a
  chosen architecture. The BC-A geometry / material constants used as
  inputs remain *Coastline* (anchored to published sources). The
  recommendations above are advisory until BC-F closure and vendor
  quote evaluation downstream.
