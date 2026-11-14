# R685 — A two-digit integral algorithm for the actual pair of CM coefficients

**Status: proved algorithm.** For one prime $p\ge41$, $p\equiv5\pmod6$,
this gives the exact reductions of the complete six-torsion numbers $C_p$
and $C_{p-3}$ in R615/R683. It uses only arithmetic modulo $p^2$ in the
three-dimensional algebra with $r^3=4$ and has quadratic operation count
in $p$. The one division by $p$ is performed only on the verified multiple
of $p$ after the complete character trace. No finite search, whether or not
it finds zeros, proves uniform nonvanishing.

## 1. Exact ordinary derivatives avoid every intermediate division by $p$

Fix one admissible weight $2\le k\le p$, $k\equiv2\pmod3$, and put
$m=k-1$, $N=2m+1<2p$. Work in

$$
 A=(\mathbf Z/p^2\mathbf Z)[r]/(r^3-4).
$$

The original scaled coordinate is $\xi=\sqrt3\,z$. At the tame point with
$\delta=1,j=0$, put $X=x$, $Y=y/\sqrt3$, and let $E$ be the completed
zeta value divided by $\sqrt3$. The characteristic-zero initial conditions
and equations are

$$
 X_0=2+r+r^2,\quad Y_0=-3-2r-r^2,\quad
 E_0=(2+2r+r^2)/6,\quad S_0=1,
$$
$$
 X'=2Y,\qquad Y'=X^2,\qquad E'=-X/3,\qquad S'=ES.
 \tag{685.1}
$$

Here $X_n,Y_n,E_n,S_n$ now denote the **ordinary** $n$-th derivatives at
zero, not Taylor coefficients. Leibniz's rule gives

$$
\begin{aligned}
 X_{n+1}&=2Y_n,\\
 Y_{n+1}&=\sum_{i=0}^n\binom niX_iX_{n-i},\\
 E_{n+1}&=-X_n/3,\\
 S_{n+1}&=\sum_{i=0}^n\binom niE_iS_{n-i}.
\end{aligned}
 \tag{685.2}
$$

All these derivatives lie in $\mathbf Z_{(p)}[r]/(r^3-4)$ because the
only initial or recursion denominators are $2$ and $3$. Thus reducing
(685.2) modulo $p^2$ computes their exact residues, even at indices
$n\ge p$. There is no loss of a digit at an intermediate differential
equation coefficient.

The script updates the binomial row by Pascal's identity modulo $p^2$.
For triples, multiplication is the exact reduction

$$
(a_0+a_1r+a_2r^2)(b_0+b_1r+b_2r^2)
 =a_0b_0+4(a_1b_2+a_2b_1)
$$
$$
\hspace{12mm}+(a_0b_1+a_1b_0+4a_2b_2)r
 +(a_0b_2+a_1b_1+a_2b_0)r^2.
$$

Consequently the recurrence uses $O(p^2)$ integer operations with
residues bounded by $p^2$, rather than constructing very large rational
coefficients or a $p$-torsion orbit.

## 2. The only factorial denominator and its retained extra digit

For $0\le n<2p$, define

$$
 v_n=\begin{cases}0&n<p,\\1&n\ge p,\end{cases}
 \qquad F_n=n!/p^{v_n}\in\mathbf Z_{(p)}^\times.
 \tag{685.3}
$$

Their residues are computed multiplicatively, replacing the single
factor $p$ by $1$. Let $s_n=S_n/n!$ be the actual Taylor coefficients of
$S(\xi)$. Although $s_n$ need not be integral for $n\ge p$, the following
quantity always is, and its reduction modulo $p^2$ is known exactly:

$$
 p\,s_n\equiv
 \begin{cases}
 pS_nF_n^{-1}&n<p,\\
 S_nF_n^{-1}&p\le n<2p.
 \end{cases}
 \pmod{p^2}.
 \tag{685.4}
$$

This identity takes place in the characteristic-zero localized ring
before reduction. No inverse of $p$ in $\mathbf Z/p^2\mathbf Z$ is used.
Knowing the derivatives modulo $p^2$ is precisely enough for (685.4).

For the inverse series $S(\xi)^{-1}=\sum b_j\xi^j$, only indices
$j\le m<p$ are needed. Their factorials are units. Therefore

$$
 s_j=S_jF_j^{-1}\pmod{p^2},\quad b_0=1,\quad
 b_n=-\sum_{j=1}^ns_jb_{n-j}\pmod{p^2}
 \tag{685.5}
$$

computes every needed $b_j$ integrally and with both digits intact.

For later binomial coefficients, $0\le j\le n<2p$ gives the exact formula

$$
 \binom nj\equiv
 p^{v_n-v_j-v_{n-j}}F_nF_j^{-1}F_{n-j}^{-1}\pmod{p^2}.
 \tag{685.6}
$$

The exponent is $0$ or $1$. This also avoids nonunit modular division.

## 3. Every inverse-sigma block is present

Let $\widetilde\sigma(\eta)=\sqrt3\sigma(\eta/\sqrt3)$ and

$$
 \eta/\widetilde\sigma(\eta)=\sum_{h\ge0}u_h\eta^{6h}.
$$

The unchanged rational recurrence is

$$
 a_1=1/189,\qquad
 a_n=\frac{\sum_{i=1}^{n-1}a_i a_{n-i}}{(n-1)(6n+1)},
$$
$$
 \ell_n=\frac{a_n}{6n(6n-1)},\quad u_0=1,\quad
 u_h=\frac1h\sum_{i=1}^hi\ell_i u_{h-i}.
 \tag{685.7}
$$

Only $h\le\lfloor(m+1)/6\rfloor=\lfloor k/6\rfloor$ occurs. Since
$p\equiv5\pmod6$ and $k\le p$, every denominator in (685.7) is a
$p$-unit: $6h\le p-5$, hence $6h+1\le p-4$, while $h<p$.
Also $p\ge41$ is prime to $189$. Thus all required $u_h$ can be computed
modulo $p^2$ by modular inverses of units.

## 4. Trace first, then the sole exact division by $p$

R683's exact coefficient formula is

$$
 c_m(r)=\sum_{j=0}^mb_j
 \sum_{\substack{h\ge0\\n=2m+1-j-6h\ge m-j}}
 u_hs_n\binom n{m-j},\qquad
 C_k=\frac{(-1)^m3^{2m}m!}{2}[r]c_m.
 \tag{685.8}
$$

All indices $n$ here satisfy $0\le n<2p$. Insert (685.4), (685.5),
(685.6), and (685.7) into the right side of $p$ times (685.8). This
computes exactly

$$
 P_m:=p\,c_m(r)\pmod{p^2}
 \tag{685.9}
$$

in $A$, retaining all inverse-sigma blocks. Individual constant or
$r^2$ components need not encode integral unweighted diagonals; the
original tame character trace extracts only the $r$ coefficient, since
$\operatorname{Tr}(c_m/r)=3[r]c_m$.

By the proved integrality in R658/R683 and the fact that
$(-1)^m3^{2m}m!/2$ is a $p$-unit, the rational coefficient $[r]c_m$
is integral. Hence $[r]P_m$ is divisible by $p$ modulo $p^2$. If its
canonical representative is $a\in\{0,\ldots,p^2-1\}$, then the exact
answer is

$$
 \boxed{
 C_k\bmod p=
 \frac{(-1)^m3^{2m}m!}{2}\,\frac{a}{p}\pmod p.
 }
 \tag{685.10}
$$

The script checks the integer condition $p\mid a$ before taking this
last quotient. Choosing any other representative changes $a/p$ by a
multiple of $p$, so the output is well-defined. This check is meaningful:
it is not an instruction to divide a zero residue in $\mathbf F_p$.
The extra digit in (685.9) determines the quotient.

Equations (685.1)–(685.10) prove the algorithm for every prime in scope.
The executable can compute both weights using the single derivative
array through $2p-1$. Its memory requirement is $O(p)$ aside from its
small output record, and its operation count is $O(p^2)$.

## 5. Reproduction and exact scope

Stable standalone script: `scripts/R685_modular_kronecker.py`.
It requires only Python's standard library. From the topic directory:

```bash
python scripts/R685_modular_kronecker.py --prime 41 --output result41.json
python scripts/R685_modular_kronecker.py --prime 101 --output result101.json
```

`--weights 98` may select one admissible weight at prime $101$.
The output contains the complete $p$-scaled coefficient triple modulo
$p^2$ for each inverse-sigma block, the exact-divided $r$ coefficient,
the result, source hash, and measured runtime.

The short computations already executed give

| $p$ | $C_p\bmod p$ | $C_{p-3}\bmod p$ |
|---:|---:|---:|
| 41 | 28 | 35 |
| 101 | 51 | 18 |

At $41$, both entries equal the already computed exact rational values.
At $101$, the second also equals the reduction of the independently
computed exact rational $C_{98}$; the full rational record is retained.
The two-digit runs took approximately $0.066$ and $0.33$ seconds.
These are normalization checks of an algorithm proved by the identities
above, not evidence claimed to cover every prime.

The public Actions finite-window request is to examine primes
$41\le p\le2000$ with $p\equiv2,5\pmod9$. A zero result, if obtained
and retained, would refute the corresponding universal unit claim for
that actual congruence range. If no zero is found, universal
nonvanishing remains open. No result from that request has been assumed
in this proof.
