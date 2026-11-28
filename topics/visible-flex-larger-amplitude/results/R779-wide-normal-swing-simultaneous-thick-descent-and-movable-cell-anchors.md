# R779. A single wide normal swing, exact corner chords, and an angular correction that preserves quantitative reach

This uses the one fixed R776 initial metric, its exact short field $F_t$, its full material sphere, and its phases $0\le t\le\pi/2$. There are two positive conclusions. A single signed normal swing on each actual full corner pays the fixed angular coefficient and all its endpoint conditions, and its new angular tangent remains orthogonal to the original short axial tangent. A specific nonzero fraction of that swing gives an embedded family whose worst all-material, all-phase relative spectral metric error is strictly smaller than that of $F_t$, while retaining reach $>.03D$ at **every** phase and both macroscopic endpoint separations. This is a finite deformation on the same fixed target. The guaranteed decrease from the short field is small and leaves a large metric error.

## A scalar full-chord equation in the true short-field normal plane

Use R776's transverse unit tangent $T$, outward section normal $n$, short unit shell normal $N=(\cos q\,n,\sin q)$ and short axial unit tangent $U=(-\sin q\,n,\cos q)$. World coordinates here are grouped as (the transverse plane, the axial coordinate). On a true curved quarter with arclength $s\in[0,l]$, $l=.27\pi/2+.001$, write $\beta(s)$ for its turning angle, $a_0=1-k Z_0$, $a_t=1-kZ_t$, $\delta=Z_t-Z_0$, and $c=\cos q_t$. Use a broad odd pulse. For $u=s/l$ in $[0,.5]$ set
$$
 b(u)=P_c(u/.10)P_c((.5-u)/.10),\qquad b(1-u)=-b(u).
$$
Here $P_c$ is the exact R776 integrated $.06$ clock, including constant extensions. Each of the four transitions has width $.10l$ and $|b_s|<25.1$. Write $\omega=\beta-\pi/4$. Select $\gamma\in[0,\pi/2)$ by the equation
$$
 E(\gamma)=\int_0^l a_0\{[1-\cos(\gamma b)]\cos\omega
             -c\sin(\gamma b)\sin\omega\}\,ds=\sqrt2\,\delta.                 \tag{1}
$$
Use the spatial corner velocity
$$
 V=a_0\{\cos(\gamma b)T+\sin(\gamma b)N\},\qquad
 H(s,x,t)=\int_0^s(V-a_tT)\,ds',\qquad F^{w}=F_t+H.                         \tag{2}
$$
Extend $H=0$ to the straight bands, complete end rolls and cap disks. The scalar projection of $n$ onto the corner chord unit direction is $\sin\omega$. Reflection in the chord direction in the section plane sends $T(s)$ to $T(l-s)$ and $n(s)$ to $-n(l-s)$. The resulting planar transverse components perpendicular to the chord cancel, as does the axial increment from $a_0\sin(\gamma b)\sin q$. Since $\int k\cos\omega\,ds=\sqrt2$, equation (1) makes the remaining full-chord component exact. Thus every corner starts and ends at the **actual** short-field material endpoints.

For $0\le\gamma\le\pi/2$ both terms of $E'(\gamma)$ are nonnegative by the signs of $b$ and $\sin\omega$. The derivative is positive even at zero because $c\ge\cos1.13>.426$ and the second term is positive on a subarc. At the upper limit the projected planar chord component is at most $.40 l/\sqrt2$: its normal contribution has nonpositive sign; the cosine contribution on each transition has mean at most $\cos(\pi/4)$ by concavity and the clock's symmetric mean. The requested chord component is at least $(1-.181/.27)\,.27\sqrt2>.40l/\sqrt2$, since $ds\ge.27\,d\beta$. This establishes one unique root of (1), including zero where $\delta=0$. For $\gamma\le\pi/3$ restrict the second term of $E'$ to $s/l\in[.10,.20]$ and its reflection, where $|b|=1$, $|\sin\omega|>.44$, $a_0>.992$ and $\cos(\gamma b)\ge.5$. For $\gamma\ge\pi/3$ the first term alone on the $.60l$ total plateau exceeds $.60l(.992)\sin(\pi/3)/\sqrt2$. In particular $E'>.007$ uniformly. Smooth implicit differentiation gives $\gamma=\delta$ times a smooth positive factor in $Z_0,\delta,c$. It has no square-root singularity at either axial lobe edge. At the edges $k=k'=b=b'=0$. The first and second angular derivatives match the adjacent flat; the actual endpoint identities for all $x$ give the matching longitudinal derivatives, and first angular identities give the mixed ones. At the axial joins $\delta=\delta_x=\delta_{xx}=0$, so the original full physical two-jets persist there and on all cap transitions. The resulting sphere map is jointly $C^2$ for all phases.

On each corner $(F^w)_e=V$ has length $a_0$ and $V\cdot U=0$ exactly. The true remaining coefficients are $V\cdot H_x$ and $|U+H_x|^2$. On the two full axial station rings $x=.25,.75$ we have $q=q'=Z_0'=\delta'=0$, so $H_x=0$ and all three rows agree there as well as on the complete straight bands, rolls and terminal disks. For the unscaled wide swing embeddedness and quantitative reach are separate questions. All fractions $F^\lambda=F_t+\lambda H$ with $0\le\lambda\le1$ retain the two exact rigid head poses. They also retain the whole-image extreme: $\int_0^s a_0\sin(\gamma b)ds'$ is nonnegative and at most $l/2$. The axial correction is this integral times $\sin q$, hence can be negative only for $x\ge.25$, where $A_t(x)-A_t(0)+p_b\ge.25\cos1.13+.09>.196$. Its absolute magnitude is at most $.5l\sin1.13<.193$. The retracted left disk still realizes the minimum physical axial coordinate. This gives held $>.323$ across the endpoint phases and the unchanged right grip has diameter $\ge.68$.

## A quantified simultaneous improvement at one finite amplitude

Write $d=k\delta/a_0$, $d_x^{\max}=(\delta/.27)/(1-Z_0/.27)$ (the superscript denotes a maximum over the transverse material, **not** differentiation), and $d_*=\max_{x,t}d_x^{\max}$. The initial short-field worst relative spectral deficit is $M_*=1-(1-d_*)^2$. At fixed phase both $\delta$ and $Z_0$ increase up to the peak of a folded positive quarter. For fixed axial label $\delta$ is largest at the last phase. Thus the maximum occurs at the terminal phase and $x=.25,.75$, and $d_*>.62$ by the last-section bounds $Z_1>.1729$, $Z_0\le.0015$. In every chart $d_*<.68$.

Call a point near this maximum if $d>d_*-.003$. Then its $c>.90$. In fact, if $c\le.90$, the remaining positive-quarter rise of $\delta$ up to its axial maximum at that phase is at least
$$
 (1-\cos |q|-.008|q|)/19.24 > .0047 .
$$
To see this, use the descending copy of each value $0\le z\le |q|$ on the remaining part of the folded positive quarter. The integrand $\sin z-\sin(Q_0 z/Q)$ is nonnegative and its arclength weight is at least $dz/19.24$. On the reflected half use its identical folded value. This would lower $d_x^{\max}$ relative to its peak by more than $.0047/.27>.017$. Also $d_x^{\max}-d<.003$ at every near point.

Put $\gamma_*=\arccos(1-d_x^{\max})$. We estimate the actual root strictly below this angle at the near points. The complete quarter satisfies
$$
 l^{-1}\int |b|\,|\sin\omega|\,ds>.285.
$$
Indeed the integral without $|b|$ is at least $2(.27)(1-1/\sqrt2)$. On the two outer transitions the deficit is at most $.10l/\sqrt2$ by the average of $1-|b|$. On the two transitions adjacent to the midpoint it is at most $.10l(.158)$ since $|\omega|\le.10l/.27<.158$. Also $\int(1-b^2)\cos\omega\,ds\le .30l$ because the mean of $b^2$ on each of the four transitions is at least $1/4$. The inequalities $1-\cos(\gamma_* b)\ge b^2(1-\cos\gamma_*)$, $|\sin(\gamma_* b)|\ge |b|\sin\gamma_*$, and $a_0d_x^{\max}\ge k\delta$ now give
$$
 E(\gamma_*)-\sqrt2\delta\ \ge\
 l\{(.90)(.992)(.285)\sin\gamma_*-.30d_x^{\max}\}
 >.05 l\,d_x^{\max}.
$$
Here $\sin\gamma_*/d_x^{\max}=\sqrt{(2-d_x^{\max})/d_x^{\max}}>1.39$. Since $E'\le\sqrt2l$, we have $\gamma_*-\gamma>.035d_x^{\max}>.021$. Using $\gamma_*>\arccos(1-.617)>1.17$ gives $\cos\gamma-\cos\gamma_*>.018$. Therefore
$$
  \cos(\gamma b)-(1-d)>.015
$$
throughout the near set. This strictly raises the tangential velocity component where the original global maximum can be active.

For transparency the following rough derivative bounds provide explicit shape, metric and reach estimates on the same field:
$$
 |H|\le.852,\quad |H_e|\le2,\quad |H_x|<610,\quad
 |H_{ee}|<1400,\quad |H_{ex}|<1430,\quad |H_{xx}|<2\,10^8 .
$$
Indeed $|q'|<19.24$, $|q''|\le1.13(1.875)/(.94\cdot.06\cdot(1/16)^2)<9700$, so $|c'|<19.24$, $|c''|<10100$. The bounds $|(a_0)_x|<.03$, $|(a_0)_{xx}|<.51$, $|(a_0)_e|<13.9$, $|(a_t)_e|<1258$, $|\delta'|\le1$ and $|\delta''|<19.38$ follow directly from R776. For $G=E-\sqrt2\delta$ at fixed $\gamma$ we obtain $|G_x|<9.8$, $|G_{xx}|<4400$, $|G_{\gamma x}|<10$ and $|G_{\gamma\gamma}|\le2l<1$. The root derivative formulas with $E'>.007$ give $|\gamma_x|<1400$ and $|\gamma_{xx}|<3\,10^8$. Differentiating (2) with these bounds, $|k|\le1/.27$, $|b_s|<25.1$ and $|N_x|=|q'|$ gives the stated six estimates.

Take $\lambda=10^{-10}$. In the fixed target orthonormal basis $(a_0^{-1}\partial_e,\partial_x)$ the short relative Gram deviation is $\operatorname{diag}(-M,0)$ with $M=1-(1-d)^2$. Its tangential column has leading component $1-d$ and the scaled correction is $V/a_0-(1-d)T$. On the near set the $ee$ diagonal increment is at least $2\lambda(.32)(.015)>.009\lambda$. The $xx$ diagonal change has magnitude at most $1221\lambda$; the off-diagonal magnitude is at most $614\lambda$. Since $M>.85$ there, the negative eigenvalue differs from its changed $ee$ diagonal by at most $2(614\lambda)^2/.8$ (the explicit two-by-two eigenvalue formula). The other eigenvalue is smaller in magnitude. On the complement, $M_*-M\ge 2(1-d_*)(.003)>.0019$ and the relative Gram change is less than $1300\lambda$. These estimates prove on the whole closed sphere and over every phase
$$
 \sup\|g_0^{-1/2}((F^\lambda)^*e-g_0)g_0^{-1/2}\|_{\rm op}
 \ \le\ M_*-.008\lambda .
$$
The unchanged cap and straight-band rows have zero error there. This is a strict all-phase descent, with guaranteed decrement $8\,10^{-13}$ for this explicit conservative amplitude; it is not a numerical-resolution claim.

It remains to establish the thickness of this very same field. Compare all point pairs to the R776 short surface at their common phase. Relative to its metric, $\|DH\|<2000$ because its smallest cylinder singular value exceeds $.32$. On a corner the unit normal changes by at most $8000\lambda$, by the cross-product formula and area $\ge.32$. On the rest $H=0$. The norm of the short physical Hessian on a material unit direction is less than $1300$, using $|k'|<6945$, $Z_t<.181$, $|q'|<19.24$ and the formula for $F_t$. Thus the magnitude of every new normal curvature is less than
$$
 \frac{20+(8000\cdot1300+4\,10^8)\lambda/(.32)^2}{(1-2000\lambda)^2}<20.41 .
$$
The head/cap bounds persist. To check all distant normal chords, let $\rho$ be the original Euclidean distance between distinct short-field points. For $\rho\ge .0002$ the new distance is at least $\rho-1.704\lambda>0$. The original ordered normal chord magnitude was at most $10\rho^2$ since the reach is at least $.05$. The new value increases by at most $8000\lambda\rho+1.704\lambda$. Hence its double divided by the new squared chord is at most
$$
 \frac{20+16000\lambda/.0002+3.408\lambda/(.0002)^2}
 {(1-1.704\lambda/.0002)^2}<20.1 .
$$
For $0<\rho<.0002$ nearest projection of the original straight joining chord to the short field gives a surface path of length at most $\rho/(1-20\rho)$. Along this path $|DH|<2000$, so the new chord is at least $\rho(1-2000\lambda/(1-20\rho))>0$. The length of the new path divided by that chord is less than $1.005$. These comparisons first establish global injectivity. Along the new path integrate its unit normal variation, using the just-proven principal curvature bound, to bound its ordered normal chord by $20.41$ times half the squared path length. This gives an inverse normal-chord radius less than $20.41(1.005)^2<20.7$ in the near range. Both signs and all central, roll, disk or mixed pairs have been included. The ordered quadratic normal inequality then proves reach $\ge1/20.7>.03D$ throughout the family. Every endpoint image stays within $.852\lambda$ of its short counterpart; the initial image is identical and the Euclidean quotient remains $\ge.020-.852\lambda$.

The exact continuum formulas for the broad swing are implemented by scripts/resume_20261128/bent_short_normal_arc.py (the scalar is obtained from its monotone chord equation). Working arithmetic uses the split true clock and arc knots, their signed moments, and implicit derivatives of the finite root. Run 50 carries independently the unscaled swing and two larger finite fractions, plus two complete other physics families. Its fitted fields have separate geometric and metric costs; neither this low-amplitude certificate nor a small sampled error certifies a strong corrected optimizer field.

## Short-tube cell endpoints under a relative metric error and a reach bound

Let $F_0$ be the continuum R776 initial embedding with $g_0=F_0^*e$ and $D=\operatorname{diam}F_0(M)$. Consider any final closed $C^2$ embedding $F$ with
$
 F^*e\ \geq (1-10^{-6})g_0,\qquad \operatorname{reach}F(M)\ \geq .03D.
$
The usual uniform relative Gram operator error at most $10^{-6}$ implies the displayed one-sided inequality. On the material ring $x=v+1/2=1/4$, take one softened R776 corner and divide its original angular arclength interval into $N$ equal cells. A short-prescribed endpoint means the image of the indicated material point under the R776 short embedding at final phase $\pi/2$, allowing one common Euclidean isometry for all such prescriptions.

If $N\geq2$, the endpoints cannot all have their short-prescribed positions. For $N=2$, one of the first cell's endpoints must move by more than $.0004$ from that prescription. For $N\geq3$, take the cell of index $\lfloor(N-1)/2\rfloor$, counting from zero. One of its endpoints must move by more than $.026\ell$, where $\ell$ is this cell's arc length in the initial physical ring. These conclusions concern two marked positions on the final image. They apply to arbitrary changes of the intervening arc and of the rest of the surface. They use no derivative of the metric error.

### A chord estimate on a set of positive reach

Let $S$ be the image of a closed $C^2$ embedding of reach at least $r$. For $A,B\in S$ of chord length $d<2r$,
$
 d_S(A,B)\ \leq\ 2r\,\operatorname{artanh}(d/(2r)).
 \tag{1}
$
For $y=(1-u)A+uB$, the distance $s$ from $y$ to $S$ is at most $\min(u,1-u)d<r$. Let $p$ be its unique nearest point. If $s>0$, set $n=(y-p)/s$. The open tangent normal ball of radius $r'<r$ has no point of $S$ in its interior, giving $2r'\langle n,Q-p\rangle\leq |Q-p|^2$ for $Q\in S$; pass to $r'\uparrow r$. Use $Q=A,B$ with weights $1-u,u$ to obtain $2rs\leq s^2+u(1-u)d^2$. Thus $r-s\geq\sqrt{r^2-u(1-u)d^2}$, including $s=0$.

For a second point $y'$ on the chord with projection $p'$ and distance $s'$, the two tangent ball inequalities, at $p,p'$, give
$
 \langle y-y',p-p'\rangle\geq
 \left(1-\frac{s+s'}{2r}\right)|p-p'|^2.
$
The projected segment is Lipschitz by $s,s'\leq d/2<r$; its speed at almost every parameter $u$ is bounded by $d\,r/(r-s)$. Its endpoints are $A,B$. Integrating yields (1), since
$
 d\int_0^1\frac{du}{\sqrt{1-u(1-u)d^2/r^2}}
 =2r\,\operatorname{artanh}\left(\frac{d}{2r}\right).
$
Conversely, for material points $P,Q$, every path on the embedded image lifts to the material surface. The assumed metric lower bound implies
$
 d_S(F(P),F(Q))\geq\sqrt{1-10^{-6}}\,d_{g_0}(P,Q)
 \geq\sqrt{1-10^{-6}}\,|F_0(P)-F_0(Q)|.
 \tag{2}
$

### Initial diameter and the two true ring offsets

The R772 section used in R776 has four flats of length $.14$ and four symmetric quarter turns of length $L=.27\pi/2+.001$. On a quarter turn $0\leq\beta'\leq1/.27$. Write $ds=.27\,d\beta+d\mu$ with $d\mu\geq0$. The coordinate support of each opposite flat is at least $.14/2+.27\int_0^{\pi/2}\cos\beta\,d\beta=.34$. On either axial end fillet the same decomposition uses radius $.09$; its residual measure has total mass $.001$. Its axial advance $p_b=\int\cos\alpha\,ds$ is at least $.09$ and its radial debit $d_b=\int\sin\alpha\,ds$ is at most $.091$. On the initial tube the axial speed is at least $\cos(.008)$ on a unit material interval. Choose the upper cap rim at one flat midpoint and the lower cap rim at the opposite midpoint. Their axial separation is at least $\cos(.008)+.18$ and their separation along one transverse coordinate is at least $2(.34-.091)=.498$. Hence $D^2\geq(\cos(.008)+.18)^2+.498^2>1.28^2$. In (1) we may use the smaller fixed radius $r=.0384$.

The R776 short ring at the selected axial point is $\gamma(s)-z_j n(s)$, with constant axial coordinate, at the initial and final phases $j=0,1$. Here
$
 z_j=\int_0^{1/4}\sin(Q_j w(x))\,dx,\qquad Q_0=.008,\quad Q_1=1.13 .
$
The wave on this quarter interval consists of a unit plateau of length $1/8$ and two reflected ramps of length $1/16$. The unit ramp clock $f$ satisfies $f(u)+f(1-u)=1$, $0\leq f\leq1$, $0\leq f'\leq1/.94$, $f(0)=0$. Thus $\int w=3/16$. Also $f(u)\leq\min(1,u/.94)$ and
$
 \int w^3\leq \tfrac18+\tfrac18(.94/4+.06)=.161875.
$
Therefore $0\leq z_0\leq.0015$ and $z_1\geq1.13(3/16)-1.13^3(.161875)/6>.1729$. Moreover $z_1\leq1/4<.27$.

### Two cells

The first half of the true softened corner turns through $\pi/4$ by symmetry. In $ds=.27\,d\beta+d\mu$, the nonnegative residual measure on this half has mass exactly $.0005$. The parallel curve chord vector is
$
 (.27-z_j)\int_0^{\pi/4}T(\beta)\,d\beta+\int T\,d\mu ,
 \qquad \left|\int_0^{\pi/4}T(\beta)\,d\beta\right|=2\sin(\pi/8).
$
Consequently the initial chord satisfies
$d_0\geq2(.27-.0015)\sin(\pi/8)-.0005>.204$. The final short-prescribed chord is at most
$2(.27-.1729)\sin(\pi/8)+.0005<.075$.
Even if both endpoints move by $.0004$ each, their actual chord is $<.0758$. Equation (1) bounds their intrinsic distance by $.0768\operatorname{artanh}(.987)<.194$; (2) bounds it below by $ .204\sqrt{1-10^{-6}}>.203$. This proves the claimed exclusion, including the softened end of this cell.

### Three or more cells

The stated central cell lies at distance at least $L/4>.001$ from both quarter-turn endpoints, so the curvature is identically $1/.27$ there. Set $\Delta=L/N$, $\ell=(1-z_0/.27)\Delta$, $h=\Delta/(2\cdot.27)<.263$, and $\operatorname{sinc}h=\sin h/h$. Its initial chord and final short-prescribed chord satisfy
$
 d_0/\ell=\operatorname{sinc}h>.98,\qquad
 d_{\rm short}/\ell=\frac{.27-z_1}{.27-z_0}\operatorname{sinc}h<.378.
$
If both endpoints move by at most $.026\ell$, their actual chord $d<.43\ell$. Since $\ell\leq L/3<.142$, $d/(2r)<.80$. The increasing function $\operatorname{artanh}(u)/u$ is less than $1.38$ on this interval. Equation (1) therefore gives $d_S<.594\ell$, whereas (2) requires $d_S>.979\ell$.

The R778 periodic primitive vanishes at every full cell endpoint, because the cell coordinate is zero there and both partial moment primitives vanish at zero. The continuum periodic field by itself, and any perturbation keeping all those short positions, is subject to this argument. The one-cell whole-corner prescription and the Run 50 unrestricted physical coefficients require independent analysis. The latter can move the material endpoints. No sampled strain, computed reach, accepted optimizer point or numerical action result enters the proof.
