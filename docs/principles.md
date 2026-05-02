---
title: Principles
description: Governance grammar of the mg-plus-uv-chain project
---

# Principles

The Charter is a *coastline* under local stewardship: it cites external coastlines (laser physics, Boyd–Kleinman theory, manufacturer data, published source designs) as constraints rather than replicating them. The principles below are the load-bearing structure that any contributor — including the assistant agents helping with literature work — must respect.

[← Home](index.html)

---

## Level 0 → Level 1 → Level 2 constraint hierarchy

Source-side specifications are *derivations*, not free choices. Three nested levels apply (Charter §1.5):

- **Level 0 (task constraints, ion-side, non-negotiable).** Detuning window Δ from ³P₁/₂ and ³P₃/₂; target two-photon Rabi frequency Ω_R; acceptable spontaneous-scattering rate Γ_sc per gate; relative phase-noise spectral density S_φ(f) between the two Raman beams; beam geometry at the ion.
- **Level 1 (derived optical constraints, between source and ion).** Required single-beam intensity at the ion to reach Ω_R at chosen Δ; UV power at the experiment input *after* the optical loss budget; beam quality envelope; absolute UV-source linewidth; cavity impedance-matching condition; thermal-load envelope.
- **Level 2 (source constraints).** The ≥ 500 mW headline target is retained as an *indicative anchor*; its binding form is the row coupling Ω_R, Δ, and S_φ(f).

The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0×10⁴ s⁻¹}` (the Nominal scenario) was locked by the G3 closure on 2026-05-01. A bounded-scenario set Conservative / Nominal / Aggressive is also locked for Phase 4 sensitivity testing.

---

## Kill-gates

Three hard gates block downstream phases (Charter §5.1).

| Gate | Blocks | Closure condition | Status (2026-05-02) |
|---|---|---|---|
| **G1** | Architecture-family-specific simulation in `/src/architecture/` | 14-GHz unlockable domain attributed *or* formally classified Underdetermined | OPEN — awaiting Phase 2 discriminant scans |
| **G2** | Phase 4/5 acceptance of degradation-rate inputs to scoring | §8.2 degradation protocol produces reproducible exposure-history dependence | OPEN — awaiting Phase 2 baseline measurement |
| **G3** | Phase 4 architecture comparison | Phase 0.5 reference triple Integrator-acknowledged | **CLOSED** 2026-05-01 |

Each gate closes via an Integrator-acknowledged logbook entry following the [`logbook/_templates/gate-closure.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/_templates/gate-closure.md) template.

### Anti-seeding clause (§5.1)

Pre-G1, no Boyd–Kleinman optimisation, impedance-matching computation, or parameter sweep on any candidate architecture (including the Friedenauer baseline) may be committed to `/src/`. Architecture-neutral shared infrastructure — generic ABCD utilities, generic BK functions without architecture presets, units handling, plotting, test fixtures — *is* permitted pre-G1 and lives in `/src/`.

The current architecture-neutral layer:

- [`src/parameters.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/parameters.py) — SI-units contract, Phase 0.5 reference triple, G3 enforcement helper.
- [`src/boyd_kleinman.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/boyd_kleinman.py) — generic h(σ, β, κ, ξ, μ), σ-optimised h_m, optimum finder, analytic limit.
- [`src/abcd.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/abcd.py) — elementary ABCD matrices, Gaussian-beam q-parameter, cavity stability, eigenmode.

### Diagnostic-surrogate exception

If the 14-GHz attribution requires architecture context (e.g. cavity geometry to test a coating-stack hypothesis), tightly bounded *diagnostic surrogate* architectures may be instantiated under `/src/diagnostic_surrogates_archive/`, with mandatory file-level markers and a **mechanically enforced** import-path test ([`tests/test_diagnostic_surrogate_imports.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/tests/test_diagnostic_surrogate_imports.py)) that fails the build if any production module imports from the archive subtree. Surrogates are absolutely excluded from Phase 4 scoring.

---

## Outcome classification

Each open boundary closes into one of three states (Charter §8 preamble):

- **Resolved** — mechanism identified, attribution evidence-based.
- **Operationally bounded** — effect predictable and characterised, mechanism not isolated.
- **Underdetermined** — discriminant set ran, no attribution achieved (this is itself a documented result, not a failure).

The vocabulary mirrors the Breakwater Claim Analysis Ledger 3-value scheme (COMPATIBLE / UNDERDETERMINED / INCONSISTENT). The Phase 1 dossier uses the same vocabulary entry-by-entry; see [Status → Dossier population](status.html#phase-1-literature-dossier).

---

## Phase 4 fixed scoring axes

When architecture comparison runs, six axes are declared *before* evaluation. Weights are frozen at Phase 4 entry; **no axis may be introduced or removed during scoring** (Charter §5.2):

1. **Raman capability** (primary axis): achievable Ω_R(Δ); detuning continuity.
2. **Phase coherence**: intrinsic vs. engineered; robustness under drift.
3. **UV robustness**: §8.2 degradation rate; crystal *and* coating contributions partitioned.
4. **Thermal / nonlinear load**: intensity at the most-stressed crystal; lifetime; efficiency-coupled-to-thermal-gradients.
5. **Tunability and modularity**: detuning agility; upgrade paths.
6. **Complexity and maintainability**: components, alignment DOFs, failure modes.

Axis-1 primacy is by Level 0 derivation; other weights are set by evidentiary impact on Level 1, not by stance preference.

### Reference-triple anchoring

Phase 4 scoring on axes 1–4 must, *at minimum*, be computed at the locked reference triple (Charter §5.2, v0.9 Integrator insertion). Broader envelope-based scoring is admissible as supplementary evidence but cannot substitute for the reference-anchor computation. This prevents asymmetric comparisons in which one architecture is evaluated at a friendly operating point and another at a harsh one.

---

## Asymmetric erosion protection (§9)

Level 0 / Level 1 parameters are subject to a one-sided governance asymmetry:

- **Tightening** based on new evidence: *permitted* with documented rationale and a logbook entry.
- **Relaxation**: *forbidden* without a Council-3 deliberation logged in `/logbook/` and explicit Integrator sign-off.

This protects the constraint hierarchy from silent erosion under operational pressure when performance proves harder than expected. The same asymmetry applies to §6 success criteria.

The **mechanical witness** for G3 is the `G3_INTEGRATOR_ACKNOWLEDGED` flag in [`src/parameters.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/parameters.py). Setting the flag back to `False` re-engages the gate and any Phase 4 code calling `assert_g3_closed()` will raise — covered by [`tests/test_parameters.py::test_reference_triple_locks_block_when_acknowledgement_revoked`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/tests/test_parameters.py).

---

## Endorsement and lock–key separation

Per [`endorsement.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/endorsement.md): this Charter and its derived documents establish *locks* — stable concepts, structures, protocols. Interpretations and applications by users are *keys* — free to vary, with authority derived from use rather than endorsement. The Charter does not control downstream interpretation; it provides a coordinate chart against which interpretations can be checked for consistency.

The endorsement scope is **local** (AG Schätz). Other groups may adopt, adapt, or reject any element of this framework without affecting its internal consistency or applicability within this stewardship.

---

[← Home](index.html) · [Calculations →](calculations.html) · [Status →](status.html)
