# Numerical foundations — RC-01 / RC-05, with RC-02 decision inputs

**Date:** 2026-09-09  
**Steward:** Ulrich Warring  
**Baseline:** `9a498165532e029e1ba0706d380f760402dd7584`  
**Status:** Generic corrections implemented and tested; D1 evidence filed for review. RC-02/D2 and the wider RC-07 impact assessment remain open.  
**Task:** [Repository review card](2026-09-09-repository-review-task-card.md).

## Charter §9 trigger questions

- **Affects Level 0 parameters?** No: locked parameters and Raman values are unchanged.
- **Affects Level 1 parameters?** No binding requirement is amended. Revised SHG calculations require a later impact assessment before changing coating targets.
- **Affects success criteria?** No.
- **Changes Charter text or gate state?** No.

## RC-01: conventions and independent calculations

For the centred, lossless case, [Daniel, Tsai & Hemmerling (2020), Eqs. (1)–(3)](https://arxiv.org/abs/2009.08430) give

$$
P_2=K L k_1 h P_1^2,\qquad
K=\frac{2\omega_1^2 d_{\rm eff}^2}{\pi\epsilon_0c^3 n_1^2 n_2},
\quad k_1=2\pi n_1/\lambda_{\rm vac},\quad b=k_1w_0^2,
$$

and, with $\xi=L/b$, $B=\rho\sqrt{Lk_1}/2$, $\sigma=b(2k_1-k_2)/2$,

$$
h=\frac{1}{4\xi}\int_{-\xi}^{\xi}\!\int_{-\xi}^{\xi}
\frac{e^{i\sigma(\tau-\tau')}e^{-B^2(\tau-\tau')^2/\xi}}
{(1+i\tau)(1-i\tau')}\,d\tau\,d\tau'.
$$

The old code omitted `/xi` in the walk-off exponential and one `n_omega`
in K's denominator. Since Lk₁ is dimensionless, **K has units W⁻¹**.
The production code now evaluates the reduced one-dimensional Eq. (3).
The [independent reference](../scripts/review/shg_reference.py) instead uses
tensor Gauss–Legendre quadrature of Eq. (2), without importing production BK code.
Six comparisons span ξ=0.2–4 and B=0–18.0166. Refining 256×256 to 512×512
nodes and comparing the two methods gives relative differences below 10⁻¹²
in this set; regression tolerances are 2×10⁻⁸ relative / 10⁻¹⁰ absolute.
This establishes convergence at these inputs, not every possible input.

**Independent absolute normalization:** the test integrates the generated
plane-wave intensity radially over a weakly focused Gaussian pump. Using
physical peak fields, $I_j=n_j\epsilon_0c|E_j|^2/2$ and the undepleted
coupled-wave equation $dE_2/dz=i\omega_1d_{\rm eff}E_1^2/(n_2c)$, the
Gaussian intensity $I_1(r)=2P_1e^{-2r^2/w_0^2}/(\pi w_0^2)$ gives

$$
P_2/P_1^2\longrightarrow
\frac{2\omega_1^2d_{\rm eff}^2L^2}{\pi\epsilon_0c^3n_1^2n_2w_0^2}.
$$

The regression obtains this through numerical radial integration and compares
it with the public γ function at small ξ, for two different index pairs.
It does not call K to construct its expected answer (relative tolerance 10⁻⁹).
This is an undepleted, paraxial model with a fixed Gaussian pump.
The effective tanh² depletion law is not an exact focused-propagation solution.

### Absorption and focus position

The following is an explicit extension of the cited lossless integral, derived
here; Daniel et al. do not supply this absorbing-crystal formula. Let
`s=z/L`, `mu=2*z_focus/L-1`, and let α₁, α₂ be **intensity** absorption
coefficients. Then

$$
\tau(s)=2\xi s-\xi(1+\mu),\qquad
A(s)=\exp[-(\alpha_1L)s-(\alpha_2L)(1-s)/2].
$$

The pump field decays as exp(−α₁z/2), so its squared field in the SHG source
decays as exp(−α₁z). Harmonic amplitude created at z then decays by
exp[−α₂(L−z)/2] before the exit. Multiply the lossless pair kernel by
A(s)A(s′) and integrate over s,s′∈[0,1], with normalization ξ.
Input power is at the entrance; output harmonic power is at the exit.
This also fixes the sign of the old focus-offset integration limits.

A single sum `(alpha1 + alpha2/2)*L/2` cannot recover both propagation weights.
The new keyword arguments are `alpha_omega_L=alpha1*L` and
`alpha_2omega_L=alpha2*L`. **Nonzero legacy `kappa` now raises ValueError**
with migration guidance; zero remains accepted. No production notebook in this
repository supplies nonzero κ. This is an intentional API restriction, not a
silent interpretation of ambiguous caller data.

Three weak-focus limits check pump-only, harmonic-only and α₁=α₂/2 absorption.
For $a=\alpha_1L-\alpha_2L/2$,

$$
\lim_{\xi\to0}h/\xi=
\left[e^{-\alpha_2L/2}(1-e^{-a})/a\right]^2,
$$

with the continuous a=0 limit. Four additional tests solve the complex
propagation ODE directly,

$$
q'(s)=\frac{e^{-\alpha_1Ls+i\sigma\tau(s)}}{1+i\tau(s)}
-\frac{\alpha_2L}{2}q(s),\quad q(0)=0,\quad h=\xi|q(1)|^2,
$$

for positive/negative focus offsets and separate pump/harmonic absorption.
ODE tolerances are 10⁻¹¹ relative / 10⁻¹³ absolute; agreement is tested at
2×10⁻⁹ relative. These ODE comparisons use B=0; lossless nonzero B is checked
separately by tensor quadrature.

### Phase optimization and diagnostic results

`sigma_bracket` now means strict finite bounds. The implementation samples
at least eight points per π/ξ phase lobe (at least 33 total), refines each
sampled local maximum, and compares the endpoints. Four cases are checked
against an independent 481-point tensor-quadrature scan over [−6,6], including
zero and strong walk-off. A narrow interval whose maximum is an endpoint is
also tested. This is evidence for the numerical search in the tested regime,
not a proof of a global maximum for arbitrary bounds. `h_m_optimum` remains a
bounded local search in ξ, assumes one focus maximum, and checks both endpoints.

| Diagnostic | Filed baseline | Corrected |
|---|---:|---:|
| hₘ at ξ=1.41317, B=18.0166 | 0.03304954854 | 0.03924301048 |
| Independent 512×512 tensor hₘ | — | 0.03924301048 |
| ξ optimum at that B | not re-evaluated here | 1.42111651 |
| Waist optimum, L=10 mm, λ=559 nm, n₁=1.67276 | not re-evaluated here | 19.3456938 µm |
| Combined γ correction at fixed inputs | 1 | 0.709844383 |

The index is the ordinary BBO index at vacuum 559 nm from Eimerl (1987),
Eq. (1)/Table II(a), transcribed in the [draft extraction](../data/literature/Eimerl1987/extracted.yaml).
Digits reproduce the existing diagnostic input, not measurement precision.
The γ ratio uses the recomputed baseline hₘ; it differs slightly from the
card's 0.7098345 estimate, which used rounded 0.033050 and 0.039243.
This resolves the normalization direction at fixed inputs. It does **not**
settle the direction of a refitted cavity loss or a revised coating target.

## RC-05: continuous model and physical brackets

`auto` now evaluates tanh² at all powers. Explicit `small` remains γP²,
clearly documented as an unbounded approximation valid for γP≪1. Invalid
regimes and negative/nonfinite inputs are rejected even on zero-input paths.

At impedance match, Pc=Pin/T. Substituting into the matching equation gives

$$
f(T)=T-L-(1-L)\tanh^2\sqrt{\gamma P_{\rm in}/T}=0.
$$

f increases with T, f(L)≤0 and f(1)≥0; at L=T=0 use the right-hand limit −1
for positive γPin. Exact bounds [L,1] replace artificial offsets that excluded
the passive-limit root. Zero-pump/zero-γ paths return L. Saturation may round
the answer to one. The circulating-power solver uses the passive field
buildup, rounded outward by eight machine epsilons to retain the bracket
at vanishing nonlinear loss, as an upper bound and solves in sqrt(Pc/Pin), avoiding a fixed absolute
tolerance in watts. Rationalizing `1-sqrt(survival)` avoids cancellation at
tiny transmission/loss. Brent uses relative tolerance 10⁻¹² and the smallest
positive float as its absolute tolerance.

| Regression | Before | After |
|---|---|---|
| Pin=10⁻⁸ W, L=0.01, γ=10⁻⁴ W⁻¹ | bracket failure | T=0.010000000099 |
| η(auto), γP=0.049999 / 0.05 | 0.049999 / 0.04837935515 | 0.04837841908 / 0.04837935515 |
| Relative jump using the review's samples | 3.3478% downward | smooth increase |
| Explicit small-signal P=2 W, γ=1 W⁻¹ | 4 W despite bounded docstring | 4 W, explicitly outside approximation validity |

The cavity model references Pc before conversion and applies passive loss
afterward; complete harmonic extraction is assumed. At match,
`Pin = Ph + L*(Pc-Ph)`. Off match, reflected power completes the same balance.
The old test used L*Pc and a loose 0.5% tolerance. The new checks include
reflection, use 3×10⁻¹² relative tolerance, and remove the output clamp.
A computed Ph can exceed Pin by numerical roundoff of order the root tolerance;
no physically significant excess is accepted by the tests.

## RC-02: inputs for D2, without changing locked values

Write δ=Δ/(2π) and f_R=Ω_R/(2π), both in Hz. Γ is the population decay
rate in s⁻¹, with the draft's Γ/(2π)=41 MHz. The draft's simplified relation is

$$
\Gamma_{sc}=\Gamma\Omega_R/(2\Delta)=\Gamma f_R/(2\delta),\quad
 t_\pi=1/(2f_R),\quad N_{sc}=\Gamma/(4\delta).
$$

Only Ω_R/Δ changes frequency convention together; Γ remains the physical
decay rate. For the ideal, far-detuned equal-coupling Λ model, the eliminated
excited amplitude is proportional to `(Ω/(2Δ))*(c1+c2)`. On a resonant π
rotation starting in one ground state, c1=cos(Ω_R t/2), c2=−i sin(Ω_R t/2),
so |c1+c2|²=1 and Γ times the excited population gives the printed rate.
This conditional derivation does not establish the Mg⁺ Clebsch–Gordan factors,
polarization, multiple excited-state paths, branching or an actual gate error.

| Scenario | Printed-model rate (s⁻¹) | Recorded rate (s⁻¹) | Recorded/model | Model events/π pulse |
|---|---:|---:|---:|---:|
| Conservative | 161.0066235 | 2,500 | 15.5273115 | 0.0008050331 |
| Nominal | 1,288.052988 | 20,000 | 15.5273115 | 0.0016100662 |
| Aggressive | 8,587.019920 | 110,000 | 12.8100320 | 0.0042935100 |

The intensity convention also matters: a Gaussian beam with 1/e² intensity
radius w₀ has on-axis intensity **2P/(πw₀²)**. At fixed P this doubles the
single-level Ω_R relative to the draft's P/(πw₀²) convention, but does not
change the rate above at fixed target Ω_R and Δ. It cannot explain the split
recorded/model ratios.

D2 must choose prediction, upper limit or allowance for each recorded rate,
with its original rationale. If a prediction, replace it only after accepting
the atomic model and applicable §9 disposition. If a limit, preserve its
meaning and test an inequality; if an allowance, record scenario-specific
margins and their justification. No interpretation is selected here.

## Validation, outputs and remaining work

Baseline: Python 3.13.7 / NumPy 2.4.4 / SciPy 1.17.1 / pytest 9.0.3,
**142 tests passed**. A fresh `.venv` was then installed from the project's
`test,dev,notebooks` extras. Corrected full suite: **252 tests passed**,
**96.18% coverage including branches**. Resolved environment: Python 3.13.7,
NumPy 2.5.3, SciPy 1.18.1, pytest 9.1.1, recorded in
[environment.txt](../data/review/2026-09-09/environment.txt).
This snapshot supports reproducing this check; it does not select D5's
cross-platform support policy or complete RC-06's lockfile/CI work.

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r data/review/2026-09-09/environment.txt
.venv/bin/python -m pip install --no-deps -e .
.venv/bin/python -m pytest --cov=src --cov-report=term-missing -q
.venv/bin/python -m scripts.review.verify_numerical_foundations
.venv/bin/python scripts/render_tutorials.py
.venv/bin/python -m scripts.review.tutorial_manifest
```

The [numerical manifest](../data/review/2026-09-09/numerical-foundations.json)
records baseline revision, exact input hashes, conventions, environment and
unrounded results. Source and manifest are committed together; no uncommitted
input patch is required. The retained baseline comparison needs Git history
containing `9a49816`. Black/isort checks cover the three changed numerical
modules, their three test files, the renderer and review scripts. Ruff covers
the same paths with `N802` excepted for existing unit-bearing function names
such as `harmonic_output_W`; this is a scoped check, not a repository-wide
lint/type-cleanup claim. Type, schema, full link and CI checks remain RC-06/09.

All four tutorial pairs are regenerated. The renderer now creates a temporary
kernelspec using its own interpreter rather than a potentially unrelated user
`python3` kernel. Tutorial 1 corrects K's equation/units, distinguishes the
σ=0 analytic limit from optimized hₘ, and removes the auto-switch claim.
The [tutorial manifest](../data/review/2026-09-09/tutorials.json) maps source,
parameters, renderer, numerical modules, environment and all eight outputs,
with before/after printed numerical results. The first repeat-render check
failed: invalid Python string escapes produced warnings containing temporary
kernel paths. The source math-label strings are corrected (warnings are not
filtered). Inspection also found that the baseline notebooks contained **no
embedded plot outputs**: the renderer forced plain Agg. It now selects the
headless inline backend so the tutorial figures are actually included.
There is consequently no baseline rendered image for a pixel comparison.
All **eight figures** were inspected. The final unchanged repeat render produced
**zero differences across all eight HTML/notebook outputs**, checking both the
filename set and content hashes (including newly generated files). No warning
or error outputs remain in the executed notebooks. This verifies the artifacts,
not the full Jekyll site layout in a browser.

The calculations page now identifies the ≈42 µm interpretation as superseded.
The historical May notebook narratives, cascade/loss fits, IC sweep, coating
work package and uncertainty bands still require RC-07 recalculation and
impact assessment. Existing May specifications remain historical procurement
records; the 22 received Agile mirrors are not reclassified by a model change.
