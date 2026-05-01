# 2026-04-30 — Architecture-neutral simulation infrastructure (pre-G1)

## Header (Charter §9 trigger question)

- **Affects Level 0 parameter?** no
- **Affects Level 1 parameter?** no
- **Affects success criterion?** no

This entry is *not* an architectural decision under the §9 reclassification rule. It deposits architecture-neutral utilities and test infrastructure that CHARTER §5.1 explicitly permits pre-G1.

## Stance attribution

- Steward (operational): drafted by assistant under steward direction.

## Scope of this entry

Build infrastructure and architecture-neutral simulation utilities added to the repository in the immediate post-v1.0 cut window. Falls under the CHARTER §5.1 carve-out:

> "Architecture-neutral shared infrastructure may be committed to /src/ pre-G1 provided it is genuinely architecture-agnostic — examples: SI-units handling, generic ABCD cavity utilities, generic Boyd–Kleinman functions without architecture presets, test fixtures, plotting utilities."

## Files added

### Build / packaging

- `pyproject.toml` — `setuptools` build, Python ≥ 3.11, dependencies pinned with `>=` floors (numpy, scipy, matplotlib, pyyaml). Optional extras: `test` (pytest, pytest-cov, hypothesis), `dev` (black, isort, ruff, mypy). Project tooling configs co-located: pytest options, coverage targets `fail_under = 90` (CHARTER §5 Phase 3 row), black / isort / ruff / mypy. The coverage `omit` list excludes `src/diagnostic_surrogates_archive/*` (CHARTER §5.1).

### Documentation

- `data/README.md` — Metadata schema for measurement and literature data. Declares the per-dataset `metadata.yaml` fields required for FAIR (CHARTER §7) and the discriminant-hypothesis fields (CHARTER §8.1) and degradation-protocol fields (CHARTER §8.2). Per-paper literature extractions live under `literature/<citation-key>/extracted.yaml`.

### Architecture-neutral simulation utilities (CHARTER §5.1 permitted pre-G1)

- `src/boyd_kleinman.py` — Generic Boyd-Kleinman (1968) SHG focusing function `h(σ, β, κ, ξ, μ)`, with σ-optimised variant `h_m`, optimum-finder `h_m_optimum`, and the closed-form analytic limit `h(σ=β=κ=μ=0, ξ) = arctan²(ξ)/ξ` for unit-test reference. **No architecture presets, no material constants, no wavelength shortcuts.** The Boyd-Kleinman material constant K is explicitly *not* computed here — it is material- and wavelength-specific and lives downstream of crystal choice.

- `src/abcd.py` — Generic ABCD ray / Gaussian-beam propagation utility. Elementary matrices (free-space, thin lens, curved mirror, flat / curved interfaces); `compose()` honouring propagation order (leftmost first); `GaussianBeam` dataclass with q-parameter manipulation; `propagate`, `is_stable`, `stability_g_factor`, `cavity_eigenmode_q`. **No cavity preset.**

### Tests (≥ 90% target, CHARTER §5 Phase 3 row)

Note: `tests/test_parameters.py` (covering CODATA constants, atomic placeholders, source-side targets, and the G3 lock helpers) lands with the Phase 0.5 G3 candidate filing in a separate commit, alongside the corresponding `src/parameters.py` changes. It is omitted from this infrastructure commit to keep commit boundaries aligned with logical change.

- `tests/test_boyd_kleinman.py` — 20 tests. Analytic-limit closed form (`arctan²(ξ)/ξ`) with `pytest.approx` tolerances down to `rel=1e-12`; numerical h-factor agrees with analytic limit to `rel=1e-4`; classic BK σ-optimised optimum reproduces ξ_opt ≈ 2.84, h_m,max ≈ 1.068; walk-off and absorption monotonically reduce h; off-centre focus reduces h in the symmetric case.

- `tests/test_abcd.py` — 31 tests. Elementary matrices, compose semantics, Gaussian-beam q at the waist (q = i z_R; w(z_R) = √2 w0; R(z_R) = 2 z_R); thin-lens imaging q-transform; concentric (g=1) and confocal (g=0) limits; eigenmode self-consistency under round trip; eigenmode rejection of unstable cavities.

## Verification

- 52 tests pass at this commit (31 ABCD + 20 Boyd–Kleinman + 1 pre-existing diagnostic-surrogate import-path test) on Python 3.9.7 with scipy 1.10.0, numpy 1.23.5 (local environment; CONVENTIONS specifies ≥ 3.11 for production). Subsequent commits add `tests/test_parameters.py` for a final 74-test suite.
- The diagnostic-surrogate import-path test (CHARTER §5.1 mechanical enforcement) continues to pass.

## Notes

- Performance: `h_m_optimum` runs scipy `dblquad` inside a Brent loop and takes ~100s. Acceptable for correctness-validating tests; downstream Phase 3 work that needs h_m at many ξ values should add caching or an analytical approximation.
- The σ-optimised dblquad emits a scipy `IntegrationWarning: maximum number of subdivisions (50)` at ξ = 2.84 in some σ-search corners. The result is still correct to within the test tolerance (h_m_max ≈ 1.068, abs=2e-2). If the warning becomes load-bearing for later quantitative work, raise `limit` in the underlying `quad` call or split the integration domain.
- Coverage report deferred to a separate run pending pytest-cov install.

## Charter compliance audit (self-check)

- §5.1 anti-seeding clause: the Boyd-Kleinman and ABCD modules contain *no* architecture-family code (no `quadrupling.py`-style branch, no SFG-specific integrals, no BBO/CLBO/LBO presets). They are genuinely architecture-agnostic and are reviewable by any stance.
- §5.1 mechanical-enforcement test: `tests/test_diagnostic_surrogate_imports.py` continues to pass; no production code imports from a (currently empty) surrogates archive.
- CONVENTIONS §1: SI throughout; variable names carry units (`d_m`, `wavelength_vac_m`, `f_m`).
- CONVENTIONS §2: Python ≥ 3.11 declared in `pyproject.toml`. Code uses `from __future__ import annotations` so it remains importable on 3.9 for the steward's local environment.

---

*Logbook entry version: 1.0.*
