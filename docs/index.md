---
title: mg-plus-uv-chain
description: UV source redesign for ²⁵Mg⁺ detection, cooling, and coherent control
---

# mg-plus-uv-chain

A reproducible, version-controlled, FAIR design effort to redesign the all-solid-state CW laser source producing radiation near 280 nm for trapped **²⁵Mg⁺** ions. Successor to Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006), incorporating two decades of progress in fibre and VECSEL sources, nonlinear crystal options, cavity-locking schemes, UV-induced degradation diagnostics, and Raman / spin–motion coherent control.

The project is governed by a frozen [Charter v1.0](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) under Council-3 ADM-EC stance attribution. Steward: Ulrich Warring (Albert-Ludwigs-Universität Freiburg, AG Schätz).

---

## Why this site

The repository itself is the canonical record. This site is a navigational index for readers who want the gist before reading the Charter.

- **[Principles](principles.html)** — the governance grammar: constraint hierarchy, kill-gates, outcome classification, anti-seeding, asymmetric erosion protection.
- **[Calculations](calculations.html)** — what we have computed so far against the Friedenauer 2006 baseline, and what the recomputation tells us.
- **[Status](status.html)** — kill-gate state, dossier population, what is unblocked, what is still gated.

If you want the source: [GitHub repository](https://github.com/uwarring82/mg-plus-uv-chain) · [Charter](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CHARTER.md) · [Phase 1 dossier](KD-2026-XXX-uv-280nm.html) · [BK recalculation notebook](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/2026-05-01-friedenauer-bk-recalculation.py)

---

## At a glance

| Item | State |
|---|---|
| Charter version | v1.0, frozen 2026-04-30 |
| Phase 0 (Charter, scaffold) | **Complete** |
| Phase 0.5 (constraint extraction) | Reference triple locked; G3 closed 2026-05-01 |
| Phase 1 (literature dossier) | In progress — 5 of 15 entries past SCAFFOLD |
| Phase 2 (baseline measurement) | Unblocked, not yet started |
| Phase 3 (simulation framework) | Architecture-neutral utilities only; family-specific code blocked by G1 |
| Phase 4 (architecture comparison) | G3-unblocked; G2-dependent inputs still gated |
| Phase 5 (build and validation) | Not started |
| Phase 6 (publication) | Not started |
| Tests | 78/78 passing (24 parameters, 22 Boyd–Kleinman, 31 ABCD, 1 surrogate-import) |
| Repository visibility | Public from day one |

---

## Three things to remember

1. **The constraint chain is upstream-anchored.** Source-side numbers (≥ 500 mW at 280 nm, linewidth bounds, drift envelopes) are *derived* from ion-side Raman / detection / cooling task constraints, not asserted in isolation. See [Principles → §1.5 Constraint hierarchy](principles.html#level-0--level-1--level-2-constraint-hierarchy).

2. **Architecture choice is deferred behind kill-gates.** No architecture-family-specific simulation may be committed to `/src/` until the 14-GHz unlockable domain (Charter §8.1) is attributed or formally classified Underdetermined. See [Principles → Kill-gates](principles.html#kill-gates).

3. **The Raman intensity requirement is below the headline ≥ 500 mW target.** A first-pass loss-budget analysis shows Raman alone needs ≪ 15 mW source-side; the binding scoring axes for Phase 4 are expected to be *phase coherence, UV robustness, and thermal/nonlinear load*, not raw power. See [Calculations → Raman headroom finding](calculations.html#raman-power-headroom).

---

## License and citation

- Code: [MIT](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSE)
- Documents (Charter, dossiers, this site): [CC-BY-4.0](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSE-DOCS)
- Citation: see [`CITATION.cff`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CITATION.cff)
- Endorsement scope: local; see [`endorsement.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/endorsement.md)
