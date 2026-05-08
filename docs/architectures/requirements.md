---
layout: default
title: Architecture requirements specification
description: Shared requirements table for the three architecture candidates (next-gen CW Friedenauer-topology, IC-VECSEL alternative, pulsed-Raman alternative). Per-requirement entries cover task served, measurement plane, wavelength / detuning, output / pulse energy, duration, environment, beam quality, linewidth / phase noise, degradation allowance, and evidence artefact.
---

<p class="endorsement"><strong>Endorsement Marker.</strong> Local candidate framework — AG Schätz stewardship. This page captures requirements at the spec level; numerical values that are still TBD are marked as such and the binding form remains the CHARTER §1.5 Level 0 row coupled through the loss budget. None of the entries here is a build commitment, and several depend on Council-3 deliberations that have not yet happened.</p>

<p class="eyebrow">Architectures · requirements</p>

# Architecture requirements specification

**Purpose.** This page is the shared requirements artefact for the [architecture slate](index.html). Each requirement carries a stable ID (`REQ-NG-###` for the [next-gen CW workplan](next-gen.html), `REQ-IC-###` for the [IC-VECSEL alternative](ic-vecsel-alternative.html), `REQ-PR-###` for the [pulsed-Raman alternative](pulsed-raman-alternative.html)). Entries are uniform: task served · measurement plane · wavelength / detuning · output power or pulse energy · duration · environment · beam quality · linewidth / phase noise · degradation allowance · evidence artefact.

**What this page is not.** Not a build commitment, not a Phase 4 scoring output, not a closed numerical spec. Several entries below are **TBD** — they identify *what* must be specified before Phase 4 acceptance, not the specific numerical values. Each TBD is the spec to be measured; the requirement is that a binding number lands here before promotion.

**Charter compliance.** The reference triple `{Δ_ref = 40 GHz, Ω_R/2π = 400 kHz, Γ_sc = 2.0 × 10⁴ s⁻¹}` (locked at G3 closure 2026-05-01) is unaffected. Two requirements below are **conditional** on Council-3 deliberations that have not yet happened: `REQ-IC-002` is valid only as a paired task allocation with the pulsed-Raman alternative (or an off-board Raman pathway); the entire `REQ-PR-###` block sits across CHARTER §3 line 105 (pulsed UV out of scope) and is forward-looking only until that scope question is resolved.

---

## Summary table

| ID | Architecture | Task served | Plane | λ / Δ | Power / energy | Status |
|---|---|---|---|---|---|---|
| `REQ-NG-001` | Next-gen CW | All UV tasks | Rack output | ~ 280 nm CW, Δ_ref = 40 GHz | ≥ 0.50 W CW for ≥ 8 h | ⏳ NG-F |
| `REQ-NG-002` | Next-gen CW | NG-A validation gate | Phase E notebook | — | LBO residual ≤ 5 % | ⏳ NG-A blocking |
| `REQ-NG-003` | Next-gen CW | Source noise envelope | Rack output | 280 nm CW | Linewidth, RIN, drift TBD | ⏳ open |
| `REQ-NG-004` | Next-gen CW | Beam-quality envelope | Rack output | 280 nm CW | M², profile TBD (target M² ≤ 1.2) | ⏳ open |
| `REQ-NG-005` | Next-gen CW | UV-degradation allowance | BBO output, rack-integrated | 280 nm CW | TBD (G2-dependent) | ⏳ G2-blocked |
| `REQ-IC-001` | IC-VECSEL | Visible at BBO input | BBO ring input | 559 nm CW | ≥ 0.50 W baseline | ⏳ open scaling question |
| `REQ-IC-002` | IC-VECSEL | UV at rack output (cooling + repumping) | Rack output | ~ 280 nm CW, Δ_ref = 40 GHz | ≥ 50 mW for ≥ 8 h | ⏳ Paired-architecture conditional |
| `REQ-IC-003` | IC-VECSEL | BBO efficiency escape clause | BBO ring | 559 → 280 nm | Visible-to-UV ≥ 20 % measured ⇒ relaxes `REQ-IC-001` to 170–250 mW | ⏳ open |
| `REQ-IC-004` | IC-VECSEL | Thermal isolation | Inside IC-VECSEL cavity | — | LBO oven 150 °C vs gain-mirror Peltier ~ 20 °C, full spec TBD | ⏳ open |
| `REQ-PR-001` | Pulsed-Raman | Central wavelength and detuning | Ion plane | ~ 290–320 nm; Δ from D₁/D₂ TBD (~ tens of nm red) | — | ⏳ Charter §3 conditional |
| `REQ-PR-002` | Pulsed-Raman | Spectral FWHM | Ion plane | ~ 3 THz transform-limited at 100 fs | — | ⏳ Charter §3 conditional |
| `REQ-PR-003` | Pulsed-Raman | Pulse duration at ion | Ion plane | — | ≤ 100 fs after dispersion comp.; full spec TBD | ⏳ Charter §3 conditional |
| `REQ-PR-004` | Pulsed-Raman | Pulse energy + peak-fluence safety | Ion plane / BBO output | — | Pulse energy per beam, peak-fluence safety factor TBD | ⏳ Charter §3 conditional |
| `REQ-PR-005` | Pulsed-Raman | Beam waist at ion | Ion plane | — | TBD | ⏳ Charter §3 conditional |
| `REQ-PR-006` | Pulsed-Raman | f_rep / f₀ lock residuals | Lock-loop output | — | RMS lock residuals TBD | ⏳ Charter §3 conditional |
| `REQ-PR-007` | Pulsed-Raman | Timing-jitter spectrum | Pulse train | — | S_t(f) bound TBD | ⏳ Charter §3 conditional |
| `REQ-PR-008` | Pulsed-Raman | Per-gate Ω_R and Γ_sc | Ion-frame rate equations | — | Ω_R per gate, Γ_sc per gate TBD (from multi-level model) | ⏳ Charter §3 conditional |
| `REQ-PR-009` | Pulsed-Raman | Multi-level ²⁵Mg⁺ model — gate-level acceptance | Notebook | — | Required before Phase 4 acceptance | ⏳ Charter §3 conditional |

Status legend: ⏳ open · ✅ closed · ⛔ blocked.

---

## Next-gen CW (Friedenauer-topology, ≥ 500 mW)

### `REQ-NG-001` · UV output power and sustained operation

- **Task served.** All UV tasks at the locked Δ_ref operating point: Doppler cooling, repumping, photoionisation, coherent Raman.
- **Measurement plane.** Rack output (after final BBO output coupler, before downstream AOMs).
- **Wavelength / detuning.** ~ 280 nm CW; Δ_ref = 40 GHz from ³P₃/₂.
- **Output power / energy.** ≥ 0.50 W CW.
- **Duration.** Sustained ≥ 8 h continuous operation (warm-up time excluded; warm-up profile to be reported separately under `REQ-NG-003`).
- **Environment.** TEC-stabilised lab; rack-internal humidity / particulate spec **TBD**.
- **Beam quality.** Specified by `REQ-NG-004`.
- **Linewidth / phase noise.** Specified by `REQ-NG-003`.
- **Degradation allowance.** Specified by `REQ-NG-005`.
- **Evidence artefact.** Phase NG-F synthesis notebook + downstream rack-output measurement campaign in Phase 5.

### `REQ-NG-002` · LBO passive-loss residual ≤ 5 % (NG-A validation gate)

- **Task served.** Validation prerequisite to any 500 mW recommendation derived from the LBO sweep.
- **Measurement plane.** Phase E [Friedenauer cascade-recompute notebook](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/notebooks/diagnostic/2026-05-07-friedenauer-cascade-recompute.py) re-run with corrected `L_passive` separated from `T_IC_at_match`.
- **Wavelength / detuning.** N/A (validation gate).
- **Output / energy.** N/A — the requirement is residual: published Friedenauer LBO output 0.950 W vs computed must agree to **≤ 5 %**.
- **Duration.** N/A.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Updated [`Friedenauer2006/extracted.yaml`](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/data/literature/Friedenauer2006/) entry separating `T_IC_at_match` from `L_passive_inferred`; Phase E notebook residual updated to ≤ 5 %; short logbook entry recording the inference. **Until this lands, no `REQ-NG-001`-derived recommendation from a swept LBO parameter set is admissible.**

### `REQ-NG-003` · Source noise envelope at rack output

- **Task served.** All UV tasks; bounds the SHG-cavity-locking-bandwidth-to-amplitude-noise transfer.
- **Measurement plane.** Rack output.
- **Wavelength / detuning.** 280 nm CW.
- **Output / energy.** N/A — this is a noise spec, not a power spec.
- **Duration.** Reported across short (≤ 1 s), medium (1–100 s), and long (> 100 s) timescales.
- **Environment.** Same as `REQ-NG-001`.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** Linewidth at rack output **TBD**, target informed by [Span25] (101(8) kHz wavemeter-locked at the IR seed) and the SHG-cavity locking bandwidth (~ 18 kHz loaded piezo per [Frie06]). RIN spectrum at rack output **TBD**, target ≤ −130 dB/Hz at 2–10 MHz per [Frie06] envelope.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Phase 2 baseline-measurement campaign on the in-house chain.

### `REQ-NG-004` · Beam-quality envelope at rack output

- **Task served.** Bounds AOM-coupling efficiency and fibre-coupling losses to downstream beam paths.
- **Measurement plane.** Rack output.
- **Wavelength / detuning.** 280 nm CW.
- **Output / energy.** N/A.
- **Duration.** N/A.
- **Environment.** N/A.
- **Beam quality.** **Target M² ≤ 1.2** at rack output; spatial-profile spec **TBD**.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Phase NG-D crystal-geometry sweep + Phase 2 baseline measurement.

### `REQ-NG-005` · UV-degradation allowance (G2-blocked)

- **Task served.** Bounds BBO-output-stage operational lifetime against UV-induced surface degradation.
- **Measurement plane.** BBO output coupler + rack-integrated long-term operation.
- **Wavelength / detuning.** 280 nm CW.
- **Output / energy.** Operates at `REQ-NG-001` level.
- **Duration.** Long-term: power-loss budget over 1 month / 6 month / 1 year **TBD**.
- **Environment.** Lab air baseline; cleanliness / inert-gas-purge upgrade is a candidate mitigation per [Burk21].
- **Beam quality.** Reported with `REQ-NG-004`.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** **TBD** — G2-dependent. The full numerical bound waits on the G2-closure measurement campaign.
- **Evidence artefact.** G2-closure measurement campaign (currently unblocked, not yet started); compares against [Brow19] / [Burk21] / [Turc22] envelope.

---

## IC-VECSEL alternative (cooling + repumping; paired with pulsed-Raman)

### `REQ-IC-001` · Visible at BBO input — 0.50 W baseline

- **Task served.** Drives the BBO ring at sufficient input to reach the cooling + repumping UV target after BBO conversion.
- **Measurement plane.** BBO ring input (after isolator + EOM, before BBO crystal).
- **Wavelength / detuning.** 559 nm CW.
- **Output power / energy.** **≥ 0.50 W CW baseline** (assumes BBO efficiency at the in-house operating point ~ 10 % per [Guth21]); relaxed to 170–250 mW under `REQ-IC-003` if a higher BBO efficiency is *demonstrated*.
- **Duration.** Sustained ≥ 8 h to support `REQ-IC-002`.
- **Environment.** Inside the sealed 19" rack envelope (vacuum or N₂ / Ar purge).
- **Beam quality.** TBD; constrained by intracavity LBO mode-matching to the gain-mirror waist.
- **Linewidth / phase noise.** Inherits IC-VECSEL seed linewidth (target ~ Burd23 class, ≤ 100 kHz).
- **Degradation allowance.** TBD.
- **Evidence artefact.** Notebook exploration of the IC-VECSEL output envelope at 1118 nm under the new `shg_intracavity.py` architecture-neutral primitive (open follow-up).

### `REQ-IC-002` · UV at rack output for cooling + repumping (paired-architecture conditional)

- **Task served.** Cooling + repumping only. **Coherent Raman is *not* covered by this chain** and must be supplied by a parallel pathway (the pulsed-Raman alternative or an equivalent off-board source).
- **Measurement plane.** Rack output (after BBO output coupler).
- **Wavelength / detuning.** ~ 280 nm CW; Δ_ref = 40 GHz.
- **Output power / energy.** **≥ 50 mW CW** for ≥ 8 h continuous.
- **Duration.** ≥ 8 h.
- **Environment.** Inside the sealed rack envelope.
- **Beam quality.** TBD; same envelope as `REQ-NG-004` target.
- **Linewidth / phase noise.** TBD; inherits IC-VECSEL seed linewidth.
- **Degradation allowance.** TBD; G2-dependent. Sealed-envelope mitigation reduces the surface-contamination LIDT pressure.
- **Evidence artefact.** Notebook exploration + Phase 5 measurement on a built IC-VECSEL.
- **Conditionality.** This requirement is **valid only as a paired task allocation** with [`REQ-PR-###`](#pulsed-raman-alternative-charter-3-out-of-scope-sub-project-status-required) (or an equivalent off-board Raman pathway). Without that pairing, the chain underdelivers Level 1 and is not admissible as a single-architecture candidate.

### `REQ-IC-003` · BBO efficiency escape clause

- **Task served.** Defines the conditions under which the `REQ-IC-001` visible target may be relaxed.
- **Measurement plane.** BBO ring conversion-efficiency measurement on the actual built BBO ring (with hard fluoride coatings per [Burk21] and any waist / crystal-length optimisation).
- **Wavelength / detuning.** 559 → 280 nm.
- **Output / energy.** Visible-to-UV conversion efficiency **≥ 20 % measured** (above the [Guth21] / [Frie06] ~ 7–10 % envelope) ⇒ `REQ-IC-001` baseline relaxes proportionally to 170–250 mW visible.
- **Duration.** Sustained operation matching `REQ-IC-002`.
- **Environment.** Inside the sealed rack envelope.
- **Beam quality.** Tracked through `REQ-IC-001` and `REQ-IC-002`.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** Tracked through `REQ-IC-002`.
- **Evidence artefact.** Direct measurement on the built BBO ring; until that measurement lands, the escape clause is **not** invoked and `REQ-IC-001` baseline ≥ 0.50 W visible holds.

### `REQ-IC-004` · Thermal isolation: 150 °C LBO oven vs gain-mirror Peltier

- **Task served.** Ensures the intracavity LBO oven (NCPM Type-I, ~ 150 °C) does not perturb the gain-mirror Peltier (~ 20 °C) and *vice versa* across the IC-VECSEL operating envelope.
- **Measurement plane.** Inside the IC-VECSEL cavity housing.
- **Wavelength / detuning.** N/A.
- **Output / energy.** N/A.
- **Duration.** Sustained operation matching `REQ-IC-002`.
- **Environment.** Inside the sealed rack envelope.
- **Beam quality.** N/A directly; indirectly affected via gain-mirror thermal stability.
- **Linewidth / phase noise.** Indirectly affected via gain-mirror temperature stability (cf. [Span25] 0.08 mK long-timescale TEC Allan deviation).
- **Degradation allowance.** TBD.
- **Evidence artefact.** Mechanical / thermal CAD with FEA simulation; long-term stability test on a built IC-VECSEL. **Specific thermal-coupling spec TBD**: target gain-mirror temperature drift < 1 mK with LBO oven at full power, against a baseline measurement with LBO oven cold.

---

## Pulsed-Raman alternative (CHARTER §3 out-of-scope; sub-project status required)

> ⚠️ **CHARTER §3 conflict — load-bearing.** `CHARTER.md` line 105 lists pulsed UV systems explicitly as out of scope (*"Pulsed UV systems (the stroboscopic / fs-comb discussion with Leibfried is a distinct project)"*). The `REQ-PR-###` block below is forward-looking only — it specifies *what would need to be specified* if and when one of (i) a Council-3 Charter exception that rewrites §3 or (ii) explicit "parallel Raman sub-project" status is granted. None of the entries below is binding until that scope question is resolved.

### `REQ-PR-001` · Central wavelength and detuning from D₁ / D₂

- **Task served.** Far-red-detuned coherent Raman.
- **Measurement plane.** Ion plane (after final UV beam shaping).
- **Wavelength / detuning.** Central wavelength **TBD** in ~ 290–320 nm range; detuning from ²⁵Mg⁺ ³P₁/₂ and ³P₃/₂ each specified separately, target Δ ~ tens of THz (orders of magnitude above Δ_ref).
- **Output / energy.** Tracked via `REQ-PR-004`.
- **Duration.** N/A directly; tracked via lock residuals (`REQ-PR-006`).
- **Environment.** Pulse train delivered via free-space beam path to the ion.
- **Beam quality.** Tracked via `REQ-PR-005`.
- **Linewidth / phase noise.** Tracked via `REQ-PR-002` (spectral FWHM) and `REQ-PR-007` (timing jitter).
- **Degradation allowance.** Tracked separately for the BBO single-pass tripler.
- **Evidence artefact.** Notebook computing the multi-level Ω_R / Γ_sc per `REQ-PR-008` against the candidate operating point.

### `REQ-PR-002` · Spectral FWHM at the ion plane

- **Task served.** Bounds the simultaneous addressing of D₁ and D₂ by the comb spectral envelope.
- **Measurement plane.** Ion plane.
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** N/A.
- **Duration.** N/A.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** Spectral FWHM **TBD** — transform-limited at 100 fs ≈ 3 THz, comparable to the ²⁵Mg⁺ fine-structure splitting; whether the spec calls for spectral filtering, dispersion management, or unfiltered simultaneous addressing depends on the multi-level model output of `REQ-PR-009`.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Multi-level pulse-train notebook (`REQ-PR-009`).

### `REQ-PR-003` · Pulse duration at ion plane

- **Task served.** Determines peak intensity at fixed pulse energy.
- **Measurement plane.** Ion plane (after dispersion management).
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** N/A.
- **Duration.** Pulse duration **≤ 100 fs** target (transform-limited or near); chirp / dispersion budget **TBD**.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** N/A directly.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Autocorrelator / FROG measurement at the ion plane.

### `REQ-PR-004` · Pulse energy per beam and peak-fluence safety factor

- **Task served.** Drives Ω_R per gate.
- **Measurement plane.** Ion plane (each Raman beam separately).
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** Pulse energy per beam **TBD** (set by `REQ-PR-008` Ω_R-per-gate target); peak-fluence safety factor against BBO LIDT **TBD**, target factor ≥ 5× below [Eime87] / [Turc22] / [Kuma15] envelope.
- **Duration.** Per-pulse.
- **Environment.** Pulse train environment **TBD**; sealed envelope candidate per the IC-VECSEL alternative.
- **Beam quality.** Tracked via `REQ-PR-005`.
- **Linewidth / phase noise.** N/A directly.
- **Degradation allowance.** Bounded by peak-fluence safety factor.
- **Evidence artefact.** Direct pulse-energy measurement; LIDT bench test on the BBO single-pass tripler.

### `REQ-PR-005` · Beam waist at ion plane

- **Task served.** Sets focal intensity at fixed pulse energy.
- **Measurement plane.** Ion plane.
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** N/A.
- **Duration.** N/A.
- **Environment.** N/A.
- **Beam quality.** Beam waist **TBD**; target consistent with two-photon Raman addressing at the trap site geometry.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Beam-profile measurement at the ion plane.

### `REQ-PR-006` · Repetition-rate / CEO lock residuals

- **Task served.** Bounds comb-tooth frequency stability.
- **Measurement plane.** Lock-loop output.
- **Wavelength / detuning.** N/A.
- **Output / energy.** N/A.
- **Duration.** Reported across short (≤ 1 s) and long (> 100 s) timescales.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** RMS f_rep lock residual **TBD**; RMS f₀ lock residual **TBD**; both with phase-noise spectra reported against the in-loop reference.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Phase-noise measurement against an independent stable reference (iodine-locked CW laser or H-maser-derived RF reference).

### `REQ-PR-007` · Timing-jitter spectrum

- **Task served.** Couples to motional-state phase via pulse-train arrival time.
- **Measurement plane.** Pulse train at the ion plane (or equivalent point along the beam path).
- **Wavelength / detuning.** N/A.
- **Output / energy.** N/A.
- **Duration.** N/A; reported as power spectral density.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** Timing-jitter PSD `S_t(f)` **TBD**; bound set by the maximum tolerable motional-mode dephasing per gate operation.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Timing-jitter measurement campaign + propagation through the multi-level model of `REQ-PR-009`.

### `REQ-PR-008` · Per-gate Ω_R and Γ_sc

- **Task served.** Direct Phase 4 axis-1 (Raman capability) and axis-2 (phase coherence) inputs.
- **Measurement plane.** Ion-frame rate equations driven by the multi-level model.
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** N/A; computed quantity.
- **Duration.** Per gate operation.
- **Environment.** N/A.
- **Beam quality.** Tracked via `REQ-PR-005`.
- **Linewidth / phase noise.** Tracked via `REQ-PR-002`, `REQ-PR-006`, `REQ-PR-007`.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Multi-level pulse-train notebook (`REQ-PR-009`); both Ω_R per gate and Γ_sc per gate values reported with sensitivity envelope.

### `REQ-PR-009` · Multi-level ²⁵Mg⁺ pulse-train model — gate-level acceptance prerequisite

- **Task served.** Phase 4 acceptance gate for the pulsed-Raman candidate.
- **Measurement plane.** Notebook (computational model).
- **Wavelength / detuning.** Tracked via `REQ-PR-001`.
- **Output / energy.** N/A.
- **Duration.** N/A.
- **Environment.** N/A.
- **Beam quality.** N/A.
- **Linewidth / phase noise.** N/A.
- **Degradation allowance.** N/A.
- **Evidence artefact.** Notebook implementing a multi-level ²⁵Mg⁺ model (³S₁/₂ × ³P₁/₂ × ³P₃/₂ at minimum) coupled to the comb spectral envelope (~ 3 THz), computing per-gate Ω_R and Γ_sc with both fine-structure components addressed simultaneously. **Validated against a Monroe-group Yb⁺ benchmark** (proposed extractions `[Haye10]` / `[Mizr13]` / `[Camp10]` / `[Inle14]`) before being applied to ²⁵Mg⁺. Until this notebook lands, the pulsed-Raman candidate is **below gate-level acceptance** and the scaling-argument prose alone does not constitute admissible Phase 4 input.

---

## See also

- [Architectures (catalog)](index.html) — the four-page architecture slate that this requirements page covers.
- [Next-gen workplan](next-gen.html) · [IC-VECSEL alternative](ic-vecsel-alternative.html) · [Pulsed-Raman alternative](pulsed-raman-alternative.html) · [Friedenauer 2006 baseline](friedenauer-2006.html).
- [Logbook entries](https://github.com/uwarring82/mg-plus-uv-chain/blob/main/logbook/) — full Charter §9 / Coastline / Sail / G1-G2-G3 statements per architecture.
- [References](../references.html) — alphabetical literature index.
