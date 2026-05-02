# Licence map — `mg-plus-uv-chain`

**Endorsement Marker.** Local stewardship — AG Schätz at Albert-Ludwigs-Universität Freiburg. The licensing architecture below is adopted from [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) §0.3 *Split licence architecture* and §0.10 *Distributed copy with checksum*; the model is not endorsed by external bodies and is local to this repository.

**Effective date.** 2026-05-02 — Council-3 deliberation logged at [`logbook/2026-05-02-licence-split-adoption.md`](logbook/2026-05-02-licence-split-adoption.md). Supersedes the v1.0-cut Steward decision (CHARTER §13.2: "Document license: CC-BY-4.0") which was filed under the Charter's "(license decision pending)" parenthetical at §7. CHARTER.md itself is unchanged (frozen at v1.0); the present split is a derivative governance decision logged outside the Charter freeze.

**Contact.** Ulrich Warring · `https://orcid.org/0000-0001-8081-9718`

---

## 1. Why a split, not a single licence

A uniform CC-BY licence would be internally consistent but externally frictional in three ways.

1. **It under-protects authored interpretive work.** The Kompass dossier and the logbook entries are not just data — they are interpretive analyses whose meaning depends on the epistemic commitments (Council-3 governance, anti-seeding, asymmetric erosion protection) that produced them. Republishing them in a commercial product without those commitments would degrade their meaning. CC-BY allows that without recourse.
2. **It over-restricts framework infrastructure.** The Charter, the constraint hierarchy, the kill-gate protocol, and the outcome-classification vocabulary are *infrastructure* meant to be adopted and adapted by other research groups. A NonCommercial restriction would block adoption inside any university or institute that mixes funding sources — exactly the reuse this project wants to enable.
3. **It blurs the data layer.** Structured literature extractions (`extracted.yaml`) are *facts* (with permission to organise them in a particular schema) — they should follow FAIR-data norms, not the conventions used for authored prose.

The cd-rules §0.3 split addresses all three by mapping content type → licence according to *what kind of work the file is*, not where it sits in the directory tree. Adopting that pattern here.

## 2. The map

| Layer | Term (cd-rules §0.3) | Content in this repo | Licence | SPDX | Rationale |
|---|---|---|---|---|---|
| Core frameworks | **Coastline** | `CHARTER.md`, `CONVENTIONS.md`, `endorsement.md`, `README.md`, `LICENSES.md` (this file), `constraints/`, `logbook/_templates/`, `data/README.md`, `docs/index.md`, `docs/principles.md`, `docs/status.md`, `docs/LICENSE.md`, `docs/assets/SOURCE.md` | CC-BY-SA-4.0 | `CC-BY-SA-4.0` | Freely reusable, must stay open. Attribution required. ShareAlike ensures derivatives remain open. No NC friction with mixed-funding research groups. |
| Authored works | **Sail** | `docs/KD-2026-XXX-uv-280nm.md` (Kompass dossier), `docs/calculations.md` (interpretive analysis), `logbook/2026-04-30-kickoff.md`, `logbook/2026-04-30-architecture-neutral-infrastructure.md`, `logbook/2026-05-01-gate-g3-closure.md`, `logbook/2026-05-02-licence-split-adoption.md`, `data/literature/<key>/notes.md` | CC-BY-NC-SA-4.0 | `CC-BY-NC-SA-4.0` | Interpretive work protected from commercial repackaging without the epistemic commitments that give it meaning. |
| Design assets | **Handbook** | `docs/assets/tokens.css`, `docs/assets/site.css`, `docs/assets/emblem-32.svg`, `docs/assets/wordmark-full.svg`, `docs/_layouts/default.html` | MIT | `MIT` | Maximum integrability. The borrowed assets carry the upstream MIT licence per cd-rules §0.10 Model B; the layout file is a derived work offered under the same licence. |
| Code and tooling | **Infrastructure** | `src/`, `tests/`, `notebooks/`, `pyproject.toml`, `.gitignore`, `.github/`, build scripts | MIT | `MIT` | Standard open-source practice. Frictionless integration with GitHub workflows and Python tooling. |
| FAIR-published data | **Data** | `data/literature/<key>/extracted.yaml`, `data/baseline/**/metadata.yaml`, raw and processed measurement files under `data/baseline/` | CC-BY-4.0 | `CC-BY-4.0` | FAIR-data norm. Permissive, attribution-only; maximises downstream reuse and re-aggregation. The structuring schema is mine; the underlying scientific facts are in the public domain. |
| Fonts | **External** | IBM Plex Mono, Crimson Pro (loaded from Google Fonts; not redistributed in this repo) | SIL OFL 1.1 | `OFL-1.1` | Governed by their own licence; not relicensed by this project. |

Per-folder declaration files exist where useful: [`constraints/LICENSE.md`](constraints/LICENSE.md), [`logbook/LICENSE.md`](logbook/LICENSE.md), [`data/literature/LICENSE.md`](data/literature/LICENSE.md), [`docs/LICENSE.md`](docs/LICENSE.md). The matrix above governs in case of conflict.

## 3. SPDX text files

Verbatim licence texts and SPDX identifiers live under [`LICENSES/`](LICENSES/):

- [`LICENSES/MIT.txt`](LICENSES/MIT.txt) — full MIT text.
- [`LICENSES/CC-BY-SA-4.0.txt`](LICENSES/CC-BY-SA-4.0.txt) — SPDX header + canonical link + per-file applicability.
- [`LICENSES/CC-BY-NC-SA-4.0.txt`](LICENSES/CC-BY-NC-SA-4.0.txt) — same pattern.
- [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt) — same pattern.

For Creative Commons licences, the canonical authoritative text lives at `creativecommons.org/licenses/<id>/legalcode`. The SPDX identifier in each `LICENSES/` file binds; the canonical text is referenced by URL.

## 4. Per-file SPDX headers

For machine-readable licensing the repo follows the **REUSE** practice opportunistically (not strictly):

- New code files **should** carry an `SPDX-License-Identifier:` comment at the top (e.g. `# SPDX-License-Identifier: MIT` for Python).
- Borrowed assets in `docs/assets/` carry their licence in their existing header (`tokens.css`) or in [`docs/assets/SOURCE.md`](docs/assets/SOURCE.md).
- Existing files are **not** retrofitted in bulk; they pick up their licence from the table in §2 and from per-folder declarations.
- This is a soft norm, not a kill-gate.

## 5. Why not NC-SA everywhere?

A uniform CC-BY-NC-SA-4.0 licence would protect authored interpretive work but would block adoption of the Charter's framework by university research groups, NIST/PTB-style institutes, and anyone with mixed funding (which is most academic research). The §1 argument from cd-rules §0.3 applies directly: NC introduces legal ambiguity and produces a chilling effect even when use is benign.

Coastline content (Charter, constraint hierarchy, kill-gate protocol) is *infrastructure for governance*, not authored interpretive output. It should be reusable without the NC restriction.

## 6. Why not CC-BY everywhere?

A uniform CC-BY-4.0 licence (the v1.0-cut decision) under-protects authored interpretive work — it permits commercial repackaging of the Kompass dossier, the logbook deliberations, and the calculation narratives without preserving the epistemic commitments that produced them. The Sail layer is the right home for these.

## 7. Drift detection — borrowed assets

Site assets in [`docs/assets/`](docs/assets/) are borrowed from `threehouse-plus-ec/cd-rules` under cd-rules §0.10 Model B (distributed copy with checksum). SHA-256 hashes pinned at upstream commit `ee01c80` are recorded in [`docs/assets/SOURCE.md`](docs/assets/SOURCE.md). Drift checks live in that file.

## 8. Relicensing rule (cd-rules §0.3 inherited)

The Steward may relicense specific assets to a more permissive licence (e.g. CC-BY-SA → CC-BY, MIT → CC0). Relicensing to a more restrictive licence (e.g. Coastline → Sail, or CC-BY → CC-BY-NC-SA) requires a Council-3 deliberation logged in `/logbook/`. All relicensing is recorded in version history; rollback is via `git revert` of the relicensing commit, not by silent change.

## 9. Citation

For any reuse, please cite per [`CITATION.cff`](CITATION.cff). The CITATION.cff `license:` field declares MIT (the licence governing the primary code product); the document-layer split per this file applies to the markdown content. Citing tools that read CITATION.cff will pick up MIT — that is intended for the code-citation use case.

---

*Licence-map version: 1.0 — adopted 2026-05-02.*
