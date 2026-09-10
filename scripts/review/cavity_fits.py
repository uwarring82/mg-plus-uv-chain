"""Generic cavity calibration helpers for review calculations.

No material presets, notebook execution, data loading or plotting imports.
Architecture-specific scenarios remain in the exploratory notebooks.
"""

import math

from scipy.optimize import brentq

from src.enhancement_cavity import harmonic_output_W, optimal_input_coupler


def fit_passive_loss(
    pump_W: float,
    transmission: float,
    gamma_per_W: float,
    measured_harmonic_W: float,
    extraction_efficiency: float = 1.0,
) -> float:
    """Fit dimensionless fundamental loss to one extracted harmonic power.

    Extraction is downstream of conversion, with no UV feedback. Reject an
    unattainable measurement rather than returning a boundary as a fitted loss.

    Parameters
    ----------
    pump_W : float
        Incident fundamental pump power, in W.
    transmission : float
        Dimensionless input-coupler power transmission.
    gamma_per_W : float
        Single-pass conversion coefficient, in W⁻¹.
    measured_harmonic_W : float
        Positive extracted harmonic power, in W.
    extraction_efficiency : float
        Dimensionless downstream harmonic throughput in (0, 1].

    Returns
    -------
    float
        Dimensionless passive round-trip fundamental power loss.
    """
    if not 0.0 < extraction_efficiency <= 1.0:
        raise ValueError("extraction efficiency must be in (0,1]")
    if not math.isfinite(measured_harmonic_W) or measured_harmonic_W <= 0.0:
        raise ValueError("measured harmonic power must be positive and finite")

    def residual(loss: float) -> float:
        return (
            extraction_efficiency
            * harmonic_output_W(pump_W, transmission, loss, gamma_per_W)
            - measured_harmonic_W
        )

    high = math.nextafter(1.0, 0.0)
    low_residual, high_residual = residual(0.0), residual(high)
    # The forward solver has a 1e-12 relative root tolerance. At a physical
    # endpoint, an equivalent independently generated observation can differ
    # by roundoff. Accept only a correspondingly small *relative output* error.
    output_tolerance = 3e-12 * measured_harmonic_W
    if abs(low_residual) <= output_tolerance:
        return 0.0
    if abs(high_residual) <= output_tolerance:
        return high
    if low_residual < 0.0 or high_residual > 0.0:
        raise ValueError("measured output is outside the passive-loss model range")
    return float(brentq(residual, 0.0, high, xtol=1e-15, rtol=1e-12))


def minimax_coupler(
    powers_W: list[float], loss: float, gamma: float
) -> dict[str, float]:
    """Equalise relative output penalties for two endpoint pump scenarios.

    Parameters
    ----------
    powers_W : list of float
        Two positive, increasing incident pump powers, in W.
    loss : float
        Dimensionless passive round-trip fundamental power loss.
    gamma : float
        Single-pass conversion coefficient, in W⁻¹.

    Returns
    -------
    dict of str to float
        Dimensionless coupler transmission and worst relative output penalty.
    """
    if len(powers_W) != 2 or not 0.0 < powers_W[0] < powers_W[1]:
        raise ValueError("two positive increasing pump scenarios are required")
    optima = [optimal_input_coupler(p, loss, gamma) for p in powers_W]
    peaks = [
        harmonic_output_W(p, t, loss, gamma)
        for p, t in zip(powers_W, optima, strict=True)
    ]

    def penalty(p: float, t: float, peak: float) -> float:
        return 1.0 - harmonic_output_W(p, t, loss, gamma) / peak

    def difference(t: float) -> float:
        return penalty(powers_W[0], t, peaks[0]) - penalty(powers_W[1], t, peaks[1])

    centre = brentq(difference, *optima, xtol=1e-15)
    return {
        "transmission": float(centre),
        "worst_relative_penalty": max(
            penalty(p, centre, peak) for p, peak in zip(powers_W, peaks, strict=True)
        ),
    }
