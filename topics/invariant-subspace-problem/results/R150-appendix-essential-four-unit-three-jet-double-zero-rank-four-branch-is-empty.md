# R150: a unit triple jet and a simple zero on the double factor cannot be rank-four critical

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** In the original essential-four outer-mean length-five reduction, the rank-four branch with divisor type $3+2$, $L$ a unit on the triple factor and of order one on the double factor, is empty. Together with the exclusion with the two roles reversed, this removes all rank-four placements on divisor type $3+2$.

## 1. Original normalization and the necessary equations

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md) under its rank-three mean-catalecticant, essential-four and outer-mean hypotheses. The algebra is
$$
\mathcal A=\mathbb C[t]/(t^3)\times\mathbb C[\epsilon]/(\epsilon^2).
$$
On the first factor divide the physical representative by the same unit $L$; then normalize its parameter so that
$$
L=1,\qquad \tau(1)=1,\quad \tau(t)=0,\quad \tau(t^2)=1.
\tag{1.1}
$$
An invertible change $t\mapsto c_1t+c_2t^2$ first normalizes the nonzero top value and then kills the middle value.

On the second factor keep $L$ as its local parameter and use the allowed physical rescaling described in [the isotropic-active double-zero exclusion](R150-appendix-essential-four-double-zero-rank-four-isotropic-active-branch-is-empty.md), Section 1, so that
$$
L=\epsilon,\qquad \nu(1)=0,\qquad \nu(\epsilon)=1.
\tag{1.2}
$$
That change explicitly preserves the original tensors and the same $L$; it does not divide by the nonunit.

Let $u_0,u_1,u_2$ be the three active physical jets, and $w_0,w_1$ the double-point jets. For a covector $r$ use
$$
X=r(u_0),\quad Y=r(u_1),\quad Z=r(u_2),\quad
R=r(w_0),\quad S=r(w_1).
$$
The exact moments and cubic are
$$
y(r)=X+Z,\qquad
H(r,r)=\tfrac14(X^2+Y^2+2XZ+R^2),
$$
$$
V_{\rm act}(r,r,r)=\tfrac18\tau((X+Yt+Zt^2)^3),\qquad
V_{\rm dbl}(r,r,r)=\tfrac38R^2S,
$$
$$
T_3=P(Y,Z)+\tfrac32R^2(S-X-Z),\qquad
P(Y,Z)=Z^3-\tfrac32ZY^2.
\tag{1.3}
$$

Write the active Gram matrix and the base cross column as
$$
K_a=\begin{pmatrix}0&0&A\\0&-2A&B\\A&B&C\end{pmatrix},
\qquad
U=(x,y,z)=(K(u_0,w_0),K(u_1,w_0),K(u_2,w_0)).
\tag{1.4}
$$
The entries $K_{00}=K_{01}=0$, $K_{11}=-2K_{02}$ are the original physical curve isotropy. The entire five-dimensional support has Gram rank at least four, because its radical has dimension at most one in the original nondegenerate six-dimensional space.

The active complete mean equation in the simple-zero-on-a-double-point case is
$$
E_a+U^2-2d_0U=0,\qquad d_0=\tau(U)=x+z,
\tag{1.5}
$$
and the constant mean equation on the double factor is
$$
\tau(U^2)=2d_0^2.
\tag{1.6}
$$
These are the exact original mean identities derived in Section 1 of the linked double-zero exclusion from
$e_L-2L D_Ld-2d^2+4FLd=0$; no restricted mean equations replace the original ones.

For the active local algebra, direct substitution gives
$$
E_a=\bigl(2AC,\ 2B(A+C),\
2(A^2-AC+C^2-2B^2)\bigr).
$$
The coefficients of $U^2-2d_0U$ are
$(-x^2-2xz,-2yz,y^2-2z^2)$.
Combining (1.5) and (1.6) therefore gives the four exact relations
$$
\boxed{
x^2+2xz=2AC,\quad yz=B(A+C),\quad
y^2-2z^2=2AC,\quad A^2+C^2=2B^2.
}
\tag{1.7}
$$

## 2. The original highest and second equations at the double base

Physical isotropy gives
$$
R(w_0)=K(w_0,w_0)=0,\qquad S(w_0)=K(w_1,w_0)=0.
$$
Consequently the unchanged highest identity at this physical point is
$$
P(y,z)=z^3-\tfrac32zy^2=0.
\tag{2.1}
$$

For the original tensor $N=T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH$, every term involving the double factor has a factor $R$. Indeed its exact additional part is
$$
d_0R(S-X-Z)+\tfrac12(d_1-F)R^2
+\tfrac12\tau(U(X+Yt+Zt^2))R,
$$
where $d_1=\tau(K(w_1,\cdot))$ and $F=A+C/2$. At the physical double base this vanishes. The complete original second-gradient identity there therefore requires $N_a(x,y,z)=0$, where
$$
N_a(X,Y,Z)=
\tfrac C2 Z^2-\tfrac{A+C}{2}XZ-\tfrac{2A+C}{4}Y^2
+\tfrac B2XY-BYZ.
\tag{2.2}
$$
For a direct source, the active cubic is $P(Y,Z)$, its polar mean is $(A,B,A+C)$, and its Frobenius matrix is
$$
J=\begin{pmatrix}1&0&1\\0&1&0\\1&0&0\end{pmatrix}.
$$
Substitution of $T_{3,Ky}$, $-F(yy^{\mathsf T}-2H)$ and $4HKH=JK_aJ/4$ yields (2.2). Thus the condition used below is a coefficient of the full original eleven second-moment gradients.

We now show that (1.7), (2.1), and (2.2) are already impossible with the required Gram rank.

## 3. The case $z=0$

Here (1.7) gives
$$
x^2=y^2=2AC,\qquad B(A+C)=0,\qquad A^2+C^2=2B^2.
\tag{3.1}
$$
If $AC=0$, these identities force $A=B=C=x=y=0$. The active Gram block and the cross column against $w_0$ are then zero. The remaining cross column against $w_1$ has rank at most one, leaving at least two active vectors in the radical of the full Gram form. This contradicts its rank at least four.

Hence $AC\ne0$. If $B=0$, then $A^2+C^2=0$. Equation (2.2), using $z=0$ and $y^2=2AC$, gives
$$
0=N_a(x,y,0)=-\tfrac12AC(2A+C).
$$
Thus $C=-2A$, contradicting $A^2+C^2=0$ and $A\ne0$.

If $B\ne0$, (3.1) gives $C=-A$ and $B^2=A^2$. Since $x^2=y^2=-2A^2\ne0$, put $\eta=y/x\in\{1,-1\}$. Equation (2.2) becomes
$$
0=\tfrac12A^3-\eta BA^2,
$$
so $\eta B=A/2$. Squaring contradicts $B^2=A^2$ and $A\ne0$. Thus no $z=0$ case remains.

## 4. The case $z\ne0$

Equation (2.1), together with (1.7), gives
$$
z^2=-\tfrac32AC,\qquad y^2=-AC.
\tag{4.1}
$$
Thus $A,C,y$ are nonzero. Also $B$ and $A+C$ are nonzero, since $yz=B(A+C)$.

Set
$$
t=C/A,\qquad r=x/z.
$$
The first relation in (1.7) gives
$$
r^2+2r+\tfrac43=0.
\tag{4.2}
$$
Squaring $yz=B(A+C)$ and using (4.1) and $2B^2=A^2+C^2$ gives
$$
(A^2+C^2)(A+C)^2=3A^2C^2.
$$
After division by $A^4$ this factors as
$$
(t^2-t+1)(t^2+3t+1)=0.
\tag{4.3}
$$

There is also a particularly small form of the full second-gradient condition. Multiply (2.2) by four and use (1.7) and (4.1). Its value at $U$ simplifies to
$$
4N_a(U)=
r(A+C)(A^2+3AC+C^2)
-2(A^3+2AC^2+C^3).
$$
Thus
$$
r(1+t)(1+3t+t^2)=2(1+2t^2+t^3).
\tag{4.4}
$$
For example, the terms without $x$ combine to
$-2(A^3+2AC^2+C^3)$; the $x$ terms are
$2(x/z)(A+C)(B^2-z^2)
=r(A+C)(A^2+3AC+C^2)$.
This verifies the displayed simplification directly.

If $t^2+3t+1=0$, the left side of (4.4) is zero, whereas its right side reduces to $4(1+t)$. This would give $t=-1$, which is not a root of $t^2+3t+1$. Hence this factor in (4.3) is impossible.

The other factor gives $t^2-t+1=0$ and $t^3=-1$. Equation (4.4) then gives
$$
r=\frac{t}{1+t},
$$
with nonzero denominator. Substituting into (4.2) and multiplying by $3(1+t)^2$ gives
$$
13t^2+14t+4=9(3t-1)=0,
$$
where the middle equality uses $t^2=t-1$. Thus $t=1/3$, but $t^2-t+1=7/9$ at that value. This is the final contradiction.

## 5. Accurate conclusion

Both cases for $z$ are exhausted. The proof uses only the original complete mean equations, the highest identity at the physical double base, the original second-gradient value at that same base, and the unavoidable Gram rank bound. No uncomputed elimination, finite-field lift or positivity assumption is used.

The unit triple-jet/simple-zero double-jet branch is empty, including infinity. With the earlier exclusion of a simple zero on a triple block and a unit double block, every rank-four placement on divisor type $3+2$ is now excluded. The unit complements of types $2+1$ and $1+1+1$ for a simple-zero double block remain distinct cases; isolated zero points with other unit length-four supports and rank five also remain open.
