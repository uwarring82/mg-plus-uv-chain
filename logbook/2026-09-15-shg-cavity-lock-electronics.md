# SHG catalogue: planned cavity-lock electronics

**Date:** 2026-09-15\
**Steward:** Ulrich Warring\
**SHG design author attribution:** AG Schaetz\
**Licence:** CC-BY-SA-4.0\
**Starting revision:** `12dffc02c4ea57602e1b44cebf443146256635d0`\
**Status:** Published; local checks and live GitHub Pages verification passed.

## Charter §9 triggers

- Affects Level 0 parameters? No.
- Affects Level 1 parameters? No.
- Affects success criteria or gate state? No.

G1 and G2 remain OPEN. G3 remains CLOSED (2026-05-01). This entry records
presentation of the Steward's controller plan and corrections to literature
descriptions. It does not establish controller settings, performance,
firmware identity, installed-hardware association or a next-generation
architecture selection. All 28 drawing records remain `design_only` and
their previews remain `unverified`.

## Decisions

The Steward supplied an uncommitted catalogue subsection for visitors who
cannot access the laboratory's private controller records. The existing
authorization to publish SHG work and instruction to keep logbook entries
apply to this follow-up.

1. Keep the collapsible **Cavity-lock electronics (planned)** section after
   **How to read and reuse this archive**, at
   [`shg-designs.html#cavity-lock-electronics`](../docs/components/shg-designs.html#cavity-lock-electronics).
   The catalogue remains the public reference; no separate page is needed.
2. Omit the private repository's name and link. The public explanation is
   self-contained. No private repository content was accessed in this review
   or included in these changes.
3. Add a pointer from the photo survey's **HC servo electronics and bandwidth**
   gap. The stated intention is to use the PTB digital PID for LBO and BBO
   cavity locks. This intention comes from the Steward; technical descriptions
   and reported results come from the cited public literature.
4. Record the work here despite the absence of parameter changes, following
   the Steward's instruction to keep SHG work records. The existing catalogue
   narrative assignment and this entry are CC-BY-SA-4.0; the root licence map
   explicitly lists this new entry. Existing component-page and literature-note
   assignments are preserved. Public citations do not relicense third-party
   hardware or software.

## Source review and qualifications

The local publisher copy of
[Hannig et al. (2018)](https://doi.org/10.1063/1.5005515), §§IV–V,
pp. 013106-5–8, was checked for the controller and lock claims. The catalogue
also links the [2017 arXiv preprint](https://arxiv.org/abs/1709.07188) for
public access when the publisher blocks a request.

- §IV.C specifies FPGA PI operation with D set to zero, the modified
  STEMlab 125-14, two fast input and two output channels, interfaces,
  controller additions and eightfold output amplification. Its hardware
  subsection explicitly says that the board hardware is not open source.
  The earlier blanket description in
  [`Hannig2018/notes.md`](../data/literature/Hannig2018/notes.md) is corrected;
  the machine-readable extraction remains a scaffold.
- §IV.D.2 derives a few-MHz controller-bandwidth estimate from 155 ns group
  delay. The complete system also includes the 21.2 kHz piezo low-pass filter
  described in §IV.C.1. The estimate is not presented as measured cavity
  bandwidth.
- §V.B identifies a broad resonance near 17 kHz as the lock-bandwidth upper
  limit, probably due to the mirror, piezo and holder. The 130 h lock record
  (§V.A) and acceleration test up to about 1 g (§V.C) are separate results
  from the published 313 nm cavity.
- Friedenauer 2006 §3, p. 372, reports an approximately 18 kHz **loaded LBO
  piezo resonance**, not a measured closed-loop bandwidth. Similar resonance
  frequencies do not establish identical loop limits or any performance of
  the laboratory units. The linked baseline, photo survey and seed-laser
  pages were corrected where they equated that resonance with a measured
  loop bandwidth or assigned it to fielded doublers. The seed-linewidth
  budget and project parameters were not changed.

The code cited by Hannig ref. 67 is linked at
[`Julia-F/RedPitaya`, commit `7938c27fc030ca5d8d13b1731f559e33585458f1`](https://github.com/Julia-F/RedPitaya/tree/7938c27fc030ca5d8d13b1731f559e33585458f1),
dated 26 May 2016. Public `COPYING`, `apps-free/pid2/src/pid.c` and
`fpga/rtl/red_pitaya_pid2.v` were inspected. The explicit BSD directory list
uses different names from the modified controller paths; the two source
headers do not settle coverage. The page states this uncertainty without
using GitHub's automatic licence detection as a legal conclusion. No code
or firmware is imported, and no lab firmware match is claimed.

Fenske's 2015 thesis is cited through Hannig ref. 42; its text was not
reviewed. Knauer's public
[2019 thesis](https://pure.mpg.de/rest/items/item_3048433_1/component/file_3048434/content),
§§3.2 and 4.1 (pp. 20 and 23), and
[`PatKnauer/redpitaya`](https://github.com/PatKnauer/redpitaya) establish the
later PTB-PID/MPIK-PID terminology. This adaptation uses a
Pound–Drever–Hall error signal; it is not evidence of the laboratory's
Hänsch–Couillaud implementation.

## Validation and publication

- `.venv/bin/python -m pytest -q`: **275 passed, 3 skipped**. The existing
  block-audit regeneration and two viewport/proxy tests skip because ezdxf
  is absent from the standard environment. No new test is claimed to cover
  the page's scientific prose.
- The catalogue and default layout rendered with **Liquid 4.0.4** in strict
  parsing/filter mode using `docs/_config.yml` and `docs/_data/shg.yml`.
  This is a local template check, not a local Jekyll build.
- Parsed rendered HTML has balanced tags, unique IDs, 28 design cards, the
  collapsed electronics section in the intended position, and valid local
  fragment targets. Survey and seed-page pointers target the new anchor.
  The private repository identifier is absent from the rendered catalogue.
- Public source checks without authentication return HTTP 200 for the
  pinned code snapshot, its `COPYING`, the arXiv preprint, Knauer's PDF and
  the MPIK code repository. The DOI redirects to the correct publisher
  article, which returns HTTP 403 to the scripted request; the preprint is
  provided as an alternative access route.
- `git diff --check` passes. The new logbook entry is explicitly present in
  `LICENSES.md`. No drawing, export, preview, generated catalogue, simulation
  or parameter data changed.

The existing GitHub Pages source was confirmed as `main:/docs` (legacy
build). Documentation commit
`7a4db92e5cc3cfc24a481171163f55ee5d7e2af0` was pushed to `main`; GitHub Pages
reports that exact commit **built**, with no error, at
2026-09-15 16:07:51 UTC. The first HTTP check during the build still served
the preceding page; checks after completion passed.

The live
[catalogue section](https://uwarring82.github.io/mg-plus-uv-chain/components/shg-designs.html#cavity-lock-electronics)
matches the local rendered section byte for byte, retains all 28 cards and
contains no private repository identifier. Public HTTP checks also confirm
the corrected
[photo survey](https://uwarring82.github.io/mg-plus-uv-chain/components/home-built-doublers.html),
[Friedenauer baseline](https://uwarring82.github.io/mg-plus-uv-chain/components/friedenauer-baseline.html#b2-piezo-and-mount)
and [seed-laser page](https://uwarring82.github.io/mg-plus-uv-chain/components/seed-lasers.html).
The survey/seed pointers resolve to the new section after Jekyll's relative-link
rewriting, and the baseline anchor exists. These are rendered-content and
HTTP checks; no interactive browser test or laboratory validation is claimed.
