---
title: Status
description: Kill-gate state, dossier population, phase progress
---

# Status

Snapshot at HEAD (commit `3fbe1bf`, 2026-05-02). The canonical state lives in the [git history](https://github.com/uwarring82/mg-plus-uv-chain/commits/main) and the [`logbook/`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/logbook).

[← Home](index.html)

---

## Kill-gates

| Gate | Blocks | Status | Closure evidence / dependency |
|---|---|---|---|
| **G1** | Architecture-family-specific simulation in `/src/architecture/` | OPEN | Awaits Phase 2 discriminant scans on the existing chain (cavity scan vs. crystal temperature, polarisation, intra-cavity intensity, vendor/batch). |
| **G2** | Phase 4 / 5 acceptance of degradation-rate inputs to scoring | OPEN | Awaits Phase 2 §8.2 protocol producing reproducible exposure-history dependence. |
| **G3** | Phase 4 architecture comparison | **CLOSED** 2026-05-01 | [`logbook/2026-05-01-gate-g3-closure.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-01-gate-g3-closure.md) — Integrator-acknowledged. `src.parameters.assert_g3_closed()` is silent at module load. |

The diagnostic-surrogate import-path test (the §5.1 mechanical enforcement that backs G1) continues to pass; no production code currently imports from the empty surrogate archive.

---

## Phases

| Phase | Deliverable | State |
|---|---|---|
| 0 | Charter v1.0 + repo scaffold | **Complete** (frozen 2026-04-30) |
| 0.5 | Reference triple `{Δ_ref, Ω_R,ref, Γ_sc,ref}` and Conservative / Nominal / Aggressive bounded-scenario set | **Complete** — locked at G3 closure (2026-05-01) |
| 1 | Literature dossier `KD-2026-XXX-uv-280nm.md` with crystal/coating evidence table | **In progress** — 5 of 15 entries past SCAFFOLD; structured Friedenauer 2006 extraction landed |
| 2 | Baseline measurement protocol + first-pass data on the existing chain | Not started |
| 3 | Boyd–Kleinman cavity model, damage/degradation model, parameter sweeps; ≥ 90 % test coverage | Architecture-neutral layer in place; family-specific code G1-blocked |
| 4 | Falsifiable architecture comparison against the six fixed scoring axes | Not started; G3-unblocked, G2-dependent inputs gated |
| 5 | Procurement, assembly, validation against §2 targets | Not started |
| 6 | Manuscript + Zenodo deposit + tagged release | Not started |

---

## Phase 1 literature dossier

[`docs/KD-2026-XXX-uv-280nm.md`](KD-2026-XXX-uv-280nm.html)

Population protocol: SCAFFOLD → POPULATING → DRAFT → REVIEWED. Cells in the crystal/coating evidence table without citations are not admitted as Phase 4 inputs.

| Entry | Title | Outcome | Status |
|---|---|---|---|
| KD-UV280-001 | Quadrupling architecture (Friedenauer baseline family) | Operationally bounded | POPULATING |
| KD-UV280-002 | Sum-frequency mixing architectures | TBD | SCAFFOLD |
| KD-UV280-003 | Hybrid architectures (dual-source / OPA-based) | TBD | SCAFFOLD |
| KD-UV280-004 | Direct deep-UV sources (AlGaN, deep-UV VECSEL) | TBD | SCAFFOLD |
| KD-UV280-005 | BBO at 280 nm — phase-matching, walk-off, damage threshold | Operationally bounded | POPULATING |
| KD-UV280-006 | CLBO at 280 nm | TBD | SCAFFOLD |
| KD-UV280-007 | LBO at relevant SHG/SFG stages | TBD | SCAFFOLD |
| KD-UV280-008 | UV mirror coatings (HR, OC, AR) | TBD | SCAFFOLD |
| KD-UV280-009 | Hygroscopic and environmental constraints (BBO, CLBO) | TBD | SCAFFOLD |
| KD-UV280-010 | 14-GHz unlockable resonance domain | **Underdetermined** (literature-level) | POPULATING |
| KD-UV280-011 | UV-induced BBO degradation, gas-environment dependence | TBD | SCAFFOLD |
| KD-UV280-012 | UV mirror coating degradation under CW exposure | TBD | SCAFFOLD |
| KD-UV280-013 | Friedenauer 2006 baseline parameter extraction | **Resolved** | DRAFT |
| KD-UV280-014 | Phase-locked dual-source phase-noise literature | TBD | SCAFFOLD |
| KD-UV280-015 | Pump source options (Yb-fibre vs. VECSEL near 1118 nm) | Operationally bounded | POPULATING |

**5 / 15** past SCAFFOLD. All five are backed by the structured [Friedenauer 2006 extraction](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) plus the dossier's first cited literature constants. Further entries require new source readings.

---

## Test posture

| Test file | Tests | Notes |
|---|---|---|
| `tests/test_parameters.py` | 24 | G3 lock helpers, defence-in-depth for revocation |
| `tests/test_boyd_kleinman.py` | 22 | Includes regression for the bounded-`h_m_optimum` fix |
| `tests/test_abcd.py` | 31 | Cavity stability and eigenmode |
| `tests/test_diagnostic_surrogate_imports.py` | 1 | §5.1 mechanical enforcement (G1) |
| **Total** | **78** | All passing |

Coverage at last full run: 91.23 % (target ≥ 90 % per Charter §5 Phase 3 row). The σ-optimised Boyd–Kleinman tests are the slow path (full BK suite ≈ 25 s; fast suite, excluding BK, runs in ≈ 2 s).

---

## What is unblocked, what is gated

### Unblocked at HEAD

- **Phase 1 literature dossier population.** Literature collection was never gated.
- **Phase 2 baseline measurement.** Bench work on the existing chain can begin; the §8.2 protocol must produce reproducible exposure-history dependence to close G2.
- **Architecture-neutral simulation utilities.** New generic ABCD or BK functions can land in `/src/` provided they are genuinely architecture-agnostic.
- **Phase 4 architecture comparison entry conditions other than G2.** G3 closure unblocks the entry; comparison scoring can begin once G2 is resolved.

### Still gated

- **Architecture-family-specific simulation in `/src/architecture/`.** G1-blocked. Pre-G1 exploratory notebooks are permitted in `/notebooks/` with the `pre-G1, exploratory, not promoted` header.
- **Phase 4 scoring of axis-3 / axis-4 inputs that depend on a measured degradation rate.** G2-blocked.
- **Public push.** Pending Steward action: insert real ORCID into [`CITATION.cff`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/CITATION.cff) line 17 (`BLOCKING` marker in place).

---

## Recent commits

```
3fbe1bf  fix(simulation): bound h_m_optimum search; correct BK-recalc notebook narrative
92f6f43  docs(simulation): add Friedenauer 2006 BK-recalculation notebook (pre-G1)
145814e  chore(governance): tighten G3-vs-G2 wording; fix publication metadata
23f2e59  docs(governance): update README — G3 closed; Phase 1 dossier 5/15 populated
fd3cc47  gate(governance): close G3 — Integrator-acknowledged; Phase 4 unblocked
3b855a6  docs(literature): populate KD-UV280-005 (BBO) and -010 (14-GHz domain) from Friedenauer
a663965  docs(literature): populate KD-UV280-001 and -015 from Friedenauer extraction
8b2ec74  docs(literature): populate KD-UV280-013 from Friedenauer 2006 (Resolved/DRAFT)
9f3f464  docs(literature): scaffold Phase 1 KD-2026-XXX-uv-280nm.md dossier
5eb63d6  gate(governance): file Phase 0.5 G3 candidate values; Phase 4 still blocked
8c43c00  feat(infra): add architecture-neutral simulation utilities, build, tests
0423b2f  Initial commit: Charter v1.0 frozen, Phase 0 complete
```

[Full history on GitHub](https://github.com/uwarring82/mg-plus-uv-chain/commits/main).

---

[← Home](index.html) · [← Principles](principles.html) · [← Calculations](calculations.html)
