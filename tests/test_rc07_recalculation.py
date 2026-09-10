"""Independent inverse-calibration and minimax checks for the RC-07 analysis."""

import math
import runpy

import numpy as np
import pytest

from src.enhancement_cavity import harmonic_output_W, optimal_input_coupler

analysis = runpy.run_path("notebooks/exploration/2026-09-10-rc07-recalculation.py")
fit_loss = analysis["fit_passive_loss"]
minimax = analysis["minimax_coupler"]


@pytest.mark.parametrize("loss, extraction", [(0.007, 1.0), (0.02, 0.95), (0.0, 0.9)])
def test_fit_recovers_loss_from_independent_field_balance(
    loss: float, extraction: float
) -> None:
    pc, gamma, transmission = 25.0, 1e-4, 0.02
    eta = math.tanh(math.sqrt(gamma * pc)) ** 2
    amplitude_survival = math.sqrt((1 - transmission) * (1 - loss) * (1 - eta))
    pump = pc * (1 - amplitude_survival) ** 2 / transmission
    measured = extraction * eta * pc
    assert fit_loss(pump, transmission, gamma, measured, extraction) == pytest.approx(
        loss, abs=2e-14
    )


def test_unattainable_fit_is_rejected() -> None:
    with pytest.raises(ValueError, match="outside"):
        fit_loss(1.0, 0.02, 1e-4, 2.0)


@pytest.mark.parametrize("bad", [0.0, -0.1, 1.1, math.nan])
def test_invalid_extraction_is_rejected(bad: float) -> None:
    with pytest.raises(ValueError, match="extraction"):
        fit_loss(1.0, 0.02, 1e-4, 0.1, bad)


def test_minimax_is_best_worst_relative_penalty_on_dense_grid() -> None:
    powers, loss, gamma = [0.5, 1.5], 0.011, 1e-4
    optima = [optimal_input_coupler(p, loss, gamma) for p in powers]
    peaks = [
        harmonic_output_W(p, t, loss, gamma)
        for p, t in zip(powers, optima, strict=True)
    ]

    def worst(t: float) -> float:
        return max(
            1.0 - harmonic_output_W(p, t, loss, gamma) / peak
            for p, peak in zip(powers, peaks, strict=True)
        )

    result = minimax(powers, loss, gamma)
    dense_best = min(worst(float(t)) for t in np.linspace(*optima, 1001))
    assert optima[0] < result["transmission"] < optima[1]
    assert worst(result["transmission"]) <= dense_best
    assert worst(result["transmission"]) == pytest.approx(dense_best, abs=2e-5)
