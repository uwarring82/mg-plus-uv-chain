# CONVENTIONS

Operational conventions for `mg-plus-uv-chain`. Aligned with the AG Schätz norm and the `single-25Mg-plus` v1.0.0 pattern.

These conventions apply to all code and document contributions. Violations are reverted on review.

---

## 1. Units (the contract layer)

**SI throughout.** No mixed-unit code. Numerical values in `src/parameters.py` carry SI units in their variable names where ambiguity is possible (e.g. `power_W`, `wavelength_m`, `detuning_Hz`). Conversions to derived units (mW, nm, GHz) happen at the presentation boundary only — never inside computation.

The `src/parameters.py` module is the **single source of truth** for physical constants and project-wide parameters. Code that hard-codes a constant available in `parameters.py` is rejected.

---

## 2. Code style

- Python ≥ 3.11.
- Formatting: `black` with default line length.
- Import sorting: `isort`.
- Linting: `ruff` with project config.
- Type hints required for all public functions and module-level constants.
- Docstrings: NumPy style. Every public function documents its physical meaning and the units of its arguments and return value.

Tests live in `/tests/` and run under `pytest`. Coverage target: ≥ 90 % for `src/`.

---

## 3. Charter compliance for code

CHARTER §5.1 governs what may be committed when:

- **Pre-G1 architecture-family-specific code is forbidden in `/src/`.** It may live in `/notebooks/` with the header `pre-G1, exploratory, not promoted` and must remain unpromoted until G1 closes.
- **Architecture-neutral shared infrastructure** (units handling, generic ABCD utilities, generic Boyd–Kleinman functions without architecture presets, test fixtures, plotting utilities) may be committed pre-G1 to `/src/`.
- **Diagnostic surrogates** under the §5.1 exception live under `/src/diagnostic_surrogates_archive/` (or `/notebooks/archive/` after G1 closure) and must carry a `diagnostic-surrogate, not-candidate` header. Production simulation code must not import from this subtree — this is mechanically enforced by `tests/test_diagnostic_surrogate_imports.py`.

---

## 4. Commit conventions

Commit messages follow Conventional Commits with project-specific scopes:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `logbook`, `gate`.

**Scopes:** `charter`, `constraints`, `simulation`, `baseline`, `literature`, `surrogate`, `governance`, `infra`.

**Charter-relevant footer flags** (CHARTER §9 logbook trigger question):

- `Affects-Level-0: yes|no`
- `Affects-Level-1: yes|no`
- `Affects-Success-Criteria: yes|no`
- `Council-3-deliberation: <logbook entry ref>` (required if any of the above is `yes`)

Example:

```
feat(simulation): add architecture-neutral ABCD ring-cavity utility

Pure-geometry ABCD propagation for stable ring resonators with no
architecture presets. Tested against analytic confocal limit.

Affects-Level-0: no
Affects-Level-1: no
Affects-Success-Criteria: no
```

---

## 5. Logbook discipline

Every architectural decision is recorded in `/logbook/YYYY-MM-DD-<topic>.md`. The §9 trigger question must be answered in the entry header. Gate-closure entries follow the `/logbook/_templates/gate-closure.md` template. Stance attribution is mandatory where a Council-3 stance was invoked.

Routine experimental tactics within an agreed protocol do not require logbook entries — but any decision that changes a §1.5 Level 0 or Level 1 parameter does, regardless of how routine it appears (CHARTER §9 reclassification rule).

---

## 6. Versioning

The Charter is frozen at v1.0. Code releases follow semantic versioning:

- **MAJOR** for backward-incompatible parameter or API changes.
- **MINOR** for new features that do not break existing tests.
- **PATCH** for bug fixes and documentation.

Tagged releases trigger Zenodo deposit (concept-DOI registered against v1.0 of this repository).

---

## 7. Documents

Markdown is the default. LaTeX permitted for manuscripts. Diagrams committed as source (TikZ, mermaid, or SVG) plus rendered PNG/PDF. Binary-only diagrams are rejected.

Document license is CC-BY-4.0; code license is MIT. The Charter and Kompass-Dossiers carry an explicit endorsement marker per `endorsement.md`.

---

## 8. FAIR commitments

- All raw measurement data deposited under `/data/baseline/` with metadata schema declared in `/data/README.md`.
- Processed data separated from raw; provenance preserved.
- Computational results reproducible from committed code and committed input parameters; random seeds explicit.
- External dependencies pinned in `pyproject.toml`; lockfile committed.

---

## 9. Council-3 governance interface

CHARTER §9 governs deliberation. Issues with the `council-3` label trigger Council-3 review; deliberation outcomes are recorded in `/logbook/`. Vetoes (Guardian, Architect, Integrator) cite the violated Core Function per CHARTER §9.

---

End of CONVENTIONS v1.0.
