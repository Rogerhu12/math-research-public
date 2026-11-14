# R687 — A direct characteristic-p computation of the actual two coefficients

## Statement and scope

For every prime $p\ge41$, $p\equiv5\pmod6$, the attached algorithm computes
the two coefficients $r_2,r_3$ of R605 directly in $\mathbf F_p$.  It does
not use either the R658 comparison with $C_p$ or the R683 comparison with
$C_{p-3}$ to obtain the coefficients.  It therefore gives an independent
way to check any putative zero produced by the Kronecker algorithm R685.

The exact formula is

$$
\begin{aligned}
M_2&=(p^2-p-2)/6,& M_3&=(p^2-4p+1)/6,\\
A(w)&=\frac{1+34w-8w^2}{1-228w+48w^2-64w^3},&
C(w)&=(1-w)^{-1/2},\\
Z(w)&=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(6j+1)}w^j,&
\mathcal T(w)&=\frac{Z(w^p)}{Z(w)},\\
r_2&=[w^{M_2}]AC\mathcal T,&
r_3&=[w^{M_3}]AC\mathcal T^4.
\end{aligned}
\tag{687.1}
$$

Here these are the actual R605 coefficients of $R_-$, with its specified
integral logarithm truncation.  In particular this calculation does not
replace the actual $c_1$ point by the distinct $c_0$ point.

## 1. Cancelling the logarithm denominators exactly

Put $M=M_2$.  Then

$$
2M<p^2,\qquad 6M+1=p^2-p-1<p^2.
\tag{687.2}
$$

For $0\le n\le2M$ define the integer unit part

$$
U_n=\frac{n!}{p^{\lfloor n/p\rfloor}}\in\mathbf Z_{(p)}^\times.
\tag{687.3}
$$

There are no multiples of $p^2$ in this range.  Consequently its reductions
can be computed with

$$
U_0=1,\qquad
U_n\equiv U_{n-1}
\begin{cases}
n,&p\nmid n,\\ n/p,&p\mid n
\end{cases}\pmod p.
\tag{687.4}
$$

For $0\le j\le M$ set

$$
v_j=\lfloor2j/p\rfloor-2\lfloor j/p\rfloor\in\{0,1\},
\qquad b_j=U_{2j}U_j^{-2}\in\mathbf F_p^\times.
\tag{687.5}
$$

Legendre's factorial formula, using (687.2), gives the exact equality in
$\mathbf Z_{(p)}$

$$
\binom{2j}{j}=p^{v_j}\frac{U_{2j}}{U_j^2}.
\tag{687.6}
$$

Write $6j+1=p^{d_j}a_j$ with $p\nmid a_j$.  By (687.2), $d_j$ is either
zero or one.  If $d_j=1$ and $j=sp+t$ with $0\le t<p$, then

$$
6t+1=5p,\qquad t=(5p-1)/6>p/2,
\tag{687.7}
$$

because $p\equiv5\pmod6$.  This proves $v_j=1$ whenever $d_j=1$.
In particular $v_j\ge d_j$ throughout the calculation; the logarithm
coefficient is integral without assuming it.

The required reductions are thus

$$
[w^j]C=\begin{cases}4^{-j}b_j,&v_j=0,\\0,&v_j=1,\end{cases}
\qquad
[w^j]Z=\begin{cases}4^{-j}b_ja_j^{-1},&v_j=d_j,\\0,&v_j>d_j.
\end{cases}
\tag{687.8}
$$

Every division in (687.8) is by a unit.  In particular, a vanishing
denominator $6j+1$ is cancelled *before* reduction, with its matching
binomial factor $p$ removed exactly by (687.6).  No residue modulo $p$
is divided by $p$, and no unknown higher precision is discarded.

## 2. Finite polynomial arithmetic and sparse final sums

Work in $\mathbf F_p[w]/(w^{M+1})$.  The series $Z$ and the denominator
of $A$ both have constant term one, so their inverses are uniquely
defined in this finite ring.  Compute

$$
Q_2=AC/Z\pmod{w^{M_2+1}},\qquad
Q_3=AC/Z^4\pmod{w^{M_3+1}}.
\tag{687.9}
$$

With $z_j=[w^j]Z$ and $h_j=[w^j]Z^4$, formula (687.1) becomes

$$
\begin{aligned}
r_2&=\sum_{j=0}^{\lfloor M_2/p\rfloor}
       [w^{M_2-pj}]Q_2\,z_j,\\
r_3&=\sum_{j=0}^{\lfloor M_3/p\rfloor}
       [w^{M_3-pj}]Q_3\,h_j.
\end{aligned}
\tag{687.10}
$$

The second equality uses $Z(w^p)^4=(Z(w)^4)(w^p)$, an identity before
reduction.  Thus only $Z^4$ through degree $\lfloor M_3/p\rfloor$ is
needed in the final sparse sum.  All other truncations are legitimate
because the factors are power series with no negative exponents.

Equations (687.3)--(687.10), together with the already proved actual
coefficient identity R605, prove the algorithm.  Storage is $O(p^2)$
field elements.  Preparation takes $O(p^2)$ elementary field operations;
the remaining operations are a fixed number of finite-series inversions
and truncated polynomial products.  The implementation delegates these
exact operations to FLINT, using its `nmod_poly` type.

## 3. Implementation and executed checks

The standalone script is `R687_direct_R605_flint.py`.  It needs Python
and `python-flint`.  Its interface is

```bash
python R687_direct_R605_flint.py --prime 1013 --output direct1013.json
```

The JSON certificate records the raw $r_2,r_3$, both complete lists of
sparse summands in (687.10), all cancelled-denominator indices, the input
prime, the source SHA256, and runtime.  It additionally reports the
values *predicted* for $C_p,C_{p-3}$ by R658/R683; those comparisons do
not enter the computation of $r_2,r_3$.

Two actual executions were made, one small comparison and one larger
runtime measurement.  Both primes lie in the remaining classes:

| $p$ | $r_2$ | $r_3$ | predicted $C_p$ | predicted $C_{p-3}$ |
| ---: | ---: | ---: | ---: | ---: |
| 101 | 88 | 95 | 51 | 18 |
| 1013 | 964 | 778 | 986 | 104 |

The $p=101$ values match the separate R685 Kronecker calculation;
$C_{98}\equiv18$ was also obtained from the exact characteristic-zero
rational calculation.  The second row is a new direct coefficient
calculation, not an assertion of an independent Kronecker replay.
On the development machine the direct computations took approximately
0.010 and 1.61 seconds respectively.  No local prime scan was run.

These two rows do not establish nonvanishing for all primes or all
remaining primes.  The role of the result is an exact independent
algorithm and its proof, suitable for replaying any finite candidate
exception produced by the public-repository Actions scan.

## Dependencies

- R605, specifically its integral truncation and formula (605.21).
- R658 and R683 only for the optional displayed conversion to $C_p$ and
  $C_{p-3}$; neither is needed for the raw coefficient algorithm.

