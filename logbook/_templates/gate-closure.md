# Gate closure template — `logbook/_templates/gate-closure.md`

**Use this template** to record the closure of a kill-gate (G1, G2, or G3) per CHARTER §5.3. Copy this file to `/logbook/YYYY-MM-DD-gate-<id>-closure.md` and fill in the fields.

---

# Gate <G1 | G2 | G3> closure — YYYY-MM-DD

## Header (Charter §9 trigger question)

- **Affects Level 0 parameter?** yes / no
- **Affects Level 1 parameter?** yes / no
- **Affects success criterion?** yes / no

If any of the above is `yes`, this entry is *also* an architectural decision and requires Council-3 deliberation logged below in addition to the gate-closure protocol.

## Gate identification

- **Gate:** G1 | G2 | G3
- **Charter reference:** CHARTER §5.1 G<id>
- **Date:** YYYY-MM-DD
- **Steward:** Ulrich Warring

## Evidence artefacts

*Required content varies by gate (CHARTER §5.3):*

### For G1 (14-GHz unlockable domain attribution)

- Phase 2 discriminant scan reports — list with paths under `/data/baseline/`:
  - Scan vs. crystal temperature: …
  - Scan vs. input polarisation: …
  - Scan vs. intra-cavity intensity: …
  - Scan vs. crystal manufacturer batch / cut: …
- Outcome classification per CHARTER §8 preamble: **Resolved | Operationally bounded | Underdetermined**
- Mechanism (if Resolved): …
- Diagnostic-surrogate import-path test result (CHARTER §5.1 mechanical enforcement): pass / fail
  - Last test run: <date, commit hash>
  - Surrogates retired into: `/notebooks/archive/` and/or `/src/diagnostic_surrogates_archive/` — list:
    - …

### For G2 (degradation protocol reproducibility)

- Reproducibility evidence for the §8.2 degradation protocol — paths under `/data/baseline/`:
  - Time-resolved {power, M², phase noise, polarisation} measurements: …
  - Exposure-history dependence demonstrated: yes / no
  - Partition method (CHARTER §8.6) chosen: swap-test | witness-mirror
  - Partition method validated per §8.6 *Method validation* clause: yes / no
- Outcome classification: **Resolved | Operationally bounded | Underdetermined**

### For G3 (Phase 0.5 reference-triple lock)

- Reference triple {Δ_ref, Ω_R,ref, Γ_sc,ref} or Conservative-scenario triple per §1.5 stall mitigation:
  - Δ = … Hz
  - Ω_R = … Hz
  - Γ_sc = … s⁻¹
- Source documents: `/constraints/raman-requirements.md`, `/constraints/loss-budget.md`, `/constraints/phase-noise-budget.md`
- Locking commit hash: …
- `src/parameters.py` populated: yes / no

## Council-3 acknowledgement

- **Integrator confirmation:** *required for closure* — yes / no, signed: …, date: …
- **Architect flag raised?** yes / no — if yes, summary: …
- **Guardian flag raised?** yes / no — if yes, summary: …

## Closure decision

- **Status at filing:** OPEN | CLOSED
- **Effective date of closure:** YYYY-MM-DD (must precede dependent work)
- **Dependent work now unblocked:** …

## Notes

(Free-form discussion of borderline calls, residual concerns, or items propagated to v1.x.)

---

*Template version: 1.0 (frozen with CHARTER v1.0).*
