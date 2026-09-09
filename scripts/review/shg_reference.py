"""Independent tensor quadrature of Daniel et al. (2020), Eq. (2).

This reference deliberately does not import the production BK implementation.
Source: https://arxiv.org/abs/2009.08430 (lossless, centred Gaussian beams).
"""

from functools import lru_cache

import numpy as np
from scipy.special import roots_legendre


@lru_cache(maxsize=8)
def _rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    return roots_legendre(order)


def tensor_h(xi: float, sigma: float, beta: float, order: int = 256) -> float:
    """Return dimensionless h using an order × order Gauss–Legendre rule."""
    nodes, weights = _rule(order)
    tau = xi * nodes
    difference = tau[:, None] - tau[None, :]
    fields = np.exp(1j * sigma * tau) / (1.0 + 1j * tau)
    kernel = np.outer(fields, fields.conj()) * np.exp(-(beta**2) * difference**2 / xi)
    return float(xi / 4.0 * np.sum(np.outer(weights, weights) * kernel).real)
