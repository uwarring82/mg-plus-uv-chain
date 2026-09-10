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
# # Tutorial 4 — Two-Stage SHG Cascade
#
# **Architecture-neutral · pre-G1 admissible**
#
# Many UV sources (including the Friedenauer 2006 baseline) use **two**
# enhancement-cavity doubling stages in series: e.g. 1118 nm → 559 nm →
# 280 nm.  This notebook shows how to compose the single-stage physics from
# Tutorials 1–3 into a cascade, and explains a useful mathematical fact:
# the cascade optimum **factorises exactly**.

# %% [markdown]
# ## Run in Google Colab
#
# [Open this notebook in Colab](https://colab.research.google.com/github/uwarring82/mg-plus-uv-chain/blob/main/docs/tutorials/04-cascade-shg.ipynb).
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

from src.enhancement_cavity import harmonic_output_W, optimal_input_coupler  # noqa: E402
from src.shg_cascade import Stage, cascade_output, optimise_cascade  # noqa: E402

print("Imports OK")

# %% [markdown]
# ## Your experiment
#
# Leave the dictionary empty to reproduce the bundled example. Then try
# `{"transport": {"efficiency": 0.50}}` and run this cell and all cells below it again.
# Change this cell rather than runtime files so saving the notebook preserves
# your experiment. Input names and units are listed in the paired YAML file.
#
# %%
parameter_overrides = {}

# %% [markdown]
# ## 1. A two-stage example
#
# Consider a cascade with:
# - **Stage 1** (low nonlinearity): γ₁ = 0.001 W⁻¹, L₁ = 0.02
# - **Stage 2** (high nonlinearity): γ₂ = 0.010 W⁻¹, L₂ = 0.02
# - **Transport efficiency** between stages: ηₜ = 0.95
#
# The pump power into stage 1 is $P_\mathrm{in} = 1.0$ W.

# %%
# -----------------------------------------------------------------------------
# Load parameters
# -----------------------------------------------------------------------------
YAML_PATH = REPO_ROOT / "notebooks" / "tutorials" / "04-params.yaml"
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

s1 = params["stage_1"]
s2 = params["stage_2"]
eta_t = params["transport"]["efficiency"]
P_in = params["power_in_W"]

print(f"Stage 1: L = {s1['loss_per_pass']},  γ = {s1['gamma_shg']} W⁻¹")
print(f"Stage 2: L = {s2['loss_per_pass']},  γ = {s2['gamma_shg']} W⁻¹")
print(f"Transport efficiency: {eta_t}")
print(f"Input power: {P_in} W")

# %% [markdown]
# ### 1.1 Optimise each stage independently

# %%
opt_stages = optimise_cascade(
    P_in,
    stage_params=[(s1["loss_per_pass"], s1["gamma_shg"]),
                  (s2["loss_per_pass"], s2["gamma_shg"])],
    transport_efficiencies=[eta_t],
)

print("Optimised cascade:")
for i, st in enumerate(opt_stages, 1):
    print(f"  Stage {i}:  T_IC = {st.T_IC*100:.3f} %")

# %% [markdown]
# ### 1.2 Evaluate the cascade at these operating points

# %%
result = cascade_output(P_in, opt_stages, [eta_t])

for i, entry in enumerate(result["per_stage"], 1):
    print(f"\nStage {i}:")
    print(f"  Input power      = {entry['input_W']:.4f} W")
    print(f"  Circulating power = {entry['circulating_W']:.2f} W")
    print(f"  Harmonic power   = {entry['harmonic_W']:.4f} W")
    if entry["into_next_stage_W"] is not None:
        print(f"  Into next stage  = {entry['into_next_stage_W']:.4f} W")

print(f"\nTotal harmonic output = {result['total_harmonic_W']:.4f} W")
print(f"Overall efficiency    = {result['total_efficiency']*100:.2f} %")

# %% [markdown]
# **Take-away.** Read each stage efficiency from the powers printed above.
# Their product, including the relay throughput, gives the overall efficiency:
#
# $$\eta_\mathrm{overall} = \eta_1 \times \eta_t \times \eta_2$$
#
# This is power accounting at the evaluated operating points, including
# depletion; it does not require impedance matching or a small-signal limit.

# %% [markdown]
# ## 2. Why the cascade factorises exactly
#
# You might expect that optimising a cascade requires solving a coupled
# two-variable problem (T₁ and T₂ jointly).  It does not.
#
# The reason is **one-way coupling**: stage 2 does not feed back into stage 1.
# The total harmonic output is
#
# $$P_{h,\mathrm{tot}} = P_{h,2}\bigl(P_{h,1}(T_1), \, T_2\bigr)$$
#
# Taking the derivative with respect to $T_1$:
#
# $$\frac{\partial P_{h,\mathrm{tot}}}{\partial T_1}
#   = \underbrace{\frac{\partial P_{h,2}}{\partial P_{h,1}}}_{> 0}
#     \times
#     \underbrace{\frac{\mathrm d P_{h,1}}{\mathrm d T_1}}_{= 0 \text{ at optimum}}
#   + \underbrace{\frac{\partial P_{h,2}}{\partial T_2}}_{= 0 \text{ at optimum}}
#     \times
#     \underbrace{\frac{\mathrm d T_2^*}{\mathrm d T_1}}_{\text{whatever}}$$
#
# The second term vanishes because $T_2^*$ is already the optimum for stage 2
# (its own derivative is zero).  The first term vanishes because
# $\mathrm d P_{h,1}/\mathrm d T_1 = 0$ at the stage-1 optimum.  Therefore the
# cascade-optimum condition reduces to **independently impedance-matching each
# stage**.
#
# This holds **exactly**, not just in the small-signal limit.

# %% [markdown]
# ## 3. Visualising the factorisation
#
# We sweep $T_1$ and $T_2$ on a grid and colour the total harmonic output.
# The maximum sits exactly at the independently-optimised values.

# %%
T1_grid = np.linspace(0.005, 0.08, 80)
T2_grid = np.linspace(0.01, 0.15, 80)
P_tot = np.zeros((len(T2_grid), len(T1_grid)))

for i, T2 in enumerate(T2_grid):
    for j, T1 in enumerate(T1_grid):
        stages = [
            Stage(s1["loss_per_pass"], s1["gamma_shg"], T1),
            Stage(s2["loss_per_pass"], s2["gamma_shg"], T2),
        ]
        P_tot[i, j] = cascade_output(P_in, stages, [eta_t])["total_harmonic_W"]

fig, ax = plt.subplots(figsize=(7, 5.5))
im = ax.contourf(T1_grid * 100, T2_grid * 100, P_tot, levels=20, cmap="viridis")
ax.plot(
    [opt_stages[0].T_IC * 100],
    [opt_stages[1].T_IC * 100],
    "r*",
    ms=14,
    label="Independent optima",
)
ax.set_xlabel("Stage-1 transmission  $T_1$ (%)")
ax.set_ylabel("Stage-2 transmission  $T_2$ (%)")
ax.set_title("Total harmonic output (W) — 2-D sweep")
fig.colorbar(im, ax=ax, label=r"$P_{h,\mathrm{tot}}$ (W)")
ax.legend(loc="lower right")
fig.tight_layout()

# %% [markdown]
# **Take-away.** The red star (independent optima) sits exactly on the ridge
# of the landscape.  There is no coupled optimum to search for — you simply
# match each stage to its own input power.

# %% [markdown]
# ## 4. Applying the model to measured stages
#
# **Updated 2026-09-10 (RC-07).** The former Friedenauer comparison used
# the incorrect SHG normalization and assumed passive loss L=T_IC. Its
# agreement at one BBO output did not validate the material constants.
# Nonlinear impedance matching gives T=L+(1-L)η; coupler transmission
# therefore cannot be substituted for passive loss.
#
# The [dated recalculation](../review/2026-09-10-rc07-recalculation.html)
# compares fixed-coupler outputs, independently optimized stages, and
# losses fitted to the reported operating points. It separates holding
# losses fixed from refitting them after the γ correction. Fitting the
# same output you later reproduce is calibration, not a validation test.
# UV extraction and inter-stage transport also need explicit assumptions.
#
# %% [markdown]
# ## 5. Try this
#
# Edit `parameter_overrides` (or the local `04-params.yaml`) and experiment:
# - Make stage 1 much stronger than stage 2 (swap γ values).  Does the
#   overall efficiency change?  (Hint: the bottleneck is usually the
#   *downstream* stage because it sees less power.)
# - Reduce the transport efficiency to 0.50 (a poorly mode-matched relay).
#   How much does the overall efficiency drop?
# - Add a third stage with γ = 0.1 W⁻¹.  What T_IC does the optimiser
#   choose, and what is the three-stage overall efficiency?

# %%
print("Tutorial 04 complete.")
