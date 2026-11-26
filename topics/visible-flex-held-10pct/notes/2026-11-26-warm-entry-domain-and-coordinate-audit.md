# Warm entry: auxiliary domain, actual scale chain, and radial coordinates

Date: 2026-11-26. Session: Astra-held10-06bbeb39-20261126 / fixed_metric.

This records newly found implementation facts, not a new surface or a
successful warm BVP. The restored original M24 run passed its original finite
gates. The first actual same-lambda warm attempt ended with
`OverflowError('math range error')` before a raw solver return; its caller
reported run SHA
`0636aa7be3fbaec8f2f86e7774decb9cc4f444c2218769e26e897d8037ca440a`.
The traceback was not yet available to this review. The source below proves
one uncaught-overflow path; it does not by itself prove that it was the
observed traceback's exact location, or that removing it yields convergence.

## 1. An impossible trial can escape the original rejection loop

The actual `WarpedBVP.initial` first evaluates

```python
q = self.seed_support_amplitude * math.exp(float(p[0]))
```

and only afterwards checks `1e-7 < q < .124`. The inherited fixed metric
flow is independent of `p[0]`; the value `q` is the new auxiliary coordinate
carrier, not the gauge multiplying the physical field. The original domain
Newton catches `FloatingPointError` inside its trial/backtracking loop, but
does not catch `OverflowError`. Hence a finite trial with a sufficiently
large positive `p[0]` can terminate the solver before the old domain gate
is reached. This is an implementation domain exception, not evidence that
the physical boundary problem has no solution.

For the current gauge `.06` and phase scale `1`, the inherited open carrier
domain is exactly equivalent in real arithmetic to

\[
 -13.304684934198283\ldots < p_0 < 0.7259370033829363\ldots.
\]

It therefore imposes a non-symmetric bound on the first phase control.
It is not a support-amplitude bound on the new core and is not a condition
on the intrinsic metric. The default phase scale in the actual entry is
`1.0`, not a small factor.

The independent optional adapter `warm_auxiliary_domain_guard.py` first
rejects parameters outside the logarithmic interval enlarged by one on
both ends. On that enlarged interval the exponential is finite, and the
unchanged original post-exponential test still decides all points near
the true boundary. The padding avoids deciding the true boundary with a
rounded logarithm. Thus every valid original value and its derivatives are
unchanged, and invalid distant trials use an exception type already handled
by the original Newton algorithm. No field or geometric guard is removed.
Importing the adapter does not install it.

An actual tiny synthetic check verified exact equality at four valid values
and `FloatingPointError` rejection at `p0 = -1000, 1000, NaN, Inf`. This
checks the adapter only; no real BVP was run for this note.

## 2. The recorded phase parameter formula is not the current implementation

The actual warped BVP sets

\[
 s_j=\max(q^j,10^{-9}),\qquad j=2,\ldots,M,
\]

whereas the deployed provider divides its incoming legacy coefficients by

\[
 \widetilde s_j=\max(q^j,10^{-10}).
\]

Its true physical phase parameters are consequently

\[
 d_1=\sigma p_0,\qquad
 d_j=\sigma\frac{s_j}{\widetilde s_j}p_{j-1},\quad j\ge2,
\]

not the recorded formula `d_j = phase_scale * p_(j-1)` for all `j`.
At `q=.06`, the ratio is `1` through `j=7`,
`5.953741807651275...` at `j=8`, and `10` for `j>=9`.
The zero-control complete core remains exactly the anchor, because every
one of these controls is then zero. The multiplier for each fixed index
does not depend on the truncation `M`; this is a scale-contract error, not
evidence that enlarging `M` changes the intrinsic metric.

The analytic Jacobian chain is nevertheless consistent with the actual
implemented map. The provider returns derivatives with factors

\[
 \operatorname{diag}\left(\sigma/q_{aux},
                    \sigma/\widetilde s_2,\ldots\right),
\]

while the original inlet Jacobian and analytic exact-lift Jacobian multiply
by `diag(q_aux, s_2, ...)`. Their product is exactly the true diagonal
`diag(sigma, sigma*s_j/tilde_s_j)` above. A different finite-difference
failure could still exist, but this mismatch is not a missing chain-rule
factor. A future corrected entry must either explicitly record and retain
these true scale factors, or use the actual BVP scale array in the provider
and bind the changed provider version. No accepted warm field existed at
the time of this discovery.

## 3. Freezing the metric also changed the numerical radial chart

`SupportBVP.__init__` derives `chart_reference_prefix` and `chart_join` from
the constructor's reference profile. The original design BVP constructs
this chart at the reference delta and evaluates it at its returned delta.
The new `fixed=True` constructor uses the returned delta as its reference,
so the default new radial chart is generally different. On the short
bridge the old chart includes a nonlinear smooth scaling; the new frozen
constructor has the scale ratio equal to one.

The transferred physical quintic remains an initial guess for the new
collocation grid. An original raw cubic solution composed with a nonlinear
change of independent variable need not remain a cubic on the new grid.
Adding chart breakpoints also changes the finite collocation problem.
Therefore zero-control equality of complete core geometry does not alone
make the remeshed raw array an accepted finite collocation solution.

Conversely, freezing the original `chart_join` and
`chart_reference_prefix` retains exactly the original numerical radial
coordinate. At the same `M`, angular projection, actual profile, gauge,
full core, and exact-lift projection, the original raw grid can be checked
directly. This coordinate choice does not change the physical metric.

`warm_handoff_equivalence_probe.py` binds the accepted original run/raw,
the actual prepared same-lambda warm run, numerical sources, provider,
physical interpolant, and original parameter scales. It does not invoke a
BVP solver or label its output accepted. It evaluates:

1. Original raw collocation residual, actual original RMS formula and BC.
2. The same node values under the deployed new radial chart.
3. The same raw grid after freezing the original radial chart.
4. Complete core equality, physical mean1168 two-jet comparisons, and
   selected actual analytic Jacobian columns against finite differences.

The position difference is evaluated before adding a common literal
vertical primitive, while both mean derivatives are evaluated independently.
No primitive is resampled or silently given a new acceptance label. The
entry had passed syntax/CLI checks but had not returned actual-run results
when this note was written.

Higher-mode handoff is distinct: retaining the entire geometric lift while
adding zero field coefficients does not make the newly projected equations
vanish. A large new-mode residual is not by itself a geometric handoff
failure or a same-metric contradiction.

## 4. A separate design family if the frozen-delta branch is unsuitable

Using the supported-phase provider with the original `fixed=False`
constructor gives another precise finite problem: `p0` controls delta,
the positive carrier is the unchanged gauge so `d1=0`, and the remaining
`M-1` variables control `d2,...,dM`. There are still `M` unknown parameters
for the `M` terminal equations. At the actual anchor, zero new controls and
the original returned delta retain the complete core and metric. At
lambda one all new controls vanish on the protected arc, so the exact arc
condition is preserved for this new design family as well.

This would be delta/lambda **design**, with a changing intrinsic metric;
it is not a fixed-metric refinement and does not inherit the current
fixed-metric label. Only after an actual accepted lambda-one candidate may
one freeze its delta and lambda, enable the full phase unknown space, and
test refinement of that single full problem. This paragraph is an algebraic
interface evaluation only, not an executed alternate branch.

## Source identity checked for this review

| Source | SHA-256 |
|---|---|
| Original `950f-prefix-warped-bvp.py` | `eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70` |
| Original `fixed_metric_mode3_bvp.py` | `e2e5cf08339c82fac24ef296dc721cec4e43852d2a6d963721ce69a1d8d7a11c` |
| Original `f6curve_domain_newton.py` | `6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654` |
| Deployed `warm_supported_core_factory.py` | `9192499334d9f8603c812cd95964cc660a065132a82ce240fe2331f64c9b14dc` |
| `round_raw_lib/analytic_adaptive_core_jac.py` | `da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431` |

The original source files were read from the restored public source tree.
The real-run probe independently checks its runner's source bindings; these
local hashes must not substitute for that runtime verification.

## Actual subsequent probe

The same-runner probe subsequently completed with exit 0. On the frozen original radial chart, f, fm, collocation residual, both boundary residuals and the complete RMS vector were bitwise identical. The original maximum RMS was 9.927150345213775e-7 at 631 nodes. The core jets, inlet projection, and the six inspected physical-map jets were also bitwise identical. This is actual finite verification, not a new solve or continuous error certificate.

Across columns 0,1,6,7,8,23 at two centered step sizes, the largest observed RHS derivative difference was 3.2192494079679086e-8; the BC difference was 1.6970799765481104e-10. Smaller steps increased cancellation error in these checks; no missing chain factor was detected. The complete small projected evidence and its scope are in [the actual execution record](2026-11-26-warm-handoff-equivalence-execution.json).
