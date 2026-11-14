# Exact finite-time Grams for the same five-input core source

Date: 2026-11-13.

## 1. Reused actual object and reference

The new entry
[scripts/fourfold_phase_core_even_weak_residual_exact.py](../scripts/fourfold_phase_core_even_weak_residual_exact.py)
uses the existing ExactEvenCoreReference without changing its mathematical definition. It reuses all 175 proved positive-half leaf inputs on the same whole $\eta=10^{-9}$ affine family. Their cosine compression retains both Cauchy channels.

The five inputs are the normalized paired physical heights
$$
(w_-,w_+)=(Q_{\cos}v,Q_{\cos}v)/\sqrt2.
$$
The mean cosine is retained. The paired regular coordinate is a separate sixth coordinate with zero direct core reference column; it is not deleted from the full cap or low system.

The exact reference is continuous at every radial join. On each leaf it uses
$$
R_i(u)=Z_i(u)Z_i(-1)^{-1}
 +\frac{u+1}{2}\big(T_i^{\cos}-Z_i(1)Z_i(-1)^{-1}\big),
$$
followed by the ordered exact prefix and the waist map $(A^{-1},0)/\sqrt2$.
The actual saved algebraic cosine compression is not replaced by a rounded new local transfer. The returned momentum is the physical raw $p$, with the existing scale eight restored exactly.

The new source accepts any of the complete actual five-field, seven-field, or nine-field producers, with the exact expected field order and producer/dependency hashes. For the nine-field package it uses the original first five fields and their complete errors; it also retains the existing $\alpha,v$ multiplier records for later source wiring. There is no second geometric sampling pass.

## 2. Unchanged scalar and divergence residuals

For each complete Fourier coefficient polynomial the source forms
$$
\begin{aligned}
R_r&=a w_r+bw_\theta-p_N,\\
R_\theta&=P_H(bw_r+cw_\theta+\sigma w),\\
R_0&=\sigma w_\theta-\tau w-p_{N,r}
       -D P_N(bw_r+cw_\theta+\sigma w).
\end{aligned}                                                   \tag{1}
$$
Thus
$$
\mathcal P w=-R_0+\partial_rR_r+D R_\theta,
\qquad p_{\rm shifted}=p_N.
$$
The full angular range of every finite coefficient/reference product is retained. The code never treats a retained-row cutoff as the complete residual or silently promotes a negative Sobolev norm to a positive one.

For the explicitly invariant object and reference, the exact radial parities are
$$
R_r(-r,\theta)=-R_r(r,\theta),\qquad
R_\theta(-r,\theta)=R_\theta(r,\theta),\qquad
R_0(-r,\theta)=R_0(r,\theta).
$$
Consequently the true source Gram on a positive interval and its reflected negative interval is twice the one-side Gram for these same normalized paired inputs. This is an integration identity, not a change of the $1/\sqrt2$ input normalization. The angularly odd divergence component $R_\theta$ is still needed.

## 3. Exact integration of the finite time polynomial

Let one Fourier output row of a finite residual be
$$
\widehat r_k(u)=\sum_{j=0}^D c_{k,j}u^j,\qquad -1\le u\le1,
$$
where each $c_{k,j}$ is a row acting on the same five input columns. For physical $r=c+hu$, its finite $L^2(dr;H^s)$ input Gram is
$$
\widehat G_s=
 h\sum_k \max(1,|4k|)^{2s}
       \sum_{i,j=0}^D
       \mu_{i+j}\,c_{k,i}^*c_{k,j},\qquad
\mu_q=
\begin{cases}
2/(q+1),&q\ \text{even},\\
0,&q\ \text{odd}.
\end{cases}                                                   \tag{2}
$$
This identity retains every finite time cross term. It is positive semidefinite because it is the integral of the actual finite squared norm. It is not obtained from positivity of individually selected floating matrix entries.

The new implementation forms, for each upper-triangular input pair, the full acb_poly product of the coefficientwise-conjugated first residual polynomial and the second polynomial. It integrates every even coefficient through degree $2D$ using the exact moments in (2), then sets the lower triangle to the conjugate. On diagonal entries the complete imaginary enclosure must contain zero before real projection.

The conjugation is of polynomial coefficients; the real variable $u$ is not changed to an independent complex variable. This distinction is necessary for the actual real-time Gram.

The whole finite angular sum is performed before the final Hermitian center is selected. The four implemented Sobolev spaces are $H^0,H^{1/2},H^1,H^{3/2}$, so all squared angular weights in (2) have exact integer exponents $0,1,2,3$. No approximate fractional frequency weight is used.

For example, the scalar finite row $1-u^2$ has exact squared integral $16/15$. A time-power triangle estimate would instead give $(\sqrt2+\sqrt{2/5})^2$. Both are valid upper bounds, but only (2) retains the cancellation. This example is a mathematical illustration, not an execution of the new native source.

The same per-frequency finite Gram is reused for all four diagonal Sobolev weights and for both all-mode and high-mode records where applicable. This removes the old per-time-power matrix-majorant loop. Actual CPU improvement remains to be measured.

## 4. The infinite-field remainder remains fully charged

Only the finite part has changed. The actual coefficient package still provides complete multiplier errors
$$
\|\delta a\|_{M_s},\ \|\delta b\|_{M_s},\
\|\delta c\|_{M_s},\ \|\delta\tau\|_{M_s},\
\|\delta\sigma\|_{M_s}
$$
uniformly over the whole real leaf and parameter family. They include native primitive errors, selected coefficient fees, angular and time aliases, and both complete rectangular complements.

Let $W,W_r,W_\theta$ be the existing whole-real-time operator bounds of the exact finite reference in $H^s$. Then the unchanged complete residual-difference bounds are
$$
\begin{aligned}
e_r&=\epsilon_a W_r+\epsilon_b W_\theta,\\
e_\theta&=\epsilon_b W_r+\epsilon_c W_\theta+\epsilon_\sigma W,\\
e_0&=\epsilon_\sigma W_\theta+\epsilon_\tau W.
\end{aligned}
$$
For the all-mode scalar residual the additional differentiated retained angular term costs $4N e_\theta$; $DP_N$ has exactly that maximum physical frequency. The high scalar residual has no such low-projected term.

Multiplication by $\sqrt{2h}$ converts the uniform real-time difference into an $L^2(dr)$ operator bound $E$. If $\widehat R$ is the finite residual operator, its complete true Gram obeys
$$
\|R^*R-\widehat R^*\widehat R\|
 \le 2\|\widehat R\|E+E^2.                                  \tag{3}
$$
The final exact binary Hermitian midpoint receives its own directed selection error. Equation (3), that selection fee, and all original coefficient errors remain in the returned nonnegative diagonal radius.

Accordingly, exact integration of a finite time polynomial does not make the true residual exact. A small finite tail is never substituted for an infinite-field error.

## 5. Direct complete source product for R107/R110

The new source additionally returns the five-by-five majorant for the precise product space
$$
L^2\big(dr;\
 H^{1/2}R_0\oplus H^{3/2}R_r\oplus H^{3/2}R_\theta\big).     \tag{4}
$$
It adds the three corresponding complete component Grams and diagonal radii, then pays the selection error of this new sum. The exact forcing signs remain
$(f_0,f_r,f_\theta)=(-R_0,R_r,R_\theta)$; no radial derivative of $R_r$ is introduced.

For disjoint actual radial leaves these complete source Grams can be summed in the same fixed five-input coordinates. If an exact endpoint-height or low-block injection is later applied, it acts on the entire Gram and its radius. The sixth regular input is added as an exact zero core column before the complete cap and boundary wiring are combined.

The returned raw endpoint reference flux is still $8CA^{-1}$ before Hermitian projection. Its selected center and selection error are saved separately. It is not silently identified with the actual whole-family finite DN or the selected low-block matrix.

The positive and negative scalar roots, Airy collars and positive caps remain separate propagation pieces. The source Gram itself is valid for the stated actual operator wherever its complete coefficient package exists; applying the R110 energy estimate additionally requires a genuinely strict-negative interval. The entire quarter-core is not reclassified as strict.

## 6. Replay and current status

After the full original 175 arrays and a completed nine-field package are actually available, the first replay is:
~~~sh
python scripts/fourfold_phase_core_even_weak_residual_exact.py \
  --cover-root data/core_uniform_flow_ci/43307149760 \
  --field-report notes/native_core_20261113_0102/energy9_leaf0060.json \
  --side 1 --bits 320 \
  --out notes/native_core_20261113_0102/core_source_leaf0060_exact_time.json
~~~
The program uniquely identifies the accepted leaf by the report's exact real interval. An optional explicit --leaf-index must match that same interval. A common-span number and an accepted-leaf number are never assumed interchangeable.

This source was written while the native executor was unavailable and has not run. The old observed nine-field leaf package and its full arrays were not pushed before the outage; they must first be restored or rerun. No new complete strong source Gram, measured CPU gain, whole-core propagation, high feedback inverse, or nonlinear correction is asserted by this note.
