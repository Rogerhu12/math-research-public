# R131 supplement: positive weights and complete cleared nonlinear tube rows

2026-11-13, visible-exact-astra-ac0d.

**Proved:** a positive-weight comparison for the actual nonlinear Codazzi
system, its complete polynomial verification method, and the exact initial
pilot intervals below. All complete finite weight functions, including the
unsuccessful preliminary choices, are preserved. The new full [0,1/5]
coefficient computation is ongoing; this note does not certify that whole
continuation. The previously proved same-waist interval [0,1/10] remains
as in the preceding complete-cubic supplement.

## 1. Same actual target and exact error equations

The target object SHA256 is
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848.
The exact parameter center is -7789843107295549/4611686018427387904,
with every displacement |eta| <= 1/1000000000. E is still the complete
angular average of the original candidate's squared radial derivative.
The whole primitive and its tails are retained.

With true k=sqrt(-K)>0, the exact system is

$$
 D_p p=-\beta q(1+p^2)+\kappa(p-q),\qquad
 D_q q=-\beta p(1+q^2)+\kappa(q-p),
$$
$$
 D_p=\partial_r-\gamma q\partial_\theta,\quad
 D_q=\partial_r-\gamma p\partial_\theta,\quad\kappa=K'/(4K).
                                                               \tag{P.1}
$$

Let B,C be the complete finite candidate, with C<0, and put
P=(B+k)/C, Q=(B-k)/C. These use the **true** k. Let R_P,R_Q be their
exact residuals in (P.1), using the candidate transports. The preceding
cubic native bounds both residuals by rho_0 on each original closed cell.
For u=p-P, v=q-Q, subtraction gives

$$
 D_pu=a u+b v-R_P,\qquad D_qv=c u+e v-R_Q,
$$
$$
\begin{split}
 a&=-\beta q(p+P)+\kappa,&
 b&=\gamma P_\theta-\beta(1+P^2)-\kappa,\\
 c&=\gamma Q_\theta-\beta(1+Q^2)-\kappa,&
 e&=-\beta p(q+Q)+\kappa.
\end{split}                                                   \tag{P.2}
$$

The off-diagonal coefficients involve no unknown angular error derivative.

## 2. Positive comparison with an unweighted final gate

Let Wp,Wq be positive, continuous and piecewise C1 in r, and smooth in
angle. Suppose on the actual tube |u|,|v| <= T that

$$
 (aW_p+|b|W_q-D_pW_p)/W_p\le L,\qquad
 (eW_q+|c|W_p-D_qW_q)/W_q\le L.                              \tag{P.3}
$$

If w_- <= min(Wp,Wq) and max(Wp,Wq) <= w_+, with w_->0, then

$$
 z=\max(\|u/W_p\|_\infty,\|v/W_q\|_\infty),\qquad
 D^+z\le Lz+\rho_0/w_-.                                      \tag{P.4}
$$

Indeed, differentiate u/Wp along its actual characteristic, use (P.2),
and evaluate at a positive or negative maximum. Its coupling is at most
|b|Wq z/Wp; the q row gives the other bound. There is no Fourier
truncation of the errors. At each radial join the candidate, weights,
errors and z are continuous. Applying the comparison on both adjacent
open pieces and taking limits therefore requires no jump fee.
The weights need not solve any differential equation.

The implementation replaces L by max(0,L). On a cell of length h,
it constructs a strict affine supersolution with endpoint z1 by checking

$$
 1-hL>0,\qquad z_1-z_0>h(Lz_1+\rho_0/w_-).                  \tag{P.5}
$$

It starts with (z0+h rho_0/w_-)/(1-hL), multiplies by 1+2^-40, and
adds 2^-180; the strict directed margin is then actually checked.
The decisive tests are

$$
 w_+z_1<T,\qquad\operatorname{gap}_{cand}-2w_+z_1>0,
 \qquad k_->0.                                               \tag{P.6}
$$

The positive gap is Q-P in the C<0 convention. A small weighted z does
not replace the unweighted w_+z1. A first-exit argument proves the true
tube throughout each passing cell. Independently, the R131 true weighted
angular-gradient transport gives, for actual |p|,|q| <= M,

$$
 \mathcal G_1\le\mathcal G_0
  \exp\{h[|\beta|(2+4M^2)+4|\kappa|]\},\qquad
 \max(|p_\theta|,|q_\theta|)\le\mathcal G/\operatorname{gap}.
                                                               \tag{P.7}
$$

The initial gradient is the independently certified actual waist value,
not a candidate derivative. Thus the same actual Cauchy solution extends
through every passing cell. Each exact tube is attempted separately,
with the first failing row and all preceding rows saved. The same proof
also permits a certified tube choice on each cell, carrying z continuously;
the saved consumers here use fixed tubes and claim no adaptive result.

## 3. Complete finite weight objects, with their own identity

Floating cooperative evolution, with sqrt(b^2+smoothing^2) in the cross
majorant, is only a way to choose finite functions. Solver success and
tolerance do not prove (P.3). The weight storage has its own object kind
and its own exact initial condition Wp=Wq=1. On each piece, x in [0,1],
the exact polynomial is

$$
 (1-x)L+xR+x(1-x)
 [F_1+x(F_2+(1-x)(F_3+x(F_4+(1-x)(F_5+xF_6))))].             \tag{P.8}
$$

All stored binary64 coefficients mean exact dyadic numbers. L,R are
shared endpoint Fourier arrays; (P.8) interpolates them exactly and is
degree seven. The floating DOP853 endpoint discrepancy is not carried
as a hidden jump. Radial derivative continuity is not needed or claimed.
The non-executed polynomial_contract string in the frozen metadata has
a redundant closing parenthesis; (P.8) is the unambiguous formula of the
actual polynomial_jet evaluator. The stored arrays are unchanged.
The real mean, all specified coefficients and exact negative conjugates
are retained; the specified Nyquist coefficient is zero. The reader
independently checks shapes, exact time fractions, the real mean, and
both initial weights. It shares only polynomial algebra with the BC
reader and does not pretend that weights satisfy BC initial constraints.

| Grid | Smoothing | Pieces | Complete original gzip bytes | Shards |
|---:|---:|---:|---:|---:|
| 512 | 3 | 655 | 30,390,682 | 8 |
| 512 | 10 | 579 | 27,177,816 | 7 |

The original gzip stream is split into consecutive chunks of at most
4 MiB and each chunk is compressed separately. Offset, byte-count and
SHA256 checks reconstruct the entire original byte stream before loading
arrays. Every endpoint, radial correction, Fourier coefficient and mean
is saved. This is not a metadata substitute for complete candidates.

## 4. Both cooperative signs, cleared before interval collapse

For radial scalar models k0,g0,b0,h0 of k,gamma,beta,kappa, set
P0=(B+k0)/C, Q0=(B-k0)/C and A0=-2b0(B^2-k0^2)+h0 C^2. Define

$$
\begin{split}
 H_p&=g_0C(B-k_0)W_{p,\theta}+A_0W_p-C^2W_{p,r},\\
 H_q&=g_0C(B+k_0)W_{q,\theta}+A_0W_q-C^2W_{q,r},\\
 C_p&=g_0[B_\theta C-(B+k_0)C_\theta]
             -b_0[C^2+(B+k_0)^2]-h_0C^2,\\
 C_q&=g_0[B_\theta C-(B-k_0)C_\theta]
             -b_0[C^2+(B-k_0)^2]-h_0C^2.
\end{split}                                                   \tag{P.9}
$$

The two model row rates are the maxima of

$$
 (H_p\mathbin\pm C_pW_q)/(C^2W_p),\qquad
 (H_q\mathbin\pm C_qW_p)/(C^2W_q).                            \tag{P.10}
$$

In particular, an absolute cross term is not bounded separately before
it cancels against the weight derivative. All finite products are formed
first. Their angular degree is at most 2*511+255=1277, so the complete
4096-point product algebra does not alias. Radial degree is at most 21
for v1 and 24 for v2.

For every radial polynomial coefficient the directed Fourier transform
bounds each closed angular cell by its second Taylor polynomial and
complete third-derivative Wiener remainder. The angular half-width is
pi/(4*angles), on the physical quarter circle. Radial Horner evaluation
is then performed at each angular location. Radial variations at
unrelated angles are not collapsed into one Wiener sum first. The
actual positive lower bounds for C^2, Wp and Wq justify every division.

## 5. All true-scalar and nonlinear tube discrepancies

Let dk=k-k0, dg=gamma-g0, db=beta-b0, dh=kappa-h0 and
DeltaK=K+k0^2. The exact common diagonal discrepancy is

$$
 E_a=-2\,db\,PQ-2b_0\Delta K/C^2+dh.                        \tag{P.11}
$$

The velocity discrepancies are dg Q-g0 dk/C and dg P+g0 dk/C.
The off-diagonal discrepancies are exactly

$$
\begin{split}
 E_b={}&dg P_\theta-g_0dk C_\theta/C^2-db(1+P^2)
                   -b_0(dk/C)(2P_0+dk/C)-dh,\\
 E_c={}&dg Q_\theta+g_0dk C_\theta/C^2-db(1+Q^2)
                   +b_0(dk/C)(2Q_0-dk/C)-dh.
\end{split}                                                   \tag{P.12}
$$

Their absolute values are multiplied by the corresponding W, the other
weight, or its angular derivative, and divided by the same row weight.
The v2 calculation keeps the correlated exact identity
DeltaK=-dk(2k0+dk). No actual scalar is silently replaced by its model.

The remaining change of the actual p row inside the error tube is at most

$$
 T|\gamma W_{p,\theta}-2\beta P W_p|/W_p
       +|\beta|T|Q|+|\beta|T^2,                             \tag{P.13}
$$

with P,Q and weights interchanged for the q row. This follows from the
diagonal change -2 beta P v-beta Q u-beta u v and transport change
gamma v Wp,theta/Wp. Thus all linear and quadratic tube terms are paid.
The five exact choices are 1/500, 1/200, 1/100, 1/50 and 1/16.
All original BC endpoints, weight endpoints and true scalar-germ joins
are present in the common partition.

## 6. True cubic models without an extra derivative assumption

The frozen v1 producer uses constant scalar models. The separate v2
producer and explicit consumer use degree three for k,gamma,beta and
degree two for kappa. On a cell with midpoint r0 and half-width h,
Taylor's theorem uses derivatives through d-1 at r0 and the d-th
derivative on the **whole original target germ**. Every model coefficient
is a chosen dyadic number. The sum of distances from all coefficient
balls to those choices bounds the whole scalar error for |x|<=1.
The highest Taylor derivative is not assumed constant for the true field.

The midpoint uses whole eta and the complete primitive; the highest
coefficient consumes the already proved original whole-germ target.
In particular,

$$
 \kappa'=K''/(4K)-(K')^2/(4K^2),
$$
$$
 \kappa''=K'''/(4K)-3K'K''/(4K^2)+(K')^3/(2K^3).              \tag{P.14}
$$

The k derivatives come from the square-root series of -K through third
order. No fourth derivative of k or third derivative of kappa is assumed.
No k0' or g0' term is missing from (P.9): the differentiated functions
in the weight comparison are Wp,Wq. The independently certified true
residual rho_0 includes the full radial derivatives of P,Q.

## 7. Executed failures, floating diagnostics and true native pilots

The initial piecewise-linear 256-angle, smoothing-3 choice has a negative
sampled weight about -1.019486. The linear 512-angle choice has positive
samples but its radial derivative makes all five floating tube trials
fail; their maximum trial errors range from 5.846e12 to 1.655e13.
Both complete arrays, full reports and all attempted failure rows are
preserved. These failures are not a nonexistence claim for the PDE.

The degree-seven choices give these **floating diagnostics only**:

| Smoothing | T | Maximum sampled error | Sampled test |
|---:|---:|---:|---|
| 3 | .01 | .009644330 | passes |
| 3 | .02 | .014603658 | passes |
| 10 | .005 | .003539957 | passes |
| 10 | .01 | .004538264 | passes |
| 10 | .02 | .007659632 | passes |

All other attempted tubes, including unsuccessful .002 and .0625,
remain in the complete reports. None of this table is a native bound.

The actual 192-bit pilots use all finite products and 4096 closed angles:

| Pilot | Actual scope |
|---|---|
| v1, smoothing 3, first two cells | Positive weights and all five true C0/C1 tube consumers pass |
| v1, smoothing 3, partition 600 | Complete isolated row; no waist-to-row continuation |
| v1, smoothing 10, partition 500 | Complete isolated row, T=.02 rate <14.45362 |
| v2, smoothing 10, first cell | Positive weights and all five true C0/C1 tube consumers pass |
| v2, smoothing 10, partition 500 | Complete isolated row, nominal rate <.702646, T=.02 rate <11.095825 |

The last v2 row has true kappa-model error <1.271076e-5. This is a new
coefficient bound for the same actual target and BC candidate.

The v1 two-cell interval is exactly
[0,5348752136943967/9223372036854775808]. Its best attempted tube is
1/500 and proves actual error <4.028117e-8, gap >.24349076109,
and first angular derivative <909.647724. The v2 first interval is
exactly [0,1152921504606847/2305843009213693952]. Its best tube is
1/500, giving error <3.470723e-8, gap >.24349077224 and first angular
derivative <909.589059. The canonical consumers were actually rerun
using their repository native copies; they do not need a transient
scratch file for their verified native input.

These pilots establish the new method's actual data flow. They do not
extend the prior 1/10 result. The full v2 request at 8192 angles is a
separate computation; its unfinished checkpoint and the floating table
do not grant a completed full-interval result.

## 8. Complete artifacts, reproduction and remaining interfaces

[The complete manifest](../notes/2026-11-13-R131-positive-weight-comparison-manifest.json)
records all fifteen weight shards, unsuccessful linear choices, floating
trials, five directed pilots, both actual C0 consumers, all nine new
scripts and their byte identities. The preceding complete BC candidates
and true cubic residual report remain unchanged. Some original floating
reports retain their historical scratch output names; the manifest maps
those names to the saved byte-identical files.

The principal scripts are fourfold_codazzi_positive_weight_candidate.py,
fourfold_codazzi_positive_weights_dense_probe.py, the frozen
fourfold_codazzi_positive_weight_native.py and
fourfold_codazzi_positive_weight_C0.py, and the separate
fourfold_codazzi_positive_weight_cubic_native.py and
fourfold_codazzi_positive_weight_cubic_C0.py.

Use fresh paths because native producers refuse to overwrite an earlier
certificate or failure. The full request is reproduced from the topic by

~~~bash
python scripts/fourfold_codazzi_positive_weight_cubic_native.py \
  --weights notes/2026-11-13-Codazzi-positive-dense-weights-r02-n512-s10-shards.json \
  --grid 4096 --angles 8192 --out /tmp/positive-weight-full-new.json.gz
python scripts/fourfold_codazzi_positive_weight_cubic_C0.py \
  --native /tmp/positive-weight-full-new.json.gz \
  --out /tmp/positive-weight-full-new-C0.json.gz
~~~

The first command must complete every requested box before the second
accepts it. Actual unweighted error, gap and true gradient gates must
then pass. Embedding, crossing the turning point, all cap and nonlinear
regular matching, holonomy and the final common-metric closed family
remain separate requirements.
