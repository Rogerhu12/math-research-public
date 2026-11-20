# R975 — the original balanced Kronecker integral heat recurrence

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved identities and integrality; no uniform unit assertion.**
This is the bare canonical Kronecker coefficient in the R973 execution
contract. It is not the eighteen-point, weight-one source of the older
`2026-11-15-sigma-Kronecker-weight-one-square-and-critical-convolution.md`.
The argument is symbolic. No new arithmetic was executed locally.

## 1. The original source and the universal polynomial

Let \(\sigma(z;g_2,g_3)\) be the canonical Weierstrass sigma function,
normalized by \(\sigma'(0)=1\) and
\[
-(\log\sigma)''=\wp,\qquad
\wp'^2=4\wp^3-g_2\wp-g_3.
\tag{975.1}
\]
In particular there is no freely chosen Gaussian. Put
\[
K(z,w)=\frac{\sigma(z+w)}{\sigma(z)\sigma(w)},\qquad
c_n(g_2,g_3)=[z^n w^{n-1}]K(z,w),
\quad n\ge1,
\]
\[
U_n(g_2,g_3)=n!(n-1)!c_n(g_2,g_3).
\tag{975.2}
\]
The original curve and differential are exactly
\[
E_0:y^2=x^3-1,\qquad dz=dx/(2y),\qquad
(g_2,g_3)=(0,4).
\tag{975.3}
\]
Thus R973's coefficient is \(c_n(0,4)\). Its modular weight is \(2n\);
the separate CM modular form under investigation there has weight \(n+1\).

The universal recurrence is
\[
\boxed{
\begin{aligned}
U_1&=0,\qquad U_2=-g_2/12,\\
U_n&=\mathcal L U_{n-1}
       -\frac{(n-1)(n-2)}{12}g_2U_{n-2}\quad(n\ge3),\\
\mathcal L&=6g_3\partial_{g_2}
                   +\frac{g_2^2}{3}\partial_{g_3}.
\end{aligned}}
\tag{975.4}
\]
In particular
\[
U_n\in\mathbf Z[1/6][g_2,g_3],
\qquad \operatorname{wt}(U_n)=2n
\quad(\operatorname{wt}g_2=4,\ \operatorname{wt}g_3=6).
\tag{975.5}
\]
All constants in (975.4) will be derived below from (975.1), rather than inferred
from initial coefficients.

## 2. Theta, the Gaussian, and every scaling constant

Temporarily use the lattice \(\Lambda_\tau=\mathbf Z+\tau\mathbf Z\),
and the standard normalized series \(E_2,E_4,E_6\) with constant term one.
Set \(x=2\pi i z\), and use the algebraically scaled sigma
\[
\sigma_{\rm alg}(x)=(2\pi i)\sigma_{\Lambda_\tau}(x/(2\pi i)).
\]
Its invariants are
\[
g_{2,\rm alg}=E_4/12,\qquad g_{3,\rm alg}=-E_6/216.
\tag{975.6}
\]
Indeed the usual lattice invariants are
\(4\pi^4E_4/3\) and \(8\pi^6E_6/27\); divide these by
\((2\pi i)^4\) and \((2\pi i)^6\), respectively. The minus sign in the
second equation is essential. The original point (975.3) therefore corresponds
in these algebraic invariants to \(E_4=0,E_6=-864\).

Use the odd theta series with algebraic argument
\[
\theta_\tau(x)=\sum_{m\in\mathbf Z}
 (-1)^m q^{(m+1/2)^2/2}e^{(m+1/2)x},
\qquad q=e^{2\pi i\tau}.
\]
The canonical sigma/theta relation is
\[
\sigma_{\rm alg}(x)
=e^{-E_2x^2/24}\frac{\theta_\tau(x)}{\theta_\tau'(0)}.
\tag{975.7}
\]
The sign can also be seen at the cusp: the normalized theta tends to
\(2\sinh(x/2)=x+x^3/24+\cdots\), and the canonical sigma has no cubic
term. Equation (975.7), not a choice to discard its Gaussian, gives
\[
K_{\rm alg}(x,y)=e^{-E_2xy/12}F_\tau(x,y),\qquad
F_\tau(x,y)=\frac{\theta_\tau'(0)\theta_\tau(x+y)}
 {\theta_\tau(x)\theta_\tau(y)}.
\tag{975.8}
\]

The classical Kronecker mixed heat equation, after this change of both
arguments and the residue-one normalization, is
\[
\Theta F_\tau=\partial_x\partial_yF_\tau,
\qquad \Theta=q\frac{d}{dq}=\frac{1}{2\pi i}\partial_\tau.
\tag{975.9}
\]
For clarity, in unscaled arguments its form is
\(2\pi i\,\partial_\tau\phi=\partial_z\partial_w\phi\).
Here \(F_\tau(x,y)=\phi(x/(2\pi i),y/(2\pi i))/(2\pi i)\), so the
three factors of \(2\pi i\) on the right match the left exactly.

Write \(a=E_2/12\). Substituting \(F=e^{axy}K\) into (975.9) gives
\[
\Theta K-a(x\partial_x+y\partial_y+1)K
 =\partial_x\partial_yK+(a^2-\Theta a)xyK.
\]
The Ramanujan identity \(\Theta E_2=(E_2^2-E_4)/12\) gives
\[
\boxed{\quad
\left(\Theta-\frac{E_2}{12}(x\partial_x+y\partial_y+1)\right)K
 =\partial_x\partial_yK+\frac{E_4}{144}xyK.
\quad}
\tag{975.10}
\]

## 3. The balanced coefficient and the initial polar term

Let \(\kappa_n=c_n(E_4/12,-E_6/216)\), and for this paragraph only set
\(\kappa_0=[x^0y^{-1}]K=1\). The coefficient \(\kappa_1\) is zero:
the canonical sigma has no cubic term. Extracting
\([x^{n-1}y^{n-2}]\) from (975.10) yields, for \(n\ge2\),
\[
n(n-1)\kappa_n
 =D_{2n-2}\kappa_{n-1}-\frac{E_4}{144}\kappa_{n-2},
\qquad D_k=\Theta-\frac{kE_2}{12}.
\tag{975.11}
\]
For \(n=2\), the last term uses the actual polar residue
\(\kappa_0=1\); consequently
\(\kappa_2=-E_4/288\). It must not be omitted by treating the entire
Kronecker function as a regular two-variable power series.

Multiplication by the two factorials gives
\[
U_2=-E_4/144,\qquad
U_n=D_{2n-2}U_{n-1}
 -\frac{(n-1)(n-2)E_4}{144}U_{n-2}.
\tag{975.12}
\]
On the full modular ring the Serre derivative is the derivation
\[
\mathcal D=-\frac{E_6}{3}\partial_{E_4}
                   -\frac{E_4^2}{2}\partial_{E_6}.
\]
Equations (975.6) imply
\(\mathcal Dg_2=6g_3\) and
\(\mathcal Dg_3=g_2^2/3\). Thus (975.12) is exactly (975.4).
Since the sigma coefficients are universal homogeneous polynomials in the
invariants, this proves the universal identity, not just a formula at one
complex lattice.

For explicit normalization, the first values from (975.4) are
\[
\begin{array}{c|l}
n&U_n\\ \hline
1&0\\
2&-g_2/12\\
3&-g_3/2\\
4&-g_2^2/8\\
5&-g_2g_3\\
6&-g_2^3/8-6g_3^2.
\end{array}
\tag{975.13}
\]
In particular \(U_3(0,4)=-2\), hence
\(c_3(0,4)=-2/(3!2!)=-1/6\), exactly the original R973 calibration.
These displayed identities are direct symbolic applications of the
recurrence; they do not constitute a new finite-prime window.

## 4. An exact Ramanujan-polynomial version

This alternative expression isolates what the outstanding nonvanishing
question actually asks. Let \(E,X,Y\) be formal variables of weights
\(2,4,6\), and put
\[
\mathcal R=\frac{E^2-X}{12}\partial_E
       +\frac{EX-Y}{3}\partial_X
       +\frac{EY-X^2}{2}\partial_Y,
\qquad
\mathcal F_n(X,Y)=\left.\mathcal R^{n-1}E\right|_{E=0}.
\tag{975.14}
\]
Then, for every \(n\ge1\),
\[
\boxed{\quad
U_n(g_2,g_3)=\frac1{12}\mathcal F_n(12g_2,-216g_3),
\qquad
c_n(0,4)=\frac{\mathcal F_n(0,-864)}{12n!(n-1)!}.
\quad}
\tag{975.15}
\]

Here is a direct algebraic proof, including the factor \(12\).
With \(H=2E\partial_E+4X\partial_X+6Y\partial_Y\), one has
\([\partial_E,\mathcal R]=H/12\). Homogeneity gives, for \(m\ge1\),
\[
\partial_E\mathcal R^mE
 =\frac{m(m+1)}{12}\mathcal R^{m-1}E.
\tag{975.16}
\]
Indeed commute \(\partial_E\) through the \(m\) copies of
\(\mathcal R\); the weights encountered are \(2,4,\ldots,2m\).
After evaluating \(E=0\), (975.16) gives
\[
\mathcal F_1=0,\quad\mathcal F_2=-X/12,
\qquad
\mathcal F_n=\mathcal D\mathcal F_{n-1}
 -\frac{(n-1)(n-2)X}{144}\mathcal F_{n-2}.
\tag{975.17}
\]
Its initial value is twelve times (975.12), proving (975.15).
Evaluation at \(E=0\) here is an algebraic operation on the universal
Ramanujan ring; it is not a claim that the holomorphic numerical value
\(E_2(\zeta)\) vanishes.

## 5. What follows at every prime, and what does not

For every \(p>3\), every pair of \(p\)-integral invariants, and
\(1\le n<p\), (975.4) gives
\[
c_n(g_2,g_3)\in\mathbf Z_{(p)}[g_2,g_3].
\tag{975.18}
\]
Both factorials in (975.2) are units, and the only denominator primes in
\(U_n\) are \(2,3\). This proves integrality of the complete balanced
coefficient independently of the first-pole cancellation in the R973
finite-sum formula. It does not assert that its individual sigma factors
are all integral beyond the first block.

If \(n=p-r\), \(1\le r<p\), Wilson's formula gives
\[
(p-r)!(p-r-1)!\equiv-\frac1{r!(r-1)!}\pmod p,
\]
and therefore, in the original frame,
\[
\boxed{\quad
c_{p-r}(0,4)\equiv-r!(r-1)!\,U_{p-r}(0,4)
 =-\frac{r!(r-1)!}{12}\mathcal F_{p-r}(0,-864)\pmod p.
\quad}
\tag{975.19}
\]
For the two actual rows, \(r=2\) or \(8\), this is a reduction to a
specified universal polynomial value. The multiplier is a unit for all
the original primes \(p\ge41\). The exact remaining question is
\[
\mathcal F_{p-2}(0,-864)\ne0
\quad\hbox{or}\quad
\mathcal F_{p-8}(0,-864)\ne0
\]
in its respective row. No assertion here answers it for all primes.
Homogeneity only implies that \(U_n(0,g_3)=0\) unless \(3\mid n\),
and otherwise reduces the value to a single rational coefficient times
\(g_3^{n/3}\); it supplies no unit statement about that coefficient.

In particular, neither a higher Ramanujan derivative known to be a unit
nor the original high sigma block rigidity can be inverted through a
zero coefficient modulo \(p\) to settle (975.19). The actual [R974](R974-original-balanced-coefficient-and-one-sided-CM-period-bridge.md)
bridge gives the single implication from a unit of this coefficient to a unit
of the original high CM congruence ideal, and then to a nonzero original
supersingular trace. The integrality proved here does not fulfill its unit
hypothesis. The primitive / Legendre same-label condition is separate.

## References and scope

- [R973 execution contract](../notes/R973-original-balanced-Kronecker-four-prime-execution-method.md):
  the original bare coefficient, the sigma differential equation, and the
  independent single-carry formula. Its four-prime computation is not
  repeated or used to prove (975.4).
- Francis Brown and Andrey Levin, *Multiple elliptic polylogarithms*,
  §3.4, Proposition 5(ii),
  https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2011/2011_063.pdf :
  the unscaled mixed heat equation. This is the same standard identity
  already cited in the old Kronecker note, used here on a different source.
- A. Levin, M. Olshanetsky, A. Zotov, *Noncommutative extensions of elliptic
  integrable Euler–Arnold tops and Painlevé VI equation*, J. Phys. A
  **49** (2016), 395202, Appendix A, (A.9), (A.10), and (A.17),
  https://publications.hse.ru/pubs/share/folder/unlb9g7zzk/191018193.pdf :
  theta normalization and the same heat identity.
- N. Matthes, *An algebraic characterization of the Kronecker function*,
  Research in the Mathematical Sciences **6** (2019), 24, §2.1,
  https://doi.org/10.1007/s40687-019-0186-0 :
  the algebraic-argument theta convention used in (975.7)–(975.9).

The new content is the exact balanced recurrence (975.4), its full scale
comparison, and its consequences (975.15), (975.18), (975.19). It proves neither
the varying adjoint value is a unit nor Serre uniformity.
