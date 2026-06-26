# VECSEL systems tutorial; in-house Evernote lab-note extraction

**Steward:** Ulrich Warring
**Date:** 2026-06-26
**Status:** NEW PEDAGOGICAL ARTEFACT + LOCAL-DATA EXTRACTION. A new tutorial [`docs/tutorials/vecsel-systems.md`](../docs/tutorials/vecsel-systems.md) explains the in-house VECSEL seed lasers — gain properties, intracavity filtering, and the parameter sensitivities that set the linewidth — for the **~1120 nm → 280 nm** (cooling/detection/Raman) and **~1140 nm → 285 nm** (photoionisation) systems. Two Evernote lab notes were converted ENEX → Markdown into a new `data/lab notes/` category and used to source the tutorial's in-house numbers. No architecture-family-specific code; no binding parameter changed; no gate advanced.

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — the §1.5 Level 0 row and the G3 reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` are untouched.
- **Affects Level 1 parameter?** no — the tutorial *reports* in-house **measured** device values (étalon FSR ≈ 73 GHz / ≈ 70 GHz, BRF Brewster 57.15°, cavity 127.5 mm, 1.5 % output coupler, PZT ≈ 100 MHz/V, and the VECSEL #2 frequency-noise budget). These are descriptions of existing hardware, not a tightening or relaxation of any Level 1 row. The seed-laser linewidth budget (target ≤ 100 kHz; Friedenauer-parity floor ≈ 200 kHz; stretch ceiling 50 kHz) recorded in [2026-05-08](2026-05-08-vecsel-seed-lasers.md) is unchanged.
- **Affects success criterion?** no.

No Council-3 deliberation required. Tightening-vs-relaxation note: nothing here is a parameter change in either direction; it is documentation plus local-data filing.

## Anti-seeding boundary

The tutorial is pedagogical material over published in-house and external literature; it adds no `/src/` code and no architecture preset. The lab-note extractions live under `data/lab notes/` — a new **local-data** category, sibling to `data/literature/` — not in `/src/`. All of this is admissible pre-G1. **G1 / G2 / G3 status:** G3 closed (2026-05-01); G1 and G2 remain open; nothing in this entry touches them (in particular, UV-degradation / G2 is independent of the seed-laser layer).

## Coastline / Sail

The tutorial labels its sections explicitly: *Coastline* for testable, literature-anchored constraints (gain-medium properties, the filter free spectral ranges, the linewidth criterion) and *Sail* for build-dependent guidance (the 1141 nm "Heidi" system, whose full characterisation is not yet extracted).

---

## 1 · The tutorial

- New page [`docs/tutorials/vecsel-systems.md`](../docs/tutorials/vecsel-systems.md) built around three pillars (steward direction): **gain properties** (resonant-periodic-gain quantum wells, class-A dynamics, gain-peak temperature sensitivity, Henry α), **intracavity filtering** (the BRF / YAG-étalon / PZT hierarchy as a *product-of-losses* mode selection), and **parameter sensitivities → linewidth**.
- Two SVG figures (the project's first content figures): the nested filter / mode-selection hierarchy and the frequency → amplitude-noise conversion chain, both on the site palette.
- The tutorials index was restructured into two tracks (seed-laser systems + SHG enhancement-cavity numerics); the [seed-lasers components page](../docs/components/seed-lasers.md) gained a cross-link.
- A newcomer pass added: learning-objectives box, key-terms glossary, inline glosses, scale callouts, and a "what this proves / does not prove" box.

## 2 · In-house lab-note extraction (ENEX → Markdown)

Two Evernote notes were exported to ENEX and converted to Markdown with a streaming converter (extracts the note body, converts tables/formatting, decodes the embedded `en-media` attachments):

| Note | In-repo Markdown | Source / attachments |
|---|---|---|
| `2021-07 VECSEL project summary` | [`data/lab notes/2021-07-vecsel-project-summary.md`](../data/lab%20notes/2021-07-vecsel-project-summary.md) | fleet #1–#5, assembly/optical-element detail, the **VECSEL #2 frequency-noise budget** |
| `2020-11 VECSEL #2 "Heidi"` (operational diary) | [`data/lab notes/2020-11-vecsel-2-heidi.md`](../data/lab%20notes/2020-11-vecsel-2-heidi.md) | day-by-day operations log for the 1140 nm unit |

**Data-handling policy (new precedent).** The converted Markdown **text** is committed; the binary attachments (102 + 138 images, vendor PDFs) and the source `.enex` files are kept **local-only** via `.gitignore` (`/data/lab notes/*.enex`, `/data/lab notes/*.attachments/`) — the same local-only treatment as `/outreach/`.

**Redaction.** Because the repository is public ([2026-06-26 publication event](2026-06-26-repo-public-and-pages.md)), the "Heidi" operational diary was redacted before commit: lab-internal IP address, internal hostname, and TEC/PID controller register dumps removed; the engineering narrative (diary, observations, target frequencies, the "PID parameters not active — only GAIN" insight) retained.

**Provenance.** Every in-house number folded into the tutorial links back to the 2021-summary Markdown, so the reader can trace each value to its source note. The two earlier Evernote share-links were removed from the tutorial in favour of these in-repo extractions.

## 3 · Rigor revisions (reviewer-driven)

- **Linewidth criterion reframed** from an inequality (`Δν_seed ≪ 18 kHz`) to a **transfer-function** statement: the resonant SHG cavities respond to the residual frequency-noise spectral density *above* the ~18 kHz doubling-cavity lock bandwidth, not to the integrated linewidth. A below/above lock-bandwidth error in the figure and SVG was corrected (the lock *tracks out* sub-bandwidth noise; the *above*-bandwidth residual converts to amplitude noise).
- **Spanke 2025** 101(8) kHz is no longer presented as a proven sub-100 kHz result — it is consistent with the ≤ 100 kHz target but not below it without a delayed self-heterodyne / beat-note measurement.
- **Evidence labels** (`[in-house]`, `[external]`, `[analogue]`, `[inferred]`, `[open]`) added so in-house Heidi data are never silently blended with the Burd 2016 analogue.
- **`docs/references.md` corrected** — Burd 2016: 1117 nm IC = **I-cavity, externally frequency-quadrupled**; 1141 nm VC = **V-cavity, intracavity-doubled to 571 nm** then externally doubled to 285 nm (the prior entry had the topologies reversed).

## 4 · What is *not* in this entry / open items

- **RIN at the SHG lock bandwidth** — the binding figure of merit of §3.4 — is still unmeasured for the in-house build.
- **In-house 1140 nm ("Heidi")** linewidth, output power, and 285 nm conversion route are not yet extracted (the relevant cells in the tutorial are tagged `[open]`).
- **A true sub-100 kHz intrinsic linewidth** has not been demonstrated (measurement-method-limited).
- The Evernote **attachments remain local-only**; only the redacted Markdown text is public.

## See also

- [Tutorial — VECSEL systems (1118 nm and 1141 nm)](../docs/tutorials/vecsel-systems.md)
- [Components — Seed lasers (VECSEL)](../docs/components/seed-lasers.md) · [2026-05-08 steward direction](2026-05-08-vecsel-seed-lasers.md)
- [References — Burd 2016 / 2023, Kiefer/Guth/Spanke lineage](../docs/references.md)
- [2026-06-26 — repository made public; Pages enabled](2026-06-26-repo-public-and-pages.md)
