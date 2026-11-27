# R119 SHT: C1 physical height of the actual selected exact tail

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** On the original S/T parameter domain, the actual selected
scalar height, with its one global height input fixed, is Lipschitz
in the normalized parameter $A^0$ distance with values in the
physical global $C^2$ space on the original tail and finite connector.
Its complete linear response has norm at most
$2^{-31220733}r_\gamma^{-1}$.

The response is a genuine Frechet derivative on the strict
$H^{8193}$ interior. It is continuous in the operator topology
$H^{8193}\to C^2$. At every boundary point it also gives the
relative first-order expansion along all admitted $A^0$-small
increments. The derivative is obtained from differences of actual
matched heights, so the global second-jet conditions are preserved.

This conclusion concerns the actual selected height and its original
material domain. The horizontal frame, core equations, all matching
ports and the final fixed-metric family retain their own obligations.
In particular, an independently chosen global height input has its
own derivative; it is not set to zero by a reconstruction estimate.

## 1. The original family and the complete readout

Use:

- [SDIF](R119-supplement-A0-response-and-differentiability-of-the-selected-exact-tail.md), the actual selected-coordinate response;
- [GHW](R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md), the complete low-graph physical height derivative;
- [GHC](R144-supplement-complete-actual-parameter-height-at-fixed-physical-coordinate.md), the true fixed-physical-coordinate parameter column;
- [GHR](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md), the independent metric-reference height and both endpoint columns.

Keep the original domain
$$
 {\cal D}=
 \{\gamma\in H^{8193}_{\perp,\mathrm{ev}}(4\mathbb Z):
       \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
       \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}\},
 \qquad r_\gamma=10^{-9}.                                  \tag{SHT.1}
$$
For directions write
$$
 |\eta|_X=\|\eta/r_\gamma\|_{A^0},\qquad
 |\eta|_Y=\|\eta/r_\gamma\|_{H^{8193}} .
$$
The original seed-selected second parameter and full first-principal
response are retained. All comparisons are in the common physical
reference of SDIF, with the reference costs already included in
GHW's displayed constants.

Let ${\cal R}(\gamma,w,\lambda)$ be the actual scalar height on
the original tail and its entire finite connector, with the one
global additive height input $\lambda$. It has the exact affine
dependence
$$
 {\cal R}(\gamma,w,\lambda)
            ={\cal R}(\gamma,w,0)+\lambda\,{\bf1}.          \tag{SHT.2}
$$
There are no independently reset constants on separate pieces.

Let ${\cal Z}^2$ be GHW's complete piecewise physical $C^2$ readout,
including all one-sided representatives and the flat-end limits.
Let ${\cal C}^2\subset{\cal Z}^2$ be its closed subspace satisfying
all original value, first-jet, second-jet and flat-end matching
conditions. Its elements are the global $C^2$ heights on this
original material domain. This is not the entire closed surface.

For fixed $\lambda_0$ put
$$
 Z(\gamma)={\cal R}(\gamma,w_\gamma,\lambda_0),
$$
where $w_\gamma$ is exactly the original S/T selection.
Its zero residual, original state traces and matching imply
$Z(\gamma)\in{\cal C}^2$ for every $\gamma\in{\cal D}$.

The selected common $E_{2960}^+$ bound is $2^{-49999998}$.
Even after a further factor2, every selected height, any segment
between two of them and every cross pair with an admitted gamma
remains in GHW's $E_{1856}^+$ ball of radius $2^{-49000000}$.
The exponent margin is999997. Thus the reconstructions used below
are actual admitted inputs, not formal extrapolations.

## 2. Completed derivative bounds and the new complete coefficient

Write, at the actual selected point,
$$
 A_\gamma=D_w{\cal R}(\gamma,w_\gamma,\lambda_0),\qquad
 C_\gamma=D_\gamma{\cal R}(\gamma,w_\gamma,\lambda_0).
$$
GHW.21--GHW.22 prove the complete bounds
$$
 \begin{split}
 \|A_\gamma h\|_{{\cal Z}^2}
                    &\le2^{2048}\|h\|_{E_{20,c}^+},\\
 \|C_\gamma\eta\|_{{\cal Z}^2}
                    &\le2^{-56000000}|\eta|_X .
 \end{split}                                               \tag{SHT.3}
$$
These also hold along the admitted cross segments just identified.
They include the ordinary mean, true first-principal feedback,
second seed parameter, reference-height term with its constant1,
the entire finite connector, physical scales and both endpoints.

SDIF constructs the actual selected derivative $V_\gamma$ and gives
$$
 \|w_{\gamma'}-w_\gamma\|_{E_{20,c}^+}
                   \le L_0|\gamma'-\gamma|_X,\qquad
 \|V_\gamma\eta\|_{E_{20,c}^+}\le L_0|\eta|_X,
 \quad L_0=2^{-31222782}.                                  \tag{SHT.4}
$$
Define
$$
 {\cal V}_\gamma\eta
       =A_\gamma V_\gamma\eta+C_\gamma\eta .               \tag{SHT.5}
$$
The entire chain-rule coefficient is
$$
 \begin{split}
 2^{2048}L_0+2^{-56000000}
  &=2^{-31220734}+2^{-56000000}\\
  &< L_Z,\qquad L_Z=2^{-31220733}.
 \end{split}                                               \tag{SHT.6}
$$
The parameter term is included before widening. No height or
metric-reference column is hidden in a vanishing source norm.

To see the full geometry of (SHT.5), put
$$
 v_\eta=D_w{\cal U}_\gamma(w_\gamma)V_\gamma\eta,\qquad
 \widetilde v_\eta=D_\gamma{\cal U}_\gamma(w_\gamma)\eta .
$$
Then its two contributions are exactly
$$
 {\cal V}_\gamma\eta
   =\{v_\eta+H_{v_\eta}+H_{\Gamma_1,V_\gamma\eta}\}
    +\{\widetilde v_\eta+H_{\partial,\eta}
                           +H_{\mathrm{met},\eta}\}.      \tag{SHT.7}
$$
The first brace is GHW.4. The second is the fixed-$w$, fixed-$\lambda$
column GHC.5. In particular the metric reference1 is present in
$H_{\mathrm{met},\eta}$, and $\kappa_t$ and $q_t$ in these heights
are their actual derivatives. This equation is not the fixed-metric
nonmean response alone.

## 3. Global low-distance control on the existing value domain

For $\gamma,\gamma+\delta\in{\cal D}$ let
$h=w_{\gamma+\delta}-w_\gamma$ and $d=|\delta|_X$.
Use the exact two-stage decomposition
$$
 \begin{split}
 Z(\gamma+\delta)-Z(\gamma)
  ={}&{\cal R}(\gamma,w_\gamma+h,\lambda_0)
                      -{\cal R}(\gamma,w_\gamma,\lambda_0)\\
    &+{\cal R}(\gamma+\delta,w_\gamma+h,\lambda_0)
                      -{\cal R}(\gamma,w_\gamma+h,\lambda_0).
 \end{split}                                               \tag{SHT.8}
$$
The first difference integrates the true $w$ derivative at fixed
gamma. The second integrates the complete gamma derivative at
fixed physical $w$. The gamma segment lies in the convex set
${\cal D}$. The height segment and all its cross pairs have already
been shown admissible.

Using (SHT.3)--(SHT.4) gives
$$
 \boxed{\quad
 \|Z(\gamma+\delta)-Z(\gamma)\|_{{\cal C}^2}
                         \le L_Z|\delta|_X .
 \quad}                                                    \tag{SHT.9}
$$
The norm may be written ${\cal C}^2$ because the two endpoint
heights are actual globally matched heights. The intermediate
cross heights need only belong to ${\cal Z}^2$.

This is a global Lipschitz statement on the original closed
parameter set. It does not construct a new value map on an
open rough $A^0$ ball.

## 4. Relative first-order expansion without an unjustified topology change

Fix $\gamma\in{\cal D}$. For any admitted $\delta$ with $d\to0$,
SDIF proves
$$
 h=V_\gamma\delta+o(d)\quad\hbox{in }E_{20,c}^+,
 \qquad h\longrightarrow0\quad\hbox{in }E_{21,c}^+ .        \tag{SHT.10}
$$
The latter follows from SDIF's actual $A^0$ continuity through
order3120. It is the higher background continuity needed by GHC.

At this fixed gamma, GHW's true $C^1$ height reconstruction gives
$$
 {\cal R}(\gamma,w_\gamma+h,\lambda_0)
       -{\cal R}(\gamma,w_\gamma,\lambda_0)
       -A_\gamma h=o(\|h\|_{E_{20,c}^+})=o(d).             \tag{SHT.11}
$$
For the parameter part of (SHT.8), the remainder is the exact
integral
$$
 \int_0^1
 \{D_\gamma{\cal R}(\gamma+t\delta,w_\gamma+h,\lambda_0)
                        -C_\gamma\}[\delta]\,dt .         \tag{SHT.12}
$$
GHC proves joint operator continuity for the relative $A^0$
parameter topology and the $E_{21}^+$ height background.
Consequently (SHT.10) makes (SHT.12) equal to $o(d)$.

Together these give
$$
 \boxed{\quad
 Z(\gamma+\delta)-Z(\gamma)-{\cal V}_\gamma\delta
                         =o(|\delta|_X)\quad\hbox{in }{\cal Z}^2 .
 \quad}                                                    \tag{SHT.13}
$$
This is a relative expansion at every fixed base point of the
original closed set, including its boundary. For the fixed-$w$
derivative the original continuity in gamma from GHW is
$H^{8193}$ continuity. We have not upgraded that statement
to $A^0$ operator continuity. In particular (SHT.13) is not
asserted uniformly in all base points by such an upgrade.

The argument instead fixes the base in its $w$ Taylor remainder
and uses GHC's separately established $A^0$ continuity only for
the complete partial-gamma integral. Thus arbitrarily large
high norms of $\delta/|\delta|_X$ do not invalidate the expansion.

## 5. The derivative lies in the true global C2 space

The two summands of (SHT.5) were initially read in ${\cal Z}^2$.
An arbitrary broken direction need not have all global matching
jets. The actual selected differences identify the required
subspace without assuming that false implication.

For $|\eta|_Y\le1$ and $0<t<1/512$, use the same two actual
inward parameters as SDIF:
$$
 \gamma_t^0=(1-256t)\gamma,\qquad
 \gamma_t^1=(1-256t)\gamma+t\eta .
$$
They both belong to ${\cal D}$, and their $A^0$ increments
from gamma are at most $2t$ and $3t$ in the normalized norm.
Apply (SHT.13) separately at the same base gamma and subtract:
$$
 {Z(\gamma_t^1)-Z(\gamma_t^0)\over t}
                         \longrightarrow{\cal V}_\gamma\eta
                                  \quad\hbox{in }{\cal Z}^2.
                                                               \tag{SHT.14}
$$
Each numerator is the difference of two actual globally $C^2$
heights with all original matching and the same height gauge.
Every finite quotient therefore belongs to ${\cal C}^2$.

GHW section8 proves that the whole set of matching two-jets is closed
in the complete readout, including the infinitely accumulating
flat end through its uniform vanishing profile. It follows that
$$
 {\cal V}_\gamma\eta\in{\cal C}^2,\qquad
 \|{\cal V}_\gamma\eta\|_{{\cal C}^2}
                                      \le L_Z|\eta|_X .    \tag{SHT.15}
$$
Linearity was already established by the complete chain rule
(SHT.5). Scaling treats all high-regularity directions.
The finite even Fourier directions are dense in $A^0$; the
bound and closedness therefore extend ${\cal V}_\gamma$
uniquely to a bounded linear map from $X$ into ${\cal C}^2$.

This extends the linear response, not the nonlinear value
domain. It also proves that (SHT.13) holds in the genuine
global $C^2$ space, with exactly the original matching.

## 6. The precise C1 statement

On the strict $H^{8193}$ interior, $|\delta|_X$ is bounded
by a fixed multiple of $|\delta|_Y$. Equation (SHT.13)
therefore gives the ordinary Frechet derivative
${\cal V}_\gamma$ in the $H^{8193}$ topology.

Continuity of that derivative follows from the actual input
topologies of the two factors in (SHT.5):

1. SDIF gives $V_\gamma$ continuous in
   ${\cal L}(H^{8193},E_{20,c}^+)$, even for the relative
   $A^0$ topology on the base parameter.
2. GHW gives $A_\gamma$ continuous in
   ${\cal L}(E_{20,c}^+,{\cal Z}^2)$ when gamma varies in
   its original $H^{8193}$ topology and the height varies
   in $E_{20,c}^+$.
3. GHC gives $C_\gamma$ continuous in
   ${\cal L}(X,{\cal Z}^2)$ for the relative $A^0$ base
   topology and the $E_{21,c}^+$ height background.
   Restriction to high directions preserves continuity.

The selected background has all these value continuities.
Composition and addition of bounded operators thus prove
$$
 \boxed{\quad
 Z\in C^1({\cal D}^{\circ}_{H^{8193}};{\cal C}^2),\qquad
 \gamma\longmapsto{\cal V}_\gamma
     \ \hbox{is continuous in }{\cal L}(H^{8193},{\cal C}^2)
     \ \hbox{on the original closed domain}.
 \quad}                                                    \tag{SHT.16}
$$
For the last closed-domain continuity statement the base has
its original relative $H^{8193}$ topology.
No continuity in ${\cal L}(X,{\cal C}^2)$ is inferred.

This is the actual physical scalar-height version of the selected
parameter response, including the full reference metric and mean
height. It is not merely a derivative of the normalized B trace.

## 7. The one global height input and actual endpoint readouts

If an independent scalar input is prescribed as
$\lambda=\lambda(\gamma)$, the exact result is
$$
 \begin{split}
 \widetilde Z(\gamma)
     &=Z(\gamma)+(\lambda(\gamma)-\lambda_0){\bf1},\\
 D\widetilde Z(\gamma)[\eta]
     &={\cal V}_\gamma\eta+D\lambda(\gamma)[\eta]\,{\bf1},\\
 \|D\widetilde Z(\gamma)[\eta]\|_{{\cal C}^2}
     &\le L_Z|\eta|_X+|D\lambda(\gamma)[\eta]|.
 \end{split}                                               \tag{SHT.17}
$$
The constant function has norm1 in this readout.
A C1 conclusion for $\widetilde Z$ requires the actual scalar
input to have its own C1 law; it is not supplied by the height
reconstruction.

Every original fixed physical endpoint value or unweighted
angular mean-height readout is a bounded linear functional
$T:{\cal C}^2\to\mathbb R$ of norm at most1. Hence
$$
 |T Z(\gamma')-T Z(\gamma)|\le L_Z|\gamma'-\gamma|_X,\qquad
 |T{\cal V}_\gamma\eta|\le L_Z|\eta|_X .                    \tag{SHT.18}
$$
The actual mean is used; no mean-zero projection is applied to
the physical height. A normalized height $T Z/s_B$ retains its
explicit factor $s_B^{-1}$, and any different weighted physical
test retains its full dual norm. A parameter-dependent endpoint or
test has the additional differentiated-readout term; for example,
a moving angular density retains its full derivative. The fixed
functional statement (SHT.18) does not remove that term.

For completeness, if a separate equation prescribes one physical
height row $T\widetilde Z=\beta(\gamma)$ with $T{\bf1}=1$,
its global additive input is exactly
$$
 \lambda(\gamma)=\lambda_0+\beta(\gamma)-T Z(\gamma),
 \qquad
 D\lambda=D\beta-T{\cal V}_\gamma .
                                                               \tag{SHT.19}
$$
This is an affine elimination of that single height port.
When $\beta$ is constant and $\|T\|\le1$, the resulting derivative
has bound
$$
 \|D\widetilde Z(\gamma)[\eta]\|_{{\cal C}^2}
                    \le2L_Z|\eta|_X
                    =2^{-31220732}|\eta|_X .              \tag{SHT.20}
$$
The other endpoint span, all coframe/position/world-frame
conditions and any prescribed flux remain independent. This
single affine elimination neither solves two mean equations
nor constructs a core solution.

The northern convention $Z_0-z$ changes the derivative's sign,
and retains exactly the same norm bounds. It does not permit
independent rigid changes on different pieces.

## 8. Scope and first exact combinations

The companion reader combines the completed SDIF and GHW bounds
in five new exact integer comparisons. The first evaluation was
performed once in code mode while the local execution environment
was unavailable. No old seed, principal map, profile, norm,
integral, geometry carrier or scientific target was rerun.

This proves global physical $C^2$ scalar-height dependence for
the existing exact tail family, with actual mean, metric-reference,
connector and matching contributions. It leaves the horizontal
coframe, single world frame, full core inverse, true mean/nu/phase
Schur, B/C/Cmean equations, holonomy and position periods, regular
caps, and the final closed fixed-metric embedded family to their
remaining complete arguments.
