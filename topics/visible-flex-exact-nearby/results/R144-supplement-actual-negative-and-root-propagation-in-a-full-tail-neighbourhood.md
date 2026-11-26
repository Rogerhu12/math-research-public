# R144 supplement: actual negative and root propagation in a full-tail neighbourhood

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all39 saved-rational comparisons pass.** The complete negative
root and strict Cauchy propagation extends to the same arbitrary
full-tail $A^3$ background radius $10^{-6}$ used by
[QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md).
The stronger and weaker windows are realizations of one actual full
Fourier evolution, with the entire mean vector and original jumps.
On the strict interval a new direct $L^2$ energy consumes the same
completed SP two-state matrices, by a fixed diagonal similarity.
No old $H^1$ inverse is assigned an unproved $L^2$ action.

At the actual fixed root cut the root constants are
$C_0<6.532358$ and $C_{-1}<10.936492$. For the complete root-to-waist
connection the stronger $L^2$ density gains are below $1192.763571$
for root/impulse data and $84.341121$ for ordinary root sources.
The weaker primitive-plus-mean density gains are below
$2038.695371$ and $144.157533$, respectively.
All source units and the separate strict-source gains are specified
below. These are given-root Cauchy maps; no boundary selection,
normalized strong return or full low/high Schur is inferred.

## NR1. Same metric, same root and a genuinely infinite background

For real $|\delta|\le10^{-10}$ let

$$
 Q=\widetilde Q_\delta+e,\qquad
 \sup_{0\le r\le R_{\rm out}}\|e(r)\|_{A^3}\le\rho=10^{-6},
 \quad R_{\rm out}=25/8,
 \tag{NR.1}
$$

where $\widetilde Q_\delta$ is the compact mean-exact centre of SM.
The norm is the unweighted component-sum norm QN.2, so it controls
the Euclidean-pair Wiener norm with factor one. All Fourier modes
of $e$ are allowed. The real odd/even class is the original one.
At each original radial interface use the prescribed state
transmission and retain every affine impulse. Piecewise continuous
radial backgrounds suffice; no $e_r$ bound is assumed.

The intrinsic metric is precisely $\nu_0+\delta$, with the original
fixed intrinsic $\eta_0$. Define

$$
 \kappa=\sqrt{-K_\delta},\quad
 r_-={1191984371497\over5000000000000},\quad
 r_+={2383968743003\over10^{13}},\quad
 \omega_r=r_+-r_-=9\,10^{-13},
 \quad r_c=r_+-1/200 .
 \tag{NR.2}
$$

The true root $r_*$ remains in $[r_-,r_+]$. The strict interval
is $[0,r_c]$. Every original root window of radius at most $1/50$
lies above $9/50$, so both the intrinsic compact metric bump and
the compact-centre control vanish there exactly. On that root
region $\widetilde Q_\delta=Q_*$; only the new $e$ may depend on
$\delta$. This does not set the selected parameter to zero on
the strict interval.

The two completed small inputs are the same ones used by STC/RTC:

| Complete input | Path and whole SHA256 |
|---|---|
| SP, public run43731464771/1 | [execution](../notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json), a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12 |
| Six complete root windows, public run43621934843/1 | [summary](../notes/large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/evidence/full-real-large-root-Cauchy-summary.json), 238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5 |

The new
[rational reader](../scripts/fourfold_codazzi_compact_nearby_negative_saved_bounds.py)
only combines these complete saved bounds and already proved
STC/RTC/TH scalar conclusions. It evaluates no old native row,
growth integral, chronological product or scientific target.

## NR2. The exact strict equation gives both source windows

Use the unscaled characteristic state of
[SP.1--SP.18](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md):

$$
 \xi=T(\kappa)h,\quad y=I\xi,\quad z=\Pi\xi,\quad
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 Y=\sqrt\kappa\,\|y\|_2,\quad Z=\sqrt\kappa\,|z|.
 \tag{NR.3}
$$

Its exact norm is

$$
 Y^2+Z^2
 =\|Ih_1\|_2^2+\kappa^2\|Ih_2\|_2^2
                      +|\Pi h_1|^2+\kappa^2|\Pi h_2|^2 .
 \tag{NR.4}
$$

The actual equation and its primitive/mean equations are SP.5
and SP.6, with every primitive word and the true mean-input
rank. They hold at an unsolved background. In particular they
use no nonlinear mean equation and no derivative of an approximate
mean normalization.

For the stronger norm define instead

$$
 H=\sqrt\kappa\,\|P_\perp\xi\|_2,\qquad Z=\sqrt\kappa\,|z|,
 \qquad
 H^2+Z^2=\|h_1\|_2^2+\kappa^2\|h_2\|_2^2 .
 \tag{NR.5}
$$

We prove its comparison from the actual equation.
On each original cell use SP's complete scalar quantities
$b\ge|\beta|$, $g\ge\gamma$, $R,L,D$, and put

$$
 \begin{gathered}
 B_1=4bRL,\quad A_1=6bRL,\quad
 N_y=2bL(R+L/4),\\
 N_z=bLR/2,\qquad N_\gamma=gL,\\
 \mathcal A(b_*)=
 \begin{pmatrix}
 \max(0,b_*+D+(A_1+N_y)/4)&D/2+B_1/16+(N_z+N_\gamma)/4\\
 A_1+N_y&\max(0,b_*+N_z)
 \end{pmatrix}.
 \end{gathered}
 \tag{NR.6}
$$

The orientation-dependent $b_*$ is the original full physical
logarithmic rate $F$ or $B_{\rm rev}$. The scalar radial fee is
$c_+=\max(0,\kappa_r/\kappa)$ or
$c_-=\max(0,-\kappa_r/\kappa)$, respectively.

The nonmean part of the local equation has real energy rate
at most $b_*+c_\pm$ by the same physical symmetric calculation
SP.16--SP.19. Orthogonal nonmean projection changes no inner
product with $P_\perp\xi$. The primitive part of the full
nonlocal term acting on this nonmean input has norm at most
$bLR/2$, by $\|I\|\le1/4$, $|(r_-,r_+)|\le\sqrt2 R$
and $|(r_-,r_+)_\phi|\le\sqrt2 L$.
The independent mean-input rank acts only on $z$.

For the constant-to-nonmean column, the exact SP.5 expression is
$P_\perp[(2d_\phi I_2+B)z+\mathcal Nz]$.
The complete bounds are

$$
 2D+B_1/4+N_z+N_\gamma=4\mathcal A_{12}.
 \tag{NR.7}
$$

Here $\|B-\Pi B\|_{L^2}$ costs $B_1/4$ by the fourfold
Poincare inequality, componentwise on its two off-diagonal
entries. The radial part of $B$ has zero nonmean projection.
This is an estimate of the actual column, not an attempt
to invert the primitive on arbitrary $L^2$ functions.

For the mean equation use the already exact SP.6 row and
$\|I P_\perp\xi\|_2\le\|P_\perp\xi\|_2/4$:
its nonmean-to-mean coefficient is at most
$(A_1+N_y)/4=\mathcal A_{21}/4$.
Its mean diagonal is the same $\mathcal A_{22}+c_\pm$.
Finally
$bLR/2\le D+(A_1+N_y)/4$, so the new nonmean diagonal
is at most $\mathcal A_{11}+c_\pm$.

Thus, with $D_4=\operatorname{diag}(4,1)$, the actual strong
two-state Dini inequality is dominated by

$$
 {d^+\over dt}\binom HZ
 \le[D_4\mathcal A(b_*)D_4^{-1}+c_\pm I_2]\binom HZ
          +\sqrt\kappa
                  \binom{\|P_\perp T f\|_2}{|\Pi T f|}.
 \tag{NR.8}
$$

The weak inequality remains SP.18, with $If$ in its first
source slot. Both characteristic means are retained as the
complete vector $z$; the original reflection constraint on
the odd physical mean is not replaced by deleting a branch.
All estimates extend to the full infinite Fourier equation
by the original characteristic flow, energy approximation
and density argument.

## NR3. Actual nearby strict matrices and propagation constants

The metric is the same as the original selected family.
STC gives $b<2$, $g<7$, $\kappa<1.03$,
$R^o<1.912$, $L^o<3.704$, and $\kappa>.5338$.
The exact compact-to-selected bridge, together with (NR.1),
permits the full state and angular increments

$$
 \epsilon_R=5\,10^{-7}+1.03\rho,\qquad
 \epsilon_L=1.31\,10^{-6}+1.03\rho .
 \tag{NR.9}
$$

No support restriction is used. Define

$$
 \begin{aligned}
 s&=2(1.912)\epsilon_R+\epsilon_R^2,\\
 p&=1.912\epsilon_L+3.704\epsilon_R+\epsilon_R\epsilon_L,\\
 t&=2(3.704)\epsilon_L+\epsilon_L^2,\\
 d_D&=4s,\quad d_b=8s,\quad d_A=12p,\quad d_B=8p,\\
 d_y&=4p+t,\quad d_z=p,\quad d_\gamma=7\epsilon_L,\\
 E&=
 \begin{pmatrix}
 d_b+d_D+(d_A+d_y)/4&d_D/2+d_B/16+(d_z+d_\gamma)/4\\
 d_A+d_y&d_b+d_z
 \end{pmatrix}.
 \end{aligned}
 \tag{NR.10}
$$

Exactly as in STC, both new nonnegative weak matrices are
entrywise bounded by the old completed matrices plus $E$.
For the strong matrices the corresponding increment is
$D_4ED_4^{-1}$. The actual rational bounds are

$$
 \|E\|_F<.000224,\qquad
                   \|D_4ED_4^{-1}\|_F<.000167 .
 \tag{NR.11}
$$

For the following sharper constants the reader retains
directed rational square-root bounds for the exact matrices
in (NR.10), before rounding the displayed numbers.

Let $P_\pm^o$ be the original saved nonradial products,
and $U_\pm^o$ the original complete positive matrices,
including the entire scalar $\kappa$ factor. Their producing
formulas are the function propagate in the original SP source:
$U_\pm^o=\exp(c_\pm^{\rm bound})P_\pm^o$ with outward rounding.
Each original nonnegative factor is entrywise at least the
identity. Consequently the full products dominate every
chronological subinterval product and every source insertion
time, without exchanging matrix order.

Use $D=I_2$ for the weak norm and $D=D_4$ for the strong norm.
Set $k_D=\|DP_\pm^oD^{-1}\|_F$ and
$e_D=\|DED^{-1}\|_F$. The original scalar radial factor is
unchanged by the background variation and commutes with
the full matrix equation. Duhamel on the nonradial product
therefore proves the actual bound

$$
 \sup_{s,t}\|\mathcal U_{\pm,D}^{\,Q}(t,s)\|
 \le{\|DU_\pm^oD^{-1}\|_F\over1-\theta_{\pm,D}},
 \qquad
 \theta_{\pm,D}=k_De_D(.234)<.001 .
 \tag{NR.12}
$$

The numerator retains the saved complete positive matrix,
including its radial factor. No quotient of two norm
upper bounds is interpreted as a function lower bound.
The completed upper bounds are:

| Orientation | Weak nonradial $k$ | Strong nonradial $k$ | Weak feedback | Strong feedback | Weak full flow | Strong full flow |
|---|---:|---:|---:|---:|---:|---:|
| Reverse | 2.163851 | 2.184943 | .000113 | .000085 | 173.891176 | 175.581230 |
| Forward | 2.515703 | 2.568757 | .000131 | .000100 | 5.868691 | 5.992268 |

These flows act on (NR.4) and (NR.5), respectively. Both
include all shorter intervals, both characteristic means,
ordinary insertions and original impulses.

For standard raw Sobolev spaces note that

$$
 \|h\|_{H^{-1}}\le
 \bigl(\|Ih\|_2^2+|\Pi h|^2\bigr)^{1/2}
 \le C_I\|h\|_{H^{-1}},\qquad
 C_I=\sqrt{17}/4<1.031 .
 \tag{NR.13}
$$

The additional input/output $\kappa$ factors cost at most
$1.03/.5338$. Thus complete raw $L^2$ flows have gains
below $338.794805$ reverse and $11.562450$ forward;
the standard raw $H^{-1}$ gains are below $345.935287$
and $11.675044$.
On their common smooth domain these are the same actual
flow, and uniqueness identifies their density extensions.
Interpolation consequently gives, for every $-1\le s\le0$,

$$
 \|\mathcal U_-^Q(t,s_0)\|_{H^s\to H^s}<347,\qquad
 \|\mathcal U_+^Q(t,s_0)\|_{H^s\to H^s}<12 .
 \tag{NR.14}
$$

For ordinary sources multiply these uniform kernels by the
actual $L^1_rH^s$ norm; for $L^2_rH^s$ also pay the square
root of the true insertion interval. Impulses use the sum
of their actual norms and no length factor. Equation
(NR.14) asserts no $H^1$ smoothing.

## NR4. The root energy pays the unknown full tail explicitly

The original regular root multiplier in
[E.1--E.10](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md)
is intrinsic. Put $\varrho=r_*-r$ and

$$
 \Lambda_j=\sqrt{1+16j^2},\quad x=\varrho\Lambda_j^{2/3},\quad
 w_j^2=\kappa^2+\Lambda_j^{-2/3}e^{-x},\quad
 \theta_j=e^{-(13/10)(1-e^{-x})},\quad
 M=\operatorname{diag}(\theta/w,\theta).
 \tag{NR.15}
$$

The complete original root gates and nonmonotone weight fee
are unchanged: $-\!K/\varrho>49.1638>1$,
$\kappa^2<1.049$, $\kappa<1.025$ and
$\sqrt{1+\kappa^2}<1.432$.
The actual new angular speed obeys

$$
 |\eta_Q|
 <1.253802+7(2\,10^{-7}+3.861\,10^{-18}+\rho)<13/10 .
 \tag{NR.16}
$$

Thus the true principal cancellation E.5 applies. It retains
both root-bracket endpoints and the genuine nonmonotone
intrinsic weight term. It does not require $m_Q'$.

For $s=0,-1$ write $Z_s=\Lambda^sMh$.
The diagonal multipliers $m_{\nu,s}(\Lambda)$ satisfy

$$
 \left|\partial_{\log\Lambda}\log m_{\nu,s}\right|
                                    \le4/3 .
 \tag{NR.17}
$$

This yields an arbitrary-lag lemma. For physical frequencies
$k,n\in4\mathbb Z$, including zero, let $\ell=k-n$.
Since $\max(\Lambda_k,\Lambda_n)/\min(\Lambda_k,\Lambda_n)
\le1+|\ell|$, integration of (NR.17) and the scalar
mean-value theorem give

$$
 \left|{m_k\over m_n}\right|\le(1+|\ell|)^{4/3},\qquad
 |n|\left|{m_k\over m_n}-1\right|
       \le{4\over3}|\ell|(1+|\ell|)^{4/3}.
 \tag{NR.18}
$$

For the second inequality use
$R^{4/3}-1\le(4/3)R^{1/3}(R-1)$ and $|n|\le
\max(\Lambda_k,\Lambda_n)$. The zero input has zero drift.
Ordinary convolution Young inequalities therefore give

$$
 \|m a m^{-1}\|\le\|a\|_{A^{4/3}},\qquad
 \|[m,d]m^{-1}\partial_\phi\|
                         \le{4\over3}\|d_\phi\|_{A^{4/3}} .
 \tag{NR.19}
$$

In particular the finite coefficient lag768 used for the
old centre is not assigned to the unknown $e$.
The exact new skew scalar transport is kept inside the
energy identity.

The known compact centre satisfies the full pair bounds
$\|Q_*\|_{A^0}<6.407$ and
$\|Q_*\|_{A^{4/3}}<34.141$ from TH.
Put $b=2$, $K_+=1.049$, and

$$
 d_p=bK_+(2(6.407)\rho+\rho^2),\quad
 d_w=bK_+(2(34.141)\rho+\rho^2),\quad
                  J={d_p\over2}+{4d_w\over3}+4d_w .
 \tag{NR.20}
$$

Here $d_p$ bounds the new scalar transport energy difference,
$d_w$ bounds its complete differentiated drift in
$A^{4/3}$, and $4d_w$ bounds the sum of the two actual
diagonal reaction differences in that same algebra.
The factor4 comes from the exact diagonal coefficients
$-\beta(1+3u^2+Kv^2)$ and
$\beta(1-u^2-3Kv^2)$.

The off-diagonal local, ordered primitive and mean-rank
proofs of E.9--E.10 use the displayed Sobolev multiplier
norms, not the old finite lag. They consequently apply to
the new tail using its actual first and second derivatives.
For completeness define

$$
 \begin{gathered}
 U=.629,\quad V=6.407,\quad U_1=V_1=5.438,\quad
 U_2\le128U_1,\quad W=1.432,\quad q_+=1.025,\\
 l_0=2b\{(U+V)\rho+\rho^2\},\\
 l_1=2b\{(U_1+V+U+V_1)\rho+2\rho^2\},\\
 A=U_1+V_1,\quad \Delta A=2\rho,\\
 B=W(U+U_1)+K_+(V+V_1),\quad
 \Delta B=2(W+K_+)\rho,\\
 p_-=8b(1.031)(A\Delta B+B\Delta A+\Delta A\Delta B),\\
 n_-=4g(K_++1)\rho,\qquad g=7 .
 \end{gathered}
 \tag{NR.21}
$$

Then the entire additional negative-one growth is

$$
 \Delta G_-^{\rm tail}
 \le J+4(q_++W)(l_0+l_1)+p_-+n_-<.0035 .
 \tag{NR.22}
$$

The ordinary energy retains its full second angular
mean-rank term. Set

$$
 \begin{gathered}
 C=WU+K_+V,\quad\Delta C=(W+K_+)\rho,\\
 D=.41(U_1+128U_1)+V_1/4,\quad
 \Delta D=(.82+1/4)\rho,\\
 p_0=8b(C\Delta D+D\Delta C+\Delta C\Delta D),\quad
 n_0=4g(2K_++1)\rho .
 \end{gathered}
 \tag{NR.23}
$$

The centre alone uses its degree32 derivative bound128.
The unknown derivatives obey
$\|e_\phi\|_{A^0},\|e_{\phi\phi}\|_{A^0}\le\rho$
directly from (NR.1), without any frequency support.
The full strong growth increment is

$$
 \Delta G_0^{\rm tail}
 \le J+4(q_++W)l_0+p_0+n_0<.0135 .
 \tag{NR.24}
$$

The reader obtains the stricter directed values
$.003403$ and $.012743$ for (NR.22),(NR.24).
Add these to the already proved compact-centre increments
RTC.15/RTC.17, $.003253$ and $.006290$.
Convenient total enlargements over the original saved
root budgets are therefore

$$
                         \Delta_-=.0068,\qquad\Delta_0=.0200 .
 \tag{NR.25}
$$

These are full-frequency energy increments. No original
root integral is recomputed.

## NR5. All six complete root radii and one common Cauchy flow

Let $C_s^o(R)$ denote the original completed root constant.
Exactly as in RTC.18,

$$
 C_s^Q(R)\le
 {C_s^o(R)\over1-\Delta_s(R+\omega_r)},\qquad s=0,-1 .
 \tag{NR.26}
$$

The positive denominators cover the entire original
enclosing interval, while the actual root-to-cut source
length remains at most $R$.
The resulting strict upper bounds are:

| Exact radius | $C_0^Q$ | $C_{-1}^Q$ | $C_I C_{-1}^Q$ |
|---|---:|---:|---:|
| $1/1000$ | 4.287137 | 4.650035 | 4.793146 |
| $1/500$ | 4.665246 | 5.544115 | 5.714743 |
| $1/200$ | 6.532358 | 10.936492 | 11.273078 |
| $1/100$ | 13.918614 | 50.809730 | 52.373471 |
| $3/200$ | 32.152679 | 285.590041 | 294.379477 |
| $1/50$ | 73.607544 | 1515.158338 | 1561.789467 |

The last column retains the original completed primitive
product before applying the new denominator.
Define the actual mixed source space

$$
 \mathcal X_s=H^{s+1/3}_\phi\oplus H^s_\phi .
 \tag{NR.27}
$$

The complete root solution satisfies

$$
 \sup_{0\le\varrho\le R}\|h(\varrho)\|_{H^s\oplus H^s}
 \le C_s^Q(R)
 \left(\|h(0)\|_{\mathcal X_s}
       +\sqrt R\,\|f\|_{L^2_\varrho\mathcal X_s}
       +\sum_i\|j_i\|_{\mathcal X_s}\right).
 \tag{NR.28}
$$

For zero data use the corresponding equality/zero bound.
The second source component includes its independent
even mean. Jumps keep their original order and no length
factor. Coefficient jumps are not additional state impulses.

The same full Fourier solution realizes both endpoints
$s=0$ and $s=-1$: the regular multipliers in (NR.15)
come from one equation, and uniqueness on smooth data
identifies the extensions. Interpolation gives every
$-1\le s\le0$, with constant at most
$(C_0^Q)^{1+s}(C_{-1}^Q)^{-s}$ and the interpolated
anisotropic space (NR.27). Together with (NR.14) this
provides a common range of raw Sobolev orders across the
true cut. It does not turn a weak source into a strong one.

## NR6. Actual waist and cut density factors

The full actual density is

$$
 n_Q(r)={a_{\rm phys}(r)^2\over m_Q(r)^2},\qquad
 w=n_Q T(\kappa)h .
 \tag{NR.29}
$$

The compact centre has $M(0)=-a_{\rm phys}(0)$, but the
unknown background does not receive that identity.
Its actual mean perturbation is at most $\rho$, so

$$
 {1\over(1+\rho/a_0)^2}\le n_Q(0)
       \le {1\over(1-\rho/a_0)^2},\qquad
                   .999998<n_Q(0)<1.000002 .
 \tag{NR.30}
$$

The same saved complete radius lower bounds $a_0$ away
from zero. The new upper factor is strictly smaller
than the old positive waist factor
$1.00009320264955\ldots$ used in the complete SP
source/waist products. This compares positive numerical
budgets; it asserts no lower bound for the old physical
density from its upper ball.

At the actual fixed cut, retain every original one-sided
row and the old complete mean lower $m_l=1.117244$.
The mean change from the repaired $\delta=0$ member
is bounded by $\epsilon_m=2.001\,10^{-7}+\rho$.
Consequently

$$
 { .958234592\over(1+\epsilon_m/m_l)^2}
       <n_Q(r_c)<
 { .962284474\over(1-\epsilon_m/m_l)^2},
 \qquad
                 .958232<n_Q(r_c)<.962287 .
 \tag{NR.31}
$$

The unchanged cut bounds are
$.668124<\kappa(r_c)<.723092<1$.
Thus $\|T(\kappa(r_c))\|<1.224$ and
$n_Q(r_c)\|T(\kappa(r_c))\|<1.178$.
At the waist the saved true intrinsic bounds give

$$
                    .9616<\sqrt{\kappa(0)}<.962 .
 \tag{NR.32}
$$

The genuine cut tuple is

$$
 \mathfrak d_Q(r_c)h
   =\bigl(I[n_Q(r_c)T(\kappa(r_c))h],
                    \Pi[n_Q(r_c)T(\kappa(r_c))h]\bigr).
 \tag{NR.33}
$$

It includes the complete mean vector. Combining the
last column of the root table, its original ordinary
source product and the factor1.178 gives

$$
 \|\mathfrak d_Q(r_c)h\|
 <13.279686(B_{\rm root}+J_{\rm root})
                       +.939016F_{\rm root}
 \tag{NR.34}
$$

in the weaker root units $\mathcal X_{-1}$.
The strict forward map from the actual new waist
density tuple to (NR.33) has gain below $6.650624$;
a strict $L^1H^{-1}$ source or summed impulse has
gain below $7.332903$.
These numbers use the actual $n_Q(0)$ in the inverse
waist conversion; it is not reset to one.

No original $T_2^{-1}T_1^{-1}$ normalizer is included.
Those operators depend on further background radial
jets. The present exact unscaled characteristic route
needs neither of them and does not claim their transfer.

## NR7. Complete root-to-waist gains in both windows

There are two distinct complete output norms at the waist:

$$
 \mathcal D_-(h)=
 \bigl(\|Iw(0)\|_2^2+|\Pi w(0)|^2\bigr)^{1/2},
 \qquad
                         \mathcal D_0(h)=\|w(0)\|_2 .
 \tag{NR.35}
$$

In the weaker window root data and root impulses use
$\mathcal X_{-1}$, root ordinary sources use
$L^2_r\mathcal X_{-1}$, and strict sources/impulses
use the full raw $H^{-1}$ pair.
The original SP source products, divided by the new
weak strict denominator and root denominator (NR.26),
give

$$
 \begin{aligned}
 \mathcal D_-(h)\le{}&
 2038.695371(B_{\rm root}+J_{\rm root})
       +144.157533F_{\rm root}\\
 &+92.671633F_{\rm strict}
       +191.822390J_{\rm strict}.
 \end{aligned}
 \tag{NR.36}
$$

Here $F_{\rm strict}$ is the $L^2_rH^{-1}$ norm; the
last coefficient also applies to an $L^1_rH^{-1}$
source. The complete source injection, both means
and the original true radial length are those of SP.33.
The new waist factor is legitimately dominated by
the original positive factor by (NR.30).

In the stronger window use $\mathcal X_0$ at the root,
$L^2_r\mathcal X_0$ for root ordinary sources, and
raw $L^2_\phi$ for strict source or impulse data.
At the cut the weighted strong state has norm at most
the raw pair norm because $\kappa(r_c)<1$.
At the waist its density reconstruction costs at most
$n_Q(0)/.9616$. Use the actual strong reverse flow
from the NR3 table. This yields

$$
 \begin{aligned}
 \mathcal D_0(h)\le{}&
 1192.763571(B_{\rm root}+J_{\rm root})
       +84.341121F_{\rm root}\\
 &+90.859259F_{\rm strict}
       +188.070929J_{\rm strict}.
 \end{aligned}
 \tag{NR.37}
$$

Again the strict $L^1$ source uses the impulse coefficient.
The root ordinary coefficient pays $\sqrt{1/200}$ once.
The strict ordinary coefficient pays $\sqrt{r_c}$ once.
For clarity the positive expressions before rounding are

$$
 \begin{gathered}
 L_{0,\rm root}
   ={n_Q^+(0)\over.9616}\,
                    U_{-,0}^Q C_0^Q(1/200),\qquad
 G_{0,\rm root}=L_{0,\rm root}\sqrt{1/200},\\
 C_{0,1}={n_Q^+(0)\over.9616}\,U_{-,0}^Q(1.03),
 \qquad C_{0,2}=C_{0,1}\sqrt{r_c}.
 \end{gathered}
 \tag{NR.38}
$$

All square roots in the reader are bounded above by
strict rational squares; they are not floating-point
branch tests. The true upper budget $n_Q^+(0)$ in
(NR.30), rather than its rounded display, is used.

The two windows solve the same linearized physical
equation at the same nearby full-tail background.
Equation (NR.37) requires stronger input; it does not
improve (NR.36) for an arbitrary weak source.
An impulse at the splitting cut is assigned exactly once.
The value at that cut is the actual trace of the
propagated root solution, not an evaluation granted
to a generic radial $L^2$ function.

The positive interval can now use QN with the same
full-tail domain and its additional independent
outer-endpoint bound $\|e(R_{\rm out})\|_{A^3}\le10^{-9}$.
The root high/low matching, original low193 equations,
physical finite rows, independent physical-density
means, phase and height parameters remain their
separate coupling equations. The present result pays
both actual negative Cauchy windows in that domain,
including their common strict evolution and true
cut readout; it does not assert the missing boundary
selection or nonlinear closed family.
