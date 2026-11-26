# R144 independent compact moments and complete C0 mean receivers

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

This is **one new scientific target**, independent of the unfinished
fixed-eta0 forward endpoint. It reads the completed original scalar-mean
native and its saved whole scalars. It does not evaluate an old target,
reconstruct a primitive, run an angular DFT, or rerun any forward W flow.
Its exact analytic receiver is
[CR1--CR7, including CR19a](../results/R144-supplement-complete-C0-mean-receiver-and-compact-moments.md),
proof SHA256
`1f55171ae49a3cda07f44c2bc073a41887a7169c9fe210774a373f22599fe81f`.

## 1. Same complete original inputs

The original complete native has 7721 common closed cells, 6144 actual
candidate pieces, and 6143 actual mean interfaces. Its original gzip
container SHA256 is

`e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`.

The five original lossless parts are restored from immutable commit
`46f127c7153f5393dcd2a00f42d4c1d3662c294d`, with their full byte counts,
Git blob identities and SHA256 values. The existing original process,
parts index and old source identities are checked. Restoring bytes is
not running the old producer.

The full raw candidate identity is

`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.

Its intrinsic object is

`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`.

The exact physical amplitude and metric parameters are

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu_0=-\frac{2572625729470897}{72057594037927936},\qquad
 \eta_0=-\frac{7789843107295549}{4611686018427387904}.
$$

The original native retains its original affine half-width $10^{-9}$
around its original intrinsic centre. This target uses those valid
enclosures for that fixed centre. It does not misidentify an affine
increment zero with absolute $\eta=0$, and does not promote the result
to the selected continuous centre $Q_{\delta_*}$.

The original raw fixed-centre residual note supplies

$$
 R_*=\alpha\,\frac{4159086}{10^{13}}
       \ge \|R_0\|_\infty,\qquad
 |v|>\frac{901531879}{10^{10}},\qquad
 |m|>\frac{10687328018}{10^{10}}.
$$

The original residual is standardized, so $\alpha$ occurs exactly once.
These are already proved whole bounds. Their producer is not called.

## 2. Four old scalars are read, not recomputed

The consumer reads the already saved complete Gamma ball from
`notes/2026-11-14-R133-final-complete-scalar-mean-readable-bounds.json`,
gate `complete_Gamma`. It does not recalculate the old logarithm,
its negative-part integral, its interfaces, or its exponential.

From the full original native it reads exactly these three additional
whole scalar records:

- `bounds.complete_triangular_Schur_integral_upper.mean_source_row`;
- `bounds.complete_triangular_Schur_integral_upper.nonmean_row`;
- `bounds.full_interface_log_upper`.

Denote them by $\mathcal R_m,\mathcal R_{\rm nm},J_m$. The new
$C^0$ interpretation has coefficients

$$
 K_0=\Gamma\mathcal R_m,\qquad K_1=\Gamma\mathcal R_{\rm nm}.
$$

All products are made in 320-bit Arb and saved as complete directed
decimal balls. The old $0.538112$ $L^2\to L^2$ coefficient is not used
as a pointwise receiver. The old row maxima are never recomputed.

## 3. New whole receivers and coefficient bounds

Write $\tau=-2a^2/m^3>0$, $U=\langle u^2\rangle$ and
$V=\langle(v-m)^2\rangle$. From each unchanged original row read its
whole $\tau$, $m$, $\beta$, $K$, $U$, $V$, and $a$ records.

The first pass computes the new complete response-jump receiver

$$
 K_J=\Gamma\max_{j\ge1}
 \left(\tau_j^+\max_{i<j}\sup_{I_i}\tau^{-1}\right).
$$

All common interfaces are included, hence in particular all 6143
actual mean jumps. Gamma includes the terminal multiplicative
$T_j^{-1}$ crossed by the injection $\tau_j^+k_j$. This is the
explicit side convention in CR10. The source for a continuous new
mean is still $k_j=-[m]_j$.

The first pass also computes

$$
 m_*\le\inf|m|,\quad M\ge\sup|m|,\quad V_*\ge\sup V,\quad
 Z\ge\sup\frac{\sqrt V}{|m|},\quad B\ge\sup|\beta K|.
$$

The fixed-centre mean lower bound in section 1 may intersect the
original enclosing mean interval; this does not assert a stronger
bound over its entire affine box. The complete mean-jump sum is
bounded by the already saved quantity through $M J_m/3$.

A second pass computes the genuinely new weighted ordinary receiver

$$
 K_{\beta K}=
 \Gamma\max_i b_i\sum_{j\ge i}\ell_jt_j
                      \sup_{I_j}|\beta K|,
 \qquad b_i\ge\sup_{I_i}\tau^{-1},\quad t_j\ge\sup_{I_j}\tau.
$$

This is CR19a. It acts on the ordinary source $\beta Kf$ with zero
response jumps. The nonlinear coefficient is
$K_2=\min(K_0B,K_{\beta K})$, used consistently in both future
small-ball inequalities. Reading the same unchanged rows for this
different weighted receiver does not rerun their primitive, target,
old row maximum or Green computation.

The same reverse pass also computes all eleven weights in
[CP1--CP5](../results/R144-supplement-profile-weighted-mean-feedback-polynomial.md),
proof SHA256
`c9b2469ce02c5553aceee6401a3cc388607aa7ea83d661759aa79078aef797a1`.
With $M(r)=|m(r)|$, $B(r)=|\beta K|$, they are

$$
\begin{array}{lll}
 w_{01}=2BMV\chi,&w_{02}=BMV\chi^2,\\
 w_{10}=2BV,&w_{11}=6BV\chi,&w_{12}=3BV\chi^2,\\
 w_{20}=3B(M+V/M),&w_{21}=6BV\chi/M,&w_{22}=3BV\chi^2/M,\\
 w_{30}=B(1+V/M^2),&w_{31}=2BV\chi/M^2,&w_{32}=BV\chi^2/M^2.
\end{array}
$$

Each new whole $C_{ab}$ is
$\Gamma\max_i b_i\sum_{j\ge i}t_j\int_{I_j}w_{ab}$.
The positive complete coefficient is enclosed on each entire row;
the factors $\chi$ and $\chi^2$ use the same exact polynomial masses
already cached privately by the forward pass. The other weights
use the exact row length. No compact contribution extends beyond
its true support.

All eleven suffix sums and eleven maxima are committed together
with the exact reverse cursor after every accepted row. These
kernels give the complete polynomial CP.7 and avoid separately
multiplying unrelated global variance and nonmean-inverse bounds.
They are new source receivers, not recomputed old Green gains.

## 4. New positive normalized compact moments

Set

$$
 I=[1/20,9/50],\qquad
 \chi=4096t^6(1-t)^6,\qquad
 t=\frac{r-1/20}{13/100}
$$

on $I$, and zero elsewhere. The original common partition must
already contain both exact support edges. Let

$$
 H(r)=\exp\left(\int_0^r2\beta U\,ds\right).
$$

The fixed-centre strict-metric certificate covers
$[0,2333968743003/10^{13}]$, including $I$. Thus $K<0$ there and
$(a'/\sqrt{E_\nu})'=-a\sqrt{E_\nu}K$, $a'(0)=0$, give $\beta\ge0$
on the required prefix. Only that fixed-centre sign is used to
intersect possibly wider affine enclosures. The interval $[0,.9]$
is not treated as negative curvature.

Read only the original rows on $[0,9/50]$ for the new prefix $H$.
Each row with $c=2\beta U\in[c_-,c_+]$, $c_-\ge0$, gives

$$
 H_{\rm next}\in
 [H_-\exp(\ell c_-),\,H_+\exp(\ell c_+)].
$$

On a compact row its entire $H$ range is enclosed by the old left
lower endpoint and the new right upper endpoint. Form the positive
whole enclosure

$$
 P=\frac{4(-\beta K)a^2V}{m^2H}\in[P_-,P_+].
$$

Only strictly positive directed denominator endpoints are inverted.
No division by a wide centered ball is used.

The two new whole scalar moments are

$$
 \overline a=\int_I P\chi,\qquad
 \overline b=\frac12\int_I P\chi^2.
$$

Their exact fixed polynomial masses on each intersected row are
computed with rational arithmetic:

$$
 \int_l^r\chi^p\,ds
 =(13/100)4096^p
 \sum_{k=0}^{6p}(-1)^k\binom{6p}{k}
 \frac{t_r^{6p+k+1}-t_l^{6p+k+1}}{6p+k+1},
 \qquad p=1,2.
$$

The rational expression is checked nonnegative before its directed
Arb conversion. Multiplying these exact masses by $P_-$ and $P_+$
encloses the complete integral. No angular or radial point sample
replaces a continuous bound.

Analytically $0\le\overline b\le\overline a/2$. The actual output
tests only whether the complete saved ball for $\overline a$ proves
strict positivity. An inconclusive lower endpoint remains unknown.

The already completed full-eta signed forward retraction remains
frozen. The ongoing fixed-eta0 W target is also not called.
No future $D_R/G_R$ is presumed: its eventual complete actual
record will be a separate input to a later root/small-ball decision.

## 5. Exact science output and accepted checkpoints

The complete output contains 52 declared scalar fields: the five
receiver constants $K_0,K_1,K_J,K_{\beta K},K_2$; $m_*,M,V_*,Z,B$;
the existing residual bound expressed in physical units, the actual
mean-jump sum bound and raw $v$ gap; $H(9/50),\overline a,\overline b$;
three scalar continuation states for the new weighted suffix
and prefix maxima; all eleven $C_{ab}$; and their eleven suffix sums
and eleven maxima, saved as complete scalar continuation states.

All values use the complete decimal-ball format. The consumer writes
a scalar checkpoint after each fully accepted row and each fully
accepted reverse row. Private per-row increment records stay in one
temporary runner file. Only its accepted-prefix byte count, record
count and SHA256 are published.

If any operation fails, the exception handler reads the last atomic
checkpoint from disk, truncates the private trace to its accepted
byte count, resets complete/proved to false, and saves that prefix
with the real exception. It never writes a partially advanced
in-memory state with an older cursor. The worker independently
hashes the exact saved trace prefix and reports any uncommitted
tail if the process was externally killed.

A first-pass prefix has only prefix norms and moments. A second-pass
prefix has a full first pass and only a reverse suffix of the new
weighted norm. Such records are not complete whole-body receivers. Their explicit
`scalar_scope` is `accepted_forward_prefix_and_reverse_suffix_only`,
so a zero value for an unstarted weighted receiver is an empty
prefix state and is never interpreted as a zero whole upper bound.
The exact cursor and saved whole balls are retained for a genuine
suffix continuation if one is needed; accepted rows must not be
rerun. No automatic retry is authorized by this entry.

After both full passes, the consumer saves all complete scalar balls,
then actually parses that saved file. Only this readback can change
`scalar_scope` to `complete_whole_target` and set the
compact-positive-leverage gate and the complete flag. A complete
unknown or false leverage gate is preserved as the actual outcome.
The flag `proved` means only that the new complete moments also
prove positive compact leverage. It never means that the future
mean root or nonlinear small ball has been proved.

## 6. Public execution and publication scope

The scientific code runs only in the authorized public repository's
GitHub Actions, using Python 3.12.14 and python-flint 0.9.0 at 320 bits.
The public worker restores the exact five historical parts, validates
every current input and Python AST before science, checks actual
topic capacity, and publishes its separate consumed marker before
starting the single child.

The worker performs a real pull/rebase and checks both READMEs
after every pull and at intervals no longer than 1800 seconds.
A rejected push triggers a fresh pull/rebase and retry. Unread rule
changes stop new science and preserve the small checkpoint and receipt.
No artifact, Release, fine array, split array encoding, or repeated
old target is used.

The publication contains only the new complete scalar outcome or
genuine saved prefix, counts, parameters, input/run hashes, execution
receipt and a short scope note. It does not prove the nonmean
equations, raw-interface repair, selected design phase, physical
height/cap match, coupled inverse, exact immersion, or final topic.
