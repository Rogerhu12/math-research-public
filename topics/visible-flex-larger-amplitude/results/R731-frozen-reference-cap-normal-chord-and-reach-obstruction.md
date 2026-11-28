# R731 — Exact short-axis cap obstruction for the frozen R730 reference

2026-11-28. **Proved.** At every phase the exact closed, marked R730 reference has reach strictly less than $2/125=0.016$. Its reference diameter exceeds $97/25=3.88$, hence its reach/diameter ratio is less than $2/485$. A specified activity point already violates the inward normal-ball inequality of the lower flat cap. The separation from the marker and the size of the necessary geometric correction are explicit. This statement concerns the reference before the outer rotation controls, free height, closure lift and normal stages act. It gives neither a measurement nor an upper bound for an unreturned or different optimized field.

## 1. Exact input and the relevant short meridian

Use the six Bernstein points (14), monotone height (16), angular root (37), pulse (43a,b) and complete marked surfaces (49) of [R730](R730-whole-image-safe-cone-and-unit-speed-contracted-reference.md), Git blob 41407fa22c569fad73a848ab603b885601066228, 40604 bytes. Use the actual dyadic chart of [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md), blob 4c5d039e1797be331b49be4d244ab625ae4c9e5c. Its symmetry gives at $\varphi=\pi/2$ the core point $Y e_y$ and $e(\Theta)=e_y$. From R717 (ideal short axis $26399/60060$ with error $\le7\,2^{-53}$) and R730 (25a,b,n,o,p), (43h) we have
$$
 .439<Y<.44,\quad 9/16<R<.57,\quad 1.94<H<1.95,\quad
 2.37<S<2.38,\quad \eta=1/32,\quad 0<\kappa_0<1/4 .
$$
Here and below decimals in inequalities are exact terminating rationals. $H$ is the declared reference height word. No accurate scalar-height integral is substituted.

Let $\gamma=(5/4)\kappa_0\eta^2$. Then $0<\gamma<5/16384<.001$. Write $b(t)$ for the scalar horizontal coordinate along $e_y$ on this meridian of the uncontracted quintic. Its ordered radial control coordinates and heights are respectively
$$
 (Y,Y,Y+\gamma,R+2\eta,R+\eta,R),\qquad(0,\eta,2\eta,H,H,H).
 \tag{1}
$$
The radial coordinates increase weakly to the fourth and then decrease. In particular
$$
 0<Y\le b(t)\le R+2\eta<.633,\qquad
 \int_0^1|b'(t)|\,dt\le R-Y+4\eta<.256 .
 \tag{2}
$$
The integral bound follows by differentiating the Bernstein polynomial, integrating its nonnegative derivative weights, and summing the absolute successive control differences. It does not require the polynomial to attain its largest control coordinate.

For this angle let $\xi$ be the unique exact R730 length root. The horizontal position is $r(t)e_y$, where
$$
 r(t)=(1-\xi\psi(t))b(t),\qquad
 \psi(t)=[1-(2t-1)^{12}]^7,\qquad 0<\xi<3/4.
 \tag{3}
$$
Write $L(u)$ for the length at trial amplitude $u$. The zero-amplitude length is bounded by the length of the full spatial control polygon. The first two chords have combined length $\eta+\sqrt{\eta^2+\gamma^2}\le 2\eta+\gamma$. The last two contribute $2\eta$. For the central chord,
$$
 0<R+2\eta-Y-\gamma<.194,\qquad
 0<H-2\eta<1.8875,\qquad
 .194^2+1.8875^2<1.9^2 .
$$
Thus $L(0)<1.9+4\eta+\gamma<2.03$. The pulse rises from zero to one and falls to zero, so its total variation is two. Consequently
$$
 \int_0^1|(\psi b)'|\,dt\le 2(.633)+.256<1.53,\qquad
 L(u)\le L(0)+u\int_0^1|(\psi b)'|\,dt\quad(0\le u\le3/4).
 \tag{4}
$$
The last estimate is the norm triangle inequality for the actual three-dimensional velocity. If $\xi\le1/5$, (4) would give $L(\xi)<2.03+1.53/5<2.37<S$, contradicting its definition. We have proved $\xi>1/5$ without solving a numerical root.

## 2. A complete cap-normal chord, at an explicit parameter

Fix $t_*=7/8$ in the Bernstein parameter, and set $h=H-z(t_*)$. The material radius $s=\ell(t_*,\varphi)$ exists by R730; this argument needs the point of the surface, not a sampled radial node. Since $(3/4)^{12}<4/125$, Bernoulli's inequality gives
$$
 \psi(t_*)=[1-(3/4)^{12}]^7>97/125 .
$$
By (2)–(4), the actual projected radius satisfies
$$
 .109<Y/4<r(t_*)<.633\left(1-\frac15\frac{97}{125}\right)<.535 .
 \tag{5}
$$
At $7/8$ the first three degree-five Bernstein weights are $1,35,490$ divided by $32768$. The last three controls have height $H$, so the height gap is exactly
$$
 h=\frac{H+35(H-\eta)+490(H-2\eta)}{32768},
 \qquad .028<h<\frac{(39/20)526}{32768}<.032 .
 \tag{6}
$$
For the strict lower bound, even the last positive term is $>490(1.94-1/16)/32768>.028$.

Use the **lower reflected activity point** $q$ at this same parameter. Its height is $-H+h$. Its vertical projection $p$ onto $z=-H$ has radius in (5). The lower fixed cap has a single p4 marker at radius zero with support radius $11/200=.055$, by [R716, §4](R716-asymmetric-fixed-caps-and-centred-volume-moment.md), blob 9290818d09ba3893599d950ea9d43944e3d87bfc. As $.055<.109<r(t_*)<.535<9/16<R$, $p$ is in the interior of the actual flat unmarked part of the marked lower cap. Consequently $q-p=h e_z$ and $T_pS$ is the horizontal plane. The activity rotates with phase while this entire flat *annulus* remains fixed. Its lower-cap point and the paired activity point therefore exist at every phase, with identical height and radius. This argument does not assume any rotational symmetry of the upper markers or of the marked closed surface.

## 3. Consequence for reach and diameter

For a closed embedded $C^2$ surface $A$, every $p,q\in A$ and every $0<\tau<\operatorname{reach}(A)$ satisfy
$$
 2\tau\,\operatorname{dist}(q-p,T_pA)\ \le\ |q-p|^2 .
 \tag{7}
$$
Here $T_pA$ denotes the linear tangent plane. This is the necessity direction of H. Federer, *Curvature measures*, Transactions of the AMS **93** (1959), Theorem 4.18, p. 449. Equivalently both radius-$\tau$ balls tangent at $p$ avoid the surface in their interiors. In the present orientation the inward lower-cap center is $p+\tau e_z$ and avoidance gives $(h-\tau)^2\ge\tau^2$. It is unnecessary to assert that the midpoint of the chord has no closer third point. [Primary source](https://doi.org/10.1090/S0002-9947-1959-0110078-1)

If the reach is zero the conclusion holds immediately. Otherwise (7) applied to the chord of §2, and then taking the supremum over $\tau$, gives for each phase
$$
 \operatorname{reach}(S_{\rm ref,phase})\le h/2<.016.
 \tag{8}
$$
For the diameter $D$ of the complete reference phase-zero image, take the two cap points with identical horizontal coordinate of radius $3/10$, at heights $H$ and $-H$. Both are actual flat cap points, since all p4 supports lie within radius $1/5$ on the upper cap and $.055$ on the lower cap. Thus
$$
 D\ge2H>3.88,\qquad .03D>.1164,\qquad
 \frac{\operatorname{reach}(S_{\rm ref,phase})}{D}
       <\frac{.016}{3.88}=\frac{2}{485}.
 \tag{9}
$$
This proves the result for the complete closed surfaces. The same argument applies to the unmarked reference; the marked lower annulus was used to cover the actual p4 family directly.

## 4. What an outer correction must change, and the exact flat-cap inequality

Here is a transferable quantitative consequence. Suppose a changed closed embedded surface has the same lower-cap radius $R$ and the same central p4 support, possibly at a different height $-H'$. Suppose it contains a point $q'$ whose horizontal position differs from $q$ by at most $.025$ and whose signed height over the *new* flat-cap plane differs from $h$ by at most $.025$. These are independent assumptions on a specified point; no solver output is being asserted. The projected radius of $q'$ lies between $.109-.025>.055$ and $.535+.025<9/16<R$, while its signed height $h'$ satisfies $0<h'<.057$. Its projection is again a genuine interior flat-cap point. Equation (7) now gives reach $<.0285$. This is a geometric displacement condition relative to the new cap, unaffected by a common vertical translation.

More generally let $E$ be the closure of the footprint of the flat lower-cap region in its plane and take a point $(w,-H'+v)$ with $v>0$. The inward normal-ball tests at *all* its flat interior bases are jointly equivalent to
$$
 \operatorname{dist}(w,E)^2+v^2\ \ge\ 2\tau v .
 \tag{10}
$$
Indeed the individual inequalities are $|w-b|^2+v^2\ge2\tau v$ for every flat interior base $b$; continuity permits the closure. In this actual lower cap $E=\{.055\le |b|\le R\}$. If $|w|\ge.055$ and $0<v<2\tau$, (10) forces
$$
 |w|\ge R+\sqrt{v(2\tau-v)} .
 \tag{11}
$$
Conversely (11) pays every such lower-plane inward test for this point. The radius in (11) is paired with the point's actual gap $v$; a box whose horizontal and vertical extrema come from different candidates cannot be treated as a witness. Outward balls, marked parts, reverse bases on activity, activity/activity and other mixed pairs remain separate. A subsequent construction can impose (10) while assigning the necessary meridional length in a region farther from the cap.

The R730 seed makes a genuine strong-held construction with a genuine unit-speed radial coordinate. Its theorem explicitly leaves reach open. Equations (8)–(11) resolve that question *for this frozen reference* without modifying R730 or the fully parameterized run 34. An optimized outer field can move the specified point and change the cap-relative geometry. Its actual Gram, full reach, diameter and all phase/model/point identities must be obtained from its own field. The original problem allows other seeds and closed surfaces.

No scientific program, quadrature, mesh, length root or stage was executed for this result. The constants above come from the exact cited prescriptions and finite inequalities.
