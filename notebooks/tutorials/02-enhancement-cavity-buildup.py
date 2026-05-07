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
# # Tutorial 2 — Passive Enhancement-Cavity Buildup
#
# **Architecture-neutral · pre-G1 admissible**
#
# Before adding a nonlinear crystal, it helps to understand how a *passive*
# ring cavity builds up circulating power.  This notebook derives the Airy
# formula in plain language and shows where the impedance-matched maximum
# sits.
#
# > *"Given an input coupler with transmission $T$ and a round-trip passive
# > loss $L$, what is the circulating power?"*

# %%
# -----------------------------------------------------------------------------
# Imports and path setup
# -----------------------------------------------------------------------------
from __future__ import annotations

import math
import sys
from pathlib import Path

REPO_ROOT = Path.cwd().resolve()
while not (REPO_ROOT / "pyproject.toml").exists() and REPO_ROOT != REPO_ROOT.parent:
    REPO_ROOT = REPO_ROOT.parent
sys.path.insert(0, str(REPO_ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from src.enhancement_cavity import circulating_power, passive_buildup  # noqa: E402

print("Imports OK")

# %% [markdown]
# ## 1. The Airy buildup formula
#
# For a ring cavity on resonance, the circulating power is
#
# $$\frac{P_\mathrm{circ}}{P_\mathrm{in}} = \frac{T}{(1 - \sqrt{R\,(1-L)})^2}$$
#
# where $R = 1-T$ is the input-coupler reflectivity and $L$ is the
# round-trip passive loss *excluding* the input coupler.
#
# **Why this formula?**  On each round trip the beam:
# 1. Reflects off the input coupler → factor $R$
# 2. Suffers passive loss → factor $1-L$
# 3. Returns to the input coupler
#
# The amplitude that survives one round trip is $\sqrt{R(1-L)}$.  The
# geometric series of all round trips gives the denominator $(1 - \sqrt{R(1-L)})^2$.

# %%
# -----------------------------------------------------------------------------
# Load parameters
# -----------------------------------------------------------------------------
YAML_PATH = Path(__file__).with_suffix("").parent / "02-params.yaml"
with YAML_PATH.open() as f:
    params = yaml.safe_load(f)

c = params["cavity"]
P_in = c["power_in_W"]
L_loss = c["loss_per_pass"]
gamma = c["gamma_shg"]

sweep = params["sweep"]
T_min = sweep["T_IC_min"]
T_max = sweep["T_IC_max"]
n_pts = sweep["n_points"]

print(f"Parameters: P_in = {P_in} W,  L = {L_loss},  γ = {gamma} W⁻¹")

# %% [markdown]
# ## 2. Buildup curves for several passive losses

# %%
T_grid = np.linspace(T_min, T_max, n_pts)
losses = [0.005, 0.01, 0.02, 0.05]

fig, ax = plt.subplots(figsize=(8, 4.5))
for L_val in losses:
    buildup = [passive_buildup(T, L_val) for T in T_grid]
    ax.plot(T_grid * 100, buildup, lw=2, label=f"L = {L_val:.3f}")
    # Mark the impedance-matched maximum at T = L
    idx = np.argmin(np.abs(T_grid - L_val))
    ax.plot([L_val * 100], [buildup[idx]], "o", ms=6)

ax.set_xlabel("Input-coupler transmission  T (%)")
ax.set_ylabel(r"Buildup  $P_\mathrm{circ} / P_\mathrm{in}$")
ax.set_title("Passive ring-cavity buildup vs. input-coupler transmission")
ax.legend(loc="upper right", title="Passive loss")
ax.grid(alpha=0.3)
ax.set_yscale("log")
fig.tight_layout()

# %% [markdown]
# **Take-away.** Each curve has a sharp maximum at **T = L** (the open
# circles).  This is the **impedance-matched** point: the input coupler
# transmits exactly as much power as the cavity loses per round trip, so
# no power is reflected back to the source.  At this point the buildup is
# $1/L$ — for $L = 0.01$ the circulating power is 100× the input power.

# %% [markdown]
# ## 3. Circulating power with nonlinear loss
#
# When a crystal is inside the cavity, each round trip converts a fraction
# $\eta_\mathrm{nl}$ of the circulating power to harmonic.  The nonlinear
# loss modifies the buildup.  Here we compare the passive curve with the
# nonlinear curve for a small SHG coefficient.

# %%
T_grid = np.linspace(0.001, 0.10, 200)
L_val = 0.02
gamma_small = 1e-3  # W⁻¹ — small enough to stay in the small-signal regime

buildup_passive = [passive_buildup(T, L_val) for T in T_grid]
buildup_nonlinear = [
    circulating_power(P_in, T, L_val, gamma_small) / P_in for T in T_grid
]

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(T_grid * 100, buildup_passive, "-", lw=2, label="Passive (γ = 0)")
ax.plot(T_grid * 100, buildup_nonlinear, "--", lw=2,
        label=rf"Nonlinear ($\gamma = {gamma_small}$ W⁻¹)")
ax.axvline(L_val * 100, ls=":", color="gray", lw=1, alpha=0.6,
           label=f"Impedance match  T = L = {L_val:.3f}")
ax.set_xlabel("Input-coupler transmission  T (%)")
ax.set_ylabel(r"Buildup  $P_\mathrm{circ} / P_\mathrm{in}$")
ax.set_title("Passive vs. small-nonlinear-loss buildup")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)
ax.set_yscale("log")
fig.tight_layout()

# %% [markdown]
# **Take-away.** Even a tiny SHG coefficient pulls the optimum to slightly
# larger T (the nonlinear loss acts like extra round-trip loss).  The shift
# is small here, but it grows with pump power — that is the subject of
# Tutorial 3.

# %% [markdown]
# ## 4. Try this
#
# Open `02-params.yaml` and change the passive loss `loss_per_pass`.  Try
# values from 0.001 (very low-loss super-mirror cavity) to 0.10 (a
# lossy prototype).  Re-run the cells and watch how the impedance-matched
# buildup $1/L$ changes.

# %%
print("Tutorial 02 complete.")
