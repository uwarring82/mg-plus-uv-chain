"""
enhancement_cavity.py — SHG enhancement-cavity steady state
============================================================

Architecture-NEUTRAL ring-cavity solver for second-harmonic generation
with passive round-trip loss and a single-pass nonlinear conversion
fraction supplied by :mod:`src.shg_single_pass`.

Cavity equation (lossless input coupler, on-resonance):

    P_circ / P_in = T / (1 - sqrt(R · (1-L) · (1 - η_nl(P_circ))))²

with R = 1 - T, L = passive round-trip loss (everything except the
input coupler), and
η_nl(P_circ) = single_pass_conversion_fraction(P_circ, γ_SHG).

The intensity-form impedance-matching condition is

    T_match = 1 - (1-L)(1-η_nl) = L + η_nl - L · η_nl                (1)

The cross term -L · η_nl distinguishes the exact match from the
linearised approximation T ≈ L + η_nl. In the small-signal limit
η_nl = γ · P_circ this reduces to the quadratic

    T² - L T - (1-L) γ P_in = 0                                       (2)

→ T_match = ½ [L + sqrt(L² + 4 (1-L) γ P_in)]                         (3)

with high-pump leading order T_match → sqrt((1-L) γ P_in) (no L under
the radical) and low-pump leading order T_match → L + (1-L) γ P_in / L.

Implementation choices
----------------------
- The solver uses the continuous effective tanh² depletion model, also
  used by the single-pass "auto" default. This is not a full solution
  of depleted Gaussian-beam propagation.
- P_circ is referenced immediately before conversion. Passive loss acts
  on the remaining fundamental power, so round-trip dissipation is
  [η_nl + L(1-η_nl)] P_circ. Harmonic extraction is assumed complete.
- The gamma_shg = 0 path short-circuits to a closed-form passive
  Airy buildup; this avoids a degenerate brentq bracket and gives
  exact answers in the linear regime.

Per CHARTER §5.1, this module contains no crystal preset, no
wavelength preset, and no architecture preset. All parameter values
flow from callers.

References
----------
- E. S. Polzik & H. J. Kimble, *Opt. Lett.* **16**, 1400 (1991).
- A. Ashkin, G. D. Boyd & J. M. Dziedzic, *IEEE J. Quantum Electron.*
  **2**, 109 (1966).
"""

from __future__ import annotations

import math

from scipy.optimize import brentq

from src.shg_single_pass import single_pass_harmonic_power_W

# =====================================================================
# Passive / linearised closed forms
# =====================================================================


def passive_buildup(T_IC: float, loss_per_pass: float) -> float:
    """
    Closed-form passive ring-cavity power buildup P_circ / P_in.

    P_circ / P_in = T / (1 - sqrt((1-T)(1-L)))²

    Reaches the Airy maximum 1/L at impedance match (T = L).

    Parameters
    ----------
    T_IC : float
        Input-coupler power transmission, dimensionless in [0, 1].
    loss_per_pass : float
        Round-trip passive loss (everything except the IC),
        dimensionless in [0, 1).

    Returns
    -------
    float
        Power buildup factor (≥ 1 at impedance match; 1 at T = 1).
    """
    if not 0.0 <= T_IC <= 1.0:
        raise ValueError(f"T_IC must be in [0, 1]; got {T_IC}")
    if not 0.0 <= loss_per_pass < 1.0:
        raise ValueError(f"loss_per_pass must be in [0, 1); got {loss_per_pass}")
    if T_IC == 0.0:
        return 0.0

    denom = _round_trip_denominator(T_IC, loss_per_pass, 0.0)
    return (T_IC / denom) / denom


def _round_trip_denominator(T: float, loss: float, eta: float) -> float:
    """Rationalise 1 - sqrt((1-T)(1-L)(1-η)) at small total loss."""
    total_loss = T + (1.0 - T) * (loss + (1.0 - loss) * eta)
    return total_loss / (1.0 + math.sqrt((1.0 - T) * (1.0 - loss) * (1.0 - eta)))


# =====================================================================
# Steady-state circulating power (passive or nonlinear)
# =====================================================================


def circulating_power(
    power_in_W: float,
    T_IC: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> float:
    """
    Steady-state circulating power (W) in the SHG enhancement cavity.

    For gamma_shg = 0 returns the closed-form passive Airy buildup
    times power_in_W. For gamma_shg > 0 solves the transcendental
    cavity equation via Brent's method on the residual

        f(P_circ) = P_circ - P_in · T / (1 - sqrt(R(1-L)(1-η_nl)))²

    with η_nl = single_pass_conversion_fraction(P_circ, γ_SHG, "depleted").

    Parameters
    ----------
    power_in_W : float
        Input pump power in watts.
    T_IC : float
        Input-coupler power transmission, dimensionless in [0, 1].
    loss_per_pass : float
        Passive round-trip loss in [0, 1).
    gamma_shg : float
        Single-pass SHG efficiency coefficient in W⁻¹.

    Returns
    -------
    float
        Circulating power in watts.
    """
    _validate_cavity_inputs(power_in_W, T_IC, loss_per_pass, gamma_shg)

    if power_in_W == 0.0 or T_IC == 0.0:
        return 0.0

    # Linear path: closed form
    if gamma_shg == 0.0:
        return power_in_W * passive_buildup(T_IC, loss_per_pass)

    # Solve for a = sqrt(P_circ/P_in), avoiding a fixed tolerance in watts.
    # Nonlinear loss only lowers the buildup: the passive field buildup is
    # an exact upper bracket. Rationalisation preserves very small T and L.
    sqrt_T = math.sqrt(T_IC)
    nonlinear_scale = math.sqrt(gamma_shg) * math.sqrt(power_in_W)
    upper = sqrt_T / _round_trip_denominator(T_IC, loss_per_pass, 0.0)
    # Round the analytic upper bound outward: at vanishing nonlinear loss,
    # division/multiplication roundoff can otherwise make f(upper) negative.
    upper *= 1.0 + 8.0 * math.ulp(1.0)

    def residual(a: float) -> float:
        eta = math.tanh(nonlinear_scale * a) ** 2
        return a * _round_trip_denominator(T_IC, loss_per_pass, eta) - sqrt_T

    amplitude = brentq(
        residual, 0.0, upper, xtol=math.ulp(0.0), rtol=1e-12, maxiter=2048
    )
    return (power_in_W * amplitude) * amplitude


# =====================================================================
# Harmonic output and impedance-matched coupling
# =====================================================================


def harmonic_output_W(
    power_in_W: float,
    T_IC: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> float:
    """
    Harmonic power leaving the cavity (W).

    Internally evaluates :func:`single_pass_harmonic_power_W` at the
    converged circulating power with regime="depleted". Valid in both
    small-signal and depleted operating regimes.

    Parameters
    ----------
    See :func:`circulating_power`.

    Returns
    -------
    float
        Harmonic power in watts. Bounded above by `power_in_W` by
        Manley-Rowe.
    """
    p_circ = circulating_power(power_in_W, T_IC, loss_per_pass, gamma_shg)
    p_h = single_pass_harmonic_power_W(p_circ, gamma_shg, regime="depleted")
    # At match P_in = [η + L(1-η)] P_circ. Do not clamp the result:
    # tests check this balance and the reflected-power balance off match.
    # A relative ~1e-12 root tolerance can leave roundoff-sized overshoot.
    return p_h


def optimal_input_coupler(
    power_in_W: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> float:
    """
    Impedance-matched input-coupler transmission T_match.

    Solves the self-consistent intensity-form match

        T = L + (1-L) · η_nl(P_circ(T))                                (1)

    using P_circ = P_in/T at match and Brent's method over T ∈ [L, 1].
    The reduced residual is strictly increasing: η(P_in/T) decreases
    with T. Its endpoint signs bracket the unique root without offsets.
    At L=0 the lower-end residual is its T→0⁺ limit, -1. The (1-L) factor is the cross
    term that distinguishes the exact match from the linearised
    approximation T ≈ L + η_nl.

    For gamma_shg = 0 the match degenerates to T_match = L (passive
    impedance match) and is returned in closed form.

    Parameters
    ----------
    power_in_W : float
        Input pump power in watts.
    loss_per_pass : float
        Passive round-trip loss in [0, 1).
    gamma_shg : float
        Single-pass SHG efficiency coefficient in W⁻¹.

    Returns
    -------
    float
        Impedance-matched transmission in [L, 1], including rounded limits.
    """
    _validate_cavity_inputs(
        power_in_W=power_in_W,
        T_IC=0.5,  # placeholder; T is the unknown here
        loss_per_pass=loss_per_pass,
        gamma_shg=gamma_shg,
    )

    if power_in_W == 0.0 or gamma_shg == 0.0:
        return loss_per_pass

    one_minus_L = 1.0 - loss_per_pass
    nonlinear_scale = math.sqrt(gamma_shg) * math.sqrt(power_in_W)

    def residual(T: float) -> float:
        if T == 0.0:
            return -1.0
        eta_nl = math.tanh(nonlinear_scale / math.sqrt(T)) ** 2
        return (T - loss_per_pass) - one_minus_L * eta_nl

    return brentq(
        residual, loss_per_pass, 1.0, xtol=math.ulp(0.0), rtol=1e-12, maxiter=2048
    )


# =====================================================================
# Internal validation
# =====================================================================


def _validate_cavity_inputs(
    power_in_W: float,
    T_IC: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> None:
    if not math.isfinite(power_in_W) or power_in_W < 0.0:
        raise ValueError(
            f"power_in_W must be finite and non-negative; got {power_in_W}"
        )
    if not 0.0 <= T_IC <= 1.0:
        raise ValueError(f"T_IC must be in [0, 1]; got {T_IC}")
    if not 0.0 <= loss_per_pass < 1.0:
        raise ValueError(f"loss_per_pass must be in [0, 1); got {loss_per_pass}")
    if not math.isfinite(gamma_shg) or gamma_shg < 0.0:
        raise ValueError(f"gamma_shg must be finite and non-negative; got {gamma_shg}")
