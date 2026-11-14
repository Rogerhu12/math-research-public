# Independent audit: protected160 mode3 linear port

Reviewer: Astra independent_audit, 2026-11-09. No construction code was modified. This is an independent reconstruction and linear propagation of the new fixed background, not a nonlinear or infinite-tail certificate.

Targets:

- `notes/root_cut_tail_cap002_p160_config.json`.
- `notes/root_cut_tail_cap002_p160_m3_s1024_far48.json`.
- `scripts/root_cut_tail_general_linear.mjs`, SHA256 `0ca6574d7590cf7797b7c090d5de5f00c5a372878dc72a8edd3b39812deecc4c`.
- The unchanged cap/warp constructor, SHA256 `c76f81a14c71ca6ca360c774b0b6e65c4082ada29519620949eb6ef436f3c8e1`.

## Verdict

**The new mode3 cut DN and its approximately4.06e-5 linear positivity threshold are independently confirmed.** The general script correctly substitutes the requested integer frequencies; its physical-height equation, orientation conversion, and outer normalization remain algebraically correct.

**The original far48 total log height gains are not accurate enough to use as growth factors.** The physical (f,f_r) representation loses small momentum when the two derivative terms nearly cancel in deep high-slope portions. A normalized projective direction can still converge correctly at the shallow cut after such growth errors. The agreement of the DN must not be read as an audit of those total gains.

## Independent reconstruction and results

The raw source coefficients for all160 protected cells were frozen in `notes/2026-11-09-audit-cut-tail-p160-input.json.gz`. `scripts/audit_cut_tail.py` reconstructs the cap and radial warp independently using SciPy quadrature. `scripts/audit_cut_tail_momentum.py` then propagates the independently derived nonsubtractive (V,pi) equations from `2026-11-09-audit-cut-tail.md`. No author warp evaluator or linear RK propagator is called in this Python calculation.

The source parameters including calibrationSteps512 remain fixed. ProtectCell160 is a new geometry relative to the earlier80 table, even though several shallow summary values agree to floating-point precision.

At far48, DOP853 relative tolerance2e-13 gives:

| Mode | Author RK1024 cut DN | Independent momentum cut DN |
| --- | ---: | ---: |
| 3 | 10.54376076408714 | 10.543760771206284 |
| 6 | 25.54951530789281 | 25.549515349754337 |
| 9 | 40.12563234042285 | 40.12563244375828 |
| 12 | 54.31448367384821 | 54.31448386342129 |

For mode3, numerical optimization of the independent dense solution gives threshold

$$A_{\rm lin}\approx4.060733961038424\cdot10^{-5}.$$

The minimum lies near cell0, segment3, x=.99342351185, with r=.45892707792, w=.00032086531862, f=-.01006484021, f_r=7.70427702836. The background angular Hessian is about.00014725376792, while the linear coefficient is3.62628454198. The author's finer uniform-grid value4.06073517086e-5 is consistent with this optimized estimate. The Python audit's own uniform512 sampling gives a slightly larger value4.06074274444e-5, illustrating why sampled minima are upper estimates of the true infimum, not globally certified sufficient bounds.

The same frozen background was propagated with far32 and far64 at relative tolerance2e-12:

| Far index | m3 cut DN | Optimized threshold estimate |
| --- | ---: | ---: |
| 32 | 10.543760771217059 | 4.060733960926555e-5 |
| 48 | 10.543760771206284 | 4.060733961038424e-5 |
| 64 | 10.543760771217059 | 4.0607339609258324e-5 |

The far48 row uses the tighter tolerance. Their agreement confirms stability of this shallow linear diagnostic under the tested truncations. It does not establish the finite far condition as an exact nonlinear round-collar condition.

## Growth-factor discrepancy

For the same far48 initial physical height normalized to one, the log height gains differ as follows:

| Mode | Author physical-coordinate RK1024 | Independent momentum DOP853 |
| --- | ---: | ---: |
| 3 | 634.9704859818719 | 655.9121564849083 |
| 6 | 767.4032364718852 | 788.7315986255892 |
| 9 | 860.9928854306384 | 879.979667340441 |
| 12 | 942.5617554787913 | 942.4713794948782 |

The mode3 difference is about20.94 in a natural logarithm, so it is substantial. The momentum formula includes the same initial ideal graph and the exact per-cell rescaling pi_new=(mu_old/mu_new)*pi_old; its reconstructed initial physical height is one. It is not comparing a differently normalized mode.

The direct state has to retain f_r-m²f/r after passage through cells where its size falls below the roundoff scale of the individual terms. Renormalizing the two large components does not restore that lost information. The independently derived momentum system evolves the small quantity itself. The reliable evidence here is the stable shallow DN and Hessian coefficient; deep growth estimates need this better-conditioned state and their own refinement.

## Artifacts and remaining scope

- `notes/2026-11-09-audit-cut-tail-p160-m3.json`: four-mode refined independent calculation.
- `notes/2026-11-09-audit-cut-tail-p160-m3-farcheck.json`: mode3 far32/64 comparison.
- `notes/2026-11-09-audit-cut-tail-p160-input.json.gz`: frozen raw coefficients and comparison samples.

For example, the main rerun is:

```text
python scripts/audit_cut_tail_momentum.py notes/2026-11-09-audit-cut-tail-p160-input.json.gz \
  --out notes/REVIEW_OUTPUT.json --far 48 --modes 3 6 9 12 --rtol 2e-13
```

Run paths relative to the topic directory. These scripts require NumPy and SciPy and consume the frozen input directly.

This audit does not prove a uniform exact alpha_n bracket for the unchanged source, a full deep-source curvature bound, a nonlinear stable tail at a visible amplitude, a Cartesian seam, or global reach. The new source must continue to be treated as one separately frozen candidate in subsequent frequency, radial, and phase checks.
