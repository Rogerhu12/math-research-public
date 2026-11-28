# R791. A pre-bent lever sphere with one longitudinal strain row and a global signed normal tube

Use one new sphere and one new phase-zero metric. A broad fixed planar grip, a genuinely moving distant cap and a long pre-bent waist give the following finite estimates on a complete physical family:
$$
 D<3.22,\qquad \operatorname{diam}F_0(H)\ge .648,\qquad
 \delta_{\rm hold}>.652,\qquad\delta_{\rm E}>0,\qquad
 \inf_t\operatorname{reach}(F_t(M))\ge .104.
$$
All three rows of the fixed metric are paid everywhere except for the longitudinal entry on the open waist. Its relative spectral error there is below $.096$, over the full material angle and phase. The initial waist already has both curvature signs with no open flat subset. These claims concern the prescribed reference, and do not make its nonzero waist error an exact flex.

## Actual closed material and placement

Use $t\in[0,\pi/2]$, axial spine material $s\in[-.85,1.95]$, conventional circular angle $\theta=e/.43$, and $B=1.4$. In the supplied atlas the central chart uses $s=v+.55$ and $v\in[-1.4,1.4]$. The starting axis angle is nonzero:
$$
 \Phi(t)=.10+.55\sin^2t,\qquad \psi(s)=\Phi(t)[1-P_c(s/B)].
$$
Here $P_c$ is the original R776/R781 integrated clipped clock, constant zero/one outside the unit interval, with $P_c(1-x)=1-P_c(x)$ and $0<P_c'\le1/.94$ on the open interval. In world order $(X,Y,Z)$ set
$$
 T=(\sin\psi,\cos\psi,0),\quad N=(\cos\psi,-\sin\psi,0),\quad
 C=(0,B,0)-\int_s^B T(u)\,du,\qquad
 \Psi(s,\xi,\zeta)=C(s)+\xi N(s)+\zeta e_Z .
$$
The frames are constant on both straight exterior rays. On the central chart use
$$
 r(s)=.11+.32[S_5(-s/.55)+S_5((s-B)/.55)],\qquad
 F=\Psi(s,r(s)\cos\theta,r(s)\sin\theta).
$$
Here and below $S_5$ is clipped to zero/one outside its unit interval. The region $0\le s\le B$ is the constant-radius waist. Both flares reach $.43$ with zero first and second derivatives at the joining ends.

At each $s_j=-.85,1.95$ attach the R781-style softened quarter turn of radius $h=.105$, terminal smoothing $\eta=.001$ and length $L=h\pi/2+\eta$. Write $p'=\cos\beta,\ d'=\sin\beta$ from zero, with $\beta'$ ramping via $S_5$ to $1/h$, staying constant, and ramping down over the last $\eta$. Let $p_b=d_b\in[.105,.106]$ be the terminal coordinate. The actual annulus uses
$$
 \Psi\big(s_j+\sigma p(b),(.43-d(b))\cos\theta, (.43-d(b))\sin\theta\big),\quad 0\le b\le L,
$$
where $\sigma=-1,+1$ at the left and right. The caps are filled plane disks of radius $a_b=.43-d_b\ge.324$ at $s_j+\sigma p_b$. Both have polar, Cartesian and true normal-overlap material charts with $\rho=1-w/a_b$. All end points are on the corresponding straight-ray portion of $\Psi$. Their chart two-jets match: at the flare the new axial direction is the signed spine tangent and the transverse acceleration is zero; at the disk the radius velocity is $-1$, axial velocity is zero, and both profile second derivatives vanish. The true positive-radius profile remains one connected embedded sphere as verified below. All maps and their material two-jets are continuous in $t$. No R781 initial metric or radius is being used on this sphere.

## One true metric row and the two curvature signs

With $k_t=\psi'(s)$ one has $\Psi_s=(1-\xi k_t)T$, $\Psi_\xi=N$, $\Psi_\zeta=e_Z$. Thus the actual central metric in $(s,\theta)$ has entries
$$
 g_{ss,t}=(1-rk_t\cos\theta)^2+(r')^2,\qquad g_{s\theta,t}=0,\qquad
 g_{\theta\theta,t}=r^2 .
$$
Use this formula at the actual $\Phi(0)=.10$ as the unique fixed target. On both straight parts and the two complete flares, skirts and caps the motion is a rigid pose and the full metric is exact. On the waist $r=.11$. There $|1-rk_0\cos\theta|\ge 1-.11(.10)/(1.4\cdot.94)$, and $r|k_t-k_0|\le .11(.55)/(1.4\cdot.94)$. With
$$
 u={.11(.55)\over 1.4(.94)-.11(.10)}<.0464
$$
the full relative spectral error is at most $2u+u^2<.096$. In particular the estimate is dimensionless and uses the real non-axisymmetric initial tensor. The waist principal curvatures, with outward normal, are $-1/r$ in the angular direction and $k_t\cos\theta/(1-rk_t\cos\theta)$ along the spine. Hence
$$
 K_t=-{k_t\cos\theta\over r(1-rk_t\cos\theta)} .
$$
Throughout $0<s<B$, $k_t$ has the same nonzero sign at all phases. The initial waist has precisely two parabolic generators, and the positive and negative open cells have the same material labels at every phase. No cone endpoint, cylinder-ruling theorem or change of sign at an initially positive point has been used to infer global feasibility.

## Normal layers on the whole shell

First $\Psi$ is injective for all $s\in\mathbb R$, $|\xi|\le.535$ and any $\zeta$. At fixed $\xi$ the world axial coordinate increases at rate $(1-\xi k_t)\cos\psi>0$, since $|k_t|\le.65/(1.4\cdot.94)<.495$ and $\cos\psi\ge\cos(.65)$. Both infinite exterior rays imply that every axial height occurs. At fixed actual axial height the world transverse $X$ coordinate increases with $\xi$ at rate $1/\cos\psi$, by eliminating $s$ between the two derivatives of $\Psi$. The third world coordinate is precisely $\zeta$. These assertions provide a common inverse spine coordinate on the whole stated strip, including extrema and the straight segments.

For $|z|<.104$, use outward signed normals. On the bent constant-radius waist the entire normal layer is
$$
 \Psi(s,(.11+z)\cos\theta,(.11+z)\sin\theta).
$$
Its inverse spine coordinate is exactly $s$. Since $.11+z>0$, two such layers never meet, including both interface circles. On either adjacent straight portion, including the flares, ordinary revolution meridian coordinates apply. The longitudinal principal curvature of a graph $r(s)$ is bounded by $|r''|\le.32(6)/.55^2<6.35$; the angular absolute curvature is at most $1/r\le1/.11$. The signed-offset meridian has the same tangent direction and positive speed factor $1\pm z\kappa$. Through the straight flare its inverse spine coordinate is strictly increasing and equals its old value at either endpoint (the endpoint derivative $r'=0$). Thus these parts have inverse coordinates outside the open interval $(0,B)$. At fixed inverse spine coordinate their transverse radius is strictly increasing with signed offset: its derivative is $1/(n\cdot e_r)>0$; the endpoints of the inverse-coordinate domain on each flare are fixed. All azimuths are genuinely present.

For the rounded edges and flat disks, the profile turn has curvature at most $1/.105<1/.104$. Its transverse radius remains $\ge .324$ on the curved portion. From a cap center up through its adjacent roll, every fixed-$z$ profile has strictly increasing transverse radius up to the central attaching rim. Its final radius is $.43+z$. The signed layers for a common transverse radius are therefore defined for an interval of $z$, and their actual axial heights are strictly ordered. At fixed transverse radius the derivative is $1/(n\cdot T)$ with the sign of that cap, by eliminating the meridional parameter. This statement is immediate on the disk and extends continuously to the single vertical end tangent. All open cap/roll layers have inverse spine coordinate strictly exterior to their attaching plane and meet a flare only at their common rim. In particular the two curved and straight pieces of a flared head have both been covered, not merely its meridional curvature bound. The disks include their regular poles. Every normal point in this argument satisfies $|\xi|\le.43+.104<.535$. The inverse-coordinate intervals at the two opposite ends are disjoint. This proves global normal injectivity and embeddedness on the connected closed sphere. For a compact $C^2$ embedded surface, if a point at distance $<.104$ had two nearest points, both would be on the constructed signed normal layers at that distance; the injectivity rules this out. Hence the reach is at least $.104$ at every phase.

## Full-image displacement and Euclidean quotient

For the initial diameter use the constant axis making angle $.05$ to the original world $Y$ direction. Every initial spine tangent is at angle at most $.05$ to that axis. The longest centerline label interval, including the caps, has length at most $2.80+2(.106)=3.012$. The diameter of the image projected onto the bisecting axis is at most $3.012+2(.43)\sin(.05)$. The diameter of its projection onto the orthogonal two-plane is at most $3.012\sin(.05)+2(.43)$. By the orthogonal decomposition their squared sum gives $D^2<3.22^2$. Thus $.104>.03D$. The right disk is fixed in world coordinates throughout; one can take for $H$ its closed strip $|X|\le.035$, including both $Z$ extremes, so that $H$ has nonempty interior and diameter at least $.648>.2D$. The remainder of this right disk is available for other proposed bending fields.

The entire initial surface satisfies
$$
 X\ge-[1.4(.10/2)+(.85+.106)\sin(.10)+.43]>-.596 .
$$
Indeed $\sin\psi\le\psi$, and the mean of the clipped profile over the bend is $.10/2$. At the terminal phase pick the true left cap point $\xi=-a_b,\ \zeta=0$. Its negative transverse displacement from the original world axis is at least
$$
 1.4(.94){1-\cos(.65)\over.65}+(.85+.105)\sin(.65)+.324\cos(.65)>1.248 .
$$
To see the first term use that the clock sends normalized length to a measure dominating $.94$ times uniform measure on $[0,1]$, by its derivative bound. The other two terms are the actual outgoing straight arm and its actual filled cap. The difference from the initial support is $>.652$. The directed distance of this one embedded point to the entire initial image is therefore $>.652>.2D$, with no material-point correspondence or sampled mesh in the inequality.

The only maximal open planar regions are the two cap interiors. The straight and flared walls have nonzero angular normal curvature, the open waist has the same nonzero angular curvature, and the actual curved head arcs have nonzero angular normal curvature at every interior point. A congruence must map the two maximal planar regions to the corresponding pair. The smaller angle between their unoriented plane normals is $.10$ at the initial phase and $.65$ at the terminal phase. The two images are consequently noncongruent. The infimum over the Euclidean group in the Hausdorff metric is positive: any sequence approaching zero would have translations bounded by compactness of both images and rotations in the compact orthogonal group, and a subsequence would realize a congruence.

This witness supplies genuine held and quotient separation for the named shape. It does not supply them for arbitrary fitted perturbations. Fields retaining the specified left cap witness and right strip do retain the same held lower bound against this unchanged initial image. The signed curvature cells and the sub-$.096$ starting error are finite inputs to a whole-surface correction, not a statement that this reference error tends to zero under resampling.


## A finite motion forced at the two physical waist ports

No exact correction can keep both outer equatorial waist-port points at the depicted final positions. This statement already holds at the relative metric tolerance in the problem, independently of reach. Fix the actual material endpoints $A=(0,0), B_1=(1.4,0)$ in $(s,\theta)$, and compare them along the true outer meridian $\theta=0$. Its initial material length is exactly
$$
 \ell_0=\int_0^{1.4}(1-.11 k_0(s))\,ds=1.4+.11(.10)=1.411.
$$
The initial metric is the R791 tensor. For any immersion at the final phase with $F^*e\preceq(1+10^{-6})g_0$, the Euclidean distance between these same two material endpoints is at most $\sqrt{1+10^{-6}}\,\ell_0<1.411001$.

At the named terminal phase let $b=.65/2=.325$. The chord from $A$ to $B_1$ is the spine chord plus $.11(N(1.4)-N(0))$. Its projection on the unit middle tangent $(\sin b,\cos b,0)$ is
$$
 \int_0^{1.4}\cos(\psi(s)-b)\,ds+2(.11)\sin b .
$$
The distribution of $\psi$ under uniform spine material dominates $.94$ times uniform measure on $[0,.65]$, as follows by changing variables on the open clock and using $P'_c\le 1/.94$. The remaining positive measure has mass $.06$. The integrand is at least $\cos b$ throughout, so the projected chord is at least
$$
 1.4\left(.94\,{\sin b\over b}+.06\cos b\right)+.22\sin b>1.442 .
$$
The final strict numerical inequality follows already from $\sin b\ge b-b^3/6$ and $\cos b\ge1-b^2/2$. Both endpoint positions cannot stay within $.015$ of the named positions, by the triangle inequality and $1.442-2(.015)>1.411001$. Thus at least one of the two actual outer equatorial waist ports must move by more than $.015$ in a correction, even at the requested finite metric tolerance. This does not rule out the stated whole-image witness or fixed right grip, which lie on different material pieces. The run54 trial fields permit three physical displacement components at each of these waist stations.
