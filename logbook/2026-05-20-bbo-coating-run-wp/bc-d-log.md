# BC-D · LIDT and substrate constraints — running log

**Phase:** BC-D of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20 (after BC-C closure same day)
**Status:** CLOSED 2026-05-20 — BC-E unblocked

This log accumulates entries as BC-D executes against the per-mirror
peak-intensity table in [`bc-c-results.md`](bc-c-results.md) §E.

---

## 2026-05-20 · Kickoff

BC-C closed within the calendar day (see [`bc-c-log.md`](bc-c-log.md));
the steward greenlit BC-D start. BC-D opens against:

| Mirror | Surface | Load (1.5 W scenario) | From |
|---|---|---|---|
| M1' | front (intracavity) | ~ 100–190 kW/cm² CW @ 559 nm (long-arm leg-distribution dependent) | [`bc-c-results.md`](bc-c-results.md) §E |
| M1' | back (input side) | ~ 2–4 kW/cm² CW @ 559 nm | §E |
| M2' | front (HR @ 559 nm) | ~ 100–190 kW/cm² CW @ 559 nm | §E |
| M3' | front (curved HR @ 559 nm, AOI 13.7°) | ~ 65 kW/cm² CW @ 559 nm | §E |
| **M4'** | **front (curved dichroic, AOI 13.7°)** | **~ 65 kW/cm² CW @ 559 nm + ~ 0.6 kW/cm² CW @ 280 nm transit** | §E — binding LIDT case |
| M4' | back (AR @ 280 nm) | ~ 0.6 kW/cm² CW @ 280 nm | §E |

**BC-D scope recap** (from [`workplan.md`](workplan.md) §4 Phase BC-D):

- **Per-mirror LIDT margin** at the higher-stress (1.5 W) scenario,
  evaluated against the dossier LIDT envelopes.
- **Material ranking** for M4' dichroic stack composition,
  driven by Brown2019's bandgap-scaling argument (silica > alumina
  > hafnia > tantala > niobia > titania).
- **Substrate confirmation** (Herasil throughout — already chosen at
  BC-C §G; BC-D confirms the UV-grade + LIDT-compatible justification).
- **Surface-quality envelope** (scratch / dig ≤ 10/5, flatness
  ≤ λ/10 @ 633 nm — BC-D restates the standard cavity-grade floors).
- **Flag any scenarios that exceed published LIDT margins** —
  de-rate UV target or escalate to steward.

**Acceptance** (from [`workplan.md`](workplan.md) §4 BC-D):

A LIDT-and-substrate paragraph per mirror, attached to the BC-C row.
Scenarios exceeding LIDT margins are flagged.

**Dossier inventory** (per BC-C §E and BC-A §C path-1 follow-up):

| Source | Status | What it gives BC-D | What it does *not* give |
|---|---|---|---|
| [`Burkley2021`](../../data/literature/Burkley2021/notes.md) | SCAFFOLD (PDF staged; `extracted.yaml` exists but no numerical extraction yet — `parameters` block empty) | Closest published-wavelength CW UV cavity-mirror lifetime data (oxide vs fluoride at ~ 244 nm). Triggers a numerical-extraction pass if the 1.5 W scenario sits near survival envelope | Bench-measured 280 nm LIDT (G2-OPEN; needs full numerical extraction to confirm 244 nm → 280 nm scalability) |
| [`Brown2019`](../../data/literature/Brown2019/notes.md) | DRAFT (numerical extraction complete) | Bandgap-scaling model for contamination-driven LIDT lowering; material ranking silica > alumina > hafnia > tantala > niobia > titania | Absolute LIDT thresholds (the 1070 nm test bench is wavelength-non-portable). Only the *mechanism* is portable |
| [`Turcicova2022`](../../data/literature/Turcicova2022/notes.md) | DRAFT (secondary literature) | BBO + CLBO LIDT review; AR-coating LIDT lowering (multi-WL vs single-WL); IBS > magnetron / PLD / e-beam ranking | Direct HR-coating 559 nm loss data; primary LIDT measurements (it's a review, source-tier `S`) |
| [`Kondo1998`](../../data/literature/Kondo1998/notes.md) / [`Kubota1998`](../../data/literature/Kubota1998/notes.md) | (referenced by Turcicova / Hannig) | 266 nm CW operational lifetime: 1 000 h with 5 × 10⁻⁵ %/h cavity-loss-rate increase at 260 W/cm² UV power density | Below-1000 h timescales; coating-class breakdown |
| [`Hannig2018`](../../data/literature/Hannig2018/notes.md) | SCAFFOLD | 313 nm CW operational lifetime: 130 h, no power decay observed | Coating breakdown threshold; 280 nm-specific data |

**Plan of attack.**

1. Read the available extracted numbers from Brown2019 + Turcicova2022
   to anchor the *mechanism* + *material-ranking* argument.
2. Compute LIDT margin per mirror at the 1.5 W scenario, using:
   - Brown2019 bandgap-scaling for the M4' material recommendation
   - Turcicova2022 multi-WL-AR LIDT-lowering envelope for the M4'
     dichroic stack
   - Burkley2021's qualitative oxide-vs-fluoride survival data at
     244 nm as the closest-wavelength UV survivability benchmark
3. Note where the dossier is silent (G2-OPEN at 280 nm; no extracted
   559 nm HR LIDT) and produce a *conditional* service-life
   envelope rather than a measured one.
4. Confirm Herasil substrate choice from BC-C §G against the
   UV-transmission + bulk-absorption + scatter-uniformity arguments.
5. Restate the standard cavity-grade surface-quality + flatness
   floors for the BC-E spec-sheet template.
6. Write `bc-d-results.md` as a per-mirror LIDT-and-substrate
   paragraph anchored to the BC-C handoff structure.
7. Flag any scenarios exceeding LIDT margins → de-rate or escalate.

Each step appended below as a dated sub-section.

---

## 2026-05-20 · BC-D executed and closed (half-day)

### Step 1 — Dossier numerical sweep

Three key sources read end-to-end:

- **Brown2019 (DRAFT, extracted):** bandgap-scaling LIDT data at
  1070 nm CW with carbon/steel particulate contamination. Material
  ranking silica > alumina > hafnia > tantala > niobia > titania.
  Numerical λ/2 LIDT runaway thresholds: silica > 17 800 kW/cm²
  (no damage at highest tested), alumina 6 300, hafnia 3 800,
  tantala 1 600 kW/cm². **Wavelength-non-portable** — only the
  mechanism + ranking are.
- **Burkley2021 (SCAFFOLD):** 244 nm UV cavity-mirror lifetime data
  in UHV. Oxide (HfO₂/Al₂O₃/SiO₂) coatings die in minutes at
  ~ 5 W intracavity in UHV; fluoride (MgF₂/LaF₃/CaF₂) survives
  10 W for hours in O₂-rich atmosphere. **Closest-wavelength UV
  cavity-mirror lifetime data**; numerical full extraction queued
  (still SCAFFOLD).
- **Turcicova2022 (DRAFT, secondary):** BBO LIDT review.
  IBS > magnetron > e-beam > PLD for damage tolerance. Mixture
  coatings (ZrO₂-SiO₂) > discrete Al₂O₃/SiO₂ at 355 nm. Multi-WL
  AR ~ 20 % lower than single-WL AR. Single CW BBO data point in
  Fig. 1b at ~ 1–10 kW/cm² (bulk, not coating; Nikogosyan compendium).
- **Kondo1998 / Kubota1998 (referenced via Turcicova):** 266 nm
  CW BBO operational lifetime: **1 000 h with 5 × 10⁻⁵ %/h
  cavity-loss-rate increase at 260 W/cm² average UV power
  density**. Closest CW UV operational benchmark.
- **Hannig2018 (SCAFFOLD):** 313 nm CW BBO ring, 130 h with no
  power decay observed. Longer wavelength than ours but a useful
  CW UV operational data point.

### Step 2 — Per-mirror margin analysis

Computed inline; full table → [`bc-d-results.md`](bc-d-results.md) §C.

**Headline margins at 1.5 W scenario:**

- **559 nm axis (all four mirrors):** Worst-case 190 kW/cm² peak on
  M1' / M2'. **Screening comparison** against Brown2019 1070 nm
  thresholds (mechanism + bandgap-ranking portable; absolute
  thresholds are *not* portable across wavelengths): 8.4 × vs
  tantala, 20 × vs hafnia, > 94 × vs silica. **All four mirrors
  comfortably below the visible-axis envelope** under conservative
  wavelength-scaling pessimism.
- **280 nm axis (M4' only):** 0.6 kW/cm² peak / ~ 0.3 kW/cm² avg on
  M4' front transit + M4' back AR. Sits **~ 1.15 × *above*** the
  Kondo / Kubota 1 000-hour 266 nm CW operating point on bulk BBO
  — i.e., **on the same order of magnitude, not below**.
  Burkley2021 numerical fluence comparison is **not** admissible
  (SCAFFOLD; no extracted mirror spot / fluence in the dossier).
  **The 280 nm axis is the binding LIDT case of this WP**, with
  service-life expectation *on the order of* the Kondo / Kubota
  1 000-h envelope.

### Step 3 — Material ranking for M4' dichroic stack

Per Brown2019 bandgap scaling + Turcicova2022 deposition ranking:

- **High-index:** HfO₂ (Eg = 5.8 eV) acceptable; ZrO₂ (Eg = 5.0 eV)
  is a vendor-design alternative; LaF₃ (Eg ~ 11 eV, fluoride) is
  the best-LIDT upgrade option if vendor offers a fluoride-on-FS
  dichroic design. **Avoid Nb₂O₅, TiO₂ entirely.**
- **Low-index:** SiO₂ — universal best choice at this wavelength.
- **Deposition:** **IBS** explicitly. Magnetron / e-beam / PLD all
  worse per Turcicova2022 §4.3.
- **Cap layer:** No thin silica cap needed; Brown2019 showed
  1–5 μm silica caps give zero measurable LIDT improvement under
  particulate contamination.

Cover-letter sentence drafted in [`bc-d-results.md`](bc-d-results.md) §C.3.

### Step 4 — Substrate confirmed

Herasil throughout — UV-grade FS, mandatory on M4' (280 nm
transits), inherited on M1'/M2'/M3' for scatter-uniformity +
procurement-simplicity reasons (BC-C §G). One-line "ordinary
UV-grade FS acceptable on M1'/M2'/M3' as a lead-time fallback"
footnote permitted on those three sheets; **not** on M4'.

### Step 5 — Surface-quality + flatness envelope restated

Standard cavity-grade IBS substrate spec:

- Scratch / dig ≤ 10/5
- Flatness ≤ λ/10 P-V @ 633 nm over CA (plane mirrors;
  load-bearing on M2' for the HC servo seat)
- Surface figure ≤ λ/10 P-V over CA (curved mirrors; not centre-
  only)
- Wedge ≤ 5 arcmin (plane), centring decentre ≤ 5 arcmin (curved)
- CA ≥ 8 mm (~ 30 × beam-radius margin)
- **Cleanliness on delivery: MIL-STD-1246C Class 100 or better**
  (this is the load-bearing Brown2019 detail — particulate
  contamination drops LIDT by 3–6 orders of magnitude; BC-E
  cover letter carries this as a procurement-acceptance
  condition).

### Step 6 — Service-life envelope (G2-conditional)

[`bc-d-results.md`](bc-d-results.md) §C.4:

- **M1'/M2'/M3' (single-WL @ 559):** > 1 000 h, < 1 %/100 h
  loss-rate increase
- **M4' (dual-WL dichroic, binding case):** **100–1 000 h at 1.5 W;
  > 1 000 h at 0.5 W**, with monotonic slow-rate loss accumulation
- **M4' back AR @ 280 nm:** > 1 000 h

All numbers **G2-conditional**: no measured 280 nm coating
lifetime data exists in the dossier at our specific fluence regime;
the envelope is bracketed by Kondo/Kubota above and Burkley below.

### Step 7 — Findings + G2 conditional clauses

[`bc-d-results.md`](bc-d-results.md) §F includes three conditional
clauses for the BC-E cover letter:

- If G2 closes worse than Burkley *fluoride*-class → M4' must be
  re-specced toward LaF₃ / MgF₂ / CaF₂ multilayers.
- If G2 closes worse than Burkley *oxide*-class (= minutes-to-hours
  failure at our fluence) → **WP closes with the 0.5 W scenario
  only**; the 1.5 W scenario becomes architecturally untenable.
- The 100–1 000 h envelope above assumes Friedenauer-class
  operational quality of the new build's M4' coating.

### Step 8 — Acceptance gate review

All five workplan §4 BC-D gates pass; full table →
[`bc-d-results.md`](bc-d-results.md) §A.

**BC-D closed 2026-05-20.** Calendar: half-day (workplan estimate
0.5 day; actual ~ matches). No `/src/` change; no notebook commit;
no MEMORY.md update; no vendor contact.

**BC-E is unblocked** — opens against all four upstream-result
files (constants.md §F + bc-b-results.md §F + bc-c-results.md §D /
§E + bc-d-results.md §C / §E) and assembles five vendor-facing
pages mapped from [`bc-c-results.md`](bc-c-results.md) §D (D.1–D.4
per-mirror tables, structured to map directly to four spec-sheet
pages) + §J (the open-items hand-forward).

### Surprising findings to flag for the steward

1. **No fatal LIDT exceedances** at 1.5 W. The 559 nm axis screens
   adequately against wavelength-pessimistic Brown2019 thresholds.
   **The 280 nm axis is not a margin** — our M4' transit fluence is
   ~ 1.15 × *above* the Kondo / Kubota 266 nm CW 1 000-hour
   benchmark. Both scenarios remain LIDT-acceptable in the
   *order-of-magnitude* sense, subject to the G2 conditional
   clauses below; the 1.5 W scenario service-life expectation is
   *on the order of* (not comfortably below) the Kondo benchmark.
2. **Our 280 nm fluence sits at ~ 1.15 × the Kondo / Kubota
   1 000-hour 266 nm operating point** (slightly above, not below).
   This is the closest-wavelength CW UV operational benchmark in
   the dossier; the ~ 1 × ratio (not 10 ×, not 0.1 ×) is the
   most-actionable data point in the BC-D analysis. **Expect
   service life on the order of the Kondo / Kubota benchmark,
   plausibly somewhat shorter** — not a comfortable margin below.
3. **Operating environment matters** (Burkley2021). The current
   atmospheric / O₂-rich operation favours our coating class;
   any future evacuated-cavity variant would shift the M4'
   material-class recommendation toward fluorides.
4. **Cleanliness on delivery (MIL-STD-1246C Class 100)** is the
   single load-bearing handling specification — Brown2019's
   3–6 orders of magnitude LIDT drop under particulate
   contamination dominates *any* coating-stack choice. The
   BC-E cover letter must carry this explicitly.

### Open items handed to BC-E + procurement KD

(Full table → [`bc-d-results.md`](bc-d-results.md) §F.)

To BC-E:
- LIDT paragraphs ready to paste into per-mirror sheets.
- Material-ranking sentence ready for cover letter.
- Cleanliness clause ready for cover letter as procurement-
  acceptance condition.

To the procurement KD (downstream):
- G2 measurement task: M4' loss-rate vs time at 1.5 W operating
  scenario, monitor 100+ h.
- Burkley2021 + Hannig2018 numerical extraction would tighten
  the service-life envelope (queued, not blocking).

---
