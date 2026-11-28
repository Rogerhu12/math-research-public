# R765. An exact signed-ratio development on almost all of each full roll and a global rotation equation

The fixed material sphere $M$ and its metric $g$ are the actual R757 initial closed surface, including the graph heights of both caps. The phase is the full interval $0\leq t\leq\pi/2$. All statements of exactness below use exact integrals of the specified real functions. The source evaluates those integrals with split Gaussian rules. The reference is continuous in $C^2$ and the resulting metric identities apply at finite phase. A full spherical isometry, a positive reach for the new reference and embedding of its two altered cap collars are open.

## The signed-ratio central curve

Use the original material track and sign conventions of R759. Its old projected coordinate is $0\leq x\leq U=1.30$ and each of its eleven identical cells has width $b=U/11$. On a cell $x=b(j+a)$, $f=.04b^2[4a(1-a)]^5$, the old tangent slope is $f_x$, its speed is $e=\sqrt{1+f_x^2}$, and its signed curvature with $n'=k_0T$ is $k_0=-f_{xx}/e^3$. The two tracks have opposite oriented tangent vectors at equal increasing $x$. On their complementary heads retain the original curvature. The axial coordinate there is $y$. The right head is fixed in the world throughout.

Set $h=.024$ and $S(a)=35a^4-84a^5+70a^6-20a^7$ on $[0,1]$, extended by $0,1$ at the two ends. On an interval $(l,r)$ put $H_{lr}(a)=S((a-l)/h)S((r-a)/h)$. Let $H_+$ be the sum of these functions on $(0,1/3),(2/3,1)$ and $H_-$ the one on $(1/3,2/3)$. These names denote increasing and decreasing heading; $k_0<0$ on the first set and $k_0>0$ on the second. Define the strictly positive constants
$$
m_\pm=\int_0^1 \frac{\pm b f_{xx}(ba)}{1+f_x(ba)^2}\,H_\pm(a)^8\,da .
$$
Choose positive integers $j_+,j_-$ with $j_++j_-\leq11$. For the first $j_+$ cells use $\mu=\theta H_+^8/(j_+m_+)$, for the last $j_-$ use $\mu=\theta H_-^8/(j_-m_-)$ and elsewhere use $\mu=0$, where $\theta=\theta_*\sin t$. Prescribe the excess heading $\psi(0)=0$ by
$$
\psi_x=\mu\,f_{xx}/(1+f_x^2).
$$
Each rising cell contributes $\theta/j_+$; each descending cell contributes $-\theta/j_-$. In between $\psi=\theta$ and both outer endpoints have $\psi=0$. Rotate the original two tangent vectors by this same $\psi(x)$ and integrate in arclength. Their vector displacement changes cancel exactly on the whole loop. The right head is stationary; the left translates by the negative of the total upper-track displacement change. At the four head joints, $\mu$ vanishes with its first two derivatives and the headings agree. The new periodic unit curve satisfies
$$
 k_t=(1+\mu)k_0,\qquad \lambda=(1+\mu)^{-1},\qquad
 z=\sqrt{1-\lambda^2}
   =\frac{\sqrt c\,H_\pm^4\sqrt{2+cH_\pm^8}}{1+cH_\pm^8},
 \quad c=\frac{\theta}{j_\pm m_\pm}.
$$
Here $z=0$ off the controlled cells. These formulas extend through every original curvature zero without division by a curvature. The central cylinder $F=(q_t(s),y)$ has the entire initial metric $ds^2+dy^2$. Its right open grip has diameter at least $.72$ as in R759.

For $j_+=j_-=2,\theta_*=.78$ the head displacement remains macroscopic. The density of heading change in each of the four cells is symmetric about its midpoint, so the average heading is the arithmetic mean of the cell endpoint values. By concavity, the sine integral is at least the trapezoidal endpoint-sine average times $b$. Using $|f_x|<.0201$ from R757,
$$
 D_z\geq b[7\sin .78+2\sin .39+\sin .78]-.0201U(1-\cos .78)>.74,\qquad
 |D_x|\leq U(1-\cos .78+.0201\sin .78)<.397 .
$$
The final lower-left central endpoint at $y=0$ has $x<-.603,z<-.91$. The complete initial R757 image below $x=.18$ has $z\geq-.171$, while the part with $x\geq.18$ is horizontally more than $.783$ away. Thus the directed final-to-initial whole-image distance is $>.739>.2D$ for this trace, using the original $D<3.50$. This result survives arbitrary changes of the two positive-phase rolls and caps that keep this central material trace and the original initial surface.

## Complete meridians and the exact set of angular equations

Write $v\in[0,L]$ for the unchanged R757 physical roll coordinate, $d'=\sin\alpha,\ p'=\cos\alpha$, $d(0)=p(0)=0$, with $\alpha(0)=0,\alpha(L)=\pi/2,\alpha'(0)=\alpha'(L)=0$. Its target is $A^2ds^2+dv^2$, $A=1-dk_0>0$. The old axial central half-width is $Y=.37$. On either *entire* roll set
$$
 P(s,v)=\int_0^v\sqrt{\cos^2\alpha(u)+z(s)^2\sin^2\alpha(u)}\,du,\qquad
 F=(q_t(s)-\lambda(s)d(v)n_t(s),\ \pm(Y+P(s,v))).
$$
The ordered pair denotes the planar profile-plane vector and the axial component. In vector notation its actual derivatives are
$$
 F_s=(A T_t-\lambda_s d n_t,\ \pm P_s),\qquad
 F_v=(-\lambda d'n_t,\ \pm P_v).
$$
Indeed $\lambda k_t=k_0$ holds globally. Consequently
$$
 g_{vv}=1,\qquad g_{ss}=A^2+\lambda_s^2d^2+P_s^2,\qquad
 g_{sv}=\lambda_s\lambda dd'+P_sP_v .
$$
Every meridian has its original length. Wherever the multiplier is constant in $s$, all three original equations hold through the full closed interval $0\leq v\leq L$. This includes nontrivially changed arcs of both signs, every untouched head, and intermediate constant-heading cells. At transition endpoints the same equations follow by continuity. In particular these controls do not require the elliptic sign change excluded in R759.

For $j_+=j_-=2$, on a rising cell only $4h$ of its dimensionless width can have derivative of $H_+$, on a descending cell only $2h$. Counting both tracks gives old total exceptional width at most $2b(2\cdot4h+2\cdot2h)=.576b$. In actual arclength this is $<.069$ since $e\leq\sqrt{1+.0201^2}$. On each roll the exceptional label strip has original area fraction
$$
 \frac{\int_0^L\int_{\rm exceptional}(1-d k_0)\,ds\,dv}
      {\int_0^L\int_0^{P_0}(1-d k_0)\,ds\,dv}
 \ <\ \frac{.069(1+.1093\cdot6.91)}{4-2\pi\cdot.1093}<.037 .
$$
Here $P_0>4$ is the R757 true period and $\int k_0\,ds=2\pi$ in its orientation. Thus *more than 96.3 percent of the material area of each whole roll* is exactly isometric for the complete motion. The remaining area has genuine positive circumferential cost when $v>0$ and $\lambda_s\ne0$; in particular a change of angular label alone cannot remove its excess length.

For regularity put $B(z,\alpha)=\sqrt{\cos^2\alpha+z^2\sin^2\alpha}$. Away from $(z,\cos\alpha)=(0,0)$ one has $|B_z|\leq1$, $0\le B_{zz}\leq1/z$ for $z>0$. At a cutoff $z=O(\sqrt c H^4)$, $z_s=O(\sqrt c H^3)$ and $z_{ss}=O(\sqrt c H^2)$, with $z_s^2/z=O(\sqrt c H^2)$ from the displayed positive factorization. Thus $B_z z_s$, $B_z z_{ss}+B_{zz}z_s^2$ extend by zero across a cutoff, uniformly in $v$. The same bounds go to zero uniformly as $t\downarrow0$. The mixed derivative $P_{vs}=B_z z_s$ is continuous. The expression $P_{vv}=-(1-z^2)\sin\alpha\cos\alpha\,\alpha'/B$ extends by zero at $v=L$ since $|\cos\alpha|/B\leq1$ and $\alpha'(L)=0$. At $v=0$, $P=0,P_v=1,P_{vv}=0,d=d'=d''=0$. Differentiation under the integral is justified by the uniform bounds. All these conclusions concern the full two-variable second jets and give continuity in the $C^2$ topology for the compact phase interval.

## A center curvature test and a second finite strong control

The preceding $2+2$ multiplier with constant plateau values has a strict local thickness obstruction at the midpoint of a falling cell. There $k_0=1.6,H_-=1$ and
$
 m_-\leq 2\arctan\bigl(.04b(20/3)(8/9)^4\bigr)<.040 .
$
Indeed the ungated integral of $-d\arctan f_x$ from $a=1/3$ to $2/3$ is precisely the displayed turning angle. At the last phase the central cylinder therefore has a principal curvature $>1.6(1+.78/.080)>17.2$. The reach of a $C^2$ embedded surface is bounded above by the reciprocal of every nonzero absolute principal curvature (take the tangent limit in the ordered tangent-ball inequality). The initial two rim heights already differ by $2(Y+p_b)>2$: the $.81$ extra transverse material lies at angle at most $1/1024$ and contributes at least $.81\cos(1/1024)$ to $p_b$. Hence even $.03D>.06$ exceeds $1/17.2$. Positive-phase end corrections leaving this $2+2$ central trace cannot meet the reach target.

A second actual control on exactly the same $g$ pays the strong displacement and the central local curvature bound simultaneously. Set $j_+=2,j_-=3$, edge width $.006$, $\theta_*=.78$, $\varepsilon=10^{-6}$, and use the smooth positive factor
$
 b_0(s)=[\varepsilon+\sqrt{k_0(s)^2+\varepsilon^2}]^{-1}.
$
In the turning masses and multiplier replace $H_\pm^8$ by $H_\pm^8 b_0$. This changes the finite positive-phase reference, with $F_0$ unchanged. The density remains symmetric on each cell and $k_t=(1+\mu)k_0$. Every meridian and every constant-multiplier arc, both cap cores and all matching equations above stay exact. The 96.3 percent area estimate pertains to the first control. Inside the bounded control's active regions, $b_0$ varies and its true derivatives contribute to both angular and mixed rows.

To bound the peak put $u=4a(1-a)$. The exact second derivative is $f_{xx}=12.8u^3-14.4u^4=3686.4a^3(1-a)^3(a-1/3)(a-2/3)$. Its positive maximum is below $.95$ and its negative minimum is $-1.6$. Division by $e^3$ only decreases the magnitude. Each new mass is the integral of $b e H_\pm^8 |k_0|/(\varepsilon+\sqrt{k_0^2+\varepsilon^2})$ over the unit cell. In the decreasing-heading cell on $[1/3+.014,2/3-.014]$ the cutoff equals one, $a(1-a)\geq2/9$ and $|(a-1/3)(a-2/3)|\geq .014(1/3-.014)$. Hence $|k_0|>.17$ and $m_->.03595$. For the positive heading use $[.04,.32]$ and its reflection, of total length $.56$. There $a(1-a)\geq.0384$, $|(a-1/3)(a-2/3)|\geq (1/3-.32)(2/3-.32)$, giving $|k_0|>.0009$ after $e^3<(1+.0201^2)^{3/2}$. This yields $m_+>.0659$. Since $|k_0|b_0<1$, on all central material the nonzero principal curvature is at most
$
 \max\{6.91,\ .95+.78/(2\cdot.0659),\ 1.6+.78/(3\cdot.03595)\}<8.84 .
$
This is below $1/(.03\cdot3.50)$; focal curvature of the central cylinder satisfies the required local inequality. The full ambient tube, including all extra pairs and both rolls and caps, still needs its own proof.

There are now six plateau cells. The same symmetric trapezoidal estimate gives
$
 D_z\ \geq\ b[7\sin(.78)+\sin(.39)+\sin(.26)+\sin(.52)]-.0201U(1-\cos(.78))>.706 .
$
Use $\sin(.78)>.703,\sin(.39)>.380,\sin(.26)>.257,\sin(.52)>.496,\cos(.78)>.710$. Again $|D_x|<.397$; the same initial-image separation certifies $\delta_{\rm hold}>.705>.2D$. The capped multiplier is smooth, with bounded derivatives for fixed positive $\varepsilon$. In the preceding endpoint regularity proof for $z$, the additional factor $\sqrt{b_0}$ is smooth, bounded and positive on each active compact arc, so all the $H$-orders and joint continuity assertions persist.

## Both entire material caps

At the true roll end $d_b=d(L)$ and $P_b=P(s,L)$. Continue the ending physical meridian across the common rim by the true two-jet model
$$
 N_t(s,w)=(q_t-\lambda(d_b+w)n_t,\ \pm(Y+P_b+wz)),\qquad w\geq0.
$$
The roll has $F_v=(-\lambda n_t,\pm z)$ and $F_{vv}=0$ there. The $s$ derivatives and the mixed derivative are those of the same displayed expression. Write $N_0$ for its initial member. On the *original* material cap $F_0^{\rm cap}(s,w)$ use the total translation vector $h_t=(-D_x/2,\mp c_0\sin t,-D_z/2)$ in world $(x,y,z)$ order, with $c_0=.23$ or another supplied control. Set
$$
 F_t^{\rm cap}=F_0^{\rm cap}+h_t+
 [1-S(w/.19)](N_t-N_0-h_t).
$$
Use the original polar-chart coordinate $w=1-v$ and the original normal-chart coordinate $w=v$. In its regular Cartesian core the translation formula applies where $w\geq.19$. In the relevant chart overlap use the identical original material label $w$ obtained from its original planar cap map. The original normal cap and $N_0$ differ by a graph height with vanishing two-jet on the entire rim; the marked radius-$.04$ height is away from there. The cutoff equals one to second order there. All four seams, including both axial signs, therefore glue through their two spatial derivatives and both entire caps recover the original initial metric at $t=0$. On the portion $w\geq.19$ the complete true nonflat cap metric is exactly preserved at every phase. On the remaining material portions of both caps the full three tensor entries must be paid. No claim about regularity of the map *as an immersion* follows from matching the jets if the interior collar folds.

## The exact full-sphere rotation equation and the roll development

For this paragraph $F_0$ is the true oriented R757 initial sphere. A $C^1$ map $R:M\to SO(3)$ determines the vector one-form $\omega=R\,dF_0$. An oriented $C^2$ immersion with that differential exists exactly when
$$
 \partial_s(RF_{0,v})-\partial_v(RF_{0,s})=0
$$
in every regular chart. Necessity is equality of mixed derivatives. Sufficiency follows by integrating the closed vector-valued form from a fixed point: $M$ is a sphere, so its first de Rham cohomology is zero. Equivalently integrate along paths and use Stokes on contractible loops. Regularity and the exact metric follow from $R\in SO(3)$ and $dF_0$ of rank two. Conversely the two oriented tangent frames of any $C^2$ same-metric immersion and $F_0$, completed by their oriented unit normals, define a unique global $C^1$ rotation. This expression is independent of the tangent frame used on each overlap. A compatible continuous-in-$C^1$ family integrates to a continuous-in-$C^2$ family after one common world-point normalization. If $R=I$ on the connected fixed grip $H$, that normalization there fixes all of $H$. On the hard central trace the actual rotation is the rotation in the profile plane by $\psi(s)$ (identity on the stationary head). The conditions apply through both cap edges as well as the two regular cap centers.

For an exact roll another equivalent development has a single geometric unknown, a family of spatial curves $F(s,v)$. Put $T=F_s/|F_s|$, $C=(I-TT^T)F_{ss}/|F_s|^2$, $H=-A_v/A$. Where $C\ne0$ and $|C|\geq |H|$ the allowed meridian velocity is exactly
$$
 V=H C/|C|^2+\epsilon\sqrt{1-H^2/|C|^2}\,(T\times C)/|C|,
 \qquad \epsilon\in\{-1,1\}.
$$
For $F_v=V$, one has $|V|=1,V\cdot F_s=0,C\cdot V=H$ and, by differentiating the orthogonality in $s$, $\partial_v\log|F_s|=-C\cdot V=A_v/A$. Since $|F_s(s,0)|=A(s,0)=1$ the entire target follows. The converse uses the same identities. At zero curvature retain the undivided three constraints on $V$; if $C=0$ then necessarily $H=0$. This direction equation alone gives no regular continuation across a zero or a grazing characteristic. The constant-ratio pieces above realize its full material length without a continuation assertion.

## A coercive simultaneous numerical problem

Let $J=[F_s,F_v]$, $J_0=[F_{0,s},F_{0,v}]$ and take an upper-triangular frame change $W$ making $U_0=J_0W$ orthonormal. For $Z=JW$ choose its nearest orthonormal two-frame $Q$ (a thin singular value decomposition gives $Q=UV^T$). Complete each of $U_0,Q$ by its oriented unit normal to obtain the proper rotation. For singular values $\sigma_1,\sigma_2$ of $Z$,
$$
 \min_{R\in SO(3)}|Z-RU_0|_{\rm F}^2
       =(\sigma_1-1)^2+(\sigma_2-1)^2 .
$$
Indeed maximizing the trace pairing with a two-frame yields $\sigma_1+\sigma_2$ and its extremal frame extends to a proper three-dimensional rotation. The relative Gram spectral error is $\max_i|\sigma_i^2-1|$, bounded by $2e+e^2$ with $e^2$ the right side. This remains valid if the physical map is singular at a tested point (a nearest frame need not be unique). Integration of arbitrary independently projected rotations is not justified. In the simultaneous problem the actual unknown field is a single full physical position field joined to second order at both true rims. Its tangent derivatives are taken from that same field on all charts, with the analytic hard central trace. For frozen rotations, their metric-distance objective is a genuine linear least-squares problem in the full spatial and temporal position coefficients. On a regular phase evaluate the integrability defect of the projected form in addition to the physical Gram error. True full-domain bounds, reaching zero along fixed-input refinements, and positive tube and rigid-quotient bounds for the optimized field still require independent evidence. R761's quantitative enclosed-volume bound applies to its own specified physical family.
