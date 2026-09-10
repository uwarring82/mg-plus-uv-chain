# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Tutorial 1 — From Boyd–Kleinman to γ_SHG
#
# **Architecture-neutral · pre-G1 admissible**
#
# This notebook explains how the dimensionless Boyd–Kleinman (BK) focusing
# factor $h_m$ is turned into the engineering single-pass efficiency
# coefficient $\gamma_\mathrm{SHG}$ (units W⁻¹).  It is the first stepping
# stone toward answering:
#
# > *"Given a crystal, a pump wavelength, and a focused beam — how much
# > harmonic power comes out in a single pass?"*
#
# No cavity physics yet; that is Tutorial 2.

# %% [markdown]
# ## Run in Google Colab
#
# [Open this notebook in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/01-shg-single-pass.ipynb).
# Save a copy to your Drive, then run all cells using a standard CPU runtime.
# The setup cell below downloads the reviewed code and inputs when no local
# project checkout is present. No Drive mount is needed. For an experiment,
# edit `parameter_overrides` below; your changes then travel with the notebook.
# [Student guide and exercises](https://uwarring82.github.io/mg-plus-uv-chain/tutorials/).
#

# %%
# -----------------------------------------------------------------------------
# Imports and path setup
# -----------------------------------------------------------------------------
from __future__ import annotations

import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

# A local checkout uses its own code. Colab starts without a checkout, so
# fetch a fixed reviewed revision into a temporary runtime directory.
REFERENCE_REVISION = "3466c3262aa72af93f10a3699c48782d401548f8"
REPO_ROOT = Path.cwd().resolve()
while not (REPO_ROOT / "src" / "enhancement_cavity.py").is_file():
    if REPO_ROOT == REPO_ROOT.parent:
        break
    REPO_ROOT = REPO_ROOT.parent
if not (REPO_ROOT / "src" / "enhancement_cavity.py").is_file():
    REPO_ROOT = Path(tempfile.mkdtemp(prefix="mg-uv-tutorial-"))
    subprocess.run(
        ["git", "clone", "--quiet",
         "https://github.com/uwarring82/mg-plus-uv-chain.git", str(REPO_ROOT)],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(REPO_ROOT), "checkout", "--quiet", REFERENCE_REVISION],
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--quiet", "-e", str(REPO_ROOT)],
        check=True,
    )
    os.chdir(REPO_ROOT)
    print("Runtime code and inputs:", REFERENCE_REVISION)
sys.path.insert(0, str(REPO_ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from src import boyd_kleinman as bk  # noqa: E402
from src.shg_single_pass import (  # noqa: E402
    boyd_kleinman_K_factor,
    gamma_shg_coefficient,
    single_pass_conversion_fraction,
    single_pass_harmonic_power_W,
)

print("Imports OK")

# %% [markdown]
# ## Your experiment
#
# Leave the dictionary empty to reproduce the bundled example. Then try
# `{"crystal": {"d_eff_pm_per_V": 1.68}}` and run this cell and all cells below it again.
# Change this cell rather than runtime files so saving the notebook preserves
# your experiment. Input names and units are listed in the paired YAML file.
#
# %%
parameter_overrides = {}

# %% [markdown]
# ## 1. The Boyd–Kleinman focusing factor
#
# Boyd & Kleinman (1968) showed that, for a focused Gaussian pump in a
# non-depleted crystal, the harmonic power is
#
# $$P_{2\omega} = K \; L \; k_1 \; h \; P_\omega^2$$
#
# where $h$ is a **dimensionless** double integral that depends only on
# geometric and optical parameters:
#
# | Symbol | Meaning |
# |---|---|
# | $\xi = L/b$ | focusing parameter ($b = 2z_R$ is the confocal parameter) |
# | $\sigma = \tfrac{1}{2}\Delta k \, b$ | phase mismatch |
# | $\beta = \tfrac{1}{2}\rho\sqrt{L k_1}$ | walk-off parameter |
# | $\alpha_1 L$, $\alpha_2 L$ | separate intensity absorption depths (zero here) |
# | $\mu = 2z_\mathrm{focus}/L-1$ | focus offset from crystal centre |
#
# Nonzero legacy `kappa` is rejected: use `alpha_omega_L` and
# `alpha_2omega_L` separately. This tutorial uses zero absorption.
# Conventions and normalization follow [Daniel et al., Eqs. 1–3](https://arxiv.org/abs/2009.08430).
#
# In the lab you tune $\sigma$ (temperature or angle) for maximum conversion.
# The $\sigma$-optimised version is $h_m(\xi, \beta)$ for the centred, lossless case used here.

# %%
# Quick look: h_m(ξ) for several walk-off parameters β.
# All curves optimise σ; arctan²(ξ)/ξ would only give the σ=0 limit.
xi_grid = np.linspace(0.2, 6.0, 150)

fig, ax = plt.subplots(figsize=(8, 4.5))

# β = 0  →  σ-optimised; arctan²(ξ)/ξ is only the σ=0 limit.
h_beta0 = np.array([bk.h_m_factor(x) for x in xi_grid])
ax.plot(xi_grid, h_beta0, lw=2, label=r"$\beta = 0$ (σ-optimised)")

# β = 1 and β = 2  →  numerical (a few evaluations, still fast)
for beta_val in [1.0, 2.0]:
    h_vals = []
    for xi in xi_grid[::5]:  # coarse sub-sample for speed
        h_vals.append(bk.h_m_factor(xi=xi, beta=beta_val, kappa=0.0, mu=0.0))
    ax.plot(xi_grid[::5], h_vals, "o-", ms=3, label=rf"$\beta = {beta_val}$")

# Mark the classic BK optimum (β = 0, σ-optimised)
xi_opt, h_max = bk.h_m_optimum(beta=0.0, kappa=0.0, mu=0.0)
ax.axvline(xi_opt, ls="--", color="C2", lw=1, alpha=0.6,
           label=rf"$\xi_\mathrm{{opt}} \approx {xi_opt:.2f}$")
ax.axhline(h_max, ls=":", color="C2", lw=1, alpha=0.6)
ax.plot([xi_opt], [h_max], "C2*", ms=12,
        label=rf"$h_m^\max = {h_max:.3f}$")

ax.set_xlabel(r"$\xi = L / b$")
ax.set_ylabel(r"$h_m(\xi, \beta)$")
ax.set_title(r"BK $\sigma$-optimised focusing factor for several walk-off parameters")
ax.legend(loc="upper right", fontsize=9)
ax.grid(alpha=0.3)
ax.set_ylim(0, 1.2)
fig.tight_layout()

print(f"Classic BK optimum:  ξ_opt = {xi_opt:.3f},  h_m_max = {h_max:.4f}")

# %% [markdown]
# **Take-away.** Walk-off drags the optimum to **smaller** ξ (looser focus)
# and suppresses the peak $h_m$.  For a walk-off-limited crystal you do not
# simply use the textbook ξ ≈ 2.84 — you must re-optimise.

# %% [markdown]
# ## 2. From $h_m$ to the engineering coefficient $\gamma_\mathrm{SHG}$
#
# The material constant $K$ packages all the wavelength- and crystal-specific
# physics:
#
# $$K = \frac{2\,\omega^2 \, d_\mathrm{eff}^2}{\pi \, \varepsilon_0 \, c^3 \, n_\omega^2 \, n_{2\omega}}$$
#
# and the single-pass coefficient is
#
# $$\gamma_\mathrm{SHG} = K \; k_1 \; L \; h_m$$
#
# so that
#
# $$P_{2\omega} = \gamma_\mathrm{SHG} \; P_\omega^2 \qquad (\text{small-signal})$$
#
# $$P_{2\omega} = P_\omega \; \tanh^2\!\bigl(\sqrt{\gamma_\mathrm{SHG} \, P_\omega}\bigr) \qquad (\text{depleted})$$

# %%
# -----------------------------------------------------------------------------
# Load generic parameters from the paired YAML
# -----------------------------------------------------------------------------
YAML_PATH = REPO_ROOT / "notebooks" / "tutorials" / "01-params.yaml"
with YAML_PATH.open() as f:
    params = yaml.safe_load(f)

# Apply saved notebook experiments to the bundled YAML defaults.
for key, value in parameter_overrides.items():
    if key not in params:
        raise KeyError(f"Unknown parameter section: {key}")
    if isinstance(value, dict):
        unknown = value.keys() - params[key].keys()
        if unknown:
            raise KeyError(f"Unknown parameters in {key}: {sorted(unknown)}")
        params[key].update(value)
    else:
        params[key] = value

c = params["crystal"]
d_eff = c["d_eff_pm_per_V"] * 1e-12  # convert pm/V → m/V
n_o = c["n_omega"]
n_2 = c["n_2omega"]
lam = c["wavelength_nm"] * 1e-9
L_mm = c["length_mm"]
L = L_mm * 1e-3

foc = params["focusing"]
w0_um = foc["w0_um"]
rho_mrad = foc["walk_off_angle_mrad"]

print("Loaded parameters from 01-params.yaml")
print(f"  d_eff = {d_eff*1e12:.2f} pm/V")
print(f"  n_ω = {n_o},  n_2ω = {n_2}")
print(f"  λ = {lam*1e9:.0f} nm,  L = {L_mm:.0f} mm")
print(f"  w0 = {w0_um} μm,  ρ = {rho_mrad} mrad")

# %% [markdown]
# ### 2.1 Compute the BK focusing factor
#
# If `w0_um` is `null` in the YAML, we use the σ-optimised BK waist.
# Otherwise we compute ξ from the specified waist and evaluate $h_m$ there.

# %%
if w0_um is None:
    # Use the BK σ-optimum (β includes walk-off if ρ > 0)
    beta = 0.5 * (rho_mrad * 1e-3) * math.sqrt(L * 2 * math.pi * n_o / lam)
    xi_opt_val, h_m_val = bk.h_m_optimum(beta=beta, kappa=0.0, mu=0.0)
    w0_calc = math.sqrt(L * lam / (2 * math.pi * n_o * xi_opt_val))
    print(f"BK σ-optimum:  ξ = {xi_opt_val:.3f},  h_m = {h_m_val:.4f}")
    print(f"Corresponding waist: w0 = {w0_calc*1e6:.2f} μm")
else:
    w0_m = w0_um * 1e-6
    xi_val = L * lam / (2 * math.pi * n_o * w0_m**2)
    beta = 0.5 * (rho_mrad * 1e-3) * math.sqrt(L * 2 * math.pi * n_o / lam)
    h_m_val = bk.h_m_factor(xi=xi_val, beta=beta, kappa=0.0, mu=0.0)
    print(f"Specified waist:  ξ = {xi_val:.3f},  h_m = {h_m_val:.4f}")

# %% [markdown]
# ### 2.2 Compute γ_SHG and the single-pass harmonic power

# %%
K = boyd_kleinman_K_factor(d_eff, n_o, n_2, lam)
gamma = gamma_shg_coefficient(d_eff, n_o, n_2, lam, L, h_m_val)

print(f"Material constant K = {K:.4e} W⁻¹")
print(f"Single-pass coefficient γ_SHG = {gamma:.4e} W⁻¹")

# Plot single-pass conversion vs pump power
P_range = np.linspace(0.01, 50.0, 200)
h_small = gamma * P_range**2
h_depl = np.array([
    single_pass_harmonic_power_W(p, gamma, "depleted") for p in P_range
])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(P_range, h_small, "--", lw=1.5, alpha=0.7, label=r"Small-signal  $\gamma P^2$")
ax.plot(P_range, h_depl, "-", lw=2, label=r"Depleted  $P \tanh^2(\sqrt{\gamma P})$")

# Mark a small-signal reference value; auto now uses tanh² everywhere.
P_reference = 0.05 / gamma
ax.axvline(P_reference, ls=":", color="C2", lw=1, alpha=0.6,
           label=f"γP = 0.05  ({P_reference:.1f} W)")

ax.set_xlabel(r"Pump power $P_\omega$ (W)")
ax.set_ylabel(r"Harmonic power $P_{2\omega}$ (W)")
ax.set_title("Single-pass harmonic generation")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
ax.set_xlim(0, 50)
ax.set_ylim(0, min(50, max(h_depl) * 1.2))
fig.tight_layout()

# %% [markdown]
# **Take-away.** At low power the two curves sit on top of each other.
# The default `auto` uses the depleted model continuously; the explicit
# small-signal approximation increasingly overestimates conversion:
# the pump is being consumed, and the conversion fraction can never exceed
# 100 % (the Manley–Rowe ceiling).

# %% [markdown]
# ## 3. Conversion fraction vs pump power
#
# The **conversion fraction** $\eta = P_{2\omega} / P_\omega$ is what the
# cavity solver (Tutorial 3) consumes.  It is not simply $\gamma P_\omega$
# outside the small-signal regime.

# %%
eta_small = gamma * P_range
eta_depl = np.array([
    single_pass_conversion_fraction(p, gamma, "depleted") for p in P_range
])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(P_range, eta_small * 100, "--", lw=1.5, alpha=0.7,
        label=r"Small-signal  $\gamma P$")
ax.plot(P_range, eta_depl * 100, "-", lw=2,
        label=r"Depleted  $\tanh^2(\sqrt{\gamma P})$")
ax.axhline(100, ls=":", color="gray", lw=1, alpha=0.5)
ax.set_xlabel(r"Pump power $P_\omega$ (W)")
ax.set_ylabel(r"Conversion fraction  $\eta$ (%)")
ax.set_title("Single-pass conversion fraction")
ax.legend(loc="lower right")
ax.grid(alpha=0.3)
ax.set_xlim(0, 50)
ax.set_ylim(0, 105)
fig.tight_layout()

# %% [markdown]
# ## 4. Try this
#
# Open `01-params.yaml` next to this notebook and change the crystal
# parameters.  For example:
# - Set `d_eff_pm_per_V: 2.2` (a high-nonlinearity crystal like KNB)
# - Set `length_mm: 25`
# - Set `walk_off_angle_mrad: 50` (a walk-off-limited geometry)
#
# Re-run the cells above and watch how $\gamma_\mathrm{SHG}$ and the
# conversion curves shift.

# %%
print("Tutorial 01 complete.")
