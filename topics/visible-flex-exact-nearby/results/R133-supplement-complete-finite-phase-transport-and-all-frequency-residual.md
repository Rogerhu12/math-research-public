# R133 supplement — exact finite phase transport and its complete residual

## T.1. The actual object and the conclusion

This result uses the repaired continuous final moving centre with definition
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`,
derived from the complete `ac1d5b98…` candidate. The actual affine parameter is fixed at $\eta=\eta_0$, meaning that
the offset is $\delta\eta=0$; this does not set the original $\eta_0$
to zero. The compact parameter is

$$
 \nu=-2572625729470897/72057594037927936.
$$

The original even mean, all 32 finite centre modes, all cumulative value
corrections, both ray signs, and the complete intrinsic Fourier tails are
retained. This is the principal transport of the direct moving Jacobi
system. Identifying it with a passive physical Jacobi transport at an
approximate centre still requires the previously stated residual-sensitive
bridge.

The new producer constructs an exact, finite, piecewise polynomial
transport reference and encloses its **full** PDE residual. The recurrence
which selects the reference has a Fourier projection. The evaluated
residual has no such projection. The infinite-frequency obligation is
paid because the reference and its model coefficient are finite, their
entire product is evaluated, and the error between the model coefficient
and the true coefficient has an independently proved complete Wiener
bound.

The first actual complete scalar germ has now been consumed. It is

$$
 I_0=[0,2609037194989121/1152921504606846976].                 \tag{T.1}
$$

Its two scalar Taylor cells intersect eleven actual candidate pieces in
twelve successive integration intervals. With 64 positive Fourier indices
and radial degree 12, the actual two-leg integrated bounds are

$$
\begin{array}{c|c}
 \text{part of the full residual}&\text{strict upper bound}\\ \hline
 \text{finite residual, }|j|\le64&5.4560\,10^{-35}\\
 \text{finite residual, }64<|j|\le128&2.7180\,10^{-42}\\
 \text{complete true scalar-model remainder}&1.828549\,10^{-16}.
\end{array}                                                   \tag{T.2}
$$

All phase value jumps and both initial errors are **exactly zero**. The
new first-germ native is a complete result on (T.1), not a complete return
certificate. The remaining germs are consumed chronologically by the
same source and exact-source continuation mechanism. No Diophantine
condition, true conjugacy, parameter inverse, or whole body inverse is
claimed from this first prefix.

## T.2. The true and finite coefficient fields

Use physical angular variable $\phi$ with period $\pi/2$, Fourier
functions $e^{4ij\phi}$, and the full norm

$$
 \|f\|_\sigma=\sum_{j\in\mathbb Z}|\widehat f_j|e^{4|j|\sigma},
 \qquad \sigma=1/32.                                      \tag{T.3}
$$

For the actual repaired centre put

$$
 d=\beta I(u^2+Kv^2),\qquad c=-\gamma m q,
 \qquad m=\langle v\rangle,\quad q=\sqrt{-K},
 \qquad F_\pm=d\pm c.                                    \tag{T.4}
$$

Here $I$ is the zero-mean inverse of $\partial_\phi$, with multiplier
$(4ij)^{-1}$ on nonzero indices and zero on the mean. In particular
$\|I f\|_\sigma\le\|f\|_\sigma/4$; the mean of $v$ in $c$ is
not removed.

Each accepted scalar cell comes from
`R133-supplement-complete-Arb-scalar-jets-and-directed-high-Taylor-models.md`.
It supplies exact dyadic degree-seven polynomials for
$\beta,K,s,\gamma,q$ and complete uniform errors
$\epsilon_\beta,\epsilon_K,\epsilon_s,\epsilon_\gamma,\epsilon_q$.
All their original primitive and angular exponential errors are included.
Restricting such a model to a smaller interval preserves its proved
uniform error. This result does not differentiate that error.

On an intersection $[a,b]$ with a single genuine candidate piece,
write $x=(r-a)/(b-a)$. Exact rational polynomial substitution gives the
original cubic $u$, the cubic nonmean part of $v$, its complete mean
correction, and the selected polynomial $s_0$. Thus

$$
 v_0=s_0+\alpha V+e_v,\qquad m_0=\langle v_0\rangle,
 \qquad d_0=\beta_0 I(u^2+K_0v_0^2),
 \qquad c_0=-\gamma_0m_0q_0.                              \tag{T.5}
$$

The exact radial degrees are at most 28 for $d_0$ and 21 for $c_0$.
The complete angular support of $d_0$ is $|j|\le64$; $c_0$ is a
genuine scalar mean. Laurent multiplication forms every coefficient.
There is no angular grid or FFT in this producer.

The following elementary bounds are implemented without discarding
correlations that are needed for validity. Let $U,V$ bound
$\|u\|_\sigma,\|v_0\|_\sigma$; let $K_0^*,q_0^*,m_0^*$ bound the
polynomial scalar absolute values; and let $B^*,K^*,G^*$ be the full
true scalar bounds for $|\beta|,|K|,|\gamma|$. Then

$$
\begin{split}
 \|d-d_0\|_\sigma
 &\le {\epsilon_\beta\over4}(U^2+K_0^*V^2)\\
 &\quad+{B^*\over4}\{\epsilon_K V^2+
             K^*\epsilon_s(2V+\epsilon_s)\},                 \tag{T.6}\\
 |c-c_0|
 &\le\epsilon_\gamma m_0^*q_0^*
       +G^*\{\epsilon_s q_0^*+(m_0^*+\epsilon_s)\epsilon_q\}.
                                                               \tag{T.7}
\end{split}
$$

For (T.6), expand first the change in $\beta$, then
$(K-K_0)v_0^2+K(v^2-v_0^2)$. For (T.7), expand first the change in
$\gamma$, then the change in $m$, then the change in $q$.
Consequently the sum $\epsilon_F$ of these two right sides bounds
$F_\pm-F_{\pm,0}$ on the entire real radial interval and complex
angular strip. A finite radial polynomial is bounded by the sum of the
absolute values of all its coefficients on $0\le x\le1$, with complete
Wiener weights for its angular coefficients.

## T.3. Selecting an exact reference

The fixed polynomial lift $H$ is the one in
`R133-supplement-actual-phase-root-sliver-and-full-transport-residual.md`.
All its 24 sine and 24 cosine coefficients are exact dyadics. Define

$$
 A_\pm=\phi+W_\pm,\qquad
 (W_\pm)_r+F_\pm(1+(W_\pm)_\phi)=0,
 \qquad W_\pm(0)=H-\phi.                                  \tag{T.8}
$$

Fix a reference index bound $N$ and degree $p$. At the beginning of
each successive interval the exact previous reference endpoint supplies
$w_0$. Write

$$
 (b-a)F_{\pm,0}(a+(b-a)x)=\sum_{k=0}^{28} f_{\pm,k}x^k.
$$

The projected Taylor recurrence is only a way of choosing coefficients:

$$
 w_{n+1}^{\rm tentative}
 =-{1\over n+1}\Pi_N\left(
       f_{\pm,n}+\sum_{i=0}^{n}f_{\pm,i}\partial_\phi w_{n-i}
                         \right),\quad 0\le n<p.             \tag{T.9}
$$

All products in (T.9) are computed by finite Laurent polynomial arithmetic.
An Arb enclosure of each positive angular coefficient is replaced by its
explicit dyadic real and imaginary midpoint. The negative coefficient is
**defined** to be its conjugate; the mean is defined to be real. Thus
$\widehat W(x,\phi)=\sum_{n=0}^p w_n(\phi)x^n$ is an exactly defined
real trigonometric polynomial. Nothing assumes that the chosen midpoint
satisfies (T.9) exactly: every rounding error is paid by the complete
residual below.

Its endpoint is the exact rational sum $\sum_nw_n$. This exact sum is
the next interval's $w_0$. It is never rounded to a floating endpoint.
This proves exact continuity across scalar subdivisions, original cubic
interfaces, and adaptive subdivisions. Radial derivative jumps are
permitted; the transport identity uses the polynomial derivative on each
open interval and the exact value matching at its boundaries.

## T.4. The complete residual, including the unretained output

For each leg form the **unprojected** polynomial

$$
 \mathcal R_{\pm,0}(x,\phi)
   =\partial_x\widehat W_\pm+
       (b-a)F_{\pm,0}(1+\partial_\phi\widehat W_\pm).
                                                               \tag{T.10}
$$

Its radial degree is at most $p+28$; its angular support is exactly
contained in $|j|\le N+64$. Every one of these output coefficients is
formed before taking absolute values. If
$\mathcal R_{\pm,0}=\sum_nr_{\pm,n}x^n$, then

$$
 \int_a^b\|\widehat W_{\pm,r}
       +F_{\pm,0}(1+\widehat W_{\pm,\phi})\|_\sigma\,dr
 \le\sum_n{\|r_{\pm,n}\|_\sigma\over n+1}.                  \tag{T.11}
$$

The factor $b-a$ has already been put in (T.10), so there is no missing
radial Jacobian. The stored native separates $|j|\le N$ and
$N<|j|\le N+64$, but sums both in the actual residual. In particular
no assumption that an evolving solution remains in a frequency head is
used.

The complete true-coefficient contribution is bounded by

$$
 (b-a)\epsilon_F\left(
       1+\sum_{n=0}^{p}{\|\partial_\phi w_n\|_\sigma\over n+1}
                         \right).                          \tag{T.12}
$$

The Wiener product inequality proves (T.12). Equations (T.6)–(T.12)
therefore include the entire unknown Fourier remainder of the intrinsic
target, although only finite angular polynomials were generated as a
reference. Both legs are added. The even mean is included in (T.10), in
the exact endpoint, and in the terminal difference.

The adaptive test only controls the retained finite part of (T.11),
requiring it to be below $(b-a)10^{-18}$. A failure bisects the actual
interval and is saved. The unretained finite part and the true scalar
remainder are always charged; they are never made to disappear by this
test. This distinguishes radial approximation error from a genuine
Fourier output tail.

## T.5. Consumption by the complete true-flow contract

The root-sliver theorem proves the true complex path containment needed
to evaluate (T.11)–(T.12) on strip $1/32$ and conclude a return defect
on strip $1/64$. Once **all 169** scalar germs have been consumed up to

$$
 r_b=1249886203106135147/5242880000000000000,
$$

the complete terminal polynomial is

$$
 \widehat D=\widehat W_-(r_b)-\widehat W_+(r_b)-\Omega.
$$

Its mean is retained. The exact source, interface, and endpoint identity
of the preceding theorem gives

$$
 \|H\circ P-H-\Omega\|_{1/64}
 \le\|\widehat D\|_{1/32}
     +\sum_{\text{all intervals and both signs}}
             (\text{T.11}+\text{T.12})
     +4.968975\,10^{-14}.                                 \tag{T.13}
$$

The initial and value-jump terms are exactly zero by T.3. There is no
amplitude Gronwall factor in (T.13), since the error is transported by
the true scalar characteristic. The full initial/terminal and common
drift domain expenses have already been paid in the cited theorem.

The present first-prefix native does not activate (T.13): its boolean
`whole_negative_domain` is false. The source explicitly requires all
169 same-configuration scalar reports and the exact final endpoint
before producing a numerical value for the right side of (T.13).
Even such a defect bound is not by itself a true conjugacy or a complete
nonlinear parameter correction theorem.

## T.6. Actual computation, identity, and continuation

The actual first-prefix run used 256-bit Arb arithmetic, $N=64$,
$p=12$, the complete installed first-germ scalar native, and the original
scientific candidate/shards. Its optimized run completed in 47.15 seconds;
the earlier equivalent first-prefix run took 58.99 seconds. Only repeated
Wiener exponential weights were cached in the optimization. Both reported
the values in (T.2). The earlier initial attempt stopped before any
mathematical output because a hard-coded provider SHA was misspelled;
that failure log is preserved in scratch and not treated as a result.

Files:

- `scripts/fourfold_codazzi_phase_full_transport_Taylor.py` is the complete
  producer and source of all reference/whole-residual arithmetic.
- `notes/2026-11-14-R133-complete-two-ray-transport-first-germ-native.json.gz`
  is the original complete twelve-interval output, copied byte for byte.

Each completed germ records its exact final phase state, all its actual
intervals, both complete residual sums, every rejected subdivision, and
the SHA of each generated exact polynomial. Large readily reproducible
intermediate coefficient arrays are not committed. `--resume` accepts
only a gap-free sequence of completed germ checkpoints with the same
source/configuration and the exact same scalar native SHA for every row.
It resumes from the stored exact rational state, not a reconstructed
floating approximation. The saved residual upper endpoints are rounded
outward when read back.

Reproduction from the topic directory, with the same restored scientific
candidate supplied explicitly:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python -u \
  scripts/fourfold_codazzi_phase_full_transport_Taylor.py \
  --candidate /path/to/the/restored/ac1-candidate.json \
  --scalar notes/2026-11-14-R133-complete-Arb-high-scalar-Taylor-first-germ-native.json.gz \
  --out-dir /path/to/new-phase-transport-prefix
```

Additional published `germNNNN.json.gz` directories are supplied with
`--scalar-dir`; continuation into an existing exact-source output uses
`--resume`. The current actual whole-prefix computation consumes the
published disjoint high-seven CI ranges without reevaluating their
primitive target data.
