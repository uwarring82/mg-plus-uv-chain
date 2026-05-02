# `docs/assets/` — provenance record

**Endorsement Marker:** Local copy of upstream design assets. Borrowed under the MIT licence per the threehouse-plus-ec/cd-rules split-licence architecture (cd-rules §0.3, §0.10, §0.11). No external endorsement of this project's content is implied by re-use of the visual identity.

**Distribution model:** cd-rules §0.10 *Model B (distributed copy + checksum)* — local copies are pinned to a specific upstream commit; checksums make drift visible rather than silent.

---

## Upstream source

| Field | Value |
|---|---|
| Source repository | [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) |
| Source commit (pinned) | `ee01c80352dd8446f189c3159a3d9e347463902c` |
| Source commit date | 2026-04-17 |
| Local copy date | 2026-05-02 |
| Licence | MIT (cd-rules §0.3 *Handbook* layer) |

## Files copied

| File | SHA-256 | Notes |
|---|---|---|
| `tokens.css` | `68b5876f35aad95cb32d06e8c0c05a88366a45e75aab15fbdc0e43c179b27d94` | Verbatim copy of cd-rules `tokens.css` with provenance header rewritten for this folder. Token *values* are not redefined locally per cd-rules §0.12. |
| `emblem-32.svg` | `e799f0bd9ddc5d36c6904c43690c8507215ea78d5d12cc5fec53992bade9ff0b` | Verbatim copy of cd-rules `emblem-32.svg`. Used as the favicon and the header brand-lockup mark to signal threehouse-stewardship of this project. |
| `wordmark-full.svg` | `84defa4091307bd59a30b262ea83d1e244da0d317770dbf56661baaa09add0f2` | Verbatim copy of cd-rules `wordmark-full.svg`. Used in the colophon only — never as the site identity (this site's identity is the project name `mg-plus-uv-chain`). |

## Files derived (not verbatim)

| File | Derivation | Notes |
|---|---|---|
| `site.css` | Adapted from the `<style>` block in cd-rules `index.html` at the pinned commit. Tokens stripped (kept in `tokens.css`); page-specific demonstrator chrome (hero-panel circles, layer-stack, evidence-grid) omitted. Prose typography rules added for Jekyll-rendered markdown. | Distributed under MIT per cd-rules §0.3 *Handbook* layer; the derived work is offered under the same licence. |

## Drift detection

Compare the SHA-256 hashes above against the upstream file hashes at the pinned commit. If a mismatch exists and no justification is recorded below, the local copy is stale and should be updated within one cd-rules release cycle (cd-rules §0.10).

```bash
# Local check
shasum -a 256 docs/assets/tokens.css docs/assets/emblem-32.svg docs/assets/wordmark-full.svg

# Upstream check (requires gh CLI)
gh api repos/threehouse-plus-ec/cd-rules/contents/tokens.css \
  --jq '.content' | base64 -d | shasum -a 256
gh api repos/threehouse-plus-ec/cd-rules/contents/emblem-32.svg \
  --jq '.content' | base64 -d | shasum -a 256
gh api repos/threehouse-plus-ec/cd-rules/contents/wordmark-full.svg \
  --jq '.content' | base64 -d | shasum -a 256
```

## Justified divergences

*(none at this commit)*

## Update log

| Date | Action | Notes |
|---|---|---|
| 2026-05-02 | Initial copy | Pinned to cd-rules commit `ee01c80`. |

---

## Licence

Files copied under cd-rules §0.3 *Handbook* layer are MIT-licensed. The MIT notice is embedded in `tokens.css` and applies in the same form to the SVG files and to `site.css` as a derived work. See cd-rules `LICENCE` for the full upstream text.
