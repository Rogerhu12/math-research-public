# R133 supplement: complete optical speed bounds on the parameter disc

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** For the final fixed metric parameter $\nu_0$ and actual
affine value $\eta=\eta_0$, the true compact metric variation admits an
exact cancellation in the two characteristic speeds. On the entire
complex parameter disc $|\delta|\le10^{-6}$, the complete square-root
margin is greater than $0.9999955393$. The companion Arb computation
consumes all 626 accepted scalar cells and all 220 compact-control
quotient cells. It gives explicit integrated bounds through three
parameter derivatives and retains the true mean direction.

These are bounds for an **explicit approximate-centre family**. They do
not assume an exact PDE solution branch, identify a finite response with
a true inverse, or close the joint PDE and phase Schur complement.

## 1. The explicit family and the same actual metric

Let $\bar Q=(u,v)$ be the exactly continuous repair with definition
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.
Let $Z=(\xi,\zeta)$ be any explicitly specified direction with the same
odd/even reflection convention. It may have infinitely many angular
frequencies if the norms used below are finite. Define

$$
 Q_\delta=\bar Q+\delta Z,
 \qquad \nu_\delta=\nu_0+\delta,
 \qquad m=\langle v\rangle,\quad z=\langle\zeta\rangle,
 \tag{P.1}
$$

where

$$
 \nu_0=-2572625729470897/72057594037927936.
 \tag{P.2}
$$

The parameter in (P.1) is a construction parameter. After the joint
problem has selected its final value, that value must remain fixed
through the intended flex family. No varying metric is being counted
as an isometric deformation.

The actual compact function is

$$
 w(r)=4096t^6(1-t)^6,
 \qquad t=\frac{r-1/20}{9/50-1/20},
 \quad 1/20\le r\le9/50,
 \tag{P.3}
$$

and $w=0$ outside this interval. Thus $0\le w\le1$ on the real radial
axis, and

$$
 w'=\frac{24576}{9/50-1/20}t^5(1-t)^5(1-2t).
 \tag{P.4}
$$

All unsubscripted metric coefficients below are the true coefficients
at $\nu_0$ and $\eta_0$. Set

$$
 T=\frac{\beta}{2E_{\nu_0}}
   =\frac{\beta}{2(a\gamma)^2},\qquad k=Tw',\qquad q^2=-K.
 \tag{P.5}
$$

The complete quotient $T$ is already proved in
[the cached derivative theorem](R133-supplement-cached-complete-scalar-derivatives-and-compact-parameter-column.md).
Its actual denominator, complete primitive errors and original affine
value are retained; it is not a fitted or truncated scalar.

## 2. Exact cancellation and root behavior

Since $E_{\nu_0+\delta}=E_{\nu_0}e^{\delta w}$ and $\beta$ is
independent of $\nu$, the actual metric identities give

$$
 \gamma_\delta=\gamma e^{\delta w/2},\qquad
 K_\delta=(K+\delta k)e^{-\delta w}.
 \tag{P.6}
$$

Consequently, with the branches continued from $\delta=0$,

$$
 \boxed{\quad
 \gamma_\delta\sqrt{-K_\delta}
     =\gamma\sqrt{q^2-\delta k},\qquad
 c_\delta=-\gamma(m+\delta z)\sqrt{q^2-\delta k}.
 \quad}
 \tag{P.7}
$$

Here $c_\delta$ is the full scalar part of the moving characteristic
speed. The angular drift is

$$
 d_\delta=\beta I_\phi
       \big((u+\delta\xi)^2+K_\delta(v+\delta\zeta)^2\big),
 \qquad F_{\pm,\delta}=d_\delta\pm c_\delta.
 \tag{P.8}
$$

The real mean $z$ is present in (P.7), even when it nearly cancels the
direct metric contribution in a first-order twist. It is not removed by
the zero-mean primitive in (P.8).

Outside the exact compact support, $k=w=0$. There

$$
 c_\delta=c_0-\delta\gamma qz,
 \qquad \partial_\delta^2c_\delta
       =\partial_\delta^3c_\delta=0.
 \tag{P.9}
$$

This holds in the entire actual root collar as well as on the remaining
outer portion of the negative interval. In particular, separately
estimating $\gamma_\delta$ and $q_\delta$ and then charging root factors
$q^{-3}$ for their parameter derivatives would discard the exact
cancellation. The metric type zeros near the actual root do not move
under this compact parameter change.

## 3. Complete branch margin on the parameter disc

Put $\rho=10^{-6}$ and $R(r)=|k|/q^2$ on the compact support, with
$R=0$ elsewhere. The true cache gives

$$
 \sup R<4.460664470,
 \qquad 1-\rho\sup R>0.9999955393.
 \tag{P.10}
$$

Thus every $|\delta|\le\rho$ lies in a single nonzero analytic square-root
disc. Write

$$
 s_-=(1-\rho R)^{1/2},\qquad s_+=(1+\rho R)^{1/2}.
 \tag{P.11}
$$

For complex $\delta$ in that disc,
$|\sqrt{1-\delta k/q^2}|\le s_+$,
$|\sqrt{1-\delta k/q^2}|\ge s_-$ and its real part is at least $s_-$.
The identity
$\sqrt{1-a}-1=-a/(\sqrt{1-a}+1)$ therefore gives the following
complete majorants, each multiplied by the true positive $\gamma q$:

| Quantity | Coefficient of $|m|$ | Coefficient of $|z|$ |
|---|---:|---:|
| $|c_\delta-c_0|/|\delta|$ | $R/(1+s_-)$ | $s_+$ |
| $|\partial_\delta c_\delta|$ | $R/(2s_-)$ | $s_++\rho R/(2s_-)$ |
| $|\partial_\delta^2c_\delta|$ | $R^2/(4s_-^3)$ | $R/s_-+\rho R^2/(4s_-^3)$ |
| $|\partial_\delta^3c_\delta|$ | $3R^3/(8s_-^5)$ | $3R^2/(4s_-^3)+3\rho R^3/(8s_-^5)$ |

For example, differentiating (P.7) without changing the branch gives

$$
 \begin{aligned}
 \partial_\delta^2c_\delta
 &=\frac{\gamma zk}{\sqrt{q^2-\delta k}}
   +\frac{\gamma(m+\delta z)k^2}{4(q^2-\delta k)^{3/2}},\\
 \partial_\delta^3c_\delta
 &=\frac{3\gamma zk^2}{4(q^2-\delta k)^{3/2}}
   +\frac{3\gamma(m+\delta z)k^3}{8(q^2-\delta k)^{5/2}}.
 \end{aligned}
 \tag{P.12}
$$

All denominators in (P.12) occur strictly inside the compact support,
where (P.10) is a complete true bound. The zero expressions in (P.9)
are used exactly outside it.

On the complete cached interval

$$
 0\le r\le r_b
 =1249886203106135147/5242880000000000000,
 \tag{P.13}
$$

the integrated bounds are

| Integral | Coefficient of $\|m\|_\infty$ | Coefficient of $\|z\|_\infty$ |
|---|---:|---:|
| $\int|c_\delta-c_0|/|\delta|$ | $0.069831857$ | $0.199101673$ |
| $\int|\partial_\delta c_\delta|$ | $0.069831903$ | $0.199101743$ |
| $\int|\partial_\delta^2c_\delta|$ | $0.092622552$ | $0.139663898$ |
| $\int|\partial_\delta^3c_\delta|$ | $0.453470289$ | $0.277868109$ |

The native retains the individual cell coefficients, so a consumer can
use the actual local mean functions rather than their global suprema.
These displayed coefficients do not assume a bound for an unvalidated
PDE response direction.

## 4. Complete angular drift and metric derivatives

For a true radial cell, let $W\ge|w|$, $k_*\ge|k|$ and $K_*\ge|K|$.
Put $E=e^{\rho W}$. Valid bounds on the whole complex disc are

$$
 \begin{aligned}
 K_a&=(K_*+\rho k_*)E,\\
 K_d&=(k_*+WK_*)E,\\
 K_1&=(k_*+W(K_*+\rho k_*))E,\\
 K_2&=(W^2(K_*+\rho k_*)+2Wk_*)E,\\
 K_3&=(W^3(K_*+\rho k_*)+3W^2k_*)E.
 \end{aligned}
 \tag{P.14}
$$

They bound, respectively, $|K_\delta|$,
$|K_\delta-K|/|\delta|$, and the first three parameter derivatives.
Similarly
$|\partial_\delta^j\gamma_\delta|
\le\gamma e^{\rho W/2}(W/2)^j$ for $j=1,2,3$.

In any complete Wiener strip $A_\sigma$, write
$U=\|u\|_{A_\sigma}$, $V=\|v\|_{A_\sigma}$,
$X=\|\xi\|_{A_\sigma}$, $Z=\|\zeta\|_{A_\sigma}$,
$U_\rho=U+\rho X$ and $V_\rho=V+\rho Z$.
Since the smallest nonzero physical frequency is four, the complete
primitive has norm at most $1/4$, and (P.8) gives

$$
 \begin{aligned}
 \frac{\|d_\delta-d_0\|_{A_\sigma}}{|\delta|}
 &\le\frac{|\beta|}{4}
  [2UX+\rho X^2+K_dV^2+2K_aVZ+\rho K_aZ^2],\\
 \|\partial_\delta d_\delta\|_{A_\sigma}
 &\le\frac{|\beta|}{4}
  [2U_\rho X+K_1V_\rho^2+2K_aV_\rho Z],\\
 \|\partial_\delta^2d_\delta\|_{A_\sigma}
 &\le\frac{|\beta|}{4}
  [2X^2+K_2V_\rho^2+4K_1V_\rho Z+2K_aZ^2],\\
 \|\partial_\delta^3d_\delta\|_{A_\sigma}
 &\le\frac{|\beta|}{4}
  [K_3V_\rho^2+6K_2V_\rho Z+6K_1Z^2].
 \end{aligned}
 \tag{P.15}
$$

These estimates are complete product inequalities. They retain all
angular frequencies of $Z$, its mean, and the independent metric
parameter column. Angular derivatives can be paid by differentiating
these products using explicitly supplied higher Wiener norms, or by an
explicitly paid narrower strip. No finite-band permission is transferred
to an unknown correction.

For convenience, the actual integrated scalar factors in (P.15) satisfy

| Factor | Complete radial integral |
|---|---:|
| $|\beta|/4$ | $<0.006571341$ |
| $|\beta|K_a/4$ | $<0.003805011$ |
| $|\beta|K_d/4$ | $<0.003524487$ |
| $|\beta|K_1/4$ | $<0.003524488$ |
| $|\beta|K_2/4$ | $<0.003541623$ |
| $|\beta|K_3/4$ | $<0.003637426$ |

One may use these global integrals only when the associated field norms
are bounded over the whole radial interval. The native cell coefficients
allow a sharper local product integration without that replacement.

## 5. Actual computation and remaining obligations

The new source
`scripts/fourfold_codazzi_phase_all_delta_speed.py` consumes the complete
169-germ scalar cover and the complete derivative/$T$ cache. For each
accepted cell it restricts the already proved Taylor identity, including
its point-jet errors and seventh-derivative remainder. It computes
(P.4), (P.10)--(P.15) with Arb at 320 bits and uses the exact compact
support endpoints. No original primitive or angular exponential is
recomputed. All 626 cells and all 220 compact $T$ cells are checked.

The actual run completed seven gates in 4.166 seconds. It also checks
that the whole real interval $\nu_0+[-10^{-6},10^{-6}]$ stays inside
the previously proved intrinsic parameter box $(-1/25,-1/40)$.
The new native is
`notes/2026-11-14-R133-complete-all-delta-optical-speed-native.json.gz`.

The exact invocation, from the topic directory, is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_codazzi_phase_all_delta_speed.py \
  --out notes/2026-11-14-R133-complete-all-delta-optical-speed-native.json.gz
```

This pays the complete scalar parameter coefficients for a genuine
explicit family. A numerical phase-parameter theorem still needs the
complete norms of its chosen direction, the actual full transport and
terminal defect, the parameter twist and the corresponding conjugacy
estimates. A true solution requires the joint PDE and phase correction,
including the finite head, means, all boundary and interface sources,
and the complete returned remainder. None of those conditions is
replaced by the finite response proposal or by (P.10).
