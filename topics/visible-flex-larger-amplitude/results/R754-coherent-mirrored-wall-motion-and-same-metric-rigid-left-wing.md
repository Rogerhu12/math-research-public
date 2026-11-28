# R754 — Coherent mirrored sliding, a real wall shortcut, and its same-metric whole-wing correction

2026-11-28. We construct two finite phase families on **one new initial metric**. The first moves both closing walls. Its upper and lower principal horizontal sheets slide in the same direction, paying their entire cross-cap Euclidean bridge, but it has a different shortcut on the left wall. In the second family the complete initial left wing undergoes one rigid translation before the eccentric spatial rotation. This pays the same initial metric on the complete left cylinder, both matching rolls, and the parts of both full cap disks at original $x\le0$, including the failed wall and its entire shortcut. Both families still have an unsolved right-hand region. The common phase range is $0\le\theta\le.90$; none of the $\pi/2$ held estimates from R746 are used.

The [entire physical two-jet source](../scripts/resume_20261126/r754_coherent_mirror_bowed_walls_two_jets.py) and the [whole-cap bridge registration](../scripts/resume_20261126/r754_translate_complete_cap_bridge.py) accept the same option for the two moving walls or the corrected rigid left wing. Their exact integral definitions give closed $C^2$ embeddings with all-phase reach at least .132, $D<4.21$, held distance $>1.09$, stationary grip diameter at least 1.40, and positive Euclidean-quotient distance. The standalone star charts also give the same whole images without switching on cap transport; their cap metrics are a separate baseline.

## 1. Fixed-length walls and coherent upper and lower section labels

Use the upper strong R740 curve of R744, but at height $H=.71$. The radius of its genuine right circular turn remains $r=.15$, the planar turn ramp is .001, and $q=\int_{.30}^{.56}\sin\beta=\int_{.30}^{.56}\cos\beta\in[.13,.184)$. Thus $u_*=.30+q,\ z_*=H+.44+q$. The left quarter-turn and right half-turn and their vertical terminal tracks are exactly those in R744 translated to this upper height. Their track abscissas are $x_L\in[-1.151,-1.149]$ and $x_R\ge u_*+.30-.001$. Reflect the upper shape in $z=0$ for the lower part.

At phase zero cut the upper left and right vertical tracks at $z_L=.41,\ z_R=.60$. Write $b(t)$ for the unit-speed upper arc between the cuts, with its vertical tracks continued a short distance past them. At phase $\theta$ the physical upper material arc is $b(t+\delta)$, $\delta=r\theta\in[0,.135]$. The two cut positions are therefore $z_L+\delta,\ z_R-\delta$. At the left, even $.41+.135=.545$ is strictly below the end of the upper straight track, whose height is at least $H-.15-.001=.559$. The right track stays well above zero. The lower arc uses the reflected point with the *same upper material label*, reversing arclength orientation around the closed curve. On either true horizontal main-sheet segment the physical motion before the common rotation is exactly $x\mapsto x+\delta$, rather than opposite translations on the two sheets.

Join the upper and lower ends of each track by an actually moving wall of fixed material length
$$
 L_L=2(.41+.135)=1.09,\qquad L_R=2(.60)=1.20 .
$$
On the upper half of a wall let $a\in[0,L_i/2]$ measure arclength from its upper cut towards the equator. Fix $\epsilon=.01$. The clock $w:[0,1]\to[0,1]$ has derivative $1/(1-\epsilon)$ except on the first and last intervals of width $\epsilon$, where it is multiplied by the rising or falling $S_5$; set $w(0)=0$. It is symmetric, $w(1-t)=1-w(t)$. With $\tau=A_i\sin(2\pi w(a/L_i))$, define the wall by
$$
 x=x_i+e_i\int_0^a\sin\tau\,da,\quad
 z=z_i(\theta)-\int_0^a\cos\tau\,da,\quad e_L=-1,\quad e_R=1,
 \qquad \int_0^{L_i/2}\cos\tau\,da=z_i(\theta).
 \tag{1}
$$
Reflect about $z=0$ to give the entire wall. Its speed is identically one. The vertical tangent and zero curvature at the attachment match the straight track; the clock guarantees more than the required two derivatives. At the equator the tangent is vertical, with matching curvature under reflection. The lower arc and the two fixed-length walls give one periodic arclength coordinate for all phases.

Equation (1) has a unique $A_i\in[0,1.2]$, including zero at a fully stretched wall. Its normalized mean is 1 at zero and strictly decreases for positive $A$ in this range. To bound it at 1.2, write the clock measure $dt=(1-\epsilon)dw+d\mu$ with $d\mu\ge0$ of mass $\epsilon$. By symmetry the mean on either half is also the full-clock mean. The cosine Taylor bound yields
$$
 \mathrm{mean}\,\cos(A\sin(2\pi w))
 \le .99(1-A^2/4+A^4/64)+.01 .
$$
At 1.2 this is below both minimal prescribed ratios $.82/1.09,\ .93/1.20$. The inverse depends continuously on phase up to both zero-amplitude endpoints. One may use the time coordinate $\theta=.90\sin^2(\pi t/2)$, $0\le t\le1$; the square-root inverse at zero amplitude is then smoothly approached from inside. The curvature is at most $2\pi(1.2)/(.99 L_i)<7$.

For the corrected family translate the *entire initial left wall, its quarter-turn and the adjacent sheet* by $+\delta e_x$. In particular its curvature and its initial bow stay exactly as at zero. Switch to the moving upper and lower main arcs at their material main-curve $x=-.5$. On an open neighborhood both prescriptions are identically $x\mapsto x+\delta$ at the original constant horizontal height, so the join needs no interpolation and changes no arclength. The right wall still uses (1). This is a real change to the central motion; the entire initial material surface is exactly the same in both families.

## 2. The full section, both ends and both filling disks

Let $\gamma_\theta(s)$ denote either new section, with outward normal $n$, $n'=\kappa T$. Use central cylinder $(\gamma_\theta(s),y)$, $|y|\le1$. Make both ends as true inward parallel rolls with radius $r_e=.132$, curvature ramps of length .0005, and arclength $L=.132\pi/2+.0005<.208$. Their meridian angle $\alpha$ turns from zero to $\pi/2$ with the R744 $S_5$ prescription. Set $p'=\cos\alpha,\ d'=\sin\alpha$, and use $(\gamma_\theta-dn,\ \sigma(1+p))$ for $\sigma=\pm1$, with terminal $p_b,d_b\in[.132,.1325]$. Fill both terminal rings by their entire planar disks. Rotate the whole field in $xz$ by $B_\theta$ about the *true* upper circle center $O$ of the new height: $|O-(u_*+.15,z_*)|\le.001$.

Use the fixed planar support center $c_2=(u_*+.15,0)$. Every whole profile has support at least $1/7$. On the main curve it is $(c_{2,x}-u)\sin\beta+(H+v)\cos\beta\ge.15$; in the translated left region only its horizontal part is used. On the right turn the circle comparison gives at least $.15-.001$; the left turn has the same bound since its comparison center is to the left of $c_2$ and has nonnegative height. Translating that whole left turn by at most .135 preserves these two signs. The unbowed track supports satisfy the same bound. On either bowed wall the outward horizontal distance to $c_2$ is at least .149, and the vertical part of its upper normal is $\sin\tau\ge0$. Since $\tau=0$ at the equator, $|\tau'|<7$ implies $\sin\tau\le7\int_a^{L_i/2}\cos\tau\,da=7z$. The lower half is symmetric. Thus the support is at least $.149\cos\tau+\sin^2\tau/7\ge1/7$; the last expression is concave in $\cos\tau\in[0,1]$ and both endpoints suffice. The upper profile runs monotonically in $x$, with positive height until its equator, and the walls are distinct and extend outward. Reflection and the two equator crossings prove simplicity and winding one. The signed curvature everywhere has magnitude $<7$.

All offsets through $d_b+.0015\le.134$ have $1-d\kappa>0$ and support $\ge1/7-d>0$. R744's polar-angle argument proves they are simple and strictly nested, with $\partial_d R=-1/(n\cdot e_{\rm ray})<0$ at fixed ray. The complete plane fills therefore embed. In the source an inward collar first uses $j=w$ up to .001, then has slope $1-S_5((w-.001)/.001)$ up to .002, then zero, with $j_{\rm final}=.0015$. Scale the leaves about $c_2$ by $\rho=1-(w-j)/(1-.0015)$. In the already flat inner part interpolate their scaled radii to $.003\rho$ between $\rho=.70$ and .40, monotonically as in R751 §2. Direction becomes the common $\pi-2\pi s/P$ between $\rho=.35$ and .15 on these circular leaves. Both orientation lifts are strictly decreasing and have degree minus one. The plane core $\rho<.15$ is a common *regular material Cartesian disk*. Throughout the outer collar the zero normal acceleration of the meridian at the seam matches the flat cap. These nine charts evaluate the whole closed sphere, without treating singular polar labels as a second surface.

On the rolls the positional support is $(\sigma_0-d)\cos\alpha+(1+p)\sin\alpha$. Here $\sigma_0\ge1/7$ and $d\le L\sin\alpha$, hence it is $\ge1/7$. The positive angular principal curvature is at most
$$
 \frac{\cos\alpha}{1/7-.132(1-\cos\alpha)-.0005}
 \le\frac1{1/7-.0005}<1/.132 .
$$
This uses $d\le.132(1-\cos\alpha)+.0005$; negative section curvature gives an absolute bound 7. The meridian curvature is at most $1/.132$. Planar caps have support $1+p_b$ and zero curvatures before adding the marks described below, which are on the grip alone.

## 3. Whole-image held distance and noncongruence

The material upper true-circle interval $.10\le\alpha\le1.05,\ |y|\le.70$ is pointwise stationary after $B_\theta$, since its source labels move by $r\theta$ around the true constant-radius circle throughout $0\le\theta\le.90$. Its interior is nonempty, its diameter at least 1.40. Use four distinct stationary height bumps on this patch, without overlapping footprints. Their centers have $(\alpha,y)=(.25,0),(.55,0),(.85,0),(.55,.33)$, and radii $d_i=.002,.003,.004,.005$ respectively. At a grip point $P$ displace along the true circular-cylinder outward normal by
$$
 h_i=10^{-5}d_i^2(1-|P-P_i|^2/d_i^2)_+^3 .
$$
The normal and the whole physical patch remain fixed at every phase. In unit cylinder coordinates the gradient is $\le6\cdot10^{-5}d_i$ and the Hessian norm is $<.00031$, since the squared-distance Hessian in the support has norm at most $2(1+d_i/.15)$ before division by $d_i^2$. On the fixed circular patch the normal graph tangent denominator is $1+h_i/.15$; differentiation in its principal frame bounds the graph curvatures by $6.68$. Its support has loss $<.00001$ while its unmarked support is at least $.149+(z_*-.001)\sin(.20)>.39$. Thus [R723-A](R723-directional-normal-flow-support-reach.md), with transported center $B_\theta c_2$, proves whole-image reach $\ge.132$ at every phase.

These four rims are the only places where the image fails to be $C^3$ in a neighborhood. The unmarked surface across all wall, roll and cap seams is at least $C^3$ by the vanishing ramp derivatives; smooth material relabelings do not change the image. Each rim is the transverse intersection of a sphere and the true cylinder, with nonzero normal third-derivative jump. Each such circle on the cylinder is a nonplanar spatial curve: it contains both $(P_{i,x},y_i\pm d_i,P_{i,z})$, so any containing plane would contain the transverse direction, whereas its $xz$-projection ranges over a nontrivial true circular arc. A nonplanar curve lies on at most one sphere. The four radii distinguish the four rims, so a Euclidean congruence of two whole marked images must fix each one of their four sphere centers. The first three centers are noncollinear in their common plane and the fourth is outside it. Their common rigid stabilizer is the identity.

For the initial diameter all projected end and cap points lie inside the original section. Its planar radius is $<1.64$. On the initial left wall the abscissa deviation from $x_L$ is $\le1.09(1.2)[.99/\pi+.01/2]<.420$ by the clock measure and $|\sin\tau|\le1.2|\sin(2\pi w)|$; its height is at most .41. The initial right wall is straight. On the main horizontal part use $|x|\le1,\ z=.71$; on the later main arc use $|x|<.484,\ z<1.334$. The right half-turn is inside the ball of radius $\sqrt{.634^2+1.334^2}+.151<1.64$; the left quarter-turn and their straight tracks also have smaller norms. Including the negligible mark height and $|y|\le1.1325$ gives $D<2\sqrt{(1.64+.000001)^2+1.1325^2}<4.01<4.21$.

Let $x_m\le-1.149$ be the actual minimum abscissa of the initial planar section, attained on the left wall. In the corrected final left component its corresponding minimum is $x_m+\delta$; in the two-wall reference the stretched straight left wall has minimum $x_L\ge x_m$. All final unrotated points with $x\le.25$ have $z\le H$, by the horizontal sheet and the lower heights on the left wall. The true axis has $O_x\ge.579,\ O_z-H\ge.569$. The new spatial coordinate is $x'=O_x(1-\cos\theta)+x\cos\theta+(O_z-z)\sin\theta$. At .90 its lower excess over $x_m$ on this region is therefore at least
$$
 (.579+1.149)(1-\cos(.90))+.569\sin(.90) > 1.09 .
$$
For $x>.25$, use $z\le O_z+.152$; the template's right circular turn is its topmost part, and no wall exceeds its track height. Then $x'>.579(1-\cos(.90))+.25\cos(.90)-.152\sin(.90)>.25$, giving an even larger gap from $x_m$. Inward offsets and cap fills are covered by projected nesting; the tiny stationary marks have no effect on the strict margins. The initial left wall point is consequently at distance $>1.09$ from the **entire final image**. Hence $\delta_{\rm hold}>.2D$, reach $>.03D$, and noncongruence follows from the four-center argument. Compactness of the images and the Euclidean group modulo bounded translations gives $\delta_{\rm E}>0$. This does not provide a large quantitative lower bound for the Euclidean quotient.

## 4. An isometric material bridge through the entire caps

In the moving-wall case use the interval $-.65\le x\le0$. Both originally horizontal labels there, with their full rolled transverse arcs, move by exactly $\delta e_x$ in the pre-rotation frame. The initial cap between those labels contains the entire rectangle $-.65\le x\le0,\ |z|\le H-d_b$; at each phase its translate is the corresponding rectangle. In the rigid-left case the same statement holds on the **entire original cap subdomain $x\le0$**, including its bowed-side boundaries. To see this, all actual curve and offset labels projecting to a slightly larger slab with reference $x\le.08$ there lie on the prescribed rigid left wing or the coherently shifted horizontal straight section. The right tongue and turns remain farther right, including after the largest inward offset.

Here is an explicit complete registration that pays these rigid fields while still mapping the rest of each cap onto its actual disk. Let $A_t$ be the smooth full star material map of §2 to the pre-rotation cap, with temporal coordinate $\theta=.90\sin^2(\pi t/2)$. Its Eulerian planar velocity is $V_t(A_t(p))=\partial_t A_t(p)$. Change it to
$$
 (1-\chi(x-\delta(t)))V_t+\chi(x-\delta(t))\,\delta'(t)e_x .
$$
For two moving walls take $\chi(x)=S_7((x+.80)/.15)[1-S_7(x/.08)]$; for rigid left take just the second factor. These clamped functions equal one on the claimed protected set. Across the true cap rim and a whole normal collar wherever $\chi\ne0$, $V_t=\delta'e_x$ already. Elsewhere on that rim the field is unchanged. The common Cartesian center is also unchanged. The new $C^2$ spatial vector field may be smoothly extended across the boundary collar into a bounded ambient neighborhood. Its time flow exists and is a diffeomorphism, agrees with $A_t$ near all rims and the center, and moves the protected initial area rigidly for every phase. This produces one closed material map, not separate unrelated patch assignments. Its metric is exactly the initial metric on the full bridge and on the adjacent rolls and central sheets, before and after spatial rotation. In particular all oblique as well as normal chords of this complete material bridge have the prescribed metric.

The second source evaluates this transport as a convergent time composition. At a small step with old and new raw caps $A,B$, update a physical point $p$ by
$$
 B(A^{-1}p)+\chi(p_x-\delta_{\rm old})[p+(\delta_{\rm new}-\delta_{\rm old})e_x-B(A^{-1}p)] .
$$
Differentiate the two-jet of $A^{-1}$ by its implicit equation. For sufficiently fine partitions each step is $C^1$-close to identity, is bijective onto the new disk and agrees with the unchanged boundary registration. The increments are the first-order increments of the displayed velocity, with corresponding spatial derivatives through order two. The compositions converge to its flow in $C^2$ by the usual differentiable-ODE estimates; the protected bridge is *already exactly translated at every step count*. Outside it the finite time-step entry is a numerical approximation, and the raw star entry is an independent untransported reference.

## 5. The failed wall and what the correction fixes

In the two-wall field, the two left upper/lower track cuts on $y=+1$ separate to $1.09$ at the final phase as the wall straightens. There is an initial path of length $<1.074$ between these same material labels. At the initial left wall, the unique amplitude is between 1 and 1.06. At 1 use the cosine series through sixth order for the uniform-clock integral, at least $1-1/4+1/64-1/2304$, multiply by .99 and add $.01\cos1$; this exceeds $.82/1.09$. At 1.06 the upper Taylor bound in §1 gives strictly less than that ratio. Consequently $\tau'\le6.2$. Travel into the upper end by the true material path $a=.25v/L$, with the analogous lower path. Its length is at most
$$
 \sqrt{L^2+.25^2}+
 \frac{.25}{L}\int_0^L 6.2d(v)\,dv
 \le \sqrt{L^2+.25^2}+.25(6.2)L^2/[6(.132)] <.411.
$$
Indeed $1-d\kappa=1+d\tau'$ along this path, and $d(v)\le v^2/(2\cdot.132)$. At the terminal ring the upper height in the planar $xz$ picture is $z=.41-\int_0^{.25}\cos\tau\,da-d_b\sin\tau(.25)<.126$. On $[0,.17]$ use $\cos\tau\ge1-(6.2a)^2/2$, on $[.17,.25]$ use $\cos\tau\ge\cos(1.06)$, and $\sin\tau(.25)>.82$ by the true clock at .25. The terminal upper/lower points have equal $x$. Their vertical planar segment lies inside the terminal disk: the upper section is $x$-monotone and its inward offset has the same tangent with positive speed; the lower section is its reflection. This supplies the claimed total upper bound. Thus the original two-wall central motion cannot be completed on its own $g_0$ by changing only the ends.

The corrected field takes these same two central labels and the entire left wing and its end paths by one rigid motion. Their Euclidean separation is exactly the original .82; their whole neighborhood, including the preceding cap shortcut, has the initial metric with the corrected cap registration. No height, target metric, phase limit or material arclength has been changed between the two alternatives. The remaining right bow and cap portion still carry genuine metric costs; coverage of the left wing and a suitable diameter ratio do not solve the entire closed problem.

## 6. A second wall shortcut after the left-wing correction

The rigid-left construction solves the previous wall failure on its full material region, but its original outward sinusoidal right bow expands the extreme horizontal span too much for the same $g_0$. Let $x_m$ be the initial left wall equator, $x_R$ the straight right wall equator, both at $y=+1,\ z=0$. In the initial metric a path from one to the other follows their true end meridians to the terminal ring, the planar horizontal diameter between the two rim points, and the opposite meridian back. The initial cap is star-shaped and symmetric in $z$; in particular the whole horizontal segment between the equators is inside it. Its length is $x_R-d_b-(x_m+d_b)$, since both endpoint normals are horizontal. Thus
$$
 d_{g_0}(p_m,p_R)\le (x_R-x_m)+2(L-d_b)<(x_R-x_m)+.152 .
$$
The original right-wall amplitude at $\theta=.90$ solves a cosine mean of .775. At $A=.96$, the lower Taylor bound $.99(1-A^2/4+A^4/64-A^6/2304)+.01\cos A$ exceeds .775, hence $A_R>.96$. The outward equator shift satisfies
$$
 b_R\ge \frac{.99(1.20)}{\pi}(A_R-A_R^3/9)>.32
$$
by integrating $\sin(A_R\sin(2\pi w))\ge A_R\sin(2\pi w)-A_R^3\sin^3(2\pi w)/6$ over the upper half clock; its positive remainder measure can be discarded. At the final phase the rigid-left equator is $x_m+.135$ and the right equator $x_R+b_R$ before $B_\theta$. Their Euclidean separation therefore exceeds $(x_R-x_m)+.185$. This contradicts the fixed-metric upper bound independently of any end filling one might attempt. The corresponding central lower bound on the required change of endpoint locations is $>.0165$ in their maximum norm.

Thus *both* named R754 families are incompatible with a global isometry when their whole central motions are held fixed. Their failures use different material labels. Their closed geometry, stationary marked grip and exact complete left material region in the second family stand. A different actual right-wall mechanism is required; no compatibility of an uncomputed replacement is asserted here.
