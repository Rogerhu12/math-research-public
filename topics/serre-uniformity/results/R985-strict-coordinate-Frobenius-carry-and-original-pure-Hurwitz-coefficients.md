# R985 — The strict-coordinate Frobenius carry in the original pure Hurwitz source

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: legendre_shift; independently reviewed by root.

**Status: proved source identities; no mixed-to-pure scalar or nonvanishing assertion.**
The rational Cartier primitive in R984 gives the original low balanced
coefficient. At the high pure indices, changing from its actual parameter
to R978's strict Lubin–Tate parameter introduces an additional integral
Frobenius carry. This note identifies that carry, proves its exact
reduction and first nonzero term, and gives the corrected pure-coefficient
formula. In particular it corrects the tempting but false omission of
the carry after the coordinate change. All calculations are symbolic.

## 1. Fixed parameters and the two genuine Frobenius decompositions

Use the original curve and differential
\[
E_+:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad
t=-x/y,\qquad g_2=0,\quad g_3=-4.
\tag{985.1}
\]
Let \(p\ge41\), \(p\equiv5\pmod6\), \(q=p^2\),
\(A=W(\mathbb F_{p^2})\), and let \(\varphi\) be arithmetic Frobenius
on \(A\). Write
\[
\omega=f_E(t)\,dt,\qquad
l_E(t)=\int_0^t\omega,
\qquad
f_E=\frac{x^3+1}{x^3-2}.
\tag{985.2}
\]
The expansion \(f_E(t)\) belongs to \(A[[t]]\) and has constant term
one. For the strict integral isomorphism of R978 put
\[
t=g(T),\qquad g\in T+T^2A[[T]],\qquad
L(T)=l_E(g(T)).
\tag{985.3}
\]
Here \(L\) is the logarithm of the Lubin–Tate group associated with
\[
F_0(T)=-pT+T^q,\qquad L(F_0(T))=-pL(T),
\qquad L(T)=T+O(T^q).
\tag{985.4}
\]
No change to the source differential or the derivative \(g'(0)=1\)
is made.

Keep the canonical pure coefficients and zeta function
\[
\zeta(z)=\frac1z-\sum_{N\ge4}\mathcal G_Nz^{N-1},
\qquad \zeta=\sigma'/\sigma.
\tag{985.5}
\]
R984 applies Guerzhoy's strict-invariant Frobenius decomposition with
the weight-two coefficient zero at this CM point. Its actual-parameter
and strict-parameter representatives are, respectively,
\[
R_t(t)=\zeta(l_E(t))-\frac{\mu}{p}l_E^\varphi(t^p)
\in t^{-1}+tA[[t]],
\]
\[
R_T(T)=\zeta(L(T))-\frac{\mu}{p}L^\varphi(T^p)
\in T^{-1}+TA[[T]].
\tag{985.6}
\]
The same \(\mu\in A\) occurs in both formulas. With R980's original
Eisenstein normalization,
\[
\beta=\frac{\overline{E_{p+1}(E_+,\omega)}}{12}
\in\mathbb F_p^\times,\qquad \overline\mu=-\beta.
\tag{985.7}
\]

Strict invariance in (985.6) is invariance of the two crystalline
coefficients. It does not assert equality of the two regularized
Laurent series after substituting \(t=g(T)\).

## 2. The exact carry and its reduction

Define
\[
\delta_g(T)=\frac{g(T)^p-g^\varphi(T^p)}p\in A[[T]],
\tag{985.8}
\]
\[
\mathcal C_g(T)=
\frac{l_E^\varphi(g(T)^p)-L^\varphi(T^p)}p.
\tag{985.9}
\]
Integrality in (985.8) follows from coefficient Frobenius:
\(g(T)^p\equiv g^\varphi(T^p)\pmod p\). The difference of the two
series in (985.6) is the exact characteristic-zero identity
\[
\boxed{\quad
R_T(T)=R_t(g(T))+\mu\mathcal C_g(T).
\quad}
\tag{985.10}
\]
Indeed \(L^\varphi(T^p)=l_E^\varphi(g^\varphi(T^p))\); the other
argument is \(g(T)^p\), which need not be equal to
\(g^\varphi(T^p)\).

Here is a direct integral divided-difference argument, valid in all
degrees. Suppose \(l(U)=\sum_{m\ge1}b_mU^m/m\) with \(b_m\in A\),
and let \(V,\delta\) have positive \(T\)-order. Then
\[
\frac{l(V+p\delta)-l(V)}p
=\sum_{m\ge1}b_m\sum_{j=1}^m
\binom{m-1}{j-1}\frac{p^{j-1}}j
V^{m-j}\delta^j.
\tag{985.11}
\]
Every coefficient is integral. For \(j\ge2\) and \(p>2\),
\(v_p(p^{j-1}/j)\ge1\). The reduction is consequently just
\(\overline\delta\,\overline{l'(V)}\). Apply this with
\(l=l_E^\varphi\), \(V=g^\varphi(T^p)\), and
\(\delta=\delta_g\). This proves both the integrality of (985.9) and
the full formal identity
\[
\boxed{\quad
\overline{\mathcal C_g}
=\overline{\delta_g}\,
\overline{f_E^\varphi(g^\varphi(T^p))}
=\overline{\delta_g}\,f_E(\overline g(T))^p.
\quad}
\tag{985.12}
\]
In the last expression \(f_E\) means its reduction. There is no
unproved omission of a term divisible by \(p\) before division by
\(p\): that division is exactly (985.11).

One can simplify (985.12) further. The invariant differential of the
integral Lubin–Tate formal group implies \(L'(T)\in A[[T]]\).
Differentiating (985.4) gives
\[
L'(T)=L'(F_0(T))(1-pT^{q-1}).
\]
After reduction, \(H(T)=\overline{L'}(T)\) therefore satisfies
\(H(T)=H(T^q)\). Since \(H(0)=1\), comparing any hypothetical least
positive nonzero coefficient forces a contradiction. Hence
\[
\overline{L'}=1,\qquad
f_E(\overline g(T))\overline g'(T)=1,
\]
\[
\boxed{\quad
\overline{\mathcal C_g}(T)
=\frac{\overline{\delta_g}(T)}{\overline g'(T)^p}.
\quad}
\tag{985.13}
\]
This is an equality of full formal series over the residue field, not
just a low-degree truncation. The coordinate \(g\) remains the fixed
strict isomorphism; (985.13) does not replace it by an arbitrary
parameter with derivative one.

## 3. Combining the actual rational primitive with the carry

Let \(J\in k(E_+)\), \(k=\mathbb F_{p^2}\), be a normalized rational
Cartier primitive supplied by R984:
\[
dJ=-x\omega+\beta t^{p-1}f_E^p\,dt,
\qquad J=t^{-1}+t\,k[[t]]
\quad\text{at the origin}.
\tag{985.14}
\]
For some \(h\in tk[[t]]\), that result gives
\[
\overline{R_t}(t)-J(t)=h(t)^p.
\tag{985.15}
\]
Substitution into (985.10), with the calibrated sign (985.7), gives
\[
\boxed{\quad
\overline{R_T}(T)
=J(\overline g(T))-
\beta\overline{\mathcal C_g}(T)
+h(\overline g(T))^p.
\quad}
\tag{985.16}
\]
The \(p\)th-power remainder in (985.16) has only degrees divisible
by \(p\). The carry need not have that property.

The connection itself provides a separate scale and sign check.
Differentiating (985.8) before reducing gives
\[
\delta_g'
=g^{p-1}g'-T^{p-1}(g')^\varphi(T^p).
\]
Since the derivative of \(\overline g'^p\) is zero, (985.13) implies
\[
\boxed{\quad
\overline{\mathcal C_g}'
=\left(\frac{\overline g}{\overline g'}\right)^{p-1}
-T^{p-1}.
\quad}
\tag{985.17}
\]
On the other hand, pulling (985.14) back by \(\overline g\) and using
\(f_E(\overline g)\overline g'=1\) gives
\[
\frac d{dT}J(\overline g(T))
=-x(\overline g(T))+
\beta\left(\frac{\overline g}{\overline g'}\right)^{p-1}.
\]
Thus the corrected primitive
\[
\mathscr R_g(T)=J(\overline g(T))-
\beta\overline{\mathcal C_g}(T)
\]
has exactly the strict-coordinate connection
\[
\boxed{\quad
\mathscr R_g'(T)=-x(\overline g(T))+\beta T^{p-1}.
\quad}
\tag{985.18}
\]
Direct differentiation of \(R_T\) in (985.6) has the same reduction.
This also explains why a carry is required: it changes the actual
parameter's Frobenius connection term into the strict parameter's term.

## 4. The exact high pure-coefficient formula

Let
\[
6\mid N,\qquad 4\le N<q-1,
\qquad p\nmid N-1.
\tag{985.19}
\]
The pure coefficient \(\mathcal G_N\) is \(p\)-integral, and
\[
\boxed{\quad
-\overline{\mathcal G_N}
=[T^{N-1}]\left(
J(\overline g(T))-
\beta\overline{\mathcal C_g}(T)\right).
\quad}
\tag{985.20}
\]

To verify the precise range, replacing \(L(T)\) by \(T\) in the pole
\(1/L(T)\) first changes degree \(q-2\). Replacing it in the regular
part of (985.5) changes only still higher degrees. Thus for
\(N-1<q-2\), the coefficient of \(T^{N-1}\) in \(\zeta(L(T))\)
is exactly \(-\mathcal G_N\). Also
\(L^\varphi(T^p)=T^p+O(T^{pq})\). The hypothesis
\(p\nmid N-1\) excludes the only possible correction degree \(p\)
in this range. Hence the coefficient in \(R_T\) is exactly
\(-\mathcal G_N\); its integrality follows already from (985.6).
Finally the last term of (985.16) contributes zero because its degrees
are divisible by \(p\). This proves (985.20), including its minus sign.

All four actual indices of R978/R980 meet (985.19). With
\(r\in\{2,8\}\), \(a=r+1\), and \(n=p-r\), their residues are
\[
\begin{array}{c|c|c}
\text{label}&N&N-1\pmod p\\ \hline
\mathrm{low}&a(p-1)&-a-1\\
\mathrm{low\ star}&a(p-1)+p+1&-a\\
\mathrm{high}&n(p-1)&r-1\\
\mathrm{high\ star}&np+a&r.
\end{array}
\tag{985.21}
\]
None of these residues is zero in the original range. The bounds and
the exact source indices are the ones already established in R981;
they are not replaced by pure coefficients of a different model.
Formula (985.20) is also unchanged by replacing \(J\) by another
normalized rational primitive: their difference is a rational
\(p\)th power, whose composition with \(\overline g\) contributes
only degrees divisible by \(p\).

## 5. The first carry is nonzero at every original prime

The original Laurent expansion begins
\[
x(z)=z^{-2}-\frac17z^4+O(z^{10}),\qquad
y(z)=-z^{-3}-\frac27z^3+O(z^9).
\]
This is R981's \(g_3=-4\) normalization. Since \(t=-x/y\),
\[
t(z)=z-\frac37z^7+O(z^{13}).
\]
Using \(L(T)=T+O(T^q)\), with \(q>13\), gives
\[
g(T)=T-\frac37T^7+O(T^{13}).
\tag{985.22}
\]
The \(\mu_6\)-equivariance of the original strict isomorphism ensures
that its degrees are one modulo six.

The linear coefficient of \(g\) is exactly one, so the degree-\(p\)
terms in \(g(T)^p-g^\varphi(T^p)\) cancel exactly. The first mixed
term in the power \(g(T)^p\) is
\(p(-3/7)T^{p+6}\). The corresponding first nonlinear term of
\(g^\varphi(T^p)\) has degree \(7p>p+6\), so it cannot cancel this
term. No lower degree is available from the equivariant expansion.
Therefore
\[
\overline{\delta_g}(T)
=-\frac37T^{p+6}+O(T^{p+12}).
\]
The factor \(\overline g'^{-p}\) in (985.13) has constant term one
and no nonconstant term before degree \(6p\). Consequently
\[
\boxed{\quad
\overline{\mathcal C_g}(T)
=-\frac37T^{p+6}+O(T^{p+12}).
\quad}
\tag{985.23}
\]
This is nonzero for every \(p\ge41\). As another check, (985.17)
has leading term \(-18T^{p+5}/7\), which is the derivative of
(985.23) in characteristic \(p\).

The first affected pure index is \(N=p+7\). It is divisible by six,
lies below \(q-1\), and satisfies \(N-1\equiv6\not\equiv0\pmod p\).
At this index (985.20) reads
\[
\boxed{\quad
-\overline{\mathcal G_{p+7}}
=[T^{p+6}]J(\overline g(T))+\frac{3\beta}{7}.
\quad}
\tag{985.24}
\]
The additional term is a unit. It cannot be removed by changing the
normalized rational primitive, since that only changes \(p\)-divisible
degrees. Thus an uncorrected formula using \(J(\overline g)\) alone
already fails at this explicit first index, without any prime scan.
This statement says that the correction is nonzero; it does not say
that either summand or their sum in (985.24) is always nonzero.

## 6. Compatibility with the low balanced rectangle

R984 proves, for the original \(n=p-r\le p-2\),
\[
\overline{c_n^+}
=[T^n]\sum_{j=0}^n
\frac{J(\overline g(T))^{n-j}}{(n-j)!}
\overline L_j(\overline g(T)),
\tag{985.25}
\]
where \(L_j\) are the actual rational connection functions defined by
\(e^{-\zeta(z)W}\sigma(z+W)/(\sigma(z)\sigma(W))
=\sum L_j(z)W^{j-1}\).

The carry does not invalidate this low formula. Replacing
\(J(\overline g)\) by \(\mathscr R_g\) multiplies the finite kernel
by \(\exp(-\beta\overline{\mathcal C_g}W)\), which differs from one
first in degree \(T^{p+6}W\). The full finite kernel, rather than
each summand in (985.25), has only a simple \(T\)-pole by R984.
The correction therefore first affects \(T\)-degree at least \(p+5\),
well outside \(n\le p-2\). All exponential factorials involved have
index below \(p\). Consequently (985.25) also holds with
\(\mathscr R_g\) in place of \(J(\overline g)\).

We now have one accurately corrected strict-coordinate source for the
two types of coefficient: a linear high coefficient in (985.20), and
a nonlinear low coefficient with the genuine connection functions in
(985.25). These facts do not identify the two functionals or imply
their simultaneous nonvanishing. In particular the failed common
scalar comparison tested in R981/R983 is not reinstated by the shared
source. The pure high unit, the balanced near-\(p\) unit, and the
original same-label primitive/Legendre requirement remain separate
questions.

## Dependencies

- [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md):
  the actual-parameter Frobenius decomposition, its sign, the rational
  primitive, and the finite balanced kernel. This note supplies the
  strict-coordinate carry that is not part of its low rectangle.
- [R978](../results/R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md):
  the original strict integral Lubin–Tate isomorphism and normalization
  of \(\mathcal G_N\).
- [R980](../results/R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md):
  the same differential, \(\beta\), and the four actual mirror indices.
- [R981](../results/R981-original-pure-Hurwitz-residue-compression.md):
  the source Laurent coefficient and original-index range, reused here
  without executing its consumer.
- P. Guerzhoy, *On the p-adic values of the weight two Eisenstein series
  for supersingular primes*, Research in the Mathematical Sciences
  **12** (2025), article 64; equation (4), Proposition 1, Corollary 1,
  equation (14), and Theorem 1. [Primary author manuscript](https://arxiv.org/pdf/2403.02592).
  The external input used here is its strict-invariant formal-group
  decomposition; the carry, divided-difference proof, derivative check,
  and explicit first discrepancy are proved above.
