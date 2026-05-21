# BC-G · M2′ piezo-mirror substrate mechanics — running log

**Phase:** BC-G of the BBO coating-run WP ([`workplan.md`](workplan.md))
— a **post-closure addendum**.
**Steward:** Ulrich Warring.
**Opened:** 2026-05-21 (WP was CLOSED 2026-05-20).
**Status:** CLOSED 2026-05-21 — addendum complete, M2′ page re-frozen.
**Result artefact:** [`bc-g-results.md`](bc-g-results.md).

---

## Why reopen a closed WP

The WP closed 2026-05-20 with five frozen spec pages. On 2026-05-21 the
steward raised two add-ons (deliberation in the session transcript):

1. **Substrate size / thickness** — make thickness an explicit
   per-element decision, and shrink the M2′ piezo mirror for higher
   cavity-lock bandwidth.
2. **Vendor shortlist + substrate-sourcing matrix + a sourcing
   consultant** (e.g. agile-optic.com).

Add-on 1 is **spec content** — it has to touch the frozen M2′ page — so
it is handled here as a reopened amendment phase rather than a silent
edit, consistent with the repo's frozen-artefact discipline. Add-on 2
was already scoped out of this WP (§6 Q4, §10, [`closure.md`](closure.md)
§D item 1) and goes to the **procurement KD**, not here. The steward
chose: *reopen as BC-G* for add-on 1, *new procurement KD* for add-on 2.

The decision to draft **both actuator tiers** (not just the implemented
one) is the steward's: low marginal effort, and a documented both-tier
analysis gives future builds a reference.

---

## CHARTER §9 / boundaries

Carried in full at [`bc-g-results.md` header](bc-g-results.md). Summary:
Level 0/1/success-criterion all **untouched** (a substrate dimension does
not move the reference triple; a faster lock helps *meet* the existing
`S_φ` budget, it does not redefine it). *Sail*; PI catalog values are
*Coastline*. No `/src/` change; G1/G2/G3 unaffected.

---

## 2026-05-21 · Deliberation → decision

### Step 1 — Identify the real actuator

The frozen M2′ page named "Thorlabs AE020304D04-class" — a stale
Friedenauer-LBO inheritance. Steward confirmed the build uses **PI
P-887.31**. The AE0203D04F (3.5 × 4.5 mm face, discontinued) would have
been overhung by any ≥ Ø 4.5 mm mirror anyway; P-887.31's 7 × 7 mm face
admits a Ø 6.35 mm blank.

### Step 2 — Run the clamped-free spring–mass model

Full derivation in [`bc-g-results.md`](bc-g-results.md) §B–§C. Headline:

- P-887.31 clamped-free unloaded resonance ≈ 45 kHz (90 kHz / 2 per the
  PI one-sided-clamping footnote); back-out `m_p,eff` ≈ 1.63 g.
- **The actuator's own 1.63 g effective mass dominates any sane mirror**,
  so loaded resonance *saturates* near 45 kHz. Dropping the frozen 1.77 g
  half-inch blank (31 kHz rigid) to a 0.14 g quarter-inch blank (43 kHz)
  captures essentially all the available gain; below Ø 6.35 mm the curve
  is flat. **The mirror is not the lever — the actuator is.**
- Model calibrates against Friedenauer's measured ~18 kHz loaded
  resonance (heavy blank, ~0.6× mount derating).

### Step 3 — Both tiers

| Tier | Actuator | Blank | `f_loaded` real | UGF | vs Friedenauer |
|---|---|---|---|---|---|
| **1 (implemented)** | P-887.31 (unchanged) | Ø 6.35 × 2.0 mm | ~26 kHz | ~6–9 kHz | ~1.5× |
| **2 (documented)** | P-885.11-class | Ø 5.0 × 1.5 mm | ~38 kHz | ~10–13 kHz | ~2.5× |

- **Tier 1** fixes the overhang + mass + stale-ref defects with **zero
  build change**, at the saturation stop-point. → implemented in
  [`specs/M2-plane-HR.md`](specs/M2-plane-HR.md).
- **Tier 2** reaches the defensible ~10 kHz UGF target, but only by
  swapping the **actuator** (shorter, stiffer stack) — a build/mount
  change. → documented; carried to the procurement / build KD.
- Earlier-floated 20 kHz UGF **retired**: unreachable on P-887.31 at any
  mirror size; marginal even on the shortest PICMA chips after derating.
- No fast/slow split: P-885.11's 6.5 µm stroke (~15 GHz capture) is
  ample single-actuator.

### Step 4 — Per-element thickness review (add-on 1 part a)

Closed in [`bc-g-results.md`](bc-g-results.md) §D.3: only M2′ moves (to
2.0 mm). M4′ keeps 6.35 mm — 280 nm transit through 6.35 mm of UV-grade
FS absorbs ≲ 0.06 %, negligible vs the figure-stability cost of thinning
a curved dual-coated optic.

### Step 5 — Apply to frozen artefacts + re-freeze

- [`specs/M2-plane-HR.md`](specs/M2-plane-HR.md): geometry → Ø 6.35 × 2.0
  mm; actuator ref → P-887.31 (AE0203D04 retired); Tier-2 alternative
  blank noted; resonance rationale + "no lead disk" added; CA ≥ 4 mm.
  Re-frozen **2026-05-21 (BC-G)**.
- [`specs/coating-run-cover-letter.md`](specs/coating-run-cover-letter.md):
  M2′ summary-table row updated; substrate-size non-uniformity note added
  (material uniformity — the §6 Q3 decision — preserved; *size*
  uniformity, an undeliberated default, intentionally broken for M2′).
- [`closure.md`](closure.md): §A substrate line, §C phase index (+BC-G
  row), status + sign-off amended to record the 2026-05-21 reopening.
- [`workplan.md`](workplan.md): header status + §4 BC-G phase + §5 effort
  row.

---

## Acceptance

| Gate | Status |
|---|---|
| M2′ blank derived from the real actuator (not a convention) | ✅ Ø 6.35 × 2.0 mm on P-887.31 |
| Both tiers documented for future reference | ✅ [`bc-g-results.md`](bc-g-results.md) §C–§D |
| Per-element thickness made explicit | ✅ §D.3 |
| Frozen artefacts updated consistently + re-frozen | ✅ M2′ page, cover letter, closure, workplan |
| No `/src/` change; gates untouched; no vendor inquiry sent | ✅ |

**BC-G closed 2026-05-21.** The actuator-swap (Tier 2) and the vendor /
substrate-sourcing questions (add-on 2) are handed to the downstream
procurement / build KD (KD-UV280-005 / -007).
