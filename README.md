# mg-plus-uv-chain

UV source redesign for ²⁵Mg⁺ detection, cooling, and coherent control.

A reproducible, version-controlled, FAIR design effort to redesign the all-solid-state CW laser source producing radiation near 280 nm for trapped ²⁵Mg⁺. Successor to Friedenauer *et al.*, *Appl. Phys. B* **84**, 371 (2006).

**Status — checked 2026-09-09.** The [literature dossier index](docs/KD-2026-XXX-uv-280nm.md#entry-index) records **9 of 15 entries past SCAFFOLD** (8 POPULATING, 1 DRAFT). These are dossier topics, distinct from the **22 per-paper extraction files** under [data/literature/](data/literature/). The [September review card](logbook/2026-09-09-repository-review-task-card.md) tracks numerical corrections and documentation work; the [correction record](logbook/2026-09-09-public-record-corrections.md) records progress. The [inventory](docs/components/inventory.md#agile-receipt) includes the Agile mirror receipt and selected coating data.

Phase 2 baseline measurement remains unblocked. G1 and G2 remain OPEN; G3 has been CLOSED since 2026-05-01 (reference triple locked). Architecture-specific simulation and degradation-dependent comparison inputs remain subject to their [gate conditions](#status-of-kill-gates-charter-51). The Charter remains frozen at v1.0.

**Steward.** Ulrich Warring (Albert-Ludwigs-Universität Freiburg, AG Schätz).

**Project site (GitHub Pages).** [Project overview](https://uwarring82.github.io/mg-plus-uv-chain/), built from `main:/docs` using Jekyll. The site introduces the optics, calculations and current status. Borrowed visual assets use **Handbook (MIT)** licensing and **Model B (distributed copies pinned by checksum)**; attribution and hashes are in [asset provenance](docs/assets/SOURCE.md).

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

Selected paths present in the repository:

```text
mg-plus-uv-chain/
├── CHARTER.md                  Frozen at v1.0; canonical design document
├── README.md                   This file
├── CONVENTIONS.md              Units, code and contribution conventions
├── CITATION.cff                Software citation metadata
├── LICENSE                     MIT (code)
├── LICENSE-DOCS                Document-licence scope and prior declaration
├── LICENSES.md                 Licence map and pending assignments
├── endorsement.md              Historical scope and attribution record
├── src/
│   ├── parameters.py           SI constants and locked reference values
│   └── boyd_kleinman.py        One of the generic optical-model utilities
├── constraints/                Constraint derivations; draft status noted in each file
│   ├── raman-requirements.md
│   ├── loss-budget.md
│   └── phase-noise-budget.md
├── docs/
│   ├── KD-2026-XXX-uv-280nm.md  Literature dossier (Phase 1)
│   ├── architectures/          Candidate sketches and requirements
│   ├── components/             Baseline, stock inventory and seed-laser records
│   ├── tutorials/              Generated tutorials and supporting documentation
│   ├── hardware-status.md     Dated hardware record
│   └── status.md              Dated phase/gate snapshot
├── tests/                      Numerical tests and import guards; CI work in RC-06
├── notebooks/                  Tutorial sources, diagnostics and explorations
├── scripts/                    Rendering and conversion tools
├── data/
│   ├── README.md               Data layout and measurement-metadata conventions
│   ├── literature/             Per-paper extractions and notes
│   └── lab notes/              Converted lab records; private attachments excluded
└── logbook/
    ├── _templates/
    │   └── gate-closure.md     §5.3 template
    └── 2026-09-09-repository-review-task-card.md
```

**Planned, not yet present:** `data/baseline/` for Phase 2 measurement deposits,
and `docs/architecture-comparison.md`, `docs/stability-budget.md` and
`docs/degradation-protocol.md` as dedicated outputs. Current architecture
requirements live under [docs/architectures/](docs/architectures/); measurement
metadata conventions are in [data/README.md](data/README.md).


---

## Status of kill-gates (CHARTER §5.1)

| Gate | Blocks | Status |
|---|---|---|
| G1 | Phase 3 architecture-family-specific simulation | OPEN — awaiting Phase 2 attribution of 14-GHz domain |
| G2 | Phase 4 / Phase 5 acceptance of degradation rate | OPEN — awaiting Phase 2 §8.2 protocol reproducibility |
| G3 | Phase 4 architecture comparison | **CLOSED** 2026-05-01 — see [`logbook/2026-05-01-gate-g3-closure.md`](logbook/2026-05-01-gate-g3-closure.md) |

Gate closure requires the recorded acknowledgement defined in Charter §5.3, using [`logbook/_templates/gate-closure.md`](logbook/_templates/gate-closure.md).

---

## How to contribute

Ulrich Warring is accountable for this project. External issues, suggestions and technical reviews are welcome. Changes to Charter §1.5 Level 0/1 constraints, §6 success criteria or gate closures require a recorded review under Charter §9. The historical `council-3` issue label identifies that review process; it does not imply a separately staffed committee.

The Charter is frozen at v1.0. Revisions require a documented v1.x cycle.

---

## Citation

If this repository or its outputs inform your work, please cite as in [`CITATION.cff`](CITATION.cff). A Zenodo DOI has not been verified. No tags or GitHub releases were present on the remote when checked on 2026-09-09. Cite the repository and the commit used; the frozen Charter version is not evidence of a tagged software release.

## License

Licensing is specified by content in the [licence map](LICENSES.md):

- **Coastline — CC-BY-SA-4.0:** mapped framework and navigation documents, including this README; attribution and ShareAlike apply.
- **Sail — CC-BY-NC-SA-4.0:** mapped authored analyses; attribution, NonCommercial and ShareAlike apply.
- **Handbook — MIT:** borrowed site assets and mapped layouts. **Code — MIT.**
- **Data — CC-BY-4.0:** mapped structured extractions and measurement data.

These are licence categories, not ratings of scientific confidence. The map
records remaining scope questions and prior declarations; third-party sources
retain their own terms. [LICENSE-DOCS](LICENSE-DOCS) explains document scope.
