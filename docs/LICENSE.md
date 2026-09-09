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

The 12 pages under `architectures/` and `components/` are not assigned a
split category in the original map. They were included in LICENSE-DOCS's
blanket **CC-BY-4.0** declaration: [attribution is required](https://creativecommons.org/licenses/by/4.0/).
A page-by-page D6 assignment remains pending. This review does not add
NonCommercial or ShareAlike restrictions to those pages.

The [repository licence map](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/LICENSES.md)
lists every page and its disposition. Other unmapped pages and generated
assets remain in RC-10's scope audit; their licence must not be inferred from
visual styling. Third-party sources retain their own terms.

## Declaration history

Commit `e67bdaa` introduced the split declarations on 2026-05-02. Its cited
adoption log is absent from the current checkout; RC-10 tracks that missing
record. The former blanket CC-BY-4.0 declaration and any rights already
granted remain part of the record. The frozen Charter is unchanged.

Citation metadata in [CITATION.cff](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CITATION.cff)
describes the software, licensed MIT; it is not a licence declaration for all
site prose.
