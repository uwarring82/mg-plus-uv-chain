# Licence map — `mg-plus-uv-chain`

**Steward:** Ulrich Warring, AG Schätz, Albert-Ludwigs-Universität Freiburg. The licence categories below follow [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) §0.3 *Split licence architecture* and §0.10 *Distributed copy with checksum*.

**Record checked 2026-09-09.** Commit `e67bdaa` introduced the split declarations
on 2026-05-02. It did not include the adoption record cited by the earlier
version of this map (`logbook/2026-05-02-licence-split-adoption.md`), and that
file is absent from the current checkout. The declarations below are recorded
as found; the missing approval record remains an RC-10 question. The original
blanket CC-BY-4.0 notice is documented in [LICENSE-DOCS](LICENSE-DOCS).
This correction does not amend the frozen Charter or revoke prior grants.

**Contact.** Ulrich Warring · `https://orcid.org/0000-0001-8081-9718`

---

## 1. Licence categories

The split distinguishes reusable framework documents, authored analyses,
software/design assets and structured data. Keep the SPDX licence alongside
each category so reuse conditions are visible. The category names follow the
upstream licence/provenance records; they do not describe scientific certainty
or require readers to adopt this project's governance.

## 2. The map

**Coastline means CC-BY-SA-4.0; Sail means CC-BY-NC-SA-4.0; Handbook means
MIT.** These terms identify licence categories here, not levels of scientific
confidence. Model B means distributed copies pinned by checksum; it specifies
asset provenance, not a separate licence.

### Generated review outputs added 2026-09-10

The [review index and four generated notebook/HTML pairs](docs/review/index.md)
reproduce the source notebooks listed there, including their code and dated
analysis. Code remains covered by the software declaration below. Explicit
split assignment for the new mixed narrative/figure outputs and
`data/review/2026-09-10/` is recorded as **pending D6**, alongside the wider
RC-10 generated-asset review; a licence category is not inferred from their
page layout. No existing grant is revoked or new restriction imposed here.

### Public pages awaiting explicit split assignment

The student guide at `docs/tutorials/index.md` and the four mixed
tutorial notebook/HTML outputs also await explicit D6 split assignment.
The notebook code remains covered by the existing MIT software declaration.
Student access links do not change licence scope or revoke prior grants.

The following 12 pages are absent from the original map. `LICENSE-DOCS`
previously included them in its blanket CC-BY-4.0 declaration. Their current
scope review is recorded individually below; no new NonCommercial or
ShareAlike restriction is inferred from their subject or decorative labels.

| Page | Existing declaration | D6 split assignment |
|---|---|---|
| [docs/architectures/bbo-coating-brief.md](docs/architectures/bbo-coating-brief.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/bbo-coating-run.md](docs/architectures/bbo-coating-run.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/friedenauer-2006.md](docs/architectures/friedenauer-2006.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/ic-vecsel-alternative.md](docs/architectures/ic-vecsel-alternative.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/index.md](docs/architectures/index.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/next-gen.md](docs/architectures/next-gen.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/pulsed-raman-alternative.md](docs/architectures/pulsed-raman-alternative.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/architectures/requirements.md](docs/architectures/requirements.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/components/friedenauer-baseline.md](docs/components/friedenauer-baseline.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/components/home-built-doublers.md](docs/components/home-built-doublers.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/components/inventory.md](docs/components/inventory.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |
| [docs/components/seed-lasers.md](docs/components/seed-lasers.md) | CC-BY-4.0 in the original LICENSE-DOCS | Pending steward disposition |

### Existing split declarations

| Layer | Term (cd-rules §0.3) | Content in this repo | Licence | SPDX |
|---|---|---|---|---|
| Core frameworks | **Coastline** | `CHARTER.md`, `CONVENTIONS.md`, `endorsement.md`, `README.md`, `LICENSES.md` (this file), `constraints/`, `logbook/_templates/`, `data/README.md`, `docs/index.md`, `docs/principles.md`, `docs/status.md`, `docs/LICENSE.md`, `docs/assets/SOURCE.md` | CC-BY-SA-4.0 | `CC-BY-SA-4.0` |
| Authored works | **Sail** | `docs/KD-2026-XXX-uv-280nm.md` (Kompass dossier), `docs/calculations.md` (interpretive analysis), `logbook/2026-04-30-kickoff.md`, `logbook/2026-04-30-architecture-neutral-infrastructure.md`, `logbook/2026-05-01-gate-g3-closure.md`, `data/literature/<key>/notes.md` | CC-BY-NC-SA-4.0 | `CC-BY-NC-SA-4.0` |
| Design assets | **Handbook** | `docs/assets/tokens.css`, `docs/assets/site.css`, `docs/assets/emblem-32.svg`, `docs/assets/wordmark-full.svg`, `docs/_layouts/default.html` | MIT | `MIT` |
| Code and tooling | **Infrastructure** | `src/`, `tests/`, `notebooks/`, `pyproject.toml`, `.gitignore`, `.github/`, build scripts | MIT | `MIT` |
| FAIR-published data | **Data** | `data/literature/<key>/extracted.yaml`, `data/baseline/**/metadata.yaml`, raw and processed measurement files under `data/baseline/` | CC-BY-4.0 | `CC-BY-4.0` |
| Fonts | **External** | IBM Plex Mono, Crimson Pro (loaded from Google Fonts; not redistributed in this repo) | SIL OFL 1.1 | `OFL-1.1` |

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

## 5. Reuse conditions

[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) requires
attribution and ShareAlike; [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
adds NonCommercial. [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
requires attribution. The applicable legal texts govern, including their
exceptions and notices; these category names do not add licence conditions.

## 6. Prior declarations

The initial blanket CC-BY-4.0 notice remains part of the licence history.
The split map does not revoke rights already granted. Missing scope and
approval records are resolved through RC-10 with explicit file assignments,
not through assumptions about page design or subject matter.

## 7. Drift detection — borrowed assets

Site assets in [`docs/assets/`](docs/assets/) are borrowed from `threehouse-plus-ec/cd-rules` under cd-rules §0.10 Model B (distributed copy with checksum). SHA-256 hashes pinned at upstream commit `ee01c80` are recorded in [`docs/assets/SOURCE.md`](docs/assets/SOURCE.md). Drift checks live in that file.

## 8. Relicensing rule (cd-rules §0.3 inherited)

The Steward may relicense specific assets to a more permissive licence (e.g. CC-BY-SA → CC-BY, MIT → CC0). Relicensing to a more restrictive licence (e.g. Coastline → Sail, or CC-BY → CC-BY-NC-SA) requires a Council-3 deliberation logged in `/logbook/`. All relicensing is recorded in version history; rollback is via `git revert` of the relicensing commit, not by silent change.

## 9. Citation

For any reuse, please cite per [`CITATION.cff`](CITATION.cff). The CITATION.cff `license:` field declares MIT (the licence governing the primary code product); the document-layer split per this file applies to the markdown content. Citing tools that read CITATION.cff will pick up MIT — that is intended for the code-citation use case.

---

*Split declarations introduced 2026-05-02; scope and provenance clarification 2026-09-09. Missing adoption record and pending assignments remain under RC-10.*
