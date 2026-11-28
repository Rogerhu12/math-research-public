# R753. A spatial rectifying cylinder and independent, regularly ruled, movable caps on the delayed-turn metric

Use the entire R752 material sphere, with phase-zero curve \(q=\Gamma\), full transverse coordinates \(|y|\le .37\), and both delayed rolled shoulders. We give three pieces which are **exactly isometric for arbitrary admissible values of their controls**: a generally nonplanar middle cylinder and both full caps. They are joined into genuine \(C^2\) trial immersions by an explicit formula on the two remaining annuli. This changes physically the boundary curves on both sides of each annulus. [Closed physical two-jet generator](../scripts/resume_20261126/r753_rectifying_cylinder_and_cap_fans.py).

## 1. A closed spatial curve with unchanged arclength and open true grip

In the unrotated physical frame first define an isometric development of the *whole plane* containing \(\Gamma\). For \(X_L=-1.125,\ X_R=-1.045,\ w=.08\), set
\[
 \beta(x)=a\,\sin^8\!\left(\pi(x-X_L)/w\right)\quad(X_L<x<X_R),\qquad
 \beta=0\text{ elsewhere},
\]
where \(a=a(\phi)\) vanishes at zero. Set
\[
 (U,V)(x)=(x,0)+\int_{X_R}^x(\cos\beta-1,\sin\beta)(\xi)\,d\xi,\qquad
 \gamma(s)=(U(q_x(s)),V(q_x(s)),q_z(s)).
\]
Since \((U',V')\) has length one, \(\gamma\) is an actual periodic unit-speed curve, without an endpoint-closure residual. To the right of the window the development is exactly the identity; to its left only a constant translation is applied. The window meets the original profile solely on two positive constant-curvature arcs with \(k=1/.15\). Indeed the left quarter-turn has \(x=-1-\int_0^\sigma\cos\alpha\,ds\); its initial ramp has horizontal displacement \(\le .001\) and its terminal ramp lies within \(.002\) of the left vertical wall at \(x<-1.149\). The right pieces and main arc have \(x\ge-1\). Reflection preserves the active interval. This avoids Frenet divisions at the flat walls, inflections, and all joins of the original planar construction.

In the active arcs put \(T=\gamma',\ K=|\gamma''|,\ B=(T\times\gamma'')/K,\ \eta=\det(T,\gamma'',\gamma''')/K^3=\tau/K\). Off the window use \(B=e_y,\ \eta=0\). At the window ends this agrees to the required orders because \(\beta\) and its first seven derivatives vanish there and the original binormal for the positive oriented arc is \(e_y\). On the remainder, including regions where \(\gamma''\) vanishes or reverses sign, these are prescribed fields, using no Frenet quotient. They give
\[
 (B+\eta T)'=\eta' T
\]
everywhere, by the Frenet equations on the window and direct differentiation off it.

For the largest argument needed on the closed body, \(|y|\le1.2885\). The profile lift \(s=\sigma+y\eta(\sigma)\) has degree one and a unique orientation-preserving periodic inverse if \(1-|y|\|\eta'\|_\infty>0\). Define
\[
 C(s,y)=\gamma(\sigma)+y[B(\sigma)+\eta(\sigma)T(\sigma)] .
\]
Exactly
\[
 C_s=T,\quad C_y=B,\quad
 (C_{ss},C_{sy},C_{yy})
 ={ \gamma''(\sigma)\over1+y\eta'(\sigma)}(1,-\eta,\eta^2).
\]
In particular \(C^*e=ds^2+dy^2\) on the entire rectangle modulo \(s\sim s+P\). In the central piece use \(C(s+.15\phi,y)\) and then the R746 spatial rotation. On the circular grip sector and its whole swept range \(\beta=\eta=0\) and the development was anchored to the identity on the right. Exactly the old cancellation fixes the full open grip.

Here are usable sufficient bounds. Put \(b_j=|a|(8\pi/.08)^j,\ 0\le j\le3\), by expanding \(\sin^8\) into exponentials whose absolute coefficient sum is one. On the active arc write \(P=(\cos\beta,\sin\beta,0)\), \(Q=(-\sin\beta,\cos\beta,0)\). Then \(\gamma'=x'P+z'e_z,\ \gamma''=x''P+\beta'x'^2Q+z''e_z\), hence \(K^2=k^2+(\beta' x'^2)^2\). With
\[
 B_1=b_2+3kb_1+b_1^2,\quad
 B_2=b_3+6kb_2+8k^2b_1+b_1^3+3b_1b_2+6kb_1^2
\]
one has
\[
 |\eta|\le B_1/k^2,\quad
 |\eta'|\le B_2/k^2+3|\eta|\, b_1(b_2+2kb_1)/k^2. \tag{1}
\]
Indeed \(\gamma'''+k^2T\) has length \(\le B_1\) and \(\gamma''''+k^2\gamma''\) length \(\le B_2\) by differentiating in \(P,Q,e_z\), using \(x'''=-k^2x'\) and the corresponding fourth derivative. Differentiate the determinant expression for \(\eta\) (the first two differentiated columns contribute zero) and \(K^2=k^2+(\beta' x'^2)^2\). For \(|a|\le2^{-21}\), using \(8\pi/.08<315,\ k=20/3\), (1) gives \(|\eta|<.0012,\ |\eta'|<.40\). Thus the whole lift is admissible even at the outside of both new shoulders. For the named \(|a|\le2^{-38}\) the bounds improve to \(|\eta|<10^{-8},\ |\eta'|<3.2\,10^{-6}\). A nonzero pulse changes the plane of the actual upper/lower center curve, while the right open sector remains unchanged: at points of the left turn with \(x'\ne0\) the \(y\)-coordinate varies, yet a right upper open arc forces the only candidate containing plane to be the original \(xz\) plane. The new cylinder therefore offers a spatial freedom in addition to reparametrization.

## 2. A regular fan of generators covers each whole planar cap

Place a pole at \((3,0)\) in the material \(xz\) plane. The bounded planar end domain lies in \(|(x,z)|<1.17\); hence its polar description \(x=3-R\cos u,\ z=R\sin u\) has \(R>1.83,\ |u|<.6\) and no apex. Independently on either cap choose
\[
 W(u)=A u_+^3+B\sin u+C\sin2u,\quad
 q'(u)={\sqrt{1-W'(u)^2}\over\cos W(u)},\quad q(0)=0,\qquad
 b=(-\cos q\cos W,\sin W,\sin q\cos W).
\]
Take \(|W'|<1,\ |W|<\pi/2\) on this range. Then \(|b|=|b'|=1,\ b\cdot b'=0\). The map \((R,u)\mapsto (3,y_b,0)+R b(u)\), where \(y_b=\pm(.37+p_b)\), has exactly \(dR^2+R^2du^2=dx^2+dz^2\) everywhere. It remains exactly isometric after an arbitrary independent rigid rotation and translation about the cap center. The implementation takes all three latitude coefficients and six pose coordinates independently at positive and negative ends, with phase factors vanishing at zero. The cap code evaluates the smooth fixed material charts, including the usual regular interior Cartesian coordinates. This is a two-dimensional physical deformation on the full disk with varying ruling directions.

With \(A\ne0\), the cap has a non-\(C^3\) line inside it at \(u=0\). At zero \(W=0,\ b=-e_x,\ b'=(0,W',\sqrt{1-W'^2})\). The one-sided jump in \(b'''\) projected on \(b\times b'\) is \(6A/\sqrt{1-W'^2}\), by the formula for \(q'\). Since \(R>0\) and the two-jet is regular, this is also a jump of the third normal derivative as an embedded graph. At phase zero the complete R752 initial image is \(C^3\). For any resulting embedded full family with positive-cap \(A\ne0\) at the last phase the endpoint rigid-quotient distance is positive, by compactness of the relevant Euclidean motions. The two-jet/\(C^2\)-continuity does not require third derivatives across this germ.

## 3. Physical joins, width and the genuine remaining problem

Write \(v\) for R752 outward roll arclength, \(w=S_7(v/L)\), \(y=\pm(.37+p(v))\). In the legacy chart take \(S=s+.15\phi(1-w)\). Let \(Q=q(S)-d(v)n(S)\), \(\Delta_C=C(S,y)-(q(S),y)\) and \(\Delta_\pm(Q)\) be the displacement of the chosen posed fan from its original planar cap at \(Q\). In the common \(x,y,z\) frame an actual joined roll is
\[
 (Q,y)+(1-w)\Delta_C+w\Delta_\pm(Q)+V_\pm(s,v,\phi).
\]
Here \(V_\pm\) are independent three-component roll corrections whose first two transverse jets vanish at both seams, and which vanish everywhere initially. Their tangential and mixed jets at the seams vanish by differentiating the boundary identities. Alternative gauges use
\[
 \Omega(S,d)=\Omega(s,d)+\phi(.15-d) g(v),\qquad \Omega(s,d)=s-d\Theta(s)
\]
with \(g(0)=1,\ g(L)=0\) and its first two derivatives zero at both ends. One option gives a nearly constant phase loss per unit arclength via 8% smooth end ramps of its derivative. Every option has the same phase-zero metric and the same two material seam jets. At the center seam \(d'=0,p'=1,d''=p''=0\). At the cap seam \(d'=1,p'=d''=p''=0\). These, the actual roll and fan compositions, and the flat endpoint jets of \(w,g\) give the genuine two-jets across all four seams. At zero all corrections vanish, and the entire initial body is exactly R752. The **whole closed-distance compatibility** on the prescribed central cylinder in fact persists for all \(|a|\le2^{-21}\), by the following additional argument on the new physical curve. For a shallow excursion the R752 spherical comparison gives the shorter material profile arclength. The two shifted points on \(s\mapsto C(s+h,\pm.37)\) are joined on this new spatial curve by a path of exactly that length, since \(|C_s|=1\). At the bounding circles let \(E_0=\sup|C(s,\pm .37)-(q(s),\pm .37)|\). Since \(|\sigma-s|\le .37|\eta|,\ |\gamma''|\le k+b_1\) on the active arcs and \(|B-e_y|\le b_0+b_1/k\), Taylor cancellation of \(y\eta T\) gives
\[
 E_0\le .08|a|+.37(b_0+b_1/k)+\tfrac12(k+b_1)(.37\, .0012)^2<10^{-5}.
\]
Outside the window there is only the integrated constant translation or zero. The deep-path lower bound remains \(\sqrt{d_0^2+4(.789)^2}\) in the unchanged initial closed metric. For all \(0\le d_0\le2.34,\ 0\le h\le .15\pi/2\) this strictly exceeds \(d_0+2h+2\cdot10^{-5}\) (the difference is smallest at the two upper endpoints). The latter bounds the two new spatial endpoints by the triangle inequality. Concatenating excursions as in R752, with the local exact central isometry just proved, gives the closed-distance inequality for every pair of central points over all these amplitudes and phases. It gives no corresponding automatic cap-pose compatibility.

For clarity the named \(|a|\le2^{-38}\), \(|A|+|B|+|C|\le2^{-26}\), poses zero, \(V_\pm=0\), lies in the strict whole-image reach/held margin. Here are details. Use the actual image coordinates \(S,v\) on the rolls, whose underlying unperturbed metric is \(m^2dS^2+dv^2,\ m=1-dk>.27\). On the reference profile \( |k|\le7,\ |k'|<13000\) by the two actual smooth curvature ramps (R744). The physical tangent perturbation \(E=C(S,y)-(q(S),y)\) satisfies
\[
 |E|<3\,10^{-10},\quad |E_S|<10^{-7},\quad |E_y|<3\,10^{-10},
 \quad |E_{SS}|<4\,10^{-5},\ |E_{Sy}|<8\,10^{-8},\ |E_{yy}|<10^{-15}.
\]
Use (1), \(|S-\sigma|\le1.289\,10^{-8}\), \(|B-e_y|\le b_0+2b_1/k\), with the sharper \(|B-e_y|\le b_0+b_1/k\) from the angle \(\arctan(|\beta' x'^2|/k)\), and the cancellation \(\gamma(\sigma)+y\eta T(\sigma)-\gamma(S)=O(k|y\eta|^2)\). For \(E_{SS}\) compare \(\gamma''/(1+y\eta')\) with \(q''(S)\); nearby points on any active interval remain in the same constant-\(k\) arc. Off it \(E\) is either zero or a constant translation. For the fan displacement \(D_\pm\), \(|D_\pm|<10^{-7},\ |D D_\pm|<10^{-7},\ |D^2D_\pm|<10^{-7}\) in planar Euclidean coordinates. Indeed \(|W|<2^{-26}, |W'|<2.1\,2^{-26}, |W''|<4\,2^{-26}\), \(|q'-1|<4\,10^{-15}, |q''|<10^{-14}\). The polar affine radial map has orthonormal Hessian only in its angular-angular slot, equal to \((b''+b)/R\), and \(R\in(1.83,4.17)\). These bounds follow directly by differentiating the displayed trigonometric formula for \(b\).

For the roll perturbation \(U=(1-w)E+wD_\pm(Q)\) these bounds give
\[
 |U|<1.1\,10^{-7},\quad |U_S|<3\,10^{-7},\quad |U_v|<5\,10^{-7},
 \quad |U_{SS}|<.00021,\ |U_{Sv}|<.000005,\ |U_{vv}|<.000006 .
\]
Here \(|Q_S|\le1.77,\ |Q_{SS}|\le .1093(13000)+1.77(7)<1440,\ |Q_v|\le1,\ |Q_{Sv}|\le7,\ |Q_{vv}|,|p''|\le1/.108\), and \(|w'|<2.3,\ |w''|<28\). In the orthonormal frame \((m^{-1}\partial_S,\partial_v)\) the covariant Hessian entries of \(U\) are
\[
 (U_{SS}-m_SU_S/m+mm_vU_v)/m^2,\quad
 (U_{Sv}-m_vU_S/m)/m,\quad U_{vv}.
\]
With \(|m_S|<1422,\ |m_v|<7\) the operator norm is \(<.026\), and the differential norm is \(<2\,10^{-6}\). The same bounds hold on the central cylinder and caps by the simpler formulas there. Along an old intrinsic unit-speed geodesic the change of the ambient acceleration is \(\nabla^2 U(\dot c,\dot c)\); thus the new maximum normal curvature is at most \((1/.108+.026)/(1-2\,10^{-6})^2<9.29\). On any oriented orthonormal tangent basis the change of the cross product is at most \(4.1\,10^{-6}\); normalizing changes the normal by \(<9\,10^{-6}\). The old support \(.110\) about \(c=(.595,0,0)\), with \(|F_0-c|<2.4\), therefore leaves support \(>.1099\) through the full linear homotopy of these displacements. Radial projection about \(c\) has nonsingular derivative throughout and degree one, hence is bijective on each closed sphere. These are global embeddings. R723-A yields all-phase reach at least .107, while \(D<3.49,\ \mathrm{diam}(H)\ge.72\). The R752 all-image held witness loses at most \(1.1\,10^{-7}\) in support-coordinate position, still giving held \(>1.521\); undoing the rigid rotation gives \(\delta_E\le1.1\,10^{-7}\) for the named field. Its strict positivity uses the actual upper-cap germ above.

These certified small amplitudes do not certify the geometry of arbitrary larger optimization controls. The fixed target is the new phase-zero tensor, the mobile center and both caps pay all three tensor components identically, and the remaining full two-dimensional isometry equations are located on the two rolls. In particular, genuine extension through every angle, and mesh/refinement verification of a solution, are still required.
