# Actual request28: the original first native correction has a huge computed linear defect

## Actual execution and scope

Public run `43611175099`, job `132496373274` (`Mainline nativecorrection`), used source `6bd52b446241be53e8842d4db5a24f9c2069e6e5`. The job completed successfully as a diagnostic capture. It issued one original native request, retained the original first full withJac evaluation and original correction, and executed zero nonlinear trials. It stopped at the declared `VISIBLE_NATIVE_CORRECTION_CAPTURE_COMPLETE_V1` point before the first trial.

The downloaded artifact is `14120548264`, `visible-mainline-nativecorrection-43611175099-1`, with 235,561,097 ZIP bytes and SHA256 `0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee`. The complete archive hash was checked. The original capture reports 1,176.036 seconds through its final diagnostic and the launcher reports 1,201.623083017 seconds overall. The original first withJac result had already returned at capture elapsed 1,117.609 seconds.

The actual output explicitly has `diagnostic_complete=true`, `planned_diagnostic_stop_observed=true`, `native_accepted=false`, `task_completed=false`, and no final endpoint J or audit. The original client surfaces the planned stop as a failed solve response; the wrapper's success means that the requested complete diagnostic was preserved, not that this response became a native solution.

The source and insertion-only observer contract are in [the capture interface](2026-11-14-native-correction-capture-interface.md). The original numerical core SHA remains `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`; launcher SHA is `0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0`, hook SHA is `b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30`.

## Same complete state and original baseline

The input is the complete actual23 candidate at the same actual17 nonzero height already used by actual25. Its 577-by-224 little-endian binary64 state identity remains

    6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8

including all 9,546 negative zeros. All 112 height components remain present. The original scales have SHA `ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`, and the original diagonal far graph has SHA `395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54`.

All 576 original withJac stage evaluations returned their original guards. The baseline values exactly repeat actual25's saved values:

| Original quantity | Saved value |
| --- | ---: |
| Original scaled residual norm | `0.04177307820740199` |
| Original minimum A guard | `0.9999999999759498` |
| Original minimum D guard | `0.9999999999999858` |
| Returned Riccati chart condition diagnostic | `8.810946110232247e59` |

Thus this capture has not changed the base problem or substituted a new height, graph, scale, target, zero solution or initializer. The baseline residual still exceeds the original native tolerance. No complete tail or closed surface has been accepted.

## Complete model and original-array audit

The manifest contains 29 complete arrays in 116 chunks, totaling 238,972,680 raw bytes. The read-only audit verified all chunk file hashes, concatenated full-array hashes, shape/order, continuous row ranges and chunk-ledger entries. It also checked the 22 small output files listed by the result. No local Jacobian, nonlinear field, matrix product or scientific solve was recomputed during these byte checks.

| Actual array | Shape | Raw bytes | Full raw SHA256 |
| --- | --- | ---: | --- |
| Original stage Jacobians | `576 x 224 x 224` | 231,211,008 | `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19` |
| Original stage residuals | `576 x 224` | 1,032,192 | `4cd548d191d2f57a33a9fc8b1455ac2d07b442a6031f08b344906a3773658c05` |
| Original returned delta | `577 x 224` | 1,033,984 | `d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2` |
| Computed scaled stage defects | `576 x 224` | 1,032,192 | `65873e31430920893f4fc062bb1fb93e7d55b5c0819f67423130fbbbd92aadbb` |

All 28,901,376 stored J entries and all 129,248 stored delta entries are finite. The producer's saved maximum absolute J entry is `1.0007950021979336e29`; matching that saved value's bit pattern locates its unique occurrence at stage58, row223, column111, namely Pi112 versus Q112. The producer's saved maximum absolute delta is `3.0663412735007466e26`; its unique matching bit pattern is negative at node43, row223, Pi112. These positions were located by original-byte identity matching of already reported extrema, not by a locally executed new numerical experiment.

The complete base, target, residuals, stage outputs, original scales, far graph, physical height, original correction, all computed defects and the selected maximum-chart matrices are preserved. The large raw arrays stay in the public Actions artifact; their complete chunk/source/input/hash manifest is published in Git.

## Actual computed defects in the original equations and scales

The diagnostic implements the full stage/cut/far model of [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md). For the originally returned direction delta it records the floating evaluation of all rows of $e=A\delta+\widehat r$, divided by the corresponding original sigma. It uses the original stored stage Jacobians and the original matrix-vector routine, with every mode retained.

| Original row family | Rows | Saved maximum absolute scaled defect | Nonfinite values |
| --- | ---: | ---: | ---: |
| All stage rows | 129,024 | `7.3718085303337e40` | 0 |
| Complete cut rows | 112 | `0` | 0 |
| Complete far rows | 112 | `0` | 0 |

The worst saved scaled stage defect is negative, at stage43, rawCell0, rawSegment3, residual row221: Pi mode110, frequency220. Its binary64 little-endian representation is `b3195f596a146bc8`.

This is a direct computed linear-model discrepancy, substantially different from merely observing a large chart-condition number. The enormous reported full-model defect supplies a concrete reason to examine the original linear correction before retrying its known failed nonlinear trials. It does not by itself identify the exact real-arithmetic defect of the saved binary arrays: dot-product cancellation and ordinary rounding remain part of this readout. R266 separates that finite-array algebra from the exact derivative of a nonlinear reference map. A targeted exact binary-rational reconstruction of the reported worst row is therefore a useful next Actions calculation.

The floating zeros at cut and far are reported as such. They do not assert exact nonlinear tail acceptance or a rigorous derivative bound.

## Actual worst chart and its limits

All 576 backward chart stages were observed. The greatest reported finite product occurs at stage43, rawCell0, rawSegment3:

| Chart quantity | Saved value |
| --- | ---: |
| Infinity norm of G | `2.8010116829379707e37` |
| Infinity norm of the computed inverse | `3.145629903617709e22` |
| Original reported product | `8.810946110232247e59` |

The complete G, H, inverse, next/current graph, affine vectors and intermediate t/u/graph-times-t arrays at this selected stage are saved. The maximum-chart stage and maximum computed-defect stage coincide in this run. This does not make the chart product a condition number of the entire multiple-shooting system, nor does it establish a unique cause. R266 gives the exact distinction between a chart failure and invertibility of the full system.

The known actual25 nonlinear trials failed at stage13/rawCell0/rawSegment7. That is a different recorded location. Request28 did not execute those trials again, and it does not manufacture a trial norm or claim a nonlinear correction was accepted.

## Continuation from this complete finite model

The next independent Actions calculation can reuse every saved J, residual and boundary block to solve the identical full linear system with pivoted band factorization. Original row and column scales are explicit invertible transformations; every recovered direction must still be read back in all original stage/cut/far equations and original sigma. This does not require another native Jacobian pass.

The comparison will retain the original delta and its complete defect readout, add exact binary-rational checks of selected worst rows, and preserve the entire new direction and original-scale residual. No full-system condition claim, new height, repeated zero solve or native acceptance is inferred in advance. Actual nonlinear trials and any complete tail response remain separate future calculations under the original scientific gates.

## Principal receipt identities

| File | SHA256 |
| --- | --- |
| `capture-summary.json` | `48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1` |
| `capture-manifest.json` | `3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3` |
| `capture-initial-arrays.json` | `92d96d99b996fba23829742de9f2a187ec3a06ede25a51aa62febf498224e721` |
| `capture-begin.json` | `8eb2996c3c41cd230ed4f58cc78c17c35482c612b9c34a3b6668ec5dd097f676` |
| `result.json` | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
