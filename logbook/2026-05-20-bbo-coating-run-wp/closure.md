# BBO coating-run WP — closure document

**Status:** **CLOSED 2026-05-20.**
**Steward:** Ulrich Warring.
**Phases:** BC-A → BC-F, all closed within a single calendar day
(2026-05-20).
**Workplan:** [`workplan.md`](workplan.md) (v3, endorsed 2026-05-20
after a four-round review pass).

This file is the index + handoff to the procurement KD downstream of
this WP. It does **not** duplicate per-phase results; it points at
them and records what is *frozen*, what is *open*, and what comes
*next*.

---

## A · Frozen specifications (sent-to-vendor-ready)

Five vendor-facing pages inside [`specs/`](specs/), all frozen at
BC-F closure on 2026-05-20:

| Page | Front-face spec | Back-face spec | Quantity |
|---|---|---|---|
| [M1'](specs/M1-input-coupler.md) input coupler (plane) | T = 19 965 ppm ± 500 ppm @ 559 nm, AOI ~ 0° p-pol | AR @ 559 nm | 4 |
| [M2'](specs/M2-plane-HR.md) plane HR (HC servo seat) | R ≥ 99.970 % @ 559 nm, AOI ~ 0° p-pol | AR @ 559 nm | 4 |
| [M3'](specs/M3-curved-HR.md) curved HR (ROC = 50 mm) | R ≥ 99.970 % @ 559 nm, AOI 13.7° ± 1.5° p-pol | AR @ 559 nm | 4 |
| [M4'](specs/M4-curved-OC-dichroic.md) curved dichroic OC (ROC = 50 mm) | R ≥ 99.910 % @ 559 nm AND T ≥ 95.0 % @ 280 nm, AOI 13.7° ± 1.5° p-pol | AR @ 280 nm (narrow-band) | 4 |
| [Cover letter](specs/coating-run-cover-letter.md) | Eight callouts: AOI band, M4' material tier, single-variant rationale, T_IC-above-Friedenauer justification, AR bandwidth, LIDT + G2-conditional clauses, cleanliness clause, quote format | — | — |

Substrate: Heraeus Herasil throughout (UV-grade FS; mandatory on
M4', preferred on M1'/M2'/M3'). Deposition: IBS required.
Cleanliness on delivery: MIL-STD-1246C Class 100 or better
(load-bearing — see cover letter §G).

---

## B · Quantitative pins (canonical references)

The single γ / L authority for the WP is
[`constants.md`](constants.md) §F:

| Symbol | Value | Source |
|---|---|---|
| `γ_SHG_BBO_PHE` | 1.4914 × 10⁻⁴ W⁻¹ | Phase E re-run, [constants.md §A3](constants.md) |
| `L_passive_PHE` | 15 288 ppm at the Friedenauer corner | BC-A forward-solve, [constants.md §B](constants.md) |
| `L_nonmirror_PHE` | 11 888 ppm (held fixed; inherited from Friedenauer crystal + oven) | BC-A decomposition, [constants.md §B](constants.md) |
| `Σ T_loss_VENDOR_max` | 1 500 ppm summed across M2'/M3'/M4' (allocated 300/300/900) | [bc-c-results.md §C.2](bc-c-results.md) |
| `T_IC_opt` Low (0.5 W) | 17 565 ppm | [bc-b-results.md §F](bc-b-results.md) |
| `T_IC_opt` High (1.5 W) | 22 945 ppm | [bc-b-results.md §F](bc-b-results.md) |
| **T_IC single-variant centre (frozen)** | **19 965 ppm ± 500 ppm** | [bc-b-results.md §F.2](bc-b-results.md) (equal-penalty / minimax) |
| `L_total` operating point | 13 388 ppm (intermediate IBS, 500 ppm/mirror) | [bc-b-results.md §F](bc-b-results.md) |

---

## C · Phase index

| Phase | What landed | Artefact |
|---|---|---|
| **BC-A** | Loss-model normalisation gate; γ pinned; three-row `L_passive` separation; literature-gap call (path 2 adopted); intensity envelope; NG-D consistency check | [`bc-a-log.md`](bc-a-log.md) + [`constants.md`](constants.md) |
| **BC-B** | Impedance-match grid 2 scenarios × 4 `L_total` points; sensitivity columns; §6 Q2 resolved to *one* M1' variant; tolerance band recommendation ±500 ppm | [`bc-b-log.md`](bc-b-log.md) + [`bc-b-results.md`](bc-b-results.md) + [`notebooks/exploration/`](../../notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py) (promoted at BC-F) |
| **BC-C** | Per-mirror coating targets (300/300/900 ppm allocation, Friedenauer 3:1 dichroic ratio); AOI bands; substrate; LIDT hand-forward to BC-D | [`bc-c-log.md`](bc-c-log.md) + [`bc-c-results.md`](bc-c-results.md) |
| **BC-D** | LIDT margin per mirror at 1.5 W; M4' material tier (HfO₂ / SiO₂ default, ZrO₂ / SiO₂ alt, LaF₃ / MgF₂ on CaF₂ upgrade, no Nb₂O₅ / TiO₂); G2-conditional service-life envelope; MIL-STD-1246C cleanliness clause | [`bc-d-log.md`](bc-d-log.md) + [`bc-d-results.md`](bc-d-results.md) |
| **BC-E** | Five vendor-facing pages in [`specs/`](specs/) (M1'–M4' + cover letter) | [`bc-e-log.md`](bc-e-log.md) + [`specs/`](specs/) |
| **BC-F** | Steward review + freeze; notebook promotion; cross-links; this closure document | [`bc-f-log.md`](bc-f-log.md) + this file |

Calendar: workplan estimate ~ 4.5 days focused. Actual ~ 1 calendar
day (BC-A 1 day; BC-B / BC-C / BC-D / BC-E / BC-F each within
half-day to single-day). The compressed calendar was possible because
no vendor contact and no external lit-pass were on the critical path;
all phases consumed dossier-extracted numbers plus the `/src/`
primitives.

---

## D · Open items (handed to the procurement KD)

These items are **out of scope** of this WP and belong to the
procurement KD downstream (KD-UV280-005 / -007):

1. **Vendor shortlist + quote intake.** Send the
   [`specs/`](specs/) package to several coating houses
   (Layertec / Laseroptik / ATFilms / MLD / Manx Precision Optics /
   any house the steward names). Quote-comparison criteria: price,
   lead time, M4' dichroic stack design quality, ITAR / EAR
   considerations. Cover letter §H specifies the quote-format
   requests.
2. **Vendor selection + ordering.** Award contract against the
   frozen specs.
3. **Receipt inspection.** Verify cleanliness, scratch / dig, R/T
   against the per-mirror sheets. The MIL-STD-1246C Class 100
   clause is a procurement-acceptance condition (cover letter §G).
4. **Bench installation + cavity-finesse measurement.** Reconcile
   the as-built cavity loss against BC-B's `L_total = 13 388 ppm`
   operating point and `T_IC = 19 965 ± 500 ppm` tolerance.
5. **G2 measurement at install.** Monitor M4' loss-rate increase
   under the 1.5 W operating scenario for 100+ h. Outcome closes
   the G2-conditional escalation paths in cover letter §F.

---

## E · Open items (queued literature follow-ups; non-blocking)

These items would tighten BC-A / BC-B / BC-D inputs if landed, but
are not blocking the procurement KD:

1. **Burkley2021 numerical extraction.** PDF locally staged;
   `extracted.yaml` exists with empty `parameters` block. Extracting
   the intracavity power, finesse, spot size at the mirrors, and
   time-to-failure curves would tighten BC-D's service-life envelope
   on M4'.
2. **Hannig2018 numerical extraction.** Same — the 130-hour 313 nm
   CW result is a useful unextracted operational-lifetime data
   point.
3. **IBS HR 559 nm coating-loss anchor.** BC-A's path-1 literature
   pass returned empty in extracted form; a targeted lit pass
   (Layertec / Laseroptik measured-loss publications, ATFilms /
   MLD measured-loss papers) would tighten `T_loss_VENDOR_max`
   below the 1 133 ppm Friedenauer-floor allocation.
4. **Post-2020 BBO d_eff anchor.** d_eff bracket 1.30–1.60 pm/V
   is the binding γ uncertainty axis (BC-B §E.2); a tighter
   measurement would shift the `T_IC_opt` centre by up to
   ~ 1 000 ppm at the High scenario.

---

## F · G2-conditional escalation paths (carried in cover letter §F)

The WP closes with three forward-looking escalation paths conditional
on the eventual G2 measurement:

1. **If M4' service-life matches the Kondo / Kubota ~ 1 000-hour
   envelope:** baseline path holds. Build proceeds at 1.5 W upstream
   if available, else at 0.5 W; both scenarios LIDT-acceptable on
   the spec'd coating.
2. **If M4' fails at the Burkley fluoride-class envelope (i.e.,
   oxide coatings die faster than the dossier suggests):** re-spec
   M4' toward the **LaF₃ / MgF₂ on CaF₂ multilayer** upgrade tier
   (cover letter §B). This is a single-page re-quote, not a full
   WP re-run.
3. **If M4' fails at the Burkley oxide-class envelope under our
   fluence (minutes-to-hours):** the 1.5 W scenario becomes
   architecturally untenable. Build moves to **0.5 W scenario only**;
   M1' page re-spec'd to T = 17 565 ± 500 ppm centre. M2'/M3'/M4'
   pages unchanged under that escalation.

---

## G · NG-D consistency check (BC-A Deliverable E commitment)

BC-A §E committed to a re-check at BC-F closure. As of 2026-05-20,
[NG-D status in `docs/architectures/next-gen.md`](../../docs/architectures/next-gen.md)
is still **"⏳ pending NG-A"** — no NG-D output has landed since BC-A
opened. The Friedenauer-frozen geometry (`L_BBO = 10 mm`,
`w_0 = 19.4 μm`, `f = 25 mm`) is therefore **unchallenged** at
this closure.

**If NG-D lands after this closure and recommends a different `f`**
the BC-E spec sheets (specifically the ROC = 50 mm row on M3' and
M4') would need re-quoting. This is logged here as the binding
geometric-dependency risk for the procurement KD.

---

## H · Charter compliance summary

- **§1.5 Levels 0 / 1.** Untouched. The two scenarios bracket the
  upstream LBO-output uncertainty, not the §1.5 UV anchor.
- **§5.1 anti-seeding.** All numerical work consumes architecture-
  neutral primitives in `/src/` ([`enhancement_cavity`](../../src/enhancement_cavity.py),
  [`shg_single_pass`](../../src/shg_single_pass.py),
  [`boyd_kleinman`](../../src/boyd_kleinman.py),
  [`abcd`](../../src/abcd.py)). No commit to `/src/` from this WP.
  BC-B notebook promoted from this folder to
  [`/notebooks/exploration/`](../../notebooks/exploration/) at
  BC-F per §6 Q8.
- **G1 (14-GHz unlockable domain).** Inherited unchanged from
  Friedenauer's crystal + cavity geometry; coating choices do *not*
  introduce or resolve G1. Spec sheets carry the one-line
  inheritance note.
- **G2 (UV-induced degradation at 280 nm).** Remains OPEN. The
  service-life envelope in BC-D §C.4 is conditional on G2 closure
  measurement (procurement KD §D item 5).
- **G3 (Phase 0.5 reference triple).** Closed 2026-05-01; unaffected
  by this WP.
- **Coastline / Sail.** This WP is *Sail* — exploratory parameter
  optimisation on a chosen architecture. Inputs (Friedenauer
  geometry, dossier-extracted constants) are *Coastline*; spec
  sheets remain advisory until vendor quotes return and the
  procurement KD closes.

---

## I · Cross-references added at closure

- [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D.6 — pointer to this WP and the
  new-build spec sheets.
- [`docs/components/inventory.md`](../../docs/components/inventory.md) §B — pointer to the new coating spec for
  the BBO-stage seats, with a "none of the on-shelf candidate rows
  are drop-in matches" note.
- [`notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py`](../../notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py) —
  BC-B notebook promoted from this folder; carries explicit
  back-references to [`constants.md`](constants.md) §A3 / §F as
  the sole γ / L authority.

---

## J · Sign-off

Steward sign-off on the five spec pages: **frozen 2026-05-20.**

WP closes here. The act of *sending* the quote package to coating
houses is the first deliverable of the downstream procurement KD,
not part of this WP.

---

**Workplan v3 acceptance criteria (§9) — final check:**

1. ✅ BC-B notebook reproduces P_UV = 0.275 W within 5 % at the
   Friedenauer corner with the BC-A-pinned `(L_PHE, γ_PHE)`
   (residual: −0.00 % to display precision; passes acceptance gate
   #1 in [`bc-b-results.md`](bc-b-results.md) §A).
2. ✅ Five spec sheets under [`specs/`](specs/) carry explicit R/T
   targets, tolerance bands, AOI, polarization, substrate, LIDT
   margin, quantity, and the (single-variant resolved) M1'
   column structure.
3. ✅ This `closure.md` records the frozen spec set, the open items
   deferred to vendor-quote time, and cross-links from
   [`docs/components/inventory.md`](../../docs/components/inventory.md) §B and [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D.6.
4. ✅ The mechanical anti-seeding scan still passes
   ([`tests/test_anti_seeding_src_imports.py`](../../tests/test_anti_seeding_src_imports.py),
   142/142 last green; no `/src/` change in this WP).
5. ✅ **No vendor inquiry has been sent.** Sending an inquiry is
   the downstream procurement KD's first deliverable.
