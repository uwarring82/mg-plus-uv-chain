"""Architecture-neutral Boyd–Kleinman SHG focusing factors.

Conventions follow Daniel, Tsai & Hemmerling (2020), Eqs. (1)–(3),
https://arxiv.org/abs/2009.08430, for a paraxial, undepleted Gaussian pump:

* ξ = L/b, b = k₁ w₀² = 2z_R, k₁ = 2πn₁/λ_vac.
* σ = b(2k₁-k₂)/2. σ=0 is wave-vector matching, not the Gouy-phase optimum.
* β is the paper's B = ρ sqrt(Lk₁)/2; its kernel is exp[-B²(τ-τ′)²/ξ].
* μ = 2z_focus/L - 1, hence τ = 2ξ z/L - ξ(1+μ).
* alpha_omega_L and alpha_2omega_L are intensity absorption optical depths
  α₁L and α₂L. Pump power is referenced at the crystal entrance; harmonic
  power is evaluated at the exit. A source at s=z/L has amplitude weight
  exp[-α₁L s - α₂L(1-s)/2]. These two depths cannot be inferred from the
  old single κ=(α₁+α₂/2)L/2 argument.

The absorption extension and limits are derived in
logbook/2026-09-09-numerical-foundations.md. K is computed downstream by
src.shg_single_pass. All parameters come from callers (CHARTER §5.1).
"""

from __future__ import annotations

import cmath
import math

import numpy as np
from scipy import integrate, optimize


def _validate(
    xi: float,
    sigma: float,
    beta: float,
    kappa: float,
    mu: float,
    alpha_omega_L: float,
    alpha_2omega_L: float,
) -> None:
    if not math.isfinite(xi) or xi <= 0.0:
        raise ValueError(f"xi must be positive and finite; got {xi}")
    if not all(
        math.isfinite(x)
        for x in (sigma, beta, kappa, mu, alpha_omega_L, alpha_2omega_L)
    ):
        raise ValueError("BK inputs must be finite")
    if beta < 0.0 or alpha_omega_L < 0.0 or alpha_2omega_L < 0.0:
        raise ValueError(
            "walk-off magnitude and absorption depths must be non-negative"
        )
    if kappa != 0.0:
        raise ValueError(
            "nonzero legacy kappa is ambiguous: supply alpha_omega_L=alpha1*L "
            "and alpha_2omega_L=alpha2*L separately (intensity absorption)"
        )


def h_factor(
    xi: float,
    sigma: float = 0.0,
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
    *,
    alpha_omega_L: float = 0.0,
    alpha_2omega_L: float = 0.0,
) -> float:
    """Return the dimensionless, undepleted SHG focusing factor.

    Parameters
    ----------
    xi, sigma, beta, mu : float
        Dimensionless focusing, mismatch, walk-off and focus offset; see
        module conventions. ξ must be positive, β non-negative, all finite.
        The waist may lie outside the crystal (|μ| > 1).
    kappa : float
        Legacy argument, accepted only when zero. A single combined depth
        does not specify pump and harmonic absorption independently.
    alpha_omega_L, alpha_2omega_L : float
        Non-negative, finite intensity absorption depths α₁L, α₂L.

    Returns
    -------
    float
        Dimensionless h, with P₂ = K L k₁ h P₁².

    Notes
    -----
    Lossless centred beams use the reduced one-dimensional integral,
    Daniel et al. Eq. (3). Otherwise integrate the Eq. (2) kernel over
    s,s′ in [0,1], including the source/exit attenuation above; h=ξ∫∫kernel.
    Swapping s and s′ conjugates the kernel, so its integral is real.
    Quadrature tolerances are absolute 1e-10 and relative 1e-8 for h.
    Highly oscillatory or extreme inputs may require a convergence study;
    SciPy integration warnings are deliberately not suppressed.
    """
    _validate(xi, sigma, beta, kappa, mu, alpha_omega_L, alpha_2omega_L)
    if mu == 0.0 and alpha_omega_L == 0.0 and alpha_2omega_L == 0.0:
        # Eq. (3), x = sqrt(2)*ξ*u. This scales the integration range to [0,1].
        def reduced(u: float) -> float:
            z = 1.0 + 1j * xi * u
            return float(
                (
                    -2.0
                    * cmath.exp(2j * sigma * xi * u)
                    * math.exp(-4.0 * beta**2 * xi * u**2)
                    * cmath.atan(xi * (u - 1.0) / z)
                    / z
                ).real
            )

        value, _ = integrate.quad(
            reduced, 0.0, 1.0, epsabs=1e-10, epsrel=1e-8, limit=300
        )
        return float(value)

    def kernel(s_p: float, s: float) -> float:
        tau = xi * (2.0 * s - 1.0 - mu)
        tau_p = xi * (2.0 * s_p - 1.0 - mu)
        diff = tau - tau_p
        attenuation = -alpha_omega_L * (s + s_p) - alpha_2omega_L * (
            1.0 - (s + s_p) / 2.0
        )
        z = (
            cmath.exp(1j * sigma * diff)
            * math.exp(attenuation - beta**2 * diff**2 / xi)
            / ((1.0 + 1j * tau) * (1.0 - 1j * tau_p))
        )
        return float(xi * z.real)

    value, _ = integrate.dblquad(kernel, 0.0, 1.0, 0.0, 1.0, epsabs=1e-10, epsrel=1e-8)
    return float(value)


def h_m_factor(
    xi: float,
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
    *,
    sigma_bracket: tuple[float, float] = (-6.0, 6.0),
    alpha_omega_L: float = 0.0,
    alpha_2omega_L: float = 0.0,
) -> float:
    """Maximise h over a finite phase-mismatch interval, including endpoints.

    Parameters
    ----------
    xi, beta, kappa, mu, alpha_omega_L, alpha_2omega_L
        Dimensionless inputs as in :func:`h_factor`.
    sigma_bracket : tuple[float, float]
        Finite, strictly increasing bounds, now enforced as bounds rather
        than an initial Brent bracket. No claim is made outside this interval.

    Returns
    -------
    float
        Largest h found. Sample at least eight points per π/ξ phase lobe,
        then refine every sampled local maximum with a bounded optimiser.
        This is a numerical search, not a proof of a global maximum for
        arbitrary inputs; tests compare a denser independent scan.
    """
    _validate(xi, 0.0, beta, kappa, mu, alpha_omega_L, alpha_2omega_L)
    lo, hi = sigma_bracket
    if not (math.isfinite(lo) and math.isfinite(hi) and lo < hi):
        raise ValueError("sigma_bracket must contain finite increasing bounds")

    def value(sigma: float) -> float:
        return h_factor(
            xi,
            sigma,
            beta,
            kappa,
            mu,
            alpha_omega_L=alpha_omega_L,
            alpha_2omega_L=alpha_2omega_L,
        )

    count = max(33, math.ceil((hi - lo) * xi * 8.0 / math.pi) + 1)
    if count > 100_000:
        raise ValueError(
            "sigma_bracket is too wide for the phase-lobe search at this xi"
        )
    grid = np.linspace(lo, hi, count)
    values = [value(float(sigma)) for sigma in grid]
    best = max(values)
    for i in range(1, count - 1):
        if values[i] >= values[i - 1] and values[i] >= values[i + 1]:
            result = optimize.minimize_scalar(
                lambda sigma: -value(sigma),
                bounds=(grid[i - 1], grid[i + 1]),
                method="bounded",
                options={"xatol": 1e-8},
            )
            if not result.success:
                raise RuntimeError(
                    f"phase-mismatch optimisation failed: {result.message}"
                )
            best = max(best, float(-result.fun))
    return best


def h_m_optimum(
    beta: float = 0.0,
    kappa: float = 0.0,
    mu: float = 0.0,
    *,
    xi_bounds: tuple[float, float] = (0.05, 10.0),
    alpha_omega_L: float = 0.0,
    alpha_2omega_L: float = 0.0,
) -> tuple[float, float]:
    """Find the best focusing parameter ξ and dimensionless h_m.

    Parameters
    ----------
    beta, kappa, mu, alpha_omega_L, alpha_2omega_L
        Dimensionless inputs as in :func:`h_factor`.
    xi_bounds : tuple[float, float]
        Positive, finite, strictly increasing bounds. The bounded local
        search assumes a single focus maximum within these bounds; both
        endpoints are also checked. Phase mismatch uses h_m_factor defaults.

    Returns
    -------
    tuple[float, float]
        (ξ_opt, h_m). For no walk-off or absorption, ξ_opt≈2.84, h_m≈1.068.
    """
    lo, hi = xi_bounds
    if not (math.isfinite(lo) and math.isfinite(hi) and 0.0 < lo < hi):
        raise ValueError(
            f"xi_bounds must be finite, positive and increasing; got {xi_bounds}"
        )

    def value(xi: float) -> float:
        return h_m_factor(
            xi,
            beta,
            kappa,
            mu,
            alpha_omega_L=alpha_omega_L,
            alpha_2omega_L=alpha_2omega_L,
        )

    result = optimize.minimize_scalar(
        lambda xi: -value(xi),
        bounds=xi_bounds,
        method="bounded",
        options={"xatol": 1e-5},
    )
    if not result.success:
        raise RuntimeError(f"focus optimisation failed: {result.message}")
    return max(
        [(float(result.x), float(-result.fun)), (lo, value(lo)), (hi, value(hi))],
        key=lambda pair: pair[1],
    )


def h_analytic_no_walkoff_no_loss(xi: float) -> float:
    """Return h(σ=β=0, μ=0, no absorption) = arctan²(ξ)/ξ.

    Parameters
    ----------
    xi : float
        Positive, finite, dimensionless L/b.

    Returns
    -------
    float
        Dimensionless focusing factor at σ=0. Its maximum, ≈0.646 at
        ξ≈1.392, differs from the σ-optimised maximum ≈1.068 at ξ≈2.84.
    """
    if not math.isfinite(xi) or xi <= 0.0:
        raise ValueError(f"xi must be positive and finite; got {xi}")
    return math.atan(xi) ** 2 / xi
