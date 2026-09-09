"""
test_boyd_kleinman.py
=====================

Tests for src/boyd_kleinman.py — the architecture-neutral BK focusing
utility.

Coverage targets:
    - Analytic limit (σ=β=κ=0, μ=0): h = arctan²(ξ)/ξ
    - h_factor matches the analytic limit numerically
    - σ-optimised h_m has the classic BK optimum ξ ≈ 2.84, h ≈ 1.068
    - Walk-off (β > 0) reduces h
    - Absorption (κ > 0) reduces h
    - Gouy phase shifts the optimum away from wave-vector matching σ=0
    - Off-centre focus (μ ≠ 0) reduces h relative to centred focus
      (in the symmetric lossless case)
    - Edge: xi <= 0 raises ValueError

Reference: G. D. Boyd & D. A. Kleinman, J. Appl. Phys. 39, 3597 (1968).
"""

from __future__ import annotations

import math

import numpy as np
import pytest
from scipy.integrate import solve_ivp

from scripts.review.shg_reference import tensor_h
from src import boyd_kleinman as bk

# =====================================================================
# Analytic-limit closed form
# =====================================================================


@pytest.mark.parametrize("xi", [0.1, 0.5, 1.0, 1.392, 2.0, 5.0, 10.0])
def test_analytic_closed_form_matches_arctan_squared_over_xi(xi: float) -> None:
    expected = math.atan(xi) ** 2 / xi
    assert bk.h_analytic_no_walkoff_no_loss(xi) == pytest.approx(expected, rel=1e-12)


def test_analytic_optimum_near_1p392() -> None:
    """arctan²(ξ)/ξ has its maximum at ξ where arctan(ξ) = 2ξ/(1+ξ²)."""
    xi_opt = 1.3915
    h_left = bk.h_analytic_no_walkoff_no_loss(xi_opt - 0.05)
    h_at = bk.h_analytic_no_walkoff_no_loss(xi_opt)
    h_right = bk.h_analytic_no_walkoff_no_loss(xi_opt + 0.05)
    assert h_at > h_left
    assert h_at > h_right
    assert h_at == pytest.approx(0.6458, abs=2e-3)


def test_analytic_raises_for_nonpositive_xi() -> None:
    with pytest.raises(ValueError, match="xi must be positive"):
        bk.h_analytic_no_walkoff_no_loss(0.0)
    with pytest.raises(ValueError, match="xi must be positive"):
        bk.h_analytic_no_walkoff_no_loss(-1.0)


# =====================================================================
# h_factor numerical matches analytic limit
# =====================================================================


@pytest.mark.parametrize("xi", [0.5, 1.0, 2.0, 4.0])
def test_h_factor_matches_analytic_limit(xi: float) -> None:
    """In the (σ=β=κ=μ=0) corner, the dblquad integral must reproduce arctan²(ξ)/ξ."""
    numerical = bk.h_factor(xi=xi, sigma=0.0, beta=0.0, kappa=0.0, mu=0.0)
    analytic = bk.h_analytic_no_walkoff_no_loss(xi)
    assert numerical == pytest.approx(analytic, rel=1e-4, abs=1e-6)


def test_h_factor_raises_for_nonpositive_xi() -> None:
    with pytest.raises(ValueError, match="xi must be positive"):
        bk.h_factor(xi=0.0)


# =====================================================================
# Phase-mismatch reduces h (relative to σ=0 in the lossless centred case)
# =====================================================================


def test_phase_mismatch_reduces_h() -> None:
    """Large mismatch reduces h; σ=0 itself is not the Gouy-phase optimum."""
    xi = 2.84
    h_zero = bk.h_factor(xi=xi, sigma=0.0)
    h_off = bk.h_factor(xi=xi, sigma=2.0)
    assert h_off < h_zero


# =====================================================================
# h_m σ-optimised: classic BK optimum ξ ≈ 2.84, h_m,max ≈ 1.068
# =====================================================================


def test_hm_classic_optimum() -> None:
    """The famous Boyd-Kleinman result: ξ_opt ≈ 2.84, h_m_max ≈ 1.068."""
    xi_opt, hm_max = bk.h_m_optimum(beta=0.0, kappa=0.0, mu=0.0)
    assert xi_opt == pytest.approx(2.84, abs=0.10)
    assert hm_max == pytest.approx(1.068, abs=2e-2)


def test_hm_at_xi_one_matches_full_optimisation() -> None:
    """At any ξ, h_m must be ≥ h(σ=0)."""
    xi = 1.0
    h_zero = bk.h_factor(xi=xi, sigma=0.0)
    hm = bk.h_m_factor(xi=xi)
    assert hm >= h_zero - 1e-9


def test_hm_optimum_strict_bounds_never_evaluates_negative_xi() -> None:
    """Regression test: scipy minimize_scalar with method='brent' was
    extrapolating outside the initial bracket and asking h_factor to
    evaluate at negative ξ (raising ValueError on h_factor's xi > 0 guard).
    The current implementation uses method='bounded' which respects
    xi_bounds strictly.

    Uses β = 4 (a moderate walk-off case where ξ_opt sits well inside any
    reasonable bracket) rather than the much-slower β ≈ 18 from the
    Friedenauer BBO notebook. The mechanical property under test is
    "bounded minimization respects bounds" — that property is wavelength-
    and walk-off-independent, so β = 4 covers the regression while
    keeping the test under a few seconds.
    """
    xi_opt, hm_max = bk.h_m_optimum(beta=4.0, kappa=0.0, mu=0.0, xi_bounds=(0.05, 5.0))
    assert 0.05 < xi_opt < 5.0
    assert hm_max > 0.0


def test_hm_optimum_rejects_invalid_bounds() -> None:
    with pytest.raises(ValueError, match="xi_bounds"):
        bk.h_m_optimum(beta=0.0, xi_bounds=(0.0, 5.0))
    with pytest.raises(ValueError, match="xi_bounds"):
        bk.h_m_optimum(beta=0.0, xi_bounds=(2.0, 1.0))


# =====================================================================
# Walk-off and absorption monotonically reduce h
# =====================================================================


def test_walkoff_reduces_h() -> None:
    xi = 2.84
    h_no_walkoff = bk.h_factor(xi=xi, sigma=0.0, beta=0.0)
    h_with_walkoff = bk.h_factor(xi=xi, sigma=0.0, beta=1.0)
    assert h_with_walkoff < h_no_walkoff


def test_absorption_reduces_h() -> None:
    xi = 2.84
    h_lossless = bk.h_factor(xi=xi, sigma=0.0, kappa=0.0)
    h_lossy = bk.h_factor(xi=xi, sigma=0.0, alpha_omega_L=1.0)
    assert h_lossy < h_lossless


def test_offcentre_focus_reduces_h_in_symmetric_case() -> None:
    """μ=0 is the symmetric optimum in the σ=β=κ=0 case."""
    xi = 2.0
    h_centred = bk.h_factor(xi=xi, mu=0.0)
    h_off = bk.h_factor(xi=xi, mu=0.5)
    assert h_off < h_centred


@pytest.mark.parametrize(
    "xi, sigma, beta",
    [
        (0.2, 0.9, 0.0),
        (1.0, 0.7, 1.0),
        (2.84, 0.57, 0.0),
        (4.0, 0.5, 4.0),
        (1.41317, 0.8, 18.0166),
        (0.5, -1.0, 8.0),
    ],
)
def test_reduced_integral_against_independent_tensor_rule(
    xi: float, sigma: float, beta: float
) -> None:
    coarse = tensor_h(xi, sigma, beta, order=256)
    fine = tensor_h(xi, sigma, beta, order=512)
    assert coarse == pytest.approx(fine, rel=2e-8, abs=1e-10)
    assert bk.h_factor(xi, sigma, beta) == pytest.approx(fine, rel=2e-8, abs=1e-10)


@pytest.mark.parametrize(
    "xi, beta", [(0.3, 0.0), (2.84, 0.0), (8.0, 1.0), (1.41317, 18.0166)]
)
def test_phase_lobes_against_independent_dense_scan(xi: float, beta: float) -> None:
    # The reference uses neither production quadrature nor its optimiser.
    values = [tensor_h(xi, float(sigma), beta) for sigma in np.linspace(-6.0, 6.0, 481)]
    hm = bk.h_m_factor(xi, beta)
    assert hm >= max(values) - 1e-9
    assert hm == pytest.approx(max(values), rel=5e-4)


def test_phase_bounds_include_endpoint_maximum() -> None:
    assert bk.h_m_factor(2.84, sigma_bracket=(-0.1, 0.0)) == pytest.approx(
        bk.h_factor(2.84, sigma=0.0), rel=1e-10
    )
    assert bk.h_m_factor(2.84, sigma_bracket=(0.5, 0.6)) > 1.06


def test_bbo_diagnostic_anchor_and_optimum_waist() -> None:
    assert bk.h_m_factor(1.41317, 18.0166) == pytest.approx(0.0392431, rel=3e-6)
    xi, hm = bk.h_m_optimum(18.0166)
    waist_m = math.sqrt(0.01 * 559e-9 / (2.0 * math.pi * 1.67276 * xi))
    assert waist_m == pytest.approx(19.346e-6, abs=0.002e-6)
    assert hm >= bk.h_m_factor(1.41317, 18.0166)


@pytest.mark.parametrize("A1, A2", [(0.7, 0.0), (0.0, 1.4), (0.7, 1.4)])
def test_separate_absorption_plane_wave_limits(A1: float, A2: float) -> None:
    # Integrate a constant source with pump attenuation and exit propagation.
    a = A1 - A2 / 2.0
    amplitude = math.exp(-A2 / 2.0) * (-math.expm1(-a) / a if a else 1.0)
    xi = 1e-5
    assert bk.h_factor(xi, alpha_omega_L=A1, alpha_2omega_L=A2) / xi == pytest.approx(
        amplitude**2, rel=1e-9
    )


@pytest.mark.parametrize("mu", [-0.6, 0.6])
@pytest.mark.parametrize("A1, A2", [(0.9, 0.0), (0.0, 1.2)])
def test_absorbing_offset_focus_against_propagation_ode(
    mu: float, A1: float, A2: float
) -> None:
    xi, sigma = 1.7, 0.6
    focus_s = (1.0 + mu) / 2.0

    def propagate(s: float, q: np.ndarray) -> np.ndarray:
        tau = 2.0 * xi * (s - focus_s)
        source = np.exp(-A1 * s + 1j * sigma * tau) / (1.0 + 1j * tau)
        return source - A2 / 2.0 * q

    sol = solve_ivp(propagate, (0.0, 1.0), [0j], rtol=1e-11, atol=1e-13)
    assert sol.success
    expected = xi * abs(sol.y[0, -1]) ** 2
    assert bk.h_factor(
        xi, sigma, mu=mu, alpha_omega_L=A1, alpha_2omega_L=A2
    ) == pytest.approx(expected, rel=2e-9)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"xi": math.nan},
        {"xi": math.inf},
        {"sigma": math.nan},
        {"beta": -1.0},
        {"mu": math.inf},
        {"alpha_omega_L": -0.1},
        {"alpha_2omega_L": math.inf},
        {"kappa": 0.1},
    ],
)
def test_invalid_bk_conventions(kwargs: dict[str, float]) -> None:
    with pytest.raises(ValueError):
        bk.h_factor(**({"xi": 1.0} | kwargs))


@pytest.mark.parametrize(
    "bounds", [(0.0, 0.0), (2.0, 1.0), (math.nan, 1.0), (0.0, math.inf)]
)
def test_invalid_phase_bounds(bounds: tuple[float, float]) -> None:
    with pytest.raises(ValueError, match="sigma_bracket"):
        bk.h_m_factor(1.0, sigma_bracket=bounds)
