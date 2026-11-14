# R133 supplement: actual missing-midpoint Taylor Hessian

## Public computation and actual reuse

Public Actions [run43633412397](https://github.com/Rogerhu12/math-research-public/actions/runs/43633412397) completed the mathematical child with return code0 and all26 gates. The child took40.001433645 seconds; the native mathematical timer records32.561316291 seconds.

The computation first diagnosed the complete cached Hessian from run43628443697, native SHA256 `8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c`. It preserved all7844 already completed residual rows, all7908 original target domains, every original trial norm, and1325 unaffected complete local Hessian rows. It then derived64 previously missing midpoint enclosures and computed64 new residual rows and16 updated local Hessian rows. **There were zero target evaluations.** All64 missing midpoints were available; no remaining local row needed the missing-point fallback.

The affected original local indices are
$225,226,237,239,248,259,260,270,272,284,293,295,305,306,316,385$.
The whole interval remains exactly $[9/10,25/8]$, with the same candidate, same repaired centre, same physical $\eta_0$, original $\nu$ and same direction $w_0$.

## The actual diagnostic and resulting bound

The group diagnostic sums the original four source-square channels before applying their matching Green gains and the existing Hessian resolvent. It does not sum per-row scores or assert a lower bound on the unknown actual defect.

| Complete original group | Additive numerical-majorant upper |
| --- | ---: |
| The16 missing-midpoint rows | $6.416628352232\,10^{-7}$ |
| The1325 unaffected rows, considered as their own group | $2.288283570496\,10^{-9}$ |
| All1341 selected rows | $6.417342110712\,10^{-7}$ |

The actual directed ratio of the first group budget to the third is enclosed around $.99988877661994719$. This passed the prescribed one-half diagnostic and triggered the64 derivations. Group bounds in this table are separate square-sum budgets and are not asserted to add exactly.

After the derivations and new residual consumption, the final complete additive is

$$
E_H(Tw_0)<5.884046519508\,10^{-7}.
$$

The final selection uses the complete tight split four-source bound:

| Source channel | Upper bound |
| --- | ---: |
| Ordinary $B$ | $9.137102786558\,10^{-10}$ |
| Ordinary $C$ | $9.531845679760\,10^{-10}$ |
| Angular-divergence $B$ | $9.666974667037\,10^{-9}$ |
| Angular-divergence $C$ | $9.142354717146\,10^{-9}$ |

The corresponding physical Green source is below $5.861450832307\,10^{-7}$. The original Hessian resolvent is unchanged and below $1.003854964897$. Complete old and new decompositions were compared as whole legal bounds. In particular, the locally selected mixed decomposition was not silently substituted when its whole bound was larger.

This is a strict improvement of the complete $w_0$-specific bridge bound. The derived points still leave a substantial majorant. This run does not itself produce a new finite193 response-error bound, prove the $1/200$ response gate, or identify the displayed majorant with an actual error.

## Why the new midpoint rows are certified

For each missing point, the consumer used only original saved point anchors on the same actual scalar germ. It covered the entire signed displacement path with original closed third-derivative enclosures and took their interval convex hull $J_3$. The identities were

$$
f(y)\in f(x)+d f'(x)+d^2f''(x)/2+d^3J_3/6,
$$

$$
f'(y)\in f'(x)+d f''(x)+d^2J_3/2,\qquad
f''(y)\in f''(x)+dJ_3,\qquad d=y-x.
$$

These signed integral-Taylor enclosures also cover negative $d$. The consumer intersected valid left/right-anchor enclosures with the original target whole jets; an empty intersection would fail. It never used a newly derived point as a fresh anchor.

Every original parameter enclosure was verified to contain the same fixed physical $\eta_0$. The wider positive-width graft boxes remained valid enclosures of that point; this grants no wider-parameter conclusion. The receipts distinguish newly derived points from original native point jets.

The residual and Hessian consumption retained complete finite Fourier support, every scalar/radius remainder, the independent mean, pointwise versus joint-Wiener bounds, the factor for the repaired centre and the exact original trial direction. The original14 physical-cap fees and6 boundary errors remain unchanged. The difference $Z_{\rm even}-w_0$ still uses the old complete moving error-operator norm; this run improves neither that operator nor unknown high feedback.

## Evidence identities and actual rule checks

The directory is

`notes/missing_midpoint_Taylor_Hessian_ci/run-43633412397-1-missing-midpoint-Taylor-Hessian/`.

| Record | Bytes | SHA256 |
| --- | ---: | --- |
| Repository `process.json` | 26846 | `2fbb9f43f25d99e8bedccc0ddcde1993c8d15f45385121411928bcba5104c23e` |
| `evidence/complete-missing-midpoint-Taylor-Hessian-summary.json` | 29251 | `3b04068d298d303d4ebc58f6003fc5a3b326ad8905a9c5f0ee3b4d812e4526df` |
| `evidence/actual-original-fallback-group-budget.json` | 7675 | `cf2e66446ad215aadad805b3f8a311c9c4b304f4d259c383ea1594b77a9380dd` |
| `native/complete-missing-midpoint-Taylor-Hessian.json.gz` | 7538124 | `f85bddc8c1ac7e30a6790818fb52596c88e193fff9312cd4f2bfe20b07549759` |

The native is preserved in4 exact byte parts, with its lossless manifest. All small summaries are below60000 bytes. The source SHA is `ebaa3caaca274b36e816dc4c1797cf7367a3ce06d5eb1d8778879e24c0349c3e`; helper SHA is `356c8c09ff9014e56e7d0e53521552d6f3d66c96801478c66735790791cef850`. The worker SHA is `5ea4af7652c92b89b7570fde1a9a187ff24be1a37a6fdd357ddc45efccac9963`, and the189-file manifest SHA is `890c5f9d9c5251ddf7d545b4c373fd96d35dfca5782b9137651374be367a14fd`.

The process records4 actual pull/README checks with empty diffs. Its last read commit is `365e1c40c0ff0357a8915fda4c3ec5427842c0e1`; separately reviewed rules remain at `ee26c0a65a2e63c15f2ccfba6714181584416542`. The complete stored input receipts preserve the original artifact-process identities, including their distinction from later repository publication snapshots.

The same-$Z$ true-cut conversion and the right Green-channel reweighting are separate consumers. The full high BVP inverse, low/high Schur feedback, changed-parameter transfer and nonlinear existence remain outside this result.
