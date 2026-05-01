# Data — `data/`

**CHARTER §7 FAIR commitment:** raw and processed data separated; metadata schema declared here.

This directory holds all measurement and reference data for `mg-plus-uv-chain`. Empty at v1.0 cut; populated during Phase 1 (literature parameter extraction) and Phase 2 (baseline measurements).

---

## Layout

```
data/
├── README.md                ← this file (metadata schema)
├── baseline/                ← Phase 2 measurements on the existing chain
│   └── YYYY-MM-DD_<topic>/
│       ├── raw/             ← unmodified instrument output
│       ├── processed/       ← analysed; provenance preserved
│       └── metadata.yaml    ← per-dataset metadata (schema below)
└── literature/              ← parameters extracted from cited works
    └── <citation-key>/
        ├── extracted.yaml   ← parameter table
        └── notes.md         ← extraction commentary
```

Per CHARTER §7: raw and processed data are kept in sibling directories, never co-mingled. Provenance from raw → processed must be reconstructible from committed code.

---

## Metadata schema (`metadata.yaml`)

Every measurement dataset under `baseline/` carries a `metadata.yaml` file at its root with the following fields:

```yaml
# Required
dataset_id: "YYYY-MM-DD_<topic>"           # matches directory name
date: "YYYY-MM-DD"                         # ISO 8601
operator: "<name>"                         # who took the data
charter_phase: 2                           # which CHARTER phase this serves
charter_section_refs:                      # which CHARTER sections it informs
  - "§8.1"                                 # e.g. 14-GHz domain discriminant
  - "§8.2"                                 # e.g. degradation tuple

# Apparatus state — reproducibility anchor
apparatus:
  source_chain: "<short description>"      # e.g. "1118 nm fibre amp + 2× SHG, BBO at UV stage"
  source_version: "<git tag or label>"     # if a software-controlled chain
  enclosure_atmosphere: "N2 | O2 | dry-air | ambient"
  ambient_temperature_C: <float>           # if relevant
  exposure_history: "<free-form>"          # CHARTER §8.2: cumulative UV exposure context

# Instruments — every channel that produced a value
instruments:
  - role: "<e.g. UV power meter>"
    make_model: "<vendor / model>"
    serial: "<sn or label>"
    last_calibration: "YYYY-MM-DD"

# Measurement parameters — what was scanned
scan:
  type: "<e.g. cavity-length, polarisation, intra-cavity-intensity>"
  variable: "<symbol>"
  units: "<SI>"
  range: [<low>, <high>]
  step: <float>
  averaging: <int>                          # samples per point

# Data files — pointer with units
files:
  - path: "raw/<file>"
    columns:
      - name: "<symbol>"
        units: "<SI>"
        description: "<one line>"

# Discriminant hypothesis (if applicable; CHARTER §8.1)
discriminant:
  hypothesis_under_test: "<text>"
  expected_signature: "<text>"
  outcome_classification: "Resolved | Operationally bounded | Underdetermined | TBD"

# Provenance — raw → processed
processing:
  pipeline: "<git path to processing script>"
  pipeline_commit: "<sha>"
  random_seed: <int>                        # required if any stochastic step
  inputs: ["raw/<file>", ...]
  outputs: ["processed/<file>", ...]

# Notes
notes: |
  Free-form commentary. Anything that would be needed to interpret this
  dataset six months later, or by an outside reader, goes here.
```

All units are SI per CONVENTIONS §1. Derived-unit presentation (mW, nm, GHz) lives in plotting code, not in the metadata file.

---

## Literature data (`literature/<citation-key>/`)

Per-paper parameter extractions live under `literature/<citation-key>/extracted.yaml`:

```yaml
citation_key: "Friedenauer2006"             # matches CITATION.cff and dossier
doi: "10.1007/s00340-006-2274-2"
extracted_by: "<name>"
extracted_on: "YYYY-MM-DD"
charter_section_refs: ["§2", "§4", "§8.1"]

parameters:
  - symbol: "P_UV"
    value: 0.275
    units: "W"
    location_in_paper: "Abstract; Fig. 3"
    notes: "Reported source-side; loss budget to ion not stated."
  - ...
```

Vendor / batch sensitivity, where the paper reports it, must be captured (CHARTER §5 Phase 1 evidence-table requirement).

---

## Charter compliance

- **Pre-G1**: data may be deposited freely; data ingest does not constitute architecture-family-specific simulation under CHARTER §5.1.
- **Discriminant scans (CHARTER §8.1)**: deposited under `baseline/`; `outcome_classification` tracks per-scan progress toward G1 closure.
- **Degradation protocol (CHARTER §8.2)**: time-resolved {power, M², phase noise, polarisation} mandatory. Single-number degradation rates without protocol attribution will be rejected per the Charter.
- **§9 trigger question**: depositing data does not by itself change a Level 0/1 parameter. If interpreting the data prompts a constraint change, that's an architectural decision and lives in `/logbook/`.

---

End of `data/README.md`.
