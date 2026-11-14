# R133 supplement: actual complete cap-trial Hessian error

2026-11-14, visible-exact-astra-ac0d / newton_source.

**Proved by a complete directed computation.** On the exactly repaired
final centre, the residual-sensitive change from the physical cap equation
to the moving equation has the following error on the actual 97-column
cap trial $T$:

$$
 \mathcal E_H(T)<3.320733114\,10^{-5},\qquad
 \frac{\mathcal E_H(T)}{1-\chi_H}<3.333534423\,10^{-5}.
 \tag{T.1}
$$

Every one of the 1,341 original local source cells and all 1,977
intersections with the true trial intervals is included. The computation
uses all 97 orthonormal moving input columns, all 257 physical states,
and the physical even mean. No target or primitive is recomputed.

This is the actual additional Hessian error of this trial. Its complete
physical equation residual, independent boundary errors, and complete
physical output tail remain a separate number $\varepsilon_T$. In
particular the following conclusion is already available without
pretending that the uncompleted residual cover is complete:

$$
 \boxed{\quad
 \|T_{\rm mov}-T\|_{\mathfrak M}
 <1.003854965\,\varepsilon_T+3.333534423\,10^{-5}.
 \quad}
 \tag{T.2}
$$

Here the norm is the full physical module of
[the local triangular source theorem](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md),
and $T_{\rm mov}$ is the genuine moving linear cap solution expressed in
physical variables. The bound holds at **$\eta=\eta_0$**, with affine
offset zero. It does not enlarge the residual-sensitive bridge to the
whole original affine interval.

## 1. The exact common input

The original centre is
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
The actual continuous repair is
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.
The true radial interval is $[9/10,25/8]$. The original centre, its
repair, and the physical cap proposal are distinct objects with their
individual recorded identities.

The trial is the exact real piecewise cubic Hermite matrix defined by
the complete shared-value array and its two one-sided derivative arrays.
Its physical states are

$$
 (B_1,\ldots,B_{128},C_0,C_1,\ldots,C_{128}).
 \tag{T.3}
$$

The input is the entire orthonormal moving even head
$1,\sqrt2\cos(4\phi),\ldots,\sqrt2\cos(384\phi)$.
The proposal was already precomposed with the actual directed
moving-to-physical inlet. The three whole-array SHA-256 values are

| Array | SHA-256 |
|---|---|
| Shared values | `007cb7045db455c2c9a3872b37db91933a676c164b52b81c940929c12648af31` |
| Left derivatives | `d292fb049c3cc004f8ab711d5abff93f37e07c25b930d93167ad733d01791197` |
| Right derivatives | `b4692b336b1961fe058a9882b8c093722f724fcbdda40776e8d34c99d11026fd` |

The proposal index SHA is
`b9819522aceed06b73628d84b8bb80dbcc5b734971c6b3c20544e9876c23d78a`.
The producer checks every whole array before using it. The endpoint
graph separately supplies all 1,297 actual radial nodes. In particular,
the first binary64 node is not declared to equal the rational $9/10$:
the same exact first cubic is evaluated on the short interval between
these two points. The final node is exactly $25/8$.

The 1,341 local source cells and their six directed coefficients are
read from
`2026-11-14-R133-complete-local-cap-Hessian-source-native.json.gz`,
SHA `bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd`.
This input already includes the actual full centre residual, its first
angular derivative, the continuous-repair difference, all means, and
the original complete physical Green gains. The current calculation
does not replace any of them by a finite background model.

## 2. Gram factors and continuous radial integration

All circle $L^2$ norms use normalized measure. For a physical coefficient
matrix $X$, whose input columns are orthonormal, define

$$
 \begin{aligned}
 \|X_B\|_{\rm HS}^2
   &=\frac12\sum_{j=1}^{128}\sum_{a=0}^{96}|X_{B,j,a}|^2,\\
 \|X_C\|_{\rm HS}^2
   &=\sum_{a=0}^{96}|X_{C,0,a}|^2
     +\frac12\sum_{j=1}^{128}\sum_{a=0}^{96}|X_{C,j,a}|^2.
 \end{aligned}
 \tag{T.4}
$$

The input mean has unit norm. The physical nonzero sine/cosine modes
have squared norm $1/2$, and the physical even mean has squared norm
one. The producer applies these factors to every output and every
input column. Thus these Hilbert--Schmidt bounds also bound the full
operator norm from the input $\ell^2_{97}$.

Intersect each original local source cell $I_i$ with every trial cubic
that it meets. On an intersection $J$, write the exact same Hermite
polynomial in the normalized variable $x\in[-1,1]$, and then in Legendre
form $T(x)=\sum_{k=0}^3 L_kP_k(x)$. Orthogonality gives the exact identity

$$
 \int_J\|T_B(r)\|_{\rm HS}^2\,dr
  =|J|\sum_{k=0}^3\frac{\|L_{B,k}\|_{\rm HS}^2}{2k+1},
 \tag{T.5}
$$

and likewise for $C$, with its mean included. All coefficients are
enclosed by directed interval arithmetic before this identity is
consumed. No radial sample is used to bound the integral.

For the module norm, a cubic $a_0+a_1x+a_2x^2+a_3x^3$ is converted
exactly to its four Bernstein coefficients on $x=2t-1$, $0\le t\le1$.
Writing

$$
 c_0=a_0-a_1+a_2-a_3,\quad c_1=2a_1-4a_2+6a_3,\quad
 c_2=4a_2-12a_3,\quad c_3=8a_3,
 \tag{T.6}
$$

the coefficients are
$c_0$, $c_0+c_1/3$, $c_0+2c_1/3+c_2/3$,
$c_0+c_1+c_2+c_3$. Their convex hull gives a continuous bound for
each individual output-mode/input-column entry. The maximum over all
subintervals of $I_i$ is taken **before** summing modes or columns.
This is exactly the order in the $\ell^2_k(\sup_r)$ module norm.

## 3. All ordinary and divergence source terms

Use the six local coefficients of the cited source theorem. On a true
intersection $J\subset I_i$, put
$b_J=\|T_B\|_{L^2(J;\mathrm{HS})}$ and
$c_J=\|T_C\|_{L^2(J;\mathrm{HS})}$. The complete ordinary source
bounds are

$$
 \begin{aligned}
 o_{B,J}&=(E_{1,i}+Z_{BB,i})b_J+Z_{BC,i}c_J,\\
 o_{C,J}&=(E_{1,i}+Z_{CC,i})c_J,\\
 O_B^2&=\sum_Jo_{B,J}^2,\qquad O_C^2=\sum_Jo_{C,J}^2.
 \end{aligned}
 \tag{T.7}
$$

The local coefficients are upper bounds on the whole original cell,
so (T.7) follows from the triangle inequality in $L^2(J)$ followed by
the exact disjoint union of the intersections. It includes every
physical mean contribution of the triangular source formula.

Let $b_i,c_i$ be the module Hilbert--Schmidt bounds obtained by the
coefficientwise Bernstein maxima in Section 2. Then

$$
 D_B^2=\sum_i(E_{A,i}b_i)^2,\qquad
 D_C^2=\sum_i(E_{A,i}c_i)^2
 \tag{T.8}
$$

bound the complete two angular-divergence sources. There is **no radial
length factor** in (T.8). For each Fourier coefficient the supremum on
the whole cap is at most the square root of the sum of squared cell
bounds; summing Fourier coefficients and input columns proves the
stated bound. Multiplication by the original full $A^0$ coefficient
uses the already proved module Young inequality. The finite support of
the trial does not truncate the product or the unknown solution.

The actual directed results are

| Complete source norm | Strict outward upper bound |
|---|---:|
| $O_B$ | $1.215469180\,10^{-7}$ |
| $O_C$, including the even mean | $1.024297349\,10^{-7}$ |
| $D_B$ | $5.620397731\,10^{-7}$ |
| $D_C$, including all induced modes | $4.637280826\,10^{-7}$ |

The auxiliary full trial norms satisfy
$\|T_B\|_{L^2_r\mathrm{HS}}<0.054711480368$ and
$\|T_C\|_{L^2_r\mathrm{HS}}<0.043631588450$.

## 4. Applying the actual complete inverse

Let $G_{o,B},G_{o,C},G_{d,B},G_{d,C}$ be the four complete physical
Green gains from the local input. The producer reads their directed
values and computes

$$
 \mathcal E_H(T)=
 G_{o,B}O_B+G_{o,C}O_C+G_{d,B}D_B+G_{d,C}D_C.
 \tag{T.9}
$$

These gains already include the full physical coefficient feedback,
all Fourier modes, and the actual exterior derivative. Applying that
feedback a second time would be incorrect. The only additional
resolvent in (T.2) is the proved residual-sensitive Hessian feedback,
whose directed value is less than $1.003854965$.

For completeness, write the physical solution with the same exact data
as $T_{\rm phys}$, and let $A$ be the full Hessian feedback in physical
variables. Then
$T_{\rm mov}=T_{\rm phys}+AT_{\rm mov}$, $\|A\|<\chi_H$, and

$$
 (I-A)(T_{\rm mov}-T)
   =(T_{\rm phys}-T)+AT.
 \tag{T.10}
$$

The whole-interval bound $\|AT\|\le\mathcal E_H(T)$ proves (T.2).
No pointwise identification of the physical and moving equations is
made. Every inner inlet error, the independent physical mean matching
row, outer Robin and mean errors, and any genuine point source must
remain in $\varepsilon_T$ with its original gain. The unknown full
physical tail is part of that error, not silently zeroed.

At the moving cut, the already proved complete change of equations has
norm less than $3.228515$. Hence its contribution from the particular
Hessian term (T.1) is less than $1.076241934\,10^{-4}$; the independent
mean row keeps its original normalization. This does not replace the
full cut matrix or delete its infinite moving output tail.

## 5. Computation, files, and scope

The producer is
`scripts/fourfold_codazzi_cap_trial_local_Hessian.py`, SHA
`0a0473fe57f250f74c52a7c59848812007ab9762947340041d7bb17b7ae50e59`.
It completed normally with all eight gates, 1,341 original cells and
1,977 exact trial intersections. Core wall time was 349.249 seconds;
the recorded process took 353.269 seconds, maximum RSS 426,000 KiB,
with an explicit 1,792 MiB address-space bound. No optional repeat run
was used as an extra publication condition.

The complete native is
`notes/2026-11-14-R133-complete-cap-trial-local-Hessian-native.json.gz`,
SHA `cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26`.
It contains all 1,341 rows, each exact interval and local source
coefficients, the full input-array identities, all source norms, and
the final directed bounds. Its original process record and a small
reconstruction manifest accompany it. The reproducible invocation is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python3 scripts/fourfold_codazzi_cap_trial_local_Hessian.py \
  --proposal /workspace/scratch/ac0d699811ad/physical-cap-precompose-20261114.json \
  --out /workspace/scratch/ac0d699811ad/cap-Hessian-trial-20261114/recomputed-native.json.gz
```

The large proposal arrays are reproducible inputs and are not duplicated
in the repository. Their complete construction is the previously
published padded-cap/precomposition reconstruction. The final native
is 822,018 bytes. This conclusion pays the actual trial Hessian term;
it does not assert a full continuous body inverse, a nonzero exact
parameter Schur complement, or a nonlinear solution.
