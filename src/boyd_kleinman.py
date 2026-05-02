"""
boyd_kleinman.py — generic Boyd-Kleinman SHG focusing utility
==============================================================

Architecture-NEUTRAL implementation of the Boyd-Kleinman (1968) focusing
function h(σ, β, κ, ξ) for second-harmonic generation with a focused
Gaussian pump in a non-depleted-pump approximation.

Reference: G. D. Boyd & D. A. Kleinman, *J. Appl. Phys.* **39**, 3597 (1968).
This module implements the generic function only; it does NOT contain
architecture- or material-specific presets (no BBO-at-280nm shortcut, no
quadrupling-stage shortcut, etc.). Per CHARTER §5.1, this places the
module in the architecture-neutral pre-G1 layer.

Conventions
-----------
- All inputs and outputs SI per CONVENTIONS §1.
- Focusing parameter: ξ = L / b, where L is crystal length and b = 2 z_R
  is the confocal parameter (z_R = π w_0² / λ).
- Phase-mismatch parameter: σ = (1/2) Δk · b, dimensionless.
- Walk-off parameter: β = (1/2) ρ √(L k₁), dimensionless.
- Absorption parameter: κ = (α₁ + α₂/2) · L / 2, dimensionless.
- Focus position: μ = (z_focus − L/2) / (L/2), dimensionless. μ = 0 at
  crystal centre.

The output h is dimensionless and enters

    P_2 = K · L · k₁ · h(σ, β, κ, ξ, μ) · P_1²

where K is the standard Boyd-Kleinman material constant
(deff², refractive indices, ω). K is *not* computed here — it is
material- and wavelength-specific and lives downstream of crystal choice.

Charter compliance
------------------
This module is architecture-neutral:
- No crystal preset, no wavelength preset, no architecture preset.
- All parameter values flow from Phase 0.5 / Phase 1 inputs at call sites.
- The σ-optimised variant `h_m` is provided because optimisation over σ is
  a property of the focusing function itself, not of any architecture.
"""

from __future__ import annotations

import math

import numpy as np
from scipy import integrate, optimize


# =====================================================================
# Core BK h-function (generic σ, β, κ, ξ, μ)
# =====================================================================


def h_factor(
    xi: float,
    sigma: float = 0.0,
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
) -> float:
    """
    Boyd-Kleinman SHG focusing function h(σ, β, κ, ξ, μ).

    Computes the generic BK focusing factor by direct numerical evaluation of
    the BK 1968 double integral. No simplifications beyond the BK derivation
    itself (non-depleted pump, paraxial Gaussian, slowly varying envelope).

    Parameters
    ----------
    xi : float
        Focusing parameter ξ = L / b. Must be > 0.
    sigma : float
        Phase-mismatch parameter σ = (1/2) Δk · b. Default 0 (perfect match).
    beta : float
        Walk-off parameter β = (1/2) ρ √(L k₁). Default 0 (no walk-off).
    kappa : float
        Absorption parameter κ = (α₁ + α₂/2) · L / 2. Default 0 (lossless).
    mu : float
        Normalised focus offset, μ = (z_focus − L/2)/(L/2). Default 0 (centre).

    Returns
    -------
    float
        h(σ, β, κ, ξ, μ), dimensionless.

    Notes
    -----
    Uses scipy.integrate.dblquad over τ, τ' ∈ [−ξ + μξ, ξ + μξ]. The
    integrand is

        exp[−κ ξ (1 + (τ + τ')/(2ξ))] · exp[−β² (τ − τ')²]
        · exp[i σ (τ − τ')]                          (phase factor)
        · 1 / [(1 + i τ)(1 − i τ')]

    Real and imaginary parts of the integrand are integrated separately
    (scipy's dblquad expects real integrands). The result is taken as the
    real part of the complex double integral, divided by 4ξ.
    """
    if xi <= 0.0:
        raise ValueError(f"xi must be positive; got {xi}")

    tau_low = -xi + mu * xi
    tau_high = xi + mu * xi

    def integrand_real(tau_p: float, tau: float) -> float:
        diff = tau - tau_p
        sum_ = tau + tau_p
        amp = math.exp(-kappa * (xi + sum_ / 2.0)) * math.exp(-beta * beta * diff * diff)
        # 1 / ((1 + i τ)(1 − i τ')) · exp(i σ diff)
        denom = (1 + 1j * tau) * (1 - 1j * tau_p)
        z = amp * np.exp(1j * sigma * diff) / denom
        return z.real

    def integrand_imag(tau_p: float, tau: float) -> float:
        diff = tau - tau_p
        sum_ = tau + tau_p
        amp = math.exp(-kappa * (xi + sum_ / 2.0)) * math.exp(-beta * beta * diff * diff)
        denom = (1 + 1j * tau) * (1 - 1j * tau_p)
        z = amp * np.exp(1j * sigma * diff) / denom
        return z.imag

    real_part, _ = integrate.dblquad(
        integrand_real,
        tau_low,
        tau_high,
        tau_low,
        tau_high,
        epsabs=1e-9,
        epsrel=1e-7,
    )
    # Imaginary part is exactly zero by symmetry for real outputs;
    # we don't need to evaluate it. h is real by construction.
    return real_part / (4.0 * xi)


# =====================================================================
# σ-optimised BK function h_m(ξ, β, κ, μ)
# =====================================================================


def h_m_factor(
    xi: float,
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
    *,
    sigma_bracket: tuple[float, float] = (-6.0, 6.0),
) -> float:
    """
    σ-optimised BK focusing function h_m(ξ, β, κ, μ) = max_σ h(σ, β, κ, ξ, μ).

    For phase-matchable SHG the experimentalist tunes σ (via temperature /
    angle) for maximum conversion. h_m captures that operating point.

    Parameters
    ----------
    xi, beta, kappa, mu
        As in :func:`h_factor`.
    sigma_bracket
        Interval over which to search for the optimum σ. The default
        (−6, 6) is wide enough for the standard ξ ∈ [0.1, 10] regime.

    Returns
    -------
    float
        h_m(ξ, β, κ, μ).
    """
    if xi <= 0.0:
        raise ValueError(f"xi must be positive; got {xi}")

    def neg_h(sigma: float) -> float:
        return -h_factor(xi=xi, sigma=sigma, beta=beta, kappa=kappa, mu=mu)

    result = optimize.minimize_scalar(
        neg_h,
        bracket=sigma_bracket,
        method="brent",
        options={"xtol": 1e-6},
    )
    return -result.fun


# =====================================================================
# Optimum focus ξ_opt for given (β, κ, μ) under σ-optimisation
# =====================================================================


def h_m_optimum(
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
    *,
    xi_bounds: tuple[float, float] = (0.05, 10.0),
) -> tuple[float, float]:
    """
    Find ξ_opt and h_m_max for given (β, κ, μ).

    For (β, κ, μ) = (0, 0, 0), the classic Boyd-Kleinman result is
    ξ_opt ≈ 2.84, h_m_max ≈ 1.068.

    Parameters
    ----------
    beta, kappa, mu
        As in :func:`h_factor`.
    xi_bounds
        Strict bounds on ξ for the search. Must be positive on both ends —
        scipy's `bounded` method respects them, so the underlying
        :func:`h_factor` is never asked to evaluate at ξ ≤ 0.

    Returns
    -------
    (xi_opt, h_m_max) : tuple[float, float]
        Optimum focusing parameter and the corresponding σ-optimised h.
    """
    lo, hi = xi_bounds
    if lo <= 0.0 or hi <= lo:
        raise ValueError(
            f"xi_bounds must be (positive, larger-positive); got {xi_bounds}"
        )

    def neg_hm(xi: float) -> float:
        return -h_m_factor(xi=xi, beta=beta, kappa=kappa, mu=mu)

    result = optimize.minimize_scalar(
        neg_hm,
        bounds=xi_bounds,
        method="bounded",
        options={"xatol": 1e-5},
    )
    return float(result.x), float(-result.fun)


# =====================================================================
# Analytic limit (σ = β = κ = 0, μ = 0)
# =====================================================================


def h_analytic_no_walkoff_no_loss(xi: float) -> float:
    """
    Closed-form h(σ=0, β=0, κ=0, ξ, μ=0) = arctan²(ξ) / ξ.

    Useful as a sanity / unit-test reference for :func:`h_factor` in the
    perfect-phase-match, no-walk-off, no-absorption limit.

    Derivation: with σ = β = κ = 0 the BK double integral factorises:

        h = (1 / 4ξ) · |∫_{−ξ}^{ξ} dτ / (1 + iτ)|²
          = (1 / 4ξ) · (2 arctan ξ)²
          = arctan²(ξ) / ξ.

    The maximum of arctan²(ξ)/ξ is at ξ ≈ 1.392 with h ≈ 0.646. This is
    *not* the famous BK optimum ξ ≈ 2.84, h ≈ 1.068 — that result requires
    σ to be optimised (use :func:`h_m_optimum`).
    """
    if xi <= 0.0:
        raise ValueError(f"xi must be positive; got {xi}")
    return math.atan(xi) ** 2 / xi
