"""
shg_cascade.py — composition of multiple SHG enhancement-cavity stages
======================================================================

Architecture-NEUTRAL helpers for cascading two or more enhancement-cavity
stages with inter-stage transport efficiencies. The LBO → BBO
1118 → 559 → 280 nm chain is the canonical example, but this module
contains no architecture, wavelength, or material preset; all values flow
from callers.

Per CHARTER §5.1, this module belongs to the architecture-neutral
pre-G1 layer.

Conventions
-----------
- ``Stage`` carries the operating-point parameters of one enhancement
  cavity: passive round-trip loss, single-pass SHG efficiency
  coefficient, and input-coupler transmission. The T_IC field is the
  *operating point*; for cascades that are still being designed,
  populate T_IC by calling :func:`optimise_cascade`, which returns new
  ``Stage`` objects with the impedance-matched values.
- ``transport_efficiencies[i]`` is the fractional throughput from
  stage *i*'s harmonic output into stage *(i+1)*'s pump input,
  accounting for mode-matching, dichroic, and relay losses. Its length
  must equal ``len(stages) - 1``.

Optimum factorisation
---------------------
The cascade optimum factorises **exactly**, not just in the small-signal
limit. Reason: the cascade is one-way — stage 2 does not feed back into
stage 1 — so

    dP_h2 / dT_1
        = (∂P_h2 / ∂P_h1) · (dP_h1 / dT_1)
        + (∂P_h2 / ∂T_2) · (dT_2* / dT_1)

The second term vanishes at the stage-2 impedance match (∂P_h2/∂T_2 = 0
by definition of the local optimum), and ∂P_h2/∂P_h1 > 0 always, so the
cascade-optimum condition reduces to dP_h1/dT_1 = 0 — i.e., stage 1 is
impedance-matched to its *own* input independently of stage 2.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from src.enhancement_cavity import (
    circulating_power,
    harmonic_output_W,
    optimal_input_coupler,
)


# =====================================================================
# Stage operating point
# =====================================================================


@dataclass(frozen=True)
class Stage:
    """Operating point of one SHG enhancement-cavity stage.

    Attributes
    ----------
    loss_per_pass : float
        Round-trip passive loss (everything except the input coupler),
        dimensionless in [0, 1).
    gamma_shg : float
        Single-pass SHG efficiency coefficient, in W⁻¹.
    T_IC : float
        Input-coupler power transmission at the chosen operating point,
        dimensionless in [0, 1]. For a freshly-optimised cascade this is
        the impedance-matched value returned by :func:`optimise_cascade`.
    """

    loss_per_pass: float
    gamma_shg: float
    T_IC: float


# =====================================================================
# Cascade evaluation at fixed operating points
# =====================================================================


def cascade_output(
    power_in_W: float,
    stages: Sequence[Stage],
    transport_efficiencies: Sequence[float],
) -> dict:
    """Evaluate an SHG cascade at fixed per-stage operating points.

    Parameters
    ----------
    power_in_W : float
        Pump power into the first stage, in watts.
    stages : sequence of Stage
        One Stage per cascade element.
    transport_efficiencies : sequence of float
        Fractional throughput between consecutive stages. Length must
        equal ``len(stages) - 1``.

    Returns
    -------
    dict
        - ``per_stage`` : list of dicts, one per stage, with keys
          ``input_W``, ``circulating_W``, ``harmonic_W``, and
          ``into_next_stage_W`` (``None`` for the last stage).
        - ``total_harmonic_W`` : harmonic power leaving the last stage.
        - ``total_efficiency`` : ``total_harmonic_W / power_in_W``
          (zero when the input is zero).
    """
    _validate_cascade_inputs(power_in_W, len(stages), transport_efficiencies)

    per_stage: list[dict] = []
    p_in = power_in_W
    p_h = 0.0

    for i, stage in enumerate(stages):
        p_circ = circulating_power(
            p_in, stage.T_IC, stage.loss_per_pass, stage.gamma_shg
        )
        p_h = harmonic_output_W(
            p_in, stage.T_IC, stage.loss_per_pass, stage.gamma_shg
        )

        if i < len(stages) - 1:
            p_into_next: Optional[float] = p_h * transport_efficiencies[i]
        else:
            p_into_next = None

        per_stage.append(
            {
                "input_W": p_in,
                "circulating_W": p_circ,
                "harmonic_W": p_h,
                "into_next_stage_W": p_into_next,
            }
        )

        if p_into_next is not None:
            p_in = p_into_next

    return {
        "per_stage": per_stage,
        "total_harmonic_W": p_h,
        "total_efficiency": (
            p_h / power_in_W if power_in_W > 0.0 else 0.0
        ),
    }


# =====================================================================
# Cascade impedance-match optimisation (free variable: T_IC per stage)
# =====================================================================


def optimise_cascade(
    power_in_W: float,
    stage_params: Sequence[tuple[float, float]],
    transport_efficiencies: Sequence[float],
) -> list[Stage]:
    """Solve the impedance-matched T_IC of each stage in a cascade.

    Returns a list of new ``Stage`` objects whose T_IC values jointly
    maximise the cascade harmonic output. Per the factorisation derived
    in the module docstring, this reduces to independently impedance-
    matching each stage to the power it actually sees.

    Parameters
    ----------
    power_in_W : float
        Pump power into the first stage, in watts.
    stage_params : sequence of (loss, gamma) tuples
        ``loss`` is the passive round-trip loss in [0, 1); ``gamma`` is
        the single-pass SHG efficiency coefficient in W⁻¹. Length sets
        the number of cascade stages.
    transport_efficiencies : sequence of float
        Inter-stage throughput. Length must equal
        ``len(stage_params) - 1``.

    Returns
    -------
    list of Stage
        One Stage per element of ``stage_params``, with T_IC populated
        to the impedance-matched value for that stage's input power.
    """
    _validate_cascade_inputs(
        power_in_W, len(stage_params), transport_efficiencies
    )

    optimised: list[Stage] = []
    p = power_in_W

    for i, (loss, gamma) in enumerate(stage_params):
        T_IC = optimal_input_coupler(p, loss, gamma)
        optimised.append(
            Stage(loss_per_pass=loss, gamma_shg=gamma, T_IC=T_IC)
        )
        p_h = harmonic_output_W(p, T_IC, loss, gamma)
        if i < len(stage_params) - 1:
            p = p_h * transport_efficiencies[i]

    return optimised


# =====================================================================
# Internal validation
# =====================================================================


def _validate_cascade_inputs(
    power_in_W: float,
    n_stages: int,
    transport_efficiencies: Sequence[float],
) -> None:
    if power_in_W < 0.0:
        raise ValueError(f"power_in_W must be non-negative; got {power_in_W}")
    if n_stages == 0:
        raise ValueError("at least one stage is required")
    expected_transports = n_stages - 1
    if len(transport_efficiencies) != expected_transports:
        raise ValueError(
            f"transport_efficiencies length must equal n_stages-1 = "
            f"{expected_transports}; got {len(transport_efficiencies)}"
        )
    for eta in transport_efficiencies:
        if not 0.0 <= eta <= 1.0:
            raise ValueError(
                f"transport efficiency must be in [0, 1]; got {eta}"
            )
