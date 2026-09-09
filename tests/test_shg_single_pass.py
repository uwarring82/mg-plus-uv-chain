"""
test_shg_single_pass.py
=======================

Tests for src/shg_single_pass.py.
"""

from __future__ import annotations

import math

import pytest

from src import boyd_kleinman
from src.parameters import SPEED_OF_LIGHT_m_per_s, VACUUM_PERMITTIVITY_F_per_m
from src.shg_single_pass import (
    boyd_kleinman_K_factor,
    gamma_shg_coefficient,
    single_pass_conversion_fraction,
    single_pass_harmonic_power_W,
)

# =====================================================================
# gamma_shg_coefficient & boyd_kleinman_K_factor
# =====================================================================


def test_gamma_shg_dimensional_scaling() -> None:
    """γ_SHG scales correctly with physical parameters."""
    base = dict(
        d_eff_mV=1e-12,
        n_omega=1.5,
        n_2omega=1.5,
        wavelength_m=1e-6,
        length_m=0.01,
        h_m=1.0,
    )
    gamma_base = gamma_shg_coefficient(**base)

    # γ ∝ d_eff²
    doubled_d = {**base, "d_eff_mV": 2e-12}
    assert gamma_shg_coefficient(**doubled_d) == pytest.approx(
        4.0 * gamma_base, rel=1e-12
    )

    # γ ∝ L
    doubled_L = {**base, "length_m": 0.02}
    assert gamma_shg_coefficient(**doubled_L) == pytest.approx(
        2.0 * gamma_base, rel=1e-12
    )

    # γ ∝ h_m
    doubled_h = {**base, "h_m": 2.0}
    assert gamma_shg_coefficient(**doubled_h) == pytest.approx(
        2.0 * gamma_base, rel=1e-12
    )


def test_gamma_shg_wavelength_scaling() -> None:
    """For fixed n and h_m, γ_SHG ∝ 1/λ³."""
    base = dict(
        d_eff_mV=1e-12,
        n_omega=1.5,
        n_2omega=1.5,
        wavelength_m=1e-6,
        length_m=0.01,
        h_m=1.0,
    )
    gamma_1 = gamma_shg_coefficient(**base)
    gamma_2 = gamma_shg_coefficient(**{**base, "wavelength_m": 2e-6})
    # K ∝ 1/λ², k₁ ∝ 1/λ, so γ ∝ 1/λ³
    expected_ratio = (1e-6 / 2e-6) ** 3
    assert gamma_2 == pytest.approx(gamma_1 * expected_ratio, rel=1e-12)


@pytest.mark.parametrize("n_omega, n_harmonic", [(1.5, 1.7), (2.0, 2.4)])
def test_absolute_weak_focus_normalisation(n_omega: float, n_harmonic: float) -> None:
    """Integrate the plane-wave generated intensity over a Gaussian pump.

    For physical peak fields, dE₂/dz = iωd_eff E₁²/(n₂c) and
    I_j = n_j ε₀ c |E_j|²/2. This oracle never calls the K helper.
    """
    from scipy.integrate import quad

    c, eps0 = SPEED_OF_LIGHT_m_per_s, VACUUM_PERMITTIVITY_F_per_m
    power, waist, length, wavelength, d_eff = 1.3, 1e-3, 1e-4, 1e-6, 1e-12
    omega = 2.0 * math.pi * c / wavelength

    def radial_power(u: float) -> float:
        intensity = 2.0 * power / (math.pi * waist**2) * math.exp(-2.0 * u**2)
        field_sq = 2.0 * intensity / (n_omega * eps0 * c)
        harmonic_field = omega * d_eff * length / (n_harmonic * c) * field_sq
        harmonic_intensity = n_harmonic * eps0 * c / 2.0 * harmonic_field**2
        return 2.0 * math.pi * waist**2 * u * harmonic_intensity

    expected, _ = quad(radial_power, 0.0, 8.0, epsabs=1e-25, epsrel=1e-11)
    xi = length * wavelength / (2.0 * math.pi * n_omega * waist**2)
    h = boyd_kleinman.h_factor(xi)
    gamma = gamma_shg_coefficient(d_eff, n_omega, n_harmonic, wavelength, length, h)
    assert gamma * power**2 == pytest.approx(expected, rel=1e-9)


def test_gamma_shg_cross_check_vs_boyd_kleinman() -> None:
    """
    At ξ = 2.84, β = κ = μ = 0, h_m ≈ 1.068. Verify that γ_SHG recovers
    K · L · k₁ · 1.068 to numerical precision.
    """
    d_eff = 0.84e-12
    n_omega = 1.6
    n_2omega = 1.6
    wavelength = 1.118e-6
    length = 1.8e-2

    h_m = boyd_kleinman.h_m_factor(xi=2.84, beta=0.0, kappa=0.0, mu=0.0)
    gamma = gamma_shg_coefficient(d_eff, n_omega, n_2omega, wavelength, length, h_m)

    K = boyd_kleinman_K_factor(d_eff, n_omega, n_2omega, wavelength)
    k1 = 2.0 * math.pi * n_omega / wavelength
    expected = K * k1 * length * h_m

    assert gamma == pytest.approx(expected, rel=1e-12)
    # Also verify h_m is close to the textbook 1.068
    assert h_m == pytest.approx(1.068, abs=1e-3)


# =====================================================================
# single_pass_harmonic_power_W
# =====================================================================


def test_small_signal_harmonic_power() -> None:
    """Small-signal regime: P₂ω = γ P²."""
    gamma = 0.01
    P = 1.0
    assert single_pass_harmonic_power_W(P, gamma, "small") == pytest.approx(
        gamma * P**2, rel=1e-12
    )


def test_small_signal_fraction() -> None:
    """Small-signal regime: η = γ P."""
    gamma = 0.01
    P = 1.0
    assert single_pass_conversion_fraction(P, gamma, "small") == pytest.approx(
        gamma * P, rel=1e-12
    )


def test_depleted_harmonic_saturates_to_pump() -> None:
    """
    As γP → ∞, tanh²(√(γP)) → 1 and harmonic power → pump power
    (Manley–Rowe ceiling).
    """
    P = 2.5
    gamma = 1e6  # very large → depleted regime
    result = single_pass_harmonic_power_W(P, gamma, "depleted")
    assert result == pytest.approx(P, rel=1e-12)


def test_depleted_fraction_saturates_to_one() -> None:
    """As γP → ∞, conversion fraction → 1."""
    P = 2.5
    gamma = 1e6
    assert single_pass_conversion_fraction(P, gamma, "depleted") == pytest.approx(
        1.0, rel=1e-12
    )


def test_auto_is_continuous_and_increasing_at_old_switch() -> None:
    points = [0.049999, math.nextafter(0.05, 0.0), 0.05, 0.050001]
    fractions = [single_pass_conversion_fraction(1.0, x) for x in points]
    assert all(a <= b for a, b in zip(fractions, fractions[1:], strict=False))
    # A finite slope over the original review's sampling points, no 3.35% drop.
    assert 0 < fractions[2] - fractions[0] < 1e-6
    assert fractions[1] == pytest.approx(fractions[2], rel=1e-14)


@pytest.mark.parametrize("x", [1e-12, 1e-8, 1e-5])
def test_auto_recovers_small_signal_limit(x: float) -> None:
    eta = single_pass_conversion_fraction(1.0, x)
    assert eta == pytest.approx(x, rel=x)
    assert eta <= x


def test_explicit_small_is_unbounded_approximation() -> None:
    assert single_pass_harmonic_power_W(2.0, 1.0, "small") == 4.0
    assert single_pass_conversion_fraction(2.0, 1.0, "small") == 2.0
    assert single_pass_conversion_fraction(2.0, 1.0) < 1.0


@pytest.mark.parametrize("bad", [-1.0, math.nan, math.inf, -math.inf])
@pytest.mark.parametrize("other", [0.0, 1.0])
def test_invalid_inputs_even_at_zero(bad: float, other: float) -> None:
    for fn in (single_pass_harmonic_power_W, single_pass_conversion_fraction):
        with pytest.raises(ValueError):
            fn(bad, other)
        with pytest.raises(ValueError):
            fn(other, bad)


@pytest.mark.parametrize("P, gamma", [(0.0, 1.0), (1.0, 0.0), (1.0, 1.0)])
def test_invalid_regime_even_at_zero(P: float, gamma: float) -> None:
    for fn in (single_pass_harmonic_power_W, single_pass_conversion_fraction):
        with pytest.raises(ValueError, match="regime"):
            fn(P, gamma, "typo")


def test_finite_extreme_inputs_saturate_without_overflow() -> None:
    assert single_pass_harmonic_power_W(1e300, 1e300) == 1e300
    assert single_pass_conversion_fraction(1e-300, 1e300) == pytest.approx(
        math.tanh(1.0) ** 2
    )


def test_energy_conservation_bound() -> None:
    """Harmonic power never exceeds pump power for any γ > 0, P > 0."""
    test_cases = [
        (0.01, 1.0),
        (0.1, 10.0),
        (1.0, 0.5),
        (10.0, 100.0),
        (1e-4, 1e3),
        (1e-6, 1e6),
    ]
    for gamma, P in test_cases:
        harmonic = single_pass_harmonic_power_W(P, gamma, "auto")
        assert harmonic <= P + 1e-15, f"Energy violation at γ={gamma}, P={P}"
        fraction = single_pass_conversion_fraction(P, gamma, "auto")
        assert 0.0 <= fraction <= 1.0 + 1e-15


def test_zero_power_returns_zero() -> None:
    """Zero input gives zero output."""
    assert single_pass_harmonic_power_W(0.0, 0.01, "auto") == 0.0
    assert single_pass_conversion_fraction(0.0, 0.01, "auto") == 0.0
    assert single_pass_harmonic_power_W(1.0, 0.0, "auto") == 0.0


def test_invalid_inputs_raise() -> None:
    """Negative power or gamma raises ValueError."""
    with pytest.raises(ValueError):
        single_pass_harmonic_power_W(-1.0, 0.01)
    with pytest.raises(ValueError):
        single_pass_harmonic_power_W(1.0, -0.01)
    with pytest.raises(ValueError):
        gamma_shg_coefficient(1e-12, 1.5, 1.5, -1e-6, 0.01, 1.0)
    with pytest.raises(ValueError):
        gamma_shg_coefficient(1e-12, 1.5, 1.5, 1e-6, -0.01, 1.0)


@pytest.mark.parametrize("index", range(6))
@pytest.mark.parametrize("bad", [math.nan, math.inf, -math.inf])
def test_nonfinite_gamma_coefficient_inputs(index: int, bad: float) -> None:
    args = [1e-12, 1.5, 1.7, 1e-6, 0.01, 1.0]
    args[index] = bad
    with pytest.raises(ValueError):
        gamma_shg_coefficient(*args)
