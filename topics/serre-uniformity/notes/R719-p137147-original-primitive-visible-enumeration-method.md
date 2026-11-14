# R719 method: complete visible-point certification for the original p = 137147 factor

Date: 2026-11-14. **Pre-run status: the complete analytic reduction and
verification program are specified; no numerical bound is asserted
until the public Actions receipt reports success.**

This result concerns only the original nonvanishing, rank, and logarithm
premise of R616 at $p=137147$. It retains the positive cubic quotient
of $J_{X_1}$ and uses the negative cubic family only as the second
factor in the original point-difference formula. It does not exclude
a rational point or complete the uniformity problem.

## 1. Exact original error bound and the success criterion

Use R714's actual notation

$$
M=(p+1)/3=4\cdot11\cdot1039,\qquad
c=\frac{\pi}{3\sqrt3},\qquad
t=c/p,\qquad S=\frac32(1+1/p).
$$

Let $\mathcal V$ be the visible primary Eisenstein integers
$\beta=a+b\zeta$ with

$$
\zeta^2+\zeta+1=0,\quad
a\equiv1,\ b\equiv0\pmod3,\quad
\gcd(a,b)=1,\quad
\gcd(N\beta,6p)=1,
$$

where $N\beta=a^2-ab+b^2$. Define the actual finite-field order

$$
o(\beta)=\operatorname{ord}
\bigl(\beta^{3(p-1)}\bmod p\bigr)\mid M.
$$

The squarefree orders greater than two are exactly

| $o$ | 11 | 22 | 1039 | 2078 | 11429 | 22858 |
|---|---:|---:|---:|---:|---:|---:|
| $\varphi(o)$ | 10 | 10 | 1038 | 1038 | 10380 | 10380 |

R714 (714.7)--(714.9), after the complete signed sum of
integer multiples on each visible ray, give

$$
|A_-^{\rm prim}-A_-^{\rm full}|
\le B
:=2S\sum_{\substack{\beta\in\mathcal V\\o(\beta)>2\ {\rm squarefree}}}
\frac{e^{-tN\beta}}{\varphi(o(\beta))|\beta|}.
\tag{719.1}
$$

The same original ray identity bounds the positive-family error
by replacing $e^{-x}$ with $E_1(x)$. For $x>0$,

$$
E_1(x)=e^{-x}\int_0^\infty\frac{e^{-u}}{x+u}\,du
<e^{-x}\left(\log(1+1/x)+1\right).
$$

Indeed the interval $[0,1]$ is bounded by
$\int_0^1du/(x+u)$, and the remaining integral is at most
$\int_1^\infty e^{-u}du<1$. Since $x\ge c/p$ and $c>3/5$,

$$
\log(1+1/x)+1<\log p+2.
$$

For the last inequality, $1/p+1/c<8/3<e$ suffices.
Thus

$$
|A_+^{\rm prim}-A_+^{\rm full}|
<(\log p+2)B.
\tag{719.2}
$$

The formal success condition is a certified bound $B<1/2$.
It is the shared exponential bound $B$, not the larger
right side of (719.2), that is compared to $1/2$.

R714 (714.18) retains the full-family estimates

$$
A_-^{\rm full}>\frac{5393}{6150},\qquad
A_+^{\rm full}>\frac95(\log p-1)-\frac1{250}.
$$

Consequently $B<1/2$ proves

$$
\boxed{
A_-^{\rm prim}>\frac{1159}{3075}>0,\qquad
A_+^{\rm prim}>
\frac{13}{10}\log p-\frac{701}{250}>
\frac{137}{125}>0.
}
\tag{719.3}
$$

The last strict comparison uses $\log p>3$.
The original R616 primitive-orbit and point-difference argument
then applies to the same specified factor and point:
$L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$,
$A_{-1,1}(\mathbf Q)\otimes\mathbf Q=F\beta$,
and the stated original logarithm is an isomorphism.
No direct Galois action on transcendental $L'$ values is used.

## 2. Complete finite part with the original orders

Set

$$
R^2=25p,\qquad R=\sqrt{25p}.
$$

The enumerator visits all integers $a,b$ with
$|a|,|b|\le\lfloor\sqrt{4R^2/3}\rfloor$, then applies the
exact primary, norm, visibility, and $\gcd(6p,N)=1$ conditions.
This box contains the entire norm ball, since

$$
N(a+b\zeta)=(a-b/2)^2+3b^2/4
=(b-a/2)^2+3a^2/4.
$$

Every accepted point is counted exactly once. Norms and the
boundary comparison are integer operations, not approximate
Euclidean-circle tests.

As $p\equiv2\pmod3$, the reduction is the field
$\mathbf F_p[\zeta]/(\zeta^2+\zeta+1)$. The fast value is

$$
u=\left(\frac{\bar\beta^2}{N\beta}\right)^3,
\qquad \bar\beta=(a-b)-b\zeta.
\tag{719.4}
$$

Frobenius is conjugation, so (719.4) is exactly
$\beta^{3(p-1)}$. The code first verifies every entry of
the modular inverse table. It checks $u^M=1$, strips
prime factors $2,11,1039$, and verifies the resulting
order by all prime-divisor tests. No discrete-log or
angular approximation assigns a point to an order.

For every norm with a nonzero contribution, the complete
six-column histogram records the six actual-order counts.
All omitted norms have all six counts zero. Its exact
finite sum is

$$
F_R=\sum_{n\le25p}\sum_{j=1}^6
\frac{h_{n,j}}{\varphi(o_j)}
\frac{e^{-tn}}{\sqrt n}.
\tag{719.5}
$$

The full histogram is preserved as CSV and deterministic
gzip; it is not replaced by aggregate totals.

## 3. Independent exact audit on the whole small ball

For every admissible point of norm at most $10000$, the
C++ program outputs $a,b,N,u$ and its exact order, and
also compares (719.4) to a direct power.

The independent Python audit enumerates every integer
coordinate in its own enclosing box and applies the
conditions separately. It computes
$\beta^{3(p-1)}$ directly, without the inverse table,
and finds the order by the first successful divisor
of $M$ in increasing order, without prime-factor
stripping. It compares the entire dictionaries of
points and their values, so agreement includes absence
of omitted or duplicate points in that ball.

The complete finite enumeration remains the C++ integer
calculation. The small-ball comparison is an independent
implementation check, not a claim that a short prefix
certifies the unenumerated finite ball.

## 4. The entire infinite tail

Any two different primary elements are separated by
at least $3$ in the complex embedding. The disks of
radius $3/2$ around them are disjoint. Hence the number
of all primary points of modulus at most $T$ satisfies

$$
N_{\rm prim}(T)\le(1+2T/3)^2.
\tag{719.6}
$$

This overcount includes nonvisible points, wrong orders,
and points with norm not prime to $6p$. It therefore
bounds the required tail. Also
$\varphi(o)^{-1}\le1/10$ for every contributing order.

Put $f(T)=T^{-1}e^{-tT^2}$. Stieltjes summation and
discarding the negative lower endpoint give

$$
\sum_{|\beta|>R}f(|\beta|)
\le\int_R^\infty(1+2T/3)^2
e^{-tT^2}(2t+T^{-2})\,dT.
$$

The constant term integrates to $e^{-tR^2}/R$.
The linear term gives

$$
\frac43\left(e^{-tR^2}+\frac12E_1(tR^2)\right)
\le\frac43 e^{-tR^2}
\left(1+\frac1{2tR^2}\right).
$$

The quadratic term gives

$$
\frac49\left(Re^{-tR^2}
+2\int_R^\infty e^{-tT^2}\,dT\right)
\le\frac49e^{-tR^2}
\left(R+\frac1{tR}\right).
$$

Here $E_1(x)\le e^{-x}/x$, and the Gaussian tail
inequality follows by replacing $1$ by $T/R$
inside the integral. Therefore the complete weighted
tail is bounded by

$$
\boxed{
\mathcal T_R=
\frac1{10}e^{-tR^2}
\left[
\frac1R+
\frac43\left(1+\frac1{2tR^2}\right)+
\frac49\left(R+\frac1{tR}\right)
\right].
}
\tag{719.7}
$$

No extrapolation from the order frequencies in the finite
ball enters (719.7). Together, (719.5) and (719.7) give

$$
\boxed{B\le 2S(F_R+\mathcal T_R).}
\tag{719.8}
$$

## 5. Certified numerical protocol and publication boundary

The public runner uses python-flint Arb at at least
192 bits, default 256 bits. It evaluates every term
of (719.5), the entire expression (719.7), and the
factor $2S$ using real-ball arithmetic. It extracts
a single strict rational upper bound with denominator
$10^{12}$ by integer bisection controlled only by
certified Arb comparisons; no floating-point midpoint
selects the conclusion.

The output is successful only if this rational bound
is strictly below $1/2$. It also verifies the lower
bounds of (719.3) with Arb, and records the two
primitive lower-bound balls. If the inequality does
not close, the full counts, tail, and false success
flag are still preserved, with no nonvanishing claim.

Sources and outputs are bound by SHA256, including
the C++ source, Python driver, both repository READMEs,
R714, R616, this proof when passed by the wrapper,
the entire histogram, the small-radius dictionary,
the input receipt, and the complete numerical certificate.
The receipt includes the actual public repository,
source commit, run ID, attempt, software version,
and mathematical success flag. The driver refuses
formal execution outside GitHub Actions of
Rogerhu12/math-research-public.

Expected source paths:

- [r719_visible_order_histogram.cpp](../scripts/r719_visible_order_histogram.cpp)
- [run_r719_p137147_primitive_certificate.py](../scripts/run_r719_p137147_primitive_certificate.py)

Run from the repository root:

~~~sh
python topics/serre-uniformity/scripts/run_r719_p137147_primitive_certificate.py \
  --cpp-source topics/serre-uniformity/scripts/r719_visible_order_histogram.cpp \
  --repo-root . \
  --proof-path topics/serre-uniformity/notes/R719-p137147-original-primitive-visible-enumeration-method.md \
  --output output/R719
~~~

The complete public Actions artifact and its success
receipt must be appended before changing the pre-run
status at the top of this note to a numerical theorem.

Dependencies:
[R614](../results/R614-actual-primitive-visible-ray-radical-bound.md),
[R616](../results/R616-original-CM-point-difference-and-explicit-height-basis.md),
and
[R714](../results/R714-global-visible-count-and-sublogarithmic-divisor-primitive-region.md).
The software's real-ball comparison contract is documented in
[python-flint general concepts](https://python-flint.readthedocs.io/en/stable/general.html)
and [Arb real numbers](https://python-flint.readthedocs.io/en/stable/arb.html).
