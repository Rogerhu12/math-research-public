# R147 CW: actual cap world anchors and the supported parameter height

2026-11-28, visible-exact-astra-b0d5a16-20261128 / cap_world.

**Proved for the actual reflected M cap in RA's axial world.** Its
genuine frame and position at $L=9/10$, in the original moving angle,
have the three vertical comparison bounds

$$
 A_{0,L}<0.002234557,\qquad
 A_{1,L}<0.005399,\qquad B_{1,L}<0.009528.             \tag{CW.1}
$$

These are actual cap outputs. Continuing the original selected
passive core from this anchor gives, at $b=9/50$,

$$
 a_0<0.002235,\qquad a_1<0.015072,\qquad b_1<0.04748,
 \qquad p_0<0.004288,                               \tag{CW.2}
$$

where $p_0$ is the vertical position difference modulo one constant.
Thus WRA's original weak-height receiver now has the actual constants

$$
 |\mathcal L_b(h)|
 <94600(D_*+J_-)+6693F_-+3024F_{\rm st}+8907J_{\rm st},
                                                               \tag{CW.3}
$$

with its independent varying-anchor port retained.

For the precise NP particular whose entire exterior is fixed,
that varying port is zero by construction and uniqueness. The
complete physical mean-height parameter entry in this actual
cap-anchored passive model satisfies

$$
 \boxed{\quad -0.02547<\mathcal L_{\mathrm{cap},\nu}
                         <-0.02513<0.\quad}           \tag{CW.4}
$$

Its scalar reciprocal has absolute value less than 40. This is a
particular height entry. The incoming correction, full finite/high
Schur, actual core/cap curvature matching, and final nonlinear
closed surface remain separate problems.

## 1. Domain, single world placement and comparison object

Use the following already completed inputs:

- [M: actual two-input cap](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md);
- [RA: its actual long $R$-anchor](R133-supplement-actual-long-cap-R-anchor-and-complete-vertical-C1-bounds.md);
- [RB: exact nonlinear physical-to-moving comparison](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md);
- [C: complete $C^0$ geometry response](R133-supplement-complete-C0-state-and-nu-geometry-response.md);
- [the repaired cap coefficient table](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md);
- [ACT: selected-core anchor transport](R147-supplement-selected-core-C1-anchor-transfer-and-weak-height-ports.md);
- [WRA: actual-anchor weak height](R147-supplement-actual-anchor-sensitive-weak-height-receiver.md);
- [AWH: the completed physical mean-height calculation](R147-supplement-actual-complete-reference-world-height-and-anchor-budget.md).

Fix the original $\eta_0$, all positive-cap intrinsic data, and the
actual interval $[L,R]=[9/10,25/8]$. The inputs are real reflected
M data: the nonmean $\gamma$ and normalized nonmean $f_B$ are even,
and the solution has $B$ odd and $C$ even. We use an admitted
finite-regularity M solution, including the actual selected SCAP
composition. No regularity is inferred merely from a zero-width
$A^0$ input bound. All the value estimates below are uniform on
M's original product domain

$$
 \|\gamma\|_{A^0}<10^{-9},\qquad
 \|f_B\|_{\dot A^2}<2^{-60},\qquad
 \|W_*-\widehat W\|_{X_0}\le\rho=3\,10^{-6}.          \tag{CW.5}
$$

The actual $C$ mean and the mean-height span are retained. The
reflection makes the actual $B$ mean zero; it is not discarded by
a gauge or by a mean-free projection.

Write $U^0=(u^0,v^0)$ for the raw moving candidate,
$\widehat U$ for its exact continuous repair, and $U_*$ for the
actual cap's moving readout. The original raw world frame and
position are $\mathsf Q^0,F^0$. Geometric frames are denoted by
$\mathsf Q$ so that they are not confused with a moving curvature
pair. The absolute frames have determinant $-1$.

Take the actual cap's $R$-anchor from RA, in the same original
axial world orientation. A single height translation $\lambda$
remains allowed. In vertical observations RA gives

$$
 \|e_z^T(\mathsf Q_{*,R}-\mathsf Q_R^0)\|_\infty<10^{-12},
 \qquad
 \|e_z^T(F_{*,R}-F_R^0)+\lambda\|_\infty<6\,10^{-21}.
                                                               \tag{CW.6}
$$

No angle-dependent world rotation is made. A different fixed tilt
would have RA.24's additional explicit ports and is not included
in the numerical constants (CW.1)--(CW.4).

On the cap the geometric fields are the actual M solution. Below
$L$ continue the selected passive radial model using the same
actual cap frame and position as its $L$ data, and the original
selected state $Q_{\delta_*}=Q_0+\delta_*Z$. The selected state
estimate is used only on $[0,L]$. The normalized moving label
$\phi$ is the original one on each side; no further physical
phase shift or fitted world gauge is inserted.

This defines the reference model required for the parameter and
weak-height rows. It does not assert the remaining curvature
match at $L$. Until that match holds, this continuation is a
passive core attached to an exact cap, rather than an exact
isometric immersion across the interface. The reference-height
functional and its derivatives are nevertheless defined by the
same exact passive equations as WMR, WRC and ACT.

## 2. A true moving $C^0$ cap estimate from the complete physical ball

Use RB with $\delta=0$ on the cap. Put
$h_B=B_*-\widehat B$ and $h_C=C_*-\widehat C$.
The complete changing-mean inverse-angle identity RB.11--14 gives

$$
 \|\Theta_*-\widehat\Theta\|_\infty
       <4\|h_C\|_{L^2}\le4\|h_C\|_\infty.              \tag{CW.7}
$$

In particular this is the genuine nonlinear inverse angle, with
its complete mean and reflection-fixed constant. At the same
physical angle, the reciprocal identity in RB.15 holds pointwise:

$$
 \left|\frac{B_*}{C_*}-\frac{\widehat B}{\widehat C}\right|
 +\left|\frac1{C_*}-\frac1{\widehat C}\right|
 \le7|h_B|+43|h_C|.                                    \tag{CW.8}
$$

The known function
$F_0(\theta)=(\widehat B/\widehat C,1/\widehat C)$ has
the sum of its two global derivative suprema less than 1 by
RB.8. Decompose the actual moving difference exactly as

$$
 U_*-\widehat U
  =(F_*-F_0)\circ\Theta_*
       +F_0\circ\Theta_*-F_0\circ\widehat\Theta .       \tag{CW.9}
$$

Composition does not enlarge a supremum norm on the real circle.
Using (CW.7) only on the known second term, (CW.8)--(CW.9) yield

$$
 \|u_*-\widehat u\|_\infty+
 \|v_*-\widehat v\|_\infty
 \le7\|h_B\|_\infty+47\|h_C\|_\infty
 \le47\rho=0.000141.                                  \tag{CW.10}
$$

There is no measure-conversion factor in a supremum norm. The
factor $8/5$ used for RB's $L^2$ estimate is not needed here.
No derivative of the unknown cap correction or unknown inverse
angle occurs.

The complete repaired-cap table gives
$\|\widehat U-U^0\|_{A_{1/32},\mathrm{pair}}
 <4.832\,10^{-18}<5\,10^{-18}$. Therefore

$$
 \max(\|u_*-u^0\|_\infty,\|v_*-v^0\|_\infty)
 <e:=0.000142<10^{-3}.                                \tag{CW.11}
$$

The full even mean is part of (CW.10)--(CW.11). This estimate is
pointwise on the whole cap. It does not assert a moving Fourier
module bound, a small angular derivative of the unknown state,
or the final $10^{-4}$ state ball.

## 3. Complete vertical propagation from the actual $R$-anchor

C's comparison has a vertical-row version with exactly the same
constants. To see this without replacing a vertical error by an
unpaid full-frame error, let

$$
 q_*=e_z^T\mathsf Q_*,\qquad q_0=e_z^T\mathsf Q^0,
 \qquad \Delta M=M_*-M_0.
$$

Both rows have norm 1. The exact equation for their difference is

$$
 (q_*-q_0)_r=(q_*-q_0)M_0+q_*\Delta M.                \tag{CW.12}
$$

Orthogonal variation of constants gives the same integral bound
as C.16 with the initial vertical-row error in place of $b_Q$.
For vertical position use the full identity

$$
 (e_z^TF_*-e_z^TF^0)_r
           =(q_*-q_0)c_0+q_*(c_*-c_0).               \tag{CW.13}
$$

The same ordered double integral in C.17 applies. It preserves
both state means, every ordinary interval and all reference
coefficient interfaces. There is no exponential Gronwall fee.

On the actual cap the metric is unchanged, so (CW.6), (CW.11)
and the already paid nonnegative integral coefficients give

$$
 \begin{split}
 A_{0,L}&<10^{-12}+15.736315e<0.002234557,\\
 \inf_c\|e_z^T(F_{*,L}-F_L^0)-c\|_\infty
 &<6\,10^{-21}+1.950540\,10^{-12}+30.196406e\\
 &<0.004287890.
 \end{split}                                             \tag{CW.14}
$$

The constant chosen in the second line is $c=-\lambda$ from
the same actual $R$-anchor. This does not reset the cap's mean
height at $L$.

The whole cap-anchored passive reference on $[0,R]$ has state
error below $e$: the selected core has the smaller already paid
bound $2\,10^{-9}$, and (CW.11) covers the cap. Its only metric
change is the original $|\delta_*|<10^{-10}$ compact change.
Consequently, using C.17's full ordered integral just once,

$$
 \begin{split}
 a_0&<10^{-12}+15.736315e+0.304809\,10^{-10}<0.002235,\\
 p_0&<6\,10^{-21}+1.950540\,10^{-12}
                   +30.196406e+0.105999\,10^{-10}\!<0.004288.
 \end{split}                                             \tag{CW.15}
$$

This comparison is valid for the piecewise-defined passive
coefficient field even before the curvature match at $L$.
The frame and position themselves are propagated continuously;
no independent geometric jump is inserted. If such a jump
were prescribed, it would be a separate port.

## 4. Actual cap $C^1$ anchors from the exact angular equations

It is unnecessary to differentiate the zero-width cap correction
to obtain its frame and position's first angular derivatives.
The cap is an actual solution. Its complete Gauss--Weingarten
equations in the original moving angle are

$$
 (\mathsf Q_*)_\phi=\mathsf Q_*\Omega_{\phi,*},\qquad
 (F_*)_\phi=\mathsf Q_*c_{\phi,*},
$$
$$
 \Omega_\phi=\Omega\left(
      \frac\beta{\gamma_{\rm met}}\frac vm,
      a\frac um,\frac a m\right),\qquad
 c_\phi=(0,av/m,0)^T .                                \tag{CW.16}
$$

Here $\gamma_{\rm met}$ is the fixed radial metric coefficient,
not the cap input $\gamma$. Equation (CW.16) is justified by
M's full solved equations and RA's genuine matching $R$-anchor.
It is not imposed on the unsolved raw model.

For that raw model retain its actual angular defects

$$
 E_0=(\mathsf Q^0)_\phi-\mathsf Q^0\Omega_{\phi,0},\qquad
 P_0=(F^0)_\phi-\mathsf Q^0c_{\phi,0} .                \tag{CW.17}
$$

The [completed full angular certificate](../notes/2026-11-14-R133-final-complete-angular-defect.md)
gives, on every original piece and interface,

$$
 \|E_0\|<\varepsilon_Q=3.127699\,10^{-8},\qquad
 |P_0|<\varepsilon_F=4.956566\,10^{-8}.                \tag{CW.18}
$$

ACT.7--8, already derived from the same complete old geometry,
give $\|\mathsf Q^0_\phi\|<2.156$ and $|F^0_\phi|<4$.
Hence

$$
 \|\Omega_{\phi,0}\|<2.157=:N_0,\qquad
 |c_{\phi,0}|<4.001=:V_0.                             \tag{CW.19}
$$

The repaired-cap table and its full tiny repair show that the
raw values satisfy

$$
 3<|m^0|<6,\quad |v^0|<6,\quad |u^0|<1/50,
 \qquad J^0=v^0/m^0>31/32 .                           \tag{CW.20}
$$

Also $|m_*|>3$, since the original lower bound
$3.1914104290$ loses at most $5\,10^{-18}+e$.
The first and last components in (CW.16) and (CW.19)--(CW.20)
therefore supply actual intrinsic bounds, without new scalar
evaluation:

$$
 \left|\frac\beta{\gamma_{\rm met}}\right|
       <\frac{32}{31}N_0<2.227,
 \qquad a<\frac{32}{31}V_0<4.131 .                    \tag{CW.21}
$$

The exact changing-mean fractions, using (CW.11) and both mean
gaps greater than 3, give

$$
 \begin{split}
 \left|\frac{v_*}{m_*}-\frac{v^0}{m^0}\right|&\le e,\\
 \left|\frac{u_*}{m_*}-\frac{u^0}{m^0}\right|
        &\le\left(\frac13+\frac1{450}\right)e,\\
 \left|\frac1{m_*}-\frac1{m^0}\right|&\le e/9 .
 \end{split}                                             \tag{CW.22}
$$

For instance the first line bounds the two terms
$\Delta v/m_*$ and $-v^0\Delta m/(m_*m^0)$ separately.
No mean is fixed by declaration. Combining all three skew
coefficients by their component sum yields

$$
 \|\Delta\Omega_\phi\|
 \le\left(2.227+4.131\frac{67}{150}\right)e<4.073e,
 \qquad |\Delta c_\phi|<4.131e .                     \tag{CW.23}
$$

Now subtract (CW.16) and (CW.17), before estimating:

$$
 \partial_\phi(q_*-q_0)
   =(q_*-q_0)\Omega_{\phi,0}
                  +q_*\Delta\Omega_\phi-e_z^TE_0,
$$
$$
 \partial_\phi[e_z^T(F_*-F^0)]
   =(q_*-q_0)c_{\phi,0}
                  +q_*\Delta c_\phi-e_z^TP_0 .       \tag{CW.24}
$$

These retain the complete raw angular defects. At $L$, (CW.14)
and $|q_*|=1$ prove

$$
 \begin{split}
 A_{1,L}&<2.157(0.002234557)+4.073e+\varepsilon_Q
                                                    <0.005399,\\
 B_{1,L}&<4.001(0.002234557)+4.131e+\varepsilon_F
                                                    <0.009528.
 \end{split}                                             \tag{CW.25}
$$

This is the missing $R\to L$ actual cap transfer. No $C^1$
bound is inferred from a $C^0$ function bound; instead (CW.24)
uses the cap's exact first-order angular equations. The core
estimate has not been extended beyond its domain.

## 5. Complete selected-core propagation and weak receiver

Insert the genuine $L$-ports (CW.14),(CW.25) into ACT.1:

$$
 \begin{split}
 a_0&\le A_{0,L}+3.148\,10^{-8}<0.002235,\\
 a_1&\le A_{1,L}+4.312A_{0,L}+3.6461\,10^{-5}<0.015072,\\
 b_1&\le B_{1,L}+1.950541A_{1,L}
                       +12.205365A_{0,L}+1.41\,10^{-4}<0.04748.
 \end{split}                                             \tag{CW.26}
$$

All these are full-circle vertical observations. The actual
reflected cap has the original quarter-turn equivariance.
The selected passive coefficients are fourfold-periodic, so
radial uniqueness preserves that equivariance below $L$.
The vertical observables and their differences are therefore
genuinely periodic, as required by WRA's integration by parts.
There is no unpaid angular seam functional in this stated axial
world. A different unmatched world seam is outside this assertion.

Substitute (CW.26) into the complete WRA.13 table. Four new exact
rational comparisons give

| Original source | Actual sufficient coefficient |
|---|---:|
| $D_*+J_-$ | $94600$ |
| $F_-$ | $6693$ |
| $F_{\rm st}$ | $3024$ |
| $J_{\rm st}$ | $8907$ |

This proves (CW.3). The root units remain
$H^{-2/3}\oplus H^{-1}$; the strict units remain
$H^{-1}\oplus H^{-1}$; the body norms use ordinary radial
$L^2(dr)$; both means and every original affine impulse remain.
No incomplete TC prefix supplies those complete source norms.

For a general correction the exact varying-anchor contribution
is still

$$
 P_b=\Pi J e_z^T(Y_b+K_b\mathsf Q_bx).
                                                               \tag{CW.27}
$$

ACT.20--22 transfer these genuine ports from $L$ with the
determinant-$-1$ axial sign. They are not included in (CW.3)
by hiding them in an ordinary body source.

## 6. A supported parameter column with a genuinely fixed exterior

Use [NP's original full particular](R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md):

$$
 (\partial_r-A_{\delta_*})v_\nu=f_{\nu,\delta_*}
       \quad(0<r<b),\qquad v_\nu(b)=0,
 \qquad v_\nu=0\quad(r\ge b).                         \tag{CW.28}
$$

The full source is supported in $[1/20,9/50]$ and has its
complete mean. NP proves that this zero extension satisfies
the complete ordinary equation and every interface above $b$;
the endpoint bump vanishing and the zero state introduce no
delta source.

We now specify the geometric column, instead of deducing a
world gauge from the local state. Hold the actual cap inputs,
all other intrinsic design parameters, its single world
placement and its height translation fixed. Hold the state on
$[b,L]$ fixed. Vary $\nu$ with derivative 1 and the state on
$[0,b]$ with derivative $v_\nu$. The intrinsic $\nu$ bump is
identically zero on $[b,R]$. Therefore the full radial geometric
connection and velocity, and the actual $R$-anchor, have zero
variation on that entire exterior interval. Differentiating
their initial-value equations and using uniqueness gives

$$
 \dot{\mathsf Q}(r)=0,\quad \dot F(r)=0\quad(b\le r\le R),
 \qquad K_b=0,\quad Y_b=0.                            \tag{CW.29}
$$

This is an explicit fixed-exterior column. It is stronger than
the unsupported inference that $v_\nu(b)=0$ alone would force
world ports to vanish. If the cap is written using the selected
composition, $v_\nu(L)=0$ also gives zero variation of its actual
inner curvature datum, and the fixed cap/tail inputs agree with
that direction. No other metric parameter is varied implicitly.

On $[0,b]$ the relative geometric variation is exactly the RHI
one used by the completed WMR calculation, including its direct
metric terms. Thus AWH.7 applies to the actual cap-anchored
base rows, and (CW.29) gives $P_b=0$ for this particular.
The complete fixed-base translation still cancels only because
$\Pi g=0$; an independent varying translation would not cancel.

Using (CW.15) in AWH.8, the full additional error is less than

$$
 0.031082487(0.002235)+0.006877446(0.004288)
   =\frac{98959846893}{10^{15}}<0.000099.               \tag{CW.30}
$$

The completed reference interval AWH.1 then gives

$$
 -0.0253702-0.000099
   <\mathcal L_{\mathrm{cap},\nu}
   <-0.0252298+0.000099 .                             \tag{CW.31}
$$

Both ends lie strictly inside (CW.4), and
$1/0.02513<40$. This proves the actual cap-anchored particular
height sign without repeating a geometric ODE, RHI carrier,
NP residual or WMR contraction.

The homogeneous incoming correction used to satisfy the waist
and other equations can vary the cap inputs and world ports.
Its complete contributions must still be added. In particular
(CW.4) is not the fully corrected $\nu$ Schur complement and
does not prove that a whole bordered operator is invertible.

## 7. New arithmetic and remaining scope

The companion
[exact saved-bound combinations](../scripts/fourfold_codazzi_cap_world_anchor_saved_bounds.py)
contains 24 new rational comparisons. They were evaluated once
and all passed. They combine only the complete existing
constants, the actual successful WMR output and the identities
proved above. No old scientific target was rerun and no new
floating approximation was promoted to a certificate.

The missing actual $L$ and $b$ vertical anchor values and their
first angular derivatives for this cap-anchored selected
reference have now been supplied. The $C^0$ cap state bound
$e=0.000142$ is weaker than the final geometric $10^{-4}$
requirement. Full core/cap curvature matching, the true
homogeneous finite/high inverse and incoming corrections,
nonlinear residual zero, fixed final metric and the final
closed-family geometry are not asserted.
