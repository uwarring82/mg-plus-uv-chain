# Hume2010 Extraction Notes

**Citation:** D. B. Hume, *Two-Species Ion Arrays for Quantum Logic Spectroscopy*, Ph.D. thesis, University of Colorado / NIST Boulder (2010). 129 pages.

**Source used:** open-access NIST PDF copied on 2026-05-06 to ignored path `downloads/literature/task-e/Hume2010_NIST_open.pdf`.

## Why this paper

Identified in the first scout pass as an institutional thesis breadcrumb toward NIST operational records on Mg⁺ Doppler / Raman 280 nm BBO doubling cavities. `[S]`-tier source. Lower priority for Task E than the peer-reviewed `[P]` papers in the cluster. Useful for `KD-UV280-001` architecture-family corroboration and as a pointer to NIST Wineland-group operational records.

## Extraction Scope

The 2026-05-06 pass is a **targeted partial extraction**. The thesis is 129 pages and most of it is about Be⁺ / Al⁺ quantum-logic spectroscopy, ion reordering, and QND measurements — not relevant to Task E. The relevant content is concentrated in §3.2.3 ("Mg⁺ Lasers", page 39), which is a single paragraph documenting the architecture but giving no detailed numerical content. §3.2.1 ("Be⁺ lasers") and §3.2.2 ("Al⁺ lasers") on pages 32-39 give more detail on the analogous Be⁺ at 313 nm and Al⁺ at 267 nm laser systems but are not Mg⁺ / 280 nm specific.

What the targeted extraction yields:

- §3.2.3 Mg⁺ Lasers (page 39): two laser sources for Mg⁺.
  - Mg-Doppler: dye laser at 560 nm (similar to Be⁺ laser systems) → BBO doubling cavity → 280 nm. Dither-locked to a reference cavity external to the dye-laser cavity.
  - Mg-Raman: fiber laser at 1120 nm (similar to Al⁺ laser systems) → LBO doubling cavity → 560 nm → BBO doubling cavity → 280 nm. Natural fiber-laser stability sufficient for stimulated Raman; not stabilised to any external reference.
- §3.2.2 (page 37) gives Yb-fiber-amplifier specifications used in the Al⁺ system: 4 W diode pump at 976 nm, NCPM LBO 2 cm at ~140 °C, BBO doubling cavity for the ³P₀ laser at 267 nm (1 mW UV) and KD\*P doubling cavity for the ³P₁ laser at 267 nm (5-25 mW UV). The Mg-Raman 1120 nm fiber-laser system is described as "similar to" the Al⁺ system, so the architectural parallels apply.
- The thesis does **not** give any of: BBO crystal vendor / dimensions / cut for the Mg⁺ stage; UV output power for the Mg⁺ system; operational-lifetime data; degradation observations; cleanliness protocol.

## Extraction Passes

- **2026-05-06 (assistant under steward direction, partial DRAFT).** Targeted extraction of §3.2.3 Mg⁺ Lasers and adjacent §3.2.1-3.2.2 Be⁺ / Al⁺ context. Rest of the 129-page thesis was not extracted because it covers Be⁺ / Al⁺ quantum-logic experiments not relevant to Task E. Status promoted from `SCAFFOLD` to **partial DRAFT** (acknowledging that a fuller extraction is possible if the steward needs the Mg-related QIP content for later Phase 1 dossier entries beyond `KD-UV280-001`).

## Review Notes

- **Architecture-family corroboration only.** The Hume2010 Mg⁺ Raman laser is a 1120 nm Yb-fiber + LBO + BBO chain producing 280 nm — essentially the same architecture as Friedenauer 2006 (1118 nm) and Hemmerling2011 (1118.21 nm), with a 2 nm shift in the fundamental. The Mg-Doppler chain is a dye-laser + BBO version (similar to Kjaergaard2000's architecture). NIST operates *both* a Yb-fiber-pumped chain and a dye-laser-pumped chain in parallel for the same Mg⁺ ion.
- **No operational-lifetime number.** Same gap as Hemmerling2011, Kjaergaard2000, Burd2016. The thesis documents what's there but not how often it breaks.
- **Pointer to NIST Wineland group institutional records.** The thesis was supervised by Dave Wineland and Till Rosenband (acknowledgements page v); the experimental apparatus was operational at NIST Boulder for the Al⁺ optical clock work (Rosenband 2008 Science). Any institutional `[I]` record from this lab is gated on the Wineland group's archive policy. Section 3 of the thesis acknowledges that the Mg⁺ system is similar to the Al⁺ Raman laser system, so the relevant logbook / lab-notebook records would be in the Al⁺ workflow.
- **Direct architectural parallel to Friedenauer 2006 in different lab.** The fact that NIST runs the same essential architecture as the Garching → Freiburg lineage with no special workarounds documented suggests that the architecture is reproducible; this is a *qualitative* validation of the Friedenauer-class baseline.

## Downstream Dossier Links

- `KD-UV280-001`: single-source quadrupling demonstrated. Hume2010 contributes corroboration that NIST operates a Yb-fiber + LBO + BBO chain at 1120 → 560 → 280 nm for Mg⁺ Raman, and a dye-laser + BBO chain at 560 → 280 nm for Mg⁺ Doppler. `[S]`-tier source supporting the architecture-family lineage. Should accompany Friedenauer 2006 (`[P]`) and Hemmerling2011 (`[P]`) but cannot stand alone.
- `KD-UV280-005`: no quantitative contribution. Architecture-only documentation.
- `KD-UV280-015`: 1118-1120 nm Yb-fibre pump option corroboration. NIST uses 1120 nm at the Mg-Raman stage; Friedenauer uses 1118 nm; Hemmerling uses 1118.21 nm. 2 nm spread across the lineage is operationally insignificant.
