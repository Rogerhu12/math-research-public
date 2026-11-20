# R998 method — one exact second-end-column cusp constant

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: proved algorithm and fixed execution contract; not executed.** This is a new finite arithmetic input for the remaining branch of R996. It computes only the second end column, its original Legendre factor, and the complete prime factorization needed to state its exception set. It does not repeat any sigma, trace, matrix, or prime window.

## 1. Exact fixed target

Take the unchanged original indices

$$
p=6N+5\ge41,\qquad i=N-2,\qquad j=1,
$$
$$
a=6i+4=p-13,\quad b=6j+1=7,\quad h=6i+7=p-10.
\tag{998M.1}
$$

The original primitive condition is exactly $11\nmid p+1$. The Legendre factor reflects to $P_{10}(1/s)$, with $s^2=-3$. The specific new branch sought after R996 is

$$
p\ge41,\quad p\equiv5\pmod6,\quad p\bmod9\in\{2,5\},
\quad 5\mid p+1,\quad11\nmid p+1.
\tag{998M.2}
$$

The consumer does not enumerate primes in (998M.2). It factors the fixed exact numerators and denominators, certifies every resulting prime factor, and classifies only those finitely many factors by (998M.2).

## 2. First exact route: all terms of the original R968 formula

R996's complete norm-one cusp source gives

$$
a![q^0]T_{a,l}
=\mathbf1_{l\equiv3\ (6)}
\sum_{t=0}^{l}
\frac{(-1)^t\prod_{r=0}^{t-1}(-13-r)}
 {2^t t!(l-t)!}\pmod p.
\tag{998M.3}
$$

The empty product is one. The product is the falling factorial of the residue $a=-13$. The unit-orbit condition still uses the **original** $a\equiv4\pmod6$. It must not be recomputed from the integer representative $-13$, which has a different residue modulo six. All required $l\le9$ are less than the actual $a=p-13\ge28$.

For $b=7$, the complete R968(968.9) consists of the leading term, the three single-zeta terms $n=2,3,4$, and the one double term $(n,m)=(2,2)$. The consumer evaluates all of them, including their zero complete unit-orbit coefficients. The $n=2,4$ terms and the double term have a Taylor index outside $l\equiv3\pmod6$; hence their original $T$ coefficient is zero. Exactly

$$
Z_{a,7}=6T_{a,9}+6\beta_3T_{a,3},
\qquad [q^0]\beta_3=\frac1{30240}
\tag{998M.4}
$$

remains. The source of this reduction is verified by the complete sum, not imposed by omitting its other terms.

For the weighted zeta constants, the script independently constructs $B_0,\ldots,B_8$ from

$$
B_0=1,\qquad
B_m=-\frac1{m+1}\sum_{k=0}^{m-1}\binom{m+1}{k}B_k.
\tag{998M.5}
$$

Thus the convention is $B_1=-1/2$, and $\beta_n=B_{2n}/(2n)!$. Exact `Fraction` arithmetic is used throughout. Every falling-factorial summand and every complete R968 term is included in the output.

## 3. Independent integer ODE route

By R996, put

$$
S_7(v)=e^v(1-v/2)^{-13},\qquad
K_l=2^l l![v^l]S_7.
$$

The exact first-order identity $(2-v)S_7'=(15-v)S_7$ gives

$$
K_0=1,\quad K_1=15,\qquad
K_{l+1}=(l+15)K_l-2lK_{l-1}.
\tag{998M.6}
$$

The consumer computes $K_0,\ldots,K_9$ by this integer recurrence, without calling the direct Gaussian/falling-factorial route. Its independent target is

$$
C_1=6\frac{K_9}{2^9\,9!}
+\frac1{5040}\frac{K_3}{2^3\,3!}.
\tag{998M.7}
$$

The two routes must agree exactly as rational numbers and verify the paper value

$$
\boxed{\qquad
a![q^0]Z_{p-13,7}
=C_1=\frac{319435001}{40320}\pmod p.
\qquad}
\tag{998M.8}
$$

If they disagree, the execution fails rather than replacing the target or silently selecting one route. The arithmetic of (998M.8), including its numerator factorization, has not been run locally.

## 4. Two independent exact Legendre evaluations

One route constructs the entire polynomial $P_{10}$ using

$$
P_0=1,\quad P_1=x,\qquad
(n+1)P_{n+1}=(2n+1)xP_n-nP_{n-1},
$$

then evaluates its even powers at $x^2=-1/3$. The other directly evaluates the factorial expression

$$
P_{10}(x)=2^{-10}\sum_{k=0}^{5}
\frac{(-1)^k(20-2k)!}{k!(10-k)!(10-2k)!}\,x^{10-2k}.
\tag{998M.9}
$$

The two exact results must agree and give

$$
\boxed{P_{10}(1/s)=-8953/243=-7\cdot1279/243.}
\tag{998M.10}
$$

This is the original factor of the same $h=p-10$. No neighboring label or alternate curve is used.

## 5. Complete factorization and explicit primality receipts

The fixed positive integers factored are the numerator and denominator of (998M.8), and the absolute numerator and denominator of (998M.10). The factorization algorithm removes the factor two and then tries successive odd integers until the square of the current divisor exceeds the remaining quotient. The factor list must reconstruct its input exactly.

Every distinct reported prime factor is then **independently** certified: the script tests divisor two when it is at most the square root, and every odd integer from three through $\lfloor\sqrt q\rfloor$. Every tested remainder must be nonzero. These tests prove primality, since any composite number has a prime divisor in that range. The report records for each factor:

- the exact square-root bound and both bounding squares;
- whether two was tested, the complete odd-divisor range, and the number of tests;
- the successful all-nonzero condition and SHA256 of the complete ordered `divisor:remainder` stream.

The remainder array is not retained. The exact range, encoding, and frozen code determine that stream and allow its hash to be reproduced. No probable-prime routine or unexplained remaining cofactor is accepted.

The report classifies every certified prime factor by the unchanged original congruences and by (998M.2). In particular it separately prints all original allowed prime divisors of the cusp numerator and the subset belonging to the specified new branch. These lists are not required in advance to be empty. A genuine bad factor is a mathematical outcome of the fixed computation, not a runtime failure.

The denominator must have no prime in the original range, and the Legendre numerator must factor as $7\cdot1279$ with both factors certified. Their residue classes give no original allowed Legendre exception. If either assertion fails, the execution is unsuccessful.

## 6. Public guard, output and acceptance

Script: `scripts/original_second_end_column_cusp_consumer.py`.

Suggested fixed invocation:

```text
python topics/serre-uniformity/scripts/original_second_end_column_cusp_consumer.py --seconds 30 --output /tmp/serre-second-end-column-cusp.json
```

Only the Python standard library is used. Before any mathematical call, require `GITHUB_ACTIONS=true` and `GITHUB_REPOSITORY=Rogerhu12/math-research-public`. Local work is limited to paper reasoning, file I/O, source inspection, AST parsing and hashes. The source R968 and R996 files are pinned inside the consumer; the method and consumer hashes are also included in its receipt.

The maximum execution budget is thirty seconds, beginning before source hashing and all arithmetic. The factor loops repeatedly check the deadline. A failure reports its actual error and nonzero exit status. A successful receipt requires all exact-route comparisons, complete factor reconstructions, every prime-factor trial certificate, a final timing receipt with `within_total_budget=true`, and exit zero.

The deterministic payload contains the source contract, both cusp routes, both Legendre routes, factorizations, primality receipts, actual prime-class lists and summary. It is encoded as sorted-key compact ASCII JSON followed by one newline. Timing is separate and is not part of this payload. The payload, its byte length and SHA256 are printed; the same bytes may be written only to runner `/tmp` scratch. There are no artifacts, Releases, committed data, raw sigma arrays or prime windows.

The next result may use the actual public receipt to state the exact new nonzero-space family, excluding any actual bad factor the report finds. This method itself does not predeclare the factorization or its exception set. It never turns a cusp unit into a CM marked unit or a proof of $\mathcal G$-stability.

## Dependencies

- [R968](../results/R968-full-level-mixed-CM-jet-and-critical-factor.md), especially (968.9): the complete original source formula.
- [R996](../results/R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md), especially §4: the precise finite cusp reduction and the separate old end-column theorem.
- [R992](../results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md): the conditional role of $V_p\ne0$, which is the only proposed application of this finite input.

The existing $j=0$ cusp constant is consumed from R996 and is not recomputed by this script. The proposed calculation is solely the new $j=1$ column and its complete finite exception set.
