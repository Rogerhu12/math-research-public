# R778. Explicit all-phase near-isometric embeddings of the R776 closed sphere, with a finite frequency and its thickness cost

Fix **one** metric, namely the initial nine-chart metric in R776. This result supplies a sequence of complete jointly $C^2$ embedded families. They fix the same entire right head, preserve both complete head poses, retain macroscopic whole-image and Euclidean quotient separations, and their relative metric errors tend uniformly to zero in phase and in all material coordinates, including the two poles. At the explicit finite angular repetition $n=40\,000\,000\,000$ the full relative spectral error is less than $10^{-6}$. Their curvatures grow at least linearly in $n$ and their reaches tend to zero. The limiting position map itself is the R776 short field. This sequence does not supply the requested exact thick isometry or a mesh resolving forty billion angular periods.

## The finite physical field and its corner compatibility

Use the constants, materials and signed normal convention of R776. In the central chart write $T=C'(e)$, $N_t=(\cos q_t\,n,\sin q_t)$ in transverse/axial pair notation, $U=F_{t,x}=(-\sin q_t\,n,\cos q_t)$ and $F_{t,e}=a_tT$, where $a_t=1-kZ_t$. The three world vectors $T,N_t,U$ form an orthonormal frame. Let
$$
 \delta=Z_t-Z_0,\qquad a_0=1-kZ_0,\qquad d=k\delta/a_0,\qquad h=l/n,\qquad l=.27\pi/2+.001<.426 .
$$
We have $a_0>.992$ and $0\le d<.68$, with $a_t/a_0>.32$. Let $b(u)$ be the period-one odd pulse of R776: on $[0,.5]$, $b=S_7(u/.025)S_7((.5-u)/.025)$, with clipped arguments, and on $[.5,1]$ use $b(u)=-b(1-u)$. Its absolute value is one on $.9$ of a period. There is a unique $\alpha\in[0,\pi/2)$ such that
$$
 \int_0^1[1-\cos(\alpha b(u))]\,du=d .
$$
The integral increases strictly, from zero to at least $.9$ at $\pi/2$. Since $\int\cos(\alpha b)\le .1+.9\cos\alpha$, we have $\cos\alpha>(.32-.1)/.9>.244$. In particular even the largest oscillating tangent stays transverse to the nearest-normal fibers of the original embedded shell. Put
$$
 v(s,x,t,u)=a_0\{\cos(\alpha b(u))T+\sin(\alpha b(u))N_t\},\qquad
 W(s,x,t,y)=\int_0^y [v(s,x,t,u)-a_tT]\,du .
$$
The mean of the first summand is $a_tT$ and that of the normal summand is zero by reflection. Thus $W$ is a periodic primitive with $W(0)=W(1)=0$. In a true curved quarter use its own arclength $s\in[0,l]$ starting at the preceding straight face. Define the complete map there by
$$
 \widehat F_{n,t}=F_t+h W(s,x,t,s/h).
$$
Keep $F_t$ unchanged on every straight-transverse band, both entire rolls and both entire terminal disks. There are $n$ full periods in each corner regardless of the perimeter-to-corner-length ratio. This cornerwise phase is part of the field.

For regularity set $\Psi(G)=\int[1-\cos(\sqrt G b)]du$. Its derivative is $\int b^2\operatorname{sinc}(\sqrt G b)/2\,du\ge .9/\pi$ on this interval, including $G=0$. Hence $G(d)=\alpha^2$ is smooth, with $G(0)=0$ and $G(d)/d$ smooth and strictly positive. In particular $\alpha=\sqrt{k}\sqrt{\delta}\,L(d)/\sqrt{a_0}$ where $L(d)=\sqrt{G(d)/d}$. The exact moment series of the tangential primitive uses only powers of $G$, and the normal primitive is $\alpha$ times a smooth function of $G,y$. As established in R776, $\sqrt{\delta}$ has a continuous full two-jet, one-sided in phase at the two phase endpoints; at each axial lobe edge it is $\sin t$ times $|x-x_*|^{5/2}$ times a positive smooth one-sided function. Thus the longitudinal zero and the initial phase cause no derivative loss.

At a transverse edge let $u_*$ be its one-sided material distance. Here $k=O(u_*^3)$, $\sqrt k=O(u_*^{3/2})$ with successive derivative orders reduced by one, and, for fixed integer $n$, the actual phase is $O(u_*/h)$ from an integer. The primitive divided by $\alpha$ in its normal component vanishes at **both** ends of a period for every $G$. Near the integer it is $O((u_*/h)^5)$ since $b$ starts at order four. Its $G$-derivatives also vanish to this order. The tangential primitive is $O(k\,u_*/h)$ together with the differentiated versions from its smooth series. Consequently the correction, its first and both second material derivatives all tend to zero at the curved-to-flat boundaries. At axial lobe edges the correction likewise vanishes through order two, using the $\sqrt{\delta}$ factor. The exact published full two-jets between cylinder, rolls, planar collars, polar and Cartesian disk charts are preserved. This proves joint $C^2$ on the whole material sphere and in the phase parameter. In particular $\widehat F_{n,0}=F_0$ exactly for all $n$.

## A fixed finite bound for all three coefficients

A subscript on $W$ in this paragraph differentiates the slow material variables with the argument $y$ held fixed. Direct differentiation gives
$$
 (\widehat F_n)_e=v+hW_e,\qquad
 (\widehat F_n)_x=U+hW_x,\qquad v\cdot U=0,\quad |v|=a_0,\quad |U|=1 .
$$
Thus a single construction corrects the angular speed without retaining an oscillating mixed term. The slow derivative errors admit the following uniform elementary estimates:
$$
 |W|\le2,\qquad |W_e|<36000,\qquad |W_x|<40 .
$$
Here are details of the numerical constants. $\partial_\alpha\int(1-\cos(\alpha b))\ge .9(2/\pi)\alpha$, and $d\le\alpha^2/2$, so $|d\alpha/d\sqrt d|<2.5$. On a curvature ramp $z=s/.001$, $S_5(z)\ge z^3$, $|S_5'(z)|\le30z^2$. Thus $|(\sqrt k)'|\le15/(.001\sqrt{.27})<28868$, $|k'|\le1.875/(.001\cdot.27)<6945$ and $|(a_0)_e|<13.9$. Differentiating $\sqrt d=\sqrt{k}\sqrt{\delta}/\sqrt{a_0}$ gives $|\alpha_e|<31000$. The longitudinal estimate follows from $|\delta''|\le(1.13+.008)/(.94/16)<19.38$ and nonnegativity of $\delta$ on its full periodic continuation. The quadratic Taylor upper bound at the stationary point of the comparison parabola gives $|\delta'|^2\le2(19.38)\delta$. Hence $|(\sqrt\delta)'|<3.12$, while $|(a_0)_x|\le.008/.27<.030$; it follows that $|\alpha_x|<15.3$. Finally $|T_e|\le1/.27$, $|(N_t)_e|\le1/.27$, $|(N_t)_x|=|q_t'|<19.24$, $|(a_t)_e|\le.181(6945)$, and $|(a_t)_x|\le1/.27$. In differentiating $\cos(\alpha b)T+\sin(\alpha b)N$ its angle derivative has norm exactly $|b|$. Inserting these bounds into the primitive over at most one period proves all three estimates.

In the target-orthonormal coordinates $a_0^{-1}\partial_e,\partial_x$, the leading columns $v/a_0,U$ are orthonormal. Their joint perturbation has operator norm bounded by its Frobenius norm, less than $16000/n$. If $E_n$ denotes the relative spectral error of the metric on the full sphere, at every phase,
$$
 E_n\le 2(16000/n)+(16000/n)^2 .
$$
It is zero on the rest of the charts. The stated finite $n$ therefore gives $E_n<.000001$. The position error relative to the true short field is at most $2h<.852/n$, uniformly in phase, with no constant depending on the selected finite field.

## Global embeddedness, fixed grip, and both separations

For $n\ge2\,000\,000$, $u_0=2h<.000001$. At each phase, nearest projection $\pi$ to $F_t$ is well defined in this tube by the complete R776 global certificate. Along the segment from $F_t(p)$ to $\widehat F_{n,t}(p)$ the foot moves by at most $u_0/(1-20u_0)$, measured in intrinsic length on $F_t$, by the inverse differential of its normal coordinates. The normals of the two feet therefore differ by at most $20u_0/(1-20u_0)$. Choose the positive sign of the cross product to agree with $N_t$. On the corner its leading unit-normal component is $a_0\cos(\alpha b)>.242$. The two error columns have lengths at most $h(36000)$ and $h(40)$, so their error in the cross product is less than $.008$ in this $n$-range. The replacement of the normal by the normal at the actual foot subtracts less than $.00003$. On the remaining charts the projection is exactly the identity. Consequently the closed map $\pi\circ\widehat F_n$ onto $F_t(S^2)$ is everywhere a local diffeomorphism. Compactness, connectedness and the simple connectivity of the target sphere give a one-sheeted cover. Each $\widehat F_n$ is an embedded global normal graph, and no mixed caps or distant pairs were excluded from the argument.

The entire right grip and both exact head poses persist, with diameter of the former at least $.68$; the initial diameter is still $D<1.55$. From R776 and the position error the held separation is at least $.323-.852/n$, and the Euclidean-quotient separation at least $.020-.852/n$ by the triangle inequality, uniformly in the comparison Euclidean motion. In fact the explicit shape preserves the macro axial bound already at $n=1$: its tangential primitive is horizontal, and the normal primitive has nonnegative scalar coefficient bounded by $a_0/2$ by the sign of $b$ and reflection. Thus a negative axial displacement from $F_t$ is possible only on a negative axial quarter, $x\ge.25$, and then has magnitude $<.5l\sin1.13<.193$. On these quarters $A_t(x)-A_t(0)+p_b\ge.25\cos1.13+.09>.196$. All central points therefore stay above the fully retracted leftmost terminal plane, where equality is attained. The physical leftmost-to-whole-image held stays $>.323$ for every positive integer at the terminal phase, independently of the embedding conclusion for small $n$.

## Upper and lower thickness costs for each finite frequency

For any fixed $n$ in the embedded range, joint $C^2$ compactness gives positive reach uniformly in phase. A finite-frequency version uses the actual second jets directly. Define $M_n$ to be the maximum of the norms of the second $(e,x)$ material derivatives of the formula in the four closed central corner rectangles, over $t$, increased to at least $20$; use the closed analytic one-sided values at all seams. It is finite by the proven two-jet compatibility. The two material derivatives differ from orthogonal vectors of lengths $a_0,1$ by a joint norm $<.009$, so their smallest singular value is $>.98$. Every central principal curvature is therefore bounded by $3M_n$ and the unchanged rest by $20$. The plane projection of the data at each foot, restricted to the perturbed tangent plane, has least singular value equal to the absolute normal scalar product. The cross-product estimate in the preceding paragraph, with actual area at most $(1+.009)^2$, makes this singular value $>.22$. The extra factors of the footpoint projection on that plane are at least $1/(1+20u_0)$. The inverse graph map thus has norm less than $5$.

If two perturbed surface points are at Euclidean distance $\rho<.01$, their joining segment is in the $.011$ tube of the short surface. The projected path there has length at most $\rho/(1-20(.011))$ and its inverse graph lift has length less than $7\rho$ on the perturbed shell. Along a unit-speed surface path of length $m$ intrinsic normal variation has speed at most $3M_n$, hence the ordered normal chord at the initial point has magnitude at most $3M_n m^2/2$. For $\rho\ge.01$ its magnitude is at most $\rho$. Together these two estimates give the explicit usable comparison
$$
 \operatorname{reach}(\widehat F_{n,t})\ \ge\ \min\{.005,1/(147 M_n)\}.
$$
Indeed the ordered quadratic normal-chord bound ensures that open balls of this radius tangent on either side contain no surface points, or directly excludes two distinct nearest points at any smaller offset. $M_n$ is computed from the stated field for a given $n$; a maximum on finitely many sampled nodes alone cannot be substituted for its supremum.

There is also an explicit upper bound at the terminal phase. Use axial station $x=.25$ where $q=q'=0$ and $Z_t,Z_0,\delta$ all have zero first axial derivative. Consequently $U=e_Y$, $N=n$, $W_x=0$, the actual axial derivative is $e_Y$, and the physical angular curve lies entirely in an $(X,Z)$ plane. Its ordinary planar curvature equals the magnitude of its normal curvature on the shell. In the constant-curvature interior of one quarter choose a point with $s/h$ of fractional part $.0125$. Such a point exists for every $n\ge100$ since $l-2(.001)>h$. Here $a_0>.992$, $\delta>.125\sin1.13-.002>.110$, $d>.407$, $\alpha\ge\sqrt{2d}>.90$, and $b'(.0125)=2.1875/.025=87.5$. Write $W=A T+B n$. The position derivative is
$$
 D=v+h k(BT-A n).
$$
The slow angular derivatives of $A,B$ vanish on this constant-curvature arc, $|W|\le2$, $|\partial_yW|\le2$, and $T'=-kn$, $n'=kT$. Thus
$$
 D'=(a_0\alpha b'/h)\{-\sin(\alpha b)T+\cos(\alpha b)n\}+R,\qquad
 |R|\le 3k+2hk^2<11.3 .
$$
For $n\ge100$, $|D-v|\le2hk<.032$. Hence the component of the leading $D'$ in the actual planar normal direction is at least $(a_0-.032)/(a_0+.032)>.93$ times its magnitude. Using $|D|\le1.032$ and $h=l/n$, the curvature is greater than $100n$. The reach of a $C^2$ embedded hypersurface is at most the reciprocal of any absolute normal curvature, as follows by taking the second-order limit in its ordered normal-chord inequality. In particular in the established embedded range the reach is $<1/(100n)$. This is an actual simultaneous cost of the selected fixed-metric approximation. The true quantitative thickness bound of the uncorrugated R776 shell cannot be transferred to this high-frequency branch. It leaves open finite, low-curvature physical redistribution of both tangent directions on the same frozen target.

The full world two-jet generator is scripts/resume_20261126/r778_normal_periodic_closed_corrugation.py. The integer harmonics counts full repeats per actual curved quarter. Individual finite fields use R776's real nine charts. The numerical code uses split quadrature for the pulse moments, 16 nonzero cosine terms, 17 sine terms and a 52-step scalar bisection for $G/d$, followed by implicit first and second differentiation. The estimates above are for the integral definitions, independently of floating point evaluation or an angular mesh size.