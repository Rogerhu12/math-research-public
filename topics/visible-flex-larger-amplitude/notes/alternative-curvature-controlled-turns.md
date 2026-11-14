# A pointwise curvature budget for a radial-metric turn

Status: the algebraic proposition below is proved. Numerical values are
sampled diagnostics of finite maps, not a global curvature or reach proof.
The turn profiles are exact definitions of metrics; their definition does
not prove the existence of the desired closed embeddings.

## Exact proposition

Let a C² isometric immersion have metric
`ds² + a(s)² du²`, with `a > 0`. In the orthonormal basis
`(∂s, a⁻¹∂u)`, write its second fundamental form as

\[
 S=\begin{pmatrix}L&M\\M&N\end{pmatrix}.
\]

Choose a normal and a cross-section on which `0 < N < B`, where `B` is a
proposed upper bound for both absolute principal curvatures. At each point,
the condition `‖S‖op ≤ B` is equivalent to

\[
 aB\left(\frac{M^2}{B-N}-N\right)
 \leq a'' \leq
 aB\left(\frac{M^2}{B+N}+N\right). \tag{1}
\]

Consequently, one scalar acceleration can satisfy the bound on the entire
cross-section exactly when the maximum of the left side is at most the
minimum of the right side. This is an instantaneous condition: the
quantities `M,N` change as the immersion evolves, so checking (1) only at
the start of a turn does not bound its continuation.

### Proof

The Gauss equation and the Gaussian curvature of the specified metric give

\[
 LN-M^2=-\frac{a''}{a},\qquad
 L=\frac{M^2-a''/a}{N}. \tag{2}
\]

Since `B±N > 0`, the Schur complements of the lower right entries show

\[
 -BI\preceq S\preceq BI
 \iff
 -B+\frac{M^2}{B+N}\leq L
 \leq B-\frac{M^2}{B-N}.
\]

Substitute (2), multiply by `N > 0`, and solve the two inequalities for
`a''`. This gives (1). Intersecting the pointwise intervals proves the
cross-section statement. No assumption about principal directions is used.

The interval at one point is nonempty if and only if
`M² + N² ≤ B²`. For a flat strip (`a''=0`), the nonzero principal curvature
is `N + M²/N`; thus a strictly smaller flat-strip curvature supplies a
nonempty interval around zero.

## A C² outward-to-inward metric transition

Given an entry `a0 > 0`, slope `v0`, zero acceleration, an exit slope `v1`,
and a length `T > 0`, put `u=s/T` and define

\[
\begin{aligned}
 a(s)&=a_0+T\{v_0u+(v_1-v_0)(u^3-u^4/2)\},\\
 a'(s)&=v_0+(v_1-v_0)(3u^2-2u^3),\\
 a''(s)&=\frac{6(v_1-v_0)}T u(1-u),\qquad 0\leq u\leq1.
\end{aligned}
\]

These jets match constant-slope metrics on both sides. The slope stays
between `v0` and `v1`, the endpoint radius is `a0+T(v0+v1)/2`, and the peak
absolute acceleration is `3|v1-v0|/(2T)`. Positivity of `a` still has to be
checked for the proposed parameters.

For example, `v0=.35`, `v1=−.6`, `T=.4` gives peak acceleration `−3.5625`.
Its peak radius before the slope becomes negative exceeds its entry radius
by only `.0365794702` (the maximum is obtained at the unique zero of
the monotone slope). This provides a concrete inward-turn candidate; it is
not an isometric embedding construction by itself.

## Actual entry diagnostics

The script `computations/alternative-flat-continuation.py` computes (1)
with the angular and mixed derivatives of the nonprojected R71 ruled map.
It retains the finite entry defects and measures the actual first
fundamental form. The numerical use of (2) as a *design* interval does not
replace the actual computed second fundamental form of the finite map.

| Entry | a | a′ | N range | max abs(M) | interval for a″ with B=8 |
|---|---:|---:|---:|---:|---:|
| fast `.35/.45`, then flat `.1` | 1.14 | .35 | [.4759676, 5.2540402] | .5172612 | [−4.0275274, 4.6186369] |
| slow `.5/1`, coast to `.9`, then flat `.15` | 1.2692 | .464 | [.4478283, 2.1699475] | .6598050 | [−4.2689048, 4.7924775] |

The corresponding reports are
`notes/alternative-flat-fast035-m96-turn-budget.json` and
`notes/alternative-flat-slow128-turn-budget.json`. These intervals show
that a short inward turn is not excluded by its entry curvature. They do
not certify an entire turn, reach, closure, or phase-family displacement.

## Outward start with a controlled initial acceleration

For `0 ≤ k0 S ≤ 3V`, define `b=k0 S` and, for `u=s/S`,

\[
\begin{aligned}
 v(u)&=bu+(3V-2b)u^2+(b-2V)u^3,\\
 a(s)&=1+S\{bu^2/2+(3V-2b)u^3/3+(b-2V)u^4/4\}.
\end{aligned}
\]

Then `a′=v`, the initial jets are `(1,0,k0)`, and the terminal jets are
`(1+SV/2+k0 S²/12,V,0)`. Indeed

\[
 a''(s)=S^{-1}(1-u)\{b+(6V-3b)u\}\geq0.
\]

Thus it joins C² to a constant-slope strip. Unlike a fixed fast-start
shape, `k0` can be chosen independently of the terminal speed and length.
This is useful because the exact core witness has an initial acceleration
constraint; the geometric agent's exclusion-ball calculation must still
be checked over the complete strip.

`computations/alternative-controlled-profile.py` implements both formulas
and stores complete finite Fourier states, source and parameter hashes,
actual metric/curvature samples, and the distance from every sampled
latitude to the rotated major-core witness. Its radial-law metadata can
reconstruct either profile without reading a live external source tree.
