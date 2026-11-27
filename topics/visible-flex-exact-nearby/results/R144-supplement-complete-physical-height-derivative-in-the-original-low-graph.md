# R144 GHW: complete physical height differentiation in the original low graph

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 10 new exact integer comparisons pass.**
At fixed gamma and fixed one global height input, the actual S/T scalar
height reconstruction satisfies
\[
 \|D_w z(\gamma,w)[h]\|_{\mathcal Z^2}
                       \le2^{2048}\|h\|_{E_{20}^+}.
\]
Here \(\mathcal Z^2\) is the complete original piecewise physical
\(C^2\) readout, including the whole finite connector, infinite tail,
and flat-end limits. It does not silently impose missing one-sided
jet matching on an arbitrary graph direction.

The actual installation also converts GHC's explicit scale factors
into the uniform bound
\[
 \|D_\gamma z(\gamma,w,\lambda)[\eta]\|_{\mathcal Z^2}
             <2^{-56000000}r_\gamma^{-1}\|\eta\|_{A^0}
\]
when \(w\) and the one global \(\lambda\) are fixed.
All ordinary mean, first-principal metric feedback, endpoint
straightening, and physical scale factors are included.

For the actual zero-residual selected family, the original matching
jets form a closed subspace of this complete readout. Thus a separately
proved \(E_{20}^+\) selected derivative passes to a genuine \(C^2\)
height derivative on its original tail--connector domain. This does
not grant arbitrary graph directions automatic global \(C^2\) matching
or declare the full closed surface problem solved.

## 1. Completed inputs, physical norms, and fixed parameters

Use:

- [S: the actual nonlinear far graph](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md);
- [T: the actual selected family and common reference](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md);
- [E: the original graph and exact height reconstruction](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md);
- [J: the complete broken radial jets and original trace qualifications](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md);
- [Mhol: the actual holonomy mean and height graph](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md);
- [L: the genuine low-norm first-principal value map](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md);
- [G: the complete first-parameter height column](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md);
- [GHR: the complete metric height and full profile sums](R144-supplement-actual-seed-metric-reference-height-and-complete-endpoint-column.md);
- [GHC: the true partial parameter-height column](R144-supplement-complete-actual-parameter-height-at-fixed-physical-coordinate.md);
- [the actual fixed-stop object's installation](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md), denoted Sobj;
- [D: the unchanged true long radial segment](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md).

The body here is the original infinite tail plus its same finite
connector through the B section. The material coordinate and the
installation scales are fixed. Gamma is in T's original
\(H^{8193}\) value domain, and
\[
        \|w\|_{E_{1856}^+}\le2^{-49000000}.
\]
Directions \(h\) lie in the original nonmean fixed-linear-boundary
graph \(E_{20,0}^+\). The independent rigid height and any independently
prescribed flux or compatibility data remain separate inputs.

Let \(\mathcal Z^2\) denote the sum of the suprema of the value and all
physical material Cartesian derivatives through order two, taken
piece by piece on the original partition and including their actual
one-sided endpoint representatives. Its height gauge is not removed
separately on each piece.

The original linear traces stay in force. As J section 1 and section 4
state, an ordinary broken-jet bound does not create additional
one-sided source or state compatibility. Accordingly the initial
operator statement is into \(\mathcal Z^2\). The precise global
\(C^2\) conclusion for compatible exact solutions is given in section 8.

## 2. The true tangent coordinate and the exact height decomposition

At fixed gamma,
\[
 u={\cal U}_\gamma w,\qquad
 J_w=D_w{\cal U}_\gamma
       =I+{\cal L}_\partial D_fq_\gamma(F_Bw)F_B .
                                                               \tag{GHW.1}
\]
This is S's actual nilpotent coordinate; it is not replaced by the
identity. The full mixed kernel bound S.14--S.16 at \(r=21\)
uses precisely the added physical \(H^{23}\) B-height trace in
\(E_{20}^+\). With the original gamma high gate included in
\(K_\partial=2^{6291456}\), the low derivative correction has a
strict small margin:
\[
                 6291456-49000000+16<-2 .
\]
Allowing the actual common-reference comparison gives the safe bound
\[
                         \|J_wh\|_{E_{20}^+}<4\|h\|_{E_{20}^+}.
                                                               \tag{GHW.2}
\]

Set \(v=J_wh\). At the current metric let \(\kappa_h\) be the fixed-metric
holonomy-mean derivative in this physical nonmean direction, and define
\[
 H_h(t)=\int_{t_f}^t a_{\rm ph}w_{\rm metric}\kappa_h\,ds,
                       \qquad H_h(t_f)=0 .
                                                               \tag{GHW.3}
\]
The first design parameter also varies. By the exact full-domain
support identity GF.4, its derivative in direction \(v=J_wh\)
equals its derivative in direction \(h\) on the original principal
input. The second seed parameter is fixed when gamma is fixed.

Let \(H_{\Gamma_1,h}\) be the complete reference-height column of
that genuine first-parameter variation, including its mean response.
Then the scalar height derivative is exactly
\[
             D_w z[h]=v+H_h+H_{\Gamma_1,h}.                   \tag{GHW.4}
\]
An independently varied global height adds its single scalar
derivative. Formula (GHW.4) retains the reference-height term and
the complete first-principal response; it is not a fixed-metric
proxy derivative.

For the fixed-metric four states of \(v\), use a common size
\[
 \Sigma=16\|h\|_{E_{20}^+}.
\]
The actual scalar multiplier from the common reference and its first
scaled radial derivative are bounded by the original small profile
budgets. The seed reference part costs at most
\(2^{1048576-110000000}\), and the first-principal part at most
\(2^{170016-2\cdot48000000}\); even after a fixed factor \(2^{16}\)
their sum is \(<1/16\).
Consequently E.3 and (GHW.2) give
\[
 \begin{split}
 \max_{a=0,1}\ell_j^a
       \|\partial_t^aZ_v\|_{H^2}
       &\le C_j\Sigma \quad\hbox{on each original cell},\\
 \max_{a=0,1}\ell_o^a
       \|\partial_t^aZ_v\|_{H^2}
       &\le2^{-440}\Sigma
          \quad\hbox{on the finite connector},
 \qquad\ell_o=2^{-1024}.
 \end{split}                                                   \tag{GHW.5}
\]
These are genuine radial jets of the graph direction. They are not
derived from an arbitrary radial \(L^2\) input.

## 3. The complete mean direction and its actual radial derivative

Write the actual mean small root as \(\kappa(q,Z)\), with
\(Z=(P,K_\perp,U,V)\) and the original angular derivative constraints.
The fixed-metric mean derivative is exactly
\[
       \kappa_h=D_Z\kappa(q,Z)[Z_v].
\]
The quadratic removable holonomy formula, with its mean denominator
\(>3/4\), is analytic on the same complex state and scalar-q balls
used in Mhol/GHR/Gseed. For the low derivatives needed here, its
complete coefficients can be bounded by
\[
 \|D_Z\kappa\|,\quad \|D_Z^2\kappa\|,\quad
                         \|D_qD_Z\kappa\|\le2^{80}.           \tag{GHW.6}
\]
This is the original conservative state-derivative budget. It can
also be read directly from the removable quotient by one state
circle of radius \(2^{-11}\), one q circle of radius \(1/8\),
and the already bounded small-root value. It uses a genuine
function-parameter domain, not a spatial analytic extension.

The actual radial derivative is
\[
 (\kappa_h)_t
  =D_Z\kappa[Z_{v,t}]
      +D_Z^2\kappa[Z_t,Z_v]
      +D_qD_Z\kappa[q_t,Z_v],\qquad q_t=2Aq .
                                                               \tag{GHW.7}
\]
No term in this formula is removed.

The actual background \(Z_t\) is uniformly small despite the
shrinking graph radial scales. Indeed, on the internal cells,
\[
 \begin{split}
 C_j\ell_j^{-1}
 &=2^{264}J_j^2h_j^{-5}
               (\zeta_j/\mu_j)\delta_j^{-6}\\
 &\le2^{264}J_j^3h_j^{-10}
               (\zeta_j/\mu_j)\delta_j^{-57/2}
 <2^{262408}.
 \end{split}
\]
Here \(h_j<1\) and \(\delta_j<1\), and the final bound is the
already completed T.C.13 profile, including its full finite prefix.
With GHR's actual background radius \(R=2^{-47000000}\),
\(\|Z_t\|_{A^0}\le C_j\ell_j^{-1}R<1\).
On the finite connector the same fact is GHC's already completed
finite radial graph bound.

Also \(q<1/4\) on these actual domains. Internally this follows
from Mhol.3; on the finite connector Sobj.13 gives
\(w/a<5/18\) and \(a<7\cdot10^{-6}\), hence an even smaller \(q\).
Thus \(|q_t|\le|A|/2\).
Since \(1+|A|\le\ell_j^{-1}\) internally, (GHW.5)--(GHW.7) give
\[
 |\kappa_h|\le2^{80}C_j\Sigma,\qquad
 |(\kappa_h)_t|
                   \le2^{82}C_j\ell_j^{-1}\Sigma.             \tag{GHW.8}
\]
On the finite connector, \(|A|\le7\), and the same computation with
\(\ell_o=2^{-1024}\) gives the safe complete bounds
\[
          |\kappa_h|\le2^{-360}\Sigma,\qquad
          |(\kappa_h)_t|\le2^{666}\Sigma.                     \tag{GHW.9}
\]
The latter exponent includes all three positive terms of (GHW.7).

This argument is valid on the stated nearby holonomy-one graph,
including nonzero ordinary residuals. It does not invoke
\(K_t=\mathcal F\) to manufacture a radial derivative. General
independent flux charges are not included in this holonomy-one
direction and keep their original separate columns.

## 4. The actual installation removes the internal physical scale loss

The internal material radius is \(a=\rho r\).
Mhol.3 and the exact definitions give
\[
 \begin{split}
 \frac wa C_j\ell_j^{-1}
 &\le2^{129}\frac{\mu_j}{\rho\delta_j}\,
    2^{200}h_j^{-5}
       \frac{\zeta_j}{\mu_j\delta_j^2}\,
    2^{64}J_j^2\delta_j^{-4}\\
 &=2^{393}\rho^{-1}
                    J_j^2h_j^{-5}\zeta_j\delta_j^{-7}.
 \end{split}                                                   \tag{GHW.10}
\]
Use GHR's complete sum, not a new integral:
\[
 \sum_{j\ge129}J_j^3h_j^{-5}\zeta_j\delta_j^{-7}
                                      <2^{-300}\varepsilon_s.
\]
The actual installation Sobj.17 is
\(\varepsilon_s/\rho<2^{440}\). Therefore
\[
             \sup_j \frac wa C_j\ell_j^{-1}<2^{533}.           \tag{GHW.11}
\]
Both profile junctions, the actual normalization factors, and the
whole shallow prefix are included. The physical scale was consumed
by an original inequality; it was not set to one.

For a fixed-metric nonmean physical height \(v\), the exact polar
derivative formulas are
\[
 \begin{gathered}
 v_a=wk,\qquad a^{-1}v_\theta=wp,\qquad v=awI_\theta p,\\
 (\nabla^2v)_{aa}=\frac wa(k_t+Ak),\\
 (\nabla^2v)_{a\theta}=\frac wa(V-p),\qquad
 (\nabla^2v)_{\theta\theta}=\frac wa(U+k).
 \end{gathered}                                                \tag{GHW.12}
\]
They require no PDE and retain the full radial derivative \(k_t\).
The primitive is the original zero-mean primitive on nonzero
\(4\mathbb Z\) modes.

The internal installation has \(a\le2\rho<1\). Combining
(GHW.5), \(1+|A|\le\ell_j^{-1}\), and (GHW.11), then converting
the orthonormal polar components to Cartesian components, bounds
the complete internal nonmean height readout by
\[
                 \|v\|_{\mathcal Z^2,\rm int}
                                      \le2^{550}\Sigma.       \tag{GHW.13}
\]
This includes the value, both first derivatives, and all second
derivatives.

For the mean height in (GHW.3),
\[
 (H_h)_a=w\kappa_h,\qquad
 (H_h)_{aa}=\frac wa\{(\kappa_h)_t+A\kappa_h\},
 \qquad
 (\nabla^2H_h)_{\theta\theta}=\frac wa\kappa_h .
                                                               \tag{GHW.14}
\]
Equations (GHW.8) and (GHW.11) bound its derivatives. Its value
must additionally be integrated once from the same flat end:
\[
 \begin{split}
 \int_{\rm tail}aw|\kappa_h|\,dt
 &\le\rho\,2^{212}\sum_j\mu_jC_j\Sigma\\
 &=\rho\,2^{412}\sum_jh_j^{-5}\zeta_j\delta_j^{-2}\Sigma\\
 &\le\rho\varepsilon_s\,2^{112}\Sigma<2^{112}\Sigma .
 \end{split}                                                   \tag{GHW.15}
\]
The same GHR full profile sum applies since
\(h_j^{-5}\zeta_j\delta_j^{-2}\le
 J_j^3h_j^{-5}\zeta_j\delta_j^{-7}\).
No endpoint height is reset. With all component sums,
\[
                    \|H_h\|_{\mathcal Z^2,\rm int}
                                         \le2^{640}\Sigma.    \tag{GHW.16}
\]
The deep positive powers also make the derivatives and the
directed height tails tend to zero uniformly at the flat end.

## 5. The whole finite connector, including its root and both signs

Use the actual Sobj.13 bounds on the entire finite connector:
\[
 \frac wa<5/18,\qquad |A|\le7,\qquad
 a<7\cdot10^{-6},\qquad \text{total }|t|\text{-length}<127 .
                                                               \tag{GHW.17}
\]
These hold through the actual preparation, amplification, new
simple-root transition, and fixed stopping platform. They are not
restricted to GHC's short positive collar.

The fixed-metric four states and their first radial derivative
are (GHW.5). Formulas (GHW.12) give a complete finite nonmean
height bound below \(2^{600}\Sigma\).
In particular the largest ordinary state derivative costs
\(2^{1024-440}=2^{584}\); it is multiplied by the true
\(w/a<5/18\) in the physical Hessian. A bare \(a^{-2}\) is
not introduced and then left unpaid.

For the mean, (GHW.9) and (GHW.14) bound the derivatives on
both signs and at the root without dividing by \(Q=-A\).
The additional directed mean-height span is at most
\[
       127\,\sup_{\rm con}(aw)\,2^{-360}\Sigma
                                           <2^{-353}\Sigma ,
\]
since \(aw<1\). The inherited constant in (GHW.15) remains
part of the same value. All finite mean components fit
\(2^{700}\Sigma\).

Combining the internal and finite components, with their
original readouts and the single height integral, gives the
safe fixed-metric bound
\[
                  \|v+H_h\|_{\mathcal Z^2}
                                         \le2^{704}\Sigma.    \tag{GHW.18}
\]
No sign-changing coefficient was inverted in this argument.
All source/interface qualifications remain the original ones.

## 6. The true first-principal metric height is also paid

At fixed gamma the second parameter is fixed, but the first one
has its actual derivative. L.17/G.19 give its full internal
support sum
\[
 g_{1,j}\le2^{9216}J_j^2\delta_j^{-1}C_j^\#
                  R\,{\cal D}_8(h),\qquad
 g_{1,o}\le2^{8960}R\,{\cal D}_8(h),
                                                               \tag{GHW.19}
\]
including the full inverse \((I-D_pT)^{-1}\).
The actual common-reference comparison gives
\({\cal D}_8(h)\le4\|h\|_{E_{20}^+}\).

To consume the already proved GHR scalar-height inequalities,
use the following numerical majorant only:
\[
                  \tau_{\rm maj}
                     =2^{9154}R\|h\|_{E_{20}^+}.
\]
Since \(J^2\delta^{-1}\le J^3\delta^{-5}\), (GHW.19) is
bounded by GHR.9 with this scalar majorant. The shallow
row fits its separate GHR.10 bound because
\(8960+2<14+9154\).
This is not a claim that a first-parameter direction is a
second-parameter vector. GHR.2--GHR.18 prove a height estimate
from the displayed actual bump sums and the exact mean
formula; those scalar inequalities apply to this genuine
first-parameter direction as well.

The physical scale factor in GHR.18 is fully paid:
\[
 \rho\varepsilon_s\max(1,\rho^{-2})
       =\varepsilon_s/\rho<2^{440},
\]
because the actual \(\rho<1\).
Thus
\[
 \|H_{\Gamma_1,h}\|_{\mathcal Z^2}
   \le2^{9154+1024+8+440}R\|h\|_{E_{20}^+}
   <2^{12000}R\|h\|_{E_{20}^+}
   <\|h\|_{E_{20}^+}.                                       \tag{GHW.20}
\]
The complete reference \(1\), its two endpoint heights, and
the original conormal column remain in this estimate.

Finally (GHW.4), (GHW.18), \(\Sigma=16\|h\|_{E_{20}^+}\),
and (GHW.20) prove
\[
 \boxed{\qquad
     \|D_w z(\gamma,w,\lambda)[h]\|_{\mathcal Z^2}
                       \le2^{2048}\|h\|_{E_{20}^+},
 \qquad \lambda\ \hbox{fixed}.
 \qquad}                                                       \tag{GHW.21}
\]
The complete exponent before widening is below 710.
If \(\lambda\) is varied, its single scalar derivative is
added to the right side; it is not a norm of each component's
independently chosen constant.

## 7. The actual physical partial-gamma height is uniformly small

GHC.17 retained the two actual installation factors.
They can now be evaluated with the completed original
geometry. D.2 gives
\[
 a_B<1,\qquad
 s_B\max(1,a_B^{-2})=\frac{w_B}{a_B}
                 =\frac1{4\omega_*}<\frac5{28}<1 .
\]
Sobj.16--Sobj.17 give
\[
 \rho<1,\qquad
 \rho\varepsilon_s\max(1,\rho^{-2})
                         =\varepsilon_s/\rho<2^{440}.
\]
Consequently the endpoint and metric terms in GHC.17
have exponents at most
\[
             262152-57000000,\qquad
             1032+440-110000000 .
\]
Their complete sum is bounded by
\(2^{-56737847}<2^{-56000000}\).
Therefore at fixed \(w,\lambda\),
\[
 \boxed{\qquad
 \|D_\gamma z(\gamma,w,\lambda)[\eta]\|_{\mathcal Z^2}
       <2^{-56000000}r_\gamma^{-1}\|\eta\|_{A^0}.
 \qquad}                                                       \tag{GHW.22}
\]
This consumes the actual fixed scales without changing them.
The full ordinary mean, the reference height \(1\), the
complete two-parameter response, and all endpoint units
remain exactly those of GHC/GHR.

The cap--long unscreened mean-height span is still a separate
matching output. If that equation chooses the global height
input as a function of gamma, its actual derivative must be
added to (GHW.22). The estimate does not declare such a
derivative zero.

## 8. Differentiability, the original matching jets, and exact selected solutions

For fixed gamma, S.14--S.16 gives the genuine \(C^1\)
endpoint coordinate on the low \(E_{20}^+\) graph; its
\(r=21\) estimate uses the actual added \(H^{23}\) trace.
L gives the true \(C^1\) principal value map on its
\({\cal D}_{20}\) domain. Mhol gives the complete small-root
mean derivative, and the radial jets in E.3 give the
ordinary derivatives used above. These establish that
the scalar-height reconstruction is \(C^1\) into
\(\mathcal Z^2\), with (GHW.21).

The derivative is continuous in its actual operator norm
when \(w\) varies in \(E_{20}^+\) and gamma in its original
relative \(H^{8193}\) topology. The finite pieces use the
true endpoint kernel, real principal operator, mean
formula, and original physical coefficients. The
infinite physical tail uses the uniformly vanishing
profiles in (GHW.10), (GHW.15), and GHR; it is not justified
by an unsupported supremum of coordinatewise derivatives.
The partial gamma-height continuity from GHC is retained
with its stated \(E_{21}^+\) background topology.

To obtain a global \(C^2\) height on the original body,
one must retain the original matching conditions.
Value, first-jet, and second-jet equality at every true
interface are closed linear conditions in the complete
\(\mathcal Z^2\) readout. The uniformly vanishing deep
profiles also preserve the flat-end two-jet conditions.
Hence the set of globally \(C^2\) scalar heights on this
tail--connector domain is a closed subspace of the
specified readout space.

For actual selected exact solutions, the original
continuous height/state traces and the exact two PDE
rows identify the second jets, as in the original
finite Nash convergence proof. Thus their heights
belong to this closed subspace. Every difference
quotient of those actual heights has the same matching.
If the separately established selected-coordinate
difference quotients converge in \(E_{20}^+\), with the
higher background continuity required by GHC, then
(GHW.21)--(GHW.22) and the true chain rule give convergence
in \(\mathcal Z^2\). The closed matching conditions
therefore give a genuine global \(C^2\) scalar-height
derivative on that original body.

This explains exactly how the low selected derivative
is consumed. It does not claim that an arbitrary broken
graph direction already has matching second jets, does
not grant a new bare trace to a radial \(L^2\) direction,
and does not assume onto solvability of any rough-source
operator.

The statement concerns scalar height. The original
horizontal coframe, single spatial frame, position
periods, core matching, and the final fixed-metric
family still have their own equations. The northern
physical height keeps its original overall sign
\(Z_0-z\); the norm estimates above are unchanged
by that fixed sign.

## 9. New saved-bound combinations

The companion
[fourfold_codazzi_low_graph_physical_height_saved_bounds.py](../scripts/fourfold_codazzi_low_graph_physical_height_saved_bounds.py)
contains 10 new exact integer combinations. Each was
executed once in code mode after the local environment
became unavailable; all passed. The Python reader
records the same operations and was not run in the
unavailable local environment.

Only completed profile sums, actual installation
bounds, endpoint graph constants, and real mean/
principal columns are combined. No earlier successful
comparison, native array, profile integral, long
kernel, or scientific target was rerun.
