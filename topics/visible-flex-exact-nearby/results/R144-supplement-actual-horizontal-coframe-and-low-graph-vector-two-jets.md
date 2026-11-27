# R144 GHV: the actual horizontal coframe and complete physical two-jet derivative in the low graph

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved.** On the original S/T value domain, the complete canonical vector
reconstruction has a continuously differentiable formal physical two-jet
readout with
$$
 \|D_w{\cal V}(\gamma,w)[h]\|_{\mathcal V^2}
             \le 2^{4096}\|h\|_{E_{20}^+},\qquad
 \|D_\gamma{\cal V}(\gamma,w)[\eta]\|_{\mathcal V^2}
             <2^{-55000000}r_\gamma^{-1}\|\eta\|_{A^0}.
 \tag{GHV.1}
$$
The global height input and the one spatial placement are held fixed in
these estimates. Their independent columns are retained below. The norm
includes the entire original infinite tail, its filled flat disk, the
same finite connector, every original one-sided jet, and both genuine
end outputs. It is not a new Sobolev trace theorem.

On actual exact selected solutions the formal readout is the compatible
two-jet of the original vector surface. The original matching and
flat-end conditions form a closed subspace. Consequently a true selected
$E_{20}^+$ derivative, with the background continuity required below,
passes through (GHV.1) to a genuine global $C^2$ vector derivative on this
tail--connector disk. No arbitrary broken graph direction is declared
globally compatible, and no core/cap matching equation or fixed-metric
closed-family conclusion is inferred.

The estimate does not require a third derivative of physical height.
It uses the Cartesian horizontal metric, its genuine $C^1$ coframe,
and the full radial rotation connection.

## 1. Original inputs and the actual material domain

Use the completed proofs:

- [GHW: complete physical height in the low graph](R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md), especially GHW.5, GHW.18--GHW.22 and section 8;
- [GHR: actual metric reference-height](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md), especially GHR.4--GHR.8 and GHR.18--GHR.19;
- [GHC: complete actual parameter height](R144-supplement-complete-actual-parameter-height-at-fixed-physical-coordinate.md), including joint operator continuity;
- [GF](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md) and [GA](R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md), with the full first-principal inverse and separated endpoint column;
- [S](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), [T](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), and [the fixed-stop installation Sobj](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md);
- [single-frame reconstruction Tfr](R119-supplement-positive-collar-principal-invariance-and-single-frame-reconstruction.md), especially T.5--T.17 and section 10;
- [LV: the finite-long vector graph](R144-supplement-complete-long-horizontal-coframe-and-vector-tame-graph.md), for the consistent frame, independent world ports, and formal versus compatible jets.

The graph input $w$ is the nonmean coordinate of S/T. Write $W(a)>0$
for the metric slope, to distinguish it from that graph input:
$$
 g=(1+W(a)^2)\,da^2+a^2d\theta^2,\qquad
 u={\cal U}_\gamma w,\qquad
 \|w\|_{E_{1856}^+}\le2^{-49000000},\qquad r_\gamma=10^{-9}.
 \tag{GHV.2}
$$
Gamma remains in the original $H^{8193}$ value domain. No $A^0$ open
extension is introduced. The physical radius, material interfaces,
common reference, fixed stop and installed scales are fixed.

The filled tail and finite connector form the material disk
$0\le a\le a_B$. Its flat part is $0\le a\le a_f$, with fixed $a_f>0$.
Sobj.13 gives $a_B<1$. Use Cartesian material coordinates
$y=(x_1,x_2)=(a\cos\theta,a\sin\theta)$. A path from one fixed point on
the outer circle to any point can consist of a radial segment and an
angular arc, with length less than $(1+2\pi)a_B<8$. The total material
length, not the number of crossed cells, controls integration.

The readout $\mathcal V^2$ is the component sum of suprema of values,
first Cartesian derivatives and all ordered second Cartesian
derivatives, including the original one-sided representatives. For
the formal path construction, keep also the two sides of one fixed
angular cut. No compatibility across this cut or a material interface
is inserted into the norm.

## 2. The actual background admits a uniform Cartesian metric chart

Sobj.13 and Sobj.19 give on the entire tail and finite connector
$$
             |W_a|<2,\qquad W/a<1/3,\qquad W<1/8.
 \tag{GHV.3}
$$
The internal tail has the sharper first two bounds $1/8$. On the
finite connector, $W/a<5/18$, $|(\log W)_t|\le7$, and
$a<7\cdot10^{-6}$ imply (GHV.3), including $|W_a|<35/18<2$.
These are the actual installed bounds, with neither an old radius
nor a root-free subinterval substituted.

Let $z$ be the full positive Darboux height. At its current fixed metric
the radial reference satisfies $z_{{\rm ref},a}=W$, so its gradient has
norm $W$ and its orthonormal polar Hessian entries are $W_a,W/a$.
Put $R=2^{-47000000}$. The actual nonmean bound of GF.11/GHR.6 and the
fixed-metric derivative in GHW.18, integrated along the segment from
zero to the actual nonmean field at this same metric, give
$$
             \|z-z_{\rm ref}-\lambda\|_{\mathcal Z^2}<2^{708}R.
 \tag{GHV.4}
$$
The complete mean root and the true radial jets remain in this
fixed-metric integral. Since $708-47000000<-5$, (GHV.3)--(GHV.4) imply
$$
                  \|Dz\|_\infty<1/4,\qquad \|D^2z\|_\infty<4.
 \tag{GHV.5}
$$
Tensor norms here are Euclidean operator norms, dominated by GHW's
component-sum norm. The additive $\lambda$ does not enter (GHV.5).

With $e_r=y/a$, the exact horizontal metric is
$$
                 G=I+W^2 e_r e_r^{\mathsf T}-Dz\,Dz^{\mathsf T}.
 \tag{GHV.6}
$$
On the flat disk $W=Dz=0$, so $G=I$, including at the center.
The polar expression is exactly Tfr.9, without angular averaging.
The actual bounds give
$$
 \|G-I\|_\infty<1/64+1/16=5/64<1/8,\qquad \|DG\|_\infty<32.
 \tag{GHV.7}
$$
Before widening, the second bound follows from
$$
 \|DG\|_\infty
 \le2W|W_a|+2W^2/a+2\|Dz\|_\infty\|D^2z\|_\infty
 <1/2+1/12+2<4.
$$
The derivative of $e_r e_r^{\mathsf T}$ is explicitly charged by $2/a$.
Its actual products are bounded; no bare singular chart factor is left.

## 3. The full metric direction is controlled by its already paid height

Let $\dot W$ be the actual first-principal response to a graph direction
at fixed gamma, or the complete second-parameter response to a gamma
direction at fixed $w$. The latter includes radial first compensation
and the full first-principal inverse. Both are compact radial metric
variations on the original bump supports. Put
$$
 \Xi(\dot W)=\|\dot W\|_\infty+\|\dot W_a\|_\infty
                                      +\|\dot W/a\|_\infty.
 \tag{GHV.8}
$$
At the center all three entries use their zero continuation.

Let $H_{\rm met}$ be the actual metric reference-height column, including
the reference $1$ and complete mean response. GHR.4's analytic function
$\mathcal L$ gives the exact identity and genuine radial bounds
$$
 (H_{\rm met})_a=\dot W(1+{\cal L}),\qquad
          |{\cal L}|<1/4,\quad |{\cal L}_t|<1/4
                            \quad\hbox{on the bump supports}.
 \tag{GHV.9}
$$
The bound on $\mathcal L_t$ was proved by differentiating the true mean
root in GHR.5--GHR.8. It is not inferred from a small value. It applies
also to a first-principal variation: $\mathcal L$ depends on the
background mean formula, not on which scalar radial bump generated
$\dot W$.

Inverting and differentiating (GHV.9) gives
$$
 \begin{aligned}
 |\dot W|&\le\tfrac43|(H_{\rm met})_a|,\\
 |\dot W/a|&\le\tfrac43|(H_{\rm met})_a/a|,\\
 |\dot W_a|&\le\tfrac43|(H_{\rm met})_{aa}|
                              +\tfrac49|(H_{\rm met})_a/a|.
 \end{aligned}
 \tag{GHV.10}
$$
For this radial function, $(H_{\rm met})_a/a$ is its tangential
Cartesian Hessian entry. Both it and $(H_{\rm met})_{aa}$ are bounded
by the Hessian component sum. The combined Hessian coefficient is
$4/3+16/9=28/9<4$, while the gradient coefficient is $4/3<4$.
Consequently
$$
                     \Xi(\dot W)<4\|H_{\rm met}\|_{\mathcal Z^2}.
 \tag{GHV.11}
$$
Outside the metric supports $\dot W=0$. The height column may retain a
nonzero constant there; this constant is neither removed nor used to
declare the whole height column zero.

GHW.20 and the installed GHR.18--GHR.19 now give
$$
 \begin{aligned}
 \Xi(D_wW[h])&<2^{12002}R\,\|h\|_{E_{20}^+},\\
 \Xi(D_\gamma W[\eta])&<2^{1474-110000000}
                                     r_\gamma^{-1}\|\eta\|_{A^0}.
 \end{aligned}
 \tag{GHV.12}
$$
Here $1474=1024+8+440+2$ retains, respectively, the actual material
height constant, Cartesian conversion, installed
$\varepsilon_s/\rho$ factor, and (GHV.11). The first line uses the
genuine first-principal bound of GHW.19--GHW.20; it does not identify
a first-parameter vector with a second-parameter vector.

The endpoint straightening column does not change the metric because
its full support lies in the original positive B collar, and the
principal map is exactly invariant under that change for every
admitted parameter. That endpoint column is present in $\dot z$
through GHC/GHW. Both the actual endpoint change and complete principal
feedback are therefore retained.

## 4. The actual coframe derivative uses only one physical metric jet

The complete variation of (GHV.6) is
$$
 \dot G=2W\dot W\,e_r e_r^{\mathsf T}
              -D\dot z\,Dz^{\mathsf T}-Dz\,D\dot z^{\mathsf T}.
 \tag{GHV.13}
$$
Cartesian differentiation, using (GHV.3)--(GHV.5), gives
$$
 \|\dot G\|_{C^1}
  \le6\Xi(\dot W)+10\|\dot z\|_{\mathcal Z^2}
  <2^8\{\Xi(\dot W)+\|\dot z\|_{\mathcal Z^2}\}.
 \tag{GHV.14}
$$
The metric part has coefficients $1/4,4,1/4,1/2$, whose sum is $5<6$.
The height part has coefficients $1/2,8,1/2$, with sum $9<10$.
In particular the $4W\dot W/a$ term from angular differentiation of
$e_r e_r^{\mathsf T}$ is charged. No height third derivative occurs.

Take the positive symmetric matrix square root
$$
                              S=G^{1/2}.
 \tag{GHV.15}
$$
Its rows form a positively oriented orthonormal coframe:
$G=S^{\mathsf T}S$ and $\det S>0$. This is the two-dimensional
horizontal coframe. It says nothing about the determinant of an
unrelated absolute three-dimensional body anchor.

The absolutely convergent matrix binomial series on $\|G-I\|\le1/4$
gives the full noncommutative derivative bounds
$$
 \|S\|,\ \|S^{-1}\|\le2,\qquad
                  \|D_GS\|\le2,\qquad \|D_G^2S\|\le8.
 \tag{GHV.16}
$$
They follow by replacing ordered products by products of their norms
and differentiating the convergent scalar majorant. A direction is
not assumed to commute with the background.

At a real background satisfying (GHV.7), put $N=\|\dot G\|_{C^1}$.
The true chain rule gives
$$
 \|DS\|\le64,\qquad \|\dot S\|\le2N,\qquad
                \|D\dot S\|\le(2+8\cdot32)N<2^9N.
 \tag{GHV.17}
$$
The last expression explicitly includes $D_G^2S[DG,\dot G]$.

## 5. Complete connection, one spatial frame, and formal two-jets

Write
$$
 \omega_1=S_{11}\,dx_1+S_{12}\,dx_2,\qquad
 \omega_2=S_{12}\,dx_1+S_{22}\,dx_2.
$$
Use the exact orientation convention of Tfr.11:
$$
 d\omega_1=\Omega\wedge\omega_2,\qquad
 d\omega_2=-\Omega\wedge\omega_1.
$$
Define
$$
 c_1=\partial_1S_{12}-\partial_2S_{11},\qquad
 c_2=\partial_1S_{22}-\partial_2S_{12}.
$$
Solving the two equations with the actual determinant gives
$$
                  \binom{\Omega_1}{\Omega_2}
                           =\frac{S}{\det S}\binom{c_1}{c_2}.
 \tag{GHV.18}
$$
Both components, including the complete radial connection, remain.
In polar coordinates this is Tfr.12--Tfr.12a after changing coframe.
The radial rotation mean has not been set to zero.

Equations (GHV.16)--(GHV.17) imply the uniform budgets
$$
 \begin{gathered}
 \|c\|\le2^8,\quad \|\dot c\|\le2^{11}N,\quad
 \|S/\det S\|\le4,\quad
             \|D_G(S/\det S)[\dot G]\|\le2^6N,\\
 \|\Omega\|\le2^{10},\qquad \|\dot\Omega\|<2^{15}N.
 \end{gathered}
 \tag{GHV.19}
$$
Here (GHV.7) gives $\det S\ge7/8>1/2$.
For the determinant derivative use
$\dot{\det S}=(\det S)\operatorname{tr}(S^{-1}\dot S)$.
The fourth bound is at most
$(2+16)\|\dot S\|\le36N<2^6N$. The last is
$2^6\,2^8N+4\,2^{11}N<2^{15}N$. No derivative of the connection
has been introduced.

Choose one initial planar rotation $\alpha_0$ and position $X_0$ at
the fixed outer material point. Let $\mathcal P_y$ be the fixed paths
from section 1. Define
$$
 \alpha(y)=\alpha_0+\int_{{\cal P}_y}\Omega,\qquad
 T(y)=R_{\alpha(y)}S(y),\qquad
 X(y)=X_0+\int_{{\cal P}_y}T(s)\,ds ,
 \tag{GHV.20}
$$
where $R_\alpha$ is the planar rotation. Every integration crosses the
actual original interfaces in order.

For a general broken graph, this is a path-dependent algebraic
extension. Its formal first-jet readout is $T$, and the formal
second-jet readout is
$$
 T_{,k}^{\rm form}=R_\alpha\{JS\,\Omega_k+S_{,k}\},\qquad
              J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{GHV.21}
$$
Off shell these need not be derivatives of the path-defined value.
They are nevertheless continuously differentiable maps of the
complete $C^1$ metric data on the displayed matrix domain.

For fixed $\alpha_0,X_0$, the path bound and (GHV.19) yield
$$
                  \|\dot\alpha\|_\infty<2^{18}N,\qquad
                  \|\dot T\|_\infty<2^{20}N.
 \tag{GHV.22}
$$
The background rotations are real and have norm one. The exact four
differentiated terms of (GHV.21) are
$$
 R_\alpha\{
 J\dot\alpha(JS\,\Omega_k+S_{,k})
           +J\dot S\,\Omega_k+JS\,\dot\Omega_k+\dot S_{,k}\}.
 \tag{GHV.23}
$$
Their combined bound is
$$
 \{2^{18}(2^{11}+2^6)+2^{11}+2^{16}+2^9\}N<2^{30}N .
$$
The value variation is at most $8\|\dot T\|_\infty<2^{23}N$.
Counting the two horizontal coordinates, both first-coordinate
directions, and all ordered second entries gives
$$
     \|D_G{\cal X}[\dot G]\|_{\mathcal V^2_{\rm hor}}
                                      <2^{40}\|\dot G\|_{C^1}.
 \tag{GHV.24}
$$
Before widening the component count is bounded by
$2^{24}+2^{22}+2^{33}<2^{40}$. This is the strong physical supremum
norm; no radial supremum is exchanged with a Fourier sum.

The infinite-cell paths have finite total material length. Integration
is bounded on the corresponding piecewise coefficient spaces, and
the uniform original physical tail limits pass through it. There is
no summation of a cell-independent constant over infinitely many cells.

## 6. Complete actual graph and gamma columns

Adjoin the actual height to the horizontal formal readout. Equations
(GHV.14), (GHV.24), and the unchanged height column give
$$
 \|\dot{\cal V}\|_{\mathcal V^2}
       \le2^{64}\{\Xi(\dot W)+\|\dot z\|_{\mathcal Z^2}\}.
 \tag{GHV.25}
$$
All values, both first derivatives and all Hessian entries are included.
For the northern physical convention use $Z_0-z$ with its original
single constant $Z_0$; the norm estimate is unchanged.

With the same fixed height input, GHW.21--GHW.22 give
$$
 \|\dot z_w\|_{\mathcal Z^2}\le2^{2048}\|h\|_{E_{20}^+},\qquad
 \|\dot z_\gamma\|_{\mathcal Z^2}
                <2^{-56000000}r_\gamma^{-1}\|\eta\|_{A^0}.
$$
Together with (GHV.12), the graph coefficient is at most
$$
                    2^{2112}+2^{12066-47000000}<2^{4096},
$$
and the gamma coefficient is at most
$$
            2^{64-56000000}+2^{1538-110000000}<2^{-55000000}.
$$
This proves (GHV.1). It includes the true endpoint tangent
$I+{\cal L}_\partial D_fq_\gamma(F_Bw)F_B$, the full mean response,
the entire first-principal feedback and the actual seed's second
parameter. No part is replaced by a fixed-metric proxy.

The graph derivative is continuous in its actual operator norm when
$w$ varies in $E_{20}^+$ and gamma in its original relative $H^{8193}$
topology. For the partial gamma derivative, GHC/GHR's stronger
continuity is retained: it is jointly continuous in
$\mathcal L(A^0,\mathcal V^2)$ with gamma in its relative $A^0$
topology and $w$ in $E_{21}^+$, always inside the original value domain.
The scalar-height and metric-height operators have these properties;
(GHV.9)--(GHV.10) use continuous true mean coefficients; and
(GHV.13)--(GHV.24) are continuous operations on the complete physical
coefficients. The background $C^1$ metric is continuous in the same
topology. The uniform deep limits are the profiles already paid in
GHR/GHW, not an unsupported coordinatewise convergence argument.

No stronger relative-$A^0$ operator continuity is assigned to the
fixed-gamma graph derivative. It keeps exactly GHW's stated topology.

## 7. Exact solutions, original matching, and the filled flat disk

For a genuine S/T zero-residual solution, Tfr.15 proves flatness of
the horizontal metric from the complete Darboux equation and the same
holonomy-one root. Its original height/state traces and true PDE rows
match the physical second jets at every original material interface.
Thus $G$ and $S$ have their actual matching first jets, with no
unrecorded distributional interface curvature.

Tfr section 10 proves the actual physical flat-end limits and
filled-disk extension. On that disk $G=I$ and the connection is zero;
the one-sided limits agree with the extension. Therefore (GHV.18)
is the single flat oriented connection on this same material disk.
Integrating from the chosen outer frame gives $d\alpha=\Omega$.
The complete coframe equations give
$$
                         d(R_\alpha S\,dy)=0.
 \tag{GHV.26}
$$
The value in (GHV.20) is consequently path independent, and its true
first and second derivatives are precisely (GHV.20)--(GHV.21).
On the annulus this is the original holonomy and position-period
argument of Tfr; the filled disk adds no independent position or
phase choice.

In particular the actual flat part is
$$
              X(y)=c+R_{\alpha_f}y,\qquad z(y)=z_f,
                             \qquad 0\le |y|\le a_f.
 \tag{GHV.27}
$$
The constants $c,\alpha_f,z_f$ are outputs of the same reconstruction.
Their variations are included in (GHV.20)--(GHV.25); they are not reset
at the flat end. The affine second jets are zero and the limiting
jets agree with this continuation.

Globally compatible Cartesian jets form a closed linear subspace of
the complete two-jet readout: uniform convergence of the function and
its derivative representatives preserves the derivative identities,
all interface equalities, the angular-period identities and affine
flat-disk matching. For the countable partition, apply this first to
each finite union and then at the accumulation circle using the
uniform physical tails. Matching only finitely many cuts would not
justify the final passage.

Consequently convergent graph difference quotients of exact selected
solutions, passed through the actual chain rule and (GHV.1), converge
in that same compatible subspace. A separately established selected
derivative $D_\gamma w_\gamma$ gives
$$
 D_\gamma F^{\rm can}_\gamma[\eta]
 =D_\gamma{\cal V}(\gamma,w_\gamma)[\eta]
      +D_w{\cal V}(\gamma,w_\gamma)[D_\gamma w_\gamma[\eta]]
 \tag{GHV.28}
$$
in genuine global physical $C^2$ on the original tail--connector disk.
Parameter differentiability is on the strict interior of the
original $H^{8193}$ domain. Any additional relative continuity uses
the separately proved selection theorem with its actual topology.
Neither an $A^0$ open value domain nor rough-source onto solvability
has been assumed here.

This is the complete horizontal counterpart to GHW. It preserves
the actual means, radial rotation mean, flat-end constants and both
genuine endpoint traces. Arbitrary broken directions have only the
specified formal readout.

## 8. Independent spatial ports and scope

Fixing $\alpha_0,X_0$ in (GHV.20) specifies a canonical readout.
For varied initial planar phase and position the exact extra column is
$$
           \dot X_{\rm rigid}
                   =\dot X_0+\dot\alpha_0\,J(X-X_0).
 \tag{GHV.29}
$$
There is one such initial phase and position, not a new choice at
every radius or endpoint. The original height input contributes its
one exact vertical-translation column. If a cap--long mean-height
equation selects that input, its actual derivative must be supplied.

For an independent ambient placement
$F^{\rm world}=O F^{\rm can}+b$, retain the actual formula
$$
 DF^{\rm world}
        =O\{DF^{\rm can}+\Omega_{\rm world}F^{\rm can}\}+\dot b.
 \tag{GHV.30}
$$
The skew matrix $\Omega_{\rm world}$ and position direction are true
ports, or come from the actual matching graph. The one global height
and phase coordinates are identified with the corresponding rigid
coordinates when this full placement chart is used; they are not
counted twice. No absolute body-anchor orientation or signed
cross-product column follows from this planar construction.

Core/cap matching, physical mean equations, amplitude/design
conditions and the final common-metric geometry gate retain their
original obligations. The present result supplies the actual
uniform vector readout for the exact tail and its same finite
connector. Varying gamma or selected principal parameters changes
the intrinsic design at this stage; it is not the final fixed-metric
bending family.

## 9. New exact saved-bound combinations

The companion
[fourfold_codazzi_low_graph_horizontal_saved_bounds.py](../scripts/fourfold_codazzi_low_graph_horizontal_saved_bounds.py)
records the 15 new exact rational and integer combinations used here.
Their first execution in code mode passed all 15. The Python reader
preserves those same operations; it was not run in the unavailable
local environment.

Only completed height, metric, profile and geometry bounds are
combined. No native array, earlier saved comparison, PDE solve,
profile integral, long kernel or old scientific target was rerun.
