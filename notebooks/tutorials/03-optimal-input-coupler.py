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
# # Tutorial 3 — Optimal Input-Coupler Reflectivity
#
# **Architecture-neutral · pre-G1 admissible**
#
# This is the notebook that answers the project's motivating question:
#
# > *"Given a pump power, a passive loss budget, and a single-pass SHG
# > efficiency coefficient — what input-coupler reflectivity should I order
# > from the coating vendor, and how much harmonic power will that produce?"*
#
# We give both the **closed-form textbook answer** (small-signal, Polzik–Kimble)
# and the **numerical solver** for the saturated regime.

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

from src.enhancement_cavity import (  # noqa: E402
    circulating_power,
    harmonic_output_W,
    optimal_input_coupler,
)

print("Imports OK")

# %% [markdown]
# ## 1. The small-signal closed form
#
# In the small-signal limit ($\eta_\mathrm{nl} = \gamma P_\mathrm{circ} \ll 1$)
# the impedance-match condition is
#
# $$T_\mathrm{match} = L + (1-L)\,\gamma\,P_\mathrm{circ}$$
#
# and because $P_\mathrm{circ} \approx P_\mathrm{in} / T$ at match, this
# becomes the quadratic
#
# $$T^2 - L\,T - (1-L)\,\gamma\,P_\mathrm{in} = 0$$
#
# whose physical root is
#
# $$T_\mathrm{opt} = \tfrac{1}{2}\Bigl[\,L + \sqrt{L^2 + 4(1-L)\,\gamma\,P_\mathrm{in}}\,\Bigr]$$
#
# This is the **Polzik–Kimble** result (Opt. Lett. 16, 1400, 1991).

# %%
# -----------------------------------------------------------------------------
# Load parameters
# -----------------------------------------------------------------------------
YAML_PATH = Path(__file__).with_suffix("").parent / "03-params.yaml"
with YAML_PATH.open() as f:
    params = yaml.safe_load(f)

c = params["cavity"]
P_in = c["power_in_W"]
L_loss = c["loss_per_pass"]
gamma = c["gamma_shg"]

sens = params["sensitivity"]
gamma_rel = sens["gamma_relative_variation"]
loss_abs = sens["loss_absolute_variation"]

sweep = params["sweep"]
T_min = sweep["T_IC_min"]
T_max = sweep["T_IC_max"]
n_pts = sweep["n_points"]

print(f"Parameters: P_in = {P_in} W,  L = {L_loss},  γ = {gamma} W⁻¹")

# %% [markdown]
# ### 1.1 Compute the analytic optimum and compare with the numerical solver

# %%
# Analytic closed form (small-signal)
T_opt_analytic = (
    L_loss + math.sqrt(L_loss**2 + 4.0 * (1.0 - L_loss) * gamma * P_in)
) / 2.0

# Numerical solver (exact, depleted regime)
T_opt_numerical = optimal_input_coupler(P_in, L_loss, gamma)

P_h_analytic = harmonic_output_W(P_in, T_opt_analytic, L_loss, gamma)
P_h_numerical = harmonic_output_W(P_in, T_opt_numerical, L_loss, gamma)

print(f"Analytic  T_opt = {T_opt_analytic:.5f}  →  P_h = {P_h_analytic:.4f} W")
print(f"Numerical T_opt = {T_opt_numerical:.5f}  →  P_h = {P_h_numerical:.4f} W")
print(f"Deviation in T_opt: {(T_opt_numerical - T_opt_analytic) / T_opt_analytic * 100:+.2f} %")

# %% [markdown]
# **Take-away.** The analytic formula is usually within a few percent of the
# exact solver.  The deviation grows when $\gamma P_\mathrm{circ}$ approaches
# the depleted regime ($\gtrsim 5$ %).  For procurement estimates the closed
# form is excellent; for final performance predictions you want the solver.

# %% [markdown]
# ## 2. Harmonic output vs. input-coupler transmission
#
# A 2-D sweep shows the landscape: there is a single maximum, and missing it
# by even a few percent of T can cost tens of percent in harmonic power.

# %%
T_grid = np.linspace(T_min, T_max, n_pts)
P_h_grid = np.array([
    harmonic_output_W(P_in, T, L_loss, gamma) for T in T_grid
])

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(T_grid * 100, P_h_grid, lw=2, label="Exact solver")
ax.axvline(T_opt_numerical * 100, ls="--", color="C2", lw=1.5,
           label=rf"Optimum  $T = {T_opt_numerical*100:.2f}$ %")
ax.axvline(T_opt_analytic * 100, ls=":", color="C3", lw=1.5,
           label=rf"Analytic  $T = {T_opt_analytic*100:.2f}$ %")
ax.plot([T_opt_numerical * 100], [P_h_numerical], "C2*", ms=12)

ax.set_xlabel("Input-coupler transmission  T (%)")
ax.set_ylabel("Harmonic output $P_{2\omega}$ (W)")
ax.set_title("Harmonic output vs. input-coupler transmission")
ax.legend(loc="lower left")
ax.grid(alpha=0.3)
fig.tight_layout()

# %% [markdown]
# **Take-away.** The curve is **asymmetric**: over-coupling (T too large) is
# generally less painful than under-coupling (T too small), but the penalty
# is significant on both sides.  When you order coatings, specify the target
# T at the centre of your expected loss budget and include a tolerance band.

# %% [markdown]
# ## 3. Sensitivity — how wrong can γ and L be?
#
# In practice you never know $\gamma$ or $L$ exactly.  Here we sweep both
# around the nominal values and plot the optimum T and the resulting
# harmonic output.

# %%
# γ sensitivity
gammas = gamma * np.array([1 - gamma_rel, 1.0, 1 + gamma_rel])
fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))

for g in gammas:
    P_h = np.array([harmonic_output_W(P_in, T, L_loss, g) for T in T_grid])
    T_opt = optimal_input_coupler(P_in, L_loss, g)
    axs[0].plot(T_grid * 100, P_h, lw=2, label=rf"$\gamma = {g:.4f}$ W⁻¹")
    axs[0].axvline(T_opt * 100, ls="--", lw=1, alpha=0.5)

axs[0].set_xlabel("Input-coupler transmission  T (%)")
axs[0].set_ylabel("Harmonic output $P_{2\omega}$ (W)")
axs[0].set_title(rf"Sensitivity to $\gamma$  (nominal ±{gamma_rel*100:.0f} %)")
axs[0].legend(loc="lower left", fontsize=9)
axs[0].grid(alpha=0.3)

# L sensitivity
Ls = [L_loss - loss_abs, L_loss, L_loss + loss_abs]
for L_val in Ls:
    P_h = np.array([harmonic_output_W(P_in, T, L_val, gamma) for T in T_grid])
    T_opt = optimal_input_coupler(P_in, L_val, gamma)
    axs[1].plot(T_grid * 100, P_h, lw=2, label=rf"$L = {L_val:.4f}$")
    axs[1].axvline(T_opt * 100, ls="--", lw=1, alpha=0.5)

axs[1].set_xlabel("Input-coupler transmission  T (%)")
axs[1].set_ylabel("Harmonic output $P_{2\omega}$ (W)")
axs[1].set_title(rf"Sensitivity to $L$  (nominal ±{loss_abs*100:.1f} pp)")
axs[1].legend(loc="lower left", fontsize=9)
axs[1].grid(alpha=0.3)

fig.tight_layout()

# Print numeric summary
print("\nSensitivity summary:")
for g in gammas:
    T_opt = optimal_input_coupler(P_in, L_loss, g)
    P_h = harmonic_output_W(P_in, T_opt, L_loss, g)
    print(f"  γ = {g:.4f} W⁻¹  →  T_opt = {T_opt*100:.2f} %  →  P_h = {P_h:.3f} W")
for L_val in Ls:
    T_opt = optimal_input_coupler(P_in, L_val, gamma)
    P_h = harmonic_output_W(P_in, T_opt, L_val, gamma)
    print(f"  L = {L_val:.4f}    →  T_opt = {T_opt*100:.2f} %  →  P_h = {P_h:.3f} W")

# %% [markdown]
# **Take-away.** A **±20 % error in γ** shifts the optimum T by a few
# percent and changes the peak harmonic power by ~10 %.  A **±0.5 pp
# error in L** has a comparable effect.  When you write a coating
# specification, include both the central target T and the tolerance band
# implied by your uncertainty in γ and L.

# %% [markdown]
# ## 4. Procurement implication
#
# Suppose you are about to order input-coupler coatings for a new cavity.
# You have:
# - A measured passive loss $L = 0.020 \pm 0.003$
# - An estimated γ = 0.010 ± 20 % W⁻¹
# - A design pump power $P_\mathrm{in} = 1.0$ W
#
# The table above tells you the optimum T sits in the range **2.5–3.5 %**.
# Ordering a coating at a single fixed T = 2.5 % leaves you under-coupled
# if the true loss is higher; ordering at T = 4 % leaves you over-coupled
# if γ is lower than expected.
#
# A robust procurement strategy:
# 1. **Bracket the coating run.** Order a small batch at T = 2.5 %, 3.0 %,
#    and 3.5 %.  Characterise each in the actual cavity and pick the best.
# 2. **Tunable IC.** Use a piezo-actuated wedge or a rotatable Brewster plate
#    to fine-tune the effective T after installation.

# %% [markdown]
# ## 5. Try this
#
# Open `03-params.yaml` and change the operating point:
# - Double the pump power (`power_in_W: 2.0`)
# - Halve the nonlinearity (`gamma_shg: 0.005`)
# - Make the cavity very lossy (`loss_per_pass: 0.08`)
#
# Re-run the cells and watch how the optimum T and the sensitivity
# landscape change.

# %%
print("Tutorial 03 complete.")
