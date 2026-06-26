# rnd_vecsel channel record (2021–2026) — in-house extraction

**Evidence class.** [in-house], channel-derived. Sanitised automated extraction from the
AG Schätz internal `#rnd_vecsel` Mattermost channel (≈2265 posts, 2021-12 → 2026-06),
mirrored read-only via the private `connect-to-mattermost` archive.

**Status.** DRAFT — pending Steward cross-check against the primary lab logbook. Values
below are operational notes from the channel, not yet promoted to Coastline. Treat
single-number figures as **[in-house, unverified]** until cross-checked.

**Sanitisation.** Personal names → roles; vendor prices, quotes, PO numbers, e-mail
addresses, phone numbers, internal IPs/credentials, server paths, and chat permalinks
are **omitted**. Image/PDF attachments remain local-only in the private archive.

---

## 1. Scope and relation to the existing record

This channel is the running build/operations log for the in-house VECSEL fleet. It
**extends** the [2021 VECSEL project summary](2021-07-vecsel-project-summary.md) and the
[2020-11 "Heidi" diary](2020-11-vecsel-2-heidi.md) forward through 2026. Component
choices (Vexlum GaInAs/GaAs gain chips, LightMachinery YAG étalon, Newlight Lyot/BRF,
PI ring piezo, Ostech 808 nm pumps, Alphacool PC-water cooling) are **consistent with**
the part numbers already documented there; this note records only what is *new or
updated* by the channel.

> **Fleet mapping (Steward-confirmed 2026-06-26).** **V#2 "Heidi" = the 1141 nm
> photoionisation unit**, doubling **1141 → ≈570 nm** (first SHG stage toward 285 nm) —
> consistent with the tutorial's #2 "Heidi" assignment. The other channel units
> (**V#4, V#5, "NeXt"**, and V#3) are **1118 nm** cooling/detection builds. (An earlier
> draft of this note mis-read Heidi's LBO output as 559 nm from a 1118 unit; corrected.)

---

## 2. Fleet status (channel-derived, 2025–2026)

| Unit (channel ID) | Role (channel) | Latest channel status |
|---|---|---|
| **V#2 "Heidi"** | **1141 nm** photoionisation + **LBO doubling → ≈570 nm** | Lasing; LBO stage commissioned 2026; ≈570 nm output measured (§3) |
| **V#4** | 1118 nm cooling/detection | Moved to the "Paula" experiment (2024); upgraded |
| **V#5** | 1118 nm (student project) | Operating ~2.6 W; BRF re-fit in progress (§4) |
| **NeXt** | 1118 nm (bachelor project) | Re-lased; mounted on cold plate (last activity 2026-06-26) |

---

## 3. Measurements & results (new vs. the 2021 summary) — [in-house, unverified]

- **Free-running linewidth, ~2022:** "122(1) kHz at 10 ms"; "< 200 kHz for 30 ms to 8 s"
  (consistent with the [Span23] short-term improvement narrative). Later "≈ 1 MHz on a
  0.26 s timescale" quoted for a NIR unit.
- **V#5 (1118 nm), 2026:** "2.6 W" output at **267.74384 THz** (≈ 1119.7 nm).
- **V#2 "Heidi" (1141 nm) + LBO, 2026:** SHG to **≈570 nm** measured at **110 mW** in one
  run (with the 19″ HV amplifier substituted by the lock-box amplifier — see §4). This is
  an **extra-cavity LBO ring** (separate lock/piezo/PD electronics), i.e. the same
  external-doubling topology as the 1118 nm path — *not* the intra-cavity scheme of the
  Burd 2016 analogue. UV figures elsewhere in the channel remain low (single-digit to
  ~19 mW), consistent with the tutorial's **[open]** UV-power status.

*(These refine the tutorial's §4 "[open]" entries for current 2026 operating points but
are not yet promoted; cross-check against the primary logbook before tutorial promotion.)*

## 4. Open / unresolved (commissioning, 2025–2026)

*Engineering-status level — specific failure causes and facility detail are kept to the private logbook.*

- **V#5 BRF** re-fit in progress (2026-05); interim single-mode hold ~5–10 min before mode-hop.
- **New gain-chip mounting** shows power/frequency settling after ~10 min; under characterisation (2026-06).
- **V#2 LBO lock** under stabilisation; fibre-outcoupler mechanics being finished.
- **NeXt** water-cooling vibration test pending; control-board revision in progress.

## 5. Provenance & method

Source: private `connect-to-mattermost` archive, channel `oneworld/rnd_vecsel`,
`posts.jsonl` → sanitised summary. The primary (authoritative) record remains the lab
logbook and the units' own documentation. This extraction exists so the public tutorial
and hardware-status page can cite a stable, sanitised in-repo artefact rather than the
internal chat.
