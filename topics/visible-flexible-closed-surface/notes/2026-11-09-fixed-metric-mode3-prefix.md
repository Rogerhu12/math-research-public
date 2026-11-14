# Mode3 planar support core and real-prefix implementation

2026-11-09. Astra-visible-flex-4ffd372b numerical subagent. Work in progress; no closed-surface claim.

## Exact core

For `h(φ)=1+q cos(3φ)`, the normal-angle parametrization is

\[
\gamma(\phi)=h(\phi)n(\phi)+h'(\phi)t(\phi),\quad
\rho=h+h''=1-8q\cos3\phi,
\]

\[
\theta=\phi-\frac{8q}{3}\sin3\phi,\qquad
\gamma_\theta=t(\phi),\quad
\gamma_{\theta\theta}=-\frac{n(\phi)}{\rho(\phi)}.
\]

For `0≤q<1/8`, this has perimeter `2π`, constant width `2`, and exact curvature maximum `1/(1−8q)`. The generalized cylinder over this curve therefore has exact metric `ds²+dθ²`.

`fixed_metric_mode3_core.py` implements these formulas by safeguarded inversion of the analytic arc map. It also permits additional support coefficients `c_j cos(3jφ)`. Perimeter stays exactly `2π`; positive curvature is checked using a sampled lower bound minus a global derivative Lipschitz allowance. Any even-frequency support coefficient changes width, and the code reports that explicitly. Parent confirmed that constant width is a useful initial core, not a completion requirement; corrected cores must report actual width/support/curvature data.

## Exact core parameter Jacobian

For a general support coefficient `c_m`, differentiation at fixed arclength gives

\[
\partial_{c_m}\phi=-\frac{(1-m^2)\sin(m\phi)}{m\rho},
\qquad
\partial_{c_m}\gamma=\cos(m\phi)n-\frac{\sin(m\phi)}m t.
\]

The cancellation follows from `γ_φ=ρ t`. Projection of this exact derivative gives the inlet Jacobian; no finite difference of a numerically inverted curve is needed. At `q=0`, the first cylindrical coefficients are `r_m=q`, `t_m=−q/m`, `z_m=0`.

## Projection diagnostic (2026-11-09)

`fixed_metric_mode3_core_projection.json` checks the exact inlet against the complete cylindrical modes `3,6,...,3M`. The exact arclength metric is at floating-point precision throughout. At `q=.10`, where the exact core curvature maximum is `5`, the truncated inlet has:

| M | whole-angle metric l1 diagnostic | maximum second-jet projection error |
|---:|---:|---:|
| 4 | .0263454 | 2.06496 |
| 8 | .0106516 | 1.21630 |
| 16 | .00259039 | .471566 |
| 32 | .000267182 | .0831271 |
| 64 | 5.67721e−6 | .00318493 |

Thus a low-M solution at large `q` would not meet the metric tolerance even at the cylinder inlet. These projection rows are not BVP convergence evidence. Small amplitudes can use low M; large amplitudes require stronger angular resolution or a representation that preserves the exact inlet.

## New physical tail

The actual mode3 DN seed is the parent's `root_cut_tail_cap002_p160_m3_s1024_far48.json`, with protectCell160 and frequencies3,6,9,12. It is a new physical metric relative to the earlier N80 table. The code will use its genuine coefficients and cut jets, with no rescaling of an old tail. Nonlinear matching and infinite round-collar extension remain separate requirements.


### Complete derivation of the moving-frame term

The outward normal and positively oriented tangent satisfy `n_φ=t` and `t_φ=−n`. Hence

\[
\gamma_\phi=h'n+h t+h''t-h'n=(h+h'')t=\rho t.
\]

At fixed normal angle, a coefficient variation has

\[
(\partial_{c_m}\gamma)_\phi=\cos(m\phi)n-m\sin(m\phi)t.
\]

At fixed arclength, the chain rule adds the entire rotating-frame contribution `γ_φ δφ=ρ t δφ`. Differentiating the analytic arc equation gives

\[
0=\rho\,\delta\phi+\frac{1-m^2}{m}\sin(m\phi),
\]

so

\[
\delta\gamma=\cos(m\phi)n-\left[m+\frac{1-m^2}{m}\right]\sin(m\phi)t
=\cos(m\phi)n-\frac{\sin(m\phi)}m t.
\]

In particular, this is not differentiation while holding `φ` fixed. The additional derivative of the tangent is

\[
\delta\gamma_\theta=-n\delta\phi
=-\frac{m^2-1}{m\rho}\sin(m\phi)n.
\]

For completeness, with `δρ=(1−m²)cos(mφ)+ρ_φ δφ`,

\[
\delta\gamma_{\theta\theta}=-\frac{t\delta\phi}{\rho}+\frac{n\delta\rho}{\rho^2}.
\]

These formulas hold for arbitrary finite support coefficients in the verified strictly convex domain; they do not rely on small amplitude or constant width.

## Actual p160 mode3 linear-port nonlinear prefix (design branch)

Physical prefix controls are vu=.25, vd=.4, ramp=.4, cycles=1; parent planar inlet root delta=.0725268280429954. The nonlinear Frenet flow uses the general cylindrical basis directly, without invoking or changing the reflected nonplanar core guard. Exact core parameter derivatives are projected for the boundary Jacobian.

| support q | designed delta | metric l1 | full Darboux l1 | sampled kappa | port height |
|---:|---:|---:|---:|---:|---:|
| 0.001 | 0.072526836720625515 | 2.5591408e-11 | 2.4695002e-08 | 5.3223365 | 1.5970463e-05 |
| 0.003 | 0.072526906567479524 | 4.9841603e-10 | 1.995007e-07 | 5.3471485 | 4.7911359e-05 |
| 0.01 | 0.072527700860683192 | 2.1480824e-07 | 1.6992868e-05 | 5.4338973 | 0.0001597034 |

All three M4 solves report convergence. These rows adjust delta and therefore are design exploration, not fixed-metric convergence. At q=.01 the metric l1 happens to be below1e-6 but the full Darboux defect is1.70e-5; M4 is not a resolved full solution. The maximum support width defect is7.57e-6, and height remains1.168. The tail is an actual physical *linear* DN; no nonlinear tail/round closure has been established. Checkpoints and exact coefficient chunks are named in fixed_metric_mode3_p160_design2_m4_summary.json.

The geometry/flow checks in fixed_metric_mode3_checks.json compare Cartesian and local-frame equations (max difference4.80e-13), complex-step state Jacobian (relative4.85e-16), and reinverted-arc finite differences of the analytic core derivatives (max2.63e-8 at step2e-7, consistent with arc-inversion roundoff amplification). Independent mathematical review in2026-11-09-audit-support-core.md passed the complete fixed-theta formulas. Its correction was applied: the reported admissibility speed limit now uses the conservative curvature_lower_bound, with the sampled value labeled separately.

At fixed q=.01-designed metric, M4 tolerances are being tightened to2e-9/2e-10 with q itself an extrinsic unknown. Momentum-based m15,18,21,24 DN values are being computed on the identical p160 metric, to permit M8 extension. The low four port entries will remain unchanged in the first angular comparison; the new higher entries are actual physical responses, not extrapolated slopes.



## Support gap and radius under higher corrections

For the phase rotation `α=π/3`,

\[
h(\phi)-h(\phi-\alpha)=2\sum_{j\ {\rm odd}}c_j\cos(3j\phi).
\]

Even `j` corrections cancel exactly in this support difference, although they change width. The direction `φ=0` therefore gives the exact algebraic lower bound `2|Σ_{j odd}c_j|` for the Hausdorff support gap of the two central curves, and the more conservative bound is `2q−2Σ_{j≥3,odd}|c_j|`. Translating that central-curve fact to the prescribed material displacement and Euclidean-alignment conditions remains the parent construction's task.

For a convex body containing the origin, `max|x|=max h`. If `q>Σ_{j≥2}j²|c_j|`, the support polynomial `h=1+Σc_j T_j(cos3φ)` is increasing as a function of `cos3φ`, because `|T_j'|≤j²`. Consequently its exact extrema are `h_max=1+Σc_j` and `h_min=1+Σ(−1)^j c_j`; otherwise the code reports the general coefficient l1 radius bounds. These are algebraic bounds for the selected support curve, separate from sampled bounds for the full prefix.
