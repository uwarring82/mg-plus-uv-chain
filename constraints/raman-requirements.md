# Raman requirements — `constraints/raman-requirements.md`

**CHARTER §1.5 Level 0** task constraints for ²⁵Mg⁺ Raman / spin–motion control.

**Status:** Phase 0.5 deliverable. **DRAFT — NOT LOCKED.** This document contains a proposed bounded-scenario set (Conservative / Nominal / Aggressive) for Steward review. It does **not** constitute a G3 closure; locking requires the §5.3 gate-closure protocol, a logbook entry, and Integrator acknowledgement.

---

## Draft scenario summary

| Scenario | Δ (GHz) | Ω_R / 2π (kHz) | Γ_sc (s⁻¹) | Gate-time estimate (μs) | Scattering / gate |
|---|---|---|---|---|---|
| **Conservative** | 80 | 100 | 2.5 × 10³ | ~5.0 | ~0.013 |
| **Nominal** | 40 | 400 | 2.0 × 10⁴ | ~1.25 | ~0.025 |
| **Aggressive** | 15¹ | 1 000 | 1.1 × 10⁵ | ~0.50 | ~0.055 |

*Table 1 — Proposed bounded-scenario set. All values are **draft estimates** anchored to order-of-magnitude ²⁵Mg⁺ physics below; Steward must verify against the institutional trap record and Phase 1 literature dossier before locking.*

¹ *See §1.4: conditional on G1 closure narrowing the §8.1 forbidden domain to < 500 MHz width or demonstrating architecture-specific absence.*

---

## 1. Detuning window Δ from ³P₁/₂ and ³P₃/₂

### 1.1 Sign convention

Red-detuned relative to the excited state: Δ > 0 means the laser frequency is **below** the ³S₁/₂ → ³Pⱼ transition frequency (ω_L = ω₀ − Δ).

Both ³P₁/₂ and ³P₃/₂ are used as intermediate levels. The Raman transition involves two beams whose frequency difference matches the ground-state hyperfine / motional splitting. Each beam is detuned from its nearer ³P level by Δ₁ or Δ₂.

### 1.2 Admissible Δ range (draft)

| Boundary | Value | Rationale |
|---|---|---|
| Lower bound | ~10 GHz (~250 × Γ) | Must stay far enough from resonance that spontaneous scattering remains controllable and AC Stark shifts do not destabilise the qubit frequency beyond the compensation range. |
| Upper bound | ~200 GHz | Practical intensity ceiling: at very large Δ the required laser power becomes prohibitive for a given Ω_R (Ω_R ∝ I/Δ). The fine-structure splitting (~2.74 THz) sets a much-higher hard ceiling beyond which two-path interference between ³P₁/₂ and ³P₃/₂ must be modelled explicitly. |

*The Charter v1.0 numeric anchor is “order ~10 GHz to ~100 GHz”; the draft upper bound is extended to ~200 GHz to accommodate the Conservative scenario.*

### 1.3 Forbidden sub-domains

- **14-GHz unlockable resonance domain** (CHARTER §8.1). Until G1 closes, this region is treated as operationally forbidden regardless of architecture choice.
- **Regions where Δ is comparable to the fine-structure splitting** (~2.74 THz) with sign such that one beam is near ³P₁/₂ and the other near ³P₃/₂ — these require explicit two-path Raman analysis and are excluded from the scenario set above.

### 1.4 Scenario detunings

- **Conservative:** Δ = 80 GHz. Large margin against the 14-GHz anomaly; scattering suppressed as 1/Δ².
- **Nominal:** Δ = 40 GHz. Typical of published Mg⁺ Raman sources (Friedenauer 2006 and institutional record).
- **Aggressive:** Δ = 15 GHz. Near the lower practical limit; requires careful scattering budgeting and AC-Stark compensation. **Operational warning:** This is only ~1 GHz from the §8.1 14-GHz forbidden domain. Friedenauer 2006 §4 describes the anomaly as a domain of finite width. The Aggressive scenario is therefore **conditional on G1 closure** demonstrating that the forbidden domain is narrower than ~500 MHz or is architecture-specific and absent in the chosen design.

---

## 2. Target two-photon Rabi frequency Ω_R

### 2.1 Scaling relation

For a Raman transition driven by two beams of equal single-photon Rabi frequency Ω₁ = Ω₂ = Ω through a single intermediate level (or through two levels with comparable detuning):

$$\Omega_R = \frac{\Omega^2}{2\Delta}$$

with

$$\Omega = \frac{|\mathbf{d}_{ge}| \, E_0}{\hbar} = \frac{|\mathbf{d}_{ge}|}{\hbar} \sqrt{\frac{2 I}{c \varepsilon_0}}$$

where $I = P / (\pi w_0^2)$ is the single-beam intensity at the ion for a Gaussian beam of waist $w_0$.

### 2.2 Effective dipole moment (²⁵Mg⁺ placeholder)

From the natural linewidth $\Gamma / 2\pi \approx 41$ MHz (NIST / atomic-data reference; see `src/parameters.py` placeholder):

$$|\mathbf{d}_{ge}|^2 = \frac{3\pi \varepsilon_0 \hbar c^3 \Gamma}{\omega^3}$$

Evaluated at $\lambda \approx 280$ nm this gives $|d_{ge}| \approx 1.6 \times 10^{-29}$ C·m ($\approx 1.9\, e a_0$). This is an **order-of-magnitude estimate** pending Phase 1 atomic-data verification. The actual Raman transition involves Clebsch–Gordan coefficients and interference between ³P₁/₂ and ³P₃/₂ paths; the effective dipole may differ by factors of order unity.

### 2.3 Intensity → Ω_R coupling (draft)

Using the placeholder dipole moment, the single-beam Rabi frequency is approximately

$$\frac{\Omega}{2\pi} \approx 525 \,\text{MHz} \times \sqrt{\frac{P}{\text{mW}}} \times \frac{20\,\mu\text{m}}{w_0}$$

and therefore

$$\frac{\Omega_R}{2\pi} \approx 138 \,\text{MHz} \times \frac{P/\text{mW}}{(w_0 / 20\,\mu\text{m})^2} \times \frac{1}{\Delta / \text{GHz}}$$

*This prefactor is an order-of-magnitude estimate from the single-intermediate-level model; the full multi-level Raman interference (²⁵Mg⁺ ³P₁/₂ and ³P₃/₂ paths, Clebsch–Gordan coefficients) will be implemented in Phase 3 simulation. The tabulated scenario values below are retained as draft estimates pending that verification.*

### 2.4 Scenario Ω_R values

| Scenario | Ω_R / 2π | Derivation sketch |
|---|---|---|
| Conservative | 100 kHz | ~5.0-μs π-pulse; compatible with low heating-rate traps and modest UV power. |
| Nominal | 400 kHz | ~1.25-μs π-pulse; matches typical Mg⁺ gate speeds in the institutional record. |
| Aggressive | 1 000 kHz | ~0.50-μs π-pulse; demands highest UV power and smallest waist, tightest stability. |

---

## 3. Acceptable spontaneous-scattering rate Γ_sc

### 3.1 Scaling relation

For a single intermediate level and two beams of equal intensity:

$$\Gamma_{sc} \approx \frac{\Gamma}{2} \left(\frac{\Omega}{2\Delta}\right)^2 \times 2 = \Gamma \left(\frac{\Omega}{2\Delta}\right)^2$$

Using $\Omega_R = \Omega^2/(2\Delta)$, this becomes

$$\Gamma_{sc} \approx \frac{\Gamma \, \Omega_R}{2\Delta}$$

### 3.2 Scenario Γ_sc values (derived, not independent)

| Scenario | Γ_sc (s⁻¹) | Scattering events / π-pulse | Comment |
|---|---|---|---|
| Conservative | 2.5 × 10³ | ~0.013 | Low single-percent scattering probability in the draft single-level estimate. |
| Nominal | 2.0 × 10⁴ | ~0.025 | Few-percent scattering probability; must be checked against the full gate-error budget. |
| Aggressive | 1.1 × 10⁵ | ~0.055 | Approaching the practical limit; requires error-model justification or shorter gates. |

*These are derived from the (Ω_R, Δ) pairs above using the scaling relation with Γ / 2π = 41 MHz. They are **not** independent choices — if Ω_R or Δ is revised, Γ_sc must be recomputed.*

### 3.3 Per-gate scattering budget

For a gate of duration τ_gate = π/Ω_R, where Ω_R is an angular frequency:

$$N_{sc} = \Gamma_{sc} \, \tau_{gate} = \frac{\pi \Gamma}{2\Delta}$$

Remarkably, $N_{sc}$ depends **only on Δ** (for the single-intermediate-level model). Using the draft table values above, Δ = 40 GHz gives $N_{sc} \approx 0.025$ and Δ = 80 GHz gives $N_{sc} \approx 0.013$.

*This independence breaks down when two ³P paths interfere, when polarisation selection rules suppress one path, or when the gate is not a simple π-pulse. Phase 3 simulation must use the full multi-level model.*

---

## 4. Beam geometry at the ion

### 4.1 Beam waist

| Scenario | Waist w₀ (μm) | Comment |
|---|---|---|
| Conservative | 30 | Large waist relaxes alignment and astigmatism tolerances; higher power required for same Ω_R. |
| Nominal | 20 | Typical of the existing trap geometry. |
| Aggressive | 12 | Tight focus for peak intensity; demands M² < 1.2 and stable pointing. |

### 4.2 Propagation directions and k-vector projections

The Raman beam pair is assumed to propagate at an angle θ_Raman relative to each other, with a component of $\Delta \mathbf{k}$ along the trap axis of interest (typically the axial mode). The exact geometry is trap-specific and does **not** belong in the source-side constraint file; it is recorded here as a placeholder pending trap-side coordination.

- **Draft assumption:** counter-propagating geometry (θ_Raman ≈ 180°) for maximum $\Delta k$ and strongest Lamb–Dicke coupling.
- **k-vector projection onto motional modes:** to be specified in coordination with the trap apparatus (outside this Charter’s scope per §3 non-goals).

### 4.3 Polarisation requirements

- σ⁺/σ⁻ or π/σ combinations depending on the chosen Raman transition (e.g. |F=3, m_F=+1⟩ ↔ |F=2, m_F=+1⟩ via σ⁺/σ⁻ or similar).
- Polarisation purity > 100:1 to suppress off-resonant coupling to unwanted Zeeman sub-levels.
- Polarisation drift envelope: < 5 % relative over an 8-h operation (couples to `phase-noise-budget.md`).

---

## 5. Reference triple and bounded-scenario set

### 5.1 Reference triple (draft — for Phase 4 anchoring)

Per CHARTER §5.2, Phase 4 scoring must be computed at minimum on a reference triple. The **Nominal** scenario is proposed as the reference:

| Parameter | Value |
|---|---|
| Δ_ref | 40 GHz (red-detuned from nearer ³P level) |
| Ω_R,ref / 2π | 400 kHz |
| Γ_sc,ref | 2.0 × 10⁴ s⁻¹ |

*Steward to confirm or replace before G3 closure.*

### 5.2 Bounded-scenario set (fallback)

If the Steward decides that precise envelopes cannot be locked, the full C/N/A table above serves as the bounded-scenario set per CHARTER §1.5 stall mitigation. Phase 4 scoring would then run:

1. **At minimum** on the Conservative scenario (mandatory per v0.9 Integrator insertion).
2. Optionally on Nominal and Aggressive as sensitivity tests.

---

## 6. Locking protocol

**This document is NOT locked.**

Before G3 closure, the following must occur:

1. Steward review of the C/N/A numbers against the institutional trap record and Phase 1 literature.
2. Verification of the effective dipole moment and multi-level Raman prefactor (see §2.2).
3. Confirmation of beam-geometry placeholders against the trap apparatus.
4. Population of `src/parameters.py` with the agreed reference triple or Conservative scenario.
5. Filing of the G3 gate-closure logbook entry per `/logbook/_templates/gate-closure.md`.
6. Integrator acknowledgement of the G3 closure entry.

After locking, this document and the populated `parameters.py` become subject to CHARTER §9 asymmetric erosion protection: tightening is permitted with rationale; relaxation requires Council-3 + Integrator deliberation.

---

## 7. Open items / literature anchors needed

- [ ] **Atomic data:** Confirm |d_ge|, Γ, and isotope shifts for ²⁵Mg⁺ from NIST ASD or peer-reviewed compilation.
- [ ] **Multi-level Raman prefactor:** The single-intermediate-level model used here is a simplification. The actual Ω_R and Γ_sc involve two ³P paths (fine-structure splitting ~2.74 THz) with opposite detuning signs. Derive the full expression and update the scaling relations.
- [ ] **AC Stark shift:** At Δ = 15 GHz (Aggressive), quantify the differential AC Stark shift of the qubit states and verify it lies within the compensation range.
- [ ] **14-GHz anomaly:** Until G1 closes, the forbidden domain near 14 GHz is treated as absolute. Revisit after G1 attribution if the mechanism suggests the anomaly is architecture-specific.
- [ ] **Trap geometry:** Confirm beam waist, propagation angle, and k-vector projection with the trap-side team.

---

## References

- CHARTER §1.5, §2, §5 Phase 0.5 row, §5.1 G3, §5.2 reference-triple anchoring, §8.1, §9 erosion protection.
- CONVENTIONS §1 (SI units; `parameters.py` contract layer).
- `src/parameters.py` — placeholder atomic data and G3 lock helpers.
- Background literature: `/docs/KD-2026-XXX-uv-280nm.md` (Phase 1 dossier; to be created).

---

*Document version: DRAFT 0.1 — 2026-05-01. Not for locking.*
