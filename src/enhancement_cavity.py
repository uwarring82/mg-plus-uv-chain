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
- The solver always evaluates η_nl with regime="depleted" — i.e. the
  exact tanh² expression — so the residual is C¹-continuous and the
  Brent root finder cannot oscillate at the small/depleted threshold
  carried by the public Phase A "auto" default. Calling code that
  wants the small-signal-only value can still pass through Phase A
  directly.
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

from src.shg_single_pass import (
    single_pass_conversion_fraction,
    single_pass_harmonic_power_W,
)


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

    sqrt_arg = (1.0 - T_IC) * (1.0 - loss_per_pass)
    denom = 1.0 - math.sqrt(sqrt_arg)
    if denom == 0.0:
        return float("inf")
    return T_IC / denom**2


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

    # Nonlinear path: brentq on the cavity equation
    R = 1.0 - T_IC
    one_minus_L = 1.0 - loss_per_pass

    def residual(p_circ: float) -> float:
        eta_nl = single_pass_conversion_fraction(
            p_circ, gamma_shg, regime="depleted"
        )
        denom = 1.0 - math.sqrt(R * one_minus_L * (1.0 - eta_nl))
        # denom > 0 always (R, 1-L, 1-η_nl ≤ 1, with at least one < 1
        # whenever T > 0 OR L > 0 OR η_nl > 0; T > 0 here by the early-return).
        if denom <= 0.0:
            return p_circ
        return p_circ - power_in_W * T_IC / denom**2

    # Upper bracket: passive Airy max divided by no nonlinear loss is the
    # absolute ceiling. With nonlinear loss P_circ is monotonically smaller
    # at any given T, so this bound is conservative and brentq always finds
    # the root in [0, upper].
    if loss_per_pass > 0.0:
        upper = power_in_W / loss_per_pass
    else:
        # Pure-nonlinear-loss limit: P_circ saturates near P_in / T_IC
        # times a finite buildup; use a safe multiple.
        upper = max(power_in_W / max(T_IC, 1e-9), 1e12 * power_in_W)

    upper = max(upper, 1.01 * power_in_W)  # never less than the input

    # Defensive expansion if residual at upper is still negative
    # (shouldn't happen for valid inputs, but guards numerical edges).
    iterations = 0
    while residual(upper) < 0.0 and iterations < 60:
        upper *= 10.0
        iterations += 1

    return brentq(residual, 0.0, upper, xtol=1e-14, rtol=1e-12)


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
    # Cavity-level Manley-Rowe ceiling: P_in = L·P_circ + P_h at impedance
    # match, so P_h ≤ P_in always. The min() guards against floating-point
    # overshoot in the deeply saturated regime where the brentq solver and
    # the tanh² short-circuit can compound to ~1e-13 above the physical
    # bound; the clamp is exact in the linear and small-signal regimes.
    return min(p_h, power_in_W)


def optimal_input_coupler(
    power_in_W: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> float:
    """
    Impedance-matched input-coupler transmission T_match.

    Solves the self-consistent intensity-form match

        T = L + (1-L) · η_nl(P_circ(T))                                (1)

    via Brent's method over T ∈ [L, 1). The (1-L) factor is the cross
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
        Impedance-matched input-coupler transmission, in (L, 1).
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

    def residual(T: float) -> float:
        p_circ = circulating_power(power_in_W, T, loss_per_pass, gamma_shg)
        eta_nl = single_pass_conversion_fraction(
            p_circ, gamma_shg, regime="depleted"
        )
        return T - (loss_per_pass + one_minus_L * eta_nl)

    # T_match is strictly above L when gamma_shg · P_in > 0.
    T_low = loss_per_pass + max(1e-12, 1e-6 * loss_per_pass)
    T_high = 0.999_999

    f_low = residual(T_low)
    f_high = residual(T_high)

    # Adaptive T_high expansion for highly-depleted regimes, where η_nl → 1
    # and T_match → 1 from below. We push T_high closer to 1 in decade
    # steps until residual flips sign or we hit machine precision.
    while f_high < 0.0 and (1.0 - T_high) > 1e-14:
        T_high = 1.0 - (1.0 - T_high) / 10.0
        f_high = residual(T_high)

    # Saturated regime: residual at T_high is negative but within numerical
    # precision of zero — η_nl(P_circ(T_high)) = 1 to machine precision so
    # T_match → 1 exactly. Cavity enhancement is degenerate (single-pass
    # conversion ≈ 100 %); return T_high rather than failing the bracket.
    if f_low < 0.0 and -1e-10 < f_high <= 0.0:
        return T_high

    if f_low * f_high > 0.0:
        # Both ends on the same side after adaptive expansion *and* not in
        # the recognised saturated regime — caller's inputs are pathological.
        raise RuntimeError(
            "optimal_input_coupler could not bracket the impedance match: "
            f"residual(T={T_low:.3e})={f_low:.3e}, "
            f"residual(T={T_high:.3e})={f_high:.3e}. "
            f"Inputs: P_in={power_in_W}, L={loss_per_pass}, gamma={gamma_shg}."
        )

    return brentq(residual, T_low, T_high, xtol=1e-14, rtol=1e-12)


# =====================================================================
# Internal validation
# =====================================================================


def _validate_cavity_inputs(
    power_in_W: float,
    T_IC: float,
    loss_per_pass: float,
    gamma_shg: float,
) -> None:
    if power_in_W < 0.0:
        raise ValueError(f"power_in_W must be non-negative; got {power_in_W}")
    if not 0.0 <= T_IC <= 1.0:
        raise ValueError(f"T_IC must be in [0, 1]; got {T_IC}")
    if not 0.0 <= loss_per_pass < 1.0:
        raise ValueError(f"loss_per_pass must be in [0, 1); got {loss_per_pass}")
    if gamma_shg < 0.0:
        raise ValueError(f"gamma_shg must be non-negative; got {gamma_shg}")
