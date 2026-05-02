# `data/literature/` — licence

The `data/literature/<key>/` folders contain two file types under different licences.

## Structured extractions — Data (FAIR)

Files: `<key>/extracted.yaml`.

**Licence:** CC-BY-4.0 — see [`/LICENSES/CC-BY-4.0.txt`](../../LICENSES/CC-BY-4.0.txt).

These are structured extractions of *facts* from published primary literature. The schema is defined in [`/data/README.md`](../README.md). FAIR-data norm: permissive attribution-only licence to maximise downstream reuse and re-aggregation. The underlying scientific facts are in the public domain; the structuring schema and extraction effort are mine.

**Important:** the FACTS inside `extracted.yaml` are sourced from the cited primary literature (see each file's `citation:` field). The CC-BY-4.0 licence here governs the *organisation* of those facts in this schema; it does not extend to the underlying papers, which carry their own licences.

## Extraction notes — Sail

Files: `<key>/notes.md`.

**Licence:** CC-BY-NC-SA-4.0 — see [`/LICENSES/CC-BY-NC-SA-4.0.txt`](../../LICENSES/CC-BY-NC-SA-4.0.txt).

These are interpretive notes documenting extraction caveats, scope boundaries, and downstream-use guidance. They are authored work in the cd-rules §0.3 *Sail* sense — interpretive content whose meaning depends on the epistemic commitments of this project.

See [`/LICENSES.md`](../../LICENSES.md) for the full split-licence map. Suggested citation: [`/CITATION.cff`](../../CITATION.cff).
