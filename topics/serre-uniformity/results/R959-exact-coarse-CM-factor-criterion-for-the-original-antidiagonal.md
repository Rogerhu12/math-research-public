# R959 — An exact coarse CM factor criterion for the original antidiagonal

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved global polynomial descriptions, exact extra zero orders, and the common-factor criterion.** These are structure statements for the actual families of R949/R954 and their fully filtered source of R957. They do not exclude the resulting common linear factor. No new mathematical computation is performed; the two finite zeros used in §5 are reused from R945.

## 1. The odd CM family has a full-level quotient

Use exactly the four theta terms in R954(954.8), with its odd theta convention. Put
$$
R_a(z,\tau)=\theta_a^*(z;\tau)\theta_a(sz;\tau)
\quad(a=2,3,4),\qquad
R_0(z,\tau)=\theta^*(z;\tau)\theta(sz;\tau).
$$
Then $J_o=(R_2+R_3+R_4-sR_0)/2$.

Under $T:\tau\mapsto\tau+1$, the odd theta and $\theta_2$ acquire the factor $e^{\pi i/4}$, while $\theta_3$ and $\theta_4$ interchange. Since $\eta$ acquires $e^{\pi i/12}$, R954's exact quotient definitions give
$$
R_2\mapsto\rho R_2,\qquad
R_3\mapsto\rho R_4,\qquad
R_4\mapsto\rho R_3,\qquad
R_0\mapsto\rho R_0.
$$
In particular
$$
J_o(z,\tau+1)=\rho J_o(z,\tau).
\tag{CM1}
$$

Under $S:(z,\tau)\mapsto(z/\tau,-1/\tau)$, write $v=\sqrt{-i\tau}$ with the consistent theta multiplier. The transformation factors are
$$
\eta\mapsto v\eta,\quad
\theta(z)\mapsto-i v e^{\pi iz^2/\tau}\theta(z),
$$
while the three even theta functions acquire $v e^{\pi iz^2/\tau}$ and the permutation $2\leftrightarrow4$, $3\leftrightarrow3$. Therefore each even starred theta has factor
$-iv e^{3\pi iz^2/\tau}$ with the same permutation; the odd starred theta has factor $v e^{3\pi iz^2/\tau}$. After multiplication by the theta at $sz$, every term has factor
$$
-iv^2 e^{\pi i(3+s^2)z^2/\tau}=-\tau.
$$
Thus the Gaussian cancels in every term, and
$$
J_o(z/\tau,-1/\tau)=-\tau J_o(z,\tau).
\tag{CM2}
$$
No relative sign in the $-sR_0$ term has changed.

Compare the complete expansion R954(954.10). For $k=6j+2$ the functions $W_k(\tau)$ satisfy
$$
W_k(\tau+1)=\rho W_k(\tau),\qquad
W_k(-1/\tau)=-\tau^k W_k(\tau).
$$
These are precisely the multiplier of $\eta^4$, followed by ordinary weight $6j$. Since $\eta$ has no zero in the upper half-plane,
$$
M_j:=\frac{W_{6j+2}}{\eta^4}
\tag{CM3}
$$
is holomorphic there and transforms as a full-level modular form of weight $6j$. At the cusp, the nonzero frequencies in the conductor-$(2s)$ ideal sum have norm $1\pmod6$. Thus, with $q=Q^6=e^{2\pi i\tau}$,
$W_{6j+2}=Q(1+O(q))$ and $\eta^4=Q(1+O(q))$. The quotient is holomorphic at the full-level cusp and has constant term one. Hence
$$
\boxed{M_j\in M_{6j}(\mathrm{SL}_2(\mathbf Z)),\qquad M_j=1+O(q).}
\tag{CM4}
$$

The Fourier coefficients of $W_{6j+2}$ are integers: the ideal character values are algebraic integers in $\mathbf Q(s)$, and conjugate ideals give conjugate values. Multiplication by the integral inverse of $\prod_{n\ge1}(1-q^n)^4$ then shows $M_j\in\mathbf Z[[q]]$.

The full-level weight-$6j$ space has the basis
$$
E_6^{j-2r}\Delta^r,\qquad 0\le r\le\lfloor j/2\rfloor.
\tag{CM5}
$$
Indeed the usual $E_4,E_6$ presentation allows only powers of $E_4$ divisible by three at this weight, and $E_4^3=E_6^2+1728\Delta$. The displayed basis has respective leading terms $q^r$ with coefficient one. Successively matching the integral $q$ coefficients therefore proves the integral identity
$$
\boxed{
\frac{W_{6j+2}}{\eta^4E_6^j}
=R_j\!\left(\frac{\eta^{24}}{E_6^2}\right),\qquad
R_j(U)\in\mathbf Z[U],\quad
\deg R_j\le\lfloor j/2\rfloor,\quad R_j(0)=1.
}
\tag{CM6}
$$
This is a global description of the whole odd evaluation family, not only its value at $j=0$. It does not change its conductor or identify it with an original Jacobian companion. The already registered base identities $R_0=R_1=1$ are also forced by (CM5); no numerical recomputation of them is needed.

## 2. The even family in the original graph coordinate

R913 retains the same actual tame and deck character for all $V_{6i+4}^\dagger$. R918/R920 give the complete minimum divisor of $V_4^\dagger$. Dividing a weight-$6i+4$ cusp form in this character by $V_4^\dagger$ is therefore regular, and the quotient has trivial deck character and weight $6i$.

R920 gives the degree-three weight-six line on the coarse curve $\mathbf P^1_u$, with
$$
M_6(H_6)=W_6\langle1,u,u^2,u^3\rangle,
\qquad E_6=(8u^3-1)W_6,\qquad
W_6=\pm24s\eta^{12}.
$$
Taking its $i$th tensor power and the actual $\delta:u\mapsto\zeta u$ invariants gives
$$
M_{6i}(H_6)^{\delta=1}
=\left\langle E_6^{i-a}\eta^{12a}:0\le a\le i\right\rangle.
\tag{CM7}
$$
This uses the complete coarse line $O(3i)$, whose invariant polynomials are exactly $1,u^3,\ldots,u^{3i}$. It is not a dimension guess from a few weights.

Set
$$
X=s\frac{\eta^{12}}{E_6}.
$$
The basis $V_4^\dagger E_6^{i-a}(s\eta^{12})^a$ has respective initial terms $s^aQ^{1+3a}$. All these initial coefficients are units away from six. Integral triangular elimination at the cusp therefore gives
$$
\frac{V_{6i+4}^\dagger}{V_4^\dagger E_6^i}=P_i(X),
\qquad P_i\in\mathbf Z[1/6,s][X],\quad
\deg P_i\le i,\quad P_i(0)=1.
\tag{CM8}
$$
The coefficients in fact lie in $\mathbf Z[1/6]$. Here is a direct check retaining the oldform phase. The level-nine CM form $F_k$ has integral coefficients, and ideals of even norm are exactly those divisible by $(2)$. Their character factor is $\epsilon_3(2)2^{k-1}=-2^{k-1}$. Hence
$$
F_k(-Q)=-F_k(Q)-2^kF_k(Q^4),
$$
and the actual oldform satisfies
$$
V_k^\dagger(-Q)=-\overline{V_k^\dagger(Q)}.
\tag{CM9}
$$
Here the bar conjugates $s$ and the coefficient field, leaving the formal variable $Q$ fixed. Also $E_6(-Q)=E_6(Q)$, $\eta^{12}(-Q)=-\eta^{12}(Q)$, and $\overline X=-X$. Applying (CM9) to (CM8) gives
$P_i(-X)=\overline{P_i}(-X)$; the nonconstant formal coordinate $X$ makes this a polynomial identity. Thus
$$
\boxed{P_i(X)\in\mathbf Z[1/6][X].}
\tag{CM10}
$$
All these descriptions commute with reduction at $p\ge41$. The triangular leading coefficients give the integral statement directly; there is no unspecified index of a candidate lattice.

## 3. The exact extra fine zero order

The original marked ratio is $E_6/\eta^{12}=-24s$, so
$$
X_0=-1/24,\qquad U_0=\frac{\eta^{24}}{E_6^2}=-1/1728.
\tag{CM11}
$$
The global discriminant identity gives
$$
\boxed{(1-24X)(1+24X)=\frac{E_4^3}{E_6^2}.}
\tag{CM12}
$$
At the original mark, $1-24X=2$ and $E_6$ are units, whereas $E_4$ is a fine tame uniformizer after choosing a unit Hodge frame. Consequently
$$
\operatorname{ord}_{\rm mark}(X-X_0)=3.
\tag{CM13}
$$
Similarly $U-U_0=E_4^3/(1728E_6^2)$ has order three. The multiplicity is a tame cubic ramification; it is not an order-$p$ phenomenon.

R949/R954 identify $P_i(X_0)$ and $R_j(U_0)$ with the original $f_i,g_j$ up to explicit units when $6i+4<p$ and $6j+1<p$, respectively. These inequalities hold throughout the original critical antidiagonal. In these ranges,
$$
\begin{aligned}
f_i=0\pmod p&\Longleftrightarrow P_i(X_0)=0
\Longrightarrow\operatorname{ord}_{\rm mark}V_{6i+4}^\dagger\ge4,\\
g_j=0\pmod p&\Longleftrightarrow R_j(U_0)=0
\Longrightarrow\operatorname{ord}_{\rm mark}W_{6j+2}\ge3.
\end{aligned}
\tag{CM14}
$$
More exactly the two orders are
$$
1+3\operatorname{mult}_{X_0}(P_i),\qquad
3\operatorname{mult}_{U_0}(R_j),
\tag{CM15}
$$
because $V_4^\dagger,\eta^4,E_6$ have the already fixed orders $1,0,0$. In the odd case a zero at $U_0$ gives the factor $U-U_0$, so it is equivalently an $E_4^3$ factor of the full-level form $M_j$. In the $X$ coordinate it gives both factors $1+24X$ and $1-24X$; the two marked branches are kept distinct.

## 4. The complete primitive/Legendre polynomial on the coarse line

Put $\ell=N-1$, $d=p-7$, and use exactly the original visible set
$$
I_p=\{0\le i\le\ell:\gcd(6i+7,p+1)=1,\
P_{6i+6}(1/s)\ne0\}.
$$
The letter $P_n$ with an integer subscript and displayed Legendre argument continues to mean the Legendre polynomial; $P_i(X)$ in (CM8) is the separately defined CM polynomial.

Equations (957.10), (957.23) and (CM6)–(CM8) give a complete two-variable polynomial
$$
\boxed{
\begin{aligned}
\mathscr B_p(C,X)
&:=\frac{\mathcal T_p(C;Q)}{V_4^\dagger\eta^4E_6^\ell}\\
&=36\sum_{i=0}^{\ell}\binom d{6i+3}
  \mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s)\,
  P_i(X)R_{\ell-i}(-X^2/3) C^{6i+3}.
\end{aligned}}
\tag{CM16}
$$
It belongs to $\mathbf F_p[C,X]$, has $X$ degree at most $\ell$, and uses the unchanged positive embedding, oldform phase, and primitive mask. The weight of numerator and denominator is $p-5$. The expression is a rational modular identity on $E_6\ne0$, with its polynomial continuation in $X$ displayed on the right.

The failure of every actual same-label product is now exactly
$$
\boxed{
\forall i\in I_p:\ f_i g_{\ell-i}=0
\quad\Longleftrightarrow\quad
1+24X\text{ divides }\mathscr B_p(C,X)\text{ in }\mathbf F_p[C,X].
}
\tag{CM17}
$$
No cancellation between different $i$ occurs in this equivalence, because their powers of $C$ are distinct and their remaining scalar factors are units. It is stronger than saying that the specialization $C=1$ vanishes. By (CM13)–(CM15), failure gives at least four fine zeros for every visible product $V_{6i+4}^\dagger W_{6(\ell-i)+2}$, while its forced base zero has order one.

There is an exact global nonzero source before taking the marked value. Since the two normalized CM forms have first $Q$ coefficient one,
$$
\boxed{
[Q^2]\mathcal T_p(C;Q)=\mathscr B_p(C,0)
=36\sum_{i=0}^{\ell}\binom d{6i+3}
 \mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s)C^{6i+3}.
}
\tag{CM18}
$$
Every displayed binomial coefficient is a unit, since $d<p$. R734 supplies a nonendpoint original primitive label with unit Legendre factor at every allowed prime. Thus (CM18) is a nonzero polynomial for every such prime. The complete primitive/Legendre source is not globally annihilated by the filters.

Nevertheless (CM18) does not contradict (CM17): the factor $1+24X$ takes value one at the cusp $X=0$. Its extra fine order three costs only one degree on the coarse $X$ line. For $\ell\ge1$, the degree bound $\deg_X\mathscr B_p\le\ell$ and the nonzero constant-in-$X$ value permit that factor. Thus plain valence and the nonzero first cusp polynomial do not close the marked gap.

To obtain a nonzero original coefficient one must still rule out the specific common factor in (CM17), for these actual CM polynomials and the actual visible set. An arbitrary nonzero summand of the fixed-pole kernel, the nonzero polynomial (CM18), or a hypothetical spanning assertion for the products would not supply that rule. No such spanning or differential-equation exclusion is asserted here.

## 5. Two different mechanisms at the already proved central zeros

Reuse the exact values of R945, without recalculating the sigma arrays, Legendre values, or supersingular trace.

At $p=227$, the original central label is $h=115$ and $i=j=18$. R945 proves $f_{18}=0$ and $g_{18}=136\ne0$. The two actual modular weights are $112$ and $110$. Thus (CM14)–(CM15) give
$$
\operatorname{ord}_{\rm mark}V_{112}^\dagger\ge4,\qquad
\operatorname{ord}_{\rm mark}W_{110}=0.
\tag{CM19}
$$
At $p=857$, the original central label is $h=433$, with $i=71$ and $j=70$. R945 proves $f_{71}=176\ne0$ and $g_{70}=0$. The two actual weights are $430$ and $422$, so
$$
\operatorname{ord}_{\rm mark}V_{430}^\dagger=1,\qquad
\operatorname{ord}_{\rm mark}W_{422}\ge3.
\tag{CM20}
$$
These exhibit different actual CM factors supplying the extra zero. In both cases the product has order at least four, while the original Legendre factor is a unit. No claim that either unspecified multiplicity is exactly its minimum is made. R945's verified alternative same-label products are unaffected; these are not counterexamples to existence of some other allowed label, or to a sufficiently-large-prime assertion.

## 6. Why the general source constraints do not exclude the common factor

There is also an explicit modular example showing the limit of just the weight, character, cusp, and marked-order conditions. Choose any $i\in I_p$, and put
$$
\mathcal E_i(C;Q)
=V_4^\dagger\eta^4E_6^{\ell-1}
       (E_6+24s\eta^{12})C^{6i+3}.
\tag{CM21}
$$
Here $\ell\ge1$ in the actual range. This is a nonzero integral modular polynomial of weight $p-5$, with the same graph and deck character as the products in (CM16). Its first cusp term is $Q^2C^{6i+3}$ with coefficient one, and its support lies at an actual primitive, Legendre-visible label. At the specified mark it has order exactly four, because
$$
\frac{\mathcal E_i}{V_4^\dagger\eta^4E_6^\ell}
=(1+24X)C^{6i+3}.
\tag{CM22}
$$
It can equally be obtained by applying the original filters to $P_{6i+6}(1/s)^{-1}\mathcal E_i$, since that Legendre factor is a unit and the label is primitive.

This is a concrete example inside the same full modular space and at the same marking. It is not asserted to equal the actual CM source (CM16), or to belong to the span of its actual visible CM products. Its purpose is precise: the general conditions already listed do not prevent the common factor. A further theorem must use the coupled, specified CM polynomials $P_i$ and $R_{\ell-i}$ themselves, rather than substitute an arbitrary modular section or an unproved spanning statement.

The exact criterion (CM17) remains unresolved for the complete original source. The main Serre-uniformity goal remains open.

## Dependencies and provenance

- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md) and [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md)/[R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md): the unchanged even family, full graph character, coarse line, and marked simple zero.
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md)/[R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md): the original sigma normalizations, complete Jacobi formulas, and the below-$p$ unit comparisons.
- [R734](R734-primitive-unit-toric-norm-at-every-prime.md): existence of a nonendpoint primitive original unit Legendre norm.
- [R945](R945-original-central-sigma-zeros-and-same-label-alternatives.md): the two fully verified central sigma zeros and their nonzero partners; only those existing values are reused in §5.
- [R957](R957-original-Legendre-filter-as-a-fixed-pole-CM-convolution.md): the precise common-lattice product and the complete primitive/Legendre source.

The new full-level quotient (CM4)–(CM6), the all-degree coarse descriptions, and the exact common-factor/multiplicity interface are proved above. No external theorem on Bernoulli–Hurwitz numbers or elliptic units has been used.
