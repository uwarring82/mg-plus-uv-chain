# mg-plus-uv-chain

UV source redesign for ²⁵Mg⁺ detection, cooling, and coherent control.

A reproducible, version-controlled, FAIR design effort to redesign the all-solid-state CW laser source producing radiation near 280 nm for trapped ²⁵Mg⁺. Successor to Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006).

**Status.** Phase 0 complete (Charter v1.0 frozen 2026-04-30). Phase 0.5 (constraint extraction) begins next.

**Steward.** Ulrich Warring (Albert-Ludwigs-Universität Freiburg, AG Schätz).

---

## Quick navigation

This repository is governed by the [Charter](CHARTER.md). The Charter is the canonical reference; this README is a navigational index.

**If you want to know…**

| Question | Look in |
|---|---|
| Why this redesign exists, and what it is *not* | [CHARTER.md §1, §3](CHARTER.md) |
| What constraints flow from the ion physics down to the source | [CHARTER.md §1.5](CHARTER.md) (Level 0 → Level 1 → Level 2) |
| What "≥ 500 mW at 280 nm" actually means | [CHARTER.md §2](CHARTER.md) and [`constraints/`](constraints/) |
| Which architectures are on the table | [CHARTER.md §4](CHARTER.md) (quadrupling / SFG / hybrid / direct deep-UV) |
| The phase plan and what blocks what | [CHARTER.md §5, §5.1, §5.3](CHARTER.md) (phases, kill-gates, gate closure protocol) |
| How architectures will be compared | [CHARTER.md §5.2](CHARTER.md) (six fixed scoring axes, reference-triple anchoring) |
| What "success" means | [CHARTER.md §6](CHARTER.md) |
| Known unsolved boundaries (14-GHz domain, UV degradation, coatings) | [CHARTER.md §8](CHARTER.md) |
| Governance, vetoes, logbook discipline | [CHARTER.md §9](CHARTER.md) |
| Why the Charter has the shape it does | [`logbook/2026-04-30-kickoff.md`](logbook/2026-04-30-kickoff.md) (nine-cycle deliberation history) |
| How to cite this work | [`CITATION.cff`](CITATION.cff) |

---

## Repository layout

```
mg-plus-uv-chain/
├── CHARTER.md                  Frozen at v1.0; canonical design document
├── README.md                   This file
├── CONVENTIONS.md              Code, units, naming, commit conventions
├── CITATION.cff                Citation metadata
├── LICENSE                     MIT (code)
├── LICENSE-DOCS                CC-BY-4.0 (documents)
├── endorsement.md              Coastline Template v2.0 endorsement marker
├── src/
│   ├── parameters.py           SI-units contract (single source of truth)
│   └── …                       (architecture-neutral utilities pre-G1; family-specific code post-G1)
├── constraints/                Immutable Level 0/1 reference objects (§1.5)
│   ├── raman-requirements.md
│   ├── loss-budget.md
│   └── phase-noise-budget.md
├── docs/
│   ├── KD-2026-XXX-uv-280nm.md Literature dossier (Phase 1)
│   ├── architecture-comparison.md
│   ├── stability-budget.md
│   └── degradation-protocol.md
├── tests/                      ≥ 90 % coverage target; mechanical enforcement of §5.1
├── notebooks/                  Exploratory; pre-G1 work tagged
├── data/
│   ├── baseline/               Measurements on the existing chain (Phase 2)
│   └── literature/             Parameters extracted from cited works
└── logbook/
    ├── _templates/
    │   └── gate-closure.md     §5.3 template
    └── 2026-04-30-kickoff.md   Charter deliberation history
```

---

## Status of kill-gates (CHARTER §5.1)

| Gate | Blocks | Status |
|---|---|---|
| G1 | Phase 3 architecture-family-specific simulation | OPEN — awaiting Phase 2 attribution of 14-GHz domain |
| G2 | Phase 4 / Phase 5 acceptance of degradation rate | OPEN — awaiting Phase 2 §8.2 protocol reproducibility |
| G3 | Phase 4 architecture comparison | OPEN — awaiting Phase 0.5 reference triple |

Each gate closes via an Integrator-acknowledged logbook entry following [`logbook/_templates/gate-closure.md`](logbook/_templates/gate-closure.md).

---

## How to contribute

This is a single-steward project under public-from-day-one FAIR conventions. External issues, suggestions, and reviews are welcome via standard GitHub mechanisms. Substantive proposals affecting Charter §1.5 Level 0/1 constraints, §6 success criteria, or kill-gate closures require Council-3 deliberation per CHARTER §9 — open an issue with the `council-3` label.

The Charter is frozen at v1.0. Revisions require a documented v1.x cycle.

---

## Citation

If this repository or its outputs inform your work, please cite as in [`CITATION.cff`](CITATION.cff). A Zenodo concept-DOI is registered against the v1.0 tag.

## License

- Code: [MIT](LICENSE)
- Documents (Charter, dossiers, logbook entries): [CC-BY-4.0](LICENSE-DOCS)
