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
    - Phase mismatch reduces h relative to σ=0 (in the lossless,
      no-walk-off case where σ=0 is exactly optimum)
    - Off-centre focus (μ ≠ 0) reduces h relative to centred focus
      (in the symmetric lossless case)
    - Edge: xi <= 0 raises ValueError

Reference: G. D. Boyd & D. A. Kleinman, J. Appl. Phys. 39, 3597 (1968).
"""

from __future__ import annotations

import math

import pytest

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
    """In the lossless, no-walk-off, centred-focus case, σ=0 is the maximum."""
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
    xi_opt, hm_max = bk.h_m_optimum(beta=4.0, kappa=0.0, mu=0.0,
                                    xi_bounds=(0.05, 5.0))
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
    h_lossy = bk.h_factor(xi=xi, sigma=0.0, kappa=0.5)
    assert h_lossy < h_lossless


def test_offcentre_focus_reduces_h_in_symmetric_case() -> None:
    """μ=0 is the symmetric optimum in the σ=β=κ=0 case."""
    xi = 2.0
    h_centred = bk.h_factor(xi=xi, mu=0.0)
    h_off = bk.h_factor(xi=xi, mu=0.5)
    assert h_off < h_centred
