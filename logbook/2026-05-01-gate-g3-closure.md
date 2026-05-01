# Gate G3 closure — 2026-05-01

## Header (Charter §9 trigger question)

- **Affects Level 0 parameter?** yes
- **Affects Level 1 parameter?** yes
- **Affects success criterion?** yes (§6.4 Raman validation)

This entry files the proposed Phase 0.5 reference triple and bounded-scenario set, and records Integrator acknowledgement. Per CHARTER §9, Level 0/1 parameters are now subject to asymmetric erosion protection: tightening permitted with documented rationale; relaxation requires Council-3 deliberation + Integrator sign-off.

## Gate identification

- **Gate:** G3
- **Charter reference:** CHARTER §5.1 G3
- **Date:** 2026-05-01
- **Steward:** Ulrich Warring

## Evidence artefacts

### Reference triple {Δ_ref, Ω_R,ref, Γ_sc,ref}

Per CHARTER §5.2 reference-triple anchoring, the Nominal scenario is designated as the reference triple:

| Parameter | Value | Source document |
|---|---|---|
| Δ_ref | 40 GHz (red-detuned from nearer ³P level) | `constraints/raman-requirements.md` §5.1 |
| Ω_R,ref / 2π | 400 kHz | `constraints/raman-requirements.md` §5.1 |
| Γ_sc,ref | 2.0 × 10⁴ s⁻¹ | `constraints/raman-requirements.md` §5.1 |

### Bounded-scenario set (Conservative / Nominal / Aggressive)

Per CHARTER §1.5 stall mitigation and v0.9 Integrator insertion, the full scenario set is proposed for Phase 4 sensitivity testing. After G3 closure, Phase 4 scoring must run at minimum on the Conservative scenario.

| Scenario | Δ | Ω_R / 2π | Γ_sc |
|---|---|---|---|
| Conservative | 80 GHz | 100 kHz | 2.5 × 10³ s⁻¹ |
| Nominal (reference triple) | 40 GHz | 400 kHz | 2.0 × 10⁴ s⁻¹ |
| Aggressive | 15 GHz¹ | 1 MHz | 1.1 × 10⁵ s⁻¹ |

¹ *Conditional on G1 closure demonstrating the §8.1 14-GHz forbidden domain is < 500 MHz wide or architecture-specific (see `constraints/raman-requirements.md` §1.4).*

### Supporting constraint documents

- `constraints/raman-requirements.md` — Level 0 task constraints (DRAFT 0.1, physics-corrected 2026-05-01).
- `constraints/loss-budget.md` — Level 1 derived optical constraints (DRAFT 0.1).
- `constraints/phase-noise-budget.md` — Level 0/1 boundary phase-noise constraints (DRAFT 0.1).

### Locking commit

- Candidate-filing commit hash: `5eb63d6` ("gate(governance): file Phase 0.5 G3 candidate values; Phase 4 still blocked").
- Closure commit hash: filled at the closure-commit time (this commit).
- `src/parameters.py` populated: yes — reference triple and bounded-scenario values committed at `5eb63d6`.
- `src/parameters.py` G3 acknowledgement flag: `G3_INTEGRATOR_ACKNOWLEDGED = True` at the closure commit.

### Mechanical-enforcement attestation (CHARTER §5.3)

- `src/parameters.assert_g3_closed()` is silent at module load after closure.
- `tests/test_parameters.py::test_g3_integrator_acknowledged_true_after_closure` is the binding mechanical witness for the flag state at module load.
- `tests/test_parameters.py::test_assert_g3_closed_silent_at_module_load_after_closure` is the binding mechanical witness for the gate.
- `tests/test_parameters.py::test_reference_triple_locks_block_when_acknowledgement_revoked` confirms the gate re-engages if the flag is later revoked (defence in depth against silent erosion of CHARTER §9).
- All Phase 4 architecture-comparison code paths that call `assert_g3_closed()` are unblocked from this commit forward.

### Known uncertainties logged at filing

The following items are explicitly acknowledged as open and subject to tightening after closure:

1. **Raman prefactor K_Raman.** The single-intermediate-level estimate (138 MHz) is order-of-magnitude; the full multi-level ²⁵Mg⁺ Raman interference model (³P₁/₂ + ³P₃/₂ paths, Clebsch–Gordan coefficients) may shift the ion-side intensity requirement by a factor of 2–5. This does not invalidate the reference triple because the loss-budget analysis shows Raman power requirements remain ≪ 500 mW even with large variation. Tightening is expected from Phase 1 literature dossier and Phase 3 simulation.

2. **Aggressive scenario G1-dependence.** Δ = 15 GHz is conditional on G1 attribution. If G1 closes as Operationally bounded or Underdetermined with a forbidden domain > 500 MHz, the Aggressive scenario must be revised or retired.

3. **Phase-noise absolute linewidth bound.** The ≤ 500 kHz Nominal bound is informed by typical fibre-laser performance; Phase 2 baseline measurement on the existing chain will verify or tighten.

## Council-3 acknowledgement

- **Integrator confirmation:** **yes**, signed: Ulrich Warring (acting Integrator stance per the single-steward attribution pattern established at CHARTER §12 v1.0 sign-off block), date: 2026-05-01.
- **Architect flag raised?** no.
- **Guardian flag raised?** no.

*Closure date is non-retroactive per CHARTER §5.3: dependent work may proceed only on or after the closure commit.*

## Closure decision

- **Status at closure:** **CLOSED**.
- **Effective date of closure:** 2026-05-01 (the closure-commit date).
- **Dependent work now unblocked:** Phase 4 architecture comparison may commence at this commit's HEAD per CHARTER §5.1 G3 + §5.3. Phase 1 literature dossier and Phase 2 baseline measurement continue / interleave as before (they were never G3-blocked).

## Notes

- The bounded-scenario set was chosen over a single precise envelope because the Raman prefactor carries a known ~2–5× uncertainty. After G3 closure, Phase 4 scoring on the Conservative scenario is intended to guarantee that any architecture passing the comparison meets the Raman task constraints even under conservative physics assumptions.
- The observation that Raman-only ion-side power is < 15 mW source-side (see `constraints/loss-budget.md` §2.3) implies that Phase 4 axis 1 (Raman capability) is intensity-easy for all candidate families. The binding scoring axes are expected to be axes 2–4 (phase coherence, UV robustness, thermal / nonlinear load). This weighting implication is recorded for the Phase 4 pre-scoring deliberation.

---

*Gate-closure entry version: 1.1 — closed 2026-05-01 (filed and closed same day under single-steward stance attribution).*
