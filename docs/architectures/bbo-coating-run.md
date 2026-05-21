---
layout: default
title: "BBO coating run — 559 → 280 nm CW SHG, rationale and calculations"
description: "Public-facing explainer for the 2026-05-20 coating-run work program: how a re-anchored impedance-match calculation against the Friedenauer 2006 baseline showed that the published M1' input coupler sits ~ 0.6 percentage points below the impedance-matched optimum at the published operating point, forfeiting ~ 3.6 % UV buildup, and how that motivated a new four-mirror coating-spec package for the next-generation BBO ring at 559 → 280 nm. Intended audience: trapped-ion / atomic-physics builders running Friedenauer-class CW SHG cavities."
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page explains a closed coating-run procurement work program: a vendor-facing spec package for the BBO ring of the next-generation ²⁵Mg⁺ UV source. Quantitative findings are anchored to the published Friedenauer 2006 reference and to the architecture-neutral numerics in <code>/src/</code>; LIDT claims are dossier-tier honest (Section 6 below).</p>

<p class="eyebrow">Architecture · BBO ring coating-run</p>

# BBO coating run for a 559 → 280 nm CW SHG ring cavity

A four-mirror Brewster-cut-BBO bowtie ring of the kind that
[Friedenauer et al. (2006)][Friedenauer2006] built to produce ~ 0.275 W
at 280 nm for ²⁵Mg⁺ detection, cooling, and Raman work, re-evaluated for
a coating-class upgrade twenty years on.

The work program ran from BC-A through BC-F (six internal phases:
*scope / impedance match / per-mirror allocation / damage threshold /
spec sheets / freeze*) in a single calendar day on
2026-05-20 ([phase log index][closure]) and closed with a
[five-page vendor-ready spec package][specs] covering M1' / M2' / M3' /
M4' plus a cover letter. **This page is not the spec sheet** — those are
the linked-procurement artefacts. This page explains *why the spec is
what it is*, with the math, the dossier evidence, and the honest
uncertainty inventory.

---

## Concepts for newcomers

If you are new to cavity-enhanced second-harmonic generation, the
following one-paragraph primers should be enough to read the rest of
the page. Builders already familiar with the topic can skip to the
TL;DR.

**Why ²⁵Mg⁺ needs 280 nm UV.** The ²⁵Mg⁺ ion's strong dipole-allowed
cooling and detection transitions sit at ~ 280 nm. Cooling, optical
pumping, and Raman manipulation of trapped Mg⁺ all need CW
(continuous-wave, i.e., not pulsed) laser light at this wavelength,
with hundreds of milliwatts on the experiment.

**Second-harmonic generation (SHG) in a nonlinear crystal.** Optical
materials lacking inversion symmetry can convert two input photons at
ω into one output photon at 2ω. β-barium borate (BBO, formula
β-BaB₂O₄) is the workhorse crystal at our wavelengths: it converts
559 nm (visible green-yellow) into 280 nm (deep UV). The conversion
efficiency depends on the input intensity, the crystal length, the
focusing geometry, the phase-matching angle, and the effective
nonlinear coefficient `d_eff` of the crystal cut.

**Cavity-enhanced SHG, and why one builds a ring.** At a few-watt CW
pump (here 559 nm) the single-pass SHG conversion through a 10-mm
BBO crystal is only a fraction of a percent. To get watt-class UV
out, the build-up trick is to embed the crystal inside a low-loss
resonator that recirculates the unconverted fundamental. The
intracavity power grows by a factor up to `1 / L_total` (the inverse
of the round-trip loss), so a 1-W input plus 1 % loss can give
~ 50 W circulating — enough that the per-pass conversion delivers
hundreds of mW of UV. A *bowtie ring* is one of the standard
geometries: four mirrors arranged in a figure-eight shape (two flat
mirrors on a long arm, two curved focusing mirrors at a short-arm
waist where the crystal sits), used because the unidirectional travel
prevents standing-wave artefacts in the crystal.

**Impedance matching (what `T_IC` does).** The input coupler (`IC`,
labelled M1' in this paper's geometry) is a partial reflector with
transmission `T_IC`. If `T_IC` is too small, most of the pump bounces
back off the cavity and never enters; if `T_IC` is too large, the
cavity has no buildup. The optimum is **`T_IC` = round-trip loss the
cavity actually consumes** (mirror absorption + scatter + crystal
losses + nonlinear conversion). This is the *impedance match*. Real
SHG cavities have a *nonlinear* contribution to round-trip loss
(the SHG itself removes fundamental photons), so the optimal `T_IC`
grows with input power.

**Boyd-Kleinman focusing.** How tightly to focus a Gaussian beam into
a nonlinear crystal? Too loose and the intensity is too low for
efficient conversion; too tight and the beam diverges out of the
phase-matched volume before converting. Boyd & Kleinman (1968)
worked out the optimum and packaged it into a focusing factor
`h_m(ξ, β)` where `ξ = L / b` is the ratio of crystal length to
confocal parameter `b = π · n · w₀² / λ`. For BBO Type-I at our
wavelengths there is an additional walk-off effect (the
extraordinary harmonic beam exits the crystal at a small angle to
the ordinary fundamental), which makes `h_m` substantially smaller
than the no-walk-off optimum.

**Hänsch–Couillaud locking.** The cavity must be held on resonance
with the input laser to a tiny fraction of the line-width. The
Hänsch–Couillaud (HC) scheme generates an error signal from the
polarisation of the cavity-reflected light: any frequency mismatch
rotates the reflected polarisation away from horizontal, and a
balanced photodiode pair measures the offset. The error feeds a
piezo-mounted cavity mirror (here M2', the second plane mirror) that
adjusts the cavity length on the sub-nanometre scale.

**Mirror coatings and damage thresholds (LIDT).** Each mirror in the
ring carries a dielectric thin-film stack tens of layers deep: a
high-reflector (HR) is a quarter-wave stack alternating high-index
material (HfO₂, ZrO₂, Ta₂O₅, …) with low-index SiO₂; an
anti-reflection (AR) coating suppresses the back-face reflection; the
M4' dichroic in our build is a dual-band stack that simultaneously
high-reflects the 559 nm fundamental and high-transmits the 280 nm
harmonic. The Laser-Induced Damage Threshold (LIDT) is the peak
intensity at which the coating begins to fail; for CW use it is
typically expressed in kW/cm² and is set by the coating-material
bandgap, the deposition method (Ion-Beam Sputtering, IBS, is the
gold standard), and particulate contamination (which can drop the
LIDT by orders of magnitude). The new build's spec sheets explicitly
specify CW LIDT and a cleanroom-grade cleanliness clause on
delivery.

A more compact glossary of every abbreviation and symbol used on
this page sits in [Section 10](#10--glossary-of-abbreviations-and-symbols).

---

## TL;DR for the busy ion trapper

(*TL;DR* = "too long, didn't read" — the headline summary.)

1. **Friedenauer's published M1' input coupler had `R = 0.984`
   (`T_IC = 0.016 = 1.6 %`).** Re-running the published operating
   point through the architecture-neutral cavity solver in
   [`src/enhancement_cavity.py`][enhancement_cavity] with the
   Phase-E-validated `γ_SHG_BBO ≈ 1.49 × 10⁻⁴ W⁻¹` and the
   forward-solved `L_passive_PHE ≈ 1.53 %` reproduces the published
   `P_UV = 0.275 W` exactly *and* puts the impedance-matched optimum at
   **`T_IC_opt ≈ 0.0217 = 2.17 %`** — about **+0.57 pp above the
   procured T_IC**. Operating off the optimum costs **~ 3.6 % UV
   buildup** (`P_UV(T_IC_opt) − P_UV(T_IC) ≈ 0.285 − 0.275 W`).
2. **The new build picks T_IC at the optimum**, with one M1' coating
   centred at the equal-penalty (minimax) point between two upstream
   scenarios (0.5 W and 1.5 W of 559 nm into the BBO ring):
   **`T_IC = 19 965 ± 500 ppm = 2.00 % ± 0.05 %`**.
3. **Loss budget on M2'/M3'/M4'** preserves Friedenauer's published
   ~ 3:1 dichroic-vs-HR ratio, scaled down to a 1 500 ppm summed
   mirror-loss target → **R ≥ 99.970 % @ 559 nm on M2' and M3'**,
   **R ≥ 99.910 % @ 559 nm + T ≥ 95 % @ 280 nm on the M4' dichroic**.
4. **Material recommendation for M4' dichroic stack:** IBS-deposited
   **HfO₂ / SiO₂** default, **ZrO₂ / SiO₂** acceptable alternative,
   **LaF₃ / MgF₂ on CaF₂** as the fluoride-class upgrade option;
   **Nb₂O₅ and TiO₂ excluded** on bandgap grounds.
5. **The 280 nm axis is the binding LIDT case** but not a margin —
   our M4' transit fluence sits ~ 1.15 × *above* the
   [Kondo / Kubota (1998)][Kondo1998] 1 000-hour CW UV operating point
   on bulk BBO. Service-life expectation is *order-of-magnitude match*
   to that benchmark, G2-conditional pending the new build's M4'
   loss-rate measurement under operation.

If any of these statements is surprising, the section it lives in
below carries the underlying calculation.

---

## 1 · The cavity in 30 seconds

Friedenauer's BBO ring ([§3, Table 1 of the 2006 paper][Friedenauer2006])
is a four-mirror bowtie with:

- Two **plane** mirrors on the long arm: input coupler **M1'**
  (R = 0.984 @ 559 nm) and a piezo-mounted high-reflector **M2'**
  (R > 0.9993 @ 559 nm) carrying the Hänsch–Couillaud servo seat.
- Two **concave focusing** mirrors at the short-arm waist:
  high-reflector **M3'** and the dichroic output coupler **M4'**
  (R > 0.998 @ 559 nm + T > 0.94 @ 280 nm), both with focal length
  f = 25 mm (ROC = 50 mm).
- A Brewster-cut Type-I BBO crystal, 4 × 4 × 10 mm³, at θ ≈ 44.4°
  Sellmeier-derived phase-matching angle, oven-temperature-stabilised
  at ~ 50 °C.
- Full folding angle 27.4° (13.7° per curved mirror); focusing-mirror
  separation `d' = 59.4 mm`; total cavity length `L_cav = 0.470 m`.

The 559 nm fundamental builds up inside the ring; second-harmonic
generation in the BBO crystal at the short-arm waist (w₀ = 19.4 μm) drives
the 280 nm output through the dichroic M4'. Locking is Hänsch–Couillaud
on the polarisation rotation of the 559 nm leakage through M2'.

The cavity *fundamentally* obeys the steady-state buildup relation

```
P_circ / P_in = T_IC / (1 − √[(1 − T_IC)(1 − L_passive)(1 − η_nl)])²
```

with `L_passive` the round-trip passive loss (everything except the
input-coupler transmission) and `η_nl(P_circ)` the single-pass
nonlinear conversion fraction. The **exact** depleted-regime form is

```
η_nl(P_circ) = tanh²(√[γ_SHG · P_circ])
```

(reducing to the small-signal approximation `η_nl ≈ γ_SHG · P_circ`
when `γ_SHG · P_circ ≪ 1`). The exact impedance-matched coupling is

```
T_IC_opt = L_passive + (1 − L_passive) · η_nl(P_circ(T_IC_opt))
```

solved self-consistently. In the small-signal limit this reduces to
`T_IC_opt ≈ L_passive + η_nl`, and in the high-pump limit to
`T_IC_opt → √[(1 − L_passive) γ_SHG P_in]`. Both the buildup relation
and the impedance-match solver consume the **exact tanh² form** of
η_nl, not the small-signal approximation, and are implemented in
[`src/enhancement_cavity.py`][enhancement_cavity] with no architecture
or wavelength preset — references [Polzik & Kimble (1991)][PolzikKimble1991]
and [Ashkin, Boyd & Dziedzic (1966)][Ashkin1966].

---

## 2 · The Boyd–Kleinman factor and γ_SHG at the Friedenauer geometry

The single-pass conversion coefficient `γ_SHG` follows the standard
[Boyd & Kleinman (1968)][BoydKleinman1968] result for a focused Gaussian
beam in a Type-I crystal:

```
γ_SHG = (2 ω² d_eff² L) / (π ε₀ c³ n_ω² n_2ω) · h_m(ξ, β)
```

where `ξ = L / b` is the focusing parameter (L = crystal length,
b = confocal parameter = π n w₀² / λ), `β = (ρ/2) √(L k)` is the
walk-off parameter (ρ = walk-off angle in radians), and `h_m(ξ, β)` is
the Boyd–Kleinman focusing factor maximised over the phase mismatch.

For Friedenauer's BBO geometry at 559 → 280 nm:

| Quantity | Value | Source |
|---|---|---|
| Crystal length L | 10 mm | [Friedenauer2006][Friedenauer2006] |
| Intracavity waist w₀ at BBO centre | 19.4 μm | [Friedenauer2006][Friedenauer2006] |
| `n_o(559 nm)` BBO | 1.67276 | [Eimerl1987][Eimerl1987] |
| `d_eff` BBO Type-I at 559 → 280 nm | 1.44 pm/V (central; range 1.30–1.60) | [Eckardt1990][Eckardt1990] |
| Walk-off ρ at θ_PM | 83.1 mrad | [Eimerl1987][Eimerl1987] |
| **Focusing parameter ξ** | 1.413 | computed |
| **Walk-off parameter β** | 18.0 | computed (deeply walk-off-limited) |
| **Boyd–Kleinman factor h_m** | 0.0330 | computed via [`src/boyd_kleinman.py`][bk] |
| **γ_SHG (central)** | **1.4914 × 10⁻⁴ W⁻¹** | this WP, BC-A |

The d_eff bracket from Eckardt (1.30–1.60 pm/V) is the dominant
γ-uncertainty axis and propagates through every downstream number on
this page. The Eimerl–[Tamosauskas2018][Tamosauskas2018] Sellmeier
cross-check on n and ρ agrees to < 1 % and is sub-dominant.

---

## 3 · Reproducing Friedenauer's 0.275 W UV — and finding the 3.6 % buildup gap

Friedenauer published three numbers for the BBO stage:

| Symbol | Value | From |
|---|---|---|
| P_in (559 nm into the BBO ring) | 0.95 W | [Table 1][Friedenauer2006] |
| T_IC | 1 − R = 1 − 0.984 = 0.016 | §3 |
| P_UV (280 nm output) | 0.275 W | Abstract / §3 |

With γ_SHG pinned above, the only remaining unknown is the round-trip
passive loss `L_passive`. Forward-solving the cavity equation for the
`L_passive` that reproduces P_UV = 0.275 W gives:

```
L_passive_PHE = 15 288 ppm ≈ 1.53 %
```

(`PHE` = Phase E, the diagnostic notebook [`2026-05-07-friedenauer-cascade-recompute.py`][PhaseE]
that first cross-checked this number to 1.5 % agreement.) This is
larger than the sum of Friedenauer's published mirror R-floors:

```
Σ T_loss(M2' + M3' + M4' at the published lower-bound R-floors)
  = (1 − 0.9993) + (1 − 0.9993) + (1 − 0.998)
  ≈ 3 400 ppm  (≈ 0.34 %)
```

The ~ 11 900 ppm gap is the **non-mirror passive loss**: BBO Brewster-face
scatter, BBO bulk absorption at 559 nm, oven-window AR, and scatter
floors. We hold this contribution fixed in the new build under the
assumption that the new crystal class (Raicol 2025 Brewster-cut BBO,
same dimensions, same oven design) inherits the Friedenauer non-mirror
loss budget.

**Now the headline.** At `(P_in = 0.95 W, L_passive = 1.53 %,
γ_SHG = 1.4914 × 10⁻⁴ W⁻¹)`, the cavity solver returns the
impedance-matched optimum

```
T_IC_opt = 0.0217 = 2.17 %
```

— that is, **0.57 percentage points above Friedenauer's procured
T_IC = 0.016**. Running the cavity *at* that optimum (rather than at
the procured T_IC) gives P_UV = 0.285 W, i.e., **about 3.6 % more
280 nm output** than what Friedenauer actually achieved.

This is not an error in the 2006 paper. It is exactly what one would
expect from a 20-year-old build: Friedenauer ordered the closest
catalog R available to a cavity model that was an *under*-coupling
estimate, and accepted the few-percent buildup penalty. Modern IBS
coating houses can target the impedance-matched optimum to ± 500 ppm
absolute, recovering the buildup left on the table.

The full BC-B forward cross-check sits in
[`bc-b-results.md`][bc-b-results] and is implemented in the BC-B
notebook [`2026-05-20-bbo-ic-impedance-match.py`][BC-B-notebook]
(promoted to `/notebooks/exploration/` at WP closure).

---

## 4 · Two upstream scenarios, one M1' coating

The new build's upstream LBO stage is being separately re-evaluated in
the [next-generation 500 mW workplan][next-gen]; its 559 nm output is
not yet fixed, and plausibly lands anywhere between ~ 0.5 W
(Friedenauer baseline kept; conservative) and ~ 1.5 W (LBO at 1.5 ×
Friedenauer, with a higher-power Yb pump and re-optimised IC). The
optimal T_IC differs between the two scenarios because nonlinear
depletion `η_nl` scales with P_in:

| Scenario | P_in (559 nm into BBO ring) | T_IC_opt |
|---|---|---|
| Low | 0.50 W | **17 565 ppm (1.756 %)** |
| Friedenauer corner | 0.95 W | 21 690 ppm (2.169 %) |
| High | 1.50 W | **22 945 ppm (2.295 %)** |

(Same γ_SHG, same L_passive_PHE; only P_in changes.) The Δ`T_IC_opt`
between the two scenarios is **+0.54 pp absolute** (≈ 5 400 ppm).
This is **below the project's 1 pp branch-rule threshold** for going
to two coating variants (the workplan's §6 Q2 default rule), so a
single M1' coating variant is acceptable under the rule — *not*
because the two optima fall inside any one vendor-tolerance band.
The vendor manufacturing tolerance on the chosen centre is
**±500 ppm = ±0.05 pp**, much tighter than the 5 400-ppm spread
between the optima; the one-variant choice is therefore a
**performance-acceptable** decision (acceptable UV penalty at the
centre point), not a coverage decision.

**The equal-penalty (minimax) centre.** A single coating sitting at
some centre `T_C` between the two optima delivers less than the
optimum P_UV in *both* scenarios. The Low scenario has a sharper
impedance-match peak (lower depletion makes the optimum narrower), so
biasing toward Low's optimum saves more buildup than the corresponding
shift away from High's costs. The equal-penalty centre — where both
scenarios pay the same fractional UV penalty — therefore sits *below*
the geometric / arithmetic mean of the two optima:

```
Equal-penalty centre:    T_IC = 19 965 ppm = 2.00 %
Low scenario penalty:    −0.68 % UV vs Low's optimum
High scenario penalty:   −0.68 % UV vs High's optimum
```

With a ±500 ppm vendor manufacturing tolerance on this centre, the
worst-case penalty across the band stays below ~ 1 % UV in either
scenario.

**Where the new centre wins, and where the comparison is more subtle.**
At the High scenario (1.5 W) and at the Friedenauer historical point
(0.95 W) the new centre is much closer to the relevant optimum than
Friedenauer's `T_IC = 0.016` would be — at 1.5 W the gain is large
(centre penalty −0.68 % vs −4.33 % for the old T at the new build's
loss budget). At the **Low scenario specifically, however, the old
T = 0.016 coincidentally lands slightly closer to the Low optimum
(17 565 ppm) than the equal-penalty centre does** — at the new build's
default loss the old coating would pay −0.35 % at Low while the
centre pays −0.68 %. The equal-penalty centre is therefore the
**minimax (worst-case-minimising) choice across the two scenarios**,
not the everywhere-better choice. The win that *does* hold uniformly
is on the High side and at the Friedenauer historical operating
point.

---

## 5 · Per-mirror loss-budget allocation — Friedenauer's 3:1 dichroic ratio scaled

The BC-A loss decomposition (Section 3) inherits the non-mirror passive
loss from Friedenauer; the *mirror* loss-budget is what the new
coating run actually buys. We size the **summed** mirror ceiling at

```
Σ T_loss_VENDOR_max = 1 500 ppm
```

— roughly 44 % of the Friedenauer mirror floor (3 400 ppm), which buys
~ 19 % more UV at the High scenario than the path-2 baseline. How is
that 1 500 ppm divided between the three non-IC mirrors?

Friedenauer's *published* M4' / (M2' or M3') ratio is

```
M4' floor: T < 2 000 ppm  (R > 0.998)
M2' / M3' floor: T < 700 ppm  (R > 0.9993)
Ratio:  2 000 / 700  ≈  2.9
```

— i.e., a dichroic stack (HR @ 559 + HT @ 280 in the same layers)
delivers about 3 × the 559-nm loss of a dedicated single-wavelength HR.
Preserving this ratio and scaling down to the new 1 500 ppm sum gives:

| Mirror | Allocation | R-spec floor |
|---|---|---|
| **M2'** (plane HR) | 300 ppm | R ≥ 99.970 % @ 559 nm |
| **M3'** (curved HR) | 300 ppm | R ≥ 99.970 % @ 559 nm |
| **M4'** (curved dichroic) | 900 ppm | R ≥ 99.910 % @ 559 nm |

This 300 / 300 / 900 ppm split (3:1 dichroic-vs-HR ratio) is the WP's
recommended allocation; the alternative equal-split 500 / 500 / 500
ppm would over-budget M2' / M3' (which can comfortably hit
R ≥ 99.99 % at IBS premium grade) and under-budget M4' (which
realistically delivers ~ 100–1 000 ppm at 559 nm when carrying an
HT @ 280 in the same stack).

The M4' page additionally carries a **T ≥ 95 % @ 280 nm** floor on the
dichroic transmission — tighter than Friedenauer's published T > 94 %,
because modern IBS dichroics routinely deliver T ≥ 97 % at the design
wavelength and there is no economic reason to spec the floor at the
2006 number.

---

## 6 · LIDT, material ranking, and the 280 nm axis (honest dossier)

The peak CW intensity on each mirror at the High scenario
(P_in_559 = 1.5 W, P_circ ≈ 65 W, P_UV ≈ 0.63 W), computed via proper
Gaussian propagation through the BBO + flat-interface + air ABCD chain:

| Mirror | Surface | Peak CW intensity |
|---|---|---|
| M1' / M2' plane | front, 559 nm intracavity | ~ 100–190 kW/cm² (long-arm leg-distribution dependent) |
| M3' / M4' curved | front, 559 nm intracavity | ~ 65 kW/cm² |
| M4' curved | front, 280 nm transit | ~ 0.6 kW/cm² |
| M4' back AR | 280 nm outgoing | ~ 0.6 kW/cm² |

The dossier carries three relevant CW UV / coating LIDT sources, and we
use them in the order in which they admit numerical comparison.

### 6.1 · 559 nm axis — *screening* against the Brown2019 bandgap ladder

[Brown et al. (2019)][Brown2019] measured CW λ/2 damage thresholds at
1 070 nm under controlled carbon-particulate contamination across six
oxide film classes. The thresholds scale monotonically with bandgap
from titania (Eg ~ 3 eV, ~ 100 kW/cm² CW) to silica (Eg ~ 9 eV, no
damage at the highest tested 17.8 MW/cm²). **The absolute thresholds
are *not* wavelength-portable** (the test bench is at 1 070 nm, far from
559 nm), but the bandgap-ranking *is* portable because the mechanism
is thermally driven free-carrier breakdown from contaminant heating —
the underlying coating material sets the runaway threshold via its
bandgap. The Brown thresholds therefore serve as a *screening*
comparison:

| Material | 1 070 nm threshold | Ratio vs our worst-case 559 nm peak (190 kW/cm²) |
|---|---|---|
| Silica | > 17 800 kW/cm² | > 94 × (screening only) |
| Alumina | 6 300 kW/cm² | 33 × |
| Hafnia | 3 800 kW/cm² | 20 × |
| Tantala | 1 600 kW/cm² | 8.4 × |
| Niobia | ~ 200 kW/cm² (extrapolated) | ~ 1 × — **excluded** |
| Titania | ~ 100 kW/cm² | < 1 × — **excluded** |

These ratios are an *upper bound* on the 559 nm threshold (since UV
contamination absorption is typically higher than 1070 nm
contamination absorption). With that pessimism baked in, **silica,
alumina, hafnia, and tantala all admit a comfortable screening
margin**; **niobia and titania do not**. The new coating spec excludes
these last two materials on all four mirrors.

### 6.2 · 280 nm axis — the binding case, but *not* a margin

The closest-wavelength CW UV *operational* benchmark in our dossier is
[Kondo et al. (1998)][Kondo1998] / [Kubota et al. (1998)][Kubota1998],
on Sony Cz-grown BBO at **266 nm CW**: a 1 000-hour run at
**260 W/cm² CW UV power density** with a measured cavity-loss-increase
rate of `5 × 10⁻⁵ %/h`.

Our M4' transit at 280 nm in the High scenario carries

```
I_280_peak ≈ 600 W/cm²    (Gaussian peak)
I_280_avg  ≈ 300 W/cm²    (spot-averaged = peak/2)
```

That is **~ 1.15 × *above* the Kondo / Kubota 1 000-hour operating
point**, not below it. This is the **binding case** of the WP and not
a comfortable margin: service-life expectation at the new build's
1.5 W scenario is *on the same order of magnitude* as the
1 000-hour benchmark, plausibly somewhat shorter, with monotonic
slow-rate loss accumulation. At the 0.5 W scenario the 280 nm
fluence scales down to ~ 60 W/cm² average, well below the
Kondo / Kubota point.

[Burkley et al. (2021)][Burkley2021] is the closest published *coating*
data point — a 244 nm UHV cavity in which oxide (HfO₂/Al₂O₃/SiO₂)
coatings degrade in minutes and fluoride (MgF₂/LaF₃/CaF₂) coatings
survive 10 W intracavity for hours in O₂-rich atmosphere. **The
Burkley paper is not yet numerically extracted in our dossier**, so we
do not currently have a defensible mirror-fluence comparison against
their measurement; what we *do* inherit is the qualitative
oxide-vs-fluoride mechanism (oxygen depletion of the high-index oxide
under UV intracavity exposure) and the recommendation to **operate in
laboratory atmosphere or O₂-rich purge, not UHV**.

### 6.3 · Material recommendation for the M4' dichroic

Combining the bandgap screening (Section 6.1) with the
oxide-vs-fluoride mechanism (Section 6.2) and the
[Turcicova (2022)][Turcicova2022] BBO LIDT review's
**deposition-method ranking IBS > magnetron > e-beam > pulsed-laser-
deposition**, the recommended M4' dichroic stack is a single tiered
policy:

| Tier | Stack | Rationale |
|---|---|---|
| Default | IBS-deposited **HfO₂ / SiO₂** multilayer | Standard PTB-class dichroic at this wavelength; inferred Friedenauer-2006 composition. |
| Acceptable alternative | IBS-deposited **ZrO₂ / SiO₂** multilayer | Equivalent bandgap tier to HfO₂; admissible if it matches the vendor's validated design. |
| Upgrade tier (forward-looking) | **LaF₃ / MgF₂ on CaF₂** substrate | Fluoride multilayer; best LIDT for future evacuated-cavity operation per Burkley. Current build is atmospheric, so this is optional. |
| Excluded | **Nb₂O₅** and **TiO₂** | Bandgap too low at our 559 nm fluence regime per Brown screening. |

A thin SiO₂ cap layer (1–5 μm) does **not** improve LIDT under
particulate contamination per Brown2019 Fig. 5 — the heat from the
heated contaminant diffuses through 1–5 μm of silica in < 1 ms, faster
than the contaminant evaporates, so the cap has no useful timescale.
No cap is specified.

### 6.4 · The cleanliness clause is load-bearing

Brown2019 also demonstrates that **particulate contamination drops the
CW damage threshold by 3–6 orders of magnitude** below the
pristine-sample level. *All* the material-class and
deposition-method discussion above matters only if the delivered
optics are clean: a vendor-clean optic that collects a single 7 μm
carbon particle during shipping operates in a fundamentally different
LIDT regime than the same coating in its packaged state.

The vendor cover letter therefore carries

```
"MIL-STD-1246C Class 100 or better, double-bagged in cleanroom-grade
packaging, on all 16 optics."
```

as a **procurement-acceptance condition** — visible contamination on
delivery is grounds for return-for-re-cleaning before payment is
authorised. This is the single highest-leverage clause in the whole
quote package.

---

## 7 · Service-life expectation and G2-conditional escalation

Conditional on the upstream LBO landing at the High (1.5 W) scenario,
**M4' service-life at the new build is expected on the order of the
Kondo / Kubota 1 000-hour benchmark** (Section 6.2), plausibly
somewhat shorter, with slow monotonic loss-rate accumulation. The
0.5 W scenario sits comfortably above this benchmark. M1' / M2' / M3'
are single-wavelength @ 559 nm and carry > 1 000-hour service-life
expectation with sub-percent / 100 h loss-rate increase.

These numbers are **G2-conditional** — the new build's actual M4'
loss-rate increase under operation has not been characterised
(G2 remains OPEN per [CHARTER][charter] §1.5), so the absolute
service-life claim is bracketed, not measured. The vendor cover
letter carries three escalation paths:

1. **If the M4' coating fails at the *fluoride*-class envelope**
   (oxide coatings die faster than the dossier suggests): re-spec
   M4' toward the LaF₃ / MgF₂ on CaF₂ multilayer upgrade tier.
   Single-page re-quote.
2. **If the M4' coating fails at the *oxide*-class envelope**
   (minutes-to-hours failure under our operating fluence): the
   1.5 W upstream scenario becomes architecturally untenable; the
   build moves to the 0.5 W scenario only. M1' page re-spec'd to
   T = 17 565 ± 500 ppm. M2' / M3' / M4' pages unchanged.
3. **If the M4' coating performs within the dossier envelope:**
   baseline path holds. Both scenarios remain LIDT-acceptable.

The G2 measurement — monitoring M4' cavity-loss-rate increase under
the 1.5 W operating scenario for 100 + hours — is the first
deliverable of the procurement KD downstream of this WP.

---

## 8 · The frozen spec package

Five vendor-facing pages live under
[`logbook/2026-05-20-bbo-coating-run-wp/specs/`][specs]:

| Page | Front face | Back face | Quantity |
|---|---|---|---|
| [M1' input coupler][M1-spec] (plane) | T = 19 965 ± 500 ppm @ 559 nm, AOI ~ 0° | AR @ 559 nm | 4 |
| [M2' plane HR][M2-spec] (HC servo seat, **Ø 6.35 × 2.0 mm** per BC-G addendum) | R ≥ 99.970 % @ 559 nm, AOI ~ 0° | AR @ 559 nm | 4 |
| [M3' curved HR][M3-spec] (ROC = 50 mm) | R ≥ 99.970 % @ 559 nm, AOI 13.7° ± 1.5° p-pol | AR @ 559 nm | 4 |
| [M4' curved dichroic OC][M4-spec] (ROC = 50 mm) | R ≥ 99.910 % @ 559 nm AND T ≥ 95.0 % @ 280 nm, AOI 13.7° ± 1.5° p-pol | AR @ 280 nm (narrow-band) | 4 |
| [Coating-run cover letter][cover-letter] | Eight callouts: AOI band, M4' material tier, single-variant rationale, T_IC-above-Friedenauer justification, AR bandwidth, LIDT acceptance margin vs literature service-life, cleanliness clause, quote format | — | — |

Substrate **material**: Heraeus Herasil throughout (UV-grade fused
silica; mandatory on M4' for the 280 nm transit, preferred uniformly for
scatter-uniformity and procurement-simplicity). Substrate **size**:
Ø 12.7 × 6.35 mm on M1' / M3' / M4'; **M2' is a smaller Ø 6.35 × 2.0 mm
blank** — a [post-closure BC-G addendum][bc-g] dropped the piezo-mounted
servo mirror's moving mass ~ 13× to raise the cavity-lock bandwidth
(~ 1.5× over Friedenauer; the actuator's own mass, not the optic, sets
the ceiling). Deposition: IBS. N = 4 pieces per mirror role yields 4 full
sets — one for the build, three as forward stock against coating-run
rejection, build-time damage, and a future replacement cycle.

---

## 9 · What is *not* claimed

In the spirit of honest dossier accounting:

- **No measured 559 nm IBS HR coating-loss anchor** is in our local
  dossier. The R-spec floors (R ≥ 99.97 %, R ≥ 99.91 %) sit within
  *vendor catalog* capability at Layertec / Laseroptik / ATFilms /
  MLD (vendor-stated, not independently extracted), but a targeted
  literature pass on Hannig2018 + Kraus2022 PTB UV SHG cavities is
  queued and not yet complete.
- **Burkley2021 is SCAFFOLD-tier** (PDF locally staged, no numerical
  fluence extracted). The qualitative oxide-vs-fluoride argument
  inherits; no numerical mirror-fluence comparison against Burkley is
  admitted on this page.
- **G2 (UV-induced degradation rate at 280 nm) remains OPEN.** The
  service-life envelope is a bracket from the closest available CW UV
  operational benchmark (Kondo / Kubota at 266 nm), not a measured
  number on our coating class.
- **G1 (14 GHz unlockable domain)** is inherited from the Friedenauer
  crystal + cavity geometry and is *not* introduced or resolved by
  coating choices ([CHARTER][charter] §8.1).

---

## 10 · Glossary of abbreviations and symbols

### Abbreviations and acronyms

| Abbreviation | Expansion / meaning |
|---|---|
| **AOI** | Angle of incidence (measured from surface normal). |
| **AR** | Anti-reflection coating: thin-film stack that suppresses surface reflection at a target wavelength and AOI. |
| **BBO** | β-barium borate (β-BaB₂O₄). Negative-uniaxial nonlinear crystal used for SHG / SFG in the visible-to-UV range. |
| **BC-A … BC-F** | The six internal phases of this work program (BBO-coating phases A–F): scope / impedance match / per-mirror allocation / LIDT / spec sheets / freeze. See the [closure index][closure]. |
| **CA** | Clear aperture: the centred-circle region of a mirror over which the coating, surface figure, and damage threshold are guaranteed to spec. |
| **CW** | Continuous-wave (as opposed to pulsed) laser operation. |
| **DOI** | Digital Object Identifier — the persistent identifier used in the reference list. |
| **EAR** | (US) Export Administration Regulations — dual-use export-control rules; flagged in the procurement letter alongside ITAR. |
| **FS** | Fused silica (amorphous SiO₂); the standard UV-grade substrate for visible/UV cavity mirrors. *Herasil* and *Suprasil* are Heraeus product grades of UV-grade fused silica. |
| **G1, G2, G3** | Project gates carried in the [CHARTER][charter]: G1 = the 14-GHz "unlockable domain" attribution; G2 = UV-induced coating degradation rate at 280 nm; G3 = Phase-0.5 reference triple (Δ, Ω_R, Γ_sc). Closures advance the WP through Council-3 governance. |
| **HC** | Hänsch–Couillaud (polarisation-based cavity-locking scheme, 1980). |
| **HR** | High reflector (dielectric mirror with R typically ≥ 99.9 %). |
| **HT** | High transmission (used here for the 280 nm-transmissive face of the dichroic output coupler). |
| **IBS** | Ion-Beam Sputtering — the highest-LIDT, lowest-loss thin-film deposition method for dielectric coatings. |
| **IC** | Input coupler (the partial reflector through which the pump enters the cavity). |
| **ITAR** | (US) International Traffic in Arms Regulations — export controls; flagged in the procurement letter. |
| **kW / cm², MW / cm²** | Intensity units: kilowatts and megawatts per square centimetre. |
| **LBO** | Lithium triborate (LiB₃O₅); the nonlinear crystal used *upstream* of the BBO ring to produce 559 nm from 1118 nm. Not redesigned in this WP. |
| **LIDT** | Laser-Induced Damage Threshold (typically expressed as peak CW intensity or pulsed fluence at which the coating begins to fail). |
| **MIL-STD-1246C** | US Military Standard cleanliness specification for optical surfaces and packaging. Class 100 = stringent particulate limit; the new spec's procurement-acceptance condition. |
| **OC** | Output coupler — the mirror through which the harmonic output leaves the cavity. On M4' (a dichroic) this means HR @ 559 nm + HT @ 280 nm in the same stack. |
| **PHE** | "Phase E" — the diagnostic notebook [`2026-05-07-friedenauer-cascade-recompute.py`][PhaseE] that first cross-checked the cavity model against Friedenauer's published numbers. Suffix on `L_passive_PHE`, `γ_SHG_BBO_PHE`. |
| **PM** | Phase matching (the wavevector matching `k_2ω = 2 k_ω` required for efficient SHG). |
| **ppm, pp** | parts per million (1 ppm = 10⁻⁶) and percentage points (1 pp = 10⁻² absolute). 500 ppm = 0.05 pp. |
| **ROC** | Radius of curvature (of a concave or convex mirror). |
| **SHG** | Second-Harmonic Generation: nonlinear process converting two ω photons into one 2ω photon. |
| **SFG / FiHG** | Sum-frequency / fifth-harmonic generation — broader nonlinear processes; relevant in some of the LIDT literature cited (Turcicova2022 §4.2). |
| **TL;DR** | "Too long; didn't read" — the headline summary. |
| **UHV** | Ultra-High Vacuum (typically ≤ 10⁻⁸ mbar). |
| **UV** | Ultraviolet light (here meaning the ≈ 280 nm second harmonic). |
| **WP** | Work program (a structured multi-phase task; this page documents the BBO coating-run WP). |

### Material symbols

| Symbol | Meaning |
|---|---|
| **HfO₂, ZrO₂, Nb₂O₅, Ta₂O₅, TiO₂** | High-index oxide thin-film materials used in dielectric coatings. Bandgap descends in this order; LIDT generally tracks bandgap (Brown2019). |
| **SiO₂** | Silicon dioxide / fused silica — the low-index counterpart in oxide multilayers. Highest bandgap (~ 9 eV), best LIDT screening tier. |
| **MgF₂, LaF₃, CaF₂** | Fluoride thin-film materials — alternative low- and high-index choices for UV operation, with higher bandgaps than the oxide series. Burkley2021's preferred stack for UHV-UV cavities. |
| **Al₂O₃** | Alumina; medium-index oxide used in some HR / AR stacks. |

### Physical quantities

| Symbol | Meaning | Typical value here |
|---|---|---|
| `λ` | Vacuum wavelength | 559 nm (pump), 280 nm (UV) |
| `n` | Refractive index | `n_o(559) = 1.673` in BBO; 1 in air |
| `n_o` / `n_e` | Ordinary / extraordinary index of a uniaxial crystal | per Eimerl Sellmeier |
| `θ_PM` | Phase-matching angle (between optical axis and beam in the crystal) | 44.4° for Type-I 559 → 280 nm BBO |
| `ρ` | Walk-off angle (between Poynting and wavevector for the extraordinary beam) | 83.1 mrad at θ_PM in BBO |
| `d_eff` | Effective nonlinear coefficient (projected for the chosen interaction and polarisation) | 1.44 pm/V central, range 1.30–1.60 (BBO Type-I 559 → 280 nm) |
| `w₀` | Gaussian beam waist (intensity 1/e² half-width at the focus) | 19.4 μm at the BBO short-arm waist |
| `z_R` | Rayleigh range (`π · n · w₀² / λ`); distance over which the spot stays within √2 of waist | 3.54 mm in BBO (air-equivalent 2.12 mm) |
| `ξ` | Boyd-Kleinman focusing parameter `L / b` where `b = 2 z_R` | 1.413 at the Friedenauer geometry |
| `β` | Boyd-Kleinman walk-off parameter `(ρ / 2) √(L · k)` | 18.0 (deeply walk-off-limited) |
| `h_m(ξ, β)` | Boyd-Kleinman focusing factor (≤ 1; product of phase-mismatch and walk-off reductions) | 0.0330 |
| `γ_SHG` | Single-pass SHG conversion coefficient, `γ = η_nl / P_in_single_pass` in the small-signal limit | 1.49 × 10⁻⁴ W⁻¹ at our BBO geometry |
| `η_nl` | Single-pass nonlinear conversion fraction inside the cavity (the cavity sees `η_nl(P_circ) = tanh²(√[γ · P_circ])`) | ~ 1 % at the impedance-matched point |
| `T_IC` | Input-coupler transmission (front face of M1', at 559 nm) | 16 000 ppm in Friedenauer, 19 965 ppm in the new build |
| `R` | Reflectivity (mirror front-face); `T + R + loss = 1` | 99.97 % on M2', M3' fronts; 99.91 % on M4' front @ 559 |
| `L_passive` | Round-trip passive loss (everything in the cavity except the input-coupler transmission and the nonlinear conversion) | 15 288 ppm at the Friedenauer corner |
| `L_total` | Round-trip operating loss = `L_passive` minus the nonlinear-conversion contribution + IC transmission | 13 388 ppm at the new-build default |
| `P_in` | Pump power into the cavity at 559 nm | 0.5–1.5 W (two scenarios) |
| `P_circ` | Steady-state circulating power inside the cavity at 559 nm | 28.5 W @ Low scenario, 65.4 W @ High |
| `P_UV` | Output power at the harmonic, 280 nm | 0.12 W @ Low scenario, 0.63 W @ High |
| `Δ_ref` | Raman detuning reference for the ²⁵Mg⁺ build (CHARTER §1.5 Phase 0.5 triple) | 40 GHz |
| `Ω_R` | Raman Rabi frequency reference | 2π × 400 kHz |
| `Γ_sc` | Scattering-rate reference per Raman gate | 2.0 × 10⁴ s⁻¹ |

### Mirror identifiers (Friedenauer-2006 §3 / Table 1)

| ID | Role | Position |
|---|---|---|
| **M1'** | Plane input coupler (IC); partial reflector at 559 nm + AR @ 559 on back | Long arm of the bowtie ring; near-normal AOI |
| **M2'** | Plane high-reflector (HR @ 559 nm); piezo-mounted for the HC servo lock; AR @ 559 on back | Long arm; near-normal AOI |
| **M3'** | Curved HR @ 559 nm (focusing mirror), ROC = 50 mm; AR @ 559 on back | Short arm; 13.7° AOI p-pol |
| **M4'** | Curved dichroic output coupler — HR @ 559 nm AND HT @ 280 nm in the same stack on the concave front; narrow-band AR @ 280 nm on the planar back | Short arm; 13.7° AOI p-pol |

The prime (`'`) distinguishes the four BBO-stage mirrors from their LBO-stage
counterparts (M1, M2, M3, M4, all at 1118 nm) in the upstream cavity.

---

## References

[Friedenauer2006]: https://doi.org/10.1007/s00340-006-2222-1
[Eckardt1990]: https://doi.org/10.1109/3.55534
[Eimerl1987]: https://doi.org/10.1063/1.339536
[Tamosauskas2018]: https://doi.org/10.1364/OME.8.001410
[BoydKleinman1968]: https://doi.org/10.1063/1.1656831
[PolzikKimble1991]: https://doi.org/10.1364/OL.16.001400
[Ashkin1966]: https://doi.org/10.1109/JQE.1966.1073956
[HanschCouillaud1980]: https://doi.org/10.1016/0030-4018(80)90069-3
[Brown2019]: https://doi.org/10.1038/s41598-018-37337-5
[Burkley2021]: https://arxiv.org/abs/2105.14977
[Turcicova2022]: https://doi.org/10.1016/j.optlastec.2022.107876
[Kondo1998]: https://doi.org/10.1364/OL.23.000195
[Kubota1998]: https://doi.org/10.1364/DLAI.1998.FC4
[Hannig2018]: https://doi.org/10.1063/1.5005515
[Kraus2022]: https://doi.org/10.1364/OE.471450

1. **Friedenauer, A., et al.** *"A laser system for ultracold experiments with electroshelved trapped ions."*
   *Applied Physics B* **84**, 371–380 (2006). DOI [`10.1007/s00340-006-2222-1`][Friedenauer2006].
   The reference architecture this WP re-evaluates.
2. **Eckardt, R. C., Masuda, H., Fan, Y. X., Byer, R. L.** *"Absolute and relative nonlinear optical coefficients of KDP, KD*P, BaB₂O₄, LiIO₃, MgO:LiNbO₃, and KTP measured by phase-matched second-harmonic generation."* *IEEE J. Quantum Electron.* **26**, 922–933 (1990). DOI [`10.1109/3.55534`][Eckardt1990].
   d_eff anchor for BBO Type-I.
3. **Eimerl, D., Davis, L., Velsko, S., Graham, E. K., Zalkin, A.** *"Optical, mechanical, and thermal properties of barium borate."* *J. Appl. Phys.* **62**, 1968–1983 (1987). DOI [`10.1063/1.339536`][Eimerl1987].
   Sellmeier dispersion + walk-off.
4. **Tamošauskas, G., Beresnevičius, G., Gadonas, D., Dubietis, A.** *"Transmittance and phase matching of BBO crystal in the 0.188–5.2 μm wavelength range."* *Opt. Mater. Express* **8**, 1410–1418 (2018). DOI [`10.1364/OME.8.001410`][Tamosauskas2018].
   Modern Sellmeier cross-check.
5. **Boyd, G. D., Kleinman, D. A.** *"Parametric interaction of focused Gaussian light beams."* *J. Appl. Phys.* **39**, 3597–3639 (1968). DOI [`10.1063/1.1656831`][BoydKleinman1968].
   The h_m focusing-factor formalism this WP consumes.
6. **Polzik, E. S., Kimble, H. J.** *"Frequency doubling with KNbO₃ in an external cavity."* *Opt. Lett.* **16**, 1400–1402 (1991). DOI [`10.1364/OL.16.001400`][PolzikKimble1991].
   The impedance-match relation `T = L + (1−L) η_nl` derived for the SHG enhancement cavity. The exact cross-term is implemented in [`src/enhancement_cavity.py`][enhancement_cavity].
7. **Ashkin, A., Boyd, G. D., Dziedzic, J. M.** *"Resonant optical second-harmonic generation and mixing."* *IEEE J. Quantum Electron.* **2**, 109–124 (1966). DOI [`10.1109/JQE.1966.1073956`][Ashkin1966].
   The original SHG ring-cavity buildup analysis.
8. **Hänsch, T. W., Couillaud, B.** *"Laser frequency stabilisation by polarization spectroscopy of a reflecting reference cavity."* *Opt. Commun.* **35**, 441–444 (1980). DOI [`10.1016/0030-4018(80)90069-3`][HanschCouillaud1980].
   The locking scheme used on both Friedenauer and the new build.
9. **Brown, A., et al.** *"Physical origin of early failure for contaminated optics."* *Sci. Rep.* **9**, 635 (2019). DOI [`10.1038/s41598-018-37337-5`][Brown2019].
   Bandgap-vs-LIDT scaling at 1 070 nm CW; mechanism portable, thresholds not.
10. **Burkley, Z., et al.** *"Stable high power deep-UV enhancement cavity in ultra-high vacuum with fluoride coatings."* arXiv [`2105.14977`][Burkley2021] (2021).
    Closest published CW UV cavity-mirror lifetime data; oxide vs fluoride at ~ 244 nm. SCAFFOLD in our dossier (not yet numerically extracted).
11. **Turcicova, H., et al.** *"Laser induced damage threshold (LIDT) of β-barium borate (BBO) and cesium lithium borate (CLBO) — Overview."* *Opt. Laser Technol.* **149**, 107876 (2022). DOI [`10.1016/j.optlastec.2022.107876`][Turcicova2022].
    BBO LIDT review; deposition-method ranking; AR-coating LIDT lowering.
12. **Kondo, K., et al.** *"Demonstration of long-term reliability of a 266-nm continuous-wave light source for a photolithography aligner."* *Opt. Lett.* **23**, 195–197 (1998). DOI [`10.1364/OL.23.000195`][Kondo1998]; companion: **Kubota, S., et al.** *"Efficient 213 nm and 266 nm generations in Czochralski-grown beta-barium borates."* *OSA TOPS* **17**, 79–83 (1998). DOI [`10.1364/DLAI.1998.FC4`][Kubota1998].
    1 000-hour CW UV operational benchmark at 266 nm; closest-wavelength CW UV service-life data point.
13. **Hannig, S., et al.** *"A highly stable monolithic enhancement cavity for second harmonic generation in the ultraviolet."* *Rev. Sci. Instrum.* **89**, 013106 (2018). DOI [`10.1063/1.5005515`][Hannig2018].
    PTB monolithic BBO ring SHG at 626 → 313 nm; 130-hour CW operation. Queued for numerical extraction.
14. **Kraus, B., et al.** *"Phase-stabilized UV light at 267 nm through twofold second harmonic generation."* *Opt. Express* **30**, 44992–45003 (2022). DOI [`10.1364/OE.471450`][Kraus2022].
    PTB twofold UV SHG cavity at 267 nm; direct architectural analogue of Friedenauer. Queued for numerical extraction.

---

## Internal cross-links (for builders working from this repository)

- The full work-program folder: [`logbook/2026-05-20-bbo-coating-run-wp/`][closure].
- The reference architecture: [Friedenauer 2006](friedenauer-2006.html).
- The parent next-gen workplan: [Next-generation 500 mW UV source](next-gen.html).
- The frozen vendor-facing spec package: [`specs/`][specs].
- The architecture-neutral numerics this page consumes:
  [`src/enhancement_cavity.py`][enhancement_cavity],
  [`src/boyd_kleinman.py`][bk],
  [`src/shg_single_pass.py`][shg],
  [`src/abcd.py`][abcd].

[closure]: https://github.com/uwarring82/mg-plus-uv-chain/tree/main/logbook/2026-05-20-bbo-coating-run-wp
[specs]: https://github.com/uwarring82/mg-plus-uv-chain/tree/main/logbook/2026-05-20-bbo-coating-run-wp/specs
[M1-spec]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/specs/M1-input-coupler.md
[M2-spec]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/specs/M2-plane-HR.md
[M3-spec]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/specs/M3-curved-HR.md
[M4-spec]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/specs/M4-curved-OC-dichroic.md
[cover-letter]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/specs/coating-run-cover-letter.md
[bc-b-results]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/bc-b-results.md
[bc-g]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-20-bbo-coating-run-wp/bc-g-results.md
[next-gen]: next-gen.html
[charter]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md
[enhancement_cavity]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/enhancement_cavity.py
[bk]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/boyd_kleinman.py
[shg]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/shg_single_pass.py
[abcd]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/abcd.py
[PhaseE]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py
[BC-B-notebook]: https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py
