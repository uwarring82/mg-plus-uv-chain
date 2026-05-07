"""
test_enhancement_cavity.py — tests for src/enhancement_cavity.py

Test order mirrors the implementation split: passive/linearised path
first (closed forms, easy to localise failures), then nonlinear cross
term and depleted regime, then energy-conservation and Manley–Rowe
ceiling, then input-validation guards.
"""

from __future__ import annotations

import math

import pytest

from src.enhancement_cavity import (
    circulating_power,
    harmonic_output_W,
    optimal_input_coupler,
    passive_buildup,
)
from src.shg_single_pass import single_pass_conversion_fraction


# =====================================================================
# 1 · Passive (gamma_shg = 0) closed-form path
# =====================================================================


class TestPassive:
    def test_passive_buildup_at_impedance_match(self) -> None:
        """Airy maximum: T = L gives buildup 1/L."""
        L = 0.005
        assert passive_buildup(L, L) == pytest.approx(1.0 / L, rel=1e-12)

    def test_passive_buildup_general_formula(self) -> None:
        """Spot-check the closed form for an over-coupled cavity."""
        T = 0.02
        L = 0.005
        sqrt_arg = (1.0 - T) * (1.0 - L)
        expected = T / (1.0 - math.sqrt(sqrt_arg)) ** 2
        assert passive_buildup(T, L) == pytest.approx(expected, rel=1e-12)

    def test_passive_buildup_T_zero(self) -> None:
        """No light enters when T_IC = 0."""
        assert passive_buildup(0.0, 0.005) == 0.0

    def test_passive_buildup_T_one(self) -> None:
        """T_IC = 1 → no enhancement, buildup = 1."""
        assert passive_buildup(1.0, 0.005) == pytest.approx(1.0, rel=1e-12)

    def test_circulating_power_passive_consistency(self) -> None:
        """circulating_power with gamma_shg = 0 matches passive_buildup."""
        P_in = 2.0
        T = 0.02
        L = 0.005
        expected = P_in * passive_buildup(T, L)
        assert circulating_power(P_in, T, L, 0.0) == pytest.approx(
            expected, rel=1e-10
        )

    def test_optimal_T_passive_equals_L(self) -> None:
        """With gamma_shg = 0, T_match = L."""
        L = 0.005
        assert optimal_input_coupler(1.0, L, 0.0) == pytest.approx(L, abs=1e-15)

    def test_passive_no_harmonic(self) -> None:
        """Harmonic output is exactly zero when gamma_shg = 0."""
        assert harmonic_output_W(1.0, 0.02, 0.005, 0.0) == 0.0


# =====================================================================
# 2 · Linearised (small-signal) limits
# =====================================================================


class TestLinearised:
    def test_low_pump_limit(self) -> None:
        """T_match → L + (1-L) γ P_in / L for γ P_in ≪ L²."""
        L = 0.01
        gamma = 1e-4
        P_in = 1e-3
        # gamma * P_in = 1e-7; L² = 1e-4 → ratio 1e-3 (well into low-pump)
        T_opt = optimal_input_coupler(P_in, L, gamma)
        T_expected = L + (1.0 - L) * gamma * P_in / L
        assert T_opt == pytest.approx(T_expected, rel=1e-3)

    def test_high_pump_limit_no_L_under_radical(self) -> None:
        """T_match → sqrt((1-L) γ P_in) for γ P_in ≫ L².

        Critical correction from the v1.1 peer review: the high-pump
        leading order has *no* L_passive under the radical.
        """
        L = 1e-5
        gamma = 0.01
        P_in = 0.1
        # gamma * P_in = 1e-3; L² = 1e-10 → ratio 1e7 (deep high-pump)
        # gamma * P_circ at the optimum ~ T_opt ~ sqrt(gamma * P_in) ≈ 0.0316,
        # safely below the 5 % small-signal threshold.
        T_opt = optimal_input_coupler(P_in, L, gamma)
        T_expected = math.sqrt((1.0 - L) * gamma * P_in)
        assert T_opt == pytest.approx(T_expected, rel=2e-2)

    def test_linearised_quadratic_oracle(self) -> None:
        """Exact small-signal closed form including the (1-L) cross term.

        T_match = ½ [L + sqrt(L² + 4 (1-L) γ P_in)]

        The oracle assumes η_nl = γ P_circ exactly; the solver evaluates
        η_nl with the depleted tanh² expression. The two agree to leading
        order in γ P_circ; the next-order correction scales as γ P_circ / 3.
        Tolerance is set accordingly.
        """
        L = 0.005
        gamma = 1e-3
        P_in = 0.5
        # gamma * P_in = 5e-4 → T_opt ≈ 0.025; gamma * P_circ ≈ 0.02
        # leading-order tanh² correction ≈ γ P_circ / 3 ≈ 0.7 %
        T_opt = optimal_input_coupler(P_in, L, gamma)
        T_expected = (L + math.sqrt(L**2 + 4.0 * (1.0 - L) * gamma * P_in)) / 2.0
        assert T_opt == pytest.approx(T_expected, rel=1e-2)

    def test_linearised_quadratic_oracle_deep_small_signal(self) -> None:
        """Same oracle in the deep-small-signal regime (γ P_circ ≪ 0.005),
        where the depleted tanh² correction drops to < 0.1 % and the oracle
        is tight to the solver."""
        L = 0.005
        gamma = 1e-6
        P_in = 1.0
        # gamma * P_in = 1e-6 → T_opt ≈ 5.2e-3; gamma * P_circ ≈ 2e-4
        T_opt = optimal_input_coupler(P_in, L, gamma)
        T_expected = (L + math.sqrt(L**2 + 4.0 * (1.0 - L) * gamma * P_in)) / 2.0
        assert T_opt == pytest.approx(T_expected, rel=1e-3)


# =====================================================================
# 3 · Cross term — Friedenauer-LBO regime, η_nl = 0.5
# =====================================================================


class TestCrossTerm:
    """The exact intensity-form match T = L + η_nl - L·η_nl, *not* T = L + η_nl.

    Constructed so that at the impedance-matched optimum,
    η_nl(P_circ) = 0.5 (depleted regime).  Then

        exact:      T = 0.005 + 0.5 - 0.005·0.5 = 0.5025
        linearised: T = 0.005 + 0.5            = 0.5050

    The 0.25 percentage-point gap is the cross term; the solver must
    reproduce the exact value.
    """

    L = 0.005
    P_in = 1.0
    target_eta_nl = 0.5

    @classmethod
    def _gamma_for_target_eta(cls) -> float:
        # Depleted: tanh²(sqrt(γ P_circ)) = η  →  γ P_circ = atanh(sqrt(η))²
        gp_target = math.atanh(math.sqrt(cls.target_eta_nl)) ** 2
        T_match_exact = cls.L + (1.0 - cls.L) * cls.target_eta_nl
        P_circ_at_match = cls.P_in / T_match_exact
        return gp_target / P_circ_at_match

    def test_solver_reproduces_exact_match(self) -> None:
        gamma = self._gamma_for_target_eta()
        T_opt = optimal_input_coupler(self.P_in, self.L, gamma)
        T_exact = self.L + (1.0 - self.L) * self.target_eta_nl  # 0.5025
        assert T_opt == pytest.approx(T_exact, abs=1e-6)

    def test_solver_does_not_return_linearised(self) -> None:
        gamma = self._gamma_for_target_eta()
        T_opt = optimal_input_coupler(self.P_in, self.L, gamma)
        T_linearised_no_cross_term = self.L + self.target_eta_nl  # 0.5050
        # Cross term is L·η = 0.0025; solver must be at least an order of
        # magnitude tighter to the exact value than to the linearised one.
        assert abs(T_opt - T_linearised_no_cross_term) > 2e-3

    def test_eta_nl_matches_target_at_optimum(self) -> None:
        gamma = self._gamma_for_target_eta()
        T_opt = optimal_input_coupler(self.P_in, self.L, gamma)
        P_circ = circulating_power(self.P_in, T_opt, self.L, gamma)
        eta = single_pass_conversion_fraction(P_circ, gamma, regime="depleted")
        assert eta == pytest.approx(self.target_eta_nl, rel=1e-3)


# =====================================================================
# 4 · Depleted regime — solver stability
# =====================================================================


class TestDepleted:
    def test_extreme_gamma_no_blowup(self) -> None:
        """Very high gamma drives η_nl → 1; solver must stay finite."""
        L = 0.005
        gamma = 100.0
        P_in = 1.0
        T_opt = optimal_input_coupler(P_in, L, gamma)
        P_circ = circulating_power(P_in, T_opt, L, gamma)
        P_h = harmonic_output_W(P_in, T_opt, L, gamma)
        assert math.isfinite(T_opt)
        assert math.isfinite(P_circ)
        assert math.isfinite(P_h)
        assert 0.0 < T_opt < 1.0
        assert 0.5 * P_in < P_h <= P_in  # high-conversion regime

    def test_depleted_harmonic_uses_tanh_squared_at_optimum(self) -> None:
        """harmonic_output_W = P_circ · tanh²(sqrt(γ P_circ)) at convergence,
        not γ P_circ²."""
        L = 0.005
        gamma = 0.39  # Friedenauer-LBO regime (η_nl ≈ 0.5)
        P_in = 1.0
        T_opt = optimal_input_coupler(P_in, L, gamma)
        P_circ = circulating_power(P_in, T_opt, L, gamma)
        P_h = harmonic_output_W(P_in, T_opt, L, gamma)
        gp = gamma * P_circ
        expected = P_circ * math.tanh(math.sqrt(gp)) ** 2
        assert P_h == pytest.approx(expected, rel=1e-10)
        # And explicitly different from the small-signal γ P_circ²:
        assert P_h < gamma * P_circ**2  # depleted < small-signal

    def test_circulating_power_continuous_in_gamma(self) -> None:
        """No discontinuity sweeping gamma through the 5 % threshold of
        single_pass_conversion_fraction (the solver uses regime='depleted')."""
        L = 0.005
        T = 0.02
        P_in = 1.0
        # γ P_circ at T = 0.02, P_in = 1, L = 0.005 (small gamma): P_circ ≈ 1/T_opt
        # Sweep gamma so γ * P_circ crosses 0.05.
        gammas = [0.001, 0.005, 0.01, 0.05, 0.1]
        P_circs = [circulating_power(P_in, T, L, g) for g in gammas]
        # Expect monotonically decreasing P_circ as gamma rises (more
        # nonlinear loss).  Continuous (no kink) by construction since the
        # solver sticks to depleted regime throughout.
        for a, b in zip(P_circs, P_circs[1:]):
            assert a > b


# =====================================================================
# 5 · Energy conservation and Manley–Rowe ceiling
# =====================================================================


class TestEnergyConservation:
    def test_round_trip_at_impedance_match(self) -> None:
        """At impedance match, P_in = L · P_circ + harmonic (no reflection)."""
        L = 0.005
        gamma = 0.39
        P_in = 1.0
        T_opt = optimal_input_coupler(P_in, L, gamma)
        P_circ = circulating_power(P_in, T_opt, L, gamma)
        P_h = harmonic_output_W(P_in, T_opt, L, gamma)
        P_passive_loss = L * P_circ
        # At impedance match, all input power goes to passive loss + harmonic.
        # Tolerance set to 0.5 % to absorb the higher-order terms in the
        # impedance-match expansion that we don't model here.
        assert P_in == pytest.approx(P_passive_loss + P_h, rel=5e-3)

    def test_manley_rowe_ceiling_grid(self) -> None:
        """Harmonic output never exceeds input over a parameter grid."""
        L = 0.005
        for P_in in [1e-3, 0.1, 1.0, 10.0]:
            for gamma in [1e-4, 0.01, 1.0, 100.0]:
                T = optimal_input_coupler(P_in, L, gamma)
                P_h = harmonic_output_W(P_in, T, L, gamma)
                assert 0.0 <= P_h <= P_in, (
                    f"Manley-Rowe violated at P_in={P_in}, gamma={gamma}: "
                    f"P_h={P_h}, T_opt={T}"
                )


# =====================================================================
# 6 · Input-validation guards
# =====================================================================


class TestValidation:
    def test_negative_power(self) -> None:
        with pytest.raises(ValueError, match="power_in_W"):
            circulating_power(-1.0, 0.02, 0.005, 1e-4)

    def test_T_out_of_range_low(self) -> None:
        with pytest.raises(ValueError, match="T_IC"):
            circulating_power(1.0, -0.1, 0.005, 1e-4)

    def test_T_out_of_range_high(self) -> None:
        with pytest.raises(ValueError, match="T_IC"):
            circulating_power(1.0, 1.5, 0.005, 1e-4)

    def test_loss_out_of_range(self) -> None:
        with pytest.raises(ValueError, match="loss_per_pass"):
            circulating_power(1.0, 0.02, 1.5, 1e-4)

    def test_loss_negative(self) -> None:
        with pytest.raises(ValueError, match="loss_per_pass"):
            circulating_power(1.0, 0.02, -0.001, 1e-4)

    def test_negative_gamma(self) -> None:
        with pytest.raises(ValueError, match="gamma_shg"):
            circulating_power(1.0, 0.02, 0.005, -1.0)

    def test_passive_buildup_validates_T(self) -> None:
        with pytest.raises(ValueError, match="T_IC"):
            passive_buildup(1.5, 0.005)

    def test_passive_buildup_validates_loss(self) -> None:
        with pytest.raises(ValueError, match="loss_per_pass"):
            passive_buildup(0.02, 1.0)

    def test_optimal_input_coupler_validates(self) -> None:
        with pytest.raises(ValueError):
            optimal_input_coupler(-1.0, 0.005, 1e-4)
