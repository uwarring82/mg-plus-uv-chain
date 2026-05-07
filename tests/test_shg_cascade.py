"""
test_shg_cascade.py — tests for src/shg_cascade.py

Exercises the thin composition over Phase A/B primitives. Tests are
ordered by dependency: dataclass first, then single-stage degenerate
case (trivial reduction to Phase B), then two-stage evaluation, then
the optimum factorisation property, then bounds (Manley-Rowe per stage,
total efficiency ≤ Π transport), then validation guards.
"""

from __future__ import annotations

import dataclasses

import pytest

from src.enhancement_cavity import (
    harmonic_output_W,
    optimal_input_coupler,
)
from src.shg_cascade import (
    Stage,
    cascade_output,
    optimise_cascade,
)


# =====================================================================
# 1 · Stage dataclass
# =====================================================================


class TestStageDataclass:
    def test_construction_and_attributes(self) -> None:
        s = Stage(loss_per_pass=0.005, gamma_shg=0.01, T_IC=0.02)
        assert s.loss_per_pass == 0.005
        assert s.gamma_shg == 0.01
        assert s.T_IC == 0.02

    def test_frozen_immutable(self) -> None:
        s = Stage(loss_per_pass=0.005, gamma_shg=0.01, T_IC=0.02)
        with pytest.raises(dataclasses.FrozenInstanceError):
            s.T_IC = 0.03  # type: ignore[misc]


# =====================================================================
# 2 · Single-stage degenerate reduction to Phase B
# =====================================================================


class TestSingleStage:
    def test_single_stage_matches_phase_b_harmonic(self) -> None:
        L, gamma, T = 0.005, 0.01, 0.02
        P_in = 1.0
        stage = Stage(loss_per_pass=L, gamma_shg=gamma, T_IC=T)
        result = cascade_output(P_in, [stage], [])
        expected = harmonic_output_W(P_in, T, L, gamma)
        assert result["total_harmonic_W"] == pytest.approx(expected, rel=1e-12)

    def test_single_stage_into_next_is_none(self) -> None:
        stage = Stage(loss_per_pass=0.005, gamma_shg=0.01, T_IC=0.02)
        result = cascade_output(1.0, [stage], [])
        assert result["per_stage"][0]["into_next_stage_W"] is None

    def test_single_stage_optimum_matches_phase_b(self) -> None:
        L, gamma = 0.005, 0.01
        P_in = 1.0
        optimised = optimise_cascade(P_in, [(L, gamma)], [])
        T_standalone = optimal_input_coupler(P_in, L, gamma)
        assert len(optimised) == 1
        assert optimised[0].T_IC == pytest.approx(T_standalone, rel=1e-12)
        assert optimised[0].loss_per_pass == L
        assert optimised[0].gamma_shg == gamma


# =====================================================================
# 3 · Two-stage evaluation
# =====================================================================


class TestTwoStageEvaluation:
    def test_per_stage_matches_direct_phase_b_calls(self) -> None:
        s1 = Stage(loss_per_pass=0.005, gamma_shg=0.01, T_IC=0.025)
        s2 = Stage(loss_per_pass=0.005, gamma_shg=0.5, T_IC=0.5)
        eta_t = 0.95
        P_in = 1.0

        result = cascade_output(P_in, [s1, s2], [eta_t])

        # Stage 1 — direct Phase B call
        p_h1 = harmonic_output_W(
            P_in, s1.T_IC, s1.loss_per_pass, s1.gamma_shg
        )
        # Stage 2 — direct Phase B call at the transported input
        p_in_2 = p_h1 * eta_t
        p_h2 = harmonic_output_W(
            p_in_2, s2.T_IC, s2.loss_per_pass, s2.gamma_shg
        )

        assert result["per_stage"][0]["harmonic_W"] == pytest.approx(p_h1)
        assert result["per_stage"][0]["into_next_stage_W"] == pytest.approx(
            p_in_2
        )
        assert result["per_stage"][1]["input_W"] == pytest.approx(p_in_2)
        assert result["per_stage"][1]["harmonic_W"] == pytest.approx(p_h2)
        assert result["per_stage"][1]["into_next_stage_W"] is None
        assert result["total_harmonic_W"] == pytest.approx(p_h2)
        assert result["total_efficiency"] == pytest.approx(p_h2 / P_in)

    def test_per_stage_dict_keys(self) -> None:
        stages = [
            Stage(0.005, 0.01, 0.02),
            Stage(0.005, 0.5, 0.5),
        ]
        result = cascade_output(1.0, stages, [0.9])
        for entry in result["per_stage"]:
            assert set(entry.keys()) == {
                "input_W",
                "circulating_W",
                "harmonic_W",
                "into_next_stage_W",
            }

    def test_zero_input_zero_harmonic(self) -> None:
        stages = [Stage(0.005, 0.01, 0.02), Stage(0.005, 0.5, 0.5)]
        result = cascade_output(0.0, stages, [0.9])
        assert result["total_harmonic_W"] == 0.0
        assert result["total_efficiency"] == 0.0
        for entry in result["per_stage"]:
            assert entry["circulating_W"] == 0.0
            assert entry["harmonic_W"] == 0.0


# =====================================================================
# 4 · Optimum factorisation (exact, not just small-signal)
# =====================================================================


class TestOptimumFactorises:
    """Cascade impedance-match factorises *exactly* — see module docstring.

    Two checks:
    - Stage 1's T_IC matches the stand-alone Phase B optimum at P_in.
    - Stage 2's T_IC matches the stand-alone Phase B optimum at the
      transported harmonic-1 power. Holds in both small-signal and
      depleted regimes because the factorisation is a consequence of
      one-way coupling, not of regime.
    """

    def test_factorises_in_small_signal(self) -> None:
        stage_params = [(0.005, 1e-3), (0.005, 1e-3)]
        eta_t = 0.9
        P_in = 1.0

        opt = optimise_cascade(P_in, stage_params, [eta_t])

        T1_standalone = optimal_input_coupler(P_in, 0.005, 1e-3)
        assert opt[0].T_IC == pytest.approx(T1_standalone, rel=1e-9)

        p_h1 = harmonic_output_W(P_in, opt[0].T_IC, 0.005, 1e-3)
        p_in_2 = p_h1 * eta_t
        T2_standalone = optimal_input_coupler(p_in_2, 0.005, 1e-3)
        assert opt[1].T_IC == pytest.approx(T2_standalone, rel=1e-9)

    def test_factorises_in_depleted_regime(self) -> None:
        # Stage 1 in Friedenauer-LBO-class regime (η_nl ≈ 0.5)
        stage_params = [(0.005, 0.39), (0.005, 0.5)]
        eta_t = 0.9
        P_in = 1.0

        opt = optimise_cascade(P_in, stage_params, [eta_t])

        # Stage 1 optimum is independent of stage 2's parameters
        T1_standalone = optimal_input_coupler(P_in, 0.005, 0.39)
        assert opt[0].T_IC == pytest.approx(T1_standalone, rel=1e-9)

        # Stage 2 optimum at the actual transported power
        p_h1 = harmonic_output_W(P_in, opt[0].T_IC, 0.005, 0.39)
        p_in_2 = p_h1 * eta_t
        T2_standalone = optimal_input_coupler(p_in_2, 0.005, 0.5)
        assert opt[1].T_IC == pytest.approx(T2_standalone, rel=1e-9)

    def test_stage_1_optimum_independent_of_stage_2_params(self) -> None:
        # Sweep stage 2's gamma; stage 1's optimal T should stay fixed.
        P_in = 1.0
        stage_1 = (0.005, 0.05)
        eta_t = 0.85

        T1_values = []
        for gamma_2 in [1e-4, 0.01, 0.5, 5.0]:
            opt = optimise_cascade(
                P_in, [stage_1, (0.005, gamma_2)], [eta_t]
            )
            T1_values.append(opt[0].T_IC)

        # Stage 1's optimum must be identical across stage 2's variations
        for T_first, T_other in zip(T1_values, T1_values[1:]):
            assert T_first == pytest.approx(T_other, rel=1e-12)


# =====================================================================
# 5 · Bounds — Manley-Rowe per stage, total ≤ Π transport
# =====================================================================


class TestCascadeBounds:
    def test_per_stage_manley_rowe(self) -> None:
        """Each stage's harmonic ≤ its input."""
        stages = [
            Stage(loss_per_pass=0.005, gamma_shg=0.5, T_IC=0.5),
            Stage(loss_per_pass=0.005, gamma_shg=1.0, T_IC=0.5),
        ]
        result = cascade_output(1.0, stages, [0.95])
        for entry in result["per_stage"]:
            assert entry["harmonic_W"] <= entry["input_W"] + 1e-12

    def test_total_efficiency_bounded_by_transport_product(self) -> None:
        """In the absolute (100 %-conversion) limit, total η ≤ Π η_transport."""
        # High-gamma cascade — both stages near full conversion
        stage_params = [(0.005, 100.0), (0.005, 100.0)]
        eta_t = 0.9
        P_in = 1.0

        opt = optimise_cascade(P_in, stage_params, [eta_t])
        result = cascade_output(P_in, opt, [eta_t])

        assert result["total_efficiency"] <= eta_t + 1e-12
        # And approaches the limit (within numerical tolerance):
        assert result["total_efficiency"] > 0.85

    def test_total_efficiency_at_most_one(self) -> None:
        """Even with η_transport = 1, total η can't exceed unity."""
        stage_params = [(0.005, 100.0), (0.005, 100.0)]
        opt = optimise_cascade(1.0, stage_params, [1.0])
        result = cascade_output(1.0, opt, [1.0])
        assert result["total_efficiency"] <= 1.0 + 1e-12


# =====================================================================
# 6 · Validation guards
# =====================================================================


class TestValidation:
    def test_empty_stages_raises(self) -> None:
        with pytest.raises(ValueError, match="at least one stage"):
            cascade_output(1.0, [], [])

    def test_mismatched_transport_too_few(self) -> None:
        stages = [Stage(0.005, 0.01, 0.02), Stage(0.005, 0.5, 0.5)]
        with pytest.raises(ValueError, match="transport_efficiencies length"):
            cascade_output(1.0, stages, [])

    def test_mismatched_transport_too_many(self) -> None:
        stages = [Stage(0.005, 0.01, 0.02), Stage(0.005, 0.5, 0.5)]
        with pytest.raises(ValueError, match="transport_efficiencies length"):
            cascade_output(1.0, stages, [0.9, 0.8])

    def test_negative_power(self) -> None:
        with pytest.raises(ValueError, match="power_in_W"):
            cascade_output(-1.0, [Stage(0.005, 0.01, 0.02)], [])

    def test_transport_efficiency_negative(self) -> None:
        stages = [Stage(0.005, 0.01, 0.02), Stage(0.005, 0.5, 0.5)]
        with pytest.raises(ValueError, match="transport efficiency"):
            cascade_output(1.0, stages, [-0.1])

    def test_transport_efficiency_above_one(self) -> None:
        stages = [Stage(0.005, 0.01, 0.02), Stage(0.005, 0.5, 0.5)]
        with pytest.raises(ValueError, match="transport efficiency"):
            cascade_output(1.0, stages, [1.5])

    def test_optimise_cascade_validates(self) -> None:
        with pytest.raises(ValueError, match="power_in_W"):
            optimise_cascade(-1.0, [(0.005, 0.01)], [])

    def test_optimise_cascade_empty(self) -> None:
        with pytest.raises(ValueError, match="at least one stage"):
            optimise_cascade(1.0, [], [])

    def test_optimise_cascade_transport_mismatch(self) -> None:
        with pytest.raises(ValueError, match="transport_efficiencies length"):
            optimise_cascade(1.0, [(0.005, 0.01), (0.005, 0.5)], [])
