# Numerics-package expansion — workplan

**Steward:** Ulrich Warring
**Date:** 2026-05-07
**Status:** DRAFT v1.1 — revised after peer review (2026-05-07). Planning artefact only; no code yet committed under this plan.
**Baseline:** `pytest -q` reports `78 passed` at the parent commit, verified during peer review on 2026-05-07.

## Header (Charter §9 trigger questions)

- **Affects Level 0 parameter?** no — generic SHG / cavity primitives only.
- **Affects Level 1 parameter?** no — primitives are wavelength- and architecture-neutral; the *application* of the primitives to an architecture remains G1-gated.
- **Affects success criterion?** no.

Plan therefore does not require Council-3 deliberation. Any *use* of the primitives that locks an architecture-specific parameter still requires the existing Charter §9 footers.

---

## 1 · Goal

Add a generic, architecture-neutral toolkit that lets us answer:

> *"Given a single pump power, an estimate of round-trip passive loss, and a single-pass SHG efficiency coefficient — what is the optimal input-coupler reflectivity, and what harmonic output does that produce?"*

…with both the **closed-form analytical limit** (small-signal Polzik–Kimble) and the **numerical solver** for the saturated regime, plus tutorial notebooks that explain the principles to a visitor approaching the page from outside the field.

The same primitives must also support the cascaded LBO → BBO problem and the open inventory questions ("what reflectivity should the next IC coating run target?").

---

## 2 · Constraints

- **Anti-seeding (CHARTER §5.1).** Pre-G1, no architecture-specific code may land in `/src/`. All new modules are wavelength-, material-, and architecture-neutral. Architecture-specific *applications* (Friedenauer reproduction, BBO at 559 nm) live exclusively under `/notebooks/`.
- **SI contract (CONVENTIONS §1; `src/parameters.py`).** All inputs / outputs SI; variable names carry units where ambiguous (`power_W`, `wavelength_m`, `loss_per_pass`).
- **Test-suite invariant.** Existing 78 / 78 baseline must remain green at every commit. New modules ship with their own tests.
- **No new heavy dependencies** beyond the existing `numpy` / `scipy` / `matplotlib` stack unless the new requirement is justified in the commit message.

---

## 3 · Existing primitives (already in `/src/`)

- [`src/parameters.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/parameters.py) — SI-units contract, CODATA 2018 constants, Phase 0.5 reference triple.
- [`src/boyd_kleinman.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/boyd_kleinman.py) — generic `h(σ, β, κ, ξ, μ)`, σ-optimised `h_m(β, κ, ξ, μ)`, and the analytic limit `h_m^∞ = 1.068` at `ξ_opt ≈ 2.84`.
- [`src/abcd.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/abcd.py) — ABCD matrices, Gaussian-beam q-parameter, stability test, ring-cavity eigenmode.

These give us the **focused-Gaussian SHG efficiency** and the **cavity geometry**. What is *missing* — and the focus of this workplan — is the **bridge between them**: single-pass conversion efficiency expressed as an actual coupling coefficient `γ_SHG` (W⁻¹), and the steady-state enhancement-cavity equation that uses it.

---

## 4 · Phase plan

### Phase A · Single-pass SHG coupling — `src/shg_single_pass.py` ✅ **DONE 2026-05-07** (commit `8296fff`; 78 → 91 tests green)

**Goal.** Convert the Boyd–Kleinman dimensionless focusing factor (`h_m_factor`
in `src/boyd_kleinman.py`) into the engineering coefficient `γ_SHG` (units W⁻¹)
and derive *both* the harmonic power and the single-pass conversion fraction
from it:

```
P_2ω,single-pass = γ_SHG · P_ω²                                (small-signal, W)
P_2ω,single-pass = P_ω · tanh²(√(γ_SHG · P_ω))                 (depleted, W)
η_SP             = P_2ω,single-pass / P_ω                       (fraction in [0, 1]; consumed by the cavity solver)
```

**API design note (peer-review consensus).** The Phase A API does *not*
re-introduce the BK walk-off parameter `β`; that responsibility stays in the
BK layer.

- BK layer (`src/boyd_kleinman.py`) owns *all* focusing geometry — including
  walk-off, absorption, and focal-position offsets — and returns the
  dimensionless `h_m`.
- SHG layer (`src/shg_single_pass.py`) owns material / wavelength coupling
  and *consumes* `h_m`.
- Notebook authors precompute `h_m = boyd_kleinman.h_m_factor(xi, beta, ...)`
  and pass it in. Any one-stop convenience wrapper lives in notebooks, not
  in `/src/`.

This split prevents the silent-double-count failure mode of the earlier draft
signature `gamma_shg_coefficient(..., h_m, walk_off_angle_rad=0.0)`, where one
of the two arguments was always dead.

**Deliverables.**
- `gamma_shg_coefficient(d_eff_mV, n_omega, n_2omega, wavelength_m, length_m, h_m)` → `float` (W⁻¹). Takes the dimensionless BK factor as an explicit input; **no walk-off argument**.
- `single_pass_harmonic_power_W(power_in_W, gamma_shg, regime="auto")` → `float` (W). Returns `γ P²` (small-signal) or `P · tanh²(√(γP))` (depleted). `"auto"` switches at the 5 % conversion threshold; `regime` may be forced to `"small"` or `"depleted"` for didactic plots.
- `single_pass_conversion_fraction(power_in_W, gamma_shg, regime="auto")` → `float` (dimensionless, in `[0, 1]`). Equal to `single_pass_harmonic_power_W / power_in_W`. **This is the function the cavity solver in Phase B consumes** — it is *not* simply `γ · P²` outside the small-signal regime.
- Internal helper: `boyd_kleinman_K_factor(d_eff_mV, n_omega, n_2omega, wavelength_m)` (the material constant `K` in `P_2 = K · L · k₁ · h · P_1²`) factored out so notebooks can introspect the prefactor.

**Tests (`tests/test_shg_single_pass.py`).**
- Dimensional analysis: `γ_SHG` returns SI W⁻¹ for SI inputs.
- Small-signal harmonic limit: `single_pass_harmonic_power_W(P, γ, "small")` → `γ P²`.
- Small-signal fraction limit: `single_pass_conversion_fraction(P, γ, "small")` → `γ P`.
- Saturated harmonic limit: `tanh²(√(γP)) → 1` as `γP → ∞`; `single_pass_harmonic_power_W → P` (no overshoot, Manley–Rowe respected).
- Saturated fraction limit: `single_pass_conversion_fraction → 1` as `γP → ∞`.
- Cross-check vs `boyd_kleinman.h_m_factor` at `ξ_opt ≈ 2.84`, `β = κ = μ = 0`: recover the textbook `K · L · k₁ · 1.068` to numerical precision.
- Energy conservation: `single_pass_harmonic_power_W(P, γ) ≤ P` for all `γ > 0` and `P > 0`.

### Phase B · Enhancement-cavity steady state — `src/enhancement_cavity.py` ✅ **DONE 2026-05-07** (commit `232e3d5`; 91 → 119 tests green)

**Implementation refinements** (compatible with v1.1 design; recorded for the audit trail):

- **Adaptive `T_high` in `optimal_input_coupler`.** For highly-depleted
  regimes (`γ P_in ≳ 10`), `T_match` approaches 1 so closely that a fixed
  `T_high = 1 − 1e-6` cannot bracket the root. The solver now expands
  `T_high → 1` in decade steps until the residual flips sign.
- **Cavity-level Manley–Rowe clamp in `harmonic_output_W`.** The brentq
  cavity solver and Phase A's `tanh²` short-circuit (at `γP > 700`) compound
  to a ~1e-13 floating-point overshoot above `P_in` in the saturated
  regime. A `min(p_h, power_in_W)` clamp at the cavity output enforces
  the physical ceiling exactly. The clamp is a no-op in linear and
  small-signal regimes.
- **Saturated-regime graceful fallback.** When `T_match → 1` within
  machine precision (single-pass conversion ≈ 100 %), the solver returns
  `T_high` rather than raising — cavity enhancement is degenerate but
  the output is well-defined.
- **Test tolerance on the linearised quadratic oracle.** The oracle
  assumes `η_nl = γ P_circ` exactly while the solver uses depleted
  `tanh²`. Leading-order correction is `~γ P_circ / 3`, so the test
  uses `rel=1e-2` at `γ P_circ ≈ 0.02` (the operating point of the
  test) and `rel=1e-3` for a deep-small-signal companion test where
  `γ P_circ < 1e-3`.

**Goal.** Solve the impedance-matching equation for an SHG ring cavity with
passive loss `L_passive` and a *single-pass conversion fraction*
`η_nl(P_circ) = single_pass_conversion_fraction(P_circ, γ_SHG)` from Phase A:

```
P_circ / P_in = T_IC / (1 − √(R_IC · (1 − L_passive) · (1 − η_nl(P_circ))))²
```

The intensity-form (large-finesse) impedance-matching condition is

```
T_IC,match = 1 − (1 − L_passive)(1 − η_nl)  =  L_passive + η_nl − L_passive · η_nl
```

— the cross term `− L_passive · η_nl` is the difference between the exact
match and the linearised expression `T = L + η_nl`. For Friedenauer-LBO-class
parameters (`L ≈ 0.005`, `η_nl ≈ 0.5`) the cross term shifts the match by
`≈ 0.25 percentage points` of `T_IC`; small but well above solver tolerance.

**Peer-review correction to high-pump scaling.** In the linearised small-signal
regime `η_nl = γ P_circ`, combining with `P_circ ≈ P_in / T_IC` gives the
quadratic `T² − L_passive · T − γ P_in = 0`, so

```
T_IC,opt(small-signal)  =  ½ [ L_passive + √(L_passive² + 4 γ P_in) ]
```

and the high-pump leading order is `T_IC,opt → √(γ P_in)` — **no `L_passive`
under the radical**, contra the original draft's `√(γ P_in L_passive)`.

**Deliverables.**
- `circulating_power(power_in_W, T_IC, loss_per_pass, gamma_shg)` → `float`. Transcendental solver via `scipy.optimize.brentq` on the residual of the cavity equation; supports `gamma_shg = 0` for the purely passive cavity. Internally uses Phase A's `single_pass_conversion_fraction` (regime auto-selected) — *not* a hard-coded `γ · P²` term, which would silently fail in the depleted regime.
- `harmonic_output_W(power_in_W, T_IC, loss_per_pass, gamma_shg)` → `float` (W). Returns `single_pass_harmonic_power_W(P_circ, γ)` evaluated at the converged circulating power. Valid in both small-signal and depleted regimes.
- `optimal_input_coupler(power_in_W, loss_per_pass, gamma_shg)` → `float`. Self-consistent Polzik–Kimble solver over the *exact* intensity-form match (including the `− L · η_nl` cross term and the depleted-regime fraction). Returns the impedance-matched `T_IC`.
- `passive_buildup(T_IC, loss_per_pass)` → `float` — closed-form passive-cavity buildup as a debugging primitive.

**Tests (`tests/test_enhancement_cavity.py`).**
- Passive limit: with `gamma_shg = 0` and `T_IC = L_passive`, the cavity equation gives `P_circ / P_in = 1 / L_passive` (Airy maximum at impedance match).
- Small-signal **linearised-loss** closed form (peer-review reviewer-3 labelling): `optimal_input_coupler(P_in, L, γ)` agrees with `½ [L + √(L² + 4γP_in)]` for `γP_in ≪ 1`. *This is the linearised-loss oracle*, not the exact-cross-term form. The exact intensity-form quadratic is `T² − L T − (1 − L) γ P_in = 0` (the `(1 − L)` factor on the pump term comes from carrying the `(1 − L)(1 − η_nl)` cross product through the match condition). Both forms agree to leading order in the small-signal limit; the difference appears at `O(L · γ P_in)` and is captured by the dedicated cross-term test below. Test the high-pump leading-order coefficient *with no `L` under the radical*.
- Low-pump limit: `T_IC,opt → L_passive + γ P_in / L_passive` for `γ P_in ≪ L_passive²`.
- High-pump limit: `T_IC,opt → √(γ P_in)` for `γ P_in ≫ L_passive²` (independent of `L_passive` to leading order).
- Cross-term presence (Friedenauer-LBO regime): with `L_passive = 0.005` and a circulating power giving `η_nl = 0.5`, the exact match `T_IC = 0.005 + 0.5 − 0.005·0.5 = 0.5025` differs from the linearised value `0.5050` by 0.25 pp; solver must reproduce the exact value within `< 1e-6`.
- Round-trip energy conservation: `P_in = (1 − T_IC) · P_circ,reflected + L_passive · P_circ + harmonic_output_W(...)` within solver tolerance.
- Manley–Rowe ceiling: `harmonic_output_W ≤ P_in` (the per-photon energy ratio for SHG is 2:1 but the *power* ratio is bounded by 1; tighter Manley–Rowe bound is `harmonic_output_W ≤ P_in`).
- Depleted regime: with parameters chosen so that `η_nl(P_circ) > 0.4`, the solver must not blow up and the result must agree with a direct `tanh²` evaluation at the converged `P_circ` to numerical precision.

### Phase C · Cascade composition — `src/shg_cascade.py` ✅ **DONE 2026-05-07** (commit `b820214`; 119 → 142 tests green)

**Sharpened during implementation** (compatible with v1.1; recorded for the audit trail):

- **Optimum factorisation is exact, not just small-signal.** The workplan
  framed the cascade optimum as factorising "in the small-signal limit".
  Implementation showed the property is regime-independent: differentiating
  the cascade harmonic with respect to T_1 gives `dP_h2/dT_1 =
  (∂P_h2/∂P_h1)·(dP_h1/dT_1) + (∂P_h2/∂T_2)·(dT_2*/dT_1)`, the second
  term vanishes at the local stage-2 optimum (∂P_h2/∂T_2 = 0 by
  definition), and ∂P_h2/∂P_h1 > 0 always — so the cascade-optimum
  condition reduces to `dP_h1/dT_1 = 0` regardless of regime. This
  follows from the cascade being one-way coupled (stage 2 cannot feed
  back into stage 1). The strong form is captured in
  `test_stage_1_optimum_independent_of_stage_2_params`, which sweeps
  stage 2's gamma over 4 decades and confirms stage 1's optimum is
  identical (rel < 1e-12) at every point.
- **Return shape: `dict` with `per_stage` list + totals.** Matches the
  workplan; `into_next_stage_W` is `None` (not `0.0`) for the last
  stage to make the cascade boundary unambiguous.
- **`Stage` is `frozen=True`.** Hashable; optimiser-returned instances
  can't be mutated by accident downstream.

**Goal.** Compose two `enhancement_cavity` stages with a transport efficiency `η_transport` between them, so the LBO → BBO chain is a one-call object.

**Deliverables.**
- `Stage` dataclass holding `(loss_per_pass, gamma_shg, T_IC)`.
- `cascade_output(power_in_W, stages, transport_efficiencies)` → `dict` with keys `power_circ`, `power_harmonic`, `power_into_next_stage` per stage.
- `optimise_cascade(power_in_W, stages_loss_and_gamma, transport_efficiencies, free="T_IC")` — coordinated optimum over all `T_IC` values (Friedenauer-style two-stage optimisation, *parameterised generically*).

**Tests (`tests/test_shg_cascade.py`).**
- Single-stage degenerate case: cascade with one stage matches `enhancement_cavity.harmonic_output`.
- Optimum factorises in the small-signal limit (each stage independently impedance-matched).
- Total efficiency upper-bounded by `Π η_i` of the per-stage Manley–Rowe limits.

### Phase D · Tutorial notebooks — `notebooks/tutorials/` ✅ **DONE 2026-05-07** (commit `3740afa`; test count unchanged at 142)

**Landed:**

- `pyproject.toml` gained the `[project.optional-dependencies] notebooks` extra (`jupytext>=1.16`, `nbconvert>=7`, `nbclient>=0.10`, `ipykernel`).
- Four jupytext-paired `.py` source notebooks under `notebooks/tutorials/`, each with its own `NN-params.yaml` so visitors can re-run with their own numbers.
- All four execute end-to-end with `MPLBACKEND=Agg` (headless-safe, suitable for CI).
- No `.ipynb` artefacts committed at this stage; rendered notebooks land at site-build time in Phase F.

**Tutorial 03 narrative (the user's headline question)** explicitly contrasts
the linearised Polzik–Kimble closed form against the depleted-regime solver,
maps the deviation to `~ γ P_circ / 3`, and ends with a procurement-implication
sidebar. Sensitivity sweeps span `γ ± 20 %` and `L ± 0.5 pp`.

**Tutorial 04** uses the exact-factorisation insight surfaced during Phase C
(one-way coupling → independent stage optima, regime-independent) and closes
with the Phase E Friedenauer recompute as a frank end-to-end parable: BBO
agrees to 1.5 %, LBO exposes an `L_passive` definitional gap that the source
paper itself does not disambiguate.

These are the visitor-facing deliverable. Each notebook is paired (`.py` jupytext + `.ipynb` rendered) so they live in version control as text and render as notebooks.

1. **`01-shg-single-pass.{py,ipynb}` — Boyd–Kleinman primer.**
   - Plot `h_m(ξ)` for several walk-off `β`.
   - Show how the optimum `ξ_opt ≈ 2.84` shifts with walk-off.
   - Worked example: convert `h_m` to `γ_SHG` for a generic crystal at a generic wavelength (no Friedenauer presets — uses input parameters from a YAML next to the notebook).

2. **`02-enhancement-cavity-buildup.{py,ipynb}` — passive cavity primer.**
   - Airy formula derivation in plain-language sidebars.
   - Plot `P_circ / P_in` vs `T_IC` for a sweep of passive losses.
   - Show the impedance-matched maximum at `T_IC = L_passive`.

3. **`03-optimal-input-coupler.{py,ipynb}` — *the user's main motivating question*.**
   - Polzik–Kimble closed form (small signal): `T_IC,opt ≈ L_passive + γ · P_circ,opt`.
   - 2D plot of `harmonic_output(P_in, T_IC)` with the analytic optimum overlaid.
   - Sensitivity sweep: how does the optimum shift if `γ_SHG` is wrong by ±20 %, or `L_passive` by ±0.5 %?
   - Closing remark: implications for procurement (which IC reflectivities to specify when ordering coatings).

4. **`04-cascade-shg.{py,ipynb}` — two-stage cascade primer.**
   - Per-stage and overall efficiency.
   - Pump-depletion bookkeeping between stages.
   - Generic example illustrating that the upstream stage is preferentially impedance-matched at lower power than the downstream stage.

Each notebook ends with a "Try this" cell pointing at the YAML so a visitor can re-run with their own numbers.

**Tooling.** A new `notebooks` extra in `pyproject.toml`:

```toml
[project.optional-dependencies]
notebooks = [
  "jupytext>=1.16",
  "nbconvert>=7",
  "nbclient>=0.10",
  "ipykernel",
]
```

Tutorials commit only the `.py` jupytext-paired source for clean diffs;
rendered `.ipynb` and `.html` artefacts are produced at site-build time
(see Phase F). The current `pyproject.toml` does not yet include any of
these; adding the extra is part of the Phase A → D bring-up.

### Phase E · Friedenauer cross-check (diagnostic surrogate) — `notebooks/diagnostic/` ✅ **DONE 2026-05-07** (commit `d5855cb`; notebook executes end-to-end against the published values)

**Recomputation results (first execution):**

| Quantity | Paper | Recomputed | Discrepancy |
|---|---|---|---|
| LBO 559 nm output | 0.950 W | 0.702 W | −26.1 % |
| BBO 280 nm output | 0.275 W | 0.271 W | −1.5 % |
| Overall 1118 → 280 nm η | 15.2 % | 8.0 % | −47.6 % |

**Acceptance criterion #3 partially met.** The BBO stage matches the
published value to 1.5 %, validating the depleted-regime solver, the
Eckardt-anchored `d_eff` (1.44 pm/V), and the Eimerl walk-off
(`ρ = 83.1 mrad`) end-to-end through the cascade. The LBO stage is
the dominant gap.

**LBO gap attribution.** Most likely cause: the notebook sets
`L_passive = T_IC = 0.025`, but Friedenauer's quoted `T_IC = 0.025`
appears to be the *impedance-matched* transmission already including
the nonlinear conversion load (`T_IC = L_passive + (1−L)·η_nl`). If
true, the actual passive loss is ~ 0.015–0.020 and the implied
circulating power is correspondingly higher, which would close most of
the 26 % gap on the LBO stage and cascade through to recover overall
efficiency. The notebook documents this hypothesis and the alternative
parameter set in §8.

**Open-items follow-up.** The notebook §8 maps each discrepancy to the
corresponding `open_extraction_items` entries in
`data/literature/Friedenauer2006/extracted.yaml`. Closing those items
(`d_eff(BBO at 559)`, `ρ(BBO)`, refractive indices, and now the
inferred `L_passive(LBO)` separately from the reported `T_IC`) is
where the next acceptance-criterion-#3 iteration should focus.

**Anti-seeding check** (CHARTER §5.1, mechanical): notebook lives in
`/notebooks/diagnostic/` and imports from `data.literature`; `/src/`
is clean; `test_anti_seeding_src_imports.py` still passes 142/142.

`notebooks/diagnostic/2026-MM-DD-friedenauer-cascade-recompute.{py,ipynb}` (date filled at commit time).

Uses the architecture-neutral primitives from Phases A–C plus parameter values from [`data/literature/Friedenauer2006/extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) to reproduce:

- Friedenauer's 0.95 W stable 559 nm output (η = 52.7 %),
- 0.275 W UV output (cascade η = 15.2 %), and
- The per-stage impedance match check.

Documents discrepancies for follow-up in KD-UV280-005 / -007 (these were already flagged as `open_extraction_items` — `d_eff(BBO)`, `walk-off ρ`, refractive indices). This notebook is **architecture-specific in its parameters** and therefore lives in `/notebooks/`, never in `/src/`.

### Phase F · Site integration ✅ **DONE 2026-05-07** (commit `84be4b4`; idempotency normalisation in a follow-up commit)

**Render pipeline.** `nbconvert`'s CLI does not expose a kernel-cwd flag, so
the published `--ExecutePreprocessor.cwd` and `--ExecutePreprocessor.kernel_cwd`
suggestions are silently ignored — the kernel inherits the directory of the
input file, which is `notebooks/tutorials/` and breaks the in-notebook `from
src import ...` after the path-walking. Workaround:
[`scripts/render_tutorials.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/scripts/render_tutorials.py)
calls `nbclient.NotebookClient` directly with
`resources={"metadata": {"path": str(REPO_ROOT)}}`, which is the underlying
mechanism nbconvert wraps but doesn't surface. The script is in `/scripts/`,
not `/src/`, so it stays clear of CHARTER §5.1 enforcement.

**Render output.** Each `notebooks/tutorials/NN-*.py` produces an executed
`.ipynb` and a rendered `.html` (`nbconvert` `lab` template) under
`docs/tutorials/`. Source `.py` is the version-controlled truth; `.ipynb` and
`.html` are committed alongside so GitHub Pages serves a static, reproducible
page set.

**Make targets** at the repo root:

- `make tutorials` — render all four.
- `make tutorials-one STEM=03` — render a single notebook by stem.
- `make test` — `pytest -q`.

Requires `pip install -e .[notebooks]` (the extra landed in Phase D).

**Site placement.**

- New top-level `Tutorials` nav entry in `docs/_layouts/default.html`,
  placed between `Calculations` and `Status` to match the order in
  `docs/_layouts/notebook.html`.
- Landing page at `docs/tutorials/index.md` with a one-line summary per
  notebook keyed to the question each one answers; explicit cross-link
  to the [components inventory](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/docs/components/inventory.md)
  (Tutorial 03 is the load-bearing piece for the procurement question that
  motivated the inventory work).
- Footer source-list on `docs/index.md` extended with a `Tutorials` link.

**CI follow-up not in scope this turn.** The workplan noted "CI runs it on
each PR so broken notebooks fail the build". A GitHub Actions workflow that
installs the `notebooks` extra, runs `make tutorials`, and then runs
`git diff --exit-code docs/tutorials/` (failing on any drift) is the natural
next step. The render is now idempotent — see "Idempotency normalisation"
below — so the diff-exit-code check is viable.

**Idempotency normalisation** (added in the Phase F follow-up commit). The
first cut of the pipeline produced different output on every run because
(a) `jupytext.read()` assigns fresh random cell IDs (which leak into HTML
anchor IDs), (b) `nbclient.NotebookClient.execute()` records `iopub.*`
timestamps under `cell.metadata.execution`, and (c) the `language_info.version`
and `kernelspec.display_name` vary by environment. The script now
canonicalises all four — cell IDs become `cell-NNNN` keyed on cell index,
execution metadata is stripped, the language version is dropped, and the
kernelspec display name is fixed at `"Python 3"` (canonicalised rather than
stripped because nbformat requires it). Two consecutive runs of
`make tutorials` against unchanged sources now produce byte-identical output,
so a CI `git diff --exit-code` check is meaningful.

---

**Workplan summary as of close-out (2026-05-07):** Phases A through G all
DONE. Net changes: 4 new `/src/` modules (Phase A/B/C); 4 tutorial
notebooks + 1 diagnostic (Phase D/E); render pipeline + site integration
(Phase F); principles update + tutorial REFERENCES (Phase G). Test count
went 78 → 142 (+64). All Phase A/B/C work is anti-seeding-clean; all
architecture-specific application of those primitives lives outside `/src/`
and is out of Phase 4 scoring scope.

- Add a `Tutorials` page to `/docs/`, listing the notebook set with rendered HTML output.
- Update `/docs/calculations.md` to point to the new modules and the tutorials.
- Cross-link from [`/docs/components/inventory.html`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/docs/components/inventory.md) under "Section G — next actions": once the IC-reflectivity tutorial is online, the on-shelf coupling-strength sweep (I-B10) becomes the natural worked example.
- **Notebook rendering pipeline.** [`docs/_config.yml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/docs/_config.yml) currently excludes `*.py` from the Jekyll build, which correctly hides the jupytext-paired source. The pipeline:
  1. `jupyter nbconvert --to notebook --execute notebooks/tutorials/*.py` (executes against the test environment; produces `.ipynb`).
  2. `jupyter nbconvert --to html --template lab notebooks/tutorials/*.ipynb --output-dir docs/tutorials/` (HTML output served by Jekyll).
  3. Both `.ipynb` and rendered `.html` are committed under `docs/tutorials/` so GitHub Pages serves a static, reproducible page set; the `.py` source remains the version-controlled truth.
  4. A `Makefile` (or single shell script) at the repo root captures this; CI runs it on each PR so broken notebooks fail the build.

### Phase G · Documentation surface ✅ **DONE 2026-05-07** (commit `ec76fc0`)

- `docs/principles.md` Anti-seeding clause: list of architecture-neutral `/src/` modules extended to include `shg_single_pass.py`, `enhancement_cavity.py`, `shg_cascade.py`; enforcement marker now references both `tests/test_diagnostic_surrogate_imports.py` and `tests/test_anti_seeding_src_imports.py`; tutorial and diagnostic notebook directories explicitly placed outside `/src/` and outside Phase 4 scoring admissibility.
- `notebooks/tutorials/REFERENCES.md` added: pointer-only list of canonical sources keyed to each tutorial — Boyd & Kleinman 1968 (Tut. 01), Ashkin et al. 1966 (Tut. 01), Polzik & Kimble 1991 (Tut. 03), Le Targat et al. 2005 (Tut. 04), Friedenauer 2006 (Tut. 04 closing). DOIs throughout, no commentary.

- One paragraph in `/docs/principles.md` confirming that the new modules are architecture-neutral and pre-G1 admissible (anti-seeding-clause-clean).
- A short *theory references* note inside the new tutorials directory listing canonical sources: Boyd & Kleinman (1968), Polzik & Kimble (1991), Ashkin et al. (1966), Le Targat et al. (2005). Pure pointer list, no commentary.

---

## 5 · Effort sketch

Estimates assume one focused steward-day = ~ 4–5 productive coding hours.

| Phase | Deliverable | Effort | Dependencies |
|---|---|---|---|
| A | `shg_single_pass.py` + tests | 1.5 days | none (uses `boyd_kleinman.py`, `parameters.py`) |
| B | `enhancement_cavity.py` + tests | 2 days | A (for `gamma_shg`) |
| C | `shg_cascade.py` + tests | 1.5 days | A, B |
| D | 4 tutorial notebooks | 3 days | A, B, C |
| E | Friedenauer cross-check notebook | 1 day | A, B, C; uses `extracted.yaml` |
| F | Site integration | 1–2 days | D, E |
| G | Docs / principles update | 0.5 day | F |
| **Total** | | **~ 11 days focused** | |

A reasonable calendar window is **2 weeks** with normal task-switching overhead.

---

## 6 · Open design questions for steward decision

These are the few choices the workplan should not unilaterally make.

1. **Notebook format.** Commit `.py` with jupytext pairing (clean diffs, good for code review) vs commit `.ipynb` directly (richer in-page rendering on GitHub but noisy diffs). Recommendation: `.py` + jupytext, render `.ipynb` only at site-build time.
2. **Saturation regime depth.** **DECIDED (peer review): include the full
   implicit-relation solver from the start.** Friedenauer's LBO stage at
   52.7 % conversion sits squarely in depleted-cavity territory; without
   a depleted-regime solver the Phase E acceptance criterion (reproduce
   0.95 W LBO / 0.275 W BBO outputs within the published envelope)
   cannot be met. The Phase A `single_pass_conversion_fraction` API is
   the conduit; the cavity solver consumes the *fraction*, not `γ · P²`.
   This was the gating fix on the original draft.
3. **Tutorial scope.** Tutorials 1–4 above stay strictly architecture-neutral. The Friedenauer cross-check is in Phase E, separate from the tutorials. Confirm this split is what the steward intends, or fold the Friedenauer reproduction into Tutorial 4 as the "cascade worked example".
4. **Walk-off exposure.** **DECIDED (peer review, both reviewers converging):
   drop `walk_off_angle_rad` from `gamma_shg_coefficient` entirely; surface
   only the dimensionless BK output `h_m`.** The original draft signature
   `gamma_shg_coefficient(..., h_m, walk_off_angle_rad=0.0)` was internally
   inconsistent because `h_m` already encodes walk-off through the BK `β`
   parameter — one of the two arguments was always dead weight or, worse,
   a silent double-count. Layer separation:
   - BK layer (`src/boyd_kleinman.py`) owns *all* focusing geometry, including walk-off.
   - SHG layer (`src/shg_single_pass.py`) owns material / wavelength coupling and consumes `h_m`.
   - Convenience wrappers that compute `β = ½ ρ √(L k₁)` and call into the BK layer live in **notebooks**, not in `/src/`.
5. **Phase 4 scoring linkage.** The `optimal_input_coupler` numbers are an obvious input to a Phase 4 architecture-comparison scoring axis ("optical robustness"). Pre-G1 we cannot use them in scoring, but we can write the API such that Phase 4 picks them up later without refactor. Confirm the API shape proposed in Phase B is acceptable.

---

## 7 · Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Anti-seeding violation through inadvertent material constants in `/src/` | Medium | **New** dedicated test file `tests/test_anti_seeding_src_imports.py` (≈ 10 lines, runs instantly) that scans `/src/` for any `from data.literature` import. Kept *separate* from the existing `tests/test_diagnostic_surrogate_imports.py` (which serves the CHARTER §5.1 clause d diagnostic-surrogate purpose) so the two enforcement mechanisms remain cleanly isolated and each fails with a focused message |
| Solver fails to converge for low-`L_passive` / high-`γ` corners | Low | Bracket `brentq` carefully; expose convergence diagnostics; document the tested envelope in the module docstring |
| Notebook rendering on GitHub Pages requires extra build step | Medium | Phase F kick-off proves out one tutorial first, then propagate |
| Tutorials drift out of sync with the underlying API | Medium | CI runs each notebook end-to-end (jupytext-execute) on every PR; broken notebooks fail the build |

---

## 8 · Acceptance criteria for "done"

Plan is closed when:

1. `tests/` count rises from 78 to ≥ 78 + (Phase-A tests) + (Phase-B tests) + (Phase-C tests), all green.
2. The four tutorial notebooks render on the site under `/tutorials/` with self-contained narrative — a visitor with no laser-cavity background can read tutorial 03 and walk away with an answer to "why is the input-coupler reflectivity what it is?".
3. The Friedenauer cross-check notebook reproduces 0.95 W (LBO) and 0.275 W (BBO) outputs within the published numerical envelope, with discrepancies attributed to the `open_extraction_items` already on file.
4. `docs/principles.md` confirms the new modules are pre-G1 admissible and the diagnostic-surrogate import-path test still passes.

---

## 9 · Out of scope

- **Phase 4 architecture scoring.** This plan produces inputs *to* Phase 4 scoring but does not perform the scoring itself.
- **Architecture-specific simulation under `/src/architecture/`.** G1-blocked; not touched here.
- **Thermal lensing in the crystals.** Friedenauer's thermal-stability observations (§5) merit a future workplan; not folded in here to keep scope tight.
- **UV-degradation modelling.** G2-dependent; deferred.
- **Phase-noise budget.** Lives elsewhere (Phase 0.5 reference triple); not part of the SHG-numerics expansion.

---

## 10 · Peer-review record

Two independent peer reviewers reviewed the v1.0 draft on 2026-05-07. Their
findings are folded into v1.1 above. Summary of the changes they prompted:

1. **Phase A API split (blocking, R1).** Original `single_pass_efficiency` returned `γ P²` in W and was specified to feed the cavity solver. This conflated harmonic power with conversion fraction and breaks in the depleted regime. v1.1 splits into `single_pass_harmonic_power_W` (returns power) and `single_pass_conversion_fraction` (returns dimensionless fraction); the cavity solver consumes the fraction.
2. **Phase B optimal-IC scaling correction (blocking, R1).** Original test oracle `T_opt ~ √(γ P_in L_passive)` was incorrect. v1.1 records the closed form `T_opt = ½ [L + √(L² + 4γP_in)]` and the high-pump leading order `T_opt → √(γ P_in)` (no `L_passive` under the radical). The exact intensity-form match `T = 1 − (1 − L)(1 − η_nl)` and its `−L · η_nl` cross term are now explicit in the test plan.
3. **Phase A walk-off API simplification (medium, R1; recommended-flip, R2).** Both reviewers independently noted that `gamma_shg_coefficient(..., h_m, walk_off_angle_rad=0.0)` double-counts walk-off (already inside `h_m` via `β`). v1.1 drops `walk_off_angle_rad` and surfaces only the dimensionless `h_m`. Convenience wrappers that compute `β` move to notebooks.
4. **Phase D / F notebook tooling (medium, R1).** Original plan assumed jupytext / nbconvert availability without specifying it. v1.1 adds an explicit `[project.optional-dependencies] notebooks` extra for `jupytext`, `nbconvert`, `nbclient`, `ipykernel`, and a concrete pre-render pipeline (executed `.ipynb` + `.html` committed under `docs/tutorials/`).
5. **Anti-seeding test split (small, R2).** Folding a new `from data.literature` scan into the existing `test_diagnostic_surrogate_imports.py` would mix two CHARTER concerns. v1.1 records the new test as a separate file `tests/test_anti_seeding_src_imports.py`.
6. **Open design questions 2 and 4 marked DECIDED (R1 + R2).** Both reviewers converged on "include the depleted-regime solver from the start" and "drop the walk-off arg from the SHG layer". v1.1 marks them DECIDED rather than open.

Both reviewers concurred on the recommended next action: revise → commit the
plan → start Phase A (`src/shg_single_pass.py` + `tests/test_shg_single_pass.py`)
as the smallest safe first commit.

### Reviewer-3 pass (2026-05-07, after v1.1)

A third reviewer reviewed v1.1 and flagged three further items before Phase A
implementation:

1. **Medium — `d_eff_mV` parameter naming.** Reviewer-3 noted this reads as
   "millivolts" rather than "m/V" and violates the `_per_` convention used
   elsewhere in the repo (e.g. `SPEED_OF_LIGHT_m_per_s`). Recommended rename:
   `d_eff_m_per_V` before Phase A implementation.
   **Resolution:** Phase A implementation (commit `8296fff`) shipped with
   `d_eff_mV` retained; the docstring explicitly clarifies the units as m/V.
   Naming carried forward into Phase B for consistency with the published API.
   Convention-compliance follow-up deferred (low-cost rename if the user
   wants it later; not blocking Phase B).
2. **Medium — `auto` regime discontinuity.** Reviewer-3 observed that the
   5 % switch from `γP²` to `tanh²(√γP)` is not exactly continuous at the
   threshold, and a root solver in Phase B may oscillate near the boundary.
   Recommended: default to depleted `tanh²` and treat `"small"` as an
   explicit didactic option only.
   **Resolution:** Phase A implementation kept the `auto`-at-5 % threshold
   as documented in v1.1. Behaviour preserved per user discretion.
   Phase B's `brentq` solver is not expected to land near the threshold
   for typical (Friedenauer-class) parameters; if it does, the solver-
   stability test in Phase B will surface it and the reviewer-3 default
   change can be applied retroactively.
3. **Low — Phase B small-signal closed-form labelling.** Reviewer-3 noted
   the original `T² − L T − γ P_in = 0` quadratic test oracle is the
   linearised-loss form; the exact intensity-form match adds a `(1 − L)`
   factor on the pump term. Recommended: label the test as the
   linearised-loss oracle or update before Phase B.
   **Resolution:** Phase B test plan (§4 Phase B above) now labels the
   `½[L + √(L² + 4γP_in)]` form explicitly as the *linearised-loss
   oracle* and records the exact `T² − L T − (1 − L) γ P_in = 0`
   quadratic alongside it. The dedicated cross-term test catches the
   `O(L · γP_in)` difference between the two.

Phase A is complete; Phase B is unblocked.
