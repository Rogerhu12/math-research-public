# R149 H96: complete physical height on all original finite trials

2026-11-28, visible-exact-astra-b0d5a16-20261128.

This gives seven new executable whole-row targets on the **unchanged**
96 original TC trials. It uses the entire selected member, the actual
cap world-anchor bounds, the physical waist Jacobian and its variation.
The original signed phase row is consumed only after this height row
is formed. The new numerical targets are not asserted completed here.

The trial columns still have their original differential residuals.
Nothing in this construction sets those residuals to zero or declares
the full positive/negative/mean/parameter Schur complement invertible.

## H96.1. Same complete inputs and actual readout

Use the exact original selected member and metric, including the implicit
true root, all repaired mean coefficients and the two independent means.
The original trial definition and its four complete arrays are those of
[P96](R149-supplement-complete-phase-row-on-original-finite-trials.md).
The original whole six-target P96 output is
[run 45926971089/1](../notes/finite_trial_phase_ci/run-45926971089-1/actual-finite-trial-phase.json).
In particular, retain its full 96-vector

$$
 H_j\ge\int_0^{r_*}\|T_j(r)\|_{L^2\oplus L^2}\,dr,
 \qquad 1\le j\le96,                                      \tag{H96.1}
$$

and its complete signed phase row. No old phase, trial norm, residual,
strip or propagation target is recomputed.

Write $b=9/50$. The entire short relative profiles are the original
[RH](R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md)
and [RHI](R147-supplement-certified-relative-parameter-frame-and-position-carriers.md)
objects. Their exact equations are

$$
 A'=AM,\quad A(b)=Id,\qquad x'=Ac,\quad x(b)=0 .           \tag{H96.2}
$$

The real matrix $M$ is skew, so $A(r)\in SO(3)$ even though the selected
curvature fields have their original unsolved Codazzi residual.
For a homogeneous curvature direction $h=(h_1,h_2)$, with zero relative
terminal data and no intrinsic parameter change, let $U,y$ be the first
frame/position variations in RH's relative world frame. Then

$$
 U'=A\dot M A^t,\quad y'=UAc+A\dot c,\quad U(b)=0,\quad y(b)=0,
$$

and exact integration in the original orientation gives

$$
 y(0)=\int_0^b A\dot M A^t\{x(r)-x(0)\}\,dr
                   -\int_0^b A\dot c\,dr .                \tag{H96.3}
$$

At the waist put $m=\Pi v$, $J=v/m$, $\mu_h=\Pi h_2$ and

$$
 g_h=h_2(0)/m-v(0)\mu_h/m^2,\qquad \Pi g_h=0.            \tag{H96.4}
$$

For the actual short world anchors $q_b=e_z^t\mathsf Q_b$, $f_b=e_z^tF_b$,
the full homogeneous physical mean-height readout is

$$
 \mathcal L_b[h]=\Pi Jq_b y(0)+\Pi g_h f(0),\qquad
 f(0)=f_b+q_bx(0).                                      \tag{H96.5}
$$

This is [PH](R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md)
and [WRC](R147-supplement-complete-reference-world-height-and-original-negative-receiver.md),
with its coordinate term retained. A fixed constant can be subtracted
from $f(0)$ exactly by (H96.4). Independently varying $Y_b,K_b$, direct
metric terms and any original geometric impulses remain separate ports.

## H96.2. A canonical adjoint requiring only three relative factors

Set $\chi=A(0)e_1$ and define the auxiliary canonical body functional

$$
 \mathcal L_{can}[h]=\Pi J\chi^t y(0).                    \tag{H96.6}
$$

It does not reset the actual world frame. The difference from that
frame and the complete coordinate term are paid in H96.5 below.
Set $d_x=x(r)-x(0)$ and

$$
 v_f=JA(r)^t\chi,\qquad
 (r_t,-r_k,r_p)^t=JA(r)^t(d_x\times\chi).                 \tag{H96.7}
$$

The identity behind (H96.7) is the **exact** $SO(3)$ covariance
$A^td_x\times A^t\chi=A^t(d_x\times\chi)$, applied before approximation.
An approximate polynomial matrix is never assumed orthogonal. Thus
the centre calculation needs three relative factors, with their full
errors, instead of forming four unnecessary matrix factors.

To distinguish the metric scalar from the position difference, write
$d_m=-\beta I(u^2+Kv^2)$. The connection is

$$
 p=(\beta/\gamma)d_mv/m-\beta u,\quad
 k=a(\gamma Kv+d_mu/m),\quad t=ad_m/m,
$$

$$
 M=\begin{pmatrix}0&-p&-k\\p&0&-t\\k&t&0\end{pmatrix},
 \qquad c=(a\gamma,a(d_mv/m-\gamma u),0)^t.               \tag{H96.8}
$$

Substitution into (H96.3) gives exactly PH.20--21:

$$
\begin{aligned}
 k_\tau&=(\beta/\gamma)r_p-a(v_f)_2,\\
 k_d&=k_\tau v/m+ar_ku/m+ar_t/m,\\
 k_1&=-\gamma k_\tau+ar_kd_m/m,\\
 k_2&=k_\tau d_m/m+ar_k\gamma K,\\
 k_\mu&=-k_\tau d_mv/m^2-ar_kd_mu/m^2-ar_td_m/m^2,\\
 \ell_1&=k_1+2\beta uI(k_d),\\
 \ell_2&=k_2+2\beta KvI(k_d)+\Pi k_\mu,\\
 \mathcal L_{can}[h]&=\int_0^b\Pi(\ell_1h_1+\ell_2h_2)\,dr .
\end{aligned}                                                   \tag{H96.9}
$$

In particular the mean of $k_\mu$ is retained. The sign in the two
primitive terms uses $I^*=-I$. The physical $4n$ convention and the
normalized angular measure are exactly the original ones.

## H96.3. Whole-cell, full-frequency bounds from the saved RHI output

The complete original RHI output
[45933988440/1](../notes/relative_nu_carriers_ci/run-45933988440-1/actual-relative-nu-carriers.json)
certifies normalized grid errors below $2.788351\,10^{-9}$ and
$1.424040\,10^{-9}$ for the joint $A$ and $x$ profiles, respectively.
These are whole-cell bounds: RHI's source integrals and propagated
incoming errors are nonnegative and cumulative. The final bound thus
dominates every point of every one of the 2847 original cells, as well
as the final endpoint. No midpoint sampling replaces this statement.

The same original analytic estimates give full interpolation errors
below $3.131\,10^{-26}$ and $4.181\,10^{-27}$. Although RHI.8 only
needed an $L^2$ conclusion, its explicit $4Bq^{N/2}/(1-q)$ majorant is
the sum of the two Fourier tails and their aliases. It consequently
also bounds their $C^0$ error, uniformly throughout each cell.

Use the original real trigonometric interpolant at all 2048 points,
with the real Nyquist coefficient split equally between modes
$-1024$ and $1024$. Parseval gives an $L^2$ norm no greater than the
normalized grid error. Its 2049 complex coefficients give
$\|p\|_\infty\le\sqrt{2049}\|p\|_2<46\|p\|_2$.
Consequently the new complete uniform bounds are

$$
 \|A-\widehat A\|_{C^0}<E_A:=1.3\,10^{-7},\qquad
 \|x-\widehat x\|_{C^0}<E_x:=6.6\,10^{-8}.                \tag{H96.10}
$$

The Frobenius/Euclidean joint bounds imply these bounds for every
component. RH also gives $\|c\|_\infty<19/5$, hence
$\|x\|_\infty<(19/5)b=.684$. Thus the finite centre components have
uniform norms at most $1+E_A$ and $.684+E_x$.

Necessary carrier reconstruction follows the exact original recipes.
It must match the original four complete TC array SHA256 receipts,
the NP receipts, and the original RHI full18 endpoint and cumulative
coefficient-chain SHA256. A passive tap stores only the first twelve
original degree6 radial coefficient profiles, in the private shape
`[2847,7,2048,12]`, retaining the original forward cell order and
variable $(r_{right}-r)/(r_{right}-r_{left})$. The all18 propagation is
unchanged and checked in full. No old residual or strip reducer runs.

The tap is 3918200832 bytes. The four full TC arrays are 4548105216
bytes. They are reproducible private job carriers, not new published
data; their complete identities and recipe are in the owner receipt.

## H96.4. Unrestricted-error algebra and exact contraction

The new separate 8192-point algebra embeds both Fourier signs and the
entire real Nyquist coefficient. The original 1024-point selected
coefficient algebra is unchanged. All finite products in (H96.9) are
formed before projection onto the original 193 trial coordinates.
Every intermediate angular degree is bounded by3584, and
$2(3584)<8192$, so none of these finite products aliases.

For each factor retain a finite polynomial centre, a bound $N$ for its
uniform norm on the whole current radial interval, and a genuine
unrestricted angular $C^0$ error $e$. Products use

$$
 e_{fg}\le N_fe_g+N_ge_f+e_fe_g.                         \tag{H96.11}
$$

The error from (H96.10) has **no finite-frequency support**. No angular
derivative is applied to it. The full periodic primitive has

$$
 \|I:L^\infty\to L^\infty\|=\pi/8<2/5,                \tag{H96.12}
$$

so its complete primitive error is at most $(2/5)e$. The mean has norm
one. A genuinely radial scalar error has zero angular primitive;
otherwise its entire error remains. In particular the Wiener-only
$1/4$ estimate is not used for the unknown relative-profile error.

All selected coefficient errors are those of the original RHI fields:
the complete repaired background and its $2\,10^{-9}$ selected-state
difference, all scalar Taylor remainders, true intrinsic parameter
fees, reciprocal mean and reciprocal $\gamma$ bounds. The actual
metric-bump seam is a cell boundary. Their finite-support Wiener
remainders imply $C^0$ remainders when embedded in the new algebra.

Intersect the entire RHI cover of $[0,b]$ with the unchanged TC cells.
The trial factory restores all original true-root septic coefficients
and restricts them exactly to each intersection. Since $b<r_*$, no
root sliver is omitted in this body integral. Write the common local
variable as $t\in[-1,1]$. If the row polynomial coefficient is $a_j$
and the trial coefficient is $h_k$, their exact radial contribution is

$$
 \sum_{j+k\ {
m even}} {r_{right}-r_{left}\over j+k+1}
                         \langle a_j,h_k\rangle.          \tag{H96.13}
$$

The sine and cosine coefficients use the original real orthonormal
basis, including the even constant. This contraction is performed on
all 96 columns. The unknown uniform adjoint error is received by the
whole saved vector (H96.1): if $e_*$ is the maximum of
$e_{\ell_1}+e_{\ell_2}$ over the complete cover, then

$$
 |\mathcal L_{can}[T_j]-\widehat L_j|\le e_*H_j.          \tag{H96.14}
$$

This avoids redoing the already completed original trial norm targets.
The complete signed integral prefix, actual coverage endpoint,
maximum error, degrees and intersection count are retained. A partial
prefix is never published as a complete height row.

## H96.5. Waist coordinate term and actual world-frame correction

The original waist mean obeys $|m|>16/15$, and $\|v\|_\infty<18/5$.
Put $\varepsilon=2\,10^{-9}$ for the entire selected-state difference.
The original degree32 nominal waist field and mean give $\widehat J$,
with mean exactly one, and each complete $\widehat g_j$ in (H96.4),
with mean exactly zero. Direct subtraction with both denominator
bounds yields

$$
 \|J-\widehat J\|_\infty
 \le\left({15\over16}+{18\over5}({15\over16})^2\right)\varepsilon
 ={525\over128}\varepsilon,                              \tag{H96.15}
$$

$$
 \|g_j-\widehat g_j\|_2
 \le\left(2({15\over16})^2+2{18\over5}({15\over16})^3\right)
       \varepsilon\|T_{j,2}(0)\|_2
 ={7875\over1024}\varepsilon\|T_{j,2}(0)\|_2.             \tag{H96.16}
$$

Only the **known** original finite waist vector is used in Parseval;
no unknown trial correction is supplied with a frequency cutoff.
This defines the new complete96-vector $G_j\ge\|g_j\|_2$.

RH's full $\dot M$ and $\dot c$ receivers are both below $5/2$.
Equation (H96.3), or its original double-integral form, gives

$$
 \|y_j(0)\|_2\le {5\over2}(1+{19\over5}b)H_j=4.21H_j,
 \qquad\|Jy_j(0)\|_2\le14.20875H_j,                    \tag{H96.17}
$$

using $J<27/8$. WRC's actual reference waist row and height satisfy
$\|q_0-e_1^t\|_\infty<k_q=.000108627$ and
$\|f_0\|_\infty<k_f=.000232743$.
Orthogonality transfers the former difference exactly to the relative
row $q_b-\chi^t$. Thus the complete reference height row lies in

$$
 L^{ref}_j\in L^{can}_j+
 [-1,1]\{k_q(14.20875)H_j+k_fG_j\}.                     \tag{H96.18}
$$

For the same actual admitted cap and selected passive core,
[CW](R147-supplement-actual-cap-world-anchors-and-supported-nu-height.md)
certifies $a_0=.002235$, $p_0=.004288$. Its full cap-anchored row is
therefore enclosed by

$$
 L^{cap}_j\in L^{can}_j+[-1,1]\{
 (k_q+a_0)(14.20875)H_j+(k_f+p_0+.684a_0)G_j\}.           \tag{H96.19}
$$

The second term pays the entire physical-coordinate variation. The
fixed constant removed from $f_b$ cancels only because $\Pi g_j=0$.
The varying translation $Y_b$ and rotation $K_b$ remain their original
independent columns. No actual core/cap curvature match follows from
this passive readout calculation.

## H96.6. Complete height-reduced principal phase and publication

[HP](R147-supplement-actual-height-pivot-and-complete-phase-mean-transfer.md)
uses the same unnormalized strict particular and proves
$\rho_P=c_P/c_H\in[-1.543,-1.5208]$. With the entire saved original
signed P96 row $P_j$, the new height-reduced principal row is

$$
 \widetilde P_j=P_j-\rho_P L^{cap}_j.                     \tag{H96.20}
$$

Use whole interval multiplication; no correlation is invented.
The original regular defect of the strict particular, conjugacy
$E'a$ term, direct parameter terms and independent world ports remain
the other entries in HP's exact reduced system.

For each new complete cap-height and reduced-phase row choose all96
exact dyadic centres, save the entire signed ball vector, read it back,
and then give the joint Euclidean radius relative to those **same**
centres. The seven whole targets, in order, are:

1. Complete canonical signed height row96.
2. Complete original waist-Jacobian variation norm vector96.
3. Complete reference signed height row96.
4. Complete actual-cap signed height row96 and all exact centres.
5. Its whole joint radius.
6. Complete height-reduced principal phase row96 and all exact centres.
7. Its whole joint radius.

The companion [math source](../scripts/fourfold_codazzi_finite_trial_height_math.py)
performs the new contraction; the separate owner admits all original
P96/RHI/NP/SB whole objects before importing numerical libraries.
Its nine rational comparisons are new consequences of the complete
saved inputs. They were evaluated once and all passed, with no numerical
library imported and no old scientific target evaluated. Numerical output
is usable only after the entire new seven-target receipt succeeds.
The true PDE corrections, complete finite/high/mean/parameter square,
nonlinear core construction and final closed fixed-metric family
remain separate obligations.
