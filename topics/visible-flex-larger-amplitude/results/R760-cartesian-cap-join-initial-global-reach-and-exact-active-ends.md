# R760 — A Cartesian cap join, a strictly thick new initial sphere and finite exact active curved ends

2026-11-28. The [original R758 obstruction](R760-original-R758-cap-intrinsic-curvature-obstruction.md) concerns the previous intrinsic metric. Here a different, explicit initial field has whole-image reach at least .132, diameter below 4.01 and stationary marked grip diameter at least 1.40. The closed physical baseline has held distance above 1.09 from its initial to final images. Its two active right rolls and genuine cap collars keep the new metric exactly through the full phase interval with both principal curvatures bounded by $1/.132$. The whole middle annuli and their global metrics remain active parts of the physical search.

The [complete section, collars, Cartesian bowls and spatial jets](../scripts/resume_20261126/r760_cartesian_curved_crown_and_lower_rate_walls.py) and [whole signed physical fits](../scripts/resume_20261126/solve_r760_curved_crown_middle_annuli.py) define this construction. No finite solver residual is asserted here.

## 1. Slower return elbows on the same genuinely stationary circular grip

Keep the R754 height .71, upper circular grip of radius .15, coherent advance $\delta=.15\theta$ for $0\le\theta\le.90$, whole rigid left wing, and four marked stationary rings. The new upper right straight track cut is at $z_c=.92$ initially and $.92-\delta$ subsequently, below the old constant-abscissa right track end at height $>1.27$. Give the upper wall fixed length .95. Take the four R756 softened heading changes $0\to A\to0\to -B\to0$ with $A=1.44,B=.71$, angular rate $k=5.4$ and two $S_5$ speed ramps of width $.0004$ on each change. Each change of magnitude $b$ occupies $b/k+.0004$. Insert .06 at maximum positive heading and .001 at the final zero heading. Fill the remaining positive length at heading zero at the *beginning*. These are unit-speed physical arcs joined to the straight track with zero curvature. The lower wall reflects the upper.

The height equation is $\int\cos(\lambda T_*)=.92-\delta$ with fixed template $T_*$. Its mean decreases strictly up to $\lambda=1$. There the total loss from .95 is at least
$$
 2(A-\sin A+B-\sin B)/k+.06(1-\cos A)>.238 .
$$
The initial and final required losses are .03 and .165. A unique smooth $\lambda_\theta>0$ exists. Since $1-\cos(\lambda t)\ge\lambda^2(1-\cos t)$, $\lambda_0<.356,\ \lambda_\theta<.833$ and $|\kappa_0|<1.93,\ |\kappa_\theta|<4.5$ on the active wall. In particular $\kappa_\theta=a\kappa_0$ exactly there, with $a=\lambda_\theta/\lambda_0$.

The right-wall support estimate can be made independently of that used on the old steeper wall. The final positive horizontal displacement at any amplitude is at least
$$
 \lambda[2(1-\cos A)/k-B^2/k-2(.0004) B]>.226\lambda .
$$
During the negative lobe it is always at least this equator value. The total negative lobe plus bottom dwell has length $<.266$. At absolute scaled heading $\lambda\beta$ at least $\beta/k$ of it has been spent; hence $z|\sin(\lambda\beta)|\le\lambda k(.266)^2/4<.096\lambda$. Around $c=(u_*+.15,0)$ the negative lobe therefore has support at least $(.149+.226\lambda)(1-.253\lambda^2)-.096\lambda\ge.149$. In the positive lobe $\sin\tau\le k\lambda z$ as in R756 and support is at least $\min(.149,1/(k\lambda))\ge.149$. The wall remains a strictly descending graph, at $x\ge x_R$. The other original section pieces have support $\ge1/7$ and curvature magnitude $<7$. The signed section period, angle lifts and upper/lower arclengths are computed from this new .95 wall and .92 cut. This gives a closed simple profile through every phase.

## 2. The new initial caps in true physical plane coordinates

Let $L=.132\pi/2+.0005$ and $d_b,p_b\in[.132,.1325]$ be the true end arclength and offsets of the original standard rolls. The terminal plane domain at zero phase is bounded by the regular inward parallel $\gamma_0-d_b n_0$. In the plane collar use the actual distance $0\le w\le W=.007$, so its location is $X=\gamma_0-(d_b+w)n_0$. On the upper cap set
$$
 y=1+p_b+h_*S_7(w/W)+\epsilon A(s)b(w/W),
 \quad h_*=1.5\,10^{-6},\quad\epsilon=10^{-9},\quad b(t)=t^3(1-t)^3 .
$$
The lower cap uses the opposite sign. The bump is zero outside $[0,1]$; $A=(1-\chi)\exp[(\gamma_{0,x}+.3\gamma_{0,z})/2]$ and the smooth $\chi$ is the R756 right-wall projector, equal to one on the entire active right wall and .10 of adjoining straight tracks and zero .30 above the cut. The degree-seven clamped step has zero first and second derivatives at its ends. Beyond this collar the plane height is the constant $p_b+h_*$ plus the following compact Cartesian graph on each sign.

Put $c_x=u_*+.15,\ q=[(x-c_x+.49)/.494]^2+(z/.22)^2$. The whole common inner ellipse is $q\le1$. Define
$$
 B(x,z)=2.5\,10^{-5}(q-1)\,[1-S_7((q-1)/.014)] .
$$
This quadratic bowl has constant boundary height zero on the *whole* ellipse. The extension uses the genuine Cartesian quadratic $q$ and is zero for $q\ge1.014$. Its support does not reach the terminal collar: $|z|<.222$, $x\le c_x-.49+.494\sqrt{1.014}<c_x+.0075$, while the right offset boundary throughout the collar has $x\ge c_x+.149-.14=c_x+.009$. The left offset wall remains at $x<-.874$ and the nonvertical main sheets are outside this low strip, as in R758. In particular this is a single Cartesian graph over the disk with disjoint collar and bowl features.

We give explicit global bounds for the original graph Hessian. On the collar $\ell=1-(d_b+w)\kappa_0>.02$ and $|\kappa'_0|<30000$ by the actual section ramps. For the .15-radius R744 turn ramps use $1.875/(.15\cdot.001)=12500$, on the R740 bend use the larger physical bend width, on the four right heading ramps use $5.4(1.875)/.0004<25400$, and on the old left sinusoidal wall differentiate (1) of R754 with its .01 clock margin. Put $H=h_* S_7+\epsilon A b$ as above. From the explicit cutoffs $|S_7'|\le2.188,\ |S_7''|<8$, $|A|<3, |A'|<36, |A''|<650$, $0\le b\le1/64$, $|b'|\le3/16$, $|b''|\le2$. These imply
$$
 |H_w|<.00048,\ |H_{ww}|<.246,\ |H_s|<5.7\,10^{-10},\
 |H_{ss}|<1.1\,10^{-8},\ |H_{sw}|<10^{-6}.
$$
In an orthonormal frame of the actual projection plane, the pure transverse Hessian is $H_{ww}$. The mixed entry is bounded by $|H_{sw}|/\ell+7|H_s|/\ell^2$, and the tangential entry by $|H_{ss}|/\ell^2+.14(30000)|H_s|/\ell^3+7|H_w|/\ell$. Consequently its operator norm is below .5, also at the one-sided seams by continuity.

For the Cartesian bowl $|\nabla q|^2\le4(1.014)/.22^2<84$ on its support and $\|\nabla^2 q\|<42$. For $t=q-1$ the cutoff $t(1-S_7(t/.014))$ has absolute first derivative $\le3.188$ and second derivative $\le(4.376+8)/.014$ wherever it changes. Thus $\|\nabla^2 B\|<1.87$ and $|\nabla B|<.00074$. The original cap graph has $|\nabla H_{\rm cap}|<.00075$ and both absolute principal curvatures below 1.87 everywhere. On either cap, relative to $c$ its outward support exceeds 1.10 using the transverse height $>1.13$ and projected distance to $c$ below 2.3. These estimates are in physical coordinates, including exactly the former R758 high-curvature location and the separate thin normal collar.

The original entire cylinder, real rolls, marks and cap seams have support at least .132 and both absolute principal curvatures at most $1/.132$. On the standard rolls use the original section bound 7 and $d(v)\le.132(1-\cos\alpha)+.0005$ as in R754; on the four tiny grip marks use their strict original margins. The cap graph has zero derivative and second derivative matched to the terminal roll. The full closed image is embedded by the nested regular section parallels, filled graph disks, and opposite positive/negative transverse heights. The normal-flow criterion of [R723](R723-directional-normal-flow-support-reach.md) gives **whole-image initial reach at least .132**. At zero amplitude of the external phase the right wall has outward excursion below $\lambda_0[A^2/k+.06A+2(.0004)A]<.17$, and $|z|\le.92$, so it does not enlarge the R754 bound 1.64 on planar radius. Together with the tiny original cap heights this gives $D_0<4.01$, hence $.132>.03D_0$. The stationary grip diameter is at least 1.40. This calculation establishes the requested initial thickness on a new actual metric.

## 3. Finite isometry on both active rolled and curved parts

Write $C=1/a$ on the actual complete right wall. On each roll take $D=Cd$ and $P_\theta'=\sqrt{1-C^2\sin^2\alpha}$. On the true cap collar take
$$
 D=C(d_b+w),\qquad
 P_\theta=P_\theta(L)+\int_0^w\sqrt{1-C^2+f'(t)^2}\,dt,\qquad
 f(w)=h_* S_7(w/W).
$$
Before the common rotation the field is $(\gamma_\theta-Dn_\theta,\pm(1+P_\theta))$. The angular length factor is exactly $1-(d_b+w)\kappa_0$, the cross term zero, and the transverse squared length $1+f'^2$ equals the original graph metric. At $\theta=0$, $f'\ge0$ selects the original branch; at $w=0$ the two-jet joins the real roll. The initial collar has
$$
 K_0=-\kappa_0 f'f''/[(1-(d_b+w)\kappa_0)(1+f'^2)^2].
$$
For a nonzero curvature label $K_0$ is nonzero immediately after the rim, and vanishes at the intermediate inflection $w=W/2$ without containing a flat neighborhood. On initially straight main pieces the $w^3A(s)$ term separately gives negative leading Hessian determinant wherever $\chi=0$ as in R758. No planar-ruling continuation across an entire intervening cap follows.

The full true right angular curvatures on the rolls and the exact cap bands have magnitude $\le4.5/(1-.14\cdot1.93)<6.18$. The meridian turn angle on the roll is $\arcsin(C\sin\alpha)$ with derivative of magnitude $\le|\alpha'|\le1/.132$. On the curved cap the absolute meridian curvature is $C|f'f''|/[(1+f'^2)^{3/2}\sqrt{1-C^2+f'^2}]\le |f''|<.246$. At $C=1$ use the continuous original graph formula. These are finite all-phase bounds on the named actual sectors, not a whole-image reach estimate after $\theta=0$.

Outside the exact right region put $C(s)=\cos[\chi(s)\arccos(1/a)]$, and join through the true neighboring straight track as in R756. In the cap use the R758 collar clock $j=w$ through .007, then $j'=1-S_5((w-.007)/.001)$ until constant $.0075$. Replace $w$ by $j$ in the outer formulas. Use the true time-zero final-offset angle lift for the common elliptical labels, avoiding an artificial angular twist of the zero-phase cap. Let $r,R$ be the actual projected point and outer-leaf radii about $c$ and $r_E$ the common ellipse radius. After the inner angle interpolation is complete, use the *physical fraction*
$$
 T=\frac{r-(.87/.82)r_E(\phi)}{R-(.87/.82)r_E(\phi)},\qquad \eta=S_7(T/.80).
$$
Earlier in the angle interpolation set $\eta=0$ (the source uses the positive outer-angle denominator and a nonpositive numerator). The R758 strict ellipse enclosure applies since the new right support is at least .149 and true effective offset at most .14. This guarantees a positive denominator and exact outer height on the true collar. Continue the incoming normal slope by the height correction $-\tan\psi\,n_\theta\cdot(X-X_{\rm outer})$ on the annular side, where $\psi=\arccos C$. Interpolate this continued outer height and an inner rigid transverse shift with $\eta$, and add the same Cartesian bowl $B$. At phase zero the meridian plateau, the zero slope and zero shift give *exactly* the physical original graph of §2, independently of this interpolation clock.

Where $\eta>0$ both planar positions are on the same ray, the current one inside and the true section normal has positive support on the outer leaf. The slope term therefore increases the absolute transverse height there. The opposite signed filled disks stay separated. The baseline sphere remains embedded and its cap projections stay inside the true section. The original left wall point has distance $>1.09$ to the entire final baseline using the R754 half-plane proof and the fixed genuine upper circular grip. This compares closed images at phases 0 and .90. The unfixed annular and transition curvatures remain actual costs after the initial phase.

## 4. Full new physical solve

Both signed ends and both choices of exact or free outer data are fitted on this sole new zero-phase metric, with the full three resolutions, seven fitted phases and six intermediate checks from R758. The physical curve, true cap and original metric are all recomputed. Fifteen extra localized functions of the *initial spatial* $(x,z)$ coordinates enrich each of the angular/radial correction packets in all three spatial components. Before fitting, the whole rigid crown also receives an independent genuine $SE(3)$ registration on each phase and half: 24 complete original radial rim-to-crown paths and $24^2$ continuations inside the convex quadratic ellipse put explicit upper bounds on the corresponding new chords. A six-coordinate rigid motion fits the positive excesses, with weak regularization, using its full finite rotation matrix. This yields a physical initial candidate at every phase and may be further translated. The complete curves at intermediate phases use quintic time interpolation of the rotation vector and all physical mode coefficients. The strictly demonstrated embedding and initial reach in §2 concern the stated family; later numerical poses and shape corrections need their own full verification.

The scanner also evaluates the actual Cartesian gradient, Hessian and Gauss curvature of the *old* and *new* entire physical fields at their corresponding right-equator $\rho=.84$ points, at all seven phases. The four true branch sources retain every previously prescribed grid, original phase, full result and fit budget. Their returned finite outcomes are registered independently of the intrinsic obstruction of the old metric or the positive initial reach of the new metric.
