# R762 — Positive transverse arclength on the R760 sphere and physical fields with two free material coordinates

2026-11-28. We use the initial sphere, metric, marked material and time interval of [R760](R760-cartesian-cap-join-initial-global-reach-and-exact-active-ends.md). On the whole wide annulus of each genuine cap there is a positive, two-jet controlled change of coordinates that keeps two prescribed open collars pointwise fixed. Its enclosed image and true geometric curvatures agree with those of its input at each phase. We give a criterion for *all three* entries of the metric to agree under such a change. The construction supplies a separate complete fit with local three-dimensional displacement fields and an independent check of every relative Gram component. The initial thickness result belongs to R760. The later closed shapes, fixed-metric error and thickness after physical correction are part of the experiment.

## 1. Fixed metric and the freedom of a single cap coordinate

Use the physical R760 wires, two curved rolls, signed caps and regular Cartesian cores. In the cap polar chart let $s$ have the true material period $P$ and let $v$ increase towards the rim. Work on
$$
 v_-=.82(1-.0075),\qquad v_+=1-.007,\qquad \Delta=v_+-v_-,\qquad z=(v-v_-)/\Delta .
$$
The original entire regular Cartesian ellipse lies on its inner side. Positive and negative caps are treated separately. The phase is $0\le\theta\le.90$. Write $F_\theta$ for the actual R760 posed field before the new coordinate change. It uses the original 24-ray, $24^2$-pair proper rigid crown calculation and its finite rotation on the true bowl. The pose is identity at zero. The target everywhere is the Gram matrix $g_0=(DF_0)^T DF_0$ of the complete real zero-phase physical field, including the small graph terms of R760. We do not project $g_0$ into splines. The numerical orders 16, 24 and 32 evaluate one fixed analytic construction at increasing quadrature resolution.

Here is an exact test for what one transverse coordinate alone can achieve. At an immersed patch with $r=|F_v|>0$ introduce
$$
 \ell(s,v)=\int_{v_-}^{v}r(s,t)\,dt,\quad L(s)=\ell(s,v_+),\quad
 A=\frac{F_s\cdot F_v}{r}-\ell_s,\quad Q^2=|F_s|^2-\frac{(F_s\cdot F_v)^2}{r^2}.
$$
The partial $\ell_s$ is taken at fixed $v$. Regard $A,Q$ as functions of $(s,\ell)$ by inverting the strictly increasing $\ell$. Substituting $r\,dv=d\ell-\ell_s\,ds$ gives the exact metric
$$
                  Q^2\,ds^2+(d\ell+A\,ds)^2.                    \tag{1}
$$
Consequently an orientation-preserving radial map $(s,v)\mapsto(s,\Phi(s,v))$ that fixes each end and exactly matches the whole initial Gram matrix exists if and only if:

1. $L_\theta(s)=L_0(s)$ for every $s$.
2. $A_\theta(s,\ell)=A_0(s,\ell)$ throughout the common physical length intervals.
3. $Q_\theta^2(s,\ell)=Q_0^2(s,\ell)$ throughout those intervals.

Indeed the $vv$ entry forces $\ell_\theta(s,\Phi)=\ell_0(s,v)$ and hence uniquely determines $\Phi$. Formula (1) proves the remaining two statements by comparing the cross term first. Conversely they make (1) the same tensor after the unique pullback. Identity on particular open guards additionally requires $\ell_\theta(s,v)=\ell_0(s,v)$ there. With a free physical shape these three functions can change, whereas a mere reparametrization with fixed $s$ preserves their intrinsic arclength representation.

There is a quantitative necessary price. If the maximum relative metric operator error is at most $e$, then on each radial line the speed lies between $\sqrt{\max(0,1-e)}\,r_0$ and $\sqrt{1+e}\,r_0$. Both ends are fixed, so
$$
     e\ \ge\ \left|(L_\theta(s)/L_0(s))^2-1\right|.
$$
For *any* physical annulus retaining the same boundary points the new chord $d_\theta(s)$ also gives $e\ge\max(0,(d_\theta/L_0)^2-1)$. For the first inequality use the complete arclength of the original curve as input. A speed surrogate or a finite quadrature value alone does not certify the true continuous obstruction. The original labelled path prices remain in the physical experiment.

## 2. An explicit positive gauge with two exact guards

For each $(s,\theta)$ select positive $C^2$ model speeds $a_\theta,a_0$ in normalized coordinate $z$. They may be the true speeds $\Delta r$ if smooth enough. For the public run the models are separately defined from actual physical samples in §3. Take $\omega(z)=0$ through .04 and from .96, equal to one on $[.16,.84]$, and rising and falling by $S_5(t)=10t^3-15t^4+6t^5$ on the intervening intervals. Put
$$
 b(s)=\frac{\int_0^1\omega a_\theta\,dz}{\int_0^1\omega a_0\,dz},\qquad
 G=(1-\omega)a_\theta+\omega b\,a_0 .
$$
Both denominators and both effective speeds are strictly positive. In particular no monotone inverse requires a signed or clamped physical speed. The total integrals of $G$ and $a_\theta$ agree by the definition of $b$. For each $z$ there is a unique $x$ satisfying
$$
 \int_0^x a_\theta(s,t)\,dt=\int_0^z G(s,t)\,dt,\qquad \Phi=v_-+\Delta x.       \tag{2}
$$
This is a degree-one increasing diffeomorphism of the entire radial interval with $x_z=G(s,z)/a_\theta(s,x)>0$. It is identity on both open guards. The inner guard follows by integrating from zero and the outer guard by integrating from one using the equal totals. For $\theta=0$ both model speeds are identical, hence $b=1,\ G=a_0,\ \Phi=v$ at every label even if the model speed differs substantially from $|F^0_v|\Delta$. This proves equality to the actual initial metric, independently of the accuracy of the surrogate.

On the central plateau the true transformed transverse speed in normalized coordinates is
$$
   \Delta|F_{\theta,v}(s,\Phi)|\,
   \frac{b(s)a_0(s,z)}{a_\theta(s,x)} .                              \tag{3}
$$
The proxy speed ratio there is exactly $b(s)$. Formula (3) retains the discrepancy between both models and the true physical speeds. The mixed and tangential entries are taken from the full pulled-back two-jet. For example
$$
 g'_{sv}=\Phi_v(g_{sv}+\Phi_sg_{vv}),\qquad
 g'_{ss}=g_{ss}+2\Phi_sg_{sv}+\Phi_s^2g_{vv}.
$$
The argument of every $g$ on the right is $(s,\Phi)$. At each phase precomposition is a diffeomorphism of the entire cap fixing its two open guards. Extending by the identity onto the other charts preserves the image as a set, the stationary grip, embeddedness if present, all principal curvatures as a set, whole reach, diameter and image-to-image distances. It may change the identification of points on the wide annulus. A subsequent three-component displacement requires a new geometric verification.

For the complete six-jet write $a=a_\theta$, $I(s,x)=\int_0^x a$, $J(s,z)=\int_0^zG$. In derivatives on the right evaluate $I,a$ at $x$ and $J,G$ at $z$. All $s$ derivatives shown for these functions are partial at their stated argument. Direct implicit differentiation gives
$$
\begin{aligned}
 x_s&=(J_s-I_s)/a, & x_z&=G/a,\\
 x_{ss}&=(J_{ss}-I_{ss}-2a_sx_s-a_xx_s^2)/a,\\
 x_{sz}&=(G_s-a_sx_z-a_xx_sx_z)/a,&
 x_{zz}&=(G_z-a_xx_z^2)/a .
\end{aligned}
$$
In physical $v$ the derivative tuple of $\Phi$ is $(\Delta x_s,x_z,\Delta x_{ss},x_{sz},x_{zz}/\Delta)$. The second jets of $F_\theta(s,\Phi)$ use the ordinary full chain rule, including $F_v\Phi_{ij}$. No third derivative of the original cap is used by this evaluation.

## 3. Positive physical samples and independent angle/radial shape controls

The [gauge implementation](../scripts/resume_20261126/r762_positive_meridian_arclength_and_full_jets.py) samples $\Delta|F_{\theta,v}|$ from the actual unprojected original R760 posed jet at the Greville labels of a tensor cubic spline. The angular direction uses the true period, all true elbow clock anchors and their reflected mates. The open radial knots include the real cap transitions and the four cutoff edges. The basic refinements use 48/96/192 angular and 24/40/64 transverse intervals. Periodic coefficients at the two sides are the same original physical sample. Positive B-spline partition of unity makes the models strictly positive whenever the sampled speeds are positive. These quasi-interpolants converge uniformly to a continuous actual speed as the maximum knot span goes to zero, by bounding each value between actual samples from neighbouring supports. This construction gives the finite run an explicit model independent of any assertion of threshold attainment at a fixed grid.

Each radial speed is cubic per true spline cell. Its product with $\omega$ has degree at most eight there. The code integrates these polynomials by their own power coefficients, carries two angular derivatives of $b$ by the quotient rule, locates the appropriate cumulative cell and solves its strictly increasing primitive with bracketed Newton and up to 52 updates. The source returns literal identity coordinates and coordinate derivatives on the open guards and for every zero-phase label. The separate physical audit reports the numerical discrepancy in the six geometry channels as well as the coordinate discrepancy there.

The [physical solver](../scripts/resume_20261126/solve_r762_gauged_crown_tensor_annuli.py) takes the resulting *complete* fields at every original signed cap and keeps the five original charts, the real marked cylinder and its signed end/normal charts and Cartesian bowl. Add a vector field with three independent physical components supported away from the guards. For each of two material packets use a normalized transverse coordinate $u$ increasing from zero to one on its active range and a clamped envelope $e$. The main packet is contained strictly between the two cap guards. The second, a sleeve, ends at inward normal distance $.007-.0008$ from the rim. It is allowed to deform outer portions of the end. In the locked option its angular factor is $1-\chi$ on the right and it starts at the cylinder/roll seam. In the free option it starts .30 before that seam and includes the whole signed roll. In both cases the exact gauge guard at inward distance .007 and the guard beside the bowl see no added displacement. The Cartesian core keeps its original registered rigid pose, with zero additional displacement.

In addition to angular Fourier functions, radial cosine functions and the 15 Cartesian packets per active window, the new local expansion on each window is
$$
 e(s,u)\sum_{i=0}^{n_s-1}\sum_{j=-1}^{n_r+1}
      c_{ij}\,M_3(n_s s/P-i)\,M_3(n_r u-j), \qquad c_{ij}\in\mathbb R^3 .
$$
Use periodic distance in the first argument. Here $M_3(x)=(4-6x^2+3|x|^3)/6$ for $|x|\le1$, $(2-|x|)^3/6$ for $1\le |x|\le2$ and zero outside. Its two derivatives agree through every boundary. The boundary of the periodic distance chart is outside its support at all three resolutions. The levels $(n_s,n_r)=(6,3),(12,6),(24,12)$ allow independently varying angular and radial physical deformations. The last level has 720 scalar tensor columns across the two windows before assigning three physical components to each. The coarse space prolongs exactly by the cardinal cubic two-scale mask $(1,4,6,4,1)/8$ in both variables with angular wrap. Truncating newly refined radial centers beyond the stated range drops functions identically zero through two derivatives on the active interval. The global envelopes are kept fixed in physical material coordinates. Such local spline spaces can approximate compactly supported smooth vector fields inside the free windows with spatial derivatives up to order two under continued refinement. This is an approximation property of the *physical search space*. It gives no exact nonlinear isometric solution by itself.

## 4. Complete finite experiment

The [controller](../scripts/resume_20261126/run_r762_all_gauged_crown_fits.py) runs four independent, single-BLAS-thread physical fits on the same R760 target. Each signed side and each of the two outer choices gets all three spatial levels, seven original phases and six separate intermediate checks. The true global and local columns enter the physical shape residual through both principal-curvature matrix inequalities, support and the complete relative Gram tensor. To reduce storage the matrix of six-jet basis evaluations is built in bounded point batches and applied in sparse form, with its actual transpose used in the adjoint. The refinement budgets are respectively 12/20/30 nonlinear and 12/16/20 inner iterations. Independent angular grids have 64/96/144 nominal points before the original feature enrichment; the Cartesian pole is checked in its own regular chart. The crown path prices on all 16 independently labelled radial paths and the actual old/new tip graph Hessian comparisons are preserved.

There are two separate scientific outputs per sign. The gauge-only measurement covers all 13 phases at each of three resolutions, before any physical displacement, including the true componentwise prices before and after, actual radial Gram price, sampled extrema of $\Phi_v$, checks on both guards, primitive total gap and model length ratio. The physical fit independently reports per-chart relative spectral error and all three componentwise errors against the true initial orthonormal frame, minimum relative area, largest absolute principal curvature and minimum support for each completed fit and its independent samples. The two modes have independent coefficient words, report, identifier and reproducible source. Gauge-only data are recorded once per sign. The parent R760 experiment retains its own source, all original fields and budgets. No report in this statement supplies continuous global upper bounds for the final fitted residual, thickness or all-phase existence.
