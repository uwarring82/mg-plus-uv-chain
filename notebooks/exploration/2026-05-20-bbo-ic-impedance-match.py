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
# # BC-B · BBO IC impedance-match sweep — 2026-05-20
#
# **`pre-G1, exploratory`** (CHARTER §5.1)
# **Origin.** This notebook was produced during BC-B of the BBO
# coating-run WP at
# [`logbook/2026-05-20-bbo-coating-run-wp/`](../../logbook/2026-05-20-bbo-coating-run-wp/).
# It was promoted from that folder to `/notebooks/exploration/` at
# BC-F closure (2026-05-20) per the parent
# [`workplan.md`](../../logbook/2026-05-20-bbo-coating-run-wp/workplan.md) §6 Q8.
#
# **Author:** assistant under steward direction · **Date:** 2026-05-20
#
# **Purpose.** Generate the impedance-match table that BC-C consumes:
# per scenario × per `L_total_VENDOR_grid` point, report `T_IC_opt`,
# circulating power, peak intensity, UV output, plus two sensitivity
# columns (manufacturing tolerance and physics tolerance).
#
# **γ authority.** This notebook **does not derive γ**. It consumes
# `γ_SHG_BBO_PHE = 1.4914e-4 W⁻¹` from
# [`constants.md`](../../logbook/2026-05-20-bbo-coating-run-wp/constants.md)
# §A3 (sole γ authority for this WP).
#
# **Acceptance gates (workplan §4 BC-B):**
# 1. Forward cross-check: at `(P_in = 0.95 W, T_IC = 0.016)` with the
#    BC-A pinned `(L_PHE, γ_PHE)`, reproduce `P_UV = 0.275 W` within 5 %.
# 2. Optimum-finding: report `T_IC_opt(0.95 W, L_PHE, γ_PHE)` (expected
#    ≈ 0.022; surfaces that Friedenauer ran below the optimum).
# 3. Grid: 2 scenarios × 4 `L_total` points; with both sensitivity
#    columns.

# %%
# -----------------------------------------------------------------------------
# Imports + path setup
# -----------------------------------------------------------------------------
from __future__ import annotations

import math
import sys
from pathlib import Path

REPO_ROOT = Path.cwd().resolve()
while not (REPO_ROOT / "pyproject.toml").exists() and REPO_ROOT != REPO_ROOT.parent:
    REPO_ROOT = REPO_ROOT.parent
sys.path.insert(0, str(REPO_ROOT))

from src.enhancement_cavity import (  # noqa: E402
    circulating_power,
    harmonic_output_W,
    optimal_input_coupler,
)

print(f"REPO_ROOT: {REPO_ROOT}")

# %% [markdown]
# ## 1. Constants — sourced from `constants.md` §F
#
# Every numeric below comes from BC-A's
# [`constants.md`](../../logbook/2026-05-20-bbo-coating-run-wp/constants.md).
# If any of these change, this notebook does not "fix" — `constants.md`
# is updated first and the notebook is re-run.

# %%
# γ — pinned in constants.md §A3 (sole γ authority)
GAMMA_BBO_PHE = 1.4914e-4  # W^-1 (Phase E central, d_eff = 1.44 pm/V)
GAMMA_BBO_LOW = 1.2155e-4  # W^-1 (d_eff = 1.30 pm/V)
GAMMA_BBO_HIGH = 1.8412e-4  # W^-1 (d_eff = 1.60 pm/V)

# Loss decomposition (constants.md §B)
L_PASSIVE_PHE = 15_288e-6  # round-trip total at Friedenauer corner
L_MIRROR_T_AT_SPEC_LIMIT = 3_400e-6  # upper envelope from R-floors
L_NONMIRROR_PHE = L_PASSIVE_PHE - L_MIRROR_T_AT_SPEC_LIMIT  # = 11 888 ppm

# Friedenauer corner (for the forward cross-check)
P_IN_FRIEDENAUER = 0.95  # W of 559 nm into BBO ring
T_IC_FRIEDENAUER = 0.016  # paper-stated R = 0.984
P_UV_FRIEDENAUER = 0.275  # W published

# BBO beam geometry (constants.md §A1)
W0_BBO = 19.4e-6  # m
LAMBDA_559 = 559e-9  # m
N_O_559 = 1.67276  # BBO ordinary at 559
F_FOCUSING = 25e-3  # m
D_PRIME = 59.4e-3  # m (focusing-mirror separation)

# Two-scenario input powers (workplan §1 + §6 Q1)
P_IN_LOW = 0.50  # W (low scenario)
P_IN_HIGH = 1.50  # W (high scenario)

print("Constants loaded from constants.md §F:")
print(f"  γ_SHG_BBO (Phase E central)   = {GAMMA_BBO_PHE:.4e} W⁻¹")
print(f"  L_passive_PHE                  = {L_PASSIVE_PHE*1e6:.0f} ppm")
print(f"  L_nonmirror_PHE                = {L_NONMIRROR_PHE*1e6:.0f} ppm")
print(f"  L_mirror_T_at_spec_limit       = {L_MIRROR_T_AT_SPEC_LIMIT*1e6:.0f} ppm")
print(f"  Two scenarios at 559 nm        = {P_IN_LOW} W, {P_IN_HIGH} W")

# %% [markdown]
# ## 2. Forward cross-check (acceptance gate 1)
#
# At Friedenauer's published operating point with the BC-A-pinned
# `(L_passive_PHE, γ_BBO_PHE)`, the forward solver must reproduce the
# published `P_UV = 0.275 W` within 5 %. This is the binding one-equation
# test on the model.

# %%
P_UV_cross_check = harmonic_output_W(
    P_IN_FRIEDENAUER, T_IC_FRIEDENAUER, L_PASSIVE_PHE, GAMMA_BBO_PHE
)
residual_pct = (P_UV_cross_check - P_UV_FRIEDENAUER) / P_UV_FRIEDENAUER * 100.0

print("Acceptance gate 1 — Friedenauer forward cross-check")
print(f"  Inputs: P_in = {P_IN_FRIEDENAUER} W, T_IC = {T_IC_FRIEDENAUER}, "
      f"L = {L_PASSIVE_PHE*1e6:.0f} ppm, γ = {GAMMA_BBO_PHE:.4e} W⁻¹")
print(f"  P_UV computed = {P_UV_cross_check:.4f} W")
print(f"  P_UV published = {P_UV_FRIEDENAUER:.4f} W")
print(f"  Residual = {residual_pct:+.2f} %  ({'PASS' if abs(residual_pct) < 5 else 'FAIL'} 5 % gate)")

# %% [markdown]
# ## 3. Optimum-finding (acceptance gate 2, reported as a finding)
#
# `T_IC_opt(0.95 W, L_PHE, γ_PHE)` is expected to differ from
# Friedenauer's procured 0.016 — surfacing that Friedenauer ran below
# the impedance-matched optimum at their γ. **Not a pass/fail criterion.**

# %%
T_opt_corner = optimal_input_coupler(P_IN_FRIEDENAUER, L_PASSIVE_PHE, GAMMA_BBO_PHE)
P_UV_at_opt = harmonic_output_W(P_IN_FRIEDENAUER, T_opt_corner, L_PASSIVE_PHE, GAMMA_BBO_PHE)
P_circ_at_opt = circulating_power(P_IN_FRIEDENAUER, T_opt_corner, L_PASSIVE_PHE, GAMMA_BBO_PHE)

gap_pp = (T_opt_corner - T_IC_FRIEDENAUER) * 100.0
forgone_pct = (P_UV_at_opt - P_UV_FRIEDENAUER) / P_UV_FRIEDENAUER * 100.0

print("Acceptance gate 2 — optimum-finding (Friedenauer corner)")
print(f"  T_IC_opt        = {T_opt_corner:.5f}  ({T_opt_corner*100:.2f} %)")
print(f"  T_IC published  = {T_IC_FRIEDENAUER:.5f}  ({T_IC_FRIEDENAUER*100:.2f} %)")
print(f"  Gap             = {gap_pp:+.2f} pp  (Friedenauer ran below the optimum)")
print(f"  P_UV at T_opt   = {P_UV_at_opt:.4f} W  (buildup forgone: {forgone_pct:+.2f} %)")
print(f"  P_circ at T_opt = {P_circ_at_opt:.2f} W")

# %% [markdown]
# ## 4. Helper — Gaussian beam geometry on the curved mirrors
#
# For peak-intensity reporting on the curved mirrors (BC-D will consume
# these values too).

# %%
def peak_intensity_W_per_cm2(power_W: float, w0_m: float) -> float:
    """Peak Gaussian-beam intensity = 2 P / (π w₀²), converted to W/cm²."""
    return 2.0 * power_W / (math.pi * w0_m**2) * 1e-4


def spot_radius_at_curved_mirror_proper(
    w0_m: float,
    half_crystal_m: float,
    air_distance_m: float,
    lam_m: float,
    n_crystal: float,
) -> float:
    """Proper Gaussian spot radius at the curved mirror via BBO + air propagation.

    Friedenauer's BBO sits at the short-arm waist with half-length
    `half_crystal_m` (= 5 mm) from waist to crystal exit face; the remaining
    `air_distance_m` (= d′/2 − half_crystal_m ≈ 24.7 mm) is air. Use the
    q-parameter:
        q_at_waist_in_BBO = i · zR_BBO   (zR_BBO = π n w0² / λ)
        q_at_BBO_exit = q_at_waist + half_crystal       (free space in BBO)
        q_just_after_interface = q_at_BBO_exit          (w continuous across flat interface)
        q_at_curved_mirror = q_just_after_interface + air_distance  (free space in air)
        w² at mirror = -λ / (π · n_air · Im(1/q))   with n_air = 1

    The v1 of this notebook used a single-medium call with n_BBO for the
    full distance, which underestimates the spot. Corrected here per BC-C v2.
    """
    z_R_in_crystal = math.pi * n_crystal * w0_m**2 / lam_m
    q_at_exit = complex(half_crystal_m, z_R_in_crystal)  # in BBO
    # Flat interface: w continuous, so q in air just after exit has the same
    # imaginary part (zR_in_BBO) but the same z, since w stays continuous and
    # the standard flat-interface ABCD acts as [[1,0],[0, n_BBO/n_air]] on
    # (height, slope) which leaves w continuous. For Gaussian beams the
    # transformation is q_after = q_before · (n_after / n_before) in the
    # standard sign convention; with n_after = 1 this scales q by 1/n_BBO.
    # Equivalently: zR shrinks from zR_in_BBO to zR_in_air = zR_in_BBO/n_BBO.
    # Implement both pieces explicitly:
    q_just_after_interface = complex(q_at_exit.real / n_crystal,
                                     q_at_exit.imag / n_crystal)
    q_at_mirror = q_just_after_interface + air_distance_m  # free space in air
    # 1/q = 1/R - i λ / (π n w²) ; n_air = 1
    inv_q_im = (1.0 / q_at_mirror).imag
    return math.sqrt(-lam_m / (math.pi * 1.0 * inv_q_im))


W_CURVED_BBO = spot_radius_at_curved_mirror_proper(
    w0_m=W0_BBO,
    half_crystal_m=5e-3,                   # half of 10 mm BBO crystal
    air_distance_m=D_PRIME / 2.0 - 5e-3,   # remaining short-arm distance in air
    lam_m=LAMBDA_559,
    n_crystal=N_O_559,
)
print(f"Beam geometry helpers")
print(f"  w(curved mirror, BBO + air propagation) = {W_CURVED_BBO*1e6:.0f} μm  "
      f"(waist {W0_BBO*1e6:.1f} μm, half-crystal 5 mm + air "
      f"{(D_PRIME/2-5e-3)*1e3:.1f} mm)")

# %% [markdown]
# ## 5. Main impedance-match grid (acceptance gate 3)
#
# 2 scenarios × 4 L_total grid points. Per cell:
# `T_IC_opt`, `P_circ`, `P_UV`, peak intensity at the BBO waist + on the
# curved mirrors.

# %%
SCENARIOS = [
    ("Low",  P_IN_LOW),
    ("High", P_IN_HIGH),
]

L_TOTAL_GRID = [
    ("Friedenauer R-floor (path 2 baseline)", 3_400e-6,   L_NONMIRROR_PHE + 3_400e-6),
    ("Intermediate IBS (500 ppm/mirror)",      1_500e-6,   L_NONMIRROR_PHE + 1_500e-6),
    ("Upper-class IBS (200 ppm/mirror)",         600e-6,   L_NONMIRROR_PHE +   600e-6),
    ("Cavity-finesse-grade (100 ppm/mirror)",    300e-6,   L_NONMIRROR_PHE +   300e-6),
]

grid_rows = []
print(f"\n{'Scenario':<6} {'L_total class':<42} {'L_tot ppm':>10} "
      f"{'T_IC_opt (ppm)':>14} {'T_IC_opt (pp)':>14} {'P_circ (W)':>11} "
      f"{'P_UV (W)':>10} {'I_waist (MW/cm²)':>18} {'I_curved (kW/cm²)':>19}")
print("-" * 152)
for scen_name, P_in in SCENARIOS:
    for L_name, sum_mirror, L_total in L_TOTAL_GRID:
        T_opt = optimal_input_coupler(P_in, L_total, GAMMA_BBO_PHE)
        P_c = circulating_power(P_in, T_opt, L_total, GAMMA_BBO_PHE)
        P_uv = harmonic_output_W(P_in, T_opt, L_total, GAMMA_BBO_PHE)
        I_waist = peak_intensity_W_per_cm2(P_c, W0_BBO) / 1e6   # MW/cm²
        I_curved = peak_intensity_W_per_cm2(P_c, W_CURVED_BBO) / 1e3  # kW/cm²
        grid_rows.append({
            "scenario": scen_name,
            "P_in_W": P_in,
            "L_name": L_name,
            "sum_mirror_ppm": sum_mirror * 1e6,
            "L_total_ppm": L_total * 1e6,
            "T_IC_opt": T_opt,
            "P_circ_W": P_c,
            "P_UV_W": P_uv,
            "I_waist_MW_cm2": I_waist,
            "I_curved_kW_cm2": I_curved,
        })
        print(f"{scen_name:<6} {L_name:<42} {L_total*1e6:>10.0f} "
              f"{T_opt*1e6:>14.0f} {T_opt*100:>14.3f} {P_c:>11.2f} "
              f"{P_uv:>10.4f} {I_waist:>18.2f} {I_curved:>19.1f}")

# %% [markdown]
# ## 6. Manufacturing tolerance sensitivity
#
# For each cell, UV-output drop when `T_IC` lands at `T_IC_opt ± Δ`.
# Four bands: `± 0.5 pp`, `± 1.0 pp` (the wide regime; reviewer-flagged
# realistic IBS batch-to-batch drift), `± 500 ppm`, `± 1 000 ppm` (the
# fine regime where IBS metrology is actually challenged).

# %%
TOL_BANDS = [
    ("±  500 ppm", 500e-6),
    ("± 1000 ppm", 1000e-6),
    ("±   0.5 pp", 0.005),
    ("±   1.0 pp", 0.010),
]

print(f"\n{'Scenario':<6} {'L_total ppm':>11} {'T_IC_opt (ppm)':>15} "
      f"{'P_UV_opt (W)':>13}", end="")
for label, _ in TOL_BANDS:
    print(f" {('ΔP_UV ' + label):>16}", end="")
print()
print("-" * 150)
for row in grid_rows:
    T_opt = row["T_IC_opt"]
    P_uv_opt = row["P_UV_W"]
    L_total = row["L_total_ppm"] * 1e-6
    P_in = row["P_in_W"]
    print(f"{row['scenario']:<6} {row['L_total_ppm']:>11.0f} "
          f"{T_opt*1e6:>15.0f} {P_uv_opt:>13.4f}", end="")
    for label, delta in TOL_BANDS:
        # Worst-case across +Δ and −Δ
        P_uv_plus = harmonic_output_W(P_in, min(0.999, T_opt + delta), L_total, GAMMA_BBO_PHE)
        P_uv_minus = harmonic_output_W(P_in, max(1e-6, T_opt - delta), L_total, GAMMA_BBO_PHE)
        # Symmetric near optimum; report max relative drop
        drop_plus_pct = (P_uv_plus - P_uv_opt) / P_uv_opt * 100.0
        drop_minus_pct = (P_uv_minus - P_uv_opt) / P_uv_opt * 100.0
        worst = min(drop_plus_pct, drop_minus_pct)  # most-negative
        print(f" {worst:>+15.2f}%", end="")
    print()

# %% [markdown]
# ## 7. Physics tolerance sensitivity (γ ± 1.5 %)
#
# The Phase E validation residual gives γ a ±1.5 % uncertainty.
# `T_IC_opt ∝ √(γ · P_in)` in the depleted regime, so a 1.5 % γ shift
# produces a ~ 0.75 % shift in `T_IC_opt`. Reporting this column
# alongside the manufacturing column prevents BC-C from over-specifying
# the manufacturing tolerance against a comparable-size physics
# uncertainty.

# %%
GAMMA_BANDS = [
    ("γ × 0.985 (−1.5 %)", GAMMA_BBO_PHE * 0.985),
    ("γ × 1.000 (PINNED)", GAMMA_BBO_PHE),
    ("γ × 1.015 (+1.5 %)", GAMMA_BBO_PHE * 1.015),
]
DEFF_BANDS = [
    ("d_eff = 1.30 (low)",     GAMMA_BBO_LOW),
    ("d_eff = 1.44 (central)", GAMMA_BBO_PHE),
    ("d_eff = 1.60 (high)",    GAMMA_BBO_HIGH),
]

print("\n=== γ ± 1.5 % bracket (Phase E validation residual) ===")
print(f"\n{'Scenario':<6} {'L_total ppm':>11}", end="")
for label, _ in GAMMA_BANDS:
    print(f" {('T_IC_opt (' + label + ')'):>30}", end="")
print()
print(f"{'':<6} {'':>11}", end="")
for label, _ in GAMMA_BANDS:
    print(f" {('P_UV ' + label):>30}", end="")
print()
print("-" * 110)
for row in grid_rows:
    L_total = row["L_total_ppm"] * 1e-6
    P_in = row["P_in_W"]
    print(f"{row['scenario']:<6} {row['L_total_ppm']:>11.0f}", end="")
    for label, gamma in GAMMA_BANDS:
        T_opt = optimal_input_coupler(P_in, L_total, gamma)
        P_uv = harmonic_output_W(P_in, T_opt, L_total, gamma)
        print(f" {T_opt:>15.5f}/{P_uv:>7.4f} W", end="")
    print()

print("\n=== d_eff full bracket (1.30 → 1.60 pm/V, dominant uncertainty axis) ===")
print(f"\n{'Scenario':<6} {'L_total ppm':>11}", end="")
for label, _ in DEFF_BANDS:
    print(f" {('T_opt / P_UV @ ' + label):>32}", end="")
print()
print("-" * 115)
for row in grid_rows:
    L_total = row["L_total_ppm"] * 1e-6
    P_in = row["P_in_W"]
    print(f"{row['scenario']:<6} {row['L_total_ppm']:>11.0f}", end="")
    for label, gamma in DEFF_BANDS:
        T_opt = optimal_input_coupler(P_in, L_total, gamma)
        P_uv = harmonic_output_W(P_in, T_opt, L_total, gamma)
        print(f" {T_opt:>16.5f}/{P_uv:>8.4f} W", end="")
    print()

# %% [markdown]
# ## 8. T_IC_opt separation between scenarios — §6 Q2 input
#
# Reports the Δ`T_IC_opt` between the Low and High scenarios at each
# `L_total` grid point. The default §6 Q2 path holds the M1' coating
# spec at a single variant if Δ`T_IC_opt` ≲ 1 pp (a typical single
# coating-run tolerance); branches to two M1' variants otherwise.

# %%
print(f"\n{'L_total class':<42} {'L_tot ppm':>10} "
      f"{'T_opt Low':>11} {'T_opt High':>12} {'ΔT_opt (pp)':>13} "
      f"{'ΔT_opt (ppm)':>14} {'§6 Q2 default':>20}")
print("-" * 140)
for L_name, sum_mirror, L_total in L_TOTAL_GRID:
    T_low = optimal_input_coupler(P_IN_LOW, L_total, GAMMA_BBO_PHE)
    T_high = optimal_input_coupler(P_IN_HIGH, L_total, GAMMA_BBO_PHE)
    delta_pp = (T_high - T_low) * 100.0
    delta_ppm = (T_high - T_low) * 1e6
    if delta_pp <= 1.0:
        recommend = "one variant"
    elif delta_pp <= 2.0:
        recommend = "borderline"
    else:
        recommend = "two variants"
    print(f"{L_name:<42} {L_total*1e6:>10.0f} "
          f"{T_low:>11.5f} {T_high:>12.5f} {delta_pp:>13.3f} "
          f"{delta_ppm:>14.0f} {recommend:>20}")

# %% [markdown]
# ## 9. BC-C consumption table — distilled
#
# The single per-scenario row BC-C needs. Centre point of the M1'
# coating spec, conservative tolerance band (matched to the realistic
# IBS metrology regime), worst-case UV penalty across the band, and
# `Σ T_loss_VENDOR_max` budget that the M2'/M3'/M4' coating specs must
# collectively hit.
#
# Default operating point: **`L_total = 13 388 ppm` (intermediate IBS,
# 500 ppm/mirror sum, 1500 ppm)** — the row where Δ`T_IC_opt` between
# scenarios is well below a typical IBS run tolerance and the buildup
# headroom over Friedenauer-class is meaningful. The workplan §6 Q5
# steward call could move this to the IBS upper-class row instead;
# the BC-E sheets carry both options.

# %%
DEFAULT_L_TOTAL_PPM = 13_388
DEFAULT_L_TOTAL = DEFAULT_L_TOTAL_PPM * 1e-6
DEFAULT_SUM_MIRROR_PPM = 1_500

print("BC-C consumption — default operating point "
      f"(L_total = {DEFAULT_L_TOTAL_PPM} ppm, "
      f"Σ T_loss_VENDOR_max = {DEFAULT_SUM_MIRROR_PPM} ppm)")
print()
print(f"{'Scenario':<8} {'P_in (W)':>10} {'T_IC_opt (ppm)':>15} "
      f"{'T_IC_opt (%)':>14} {'P_UV (W)':>10} {'P_circ (W)':>12} "
      f"{'I_waist MW/cm²':>16} {'I_curved kW/cm²':>17}")
print("-" * 110)
for scen_name, P_in in SCENARIOS:
    T_opt = optimal_input_coupler(P_in, DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
    P_c = circulating_power(P_in, T_opt, DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
    P_uv = harmonic_output_W(P_in, T_opt, DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
    I_waist = peak_intensity_W_per_cm2(P_c, W0_BBO) / 1e6
    I_curved = peak_intensity_W_per_cm2(P_c, W_CURVED_BBO) / 1e3
    print(f"{scen_name:<8} {P_in:>10.2f} {T_opt*1e6:>15.0f} "
          f"{T_opt*100:>14.3f} {P_uv:>10.4f} {P_c:>12.2f} "
          f"{I_waist:>16.2f} {I_curved:>17.1f}")

# Recommended tolerance for the BC-E spec sheets
# At the default L_total, characterise UV penalty at multiple bands
print(f"\nRecommended M1' coating-spec tolerance at the default L_total")
print(f"  (worst-case UV penalty across +Δ and −Δ from T_IC_opt)")
print(f"{'Scenario':<8} {'Band':<12} {'UV penalty':>12}")
print("-" * 45)
for scen_name, P_in in SCENARIOS:
    T_opt = optimal_input_coupler(P_in, DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
    P_uv_opt = harmonic_output_W(P_in, T_opt, DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
    for label, delta in TOL_BANDS:
        P_uv_plus = harmonic_output_W(P_in, min(0.999, T_opt + delta),
                                       DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
        P_uv_minus = harmonic_output_W(P_in, max(1e-6, T_opt - delta),
                                       DEFAULT_L_TOTAL, GAMMA_BBO_PHE)
        worst = min(
            (P_uv_plus - P_uv_opt) / P_uv_opt * 100.0,
            (P_uv_minus - P_uv_opt) / P_uv_opt * 100.0,
        )
        print(f"{scen_name:<8} {label:<12} {worst:>+11.2f}%")

# %% [markdown]
# ## 10. Acceptance summary
#
# Per workplan §4 BC-B acceptance:
# - Gate 1 (forward cross-check) status from §2 above.
# - Gate 2 (optimum-finding) status from §3 above.
# - Gate 3 (grid + sensitivity) populated by §5 / §6 / §7.
#
# The BC-C consumption table in §9 is the single row downstream
# consumers need.

# %%
print("=" * 70)
print("BC-B ACCEPTANCE SUMMARY")
print("=" * 70)
print(f"Gate 1 (forward cross-check, 5 %): residual = {residual_pct:+.2f} %  "
      f"{'PASS' if abs(residual_pct) < 5 else 'FAIL'}")
print(f"Gate 2 (T_IC_opt finding):  {T_opt_corner:.5f}  vs Friedenauer 0.016  "
      f"(reported as a finding)")
print(f"Gate 3 (grid table):        2 scenarios × {len(L_TOTAL_GRID)} L_total "
      f"points × {len(TOL_BANDS)} tolerance bands + γ ± 1.5 % column populated")
print("=" * 70)
