"""
test_parameters.py
==================

Tests for the SI-units contract layer in src/parameters.py.

Covers:
    - CODATA physical constants (sanity)
    - Indicative source-side targets (CHARTER §2)
    - Phase 0.5 reference-triple lock helpers (CHARTER §5.1 G3, §5.2, §5.3)
    - Bounded-scenario-set fallback helpers (CHARTER §1.5)
    - assert_g3_closed() raises before Integrator acknowledgement, returns after lock
"""

from __future__ import annotations

import importlib

import pytest

from src import parameters


@pytest.fixture(autouse=True)
def _restore_parameters_state() -> None:
    """Reload parameters before each test so module-level state is fresh."""
    importlib.reload(parameters)
    yield
    importlib.reload(parameters)


# =====================================================================
# Physical constants (CODATA 2018 values to within float precision)
# =====================================================================


def test_speed_of_light_codata() -> None:
    assert parameters.SPEED_OF_LIGHT_m_per_s == 2.99792458e8


def test_planck_constants_consistent() -> None:
    h = parameters.PLANCK_CONSTANT_J_s
    hbar = parameters.REDUCED_PLANCK_J_s
    import math

    assert hbar == pytest.approx(h / (2 * math.pi), rel=1e-9)


def test_elementary_charge_codata() -> None:
    assert parameters.ELEMENTARY_CHARGE_C == 1.602176634e-19


def test_boltzmann_codata() -> None:
    assert parameters.BOLTZMANN_CONSTANT_J_per_K == 1.380649e-23


# =====================================================================
# 25Mg+ atomic data — placeholder values; Phase 1 to verify
# =====================================================================


def test_mg_wavelengths_in_uv_band() -> None:
    """Both 25Mg+ ³S->³P transitions live near 280 nm."""
    for wl in (
        parameters.WAVELENGTH_3S_3P_HALF_m,
        parameters.WAVELENGTH_3S_3P_THREEHALF_m,
    ):
        assert 270e-9 < wl < 290e-9


def test_mg_fine_structure_ordering() -> None:
    """³P_{3/2} sits at higher energy → shorter wavelength than ³P_{1/2}."""
    assert (
        parameters.WAVELENGTH_3S_3P_THREEHALF_m
        < parameters.WAVELENGTH_3S_3P_HALF_m
    )


def test_mg_natural_linewidths_positive_and_mhz_scale() -> None:
    for gamma in (
        parameters.NATURAL_LINEWIDTH_3P_HALF_Hz,
        parameters.NATURAL_LINEWIDTH_3P_THREEHALF_Hz,
    ):
        assert 1e6 < gamma < 1e9  # MHz to GHz envelope


# =====================================================================
# Source-side targets (CHARTER §2)
# =====================================================================


def test_uv_power_target_indicative() -> None:
    assert parameters.UV_POWER_TARGET_INDICATIVE_W == pytest.approx(0.5)


def test_uv_sustained_operation_target_8h() -> None:
    assert parameters.UV_SUSTAINED_OPERATION_TARGET_s == 8 * 3600


def test_uv_linewidth_indicative_bound_1MHz() -> None:
    """v0.8 external-Verifier addition: ≤ 1 MHz at 280 nm, indicative."""
    assert parameters.UV_LINEWIDTH_BOUND_INDICATIVE_Hz == pytest.approx(1.0e6)


# =====================================================================
# Phase 0.5 reference-triple candidate values (G3 filed OPEN, 2026-05-01)
# =====================================================================


def test_reference_triple_candidate_values_after_g3_filing() -> None:
    assert parameters.DELTA_REF_Hz == pytest.approx(40.0e9)
    assert parameters.OMEGA_R_REF_Hz == pytest.approx(400.0e3)
    assert parameters.GAMMA_SC_REF_per_s == pytest.approx(2.0e4)


def test_conservative_scenario_candidate_values_after_g3_filing() -> None:
    assert parameters.DELTA_CONSERVATIVE_Hz == pytest.approx(80.0e9)
    assert parameters.OMEGA_R_CONSERVATIVE_Hz == pytest.approx(100.0e3)
    assert parameters.GAMMA_SC_CONSERVATIVE_per_s == pytest.approx(2.5e3)


def test_nominal_scenario_values_populated() -> None:
    assert parameters.DELTA_NOMINAL_Hz == pytest.approx(40.0e9)
    assert parameters.OMEGA_R_NOMINAL_Hz == pytest.approx(400.0e3)
    assert parameters.GAMMA_SC_NOMINAL_per_s == pytest.approx(2.0e4)


def test_aggressive_scenario_values_populated() -> None:
    assert parameters.DELTA_AGGRESSIVE_Hz == pytest.approx(15.0e9)
    assert parameters.OMEGA_R_AGGRESSIVE_Hz == pytest.approx(1000.0e3)
    assert parameters.GAMMA_SC_AGGRESSIVE_per_s == pytest.approx(1.1e5)


def test_reference_triple_values_complete_after_g3_filing() -> None:
    assert parameters.reference_triple_values_complete() is True


def test_g3_integrator_acknowledged_true_after_closure() -> None:
    """G3 closed 2026-05-01 — flag is True at module load."""
    assert parameters.G3_INTEGRATOR_ACKNOWLEDGED is True


def test_reference_triple_locked_true_after_integrator_acknowledgement() -> None:
    assert parameters.reference_triple_locked() is True


def test_assert_g3_closed_silent_at_module_load_after_closure() -> None:
    """Mechanical witness for the §5.3 G3-closure attestation."""
    parameters.assert_g3_closed()


def test_reference_triple_locks_block_when_acknowledgement_revoked() -> None:
    """If G3_INTEGRATOR_ACKNOWLEDGED is revoked, the gate re-engages even
    when candidate values remain numerically complete."""
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = False
    assert parameters.reference_triple_values_complete() is True
    assert parameters.reference_triple_locked() is False
    with pytest.raises(RuntimeError, match="Integrator-acknowledged"):
        parameters.assert_g3_closed()


# =====================================================================
# Lock helpers — partial vs full lock semantics
# =====================================================================


def test_partial_single_triple_does_not_lock() -> None:
    # Start from locked state, clear one field to simulate partial lock
    parameters.DELTA_REF_Hz = 1.0e10
    parameters.OMEGA_R_REF_Hz = 1.0e6
    parameters.GAMMA_SC_REF_per_s = None
    # Also clear Conservative to isolate the single-triple test
    parameters.DELTA_CONSERVATIVE_Hz = None
    parameters.OMEGA_R_CONSERVATIVE_Hz = None
    parameters.GAMMA_SC_CONSERVATIVE_per_s = None
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = True
    assert parameters.reference_triple_values_complete() is False
    assert parameters.reference_triple_locked() is False
    with pytest.raises(RuntimeError):
        parameters.assert_g3_closed()


def test_full_single_triple_locks() -> None:
    parameters.DELTA_REF_Hz = 1.0e10
    parameters.OMEGA_R_REF_Hz = 1.0e6
    parameters.GAMMA_SC_REF_per_s = 1.0e2
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = True
    assert parameters.reference_triple_values_complete() is True
    assert parameters.reference_triple_locked() is True
    parameters.assert_g3_closed()  # must not raise


def test_conservative_scenario_alone_locks() -> None:
    """Bounded-scenario fallback: Conservative triple alone is sufficient."""
    parameters.DELTA_CONSERVATIVE_Hz = 1.0e10
    parameters.OMEGA_R_CONSERVATIVE_Hz = 1.0e6
    parameters.GAMMA_SC_CONSERVATIVE_per_s = 1.0e2
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = True
    assert parameters.reference_triple_values_complete() is True
    assert parameters.reference_triple_locked() is True
    parameters.assert_g3_closed()


def test_partial_conservative_does_not_lock() -> None:
    # Start from locked state, clear one field to simulate partial lock
    parameters.DELTA_CONSERVATIVE_Hz = 1.0e10
    parameters.OMEGA_R_CONSERVATIVE_Hz = 1.0e6
    parameters.GAMMA_SC_CONSERVATIVE_per_s = None
    # Also clear reference triple to isolate the conservative test
    parameters.DELTA_REF_Hz = None
    parameters.OMEGA_R_REF_Hz = None
    parameters.GAMMA_SC_REF_per_s = None
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = True
    assert parameters.reference_triple_values_complete() is False
    assert parameters.reference_triple_locked() is False


def test_nominal_or_aggressive_alone_does_not_lock() -> None:
    """Per CHARTER §1.5: Phase 4 must score AT MINIMUM the Conservative
    scenario. Nominal and Aggressive are sensitivity tests, not the gate."""
    # Clear both locking paths first
    parameters.DELTA_REF_Hz = None
    parameters.OMEGA_R_REF_Hz = None
    parameters.GAMMA_SC_REF_per_s = None
    parameters.DELTA_CONSERVATIVE_Hz = None
    parameters.OMEGA_R_CONSERVATIVE_Hz = None
    parameters.GAMMA_SC_CONSERVATIVE_per_s = None
    # Now set only Nominal and Aggressive
    parameters.DELTA_NOMINAL_Hz = 1.0e10
    parameters.OMEGA_R_NOMINAL_Hz = 1.0e6
    parameters.GAMMA_SC_NOMINAL_per_s = 1.0e2
    parameters.DELTA_AGGRESSIVE_Hz = 5.0e9
    parameters.OMEGA_R_AGGRESSIVE_Hz = 5.0e6
    parameters.GAMMA_SC_AGGRESSIVE_per_s = 1.0e3
    # Without Conservative or single-ref, lock is not satisfied
    parameters.G3_INTEGRATOR_ACKNOWLEDGED = True
    assert parameters.reference_triple_values_complete() is False
    assert parameters.reference_triple_locked() is False
    with pytest.raises(RuntimeError):
        parameters.assert_g3_closed()
