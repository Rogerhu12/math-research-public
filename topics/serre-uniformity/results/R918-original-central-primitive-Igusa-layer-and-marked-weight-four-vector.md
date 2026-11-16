# R918 — The original central primitive Igusa layer is the marked weight-four CM vector

Date: 2026-11-16. Status: **proved for all original allowed primes with $p\equiv11\pmod{12}$**. The exact good-model layer supplied by R916 is identified with the original marked weight-four CM vector, with a nonzero scalar. Its order at the marked fine Igusa supersingular point is also determined. The original Tate index and the subsequent transport to a normal coefficient on the contracted component remain present.

## 1. The original label and statement

Retain the objects, scales, and positive CM convention of R908–R916:
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad p\equiv11\pmod{12},
\qquad n=p+1,\quad e=p^2-1,\quad\varpi^e=p.
\tag{918.1}
$$
Set
$$
h=\frac{p+3}{2},\qquad r=2h-n=2.
\tag{918.2}
$$
Then $h\equiv1\pmod6$ and $h$ is odd. A common divisor of $h$ and $n$ divides $2h-n=2$, so
$$
(h,n)=1.
\tag{918.3}
$$
Also $n/2<h\le p-4$, with the upper bound following from $p\ge11$. Thus this is an actual upper-half primitive label in the original set $\mathcal H$, without an additional prime restriction or a choice among several labels.

For the original Raynaud abelian part $B$ and original positive target factor, write exactly as in R916
$$
e_hq_B=[p^{a_h}]\circ f_h,\qquad a_h\ge0.
\tag{918.4}
$$
Let $\omega_h$ be the same unit positive-CM generator. R916 gives
$$
L_h=\varpi^{-2p}f_h^*\omega_h\in\omega_B,\qquad
\overline L_h\ne0,
\tag{918.5}
$$
and puts its reduction on the actual Igusa abelian part. R913 assigns to this vector the weight
$$
k_+=2h-p+1=4,
\qquad
k_-=2p+2-2h=p-1
\tag{918.6}
$$
to the distinct Cartier-cokernel functional.

Let
$$
F_4(\tau)=\eta(3\tau)^8,
\qquad
V_4^\dagger(Q)=F_4(Q)-16\zeta^2F_4(Q^4)
\tag{918.7}
$$
with the series notation and the transported full-six marking of R869 and R913. In particular the phase is $\zeta^2$ at that marking. Let
$$
\Phi_4(F)=\frac16\operatorname{KS}(F/\mathfrak a^2)
\tag{918.8}
$$
be their actual Igusa differential map, followed by the original exotic/Frobenius and determinant correction; $\mathfrak a$ is the canonical Igusa Hasse root.

There is a scalar $c_h\in k^\times$ such that, on the original marked Igusa part,
$$
\boxed{\quad
\overline L_h=c_h\,\Phi_4(\overline V_4^\dagger).
\quad}
\tag{918.9}
$$
The assertion specifies the actual vector up to a nonzero scalar, not merely its prime-to-$6p$ Hecke eigensystem. The scalar is not normalized to one and is not computed here.

## 2. The whole original tame group

Use the original graph subgroup
$$
H_6=\{(\vartheta(g),g):g\in\operatorname{GL}_2(\mathbf F_3)\},
\qquad
\ker\vartheta=Q_8,
\tag{918.10}
$$
inside $\operatorname{GL}_2(\mathbf F_2)\times
\operatorname{GL}_2(\mathbf F_3)$. This is the subgroup of R376(376.12) and R575(575.3), not a subgroup selected only by the desired Hecke eigenvalues.

Its geometric modular curve is
$$
X'(6)=\mathbf P^1_u,\qquad
j=27648u^3(1-4u^3).
\tag{918.11}
$$
The effective index in $\operatorname{PSL}_2(\mathbf Z)$ is six. There is one cusp, of width six, at $u=\infty$. Over $j=0$ the point $u=0$ has ramification index three; the three roots of $1-4u^3$ have index one and are the three elliptic points of order three of this modular curve. Moreover
$$
j-1728=-1728(8u^3-1)^2.
\tag{918.12}
$$
Thus all three points above $j=1728$ have index two, and there are no elliptic points of order two on $X'(6)$. These statements hold in characteristic zero and over every residue field of characteristic greater than three: the indicated roots remain distinct and the relevant orders are tame.

The actual positive cubic form of this curve is obtained by
$a=\sqrt[3]4\,u$. At the primes in (918.1), the cube map on $\mathbf F_p$ is bijective and Hensel lifting gives the fixed $\sqrt[3]4\in\mathbf Z_p^\times$. Hence this original descent does not introduce an additional ramified inertia character. We continue to use the original transported marking; this observation is not a replacement of the positive cubic descent by a different CM twist.

## 3. The integral weight-four cusp module has rank one

Let $\mathcal O$ be a finite unramified $p$-adic coefficient ring containing the actual tame constants, and work first on one fixed pairing component of the full-six curve. The full $\operatorname{GL}_2$ transports reconstruct the other components. Since all groups in (918.10) have order divisible only by two and three, taking their invariants commutes with reduction modulo $p$.

For completeness, there is no failure of integral base change hidden in this assertion. The compact full-six curve is smooth of genus one over $\mathcal O$, has twelve cusps, and its Hodge line $\omega$ has degree six. One can also obtain these numbers directly: $\Gamma(6)$ has effective index $72$, has no elliptic stabilizers, and has twelve width-six cusps; the genus formula gives one, and Kodaira–Spencer gives
$\omega^2\simeq\Omega^1(\text{cusps})$, hence $\deg\omega=6$. The line bundle of weight-four cusp forms has degree
$$
\deg\bigl(\omega^4(-\text{cusps})\bigr)=24-12=12.
\tag{918.13}
$$
Its $H^1$ is zero on both the characteristic-zero and special fibers, by Serre duality on the genus-one curve. Cohomology and base change therefore make its global sections a finite free $\mathcal O$-module whose formation commutes with reduction. The $H_6$ invariant module is a direct summand, using the actual averaging idempotent with unit denominator. Thus its rank equals its characteristic-zero dimension, and its reduction is the full Katz cusp space for the same tame moduli problem.

That dimension is one. Here is the divisor calculation, including the elliptic constraints. The weight-four valence degree on the index-six curve is
$$
4\cdot6/12=2.
\tag{918.14}
$$
A cusp form has order at least one at the unique cusp. At each of the three order-three elliptic points, a weight-four section has local order congruent to one modulo three on the fine uniformizing cover. This follows from the stabilizer action on the Hodge line and its weight-four power; equivalently it is the usual local modular transformation law with $4\equiv1\pmod3$. Each point therefore contributes at least $1/3$ to the valence divisor. The lower bounds already sum to
$$
1+3\cdot\frac13=2.
\tag{918.15}
$$
A nonzero cusp form has exactly those zeros and no additional zero. The ratio of any two such forms has no pole on $\mathbf P^1_u$, so it is constant.

Existence and its actual marking are supplied by (918.7). Its membership in this whole $H_6$ invariant space follows from the uniform tame matrices in R913(913.32–33), not only from a dimension assertion. In the basis $(H_0,16H_2)$ these matrices are
$$
H_0|S=16H_2,\qquad
(16H_2)|S=H_0,
$$
$$
H_0|T=-\zeta^2(H_0+16H_2),\qquad
(16H_2)|T=\zeta^2(16H_2).
\tag{918.16}
$$
They give exactly the original graph-invariant line with vector $H_0-\zeta^2(16H_2)$. The $Q_8$ kernel and the mod-two standard factor are the original ones.

The form $V_4^\dagger$ is integral at every full-six cusp. This follows either from its fixed theta expression in R869(869.29), or from the integral transforms (918.16) and the original full-level cusp transports. Its coefficient of $Q$ at the selected width-six cusp is one. It is therefore primitive in the rank-one invariant module. We obtain
$$
S_4(H_6,\mathcal O)=\mathcal O\,V_4^\dagger,
\qquad
S_4(H_6,k)=k\,\overline V_4^\dagger.
\tag{918.17}
$$
All pairing-component transports and the actual unit cubic descent preserve this statement. There is no unspecified residual Hecke multiplicity left in this particular weight.

## 4. The full norm character and the single Igusa part

The original cotangent layer in (918.5) has full inertia character
$$
\chi_+(u)=\operatorname N(u)^{1-h}.
\tag{918.18}
$$
It also has the original $\delta=\zeta$ character. The weight computation cannot be made only on scalar $u$: doing so would leave a quadratic extension ambiguity.

Here $p\equiv3\pmod4$. The actual normalizer quotient therefore has one Igusa part of type $\operatorname{Ig}(p)/\{\pm1\}$, with the tame quotient still included, as in R910 and R913 §3. For scalar $u=a\in\mathbf F_p^\times$ the original index-restoring element sends the étale generator $P$ to $aP$, whereas $\operatorname N(u)=a^2$. Since $h=(p+3)/2$,
$$
a^{2(1-h)}=a^{-(p+1)}=a^{-2}.
\tag{918.19}
$$
This is exactly the $P$-scaling character of $\Phi_4$.

For a nonsquare norm write $\operatorname N(u)=-a^2$; such a representation exists since $-1$ is a nonsquare. The original $w_1$ correction changes $P$ only by $-1$, already identified in this quotient. Further, $1-h=-n/2$ is even. Hence
$$
(-a^2)^{1-h}=a^{2(1-h)}=a^{-2}.
\tag{918.20}
$$
This proves compatibility with the full inertia character (918.18), not just its scalar restriction. The other possible norm extension would insert a minus sign on these nonsquare norms and is not the original action.

The Igusa correspondence is applied on the full-six fine cover and then to invariants of the actual tame group. Its order is prime to $p$, so this does not alter the isomorphism. The relative Frobenius changes the six-level pairing by $p\equiv-1\pmod6$; the determinant-$-1$ correction fixed in R575 and R913 is retained. It conjugates the mod-three deck generator. Consequently the vector with phase $\zeta^2$ in (918.7) is transported to the original $\delta=\zeta$ space. The phase and the CM marking are transported together.

Here the Igusa map is surjective onto the entire holomorphic differential character space, not only injective on the proposed form. Apply Cais Proposition 3.1 on the fine full-six cover with $k=k_0=4$. Its exceptional supersingular-pole term is absent, because $4<p+1$. It identifies $M_4$ with the character-$d^2$ part of $\Omega^1(\text{cusps})$ for $\beta\mapsto d\beta$. The inverse relation $\beta\mapsto a^{-1}\beta$ for $P\mapsto aP$ changes this to $a^{-2}$, exactly (918.19). Restricting to cusp forms gives all holomorphic differentials, not differentials with allowed cusp poles.

One can check the surjectivity and the absence of an extra higher-weight space directly. Start with any holomorphic differential in this character. Divide by the pulled-back Kodaira–Spencer map and multiply by $\mathfrak a^2$. The character makes the resulting weight-four section descend to the tame base. At a fine supersingular point the pulled-back Kodaira–Spencer map has order $p-2$ and $\mathfrak a^2$ has order two; thus this descended meromorphic section $F$ satisfies
$$
(p-1)\operatorname{ord}_{P_{\rm tame}}F\ge4-p>-(p-1).
\tag{918.20a}
$$
The left side is a multiple of $p-1$, so its base order is nonnegative. At a cusp, holomorphicity of the differential forces the coefficient of $dQ/Q$ to vanish, so $F$ is cuspidal. This gives the inverse of $\Phi_4$. In particular forms presented in higher weights do not create an additional holomorphic character space; their descent by the Hasse root must give this same regular weight-four section.

Taking invariants under the actual tame group preserves this isomorphism. For a tame quotient of smooth curves, an invariant regular differential descends regularly: in a parameter $w$ with quotient parameter $w^d$, invariance forces its first possible exponent to be at least $d-1$. The full-norm extension in (918.19–20), the single Igusa part, and the fixed determinant correction then give
$$
\Phi_4:S_4(H_6,k)\ \xrightarrow{\;\sim\;}\
(\omega_{B_{\mathrm I}})_{\chi_+,\,\delta=\zeta}.
\tag{918.20b}
$$
The source is the whole space in (918.17); its single line already has the displayed transported $\delta$ character.

Thus the entire space containing the actual (918.5) is one-dimensional with the specified generator. R916 gives its nonzero reduction. This proves (918.9) with $c_h\ne0$, without using residual Hecke semisimplicity or an eigenform congruence argument.

## 5. Actual cusp coefficient and marked fine Igusa order

At the selected Igusa cusp the canonical Hasse root has expansion one, and $q=Q^6$. The factor $1/6$ in (918.8) gives
$$
\Phi_4(\overline V_4^\dagger)
=\overline V_4^\dagger(Q)\,\frac{dQ}{Q}
=(1+O(Q))\,dQ.
\tag{918.21}
$$
Therefore the actual leading coefficient of $\overline L_h$ there is $c_h\ne0$. This is an actual good-component cusp coefficient of the original normalized map.

There is also an exact order at the specified full-six supersingular marking. R869(869.29–30), with
$A_2=\vartheta_2^4$, $B=\vartheta_4^4$, gives
$$
V_4^\dagger=\eta^4(B-\zeta^2A_2),
\qquad
\frac{V_4^\dagger}{E_4}
=-\frac{\zeta^2\eta^4}{A_2-\zeta^2B}.
\tag{918.22}
$$
At the transported marking $A_2=\zeta B$, the second expression is a unit. The tame full-six uniformizer at this $j=0$ point can be taken proportional to $E_4$ after a unit Hodge trivialization. Thus $V_4^\dagger$ has order exactly one there, in every characteristic under consideration.

Pass to the fine Igusa cover before the tame and $\{\pm1\}$ quotients. The canonical section $\mathfrak a$ has a simple zero there, and the tame base uniformizer has order $p-1$. Kodaira–Spencer, after pullback to this cover, contributes the derivative order $p-2$. Consequently
$$
\operatorname{ord}_{P_{\rm ss}}
\Phi_4(\overline V_4^\dagger)
=(p-1)-2+(p-2)=2p-5.
\tag{918.23}
$$
Every unit used here is the transported unit in (918.22); $p-1$ is nonzero in the residue field. Equation (918.9) proves the same exact order for the pullback of the actual layer $\overline L_h$. Statement (918.23) is explicitly on the fine Igusa cover. It does not identify its parameter with the original coarse normal parameter at $c_1$.

## 6. What this identification does not remove

The original full differential still has content
$$
\operatorname{content}_R((e_hq_B)^*\omega_h)
=\varpi^{e a_h+2p}R.
\tag{918.24}
$$
Neither $a_h$ nor the unit $c_h$ is assigned a new value. No change to the original quotient, target generator, or $c_0$ rigidification is made.

The other companion has weight $p-1$ and belongs to the distinct Cartier-cokernel functional of R913. The one-dimensional statement (918.17) concerns weight four; it does not prove that this other functional detects its named companion.

Finally, in the original critical notation,
$$
i=j=\frac{p-11}{12},\qquad
h=6i+7,\qquad
p=6N+5,\qquad i+j=N-1.
\tag{918.25}
$$
The actual same-label expression is still
$$
P_{h-1}(1/s)\,f_i g_i.
\tag{918.26}
$$
The geometric identification (918.9) is not an identification of (918.26) with its nonzero scalar. In particular the central Legendre value cannot be replaced by the Hasse unit at the original $j=0$ curve: the marked Legendre comparison recorded earlier has $\lambda(1-\lambda)=1/3$ and $j=2048/3$. The original two-flag/source transport, its ramified scales and any holomorphic ambiguity at the contracted component must still be controlled. A global good-model vector, even the exact named one, is not by itself a specified normal jet.

## Sources

- [R916](R916-original-finite-flat-quotient-and-exact-Hodge-content.md), (916.4–5), (916.28–29): exact content and nonzero actual upper-half layer.
- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md), §§3–7: the two different weights, full norm extensions, original phase, and actual Igusa map.
- [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), (869.27–30): the fixed weight-four vector and its marked unit ratio.
- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md), §2, and [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), (575.3), (575.14): the actual graph group, unit positive cubic descent, and determinant correction.
- Brau–Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, [author PDF](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf), (8–10) and Theorem 1.4: the graph subgroup and explicit tame modular curve.
- Cais, *On the $U_p$ operator in characteristic $p*, [author paper](https://arxiv.org/pdf/1305.4188), Proposition 3.1, its equation (3.2), and the invariant-group discussion following the proof: the fine Igusa differential map, local orders, and descent to the tame moduli problem. The integral rank-one and full-character arguments above are proved directly.

No new numerical computation is used.

