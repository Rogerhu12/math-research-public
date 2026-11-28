# R732 — A rounded cap with exact terminal metric, two-sided normal balls and a full strong-held reference

2026-11-28. **Proved.** We give an explicit new closed reference for the same fixed R690 metric, physical meridian length $S$, Fejér core, cap radius and declared height as R730. On both terminal material collars of width $1/1000$ the complete first fundamental form is exactly the prescribed metric, including the full infinite deep tail. At all phases every pair involving a cap passes the two-sided normal-ball inequalities of radius $.126$, with either point as base. The same inequalities hold among all points in a single rounded terminal end (from the flat disk to the bottom of its vertical collar). The full closed family is embedded, $C^2$, has $D\le4.2$, strong held displacement $>.91$, and $\delta_{\rm E}>0$. The core acceleration is corrected for the noncircular chart. No metric or reach bound for all remaining active pairs is inferred. This is a different reference from run 34.

## 1. Exact data and backward terminal coordinate

Use the fixed seven-mode dyadic $\Gamma=p n+p't$, $\Gamma_\varphi=\rho t$, $\Theta'=\rho$, $e=e_r(\Theta)$ of [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) and the scalars of [R730, §§3–5,9.1](R730-whole-image-safe-cone-and-unit-speed-contracted-reference.md). The target is $ds^2+a_{\rm deep}(s)^2d\Theta^2$. All decimals used for bounds below are terminating rational numbers. We use
$$
 2.37<S<2.38,\quad 1.94<H<1.95,\quad 9/16<R<.57,\quad
 .439<Y<.44,\quad X<1.4,\quad C_\Gamma:=\sup|\Gamma|<1.43,\quad
 \sup|\Gamma-Re|=X-R<.8375.
 \tag{1}
$$
Also $0<k_0<1/4$ is the actual initial-law dyadic, $a(0)=1$, $a_s(0)=0$, $a_{ss}(0)=k_0$. Set
$$
 \tau=.126,\qquad d=.14,\qquad b=.001,\qquad h_T=.26 .
 \tag{2}
$$
The backward material coordinate at the upper cap is $u=S-s$. Write $\beta(u)$ for the **actual fixed** R690 angle. On $0\le u\le2b$ it satisfies $\beta(0)=\beta'(0)=0$, $\beta(u)>0$ for $u>0$, $|\beta'|<1$, and
$$
 a_{\rm deep}(S-u)=R+\int_0^u\cos\beta(v)\,dv.
 \tag{3}
$$
Indeed the original out width is binary64 $.02> .019$; hence $2b$ is inside its first eighth. The exact deep exponential with all its turns and the derivative bound are [R690, §§2–2.3](R690-quasimonotone-tail-and-deep-valley-input.md), equations (3)–(7). The reference height here is anchored at the declared $H$, a constant translation in (3)'s corresponding height primitive.

## 2. Rotate a controlled tangent from the accurate tail to a vertical cylinder

Let $S_5(v)=10v^3-15v^4+6v^5$ on $[0,1]$, extended by zero on the left and one on the right. It is nondecreasing and $\int_0^1S_5=1/2$. Define a tangent angle $\alpha$ with $\alpha(0)=0$. On $[0,2b]$ put $\chi(u)=S_5((u-b)/b)$ and prescribe
$$
 \alpha'=(1-\chi)\beta'+\chi/d .
 \tag{4}
$$
Thus $\alpha=\beta$ up through $b$. On the whole interval $|\alpha'|\le1/d$. Moreover
$$
 \alpha(u)=(1-\chi(u))\beta(u)+\int_0^u\chi'(v)\beta(v)\,dv
                      +d^{-1}\int_0^u\chi(v)\,dv .
$$
Therefore $\alpha(u)>0$ for $u>0$, including the interval where $\beta'$ oscillates in sign. Put $A=\alpha(2b)$, so $0<A\le2b/d$. Follow (4) by a constant-curvature interval $\alpha'=1/d$ of length $d(\pi/2-A)-b/2>0$. Then use $\alpha'=(1-S_5(v))/d$ for another interval of length $b$, with $v$ its affine parameter from zero to one. At its end $u_f$ the angle is exactly $\pi/2$ and the curvature is zero. Set $\alpha=\pi/2$ afterwards. This gives $0\le\alpha\le\pi/2$, with $\alpha>0$ except at $u=0$, and
$$
 0\le u_f-d\pi/2=5b/2-dA\le5b/2 .
 \tag{5}
$$

Use actual arclength for this meridian, and define
$$
 x(u)=\int_0^u\cos\alpha,\qquad h(u)=\int_0^u\sin\alpha,\qquad
 P(u,\varphi)=((R+x(u))e(\varphi),\, H-h(u)).
 \tag{6}
$$
In (6) $e(\varphi)$ always means $e_r(\Theta(\varphi))$. For either $f=\sin$ or $f=\cos$ one has
$$
 \int_0^{u_f}f(\alpha)\,du
 =d\int_0^{u_f}f(\alpha)\alpha'\,du+\int_0^{u_f}f(\alpha)(1-d\alpha')\,du.
$$
The first term is $d$ by the endpoints, even if the angle reverses in the original tail. The second lies in $[0,u_f-d\pi/2]$. In particular both $x_f=x(u_f)$ and $h_f=h(u_f)$ are in $[.14,.1425]$. Continue the vertical cylinder for exactly $h_T-h_f>0$. At the bottom of this terminal portion set
$$
 L=u_f+h_T-h_f,\quad R_v=R+x_f,\quad Z=H-h_T,\quad Q=R_v e+Ze_z.
$$
Equations (1),(5) and $3.14<\pi<22/7$ give
$$
 .33<L<.35,\quad .7025<R_v<.713,\quad 1.68<Z<1.69,\quad
 2.02<S-L<2.05 .
 \tag{7}
$$
In the inward orientation, from core toward cap, the data at $Q$ are tangent $+e_z$ and second meridional derivative zero, and the circular section has radius $R_v$. At the cap the tangent is $-e$ and second derivative is zero. Equation (3) proves exact angular length on $u\le b$; the unit meridian is in the radial/vertical plane, so its scalar product with the angular tangent is zero. Thus **all three** target Gram entries hold there, including after the material phase shift $\Theta\mapsto\Theta-\pi t/2$ and the compensating spatial rotation. The induced angular radius farther along (6) is $R+x(u)$; no equality with $a_{\rm deep}$ is asserted outside the unchanged portion.

## 3. Two-sided rolling on the whole rounded end

We give the pointwise chord estimate because a principal-curvature bound alone cannot rule out R731's close second sheet. Consider any plane unit-speed meridian with tangent angle in a fixed interval of length $\pi/2$, and $|\alpha'|\le1/d$. Both directions of traversal are allowed. At a chosen base set tangent-normal coordinates $(X,Y)$ for the chord from that base, oriented initially along the direction of traversal. Then $X$ is nondecreasing, since the relative tangent angle $\lambda$ is between $-\pi/2$ and $\pi/2$. Along the arc,
$$
 \left|\frac{d}{du}\sin\lambda\right|\le d^{-1}\cos\lambda
                   =d^{-1}\frac{dX}{du},\qquad |\sin\lambda|\le X/d .
$$
For $X<d$ this implies $\cos\lambda>0$ and $|dY/dX|\le X/\sqrt{d^2-X^2}$. Integration from the base yields $|Y|\le d-\sqrt{d^2-X^2}$, hence $X^2+Y^2\ge2d|Y|$. For $X\ge d$ the latter inequality follows from $X^2+(|Y|-d)^2\ge d^2$. This proves both normal balls, including endpoints and both choices of base. It requires no monotonicity of $\alpha$. Apply it to (6) with a straight horizontal radius of the flat disk adjoined at the cap and a vertical straight piece at the bottom.

For the surface of revolution put $r=R+x$ on the roll and let the flat radius run down to zero. For radii $r,r'$ and two azimuths differing by $\omega$, the horizontal angular change adds $2rr'(1-\cos\omega)$ to the squared meridional chord. Its extra contribution in absolute value to $2d$ times the normal chord projection at the first base is at most $2d|n_r|r'(1-\cos\omega)$, where $n_r$ is the radial component of the unit surface normal there. At a flat base $n_r=0$; otherwise $r\ge R>d$. The extra squared length covers this contribution. At the disk center the normal is vertical and the formula extends directly. Therefore all chords in this unmarked end pass the two-sided radius-$d$ tests for either base.

For the actual p4 disks of [R716, §4](R716-asymmetric-fixed-caps-and-centred-volume-moment.md), a marker and any point of the roll/cylinder are horizontally separated by at least $R-.2>.36>2\tau$. The same is true if the marker is the base. Any two points of the same marked cap pass the tests directly as follows. Its entire disk is a graph with disjoint compact bumps $m(1-r^2/B^2)^4$, where $m=.001$, $B\ge.04$. Its Hessian in the tangential/radial principal axes has eigenvalues $(8m/B^2)$ times $-(1-v)^3$ and $(1-v)^2(7v-1)$, $v=r^2/B^2$. Each modulus is at most one after removing the common factor: the radial expression ranges from $-1$ to $(4/7)^2\cdot2<1$ (its interior maximum is at $v=3/7$). Outside supports the Hessian is zero and extends continuously across their boundaries. Hence $\|D^2 f\|\le5$. On the disk's convex footprint Taylor's formula gives $|n_p\cdot(q-p)|\le(5/2)|q-p|^2$ at every actual cap base, in either order. This pays radius $\tau<1/5$. Flat cap points paired with the roll were covered above. Opposite ends have vertical separation at least $2Z>2\tau$. The assembly below places the entire central band in $|z|\le Z$, so its gap to either actual cap, including the outward markers, is at least $h_T=.26>2\tau$. For chords of length at least $2\tau$ the two-sided test is immediate at either base. These arguments cover **every** pair involving an actual cap point, and every pair contained in the same rounded end; they do not delete the unresolved pairs between the central band and its adjoining end.

## 4. A full central unit-speed band fitting the new terminal data

Take $\eta=1/512$, $\lambda=(5/4)k_0\eta^2<1/800000$. The six quintic Bernstein controls are
$$
 \Gamma,\quad \Gamma+\eta e_z,\quad \Gamma+2\eta e_z+\lambda\rho n,\quad
 Q-2\eta e_z,\quad Q-\eta e_z,\quad Q .
 \tag{8}
$$
The core horizontal second jet has been changed from R730's $k_0e$ to $k_0\rho n$, the exact fixed-metric necessary value in [R7](R7-core-witness-initial-acceleration.md). In fact the end velocities in Bernstein parameter are $5\eta e_z$ at both ends, and the second derivatives are $20\lambda\rho n$ and zero. After arclength division by $25\eta^2$, the first becomes $k_0\rho n$. This also corrects the core Gaussian curvature to $-k_0$, since the other principal curvature, with outward normal $n$, is $-1/\rho$, and the mixed coefficient vanishes. For the original R730 reference the core value instead equals $-k_0\cos(\Theta-\varphi)/\rho$ by its literal (18). Those computations are about the specified cores and do not address a modified outer field.

The ordered heights in (8) are $0,\eta,2\eta,Z-2\eta,Z-\eta,Z$, strictly increasing, so $z_t>0$ on the whole central band. Let $b_c(t,\varphi)$ be the horizontal Bernstein polynomial. All controls lie in the R730 cone $|y|\le Y_c+z/5$, $Y_c=Y+.005$, and the ball of radius $2.099$. Indeed $\rho<7$ by R717, giving core horizontal perturbation $<.00001$, and the upper controls have radius $R_v<.713$ and height at least $Z-2\eta>1.67$. Their cone allowance exceeds $.439+.005+1.67/5>.77$. The core controls have norm at most $\sqrt{(1.431)^2+(2\eta)^2}<2.099$. The three upper controls and the whole unmarked terminal portion lie in that ball by $.713^2+1.95^2<2.099^2$. The entire terminal portion lies in the cone because its height is at least $Z$. The reflections and original p4 will be handled as in R730.

For completeness, angular regularity of the new perturbation must be checked. Write $C=B_0^5+B_1^5+B_2^5$, $E=(1-C)R_v$, $b_0=C\Gamma+Ee$, $v=\lambda B_2^5\rho n$, so $b_c=b_0+v$. R717 dyadic bounds give $\rho>1/5$, $\rho<7$, $|\rho'|<32$. For the last inequality the ideal Fourier bound is $\sum_{j=1}^7(3/8)j(8-j)=31.5$, and the dyadic error is at most $2^{-53}\sum_{j=1}^7 2j(4j^2-1)<.5$. Thus
$$
 |v|\le .001C,\quad |v_\varphi|/\rho\le .001C,\quad
 |b_0|\le2C+E,\quad |(b_0)_\varphi|/\rho\le C+E .
$$
By R730 (26),(27) the unperturbed determinant divided by $\rho$ is at least $C^2p+E^2$, $p>.439$; $C,E\ge0$ do not vanish together. The perturbation costs at most $.004 C^2+.002 CE$. Using $2CE\le C^2+E^2$ proves strict positivity everywhere. In particular each section is nonzero, winds once by continuity from the core, and is strictly star-shaped.

Use the original $\psi=[1-(2t-1)^{12}]^7$ and trial horizontal contraction $(1-\xi\psi)b_c$, with $\xi\in[0,3/4]$. It preserves the cone and ball. Let $\mathcal L(\xi,\varphi)$ be the full central length. We must hit $S-L$, *not* $S$. By (1) and (7),
$$
 |R_v e-\Gamma|\le .8375+.1425=.98,\qquad
 |Q-\Gamma|\le\sqrt{.98^2+1.69^2}<1.96 .
$$
The complete spatial control polygon length is bounded by $|Q-\Gamma|+8\eta+2\lambda\sup\rho<1.98<2.02$. To see the count, the first two chords cost at most $2\eta+\lambda\sup\rho$, the central chord at most $|Q-\Gamma|+4\eta+\lambda\sup\rho$, and the last two cost $2\eta$. This proves $\mathcal L(0,\varphi)<S-L$ uniformly.

For the opposite endpoint put $t_0=1/8$. The three chords through $0,t_0,1-t_0,1$ bound the length below by
$$
 Z+(3/4)\psi(t_0)(|\Gamma|+R_v)-E_0 ,
$$
where $E_0$ is the sum of the uncontracted horizontal discrepancies from the corresponding endpoints at $t_0,1-t_0$, plus $z(t_0)+Z-z(1-t_0)$. This is R730 (43c,d)'s triangle inequality applied to (8). Here the far-side Bernstein mass at either endpoint is $526/32768$, hence
$$
 E_0\le 2[(526/32768)\,.98+\lambda\sup\rho]
       +2[2\eta+(526/32768)1.69]<.1.
$$
Since $|\Gamma|\ge p>.439$ and $\psi(t_0)>97/125$, the lower bound exceeds $1.68+(3/4)(97/125)(.439+.7025)-.1>2.05>S-L$. Strict positive speed follows from $z_t>0$. Convexity in $\xi$, the secant derivative bound at the crossing and the implicit theorem as in R730 §§8–10 now give a unique positive analytic periodic root, common total central length $S-L$, and accurate inverse arclength. Analyticity follows locally by integrating analytic positive-speed data over a fixed compact interval and applying the analytic implicit function theorem. The central patch is embedded by strict monotone height and star-shaped sections since contraction multiplies their angular determinant by $(1-\xi\psi)^2$. The pulse's endpoint derivatives through order six vanish. At $Q$ the complete two-jet agrees with the terminal vertical cylinder: positional radius $R_v$ and fixed angle $\Theta$, unit vertical meridian, zero radial acceleration and zero mixed derivative. At the core the reflected halves glue in $C^2$ by (8). At the cap (3) and flatness at zero give the complete flat-disk jets. Reflection and rotation preserve these statements. The stacked height ranges have disjoint interiors; each matched boundary is the same single circle.

## 5. Whole-family geometry, noncongruence and remaining work

Use R730's unchanged material phase shift and spatial rotation on the activity, with the same fixed marked caps. The $C^2$ frames glue at each seam and depend continuously on phase in the $C^2$ topology by uniform continuity of their derivatives on the compact material domain (using the same rim atlas as R730). The positional cone and its reflection cover the complete base image, including both fixed caps and markers, since p4 extends the height only outward. The two opposite rotated core points thus have distance $>.91$ from the entire base image by R730 (6)–(12). The unmarked radius bound $2.099$ and marker height $.001$ give $D\le4.2$ for the complete reference, and its fixed grip diameter $.9$ exceeds $D/5$. All cap and terminal mutual chord inequalities proved in §3 hold for every phase, with $\tau=.126\ge .03D$.

There is also a full-image noncongruence conclusion, independently of central Gram. The open central annulus is a connected real-analytic parametrized surface. If any open subpatch lay in a plane, the scalar plane equation would vanish on the whole central annulus by analytic continuation and on its boundary by continuity. The core contains three noncollinear points at height zero, whereas $Q$ has height $Z>0$. This is impossible. In the rotational end, a plane containing an open patch would contain an open circular arc at each nearby $u$. A plane containing such an arc must be its horizontal plane, whereas $h$ is strictly increasing for $u>0$. Seams do not contain a two-dimensional open set. Hence activity has no planar germ. Together with the four disjoint p4 support circles of distinct radii and affinely independent centers from [R661, §4](R661-complete-nonplanar-activity-and-four-fixed-markers.md), [R238](R238-planar-germ-marker-rigidity.md) forces any Euclidean congruence between complete phases, including reflections, to be the identity. The end phase differs from the base by the two held witnesses. Compactness of orthogonal transformations and boundedness of translations in a hypothetical zero-distance aligning sequence show that their Euclidean quotient Hausdorff distance is strictly positive. Exactly the same analytic-plane argument also gives $\delta_{\rm E}>0$ for the original frozen R730 reference: its full upper activity is analytic, its core is noncollinear, its cap rim is at positive height, and R730 already proves its closed embedding and held witnesses. Neither result evaluates the quantitative maximum of the quotient distance.

The middle and the non-original part of the rounded end still require the prescribed angular metric. The remaining global radius tests concern central/central and central/rounded-activity pairs (the pair reversal is included). A changed outer field has to establish its own relations to its actual cap and normal coordinates. This construction changes the physical program, and gives no runtime value, source identity, or root for run 34. Original full solver dimensions, budget, complete-field refinement, and deliverables remain unchanged. No scientific code, integration, mesh or optimizer was executed for this proof.
