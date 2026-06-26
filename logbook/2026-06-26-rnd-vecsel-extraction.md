# 2026-06-26 — rnd_vecsel channel extraction + hardware-status page

**§9 trigger question — does this entry alter, relax, or tighten any §1.5 Level 0 or
Level 1 parameter?** **No.**

- Affects-Level-0: no
- Affects-Level-1: no
- Affects-Success-Criteria: no
- Council-3-deliberation: not required (routine documentation; no architectural change)

## What

Extracted a sanitised in-house record from the internal `#rnd_vecsel` Mattermost channel
(2021–2026), mirrored read-only via the private `connect-to-mattermost` archive, and:

1. Added **`data/lab notes/2026-06-rnd-vecsel-channel-record.md`** — sanitised extraction
   (fleet status, 2026 operating points, open operational items), evidence class
   `[in-house, channel-derived, unverified]`, pending Steward cross-check.
2. Added **`docs/hardware-status.md`** — a public, sanitised hardware-status page (what
   has been built/done; current open items) distinct from the governance `status.md`.
3. Minor citations in `docs/tutorials/vecsel-systems.md`: filled the §4 / §5 **[open]**
   item on Heidi's (1141 nm) doubling route with the now-confirmed **extra-cavity LBO
   ring → ≈570 nm** (~110 mW, 2026), and listed the new lab note under "Lab notes".

## Steward-confirmed fact (2026-06-26)

**V#2 "Heidi" = the 1141 nm photoionisation unit, doubling 1141 → ≈570 nm** (first SHG
stage toward 285 nm), extra-cavity LBO ring. This resolves an apparent fleet-ID ambiguity
in an earlier draft of the extraction (which mis-read the LBO output as 559 nm from a
1118 unit). No conflict with the tutorial's #2 assignment.

## Sanitisation

Personal names → roles; vendor prices/quotes/PO numbers, e-mail/phone, internal
IPs/credentials, server paths, and chat permalinks omitted. Attachments remain
local-only in the private archive. The public pages assert only physics/results at the
existing tutorial's evidence level.

## Status

DRAFT — not promoted to Coastline; figures marked `[in-house, unverified]` pending
cross-check against the primary lab logbook.
