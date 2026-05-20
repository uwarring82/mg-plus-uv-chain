# Coating-run cover letter — BBO ring cavity, 559 → 280 nm CW SHG

**From:** AG Schätz, Universität Freiburg.
Steward: Ulrich Warring (u.j.warring@gmail.com).
**Build:** Next-generation BBO ring cavity for ²⁵Mg⁺ ion-trap UV
source, replacing the Friedenauer-2006 reference build.
**Sheet status:** DRAFT (2026-05-20) — pending steward sign-off at BC-F.

---

This run covers four optics in a 559 → 280 nm CW SHG ring cavity:

| Optic | Geometry | Front coating | Back coating | Quantity |
|---|---|---|---|---|
| **M1'** input coupler | Plane | T = 19 965 ppm ± 500 ppm @ 559 nm, AOI ~ 0° | AR @ 559 nm | 4 |
| **M2'** plane HR (piezo seat) | Plane | R ≥ 99.970 % @ 559 nm, AOI ~ 0° | AR @ 559 nm | 4 |
| **M3'** curved HR | Concave ROC = 50 mm | R ≥ 99.970 % @ 559 nm, AOI 13.7° ± 1.5° p-pol | AR @ 559 nm | 4 |
| **M4'** curved dichroic OC | Concave ROC = 50 mm | R ≥ 99.910 % @ 559 nm AND T ≥ 95.0 % @ 280 nm, AOI 13.7° ± 1.5° p-pol | AR @ 280 nm (narrow-band) | 4 |

Substrate: Heraeus Herasil throughout (UV-grade fused silica; mandatory
on M4', preferred on M1'/M2'/M3').
Per-mirror sheets in
[`M1-input-coupler.md`](M1-input-coupler.md),
[`M2-plane-HR.md`](M2-plane-HR.md),
[`M3-curved-HR.md`](M3-curved-HR.md),
[`M4-curved-OC-dichroic.md`](M4-curved-OC-dichroic.md).

The eight callouts below resolve the design choices that are *not*
obvious from the per-mirror sheets alone. Please read before quoting.

---

## A · AOI band on the curved mirrors (13.7° ± 1.5° p-pol)

The Friedenauer ring uses a bowtie geometry with full folding angle
27.4°, i.e., 13.7° AOI per curved mirror. **The coating must hold
spec across a ± 1.5° band**, i.e., over 12.2°–15.2°, not only at the
nominal 13.7°.

The reason: bench-build alignment realistically varies between
near-identical bowtie cavities. Our procurement band is set
conservatively to cover this — a coating that drifts off-spec by the
band edge would degrade the cavity finesse and the dichroic T/R
balance once installed. The ± 1.5° figure is a chosen procurement
spec; it is not bench-measured tolerance data.

The plane mirrors M1' and M2' sit at near-normal incidence (~ 0°);
the AOI band there is ± 1°.

## B · M4' dichroic material recommendation

The M4' dichroic stack is the most-differentiated coating in this run.
**The recommended material tier:**

1. **Default (baseline):** **IBS-deposited HfO₂ / SiO₂ multilayer.**
   This is the standard PTB-class dichroic at this wavelength and the
   inferred Friedenauer-2006 composition.
2. **Acceptable alternative:** **IBS-deposited ZrO₂ / SiO₂ multilayer.**
   Equivalent bandgap-tier to HfO₂; admissible if it matches your
   existing validated design.
3. **Upgrade tier (please quote as separate line item):**
   **LaF₃ / MgF₂ on CaF₂ substrate** — fluoride multilayer for the
   longest UV service life under future evacuated-cavity operation.
   The current build is atmospheric; this option is forward-looking.
4. **Excluded materials:** **Nb₂O₅ and TiO₂** — bandgap too low at
   our 559 nm fluence regime per Brown2019 screening (BC-D §C.1).
5. **No silica cap layer.** Brown2019 shows that thin SiO₂ caps
   (1–5 μm) give zero measurable LIDT improvement under particulate
   contamination — don't pay the premium.

For M1' / M2' / M3' (single-WL @ 559 nm HRs and IC), the
material-class screening admits silica / alumina / hafnia / tantala;
**niobia and titania are excluded** on these too.

## C · Why one M1' variant covers both upstream scenarios

The new build's upstream LBO output sits anywhere between ≈ 0.5 W
and ≈ 1.5 W of 559 nm into the BBO ring, depending on which LBO
configuration the parent next-gen workplan converges to. These two
scenarios would in principle want different impedance-matched M1'
transmissions:

- Low scenario (0.5 W in): T_IC_opt = 17 565 ppm (1.756 %).
- High scenario (1.5 W in): T_IC_opt = 22 945 ppm (2.295 %).

**The Δ between these is 5 380 ppm (≈ 0.54 pp absolute).** A single
M1' coating at the equal-penalty (minimax) centre 19 965 ppm
± 500 ppm has both scenarios paying ~ −0.68 % UV vs their respective
optima — within the noise of typical IBS-run-to-run variation.
**We are not requesting two M1' variants; one coating run with the
single centre above covers both upstream scenarios with acceptable
penalty.**

## D · Why T_IC = 19 965 ppm (above Friedenauer's published 16 000 ppm)

Friedenauer 2006 published a BBO ring IC with R = 0.984
(equivalently T = 16 000 ppm = 1.60 %). Re-running their published
configuration through the forward model with the BC-A-pinned
`(L_passive_PHE, γ_SHG_BBO)` constants gives the impedance-matched
optimum at **T_IC_opt = 21 700 ppm ≈ 2.17 %**, ~ 0.57 pp *above*
Friedenauer's procured T_IC. Friedenauer's published coating ran
~ 0.6 pp below the impedance-matched optimum at their γ, forfeiting
about **3.6 % UV buildup**. We are spec'ing the new run *at* the
optimum, not below it.

The new-build optimum at our two-scenario equal-penalty centre lands
at **T = 19 965 ppm = 2.00 %** ± 500 ppm. This is **higher T** (lower
R) than the Friedenauer reference — by design, not by accident.

## E · AR bandwidth at 280 nm on M4' back face

**Default: narrow-band AR centred at 280 nm.** The CW chain is locked
at Δ_ref = 40 GHz (≈ 0.01 nm at 280 nm), so a typical narrow-band IBS
AR coating (FWHM ~ 5 nm) is more than adequate. Narrow-band is also
easier to spec and cheaper than broadband.

**Optional upgrade: broadband 250–300 nm AR.** Please quote as a
separate line item if your standard catalog supports it. This option
is only worthwhile if we ever need to re-purpose M4' for a different
build at a different UV wavelength — not required for the current run.

## F · LIDT margin + G2-conditional service-life clauses

LIDT specs on each per-mirror sheet carry **3–8 × margin** over the
worst-case CW operating intensity at the 1.5 W upstream scenario.
This margin is set against the closest-wavelength published CW UV
operational benchmark in our literature dossier:

- **Kondo / Kubota 1998** (Sony Cz-BBO at 266 nm CW): 260 W/cm² CW
  UV power density operating point, with 1 000 h of operation and
  5 × 10⁻⁵ %/h cavity-loss-rate increase.
- **Our M4' transit 280 nm fluence**: ~ 300 W/cm² average (1.5 W
  scenario), i.e., **~ 1.15 × *above* the Kondo / Kubota benchmark**.
  Service life is expected to be *on the order of* (not comfortably
  below) the 1 000 h benchmark.

**G2-conditional escalation paths:**

1. If the M4' coating fails worse than expected at the **fluoride**
   class envelope (i.e., the Burkley2021 LaF₃ / MgF₂ / CaF₂ data
   point — see [`bc-d-results.md`](../bc-d-results.md) §C.2 for the
   data inventory), we may re-spec the M4' page toward the upgrade
   tier (§B above). Please indicate whether re-quoting against the
   LaF₃ / MgF₂ on CaF₂ alternative would require a new design study
   or a runtime extension on this initial order.
2. If the M4' coating fails worse than the **oxide** class envelope
   (i.e., minutes-to-hours failure under our operating fluence), the
   1.5 W upstream scenario becomes unsustainable and the build moves
   to the 0.5 W scenario only. The M1' centre would re-spec to
   17 565 ± 500 ppm in that case; please note that the M2'/M3'/M4'
   pages above are *unchanged* under that escalation, so this is a
   single-page re-quote, not a full re-run.

The absolute service-life claim above (~ 1 000 h order of magnitude)
is **G2-conditional**: it depends on the new build's measured M4'
loss-rate increase under the 1.5 W operating scenario, which has not
yet been characterised. The above is the dossier-anchored bracket,
not a measured number.

## G · Cleanliness on delivery (LOAD-BEARING)

**MIL-STD-1246C Class 100 or better**, **double-bagged in
cleanroom-grade packaging**, on all 16 optics. This is *the*
single most important handling clause in this entire quote.

The rationale: Brown2019 (open-access *Sci. Rep.* 9, 635) demonstrates
that particulate contamination (carbon microparticles, steel dust)
drops the CW damage threshold of dielectric coatings by **3–6 orders
of magnitude** below the pristine-substrate level. The bandgap
ranking and IBS deposition method we are requesting matter *only*
if the delivered surfaces are clean; a vendor-clean optic that
collects a single 7 μm carbon particle during shipping is operating
in a fundamentally different LIDT regime than the same coating in
its packaged state.

The cleanliness clause is **a procurement-acceptance condition**:
any optic delivered visibly contaminated or with packaging integrity
compromised will be returned for re-cleaning before payment is
authorised. Please confirm in quote that your standard delivery
meets MIL-STD-1246C Class 100; if it does not, please indicate the
incremental cost for the upgrade.

## H · Quote format and timeline

| Field | Request |
|---|---|
| Lead time | Please quote earliest delivery for the standard line items + any longer lead for the M4' dichroic |
| Quote validity | ≥ 60 days from issue (we may re-quote the M4' page after the steward's BC-F review) |
| Currency | EUR preferred; USD acceptable |
| Incoterms | DDP (delivered duty paid) to AG Schätz Freiburg if you have an EU presence; otherwise DAP + import paperwork |
| ITAR / EAR coverage | No US-government restrictions expected on this build — please flag if your stack designs trigger any |
| Cleanliness upgrade (if not standard) | Quote as separate line item |
| Vendor catalog references | Please quote against your standard catalog stack designs and identify the closest match; non-stock coating runs are welcome but please flag run-frequency / minimum-order constraints |
| Drawings | We can supply CAD drawings (Friedenauer-2006 §3 / Table 1 cavity layout) if helpful for fit-check |

---

## Conventions, contact, references

- All intensities specified as **peak Gaussian intensity** at the
  spot center, 1/e² half-width (not 1/e). LIDT specs are CW unless
  otherwise stated.
- All numerical specs are **fractional units** (1 = 100 %). Where
  ppm appears, ppm = parts per million absolute (1 ppm = 10⁻⁶).
- All AOI values are measured from surface normal.
- Steward contact: **Ulrich Warring** <u.j.warring@gmail.com>.
- Build documentation: Friedenauer et al., *Appl. Phys. B* **84**,
  371 (2006), DOI [`10.1007/s00340-006-2222-1`](https://doi.org/10.1007/s00340-006-2222-1).
- Architecture is a **next-generation iteration** of the Friedenauer
  reference, with the BBO ring geometry held fixed and only the
  coating specifications optimised against the published baseline.

---

**Quotes from multiple coating houses will be compared on price,
lead time, and the quality of the M4' dichroic stack design.** We
expect to award the contract within ~ 30 days of receiving quotes;
please ensure your quote covers the full set above as a single
package.

Thank you.

Ulrich Warring, on behalf of AG Schätz / Universität Freiburg.
