# BC-F · Steward review and freeze — running log

**Phase:** BC-F of the BBO coating-run WP
([`workplan.md`](workplan.md))
**Steward:** Ulrich Warring
**Opened:** 2026-05-20 (after BC-E closure same day)
**Status:** CLOSED 2026-05-20 — **WP CLOSED**

This log records the steward review pass and the WP-closure
artefacts (closure.md, notebook promotion, cross-links).

---

## 2026-05-20 · Kickoff

BC-E closed within the calendar day (see [`bc-e-log.md`](bc-e-log.md));
the steward greenlit BC-F start. BC-F is the **WP-closure phase**:

**BC-F scope** (from [`workplan.md`](workplan.md) §4 Phase BC-F):

- Steward sign-off on the five
  [`specs/`](specs/) pages (M1' / M2' / M3' / M4' + cover letter).
- Write `closure.md` recording the frozen specs, open items deferred
  to vendor-quote time, and the next decision gate
  (KD-UV280-005 / -007 procurement).
- Cross-links added to
  [`docs/components/inventory.md`](../../docs/components/inventory.md) §B and
  [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) §D.6
  pointing at the new spec sheets.
- Promote the BC-B notebook from
  `logbook/2026-05-20-bbo-coating-run-wp/notebooks/` to
  `/notebooks/exploration/` (workplan §6 Q8).
- Re-check NG-D status against BC-A Deliverable E commitment.

**Acceptance** (from [`workplan.md`](workplan.md) §4 BC-F):

- Steward sign-off on the spec sheets. **The WP closes here.**
- The act of *sending* the inquiry to a vendor is a separate decision
  (and arguably belongs to a procurement KD), not part of this WP.

**Plan of attack.**

1. NG-D re-check (BC-A Deliverable E commitment).
2. Promote BC-B notebook with `git mv` to preserve history;
   update relative-path references that break under the move.
3. Add cross-links to dossier pages and to a new
   `notebooks/exploration/README.md` if needed.
4. Write `closure.md` (the WP-closure artefact; this file does
   *not* duplicate the per-phase results but acts as the index +
   handoff to the procurement KD).
5. Close this log.
6. Commit + push (steward call on commit granularity).

Each step appended below as a dated sub-section.

---

## 2026-05-20 · BC-F executed and closed (half-day)

### Step 1 — NG-D re-check (BC-A Deliverable E commitment)

[`docs/architectures/next-gen.md`](../../docs/architectures/next-gen.md)
status as of 2026-05-20: NG-D is **"⏳ pending NG-A"** — unchanged
since BC-A opened (same calendar day). No NG-D output has landed
that could challenge the Friedenauer-frozen geometry used here.
**Re-check trivially passes** — geometry stands; ROC = 50 mm rows on
M3' / M4' are not at risk.

Forward-looking dependency logged in [`closure.md`](closure.md) §G:
if NG-D eventually recommends a different `f` after this closure,
the BC-E spec sheets would need re-quoting. The procurement KD
inherits this risk.

### Step 2 — BC-B notebook promotion

[`logbook/2026-05-20-bbo-coating-run-wp/notebooks/2026-05-20-bbo-ic-impedance-match.py`](../../notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py)
moved via `git mv` to
[`notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py`](../../notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py).
The move:

- Preserves git history (rename detected).
- Removes the now-empty WP-internal `notebooks/` subfolder.
- Required updating the markdown cross-link paths inside the
  notebook header (lines 23, 34, 70 in v1) to the new relative
  positions from `/notebooks/exploration/`:
  `../constants.md` → `../../logbook/2026-05-20-bbo-coating-run-wp/constants.md`
  (3 occurrences); same for `../workplan.md`.
- Smoke-tested the promoted file from its new location:
  notebook runs end-to-end, all three acceptance gates pass
  (forward cross-check residual −0.00 %; T_IC_opt = 0.0217;
  grid populated; w_curved = 255 μm; default I_curved = 64.2 kW/cm²
  at the 1.5 W cell).
- Added a one-paragraph **"Origin"** block to the notebook header
  noting the BC-B → BC-F promotion path and date.

### Step 3 — Cross-links

Two pointers added at WP closure:

- [`docs/components/friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md)
  **§D.6** — paragraph noting the new build's coating-run WP,
  the spec-sheet location, and the headline finding that
  Friedenauer ran ~ 0.6 pp below the impedance-matched optimum.
- [`docs/components/inventory.md`](../../docs/components/inventory.md)
  **§B intro** — pointer to the new spec sheets, with the frozen
  M1'–M4' R/T targets summarised in-place. Includes the note that
  none of the on-shelf candidate rows below are drop-in matches
  for the new spec (T_IC ±500 ppm tolerance, curved-seat AOI band,
  and M4' dichroic dual-WL requirement together exceed what the
  on-shelf inventory carries).

No update to [`notebooks/README.md`](../../notebooks/README.md) —
file does not exist; no `README.md` convention is established in the
`/notebooks/` tree (only the per-subfolder organisation:
`diagnostic/`, `tutorials/`, and now `exploration/`). Creating a
project-wide notebooks README is **out of scope** of this WP and
would itself be a documentation task. Logged here as a one-line
future task if the notebooks tree grows.

### Step 4 — closure.md drafted

[`closure.md`](closure.md) — the WP-closure artefact — assembled
from the per-phase results files. Sections:

- §A frozen specifications + cover letter
- §B quantitative pins (canonical references)
- §C phase index
- §D open items handed to the procurement KD
- §E open items queued literature follow-ups (non-blocking)
- §F G2-conditional escalation paths
- §G NG-D consistency check
- §H Charter compliance summary
- §I cross-references added at closure
- §J sign-off + final v3 acceptance-criteria check

The acceptance-criteria check at §J confirms all five workplan v3
acceptance criteria pass (P_UV cross-check, five sheets in place,
closure.md exists, anti-seeding scan unchanged, no vendor inquiry
sent).

### Step 5 — Acceptance gate review

| Workplan §4 BC-F gate | Status |
|---|---|
| Steward sign-off on the five spec pages | ✅ Frozen 2026-05-20 |
| `closure.md` records frozen specs + open items + decision gate | ✅ §D points at the procurement KD |
| Cross-links to [`inventory.md`](../../docs/components/inventory.md) + [`friedenauer-baseline.md`](../../docs/components/friedenauer-baseline.md) | ✅ Added in §B-intro and §D.6 |
| BC-B notebook promoted to `/notebooks/exploration/` (workplan §6 Q8) | ✅ Via `git mv`; relative paths updated; smoke-tested |
| WP closes here; no vendor inquiry sent | ✅ Acceptance condition explicit in `closure.md` §J |

**BC-F closed 2026-05-20.** Calendar: half-day (workplan estimate
0.5 day; actual ~ matches).

**THE BBO COATING-RUN WP IS CLOSED.** Next decision gate is the
downstream procurement KD (KD-UV280-005 / -007), which is **not**
opened by this log; that is a separate steward action when ready.

### Surprising findings to flag for the steward

1. **BC-A → BC-F closed in one calendar day.** The compressed
   schedule was possible because every phase consumed
   dossier-extracted numbers + the `/src/` primitives; no vendor
   contact, no external lit-pass, no bench measurement on the
   critical path. The workplan's 4.5-day estimate budgeted for
   the possibility that path-1 literature extraction or vendor
   pre-inquiry would land on the critical path — neither did.
2. **No re-quote needed.** All five BC-F gates pass; no
   mid-quote re-spec is anticipated. Cover letter §F's
   G2-conditional escalation paths handle the *post*-quote
   scenarios where the M4' coating underperforms.
3. **The BC-B notebook is the only `/src/`-promoted artefact from
   this WP.** All other deliverables live inside the WP folder
   and are referenced from the dossier pages but not promoted to
   the project's primary documentation tree. This is
   intentional — the spec sheets are advisory until a
   procurement KD closes downstream.

### What's preserved for the next iteration of this kind of WP

1. **The phase-gate template** (BC-A loss-model normalisation →
   BC-B impedance match → BC-C per-mirror allocation → BC-D LIDT
   → BC-E spec sheets → BC-F closure) is reusable for any future
   coating-run WP at any cavity stage. The BC-A loss-model
   normalisation gate is the load-bearing structural move that
   resolved the v1 reviewer-flagged inconsistency.
2. **The forward cross-check acceptance pattern** (reproduce one
   measured published number within X %; report any
   optimum-finding as a *finding*, not a check) is the v3
   reviewer-driven correction worth preserving.
3. **The honest dossier handling** (acknowledge SCAFFOLD-tier
   sources; do not over-claim margins beyond what extracted-tier
   data supports; use Brown2019 as screening, not literal
   pass/fail at 559 nm) — three reviewer rounds of corrections
   landed this pattern.
4. **The single-γ-authority pattern** (`constants.md` consulted,
   not regenerated) prevents the BC-A/BC-B `T_IC = 0.016` vs
   `T_IC_opt = 0.022` inconsistency from re-appearing in future
   WPs.

---
