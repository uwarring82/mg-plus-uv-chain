# Raman requirements — `constraints/raman-requirements.md`

**CHARTER §1.5 Level 0** task constraints for ²⁵Mg⁺ Raman / spin-motion control.

**Status:** Phase 0.5 deliverable. **Not yet populated at v1.0 cut.**

---

## Required content (Phase 0.5)

This document locks the numerical envelopes for the Raman task constraints. It is one of the three constraint files (the others are `loss-budget.md` and `phase-noise-budget.md`) that Phase 0.5 must produce before Phase 4 architecture comparison can begin.

Phase 0.5 may close on:

- **Precise envelopes** (preferred), or
- A **bounded-scenario set** labelled *Conservative / Nominal / Aggressive* per CHARTER §1.5 stall mitigation. Phase 4 scoring must run at minimum on the Conservative scenario.

In either case, the document must provide a **reference triple** {Δ_ref, Ω_R,ref, Γ_sc,ref} for Phase 4 reference-triple anchoring (CHARTER §5.2).

---

## Required fields

### Detuning window Δ from ³P_{1/2} and ³P_{3/2}

- Admissible Δ range (Hz; expressed relative to which level)
- Forbidden sub-domains (e.g. the 14-GHz unlockable region per CHARTER §8.1, until G1 closes)
- Sign convention (red- vs. blue-detuned)

Numeric anchor at v1.0 cut (per CHARTER §5 Phase 0.5 row): order ~10 GHz to ~100 GHz from ³P_{1/2,3/2}, refined by Phase 0.5.

### Target two-photon Rabi frequency Ω_R

- Envelope at the chosen Δ
- Coupling: Ω_R ∝ I/Δ (well-known scaling; document the prefactor used)
- Reference triple value Ω_R,ref

### Acceptable spontaneous-scattering rate Γ_sc

- Envelope at the chosen Δ
- Coupling: Γ_sc ∝ I/Δ² (well-known scaling)
- Per-gate scattering budget (typical: sub-percent)
- Reference triple value Γ_sc,ref

### Beam geometry at the ion

- Beam waist envelope (μm)
- Propagation directions and k-vector projections onto motional modes
- Polarisation requirements at the ion

---

## Locking protocol

Phase 0.5 closure for this document follows the §5.3 gate closure protocol with G3 as the relevant gate. The locked values populate `src/parameters.py` (the Phase 0.5 reference-triple variables) — the locking commit must reference both this document and the `/logbook/` entry.

After locking:

- This document becomes immutable in the strong sense — relaxation requires Council-3 + Integrator review per CHARTER §9 (asymmetric erosion protection).
- Tightening based on new evidence is permitted with documented rationale and a logbook entry.

---

## References

- CHARTER §1.5, §5 Phase 0.5 row, §5.1 G3, §5.2 reference-triple anchoring, §9 erosion protection.
- Related: `loss-budget.md` (Level 1), `phase-noise-budget.md` (Level 0/1 boundary).
- Background literature: see `/docs/KD-2026-XXX-uv-280nm.md` (Phase 1 dossier).

---

End of `raman-requirements.md` — placeholder at v1.0 cut.
