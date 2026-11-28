# R733 — An exact noncircular metric collar with both global reach inequalities at every collar point

2026-11-28. **Proved.** A further closed strong-held reference, with the very same fixed metric target, Fejér core and $S,R,H$ as R732, realizes that metric exactly on a positive-width two-sided collar of the actual noncircular core and on both R732 terminal collars. At all phases every ordered pair of points of the whole closed surface with either point in the exact core collar satisfies the radius-$.126$ normal-ball inequality. All R732 cap and end-pair certificates also hold. A wider two-sided middle cylinder containing the collar has radius-$.18$ normal-ball inequalities for every pair within it. The proof constructs the analytic core germ from the true first fixed quintic, then controls the interpolation, long chords, and the full per-angle material-length root. The core width obtained here is positive but not numerically enclosed. Global isometry, full active reach, and a set of computed meshes remain open.

## 1. Direct noncharacteristic isometry equation in the actual core variables

Use the intrinsic angle $\theta=\Theta(\varphi)$ from [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md). Its period is $2\pi$. As functions of $\theta$ the exact dyadic core $\gamma(\theta)=\Gamma(\varphi(\theta))$, tangent $t$, normal $n$, and radius of curvature $\rho$ are analytic on the circle, since $\Theta'=\rho>0$. They obey $\gamma_\theta=t$ and $t_\theta=-n/\rho$. Write $a=a_{\rm deep}$. Its first radial cell is the original polynomial quintic in $s$ with $a(0)=1,\ a_s(0)=0,\ a_{ss}(0)=k_0$. This follows directly from the strictly increasing original knots, true initial-law end jet and the physical Hermite coefficients in lines 29–46 of [FullHold](../notes/2026-11-17-parallel-model-full-hold-oracle.py) (file SHA-256 a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670). R690 changes only the terminal tail. Thus this *actual* first-cell function admits an analytic extension at the origin; no global analyticity across the 416 knots is assumed.

Seek $X(s,\theta)$ with $P=X_s$, $Q=X_\theta$. Use the normal and scalars
$$
 N=\frac{Q\times P}{|Q\times P|},\qquad m=N\cdot P_\theta,\qquad
 l=N\cdot Q_\theta,\qquad B=\frac{m^2-aa_{ss}}{l}.
$$
Set the three vector equations and initial values
$$
 X_s=P,\quad P_s=BN,\quad Q_s=P_\theta,\qquad
 (X,P,Q)(0,\theta)=(\gamma,e_z,t).
 \tag{1}
$$
Initially $N=n$, $l=-1/\rho$, $m=0$. The right sides are analytic in $s,\theta$ and in the unknowns and their first angular derivatives near the entire initial data graph. In particular the square-root branch and division are regular. The first-order Cauchy–Kovalevskaya theorem now gives a real analytic solution on a uniform positive-width strip. For detail, apply the theorem around each initial angle after subtracting its analytic initial functions, identify overlapping germs by analytic uniqueness and use a finite cover of the initial circle. Translating an angle by $2\pi$ solves the identical data and gives periodicity by the same uniqueness. Complexification, if used, takes the analytic square root of the dot product on the real positive branch. Coordinate and Euclidean symmetries of the original data are preserved since the product $BN$ is unchanged by the sign convention on $N$. [T. Gantumur, *Math 580 Lecture Notes 2: The Cauchy–Kovalevskaya Theorem* (2011), Theorem 18 and Corollary 20](https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf)

We verify the metric directly. The third equation and the initial value imply $Q=X_\theta$. Since $P_s$ is normal to $P,Q$, we have $(|P|^2)_s=0$ and $(P\cdot Q)_s=P\cdot P_\theta=0$. Thus $|P|=1$ and $P\cdot Q=0$. Put $w=|Q|>0$. Then $P_\theta=w_s Q/w+mN$ and
$$
 \tfrac12 (w^2)_{ss}=|P_\theta|^2+Q\cdot(BN)_\theta
                   =w_s^2+m^2-Bl.
$$
Consequently $ww_{ss}=aa_{ss}$. For each $\theta$ this ordinary differential equation has initial values $w(0)=1$, $w_s(0)=0$ and a unique local solution as long as $w>0$. The function $a(s)$ realizes them. Hence the induced metric is exactly $ds^2+a(s)^2d\theta^2$ on a nonempty complete angular strip. Also $X_{ss}(0)=k_0\rho n$ as required by [R7](R7-core-witness-initial-acceleration.md). Formal coefficients, when wanted, are given without an angular shooting parameter by taking the $s^j$ coefficients of (1) and dividing by $j+1$; the theorem just used supplies local convergence, not a numerical error or convergence radius for an unexecuted recurrence.

We use the positive-$s$ solution only, and reflect it across $z=0$ for the lower physical piece. Its radial and mixed jets give a $C^2$ joint; the reflected target uses the same positive-side $a(|s|)$. No even analytic continuation of the original polynomial is needed. The height derivative at the core is one, so by compactness it is positive on a common smaller collar. Write the upper germ in physical height as $(A(z,\theta),z)$. Uniform Taylor expansions on a smaller collar, with any fixed finite number of angular derivatives, give
$$
 A(z,\theta)=\gamma(\theta)+\tfrac12 z^2 W(\theta)+O(z^3),\qquad
 W=k_0\rho n .
 \tag{2}
$$
The upper germ is given by joint analytic inversion of $s\mapsto e_z\cdot X(s,\theta)$, whose derivative with respect to $s$ is one at the core. The usual differentiated bounds on the remainder in (2) through two $z$ derivatives follow from that analyticity.

## 2. Turn off the horizontal acceleration without a concentrated curvature cost

Let $z_0=.26$ and choose a positive $h<1$ small enough for (2) on $[0,h]$. Set $J=\log(1/h)$ and let $c=1-S_5$, with $S_5$ extended as in [R732](R732-rounded-cap-exact-terminal-metric-and-full-reference.md). Define
$$
 C_h(z)=
 \begin{cases}
 1, &0\le z\le h^2,\\
 c\big(\log(z/h^2)/J\big), &h^2\le z\le h,\\
 0, &h\le z\le z_0 .
 \end{cases}
$$
For $z\le h$ use $A_h=\gamma+C_h(A-\gamma)$; above $h$ set $A_h=\gamma$. The upper height-parametrized column is $(A_h,z)$, and the lower is its reflection. A fixed cutoff over a width proportional to $h$ would not make the two curvature-derivative terms disappear merely by sending $h$ to zero. This logarithmic transition gives
$$
 |z C'_h|\le\|c'\|_\infty/J,\qquad
 |z^2 C''_h|\le \|c''\|_\infty/J^2+\|c'\|_\infty/J .
 \tag{3}
$$
It is $C^2$ also at both switch heights. Thus, uniformly on the upper column,
$$
 \begin{aligned}
 A_h-\gamma&=O(h^2),& (A_h)_z&=O(h),\\
 (A_h)_{zz}&=C_h W+O(h+J^{-1}),&
 (A_h)_{z\theta}&=O(h),&
 (A_h)_{\theta\theta}&=\gamma_{\theta\theta}+O(h^2).
 \end{aligned}
 \tag{4}
$$
The first line holds with angular derivatives as needed. At the two-sided core the horizontal first $z$ derivative is zero; the second derivatives of the reflected halves agree, as do the mixed derivatives. In signed height the angular coordinate is unchanged.

The columns therefore converge in $C^1$ to the vertical cylinder $(\gamma(\theta),z)$, $-z_0\le z\le z_0$. In particular all complete horizontal sections remain strictly star-shaped for sufficiently small $h$, since the limiting angular determinant has a positive minimum, and the signed height excludes intersections of different sections. The coordinate metric tends uniformly to the identity in $(z,\theta)$, and a consistent unit normal tends to $n$. By (4) the normal second-form matrix in this order of coordinates differs by $o(1)$ from
$$
 \begin{pmatrix} C_h k_0\rho&0\\0&-1/\rho\end{pmatrix}.
$$
The same bounds hold on the lower reflection. R717 gives $\rho\ge1/4-553\,2^{-53}$ and $\rho<7$, so $1/\rho<4.01$ and $k_0\rho<7/4$. The absolute principal curvatures of the entire column are consequently $<4.5$ for all sufficiently small $h$. All coordinate second derivatives are uniformly bounded by (4). Angles need not share a common meridional arclength for the entire column.

## 3. All pairs within the complete column

First the limiting cylinder satisfies for all its pairs
$$
 2r_0|n_p\cdot(q-p)|\le |q-p|^2,\qquad r_0=.2 .
 \tag{5}
$$
Here is a global proof. In physical normal angle let $\gamma_0=\Gamma-r_0n$. Its derivative is $(\rho-r_0)t$ with positive coefficient. For each normal direction $\psi$, the derivative of $\gamma_0(\varphi)\cdot n(\psi)$ has sign $\sin(\psi-\varphi)$, so its global maximum is attained at $\varphi=\psi$. The same is true for $\Gamma$. For two planar points $p=\Gamma(\varphi)$, $q=\Gamma(\psi)$ these support inequalities give $(q-p)\cdot n(\varphi)\le0$ and
$$
 (q-(p-r_0n(\varphi)))\cdot n(\psi)\ge r_0 .
$$
The latter implies $|q-(p-r_0n(\varphi))|\ge r_0$; expansion gives (5). Distinct heights add a nonnegative squared vertical difference and leave the normal projection unchanged. This handles different angles, the same angle at different heights, and either base throughout the limiting column.

For all sufficiently small $h$, the full changed column satisfies (5) with $.18$ in place of $.2$. Suppose otherwise and take a failing sequence $h_j\downarrow0$ and pairs. Pass to convergent base and test parameters by compactness. Distinct limiting parameters yield a nonzero chord of the embedded limit cylinder. Its bound with $.2$ implies a strict inequality with $.18$, also when the normal projection is zero, contradicting $C^1$ convergence. If the parameters coalesce, write $v_j$ for their difference in a local $(z,\theta)$ chart, unwrapping the circle. The straight parameter segment stays inside the closed height interval. Along it the columns' tangent derivatives converge uniformly to the limiting derivative at the common limit point, an isometry on the parameter tangent plane. Hence the squared chord length is $(1+o(1))|v_j|^2$. Their normals on the segment differ from the base normal by $o(1)$ by uniform $C^1$ convergence. The coordinate Hessians are uniformly bounded. When projected on the contemporaneous unit normal the second directional derivative has magnitude at most $4.5|D X_j v_j|^2$ by §2. Substituting the base normal costs $o(|v_j|^2)$. Taylor's integral formula and vanishing of the base normal's linear term now give
$$
 \frac{2|n_p\cdot(q-p)|}{|q-p|^2}\le4.5+o(1)<1/.18 .
$$
This contradicts failure. No compactness of the coordinate second derivatives or uniform third derivative of the varying cutoff was assumed. This statement pays the normal-ball tests between all pairs of column points; it does not identify the reach of a separately cut surface with boundary.

## 4. Embed the column in a full reference with the same radial length

Keep both terminal assemblies of R732 unchanged, including their true $u=S-s\le .001$ R690 collars, their end length $L\in(.33,.35)$ and their vertical ends at $Q=R_v e+Ze_z$, $1.68<Z<1.69$, $.7025<R_v<.713$. The new upper central band extends from height $z_0$ to $Z$, both end tangents vertical and end accelerations zero. Set $\eta=1/512$. Use the Bernstein controls
$$
 B_0=\Gamma+z_0e_z,\quad B_1=B_0+\eta e_z,\quad
 B_2=B_0+2\eta e_z,\quad B_3=Q-2\eta e_z,\quad B_4=Q-\eta e_z,\quad B_5=Q .
 \tag{6}
$$
The horizontal polynomial is now simply $C\Gamma+(1-C)R_ve$ with $C=B_0^5(t)+B_1^5(t)+B_2^5(t)$, where $B_j^5$ denotes the Bernstein *weight*, distinct from the control point $B_j$. Its angular determinant is positive by R730 (26),(27) with nonnegative coefficients, and the ordered heights are strictly increasing. Apply the same positive factor $1-\xi\psi(t)$, $\psi=[1-(2t-1)^{12}]^7$.

The column's actual individual length is
$$
 L_h(\theta)=\int_0^{z_0}\sqrt{1+|\partial_z A_h|^2}\,dz.
$$
It is $z_0+O(h^3)$ uniformly since the derivative is $O(h)$ and supported in $[0,h]$. It is periodic and analytic in angle: the fixed compact analytic core germ extends in angle to a common complex neighborhood on a small closed real height interval, real height cutoff coefficients are independent of angle, and the speed's positive square-root branch extends uniformly to a smaller angular neighborhood. Integrating the resulting holomorphic functions over real height proves the claim. In particular $z_0\le L_h<.261$ for sufficiently small $h$. The required central length is
$$
 \Lambda(\varphi)=S-L-L_h(\Theta(\varphi)),\qquad 1.759<\Lambda<1.79 .
 \tag{7}
$$
This per-angle value is essential for keeping the cap and original terminal $s$ positions.

By (1) of R732, the horizontal endpoint gap is at most $.98$. The height difference is $<1.43$ and $>1.42$. The complete length at $\xi=0$ is bounded by the spatial control polygon, hence by
$$
 \sqrt{.98^2+1.43^2}+8/512<1.751<\Lambda .
$$
For $\xi=3/4$, the three chords through $t=0,1/8,7/8,1$ give a complete lower bound as in R732 §4. The horizontal error of either near-end chord is at most $(526/32768).98$ and its vertical endpoint discrepancy at most $2\eta+(526/32768)1.43$. Their sum for both ends is $<.1$. Thus length exceeds
$$
 1.42+(3/4)(97/125)(.439+.7025)-.1>1.98>\Lambda .
$$
Uniform positive speed and strict endpoint inequalities give a unique positive analytic angular root of the convex length equation by R730 (35)–(39), now with the analytic right side (7); derivatives of the equation must include the derivatives of $\Lambda$. The accurately arclength-parametrized column, central band and terminal end thus have combined length exactly $S$ at every angle, with terminal start $s=S-L$ independent of angle. The column-to-central material seam is really $s=L_h(\theta)$. One convenient atlas uses height in a neighborhood of that seam. Both horizontal curves have exactly $\Gamma$ as value there and zero first and second height derivatives (the Bernstein pulse vanishes to seventh order). Their first and second angular and mixed jets agree as well. They give the same $C^2$ height chart. The arclength coordinate has positive derivative and matches across this chart by integration with the true angle-dependent initial length. For angular derivatives through order two this uses the available angular smoothness of the pieces and the matching differentiated jets; no fixed-angle seam table is substituted. At $Q$ the same statement holds with the identical circular cylinder jets and angular-independent material end $S-L$.

In particular, with a dot denoting the derivative in the **actual chart angle** $\varphi$, the two amplitude jets solve explicitly
$
 \dot\xi=(\dot\Lambda-\mathcal L_\varphi)/\mathcal L_\xi,\qquad
 \ddot\xi=(\ddot\Lambda-\mathcal L_{\varphi\varphi}
       -2\mathcal L_{\xi\varphi}\dot\xi-\mathcal L_{\xi\xi}\dot\xi^2)/\mathcal L_\xi .
$
Here $\dot\Lambda=-\partial_\varphi L_h(\Theta(\varphi))$, with the analogous second derivative. For the central local coordinate $t$, after substituting the root, let $\ell(t,\varphi)=\int_0^t v\,dt$ denote its arclength and $A=L_h(\Theta(\varphi))+\ell(t,\varphi)$. Then $A=s$, $A_t=v>0$, $t_s=1/v$, $t_\varphi=-A_\varphi/v$, and
$
 t_{ss}=-v_t/v^3,\quad t_{s\varphi}=-(v_\varphi+v_t t_\varphi)/v^2,\quad
 t_{\varphi\varphi}=-(A_{\varphi\varphi}+2v_\varphi t_\varphi+v_t t_\varphi^2)/v .
$
All fixed-$t$ derivatives of $\ell$ here include the two true root jets. Composing the spatial polynomial with these inverse jets gives the actual six jets, e.g. $F_{s\varphi}=G_{t\varphi}t_s+G_{tt}t_st_\varphi+G_t t_{s\varphi}$. On the column the corresponding inverse uses $\int_0^z\sqrt{1+|(A_h)_v|^2}\,dv$. Near its top this primitive is $z-z_0+L_h(\theta)$, so its purely angular terms at the seam agree with $A_\varphi,A_{\varphi\varphi}$ at $t=0$. This is the material mixed-jet contribution of the moving interface.

All sections of the column, central band and rounded end are one-to-one and strictly ordered by height outside the actual flat disks. The R730 positional cone and radius-$2.099$ ball hold for (6) by the same control estimates as R732, now with the lower controls at heights between $.26$ and $.264$. On the column $|A_h-\gamma|<.005$ for sufficiently small $h$, and $|A_h|<1.435$, $|z|\le.26$. The same cone and ball therefore hold on it too. Reflection, the unchanged caps and outward p4 give the full closed $C^2$ embedded family, $D\le4.2$, grip diameter $.9$, and both strong held witnesses $>.91$. Each active section at a fixed non-end height is angular-analytic, noncollinear and closed. Any open planar patch would contain open arcs at each of two different nearby heights in the interior of one piece. The plane equation analytically continues around each angular circle. A noncollinear full horizontal section determines its own horizontal plane, incompatible with the other height. The finite seams have no two-dimensional interior. Thus R238/R661 give the same positive $\delta_{\rm E}$ including reflections as in R732.

## 5. The exact core collar against the entire closed surface

Take $h$ further small so that $h^2<.007$ and all preceding strict conclusions hold. On $0\le z\le h^2$ the column equals the actual isometry of §1. Its meridians are unit-speed in original $s$ and have strictly increasing height. Since $|dz/ds|\le1$ and the height is zero at the core, **the complete common material band $|s|\le h^2$** belongs to this exact collar; the part at fixed height $|z|\le h^2$ may extend slightly farther at some angles. No finite-mode or sampling error occurs in this assertion.

If one point lies at $|z|\le h^2$ and the other belongs to the column, §3 gives the two-sided $.18$ inequalities in both orders. If the other lies outside the column, its absolute height is at least $.26$. Their separation is at least $.26-h^2>.253>2(.126)$. The radius-$.126$ conditions at *both* bases follow immediately even when the other base is on a marker. This covers all components and phases. R732's proof of the cap and terminal inequalities continues to hold because the whole nonterminal portion is still in $|z|\le Z$. In particular exact core metric and all global ordered normal tests involving that collar coexist in one closed strong-held reference. The local exact angular metric is not being inferred from proximity of two surfaces.

The unproved pairs are among the remaining activity outside this exact core collar and not already covered by the column/column, same terminal assembly, chords longer than $.252$, and cap estimates. The fixed metric is still unpaid on the intervening material interval. No bound on a numerical CK width or solver field is reported. The logarithmic cutoff theorem permits every sufficiently small positive $h$, including sufficiently small dyadic values; its physical parameter must be fixed before any refinement claim. The positive width and the corrected length root cannot substitute for a certified global continuation of (1) or an actual whole-field solve. No scientific computation, integral, grid or root was executed for this proof.
