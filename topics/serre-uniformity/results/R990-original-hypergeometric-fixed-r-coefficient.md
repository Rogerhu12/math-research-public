# R990 — The original Gauss--Manin hypergeometric source and a fixed-r coefficient

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: literature_frontier; independently reviewed by root and legendre_shift, with the finite evaluation contract separately reviewed by handoff_audit.

**Status: proved identities and a quasilinear finite-field evaluation method; no uniform nonvanishing assertion.** The hypergeometric functions below are identified with the original balanced Kronecker coefficient by checking the actual Ramanujan differential equations and initial frame. The near-prime exponent is then reduced to the fixed exponent $r=2$ or $8$. A rational root-residue formula and the first resonance obstruction are explicit. None of these identities assumes that the target coefficient is a unit.

All calculations in this note are symbolic. No numerical mathematical computation was executed locally.

## 1. Original rows and notation

Retain the original two rows:
\[
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
(r,n)=
\begin{cases}
(2,p-2),&p\equiv11\pmod{12},\\
(8,p-8),&p\equiv5\pmod{12}.
\end{cases}
\tag{990.1}
\]
Put
\[
m=n/3,\qquad k=\lfloor p/12\rfloor,
\qquad \ell=(p+1)/3,\qquad b=(r+1)/3.
\tag{990.2}
\]
Thus $m=\ell-b<\ell$, and the endpoints are
\[
\begin{array}{c|c|c|c|c}
p&r&k&m&\ell\\\hline
12k+11&2&k&4k+3&4k+4\\
12k+5&8&k&4k-1&4k+2.
\end{array}
\tag{990.3}
\]
The inequalities $m<p$ and $3m+1=n+1<p$ will be used before taking any reduction.

The curve and sigma phase are the original positive model
\[
E_+:y^2=x^3+1,\qquad\omega=dx/(2y),\qquad
(g_2,g_3)=(0,-4).
\tag{990.4}
\]
Let
\[
c_n^+=[z_1^n z_2^{n-1}]
\frac{\sigma_+(z_1+z_2)}{\sigma_+(z_1)\sigma_+(z_2)}.
\tag{990.5}
\]
The new hypergeometric variable used below is denoted by $z$ and is unrelated to the two elliptic arguments $z_1,z_2$. In the original R974/R975 negative model $(g_2,g_3)=(0,4)$, the two rows satisfy $c_n^-=-c_n^+$, as fixed in R979. That phase is not changed inside the derivation.

## 2. An actual parametrization of the original Ramanujan solution

Over characteristic zero define
\[
A(z)={}_2F_1\left(\frac1{12},\frac7{12};\frac23;z\right),
\qquad
B(z)={}_2F_1\left(\frac5{12},\frac{11}{12};\frac43;z\right),
\tag{990.6}
\]
and set
\[
z=\frac{u^3}{432},\qquad
T=-\frac{uB(z)}{24A(z)}.
\tag{990.7}
\]
Both hypergeometric series have constant coefficient one, so (990.7) is an invertible formal change of parameter. The factor $-24$ is retained.

The two functions $A(z)$ and $z^{1/3}B(z)$ solve the same Gauss equation. Their Wronskian, normalized at zero, gives
\[
A(B+3zB')-3zA'B=\frac1{1-z}.
\tag{990.8}
\]
Indeed the Gauss parameters for $A$ have $c=2/3$ and $a+b=2/3$, so its Wronskian is $(1/3)z^{-2/3}(1-z)^{-1}$. Multiplication by $3z^{2/3}$ gives (990.8). Consequently
\[
\frac{dT}{du}=-\frac1{24(1-z)A^2},\qquad
\frac{du}{dT}=-24(1-z)A^2.
\tag{990.9}
\]

Now define
\[
X=12uA^4,\qquad Y=864A^6,\qquad
E=\frac{u^2A^2}{6}-2u^2(1-z)AA'.
\tag{990.10}
\]
These functions satisfy the exact Ramanujan system
\[
\frac{dE}{dT}=\frac{E^2-X}{12},\qquad
\frac{dX}{dT}=\frac{EX-Y}{3},\qquad
\frac{dY}{dT}=\frac{EY-X^2}{2},
\tag{990.11}
\]
with initial values
\[
(E,X,Y)|_{T=0}=(0,0,864).
\tag{990.12}
\]
Here is a direct check that fixes the source, rather than just matching one or two coefficients. The second and third equations in (990.11) follow by differentiating (990.10) and substituting (990.9). For the first, the exact error before using the Gauss equation is
\[
\frac{dE}{dT}-\frac{E^2-X}{12}
=144u(1-z)A^3
\left\{z(1-z)A''+\frac{2-5z}{3}A'-\frac7{144}A\right\}.
\tag{990.13}
\]
The braced expression is the Gauss equation for $A$, hence zero. Uniqueness of the characteristic-zero formal solution to (990.11) now identifies this with the actual Ramanujan flow of R975 at the original point (990.12).

In particular,
\[
\Delta(T)=\frac{X^3-Y^2}{1728}=(u^3-432)A^{12},\qquad
\Delta(0)=-432,
\tag{990.14}
\]
and $d\log\Delta/dT=E$. By R975's exact balanced coefficient formula,
\[
\boxed{\quad
\log\bigl((1-z)A(z)^{12}\bigr)
=12\sum_{n\ge1}(n-1)!c_n^+T^n.
\quad}
\tag{990.15}
\]
This is an equality of the original characteristic-zero formal series. It does not identify $T$ with a ring-class uniformizer or discard a crystalline coordinate correction. The original coefficient is identified through (990.11), not through an analogy between hypergeometric differential equations.

## 3. Exact Lagrange extraction and the fixed-r reduction

Let $n=3m>0$. Apply Lagrange inversion to (990.7) and (990.15). Since
\[
\frac d{du}\log\bigl((1-z)A^{12}\bigr)
=\frac{u^2}{144}
\left(12\frac{A'}A-\frac1{1-z}\right),
\tag{990.16}
\]
one gets
\[
12(n-1)!c_n^+
=\frac{(-24)^n}{144n}\,432^{-(m-1)}
[z^{m-1}]
\left(12\frac{A'}A-\frac1{1-z}\right)
\left(\frac AB\right)^n.
\tag{990.17}
\]
Here $(-24)^{3m}=(-13824)^m$, and $13824/432=32$. Thus the exact characteristic-zero formula is
\[
\boxed{\quad
c_n^+=\frac{(-32)^m}{4n!}
[z^{m-1}]
\left(12\frac{A'}A-\frac1{1-z}\right)
\left(\frac AB\right)^n.
\quad}
\tag{990.18}
\]
For example, the constant in parentheses is $12\cdot7/96-1=-1/8$, so $n=3$ gives $c_3^+=1/6$, with the original phase. This is a symbolic normalization check, not a new finite-prime computation.

Now take either original row and $n=p-r$. Every coefficient of $A$ and $B$ required through index $m$ is $p$-integral. In fact the denominator factors of $(2/3)_i$ and $(4/3)_i$ have numerators $3j+2$ and $3j+4$, respectively, with $0\le j<i\le m$. Their largest value is $3m+1=n+1<p$, while $i!$ is also a unit. This argument is made before reduction and includes the coefficient $A_m$ needed by $A'$.

We may therefore reduce (990.18) in the finite ring $\mathbb F_p[z]/(z^{m+1})$. Since $m<p$ and both series have constant term one,
\[
\left(\frac AB\right)^p\equiv1\pmod{p,z^{m+1}},
\qquad
\left(\frac AB\right)^{p-r}
\equiv\left(\frac BA\right)^r\pmod{p,z^{m+1}}.
\tag{990.19}
\]
No coefficient beyond the proved integral range is used here. Hence the large near-prime exponent has become the fixed exponent $r$ in the exact required truncation.

## 4. A rational-polynomial input and the precise stopping index

From now on all series in this section are over $\mathbb F_p$. The reduction of $B$ through degree $m$ is the actual polynomial
\[
\boxed{\quad
B_k(z)={}_2F_1\left(-k,k+\frac43;\frac43;z\right),
\qquad\deg B_k=k.
\quad}
\tag{990.20}
\]
For $p=12k+5$, the parameter $5/12$ reduces to $-k$; for $p=12k+11$, the parameter $11/12$ reduces to $-k$. The other parameter is $k+4/3$ in each case. All denominators through degree $m$ have already been shown to be units, so the numerator factor at index $k+1$ really makes every subsequent required coefficient zero.

Equivalently $B_k$ is the normalized Jacobi polynomial with parameters $(1/3,0)$, at argument $1-2z$. Its coefficients are supplied without any hypergeometric division beyond the allowed range by
\[
b_0=1,\qquad
b_i=b_{i-1}
\frac{(i-1-k)(3k+3i+1)}{i(3i+1)},
\qquad1\le i\le k.
\tag{990.21}
\]
Every displayed denominator and every numerator in this range is nonzero modulo $p$.

Write
\[
f=A/B_k,
\qquad H=\frac1{(1-z)B_k^2}.
\tag{990.22}
\]
The exact Wronskian (990.8) gives
\[
f-3zf'=H,\qquad f(0)=1.
\tag{990.23}
\]
Consequently the entire necessary part of $f$ can be formed from the rational function $H$:
\[
\boxed{\quad f_i=\frac{H_i}{1-3i},\qquad0\le i\le m<\ell=(p+1)/3.\quad}
\tag{990.24}
\]
The first zero denominator is at $i=\ell$. It is not crossed, assigned a value, or canceled after reduction.

Substitute $A'/A=B_k'/B_k+f'/f$ in (990.18), after (990.19). An integration by parts in the finite coefficient gives
\[
[z^{m-1}]
\left(12\frac{A'}A-\frac1{1-z}\right)f^{-r}
=[z^m]\left(
12z\frac{B_k'}{B_k}-\frac z{1-z}-\frac{12m}{r}
\right)f^{-r}.
\tag{990.25}
\]
Since $3m=p-r$, one has $-12m/r\equiv4\pmod p$. Put
\[
Q(z)=4+12z\frac{B_k'}{B_k}-\frac z{1-z},\qquad
\mathcal J_{p,r}=[z^m]Q(z)f(z)^{-r}.
\tag{990.26}
\]
Wilson's formula, with the original even values $r=2,8$, gives
$1/(p-r)!\equiv(r-1)!$. The final formula is
\[
\boxed{\qquad
c_{p-r}^+
\equiv \frac{(-32)^m(r-1)!}{4}\,\mathcal J_{p,r}
\pmod p.
\qquad}
\tag{990.27}
\]
The scalar in (990.27) is a unit for every prime in (990.1). Thus the remaining unit question is exactly $\mathcal J_{p,r}\ne0$ in this finite polynomial calculation. It has not been settled by deriving the formula.

## 5. The actual root residues and the known resonance unit

The endpoint values of $B_k$ are units:
\[
B_k(0)=1,\qquad
B_k(1)=\frac{(-1)^k k!}{(4/3)_k}\in\mathbb F_p^\times.
\tag{990.28}
\]
The second formula is the terminating Vandermonde identity. Its denominator factors are again strictly below $p$.

The roots of $B_k$ are simple and avoid $0,1$. Indeed $B_k$ solves
\[
z(1-z)B_k''+\left(\frac43-\frac73z\right)B_k'
-\frac{55}{144}B_k=0\pmod p.
\tag{990.29}
\]
At an ordinary point, a repeated root would force all derivatives through degree $k<p$ to vanish by this equation, contradicting $B_k(0)=1$. The endpoints are excluded by (990.28).

For a root $\gamma$ of $B_k$ put
\[
\lambda_\gamma=
\frac1{9\gamma^2(1-\gamma)B_k'(\gamma)^2}.
\tag{990.30}
\]
These are nonzero elements of the splitting field, but no order or positivity is assigned to them.

Consider the rational differential, with $z=u^3/432$,
\[
\mathcal R(u)\,du=
\frac{du}{u^2(1-z)B_k(z)^2}.
\tag{990.31}
\]
Its poles over a root $\gamma$ of $B_k$ are double poles at the three points $a^3=432\gamma$. Their double-pole coefficients are $\lambda_\gamma$, and their residues vanish. To check the latter directly, in the $z$ variable the differential is a nonzero constant times
$z^{-4/3}(1-z)^{-1}B_k^{-2}dz$. The logarithmic derivative of the prefactor is
\[
-\frac4{3z}+\frac1{1-z}
=-\frac{4/3-7z/3}{z(1-z)},
\]
which is exactly $B_k''/B_k'$ at a root, by (990.29). This is the cancellation of the simple-pole coefficient.

There is a double pole of coefficient one at $u=0$, and the three cusp poles $c^3=432$ have residues
\[
\operatorname{Res}_{u=c}\mathcal R(u)du
=-\frac1{3cB_k(1)^2}.
\tag{990.32}
\]
There is no polynomial part at infinity. Hence the full partial-fraction identity is
\[
\mathcal R(u)=\frac1{u^2}
+\sum_{B_k(\gamma)=0}\ \sum_{a^3=432\gamma}
\frac{\lambda_\gamma}{(u-a)^2}
-\frac1{3B_k(1)^2}\sum_{c^3=432}\frac{1/c}{u-c}.
\tag{990.33}
\]

Since $d(f(z)/u)/du=-\mathcal R(u)$, integration at the origin, with its fixed leading term $1/u$, gives the exact required truncation
\[
\boxed{\quad
f(z)=1+3\sum_{B_k(\gamma)=0}
\lambda_\gamma\frac{z}{z-\gamma}
-\frac1{B_k(1)^2}
\sum_{i=1}^{m}\frac{z^i}{3i-1}
\pmod{z^{m+1}}.
\quad}
\tag{990.34}
\]
For example, grouping the three rational poles over $\gamma$ gives
$\sum_{a^3=432\gamma}u/(u-a)=3z/(z-\gamma)$. Grouping the normalized cusp logarithms $\log(1-u/c)/c$ gives the displayed coefficients $-z^i/(3i-1)$. All such denominators are units in the required range. Formula (990.34) is a finite-field trace expression for the rational part together with an explicit finite logarithm. It does not turn the nonlinear coefficient in (990.26) into a sum known to be nonzero.

There is a useful exact boundary at the first excluded index:
\[
\boxed{\quad H_\ell=B_k(1)^{-2}\ne0,\qquad\ell=(p+1)/3.\quad}
\tag{990.35}
\]
For a proof, apply the residue theorem to $z^{-\ell-1}H(z)dz$. At every root of $B_k$ its residue is zero: modulo $p$, the logarithmic derivative of $z^{-\ell-1}(1-z)^{-1}$ is the same $-4/(3z)+1/(1-z)$ used above. The residue at $z=0$ is $H_\ell$; the residue at $z=1$ is $-B_k(1)^{-2}$; there is no residue at infinity. This proves (990.35).

The value (990.35) explains why one cannot extend (990.24) across $\ell$ by dividing by zero. It is a known nonzero obstruction at the next resonance. It is not a proof that the different nonlinear coefficient at $m=\ell-1$ or $\ell-3$ in (990.26) is nonzero.

## 6. Quasilinear evaluation contract and scope

Formula (990.27) requires only the following finite operations for each new prime:

1. Form the degree-$k$ polynomial $B_k$ by (990.21).
2. Invert $(1-z)B_k^2$ through degree $m$ to obtain $H$.
3. Set $f_i=H_i/(1-3i)$ for $0\le i\le m$.
4. Form $Q$ from (990.26), compute the fixed power $f^{-r}$ through degree $m$, and extract $\mathcal J_{p,r}$.
5. Multiply by the original unit in (990.27); negate only when explicitly comparing with the $E_-$ phase.

The root decomposition of Section 5 is not needed computationally. With polynomial multiplication cost $M(d)$, the inversions and fixed powers use $O(M(p))$ field operations and $O(p)$ coefficients of memory; the scalar recurrences and divisions are linear in $p$. There are no arrays of length proportional to $p^2$. An independent original sigma or Chazy consumer remains a separate verification channel; this note does not claim that one has already been run.

Together with R988, the formula supplies a concrete coefficient for the same original high Hurwitz coordinate and the original high-trace unit question. It does not identify different Robert mirror pairs, remove the fixed original scalar phases, or prove the target unit. The unproved assertion is specifically
\[
[z^{\ell-b}]
\left(4+12zB_k'/B_k-z/(1-z)\right)
\left(\sum_{i=0}^{\ell-b}
\frac{[z^i]((1-z)B_k^2)^{-1}}{1-3i}\,z^i\right)^{-r}\ne0.
\tag{990.36}
\]
The nonzero cusp residues, the simple Jacobi roots, and the resonance unit in Section 5 are all compatible with cancellation in this specified coefficient; no finite-field norm-positivity argument is used.

## Dependencies

- [R975](R975-original-balanced-Kronecker-integral-heat-recurrence.md) for the exact original Ramanujan polynomial and balanced sigma normalization.
- [R979](R979-balanced-Kronecker-and-normalized-discriminant-Taylor-source.md) for the $E_+/E_-$ phase and the normalized discriminant source; the present source equality is independently fixed by (990.11)--(990.13).
- [R987](R987-original-Poincare-Cartier-identity-and-first-denominator.md) and [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md) for the actual Cartier connection identity and the exact original high Hurwitz / balanced coefficient comparison. Neither is needed to prove (990.27), only to transport its interpretation to the original high trace.
- The hypergeometric, Wronskian, and terminating Vandermonde identities used above are supplied with their parameters and their algebraic role. The actual differential-system identification and all reductions are proved in the text; no ordinary-reduction interpolation theorem is invoked.

- NIST Digital Library of Mathematical Functions, [15.10.1–15.10.3](https://dlmf.nist.gov/15.10), for the Gauss equation, the second solution, and its Wronskian, and [15.4.24](https://dlmf.nist.gov/15.4.E24), for the terminating Chu–Vandermonde identity. These primary formulas were checked directly; the original source scaling, finite integral reduction, residues, and target coefficient are proved above.
