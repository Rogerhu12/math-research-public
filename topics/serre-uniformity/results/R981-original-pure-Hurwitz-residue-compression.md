# R981 — Residue compression of the original pure Hurwitz coordinates

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: handoff_audit; independently reviewed by root.

**Status: proved identities and execution method; no execution result is claimed.** This method computes the four actual Hurwitz coefficients appearing in R978 and the Robert reflection of R980 directly over $\mathbb F_p$, with only a linear number of distinct input coefficients. It does not compute an original supersingular trace, a same-label sigma product, or an already registered balanced Kronecker coefficient.

The final series may have length proportional to $p^2$. The result below is an input and exponent compression, not a claim of linear running time. The consumer uses bounded powers and inverses of truncated series, without constructing a large rational sigma series. Exact rational $\wp$ coefficients are used only at the two small calibration primes.

## 1. Fixed source and indices

Keep the original curve and differential
$$
E_+:y^2=x^3+1,\qquad \omega=dx/(2y),\qquad
(g_2,g_3)=(0,-4).
\tag{981.1}
$$
The pure Hurwitz numbers are exactly those of R978:
$$
\log(\sigma_+(z)/z)=-\sum_{N\ge4}\frac{\mathcal G_N}{N}z^N,
\qquad
\wp_+(z)=z^{-2}+\sum_{6\mid N}(N-1)\mathcal G_Nz^{N-2}.
\tag{981.2}
$$
No factorial is included in $\mathcal G_N$.

Let $p=6h+5\ge41$ be an original prime, and put
$$
q=p^2,\quad d=\frac{p-1}{2}=3h+2,\quad
e=\frac{5p-1}{6}=5h+4,\quad m=\frac{p+1}{3}.
\tag{981.3}
$$
Use $r=2$ for $p\equiv11\pmod{12}$, and $r=8$ for $p\equiv5\pmod{12}$. Write $a=r+1$ and $n=p-r$. The four indices are
$$
\begin{array}{c|c}
\text{label}&N\\ \hline
\text{low}&a(p-1)\\
\text{low star}&a(p-1)+p+1\\
\text{high}&n(p-1)\\
\text{high star}&n(p-1)+p+1=np+a.
\end{array}
\tag{981.4}
$$
All are divisible by six, lie strictly below $q-1$, and satisfy $p\nmid N-1$. These statements follow directly from $r\in\{2,8\}$ and $p\ge41$. In the two star cases the residues of $N-1$ are respectively $-a$ and $r$; in the nonstar cases they are respectively $-a-1$ and $r-1$.

The method is valid more generally for any $6\mid N<q-1$ with $p\nmid N-1$. Set $M=N/6$.

## 2. The integral elliptic logarithm and a denominator-free residue formula

Choose the formal square-root parameter $s=x^{-1/2}$ with $s=t+O(t^7)$ at the origin, where $t=-x/y$. The branch of $y$ is
$$
x=s^{-2},\qquad y=-s^{-3}\sqrt{1+s^6}.
$$
Hence
$$
dz=\omega=\frac{ds}{\sqrt{1+s^6}},\qquad
z=L(s)=s f(s^6),
\tag{981.5}
$$
where
$$
c_j=\binom{-1/2}{j}=\frac{(-1)^j}{4^j}\binom{2j}{j},
\quad
f(X)=\sum_{j\ge0}\frac{c_j}{6j+1}X^j,
\quad
C(X)=(1+X)^{-1/2}=\sum_{j\ge0}c_jX^j.
\tag{981.6}
$$
Thus $f={}_2F_1(1/6,1/2;7/6;-X)$ and $6Xf'+f=C$.

Every coefficient of $f$ of degree $j<(q-1)/6$ is $p$-integral. One proof uses the actual strict Lubin–Tate isomorphism of R978: the parameter changes $s(t)$ and $t(s)$ are integral because two is a unit, and the strict Lubin–Tate logarithm is $T+O(T^q)$. Therefore $L(s)$ agrees below degree $q$ with an integral series. Section 3 also proves the integrality directly, with the one possible denominator-$p$ residue explicitly canceled.

Formal residue change of variables, over characteristic zero, gives
$$
\begin{aligned}
(N-1)\mathcal G_N
&=\operatorname{Res}_{z=0}\wp_+(z)z^{-(N-1)}\,dz\\
&=\operatorname{Res}_{s=0}
s^{-2}(s f(s^6))^{-(N-1)}C(s^6)\,ds\\
&=[X^M]\,C(X)f(X)^{1-N}.
\end{aligned}
\tag{981.7}
$$
Consequently the main computation is
$$
\boxed{\quad
\mathcal G_N\bmod p
=\frac1{N-1}[X^M]\,\overline C(X)\overline f(X)^{\,1-N}.
\quad}
\tag{981.8}
$$
This has no division by $N-2$.

For comparison, ordinary Lagrange inversion gives
$$
\mathcal G_N
=-\frac2{(N-1)(N-2)}[X^M]f(X)^{2-N}.
\tag{981.9}
$$
At the original high $r=2$ index,
$$
N-2=p(p-3).
$$
The coefficient in (981.9) is then divisible by $p$, and its reduction is zero. It cannot be divided by $p$ after reduction. Formula (981.7) avoids that artificial singularity by changing variables in the residue before division. The secondary arithmetic information is retained in the canonical integral coefficients of $f$, especially the resonance described next.

## 3. Two digits, including the unique resonance

Let $J<(q-1)/6$ be any cutoff, and write a coefficient index as $j=ip+b$, $0\le b<p$. In this range $2i+1<p$. The coefficients $c_i$ for the upper digit are all $p$-units.

Define the polynomial
$$
A(X)=\sum_{b=0}^d\frac{\overline c_b}{6b+1}X^b
\in\mathbb F_p[X],
\tag{981.10}
$$
and the nonzero constant
$$
\mathfrak c_p=(-1)^{e+1}4^{-e}
\frac{(2e-p)!}{(e!)^2}\pmod p.
\tag{981.11}
$$
Here all factorial arguments are strictly less than $p$.

If $0\le b\le d$, Lucas's theorem gives
$$
\frac{c_{ip+b}}{6(ip+b)+1}
\equiv c_i\frac{c_b}{6b+1}\pmod p.
\tag{981.12}
$$
There is no denominator divisible by $p$ in this range. If $d<b<p$ and $b\ne e$, the central binomial coefficient has one base-$p$ carry, while the denominator is a unit, so
$$
\frac{c_{ip+b}}{6(ip+b)+1}\equiv0\pmod p.
\tag{981.13}
$$
The single resonance is $b=e$, since $6e+1=5p$. In the stated cutoff range $6i+5$ is a unit: its first zero would be $i=h$, producing the excluded index
$$
hp+e=(q-1)/6.
$$
For this residue class the exact reduction is
$$
\boxed{\quad
\frac{c_{ip+e}}{6(ip+e)+1}
\equiv
\mathfrak c_p\,\frac{(2i+1)c_i}{6i+5}\pmod p.
\quad}
\tag{981.14}
$$

To verify the sign, put $v=2e-p$. Stripping powers of $p$ from factorials yields
$$
\frac1p\binom{2(ip+e)}{ip+e}
\equiv
-(2i+1)\binom{2i}{i}\frac{v!}{(e!)^2}\pmod p.
\tag{981.15}
$$
Indeed $(Ap+B)!/p^A\equiv(-1)^A A!B!\pmod p$ for the relevant $A,B<p$. The numerator has upper digit $2i+1$ and the two denominator factorials have upper digit $i$. Their Wilson signs leave the minus sign in (981.15). Multiplying by $(-1)^{ip+e}4^{-(ip+e)}$ gives $\mathfrak c_p(2i+1)c_i$. Division by $p(6i+5)$ now proves (981.14).

The three cases prove integrality of every selected logarithm coefficient. In particular the resonance is not set to zero merely because $c_{ip+e}\equiv0\pmod p$.

Equivalently, put $Y=X^p$ and
$$
D(Y)=\sum_{i\ge0}\frac{(2i+1)c_i}{6i+5}Y^i.
\tag{981.16}
$$
Only terms with $ip+e\le J$ are needed; they have $i<h$, so all these denominators are units. Then the entire required logarithm segment is represented by
$$
\boxed{\quad
\overline f(X)
\equiv A(X)(1+Y)^{-1/2}
+\mathfrak c_pX^eD(Y)\pmod{X^{J+1}}.
\quad}
\tag{981.17}
$$
Also
$$
\overline C(X)
\equiv (1+X)^d(1+Y)^{-1/2}\pmod{X^{J+1}}.
\tag{981.18}
$$
Thus only $d+1$ coefficients of $A$, at most $h$ coefficients of $D$, and the single constant (981.11) are needed as distinct input data.

There is a useful smaller recurrence for the second column. If
$$
R(Y)=(1+Y)^{1/2}D(Y),
$$
then
$$
6Y(1+Y)R'(Y)+(5+2Y)R(Y)=1,\qquad R(0)=1/5.
\tag{981.19}
$$
Indeed $D=(C-2J_5)/3$ for $J_5=\sum c_iY^i/(6i+5)$, and $6YJ_5'+5J_5=C$. Consequently
$$
R_i=-\frac{6i-4}{6i+5}R_{i-1},\qquad 1\le i<h.
\tag{981.20}
$$
All coefficients in this range are units. This statement alone does not imply that the final coefficient in (981.8) is a unit: that coefficient combines both columns.

## 4. Bounded exponent channels and the final linear sum

For $J<(q-1)/6$ one has $\lfloor J/p\rfloor\le h<d$. Hence
$$
\overline f(X^p)\equiv A(Y)\pmod{X^{J+1}},
\qquad
\overline f(X)^q\equiv1\pmod{X^{J+1}}.
\tag{981.21}
$$
For each original index write
$$
f(X)^{1-N}\equiv f(X)^u A(Y)^v
\pmod{X^{M+1}}.
\tag{981.22}
$$
The exponents are fixed small integers:
$$
\begin{array}{c|r|r}
\text{label}&u&v\\ \hline
\text{low}&a+1&-a\\
\text{low star}&a&-a-1\\
\text{high}&1-r&a\\
\text{high star}&-r&r.
\end{array}
\tag{981.23}
$$
For the high rows the omitted exponent is $-q$; for the low rows there is no omitted exponent. Equation (981.21) justifies both operations.

Let $T_u(X)=C(X)f(X)^u$, truncated after degree $M$, and let $A(Y)^v$ be truncated after degree $\lfloor M/p\rfloor$. Then
$$
\boxed{\quad
\mathcal G_N=
\frac1{N-1}
\sum_{j=0}^{\lfloor M/p\rfloor}
[Y^j]A(Y)^v\,[X^{M-pj}]T_u(X)
\pmod p.
\quad}
\tag{981.24}
$$
The final contraction has $O(p)$ terms. Negative powers use inverses of series with constant coefficient one. The only high-length operations are truncated multiplication and inversion over $\mathbb F_p$.

An independent exponent channel uses the same proved residue identity but a positive power:
$$
\mathcal G_N=
\frac1{N-1}[X^M]C(X)f(X)^{q+1-N}\pmod p.
\tag{981.25}
$$
The exponent is positive, and its difference from $1-N$ is $q$. It is computed directly, without the bounded-exponent table.

When $p\nmid N-2$, (981.9) yields a further check using
$$
-\frac2{(N-1)(N-2)}
[X^M]f(X)^{q+2-N}\pmod p.
\tag{981.26}
$$
When $p\mid N-2$, the coefficient in (981.26) must instead be zero and is not used to recover $\mathcal G_N$.

## 5. A separate input construction for the consumer

The second channel does not reuse (981.12)–(981.15) to form its logarithm coefficients. It iterates the rational recurrence
$$
c_0=1,\qquad
c_{j+1}=-\frac{2j+1}{2(j+1)}c_j.
\tag{981.27}
$$
At every step it stores the integer valuation $v_p(c_j)$ and the residue of the unit part $p^{-v_p(c_j)}c_j$. Every numerator and denominator is first divided by its exact power of $p$; the remaining denominator is inverted in $\mathbb F_p$. To obtain $c_j/(6j+1)$, the valuation of $6j+1$ is subtracted and its unit part is divided out.

This is rational arithmetic in the localized integers reduced only after exact powers of $p$ have been removed. In the required range the resulting valuation is nonnegative by Section 3. The consumer compares every required coefficient from (981.27) against the two-digit construction, including the resonance, before comparing the exponent channels. This separates an input-construction error from an exponent-reduction error.

## 6. Exact small-prime calibration and reused scales

For $p=41,47$ only, use the independent rational Laurent recurrence
$$
\wp_+(z)=z^{-2}+\sum_{j\ge1}x_jz^{6j-2},\qquad
x_1=-1/7,
$$
$$
x_j=\frac{\sum_{i=1}^{j-1}x_i x_{j-i}}
{(6j+1)(j-1)}\quad(j\ge2),\qquad
\mathcal G_{6j}=\frac{x_j}{6j-1}.
\tag{981.28}
$$
This follows by comparing coefficients in $\wp''=6\wp^2$ with the specified $g_3=-4$. The maximum index needed at these two primes is only a few hundred. The rational values are reduced modulo $p$ after checking their denominators, and their canonical numerator/denominator hashes are output. The method does not require such large rational arithmetic at $227$ or $857$.

The already registered R973 values are consumed, not recomputed:
$$
\begin{array}{c|rrrr}
p&41&47&227&857\\ \hline
c_n(E_-)&13&4&171&317\\
B_{\mathrm{old}}(E_-)&11&10&179&489.
\end{array}
\tag{981.29}
$$
Here $E_-:y^2=x^3-1$ has $g_3=4$. The balanced coefficient has weight $2n$ and $n\equiv3\pmod6$, so
$$
c_n(E_+)=-c_n(E_-)\pmod p.
\tag{981.30}
$$
For the second row of (981.29), $B_{\mathrm{old}}$ is the coefficient $x_{(p+1)/6}$ of that same $E_-$ Laurent expansion. Its change to $E_+$ multiplies it by $(-1)^{(p+1)/6}$.

Let $\mathscr B_p=E_{p+1}(E_+,\omega)$ in Robert's normalized Eisenstein convention, so $E_4=0,E_6=864$. The exact identity
$$
\mathcal G_k=-\frac{\mathrm B_k}{k!}\,E_k(E_+,\omega)
\tag{981.31}
$$
uses the ordinary Bernoulli number $\mathrm B_k$. Kummer's congruence gives
$$
\mathrm B_{p+1}\equiv1/12\pmod p,\qquad
(p+1)!/p\equiv-1\pmod p.
$$
Since $x_{(p+1)/6}=p\mathcal G_{p+1}$, equation (981.31) proves
$$
\boxed{\quad
\mathscr B_p
=12(-1)^{(p+1)/6}B_{\mathrm{old}}\pmod p.
\quad}
\tag{981.32}
$$
The small rational recurrence independently checks this scale at $41,47$. At the other two primes the program simply consumes the old constants in (981.29).

The R980 reflection is checked as an equality of independently computed residues:
$$
\mathcal G_{t(p-1)+p+1}
=\frac{\mathscr B_p}{12t}\mathcal G_{t(p-1)}
\pmod p,\qquad t=a,n.
\tag{981.33}
$$
The star values are not assigned by this relation. Nor is either pure coefficient assigned using a balanced Kronecker value.

### An explicitly unproved mixed comparison probe

The consumer also records a proposed comparison, separately from all proved checks. Put $\beta=\mathscr B_p/12$ and
$$
K_j=(p+1-j)(p-1)+p+1,\qquad
\xi_j=\frac{(-1)^{j+1}(j-2)!\,c_j(E_+)\,\beta^{1-j}}
{\mathcal G_{K_j}}\pmod p.
\tag{981.34}
$$
At $41,47$ it independently computes $\mathcal G_{K_3}$ and $\mathcal G_{K_6}$ and uses the exact initial coefficients
$$
c_3(E_+)=1/6,\qquad c_6(E_+)=-1/900.
$$
These follow from R975's original universal recurrence and are not newly computed balanced values. For these extra indices the bounded-exponent channel is $u=1-j$, $v=j-1$, since
$$
1-K_j=-q+(j-1)p+(1-j).
$$
Both indices are divisible by six, strictly below $q-1$, and have $K_j-1\equiv j-1\ne0\pmod p$. They are included in the same independent rational calibration at the small primes. Duplicate indices, such as a coinciding original high-star index, are computed only once.

For $j=n$, $K_n$ is exactly the already computed low-star index, and $c_n(E_+)$ is the signed old datum in (981.30). This probe is recorded at all four primes. The script reports whether the three available $\xi$ values agree at $41,47$, but does not assert agreement and does not make it a success condition. A zero denominator is recorded as such, with no ratio assigned. No mixed comparison theorem is claimed in this method. The same small-prime data also record the denominator-free necessary equality
$$
25\beta^3\mathcal G_{K_6}=4\mathcal G_{K_3}\pmod p.
\tag{981.35}
$$
This follows from $\xi_3=\xi_6$ using the two specified initial coefficients. Its two sides and their difference are printed even when a denominator in (981.34) vanishes. It is not an assertion or a success condition.

## 7. Execution contract and boundaries

Consumer: [original_pure_hurwitz_four_prime_consumer.py](../scripts/original_pure_hurwitz_four_prime_consumer.py).

It is guarded to run mathematical work only in Rogerhu12/math-research-public GitHub Actions. The required runtime is Python with python-flint==0.9.0. It requests exactly $41,47,227,857$ and has a bounded worker timeout. The only added indices are the two small-prime probes (981.34). The root agent owns workflow/request changes and execution.

For each prime the output records the original row, four indices, four computed residues, each comparison flag, the consumed scales, the input hashes, and unit/zero status. All summary data are deterministic; timing is printed separately. No full computed array or regenerable certificate is committed. An incomplete or failed run carries an explicit uncompleted list and proves nothing about those primes.

This proof and execution contract contains no run identifier or numerical result. A subsequent receipt must name the exact source commit, script hash, parameters, public run/job, output hash, and observed values before any finite computation is registered.

The method provides a direct finite-field consumer of R978's actual source. It does not yet establish nonvanishing for all primes, identify the two mirror coordinates, or turn the high trace into an original $Q'_h$ unit.

## Dependencies and primary implementation references

- [R978](../results/R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md), especially its strict original Lubin–Tate coordinate and selected-index normalization.
- [R980](../results/R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md), for the exact same-source Robert reflection.
- [R973](../results/R973-certified-balanced-Kronecker-coefficients-at-four-primes.md), for exactly the fixed source constants in (981.29).
- [R975](../results/R975-original-balanced-Kronecker-integral-heat-recurrence.md), for the balanced coefficient's weight and model normalization.
- NIST DLMF [§23.9](https://dlmf.nist.gov/23.9), for the ordinary Weierstrass Laurent convention. The recurrence (981.28) is derived directly from its differential equation.
- The pinned python-flint 0.9.0 primary documentation for [nmod_poly](https://python-flint.readthedocs.io/en/latest/nmod_poly.html): inverse_series_trunc, mul_low, and pow_trunc. Only exact finite-ring operations are used; no analytic log/exp series implementation is called in characteristic $p$.
