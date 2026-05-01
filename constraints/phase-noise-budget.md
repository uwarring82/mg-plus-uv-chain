# Phase noise budget — `constraints/phase-noise-budget.md`

**CHARTER §1.5 Level 0/1 boundary** — phase-noise constraints for Raman coherent control.

**Status:** Phase 0.5 deliverable. **DRAFT — NOT LOCKED.** This document quantifies the relative phase-noise spectral density $S_\varphi(f)$ between the two Raman beams and the absolute UV-source linewidth bound. All numeric envelopes are draft estimates for Steward review.

---

## 1. Relative phase-noise spectral density $S_\varphi(f)$ — Level 0

### 1.1 Gate-error coupling

For a Raman $\pi$-pulse of duration $\tau_{\text{gate}} = \pi / \Omega_R$, phase noise at Fourier frequencies $f \sim 1/\tau_{\text{gate}}$ contributes to gate infidelity. In the white-noise approximation ($S_\varphi(f) = S_0$ constant across the gate bandwidth):

$$\varepsilon_\varphi = \frac{1}{2} S_0 \, \Omega_R$$

*(Here $\Omega_R$ is the two-photon Rabi frequency in rad s⁻¹.)*

Requiring $\varepsilon_\varphi < 10^{-4}$ (i.e. phase noise contributes $<0.01$ % infidelity, leaving headroom for scattering, addressing error, etc.):

$$S_0^{\max} = \frac{2 \times 10^{-4}}{\Omega_R}$$

### 1.2 Scenario-specific $S_\varphi$ envelopes (draft)

| Scenario | $\Omega_R / 2\pi$ | $\tau_{\text{gate}}$ | $S_0^{\max}$ (rad²/Hz) | $S_\varphi^{\max}$ (dBc/Hz) | Gate-relevant band |
|---|---|---|---|---|---|
| Conservative | 100 kHz | 5.0 μs | $3.2 \times 10^{-10}$ | −95 | 100 kHz – 1 MHz |
| Nominal | 400 kHz | 1.25 μs | $8.0 \times 10^{-11}$ | −101 | 400 kHz – 4 MHz |
| Aggressive | 1 MHz | 0.50 μs | $3.2 \times 10^{-11}$ | −105 | 1 MHz – 10 MHz |

*Table 1 — Draft relative phase-noise envelopes. The white-noise approximation is a simplification; the true requirement is a frequency-dependent envelope $S_\varphi(f)$ that integrates to the same infidelity budget. The “gate-relevant band” is the frequency range where noise couples most strongly to the gate.*

### 1.3 Frequency-dependent envelope shape (draft)

Rather than a flat $S_0$, the practical budget is often specified as:

- **1/f region ($f \lesssim 100$ kHz):** $S_\varphi(f) \propto 1/f$ from laser frequency noise, acoustic perturbations, and thermal drift. The integrated contribution over a servo-loop bandwidth must be bounded.
- **Flat region ($100\,\text{kHz} \lesssim f \lesssim 10$ MHz):** dominated by electronic noise in AOM drivers, detector shot noise in any feedback loops, and photon-shot-noise contributions in the beam path.
- **High-frequency roll-off ($f \gtrsim 10$ MHz):** beyond the servo bandwidth of any phase-lock; noise here is suppressed by the finite response time of the ion (the gate acts as a low-pass filter).

**Draft envelope (Nominal scenario):**

| Frequency band | $S_\varphi(f)$ (dBc/Hz) | Comment |
|---|---|---|
| 10 Hz – 1 kHz | −60 (1/f slope from −30 dBc/Hz @ 1 Hz) | Acoustic / thermal; common-mode rejected in single-source architecture. |
| 1 kHz – 100 kHz | −80 | Residual fibre-noise servo errors, AOM thermal drift. |
| 100 kHz – 4 MHz | −101 | **Gate-critical band.** Flat white-noise floor target. |
| 4 MHz – 100 MHz | −90 | Electronic noise floor; relaxed because gate is insensitive. |

*Table 2 — Draft frequency-dependent envelope (Nominal). The Conservative envelope relaxes the gate-critical band to −95 dBc/Hz; the Aggressive envelope tightens it to −105 dBc/Hz.*

---

## 2. Absolute UV-source linewidth bound — Level 1

### 2.1 Detection / cooling requirement (v0.8 external-Verifier addition)

For detection and Doppler cooling, the source linewidth $\Delta \nu_{\text{source}}$ must be comfortably below the natural transition linewidth of ²⁵Mg⁺ ($\Gamma / 2\pi \approx 41$ MHz) to avoid power broadening and to preserve fluorescence SNR.

**Draft bound:** $\Delta \nu_{\text{source}} \le 1$ MHz at 280 nm.

*Rationale:* A 1 MHz linewidth is ~40× narrower than the natural linewidth. It ensures that > 99 % of the source power falls within the atomic absorption profile and that frequency noise does not appreciably modulate the scattering rate during detection pulses (typically 100 μs–1 ms).

### 2.2 Raman-mode implication

In the Raman mode, common-mode rejection between the two beams cancels the *correlated* part of the absolute phase noise. However:

- The cancellation bandwidth is limited by the differential path length after the beam split. Path-length fluctuations faster than the cancellation bandwidth appear as relative phase noise.
- The absolute linewidth determines the stability of the Raman resonance condition against long-term drift (e.g. over an 8-hour operation).
- If the two beams experience different optical elements (e.g. separate AOMs), the uncorrelated phase noise of those elements adds in quadrature to the relative-noise budget.

Therefore the absolute linewidth bound is not redundant with the relative $S_\varphi(f)$ envelope; it is a distinct Level 1 constraint that protects the low-frequency stability of the Raman resonance.

### 2.3 Scenario linewidth bounds (draft)

| Scenario | $\Delta \nu_{\text{source}}$ (kHz) | Comment |
|---|---|---|
| Conservative | ≤ 100 | Fibre-laser or VECSEL with active frequency stabilisation; comfortable margin for detection SNR. |
| Nominal | ≤ 500 | Moderate stabilisation; acceptable for detection and for Raman common-mode rejection with careful path-length matching. |
| Aggressive | ≤ 1 000 | Upper bound from v0.8 indicative value; tight but achievable with commercial narrow-linewidth fibre sources. |

*Table 3 — Draft absolute linewidth bounds. These are source-side specifications at 280 nm. Note that quadrupling multiplies the infrared linewidth by 4; an IR source with 250 kHz linewidth produces ~1 MHz UV linewidth.*

---

## 3. Common-mode rejection — architecture-class characterisation

This document does **not** select an architecture. It specifies the phase-noise envelope that each candidate must demonstrate it can meet, for Phase 4 axis 2 (“Phase coherence”) scoring.

### 3.1 Single-source / quadrupling (family 1)

- **Intrinsic rejection:** Both Raman beams are derived from the same 280 nm output by downstream AOM or beam-splitter. The source phase noise is 100 % correlated before the split and cancels in the heterodyne (Raman) combination to first order.
- **Residual differential noise:** After the split, the two beams traverse different paths (AOMs, fibres, free-space steering). Differential path-length fluctuations $\delta L$ convert source frequency noise $\delta \nu$ to relative phase noise via $S_\varphi = (2\pi \delta \nu / c)^2 S_{\delta L}$.
- **Rejection bandwidth:** Set by the mechanical / thermal stability of the differential path. With passive isolation (foam, enclosures), rejection bandwidths of ~100 Hz–1 kHz are typical; with active stabilisation (e.g. fibre-noise cancellation), bandwidths of ~100 kHz are achievable.
- **Draft requirement for family 1:** Differential path length must be stabilised such that the uncancelled relative phase noise meets Table 1/Table 2 in the gate-critical band. For the Nominal scenario, this implies differential path-length stability $< 10$ nm over 1 ms (draft).

### 3.2 Dual-source / SFG / hybrid (families 2 and 3)

- **No intrinsic rejection:** The two Raman beams originate from independent optical paths (e.g. two IR sources mixed in SFG, or one doubled and one mixed). Their phase noises are uncorrelated before any active lock.
- **Engineered rejection:** A phase-lock loop (PLL) or optical phase-locked loop (OPLL) can force one source to track the other. Modern fibre-laser OPLLs achieve:
  - Loop bandwidth: ~100 kHz – 1 MHz
  - Residual phase noise: −100 to −120 dBc/Hz in-band
  - Relative linewidth: sub-Hz to mHz
- **Robustness:** The lock must hold under thermal transients, acoustic perturbation, and long-term drift. Loss of lock during a gate is a catastrophic failure mode.
- **Draft requirement for families 2/3:** Demonstrated OPLL residual phase noise $< -100$ dBc/Hz in the gate-critical band, with mean-time-between-lock-loss > 10× the longest experimental sequence (draft: > 1 hour).

### 3.3 Direct deep-UV (family 4)

- Not an active candidate at v1.0 (literature-only per CHARTER §4). If elevated to candidate in Phase 4, the phase-noise requirement is the same as for families 1–3: meet Table 1/Table 2.

### 3.4 Scoring implication for Phase 4

Phase 4 axis 2 (“Phase coherence”) must score each family on:

1. **Achievable $S_\varphi(f)$** in the gate-critical band (evidence: measurement or vendor spec).
2. **Robustness** under thermal and mechanical drift (evidence: stability measurement over > 1 hour).
3. **Complexity** of the rejection scheme (intrinsic vs. engineered; component count; alignment sensitivity).

The “engineerable phase coherence vs. non-engineerable UV degradation” tension (CHARTER §4) maps onto axes 2 and 3 explicitly: family 1 scores well on axis 2 intrinsically but may score poorly on axis 3 if UV degradation is severe; families 2/3 score well on axis 3 if crystal choices reduce UV stress but require engineered phase coherence that adds complexity and failure modes.

---

## 4. Coherence time requirements

| Operation | Duration (typical) | Required coherence time | Linewidth implication |
|---|---|---|---|
| Detection | 100 μs – 1 ms | ≥ 10 ms | $\Delta \nu \ll 100$ Hz over detection window; trivially satisfied by any source ≤ 1 MHz. |
| Doppler cooling | 1 – 10 ms | ≥ 100 ms | $\Delta \nu \ll 10$ Hz over cooling pulse; still satisfied by ≤ 1 MHz source. |
| Raman gate (π-pulse) | 0.5 – 5 μs | ≥ 50 μs | Relative phase stable to $< 10^{-2}$ rad over gate; drives the $S_\varphi(f)$ envelope in Table 1. |
| Raman gate sequence | 10 – 100 μs | ≥ 1 ms | Cumulative phase drift over multi-pulse sequence; drives low-frequency $S_\varphi(f)$. |

*Table 4 — Coherence time requirements. The binding constraint is the Raman gate sequence, which demands both low high-frequency noise (Table 1 gate-critical band) and low low-frequency drift (Table 2 10 Hz–1 kHz band).*

---

## 5. Reference values and bounded-scenario set

### 5.1 Reference values (proposed, draft)

Using the **Nominal** scenario as the Phase 4 reference triple anchor:

| Parameter | Value |
|---|---|
| $S_\varphi(f)$ envelope (gate-critical band) | −101 dBc/Hz (100 kHz – 4 MHz) |
| Absolute UV linewidth $\Delta \nu_{\text{source}}$ | ≤ 500 kHz |
| Differential path-length stability (family 1) | $< 10$ nm over 1 ms |
| OPLL residual noise (families 2/3) | $< -100$ dBc/Hz |

### 5.2 Bounded-scenario fallback

If precise envelopes cannot be locked, the Conservative scenario relaxes the requirements and the Aggressive scenario tightens them. Phase 4 scoring must run at minimum on the Conservative envelope:

| Scenario | $S_\varphi$ (gate-critical) | $\Delta \nu_{\text{source}}$ |
|---|---|---|
| Conservative | −95 dBc/Hz | ≤ 100 kHz |
| Nominal | −101 dBc/Hz | ≤ 500 kHz |
| Aggressive | −105 dBc/Hz | ≤ 1 MHz |

*Note: The Aggressive scenario allows a wider absolute linewidth because the shorter gate time (0.5 μs) is less sensitive to low-frequency drift, and the higher Ω_R demands tighter high-frequency noise but not tighter low-frequency stability.*

---

## 6. Locking protocol

**This document is NOT locked.**

Before G3 closure, the following must occur:

1. Steward review of the $S_\varphi(f)$ envelopes against the institutional trap record (existing Raman gate fidelities, measured phase-noise spectra).
2. Verification of the white-noise-to-infidelity formula (§1.1) against the actual multi-pulse gate sequences used in the group.
3. Confirmation of the absolute linewidth bound against detection/cooling SNR requirements.
4. Measurement or vendor certification of the existing source’s phase-noise spectrum and linewidth (Phase 2 baseline).
5. Population of `src/parameters.py` with the agreed phase-noise envelope (or explicit reference to this document if the envelope is frequency-dependent).

After locking, this document becomes subject to CHARTER §9 asymmetric erosion protection.

---

## 7. Open items / literature anchors needed

- [ ] **Infidelity formula:** The white-noise approximation $ \varepsilon_\varphi = S_0 \Omega_R / 2 $ is a simplification. Verify against the exact filter function for the specific pulse sequences (e.g. Walsh-modulated, BB1 composite) used in the trap.
- [ ] **1/f noise contribution:** The integrated phase noise from the 10 Hz–1 kHz band may dominate over the flat high-frequency floor. Compute the integral for the existing source and verify the envelope shape.
- [ ] **AOM phase noise:** Acousto-optic modulators contribute phase noise (thermal drift of the Bragg cell, RF driver noise). Quantify for the specific AOM model used.
- [ ] **Fibre-noise cancellation:** If family 1 uses fibre delivery after the split, the fibre-noise cancellation servo bandwidth and residual noise must be measured.
- [ ] **Dual-source OPLL evidence:** For families 2/3, collect literature evidence of demonstrated OPLL performance at comparable wavelengths and power levels.

---

## References

- CHARTER §1.5 Level 0 and Level 1, §4 architecture families, §5.2 Phase 4 axis 2, §6.4 Raman validation, §9 erosion protection.
- `raman-requirements.md` — gate durations and Ω_R targets (Level 0 input).
- `loss-budget.md` — beam-path differential-length stability (couples to common-mode rejection).
- Phase 1 literature dossier (to be created): laser linewidth specifications, OPLL performance, fibre-noise cancellation.

---

*Document version: DRAFT 0.1 — 2026-05-01. Not for locking.*
