"""
parameters.py — SI-units contract layer for mg-plus-uv-chain
=============================================================

Single source of truth for physical constants and project-wide parameters.
SI units throughout; variable names carry units where ambiguity is possible
(e.g. `power_W`, `wavelength_m`, `detuning_Hz`).

Per CHARTER.md §1.5 and CONVENTIONS.md §1, this module is the *contract layer*
between simulation code and the physical world. Code that hard-codes a constant
available here is rejected on review.

Status: scaffold at v1.0 cut. Numerical values for project-specific parameters
(detunings, target Rabi frequencies, loss budgets) are populated during Phase 0.5
constraint extraction — see /constraints/.

Charter compliance:
    - This module is architecture-neutral (no candidate-architecture presets).
    - Pre-G1 commits to this module require the `Affects-Level-0`,
      `Affects-Level-1`, and `Affects-Success-Criteria` footers per CONVENTIONS.md §4.
    - Numerical values flowing from Phase 0.5 must reference the corresponding
      /constraints/ document and the locking logbook entry.
"""

from __future__ import annotations

# =====================================================================
# Physical constants (CODATA 2018)
# =====================================================================

SPEED_OF_LIGHT_m_per_s: float = 2.99792458e8
PLANCK_CONSTANT_J_s: float = 6.62607015e-34
REDUCED_PLANCK_J_s: float = 1.054571817e-34
ELECTRON_MASS_kg: float = 9.1093837015e-31
ELEMENTARY_CHARGE_C: float = 1.602176634e-19
BOLTZMANN_CONSTANT_J_per_K: float = 1.380649e-23
VACUUM_PERMITTIVITY_F_per_m: float = 8.8541878128e-12

# =====================================================================
# 25Mg+ atomic data
# =====================================================================
# Source: literature dossier (Phase 1 deliverable, /docs/KD-2026-XXX-uv-280nm.md)
# These values are NOT yet locked at v1.0; they are populated and cross-checked
# during Phase 1 literature work.

# Wavelengths (vacuum), 25Mg+ ³S_{1/2} -> ³P transitions
# Approximate values per Friedenauer 2006 and standard references; tightened in Phase 1.
WAVELENGTH_3S_3P_HALF_m: float = 280.353e-9   # ³P_{1/2}; Phase 1 to verify and add isotope shift
WAVELENGTH_3S_3P_THREEHALF_m: float = 279.635e-9  # ³P_{3/2}; Phase 1 to verify

# Natural linewidths (Γ/2π), order-of-magnitude placeholders
NATURAL_LINEWIDTH_3P_HALF_Hz: float = 4.1e7   # placeholder; Phase 1 to verify
NATURAL_LINEWIDTH_3P_THREEHALF_Hz: float = 4.1e7  # placeholder; Phase 1 to verify

# =====================================================================
# Source-side targets (CHARTER §2)
# =====================================================================
# Indicative values. Binding specifications flow from Phase 0.5 (§1.5 Level 0 -> Level 1).

UV_POWER_TARGET_INDICATIVE_W: float = 0.500   # ≥ 500 mW at 280 nm (CHARTER §2)
UV_SUSTAINED_OPERATION_TARGET_s: float = 8 * 3600  # 8 hours (CHARTER §6.1)

# Absolute UV-source linewidth bound (CHARTER §1.5 Level 1, v0.8 external-Verifier addition)
UV_LINEWIDTH_BOUND_INDICATIVE_Hz: float = 1.0e6  # ≤ 1 MHz at 280 nm; tightened by Phase 0.5

# =====================================================================
# Phase 0.5 reference triple (§1.5, §5.1 G3, §5.2 reference-triple anchoring)
# =====================================================================
# {Δ_ref, Ω_R,ref, Γ_sc,ref}
# Locked values per the G3 gate-closure logbook entry filed 2026-05-01 and
# Integrator-acknowledged 2026-05-01 (see logbook/2026-05-01-gate-g3-closure.md).
# Source: constraints/raman-requirements.md (Nominal reference triple).
# Values are subject to CHARTER §9 asymmetric erosion protection:
#   - Tightening permitted with documented rationale and logbook entry.
#   - Relaxation requires Council-3 deliberation + Integrator sign-off.

G3_INTEGRATOR_ACKNOWLEDGED: bool = True

DELTA_REF_Hz: float | None = 40.0e9          # 40 GHz red-detuned
OMEGA_R_REF_Hz: float | None = 400.0e3       # 400 kHz two-photon Rabi frequency
GAMMA_SC_REF_per_s: float | None = 2.0e4     # 2.0 × 10⁴ s⁻¹ spontaneous scattering

# Bounded-scenario-set fallback (CHARTER §1.5, v0.9 Integrator)
# Populated alongside the reference triple for Phase 4 sensitivity testing once
# G3 is Integrator-acknowledged. Phase 4 scoring must run at minimum on the
# Conservative scenario.

DELTA_CONSERVATIVE_Hz: float | None = 80.0e9
OMEGA_R_CONSERVATIVE_Hz: float | None = 100.0e3
GAMMA_SC_CONSERVATIVE_per_s: float | None = 2.5e3

DELTA_NOMINAL_Hz: float | None = 40.0e9
OMEGA_R_NOMINAL_Hz: float | None = 400.0e3
GAMMA_SC_NOMINAL_per_s: float | None = 2.0e4

DELTA_AGGRESSIVE_Hz: float | None = 15.0e9
OMEGA_R_AGGRESSIVE_Hz: float | None = 1000.0e3
GAMMA_SC_AGGRESSIVE_per_s: float | None = 1.1e5


def reference_triple_values_complete() -> bool:
    """
    Return True iff the G3 candidate values are numerically complete.

    Completeness alone does not close G3. CHARTER §5.3 requires Integrator
    acknowledgement before Phase 4 architecture-comparison code may execute.
    """
    single_complete = (
        DELTA_REF_Hz is not None
        and OMEGA_R_REF_Hz is not None
        and GAMMA_SC_REF_per_s is not None
    )
    conservative_complete = (
        DELTA_CONSERVATIVE_Hz is not None
        and OMEGA_R_CONSERVATIVE_Hz is not None
        and GAMMA_SC_CONSERVATIVE_per_s is not None
    )
    return single_complete or conservative_complete


def reference_triple_locked() -> bool:
    """
    Return True iff the Phase 0.5 reference triple is locked.

    Used by Phase 4 scoring code to gate execution per CHARTER §5.2 and §5.3.
    Either the single reference triple or the Conservative scenario must be
    numerically complete, and Integrator acknowledgement must be recorded.
    """
    return G3_INTEGRATOR_ACKNOWLEDGED and reference_triple_values_complete()


# =====================================================================
# G3 enforcement helper
# =====================================================================

def assert_g3_closed() -> None:
    """
    Raise RuntimeError if Phase 0.5 reference triple is not locked.

    Phase 4 architecture-comparison code calls this at module import or
    function entry to enforce CHARTER §5.1 G3 and §5.3 acknowledgement.
    """
    if not reference_triple_locked():
        raise RuntimeError(
            "CHARTER §5.1/§5.3 G3 not closed: Phase 0.5 reference triple "
            "(or Conservative-scenario fallback) must be numerically complete "
            "and Integrator-acknowledged before Phase 4 architecture-comparison "
            "code may execute. See /constraints/raman-requirements.md and "
            "/logbook/ for the gate-closure entry."
        )
