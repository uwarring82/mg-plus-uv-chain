# SHG design archive: publication and implementation record

**Date:** 2026-09-14\
**Steward:** Ulrich Warring\
**Design author attribution:** AG Schaetz (as explicitly directed by the Steward)\
**Status:** Publication and licence mapping adopted; archive implemented with unverified conversion fidelity.\
**Starting revision:** `909f2919716a2c528536fef1dab331b0f0c83f58`

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No.
- Affects success criteria or gate state? No.

G1 and G2 remain OPEN. G3 remains CLOSED (2026-05-01). This is a record of
existing designs, not a build commitment for the next-generation source.
Conversion and catalogue tools belong in `scripts/`; no cavity simulation is
introduced into `src/`.

## Steward authorization and licence adoption

The Steward instructed: “Go, mention AG Schaetz as author, I authorize
publication, you suggest an open license that fits my philosophy, keep
logbook entries for this work”. Publication authorization covers the SHG
package discussed in this thread. It does not identify individual designers
or establish that a drawing matches installed hardware.

The Steward explicitly answered **“Adopt this licence mapping (recommended)”**
to the proposed mapping on 2026-09-14:

| Artifact | Adopted licence |
|---|---|
| Original DWGs, derived DXF and DWG JSON object graphs, drawing exports and previews | CERN-OHL-S-2.0 |
| Catalogue YAML metadata, generated JSON and `docs/_data/shg.yml` | CC-BY-4.0 |
| Catalogue narrative and this logbook entry | CC-BY-SA-4.0 |
| Conversion/generation scripts, schema and tests | MIT |

CERN-OHL-S-2.0 is a hardware-specific reciprocal licence, consistent with
the project's ShareAlike approach while permitting open use, modification
and distribution. It is a new scoped assignment, not a reinterpretation of
the site's MIT “design assets” row. Existing licence assignments elsewhere
are unaffected. Sources: [CERN overview](https://ohwr.org/licences/),
[licence](https://gitlab.com/ohwr/project/cernohl/-/wikis/uploads/819d71bea3458f71fba6cf4fb0f2de6b/cern_ohl_s_v2.txt).

## Agreed acceptance rules

1. Preserve all 28 DWGs byte for byte; record individual and ZIP SHA-256
   hashes. Omit `.DS_Store` and `__MACOSX`. Stable design IDs are independent
   of filenames; preserve original names and archive-name encoding evidence.
2. Extract Guth2021 §2.2.2 geometry before comparisons. Thesis/design matches
   can only support provisional association; confirmation requires bench
   evidence. Source dimensions, inferred geometry and hardware measurements
   remain distinct.
3. Compare ODA and LibreDWG conversion routes on the baseplate, BBO cavity,
   posts/optomechanics assembly, largest assembly and umlaut filename. All
   files still require individual validation despite sharing AC1032 headers.
4. A reference rendering must use an engine independent of the converter.
   Fidelity is unverified when that reference is unavailable. A successful
   parse or a source thumbnail is not a substitute for this check.
5. A qualifying layout has renderable paper-space content beyond viewport
   frames, or an enabled viewport displaying renderable model-space content
   under its clipping/layer settings. Record every layout's disposition.
   Provide a model-space view when substantive geometry has no such layout.
6. A part describes one manufactured component; an assembly depicts multiple
   identifiable components, including flattened geometry. Annotation blocks
   do not establish assembly status. Unresolved classification cannot waive
   the required part DXF export. Record conversion losses and unavailable
   source-side checks explicitly; do not claim fabrication readiness.
7. Preserve source units; normalize extracted numerical fields to SI. Use
   drawing evidence tags `D` (direct), `D*` (ambiguous/inferred), `OPEN`
   (unresolved), separate from hardware-association status. Materials and
   tolerances require source evidence.
8. Canonical YAML and raw/processed data live under `data/designs/shg/`.
   Declare this layout in `data/README.md`, map licences in `LICENSES.md`,
   and generate the new `docs/_data/shg.yml` and downloadable JSON from it.
   Add new schema, checksum, link and generated-data staleness tests.

STEP and interactive 3D are deferred until suitable source models and a
validated route exist. Large export sizes are measured before choosing
storage. Neither a software release nor a Zenodo deposit is part of this
task. The unqualified Zenodo sentence in `CONVENTIONS.md:94` remains a
separate RC-10 inconsistency; it is not corrected here.

## Implementation and validation

The [catalogue](../data/designs/shg/catalogue.yaml) records all 28 originals,
22 parts and 6 assemblies, direct compressed DXF exports, compressed source
reader JSON graphs and 41 qualifying paper layouts. Each has PDF/SVG/PNG
previews, individual hashes, source-side inspection and annotation records.
Raw DWGs are unchanged. The five-file conversion comparison and the
all-file source checks are detailed in the
[conversion work record](2026-09-14-shg-conversion-pilot.md).

The [web catalogue](../docs/components/shg-designs.html) is linked from the
site index, component baseline and photographic survey. It reads generated
site YAML from canonical metadata, offers downloadable JSON plus JSON Schema,
and supports stage/name filtering. Its content remains available without
JavaScript. `data/README.md` and `LICENSES.md` explicitly declare the new
layout and adopted artifact scopes; the new data directory and generated-data
staleness tests are additions to the repository.

The [Guth geometry extraction](../data/literature/Guth2021/geometry.yaml)
adds §2.2.2 values with printed and PDF page references. The local PDF is
not committed. No numerical drawing-to-thesis match has been established.
All 28 hardware associations therefore remain `design_only`.

Publication is permitted with the explicit `unverified` preview label.
An independent CAD rendering, complete native assembly relationships,
engineering-font fidelity, fabrication validation and bench association
remain open. They are acceptance conditions for stronger future claims,
not claims made by this publication. Gate state is unchanged.
