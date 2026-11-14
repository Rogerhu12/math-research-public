# R106 supplement: complete finite part below 8822 using the actual real flow

The exact root finite-part identity, actual affine step5 family, original
fixed physical cut and all seven-field/source errors are those in
[the actual root finite-part proof](R106-supplement-actual-root-finite-part.md).
The following refinement replaces the uniform-field Cauchy bound for the flow
by the complete finite derivative plus a Cauchy bound only for its true error.
It also uses realness to control the imaginary image. No root term or mean is
removed.

For the same whole parameter interval and physical root-label strip
\(|\Im\eta|\le1/900\), the executed result is

\[
 \boxed{\ |h_\sigma^{\rm root}(\eta,p)|<8822,\qquad
          |J(s,\eta,p)|<1.009.\ }                              \tag{1}
\]

It holds on the whole actual interval \(0\le s\le c(p)\), for both inward signs
and both physical roots, before pullback by a global root label.

## 1. The derivative estimate

Let \(\widehat q,\widehat k\) be the complete finite Fourier/Taylor
polynomials in the SHA-bound seven-field report, with true errors
\(e_q,e_k\) on \(|\rho|\le R=7/25000,\ |\Im\theta|\le S_{\rm in}=1/400\).
Use \(r=c_{\max}^2<R\) and \(S=1/800\).
For the exact scaled coefficients

\[
 \widehat f(\rho,\theta)=\sum_{n=0}^{64}
 \sum_{|j|\le450}f_{nj}(\rho/\mathrm{scale})^n e^{4ij\theta}
\]

define

\[
 L_f=\sum_{n,j}4|j|\,|f_{nj}|
       (r/\mathrm{scale})^n e^{4|j|S}
      +\frac{e_f}{S_{\rm in}-S}.
                                                               \tag{2}
\]

The finite sum keeps every input coefficient. The error is holomorphic on
the larger paid bidisk, so Cauchy proves
\(|\partial_\theta f|\le L_f\) on the smaller bidisk.
The native Arb run gives

| Bound | Finite contribution | True error contribution | Complete bound |
| --- | ---: | ---: | ---: |
| \(L_q\) | \(29.740460772532\) | \(0.307606621552\) | \(30.048067394083\) |
| \(L_k\) | \(515.531013230657\) | \(8.700777836539\) | \(524.231791067196\) |

All displayed values in this table are rounded outward; full endpoint balls
are retained in the report.

For the actual vector field

\[
 v_\sigma(s,\theta)=2s q(s^2,\theta)-2\sigma s^2k_*(s^2,\theta)
\]

this gives the integrated Lipschitz bound

\[
 \Gamma=c_{\max}^2L_q+\frac23c_{\max}^3L_k
 <0.008669166146589,\qquad
 e^\Gamma<1.008706852190901.                                  \tag{3}
\]

## 2. Whole-time imaginary image and Jacobian

For real \(p,s,\theta\), the exact fields \(q,k_*\) are real. On any
solution \(\Theta=u+iy\) before its first exit from \(|\Im\theta|<S\),
the vertical segment from \(u\) to \(u+iy\) lies in that strip, and

\[
 |\Im v_\sigma(s,u+iy)|
 \le |y|\sup_{|\Im\theta|\le S}|\partial_\theta v_\sigma(s,\theta)|.
\]

Gronwall therefore gives

\[
 |\Im\Theta(s,\eta)|\le |\Im\eta|e^\Gamma
 \le\frac{e^\Gamma}{900}
 <0.001120785391324<\frac1{800}.                               \tag{4}
\]

The strict inequality excludes a first exit. Analytic local existence and
bounded periodic velocity then continue the actual flow to \(c(p)\).
Its label derivative solves \(J_s=(\partial_\theta v_\sigma)\circ\Theta\,J\),
\(J(0)=1\), so \(|J|\le e^\Gamma\).
The same argument applies to the full closed label strip by taking a slightly
larger initial strip within the strict margin in (4). Thus the resulting
coefficient is holomorphic on a neighborhood of the claimed closed strip.

This is a direct estimate for the actual nonlinear flow. It uses neither a
finite saved characteristic nor a finite grid in time.

## 3. Complete phase budget

The image in (4) lies in the original \(1/800\) source strip. Consequently
the original completed regularized-source report can be consumed without
enlarging its true error domain. Its finite expression moduli and complete
errors give

\[
\begin{aligned}
 M_H&<2059.360847610260,\\
 M_C&<8712.952117393824,\\
 M_Z&<0.369842735623359 .
\end{aligned}
\]

Finite expression moduli enclose the complete finite products before the new
dyadic coefficient choice; the saved complete errors also include every
choice/arithmetic fee, so their sum is a valid (possibly redundant) true
modulus. Every angular mean and every output product mode remains included.

Using the exact finite-part identity

\[
 h_\sigma^{\rm root}
 =J_c C_\sigma(c,\Theta_c)
  +\int_0^c H_\sigma(s,\Theta_s)J_s\,ds+Z_\sigma(\eta)
\]

and the unrounded saved upper bounds gives

\[
 |h_\sigma^{\rm root}|
 \le e^\Gamma(M_C+c_{\max}M_H)+M_Z
 \le8821.642062364719<8822 .
\]

The sign and negative-root conversions are exactly those in the preceding
root finite-part proof. A complete global root map still contributes its
actual pullback Jacobian. This result does not identify the R104 full-return
coefficient or prove a strong PDE remainder.

## 4. Executed certificate

The new source is
[fourfold_subprincipal_root_flow_sharp.py](../scripts/fourfold_subprincipal_root_flow_sharp.py).
Its report is

    notes/2026-11-13-R106-actual-complete-root-phase-sharp-flow.json

SHA256:

    3a65b34d78c21753f9d65aa7e7b48742ee74e5b4d5d592d261b86567997016aa

The report binds the exact parameter and root, full input/source hashes,
all actual field moduli, the whole-flow bootstrap, and the complete phase
budget. The seven-field loader checks all coefficient shards and the true
outer certificates. The regularized source report is consumed for its
completed moduli, which are reproduced by the already recorded source
producer; this consumer does not need its large intermediate source shards.

Executed from the topic directory:

~~~bash
python3 scripts/fourfold_subprincipal_root_flow_sharp.py \
  data/R106/root_regularized_native_degree64_plus/report.json \
  --out notes/2026-11-13-R106-actual-complete-root-phase-sharp-flow.json
~~~

The actual native run used python-flint \(0.9.0\), \(256\)-bit Arb arithmetic
and took about \(6.4\) seconds. The source refuses to overwrite a saved report.
