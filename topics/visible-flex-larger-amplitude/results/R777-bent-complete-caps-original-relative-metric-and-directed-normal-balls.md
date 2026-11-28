# R777. Bending both complete caps on the original R764 metric, with a shared terminal collar and a full Cartesian correction

Use throughout the actual R764 initial tensor $g_0$ on the once-marked material sphere. Thus $B=.88$, $E=.44$, $L=.132\pi/2+.0005$, $T=E+L$, and both original closed R760 cap disks have their actual small curved bowl and outer normal collar. No amplitude, height, tensor, phase range or material ratio is changed under refinement. R774 proved that its hard final central trace cannot be connected to any one rigidly moved original cap: an upper/lower midpoint separation would have to increase by more than $.005$. Here the actual cap pair increases this separation by more than $.086$; the increase is placed in the required horizontal projection by one spatial motion of each whole cap. The original and new cap tensors, their relative operator norm on the whole disks, and the normal-ball estimates are computed in physical coordinates. A small fixed residual and a refinement to a truly common metric are different requirements.

## 1. True cap graph and a finite bending path

Use the positive end's outward Cartesian coordinate $y$; at the negative end use $-y$. Set $b_0=p_E+p_b$, $y_b=B+b_0$, with the actual R764 pre-roll displacement $p_E$ and standard terminal displacement $p_b=d_b\in[.132,.1325)$. At zero phase the positive cap is
$$
       (x,y_b+f(x,z),z),\qquad (x,z)\in\overline\Omega .
$$
Here $\Omega$ is bounded by the true inward parallel $q_0-d_bN_0$. R760 gives the complete graph in the regular Cartesian center and the two overlapping rim charts. In the physical collar $f=1.5\,10^{-6} S_7(w/.007)$ plus the actual $10^{-9}$ cutoff term with zero transverse two-jet at both ends. In the interior it is the height plateau plus the true cut-off elliptical bowl of amplitude $.000025$. The R760 physical calculation gives
$$
 |f|<.000030,\qquad |\nabla f|<.00075,\qquad \|\nabla^2 f\|<1.89 .        \tag{1}
$$
For the last relaxed constant one may also use the R760 principal bound $1.87$ and the graph inequality $\|\nabla^2 f\|\le(1+|\nabla f|^2)^{3/2}\max_i|k_i|$. The original value, gradient and Hessian of $f$ are zero on the entire outer rim; its extension by zero to the rest of the Cartesian plane is $C^2$ and obeys the same bounds. This extension is used for estimates on both nonconvex material disks.

Write $S(t)=10t^3-15t^4+6t^5$ extended by its constant endpoint values. For the full physical phase $0\le\theta\le.90$, put
$$
 a(\theta)=1-(1-2^{-12})S(\theta/.075),\qquad
 k(\theta)=S((\theta-.075)/.825).
$$
The crown retains a positive copy of its original physical height. To define its bend take $r=.245$, ramp $e=.015$, and let $A(v)$ be the softened quarter-turn from zero to $\pi/2$ on $[0,r]$. Its speed rises by $S$ through length $e$, stays constant in the middle and falls symmetrically at the end, with peak $K_b=\pi/[2(r-e)]<6.84$. The angle is continued by constants. On all real $z$ take
$$
 \beta(z)=-k\,\mathrm{sgn}(z)[A(|z|)-A(|z|-.58)],\qquad
 Y(z)=\int_0^z\sin\beta(w)\,dw,\quad Z(z)=\int_0^z\cos\beta(w)\,dw .
$$
$Y$ is even, $Z$ odd, $|\beta|\le\pi/2$, $|\beta'|\le6.84$, $|\beta''|<856$. The two smooth bends have disjoint supports. The soft origin has a classical two-jet on both sides. The returning bend is important since the very highest parts of the actual cap must also fit in a finite outward interval.

For $T_z=(\sin\beta,\cos\beta)$ and $N_z=(\cos\beta,-\sin\beta)$ in the $(y,z)$ plane make the single ambient map
$$
 \Psi(x,\eta,z)=(x,\;Y(z)+\eta\cos\beta(z),\;Z(z)-\eta\sin\beta(z)).
                                                                        \tag{2}
$$
On the cap use $\eta=a f$. On the actual final part of the old standard roll use $\eta=y_{\rm old}-y_b$, with the true initial abscissa and height $z_{\rm old}$. Both then use the same rigid pose described below and the same final global rotation from the stationary grip construction. During the initial crown-height change $k=0$, so (2) is an exact rigid Cartesian frame on the roll. At the seam $\eta=f=0$, and the original transverse cap height and its first two derivatives vanish. The original roll velocity is the inward planar normal at its endpoint, also with transverse acceleration zero. The chain rule for the same smooth $\Psi$ on both sides gives the full position, both first derivatives and all three second derivatives there, for either signed end. Each cap Cartesian overlap is the same spatial composition of the old physical graph. This construction changes the whole cap's spatial position and its boundary; there is no displacement fade at its rim.

The ambient pullback in $(x,\eta,z)$ is
$$
 \Psi^*I=dx^2+d\eta^2+(1-\beta'\eta)^2dz^2,                              \tag{3}
$$
since $T_z'=\beta'N_z$, $N_z'=-\beta'T_z$. Consequently the actual difference on the whole cap is
$$
 g_\theta-g_0=\big[(1-\beta'a f)^2-1\big]\,dz^2+(a^2-1)\,df^2,
 \qquad g_0=dx^2+dz^2+df^2.                                             \tag{4}
$$
The dual $g_0$ norm of $dz$ is at most one and $|df|_{g_0}^2=|\nabla f|^2/(1+|\nabla f|^2)$. On the first interval $\beta'=0$, so the operator norm relative to the true $g_0$ is exactly $(1-a^2)|\nabla f|^2/(1+|\nabla f|^2)<5.625\,10^{-7}$. Wherever the bend is active $a=2^{-12}$, so (1) and the triangle inequality for the two rank-one tensors give on every cap and at every material point
$$
 \|g_0^{-1/2}(g_\theta-g_0)g_0^{-1/2}\|_{\rm op}
 \le (.00075)^2+2(6.84)(.000030)2^{-12}
                   +[(6.84)(.000030)2^{-12}]^2
 <6.64\,10^{-7}.                                                        \tag{5}
$$
This is a coordinate-invariant whole-metric bound, even in the old polar charts. During bending the uncorrected field retains a fixed residual from the true old tensor on the parts where $df\ne0$.

On the common complete final collar $T-h\le u\le T$, $h=.00013$, use the exact original transverse velocity $\cos\alpha(u)$ with $\alpha(T)=\pi/2$, $|\alpha'|\le1/.132$. Hence $|\eta|\le h^2/(2(.132))$. Restricting (3) to any old unit tangent gives
$$
 \|g_0^{-1/2}(g_\theta-g_0)g_0^{-1/2}\|_{\rm op}
 \le 2(6.84)h^2/.264+(6.84h^2/.264)^2<8.8\,10^{-7}.                    \tag{6}
$$
This holds for every angular label on both actual curved rolls, at every phase. It includes the seam itself, where the ambient differential is orthogonal. The new rank-one term in (3) comes from differentiation in the true physical $z$ direction, irrespective of the angular and radial components of either material chart.

## 2. Exact change in the material midpoint separation

Take the actual cap pair from R774 §4 on a single signed end. For each label average its upper and lower representative, never opposite signed caps. At the left pair $Q_{+,\pm}$ the old coordinates are $x=.30$, $z=\pm z_l$, $z_l=.71-d_b>.5775$. On the right use the end of the complete first positive physical wall pulse, before the first negative stroke. Here the old planar normal points along $x$. The old cap abscissa is $X_{R,0}-d_b$, and its old positive height $z_r$ equals the remaining vertical travel on the genuine two negative heading changes and the final zero dwell. Thus
$$
 .255<.001+2(.71/5.4+.0004)\cos(.35\cdot.71)
       \le z_r\le .001+2(.71/5.4+.0004)<.265 .
$$
We used the already proved $\gamma_0<.35$. The old horizontal span $d=X_{R,0}-d_b-.30$ is positive. It is less than $.519$ because the old ascending tongue has abscissa at most $.30+.26/\sqrt2$, the U-turn adds at most $.301$, and at the old positive wall pulse the excursion is less than $.1651$ by R774. The true upper bound $.26/\sqrt2$ on the disk-bend abscissa follows by its complementary angle symmetry and $\cos v+\sin v\le\sqrt2$.

Both labels lie on the real rim with $f=0$. As $z_r,z_l\in(.245,.58)$, at the last phase $Z(z_l)=Z(z_r)$ and $Y(z_r)-Y(z_l)=z_l-z_r>.312$. For any phase their midpoint separation after (2), before any rigid pose, is exactly
$$
          d_\theta=\sqrt{d^2+[Y(z_r)-Y(z_l)]^2}.
$$
It increases at the endpoint by at least
$$
 \sqrt{.519^2+.312^2}-.519>.086.                                       \tag{7}
$$
A rigid rotation in the old $x$, outward-$y$ plane uses $\cos\delta=d/d_\theta$, $\sin\delta=[Y(z_r)-Y(z_l)]/d_\theta$. Subtract $Y(z_l)$ and use $.30$ as the abscissa origin first. After this rotation the two midpoint vectors differ by $(d_\theta,0,0)$ in the common raw frame. Thus (7) increases the *horizontal projection* which was previously bounded by one rigid-cap distance. Substituting the new value in (1) of R774 lowers its left-minus-right excess by exactly $d_\theta-d$. Passing this test or a selected pair of paths does not settle every other end path. The program gives both the old and new excess and the actual separate upper/lower endpoint height costs.

Both branches retain the true R774 periodic center, including all original material on its stationary grip. Write $J_\theta$ for its common raw left translation. After the above cap rotation, translate by $(X_\theta,b_\theta)$ in $x$ and the outward direction, in addition to $J_\theta$ in the section plane and the true central height $B$. The point $Q_+$ now has horizontal coordinate $X_\theta$ in the left-body frame and outward distance $b_\theta$ from the central seam. $Q_R$ then has coordinates $X_\theta+d_\theta,b_\theta$. The upper signed $z$ coordinates relative to the translated midline are $Z(z_l),Z(z_r)$, the lower ones their negatives.

On the first branch set $b=(1-S(\theta/.35))b_0+.105 S(\theta/.35)$. Write $X_{R,\theta},z_{R,\theta}$ for the true raw current right central label relative to the same left body. Define the two horizontal allowances
$$
 h_l=\sqrt{1.30^2+T^2-b^2-(.71-Z(z_l))^2},\qquad
 h_r=\sqrt{T^2-b^2-(z_{R,\theta}-Z(z_r))^2}.
$$
They are real: $b\le b_0<.573$, and $z_{R,\theta},Z(z_r)\in[0,.265]$ from the wall's original negative remaining material and $|\cos\beta|\le1$. The two limits on $X_\theta$ are $-1+h_l$ and $X_{R,\theta}-h_r-d_\theta$. Use their average for the proposed new abscissa. Transition from $.30,b_0$ to the proposed pair by $S(\theta/.20)$. This defines a center for the two path tests even when their allowed interval is empty. The report gives the two true sign costs.

On the second branch sample the full periodic center at the fixed equally spaced 512 true material labels, every real upper clock station and their lower reflections. For each known trial pose write the meridian's squared chord as $|(X,b)+r_j|^2+z_j^2$. Choose the translation minimizing
$$
 (1/48)\log\Big(\sum_j\exp(48(|(X,b)+r_j|^2+z_j^2))/n\Big).
$$
Its Hessian is $2I+192\operatorname{Cov}_w(r_j)$, so it is coercive and strictly convex with a unique smooth minimum. Use the actual Newton gradient residual and keep it in the report. Smoothly floor its axial coordinate at $.10$ by $.10+\log(1+\exp(60(b-.10)))/60$ and transition by the same $S(\theta/.20)$. This second pose distributes the true sampled angular costs. A discrete maximum here does not enclose all angles. Both branches have $b_\theta\ge.10$ at every phase. Their rotations are one proper Euclidean motion of each entire folded cap, in addition to the outside prescribed motion about the stationary grip.

## 3. Absolute curvature and all directed cap-to-cap normal balls

These claims concern the explicit caps, before independent whole-surface correction. During the initial crown attenuation they are graphs of $a f$ over the whole plane after extension by zero, followed by a common rigid motion. Taylor's formula gives the directed tangent-ball curvature
$$
    \frac{2|(F(v)-F(u))\cdot n(u)|}{|F(v)-F(u)|^2}
      \le\|\nabla^2 f\|_\infty<1.89
$$
for any two points of the same cap, however far apart in its nonconvex material domain. In the bending phase the reference unperturbed infinite surface is
$$
      C(x,z)=(x,Y(z),Z(z)).
$$
Its normal is $(0,N_z)$. Its full reach is at least $1/6.84$. First shrink $\beta$ by a fixed factor less than one. At each signed normal height $h$ with $|h|<1/6.84$, the $Z$ coordinate of the parallel curve has derivative $(1-h\beta')\cos\beta>0$. Its straight tails go to both infinities; it is globally a graph over $Z$. Holding $Z$ fixed and differentiating the other coordinate with respect to $h$ gives $1/\cos\beta>0$. All these graphs are disjoint and embedded. Any nearest point on this complete proper cylinder at distance less than $1/6.84$ lies on its unique normal segment; two nearest points are therefore impossible. Equivalently its ordered tangent-ball inequality holds with curvature $6.84$. Let the angular shrink tend to one. Each fixed pair of positions and their normals converges, so the same ordered inequality holds even on the true horizontal plateaus at the last phase.

The new cap is a normal graph of $h(x,z)=2^{-12}f(x,z)$ over that cylinder. Write $H=\|h\|_\infty<7.33\,10^{-9}$ and $G=\|\nabla h\|_\infty<1.84\,10^{-7}$. The coordinate derivatives are $e_x+h_xN_z$ and $(1-\beta'h)T_z+h_zN_z$. For each unit material vector the squared tangent length is at least $(1-6.84H)^2$, and the new unit normal differs from the cylindrical one by at most $G/(1-6.84H)$. The affine-coordinate Hessian of the new field has operator norm at most
$$
 6.84(1+6.84H)+856H+2(6.84)G+1.89\,2^{-12}<6.85,                       \tag{8}
$$
by differentiating the two tangent formulas. In particular both principal curvature magnitudes of each whole cap are below $6.85/(1-6.84H)^2<6.851$.

For any two cap labels let $d$ denote the length of their base-cylinder chord. If $d\ge.004$, the true chord is at least $d-2H$. Its normal component at the first endpoint is at most $6.84d^2/2+dG/(1-6.84H)+2H$. The ordered curvature ratio is bounded by
$$
 \frac{6.84+2G/[.004(1-6.84H)]+4H/.004^2}{(1-2H/.004)^2}<6.85 .
$$
For $d<.004$ and two $z$ of the same sign, the whole turning tangent has just one sign for each of its $Y$ and $Z$ components. Thus the planar chord is at least $|\Delta z|/\sqrt2$. At opposite signs, $Z$ is odd and nondecreasing. If either $|z|\ge.01$, the $Z$ difference is at least $.01\cos(6.84\cdot.01)>.004$. Otherwise $\cos\beta\ge\cos(.0684)$ between them and the same bound $|\Delta z|\le\sqrt2$ times the planar chord holds. Consequently the full Euclidean difference of the two material labels in $(x,z)$ is at most $\sqrt2 d<.00566$. Apply Taylor along their straight segment in the extended plane. By (8) and the lower tangent bound, the actual chord is at least $(1-6.84H-6.85(.00566)/2)|\Delta(x,z)|>.98|\Delta(x,z)|$. Its normal component is at most $6.85|\Delta(x,z)|^2/2$. The directed curvature is less than $6.85/.98^2<7.14$. This handles every close pair, including pairs on opposite sides of an old cap chart boundary. These estimates also imply embeddedness of each individual cap. Equivalently (2) on its tiny normal graph lies in the original cylinder's injective tube; on plateaus the regular graph in its true material coordinates follows by the same close/far estimates.

The two opposite caps have a uniform separation bound in the physical axial direction. The true maximum planar $x$ of the old closed disk is a boundary maximum. The upper/right track bounds of section 2, including $d_b$ in the unfavourable direction, give $x_{\max}\le .30+.26/\sqrt2+.301+.1651+.1325<1.084$. $Y$ is even and nonincreasing in $|z|$, constant above $.825$. Therefore $Y(z)-Y(z_l)\ge-(.825-z_l)>-.248$. In the transformed outward coordinate the worst possible loss is at most $\sqrt{.784^2+.248^2}<.823$ plus $H$ in the bending phase. During the initial height change $\delta=0$ and $|\eta|<.000030$. Both signed disks lie at $|y|>.88+.10-.823-.000030>.156$ with the correct sign. Their distance is greater than $.312>2(.132)$. For any pair of opposite-cap points, the absolute normal projection is bounded by their full chord, so this separation pays the two directed tangent-ball inequalities of radius $.132$. Together with the same-cap inequalities, this proves the radius-$.132$ directed balls for every ordered pair whose endpoints belong to the two complete caps. The argument is preserved by the final shared spatial rotation about the $y$ axis.

On a narrower final original roll strip of width $h_1=.000075$ both absolute principal curvatures of the new physical image are below $7.1$. Here the original meridional curvature is at most $S(.000075/.0005)/.132<.203$. The angular principal curvature satisfies
$$
 |K_s|\le 7(h_1/.132)/(1-7(.1325))<.055 ,
$$
using the true original section $|\kappa_0|<7$. For an original unit tangent in the collar the axial ($\eta$) component has magnitude at most $h_1/.132$ because the angular tangent has zero axial component. In (2) the second derivative on any such tangent is bounded by $6.84(1+6.84|\eta|)+856|\eta|+2(6.84)h_1/.132$. Take a unit-speed original geodesic through the point; its ambient acceleration is bounded by $.203$, and the derivative norm of (2) is at most $1+6.84|\eta|$. Dividing by the lower squared speed $(1-6.84|\eta|)^2$ gives the claimed bound. This is a local curvature estimate on a narrower actual material collar, separate from the complete wider two-tensor estimate (6). It does not by itself establish every same-side cap/roll ball.

## 4. Complete signed joins and the remaining common-metric correction

All eleven true material charts have a continuous-in-phase two-jet. On the central cylinder use exactly R774's closed section, the old axial coordinate and the genuine stationary markers. On a complete signed pre/standard end use accumulated $u\in[0,T]$, including the old interface $u=E$. Write $(p(u),d(u))$ for the full original signed pre-roll displacement followed by the standard-roll displacement, with the old $d(E)=0$. The incoming continuation is
$$
      F_l=(q_\theta-dN_\theta,\ B+p),
$$
where $q_\theta,N_\theta$ are the actual new section and its normal. The outgoing continuation is the above posed (2) applied to the true original pre/standard end, with the signed outward coordinate and $\eta=y_{\rm old}-y_b$. On the entire interval set
$$
 F=(1-w)F_l+wF_r,\qquad w=S_7((u-.012)/(T-.00013-.012)).
$$
This leaves genuine open collars at both ends and uses the same full smooth formula on either side of $E$. All first/second jets agree on both signed ends at the center, pre/standard seam, terminal seam and both cap overlaps. At zero phase both continuations equal the actual old field, and $a=1$, so the entire physical field at time zero is the original surface, with its whole normal radius at least $.132$, $D_0<4.386$ and stationary grip of diameter at least $1.40$. The later central section has the rigid grip from R774. Bounds (5),(6) and the cap pair balls hold throughout the uncorrected guide. This broad physical interpolation may have substantial middle-roll shear, principal curvature or global overlap. Its complete relative Gram operator, held witness, area, all ordered cross-region charges sampled below, and both outward caps use the true old geometry. A later whole held distance or whole reach is not a consequence of the sectional or cap estimates.

The fixed error in (4) matters for the separate refinement condition in the topic README. There is also an exact obstruction to keeping the first Cartesian coordinate immobile while asking the other two coordinates to clear this error. On any open set with $f_x\ne0$, suppose an exact embedding of $dx^2+dz^2+df^2$ has form $(x,P(x,z))$. Then the three Gram equations force $P_x=f_x n$ and $P_z=f_z n+t$ for an orthonormal pair $n,t$ in the plane. On a connected orientable patch choose $\partial_i n=\omega_i t$, $\partial_i t=-\omega_i n$. Equality of mixed derivatives gives
$$
 f_x\omega_z t=f_z\omega_x t-\omega_x n .
$$
It follows that $\omega_x=\omega_z=0$. The physical plane frame is locally fixed there. A two-channel correction retaining an exactly prescribed Cartesian $x$ cannot realize a varying direction on such an open patch. The actual restoration therefore allows all three Cartesian channels, including moving $x$ on the cap and its shared rim.

There is a constructive linear solution of the three independent first-order strain equations on each open nonzero-curvature substrip of the ideal bent cap. Use $C(x,z)=(x,Y,Z)$, the constant ruling $e_x$, the tangent $T_z$ and its normal $N_z$. For a displacement $V=u e_x+v T_z+w N_z$,
$$
 \tfrac12DG_C[V]_{xx}=u_x,\quad
 \tfrac12DG_C[V]_{xz}=(u_z+v_x)/2,\quad
 \tfrac12DG_C[V]_{zz}=v_z-\beta' w .
$$
For every smooth residual $S$ there and any smooth initial functions $u_0(z),v_0(z)$ use the actual scalar primitives
$$
 u=u_0+\int_{x_0}^{x}S_{xx}(\xi,z)d\xi,\qquad
 v=v_0+\int_{x_0}^{x}(2S_{xz}-u_z)(\xi,z)d\xi,\qquad
 w=(v_z-S_{zz})/\beta'.
$$
This gives one physical three-channel displacement rather than three independent per-cell metric variables, and exactly pays all three linearized components. Substituting a finite correction into the ideal field adds the known nonlinear tensor $(dV)^T dV$, which must be removed by the next correction. The primitive does not supply a uniformly bounded inverse where $\beta'=0$ or boundary values for a whole cap. The full source uses complete-integrable physical $C^2$ basis functions in all three channels across cells and releases the rim into the final roll; no tensor is replaced by one with the guide's small permanent defect.

## 5. Actual public experiment and scope of conclusions

The launch inventory fixes every original and new source word and both full signed caps. Four independent complete studies use the two poses above with either the original constructed caps retained or an independent three-channel restoration and a subsequent whole-geometry fit. The true original zero-phase reference and the whole phase interval are identical in all four and at every resolution.

The two restoring branches directly fit the old Gram matrix on both entire cap disks in their original regular center, annular and normal charts and on the true adjacent terminal rolls. They use physical Cartesian tensor products of compact cubic splines on the fixed rectangle $[-1.8,1.15]\times[-1.6,1.6]$, plus the true graph-height features $f,xf,zf,xzf$. The last four have zero two-jet at the outer boundary and extend by zero on the rolls. The other features use the actual projected material coordinates through the cap rim and fade through a true length $.12$ of the standard rolls; they can therefore change the common rim pose. All three physical coefficients for every feature are independent. Upper and lower material labels are independent through their true $z$ coordinate; the two opposite signed ends reflect a single fitted cap displacement. The refinement dimensions $(n_x,n_z)$ are $(6,8),(10,14),(16,22)$ with actual nonlinear evaluation budgets $18,28,42$ and LSMR iteration budgets $32,44,64$. In the original metric's orthonormal frame the independent residual entries are weighted by $10^6(1,\sqrt2,1)$; the exact public report is in unscaled relative metric units. It records all chart maxima before and after, the required true second-grid reread, and the six intermediate time interpolations at every level. Neither the amplitude $a=2^{-12}$ nor any part of $g_0$ is tightened in this test: any improvement must come from an actual additional physical displacement.

The two retained-cap whole fits keep every cap correction zero and keep an open terminal strip fixed. The two restored-cap whole fits also release all three ordinary whole-surface material correction components over the original permitted region outside the grip. Each runs three original complete whole-sphere levels, seven fitted phases and six independent intermediate phases. All eleven charts, their independent principal/Gram/support/area diagnostics, centered volume integrals and the original whole-sphere coefficient words are bound by the sources. The extra sampling inserts the physical inner bowl transition and true terminal strips on both sides. For each of the 13 uncorrected-guide phases per level and the final independently reconstructed fitted field, the source additionally enumerates both normal directions on every pair from each of ten distinct material-block comparisons between the central cylinder, the signed cap disks and the signed standard rolls. It returns the minimum Euclidean separation, worst finite directed radius and its two true material labels; these are finite grids, not a new proof for all cross-body pairs. The independent phase loops, source freeze and separately recorded rule-read commits, four real return codes, small per-stage reports and raw runner-only coefficients are part of the launch.

For the analytic uncorrected geometry, (5) pays the uniform $10^{-6}$ tolerance on the whole two caps and (6) on the two terminal collars. All ordered cap-to-cap normal balls, a narrower collar pointwise curvature bound, the actual increase in the key cap midpoint separation, both shared rim two-jets, and the unchanged true initial whole normal radius have separate proofs above. The whole later metric, complete displacement, all remaining normal-ball pairs and a decrement of the fixed-target error under successive refinements remain to be established on one common field. No numerical outcome is assumed here.
