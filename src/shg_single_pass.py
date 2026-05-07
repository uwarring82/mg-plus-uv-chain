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
    Material constant *K* (SI units W⁻¹·m⁻¹) in the Boyd–Kleinman formula

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
        *K* in W⁻¹·m⁻¹.
    """
    if wavelength_m <= 0.0:
        raise ValueError(f"wavelength_m must be positive; got {wavelength_m}")
    if n_omega <= 0.0 or n_2omega <= 0.0:
        raise ValueError("refractive indices must be positive")

    c = SPEED_OF_LIGHT_m_per_s
    eps0 = VACUUM_PERMITTIVITY_F_per_m
    omega = 2.0 * math.pi * c / wavelength_m

    return (2.0 * omega**2 * d_eff_mV**2) / (
        math.pi * eps0 * c**3 * n_omega * n_2omega
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
    if length_m < 0.0:
        raise ValueError(f"length_m must be non-negative; got {length_m}")
    if h_m < 0.0:
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
        ``"small"`` forces the non-depleted expression γ·P².
        ``"depleted"`` forces the exact tanh² expression.
        ``"auto"`` selects ``"small"`` when γ·P < 0.05 (5 % single-pass
        conversion) and ``"depleted"`` otherwise.

    Returns
    -------
    float
        Harmonic power in watts. Always ≤ ``power_in_W``.
    """
    if power_in_W < 0.0:
        raise ValueError(f"power_in_W must be non-negative; got {power_in_W}")
    if gamma_shg < 0.0:
        raise ValueError(f"gamma_shg must be non-negative; got {gamma_shg}")
    if power_in_W == 0.0 or gamma_shg == 0.0:
        return 0.0

    gamma_p = gamma_shg * power_in_W

    if regime == "auto":
        regime = "small" if gamma_p < 0.05 else "depleted"

    if regime == "small":
        return gamma_shg * power_in_W**2
    elif regime == "depleted":
        # For very large gamma_p, tanh(sqrt(gamma_p)) is 1.0 to machine precision.
        if gamma_p > 700.0:
            return power_in_W
        return power_in_W * math.tanh(math.sqrt(gamma_p)) ** 2
    else:
        raise ValueError(
            f"regime must be 'auto', 'small', or 'depleted'; got {regime}"
        )


def single_pass_conversion_fraction(
    power_in_W: float,
    gamma_shg: float,
    regime: str = "auto",
) -> float:
    """
    Single-pass conversion fraction η = P₂ω / Pω, dimensionless in [0, 1].

    This is the quantity consumed by the enhancement-cavity solver in
    Phase B.

    Parameters
    ----------
    power_in_W, gamma_shg, regime
        As in :func:`single_pass_harmonic_power_W`.

    Returns
    -------
    float
        Conversion fraction in [0, 1].
    """
    if power_in_W == 0.0:
        return 0.0
    return single_pass_harmonic_power_W(power_in_W, gamma_shg, regime) / power_in_W
