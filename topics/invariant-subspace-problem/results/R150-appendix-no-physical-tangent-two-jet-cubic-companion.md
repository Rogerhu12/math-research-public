# R150 appendix — no physical tangent two-jet cubic companion with a nonzero mean cube

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, as a pure statement about the original physical kernel.

## 1. Statement

Let $u_0=v(s)$ be any original physical point, let $u_1$ be a genuine
first jet there, and let $y$ be independent of $u_0,u_1$.
Use their original quintic polars
$$
p_0=u_0^{\mathsf T}Kv,\qquad p_1=u_1^{\mathsf T}Kv,\qquad
P=y^{\mathsf T}Kv.
$$
For arbitrary complex $h_0,h_1,v_0,v_1$ and $\kappa\ne0$, form
$$
C(Y,X,Z)=
\kappa Y^3-6Y(h_0X^2+2h_1XZ)+4(v_0X^3+3v_1X^2Z).
\tag{1.1}
$$

**Theorem.** It is impossible that $C(P,p_0,p_1)=0$ identically
and that the image of $[P:p_0:p_1]$ is an irreducible plane cubic.

The assertion includes every zero coefficient among $h_i,v_i$,
every finite or infinite $s$, all choices of genuine local first
jet, and every $y$ outside the tangent two-space. It imposes no
catalecticant condition on $y$ and uses no lower critical gradient.
It is the cubic-image obstruction; a conic image is a separate
case and is not assumed absent here.

## 2. A useful original squarefreeness fact

Write
$$
k(s,z)=-(z-s)^2q(s,z),
$$
$$
q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2+
(s^3-3s^2+22s)z+s^3-5s^2.
$$

**Lemma.** If the homogeneous greatest common divisor $D$ of a
physical value polar and its genuine first-jet polar has degree two,
then $p_0/D$ is a squarefree binary cubic.

Here and below squarefree means three distinct projective roots.
The
[physical tangent common-factor theorem](R150-appendix-physical-tangent-cubic-gcd-only-zero-and-infinity.md)
proves that the common divisor has degree exactly three at $s=0,\infty$,
and at most two everywhere else. Thus those exceptional points
do not occur under the lemma's assumption.

At $s=2,-6$, the value and first-jet self orders are three and two.
Their cubic-polar coefficient pairs $q,q_s$ have no common root
away from $s$, as proved by the nonzero original resultants
$-124928,-488208384$. Hence $D$ is precisely the double self point,
and the residual value cubics are, up to nonzero scalars,
$$
(z-2)(3z^2-17z+6),\qquad
(z+6)(5z^2+65z+66).
$$
The quadratic discriminants are $217,2905$, and their values at
the displayed self roots are $-16,-144$.
Both residual cubics are squarefree.

It remains that $s$ is finite and outside $\{0,2,-6\}$.
The self orders are two and one, so a degree-two common divisor
has, in addition to one self point, an off-diagonal point $t$.
For finite $s$, an infinite $t$ is impossible: the leading
coefficient of $q(s,z)$ is $s+1$, while its $s$ derivative is one.
The off-diagonal common-zero conditions are therefore
$$
q(s,t)=q_s(s,t)=0.
\tag{2.1}
$$
The original bicubic is smooth off the diagonal, so $q_z(s,t)\ne0$;
in particular this is a simple root of $q(s,\cdot)$.

Section 3 of
[the shifted-tangent companion theorem](R150-appendix-no-physical-shifted-tangent-conic-companion.md)
proves the stronger, projectively complete consequence of (2.1):
$q(s,\cdot)$ has three distinct roots.
For clarity, its exact arithmetic content is that, with
$$
E_8(z)=5z^8+50z^7+153z^6-936z^5-2888z^4+
15936z^3-3392z^2-25472z+9600,
$$
$$
D_4(z)=6z^4+24z^3-18z^2-36z+25,\qquad
N_5(z)=3z^5+3z^4+26z^3+6z^2+110z,
$$
(2.1) gives
$$
E_8(t)=0,\qquad s=N_5(t)/(2D_4(t)),\qquad E_8(s)\ne0.
$$
The last nonvanishing is proved there by a retained-degree integer
resultant, with its complete modular Bezout certificate; it is not
a numerical genericity assertion. The exceptional cubic at $s=-1$
also has three distinct projective roots and is included.

Furthermore $q(s,s)\ne0$ in the current case. Removing the common
divisor therefore leaves
$$
p_0/D \ \propto\ (z-s)\,q(s,z)/(z-t),
$$
with one simple self root and the two remaining distinct roots
of $q$. It is squarefree. This proves the lemma in every chart.

Rescaling $u_1$ or adding a multiple of $u_0$ changes neither its
common divisor with $p_0$ nor this conclusion.

## 3. The complete common divisor is forced by the identity

Let $G$ be the common divisor of $P,p_0,p_1$, and let
$D=\gcd(p_0,p_1)$, both homogeneous.
We prove equality including multiplicities.

At any projective point, use a local trivialization and put
$$
m=\min(\operatorname{ord}p_0,\operatorname{ord}p_1),\qquad
d=\operatorname{ord}P.
$$
If $d<m$, the term $\kappa P^3$ in (1.1) has order $3d$.
Every term involving $PH$ has order at least $d+2m>3d$;
every term involving $V$ has order at least $3m>3d$.
Its nonzero leading coefficient cannot cancel. Thus $d\ge m$.

This applies at every finite or infinite point and proves
$$
G=D.
\tag{3.1}
$$
In particular the identity cannot discard one order of a tangent
common zero by taking a smaller base divisor.

## 4. Cubic-image degree and the final contradiction

The three polars are independent because $K$ is nondegenerate.
After removing $G$ they define a morphism from $\mathbb P^1$.
If its image is an irreducible cubic and its covering degree is $e$,
the pullback of a general line gives
$$
5-\deg G=3e.
$$
Thus $e=1,\deg G=2$. By (3.1), the lemma applies:
$$
A=p_0/G
$$
is a squarefree binary cubic. Write also $B=p_1/G$ and $R=P/G$.

Divide the highest identity by $G^3$ and reduce it at any root of $A$.
All terms except $\kappa R^3$ have a factor $A$, so $R$ vanishes
at that root. There are three different roots. Since $R$ is also
a binary cubic, it follows that $R=cA$ for a constant $c$.
Multiplying by $G$ gives $P=cp_0$.

The original invertible $K$ and the fact that physical vectors span
the full six-dimensional space imply $y=c u_0$. This contradicts
the assumed independence of $y,u_0,u_1$ and proves the theorem.

## 5. Use in the rank-two-mean support problem

Whenever an already justified support reduction gives
$$
T_3=\kappa Y^3-6YH_R+4V_R,\qquad \kappa\ne0,
$$
with $R=2s$ an exact physical tangent block, $Y$ outside that block,
and $H_R,V_R$ its original Hankel quadratic and cubic tensors,
(1.1) is exactly its complete third tensor.
The irreducible-cubic alternative is therefore empty.
The theorem is valid whether $V_R$ has rank one or rank two.

No independent verification stage is inserted. The only finite
arithmetic facts used are the existing original-kernel certificates
cited in §2; the new common-divisor and squarefree-root arguments
are proved here. Conic alternatives, $\kappa=0$, other support types,
global Jacobian powers, and the ordinary Hilbert ISP are not
silently included in this conclusion.
