# R147: selected-core C1 anchor transport and complete weak-height ports

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** On the original selected core, an actual outer-core anchor at
$L=9/10$ can be transported to $b=9/50$, in the original moving angle,
with the complete bounds
$
\begin{split}
 a_0&\le A_0+3.148\,10^{-8},\\
 a_1&\le A_1+4.312 A_0+3.6461\,10^{-5},\\
 b_1&\le B_1+1.950541 A_1+12.205365 A_0+1.41\,10^{-4}.
                                                        \tag{ACT.1}
\end{split}
$
The quantities on the left are exactly the three anchor quantities in
[WRA](R147-supplement-actual-anchor-sensitive-weak-height-receiver.md).
Those on the right compare the actual $L$-anchor with the original
raw world model in the same angle and world placement. They remain
genuine inputs. This theorem does not assign an actual cap anchor or
extend a core state bound across the cap.

Only already completed whole-domain reference geometry, nonnegative
coefficient integrals, and new exact rational combinations are used.
No old geometric ODE, residual, norm, or trial pairing is repeated.

## 1. Same state, same angle, separate cap

Write $\mathsf Q^0,F^0$ for the original raw radial frame and position
at the fixed $\eta_0$, with the exact world translation in
[R133 G.1](R133-supplement-complete-141-block-continuous-model-geometry.md).
Thus
$
 (\mathsf Q^0)_r=\mathsf Q^0 M_0,\qquad
 (F^0)_r=\mathsf Q^0 c_0,\qquad
 (\mathsf Q^0)^T\mathsf Q^0=I,\quad\det\mathsf Q^0=-1.
                                                        \tag{ACT.2}
$
Use the original selected family
$
 Q_\delta=Q_0+\delta Z,\quad \nu_\delta=\nu_0+\delta,\quad
 |\delta|\le10^{-10},\quad \eta=\eta_0
$
on $0\le r\le L$, with complete moving degrees $32,96$, as in
[the exact selected-core theorem](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md).
Its centre and direction definitions are, respectively,

    440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
    6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04

The complete repair fee is below $3.861\,10^{-18}$, and the full
physical direction pair bound is $19|\delta|$. Hence on this core
$
 \max(\|u_\delta-u_{\rm raw}\|_\infty,
      \|v_\delta-v_{\rm raw}\|_\infty)<e,\qquad e=2\,10^{-9}.
                                                        \tag{ACT.3}
$
The full even mean belongs to this state difference. A separate
reference-mean derivative is not omitted.

The complete selected connection and velocity retain
$
 d=-\beta I(u^2+Kv^2),\quad \tau=dv/m-\gamma u,\quad m=\Pi v,
$
$
 M=\Omega\!\left(\beta\tau/\gamma,\,
                  a(\gamma Kv+du/m),\,ad/m\right),
 \qquad c=(a\gamma,a\tau,0).                              \tag{ACT.4}
$
They are the equations of the
[complete moving-frame identity](R133-supplement-moving-frame-with-complete-residual-and-mean.md).
They define a passive radial model even when the centre is not a GC
solution. No residual-free angular equation is imposed.

On $[b,L]$ the compact metric weight and its derivative are zero.
The selected and raw metric coefficients are therefore exactly the
same there, including the endpoints. Only the actual state difference
enters $\Delta M=M_\delta-M_0$ and $\Delta c=c_\delta-c_0$.
Nothing here applies (ACT.3) on $[L,25/8]$. A true M cap, its angle
bridge, and its world placement must provide the $L$-anchor.

Start the selected radial model from an orthogonal, correctly oriented
frame $\widehat{\mathsf Q}_L$ and position $\widehat F_L$, in the
same original angle, and define
$
\begin{split}
 A_0&=\|e_z^T(\widehat{\mathsf Q}_L-\mathsf Q^0_L)\|_\infty,\\
 A_1&=\|\partial_\phi[e_z^T
                  (\widehat{\mathsf Q}_L-\mathsf Q^0_L)]\|_\infty,\\
 B_1&=\|\partial_\phi[e_z^T(\widehat F_L-F^0_L)]\|_\infty .
                                                        \tag{ACT.5}
\end{split}
$
Frame bounds use the Euclidean row norm on the entire circle.
A constant vertical position displacement is absent from $B_1$
because the height row pairs it with a true zero-mean coordinate
derivative. A varying position port is retained in section 7.

## 2. Whole-reference first derivatives without new integration

The completed original angular certificate covers every
$r\in[0,25/8]$, the complete circle and every original interface.
Its [actual record](../notes/2026-11-14-R133-final-complete-angular-defect.md)
gives
$
 \|\mathsf Q^0_{\phi\phi}\|_{\rm op}<4.646383,\qquad
 |F^0_{\phi\phi}|<5.970523.                               \tag{ACT.6}
$
The original whole native has 7,722 common boxes, all 6,143 interfaces,
6,871,825 bytes, and SHA256

    7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90

For every fixed unit vector $v$, twice differentiating
$|\mathsf Q^0v|^2=1$ gives
$
 |\mathsf Q^0_\phi v|^2
 =-\langle\mathsf Q^0v,\mathsf Q^0_{\phi\phi}v\rangle
 \le\|\mathsf Q^0_{\phi\phi}\|_{\rm op}.
$
Thus, with $G=539/250=2.156$,
$
 \|\mathsf Q^0_\phi\|_{\rm op}<G,\qquad 4.646383<G^2.
                                                        \tag{ACT.7}
$
This holds for the actual determinant-$-1$ frame.

The complete 141-block result gives $|F^0|<1.275713422847$.
The Banach-valued centred-difference bound
$\|f'\|\le\|f\|/h+(h/2)\|f''\|$, optimized in $h$, yields
$
 |F^0_\phi|^2\le2\|F^0\|_\infty\|F^0_{\phi\phi}\|_\infty<16.
                                                        \tag{ACT.8}
$
World vectors are taken on the full periodic circle; a quarter-turn
seam is not replaced by an unrotated periodic seam.

The completed nonnegative path-length bound is
$
 \int_0^{25/8}|c_0|\,dr<C,\qquad C=1.950540.
                                                        \tag{ACT.9}
$
Consequently, for $r,s\in[b,L]$,
$
 |F^0(r)-F^0(s)|<C,\qquad
 |\partial_\phi(F^0(r)-F^0(s))|<8.                       \tag{ACT.10}
$
Only a nonnegative whole-domain upper is restricted to a subinterval.

## 3. Complete selected connection budgets

The completed
[C0 state response](R133-supplement-complete-C0-state-and-nu-geometry-response.md),
(C.13)--(C.18), supplies nonnegative coefficients with
$
 \int L_{\Omega,u}<15.736315,\qquad
 \int\left(L(s)\int_s^R L_{\Omega,u}(t)\,dt
                         +L_{f,u}(s)\right)ds<30.196406.
$
The second nonnegative integrand also bounds the integral of
$L_{f,u}$. This is an upper bound on a summand, not subtraction of
two upper bounds. Applying the actual finite-difference formulas
only on the core segment gives
$
 \int_b^L\|\Delta M\|_{\rm op}\,dr
 \le D:=15.736315e={3147263\over10^{14}},
$
$
 \int_b^L|\Delta c|\,dr
 \le E:=30.196406e={15098203\over250000000000000}.
                                                        \tag{ACT.11}
$
There is no metric-parameter fee on this segment, because that metric
difference is exactly zero.

At each fixed radius the selected $M,c$ have complete angular
degree at most $288$ in the original $4\mathbb Z$ variable. The
primitive of the full quadratic shape, multiplication by the state,
and the true radial mean denominator are included. The raw degree
is at most $96$. Bernstein's inequality, applied by norm duality to
vectors and operator-norm matrices, therefore yields
$
 \int_b^L\|\partial_\phi\Delta M\|\,dr\le ND,\qquad
 \int_b^L|\partial_\phi\Delta c|\,dr\le NE,\qquad N=1152.
                                                        \tag{ACT.12}
$
This degree belongs only to the difference of two specified centres.
It is not a truncation of a true TC variation or a future nonlinear
correction.

## 4. Exact relative-frame identity

Let $\widehat{\mathsf Q},\widehat F$ be the selected passive model
with the $L$-ports above, and set
$
 P=\widehat{\mathsf Q}(\mathsf Q^0)^T,\quad
 B=\mathsf Q^0\Delta M(\mathsf Q^0)^T,\quad
 y=e_z^TP,\quad d=y-e_z^T .
$
The exact equations are
$
 P_r=PB,\quad y_r=yB,\quad |y|=1,\quad B^T=-B,\quad P\in SO(3).
                                                        \tag{ACT.13}
$
Writing
$d_L=e_z^T(\widehat{\mathsf Q}_L-\mathsf Q^0_L)
(\mathsf Q^0_L)^T$, one has
$
 |d_L|\le A_0,\qquad |(d_L)_\phi|\le A_1+GA_0,\qquad
 \int_b^L\|B_\phi\|\,dr\le(N+2G)D=:H .
$
Orthogonal propagation, without an exponential factor, gives
$
 |d(r)|\le A_0+D,\qquad
 |y_\phi(r)|\le A_1+GA_0+H.                              \tag{ACT.14}
$
The actual vertical frame difference is $d\mathsf Q^0$, so
$
 a_0\le A_0+D,\qquad
 a_1\le A_1+2GA_0+(N+3G)D.                             \tag{ACT.15}
$
The derivative of a genuine angular world gauge is precisely in
$A_1$; it has not been set to zero.

## 5. Position derivative and the complete difference kernel

For $r\in[b,L]$, put
$
 V(r,s)=F^0(r)-F^0(s),\qquad
 Z(s,r)=\mathsf Q^0(s)\Delta c(s)+B(s)V(r,s).
$
Integration by parts using $P_r=PB$ gives the exact identity
$
 e_z^T(\widehat F(r)-F^0(r))
 =e_z^T(\widehat F_L-F^0_L)+d_L V(r,L)
                        +\int_L^r y(s)Z(s,r)\,ds.         \tag{ACT.16}
$
It also follows by differentiation in $r$ and the actual initial
value. It precedes every norm estimate.

With
$
 T_0=E+CD,\qquad
 T_1=(N+G)E+\{C(N+2G)+8\}D,                              \tag{ACT.17}
$
the complete kernel satisfies
$
 \int_b^L|Z|\,ds\le T_0,\qquad \int_b^L|Z_\phi|\,ds\le T_1.
$
Both endpoint derivatives in $V_\phi(r,s)$ are retained. It follows
from (ACT.14) and differentiating (ACT.16) that
$
\begin{split}
 b_1\le{}&B_1+(C+T_0)A_1+(GC+8+GT_0)A_0\\
         &+T_1+(N+2G)DT_0.                              \tag{ACT.18}
\end{split}
$
In particular the angular derivative of the anchor difference times
the relative displacement remains present. No $C^0$ port or radial
body $L^2$ norm has been converted into a $C^1$ port or trace.

All original radial coefficient interfaces are admitted one-sided.
The passive frame, position and their angular derivatives are
continuous through them, so the identities concatenate exactly.
The original angular certificate paid all of its own connection
defect jumps. An independently imposed geometric jump would be an
additional port, not an absent term.

The exact new rational values include
$
\begin{split}
 T_0&={608907178601\over5000000000000000000},\\
 (N+3G)D&={911500868271\over25000000000000000},\\
 T_1+(N+2G)DT_0
 &={8808682129357237512060772046957
       \over62500000000000000000000000000000000}.
\end{split}
$
They imply (ACT.1). The middle value is slightly greater than
$3.6460\,10^{-5}$; the valid outward upper used here is
$3.6461\,10^{-5}$.

## 6. Direct original weak-height consumer

Substitution in the already proved WRA estimate gives
$
\begin{split}
 |\ell_{\rm height}(h)|\le{}&
 (94002+196118A_0+21484A_1+4590B_1)(D_*+J_-)\\
 &+(6651+13878A_0+1521A_1+325B_1)F_-\\
 &+(3001+7384A_0+851A_1+210B_1)F_{\rm st}\\
 &+(8851+18459A_0+2023A_1+432B_1)J_{\rm st},
                                                        \tag{ACT.19}
\end{split}
$
plus the independent varying-anchor ports in section 7.

All four source units are unchanged: $D_*+J_-$ is the true root
Cauchy/interface input, $F_-$ uses the original root
$H^{-2/3}\oplus H^{-1}$ norm, and $F_{\rm st},J_{\rm st}$ use the
original strict $H^{-1}\oplus H^{-1}$ norm, ordinary radial $L^2$
integration, and genuine strict atoms. Both source means are kept.

No new numerical propagation target is needed between an admitted
actual $L$-anchor and WRA. The three actual $L$-quantities and the
complete TC source quantities remain necessary. A candidate phase
row or an incomplete residual prefix does not supply a true-column
error bound.

WRA's fourfold integration by parts requires the same genuine periodic
vertical observables. It applies to the admitted axially placed
fourfold world. A tilted placement or unmatched angular seam retains
the corresponding original boundary functional until its periodicity
is proved. An unqualified angle, frame, or phase change is not part of
(ACT.19).

## 7. Exact varying-port transfer and adjoint

Let $A_\ell,x_\ell$ be the selected relative frame and position from
$L$ to $b$, with $A_\ell(L)=I,x_\ell(L)=0$, evaluated below at
$b$. Let $A_s,x_s$ be the selected relative objects from $b$
to the waist. All are complete curves in the same original angle.

Write the genuine external variations at $L$ as
$
 \dot{\mathsf Q}_L=K_L\mathsf Q_L,\quad K_L^T=-K_L,\qquad
 \dot F_L=Y_L,
$
and the body variations on the long core piece as
$
 \dot A_\ell A_\ell^T=[u_\ell]_\times,\qquad \dot x_\ell=y_\ell .
$
Then the exact transferred ports are
$
\begin{split}
 K_b&=K_L+\mathsf Q_L[u_\ell]_\times\mathsf Q_L^T,\\
 Y_b&=Y_L+K_L\mathsf Q_Lx_\ell+\mathsf Q_Ly_\ell .
                                                        \tag{ACT.20}
\end{split}
$
Because $\det\mathsf Q_L=-1$,
$
 \operatorname{ax}(K_b)=\operatorname{ax}(K_L)-\mathsf Q_Lu_\ell .
$
The sign is not the proper-frame sign.

The full independent waist port in WRA is thus
$
\begin{split}
 \Pi J\,e_z^T(Y_b+K_b\mathsf Q_b x_s)
 =\Pi J\,e_z^T\big\{&
 Y_L+K_L\mathsf Q_L(x_\ell+A_\ell x_s)\\
 &+\mathsf Q_L(y_\ell+u_\ell\times A_\ell x_s)\big\}.
                                                        \tag{ACT.21}
\end{split}
$
Both angular curves, the full physical $J$, and the complete frame
and position columns are retained. They are not replaced by means.

With $w=\mathsf Q_L(x_\ell+A_\ell x_s)$, the exact pullback to the
two external $L$-ports is
$
             J e_z,\qquad w\times(J e_z),                \tag{ACT.22}
$
acting on $Y_L$ and the world axial vector $\operatorname{ax}K_L$,
respectively. The long-core body contribution is the second line of
(ACT.21), and needs its own genuine receiver or signed carrier.
There is no free endpoint trace from a body norm, and no world port is
set to $I$, zero, or a separately fitted angle-dependent gauge.

## 8. New arithmetic and scope

The companion
[saved-bound combination](../scripts/fourfold_codazzi_selected_core_anchor_transfer_saved_bounds.py)
contains 19 distinct exact rational comparisons: two derivative
consequences of old whole geometry, five selected transfer bounds,
and twelve coefficients in (ACT.19). All 19 hold. The initial too-low
rounding $3.6460\,10^{-5}$ was rejected by its exact comparison and
raised to $3.6461\,10^{-5}$; only that corrected comparison and the
four affected new bias combinations were evaluated again. No old
scientific target was repeated.

This supplies the selected-core transport and its original
weak-height consumer. Actual cap matching, full TC residual coverage,
the full bordered inverse, and final nonlinear/geometric closure are
not asserted.
