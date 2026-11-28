# R783. Four moving cap sectors with the minimum number of fixed rim points

Use the R781 material sphere, its unchanged initial metric \(g_0\), and its original time interval \(0\le t\le\pi/2\). There are exact \(C^2\) developments of the **whole** right disk, fixed on its centered radius-\(.18\) grip, that move its entire boundary except for four material points at every positive phase. Four is optimal for this disk and grip. The bends on the four sectors have independent amplitudes. We extend them by one ambient formula on the entire closed R781 reference so the physical two-jets agree at every material seam.

For the R781 short and balanced reference families (\(0\le\xi\le.06\)) every four-angle choice below yields a closed embedded sphere at every phase with the original grip, held distance \(>.320\), and Euclidean-quotient separation \(>.096-.55b\), where \(b\) is the largest prescribed angle. Two explicit choices have different quantitative conclusions. At angles \((.020,.022,.024,.025)\), we prove radius \(>.0021\) for the whole closed sphere and much larger radii for all right-cap/right-cap normal pairs. At fixed positive angles \((.80,.85,.90,1.00)\,10^{-6}\) the full sphere satisfies \(\operatorname{reach}\ge1/24.46>.03D\) at all phases. Both retain a true circumferential metric deficit \(>.23\) away from the moving cap. These are fixed finite physical designs; their cap angles do not remove that deficit. The complete [physical source](../scripts/resume_20261126/r783_four_developable_cap_flaps.py) uses the R781 chart, angle clocks and quadrature. The estimates below refer to the defining integrals.

## The fixed set of a developed planar disk

Let \(D_a\) be the radius-\(a\) material disk with its Euclidean metric. Let \(I\) include it in a plane, and let a \(C^2\) isometric immersion \(G\) on its closure agree with \(I\) on the centered disk of radius \(h_0>0\). Its full pointwise fixed set \(K=\{p:G(p)=I(p)\}\) is closed and convex. A straight material segment between any two fixed points has length equal to its spatial endpoint distance, so its constant-speed spatial image is the original straight segment.

Every extreme point of \(K\) lies on the outer material circle. Indeed an interior-disk boundary point \(p\) of \(K\) has \(DG(p)=DI\) by continuity from the interior of the convex set. The immersion is not locally affine at \(p\), since the affine map with these data would coincide with \(I\) on a whole neighborhood. The flat-isometry developability theorem then supplies a complete straight material chord through \(p\), reaching the outer circle at both ends, on which \(DG\) is constant. Its constant is \(DI\), so this chord lies in \(K\). Hence \(p\) is not extreme. This use of the theorem is valid for the \(C^2\) immersion on a convex disk; the result also holds in \(W^{2,2}\). See Pakzad, *On the Sobolev space of isometric immersions*, J. Differential Geom. **66** (2004), and Hornung, *Approximating \(W^{2,2}\) isometric immersions*, C. R. Acad. Sci. Paris, Ser. I **346** (2008), sections 2–3. [Pakzad](https://doi.org/10.4310/jdg/1090415029) · [Hornung](https://doi.org/10.1016/j.crma.2008.01.001)

A compact convex set in the plane is the convex hull of its extreme points. Thus \(K=\operatorname{conv}(K\cap\partial D_a)\). If only \(k\) rim points are fixed, they form a polygon containing the centered grip disk. Every successive angular gap is less than \(\pi\). A gap of size \(\Delta\) gives a supporting edge at distance \(a\cos(\Delta/2)\) from the center. The largest gap is at least \(2\pi/k\), so
\[
 h_0\leq a\cos(\pi/k),\qquad
 k\geq\left\lceil\frac{\pi}{\arccos(h_0/a)}\right\rceil .
\]
An infinite fixed subset satisfies the lower bound automatically. The R781 fillet has \(d_b\in(.09,.091]\): writing \(ds=.09\,d\alpha+d\mu\) along the quarter turn leaves positive residual mass on an interval with \(\sin\alpha>0\). Hence \(a=.45-d_b\in[.359,.36)\). For \(h_0=.18\), three points cannot suffice. This argument assumes no angular analyticity.

## Four exact sectors

Set \(h=a/\sqrt 2>.253\). The fixed square in the plane \((X,Z)\) is \(|X|,|Z|\leq h\). If a material point of \(D_a\) lies outside it, precisely one of \(u=X,-X,Z,-Z\) exceeds \(h\). Let \(v\) be the orthogonal coordinate there. For four amplitudes \(0\leq A_j\leq .08\) put \(b=\max A_j\), \(B=b/(.08\cdot.94)\), and define
\[
 \beta_j(u,t)=A_j\sin^2t\,P_c((u-h)/.08),\quad
 d_j(u)=\int_h^u(\cos\beta_j-1)\,d\sigma,\quad
 H_j(u)=\int_h^u\sin\beta_j\,d\sigma .
\]
Here \(P_c\) is the R781 integrated clock with its constant extensions; the integral notation evaluates \(\beta_j\) at \((\sigma,t)\). On the \(j\)th cap sector the physical map in the outward, axial and transverse directions is \((u+d_j,Y_*+H_j,v)\), with \(Y_*=.5+p_b\). Its two derivative vectors are orthonormal. At \(u=h\) the physical position, first and second derivatives agree with the original plane. The four sectors and the fixed part therefore make one \(C^2\) isometric immersion, continuous in time in \(C^2\). Because \(u+d_j\) is strictly increasing, it exceeds \(h\) for \(u>h\), while \(|v|<h\). Their planar projections remain disjoint and the whole cap is embedded. If every \(A_j>0\) and \(t>0\), each open outer boundary arc has \(H_j>0\). The only fixed rim points are the four vertices \((\pm h,\pm h)\). The full fixed set on this cap is the square.

For the ordered normal-ball inequalities, extend each bent profile to its entire material axis with its terminal heading constant. With physical horizontal variable \(U=u+d_j\) its height is a graph \(f_j(U)\) with slope \(\tan\beta_j\) and second derivative \(\beta'_j/\cos^3\beta_j\). Incorporating the reflected coordinate for each opposite sector makes a function of the whole physical \(X\)-axis, and similarly of \(Z\); their opposite-side supports within each axis are disjoint. All four material sectors, including their boundaries, are subsets of the same complete graph \(Y=Y_*+f_X(X)+f_Z(Z)\), with identical tangent planes to this graph. Its Hessian is diagonal with operator norm bounded by \(M_c=B/\cos^3 b\). Taylor's inequality gives
\[
 2|\langle n(p),q-p\rangle|\ \leq\ M_c |q-p|^2
\]
for all pairs in that graph, since the Taylor remainder is at most \(M_c\) times half the squared horizontal difference and the unit normal divides by \(\sqrt{1+|\nabla f|^2}\). This handles pairs from different moving sectors as well as pairs involving the fixed square. At distance \(|\tau|<1/M_c\), the squared distance of any other graph point from \(p+\tau n(p)\) strictly exceeds \(\tau^2\); both signed normal layers therefore have unique feet and cannot meet one another. This concerns all right-cap/right-cap pairs, including the true six-jet normals from the closed surface. For \(b=.025\) the resulting radius exceeds \(3.0\). If \(b=0\) the cap is planar.

## Extension to all nine charts and the original diameter scale

For each of the four outward unit directions \(e_j\) in the \(XZ\) plane write \(u=(X,Z)\cdot e_j\), \(w=Y-Y_*\), and \(G(Y)=S_7((Y-.36)/.165)\) with the standard constant extensions. Define one world map \(\mathcal A_t\) by adding
\[
 G(Y)\sum_j(d_j(u)-w\sin\beta_j)e_j
 \quad\text{in the transverse plane},\qquad
 G(Y)\sum_j(H_j(u)+w(\cos\beta_j-1))
 \quad\text{in the axial direction}.
\]
It is a \(C^2\) function of world coordinates and time; the displayed additions vanish at \(t=0\). Every physical chart is the composition of its full R781 field with this same map. In particular the two roll-to-cap joins use the true material normal coordinate, both poles use Cartesian charts, and the cap-polar and normal transitions are the R781 ones. Composing the matching two-jets by the ordinary chain rule proves the complete seam equalities. Since \(Y_*>.59\), \(G=1\) at and near the entire right cap. The left cap and its exterior roll are unchanged in the R781 short/balanced range: at their rightmost axial station \(Y=.5-S<-.05\) by \(S>.55\). The optional spatial-ring mode in the source supplies its own actual six-jets; the following global estimates use the R781 short/balanced reference, with its previously proved reach and coordinate bounds.

All points of every such reference lie in the convex box \(|X|,|Z|\leq.45,\ Y_{\min}\leq Y\leq Y_*\) for a common finite \(Y_{\min}\). Only \(Y\geq.36\) needs estimates. Here \(|w|\leq.231\), each active distance \(u-h<.197\), and at most one direction per horizontal axis is active. The inequalities \(|d_j|\leq .197 b^2/2\), \(|H_j|\leq.197 b\), \(|\beta_j'|\leq B\), and \(|G'|<13.26\) follow directly. Bound the infinity matrix norm of \(D(\mathcal A_t-\operatorname{id})\) by the maximal absolute row sum. For a transverse row an upper bound is
\[
 b^2/2+.231B + b+13.26(.197 b^2/2+.231b).
\]
For the axial row an upper bound is
\[
 2\{b+.231bB+b^2/2+13.26(.197b+.231 b^2/2)\}.
\]
Both are below \(.65\) for \(b\leq.08\), and below \(.19\) for \(b\leq.025\). This proves injectivity and nonsingularity throughout the box by integration on straight segments. It proves embeddedness of the full sphere and \(C^2\) continuity of the family. The initial world diameter remains \(D<1.362\) from R781. The fixed grip disk has diameter \(.36>.2D\). Every axial addition is nonnegative since \(H_j\geq0,\ w\leq0\), and the original leftmost final cap remains in place relative to its prescribed R781 translation. Thus the R781 witness still gives whole-image \(\delta_{\rm hold}>.320\).

Each horizontal displacement has absolute value below \(.239b\), and the total axial displacement below \(.413b\). The Euclidean displacement is therefore less than \(.55b\) for \(b>0\), with equality zero for \(b=0\). At the final phase the distance of the original R781 image from every rigid copy of its initial image exceeds \(.096\) by its diameter gap. Hausdorff's triangle inequality after any rigid alignment gives the claimed quotient bound. This comparison uses no symmetry of the four amplitudes.

## Full-sphere reach and metric costs

For later use record two uniform bounds on the box in Euclidean norms:
\[
 \|D(\mathcal A_t-\operatorname{id})\|_2\leq40b,\qquad
 \|D^2\mathcal A_t\|_2\leq7000b. \tag{1}
\]
In the second inequality the norm is the supremum of the Euclidean length of a bilinear output over unit input vectors. To see the constants, for each scalar summand write its ungated displacement as \(T(u)+wU(u)\). The choices are \((T,U)=(d_j,-\sin\beta_j)\) and \((H_j,\cos\beta_j-1)\). The clock has \(|\beta_j'|<14b\), \(|\beta_j''|<5300b\), since the quintic ramp of its speed has maximum derivative \(1.875\) and physical rounding fraction \(.06\). Hence
\[
 |T|\leq .197b,\ |T'|\leq b,\ |T''|\leq14b,\quad
 |U|\leq b,\ |U'|\leq14b,\ |U''|\leq5302b .
\]
For the last bound the sine second derivative has its extra term at most \(196b^3\); for cosine one can use \(5300b^2+196b^2\). Now \(|G'|<14,\ |G''|<1000\), using the bounds \(140/64\) and \(420/16\) on the first and second unscaled septic derivatives. Each unweighted \(T+wU\) has value at most \(.428b\) and \(u\)-derivative at most \(4.234b\). Each gated displacement has \(uu,uY,YY\) second derivatives of magnitudes below \(1240b,74b,456b\), respectively. The axial component can sum two terms; its \(YY\) sum is below \(912b\) and its mixed horizontal derivative is zero. Thus every scalar second partial is below \(1240b\), giving the Euclidean bilinear bound \(3\sqrt3(1240)b<7000b\). The first derivative bounds in a transverse coordinate and in \(Y\) are \(4.234b\) and \(7b\) for one summand. Summing the two possible axial summands gives row norm below \(23b\), hence Euclidean operator norm below \(23\sqrt3 b<40b\). The zero-angle case follows directly.

Suppose a compact embedded reference \(S\) has reach at least \(r_0\), an ambient \(C^2\) map \(A\) is injective and regular there, \(|A(q)-A(p)|\geq m|q-p|\), \(\|DA\|_2\leq M\), and \(\|D^2 A\|_2\leq J\) on a convex neighborhood containing the chords. For a unit normal \(n'\) at \(A(p)\), \(DA_p^\mathsf T n'\) is parallel to the original normal and has norm at most \(M\). Taylor's formula and the two original empty normal balls give
\[
 \frac{2|\langle n',A(q)-A(p)\rangle|}{|A(q)-A(p)|^2}
 \leq\frac{M/r_0+J}{m^2}\quad(q\ne p).
\]
Every point at a distance below the reciprocal has a closest point by compactness and its closest chord is normal. The strict empty-ball inequality makes the closest foot unique. This proves a uniform reach bound on every pair, including pairs with different chart labels.

R781 provides \(1/r_0=24.45\) for all short/balanced references and all phases. With the fixed SMALL_TUBE_ANGLES in the source (all four are positive and \(b=10^{-6}\)), (1) gives \(m\geq1-.00004,\ M\leq1+.00004,\ J\leq.007\). Thus the right side above is below \(24.46\), and \(24.46(.03)(1.362)<1\). With the MILD_ANGLES, \(\|D(A-\operatorname{id})\|_2\leq\sqrt3(.19)<.33\), \(J\leq175\); the same argument gives reach greater than \(.67^2/(1.33\cdot24.45+175)>.0021\). This estimate does not settle the target whole-sphere reach at the larger four amplitudes. Across the full allowed box \(b\leq.08\), the infinity-norm estimate gives \(m\geq.35/\sqrt3,\ M\leq1.65\sqrt3,\ J\leq560\), hence a strictly positive whole-sphere tube for every allowed choice. The stronger right-cap pair bound is independent of these ambient estimates.

Finally, the selected R781 \(g_0\) is unchanged. The deformed right cap has exactly its original metric. For the tiny four amplitudes, the additional pullback error relative to \(g_0\) on the whole surface is at most \(80b+1600b^2\), since the R781 base is globally weakly short relative to \(g_0\) and \(\|DA^\mathsf T DA-\operatorname{id}\|\leq80b+1600b^2\). There is a finite remaining defect for every choice here. At the terminal ring \(x=1/6\), the axial height is at most \(.5-S+1/6<.117\). On a whole neighborhood the gate is zero, so its relative angular row is precisely \([1-(1-\xi)d_*]^2\), with \(d_*>.135\) by R781. The deficit exceeds \(1-(1-.94\cdot.135)^2>.23\). Any improvement of that row toward \(10^{-6}\) must come from a further physical solve, with the same metric and full shell. Quadrature evaluations and triangular meshes of this reference provide reproducible numerical fields, while the estimates above concern the continuum maps.
