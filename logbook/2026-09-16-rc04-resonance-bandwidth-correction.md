# RC-04: a loaded piezo resonance is not a lock bandwidth

**Date:** 2026-09-16\
**Steward:** Ulrich Warring\
**Licence:** CC-BY-NC-SA-4.0 — logbook entries are Sail per [`logbook/LICENSE.md`](LICENSE.md). This entry is not added to the explicit `LICENSES.md` rows used for the SHG catalogue records; the folder declaration governs it.\
**Starting revision:** `f75120e`\
**Status:** Corrections applied to six artefacts; the RC-04 package remains open.

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No. The Level-1 seed frequency-noise constraint keeps its existing definition and numerical budget; only an unsupported bandwidth attribution is withdrawn.
- Affects success criteria or gate state? No.

G1 and G2 remain OPEN. G3 remains CLOSED (2026-05-01). No simulation code, numerical parameter value, measurement record or drawing artefact changed; nothing was added to `/src/`. This is a withdrawal of an unsupported claim, not a relaxation of a constraint.

## What prompted this

The [cavity-lock electronics record](2026-09-15-shg-cavity-lock-electronics.md) corrected the resonance-versus-bandwidth confusion on the catalogue, photo survey, baseline and seed-laser pages. A repository-wide check found the same equation in six further artefacts, including the machine-readable extraction that those corrected pages cite. RC-04's third bullet asks for exactly this distinction.

## Source check

The publisher PDF (local, uncommitted copy) was read for §3, printed p. 372. The paper states:

- "The second mirror, highly reflective (M2, R > 99.98%), is mounted on a small stacked piezo with high resonance frequency (Thorlabs model AE020304D04, ν_res ≈ 18 kHz loaded)."
- "We glued the piezo to a disk made of lead to absorb vibrations and reduce the resonance frequency of the mirror mount."
- "The dimension of this mirror is very small, allowing for a high servo bandwidth (3 × 3 × 2 mm³)."

The error signal reaches "a proportional-integral-derivative (PID) servo and after amplification (HV amp) is fed to the piezo (PZT) on which the mirror M2 is mounted."

So 18 kHz is a **loaded piezo resonance**. The paper reports **no** measured servo, unity-gain or closed-loop bandwidth, and links the mirror's small dimension to "a high servo bandwidth" only qualitatively. Note also that the lead disk *reduces* the mirror-mount resonance, so the loaded piezo figure is not itself the mount's resonance.

## Changes

| Artefact | Before | After |
|---|---|---|
| [`Friedenauer2006/extracted.yaml`](../data/literature/Friedenauer2006/extracted.yaml) `LBO_M2_piezo_resonance_loaded` | note: "bounds the achievable Hänsch-Couillaud servo bandwidth" | paper quotation with printed page; inference explicitly withdrawn; value unchanged at 1.8e4 Hz |
| [`Friedenauer2006/notes.md`](../data/literature/Friedenauer2006/notes.md) extraction log | "≈ 18 kHz (bounds the achievable servo bandwidth)" | dated correction; gloss withdrawn |
| [`docs/hardware-status.md`](../docs/hardware-status.md) | "above the ~18 kHz doubling-cavity lock bandwidth" | servo band named; loop bandwidth marked unmeasured, with a pointer to the electronics section |
| [`docs/architectures/requirements.md`](../docs/architectures/requirements.md) `REQ-NG-003` | "the SHG-cavity locking bandwidth (~ 18 kHz loaded piezo per [Frie06])" | servo response cited; bandwidth marked unmeasured; resonance identified as such |
| [`docs/tutorials/vecsel-systems.md`](../docs/tutorials/vecsel-systems.md) §3 Coastline label | "(~18 kHz lock bandwidth)" | parenthetical removed; the transfer-function statement stands unchanged |
| [`docs/assets/vecsel-linewidth-conversion.svg`](../docs/assets/vecsel-linewidth-conversion.svg) | "lock bandwidth ≈ 18 kHz"; "tracks out seed FM below ≈ 18 kHz"; footnote naming 18 kHz | "closed-loop bandwidth unmeasured"; tracking described relative to the loop bandwidth; footnote drops the number |
| [`repository review task card`](2026-09-09-repository-review-task-card.md) RC-04 | progress recorded to 2026-09-10 | dated 2026-09-16 progress block; remaining scope listed |

The numerical value ≈ 18 kHz is retained everywhere it appears. Only its interpretation changed.

## What remains open in RC-04

- [`constraints/phase-noise-budget.md`](../constraints/phase-noise-budget.md) and [`bc-g-results.md`](2026-05-20-bbo-coating-run-wp/bc-g-results.md) still carry their own servo-bandwidth wording; `bc-g-results.md` §E cites a "Friedenauer loaded-resonance / HC-bandwidth anchor (~18 kHz)". Both are dated work-package records; their reconciliation is RC-04 acceptance work, not a silent edit.
- The four-document cross-reference table, the harmonic-phase and path-length checks, and the unavailable measurement evidence are unchanged and still required.
- `requirements.md` `REQ-NG-003` still describes its task as bounding the "SHG-cavity-locking-bandwidth-to-amplitude-noise transfer". That wording presumes a loop bandwidth exists but assigns it no value; reviewed and left as is.
- No closed-loop bandwidth has been measured for any in-house doubling cavity. That measurement remains the only route to a supported number.
- `vecsel-linewidth-conversion.svg` is referenced by no page in the repository, though it is still published under `docs/assets/`. Its removal or reuse is a steward decision; it was corrected rather than deleted.

## Validation

- `.venv/bin/python -m pytest -q`: **275 passed, 3 skipped**. The skips are the block-audit regeneration and two viewport/proxy tests that need ezdxf, absent from the standard environment. No test covers this prose.
- `git diff --check` passes.
- The rewritten SVG parses as XML. Publication review with macOS Quick Look found the revised footnote clipped at the left edge; that sentence was wrapped onto two lines without changing its wording. The diagram geometry and colours are unchanged.
- Publication review also confirmed that the parsed extraction differs from the previous revision only in the intended note, with the value and units preserved at 1.8e4 Hz. Every relative link in this entry and the task card's link to it resolves.
- Implementation checks above were supplied with the handoff; publication review did not repeat the full suite for the footnote wrap and logbook updates. Live publication verification follows the documentation commit.
