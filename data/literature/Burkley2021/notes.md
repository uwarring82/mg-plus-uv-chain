# Burkley2021 Extraction Notes

**Citation:** Z. Burkley, L. de Sousa Borges, B. Ohayon, A. Golovozin, J. Zhang, P. Crivelli, "Stable High Power deep-UV Enhancement Cavity in Ultra High Vacuum with Fluoride Coatings," arXiv:`2105.14977v1` (31 May 2021). Affiliations: ¹Institute for Particle Physics and Astrophysics, ETH Zürich; ²Lebedev Physical Institute, Moscow.

**Source available:** open-access arXiv preprint copied on 2026-05-06 to ignored path `downloads/literature/task-e/vonMilczewski2021_arxiv_open.pdf` (filename is the scaffold-era misnomer; see §Scaffold author-list correction below). The file content is the Burkley et al. preprint. Structured extraction beyond bibliographic confirmation still pending.

## Scaffold author-list correction

The original Task E scaffold (committed 2026-05-06) recorded this paper as **"vonMilczewski2021"** based on a public-metadata guess made before the PDF was in hand. Direct read of the arXiv PDF on 2026-05-13 confirms the correct first author is **Z. (Zakary) Burkley** (ETH Zürich), with co-authors L. de Sousa Borges, B. Ohayon, A. Golovozin (Lebedev), J. Zhang, and P. Crivelli. There is no author named "von Milczewski" on this paper; the original scaffold attribution is an error analogous to the one logged for Hemmerling2011 (`scout_pass_authorship_correction` in `data/literature/Hemmerling2011/extracted.yaml`).

This folder name (`Burkley2021/`) is correct and was used from creation; the internal `citation_key`, `citation`, and notes-header strings have been corrected in this pass. The download filename `vonMilczewski2021_arxiv_open.pdf` is retained in the gitignored `downloads/` tree as historical artefact and is **not** renamed (it is not committed to the repo, and renaming would break the chain-of-provenance trail back to the 2026-05-06 scout pass commit).

## Why this paper

Identified in the third scout pass as the **most directly transferable CW deep-UV intracavity mirror-lifetime data** for `KD-UV280-008` and `KD-UV280-012`. Reports oxide (HfO₂ / Al₂O₃ on SiO₂) coating degradation in UHV (10⁻⁸ mbar) at ~5 W intracavity within minutes, and fluoride (MgF₂ / LaF₃ on CaF₂) coating survival at 10 W intracavity for hours, with 20 W for several hours in O₂-rich environments (10⁻⁴ – 1 mbar O₂). UV-ozone / O₂ exposure recovers oxide mirrors but the recovery becomes ineffective after several applications. The closest published wavelength is ~244 nm (Yb-quadrupling regime), not 280 nm — but the oxygen-depletion / hydrocarbon-contamination mechanism is wavelength-scalable and the operating-power range overlaps the Friedenauer-class envelope.

## Extraction targets

When the structured pass is run, extract:

1. Cavity wavelength (likely ~243-244 nm from the abstract context).
2. Intracavity power, finesse, and beam waist at the mirrors for each test geometry.
3. Coating stack composition and substrate for the oxide and fluoride mirrors.
4. Oxygen / hydrocarbon partial-pressure thresholds for oxide-coating failure.
5. Time-to-failure at fixed intracavity power for oxide coatings (the abstract states "minutes" at "lower intracavity powers" for oxides vs "hours" at 10-20 W for fluorides).
6. Fluoride-coating reflectivity / loss vs power and time over the test interval.
7. UV-ozone / O₂ cleaning protocol and recovery factor for oxide coatings.
8. Authors' mechanism statement (oxygen-depletion vs photodecomposition vs hydrocarbon polymerisation).
9. Any direct comparison to Gallego2017 thesis or other UHV / deep-UV cavity precedents.

## Status

`SCAFFOLD` — open-access arXiv PDF is available locally, authorship and bibliographic record are now corrected against the PDF, but no numerical extraction has been performed from the article body.

## Extraction passes

- **2026-05-06 (assistant under steward direction, SCAFFOLD).** Created bibliographic scaffold from public arXiv metadata; first-author guess "vonMilczewski" recorded under that (incorrect) citation key inside the (correctly-named) `Burkley2021/` folder.
- **2026-05-13 (assistant under steward direction, SCAFFOLD-corrected).** Confirmed bibliographic record against the arXiv PDF (now in hand under `downloads/literature/task-e/`). Corrected the `citation_key`, `citation`, and notes-header strings from the scout-pass author guess to the actual Burkley/de Sousa Borges/Ohayon/Golovozin/Zhang/Crivelli author list. Filed by `2026-05-13-task-e-third-scout-pass` paragraph in [`logbook/2026-05-04-bbo-cw-uv-lidt-task.md`](../../../logbook/2026-05-04-bbo-cw-uv-lidt-task.md). Status remains `SCAFFOLD` — numerical extraction targets enumerated above are still open.
