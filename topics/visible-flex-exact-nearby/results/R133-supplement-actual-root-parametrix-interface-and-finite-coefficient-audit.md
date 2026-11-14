# R133 supplement: actual root-parametrix interface and finite-coefficient audit

2026-11-14, phase_inverse.

Public Actions run **43608838195**, attempt 1, actually completed the
independent interface consumer with return code 0 and **25/25 gates**.
Its mathematical process took 0.665159872 seconds and verified all 15
pinned inputs. No original interface computation was rerun.

The object is the continuous repaired M32 centre at the original
intrinsic parameters and explicit affine offset $\delta=0$.
This result supplies actual numerical interfaces for
[the complete moving root parametrix](R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md).
The analytic proof identifies the scalar finite root coefficient;
these finite checks do not replace its full construction.

## 1. Actual execution and immutable identities

The workflow event was commit
2d9d443b25412a4982fd8b8a3bf61fa2d354832c.
The independently recorded scientific checkout was
20fdbe541e27fa1309364350c8c6a5649eabd904.

| Artifact | SHA256 |
| --- | --- |
| Complete actual native, 3341 bytes | e80e42d182f5b77158fb147cfe12300d62769dbf7d4777d1bd4e5c244a70cdb6 |
| Actual process record | 6e37f952b75f030ead37cddef72cafc37c7bace8672a9c9f1ff6bbeeb007e151 |
| Mathematical consumer | cfda10d805d4a21811a13d95aaa5f53a3325230855af790d2e6c4fe6fdc2c44a |
| Independent execution driver | cbcfbcb21bdbe5c28170b08366bfec057fb4919dafeb17a9a3c81331e7ccc876 |
| Exact 15-file manifest | 23ee815bad88e7972aff601974cdc4e246ab0e5a4a886626e669605eaa170c33 |
| Reviewed parametrix proof | f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7 |

Original native identities:

| Original interface | SHA256 |
| --- | --- |
| Complete positive root graph | 2425a0338b958be5d7fb48c955b5a5ce59348f05f1832ab50a81d6cf7dbbc501 |
| Full root-to-negative Cauchy map | 8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d |
| Old-curve primitive and Airy amplitudes | 4ebc5865a8427e67e003e0aa25d8f629353ed87efd67d1705e1cdac7d2fc5b39 |
| Actual principal fold | 9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd |

The source is
[scripts/fourfold_codazzi_actual_root_parametrix_interface.py](../scripts/fourfold_codazzi_actual_root_parametrix_interface.py).
The original output is under
[notes/actual_root_parametrix_interface_ci/run-43608838195-1/consumers/](../notes/actual_root_parametrix_interface_ci/run-43608838195-1/consumers/process.json).
Runtime was Python 3.12.14, python-flint 0.9.0 and Sympy 1.14.0;
the numerical child used 320-bit Arb.

## 2. The real ordinary-source correction fees

Both positive source columns use the ordinary norm
$L^2_rH^{1/3}_\phi$. With the original notation,
the exact collar column is $q_cq_b\sigma B_c$, not
$q_c^2\sigma B_c$. The consumer independently checked this
identity before applying the saved interval rows.

| Quantity | Certified bound |
| --- | --- |
| Collar source to root $Z$ | $<0.012924069462859$ |
| Body source to root $Z$ | $<0.181137705127099$ |
| Combined positive source to root $Z$ | $<0.181598182233<1/5$ |
| Collar source to negative raw state | $<0.953796326358962<1$ |
| Body source to negative raw state | $<13.367962638380$ |
| Negative ordinary source to negative raw state | $\le0.0123<1/80$ |
| Root Airy error to negative raw state | $\le41/10$ |

The fourth and fifth rows include the root factor 9, Bessel
conversion factor 2, and negative propagation factor $41/10$.
Consequently, if the trial has zero body residual and zero other
exterior/jump inputs as constructed in (P.15)--(P.18), then
$$
 \|e_-\|_{L^\infty_rL^2_\phi}
 \le F_c+\frac1{80}F_-+\frac{41}{10}E_{\rm root,low}.
$$
The last term retains the entire low root trace and its true mean.

All seven positive columns remain: root stable input, collar/body
sources, outer mean/head and weighted jumps, collar jumps, and both
cut jumps. Nonzero ports require that full map; a nonzero body source
has the separate coefficient above.

## 3. Actual domains and elliptic root port

For the exact negative cut
$r_c=76285779072683/320000000000000$, the complete root interval gives
$$
 1.733762866879\,10^{-5}<-T(r_c,\phi)
                         <1.7444326892969\,10^{-5}.
$$
The positive cutoff between distances $2\,10^{-6}$ and $3\,10^{-6}$
from the true root satisfies
$$
 9.0899106595\,10^{-6}<T<1.3718773650426\,10^{-5}.
$$
Both lie inside the previously certified inner domain $|T|<19/10^6$.
The real positive Airy exponent and old-mean contour exponent obey
$$
 c_+>1.8270404521604\,10^{-8},\qquad
 c_\Pi>0.0029212649980456>1/512.
$$
Positivity of this very small $c_+$ gives no cutoff-97 smallness.

Arb evaluation of the exact gamma-function values gives
$\operatorname{Ai}(0)>1/3$ and $\operatorname{Ai}'(0)<0$.
The principal stable root diagonal therefore has the uniform floor
$$
 c_n\ge\operatorname{Ai}(0)/\sqrt{67}
                  >0.0433735800743750>1/25.
$$
This diagonal floor gives no numerical incoming cutoff.
The full inverse gives
$$
 \|J\|_{L^2\to H^{1/3}}
 \le\sqrt{J_0^2+J_1^2}<3.402933566759<7/2.
$$

## 4. What the finite algebra verified

The symbolic checks retain the inverse-frame orientation, the common
$\ell$ term in both curvature rows, the zero constant in the analytic
Puiseux ratio, and the odd finite symmetric gauge. Its zero mean
does not delete the nonmean operator.
The proof's other-branch cancellation (P.23a) is applied before a
row is represented by a single canonical graph.

The density input normalization is $n^{7/6}$, with $n=4|j|$.
An unnormalized residual of order $n^{-4}$ consequently gives
order $n^{-17/6}$ after this normalization.
The full-output column remainder of order $n^{-2}$ has weighted
Hilbert--Schmidt series power $-4/3$ in the
$H^{-4/3}\to L^2$ window.

All of the following actual numerical claims remain explicitly
false in the saved native: complete transported amplitudes evaluated;
$C_E,C_s$ evaluated; numerical incoming cutoff certified; numerical
strong-return budget certified; full return inverse from 97 proved;
nonzero-$\delta$ positive graph transferred; and nonlinear PDE or
true parameter Schur proved. The analytic strong-class construction
and its bound formula remain distinct from those outstanding
numerical obligations.
