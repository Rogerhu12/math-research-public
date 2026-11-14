# Independent review of the finite-tail metric and curvature formulas

Reviewer: `coupled_prefix`, 2026-11-09. This reviewer did not implement the
audited backend. The review covers `metric_residuals`,
`perturbative_curvature`, `direct_curvature`, and their cylindrical
coefficient conventions in `scripts/db6f-audit-tail-metric-curvature.py`.
It does **not** certify the supplier's background packets, all-tail interval
coverage, the closed surface, or README completion.

The mathematical formulas pass. The initially reviewed source hash was
`87bcf9d395e3d83df11e1d8d3ba5c0ca77dcc10645feff390c45271421373e9d`.
A zero-vector interval-norm edge case was found and safely rejected by
that version. The author corrected it without changing the three formulas.
The reviewed corrected hash is
`ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`.
The distinction between these versions is retained in the two test reports.

## Coordinates and metric

Write the actual map in the rotating orthonormal frame as
$$
F=(r+R)e_r+T e_\theta+(h+Z)e_z,\qquad h_r=w,
\qquad g=E\,dr^2+r^2d\theta^2,\quad E=1+w^2.
$$
Direct differentiation gives
$$
F_r=(1+R_r,T_r,w+Z_r),\qquad
F_\theta=(R_\theta-T,r+R+T_\theta,Z_\theta).
$$
Subtracting the background metric before bounding coefficients therefore
gives exactly the three expressions in `metric_residuals`. In particular,
the radial term includes $2wZ_r$, the mixed term includes the full
$(w+Z_r)Z_\theta$, and the angular term includes
$2r(R+T_\theta)$. None may be replaced by an absolute first-jet bound
before these cancellations.

If their absolute bounds are $b_{rr},b_{r\theta},b_{\theta\theta}$,
the code bounds the symmetric normalized residual entrywise by
$$
A=\frac{b_{rr}}{E_{\min}},\qquad
B=\frac{b_{r\theta}}{r_{\min}\sqrt{E_{\min}}},\qquad
C=\frac{b_{\theta\theta}}{r_{\min}^2}.
$$
The spectral operator norm is at most $\max(A+B,B+C)$, by the maximum
row sum bound for a symmetric matrix. Thus `metric` is a valid relative
metric bound, conditional on the supplied background enclosures.

The coefficient conventions are consistent: the saved complex planar mode
$c_m e^{im\theta}$ becomes $c_m e^{i(m-1)\theta}$ in the rotating frame.
For $m=1+3k$, this has radial coefficient $c_m\cos(3k\theta)$ and
tangential coefficient $c_m\sin(3k\theta)$. The code's imaginary Laurent
phase and opposite signs give precisely this positive sine. `P.theta()`
multiplies frequency $k$ by $3k$, as required. Negative planar modes are
handled by the same formula.

## Perturbative curvature

For $V=F-F_0$, the three components of its ambient covariant Hessian in
the background orthonormal frame are
$$
H_{11}=\frac{V_{rr}-(ww_r/E)V_r}{E},\qquad
H_{12}=\frac{V_{r\theta}-V_\theta/r}{r\sqrt E},\qquad
H_{22}=\frac{V_{\theta\theta}+(r/E)V_r}{r^2}.
$$
The extra rotating-frame terms in $V_\theta,V_{r\theta}$ and
$V_{\theta\theta}$ in the implementation are correct. If their Euclidean
norms are bounded by $h_{11},h_{12},h_{22}$, then
$$
|H(v,v)|\le\eta |v|_g^2,\qquad
\eta=\max(h_{11}+h_{12},h_{12}+h_{22}).
$$
Let $K_0$ bound the background principal curvatures and let the relative
metric bound be $\epsilon<1$. The background embedding satisfies
$\operatorname{Hess}_gF_0=\mathrm{II}_0n_0$. Projection onto the *actual*
normal eliminates the difference between the actual and background
connections, so for every vector
$$
|\mathrm{II}_F(v,v)|
\le(K_0+\eta)|v|_g^2
\le\frac{K_0+\eta}{1-\epsilon}|v|_{F^*\mathrm{eucl}}^2.
$$
This proves the returned bound. It does not assume the actual normal is
close to the background normal, and it needs a valid independent $K_0$.

## Direct curvature and cancellation

The direct branch uses actual Cartesian second jets expressed in the
rotating frame. Its $F_{r\theta}$ tangential component contains the
background $1$, and its $F_{\theta\theta}$ radial component contains
the background $-r$. The complete vertical sums are $w+Z_r$ and
$w_r+Z_{rr}$ before Bernstein evaluation. All signs agree with direct
differentiation of the Cartesian map.

Writing $\ell=|F_r\times F_\theta|$, the metric estimate gives the
additional area lower bound
$$
\ell\ge r\sqrt E(1-\epsilon).
$$
Intersecting this lower bound with the direct interval norm enclosure is
valid. The code then encloses the actual unit normal and both fundamental
forms. For coefficients $E_F,F_F,G_F$ and $L,M,N$, its expressions
$$
\operatorname{tr}S=
\frac{LG_F-2MF_F+NE_F}{\ell^2},\qquad
\det S=\frac{LN-M^2}{\ell^2}
$$
are correct. The maximum absolute principal curvature is
$$
\frac{|\operatorname{tr}S|+
\sqrt{(\operatorname{tr}S)^2-4\det S}}2.
$$
The true discriminant is nonnegative, so imposing that known lower bound
on its interval is legitimate. The final upper-tail vertical reflection
is an ambient isometry and preserves these metric and absolute-curvature
bounds.

## Independent execution and the corrected edge case

`scripts/db6f-prefix-review-tail-formulas.py` forms analytic maps in
Cartesian coordinates and differentiates them by a separate two-variable
second-order automatic-differentiation implementation. It does not reuse
the audited cylindrical differentiation. Each of three cases is compared
on 11 radial values and 97 angular values, and the coefficient expressions
are checked against those Cartesian jets.

The initial test record is
`2026-11-09-db6f-prefix-review-tail-formulas-v1.json`. A zero Hessian
component produces squares with lower endpoint zero; outward-rounded
addition can then make their sum's lower endpoint a negative subnormal.
The original square-root routine rejected it. The author's correction
retains the known structural lower bound zero for a sum of three squares
before taking the square root. It does not lower any upper endpoint.
This is a safe-rejection fix, not a repair of an underestimated certificate.

The corrected rerun is
`2026-11-09-db6f-prefix-review-tail-formulas-v2.json`; all cases pass:

| Analytic case | Direct curvature upper | Perturbative upper | Sampled actual curvature |
|---|---:|---:|---:|
| Round cone, $V=0$ | 2.51558 | 2.00001 | 1.11804 |
| Threefold polynomial perturbation | 3.68811 | 2.03204 | 1.48777 |
| Large second jets cancelling to a cone | .988706 | 112.962 | .912681 |

The last case has $w=20r-9$ and
$Z=-10r^2+(19/2)r$, so $w+Z_r=1/2$ and $w_r+Z_{rr}=0$ exactly.
It verifies the practical value of preserving these cancellations.
The largest coefficient-formula discrepancy in the floating Cartesian
checks is $2.23\times10^{-15}$. Floating comparisons allow an explicit
roundoff tolerance; they are diagnostics, while the formulas above supply
the mathematical argument. For the exact round cone the true metric
residual is zero, even though floating Cartesian evaluation returns about
$4.5\times10^{-16}$.

Reproduction:

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-review-tail-formulas.py \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-review-tail-formulas-v2.json
```

The remaining gate is the analytic validity and complete partition of the
actual background packets, followed by the actual full-tail run. This
component review alone does not pay either gate.
