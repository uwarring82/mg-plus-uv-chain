"""
shg_single_pass.py — single-pass SHG efficiency coefficient
===========================================================

Architecture-NEUTRAL conversion from the Boyd–Kleinman dimensionless
focusing factor `h_m` to the engineering single-pass efficiency
coefficient `γ_SHG` (units W⁻¹), plus harmonic-power and conversion-
fraction evaluators for both the small-signal and depleted (tanh²)
regimes.

Per CHARTER §5.1, this module contains no crystal preset, no
wavelength preset, and no architecture preset. All parameter values
flow from callers.
"""

from __future__ import annotations

import math

from src.parameters import SPEED_OF_LIGHT_m_per_s, VACUUM_PERMITTIVITY_F_per_m

# =====================================================================
# Material constant K
# =====================================================================


def boyd_kleinman_K_factor(
    d_eff_mV: float,
    n_omega: float,
    n_2omega: float,
    wavelength_m: float,
) -> float:
    """
    Material constant *K* (SI units W⁻¹) in the Boyd–Kleinman formula

        P₂ = K · L · k₁ · h · P₁²

    Parameters
    ----------
    d_eff_mV : float
        Effective nonlinear coefficient in m/V.
    n_omega : float
        Refractive index at the fundamental.
    n_2omega : float
        Refractive index at the harmonic.
    wavelength_m : float
        Vacuum wavelength of the fundamental in metres.

    Returns
    -------
    float
        *K* in W⁻¹.
    """
    # Daniel, Tsai & Hemmerling (2020), Eq. (1):
    # https://arxiv.org/abs/2009.08430. L*k1 is dimensionless, so K is W^-1.
    if not math.isfinite(d_eff_mV):
        raise ValueError("d_eff_mV must be finite")
    if not math.isfinite(wavelength_m) or wavelength_m <= 0.0:
        raise ValueError(f"wavelength_m must be positive; got {wavelength_m}")
    if any(not math.isfinite(n) or n <= 0.0 for n in (n_omega, n_2omega)):
        raise ValueError("refractive indices must be positive")

    c = SPEED_OF_LIGHT_m_per_s
    eps0 = VACUUM_PERMITTIVITY_F_per_m
    omega = 2.0 * math.pi * c / wavelength_m

    return (2.0 * omega**2 * d_eff_mV**2) / (
        math.pi * eps0 * c**3 * n_omega**2 * n_2omega
    )


# =====================================================================
# γ_SHG coefficient
# =====================================================================


def gamma_shg_coefficient(
    d_eff_mV: float,
    n_omega: float,
    n_2omega: float,
    wavelength_m: float,
    length_m: float,
    h_m: float,
) -> float:
    """
    Single-pass SHG efficiency coefficient γ_SHG (W⁻¹).

    For small-signal (non-depleted) operation::

        P₂ω = γ_SHG · Pω²

    and for the depleted regime::

        P₂ω = Pω · tanh²(√(γ_SHG · Pω))

    Parameters
    ----------
    d_eff_mV, n_omega, n_2omega, wavelength_m
        As in :func:`boyd_kleinman_K_factor`.
    length_m : float
        Crystal length in metres.
    h_m : float
        Dimensionless Boyd–Kleinman focusing factor (e.g. from
        :func:`boyd_kleinman.h_m_factor` or :func:`boyd_kleinman.h_m_optimum`).

    Returns
    -------
    float
        γ_SHG in W⁻¹.
    """
    if not math.isfinite(length_m) or length_m < 0.0:
        raise ValueError(f"length_m must be non-negative; got {length_m}")
    if not math.isfinite(h_m) or h_m < 0.0:
        raise ValueError(f"h_m must be non-negative; got {h_m}")

    K = boyd_kleinman_K_factor(d_eff_mV, n_omega, n_2omega, wavelength_m)
    k1 = 2.0 * math.pi * n_omega / wavelength_m
    return K * k1 * length_m * h_m


# =====================================================================
# Harmonic power and conversion fraction
# =====================================================================


def single_pass_harmonic_power_W(
    power_in_W: float,
    gamma_shg: float,
    regime: str = "auto",
) -> float:
    """
    Single-pass harmonic power (W).

    Parameters
    ----------
    power_in_W : float
        Fundamental power in watts.
    gamma_shg : float
        Single-pass efficiency coefficient in W⁻¹.
    regime : {"auto", "small", "depleted"}
        ``"small"`` returns the undepleted approximation γ·P², valid
        only for γ·P ≪ 1; it is not bounded by the input power.
        ``"depleted"`` and ``"auto"`` both use the continuous tanh²
        model at every power, recovering the small-signal limit smoothly.
        This is an effective depletion model using a fixed focusing factor,
        not an exact solution of depleted, focused propagation.

    Returns
    -------
    float
        Harmonic power in watts. Bounded by input power for ``"auto"``
        and ``"depleted"`` only.
    """
    return power_in_W * single_pass_conversion_fraction(power_in_W, gamma_shg, regime)


def single_pass_conversion_fraction(
    power_in_W: float,
    gamma_shg: float,
    regime: str = "auto",
) -> float:
    """
    Single-pass conversion fraction η = P₂ω / Pω.

    Parameters
    ----------
    power_in_W, gamma_shg, regime
        As in :func:`single_pass_harmonic_power_W`. Inputs must be finite
        and non-negative, including when either input is zero.

    Returns
    -------
    float
        Fraction in [0, 1] for ``"auto"`` and ``"depleted"``. The explicit
        ``"small"`` approximation returns γ·P and is not bounded above.
        At zero input power the limiting fraction is zero.
    """
    if regime not in ("auto", "small", "depleted"):
        raise ValueError(f"regime must be 'auto', 'small', or 'depleted'; got {regime}")
    if not math.isfinite(power_in_W) or power_in_W < 0.0:
        raise ValueError(
            f"power_in_W must be finite and non-negative; got {power_in_W}"
        )
    if not math.isfinite(gamma_shg) or gamma_shg < 0.0:
        raise ValueError(f"gamma_shg must be finite and non-negative; got {gamma_shg}")
    if regime == "small":
        return gamma_shg * power_in_W
    # Taking the roots first avoids overflowing/underflowing γ·P before
    # evaluating the saturation law. tanh(inf) = 1 for finite extreme inputs.
    return math.tanh(math.sqrt(gamma_shg) * math.sqrt(power_in_W)) ** 2
