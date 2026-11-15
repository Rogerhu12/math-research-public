# R133 supplement: actual complete strict-exterior first Airy derivatives and local sources

2026-11-15, visible-exact / phase_inverse.

**Actual public execution completed.** Run
[43657793725](https://github.com/Rogerhu12/math-research-public/actions/runs/43657793725)
returned zero and passed all eleven mathematical gates. It completed the new
first coefficient derivative table on all 1328 original common cells and the
strict-exterior first-correction derivatives and local source on all six
original radii. The six cases contain 4359 accepted exterior integral rows.

The local source bounds are finite but much too large to close the required
strong return. This execution does not certify the cutoff-97 inverse.
It preserves the complete derivative and normalized forcing data needed to
improve the bounds without repeating successful mathematics.

## 1. Exact execution and scientific identities

The implemented theorem is
[the ordered old-radial transport and strict-exterior derivative contract](R133-supplement-ordered-old-radial-transport-and-strict-exterior-first-correction-derivatives.md),
(E.1)--(E.18), with
[the third-jet exterior and holomorphic inner overlap](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md),
(D.1)--(D.24). It consumes the same genuine correction as
[the actual complete old-radial Taylor calculation](R133-supplement-actual-complete-old-radial-first-Airy-Taylor-bounds.md).
It introduces no new correction or interface datum.

The workflow event commit is 52b9c8e25571ea9fdf4d2f3b08519bcce291a6e8.
The immutable scientific checkout, after the first real pull, is
59bc1e3209c4bdbc16ed8d6774368c5ef74702b4.
The actual runtime is Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5,
SciPy 1.17.0, with 320-bit Arb arithmetic.

| Item | SHA256 |
|---|---|
| Mathematical producer | e196557e61aa9b83249654a1a81ca3a003ca38e1e07f4ff4fdb19a877f86f4df |
| Immutable input manifest | acf16500058828ddb96dcec22de8d3fb80cd5743e979dae908a554566a3c49f7 |
| Index native, 14518 bytes | 7322737799bb339750e2df4fb9738da32690801cb669655a600200df5691ba35 |
| Mathematical process, 43892 bytes | bca94cb112df2f916935b002ed3c4ffd58ab6eea827f579d82c1864369308f4d |
| Worker process, 3206 bytes | 70b527dd6168b4f147530a42987c21c16468218ee1a0f278e1ea8377ca0642e9 |

The complete readable receipts are
[mathematical process](../notes/strict_exterior_first_Airy_local_sources_ci/run-43657793725-1/consumers/process.json),
[worker process](../notes/strict_exterior_first_Airy_local_sources_ci/run-43657793725-1/worker-process.json),
and [publication record](../notes/strict_exterior_first_Airy_local_sources_ci/run-43657793725-1/publication.json).
The mathematical child took 1355.98521484 seconds; the wrapper recorded
1356.677235266 seconds for the driver.

The worker made two real pulls and checked the two required README differences:

- 2026-11-15T00:22:33.133115+00:00: the event commit advanced to the
  scientific checkout above; the combined README diff was empty.
- 2026-11-15T00:45:16.938393+00:00: the checkout advanced to
  97f93fd585302d68f0f459ec2090e0005bbbb55e; the combined README diff
  was empty.

## 2. Same family, uncertain root and exact source

The unchanged background definition has SHA256
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.
The unchanged explicit direction definition has SHA256
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.

The intrinsic parameter is fixed at the original $\eta_0$.
The real explicit parameter disk is $|\delta|\le10^{-8}$, with the
original $\nu_\delta$ identity and complete coefficient/repair charges.
No wider intrinsic-parameter statement is inferred.

Write $\rho=r_*-r$ and $h=9\cdot10^{-6}$. The retained root interval is

$$
r_*\in[r_-,r_+]
=\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
 \right].
\tag{E.1}
$$

The complete fixed inner physical interval is

$$
[r_- -h,r_++h]
=\left[
 \frac{1191939371497}{5000000000000},
 \frac{2384058743003}{10000000000000}
 \right].
\tag{E.2}
$$

For each original radius $R$, the exterior is
$[r_- -R,r_- -h]\cup[r_++h,r_++R]$, intersected with the unchanged
original common partition. Every exterior point therefore has a paid
distance at least $h$ from every possible true root.

The local numerator is the unnormalized quantity

$$
N_{\rm raw}=\mu\mathcal L_0w_1,\qquad
\mu=Q^2(X_\phi^2+T T_\phi^2).
\tag{E.3}
$$

The original scalarized trial has input density $n^{7/6}$ and correction
$n^{-1}w_1$, where $n=4|j|$. Its first original-row local source is

$$
J\,P\,\mathsf S_\rho(N_{\rm raw}),\qquad
\mathsf S_\rho(w)c
 =\sum_{|j|\ge97}n^{1/6}\mathcal U_{n,\epsilon}(w_\epsilon)c_j .
\tag{E.4}
$$

The execution bounds this whole operator from $H^{-4/3}$ input to the
ordinary radial $L^2H^{-2/3}$ source window. Every output Fourier mode,
the output mean, and the final old $J$ window are retained.
There is no further free factor $1/(4\cdot97)$, and
$\mu^{-1}N_{\rm raw}$ is not substituted for $N_{\rm raw}$.

The new third leading jets and first normalized forcing derivatives use
the original complete intrinsic derivatives through order three and the
strict-root identities (D.5)--(D.16). No fourth intrinsic derivative or
new target evaluation was performed. The first-correction derivatives
come from the genuine ordered first-order old-radial transport, including
all differentiated ordered products.

## 3. Actual complete six-case bounds

These table entries are strict outward decimal upper bounds for the
reported interval values. Both source columns are ordinary radial
$L^2H^{-2/3}$ bounds for (E.4).

| $R$ | Negative rows | Positive rows | Negative local source | Positive local source |
|---:|---:|---:|---:|---:|
| $1/1000$ | 113 | 28 | $4.691836\cdot10^{21}$ | $1.150755\cdot10^{22}$ |
| $1/500$ | 201 | 70 | $5.918771\cdot10^{21}$ | $1.416320\cdot10^{22}$ |
| $1/200$ | 403 | 221 | $8.533838\cdot10^{21}$ | $1.952455\cdot10^{22}$ |
| $1/100$ | 565 | 330 | $1.425015\cdot10^{22}$ | $3.121238\cdot10^{22}$ |
| $3/200$ | 681 | 422 | $2.515435\cdot10^{22}$ | $5.350317\cdot10^{22}$ |
| $1/50$ | 790 | 535 | $4.000637\cdot10^{22}$ | $8.318498\cdot10^{22}$ |

The true inverse-phase Fourier tail begins at lag 97 in all six cases.
Its complete factors are bounded above by, respectively,

$$
15758.084,\quad15772.104,\quad15863.389,\quad
16140.621,\quad16403.359,\quad16629.073.
\tag{E.5}
$$

Both lag signs and zero output are included, with the infinite geometric
tail actually checked. The local-numerator angle strip is $1/128$;
the saved amplitude derivative output strip is $1/512$.
The original wider leading strip is $3/64$.

After the independently accepted complete negative source-to-primitive
map, the bounds for this local component alone are

$$
\begin{array}{c|c}
R&H^{-4/3}\to L^2\text{ primitive}\\
\hline
1/1000&7.111488\cdot10^{20}\\
1/500&1.512646\cdot10^{21}\\
1/200&6.802321\cdot10^{21}\\
1/100&7.462789\cdot10^{22}\\
3/200&9.068217\cdot10^{23}\\
1/50&8.835020\cdot10^{24}.
\end{array}
\tag{E.6}
$$

All other sources and the root datum are zero for this particular
linear component. Equation (E.6) is not a boundary-value inverse or
feedback estimate. Every strict positive exterior cell lies beyond the
original fixed body cut; its collar contribution for this component is
exactly zero. The positive body entries above remain source bounds.
A complete positive port conversion is separate.

The raw derivative majorants locate the current loss. At $R=1/1000$,
the saved $b_1$ supremum bound is below $5.485268\cdot10^6$,
its first old-radial derivative below $4.074650\cdot10^{13}$,
and its second below $2.502527\cdot10^{19}$.
At $R=1/50$ these bounds are below $1.117835\cdot10^7$,
$1.079187\cdot10^{14}$ and $7.055318\cdot10^{19}$.
They are upper bounds, not measured sizes or lower bounds for the true
derivatives. Their size does not establish that the actual return is large.

## 4. Preserved complete state and exact reuse

The process verifies the original successful 1300-row root, 1328-row
first-forcing, all 1079 true seams, all six complete fold/amplitude
tensors, and all 75 old-radial Taylor stages. All old target, FFT,
intrinsic/cubic point, ray, completed forcing coefficient, completed
amplitude, Taylor algebra and seam recomputation counters are zero.

Only the 1328 new first coefficient derivative rows and 4359 exterior
derivative/local-source rows were evaluated. There are six new
partial-endpoint radial weights; the other 4353 weights are copied
from the complete original radial source partition.

The index and these seven natural mathematical files are preserved
unchanged. Each is below the original-file publication limit.

| Natural file under consumers/ | Bytes | SHA256 |
|---|---:|---|
| coefficients/complete-new-first-coefficient-derivatives.json.gz | 2528689 | 5a3c5f4d7a8b65e35c698a5b68725c3f7f6d99a8bcb0d00a6c2c36bdc78f6ddd |
| cases/radius-1-1000.json.gz | 278441 | f036ffdbe1b5f82074df6680d8ed8546e3b923caaa2d75511e9f7f936af037f2 |
| cases/radius-1-500.json.gz | 527166 | 594a12a49afcef302f373f4650a64be7971bdc6104d835e256ede91fea3d5fc5 |
| cases/radius-1-200.json.gz | 1197342 | 7e2bc6efdbe55987ce2b505dcfbd1287ac267ab155dca18990c247dec180cc77 |
| cases/radius-1-100.json.gz | 1712245 | 1bf250f7bd2f96cdc331fe2c876527e9a66e7ae3ea4e03080a8347f2bca3454b |
| cases/radius-3-200.json.gz | 2105663 | 5ac946cf9eebf66a627eedab0f7422b50609f91c3411bbd63d342a6c607e993e |
| cases/radius-1-50.json.gz | 2522939 | fd3308cbe8828c58d355b07d148b5726c99fb36101b481f06365ddc864a5a07a |

Each exterior row retains its original physical interval, side, root
row and candidate piece; new leading-third evidence; complete forcing
and its first radial derivative; both normalized vectors
$f=(f_a,f_b)$ and $f_\rho$ with angular Cauchy bounds; separate strip
supremum and Wiener derivative tables; raw and normalized local
numerators; the actual final $J$ factor; and radial squared integrals.

The reviewed producer saves the two normalized forcing value vectors
on strip $1/32$ and their angular Cauchy bounds on $1/128$.
They are majorants in the displayed order, not signed coefficient
arrays and not permission to subtract independent upper bounds.

Every new row was checkpointed before the next row was attempted.
A completed case summary is also retained across the interruption
window between case completion and index completion.

## 5. Scope and exact remaining obligations

The artificial boundary (E.2) is an overlap boundary for two estimates
of the same correction in the original physical piece. There is no new
trial cutoff, jump or partition-of-unity source. The genuine physical
seam contributions remain separate and are not set to zero.

This execution pays only the exterior local term.
The complete old-circle nonlocal words and independent even-mean
residual still require consumption of these accepted derivative tables,
using [the exact mean compression and complete correction budgets](R133-supplement-exact-old-mean-compression-and-first-correction-nonlocal-budgets.md).
All full matrix triples and successful local arrays are available.

The [exact root-value subtraction contract](R133-supplement-exact-root-value-subtraction-and-real-radial-first-Airy-amplitude-bounds.md)
removes the apparent $b_*/T$ contribution before norms, while preserving
the same physical correction and all genuine forcing jumps.
No numerical improvement from that contract is asserted here.

The full corrected strong return, all seam and endpoint ports,
unknown high feedback, finite-head Schur complement, genuine parameter
response and nonlinear PDE branch are not proved by this local result.
All eleven gates establish complete finite bounds; none is a final
small-strong-norm acceptance gate.
