# R973 execution contract — the actual balanced Kronecker coefficient

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.
Root authoring; coefficient formulas and the complete consumer were independently paper-audited by legendre_shift.

**Status before execution:** the source and the integral single-carry reduction below are proved. Four new exact values are requested, not assumed. No all-prime nonvanishing or comparison with the original supersingular trace is asserted by this contract.

## 1. The precise new source

Use exactly the curve and differential of [R574](../results/R574-completed-zeta-Cartier-input.md):
\[
E_0:y^2=x^3-1,\qquad \omega=dx/(2y),\qquad
x(z)=z^{-2}+O(z^4),\quad y(z)\sim-z^{-3}.
\]
Let \(\sigma(z)\) be the canonical Weierstrass sigma function for this differential, with \(\sigma'(0)=1\). The invariants are \(g_2=0,g_3=4\). The completed weight-two constant is zero by the original CM symmetry. No additional Gaussian is inserted.

Define
\[
\Theta(z,w)=\frac{\sigma(z+w)}{\sigma(z)\sigma(w)},\qquad
c_n=[z^n w^{n-1}]\Theta(z,w).
\tag{973M.1}
\]
This is the actual balanced coefficient of the original elliptic Kronecker function. The homogeneous modular weight of \(c_n\) is \(2n\). The different weight \(n+1\) belongs to the high CM modular form under investigation; these weights are not identified.

The Eisenstein–Kronecker generating convention can be checked against Bannai–Kobayashi, [Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers](https://arxiv.org/pdf/math/0610163), Theorem 1.17:
\[
c_n=-\frac{e^*_{n-1,n+1}(0,0)}{(n-1)!\,\mathcal A^{\,n-1}},
\qquad \mathcal A=\operatorname{Area}(\mathbf C/\Lambda)/\pi.
\tag{973M.2}
\]
Here the sign is \((-1)^{(n-1)+(n+1)-1}=-1\).
This identity identifies the coefficient, not its nonvanishing or its integral Manin period.

The four primes are fixed:
\[
p=41,\ 47,\ 227,\ 857,\qquad
r=\begin{cases}2&p\equiv11\pmod{12},\\8&p\equiv5\pmod{12},\end{cases}
\qquad n=p-r.
\tag{973M.3}
\]
All are in the original allowed classes \(p\bmod9\in\{2,5\}\). The first two cover both rows; the last two retain the previously distinguished central-failure primes as reference labels, without recomputing their old same-label values or traces. The target (973M.1) is new.

## 2. Exact rational coefficients from the original differential equation

Write
\[
x=z^{-2}+\sum_{j\ge1}X_jz^{6j-2},\qquad
\sigma(z)=zS(z),\qquad S(z)=\sum_{j\ge0}s_jz^{6j}.
\]
The equations \(x''=6x^2\) and \(x'^2=4(x^3-1)\), with the original normalization, give
\[
X_1=\frac17,\qquad
X_j=\frac{\sum_{a=1}^{j-1}X_aX_{j-a}}{(6j+1)(j-1)}
\quad(j\ge2).
\tag{973M.4}
\]
For
\[
\log S(z)=\sum_{j\ge1}\ell_j z^{6j}
\]
the exact equation \((\log\sigma)''=-x\) gives
\[
\ell_j=-\frac{X_j}{6j(6j-1)},\qquad
s_0=1,\quad
j s_j=\sum_{a=1}^j a\ell_a s_{j-a}.
\tag{973M.5}
\]
Independently generate the coefficients \(b_j\) of \(1/S(z)\) by the exponential recurrence with \(-\ell\):
\[
b_0=1,\qquad j b_j=-\sum_{a=1}^j a\ell_a b_{j-a}.
\tag{973M.6}
\]
The public consumer checks the exact coefficient identity \(S\cdot S^{-1}=1\) through the full needed degree. In particular \(s_1=-1/210\).

If \(n=6t+3\), direct multiplication of (973M.1) gives
\[
\boxed{\quad
c_n=\sum_{u,v=0}^{t}
 b_u b_v s_{2t+1-u-v}
 \binom{6(2t+1-u-v)+1}{n+1-6u}.
\quad}
\tag{973M.7}
\]
Indeed, a summand of \(\Theta\) is
\[
b_u b_v s_k z^{6u-1}w^{6v-1}(z+w)^{6k+1}.
\]
The requested exponents force \(k=2t+1-u-v\), and the displayed binomial is its exact coefficient. Both upper limits equal \(t\), so no boundary term is omitted. The normalization check is
\[
c_3=35s_1=-1/6.
\tag{973M.8}
\]

## 3. Why every summand is integral at the actual prime

Set \(p=6N+5\). In the two rows \(t=N\) and \(t=N-1\), respectively. Thus the coefficients \(b_u,b_v\) in (973M.7) are in the first integral block.

The already fixed first-pole relation of R702, equivalently the original sigma logarithm obtained from R574, is
\[
p s_{N+1+j}\equiv-Bs_j\pmod p,\qquad 0\le j\le N,
\tag{973M.9}
\]
where the original nonzero constant is precisely
\[
B=(-1)^{(p-1)/2-(p-2)/3}
 \binom{(p-1)/2}{(p-2)/3}.
\tag{973M.10}
\]
There is no replacement of \(B\) by the weight-\(p+1\) modular section or by the formal Igusa height coefficient.

One can also verify the range in (973M.9) directly from (973M.4)–(973M.5). The \(X_j\) through \(2N+1\) are \(p\)-integral. In that range the only logarithmic denominator divisible by \(p\) is \(6(N+1)-1=p\). Its residue is \(p\ell_{N+1}=-B\), by \(D^{p-1}x=-B\) and Wilson. Since \(2(N+1)>2N+1\), the exponential has at most one such pole in the whole requested block. Multiplying this pole by its first integral block yields (973M.9).

For a summand in (973M.7), put
\[
k=2t+1-u-v,\quad A=n+1-6u,\quad C=n-6v.
\]
Then \(A+C=6k+1\), and
\[
0<A<p,\qquad0<C<p.
\tag{973M.11}
\]
If \(k\le N\), all factors are integral. If \(k\ge N+1\), then
\[
p<6k+1<2p,\qquad
v_p\binom{6k+1}{A}=1.
\tag{973M.12}
\]
Its one factor of \(p\) cancels the only possible pole of \(s_k\). Thus (973M.7) is termwise integral for both rows, and its residue is obtained by replacing the high summand by
\[
-B\,b_u b_v s_{k-N-1}
 \left(\frac1p\binom{6k+1}{A}\right)\pmod p.
\tag{973M.13}
\]
The integer binomial is divided by \(p\) before reduction. The consumer verifies its valuation is exactly one, and independently compares the complete exact rational value with this pole-residue calculation. It does not determine the exact value by assigning a proposed unit.

## 4. Public execution and receipts

The consumer is [original_balanced_kronecker_four_prime_consumer.py](../scripts/original_balanced_kronecker_four_prime_consumer.py). Its hash is frozen in the current request. Runtime is python-flint 0.9.0, whose [official rational-number API](https://python-flint.readthedocs.io/en/latest/fmpq.html) has been read. Only exact rational arithmetic and exact integer binomials are used.

All mathematics runs exclusively in this public repository's GitHub Actions. Local review is limited to source reading, AST parsing, bytes, hashes and metadata. One exact sigma prefix is shared among the four new coefficients; neither the old moment/trace window nor any same-label sigma product is recalculated.

Stdout contains each complete rational target, its hash, the prime valuation and residue, the actual first-pole comparison, and hashes of the needed rational prefixes. No coefficient array or certificate file is committed or uploaded as an artifact. The parent process enforces a maximum 620-second budget and prints any uncompleted tail explicitly. A complete four-prime success says only that these four calculations completed; zero or nonunit targets are recorded as mathematical results, not masked as runtime failures.

The root must read the actual public logs, verify the output hashes by pure I/O, and register the actual finite outcome. These finite outcomes cannot prove all-prime units. A separate exact adjoint-value and Manin-period argument is still required even to use a unit of (973M.1) for R970.

