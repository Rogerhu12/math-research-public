# R740 — A finite bent disk, two explicit closed shoulder fields and whole-image displacement

2026-11-28. These two finite reference fields use the same bent Euclidean unit disk and a horizontal reflecting plane. Each complete phase is a closed embedded sphere. A fixed material disk of diameter at least .60 has radius-.08 tangent balls against the whole image in both orders. The half-turn moves a point at least .564 from the entire other image, and the diameter is less than 2.60. Three fixed marks give positive Euclidean-quotient distance. Each end contains a positive-width exact rotational-metric cylinder on a **noncircular** planar geodesic. The middle shoulder has an explicitly angle-dependent Gram matrix. These are whole starting fields for a same-metric solve. They do not establish a closed isometric path. The tilted-mirror problem is separate.

The complete integral generator is [r740_rolled_disk_seed.py](../scripts/resume_20261126/r740_rolled_disk_seed.py). Use the argument `design="ellipse"` for the corrected terminal ring or `design="rolled"` for the first roll. In both cases the grip marks can be omitted separately. All estimates below are analytic inequalities for the indicated exact integrals.

## Disk and fixed parameters

Use Cartesian material coordinates \(x^2+y^2\le1\), with \(h=.30,b=.26,e=1/8,H=.17\). Set \(S_5(v)=10v^3-15v^4+6v^5\), \(S(v)=35v^4-84v^5+70v^6-20v^7\) on \([0,1]\), continued by their endpoint values. Put \(\kappa_m=\pi/[2b(1-e)]\). From \(x=h\) to \(h+b\), the derivative \(\beta'\) rises from zero to \(\kappa_m\) by \(S_5\) over length \(be\), stays constant for \(b(1-2e)\), then uses its reflected ramp. Elsewhere \(\beta'=0\). With \(\beta(h)=0\), the final angle is exactly \(\pi/2\). Write
\[
 u(x)=h+\int_h^x\cos\beta,\qquad v(x)=\int_h^x\sin\beta,\qquad
 P(x,y)=(u(x),y,H+v(x)).
\]
Thus \(P^*I=dx^2+dy^2\). Let \(q=\int_h^{h+b}\sin\beta=\int_h^{h+b}\cos\beta\) by reflection of the turning law. Since \(1\le\sin\beta+\cos\beta\le\sqrt2\), \(b/2\le q\le b/\sqrt2<.184\). For \(x\ge h+b\), \(u=h+q,\ v=x-h-b+q\). This is a true vertical planar tongue. The embedded sheet is regular even where its horizontal projection collapses.

Let \(r=.09,\ \epsilon=.001\). On segment A of length \(r\pi/2+\epsilon\), raise curvature from 0 to \(1/r\) by \(S_5\) over length \(\epsilon\), hold it for \(r\pi/2-\epsilon\), and drop it to 0 by the reflected ramp. Integrating gives an angle \(\alpha\) from 0 to \(\pi/2\). Take \(R'= \cos\alpha,\ t'=\sin\alpha,\ R(0)=1,\ t(0)=0\). Write \(R_b,t_b\) for their endpoint values. The nonnegative remainder in \(ds=r\,d\alpha+(1-r\alpha')ds\) has mass \(\epsilon\), hence
\[
 1.09\le R_b\le1.091,\qquad .09\le t_b\le.091 .
\]
For \(x=R\cos\theta,\ y=R\sin\theta\) the first shoulder is
\[
 A(s,\theta)=(u(x)+t\sin\beta(x),\;y,\;H+v(x)-t\cos\beta(x)).                 \tag{1}
\]
At the disk rim \(R'=1,t'=R''=t''=0\). Equation (1) consequently matches \(P,P_\rho,P_{\rho\rho}\) and their appropriate angular and mixed jets. At its other end \(A_s=(\sin\beta,0,-\cos\beta)\), \(A_{ss}=0\). In subsequent segments \(x=R_b\cos\theta,\ y=R_b\sin\theta\) and \(\beta=\beta(x)\).

## Two complete closures

**First roll.** During a second parameter interval \(s\in[0,\eta]\), \(\eta=.01\), put \(f=1-S(s/\eta)\) and integrate, from the true last value of A,
\[
 B_s=(1-r\beta f')(\sin(\beta f),0,-\cos(\beta f)).
\]
The speed is positive, and the curvature of each such individual plane curve is at most \(1/r\). The horizontal increment is \(r(\cos(\beta f)-\cos\beta)+\int_0^s\sin(\beta f)\,ds\), and the height drop is \(r(\sin\beta-\sin(\beta f))+\int_0^s\cos(\beta f)\,ds\). Its endpoint has downward unit tangent and zero acceleration. Because \(H-\eta-\sqrt{t_b^2+r^2}>.02\), the terminal height \(Z(\theta)\) exceeds .02. Over a further interval \(0\le d\le c=.01\), retain the endpoint horizontal point and use height \(Z-d-(Z-2c)S(d/c)\). This decreases to \(c\) with downward unit speed and zero acceleration at both ends. Append a straight vertical strip of width \(c\) down to \(z=0\).

The first roll has a serious transverse curvature defect, notwithstanding its meridional curvature bound. Its terminal ring is \((a(x),R_b\sin\theta)\) where
\[
 a=u+t_b\sin\beta+r(1-\cos\beta)+\eta\int_0^1\sin(\beta(1-S(v)))\,dv.
\]
Here \(a'=\cos\beta+kJ\) with \(k=\beta'\) and \(J=t_b\cos\beta+r\sin\beta+\eta\int f\cos(\beta f)\,dv\). At \(x_*=h+b(1-e/2)=.54375\), \(k=\kappa_m/2<3.46\), \(k'=-(15/8)\kappa_m/(be)<-397\). The remaining angle is at most \(be\,\kappa_m/4<.057\). Hence \(\cos\beta<.057,\sin\beta>.998,\ .0898<J<.106,\ a'<.424\). Also \(J_\beta\le r\cos\beta<.0052\), giving \(a''=-k\sin\beta+k'J+k^2J_\beta<-35.5\). The absolute planar curvature is
\[
 \frac{|a'-x(1-x^2/R_b^2)a''|}
 {R_b[(1-x^2/R_b^2)a'^2+x^2/R_b^2]^{3/2}}>40
\]
at this point, using \(x_*/R_b<1/2\). This curvature is a principal curvature of the actual open vertical strip. The first closed reference therefore has reach at most \(1/40\), while \(D\ge2\). Bounding the normal section curves alone would miss this failure.

**Replacement by a prescribed ellipse.** Replace everything after (1). Let \(l=z_e=.025,\ j=1.01,\ c_0=.12\). Define \(X_0=u+t_b\sin\beta,\ Z_0=H+v-t_b\cos\beta,\ X_e=jx+c_0\). Take a parameter \(p\in[0,1]\) over physical material length \(l\). Put \(D_0(p)=\int_0^p(1-S(v))dv,\ E_0=p-D_0,\ G=D_0-S/2\). The new shoulder is
\[
 \begin{split}
 X&=(1-S)X_0+S X_e+lG\sin\beta,\quad Y=y,\\
 Z&=(1-S)Z_0+S z_e+l[S/2-E_0-G\cos\beta].
 \end{split}                                                                  \tag{2}
\]
It matches the incoming position, velocity and acceleration and ends at \((X_e,y,z_e)\) with velocity \(-e_z\) and zero acceleration, with derivatives taken in \(lp\). The other second derivatives match by differentiating the identities in \(\theta\). Indeed \(X=X_0+lD_0\sin\beta+[X_e-X_0-(l/2)\sin\beta]S\). The square-bracket coefficient is positive, since for \(x\le h\) it is \(c_0+.01x>0\), and for \(x>h\) use \(u\le x\) and \(t_b+l/2\le.1035<c_0\). Height can be written \(Z=Z_0-lD_0\cos\beta-lE_0-[Z_0-z_e-l(1+\cos\beta)/2]S\). Its square-bracket coefficient is positive by \(Z_0\ge H-t_b\). Consequently \(X\) increases and \(Z\) strictly decreases in the open parameter interval. The cross-angle orientation is controlled by
\[
 G=p(1-p)^4(1+4p+10p^2+(5/2)p^3)\ge0,\quad
 X_x=(1-S)(1+t_b k)\cos\beta+Sj+lGk\cos\beta .
\]
In particular \(X_x>0\) in the open interval. Follow this curve by a vertical strip down from \(z_e\) to zero.

For either design use the original ring parameter \(\theta\) at the top of the vertical transition. Its eventual strictly increasing arclength inverse is the lift \(\psi\) defined by
\(\int_0^{\psi(\theta)}|\Gamma'|=(|\Gamma|/2\pi)\theta\).
The ring speed is positive, including the two points \(\cos\theta=0\), where the original \(x\)-derivative is one for the roll or \(j\) for the ellipse. In the old height-flattening segment replace \(\theta\) by \(\theta+S(d/c)(\psi(\theta)-\theta)\) in both horizontal point and height. For (2) apply the same angular change over the first half of its straight strip. These are diffeomorphisms of each angular circle and have vanishing derivatives of the weight at both ends. The old transition is also a change of chart on its vertical wall. The final positive-width open strip in both designs has *exact material metric*
\[
 ds^2+(|\Gamma|/2\pi)^2d\theta^2 .
\]
Its end is a planar noncircular geodesic. The ellipse has curvature bounded by \(j/R_b\): with semiaxes \(jR_b,R_b\) its curvature is \(j/[R_b(j^2\sin^2\theta+\cos^2\theta)^{3/2}]\). Its infinite product cylinder has two-sided tangent balls of radius \(R_b/j\). This follows either from the integral convex-curve argument below, using shorter tangent-turning arcs of size at most \(\pi\), or directly from the ellipse parametrization. It applies in particular to all ordered pairs within the terminal product cylinder. It does not settle pairs with the middle shoulder.

Reflect the upper half about \(z=0\). The positive-width product strip makes this a regular seam. All unmarked reference functions are at least \(C^3\) as surface charts. For example \(S\) has its first three derivatives zero at each end, so the second segment's speed joins through its second derivative. Both end caps are made of copies of the actual compact disk, with the common seam at the equator rather than a repeated pole.

## Embedding and whole-image held distance

On A, fix \(y\). For \(x>0\), \(x=(R^2-y^2)^{1/2}\); the right projected abscissa increases by
\[
 (1+t k)\cos\beta\, R R'/x+t'\sin\beta .
\]
The left branch has \(\beta=0\) and moves left. Thus successive projected rings of A are nested in the strict interior of the segment, including where the original disk has a vertical part. At \(x=0\) the planar \((R,\theta)\) map on the inactive circle is regular. More generally A is a regular surface: in coordinates \((x,y,t)\) the ambient map in (1) has orthogonal columns of lengths \(1+t k,1,1\), hence is locally invertible. The disk is embedded by the monotone planar bending coordinate and its preserved \(y\); equality on its vertical tongue requires equal height as well.

For the old B, the right branch moves farther to the right if \(\beta>0\), with strictly decreasing height in the interior; on \(\beta=0\) it is vertical. The following straight walls continue downward from that endpoint. The two branches at a fixed \(y\) cannot meet: for positive \(x>h\) they are separated by the sign of \(X\), and for \(|x|\le h\) they are opposite points of a circular section with identical heights. Endpoint equality under angular changes is just the indicated common meridian. For the ellipse B, contact with A or the disk is excluded on \(x>h\) by the outermost right abscissa, and on \(x\le h\) by strict descent below \(H-t_b\), the lower height bound for all preceding points. The two points at fixed \(y\) for \(0<x\le h\) follow identical strictly decreasing height functions; at the same height their abscissas differ by \(2x[(1-S)+Sj]\). For \(x>h\) the negative branch always has \(X\le-h+c_0<0\), and the active branch \(X\ge h\). Regularity holds for \(\cos\theta\ne0\) by its nonzero angular \(y\)-derivative and nonzero meridian tangent. At \(\cos\theta=0\), \(Z_\theta=0,\ X_\theta\ne0,\ Z_s<0\). The straight strip lies below all its preceding segment. All open upper-half points have positive height and the reflected lower ones negative. These facts prove embedding, also after any equatorial rotation.

Use the phase \(F_t(\rho,\theta)=\mathcal R_t F(\rho,\theta-t)\) away from the added stationary marks; \(\mathcal R_t\) is rotation about the vertical axis. The upper disk \(\rho\le h\) is pointwise fixed and has diameter at least \(2h=.60\). Give it three circular graph marks of radii \(.010,.012,.014\), with centers respectively \((-.10,-.08),(.06,-.08),(0,.09)\). In material Cartesian coordinates add height \(10^{-4}d_i^2(1-|p-p_i|^2/d_i^2)_+^3\), independent of \(t\). These small graphs are \(C^2\); the points on their rims stay fixed. Neither disk cropping nor rim jets are altered. The metric throughout this marked disk is also phase-independent.

Take the actual upper point \(p=P(.995,0)\) in the first phase. It has \(p_x=h+q\ge.43,\ p_z-H=.435+q\ge.565\). In the half-turn, an upper comparison point with its original abscissa \(x>h\) has rotated abscissa at most \(-h\) on both closures. Every upper point with \(x\le h\) has height at most \(H\), apart from the tiny fixed marks of height \(<.001\). This partition persists through the angular reparametrization. Every lower point has nonpositive height. Therefore \(\operatorname{dist}(p,S_\pi)\ge.564\) against the **entire** closed comparison image. Strong displacement is already present at a specified material point.

Here are diameter bounds at all phases. On the disk, A and the old B/wall let \(R\le1.091\), and let the positive horizontal addition to \(u(x)\) be at most \(J_0=t_b+r+\eta\le.191\); \(|z|\le H+v(x)\) for the upper and reflected points. In the unbent sector the old additions vanish. In the bend \(h\le x\le h+b\), the squared norm is at most \(R_b^2+2(h+b)J_0+J_0^2+(H+q)^2<1.58\). On the vertical tongue it is at most
\[
 R_b^2+(h+q+J_0)^2+(H-h-b+q)^2+2x(H-h-b+q)<1.58 .
\]
For the last inequality use \(q\le .184,\ h+b=.56\) and the negative slope \(H-h-b+q\); alternatively maximize the original increasing expression in \(q\) first and then take \(x=.56\). The inactive sector has norm squared at most \(R_b^2+H^2\). Hence these parts fit inside radius 1.26. On (2), the straight convex combination of the endpoints has norm bounded by the larger endpoint norm; the other endpoint has norm at most \(\sqrt{(jR_b+c_0)^2+z_e^2}<1.23\). The residual in \(X\) has absolute value at most \(l/2\), since \(0\le G\le1/2\). The residual in \(Z\) has magnitude at most \(l\) from \(D_0+E_0=p\) and \(0\le S(1+\cos\beta)/2\le1\). Its vector length is \(<.028\). The tiny fixed marks lie well inside the same ball. Thus \(D<2.60,\ .564>.2D,\ .60>.2D\) for both designs.

Away from the three mark rims the embedded image is \(C^3\). At each rim the normal third derivative of the graph across the circle has a nonzero jump while the graph plane there is regular. These three disjoint circles are exactly its non-\(C^3\) locus. A Euclidean congruence must fix each distinct-radius circle, then their three noncollinear centers. It is the identity or reflection in their common plane \(z=H\). The latter cannot map one image onto the other: before the marks the height extrema are \(\pm Z_\mathrm{max}\), the marks lie strictly between those extrema, and \(H>0\). The identity is excluded by the witness. Compactness of the orthogonal group and bounded translations of any approximating congruences now give positive quotient Hausdorff separation.

## Normal balls actually covered; specific metric defect

For the bare disk \(P\), all ordered pairs obey both tangent-ball inequalities at \(d=1/\kappa_m\). Write \(C=(u,v)\), \(n=(-\sin\beta,\cos\beta)\). Convex turning gives \((C(q)-C(p))\cdot n(p)\ge0\); the opposite normal ball is immediate. For the other center, if \(p<q\),
\[
 (C(p)+d n(p)-C(q))\cdot n(q)
 =d\cos(\beta_q-\beta_p)+\int_p^q\sin(\beta_q-\beta(t))dt\ge d .
\]
Use \(dt\ge d\,d\beta(t)\) against a nonnegative integrand. For the reversed order integrate \(\sin(\beta(t)-\beta_q)\) on \([q,p]\). Adding the free \(y\) difference only increases squared distance. This is a whole-curved-disk test, including the vertical tongue.

With marks, every ordered top-disk pair still passes radius .08. For two points in the flat sector the plane graph extends to all of \(\mathbb R^2\) with Hessian norm \(\le30\cdot10^{-4}\), so Taylor's theorem bounds twice the normal chord by this constant times the squared horizontal separation. Each mark is separated horizontally by \(>.16\) from every point \(x>h\); the remaining pairs use the bare proof. Opposite disks have separation at least \(2H\).

Moreover **every point of the upper grip** \(\rho\le h\) has radius-.08 normal balls with *all points of the closed image, in either order*. Other than top-disk pairs it suffices to prove distance at least .16. A lower point has \(z\le0\). A shoulder point in the flat or bending sector before the ellipse interpolation has large \(|y|\) whenever \(|x|\le h+b\) (on A/B, \(|y|\ge\sqrt{1-.56^2}\)); for \(x<-.56\) its abscissa is at most \(-.56\) before the interpolation. For old B in the right plateau \(X\ge h+q+t_b\ge.52\). On right-plateau A, either \(|y|\ge.5\), or \(x>\sqrt{1-.5^2}\) gives \(z-H=x-h-b+q>.43\). Its old final wall keeps the large plateau \(X\). For the ellipse segment and its terminal wall, if \(|y|\ge.5\) the horizontal gap suffices. Otherwise \(|x|=\sqrt{R_b^2-y^2}>.96\). Its positive branch starts at \(X_0\ge.52\) and increases; its negative branch has \(X\le-.96+.12<-.8\). Angular reparametrization preserves these whole-image statements. Marks can add less than .001 to the grip height in the vertical comparison. Separations of at least \(2d\) prove the claimed two normal inequalities by Cauchy–Schwarz irrespective of the other point's normal. Since \(.08>.03D\), no pair touching this grip can cause a violation of the requested normalized thickness. Full closed-surface reach of the replacement still requires the other ordered pairs; its compact \(C^2\) embedding ensures some positive reach, without fixing its ratio.

In the orthogonal coordinates of (1) the exact ambient metric is \((1+t k)^2 dx^2+dy^2+dt^2\). Put \(E=(1+t k)^2-1\). On A its induced coefficients are
\[
 g_{ss}=1+E\cos^2\alpha\cos^2\theta,\quad
 g_{s\theta}=-E R\cos\alpha\cos\theta\sin\theta,\quad
 g_{\theta\theta}=R^2(1+E\sin^2\theta).
\]
At an interior \(s\) the inactive sector has \(E=0\) whereas the true bend has \(E>0\). These exact coefficients identify the middle defect on a finite open set. The stationary marked disk, full unmarked remainder of the Euclidean disk, and the final normalized product strip have phase-independent metrics; matching two-jets at their boundaries does not make the intervening metric radial. The whole-field initial data and the ellipse's corrected terminal geometry are available without fitting a selected meridian. No nonlinear fixed-metric solution, full .03D thickness, or mesh-refinement result for such a solution is claimed here.
