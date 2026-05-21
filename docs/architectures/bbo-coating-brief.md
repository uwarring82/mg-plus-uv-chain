---
layout: default
title: "Coatings for a 559 → 280 nm CW BBO doubling cavity — spec and open questions"
description: "A standing technical brief: how the mirror-coating parameters were fixed for a continuous-wave 559 → 280 nm BBO ring doubler on a Friedenauer-2006 geometry, the resulting four-mirror coating targets, and the open questions we would value expert input on — coating feasibility, the atmosphere around the SHG crystal, and BBO vs CLBO. Audience: anyone who has built, operated, or coated CW UV second-harmonic cavities."
---

<p class="eyebrow">Coating brief · 559 → 280 nm BBO ring</p>

# Coatings for a 559 → 280 nm CW BBO doubling cavity

A short standing brief on the **mirror-coating specification** for a
continuous-wave cavity that frequency-doubles 559 nm to 280 nm in a
Brewster-cut BBO crystal, for a ²⁵Mg⁺ ion-trap ultraviolet source. The
cavity geometry follows a published reference design
([Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006)][friedenauer]);
we have re-specified **only the mirror coatings** for a new coating run.

Before the spec goes to coating vendors, we would value a sanity-check
from anyone who has built and operated a CW UV doubling cavity, on:

1. whether the coating parameter choices are sound and manufacturable; and
2. a few genuinely open physics questions — the atmosphere around the
   crystal, and whether BBO is the right nonlinear medium at all (vs CLBO).

If you also have coating-vendor or substrate-sourcing experience to
share, that is welcome too, but secondary. This page carries the
reasoning and the numbers so a reader can react to the design rather than
re-derive it.

---

## 1 · The system in brief

A four-mirror bow-tie ring, continuously locked to the 559 nm pump, with
second-harmonic generation at the intracavity focus. The geometry below
is held **fixed** (inherited from the reference design); only the
coatings are free parameters.

| Parameter | Value |
|---|---|
| Pump / harmonic wavelength | 559 nm → 280 nm, CW |
| Cavity round-trip length | 0.470 m |
| Topology | bow-tie ring, full fold angle 27.4° (13.7° per curved mirror) |
| Curved mirrors | ROC = 50 mm (f = 25 mm), separation 59.4 mm |
| Intracavity waist at the crystal | 19.4 µm (Boyd–Kleinman optimum for the crystal length) |
| Nonlinear crystal | BBO, Brewster-cut, Type-I, 4 × 4 × 10 mm³, θ ≈ 44.4° |
| Crystal temperature | ~ 50 °C (kept warm to avoid condensation on the hygroscopic faces) |

We use the primed mirror labels **M1′–M4′** for the doubling stage, to
avoid confusion with the upstream cavity. Two plane mirrors sit on the
long arm — the **input coupler (M1′)** and a **piezo-mounted high
reflector (M2′)** that carries the cavity lock. Two concave mirrors at
the focus are a **high reflector (M3′)** and the **dichroic output
coupler (M4′)** that reflects 559 nm and transmits the 280 nm harmonic
out of the cavity.

---

## 2 · How the coating parameters were fixed

We tried to make every coating number traceable to a measurement or a
self-consistent calculation rather than a convention. The chain was:

1. **Hold the geometry, free only the coatings.** Walk-off, focusing,
   and the nonlinear gain are inherited from the reference design, which
   we cross-checked against its published harmonic output to ~ 1.5 %.
   That fixes the single-pass nonlinear coefficient used downstream.

2. **Calibrate the round-trip loss against the published reference.**
   We required our cavity model to reproduce the reference's measured
   operating point (0.95 W at 559 nm in, 1.6 % input-coupler
   transmission, 0.275 W of 280 nm out) within 5 %. This pins the
   round-trip *passive* loss self-consistently — about 1.5 % total, of
   which only ~ 0.34 % can be mirror transmission at the published
   reflectivity floors; the remainder is crystal / Brewster-face
   scatter, bulk absorption, and similar non-mirror loss that a new
   build of the same crystal class inherits.

3. **Two pump-power scenarios bracket the upstream uncertainty.** The
   559 nm source may deliver anywhere between ~ 0.5 W (a conservative
   fallback) and ~ 1.5 W (an upgraded pump). Because the optimal
   input-coupler transmission *rises* with pump power (nonlinear
   depletion adds to the round-trip loss the coupling must match), we
   computed the impedance-matched coupler for both ends:

   - 0.5 W in → optimum ≈ 1.76 % transmission;
   - 1.5 W in → optimum ≈ 2.29 % transmission.

4. **One compromise input coupler instead of two.** The two optima
   differ by only ~ 0.54 percentage points, so a single coating at the
   equal-penalty centre — **T = 2.00 % (≈ 20 000 ppm) ± 0.05 percentage
   points (± 500 ppm)** — leaves both scenarios within ~ 1 % of their
   respective best buildup. We are not requesting two coupler variants.

   *(A side finding worth flagging: the reference design ran ~ 0.6
   percentage points below its own impedance-matched optimum, leaving
   ~ 3.6 % of buildup on the table. We are specifying at the optimum.)*

5. **Allocate the remaining loss budget across the other three
   mirrors.** We hold the summed transmission loss of the two high
   reflectors plus the dichroic to ≤ 1500 ppm, split 300 / 300 / 900 ppm
   (the dichroic is allowed the larger share, matching the reference's
   ~ 3:1 dichroic-to-HR loss ratio). This gives the per-mirror
   reflectivity floors below.

6. **Set damage thresholds and substrates from the intracavity intensity
   envelope.** At the impedance-matched point the cavity circulates
   ~ 28 W (0.5 W in) to ~ 65 W (1.5 W in) of 559 nm. That puts
   ~ 110–200 kW/cm² on the plane mirrors, ~ 28–64 kW/cm² on the curved
   mirrors, and ~ 5–11 MW/cm² at the crystal waist (all CW, peak
   Gaussian). We set CW LIDT acceptance thresholds 3–8× above the worst
   case; this is a **vendor acceptance margin**, not a
   literature-supported service-life claim. UV-grade fused silica
   throughout; mandatory on the dichroic because 280 nm transits its
   substrate. IBS deposition; a stringent cleanliness-on-delivery clause
   (particulate contamination is, in our reading of the literature, the
   dominant damage risk).

7. **Size the lock mirror for servo bandwidth, not for symmetry.** The
   piezo-mounted M2′ is the one mirror whose *substrate mass* matters: it
   sets the loaded mechanical resonance and hence the cavity-lock
   bandwidth. With our actuator (a PI P-887.31 stack), the stack's own
   effective mass dominates, so we shrank M2′ to a small Ø 6.35 × 2.0 mm
   blank — light enough to recover most of the available bandwidth, and
   matched to the actuator face. The other mirrors stay at the standard
   Ø 12.7 × 6.35 mm.

### Resulting coating targets

| Mirror | Substrate | Front-face coating @ 559 nm | Extra | CW LIDT target |
|---|---|---|---|---|
| **M1′** input coupler (plane) | Ø 12.7 × 6.35 mm | **T = 2.00 % ± 0.05 pp** (≈ 20 000 ± 500 ppm), AOI ~ 0° | AR @ 559 (back) | ≥ 500 kW/cm² |
| **M2′** lock HR (plane, piezo) | **Ø 6.35 × 2.0 mm** | **R ≥ 99.970 %**, AOI ~ 0° | AR @ 559 (back); flatness ≤ λ/10 | ≥ 500 kW/cm² |
| **M3′** focusing HR (concave) | Ø 12.7 × 6.35 mm | **R ≥ 99.970 %** over 13.7° ± 1.5° p-pol | AR @ 559 (back) | ≥ 250 kW/cm² |
| **M4′** dichroic output coupler (concave) | Ø 12.7 × 6.35 mm | **R ≥ 99.910 % @ 559** *and* **T ≥ 95 % @ 280**, over 13.7° ± 1.5° p-pol | AR @ 280 (back, narrow-band) | ≥ 250 kW/cm² @ 559 + ≥ 5 kW/cm² @ 280 |

All curved-mirror reflectivities must hold across the **± 1.5° angle-of-
incidence band**, not only at the nominal 13.7°. Expected quantity is
**N = 4 per mirror role** (16 optics total). Full per-mirror sheets
(coating targets, AOI bands, tolerance and LIDT margins) are available on
request.

---

## 3 · Open questions we would value input on

### A · Coatings

1. **Dichroic feasibility.** Is **R ≥ 99.91 % @ 559 nm together with
   T ≥ 95 % @ 280 nm in one stack, held over a ± 1.5° AOI band**,
   comfortably within current IBS practice — or near an edge on either
   the reflectivity or the band? What T @ 280 nm would you actually
   expect to deliver?
2. **Is the ± 1.5° AOI band over-conservative?** It comes from a
   photogrammetric estimate of fold-angle spread across existing
   doublers, not a bench measurement, so it may be wider than the real
   build-to-build variation. A tighter band could relax the dichroic.
3. **Achievable 559 nm HR loss.** We could not find a solid published
   anchor for IBS HR transmission loss at 559 nm, so the budget uses the
   reference reflectivity floors. What total loss (absorption + scatter)
   do you typically measure at this wavelength?
4. **Dichroic material.** Default HfO₂/SiO₂, with ZrO₂/SiO₂ acceptable;
   a fluoride stack on CaF₂ as a longer-UV-life upgrade. Would you choose
   differently for CW 280 nm transmission?
5. **280 nm damage and service life.** This is the parameter we are least
   sure of (see §3B). The 280 nm transit fluence on the dichroic is
   ~ 300 W/cm² average, sitting right at the nearest published CW-UV
   operational benchmark (~ 1000 h at a comparable density), not
   comfortably below it. How do your 280 nm coatings behave over
   hundreds to thousands of hours?

### B · Atmospheric conditions near the SHG

This is genuinely open for us; input from anyone who has run CW UV optics
at comparable wavelengths (e.g. 313 nm systems) would help most.

- BBO is mildly hygroscopic; the reference design simply kept the crystal
  warm. Beyond condensation, **UV-induced degradation** of both the
  crystal exit faces and the dichroic coating depends strongly on the
  local atmosphere (humidity, hydrocarbons, oxygen content).
- **What enclosure / atmosphere would you recommend around the crystal
  and the output coupler for best long-term UV stability?** Options on
  the table: dry purged air, dry nitrogen, oxygen-enriched purge (to
  suppress UV-darkening / hydrocarbon cracking), a sealed box, or a light
  vacuum. Each trades condensation, UV degradation, and practicality
  differently, and we have no measured basis to choose.
- Does the answer change between the 0.5 W and 1.5 W output cases?

### C · BBO vs CLBO

We are staying on **BBO** for this coating run — it matches the reference
design and is the conventional CW choice at 280 nm. **CLBO (CsLiB₆O₁₀)**
is the obvious alternative to weigh. The draw is *not* efficiency: CLBO's
effective nonlinearity is actually lower than BBO's, so it would mean a
longer crystal or more buildup for the same harmonic power. What it
offers instead is a higher UV damage threshold, smaller walk-off, and
reputedly better longevity under sustained UV fluence — which matters
precisely because UV service life is our weakest-known parameter.

Our hesitation is operational. CLBO is strongly hygroscopic: it typically
demands ~ 150 °C and a tightly controlled dry atmosphere — hermetic
sealing or active dry-gas management — which feeds straight back into the
atmosphere question above.

**For anyone who has chosen between BBO and CLBO for a CW UV cavity: what
drove your crystal choice? And is CLBO's handling overhead ever worth it
at 280 nm CW in a lab that does not run a sealed UV envelope — or is it
really a sub-266 nm / high-pulse-energy tool that should not be reached
for here?**

---

## Appendix · Reference numbers

| Pump (559 nm in) | Optimal coupler T | Circulating 559 nm | 280 nm out | Peak intensity at waist |
|---|---|---|---|---|
| 0.5 W | 1.756 % | 28.5 W | 0.120 W | 4.8 MW/cm² |
| 0.95 W (interpolating point) | 2.026 % | 46.9 W | 0.326 W | 7.9 MW/cm² |
| 1.5 W | 2.295 % | 65.4 W | 0.633 W | 11.1 MW/cm² |

These rows use the new-build default mirror-loss allocation (summed
M2′/M3′/M4′ transmission loss 1500 ppm). The separate reference
cross-check is the 2006 operating point: 0.95 W in, T = 1.6 %, 0.275 W
out; re-optimising that published point gives T ≈ 2.17 % and 0.285 W out,
which is the ~ 3.6 % buildup gap mentioned above. All intensities are
peak Gaussian (1/e² half-width), CW. The single coating run is specified
at the compromise coupler T = 2.00 % to serve the whole range.

---

If you have a view on any of the above, we would be glad to hear it.
A fuller technical explainer — with the full impedance-match math and the
damage-threshold literature inventory — is available as a companion page:
[BBO coating run: rationale and calculations](bbo-coating-run.html).

[friedenauer]: https://doi.org/10.1007/s00340-006-2222-1
