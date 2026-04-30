# Loss budget — `constraints/loss-budget.md`

**CHARTER §1.5 Level 1** derived optical constraint: total optical loss budget from source to ion.

**Status:** Phase 0.5 deliverable. **Not yet populated at v1.0 cut.**

---

## Required content (Phase 0.5)

This document quantifies the optical loss chain between the source output and the ion position. It is the primary derivation linking the source-side ≥ 500 mW indicative target (CHARTER §2) to the ion-side intensity required to reach the Phase 0.5 reference Ω_R at Δ_ref.

---

## Required fields

### Per-element loss

For each optical element in the path (mirrors, lenses, AOMs, beam-pair-generation optics, vacuum windows, in-vacuum optics):

- Element identifier
- Single-pass transmission (or reflection where applicable)
- Tolerance / stability of the value
- Wavelength (relevant if the element is used at multiple wavelengths)

### Cavity impedance-matching contributions (CHARTER §1.5 Level 1, v0.5 cavity-coating addition)

For each SHG / SFG / build-up cavity in the chosen architecture:

- Per-stage round-trip loss budget (linear absorption + scatter + nonlinear conversion)
- Input coupler reflectivity R_in derived from the loss budget
- Output coupler transmission T_out at the harmonic wavelength
- HR mirror reflectivities at all relevant wavelengths
- Coating UV damage threshold at design fluence

These contributions are *not* free parameters — they are derived from the per-stage loss budget per CHARTER §1.5 Level 1.

### Total source → ion transmission

- End-to-end transmission with stated uncertainty
- Required source-side power to deliver the §1.5 Level 1 ion-side intensity
- Comparison with the §2 indicative ≥ 500 mW target

### Thermal-load envelope (CHARTER §1.5 Level 1, v0.6 Scout-driven)

- Maximum acceptable pump power into the most-stressed nonlinear stage
- Maximum acceptable crystal/coating temperature rise above ambient
- Minimum acceptable conversion efficiency consistent with the thermal budget
- Coupling to `/docs/degradation-protocol.md` (CHARTER §8.2)

---

## Locking protocol

Phase 0.5 closure for this document follows the §5.3 gate closure protocol with G3 as the relevant gate (alongside `raman-requirements.md` and `phase-noise-budget.md`). After locking, the Level 1 envelope is subject to the asymmetric erosion protection in CHARTER §9.

---

## References

- CHARTER §1.5 Level 1, §2, §5 Phase 0.5 row, §8.2, §8.6.
- Related: `raman-requirements.md` (Level 0), `phase-noise-budget.md` (Level 0/1 boundary).

---

End of `loss-budget.md` — placeholder at v1.0 cut.
