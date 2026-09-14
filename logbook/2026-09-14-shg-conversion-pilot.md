# SHG conversion pilot and publication validation

**Date:** 2026-09-14\
**Steward:** Ulrich Warring\
**Design author attribution:** AG Schaetz\
**Licence:** CC-BY-SA-4.0\
**Related decision:** [Publication and licence adoption](2026-09-14-shg-design-publication.md)

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No.
- Affects success criteria or gate state? No.

G1 and G2 remain OPEN; G3 remains CLOSED (2026-05-01).

## Source preservation and classification

The supplied `SHG.zip` contains 28 AC1032 DWGs. The archive's SHA-256,
original filenames, exact filename bytes and ZIP-local timestamps are in
the [catalogue](../data/designs/shg/catalogue.yaml). One filename contains
decomposed UTF-8 umlaut bytes without the ZIP UTF-8 flag; these are recovered
without discarding the original bytes. Stable ASCII filenames avoid relying
on filesystem normalization. All originals are preserved byte for byte.
Finder resource files are omitted. Each raw drawing has a licence sidecar.

Manual review identifies 22 parts and 6 assemblies. A part describes one
manufactured component; multiple components qualify as an assembly even
when flattened. Title blocks and annotation INSERTs do not count as assembly
dependencies. These Inventor proxy drawings do not provide a verified native
dependency graph, so classification records are tagged `D*`. All drawings
receive DXF exports; classification cannot exempt a part from that requirement.

## Five-file route comparison

The pilot comprises SHG-001 (baseplate), SHG-002 (BBO housing), SHG-005
(umlaut filename), SHG-014 (posts and optomechanics) and SHG-015 (largest
assembly). The complete tool output, counts and sizes are retained in
[`pilot.json`](../data/designs/shg/pilot.json).

Both ODA File Converter 27.1.0 and GNU LibreDWG 0.14 produce DXFs that ezdxf
1.4.4 can parse. ODA retains the Inventor proxy-to-cached-block references;
LibreDWG's DXF writer omits the proxy entities. This supports choosing ODA
for the direct DXF export, with audit/repair disabled. It does not validate
ODA's fidelity. SHG-005 has 78 source-reader MTEXT entities but 48 in the
ODA export; the 30-entity discrepancy is retained as unresolved loss evidence.
LibreDWG also reports unsupported classes and metadata/handle warnings.
An exit code of zero is not a clean fidelity result.

The all-file comparison finds the same deficit in SHG-003, SHG-004, SHG-005,
SHG-010, SHG-012, SHG-016, SHG-022 and SHG-023: 2 BLOCK, 2 ENDBLK, 14 LINE,
17 LWPOLYLINE and 30 MTEXT entities fewer in the DXF. No assumption that
these are harmless unused blocks is made. Each affected web record exposes
the discrepancy and links both source and export inspection data.

The largest direct DXF is 71,336,142 bytes. Lossless gzip keeps exports compact
and deterministic without requiring Git LFS. The compressed files have both
compressed and uncompressed checksums. Each source DWG is separately read
with LibreDWG, preserving the complete reader JSON object graph and compact
inspection report. The graph is useful machine-readable drawing data, but
unknown proxy payloads remain opaque. It is not a native Inventor source model
or a claim of STEP availability.

The largest committed artifact is the SHG-015 source JSON gzip at 25,085,883
bytes; its DXF gzip is 23,352,308 bytes and original DWG 22,997,689 bytes.
These fit ordinary Git storage. The full collection contains 46,711,251 bytes
of original DWGs, 47,107,342 bytes of compressed DXFs and 50,815,811 bytes of
compressed source JSON, plus metadata and previews.

## Rendering and known limitations

Ordinary layout rendering was empty because the substantive views live in
Inventor cached blocks. The renderer exposes only blocks referenced by proxy
hard pointers. A restricted decoder reads three bit-coded insertion coordinates
and accepts only this collection's observed trailing unit-transform signature.
Unknown or truncated variants fail closed. Model blocks retain their specific
viewport association; ezdxf applies viewport scale and clipping. Paper output
uses the source sheet dimensions and rotation. Each PDF and SVG is rendered
separately; sharing mutable backend recordings caused text loss during an
early attempt and was removed.

All 41 paper layouts contain substantive paper annotations or cached views.
The empty-layout test excludes a default viewport with no visible content.
Additional tests cover model content outside the viewport, disabled viewports
and hidden layers. No layout in this set requires a model-space-only fallback.

All previews prominently say **UNVERIFIED PREVIEW** and name AG Schaetz and
the hardware licence. The AIGDT symbol font is unavailable: diameter and
other engineering symbols may render as letters. Some long source title-block
strings overflow; the SHG-028 third sheet has an oversized view clipped at
the sheet edge. These issues are disclosed, not silently repaired by guessing
dimensions or geometry. An independent authoring-engine rendering is still
required. Neither the second parser nor visual review of these derivatives
provides that reference.

Source units are millimetres. ODA resets some DXF timestamps, so source DWG
date fields are preserved separately in raw Julian-day/millisecond form.
Inspection JSON exposes annotation text and handles. Three baseplate labels
(615, 440 and 20 mm) are transcribed into SI, and the SHG-022 title-block
aluminium/anodizing note is recorded directly. Exploded dimension text is not
treated as an independently measured geometric feature. Other material and
tolerance specifications remain OPEN.

## Thesis extraction and hardware association

Guth2021 §2.2.2 was extracted with `pdftotext -layout`; all six relevant PDF
pages were rendered and visually inspected. The separate geometry record
captures mirror spacings, cavity/crystal lengths, curvatures and unresolved
angles/positions. The LBO curvature entry **50 cm** in Table 3 is retained
as printed with an unresolved possible unit error. The BBO 24.6 mm distance
does not resolve crystal-face versus centre reference. Figures attributed
to reference [44] are not independent installed-hardware evidence.

No numerical CAD-to-thesis match or bench verification was completed. All
associations remain `design_only`. A future thesis match may only promote
to `provisionally_associated`; `confirmed` requires cited bench evidence.

## Validation and publication

Local validation completed:

- `python -m pytest tests/test_shg_designs.py -q`: **14 passed**. This includes
  schema and all artifact checksums, generated YAML/JSON/schema freshness,
  source preservation, filename recovery, confirmation requiring bench
  evidence, deterministic compression and restricted proxy/viewport tests.
- Black formatting and Ruff checks pass on the new script and tests.
  `git diff --check` passes. No simulation code or numerical baseline is changed.
- All 41 final PDF/PNG sheet previews were visually reviewed. All 41 PDFs
  and SVGs parse and carry the visible unverified/licence notice. The known
  symbol, title-block and SHG-028 clipping issues above remain open.
- Second rendering of SHG-001 and all three SHG-015 sheets produces
  byte-identical PDF/SVG/PNG files.
- Liquid 4.0.4 parses and renders the template with 28 design cards; 210
  unique catalogue artifact links resolve to local source/export/preview
  files. Generated site data comes from the same canonical YAML record.

The local Jekyll gem installation timed out at the package index; template
checking uses Liquid 4.0.4, and the existing GitHub Pages builder remains
the deployment build. No release tag or Zenodo deposit is created.

**Deployment verified:** commit `bd44419301b5e82e8bc47cadabc3e96e25af84dc`
was pushed to `main`; GitHub Pages reported `built`, with no error, at
13:44:05 UTC on 2026-09-14. The
[live page](https://uwarring82.github.io/mg-plus-uv-chain/components/shg-designs.html)
returns all 28 design cards and nine specific conversion notes. Public
downloads of SHG-001 DWG, DXF gzip, DWG JSON gzip, PDF, SVG and PNG, plus
the public catalogue JSON and schema, match local SHA-256 records.

The live filter script passes ID search, empty-result, stage and reset checks
in a Node DOM fixture. No connected browser was available for a live visual
or mobile interaction check; this fixture is not represented as that check.
The sheet artwork itself was reviewed locally as described above. The
temporary ODA disk image was unmounted after conversion. The original ZIP,
local thesis PDF, existing Python environment and frozen gate records are
unchanged.
