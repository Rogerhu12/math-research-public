# R133 supplement: actual ordinary-only Hessian reweight of the same-Z Green bound

2026-11-14. Public run [43619605142](https://github.com/Rogerhu12/math-research-public/actions/runs/43619605142).

**Proved in the finite 193-state compression.** The actual ordinary-only Hessian source from run 43618931236 gives a smaller same-$Z$ right-boundary load. Consuming the saved 6,391 positive Green profiles yields a fixed negative-window ordinary pair $L^2$ error upper bound below $0.045415209484$. This remains above $1/200$ and does not prove the full PDE response or its unknown high-frequency feedback.

## 1. Actual execution and exact inputs

The public child returned zero and passed all seven scientific gates. Mathematical consumption took 4.125738198 seconds; the recorded child wall time was 10.000648274 seconds. The full output contains every rescaled profile. It reuses the complete 7,721-row same-$Z$ body source, the complete 1,977-row physical cap result, and all 1,341 ordinary-only Hessian rows. It recomputes no body source propagation, Riccati solution, projector, original cap cell, endpoint, or Hessian source cell.

The fixed identity is the continuously repaired centre
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$
and continuous direction
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$,
at affine parameter offset zero, hence physical $\eta_0$ and the original $\nu$.

The actual artifact inputs are:

| Input | SHA256 |
|---|---|
| Original same-$Z$ Green native | eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18 |
| Original complete physical cut native | 8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5 |
| Ordinary-only Hessian native | b1ffc21737ba45d1ef8823af9dccc0baba8b100a1169b60c69f6a7a5d1cfda6c |
| Original Hessian artifact process | 8bd696740f0f1d667487d349cd0ebb51fc2c8efbe9927d49584885388166ea75 |

The last hash identifies the actual artifact snapshot. A later repository process snapshot can append publication records without changing the scientific input.

## 2. New boundary and exact reuse

All fourteen physical-error contributions remain unchanged, with
$$
 \varepsilon_{\rm phys}(w_0)<2.418183101840\,10^{-6}.
$$
Only the particular Hessian additive changes to
$$
 A_H(w_0)<1.348921722044\,10^{-6}.
$$
The same original Hessian resolvent, complete unknown-input error operator, and $Z_{\rm even}-w_0$ difference remain present. The resulting bounds are:

| Quantity | Outward upper bound |
|---|---:|
| Moving cap error for $w_0$ | $3.776426835\,10^{-6}$ |
| True cut 96 odd rows | $1.219226182\,10^{-5}$ |
| True cut independent mean | $3.776427039\,10^{-6}$ |
| Complete true cut 97 rows | $1.276372397\,10^{-5}$ |
| Separate complete known high cut output | $1.235258260\,10^{-5}$ |

The right-channel scale is bounded by $0.233763546095$. Its denominator is the positive numerical load used to construct the original certified profile, not a lower bound on the unknown actual boundary defect. Positivity therefore permits rescaling this one channel. The other three channels remain unchanged.

## 3. Complete finite error bounds and remaining gap

The phase norm is integrated only on the fixed interval
$[0,2383968743003/10000000000000]$, which contains the original negative region. Every ordinary pair norm includes the even mean. The complete BVP and all its interfaces still cover $[0,9/10]$.

| Channel | Whole inner body $L^2$ | Fixed negative window $L^2$ |
|---|---:|---:|
| Complete same-$Z$ body source | $<0.006513350907$ | $<0.003051713268$ |
| Old trial-jump nonnegative surplus | $<4.896727907\,10^{-11}$ | $<2.294290956\,10^{-11}$ |
| Same-$Z$ waist source | $<6.019522904\,10^{-12}$ | $<2.820848757\,10^{-12}$ |
| Refined same-$Z$ right source | $<0.090423158880$ | $<0.042363496191$ |
| Complete sum | $<0.096936509429$ | $<0.045415209484$ |

The right-boundary upper-bound component still dominates. This is not an actual-error lower bound. The source and both boundaries use the same $Z$; no extra $q^*-Z$ identity is silently substituted. The unknown high feedback, full BVP inverse, genuine parameter Schur row, and transfer to a changed nonlinear background remain separate obligations.

## 4. Reproducible evidence

The evidence directory is
`notes/ordinary_Hessian_Green_ci/run-43619605142-1-ordinary-Hessian-cut-Green/`.

| Evidence | SHA256 |
|---|---|
| Complete native, 3,996,142 bytes | 64ce558499b6ec5240ac73e36cb104672b9c2e6e01aa9c6bd4808959d24821d0 |
| Read repository process, 9,012 bytes | 21cd9a69d3f0a666ff373029e54d44c3fa4348ffe6e4d17062ff2505a5363766 |
| Small summary, 23,882 bytes | 64712cc2d7bfa1b1e72f8077630da3fb30fb5a5f099d17377ac9dd047b3c4ad9 |
| Scientific source | f978b5c062b84573ed0f192fec5ca73320bc55a9b155f31c93edd88e6e7cd0fe |
| Worker | 81905c74d1d13a41e7b8ff5b6c3f6f66bda211452b102652a02a3783c61c801d |
| Immutable 238-file manifest | 586bb1dbce5afead453e5341fd18ac48e0d5a00dbc4e3b54c7c3d643c526a64e |

The native basename is `native/complete-same-Z-ordinary-Hessian-cut-and-Green.json.gz`; the text summary is `evidence/complete-ordinary-Hessian-cut-and-Green-summary.json`. Binary native data stayed in the public runner/artifact channel. The process records four real pull/README checks, all with empty rule differences; the last read commit is `9696c3f1c316d848685731b219030795abbf06ef`. The previously reviewed rule commit remains `ee26c0a65a2e63c15f2ccfba6714181584416542`.
