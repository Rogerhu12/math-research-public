# R150: the rank-four second-moment branch on one length-five local support is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** In the essential-four, outer-mean branch with rank-three mean catalecticant, a complete critical point cannot have a length-five divisor concentrated at one point and $\operatorname{rank}H=4$. In fact the unchanged highest-gradient identity alone excludes this canonical case. The point may be finite or infinite.

## 1. The exact canonical local algebra

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), under
$$
\operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\qquad
\dim\operatorname{ess}(T_3)=4,\qquad
y\notin\operatorname{ess}(T_3).
$$
Suppose its unique divisor is $5s_0$. Then
$$
\mathcal A=\mathbb C[t]/(t^5),\qquad
V(r,r,r)=\tfrac18\nu(X_r^3),
$$
with a nondegenerate Frobenius functional $\nu$. The same outer-mean element $L$ satisfies
$$
\nu(L^3)=1,\quad
y(r)=\nu(L^2X_r),\quad
H(r,r)=\tfrac14\nu(LX_r^2),
$$
$$
T_3(r)=\tfrac12\nu\bigl(X_r-\nu(L^2X_r)L\bigr)^3.
\tag{1.1}
$$
Rank four of $H$ is rank four of multiplication by $L$, so $L$ has exactly a simple zero at $s_0$. Choose $t=L$ as the local parameter. This is legitimate: an ambient extension of the same covector $\lambda$ gives a local function $\lambda(u(s))$ with nonzero first derivative, so its inverse gives a local parameter on the original curve. The original form $K$ is unchanged.

We therefore have
$$
L=t,\qquad \nu(t^3)=1,\qquad q:=\nu(t^4)\ne0.
\tag{1.2}
$$
The last inequality is the top-jet condition, or equivalently nondegeneracy of the Frobenius pairing. No normalization or value of $\nu(1),\nu(t),\nu(t^2)$ is needed.

Write the physical local representative in divided jets:
$$
u(s)=\sum_{j\ge0}u_j s^j,\qquad
K_{ij}=u_i^{\mathsf T}Ku_j.
$$
The first five $u_j$ are independent and span the original $E_D$. Physical curve isotropy gives
$$
K_{00}=K_{01}=0,\qquad
2K_{02}+K_{11}=0,\qquad
K_{03}+K_{12}=0.
\tag{1.3}
$$
All these equalities are coefficients of the same original identity $K(u(s),u(s))=0$.

For $j\ge0$ define the element of $\mathcal A$
$$
k_j(t)=u(t)^{\mathsf T}Ku_j\bmod t^5,\qquad
Z_j(t)=k_j(t)-\nu(t^2k_j(t))t.
\tag{1.4}
$$
Here $u(t)$ is the same local representative in the first argument. By symmetry, the constant coefficient of $k_j$ is $K_{0j}$. The full original highest equation becomes the formal identity
$$
0=T_3(Ku(s))
=\tfrac12\nu\left(\sum_{j\ge0}Z_j(t)s^j\right)^3.
\tag{1.5}
$$
It is a consequence of the global binary polynomial identity, hence holds in every local chart. Products of $t$-order at least five vanish in $\mathcal A$.

## 2. The constant coefficient forces $K_{02}=0$

Put $A=K_{02}$, $B=K_{03}$, $C=K_{04}$. By (1.3),
$$
k_0=A t^2+B t^3+C t^4,\qquad
\nu(t^2k_0)=Aq,
$$
so
$$
Z_0=-Aq\,t+A t^2+B t^3+C t^4.
$$
Modulo $t^5$,
$$
Z_0^3=-A^3q^3t^3+3A^3q^2t^4.
$$
Using (1.2), the constant $s$ coefficient of (1.5) is
$$
\tfrac12\nu(Z_0^3)=A^3q^3.
$$
Thus $A=0$. Equation (1.3) also gives $K_{11}=0$, and now $Z_0=k_0$ has $t$-order at least three.

## 3. The cubic coefficient forces $K_{03}=K_{12}=0$

Now $K_{12}=-B$. Write the remaining coefficients of $k_1$ arbitrarily:
$$
k_1=-B t^2+K_{13}t^3+K_{14}t^4,\qquad
Z_1=Bq\,t-B t^2+K_{13}t^3+K_{14}t^4.
$$
Its cube has
$$
\tfrac12\nu(Z_1^3)=-B^3q^3.
\tag{3.1}
$$
The coefficient of $s^3$ in (1.5) is one half of
$$
\nu\bigl(Z_1^3+6Z_0Z_1Z_2+3Z_0^2Z_3\bigr).
$$
Since $K_{02}=0$, $Z_2$ has zero constant term and $t$-order at least one. Hence $Z_0Z_1Z_2$ has order at least $3+1+1=5$, while $Z_0^2Z_3$ has order at least six, regardless of the constant term of $Z_3$. Both vanish in $\mathcal A$.

Consequently (3.1) is the entire coefficient, and $B=0$. Thus
$$
K_{03}=K_{12}=0,\qquad
\operatorname{ord}_t Z_0\ge4,\qquad
\operatorname{ord}_t Z_1\ge3.
\tag{3.2}
$$

## 4. The sixth coefficient forces $K_{22}=0$

Put $J=K_{22}$. With all the preceding vanishing,
$$
k_2=Jt^2+K_{23}t^3+K_{24}t^4,\qquad
Z_2=-Jq\,t+Jt^2+K_{23}t^3+K_{24}t^4.
$$
Therefore
$$
\tfrac12\nu(Z_2^3)=J^3q^3.
\tag{4.1}
$$
We check every other partition of the physical degree six. The triples of nonnegative indices apart from $(2,2,2)$ are
$$
(0,0,6),\ (0,1,5),\ (0,2,4),\
(0,3,3),\ (1,1,4),\ (1,2,3).
$$
Their minimum $t$-orders are respectively
$$
8,\ 7,\ 5,\ 6,\ 6,\ 5.
$$
For these bounds use (3.2), $\operatorname{ord}_tZ_2\ge1$, and $\operatorname{ord}_tZ_3\ge1$ because $K_{03}=0$. No condition is imposed on $Z_4,Z_5,Z_6$ beyond order at least zero. Thus every listed product vanishes modulo $t^5$. Equation (4.1) is the entire sixth coefficient of (1.5), and $J=0$ follows.

The physical length-three jet space
$$
\operatorname{span}\{u_0,u_1,u_2\}
$$
is now totally isotropic: all its Gram entries $K_{00},K_{01},K_{02},K_{11},K_{12},K_{22}$ have been proved zero. This contradicts [the complete classification of isotropic length-three curve jets](R150-appendix-classification-of-isotropic-length-three-curve-jets.md), Sections 4–5, which excludes every triple jet, finite or infinite.

## 5. Accurate consequence

The canonical rank-four branch on divisor type $5$ is empty. The proof used only the original support reduction, original isotropy identities and three coefficients of the unchanged highest-gradient identity, at physical local orders $0,3,6$. It neither assumes any uncomputed elimination nor replaces the complete gradient system by a sufficient subset.

The other rank-four divisor types and the rank-five branch remain open. Together with the separate complete rank-three exclusion, this says that a length-five divisor concentrated at one point could occur in the present outer-mean problem only when the original $H$ has rank five, equivalently when the same $L$ is a unit.
