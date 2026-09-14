---
layout: default
title: Site licences
description: Document and asset licences, with explicit scope and outstanding assignments.
---

# Site licences

The repository uses different licences for documents, code and assets.
The categories retain the upstream names so attribution remains traceable:

| Category | Pages or assets explicitly mapped | Licence and reuse conditions |
|---|---|---|
| **Coastline — CC-BY-SA-4.0** | `index.md`, `principles.md`, `status.md`, this page, `assets/SOURCE.md` | [Attribution and ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/) |
| **Sail — CC-BY-NC-SA-4.0** | `KD-2026-XXX-uv-280nm.md`, `calculations.md` | [Attribution, NonCommercial and ShareAlike](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Handbook — MIT** | `_layouts/default.html`, `assets/tokens.css`, `assets/site.css`, `assets/emblem-32.svg`, `assets/wordmark-full.svg` | [MIT notice](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSES/MIT.txt) |
| **External — OFL-1.1** | IBM Plex Mono and Crimson Pro, loaded from Google Fonts | Font licences remain with their sources |

**Model B (distributed copies pinned by checksum)** describes how borrowed
assets are stored and checked. It is not another licence.
[Asset provenance](assets/SOURCE.html) identifies the upstream commit.

## Architecture and component pages

The 12 pre-existing pages under `architectures/` and `components/` listed
in the repository map are not assigned a
split category in the original map. They were included in LICENSE-DOCS's
blanket **CC-BY-4.0** declaration: [attribution is required](https://creativecommons.org/licenses/by/4.0/).
A page-by-page D6 assignment remains pending. This review does not add
NonCommercial or ShareAlike restrictions to those pages.

The [repository licence map](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSES.md)
lists every page and its disposition. Other unmapped pages and generated
assets remain in RC-10's scope audit; their licence must not be inferred from
visual styling. Third-party sources retain their own terms.

## SHG design archive — adopted 2026-09-14

Ulrich Warring authorized publication and explicitly adopted the following
scope for the [SHG design catalogue](components/shg-designs.html), attributed
to **AG Schaetz**:

| Material | SPDX licence |
|---|---|
| Original DWGs, compressed DXF and DWG JSON exports in `data/designs/shg/`, and PDF/SVG/PNG drawings under `assets/shg/SHG-*/` | [CERN-OHL-S-2.0](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSES/CERN-OHL-S-2.0.txt) |
| Catalogue and inspection metadata, `_data/shg.yml` and `assets/shg/catalogue.json` | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |
| `components/shg-designs.html`, archive README/notice and SHG logbook entries | [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| Conversion tools, tests, JSON Schema and `assets/shg/catalogue.css` | [MIT](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSES/MIT.txt) |

These assignments are settled and are separate from the outstanding RC-10
assignments above. The
[archive notice](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/designs/shg/LICENSE.md)
provides the source location and modification notices; the
[decision record](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-09-14-shg-design-publication.md)
records adoption. Conversion fidelity remains unverified; open licensing
does not establish manufacturing accuracy or installed-hardware association.

## Declaration history

Commit `e67bdaa` introduced the split declarations on 2026-05-02. Its cited
adoption log is absent from the current checkout; RC-10 tracks that missing
record. The former blanket CC-BY-4.0 declaration and any rights already
granted remain part of the record. The frozen Charter is unchanged.

Citation metadata in [CITATION.cff](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CITATION.cff)
describes the software, licensed MIT; it is not a licence declaration for all
site prose.
