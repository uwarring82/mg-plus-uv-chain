# Home-built BBO doublers — photographic survey and fold-angle extraction

**Steward:** Ulrich Warring
**Date:** 2026-05-13
**Status:** OBSERVATIONAL RECORD (Phase 1-equivalent literature / lab artefact). Three top-view photographs archived; per-doubler geometric extraction and photogrammetric fold-angle estimate committed to [`docs/components/home-built-doublers.md`](../docs/components/home-built-doublers.md). No architecture-family-specific code; no change to any binding parameter.

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — the §1.5 Level 0 row (³P₁/₂–³P₃/₂ detuning, two-photon Rabi rate, allowed scattering rate) and the G3-closure reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` are independent of the doubling-chain hardware photographed here.
- **Affects Level 1 parameter?** no — the page describes *currently fielded* hardware (Raman / BD / RD lines, all already operational) and does not alter the source-side UV-power, beam-quality, or seed-linewidth budgets. The photogrammetric fold-angle reading is *consistent with* the Friedenauer-stated 27.4° within ±5° and does not propose tightening of any Level 1 row.
- **Affects success criterion?** no.

This entry therefore does not require Council-3 deliberation. It is a **lab-asset survey** with a photogrammetric extraction attached.

---

## 1 · Artefacts landed

Three archive-grade top-view photographs of the **Bermuda ²⁵Mg⁺ apparatus** doublers, committed under [`docs/assets/components/home-built-doublers/`](../docs/assets/components/home-built-doublers/):

| File | Original size | Doubler | State at capture |
|---|---|---|---|
| `bermuda-bd-bbo-doubler-2026-05.jpeg` | 2904 × 1489 px | **BD** — blue-Doppler / cooling, 3s S₁/₂ ↔ 3p P₃/₂ | Active; 559-nm scattered light floods the green channel |
| `bermuda-raman-bbo-doubler-2026-05.jpeg` | 3026 × 1615 px | **Raman** — stimulated-Raman gates between 3s S₁/₂ hyperfine ground states | Laser off, clean service view; input λ/2 rotation mount in frame |
| `bermuda-rd-bbo-doubler-2026-05.jpeg` | 4032 × 2447 px | **RD** — red-Doppler / repump, 3s S₁/₂ ↔ 3p P₁/₂ | Laser off, well lit; distinct black-anodised mount style |

The companion components-page surface is [`docs/components/home-built-doublers.md`](../docs/components/home-built-doublers.md) — Charter idiom applied (endorsement marker, Coastline/Sail boundary, G1/G2/G3 status, anti-seeding clause, per-row `O` / `O*` / `OPEN` provenance, cross-walk to `inventory.md` and `friedenauer-baseline.md`).

Cross-references added on the same commit set:

- One-line entry in the home [docs/index.md](../docs/index.md) lookup row.
- "See also" link from [docs/components/friedenauer-baseline.md](../docs/components/friedenauer-baseline.md).
- Scope-paragraph mention in [docs/components/inventory.md](../docs/components/inventory.md).

---

## 2 · What the photographs do — and do not — establish

**Directly observable (`O`-tier):**

- All three doublers implement the **four-mirror bowtie ring** of Friedenauer 2006 §3 (two plane mirrors on the long-arm side — IC M1' and HC-piezo HR M2' — and two concave focusing seats — HR M3' and OC-with-HT-280 M4' — at the crystal waist).
- All three doublers host a **temperature-controlled, water-cooled BBO oven** centred between M3 and M4.
- The Raman-doubler **Hänsch–Couillaud servo seat** is directly visible: the piezo body (coil-wound) is in-frame behind the M2' optic.
- The RD-doubler **HC servo lead** is directly visible: the red insulated cable enters the M2' mount from the upper edge of the frame.
- The Raman doubler carries an **input λ/2 rotation mount** (Thorlabs, graduated 0–360° scale) ahead of the IC.
- The RD doubler uses a **distinct mount-vendor style** (black-anodised bodies, white substrate-side labels reading `HH56` / `HR56` plus `Rück...` — German for *back*) versus the red-anodised kinematic cubes in the BD and Raman doublers. Cavity layout is unchanged; only the optomechanics differ.
- A small flag in the BD-doubler photo carries the partial label `HR@280 HT@56_` (the trailing digit obscured by green glare).

**Partially visible / inferred (`O*`-tier):**

- The BD doubler's **HC servo seat** placement on M2' is *inferred* from the mount footprint and topology (matching Raman / RD); the piezo body itself is occluded by green flooding and the piezo lead is not separable from other cabling in the green-flooded frame.
- The `HR@280 HT@56_` flag in the BD doubler is **flagged for bench verification** because the visible coating direction does *not* match a Friedenauer M4' OC (`HR @ 559 + HT @ 280`); plausible re-readings are (i) the label belongs to an adjacent UV-pickoff dichroic, not the cavity OC, or (ii) it is a service tag pointing to a different element.
- Photogrammetric fold-angle estimate (§3 below) is `O*` *Sail*: ±5° from substrate-centre pixel-identification, not a bench measurement.

**Not in frame / not establishable from these photos (`OPEN`):**

- Input λ/2 plate (or equivalent polarisation-conditioning optic) for the **BD and RD doublers** — presumed by analogy with the Raman doubler and the *de facto* requirement of any Brewster-cut-BBO cavity, but **not photographed**.
- Coating identities (R-values at 559 nm / T-values at 280 nm) on any fielded mirror.
- BBO-crystal lot per doubler (Raicol 2025 / A-Star 2017 / Castech 2009 from on-shelf inventory, or a lot not in the inventory at all).
- Piezo make / model and HC servo-loop bandwidth (the Friedenauer-stated ~18 kHz loaded-piezo resonance is the cross-cavity reference number; per-doubler measurement is OPEN).
- BBO-oven manufacturer / set-point / stability.
- UV-output power, beam quality, polarization, and drift at each doubler.
- Bench-grade fold angle to ±1° (the photogrammetric ±5° band in §3 is `O*`, not `O`).

---

## 3 · Photogrammetric fold-angle extraction (this work)

**Why this matters.** Friedenauer 2006 §3 states a "full folding angle 27.4°" with "13.7° per focusing mirror" for the BBO ring. Before today, the components-page row for fold angle was tagged `OPEN` ("compatible with the 27.4° full fold but `OPEN` from this view alone"). The photographs do permit a reading — at lower precision than a bench protractor, but enough to resolve "bowtie compatible with Friedenauer" from "wider / squarer" or "tighter" alternative geometries.

**Method.** For each archived JPEG at original resolution, I read off mirror-substrate pixel centres on the four kinematic mounts (M1, M2 plane; M3, M4 curved), then computed at each curved-mirror vertex the angle between (i) the incoming long-arm vector (M1→M3 or M4→M2) and (ii) the outgoing short-arm vector (M3→M4). In a symmetric bowtie this V-opening is Friedenauer's "full folding angle". The X-cross apex (angle between the two long arms at their crossing point in the upper half of the cavity) was computed as a cross-check; in a symmetric bowtie X-apex = 2 × full fold.

**Result.** *Sail* — observational, not a binding parameter. Uncertainty ±5°, dominated by ±20–50 px identification of mirror-substrate centres on each kinematic mount; not by mount-style differences.

| Doubler | Fold at M3 | Fold at M4 | Mean ±5° | X-cross apex | vs Friedenauer 27.4° |
|---|---|---|---|---|---|
| **BD** (green-flooded) | 26.6° | 25.6° | **26°** | 52.2° | within ±2° |
| **Raman** (clean) | 30.5° | 28.0° | **29°** | 58.5° | within ±2° |
| **RD** (clean, black mounts) | 27.4° | 23.1° | **25°** | 50.5° | within ±3° |

**Headline.** All three doublers are built to a Friedenauer-equivalent ~27° full fold within the photogrammetric ±5° band. No doubler reads as a square-ring (45°) or wide bowtie (>35°); none reads tighter than ~20°. The 4° spread between the three mean values **is not resolved as a real build-to-build difference** from these photographs alone — bench measurement to ±1° would close it.

**M3–M4 asymmetry within each doubler.** A 2–4° gap between M3 and M4 V-openings appears in every doubler; this is comparable to the ±5° pixel-identification budget and is best read as photogrammetric noise, not a cavity-asymmetry signal. In the RD doubler the M4 substrate centre is harder to read than the others because the mount face is partly in shadow.

---

## 4 · Errata caught during the work

A labelling swap I introduced in the first draft of [`docs/components/home-built-doublers.md`](../docs/components/home-built-doublers.md): the green-flooded operating photo was titled "Raman" and the clean service view was titled "BD", which is the opposite of what the desktop filenames pin (`bermuda BD BBO doubler_2026_05.jpeg` is the green-flooded one; `bermuda Raman BBO doubler_2026_05.jpeg` is the clean one). The pixel-dimension check (BD = 2904 × 1489; Raman = 3026 × 1615; RD = 4032 × 2447) confirmed the swap.

Fixed in the same commit set: section titles (B.1 Raman → BD, B.2 BD → Raman), image alt-text, image-file references, the per-doubler function blurbs (cooling vs Raman-pair), the HBD-R-* and HBD-BD-* table prefixes (all swapped consistently across §B and §C of the page), and the §C cross-walk row that pairs "piezo directly visible" / "occluded by green flooding" with the right doubler. The RD doubler was unaffected.

This errata note is recorded here so a future reader who sees the page after the fix can still trace the correction trail.

---

## 5 · Charter compliance

**Anti-seeding boundary.** This page is an observational record of *currently fielded* hardware. It belongs to Phase 1 in the sense of an admissible literature-equivalent artefact (`docs/principles.md` "Anti-seeding clause" — Phase 1 dossier population is unblocked; architecture-family-specific simulation in `/src/` is forbidden until G1 closes). The page introduces no new architecture preset, no new simulation code, no new parameter constant. It is therefore admissible in its current form.

**Gate status.** G3 closed 2026-05-01; the reference triple is unaffected by today's entry. G1 (14-GHz unlockable-domain attribution) and G2 (UV-induced degradation at 280 nm) remain open and are not advanced by this entry.

**Provenance tier.** Every observation in [`docs/components/home-built-doublers.md`](../docs/components/home-built-doublers.md) carries an `O` / `O*` / `OPEN` tag in the per-doubler tables, consistent with the convention established in [`docs/components/inventory.md`](../docs/components/inventory.md). The photogrammetric fold-angle extraction is reported with an explicit ±5° uncertainty band derived from the pixel-identification budget; this is observational *Sail* guidance, not a binding *Coastline* parameter.

**Asymmetric erosion protection.** No tightening or relaxation of a Level 0 / Level 1 parameter is proposed. Nothing on this page weakens any committed CHARTER row.

---

## 6 · Suggested follow-on (out of scope of this entry)

In priority order for closing the `O*` / `OPEN` items above:

1. **Close-up of each substrate side-label** in the RD doubler (M1, M2, M3, M4) — the white substrate-side labels (`HH56` / `HR56` / `Rück...`) are the highest-information-density artefact in the three photographs and the RD photo has the best resolution to read them.
2. **Close-up of the `HR@280 HT@56_` flag** in the BD doubler to disambiguate cavity-element vs external-pickoff identity.
3. **Side or oblique view of each crystal oven** to read the oven manufacturer / part number / set-point label (if any).
4. **In-frame ruler photo** (or a calibration shot of the breadboard hole pattern under the same camera position) to lift the breadboard-hole-pitch scale uncertainty and let the cavity round-trip length be read off to ±5 % instead of "consistent with 0.4–0.5 m".
5. **Bench protractor / theodolite measurement** of the full folding angle on at least one of the three doublers, to anchor the photogrammetric reading to ±1° instead of the present ±5° band.
6. **Per-doubler UV-output measurement** (power, beam quality, polarization, drift) — these are operational quantities, not geometric features, and are downstream of the next-gen workplan ([`logbook/2026-05-08-next-gen-500mW-workplan.md`](2026-05-08-next-gen-500mW-workplan.md)).

---

## 7 · See also

- [`docs/components/home-built-doublers.md`](../docs/components/home-built-doublers.md) — companion components-page surface.
- [`docs/components/friedenauer-baseline.md`](../docs/components/friedenauer-baseline.md) — published BBO-ring specification that the three fielded doublers are direct topological relatives of.
- [`docs/components/inventory.md`](../docs/components/inventory.md) — on-shelf stock cross-walked in §C of the components page.
- [`docs/components/seed-lasers.md`](../docs/components/seed-lasers.md) — upstream VECSEL source-class direction (the seed feeds these doublers).
- [`logbook/2026-05-08-next-gen-500mW-workplan.md`](2026-05-08-next-gen-500mW-workplan.md) — the doubling-chain workplan that may take one of the fielded doublers as a candidate physical seat for the next-gen 500 mW build.
- [`logbook/2026-05-08-vecsel-seed-lasers.md`](2026-05-08-vecsel-seed-lasers.md) — companion steward direction on the seed-laser layer.
