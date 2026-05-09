# Council-3 deliberation trigger — task-split success-criterion question

**Steward:** Ulrich Warring
**Date:** 2026-05-09
**Status:** TRIGGER FILED — pending Council-3 deliberation; gates Phase 4 candidate-slate opening for the IC-VECSEL + pulsed-Raman pair.
**Origin:** Priority-6 action item from [`logbook/2026-05-08-architecture-review-tightening-specs.md`](2026-05-08-architecture-review-tightening-specs.md) §4.4 + §5.

## Header (Charter §9 trigger questions)

This entry is a **trigger filing**, not a unilateral steward direction. The Charter §9 questions below identify *why* Council-3 deliberation is required; they are *not* answered by this entry — answering them is the deliberation outcome.

- **Affects Level 0 parameter?** Conditional. The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is preserved as the CW-chain operating point under any disposition; what is at issue is whether the *binding form of Level 0 itself* shifts from single-operating-point to multi-operating-point semantics.
- **Affects Level 1 parameter?** Yes. The CHARTER §1.5 ≥ 500 mW UV indicative anchor is set against a single-architecture CW chain; the IC-VECSEL + pulsed-Raman pair re-allocates this into ~ 50 mW CW (cooling + repumping) + ~ 0.1–0.5 W pulsed (Raman at far-red detuning). Whether this re-allocation is admissible is the central question.
- **Affects success criterion?** Yes. CHARTER §6.1 states the success criterion as a single-architecture sustained CW UV figure; the task-split would replace it with a multi-architecture pair criterion. This requires explicit Council-3 sign-off under Charter §9.

---

## 1 · The question for Council-3

> **Does the IC-VECSEL + pulsed-Raman task-split alter CHARTER §6.1 (CW output ≥ 500 mW at 280 nm, sustained for ≥ 8 h)?**
>
> Steward proposed disposition: **Yes — the task-split replaces the single-architecture criterion with a multi-architecture pair criterion** (~ 50 mW CW for cooling + repumping; ~ 0.1–0.5 W pulsed for Raman at the far-red-detuned operating point). Confirmation, modification, or rejection of this disposition is a Council-3 matter.

Until Council-3 disposes of this question, the IC-VECSEL + pulsed-Raman pair sits as **forward-looking sketches only**, not as Phase 4 architecture-comparison candidates. The single-architecture [next-gen 500 mW workplan](2026-05-08-next-gen-500mW-workplan.md) is unaffected by this trigger and remains the load-bearing pre-G2 deliverable.

---

## 2 · Background — what the slate of architectures proposes

The architecture slate at [`docs/architectures/`](../docs/architectures/) currently holds four pages:

| Page | Role |
|---|---|
| [`friedenauer-2006`](../docs/architectures/friedenauer-2006.md) | Reference baseline (single-architecture, all UV tasks) |
| [`next-gen`](../docs/architectures/next-gen.md) | Single-architecture parameter-optimisation target at ≥ 500 mW UV |
| [`ic-vecsel-alternative`](../docs/architectures/ic-vecsel-alternative.md) | Cooling + repumping CW chain at ~ 50 mW UV |
| [`pulsed-raman-alternative`](../docs/architectures/pulsed-raman-alternative.md) | Raman-only pulsed chain at far-red detuning |

The slate is internally coherent only if the task-split is admissible. If Council-3 rejects the task-split, the IC-VECSEL alternative as currently scoped underdelivers Level 1 (~ 50 mW UV vs ≥ 500 mW anchor) and the pulsed-Raman alternative remains under the CHARTER §3 line-105 pulsed-UV non-goal — both candidates would need substantial rescoping or withdrawal.

---

## 3 · Sub-questions for Council-3

The reviewer who flagged this item ([review §3.5 / §4.4 / §5](2026-05-08-architecture-review-tightening-specs.md)) named three sub-questions that the deliberation must address. Each is non-trivial; each has its own answer space.

### 3.1 — Does the v1.0 CHARTER §3 non-goal on pulsed UV stand, or is it superseded by this sketch?

CHARTER §3 line 105 reads: *"Pulsed UV systems (the stroboscopic / fs-comb discussion with Leibfried is a distinct project)"* under the **Out of scope (non-goals)** heading. The pulsed-Raman alternative is exactly the kind of system this clause excludes.

Possible Council-3 dispositions:

| Option | Effect on the slate |
|---|---|
| **A.** §3 non-goal stands | Pulsed-Raman alternative is **withdrawn** from the slate; the task-split becomes IC-VECSEL + (off-board Raman by other means, possibly a future "distinct project" coordinated with Leibfried). |
| **B.** §3 non-goal is **superseded** | Pulsed-Raman alternative becomes admissible **inside** `mg-plus-uv-chain`'s Charter scope; CHARTER §3 line 105 is rewritten and the v1.0 → v1.1 Charter version bump is needed. |
| **C.** §3 non-goal is **scoped to a sub-project** | Pulsed-Raman alternative becomes a **parallel sub-project** that links to `mg-plus-uv-chain` via shared ²⁵Mg⁺ infrastructure but lives outside this repository's Charter scope; the architecture page stays as a forward-looking artefact but Phase 4 inclusion is *not* triggered by this repository's gates. |

Steward stance: Option **C** is least disruptive to the v1.0 Charter and respects the original "distinct project" framing. Options A and B are also valid; the choice is Council-3's.

### 3.2 — Does the reference-triple anchoring rule (CHARTER §5.2) allow per-architecture operating-point scoring?

CHARTER §5.2 anchors Phase 4 axis-1 (Raman capability) and axis-2 (phase coherence) scoring against the single locked reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}`. Under the task-split, the CW chain operates at Δ_ref while the pulsed Raman chain operates at Δ ≫ Δ_ref (~ tens of nm red).

Possible Council-3 dispositions:

| Option | Effect on Phase 4 scoring |
|---|---|
| **A.** Scoring stays anchored to Δ_ref only | Pulsed-Raman alternative scores against Δ_ref despite operating at Δ_far; this likely under-rewards the pulsed regime's principal physics advantage (Γ_sc suppression). |
| **B.** Per-architecture scoring at each architecture's own operating point | CW chain scores at Δ_ref, pulsed chain at Δ_far; the two axis-1 scores are **not directly comparable** and must be combined with explicit task-allocation weights. |
| **C.** Hybrid: scoring at Δ_ref *and* Δ_far reported separately for the pulsed candidate | Each architecture lists *both* a Δ_ref score (apples-to-apples vs the CW candidates) and a Δ_far score (true operating-point performance); deliberation explicitly trades them. |

Steward stance: Option **B** is the architecturally honest framing but introduces scoring-rule complexity; Option **C** preserves a single comparison axis at Δ_ref while still reporting the Δ_far advantage. Either is defensible.

### 3.3 — Does CHARTER §3 "single-source-derived beam pair preferred" apply per-task or per-system?

CHARTER §3 (Preserved) reads: *"Two-photon stimulated Raman capability for spin–motion control (single-source-derived beam pair preferred unless dual-source architectures demonstrate equivalent or better noise performance)"*. Under the task-split, the CW chain supplies its own beam pair from a single source, and the pulsed chain (if admitted) supplies its own beam pair from a single source — but the *project as a whole* uses two distinct sources for two distinct tasks.

Possible Council-3 dispositions:

| Option | Effect |
|---|---|
| **A.** Per-task interpretation | Each task's beam pair is single-source-derived; the project meets the §3 preserved clause. |
| **B.** Per-system interpretation | The project *as a whole* uses two distinct sources; the §3 preserved clause is violated unless dual-source noise performance is demonstrated for each task. |
| **C.** Task-relevant interpretation | The clause applies only to the Raman task (its origin context); the Doppler-cooling beam pair has no analogous preference, so per-task interpretation is fine for the CW chain. |

Steward stance: Option **C** matches the original intent of the clause (which was about Raman common-mode rejection); Option B is the strictest reading and would force consolidation back to a single-architecture chain.

---

## 4 · What this trigger gates

| Artefact | Status under this trigger |
|---|---|
| [Next-gen 500 mW workplan](../docs/architectures/next-gen.md) | **Unaffected.** Single-architecture deliverable; remains pre-G2 load-bearing. |
| [IC-VECSEL alternative](../docs/architectures/ic-vecsel-alternative.md) | **Forward-looking sketch only.** Cannot be promoted to Phase 4 candidate until §3.1 disposition allows the task-split. |
| [Pulsed-Raman alternative](../docs/architectures/pulsed-raman-alternative.md) | **Forward-looking sketch only.** Cannot be promoted to Phase 4 candidate until §3.1 + §3.2 dispositions allow both the pulsed UV scope and the multi-operating-point scoring. |
| [Architecture requirements specification](../docs/architectures/requirements.md) | **`REQ-IC-002` and `REQ-PR-###` block** are conditional on the trigger disposition. `REQ-NG-###` and `REQ-IC-001` / `REQ-IC-003` / `REQ-IC-004` are unaffected. |
| Phase 4 candidate-slate opening | **Blocked** for the IC-VECSEL + pulsed-Raman pair; **unblocked** for the single-architecture next-gen candidate (subject to G1 + G2 closures). |

---

## 5 · Process and timeline

This is a Charter-§9 deliberation request. Disposition is owned by Council-3 with Integrator sign-off per Charter §9. The Steward (filer of this trigger) does not unilaterally decide.

**Steward asks Council-3 to:**

1. Read this trigger and the underlying [review entry](2026-05-08-architecture-review-tightening-specs.md).
2. Dispose of the three sub-questions in §3 above (§3.1 CHARTER §3 scope · §3.2 reference-triple anchoring under task-split · §3.3 single-source-derived beam pair clause).
3. Issue a written disposition (`logbook/YYYY-MM-DD-council-3-disposition-task-split.md`) recording the resolution, any Charter version bump implied (v1.0 → v1.1 if §3.1-B applies), and any Phase 4 scoring-rule amendments implied (§3.2-B or §3.2-C).

**Pending disposition.** Until that disposition lands, the architecture slate operates under the Steward stance recorded in §3 above — i.e. Option **C** for §3.1 (parallel sub-project for pulsed-Raman) and Option **B** or **C** for §3.2 (per-architecture or hybrid scoring). The conditionality is recorded in each affected artefact via explicit "CHARTER §3 conditional" / "paired-architecture conditional" markers; nothing is silently committed.

---

## 6 · References

- [`CHARTER.md`](../CHARTER.md) §1.5 (constraint hierarchy), §3 (scope and non-goals; line 105 pulsed UV exclusion), §5.2 (reference-triple anchoring), §6.1 (success criterion), §9 (deliberation protocol).
- [`logbook/2026-05-08-architecture-review-tightening-specs.md`](2026-05-08-architecture-review-tightening-specs.md) §4.4 + §5 (the review item this trigger answers).
- [`docs/architectures/`](../docs/architectures/) — affected architecture pages.
- [`docs/architectures/requirements.md`](../docs/architectures/requirements.md) — affected requirements artefact.
