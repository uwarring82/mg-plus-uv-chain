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
# # Friedenauer 2006 — Cascade re-computation using Phases A–C primitives
#
# **`pre-G1, diagnostic surrogate, not promoted`** (CHARTER §5.1)
#
# **Date:** 2026-05-07 · **Author:** assistant under steward direction
#
# This notebook uses the architecture-neutral numerics primitives
# (`src.shg_single_pass`, `src.enhancement_cavity`, `src.shg_cascade`) to
# reproduce the published outputs of Friedenauer 2006:
#
# - **LBO stage:** 0.95 W at 559 nm (η = 52.7 % relative to 1.80 W input).
# - **BBO stage:** 0.275 W near 280 nm (η = 28.9 % relative to 0.95 W input).
# - **Overall:** 15.2 % conversion 1118 nm → 280 nm.
#
# It documents discrepancies attributable to the `open_extraction_items`
# already on file (BBO d_eff, walk-off ρ, refractive indices).
#
# **CHARTER §5.1 compliance.** This notebook lives under `/notebooks/diagnostic/`.
# It imports from `data.literature.Friedenauer2006` (architecture-specific
# parameters) and therefore must never be promoted to `/src/`.

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

import yaml  # noqa: E402

from src import boyd_kleinman as bk  # noqa: E402
from src.enhancement_cavity import (  # noqa: E402
    circulating_power,
    harmonic_output_W,
    optimal_input_coupler,
)
from src.shg_cascade import Stage, cascade_output, optimise_cascade  # noqa: E402
from src.shg_single_pass import gamma_shg_coefficient  # noqa: E402

print(f"REPO_ROOT: {REPO_ROOT}")

# %%
# -----------------------------------------------------------------------------
# Load Friedenauer 2006 extracted parameters
# -----------------------------------------------------------------------------
EXTRACTION_PATH = REPO_ROOT / "data" / "literature" / "Friedenauer2006" / "extracted.yaml"
with EXTRACTION_PATH.open() as f:
    fr = yaml.safe_load(f)

fr_param = {param["symbol"]: param for param in fr["parameters"]}

# LBO stage — directly from extraction
P_LBO_in = fr_param["P_LBO_in"]["value"]
L_LBO_m = fr_param["L_LBO_crystal"]["value"]
w0_LBO_m = fr_param["w0_LBO_BK_optimum"]["value"]
R_LBO_IC = fr_param["R_LBO_input_coupler_fundamental"]["value"]
d_eff_LBO_mV = fr_param["deff_LBO_at_1118"]["value"]
lambda_LBO_m = fr_param["lambda_fundamental"]["value"]
P_559_paper_W = fr_param["P_559_output_stable"]["value"]
eta_LBO_paper = fr_param["eta_LBO_doubling"]["value"]

# BBO stage — directly from extraction
P_BBO_in = fr_param["P_BBO_in"]["value"]
L_BBO_m = fr_param["BBO_crystal_size"]["value"][2]  # 10 mm long axis
w0_BBO_m = fr_param["w0_BBO_BK_optimum"]["value"]
R_BBO_IC = fr_param["R_BBO_input_coupler_fundamental"]["value"]
lambda_BBO_m = lambda_LBO_m / 2.0  # 559 nm
P_UV_paper_W = fr_param["P_UV_out"]["value"]
eta_BBO_paper = fr_param["eta_BBO_doubling"]["value"]
eta_overall_paper = fr_param["eta_overall_1118_to_280"]["value"]

print("Loaded Friedenauer2006/extracted.yaml")
print(f"  LBO: P_in = {P_LBO_in:.2f} W,  L = {L_LBO_m*1e3:.1f} mm,  w0 = {w0_LBO_m*1e6:.1f} μm")
print(f"  BBO: P_in = {P_BBO_in:.3f} W,  L = {L_BBO_m*1e3:.1f} mm,  w0 = {w0_BBO_m*1e6:.1f} μm")

# %% [markdown]
# ## 1. Cited-literature constants (not in extraction)
#
# These are the open-extraction gaps that this notebook must bridge with
# external references. Any change to these values propagates directly into
# the recomputed efficiencies.

# %%
# Refractive indices — LBO and BBO
# LBO @ 1118 nm, Type-I NCPM: n_o ≈ 1.605 (Kato 1994 / SNLO, pending KD-UV280-007)
N_LBO_1118 = 1.605
N_LBO_559 = 1.620   # ordinary index at harmonic, approximate

# BBO @ 559 nm, Type-I (o+o→e): n_o from Eimerl 1987 Sellmeier
N_BBO_O_559 = 1.67276
N_BBO_E_280 = 1.565  # extraordinary at harmonic, approximate

# BBO walk-off — Eimerl 1987 derived at θ_PM ≈ 44.2°
RHO_BBO_RAD = 0.0831  # 83.1 mrad

# BBO d_eff — *not* in Friedenauer extraction.
# The open_extraction_items flag this. We use the Eckardt-anchored central
# value (1.44 pm/V, range 1.30–1.60) as the working assumption, and bracket
# the sensitivity below.
D_EFF_BBO_CENTRAL_mV = 1.44e-12
D_EFF_BBO_LOW_mV = 1.30e-12
D_EFF_BBO_HIGH_mV = 1.60e-12

print("Cited constants (not in extraction):")
print(f"  n_LBO(1118) = {N_LBO_1118}")
print(f"  n_BBO_o(559) = {N_BBO_O_559}")
print(f"  ρ_BBO = {RHO_BBO_RAD*1e3:.1f} mrad")
print(f"  d_eff(BBO) central = {D_EFF_BBO_CENTRAL_mV*1e12:.2f} pm/V")

# %% [markdown]
# ## 2. BK focusing factors from published waists
#
# We compute the actual ξ = L/b that Friedenauer's reported w0 implies,
# then evaluate h_m at that ξ (with walk-off for BBO). This is more
# accurate than assuming the theoretical optimum, because the paper's
# w0 already embeds cavity-specific trade-offs.

# %%
def xi_from_waist(L_m: float, lam_m: float, n: float, w0_m: float) -> float:
    """BK focusing parameter ξ = L / b = L·λ / (2π·n·w0²)."""
    return L_m * lam_m / (2.0 * math.pi * n * w0_m**2)


def beta_walkoff(rho_rad: float, L_m: float, lam_m: float, n: float) -> float:
    """BK walk-off parameter β = (ρ/2)·√(L·k₁)."""
    k1 = 2.0 * math.pi * n / lam_m
    return 0.5 * rho_rad * math.sqrt(L_m * k1)


# LBO: NCPM → β = 0
xi_LBO = xi_from_waist(L_LBO_m, lambda_LBO_m, N_LBO_1118, w0_LBO_m)
h_m_LBO = bk.h_m_factor(xi=xi_LBO, beta=0.0, kappa=0.0, mu=0.0)
print(f"LBO: ξ = {xi_LBO:.3f},  h_m = {h_m_LBO:.4f}")

# BBO: with walk-off
xi_BBO = xi_from_waist(L_BBO_m, lambda_BBO_m, N_BBO_O_559, w0_BBO_m)
beta_BBO = beta_walkoff(RHO_BBO_RAD, L_BBO_m, lambda_BBO_m, N_BBO_O_559)
h_m_BBO = bk.h_m_factor(xi=xi_BBO, beta=beta_BBO, kappa=0.0, mu=0.0)
print(f"BBO: ξ = {xi_BBO:.3f},  β = {beta_BBO:.2f},  h_m = {h_m_BBO:.4f}")

# %% [markdown]
# ## 3. Single-pass γ_SHG for each stage

# %%
gamma_LBO = gamma_shg_coefficient(
    d_eff_mV=d_eff_LBO_mV,
    n_omega=N_LBO_1118,
    n_2omega=N_LBO_559,
    wavelength_m=lambda_LBO_m,
    length_m=L_LBO_m,
    h_m=h_m_LBO,
)
print(f"LBO γ_SHG = {gamma_LBO:.4e} W⁻¹")

# BBO — central value plus sensitivity bracket
gamma_BBO_central = gamma_shg_coefficient(
    d_eff_mV=D_EFF_BBO_CENTRAL_mV,
    n_omega=N_BBO_O_559,
    n_2omega=N_BBO_E_280,
    wavelength_m=lambda_BBO_m,
    length_m=L_BBO_m,
    h_m=h_m_BBO,
)
gamma_BBO_low = gamma_shg_coefficient(
    d_eff_mV=D_EFF_BBO_LOW_mV,
    n_omega=N_BBO_O_559,
    n_2omega=N_BBO_E_280,
    wavelength_m=lambda_BBO_m,
    length_m=L_BBO_m,
    h_m=h_m_BBO,
)
gamma_BBO_high = gamma_shg_coefficient(
    d_eff_mV=D_EFF_BBO_HIGH_mV,
    n_omega=N_BBO_O_559,
    n_2omega=N_BBO_E_280,
    wavelength_m=lambda_BBO_m,
    length_m=L_BBO_m,
    h_m=h_m_BBO,
)
print(f"BBO γ_SHG (central) = {gamma_BBO_central:.4e} W⁻¹")
print(f"BBO γ_SHG (low)     = {gamma_BBO_low:.4e} W⁻¹")
print(f"BBO γ_SHG (high)    = {gamma_BBO_high:.4e} W⁻¹")

# %% [markdown]
# ## 4. Per-stage cavity simulation
#
# The paper states the input-coupler reflectivity was "chosen to impedance-match
# the intracavity losses." We therefore set `loss_per_pass ≈ T_IC = 1 − R_IC` as
# the working assumption, then verify self-consistency via
# `optimal_input_coupler`.

# %%
# LBO stage
T_LBO = 1.0 - R_LBO_IC
L_loss_LBO = T_LBO  # impedance-match assumption

T_opt_LBO = optimal_input_coupler(P_LBO_in, L_loss_LBO, gamma_LBO)
P_circ_LBO = circulating_power(P_LBO_in, T_opt_LBO, L_loss_LBO, gamma_LBO)
P_h_LBO = harmonic_output_W(P_LBO_in, T_opt_LBO, L_loss_LBO, gamma_LBO)
eta_LBO_recomp = P_h_LBO / P_LBO_in

print("LBO stage")
print(f"  T_IC (paper)      = {T_LBO:.4f}")
print(f"  T_IC (optimised)  = {T_opt_LBO:.4f}")
print(f"  P_circ            = {P_circ_LBO:.2f} W")
print(f"  P_harmonic        = {P_h_LBO:.3f} W")
print(f"  η (recomputed)    = {eta_LBO_recomp:.3f}")
print(f"  η (paper)         = {eta_LBO_paper:.3f}")

# BBO stage — central assumption
T_BBO = 1.0 - R_BBO_IC
L_loss_BBO = T_BBO

T_opt_BBO = optimal_input_coupler(P_BBO_in, L_loss_BBO, gamma_BBO_central)
P_circ_BBO = circulating_power(P_BBO_in, T_opt_BBO, L_loss_BBO, gamma_BBO_central)
P_h_BBO_central = harmonic_output_W(P_BBO_in, T_opt_BBO, L_loss_BBO, gamma_BBO_central)
eta_BBO_recomp = P_h_BBO_central / P_BBO_in

print("\nBBO stage (central d_eff assumption)")
print(f"  T_IC (paper)      = {T_BBO:.4f}")
print(f"  T_IC (optimised)  = {T_opt_BBO:.4f}")
print(f"  P_circ            = {P_circ_BBO:.2f} W")
print(f"  P_harmonic        = {P_h_BBO_central:.3f} W")
print(f"  η (recomputed)    = {eta_BBO_recomp:.3f}")
print(f"  η (paper)         = {eta_BBO_paper:.3f}")

# BBO sensitivity bracket
for label, gamma in [("low", gamma_BBO_low), ("high", gamma_BBO_high)]:
    T_opt = optimal_input_coupler(P_BBO_in, L_loss_BBO, gamma)
    P_h = harmonic_output_W(P_BBO_in, T_opt, L_loss_BBO, gamma)
    print(f"\nBBO stage ({label} d_eff)")
    print(f"  P_harmonic        = {P_h:.3f} W")
    print(f"  η (recomputed)    = {P_h / P_BBO_in:.3f}")

# %% [markdown]
# ## 5. Cascade simulation
#
# The cascade uses the architecture-neutral `src.shg_cascade` primitives.
# Transport efficiency from LBO harmonic output to BBO input is inferred
# from the fact that `P_BBO_in = P_559_output_stable = 0.950 W`, i.e.
# essentially unity (any relay losses are absorbed into the reported
# 0.950 W BBO input figure).

# %%
# Fixed operating points: use the paper's T_IC values
stage_LBO = Stage(loss_per_pass=L_loss_LBO, gamma_shg=gamma_LBO, T_IC=T_LBO)
stage_BBO_central = Stage(loss_per_pass=L_loss_BBO, gamma_shg=gamma_BBO_central, T_IC=T_BBO)

# Cascade with near-unity transport
transport = 1.0
cascade_central = cascade_output(P_LBO_in, [stage_LBO, stage_BBO_central], [transport])

P_UV_central = cascade_central["total_harmonic_W"]
eta_overall_central = cascade_central["total_efficiency"]

print("Cascade (central d_eff assumption, transport = 1.0)")
print(f"  LBO harmonic      = {cascade_central['per_stage'][0]['harmonic_W']:.3f} W")
print(f"  BBO input         = {cascade_central['per_stage'][1]['input_W']:.3f} W")
print(f"  UV output         = {P_UV_central:.3f} W")
print(f"  Overall η         = {eta_overall_central:.3f}")
print(f"  Paper overall η   = {eta_overall_paper:.3f}")

# Sensitivity: vary BBO d_eff
for label, gamma in [("low", gamma_BBO_low), ("high", gamma_BBO_high)]:
    stage_BBO = Stage(loss_per_pass=L_loss_BBO, gamma_shg=gamma, T_IC=T_BBO)
    result = cascade_output(P_LBO_in, [stage_LBO, stage_BBO], [transport])
    print(f"\nCascade (BBO {label} d_eff)")
    print(f"  UV output         = {result['total_harmonic_W']:.3f} W")
    print(f"  Overall η         = {result['total_efficiency']:.3f}")

# %% [markdown]
# ## 6. Optimised cascade (impedance-matched T_IC per stage)
#
# Recompute with `optimise_cascade` to check whether the paper's T_IC values
# are close to the self-consistent impedance-matched values.

# %%
opt_stages = optimise_cascade(
    P_LBO_in,
    stage_params=[(L_loss_LBO, gamma_LBO), (L_loss_BBO, gamma_BBO_central)],
    transport_efficiencies=[transport],
)

opt_cascade = cascade_output(P_LBO_in, opt_stages, [transport])

print("Optimised cascade")
print(f"  LBO T_IC (paper)      = {T_LBO:.4f}")
print(f"  LBO T_IC (optimised)  = {opt_stages[0].T_IC:.4f}")
print(f"  BBO T_IC (paper)      = {T_BBO:.4f}")
print(f"  BBO T_IC (optimised)  = {opt_stages[1].T_IC:.4f}")
print(f"  UV output             = {opt_cascade['total_harmonic_W']:.3f} W")
print(f"  Overall η             = {opt_cascade['total_efficiency']:.3f}")

# %% [markdown]
# ## 7. Summary table and discrepancy attribution

# %%
print(f"{'Quantity':<30} {'Paper':>12} {'Recomp.':>12} {'Discrepancy':>14}")
print("-" * 70)

print(
    f"{'LBO 559 nm output (W)':<30} "
    f"{P_559_paper_W:>12.3f} {P_h_LBO:>12.3f} "
    f"{(P_h_LBO - P_559_paper_W) / P_559_paper_W * 100:>+13.1f} %"
)

print(
    f"{'BBO 280 nm output (W)':<30} "
    f"{P_UV_paper_W:>12.3f} {P_h_BBO_central:>12.3f} "
    f"{(P_h_BBO_central - P_UV_paper_W) / P_UV_paper_W * 100:>+13.1f} %"
)

print(
    f"{'Overall 1118→280 η (%)':<30} "
    f"{eta_overall_paper * 100:>12.1f} {eta_overall_central * 100:>12.1f} "
    f"{(eta_overall_central - eta_overall_paper) / eta_overall_paper * 100:>+13.1f} %"
)

print(f"\nBBO d_eff sensitivity bracket:")
print(f"  UV output (low d_eff)  = {cascade_output(P_LBO_in, [stage_LBO, Stage(L_loss_BBO, gamma_BBO_low, T_BBO)], [transport])['total_harmonic_W']:.3f} W")
print(f"  UV output (high d_eff) = {cascade_output(P_LBO_in, [stage_LBO, Stage(L_loss_BBO, gamma_BBO_high, T_BBO)], [transport])['total_harmonic_W']:.3f} W")

# %% [markdown]
# ## 8. Open extraction items and attribution
#
# The following gaps in `data/literature/Friedenauer2006/extracted.yaml` are
# the dominant sources of recomputation uncertainty. They are already flagged
# in the YAML's `open_extraction_items` block; this notebook quantifies their
# impact.
#
# | Item | Status | Impact on this notebook |
# |---|---|---|
# | `d_eff(BBO)` at 559 nm Type-I | **Closed (2026-05-04)** — Eckardt-anchored central 1.44 pm/V (range 1.30–1.60). | Dominant uncertainty for BBO stage; bracket spans ±11 % in d_eff → ±23 % in UV power. |
# | `walk-off ρ` for BBO Type-I at 559→280 | **Closed (2026-05-04)** — Eimerl-derived ρ = 83.1 mrad. | Drives h_m down to ~0.02 (severe walk-off limit); any ρ error propagates directly into h_m. |
# | `n_LBO(1118)`, `n_LBO(559)` | **Open** — placeholder 1.605 / 1.620 used. | Affects LBO γ_SHG at the ~few-% level; h_m is insensitive to n (n cancels in ξ = Lλ/(2π n w0²) if w0 is paper-reported). |
# | `n_BBO_o(559)`, `n_BBO_e(280)` | **Partially closed** — Eimerl Sellmeier gives n_o(559) = 1.67276; n_e(280) still approximate. | Affects BBO γ_SHG at the ~few-% level. |
# | Cavity passive losses beyond IC | **Open** — assumed L_passive = T_IC. | If true passive loss is lower, the paper operated slightly over-coupled, which would raise circulating power and harmonic output. |
#
# **Promotion guard.** None of the architecture-specific parameters used here
# (crystal constants, Friedenauer-extracted geometries) may be promoted to `/src/`
# without first passing through the Phase 1/Phase 3 crystallographic review.
