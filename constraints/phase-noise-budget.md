# Phase noise budget — `constraints/phase-noise-budget.md`

**CHARTER §1.5 Level 0/1 boundary** — phase-noise constraints for Raman coherent control.

**Status:** Phase 0.5 deliverable. **Not yet populated at v1.0 cut.**

---

## Required content (Phase 0.5)

This document quantifies the relative phase-noise spectral density S_φ(f) between the two Raman beams (Level 0) and the propagation of source-side absolute phase noise into this relative-noise budget (Level 1). It is one of the three constraint files locked at Phase 0.5 closure.

---

## Required fields

### Relative phase-noise spectral density S_φ(f) — Level 0

- Acceptable S_φ(f) envelope across the gate-relevant Fourier frequency band
- Coupling to gate fidelity: how S_φ(f) at frequencies near 1/τ_gate enters the gate-error budget
- Reference value at the Phase 0.5 reference triple

### Absolute UV-source linewidth bound — Level 1 (CHARTER §1.5, v0.8 external-Verifier addition)

- Required UV-source linewidth at 280 nm
- Indicative bound at v0.8: ≤ 1 MHz (relevant for detection / cooling SNR; tightened or relaxed by Phase 0.5)
- Required coherence time for relevant operations (detection, cooling, Raman gates)

### Common-mode rejection — architecture-class characterisation

For each architecture family (CHARTER §4):

- Single-source / quadrupling: intrinsic common-mode rejection inheritance (rejection bandwidth, thermal/mechanical drift sensitivity)
- Dual-source / SFG / hybrid: phase-lock loop (PLL) requirements to engineer equivalent rejection (loop bandwidth, residual phase noise of the lock, robustness)
- Direct deep-UV: not yet a candidate at v1.0; literature-only per CHARTER §4

This document does *not* select an architecture — it specifies the phase-noise envelope each candidate must demonstrate it can meet, for Phase 4 axis 2 ("Phase coherence") scoring.

---

## Locking protocol

Phase 0.5 closure for this document follows the §5.3 gate closure protocol with G3 as the relevant gate. After locking, both the relative S_φ(f) envelope and the absolute UV linewidth bound are subject to the asymmetric erosion protection in CHARTER §9.

---

## References

- CHARTER §1.5 Level 0 and Level 1, §4 architecture families, §5.2 Phase 4 axis 2, §6.4 Raman validation, §9 erosion protection.
- Related: `raman-requirements.md` (Level 0), `loss-budget.md` (Level 1).

---

End of `phase-noise-budget.md` — placeholder at v1.0 cut.
