# R110 supplement: complete periodic-kernel bounds for the tame remainder

2026-11-13, reproduce-newton.

**Status.** The inequalities in this note are proved for the full periodic
operators, including the zero mode. The companion BigInt calculation verifies
the displayed rational constants. A new actual-field consumer has been written
but has not run: the native executor is unavailable. No new numerical
strict-core growth rate or full inverse is asserted.

The purpose is specific. The complete Fourier sums in the earlier
[R110 tame supplement](R110-tame-half-derivative-triangular-propagation.md)
are sufficient bounds, but can lose cancellation between angular modes.
Here their signed remainder and zero-order commutators can also be bounded
from genuine closed-angle derivative bounds. The executable takes the minimum
of two independently complete bounds. It does not subtract a presumed Fourier
tail, discard modes, or replace a complete field by its finite polynomial.

## 1. Physical derivative and the retained mean

The physical angle has period $L=\pi/2$. Use normalized angular $L^2$ and
$$
 D=\partial_\theta,\qquad
 J e^{4ik\theta}=\max(1,|4k|)^{1/2}e^{4ik\theta}.
$$
Let $P_0$ be the exact mean projection and
$J_0=|D|^{1/2}$, with zero eigenvalue on constants. Since every nonzero
physical frequency has modulus at least four,
$$
 J=J_0+P_0.                                                   \tag{K.1}
$$
The mean correction below is essential. Replacing $J$ by $J_0$ would
change the actual state norm and remove a retained input.

The statements also apply to complex coefficients with bounded derivatives.
All actual coefficients on the real radial/parameter domain are real.
For a scalar periodic coefficient $a$ choose any one constant $a_c$, and set
$$
 O=\|a-a_c\|_\infty,\qquad L_1=\|Da\|_\infty,\qquad
 L_2=\|D^2a\|_\infty.                                         \tag{K.2}
$$
These are bounds on the entire circle and the complete radial/parameter
piece, not maxima over uncharged nodes. The constant $a_c$ need not equal
the actual Fourier mean.

## 2. Exact kernel and the zero-order commutator

For a smooth periodic function, regarded as its periodic extension to the
real line,
$$
 J_0 f(x)=c_{1/2}\int_{\mathbb R}
       \frac{f(x)-f(x-z)}{|z|^{3/2}}\,dz,\qquad
 c_{1/2}=\frac1{2\sqrt{2\pi}}.                                \tag{K.3}
$$
The Fourier multiplier is $|\xi|^{1/2}$: the odd part vanishes and
$\int_0^\infty(1-\cos z)z^{-3/2}dz=\sqrt{2\pi}$.
The latter follows by integration by parts and the Abel limit of
$\int_0^\infty e^{-\epsilon z}\sin(z)z^{-1/2}dz$.
Thus (K.3) holds for every physical frequency $4k$, with no angular
normalization factor left over.

Taking the commutator cancels the diagonal term:
$$
 [J_0,a]f(x)=c_{1/2}\int_{\mathbb R}
       \frac{a(x)-a(x-z)}{|z|^{3/2}}f(x-z)\,dz.               \tag{K.4}
$$
Translations are isometries on normalized periodic $L^2$. Since
$$
 |a(x)-a(x-z)|\le\min(L_1|z|,2O),
$$
Minkowski's inequality, split at any $R>0$, gives
$$
 \|[J_0,a]\|_{2\to2}
 \le c_{1/2}(4L_1\sqrt R+8O/\sqrt R).
$$
For $O,L_1>0$, take $R=2O/L_1$. The zero cases follow by continuity:
$$
 \|[J_0,a]\|_{2\to2}\le\frac4{\sqrt\pi}\sqrt{O L_1}.          \tag{K.5}
$$

Write $a_\perp=a-\langle a\rangle$.
The operator $[P_0,a]$ only exchanges the mean and its orthogonal
complement. Its two off-diagonal blocks have equal norm
$\|a_\perp\|_2$; their source and target spaces are orthogonal. Consequently
$$
 \|[P_0,a]\|_{2\to2}=\|a_\perp\|_2\le O.
$$
This remains valid for complex $a$: the scalar functional has representing
vector $\overline{a_\perp}$ and the other block has vector $-a_\perp$.

Combining with (K.1) proves the full-mean estimate
$$
 \boxed{\quad
 \|[J,a]\|_{2\to2}
 \le O+\frac4{\sqrt\pi}\sqrt{O L_1}
 < O+\frac{113}{50}\sqrt{O L_1}.
 \quad}                                                       \tag{K.6}
$$
The last strict coefficient inequality may be used as a non-strict
operator upper bound, including zero derivative cases.

## 3. The signed half-order remainder

The earlier supplement keeps the principal term $(Da)J/2$ in the true
energy matrix. Its remaining operator is
$$
 R_a=D[J,a]-\frac12(Da)J.                                     \tag{K.7}
$$
Put $F=DJ_0$. Integration by parts in (K.3), with both near-zero and
infinite boundary terms paid, gives
$$
 Ff(x)=\frac32 c_{1/2}\int_{\mathbb R}
  \frac{f(x-z)-f(x)+zDf(x)}{|z|^{5/2}}\operatorname{sgn}(z)\,dz.
                                                                  \tag{K.8}
$$
Near zero the numerator is $O(z^2)$; at infinity it is $O(1+|z|)$.
Both portions are absolutely integrable for smooth periodic $f$.
Subtracting the exact linear coefficient term yields
$$
 [F,a]f-\frac32(Da)J_0f
 =\frac32c_{1/2}\int_{\mathbb R}
   \frac{a(x-z)-a(x)+zDa(x)}{|z|^{5/2}}
                   \operatorname{sgn}(z)f(x-z)\,dz .        \tag{K.9}
$$
The left side equals $D[J_0,a]-(Da)J_0/2$.

Taylor's theorem and the global first-derivative bound give, respectively,
$$
 |a(x-z)-a(x)+zDa(x)|
 \le \frac12L_2|z|^2,\qquad
 |a(x-z)-a(x)+zDa(x)|\le2L_1|z|.
$$
Apply Minkowski again and split at $R>0$. The resulting operator norm is
at most
$$
 \frac32c_{1/2}(2L_2\sqrt R+8L_1/\sqrt R).
$$
For positive derivative bounds its minimum occurs at $R=4L_1/L_2$,
and the limiting cases follow directly:
$$
 \left\|D[J_0,a]-\frac12(Da)J_0\right\|_{2\to2}
 \le\frac6{\sqrt{2\pi}}\sqrt{L_1L_2}.                         \tag{K.10}
$$

The zero-mode correction is exact, rather than a convention:
$$
 D[P_0,a]-\frac12(Da)P_0=-\frac32(Da)P_0 .
$$
Its norm is $(3/2)\|Da\|_2\le(3/2)L_1$. Hence
$$
 \boxed{\quad
 \|R_a\|_{2\to2}
 \le\frac6{\sqrt{2\pi}}\sqrt{L_1L_2}+\frac32L_1
 <\frac{12}{5}\sqrt{L_1L_2}+\frac32L_1.
 \quad}                                                       \tag{K.11}
$$
No frequency cutoff occurs. The zero-order and remainder estimates extend
from smooth inputs by density to bounded operators on the stated $L^2$
space. The coefficient assumptions are just the displayed periodic
$C^1$ or $C^2$ bounds.

## 4. Insert into the existing two-level energy

All definitions, exact signed principal matrix, weak-source norm and
physical parameter family are those in the existing R110 supplement.
For each $a\in\{\alpha,v,\gamma\}$ take
$$
 A_{\rm new}(a)=\min(A_{\rm Fourier}(a),\,O_a+
                       4\sqrt{O_aL_{1,a}}/\sqrt\pi),
$$
$$
 R_{\rm new}(a)=\min(R_{\rm Fourier}(a),\,
          6\sqrt{L_{1,a}L_{2,a}}/\sqrt{2\pi}+3L_{1,a}/2).
 \tag{K.12}
$$
Here the Fourier entries include their full true infinite complements.
Both arguments of each minimum are valid bounds for the same full
operator. No unidentifiable noise is removed from an old budget.

The complete potential is $d=\tau+D\sigma$. It needs only (K.6), for which
$$
 Dd=D\tau+D^2\sigma
$$
is already in the nine-field angular budget. Take its true closed-angle
range and derivative bound and minimize its complete old $A(d)$ with
(K.6). No positive sign for $d$ is assumed; the actual waist values
change sign.

The unchanged true base-to-half energy matrix is
$$
 \begin{pmatrix}
 0&\sqrt{\lambda_+/\gamma_-}A_{\rm new}(v)
   &\sqrt{\lambda_+/\alpha_-}A_{\rm new}(\alpha)\\
 0&\sqrt{\gamma_+/\gamma_-}R_{\rm new}(v)
   &\sqrt{\gamma_+/\alpha_-}R_{\rm new}(\alpha)\\
 \sqrt{\alpha_+/\lambda_-}A_{\rm new}(d)
   &\sqrt{\alpha_+/\gamma_-}R_{\rm new}(\gamma)
   &\sqrt{\alpha_+/\alpha_-}R_{\rm new}(v)
 \end{pmatrix}.                                               \tag{K.13}
$$
Its norm is still paid only as lower-to-higher forcing. The signed
principal high-energy rates are not changed. Ordered radial composition,
the actual radial $L^2$ source integration, physical mean and regular
port conventions are also unchanged.

This theorem is confined to declared closed strictly negative pieces,
where $\alpha,\gamma,\lambda>0$ have actually been proved. It does not
authorize applying hyperbolic energy across the positive collars inside
the finite quarter-core.

## 5. Obtain genuine closed-angle second derivatives without new primitives

The new source is
[scripts/fourfold_phase_strict_core_kernel_tame_energy.py](../scripts/fourfold_phase_strict_core_kernel_tame_energy.py).
It consumes the same completed old R110 energy report and its same full
nine-field polynomial. It verifies the original producer, dependency,
array, complete-family and radial-domain identities.

The old evaluator already covers the whole radial interval, every
closed angular cell, and the complete errors of the value and first
angular derivative. For a complete second-derivative bound it uses
the following additional finite step:

1. Evaluate the entire finite $\theta^2$ polynomial on an even angular
   grid with $N>2K$. Its finite DFT has no angular alias.
2. Bound the finite angular interpolation gap by
   $h_\theta\sum_k|4k|^3|\widehat P_k|$, using every retained mode.
3. Add the already proved **complete** true $\theta^2$ polynomial error
   uniformly on the cell.

This is a bound for the full true second derivative on the closed cell.
It does not need or assert a third-derivative estimate for the infinite
remainder. The finite third derivative bounds only the finite polynomial.
All radial coefficients remain interval balls across the entire input
radial piece and whole parameter interval.

The chosen $a_c$ is an actual binary64 constant selected near the
midrange. Its full deviation from every true cell is bounded again.
It is never described as the exact mean. The potential derivative uses
the complete $\tau_\theta+\sigma_{\theta\theta}$ cells.

Cross-zero Arb values are multiplied bilinearly; no square of a
cross-zero real interval is used in the new formulas. The old complete
Fourier and source budgets remain present in the output together with
the new independent kernel bounds and the selected minima.

After the missing original full nine-field/energy outputs have been
restored or rerun:
~~~sh
python scripts/fourfold_phase_strict_core_kernel_tame_energy.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --method signed --bits 256 \
  --out notes/strict_core_kernel_tame_signed.json
~~~

The new native consumer has not run. In particular, the observed old
commutator value about $4508.91$ is not replaced by an invented new
constant. The only newly executed computation is the exact finite
rational verification of the two universal coefficients in (K.6) and
(K.11), saved separately. Continuous core propagation, strong residual
Gram, full feedback inverse and nonlinear convergence remain distinct
outstanding calculations.

## 6. Exact finite verification of the universal constants

The source
[scripts/fourfold_fractional_kernel_budget_exact.mjs](../scripts/fourfold_fractional_kernel_budget_exact.mjs)
uses Machin's identity
$$
 \pi=16\arctan(1/5)-4\arctan(1/239).
$$
For the lower bound it takes eight terms of the first alternating series
and one of the second; for the upper bound it takes nine and two.
Alternating-series remainders supply the directions. Tangent addition and
the indicated positive angle ranges prove Machin's identity itself.
Six exact integer-cross-multiplication gates then prove
$\pi>25/8$, $\pi<22/7$, $4/\sqrt\pi<113/50$ and
$6/\sqrt{2\pi}<12/5$.

The identical pure BigInt function has actually executed in V8.
Its complete output is
[notes/2026-11-13-R110-fractional-kernel-constants.json](../notes/2026-11-13-R110-fractional-kernel-constants.json).
This verifies universal coefficients only. It is not a substitute for
the unrun actual-field consumer or its missing complete radial inputs.
