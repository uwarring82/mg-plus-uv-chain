---
layout: default
title: Tutorials
description: Visitor-facing notebooks introducing focused-Gaussian SHG, enhancement-cavity buildup, optimal input-coupler reflectivity, and two-stage cascade composition. Architecture-neutral, pre-G1 admissible.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local pedagogical material — AG Schätz stewardship. The tutorials below use the architecture-neutral primitives in <code>/src/</code>; they do not endorse any specific build, vendor, or architecture.</p>

<p class="eyebrow">Tutorials</p>

# Tutorials

Two tutorial tracks. The **seed-laser systems** track explains the VECSEL
sources themselves — how they lase single-frequency and what limits their
linewidth. The **SHG enhancement-cavity numerics** track picks the seed up at
its output and follows it through the LBO + BBO doubling chain to the deep UV.

## Seed-laser systems

| Tutorial | What it explains |
|---|---|
| [VECSEL systems — 1118 nm and 1141 nm](vecsel-systems.html) | The two in-house VECSEL seeds (~1120 nm → 280 nm cooling/detection/Raman; ~1140 nm → 285 nm photoionisation): **gain-mirror properties**, the **intracavity Lyot + étalon filtering hierarchy**, and the **parameter sensitivities that set the achievable linewidth**. |

This is a narrative tutorial over the published in-house thesis lineage
([Kiefer 2020 → Guth 2021 → Spanke 2023 → Spanke 2025](../references.html)) and
the NIST + Tampere design literature; it pairs with the
[seed-lasers components page](../components/seed-lasers.html), which records the
source-class steward direction.

## SHG enhancement-cavity numerics

Four worked notebooks taking a visitor from focused-Gaussian SHG efficiency
through to a self-consistently impedance-matched two-stage cascade. They use
only the architecture-neutral primitives in
[`src/boyd_kleinman.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/boyd_kleinman.py),
[`src/shg_single_pass.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/shg_single_pass.py),
[`src/enhancement_cavity.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/enhancement_cavity.py),
and
[`src/shg_cascade.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/src/shg_cascade.py)
— so the pedagogy never depends on Friedenauer-specific or other architecture
presets.

Each tutorial is paired with a YAML parameter file (`NN-params.yaml`) so you
can re-run it with your own numbers; the rendered HTML below uses the bundled
defaults.

### The four notebooks

| # | Tutorial | Question it answers |
|---|---|---|
| 01 | [From Boyd–Kleinman to γ_SHG](01-shg-single-pass.html) | Given a crystal, a wavelength, and a focused beam — how much harmonic comes out in a single pass? |
| 02 | [Passive enhancement cavity](02-enhancement-cavity-buildup.html) | When does a ring cavity *build up* the circulating power, and what fixes the impedance match? |
| 03 | [Optimal input coupler](03-optimal-input-coupler.html) | **The headline question.** What input-coupler reflectivity should I specify when ordering coatings, given my pump power and round-trip loss budget? |
| 04 | [Two-stage cascade](04-cascade-shg.html) | How does the LBO → BBO chain compose, and why does the joint optimum factorise into two independent stage problems? |

The tutorials are designed to be read in order. Tutorial 03 is the load-bearing
one for the procurement question that motivated the [components inventory](../components/inventory.html);
Tutorial 04 closes with an honest end-to-end Friedenauer 2006 cross-check
([Phase E diagnostic notebook](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py)) where the BBO stage agrees to 1.5 % and the LBO
exposes an `L_passive` definitional gap in the source paper — the kind of
result the tutorials are meant to make you trust *and* probe.

### Source and reproducibility

- Notebook source (jupytext `.py`):
  [`notebooks/tutorials/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/tutorials/)
- Theory references (Boyd–Kleinman 1968, Polzik–Kimble 1991, …):
  [`notebooks/tutorials/REFERENCES.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/tutorials/REFERENCES.md)
- Render pipeline:
  [`scripts/render_tutorials.py`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/scripts/render_tutorials.py)
  (jupytext → executed `.ipynb` → nbconvert HTML; install `pip install -e
  .[notebooks]`, then `make tutorials` from the repo root).
- Workplan:
  [`logbook/2026-05-07-numerics-expansion-workplan.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/2026-05-07-numerics-expansion-workplan.md).

The rendered `.html` and executed `.ipynb` files in this directory are
committed alongside the source so GitHub Pages can serve them statically; the
`.py` files in [`notebooks/tutorials/`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/tutorials/)
remain the version-controlled truth.
