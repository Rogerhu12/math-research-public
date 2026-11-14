# Tangent-angle core, analytic coordinates, and prefix chart

2026-11-09. Astra-visible-flex-4ffd372b numerical subagent. Work in progress; finite prefixes/ports are not round collars.

## Exact family and amplitude convention

For an integer `m≥2`, prescribe

\[
\phi(\theta)=\theta+\sum_{j=1}^{M}b_j\sin(mj\theta),\qquad
\gamma_\theta=i e^{i\phi(\theta)}.
\]

The tangent is exactly unit speed. Its Fourier frequencies are all congruent to1 modulo m, so its mean vanishes and integration gives an exactly closed planar curve with perimeter2π. Strict positivity of

\[
\kappa(\theta)=\phi'(\theta)=1+\sum_j mj b_j\cos(mj\theta)
\]

makes the curve strictly convex. The implementation uses the coefficient l1 curvature bounds or, when sharper, a sampled extremum minus/plus a global derivative Lipschitz allowance. The single-harmonic bounds are exact.

The numerical continuation parameter is

\[
q_{\rm eff}=\frac{m b_1}{m^2-1}.
\]

For m3, this is `3b1/8`, the first-order cylindrical radial amplitude. It is not the support-function coefficient used in the earlier branch. All new reports name it `tangent_q_eff` or `actual_tangent_q_eff` and identify the core family.

## Antiderivative and Bessel truncation

The product of Jacobi–Anger expansions yields real coefficients `A_l` with

\[
e^{i\phi(\theta)}=\sum_{\ell\in\mathbb Z}A_\ell e^{i(1+m\ell)\theta},\qquad
\gamma(\theta)=\sum_\ell\frac{A_\ell}{1+m\ell}e^{i(1+m\ell)\theta}.
\]

The zero translation is chosen; no denominator vanishes. For one harmonic, `A_l=J_l(b1)`.

For `x=|b|/2`, the Bessel power series gives

\[
|J_k(b)|\le e^{b^2/4}\frac{x^{|k|}}{|k|!},
\quad
\sum_{|k|>K}|J_k(b)|\le
\frac{2e^{b^2/4}x^{K+1}}{(K+1)!\,[1-x/(K+2)]}.
\]

The latter bound applies when `K+2>x`. The Fourier coefficient l1 norm of each factor is at most `e^{|b|}`, from its two exponential power series. Multiplying finite Bessel factors and summing the corresponding product-tail bounds therefore bounds the omitted `A_l` l1 norm. Since `|1+mℓ|≥1`, the same number bounds the coordinate antiderivative tail. Floating-point evaluation/convolution errors are separate and are not interval-enclosed.

## Exact parameter Jacobian in Fourier form

For the phase coefficient `b_j`,

\[
\partial_{b_j}e^{i\phi}=i\sin(mj\theta)e^{i\phi},\qquad
\partial_{b_j}A_\ell=\frac{A_{\ell-j}-A_{\ell+j}}2,
\]

\[
\partial_{b_j}\gamma=\sum_\ell
\frac{A_{\ell-j}-A_{\ell+j}}{2(1+m\ell)}e^{i(1+m\ell)\theta}.
\]

Equivalently, `∂_{b_j}γ_θ=−e^{iφ}sin(mjθ)`. The first derivative column is multiplied by `(m²−1)/m` when the primary parameter is q_eff. The cylindrical projection can be read directly from the Fourier coefficients: mean radius `G_0`, radial coefficient `G_j+G_−j`, tangential coefficient `G_j−G_−j`, and zero height, where `G_l=A_l/(1+m l)`. This avoids cancellation in a numerical quadrature of very small inlet harmonics.

## Pure core at q_eff=.08

`fixed_metric_mode3_tangent_core_projection.json` records:

- `b1=.2133333333333333`, exact curvature interval `[.36,1.64]`;
- phase support gap at `0` and `π/3`: `.1591822965720287`;
- coefficient l1 radius upper bound `1.0701896858630877`;
- M4 inlet metric l1 `8.95576e−8`, M6 `2.48280e−11`, M8 `1.21742e−14`;
- M8 second-jet projection error `2.66221e−13`.

The gap formula is `2|Σ_{l odd}G_l|`: at both material angles0 andπ/m, every sine in φ vanishes, the curve point is aligned with that normal by reflection symmetry, and strict convexity identifies the support point. For the pure core it equals `Σ_{k≥1,odd}12k J_k(b)/(9k²−1)`.

These statements apply to the pure core. Matching the prefix generally changes b2,b3,... . Already at q_eff=.001 the computed actual-linear-port prefix requires approximately `b2=10.887q_eff²`, `b3=66.22q_eff³`, `b4=476.6q_eff⁴`. The corrected core's spectrum, support gap, and curvature must therefore be checked separately; the pure-core table cannot certify it.

## Numerical chart fixing the profile breakpoints

The earlier design-coordinate `t=s/L(delta)` moves every ramp breakpoint when delta changes. Adaptive collocation can then retain clusters of obsolete breakpoints, and a C2 Hermite interpolant on extremely short intervals amplifies nodal roundoff. Frozen-profile remeshing removed the observed artificial Darboux spike. The support M4 collocation residual reached1.996e−9, but a normalized boundary target2e−10 demanded about2e−18 in its highest physical mode, below the observed1.58e−17 floor; its failure status is retained.

The new design chart fixes all ramp breakpoints without changing the physical metric. Let `P(delta)` be the physical prefix length, `B` the fixed bridge length, `P0=P(delta_reference)`, and `t0=P0/(P0+B)`. For `t≤t0`, set `s=P(delta)t/t0`. On the bridge, write `u=(t−t0)/(1−t0)`, `a=P(delta)/P0`, and

\[
s=P(\delta)+B\,[a u+(1-a)S(u)],\qquad
S(u)=10u^3-15u^4+6u^5.
\]

At t0 the first and second derivatives match the prefix chart. For `0<a<2`, the derivative is positive because `0≤S'≤15/8`. All prefix breaks now have fixed computational locations. The BVP solves `dy/dt=(ds/dt)F(s,y)`; checkpoints and every geometric audit return to the original physical arclength coordinate. In fixed-metric mode `a=1`, so this is precisely the ordinary global normalization. It is a numerical coordinate repair, not a change to g.

## A genuinely fixed-metric small-amplitude check

All rows below hold delta=.07252770232246168 and every other physical meridian/tail parameter fixed. The M4 designed profile is frozen before increasing M; the M8 BVP solves the extrinsic q_eff rather than changing delta. The first four genuine linear DN entries are kept unchanged, and m15..24 are supplied by the independent momentum propagation on the same p160 background.

| stage | q_eff | metric l1 | flow defect | full Darboux l1 | nodes |
|---|---:|---:|---:|---:|---:|
| fixed_metric_tangent_p160_chart_design_m4_summary.json | 0.01 | 2.056124e-07 | 6.013332e-07 | 1.708334e-05 | 559 |
| fixed_metric_tangent_p160_frozen_m8_summary.json | 0.00999877484804617 | 2.263519e-10 | 2.258476e-10 | 6.052658e-08 | 560 |
| fixed_metric_tangent_p160_frozen_m8_tight_summary.json | 0.0099986030961791 | 1.450552e-11 | 5.311259e-11 | 2.06976e-09 | 2915 |

All three rows report success. The final M8 collocation tolerance is2e-9 and its weighted boundary tolerance2e-9. This is a resolved finite-prefix diagnostic, not a closed-surface or nonlinear-tail result.

## High-amplitude branch and precision issues

M4 design continuation reached q_eff=.08 with collocation success, but actual metric l1=.00735062 and full Darboux l1=.95122. Its corrected angle coefficients b2=.0648357,b3=.0247844,b4=.0174629 invalidate any attempt to reuse the pure-core M4 precision table. The full results remain in fixed_metric_tangent_p160_chart_design_m4_summary.json.

M8 q_eff=.02 initially stagnated with ordinary local-frame arithmetic despite a tiny physical boundary residual. Repeating the same equations and physical parameters with long-double local evaluation converged at560 nodes: metric7.816e-9, full Darboux1.160e-6. This changes arithmetic only. It also keeps the physical C2 interpolant jets in the same precision before storing float64 coefficients. Higher-q rows are being recorded separately and must pass their own whole-angle/error audits.

The optional --physical-bc-tol CLI parameter gives a uniform physical slope-matching target independently of q^M scaling; both weighted and physical residuals are recorded when this option is used. It is intended to avoid imposing sub-roundoff targets on tiny high harmonics. It does not waive metric, full-equation, nonlinear mean-jet, or Cartesian seam checks.

## Completed M8 design continuation and macro error gate

The same original p160 physical linear tail is used; delta varies in these design rows. The fixed-profile table above is the convergence evidence, not this table. Extended local arithmetic removes the earlier small-amplitude Newton stagnation.

| q_eff | designed delta | metric l1 | full flow defect | full Darboux l1 | port height | solver success |
|---:|---:|---:|---:|---:|---:|:---:|
| 0.02 | 0.0725303434299 | 7.81582e-09 | 2.54241e-08 | 1.15957e-06 | 0.000320473 | True |
| 0.03 | 0.07253480396947 | 2.94453e-07 | 1.00762e-06 | 5.33386e-05 | 0.000482746 | True |
| 0.04 | 0.07254117304708 | 4.71113e-06 | 1.13248e-05 | 0.000721918 | 0.000647572 | True |
| 0.05 | 0.07254946011216 | 3.786e-05 | 7.35935e-05 | 0.00564791 | 0.000815997 | True |
| 0.06 | 0.07255832453447 | 0.000182089 | 0.000349585 | 0.0296708 | 0.000989277 | True |
| 0.07 | 0.0725387729743 | 0.00130199 | 0.00354685 | 0.446766 | 0.00116907 | True |
| 0.08 | 0.07248923501042 | 0.00273604 | 0.00300117 | 0.389728 | 0.00135729 | True |
| 0.0825 | 0.07240054561133 | 0.00443363 | 0.00805806 | 3.9918 | 0.00140616 | False |

At q_eff=.08, the corrected core alone has M8 inlet metric l1=0.002173278132762059 and second-jet projection error=0.031337550239560995. This supplies a direct angular-truncation diagnosis, independently of the radial mesh. Its exact chosen angle-core support gap is0.16952021084904506, with conservative curvature interval [0.4953575687769423,2.9174172830069613]. Those exact-core quantities do not certify the mismatched truncated prefix.

Per parent decision, the q_eff=.08 M8 metric is now frozen at its exact delta=.07248923501041592 for M12→M16 tests, with q_eff an extrinsic unknown. This delta lies below the linear planar-core critical delta=.0725268280429954; a large q change, collapse toward the round branch, or failure is possible and must be reported rather than hidden by metric retuning. Actual momentum DN modes27..48 are being computed on precisely the same old p160 background. No M32 job is authorized to run without memory coordination.

## 2026-11-09: bounded old-metric M12 macro refinement

The physical profile is frozen at the M8 q_eff=.08 design value delta=.07248923501041592, with the original p160, width .35, cap .02 physical tail linear port. M12 solves only the extrinsic amplitude and higher tangent-angle coefficients. It converged in 508 nodes / 102 s, but q_eff moved to .09137022405566571 and the whole-prefix errors remain unacceptable: metric polynomial l1 .00473015763, flow .00604322624, Darboux .862055924, sampled kappa 7.23318866. The physical port boundary residual is 4.67e-17; tightening that boundary condition does not address the angular defect. The inlet projected metric l1 alone is .00217798324. The exact corrected core has phase support gap lower bound .19829864691 and curvature upper bound 4.18259024291, but this does not establish the projected prefix or a closed surface.

The actual M8 q_eff=.08 corrected core also has a whole-angle omitted-coordinate l1 bound 3.7441491e-5, first-jet .00108848287, second-jet .03212632294; its projected-core metric polynomial l1 is .00217327813. These coefficient bounds use the actual matched core and analytic omitted Bessel tails, not the pure-core small-tail estimate. Floating convolution error is not interval enclosed. Details: fixed_metric_tangent_q008_projection_bounds.json and fixed_metric_tangent_projection_bounds.py.

One M16 bounded solve at this same old delta follows. If it does not resolve the branch, a new M16 fixed-q design will be treated explicitly as a new physical metric; it cannot be counted as old-metric convergence.

## Exact support-to-tangent Fourier identity (2026-11-09)

For the pure support core $h(\phi)=1+q_s\cos(3\phi)$, let $0\le q_s<1/8$, hence $0\le e=8q_s<1$, and use unit arclength $\theta=\phi-(e/3)\sin(3\phi)$. Its tangent angle has the exact Fourier expansion

$$\phi(\theta)=\theta+\sum_{j\ge1}b_j\sin(3j\theta),\qquad b_j={2J_j(je)\over3j}.$$

A direct derivation avoids assuming an inversion formula. Differentiate the sine series: the cosine coefficient of $\kappa=\partial_\theta\phi$ is $3j b_j$. Since $\kappa\,d\theta=d\phi$ and $\theta(\phi)=\phi-e\sin(3\phi)/3$, that coefficient equals

$$ {1\over\pi}\int_0^{2\pi}\cos(3j\phi-je\sin(3\phi))\,d\phi=2J_j(je). $$

The integrand has period $2\pi/3$, and the last equality is the defining real Bessel integral. Thus the primary tangent parameter used here is exactly

$$q_{\rm eff}={3b_1\over8}={J_1(8q_s)\over4}.$$

For example, support $q_s=.08$ (support gap $.16$) corresponds to $q_{\rm eff}=.07597331158723045$. Conversely $q_{\rm eff}=.08$ corresponds to $q_s=.0847828844128083$ (support gap $.1695657688256166$); the actual matched M8 gap $.16952021085$ is close, but proximity alone is not a proof of equality. The pure-support prediction for its $b_{16}$ is $.00018085816107051467$, explaining why initializing all new high tangent coefficients at zero is weak and why the matched core loses the short pure-$b_1$ spectrum. A $q_{\rm eff}=.076$ pure-support comparison has gap $.16006274751901872$ and $b_{16}=8.86346494\times10^{-5}$. Actual corrected-core support gap must still be measured independently.

This identity can supply numerical starting coefficients at new angular orders. It changes no physical metric and proves no BVP solvability. It does not justify treating the metric-design values of delta as a fixed-metric convergence sequence.
