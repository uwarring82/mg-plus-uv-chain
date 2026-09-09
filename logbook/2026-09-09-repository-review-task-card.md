# Task card — reconcile repository reviews and correct the evidence chain

**ID:** REPO-REVIEW-2026-09
**Date:** 2026-09-09
**Status:** IMPLEMENTATION STARTED — public-facing D6/RC-09/RC-10 corrections underway; numerical packages and binding-value decisions remain open.
**Steward:** Ulrich Warring
**Prepared by:** assistant under steward direction; no Council-3 stance or sign-off inferred.
**Review baseline:** scientific/code findings refer to `50da35f`. The initial card was filed at `60c1832`; the September receipt and coating-report state used by RC-08 is now committed in `ec4e7d401344fce6ff28c5ac88785e360205600f` ([inventory.md](../docs/components/inventory.md), especially §B.3 and §D). Checking out that revision reproduces the public code/document inputs; no working-tree inventory patch is required. Private supplier originals were consulted locally and remain outside the public reproducibility claim.

## Objective and intended outcome

Establish which scientific results, constraints and repository claims are supported, correct confirmed defects, and make the resulting evidence reproducible. Deliver a reviewed correction set with an explicit before/after record for every affected numerical result or binding parameter.

The priority is to validate the numerical foundations and constraint arithmetic before reusing their outputs in coating specifications or architecture comparisons. CI is an enabling task; passing the current suite alone does not settle scientific correctness.

This card consolidates two reviews, rather than accepting either review wholesale. It does not change source code, the Charter, reference-triple values, kill-gate states, procurement decisions or published specifications. Implementation and any required governance dispositions are subsequent work.

## Charter §9 trigger questions

- **Affects Level 0 parameters?** Potentially. The scattering-rate interpretation and derived scenario values require deliberation before changing the locked reference triple.
- **Affects Level 1 parameters?** Potentially. Corrected power, phase-noise and SHG calculations may alter derived budgets and coating targets. The impact must be calculated and recorded.
- **Affects success criteria?** Not by this filing. Any later change to binding criteria must be separately identified and disposed of under §9.
- **Charter text affected?** Proposed spectroscopic notation corrections and release-history corrections may touch frozen text. Use the documented v1.x process if amending the Charter; do not rewrite historical approvals or invent missing records.

Routine code, test and documentation corrections are distinct from changing agreed requirements. A numerical correction does not itself close or reopen G1, G2 or G3. The [existing task-split deliberation](2026-05-09-council-3-trigger-task-split-success-criterion.md) remains separate.

## Evidence and review reconciliation

The inputs are two assistant reviews of the same repository baseline and a
follow-up critique supplied by the steward on 2026-09-09. They are not
independent expert sign-offs. Confidence comes from the checks performed,
source equations and reproducible results, rather than the author of a claim.
The first pasted review has SHA-256
`596764ffd60c5169dcfc844a6c2e4f9a4565adca541b959b96d515ba9cf5d2b9`;
its full execution environment was not recorded.

**Confirmed** means inspected or calculated during the initial review or
this revision. **Steward-confirmed reproduction** means the steward reports rerunning a
check with retained scripts. The walk-off anchor, optical products, per-beam
powers, bracketing failure and continuity jump now have that confirmation;
the script paths/revisions still need linking in the implementation evidence.
This records corroboration without claiming the scripts were inspected here. **Open derivation**
means a physical convention or reference still needs resolution. **Decision**
means a steward disposition is needed. Agreement between assistant runs does
not promote an open derivation into accepted physics.

| Check | Evidence / disposition |
|---|---|
| Nonzero-walk-off normalisation | Initial independent quadrature gave `h_m ≈ 0.0392431` at `B ≈ 18.0166`, `ξ ≈ 1.41317`; steward-confirmed reproduction gives `0.0392430`, optimum waist **19.346 µm**, and recovery of the zero-walk-off optimum. Preserve as diagnostic evidence; implement durable, converged regressions in RC-01. The passing existing suite does not establish this convention |
| Absolute SHG prefactor and absorption conventions | The extra fundamental-index factor is supported by a plane-wave derivation in the follow-up, but reconciliation with an external reference remains **open**. Resolve it and the absorption convention in RC-01 before accepting absolute powers |
| Constraint arithmetic | Initial checks and steward-confirmed reproductions agree on optical products **22.77% / 35.58%** and per-beam powers **130.4 / 115.9 / 39.1 µW** from the currently printed relations. Scattering-table inconsistency is confirmed; prediction/limit/allowance semantics remain D2, not an arithmetic verdict on the physical model |
| Parameter-test isolation | **Leak claim rejected and retracted in the follow-up.** `_restore_parameters_state` in [test_parameters.py](../tests/test_parameters.py) reloads before and after each test. The mutator-first pytest check passed 2/2; direct calls bypass fixtures. The generator's `-> None` annotation is a separate RC-06 type-cleanup item |
| Solver limits / auto-path continuity | Passive-limit bracketing failure is confirmed and steward-reproduced. The continuity check was also rerun locally for this filing: **3.3478%** at γP = 0.049999 / 0.05, relative to the depleted-side conversion fraction. RC-05 records the values; the earlier ≈3.2% estimate used a less tightly localised comparison |
| Import-guard coverage | “Cannot fail” is too strong: guards can detect forbidden text, but can pass vacuously and have untested syntax coverage. RC-06 must demonstrate both passing and failing fixtures and state its inspection boundary |
| Release and licence claims | Empty local tags and absent DOI metadata do not prove external nonexistence. Licence scope/precedence is inconsistent; this does not establish that newer files are legally unlicensed. RC-10 gathers evidence and records dispositions |

## Priority and ownership

**MUST now:** RC-01, RC-02 and RC-05 address numerical foundations, locked-value
semantics and reproducible solver failures. **NEXT:** RC-03–04 and RC-06–10 are
required follow-through, ordered by their actual inputs rather than held behind
one global gate. **OPTIONAL:** RC-11 needs an explicit adopt/defer decision.
A NEXT item can begin immediately where its work is independent.

**Accountable owner for every package: Ulrich Warring.** The assistant can
prepare derivations, changes and check reports under his direction. Numerical,
optics, servo and tooling expertise are review needs, not six staffed positions.
No external reviewer is assigned. RC-01 requires an independent *calculation*
using a separate method and cited equations; a second assistant's agreement
is insufficient. An external physics review may be requested by the steward,
but is not an assumed dependency. If he makes it an acceptance condition,
record the named reviewer, agreed scope and availability before scheduling it.
Required Charter dispositions remain separate from this staffing model.

## Proposed work packages

### RC-01 · MUST — independently validate and correct SHG numerics

**Evidence:** confirmed walk-off discrepancy; prefactor and absorption derivations open. **Dependency:** none for derivation or architecture-neutral corrections; D1 records acceptance evidence.

- Reconcile the β/B convention in [boyd_kleinman.py](../src/boyd_kleinman.py): for `B = (ρ/2)√(Lk₁)`, the walk-off exponential requires `−B²(τ−τ′)²/ξ`. Resolve the suspected missing `n_omega` factor in [shg_single_pass.py](../src/shg_single_pass.py), and correct K's documented unit to W⁻¹. [Daniel, Tsai & Hemmerling, Eqs. 1–3](https://arxiv.org/pdf/2009.08430) provide an independent reference.
- Resolve the absorption parameter κ and focus-offset convention from a cited derivation. The follow-up reports a length/confocal-parameter mismatch; treat the proposed correction as **unverified** until the absorption definitions and limiting cases are derived. Check pump versus harmonic absorption separately.
- Resolve `sigma_bracket` semantics: Brent's starting bracket is not a bounded interval. Verify the intended maximum across phase-mismatch lobes; changing to a bounded local optimiser alone is not proof of a global maximum. Remove the unused imaginary integrand if unnecessary and align the documentation.

**Acceptance:** an independent reference calculation and regressions cover zero and nonzero walk-off at several ξ values, absolute SHG normalisation, absorption limits, and phase-mismatch optimisation. Record source equations, conventions, tolerances and numerical convergence. Diagnostic anchors from the initial review are `B ≈ 18.0166`, `ξ ≈ 1.41317`, corrected `h_m ≈ 0.0392431` at a 19.4 µm waist, and optimum waist ≈19.35 µm. Reproduce these rather than treating them as newly frozen constants.

### RC-02 · MUST — reconcile Raman derivation and locked-value semantics

**Evidence:** confirmed arithmetic discrepancy; physical interpretation unresolved. **Dependency:** none for derivation; D2 before changing locked values or their meaning.

Re-derive [raman-requirements.md](../constraints/raman-requirements.md) with explicit Hz/rad·s⁻¹ conventions, beam-intensity convention, linewidth definition, dipole matrix element, polarisation and multilevel limitations. Resolve the Gaussian peak-intensity versus `P/(πw₀²)` convention before tightening the prefactors.

| Scenario | Γ_sc from the currently printed equation | Recorded Γ_sc | Recorded / formula |
|---|---:|---:|---:|
| Conservative | ≈161.0066 s⁻¹ | 2,500 s⁻¹ | **15.5273** |
| Nominal | ≈1,288.0530 s⁻¹ | 20,000 s⁻¹ | **15.5273** |
| Aggressive | ≈8,587.0199 s⁻¹ | 110,000 s⁻¹ | **12.8100** |

Ratios use unrounded formula results with Γ = 2π × 41 MHz, and Ω_R and Δ
converted consistently to angular frequencies. Applying the first two rows'
common factor to Aggressive gives **133,333 s⁻¹**, rather than 110,000 s⁻¹;
the difference is not rounding. One uniform convention multiplier cannot
explain all three rows. A scenario-specific allowance or manual adjustment
is a plausible explanation to investigate under D2, not established entry
history. Trace the original derivation/decision before choosing that reading.

The nominal printed relation gives ≈0.00161 scattering events per π pulse, versus 0.025 recorded. The document's dipole formula gives ≈1.4164 × 10⁻²⁹ C·m; using its stated intensity convention gives ≈523.4 MHz single-beam and ≈137.0 MHz Raman prefactors. These support correcting the quoted dipole, but do not settle the full atomic model.

**Decision required:** are the recorded Γ_sc values derived predictions, accepted upper limits, or explicit conservative allowances? A looser upper limit and a mistaken prediction have different correction paths. Do not simply replace [parameters.py](../src/parameters.py) values while preserving the old closure justification.

**Acceptance:** documented derivation and scenario table, explicit disposition of every locked value affected, updated source-of-truth links, and tests for the accepted relationships. If a value is a limit, test the appropriate inequality rather than forcing equality to a model prediction.

### RC-03 · NEXT — correct constraint arithmetic, reference frames and notation

**Evidence:** confirmed internal inconsistencies. **Dependency:** optical products, reference-frame work and notation checks can proceed now; final Raman scenario values depend on RC-02/D2. Binding document amendments require their applicable disposition.

- Recompute [loss-budget.md](../constraints/loss-budget.md). Its existing Raman formula gives ≈130/116/39 µW per beam for Conservative/Nominal/Aggressive, not 50/130/1,000 µW. Its printed optical product is 22.77%, not 18%; the corresponding one-AOM product is 35.58%, not 28%. Clarify beam-splitter throughput versus power allocated to each arm.
- Convert the forbidden-domain wavelength endpoints in the [Friedenauer extraction](../data/literature/Friedenauer2006/extracted.yaml) onto the same frequency/detuning axis as the scenarios. A 14 GHz interval width does not place its edge at 14 GHz detuning. Preserve the paper's separately reported width and endpoints with their discrepancy visible.
- Correct Mg⁺ term notation to `3s ²S₁/₂` and `3p ²Pⱼ` across prose and comments; plan compatibility if renaming exported symbols. [NIST Mg II levels](https://physics.nist.gov/PhysRefData/Handbook/Tables/magnesiumtable6.htm) are the reference. Handle frozen Charter text through the documented revision process.

**Acceptance:** generated arithmetic tables with units and provenance; scenario/domain overlap evaluated in one explicit reference frame; notation consistent; any binding-budget impact recorded.

### RC-04 · NEXT — repair phase-noise and servo interpretations

**Evidence:** confirmed conflicts with recorded definitions. **Dependency:** definitions, dimensional checks and measurement provenance can proceed now; scenario-dependent numerical limits depend only on the relevant RC-02/03 inputs.

Reconcile [phase-noise-budget.md](../constraints/phase-noise-budget.md), [vecsel-systems.md](../docs/tutorials/vecsel-systems.md), the [baseline](../docs/components/friedenauer-baseline.md), and [piezo mechanics](2026-05-20-bbo-coating-run-wp/bc-g-results.md).

- Specify noise PSD, linewidth model, bandwidth and measurement duration; remove the universal ×4 linewidth rule. Harmonic phase multiplication does not imply one universal linewidth multiplier.
- Separate optical coherence from cooling-frequency stability and relative Raman phase coherence. Remove the claims that ≤1 MHz satisfies ≪100 Hz or ≪10 Hz limits; check the path-length-to-phase-noise relation and PSD conventions.
- Distinguish the ≈18 kHz loaded mechanical resonance from measured unity-gain bandwidth and cavity optical linewidth. Base tracking/noise-transfer claims on a transfer function; mark unknown bandwidths as unknown.

**Acceptance:** a cross-reference table covers each linewidth, phase-noise and servo-bandwidth claim in the four listed documents, with definition, units, equation/source and measured/assumed/unknown status. Dimensional and numerical checks cover the harmonic phase relation and path-length conversion. Any changed requirement links to its recorded disposition; unavailable bandwidth measurements are explicitly marked unknown.

### RC-05 · MUST — correct solver/API edge behaviour

**Evidence:** confirmed counterexamples; additional robustness checks proposed. **Dependency:** none for solver edge cases; coordinate SHG model semantics with RC-01. Independent of D2.

Fix [optimal_input_coupler](../src/enhancement_cavity.py) bracketing near the passive limit (`P=1e-8 W, L=0.01, γ=1e-4 W⁻¹` currently fails) and near `L=1`. Resolve the **3.3478%** discontinuity sampled across `γP=0.05` in the single-pass `auto` path. For explicit `regime="small"`, decide whether to document its limited domain, warn, or reject out-of-domain use: it can return P₂>P₁ despite the current bounded-output docstring.

**Reproduced sampling:** with `P = 1 W`, evaluate conversion fraction η in
`auto` at γ = 0.049999 and 0.05 W⁻¹. The results are **0.049999** (small-signal
side) and **0.0483793551512** (depleted side). The reported jump is
`100 × (η_small − η_depleted) / η_depleted = 3.34780165%`.
These are finite sampling points; the limiting jump as γP approaches 0.05
from below is slightly larger. Retain the points and denominator in the
regression rather than freezing the earlier approximate 3.2% figure.

**Acceptance:** regressions cover continuity/monotonicity for the default model, valid domain boundaries, zero-power/passive limits, invalid/nonfinite inputs and explicit approximation semantics. Do not hide model errors with an unexplained output clamp.

### RC-06 · NEXT — make scientific checks and toolchain enforcement reproducible

**Evidence:** absent CI/lockfile and optional coverage invocation confirmed. **Dependency:** bootstrap and record existing failures now; add scientific regressions as RC-01–05 supply them. Independent of D2 for infrastructure.

- Keep site configuration checks scoped to the actual `docs/` root. The existing `*.py`, `*.yml.bak` and `literature/` exclusions matched no paths; the initial public-facing correction removes these no-ops. Validate any future exclusions against real inputs.
- Define a supported Python environment and committed dependency resolution. Add CI with documented install/test commands, ≥90% coverage enforcement, chosen lint/format/type checks, structured-data validation and link checks.
- Choose one formatting policy and explicit exceptions for intentional physics/unit-bearing names. Reproduce the reported mypy findings with recorded command, version and scope; fix tutorial string escapes and validate their rendered mathematical labels.
- Add a tutorial-regeneration drift check using the existing normalisation in [render_tutorials.py](../scripts/render_tutorials.py): run `python scripts/render_tutorials.py`, then `git diff --exit-code -- docs/tutorials` in a clean supported environment. Also detect untracked generated outputs, which `git diff` alone misses. Demonstrate that a stale committed output fails and that an unchanged second render passes. Record execution cost; the diff assertion is cheap, but notebook execution is not assumed free.
- Add independent equation/limit tests; avoid tests that merely duplicate implementation algebra. Preserve the existing parameter-reset fixture. Correct its generator annotation to `Iterator[None]` (or equivalent) during type cleanup; no new state-reset mechanism is needed to address the rejected leak claim.
- Test import guards using positive and negative examples, assert a nonempty source tree, and consider AST-based import inspection. Document that these checks do not establish complete Charter compliance or detect every data-loading path.

**Acceptance:** the agreed checks run in a clean supported environment and CI, fail on representative injected defects, and pass without suppressing unresolved scientific discrepancies. Record commands, versions and checked paths; do not compare raw lint totals from different scopes.

### RC-07 · NEXT — recalculate affected results and revise their claims

**Evidence:** downstream dependence on corrected calculations confirmed. **Dependency:** stage each output by the inputs it actually uses; BK/SHG outputs depend on RC-01, affected solver sweeps also on RC-05. Raman/noise budgets wait only for their relevant RC-02–04 results and binding-value dispositions.

Trace and rerun the [BK recalculation](../notebooks/2026-05-01-friedenauer-bk-recalculation.py), [cascade diagnostic](../notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py), [IC sweep](../notebooks/exploration/2026-05-20-bbo-ic-impedance-match.py), tutorial sources, [calculations page](../docs/calculations.md), and [coating work package](2026-05-20-bbo-coating-run-wp/).

Revisit γ, fitted passive/non-mirror losses, IC optima, uncertainty bands, circulating intensities and all dependent coating targets. Distinguish a loss fitted to reproduce one output point from independent validation. State harmonic-extraction assumptions. Correct the published formula's missing `k₁` and confocal-parameter factor, and reassess the ≈42 µm discrepancy narrative.

**Opposing corrections:** at the stated BBO point, the walk-off correction
changes `h_m` from approximately **0.033050 to 0.039243**, scaling γ by
**1.1874** if K is unchanged. The suspected extra fundamental-index factor
would scale K by **1/n_omega ≈ 0.598**, using the existing notebook's
`n_omega = 1.67276`: the **ordinary BBO index at vacuum wavelength 559 nm**,
from Eimerl et al. (1987), Eq. (1) and Table II row a, as transcribed in the
[repository's draft Sellmeier extraction](../data/literature/Eimerl1987/extracted.yaml)
(`BBO_sellmeier_no_eimerl1987`; DOI `10.1063/1.339536`). Its formula
`n_o² = 2.7405 + 0.0184/(λ² − 0.0179) − 0.0155 λ²`, with λ in µm,
gives **1.672757646** at λ = 0.559 µm. The retained digits reproduce the
existing notebook input; they are not a stated measurement uncertainty.
Together these would scale γ by approximately **0.710**,
with other inputs held fixed. This is a conditional sensitivity estimate,
not an accepted recalculation. The net direction is unresolved until both
RC-01 conventions are settled; neither change alone determines whether the
May coating targets tighten or loosen after the cavity model is rerun.

**Acceptance:** before/after results with source revision and environment, regenerated notebook/HTML outputs, an explicit impact assessment for the frozen May specifications, and dated amendments preserving historical reasoning. The received Agile mirrors remain recorded as delivered stock; a model correction is not evidence of a supplier defect.

### RC-08 · NEXT — qualify inventory and architecture compatibility claims

**Evidence:** confirmed contradictions in prose/tables; September coating reports now filed. **Dependency:** label/provenance corrections and bench checks can proceed now; model-based suitability claims depend on the relevant RC-07 output and measurements, not every review package.

- In [inventory.md](../docs/components/inventory.md), correct I-B17's inference from transmission to reflectivity and its “meets >99.93%” claim. Curved optics in I-B13/I-B17 cannot be treated as plane mirrors merely by placement. Keep I-B22's role conditional on vendor φ conventions.
- Preserve I-B23–I-B26, the 22 documented Agile pieces, separate receipt/issue/photo dates, and pending physical checks. Keep `T(280)>5%` literal until supplier evidence resolves it; do not substitute 95%. The subsequent supplier reply and three coating reports are now filed privately: preserve the selected inventory summary, provisional batch-to-item assignments, green p / UV s conditions and measurement-backed evidence of high UV transmission. Limit the remaining transmission question to the numerical whole-optic value at 280 nm / s / 14° for threshold acceptance; the report already includes measured UV transmission at 0°. No report explicitly identifies the piezo item. Retain the earlier message as a historical draft; do not infer its exact sent wording from the reply.
- In the [IC-VECSEL comparison](../docs/architectures/ic-vecsel-alternative.md), fix the 167/250 mW claims relative to a 30–80 mW precedent, identify the actual source/operating point behind the 7% BBO efficiency, and replace the BBO-paper reference proposed for LBO Sellmeier data.

**Acceptance:** a row-by-row correction record covers I-B13/I-B17/I-B22, the I-B23–I-B26 provenance and the three architecture-comparison claims above. Each resulting suitability claim has its source and conditions or a pending verification entry owned by the steward. Documented Agile quantities still sum to 22; no physical-verification field is filled without a dated bench record.

### RC-09 · NEXT — make data, status and publication links maintainable

**Evidence:** mixed units and stale/missing references confirmed. **Dependency:** link/schema/status work can proceed now; revised numerical content follows its particular RC-07 result.

Add a literature/measurement schema separating reported values from SI computational values, uncertainty, source location and extraction status. Preserve explicit units for nested Sellmeier data. Make README distinguish existing paths from planned ones and link to a dated current-status record; correct status.md's premature claim that ≥90% coverage is mechanically enforced (implementation belongs to RC-06); distinguish dossier-slot counts from literature-folder counts and locked reference values from still-draft envelopes.

Repair missing targets in inventory and the BC-B/BC-F records. Check Markdown and HTML links and Jekyll `.html` destinations separately. **Local source check completed:** the tracked Heidi lab note references `.attachments/` images, but `git ls-files 'data/lab notes/*.attachments/*'` returns no files and `.gitignore` excludes those directories. A clean clone therefore lacks those linked images. The note is outside the configured `docs/` Pages source; this is a GitHub Markdown image issue, not a missing Jekyll site page. Repair the Evernote `tel:` conversion. For ignored lab attachments, choose a public summary with explicit omissions or an approved asset subset; do not publish the entire private archive just to satisfy a link checker.

**Acceptance:** schema-valid inputs, reproducible status counts, and a clean-clone/site link report with explained private-source exceptions. Historical snapshots remain dated and are not silently rewritten as current facts.

### RC-10 · NEXT — licensing, contacts and release provenance

**Evidence:** internal inconsistencies confirmed; external absence claims unverified. **Dependency:** none for evidence gathering; steward disposition before licence/contact changes or release actions.

**D6 language decision:** retain Coastline, Sail and Handbook where they identify licence categories, with the SPDX licence on first use; gloss Model B as distributed copies pinned by checksum. Use plain language for public-facing review and ownership, preserving precise Charter references and G1–G3 conditions. Remove decorative endorsement/eyebrow language from README, the landing page, architecture/component pages and shared footers. Leave the frozen Charter unchanged. Licence scope is decided explicitly, never inferred from page styling. The initial audit finds **12**, not 15, Markdown pages under `docs/architectures/` and `docs/components/`; each is listed in the licence map. Their existing CC-BY-4.0 declaration is recorded while an explicit split assignment remains pending.

Reconcile README, LICENSE-DOCS, [LICENSES.md](../LICENSES.md), folder declarations and [CITATION.cff](../CITATION.cff). Identify whether citation metadata describes the software release or the mixed repository. Explicitly map newer pages, nested work-package files, generated tutorials and assets; do not assign licences solely from Coastline/Sail styling. Verify the missing adoption record without inventing or backdating it. For the coating-run subtree, inspect whether the parent workplan's §9 trigger block covers each child artifact; do not mechanically add duplicate blocks to every file. The parent workplan and the BC-G log already contain trigger records.

Check remote tags/releases and any existing Zenodo record before declaring them absent. If registration never occurred, correct the claims and propose a separate release/deposit task; if it did, record the verifiable identifiers. Inspect public contact fields in the [coating cover letter](2026-05-20-bbo-coating-run-wp/specs/coating-run-cover-letter.md) and adopt the Steward's intended public contact. The presence of a personal address alone does not establish unauthorised publication.

- **Future Git author/committer identity:** local history inspection at `60c1832` finds **76 reachable commits**, all using the same personal Gmail address for author and committer; that address also appears in the coating cover letter. Include repository-local Git identity and any environment/automation overrides in D6's public-contact decision. Record the intended identity for future commits and verify the effective author/committer fields on the next commit after any configuration change. This extends the contact review beyond document text; it neither presumes the current identity is unauthorised nor calls for rewriting past commits. Remote publication of every local commit was not separately checked here.

**Acceptance:** explicit documented scope/precedence, verified or accurately qualified release/DOI statements, and a contact disposition covering both public documents and future Git author/committer identity. No new publication, release, DOI deposit or history rewrite is authorised by this card.

### RC-11 · OPTIONAL — decide whether to rename the installed package

**Evidence:** `src` is the installed top-level package by configuration. **Dependency:** weigh after RC-06; coordinate before affected RC-07 regeneration if selected.

Evaluate a proper `mg_plus_uv_chain` package namespace to reduce generic-name collisions. This is a maintainability proposal, not a demonstrated collision in the current environment. Estimate migration of imports, notebooks, packaging, documentation and import guards; choose compatibility aliases or a documented API change if needed.

**Acceptance:** recorded adopt/defer decision with rationale. If adopted, clean-install imports and tests work outside the checkout and generated tutorials use the supported namespace.

## What can proceed and what waits

| Work | Can proceed now | Actual hold point |
|---|---|---|
| Phase 2 bench work on the existing chain | Baseline measurements, exposure-history evidence, mirror count/inspection and supplier-data clarification continue independently of this review | Existing experimental protocols and Charter G1/G2 closure criteria still apply; D2 does not block collecting these data |
| RC-01 / RC-05 | Independent derivations, benchmarks and generic numerical fixes | Acceptance of the model/conventions before promoting corrected outputs; no D2 dependency |
| RC-02 | Derive the atomic-model alternatives and compare predictions with the locked table | D2 before revising locked values, semantics or closure justification |
| RC-03 / RC-04 | Reproduce optical products; reconcile reference frames, notation, noise definitions and evidence | Scenario-dependent tables await only the inputs they use; binding amendments await their recorded disposition |
| RC-06 / RC-10 | Environment/CI baseline, drift-check setup and licence/contact/release evidence gathering | Scientific regressions join CI when available; evidence gathering neither changes licences nor authorises releases |
| RC-07 | Map dependencies and recalculate BK/SHG results after RC-01; solver-dependent sweeps after RC-05 | Revised Raman/noise outputs and binding coating changes wait for their relevant derivation/disposition; keep provisional calculations labelled |
| RC-08 / RC-09 | Correct source attribution and unsupported wording; collect bench evidence; fix links and define schemas | Numerical suitability waits for its specific model outputs and measurements; private-asset publication remains a separate decision |

This follows [status.md's unblocked/gated distinction](../docs/status.md),
whose dated snapshot is not being refreshed by this card. The review does
not change G1, G2 or G3 and does not suspend Phase 2 measurements.

**Suggested first implementation slice:** record the supported-environment
baseline and start RC-01/05 regressions alongside RC-02's derivation. Bootstrap
RC-06 and gather RC-10 evidence independently. Then propagate corrections
one calculation at a time using a dependency manifest, rather than waiting
for RC-01–05 to close as one block. This is a proposed sequence, not a record
of implementation or approval.

| Decision | Proposed disposition | Accountable owner / status |
|---|---|---|
| D1 — Evidence for accepting numerical corrections | Cited conventions and independently implemented, converged nonzero-walk-off and absolute-prefactor benchmarks; external review only if explicitly scoped and assigned | Ulrich; pending evidence |
| D2 — What do locked Γ_sc values mean? | Resolve prediction/limit/allowance semantics before changing those numbers or acceptance tests; record applicable §9 disposition | Ulrich; pending; does not gate unrelated work |
| D3 — Reliance on derived May results during correction | Mark affected recommendations as awaiting revalidation; preserve historical values and receipt facts | Ulrich; proposed, not enacted by this card |
| D4 — Charter wording/history and frozen-spec amendments | Use dated corrections and the documented revision process; preserve original sign-offs and obtain applicable governance review | Ulrich; pending |
| D5 — Toolchain and source of truth | Choose Python/dependency policy, formatter/naming exceptions, CI checks including tutorial drift, and generated-table strategy | Ulrich; pending |
| D6 — Public language, licences and records | Plain public language; preserve and gloss licence categories, Charter references and gates. Decide page-by-page licence scope, release claims and public contact (including future Git identity); consider package rename separately | Ulrich; language direction accepted in this session; initial corrections underway; remaining scope/contact decisions pending |

## Completion criteria and handoff

- [ ] Each RC-01–11 entry links to a completed artifact/check report or a dated defer/block record stating the reason, exact dependency and next action; accountable owner is Ulrich unless explicitly reassigned.
- [ ] RC-01's independent calculation records equations, input conventions, reference results, convergence and tolerances. RC-05's original counterexamples and boundary regressions pass; unresolved discrepancies are listed by test/input.
- [ ] D2 records prediction/limit/allowance semantics for every affected locked scattering value. Any changed binding value, frozen specification or Charter wording links to its dated disposition and original approval.
- [ ] An output manifest maps each affected calculation/page to its inputs, revision and environment; every changed numerical output has before/after values or a stated reason why direct comparison is invalid.
- [ ] A clean-environment report records install, test/coverage, lint/format/type, schema/link and tutorial-regeneration results. Representative injected defects fail their intended checks; a second unchanged tutorial render has no tracked or untracked output drift.
- [ ] RC-08's item/claim checklist and RC-10's licence/contact/release evidence record are filed; remaining bench/vendor questions are listed with pending status. RC-09/11 have completion or explicit deferment records.

## Reproduce the filing's arithmetic checks

Run the following from the repository root. This checks the printed relations
and existing API behaviour; it does not validate the atomic model or the
suspected SHG prefactor. Executed locally with Python 3.9.7; the steward
also reports identical output on Python 3.9.7 and 3.13. These diagnostic runs
do not select RC-06's supported environment or replace its full-suite checks.

```python
import math
from src.shg_single_pass import single_pass_conversion_fraction

for detuning_Hz, rabi_Hz, recorded_per_s in [
    (80e9, 100e3, 2500), (40e9, 400e3, 20000), (15e9, 1e6, 110000)
]:
    # Gamma is angular; Omega_R/Delta is convention-invariant (2*pi cancels).
    rate_per_s = (2 * math.pi * 41e6) * rabi_Hz / (2 * detuning_Hz)
    print(rate_per_s, recorded_per_s / rate_per_s)

eta_small = single_pass_conversion_fraction(1.0, 0.049999)
eta_depleted = single_pass_conversion_fraction(1.0, 0.05)
print(eta_small, eta_depleted, 100 * (eta_small - eta_depleted) / eta_depleted)
# Ordinary BBO index at vacuum 559 nm; Eimerl 1987 Eq. (1), Table II(a).
# Provenance and coefficient units: RC-07 and the linked draft extraction.
n_bbo_ordinary_559nm = 1.67276
print((0.039243 / 0.033050) / n_bbo_ordinary_559nm)  # conditional gamma factor
```

**Handoff status:** public-facing implementation is recorded in [the D6 correction log](2026-09-09-public-record-corrections.md); cite the reviewed revision of this
card and the inventory baseline above in the subsequent deliberation record.
Numerical correction packages and binding-value dispositions remain open; this public-facing correction does not change a gate.
