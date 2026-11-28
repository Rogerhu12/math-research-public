# R784. Exact fixed-metric continuation from bent disk arcs into the genuinely curved circular rolls

Use the exact R781 material, its initial tensor, the actual four MILD turns of R783 and the two-cap shear of R785. On each cap, eight moving angular bands extend through a uniform material distance $0.0000688$ into the genuine roll with all three fixed metric entries and the correct boundary two-jet. This holds throughout $\pi/4\le t\le\pi/2$. Four other open angular sectors admit exact extensions down the whole roll. A localized part of the eight-band continuation fits into an actual closed, thick family with the two complete developed disks and the original macroscopic displacement. The full central and roll metric still has residuals.

## Boundary data on the actual material

Write $a_b=.45-d_b\in[.359,.360]$, $\theta=e/.45$, $v=L-b$ on a roll, where $b$ is arclength from its central edge. Thus $v=0$ at the disk and $v>0$ points out of the disk in its original transverse plane. For $0\le v\le\eta=.001$ put
$$
 \alpha'(v)=S_5(v/\eta)/.09,\qquad \alpha(0)=0,\qquad
 a(v)=a_b+\int_0^v\cos\alpha,\quad
 g=dv^2+a(v)^2d\theta^2,\qquad K={\sin\alpha\,\alpha'\over a}.
$$
Here $S_5(z)=10z^3-15z^4+6z^5$. This is the right-end polynomial germ of the actual softened turn. In particular $K>0$ on the entire open strip. The same abstract metric holds on both rolls, with opposite world axial orientations. The adjacent cap has the extension $a_f(v)=a_b+v$ for $v\le0$.

Let $\ell$ be one of the four signed coordinate directions in the transverse plane. Use $\phi$ as angle from $\ell$ with a consistently oriented transverse frame, and $u=(a_b+v)\cos\phi$ on the flat development. The cap turns through
$$
 \beta(u)=A\sin^2t\,P_c((u-a_b/\sqrt2)/.08),\qquad
 A\in\{.020,.022,.024,.025\}.
$$
The four amplitudes correspond in order to $+X,-X,+Z,-Z$. The cap map $D$ on this sector is the unit-speed plane curve with velocity $(\cos\beta,\sin\beta)$ in the $\ell,Y$ plane, extruded along the perpendicular transverse coordinate. Constants of integration agree with the fixed interior disk. On either cap choose the local unit normal giving positive principal curvature in the $\ell$ direction. Its sign relative to a global closed-surface orientation may differ at the two heads. All equations below use this same normal on a patch.

Choose either sign of $.46\le|\phi|\le.69$ about each of the four axes. Each of these eight angular bands lies on the constant derivative portion of the true clock, including the real radius $.04$ about every center. Indeed $.42\le|\phi|\le.73$ gives $.0048<a_b(\cos\phi-1/\sqrt2)<.0752$. Only this flap acts there. The constant sectional curvature is
$$
 k={A\sin^2t\over .08\cdot .94},\qquad .132<k<.333
 \quad(\pi/4\le t\le\pi/2).
$$
In the orthonormal frame $(\partial_v,a^{-1}\partial_\theta)$ the entries $(L,T,N)$ of the second fundamental form of the prescribed cap at $v=0$ are
$$
 k\cos^2\phi,\quad -k\sin\phi\cos\phi,\quad k\sin^2\phi .
$$
These are independent of the signs of the chosen world coordinate once the frame is oriented as above. In particular $N>0$ on both signed bands. Orientation of $\theta$ can be reversed together with the sign of the mixed component.

On the saturated sectors $a_b(\cos\phi-1/\sqrt2)>.08$ the cap map equals one rigid motion on an open neighborhood of the rim. Apply that fixed motion, including its translation, to the complete canonical R781 roll for every such angular label. This pays $g$ through its full length $L$ and gives the correct disk two-jet. These are four exact solutions on open material sectors. Their far ends need not match the prescribed central field. The unsaturated turning sectors below use a different construction.

## Solve the two shape equations

Set $p=T/N$, $B=k/N$, and $\kappa=K/k^2$. The Gauss equation gives $L=k(p^2/B+\kappa B)$. In the chosen orthonormal frame the two Codazzi equations are
$$
 T_v=a^{-1}L_\theta-2(a'/a)T,\qquad
 N_v=a^{-1}T_\theta+(a'/a)(L-N).
$$
Eliminating $L$ and substituting the actual $p,B$ gives a system polynomial in its unknowns:
$$
 \begin{aligned}
 a p_v&=p p_\theta+\kappa B B_\theta-a'p(1+p^2+\kappa B^2),\\
 a B_v&=p B_\theta-B p_\theta-a'(p^2-1+\kappa B^2)B,\\
 p(0,\theta)&=p_0=-\cot\phi,\qquad B(0,\theta)=B_0=\csc^2\phi .
 \end{aligned}
$$
The initial functions obey $p'_0=B_0$, $B'_0=2p_0B_0$. For the flat extension $a=a_f$, $K=0$, these functions solve the system identically in $v$.

Here is a uniform analytic radius with constants. Fix an arbitrary real center in the stated bands. On its complex disk of radius $\rho=.04$, $|p_0|<2.40$, $|B_0|<6.25$. For example $|\sin\phi|\ge\sin(.46)-.04\cosh(.04)>.403$ and $|\cos\phi|\le\cos(.46)+.04\cosh(.04)<.94$. On $|v|\le v_0=.00016$ the polynomial gives $|\alpha'|<.575$, $|\alpha|<.000093$, $|a|>.358$, $|a'|<1.001$, and $|\kappa|<.009$ (use the actual lower $k\ge .010/.0752$). For $|p-p_0|<.5$, $|B-B_0|<2$, the two unknowns have absolute bounds $2.90,8.25$. Normalize
$$
 Z=(\theta-\theta_c)/\rho,\quad V=v/v_0,\quad
 w_1=2(p-p_0),\quad w_2=(B-B_0)/2 .
$$
Each coefficient of $w_{j,Z}$ and each inhomogeneous term in either $w_{i,V}$ has modulus at most $M=.06$ on the unit polydisk in $(Z,V,w_1,w_2)$. For the derivative coefficients use the four entries $p,\kappa B,-B,p$ divided by $a$, multiply by $v_0/\rho$ and by the ratio of the dependent-variable scales. For the sources use $|p'_0|\le6.25$, $|B'_0|\le30$. Before scaling they are respectively bounded by
$$
 [2.90(6.25)+.009(8.25)30+1.001(2.90)(1+2.90^2+.009(8.25)^2)]/.358<142,
$$
$$
 [2.90(30)+8.25(6.25)+1.001(2.90^2+1+.009(8.25)^2)8.25]/.358<625 .
$$
Multiply these by $v_0/.5$ and $v_0/2$.

Cauchy coefficient estimates and the power series recursion in $V$ now majorize the two zero-initial unknowns coefficient by coefficient by the nonnegative solution
$$
 W_V=M(1+2W_Z)/(1-Z-V-2W),\qquad W(Z,0)=0.
$$
Indeed the Taylor majorant for each coefficient on the four-variable unit polydisk is dominated by $M/(1-Z-V-w_1-w_2)$, and taking one $Z$ derivative preserves the domination. To see convergence directly set $H=Z+2W$. Characteristics give
$$
 H=Z-2M\log[1-V/(1-H)].
$$
For $|Z|\le.04$, $|V|\le.43$, the right side maps $|H|\le.45$ into itself and has derivative modulus $<.79$ there: use $.04+.12[-\log(1-.43/.55)]<.23$ and $.12(.43)/(.55\cdot .12)<.79$. This supplies the analytic branch and the summable majorant, including $|W|<.1$ for the two scaled unknowns by the logarithm bound. Recursion by increasing powers of $V$ computes the solution without a nonlinear shooting choice. Neighboring germs agree on their common real intervals by this same recursion and analytic continuation. These bounds and uniqueness are uniform in the actual continuous phase. They also hold about both choices of sign of $\phi$.

On the real interval $0\le v\le.43v_0=.0000688$, $B>2.2$, $|p|<2.12$, $B<5.4$. Consequently $N=k/B$, $T=pN$, $L=k(p^2/B+\kappa B)$ have absolute principal values less than $1.2$, using the maximum absolute row sum. In particular no denominator vanishes. For reconstruction let $E,G,n$ denote the unit radial tangent, unit angular tangent and chosen normal. Solve
$$
 E_v=Ln,\quad G_v=Tn,\quad n_v=-LE-TG,\quad F_v=E
$$
from the actual disk position, its two tangent vectors and its normal at $v=0$. The orthonormal frame is preserved. Gauss and Codazzi are the compatibility equations of the two Gauss–Weingarten systems; explicitly the angular equations are $E_\theta=a'G+aTn$, $G_\theta=-a'E+aNn$, $n_\theta=-aTE-aNG$. The difference between their two sides solves a homogeneous linear system in $v$ with zero initial data, so $F_\theta=aG$. This proves all three metric entries. At $v=0$, $L=T^2/N$ equals the actual cap radial normal curvature, giving all three second derivatives of the cap on the material overlap. The prescribed cap and the continued roll therefore join in $C^2$. No limiting normal field at a zero of $N$ was used. For other open true clock-polynomial pieces with nonzero $N$, the same polynomial system supplies local analytic continuation from their own data, with a radius depending on their center and phase.

## A complete closed modification with simultaneous thickness

Use the R785 two-cap shear at $\xi=.02$ as the full exterior reference, with its four MILD angles, initial R781 $g_0$, signed tube $>1/24.36$, held distance $>.320$ and quotient $>.086$. On either cap the physical position at $v=0$ is the $D$ above. The unsolved mixed coefficient of that actual shear is already nonzero in our bands when $v,t>0$. In one active coordinate its ambient pullback adds $2\sin\beta\,du\,dY$ to the Euclidean metric, and here $u_\theta\ne0$, $Y_\theta=0$, $Y_v=\mp\sin\alpha\ne0$. The analytic replacements eliminate this actual error on their plateaux.

Here are explicit, deliberately conservative global gluing sizes. Put $r=.00005$, $h=.00000005$, $z_*=2h/r=.002$. Let $\Delta$ be the analytic position above minus the R785 position on the same roll. On $|\theta-\theta_c|\le.0008$, $|v|\le r$ one has $|\Delta_i|\le5r^2$ in each Cartesian component. To verify this bound, the two fields have equal position and first radial derivative on the seam. The complex second radial derivatives are each bounded by $5$. For the constructed field use $F_{vv}=Ln$: the preceding estimates give $|p|<2.45$, $|B|<6.45$, $|B|>1.9$ on this smaller disk (here $|B_0|\ge1/(\sin(.69)+.001)^2$). Hence $|L|<1.12$, $|T|<.44$, and the initial complex frame entries have modulus $<1.1$ from the explicit unit-speed map; the linear frame equation changes that bound by a factor below $\exp(.0001) \exp(.0001)$. For the original field use $|a'|<1.001$ and $|a''|,|Y''|<.576$, together with the true linear-piece $|\beta'|<.333$, $|\sin\beta|<.03$, $|\cos\beta|<1.001$ on the stated disk. Bound after double integration on each complex $v$ radius.

The difference actually vanishes to order five. For the flat continuation $F_f=D(a_f(v)n_\theta)$, $p_0,B_0$ are exact. Since $\alpha=O(v^4)$, $a'-1=O(v^8)$ and $K=O(v^7)$, the recursions give $p-p_0,B-B_0=O(v^8)$, $L-L_f=O(v^7)$. Integrating the frame ODE gives $F-F_f=O(v^9)$. For R785, the radius differs from $a_f$ by $O(v^9)$ and the world axial roll departure is $O(v^5)$. The same orders hold on the complex germ. Hence the first possible coefficient of $\Delta$ is that of $v^5$.

Multiply $\Delta$ by a phase factor rising from zero at $\pi/4$ to one at $\pi/3$, an angular factor equal to one on $.48\le|\phi|\le.67$ and zero outside $.46\le|\phi|\le.69$, and a radial factor equal to one on $[0,h]$ and zero at and beyond $2h$. Use clipped quintic smoothsteps on each indicated transition. Extend the correction by zero to the disk. Every cap material point remains at its R785 position and all original cap two-jets agree. Both heads and all eight bands per head may be treated simultaneously.

For detailed bounds write $q=|v|/r\le z_*$. Cauchy on the preceding polydisk and the first four zero coefficients give, per component,
$$
 |\Delta|\le 6r^2q^5,\quad |\Delta_v|\le30r q^4,\quad
 |\Delta_{vv}|\le110q^3 .
$$
For $j$ added angular derivatives of the first two inequalities use the factor $j!/(.0008)^j$ and total order at most two. These follow by differentiating $\sum_{n\ge5}5r^{2-n}v^n$. The radial cutoff has first two derivative bounds $2/h,6/h^2$. In particular the cut second $v$ derivative is at most $(110+240+144)z_*^3<4\cdot10^{-6}$. Angular cutoff bounds are $100,15000$. The same inequalities give every first derivative in $(\theta,v)$ and the value below $10^{-10}$, and each second derivative below $5\cdot10^{-6}$.

Extend this displacement to world space as follows, to control all ordered normal chords. Invert the two independent one-dimensional transverse coordinates of the R785 shear (their derivatives are at least $\cos(.025)$), and subtract its two height terms to recover the unsheared $Y$. On the resulting transverse annulus read $\theta$ and $v=a^{-1}(\sqrt{X^2+Z^2})$, extending by zero below $a_b$. Cut the correction to the corresponding upper or lower terminal plane by a smoothstep gate which is one within $.01$ and zero outside $.03$ of that plane in recovered $Y$. These gates are disjoint, cover the corrected part of the true rolls at unit value, and miss the entire central body. On the support, the map to $(\theta,v,Y)$ has Euclidean derivative norm $<10$ and each component Hessian norm $<100$: polar inverse radius is $<2.8$, $a'>.999$, $|a''|<.576$, the transverse inverse slopes are $<1.001$, their second derivatives are $<.01$, and each recovered height has second derivative $<.34$. The $Y$ gate has derivative bounds $100,15000$. The angular supports are disjoint. The displayed bounds give a global world displacement $d$ with $\|Dd\|<10^{-7}$, $\|D^2d\|<.01$ (even using three component rows, all nine chart Hessian entries at their maximum, and the norm bound $10^2$). Also $\|d\|_\infty<10^{-10}$.

For any compact embedded reference of reach $\rho$ and such an ambient $I+d$, the new reach is at least $(1-\|Dd\|)^2/[(1+\|Dd\|)/\rho+\|D^2d\|]$. Indeed a target normal annihilates the transformed tangent plane, giving the old directed normal-chord estimate times $\|I+Dd\|$ plus the Taylor remainder; each transformed chord has length at least $(1-\|Dd\|)$ times its initial length. This gives the claim via the ordered normal-ball criterion, and the strict Lipschitz bound also gives global embeddedness. Thus the amended full family has reach $>1/24.38>.03D$ with the same initial diameter $D<1.362$. The Hausdorff motion and quotient each lose at most $2\|d\|_\infty$ by the triangle inequality, so the held distance exceeds $.319$ and the quotient exceeds $.085$. The common fixed cap grip is unchanged and has diameter at least $2a_b/\sqrt2>.50>.2D$.

This gives all three original metric rows on two complete moving caps and, for $t\ge\pi/3$, on their genuine curved open extensions of width $h$ in sixteen angular bands in the single closed family. The larger local width $.0000688$ and complete saturated sectors are separate exact patch conclusions. The construction gives neither uniform continuation across all inner clock joins, saturated transitions and the four flap switches, nor an all-roll match at the central boundary. At phases approaching zero the chosen Cauchy constant degenerates with $k$; the closed field there uses the actual R785 exterior. Its remaining relative metric supremum has not been controlled to the topic threshold.

## Finite Taylor field for full-sphere refinements

The exact cap-first field has a particularly simple first nonzero term beyond the flat developed continuation. With $\alpha_4=2.5/(.09\,\eta^3)$,
$$
 F-F_f={\alpha_4^2\over18a_bN_0}\,v^9 n_0+O(v^{10}),\qquad
 N_0=k\sin^2\phi .
$$
Indeed $K=(4\alpha_4^2/a_b)v^7+O(v^8)$. The changes in $p,B$ start in degree eight, so $L-L_f=4\alpha_4^2v^7/(a_bN_0)+O(v^8)$. The normal changes from its flat continuation in order eight. Integrate $E_v=Ln$ and $F_v=E$ twice, giving the factor $4/(8\cdot9)=1/18$. The initial normal is $n_0=-\sin\beta\,\ell+\cos\beta\,e_Y$ for each of the four signed directions and both caps.

The executable companion evaluates this term and differentiates the actual resulting position, including both spatial cutoffs and its phase gate. It is intended on the R786 delayed flat continuation, where $F_f$ is the actual exterior in these bands for $t\ge\pi/4$. For $r=.00005$, the same complex polydisk bounds $|(F-F_f)_i|\le5r^2$ by double radial integration. After subtracting the displayed term its Taylor series starts in degree ten. On $v\le2h$, Cauchy therefore gives per-component position, first and second radial remainder at most $6r^2q^{10},55rq^9,500q^8$, respectively, with $q=v/r$. The radial product rules for the cutoff cost at most $(500+440+144)(.002)^8<3\cdot10^{-19}$ in second radial derivatives. The angular product rules with the preceding Cauchy width and $\partial_e=\partial_\theta/.45$ bound every cut position and spatial derivative through order two by $10^{-17}$ in the actual $(e,b)$ coordinates relative to the cut exact replacement. These are bounds on mathematical evaluation of the finite field; rounding of quadratures and sums in a working solver is separate. This explicit ninth-order germ does not imply that a central or remaining roll correction is small.
