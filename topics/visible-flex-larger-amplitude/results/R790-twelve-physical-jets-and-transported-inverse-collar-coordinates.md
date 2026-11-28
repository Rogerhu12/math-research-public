# R790. Two inverse labels for one physical cap trajectory and its six material jets

The tube branch of the full R763 shared-rim problem evaluates the R761 moving cap. At a fixed material point its two planar coordinates satisfy a time-dependent ODE. Each of the two planar coordinates carries its value, two first material derivatives, and three second material derivatives. The R761 ODE computes its velocity using two inverse coordinate maps at each right-hand-side evaluation. Here those inverse labels also evolve along the physical trajectory. This gives an equivalent continuum initial-value problem on regular coordinate patches and permits one forward traversal for multiple requested angular endpoints. The complete two end caps and the two continuous material derivatives are retained. The new numerical source changes the adaptive integration path. Its actual floating-point words, timings, failures and fitted points must be measured by its own original-budget run.

## The original physical maps

Use the R761 and R763 material charts, the unchanged R757 initial closed metric, and the original paired-profile design. At angular motion time \(\theta=A\sin t\), let \(C_\theta(s,w)\) denote the two-dimensional moving normal-coordinate map implemented by the R761 function normal. Let \(P_\theta\) be the complete R761 planar material map, and set \(B_\theta(s,w)=P_\theta(C_0(s,w))\). Its initial map is \(B_0=C_0\) for the real integral fields. The actual working values and original inverse residual checks are used at the start as well.

At a moving world point \(X\), write \(b=B_\theta^{-1}(X)\) and \(c=C_\theta^{-1}(X)\) on the two regular local chart branches selected by the original construction. For the finite strip width \(h=.00035\), define
\[
 \omega(b)=1-S_7((b_w-.35h)/(.65h)),\qquad
 V_b=\partial_\theta B_\theta(b),\qquad V_c=\partial_\theta C_\theta(c).
\]
The two velocity maps are the original R761 planar and normal velocity evaluators. The old world velocity is
\[
 V(X,\theta)=V_b+\omega(b)(V_c-V_b).
\]
All of these are two-dimensional physical vectors. The time parameter here is the same actual angular deformation parameter used in R761; it is distinct from the azimuthal material coordinate. The physical complement of the flow band uses the original full direct map, and the original nonflat crown is added at the requested endpoint. The true zero-width/near-rim normal-coordinate override from R763 is used at precisely its original \(w\le10^{-8}\) inputs.

## The four additional scalar equations

Retain the world equation \(\dot X=V\) and append
\[
 \dot b=(D B_\theta(b))^{-1}(V-V_b),\qquad
 \dot c=(D C_\theta(c))^{-1}(V-V_c).
\]
Both added states have two scalar components. In real arithmetic,
\[
 \frac{d}{d\theta}(B_\theta(b)-X)=V_b+D B_\theta(b)\dot b-V=0,\qquad
 \frac{d}{d\theta}(C_\theta(c)-X)=0 .
\]
Their differences vanish at the common material start. On the same regular inverse branches this preserves \(B_\theta(b)=X=C_\theta(c)\). Conversely, differentiating the actual original inverse coordinates along the original physical solution gives these four scalar equations. This is an equivalence for the entire original active strip on its original nonsingular domain, including its transition. It does not replace the blending clock by its endpoint values. A genuine loss of invertibility remains an original physical evaluation failure.

For either inverse map \(H\) and physical material coordinates \(\alpha,\beta\), the two first and three second material derivatives of its inverse labels are obtained from the same matrices as the original Newton implementation:
\[
 H' q_\alpha=X_\alpha,\qquad H'q_\beta=X_\beta,\qquad
 H' q_{ij}=X_{ij}-H''[q_i,q_j],\quad ij=\alpha\alpha,\alpha\beta,\beta\beta .
\]
Thus the physical two-component state still transports twelve material-jet entries. Composing \(V_b,V_c,\omega\) with the full recovered label two-jets gives the same two original six-jet velocity rows, including the mixed derivative. The four predictor scalars require only the first coordinate matrices. No third derivative of the coordinate maps is introduced. The Run44 JAX optimizer differentiates the original physical Gram, curvature and pair objective with respect to the corrected physical field. The prescribed cap trajectory is a base field in that optimizer; the original shape adjoint and its material derivatives stay in use.

## Multiple actual endpoints and two physical sides

For a list of requested positive physical angles in increasing order, continue each original physical material block forward from one requested angle to the next. ODE uniqueness and composition on adjacent intervals give the same real trajectory as integrating from zero to each of those angles separately. Each requested angle is an actual solver endpoint. The material inputs, order, ramp-cell count, entire requested angle set, and all twelve original planar material input words identify the runner-local temporary table. Both complete signed caps have exactly the same two initial planar six-jets at matching material coordinates: the original R757 chart applies the upper/lower sign only to the axial height component \(Y\) in the ordered tuple \((X,Y,Z)\). The material \(X,Z\) formulas are identical. The R761 moving planar map and crown depend on the same \(X,Z\); each cap then applies its own axial sign to the complete crown six-jet. Sharing an identical planar input therefore preserves the two full physical charts and their opposite axial displacements. Unequal Cartesian, polar, or normal input jet words retain separate computations.

The production interface preserves the R763 translated and developed branches, the original paired cylinder and rolls, the original direct and active material subsets, the original source chunk size 32 and every original post-transport crown and material value. The first near search is the true original 32768-station tree and mask \(d<h+.00050\); the true initial inverse then decides \(w<h\), as before. Zero phase uses the complete old initial field. The terminal exporter requests the actual union of its independent phases and seven mesh phases. The target, nine chart labels, both full outer normal-geometry indices, every original accepted or rejected solver step, and all original budgets retain their respective definitions.

## Working arithmetic and actual evidence

The integration uses the original DOP853 coefficients, relative tolerance \(2\,10^{-9}\) and absolute tolerance \(2\,10^{-11}\). The SciPy 1.17.0 DOP853 component error estimator is applied separately to the original twelve physical rows and the four added rows; the step uses their larger value. Adding auxiliary coordinates cannot dilute the physical error estimate. Each requested endpoint also recomputes the inverse labels with unchanged physical words before the next interval. The regularity floor \(|\det D H|\ge10^{-11}\) and forward inverse residual \(\le3\,10^{-10}\) are checked on both actual chart maps. A physically good predictor can take an original Newton polishing step. A failed predictor or failed polish calls the original two-jet Newton inverse with its original branch seed: the initial normal labels for \(B\), and the recovered \(B\)-labels for \(C\). Its original loop, determinant and residual checks apply. If the augmented integration fails numerically, the defining full R761 move routine evaluates the complete same original material block separately for every remaining requested angle. An original fallback failure is still reported; no missing row or phase is synthesized.

Independent original blocks may use up to the four public runner CPUs. The scalar publications record the actual material rows, angular intervals, right-hand-side calls, returned coordinate residuals and determinants, actual Newton/fallback usage and worker progress. Temporary transport data stay on the runner, with exact-key eviction followed by recomputation when needed. These counters cannot establish a speedup in advance or establish the fixed-metric scientific target. For a genuine continuation of the original finite optimization, the new physical provider, its numerical sources, the complete original objective/field/parameters and original library versions are all bound in the new run. Original Run44 and Run45 remain independent histories.

The [augmented physical kernel](../scripts/resume_20261126/r790_augmented_collar_flow.py) implements the inverse charts, twelve physical jet rows, original numerical recovery, and actual endpoint integration. The [complete closed geometry provider](../scripts/resume_20261126/r790_multiphase_tube_transport.py) supplies the same R763 physical branches, both filled caps and their genuine material joins. All actual results require a public scientific return from these sources.
