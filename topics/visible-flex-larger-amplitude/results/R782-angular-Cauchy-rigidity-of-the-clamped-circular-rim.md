# R782. Angular Cauchy rigidity at a fully clamped circular rim

Fix the R781 initial circular cylinder metric. The complete material circle at one axial end determines an exact embedding of the cylinder in the class with locally uniform angular analyticity of its second fundamental form, if its position and transverse first derivative are prescribed there. This holds through the sign changes and zero bands of the intrinsic Gaussian curvature. The boundary assumption matters for a search that holds an interior part of a cap and lets its rim move.

## Statement and hypotheses

Use axial arclength \(x\in[0,1]\) and circular arclength \(s\in\mathbb R/(2\pi R)\mathbb Z\). The reference cylinder has radius function \(R-Z_0(x)>0\) and metric
\[
 g=dx^2+a(x)^2\,ds^2,\qquad a(x)=1-Z_0(x)/R .
\]
Write \({\bf n}(s)=(\cos(s/R),\sin(s/R))\) in the transverse plane, and \({\bf e}_Y\) for the axial direction. The reference map is
\[
 F_0(x,s)=(R-Z_0(x)){\bf n}(s)+Y_0(x){\bf e}_Y,\qquad
 (Z'_0)^2+(Y'_0)^2=1.
\]
For the R781 initial angle clock \(|q_0w(x)|\leq .6\), \(Y'_0=\cos(q_0w)\geq\cos(.6)>0\). The argument below applies to any such circular metric with \(a\in C^2\), \(a>0\) and continuous nowhere-zero \(Y'_0\).

Let \(F\) be a \(C^2\) immersion of the complete cylinder with \(F^*e=g\). Assume the boundary data at the right rim
\[
 F(1,s)=F_0(1,s),\qquad F_x(1,s)=F_{0x}(1,s)\quad\text{for every }s .
 \tag{1}
\]
Let \(e_1=\partial_x,e_2=a^{-1}\partial_s\) be the intrinsic orthonormal frame. Use the same orientation to measure the second fundamental forms of both immersions. Write \(L=h(e_1,e_1), T=h(e_1,e_2), N=h(e_2,e_2)\). At each axial station assume that on a relative axial neighborhood, \(T(x,\cdot),N(x,\cdot)\) extend to periodic holomorphic functions on a common strip \(|\operatorname{Im}s|<\rho\) with a common finite bound. The width and bound may vary between neighborhoods and embeddings. No analyticity in \(x\) is required. The reference coefficients have this property since they are angularly constant.

Then \(F=F_0\) on the entire cylinder. The result applies separately to each member of a family with data (1). The same conclusion holds after a single common Euclidean alignment if the whole trace in (1) is prescribed up to that alignment.

## A first-order angular system with continuous axial coefficients

Orient the normal via \(F_x\times F_s/a\). The connection coefficients of the frame are \(\nabla_{e_1}e_i=0\), \(\nabla_{e_2}e_1=p e_2\), \(\nabla_{e_2}e_2=-p e_1\), with \(p=a'/a\). The intrinsic Gaussian curvature is \(K=-a''/a\). The Gauss and Codazzi identities give
\[
 LN-T^2=K,\qquad
 T_x=a^{-1}\partial_s L-2pT,\qquad
 N_x=a^{-1}\partial_s T+p(L-N).
 \tag{2}
\]
At \(C^2\) regularity these identities hold distributionally, which suffices here. Indeed the moving frame and the normal are \(C^1\). In the commuting mixed distributional derivatives of its frame columns, one may substitute the continuous Gauss–Weingarten coefficients by the product rule. The normal projections give the Codazzi identities, and the tangent projections give the Gauss identity with the \(C^2\) metric. All products are of continuous frame coefficients, or derivatives of such coefficients paired by integration by parts with a \(C^1\) frame. The Gauss identity is an equality of continuous functions.

With subscript zero indicating \(F_0\), \(T_0=0\) and
\[
 |N_0(x)|=|Y'_0(x)|/(R-Z_0(x))>0 .
\]
One gets these expressions by differentiating the circular parametrization in \(s,x\) and projecting on its unit normal. At the clamped rim (1) gives the reference values of \(F_s,F_{ss},F_{xs}\) and the oriented normal. In particular it gives \(T=T_0,\ N=N_0\) there.

Suppose equality of \(T,N\) holds at an axial circle \(x=x_*\). On some relative axial interval around \(x_*\), \(N\) stays uniformly separated from zero on the real angular circle by continuity. It also stays separated from zero on a smaller common complex strip. For this last step shrink the given strip once to bound \(\partial_sN\) by Cauchy's estimate, then shrink it again so that the variation from a real value is less than half the real lower bound. Uniform holomorphic bounds and continuity on the real circles also give continuity in \(x\) on each strictly smaller strip. To see this, take a sequence of axial stations converging to one station. Every subsequence has a further subsequence converging uniformly on compact substrips by the holomorphic bounds. Its limit agrees with the real trace there and hence is the unique holomorphic extension. Periodicity gives uniformity on a closed fundamental period.

Set \(u=T-T_0,\ v=N-N_0\). On this interval the exact Gauss equation gives
\[
 L-L_0=c_1u+c_2v,\qquad
 c_1=(T+T_0)/N,\qquad c_2=-(K+T_0^2)/(N N_0).
\]
All displayed coefficients and their angular derivatives on smaller strips are bounded and continuous in \(x\). Subtraction in (2) yields the linear equation in the already given difference \(D=(u,v)^\mathsf{T}\),
\[
 \partial_xD=\mathcal L_xD,\qquad
 \mathcal L_xD=a^{-1}
 \partial_s\begin{pmatrix}c_1u+c_2v\\u\end{pmatrix}
 +p\begin{pmatrix}-2u\\c_1u+(c_2-1)v\end{pmatrix}.
 \tag{3}
\]
The coefficients may depend on the candidate \(F\); in this uniqueness argument they are bounded functions fixed by that candidate. The right hand side is continuous in \(x\) on real circles. Thus (3), initially distributional, has the usual axial integral form. That integral form extends to smaller strips by holomorphicity and the identity theorem.

## Local uniqueness and continuation

Choose a strip of width \(\rho_0>0\) inside the preceding bounds. Write \(\|\cdot\|_\sigma\) for the supremum over a period on \(|\operatorname{Im}s|<\sigma\). Cauchy's inequality, applied to each product inside \(\partial_s\), gives
\[
 \|\mathcal L_x V\|_{\sigma'}\leq
 \frac{C}{\sigma-\sigma'}\,\|V\|_\sigma
 \qquad(\rho_0/2\leq\sigma'<\sigma\leq\rho_0)
\]
with \(C\) independent of the two widths and the station in this interval. The order-zero term is absorbed using \(\sigma-\sigma'\leq\rho_0\). From \(D(x_*)=0\), iterate the integral identity \(n\) times over an axial segment of length \(h\), using the \(n\) equal strip losses between \(\rho_0\) and \(\rho_0/2\). The ordered \(n\)-simplex of integrations has volume \(h^n/n!\), in either axial direction. For \(M=\sup_x\|D(x)\|_{\rho_0}\) on the neighborhood this gives
\[
 \|D(x)\|_{\rho_0/2}
 \leq M\frac{(2Cnh/\rho_0)^n}{n!}
 \leq M(2eCh/\rho_0)^n .
\]
For \(h<\rho_0/(2eC)\), taking \(n\) to infinity gives \(D=0\). Neither the sign of \(K\) nor its axial derivative occurs in this argument.

The set of stations with \(T=T_0,\ N=N_0\) on the full real period is closed by continuity. It contains the right endpoint and is relatively open by the local proof and the strict nondegeneracy of \(N_0\). The connected interval gives equality everywhere. Gauss now determines \(L=L_0\). The two moving frames and the two positions agree on the clamped rim. Along an axial line the common metric, second form, and initial frame give identical linear Gauss–Weingarten equations with continuous coefficients. Unique integration fixes the frame, and integration of \(F_x\) fixes the position at every material point.

## Scope for the numerical families

A candidate surface whose world coordinates are finite angular Fourier sums of uniformly bounded degree, with continuous axial derivatives through order two, satisfies the strip condition when it is an exact isometry of this metric. Indeed its normal is the cross product \(F_x\times F_s\) divided by the exact \(a(x)\). Multiplying by the second derivatives gives finite trigonometric polynomials for \(T,N\) with bounded coefficients on compact intervals. Explicit analytic angular formulas give the same consequence when their own uniform strips and bounds hold.

This theorem constrains the cylinder of an exact solution with the whole prescribed rim first jet. An inner-cap grip may permit real changes of that rim, including its position and transverse derivatives. A general \(C^2\) isometric immersion need not have the assumed angular extensions, and the argument gives no uniform stability estimate for candidates with a small positive metric error. In particular a sequence of fits may lose all uniform angular strip control as the discretization changes. Each fitted full closed surface still requires its own metric, reach, embeddedness and motion measurements. The theorem supplies no conclusion about a left cap that is separately allowed to move while its cylindrical neighbor stays fixed.

## A flat disk with a held central subdisk

There is a second rigidity mechanism on a Euclidean end disk. Here the hypothesis concerns only the positions on individual circles. Let \(B_R\subset\mathbb R^2\) carry the ordinary flat metric and let \(I\) be its inclusion in a plane in \(\mathbb R^3\). Suppose \(G:\overline B_R\to\mathbb R^3\) is \(C^2\), isometric, and agrees with \(I\) on \(B_h\), \(0<h<R\). If for every \(0<r<R\) the vector \(G(r\cos\theta,r\sin\theta)\) is real analytic in \(\theta\) on the full circle, then \(G=I\) on the whole closed disk. No uniform strip estimate in \(r\) is needed here.

The set \(E=\{p:G(p)=I(p)\}\) is closed and convex. For any \(p,q\in E\), isometry gives the same length \(|p-q|\) to the straight material segment as to its Euclidean image endpoints' chord. Equality in the Euclidean length bound and the constant-speed parametrization force \(G=I\) on the entire segment. If \(E\) does not contain the open disk, take a point of its boundary in \(B_R\). Call it \(q\). The convex hull of the inner ball and \(q\) gives interior fixed points converging to \(q\), so \(DG(q)=DI\). The immersion cannot be locally affine there, since an affine map with these position and derivative data equals \(I\).

Use the flat-isometry developability theorem at \(q\). It gives a single complete material line segment through \(q\) with both endpoints on \(\partial B_R\) along which \(DG\) is constant. This theorem applies to a \(C^2\) isometric immersion of the convex disk; it also holds for \(W^{2,2}\) flat isometries. The constant derivative here is \(DI\). Integrating along the line and using boundary continuity gives a fixed outer boundary point \(b\). For the developability statement see M. R. Pakzad, *On the Sobolev space of isometric immersions*, Journal of Differential Geometry **66** (2004), 47–69, and P. Hornung, *Approximating \(W^{2,2}\) isometric immersions*, C. R. Acad. Sci. Paris, Ser. I **346** (2008), 189–192, sections 2–3. [Pakzad](https://doi.org/10.4310/jdg/1090415029) · [Hornung, 2008](https://doi.org/10.1016/j.crma.2008.01.001)

The convex hull of \(B_h\) and \(b\) contains an open angular arc of every material circle with \(h\leq r<R\). Indeed \((r/R)b\) has an open ball of radius \((1-r/R)h\) in this hull. The position difference \(G-I\) vanishes on each such arc. Angular real analyticity gives its vanishing on each whole circle and then on the outer boundary by continuity.

The preceding argument permits a direct construction once angular analyticity on the whole circle is relaxed. In material Cartesian coordinates \((X,Z)\) take a smooth one-variable angle \(\beta_t(X)\) with \(\beta_t=0\) for \(X\leq h_1\), where \(h<h_1<R\), \(\beta_0=0\) everywhere, and \(0\leq\beta_t<\pi/2\). Define
\[
 C_t(X)=X+\int_{h_1}^{X}(\cos\beta_t(u)-1)\,du,\quad
 H_t(X)=\int_{h_1}^{X}\sin\beta_t(u)\,du,\quad
 G_t(X,Z)=(C_t(X),Y_R+H_t(X),Z).
\]
The Cartesian derivative vectors are \((\cos\beta_t,\sin\beta_t,0)\) and \((0,0,1)\). They give exactly the original metric. Since \(C'_t>0\), the map is an embedding of the whole disk. The inner disk is fixed pointwise, and choosing a positive angle on an interval in \((h_1,R)\) moves an outer arc. On a material circle that contains fixed and moved open arcs this field is not globally real analytic in the angle. Its physical smoothness in material and time follows from that of \(\beta\). This supplies a moving flat cap and its actual rim data; the metric and quantitative normal tube of the attached roll and the rest of the closed shell remain separate requirements. A fixed entire cap by itself also does not supply the nonzero \(N_0\) hypothesis through the planar cap-to-roll join.
