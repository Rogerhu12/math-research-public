# R144 supplement: actual endpoint bounds imply the holonomy neighbourhood

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved, conditional only where explicitly stated.** The already required
componentwise moving $C^0$ correction bound $10^{-4}$ implies R144's
physical outer-neighbourhood and winding-branch conditions. This is a
direct whole-circle estimate; it needs no angular derivative of the
unknown correction. The cap side has a separate bound from its original
complete small input ball. That input condition is not inferred from
the body $C^0$ bound.

The original selected centre itself has a strictly nonzero waist mean
residual, even after its complete direction is included. All input
values below are read from existing complete records; no old producer,
scientific integral or endpoint evaluation is rerun.

## 1. The exact selected waist mean is not zero

The original waist-amplitude theorem and its
[complete rational record](../notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json)
give
$$
 m_c(0)+a_0=\alpha V_0,\qquad
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 V_0=\frac{1270129564654771}{158456325028528675187087900672}.
 \tag{HA.1}
$$
The [complete all-regular reconstruction](../notes/2026-11-14-R133-all-regular-head-complete-reconstruction.json),
Git blob 245b9f40400f9f68075d64952a98f8e8712dbf4a, contains the
original response trial with SHA256
ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6.
Its metadata specifies a physical unnormalized 193-state response,
the original fourth Robin row and the full even mean. The complete
initial-state entry with zero-based index 96 is the binary64 value
represented by the saved literal
$$
                         z_0=-4.552557419942977\,10^{-13}.
 \tag{HA.2}
$$
In (HA.2), the saved binary64 value is interpreted as its exact dyadic
rational, not as a newly rounded numerical evaluation.

The [already completed exact-waist audit](R133-supplement-actual-exact-selected-waist-data-and-original96-rows.md)
proved the complete base first-trace identity and reused the response
first-trace identity. It also checked that both exact continuous
repair offsets start at zero. Therefore for the actual explicit
selected family,
$$
             m_\delta(0)+a_0=\alpha V_0+\delta z_0
                         \qquad (|\delta|\le10^{-10}).
 \tag{HA.3}
$$
The response mean is not multiplied by $\alpha$.
It is also not the different outer mean displayed in R145.

Simple rational comparisons suffice to locate (HA.3): the fractions
in (HA.1) give
$3/4<\alpha<4/5$ and
$8\,10^{-15}<V_0<(17/2)\,10^{-15}$.
Thus $6\,10^{-15}<\alpha V_0<7\,10^{-15}$.
The exact saved dyadic in (HA.2) lies strictly between
$-5\,10^{-13}$ and $-4\,10^{-13}$, so
$|\delta z_0|<5\,10^{-23}$. Consequently
$$
 \boxed{\qquad
        5\,10^{-15}<m_\delta(0)+a_0<8\,10^{-15}
                   \quad\hbox{for every }|\delta|\le10^{-10}.
 \qquad}
 \tag{HA.4}
$$
In particular the implicit selected member has a nonzero waist mean
error. This statement is an exact finite comparison of saved values,
not a new finite BVP or a new response computation.

## 2. The body winding branch follows from the required correction ball

Let $(u,v)$ be an otherwise unspecified sufficiently regular candidate
or exact field in the same moving coordinate, with
$$
 \|u-u_\delta\|_{C^0([0,R]\times S^1)}\le\rho,\qquad
 \|v-v_\delta\|_{C^0([0,R]\times S^1)}\le\rho,\qquad
                         \rho\le10^{-4}.
 \tag{HA.5}
$$
A pair $C^0$ bound implying these component bounds is also sufficient.
This section does not assert that such an exact solution has been
constructed.

The [waist-amplitude theorem](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
gives $a_0>1.06873282$. Taking means in (HA.5) and using (HA.4),
$$
 |m(0)+a_0|<10^{-4}+8\,10^{-15}<101/10^6,\qquad |m(0)|>1.
$$
It follows that
$$
                  m(0)<0,\qquad
       |a_0/m(0)+1|<101/10^6<1/2.
 \tag{HA.6}
$$
This supplies R144's winding branch without treating a winding count
as numerical evidence.

The same old waist theorem gives $-v_c(0,\phi)>0.0833357128$.
The [complete continuous-direction bound](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md)
gives $\|Z_2(0)\|_\infty<19$ on the actual negative interval, including
the waist. Hence (HA.5) also gives
$$
 -v(0,\phi)>0.0833357128-19\,10^{-10}-10^{-4}>2/25.
 \tag{HA.7}
$$
The exact repaired background has the same waist value. Thus the
waist chart and the negative sign used in R144's convexity proof
remain valid on this conditional ball. The exact waist row $u(0)=0$
still has to be solved; (HA.7) does not set it to zero.

## 3. The moving outer correction gives the physical neighbourhood

All following old data are at the same physical $R=25/8$, fixed
$\eta_0$, and the complete family $|\delta|\le10^{-10}$:

* [R145, Section 4](R145-selected-nu-proposal-positive-source-and-outer-rows.md)
  gives $\|u_\delta(R)\|_\infty<2\,10^{-12}$.
* [OA.3](R141-supplement-actual-selected-physical-outer-residual-values.md)
  gives $|v_\delta(R,\phi)|>5.79999999999$ and the same-physical-angle
  change $\|C_\delta-C^{\rm raw}\|_\infty<4.973087\,10^{-19}$.
* The [original complete physical endpoint theorem, Section 4](R133-supplement-final-moving-centre-actual-regular-boundary.md)
  gives
  $\|(C^{\rm raw}-C_{\rm ref})_\perp\|_{A^0}<2.532986\,10^{-13}$
  and
  $|\langle C^{\rm raw}\rangle-C_{\rm ref}|<6.055\,10^{-43}$.

The compactly supported $\nu$ bump vanishes on the entire exterior,
so this $C_{\rm ref}$ is exactly the same rotational reference as in
R144. The triangle inequality gives
$$
                  \|C_\delta-C_{\rm ref}\|_\infty<3\,10^{-13}.
 \tag{HA.8}
$$
This retains the physical mean as well as all nonmean modes.

Under (HA.5), both $|v_\delta|$ and $|v|$ at $R$ are strictly larger
than $5$, and $v<0$. Consequently $m<0$ and $j=v/m>0$, so the real
material circle map exists. Direct pointwise estimates give
$$
 \begin{split}
 \|B(R)\|_\infty
   &\le\frac{\rho+2\,10^{-12}}5,\\
 \|C(R)-C_{\rm ref}\|_\infty
   &\le\frac{\rho}{25}+3\,10^{-13}.
 \end{split}
 \tag{HA.9}
$$
For the second line use
$|1/v-1/v_\delta|\le|v-v_\delta|/(|v v_\delta|)$.

There is no missing inverse-angle derivative in this argument:
$C_{\rm ref}$ is constant on the circle, so the supremum of
$1/v_\delta-C_{\rm ref}$ is identical in its moving and physical
angles. Supremum norms of a single function are unchanged by the true
circle diffeomorphism. No claim is made that two same-order
composition operators are close.

Combining both lines of (HA.9) with the sum bound for the Euclidean
pair gives the explicit result
$$
 \boxed{\quad
 \sup_\theta\sqrt{B(R,\theta)^2+
                         (C(R,\theta)-C_{\rm ref})^2}
     <2.4\,10^{-5}+7\,10^{-13}<1/40000<1/1000.
 \quad}
 \tag{HA.10}
$$
Only the component $C^0$ bound was used; derivatives of the unknown
correction are not needed.

## 4. The cap condition is a separate, already quantified input gate

Let a genuine cap belong to the original true exterior graph with
$$
 \|\mathcal Z\|_{A^0}\le10^{-12},\qquad
 \|f_B\|_{\dot A^2}\le2^{-60},\qquad
                  \mathcal Z=(C_{\rm cap}-C_{\rm ref})_\perp.
 \tag{HA.11}
$$
The complete small-ball estimates in
[the endpoint theorem, (F.18)--(F.19)](R133-supplement-final-moving-centre-actual-regular-boundary.md)
give
$$
 \|d(\mathcal Z,f_B)\|_{A^0}<1.638404\,10^{-18},\qquad
 |c_0(\mathcal Z,f_B)|<2.048004\,10^{-19}.
 \tag{HA.12}
$$
Its complete graph is
$$
 J_\theta B_{\rm cap}+Q_\theta\mathcal Z=d(\mathcal Z,f_B),\qquad
 C_{\rm cap}=C_{\rm ref}+\mathcal Z+c_0(\mathcal Z,f_B),\qquad
 \langle B_{\rm cap}\rangle=0.
$$
The Hilbert multiplier is an $A^0$ isometry on nonzero modes and
$\|Q_\theta\|_{A^0\to A^0}\le1$. Thus
$$
 \begin{split}
 \|B_{\rm cap}\|_\infty&<10^{-12}+1.638404\,10^{-18},\\
 \|C_{\rm cap}-C_{\rm ref}\|_\infty
                            &<10^{-12}+2.048004\,10^{-19}.
 \end{split}
$$
In particular its physical pair supremum is strictly below
$3\,10^{-12}$, far inside R144's $10^{-3}$ neighbourhood.

The existence of a genuine periodic cap with all required far labels,
position/frame closure and height matching remains its original
obligation. Equations (HA.11)--(HA.12) are a trace estimate for that
same graph. The body bound (HA.5) by itself does not prove
$\|\mathcal Z\|_{A^0}\le10^{-12}$, and no such conclusion is used.

## 5. The off-shell constant-mean segment also stays admissible

R144's off-shell identity requires the segment
$(B_{\rm cap},C_{\rm cap}+tc)$, $0\le t\le1$, where
$c=\langle C_{\rm body}-C_{\rm cap}\rangle$.
Even if the nonmean matching residuals are nonzero,
(HA.9)--(HA.12) directly verify that condition.

Write $\mu_b=\langle C_{\rm body}\rangle-C_{\rm ref}$.
Then
$$
 C_{\rm cap}+tc-C_{\rm ref}
                   =\mathcal Z+(1-t)c_0+t\mu_b,
 \qquad |\mu_b|\le\rho/25+3\,10^{-13}.
 \tag{HA.13}
$$
Its curvature error is bounded by $10^{-12}$ plus the larger of
$|c_0|$ and $|\mu_b|$. With the above cap $B$ bound, its pair supremum
is less than $10^{-5}$ throughout the segment. Hence the same
R144 monotone trace lemma applies off shell under these actual
conditional inputs; nonmean matching has not been assumed.

Finally, the R144 derivative bound retains a concrete reciprocal fee.
The old radius enclosure gives $a(R)>6.56\,10^{-6}$.
Using $\pi>157/50$,
$$
 \mathcal B(c)>\frac{3\pi}{20}a(R)^2
       >20.2688256\,10^{-12}>2\,10^{-11},
 \qquad
                         \mathcal B(c)^{-1}<5\,10^{10}.
 \tag{HA.14}
$$
This is an explicit, large allowed row-transformation cost, not a
claim that it is harmless in any inverse norm.

## 6. What is now automatic and what is still required

If a true core satisfies the original $10^{-4}$ moving correction
bound, its waist branch, negative waist sign and physical outer
neighbourhood in R144 follow from (HA.6), (HA.7), and (HA.10).
For a genuine cap in its original complete small input ball, the
cap neighbourhood and the full off-shell interpolation follow as well.
All these statements cover the actual implicit selected parameter
without replacing it by an interval endpoint.

The proof does not produce that exact core, place its exterior
trace in (HA.11), solve the common nonmean rows or the waist odd row,
or settle the far/height/phase equations. It records the precise
geometric admission consequences of those remaining input gates.
