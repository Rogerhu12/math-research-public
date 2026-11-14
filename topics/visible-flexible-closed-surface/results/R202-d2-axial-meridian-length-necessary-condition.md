# R202. A calibrated length bound for a D2 axial meridian

## Statement and scope

Let a regular $C^2$ surface strip have an exact reflection symmetry across the plane $y=0$, with the fixed material curve $u=0$. Suppose its axial curve, oriented from the central cylinder towards the cut, has endpoints and unit tangents

$$
\gamma(0)=(A,0,c),\qquad
\gamma(\ell)=(a_c,0,Z),\qquad
T(0)=e_z,\qquad T(\ell)=-e_x.
\tag{1}
$$

Here $\ell$ is its actual arclength. Assume every principal-curvature magnitude on this curve is at most $C>0$. Put

$$
r=C^{-1},\qquad d_x=A-a_c,\qquad d_z=Z-c,
$$

and assume $d_x,d_z\ge r$. Then

$$
\boxed{\displaystyle
\ell\ \ge\ \frac{\pi r}{2}
+\sqrt{(d_x-r)^2+(d_z-r)^2}.}
\tag{2}
$$

The curve may reverse turning direction or wind its tangent any integer number of times. No monotonicity of its tangent angle or its position is assumed.

If the original material variable is $s\in[c,S]$ and the actual metric satisfies $|X_s|^2\le1+\varepsilon$ there, then necessarily

$$
\boxed{\displaystyle
\frac{\pi r}{2}
+\sqrt{(A-a_c-r)^2+(Z-c-r)^2}
\ \le\ (S-c)\sqrt{1+\varepsilon}.}
\tag{3}
$$

This is a necessary condition on the specified axial curve. It neither proves existence when the inequality holds nor excludes other surface constructions. In particular, it is not asserted for the reflection-relaxed R201 representations, whose chosen material curve need not remain in one fixed plane.

## 1. Why the reflected axial curve has the surface curvature bound

Write the reflection as $M(x,y,z)=(x,-y,z)$ and the local identity as

$$
X(s,-u)=M X(s,u).
$$

At $u=0$, the vectors $X_s$ and $X_{ss}$ belong to the fixed plane, whereas differentiation in $u$ gives $M X_u=-X_u$. Thus $X_u$ is perpendicular to that plane. Regularity makes $X_s$ and $X_u$ nonzero and independent.

The unit tangent to the axial curve lies in the fixed plane. Its arclength derivative is also in that plane and is perpendicular to the tangent. It is therefore parallel to the surface normal $X_s\times X_u$. The axial curve has no geodesic-curvature component, and its curvature is the normal curvature in its own tangent direction. Consequently

$$
|T'(\sigma)|\le C
$$

for arclength $\sigma$. This argument concerns the actual induced geometry and does not require the target metric to have been attained exactly.

## 2. A nonnegative angular calibration

Work in the $(x,z)$ plane. Since the axial curve is regular and $C^2$, its unit tangent has a continuously differentiable angle lift

$$
T(\sigma)=(\cos\theta(\sigma),\sin\theta(\sigma)),\qquad
\theta(0)=\frac\pi2,\qquad
\theta(\ell)=\pi+2\pi k
$$

for some integer $k$. The curvature bound gives $|\theta'|\le1/r$.

First suppose $(d_x-r,d_z-r)\ne(0,0)$, and choose the northwest unit vector

$$
v=\frac{(-d_x+r,\ d_z-r)}
{\sqrt{(d_x-r)^2+(d_z-r)^2}}.
$$

Its coordinates have signs $v_x\le0$, $v_z\ge0$, and

$$
1\le -v_x+v_z\le\sqrt2.
$$

Define the nonnegative periodic function

$$
w(\theta)=1-v\cdot(\cos\theta,\sin\theta)\ge0.
$$

For every point of the curve, $w\ge r w|\theta'|$. Integration and the triangle inequality give

$$
\begin{aligned}
\ell-v\cdot(-d_x,d_z)
&=\int_0^\ell w(\theta(\sigma))\,d\sigma\\
&\ge r\int_0^\ell w(\theta(\sigma))|\theta'(\sigma)|\,d\sigma\\
&\ge r\left|\int_0^\ell
w(\theta(\sigma))\theta'(\sigma)\,d\sigma\right|.
\end{aligned}
\tag{4}
$$

Over the positive quarter turn, the last primitive changes by

$$
q=\int_{\pi/2}^{\pi}w(\theta)\,d\theta
=\frac\pi2-v\cdot(-1,1).
$$

The inequalities above imply $0<q<\pi$. Over a full turn, the primitive changes by $2\pi$, because both trigonometric integrals vanish. For the actual lifted endpoint, the absolute primitive change is therefore

$$
|q+2\pi k|\ge q
$$

for every integer $k$. This pays all winding and all nonmonotone turning without replacing the actual path by a presumed short arc.

Substitution into (4) yields

$$
\begin{aligned}
\ell
&\ge v\cdot(-d_x,d_z)
+r\left(\frac\pi2-v\cdot(-1,1)\right)\\
&=\frac{\pi r}{2}
+v\cdot(-d_x+r,d_z-r)\\
&=\frac{\pi r}{2}
+\sqrt{(d_x-r)^2+(d_z-r)^2},
\end{aligned}
$$

as claimed. If $d_x=d_z=r$, choose any northwest unit vector in (4); its displacement term cancels the corresponding calibration term and gives $\ell\ge\pi r/2$. This proves the remaining case of (2).

## 3. Material length and the explicit height window

The actual material curve has arclength

$$
\ell=\int_c^S |X_s(s,0)|\,ds
\le (S-c)\sqrt{1+\varepsilon}.
$$

Combining this with (2) proves (3). In particular, a relative metric-operator bound $\|g_*^{-1/2}(g_X-g_*)g_*^{-1/2}\|\le\varepsilon$ for $g_*=ds^2+a(s)^2du^2$ implies the required axial upper bound.

For a known upper length $L$ define

$$
Q=L-\frac{\pi r}{2}.
$$

If $Q<d_x-r$, (2) excludes all $d_z\ge r$. Otherwise it implies the explicit upper height

$$
Z\le c+r+\sqrt{Q^2-(A-a_c-r)^2}.
\tag{5}
$$

Every endpoint quantity in (3) and (5) belongs to the same complete field. In particular, a numerical background height cannot be substituted for the actual cut height. Increasing or decreasing a cylinder length, changing the cut, or changing the actual field requires the corresponding new quantities.

A final reach certificate can supply a curvature cap by the previously proved normal-ball consequences. This result itself uses only the stated curvature cap. A soft numerical guide is not a completion requirement and must not be silently identified with a sharp reach threshold.

## 4. Application domain for the current D2 B32 family

For the preserved D2 direct-position family, the central cylinder has exact length $c=13/128$. At its upper end the major-axis point is $(A,0,c)$ with tangent $e_z$. The flat cut has $a_c=4/5$ and tangent $-e_x$. The prescribed zero endpoint two-jets preserve these facts when the finite radius-design coefficients are changed.

The accurately normalized central ellipse has already been bounded by

$$
A>1.3620341722637314.
$$

The exact B32 endpoint packet gives the rational upper bound

$$
S\le
\frac{
102554037038709242770677509655085306426610152687168707111979643573445579262687
}{
115792089237316195423570985008687907853269984665640564039457584007913129639936
}
<\frac{88568}{100000}.
\tag{6}
$$

The source identities are recorded in the exact-domain report: the central-normalization report SHA256 begins $2f8e8dd3$ and ends $1ce186550$; the full B32 accurate-profile packet SHA256 is

`10fa877f5b1a5595416858d24878d0ba597001cb5eb8094ca9b4b8135cb71243`.

The candidate identity is the already fixed B32 $9c903de9\ldots59a938d$. The current radius-design coefficients change $a(s)$ but do not change these material endpoints.

Using only the weaker rational conditions

$$
A\ge\frac{136203}{100000},\quad
S\le\frac{88568}{100000},\quad
Z\ge\frac{62499}{100000},\quad
C\le\frac{19}{2},\quad
0\le\varepsilon\le10^{-6},
\tag{7}
$$

with $a_c=4/5$ and $c=13/128$, inequality (3) is strictly impossible. Here one applies (3) with the permitted weaker cap $19/2$, even if the actual curvature bound is smaller, so that the displacement assumptions only need to be checked against $r=2/19$. The supplied exact rational consumer proves this finite system of inequalities without using floating square roots or floating $\pi$.

This is a conditional domain exclusion. The accurate cut-height hypothesis in (7) has not yet been certified for the saved finite-height $0.625$ field. The saved field also has much larger metric and curvature errors. Thus this result does not relabel that finite field as a rigorously excluded actual surface; it identifies the conflict that would result if all of (7) were to be achieved.

## 5. Exact certificate arithmetic

Let $\pi_-$ be a proved rational lower bound for $\pi$, put $r=2/19$, and use the least allowed $A,Z$ and the largest allowed $S,\varepsilon$. Define the rational numbers

$$
u=\frac{r\pi_-}{2},\qquad
v=(A-a_c-r)^2+(Z-c-r)^2,\qquad
L_2=(S-c)^2(1+\varepsilon).
$$

Because $u,v\ge0$, the strict inequality $u+\sqrt v>\sqrt{L_2}$ holds if either

$$
M:=L_2-u^2-v<0,
$$

or

$$
M\ge0,\qquad 4u^2v-M^2>0.
\tag{8}
$$

Conversely, these cases exactly characterize that strict inequality for the stated nonnegative quantities. All tests in (8) are rational.

The consumer obtains $\pi_-$ from Machin's identity

$$
\pi=16\arctan(1/5)-4\arctan(1/239).
$$

For completeness, $\tan(2\arctan(1/5))=5/12$ and $\tan(4\arctan(1/5))=120/119$; the tangent subtraction with $1/239$ is exactly one. Its positivity follows from $4(1/5-1/(3\cdot5^3))-1/239>0$, and it is less than $4/5<1<\pi/2$; the last inequality follows from $\pi/2=2\int_0^1(1+x^2)^{-1}\,dx>1$. Hence the angle lies in $(0,\pi/2)$ and equals $\pi/4$. The alternating power series for each arctangent encloses it between the $N$-term partial sum and that sum plus its next term. The code uses $N=16$ and exact integer fractions. The same code directly verifies the strict last comparison in (6).

Already the shorter rational estimate

$
\pi>16\left(\frac15-\frac{1}{3\cdot5^3}\right)-\frac4{239}
=\frac{281476}{89625}>\frac{157}{50}
$

suffices for (7). With $\pi_-=157/50$, the exact values are

$
u=\frac{157}{950},\qquad
v=\frac{4430161561117}{11552000000000},\qquad
L_2=\frac{98374538983440609}{160000000000000000},
$

and

$
M=\frac{11784864767437059849}{57760000000000000000}>0,
$

$
4u^2v-M^2=
\frac{891749382786007519708098322392097199}
{3336217600000000000000000000000000000000}>0.
$

These displayed positive integers independently close the strict domain claim; the executable's $N=16$ enclosure is tighter.

The complete real V8 diagnostic took 10 ms. It returned strict exclusion for (7), no exclusion from this necessary bound when the lower height is changed to $121/200$, and no exclusion when the curvature cap at $Z=5/8$ is replaced by $1000/97$. The latter two outputs are not existence claims.

## 6. Finite diagnostics, kept separate from (7)

Using the saved floating endpoint values $A=1.3620341722637315$, $S=0.8856739498716915$ and $\varepsilon=0$ gives the following diagnostics. They are not the exact certificate.

| Finite cut height | Available outer length | Necessary length for guide 9.5 | Excess of necessary length |
| --- | --- | --- | --- |
| 0.625 | 0.7841114498716915 | 0.7846284524763574 | +0.0005170026046659 |
| 0.605 | 0.7841114498716915 | 0.7713028929352224 | -0.0128085569364691 |
| 0.600 | 0.7841114498716915 | 0.7680291723605599 | -0.0160822775111316 |

The finite height upper value from (5), at guide 9.5, is about $0.6242339800687295$. In contrast, the reach-related cap $1000/97$ permits about $0.6261650732612207$ by this particular necessary condition. Consequently the guide/height conflict must not be promoted to a general strong-target impossibility.

Prescribing the proposed finite height $0.605$ would define a new field, leave a margin above the earlier sufficient cap-window lower endpoint $0.60$, and leave more arclength allowance in this necessary test. A subsequently enlarged sufficient cap window does not change the axial necessary condition. It still needs actual optimization and every complete geometry certificate. At the time this proof was closed, its terminal launch had failed before a process was created because the executor was unavailable; no $0.605$ state or accepted step is asserted by this proof.

## Artifacts

The complete exact consumer is `scripts/fd2d-axial-meridian-length-bound-R202.cjs`, with factory `createR202AxialLengthBound()`. Its strict interface accepts explicit rational pairs and returns the exact quantities in (8), the proved rational $\pi$ interval, and a scope-qualified domain result. Its separate floating diagnostic is labelled as such.

The actual small execution is recorded in `notes/2026-11-13-fd2d-R202-axial-domain-exact-01.json`. No whole-body evaluation or nonlinear solve was performed for this theorem, and no claim is made for the symmetry-relaxed R201 branch.
