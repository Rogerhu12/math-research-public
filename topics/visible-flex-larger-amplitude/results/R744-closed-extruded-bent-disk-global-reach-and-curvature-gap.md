# R744 — A closed thick reference for the bent disk, with an explicit curvature-changing family

2026-11-28. We construct a finite closed reference with **all-phase global reach at least .108**, \(D<3.40\), \(\delta_{\rm hold}\ge.719\), grip diameter \(>.689\), and \(\delta_{\rm E}>0\). Every ordered point pair of each actual phase is covered by the reach proof, including both caps. Upper and lower complete unit material disks use the genuine strong bend of R740. We also give finite nonzero deformations of the central cylinder with intrinsic curvature on its previously flat centerline and the *same* whole-image bounds. The phase family is isometric on both complete disks and off the two angular-transition annuli. The metric on those annuli is not fixed; the construction is a geometrically feasible starting field, not a solution of the same-metric problem.

The [complete two-jet source](../scripts/resume_20261126/r744_extruded_closed_two_jets.py) gives six physical derivatives on overlapping charts and the actual phase motion. The geometric bounds below are for the integral formulas themselves. They are independent of the quadrature used to evaluate the formulas.

## 1. The genuine strong disk in a periodic planar section

In physical \(xz\)-coordinates write \(C(x)=(u(x),H+v(x))\) for the exact R740 planar arc, \(-1\le x\le1,\ H=.17\). It is parametrized by arclength: \(C'=(\cos\beta,\sin\beta)\), \(0\le\beta\le\pi/2,\ 0\le\beta'<6.91\). It is horizontal for \(x\le h=.30\), vertical after \(h+b=.56\), and \(b=.26\). Let \(q=\int_h^{h+b}\cos\beta=\int_h^{h+b}\sin\beta\). Then \(.13\le q\le b/\sqrt2<.184\). In particular
\[
 C(1)=(u_*,z_*),\qquad u_*=h+q,\quad z_*=H+.44+q .
\]

In all planar turns below set \(r_0=.15,\ \epsilon=.001\). For a turn through angle \(a\) let its arclength be \(r_0 a+\epsilon\). Raise its curvature from 0 to \(1/r_0\) with \(S_5(t)=10t^3-15t^4+6t^5\) over the first \(\epsilon\), hold it at \(1/r_0\) over length \(r_0 a-\epsilon\), then lower it by the reflected ramp over \(\epsilon\). Its angle \(\alpha\) starts at 0 and integrates to \(a\). The nonnegative measure \(ds-r_0d\alpha\) has total mass \(\epsilon\). Throughout every such turn its position differs from the corresponding exact circular arc position at its current angle by a vector of length at most \(\epsilon\).

From \(C(1)\) add a clockwise half-turn with tangent \((\sin\alpha,\cos\alpha)\), starting vertically upward and ending vertically downward. Its center for the preceding circular comparison is \(O_R=(u_*+r_0,z_*)\); the outward normal is \(n=(-\cos\alpha,\sin\alpha)\). Follow its endpoint straight down to \(z=0\) at fixed \(x_R\). At \(C(-1)=(-1,H)\) instead extend outward with tangent \((-\cos\alpha,-\sin\alpha)\) over a quarter-turn to downward vertical. Its comparison center is \(O_L=(-1,H-r_0)\); its outward normal is \((-\sin\alpha,\cos\alpha)\). The final height is in \([H-r_0-\epsilon,H-r_0]\), hence positive; follow its endpoint down to the plane at \(x_L\). Reflect these pieces and the main arc across \(z=0\) to make the lower half. This gives a regular periodic \(C^3\) planar curve \(\Gamma\); in fact the turns join more smoothly than needed.

Let \(s\) increase from the left-wall equator upward, along the left turn in reverse, along \(C(x)\) with \(x\) increasing, then downward over the right wall, and finally along the reflected reversed lower half. Denote \(T=\Gamma'\), \(n=(-T_z,T_x)\), and use the convention \(n'=kT,\ T'=-kn\). On the original bent disk \(k=-\beta'\). On the added turns \(0\le k\le1/.15\); the straight walls have \(k=0\). The right and left walls have distinct abscissas \(x_R\ge .729,\ x_L\le -1.149\). The upper curve has \(z>0\) except at the wall endpoints: the half-turn stays above \(z_*-.001\) and the left turn stays above \(H-r_0-\epsilon\). The main arc is embedded (vertical portion included); the right turn lies strictly to the right of \(u_*\) in its interior, the left turn strictly to the left of \(-1\). Distinct open walls extend below their turn endpoints at their outermost abscissas. This directly proves the section is simple and encloses \(c_2=(.595,0)\): the horizontal line \(z=0\) meets it only at the two transverse wall points.

The entire oriented section satisfies
\[
 \sigma(s)=(\Gamma(s)-c_2)\cdot n(s)\ge .110 .                              \tag{1}
\]
On the main arc the expression is \((.595-u)\sin\beta+(H+v)\cos\beta\), at least .111 on the bend/tongue and \(H\) on the flat part. On the right turn it is at least \(r_0-|u_*+r_0-.595|-\epsilon\ge.110\), because \(z_*\sin\alpha\ge0\). On the left turn the two components of \((O_L-c_2)\cdot n\) are nonnegative, so the bound is \(r_0-\epsilon\). End walls have support at least \(\min(x_R-.595,.595-x_L)>.13\). Reflection preserves (1).

## 2. The extrusion and its two closed ends

Start with \((\Gamma(s)_x,y,\Gamma(s)_z)\), \(-1\le y\le1\). At each end put \(r_y=.108,\ \epsilon_y=.0005\). Use the same smooth curvature rule with this radius and ramp length over \(0\le v\le L_y=r_y\pi/2+\epsilon_y<.171\); denote its increasing angle from zero to \(\pi/2\) by \(\alpha\). Integrate \(p'=\cos\alpha,\ t'=\sin\alpha,\ p(0)=t(0)=0\). On the two end annuli the planar \(xz\)-coordinate and the physical \(y\) are
\[
 Q=\Gamma(s)-t(v)n(s),\qquad y=\pm(1+p(v)).                                \tag{2}
\]
At their endpoints let \(t_b,p_b\) denote the terminal offsets. From the same nonnegative remainder measure,
\[
 0\le t(v)\le r_y(1-\cos\alpha)+\epsilon_y,\quad
 t_b,p_b\le .1085,\qquad t(v)\le L_y\sin\alpha(v).                         \tag{3}
\]
The last bound uses monotonicity of \(\alpha\) on the *whole* segment and hence remains valid at arbitrarily small angles.

Every inward offset \(\Gamma_t=\Gamma-tn\), including the last, is simple. Its tangent is \((1-tk)T\) with \(1-tk\ge1-.1085/.15>0\). By (1) its outward support about the same \(c_2\) is at least \(.110-t>.001\). Its polar-angle derivative around \(c_2\) never vanishes: its sign is the constant orientation sign, and its magnitude is \((1-tk)(\sigma-t)/|\Gamma_t-c_2|^2\). The homotopy from \(t=0\) never meets \(c_2\), so its winding number has absolute value one. Thus polar angle is a bijective coordinate on the entire offset. This proves global simplicity, rather than inferring it from the local nonvanishing of \(1-tk\). The same argument works for \(t\le t_b+.0005\).

Fill each terminal ring in the plane \(y=\pm(1+p_b)\) by its complete closed star disk about \(c_2\). A useful parametrization is \(Q=c_2+\lambda(\Gamma_{t_b}(s)-c_2)\), \(0\le\lambda\le1\), with the usual Cartesian plane chart at its polar origin. Near the seam use \(Q=\Gamma(s)-(t_b+w)n(s)\) on a short inward planar collar. Equation (2) reaches it with \(t'=1,\ p'=0,\ t''=p''=0\); the curvature ramp makes the third derivatives agree as well. At the extrusion end it begins with \(t'=0,p'=1\) and zero acceleration. These regular charts give a closed \(C^3\) sphere. Its embedding also follows directly from the strict increase of \(p\) before its endpoint, opposite sides in \(y\), simple individual offsets, and the two filled flat end disks.

## 3. All ordered pairs by support and both principal curvatures

At a point of (2) the outward normal has planar component \(n\cos\alpha\) and \(y\)-component \(\pm\sin\alpha\). About \(c=(.595,0,0)\) the support is exactly
\[
 (\sigma-t)\cos\alpha+(1+p)\sin\alpha
 \ge .110\cos\alpha+(1-L_y)\sin\alpha\ge .110.                             \tag{4}
\]
This includes the small-angle interval, where simply subtracting \(t_b\) would discard the margin. On the central extrusion the support is (1), and on the flat caps it is \(1+p_b\).

The annular coordinates are orthogonal with speeds \(1-tk\) and 1; the mixed second form vanishes. The absolute principal curvatures are
\[
 \left|\frac{k\cos\alpha}{1-tk}\right|,\qquad |\alpha'|.
\]
For \(k<0\) the first is at most 6.91. For \(k>0\), use (3) to bound it by
\(\cos\alpha/[r_0-r_y(1-\cos\alpha)-\epsilon_y]\le 1/(r_0-\epsilon_y)\), since \(r_0>r_y+\epsilon_y\). The turn curvature is at most \(1/.108\); the same bound holds on the extrusion and caps. Apply [R723-A](R723-directional-normal-flow-support-reach.md) to the entire closed sphere with \(A=I\). Equations (1) and (4) and the common curvature bound yield
\[
                         \operatorname{reach}(F(M))\ge .108 .                \tag{5}
\]
In particular this is not a minimum of unrelated patchwise reach bounds.

## 4. Genuine change of intrinsic geometry inside the same strict bounds

There is an explicit finite set of actual nonflat starting surfaces, and even an interval of amplitudes. On the central cylinder put
\[
 F_f(s,y)=(\Gamma(s)+f(s,y)n(s),\,y)
\]
in planar-plus-transverse notation. In the upper right turning arc take the constant-curvature subarc from angle \(\pi/3\) to \(2\pi/3\) of length \(w=.15\pi/3\). If \(s_0\) is its start, set
\[
 f=\varepsilon \sin^4\!\big(\pi(s-s_0)/w\big)\,y^2(1-4y^2)_+^4
 \quad(s_0\le s\le s_0+w),\qquad |\varepsilon|\le .0004 ,
\]
and set \(f=0\) elsewhere except for the reflected identical lower turn. On the subarc \(k=1/.15\) and \(k'=0\). This change is supported in \(|y|\le.5\) away from the material disks and both end annuli. The joins remain \(C^3\). The full two-jet routine also accepts external physical \(f,f_s,f_y,f_{ss},f_{sy},f_{yy}\) for a supported free correction; the bounds here are for the stated mode amplitude interval.

For the sine factor \(a\), \(|a'|\le4\pi/w=80,\ |a''|\le16\pi^2/w^2=6400\). For \(b=y^2(1-4y^2)_+^4\), \(|b|\le1/4,\ |b'|\le5,\ |b''|\le90\), by two differentiations on its support. Therefore \(|f|\le.0001,\ |f_s|\le.008,\ |f_y|\le.002\) and \(\|D^2 f\|_{\rm op}\le.81\) (the larger absolute row sum is at most \(.64+.16\)). In the frame \(T,n,e_y\),
\[
 \begin{split}
 F_s&=(1+kf)T+f_sn,\quad F_y=e_y+f_y n,\\
 F_{ss}&=2kf_sT+[f_{ss}-k(1+kf)]n,\quad
 F_{sy}=kf_yT+f_{sy}n,\quad F_{yy}=f_{yy}n .
 \end{split}
\]
The metric has least eigenvalue at least \((1-|kf|)^2>.998\). Before normalization its outward normal is \(n-f_sT/(1+kf)-f_y e_y\); the unit normal changes by less than .009. The scalar second form has operator norm at most \(|k|(1+|kf|)+.81+.009(2|kf_s|+2|kf_y|)<7.50\); after the metric factor the absolute principal curvatures are \(<7.6\). On this subarc \(\sigma\ge .110+z_*\sin(\pi/3)>.70\). The support loss is less than .02, because \(|F-c|<2\) there and the positional change is at most .0001. Thus all of (5) survives, including for nonzero amplitudes. Along \(y=0\) the centerline position, first form and tangent plane are unchanged, while the *physical intrinsic Gaussian curvature* is \(-2k\varepsilon a(s)\). This perturbation changes geometry, not just coordinates.

## 5. An explicit phase action, grip, diameter and whole-image witness

Use in each top and bottom disk the original material chart \((x,y_m)\). It extends past its four tangencies with the rectangle: extend \(x\) as signed arclength of \(\Gamma\) onto the two turns and set \(y_m=\pm(1+v)\) immediately beyond \(|y_m|=1\) on (2). Thus the material disks of radius 1.01 fit inside two disjoint charts, with seam derivatives given by the preceding formulas. For phase \(t\in[0,2\pi]\), rotate the material coordinates by angle \(-t\chi(\rho)\), \(\rho=\sqrt{x^2+y_m^2}\). Here \(\chi=1\) for \(\rho\le1\), \(\chi=0\) for \(\rho\ge1.01\), and in between \(\chi=1-S_7((\rho-1)/.01)\). It is a smooth-enough diffeomorphism for each \(t\) with inverse given by changing sign (the radius is preserved). Use the identity outside the two charts, evaluate the actual closed surface, then spatially rotate by \(t\) about the vertical axis. Time can be rescaled to \([0,1]\). The unmarked image is exactly that spatial rotation; both \(\rho\le h\) subdisks are pointwise stationary. The twist need not return the *material labels* to themselves when \(t=2\pi\).

Add the three fixed disjoint R740 marks to the upper grip, at the same centers and with the same radii and heights \(10^{-4}d_i^2(1-|p-p_i|^2/d_i^2)_+^3\). Their Hessian bound is .003, their gradient has norm \(<10^{-5}\), and their supports lie in \(\rho<.13\). For each phase use center \(c_t=\mathcal R_t c\). The flat upper support is \(H\); on the marked subgraph its loss is \(<.00001\) by the gradient bound and \(\rho+.595<.73\). Its absolute principal curvatures are at most .003. The unmarked estimates rotate rigidly, including any of the supported curvature changes of §4. R723 consequently proves (5) for **every marked phase**.

For the diameter bound, every point of \(\Gamma\) has planar norm \(<1.17\). On the right turn use \(|O_R|+r_0+\epsilon\), with \(u_*+r_0<.634,\ z_*<.794\), giving \(<1.17\). On the left use \(|(-1,H-r_0)|+r_0+\epsilon\); the main arc and straight walls satisfy the same bound by their endpoint and coordinate bounds. An inward offset moves the planar point by at most .1085, and \(|y|\le1.1085\). Flat-cap points are convex combinations of their terminal ring and \(c_2\). The tiny mark and normal-mode displacements on the central extrusion cost at most .0001 there. Hence all phases have diameter
\[
               D<2\sqrt{(1.17+.1085+.0001)^2+1.1085^2}<3.40 .
\]
Take \(H_{\rm grip}\) to be the union of the upper and lower closed marked-material disks of radius .30. The inherited definition allows disconnected grip regions. Two opposite unchanged rim points on different disks have separation \(\sqrt{.60^2+.34^2}>.689>.2D\).

Choose the center-cylinder point at \(y=0,\ \alpha=\pi/2\) on the upper right half-turn. Its height above the flat upper disk is at least \(v(1)+r_0\ge .44+.13+.15=.72\), because the vertical part of the circular-comparison remainder on the first quarter is nonnegative. Its planar abscissa is at least \(u_*+r_0\ge.58\). It is unchanged by the normal mode since \(y=0\). At the comparison half-turn, the cap annuli and cap interiors all have \(|y|\ge1\). All central-cylinder upper points from the active main arc or right-hand turn/wall came from \(x_{\rm phys}\ge.30-.0001\), hence after rotation their abscissas are negative. The remaining upper central points have height at most \(H+.001\); all lower points have nonpositive height. These facts bound distance from the witness to the **entire half-turned closed image** by at least .719. In particular \(\delta_{\rm hold}\ge.719>.2D\) and \(.108>.03D\).

The only non-\(C^3\) image locus consists of the three distinct-radius circles bounding the three \(C^2\) mark graphs. Any congruence between the two phases fixes the three noncollinear centers and so is either identity or reflection in \(z=H\). The first is excluded by the witness. Before marking, each of these surfaces has height extrema \(\pm Z_\mathrm{max}\) by its actual horizontal symmetry; the marks are strictly inside this height range, so reflection in \(z=H>0\) cannot be the congruence. Compactness gives \(\delta_{\rm E}>0\). Only these small fixed marks break the rigid rotation of the *unmarked* images, so they do not provide a large normalized quotient displacement.

## 6. Why the whole same-metric problem remains

The entire marked upper disk and the entire lower disk have a phase-independent metric, and the same is true on all portions where the material map is the identity. The angle-transition regions are genuine annuli of this finite surface. A phase-dependent material twist there is not an isometry of their metric.

For \(f=0\), the whole central cylinder has the flat metric \(ds^2+dy^2\) with \(s\) periodic of period \(P\). Lifting a Killing vector field to the Euclidean strip gives \((A-\omega y,B+\omega s)\), by the elementary three planar Killing equations. Periodicity forces \(\omega P=0\). The compensating material rotation on the open upper grip has nonzero infinitesimal angular coefficient. Hence an exact global Killing field of this unmodified surface cannot extend that rotation. The mode in §4 makes the centerline loop nonflat, but its support stops at \(|y|=.5\). A complete flat periodic subband, for example \(.55<y<.85\), still exists. It is connected to the open upper grip through an open flat corridor: near the top center the arclength coordinate is far from the right turn, hence a vertical material strip is flat from the grip into that subband. On that connected flat region the same Euclidean Killing coefficients propagate from the grip; periodicity on the subband gives the same contradiction. Thus no exact normalized Killing field exists for any of these particular supported modes either. A further free correction must cut or curve every such homologous flat strip, not just its central loop.

A separate scale discrepancy remains even for that mode: on the symmetry meridian \(y=0\) the left and right arclengths from the material top center to the equatorial wall are respectively \(1+(\pi r_0/2+\epsilon)+z_L\) and \(1+(\pi r_0+\epsilon)+z_R\). Their difference is \(r_0\pi/2+z_R-z_L>.9\), using \(z_R\ge z_*-.001\) and \(z_L\le.02\). These lengths remain unchanged under the mode in §4. A proposal that interchanges these particular reflected meridians and preserves the equatorial boundary must correct this difference. Neither a pure clock change nor the preserved reach and displacement inequalities supply that missing global isometry. Further computations must allow genuine field and metric adjustments on the complement of the two fixed grips.
