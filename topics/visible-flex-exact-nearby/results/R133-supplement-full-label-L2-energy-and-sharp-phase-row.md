# R133 supplement: full label L2 energy and the sharp phase row

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved for all true labels on the whole negative interval.**
Using every completed169-germ endpoint, its complete true transport
error, and all3072 actual analytic drift rows gives

$$
 \boxed{\sup_{0\le r\le r_*}
   \|a_\pm(r)-1\|_{L^2_\phi}
       <.013437992352652.}
 \tag{L.1}
$$

Here $a_\pm=\partial_\phi(H\circ S_\pm)$ are the true labels of the
original exact24-mode $H$, not the finite reference derivatives.
All angular $L^2$ norms use normalized measure on the fourfold circle.
The complete mean remains one.

The resulting full explicit-family phase row, after the nonzero
conjugacy-defect correction and the complete K48 change of coordinates,
obeys

$$
 \boxed{\Sigma_G>.01358262433697499544>1/80,\qquad
        \Sigma_{G,x}>.05433049734789998178>1/20.}
 \tag{L.2}
$$

The full response contract is correspondingly stronger: a same-background
complete error $\|q_\nu-Z\|_{L^2_r(E_0)}\le1/200$, or the same bound
in ordinary pair $L^2$, would leave the physical row above
$.0071115274966255>1/200$. That response-error hypothesis has not
been silently supplied.

## 1. Exact energy cancellation of the scalar speed

The true transported derivative solves

$$
 a_r+\partial_\phi((d\pm c)a)=0,\qquad \langle a\rangle=1.
$$

Put $b=a-1$. Since $c$ is a real scalar and
$\partial_\phi c=0$, integration by parts on the normalized circle
gives the exact identity

$$
 \frac12\frac{d}{dr}\|b\|_2^2
 =-\frac12\langle d_\phi b^2\rangle-\langle d_\phi b\rangle.
 \tag{L.3}
$$

Consequently, in the upper Dini-derivative sense also when
$\|b\|_2=0$,

$$
 \frac{d}{dr}\|b\|_2
 \le\frac12\|d_\phi\|_\infty\|b\|_2+\|d_\phi\|_2.
 \tag{L.4}
$$

The reversed radial equation has the same absolute-value bound.
There is no charge involving $|c|$, $q'$, or a derivative of a scalar
Taylor remainder.

Let $[u,v]$ be one whole scalar germ and let
$L_{uv}=\int_u^v\|d_\phi\|_\infty\,dr$.
Using $\|d_\phi\|_2\le\|d_\phi\|_\infty$, the forward estimate is
$(\|b(u)\|_2+L_{ur})e^{L_{ur}/2}$; the backward estimate has $v$
in place of$u$. At each intermediate$r$, one of the two actual
cumulative integrals is at most $L_{uv}/2$. Therefore

$$
 \boxed{\|b(r)\|_2\le
 \left(\max(\|b(u)\|_2,\|b(v)\|_2)+\frac{L_{uv}}2\right)
       e^{L_{uv}/4}.}
 \tag{L.5}
$$

This is a whole-germ estimate. It is not interpolation between
sampled values.

## 2. Turning every saved finite endpoint into a true endpoint

Each saved phase endpoint is an exact real Fourier polynomial.
For its derivative minus one, Parseval gives the exact expression

$$
 \|\widehat a-1\|_2^2
 =2\sum_{j=1}^{64}(4j)^2
       \big((\operatorname{Re}\widehat W_j)^2+
            (\operatorname{Im}\widehat W_j)^2\big).
 \tag{L.6}
$$

Every term in this sum is a rational square before the final Arb
square root. The true endpoint error is paid separately.

The completed genuine Wiener residual from the transport theorem is
$\mathcal R<9.652387746401\,10^{-14}$ on $A_{1/24}$.
For a true single inverse ray the complete drift budget is
$B<.010507004681650$. Choose the positive input width$3/100$.
Its actual margin is

$$
 \frac1{24}-\frac3{100}-B
 >.0011596619850167.
$$

The scalar transport error equation and the actual Wiener composition
therefore give
$\|A(r)-\widehat A(r)\|_{A_{3/100}}\le\mathcal R$
at every saved endpoint. Direct Fourier differentiation gives

$$
 \|a(r)-\widehat a(r)\|_{A_0}
 \le\frac{\mathcal R}{e(3/100)}
 <1.183638336706\,10^{-12}.
 \tag{L.7}
$$

The complete true source, including its even mean and all unretained
Fourier outputs, is the source of this endpoint bound.
There are no initial or interface value jumps.

All169 original endpoint natives are checked by their stored SHA,
exact chronological intervals and original phase configuration.
The maximum finite endpoint norm is less than
$.013295595045709$. For each germ, all intersecting actual analytic
drift boxes are consumed. Their $A_{1/64}$ first-derivative bounds
are valid upper bounds for the required real $L^\infty$ and $L^2$
norms. Combining (L.5)--(L.7) gives the strict-germ part of (L.1);
the largest enclosure occurs in germ167.

The remaining root interval starts at the saved exact$r_b$.
Its full drift Lipschitz integral is less than
$1.140939602565\,10^{-11}$. The one-sided form of (L.4), starting
from the last certified endpoint, gives a root bound below
$.013295595058378$, which is smaller than (L.1).
The interval to the common upper root endpoint is only an upper
integration budget; no positive interval is regarded as an actual
negative characteristic.

## 3. The complete first parameter functional

Use the same full explicit direction and the signed scalar and
nonmean drift derivatives of the previous correlated theorem.
Write

$$
 Y=.013437992352652,\qquad
 \epsilon_\infty\ge\sup_{r,\pm}\|a_\pm-1\|_\infty,
$$

where the actual unrounded native gives
$\epsilon_\infty<.053142540$.
The exact mean-one identity gives
$\langle a_\pm^2\rangle=1+\|a_\pm-1\|_2^2$.
Also, for$b=a-1$,

$$
 \|a^2-1\|_2
 \le2\|b\|_2+\|b^2\|_2
 \le(2+\epsilon_\infty)Y.
$$

Since the true $\dot d$ has exactly zero angular mean, the complete
functional
$\Gamma_0=\int\langle a_+^2\dot F_+-a_-^2\dot F_-\rangle\,dr$
satisfies

$$
 \left|\Gamma_0-2\int\dot c\,dr\right|
 \le2Y^2\int|\dot c|\,dr+
       2(2+\epsilon_\infty)Y\int\|\dot d\|_2\,dr.
 \tag{L.8}
$$

All these source integrals already include every3095 scalar/cubic
intersection, the true root remainder, all output frequencies and
the actual even mean. The present consumer reads their original
SHA-bound native and never substitutes products of separate
unrelated field bounds.

The two actual fees in (L.8) are less than respectively
$2.723895017826\,10^{-5}$ and $.003829744620238$.
The full signed scalar integral then gives

$$
 \Gamma_0>.01358265631934926365.
$$

The genuine nonzero-defect weight correction from the completed
transport is below $1.946519978000\,10^{-8}$, and the entire K48
row change is below $1.251717448822\,10^{-8}$.
Subtracting both gives (L.2). The resulting normalized family is
$F_\delta=4G P_\delta G^{-1}$, with initial KAM lift identity.
Its initial averaged parameter row is independent of the constant
target angle.

## 4. Full response errors and exact scope

For the same continuous background, the full response-return theorem
and positivity of $G'$ give

$$
 |\Delta\Sigma_G|
 <1.274436\,\|G'\|_\infty
     \|q_\nu-Z\|_{L^2_rL^2_\phi}.
 \tag{L.9}
$$

For the energy norm $L^2_r(E_0)$ the smaller constant1.273240 is
available. The even mean belongs to both norms; no frequency cutoff
or inverse turning weight is introduced.
With the proved $\|G'\|_\infty<1.015523233862$ and the exact rational
hypothesis $\|q_\nu-Z\|\le1/200$, (L.2) and (L.9) leave the
physical row greater than
$.0071115274966255>1/200$, hence the normalized row greater than1/50.

This remains a hypothesis on the true full regular response.
The original mean and physical fourth-mode boundary rows must remain
in its definition. A nonlinear change of background is a further
separate error. No full PDE inverse, PDE branch, or completed
nonlinear phase equation is inferred from this conditional contract.

## 5. Actual source and native

The source is
`scripts/fourfold_codazzi_phase_complete_label_L2_twist.py`.
Its first complete execution consumed every real input and passed
all seven gates in4.25 seconds. That execution took place in the
current local session; same-source public Actions replay is recorded
separately, without relabeling its provenance.

The49182-byte native is
`notes/2026-11-14-R133-complete169-label-L2-sharp-twist-native.json.gz`,
SHA256
`8ad3c9e30a15e307f036456baf3334e00592208228af6df39a9c1cc020b8eeef`.
It retains the endpoint norm on each side of every germ, each exact
interval and native SHA, all local drift integrals, the entire root
fee, the complete endpoint transport error, and every scalar-row fee.
No transported phase polynomial or scalar cache was recomputed.
