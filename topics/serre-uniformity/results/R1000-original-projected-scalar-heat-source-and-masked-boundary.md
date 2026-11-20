# R1000 — The actual projected scalar heat source and its masked boundary

Date: 2026-11-20. Author: serre-public-astra-20261120-de0a3e3b / literature_frontier.

**Status: proved source formula and exact disappearance of its own boundary under the original mask; bulk nonvanishing remains open.** This continues R997's actual conductor-$(2s)$ theta vector. The meromorphic derivative and first-variable projection are applied before taking the first-$p$ rectangle. Their full source has a bulk commutator and one explicit boundary from the first nonintegral canonical-zeta coefficient. The latter is killed by the unchanged primitive/Legendre operator, after the correctly transposed fivefold lift, throughout the family and at every connection iterate. The original critical polynomial is therefore controlled by the specific complete bulk source, not by that Hasse boundary alone.

The cross-oscillator curvature and the horizontal lift operators are the old UH results; they are not proved again here. This result does not say that the bulk source is zero or nonzero in the required critical component, does not prove the R992 filtered space invariant, and does not prove a same-label unit. No arithmetic computation is executed.

## 1. The original scalar and the finite rectangle

Use R997's exact scalar

$$
\Theta=\Theta_\epsilon(z,t),\qquad
\lambda^{-1}\mathscr J(\lambda u,\lambda v)=\Theta(v,u),
\tag{1000.1}
$$

with the same original finite character, component exchange, $\lambda$, $d_0$, and canonical sigma normalization. On the auxiliary curve write

$$
Y^2=X^3+16,\qquad DX=2Y,\quad DY=3X^2,
\quad P_0=(0,4).
$$

Thus the varying elliptic curve for the canonical sigma function is

$$
c(z)^2=x(z)^3-\frac{3X}{4}x(z)-\frac Y4,
\qquad x'=2c,\quad \zeta'=-x.
$$

The original scalar heat equation is

$$
\mathcal D\Theta=0,\qquad
\mathcal D=D-\frac16\partial_z\partial_t-\frac{3X}{2}zt.
\tag{1000.2}
$$

Put

$$
L=\partial_z-6\zeta(z),\qquad
\Pi_j=\Pi_j^t,\qquad \Theta_j=\Pi_j\Theta,
\qquad T=\Pi_4L^2\Theta=L^2\Theta_4.
\tag{1000.3}
$$

R997 proves that the complete first-$p$ rectangle

$$
T_{<p}=[T]_{0\le\deg_z,\deg_t<p}
\tag{1000.4}
$$

is $p$-integral. Here and below a rectangle means separate bounds on the two exponents, not a bound on their sum. Its reduction is an element of

$$
M=k(E_{27})[z,t]/(z^p,t^p).
$$

This uses the original unit-difference relation $\deg_t-\deg_z\equiv1\pmod6$ in $\Theta$. In particular $\Theta_4$ has $t$ exponents $4\pmod6$ and $z$ exponents $3\pmod6$, with smallest $z$ exponent three. There are no negative powers in $T$, even though the operator in (1000.3) is meromorphic. At the original CM point,

$$
T_{<p}(P_0)=-72F_{<p}(t)G_{<p}(z).
\tag{1000.5}
$$

All reductions of expressions containing zeta below concern their complete, specified finite coefficients. No unrestricted meromorphic series is reduced modulo $p$.

## 2. The full bulk commutator, with both projection shifts

Define the first-order operator

$$
U=[\mathcal D,L]
=-x(z)\partial_t-6D\zeta(z)+\frac{3X}{2}t.
\tag{1000.6}
$$

This is R997(997.18), with the same signs. Since

$$
\Pi_j\partial_t=\partial_t\Pi_{j+1},\qquad
\Pi_jt=t\Pi_{j-1},
$$

one has the exact operator identity

$$
[\mathcal D,\Pi_4]
=\frac16\partial_z\partial_t(\Pi_5-\Pi_4)
+\frac{3X}{2}zt(\Pi_3-\Pi_4).
\tag{1000.7}
$$

Using $[\mathcal D,L^2]=UL+LU$, the whole characteristic-zero bulk source is therefore

$$
\boxed{
\begin{aligned}
\mathcal C={}&[\mathcal D,L^2\Pi_4]\Theta\\
={}&(UL+LU)\Theta_4\\
&+L^2\left\{
\frac16\partial_z\partial_t(\Theta_5-\Theta_4)
+\frac{3X}{2}zt(\Theta_3-\Theta_4)
\right\}.
\end{aligned}}
\tag{1000.8}
$$

It satisfies $\mathcal DT=\mathcal C$ before truncation, because $\mathcal D\Theta=0$. Neither the $\Pi_5$ nor the $\Pi_3$ term may be omitted. They come respectively from the cross derivative and the quadratic potential, not from a change of finite character.

For another explicit order check,

$$
UL+LU=-2xL\partial_t-2c\partial_t
-12(D\zeta)L-6(D\zeta)'
+3XtL.
\tag{1000.9}
$$

The formula includes differentiation of the coefficients of $U$ by $L$. For example $Lx=xL+2c$; replacing $UL+LU$ by $2UL$ would lose the $-2c\partial_t$ and $-6(D\zeta)'$ terms.

## 3. The only returning coefficient outside the rectangle

Let $A$ be the original Hasse polynomial of UH/OP on the auxiliary curve, and put $B_0=DA$. Thus $A(P_0)=0$ and $B=B_0(P_0)$ is the previously proved unit. In the canonical zeta expansion

$$
\zeta(z)=\frac1z+\sum_{n\ge2}\beta_n z^{2n-1},
\qquad
\beta_n=\lambda^{2n}\frac{B_{2n}E_{2n}}{(2n)!},
\tag{1000.10}
$$

the first relevant nonintegral coefficient is $n=(p-1)/2$. Its residue is fixed exactly:

$$
\boxed{\quad p\beta_{(p-1)/2}\equiv A\pmod p.\quad}
\tag{1000.11}
$$

Indeed $pB_{p-1}\equiv-1$ and $(p-1)!\equiv-1$; these signs cancel. R997's normalization is $A=\lambda^{p-1}A_H$.

Set

$$
J_3(t)=[z^3]\Theta_4(z,t),
$$

and use only its coefficients of degree below $p$ in $t$. The first returning coefficient of $T$ satisfies

$$
\boxed{
p[z^p]T\equiv48A J_3(t)\pmod p.
}
\tag{1000.12}
$$

To prove this, use the complete operator

$$
L^2=\partial_z^2-12\zeta\partial_z+36\zeta^2-6\zeta'.
$$

On $z^3J_3$, the term $\beta_{(p-1)/2}z^{p-2}$ contributes

$$
\bigl(-36+72-6(p-2)\bigr)\beta_{(p-1)/2}J_3
=6(8-p)\beta_{(p-1)/2}J_3
$$

to the coefficient of $z^p$. Equation (1000.11) gives (1000.12). There are no other residues at this coefficient:

- The leading second derivative would use $[z^{p+2}]\Theta_4$, which is zero because $p+2\not\equiv3\pmod6$.
- The possible coefficient with $2n=p+1$ would multiply $[z]\Theta_4$, which is zero.
- A double non-leading zeta term involving $2n=p-1$ would require the other even index to be at most three, although such indices begin at four.
- All remaining input Taylor exponents and weighted Eisenstein indices are in the already proved integral range; their contributions vanish after multiplication by $p$.

These observations also show that the left side of (1000.12), for $t$ degree below $p$, is integral before it is reduced. The $t^p$ coefficient of $T$ is identically zero in characteristic zero, since every $t$ exponent of $T$ is $4\pmod6$ while $p\equiv5\pmod6$.

## 4. The exact finite source and its integrality

Let

$$
\mathcal R_T=\mathcal D T_{<p}
$$

in the finite module $M$. The exact answer is

$$
\boxed{
\mathcal R_T=\mathcal C_{<p}
+8A z^{p-1}\partial_tJ_{3,<p}(t).
}
\tag{1000.13}
$$

In this formula $\mathcal C_{<p}$ means: form the **entire sum** in (1000.8) in characteristic zero, take its whole indicated rectangle, and only then reduce. Individual zeta summands need not be integral and are not separately reduced.

For the sign and the absence of other edges, compare $\mathcal D T_{<p}$ with the rectangle of $\mathcal DT$. The coefficient $z^p$ outside the rectangle returns under $-\partial_z\partial_t/6$ as

$$
-\frac p6 z^{p-1}\partial_t([z^p]T).
$$

It is absent from the differentiated truncated polynomial. Thus the finite source has the positive correction $p z^{p-1}\partial_t([z^p]T)/6$, which becomes the displayed $8A$ term by (1000.12). The outside $t^p$ column and the double corner are zero by the exact $t$ character. Terms of higher degree cannot return with one cross derivative. The potential only raises degrees, and $T$ has no negative powers, so it creates no further returning term. The base derivative $D$ does not alter the Taylor exponents.

The left side of (1000.13) is integral because $T_{<p}$ is integral and the actual auxiliary derivation and cross-heat operator are integral. The correction term is integral by (1000.12). This proves the integrality of the complete $\mathcal C$ rectangle as well. It does not assert integrality of each of its summands.

At $P_0$, $J_3=-6F(t)$, so the correction in (1000.13) is zero at the point. Its first base derivative is $-48Bz^{p-1}F'(t)$; it cannot be discarded merely because $A(P_0)=0$.

## 5. Exact disappearance of this boundary under the original mask

Use precisely R997's transposed lift and transported mask:

$$
\Lambda=\mathcal L_z^3\mathcal L_t^2,
\qquad
\mathcal L_z=A\partial_t+6B_0z,
\quad \mathcal L_t=A\partial_z+6B_0t.
\tag{1000.14}
$$

The old UH identities give $[\mathcal D,\mathcal L_z]=[\mathcal D,\mathcal L_t]=0$. R997's $\mathcal W^{\rm op}$ is the unchanged original mask on each integer-difference chain, with

$$
d=\deg_z-\deg_t,\qquad
h_d=(p+1-d)/2,
$$

and weight $\mathbf1_{\gcd(h_d,p+1)=1}P_{h_d-1}(1/s)$ when $7\le h_d\le p-4$ and $h_d\equiv1\pmod6$, zero otherwise. In particular a necessary condition for a nonzero weight is $d\equiv4\pmod6$. This is the original $h$, not a reflected label silently assigned a new finite character.

Write the own boundary in (1000.13) as

$$
\mathcal E=8A z^{p-1}\partial_tJ_{3,<p}.
$$

Every exponent of $J_3$ is $4\pmod6$. Thus $\mathcal E$ has integer differences

$$
d\equiv(p-1)-(4-1)\equiv1\pmod6.
$$

Every term of $\mathcal L_z$ increases the integer difference by one, and every term of $\mathcal L_t$ decreases it by one. Consequently $\Lambda\mathcal E$ has only differences $2\pmod6$, outside the original mask. We obtain the full-family identity

$$
\boxed{
\mathcal W^{\rm op}\Lambda\mathcal E=0.
}
\tag{1000.15}
$$

This argument is in the finite rectangle: if a term is removed at an edge by $z^p=t^p=0$, it vanishes, and cannot produce a different difference class. It does not require extending the finite mask to the unrestricted Hurwitz series.

The cross heat preserves each integer difference, including at the truncated edges. Hence

$$
\boxed{
\mathcal W^{\rm op}\Lambda\mathcal D^k\mathcal E=0
\quad(k\ge0).
}
\tag{1000.16}
$$

One may see this directly from the same difference classes, or by using the already proved commutation of the lift and the finite mask with $\mathcal D$. This is why this particular Hasse boundary, even with all of its base derivatives, cannot on its own supply the required masked nonzero component. The statement does not kill the bulk term in (1000.13).

## 6. The actual scalar bulk equation for the original critical polynomial

Define

$$
V_\epsilon=\mathcal W^{\rm op}\Lambda T_{<p},
\qquad
S_\epsilon=\mathcal W^{\rm op}\Lambda\mathcal C_{<p}.
$$

Only the complete integral bulk from §4 is used. Equations (1000.13) and (1000.15), and the old horizontal identities, give the exact finite source equation

$$
\boxed{\mathcal D V_\epsilon=S_\epsilon.}
\tag{1000.17}
$$

The already proved UH cross-curvature is

$$
\mathcal D^p=\frac16\mathcal L_z\mathcal L_t.
$$

Applying it to (1000.17) yields

$$
\mathcal D^{p-1}S_\epsilon
=\frac16\mathcal L_z\mathcal L_t V_\epsilon.
\tag{1000.18}
$$

At the actual CM point the right side has, in total degree $p+1$, the exact polynomial

$$
\boxed{
\left[(\mathcal D^{p-1}S_\epsilon)(P_0)\right]_{p+1}
=-72\,6^6B^7
\sum_{i+j=N-1}w_i f_i g_j\,
z^{p-h+1}t^h,
\qquad h=6i+7.
}
\tag{1000.19}
$$

Indeed at $P_0$ the lift is $(6B)^5z^3t^2$, the curvature is $6B^2zt$, and (1000.5) supplies $-72F(t)G(z)$. The original critical degree $p-6$ is thereby increased by seven. All displayed final exponents are below $p$, and the monomials for distinct original labels are distinct. The factor $-72\,6^6B^7$ is a unit.

Thus the desired same-label nonzero statement is the nonvanishing of the displayed component of the **specified bulk source** (1000.8), after its exact integral reduction and prescribed operations. This is not a sum in which cancellation among different labels has been ignored. It is also not a claim that the component is nonzero. The old scalar/oscillator curvature alone does not determine this specified observation.

## 7. Connection to the genuine normal jet, and the remaining input

The bulk is a concrete, nonzero source before the required critical observation. For example its CM value satisfies the exact low-order identity

$$
\mathcal C(P_0)
=12F'(t)G'(z)
+6F(t)\bigl(-12P_1L-6P_1'\bigr)Y_s(z),
\qquad P_1=-c-\zeta x.
\tag{1000.20}
$$

This follows either from (1000.8), or by differentiating the actual $T$ before specializing and using R995's first projected heat jet. It retains the coefficient derivative of $L^2$. Its coefficient $[z^0t^3]$ is $48$, a unit, since $F'=4t^3+\cdots$ and $G'=1+\cdots$. That low coefficient does not prove (1000.19) nonzero; neither its degree nor its prescribed original label is the required one.

R995's third Serre derivative describes the first coarse CM normal jet of the original columns. It is not the eighth boundary iterate of R997 and is not obtained by deleting the bulk in (1000.13). Conversely, the disappearing boundary (1000.15) does not make the projected scalar horizontal. Equations (1000.8) and (1000.20) exhibit its remaining actual source explicitly.

What is now excluded is the proposed shortcut based solely on this first canonical-zeta/Hasse boundary: it is in the wrong integer-difference classes for the original mask, even after every allowed connection iterate. A proof of the actual bulk observation in (1000.19), or an actual relation putting the R995 branches back in the retained R992 space, is still required. No invariant-space or marked-unit assertion is inferred from a nonzero whole source.

## Dependencies

- [R997](R997-original-epsilon-vector-and-unitary-boundary-source.md): the actual epsilon vector, exchanged coordinates, canonical derivative, complete projected first-$p$ rectangle, and original transported mask.
- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): the exact finite canonical-zeta coefficient formula and original critical-column normalization.
- [R995](R995-original-mixed-source-for-the-first-coarse-CM-normal-jet.md): all canonical-zeta Serre jets, actual projection shifts and normal-source branches.
- [UH](../notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md), especially UH20–UH29: the exact horizontal Frobenius operators, full finite cross-curvature, and integer-difference mask. Their general proofs and old $36$-channel statement are retained.
- [MH](../notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md) and [OP](../notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md): the same Hasse polynomial, $D^p=0$, and original $B=DA(P_0)$.


## Review and scope

The full source formula, both projection shifts, the unique returning coefficient, complete-sum integrality, integer-difference mask cancellation, and the scalar factor and exponents in (1000.19) received independent full paper review by root and handoff_audit. The low coefficient in (1000.20) was independently recovered from the actual derivative of the projected source. No mathematical code was executed. R997 and the older UH/MH/OP identities are consumed with their original normalizations; their existing general connection or curvature statements are not new conclusions here.
