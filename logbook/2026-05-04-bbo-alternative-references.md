# BBO alternative-reference search task — 2026-05-04

## Header (Charter §9 trigger question)

- **Affects Level 0 parameter?** no — task is a literature-search scope, not a Level 0 change
- **Affects Level 1 parameter?** no — bringing in additional references would *tighten* but not retract any current Level 1 envelope
- **Affects success criterion?** no

## Stance attribution

- Task draft: assistant under steward direction
- Tasks A + B dispatched: 2026-05-04 (PDFs provided in-conversation; structured extractions filed as DRAFT)
- Steward sign-off: pending

## Status update — 2026-05-04 evening

Tasks **A** and **B** have been dispatched in a single follow-on session: the steward provided the Eckardt 1990 and Tamošauskas 2018 PDFs in-conversation and the structured extractions are filed as `DRAFT` under [`data/literature/Eckardt1990/`](../data/literature/Eckardt1990/) and [`data/literature/Tamosauskas2018/`](../data/literature/Tamosauskas2018/). Headline outcomes:

- **Task B (Eckardt 1990) — actionable upgrade.** `|d_22(BBO)| = 2.2 pm/V` is **37% higher** than Eimerl 1987's `|d_11| = 1.6 pm/V`, with overlap only at the very edge of Eimerl's ±25% uncertainty envelope. The KDP calibration choice (0.38 vs 0.39 pm/V) cannot account for the 37% revision (it accounts for at most 2.6%). KD-UV280-005 Section C now takes Eckardt as the central d_eff anchor with Eimerl retained as the historical lower bound. The §5 Phase 1 evidence-table BBO d_eff cell was revised from `1.15 (1.10–1.20)` to **`1.44 (1.30–1.60)`** pm/V, with conversion-efficiency-at-fixed-intensity ratio `(1.44/1.15)² = 1.57×` consistent with modern Friedenauer-class observations.
- **Task A (Tamošauskas 2018) — confirmatory cross-check.** The refined three-oscillator Sellmeier (valid 0.188 – 5.2 µm) yields `θ_PM(559 → 280, Type I) = 44.28°` and `ρ = 83.8 mrad`, agreeing with the Eimerl-anchored values within 0.07° and 1 mrad respectively despite ~10⁻³ disagreement in the absolute indices. The Eimerl and Tamošauskas Sellmeier sets are kept as **parallel anchors** in `KD-UV280-005` Section C — neither replaces the other. The 4.62 µm `n_o = n_e` crossover predicted (and experimentally verified in Fig. 4 of the paper) deviates from the Eimerl-extrapolated 5.75 µm crossover, a useful cross-set discriminant for any future mid-IR architecture work.
- **Task C (Kato 1986)** — was scoped as low priority (already partially captured as alternative Sellmeier in Eimerl 1987 Table II); tasks A and B did not surface a discrepancy that would need an independent Kato extraction. Remains a scaffold-only candidate.
- **Task D (Nikogosyan 2005 compendium)** — optional sanity-check; not pursued in this round.
- **Task E (CW-UV LIDT at 280 nm)** — **the only residual binding open item** for `KD-UV280-005` Section C. Now opened as its own logbook entry: [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](2026-05-04-bbo-cw-uv-lidt-task.md). The CW-UV-LIDT literature is structurally different from tasks A/B (no canonical primary source; figure of merit is operational lifetime not single-shot threshold; touches three dossier entries `KD-UV280-005` / `-009` / `-011`); the new entry reframes those distinctions and provides a candidate-reference list ranked by expected payoff.

Cross-set discrepancies are logged in [`data/literature/Eimerl1987/extracted.yaml`](../data/literature/Eimerl1987/extracted.yaml) `cross_check_notes`:
- `d_eff_eckardt1990_vs_eimerl1987` — the 37% upward revision and its candidate explanations.
- `sellmeier_tamosauskas2018_vs_eimerl1987` — the ~8 × 10⁻⁴ visible-band offset between the two Sellmeier-anchor measurement sets.

This logbook entry's "acceptance criteria for closing the task as a whole" (§8 below) remain partially satisfied: A and B are now in the dossier; C and D are scoped and explicitly deferred; E is split out as a separate residual task.

## Context

`KD-UV280-005` Section C is now anchored to a populated `[P:Eimerl1987]` extraction ([`data/literature/Eimerl1987/`](../data/literature/Eimerl1987/), DRAFT, 2026-05-04). The Eimerl 1987 anchor has three soft spots that an alternative reference could tighten:

1. **±25 % uncertainty on `d_11`.** Eimerl 1987 reports `d_11 = 1.6 ± 0.4 pm/V`, measured relative to `d_36(KDP) = 0.39 pm/V`, at 1064 nm SHG only. The dispersion to 559 → 280 nm is asserted to be weak but not measured. A modern absolute-`d_eff` calibration at the actual operating wavelengths would directly tighten the d_eff value for the §5 Phase 1 evidence-table BBO row.
2. **Sellmeier validity range 212.8 – 1064 nm.** The "this work" Eimerl 1987 fit is anchored to data in this band. Both the 280 nm harmonic (well inside) and the 559 nm fundamental (well inside) are covered, so the fit is not extrapolating for our operating point. But a more recent Sellmeier set with extended UV / IR coverage would (a) cross-validate the Eimerl set at 280 nm, and (b) potentially tighten `n(280 nm)` for higher-purity modern crystals where the 215 nm UV edge may sit deeper into the UV.
3. **No CW-UV LIDT at 280 nm.** Eimerl 1987 only reports a 1064 nm / 1 ns / one-on-one bulk damage threshold (13.5 J/cm²). The CW-UV photo-induced surface degradation regime that governs operational lifetime at 280 nm is not in this paper. This is a *separate-paper* gap, not an Eimerl 1987 follow-up.

This task is the deliberate forward-pointer for closing those three gaps with named candidate references.

## Candidate references

Ranked by expected payoff for `KD-UV280-005` Section C and §5 Phase 1 evidence-table row tightening. Bibliographic details are this assistant's best recollection; the steward should verify DOIs / journal volumes before requesting PDFs.

### A. Modern Sellmeier — `[P:Tamosauskas2018]` candidate

**Provisional citation:** G. Tamošauskas, G. Beresnevičius, D. Gadonas, A. Dubietis, "Transmittance and phase matching of BBO crystal in the 0.18 – 5.2 µm range," *Optical Materials Express* **8**, 1410 (2018), DOI candidate `10.1364/OME.8.001410` (steward to verify).

**What it closes:** soft spot 2 above. Modern Sellmeier extending to the mid-IR (5.2 µm) and deeper into the UV (0.18 µm) than Eimerl 1987's 1014 / 212.8 nm anchors. Direct comparison `n(280 nm)` would either confirm the Eimerl extrapolation or motivate a different anchor for the BBO BK / ABCD recomputation.

**Acceptance criteria for promotion to `[P:]`:**
1. PDF or steward-verified citation in hand.
2. `data/literature/Tamosauskas2018/extracted.yaml` populated with the Sellmeier coefficients (matching the schema convention from `BBO_sellmeier_no_eimerl1987` / `BBO_sellmeier_ne_eimerl1987` in the Eimerl extraction).
3. Side-by-side `n_o(559)`, `n_e(559)`, `n_o(280)`, `n_e(280)` with the Eimerl values; if deviations exceed 1 × 10⁻³ in either polarisation at 280 nm, log as a `cross_check_notes` entry in the Eimerl extraction and re-run the BK / ABCD computation against both sets to bound the resulting `θ_PM` and `ρ` deltas.
4. KD-UV280-005 Section C gains a `[P:Tamosauskas2018]` constraint **alongside** (not replacing) the Eimerl anchor.

**Priority:** **medium-high.** Most likely outcome is mutual confirmation of the two Sellmeier sets at our operating wavelengths, which strengthens the dossier without changing values. If they disagree at 280 nm, that is a real result.

### B. Modern absolute `d_eff` calibration — `[P:Eckardt1990]` candidate

**Provisional citation:** R. C. Eckardt, H. Masuda, Y. X. Fan, R. L. Byer, "Absolute and Relative Nonlinear Optical Coefficients of KDP, KD*P, BaB₂O₄, LiIO₃, MgO:LiNbO₃, and KTP Measured by Phase-matched Second-Harmonic Generation," *IEEE Journal of Quantum Electronics* **26**, 922 (1990), DOI candidate `10.1109/3.55534` (steward to verify).

**What it closes:** soft spot 1 above. Direct re-measurement of BBO `d_eff` against an updated `d_36(KDP)` reference; commonly cited as the modernised d_eff anchor for BBO. If this paper reports a value different from Eimerl 1987 at compatible wavelengths, the §5 Phase 1 evidence-table BBO `d_eff` cell should reflect both values until reconciled.

**Acceptance criteria:**
1. Bibliographic record verified by steward.
2. `data/literature/Eckardt1990/extracted.yaml` populated with the BBO-relevant tensor components and the `d_36(KDP)` reference value used.
3. Re-derive `BBO_d_eff_typeI_559_to_280nm` using the Eckardt anchor; record both values + the discrepancy in the Eimerl extraction's `cross_check_notes`. If the discrepancy exceeds the ±25 % envelope on Eimerl's `d_11`, escalate to a steward review before changing the §5 Phase 1 evidence-table value.

**Priority:** **high.** This is the directly-actionable improvement to the binding source-side number for the BBO BK conversion-efficiency calculation; ±25 % on `d_eff` translates into ±50 % on conversion efficiency at fixed intensity.

### C. Kato 1986 — `[P:Kato1986]` candidate (low priority, already partial coverage)

**Provisional citation:** K. Kato, "Second-Harmonic Generation to 2048 Å in β-BaB₂O₄," *IEEE Journal of Quantum Electronics* **QE-22**, 1013 (1986), DOI candidate `10.1109/JQE.1986.1073097` (steward to verify). Already cited as Eimerl 1987 reference [4].

**What it closes:** primarily a cross-reference. The Kato 1986 Sellmeier coefficients are *already* captured in `data/literature/Eimerl1987/extracted.yaml` under `BBO_sellmeier_alternative_kato1986` (reproduced in Eimerl 1987 Table II), and the paper's experimentally measured PM angles are partly cross-tabulated in Eimerl 1987 Table VI. A standalone extraction would only add value if (a) a discrepancy with Eimerl emerges from task A or B, or (b) the deep-UV (down to 204.8 nm fifth-harmonic of Nd:YAG) phase-matching data become relevant for a future architecture entry beyond `KD-UV280-005`.

**Acceptance criteria:** scaffold only at this stage; promote to DRAFT extraction only if task A or B surfaces a need.

**Priority:** **low.**

### D. Compendium reference — `[S:Nikogosyan2005]`

**Provisional citation:** D. N. Nikogosyan, *Nonlinear Optical Crystals: A Complete Survey*, Springer (2005). Secondary `[S]` (book / compendium, not primary measurement).

**What it closes:** sanity-check infrastructure. Useful as a pointer to additional primary references that a focused PDF search might miss; not a substitute for the [P] anchors above.

**Priority:** **low**, optional reference for cross-checking the dossier `KD-UV280-005` Section C against an external authority.

### E. CW-UV LIDT at 280 nm — *separate task, not Eimerl follow-on*

This is *not* a Sellmeier or `d_eff` task; it is the binding open extraction item for `KD-UV280-005` Section C TODO bullet 2 ("cite peer-reviewed CW LIDT measurements at 280 nm"). Candidate sources are *operational papers* on long-term BBO degradation under CW UV, not crystal-property surveys. Examples that may be relevant (steward to verify):
- Druon, Balembois, Georges 2003-era CW-UV-degradation studies on BBO at 200–300 nm.
- Bhar, Ghosh, Datta and similar groups on CW-UV durability.
- More recent (2010s+) operational logs from quantum-optics groups using BBO at 280 nm (the present project's use case).

This deserves its own logbook task once tasks A and B are dispatched, since the literature here is more dispersed and harder to locate via a single PDF.

## Acceptance criteria for closing this task as a whole

This logbook entry is closed when **all** of the following are true:

1. Tasks A and B above have either been dispatched (PDFs in hand, extractions filed as DRAFT in `data/literature/Tamosauskas2018/` and `data/literature/Eckardt1990/`) **or** explicitly deferred by the steward with a documented reason (e.g. Phase 1 deadline pressure, references unavailable through institutional access).
2. `KD-UV280-005` Section C reflects the outcome — either populated additional `[P:]` constraints, or a TODO marker pointing back to this logbook entry for the deferral.
3. The §5 Phase 1 evidence-table BBO row's `d_eff` and `n_o/n_e` cells either tighten (if A/B confirm Eimerl) or split into `Eimerl // Tamosauskas` / `Eimerl // Eckardt` notation (if they disagree).

## Steward decision queue

This logbook entry is a *task draft*, not a closed gate. The steward decides:

- (a) Which of A / B / C / D to pursue first. Recommendation: **B then A** (B is the higher-payoff tightening; A is the cleaner cross-validation).
- (b) Whether to attempt institutional PDF access via the Freiburg library, or wait for a re-read window when the steward is on-site at MPI Garching / similar.
- (c) Whether the CW-UV LIDT task (E) should be split out into its own logbook entry now or deferred until A/B close.

## Cross-references

- [`data/literature/Eimerl1987/notes.md`](../data/literature/Eimerl1987/notes.md) — current primary anchor, identifies the three soft spots tasks A/B/E address.
- [`docs/KD-2026-XXX-uv-280nm.md`](../docs/KD-2026-XXX-uv-280nm.md) — KD-UV280-005 Section C now points at this logbook entry from its outcome paragraph.
- [`notebooks/2026-05-01-friedenauer-bk-recalculation.py`](../notebooks/2026-05-01-friedenauer-bk-recalculation.py) — §8 item 2 closed by Eimerl 1987 extraction (2026-05-04); §8 item 4 (factor-2.17 BBO BK discrepancy) now uses the Eimerl-derived 83.1 mrad walk-off value directly.
