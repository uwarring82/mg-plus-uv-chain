# BC-G · M2′ piezo-mirror substrate mechanics — results

**Phase:** BC-G of the BBO coating-run WP ([`workplan.md`](workplan.md)),
a **post-closure addendum** reopened 2026-05-21.
**Steward:** Ulrich Warring.
**Status:** RESULT artefact; the load-bearing decision is implemented in
[`specs/M2-plane-HR.md`](specs/M2-plane-HR.md) and re-frozen at BC-G close.
**Log:** [`bc-g-log.md`](bc-g-log.md).

This file is the **reference document** for sizing a piezo-mounted
cavity-lock mirror against a chosen actuator. It is written to be reused
by future builds (the steward's explicit ask), so the derivation is kept
self-contained.

---

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** **no.** The substrate dimension does not
  change the reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz,
  Γ_sc = 2.0 × 10⁴ s⁻¹}` ([CHARTER §1.5](../../CHARTER.md)). A higher M2′
  servo bandwidth *helps the lock meet* the existing `S_φ(f)` budget; it
  does **not** redefine that budget. No new anchor is proposed.
- **Affects Level 1 parameter?** **no.** UV-power-at-input and
  source-linewidth budgets are unchanged. Lock bandwidth is a *build
  quality* axis, not a Level-1 quantity.
- **Affects success criterion?** **no.**
- **Coastline / Sail.** *Sail* — parameter optimisation on the frozen
  Friedenauer geometry. The PI piezo catalog values consumed below are
  *Coastline* (vendor-anchored, [PI PICMA® stack datasheet](#e--sources)).
- **Anti-seeding / gates.** No `/src/` change. The substrate size touches
  none of G1 (14-GHz unlockable domain — crystal + geometry inherited),
  G2 (UV degradation — M4′ only), or G3 (closed). See
  [`closure.md`](closure.md) §H for the WP-level gate inheritance this
  addendum does not alter.

---

## A · Why this addendum exists

The frozen [`specs/M2-plane-HR.md`](specs/M2-plane-HR.md) carried two
defects inherited from the Friedenauer LBO baseline without
re-derivation for the BBO stage:

1. **Stale actuator reference.** The page named a
   "Thorlabs AE020304D04-class or equivalent" piezo. The build actually
   uses **PI P-887.31** (steward, 2026-05-21). The two are not
   interchangeable for a bandwidth argument.
2. **Substrate mass + face mismatch.** The page specified the same
   Ø 12.7 × 6.35 mm blank as the HR/dichroic seats (a blanket default,
   not a derived choice). At **1.77 g** it is the heaviest reasonable
   blank, *and* Ø 12.7 mm **overhangs** the P-887.31 7 × 7 mm actuator
   face — an unsupported rim adds a low-frequency cantilever mode that
   *lowers* the loaded resonance, the opposite of the intent.

Friedenauer additionally glued the LBO mirror to a **lead disk** to
*lower* resonance and absorb vibration. For the BBO last-stage lock we
want the opposite (higher resonance → higher servo bandwidth), so **no
added mass / no lead disk** on the new build.

---

## B · The sizing model (reusable)

A piezo-mounted mirror behaves as a clamped-free spring–mass system. The
servo unity-gain frequency (UGF) must sit a factor **~3–5 below** the
first loaded mechanical resonance `f_loaded` (more, without a notch
filter), so `f_loaded` is the quantity to maximise.

```
f_loaded(M) = f_clamp · sqrt( m_p,eff / (m_p,eff + M) )
```

- `f_clamp` = unloaded resonance with **one end clamped**. PI quotes the
  resonance "unbelastet, beidseitig frei" (unloaded, both ends free) and
  notes *"bei einseitiger Einspannung halbiert sich der Wert"* — clamped
  one side, **`f_clamp = f_freefree / 2`**.
- `m_p,eff` = the actuator's own effective (modal) moving mass, back-out
  from the catalog: `m_p,eff = k / (2π·f_clamp)²`.
- `M` = added mirror (+ bond + any mount cap) mass.

**The saturation result.** For `M ≪ m_p,eff`, `f_loaded → f_clamp` and is
**insensitive to `M`**. Shrinking the mirror only helps until
`M ≈ m_p,eff`; below that the actuator's own mass dominates and further
shrinking buys nothing while adding handling / coating-fixture risk.
**This is why "smaller is always better" is wrong** — the actuator
stiffness/length, not the mirror diameter, is the real lever.

**Mount-compliance derating.** The catalog `k` is the quasi-static
large-signal stiffness in an ideal rigid clamp. Real mounts, bond lines,
and preload springs add series compliance that lowers `f_loaded`. The
Friedenauer loaded resonance (~18 kHz, [architecture-review note](../2026-05-08-architecture-review-tightening-specs.md))
against a heavy half-inch blank on a stiff stack calibrates the derating
at **≈ 0.6×** the rigid-clamp estimate. All "real" columns below apply
that factor; treat them as the engineering expectation, not a guarantee.

---

## C · The two tiers

Effective masses (fused silica ρ = 2.20 g/cm³):

| Blank | Volume | Mass `M` |
|---|---|---|
| Ø 12.7 × 6.35 mm (frozen default) | 804 mm³ | **1.77 g** |
| Ø 6.35 × 2.0 mm (Tier 1) | 63.3 mm³ | **0.139 g** |
| Ø 5.0 × 1.5 mm (Tier 2) | 29.5 mm³ | **0.065 g** |

Actuator parameters (PI PICMA® stack, [datasheet](#e--sources)):

| Actuator | A×B×L | Stroke (0–100 V) | `k` | `f_freefree` | `f_clamp` | `m_p,eff` |
|---|---|---|---|---|---|---|
| **P-887.31** (Tier 1) | 7×7×13.5 mm | 11 µm | 130 N/µm | 90 kHz | **~45 kHz** | **~1.63 g** |
| **P-885.11** (Tier 2) | 5×5×9 mm | 6.5 µm | 100 N/µm | 135 kHz | **~67.5 kHz** | **~0.56 g** |

Loaded resonance `f_loaded(M)` and the resulting servo envelope:

| Configuration | `f_loaded` (rigid) | `f_loaded` (real, ×0.6) | UGF (`f/3`–`f/5`) | vs Friedenauer |
|---|---|---|---|---|
| **Frozen** Ø12.7×6.35 on P-887.31 | 31.2 kHz | ~19 kHz | ~4–6 kHz | ~1× (≈ baseline) |
| **Tier 1** Ø6.35×2.0 on P-887.31 | **43.2 kHz** | **~26 kHz** | **~6–9 kHz** | **~1.5×** |
| **Tier 2** Ø5.0×1.5 on P-885.11 | **63.9 kHz** | **~38 kHz** | **~10–13 kHz** | **~2.5×** |
| ceiling on P-887.31 (`M→0`) | 45 kHz | ~27 kHz | — | — |
| ceiling on P-885.11 (`M→0`) | 67.5 kHz | ~40 kHz | — | — |

**Reading the table.**
- The frozen Ø12.7 row reproduces the Friedenauer ~18 kHz loaded
  resonance once derated — the model is calibrated, not assumed.
- Almost all of Tier 1's gain is the *first* step off the 1.77 g blank
  (31 → 43 kHz). The Ø6.35 → Ø5 → Ø4 sequence on P-887.31 moves
  `f_loaded` by < 2 kHz: the P-887.31's own 1.63 g effective mass has
  saturated it. **Ø 6.35 mm is the right stop point on P-887.31.**
- Tier 2's gain is real and comes from the **actuator**, not the mirror:
  the shorter, lighter P-885.11 raises the clamped ceiling from 45 → 67.5
  kHz. Its 6.5 µm stroke still gives ≈ 23 half-waves ≈ **15 GHz** optical
  capture on the 470 mm ring (FSR ≈ 638 MHz) — ample for acquisition +
  slow drift, so **no fast/slow split is needed**. (P-887.31's 11 µm →
  ≈ 25 GHz, for reference.)

**Retired target.** An earlier review floated UGF ≥ 20 kHz. Given the
P-887.31 clamped ceiling (~45 kHz) and ~0.6× mount derating, **20 kHz UGF
is unreachable on P-887.31 at any mirror size** and marginal even on the
shortest PICMA chips. The defensible target is **UGF ~10 kHz** (Tier 2),
a genuine ~2.5× over Friedenauer without exotic hardware.

---

## D · Decisions

### D.1 · Implemented (coating spec, this WP)

**Tier 1 is the BC-G default and is implemented in
[`specs/M2-plane-HR.md`](specs/M2-plane-HR.md):**

> **M2′ blank = Ø 6.35 × 2.0 mm Herasil**, λ/10 P–V @ 633 nm over
> CA ≥ 4 mm, no lead disk, dimensioned to glue onto the **PI P-887.31**
> (7 × 7 mm face) without overhang.

Rationale: it fixes the real coating-spec defects (overhang, mass, stale
actuator ref) with **zero build/inventory change**, and lands at the
engineering stop point where P-887.31's own mass saturates the
resonance. Going below Ø 6.35 mm on this actuator adds handling / vendor
fixture risk for < 2 kHz of resonance.

### D.2 · Documented parallel option (build/procurement KD)

**Tier 2 is documented but is a *build-item* decision, not a coating
decision**, because it changes the actuator and the mount, not just the
blank:

> **M2′ blank = Ø 5.0 × 1.5 mm Herasil** (Ø 4.5–5.0 mm to preserve
> centring margin on the 5 × 5 face) on a **P-885.11-class** short stack.

Carry to the procurement / build KD (KD-UV280-005 / -007), which must
check:
- **Mount geometry** — shorter stack needs a different spacer/body.
- **Driver capacitance / current** — P-885.11 (≈ 0.6 µF class) differs
  from P-887.31 (2.2 µF); confirm the existing amp sources the current
  at the target UGF.
- **Thermal path** — a shorter stack lowers mirror-to-mount thermal
  impedance (minor, generally favourable).

Because the coating blank is the only thing the **vendor** needs, both
tiers are quoted trivially: a Ø 5.0 mm blank covers Tier 2 and still
glues (with generous margin) onto P-887.31, so a future Tier-1→Tier-2
actuator swap need not re-quote the optic if the build elects to order
the Ø 5.0 mm size up front. The M2′ sheet states the Tier-1 Ø 6.35 mm as
the spec and names Ø 5.0 mm as the Tier-2 alternative blank.

---

## D.3 · Per-element substrate-thickness review (closes add-on 1 part a)

The original add-on also asked that **thickness be specified, not
defaulted**. Reviewing the blanket 6.35 mm per element:

| Element | Sees | Thickness call |
|---|---|---|
| M1′ (plane IC) | 559 nm only (reflect) | **keep 6.35 mm** — no transit; thickness is mechanical only |
| **M2′** (plane HR, piezo) | 559 nm only (reflect) | **→ 2.0 mm** — mass-driven, per §C |
| M3′ (curved HR) | 559 nm only (reflect) | **keep 6.35 mm** — curved substrate; thickness aids figure stability under mount stress |
| M4′ (curved dichroic OC) | 559 nm reflect **+ 280 nm transit** | **keep 6.35 mm** — see below |

**M4′ — the only element where thickness has an optical consequence.**
280 nm transits the M4′ substrate. UV-grade fused silica (Herasil /
Suprasil-class) internal transmittance at 280 nm is ≳ 99.9 %/cm, so
6.35 mm absorbs **≲ 0.06 %** of the transmitted UV — negligible against
the 5 % T-budget headroom on the M4′ page. Thinning the substrate to
reduce UV absorption is therefore **not worth it**, and would *cost*
surface-figure robustness on a curved, dual-coated optic. **Keep
6.35 mm on M4′.** (The fluoride/CaF₂ upgrade tier in M4′ §B has different
UV absorption but is forward-looking and out of scope here.)

Net: thickness is now an explicit per-element decision; only M2′ moves.

---

## E · Sources

- **PI PICMA® stack multilayer actuator datasheet** (steward-supplied,
  2026-05-21). P-887.31: 7×7×13.5 mm, 11 µm (0–100 V), `k` = 130 N/µm,
  resonance 90 kHz unloaded both-free. P-885.11: 5×5×9 mm, 6.5 µm,
  `k` = 100 N/µm, resonance 135 kHz. Footnote: resonance measured at
  1 V_pp unloaded both ends free; **halves under one-sided clamping**.
- Friedenauer loaded-resonance / HC-bandwidth anchor (~18 kHz):
  [`logbook/2026-05-08-architecture-review-tightening-specs.md`](../2026-05-08-architecture-review-tightening-specs.md).
- Cavity FSR (638 MHz at L = 0.470 m): [`constants.md`](constants.md) §A.
- Frozen M2′ page this addendum amends:
  [`specs/M2-plane-HR.md`](specs/M2-plane-HR.md).

---

## F · What is preserved for the next build of this kind

1. **The sizing model in §B** is the reusable artefact: pick the
   actuator first, back out `m_p,eff` from `k` and the *clamped-free*
   resonance, then the mirror only matters until `M ≈ m_p,eff`.
2. **The stop-point discipline** — shrinking the mirror past the
   saturation knee trades real handling/vendor risk for sub-kHz gains.
3. **Bandwidth lives in the actuator length/stiffness**, not the optic.
   A coating-run WP should name the actuator and treat the blank as a
   dependent variable, not the lever.
