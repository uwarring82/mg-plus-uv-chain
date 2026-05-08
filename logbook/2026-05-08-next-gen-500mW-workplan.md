# Next-generation UV source — 500 mW @ 280 nm via two SHG stages — workplan

**Steward:** Ulrich Warring
**Date:** 2026-05-08
**Status:** DRAFT (planning artefact; no architecture-specific code yet)

## Header (Charter §9 trigger questions)

- **Affects Level 0 parameter?** no — Level 0 (ion-side detuning, two-photon Rabi rate, allowed scattering) was locked at the G3 closure on 2026-05-01 and is unchanged here.
- **Affects Level 1 parameter?** no — Level 1 (UV power at experiment input, beam quality, source linewidth) targets stay derived from Level 0 + the loss budget. The 500 mW figure is the *indicative anchor* of CHARTER §1.5 and is not being moved.
- **Affects success criterion?** no — same indicative anchor; success criteria are unchanged.

This plan therefore does not require Council-3 deliberation. It is **architecture-specific exploration**, so all numerical work lives in `/notebooks/` (per CHARTER §5.1 anti-seeding clause); architecture-family-specific simulation under `/src/architecture/` remains G1-blocked. The plan respects this boundary throughout.

---

## 1 · Goal

Identify a parameter set for an all-solid-state CW two-stage SHG chain
1118 nm → 559 nm → 280 nm that delivers ≥ 500 mW at the UV output, given
the Phase 0.5 reference triple (`Δ_ref = 40 GHz`, `Ω_R/2π = 400 kHz`,
`Γ_sc = 2.0×10⁴ s⁻¹`) and the as-built Friedenauer 2006 architecture as
the starting point.

The deliverable is **not** a build decision. It is a *parameterised
recommendation set* — pump power, IC reflectivities per stage, crystal
length and waist per stage, passive-loss budget, and the coating
specifications they imply — together with the sensitivity envelope around
each value. Build/buy decisions sit downstream and depend on G1, G2, and
the dossier closures already tracked elsewhere.

The 500 mW figure is the CHARTER §1.5 indicative anchor. The binding
form remains the Level-0 constraint row (Ω_R, Δ, S_φ(f)); this workplan
checks that the indicative figure is reachable without forcing the build
into a corner of parameter space we cannot defend.

---

## 2 · Constraints

- **CHARTER §5.1 anti-seeding (mechanically enforced).** No Boyd–Kleinman
  optimisation, impedance-matching computation, or parameter sweep on a
  candidate architecture lands in `/src/`. All work is in
  `/notebooks/diagnostic/` or `/notebooks/exploration/` and uses the
  architecture-neutral primitives in `/src/{boyd_kleinman,
  shg_single_pass, enhancement_cavity, shg_cascade}.py` plus the
  parameter values in `/data/literature/` or per-notebook YAML.
- **G1 still open.** The 14 GHz unlockable domain (Friedenauer §4) is
  unattributed; no architecture-family-specific code lands in `/src/`
  until G1 closes. Workplan output is recommendations, not committed
  simulation.
- **G2 still open.** UV-induced degradation is uncharacterised. Coating-
  loss and BBO LIDT bounds entering this plan come from the existing
  literature (Tamosauskas2018, Burkley2021, Brown2019) and are flagged
  as G2-dependent.
- **SI throughout** per `CONVENTIONS.md` §1; all units explicit.
- **Validation against Phase E.** Every cascade computation in this plan
  is consistent with the Phase E Friedenauer cross-check; if a phase of
  this plan changes the cross-check residual outside its envelope, that
  phase pauses for resolution.

---

## 3 · Existing primitives (already in `/src/`, ready to consume)

The numerics-expansion workplan
([`logbook/2026-05-07-numerics-expansion-workplan.md`](2026-05-07-numerics-expansion-workplan.md))
landed everything this plan needs:

- `boyd_kleinman.py` — `h_m_factor(ξ, β, κ, ζ, μ)`, `h_m_optimum(...)`.
- `shg_single_pass.py` — `gamma_shg_coefficient(d_eff, n_ω, n_2ω, λ, L, h_m)` and the `single_pass_{harmonic_power_W, conversion_fraction}` pair.
- `enhancement_cavity.py` — `circulating_power`, `harmonic_output_W`, `optimal_input_coupler` (depleted-regime, exact `−L·η_nl` cross term).
- `shg_cascade.py` — `Stage`, `cascade_output`, `optimise_cascade` (exact one-way-coupling factorisation).
- `tests/` — 142 tests green covering the above.

Phase E ([`notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py))
showed the BBO stage agrees with Friedenauer 2006 to 1.5 %; the LBO stage
exposed an `L_passive` definitional gap which is the first item this plan
must close before parameter sweeps are meaningful.

---

## 4 · Phase plan

### Phase NG-A · Close the LBO `L_passive` gap from Phase E

**Why.** Phase E found the LBO stage at 0.702 W vs the published 0.950 W
(−26 %), most likely because Friedenauer's reported `T_IC = 0.025` is the
*impedance-matched* transmission (already including the nonlinear
conversion load), not the bare passive loss. Until that is separated,
every LBO sweep is anchored to a wrong loss number.

**Deliverables.**
- A revised entry in `data/literature/Friedenauer2006/extracted.yaml`
  separating `T_IC_at_match` (= 0.025, paper-stated) from
  `L_passive_inferred` (computed self-consistently from the published
  efficiency and `η_nl(P_circ_at_match)`).
- A short logbook entry recording the inference and the residual
  uncertainty (since the paper is silent on `L_passive` directly).
- Phase E notebook re-run with the new `L_passive` value; LBO discrepancy
  expected to drop into single digits.

**Acceptance.** Phase E LBO recomputed within 5 % of the published 0.95 W;
the BBO 1.5 % agreement holds.

**Effort.** ~ 0.5 day.

### Phase NG-B · Forward map: 500 mW UV → required pump

**Why.** Before sweeping, set the order-of-magnitude scale so that
parameter sweeps in NG-C/D operate on a defensible interval.

**Deliverables.**
- Notebook `notebooks/exploration/2026-05-MM-pump-required-vs-uv-target.py`.
- Plot of required input pump (1118 nm) vs UV target output, for a grid of
  cascade efficiencies `η_cascade ∈ [0.10, 0.30]`. Friedenauer-2006
  efficiency (`η ≈ 0.15`) sits as one anchor; impedance-matched LBO + BBO
  with realistic coating-loss budgets gives an upper anchor.
- A back-of-the-envelope "target pump for 500 mW UV at η_cascade = X" table.

**Acceptance.** Two anchored scenarios — *Friedenauer-class* and
*coating-best-case* — with 500 mW UV crossing for each.

**Effort.** ~ 1 day.

### Phase NG-C · IC reflectivity sweep per stage at fixed crystal geometry

**Why.** This is the user's headline question: "what input-coupler
reflectivity should the next coating run target?" Tutorial 03 already
answers it for one stage; here we apply it to both stages of the cascade
under the *exact* one-way-coupling factorisation (Phase C result).

**Deliverables.**
- Notebook `notebooks/exploration/2026-05-MM-ic-reflectivity-sweep.py`.
- For each of N pump levels (e.g. 1.5, 2, 3, 4, 5 W at 1118 nm) and a
  fixed crystal geometry (Friedenauer-class L_LBO = 18 mm, w0_LBO =
  27.3 µm; L_BBO = 10 mm, w0_BBO = 19.4 µm), report:
  - `T_IC_LBO_opt(P_in)` and `T_IC_BBO_opt(P_h_LBO · η_transport)`
  - cascade UV output and total efficiency
  - sensitivity bracket: `T_IC ± 0.5 pp`, `L_passive ± 0.5 pp`,
    `γ_SHG ± 20 %` (matching Tutorial 03 sensitivity convention)
- Identify the smallest pump that hits 500 mW UV under each loss budget.

**Acceptance.** A figure mapping `(P_in, T_IC_LBO, T_IC_BBO) → P_UV` with
500 mW contours overlaid; tabulated recommended `T_IC` per stage at the
chosen pump.

**Effort.** ~ 1.5 days.

### Phase NG-D · Crystal-geometry sweep (length, waist, oven temperature)

**Why.** Friedenauer's `w0 = 27.3 µm` is the BK optimum for `L = 18 mm`.
Different lengths shift the optimum; a longer LBO (more conversion) can
improve total efficiency if the cavity loss budget supports it.

**Deliverables.**
- Notebook `notebooks/exploration/2026-05-MM-crystal-geometry-sweep.py`.
- For LBO: vary `L ∈ [10, 25] mm` with `w0 = w0_BK_opt(L, β=0)` from
  `boyd_kleinman.h_m_optimum`; recompute γ_SHG and re-optimise the cavity.
  Plot UV output vs crystal length.
- For BBO: same, but with the walk-off-aware BK optimum (β > 0 from
  Eimerl 1987 walk-off `ρ`); document the sensitivity of `h_m` to
  walk-off at each length.
- Identify whether deviating from Friedenauer's `(L, w0)` choices buys
  anything within achievable ovens / vendor stock dimensions.

**Acceptance.** A short narrative answer: *"The Friedenauer crystal
choices are within X % of the BK + cavity optimum at our pump scale; a
longer LBO buys Y % efficiency at cost Z."* — with the figures backing
each claim.

**Effort.** ~ 1.5 days.

### Phase NG-E · Loss-budget anchoring

**Why.** Phases NG-C/D treat `L_passive` as an input. The achievable
`L_passive` is set by coating runs and crystal coatings; Tamosauskas2018
and Burkley2021 bound the available reflectivities. This phase couples
the parameter sweeps to the procurement reality.

**Deliverables.**
- A short table in the workplan documenting the loss budgets achievable
  for IBS-coated 1118 nm and 559 nm cavity mirrors (with citations).
- An update to `data/literature/Friedenauer2006/extracted.yaml`-style
  entry under `data/literature/` (e.g.
  `Tamosauskas2018-coating-loss-budgets.yaml`) recording the bounds.
- Notebook update plotting UV-output islands corresponding to the
  vendor-achievable `L_passive` ranges.

**Acceptance.** A defensible upper bound on cascade efficiency given
realistic coatings; a notation of which loss-budget item is *binding* at
500 mW UV.

**Effort.** ~ 1 day.

### Phase NG-F · Synthesis: recommended parameter table + sensitivity

**Why.** The deliverable of this whole plan.

**Deliverables.**
- One-page recommendation in `docs/architectures/next-gen.md` containing:
  - Pump power required at 1118 nm (with 80 % confidence interval).
  - Per-stage `(L_passive, T_IC, L_crystal, w0, T_oven)` recommendation.
  - Cascade UV output at the recommendation point.
  - Robustness envelope: how much of each parameter can drift before
    UV output falls below 80 % of target.
  - Open-items list: which `data/literature/` entries are binding inputs
    and need refresh; which dossier KD entries close to validate the
    recommendation.
- A logbook closure entry pointing to the notebooks and the
  `architectures/next-gen.md` row that landed.

**Acceptance.** The recommendation is internally consistent with NG-A
through NG-E and is stated with explicit confidence bands rather than
single-point numbers.

**Effort.** ~ 1 day.

### Phase NG-G · Documentation surface

**Deliverables.**
- `docs/architectures/next-gen.md` page populated with the synthesis
  output and links to the notebooks.
- Cross-link from `docs/architectures/friedenauer-2006.md` ("This is
  what the *next* generation must beat").
- One sentence in `docs/principles.md` clarifying that Phase NG-* work
  lives in `/notebooks/exploration/` and is not Phase 4 scoring input.

**Effort.** ~ 0.5 day.

---

## 5 · Effort sketch

| Phase | Deliverable | Effort | Dependencies |
|---|---|---|---|
| NG-A | LBO `L_passive` gap closed; Phase E re-run | 0.5 day | Phase E (done) |
| NG-B | Pump-vs-UV-target forward map | 1 day | NG-A |
| NG-C | Per-stage IC reflectivity sweep | 1.5 days | NG-A, NG-B |
| NG-D | Crystal geometry sweep | 1.5 days | NG-A |
| NG-E | Loss-budget anchoring | 1 day | NG-C |
| NG-F | Synthesis + sensitivity | 1 day | NG-A through NG-E |
| NG-G | Documentation | 0.5 day | NG-F |
| **Total** | | **~ 7 days focused** | |

Realistic calendar window: **2 weeks** with normal task-switching
overhead and time for the loss-budget reading list to be re-read.

---

## 6 · Open design questions for steward decision

1. **Architecture topology.** Stay with LBO + BBO (Friedenauer
   topology) for the first iteration of this plan, or also evaluate
   alternatives (PPLN-MgO + BBO, PPKTP + BBO, single-pass BBO with
   build-up only at 559 nm)? **Recommendation:** stay LBO + BBO for
   NG-A through NG-E; add an "alternative-topologies" Phase NG-H as a
   separate workplan when NG-G closes. Keeps this workplan testable.
2. **Pump source.** Friedenauer used a 2 W Yb fibre laser at 1118 nm
   with `Δν < 200 kHz` and ~ 1.2 W ASE. NG-B's pump scaling assumes a
   linear extension of the same source class. If a higher-power Yb
   source is on the table (4–10 W class), how does the ASE budget
   scale? Out of NG scope; logged as a follow-up.
3. **`L_passive` for the next-gen build.** Friedenauer ran with
   ≥ 99.98 % HR mirrors. For the next-gen build, do we target the same
   loss budget (cheaper, well-trodden) or push to the Tamosauskas2018
   IBS-coating envelope (lower loss, higher buildup, but a coating-run
   commitment)? **NG-E should answer this; flag here as a steward
   decision once NG-E lands.**
4. **G1 dependency.** The 14-GHz unlockable domain is unresolved;
   re-using the Friedenauer cavity geometry inherits its risk. Does the
   NG plan pause for a G1 attribution before moving from "parameter
   recommendation" to "build decision"? **Charter says yes** — Phase 4
   architecture comparison is gated. The recommendation that closes
   NG-G is Phase 4 *input*, not Phase 4 *output*.

---

## 7 · Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Anti-seeding violation through architecture-specific code in `/src/` | Low | Existing `tests/test_anti_seeding_src_imports.py` mechanical scan; all NG-* notebooks live in `/notebooks/exploration/` |
| Phase E LBO gap not actually due to `L_passive` | Medium | NG-A explicitly tests the hypothesis; if false, NG-A pauses for re-extraction rather than continuing on a wrong baseline |
| Crystal walk-off mishandled at depleted regime | Low | `boyd_kleinman.h_m_factor` already handles `β > 0`; NG-D cross-checks against the Eimerl walk-off used in Phase E |
| Loss-budget literature stale at the operating wavelengths | Medium | NG-E documents specific sources and dates; flagged as G2-dependent |
| Parameter sweep finds 500 mW unreachable at any sensible pump | Low (per Phase E) | Document the constraint that's binding and feed back to CHARTER §1.5 indicative anchor — but Phase E's BBO efficiency suggests this is comfortably reachable |
| Recommendation conflicts with G1 attribution when it eventually lands | Medium | Recommendation explicitly flags the cavity-geometry inheritance from Friedenauer as a G1-dependent assumption; G1 closure may force NG re-run |

---

## 8 · Acceptance criteria for "done"

Plan is closed when:

1. Phase E re-run with the corrected `L_passive` agrees with the
   published 0.95 W LBO output to within 5 %.
2. Notebooks under `notebooks/exploration/` produce a defensible
   recommended parameter table at 500 mW UV target, with sensitivity
   envelopes documented.
3. `docs/architectures/next-gen.md` carries the recommendation and the
   open items, in human-readable form, and is linked from the site nav.
4. The recommendation is consistent with Phase E (BBO 1.5 % agreement
   maintained) and respects the loss-budget bounds anchored in NG-E.
5. The `tests/test_anti_seeding_src_imports.py` mechanical scan still
   passes 142/142.

---

## 9 · Out of scope

- **Architecture-family-specific simulation in `/src/`.** G1-blocked.
- **Phase 4 architecture scoring.** This plan produces *inputs* to Phase
  4 scoring, not the scoring itself.
- **Build / buy decisions.** Recommendation is parameterised, not
  committed.
- **Alternative cascade topologies** (single-stage UV, OPO-based,
  intracavity SHG, …). Logged for a separate workplan after NG-G closes.
- **Pump-source-class change** (higher-power Yb, VECSEL, …). Same; out
  of scope, logged for follow-up.
- **UV-degradation modelling.** G2-dependent, separate workplan.
- **Phase-noise budget** flow to Δω_R. Lives in Phase 0.5; not part of
  this plan.

---

## 10 · Pre-conditions (state at plan opening)

- Numerics-expansion workplan
  ([`logbook/2026-05-07-numerics-expansion-workplan.md`](2026-05-07-numerics-expansion-workplan.md))
  closed. Phases A–G done; 142/142 tests green; tutorials live on the site.
- Phase E Friedenauer cross-check executed; results recorded in §10 of
  the numerics-expansion workplan.
- CHARTER §1.5 reference triple locked at G3 closure.
- G1 OPEN; G2 OPEN; G3 CLOSED.
