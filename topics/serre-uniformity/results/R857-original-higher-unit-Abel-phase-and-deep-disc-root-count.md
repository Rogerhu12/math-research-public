# R857 — The original Abel phase and a deep-disc root bound from the higher unit

Date: 2026-11-16. Session: serre-public-astra-20261115 / sigma_uniform.

**Status: proved.** R855's individual higher-jet unit fixes the common $p$-adic phase of all jets at the same original embedding. It gives an integral restricted Abel series and a root bound on the original coarse disc. It does not give a unique center, a height nonvanishing theorem, or exclusion of the positive-rank rational-point candidates.

## 1. Statement in the original coordinates

Let $p>104190883$ be prime with $p\equiv2,5\pmod9$. Choose the actual pair $(m,h)=(m_a,h_a)$ supplied by R855, so
$$
m\equiv2\pmod3,\qquad (h,p+1)=1,\quad h\equiv1\pmod6,
\qquad v_p(M_{m,h})=-m.
\tag{857.1}
$$
All Hodge, tame, split, Cartan, and coefficient-embedding normalizations remain those of R575/R588/R592/R727. Put
$$
J=\frac{m+1}{3},\qquad
V=\frac{z_{\rm f}^3}{p^3},\qquad s=a-1.
\tag{857.2}
$$
The original raw scalar Abel primitive is
$$
\mathcal I_h(z_{\rm f})
=\sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}z_{\rm f}^{3j}.
\tag{857.3}
$$
There is a nonzero constant $b_h$ of valuation zero such that
$$
\boxed{
\mathcal G_h(V):=\frac{\mathcal I_h(z_{\rm f})}{p b_h}
\in V\mathbf Z_p\langle V\rangle,\qquad
[V^J]\mathcal G_h=1.
}
\tag{857.4}
$$
Let $r_h$ be the least index with unit coefficient in this series. Then
$$
1\le r_h\le J.
\tag{857.5}
$$
The original scalar primitive, or any nonzero constant multiple of it, has **exactly $r_h$ zeros counted with multiplicity** in the open coarse disc $v_p(s)>3$, over $\mathbf C_p$. In particular the number of noncentral zeros, counted with multiplicity, is at most $J-1$.

Using the explicit alternatives in R855, the sufficient bounds are
$$
\begin{array}{c|c|c}
p&J\text{ for the chosen }a\in\{0,2\}&
\text{number of noncentral zeros}\ \le\\\hline
18k+5&2k-a&2k-a-1\le (p-5)/9-1\\
18k+11&k-a&k-a-1\le (p-11)/18-1.
\end{array}
\tag{857.6}
$$
The table does not choose $a$ independently of R855's Legendre test: it is the same candidate whose finite norm and two Cartier factors were proved to be units.

## 2. A common phase, without declaring the quotient comparison a unit

The actual real Hecke field lies in $\mathbf Q(\zeta_{p+1})^+$. Since $p\equiv-1\pmod{p+1}$, its places above $p$ are split. Thus the component quotient differential in R727 §9 is defined over $\mathbf Q_p$. For that differential, R727 (727.29) gives the exact identity
$$
J_h(s)=c_h\mathcal I_h(z_{\rm f}(s))\in s\mathbf Q_p[[s]],
\qquad c_h\ne0.
\tag{857.7}
$$
The constant is independent of the order of differentiation. The flat/coarse inverse is defined over $\mathbf Q_p$ as a series in $z_{\rm f}^3$. Consequently
$$
c_hM_{3j-1,h}\in\mathbf Q_p\qquad(j\ge1).
\tag{857.8}
$$
This step is the original quotient and Kodaira--Spencer comparison, not a claim that arbitrary CM values lie in an unramified field.

The nonzero reference jet in (857.1) may now be used instead of $M_{2,h}$:
$$
\boxed{
\frac{M_{3j-1,h}}{M_{m,h}}\in\mathbf Q_p
\qquad(j\ge1).
}
\tag{857.9}
$$
In particular every nonzero jet has integer $p$ valuation, because $v_p(M_{m,h})=-m$ is an integer. Zero coefficients are allowed, with valuation $+\infty$. Also (857.8) shows $v_p(c_h)\in\mathbf Z$, but it does **not** show $v_p(c_h)=0$.

## 3. The entire Hodge tail and the normalization

R727 (727.28) is the uniform bound for every order at this actual primitive embedding:
$$
v_p\!\left(\frac{M_{r,h}}{r!}\right)
\ge-1-r\sigma,\qquad
\sigma=\frac p{p+1},\qquad r\ge0.
\tag{857.10}
$$
It comes from the one-$p$ denominator of the actual all-cusp Cartan-averaged vector and the original fine Gauss--Manin change. The stronger lattice assertion special to $h=1$ is not used.

Set
$$
A_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!}.
$$
Putting $r=3j-1$ in (857.10) gives, with the factorial division preserved,
$$
v_p(A_{j,h})\ge
\frac{3j-1}{p+1}-v_p(3j).
\tag{857.11}
$$
If $p\nmid3j$, the right side is strictly positive. If $t=v_p(3j)\ge1$, then $3j\ge3p^t$ because $p\ne3$, and the right side is at least
$$
\frac{3p^t-1}{p+1}-t>1.
\tag{857.12}
$$
At $t=1$ this is $2-4/(p+1)>1$; the difference on increasing $t$ by one is $3p^t(p-1)/(p+1)-1>0$. All valuations on the left are integers by (857.9). We have therefore proved
$$
v_p(A_{j,h})\ge1\quad(j\ge1),\qquad
v_p(A_{j,h})\longrightarrow+\infty.
\tag{857.13}
$$
The latter assertion also follows directly from (857.11), since its linear term dominates $v_p(3j)\le\log_p(3j)$. Thus every factorial-divisible and arbitrarily late index has been included.

For $j=J$, R855 gives $m+1=3J<p$, so the factorial is a unit and
$$
v_p(A_{J,h})=(m+1)+v_p(M_{m,h})=1.
\tag{857.14}
$$
Define the actual nonzero unit-phase constant
$$
b_h=A_{J,h}/p.
\tag{857.15}
$$
It need not itself belong to $\mathbf Q_p$. Nevertheless every ratio
$$
\frac{A_{j,h}}{p b_h}
=\frac{A_{j,h}}{A_{J,h}}
\in\mathbf Q_p
$$
does belong to $\mathbf Z_p$, tends to zero, and equals one at $j=J$, by (857.9) and (857.13)--(857.14). This proves the full restricted-series statement (857.4).

For the actual quotient differential one may equivalently normalize by the rational constant $c_h p b_h\in\mathbf Q_p^\times$. Its valuation is $v_p(c_h)+1$. The comparison scalar has been retained throughout.

## 4. The zero count uses the first unit coefficient

Write $\mathcal G_h(V)=\sum_{j\ge1}a_jV^j$ and let $r_h$ be as in (857.5). Reduction modulo $p$ has the form
$$
\overline{\mathcal G_h}(V)=V^{r_h}\overline U(V),
\qquad \overline U(0)\ne0.
$$
Formal Weierstrass preparation over the complete DVR $\mathbf Z_p$ gives
$$
\mathcal G_h(V)=P_h(V)U_h(V),
$$
$$
P_h(V)=V^{r_h}+\sum_{i=0}^{r_h-1}b_iV^i,
\quad b_i\in p\mathbf Z_p,\qquad
U_h\in\mathbf Z_p[[V]]^\times.
\tag{857.16}
$$
For clarity, the elementary preparation statement here follows by successive lifting: modulo $p$ start with $V^{r_h}\overline U$; at each $p$-power precision divide the error after multiplication by the inverse unit by the monic $V^{r_h}$, putting the remainder of degree less than $r_h$ into $P_h$ and the quotient into $U_h$. The corrections are divisible by the increasing powers of $p$, so completeness gives the displayed factorization. Its constant term implies $b_0=0$, since $\mathcal G_h(0)=0$ and $U_h(0)$ is a unit.

For every $v_p(V)>0$, the series $U_h$ converges and is nonzero: its constant term is a unit and all its other terms have positive valuation. Every root of $P_h$ lies in that open disc. A root of negative valuation is excluded by dominance of the monic leading term, and a root of zero valuation is excluded because all lower coefficients are divisible by $p$. The degree-$r_h$ polynomial has exactly $r_h$ roots over $\mathbf C_p$, counted with multiplicity. Thus (857.16) proves that the zeros of $\mathcal G_h$ in $v_p(V)>0$ number exactly $r_h$.

This uses the **least** unit coefficient. A higher unit does not itself become the leading term, and there is no claim that its monomial dominates terms of lower degree. The center is among these zeros, so at most $r_h-1\le J-1$ are noncentral.

## 5. Transport to the actual coarse disc and scope

The flat/coarse change of R727 §9, independently of any first-jet-unit hypothesis, is
$$
V=\Psi(s/p^3),\qquad
\Psi(v)=\frac38v+\sum_{r\ge2}\psi_rv^r,
\quad\psi_r\in p\mathbf Z_p.
\tag{857.17}
$$
It is an integral analytic automorphism of the open unit disc; its inverse has a unit linear term, and both maps preserve valuations and multiplicities. Consequently the exact root count above transfers to $v_p(s)>3$. The cube in $V=z_{\rm f}^3/p^3$ has already descended to the coarse parameter. It does not multiply the number of coarse zeros by three.

For the two cases in R855, $m=eM-3a-3$, so
$$
J=(eM-2)/3-a.
$$
When $p=18k+5$, one has $e=2$, $M=3k+1$ and $J=2k-a$; when $p=18k+11$, one has $e=1$, $M=3k+2$ and $J=k-a$. This proves (857.6).

Every simultaneous zero of the whole original Abel increment is in particular a zero of this selected component, so the same upper bound holds for that subset. A positive-rank rational-point candidate is not, however, known to make the Abel increment vanish. Its image may be a nonzero multiple of the original Mordell--Weil line. This argument does not remove that line, the actual height comparison constants, the original second-kind periods, or the linear height term. It proves neither that $r_h=1$ nor that the noncentral zeros are absent. Those are genuine remaining conditions.

## Sources

- [R855](R855-original-primitive-higher-Abel-unit-from-cubic-Cartier.md): the same original primitive embedding and higher-jet valuation.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), (727.28)--(727.31), §9: all-order one-$p$ Hodge bound, rational quotient phase, and the actual coarse change.
- [R705](R705-actual-higher-Abel-blocks-and-uniform-order-bound.md), §§7--8: separation of the elliptic and modular flat coordinates and retention of the quotient comparison scalar.

The proof uses no new arithmetic execution or finite prime window.
