---
layout: default
title: Status
description: Kill-gate state, dossier population, phase progress. Snapshot at HEAD.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page is a snapshot of repository state, not a claim about the underlying physics or the architecture choice.</p>

<p class="eyebrow">Snapshot · 2026-05-22</p>

# What is closed, what is open, what is gated.

Snapshot at 2026-05-22. The canonical state lives in the [git history](https://github.com/uwarring82/mg-plus-uv-chain/commits/main) and the [`logbook/`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/logbook).

> **Hardware vs. governance status.** This page tracks repository *governance* state (kill-gates, phases, dossier, tests). For the *hardware/operational* snapshot of the in-house VECSEL seed fleet — what is built and what is open — see the [Hardware status](hardware-status.html) page.

---

## Kill-gates *Coastline*

<p class="classification classification--coastline">Coastline · §5.1 · gate state mechanically witnessed by tests/parameters.G3_INTEGRATOR_ACKNOWLEDGED</p>

| Gate | Blocks | Status | Closure evidence / dependency |
|---|---|---|---|
| **G1** | Architecture-family-specific simulation in `/src/architecture/` | OPEN | Awaits Phase 2 discriminant scans on the existing chain (cavity scan vs. crystal temperature, polarisation, intra-cavity intensity, vendor / batch). |
| **G2** | Phase 4 / 5 acceptance of degradation-rate inputs to scoring | OPEN | Awaits Phase 2 §8.2 protocol producing reproducible exposure-history dependence. |
| **G3** | Phase 4 architecture comparison | **CLOSED** 2026-05-01 | [`logbook/2026-05-01-gate-g3-closure.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-01-gate-g3-closure.md) — Integrator-acknowledged. `src.parameters.assert_g3_closed()` is silent at module load. |

The diagnostic-surrogate import-path test (the §5.1 mechanical enforcement that backs G1) continues to pass; no production code currently imports from the empty surrogate archive.

---

## Phases *Coastline*

<p class="classification classification--coastline">Coastline · §5 · phase ordering and entry conditions fixed</p>

| Phase | Deliverable | State |
|---|---|---|
| 0 | Charter v1.0 + repo scaffold | Complete (frozen 2026-04-30) |
| 0.5 | Reference triple `{Δ_ref, Ω_R,ref, Γ_sc,ref}` and Conservative / Nominal / Aggressive bounded-scenario set | Complete — locked at G3 closure (2026-05-01) |
| 1 | Literature dossier `KD-2026-XXX-uv-280nm.md` with crystal/coating evidence table | Populating — 22 extracted reference folders; KD-UV280 evidence table at v0.2 (see below) |
| 2 | Baseline measurement protocol + first-pass data on the existing chain | Not started |
| 3 | Boyd–Kleinman cavity model, damage / degradation model, parameter sweeps; ≥ 90 % test coverage | Architecture-neutral numerics landed — single-pass SHG, enhancement-cavity solver, SHG cascade, Boyd–Kleinman, ABCD; Friedenauer-2006 cascade cross-check agrees to 1.5 %. Family-specific code still G1-blocked |
| 4 | Falsifiable architecture comparison against the six fixed scoring axes | Exploration under way — a slate-of-three (next-gen / IC-VECSEL / pulsed-Raman) over a shared requirements artefact; formal scoring still G2-gated |
| 5 | Procurement, assembly, validation against §2 targets | Not started — BBO coating-run mirror spec frozen 2026-05-20 as procurement-prep |
| 6 | Manuscript + Zenodo deposit + tagged release | Not started |

---

## Phase 1 literature dossier *Coastline + Sail*

<p class="classification classification--coastline">Coastline · the population protocol (SCAFFOLD → POPULATING → DRAFT → REVIEWED) is fixed and inspectable.</p>
<p class="classification classification--sail">Sail · the choice of which entry to populate next, and the depth of literature search, is contextual.</p>

[`docs/KD-2026-XXX-uv-280nm.md`](KD-2026-XXX-uv-280nm.html). Cells in the crystal/coating evidence table without citations are not admitted as Phase 4 inputs.

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

**5 / 15** entries past SCAFFOLD in this summary table; the dossier's detailed evidence sections (BBO §5, coatings §8.6, environment §8.2/§8.4, pump §3) are populated ahead of this summary. **22 literature reference folders** are now extracted under [`data/literature/`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/data/literature) — from the [Friedenauer 2006 extraction](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/extracted.yaml) through the BBO / CLBO / coating LIDT and UV-degradation source set — feeding those sections. The [dossier itself](KD-2026-XXX-uv-280nm.html) is the authority for per-entry status.

---

## Test posture *Coastline*

<p class="classification classification--coastline">Coastline · ≥ 90 % coverage required by §5 Phase 3 row; mechanically enforced via pytest + pytest-cov</p>

| Test file | Tests | Notes |
|---|---|---|
| `tests/test_parameters.py` | 24 | G3 lock helpers, defence-in-depth for revocation |
| `tests/test_abcd.py` | 31 | Cavity stability and eigenmode |
| `tests/test_enhancement_cavity.py` | 28 | Steady-state buildup + optimal-input-coupler solver |
| `tests/test_shg_cascade.py` | 23 | Two-stage SHG cascade composition |
| `tests/test_boyd_kleinman.py` | 22 | Includes regression for the bounded-`h_m_optimum` fix |
| `tests/test_shg_single_pass.py` | 12 | Single-pass SHG coefficient |
| `tests/test_anti_seeding_src_imports.py` | 1 | §5.1 mechanical enforcement — no architecture preset in `/src/` |
| `tests/test_diagnostic_surrogate_imports.py` | 1 | §5.1 mechanical enforcement (G1) |
| **Total** | **142** | All passing (`142 passed`, full run 2026-05-22) |

Charter §5 Phase 3 requires ≥ 90 % coverage. The full suite runs in ≈ 28 s; the σ-optimised Boyd–Kleinman tests are the slow path (the fast suite, excluding BK, runs in a few seconds).

---

## What is unblocked, what is gated *Sail*

<p class="classification classification--sail">Sail · contextual reading of which work is next; the gate states above are the testable Coastline</p>

### Unblocked at HEAD

- **Phase 1 literature dossier population.** Literature collection was never gated.
- **Phase 2 baseline measurement.** Bench work on the existing chain can begin; the §8.2 protocol must produce reproducible exposure-history dependence to close G2.
- **Architecture-neutral simulation utilities.** New generic ABCD or BK functions can land in `/src/` provided they are genuinely architecture-agnostic.
- **Phase 4 architecture-comparison entry conditions other than G2.** G3 closure unblocks the entry; comparison scoring can begin once G2 is resolved.

### Still gated

- **Architecture-family-specific simulation in `/src/architecture/`.** G1-blocked. Pre-G1 exploratory notebooks are permitted in `/notebooks/` with the `pre-G1, exploratory, not promoted` header.
- **Phase 4 scoring of axis-3 / axis-4 inputs that depend on a measured degradation rate.** G2-blocked.

---

## Recent commits

Top of `main` at this snapshot (most recent first):

```
5e278d4  site: add coating-review outreach banner to the welcome page
fbed344  docs(architectures): add shareable BBO coating brief (sanitized)
c790265  docs(architectures): expand BBO page with BC-G lock-mirror finding (§8.1)
b25f6a7  docs(logbook): BC-G addendum — M2′ piezo-mirror substrate (Ø6.35×2.0 mm)
5bb43dd  docs(architectures): public-facing explainer for the BBO coating-run WP
9630329  docs(logbook): close BBO coating-run WP — BC-D/E/F + spec sheets + closure
c4bfb15  docs(logbook): open BBO coating-run WP — BC-A/B/C closed in one day
5405269  docs(literature): file task-E third scout pass — three new scaffolds
61d7773  docs(components): archive home-built doublers + fold-angle survey
f241443  docs(architectures): IC-VECSEL + pulsed-Raman alternatives (slate-of-three)
752885c  feat(site): introduce Architectures section + Next-Gen 500 mW workplan
d5855cb  feat(notebooks): Phase E — Friedenauer 2006 cascade cross-check
8296fff  feat(src): Phase A — single-pass SHG coefficient + anti-seeding test
fd3cc47  gate(governance): close G3 — Integrator-acknowledged; Phase 4 unblocked
0423b2f  Initial commit: Charter v1.0 frozen, Phase 0 complete
```

[Full history on GitHub](https://github.com/uwarring82/mg-plus-uv-chain/commits/main).

---

[← Home](index.html) · [← Principles](principles.html) · [← Calculations](calculations.html)
