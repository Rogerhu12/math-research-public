# R769. Redistribution of the actual turning angles, exact complete meridian lengths, and the interface that must move

**Fixed datum.** Use the single zero-phase metric of R764, with both complete nonflat pre-rolls, both complete standard rolls and the two actual curved R760 caps. This is the same tensor as in R764 and R766, including the four marked patches, every old material label and both cap overlaps. The moving field below has a new central section. All physical charts use the six derivatives in the order $F,F_s,F_v,F_{ss},F_{sv},F_{vv}$. A numerical sample of a Gram matrix, curvature or support does not certify a whole material region.

## 1. Closing a unit central section without turning any original straight interval

Let $\gamma_0$ be the R760 section of period $P$ parametrized by material length. Write $T=(\cos\beta,\sin\beta)$, $N=(-\sin\beta,\cos\beta)$, $T'=-\kappa N$, $N'=\kappa T$. The upper section starts on the left reflecting line and ends on the right one. The lower section is obtained by reflection in $z=0$ and reversal. In all formulas below $\theta\in[0,.90]$ and $A=\pi/2$.

For $l<x<h$ use a speed $W$ which rises by $S_7(t)=35t^4-84t^5+70t^6-20t^7$ in length $e$, stays at one and descends by the reverse speed in the last $e$. Extend the speed by zero. Write $H(x)=\int_{-\infty}^xW/(h-l-e)$. The first clock $H_A$ has $(l,h,e)=(.02,A-.02,.04)$. Its normalizing length is $A-.08$ and $H_A(A-x)=1-H_A(x)$. The second clock has $(1.05,\pi-.38,.14)$; call one minus its normalized integral $B_1$.

Modify the actual upper tangent angle only as follows.

* From the rising vertical track into the original left quarter-turn put $\widetilde\beta=\beta_0+\lambda H_A(A-\beta_0)$. Keep this formula on the full quarter-turn. The original horizontal panel of material length $1.30$ is a straight line of angle $\lambda$.
* On the original negative bend $.30\le x_{\rm material}\le .56$ use $\widetilde\beta=\beta_0+\lambda-(\theta+\lambda)H_A(\beta_0)$. The following original straight tongue of length $.44$ has angle $\pi/2-\theta$.
* On the entire true right U-turn use $x=\pi/2-\beta_0$, $\widetilde\beta=\pi/2-x-\theta B_1(x)$. From $x=\pi-.38$ through the straight descending track, both signs of all right wall elbows and their equator, use $\beta_0$. The old left wall and its approach also use $\beta_0$.

On the first, second and third changing arcs the factors $a$ in $\widetilde\kappa=a\kappa_0$ are respectively $1-\lambda H_A'$, $1-(\theta+\lambda)H_A'$ and $1+\theta B_1'$. They equal one on genuine open neighborhoods of the endpoints, with no quotient of two zero curvatures. Everywhere else set $a=1$, including the entire straight materials and the two reflecting joins. For $0\le\lambda\le .45$,
$$
 .09<1-\frac{1.35}{\pi/2-.08}\le a\le1,\qquad 1\le r:=a^{-1}<100/9.
$$
The multiplier is sufficiently smooth for all displayed two-jets. In particular its transition is finished before the inner break in each actual softened negative-curvature ramp. The center curvature satisfies $|\widetilde\kappa|\le|\kappa_0|<7$.

Integrate the unit tangent, starting at the old upper left equator. Its vertical integral $I(\lambda,\theta)$ must vanish. At $\lambda=0$ the deficit from the old closed height is nonnegative. It is bounded by
$$
 .26\,\theta/2+.44(1-\cos\theta)
   +\theta\{.15[1.05+(\pi-.38-1.05)/2]+.001\}<.543 .
$$
For the negative bend use the Lipschitz bound on sine and the symmetry of $H_A$ on the true softened material bend. The tongue gives its exact term. The original U-turn length measure in angle is $.15\,dx$ plus a positive measure of mass $.001$ on its two ramps. Integrate $B_1$ against that measure. The angle $x+\theta B_1(x)$ increases through the entire modified U-turn and never passes $\pi$. With increasing $\lambda$ all affected vertical derivatives have nonnegative sign: in the left and negative bends the angles stay in $[0,\pi/2]$ and the multipliers of $\lambda$ in the angle itself are nonnegative. The long panel alone contributes $1.30\sin(.45)>.565$ between the two bracket endpoints and contributes a strictly positive derivative throughout. Thus there is a unique closing $\lambda$, including $\lambda=0$ at phase zero, with smooth phase dependence.

The upper section has positive height inside the two equators. The left wall stays on its original side. From the left rotating corner up to the descending track the abscissa is nondecreasing; the U-turn angle has one extremum of height and the remaining original right wall is a translated descending graph. More explicitly the right wall's original abscissa stays on or outside its descending-track abscissa: the initial positive lateral elbow reaches angle $1.44$ in the unscaled clock and its positive dwell is $.06$, while the returning negative pulse has peak $.71$, shorter support and smaller magnitude. Integrating the actual two opposite triangular pulses, with identical endpoint regularizations and the same positive amplitude, bounds the total negative excursion by the preceding positive one. The left wall's exterior lies on the other side of the first vertical track. The middle part lies between these distinct track abscissae. Reflection therefore produces a simple regular closed section. Align it by translating its true $.55$ grip point to the R760 moving grip point, then apply the common prescribed rotation through $\theta$ about the original axis. On the whole true grip the result is the original marked circular material. This follows from equal tangents on the grip and the equality of the fixed circular point after rotating back its advance $.15\theta$. On the connected right sector the unrotated body is a single translation $J_\theta$ of the original upper and lower section. Write the complete marked center over $|y|\le .88$ just as in R764. The full central metric is exact. The stationary grip contains a material interval of Euclidean length $1.40$.

## 2. Both signs of the entire true pre-roll

Put $E=.44$, $\epsilon=.0025$, $\alpha(v)=\epsilon\sin(2\pi v/E)\sin^2(\pi v/E)$, $d'=\sin\alpha$, $p'=\cos\alpha$, $d(0)=p(0)=0$. Then $d(E)=0$ and the fixed metric is $f^2ds^2+dv^2$, $f=1-\kappa_0d$. At both ends $d'=d''=p''=0$ and $p'=1$. For every $s$ and the complete $0\le v\le E$ put
$$
 P(r,v)=\int_0^v\sqrt{1-r^2d'(t)^2}\,dt,\qquad
 F_\pm=(\widetilde\gamma-rd\widetilde N,\ \pm[.88+P(r,v)]).
$$
Here planar vector components occupy the physical $xz$ directions. The radicand exceeds $1-(.0025\cdot100/9)^2$. With $Y=P_v$, the true three components are
$$
 g_{vv}=1,\quad
 g_{sv}=r_s\{r d d'+P_rY\},\quad
 g_{ss}=f^2+r_s^2\{d^2+P_r^2\}.
$$
Indeed $F_s$ has signed orthogonal components $(f,-r_s d,r_sP_r)$ in tangent, outward normal and axial directions. $P_r=-\int_0^v r d'^2/Y$ and $P_{rr}=-\int_0^v d'^2/Y^3$. The full original metric holds wherever $r_s=0$. In particular all genuine curvature zeros, all originally straight intervals, all constant parts of the angular speed clocks and the common rigid right sector have no pre-roll defect. The other errors are explicit, supported strictly inside true curved arcs. This assertion covers both full signs and includes the angularly variable endpoint height $P(r,E)$.

## 3. A genuine complete standard quarter-turn and full curved cap charts

Write $L=.132\pi/2+.0005$. On the original complete standard roll the softened angle $\alpha_R$ increases from zero to $\pi/2$, its derivative vanishes at both ends, $D'=\sin\alpha_R$, $Q'=\cos\alpha_R$, and $D_b=D(L)=Q(L)$ satisfies $.132\le D_b<.1325$. For each of the two registered responses $c=.5,1$ let $b=1+c(r-1)$ and define
$$
 H=(\cos^2\alpha_R+b^2\sin^2\alpha_R)^{1/2},\quad
 D_b'(u)=b\sin\alpha_R/H,\quad Q_b'(u)=\cos\alpha_R/H .
$$
To distinguish the response integral from the original terminal constant, write $D_b(u),Q_b(u)$ for these two integrals from zero and $d_{\rm end}=D(L)$ for the old constant in the following formulas. Use the physical field
$$
  \big(\widetilde\gamma-D_b(u)\widetilde N,\ 
       \pm[.88+P(r,E)+Q_b(u)]\big),\qquad 0\le u\le L.
$$
It remains real when the original $\sin\alpha_R$ is arbitrarily close to one, for every original material angle. The direction at $u=0$ is the positive outward axial direction and at $u=L$ the inward planar normal. Both normal accelerations vanish there. All six physical derivatives consequently match the pre-roll across $v=E$. Write $X=D_b$, $Z=P(r,E)+Q_b$. Its complete three component prices are
$$
 g_{vv}=1,\qquad g_{sv}=X_sX_v+Z_sZ_v,\qquad
 g_{ss}=(1-\widetilde\kappa X)^2+X_s^2+Z_s^2 .
$$
The subscript $v$ denotes the local standard-roll coordinate. Where $r$ is constant only the scalar angular price remains. Since $1\le b\le r$ and $H\ge1$, $0\le X/r\le D$. Thus $1-\widetilde\kappa X\ge1-\kappa_0D>.07$ on every original positive cell, and it is at least one on negative cells. The velocity has no tangent component, so the actual area is at least $1-\widetilde\kappa X$ even in the transition windows. Every complete standard roll here is a regular immersion. On $r=1$ constant all three Gram prices vanish.

For the true cap let $j(w),\rho(w)$ be the original R760 collar clock, $w=0$ the real rim and $\rho=1$ there. In the outer polar or cap-normal chart start with $J_\theta F_{\mathrm{cap},0}$ and add the following plane vector and signed axial coordinate, multiplied by $S_7((\rho-.83)/.15)$:
$$
 \widetilde\gamma-(D_b(L)+j)\widetilde N-J_\theta\gamma_0
             +(d_{\rm end}+j)N_0,\qquad
 \pm[P(r,E)+Q_b(L)-p(E)-Q(L)] .
$$
$J_\theta$ is a translation and does not act on $N_0$. In the regular Cartesian inner chart use the original translated cap. The full correction is identically zero on the inner overlap $\rho\le .82$. Near the true rim $j(w)=w$, the fade is exactly one and the old cap rise has zero first and second derivatives. The three tangential and transverse derivatives of orders zero, one and two therefore agree with the actual standard roll at its end. This explicitly defines both whole caps. The registered cap interior data give their original positive separation from the central witness plane, including the very small original bowl height. Intermediate cap angular and mixed strains, possible folds and directed normal-ball prices are independent costs.

## 4. Finite held displacement and an intrinsic obstruction at the new intermediate ring

At the final phase the actual $\lambda>.238$. At $\lambda=0$ the tongue loses more than $.166$ of height. On the true bend, $H_A(\beta)\ge(\beta-.06)_+/A$, its curvature magnitude is at most $6.91$ and $\sin\beta-\sin(\beta-.90H_A)\ge .90H_A\cos\beta$. Integration gives an additional loss greater than
$$
 \frac{.90}{6.91 A}\int_{.06}^{A}(\beta-.06)\cos\beta\,d\beta > .042.
$$
The U-turn's first $1.05$ radians lose at least $.15[\sin(1.05)-\sin(1.95)+\sin(.90)]>.107$. On $1.05\le x\le1.85$, the sine on $[x,x+.90B_1(x)]$ is at least $.70$: the upper endpoint increases and at $1.85$ it is below $2.34$. The mean $B_1$ on this interval is at least $1-.4/1.57$, giving more than $.056$ further loss. The $\lambda$ derivative of the height is at most $1.30+.26/2+.237/2<1.55$, by symmetry of each clock on its material bend. These bounds prove the stated inequality.

After applying the outer rotation, the entire original start of the U-turn coincides with its original material image. It has abscissa at least $.43$ by symmetry of the original disk bend. The preceding tongue is exactly vertical in this physical frame. Through the complete negative bend and the long panel, backwards horizontal loss is at most $1.56\cos(1.138)$. The left quarter-turn adds at most $.15(1-\sin .90)+.001<.034$: drop its nonnegative angular increment and integrate the positive part of $\cos(\beta+.90)$ against the original softened-turn measure. Before this corner the vertical track has length greater than $.149$. Its backtracking gains more than $.149\sin .90$ in abscissa. The old bowed half-wall can lose at most $.545\sin(.20)$ of that gain. Indeed its initial amplitude is less than $1.10$: at $1.10$ its normalized vertical integral is at most $.99[1-1.10^2/4+1.10^4/64]+.01<.41/.545$. This bound follows by separating the endpoint clock slowdown of total normalized mass $.01$ from the uniform half-circle angle measure. The wall integrand in the final horizontal direction is $\sin(\alpha-.90)$ with $0\le\alpha<1.10$. To the right of the U-turn start the rotated abscissa is nondecreasing, including on the right wall where $-.71\le\alpha\le1.44$ and $0<\alpha+.90<\pi$. Lower points are farther right than their reflected upper partners because the raw upper height is positive. The marked upper points are inside the stationary grip. Thus the whole central abscissa exceeds $.43-1.56\cos(1.138)-.034$. The initial witness on the left equator has $x_m\le-1.149,y=0$; the horizontal gap exceeds $.88$.

Both normalized pre-rolls and standard rolls have $|y|\ge.88$. The curved caps retain $|y|>.88$: the physical fade makes their large positive endpoint height a convex interpolation between $p(E)+Q(L)$ and $P(r,E)+Q_b(L)$, plus the original bounded cap height excursion. Already $P(r,E)>.439$ on every angle. Hence the entire normalized guide has a directed held displacement at least $.88>.2D_0$ with the true R764 $D_0<4.386$. The initial whole normal radius is at least $.132>.03D_0$. The common right isometric parts inherit the pairwise normal-ball inequalities between their own points. A later whole-surface normal radius has not been bounded by these initial or regional estimates.

There is an additional obstruction to treating this guide as a global exact solution. At $x_{\rm material}=.30$ take the upper and its reflected lower label on the same end. On the pre-roll exit the planar positions are the new section since $d(E)=0$; their separation is at least $2(.71+1.30\sin\lambda)$. The matching points on the original cap rim have separation $2(.71-d_{\rm end})$. Both changes of a single rigid cap pose preserve the latter distance. Each remaining standard meridian has material length exactly $L$, hence all poses require $d_{\rm end}+1.30\sin\lambda\le L$. The left side is greater than $.438$ at the final phase and $L<.208$. Moreover the vertical line $x=.30$ between the two original rim labels is a physical path across the original projected cap disk. Its true graph slope has magnitude at most $.00075$ by R760/R764. For this line the first projected upper corner to its right has $x>.30$ (the inward offset of the original negative bend has an additional positive $x$ component), the right U-turn and wall stay farther right, and the old left track is to the left. Reflection supplies the opposite rim. This gives an intrinsic cap path of length at most $2(.71-d_{\rm end})\sqrt{1+.00075^2}$. Allowing a completely different isometric cap still leaves the strict contradiction. The intermediate $v=E$ trace must be released, or the central Cauchy data themselves changed. This uses the new $E$-ring and the redistributed center rather than the old R754 final wall-chord argument.

## 5. Release the entire intermediate interface using three actual meridian controls

Let $T=E+L$, and make a *single* material meridian coordinate $u\in[0,T]$ across the old join. Use the original complete signed velocity $U_0(s,u)$ in the oriented frame $(T_0,\pm e_y,-N_0)$. Its components are $(0,\cos\alpha_0,\sin\alpha_0)$ with the full corrugated angle before $E$ and the full softened quarter-turn angle after $E$. Each sign is used on its actual complete material half.

For terminal retreat $e=.30$ or $.42$ prescribe the positive axial displacement $b_\theta=p(E)+Q(L)-e\theta/.90$. Let $C=J_\theta(\gamma_0-d_{\rm end}N_0)-\widetilde\gamma$ be the planar vector to the real rigid reference rim. Set $R=\sqrt{(T-.005)^2-b_\theta^2}$ and $h=.9R$. If $z=|C|\le h$ keep it. Otherwise multiply $C$ by
$$
 \frac{h+(z-h)[1+((z-h)/(R-h))^4]^{-1/4}}{z}.
$$
This increasing saturation is $C^4$ at its guard and strictly below $R$. The whole new three-dimensional endpoint chord $D$ has $|D|\le T-.005$, positive axial component greater than $.15$ and is identically the old chord at phase zero. The construction thus pays the strict length condition on every original cell at both ends for all $\theta$, even when the unmodified rigid rim would fail it. The source reports the actual rigid excess, clipped excess and physical cap displacement separately.

Let $w(u)=16[(u/T)(1-u/T)]^2$. On the unit sphere flow $U_0$ for time $w(u)$ by the vector field $\xi-(\xi\cdot U)U$, for a constant three-component meridian parameter $\xi$. Its explicit value is
$$
 p=\frac{\tanh(w|\xi|/2)}{|\xi|}\xi,\qquad
 U_\xi=p+(1-|p|^2)\frac{U_0+p}{|U_0+p|^2}.
$$
At $\xi=0$ use the smooth limit. Both endpoint directions and their first $u$ derivatives are preserved because $w=w'=0$ there. For each finite $\xi$ the new tangent has length one at every $u$ and the denominator is nonzero. In the local oriented frame $\xi$ is constant only along an individual meridian; the physically solved controls vary around the real section and with phase.

The map $\Phi(\xi)=\int_0^T U_\xi\,du$ extends continuously to the radial compactification of $\mathbb R^3$, with boundary value $T e$ in direction $e$. For any sequence of parameters tending to infinity in direction $e$, at almost every $u$ we have $w(u)>0$ and $U_0(u)\ne-e$, so the integrand converges to $e$. The exceptional angular levels have measure zero: the corrugation is analytic and nonconstant on each complete open piece, and the standard turn is strictly monotone inside. Bounded convergence and compactness of the direction sphere give the extension, including uniform convergence near infinity. Its boundary has degree one about any $|D|<T$. If $D$ were missing, radial projection from $D$ would extend that degree-one map to the ball, contradicting its boundary degree. Thus a true full-meridian parameter exists for every registered chord. At phase zero $\xi=0$ has Jacobian $\int w(I-U_0U_0^T)\,du$ positive definite, since the true old velocity is not confined to a line. The implicit function theorem gives the actual smooth initial solution for the whole circle. This particular nonlinear three-parameter flow does not, by degree alone, select a single continuous global root for all later phases.

For numerical realization, at each of the three full angular resolutions solve all three components at each periodic angular station and fit a periodic cubic to the actual controls. Record every residual's worst address, every coefficient array's length and whole hash, and independent interleaved chord residuals. Define the actual two caps from the integrated meridian endpoints, including their possibly nonzero off-node discrepancy from the intended clipped targets. In their outer charts add the full endpoint vector difference from the translated retreated R760 cap, with the same $\rho$ fade as in section 3; use that actual translated retreated cap on the Cartesian overlap. The terminal velocity is still $-N_0$ and its derivative zero, while the correction is constant in the inward coordinate near the rim. The full two-jet join therefore holds even before an endpoint residual becomes small. Integrating each signed actual tangent gives $g_{vv}=1$ at the continuum level for any smooth angular controls. Its $g_{ss}=|F_s|^2$ and $g_{sv}=F_s\cdot U$ remain independent prices; finite quadrature also has a measurable price. The ring at $E$ is a free interior value of this construction.

## 6. Whole physical search and scope

The two normalized responses and the two whole-meridian shooting responses have four independent natural processes. Each has three physical and angular resolutions, seven fitted phases, the six intervening independent phases and all eleven closed material charts. Each level first retains its complete independent geometric study, with separate angular, mixed and meridional prices, closure root, signed six-jet seams, actual Gram/principal/support readouts and the symmetric cap-chord test. Each then performs the whole three-component physical fit with the original R764 free central, shoulder and cap coordinates and the true stationary-grip mask. The phase-zero field in both paths returns the original R764 field directly, including all curved caps and marks. The search monitors both standard rolls and the cap transition at every resolution; neither the meridian shooting nor the normalized pitch is substituted for those material domains.

Only the runner stores the full coefficient words. The versioned sources, parameters, per-experiment compact conclusions with raw identities and routine public run identify the computation. The full Gram, global embeddedness and later reach, all-pairs thickness and quantitative rigid-motion-quotient displacement remain independent conditions. A necessary interface obstruction for the normalized guide does not restrict a free fitted central trace; signed containment of the witness for that guide is not a certificate on a later freely corrected image.
