# Burd2023 Extraction Notes

**Citation:** S. C. Burd, J.-P. Penttinen, P.-Y. Hou, H. M. Knaack, S. Ranta, M. Mäki, E. Kantola, M. Guina, D. H. Slichter, D. Leibfried, and A. C. Wilson, "VECSEL systems for quantum information processing with trapped beryllium ions," *Journal of the Optical Society of America B* **40**, 773-781 (2023), DOI: `10.1364/JOSAB.475467`. Affiliations: Time and Frequency Division, NIST Boulder (Burd, Hou, Knaack, Slichter, Leibfried, Wilson) and Optoelectronics Research Centre, Tampere University (Penttinen, Ranta, Mäki, Kantola, Guina) — same NIST + Tampere collaboration that produced [Burd2016](../Burd2016/).

**Source used:** open-access HTML/PDF of the paper at the publisher (Optica). Not committed to repository.

## Why this paper

Steward direction on 2026-05-08: VECSEL systems are the seed-laser source class for current and future builds of `mg-plus-uv-chain`, and the **design principles of Burd2023 are the anchor** for that direction. This extraction is the literature artefact that pins those principles to a citable source so downstream architecture work has something concrete to point at.

The paper is the natural follow-up to [Burd2016](../Burd2016/): same collaboration, refined and rebuilt VECSEL architecture, two new wavelength routes (940 → 235 nm for ⁹Be⁺ photoionisation; 1252 → 313 nm for ⁹Be⁺ Doppler cooling). The systems are not at the `mg-plus-uv-chain` 1118 nm fundamental, but the **design philosophy is wavelength-agnostic** and is the part being inherited.

## What this extraction is for (and what it isn't)

- **It is** a Phase 1 literature artefact: a `[P]`-tier capture of the design principles, output-power / linewidth / efficiency figures, and gain-mirror + cavity architecture details.
- **It is** the `[P]` anchor for `KD-UV280-015` (VECSEL pump option), upgraded from the Burd2016-only state to a Burd2016 + Burd2023 cluster.
- **It is not** an architecture-family-specific simulation. No `/src/` change is implied. The anti-seeding clause (`docs/principles.md` §5.1) is unaffected.
- **It is not** a build commitment. The CHARTER §1.5 indicative-anchor 500 mW @ 280 nm target stays as-is; the binding form remains the Level-0 row.
- **It is not** a wavelength-matched reference. The mg-plus-uv-chain 1118 nm fundamental is not directly demonstrated in this paper; Burd2016 (1117 nm IC-VECSEL) is closer, and any 1118 nm VECSEL build would still need a respecified gain mirror.

## Extraction Scope

The 2026-05-08 pass extracts the full body of the paper:

- **§1 introduction.** VECSEL motivation: class-A laser regime (long external cavity, short carrier lifetime → photon-lifetime-dominated → suppressed relaxation oscillation and ASE pedestal); narrow linewidth (<100 kHz) and good intensity stability; broad wavelength coverage by gain-mirror design; compactness vs Ti:Sapphire + green-pump systems.
- **§2 VECSEL designs.** Common architecture (linear external cavity ~125 mm; ~2 % output-coupler transmission, RoC = 200 mm; intracavity birefringent filter + 1 mm YAG etalon for single-mode operation; PZT-tuned cavity length for fine frequency control; flip-chip or top-emitting gain mirrors with diamond heat spreaders bonded to TEC-stabilised water-cooled copper heatsinks; dry-N₂ purge of the laser enclosure for moisture-sensitive wavelengths). Material-specific designs:
  - **940 nm gain mirror:** GaInAs/GaAs QWs, 24 in 12 antinodes, GaAsP strain compensation, GaAs/AlAs DBR. Multi-crystal diamond heat spreader.
  - **1252 nm gain mirror:** GaInNAs/GaAs QWs, nitrogen incorporation extends GaInAs range to longer wavelengths via bandgap bowing without lattice mismatch. Two candidate Structures A and B characterised in detail; Structure A selected as closer to the 1252 nm target. Single-crystal diamond heat spreader, top-emitting intracavity geometry.
- **§3 940 nm → 470 nm → 235 nm chain.** PPKTP enhancement cavity (PDH-locked) → 470 nm at 270 mW from 480 mW IR injected; thermal lensing in the PPKTP limits cavity-locking stability above ~ 0.5 W IR. BBO Brewster-cut enhancement cavity (Hänsch-Couillaud-locked) → 235 nm at 54 mW from 270 mW visible. Validation: ⁹Be⁺ photoionisation resonance at 1276.080 THz UV agrees with literature.
- **§4 1252 nm → 626 nm → 313 nm chain.** Fiber-coupled PPLN waveguide doubler (NTT WH-0626-000-A-B-C) → 626 nm at 530 mW from 1.63 W IR injected (33 % conversion including fiber coupling). BBO Brewster-cut enhancement cavity → 313 nm at 41 mW from 330 mW visible. Validation: ⁹Be⁺ Doppler cooling and repumping line shape and time constant (τ = 0.55(4) µs) indistinguishable from existing fiber-laser-based source.

## Extraction Passes

- **2026-05-08 (assistant under steward direction, DRAFT).** Initial full-body extraction from the open-access version. Status `DRAFT` (not yet steward-signed-off).

## Review Notes

- **Design-principle anchor.** The load-bearing claim of the paper is the class-A laser regime: photon-lifetime-dominated dynamics that suppress relaxation oscillation and ASE. This is the *single* principle that propagates from this paper into mg-plus-uv-chain's seed-laser layer.
- **Linewidth principle.** Both VECSELs are stated to have linewidth "considerably less than the linewidths of relevant atomic transitions and sufficiently narrow that frequency fluctuations will not be converted to significant amplitude fluctuations by subsequent resonant frequency-doubling stages." This sentence is the criterion that any seed-laser candidate for mg-plus-uv-chain must meet, with the relevant atomic linewidth being the ²⁵Mg⁺ ³P₁/₂ - ³P₃/₂ transitions and the relevant SHG-cavity locking bandwidth being set by the LBO and BBO ring cavities.
- **Long-term operation.** "Over more than eight months of continuous use at an output power of about 1 W, less than 10 % power drifts observed" — this is operational maturity evidence for the VECSEL as a trapped-ion-laboratory seed laser, addressing one of the open questions in [Burd2016](../Burd2016/).
- **Bottleneck shift.** The PPKTP first-stage cavity-locking instability (attributed to thermal lensing) above ~ 0.5 W injected IR is a structural feature of PPKTP enhancement-cavity SHG that does not directly transfer to the LBO + BBO Friedenauer chain at 1118 nm; LBO has a much higher LIDT and thermal robustness than PPKTP. But the principle — *visible-stage SHG, not UV-stage SHG, becomes the binding constraint in VECSEL-pumped chains* — is consistent with the Burd2016 observation that the LiNbO₃ waveguide at the 1118 → 559 nm stage was the bottleneck rather than the BBO 280 nm stage.
- **Wavelength gap.** Burd2023 demonstrates 940 nm and 1252 nm VECSELs; mg-plus-uv-chain needs 1118 nm. Burd2016 (same collaboration) already demonstrates 1117 nm and 1141 nm VECSELs, so 1118 nm is in the demonstrated-gain-mirror envelope. A specific 1118 nm gain mirror would still need to be respecified — a future collaboration question with Tampere ORC, not solved by this paper.
- **No wavelength-specific 25Mg+ data.** This paper is a 9Be+ paper; 25Mg+-specific photoionisation, cooling, or coherent-control data are not in scope. For 25Mg+-specific VECSEL data, [Burd2016](../Burd2016/) remains the primary reference.

## Downstream Dossier Links

- `KD-UV280-015` (VECSEL pump option). Burd2023 is added as a `[P]`-tier source alongside [Burd2016](../Burd2016/). Together they cover:
  - **Burd2016:** two wavelength-matched 25Mg+ demonstrations at 1117 nm (IC) and 1141 nm (VC) → 280 nm and 285 nm UV via BBO buildup cavities. The 280 nm operating point is the relevant one for mg-plus-uv-chain.
  - **Burd2023:** the design-principles statement (class-A regime, single-frequency narrow linewidth, intracavity BRF + etalon + PZT mode selection) and the operational-maturity statement (8+ months at ~ 1 W with < 10 % drift). Wavelengths are not 25Mg+ but the principles transfer.

## Cross-Reference to Steward Direction

This extraction is the literature artefact for the steward-direction logbook entry [`logbook/2026-05-08-vecsel-seed-lasers.md`](../../../logbook/2026-05-08-vecsel-seed-lasers.md). The components-page surface for the same direction lives at [`docs/components/seed-lasers.md`](../../../docs/components/seed-lasers.md).
