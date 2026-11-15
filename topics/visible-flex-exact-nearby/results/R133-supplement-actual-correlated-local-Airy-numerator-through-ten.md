# Actual correlated local Airy numerator through degree ten

## Completed result and scope

The public computation
[43666374252, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43666374252)
completed successfully on 2026-11-15. Its mathematical child returned $0$,
all **ten** mathematical gates passed, and the mathematical process took
**23.569766216000005 seconds**. It consumed **26** already completed natural
coefficient stages without changing their bytes and saved **60** new
complete natural stages.

This executes the
[correlated-numerator and complete-tail contract](R133-supplement-correlated-complete-local-Airy-numerator-and-Taylor-tail.md)
using the accepted
[Taylor table through degree twelve](R133-supplement-actual-append-only-old-rho-Airy-Taylor-through-twelve.md).
It is a result about the full local amplitude numerator of the explicit
repaired family. The complete reconstructed $JP$ Airy source, its radial
integral, the old-circle nonlocal terms, the independent even mean, genuine
seam sources, and the global high inverse remain separate.

The fixed intrinsic parameter is

$$
\eta_0=-\frac{7789843107295549}{4611686018427387904},
\qquad |\delta|\le10^{-8}
\quad\text{on the full complex parameter disk}.                 \tag{A.1}
$$

All signed Fourier coefficients, including the amplitude mean, are retained.
No positive-mode truncation, real-part replacement, or centre-only
cancellation is used.

## A. The exact local quantity

Use $\rho=r_*-r$ and $D=-\partial_\rho-d\partial_\phi$. With $w_1=(a_1,b_1)^t$,
the quantity actually computed is

$$
\begin{aligned}
N_{\rm raw,\varepsilon}
={}&\bigl[
 \partial_\rho^2+2d\partial_\rho\partial_\phi
 +(d_\rho+dd_\phi+T_0d)\partial_\phi
 +(d^2+\eta^2K)\partial_\phi^2\\
&\hspace{25mm}+T_0\partial_\rho+V_0
\bigr]w_1
+i\varepsilon\vartheta Q
 \begin{pmatrix}0&T\\1&0\end{pmatrix}w_1.                       \tag{A.2}
\end{aligned}
$$

The order of multiplication and differentiation is exactly that displayed.
The signed $K$ in the angular coefficient is preserved. In the corrected
fold convention,

$$
N_{\rm raw,\varepsilon}=\mu L_0w_1,\qquad
\mu=Q^2(X_\phi^2+TT_\phi^2).                                  \tag{A.3}
$$

The new computation does not divide by $\mu$. The actual local reconstructed
first-row source requires $JP\,\mathsf S_\rho(N_{\rm raw})$, not the
normalized $L_0w_1$ substituted in its place.

The new finite outputs are the eleven complete coefficients

$$
N_n=[\rho^n]N_{\rm raw,+},\qquad 0\le n\le10.                  \tag{A.4}
$$

Every signed summand in a given Fourier coefficient is added before its
absolute norm is evaluated. The two previously saved complete products
$T_0d$ and $\vartheta Q$ are read directly. This consumes $w_1$ through
degree twelve and no uncomputed coefficient.

The full support is recorded separately at each degree. It runs from
$[-576,576]$ for the first component and $[-768,768]$ for the second at
degree zero, to $[-2496,2496]$ and $[-2688,2688]$ at degree ten. These are
indices $j$ in $e^{4ij\phi}$; every multiplication is non-circular.
The natural stage records contain every intermediate coefficient as well.

Both carrier signs are covered at the same complex parameter by the
accepted algebraic identities

$$
(N_{\rm raw,-})_a=-(N_{\rm raw,+})_a,\qquad
(N_{\rm raw,-})_b=(N_{\rm raw,+})_b.                            \tag{A.5}
$$

This is not a complex-conjugation argument.

## B. Full domain and complete infinite remainder

The unchanged true-root interval is

$$
r_*\in
\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
\right].                                                     \tag{B.1}
$$

The original physical root piece is

$$
\left[
 \frac{2147184947341121}{9007199254740992},
 \frac{4295308144604611}{18014398509481984}
\right].                                                     \tag{B.2}
$$

The original holomorphic product domain has radial radius $R=1/6000$ and
old-angle width $\Sigma=1/128$. The reported physical interval is

$$
\left[
 \frac{1191939371497}{5000000000000},
 \frac{2384058743003}{10000000000000}
\right],
\qquad
|\rho|\le h=\frac{90000009}{10^{13}}.                           \tag{B.3}
$$

Its identity with the physical family is only asserted inside (B.2). No
analytic continuation across an original physical seam is declared to be
the original background.

Every coefficient majorant used for the tail comes from the same complete
holomorphic auxiliary case: input radius $1/2000$, fold radius $3/8000$,
coefficient angular width $1/32$, and old leading angular width $3/128$.
The new gates verify that these domains contain the required whole product.

The complete amplitude suprema on that product remain bounded by

$$
M_a<0.515180947651754,\qquad M_b<1410.835059136508.              \tag{B.4}
$$

All degrees $n\ge11$ of (A.2) are paid by the positive radial series in
(N.6)--(N.10) of the contract. For example, with $t=h/R$ and $m=11$,

$$
\begin{aligned}
U(t)&=\frac{(m+1)(m+2)t^m}{1-t}
+\frac{2(m+2)t^{m+1}}{(1-t)^2}
+\frac{2t^{m+2}}{(1-t)^3},\\
V_0(t)&=\frac{(m+1)t^m}{1-t}+\frac{t^{m+1}}{(1-t)^2},
\qquad V_1(t)=U(t)/2.                                       \tag{B.5}
\end{aligned}
$$

The bare second radial derivative, each full coefficient-times-derivative
product, and each cross amplitude are paid separately with these complete
positive sums. No computed finite prefix is subtracted from a large
rounded total to define a remainder.

The strip-supremum and Wiener estimates are separately labelled. The latter
include the entire two-sided Fourier sums with physical factor $4|j|$,
including the $j=0$ contribution when the derivative order is zero.
The original coefficient product and the alternative half-width argument
are minimized only after each complete Wiener bound is established.

## C. Actual complete derivative bounds

The following entries are strict decimal upper bounds rounded upward from
the complete Arb records. The column $q$ denotes the actual old angular
derivative $\partial_\phi^q$. Every entry includes the full finite part
and all higher radial and angular terms.

### Strip supremum

| Output width | Component | $q=0$ | $q=1$ | $q=2$ |
|---|---|---:|---:|---:|
| $0$ | $a$ | $53.576817695$ | $404.557732574$ | $3310.666830261$ |
| $0$ | $b$ | $13315707.220991736$ | $55588.278394825$ | $392558.442870201$ |
| $1/1024$ | $a$ | $53.973471857$ | $407.804323525$ | $3339.742705596$ |
| $1/1024$ | $b$ | $13315761.680524388$ | $55971.782180292$ | $396547.362399663$ |
| $1/512$ | $a$ | $54.373309627$ | $411.079311537$ | $3369.284855065$ |
| $1/512$ | $b$ | $13315816.514291689$ | $56358.835933160$ | $401089.515656949$ |

### Analytic Wiener norm

| Output width | Component | $q=0$ | $q=1$ | $q=2$ |
|---|---|---:|---:|---:|
| $0$ | $a$ | $53.579038744$ | $404.842718752$ | $3384.008321832$ |
| $0$ | $b$ | $13315713.303384390$ | $56368.719471803$ | $593405.772175333$ |
| $1/1024$ | $a$ | $53.976016131$ | $408.177572897$ | $3449.599533338$ |
| $1/1024$ | $b$ | $13315768.648077363$ | $56993.934003704$ | $697392.763749205$ |
| $1/512$ | $a$ | $54.376285254$ | $411.588864605$ | $3544.423382876$ |
| $1/512$ | $b$ | $13315824.663112140$ | $57754.258503071$ | $880710.325800268$ |

A strip-supremum entry may not be substituted for the corresponding Wiener
entry.

For $q=0$, the complete signed-correlation bound is no larger than the
previous complete triangle bound in both components at all three widths.
For example, at width $1/512$ the old triangle bounds were

$$
\begin{aligned}
 68.712280536959127290139249634893\ldots,\\
 13452216.620034952575339835128040\ldots ,
\end{aligned}
$$

whereas the new complete bounds are

$$
\begin{aligned}
 54.373309626925364011108607589064\ldots,\\
 13315816.514291688081845564856128\ldots .
\end{aligned}
$$

The improvement is an actual result, not an assumption in any gate.

## D. Finite part, tail, and complete mean

At output width $1/512$, the complete strip-supremum components split as
follows. These are separately rounded upper bounds; their unrounded
complete sums, rather than these printed rounded columns, define Section C.

| Component | $q$ | Complete finite prefix upper bound | Complete infinite-tail upper bound |
|---|---:|---:|---:|
| $a$ | 0 | $54.373274437$ | $0.000035191$ |
| $a$ | 1 | $411.073295423$ | $0.006016114$ |
| $a$ | 2 | $3367.226044621$ | $2.058810444$ |
| $b$ | 0 | $13315816.417922894$ | $0.096368796$ |
| $b$ | 1 | $56342.360669690$ | $16.475263470$ |
| $b$ | 2 | $395451.416816668$ | $5638.098840282$ |

Thus the large zero-derivative second component is already present in the
accepted finite numerator; it is not caused by omitting or grossly rounding
its infinite tail. This observation does not permit removing the mean.
The actual degree-zero second-component mean is saved, including its
complex parameter uncertainty, as

```text
real: [-1.3248e+7 +/- 6.62e+2]
imag: [+/- 0.157]
```

Every other degree's full mean ball is saved as well. A ball containing
zero for a first-component mean has not been replaced by exact zero.
The amplitude mean is also not the independent physical even-mean
equation after Airy reconstruction.

The computed numerator remains a complete signed local object. It does
not certify that the $N=97$ reconstructed strong residual is small, nor
does it authorize division by a local gap without the stated operator
and source contracts.

## E. Exact stage inventory and the initial zero-mathematics failure

The sixty new complete natural stages are:

| New stage type | Count |
|---|---:|
| Full signed numerator coefficients, degrees 0 through 10 | 11 |
| Previously unsaved supporting derivatives/products | 11 |
| Complete Fourier norm rows, eleven at each of three widths | 33 |
| Whole-product multiplier bounds and positive radial tail | 2 |
| Complete strip-supremum and Wiener budget pairs | 3 |

The 26 inputs come from their separately identified original inventories:
the original 75 Taylor stages and their 205-stage extension. They are not
regenerated under the new source identity. Both original complete products
$T_0d$ and $\vartheta Q$ are reused as accepted outputs.

The first public attempt,
[43666029053](https://github.com/Rogerhu12/math-research-public/actions/runs/43666029053),
failed in the `Hydrate39` wrapper step. Its manifest had omitted the
topic prefix from one algebra source path. The source-parse step and
mathematics were skipped. The correction at commit
`a24bfa3d59da32453405764136ecc6b5d02e4fd0` changed only that one path and
the corresponding workflow manifest pin. No mathematical source, CI
source, worker source, accepted stage, or original byte content was changed.
There were zero mathematical stages to repeat from that failed attempt.

The successful run separately verifies source, runtime, manifest, contract,
all original complete byte identities, and every saved natural stage.
It preserves failed prefixes and requires the same scientific identity
for a future resumption.

## F. Native identities and actual pulls

The scientific source is
`scripts/fourfold_codazzi_correlated_first_Airy_local_numerator.py`,
SHA256

```text
e9024812c2f87fe18cb43fcdd5661b6063cc7e5cf5ba4380af5b8a5d50e605fe
```

The corrected 39-file manifest is
`notes/2026-11-15-R133-correlated-first-Airy-local-numerator-CI-inputs.json`,
SHA256

```text
bc34acdc1738a92bf71d9ce6c8be2dddfced3ae1de0ca884a1025c45419256d1
```

The actual scientific checkout was
`1cd8ff1bf19cee26d3d33522843f43dbd7929d91`; the workflow event commit was
`a24bfa3d59da32453405764136ecc6b5d02e4fd0`.

All files below are relative to

```text
topics/visible-flex-exact-nearby/notes/
correlated_first_Airy_local_numerator_ci/run-43666374252-1/
```

| File | Bytes | SHA256 |
|---|---:|---|
| `consumers/correlated-first-Airy-local-numerator.json.gz` | 60456 | `fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e` |
| `consumers/process.json` | 34986 | `6396a554ab8401d709744b47315ab73830dfe2051937a980ecaab0efa8fc82db` |
| `consumers/complete-natural-stage-inventory.json.gz` | 6376 | `c8158e4d381b84b9b8f5593bbab7e3bcd21dae16839207f9ef2b9b60b8c1fed7` |
| `worker-process.json` | 2744 | `ca1d91af47e141a2ab4b3a22ad8988185be25f7e8e7f6c6b6e1a3b7aedf5cb1a` |
| `publication.json` | 13844 | `41e83e4a927f2bd7c71ff4ec365727cf568c5b54b378dc3a9e4802b1ce1a6b02` |

The [readable process](../notes/correlated_first_Airy_local_numerator_ci/run-43666374252-1/consumers/process.json)
contains all ten actual gates, all three complete derivative tables,
separate finite and infinite parts, all eleven Fourier supports and mean
balls, and the full native identity. The publication lists all 66 natural
output files. The largest saved stage is 240371 bytes; no artificial file
split or truncated coefficient payload is involved.

Two real pulls were made, with empty differences for the root and topic
READMEs:

| UTC time | Before | After |
|---|---|---|
| 2026-11-15 02:09:24.323875 | `1cd8ff1bf19cee26d3d33522843f43dbd7929d91` | `1cd8ff1bf19cee26d3d33522843f43dbd7929d91` |
| 2026-11-15 02:09:49.382802 | `1cd8ff1bf19cee26d3d33522843f43dbd7929d91` | `f6c34f25c172acb0d7cf3df39add2126d92ae21b` |

The reviewed-rule receipt is
`fdb83fd44505b84955d81b1e070ea45001ef9064880b2b4613a8a67e26e3e0d1`.
All exact native, stage, and original input identities remain available for
the next physical source consumption.
