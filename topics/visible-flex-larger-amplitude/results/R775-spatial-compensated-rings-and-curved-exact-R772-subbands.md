# R775. Spatial transverse rings with exact rolling subbands on the fixed R772 sphere

This construction keeps exactly the R772 *coherent* initial embedding, all material labels and the interval $0\le t\le\pi/2$. At every positive phase every transverse ring on an open axial interval is a genuinely nonplanar closed space curve. All material transverse speeds, both complete R772 developing-cap disks, both whole rounded heads and both entire terminal planar disks have their initial metric. On the middle axial interval true open, initially curved portions of each of the four rounded side corners also have their full original metric. The result is a $C^2$ embedded closed sphere at all phases with a pointwise fixed right head, a strong held bound and differing endpoint volumes. The argument does not pay all rows on the two remaining side bands or give the prescribed quantitative reach there.

## Longitudinal and transverse controls

Use the R772 orientation, world axes $(X,Y,Z)$, axial material $x\in[0,1]$ and transverse arclength $e\in\mathbb R/P\mathbb Z$. Let $C$ be its original rounded square. Denote $c=C'_X$, $h=C'_Z$, so $c^2+h^2=1$. Write $f_0(x)=\sin q_0(x)$ for the R772 initial longitudinal slope. This notation distinguishes the two one-dimensional material coordinates. For clipped smooth step $S_7$ define
$$
 d=.06,\quad p(x,t)=(1-1/96)\sin^2t\, S_7(x/d)S_7((1-x)/d),\qquad
 f(x,t)=f_0(x)/(1-p(x,t)).
$$
Thus $|f|<.96$, $p$ is even in $x-1/2$, and $f$ is odd there. Set $A'=\sqrt{1-f^2}>.28$, $Z'=f$, $A(1)=.5$, $Z(0)=0$. Then $Z(1)=0$. All these functions are smooth to the order required, including at both ends; $p$ and its derivatives through order two vanish there.

For $0<a<b<1$ put $S_{ab}(h)= S_7[(h^2-a^2)/(b^2-a^2)]$ and take
$$
 U=1-S_{.16,.26},\qquad V=S_{.32,.42}(1-S_{.68,.78}).
$$
Each is an even function of $h$. Let $b_*=\int |h|U\,de/\int|h|V\,de$ over any complete rounded corner. The means are identical on each corner by rotation/reflection of its true tangent law. More precisely, the four corners use the same distribution of $|h|$ by the symmetry of the $\pi/2$ turning clock. Their two speed ramps use a total excess arclength at most $.001$ over $.27\,d\alpha$. All mask transitions occur in the constant-curvature interior. Therefore
$$
 0<b_*\le\frac{.27(1-\sqrt{1-.26^2})+.001(.26)}
 {.27(\sqrt{1-.42^2}-\sqrt{1-.68^2})}<.21 .
$$

For fixed $p$ define the actual unit transverse tangent, in world coordinates, by
$$
 H=h(1+p[b_*V-U]),\qquad Y_1=.001p Vc,\qquad X_1=\operatorname{sgn}(c)\sqrt{1-H^2-Y_1^2},\qquad T_p=(X_1,Y_1,H).
$$
Near every zero of $c$, including both complete vertical sides, $U=V=0$, so $X_1=c$ there. No sign selection or singular derivative is needed at a reversal. On the moving support $|h|\le.78$, $|H|\le .78(1.21)<.944$ and $|Y_1|\le.001$. Hence $|X_1|>.329$ whenever a square root differs from its original tangent component. The material and parameter derivatives are smooth across the matching windows.

Define $B_p(e)=C(e)+\int_0^e[T_p-(c,0,h)]\,d\xi$, with $C$ here inserted into the $(X,Z)$ plane. The initial cross-section label $e=0$ is the start of the top horizontal straight side. Each of the two side strips goes from one horizontal side to the next by two corners and one vertical side. The change of vertical displacement on every whole corner is zero, by the definition of $b_*$; the tangents on the straight central side and the horizontal side are unchanged. About the middle of a side strip $h$ has equal values and $c$ opposite values, so $Y_1$ and $X_1-c$ cancel pairwise on its two corners. Consequently the integral of the full change vanishes *separately on each complete side strip*. It also vanishes on both horizontal sides. This proves period closure, the original positions of all four horizontal-side endpoints, and $B_p(e)=C(e)$ at every point of either full horizontal side. The primitive and its first two longitudinal derivatives there agree with the old positions. This argument uses the actual arc profiles and does not replace a spatial closure condition by a scalar circumference condition.

Whenever $p>0$, the ring is not planar. Its horizontal side has tangent $e_X$, and a genuine curved arc with $0<|h|<.16$ has nonzero vertical tangent component but $Y_1=0$. These tangents force any putative plane of the whole curve to be parallel to the $(X,Z)$ plane. In contrast $V>0$ on a true open shoulder with $Y_1\ne0$.

## Surface, metric and all joins

The new central field is
$$
 F(x,e)=B_{p(x,t)}(e)+(0,A(x,t),Z(x,t)).
$$
At phase zero this is exactly the R772 coherent field; in particular its fixed target is $dx^2+de^2+2 f_0 h\,dx\,de$. Every transverse velocity has unit norm for all phases. On either horizontal side the physical central strip is $(X,A,\pm H_0+Z)$, where $H_0$ denotes the old square half-height. Thus the complete three metric entries there are the initial ones. At the two axial boundaries $p=p_x=p_{xx}=0$, $f=f'=0$, $A'=1$, and both curvature jets of the longitudinal base at the endpoints match the original axial extension. The complete six physical jets across either ring are exactly those of R772 up to that head's axial translation. Attach the full R772 right rounded head and whole planar disk without movement, and translate both left pieces by $A(0,t)-A(0,0)$. The two end-plane/collar overlaps, Cartesian center charts and regular normal changes are the original ones. Therefore the whole two developing disks specified in R772, including both rounded-head strips and their actual terminal-plane rectangles, retain all three entries even as their middle changes shape. The complete right head provides the same pointwise fixed grip.

On $.06\le x\le.94$ the value of $p$ depends only on phase. Thus $F_x=(0,A',f)$ on the whole periodic section and $g_{xx}=1$. On $U=1$, $V=0$ one has $Y_1=0$ and $H=h(1-p)$, so $g_{xe}=f_0 h$ exactly as well. This includes, on every corner, the real open arc $0<|h|<.16$ next to the horizontal side; its original planar curvature equals $1/.27$ on a positive-width subinterval. On an open subrectangle $f'_0\ne0$ (for instance $.1<x<.2$) and the original section normal has nonzero vertical component, so the original translation surface there has nonzero Gaussian curvature. These patches are not just another planar development. On the middle band the remaining exact mixed defect is
$$
 \sqrt{1-f^2}\;Y_1+f H-f_0h .
$$
On the two axial transition layers an additional genuine term $p_x\partial_p B_p$ enters $F_x$. Both the mixed and longitudinal errors must be counted there. These layers are part of the closed candidate.

## Slice-by-slice embeddedness in world axial coordinates

Use $y$ for the *world* coordinate. The axial part of the section correction is $pD(e)$ with $D'=.001 Vc$. We have $|D|\le .001P<.00227$ and $|D'|\le .001$. Since the two end cutoffs have disjoint transitions, $|p_x|\le (140/64)/.06<36.46$. For every label $e$, $y=A(x)+pD(e)$ runs strictly increasingly from $A(0)$ to $A(1)$, with derivative greater than $.28-36.46(.00227)>.197$. This proves a unique smooth axial label $x(y,e)$ at every $e$ on each intermediate physical slice, with $|x_e|<.001/.197$. The axial labels of any two points on a common slice differ by at most $2(.00227)/.28<.017$.

We check the entire closed slice. At fixed $p$ the transverse projected $X$ tangent has the sign of $c$ and is zero only on the two true vertical sides. To control the implicit change of $x$, differentiate the integral for $(B_p)_X$. On the active support
$$
 |\partial_p X_1|\le (|H|\,|h(b_*V-U)|+10^{-6})/|X_1|<.75 ,
$$
since $|h(b_*V-U)|\le.26$. There are at most two changing corner arcs between consecutive zero primitive values; each has length $.27\pi/2+.001<.426$. Therefore $|\partial_p(B_p)_X|<.64$. The derivative of world $X$ along the slice differs from $X_1$ by at most $36.46(.64)(.001/.197)<.12$. Where $V=0$ that correction is zero exactly, since $D'=0$. Where $V\ne0$ it is less than the genuine lower magnitude $.329$ and cannot reverse the sign. Thus between the two vertical sides the upper and lower branches each sweep the full interval of world $X$ strictly monotonically, with opposite orientations. On the two vertical sides $D'=0$, $x$ is constant and the original vertical component of the tangent is exactly $+1$ or $-1$. These are actual straight connecting segments.

At fixed $p$ the two upper corners have transverse $Z\ge .07$, and the two lower corners $Z\le-.07$: $H$ has the same sign as $h$, and the total height displacement on each corner is exactly the initial one. The horizontal sides satisfy the same inequalities. Along any common physical slice the added $Z(x)$ differs by less than $.017$ since $|Z'|<1$. Hence the upper graph and lower graph over any common $X$ stay apart by at least $.14-.017>0$. The two connecting vertical segments occur only at the extreme abscissae. This proves embeddedness of the complete slice and hence of the full middle shell. Its positive axial derivative and the nonvanishing tangent of each slice also prove immersion. The two static-form end heads are outside its open range of axial coordinates and share only the fully matched rim. This gives a closed $C^2$ embedding through every phase. Compactness of this $C^2$ embedding path gives a positive uniform normal-tube radius, but this argument has not given $.03D$ for the new fields.

## Strong held and rigid quotient

The initial diameter and grip keep the R772 bounds $D<1.55$ and grip diameter $>.68$. The minimum physical axial coordinate of the whole body is $A(0,t)-p_b$, by the preceding slice construction. Its final displacement is $\Delta_A=\int_0^1(\sqrt{1-f_0^2}-\sqrt{1-f^2})dx>.32$. To prove this, let $j=\sin(2\pi P_c(x))$, $w=j(1.5-.5j^2)$. The uniform-clock average of $w^2$ over a full cycle is $41/64$, by the even sine moments $1/2,3/8,5/16$. Its material integral is at least $.94(41/64)$. In the two omitted clock ramps $x\in[0,.06]\cup[.94,1]$, $|j|\le2\pi(.03/.94)<.201$ and $w^2<.092$. On the remaining interval at the last phase $f=96 f_0$, where $f_0=.01w/\sqrt{1+.01^2w^2}$. Thus
$$
 \int f^2dx\ge \frac{.96^2}{1+.01^2}\,[.94(41/64)-.12(.092)]>.544.
$$
Concavity gives $\int\sqrt{1-f^2}dx\le\sqrt{1-\int f^2dx}<.676$. The initial integral exceeds $.99994$, proving the claimed distance. The original axial minimum is therefore at least $.32$ from the entire endpoint image.

Finally the enclosed endpoint volumes differ by more than $.02$. In a quarter the horizontal primitive changes by less than $.05$. Indeed on the low window $|X_1-c|<.036$, which uses length at most $.27\arcsin(.26)+.001<.073$. On the compensating shoulder $|X_1-c|\le[(2(.21)+.21^2)(.78)^2+10^{-6}]/(.329+\sqrt{1-.78^2})<.298$ over length $.27(\arcsin(.78)-\arcsin(.32))<.155$. The two windows are disjoint, their combined bound is $<.049$. Opposite contributions cancel by reflection across the central straight side, so the absolute horizontal position change at *any* label is $<.05$. On a fixed physical slice the $Z$ extent is below $2(.341)+.017=.699$ and the $X$ extent below $2(.341+.05)=.782$. Its enclosed area is bounded by the product. Initial cross-sectional area is at least $4b^2+8b(.27)+\pi(.27)^2>.399$ for $b=.07$: the section encloses the Minkowski sum of $[-b,b]^2$ and the radius-$.27$ disk, as follows from the corner support estimate in R772, $C\cdot n\ge .27+b(|n_X|+|n_Z|)$. Consequently the initial middle volume exceeds $.399(.99994)$, while the final one is below $.676(.782)(.699)$. The terminal head volumes are unchanged. Noncongruence and positive rigid Hausdorff quotient follow for the complete two endpoint surfaces, with the same compact-orbit argument as R772. Its quantitative quotient bound and its $.03D$ tube are not transferred.

The supplied physical generator differentiates the split corner integrals in the actual parameter $p$ and uses the upper-limit derivative in $e$. At $p=0$ it returns the R772 material initial field. Numerical quadratures are working evaluations; the exact assertions above use the stated integral definitions. No convergence to a fixed-metric solution is certified here.
