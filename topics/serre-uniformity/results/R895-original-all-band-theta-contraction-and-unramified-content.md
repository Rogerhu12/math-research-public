# R895 — All lower bands of the original divided theta contraction

Date: 2026-11-16. Status: proved a closed formula for every band through the original $p$-dividing precision, on the unramified source class of R892. For the original odd primitive label, an integral value of $\mathcal C_h(S)/p$ on this source class always has zero reduction. The formula keeps the entire $36$-dimensional tame multiplicity space and gives a precise criterion on the specified source $x\otimes(-xy)$. It does not decide the original R770 same-label scalar criterion.

## 1. Original operators and the source class

Use exactly R889/R892:
$$
p\ge41,\quad p\equiv5\pmod6,\quad
k=\mathbf F_{p^2},\quad e=p^2-1,\quad n=p+1,
$$
$$
E_0:y^2=x^3-1,\quad dz=dx/(2y),\quad
\kappa=-6B\in\mathbf F_p^\times,
$$
$$
[D,Q]=1,\quad D^p=Q^p=0,\qquad
\Theta_j=[Y^j]\rho(\tau(P_Y)),\qquad
\Theta_p=\kappa Q.
\tag{895.1}
$$
The distributions are those of the actual symmetric theta action. In particular their full expression is not replaced by an ordinary exponential.

Put
$$
\mathcal H=H^0(E_0,O(6pO)),\qquad
\mathcal H_0=\ker D,\qquad
\mathcal M=\mathcal H_0\otimes_k\mathcal H_0.
$$
R889 gives the actual direct sum
$$
\mathcal H=\bigoplus_{r=0}^{p-1}Q^r\mathcal H_0,
\qquad \dim_k\mathcal H_0=6,\qquad \dim_k\mathcal M=36.
\tag{895.2}
$$
Write $|r,s\rangle m=(Q^r\otimes Q^s)m$, for $m\in\mathcal M$. The notation $\langle r,s|$ denotes the coefficient projection in (895.2), with no apolar or Hermitian normalization added. Thus
$$
\overline S=\sum_{r,s=0}^{p-1}|r,s\rangle S_{r,s},
\qquad S_{r,s}\in\mathcal M.
\tag{895.3}
$$
All formulas below act as the identity on this actual tame multiplicity space.

Fix the original label
$$
7\le h\le p-4,\qquad h\equiv1\pmod6,\qquad (h,p+1)=1.
\tag{895.4}
$$
As in R892, $S$ is an integral section on the original unramified smooth model over $R=W(k)$, allowing the stated unramified extension for the tame marking, and is then base changed to the ramified torsion ring $R'$. An arbitrary $R'$-lift differing only by its uniformizer is not included.

Let $X$ be the formal scalar of R892 and write
$$
\lambda=X^{p-1}.
\tag{895.5}
$$
This is a reindexing of a formal operator polynomial, not a new elliptic parameter. All congruences in $\lambda$ below are modulo $\lambda^{p+2}$, equivalently retaining the nonzero power-sum bands through $X^e$.

## 2. A limited normal-order formula which does retain the cross-$p$ corrections

For $0\le i,j<p$, put $c=\kappa/2$ and define
$$
F_{i,j}=
\sum_{b=0}^{\min(i,j)}
\frac{\kappa^{i-b}c^b}
 {(i-b)!(j-b)!b!}\,
Q^{i-b}D^{j-b}.
\tag{895.6}
$$
The precise statement needed is
$$
\Theta_{ip+j}=F_{i,j}+E_{i,j},
\tag{895.7}
$$
where $E_{i,j}$ is a sum of normal monomials $Q^aD^b$ with
$$
0\le a,b<p,\qquad a\le i,\qquad
b-a=p+1+j-i.
\tag{895.8}
$$
In particular
$$
\boxed{\Theta_{ip+j}=F_{i,j}\quad\text{if }i\le j+1.}
\tag{895.9}
$$
The assertion is not that $E_{i,j}$ always vanishes.

Here is a derivation from the actual R892 recursion. With $H_i=\Theta_{ip}$, its specialization $m=p$, $n=(i-1)p$ gives
$$
iH_i=\kappa QH_{i-1}
-\sum_{a=2}^{i-1}\frac{c^a}{a!}
 \Theta_{ip-(p+1)a}\qquad(2\le i<p).
\tag{895.10}
$$
The two terms linear in $c$ cancel. Every distribution on the right in the sum has quotient digit at most $i-3$. Induction therefore shows that the normal $Q$ degree of $H_i$ is at most $i$.

The coefficient of the first translation parameter in the same group law gives
$$
\Theta_{ip+j}
=\sum_{a=0}^{\min(i,j)}
 \frac{(-c)^a}{a!(j-a)!}\,D^{j-a}H_{i-a}.
\tag{895.11}
$$
Thus its normal $Q$ degree is at most $i$ as well. The actual norm-one action gives a normal monomial in this distribution the congruence
$$
b-a\equiv j-i\pmod{p+1}.
$$
The bounds $0\le a,b<p$ allow at most the ordinary difference $j-i$ and the two differences obtained by adding or subtracting $p+1$. The negative alternative would require $a>i$, and is excluded. This proves the description of the possible correction branch.

In $H_i$ the ordinary branch can only be $Q^i$; (895.10) gives its coefficient $\kappa^i/i!$. Substituting these ordinary branches into (895.11) and normally ordering $D^{j-a}Q^{i-a}$ gives (895.6). For a fixed total contraction index the finite binomial sum is $(\kappa-c)^b=c^b$. The correction branches remain of difference (895.8) under this operation. This proves (895.7).

For example the genuine term
$$
-\frac{\kappa^2}{24(p-2)!}D^{p-2}
$$
in $\Theta_{3p}$ belongs to (895.8). It is retained by this argument. The full Teichmueller group is not being asserted to act by global elliptic automorphisms; only the actual norm-one theta action, and weights modulo $p+1$, were used.

## 3. Exact reindexing of the original flags

Start with the actual R892 sums, including their original $\gamma$ and $1/2$. In the trace set $a=-v/\gamma$. Since $\overline\gamma=-\gamma$, its two original coordinates become $(a,-\overline a)$. In the Gauss sum set $a=u/2$. The equality $\theta_h(2)=1$ follows from its triviality on $\mathbf F_p^\times$. These are bijective reindexings of complete finite sums, so
$$
\mathscr T(\lambda)
=\sum_{a\in k}\mathscr R_a(X)\otimes\mathscr R_{-\overline a}(X),
$$
$$
\mathscr G_h(\lambda)
=\sum_{a\in k^\times}a^{-h(p-1)}
 \mathscr R_a(X)\otimes\mathscr R_{\overline a}(X).
\tag{895.12}
$$
The original marking, symmetric lifts, and section source have not changed.

Finite-field power sums give only degrees which are multiples of $p-1$. For $2\le l\le p+1$ the trace band is
$$
T_l=(-1)^{l+1}\sum_{k=1}^{l-1}
 \Theta_{lp-k(p+1)}\otimes\Theta_{k(p+1)-l},
\qquad
\mathscr T=\sum_{l=2}^{p+1}\lambda^lT_l.
\tag{895.13}
$$
For $l=p+1$ the displayed range is $1\le k\le p$ and includes both endpoints with an identity distribution. There is no degree-zero term in the reduction: its integral value is $p^2$.

Likewise
$$
G_l=-\sum_k
 \Theta_{lp-h-k(p+1)}\otimes
 \Theta_{h+k(p+1)-l},
\qquad
\mathscr G_h=\sum_{l\ge1}\lambda^lG_l,
\tag{895.14}
$$
where exactly those integers $k$ for which both indices are nonnegative are used. Their sum is $l(p-1)$, so this also supplies the upper bound. The original Gauss character has not been inverted. Its integral constant term is exactly zero.

## 4. Closed formula for every trace band

Set
$$
\delta=p+1-l,\qquad L=l-2=p-1-\delta.
$$
The two digit pairs in each summand of (895.13) satisfy $i\le j$. Thus (895.9) applies to every one of them. Expanding (895.6), and summing the two scalar contraction indices, gives
$$
T_l=(-1)^{l+1}\kappa^L
\sum_{\substack{i,j\ge0\\i+j\le L}}
\frac{Q_1^iD_1^{i+\delta}
      Q_2^jD_2^{j+\delta}}
 {i!j!(i+\delta)!(j+\delta)!(L-i-j)!}.
\tag{895.15}
$$
All denominators are factorials of integers below $p$.

This kills $|u,v\rangle$ unless $u,v\ge\delta$. Write $u=\delta+r$, $v=\delta+s$, with $0\le r,s\le L$. After multiplication by $L!$, the scalar sum in its action is the coefficient of $x^ry^s$ in
$$
\sum_{i+j\le L}
 \binom{L}{i,j,L-i-j}
 x^iy^j(1-x)^{L-i}(1-y)^{L-j}
=(1-xy)^L.
\tag{895.16}
$$
Indeed
$$
\binom{\delta+r}{\delta+i}
=\binom{\delta+r}{r-i}
\equiv(-1)^{r-i}\binom{L-i}{r-i}\pmod p,
$$
and likewise for the second factor. Consequently
$$
\boxed{
T_l=\frac{(-1)^{l+1}\kappa^{l-2}}{(l-2)!}
 \sum_{r=0}^{l-2}(-1)^r\binom{l-2}{r}
 |r,r\rangle\langle p+1-l+r,p+1-l+r|.
}
\tag{895.17}
$$
This is a direct finite identity; it does not require an unproved integral function-value realization.

Define Laurent-polynomial maps with values in the actual tame space:
$$
V(\lambda)m=\sum_{r=0}^{p-1}
 \frac{(\kappa\lambda)^r}{r!}|r,r\rangle m,
$$
$$
W(\lambda)\overline S
=\sum_{u=0}^{p-1}u!(\kappa\lambda)^{-u}S_{u,u}.
\tag{895.18}
$$
Wilson's identity and $\kappa^{p-1}=1$ rewrite (895.17) as
$$
\boxed{
\mathscr T(\lambda)
\equiv\lambda^{p+1}V(\lambda)W(\lambda)
 \pmod{\lambda^{p+2}}.
}
\tag{895.19}
$$
In the product on the right, terms of degree above $p+1$ are discarded. Its smallest degree is two. Formula (895.19) is a limited, proved factorization of the complete trace through the indicated precision. It is not a full exponential formula for an individual theta translation.

## 5. Which source components can enter the lower divided bands?

Because $V$ has nonnegative powers, only the nonpositive powers of $W\mathscr G_h$ can contribute to $\mathscr T\mathscr G_h$ through degree $p+1$.

Consider $|r,s\rangle m$ and a band $G_l$ which has a diagonal output $|u,u\rangle$. A nonpositive power of $W\mathscr G_h$ requires
$$
a=u-l\ge0.
\tag{895.20}
$$
In particular $l\le u\le p-1$. The exact index congruences in (895.14), followed by the actual norm-one weights, give
$$
r\equiv a-h,\qquad s\equiv a+h\pmod{p+1}.
\tag{895.21}
$$
The missing primary index is $p$, not an additional basis vector.

If $a\ge h$, then $r=a-h$ and $u-r=l+h$. This is impossible: the normal $Q$ degree of each distribution involved is at most its quotient digit, hence at most $l-1$. If $a+h\ge p+1$, the same argument on the second factor gives the impossible increase $l+p+1-h$. The boundary value $a+h=p$ would give the missing index $s=p$.

It follows that the only possible inputs are
$$
\boxed{
r_a=p+1-h+a,\qquad s_a=h+a,\qquad
0\le a\le A_h:=\min(h-2,p-h-1).
}
\tag{895.22}
$$
Both indices lie in $0,\ldots,p-1$. Notice
$$
r_a+s_a=p+1+2a.
\tag{895.23}
$$

For these inputs the required total primary degree change is
$$
2u-r_a-s_a=2l-p-1.
\tag{895.24}
$$
If the two distribution indices have digit pairs $(i_1,j_1)$ and $(i_2,j_2)$, their sum $l(p-1)$ permits $i_1+i_2=l-1$ or $l-2$. The ordinary branches in the first case have exactly the degree change (895.24); the second case is smaller by $p+1$. Every correction branch (895.8) decreases it by another $p+1$. Therefore only the two ordinary branches with $i_1+i_2=l-1$ can enter the coefficient under consideration.

This is the precise reason all genuine cross-$p$ corrections are invisible in this particular nonpositive part of $W\mathscr G_h$. They have not been discarded from the theta action as a whole.

## 6. The exact coefficient and its parity

For the input (895.22), all contributions to the nonpositive part have the same power $\lambda^{-a}$. Write their scalar as $C_a$. Then
$$
\bigl[W(\lambda)\mathscr G_h(\lambda)
 |r_a,s_a\rangle m\bigr]_{\le0}
=C_a\lambda^{-a}m.
\tag{895.25}
$$
We now compute $C_a$ with all factorials retained.

For this calculation only, use the ordinary normal expression
$$
e^{\kappa d^pX^pQ}e^{dXD}e^{(\kappa/2)d^{p+1}X^{p+1}}.
\tag{895.26}
$$
Its ordinary digit branch is (895.6); every extra digit-carry branch has its primary degree lowered by $p+1$. Thus §5 proves that (895.26) gives the exact coefficient in (895.25), without asserting equality with the actual theta action.

The pairing underlying $W$ is
$$
\langle Q^i,Q^j\rangle_A=\delta_{ij}i!A^{-i},
\qquad A=\kappa X^{p-1}.
$$
The elementary exponential generating-function identity for this pairing gives, after including the two scalar factors in (895.26),
$$
e^{2\kappa d^{p+1}X^{p+1}}
\sum_{j=0}^{\min(r_a,s_a)}
 \binom{r_a}{j}\binom{s_a}{j}j!A^{-j}
 (2dX)^{r_a-j}(2d^pX)^{s_a-j}.
\tag{895.27}
$$
One may prove this identity over $\mathbf Q$ by pairing two generating exponentials and then differentiating in their polynomial shifts.

Its use modulo $p$ at this coefficient is legitimate. In the original pairing sum, let $b\ge0$ denote the degree supplied by its scalar exponential. A formally added diagonal index $u\ge p$ could contribute to $X^{-a(p-1)}$ only when its two polynomial indices satisfy $j+k=u+a+1+b$. This forces both exponential factorial indices $u-j$ and $u-k$ below $p$; otherwise the other polynomial index would exceed $p-1$. Also $b\le r_a+s_a-u-a-1=p+a-u\le a<p$. Its numerator $u!$ is therefore divisible by $p$ with all these denominators units, so that added term is zero modulo $p$. For an actual index $u<p$, the same equality and $j,k\le u$ give $b\le u-a-1<p$, again with all factorial denominators units. On the right of (895.27), the contributing exponential degree is $j-a-1<p$. Thus no cancellation of a hidden factor $p$ is used.

Multiply by $d^{-h(p-1)}$ and sum over $d\in k^\times$. The required power of $X$ in (895.27) has exponential degree $j-a-1\ge0$. The power of $d$ is then zero modulo $e$, so the finite sum is $-1$. Using $2^p=2$ in $k$ yields
$$
C_a=-\kappa^{-a-1}
 \sum_{j=a+1}^{\min(r_a,s_a)}
 2^{a+1-j}
 \binom{r_a}{j}\binom{s_a}{j}
 \frac{j!}{(j-a-1)!}.
\tag{895.28}
$$
The two factors of two in (895.27), and hence the power in (895.28), come from the original plus-flag contraction. They were not set to one before the finite sums.

Put $m=a+1$ and use the falling factorial $(r)_m=r(r-1)\cdots(r-m+1)$. The sum in (895.28) is
$$
(r_a)_m\,[t^{h-1}]
 (1+t)^{h+a}(1+t/2)^{p-h}.
$$
Since $h<p$, the freshman-power identity reduces the requested coefficient to
$$
(r_a)_m\,[t^{h-1}]
 (1+t)^a
 \left(\frac{1+t}{1+t/2}\right)^h.
\tag{895.29}
$$
All these identities concern coefficients below degree $p$.

Let
$$
z=\frac{t(1+t/2)}{1+t},\qquad
w=1+t=z+\sqrt{1+z^2},\qquad w(0)=1.
$$
Lagrange inversion, with the invertible integers $h,m$, gives
$$
[t^{h-1}](1+t)^a
 \left(\frac{1+t}{1+t/2}\right)^h
=\frac h m[z^h]w^m.
\tag{895.30}
$$
The formal function $w^m$ satisfies
$$
(1+z^2)(w^m)''+z(w^m)'-m^2w^m=0.
$$
Its odd coefficients, starting with $[z]w^m=m$, therefore give, for the original odd $h$,
$$
[z^h]w^m
=\frac{m}{h!}
 \prod_{\substack{1\le j<h\\j\ {\rm odd}}}(m^2-j^2).
\tag{895.31}
$$
Combining (895.28)--(895.31) proves
$$
\boxed{
C_a=
-\frac{\kappa^{-a-1}(r_a)_{a+1}}{(h-1)!}
 \prod_{\substack{1\le j<h\\j\ {\rm odd}}}
 \bigl((a+1)^2-j^2\bigr).
}
\tag{895.32}
$$

The range (895.22) gives $m\le h-1$ and $m\le p-h$. If $a$ is even, $m$ is odd and is one of the odd factors in (895.32), so $C_a=0$. If $a$ is odd, $m$ is even; no $m-j$ is zero, and
$$
0<m+j\le m+h-2\le p-2.
$$
Each nonzero difference has absolute value below $p$. The falling factorial has factors in $p-h+1,\ldots,r_a\subset\{1,\ldots,p-1\}$, and $(h-1)!$ is a unit. Therefore
$$
\boxed{C_a=0\ \text{for even }a,\qquad
       C_a\in k^\times\ \text{for odd }a.}
\tag{895.33}
$$
This establishes the zero and unit statements for every allowed boundary value, without an additional numerical check.

## 7. Complete band formula and the actual divided-content consequence

Write $\mathscr K_h=\mathscr T\mathscr G_h$, as in R892. Equations (895.19), (895.25), and (895.33) give the closed formula
$$
\boxed{
\mathscr K_h(\lambda)\overline S
\equiv
\sum_{\substack{1\le a\le A_h\\a\ {\rm odd}}}
 C_a\sum_{v=0}^{a}
 \frac{\kappa^v}{v!}
 \lambda^{p+1-a+v}
 |v,v\rangle S_{r_a,s_a}
 \pmod{\lambda^{p+2}}.
}
\tag{895.34}
$$
Every band through $X^e$ is displayed. In particular no lower bands have been left as unspecified recursions. The earliest possible nonzero band is
$$
l=p+1-A_h=\max(p-h+3,h+2),
$$
since $A_h$ is odd. This is a possible band for the operator, not a claim about the given source.

For any fixed odd $a$, the projection to $\mathcal M=|0,0\rangle\mathcal M$ of band $p+1-a$ is exactly $C_aS_{r_a,s_a}$. Distinct $a$ have distinct such bands. Hence
$$
\boxed{
K_{h,n}(\overline S)=0\text{ for all }n<e
\quad\Longleftrightarrow\quad
S_{r_a,s_a}=0
\text{ for every odd }a\in[1,A_h].
}
\tag{895.35}
$$
When these conditions hold, (895.34) also gives $K_{h,e}(\overline S)=0$.

Apply R892 on its unramified source class. Its exact original normalization is $\varpi^e/p\equiv+1$, and pullback from the actual quotient is saturated. Thus
$$
\boxed{
\mathcal C_h(S)/p\text{ is integral}
\quad\Longleftrightarrow\quad
S_{r_a,s_a}=0\text{ for every odd }a\in[1,A_h].
}
\tag{895.36}
$$
Moreover
$$
\boxed{
\mathcal C_h(S)/p\text{ integral}
\ \Longrightarrow\
\mathcal C_h(S)/p\in\varpi\mathcal U_L.
}
\tag{895.37}
$$
In particular an integral value of this divided contraction on the stated unramified source class never has unit content.

There is no contribution to its reduction from trace terms above $X^e$: before division they have valuation at least $e+1$, and after division at least one. The same estimate applies to all positive-degree coefficient changes by a multiple of $p$. The actual degree-zero Gauss sum is exactly zero, while the actual degree-zero trace is $p^2$, not an omitted multiple of $p$. Finally saturation of $\pi_L^*\mathcal U_L$ preserves these valuations; descent cannot turn any discarded higher-valuation term into a unit. These are precisely R892's precision conditions.

If some selected component is nonzero, let $a_*$ be the largest odd $a$ for which it is nonzero. Formula (895.34) and the unit $C_{a_*}$ give the exact content valuation
$$
\operatorname{ord}_\varpi\mathcal C_h(S)
=(p-1)(p+1-a_*)<e.
\tag{895.38}
$$
This is a value for the actual unramified source and the original uniformizer; it is not a valuation of the R770 scalar. When all selected components vanish, only the lower bound $\operatorname{ord}_\varpi\mathcal C_h(S)\ge e+1$ is asserted.

## 8. The specified original source and the remaining comparison

For the original source of R886/R892 set
$$
S_{F,G}=(x s_{6p})\otimes(-xy s_{6p}),
$$
$$
V_0=\sum_{j=0}^{p-1}\frac{(-1)^jQ^jD^j}{j!},\qquad
A_r=\frac1{r!}V_0D^r(x s_{6p}),\qquad
B_s=\frac1{s!}V_0D^s(-xy s_{6p}).
\tag{895.39}
$$
These are actual elements of $\mathcal H_0$, and
$$
(S_{F,G})_{r,s}=A_r\otimes B_s.
\tag{895.40}
$$
Consequently its criterion in (895.36) is exactly
$$
\boxed{
A_{p+1-h+a}\otimes B_{h+a}=0
\quad\text{for every odd }a\in[1,A_h].
}
\tag{895.41}
$$
Over $k$, each equality means that at least one of those two actual tame vectors is zero. No dimension count replaces it.

There is also the original differential identity
$$
-xy=-D^3x/24.
$$
It gives
$$
B_s=-\frac{(s+1)(s+2)(s+3)}{24}A_{s+3}
 \quad(0\le s\le p-4),\qquad
B_s=0\quad(p-3\le s\le p-1).
\tag{895.42}
$$
This records some exact boundary zeros of (895.41), but does not decide all its factors. The six-dimensional multiplicities in (895.39)--(895.42) have not been collapsed to an arbitrarily selected coordinate.

These are the vacuum coefficients of the original unpowered sections in $H^0(O(6pO))$. They are not the ordinary sigma coefficients $f_i,g_j$ in R770. In particular the R889 explicitly constructed same-label Frobenius-source section uses primary indices $p-h,h-1$, of total degree $p-1$. All potentially contributing indices in (895.34) have total degree at least $p+3$. Therefore its separate fifth-jet identity cannot be substituted for the contraction in this theorem.

R895 closes the proposed unit-content route through $\mathcal C_h(S)/p$ on the specific unramified source class: that divided vector cannot be an integral unit there. It does not prove that the original primitive/Legendre scalar vanishes, and does not assert anything analogous for arbitrary ramified sources or a differently normalized divided contraction. The original $N_h$ and its Legendre factor from R886 remain unchanged. A comparison involving a genuine ramified source, a different justified valuation layer, or the exact R770 scalar would still require a new proof.

## Sources

- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md), §§2--7: actual $D,Q$, the six-dimensional vacuum, normal torus weights, and the separate original sigma jet formula.
- [R892](R892-original-theta-recursion-and-divided-split-contraction.md), §§2--6: full genuine distribution recursion, original uniformizer and positive unit, two-flag operator order, unramified precision, and saturated descent.
- [R886](R886-original-two-flag-theta-descent-and-split-contraction.md), §§1--7: actual two flags, original Gauss character, descended module, contraction, and period norm.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the distinct same-original-label scalar criterion.

All identities above are paper derivations from the fixed original operators. No new mathematical computation, local experiment, or finite prime scan was used.
