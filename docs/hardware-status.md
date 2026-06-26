---
layout: default
title: Hardware status — VECSEL seed fleet
description: What has been built and what is open on the in-house VECSEL seed lasers (1118 nm cooling/detection/Raman and 1141 nm photoionisation), distilled from the lab record. Operational snapshot, sanitised; distinct from the governance Status page.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local operational snapshot — AG Schätz stewardship. This page summarises the build/operations state of the in-house VECSEL seed fleet at a sanitised level (roles, not individuals; no procurement or facility detail). It is not a Phase 4 input and does not alter the reference triple. For repository governance state (kill-gates, phases, dossier) see the <a href="status.html">Status</a> page.</p>

<p class="eyebrow">Snapshot · 2026-06-26 · DRAFT</p>

# VECSEL seed fleet — what's done, what's open.

Distilled from the internal lab record (2021–2026) into a sanitised summary, so the group
can see at a glance what has been built and what is still open. Figures are
**[in-house, unverified]** pending cross-check against the primary logbook; the provenance
artefact is [`data/lab notes/2026-06-rnd-vecsel-channel-record.md`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/lab%20notes/2026-06-rnd-vecsel-channel-record.md).

For *how* the lasers work, see the [VECSEL systems tutorial](tutorials/vecsel-systems.html).

---

## The fleet *Sail*

<p class="classification classification--sail">Sail · operational state; the testable physics is in the tutorial and the cited lab notes.</p>

| Unit | Wavelength / role | State (2026-06) |
|---|---|---|
| **"Heidi" (V#2)** | **1141 nm** photoionisation → extra-cavity **LBO → ≈570 nm** (toward 285 nm) | Lasing; doubling stage commissioned 2026 (≈570 nm output measured) |
| **1118 nm units (incl. V#4)** | cooling / detection / repump / Raman seed → 280 nm | In operation; V#4 in use by a downstream experiment |
| **V#5** (1118 nm, student build) | cooling/detection-class seed | Operating ~2.6 W; Lyot-filter re-fit in progress (see open items) |
| **"NeXt"** (1118 nm, bachelor build) | next-generation low-noise platform | Re-lased; integrated onto its cold plate |

---

## What has been done *Coastline + Sail*

<p class="classification classification--coastline">Coastline · the linewidth lineage is the published in-house record (tutorial §3.3).</p>

- **Linewidth driven down > 10× across four builds** — 1.6 MHz (2021) → ~300–400 kHz (2023) → **101(8) kHz locked (2025)**, by closing thermal, mechanical, and cooling-water noise sources (tutorial [§3.3](tutorials/vecsel-systems.html)).
- **A facility-plumbing finding** — a chiller on/off cycle drove ~200 MHz of frequency oscillation; replacing the cooling loop removed it (factor-5 short-term gain).
- **Multiple operating units** built and characterised at 1118 nm (cooling/detection/Raman) plus the 1141 nm photoionisation unit.
- **1141 nm → ≈570 nm doubling stage** stood up in 2026 (extra-cavity LBO ring; ~110 mW measured in one run) — the first SHG step toward 285 nm.
- **1118 nm operating point** recently re-confirmed on the V#5 build (~2.6 W near 267.744 THz, 2026).

---

## Open items *Sail*

<p class="classification classification--sail">Sail · current work fronts; none of these alters Charter Level 0/1 constraints or the kill-gate state (see <a href="status.html">Status</a>).</p>

**Measurement gaps (also tracked in the tutorial §3.5 / §5):**
- **Seed frequency-noise PSD** above the ~18 kHz doubling-cavity lock bandwidth — unmeasured.
- **Downstream UV relative-intensity noise** at the experiment — unmeasured.
- A true **sub-100 kHz intrinsic linewidth** — not yet independently proven (needs delayed self-heterodyne or a beat note).
- **1141 nm "Heidi"** full characterisation — linewidth, output power, and the ≈570 nm → 285 nm second stage still to be recorded.

**Build / commissioning fronts** (engineering status; none affects the physics above):
- **1141 → 570 nm doubling lock** under stabilisation (commissioning in progress).
- **V#5 (student build):** intracavity birefringent (Lyot) filter re-fit in progress; single-mode hold time temporarily reduced in the interim.
- **New gain-chip mounting:** a freshly-mounted chip shows a slow (~10 min) power/frequency settling, under characterisation.
- **"NeXt":** water-cooling vibration test and control-board revision pending.

---

## See also

- [Status](status.html) — repository governance state (kill-gates, phases, dossier, tests).
- [VECSEL systems tutorial](tutorials/vecsel-systems.html) — how the seed lasers work and what limits their linewidth.
- [`data/lab notes/`](https://github.com/uwarring82/mg-plus-uv-chain/tree/main/data/lab%20notes) — the sanitised in-house extractions every figure here is drawn from.

---

[← Home](index.html) · [Status →](status.html) · [VECSEL tutorial →](tutorials/vecsel-systems.html)
