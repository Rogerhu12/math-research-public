# R119 GVC: global C2 vector response of the actual selected exact tail

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** Fix the one canonical height input and one Euclidean
placement. The original S/T selected exact tail, including its same
finite connector and filled flat disk, is globally Lipschitz in
the normalized parameter $A^0$ distance with values in physical
global $C^2$. Its complete vector response satisfies
$$
 \|{\cal W}_\gamma\eta\|_{C^2}\le L_F|\eta|_X,\qquad
 L_F=2^{-31218685},\qquad
 |\eta|_X=\|\eta/r_\gamma\|_{A^0},\quad r_\gamma=10^{-9}.
 \tag{GVC.1}
$$
It is genuinely $C^1$ on the strict $H^{8193}$ interior of the
original value domain. The derivative is continuous in the operator
topology $H^{8193}\to C^2$ for the original relative $H^{8193}$ base
topology. At every fixed base, including a boundary point, it gives
the relative first-order expansion along admitted $A^0$-small
increments.

The result includes the true horizontal coframe, full radial
rotation, physical means, endpoint outputs and the flat-disk
continuation. Their global matching is proved from differences of
the actual exact surfaces. Arbitrary broken graph directions are
not declared globally compatible. The intrinsic design varies with
gamma here; this is not by itself a fixed-metric bending family.

## 1. The actual family and physical vector norm

Use:

- [SDIF](R119-supplement-A0-response-and-differentiability-of-the-selected-exact-tail.md), especially SD.23--SD.30;
- [GHV](R144-supplement-actual-horizontal-coframe-and-low-graph-vector-two-jets.md), especially GHV.1 and GHV.25--GHV.30;
- [SHT](R119-supplement-C1-physical-height-of-the-actual-selected-tail.md), especially the admitted cross pairs and the fixed-base topology argument;
- [GHW](R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md), [GHC](R144-supplement-complete-actual-parameter-height-at-fixed-physical-coordinate.md) and [GHR](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md), with all actual metric, mean, reference-height and endpoint columns.

Keep exactly
$$
 {\cal D}=\{\gamma\in H^{8193}_{\perp,\mathrm{ev}}(4\mathbb Z):
   \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
   \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}\}.
 \tag{GVC.2}
$$
Also put $|\eta|_Y=\|\eta/r_\gamma\|_{H^{8193}}$.
No open $A^0$ value domain is introduced.

Let $\mathscr V(\gamma,w,\lambda_0)$ be GHV's canonical vector
readout, with one fixed planar starting frame and position and
one fixed height input $\lambda_0$. Let $w_\gamma$ be the same
deterministic S/T selection in the common physical reference. Set
$$
              F_\gamma=O_0\mathscr V(\gamma,w_\gamma,\lambda_0)+b_0 .
 \tag{GVC.3}
$$
Here $O_0,b_0$ specify one fixed actual Euclidean placement. The
orthogonal matrix keeps its specified orientation convention; no
absolute body anchor is silently made right-handed. The local
canonical coordinates and the displayed placement specify a single
placement, not separate resets on the material pieces.

Use the Euclidean vector norm in
$$
 \|F\|_{\mathcal J^2}
   =\sup|F|+\sum_{i=1}^2\sup|\partial_iF|
                  +\sum_{i,j=1}^2\sup|\partial_i\partial_jF|.
 \tag{GVC.4}
$$
Initially this is the complete one-sided physical readout.
It is dominated by GHV's component-sum norm and is invariant
under fixed orthogonal output maps. Thus (GVC.3) has no unpaid
coordinate factor. Let $\mathcal C^2\subset\mathcal J^2$ be the
closed subspace of globally compatible Cartesian jets on the
same filled tail--connector disk.

GHV section 7 identifies each exact selected value with an
element of $\mathcal C^2$: its full Darboux residual and original
matching vanish, the true connection has its original holonomy
and position periods, and the flat disk is the affine continuation
of this same frame. The constants there remain outputs.

SHT section 1 already proves that all selected states, their
straight graph segments, and their cross pairs with admitted
gamma values remain in the reconstruction ball
$\|w\|_{E_{1856,c}^+}\le2^{-49000000}$. We use precisely those
admitted pairs, with no enlarged graph domain.

## 2. Actual chain rule and the complete coefficient

At the selected point write
$$
 A_\gamma=D_w\mathscr V(\gamma,w_\gamma,\lambda_0),\qquad
 C_\gamma=D_\gamma\mathscr V(\gamma,w_\gamma,\lambda_0).
$$
GHV gives, including on the admitted cross pairs,
$$
 \|A_\gamma h\|_{\mathcal J^2}
            \le2^{4096}\|h\|_{E_{20,c}^+},\qquad
 \|C_\gamma\eta\|_{\mathcal J^2}
            \le2^{-55000000}|\eta|_X.
 \tag{GVC.5}
$$
These are the complete vector columns, including actual metric
variation and the reference-height $1$. They are not just the
endpoint lift or the fixed-metric nonmean response.

SDIF constructs the genuine linear response $V_\gamma$ and proves
$$
 \|w_{\gamma'}-w_\gamma\|_{E_{20,c}^+}
             \le L_0|\gamma'-\gamma|_X,\qquad
 \|V_\gamma\eta\|_{E_{20,c}^+}\le L_0|\eta|_X,\qquad
                        L_0=2^{-31222782}.
 \tag{GVC.6}
$$
The full response is
$$
                 {\cal W}_\gamma\eta
                   =O_0\{A_\gamma V_\gamma\eta+C_\gamma\eta\}.
 \tag{GVC.7}
$$
Its coefficient is
$$
 2^{4096}L_0+2^{-55000000}
       =2^{-31218686}+2^{-55000000}
       <2^{-31218685}=L_F .
 \tag{GVC.8}
$$
The complete partial-parameter term is included before widening.
The true endpoint coordinate, all ordinary means, the complete
first-principal response, the seed-selected second parameter
and radial first compensation, the metric-reference height,
and the actual coframe and radial phase integrals all occur in
(GVC.7), by the exact decompositions in GHW/GHC/GHV.

## 3. Global distance bound and relative first-order expansion

For $\gamma,\gamma+\delta\in\mathcal D$, let
$h=w_{\gamma+\delta}-w_\gamma$ and $d=|\delta|_X$.
Before the fixed placement, use the exact decomposition
$$
 \begin{aligned}
 &\mathscr V(\gamma+\delta,w_\gamma+h,\lambda_0)
                         -\mathscr V(\gamma,w_\gamma,\lambda_0)\\
 ={}&\mathscr V(\gamma,w_\gamma+h,\lambda_0)
                         -\mathscr V(\gamma,w_\gamma,\lambda_0)\\
   &+\mathscr V(\gamma+\delta,w_\gamma+h,\lambda_0)
                         -\mathscr V(\gamma,w_\gamma+h,\lambda_0).
 \end{aligned}
 \tag{GVC.9}
$$
The first difference integrates the genuine graph derivative at
fixed gamma; the second integrates the complete gamma derivative
at fixed physical $w$. The gamma segment remains in the convex
set $\mathcal D$, and section 1 supplies the graph cross pairs.
Equations (GVC.5)--(GVC.8) prove
$$
           \|F_{\gamma+\delta}-F_\gamma\|_{\mathcal C^2}
                                           \le L_F|\delta|_X .
 \tag{GVC.10}
$$
The endpoints are actual matched surfaces, so their difference
is in $\mathcal C^2$. Off-shell cross pairs need only be formal
one-sided jets.

Now fix a base $\gamma$. SDIF gives
$$
 h=V_\gamma\delta+o(d)\ \hbox{in }E_{20,c}^+,\qquad
                       h\longrightarrow0\ \hbox{in }E_{21,c}^+ .
 \tag{GVC.11}
$$
The second statement is part of its actual $A^0$ value continuity
through order 3120. At this fixed gamma, GHV's $C^1$ graph readout
makes the first difference in (GVC.9), minus $A_\gamma h$, equal
to $o(\|h\|_{E_{20,c}^+})=o(d)$. For the parameter difference,
after subtracting $C_\gamma\delta$, the exact remainder is
$$
 \int_0^1
 \{D_\gamma\mathscr V(\gamma+t\delta,w_\gamma+h,\lambda_0)
                                      -C_\gamma\}[\delta]\,dt .
 \tag{GVC.12}
$$
GHV retains GHC/GHR's joint operator continuity
$A^0\to\mathcal J^2$ in the relative $A^0$ parameter topology
and the $E_{21}^+$ background topology. Thus (GVC.12) is $o(d)$.
Together the actual remainders prove
$$
 F_{\gamma+\delta}-F_\gamma-{\cal W}_\gamma\delta
                       =o(|\delta|_X)\quad\hbox{in }\mathcal J^2 .
 \tag{GVC.13}
$$

This is a relative expansion at each fixed base of the original
closed domain. The graph Taylor remainder is taken at that base,
so its original $H^{8193}$ continuity in gamma is sufficient.
It has not been upgraded to $A^0$ operator continuity. No uniform
remainder over all bases or open rough value family is asserted
using such an upgrade.

## 4. Globally matched derivative and the precise C1 statement

Use the actual inward pairs of SDIF/SHT. For $|\eta|_Y\le1$
and $0<t<1/512$,
$$
         \gamma_t^0=(1-256t)\gamma,\qquad
         \gamma_t^1=(1-256t)\gamma+t\eta
 \tag{GVC.14}
$$
belong to $\mathcal D$. Their normalized $A^0$ increments
from gamma are at most $2t$ and $3t$. Apply (GVC.13) twice at
the same base and subtract:
$$
             \frac{F_{\gamma_t^1}-F_{\gamma_t^0}}t
                \longrightarrow{\cal W}_\gamma\eta
                                 \quad\hbox{in }\mathcal J^2 .
 \tag{GVC.15}
$$
Every finite quotient is a difference of actual globally matched
$C^2$ surfaces with the same single placement. The closedness
proved in GHV includes every original interface, the angular
cut, the infinite accumulation circle, and the true affine
flat-disk continuation. Therefore
$$
        {\cal W}_\gamma\eta\in\mathcal C^2,\qquad
        \|{\cal W}_\gamma\eta\|_{\mathcal C^2}\le L_F|\eta|_X .
 \tag{GVC.16}
$$
Linearity follows from (GVC.7). Scaling covers all original
high-regularity directions. Density of their even nonmean
Fourier polynomials in $A^0$, the bound (GVC.16), and closedness
extend the response uniquely to a bounded linear
$X\to\mathcal C^2$ operator. This extends the derivative alone.

Thus (GVC.13) holds in genuine global $C^2$. On the strict
$H^{8193}$ interior the continuous inclusion of the parameter
high space in $A^0$ makes it the ordinary Frechet remainder.
Its derivative is continuous in
$\mathcal L(H^{8193},\mathcal C^2)$: SDIF gives the required
operator continuity of $V_\gamma$; GHV gives the operator
continuity of $A_\gamma$ for the original $H^{8193}$ base
topology; and GHV gives the stronger continuity of $C_\gamma$
already used in (GVC.12). The selected background has all
the required value continuities. Hence
$$
 \begin{gathered}
 F\in C^1(\mathcal D^\circ_{H^{8193}};\mathcal C^2),\\
 \gamma\longmapsto{\cal W}_\gamma
       \quad\hbox{is continuous in }
              \mathcal L(H^{8193},\mathcal C^2)
 \end{gathered}
 \tag{GVC.17}
$$
on the original closed domain with its relative $H^{8193}$
base topology. Continuity in
$\mathcal L(A^0,\mathcal C^2)$ is not claimed.

The proof uses actual differences, not a declaration that every
broken graph tangent has matching second jets. It assumes no
onto inverse for a rough source and does not obtain a derivative
in $E_{1856}^+$ by changing the target topology.

## 5. The actual height and spatial ports

If the one global height input is chosen by a separate equation,
its derivative remains an independent scalar column. It is
$D\lambda[\eta]e_z$ for positive Darboux height and has the
original opposite sign for northern height.

For a genuinely varied placement
$\widetilde F_\gamma=O(\gamma)F^{\rm can}_\gamma+b(\gamma)$,
with an independently varied height input, retain the exact formula
$$
 \begin{aligned}
 D\widetilde F_\gamma[\eta]
   ={}&O(\gamma)\{
       D F^{\rm can}_\gamma[\eta]
       +\Omega_\eta F^{\rm can}_\gamma
       +\epsilon_zD\lambda[\eta]e_z\}+Db[\eta],\\
 &\Omega_\eta=O(\gamma)^{\mathsf T}DO(\gamma)[\eta],
       \qquad\Omega_\eta^{\mathsf T}=-\Omega_\eta .
 \end{aligned}
 \tag{GVC.18}
$$
Here $D F^{\rm can}$ is the response with height input fixed,
and $\epsilon_z$ is the actual fixed height sign. The value
$F^{\rm can}$ in the frame column includes its actual height
and position. If height and axial phase were already included
as coordinates of the full rigid placement, they are identified
with those coordinates, not added again.

The actual additional fee is
$$
 L_F|\eta|_X+\|\Omega_\eta\|\,\|F^{\rm can}_\gamma\|_{C^2}
                         +|D\lambda[\eta]|+|Db[\eta]|.
 \tag{GVC.19}
$$
The frame column retains its full value factor. It is not
assigned the small deformation constant $L_F$.
Equation (GVC.18) respects the actual orthogonal orientation
component and does not supply a determinant-sensitive
absolute signed axial identity.

Every fixed bounded physical observation $T$ on global $C^2$
satisfies
$$
                \|T{\cal W}_\gamma\eta\|
                            \le\|T\|L_F|\eta|_X .
 \tag{GVC.20}
$$
Its original mean, scale and dual norm remain. A moving endpoint,
angle map, normal, density or test has the extra differentiated
observation term. The same-frame flat-disk center, height and
phase are outputs; none is independently reset.

The actual selected tail vector dependence is now paid.
Core equations, all physical mean/design rows, attachment to
the body, global geometry bounds and the final common-metric
closed family retain their remaining obligations. The changing
principal and seed metric parameters are not frozen by this
differentiability theorem.

## 6. First new exact combination

The companion
[fourfold_codazzi_selected_vector_response_saved_bounds.py](../scripts/fourfold_codazzi_selected_vector_response_saved_bounds.py)
records the single new exact integer combination (GVC.8).
Its first evaluation in code mode passed. The Python text
preserves that computation; it was not run in the unavailable
local environment. No SDIF, SHT or GHV comparison, native data,
principal map, PDE, profile integral or old scientific target
was rerun.
