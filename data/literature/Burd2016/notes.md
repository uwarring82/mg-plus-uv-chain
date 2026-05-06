# Burd2016 Extraction Notes

**Citation:** S. C. Burd, D. T. C. Allcock, T. Leinonen, J. P. Penttinen, D. H. Slichter, R. Srinivas, A. C. Wilson, R. Jördens, M. Guina, D. Leibfried, and D. J. Wineland, "VECSEL systems for the generation and manipulation of trapped magnesium ions," *Optica* **3**, 1294-1300 (2016), DOI: `10.1364/OPTICA.3.001294`. Affiliations: ¹Time and Frequency Division, NIST Boulder (Burd, Allcock, Slichter, Srinivas, Wilson, Jördens, Leibfried, Wineland), ²Optoelectronics Research Centre, Tampere University of Technology (Leinonen, Penttinen, Guina).

**Source used:** open-access NIST author-deposit PDF copied on 2026-05-06 to ignored path `downloads/literature/task-e/Burd2016_NIST_open.pdf`.

## Why this paper

Identified in the second scout pass as a modern Mg⁺ source paper, primarily relevant to `KD-UV280-015` (VECSEL pump option) rather than to Task E's BBO-stage LIDT focus. Lower payoff for Task E than the Kondo / Kubota / Burkley / Brown / Kumar cluster, but valuable as a recent demonstration of Mg⁺ trapped-ion operation with **two distinct VECSEL-based source architectures** that produce 280 nm and 285 nm CW UV via BBO buildup cavities. Documents an alternative-to-Yb-fiber pump route that the dossier should track for Phase 1 completeness.

## Extraction Scope

The 2026-05-06 pass extracts the full body of the 6-page paper:

- §1 introduction: prior-art context for Mg⁺ light sources (dye lasers, Yb-fiber, frequency-quadrupled diode laser systems, OPO systems); VECSEL architecture motivation.
- §2 laser setup: two distinct VECSEL designs.
  - **IC system (externally-quadrupled VECSEL):** I-cavity geometry, GaInAs / GaAs gain mirror with GaAsP strain compensation, 200 mm RoC OC, 125 mm cavity, 807 nm fiber-coupled pump diode, water-cooled micro-channel cooler. 3.0 ± 0.1 W IR at 1117 nm at 21 ± 1 W of pump power (slope efficiency 19 ± 1 %). Frequency-doubled in commercial fiber-coupled QPM lithium niobate waveguide doubler (operated below 300 mW SH to avoid waveguide damage) → 22 ± 2 % conversion to 559 nm including fiber coupling losses → 260 ± 10 mW @ 559 nm. SH light coupled into BBO buildup cavity → 280 nm at 23 ± 2 mW (visible-to-UV conversion 9 ± 1 %).
  - **VC system (intracavity-doubled VECSEL):** V-cavity geometry, gain mirror + 100 mm RoC fold mirror + plane end mirror. Temperature-stabilised LBO 3 × 3 × 15 mm with dual AR coatings at 1141 and 571 nm in 65 mm short arm of cavity. 1.2 ± 0.1 W per 571 nm output beam (two equal beams from fold and end mirrors) at 8 °C gain mirror temperature. 571 nm doubled in BBO buildup cavity to 285 nm.
- §2 frequency-stability / linewidth: three-cornered hat measurement showing IC VECSEL frequency deviation <20 kHz over all averaging times, comparable to fiber laser and external-cavity diode laser. Linewidth of VC system 50 ± 10 kHz from electronic Hänsch-Couillaud error signal.
- §3 ion-trapping and spectroscopy: 285 nm photoionization at ~1 mW, 26 µm 1/e² intensity diameter, fiber-coupled. 280 nm Doppler cooling on 2S₁/₂ ↔ 2P₃/₂. Single 25Mg⁺ loaded within 10 s. Resolved sideband cooling: ⟨n⟩ = 0.008 +0.013/-0.008. Rabi frequency 191.1 ± 0.1 kHz, 1/e decay 77 ± 3 µs.
- §4 conclusion: future work targets 1118 → 559 nm doubling stage with higher optical damage threshold (LiNbO3 waveguide is the bottleneck for power scaling, NOT the BBO 280 nm stage).

## Extraction Passes

- **2026-05-06 (assistant under steward direction, DRAFT).** Initial full-body extraction. Status promoted from `SCAFFOLD` to `DRAFT`.

## Review Notes

- **The bottleneck is NOT BBO.** §4 conclusion explicitly states that the limit on power scaling is the LiNbO₃ waveguide doubler at the 1118 → 559 nm stage, not the BBO 280 nm stage. The waveguide is operated below 300 mW SH to avoid damage. This is a useful boundary-condition observation: in the Burd2016 architecture, the 280 nm stage is *not* the binding component for power scaling, contrary to the Friedenauer-class assumption.
- **280 nm RIN < -75 dBc/Hz above 10 kHz.** Useful comparison datum to Friedenauer 2006's < -130 dB/Hz at 2-10 MHz frequency range and 2 % mean fluctuations. Burd2016 RIN is *worse* than Friedenauer at high frequencies but they don't measure at the same frequency band, so the comparison is incomplete.
- **VECSEL architecture is alternative to Yb-fiber pump.** The two systems (IC at 1117 nm IR, VC at 1141 nm IR) overlap but are distinct from the Yb-fiber 1118 nm or 1064 nm sources commonly used. The wavelength tunability of VECSELs (over tens of nm by gain-mirror design) is the architectural advantage.
- **No long-term operational lifetime data.** Same gap as Hemmerling2011 and Kjaergaard2000 — architecture documented but maintenance schedule absent.
- **No BBO crystal vendor / dimensions / cut.** §2 says "BBO crystal for frequency doubling to 280 nm. Details of the cavity design are given by Wilson et al. [26]." The detailed BBO specification is in the cited Wilson et al. SPIE 9349 paper, not retrieved. Open extraction item.
- **Direct architectural comparison to Friedenauer-class.** Same 559 → 280 nm BBO buildup-cavity stage (or 571 → 285 nm in the VC system); same Hänsch-Couillaud locking; same overall architecture-family. The novelty is the VECSEL pump.
- **285 nm photoionization at 1 mW vs Kjaergaard2000's 2 mW.** Burd2016 uses ~half the photoionization power. Both are well below any UV surface-damage threshold.

## Downstream Dossier Links

- `KD-UV280-001`: single-source quadrupling demonstrated. Burd2016 contributes a 2016 demonstration of CW 280 nm at 23 mW (IC system) and 285 nm (VC system) via BBO buildup cavities, with VECSEL pumping. The 23 mW UV output is below the Friedenauer 275 mW baseline and the Hemmerling 60 mW point, but with the architectural advantage of VECSEL-based wavelength tunability.
- `KD-UV280-005`: BBO at 280 nm. Burd2016 contributes a qualitative datapoint that BBO buildup cavities operate routinely at 23 mW UV output without observable issues. No numerical contribution to LIDT or operational-lifetime questions.
- `KD-UV280-010`: 14-GHz unlockable domain. No mention of this anomaly. The Burd2016 IC system uses 1117 nm IR (vs Friedenauer's 1118 nm) and the VC system uses 1141 nm IR — both outside the Friedenauer 1118.339-1118.409 nm unlockable window.
- `KD-UV280-015`: VECSEL pump option. Burd2016 is the **primary [P]-tier source** for this entry. Two distinct VECSEL architectures (IC and VC) demonstrated; output powers and slope efficiencies measured; frequency-stability characterised by three-cornered hat.
