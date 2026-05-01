"""
test_abcd.py
============

Tests for src/abcd.py — the architecture-neutral ABCD / Gaussian-beam
propagation utility.

Coverage:
    - Elementary matrices (free space, thin lens, curved mirror, interfaces)
    - Composition order is left-to-right in propagation order
    - Gaussian-beam q at the waist: q = i z_R; w(z_R) = √2 · w0
    - Beam through a thin lens: the standard Gaussian-imaging law
    - Symmetric two-mirror cavity (radius R, length L = 2f): stability,
      eigenmode waist on-axis
    - is_stable / g-factor edge cases
    - Constructor validation (wavelength > 0, n > 0, q.imag > 0)
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from src import abcd


# =====================================================================
# Elementary matrices
# =====================================================================


def test_free_space_identity_at_zero_distance() -> None:
    np.testing.assert_array_equal(abcd.free_space(0.0), np.eye(2))


def test_free_space_compose_to_total_distance() -> None:
    M = abcd.compose(abcd.free_space(0.3), abcd.free_space(0.7))
    np.testing.assert_allclose(M, abcd.free_space(1.0))


def test_thin_lens_focuses_collimated_beam_to_focal_point() -> None:
    """A ray at height h, slope 0 should hit y=0 at distance f past the lens."""
    f = 0.1
    h = 1e-3
    ray_in = np.array([h, 0.0])
    M = abcd.compose(abcd.thin_lens(f), abcd.free_space(f))
    ray_out = M @ ray_in
    assert ray_out[0] == pytest.approx(0.0, abs=1e-15)


def test_curved_mirror_equivalent_to_thin_lens_R_over_2() -> None:
    R = 0.5
    np.testing.assert_allclose(abcd.curved_mirror(R), abcd.thin_lens(R / 2.0))


def test_flat_interface_paraxial_snell() -> None:
    M = abcd.flat_interface(1.0, 1.5)
    # A=1, B=0, C=0, D = n_from / n_to = 1/1.5
    np.testing.assert_allclose(M, np.array([[1.0, 0.0], [0.0, 1.0 / 1.5]]))


def test_curved_interface_collapses_to_flat_when_R_is_infinite() -> None:
    # Use a very large R as a proxy for flat
    M_curved = abcd.curved_interface(1e9, 1.0, 1.5)
    M_flat = abcd.flat_interface(1.0, 1.5)
    np.testing.assert_allclose(M_curved, M_flat, atol=1e-9)


def test_zero_focal_length_lens_raises() -> None:
    with pytest.raises(ValueError, match="non-zero"):
        abcd.thin_lens(0.0)


def test_zero_radius_mirror_raises() -> None:
    with pytest.raises(ValueError, match="non-zero"):
        abcd.curved_mirror(0.0)


def test_negative_distance_free_space_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        abcd.free_space(-0.1)


# =====================================================================
# Compose semantics: leftmost element is encountered first
# =====================================================================


def test_compose_order_is_propagation_order() -> None:
    """compose(M1, M2) ≡ M2 @ M1: M1 acts on the input first."""
    M1 = abcd.free_space(0.2)
    M2 = abcd.thin_lens(0.1)
    composed = abcd.compose(M1, M2)
    expected = M2 @ M1
    np.testing.assert_allclose(composed, expected)


def test_compose_requires_at_least_one() -> None:
    with pytest.raises(ValueError, match="at least one"):
        abcd.compose()


# =====================================================================
# Gaussian-beam q-parameter
# =====================================================================


def test_gaussian_at_waist_has_q_equal_i_zR() -> None:
    w0 = 50e-6
    lam = 280e-9
    beam = abcd.GaussianBeam.from_waist(w0_m=w0, wavelength_vac_m=lam)
    z_R = math.pi * w0 * w0 / lam
    assert beam.q == pytest.approx(complex(0.0, z_R))
    assert beam.w_m == pytest.approx(w0, rel=1e-12)
    assert beam.rayleigh_range_m == pytest.approx(z_R, rel=1e-12)
    assert beam.waist_m == pytest.approx(w0, rel=1e-12)
    assert beam.R_m == math.inf


def test_gaussian_w_grows_to_sqrt2_at_rayleigh_range() -> None:
    """At z = z_R, w(z) = √2 · w0."""
    w0 = 50e-6
    lam = 280e-9
    z_R = math.pi * w0 * w0 / lam
    beam = abcd.GaussianBeam.from_waist(
        w0_m=w0, wavelength_vac_m=lam, z_from_waist_m=z_R
    )
    assert beam.w_m == pytest.approx(math.sqrt(2) * w0, rel=1e-12)


def test_gaussian_R_at_rayleigh_range_equals_2_zR() -> None:
    """At z = z_R, R(z) = 2 z_R (standard Gaussian-optics result)."""
    w0 = 50e-6
    lam = 280e-9
    z_R = math.pi * w0 * w0 / lam
    beam = abcd.GaussianBeam.from_waist(
        w0_m=w0, wavelength_vac_m=lam, z_from_waist_m=z_R
    )
    assert beam.R_m == pytest.approx(2 * z_R, rel=1e-12)


def test_gaussian_propagation_through_free_space_preserves_waist_and_zR() -> None:
    w0 = 50e-6
    lam = 280e-9
    beam = abcd.GaussianBeam.from_waist(w0_m=w0, wavelength_vac_m=lam)
    propagated = abcd.propagate(beam, abcd.free_space(0.05))
    assert propagated.waist_m == pytest.approx(w0, rel=1e-9)
    assert propagated.rayleigh_range_m == pytest.approx(beam.rayleigh_range_m, rel=1e-9)


def test_thin_lens_imaging_q_transform() -> None:
    """A waist 1f past a lens of focal length f imaged to a waist 1f beyond.

    Tests that the q-transform agrees with hand calculation through M = LF*FS*FS*LF
    in the Gaussian-imaging configuration.
    """
    f = 0.1
    w0 = 100e-6
    lam = 1064e-9
    # Place the input waist exactly one focal length before the lens
    beam = abcd.GaussianBeam.from_waist(w0_m=w0, wavelength_vac_m=lam)
    # Propagate forward by f, through lens, forward by f
    M = abcd.compose(abcd.free_space(f), abcd.thin_lens(f), abcd.free_space(f))
    out = abcd.propagate(beam, M)
    # Image waist (Gaussian imaging at d_in = d_out = f): waist on the far side
    # is w0' = f λ / (π w0) (this is the FT-plane Gaussian result).
    expected_w0p = f * lam / (math.pi * w0)
    assert out.waist_m == pytest.approx(expected_w0p, rel=1e-9)


def test_propagate_changes_n_when_n_after_specified() -> None:
    w0 = 50e-6
    lam = 280e-9
    beam = abcd.GaussianBeam.from_waist(w0_m=w0, wavelength_vac_m=lam, n=1.0)
    out = abcd.propagate(beam, abcd.flat_interface(1.0, 1.5), n_after=1.5)
    assert out.n == 1.5


def test_gaussian_constructor_rejects_zero_imag() -> None:
    with pytest.raises(ValueError, match="q.imag"):
        abcd.GaussianBeam(q=complex(0.1, 0.0), wavelength_vac_m=280e-9)


def test_gaussian_constructor_rejects_negative_n() -> None:
    with pytest.raises(ValueError, match="refractive index"):
        abcd.GaussianBeam(q=complex(0.0, 1e-3), wavelength_vac_m=280e-9, n=-1.0)


def test_gaussian_constructor_rejects_negative_wavelength() -> None:
    with pytest.raises(ValueError, match="wavelength"):
        abcd.GaussianBeam(q=complex(0.0, 1e-3), wavelength_vac_m=-280e-9)


def test_from_waist_rejects_zero_w0() -> None:
    with pytest.raises(ValueError, match="w0_m"):
        abcd.GaussianBeam.from_waist(w0_m=0.0, wavelength_vac_m=280e-9)


# =====================================================================
# Cavity stability and eigenmode
# =====================================================================


def _symmetric_two_mirror_round_trip(L: float, R: float) -> abcd.ABCD:
    """Symmetric linear cavity: mirror1 → free L → mirror2 → free L → back."""
    return abcd.compose(
        abcd.curved_mirror(R),
        abcd.free_space(L),
        abcd.curved_mirror(R),
        abcd.free_space(L),
    )


def test_symmetric_linear_cavity_stable_for_L_lt_2R() -> None:
    R = 0.5
    L = 0.3  # L < R: certainly stable
    M = _symmetric_two_mirror_round_trip(L, R)
    assert abcd.is_stable(M)


def test_symmetric_linear_cavity_concentric_limit_g_equals_one() -> None:
    """L = 2R is the concentric limit: g_i = 1 − L/R = −1, g₁g₂ = +1
    (upper boundary of stability)."""
    R = 0.5
    L = 2.0 * R
    M = _symmetric_two_mirror_round_trip(L, R)
    g = abcd.stability_g_factor(M)
    assert g == pytest.approx(1.0, abs=1e-9)


def test_symmetric_linear_cavity_confocal_g_equals_zero() -> None:
    """L = R is the confocal limit: g_i = 0, g₁g₂ = 0 (lower boundary).

    Marginally stable; the round-trip matrix is degenerate (M = ±I) at any
    reference plane.
    """
    R = 0.5
    L = R
    M = _symmetric_two_mirror_round_trip(L, R)
    g = abcd.stability_g_factor(M)
    assert g == pytest.approx(0.0, abs=1e-9)


def test_symmetric_linear_cavity_unstable_above_concentric() -> None:
    R = 0.5
    L = 2 * R + 1e-2  # L > 2R
    M = _symmetric_two_mirror_round_trip(L, R)
    assert not abcd.is_stable(M)


def test_eigenmode_q_self_consistent_under_round_trip() -> None:
    """A genuine eigenmode q must satisfy q = (A q + B)/(C q + D)."""
    R = 0.5
    L = 0.5 * R  # strictly stable, non-degenerate
    lam = 1064e-9
    M = _symmetric_two_mirror_round_trip(L, R)
    beam = abcd.cavity_eigenmode_q(M, wavelength_vac_m=lam)
    propagated = abcd.propagate(beam, M)
    assert propagated.q.real == pytest.approx(beam.q.real, rel=1e-9, abs=1e-15)
    assert propagated.q.imag == pytest.approx(beam.q.imag, rel=1e-9, abs=1e-15)


def test_eigenmode_q_has_positive_imaginary_part() -> None:
    R = 0.5
    L = 0.5 * R
    M = _symmetric_two_mirror_round_trip(L, R)
    beam = abcd.cavity_eigenmode_q(M, wavelength_vac_m=1064e-9)
    assert beam.q.imag > 0
    assert beam.waist_m > 0


def test_eigenmode_raises_for_unstable_cavity() -> None:
    R = 0.5
    L = 3 * R  # well past concentric
    M = _symmetric_two_mirror_round_trip(L, R)
    with pytest.raises(ValueError, match="not stable"):
        abcd.cavity_eigenmode_q(M, wavelength_vac_m=1064e-9)


def test_g_factor_in_unit_interval_for_stable_cavity() -> None:
    R = 0.5
    L = 0.3
    M = _symmetric_two_mirror_round_trip(L, R)
    g = abcd.stability_g_factor(M)
    assert 0.0 <= g <= 1.0


def test_is_stable_rejects_non_2x2() -> None:
    with pytest.raises(ValueError, match="2x2"):
        abcd.is_stable(np.eye(3))


def test_propagate_rejects_non_2x2() -> None:
    beam = abcd.GaussianBeam.from_waist(w0_m=50e-6, wavelength_vac_m=280e-9)
    with pytest.raises(ValueError, match="2x2"):
        abcd.propagate(beam, np.eye(3))
