# R758 — Initially curved cap collars, an isometric elliptical crown and a free physical annulus

2026-11-28. We give a new complete initial metric, two evolving nonplanar cap disks and two finite isometries on named subdomains. The first covers the whole moving right wall, its two complete end rolls and genuinely curved cap bands of width .007. The second covers the complete common elliptical bowls of physical diameter at least .988. A closed physical field joins those regions. Two nonlinear fitting systems can vary their middle annuli, or the outgoing rolls as well. Their finite residuals and the full tubular-radius estimate are separate questions.

The [closed six-jet source](../scripts/resume_20261126/r758_curved_outer_collars_and_fixed_elliptical_crowns.py) and [full physical fitting source](../scripts/resume_20261126/solve_r758_curved_crown_middle_annuli.py) specify the common material positions. All branches refer to this field's actual time-zero metric. The initially flat cap interiors of [R756](R756-flat-ruling-cap-obstruction-and-preloaded-exact-returning-rolls.md) are replaced here.

## 1. A reverse turn on the actual initial cap

Use the preloaded right wall of R756, material half-length .66, initial cut height .63, four softened heading ramps and one .06 positive dwell, the R740 main curve at height .71, rigid left wing and common eccentric spatial rotation. Put $W=.007$, $e=.001$, $J_*=W+e/2=.0075$. The original end has radius .132, arclength $L=.132\pi/2+.0005$, angle $\alpha$ increasing from zero to $\pi/2$, $p'=\cos\alpha$, $d'=\sin\alpha$; set $p_b=p(L)$, $d_b=d(L)$. The signed section curvatures on the whole active right wall, both halves, equator and .10 adjacent straight tracks obey $\kappa_\theta=a\kappa_0$, $a=\lambda_\theta/\lambda_0\ge1$. The range is $0\le\theta\le.90$. Use R756's flat-end time change for smooth onset.

For $0\le w\le J_*$ define the new original unit-speed meridian by
$$
 \beta(w)=.014 S_5(w/W),\qquad
 D_0=d_b+\int_0^w\cos\beta(t)\,dt,\qquad
 P_0=p_b+\int_0^w\sin\beta(t)\,dt .
$$
The rising clamped quintic satisfies $\beta,\beta'>0$ on $(0,W)$ and $\beta(0)=\beta'(0)=0$. On each whole real right roll use (3) of R756, with $D=d/a,\ P_\theta'=\sqrt{1-a^{-2}\sin^2\alpha}$. On both true cap collars set
$$
 D_\theta=D_0/a,\qquad
 P_\theta=P_\theta(L)+\int_0^w\sqrt{1-a^{-2}\cos^2\beta(t)}\,dt,\qquad
 F_{\theta,\sigma}=(\gamma_\theta-D_\theta n_\theta,\ \sigma(1+P_\theta)),\quad \sigma=\pm1 .
 \tag{1}
$$
Positions are grouped as $(xz,y)$. At zero phase this recovers the original whole curved cap meridian since $\sin\beta\ge0$. Because $n'_\theta=\kappa_\theta T_\theta$, the angular length factor is $1-D_\theta\kappa_\theta=1-D_0\kappa_0$ and its tangent is perpendicular to the unit meridian. Therefore the exact first form throughout this band is the original $dw^2+(1-\kappa_0(s)D_0(w))^2ds^2$. Its intrinsic Gaussian curvature is
$$
 K_0=-\frac{\kappa_0(s)\sin\beta(w)\,\beta'(w)}{1-\kappa_0(s)D_0(w)}.   \tag{2}
$$
Every label with nonzero original wall curvature has nonzero intrinsic curvature at **every** $0<w<W$. The R756 negative-section-curvature label meets positive intrinsic curvature immediately after its actual rim, before any open transverse planar region. At the rim the two meridians have matching positions, tangents and second derivatives, since $\alpha'(L)=\beta'(0)=0$. The formula also covers the fixed-heading dwells, on which both section curvatures remain zero.

Outside that exact region use the R756 straight-track transition $\chi(s)$, equal to one through the wall and adjoining .10 and zero .30 above the true cut. In roll and cap formula (1) put $\cos\psi$ in place of $1/a$, $\psi=\chi\arccos(1/a)$. Add to the cap height
$$
 (1-\chi(s))\,\frac{.00030}{W^2}w^3
       \exp[(\gamma_{0,x}(s)+.3\gamma_{0,z}(s))/2].                 \tag{3}
$$
The two-jet of (3) vanishes at the rim and it is identically zero in the exact right region. On an originally straight horizontal or vertical interval with $\chi=0$, the exponential $A(s)$ has nonzero constant logarithmic derivative $q$. The initially curved meridian has height $p_b+O(w^4)$ and planar inward displacement $w+O(w^7)$. In graph coordinates along and across the original straight edge the new term is $cA(s)w^3$ to leading order, $c=.00030/W^2$. The leading physical graph-Hessian determinant is
$$
 c^2[6AA''-9(A')^2]w^4=-3c^2q^2A^2w^4.
$$
Thus the previously flat open caps adjacent to the original straight main-sheet intervals acquire strictly negative intrinsic curvature at every sufficiently small positive transverse depth. Formula (2) gives the separate exact computation on the preloaded right. These are changes of the actual initial metric. Alone they do not establish an arbitrary global continuation.

## 2. A fixed curved bowl and an embedded continuation

Put $c=(c_x,0)$, $c_x=u_*+.15$. Take the common closed ellipse
$$
 E=\{(x,z):[(x-c_x+.49)/.494]^2+(z/.22)^2\le1\}.
$$
The point $c$ is strictly inside near its right tip. The positive radial function $r_E(\phi)$ about $c$ solves
$$
 (r\cos\phi+.49)^2/.494^2+r^2\sin^2\phi/.22^2=1.
$$
On the entire regular Cartesian chart of $E$ prescribe
$$
 (x,z)\longmapsto(x,z,\ \sigma[1+p_b+\Delta_\theta+.040((x-c_x+.49)^2+z^2)]),
 \qquad \Delta_\theta=.45[P_{\theta,\mathrm{right}}(L)-p_b].         \tag{4}
$$
Before the final common rotation each bowl is a rigid transverse translation of its initial position. Its original graph Hessian is $.080I$, with strictly positive Gaussian curvature everywhere. Its projected physical diameter is $.988$. The fitting source also allows an independent three-component **rigid** translation of each complete inner bowl.

For $0\le w\le1$ use $j=w$ through $W$, $j'=1-S_5((w-W)/e)$ until $W+e$, and then the constant $J_*$. Let $\rho=1-(w-j)/(1-J_*)$. Substitute $j$ in the meridian integrals and (3). The projected outer leaf is $\gamma_\theta-D_0(j)\cos\psi\,n_\theta$. Denote its lifted section angle and radius about $c$ by $\phi_{\rm out},R$. For section period $P$ put $\phi_0=\pi-2\pi s/P$ and
$$
 \phi=\phi_0+S_7((\rho-.82)/.04)(\phi_{\rm out}-\phi_0),\qquad
 r=\rho\left[\frac{r_E(\phi)}{.82}+
 S_7((\rho-.87)/.10)\left(R-\frac{r_E(\phi)}{.82}\right)\right].
$$
The projection is $c+r(\cos\phi,\sin\phi)$, and the height interpolates by $S_7((\rho-.82)/.16)$ from (4) to (1) with (3). Near the actual rim this is the entire exact outward formula and all material two-jets match. For $\rho\le.82$ it covers exactly the common bowl. Its genuine Cartesian chart includes the polar center and agrees on overlaps. These definitions give physical fields at both signs and all phases.

We give uniform margins for the projected atlas. In the old unaffected pieces the section support is at least $1/7$ and its absolute curvature is below 7. The planar offset $D_0\le.1325+.0075=.14<1/7$. On the positive right lobe R756 gives support $\ge\min(.149,1/(7.2\lambda_\theta))$. On its negative lobe the bound is .149. The true adapted offset there is at most $.14\lambda_0/\lambda_\theta$. At $\lambda=1$ the available projected loss exceeds $.135+.06(1-\cos1.44)>.187$, so $\lambda_0^2\le.03/.187$ by $1-\cos(\lambda t)\ge\lambda^2(1-\cos t)$. Both terms of the positive support bound strictly exceed the actual offset and $1-D_0\kappa_0>0$. On the straight transition track the monotone change of $\cos\psi$ adds nonnegative outward support as in R756. All these projected leaves remain simple, star-shaped and strictly nested. For varying $\cos\psi(s)$ this follows directly from the still-positive tangent projection in the section direction and inward velocity $-\cos\psi\,n_\theta$.

The ellipse dilated by $1/.82$ about $c$ lies strictly inside all the projected leaves. Its box is $c_x-.984/.82\le x\le c_x+.004/.82$, $|z|\le .22/.82<.269$. At these low heights the two outside walls are the only boundaries. The right abscissa is $\ge x_R\ge c_x+.149$, hence still $\ge c_x+.009$ after offset. The upper and lower main-sheet pieces stay outside the low strip by the original height $.71$ and offset $\le.14$. The left wall is at $x\le-1.149+.135+.14<-.874$ after offset, whereas $c_x-.984/.82>-.63$. The remaining turns and high track pieces lie above or below the strip. Thus the common box is inside and $R>r_E(\phi_{\rm out})/.82$ on every ray. In the radius-blend interval the angle already equals $\phi_{\rm out}$ and $j$ is constant, giving strictly increasing radii with $\rho$. During the angle blend the leaves are nested copies of the same ellipse, and the convex combination of two strictly monotone degree-minus-one angle lifts remains strictly monotone. This proves a regular projected disk with the stated Cartesian center. Its upper and lower heights have opposite signs. The projected end and cap meet the central cylinder only at the prescribed seams, proving an embedded closed sphere for the baseline family.

The genuine upper circular grip remains pointwise fixed after rotation and has diameter at least 1.40. The R754 left-wall witness still gives distance $>1.09$ to the whole final baseline: the right wall stays at $x>.25$ and all end projections lie inside the true section. The new middle curvature and the full tangent-ball bound are additional extrinsic costs; the old R756 thickness estimate cannot be transferred to this cap join.

## 3. Genuine physical fitting on the two signed ends

The middle annulus has material width $1-.82(1-J_*)-W>.17$; its physical width depends on angle. The two signed ends and two freedom choices are four independent numerical systems. All displacement coefficients have three spatial components. Fourier functions run around the entire material section. Each radial packet uses clamped $S_7$ envelopes and cosine modes, so position and two derivatives match at its endpoints. The common coordinate is $\tau=|y|-1$ on the central half, $\tau=v$ on a roll and $\tau=L+w$ on a cap. The cap-normal and polar charts use the correct opposing derivatives of $w$ and the signed halves match at the cylinder seams.

In the **outer-locked** system, the middle packet runs from $w=W$ to the true bowl boundary $w=1-.82(1-J_*)$. A second packet covers the remaining rolls and their cap continuation with angular factor $1-\chi(s)$, from $\tau=0$ to $\tau=L+.12$. This preserves the whole right active isometry (1), including both true curved collars. In the **free-end** system that packet acts all the way around the section and starts on the actual central cylinder at $|y|=.70$. It can change the outgoing position, tangent and second derivatives at each signed end. The stationary open grip and the four marked patches are preserved. Both choices allow a separate three-component translation of the whole inner bowl, switched on from $w=.025$ and constant by its true boundary. There is no other boundary correspondence imposed between the two signed fits.

At a measured position $A,B$ are the gradients in an oriented orthonormal frame of the **actual initial** metric. The three metric residuals are $|A|^2-1,\sqrt2 A\cdot B,|B|^2-1$. Two curvature residuals use the negative parts of the minimum eigenvalues of $8G+II,8G-II$ in this same frame. The support residual is the positive part of $.125-(F-c)\cdot n$, with the oriented physical normal of the chart. These are objective terms; no target threshold removes phases or cells. The two curvature inequalities characterize the sampled absolute principal-curvature bound when $G$ is positive definite. The derivatives include the projected differential of the actual normalized $A\times B$ and all its first- and second-jet dependencies. Both the Jacobian and its transpose are explicit linear operators. Independent denser checks compute principal values with the physical tangent SVD and give all three relative metric, support, area and rank diagnostics.

The full levels have angular Fourier orders 2, 3, 5, radial orders 2, 3, 4, and budgets 12, 20, 30 nonlinear evaluations per nonzero phase. Original angular counts are 24, 40, 64; independent denser counts are 64, 96, 144, supplemented by the complete signed wall, ramp, cap and grip anchors. At each level seven phases from 0 through .90 are fitted on the same original field. The continuous reconstruction uses quintic interpolation of the entire spatial coefficient arrays between neighboring phases. Its additional six intermediate phases are independently evaluated. Sixteen original cap paths from the true rim to the inner bowl are also evaluated at every level and phase. Their original path lengths bound the chords between the same material endpoints for any exact isometry. The full coefficient words remain on the runner with their complete identities and deterministic reconstruction source.

Every fit covers the whole signed central half, the whole actual roll, the entire polar cap, its true normal collar and the whole regular Cartesian bowl. Pairing signs covers the full nine-chart sphere, with agreement on their common undeformed center. The public controller freezes the original source words, retains the four real process identifiers and continues ordinary pull/rebase and both README comparisons during the calculation. Its four independent logical results and their index retain the complete returned finite conclusions. A continuum metric, global reach or motion conclusion about an optimized field would still require checking that actual field over its full spatial and temporal domains.
