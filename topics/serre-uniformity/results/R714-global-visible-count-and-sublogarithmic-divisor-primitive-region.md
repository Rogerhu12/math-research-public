# R714 — A global visible-point count and a sublogarithmic-divisor primitive region

Date: 2026-11-14. Status: proved; the complete inequalities and their original-quotient interfaces have been independently reviewed.

This result concerns the two **original** families in R616. It does not
replace the positive cubic quotient by the opposite cubic twist. The new
input is a bound for the small-radius part of the primitive average that
counts all visible points together. Its complementary large-radius bound
retains the full ray calculation of R614.

## 1. Objects and statements

Let $p\ge41$ be prime, $p\equiv2,5\pmod9$, and put

$$
M=(p+1)/3,\quad R=\operatorname{rad}(M),\quad
\mathcal O=\{o:o\mid R,\ o>2\},\quad J=2^{\omega(M)}-2.
$$

Thus $M$ is even and prime to $3$. Throughout,

$$
c=\frac{\pi}{3\sqrt3},\quad t=\frac cp,\quad
S=\frac32(1+1/p)<2.
$$

Write $A_+^{\rm full},A_+^{\rm prim}$ for the normalized full and
primitive averages of $L'(g_{\theta,+},1)$, and
$A_-^{\rm full},A_-^{\rm prim}$ for the corresponding averages of
$L(g_{\theta,-},1)$, with exactly the normalizations of R616 §6.
The actual quotient of $J_{X_1}$ is the $+$ family. The $-$ family enters
the original point-difference formula as its second factor.

For a real number $X$ with $2\le X\le\sqrt{p/2}$, define

$$
L_X=\frac{\log(p/2)}{\log X}\ge2,\qquad
\delta_X=\frac{1+\log_2 L_X}{L_X},
$$
$$
Q_X=36S\delta_X X+\frac{24SJ}{X},\qquad
T_p=72SJ\sqrt{\frac{3\sqrt3}{p}}.
\tag{714.1}
$$

**Theorem 714.1.** With $E_1(u)=\int_u^\infty e^{-v}\,dv/v$,

$$
\boxed{|A_-^{\rm prim}-A_-^{\rm full}|\le Q_X+T_p,}
$$
$$
\boxed{|A_+^{\rm prim}-A_+^{\rm full}|
       \le Q_XE_1(c/p)+T_p.}
\tag{714.2}
$$

These bounds keep the original $p$-dependent cubic phase of R616. In
particular, the following entirely explicit conditions suffice for the
original nonvanishing/rank conclusion:

$$
\boxed{
72\delta_X X+48J/X\le\tfrac12,\qquad
\sqrt p\ge1440J.}
\tag{714.3}
$$

Under (714.3), the same specified point
$\beta=q_1[c_1-c_0]$ of R616 satisfies

$$
\boxed{
L'(g_{-1,+},1)L(g_{-1,-},1)\ne0,\qquad
A_{-1,1}(\mathbb Q)\otimes\mathbb Q=F\beta.}
\tag{714.4}
$$

Consequently its rank is $[F:\mathbb Q]$ and the original $p$-adic
logarithm is the isomorphism in R616. This is a positive-rank statement;
it is not a zero-image assertion for rational points of $X_1$.

**Corollary 714.2.** For each $0<\varepsilon<1$, (714.4) holds whenever

$$
\boxed{
p\ge\exp\!\bigl(\exp(64/\varepsilon^2)\bigr),\qquad
2^{\omega((p+1)/3)}-2\le(\log p)^{1-\varepsilon}.}
\tag{714.5}
$$

The double exponential is a convenient explicit threshold, not an
optimized one. For usable particular parameters, (714.1)–(714.3) are
substantially sharper and need no asymptotic argument.

**Corollary 714.3.** For every fixed integer $k$, all sufficiently large
primes in the stated residue classes with
$\omega((p+1)/3)\le k$ satisfy (714.4). An explicit threshold is given in
§6. No assertion that such a prescribed shape contains infinitely many
primes is needed or made.

## 2. The original visible-ray identities and their phases

Let $K=\mathbb Q(\zeta)$, $\zeta^2+\zeta+1=0$. A primary element
$\beta=a+b\zeta\equiv1\pmod3$ is visible if $\gcd(a,b)=1$.
Let $\mathcal V$ consist of the visible primary elements whose norms are
prime to $6p$. Write

$$o(\beta)=\operatorname{ord}(\beta^{3(p-1)}\bmod p)$$

for their orders in the actual quotient of the nonsplit torus by $\mu_3$.
The two kernels for the complete integer multiples of a visible ray are

$$
G_{2p}(u)=\sum_{\substack{n\ge1\\(n,2p)=1}}\frac{\chi_{-3}(n)}nE_1(un^2),\qquad
F_{2p}(u)=\sum_{\substack{n\ge1\\(n,2p)=1}}\frac{\chi_{-3}(n)}n e^{-un^2}.
$$

Terms with $3\mid n$ vanish. R614 (614.5)–(614.10) prove the unique
decomposition of each primary generator as
$\chi_{-3}(n)n\beta$, the full sum over $n$, and the bounds

$$|G_{2p}(u)|\le S E_1(u),\qquad
  |F_{2p}(u)|\le S e^{-u}.$$

For the original R616 families, let $m=1$ for $p\equiv5\pmod9$ and
$m=2$ for $p\equiv2\pmod9$, and retain

$$
\lambda_{p,\pm}((a))=a\,\kappa_4((a))^{\pm1}\kappa_p((a))^m.
\tag{714.6}
$$

R616 (616.24)–(616.25) identify the original representations with
$\operatorname{AI}(\lambda_{p,\pm}\nu)$ for the same full or primitive
ring-class characters $\nu$. The factor $\kappa_p^m$ is retained, not
replaced by one. Its value has absolute value one and is trivial on the
rational scalar in the visible-ray decomposition. In particular,

$$|\lambda_{p,\pm}((\beta))|=|\beta|.$$

The full odd-character kernel is $1$ at order one, $-1$ at order two,
and zero elsewhere. The primitive kernel at an element of order $o$
is $\mu(o)/\varphi(o)$. Thus their difference is supported exactly on
the squarefree orders in $\mathcal O$. The two absolutely convergent
identities are

$$
A_+^{\rm prim}-A_+^{\rm full}
=2\sum_{o\in\mathcal O}\frac{\mu(o)}{\varphi(o)}
  \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
  \frac{\lambda_{p,+}((\beta))}{N\beta}
  G_{2p}(tN\beta),
\tag{714.7}
$$
$$
A_-^{\rm prim}-A_-^{\rm full}
=2\sum_{o\in\mathcal O}\frac{\mu(o)}{\varphi(o)}
  \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
  \frac{\lambda_{p,-}((\beta))}{N\beta}
  F_{2p}(tN\beta).
\tag{714.8}
$$

We use absolute values only after this complete signed sum over integer
multiples. We have not replaced the original two-dimensional sum by an
incorrect sum over all multiples without their $\chi_{-3}$ factors.

Put

$$f_0(T)=T^{-1}e^{-tT^2},\qquad
  f_1(T)=T^{-1}E_1(tT^2).$$

Both are positive and decreasing. For $j=0,1$, the corresponding
absolute error is at most

$$
2S\sum_{o\in\mathcal O}\frac1{\varphi(o)}
       \sum_{\substack{\beta\in\mathcal V\\o(\beta)=o}}
       f_j(|\beta|).
\tag{714.9}
$$

## 3. Small-radius counting and a uniform bound for each weight

R614 Lemma 614.1 gives

$$
|\beta|\ge
\begin{cases}
(\sqrt3p/2)^{1/o},&o\text{ odd},\\
(p/2)^{2/o},&o\text{ even}.
\end{cases}
$$

In particular $|\beta|^o\ge p/2$ for every $o>2$ under consideration.
If $|\beta|\le X$, it follows that

$$o\ge L_X=\log(p/2)/\log X.$$

We need a totient bound that is uniform in this order. If the distinct
prime divisors of an integer $n$ are $q_1<\cdots<q_r$, then $q_i\ge i+1$.
As $x/(x-1)$ decreases for $x>1$,

$$
\frac n{\varphi(n)}
=\prod_{i=1}^r\frac{q_i}{q_i-1}
\le\prod_{i=1}^r\frac{i+1}{i}=r+1
\le1+\log_2 n.
\tag{714.10}
$$

The function $(1+\log_2 u)/u$ decreases for $u\ge2$: its derivative
has the sign of $1-\log2-\log u<0$. Therefore for each small-radius
point in (714.9),

$$\boxed{\frac1{\varphi(o(\beta))}\le\delta_X.}\tag{714.11}$$

Here all orders are bounded together. Applying an independent
worst-case point count for every order would lose this benefit.

The Eisenstein lattice has minimum nonzero distance one. The open disks
of radius $1/2$ about its points of absolute value at most $T$ are
disjoint and contained in the disk of radius $T+1/2$. Comparison of areas
gives, for $T\ge1$,

$$\#\{a+b\zeta:|a+b\zeta|\le T\}
  \le4(T+1/2)^2\le9T^2.\tag{714.12}$$

Removing the origin, nonvisible points, nonprimary points, or bad prime
norms only reduces this number. All nonzero lattice points have absolute
value at least one. If $N(T)$ counts the subset used in (714.9), partial
summation consequently yields

$$
\sum_{\substack{\beta\in\mathcal V,\ o(\beta)\in\mathcal O\\
                 |\beta|\le X}}\frac1{|\beta|}
=\frac{N(X)}X+\int_1^X\frac{N(T)}{T^2}\,dT
\le18X.
\tag{714.13}
$$

There is no order-two or unit point in this subset; the identity also
follows by using the counting function on $[0,X]$, where it is zero
below one. Since $e^{-tT^2}\le1$ and $E_1(tT^2)\le E_1(t)$ for $T\ge1$,
(714.11)–(714.13) bound the small-radius portions of (714.9) respectively by

$$36S\delta_X X,\qquad36S\delta_X X E_1(t).\tag{714.14}$$

## 4. The complete complementary tail

Define the weighted counting function

$$
B(T)=\sum_{o\in\mathcal O}\frac1{\varphi(o)}
      \#\{\beta\in\mathcal V:o(\beta)=o,\ |\beta|\le T\}.
$$

The actual per-ray visible-point bound R614 (614.15) is
$4+6T^2/p$. Each order-$o$ element of the quotient lifts to three rays,
and there are $\varphi(o)$ such elements. Consequently

$$\boxed{B(T)\le12J+18JT^2/p.}\tag{714.15}$$

This keeps every visible ray, including any with a very short vector;
it does not impose the full-family $p^2/4$ norm threshold on new
primitive directions.

Stieltjes partial summation, with the points of radius exactly $X$
assigned to the small part, gives

$$
\sum_{|\beta|>X}\frac{f_j(|\beta|)}{\varphi(o(\beta))}
=-B(X)f_j(X)+\int_X^\infty B(T)(-f_j'(T))\,dT
\le\int_X^\infty(12J+18JT^2/p)(-f_j'(T))\,dT.
\tag{714.16}
$$

For either kernel,

$$
\int_X^\infty T^2(-f_j'(T))\,dT
=X^2f_j(X)+2\int_X^\infty T f_j(T)\,dT.
$$

For $j=0$, the right side is
$Xe^{-tX^2}+2\int_X^\infty e^{-tT^2}\,dT$, which is at most
$2\sqrt{\pi/t}$. Indeed $Xe^{-tX^2}\le1/\sqrt{2et}<\sqrt{\pi/t}$,
and twice the Gaussian half-integral is at most $\sqrt{\pi/t}$.
For $j=1$, use the exact identity

$$
\int_X^\infty E_1(tT^2)\,dT
=-XE_1(tX^2)+\sqrt{\pi/t}\operatorname{erfc}(\sqrt tX).
$$

Its corresponding expression is
$-XE_1(tX^2)+2\sqrt{\pi/t}\operatorname{erfc}(\sqrt tX)$,
again at most $2\sqrt{\pi/t}$. Thus (714.16), multiplied by $2S$, is
bounded respectively by

$$
\frac{24SJ}{X}e^{-tX^2}+\frac{72SJ}{p}\sqrt{\pi/t},
$$
$$
\frac{24SJ}{X}E_1(tX^2)+\frac{72SJ}{p}\sqrt{\pi/t}.
\tag{714.17}
$$

The last terms are exactly $T_p$ because
$\sqrt{\pi/t}/p=\sqrt{3\sqrt3/p}$.
Using $X\ge1$ in the first terms and adjoining (714.14) proves
Theorem 714.1. These integrals include the entire infinite tail.

## 5. The original two nonvanishing conclusions

R616 retains the explicit full-family lower bounds

$$
A_-^{\rm full}>\frac{5393}{6150},\qquad
A_+^{\rm full}>\frac95(\log p-1)-\frac1{250}.
\tag{714.18}
$$

The second inequality follows directly from R616 (616.28) using its
stated bounds for $c$ and $\log2$; for $p\ge41$, $\log p-1>0$.
Also $E_1(c/p)<\log p+2$, as in R616. Since $S<2$ and
$\sqrt{3\sqrt3}<5/2$, (714.2) implies

$$
|A_-^{\rm prim}-A_-^{\rm full}|<Q_X^0+T_p^0,
$$
$$
|A_+^{\rm prim}-A_+^{\rm full}|
<Q_X^0(\log p+2)+T_p^0,
$$

where

$$Q_X^0=72\delta_X X+48J/X,\qquad T_p^0=360J/\sqrt p.$$

If (714.3) holds, then $Q_X^0\le1/2$ and $T_p^0\le1/4$. Hence

$$
A_-^{\rm prim}>\frac{5393}{6150}-\frac34
 =\frac{1561}{12300}>0,
$$
$$
A_+^{\rm prim}>
\frac{13}{10}\log p-\frac{1527}{500}
>\frac{423}{500}>0,
\tag{714.19}
$$

where $\log p>3$ for $p\ge41$ is enough for the last inequality.
If $J=0$, the two primitive families already equal their full families,
so their positivity holds without (714.3).

The passage from these two positive averages to (714.4) is exactly the
actual primitive-orbit and point-difference argument proved in R616
§§5–6. In each fixed cubic direction all primitive $\theta$ form the
one rational Galois orbit of the specified factor. The original
Gross–Zagier/Heegner rank interface transfers nonvanishing to that
factor; the two averages consequently meet at the same $\theta_{-1}$.
No direct Galois action on transcendental $L'$ values is asserted, and
the opposite cubic direction is not declared a quotient of $J_{X_1}$.

## 6. Effective regions with no restriction on the size of the radical

### 6.1 A bounded number of prime divisors

Suppose $J>0$, so $J\ge2$. Set $X=192J$ and

$$L_0=2^{17}J\log_2(2^{17}J).$$

If

$$
\boxed{
\log(p/2)\ge L_0\log(192J),\qquad
\sqrt p\ge1440J,}
\tag{714.20}
$$

then $L_X\ge L_0>2$, which also verifies $X\le\sqrt{p/2}$.
For $u=\log_2(2^{17}J)\ge18$, the elementary inequality
$1+\log_2u\le u$ gives

$$
\delta_X\le\delta(L_0)
=\frac{1+u+\log_2u}{2^{17}Ju}
\le\frac1{65536J}.
$$

It follows that

$$
Q_X^0\le\frac{13824}{65536}+\frac14
=\frac{59}{128}<\frac12.
$$

Thus (714.20) proves (714.4) without a small-radical assumption.
For a fixed $k\ge2$, let $J_k=2^k-2$. It is enough to take

$$
p\ge\max\left\{
41,\ (1440J_k)^2,\
2(192J_k)^{\,2^{17}J_k\log_2(2^{17}J_k)}
\right\}.
\tag{714.21}
$$

Indeed use $X=192J_k$ and $J\le J_k$ throughout the preceding estimates.
The case $k=1$ has $J=0$ and was handled above. This proves Corollary
714.3 for all permitted prime powers and exponents in $M$, not just
the special shape $p+1=6\ell$.

### 6.2 A growing number of prime divisors

Fix $0<\varepsilon<1$, set $T=\log p$, and choose
$X=T^{1-\varepsilon/2}$. For $T\ge32$ this choice is at least two and

$$
L_X=\frac{T-\log2}{(1-\varepsilon/2)\log T}
\ge\frac{T}{2\log T}\ge2.
$$

The last bound verifies the admissible upper bound on $X$ as well.
Using monotonicity of $\delta$ and $\log2>2/3$, one obtains

$$
\delta_X\le
\frac{2\log T}{T}(1+\log_2 T)
<\frac{6(\log T)^2}{T}.
\tag{714.22}
$$

If $J\le T^{1-\varepsilon}$, it follows that

$$
Q_X^0<\frac{432(\log T)^2+48}{T^{\varepsilon/2}},\qquad
T_p^0\le360T e^{-T/2}.
\tag{714.23}
$$

The second expression is decreasing for $T\ge2$; at $T=32$ it is
less than $360\cdot32/2^{16}=45/256<1/4$.
For the first expression, let $T_0=\exp(64/\varepsilon^2)$.
The function in (714.23) decreases when $\log T\ge4/\varepsilon$,
as follows by differentiation. At $T_0$ it is at most

$$
1769520\,\varepsilon^{-4} e^{-32/\varepsilon}<\tfrac12.
$$

For completeness, the last inequality follows from
$\log3539040<16$ and
$\log(1/\varepsilon)\le1/\varepsilon-1$:

$$
\log(3539040\varepsilon^{-4})
<12+4/\varepsilon\le16/\varepsilon<32/\varepsilon.
$$

The numerical bound $\log3539040<16$ can be checked without a floating
estimate from $e>8/3$ and $(8/3)^{16}>3539040$.
Thus $T\ge T_0$ implies both conditions in (714.3), and proves
Corollary 714.2. No assertion about the density of primes satisfying
its divisor-count hypothesis is used.

## 7. Scope and remaining inputs

The new estimate controls the original primitive averages when their
number of squarefree orders is smaller than a fixed sublinear power
of $\log p$. The largest prime factor and the size of
$\operatorname{rad}((p+1)/3)$ need not be small. It can be combined with
R616's existing small-radical and special-shape criteria.

The argument does **not** prove that every sufficiently large prime
satisfies one of these conditions. In particular it does not remove
the general R616 nonvanishing premise for all primes. It also supplies
no unit assertion for $\log_p\beta$, no actual height Taylor coefficient,
and no control on the unbounded candidate discriminant $D$. Where the
new criterion applies, it supplies the precise original rank/logarithm
input required by R634/R682/R699/R703; the separate local-height work
still has to be carried out.

This is an algebraic and analytic proof with explicit inequalities.
No prime search, $L$-value run, or repeat of a completed computation is
part of the result.

## Dependencies

- [R608](R608-actual-primitive-ring-class-trace-and-effective-mean.md):
  actual primitive ring-class kernel and the distinction between order
  primitivity and merely nontrivial conductor at $p$.
- [R614](R614-actual-primitive-visible-ray-radical-bound.md), §§2–5:
  complete signed integer-multiple kernels, genuine short-direction
  bounds, and the original visible-point count on every ray.
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md),
  §§5–6: the actual $\kappa_p^m$ phases, both full-family lower bounds,
  primitive Galois orbit, and the point-difference/rank interface.

All additional counting, totient, tail, and constant estimates used
above are proved in this document.
