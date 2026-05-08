# VECSEL systems as the seed-laser source class — steward direction

**Steward:** Ulrich Warring
**Date:** 2026-05-08
**Status:** STEWARD DIRECTION (literature artefact + components-page surface; no architecture-specific code)

## Header (CHARTER §9 trigger questions)

- **Affects Level 0 parameter?** no — Level 0 (³P₁/₂ - ³P₃/₂ detuning, two-photon Rabi rate, allowed scattering rate) was locked at G3 closure on 2026-05-01 and is unchanged by this direction.
- **Affects Level 1 parameter?** no — Level 1 (UV power at experiment input, beam quality, source linewidth budget) is *informed* by VECSEL-class linewidth (<100-110 kHz per Burd2023, <50 kHz per Burd2016 at 1141 nm), but the binding form remains the Level 0 row coupled through the loss budget. The seed-laser linewidth budget tightens as a consequence — *tightening* is permitted under the asymmetric-erosion-protection rule (`docs/principles.md` "Asymmetric erosion protection").
- **Affects success criterion?** no.

This direction therefore does not require Council-3 deliberation. It is a **source-class scoping decision**, recorded as a literature-anchored steward direction.

---

## 1 · Direction

**For current and future builds of `mg-plus-uv-chain`, VECSEL systems are the seed-laser source class.** The design principles guiding the seed laser are those described in:

> S. C. Burd, J.-P. Penttinen, P.-Y. Hou, H. M. Knaack, S. Ranta, M. Mäki, E. Kantola, M. Guina, D. H. Slichter, D. Leibfried, A. C. Wilson, "VECSEL systems for quantum information processing with trapped beryllium ions," *J. Opt. Soc. Am. B* **40**, 773-781 (2023).
> DOI: `10.1364/JOSAB.475467`. Open access.

The literature artefact landed alongside this entry is [`data/literature/Burd2023/`](../data/literature/Burd2023/) (`extracted.yaml` + `notes.md`, DRAFT). The components-page surface is [`docs/components/seed-lasers.md`](../docs/components/seed-lasers.md) (DRAFT).

---

## 2 · Why VECSEL, why these principles

The CHARTER (§1.5, §2, §4, §5.4) has named VECSELs as a candidate source class since v0.2; what was missing was a **named design-principles anchor** that downstream architecture work could point at. Burd2023 is that anchor because:

1. **Class-A laser dynamics.** Long external cavity (~125 mm) and short semiconductor carrier lifetime put the VECSEL in the photon-lifetime-dominated regime — no relaxation oscillation, suppressed ASE pedestal. This is the structural reason the VECSEL replaces the Yb-fibre source's 1.2 W ASE budget (Friedenauer 2006 §2; `Friedenauer2006/extracted.yaml::P_ASE`) with a fundamentally narrower spectrum.
2. **Single-frequency narrow linewidth.** Intracavity birefringent filter + 1 mm YAG etalon + PZT-tuned cavity length deliver < 100 kHz at 940 nm and < 110 kHz at 1252 nm. The criterion the paper makes explicit — *seed linewidth must be considerably less than the relevant atomic linewidth and the SHG cavity locking bandwidth so frequency noise is not converted to amplitude noise downstream* — transfers verbatim to the mg-plus-uv-chain LBO + BBO chain.
3. **Operational maturity.** "More than eight months of continuous use at ~ 1 W with less than 10 % power drift" addresses one of the open Burd2016-era questions on long-term VECSEL stability in trapped-ion-laboratory use.
4. **Wavelength flexibility.** Gain-mirror MBE growth covers 940 nm to 1252 nm in this paper alone; Burd2016 (same collaboration) covers 1117 nm and 1141 nm. The 1118 nm Friedenauer fundamental sits inside the demonstrated envelope of the Tampere ORC + NIST collaboration.

Friedenauer 2006 used a 2 W Yb-fibre laser at 1118 nm with `Δν < 200 kHz` and 1.2 W ASE — operational and well-understood, but with the polarisation-drift failure mode flagged in CHARTER §5.4.5 and the ASE-handling chain of components in front of the LBO cavity. A VECSEL seed at 1118 nm would replace those failure modes with a different set (gain-mirror thermal-management dependence; intracavity-element alignment), characterised in Burd2023 down to specific design choices.

---

## 3 · What is and is not being committed

**Committed by this direction:**

- The seed-laser layer of mg-plus-uv-chain is described by VECSEL physics, with Burd2023 as the design-principles anchor and Burd2016 as the wavelength-adjacent (1117 / 1141 nm) ²⁵Mg⁺ demonstration.
- Future literature work on seed-laser-class candidates is anchored to this cluster; alternative seed-laser-class candidates (Yb fibre per Friedenauer 2006, ECDL + tapered amplifier, …) remain on the comparison list but are not the default.
- The dossier entry `KD-UV280-015` (VECSEL pump option) is upgraded from a Burd2016-only `[P]` anchor to a Burd2016 + Burd2023 cluster.

**Not committed by this direction:**

- **No architecture-family-specific code in `/src/`.** The anti-seeding clause stays in force; Phase NG-* of the next-gen workplan ([`logbook/2026-05-08-next-gen-500mW-workplan.md`](2026-05-08-next-gen-500mW-workplan.md)) continues to live exclusively in `/notebooks/`.
- **No build commitment.** Procurement of a 1118 nm VECSEL gain mirror remains downstream of G1 / G2.
- **No retraction of Friedenauer 2006 as the reference baseline.** The Friedenauer architecture remains the reference baseline against which the next-gen workplan validates ([`logbook/2026-05-07-numerics-expansion-workplan.md`](2026-05-07-numerics-expansion-workplan.md), Phase E). VECSEL is the seed-class direction; LBO + BBO is the doubling-chain topology; the two are independent choices.
- **No Phase 4 architecture scoring.** Source-class scoping is upstream of axis-1 (Raman capability) and axis-2 (phase coherence) scoring; this direction provides *inputs* to that scoring, not outputs.
- **No change to Level 0 or Level 1 binding parameters.** The reference triple {Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹} stays locked at the G3-closure value.

---

## 4 · Linewidth budget — concrete consequence

For trace-ability, the VECSEL design-principle linewidth criterion translates into the following inequality at the mg-plus-uv-chain operating point:

```
Δν_seed (linewidth)  <<  min( Δν_atomic , Δν_cavity_lock_bandwidth )
```

with:

- `Δν_atomic` ≈ Γ_atomic / 2π for the relevant ²⁵Mg⁺ ³P₁/₂ - ³P₃/₂ transitions (Γ_atomic / 2π ≈ 41.8 MHz from `Burd2016/extracted.yaml::Doppler_cooling_residual_linewidth` natural-linewidth contribution)
- `Δν_cavity_lock_bandwidth` ≈ loaded cavity-mirror piezo resonance / 2π (Friedenauer 2006: ≈ 18 kHz from `Friedenauer2006/extracted.yaml::LBO_M2_piezo_resonance_loaded`)

The **binding** term is the cavity lock bandwidth, not the atomic linewidth. Friedenauer 2006 operated at < 200 kHz seed linewidth — which is an order of magnitude *above* the 18 kHz loaded piezo resonance, indicating the cavity lock is not the only noise-rejection mechanism (the cavity itself filters above its bandwidth). The Burd2023 < 100 kHz figure tightens this margin without inverting it.

For mg-plus-uv-chain, the seed-laser linewidth budget is therefore:

| Anchor | Value | Source |
|---|---|---|
| Atomic Γ / 2π | ≈ 41.8 MHz | natural linewidth, ²⁵Mg⁺ 3p excited state |
| LBO cavity locking bandwidth | ≈ 18 kHz | Friedenauer 2006, loaded piezo resonance |
| Friedenauer Yb-fibre seed | < 200 kHz | Friedenauer 2006, §2 |
| VECSEL state-of-art at adjacent λ | < 100 kHz (Burd2023, 940 nm) and < 50 kHz (Burd2016, 1141 nm) | Burd2023, Burd2016 |
| **Operating budget for new build** | **target ≤ 100 kHz; floor ≈ 200 kHz Friedenauer parity; ceiling 50 kHz Burd2016 stretch** | this direction |

The "operating budget" row is a *Sail* recommendation (`docs/principles.md`), not a Coastline requirement. It will be revisited if Phase 2 baseline measurements expose a different binding noise mechanism.

---

## 5 · ASE budget — concrete consequence

Friedenauer 2006 §2 reports 1.2 W of broadband ASE peaked between 1060 and 1100 nm, non-resonant with the LBO cavity but contributing thermal load and isolator stress. The VECSEL class-A-regime claim in Burd2023 §1 — *"broad spectral pedestal due to amplified spontaneous emission ... is largely absent"* — implies a VECSEL seed eliminates this 1.2 W ASE budget and the corresponding ASE-handling components in the front-end (whatever those are; Friedenauer 2006 is silent on the specific filter element, recorded as `Friedenauer2006::P_ASE` and as `OPEN` in the components inventory).

For the next-gen build, this means:

- The pre-LBO conditioning chain shrinks. The Friedenauer-class ASE filter is not needed.
- The LBO cavity is not loaded by 1.2 W of broadband non-resonant pump; thermal and intensity stress on the IC and HRs is reduced.
- The optical isolator at 1118 nm (Friedenauer used a 1064 nm-design isolator at ~ 90 % transmission) can be respecified for narrower bandwidth.

These are *upstream* consequences of the source-class change. They do not change Level 0 or Level 1 parameters but they materially change the front-end loss budget that feeds Phase NG-A (LBO `L_passive` gap closure).

---

## 6 · Cross-references

- [`docs/components/seed-lasers.md`](../docs/components/seed-lasers.md) — components-page surface for this direction.
- [`data/literature/Burd2023/`](../data/literature/Burd2023/) — primary literature artefact (`extracted.yaml` + `notes.md`).
- [`data/literature/Burd2016/`](../data/literature/Burd2016/) — wavelength-adjacent ²⁵Mg⁺ companion paper (existing).
- [`data/literature/Friedenauer2006/`](../data/literature/Friedenauer2006/) — reference Yb-fibre baseline against which the VECSEL direction is contrasted.
- [`docs/KD-2026-XXX-uv-280nm.md`](../docs/KD-2026-XXX-uv-280nm.md) — `KD-UV280-015` (VECSEL pump option) is the dossier-level home of this direction.
- [`logbook/2026-05-08-next-gen-500mW-workplan.md`](2026-05-08-next-gen-500mW-workplan.md) — §9 of that workplan explicitly listed VECSEL pump-source-class as out-of-scope follow-up; this entry is the corresponding follow-up artefact (it does *not* re-open the next-gen workplan, which keeps Friedenauer-2006 doubling-chain topology fixed).
- [`CHARTER.md`](../CHARTER.md) §1.5, §3, §4, §5.4.5 — VECSEL mentions across the Charter; this direction is consistent with all of them.

---

## 7 · Acceptance and review

This logbook entry is **steward direction**. Steward sign-off lands in the file's commit message; assistant-stance review and assistant-attributable refinement of the cited Burd2023 extraction can continue in future passes.

A future pass should:

1. Verify the Burd2023 numerical figures against the published version of record (the extraction was made from the open-access HTML/PDF; minor figures should be checked against the typeset PDF for the steward sign-off pass).
2. Compare the Friedenauer + VECSEL composite linewidth and ASE budgets against the Phase 2 baseline measurement once that lands (currently unblocked, not yet started; see `docs/index.md` "At a glance").
3. Identify the specific 1118 nm gain-mirror specification needed to bring the Burd2023 design into the mg-plus-uv-chain front-end — out-of-scope for this entry; logged as a future follow-up after G2 closes.
