# R144 GHC: the complete actual parameter-height column at fixed physical nonmean coordinate

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 9 new exact integer comparisons pass.**
At a fixed physical nonmean coordinate \(w\), the actual S/T gamma
derivative of the scalar height is the sum of three explicitly distinct
columns:
\[
 D_\gamma z[\eta]
   =v_\eta+H_{\partial,\eta}+H_{{\rm met},\eta}
                                  +D_\gamma\lambda[\eta].
\]
Here \(v_\eta=D_\gamma{\cal U}_\gamma(w)[\eta]\) is the actual nonmean
B-collar lift, \(H_{\partial,\eta}\) is its true holonomy-mean height
integral, and \(H_{{\rm met},\eta}\) is the complete GHR metric reference
column. The one global rigid height \(\lambda\) remains an independent
input unless a separate matching equation selects it.

The new complete endpoint contribution satisfies
\[
 \|v_\eta+H_{\partial,\eta}\|_{C^2_{t,\theta}}
  <s_B\,2^{262144}\epsilon_L
                        r_\gamma^{-1}\|\eta\|_{A^0},
 \qquad s_B=a_Bw_B.
\]
Both the nonmean and mean parts use the original physical units and the
same actual positive collar. No unscreened cap--long height span is
discarded.

## 1. The actual family and the full scalar-height identity

The completed sources are:

- [GA: complete A0 parameter forcing and joint operator continuity](R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md);
- [GHR: the complete metric reference-height column](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md);
- [GF: the actual parameter chain rule](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md);
- [S: the true endpoint graph and nilpotent collar coordinate](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md);
- [Gseed: the same actual positive B collar and its complete physical units](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md);
- [E: the complete reference graph and actual height reconstruction](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md);
- [Mhol: the genuine holonomy mean and unique height integral](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md).

Keep T/GF's original gamma value domain, its same common physical
reference, and
\[
 W_{1856}=\|w\|_{E_{1856}^+}\le2^{-49000000},\qquad
 \epsilon_L<2^{-57000000},\qquad
 e_\eta=r_\gamma^{-1}\|\eta\|_{A^0}.
\]
At fixed \(w\), set
\[
 u={\cal U}_\gamma w,\qquad
 v_\eta={\cal L}_\partial D_\gamma q_\gamma(F_Bw)[\eta],\qquad
 \mathfrak a_\eta=D_\gamma\mathfrak q(\gamma)[\eta].
                                                               \tag{GHC.1}
\]
The true scalar height is E.13:
\[
 z(t,\theta)=u(t,\theta)+\lambda+
  \int_{t_f}^t a_{\rm ph}(s)w_{\rm metric}(s)
                                    (1+\kappa(s))\,ds .
                                                               \tag{GHC.2}
\]
The first-principal map and all metric bumps are unchanged by the
entire candidate B-collar lift, as proved in GF.4/S.8.
Thus the metric direction in (GHC.1) is exactly GHR's complete
second-parameter column with its radial first compensation and
infinite principal feedback. There is no additional principal
variation caused by \(v_\eta\).

At fixed metric, the mean direction caused by \(v_\eta\) is
\[
 \dot\kappa_\partial
    =D_Z\kappa(q,Z)[Z(v_\eta)],\qquad
 Z(v_\eta)=
 \left(\frac{(v_\eta)_\theta}{aw},
       \frac{(v_\eta)_t}{aw},
       \partial_\theta\frac{(v_\eta)_\theta}{aw},
       \partial_\theta\frac{(v_\eta)_t}{aw}\right).
                                                               \tag{GHC.3}
\]
This is Mhol.13 with its complete weighted mean denominator.
Its ordinary mean is not set to zero.

Define
\[
 H_{\partial,\eta}(t)
    =\int_{t_f}^t a_{\rm ph}(s)w_{\rm metric}(s)
                             \dot\kappa_\partial(s)\,ds,
 \qquad H_{\partial,\eta}(t_f)=0.                              \tag{GHC.4}
\]
Differentiating (GHC.2) gives the exact identity
\[
 \boxed{\quad
 D_\gamma z[\eta]
    =v_\eta+H_{\partial,\eta}
       +H_{\rm met}[\mathfrak a_\eta]
       +D_\gamma\lambda[\eta].
 \quad}                                                       \tag{GHC.5}
\]
The endpoint and metric mean derivatives are separated by linearity
of the same actual small-root derivative, not by deleting a mixed term.
Their supports are disjoint before the directed height integrations.

## 2. The true finite collar and its available graph jets

Use Gseed's original
\[
 t=\log(a/a_B),\qquad -d\le t\le0,\qquad d=2^{-1024}.
\]
The actual coefficient is
\(A=(\log w)_t=1-S((-t)/2^{-24})\).
Gseed.G13 and G19 give, on this same collar,
\[
 |A+1|<4,\qquad
 |aw/s_B|<2,\qquad |s_B/(aw)|<2,\qquad s_B=a_Bw_B>0.
                                                               \tag{GHC.6}
\]
All design bumps vanish here. The actual and common-reference metric
are therefore identical on the whole collar.

Set \(V_\eta=\|v_\eta\|_{E_{20}^+}\).
The finite state part of E.3 gives the actual ordinary radial jets
\[
 \max_{a=0,1}d^a\sup_{[-d,0]}
       \|\partial_t^aZ(v_\eta)\|_{H^2}
                   \le2^{-440}V_\eta .                       \tag{GHC.7}
\]
Likewise GF.11 gives
\[
 \max_{a=0,1}d^a\sup_{[-d,0]}
       \|\partial_t^aZ(u)\|_{H^2}
                   <2^{-440-48000000}.                       \tag{GHC.8}
\]
In particular \(\|Z(u)_t\|_{A^0}<1\), since
\(1024-440-48000000<0\).

Every nonmean component here uses the full physical frequency set
\(4\mathbb Z\). The inequality \(A^0\le H^1\) on its nonzero modes
and the original scalar mean formulas are used in their respective
places. No arbitrary raw radial \(L^2\) trace is read in (GHC.7)
or (GHC.8).

## 3. The mean radial derivative is paid explicitly

Write
\[
 {\cal K}(t,Z)=\kappa(q_{\rm ph}(t),Z)
\]
on the actual first polynomial germ. Gseed.G13--G14 proves that
this full small-root map is holomorphic on
\(|t|<2^{-128}\) and the stated complex state ball of size \(2^{-10}\).
Its value may be bounded by \(2^{10}\), and its state derivatives
through order five by \(2^{80}\). These are function-parameter
statements about the coefficient and mean map. They do not assume
that the actual state is analytic in \(t\) or in its angle.

For the mixed derivative needed here, at every real point of the
collar a complex \(t\) circle of radius \(2^{-130}\) remains in
that germ, while a state circle of radius \(2^{-11}\) remains in
the same small-root ball. Cauchy on the genuine product domain,
with finite polarization, gives
\[
 \|D_Z{\cal K}\|,\ \|D_Z^2{\cal K}\|\le2^{80},\qquad
 \|\partial_tD_Z{\cal K}\|_{Z\ {\rm fixed}}\le2^{256};
                                                               \tag{GHC.9}
\]
indeed \(10+130+11+4<256\).
This last derivative includes the true \(q_{\rm ph}(t)\) dependence.

The actual chain rule is
\[
 \begin{split}
 (\dot\kappa_\partial)_t
  ={}&D_Z{\cal K}\,[Z(v_\eta)_t]
       +D_Z^2{\cal K}\,[Z(u)_t,Z(v_\eta)]\\
     &+(\partial_tD_Z{\cal K})_{Z\ {\rm fixed}}[Z(v_\eta)].
 \end{split}                                                   \tag{GHC.10}
\]
All three terms are retained. With (GHC.7)--(GHC.9),
\[
 |\dot\kappa_\partial|\le2^{-360}V_\eta,\qquad
 |(\dot\kappa_\partial)_t|\le2^{666}V_\eta.                     \tag{GHC.11}
\]
For the second estimate the exponents of the three terms are
\(664,-360,-184\); their positive sum is bounded by \(2^{666}\).
This directly pays the derivative of the actual mean map instead
of differentiating a small real norm estimate.

## 4. Mean and nonmean scalar height in the same two-jet norm

For a scalar field use the norm
\[
 \|h\|_{C^2_{t,\theta}}
   =\sum_{a+b\le2}\sup|\partial_t^a\partial_\theta^b h|
\]
on this collar, with its actual continuation on the body side.
For the angle-constant mean part there are only three nonzero terms.

By (GHC.4), (GHC.6), and (GHC.11),
\[
 \begin{split}
 |H_{\partial,\eta}|&\le s_B2^{-1383}V_\eta,\\
 |(H_{\partial,\eta})_t|&\le s_B2^{-359}V_\eta,\\
 |(H_{\partial,\eta})_{tt}|&\le s_B2^{668}V_\eta .
 \end{split}                                                   \tag{GHC.12}
\]
The first line uses the actual integration length \(d\).
For the third,
\[
 H_{\partial,tt}
    =aw\{(A+1)\dot\kappa_\partial
                          +(\dot\kappa_\partial)_t\},
\]
so the coefficient derivative is included.
The sum of the three lines is bounded by
\(s_B2^{670}V_\eta\).

For the nonmean height there is no separate unknown integration
constant. Its actual derivative identities are
\[
 \begin{gathered}
 (v_\eta)_\theta=aw\,p_\eta,\qquad
 (v_\eta)_t=aw\,k_\eta,\\
 (v_\eta)_{\theta\theta}=aw\,U_\eta,\qquad
 (v_\eta)_{t\theta}=aw\,V_\eta^{\rm state},\\
 (v_\eta)_{tt}
       =aw\{(A+1)k_\eta+(k_\eta)_t\}.
 \end{gathered}                                                \tag{GHC.13}
\]
The notation \(V_\eta^{\rm state}\) denotes the fourth state,
not the graph norm \(V_\eta\).
The value is recovered by the original zero-mean angular primitive,
whose \(A^0\) norm is at most \(1/4\) on \(4\mathbb Z\setminus\{0\}\).

From (GHC.6)--(GHC.7), the largest individual two-jet exponent in
(GHC.13) is at most 586. The sum of all six components is therefore
bounded by \(s_B2^{589}V_\eta\).
Together with the complete mean contribution,
\[
 \boxed{\quad
 \|v_\eta+H_{\partial,\eta}\|_{C^2_{t,\theta}}
     \le s_B2^{1024}\|v_\eta\|_{E_{20}^+}.
 \quad}                                                       \tag{GHC.14}
\]
The exponent before widening is at most 671.

At \(t=-d\), the true lift has its original zero jets. The endpoint
mean derivative and its radial derivative consequently also vanish
there. The integral (GHC.4) is zero on the body side before the
collar, so its extension across that join is \(C^2\). At \(B\) its
height and slope are actual output values, with their actual signs;
neither is reset to zero. No continuation through the long segment
is asserted by this local support statement.

GA.10 and \(W_{21}<1\) give
\[
 \|v_\eta\|_{E_{20}^+}
       \le2^{131073}\epsilon_L e_\eta.
\]
Hence
\[
 \boxed{\quad
 \|v_\eta+H_{\partial,\eta}\|_{C^2_{t,\theta}}
     <s_B2^{262144}\epsilon_L
                         r_\gamma^{-1}\|\eta\|_{A^0}.
 \quad}                                                       \tag{GHC.15}
\]
The actual combined exponent is only 132097 before this widening.
The only extra background index is 21, well inside the stated
\(E_{1856}^+\) value ball.

## 5. Original physical units and the complete scalar-height bound

In the original scaled material Cartesian chart
\[
 (x,y)=(a\cos\theta,a\sin\theta),\qquad a=a_Be^t,
\]
the collar has \(a>a_B/2\). The identities
\[
 \partial_x=a^{-1}(\cos\theta\,\partial_t-\sin\theta\,\partial_\theta),
 \qquad
 \partial_y=a^{-1}(\sin\theta\,\partial_t+\cos\theta\,\partial_\theta)
\]
and one further derivative give the safe complete conversion
\[
 \|h\|_{C^2_{x,y}}
       \le2^8\max(1,a_B^{-2})\|h\|_{C^2_{t,\theta}}.
                                                               \tag{GHC.16}
\]
The two first derivatives, three second derivatives, and derivatives
of the radial and trigonometric coefficients are all included.
This is a fixed material chart for the scalar height, not a
replacement of the full horizontal coframe reconstruction.

Combining (GHC.5), (GHC.15)--(GHC.16), and GHR.18--GHR.19 gives
the complete fixed-\(w\) scalar-height parameter estimate
\[
 \begin{split}
 \|D_\gamma z[\eta]\|_{C^2_{\rm material}}
 \le{}&|D_\gamma\lambda[\eta]|\\
 &+s_B2^{262152}\epsilon_L
       \max(1,a_B^{-2})\,r_\gamma^{-1}\|\eta\|_{A^0}\\
 &+\rho\varepsilon_s2^{1032-110000000}
       \max(1,\rho^{-2})\,r_\gamma^{-1}\|\eta\|_{A^0}.
 \end{split}                                                   \tag{GHC.17}
\]
The last line is the complete actual metric reference-height
column, including its unsuppressed reference \(1\), both endpoint
heights, and the actual shallow \(o\) contribution.
The second line is the full endpoint-graph nonmean plus mean
column on the unchanged B collar.
Each physical scale belongs to its original region and readout.
Neither is set to 1 to simplify the displayed bound.

When the global height input \(\lambda\) is fixed, its derivative
in (GHC.17) is exactly zero. If a matching equation selects
\(\lambda=\lambda(\gamma,w)\), that actual scalar derivative must
be added. In particular the unscreened cap--long mean-height
span may enter that matching equation. This proof does not
remove it by declaring the endpoint slope to be screened.

The two individual mean heights and the complete conormal
column of GHR remain outputs. For the endpoint column the
true B mean slope is
\(s_B\dot\kappa_\partial(0)\).
It is the derivative of the same holonomy small root which
matches the cap--long state, not an independently prescribed
zero slope.

## 6. Joint operator continuity and scope

For \(v_\eta:A^0\to E_{20}^+\), GA.11 gives joint operator
continuity when gamma varies in its relative \(A^0\) topology
and \(w\) varies in \(E_{21}^+\).
The original value domain and its low ball are retained.
The actual background \(u={\cal U}_\gamma w\) is continuous
in \(E_{20}^+\) in the same topology, by S's true far coordinate
and GA's integrated endpoint derivative bound.

On the fixed collar, (GHC.7)--(GHC.10) express the complete
mean derivative using continuous coefficient operators and
the actual first radial graph jets. Thus its directed
integral and the entire map in (GHC.15) vary continuously
in operator norm \(A^0\to C^2_{t,\theta}\).
GHR proves the corresponding operator continuity for the
whole infinite metric column. The fixed chart conversion
does not change this conclusion.

Consequently, with the independent global height input
held fixed, the full partial parameter-height operator
\[
 (\gamma,w)\longmapsto D_\gamma z(\gamma,w,\lambda)
     \quad\hbox{in }{\cal L}(A^0,C^2_{\rm material})
\]
is jointly continuous on this domain, with \(w\) in \(E_{21}^+\).
This is an assertion about the actual scalar-height
reconstruction at fixed physical nonmean coordinate.
It neither assumes differentiability of the selected
nonlinear solution nor claims that varying the actual
design parameters gives a fixed-metric isometric family.
The complete horizontal coframe, spatial frame, and
position matching retain their separate equations.

## 7. New saved-bound arithmetic

The companion
[fourfold_codazzi_complete_parameter_height_saved_bounds.py](../scripts/fourfold_codazzi_complete_parameter_height_saved_bounds.py)
records the 9 new exact integer combinations.
Their first execution in code mode after local environment
loss passed all 9. The Python text preserves those same
operations; it was not run in the unavailable environment.

Only already completed GA, GHR, Gseed, E, and mean-root
bounds are combined. No earlier saved-bound comparisons,
native arrays, long kernels, profile integrals, or prior
scientific targets were rerun.
