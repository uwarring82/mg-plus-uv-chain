# Repository made public on GitHub; GitHub Pages enabled

**Steward:** Ulrich Warring
**Date:** 2026-06-26
**Status:** INFRASTRUCTURE / PUBLICATION EVENT. The `mg-plus-uv-chain` repository was created on GitHub as a **public** repository and its documentation site was enabled via **GitHub Pages** (Jekyll, served from `main:/docs`). No source code, binding parameter, or gate status changed.

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — publication changes *visibility*, not the §1.5 Level 0 row (³P₁/₂–³P₃/₂ detuning, two-photon Rabi rate, allowed scattering rate) nor the G3-closure reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}`.
- **Affects Level 1 parameter?** no.
- **Affects success criterion?** no.

This entry does not require Council-3 deliberation. It records a **one-way publication action** (a world-readable repository and an indexable site) and the safety checks performed before it.

## Anti-seeding boundary

Publication does not alter the anti-seeding clause: `/src/` remains architecture-neutral; architecture-specific exploration stays in `/notebooks/`; literature extractions stay under `/data/literature/`. What changed is that these artefacts are now world-readable. The pre-publication scan (§2) confirmed no secrets, credentials, or unintended private material were exposed, and the existing `.gitignore` continues to hold private material (`/outreach/`, local DRAFT correspondence, literature PDFs) out of the repository.

---

## 1 · What was done

- **Created the public repository** `uwarring82/mg-plus-uv-chain`. The `origin` remote had been configured locally, but no repository existed on GitHub (`git ls-remote origin` returned *"Repository not found"*); this action created it, public, with a one-line description from the site config.
- **Pushed `main`** — 63 commits at publication (~8.9 MB history).
- **Enabled GitHub Pages** — source `main` branch, `/docs` folder, Jekyll "legacy" (deploy-from-branch) build, HTTPS enforced. First build succeeded in ~35 s. Site: <https://uwarring82.github.io/mg-plus-uv-chain/>.
- **Set the repository homepage** to the Pages URL.

## 2 · Pre-publication safety scan

Performed before creating the public repository:

- **Secret scan** of the tracked tree (`git grep` for `api_key|secret|password|token|private key|BEGIN … PRIVATE KEY|aws_|gh[op]_`): only false positives (CSS `tokens.css` references). No real secrets.
- **No credential/config files tracked** (`.env`, `*.pem`, `id_rsa`, `*.key`).
- **No build/test artefacts tracked** (`.coverage`, `*.egg-info`, `.pytest_cache`, `.DS_Store` all absent from `git ls-files`).
- **`.gitignore` confirmed** to exclude `/outreach/`, the local expert-review DRAFT, and `data/literature/**/*.pdf`.

## 3 · What is *not* in this entry

- The local `bc-g-addendum` branch (M2′ piezo-mirror BC-G addendum) was **not** pushed; only `main` is public.
- **One-way action note.** History is public from this point onward; any sensitive content in *earlier* commits would now be exposed. The pre-push scan found none, but this is recorded as the standing caveat of the publication event.

## See also

- [Principles](../docs/principles.md) — anti-seeding clause; constraint hierarchy.
- [2026-06-26 — VECSEL systems tutorial and in-house lab-note extraction](2026-06-26-vecsel-systems-tutorial-and-labnotes.md) — the documentation work that followed publication.
- Live site: <https://uwarring82.github.io/mg-plus-uv-chain/>.
