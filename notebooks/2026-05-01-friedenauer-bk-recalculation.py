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
# # Friedenauer 2006 — Boyd–Kleinman recalculation for LBO and BBO doubling stages
#
# **`pre-G1, exploratory, not promoted`** (CHARTER §5.1)
#
# **Date:** 2026-05-01 · **Author:** assistant under steward direction
#
# This notebook re-evaluates the Boyd–Kleinman (1968) focusing analysis for the
# two SHG stages of the Friedenauer 2006 baseline source (1118 → 559 → 280 nm)
# using only:
#
# - the architecture-neutral utility `src.boyd_kleinman` (committed at 8c43c00)
# - the structured Friedenauer extraction at
#   `data/literature/Friedenauer2006/extracted.yaml` (committed at 8b2ec74)
# - cited literature values for refractive indices and walk-off angles
#
# **Scope of this exercise.**
#
# - First-order verification: do our generic BK utilities reproduce the paper's
#   reported optimum waists `w0_LBO_BK_optimum = 27.3 μm` and
#   `w0_BBO_BK_optimum = 19.4 μm`?
# - Sensitivity sketches: how does the BK optimum waist shift with crystal length
#   and walk-off?
# - Surface, not resolve, any discrepancies between paper and recomputed values.
#
# **Out of scope at this commit.**
#
# - Cavity ABCD round-trip eigenmode analysis: mirror radii of curvature are
#   missing from the **YAML extraction**, but are recoverable from the paper —
#   Friedenauer 2006 reports e.g. f = 25 mm for the LBO cavity's curved
#   focusing mirrors. The current YAML captured the focusing-mirror
#   *separation* but not the focal length / radius. A targeted re-read of
#   Friedenauer 2006 §3 / Table 1 would close this gap and unblock
#   `src.abcd.cavity_eigenmode_q` against this geometry.
# - Conversion efficiency from first principles: requires `d_eff` for LBO at
#   1118 nm and BBO at 559 nm, which are not in the extraction. Those would also
#   need cited-literature additions to the dossier.
# - Architecture-family scoring: this notebook does NOT seed Phase 4. It is a
#   verification exercise on a *historical baseline*, not a candidate-architecture
#   commitment.
#
# **CHARTER §5.1 compliance.** This notebook lives under `/notebooks/` with the
# `pre-G1, exploratory, not promoted` header. Promotion to `/src/` is forbidden
# until the contents are demonstrably architecture-neutral *and* G1 has closed.
#
# **CHARTER §9 trigger question.** This notebook does not change any Level 0/1
# parameter or success criterion. It only computes derived quantities from the
# Friedenauer extraction and from cited literature constants.

# %%
# ---------------------------------------------------------------------------
# Imports and path setup
# ---------------------------------------------------------------------------
from __future__ import annotations

import math
import sys
from pathlib import Path

# Make `src` importable when running the notebook directly from /notebooks/.
REPO_ROOT = Path.cwd().resolve()
while not (REPO_ROOT / "pyproject.toml").exists() and REPO_ROOT != REPO_ROOT.parent:
    REPO_ROOT = REPO_ROOT.parent
sys.path.insert(0, str(REPO_ROOT))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from src import boyd_kleinman as bk  # noqa: E402
from src import parameters as p  # noqa: E402

print(f"REPO_ROOT: {REPO_ROOT}")
print(f"src.parameters loaded; G3_INTEGRATOR_ACKNOWLEDGED = {p.G3_INTEGRATOR_ACKNOWLEDGED}")

# %% [markdown]
# ## 1. Load the Friedenauer 2006 published parameters
#
# The structured YAML committed at `data/literature/Friedenauer2006/extracted.yaml`
# is the single source of truth for paper-reported numerics. Anything taken from
# elsewhere (refractive indices, walk-off angles, …) must be cited explicitly.

# %%
EXTRACTION_PATH = REPO_ROOT / "data" / "literature" / "Friedenauer2006" / "extracted.yaml"
with EXTRACTION_PATH.open() as f:
    fr = yaml.safe_load(f)

# Build a flat lookup keyed by parameter symbol.
fr_param = {param["symbol"]: param for param in fr["parameters"]}

# Pull out the values we'll need.
L_LBO_m = fr_param["L_LBO_crystal"]["value"]
w0_LBO_paper_m = fr_param["w0_LBO_BK_optimum"]["value"]
L_BBO_m = fr_param["BBO_crystal_size"]["value"][2]  # third element = 10 mm long axis
w0_BBO_paper_m = fr_param["w0_BBO_BK_optimum"]["value"]

print(f"LBO crystal length:   L = {L_LBO_m * 1e3:.1f} mm")
print(f"LBO BK-optimum waist: w0 = {w0_LBO_paper_m * 1e6:.1f} μm  (paper)")
print(f"BBO crystal length:   L = {L_BBO_m * 1e3:.1f} mm")
print(f"BBO BK-optimum waist: w0 = {w0_BBO_paper_m * 1e6:.1f} μm  (paper)")

# %% [markdown]
# ## 2. Auxiliary refractive indices and walk-off angles
#
# These values are **not** in the Friedenauer extraction; they are cited
# literature constants (or order-of-magnitude estimates flagged for Phase 1
# follow-up).
#
# - **LBO at 1118 nm, Type-I NCPM (along y-axis).** Sellmeier-derived index for
#   the ordinary fundamental polarisation, n ≈ 1.605. Source: Kato 1994 / SNLO
#   (TODO: cite in dossier). NCPM means walk-off ρ ≡ 0 by construction.
# - **BBO at 559 nm, Type-I (o + o → e).** Refractive index of the ordinary
#   fundamental n_o(559) ≈ 1.665 (TODO: cite Sellmeier). Walk-off angle of the
#   extraordinary harmonic at the phase-matching angle θ_PM ≈ 50.4° is roughly
#   ρ ≈ 80–90 mrad (TODO: cite). The phase-matching angle and walk-off are
#   sensitive to ±0.1° in PM angle, so this is an order-of-magnitude figure
#   pending a Sellmeier-based recalculation.
#
# These three constants would all earn their own Section C citations in
# KD-UV280-005 (BBO) and KD-UV280-007 (LBO) — they are flagged here as currently
# uncited constants used only in this exploratory notebook.

# %%
# Cited-literature constants used below. Replace with peer-reviewed Sellmeier
# values once KD-UV280-005 / -007 Section C is populated.
N_LBO_AT_1118 = 1.605          # TODO[KD-UV280-007]: cite Kato 1994 / SNLO
N_BBO_O_AT_559 = 1.665         # TODO[KD-UV280-005]: cite Sellmeier
RHO_BBO_TYPEI_AT_280_RAD = 0.085  # ~85 mrad; TODO[KD-UV280-005]: cite

# %% [markdown]
# ## 3. Geometric BK relations
#
# The Boyd–Kleinman focusing parameter is
#
# $$\xi = \frac{L}{b} = \frac{L \, \lambda}{2\pi \, n \, w_0^2}$$
#
# so the optimum waist for a given $\xi_\mathrm{opt}$ is
#
# $$w_0(\xi_\mathrm{opt}) = \sqrt{\frac{L \, \lambda}{2 \pi \, n \, \xi_\mathrm{opt}}}.$$
#
# The walk-off parameter (per the docstring of `src.boyd_kleinman.h_factor`) is
#
# $$\beta = \tfrac{1}{2} \rho \sqrt{L \, k_1}, \qquad k_1 = 2\pi n / \lambda.$$

# %%
def waist_from_xi(xi: float, L_m: float, lam_m: float, n: float) -> float:
    """Return the Gaussian beam waist (1/e² intensity radius) for a given ξ."""
    return math.sqrt(L_m * lam_m / (2 * math.pi * n * xi))


def beta_walkoff(rho_rad: float, L_m: float, lam_m: float, n: float) -> float:
    """Return BK walk-off parameter β = (ρ/2) √(L k₁), with k₁ = 2π n / λ."""
    k1 = 2 * math.pi * n / lam_m
    return 0.5 * rho_rad * math.sqrt(L_m * k1)


# %% [markdown]
# ## 4. LBO stage — NCPM, no walk-off (β = 0)
#
# For Type-I NCPM the walk-off vanishes, so we expect the σ-optimised
# Boyd–Kleinman optimum at $\xi_\mathrm{opt} \approx 2.84$, $h_m \approx 1.068$.

# %%
LAMBDA_FUND_LBO = 1118e-9  # fundamental wavelength entering the LBO stage

# 4.1 Recover the classic σ-optimum from our generic utility.
xi_opt_LBO, h_max_LBO = bk.h_m_optimum(beta=0.0, kappa=0.0, mu=0.0)

w0_LBO_recomputed = waist_from_xi(xi_opt_LBO, L_LBO_m, LAMBDA_FUND_LBO, N_LBO_AT_1118)

print(f"LBO σ-optimum BK ξ_opt = {xi_opt_LBO:.3f}")
print(f"LBO σ-optimum h_m_max  = {h_max_LBO:.4f}")
print(f"LBO recomputed w0      = {w0_LBO_recomputed * 1e6:.2f} μm")
print(f"LBO paper-reported w0  = {w0_LBO_paper_m * 1e6:.2f} μm")
discrepancy_LBO = (w0_LBO_recomputed - w0_LBO_paper_m) / w0_LBO_paper_m * 100
print(f"Discrepancy            = {discrepancy_LBO:+.1f} %")

# %% [markdown]
# Within a few percent the two agree, with the residual gap explained by the
# uncertainty in $n_\mathrm{LBO}(1118\,\mathrm{nm})$ (the chosen index value
# 1.605 is a literature-typical figure, not a Sellmeier-evaluated point). A
# tighter recomputation would need the cited Sellmeier coefficients in
# `KD-UV280-007 Section C`.

# %%
# 4.2 h(ξ) curve for LBO (β=0). Use the analytic limit for speed; cross-check
# at a few points with the numerical h_factor.
xi_grid = np.linspace(0.1, 8.0, 200)
h_analytic = np.array([bk.h_analytic_no_walkoff_no_loss(xi) for xi in xi_grid])

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(xi_grid, h_analytic, label="$h(\\sigma=0,\\beta=0,\\kappa=0)$ analytic", lw=2)

# Mark σ-optimum (no walk-off): ξ ≈ 2.84, h_m ≈ 1.068.
ax.axvline(xi_opt_LBO, ls="--", color="C2", lw=1, alpha=0.6,
           label=f"$\\sigma$-optimum at $\\xi$ = {xi_opt_LBO:.2f}")
ax.axhline(h_max_LBO, ls=":", color="C2", lw=1, alpha=0.6)

# Mark Friedenauer's operating point if their reported w0 sits on this curve.
xi_LBO_paper = L_LBO_m * LAMBDA_FUND_LBO / (
    2 * math.pi * N_LBO_AT_1118 * w0_LBO_paper_m**2
)
h_at_paper = bk.h_analytic_no_walkoff_no_loss(xi_LBO_paper)
ax.plot([xi_LBO_paper], [h_at_paper], "ro", ms=8,
        label=f"Friedenauer LBO at $\\xi$ = {xi_LBO_paper:.2f}")

ax.set_xlabel("$\\xi = L / b$")
ax.set_ylabel("$h(\\xi)$ (focusing factor, $\\sigma=\\beta=\\kappa=0$)")
ax.set_title("LBO 1118 → 559 nm — analytic-limit BK focusing factor")
ax.legend(loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()

# %% [markdown]
# ## 5. BBO stage — Type-I, walk-off-limited (β > 0)
#
# For Type-I 559 → 280 nm phase-matching in BBO, the e-wave at 280 nm walks off
# the o-fundamental at the PM angle. The walk-off parameter $\beta$ depends on
# the crystal length and the literature-typical walk-off angle ≈ 85 mrad.

# %%
LAMBDA_FUND_BBO = 559e-9

beta_BBO = beta_walkoff(
    rho_rad=RHO_BBO_TYPEI_AT_280_RAD,
    L_m=L_BBO_m,
    lam_m=LAMBDA_FUND_BBO,
    n=N_BBO_O_AT_559,
)
print(f"BBO walk-off parameter β = {beta_BBO:.2f}  (using ρ ≈ {RHO_BBO_TYPEI_AT_280_RAD * 1e3:.0f} mrad)")

# %% [markdown]
# With ρ ≈ 85 mrad the notebook's `beta_walkoff` convention gives β ≈ 18.4.
# At that β, the BK optimum sits at much smaller ξ than the no-walk-off case.
# Computing the σ-optimised optimum here is **slow** because each evaluation
# of `h_m_factor` runs a Brent search inside scipy `dblquad`. We therefore
# evaluate at a coarse grid of β values and find the optimum once for each.

# %%
# 5.1 Naive β=0 expectation, for comparison.
xi_opt_BBO_no_walkoff = xi_opt_LBO  # σ-optimum is the same for any β=0 case
w0_BBO_no_walkoff = waist_from_xi(
    xi_opt_BBO_no_walkoff, L_BBO_m, LAMBDA_FUND_BBO, N_BBO_O_AT_559
)
print(f"BBO σ-optimum (β=0):  ξ_opt = {xi_opt_BBO_no_walkoff:.2f},  "
      f"w0 = {w0_BBO_no_walkoff * 1e6:.2f} μm")

# 5.2 Where does the paper's reported w0 sit on the ξ axis?
xi_BBO_paper = L_BBO_m * LAMBDA_FUND_BBO / (
    2 * math.pi * N_BBO_O_AT_559 * w0_BBO_paper_m**2
)
print(f"BBO Friedenauer w0={w0_BBO_paper_m*1e6:.1f} μm  →  ξ = {xi_BBO_paper:.2f}")

# 5.3 Recompute the σ-optimised optimum *with* walk-off. SLOW (~ 1–2 minutes).
print("Computing β-dependent BK optimum (slow)...")
xi_opt_BBO_walkoff, h_max_BBO_walkoff = bk.h_m_optimum(
    beta=beta_BBO, kappa=0.0, mu=0.0, xi_bounds=(0.05, 4.0)
)
w0_BBO_walkoff = waist_from_xi(
    xi_opt_BBO_walkoff, L_BBO_m, LAMBDA_FUND_BBO, N_BBO_O_AT_559
)
print(f"BBO with β = {beta_BBO:.1f}:")
print(f"  ξ_opt = {xi_opt_BBO_walkoff:.3f}")
print(f"  h_max = {h_max_BBO_walkoff:.4f}")
print(f"  w0    = {w0_BBO_walkoff * 1e6:.2f} μm")
print(f"BBO paper-reported w0   = {w0_BBO_paper_m * 1e6:.2f} μm")

# %% [markdown]
# **Discrepancy between recomputation and paper.** Under the notebook's own
# β-convention `β = (ρ/2) √(L k₁)` with `k₁ = 2π n / λ`, the literature-cited
# walk-off (≈ 85 mrad → β ≈ 18.4) drives the optimum to a much looser focus
# than the paper's reported $w_0 = 19.4\,\mu\mathrm{m}$. Conversely, the
# paper's $w_0$ corresponds to $\xi \approx 1.42$; under this notebook's
# implementation that ξ matches a much smaller walk-off, β ≈ 0.55, i.e.
# ρ ≈ 2.5 mrad. (Earlier hand-estimates citing β ≈ 1.5–2 / ρ ≈ 7–9 mrad were
# read off Boyd–Kleinman 1968 Figure 6, which uses a slightly different
# convention; the values quoted here are what *this* notebook's implementation
# reproduces.)
#
# This is a real open question the dossier should resolve:
#
# 1. *Is our walk-off estimate (ρ ≈ 85 mrad) correct?* It is order-of-magnitude
#    only at this commit, pending Sellmeier-based recalculation cited in
#    `KD-UV280-005 Section C`.
# 2. *Did Friedenauer use a different optimization criterion?* For an enhancement
#    cavity rather than single-pass SHG, the figure of merit is conversion
#    efficiency *given the cavity buildup factor and round-trip losses*, not the
#    plain BK $h_m$. The optimum waist for a build-up cavity is generally tighter
#    than the single-pass BK optimum.
# 3. *Did the paper use a different B-convention?* Boyd–Kleinman 1968 itself,
#    and modern reviews, are inconsistent in factors of 2 in the definition of
#    $\beta$.
#
# The notebook records the discrepancy rather than papering over it. Resolving
# it is appropriate Phase 1 / Phase 3 work, not pre-G1 exploration.

# %%
# 5.4 Plot h_m(ξ) for several β values to visualise the walk-off shift.
print("Computing h_m curves at multiple β values (this takes a couple minutes)...")
xi_plot = np.linspace(0.2, 4.0, 18)
betas_to_plot = [0.0, 1.0, 2.0, 4.0, 8.0, beta_BBO]

fig, ax = plt.subplots(figsize=(8, 5))
for beta_val in betas_to_plot:
    h_curve = []
    for xi in xi_plot:
        try:
            h = bk.h_m_factor(xi=xi, beta=beta_val, kappa=0.0, mu=0.0)
        except Exception:
            h = np.nan
        h_curve.append(h)
    label = (f"$\\beta$ = {beta_val:.1f}"
             + (" (BBO, lit.)" if beta_val == beta_BBO else ""))
    ax.plot(xi_plot, h_curve, marker="o", ms=4, label=label)

# Mark the paper's BBO operating point on the axis.
ax.axvline(xi_BBO_paper, color="red", ls="--", lw=1, alpha=0.6,
           label=f"Friedenauer BBO at $\\xi$ = {xi_BBO_paper:.2f}")
ax.set_xlabel("$\\xi = L / b$")
ax.set_ylabel("$h_m(\\xi, \\beta)$ ($\\sigma$-optimised)")
ax.set_title("BBO 559 → 280 nm — BK $h_m(\\xi)$ for several walk-off parameters $\\beta$")
ax.legend(loc="upper right", fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()

# %% [markdown]
# ## 6. Sensitivity sketches
#
# Two cheap sensitivity views, useful for downstream Phase 3 simulation work
# once architecture-family selection is no longer G1-blocked.

# %%
# 6.1 LBO BK-optimum waist as a function of crystal length (β=0).
L_grid_LBO = np.linspace(5e-3, 30e-3, 25)
w0_grid_LBO = np.array([
    waist_from_xi(xi_opt_LBO, L, LAMBDA_FUND_LBO, N_LBO_AT_1118)
    for L in L_grid_LBO
])

fig, axs = plt.subplots(1, 2, figsize=(11, 4))

axs[0].plot(L_grid_LBO * 1e3, w0_grid_LBO * 1e6, lw=2)
axs[0].axvline(L_LBO_m * 1e3, color="C1", ls="--", lw=1, alpha=0.6,
               label=f"Friedenauer L = {L_LBO_m * 1e3:.0f} mm")
axs[0].axhline(w0_LBO_paper_m * 1e6, color="red", ls=":", lw=1, alpha=0.6,
               label=f"paper $w_0$ = {w0_LBO_paper_m * 1e6:.1f} μm")
axs[0].set_xlabel("LBO crystal length L (mm)")
axs[0].set_ylabel("BK-optimum $w_0$ (μm)")
axs[0].set_title("LBO σ-optimum waist vs. L (β = 0)")
axs[0].legend(fontsize=9)
axs[0].grid(alpha=0.3)

# 6.2 For BBO, plot w0 vs ρ (walk-off angle) at fixed L = 10 mm. SLOW; we use
# a small grid.
print("Computing BBO sensitivity to ρ (slow)...")
rho_grid = np.array([0.0, 0.005, 0.010, 0.020, 0.040, 0.060, 0.085])  # rad
w0_vs_rho = []
for rho in rho_grid:
    b = beta_walkoff(rho, L_BBO_m, LAMBDA_FUND_BBO, N_BBO_O_AT_559)
    if b == 0:
        xi_o = xi_opt_LBO
    else:
        xi_o, _ = bk.h_m_optimum(beta=b, kappa=0.0, mu=0.0,
                                 xi_bounds=(0.05, 5.0))
    w0_vs_rho.append(
        waist_from_xi(xi_o, L_BBO_m, LAMBDA_FUND_BBO, N_BBO_O_AT_559)
    )
w0_vs_rho = np.array(w0_vs_rho)

axs[1].plot(rho_grid * 1e3, w0_vs_rho * 1e6, marker="o", lw=2)
axs[1].axhline(w0_BBO_paper_m * 1e6, color="red", ls=":", lw=1, alpha=0.6,
               label=f"paper $w_0$ = {w0_BBO_paper_m * 1e6:.1f} μm")
axs[1].set_xlabel("BBO walk-off angle $\\rho$ (mrad)")
axs[1].set_ylabel("BK-optimum $w_0$ (μm) at L = 10 mm")
axs[1].set_title("BBO σ-optimum waist vs. ρ (L = 10 mm)")
axs[1].legend(fontsize=9)
axs[1].grid(alpha=0.3)

fig.tight_layout()

# %% [markdown]
# The right panel makes it explicit: with the literature-typical
# ρ ≈ 85 mrad the BK σ-optimised $w_0$ in this notebook's convention is
# ≈ 42 μm — a factor ≈ 2.17× larger than the paper's 19.4 μm. The paper's
# value matches the notebook's convention only at much smaller walk-off
# (ρ ≈ 2.5 mrad), far below published BBO Type-I walk-off angles at 280 nm.
# Most likely explanation: the paper's "BK-derived" optimum is for *the
# build-up cavity*, where the figure of merit is parametric conversion at the
# intracavity intensity for the given round-trip loss budget, and this
# naturally yields a tighter focus than single-pass BK. Resolving this is
# appropriate Phase 3 simulation work post-G1.

# %% [markdown]
# ## 7. Summary table
#
# | Stage | Quantity | Paper | Recomputed | Discrepancy |
# |---|---|---|---|---|
# | LBO 1118 → 559 | $w_0$ at BK σ-optimum | 27.3 μm | (computed below) | (computed below) |
# | BBO 559 → 280 (β = 0) | $w_0$ at BK σ-optimum | 19.4 μm | (computed below) | (computed below) |
# | BBO 559 → 280 (β ≈ 18.4) | $w_0$ at BK $\beta$-optimum | 19.4 μm | (computed below) | (computed below) |

# %%
print(f"{'Stage':<35} {'Paper (μm)':>12} {'Recomp. (μm)':>14} {'Δ (%)':>8}")
print("-" * 71)

print(f"{'LBO 1118→559, β=0':<35} "
      f"{w0_LBO_paper_m * 1e6:>12.2f} "
      f"{w0_LBO_recomputed * 1e6:>14.2f} "
      f"{(w0_LBO_recomputed - w0_LBO_paper_m) / w0_LBO_paper_m * 100:>+8.1f}")

print(f"{'BBO 559→280, β=0 (no walk-off)':<35} "
      f"{w0_BBO_paper_m * 1e6:>12.2f} "
      f"{w0_BBO_no_walkoff * 1e6:>14.2f} "
      f"{(w0_BBO_no_walkoff - w0_BBO_paper_m) / w0_BBO_paper_m * 100:>+8.1f}")

print(f"{'BBO 559→280, β≈18.4 (lit. walk-off)':<35} "
      f"{w0_BBO_paper_m * 1e6:>12.2f} "
      f"{w0_BBO_walkoff * 1e6:>14.2f} "
      f"{(w0_BBO_walkoff - w0_BBO_paper_m) / w0_BBO_paper_m * 100:>+8.1f}")

# %% [markdown]
# ## 8. Open questions / data gaps surfaced by this notebook
#
# 1. **Sellmeier coefficients for LBO at 1118 nm** — needed to lock $n_\mathrm{LBO}$
#    beyond the order-of-magnitude figure used here. Belongs in
#    `KD-UV280-007 Section C` with citation.
# 2. **Sellmeier coefficients and walk-off for BBO at 559 → 280 nm Type-I** — the
#    walk-off-vs-PM-angle relation is the binding uncertainty for the BBO BK
#    analysis. Belongs in `KD-UV280-005 Section C`.
# 3. **Cavity mirror radii of curvature (LBO and BBO ring cavities)** — missing
#    from the YAML extraction at this commit, but partly recoverable from the
#    paper itself: Friedenauer 2006 reports e.g. f = 25 mm for the LBO cavity's
#    curved focusing mirrors. Re-reading §3 / Table 1 to add these to
#    `extracted.yaml` is straightforward and unblocks
#    `src.abcd.cavity_eigenmode_q` against this geometry.
# 4. **Friedenauer's BK criterion for BBO** — single-pass BK with literature ρ
#    over-predicts the optimum waist by a factor ≈ 2.17 (recomputed 42 μm vs
#    paper's 19.4 μm). Likely the paper used a cavity-specific figure of merit.
#    Resolving this is post-G1 Phase 3 simulation work; not blocking pre-G1
#    progress.
# 5. **`d_eff` for both crystals** — needed for any conversion-efficiency
#    recomputation. Belongs in `KD-UV280-005` and `KD-UV280-007 Section C`.
#
# **Promotion guard.** None of this notebook's logic is suitable for promotion
# to `/src/` without first (a) cleaning up the cited-literature constants into a
# proper `crystals/` module that is itself architecture-neutral, and
# (b) verifying that the calculations compose cleanly with the Phase 3
# simulation framework once G1 has closed. Until then, the file remains
# `pre-G1, exploratory, not promoted`.

# %%
plt.show()
