# Task-E literature filing — third scout pass and scaffold authorship correction

**Steward:** Ulrich Warring
**Date:** 2026-05-13
**Status:** OBSERVATIONAL RECORD (Phase 1-equivalent literature population). Three new SCAFFOLD entries created in `data/literature/`; one previously-misattributed SCAFFOLD corrected; the [task-E logbook](2026-05-04-bbo-cw-uv-lidt-task.md) extended with a third scout pass that cross-walks the 2026-05-13 downloads batch to folder status. No architecture-family-specific code; no change to any binding parameter.

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — the §1.5 Level 0 row (³P₁/₂–³P₃/₂ detuning, two-photon Rabi rate, allowed scattering rate) and the G3-closure reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` are not touched by literature population.
- **Affects Level 1 parameter?** no — three new SCAFFOLD entries plus one authorship correction do not, in themselves, tighten or relax any Level 1 row. Downstream DRAFT promotion of `Hannig2018` (130 h CW operation at 313 nm) and `Burkley2021` (oxide vs fluoride coatings under high-power deep-UV CW) *may* tighten KD-UV280-005 / -008 / -012 Section C constraints when those extractions are run, but no such tightening is asserted here.
- **Affects success criterion?** no.

This entry therefore does not require Council-3 deliberation. It is a **literature-tracking-chain maintenance entry**: filing newly-arrived PDFs, fixing a 2026-05-06 scaffold-era authorship error, and weaving both into the task-E candidate list.

## Anti-seeding boundary

This entry is admissible under Phase 1 (`docs/principles.md` "Anti-seeding clause" — Phase 1 dossier population is unblocked; architecture-family-specific simulation in `/src/` is forbidden until G1 closes). The work introduces no new architecture preset, no new simulation code, and no new parameter constant. All four affected `data/literature/<key>/` folders carry `extraction_status: SCAFFOLD`; no numerical values from the article bodies have been promoted to `extracted.yaml` parameters in this pass.

---

## 1 · What was filed

Three publisher PDFs newly arrived in `downloads/literature/task-e/` on 2026-05-13 were inspected (first-page + abstract + §1-2 read) and given SCAFFOLD entries under `data/literature/`. None of the three were previously on the candidate list in either of the prior scout passes — they surfaced through the steward's institutional access route rather than through the assistant's web-scout queries.

| Citation key | Reference | Wavelength | Headline result |
|---|---|---|---|
| **`Hannig2018`** | S. Hannig, J. Mielke, J. A. Fenske, M. Misera, N. Beev, C. Ospelkaus, P. O. Schmidt, *Rev. Sci. Instrum.* **89**, 013106 (2018), DOI `10.1063/1.5005515` | 313 nm | Brewster-cut BBO bow-tie cavity; **130 h uninterrupted CW operation, no decay in output power**; vibration-robust (<10 % output variation at 1 g, 30 min at 3 g_rms); STEMlab 125-14 (Red Pitaya) digital PI lock |
| **`Shaw2021`** | J. C. Shaw, S. Hannig, D. J. McCarron, *Opt. Express* **29**, 37140-37155 (2021), DOI `10.1364/OE.441741` | 261.5 nm | LBO + CLBO cascaded monolithic bow-tie cavities (1046 nm ECDL + IPG fibre amp source); **2.75 W peak / 2 W steady-state CW at 261.5 nm over 13 h**; "largely unexplored high-intensity regime in CLBO for continuous-wave DUV" (abstract verbatim) |
| **`Kraus2022`** | B. Kraus, F. Dawel, S. Hannig, J. Kramer, C. Nauk, P. O. Schmidt, *Opt. Express* **30**, 44992-45003 (2022), DOI `10.1364/OE.471450` | 267.4 nm | Twofold *single-pass* SHG: 1069.6 nm fibre laser → 10 mm PPLN waveguide → 534.8 nm → 50 mm DKDP non-critical Type-I → 267.4 nm at >50 µW; fractional frequency instability **<5 × 10⁻¹⁷ at 1 s** (beat-note); 1 × 10⁻¹⁸ at 1 s electronics-limited |

All three are open-access at the publisher (Hannig 2018 under Creative Commons CC-BY 4.0 via AIP; Shaw 2021 and Kraus 2022 under the OSA / Optica Open Access Publishing Agreement). The publisher PDFs are therefore **admissible** for commit under the project's mixed-licence policy (cf. `LICENSES.md`), but the three SCAFFOLD entries defer that decision to the steward and currently keep the PDFs only in the gitignored `downloads/` tree.

## 2 · What was corrected

One previously-filed SCAFFOLD entry was corrected for authorship attribution.

**`data/literature/Burkley2021/`** was created on 2026-05-06 as a scaffold for arXiv:`2105.14977` *before* the PDF was in hand. The scaffold's first-author guess "von Milczewski" was committed into the YAML and notes files (`citation_key: "vonMilczewski2021"`, `citation: "J. S. B. von Milczewski et al. …"`) despite the folder itself being named `Burkley2021/` from creation. Direct read of the arXiv PDF on 2026-05-13 confirms the correct author list:

> Z. (Zakary) Burkley, L. de Sousa Borges, B. Ohayon, A. Golovozin, J. Zhang, P. Crivelli
> "Stable High Power deep-UV Enhancement Cavity in Ultra High Vacuum with Fluoride Coatings"
> arXiv:2105.14977v1 (31 May 2021)
> Affiliations: ETH Zürich (Burkley, de Sousa Borges, Ohayon, Zhang, Crivelli); Lebedev Physical Institute, Moscow (Golovozin)

There is no author named "von Milczewski" on the paper. The folder name `Burkley2021/` is correct; the `citation_key`, `citation`, `title`, and `source_document` strings inside `extracted.yaml` and the heading inside `notes.md` were rewritten in this pass. A `cross_check_notes` entry `scout_pass_authorship_correction` is now logged in [`data/literature/Burkley2021/extracted.yaml`](../data/literature/Burkley2021/extracted.yaml), parallel to the matching note already in [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml) (which records a different but procedurally identical scaffold-era misattribution).

**Filename retained.** The download filename `vonMilczewski2021_arxiv_open.pdf` is retained in the gitignored `downloads/literature/task-e/` tree as a historical artefact of the 2026-05-06 scout-pass commit. Renaming it would break the chain-of-provenance trail back to that commit (which is in `git log`) without any compensating benefit, since the downloads tree is not part of the published repository.

## 3 · How the entries weave into the task-E chain

A third scout pass section was appended to [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](2026-05-04-bbo-cw-uv-lidt-task.md) immediately before the "Acceptance criteria" section. It contains:

1. **A 16-row table** cross-walking every download in `downloads/literature/task-e/` to its current folder status (DRAFT for the already-extracted ones, SCAFFOLD-with-corrected-attribution for Burkley2021, and SCAFFOLD-newly-created for Hannig2018 / Shaw2021 / Kraus2022).
2. **The Burkley2021 authorship correction**, with the rationale reproduced from §2 above and an explicit pointer to the parallel `scout_pass_authorship_correction` in Hemmerling2011.
3. **A three-row triage table** for the three new candidates, mapping each to one or more of the Task-E sub-questions (Q1 intrinsic threshold, Q2 operational lifetime, Q3 mechanism, Q4 institutional context) and branches (BBO-cavity, CLBO comparison, alternative-topology).
4. **A cross-paper observation** that the four PTB-Schmidt-group-related papers in the dossier (`Hemmerling2011`, `Hannig2018`, `Shaw2021`, `Kraus2022`) now span four distinct UV-stage architectures (Brewster-cut BBO bow-tie cavity at 280 nm; Brewster-cut BBO monolithic bow-tie at 313 nm; LBO + CLBO cascaded monolithic bow-tie at 261.5 nm; PPLN waveguide + DKDP single-pass at 267.4 nm), with Hannig (PTB / Agile Optic GmbH) as the bridging co-author. This widens the scope of the institutional-`[I]`-tier extraction window when the steward chooses to pursue task-E acceptance criterion #3 (the MPQ Garching / AG Schätz Freiburg / PTB Braunschweig institutional record).
5. **An updated priority list** that augments rather than replaces the second scout pass's ranking, inserting Hannig2018 in parallel with Kondo1998 / Kubota1998 / Turcicova2022 at the top tier, then Shaw2021, Burkley2021, Hemmerling2011, and Kraus2022 in descending order.

## 4 · What is *not* in this entry

- **No full extraction of any of the three new papers.** All three SCAFFOLDs enumerate their highest-priority numerical extraction targets but leave them open. Promoting `Hannig2018` to DRAFT (in particular the 130 h figure and the operating conditions under which it was observed) is the highest-payoff next pass.
- **No update to KD-UV280-005, -006, -008, -009, or -012 Section C.** The dossier consumes the extractions, not the scaffolds. Updates to Section C wait for DRAFT promotion of the relevant entries.
- **No assertion that the Burkley2021 authorship correction implies a systematic problem with the 2026-05-06 scout pass.** It is the second confirmed scaffold-era author misattribution (after Hemmerling2011's `scout_pass_authorship_correction`, which speculated U. Warring as a co-author when he is not). Two confirmed cases is enough to record the pattern; a third instance, if found, should trigger a re-audit of all 2026-05-06 SCAFFOLD-only entries against their PDFs. For now, the rule "verify authorship against the PDF before promoting SCAFFOLD → DRAFT" is sufficient and is already part of the de-facto extraction workflow.

## 5 · Charter compliance

**Anti-seeding boundary.** All four affected folders are at `extraction_status: SCAFFOLD`; no numerical value from any article body has been promoted in this pass. No simulation code is committed; no parameter constant is changed.

**Gate status.** G3 closed 2026-05-01; the reference triple is unaffected. G1 (14-GHz unlockable-domain attribution) and G2 (UV-induced degradation at 280 nm) remain open and are not advanced by this entry.

**Provenance tier.** All three new entries are filed as `source_tier: P` (peer-reviewed primary) consistent with the journal venues (Rev. Sci. Instrum., Optics Express ×2). The Burkley2021 correction is at `source_tier: P` (arXiv preprint; journal status to be confirmed in a later pass).

**Asymmetric erosion protection.** No tightening or relaxation of any Level 0 / Level 1 parameter is proposed. Nothing on this page weakens any committed CHARTER row.

## 6 · See also

- [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](2026-05-04-bbo-cw-uv-lidt-task.md) — task-E task draft; the third scout pass section appended in this work is the chain-anchor for the entries filed today.
- [`logbook/2026-05-04-bbo-alternative-references.md`](2026-05-04-bbo-alternative-references.md) — parent task draft (tasks A-E) from which task-E was carved out.
- [`data/literature/Hannig2018/`](../data/literature/Hannig2018/), [`data/literature/Shaw2021/`](../data/literature/Shaw2021/), [`data/literature/Kraus2022/`](../data/literature/Kraus2022/) — the three new SCAFFOLD entries.
- [`data/literature/Burkley2021/`](../data/literature/Burkley2021/) — the corrected scaffold (folder name unchanged from 2026-05-06; internal citation strings updated).
- [`data/literature/Hemmerling2011/extracted.yaml`](../data/literature/Hemmerling2011/extracted.yaml) — `cross_check_notes.scout_pass_authorship_correction`, the procedurally identical correction filed in a previous pass.
- [`docs/KD-2026-XXX-uv-280nm.md`](../docs/KD-2026-XXX-uv-280nm.md) — the dossier entries (KD-UV280-005, -006, -008, -009, -012) that will consume the new extractions when they are promoted SCAFFOLD → DRAFT.
