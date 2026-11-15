# R133 supplement: append only the missing true-root intrinsic orders

2026-11-15, visible-exact / root.

The complete original true-root calculation already supplies ordinary finite
primitive derivatives \(F_0,\ldots,F_{11}\), the complete errors at those
orders, all 36 required bilinear means, \(E_0,\ldots,E_{10}\), and
\(K,\beta,\gamma,s\) through ordinary order nine. This note specifies an
extension to intrinsic order fifteen that preserves all those successful
records. It requires only six new finite Fourier derivative columns, at
orders 12 through 17. All new numerical work runs in the public repository's
GitHub Actions.

This is a finite, rigorous extension of the input certificate for the same
Taylor recurrence. It does not itself assert a smaller Taylor remainder,
a strong-return bound, or the full PDE inverse.

## 1. Exact inherited object and scope

Use the successful native from run43651259105, SHA256
38a8ba8d2998a75ddb863fe9b486defd756a22488e1c3a96ed8bf54581877e8f,
with its actual zero-return process
3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe.
Its original completed finite point remains the exact object copied from
run43650466853, including the raw nonzero-width Nyquist intervals and that
run's preserved failure.

The object definition, true-root germ, parameter enclosure, physical scalar
piece, 512 nodes, physical frequencies and scalar-polynomial convention are
unchanged. The intrinsic parameter is the original \(\eta_0\).
The bump vanishes identically on this germ, so the inherited intrinsic
independence of the explicit deformation parameter has precisely its
original scope. No statement about other intrinsic-parameter roots is added.

The two completed auxiliary rectangles have radii \(1/10000\) and \(1/2000\).
Their original complete error bounds through order five are consumed.
Neither a rectangle nor an infinite-tail evaluator is rerun.

All ordinary derivatives below are with respect to the old physical radial
variable \(r\), until the explicit substitution \(\rho=r_*-r\).

## 2. Recover the missing auxiliary primitive without old FFTs

Let \(P_j\) be the original finite unit-primitive derivative, and let \(a_j,z_j\)
be the physical radius and height derivatives. Write \(e_x,e_z\) for the
constant Fourier mode vectors. The original finite construction gives

$$
F_j=\sum_{h=0}^{j}\binom jh a_{j-h}P_h+a_j e_x+z_j e_z.
\tag{H.1}
$$

The stored radius has a strictly positive zeroth-order lower bound.
Thus its unsaved auxiliary \(P_0,\ldots,P_{11}\) can be enclosed by the
triangular identities

$$
P_j=a_0^{-1}\left(
 F_j-a_je_x-z_je_z
 -\sum_{h=0}^{j-1}\binom jh a_{j-h}P_h
\right),\qquad 0\le j\le11.
\tag{H.2}
$$

Every quantity on the right is either a saved successful enclosure or an
earlier value of (H.2). Directed interval operations therefore preserve the
actual finite primitive. Dependency may enlarge an enclosure; it cannot
justify narrowing it arbitrarily.

The original exact finite convention has \(P_j[N/2]=0\), and hence
\(F_j[N/2]=0\). Before using that exact identity, check that each raw saved
Nyquist interval contains zero. Apply the identity only to a decoded
consumption view. Preserve the original raw arrays and payload hashes.
The same exact parity and zero-mode conventions may be used on newly
computed unit primitives; they do not remove the true infinite Fourier tail.

No old finite column is evaluated again in (H.2), and no inverse FFT is
needed.

## 3. Exactly six new finite derivative columns

The original scalar germ is a polynomial of degree at most 20. Its unsaved
coefficient representation may be constructed on the same piece and
parameter box. Only the missing ordinary scalar derivatives \(12,\ldots,17\)
are evaluated from it:

$$
p^{(j)}(r)=
 \sum_{k=j}^{20}\frac{k!}{(k-j)!}\,p_k(r-r_c)^{k-j}.
\tag{H.3}
$$

Use exact integer or Arb-enclosed integer multipliers. In particular, do not
coerce a large factorial quotient to an unguarded binary64 number. Copy
the stored scalar derivatives \(0,\ldots,11\) unchanged.

The sine and cosine derivative states at the original 512 angles were not
saved. They are new supporting arrays, obtained from the saved scalar
derivatives and the six additions. For an ordinary derivative sequence \(b\),

$$
s_0=\sin b_0,\quad c_0=\cos b_0,\qquad
s_n=\sum_{j=0}^{n-1}\binom{n-1}{j}c_jb_{n-j},\quad
c_n=-\sum_{j=0}^{n-1}\binom{n-1}{j}s_jb_{n-j}.
\tag{H.4}
$$

Apply the original directed elementary-function enclosure and half-angle
identity \(\cos b-1=-2\sin^2(b/2)\). Differentiate the original tangent
formula only at the six missing output orders. The directed 512-point
Fourier transform is applied only to these six new tangent derivative
columns. The original finite primitive formula, all three components,
zero-mode convention, Nyquist convention, and reflection parity are kept.

The new \(P_{12},\ldots,P_{17}\), together with (H.2), give the six new
\(F_{12},\ldots,F_{17}\) through (H.1). The accepted original finite
columns and scalar derivatives remain unchanged. Store the new scalar,
tangent, Fourier and unit-primitive support needed to resume after any
interruption; a completed new column is not recomputed on resume.

## 4. Complete errors and bilinear means

Let \(\varepsilon_k(R)\) be an original complete error bound for the
\(k\)-th derivative of the same finite approximation on its accepted
complex rectangle. The disk of radius \(R\) about any allowed real root
lies in that rectangle. Cauchy's formula gives, for \(j=12,\ldots,17\),

$$
\varepsilon_j\le
 \min_{\substack{R\in\{1/10000,1/2000\}\\0\le k\le5}}
 \frac{(j-k)!}{R^{j-k}}\,\varepsilon_k(R).
\tag{H.5}
$$

Evaluate each complete quotient before selecting its upper endpoint, then
take the minimum of the independently valid upper bounds. Save every
candidate and its chosen index. The previously accepted errors
\(0,\ldots,11\) are copied, not recomputed.

Let \(M_i\) bound each component's complete finite Fourier \(\ell^1\) norm.
For the real bilinear zero convolution, with no complex conjugation,

$$
\langle F_i,F_j\rangle
 \in \langle F_{N,i},F_{N,j}\rangle
 +[-\Delta_{ij},\Delta_{ij}],\qquad
\Delta_{ij}
 =3(M_i\varepsilon_j+M_j\varepsilon_i+\varepsilon_i\varepsilon_j).
\tag{H.6}
$$

Reality of the exact finite zero convolution must be checked by enclosing
zero in its imaginary interval. Both signs of every retained Fourier mode
participate. The finite Nyquist identity is used only as in Section 2.

For all unordered positive pairs \(i\le j\), \(i+j\le18\), there are 81
required means. The original 36 means with \(i+j\le12\) are copied exactly;
only the remaining 45 are new. They give

$$
E_k=\sum_{j=0}^{k}\binom kj
       \langle F_{j+1},F_{k-j+1}\rangle,\qquad 11\le k\le16.
\tag{H.7}
$$

The original \(E_0,\ldots,E_{10}\) and all their complete error payments
remain the original successful records.

## 5. Append only the four intrinsic rows at orders 10 through 15

Set \(A(t)=\sum a_jt^j/j!\), \(\mathcal E(t)=\sum E_jt^j/j!\).
The three original positive gaps \(a_0>0\), \(E_0>0\) and
\(E_0-a_1^2>0\) select the same real branches. Use the exact identities

$$
K=-\frac{A''}{A\mathcal E}
  +\frac{A'\mathcal E'}{2A\mathcal E^2},\qquad
\beta=\frac{A'}A,\qquad
\gamma=\frac{\sqrt{\mathcal E}}A,\qquad
s=-A\sqrt{\frac{\mathcal E}{\mathcal E-(A')^2}}.
\tag{H.8}
$$

The degree-fifteen curvature coefficient requires \(a_{17}\) and
\(E_{16}\); hence the counts in Sections 3 and 4 suffice. Every inverse,
square-root and product helper is formed only with paid coefficients.
Missing higher coefficients are never silently replaced by zero.

Unsaved lower helper coefficients can be constructed to evaluate these
six new output orders. The intrinsic output records of orders zero
through nine are not reevaluated or replaced. Append only the 24 new
ordinary derivatives, retaining the original 54 low-order comparison
records and the original true-root branch checks.

The divided-curvature coefficients in the old-radial Taylor recurrence
obey the inherited exact convention

$$
K(r_*-\rho)=-\rho\,k(\rho),\qquad
k_q=\frac{(-1)^qK^{(q+1)}(r_*)}{(q+1)!}.
\tag{H.9}
$$

Preserve the original coefficients \(q=0,\ldots,8\); append \(q=9,\ldots,14\)
from the new curvature orders. The exact identity \(K(r_*)=0\) is justified
by the unchanged certified root, while the original nonzero-width
zeroth-curvature interval remains saved.

## 6. Actual-execution obligations

A successful consumer must identify both original natives and all actual
process receipts, retain the full original finite-point payload, errors,
means, energy rows, intrinsic rows and comparison records, and verify their
unchanged prefixes. Each newly accepted supporting stage or derivative row
is written before the next is attempted. Resume requires the same source,
manifest, runtime, root, parameter box and all complete original inputs.

The expected additions are six scalar derivative rows, six finite Fourier
derivative columns, six complete error orders, six finite norms, 45 complete
bilinear means, six energy derivatives and 24 intrinsic derivatives.
An actual receipt must give its real counts and any failure; this note
does not substitute expected counts for executed results.

The later extension of the Airy Taylor recurrence must independently
consume this complete result, preserve the original 75 natural stages,
and pay its own new degrees and full Fourier remainder. All original
physical seams, old-circle nonlocal words, independent means, weighted
positive ports, strong return and complete cutoff obligations remain.
