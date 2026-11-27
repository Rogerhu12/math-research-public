# R717 — Fixed seven-mode Fejér chart and whole-image bounds

Date: 2026-11-27. Status: complete analytic input definition and conditional geometric bounds. This is a new prescribed chart, not an actual returned field or a complete solution certificate. No local numerical field, root, quadrature, mesh, or interval experiment was performed for this note.

## 1. Purpose and exact scope

The next target needs a reproducible noncircular material chart that is specified before a numerical warm is computed. It must not be defined by copying the 160 coefficients of an earlier numerical output into repository parameters. A circle is easy to prescribe, but its initial core contributes no quarter-turn image displacement. A single large cosine can give displacement only by making its minimum radius of curvature small. The positive Fejér construction below gives substantial initial core anisotropy while retaining a definite curvature-radius lower bound.

The definition has two explicit layers:

1. Seven rational design coefficients admit short exact formulas and useful analytic comparisons.
2. The actual mathematical chart uses the uniquely specified nearest-even binary64 values of those formulas, interpreted thereafter as exact dyadic rational coefficients.

The second layer is the target used by the complete field, its fixed first three core coefficients, its model identity, and accurate geometry. The design curve is not silently substituted for it. The small comparison error between these two exact curves is included below.

The construction does not prove that the initial supported meridian exists, that its first numerical root calculation succeeds, that the selected normal branch is globally compatible, or that any solved field meets the metric, reach, holding-displacement, or noncongruence requirements. Those remain the original complete same-field obligations.

This note does not claim that this new material metric equals or differs geometrically from any earlier metric under a change of coordinates. It prescribes the new material-coordinate target explicitly and imports no old field certificate.

## 2. Seven rational design coefficients

Put \(B=1/4\), \(n=7\), and define the period-\(2\pi\) Fejér polynomial
\[
 K_7(t)=\frac18\left|\sum_{j=0}^{7}e^{ijt}\right|^2
       =1+2\sum_{m=1}^{7}\left(1-\frac m8\right)\cos(mt).
 \tag{1}
\]
The finite-sum formula is valid also where a quotient involving \(\sin(t/2)\) would be \(0/0\). It directly gives
\[
 0\le K_7(t)\le8,\qquad
 \frac1{2\pi}\int_0^{2\pi}K_7(t)\,dt=1.
 \tag{2}
\]

For \(m=1,\ldots,160\), prescribe the rational design values
\[
 c_m^*=
 \begin{cases}
 \displaystyle
 \frac{3(8-m)(-1)^{m+1}}{16(4m^2-1)},&1\le m\le7,\\
 0,&8\le m\le160 .
 \end{cases}
 \tag{3}
\]
The seven nonzero values, in the original mode order, are
\[
 \left(
 \frac7{16},-\frac3{40},\frac3{112},-\frac1{84},
 \frac1{176},-\frac3{1144},\frac1{1040}
 \right).
 \tag{4}
\]
They multiply \(\cos(2m\varphi)\). No mode is relabeled as a sine mode, a radial graph coefficient, or one of the three SO3 rotation channels.

Define
\[
 p^*(\varphi)=1+\sum_{m=1}^{7}c_m^*\cos(2m\varphi),\qquad
 \rho^*=p^*+(p^*)''.
 \tag{5}
\]
Substituting (3) into (5) gives the exact identity
\[
 \rho^*(\varphi)=\frac14+\frac34K_7(2\varphi-\pi),
 \qquad \frac14\le\rho^*\le\frac{25}{4}.
 \tag{6}
\]
In particular the alternating coefficients in (4) must be retained together. The sufficient estimate \(1-\sum_m(4m^2-1)|c_m|>0\) is not necessary and cannot be used to reject this explicitly positive polynomial.

## 3. The actual dyadic target and its strict margins

Let \({\rm RN}_{64}\) mean rounding an exact rational number to the nearest finite IEEE binary64 value, breaking a tie by choosing the even significand. It is a prescribed mathematical map, not a read of any earlier result. Define
\[
 \bar c_m={\rm RN}_{64}(c_m^*)\quad(1\le m\le7),
 \qquad \bar c_m=+0\quad(8\le m\le160).
 \tag{7}
\]
The initial array has exactly 160 entries in this order. An implementation can produce the seven nonzero words using integer numerator/denominator arithmetic and an explicit nearest-even conversion. The source formula and the conversion policy are the reusable parameters; generated words and their identities are actual producer outputs.

All values in (4) are small, normal binary64 numbers. The deliberately loose uniform bound
\[
 |\bar c_m-c_m^*|\le\epsilon,\qquad \epsilon=2^{-53},
 \tag{8}
\]
is enough here. It is not an assertion that every coefficient actually incurs this error. The true coefficient differences can also be recorded exactly by the producer.

Define \(\bar p,\bar\rho\) by (5) with \(\bar c\). Since
\[
 \sum_{m=1}^{7}(4m^2-1)=553,
\]
(6)–(8) imply
\[
 \frac14-553\epsilon\le\bar\rho(\varphi)
 \le\frac{25}{4}+553\epsilon,\qquad
 553\epsilon<2^{-43}.
 \tag{9}
\]
In particular the lower endpoint is strictly positive. Also
\[
 \|\bar p-p^*\|_\infty\le7\epsilon.
 \tag{10}
\]
These are whole-angle inequalities for the accurate dyadic chart, not sampled domain checks.

The fixed metric in the existing material coordinates is declared to be
\[
 g=ds^2+a_{\rm deep}(s)^2\,d\bar\Theta_0^2,
 \qquad
 \bar\Theta_0(\varphi)=
 \varphi+\sum_{m=1}^{7}
 \frac{1-4m^2}{2m}\bar c_m\sin(2m\varphi).
 \tag{11}
\]
Here the complete scalar law and the exact radial domain must be separately prescribed by their complete source-bound recipe. This note does not select an old scalar output or a time-dependent stopping outcome as a new parameter.

The actual field and accurate consumers must use \(\bar c\) in (11). Ordinary evaluation errors in trigonometry, quadrature, roots, or returned field words are not paid by (8); they remain in the existing error accounting. Conversely there is no unrecorded ideal-to-dyadic field discrepancy when the declared target is (11).

## 4. Strictly increasing chart, closure, and orientation

By construction,
\[
 \bar\Theta_0'=\bar\rho>0,\quad
 \bar\Theta_0(\varphi+2\pi)=\bar\Theta_0(\varphi)+2\pi .
 \tag{12}
\]
Thus this lift defines a \(C^\infty\) orientation-preserving circle diffeomorphism. Its inverse is unique modulo the declared period. The lower bound in (9) is an analytic inverse-chart denominator bound for the fixed reference chart.

Let
\[
 e_r(\varphi)=(\cos\varphi,\sin\varphi,0),\qquad
 e_\theta(\varphi)=(-\sin\varphi,\cos\varphi,0),
\]
and prescribe the core
\[
 \bar\Gamma(\varphi)=
 \bar p(\varphi)e_r(\varphi)+\bar p'(\varphi)e_\theta(\varphi).
 \tag{13}
\]
This is the support-function representation. It is not the radial graph \(\bar p e_r\). Direct differentiation gives
\[
 \bar\Gamma'=\bar\rho e_\theta,\qquad
 \bar\Gamma''=\bar\rho' e_\theta-\bar\rho e_r .
 \tag{14}
\]
The finite trigonometric expression is exactly closed and regular. Its tangent angle increases once around the circle; equivalently the positive-support construction in section 5 identifies it as the boundary of a strictly convex body. The parameter \(\varphi\) is its outward-normal angle. Its arclength coordinate from \(\varphi=0\) is exactly \(\bar\Theta_0(\varphi)\), because both have derivative \(\bar\rho\) and initial value zero. Its perimeter is \(2\pi\).

The chart and core have the exact symmetries
\[
 \bar\Theta_0(-\varphi)=-\bar\Theta_0(\varphi),\quad
 \bar\Theta_0(\varphi+\pi)=\bar\Theta_0(\varphi)+\pi,\quad
 \bar\Theta_0(\pi-\varphi)=\pi-\bar\Theta_0(\varphi),
 \tag{15}
\]
and the corresponding two planar reflections and central half-turn for \(\bar\Gamma\). Dyadic rounding does not break these identities: it changes coefficients, not the parity or frequencies.

These fixed-chart identities do not prove covariance of a later numerically selected normal root. That selected full-field branch still needs its own complete 32-stage, all-angle association and seam proof.

## 5. Convex support and whole-core size

For completeness, the design support has a useful positive representation. The elementary Fourier series
\[
 \frac{\pi}{2}|\cos\varphi|
 =1+2\sum_{m=1}^{\infty}
     \frac{(-1)^{m+1}}{4m^2-1}\cos(2m\varphi)
 \tag{16}
\]
can be obtained by integrating each cosine coefficient over one period. Taking its Fejér mean in the variable \(2\varphi\) gives precisely the nonconstant part in (3)–(5). Consequently \(p^*\) is the support function of a disk of radius \(1/4\) plus a positive rotational average of horizontal line segments. In particular
\[
 \frac14\le p^*(\varphi)\le C_*,
 \qquad C_*=\frac14+\frac{3\pi}{8}<\frac{10}{7}.
 \tag{17}
\]
The last strict bound follows from \(\pi<22/7\). One may alternatively keep \(C_*\) symbolic.

Equations (9) and (10) make \(\bar p\) a strictly convex support function with
\[
 \bar p\ge\frac14-7\epsilon>0,\qquad
 \bar p\le C_*+7\epsilon.
 \tag{18}
\]
Thus the entire dyadic core is contained in the disk of radius \(C_*+7\epsilon\), and its convex interior contains the disk of radius \(1/4-7\epsilon\). The outer-radius conclusion uses the support inequalities for every direction; it does not replace \(|\Gamma|\) by the single value \(p(\varphi)\).

The axis intercepts of the design curve are exactly
\[
 X_*=p^*(0)=\frac{82967}{60060},\qquad
 Y_*=p^*(\pi/2)=\frac{26399}{60060},
 \tag{19}
\]
so
\[
 \Delta_*=X_*-Y_*=\frac{4714}{5005}>\frac{47}{50}.
 \tag{20}
\]
For the dyadic core,
\[
 |\bar X-X_*|\le7\epsilon,\quad
 |\bar Y-Y_*|\le7\epsilon,\quad
 |(\bar X-\bar Y)-\Delta_*|\le8\epsilon.
 \tag{21}
\]
The sharper last constant uses only the four odd-indexed modes.

The complete core lies in \([-\bar X,\bar X]\times[-\bar Y,\bar Y]\). Indeed, from (14), its \(x\) coordinate decreases on \((0,\pi)\), and its \(y\) coordinate increases on \((-\pi/2,\pi/2)\). This proves the axis-extremum statement without assuming that the farthest Euclidean point is on an axis.

## 6. Core curvature and the original free variables

The planar curvature of the initial dyadic core is
\[
 \kappa_{\rm core}(\varphi)=\frac1{\bar\rho(\varphi)}
 \le\frac1{1/4-553\epsilon}.
 \tag{22}
\]
For the ideal design, the maximum is exactly 4, attained where \(K_7=0\). The dyadic bound is (22), not an unqualified assertion that it is at most 4.

This has direct relevance to the closed-surface ports. At the core, the original physical formulas give
\[
 F_s=e_z,\quad F_\varphi=\rho_0 e_\theta(\varphi_c),\quad
 F_{\varphi\varphi}=\rho_0'e_\theta-
                   \frac{\rho_0^2}{\rho_c}e_r .
\]
The unit outward candidate normal is \(e_r\), and angular normal curvature is \(-1/\rho_c\). Hence any reach lower bound \(\tau\) for the complete \(C^2\) embedded surface necessarily satisfies \(\rho_c\ge\tau\). This explains why pushing a single cosine to its positivity limit is geometrically costly.

The new input retains the original \(M=160,K=3,J=923\) field layout. The first three core coefficients are the fixed dyadic versions of (4). The other 157 core coefficients remain free. Their initial values are (7), including the four nonzero entries \(m=4,\ldots,7\); they are not frozen. All 1,333,212 original SO3 rotation coefficients and the free height remain. The total free size is still 1,333,370. The three original angular rotation families and every allowed radial slot are unchanged.

Therefore (9), (18), (19), and (22) always describe the fixed reference chart and its initial core. After an outer step changes any of the 157 free core coefficients, the current physical core needs a fresh bound using all 160 current coefficients. No initial Fejér curvature or axis certificate is inherited by a changed current core.

## 7. What the core displacement does and does not prove

For the phase family already defined by the complete source,
\[
 U_t(s,\varphi)=R_{\alpha(t)}U(s,\zeta_t(\varphi)),
 \quad
 \alpha(t)=\frac{\pi t}{2},\quad
 \zeta_t=\bar\Theta_0^{-1}(\bar\Theta_0(\varphi)-\alpha(t)).
 \tag{23}
\]
The material reparametrization is a circle diffeomorphism. The activity image is therefore rotated by \(R_{\alpha(t)}\), while the complete marked caps remain fixed under the established cap formula. This statement is conditional on the original physical field and port hypotheses; the new chart alone supplies only the valid smooth reparametrization.

At \(t=1\), a core point is \(P=(0,\bar X,0)\). For the core alone, (21) gives
\[
 {\rm dist}(P,\bar\Gamma)\ge \bar X-\bar Y
 \ge\Delta_*-8\epsilon.
 \tag{24}
\]
This is not yet a lower bound for distance to the whole initial surface. The target includes every upper patch, every reflected lower patch, both full cap disks, and all fixed marks.

Two complete routes remain available:

* If the whole target has \(y\le Y_{\rm all}\), then
  \({\rm dist}(P,S_0)\ge\max(0,\bar X-Y_{\rm all})\).
  Here \(Y_{\rm all}\) includes at least the cap radius, and cannot be replaced by \(\bar Y\).
* For a complete covering \(S_0\subset\bigcup_j B_j\),
  \({\rm dist}(P,S_0)\ge\min_j{\rm dist}(P,B_j)\).
  The existing whole-image consumer takes this minimum over all upper, lower, and marked-cap boxes, and then maximizes over four genuine phase-one core witnesses.

The second route keeps vertical separation. It can be much stronger than first collapsing all caps into a horizontal hull. For example, when \(H>0\), a full top or bottom cap has distance at least
\[
 \sqrt{H^2+\max(0,\bar X-R)^2}
\]
from \(P\); fixed outward marks do not reduce the vertical component. This is a symbolic bound, not a statement about an unreturned field.

A useful sufficient shape condition, if actually verified on the whole target, is
\[
 |y|\le \bar Y+\frac{z^2}{2\Delta},\qquad
 \Delta=\bar X-\bar Y>0.
 \tag{25}
\]
It implies \({\rm dist}(P,S_0)\ge\Delta\). If \(z^2\le2\Delta^2\), use
\((\bar X-y)^2+z^2\ge(\Delta-z^2/(2\Delta))^2+z^2\ge\Delta^2\);
if \(z^2>2\Delta^2\), the vertical distance alone suffices. Condition (25) is a possible geometric design guide, not an added admission test or an assumed property.

The holding displacement in the original problem uses image Hausdorff distance without rigid alignment. It must not be replaced by displacement of the same material point. The Euclidean-congruence invariant remains a separate R716 responsibility.

## 8. Height, full diameter, and why a single cosine was rejected as the default

The top and bottom flat cap rims contain diametrically opposite points. Thus every complete candidate with cap radius \(R\) and height \(H\) has
\[
 D\ge2\sqrt{R^2+H^2}\ge2|H|.
 \tag{26}
\]
Marks can increase the diameter; they do not invalidate this lower bound.

For the considered single-cosine alternative \(c_1=27/100,c_{m>1}=0\), the core-only axis difference is \(27/50\). A proof using only that difference for \(\delta_{\rm hold}\ge D/5\) would require
\[
 |H|\le\frac{27}{20},\qquad
 H^2+R^2\le(27/20)^2.
 \tag{27}
\]
Thus its attractive core-only ratio does not justify the full-surface target when the independently produced height is larger. This rejects that particular core-witness route as the default; it does not prove that a field with this chart could never acquire a better interior image witness.

The Fejér difference in (20) provides substantially more room. It still gives no unconditional full-image lower bound and no unconditional diameter upper bound. The actual current height, actual current core, and all interior patches must be read. The initial height can retain the declared complete scalar-integral rule. No old numerical height word is inserted into the new parameters, and the outer height remains free.

The fixed grip of radius \(9/20\) used in the existing assembly has image-diameter lower bound \(9/10\). Its original \(D/5\) size requirement is therefore certified by \(D\le9/2\), together with its existing radius and closed-cap assumptions. This is a useful scale to seek, not a new restriction on the solver.

## 9. A tighter complete diameter bound from the same physical leaves

The current continuous-geometry implementation bounds the closed family using separate global maxima of horizontal radius and absolute height. This is valid, but it combines extrema that may occur at different radial locations.

The same complete position boxes already support a tighter bound. For each upper physical leaf with box
\[
 B_j=[x_j^-,x_j^+]\times[y_j^-,y_j^+]\times[z_j^-,z_j^+],
\]
let \(r_j\) be an outward upper bound for
\[
 \sqrt{\max(|x_j^-|,|x_j^+|)^2+
       \max(|y_j^-|,|y_j^+|)^2+
       \max(|z_j^-|,|z_j^+|)^2}.
\]
Then put
\[
 R_{\rm all}=\max\left\{\sup_jr_j,\
       \sqrt{R_+^2+(|H|+1/1000)^2}\right\},\qquad
 D_+=2R_{\rm all}.
 \tag{28}
\]
Every upper point, its lower reflection, and every rotated activity point have the same Euclidean norm. The second term covers both complete fixed cap disks and their original p4 graphs. Hence the entire family lies in the ball of radius \(R_{\rm all}\), and the triangle inequality proves \(D\le D_+\) for every physical phase. This covers mixed activity-cap pairs as well.

Equation (28) uses no new field evaluation, root, observation angle, or quadrature. It consumes every original position leaf and the complete cap parameters. It is not yet implemented by this note, and no numerical gain is asserted. An implementation must preserve partial/null semantics and bind the same complete field and cover. Pairwise box diameter estimates could tighten it further, but are not needed for the validity of (28).

The all-phase conclusion still requires the source-specific physical phase and closed-surface interpretation. Applying (28) to unverified upper boxes gives a bound on the formal constructed image, not a certificate of an embedded closed family.

## 10. Existing supported-seed obligations under the new chart

The complete 0d09 provider uses the two relative support intervals
\[
 [1/32,15/32]\ \cup\ [17/32,31/32].
\]
Their total physical length is \(L=7S/8\). With its retained default boundary total \(b=S/16\), the two central intervals have total length \(L_c=13S/16\), and each boundary layer has width \(b/4=S/64\).

Let \(B_{\rm out}\) and \(C_{\rm out}\) be the exact horizontal and vertical integrals of the unchanged original unit meridian on the full complement of the supports. The exact mean displacement is
\[
 K(\varphi)=(R-B_{\rm out})e_r(\bar\Theta_0(\varphi))
            -\bar\Gamma(\varphi)+(H-C_{\rm out})e_z.
 \tag{29}
\]
In particular the two axis vectors are
\[
 K(0)=(R-B_{\rm out}-\bar X,0,H-C_{\rm out}),\quad
 K(\pi/2)=(0,R-B_{\rm out}-\bar Y,H-C_{\rm out}).
 \tag{30}
\]
Any unit-speed replacement supported on these intervals necessarily has
\(|K(\varphi)|\le L\). The already proved R709 sufficient conditions can be instantiated, for example, with a bound \(k_+<L-2b=3S/4\), the corresponding positive vertical and nonzero-radius margins, and the original full mean equation. Neither condition is asserted to hold for the new input before its actual complete computation and accurate bounds.

The full original mean solver, scalar profile, positive quadrature, angular derivatives, 32-stage normal chain, and actual residual checks remain. Equations (29)–(30) explain a possible failure geometrically; they are not a new cheap fixture replacing that complete execution.

Transition curvature is a separate practical concern. In a boundary layer,
\[
 T_b=N(Y),\quad Y=(1-\chi)T_0+\chi d,\quad
 (T_b)_s=DN(Y)\big((1-\chi)(T_0)_s+\chi_s(d-T_0)\big).
 \tag{31}
\]
If \(|Y|\ge\nu>0\), then
\[
 |(T_b)_s|
 \le\frac{|(T_0)_s|+|\chi_s|\,|d-T_0|}{\nu}.
 \tag{32}
\]
For the retained quintic cutoff, \(\max|\chi_s|=15/(8\delta)\); at \(\delta=S/64\) this is \(120/S\). Thus a thin layer and a large tangent mismatch can dominate core curvature. The positive chart does not fix this. Wider explicitly declared layers or a different reference profile would be separate complete model choices; this note does not change the current algorithm parameters.

The R711/R712 smooth central profile comparison continues to apply only in its stated same-mean and accurate-seed scope. It is not a bound for a later nonzero outer rotation or for the whole principal-curvature matrix.

## 11. Reach, support, metric, and phase responsibilities that remain

At the initial core, the candidate outward normal is horizontal and
\[
 (\operatorname{diag}(1,1,\beta)\bar\Gamma)\cdot n=\bar p
 \ge1/4-7\epsilon.
\]
This is useful support margin. It covers only the core. The original R650 application needs one common positive definite matrix, all activity points and normals, both complete fixed caps, and the full curvature upper bound. It cannot select unrelated matrices for different pieces or omit mixed pairs.

The fixed p4 cap estimates and the original R650 and R716 deductions are reused with their actual hypotheses. They are not reproved or transferred from an old numerical surface. In particular:

- every exact radial piece and the entire angular circle must be covered;
- the selected full 32-stage branch and its periodic/seam association must be established;
- complete accurate sixjets must retain the reference-centred physical lift and all scalar/root/quadrature errors needed for their enclosures;
- relative Gram error must be measured against the actual metric (11);
- the complete current core, current height, and all free rotation variables must be read;
- principal curvature, common positive support, closed \(C^2\) immersion, and outwardness/embedding must be connected in the original noncircular order of implication;
- the lower reflection, full marked caps, all physical phases, and whole-image holding distance must be included;
- R716 noncongruence needs its own complete same-field moments or another valid invariant.

The initial core has a useful margin, but no full reach value or holding ratio is printed as paid. A failure of an actual first seed or later field would be evidence about that full candidate and source, not a proof that this prescribed target is impossible.

## 12. Source connection and implementation boundary

The chart formulas were checked against the full core and inverse-chart formulas in the existing complete SO3 family. Relevant complete sources are:

| Role | Complete source | SHA-256 |
|---|---|---|
| Original whole scalar/reference interface | scripts/resume_20261126/so3_axisymmetric_reference.py | 4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3 |
| Supported smooth-triangle reference | scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py | 0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b |
| Original fixed-reference base | scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py | 6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865 |
| Current complete closed-phase consumer | scripts/resume_20261126/run10_complete_closed_phase_grip_evidence.py | f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be |
| Current whole-leaf geometry consumer | scripts/resume_20261126/run10_continuous_gram_curvature_support.py | e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7 |

The new complete input and its derived solver family must have their own source/model identities. Old sources remain unchanged. The new target is not admitted by deleting an old chart guard or by replacing an old output hash. Its complete scalar recipe, exact radial nodes, seven-mode conversion policy, all 160 generated initial coefficients, actual input files, and actual source records are bound together when produced.

This note does not authorize reducing any variable, mode, observation, normal stage, permanent location, typed role, norm, threshold, budget, or error responsibility. It is not a new execution gate. Actual computation remains in the authorized public Actions workflow. Publication and source/queue changes are performed by the root owner.

The substantive new result is the explicit reproducible chart with rigorous whole-angle strict margins, plus the conditional whole-image and same-leaf diameter bounds above. Completion of the original geometric task still requires the actual complete source-bound field and its original global evidence.
