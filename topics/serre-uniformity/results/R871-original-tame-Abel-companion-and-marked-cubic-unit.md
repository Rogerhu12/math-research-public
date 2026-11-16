# R871 — The original tame Abel companion and its marked cubic unit

Date: 2026-11-16. Status: **proved**. For the original untwisted $h=1$ Fourier vector, its residual once-primitive is an explicit weight-$p-1$ tame CM form. Dividing by the Hasse invariant gives a rational function that is regular at the specified conjugate full-six CM marking. Its first nonconstant term there is cubic with an explicit unit coefficient. This is a statement on the tame modular curve. The cyclic-$p$ pullback, the ramified full-level source lattice, and the original $q$-normal coefficient are not identified by this result.

## 1. Original objects and the once-primitive

Let $p\ge41$, $p\equiv5\pmod6$, and retain the coefficient place, $K=\mathbb Q(\sqrt{-3})$, $\zeta=(-1+\sqrt{-3})/2$, and the actual raw untwisted newform of R575 and R869:
$$
 f_\theta=f_{\Psi_\theta},\qquad
 \Psi_\theta((a))=a\epsilon_3(a)\theta_{-1}(a),\qquad
 \theta_{-1}(a)=[a]^{-(p-1)}.
 \tag{871.1}
$$
Here $\epsilon_3$ is the nontrivial sign character modulo $\sqrt{-3}$. The finite conductor of (871.1) is $(p\sqrt{-3})$, and its level is $9p^2$. The positive $\kappa_4$ of the actual quotient is the arithmetic descent fixed in R575; it is not inserted into this raw Fourier vector.

Define a tame CM cusp form
$$
 C_{p-1}=f_{\Xi_C},\qquad
 \Xi_C((a))=a^{p-2}\epsilon_3(a).
 \tag{871.2}
$$
Its weight is $p-1$, its exact finite conductor is $(\sqrt{-3})$, and its level is $9$. The exponent $p-2$ is odd and divisible by three. Thus the formula is independent of the generator of the ideal: the contribution of $-1$ is canceled by $\epsilon_3$, and that of $\zeta$ is one. The sign character is nontrivial at $\sqrt{-3}$, so the conductor has not been silently lowered. These CM theta series have integral Fourier coefficients; conjugating the summation ideals also shows that the coefficients of (871.2) are rational integers.

For the following residual identities a bar means reduction at the fixed inert place. We use both the untwisted weight-four form and the weight-$2p$ companion already fixed in R869:
$$
 f_4=f_{a^3\epsilon_3(a)}=\eta(3\tau)^8,
 \qquad
 G_{2p}=f_{\bar a^{\,2p-1}\epsilon_3(a)}.
 \tag{871.3}
$$
The second form is holomorphic of weight $2p$, using the conjugate CM type; the bar on $a$ does not make it an antiholomorphic form.

In the base Fourier variable $q$, the exact equalities are
$$
 \boxed{
 \Theta_q\overline C_{p-1}=\overline f_\theta
       =\overline G_{2p},\qquad
 \Theta_q\overline f_\theta=\overline f_4,
 \qquad \Theta_q=q\frac d{dq}.}
 \tag{871.4}
$$
To verify the first equality, reindex the ideal sum for $C_{p-1}$ by conjugation. Its coefficients are unchanged, so one may use $\bar a^{p-2}\epsilon_3(a)$ in that sum. For an ideal prime to $p$, $\bar a=a^p$ in $\mathbb F_{p^2}$, and
$$
 \operatorname N(a)\bar a^{p-2}
 =a\bar a^{p-1}
 \equiv a^{p^2-p+1}
 =a^{2-p}.
 \tag{871.5}
$$
This is the reduction of the original character in (871.1). Also
$$
 \bar a^{2p-1}\equiv a^{2-p},\qquad
 \operatorname N(a)a^{2-p}\equiv a^3.
 \tag{871.6}
$$
These prove the remaining comparisons. Ideals divisible by the unique prime $(p)$ contribute multiples of $p^{p-2}$, $p^{2p-1}$, and $p^3$ to $C_{p-1}$, $G_{2p}$, and $f_4$, respectively. Their reductions vanish, just as the corresponding terms are omitted from $f_\theta$. The prime at three is omitted in all the series. Hence (871.4) includes all Fourier coefficients, not only those with exponent prime to $p$.

Set
$$
 Q=\exp(2\pi i\tau'/6),
 \qquad
 \begin{aligned}
 W(\tau')&=\overline C_{p-1}(\tau'/6)
             -\zeta^2\overline C_{p-1}(2\tau'/3),\\
 G(\tau')&=\overline G_{2p}(\tau'/6)
             -4\zeta^2\overline G_{2p}(2\tau'/3),\\
 V(\tau')&=\overline f_4(\tau'/6)
             -16\zeta^2\overline f_4(2\tau'/3).
 \end{aligned}
 \tag{871.7}
$$
All three are cusp forms on the same full tame level-six component, of weights $p-1$, $2p$, and $4$. For example, conjugating a matrix of $\Gamma(6)$ by $\operatorname{diag}(1,6)$ or $\operatorname{diag}(2,3)$ gives an integral matrix in $\Gamma_0(9)$; thus both displayed degeneracy functions have the asserted common level. Their scaling denominators are prime to $p$.

The original raw vector is
$F(Q)=f_\theta(Q)-4\zeta^2f_\theta(Q^4)$, so
$$
 \Theta_Q W=\overline F=G\text{ as Fourier series},
 \qquad \Theta_QG=V.
 \tag{871.8}
$$
The oldform coefficient in $W$ is $-\zeta^2$, because differentiating $C(Q^4)$ contributes four. It is not $-4\zeta^2$. The common modular variable satisfies
$$
 \Theta_{\tau'}=q_{\tau'}\frac d{dq_{\tau'}}
       =\frac16\Theta_Q.
 \tag{871.9}
$$

## 2. Same-weight identities and the two factors of six

Let $X=X(6)$ be the smooth compact full-level curve over the fixed algebraically closed residue field, let $\omega$ be its Hodge line bundle, and let $\mathcal A$ be the level-one Hasse invariant with Tate $q$ expansion one. Write
$$
 \partial_k=\Theta_{\tau'}-\frac{k}{12}E_2,
 \qquad \mathcal B=\partial_{p-1}\mathcal A.
 \tag{871.10}
$$
The notation $E_2$ in this formula means its usual quasimodular Fourier series. The resulting Serre derivative is a modular operator of weight two. The modular form $\mathcal B$ has weight $p+1$ and Fourier expansion $E_2/12$, as in R833(833.4–5).

The modular theta operator is
$$
 \Theta^{\rm K}_k(H)
     =\mathcal A\partial_kH+k\mathcal B H.
 \tag{871.11}
$$
It has weight $k+p+1$, has Fourier expansion $\Theta_{\tau'}H$, and commutes with the actual tame full-level slash action. These assertions follow directly from the Serre derivative transformation law, since $\mathcal A$ and $\mathcal B$ are level-one forms. Thus they hold also on the conjugate marked component, with the conjugated level action.

By (871.4), (871.7), (871.9), and the tame $q$-expansion principle, the same-weight identities are
$$
 \boxed{
 \Theta^{\rm K}_{p-1}W=\frac G6,
 \qquad
 \Theta^{\rm K}_{2p}G=\frac{\mathcal A^3 V}{6},
 \qquad
 (\Theta^{\rm K})^2W=\frac{\mathcal A^3 V}{36}.}
 \tag{871.12}
$$
The middle equality has weight $3p+1$ on each side; in particular $V$ is multiplied by $\mathcal A^3$, not identified directly with a form of different weight.

In characteristic $p$, $p-1=-1$ and $2p=0$. Therefore (871.11–12) become
$$
 \mathcal A\partial_{p-1}W-\mathcal B W=\frac G6,
 \qquad
 \partial_{2p}G=\frac{\mathcal A^2V}{6}.
 \tag{871.13}
$$
Define the rational weight-zero function
$$
 R=\frac W{\mathcal A}\in k(X).
 \tag{871.14}
$$
The Leibniz rule gives the exact equalities on the function field
$$
 \boxed{
 G=6\mathcal A^2\partial_0R,
 \qquad
 \partial_{2p}(\mathcal A^2\partial_0R)
       =\frac{\mathcal A^2V}{36}.}
 \tag{871.15}
$$
No pointwise division by $\mathcal A$ at a supersingular point has been made. Its Fourier expansion one by itself gives no regularity at such a point.

## 3. Injectivity of two theta derivatives at weight $p-1$

We need the following elementary all-cusp statement:
$$
 \boxed{(\Theta^{\rm K})^2:
 S_{p-1}(\Gamma(6);k)\longrightarrow
 S_{3p+1}(\Gamma(6);k)\text{ is injective}.}
 \tag{871.16}
$$
Here the spaces are on a fixed connected full-level component. There are twelve cusps. Indeed, primitive pairs modulo six number
$36(1-1/4)(1-1/9)=24$, and quotienting by the sign gives twelve. The effective index in $\operatorname{PSL}_2(\mathbb Z)$ is $72$, there are no elliptic stabilizers, and the genus formula gives genus one. Equivalently, Kodaira–Spencer gives
$$
 \omega^{\otimes2}\simeq\Omega_X^1(\text{cusps}),
 \qquad \deg\omega=6,
 \qquad \deg\omega^{p-1}=6(p-1).
 \tag{871.17}
$$
These tame properties persist over the residue field for $p>3$.

Suppose $(\Theta^{\rm K})^2H=0$ for a cusp form of weight $p-1$. At one cusp its $Q$ expansion has coefficients $a_m$, and the two derivatives multiply the $m$-th coefficient by $(m/6)^2$. Therefore $\Theta^{\rm K}H$ has zero Fourier expansion, and is zero by the $q$-expansion principle. The same conclusion holds after every full-level cusp transport, since the operator commutes with that transport.

At each of the twelve cusps, $\Theta^{\rm K}H=0$ says that its $Q$ expansion is supported on exponents divisible by $p$. If $H\ne0$, its first nonzero exponent at each cusp is therefore at least $p$: a cusp form has zero constant term, and an identically zero expansion would make the section zero everywhere. Consequently its divisor has degree at least $12p$, contradicting
$12p>6(p-1)$. This proves (871.16). It neither assumes nor constructs a characteristic-zero inverse of theta.

## 4. Actual six-level symmetry and regularity at the marked point

Let $H_6^\dagger$ be the conjugate of the actual tame subgroup and marking used in R390(390.31–34). Conjugation here transports the level marking as well as the coefficient $\zeta$; it does not replace $\zeta$ in a function while keeping the old CM point fixed.

The exact theta-constant expression is
$$
 V=\eta(\tau')^4(B_2-\zeta^2 A_2),\qquad
 A_2=\vartheta_2(\tau')^4,
 \quad B_2=\vartheta_4(\tau')^4,
 \tag{871.18}
$$
and $V$ is invariant under the full $H_6^\dagger$. This is the conjugate of the full-group calculation in R390 §6: the quaternion kernel at three acts trivially on the specified tame standard constituent, and the diagonal three-cycle fixes the displayed vector. It is not an invariance assertion for just one Fourier coefficient or an unspecified eigenline.

The Hasse invariant is level one. For every $g\in H_6^\dagger$, (871.12) and tame equivariance give
$$
 (\Theta^{\rm K})^2(W|_{p-1}g-W)=0.
 \tag{871.19}
$$
The difference is still a weight-$p-1$ cusp form on $X(6)$. By (871.16) it vanishes. We have proved
$$
 W|_{p-1}g=W\quad(g\in H_6^\dagger).
 \tag{871.20}
$$
This obtains the true tame action of the once-primitive without guessing a Fricke sign for a new weight.

Let $P^\dagger$ be the conjugate full-six $j=0$ point fixed in R869(869.29–30). In the displayed theta constants it has
$$
 A_2(P^\dagger)=\zeta B_2(P^\dagger).
 \tag{871.21}
$$
Its order-three geometric stabilizer in $H_6^\dagger$ acts on an invariant elliptic differential by a primitive cube root. Since $p-1\equiv1\pmod3$, an invariant modular form of weight $p-1$ must have value zero there. Equation (871.20) therefore proves
$$
 W(P^\dagger)=0.
 \tag{871.22}
$$
The point is supersingular because $p\equiv2\pmod3$. The Hasse invariant has a simple zero on the fine modular curve, and
$\mathcal B(P^\dagger)\ne0$, as in R833(833.5). Both statements refer to the same Hodge frame, not to the Fourier value $\mathcal A(q)=1$. Hence (871.22) proves
$$
 \boxed{R=W/\mathcal A\text{ is regular at }P^\dagger.}
 \tag{871.23}
$$
This is the step that excludes a possible simple pole of $R$. Such a pole would not have been excluded by the second differential equation in (871.13) alone.

Finally, the exact unit formula of R869 is
$$
 U:=\frac V{E_4}
   =-\frac{\zeta^2\eta^4}{A_2-\zeta^2B_2}
 \quad\text{at and near }P^\dagger.
 \tag{871.24}
$$
Here $E_4=(A_2-\zeta B_2)(A_2-\zeta^2B_2)$. At the point, $\Delta$ is a unit, so $A_2$, $B_2$, $A_2+B_2$, and $\eta^4$ are units. The denominator in (871.24) equals $(\zeta-\zeta^2)B_2$ and is also a unit. Thus $U(P^\dagger)\in k^\times$ and $V$ has exactly a simple zero there.

## 5. Exact cubic coefficient and the possible homogeneous terms

Use the original elliptic frame of R592,
$$
 E_t:y^2=x^3+tx-1,\qquad \omega=\frac{dx}{2y},
 \tag{871.25}
$$
with the conjugate tame level marking at $t=0$. Let
$T=E_4(E_t,\omega)$ be the local scalar of $E_4$. It is a fine parameter: in this algebraic Tate normalization $T=c_4=-48t$. The weight-six series with Tate constant term one is $E_6=-c_6$, so $E_6=-864$ here. The sign can already be checked on the nodal Tate equation, where $c_4=1$ and $c_6=-1$. More generally the formulas below can be used in any local Hodge frame, retaining its actual value of $E_6(P^\dagger)$.

Write the Serre derivative in a local frame as
$$
 \partial_k f=v(T)\frac{df}{dT}+k b(T)f.
 \tag{871.26}
$$
The functions $v$ and $b$ are regular near the point, and the Ramanujan identity
$\partial_4E_4=-E_6/3$ gives
$$
 v_0:=v(0)=-\frac{E_6(P^\dagger)}3\ne0.
 \tag{871.27}
$$
Let $\mathcal A=a_1T+O(T^2)$ and $V=u_0T+O(T^2)$. The established simple-zero and unit statements give
$$
 a_1\ne0,\qquad u_0=U(P^\dagger)\ne0.
 \tag{871.28}
$$
The weight of $G$ is $2p$, so its connection term in (871.26) is zero in characteristic $p$. Equations (871.13) and (871.28) give
$$
 v(T)G'(T)=\frac{a_1^2u_0}{6}T^3+O(T^4).
 \tag{871.29}
$$
On its own this equation would allow a nonzero constant $G(0)$, corresponding through (871.15) to a simple pole of $R$. But (871.23) and the first equation of (871.15) show that $G$ is divisible by $T^2$. Since $1,2,3,4$ are nonzero modulo $p$, (871.29) then gives
$$
 G(T)=\frac{a_1^2u_0}{24v_0}T^4+O(T^5).
 \tag{871.30}
$$
Substitution back into (871.15) yields
$$
 v(T)R'(T)=\frac{u_0}{144v_0}T^2+O(T^3).
 \tag{871.31}
$$
Thus the claimed first nonconstant term is
$$
 \boxed{
 R(T)-R(0)
   =\frac{u_0}{432v_0^2}T^3+O(T^4)
   =\frac{U(P^\dagger)}{48E_6(P^\dagger)^2}T^3+O(T^4).}
 \tag{871.32}
$$
Every factor in the displayed coefficient is a unit for $p\ge41$. In the fixed frame (871.25) it can equally be written with $E_6(P^\dagger)=-864$ and $T=-48t$; neither a complex period nor an unchosen scalar is inserted.

The constant $R(0)$ is retained. The argument does not determine it or declare it zero. Subtracting it is the local rigidification of this rational companion at the marked point, not an identification with the original global $c_0$-rigidified Abel map.

There can also be characteristic-$p$ homogeneous terms. Locally $\partial_0R=0$ permits $p$-th-power series, and the homogeneous equation for $G$ permits a constant or $p$-th-power series because its weight is zero modulo $p$. Regularity excludes the nonzero constant $G(0)$ mode. A nonconstant regular homogeneous $G$ starts at order at least $p$; after division by $\mathcal A^2$ and one integration its contribution to $R$ can start at order $p-1$. These terms, as well as the $p$-th-power kernel of $\partial_0$, do not change (871.30–32). No characteristic-zero uniqueness argument has been used to remove them.

## 6. Relation to the original ramified source and the remaining comparison

At the reference full-$6p$ cusp, R869 has $Q=e^{2\pi i\tau/(6p)}$. Thus the equality with the tame variable in this paper uses $\tau'=\tau/p$. The reduced formal Fourier primitive of the raw vector is exactly $W$, and $R$ has the same Fourier expansion because $\mathcal A$ has Fourier expansion one. This is an equality of those Fourier series, followed by the proved extension and local expansion on the tame curve.

R869 separately identifies the actual maximal all-cusp raw Hodge lattice as
$\mathcal L=R_\pi\Lambda+\pi^{-1}R_\pi\Lambda_S$, with $\pi=1-\zeta_p$. Its first ramified layer is
$$
 \overline{F_{s/\pi}}
      =\frac{\mu_1(\bar s)}6 V
 \qquad(s\in\Lambda_S).
 \tag{871.33}
$$
All original phases and tame factors in that equality are retained. The rational companion proved here is compatible with that source identity, but compatibility is not yet the full source-to-target comparison.

In particular a cyclic-$p$ quotient of the original universal elliptic curve changes the Hodge frame and the full-six marking. Near the supersingular fiber its two isogeny directions and the Frobenius transport cannot be inferred merely from the cusp substitution $\tau'=\tau/p$. Also a raw weight-two Hodge section converted to a differential in $Q$ acquires the original factor $6p$, as in R818 and R869. The displayed factors $6$ and $36$ do not remove that separate factor $p$.

One must still calculate this actual cyclic-$p$ pullback, the higher ramified phase layers when they contribute, the integral Kodaira–Spencer comparison, and the original $q$ map in the R859/R861 Néron parameters. The tame cubic unit (871.32) is not asserted to be the original first-normal unit, a primitive same-$h$ three-factor unit, or a nonzero height. The actual positive cubic descent and the original rigidification remain fixed in that remaining task.

### Sources and scope

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), (575.1–2), and [R588](R588-actual-toric-norm-and-CM-normalization.md), (588R.11): the untwisted raw Fourier family and the separate actual positive cubic descent.
- [R869](R869-original-maximal-cusp-lattice-and-first-theta-layer.md), §§1, 3 and 6: the exact full-$6p$ phase, the companion $G_{2p}$, the oldform constants, and the marked unit $V/E_4$.
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), (390.29–34): the fixed tame weight-four form, the full actual six-level action, and its theta-constant unit. Only this fixed tame calculation is used; no withdrawn rank-zero quotient claim is restored.
- [R833](R833-original-inert-supersingular-weight-six-and-quaternionic-evaluation.md), §2: the Hasse/Serre derivative normalization, including $12\partial_{p-1}\mathcal A=\overline E_{p+1}$ and its nonzero supersingular restriction.
- [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md), §§1, 3–5, and [R818](R818-original-primitive-cusp-coefficients-and-unramified-Hom-existence.md), §1: the actual elliptic differential, raw Hodge normalization, and the separate $6p$ differential scale.

The new coefficient comparisons, the all-cusp injectivity proof, the marked regularity argument, and the cubic calculation are paper proofs. No local mathematical execution or new finite-prime scan was used.
