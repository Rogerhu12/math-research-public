# R749 — A genuinely \(C^2\) nonlinear isometric continuation at the displaced straight wall

2026-11-28. On an actual material interval of the R746/R747 right turn, the specified initial end metric has positive Gaussian curvature for every sufficiently small \(v>0\). After a finite phase the complete locked central cylinder supplies a *straight* entrance line with its full flat two-jet. The one-sided \(C^4\) continuation is impossible there by R747. We construct a one-sided \(C^2\), non-\(C^3\), exact local isometric embedding for the **same metric and the same actual entrance jets**. It works on a common positive-width rectangle for a whole finite interval of phases. The exponent \(5/2\) converts the full nonlinear Darboux equation into an analytic noncharacteristic Cauchy problem in the *longitudinal* variable.

The width in this proof is existential. The construction also gives closed thick starting fields containing this exactly solved patch. It does not solve the remaining rolled annuli or caps, and does not claim a quantitative fixed-domain convergence certificate.

## 1. The actual material interval and target

Use the [R746 axial family](R746-circular-grip-periodic-translation-and-physically-free-closed-ends.md) and [R747 full material atlas](R747-offset-ring-arclength-transport-and-the-physical-end-cost.md). Let \(r=.15,\ \epsilon_x=.001\). On the upper right clockwise half-turn let
\[
 s_*=s_1+\epsilon_x/2+r(\pi-.5),\qquad x=s-s_* .
\]
For \(|x|<.02\) the original material profile is genuinely circular, \(\kappa(s)=\kappa_*=1/r=20/3\). For every \(1\le\theta\le\pi/2\) the shifted coordinate \(s+r\theta\) belongs to the interior of the straight right wall. Its arclength past the turn endpoint is \(x+r(\theta-.5)-\epsilon_x/2\), positive and \(<.19\), while that wall has length \(>.739\). The trace at either transverse edge, viewed before the common rigid rotation, is consequently a physical line with constant longitudinal unit tangent \(T\), transverse tangent \(\sigma e_y\) for side \(\sigma=\pm1\), constant outward planar unit normal \(n\), and zero entire second jet. Write \(v=0\) at that edge; \(v<0\) is the physical cylinder continuation in its straight material coordinates.

The fixed metric on the positive rolled side is
\[
 g=A^2dx^2+dv^2,\quad A=1-\kappa_*d(v),\quad d'=\sin\eta,\quad d(0)=0 .
\]
In the actual entrance ramp \(0\le v<\epsilon_y=1/2000,\ r_y=27/250\), the primitive of its true curvature is
\[
 \eta(v)=\frac{1}{r_y}\left(\frac{5v^4}{2\epsilon_y^3}
                  -\frac{3v^5}{\epsilon_y^4}+\frac{v^6}{\epsilon_y^5}\right).
\]
The analytic continuations of \(d,A\) across 0 serve only as analytic coefficients of the positive-side problem. Physically the cylinder at \(v<0\) remains the original plane. In particular
\[
 d=d_5v^5+O(v^6),\quad d_5=\frac1{2r_y\epsilon_y^3}>0,\qquad
 K_g=-A_{vv}/A=\kappa_*d''/A .
 \tag{1}
\]
The metrics of the undeformed R746 and R747 maps agree at \(\theta=0\); the named height and cap deformations vanish then. This fixes the actual target for the whole argument.

## 2. Remove the fractional degeneracy in the exact Darboux equation

Write \(z\) for the height in direction \(n\) from the flat entrance plane and set \(z=v^{5/2}u(x,v)\) for \(v\ge0\). We seek the intrinsic Darboux equation
\[
 \det\operatorname{Hess}_g z
   =K_g\det(g)\left(1-|\nabla_g z|^2\right),                            \tag{2}
\]
where the determinant on the left uses covariant components in \((x,v)\). The following quantities involve analytic integer powers of \(v\):
\[
 \begin{split}
 T_0&=\tfrac52u+vu_v,\qquad
 B=\tfrac{15}{4}u+5vu_v+v^2u_{vv},\\
 D_0&=\tfrac52u_x+vu_{xv}-v(A_v/A)u_x,\\
 W^2&=1-v^5u_x^2/A^2-v^3T_0^2,\qquad
 C=\kappa_*A\,d''/v^3 .
 \end{split}
 \tag{3}
\]
In the first two coordinates of \(g\) the relevant Christoffel symbols are \(\Gamma^x_{xx}=A_x/A,\ \Gamma^v_{xx}=-AA_v,\ \Gamma^x_{xv}=A_v/A\). Here \(A_x=0\), but keeping the term makes the longitudinal calculation transparent. The \(vv,xv,xx\) components of the Hessian are respectively
\[
 v^{1/2} B,\qquad v^{3/2}D_0,\qquad
 v^{5/2}\big[u_{xx}-(A_x/A)u_x+(AA_v/v)T_0\big].
\]
Dividing (2) by \(v^3\) on the positive side therefore gives **exactly**
\[
 u_{xx}=(A_x/A)u_x-(AA_v/v)T_0+\frac{D_0^2+C W^2}{B}.                 \tag{4}
\]
Equation (1) makes \(A_v/v\) and \(d''/v^3\) analytic at zero, with \(C(0)=20d_5\kappa_*\). No singular coefficient remains.

Prescribe analytic Cauchy data on the transverse segment \(x=0\):
\[
                    u(0,v)=h_0>0,\qquad u_x(0,v)=0 .                    \tag{5}
\]
At its origin \(B=15h_0/4\), \(A=1\), \(W^2=1\). The right-hand side of (4) is analytic near the prescribed jet and depends only on \(x,v,u,u_x,u_v,u_{xv},u_{vv}\). Each second derivative on the right has fewer than two longitudinal derivatives. Thus (4) has the noncharacteristic Cauchy–Kowalevski normal form with **\(x\) as the evolution variable**. The analytic Cauchy theorem gives a unique real analytic \(u\) in a neighborhood of \((0,0)\). Shrink to an open rectangle \(|x|<b,\ |v|<c\) with \(b<.02,\ c<\epsilon_y,\ B>0,\ W^2>0,\ u>0\). This is an actual local solution of the nonlinear equation, rather than an inference from finite coefficients. For \(v>0\), \(z=v^{5/2}u\) satisfies (2) everywhere on that rectangle. Its derivatives through order two tend to zero on \(v=0\); \(z_{vvv}(0,v)\) is unbounded as \(v\downarrow0\) by (5).

At \(v=0\) write \(h(x)=u(x,0)\). Then (4) recovers \(3hh''-5(h')^2=16d_5\kappa_*\), precisely the three-row leading condition of R747. Unlike the leading condition by itself, (4) pays all the higher nonlinear orders throughout an open set.

## 3. Recover both planar coordinates and the exact trace jets

Set \(\bar g=g-dz\otimes dz\) for \(v\ge0\). It is positive definite since \(W^2=1-|\nabla_g z|^2>0\). Its entries
\[
 \bar g_{xx}=A^2-v^5u_x^2,\quad \bar g_{xv}=-v^4u_x T_0,\quad
 \bar g_{vv}=1-v^3T_0^2
\]
extend analytically to the full small rectangle. For completeness, consider the graph of \(z\) in the Riemannian product with two-dimensional base metric \(\bar g\) and vertical metric \(dt^2\), for \(v>0\). Its induced metric is \(g\), its unit normal has vertical component \(W>0\), and its second form is \(\operatorname{Hess}_g z/W\). The last identity follows by taking the vertical component of the product connection's Gauss formula. The horizontal area ratio of its tangent plane is \(W\), whence the ambient sectional curvature of that tangent plane is \(W^2 K_{\bar g}\). The Gauss equation gives
\[
 K_g=W^2 K_{\bar g}+\frac{\det\operatorname{Hess}_g z}{W^2\det(g)}.
\]
Equation (2) now forces \(K_{\bar g}=0\). Analyticity and nondegeneracy let this identity extend through \(v=0\), after shrinking if needed.

The simply connected smaller rectangle admits an analytic planar development \((X,Y)\) of \(\bar g\). For instance parallel transport an orthonormal coframe from the origin with the flat Levi-Civita connection; torsion freeness makes both parallel one-forms closed, and their integrals give the two coordinates. Fix the planar rigid freedom by \((X,Y)(0,0)=(0,0)\) and its differential equal to the identity there. At \(v=0\) all first derivatives of \(\bar g\) vanish, so the full connection vanishes along that edge. The exact equation \(\partial_{ij}(X,Y)=\bar\Gamma^k_{ij}\partial_k(X,Y)\) then gives on the entire edge
\[
 (X,Y)(x,0)=(x,0),\qquad (X,Y)_v(x,0)=(0,1),\qquad D^2(X,Y)(x,0)=0 .
\]
Consequently \((X,Y,z)\) has metric \(g\) and matches the **whole two-jet** of \((x,v,0)\) along \(v=0\). Using \((x,v,0)\) for \(v<0\) gives a \(C^2\) local isometric embedding across the seam: its differential at the origin has rank two and its planar component is locally injective. The right-sided third derivative of the normal component excludes \(C^3\). This explicitly accommodates the known higher-order mismatch between the target and a shifted straight boundary.

For each \(\theta\in[1,\pi/2]\) let \(p_{\sigma,\theta}\) be the source cylinder point at \((s_*+r\theta,\sigma)\). Embed the positive-side local coordinates by
\[
 B_\theta\left[p_{\sigma,\theta}+X T+Y\,\sigma e_y+z n\right]
\]
and use the actual cylinder below. Here \(B_\theta\) acts as the R746 affine rotation on the whole point. Only a rigid frame and origin change with phase. The same \(b,c\) and the same isometric functions work on both sides and throughout this whole finite phase interval.

## 4. A closed-field splice and its precise scope

This local exact patch can be inserted in a continuously moving closed R747 reference, while keeping a uniform global tube and the cap volume witness. This is an existence statement with a small selectable width. Work on the upper or lower rolled end, in a smaller compact longitudinal subinterval of \((-b,b)\), and restrict support in phase to \(\theta>1\), with the phase cutoff equal to 1 for \(\theta\in[1.1,\pi/2]\). Use a longitudinal cutoff supported in \((-b,b)\) and equal to one on a smaller nonempty interval. For \(0<v<\delta\ll c\) multiply the difference between the local exact embedding and the R747 reference in the pre-rotation frame by these cutoffs and a smooth radial cutoff equal to one on \(v\le\delta/3\), zero on \(v\ge2\delta/3\). Add it to the actual R747 field and rotate; leave the original cylinder and caps unchanged.

The resulting global difference tends to zero in \(C^2\), uniformly in phase. Indeed the analytic planar development has the same two-jet along \(v=0\) as the reference planar coordinates, which are analytic here. The nonanalytic height is \(v^{5/2}u\). The difference and its first two transverse derivatives are \(O(v^{5/2}),O(v^{3/2}),O(v^{1/2})\). The corresponding mixed estimates follow by differentiating the analytic coefficients on the compact longitudinal interval. The radial cutoff derivatives cost \(O(\delta^{-1}),O(\delta^{-2})\), leaving a \(C^2\) change \(O(\delta^{1/2})\). The reference angle inversion in R747 is analytic on this actual open constant/straight segment by its nonzero derivative. Named height terms and the seam chart are smooth from the positive side.

R746 has uniform support \(>.107\), absolute principal curvatures \(<1/.107\), and a compact \(C^2\)-continuous family of embedded closed spheres. For sufficiently small \(\delta>0\), the new fields remain embeddings by \(C^1\) openness uniformly on the compact phase set, retain support \(>.106\) and absolute principal curvatures \(<1/.106\) about the transported centers. [R723-A](R723-directional-normal-flow-support-reach.md) again gives whole-image reach at least \(.106\) for every phase. The target initial diameter stays \(D<3.40\), the grip stays pointwise fixed with diameter \(\ge1.40\), and the held distance exceeds \(1.520\) by the R746 witness and uniform small positional change. The endpoint volume difference stays positive: the R746 gap from its two cap graphs is strictly positive, and signed enclosed volume is continuous under \(C^1\) perturbations of these closed embeddings. Thus \(\delta_{\rm E}>0\) still holds, without new marks. On the smaller strip where all cutoffs are one, its induced metric equals the specified \(g\) **exactly** for every \(\theta\in[1.1,\pi/2]\). The splice and the remaining end region retain explicit unpaid metric costs. This does not give a specified width, a solution through the cap, or a closed same-metric family.

## 5. Reproducible finite CK coefficients of the actual target

The [public-run exact coefficient generator](../scripts/resume_20261126/r749_fractional_darboux_coefficients.py) uses rational arithmetic throughout. In the actual constant-curvature material band, multiply (4) by \(B\) and write the residual as
\[
 {\cal R}=B[u_{xx}+(AA_v/v)T_0]-D_0^2-CW^2 .
\]
For \(u(0,v)=h_0,\ u_x(0,v)=0\), \(B(0,v)=15h_0/4\) exactly. If the rows of the \(x\)-expansion are known through \(x^{i+1}\), set the next temporarily to zero and compute the whole current \(x^i\) residual. The unique \(x^{i+2}\) row is the negative of that row divided by \((15h_0/4)(i+2)(i+1)\). The factors \(v u_v,\ v^2 u_{vv},\ v u_{xv}\) preserve the radial truncation order. The actual \(A,A_v/v,C\) are generated with the extra degrees required before dividing by radial powers. The source recomputes the original nonlinear residual in every requested coefficient box and compares the overlapping coefficients at each refinement. It records entire coefficient-array identities and the full residual support in the runner's reproducible raw, with a complete lightweight report on main. Those finite algebraic checks do not provide a numerical lower bound on an analytic convergence radius.

The fixed public parameters are \(h_0=1,64\) in separate branches and \((\deg_x,\deg_v)=(4,8),(8,12),(12,16)\). The geometry, transverse ramp, spatial phase interval and initial metric are held fixed at all orders. No finite return is quoted here before its public execution.
