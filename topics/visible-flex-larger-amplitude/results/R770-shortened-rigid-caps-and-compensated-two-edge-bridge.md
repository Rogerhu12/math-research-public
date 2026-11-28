# R770. One common preloaded metric with shorter moving ends, distinct incoming and outgoing Cauchy data, and a bounded three-vector endpoint correction

The fixed material sphere, its metric $g_0$, initial map, right fixed grip and moving central extrusion are precisely R767. The last-phase fixed-boundary obstruction of R768 was for the old exterior translations. Here the axial translation of each whole exterior at phase $t$ is changed from $\mp.18\sin t$ to $\mp.40\sin t$ while its horizontal part stays $-\Delta J/2$. Both true translated exterior components, including the nonplanar caps, retain their initial metrics. The displacement bound for the terminal central head, the fixed grip and the initial reach apply since the initial map and the central field agree exactly with R767. We construct a physical unit-speed connector with independent end velocities to first nontrivial order, a genuine non-even interior freedom and an actual uniformly invertible three-vector correction. The remaining two bridge metric entries and the complete positive-phase thickness are open.

## A strictly shortened range of true diagonal chords

Put $x=\sin t$. If $r=|q_0(s_2)-q_0(s_1)|$, consider the incoming rim label $s_1$ and the outgoing rim label $s_2$ on one side. Their initial squared distance is $r^2+P_0^2$. The new horizontal displacement relative to the initial difference is $h(s_1,t)$ with $|h|\le.340x$ by R767. Their final squared distance minus the initial one is at most
$$
 x[.680r-.80P_0+(.340^2+.40^2)x].
$$
This is negative at every positive phase if $r\le.37$, since $P_0>.65986$. In particular the original forbidden arc has $r=2(.23)\sin(.85)<.347$. This compares true space chords even before using that the initial intrinsic distance dominates each initial chord. No condition on longer chords follows from this estimate.

## The angular drift and the meridian mean

Work on the dimensionless interval $u=v/L$, $L=.66$. Write $b(u)=\sin(2\pi P(u))$ as in R767 and
$$
 p(u)=[P(10u)P(10(1-u))]^2.
$$
Thus $p=1$ on $[.1,.9]$ and it is $O(u^8)$ at the two edges. The required axial and horizontal means are $Z_*=(P_0-.40x)/L>.393$ and $X_*=|h|/L\le.340x/L$. First take the two-parameter mean $(X,Z)=\int\cos(\gamma b)(\sin(\beta p),\cos(\beta p))du$. There is a unique root with $0\le\beta<\pi/2$, $.005<\gamma<\pi$ along the branch from the positive-bulk solution. On the two tails of total length $.2$ one has $|b|\le\sin(2\pi(.1-.03)/.94)<.452$, so $\cos(\gamma b)>0$ for $\gamma\le\pi$. Let $B=\int_{.1}^{.9}\cos(\gamma b)du$. Wherever $Z\ge Z_*$ we have $B>0$, since $\beta\in[0,\pi/2]$ and the contribution of the tails to $Z$ is at most $.2$. At such a root $X_\beta>0$, $Z_\beta\le0$, $X_\gamma\le0$ and $Z_\gamma<0$. These signs follow by separating the $p=1$ bulk and the tails, using $b\sin(\gamma b)\ge0$. At fixed $X$ the axial value is strictly decreasing.

At $\gamma=0$ the desired $X$ is attained with $\sin\beta\le X_*/.8$; the axial loss is at most $X_*\tan(\beta/2)<.21x$, smaller than $1-Z_*\ge 1-P_0/L+.40x/L$. At $\beta=\pi/2$ the axial mean is at most $.2$. At $\gamma=\pi$ use $\cos(\pi b)\le 1-2b^2$ and the clock substitution $du\ge.94\,dP$ to get $\int\cos(\pi b)du\le.06$. In particular $B\le.06$, as the tails here are nonnegative; hence $Z\le .26$. At $B=0$ one already has $Z\le.2$. Continuation gives the root. To see the uniform lower bound, if $\gamma\le.005$ use $\sin\beta\le X_*/(.8\cos(.005))$ and
$$
 1-Z\le \gamma^2/2+X_*\tan(\beta/2)<.000013+.21x .
$$
But $1-P_0/L>(.94)(2/3)(1-\cos(.01))>.000031$. The implicit inverse in $(b_{h,x},b_{h,z},\gamma^2)$ is smooth even through $h=0$: the transverse horizontal eigenvalue is $\int\cos(\gamma b)p\operatorname{sinc}(\beta p)>0$, by the same bulk/tail argument, and the axial/radial derivative matrix has the preceding strict determinant divided by the positive scalar $2\gamma$. At phase zero the root is $b_h=0$, $\gamma=.02$.

Use the R768 non-even rotation law with support $[.006,.088]$ and its reflection, two $S_7$ ramps of width $.008$. The new $p$ varies on this support. The weight $\Omega b^2\operatorname{sinc}(\gamma b)$ remains positive there for $\gamma<\pi$. The proof of the three projected zero moments, including $b_h=0$, is unchanged. The base horizontal direction $N_e=-\cos\chi\,n_t+\sin\chi\,T_t$ is independent of $u$ on that support. Its longitudinal/time coefficients and up to three odd polynomial modes in the source are freely selectable and all carry the factor $\sin t$. Denote the resulting unit velocity by $V_0$. Its full average is the specified vector, and at paired $u$ outside the odd support it has the form $cE_1\pm dE_2$ in one common orthonormal pair, $c=\cos(\gamma b)$, $d=\sin(\gamma b)$.

## Perturb both physical edges and restore the three real endpoint coordinates

Set $e=.0005$, $l=1-S_7(u/e)$, $r=1-S_7((1-u)/e)$ (extend the cutoffs by constants). Let $k_t$ be R767's signed profile curvature and let $\delta$ be the actual heading change from $q_0$ to $q_t$, zero on both heads. For $u>0$ let
$$
 \Lambda=1+\frac{k_t(k_0-k_t)}{k_t^2+u^2}.
$$
Where $k_t\ne0$ it lies between $1$ and $k_0/k_t$. From the common positive summands in the heading derivative, $0<k_0/k_t\le .87/.09<9.67$ on track interiors; at heads it is one. At a common zero put $\Lambda=1$ at $u=0$. In the original unit velocity, before applying $R_{b_h}(p)$, change the signed elevation $\gamma b$ and the horizontal yaw $\chi$ to
$$
 q=(1-l-r)\gamma b+l\arcsin(\Lambda\sin(.02 b))+r(.02 b),\qquad
 \chi_*=(1-l-r)\chi-r\delta.
$$
The two supported edge neighborhoods miss all the odd modes. At the right edge $-\cos(-\delta)n_t+\sin(-\delta)T_t=-n_0$; at the left the limiting direction is $-n_t$. At zero phase the new angles agree with the old angles everywhere. The arcsine is smooth on the used support; elsewhere its value is immaterial and the source bounds its working argument. Let $V_*$ be this new unit vector. For fixed nonzero $k_t$ the incoming horizontal fourth-order coefficient is $-\Lambda(s,0)\,.02 (2\pi C)n_t$ with the $C$ from R768. The outgoing one has the initial normal and amplitude and opposite sign. The drift has order eight. Thus the edge tangential projection in the mixed row vanishes at order four on both ends; at a station with $k_t\ne0$ the first incoming tangential projection of the integrated longitudinal derivative uses $k_t\Lambda(s,0)=k_0$. This local statement does not solve either row in the interior.

For completeness the regularization gives a genuine two-jet field through the four zero stations. On either side of a station the curvatures and their first two one-sided derivatives are bounded. $k_0,k_t$ have matching first derivatives at the join (zero), and the difference $k_0-k_t$ vanishes to order three on the track and identically on the neighboring head. Thus their product $k_t(k_0-k_t)$ is $C^2$ across the join, as is $k_t^2$. For all $u>0$ the quotient is $C^2$ in $s$. On the compact curves $|k_0-k_t|\le C|k_t|$. Differentiating the regularized quotient using $|k_t|/(k_t^2+u^2)^{1/2}\le1$ gives $|\nabla\Lambda|\le C/u$ and $|\nabla^2\Lambda|\le C/u^2$ on smooth pieces; the phase derivatives obey the same bounds on compact time. Its product with $\sin(.02b)=O(u^4)$ has derivatives of orders 1,2 bounded by $O(u^3),O(u^2)$ and hence extends with a continuous zero two-jet at $u=0$. This suffices for the integrated immersion field on each closed chart. No division by curvature is used at an actual zero.

Let $w$ be the symmetric $S_7$ window on $[.44,.47]$ and its reflection, unit on $I=[.45,.46]$ and its reflection. Seek $a\in\mathbb R^3$ so that
$$
 V=\frac{V_*+w a}{|V_*+w a|},\qquad \int Vdu=\int V_0du .
$$
At $a=0$ the defect norm is at most $2\int_0^e20|b|du<2.1\,10^{-11}$. Indeed $P(u)\le12500u^4$, $|b|\le80000u^4$, and the two altered elevations have absolute values at most $\pi |b|$, $.20 |b|$ on the edge where they mix. An arbitrary change of horizontal direction then costs less than $20|b|$. These estimates are independent of the free yaw and three odd coefficients.

The mean map is the gradient of $\int(|V_*+wa|-1)/w\,du$, interpreting $w=0$ by $V_*\cdot a$. Its Hessian is $\int w(I-VV^T)/|V_*+wa|\,du$. Uniformly on $|a|\le.04$ its least eigenvalue exceeds $2\,10^{-9}$. On $I$ and its reflection $T_\pm=cE_1\pm dE_2$, $.25<|b|<.34$, $c>.48$, $|d|>.00078$ (use $\gamma>.005$ and $|\gamma b|<1.07$). For each unit $z$, the average of $|z\times(T_\pm+a)|^2$ equals $|z\times(cE_1+a)|^2+d^2|z\times E_2|^2$. If $|z\times E_2|\ge.5$ the second term is at least $(.00078)^2/4$; otherwise $|z\times E_1|\ge\sqrt3/2$ and the first term is greater than $(.48\sqrt3/2-.04)^2$. Divide by at most $1.04^3$ and integrate over length $.02$ to obtain the asserted lower bound. On the boundary of the radius-$.04$ ball the gradient of the potential minus the desired linear functional points strictly outward: $.04(2\,10^{-9})>2.1\,10^{-11}$. It therefore has one critical point in this ball, unique there by strict convexity. The inverse is uniform. At phase zero $a=0$; at all phases it varies with the genuine material parameters by implicit differentiation. This correction preserves each assigned edge velocity as $w=0$ there.

Integration from the original moving central point gives the full closed map. The velocity equals $e_y$ with zero first material derivatives at both ends. The longitudinal position derivatives at the far end follow by differentiating the corrected full vector moment twice. Thus both meridian edges have the required six physical jets, and the rigid outer roll and its cap use their original two-jet transition. The source supplies also the right-hand chart at the internal $v=L$ seam and the same regular Cartesian caps and true normal-to-disk overlap as R767. Every bridge has $g_{vv}=1$ identically in the exact integrals. Source evaluations use split quadrature, original derivative conventions and four jet Newton steps for the small convex three-vector correction; numerical errors remain measured quantities. The proof gives no all-phase embedding or reach for the new bridge and no whole-sphere isometry. Additional shared displacements of the exterior/rim or bridge in the numerical search require evaluation of every affected Gram component.
