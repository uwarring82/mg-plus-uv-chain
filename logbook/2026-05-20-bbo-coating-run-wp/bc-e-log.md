# BC-E · Spec-sheet drafting — running log

**Phase:** BC-E of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20 (after BC-D closure same day)
**Status:** CLOSED 2026-05-20 — BC-F (steward review + freeze) unblocked

This log accumulates entries as BC-E assembles the five vendor-facing
spec pages from the four upstream artefacts.

---

## 2026-05-20 · Kickoff

BC-D closed within the calendar day (see [`bc-d-log.md`](bc-d-log.md));
the steward greenlit BC-E start. BC-E opens against **four pinned
upstream authorities**:

| Source | What BC-E consumes |
|---|---|
| [`constants.md`](constants.md) §F | γ_SHG_BBO, L_passive_PHE, L_nonmirror_PHE, mirror loss-budget envelope |
| [`bc-b-results.md`](bc-b-results.md) §F | M1' single-variant centre = 19 965 ppm ± 500 ppm; per-scenario optima 17 565 / 22 945 ppm |
| [`bc-c-results.md`](bc-c-results.md) §D | Per-mirror nominal R/T targets, AOI bands, substrate, ROC / CA / wedge / flatness floors |
| [`bc-d-results.md`](bc-d-results.md) §C, §E, §F.2 | LIDT margin paragraph per mirror, material recommendation, cleanliness clause, G2-conditional escalation paths |

**BC-E scope recap** (from [`workplan.md`](workplan.md) §4 Phase BC-E):

Five vendor-ready pages inside [`specs/`](specs/):

- `M1-input-coupler.md` — plane impedance-coupled IC, single-variant
  centre (§6 Q2 resolved at BC-B).
- `M2-plane-HR.md` — plane HR @ 559 nm (HC servo seat).
- `M3-curved-HR.md` — curved HR @ 559 nm.
- `M4-curved-OC-dichroic.md` — curved dichroic; the most
  differentiated of the four.
- `coating-run-cover-letter.md` — six callouts (AOI band, substrate,
  quantity math, LIDT margin, AR bandwidth, T_IC justification)
  plus three BC-D additions (cleanliness, M4' material tier,
  G2-conditional escalation paths).

Per-page template specified in [`workplan.md`](workplan.md) §4 BC-E
(reflectivity in ppm with pp in parentheses; per-surface LIDT on M4';
quantity per variant or per role per [`workplan.md`](workplan.md) §6 Q5).

**Acceptance** (from [`workplan.md`](workplan.md) §4 BC-E):

Five short pages under `specs/` that a coating-house engineer can read
in ~ 5 min, with explicit tolerance bands and LIDT margins. Cover
letter explains why two scenarios exist (now resolved to one M1'
variant per §6 Q2) and why the new T_IC targets sit *above* the
Friedenauer-2006 reference.

**Plan of attack.**

1. Draft M1' page (only scenario-coupled element; uses 19 965 ppm
   centre + ±500 ppm tolerance; per-scenario optima as informational
   rows below the primary spec).
2. Draft M2' page (plane HR, R ≥ 99.970 %, flatness load-bearing).
3. Draft M3' page (curved HR, AOI 13.7° ± 1.5° band, R ≥ 99.970 %).
4. Draft M4' page (curved dichroic, dual-WL spec, material tier
   recommendation, per-surface LIDT).
5. Draft cover letter (six workplan callouts + three BC-D additions).
6. Close this log.

Each step appended below as a dated sub-section.

---

## 2026-05-20 · BC-E executed and closed (single calendar day)

### Step 1 — Folder structure

Created [`specs/`](specs/) subfolder; populated five vendor-facing
pages:

- [`specs/M1-input-coupler.md`](specs/M1-input-coupler.md) — plane IC
- [`specs/M2-plane-HR.md`](specs/M2-plane-HR.md) — plane HR (piezo seat)
- [`specs/M3-curved-HR.md`](specs/M3-curved-HR.md) — curved HR
- [`specs/M4-curved-OC-dichroic.md`](specs/M4-curved-OC-dichroic.md) — dichroic OC
- [`specs/coating-run-cover-letter.md`](specs/coating-run-cover-letter.md) — eight-section cover letter

### Step 2 — Per-mirror page mapping from BC-C / BC-D

Each per-mirror page maps directly to its
[`bc-c-results.md`](bc-c-results.md) §D row with the BC-D LIDT
paragraph attached:

| Page | Front-face spec | LIDT (CW, surface) | Inherited from |
|---|---|---|---|
| M1' | T = 19 965 ppm ± 500 ppm @ 559 nm, AOI ~ 0° | ≥ 500 kW/cm² @ 559 (~ 3 × margin) | BC-B §F (centre), BC-C §D.1, BC-D §C.1 |
| M2' | R ≥ 99.970 % @ 559 nm, AOI ~ 0° | ≥ 500 kW/cm² @ 559 (~ 3 × margin) | BC-C §D.2, BC-D §C.1 |
| M3' | R ≥ 99.970 % @ 559 nm, AOI 13.7° ± 1.5° p-pol | ≥ 250 kW/cm² @ 559 (~ 4 × margin) | BC-C §D.3, BC-D §C.1 |
| M4' | R ≥ 99.910 % @ 559 AND T ≥ 95 % @ 280, AOI 13.7° ± 1.5° p-pol | ≥ 250 kW/cm² @ 559 AND ≥ 5 kW/cm² @ 280 (~ 4 × / 8 × margins) | BC-C §D.4, BC-D §C.2 / §C.3 |

LIDT specs are stated **per surface** on M4' (front dichroic vs back
AR), per the workplan §3 / §4 update. All per-mirror pages carry the
**material-class exclusion** (no Nb₂O₅ or TiO₂) and the IBS-deposition
requirement explicitly; the M4' page adds the full tiered
material-recommendation block (default HfO₂ / SiO₂; alt ZrO₂ / SiO₂;
upgrade LaF₃ / MgF₂ on CaF₂; no silica cap).

### Step 3 — Cover-letter eight-section structure

The cover letter ([`coating-run-cover-letter.md`](specs/coating-run-cover-letter.md))
carries the six callouts the workplan v3 prescribed (§6 Q3 / Q5 / Q6,
plus AOI band, T_IC justification, LIDT margin) and three BC-D
additions (cleanliness clause, material recommendation, G2-conditional
escalation paths):

| § | Callout | Source |
|---|---|---|
| A | AOI band 13.7° ± 1.5° p-pol on curved; ~ 0° ± 1° on plane — chosen procurement spec, not bench-measured | BC-C §D.3 / §D.4, workplan §4 BC-C |
| B | M4' material tier (default HfO₂ / SiO₂; alt ZrO₂ / SiO₂; upgrade LaF₃ / MgF₂ on CaF₂; excluded Nb₂O₅ / TiO₂; no silica cap) | BC-D §C.3 |
| C | One M1' variant covers both upstream scenarios (§6 Q2 resolved at BC-B); equal-penalty centre 19 965 ppm ± 500 ppm with ~ −0.68 % UV penalty per scenario | BC-B §F, workplan §6 Q2 |
| D | Why T_IC sits *above* Friedenauer-2006 reference: at the BC-A-pinned `(L_passive_PHE, γ_PHE)`, impedance-match optimum is 21 700 ppm — Friedenauer procured 16 000 ppm and forfeited ~ 3.6 % UV buildup. New build spec'd at the optimum | BC-A §A3 / §B, BC-B §A gate 2 |
| E | Narrow-band AR @ 280 nm default (CW chain locked at Δ_ref = 40 GHz, no broadband need); broadband 250–300 nm as optional upgrade line item | Workplan §6 Q6, BC-C §F |
| F | LIDT margin + G2-conditional escalation paths (fluoride upgrade if oxide fails; 0.5 W-only scenario if oxide *minutes* failure) | BC-D §C.4 / §F.2 |
| G | **Cleanliness on delivery: MIL-STD-1246C Class 100 or better** — procurement-acceptance condition, load-bearing | BC-D §E + §H finding 5 |
| H | Quote format / timeline (lead time, validity, currency, incoterms, ITAR, cleanliness upgrade, vendor-catalog references) | Steward-defined; standard procurement |

### Step 4 — Acceptance gate review

Workplan §4 BC-E acceptance: *"Five short pages under `specs/` that a
coating-house engineer can read in 5 min, with explicit tolerance
bands and LIDT margins."* Achieved.

**BC-E closed 2026-05-20.** Calendar: single working day (workplan
estimate 1 day; actual ~ matches). No `/src/` change; no notebook
commit; no MEMORY.md update; no vendor contact.

**BC-F (steward review + freeze) is unblocked.** Steward action
items for BC-F (per workplan §4 BC-F):

1. Read the five pages end-to-end as a coating-house reviewer
   would; flag any unclear / unworkable / conflicting language.
2. Confirm the §6 Q1 input-power scenarios (0.5 W / 1.5 W) are
   still the right pair; revisit only if upstream LBO situation
   has changed since 2026-05-20.
3. Confirm the §6 Q2 single-M1'-variant resolution stands (no
   coating-house quote pushback expected at this Δ).
4. Confirm the §6 Q3 / Q5 / Q6 defaults (Herasil throughout,
   N = 4 per role, narrow-band AR) match the steward's procurement
   preferences.
5. Confirm the cover-letter §H quote-format requests
   (lead time, currency, incoterms, ITAR) match the procurement-KD
   downstream expectation.
6. Sign-off, then either: (a) write `closure.md` and proceed to
   send the quotes; or (b) defer sending until the procurement KD
   names the vendor shortlist.

### Surprising findings to flag for the steward

1. **The M4' page is by far the longest and most-differentiated of
   the four.** It carries the only material-tier recommendation,
   the only G2-conditional clauses, and the only "per-surface" LIDT
   spec. This is the page coating houses will engage with most
   deeply; the other three are vendor-catalog-routine.
2. **The cleanliness clause (cover letter §G) is the single
   highest-leverage procurement detail.** Brown2019's 3–6
   orders-of-magnitude LIDT-drop result under particulate
   contamination means that *all* the material-class and
   deposition-method discussion is downstream of getting clean
   optics to the bench. The clause is phrased explicitly as a
   procurement-acceptance condition.
3. **No two-M1'-variant branch.** §6 Q2 resolved to one variant
   at BC-B. The cover letter §C carries the rationale; the
   coating houses should not push back on this — Δ`T_IC_opt`
   between the two scenarios (0.54 pp) is well within typical
   single-run vendor tolerance.
4. **T_IC = 19 965 ppm = 2.00 %** is approximately the *round
   number* near the equal-penalty centre. This is a numerical
   convenience for the cover-letter narrative and for the coating
   house ("two percent transmission" reads cleaner than
   "19 965 ppm transmission").

### Open items handed to BC-F + procurement KD

(Most of these have been queued through earlier phases; restated
here for the BC-F review.)

To BC-F (steward):
- Sign-off on the five pages.
- Decision: send-quote-now vs procurement-KD-shortlist-first.
- `closure.md` drafting (workplan §4 BC-F deliverable).
- Cross-links to add at closure:
  [`docs/components/inventory.md`](../../docs/components/inventory.md) §B and
  [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D.1.
- BC-B notebook promotion from this folder to `/notebooks/exploration/`.

To the procurement KD (downstream of BC-F):
- Vendor shortlist (Layertec / Laseroptik / ATFilms / MLD / Manx
  / others).
- Quote intake, comparison, vendor selection.
- Order placement against the frozen specs.
- Receipt inspection (verify cleanliness, scratch / dig, R/T against
  the per-mirror sheets).
- Bench installation + cavity-finesse measurement; reconcile against
  BC-B's T_IC ± 500 ppm tolerance + the L_total operating point.
- **G2 measurement at install:** monitor M4' loss-rate increase
  under the 1.5 W operating scenario for 100+ h. Outcome closes
  the G2-conditional escalation paths in cover letter §F.

---
