# R892 — Full first-$p^2$ theta distributions and the original divided split contraction

Date: 2026-11-16. Status: proved finite distribution recursion and an exact integrality/unit-vector criterion for the original $\mathcal C_h(S)/p$ on the stated unramified source class. The required vanishing of the lower bands and the required original scalar nonvanishing are not asserted.

## 1. Fixed original objects and the two different precision parameters

Keep R889's original curve, differential, theta action, and parameter:
$$
E_0:y^2=x^3-1,\quad \omega=dx/(2y),\quad
p\ge41,\quad p\equiv5\pmod6,\quad k=\mathbf F_{p^2},
$$
$$
D=\frac d\omega,\qquad
q=-B^{-1}D^{p-2}x,\qquad
Q=q-\frac{d_p}{6B},\qquad
\kappa=-6B.
\tag{892.1}
$$
Here $B\in\mathbf F_p^\times$ has exactly the sign fixed in R574/R889. On
$\mathcal H=H^0(E_0,O(6pO))$,
$$
[D,Q]=1,\quad D^p=Q^p=0,\quad
\Theta_0=1,\quad
\Theta_j=D^j/j!\ (0<j<p),\quad
\Theta_p=\kappa Q,
$$
$$
\Theta_j=[Y^j]\rho(\tau(P_Y)).
\tag{892.2}
$$
The operators are the actual symmetric theta distributions, with rational-frame translation $P\mapsto P+P_Y$. No commuting replacement of $d_p$ and $q$ is made.

Write
$$
q_{\!p}=p^2,\qquad e=q_{\!p}-1.
\tag{892.3}
$$
The symbol $q_{\!p}$ is a number and is distinct from the rational function $q$ in (892.1).

For the integral part let $R=W(k)$, with the finite unramified extension required for the original tame marking if necessary. Use the same smooth equation and its fixed integral rational section basis. Let
$$
\varpi=Y(P_1)
$$
be the original nonzero $p$-torsion coordinate, not a newly rescaled uniformizer. R589's complete CM multiplication law gives
$$
Y(P_a)=[a]\varpi\quad(a\in k),\qquad
v_p(\varpi)=1/e,
$$
$$
\boxed{\varpi^e/p=U,\qquad U\equiv1\pmod p.}
\tag{892.4}
$$
The sign in (892.4) follows from the actual reduction $[p](Y)=-Y^{p^2}$: writing
$[p](Y)=Y(p+a_1Y^e+a_2Y^{2e}+\cdots)$, one has
$a_1\equiv-1$ and $a_j\equiv0$ for $j\ge2$, so the torsion equation gives $U\equiv1$. It is not set equal to one by a choice of scale.

Work over the corresponding ramified DVR $R'=R[\varpi]$, enlarging the unramified constants as just stated. All original $p$-torsion points and their Weil pairings are defined there. Its valuation normalized by $\operatorname{ord}_\varpi(\varpi)=1$ satisfies $\operatorname{ord}_\varpi(p)=e$.

The special-fiber distribution recursion below uses total formal degree strictly less than $q_{\!p}$. Its integral application uses precision modulo $\varpi^{e+1}=\varpi^{p^2}$. These bounds agree, but a coefficient in the unramified integral ring can still contribute a multiple of $p$ at degree zero. Such constant terms are treated explicitly in §5.

## 2. The genuine truncated group law and Weil pairing

Let $\mathcal F(S,Y)$ be the formal group law in the original integral CM parameter. The Teichmueller group of order $e$ acts by multiplication on this parameter. Therefore every non-linear monomial of $\mathcal F$ has total degree congruent to one modulo $e$. In particular
$$
\mathcal F(S,Y)\equiv S+Y
 \pmod{(S,Y)^{q_{\!p}}}.
\tag{892.5}
$$
This is a statement of total degree, not a global splitting of $E_0[p]$.

Let $E(S,Y)$ denote the commutator pairing of the actual $p$-primary theta group for $O(6pO)$. The canonical symmetric section satisfies
$$
\tau(P_S)\tau(P_Y)
=E(S,Y)^{1/2}\tau(P_{\mathcal F(S,Y)}).
\tag{892.6}
$$
The inverse of two on $\mu_p$ is meant; no new square-root branch is introduced.

Because the pairing is trivial on $\ker F\times\ker F$, and is one when either input is zero, every term of $E-1$ has total degree at least $p+1$. Consequently the truncated logarithm and exponential are inverse in total degrees less than $q_{\!p}$: all denominators that can occur are among $1,\ldots,p-1$, and a product of $p$ terms of positive minimum degree has degree at least $p(p+1)>q_{\!p}$.

The logarithm is biadditive for (892.5). A biadditive polynomial of positive degree in each variable and total degree less than $p^2$ has exponents $1$ or $p$ in each variable. The coefficient of $SY$ vanishes by the same isotropy, and alternation kills the coefficient of $S^pY^p$ since $p$ is odd. The two remaining coefficients are negatives of each other. R889's actual commutator
$[D,\Theta_p]=\kappa\,1$ fixes the coefficient of $SY^p$. Therefore
$$
\boxed{
\log E(S,Y)\equiv
 \kappa(SY^p-S^pY)\pmod{(S,Y)^{q_{\!p}}}.
}
\tag{892.7}
$$
In particular
$$
E(S,Y)^{1/2}\equiv
 \sum_{a,b\ge0}
 \frac{(\kappa/2)^{a+b}(-1)^b}{a!\,b!}
 S^{a+pb}Y^{pa+b}
 \pmod{(S,Y)^{q_{\!p}}},
\tag{892.8}
$$
where only terms of total degree less than $q_{\!p}$ are retained. They have $a+b<p$, so every denominator displayed is a unit.

This scalar exponential is legitimate because its minimum positive degree is $p+1$. It is not the invalid assertion that the operator-valued theta action is an ordinary exponential in $D$ and $Q$.

## 3. The full noncommutative recursion

Comparing the coefficient of $S^mY^n$ in (892.6), where $m+n=L<q_{\!p}$, gives
$$
\boxed{
\Theta_m\Theta_n=
 \sum_{\substack{a,b\ge0\\
                 a+pb\le m\\
                 pa+b\le n}}
 \frac{(\kappa/2)^{a+b}(-1)^b}{a!\,b!}
 \binom{L-(p+1)(a+b)}{m-a-pb}
 \Theta_{L-(p+1)(a+b)}.
}
\tag{892.9}
$$
All binomial coefficients are reduced in $k$. The term $a=b=0$ is
$\binom Lm\Theta_L$; every other term has a strictly smaller distribution index. Operator multiplication on the left retains its displayed order.

This determines every $\Theta_L$ for $L<p^2$ from $D,\Theta_p$:

- If $L<p$, use (892.2).
- If $L=ip+j$, $1\le i<p$ and $1\le j<p$, use $m=j,n=ip$. Lucas's binomial formula gives $\binom{ip+j}{j}=1$ modulo $p$.
- If $L=ip$, $2\le i<p$, use $m=p,n=(i-1)p$. Then $\binom{ip}{p}=i$, also a unit.

Both distributions on the left and every correction on the right have already been determined. Thus (892.9), with the specified choices, is a finite ascending recursion involving no division by $p$ and no missing high distribution. It produces actual operators on the original $\mathcal H$.

For example, direct coefficient comparison gives
$$
\Theta_{p+1}=\Theta_1\Theta_p-\kappa/2
            =\kappa DQ-\kappa/2,
$$
$$
\Theta_{2p}=\Theta_p^2/2,
$$
$$
\boxed{
\Theta_{3p}=\Theta_p^3/6
 -\frac{\kappa^2}{24(p-2)!}D^{p-2}.
}
\tag{892.10}
$$
For the second identity the two terms linear in $\kappa$ cancel. For the third, those linear terms again cancel and the remaining correction is the $a=2,b=0$ term
$\kappa^2\Theta_{p-2}/8$ before division by three. All three indices are below $p^2$ in the stated range.

These examples also locate the failure of a tempting operator exponential. If
$\exp(YD)\exp(\kappa Y^pQ)\exp(-\kappa Y^{p+1}/2)$ is formed using truncated exponentials, its coefficient at $Y^{2p}$ contains the additional term
$\kappa D^{p-1}/2$, because $(p-1)!=-1$. That term is absent in the actual $\Theta_{2p}$ of (892.10). This expression is not used in the recursion or in the contraction below.

Every $\Theta_L$ commutes with the actual six-primary theta group, since it is a distribution of the commuting $p$-primary group. Thus the full tame multiplicity space remains present in (892.9); it has not been replaced by a scalar channel.

## 4. Original two-flag coordinates and the finite operator polynomial

Use exactly R881/R886's marked generic $p$-torsion vector space
$\mathbb E=\mathbf F_{p^2}$, additive character, and pairing scale
$$
b(a,a')=\operatorname{Tr}_{\mathbb E/\mathbf F_p}
 (\gamma a\overline{a'}),\qquad
\overline\gamma=-\gamma,\quad\gamma\ne0.
\tag{892.11}
$$
The value of $\gamma$ is the actual one determined by the Weil pairing and the original additive character. It is not normalized away.

The two symplectic coordinates and their inverse are
$$
u=a+\overline b,\qquad
v=-\frac{\gamma}{2}(a-\overline b),
$$
$$
a=u/2-v/\gamma,\qquad
b=\overline u/2-\overline v/\gamma.
\tag{892.12}
$$
Thus the first and second flags have points
$$
L:\ (-v/\gamma,-\overline v/\gamma),\qquad
L':\ (u/2,\overline u/2).
\tag{892.13}
$$
These are the same finite flat closures and the same symmetric theta lifts as R886. The tensor action is for the positive product line bundle
$O(6pO)\boxtimes O(6pO)$.

Fix the original primitive label
$$
7\le h\le p-4,\quad h\equiv1\pmod6,\quad (h,p+1)=1,
\qquad
\theta_h(u)=[u]^{-h(p-1)}.
\tag{892.14}
$$
Define a formal operator polynomial over $k$, using a new scalar variable $X$:
$$
\mathscr R_c(X)=\sum_{j=0}^{e}c^j\Theta_jX^j
 \pmod{X^{e+1}}\qquad(c\in\mathbb E),
$$
$$
\mathscr R_{c,d}(X)=
 \mathscr R_c(X)\otimes\mathscr R_d(X)
 \pmod{X^{e+1}}.
\tag{892.15}
$$
For $c=0$, take $c^0=1$ and $c^j=0$ for $j>0$. Every distribution in this formula is supplied by §3.

Now put
$$
\mathscr T_L(X)=
 \sum_{v\in\mathbb E}
 \mathscr R_{-v/\gamma,-\overline v/\gamma}(X),
$$
$$
\mathscr G_h(X)=
 \sum_{u\in\mathbb E^\times}
 u^{-h(p-1)}
 \mathscr R_{u/2,\overline u/2}(X),
$$
$$
\boxed{
\mathscr K_h(X)=\mathscr T_L(X)\mathscr G_h(X)
 =\sum_{n=1}^{e}K_{h,n}X^n
 \pmod{X^{e+1}}.
}
\tag{892.16}
$$
The order of the two factors is the actual order in R886's contraction. The character is $\theta_h$, not its inverse. The first sum is an unnormalized trace; no division by $p^2$ is made. The constant term of the second sum is exactly zero by nontrivial character orthogonality; the first has constant term $p^2=0$ in $k$.

Formula (892.16) is a precise finite prescription, rather than a claim that its coefficients vanish. Finite field power sums may be used to simplify it, but none has been omitted. In particular replacing $h$ by $h+(p+1)/2$ multiplies the second sum by the actual norm-quadratic character. The original determinant extension is still distinguished.

## 5. Exact integral precision for the fixed original source

Let
$$
\mathcal B_R=
H^0(E_0,O(6pO))\otimes_R H^0(E_0,O(6pO)).
$$
The source class in this section consists of sections $S\in\mathcal B_R$ defined on the original unramified smooth model and then base changed to $R'$. The principal application is exactly
$$
\boxed{S_{F,G}=(x s_{6p})\otimes(-xy s_{6p}).}
\tag{892.17}
$$
It is not replaced by a Frobenius-source vector or by an arbitrary ramified lift.

The coaction of the integral theta group has integral matrix entries in the finite flat $p$-torsion coordinate algebra. Reducing its coefficients modulo $p$ gives the actual $\Theta_j$ of §3. Evaluation at $P_c$ uses
$Y(P_c)=[c]\varpi$ from (892.4). Terms of degree at least $p^2=e+1$ vanish at the present precision. For every positive degree $n\le e$, changing an integral coefficient by a multiple of $p$ changes its value by an element of
$$
p\varpi^nR'\subseteq\varpi^{e+1}R'.
\tag{892.18}
$$
Thus the special-fiber distributions suffice for every positive-degree term through this precision.

The degree-zero issue is separate and harmless for the present operator. In the actual Gauss sum the constant is
$\sum_{u\ne0}\theta_h(u)=0$ exactly, while the constant of the actual trace is $p^2\,1$, which has valuation $2e\ge e+1$. Consequently there is no unrecorded constant multiple of $p$ at degree zero. This is the reason that replacing the positive-degree coefficients by their reductions is valid even through degree $e$.

Let $\overline S$ be the reduction of the fixed unramified section. The same estimate (892.18) shows that replacing $S$ by another unramified lift with the same reduction changes the output only modulo $\varpi^{e+1}$: the operator has zero degree-zero term and every remaining term has positive degree. It does not justify the corresponding assertion for arbitrary $R'$-lifts differing only by $\varpi$.

It follows that the actual integral operator satisfies
$$
\boxed{
\mathcal T_L\mathcal G_{\theta_h}(S)
\equiv
 \sum_{n=1}^{e}\varpi^n\,\widetilde{K_{h,n}(\overline S)}
 \pmod{\varpi^{e+1}\mathcal B_{R'}}.
}
\tag{892.19}
$$
Each tilde is any lift in the fixed unramified section basis; (892.18) makes the choice immaterial. The formula includes all lower bands and the coefficient at valuation exactly one in the $p$ normalization.

No ordinary reduction of a nonintegral full sigma series is used. The only theta coefficients needed are reductions of an actual integral group action.

## 6. Saturated descent and the genuine divided-value criterion

Let
$$
\pi_L:E_0^2\longrightarrow B_L
$$
be the actual quotient of R886, let $\mathcal M_L$ be its descended type-$(6,6)$ line bundle, and put
$$
\mathcal U_L=H^0(B_L,\mathcal M_L).
$$
The pullback is the actual inclusion
$$
\pi_L^*:\mathcal U_L
 \xrightarrow{\ \sim\ }
 \mathcal B_{R'}^{\tau(L)}.
\tag{892.20}
$$
Its image is saturated over the DVR $R'$. Indeed the invariant module is the kernel of
$$
\mathcal B_{R'}\longrightarrow
\mathcal B_{R'}\otimes_{R'}O(L),\qquad
s\longmapsto\operatorname{coact}(s)-s\otimes1.
\tag{892.21}
$$
The target is free because $L$ is finite flat. Therefore the quotient by this kernel embeds into a torsion-free module and is torsion-free. In particular pullback preserves divisibility by every power of $\varpi$, and preserves the content ideal of a vector.

The original integral contraction is
$$
\mathcal C_h=(\pi_L^*)^{-1}
 \mathcal T_L\mathcal G_{\theta_h}.
\tag{892.22}
$$
Combining (892.19)--(892.22) gives the following exact test on the unramified source class:
$$
\boxed{
\mathcal C_h(S)/p\in\mathcal U_L
\quad\Longleftrightarrow\quad
K_{h,n}(\overline S)=0\text{ for every }1\le n<e.
}
\tag{892.23}
$$
When this holds, the reduction of its pullback is
$$
\boxed{
\overline{\pi_L^*(\mathcal C_h(S)/p)}
=K_{h,e}(\overline S).
}
\tag{892.24}
$$
The scalar is exactly one because division by $p$ multiplies
$\varpi^{-e}$ by $U=\varpi^e/p$, whose original residue is one by (892.4). An unspecified unit or a changed uniformizer has not been substituted.

In particular
$$
\boxed{
\mathcal C_h(S)/p
\text{ is an integral vector of unit content}
}
$$
$$
\boxed{
\Longleftrightarrow\
K_{h,n}(\overline S)=0\ (1\le n<e),\qquad
K_{h,e}(\overline S)\ne0.
}
\tag{892.25}
$$
Here “unit content” means that at least one coordinate in an integral basis of the actual descended module is a unit. Saturation makes this criterion independent of that basis and of the pullback.

If the first nonzero coefficient in (892.19) has index $n<e$, the exact content valuation is $n$ and the divided vector is not integral. If every displayed coefficient is zero, (892.19) gives only the stronger lower bound $\operatorname{ord}_\varpi\mathcal C_h(S)\ge e+1$; further precision would then be needed. These alternatives are not silently discarded.

## 7. Relation to the original sigma and period questions

All operators in (892.23)--(892.25) act on the specified original reduction
$x s_{6p}\otimes(-xy)s_{6p}$ when $S=S_{F,G}$. The result therefore supplies a complete first-$p^2$ finite recipe for the original contraction's lower polar bands and its first divided residue.

It does not prove that those lower bands vanish for this source. It also does not identify a unit vector in $\mathcal U_L$ with a unit value of its required CM jet. R889 gives the separate exact fifth-jet formula on its explicitly constructed Frobenius-source character section; no equality between that section and $S_{F,G}$ or $\Gamma_h(\mathcal U_L)$ has been inserted here.

The original period average still uses R881/R886's separate $\mathsf T_\zeta$, the full determinant extension, and
$$
\mathcal C_h\mathcal A_h\Gamma_h=p^2N_h,\qquad
N_h\bmod p=-P_{h-1}(1/\sqrt{-3})^2.
\tag{892.26}
$$
The finite recipe above does not remove this Legendre factor or infer the original same-$h$ scalar nonvanishing from a nonzero ambient weight space.

The next positive task is to simplify the actual coefficients
$K_{h,n}(x\otimes-xy)$ with the same marking, establish the necessary lower-band cancellation where it is true, and compare the resulting original output with the required scalar jet. This paper does not execute that arithmetic or add a finite prime window.

## Sources

- [R574](R574-completed-zeta-Cartier-input.md): original $B,q,D$ and their signs.
- [R589](R589-specified-type-three-coefficient-and-actual-CM-unit-criterion.md), (589.6)--(589.10): the full CM parameter, actual $[p](Y)$, all torsion labels, and the positive residue $\varpi^e/p\equiv1$.
- [R878](R878-original-finite-theta-action-and-section-projections.md), §§2--4: the actual symmetric theta group law and Cartier splitting.
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md), §§2--5: actual $\Theta_p=\kappa Q$, its noncommutativity, and its original sigma interpretation.
- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md), §§5--7: original symplectic coordinates, $\gamma$, character direction, and determinant extension.
- [R886](R886-original-two-flag-theta-descent-and-split-contraction.md), §§2--7: the actual quotient, descended module, trace, Gauss sum, split contraction, and original period norm.

Every displayed recursion and precision bound is proved symbolically above. No local mathematical computation or new numerical prime scan was used.
