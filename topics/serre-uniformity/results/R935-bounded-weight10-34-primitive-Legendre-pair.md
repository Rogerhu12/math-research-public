# R935: A fixed weight-10/34 pair with no common original Legendre zero for sufficiently large primes

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved.** This gives two actual upper-half primitive labels, both at a fixed distance from the center, such that their original Legendre factors cannot both vanish outside an explicit fixed finite set. It does not prove a nonzero original low normal coefficient at either label, nor identify the actual weight-34 layer with its named CM vector.

The earlier R734/R741/R855 results already supply original unit norms or pairs at other labels. The new point here is a pair whose good Igusa weights stay equal to **10 and 34**, allowing the fixed-dimensional original source analysis of R918/R920 to be continued. Those earlier labels and their established conclusions are not recomputed.

## 1. Two always-primitive labels in the original set

Let $p\ge41$ be a prime with $p\equiv5\pmod{12}$, and set
$$
n=p+1,\qquad m=(p-1)/2,\qquad x=1/s,\quad s^2=-3.
$$
For the original Serre residual problem also impose $p\equiv2,5\pmod9$; the elementary Legendre assertion below holds without this extra restriction. Define
$$
h_8=\frac{p+9}{2}=\frac{n+8}{2},\qquad
h_{32}=\frac{p+33}{2}=\frac{n+32}{2}.
\tag{LP1}
$$
Writing $p=12t+5$ gives $h_8=6t+7$ and $h_{32}=6t+19$. Therefore both are odd and congruent to one modulo six. A common divisor of $h_r$ and $n$ divides $2h_r-n=r$. Since $r$ is a power of two and $h_r$ is odd, it follows that
$$
\boxed{(h_8,n)=(h_{32},n)=1.}
\tag{LP2}
$$
Moreover
$$
\frac n2<h_8<h_{32}\le p-4
$$
for every $p\ge41$. Thus both are genuine labels in the original interior primitive range. They are not half-period replacements or alternate norm extensions of one label.

Their actual R913/R916 parameters are
$$
\begin{array}{c|c|c|c}
h&r=2h-n&k_+=r+2&k_-=p+1-r\\ \hline
h_8&8&10&p-7\\
h_{32}&32&34&p-31.
\end{array}
\tag{LP3}
$$
In particular $2<k_\pm<p$ for this whole range. The full character remains $\chi_+(u)=\operatorname N(u)^{1-h_r}$ for the respective original label. Since $r=8,32$ are divisible by four, both descend through the actual $C_4$ Igusa quotient in this prime class.

The finite Legendre reflection used in R929 gives
$$
P_{h_8-1}(x)=P_{m-4}(x),\qquad
P_{h_{32}-1}(x)=P_{m-16}(x)
\quad\text{in }\mathbf F_p.
\tag{LP4}
$$
Both factors use the same original $x=1/s$, marking, period convention, and determinant extension.

## 2. The fixed integer controlling a simultaneous zero

Define positive integers by
$$
a_0=1,\qquad a_1=20,
$$
$$
\boxed{a_j=4(j+4)a_{j-1}+3(2j+7)^2a_{j-2}
\qquad(2\le j\le11).}
\tag{LP5}
$$
Put $A_{10,34}=a_{11}\in\mathbf Z_{>0}$. This is one fixed integer independent of $p$.

Then the exact finite-exception statement is
$$
\boxed{p\nmid A_{10,34}\ \Longrightarrow\
P_{h_8-1}(1/s)\ne0\ \text{or}\ P_{h_{32}-1}(1/s)\ne0.}
\tag{LP6}
$$
In particular an entirely explicit sufficient bound is
$$
\boxed{p>10^{22}.}
\tag{LP7}
$$
The bound is deliberately coarse; the theorem with the exact exception set in (LP6) does not require factorization of $A_{10,34}$.

## 3. Complete recurrence proof

Put
$$
F_j=P_{m-j}(x),\qquad 0\le j\le16.
$$
These indices are nonnegative because $m\ge20$. Reducing $m=-1/2$ modulo $p$ in the ordinary Legendre recurrence gives
$$
\boxed{(2j-1)F_j=4(j-1)xF_{j-1}-(2j-3)F_{j-2}
\qquad(2\le j\le16).}
\tag{LP8}
$$
The integers inverted here are at most $31$ and are units for every $p\ge41$.

Suppose $F_4=0$. R929 supplies $F_0=P_m(x)\ne0$. If also $F_3=0$, the recurrence at $j=4,3,2$ successively forces $F_2=F_1=F_0=0$, a contradiction. Hence
$$
F_4=0\quad\Longrightarrow\quad F_3\ne0.
\tag{LP9}
$$
Under this assumption write $F_j=b_jF_3$ for $j\ge3$, with $b_3=1$ and $b_4=0$. In particular $b_5=-7/9$. For $j\ge5$ define
$$
D_j=\prod_{k=5}^{j}(2k-1),\qquad K_j=D_jb_j,
$$
and put $K_4=0$. Multiplying (LP8) by $D_j$ gives
$$
K_5=-7,\qquad
K_j=4(j-1)xK_{j-1}-(2j-3)^2K_{j-2}\quad(6\le j\le16).
\tag{LP10}
$$
Since $x^2=-1/3$, induction using (LP5) proves
$$
\boxed{K_j=-7x^{j-5}a_{j-5}\qquad(5\le j\le16).}
\tag{LP11}
$$
For the step, divide the right-hand side of (LP10) by $-7x^{j-5}$. The coefficient of $a_{j-7}$ is
$-(2j-3)^2/x^2=3(2j-3)^2$, exactly the second coefficient in (LP5). The initial two values are $K_5=-7$ and $K_6=-140x=-7x\cdot20$.

Consequently
$$
\boxed{F_4=0\quad\Longrightarrow\quad
F_{16}=-\frac{7x^{11}A_{10,34}}{9\cdot11\cdot13\cdots31}\,F_3.}
\tag{LP12}
$$
Every displayed factor except possibly $A_{10,34}$ is a unit, including $F_3$ by (LP9). This proves (LP6) with no independence assumption on the two values.

For (LP7), all terms of (LP5) are positive. For $2\le j\le11$ its two coefficients satisfy
$$
4(j+4)\le60,\qquad 3(2j+7)^2\le2523.
$$
Starting from $a_0=1$, $a_1=20<100$, induction gives
$$
a_j<100^j\quad(1\le j\le11),
$$
since
$$
60\cdot100^{j-1}+2523\cdot100^{j-2}
=8523\cdot100^{j-2}<100^j.
$$
Thus $0<A_{10,34}<10^{22}$, so every prime above the bound is excluded from its prime divisors.

## 4. The corresponding complete weight-34 source space

The existing original geometry makes the new label usable without changing its tame problem. Retain R918/R920's $H_6$, deck action, $V_4^\dagger$, and
$$
X'(6)=\mathbf P^1_u,\qquad
W_6=\frac{E_6}{8u^3-1},\qquad W_6^2=-1728\eta^{24}.
$$
The weight-34 cusp forms have the same order-three stabilizer character as weight four. Division by $V_4^\dagger$, using its exact minimum divisor from R918, therefore identifies
$$
S_{34}(H_6)=V_4^\dagger M_{30}(H_6).
$$
On the coarse $\mathbf P^1$, the weight-30 line is the fifth power of the weight-six line of degree three. Consequently
$$
M_{30}(H_6)=W_6^5\langle1,u,u^2,\ldots,u^{15}\rangle.
$$
The deck transformation fixes $W_6$ and sends $u$ to $\zeta u$. Its invariant part is therefore
$$
W_6^5\langle1,u^3,u^6,u^9,u^{12},u^{15}\rangle.
$$
Because $E_6=(8u^3-1)W_6$ and $\eta^{12}=\pm W_6/(24s)$, an equivalent basis is
$$
\boxed{B_a=V_4^\dagger E_6^{5-a}\eta^{12a},\qquad0\le a\le5.}
\tag{LP13}
$$
This is the complete six-dimensional branch with the same transported deck character as the original CM vector. Its integrality and reduction can be checked exactly as in R920: on the fine full-six genus-one curve the weight-34 cusp line has degree $6\cdot34-12=192$, so $H^1$ vanishes; taking the actual tame and deck invariants uses only prime-to-$p$ averaging. In the same width-six variable $Q=q$ after $\tau'=6\tau$, one has
$$
V_4^\dagger=q+O(q^4),\quad E_6(6\tau)=1+O(q^6),\quad
\eta(6\tau)^{12}=q^3(1+O(q^6)).
$$
The coefficients of the six basis forms at $q,q^4,q^7,q^{10},q^{13},q^{16}$ form a triangular matrix with diagonal one. Thus (LP13) is a basis of the full integral lattice at every $p\ge41$, not just an unspecified finite-index sublattice.

For $h_{32}$, R916 supplies the nonzero normalized actual layer with content $\varpi^{32p}$ before reinstating the original $\varpi^{ea_{h_{32}}}$. Its entire holomorphic Igusa character space is identified with (LP13) by the same inverse Igusa construction as R920: $k_+=34<p+1$, the exponent $32$ descends through $C_4$, and the full character uniquely extends from one Igusa component to the other. Thus the actual vector lies nontrivially in this explicit six-dimensional space.

The named CM companion remains
$$
V_{34}^\dagger=F_{34}(Q)-2^{34}\zeta^2F_{34}(Q^4)
$$
with exactly the R913 phase and marking. This note does **not** prove that the whole residual Hecke packet in (LP13) is its one-dimensional span. In particular the weight-ten row with coefficient $8$ in R920 cannot be reused as a weight-34 rank assertion.

## 5. Exact scope after a Legendre-visible choice

For $p\nmid A_{10,34}$, choose $r\in\{8,32\}$ for which (LP6) holds. The choice is made at a real original primitive label, with all original norm and scalar conventions retained. This solves the Legendre part for one of two bounded good Igusa weights; it makes no replacement of the other factors.

The original first critical product at the chosen label is still
$$
P_{h_r-1}(1/s)\,f_{(h_r-7)/6}\,g_{(p-11)/6-(h_r-7)/6}.
$$
For $p=12t+5$, the two sigma pairs are respectively
$$
(f_t,g_{t-1}),\qquad(f_{t+2},g_{t-3}).
$$
These indices are nonnegative for $p\ge41$. Their nonvanishing is not proved here, and a value from one pair cannot be transferred to the other. The actual weight-34 source identification, its normal transport and specified low coefficient, and the separate height comparison remain necessary. Hence this theorem neither completes the same-label critical-jet problem nor Serre uniformity.

## Dependencies

- R929, §5: finite Legendre reflection and the original normalization; its proved ordinary unit supplies $F_0\ne0$.
- R913, §§3--7; R916: actual primitive labels, full norm characters, Igusa weights, actual nonzero normalized upper layer, and the fixed companion phases.
- R918, §§2--4; R920, §§2 and 5: exact tame divisor geometry, integral base change, and full two-component Igusa source space.
- R734/R741/R855: already established original unit-norm results at their own labels; no conclusion or computation from them is repeated or altered.
