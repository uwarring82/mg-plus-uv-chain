---
layout: default
title: mg-plus-uv-chain
description: UV source redesign for ²⁵Mg⁺ detection, cooling, and coherent control. A research project led by Ulrich Warring, AG Schätz.
---

# UV light near 280 nm for trapped magnesium ions

This page summarises the principles, calculations, and current status of `mg-plus-uv-chain` — a redesign of the all-solid-state CW laser source producing radiation near 280 nm for trapped **²⁵Mg⁺** ions. Successor to Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006), incorporating two decades of progress in fibre and VECSEL sources, nonlinear crystal options, cavity-locking schemes, UV-induced degradation diagnostics, and Raman / spin–motion coherent control.

Ulrich Warring, AG Schätz, leads the project. The repository records the measurements, calculations and decisions; the [Charter](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) defines its constraints and gate conditions.

<aside class="banner"><strong>September update.</strong> The Agile mirrors arrived on 7 September; selected supplier coating data are in the <a href="components/inventory.html#agile-receipt">inventory</a>. Numerical and documentation corrections are tracked in the <a href="https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-09-09-repository-review-task-card.md">repository review card</a>.</aside>

---

## Three pages

- **[Principles](principles.html)** — the constraint hierarchy, gate conditions and rules for changing requirements.
- **[Calculations](calculations.html)** — what has been computed against the Friedenauer 2006 baseline, what the recomputation tells us, and which open questions the dossier should resolve.
- **[Status](status.html)** — kill-gate state, Phase 1 dossier population, what is unblocked, what is still gated. Dated project snapshot.

**Source & governance:** [GitHub repository](https://github.com/uwarring82/mg-plus-uv-chain) · [Charter v1.0](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) · [Phase 1 dossier](KD-2026-XXX-uv-280nm.html) · [References](references.html) · [Tutorials](tutorials/) · [Numerical review](review/)

**Architectures:** [overview](architectures/) · [Next-gen 500 mW](architectures/next-gen.html) · [BBO coating-run explainer](architectures/bbo-coating-run.html) · [coating brief & open questions](architectures/bbo-coating-brief.html) · [IC-VECSEL alternative](architectures/ic-vecsel-alternative.html) · [pulsed-Raman alternative](architectures/pulsed-raman-alternative.html) · [shared requirements](architectures/requirements.html)

**Components:** [Friedenauer baseline](components/friedenauer-baseline.html) · [inventory](components/inventory.html) · [seed lasers (VECSEL)](components/seed-lasers.html) · [home-built doublers survey](components/home-built-doublers.html) · [hardware status (seed fleet)](hardware-status.html)

---

## At a glance

*Historical snapshot at 2026-05-22; the September receipt and review are linked above. Numerical claims below await the corrections in the review card.*

| Item | State |
|---|---|
| Charter version | v1.0, frozen 2026-04-30 |
| Kill-gates | **G1 open** (architecture-specific simulation) · **G2 open** (UV-degradation rate) · **G3 closed** 2026-05-01 |
| Phase 0 (Charter, scaffold) | Complete |
| Phase 0.5 (constraint extraction) | Complete — reference triple locked at G3 closure (2026-05-01) |
| Phase 1 (literature dossier) | Populating — 22 extracted reference folders backing the KD-UV280 evidence table (v0.2) |
| Phase 2 (baseline measurement) | Unblocked; not yet started |
| Phase 3 (simulation framework) | Architecture-neutral numerics in place — single-pass SHG, enhancement-cavity solver, SHG cascade, Boyd–Kleinman, ABCD; Friedenauer-2006 cascade cross-check agrees to 1.5 %. Family-specific code still G1-blocked |
| Phase 4 (architecture comparison) | Exploration under way — a slate-of-three (next-gen / IC-VECSEL / pulsed-Raman) over a shared requirements artefact; formal scoring still G2-gated |
| Phase 5 (build & validation) | Not started — first procurement-prep artefact is the frozen BBO coating-run mirror spec (2026-05-20) |
| Phase 6 (publication) | Not started |
| Tests | 142 / 142 passing |
| Repository visibility | Public from day one |

---

## Three things to remember

1. **The constraint chain is upstream-anchored.** Source-side numbers (≥ 500 mW at 280 nm, linewidth bounds, drift envelopes) are *derived* from ion-side Raman / detection / cooling task constraints, not asserted in isolation. See [Principles → Constraint hierarchy](principles.html#constraint-hierarchy-coastline).
2. **Architecture choice is deferred behind kill-gates.** No architecture-family-specific simulation may be committed to `/src/` until the 14-GHz unlockable resonance domain is either attributed or formally classified Underdetermined. See [Principles → Kill-gates](principles.html#kill-gates-coastline).
3. **Raman intensity is far below the headline ≥ 500 mW target.** A first-pass loss-budget analysis shows Raman alone needs ≪ 15 mW source-side; the binding scoring axes for Phase 4 are expected to be *phase coherence, UV robustness, and thermal/nonlinear load*, not raw power. See [Calculations → Raman power headroom](calculations.html#raman-power-headroom).

---

## Licence

This page is **Coastline — [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)**:
reuse requires attribution and ShareAlike. The repository uses several licences:

| Category | Content | Licence |
|---|---|---|
| Coastline | Mapped framework and navigation documents | CC-BY-SA-4.0 |
| Sail | Mapped authored analyses | CC-BY-NC-SA-4.0 (attribution, NonCommercial, ShareAlike) |
| Handbook | Borrowed site assets and mapped layouts | MIT |
| Code | Software and tooling | MIT |
| Data | Mapped structured extractions and measurements | CC-BY-4.0 |
| External fonts | IBM Plex Mono and Crimson Pro | OFL-1.1 |

See the [licence map](LICENSE.html) for file scope and remaining assignment
questions. Borrowed assets use **Model B (distributed copies pinned by
checksum)**; [asset provenance](assets/SOURCE.html) records the upstream source.
