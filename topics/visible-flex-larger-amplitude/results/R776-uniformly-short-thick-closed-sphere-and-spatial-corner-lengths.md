# R776. A globally short, thick closed shell and exact replacement of every curved corner length

The initial metric here is new. It is the metric of an inward parallel tube at a small nonzero two-lobed axial angle. A single $C^2$ family covers the complete sphere, retracts one whole head by more than $.323$, fixes the other actual head pointwise, and has reach at least $.05$ at all times. Its two endpoint images have Euclidean quotient Hausdorff distance at least $.020$. Every material tangent vector is shortened weakly relative to the one fixed initial metric. This proves the intrinsic upper bound for **every** endpoint chord, including chords with both endpoints in different caps or any individual roll. The sole metric deficit is an angular length on the curved parts of the cross-section. A second explicit spatial field restores that full prescribed angular speed and the exact two-jet joins, with two other metric coefficients recorded below.

## Initial section, axial wave and the closed sphere

Use the R772 clockwise convex rounded square $C(e)$ in the $(X,Z)$ plane, with unit-speed material $e$ modulo $P=4(.14+l)$, $l=.27\pi/2+.001$. Each of the four straight sides has length $.14$. On each connecting quarter turn the nonnegative curvature $k$ rises from $0$ to $1/r$, $r=.27$, by the quintic $S_5(s)=10s^3-15s^4+6s^5$ over $.001$, is constant in the middle and descends by reflection. Write $T=C'$ and $n$ for the outward normal, so that $n'=kT$. From the section calculation in R772 the extremal coordinate $H$ lies in $[.34,.341]$ and $C\cdot n\ge H$ at every point. To see the latter on the first half corner, with tangent turning angle $\alpha$, its support exceeds $.07\sin\alpha+H\cos\alpha+r(1-\cos\alpha)$: integrate the positive turning-angle measure $de\ge r\,d\alpha$. The result follows from $.07\sin\alpha\ge(H-r)(1-\cos\alpha)$ for $0\le\alpha\le\pi/4$ and symmetry.

For every $d<r$ used below, $C_d=C-dn$ is a regular simple convex curve, and different $d$ give strictly nested distinct curves. Indeed $C_d'=(1-dk)T$, and these shorter straight edges and four coordinate-monotone rounded arcs form a regular clockwise convex curve of total turn $2\pi$. Alternatively at any prescribed tangent direction, integration of the sine of the angle difference shows the tangent line supports the full traversal; the parameter speed is positive even on the flat portions. The normal support function is exactly $h_C(u)-d$ for every unit $u$, including each normal with a straight supporting segment. Convex support comparison implies strict nesting, and the region enclosed contains the disk of radius $H-d$ when $d<H$. Write $B(d)$ for its area.

Let $t\in[0,\pi/2]$, $x\in[0,1]$, and
$$
 Q_0=.008,\qquad Q(t)=Q_0+(1.13-Q_0)\sin^2t,\qquad q_t(x)=Q(t)\,u(x).
$$
The dimensionless clock $P_c(y)$ is zero for $y\le0$, one for $y\ge1$, and on $[0,1]$ is the integral from zero to $y$ of $S_5(\min(y,1-y)/.06)$ divided by $.94$, with the argument of $S_5$ clipped to $[0,1]$ in this speed formula. Thus $P_c(1-y)=1-P_c(y)$, its maximum speed is $1/.94$, and it starts with a positive term of degree four. Put $\ell=1/16$ and, on $[0,1/4]$, set $u(x)=P_c(x/\ell)P_c((1/4-x)/\ell)$. Extend by odd reflection about $1/4$ to $[0,1/2]$, and repeat with period $1/2$. Define
$$
 A_t(x)=.5-\int_x^1\cos q_t(s)\,ds,\qquad Z_t(x)=\int_0^x\sin q_t(s)\,ds .
$$
The negative quarter exactly unwinds the preceding positive quarter. Thus $Z_t\ge Z_0\ge0$ at every label, $Z_t(0)=Z_t(.5)=Z_t(1)=0$, and $A_t'>0$. All $q_t,q_t'$ vanish at each lobe endpoint. The two ramps in a positive quarter each have average sine at most $\sin(Q/2)$ by the reflection of $P_c$ and concavity. Consequently
$$
 0\le Z_t\le .125(\sin1.13+\sin .565)<.181,\qquad
 Z_0\le .25(.008)=.002,\qquad |q_t'|\le1.13/(.94\ell)<19.24.
$$

In the pair notation (transverse $(X,Z)$ position, axial $Y$ position), the central shell is
$$
 F_t(e,x)=(C(e)-Z_t(x)n(e),A_t(x)).
$$
At $x_*=0,1$ use the left and right end rolls ($\sigma=-1,+1$)
$$
 (C(e)-d(v)n(e), A_t(x_*)+\sigma p(v)),\quad d'=\sin\beta,\quad p'=\cos\beta,\quad p(0)=d(0)=0.
$$
The softened quarter-turn $\beta$ has length $L=.09\pi/2+.001$, with the same two $.001$ curvature ramps and maximum speed $1/.09$. Its final values are $p_b=d_b\in[.09,.091]$. At $v=L$ fill the entire plane disk enclosed by $C_{d_b}$ at $Y=A_t(x_*)+\sigma p_b$. Its polar chart uses the position $\rho C_{d_b}(e)$; the Cartesian chart is the actual $(X,Z)$ plane, including the center. Its normal collar uses $C_{d_b+w}(e)$ with the exact polar label obtained by angular inversion and radial ratio. The positive support of $C_{d_b}$ makes its angular map strictly monotone with a unique inverse. These are the two complete disk charts and collar on each side, the two rolls, and the central chart. On the central side of a roll join $Z=Z'=Z''=0$, $A'=1$, $A''=0$; the roll has the same physical two-jet in the respective signed axial material direction, and both mixed derivatives vanish. At $v=L$ the roll velocity is $-n$, with zero meridian acceleration, and its mixed derivative is $-kT$, exactly the physical derivatives of the normal collar on the flat cap. All formulas are $C^2$ jointly in phase and materials. Horizontal slices are successive simple convex section curves, with strictly increasing axial coordinates in the central material and strictly outward axial coordinates up to the terminal planes on both ends. This gives a closed embedded sphere with the indicated cap centers.

## Uniformly short in the complete fixed metric

The central physical derivatives are $F_e=(1-kZ_t)T$ and $F_x=-\sin q_t\,n+\cos q_t\,e_Y$. They are orthogonal and $|F_x|=1$. Therefore the one fixed target on the central material and its present metric are
$$
 g_0=dx^2+(1-kZ_0)^2\,de^2,\qquad g_t=dx^2+(1-kZ_t)^2\,de^2 .
$$
The coefficient $1-kZ_t$ is at least $1-.181/.27>.32$. On both entire rolls and cap disks only a rigid translation applies. This proves $0<g_t\preceq g_0$ everywhere, including both poles in Cartesian coordinates. For any two material points $p,q$ and any rectifiable connecting path $\gamma$ in this sphere,
$$
 |F_t(p)-F_t(q)|\le \operatorname{length}_{g_t}(\gamma)
 \le\operatorname{length}_{g_0}(\gamma).
$$
Taking the infimum treats every pair at once. All three coefficients agree exactly on every straight-transverse-edge band, both complete rolls and both full disks. In particular take each of the two developed disks specified in R772 by the whole axial straight segment $Z=\pm H$, its two end rolls, and its extension $.06\le\pm Z\le H-d_b$ on the true caps: the same material sets are exactly isometric to this new initial metric. An open part of each curved corner strictly loses transverse speed at positive phase. The metric differs from R772 even at phase zero: its central mixed row vanishes identically and its curvature enters a nonconstant transverse scale.

## Every signed normal layer, including mixed chart pairs

Write the signed normal parameter as $z$, $|z|<.05$. In the middle the actual outward unit normal is $(\cos q\,n,\sin q)$, so write the parallel surface as $(C-Dn,Y)$ with
$$
 D=Z_t-z\cos q,\qquad Y=A_t+z\sin q,\qquad
 Y_x=\cos q(1+zq')>0 .
$$
For each fixed $z$ its axial range is precisely $[A_t(0),A_t(1)]$. At each fixed interior axial height and varying $z$, implicit differentiation gives $x_z=-\tan q/(1+zq')$ and
$$
 \left.\partial_zD\right|_Y=-\cos q+\sin q(1+zq')x_z=-1/\cos q<0 .
$$
The same formula extends one-sided to the endpoints. The effective offset lies in $(-.05,.231)$, so all cross-sections are regular simple nested curves. This proves both within-layer and between-layer injectivity on the central portion, for arbitrary angular labels.

On either end use the outward axial distance $y=\sigma(Y-A_t(x_*))$. The corresponding layer has
$$
 y=p(v)+z\sin\beta(v),\qquad D=d(v)-z\cos\beta(v).
$$
Here $y_v=\cos\beta(1+z\beta')>0$ up to the terminal rim, with range $0\le y\le p_b+z$, and $D_v=\sin\beta(1+z\beta')\ge0$. On $0<v<L$ one has $D<d_b$ from the strictly increasing final part, and $D>-.05$. For fixed $y$ the admissible $z$ form an interval cut out by $p_b+z\ge y$. In its relative interior the same calculation gives $\partial_zD|_y=-1/\cos\beta<0$. At the terminal rim, $D=d_b$ by continuity. Thus all open-roll layers on this head are separated for equal physical $Y$, and at all other $Y$ disjointness is automatic. Every layer of its terminal disk is the full region bounded by $C_{d_b}$ at $y=p_b+z$. Distinct such disk layers occupy distinct planes. If an open-roll point from a different $z$ is on such a plane, then $D<d_b$ places it strictly outside that planar disk, by convex nesting. Central/roll components can touch only at their common initial rim $y=0$ where $D=-z$; distinct layers there are again distinct curves. The two opposite heads are separated by the positive central axial span; both terminal ranges $p_b+z$ are positive. These cases exhaust all normal offsets, including seam points and both poles.

In the middle the shape operator has principal curvature magnitudes $|q'|$ and $k\cos q/(1-k Z_t)$, bounded by $\max(19.24,1/(.27-.181))<20$. The roll curvature magnitudes are bounded by $1/.09$ and $1/(.27-.091)$, and the planes have curvature zero. The normal map is thus regular and injective on $|z|<.05$. A nearest point to a compact $C^2$ surface has normal displacement, so uniqueness throughout this tube proves $\operatorname{reach}F_t\ge.05$.

## Whole-image held, fixed grip, and the rigid-motion quotient

At every phase the transverse coordinate ranges are at most $2H\le.682$ in each axis, and the full axial range is at most $1+2p_b\le1.182$. Thus $D=\operatorname{diam}F_0<1.55$ and the same upper bound holds for every image. The right entire fixed head contains the full seam curve of diameter at least $2H\ge.68$; a closed full-dimensional material patch containing this curve and part of the roll also works as the grip. At $t=\pi/2$ set $\Delta=A_t(0)-A_0(0)$. On half of the whole material $|q_t|=1.13$, and another quarter of the whole material has $|q_t|\ge.565$. Since $\cos q_0\ge1-.008^2/2$,
$$
 \Delta\ge\tfrac12(1-\cos1.13)+\tfrac14(1-\cos .565)-.008^2/2>.323.
$$
(The comparison numbers follow, for example, from the alternating Taylor bounds through terms of degree eight.) The initial leftmost head point is at axial distance at least $\Delta$ from all final image points. This gives whole-image held $>.323>.2D$. Also $.05>.03D$.

The two head volumes are individually fixed. The middle enclosed volume is $\int B(Z_t)\cos q_t\,dx$. At every label $B(Z_t)\le B(Z_0)$ and $\cos q_t\le\cos q_0$, while $B(Z_0)\ge\pi(.338)^2>.358$. Thus the initial volume exceeds the final one by at least $.358\Delta>.115$. The final surface has area at most $P+2PL+2(2H)^2<3.85$. If a Euclidean isometry, including a reflection, placed the initial boundary within Hausdorff distance $d<.020$ of the final one, the transformed enclosed solid would fit in the final solid and its outward $d$-tube. Indeed the exterior of that parallel sphere is connected to infinity and avoids the transformed boundary. The volume gain is at most $3.85d[1+20d+(20d)^2/3]<.113$, by integration of the signed layer Jacobian. This contradicts the volume difference. Hence the quotient distance for the specified endpoints is at least $.020$.

## Global angular speed correction on the identical target

On each actual corner write $s\in[0,l]$ for its material, $\alpha(s)$ for its turning angle, $a_i=1-kZ_i$ for $i=0,t$ and introduce the same smooth odd pulse $b$. On $z=s/l\in[0,1/2]$ let
$$
 b=S_7(z/.025)\,S_7((.5-z)/.025),\qquad
 S_7(u)=35u^4-84u^5+70u^6-20u^7
$$
with clipped arguments, and extend by $b(1-z)=-b(z)$. It is $\pm1$ on $.9$ of the length. Replace the tangent of the corner by the following genuinely spatial tangent, integrated starting at the **same** short-field initial endpoint in the appropriate oriented world quadrant:
$$
 V(s)=a_0[\cos(\gamma b(s))T(s)+\sin(\gamma b(s))e_Y].
$$
The scalar $\gamma$ is chosen from $[0,\pi/2)$ by
$$
 \int_0^l a_0[1-\cos(\gamma b)]\cos(\alpha-\pi/4)\,ds
 =\sqrt2\,(Z_t-Z_0).
$$
Indeed $\int k\cos(\alpha-\pi/4)\,ds=\sqrt2$. The actual $Y$ increment is zero by odd reflection. The planar component perpendicular to the chord cancels by corner symmetry. The remaining planar component matches exactly the prescribed chord $\int_0^l a_t T\,ds$ by this equation. At $\gamma=0$ the uncorrected angular chord component is at least the requested one; at $\pi/2$ it is at most $.1l$, smaller than the target component $(1-.181/.27)l/\sqrt2$. Strict monotonicity after zero and the positive $a_0$ give a unique root. When $Z_t>Z_0$ its transverse tangent has nonzero $Y$ component on an open subset; outside the corner all straight bands and both complete caps keep the physical short field. The exact corner endpoints prove consistent global ring closure, including the last-to-first corner.

For joint regularity put $G=\gamma^2$ and factor the root equation as $G M(G,Z_0)=\sqrt2\,(Z_t-Z_0)$ where $M$ is analytic in $G$ and smooth in $Z_0$; at zero its integral has the factor $b^2/2$ with strictly positive weighted integral. For $0<G\le(\pi/2)^2$ also $\partial_G(GM)>0$. Consequently $\gamma=\sqrt{Z_t-Z_0}$ times a strictly positive smooth function of $Z_t-Z_0,Z_0$ on this compact range. In a lobe $\Delta Z=Z_t-Z_0$ is $\Delta Q=Q(t)-Q_0$ times the integral from the nearest lobe endpoint to its folded positive-quarter label of the smooth positive integrand $u\int_0^1\cos((Q_0+\tau\Delta Q)u)d\tau$. Near an axial lobe endpoint that integral has the form $|x-x_*|^5$ times a positive smooth one-sided function, by the degree-four start of $P_c$. Its square root, with derivatives through order two, extends by zero through all three axial lobe endpoints. Also $\sqrt{\Delta Q}=\sqrt{1.13-Q_0}\sin t$ on the given phase interval. This gives the full continuous two-jet, including the joint initial-phase and lobe-edge limits.

At every corner endpoint $k=k'=b=b'=0$. The terminal and initial angular tangents and their first angular derivatives match the old ones; longitudinal and mixed derivatives match by equality of the endpoint curves for all $x$ and of their first angular tangents. The closed spatial field therefore has the full physical two-jet at every flat/curved join. The vanishing of $\gamma,\gamma_x,\gamma_{xx}$ at the lobe ends also gives both original roll two-jets. It follows that the entire angular coefficient is now the exact fixed $a_0^2$ on every corner and every straight band, and all three coefficients remain exact on the two whole caps, two rolls and all four flat bands. The remaining physical coefficients can be evaluated without inference: write $H(s,x)=\int_0^s[V(\sigma,x)-a_t(\sigma,x)T(\sigma)]d\sigma$. In the global physical coordinates the corner sheet is $F_t+H$, its angular tangent is $V$, and its longitudinal tangent is $F_{t,x}+H_x$. Its mixed and longitudinal coefficients are $V\cdot(F_{t,x}+H_x)$ and $|F_{t,x}+H_x|^2$. No shortening, reach, injectivity or fixed-metric conclusion for this companion follows from the corresponding certificate for the short reference.

The companion source scripts/resume_20261126/r776_short_inward_tube_and_spatial_corners.py returns $(F,F_e,F_v,F_{ee},F_{ev},F_{vv})$ in world coordinates on all nine charts, using v=x-.5 centrally. The two branch names are short and arclength. In working arithmetic it uses split Gauss quadrature, 52 positive scalar bisections on the regular unknown $G/(Z_t-Z_0)$, the first 16 nonzero cosine coefficients for the scalar integral, and analytic implicit derivatives. These are numerical realizations of the exact definitions above. The phase-zero fixed source is the same for both branches.