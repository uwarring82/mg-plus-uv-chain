# Public record corrections — D6 / RC-09 / RC-10

**Date:** 2026-09-09
**Steward:** Ulrich Warring
**Baseline:** `c16345e`
**Status:** First public-facing correction set; numerical work packages remain open.
**Task:** [Repository review card](2026-09-09-repository-review-task-card.md), D6 with RC-06/09/10 follow-through.

## Charter §9 trigger questions

- **Affects Level 0 parameters?** No.
- **Affects Level 1 parameters?** No.
- **Affects success criteria?** No.
- **Changes Charter text or gate state?** No. Charter, reference triple and gate records are unchanged.
- **Changes document licence assignments?** Existing split declarations and prior CC-BY-4.0 grants are recorded; no new restrictive assignment is made. The 12 architecture/component assignments remain pending steward disposition.

## Direction and scope

The steward requested simpler public language as part of D6. Retain
Coastline (CC-BY-SA-4.0), Sail (CC-BY-NC-SA-4.0), Handbook (MIT), and
Model B (distributed copies pinned by checksum) in licence/provenance
contexts. Retain Charter references and G1–G3. Describe public review and
accountability in single-steward terms; the Charter's historical role names
and procedures remain in the frozen document.

This first set covers README, the landing page, the 12 architecture/component
pages, shared footers, licence notices, asset-provenance navigation and the
coverage-status wording. It preserves quantitative tables and their technical
limitations. The landing page now links the September receipt and review
rather than soliciting a pre-order coating review after the mirrors arrived.
Its May numerical snapshot remains explicitly historical and awaiting review.

## Evidence and dispositions

| Check | Result on 2026-09-09 | Disposition |
|---|---|---|
| `git ls-remote --tags origin` | Successful response with no tags | Remove the README claim of a DOI registered against a v1.0 tag; distinguish Charter version from software release |
| `gh api repos/uwarring82/mg-plus-uv-chain/releases --jq 'length'` | 0 releases | Record the dated remote result, not a permanent absence claim |
| Pages API source | `main`, `/docs`, legacy build; status `built` | README describes Jekyll Pages from `/docs`; no deployment configuration change |
| Zenodo exact-name search | No verified record found by web search; records API request timed out | State **DOI not verified**. Do not infer that no deposit exists or create one |
| Split-licence introduction | `e67bdaa` added the map and folder declarations; it did not add the adoption log cited by the map | Replace the broken adoption-record assertion with the actual commit evidence; missing approval record remains open |
| Architecture/component coverage | 8 architecture + 4 component Markdown pages, absent from the original split map | List each page in LICENSES.md. Show the existing blanket CC-BY-4.0 declaration on each page; mark split assignment pending |
| Prior blanket versus split declarations | LICENSE-DOCS, README, index and shared footers disagreed with LICENSES.md | Distinguish existing split scope and prior grants; remove the universal CC-BY-4.0 claim from navigation/footer summaries |
| Jekyll exclusions | `*.py`, `*.yml.bak`, `literature/` match no paths under `docs/` | Remove current no-ops; future scope validation belongs to RC-06/09 |
| Coverage | ≥90% is a Charter requirement; CI enforcement is not configured | Correct status.md now; implementing enforcement remains RC-06 |
| Coating-run §9 records | Parent `workplan.md` and `bc-g-log.md` contain trigger blocks | No automatic per-file duplication; child-scope inspection remains within RC-10's record audit |

Creative Commons summaries follow the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/),
[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) and
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) deeds.
The original grants remain part of the history; these wording corrections
do not purport to revoke them or relicense third-party material.

## Validation and remaining work

Checks passed for Markdown/front-matter structure, all 12 licence-table
entries/notices, newly introduced local link targets, preserved seed-laser
fragment anchors, unchanged scientific table values and protected files/assets.
The review card's embedded arithmetic ran successfully on Python 3.9.7.
Fifteen local Markdown/layout previews generated and passed HTML-structure
checks. Browser inspection was unavailable (`No browser is available` from
the browser tool), so this is not a visual QA or a full Jekyll build claim.
CI/site-build verification remains within RC-06.

D6 remains open for the intended split assignments, other unmapped pages and
assets, and public contact/Git identity. The missing adoption record remains
unresolved. RC-09 still owns the wider status, schema and link audit; RC-06
still owns CI and supported-environment enforcement. No release, DOI deposit,
Git author-configuration change or history rewrite is made by this work.

**Initial publication status (at `16eea0a`):** the first correction set was
committed locally; it had not been pushed or deployed at that point. The
README follow-up below precedes publication of the reviewed commits.


## RC-09 follow-up — README status and existing paths

**Baseline:** `16eea0a`; checked 2026-09-09.

The dossier index lagged its own detail sections: entries **008, 009, 011
and 012** each already stated **POPULATING / Operationally bounded** in
their closing paragraphs, while their index rows said SCAFFOLD / TBD.
The four index rows now reflect those existing classifications. The count
is **8 POPULATING + 1 DRAFT + 6 SCAFFOLD = 15 entries**, so **9/15** are
past scaffold. Separately, `git ls-files 'data/literature/*/extracted.yaml'`
returns **22** tracked extraction files. Neither count is a new scientific
acceptance or a gate disposition.

The README now dates these counts, links their source and the September
review/correction records, and lists only existing paths in its selected
layout tree. The four absent paths (`data/baseline/` and the three proposed
dedicated comparison/stability/protocol pages) are explicitly marked planned.
The stale CC-BY-4.0 annotation on LICENSE-DOCS in that tree is also corrected.
Draft constraints are distinguished from locked values in `parameters.py`.

Validation: recomputed dossier status counts from the index, cross-checked
the four changed rows against their detail sections, checked all listed tree
paths against tracked repository content, and checked README local links and
fragments. The planned paths remain absent. No numerical code, constraints,
Charter text or gate records changed.

The steward also withdrew the earlier regex-based claim that coating-run
children need duplicate §9 blocks; their parent workplan and BC-G records
supply the relevant context. The reported CSS-class check found only the
pre-existing `notebook-content` hook; this is corroborating source inspection,
not a substitute for the still-outstanding browser visual QA.
