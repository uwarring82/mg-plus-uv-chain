# SHG licence and provenance notice

Author attribution: **AG Schaetz**. Publication authorized by **Ulrich
Warring**, 2026-09-14. The licence mapping was expressly adopted by the
Steward in the same session; see the
[decision record](../../../logbook/2026-09-14-shg-design-publication.md).

| Scope | SPDX licence |
|---|---|
| `raw/*.dwg`, `processed/**/*.dxf.gz`, `processed/**/*.dwg.json.gz`, generated drawing PDF/SVG/PNG files under `docs/assets/shg/SHG-*/` | CERN-OHL-S-2.0 |
| `catalogue.yaml`, inspection/pilot JSON records, `docs/_data/shg.yml`, `docs/assets/shg/catalogue.json` | CC-BY-4.0 |
| This notice, this folder's README, catalogue narrative and SHG logbook entries | CC-BY-SA-4.0 |
| `catalogue.schema.json`, `scripts/shg_designs.py`, requirements and SHG tests | MIT |

The hardware material is licensed under the
[CERN Open Hardware Licence Version 2 - Strongly Reciprocal](../../../LICENSES/CERN-OHL-S-2.0.txt).
You may redistribute and modify it under that licence. It is distributed
without warranties, as detailed in the licence text. Existing notices in
the original CAD files are retained; byte-identical DWGs use accompanying
sidecar notices instead of in-file edits.

**Source location:**
<https://github.com/uwarring82/mg-plus-uv-chain/tree/main/data/designs/shg>

**Modification notice, 2026-09-14:** archive ingestion changes filenames only;
original DWG contents are unchanged. ODA 27.1.0 exports DWG to DXF without
audit/repair. GNU LibreDWG 0.14 supplies a compressed JSON object graph.
`scripts/shg_designs.py` compresses the DXF, extracts metadata and reconstructs
sheet previews from cached blocks using restricted proxy-origin decoding
and source viewport associations. Conversion losses and missing engineering symbols
are disclosed in the inspection records. These derivatives are not certified
manufacturing drawings or a claim of Complete Source for an entire apparatus.

The author's attribution does not imply individual authorship has been
established from title blocks. Third-party component notices, where present,
retain their own scope. See the root [licence map](../../../LICENSES.md).
