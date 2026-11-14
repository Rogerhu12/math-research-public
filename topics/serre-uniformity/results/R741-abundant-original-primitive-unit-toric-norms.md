# R741 — A positive proportion of the original primitive toric norms are units

Date: 2026-11-14. Status: **proved**.

R740's exact even valuation, combined with the full-family archimedean
bound of R733, gives many actual primitive labels with unit finite norm.
This uses the same $N_h$, split vector, CM torus, and chosen $p$-adic
embedding as those results.

## 1. Statement

Let $p\ge41$ be prime, $p\equiv2,5\pmod9$, and put
$$
n=p+1,\quad
\mathcal H^*=\{1\le h<n:h\equiv1\pmod6,\ (h,n)=1\},\quad
g=|\mathcal H^*|=\frac{\varphi(n)}2.
$$
Define
$$
U_p=\#\{h\in\mathcal H^*:v_p(N_h)=0\},\qquad
\varepsilon_p=\frac{\log(5(2+\log_2p))}{\log p}.
$$
Then
$$
\boxed{\frac{U_p}{g}>\frac{1-\varepsilon_p}{2}.}
\tag{741.1}
$$
In particular,
$$
\boxed{
\begin{array}{c|c}
\text{range}&\text{proportion of unit original norms}\\
p\ge2^{64}&U_p/g>3/7\\
p\ge2^{160}&U_p/g>15/32\\
p\ge2^{512}&U_p/g>125/256
\end{array}}
\tag{741.2}
$$
and along the allowed primes
$$
\liminf_{p\to\infty}\frac{U_p}{g}\ge\frac12.
\tag{741.3}
$$
No Mordell–Weil nonvanishing or $M_2$ nonvanishing assumption is needed.

## 2. The exact integer norm and its selected valuations

Set $F_0=\mathbb Q(\zeta_n)^+$. R730 and R733 prove that the original
$N=N_1$ is a nonzero totally positive algebraic integer in $F_0$.
The $N_h$ for $h\in\mathcal H^*$ are exactly all its conjugates, counted
with the embeddings of $F_0$, whether or not $N$ generates that field.

Indeed, every unit residue modulo $n$ is $1$ or $5$ modulo six.
Exactly one representative in each pair $\{h,-h\}$ is $1$ modulo six.
Thus this is the complete real cyclotomic embedding list, with no
selected conjugate omitted.

Its rational norm is therefore a positive integer
$$
A=\operatorname N_{F_0/\mathbb Q}(N)
 =\prod_{h\in\mathcal H^*}N_h\in\mathbb Z_{>0}.
\tag{741.4}
$$
Since $p\nmid n$ and $p\equiv-1\pmod n$, Frobenius acts as complex
conjugation on $\mathbb Q(\zeta_n)$ and as the identity on $F_0$.
Hence $p$ splits completely in $F_0$. At our fixed embedding,
$$
v_p(A)=\sum_{h\in\mathcal H^*}v_p(N_h).
\tag{741.5}
$$
There is no residue-degree factor two in (741.5): the field here is the
real subfield, not the full cyclotomic field.

R740 proves that every summand is a nonnegative even integer.
Each of the $g-U_p$ nonunit terms is therefore at least two, so
$$
v_p(A)\ge2(g-U_p),\qquad
A\ge p^{\,2(g-U_p)}.
\tag{741.6}
$$
The latter inequality uses the positive integer $A$ itself.
No conclusion that $A$ is a square at other primes is needed.

## 3. The original archimedean bound gives the proportion

R733 proves, for the complete positive family
$\mathcal H=\{h\bmod n:h\equiv1\pmod6\}$ with $m=n/6$,
$$
\sum_{h\in\mathcal H}N_h<13mp,\qquad N_h\ge0.
$$
Thus its primitive subfamily satisfies the same upper bound.
Arithmetic-geometric mean gives
$$
A^{1/g}<13p\,\frac mg
 =\frac{13p}{3}\frac n{\varphi(n)}.
$$
For completeness, if $q_1<\cdots<q_k$ are the distinct prime divisors
of $n$, then $q_j\ge j+1$ and
$$
\frac n{\varphi(n)}
 =\prod_{j=1}^k\frac{q_j}{q_j-1}
 \le\prod_{j=1}^k\frac{j+1}{j}
 =k+1\le1+\log_2 n.
$$
As $n<2p$ and $13/3<5$, the exact original bound is
$$
A^{1/g}<5p(2+\log_2p).
\tag{741.7}
$$
It is a product over all real embeddings, not a bound at only one
archimedean embedding.

Taking logarithms in (741.6)–(741.7) gives
$$
2\left(1-\frac{U_p}{g}\right)\log p
 <\log p+\log(5(2+\log_2p)).
$$
Rearrangement is (741.1).

The lower bound is already positive for every $p\ge41$.
At 41, $\log_2 41<6$ implies $5(2+\log_2 41)<40<41$.
The function $x-5(2+\log_2x)$ is increasing for $x\ge41$,
so $\varepsilon_p<1$ throughout. This observation is not used
to replace R734's stronger all-prime assertion with $h>1$.

## 4. Explicit ranges and the original Legendre residues

Put $L=\log_2p$. The function
$$
f(L)=\frac{\log_2(5(L+2))}{L}
$$
is strictly decreasing for $L\ge64$, since its derivative has the sign of
$$
\frac L{L+2}-\log(5(L+2))<0.
$$
The elementary comparisons
$$
330<2^9,\qquad810<2^{10},\qquad2570<2^{12}
$$
therefore give, respectively,
$$
\varepsilon_p<9/64<1/7,\qquad
\varepsilon_p<1/16,\qquad
\varepsilon_p<3/128.
$$
Substitution in (741.1) proves (741.2). Also
$\varepsilon_p\to0$, proving (741.3).

The original full fiber identity of R727 is
$$
N_h\bmod p=-P_{h-1}(1/\sqrt{-3})^2.
$$
Consequently the same proportion bounds count exactly the primitive
positive labels with
$$
P_{h-1}(1/\sqrt{-3})\ne0
$$
in the original residue field. Removing the single label $h=1$ reduces
the count by one; labels may vary with $p$.

## 5. What remains for the original Abel and height problems

R727 needs the same actual label to have both
$C_{h-2}\ne0$ and $C_{p-h-2}\ne0$, in addition to a unit $N_h$, in its
interior range. This result proves the size of the unit-norm set; it
does not prove a common label satisfying the two additional conditions.

Likewise, the R737 lower bound for the number of bounded-$M_2$ labels
and (741.1) alone do not force these two sets to intersect: the proved
lower proportions do not sum to more than one. No unproved
independence of their zero sets is assumed.

The original height coefficients, the simultaneous common-root
exclusion, and the Serre uniformity completion criterion remain open.

## Dependencies

- [R730](R730-fixed-depth-original-Abel-isometry-by-all-embedding-norm.md),
  §3: original finite-norm algebraic integrality and conjugates.
- [R733](R733-averaged-original-toric-norms-and-depth-eight-Abel-isometry.md),
  §§2–4: exact full-family positivity, fiber average, and all-embedding
  product bound.
- [R740](R740-even-valuations-of-original-finite-toric-norms.md):
  every original primitive finite norm has even nonnegative valuation.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md):
  the original Legendre residue and simultaneous Cartier conditions.
