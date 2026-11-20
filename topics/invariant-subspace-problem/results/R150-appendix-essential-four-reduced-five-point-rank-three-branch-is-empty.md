# R150: the reduced five-point, rank-three second-moment branch is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** Under the original essential-four, outer-mean and rank-three mean-catalecticant hypotheses, a complete critical point cannot have $\operatorname{rank}H=3$ and a reduced length-five support. All half-weights, vanishing pairings and a point at infinity are included. No computer algebra output is assumed.

## 1. The same original five points

Use [the length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md). Its rank-three case splits the support into three active points and two zero points of the same $L$. Normalize the active representatives by the same $\lambda$ to have $\lambda(u_i)=1$. Their weights $a,b,c$ are nonzero and sum to one. Rescale the two zero-point representatives using their nonzero cubic coefficients. Then
$$
y=au_1+bu_2+cu_3,\quad H=\tfrac14(au_1^2+bu_2^2+cu_3^2),\quad
V=\tfrac18(au_1^3+bu_2^3+cu_3^3)+\tfrac14(u_4^3-u_5^3).
$$
The complete third moment, with $X_i=u_i^{\mathsf T}r$, is
$$
T_3=P(X_1,X_2,X_3)+X_4^3-X_5^3,\qquad
P(X)=\tfrac12\sum_{i=1}^3w_i(X_i-\sum_jw_jX_j)^3, \tag{1.1}
$$
where $(w_1,w_2,w_3)=(a,b,c)$. The five vectors are independent. Write $k_{ij}=u_i^{\mathsf T}Ku_j$. Physical curve isotropy gives $k_{ii}=0$. Since $K$ is nondegenerate in dimension six,
$$
\operatorname{rank}(K|_E)\ge4,\qquad E=\operatorname{span}(u_1,\ldots,u_5), \tag{1.2}
$$
because its radical is contained in the one-dimensional $E^{\perp_K}$.

All the [original low-gradient identities](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md), Sections 2–3, apply. Pairing the complete mean equation with $\lambda$ gives $\mathcal Q_{F_0^2}=0$. The full highest equation is the binary polynomial identity
$$
P(p_1,p_2,p_3)+p_4^3-p_5^3=0,\qquad
p_i(z)=u_i^{\mathsf T}Kv_{\rm hom}(z). \tag{1.3}
$$
All $p_i$ have degree five. This identity is retained on the entire physical curve, not only its five support points.

## 2. Exact active mean equations

Set $x=k_{12},y_0=k_{13},z_0=k_{23}$ and $A=2a-1,B=2b-1,C=2c-1$. With
$$
d=K_a(a,b,c)^{\mathsf T},\quad D=K_a\operatorname{diag}(a,b,c),\quad
F=abx+acy_0+bcz_0,\quad e_i=\sum_jw_jk_{ij}^2,
$$
the active coefficients of the complete mean equation give
$$
E=e-2Dd-2(d_i^2)_i+4Fd=0. \tag{2.1}
$$
Indeed, after $\mathcal Q_{F_0^2}=0$, that equation is
$-4FHp+8HKHp+4V(p,p,\cdot)-8V:(KHK)=0$, $p=Ky$.
Its $u_i$ coefficient multiplied by $-4/w_i$ is (2.1). Expanding gives
$$
\begin{aligned}
E_1={}&bABx^2+4bcAxy_0+2bcBxz_0+cACy_0^2+2bcCy_0z_0,\\
E_2={}&aABx^2+2acAxy_0+4acBxz_0+2acCy_0z_0+cBCz_0^2,\\
E_3={}&2abAxy_0+2abBxz_0+aACy_0^2+4abCy_0z_0+bBCz_0^2.
\end{aligned} \tag{2.2}
$$
At most one of $A,B,C$ is zero. Relabel so that $A,B\ne0$. The coefficient matrix $M$ of $x^2,xy_0,xz_0$ in (2.2) has determinant $-8a^2b^2cA^2B^2\ne0$. Direct comparison gives $E=M(Q_1,Q_2,Q_3)^{\mathsf T}$, where
$$
\begin{aligned}
Q_1&=x^2-\frac{cC}{bB}y_0^2-\frac{4cC}{AB}y_0z_0-\frac{cC}{aA}z_0^2,\\
Q_2&=xy_0+\frac C{2b}y_0^2+\frac CAy_0z_0,\\
Q_3&=xz_0+\frac CBy_0z_0+\frac C{2a}z_0^2.
\end{aligned} \tag{2.3}
$$
If $C\ne0$, $y_0Q_3-z_0Q_2=0$ gives $y_0z_0(aAy_0-bBz_0)=0$. When $y_0=0,z_0\ne0$, $Q_3$ gives $x=-Cz_0/(2a)$ and $Q_1$ becomes $CBz_0^2/(4a^2A)=0$, impossible. The symmetric case gives $CAy_0^2/(4b^2B)=0$. If both are zero, $x=0$. Otherwise
$$
y_0=\frac{bB}{aA}z_0,\qquad x=\frac{C^2}{2aA}z_0,
$$
and $Q_1=C^2z_0^2/(4a^2A^2)\ne0$, again impossible. Thus without a half-weight the active Gram matrix is zero. If there is a half-weight, label it $c=1/2$; (2.3) then forces only $k_{12}=0$ at this stage.

## 3. Every isotropic active case is impossible

Suppose $K_a=0$. Let $U=(k_{14},k_{24},k_{34})$, $V'=(k_{15},k_{25},k_{35})$ and $\tau Z=\sum_iw_iZ_i$. Then $F=HKH=0$, and $Ky$ vanishes on the active span. The complete second equation is
$$
(\tau U)p_4^2-(\tau V')p_5^2=0.
$$
Since $K$ is invertible and the physical curve spans the ambient space, $p_4,p_5$ are linearly independent. A nontrivial relation between their squares would make their ratio constant. Hence $\tau U=\tau V'=0$. The zero-point coefficients of the complete mean equation now give $\tau(U^2)=\tau((V')^2)=0$.

The columns $U,V'$ must be independent, since rank at most one would put at least two active vectors in the radical in (1.2). At the active points, (1.3) gives $U_i^3=(V'_i)^3$. If $U_i=0$, both columns vanish at that coordinate and satisfy the same nonzero weighted linear equation in the other two coordinates, contradicting independence. Thus all $U_i\ne0$.

Let $r_i=V'_i/U_i\in\{1,\omega,\omega^2\}$. One root gives proportional columns. If exactly two roots occur, $\tau U=\tau V'=0$ separates the root blocks, and their singleton block cannot have zero weighted sum. Thus all three roots occur once. The two linear equations give $w_iU_i=tr_i$ for some $t\ne0$. The two square equations give
$\sum r_i/w_i=\sum r_i^2/w_i=0$, so all weights are $1/3$. Consequently
$$
U_i=3tr_i,\quad V'_i=3tr_i^2,\quad
P(U)=P(V')=27t^3/2\ne0.
$$
But (1.3) at $u_4,u_5$ gives $P(U)-k_{45}^3=0$ and $P(V')+k_{45}^3=0$. This contradiction excludes every isotropic active case.

## 4. Half-weight node derivatives force equal zero-point columns

It remains that $c=1/2$, $a+b=1/2$, $ab\ne0$, $k_{12}=0$. Now write
$$
k_{13}=p,\quad k_{23}=q,\quad
(k_{14},k_{24},k_{34})=(A,B,C),\quad
(k_{15},k_{25},k_{35})=(D,E,F),\quad k_{45}=G.
$$
Capital letters in this section are pairings, not the weight factors of Section 2.

All node equations used below come from one explicit polynomial. Let $\Lambda$ be the product moment functional with moments
$$
\mu_i=w_i,\quad\beta_i=w_i(w_i-\tfrac12),\quad
\gamma_i=w_i(w_i-1)(w_i-\tfrac12)\quad(i\le3),
$$
and $\mu_4=\mu_5=\beta_4=\beta_5=0$, $\gamma_4=1,\gamma_5=-1$. The original full potential restricted to these fixed physical nodes is
$$
Q_{\rm node}=\Lambda\left[\left(\sum_{i<j}k_{ij}X_iX_j\right)^3\right]. \tag{4.1}
$$
This is the original cumulant expansion; only moments through order three occur. The change from each node's original three cumulants to $(\mu,\beta,\gamma)$ is triangular with nonzero constant diagonal. Complete original criticality therefore forces all fifteen partial derivatives of (4.1) to vanish.

The derivatives in $\gamma_1,\gamma_2,\beta_1,\beta_2,\mu_1,\mu_2,\mu_3$, divided by nonzero constants, are
$$
\begin{gathered}
A^3=D^3,\qquad B^3=E^3,\\
-2b(A^2B-D^2E)-A^2C+D^2F=0,\\
2a(AB^2-DE^2)+B^2C-E^2F=0,\\
a(AB^2-DE^2)-ABC+DEF=0,\\
-2b(A^2B-D^2E)+2ABC-2DEF=0,\\
(A-B)^2C-(D-E)^2F=0.
\end{gathered} \tag{4.2}
$$
They follow by expanding the ten-edge cube (4.1). Only necessary equations are selected; no other original equation is waived.

If $A,B\ne0$, write $D=\rho A,E=\sigma B$, $\rho^3=\sigma^3=1$. A cube-root rescaling of $u_5$ makes $D=A,E=\omega B$. Suppose $\omega\ne1$. The middle equations of (4.2), with $r=a/b$, give
$$
A=-r\omega^2 B,\quad F=B(-a\omega^2+2b),\quad
C=B(-a\omega^2+2b\omega).
$$
The equation containing $B^2C-E^2F$ and the last equation then become respectively
$2r^2+r+2=0$ and $4r^2-r-2=0$. Subtracting the latter from twice the former gives $r=-2$, at which the first equals $8$. Thus $\rho=\sigma$, and the two second-moment node equations force $F=\rho C$.

If $A=0,B\ne0$, use $D=0$ and the $B^2$ equation to obtain the same proportionality; the symmetric case uses the $A^2$ equation. If $A=B=0$, then $D=E=0$, and (1.3) at $u_4$, using $P(0,0,C)=0$, gives $G=0$. The Gram matrix is then a star of rank at most two, impossible.

After rescaling $u_5$ by a cube root of unity, the entire two columns are equal. Equation (1.3) at $u_4,u_5$ gives
$$
(D,E,F)=(A,B,C),\quad G=0,\quad P(A,B,C)=0,\quad (A,B)\ne(0,0).
$$
The rank of $K|_E$ is the rank of
$$
\begin{pmatrix}0&0&p&A\\0&0&q&B\\p&q&0&C\\A&B&C&0\end{pmatrix},
$$
whose determinant is $(pB-qA)^2$. Hence $\Delta=pB-qA\ne0$.

## 5. The remaining derivative and zero multiplicity finish the exclusion

The active cubic factors exactly:
$$
P(X,Y,Z)=\frac{ab}{2}(X-Y)^2
[2(1-a)X+2(1-b)Y-3Z]. \tag{5.1}
$$
At $u_3$, (1.3) gives $(p-q)^2[(1-a)p+(1-b)q]=0$. At $G=0$, the $\beta_4$ derivative of (4.1), after removal of a nonzero scalar, is
$$
(A-B)\{p[(1-a)A+aB]-q[(1-b)B+bA]\}=0. \tag{5.2}
$$
Explicitly, its source is
$\Lambda[(AX_1+BX_2+CX_3)^2X_3(pX_1+qX_2)]$.
Here $\beta_3=\gamma_3=0$, so only $\mu_3=1/2$ remains; inserting $\beta_1=\beta_2=-ab$ and $\gamma_i=ab(1-w_i)$ gives (5.2) times $ab/2$.

If $p=q$, (5.2) gives $p(A-B)^2/2=0$, contradicting $\Delta\ne0$. Hence $(1-a)p+(1-b)q=0$. The braces in (5.2) equal
$\Delta+(A-B)[(1-a)p+(1-b)q]=\Delta$.
Therefore $A=B\ne0$ and $p\ne q$.

The binary quintic $h=p_5-p_4$ is nonzero: otherwise invertibility of $K$ and spanning of the curve would imply $u_5=u_4$. Equal columns and $G=0$ make $h$ vanish at all five distinct support points. Its five zeros are therefore simple. At the first active point $s_1$, $p_4(s_1)=p_5(s_1)\ne0$ (with a compatible homogeneous representative this value is $A$). Thus
$$
p_4^3-p_5^3=-h(p_4^2+p_4p_5+p_5^2)
$$
has zero order exactly one at $s_1$. But $p_1(s_1)=p_2(s_1)=0$ since $k_{11}=k_{12}=0$, and (5.1) gives zero order at least two for $P(p_1,p_2,p_3)$. This contradicts the full identity (1.3).

Binary forms and local zero orders include a point at infinity. Every half-weight case and every non-half-weight case has been excluded. The entire reduced five-point, rank-three-$H$ branch is empty. Nonreduced divisors, ranks four and five, inner mean and higher essential dimensions remain open; this result alone does not settle Bell nonvanishing or the Hilbert ISP.
