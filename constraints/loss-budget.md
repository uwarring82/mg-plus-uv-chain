# Loss budget — `constraints/loss-budget.md`

**CHARTER §1.5 Level 1** derived optical constraint: total optical loss budget from source to ion.

**Status:** Phase 0.5 deliverable. **DRAFT — NOT LOCKED.** This document links the ion-side intensity required for Raman operation (per `raman-requirements.md`) to the source-side power target. All numeric estimates are draft placeholders for Steward review.

---

## 1. Ion-side intensity requirement (from Level 0)

The required single-beam intensity at the ion is derived from the Raman Rabi frequency target (see `raman-requirements.md` §2.3). Using the draft scaling relation (pending Phase 1 atomic-data verification):

$$\frac{\Omega_R}{2\pi} \approx K_{\text{Raman}} \times \frac{P_{\text{ion}}/\text{mW}}{(w_0 / 20\,\mu\text{m})^2} \times \frac{1}{\Delta / \text{GHz}}$$

where $K_{\text{Raman}} \approx 138$ MHz is an order-of-magnitude prefactor for ²⁵Mg⁺ (single-intermediate-level model, averaged Clebsch–Gordan coefficients; see `raman-requirements.md` §2.3 for the full derivation). **This prefactor is flagged for verification;** the true value depends on the multi-level Raman path interference and may differ by a factor of 2–5.

### 1.1 Required power at the ion (per beam)

Solving for $P_{\text{ion}}$ at each scenario:

| Scenario | Ω_R / 2π | Δ | w₀ | P_ion / beam (draft) | P_ion total (2 beams) |
|---|---|---|---|---|---|
| Conservative | 100 kHz | 80 GHz | 30 μm | ~50 μW | ~100 μW |
| Nominal | 400 kHz | 40 GHz | 20 μm | ~130 μW | ~260 μW |
| Aggressive | 1 MHz | 15 GHz | 12 μm | ~1.0 mW | ~2.0 mW |

*Table 1 — Draft ion-side power requirements. The Conservative and Nominal values are remarkably low because the ²⁵Mg⁺ ³S–³P dipole moment is large and the detunings are moderate. The Aggressive scenario demands tighter focus and smaller Δ, raising the power requirement.*

**Observation (draft):** If the binding constraint is Raman operation alone, the required ion-side power is in the sub-mW to few-mW range. The CHARTER §2 indicative target of ≥ 500 mW source-side power therefore carries large overhead — likely driven by detection/cooling intensity requirements, beam-splitting overhead, degradation margins, or multi-port delivery. This tension is noted here for Phase 4 scoring (axis 4: thermal / nonlinear load) without resolving it.

---

## 2. Per-element loss table (source → ion)

### 2.1 Optical path (draft architecture-agnostic model)

The path below is a generic superset; not every element appears in every architecture. The table lists **single-pass** transmission or efficiency.

| Element | T or η (draft) | Tolerance | Wavelength | Comment |
|---|---|---|---|---|
| Fibre-to-free-space collimator | 0.90 | ±0.05 | 280 nm | Assumes AR-coated fibre tip and collimating lens. |
| Isolator (optional) | 0.85 | ±0.05 | 280 nm | UV isolators have lower transmission than IR equivalents. |
| AOM (per beam, double-pass) | 0.64 | ±0.10 | 280 nm | 0.80 diffraction efficiency × 0.80 return efficiency = 0.64; two AOMs per beam in some Raman schemes. |
| Beam-splitter (Raman pair generation) | 0.95 | ±0.02 | 280 nm | 50/50 or variable; assumes low-loss dielectric coating. |
| Steering mirrors (×4) | 0.98⁴ = 0.92 | ±0.02 per mirror | 280 nm | Four bounces typical in a trap optical table layout. |
| Lenses / waveplates (×6 surfaces) | 0.99⁶ = 0.94 | ±0.01 per surface | 280 nm | AR-coated fused silica at 280 nm. |
| Vacuum window | 0.96 | ±0.02 | 280 nm | Two AR-coated surfaces; Brewster-angle option improves to ~0.99. |
| In-vacuum lens / viewport | 0.95 | ±0.03 | 280 nm | Final focusing element; may be external. |
| Polarisation purity filter | 0.97 | ±0.02 | 280 nm | Cleanup polariser after stress-induced birefringence in optics. |

*Table 2 — Draft per-element transmission values. These are informed by typical UV-optics catalog data and institutional experience; they must be verified by measurement on the existing chain during Phase 2.*

### 2.2 Nominal end-to-end transmission

Multiplying the optimistic (central) values for a two-beam Raman path:

$$T_{\text{end-to-end}} = 0.90 \times 0.85 \times 0.64^2 \times 0.95 \times 0.92 \times 0.94 \times 0.96 \times 0.95 \times 0.97$$

$$T_{\text{end-to-end}} \approx 0.90 \times 0.85 \times 0.41 \times 0.95 \times 0.92 \times 0.94 \times 0.96 \times 0.95 \times 0.97 \approx 0.18$$

**Draft result:** ~18 % end-to-end transmission for a two-AOM-per-beam path. With a simpler one-AOM-per-beam path: $T \approx 0.28$.

### 2.3 Required source-side UV power (Raman only)

| Scenario | P_ion total | T_end-to-end (2 AOMs) | P_source required (Raman) |
|---|---|---|---|
| Conservative | ~100 μW | 0.18 | ~0.6 mW |
| Nominal | ~260 μW | 0.18 | ~1.4 mW |
| Aggressive | ~2.0 mW | 0.18 | ~11 mW |

*Table 3 — Draft source-side power for Raman operation only. Even with conservative loss assumptions, the Raman mode does not drive the 500 mW requirement.*

### 2.4 Headroom analysis (draft)

If the source delivers 500 mW and Raman requires < 15 mW (Nominal), the remaining ~485 mW is available for:

- **Detection / Doppler cooling beams:** typically higher power for fluorescence collection efficiency.
- **Beam-pair overhead:** multiple trap zones, imaging paths, or redundant delivery fibres.
- **Degradation margin:** if the source degrades by 20 % over months, the Raman mode still has factor ~20× headroom.
- **Alignment overhead:** non-optimal coupling during initial alignment or after maintenance.

This headroom is not a bug — it is the consequence of the Raman mode being intensity-efficient at moderate detuning. However, it shifts the design emphasis: **the binding constraints for Raman are not source-side raw power but stability, linewidth, phase noise, and degradation rate** (CHARTER §5.2 axes 2, 3, 4).

---

## 3. Cavity impedance-matching contributions

These contributions are **architecture-dependent** and therefore cannot be locked at Phase 0.5. The table below lists the quantities that each architecture-family simulation (Phase 3) must compute, per CHARTER §1.5 Level 1.

| Quantity | How derived | Phase 3 input |
|---|---|---|
| Per-stage round-trip loss (linear absorption + scatter + nonlinear conversion) | From crystal data (Phase 1 dossier) and measured degradation rates (Phase 2) | Material-specific; temperature-dependent. |
| Input coupler reflectivity R_in | Impedance-matched to round-trip loss: R_in = 1 − L_RT (for optimum coupling) | Architecture-specific cavity design. |
| Output coupler transmission T_out at harmonic | Derived from desired extraction efficiency and impedance-matching condition | Set by coating specification. |
| HR mirror reflectivities | > 99.9 % at fundamental and harmonic; certified at design fluence | Vendor data + Phase 2 witness-mirror validation (§8.6). |
| Coating UV damage threshold at design fluence | Vendor LIDT specification × safety factor (typically 2–3× for CW) | Critical for axis 3 (UV robustness) scoring. |

*Table 4 — Architecture-dependent cavity parameters. These are placeholders; locking requires Phase 3 simulation validated against Phase 2 measurement.*

### 3.1 Thermal-load envelope (CHARTER §1.5 Level 1, v0.6 Scout-driven)

| Parameter | Draft envelope | Rationale |
|---|---|---|
| Max pump power into most-stressed stage | ≤ 10 W (fundamental) | Institutional record: Friedenauer 2006 used ~1.8 W at 1118 nm for first SHG; scaling to 500 mW UV implies ~3–5 W at 1118 nm with improved crystals. 10 W leaves headroom for low-efficiency paths. |
| Max crystal temperature rise | ≤ 15 K above ambient | BBO and CLBO have temperature-dependent phase-matching bandwidth; > 15 K risks walk-off or refractive-index drift. |
| Min conversion efficiency (thermal budget) | ≥ 5 % (1118 → 280 overall) | Below 5 % overall, the rejected pump power (> 9.5 W) exceeds the thermal-load envelope for compact crystal mounts without active water cooling. |

*Table 5 — Thermal-load envelope. These are order-of-magnitude bounds for Phase 4 scoring. Tightening requires Phase 2 thermal measurements on the existing chain.*

---

## 4. Scenario summary (Conservative / Nominal / Aggressive)

| Scenario | P_source required (Raman only) | P_source with 3× overhead* | Thermal-load implication |
|---|---|---|---|
| Conservative | ~0.6 mW | ~2 mW | Trivial; any architecture meeting stability requirements is acceptable. |
| Nominal | ~1.4 mW | ~4 mW | Low thermal stress; focus on phase noise and degradation. |
| Aggressive | ~11 mW | ~33 mW | Moderate; requires verified AOM efficiency and low-loss beam path. |

*\*3× overhead accounts for detection/cooling beam splitting, alignment margin, and degradation buffer. This factor is a placeholder; Steward to confirm against trap layout.*

---

## 5. Locking protocol

**This document is NOT locked.**

Before G3 closure, the following must occur:

1. Steward verification of the ion-side power scaling (§1) against the institutional trap record.
2. Phase 2 measurement of per-element transmission on the existing chain (Table 2).
3. Confirmation of the 3× overhead factor (or replacement with a trap-specific split ratio).
4. If the ion-side power requirement remains in the sub-mW to few-mW range, document the implication that the 500 mW target is **not** Raman-binding and that Phase 4 scoring should weight axes 2–4 accordingly.
5. Population of `src/parameters.py` with the agreed loss budget (or explicit statement that loss is not the binding constraint).

After locking, this document becomes subject to CHARTER §9 asymmetric erosion protection.

---

## 6. Open items / literature anchors needed

- [ ] **Per-element transmission:** Measure or cite vendor-certified values for all elements at 280 nm.
- [ ] **Raman prefactor K_Raman:** The 138 MHz figure in `raman-requirements.md` §2.3 is the single-intermediate-level estimate. Verify against the full multi-level (³P₁/₂ + ³P₃/₂) expression with proper Clebsch–Gordan coefficients during Phase 1 atomic-data work; the multi-level value may differ by a factor of 2–5, which would shift the entire ion-side power column.
- [ ] **AOM efficiency at 280 nm:** 80 % is an optimistic draft; actual UV AOM efficiency may be 50–70 %, strongly impacting the Aggressive scenario.
- [ ] **Cavity parameters:** Cannot be populated until architecture family is chosen (post-Phase 4). Retain Table 4 as a Phase 3 checklist.
- [ ] **Thermal data:** Phase 2 must measure crystal temperature rise vs. pump power for the existing BBO stage.

---

## References

- CHARTER §1.5 Level 1, §2, §5 Phase 0.5 row, §5.2 Phase 4 axis 4, §8.2, §8.6, §9 erosion protection.
- `raman-requirements.md` — ion-side intensity requirement (Level 0 input to this Level 1 document).
- `phase-noise-budget.md` — phase-noise contribution to loss budget (polarisation drift, coherence time).
- Phase 1 literature dossier (to be created): crystal absorption, coating transmission, AOM efficiency at 280 nm.

---

*Document version: DRAFT 0.1 — 2026-05-01. Not for locking.*
