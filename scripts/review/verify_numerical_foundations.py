"""Print a reproducible RC-01/02/05 evidence manifest; run from the repo root.

Usage: .venv/bin/python -m scripts.review.verify_numerical_foundations
Diagnostic BBO inputs reproduce the review anchors, not new design presets.
Raman outputs evaluate the draft's printed relation; D2 remains undecided.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import platform
import subprocess
from pathlib import Path

from scipy.optimize import minimize_scalar

from scripts.review.shg_reference import tensor_h
from src import boyd_kleinman as bk
from src.enhancement_cavity import optimal_input_coupler
from src.shg_single_pass import single_pass_conversion_fraction

BASELINE = "9a498165532e029e1ba0706d380f760402dd7584"


def evidence() -> dict:
    """Compute dimensionless BK factors, solver outputs and conditional rates."""
    cases = [
        (0.2, 0.9, 0.0),
        (1.0, 0.7, 1.0),
        (2.84, 0.57, 0.0),
        (4.0, 0.5, 4.0),
        (1.41317, 0.8, 18.0166),
        (0.5, -1.0, 8.0),
    ]
    convergence = []
    for xi, sigma, beta in cases:
        h256 = tensor_h(xi, sigma, beta, 256)
        h512 = tensor_h(xi, sigma, beta, 512)
        reduced = bk.h_factor(xi, sigma, beta)
        convergence.append(
            {
                "xi": xi,
                "sigma": sigma,
                "B": beta,
                "tensor_256": h256,
                "tensor_512": h512,
                "reduced": reduced,
                "relative_refinement": abs(h256 / h512 - 1.0),
                "relative_method_difference": abs(reduced / h512 - 1.0),
            }
        )
    xi, beta, n, wavelength_m, length_m = 1.41317, 18.0166, 1.67276, 559e-9, 0.01
    # Re-run the filed baseline implementation, confined to its own namespace.
    old_source = subprocess.check_output(
        ["git", "show", f"{BASELINE}:src/boyd_kleinman.py"], text=True
    )
    old = {}
    exec(compile(old_source, f"{BASELINE}:src/boyd_kleinman.py", "exec"), old)
    old_hm = old["h_m_factor"](xi, beta)
    new_hm = bk.h_m_factor(xi, beta)
    independent = minimize_scalar(
        lambda sigma: -tensor_h(xi, sigma, beta, 512),
        bounds=(0.0, 1.5),
        method="bounded",
        options={"xatol": 1e-9},
    )
    xi_opt, hm_opt = bk.h_m_optimum(beta)
    raman = []
    for name, detuning_Hz, rabi_Hz, recorded in [
        ("Conservative", 80e9, 100e3, 2500.0),
        ("Nominal", 40e9, 400e3, 20000.0),
        ("Aggressive", 15e9, 1e6, 110000.0),
    ]:
        # Ω_R/Δ is invariant when both use Hz or both use rad/s.
        # Γ is the decay rate in s^-1, numerically 2π times Γ/(2π) in Hz.
        rate = 2.0 * math.pi * 41e6 * rabi_Hz / (2.0 * detuning_Hz)
        duration_s = 1.0 / (2.0 * rabi_Hz)
        raman.append(
            {
                "scenario": name,
                "detuning_Hz": detuning_Hz,
                "rabi_Hz": rabi_Hz,
                "formula_rate_per_s": rate,
                "recorded_rate_per_s": recorded,
                "recorded_over_formula": recorded / rate,
                "pi_pulse_s": duration_s,
                "formula_events_per_pi_pulse": rate * duration_s,
            }
        )
    paths = [
        "src/boyd_kleinman.py",
        "src/shg_single_pass.py",
        "src/enhancement_cavity.py",
        "src/parameters.py",
        "constraints/raman-requirements.md",
        "scripts/review/shg_reference.py",
        "scripts/review/verify_numerical_foundations.py",
        "tests/test_boyd_kleinman.py",
        "tests/test_shg_single_pass.py",
        "tests/test_enhancement_cavity.py",
    ]
    return {
        "baseline_revision": BASELINE,
        "provenance": (
            "Changed source and this manifest are filed together; "
            "hashes identify the exact inputs."
        ),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "packages": {
            p: importlib.metadata.version(p) for p in ("numpy", "scipy", "pytest")
        },
        "sha256": {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths},
        "quadrature": convergence,
        "bbo_diagnostic": {
            "xi": xi,
            "B": beta,
            "n_omega": n,
            "wavelength_m": wavelength_m,
            "length_m": length_m,
            "old_hm": old_hm,
            "new_hm": new_hm,
            "independent_tensor_hm": -float(independent.fun),
            "xi_opt": xi_opt,
            "hm_opt": hm_opt,
            "waist_opt_m": math.sqrt(
                length_m * wavelength_m / (2.0 * math.pi * n * xi_opt)
            ),
            "combined_gamma_factor_at_fixed_inputs": new_hm / old_hm / n,
        },
        "solver": {
            "low_power_match": optimal_input_coupler(1e-8, 0.01, 1e-4),
            "gamma_P_samples": [0.049999, 0.05],
            "auto_fractions": [
                single_pass_conversion_fraction(1.0, g) for g in (0.049999, 0.05)
            ],
        },
        "raman_printed_relation_only": raman,
    }


if __name__ == "__main__":
    print(json.dumps(evidence(), indent=2, allow_nan=False))
