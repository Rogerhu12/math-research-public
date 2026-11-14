# R133 supplement: exact complex root coefficient derivatives for the first Airy forcing

2026-11-14, phase_inverse.

**Proved finite-coefficient consumer contract.** This supplies the
complex coefficient and radial-derivative inputs required by
[G.11--G.13](R133-supplement-old-root-product-and-separated-first-Airy-amplitude-budgets.md)
without differentiating an interval enclosure or substituting
real-only larger-window jets. It uses the one actual original root
piece, its already proved intrinsic complex germ, and the two exact
original cubic shards. Numerical bounds remain subject to public
directed execution.

## 1. The original finite polynomials and constant repairs

The root piece is index 2549. It lies in the original candidate
shard with interval indices $[1346,2692)$ and the original complete
response shard with indices $[2265,2718)$. The local indices are
therefore 1203 and 284. Their original bytes, index files, exact
dyadic nodes and all four coefficient rows must be checked.

For either original coefficient polynomial, in its actual
local coordinate $x=r-r_{\rm left}$,

$$
 p(x)=c_0x^3+c_1x^2+c_2x+c_3,\qquad
 p_r(x)=(3c_0x+2c_1)x+c_2 .
 \tag{H.1}
$$

All $c_i$ are the exact dyadic values of the original finite
files. The candidate polynomial is multiplied by its exact
recorded amplitude; the physical response polynomial is not.
The exact continuous value repairs in both the background and
the direction are constant on this original open piece.
They therefore contribute their full values at order zero
and contribute exactly zero to (H.1). No interface jump is
thereby deleted.

The original complex radial rectangle is

$$
 \operatorname{Re}r\in[r_- -10^{-5},r_+ +10^{-5}],
 \qquad |\operatorname{Im}r|\le10^{-5},
 \tag{H.2}
$$

where $[r_-,r_+]$ is the certified actual root interval.
The original producer
[fourfold_codazzi_moving_turning_complex_germ.py](../scripts/fourfold_codazzi_moving_turning_complex_germ.py)
constructs its complex radial argument from precisely this real interval
and imaginary half-width, evaluates the intrinsic target on that argument,
and saves the two fields in its exact complex_radial_rectangle record.
Thus (H.2) is the original computed rectangle, not an enlargement inferred
from a disk-only bound.
It lies strictly inside this one original polynomial piece
and the original intrinsic scalar germ.
Evaluate (H.1) on that same rectangle by complex interval
Horner multiplication. This gives complete componentwise
bounds $P'_j,Z'_j$, including each true mean coefficient.
No original zeroth-order target, transport or amplitude
calculation is repeated.

The identities and exact constant repair are those of
[the complete scalarization input](R133-supplement-complete-moving-root-scalarization.md)
and
[L.7--L.11](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md).
A raw response is not identified with a mean-completed
response trial; the direction here is exactly the original
repaired $Z$ defining the explicit family.

## 2. Complete old-angle derivative norms

Let $\delta_0=10^{-8}$ and let $\sigma\ge0$ be the old-angle
width actually required by the inverse image. For the
complex family $|\delta|\le\delta_0$,

$$
 \begin{split}
 U_r(\sigma)&\le
       \sum_{j=1}^{32}P'_{u,j}e^{4j\sigma}
       +\delta_0\sum_{j=1}^{96}Z'_{u,j}e^{4j\sigma},\\
 V_r(\sigma)&\le M_r+
       \sum_{j=1}^{32}P'_{v,j}e^{4j\sigma}
       +\delta_0\sum_{j=1}^{96}Z'_{v,j}e^{4j\sigma}.
 \end{split} \tag{H.3}
$$

The candidate coefficients in these sums already include its
exact amplitude. The actual scalar mean derivative satisfies

$$
 M_r\le |m_{r,\rm original}|+\delta_0 Z'_{v,0}.
 \tag{H.4}
$$

The complete original complex germ already records
$m_{r,\rm original}=s_r+\alpha P'_{v,0}$, so that quantity
can be reused. The background mean repair has zero radial
derivative. The true direction mean in (H.4) remains present.

All 65 candidate and 193 direction derivatives are enclosed,
even if only their complete norms are subsequently used.
For higher angular derivatives multiply each nonzero summand
by $(4j)^q$; the mean is absent only when $q>0$.

The previously completed order-zero and angular norms may
be widened to $\sigma$ using the independently paid exact
base/direction bands 32 and 96. Their base factor is
$e^{128(\sigma-\sigma_{\rm nat})}$ and their direction factor
is $e^{384(\sigma-\sigma_{\rm nat})}$, for
$\sigma\ge\sigma_{\rm nat}=1/1024$.
The mean is retained in the zeroth-order $V$ norm.
These are bounds on the original Fourier series at fixed
old $r,\phi$, not on a finite physical-angle Fourier fit.

## 3. The scalar derivatives are exact intrinsic identities

Let $a_{\rm met},E$ denote the original intrinsic metric
functions, to distinguish $a_{\rm met}$ from the root
characteristic coefficient $\eta\sqrt{k}$. The complete
complex native already encloses
$a_{\rm met},a_{{\rm met},r},a_{{\rm met},rr},E,E_r$ and
their nonzero denominators. Thus

$$
 \beta_r=\frac{a_{{\rm met},rr}}{a_{\rm met}}-\beta^2,
 \qquad
 \frac{\gamma_r}{\gamma}=\frac{E_r}{2E}-\beta,
 \qquad
 \frac{\eta_r}{\eta}=\frac{\gamma_r}{\gamma}+\frac{m_r}{m}.
 \tag{H.5}
$$

Every division uses the actual complex denominator enclosure.
If $m_->0$ is the already proved modulus gap, a valid scalar
upper bound is

$$
 E_\eta=
 \left|\frac{E_r}{2E}-\beta\right|+\frac{M_r}{m_-}.
 \tag{H.6}
$$

The full parameter mean and both original mean repairs
remain in the denominator $m_-$. The root and these
intrinsic functions are independent of the compact metric
parameter on (H.2), which lies wholly to the right of $9/50$.
This local fact does not extend that independence into the
metric bump.

## 4. Complete coefficient majorants for the old degree-zero operator

Write $b=|\beta|$, $b_1=|\beta_r|$, $k_0=|K|$,
$k_1=|K_r|$, $\eta_+=|\eta|$, and $\eta_->0$ for a modulus
gap. Let $u_0,u_1,v_0,v_1,u_r,v_r$ denote the complete
old-angle norms supplied above at the same width. Put

$$
 S=u_0^2+k_0v_0^2,\qquad
 S_r=2u_0u_r+k_1v_0^2+2k_0v_0v_r .
$$

The old primitive, with its full zero-mode projection, gives

$$
 d_0\le bS/4,\quad d_1\le bS,\quad
 d_r\le(b_1S+bS_r)/4 .
 \tag{H.7}
$$

In particular the factor $1/4$ is applied to the entire
nonmean primitive. No old mean is substituted for that
primitive.

A direct triangle bound for the exact L.1/L.4 coefficients is

$$
 \begin{split}
 \ell_0&=2bu_0v_0,&
 \ell_\phi&=2b(u_1v_0+u_0v_1),\\
 \ell_r&=2b_1u_0v_0+2b(u_rv_0+u_0v_r),&
 e_\phi&=2b(3u_0u_1+k_0v_0v_1),\\
 b_{0,+}&=b(1+u_0^2+3k_0v_0^2),&
 (b_0)_{\phi,+}&=2b(u_0u_1+3k_0v_0v_1),\\
 (b_0)_{r,+}&=b_1(1+u_0^2+3k_0v_0^2)
       +b(2u_0u_r+3k_1v_0^2+6k_0v_0v_r),\\
 t_{Q,+}&=E_\eta+d_1+b(1+3u_0^2+k_0v_0^2).
 \end{split} \tag{H.8}
$$

Here $b_0$ is the original local operator coefficient, not an
Airy amplitude. Keeping the full one-gain contribution,

$$
 \begin{split}
 r_{Q,+}={}&\ell_r+d_0\ell_\phi+\eta_+e_\phi
       +2b\eta_+u_1u_0+\ell_0(E_\eta+d_1),\\
 \vartheta_+={}&r_{Q,+}/\eta_-+2bk_0v_0v_1,\\
 V_{0,+}={}&t_{Q,+}b_{0,+}+(b_0)_{r,+}
       +d_0(b_0)_{\phi,+}
       +k_0(\ell_0^2+4b\eta_+v_0u_1).
 \end{split} \tag{H.9}
$$

Finally

$$
 T_{0,+}\le E_\eta+4bS_{\rm mean}+5d_1,
 \qquad
 S_{\rm mean}\ge|\langle u^2+Kv^2\rangle|.
 \tag{H.10}
$$

The scalar mean in (H.10) can use the already complete native
Fourier norms before angular widening; taking a mean is
independent of the complex angular evaluation point.
The derivative and projection in all other terms still use
their declared old-angle strip.

These formulas are exactly the absolute-value versions of
L.4, including its radial derivative and the ordered
$H^{-1}H_D$ term. They supply G.11--G.13 on the true inverse
image. They do not absorb the full old-circle $I/J$ remainder
or the independent even-mean equation into the local forcing.

## 5. Numerical consumption and its scope

A complete public consumer must check the two exact shard
identities, the same piece interval, the whole original
complex domain, the actual fold/leading/root-budget receipts,
and all inverse-image and angular-characteristic margins.
It then evaluates the separate G.18--G.19 bounds and records
every positive Cauchy margin used for the first amplitude.

A positive-order derivative computed on (H.2) is a new finite
polynomial evaluation on an already proved domain. It is
neither a new target solve nor a repeat of the completed
zeroth-order root, fold or amplitude calculation.
Only the one root piece is used. No analytic continuation
across an actual polynomial seam is asserted.

The result is an actual inner-root forcing and derivative
budget only after that execution. It does not itself bound
the complete two-sided $L_0w_1$ source, the full old inverse
remainder on $w_1$, all original jumps, the finite head,
or the final strong-return inverse.
