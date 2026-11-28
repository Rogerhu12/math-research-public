# R781. A circular three-lobe shell, a thick finite metric improvement, and freely closing spatial rings

Use a new material sphere and one new initial metric throughout. The complete circular shell has a pointwise fixed right head, an axial endpoint held distance $>.320$, and a Euclidean-quotient endpoint separation $>.096$. Its initial diameter satisfies $D<1.362$. A continuum of finite physical references, including a six-percent radial correction, has reach $\ge1/24.45>.03D$ at every phase. The correction strictly improves the global relative Gram error by more than $.013$ while preserving those separations. A further two- or three-fold spatial ring construction restores the full fixed angular speed with no prescribed short cell endpoints. It pays all three metric rows and has absolute principal curvature $<9.1$ on all three complete circles where the original worst angular deficit occurs. Its moving-ring mixed/longitudinal terms elsewhere and the global thickness of this latter spatial field are separate costs.

## Exact initial material and all joins

Take transverse radius $R=.45$, arclength $e$ modulo $P=2\pi R$, angle $\theta=e/R$, transverse vectors $n=(\cos\theta,\sin\theta)$, $T=(-\sin\theta,\cos\theta)$. The world axis is $Y$, and transverse coordinates are $(X,Z)$. The central material $x=v+.5$ runs from $0$ to $1$. Use the integrated clipped R776 clock $P_c$ with smoothing fraction $.06$, strictly increasing from zero to one on the unit interval, symmetric under $P_c(1-u)=1-P_c(u)$, with $0\le P_c'\le1/.94$. Its derivative is the clipped $S_5(\min(u,1-u)/.06)/.94$, and both constant extensions are included. Set $b=1/6$, $\ell=.073$. On $[0,b]$ let $w(x)=P_c(x/\ell)P_c((b-x)/\ell)$, extend by negative reflection across $b$ to $[0,2b]$, and repeat with period $2b$. For $t\in[0,\pi/2]$ put
$$
 Q=.60+.90\sin^2 t,\quad q=Qw,\quad q_0=.60w,\qquad
 A(x)=.5-\int_x^1\cos q,\quad Z(x)=\int_0^x\sin q,\quad
 Z_0(x)=\int_0^x\sin q_0,\quad\delta=Z-Z_0.
$$
Both $Z$ and $\delta$ are zero at $x=0,1/3,2/3,1$; they increase on each folded positive half and return symmetrically. For one scalar $0\le\xi\le.06$, define $z=Z-\xi\delta$, $r=R-z$, $r_0=R-Z_0$. The actual middle field is $(r n,A)$. The values $q,q',z,z',z''$ vanish at the two end rims. Thus the meridian velocity there is $e_Y$ and its acceleration zero; the transverse radius is the full $R$.

At either end $x_*\in\{0,1\}$, $\sigma=-1,+1$, attach the full rounded annulus $((R-d)n,A(x_*)+\sigma p)$ in the true roll arclength, $p'=\cos\beta$, $d'=\sin\beta$, $p(0)=d(0)=0$. The length is $L=h\pi/2+\eta$ with $h=.09,\eta=.001$, and $\beta'$ ramps by $S_5$ to $1/h$ over $\eta$, stays constant, then ramps down over $\eta$. Write $p_b=d_b\in[.09,.091]$ for its terminal coordinates. Both complete disks have radius $R-d_b$ and constant $Y=A(x_*)+\sigma p_b$. Use on each the polar chart $\rho(R-d_b)n$, the Cartesian chart $(X,Z)$ including the pole, and the normal collar $(R-d_b-u)n$ whose polar material coordinates are exactly $(e,1-u/(R-d_b))$. At the initial roll edge the first meridian derivative is $\sigma e_Y$ with zero second and mixed derivatives; at the disk it is $-n$ with zero second derivative and mixed derivative $-T/R$. These equal the signed central and true disk-normal physical two-jets. All nine charts therefore define a jointly $C^2$ closed sphere. Each fixed axial slice of the middle or open roll is just one positive-radius circle; the middle height is strictly increasing and the two open rolls are in disjoint exterior axial intervals. Both terminal planes are distinct and each disk is filled once. This proves global embeddedness including both poles.

## Finite-amplitude bounds and the one frozen metric

In each positive half there is a constant plateau of length $b-2\ell$, hence the total plateau fraction is $p_*=1-12\ell=.124$. Each ramp clock pushes the uniform measure forward to a probability measure dominating $.94$ times the uniform measure on $[0,1]$ by its derivative bound. Its remaining mass is $.06$. Concavity and the reflected mean $1/2$ give
$$
 Z\le(b-2\ell)\sin1.50+2\ell\sin .75<.121,\quad
 Z_0\le(b-2\ell)\sin .60+2\ell\sin .30<.055 .
$$
At a positive-half summit $Z_0\ge(b-\ell)\sin .60>.0528$, by concavity. At the last phase the integrand $f(u)=\sin(1.50u)-\sin(.60u)$ is nonnegative, increasing in the parameter $Q$ in its first term, and concave on $0\le u\le1$ (its second derivative is nonpositive). Every $\delta$ is therefore bounded above by $(b-2\ell)f(1)+2\ell f(.5)<.0654$. At the terminal summit its lower bound is
$$
 (b-2\ell)f(1)+2\ell(.94)\{(1-\cos1.50)/1.50-(1-\cos .60)/.60\}>.0539 .
$$
These estimates and the monotonicity of both $\delta$ and $Z_0$ toward the summit yield
$$
 .135< d_*:=\max_{x,t}\delta/(R-Z_0)<.166 .
$$
All three identical summit rings at $x=1/6,1/2,5/6$ attain this maximum at terminal phase. The axial contraction between initial and final fields satisfies
$$
 \Delta=A_{\rm final}(0)-A_0(0)\ge
 p_*(\cos .60-\cos1.50)+(1-p_*)(.94)
 \left(\frac{\sin .60}{.60}-\frac{\sin1.50}{1.50}\right)>.320 .
$$
Here the expression on the two ramps is nonnegative; discarding only their nonnegative residual measure gives the lower bound. All decimal comparisons above may for example be checked with alternating sine/cosine bounds through degree twelve.

The complete fixed central $g_0$ is $dx^2+(r_0/R)^2de^2$. On both whole rolls and disks the initial metric is always exactly paid by the prescribed rigid poses. On the central field let $s_\xi=(1-\xi)\sin q+\xi\sin q_0$. Then $F_x=(-s_\xi n,\cos q)$, $F_e=(r/R)T$. The mixed coefficient vanishes identically. The two relative diagonal metric entries are
$$
 1-[\sin^2q-s_\xi^2],\qquad [1-(1-\xi)\delta/r_0]^2.
$$
Since $\sin(.60|w|)/\sin(Q|w|)\ge.60/Q\ge.4$ by concavity, $|s_\xi|\ge(1-.6\xi)|\sin q|$ and both coefficients are in $(0,1]$. The sphere is globally weakly short, for every $\xi$ here and all $t$. In particular every material chord is at most its intrinsic initial distance. The longitudinal deficit is at most $1-(1-.6\xi)^2\le .072$, strictly smaller than the maximum angular deficit for these $\xi$ since $d_*>.135$. Thus the global worst relative spectral error is exactly
$$
 M_\xi=1-[1-(1-\xi)d_*]^2 .
$$
It is $<.305$ even at $\xi=0$. At $\xi=.06$ it is less than $M_0-.013$, since $M_0-M_\xi=2\xi d_*(1-d_*)+\xi^2d_*^2$. No phase-dependent target, mesh change, or diverging material frequency enters this comparison.

## Exact diameters, held and the Euclidean quotient

Write $S=\int_0^1\cos q\,dx$. The surface is centrally symmetric about its axial midpoint since $w(1-x)=-w(x)$ and $z(1-x)=z(x)$. Its diameter is twice the largest radial distance to that center. In the middle radius is at most $R$ and the axial half-span at most $S/2$, both attained together at a rim. Thus the middle maximum is its rim radius. On each adjoining fillet, use axial and transverse radial coordinates $(S/2+p,R-d)$. Put $\beta_1=\eta/(2h)$ and
$$
 Y_c=S/2+p(\eta)-h\sin\beta_1,\qquad b_c=R-d(\eta)-h\cos\beta_1 .
$$
On the constant-curvature part of that actual fillet the point is exactly $(Y_c,b_c)+h(\sin\beta,\cos\beta)$. The vector $(Y_c,b_c)$ has positive components and its corresponding angle $\arctan(Y_c/b_c)$ lies strictly between $\beta_1$ and $\pi/2-\beta_1$: one can use $.55<S<1$, $0\le p(\eta)-h\sin\beta_1\le\eta$ from $ds\ge h\,d\beta$, and $.359<b_c<.361$. The norm derivative has the sign of $(S/2+p)\cos\beta-(R-d)\sin\beta$, positive on the initial small ramp and negative on the terminal ramp by those same bounds. The planar terminal disk reaches its maximum at the rim and none of its interior exceeds it. Hence, for every $\xi,t$,
$$
 D(t)=2\{h+\sqrt{Y_c^2+b_c^2}\}.                                             \tag{1}
$$
For the initial $S_0$ the clock measure estimate gives
$$
 S_0\le .124\cos .60+.876(.94\operatorname{sinc} .60+.06)<.932.
$$
For any phase the same measure gives $S\ge .124\cos1.5+.876(.94\operatorname{sinc}1.5+.06\cos1.5)>.55$. Thus $D=D(0)<1.362$. The derivative of (1) with respect to $S$ is $Y_c/\sqrt{Y_c^2+b_c^2}>.60$ on this interval. In particular $D(0)-D(\pi/2)>.60\Delta>.192$. Diameter is unchanged by all Euclidean motions and changes by at most twice Hausdorff distance. This establishes the full Euclidean-quotient distance $>.096$ for this family, irrespective of possible reflections. The original leftmost point lies at distance at least $\Delta>.320$ from all final points by their axial coordinates. The complete right head is fixed, including its $2R=.90$-diameter rim, so the fixed grip and whole-image held both exceed $.2D$.

## All signed tubular layers for the balanced fields

In the center set $v_\xi=\sqrt{\cos^2q+s_\xi^2}\ge1-.6\xi\ge.964$ and let $\psi$ be the signed meridian angle having sine $s_\xi/v_\xi$, cosine $\cos q/v_\xi>0$. Its arclength curvature is
$$
 K_m=\frac{q'[(1-\xi)+\xi((.60/Q)\cos q\cos q_0+\sin q\sin q_0)]}{v_\xi^3}.
$$
The bracket has absolute value at most one using the unit circle and $.60/Q\le1$. Hence $|K_m|\le1.50/(.94\,\ell\,.964^3)<24.45$. The other curvature has magnitude at most $1/(R-.121)<3.05$. The roll curvature bounds are $1/h$ and $1/(R-d_b)$, its planar disk has both zero.

For signed normal distance $|\tau|<1/24.45$, a central layer point has axial coordinate $Y=A+\tau\sin\psi$ and radial coordinate $R-z+\tau\cos\psi$. Its $Y_x$ is $v_\xi\cos\psi(1+\tau K_m)>0$, with the same endpoint axial heights on all layers. At fixed physical $Y$, differentiating its effective debit $z-\tau\cos\psi$ gives $-1/\cos\psi<0$. All radii stay positive. Thus two labels in any central layer and two distinct central layers cannot collide. On a roll use outward axial distance $y=p+\tau\sin\beta$, which increases strictly from zero to $p_b+\tau$, and radial debit $d-\tau\cos\beta$. For each fixed $y$ the admissible $\tau$ form an interval, and in its roll interior the same derivative is $-1/\cos\beta<0$. The debit increases to $d_b$ with meridian derivative $\sin\beta(1+\tau\beta')$, and is strictly smaller for each open roll point. Thus for every layer its open-roll projection is strictly exterior to the entire terminal disk in its transverse plane. The parallel disk layers themselves occupy distinct axial planes. Rolls meet the central layer only at their genuine corresponding rim, where distinct parallel radii are $R+\tau$. Opposite heads cannot meet across the strictly positive intervening axial span; $p_b+\tau>0$. This accounts for all different charts, different phases of the angular label within the same physical slice, and different parallel layers at a fixed time. The regular normal map is globally injective for the stated range, proving $\operatorname{reach}F_t\ge1/24.45>.03D$ even at the chosen finite $\xi=.06$ metric improvement.

## Whole spatial rings with free cell endpoints

Fix $\xi\in[0,.06]$ and $m=2$ or $3$. In the moving central orthonormal frame let $N=(\cos\psi\,n,\sin\psi)$ denote the balanced outer normal. Let $g=\gamma^2$ be defined by the positive root
$$
 1-\langle\cos(\sqrt g\sin u)\rangle=(1-\xi)\delta/r_0
$$
where brackets are the period average. The derivative with respect to $g$ is positive while $\gamma<\pi/2$ and has limit $1/4$ at zero. The even Taylor bound $\langle\cos(\gamma\sin u)\rangle\le1-\gamma^2/4+\gamma^4/64$ at $\gamma=.86$ is less than $1-.166$. This gives the unique $\gamma<.86$. As in R776, $\gamma$ is $\sqrt{\delta}$ times a smooth strictly positive function; $\delta/(Q-Q_0)$ starts at each of $0,1/3,2/3,1$ as the fifth power of the material distance times a positive one-sided smooth factor, by the clock's degree-four start. The factor $\sqrt{Q-Q_0}=\sqrt{.90}\sin t$ and this $5/2$ spatial exponent give full continuous two-jets and zero first and second axial derivatives of the corrections at those seams.

Set $\chi=\gamma\sin(m\theta)$ and prescribe the actual angular derivative
$$
 V=r_0(\cos\chi\, T+\sin\chi\,N).
$$
Its transverse part in complex notation is $r_0 e^{i\theta}(i\cos\chi+\cos\psi\,\sin\chi)$. Each factor after $e^{i\theta}$ has period $2\pi/m$. Its full-ring mean vanishes because the $m$ rotations sum to zero. Its axial mean is zero by the sine reflection. Choose the unique transverse primitive of mean zero. Equivalently integrate from $0$ to $2\pi/m$ and choose the starting point by solving $(R_{2\pi/m}-I)P(0)=\int_0^{2\pi/m}V_\perp$; the remaining sectors follow by rotation. No cell endpoint in the true interior of a ring is pinned to a short-field point. The first harmonic from the mean cosine is the balanced radius $r n$.

For its axial coordinate, let $J(\theta)=\int_0^\theta\sin(\gamma\sin(mv))dv$ with periodic continuation, and set $b_m=J(\pi/m)/2$. Then $0\le J\le2b_m$. Choose
$$
 Y=A+r_0\{b_m+\sin\psi\,[J(\theta)-b_m]\}.
$$
This compensating constant is an actual physical choice. Its axial correction is nonnegative, so all angular labels remain above the true leftmost terminal plane, including at full swing. Fill both entire end rolls and disks by their previous exact poses. The vanishing two-jets of the correction at both axial ends prove the complete nine-chart $C^2$ joins. The first angular speed is precisely $|V|=r_0$ and $V\cdot F_{t,x}=0$ for the **balanced** meridian $F_t$. The actual spatial meridian velocity includes the $x$ derivative of the full-ring primitive and the axial compensating constant. Its tilt, norm and mixed coefficient are fees on the real changed field.

Every spatial ring has a simple regular horizontal projection. Indeed, relative to $r_0 T$ the projected angular derivative changes by at most $r_0|\gamma\sin(m\theta)|$. For two labels take the shorter angular interval of length $a\in(0,\pi]$. The reference horizontal chord length is $2r_0\sin(a/2)$. For $a\le\pi/2$ its ratio to $r_0 a$ is at least $2\sqrt2/\pi>.90>.86$. For the remaining intervals,
$$
 \int_I|\sin m\theta|\,d\theta\le 2a/\pi+.5/m.
$$
For example the primitive of $|\sin u|-2/\pi$ on $[0,\pi]$ is $1-\cos u-2u/\pi$, whose two extrema are at $\sin u=2/\pi$ and whose range is less than $.5$. If $\pi/2\le a\le2.5$, the error ratio is at most $.86(2/\pi+.25/(\pi/2))<.685$, below $\operatorname{sinc}(1.25)>.75$. For $2.5\le a\le\pi$ it is at most $.86(2/\pi+.25/2.5)<.634<2/\pi$. Thus no two different labels of this same ring coincide in projection. Its transverse velocity is also nonzero since $\cos\chi>\cos .86$.

At the three positive-half summits $q=q'=0$, $Z'=Z_0'=\delta'=0$, and their second derivatives are zero too. The clock at these sign changes starts at order four, so also $q''=0$. The actual full spatial curve on each such ring is planar; the axial primitive offset may be nonzero but is independent of $\theta$. Its actual longitudinal derivatives there are $F_x=e_Y$, $F_{xx}=0$, $F_{x\theta}=0$. All three fixed Gram rows therefore hold pointwise on each of these complete originally worst rings. Their only possibly nonzero principal curvature has magnitude $|1-m\gamma\cos(m\theta)|/r_0\le(1+3(.86))/.395<9.1$. The per-ring injectivity does not by itself exclude collisions between distinct axial levels, and does not propagate the summit estimate to all phases and pairs. The full spatial field, any finite fraction blended with the balanced one, and its fitted perturbations require their own global geometry checks. The proved area, reach and diameter formulas for the circular balanced shell have not been transferred to the spatial swings.

The complete physical positions and five derivatives on the real nine charts are implemented in scripts/resume_20261126/r781_round_three_lobe_spatial_rings.py. Its short and balanced branches implement the integral fields directly, with the same true initial metric. The ring branch evaluates the mean-zero transverse primitive through the real Fourier/Bessel expansion of $\exp(i\gamma\sin(m\theta))$, retaining indices through 16 in working arithmetic, with split axial quadrature, 48 brackets for $g/((1-\xi)\delta/r_0)$, and analytic implicit differentiation. The exact comparison (1) is also available as diameter(t,order). No finite sample has been substituted for any of the global bounds above.