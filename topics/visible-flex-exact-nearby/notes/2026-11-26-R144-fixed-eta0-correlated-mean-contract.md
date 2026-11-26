# R144: fixed eta0 correlated rotational mean integral contract

2026-11-26, visible-exact-astra-198c63d-20261126.

This is the contract for **one new whole-domain scientific target**. Its output
does not exist merely because this contract or its consumer has been committed.
Every true, false or unknown conclusion requires the actual complete public
Actions output. A failed or interrupted prefix remains a prefix.

The reference-subtraction identities are proved in
[RS](../results/R144-supplement-fixed-density-rotational-reference-subtraction.md).
The old rotational identity is [R133 Q.3](../results/R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md).
The fixed-density nonlinear retraction is [R144 MV](../results/R144-supplement-exact-nonlinear-mean-elimination-and-retraction.md).
No old residual, Green, response or completed whole-parameter forward target
is recomputed by this entry.

## 1. Exact object and necessary new private input

The original candidate index has SHA256
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
It contains all 6144 original cubic PPoly pieces, 6145 exact binary64 knots,
32 sine modes of the normalized first component and 33 cosine modes of the
second. Every binary64 coefficient denotes its exact dyadic rational.
All five original shards are checked by byte count and SHA256 before use.

The exact parameters are

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu_0=-\frac{2572625729470897}{72057594037927936},\qquad
 \eta_0=-\frac{7789843107295549}{4611686018427387904}.
$$

The intrinsic object SHA256 is
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`.
Its complete original affine origin and direction are restored from immutable
history, and the exact eta0 is applied before scalar evaluation. There is
**zero parameter half-width**. In particular, a full-eta enclosure is not
relabeled as a sharp point-eta carrier.

The old complete raw residual container has SHA256
`6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`,
4592623 bytes, 7296 closed rows and 6143 actual interfaces. All three old
binary parts are restored unchanged. Only its complete identity, exact
partition and qualification are consumed, including the already completed
strict pointwise-v and mean gap balls. Its old residual norms are not
converted into a signed integral and are not recalculated.

The new input is a coherent high-precision Taylor carrier for the products
and the weighted integral below, on the **entire** interval $[0,25/8]$.
This carrier was not stored by the old raw residual producer: that producer
saved residual bounds, not these target coefficients. The old full-eta
7721-row cache and the positive-cap third-jet caches likewise do not provide
this new full-domain fixed-eta0 carrier. Its exact defining functions may
therefore be materialized privately as necessary for this new target.
This statement covers the whole body, the natural graft and every original
join; it is not a claim that only 64 cap domains were missing.

The new centre remains the piecewise raw centre at nu0. It does not inherit
the continuous repair, the selected implicit delta-star, the selected phase,
a full inverse or any unchanged exterior row.

## 2. Actual scalar definition on every germ

The body uses the exact affine scalar splines and explicit positive and
negative scalar germs already defined by the pinned original
`fourfold_phase_beta_interval.py`,
`fourfold_phase_beta_bulk_interval.py` and
`fourfold_phase_beta_affine.py`.
The new reader follows the last file's exact affine coefficient arithmetic,
and calls only the first two definition modules. It does not call any old
scientific entry point. Every real cell lies in one actual common scalar
germ and one compact-control polynomial piece.

At $r=3$, the actual natural graft is built from the same fixed-eta0
entrance coefficients as the pinned original graft and entrance definitions.
Writing $t=8(r-3)$, its cutoff is

$$
 \chi=(1-t)^5(1+5t+15t^2+35t^3+70t^4).
$$

The original log-radius, normalized height slope, normalized horizontal
angle coefficients and normalized vertical angle coefficients are continued
by exactly the original polynomial/exponential formula. The radius powers
$a^3$ and $a^2$ are retained before the infinite primitive is evaluated.
The new constructor does not invoke the old positive-half-width parameter
constructor and does not replace the graft by a rotational approximation.

On either part let $P$ be the complete unit primitive correction, let
$L=a'/a$, $H=z'/a^2$, and put $u_P=LP+P_r$. Then

$$
 e=2L(u_P)_{0,x}+\sum_k u_{P,k}\mathbin{\cdot}u_{P,-k},\qquad
 \bar E=L^2+a^2H^2+e.
$$

The dot product is bilinear on the complex radial extension; it does not
conjugate the radial variable. On the real axis this is the actual metric.
The radius-cancelled curvature is

$$
 K_0=\frac{H^2(L^2-L')+LHH'+(Le'-2L'e)/(2a^2)}{\bar E^2}.
$$

For the original compact bump $h$ and nu0, define

$$
 G=\bar E e^{\nu_0h},\qquad
 R=H^2+\frac e{a^2}+\frac{\bar E}{a^2}(e^{\nu_0h}-1),
$$

$$
 s=-\sqrt{G/R},\qquad
 K=\left(K_0+\frac{\nu_0Lh'}{2a^2\bar E}\right)e^{-\nu_0h}.
$$

These are the same formulas as the pinned complete reciprocal target
providers. Every original compact join, scalar join and the body/graft
join belongs to the immutable 7296-row cover. There is no division by $K$.

For a given real cell, the fixed local scalar and candidate polynomial
germs are analytically continued to a complex neighborhood. This is a
Taylor certificate for the function on that cell, not a definition of the
global real target beyond its germ. The analytic neighborhood must be
admitted directly: throughout the enclosing complex square the consumer
proves $a\ne0$ and positive real parts of $\bar E,G,R,G/R$, and proves
$\Re(s+w)<0$. The square contains the full Cauchy circle. These checks
retain one holomorphic square-root branch and every denominator on the
complete contour. A failed chart causes a subdivision of the current new
integral cell; it never permits a branch crossing.

## 3. Native Acb DFT and the entire primitive

The runtime is Python 3.12.14, python-flint 0.9.0 and numpy 2.3.5, with
320-bit Arb/Acb arithmetic. Dynamic carrier values are never converted to
binary64. Float conversion is used only when reading the already frozen
binary64 inputs, which then become their exact dyadic Arb values.

For $N=512$ and normalized angle $x=4\phi$, the complete point Taylor
series of the unit tangent difference are evaluated at all $N$ roots of
unity. The call is the forward-transform API

`acb.dft(values)/N`.

The DFT convention is
$\widehat T_k=N^{-1}\sum_jT_j e^{-2\pi ijk/N}$. No inverse-transform
normalization is being assumed. Primary references are the
[python-flint 0.9 Acb API](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.dft)
and [FLINT DFT convention](https://flintlib.org/doc/acb_dft/index.html).
The original repository also uses this API in
`fourfold_joint_dft_l2_noise.py`.
For physical frequency $n=4k$, the primitive coefficients are

$$
 P_{k,x}=\frac{inT_{k,x}+T_{k,y}}{1-n^2},\quad
 P_{k,y}=\frac{-T_{k,x}+inT_{k,y}}{1-n^2},\quad
 P_{k,z}=\frac{T_{k,z}}{in}\quad(k\ne0).
$$

The exact zero-mean vertical convention, the true parities and the omitted
Nyquist coefficient agree with the original definition. Omitted modes are
not zero by assertion. Every Fourier alias and the full infinite tail are
paid by the already proved `primitive_fourier_budget` at
$\sigma=8/25$ in the normalized angular variable. Its factors
$1/(4|k|-1)$ and angular multiplicities retain the physical frequency 4.

For the scalar angles on an enlarged complex radial box, let

$$
 B+T=\sum_j(|\beta_j|+|\gamma_j|)\cosh(\sigma j).
$$

Every tangent-difference component has modulus at most
$(B+T)e^{B+T}$. Multiplying the original primitive budget by this quantity
therefore encloses the full componentwise $A^0$ primitive error on the
enlarged radial domain.

If this complete error is $\varepsilon$ on a radial disk of radius
$R_t$, the error in Taylor coefficient $j$ is
$\varepsilon_j=\varepsilon/R_t^j$. These are coefficients, not derivatives;
no factorial is dropped. For $u_P=LP+P_r$, define

$$
 E_j=(j+1)\varepsilon_{j+1}
       +\sum_{i=0}^j|L_i|\varepsilon_{j-i},\qquad
 M_j=\max_{\ell=1,2,3}\sum_k|(u_{P,k,\ell})_j|.
$$

The complete energy-coefficient fee is

$$
 2\sum_{i=0}^j|L_i|E_{j-i}
 +3\sum_{i=0}^j
   (M_iE_{j-i}+M_{j-i}E_i+E_iE_{j-i}).
$$

The factor 3 pays all vector components. This is the same bilinear
product estimate for finite coefficients and the unexpanded infinite
tail. At a true real point, imaginary intervals must contain zero before
a real projection; on the complex contour no imaginary part is deleted.

The point primitive has coefficients through order 27. The energy has
coefficients through order 26 and curvature through order 25. All target
and retraction state series needed below therefore have coefficients
through order 25; the source $c,b$ needs coefficients through order 24.
The separate complex-disc bound needs primitive coefficients only through
order 2, which suffice for the exact curvature value and hence a complete
bound for $c,b$. Its derivative tails are nevertheless retained.

## 4. One shared radial variable and the new signed source

For each original PPoly piece, use its exact local cubic, with the same
radial Taylor variable as the intrinsic carrier. Form directly

$$
 w=\alpha V_0,\quad
 U=\frac{\alpha^2}{2}\sum_{k=1}^{32}U_k^2,\quad
 V=\frac{\alpha^2}{2}\sum_{k=1}^{32}V_k^2,\quad m=s+w.
$$

Every candidate mode is included. These are exact polynomial means,
without an angular FFT. By RS the single new target is

$$
 W'=cW+b,\qquad W(0)=0,\qquad
 c=2\beta U,\qquad
 b=2\beta a^2\left(\frac U{s^2}+\frac{KV}{m^2}\right).
$$

The two source terms are added as full signed Taylor series before
taking a range. They are not bounded separately by their absolute values.
Recover

$$
 N_s=a^2/s^2,\quad n=a^2/m^2,\quad
 N=N_s-n=\frac{a^2w(2s+w)}{s^2m^2},\quad
 Y=W+N_s,\quad D=W+N.
$$

The accurate nonzero original initial difference is retained as

$$
 D(0)=\frac{t(t-2)}{(1-t)^2},\qquad t=w(0)/a(0).
$$

Thus $W(0)=0$ does not reset the old raw centre's mean error.

## 5. Validated local flow and complete closed-cell ranges

Let a current real subcell be $r=r_c+x$, $|x|\le h$, and choose
$\rho=8h$. The complex square used in Section 2 encloses $|x|\le\rho$.
Let $M_c,M_b$ bound the complete exact $c,b$ on that disc. Define

$$
 P(x)=\exp\left(\int_0^xc(z)\,dz\right),\qquad
 Q(x)=\int_0^x b(z)/P(z)\,dz.
$$

The native Taylor algebra computes their coefficients through degree 25.
On the full disc,

$$
 |P|,\ |P^{-1}|\le M_P=e^{\rho M_c},\qquad
 |Q|\le M_Q=\rho M_bM_P .
$$

For $\theta=h/\rho=1/8$, a degree-25 Taylor remainder is at most

$$
 M\,\frac{\theta^{26}}{1-\theta}.
$$

This fee is applied separately with the relevant complete analytic bound,
including all primitive errors. The endpoint values $P_\pm,Q_\pm$ are
complete balls. Positive $P_\pm$ are also intersected with
$[e^{-hM_c},e^{hM_c}]$; inverse bounds are formed from positive endpoints.

Given the saved complete $W_-$, set

$$
 T=W_-/P_- - Q_-,\qquad
 W(x)=P(x)(T+Q(x)),\qquad
 G_{\rm cell}=P_+/P_- .
$$

Its full-disc bound is $M_W=M_P(|T|+M_Q)$. Both the endpoint formula
and the degree-25 Taylor formula enclose $W_+$ and are intersected.

For a whole closed cell, the consumer forms **the Taylor sum**
$W+N$ before interval evaluation. The complete remainder is bounded by
$(M_W+M_N)\theta^{26}/(1-\theta)$. The same procedure is used for $W+N_s$.
This retains same-r cancellation throughout the cell; independent scalar
ranges of $W$ and $N$ are not substituted for their sum. Directed real
Taylor ranges are intersected with the exact positive algebraic enclosure
for $n=a^2/m^2$ and with $Y=n+D$. No knot-only statement is used as a
closed-cell positivity certificate.

A complex-chart failure subdivides only the still unfinished part of
the current new cell. Each accepted subcell is checkpointed. A scientific
timeout or failure preserves its exact endpoint, whole-ball state,
first-witness history, interface state and actual private-trace hash.
All prospective state, count and trace changes become committed only with
the atomic checkpoint. If later postprocessing raises, the handler reads
that last checkpoint back, discards uncommitted in-memory changes and
truncates any private trace tail to its saved byte count. A killed process
also leaves that last checkpoint intact. The worker verifies exactly the
saved accepted trace prefix and records any uncommitted tail separately.
A complete flag is saved only after the final saved-ball decisions have been evaluated.
Already accepted subcells are not silently recomputed by an automatic
retry. An independent explicit continuation would have to consume that
checkpoint.

## 6. Every interface and full original forward sensitivity

The whole original PPoly cover and all 6143 actual joins are verified.
At a join, $a,s$ are the common intrinsic values and $w_\pm$ are the
actual left and right raw cubics. The exact signed atom is

$$
 -[n]=
 \frac{a^2(w_+-w_-)(2s+w_++w_-)}
 {(s+w_+)^2(s+w_-)^2}.
$$

$W,Y$ remain continuous, as proved in RS. The new full field is not
therefore continuous: its nonmean transmission remains an independent
obligation. No raw jump is rounded to zero.

In addition to the primary $W$, propagate the full scalar multiplier
$G(r,0)$ and the signed atom sum $A_D$ by the same local multiplier,
adding this atom once at each actual join. Then save the complete ball

$$
 B_D=D-G(r,0)D(0)-A_D.
$$

By RS.12--15 it is exactly the full weighted signed residual integral,
including the old initial sensitivity and every original mean interface.
It is not an old norm bound with a new label. The genuine physical
$a(r)^{-2}$ amplification is retained.

## 7. Whole physical gates and new outer source

All final gates consume the scalar document actually saved and parsed
back from disk. A certificate of a narrow midpoint is insufficient.

If $Y>0$ on every complete closed subcell, then
$m^\flat=-a/\sqrt Y$ and $v^\flat/v=\sqrt{n/Y}$ at the identical material
angle. The original raw density positivity is inherited only from the
already completed same-object whole raw certificate; it is not newly
asserted from $Y>0$ alone.

For complete positive balls $Y,n$, use the monotone positive endpoint
kernel in RS.21. Since all 32 nonmean cosine modes remain,

$$
 \|\bar v\|_{A^0}\le -m+\sqrt{64V},
$$

so its complete upper bound times the ratio-change bound controls the
whole componentwise moving $C^0$ change. A certified endpoint mean shift
larger than $10^{-4}$ is a genuine failure witness. A strictly negative
$Y$ is a genuine failure of the admissible real retraction. Otherwise a
nonpassing sufficient bound is recorded as unknown, not false.

At the outer endpoint the saved signed physical mean source is

$$
 \Delta\langle C\rangle_\theta
   =-\frac{D}{a(\sqrt Y+\sqrt n)}.
$$

This denominator is bounded from strict positive endpoints. It is not
inverted as a wide centered-ball product. A nonzero signed ball excludes
an unchanged outer mean; a ball containing zero alone proves neither
unchanged mean nor a zero source.

Successful completion of this single target permits true, false or
unknown gates. It does not establish the nonmean equations, phase,
height, exterior matching, a full inverse or the topic completion
criteria. The previous whole-eta row-range result remains frozen.

## 8. Publication and execution closure

The manifest pins the consumer, worker, metadata generator, this contract,
the source/proof definitions, the old complete partition index, the raw
candidate index, the exact object and the reviewed rules. Its ten
historical inputs are exactly three raw-container parts, five original
candidate shards and two frozen affine inputs. Every dependency imported
by the scientific child is included under its actual module filename.

Scientific evaluation occurs only in the authorized public Actions
repository. Private materialization precedes one scientific child.
The worker checks all Python sources by AST, pins the runtime, performs
a real pull/rebase and README comparison after every pull and at most
1800 seconds apart, checks the complete current topic capacity, and uses
one consumed marker for this new target. A rejected push immediately
enters the pull/rebase/push loop.

Fine carrier arrays and all detailed rows stay in the temporary runner
directory. The only scientific publication is the whole small scalar
outcome or a genuine prefix, with exact parameters, counts, witnesses,
run identity and hashes. No new arrays, artifacts or Releases are
published.
