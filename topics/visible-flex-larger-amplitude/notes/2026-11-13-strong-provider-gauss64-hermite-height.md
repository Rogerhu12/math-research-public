# The initial Hermite height: an analytic Gauss64 remainder

**Status: proved for the intended analytic frozen segment; 18 exact rational
checks executed.** The actual NumPy rule and rounded arithmetic remain unpaid.
This is background profile geometry, not the independent nonlinear surface mean.

This fills the initial-Hermite exception in
notes/2026-11-13-strong-provider-gauss64-phase-truncation.md.
It uses the same exact Gaussian rule and does not modify any physical parameter,
the provider, or any MJS source.

## 1. Frozen cubic speed and an analytic square-root branch

The provider's initial Hermite speed, with $u=s/S$, is
$$
 v(u)=bu+(3V-2b)u^2+(b-2V)u^3,\qquad b=k_0S.
$$
The frozen binary values are $V=0.31980000000000003$ and $k_0=0.45$,
interpreted as their exact binary64 rationals. The previously executed
33-guard analytic-profile certificate proves $4/5<S<9/10$ from the unique
positive root of
$$
 k_0S^2+6VS=12\delta.
$$
Exact rational checks, without rounding $k_0$ to $9/20$, imply
$$
 \frac{319}{1000}<V<\frac{321}{1000},\qquad
 \frac{359}{1000}<b<\frac{406}{1000}.
$$

Center the cubic at $u=1/2$. Writing $z=u-1/2$ gives the exact identity
$$
 v(1/2+z)=A_0+A_1z-\frac b2 z^2+(b-2V)z^3,
$$
$$
 A_0=\frac b8+\frac V2,\qquad A_1=\frac{3V}{2}-\frac b4.
$$
Here $A_0,A_1>0$ and $b-2V<0$.
For $|z|\le7/8$, the preceding rational endpoint bounds give
$$
 |v|<\frac9{10},\qquad |v'|<\frac75,\qquad |v''|<2. \tag{1}
$$
The supplied exact-arithmetic script evaluates the cubic coefficient majorant
and its first two derivatives with these outward endpoint bounds.

Consequently $1-v^2$ stays in the open disc with center1 and radius $81/100$.
It is nonzero and lies in the right half-plane. The function
$$
 f(u)=\sqrt{1-v(u)^2}
$$
has a single analytic branch on this whole disc, positive at real $u=0$.
Furthermore,
$$
 \frac25<|f(u)|<\frac32.
$$
The lower inequality follows from $|1-v^2|>19/100>(2/5)^2$.

Differentiate the same analytic branch:
$$
 f'=-\frac{vv'}f,\qquad
 f''=-\frac{(v')^2+vv''}{f}-\frac{v^2(v')^2}{f^3}.
$$
Using (1) and the lower branch modulus gives
$$
 |f'|<4,\qquad |f''|<36. \tag{2}
$$
The second bound is deliberately conservative; its displayed rational
majorant is $5473/160<36$.

## 2. Every partial Hermite integral uses that same disc

Let $0\le w\le1$ and
$$
 I(w)=\int_0^w f(u)\,du,\qquad
 Q(w)=w\sum_{i=1}^{64}\omega_i f(wx_i),
$$
where the nodes and weights are those of the exact positive Gauss64 rule on
$[0,1]$. The provider evaluates $w=1$ for its initial background-height
increment; variable $w$ here supplies a continuous comparison interface.

For $|x-1/2|\le7/8$,
$$
 |wx-1/2|
 \le\frac{1-w}{2}+\frac78w\le\frac78.
$$
Thus the branch and all bounds in (1)-(2) apply uniformly to every partial
integral, including $w=0$.
As in the phase-panel proof, the derivative kernels of $w f(wx)$ are
$$
 F_1=f(wx)+wx f'(wx),\qquad
 F_2=2x f'(wx)+wx^2f''(wx).
$$
Since $|x|\le11/8<3/2$ and $w\le1$, we may use
$$
 M_0=\frac32,\qquad M_1<8,\qquad M_2<128. \tag{3}
$$

The ratio of the real evaluation radius $1/2$ to the analytic radius $7/8$
is $r=4/7$. A degree-127 Taylor polynomial about $1/2$ has remainder at most
$$
 M\sum_{j=128}^{\infty}r^j=\frac73 M r^{128}.
$$
Gaussian exactness and positive mass one therefore bound the integral-rule
difference by
$$
 \frac{14}{3}M r^{128}. \tag{4}
$$
This is uniform on the whole interval, rather than a residual evaluated only
at quadrature nodes.

## 3. Physical zeroth, first and second derivative bounds

The physical background-height primitive is $H(s)=S I(s/S)$; its exact-rule
version is $H_G(s)=S Q(s/S)$. Applying (4) to the kernels in (3), and using
$4/5<S<9/10$, gives
$$
 |H_G-H|<7(4/7)^{128}<2^{-100},
$$
$$
 |(H_G-H)_s|<38(4/7)^{128}<2^{-98},
$$
$$
 |(H_G-H)_{ss}|<747(4/7)^{128}<2^{-93}. \tag{5}
$$
All three final comparisons are exact BigInt rational inequalities in the
executed result. No floating logarithm or asymptotic approximation is used.

Combining (5) with the phase-panel bounds gives the following conditional
bound for the complete ideal background primitive with fixed, compatible
segment data:
$$
 |H_G-H|<2^{-99},\qquad
 |(H_G-H)_s|<2^{-98},\qquad
 |(H_G-H)_{ss}|<2^{-93}
$$
within each open piece. The zeroth-order phase contribution is below
$2^{-118}$, so it is absorbed into $2^{-99}$.
Exact constant coasts have zero truncation error. The derivative estimates
are piecewise statements; any nonzero Gaussian derivative jump at a join
must still be distinguished from the analytic reference's exact compatibility.

## 4. Reproducibility and remaining scope

The standalone arithmetic source is
computations/strong_provider_gauss64_hermite_height.js.
Its complete 18-guard result is
notes/2026-11-13-strong-provider-gauss64-hermite-height.json.
They were executed through a JavaScript BigInt isolate, with zero physical
ODE, Newton, prefix, or tail-worker calls.

The hypotheses refer to the same exact fixed segment data in both models.
The actual provider additionally uses rounded segment construction, NumPy
Gauss nodes and weights, square roots and dot products. None of those errors
is hidden in (5). They must be bounded separately, together with the exact
choice of physical knots and their seams. The nonlinear surface mean defined
by the actual PDE is a different integral and is not certified by a
background-height calculation.
