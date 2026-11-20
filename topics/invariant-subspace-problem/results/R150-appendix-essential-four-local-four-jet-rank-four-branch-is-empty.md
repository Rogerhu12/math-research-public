# R150: the rank-four branch with a simple zero on a quadruple point is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** In the original essential-four outer-mean length-five reduction, no complete critical point has divisor type $4+1$ and a simple zero of the same $L$ on the quadruple-point factor. This is the nonunit rank-four case at that factor, and all weights, including the half-weight case, are covered. No claim is made here about a unit on the quadruple point with $L=0$ at the separate simple point.

## 1. The same physical support and an allowed local normal form

Assume the hypotheses of [the length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md):
$$
\operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\qquad
\dim\operatorname{ess}(T_3)=4,\qquad
y\notin\operatorname{ess}(T_3).
$$
Suppose its unique divisor is $4s_0+s_1$, with $s_0\ne s_1$. Its algebra is
$$
\mathcal A=\mathbb C[t]/(t^4)\times\mathbb C,
$$
and the same outer-mean element $L$ has local order one at $s_0$ and is a unit at $s_1$.

First use $L$ as the local parameter at $s_0$. At the separate point rescale its physical representative $v$ so that $L=1$. If $\nu$ is the original Frobenius functional in the normalization $V=\nu(X^3)/8$, put
$$
a=\nu_{\rm loc}(L^3),\qquad b=\nu_{\rm pt}(L^3).
$$
Both are nonzero: $a$ is the highest local value on the length-four block, and the simple-point coefficient and its $L$ value are nonzero. The unchanged identity $\nu(L^3)=1$ gives $a+b=1$.

There is an allowed change of the local physical representative which makes
$$
L=t,\quad \nu_{\rm loc}(1)=\nu_{\rm loc}(t)=\nu_{\rm loc}(t^2)=0,\quad
\nu_{\rm loc}(t^3)=a,\quad \nu_{\rm pt}=b.
\tag{1.1}
$$
Here is its full construction. Starting with parameter $t=L$, replace the local representative by $h(t)u(t)$, where
$$
h(t)=1+\eta_1t+\eta_2t^2+\eta_3t^3,
$$
and use the new parameter $z=h(t)t$. The same covector now has local value $z$, and the transformed functional is
$$
\widetilde\nu(f(z))=\nu\bigl(h(t)^{-3}f(h(t)t)\bigr).
\tag{1.2}
$$
Thus $V,y,H$ and the original $K$ are unchanged: the three factors of $h$ cancel in $V$, and the same cancellation holds for $\nu(L^2X)$ and $\nu(LX^2)$. Also $\widetilde\nu(z^3)=\nu(t^3)=a$ exactly. The lower values are killed successively using
$$
t^2h^{-1}=t^2-\eta_1t^3,
$$
$$
th^{-2}=t-2\eta_1t^2+(3\eta_1^2-2\eta_2)t^3,
$$
$$
h^{-3}=1-3\eta_1t+(6\eta_1^2-3\eta_2)t^2
+(-10\eta_1^3+12\eta_1\eta_2-3\eta_3)t^3.
$$
The respective new coefficients are $-a,-2a,-3a$, all nonzero. The parameter change has derivative one, and $h(0)=1$, so this is an invertible physical jet change. Rename $z$ as $t$. It proves (1.1) without altering the given $L$ or replacing its zero by a unit.

Write the corresponding divided jets as $u_0,u_1,u_2,u_3$. For a covector $r$ put
$$
R=r(u_0),\quad X=r(u_1),\quad Y=r(u_2),\quad Z=r(u_3),\quad T=r(v).
$$
Then the original moments are exactly
$$
y=a u_1+bv,\qquad
H(r,r)=\tfrac a4(2RY+X^2)+\tfrac b4T^2,
$$
$$
V(r,r,r)=\tfrac a8(3R^2Z+6RXY+X^3)+\tfrac b8T^3.
\tag{1.3}
$$
In the complete cubic $T_3=y(r)^3-6y(r)H(r,r)+4V(r,r,r)$ set $U=X-T$. A direct expansion gives
$$
T_3=\tfrac{3a}{2}\left[
R^2Z+2bRYU+\tfrac{b(b-a)}3U^3
\right].
\tag{1.4}
$$

## 2. Original mean equations without division by $L$

We record the general nonunit formula used below. In any of these length-five algebras let $k(t,s)$ be the original physical Gram kernel, and set
$$
d(t)=\nu_s\bigl(L(s)^2k(t,s)\bigr),\qquad
(D_Lf)(t)=\nu_s\bigl(L(s)k(t,s)f(s)\bigr),
$$
$$
e_L(t)=\nu_s\bigl(L(s)k(t,s)^2\bigr),\qquad
F=\tfrac12\nu(L^2d).
$$
At a complete critical point, contracting the original mean gradient with the same outer-mean covector gives $\mathcal Q_{F_0^2}=0$. The rest of that full mean gradient is
$$
-4FHp+8HKHp+4V(p,p,\cdot)-8V:(KHK)=0,\qquad p=Ky.
$$
Because the pairing $J_\nu(X,Y)=\nu(XY)$ is nondegenerate, multiplication by $-4J_\nu^{-1}$ gives the exact element equation
$$
\boxed{e_L-2L D_Ld-2d^2+4FLd=0.}
\tag{2.1}
$$
Indeed $H=J_\nu m_L/4$, $V(p,p,\cdot)=J_\nu(d^2)/8$, and the last contraction is $J_\nu(e_L)/32$. Only $J_\nu$ is inverted; no inverse of $L$ is used. Thus (2.1) is a necessary consequence of the complete original mean equations, including on the singular second-moment branch.

For the rest write
$$
K_{ij}=K(u_i,u_j),\quad c_i=K(u_i,v),\quad
A=K_{02},\quad B=K_{03},\quad D=K_{22}.
$$
The original curve identity gives
$$
K_{00}=K_{01}=K(v,v)=0,\qquad K_{11}=-2A,\qquad K_{12}=-B.
\tag{2.2}
$$
In the local algebra the polar mean has coefficients
$$
d_{\rm loc}(t)=bc_0+(-2aA+bc_1)t+(-aB+bc_2)t^2
+(aK_{13}+bc_3)t^3.
\tag{2.3}
$$
At the separate point it has value $d_{\rm pt}=ac_1$, and
$$
F=-a^2A+ab c_1.
\tag{2.4}
$$

The highest identity is (1.4) evaluated on the entire original physical curve. Below the same letters $R,X,Y,Z,T,U$ denote their physical quintic polars. They remain independent where their defining vectors are independent; the nonzero physical polar $R$ cannot vanish identically.

## 3. Every non-half-weight case is impossible

Suppose $a\ne b$. At the local base $u_0$, the highest identity has $R=X=0$ and $U=-c_0$. Since $ab(b-a)\ne0$, it forces $c_0=0$. At the separate point $v$, we then have $R=T=0$ and $U=c_1$, so it also forces $c_1=0$.

In a compatible local representative
$$
u(s)=u_0+u_1s+u_2s^2+u_3s^3+\cdots
$$
at $s_0$, the polars therefore begin
$$
R=A s^2+B s^3+O(s^4),\quad
U=-2A s+O(s^2),\quad
Y=A+O(s),\quad Z=B+O(s).
$$
The physical order-three coefficient of the bracket in (1.4) is
$$
-\tfrac{4b}{3}(1+4b)A^3.
\tag{3.1}
$$
Here $R^2Z$ starts at order four; the other two terms contribute $-4bA^3$ and $-8b(b-a)A^3/3$.

The local $t^2$ coefficient of the unchanged mean equation (2.1) is
$$
2a(2a-1)(2a-3)A^2=0.
\tag{3.2}
$$
For a direct check, under $c_0=c_1=0$, the needed coefficients are
$$
[d]_{t}=-2aA,\quad F=-a^2A,\quad
[e_L]_{t^2}=6aA^2,\quad [D_Ld]_t=4a^2A^2.
$$
Equation (2.1) at $t^2$ is therefore
$6aA^2-8a^2A^2-8a^2A^2+8a^3A^2$,
which is (3.2).

If $A\ne0$, (3.2) gives $a=1/2$ or $a=3/2$. The first contradicts the non-half-weight assumption. The second gives $b=-1/2$, and then (3.1) is nonzero. Thus $A=0$.

Consequently $\operatorname{span}\{u_0,u_1,v\}$ is a totally isotropic original length-three jet space of type $2+1$: all its Gram entries vanish by (2.2) and $c_0=c_1=0$. The [complete isotropic-length-three classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md), Sections 3–5, excludes this physical type, including infinity. This closes all $a\ne b$ cases.

## 4. The full half-weight case is also impossible

Now $a=b=1/2$. The highest identity (1.4) factors as a nonzero scalar times $R$ times the quadratic expression
$$
Q=RZ+Y(X-T).
$$
Since the physical polar $R$ is nonzero and the binary polynomial ring is a domain, the full highest identity gives
$$
Q\equiv0.
\tag{4.1}
$$
We keep this complete identity, not merely values at the support.

At the separate point, equation (2.1) gives
$$
Bc_0+Ac_1=0.
\tag{4.2}
$$
Here is the explicit coefficient computation. The separate-point components are
$$
e_L=\tfrac12(c_1^2+2c_0c_2),\quad
D_Ld=-\tfrac14c_0B+\tfrac12c_0c_2-\tfrac12Ac_1+\tfrac14c_1^2,
$$
$$
d=c_1/2,\qquad F=(c_1-A)/4.
$$
Their combination $e_L-2D_Ld-2d^2+4Fd$ is exactly $(Bc_0+Ac_1)/2$.

The constant and linear local coefficients of (4.1) are
$$
-Ac_0=0,\qquad Bc_0-2A^2-Ac_1=0.
\tag{4.3}
$$
If $A\ne0$, the first gives $c_0=0$, (4.2) gives $c_1=0$, and the second gives $-2A^2=0$, impossible. Hence $A=0$.

The local expansions now read
$$
R=B s^3+O(s^4),\quad
X=-B s^2+O(s^3),\quad
Y=-B s+D s^2+O(s^3),\quad Z=B+O(s),
$$
$$
T=c_0+c_1s+c_2s^2+\cdots.
$$
The linear and quadratic coefficients of $Q$ are respectively
$$
Bc_0,\qquad Bc_1-Dc_0.
\tag{4.4}
$$
If $B\ne0$, these force $c_0=c_1=0$.

If $B=0$ and $D=0$, all Gram entries on the local triple jet $\operatorname{span}\{u_0,u_1,u_2\}$ already vanish, contradicting the same complete isotropic-jet classification. Thus in the remaining case $D\ne0$. The quadratic coefficient in (4.4) gives $c_0=0$. Furthermore $R$ has order at least four, $Z$ at least one, $Y=D s^2+O(s^3)$, and $X$ at least three. The cubic coefficient of $Q$ is now $-Dc_1$, forcing $c_1=0$.

We have proved $A=c_0=c_1=0$ in every possible half-weight case as well. This again makes $\operatorname{span}\{u_0,u_1,v\}$ a forbidden totally isotropic $2+1$ physical jet space. The half-weight case is empty.

## 5. Accurate conclusion

The entire rank-four alternative with a simple zero of the original $L$ on a length-four block and a unit on its distinct simple-point block is excluded. The proof retained the original $K$, the same $L$, the full physical highest identity and necessary coefficients of the complete mean gradient. All local normalizations were invertible changes of physical representatives and local parameter with the tensors explicitly preserved by (1.2).

Together with the separate exclusion of the simple-zero rank-four length-five local block, this closes the nonunit local blocks of lengths five and four. Blocks of lengths three or two, the rank-four case where a reduced point has $L=0$, and the rank-five unit case remain to be analyzed. No Bell value or global Jacobian membership is inferred from this branch exclusion alone.
