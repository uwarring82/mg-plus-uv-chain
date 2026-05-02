---
layout: default
title: mg-plus-uv-chain
description: UV source redesign for ²⁵Mg⁺ detection, cooling, and coherent control. Single-steward FAIR effort under Council-3 governance.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship at Albert-Ludwigs-Universität Freiburg. No external endorsement implied. The Charter is a coastline, not a claim about underlying physics beyond what is already endorsed elsewhere.</p>

<p class="eyebrow">Project page</p>

# A reference page that stays open to correction.

This page summarises the principles, calculations, and current status of `mg-plus-uv-chain` — a redesign of the all-solid-state CW laser source producing radiation near 280 nm for trapped **²⁵Mg⁺** ions. Successor to Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006), incorporating two decades of progress in fibre and VECSEL sources, nonlinear crystal options, cavity-locking schemes, UV-induced degradation diagnostics, and Raman / spin–motion coherent control.

The repository itself is the canonical record. This site is a navigational index for readers who want the gist before reading the [Charter](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md).

---

## Three pages

- **[Principles](principles.html)** — the governance grammar: §1.5 constraint hierarchy, kill-gates, outcome classification, anti-seeding clause, asymmetric erosion protection. Each section labelled *Coastline* (hard, testable) or *Sail* (adaptive, contextual).
- **[Calculations](calculations.html)** — what has been computed against the Friedenauer 2006 baseline, what the recomputation tells us, and which open questions the dossier should resolve.
- **[Status](status.html)** — kill-gate state, Phase 1 dossier population, what is unblocked, what is still gated. Snapshot at HEAD.

If you want the source: [GitHub repository](https://github.com/uwarring82/mg-plus-uv-chain) · [Charter v1.0](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) · [Phase 1 dossier](KD-2026-XXX-uv-280nm.html) · [BK recalculation notebook](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/2026-05-01-friedenauer-bk-recalculation.py)

---

## At a glance

| Item | State |
|---|---|
| Charter version | v1.0, frozen 2026-04-30 |
| Phase 0 (Charter, scaffold) | Complete |
| Phase 0.5 (constraint extraction) | G3 closed 2026-05-01; reference triple locked |
| Phase 1 (literature dossier) | In progress — 5 of 15 entries past SCAFFOLD |
| Phase 2 (baseline measurement) | Unblocked, not yet started |
| Phase 3 (simulation framework) | Architecture-neutral utilities only; family-specific code G1-blocked |
| Phase 4 (architecture comparison) | G3-unblocked; G2-dependent inputs still gated |
| Phase 5 (build and validation) | Not started |
| Phase 6 (publication) | Not started |
| Tests | 78 / 78 passing |
| Repository visibility | Public from day one |

---

## Three things to remember

1. **The constraint chain is upstream-anchored.** Source-side numbers (≥ 500 mW at 280 nm, linewidth bounds, drift envelopes) are *derived* from ion-side Raman / detection / cooling task constraints, not asserted in isolation. See [Principles → Constraint hierarchy](principles.html#constraint-hierarchy-coastline).
2. **Architecture choice is deferred behind kill-gates.** No architecture-family-specific simulation may be committed to `/src/` until the 14-GHz unlockable resonance domain is either attributed or formally classified Underdetermined. See [Principles → Kill-gates](principles.html#kill-gates-coastline).
3. **Raman intensity is far below the headline ≥ 500 mW target.** A first-pass loss-budget analysis shows Raman alone needs ≪ 15 mW source-side; the binding scoring axes for Phase 4 are expected to be *phase coherence, UV robustness, and thermal/nonlinear load*, not raw power. See [Calculations → Raman power headroom](calculations.html#raman-power-headroom).

---

## Licence

| Layer | Content | Licence | Notes |
|---|---|---|---|
| Charter and governance documents | `CHARTER.md`, `endorsement.md`, `CONVENTIONS.md`, `constraints/` | CC-BY-4.0 | See [`LICENSE-DOCS`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSE-DOCS) |
| Code | `src/`, `tests/` | MIT | See [`LICENSE`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSE) |
| Borrowed site assets (`docs/assets/`) | `tokens.css`, `emblem-32.svg`, `wordmark-full.svg`, `site.css` (derived) | MIT | Borrowed from [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) at commit `ee01c80` per Model B. See [`docs/assets/SOURCE.md`](assets/SOURCE.md). |
| Fonts | IBM Plex Mono, Crimson Pro | SIL OFL 1.1 | Loaded from Google Fonts; not relicensed. |

The cd-rules split-licence pattern (CC-BY-SA for coastlines, CC-BY-NC-SA for sails, MIT for handbook assets) is recommended but not yet adopted in this repository. Adoption would be a Steward + Council-3 action; flagged here for future deliberation.
