# R739 — Developed-axis measurement of an exact flex and the sharp reach limit for weak displacement

2026-11-28. Hu's qualitative closed flex is already recorded in the neighboring topic. We prove a finite-amplitude whole-image displacement test using two developed radii, compute the exact leading Hausdorff displacement on the nonlinear branch, and determine the optimal normalized reach as a supremum when held displacement need only be positive. This is a new metric design. It supplies neither a field in the original Fejér/R690 metric nor a numerical $.2D$ displacement or the requested mesh deliverables.

## 1. The nonlinear input and its scale

Use Boyang Hu, [*Smooth isometric bending of a closed sphere*, 2611.00534v1](https://hexagonmath.org/pdf/2611.00534v1), Proposition 2.3 (p.13), Proposition 4.2 (pp.25–26), Lemma 7.6 (p.68), Theorem 10.3 (pp.106–107). We use the theorem as stated. Write $g_q=(1+w_q^2)dr^2+r^2d\theta^2$, $z_q=h_{w_q}+q u_q$, $h_w'=w$. Add constant-height collars and fill the inner disk. The orientation-preserving planar development $P_q$ normalized to the identity on the outside collar has $P_q^*I_2=g_q-dz_q^2$. The true disk embedding $X_q=(P_q,z_q)$ is a graph of $Z_q=z_q\circ P_q^{-1}$. Fix the outside height at zero. The material height $z_q$ is even and $\pi$-periodic in $\theta$. The seed in the paper's convention is $\Phi_*=\sqrt2\,\varphi_*(r)\cos(2\theta)$.

Any fixed $\alpha>0$ may be chosen before invoking the existence theorem, with $w_\alpha=\alpha w_*$ as reference. All $L_{j,w}$ of Proposition 4.2 are linear in $w$. Their kernels, the seed $\varphi_*$, and the endpoint admissible space persist. The travel angles depend on $w'/w$, so retain all arithmetic bounds and roots. Set $\chi_{*,\alpha}=\chi_*/\alpha$. The bordered column $g_*=L'_{2,w}[w\chi_*]\varphi_*$, its normalization and row $\ell_*$ then remain identical. If the original bordered inverse maps $(f/\alpha,c)$ to $(u,b)$, the scaled inverse maps $(f,c)$ to $(u,\alpha b)$. The norm and derivative estimates acquire at most the multiplier $\max(1,\alpha)\max(1,\alpha^{-1})$. Use the same cells, weights and exponents with constants depending on $\alpha$. The multiplicative travel controls of Lemma 7.6 still work since $T_m(\alpha w e^{t\chi_m})=T_m(w e^{t\chi_m})$. Theorem 10.3 applied to these data gives $q_0(\alpha)>0$ and $w_{\alpha,q}-\alpha w_*=O_\alpha(q^2)$ in every fixed $C^j$ norm. Its endpoint estimates with parameter derivatives give the same smooth extensions and $z_{\alpha,q}=h_{\alpha w_*}+q\Phi_*+O_\alpha(q^2)$ in $C^2$ of the closed disk. The outer height normalization adds no linear term. No uniform estimate from below for $q_0(\alpha)$ is asserted.

The normalized development is smooth in $q$ in $C^2$: take the positive square root of the metric matrix in Cartesian disk coordinates for a smooth oriented coframe. Its connection form is closed. Integrate it from the outer collar, rotate the coframe by the resulting angle, and integrate the closed coframe with the same normalization, as in Hu's Proposition 2.3. Flatness gives path independence, and integration on prescribed paths gives smooth dependence using the preceding estimates in sufficiently many derivatives. At $q=0$ the development is the identity. Fix any admissible nonzero $q$ and freeze $w_{\alpha,q}$ at all phases. On the disk use
$$
 X_{q,t}(r,\theta)=\mathcal R_t X_q(r,\theta-t),\qquad 0\le t\le2\pi,              \tag{1}
$$
where $\mathcal R_t$ rotates space around the vertical axis. On the outer collar (1) returns the original fixed planar chart. A stationary attached complement carries its own fixed metric. Different values of $q$ in an asymptotic argument describe different candidate designs.

## 2. A finite-amplitude test using two physical radii

Take an outer collar radius $r_b$ and let $0\le r\le r_b$. Reflection across either coordinate axis preserves $g_q-dz_q^2$. Uniqueness of the normalized planar development gives equivariance of $P_q$ under each reflection. Its restriction to either full axis is injective, differentiable with nonzero derivative, equals the identity on the outer collar and fixes the center. Thus each positive half-axis maps to itself with positive derivative. At $i=0,\pi/2$, put $z_i(r)=z_q(r,i)$. The exact physical radius there is
$$
 R_i(r)=r_b-\int_r^{r_b}\sqrt{1+w_q(s)^2-z_i'(s)^2}\,ds .                         \tag{2}
$$
In particular $R_i(0)=0$ and $R_i(r_b)=r_b$. For the two axes $i,j$, choose a witness over physical radius $R_i(r)$ and set
$$
 r_j=R_j^{-1}(R_i(r)),\qquad d_z=|z_i(r)-z_j(r_j)| .                             \tag{3}
$$
The second graph at phase $\pi/2$ has the height on the other axis there, by reflection and the half-turn. Equal material parameters generally differ from (3).

Let $e=|dz_q|^2_{g_q}=z_r^2/(1+w_q^2)+z_\theta^2/r^2$, continued at the center in Cartesian coordinates, and $e_0=\sup e<1$. Inversion of the graph metric $I_2+dZ_q^2$ gives $|\nabla Z_q|^2=e/(1-e)$ at corresponding points. The physical footprint is a convex disk. Thus each phase graph is Lipschitz with $L=\sqrt{e_0/(1-e_0)}$. For the graph witness $p$ and any comparison graph point $y$, $d_z\le |p_z-y_z|+L|p_{\rm hor}-y_{\rm hor}|\le\sqrt{1+L^2}|p-y|$. With $C$ the whole stationary complement including the attaching boundary, the entire closed images satisfy
$$
 d_H(S_{q,0},S_{q,\pi/2})\ge\min\{{\rm dist}(p,C),\,d_z\sqrt{1-e_0}\}.            \tag{4}
$$
Both axis orders and every radius are allowed. One may replace the second entry by $\min(b_0,d_z\sqrt{1-e_{\rm loc}})$, where $e_{\rm loc}$ bounds the comparison phase on the preimage of the horizontal ball of radius $b_0$ about the witness footprint. The ball intersected with the physical disk is convex, and more distant horizontal competitors cost $b_0$. If the closure uses a flat outer top annulus, an outer side at radii $\ge R_{\rm side}$, and a bottom at heights $\le z_B$, the minimum of the radial gap to the fixed top annulus, $R_{\rm side}-R_i(r)$ and $p_z-z_B$ bounds the first entry from below when positive. Any additional fixed protrusions must be included. The explicit test (4) retains the whole closed comparison surface. The existence theorem alone gives no $.2D$ lower bound.

## 3. Exact displacement coefficient on the nonlinear branch

Fix $\alpha$, abbreviate $w=\alpha w_*$ and put $\phi=\sqrt2\,\varphi_*$. The reference and its upper unit normal are $X_*=(r e_r,h_w)$ and $n=(-w e_r+e_z)/\sqrt{1+w^2}$. Its variation $Y=\partial_qX_q|_{q=0}$ satisfies homogeneous linearized isometry since $\partial_qg_q|_0=0$. Its material height is $\phi\cos m\theta$, $m=2$. Write
$$
 Y=A(r)\cos(m\theta)e_r+B(r)\sin(m\theta)e_\theta+\phi(r)\cos(m\theta)e_z.
$$
Indeed the linear equations separate into angular modes; a residual horizontal solution with zero vertical field satisfies the planar Killing equation and is zero by the outer normalization. Equivalently construct the displayed candidate and use this uniqueness. The $\theta\theta,rr,r\theta$ equations give
$$
 A+mB=0,\qquad A'=-w\phi',\qquad rB'-B-mA-mw\phi=0 .
$$
Consequently
$$
 A=\frac{w(r\phi'-m^2\phi)}{m^2-1},\quad B=-A/m,\qquad
 n\cdot Y=W_\alpha(r)\cos(m\theta),\quad
 W_\alpha=\frac{\phi+w^2(m^2\phi-r\phi')/(m^2-1)}{\sqrt{1+w^2}}.               \tag{5}
$$
Differentiating $A$ and imposing $A'=-w\phi'$ is precisely $r(w\phi')'-m^2w'\phi=0$, Hu's seed equation. On the flat extensions the seed vanishes. At an interior maximum of $|\phi|>0$, $\phi'=0$, $w>0$, and $|W_\alpha|=|\phi|(1+m^2w^2/(m^2-1))/\sqrt{1+w^2}>|\phi|$. Thus slope can enhance normal speed. This coefficient does not imply a finite admissible large $q$.

Suppose a stationary compact complement closes the graph to a $C^2$ embedded surface at $q=0$. On the glued material surface $X_{q,t}=X_*+qY_t+O(q^2)$ uniformly in $t$ in $C^1$, with zero variation on the complement. Here $n\cdot Y_t=W_\alpha(r)\cos(m(\theta-t))$ on the graph. For two such compact perturbations the Hausdorff distance is $|q|$ times the maximum absolute difference of normal variations, up to uniform $O(q^2)$. In a finite system of regular charts, decompose the variation difference into tangent and normal parts. Shift the comparison parameter by its linear $O(q)$ tangential dislocation to give an upper bound in each direction with quadratic error. A nearest comparison point has spatial separation $O(q)$ from the original base point and hence parameter separation $O(q)$ in a common chart, by compact embeddedness and a local bi-Lipschitz bound. Taylor expansion and projection on the base normal give the lower bound at a point maximizing the absolute normal difference. The closed manifold avoids a seam loss. Hence
$$
 \begin{split}
 d_H(S_{q,t},S_{q,0})&=2|q|\,|\sin(mt/2)|\,\|W_\alpha\|_\infty+O_\alpha(q^2),\\
 \delta_{\rm hold}&=2|q|\,\|W_\alpha\|_\infty+O_\alpha(q^2).
 \end{split}                                                                    \tag{6}
$$
The quarter-turn reaches the leading term for $m=2$. The constants can depend on the closure. Since $D_q=D_*+O_\alpha(|q|)$, the normalized slope is $2\|W_\alpha\|_\infty/D_*$. A spatial similarity changes both length quantities equally.

## Appendix. Optimal reach when held displacement need only be positive

At the initial phase let $R_{\rm in}$ be the maximum distance from a point of the compact enclosed body to its boundary. The body diameter is its boundary diameter $D$ since an interior endpoint could be moved further along a maximizing segment. The largest inscribed ball gives $2R_{\rm in}\le D$. Its center has at least two nearest boundary points: otherwise squared distance to the compact boundary is differentiable there with nonzero gradient twice the center minus twice the unique nearest point, contrary to interior maximality. For the differentiability claim, bound the change of squared distance using the old and new nearest points; compactness and uniqueness force the latter to converge to the former. Hence $\inf_t\operatorname{reach}(S_t)/D\le\operatorname{reach}(S_0)/D\le1/2$ for every such family.

For sharpness take a smooth convex body with upper and lower flat disks and a side containing no planar open set. For instance choose disks of radius one and a side of arclength one with outward/descending tangent $(\cos\beta,\sin\beta)$, $\beta(s)=\pi\int_0^s b/\int_0^1b$, $b(s)=\exp(-1/[s(1-s)])$ for $0<s<1$, extended by zero. Symmetry gives the returning radius, positive drop, strict meridional curvature in the interior, and flat joins to all orders. The profile with its flat segments is convex; revolution about the vertical axis gives the body. Scale it to diameter $\eta>0$, denoting it by $K_\eta$, and add the closed unit ball by Minkowski addition. The new boundary $S_*$ is parametrized by $x+n(x)$ on $\partial K_\eta$, with $n$ the outward normal. The differential stretches each principal tangent by $1+\kappa_i\ge1$ in the convex-positive convention. Projection on the closed convex body is unique and inverts this map at distance one. The surface is smooth with translated flat disks, and the side still has no planar open set. Its diameter is at most $2+\eta$. The unit ball centered at each projection lies inside the body, and an exterior tangent open ball misses the body by convexity. These two ball conditions give $\operatorname{reach}(S_*)\ge1$ by the normal-chord criterion, and its absolute principal curvatures are at most one. See Federer, *Curvature measures* (1959), Theorem 4.18, p.449.

Place three disjoint outward $C^2$ bumps of distinct footprint radii with noncollinear centers strictly inside the bottom disk. The quartic compact profiles of [R732](R732-rounded-cap-exact-terminal-metric-and-full-reference.md) suffice: for fixed $\eta$ fix the footprints and allow their positive heights to tend to zero. No bump has a planar open subset. The bottom planar component has a boundary of four circles including three nonconcentric distinct-radii holes. Put a spatially scaled Hu disk with its outer collar strictly inside the top face, extending by that plane beyond. Fix the patch's physical scale for $\eta$, then choose $\alpha$ small and then a sufficiently small nonzero $q$ depending on both. At $q=0$ the graph is arbitrarily close to its flat patch in $C^2$ since $\alpha w_*\to0$ in each fixed $C^j$. For that fixed $\alpha$, $q\to0$ gives uniform-in-phase $C^2$ convergence to the radial graph by §1. The bottom markers can independently be made arbitrarily small in $C^2$. These choices make all embeddings arbitrarily $C^2$ close to $S_*$ in a common closed-surface parametrization.

For $0<\eta<1/4$, choose the perturbations so that $D<2+2\eta$ and $\inf_t\operatorname{reach}(S_t)\ge1-\eta$. For uniform reach, failure along a convergent sequence gives ordered parameter pairs violating the smaller-radius inequality. Distinct limiting parameters contradict the reference unit-ball inequality. At coincident limits a second-order chart Taylor expansion bounds the limiting ratio of twice the absolute normal chord to squared chord by the maximal absolute reference principal curvature, at most one; this is strictly less than $1/(1-\eta)$. Embedding holds by the analogous distinct-parameter and regular local-chart arguments. The stationary portion outside the grafting disk's interior is a closed grip with interior. Two opposite equatorial points therein have separation at least two, because their outward normal offsets are horizontal and opposed. This gives $\operatorname{diam}F_0(H)>.2D$.

No open part of the active annulus is planar: its intrinsic Gaussian curvature $w_qw_q'/[r(1+w_q^2)^2]$ is nonzero off the simple zeros of $w_q'$. On the upper face the outer flat component is annular and the inner flat component is a disk; the inner development is centered by Hu's Proposition 2.3. The convex side and the bump interiors have no planar open subset. The lower flat component is recognizable from the image by its four boundary circles. A Euclidean congruence fixes the bottom plane and all three centers individually because the distinct hole radii are smaller than the outer circle. It is the identity or reflection in that plane. Reflection cannot carry one phase onto another: the opposite side has points at height at least two above the bottom plane, whereas the only points below the plane are bumps of height less than one. Formula (6) gives different quarter-turn images at sufficiently small nonzero $q$. Compactness of the orthogonal group and boundedness of translations along any vanishing-distance sequence imply positive Euclidean-quotient Hausdorff distance. Every phase is continuously isometric to the one metric frozen at that $q$. Taking $\eta\downarrow0$ proves
$$
 \sup_{\rm weak\ exact\ families}\frac{\inf_t\operatorname{reach}(S_t)}{\operatorname{diam}S_0}
  =\frac12,\qquad \operatorname{diam}F_0(H)\ge .2D,\quad
  \delta_{\rm E}>0,\quad\delta_{\rm hold}>0 .
$$
Different $\eta$ specify different families, whose displacement may tend to zero. This supremum does not estimate the best reach subject to $\delta_{\rm hold}\ge .2D$. At that displacement an actual nonlinear solution together with whole-body reach and fixed-parameter refinement remains to be found.
