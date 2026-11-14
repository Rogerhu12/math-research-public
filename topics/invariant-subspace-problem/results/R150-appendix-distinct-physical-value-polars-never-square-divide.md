# R150 appendix — a physical value polar never divides the square of a different physical value polar

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, for the unchanged original six-mode kernel.

## 1. Pure original-kernel statement

For different physical points $s,t\in\mathbb P^1$, let
$$
p_s(z)=v(s)^{\mathsf T}Kv(z),\qquad
p_t(z)=v(t)^{\mathsf T}Kv(z).
$$
Then, as homogeneous binary quintics,
$$
\boxed{p_s\ \nmid\ p_t^2.}
\tag{1.1}
$$
All nonzero choices of physical representatives and all infinite
points are included. No critical-point or mean-rank hypothesis is used.

In particular there is no identity
$$
p_s p_Z+\alpha p_s^2+\beta p_t^2=0,\qquad \beta\ne0,
\tag{1.2}
$$
for any vector $Z$ and scalar $\alpha$.
This useful conic obstruction concerns two physical value directions,
rather than a value direction and its first jet.

## 2. Existing original-polar facts

The
[length-four projection theorem](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)
proves that two different physical value polars have common divisor
of degree at most three:
$$
\deg\gcd(p_s,p_t)\le3.
\tag{2.1}
$$
The original kernel is
$$
p_s(z)=-(z-s)^2q(s,z),
$$
and the
[original bicubic calculations](R150-appendix-three-distinct-physical-support-complete-critical-classification.md)
prove that no cubic polar $q(s,\cdot)$ is a pure cube.
They also give
$$
\operatorname{disc}_z q(s,z)=s^2E_8(s),
$$
$$
E_8(s)=5s^8+50s^7+153s^6-936s^5-2888s^4+
15936s^3-3392s^2-25472s+9600.
\tag{2.2}
$$

The exact self orders are two generically, three at $2,-6$, and
four at $0,\infty$. At $2,-6$ the other two roots are distinct and
simple. At $0,\infty$ the divisors are respectively
$$
4[0]+[5],\qquad4[\infty]+[-1].
\tag{2.3}
$$
These are homogeneous statements; the finite source $s=-1$ has a
simple target root at infinity and no repeated cubic root.

Suppose, toward contradiction, that $p_s\mid p_t^2$.
Every root of $p_s$ is then a root of $p_t$.
In particular $p_t(s)=0$, and symmetry gives $p_s(t)=0$.

## 3. Four-root and higher-self-order cases

If $p_s$ has four distinct projective roots, all four divide the
common divisor, contradicting (2.1).

If $s=2$ or $-6$, divisibility requires $p_t$ to have order at least
two at $s$, because $p_s$ has self order three.
Together with its other two simple roots, the common divisor again
has degree at least four, a contradiction.

If $s=0$, (2.3) and $t\ne s$ force $t=5$.
But direct evaluation of the original polar gives
$$
p_5(0)=0,\qquad p_5'(0)=-4000.
$$
Its order at zero is only one, and its square cannot contain the
fourth-order zero of $p_0$.

If $s=\infty$, (2.3) similarly forces $t=-1$.
The $z^5,z^4$ coefficients of $p_{-1}$ are $0,5$.
Thus its order at infinity is one, and again its square has
insufficient order.

Every source covered by these alternatives is excluded.

## 4. The only remaining repeated-cubic-root pattern

The only remaining possibility is
$$
\operatorname{div}(p_s)=2[s]+2[u]+[r],
\tag{4.1}
$$
where $s,u,r$ are different and $E_8(s)=0$.
There is no triple cubic root by §2.
Since $t$ is a root of $p_s$ and differs from $s$, either $t=u$ or
$t=r$.

If $t=u$, the common divisor contains at least one copy of $s$,
two copies of $u$ (a physical self zero), and one copy of $r$.
Its degree is at least four, contradicting (2.1).

If $t=r$, divisibility also forces $p_t(u)=0$.
The three different physical points $s,u,t$ are therefore mutually
orthogonal for $K$. Their three-space is totally isotropic.
The complete
[physical isotropic length-three classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)
makes it $W_+$ or $W_-$.

Consequently $s$ must be a root of one of the integer support cubics
$$
P_+(s)=5s^3-25s^2+32s-8,\qquad
P_-(s)=5s^3+135s^2+864s+864.
$$
Neither has a common root with $E_8$, as the following exact
certificate shows.

## 5. Two retained-degree Bezout identities

All lists here are in ascending powers. Modulo $103$ define
$$
\begin{aligned}
U_+&=(10,64,93,8,75,43,39,56),&
V_+&=(48,80,47),\\
U_-&=(42,33,59,61,54,92,11,38),&
V_-&=(77,64,65).
\end{aligned}
$$
Direct multiplication gives
$$
U_+P_++V_+E_8=1,\qquad
U_-P_-+V_-E_8=1
\quad\text{in }\mathbb F_{103}[s].
\tag{5.1}
$$
The original degrees three and eight remain complete after reduction:
all three leading coefficients are five.
Thus both integer resultants are nonzero, and $E_8$ has no common
complex root with either $P_+$ or $P_-$.
This contradicts (4.1), finishing the last case.

The argument uses the finite-field identities solely to prove
nonzero retained-degree integer resultants. It does not infer a
complex conclusion from a finite-field point enumeration.

## 6. Exact record and scope

- [author verifier](../notes/2026-11-14-distinct-physical-polar-square-exclusion-verify.js)
- [execution record](../notes/2026-11-14-distinct-physical-polar-square-exclusion-verification.json)

The executable checks both identities (5.1), retained degrees,
and the exceptional polar coefficients directly from the original
integer matrix $K$, using actual BigInt arithmetic.
The root-divisor and isotropic-space arguments are proved in the text.

The result excludes (1.2) and its homogeneous scalar multiples.
It does not claim a corresponding divisibility prohibition for an
arbitrary nonphysical vector, or classify every conic projection.
