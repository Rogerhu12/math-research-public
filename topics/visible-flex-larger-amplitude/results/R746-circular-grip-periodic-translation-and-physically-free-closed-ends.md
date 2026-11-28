# R746 — A circular grip, exact axial translation on the whole periodic cylinder, and physically moving closed ends

2026-11-28. The explicit phase runs from \(0\) to \(\pi/2\). Its connected closed embedded surfaces have a pointwise stationary open cylindrical grip of diameter at least \(1.40\), whole-image held distance at least \(1.521\), diameter \(D<3.41\), and reach at least \(.107\) at **every** phase. The endpoint enclosed volumes differ, so the Euclidean-quotient distance is positive without any surface markers. The entire periodic central cylinder has exactly the same metric throughout. Both rolled annuli and both filling disks actually change shape; their whole metrics have yet to be matched. In particular this is a geometric and action starting field for the larger-amplitude problem.

The [complete physical two-jet](../scripts/resume_20261126/r746_axial_translation_closed_two_jets.py) imports the [R744 section and atlas](R744-closed-extruded-bent-disk-global-reach-and-curvature-gap.md). The analytical estimates apply to the defining integrals, independently of the quadrature for evaluating them. No solver return is asserted.

## 1. The circular orbit in the true section

Use the original, unmarked, undeformed R744 closed sphere, with planar profile arclength \(s\bmod P\), physical transverse direction \(e_y\), and planar \(xz\)-coordinates \(\Gamma(s)\). In the convention \(T'=-\kappa n,\ n'=\kappa T\), the upper right clockwise half-turn has \(r=.15,\ \epsilon=.001\). Its initial point is \((u_*,z_*)\) and its initial arclength is \(s_1\). The curvature ramps of length \(\epsilon\) flank a genuinely circular subarc. The turn-angle bounds of that subarc are \(\epsilon/(2r)\) and \(\pi-\epsilon/(2r)\). On it
\[
 s=s_1+\epsilon/2+r\alpha,\qquad
 O=\Gamma(s)-r n(s),\qquad \Gamma(s)=O+r(-\cos\alpha,\sin\alpha).
\]
Thus \(O\) is exactly constant there. By the nonnegative remainder measure of R744 §1, its distance to the comparison center \((u_*+r,z_*)\) is at most \(\epsilon\). Since \(u_*=.30+q,\ z_*=.17+.44+q,\ .13\le q<.184\), we have \(O_x\ge.579,\ O_z\ge.739\).

Let \(B_\theta\) rotate \(xz\) counterclockwise by \(\theta\) about \(O\), fixing the direction \(e_y\). This specifies the sense of rotation independently of the conventions for three-dimensional positive rotations. On the whole cylinder set
\[
 F_\theta(s,y)=B_\theta(\Gamma(s+r\theta),y),\qquad |y|\le1 .
\]
In this formula and below \(B_\theta\) acts only on the two planar physical coordinates. The induced cylinder metric is precisely \(ds^2+dy^2\). In particular the required material velocity there is the constant translation \(r\partial_s\), which is single valued on the periodic flat cylinder.

Choose \(H\) to be the closed material rectangle \(.10\le\alpha\le1.05,\ |y|\le.70\) on the true circular subarc. For all \(\theta\in[0,\pi/2]\), the shifted angle \(\alpha+\theta\) stays strictly within the constant-curvature subarc. In this convention \(B_\theta\) changes \((-\cos(\alpha+\theta),\sin(\alpha+\theta))\) to \((-\cos\alpha,\sin\alpha)\). Every point of \(H\) is stationary. Its interior is open in the surface and its diameter is at least the separation \(1.40\) between its two transverse edges.

## 2. Actual free geometry on the two annuli and caps

Use R744 §2 with \(v\in[0,L],\ L=.108\pi/2+.0005\), turn angle \(\eta\), height increment \(p'=\cos\eta\), inward offset \(d'=\sin\eta\), and terminal values \(d_b,p_b\in[.108,.1085]\). The lower bound follows by integrating the circular component \(.108\,d\eta\). Write
\[
 Q(s,v)=\Gamma(s)-d(v)n(s),\quad m(s,v)=1-d(v)\kappa(s),\quad
 w=p(v)/p_b,\quad b(v)=[4w(1-w)]^4,\quad G(Q)=1+.20Q_x+.10Q_z.
\]
The unrotated geometry of end \(\sigma=\pm1\) is
\[
 E_\theta^\sigma(s,v)=
 (Q(s,v),\,\sigma[1+p(v)+\lambda_\sigma\sin\theta\,b(v)G(Q(s,v))]).
 \tag{1}
\]
Here and below parentheses of this kind indicate planar \(xz\) followed by the physical \(y\). Use \(\lambda_+=10^{-6},\lambda_-=2\cdot10^{-6}\). The whole open annulus changes its physical height, including arbitrarily close to both seams. The full material map on the end is
\[
 B_\theta E_\theta^\sigma(s+r\theta\chi(v),v),\qquad
 \chi(v)=1-S_7(v/L),\qquad S_7(t)=35t^4-84t^5+70t^6-20t^7.
 \tag{2}
\]
For each \(v\) this is a translation of the full \(s\)-circle. Its first three transverse derivatives at each end agree with the corresponding constant shift. Source and rotated images consequently share the R744 overlapping seam charts.

The projected region of each cap is the complete R744 star disk inside \(\Gamma_{d_b}\). Change its actual graph height to
\[
 y=\sigma[1+p_b+a_\sigma\sin\theta\,h(x,z)],\qquad
 h(x,z)=b_c^2[1-(x^2+z^2)/b_c^2]_+^4,\qquad
 b_c=.04,\quad (a_+,a_-)=(.75,.50).
 \tag{3}
\]
Use the unchanged planar material coordinate here, then apply \(B_\theta\). To check the support of (3), the original planar open section contains the origin and its boundary stays at distance at least .17 from it. Indeed the main arcs have \(|z|\ge.17\), the left turns and walls lie to the left of \(-1\), and the right turns and walls have \(x\ge u_*\ge.43\). The origin is inside by the two wall crossings at \(z=0\). In the embedded inward-offset homotopy every boundary moves at most .1085, hence the closed \(.04\)-disk and a neighborhood remain inside the terminal ring. Both modes in (3) are physical bends of their initially flat caps. No singular polar chart is needed there.

In particular the new problem does not freeze a particular raw end and ask only for its tangential Killing field. The code accepts a three-component physical displacement evaluated as a two-jet in the ambient pre-rotation frame, shared by all charts. This also permits moving the seam and cap rim. A correction supported away from the swept grip leaves its pointwise condition intact. General corrections require their own metric, embedding and reach estimates.

## 3. All ordered pairs and all phases

R744 supplies support at least .110 about \(c=(.595,0,0)\), absolute principal curvatures at most \(1/.108\), and a closed embedded reference before (1) and (3). First apply (1) in space as a transverse coordinate change. In the slab \(1<\sigma y<1+p_b\), put \(w=(\sigma y-1)/p_b\) in its formula, add \(\sigma\lambda_\sigma\sin\theta\,[4w(1-w)]^4G(x,z)e_y\), and extend by zero across both faces. On the bounded region occupied by the reference, \(|G|\le1.4,\ |\nabla G|<.224\). For \(b=[4w(1-w)]^4\) one has \(|b|\le1,\ |b_w|\le16,\ |b_{ww}|\le224\). The displacement \(D_1\), its Euclidean differential and its second differential there satisfy
\[
 |D_1|<.000003,\qquad \|D D_1\|<.00042,\qquad \|D^2D_1\|<.055 .
\]
For example the second bound on derivatives of order two uses \(2\cdot10^{-6}(1.4\cdot224/.108^2+2\cdot.224\cdot16/.108)\). Both slab maps preserve planar coordinates and are strictly increasing in \(y\); they are injective on the solid.

For a coordinate change \(\Phi=I+D_1\) with differential error \(\epsilon_1\), the transformed unit normal differs from the old by at most \(2\epsilon_1/(1-\epsilon_1)\). This follows by applying \(D\Phi^{-T}\) to the old unit normal and normalizing. Before rotation every point has \(|F-c|<2.30\), by the coordinate bounds in R744 §5. The new support is therefore greater than \(.110-.000003-2.30(2\cdot.00042/(1-.00042))>.107\). Along a reference unit-speed surface geodesic the normal acceleration after transformation is at most \((1+\epsilon_1)/.108+.055\); its transformed speed is at least \(1-\epsilon_1\). Taking all tangent directions proves the absolute principal curvature bound
\[
 [(1+.00042)/.108+.055]/(1-.00042)^2 < 1/.107 .
\]

On the planar caps (3) has gradient at most \(8a_\sigma b_c\le.24\) and Hessian norm at most \(8a_\sigma\le6\). For the radial second derivative the factor after \(8a_\sigma\) is \((1-q)^2(7q-1)\), \(q=(x^2+z^2)/b_c^2\in[0,1]\); its absolute value is at most 1, as is the tangential factor \((1-q)^3\). The graph curvatures are bounded by this Hessian norm. Its support on the bump is at least \((1+p_b-(.595+.04)\cdot.24)/\sqrt{1+.24^2}>.90\).

For completeness the planar offsets in R744 are strictly nested, not just separately simple. At fixed polar ray \(e\) from \(c_2=(.595,0)\), their polar radius satisfies \(\rho'(d)=-1/(e\cdot n)<0\), by differentiating \(\Gamma(s)-dn(s)=c_2+\rho e\) and taking its scalar product with \(n\). The denominator is positive by R744 (1) and \(d\le.1085\). Every projected end outside the flat cap footprint is therefore a single height graph on each side. Formula (1) keeps this property and (3) adds separate graphs inside the terminal disk, away from the annuli. This proves global embedding and identifies the bounded solid. The seam jets in §2 give at least \(C^2\) regularity and \(C^2\) continuous dependence on \(\theta\). Rigid rotation transports the support center to \(B_\theta c\). Applying the full-sphere theorem [R723-A](R723-directional-normal-flow-support-reach.md) proves
\[
 \operatorname{reach}(F_\theta(M))\ \ge\ .107\qquad (0\le\theta\le\pi/2).
\]
This controls both sides of the surface and every point pair.

## 4. Held displacement, diameter, and noncongruence without marks

The phase-dependent physical deformations before rotation have size at most \(.0012\); the supports of (1) and (3) are disjoint. R744 gives unrotated diameter \(<3.40\), hence every phase has diameter \(<3.403<3.41\). The topic normalization is \(D=\operatorname{diam}F_0(M)<3.40\). Every original profile point has \(z<.945\): on the upper right half-turn use \(z_*+.15+.001<.945\), the simpler endpoint bounds elsewhere. Nested offsets and the filled caps project into the closed original planar section, and (1),(3) do not change \(z\). At \(\theta=\pi/2\) the spatial \(x\)-coordinate of every point is \(O_x+O_z-z>.373\). A point on the old left wall at transverse \(y=0\) has \(x_L\le-1.149\). Thus its distance to the **entire** final image exceeds \(1.521\). In particular \(\delta_{\rm hold}/D> .446,\ {\rm diam}(F_0(H))/D>.410,\ \operatorname{reach}/D>.0313\).

In the unrotated frame each of the two end graphs increases the outward height at every interior projected point with \(b>0\) because \(G>0\). The two cap graphs increase it on their supports. The closed solids at the initial and final phases are nested there, with volume difference at least the contribution of the two cap graphs,
\[
 \Delta V\ \ge\ (a_++a_-)\int_{x^2+z^2<b_c^2}h(x,z)\,dx\,dz
 =\frac{\pi}{5}(a_++a_-)b_c^4>0 .
\]
Volume is invariant under \(B_\theta\) and arbitrary Euclidean congruence. The compact endpoint images therefore have positive optimized Euclidean Hausdorff distance: any rigid sequence giving distances tending to zero has bounded translations, hence has a convergent congruent subsequence. The inverse endpoint rotation gives \(\delta_{\rm E}\le .0012\) for this pair. This proof of positivity uses moving physical ends and requires no small recognition marks. The size of the volume difference alone is not a metric defect criterion.

## 5. What the fixed metric still costs

At phase zero on an end \(g_{ss}=m^2,\ g_{sv}=0,\ g_{vv}=1\). Put \(D(s,v)=\lambda_\sigma b(v)G(Q(s,v))\). The exact first variations of the physical pullback (2) are
\[
 \dot g_{ss}=r\chi\,\partial_s(m^2),\qquad
 \dot g_{sv}=r\chi' m^2+\cos\eta\,D_s,\qquad
 \dot g_{vv}=2\cos\eta\,D_v.
 \tag{4}
\]
The dot denotes differentiation in the spatial angle \(\theta\) at zero. These follow from the Lie derivative along \(r\chi\partial_s\) and the derivative of the actual added transverse height. On the whole cylinder all three are identically zero. On the initially planar caps the first variation is also zero, but the exact finite metric change is \(\sin^2\theta\,a_\sigma^2 dh\otimes dh\). For example on the positive cap at \(x=b_c/2,\ z=0\), the \(xx\) increment at \(\pi/2\) is \([4(.75)b_c(3/4)^3]^2>10^{-3}\). The named whole field thus fails the \(10^{-6}\) metric requirement. Equation (4) also shows the actual angular row which the transverse-only named correction cannot cancel. The optional three physical components permit changes in that row. Neither endpoint volume variation nor the periodic cylinder supplies or rules out a successful all-phase end solution.

The source covers the cylinder, the two rolled ends, and polar, rim-normal and Cartesian coordinates on each cap (nine chart names in total). The source returns \(F,F_u,F_v,F_{uu},F_{uv},F_{vv}\), including the chain rule through the material shift and the physical changes. A fresh solve can retain the fixed action on the central cylinder and the same end material domain, and use the complete two-dimensional end shape as an unknown. No refined same-metric family, mesh deliverables, or certified end continuation is claimed here.
