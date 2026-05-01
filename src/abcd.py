"""
abcd.py — generic ray / Gaussian-beam ABCD propagation
========================================================

Architecture-NEUTRAL ABCD ray-transfer-matrix utility for paraxial
Gaussian-beam propagation through composed optical systems. Per
CHARTER §5.1, this module belongs to the architecture-neutral pre-G1
layer: it contains pure geometry / Gaussian-optics — no cavity preset,
no architecture preset, no wavelength-specific code.

Conventions
-----------
- All inputs and outputs SI (lengths in metres, focal lengths in metres,
  refractive index dimensionless) per CONVENTIONS §1.
- ABCD matrices act on the column vector (height, slope) under the
  paraxial approximation.
- Gaussian-beam q-parameter: 1/q = 1/R − i λ /(π n w²), where R is the
  wavefront radius of curvature, w is the 1/e² intensity beam radius,
  λ is the *vacuum* wavelength, and n is the refractive index of the
  medium in which q is evaluated.
- Stable cavity criterion (linear, two-mirror, or generic round trip):
  −1 ≤ (A + D)/2 ≤ 1, equivalently 0 ≤ (A + D + 2)/4 ≤ 1.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


ABCD = np.ndarray  # shape (2, 2), float64


# =====================================================================
# Elementary ABCD matrices
# =====================================================================


def free_space(d_m: float) -> ABCD:
    """Free-space propagation by distance d_m (metres)."""
    if d_m < 0:
        raise ValueError(f"distance must be non-negative; got {d_m}")
    return np.array([[1.0, d_m], [0.0, 1.0]])


def thin_lens(f_m: float) -> ABCD:
    """Thin lens of focal length f_m (metres). Concave: f < 0."""
    if f_m == 0.0:
        raise ValueError("focal length must be non-zero for a thin lens")
    return np.array([[1.0, 0.0], [-1.0 / f_m, 1.0]])


def curved_mirror(R_m: float) -> ABCD:
    """Spherical mirror, radius of curvature R_m (concave: R > 0).

    Acts as a thin lens of focal length R/2.
    """
    if R_m == 0.0:
        raise ValueError("mirror radius of curvature must be non-zero")
    return thin_lens(R_m / 2.0)


def flat_interface(n_from: float, n_to: float) -> ABCD:
    """Flat dielectric interface from n_from to n_to (paraxial)."""
    if n_from <= 0 or n_to <= 0:
        raise ValueError("refractive indices must be positive")
    return np.array([[1.0, 0.0], [0.0, n_from / n_to]])


def curved_interface(R_m: float, n_from: float, n_to: float) -> ABCD:
    """Spherical dielectric interface, radius R_m (convex toward incoming: R > 0)."""
    if R_m == 0.0:
        raise ValueError("interface radius of curvature must be non-zero")
    if n_from <= 0 or n_to <= 0:
        raise ValueError("refractive indices must be positive")
    return np.array([[1.0, 0.0], [(n_from - n_to) / (R_m * n_to), n_from / n_to]])


# =====================================================================
# Composition
# =====================================================================


def compose(*matrices: ABCD) -> ABCD:
    """
    Compose ABCD matrices left-to-right in propagation order.

        compose(M1, M2, M3) ≡ M3 @ M2 @ M1

    so that the leftmost element is encountered *first* by the beam.
    """
    if not matrices:
        raise ValueError("compose requires at least one matrix")
    result = matrices[0].copy()
    for m in matrices[1:]:
        result = m @ result
    return result


# =====================================================================
# Gaussian-beam q-parameter
# =====================================================================


@dataclass(frozen=True)
class GaussianBeam:
    """
    Gaussian-beam q-parameter holder.

    Attributes
    ----------
    q : complex
        Complex beam parameter, 1/q = 1/R − i λ_vac / (π n w²).
    wavelength_vac_m : float
        *Vacuum* wavelength.
    n : float
        Refractive index of the medium in which q is currently evaluated.
        Default 1.0 (free space).
    """

    q: complex
    wavelength_vac_m: float
    n: float = 1.0

    def __post_init__(self) -> None:
        if self.wavelength_vac_m <= 0:
            raise ValueError("wavelength_vac_m must be positive")
        if self.n <= 0:
            raise ValueError("refractive index n must be positive")
        if self.q.imag <= 0:
            raise ValueError(
                "q.imag must be > 0 for a physical Gaussian beam "
                "(positive Rayleigh range / positive beam waist)"
            )

    @classmethod
    def from_waist(
        cls,
        w0_m: float,
        wavelength_vac_m: float,
        n: float = 1.0,
        z_from_waist_m: float = 0.0,
    ) -> GaussianBeam:
        """
        Construct a Gaussian beam at distance z_from_waist_m past its waist.

        At the waist, q = i z_R where z_R = π n w0² / λ_vac.
        """
        if w0_m <= 0:
            raise ValueError("waist w0_m must be positive")
        z_R = math.pi * n * w0_m * w0_m / wavelength_vac_m
        q = complex(z_from_waist_m, z_R)
        return cls(q=q, wavelength_vac_m=wavelength_vac_m, n=n)

    @property
    def w_m(self) -> float:
        """1/e² intensity beam radius at the current location."""
        inv_q_imag = (1.0 / self.q).imag
        # 1/q = 1/R - i λ_vac / (π n w²)  →  w² = − λ_vac / (π n · Im(1/q))
        w2 = -self.wavelength_vac_m / (math.pi * self.n * inv_q_imag)
        return math.sqrt(w2)

    @property
    def R_m(self) -> float:
        """Wavefront radius of curvature R at the current location.

        Returns +inf at the waist (Im 1/q nonzero, Re 1/q zero) by convention.
        """
        inv_q_real = (1.0 / self.q).real
        if inv_q_real == 0.0:
            return math.inf
        return 1.0 / inv_q_real

    @property
    def rayleigh_range_m(self) -> float:
        """z_R = π n w0² / λ_vac, recovered from the current q.

        z_R is invariant under free-space propagation in a uniform medium.
        """
        return self.q.imag

    @property
    def waist_m(self) -> float:
        """Waist radius w0 derived from current q (invariant under free space)."""
        return math.sqrt(self.wavelength_vac_m * self.q.imag / (math.pi * self.n))


def propagate(beam: GaussianBeam, M: ABCD, n_after: float | None = None) -> GaussianBeam:
    """
    Propagate a Gaussian beam through ABCD matrix M.

    Standard rule: q' = (A q + B) / (C q + D).

    The vacuum wavelength is preserved; the medium index after propagation
    is supplied as `n_after` if it differs from the incoming medium.

    Parameters
    ----------
    beam : GaussianBeam
        Incoming beam.
    M : (2, 2) array
        ABCD matrix.
    n_after : float, optional
        Refractive index of the medium after propagation. Defaults to
        the incoming medium index.

    Returns
    -------
    GaussianBeam
        Outgoing beam.
    """
    if M.shape != (2, 2):
        raise ValueError(f"ABCD must be 2x2; got shape {M.shape}")
    A, B = M[0, 0], M[0, 1]
    C, D = M[1, 0], M[1, 1]
    q_in = beam.q
    q_out = (A * q_in + B) / (C * q_in + D)
    n_out = beam.n if n_after is None else n_after
    return GaussianBeam(q=q_out, wavelength_vac_m=beam.wavelength_vac_m, n=n_out)


# =====================================================================
# Cavity utilities
# =====================================================================


def is_stable(M_round_trip: ABCD) -> bool:
    """
    Stability of a generic round-trip ABCD: −1 ≤ (A + D)/2 ≤ 1.
    """
    if M_round_trip.shape != (2, 2):
        raise ValueError(f"ABCD must be 2x2; got shape {M_round_trip.shape}")
    half_trace = 0.5 * (M_round_trip[0, 0] + M_round_trip[1, 1])
    return -1.0 <= half_trace <= 1.0


def stability_g_factor(M_round_trip: ABCD) -> float:
    """
    Generic stability parameter g = (A + D + 2) / 4 ∈ [0, 1] for stable cavities.

    For a two-mirror linear cavity, g₁ g₂ = (A + D + 2)/4 with the standard
    g_i = 1 − L/R_i. This generalises to any single round-trip ABCD.
    """
    if M_round_trip.shape != (2, 2):
        raise ValueError(f"ABCD must be 2x2; got shape {M_round_trip.shape}")
    return float((M_round_trip[0, 0] + M_round_trip[1, 1] + 2.0) / 4.0)


def cavity_eigenmode_q(
    M_round_trip: ABCD, wavelength_vac_m: float, n: float = 1.0
) -> GaussianBeam:
    """
    Self-consistent Gaussian eigenmode q at the reference plane of a
    stable round-trip ABCD.

    Solves q = (A q + B)/(C q + D)  ⇒  C q² + (D − A) q − B = 0,
    selecting the root with positive imaginary part.
    """
    if not is_stable(M_round_trip):
        raise ValueError(
            "round-trip matrix is not stable: |(A+D)/2| > 1; "
            "no real Gaussian eigenmode exists"
        )
    A, B = M_round_trip[0, 0], M_round_trip[0, 1]
    C, D = M_round_trip[1, 0], M_round_trip[1, 1]
    if C == 0.0:
        raise ValueError(
            "C = 0: round-trip matrix has no Gaussian eigenmode at this plane "
            "(propagator is purely magnifying / diagonal)"
        )
    # C q² + (D − A) q − B = 0
    a = C
    b = D - A
    c = -B
    disc = complex(b * b - 4 * a * c)
    sqrt_disc = np.sqrt(disc)
    q1 = (-b + sqrt_disc) / (2 * a)
    q2 = (-b - sqrt_disc) / (2 * a)
    q = q1 if q1.imag > 0 else q2
    if q.imag <= 0:
        raise ValueError("no eigenmode root with positive imaginary part found")
    return GaussianBeam(q=complex(q), wavelength_vac_m=wavelength_vac_m, n=n)
