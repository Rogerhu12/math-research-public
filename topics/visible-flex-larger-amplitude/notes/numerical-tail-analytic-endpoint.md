# Actual finite-tail first-slope derivative

This replaces the endpoint **first-slope and mean-slope derivative rows** by
an analytic chain rule on the actual finite nonlinear shooting graph. It
does not change the nonlinear equations, physical metric, boundary height,
or positive branch. The second-jet derivative rows still use the source
symmetric difference and are labeled accordingly in each response.

## Formula and conventions

Let the retained physical cut height coefficients be \(H\), cut radius \(r\),
and normalized height state \(Q=H/r^4\). The cut shooting node stores
\((Q,\Pi)\), while the actual final cell engine uses
\(y=(Q,\rho\Pi,0,0)\), where \(\rho=2^a\). The computed finite shooting
graph derivative is

\[
G=\frac{\partial\Pi}{\partial Q}.
\]

Write the actual engine field as \(F(y)\), with the physical radial chart
derivative \(r_x\ne0\). The first \(M\) engine equations imply the exact
algebraic identity

\[
(Z_r)_j=\frac{r^4}{r_x}F_j+4r^3Q_j.
\]

At fixed physical cut and tail metric, differentiating gives

\[
\boxed{\frac{\partial Z_r}{\partial H}
 =\frac{F_Q+\rho F_\Pi G}{r_x}+\frac4r I.}
\]

The mean correction state has field \(F_{2M}=r_xwL_0\), so its first-slope
derivative is

\[
\boxed{\frac{\partial(wL_0)}{\partial H}
 =\frac{(F_{2M})_Q+\rho(F_{2M})_\Pi G}{r_xr^4}.}
\]

The background mean slope \(w\) is independent of \(H\), hence the same
derivative applies to the full mean slope. These are radial derivatives;
the prefix still needs its own orientation and arclength chain rule. In
the current prefix convention \(H=\sigma qY_z\), its terminal nonmean
first-slope condition is \(qY_{z,s}=Z_r/\sqrt E\). There is no additional
\(\sigma\) on that displayed right-hand side.

The graph \(G\) and field derivatives are those of the actual finite root,
RK integration, and far Robin condition. Calling this an analytic
derivative does not certify the Fourier, radial, or infinite-depth limit.

## Implementation and immutable source

- `computations/numerical-tail-slope-jacobian.mjs` exports
  `actualSlopeJacobian(dn, solution)` and `replaceFirstSlopeRows(...)`.
- `computations/numerical-tail-analytic-worker.mjs` reads the fixed source
  worker, checks the exact replacement occurrence counts, redirects its
  relative imports to their source locations, and evaluates the adapted
  text in memory. It does not write a modified source file.
- `computations/numerical-tail-analytic-client.py` retains the source
  persistent request/response protocol and complete compressed response
  recording. Its `WeightedTailPort` constructor has the source signature.
- `computations/numerical-m2-tail-probe.py --client analytic-first` selects
  this adapter; the default `--client source` remains the original worker.

The required backend is `fourier-root` with tangent warm prediction. Each
adapter run records exact replacements, all redirected imports, source
revision, and SHA256 in its `*_adapter.json`; each response also contains
the original and owned source hashes. The fixed source revision is
`869436630c99aa5a68afb55bd8877c826034d117`.

Relevant fixed source implementations are
`scripts/78718-tail-tangent-core.mjs` (`tangentGraphAtCut`, source endpoint
differences), `scripts/78718-tail-fourier-product-jacobian.mjs`
(`rhsWithJacobian`), and
`scripts/78718-prefix-tail-tangent-fourier-worker.mjs` (recording protocol).
The worker source SHA256 used for the first check is
`36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a`.

## Actual mixed-mode verification

The comparison uses the successful smallcut30, \(M=16\),
\(\lambda=0.5625\) nonlinear tail, with every retained physical height
coefficient present. See
`numerical-m2-smallcut30-q02-lambda05625-dn-jacobian.json` for complete
matrices, physical vector, sources, and response hash.

| Quantity | Value |
|---|---:|
| Actual shooting residual | \(2.906\times10^{-10}\) |
| Algebraic first-slope identity error | \(8.47\times10^{-22}\) |
| Mean-slope identity error | \(1.69\times10^{-21}\) |
| Maximum source first-slope Jacobian entry | \(1003.06049\) |
| Analytic minus source, source step \(10^{-4}\) | \(3.087\times10^{-6}\) |
| Same difference relative to maximum Jacobian entry | \(3.08\times10^{-9}\) |
| Analytic minus source, source step \(2\times10^{-5}\) | \(1.235\times10^{-7}\) |
| Mean derivative difference at step \(10^{-4}\) | \(6.43\times10^{-12}\) |

The first-slope discrepancy falls by approximately 25 when the symmetric
difference step falls by five, as expected for its quadratic truncation
term. This checks the new chain rule against an independent endpoint
difference, rather than against another implementation of the same formula.

A complete live-adapter request then repeated the successful
\(\lambda=0.5859375\) mixed vector, including actual nonlinear re-solve,
first/second endpoint jets, and whole-tail audit:
`numerical-m2-smallcut30-q02-analytic-check-response_0001.json.gz`.
The retained first slopes changed by at most \(5.09\times10^{-21}\), and
the whole-tail audit was unchanged to the reported digits. The reloaded
shooting residual was \(1.151\times10^{-9}\), below the configured
\(2\times10^{-9}\) tolerance. The response explicitly labels first and
mean slope derivative rows analytic, and second derivative rows symmetric
difference.

This verification only addresses the derivative adapter. The \(M=16\)
tail's normalized full Darboux defect is still approximately \(0.009804\);
same-height \(M=24\) refinement is required before making a stronger tail
accuracy claim.
