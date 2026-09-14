# AG Schaetz SHG design archive

**Author attribution:** AG Schaetz. **Publication authorized:** Ulrich Warring,
2026-09-14. [Decision and work record](../../../logbook/2026-09-14-shg-design-publication.md)
and [publication follow-ups](../../../logbook/2026-09-14-shg-publication-follow-ups.md).

The archive preserves 28 drawings supplied as `SHG.zip`. Originals retain
their exact bytes under stable IDs. The ZIP checksum, original filenames,
original filename bytes, local ZIP timestamps and individual checksums are
in [`catalogue.yaml`](catalogue.yaml). Finder timestamps and drawing creation
dates are separate evidence; ZIP timestamps have no recorded timezone.
`.DS_Store` and `__MACOSX` are excluded. IDs are an explicit registry, not
calculated from filenames or contents.

## Formats and limitations

- `raw/SHG-NNN.dwg`: unmodified AC1032 DWGs.
- `processed/SHG-NNN/SHG-NNN.dxf.gz`: direct ODA ACAD2018 ASCII DXF export,
  compressed without modifying its contents. Decompress with `gzip -dk` or
  Python `gzip.decompress`. Both compressed and uncompressed hashes are recorded.
- `processed/SHG-NNN/source-inspection.json`: source-side counts, original
  DWG date fields and warnings from GNU LibreDWG.
- `processed/SHG-NNN/SHG-NNN.dwg.json.gz`: the complete GNU LibreDWG reader
  object graph, including handles, coordinates, source classes and opaque
  proxy payloads. Decompress, then parse as JSON. This is a drawing export
  under CERN-OHL-S-2.0, distinct from the CC-BY-4.0 catalogue metadata.
- `processed/SHG-NNN/inspection.json`: DXF entity inventories, annotation
  text with source handles, references, reconstruction placements and losses.
- `docs/assets/shg/SHG-NNN/`: generated PDF/SVG/PNG previews for each
  qualifying sheet. These are **unverified reconstructed previews**.

The drawings use Inventor-specific proxy objects with cached linework and
annotation blocks. The direct exports preserve those blocks but do not
constitute editable native Inventor models. Ordinary layout rendering is
empty without exposing the cached blocks. The preview tool decodes the
observed unit-transform proxy variant, exposes blocks at their stored
coordinates, and applies source viewport associations, scale and clipping.
Unfamiliar transforms stop processing. This restricted decoder and the
resulting views remain unverified against an independent CAD engine.
The AIGDT engineering
symbol font is unavailable; some symbols appear as letters. **Use original
CAD and an independent CAD reference before machining or relying on dimensions.**

LibreDWG provides a second parse, not an independent rendering. Reader
success, matching counts and visual legibility do not establish fidelity.
Source-side dates are retained as raw day/millisecond pairs; ODA can reset
the DXF date fields, so those are labelled converter metadata. Native solids
and STEP availability are unresolved inside the proxy payloads. No STEP or
interactive 3D export is asserted.

The [block audit](block-audit.json) identifies the identical deficit in eight
drawings as omitted sheet-border (`D3`) and historical title-block (`FC`)
definitions. Both source names are `*I`; preserved handles distinguish them.
Their recorded insertion backlinks are absent from the parsed source graph.
The full deficit is accounted for, but opaque proxy references and visual
effect still need an independent CAD check. Reproduce with
`python -m scripts.shg_block_audit --check` in the full SHG environment.

## Native source and reference-rendering follow-up

No `.iam`, `.ipt`, `.idw` or `.ipj` files were found in the supplied archive,
repository or the Desktop filename search on 2026-09-14. Their location
remains an open request to the Steward; this is not a claim about other
laboratory storage. The preferred handover is an Inventor
[Pack and Go package](https://help.autodesk.com/cloudhelp/2025/ENU/Inventor-Help/files/GUID-730304AA-13BD-467B-9351-C7C1362876BD.htm)
with assemblies, parts, drawings, the project file and resolvable references.
Include referencing drawings and required libraries when collecting the
package, and record the authoring version and any missing references/fonts.

Receiving native files alone does not verify these previews. Render the
corresponding sheets with Inventor, or use an independent AutoCAD rendering
of the original DWGs, then compare dimensions, symbols, layouts and views
per file. Native assembly relationships and STEP exports require separate
checks. Hardware confirmation still requires bench evidence.

## Records and evidence

[`catalogue.schema.json`](catalogue.schema.json) validates the YAML record.
Drawing evidence tags are `D` (direct), `D*` (ambiguous/inferred), `OPEN`
(unresolved). These are separate from hardware association: `design_only`,
`provisionally_associated`, `confirmed`. The last requires bench evidence.
Guth2021 correspondence alone cannot confirm installed hardware; the
[targeted geometry extraction](../../literature/Guth2021/geometry.yaml)
records printed parameters and unresolved discrepancies.

The initial numerical extraction is deliberately limited. Inspection reports
preserve all accessible annotation text and handles, including exploded
dimension labels, but do not turn a label into a measured feature. Materials
and tolerances remain OPEN unless supported by a title block. Native CAD
units are retained; normalized numerical catalogue fields use SI.

## Reproduction

For the complete SHG test and rendering environment, run
`python -m pip install -e '.[test,shg]'` from the repository root. The `shg`
extra pins the same drawing dependencies as
[`scripts/requirements-shg.txt`](../../../scripts/requirements-shg.txt).
The standard `test` extra does not install ezdxf: the two viewport tests
skip without it. Run pytest with `-rs` to see these skip reasons. The
original **14 passed** result used the full drawing environment; the
standard environment instead reports **12 passed, 2 skipped** for that
original test file. There is currently no CI enforcing these checks.
ODA File Converter 27.1.0 and GNU LibreDWG 0.14 are external local tools;
neither tool nor the local Guth thesis PDF is redistributed here.

```sh
python scripts/shg_designs.py ingest /path/to/SHG.zip
python scripts/shg_designs.py convert --oda /path/to/ODAFileConverter --output /tmp/shg-dxf
python scripts/shg_designs.py inspect-source --reader /path/to/dwgread
python scripts/shg_designs.py process /tmp/shg-dxf
python scripts/shg_designs.py site
python scripts/shg_designs.py check
python -m pytest tests/test_shg_designs.py
```

`site` writes `docs/_data/shg.yml` and `docs/assets/shg/catalogue.json` from
canonical YAML. `check` validates the schema, original/export/preview hashes
and generated record freshness. Conversion is separate from website
generation, so checking or publishing the catalogue needs no proprietary
converter. Font availability can change rendering; record it when regenerating.

## Licence

DWGs, derived drawing exports and previews: **CERN-OHL-S-2.0**.
Catalogue metadata: **CC-BY-4.0**. This narrative: **CC-BY-SA-4.0**.
Scripts, schema and tests: **MIT**. See [LICENSE.md](LICENSE.md) for scope,
notices and the source location. Vendor components retain any applicable
third-party notices; this record makes no completeness claim for fabrication.
