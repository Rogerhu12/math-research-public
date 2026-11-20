# R150: every rank-three second moment in the essential-four outer-mean branch is excluded

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** Under the hypotheses of the original length-five reduction, a complete critical point has $\operatorname{rank}H\ge4$. This includes every nonreduced length-five divisor and points at infinity. The reduced five-point case was proved separately; the present proof supplies all remaining jet cases. It does not settle ranks four or five, the inner-mean case, higher essential dimensions, Bell radical membership or the Hilbert ISP.

## 1. Exact scope and unchanged original equations

Use [the length-five algebra and rank-defect reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), with the original nondegenerate six-dimensional form $K$, the original rational normal quintic, and
$$
\operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\qquad
W=\operatorname{ess}(T_3),\qquad \dim W=4,\qquad y\notin W.
\tag{1.1}
$$
That proof gives a unique original length-five divisor $D$, a five-dimensional support $E_D$, and a Frobenius algebra $\mathcal A$ with the same element $L$ determined by the outer mean.

Suppose $\operatorname{rank}H=3$. Section 4 of that reduction gives the exact product decomposition
$$
\mathcal A=\mathcal B\times\mathcal C,\qquad
\dim\mathcal B=3,\quad \dim\mathcal C=2,
$$
where $L$ is a unit on $\mathcal B$ and identically zero on $\mathcal C$. On the active factor divide the local physical curve representative by that unit and put $\tau(f)=\nu(L^3f)$. Thus $\tau(1)=1$, its Frobenius pairing is nondegenerate, and
$$
y(r)=\tau(X_r),\qquad H(r,r)=\tfrac14\tau(X_r^2),\qquad
V_{\rm act}(r,r,r)=\tfrac18\tau(X_r^3).
\tag{1.2}
$$
The complete active cubic is
$$
P(X)=\tfrac12\tau\bigl((X-\tau(X))^3\bigr).
\tag{1.3}
$$
Multiplication by a local unit and invertible local parameter changes preserve the original jet span and all zero orders. In these normalized local representatives $\lambda$ is the constant function one on $\mathcal B$ and zero on $\mathcal C$. We never change the original $K$.

The two possible zero factors admit the following normalizations:
$$
T_3=P+R^3-S^3\quad(\mathcal C\simeq\mathbb C^2),
\qquad
T_3=P+R^2S\quad(\mathcal C\simeq\mathbb C[\epsilon]/(\epsilon^2)).
\tag{1.4}
$$
For the first, rescale the two nonzero cubic coefficients. For the second, the top local functional is nonzero, so a triangular change of the physical base and first jet absorbs the constant-cubic term and normalizes the coefficient of $R^2S$. Write the zero-double basis as $w_0,w_1$, with $w_1$ a nonzero first jet modulo $w_0$. It retains
$$
K(w_0,w_0)=K(w_0,w_1)=0,\qquad K(w_1,w_1)=g.
\tag{1.5}
$$

For each physical basis vector $u$ use its binary quintic polar $p_u(z)=u^{\mathsf T}Kv_{\rm hom}(z)$. Independent vectors give independent polars because $K$ is invertible and the curve spans the ambient space. Since $\dim E_D=5$,
$$
\operatorname{rank}(K|_{E_D})\ge4:
\quad \operatorname{rad}(K|_{E_D})\subseteq E_D^{\perp_K},
\quad \dim E_D^{\perp_K}=1.
\tag{1.6}
$$

All equations below are necessary consequences of the unchanged complete gradients. We retain the entire highest binary identity $T_3(Kv_{\rm hom}(z))=0$. With $p=Ky$, $F=y^{\mathsf T}Ky/2$, the second-gradient tensor is
$$
N=T_{3,p}-F(yy^{\mathsf T}-2H)+4HKH,\qquad
N(Kv_{\rm hom}(z),Kv_{\rm hom}(z))=0.
\tag{1.7}
$$
The contraction $T_{3,p}$ is one symmetric tensor contraction, hence one third of the directional derivative of the cubic. Pairing the original complete mean equation with the same $\lambda$ gives $\mathcal Q_{F_0^2}=0$. Its remaining vector equation is
$$
-4FHp+8HKHp+4V(p,p,\cdot)-8V:(KHK)=0.
\tag{1.8}
$$
These formulas are the dimension-independent original identities of [the full low-gradient calculation](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md), Sections 2–3.

Here is a uniform active version of (1.8). Write $k(t,s)$ for the active physical Gram kernel in $\mathcal B\otimes\mathcal B$, set
$$
d(t)=\tau_s k(t,s),\quad
(Df)(t)=\tau_s(k(t,s)f(s)),\quad
e(t)=\tau_s(k(t,s)^2),\quad F=\tfrac12\tau(d).
$$
Then the active equation is exactly
$$
e-2Dd-2d^2+4Fd=0.
\tag{1.9}
$$
Indeed the Gram matrix $J$ of $\tau(XY)$ gives $H=J/4$ and $V_{\rm act}(p,p,\cdot)=J(d^2)/8$; (1.8) multiplied by $-4J^{-1}$ is (1.9). In particular, no restricted criticality has replaced the original gradients.

## 2. A local active triple point is impossible

Normalize $\mathcal B=\mathbb C[\epsilon]/(\epsilon^3)$ by
$$
\tau(1)=1,\qquad \tau(\epsilon)=0,\qquad \tau(\epsilon^2)=1.
$$
This is possible because the top value is nonzero: an invertible change $\epsilon\mapsto c\epsilon+d\epsilon^2$ first normalizes the top value and then kills the middle value. In the corresponding physical divided jets $u_0,u_1,u_2$, physical curve isotropy gives
$$
K_a=
\begin{pmatrix}0&0&A\\0&-2A&B\\A&B&C\end{pmatrix},
\qquad
J=\begin{pmatrix}1&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\tag{2.1}
$$
The relation $K_{11}+2K_{02}=0$ is the second coefficient of $K(u(t),u(t))=0$.

Now
$$
y=(1,0,1),\quad d=(A,B,A+C),\quad F=A+C/2,
$$
$$
D=K_aJ=
\begin{pmatrix}A&0&0\\ B&-2A&0\\ A+C&B&A\end{pmatrix},
\qquad e=(0,0,6A^2).
$$
Substitution in (1.9) gives
$$
AC=0,\qquad B(A+C)=0,\qquad A^2-AC+C^2-2B^2=0.
\tag{2.2}
$$
If $A=0$, the latter two imply $B=C=0$; if $C=0$, they imply $A=B=0$. Hence $K_a=0$. This would make the original length-three local jet space totally isotropic. The [complete classification of isotropic length-three curve jets](R150-appendix-classification-of-isotropic-length-three-curve-jets.md), Sections 3–5, excludes every nonreduced such divisor, including infinity. Thus this active type is impossible for either zero factor.

## 3. Exact mean classification for an active double point and a simple point

Let
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\times\mathbb C,\qquad
\tau(1_{\rm dbl})=a,\quad \tau(\epsilon)=1,\quad \tau(1_{\rm pt})=b,
\quad a+b=1,\quad b\ne0.
$$
Here $a$ may be zero. The physical basis is $u_0,u_1$ at the double point and $u_2$ at the distinct simple point. Put
$$
K_a=\begin{pmatrix}0&0&x\\0&h&z\\x&z&0\end{pmatrix},\qquad
J=\begin{pmatrix}a&1&0\\1&0&0\\0&0&b\end{pmatrix}.
\tag{3.1}
$$
Then
$$
d=(bx,h+bz,ax+z),\quad F=abx+bz+h/2,
$$
$$
D=K_aJ=\begin{pmatrix}0&0&bx\\h&0&bz\\ax+z&x&0\end{pmatrix},
\quad e=(bx^2,2bxz,ax^2+2xz).
$$
Set $\delta=1-2b=a-b$. The constant, simple-point and $\epsilon$ coefficients of (1.9) are respectively $-bf_1,-f_2,-2f_3$, where
$$
\begin{aligned}
f_1={}&x(\delta^2x-2h+2\delta z),\\
f_2={}&a\delta^2x^2+2\delta^2xz+2bxh+2\delta z^2-2hz,\\
f_3={}&b(1+2b)xh-b^2\delta xz+b\delta z^2-3bhz-h^2.
\end{aligned}
\tag{3.2}
$$

This system has only the following possibilities:
$$
K_a=0,\qquad\text{or}\qquad b=a=\tfrac12,\ h=0.
\tag{3.3}
$$
To prove the assertion, first suppose $x=0$. Then $f_2=2z(\delta z-h)$. If $z=0$, $f_3=-h^2$ gives $h=0$. If $z\ne0$, put $h=\delta z$; then $f_3=-\delta z^2$, since $2b+\delta=1$. Thus $\delta=h=0$.

If $x\ne0$ and $\delta\ne0$, $f_1=0$ gives $h=\delta z+\delta^2x/2$. After this substitution $f_2$ is exactly $\delta x(\delta x+z)$. Hence
$$
z=-\delta x,\qquad h=-\delta^2x/2,
$$
and $f_3$ becomes $-\delta^2x^2/4$, a contradiction. Finally $\delta=0$ makes $f_1=-2xh$; the cases just considered and $x\ne0$ give $h=0$. This proves (3.3).

The $K_a=0$ alternative would be a totally isotropic physical length-three jet space of type $2+1$, again excluded by the same classification. Consequently only the half-weight alternative remains.

## 4. The active half-weight double-point normal form

For the remaining $a=b=1/2$, $h=0$ case, in active coordinates $(X,Y,Z)$ we have
$$
y=\tfrac12u_0+u_1+\tfrac12u_2,\qquad
H(X,Y,Z)=\tfrac18X^2+\tfrac12XY+\tfrac18Z^2,
$$
$$
V_{\rm act}(X,Y,Z)=\tfrac1{16}X^3+\tfrac38X^2Y+\tfrac1{16}Z^3,
$$
$$
P(X,Y,Z)=Y^2\left[Y-\tfrac32(X-Z)\right],\qquad
K_a=\begin{pmatrix}0&0&x\\0&0&z\\x&z&0\end{pmatrix}.
\tag{4.1}
$$
Here $F=x/4+z/2$. Direct substitution in (1.7) gives the exact active second-gradient form
$$
N_a(X,Y,Z)=\tfrac{2z-x}{4}Y^2-\tfrac z2XY.
\tag{4.2}
$$
In particular it is independent of $Z$.

Let $p_0,p_1,p_2$ be the three active quintic polars. At the active double base, both $p_0$ and $p_1$ vanish to order at least two, because $K_{00}=K_{01}=K_{11}=0$. Thus $P(p_0,p_1,p_2)$ and $N_a(p_0,p_1,p_2)$ vanish there to order at least four.

If $N_a(p_0,p_1,p_2)$ vanishes identically, independence of $p_0,p_1$ forces $x=z=0$. Indeed its displayed factorization first gives the linear factor identically zero, then both coefficients zero. This would be the forbidden isotropic $2+1$ space.

## 5. Half-weight active double point with two reduced zero points

Write the zero polars as $R,S$, with $T_3=P+R^3-S^3$. Let their cross columns against the active basis be
$$
U=(A,B,C),\qquad V=(D,E,F_1),\qquad G=K(w_3,w_4).
$$
Set
$$
d_3=A/2+B+C/2,\qquad d_4=D/2+E+F_1/2.
$$
The full second-gradient identity is
$$
N_a(p_0,p_1,p_2)+d_3R^2-d_4S^2=0.
\tag{5.1}
$$
The highest identity at the active double base and its first jet gives
$$
A^3=D^3,\qquad A^2B=D^2E.
\tag{5.2}
$$
If $A\ne0$, write $D=\rho A$ with $\rho^3=1$; then $E=\rho B$. Equation (5.1) at the base gives $d_4=\rho d_3$, hence $F_1=\rho C$.

If $A=0$, then $D=0$. The active cubic has zero order at least four, so the order-three coefficient of the highest identity gives $B^3=E^3$. If $B\ne0$, write $E=\rho B$; the order-two coefficient of (5.1) gives $d_4=\rho d_3$, hence again $F_1=\rho C$. If $B=0$, then $E=0$. Evaluating the highest identity at a zero point gives $G=0$ because $P(0,0,C)=0$. The Gram matrix is then a star, of rank at most two, contradicting (1.6).

Thus a cube-root rescaling of the second zero point makes the columns equal. The highest identities at the two zero points now give
$$
U=V,\qquad G=0,\qquad P(A,B,C)=0.
\tag{5.3}
$$
The Gram rank is the rank of
$$
\begin{pmatrix}
0&0&x&A\\0&0&z&B\\x&z&0&C\\A&B&C&0
\end{pmatrix},
$$
whose determinant is $(xB-zA)^2$. Therefore $xB-zA\ne0$.

The nonzero binary quintic $S-R$ vanishes on the entire length-five divisor: twice at the active double point and once at each of the other three points. Its order at the double point is exactly two. If $A\ne0$, the difference $R^3-S^3$ then has order exactly two, because its other factor has nonzero value $3A^2$. This contradicts the order at least four of the active cubic. Hence $A=0$, so $B\ne0$ and $x\ne0$.

Equation (5.3) now gives $C=-2B/3$. The highest identity at the active simple point gives
$$
z^2(z-3x/2)=0.
$$
Equation (5.1) at either zero point gives $(2z-x)B^2/4=0$, hence $z=x/2$. These conditions contradict $x\ne0$. This entire support type is excluded.

## 6. Universal equations for a zero double point

For the rest of the proof the zero factor is a double point, normalized to $T_3=P+R^2S$ as in (1.4). Write its active cross columns as $U,V$ in the algebra $\mathcal B$ and put
$$
d_0=\tau(U),\qquad d_1=\tau(V).
$$
The exact zero contribution to $N$ is
$$
N_{\rm zero}=\tfrac13(2d_0RS+d_1R^2).
\tag{6.1}
$$
The two zero coefficients of the complete mean equation (1.8) give
$$
\boxed{\tau(U^2)=2d_0^2,\qquad \tau(UV)=2d_0d_1.}
\tag{6.2}
$$
For example, $V_{\rm zero}=R^2S/4$ has symmetric coefficient $1/12$ in the $w_0,w_0,w_1$ slots. Its $w_1$ mean coefficient is $d_0^2/3-\tau(U^2)/6$; its $w_0$ coefficient is $2d_0d_1/3-\tau(UV)/3$. These are precisely (6.2).

Every case with $K_a=0$ is impossible. Indeed then $F=HKH=0$, the active polar mean is zero, and $N_a=0$. Equation (6.1) on the curve factors as
$$
R(2d_0S+d_1R)=0.
$$
The two independent nonzero polars force $d_0=d_1=0$. Equation (6.2) now gives
$$
U,V\in\ker\tau,\qquad \tau(U^2)=\tau(UV)=0.
$$
Because $\tau(1)=1$ and the full Frobenius pairing is nondegenerate, its restriction to the two-dimensional space $\ker\tau$ is nondegenerate. If $U\ne0$, its isotropy makes its orthogonal complement in that plane exactly $\mathbb CU$, so $V$ is proportional to $U$. If $U=0$, the two-column cross matrix also has rank at most one. In either case at least two active vectors lie in the radical of $K|_{E_D}$, contrary to (1.6). This argument covers all active algebra types.

## 7. Half-weight active double point with a zero double point

Use (4.1)–(4.2) and write
$$
U=(A,B,C),\quad V=(D,E,F_1),\quad
d_0=A/2+B+C/2,\quad d_1=D/2+E+F_1/2.
$$
Expanding (6.2) in $\mathbb C[\epsilon]/(\epsilon^2)\times\mathbb C$ gives exactly
$$
C(A+2B)+2B^2=0,
$$
$$
F_1(A+2B)+DC+2E(C+2B)=0.
\tag{7.1}
$$

Suppose $A\ne0$. The highest identity at the active double base and its first jet gives
$$
A^2D=0,\qquad 2ABD+A^2E=0,
$$
so $D=E=0$. The second-gradient identity there gives $d_1=0$, hence $F_1=0$. If $d_0\ne0$, (6.1) and the order at least four of $N_a$ force $S$ to have order at least four at the active double base, where $R=A\ne0$. But $S$ also vanishes at the active simple point ($F_1=0$) and at the zero double base ($K(w_1,w_0)=0$). These are distinct points and total at least six zeros of a nonzero binary quintic. This is impossible. Hence $d_0=0$, making $N_a$ vanish identically; Section 4 excludes that possibility.

Now $A=0$. If $B\ne0$, the first equation of (7.1) gives $C=-B$. At the zero double base $R=S=0$, so the highest equation would require
$$
0=P(0,B,-B)=-B^3/2,
$$
a contradiction. Hence $A=B=0$.

If $C\ne0$, the second equation of (7.1) gives $D+2E=0$. In a local representative at the zero base, the active polars have first terms
$$
p_0=Dt+O(t^2),\quad p_1=Et+O(t^2),\quad p_2=C+O(t).
$$
Here $R$ has order at least two and $S$ at least one, by (1.5), so $R^2S$ has order at least five. The order-two coefficient of the active cubic is $3CE^2/2$, whence $E=D=0$. The Gram matrix in $(u_0,u_1,u_2,w_0,w_1)$ is now
$$
\begin{pmatrix}
0&0&x&0&0\\0&0&z&0&0\\x&z&0&C&F_1\\
0&0&C&0&0\\0&0&F_1&0&g
\end{pmatrix}.
$$
It is a star plus one diagonal entry and has rank at most three, contradicting (1.6).

Finally, if $A=B=C=0$, the three vectors $u_0,u_1,w_0$ form a totally isotropic original length-three jet space of type $2+1$: $K_{00}=K_{01}=K_{11}=0$, and $w_0$ is orthogonal to both. The complete isotropic-jet classification again excludes it. This finishes every active nonreduced case.

## 8. Active three reduced points with a zero double point

It remains that the active algebra is $\mathbb C^3$. Its weights $a,b,c$ are nonzero and sum to one. Section 2 of [the reduced-five-point exclusion](R150-appendix-essential-four-reduced-five-point-rank-three-branch-is-empty.md) used only the active mean equation (1.9); its proof is independent of the zero factor. It therefore applies here verbatim. It says that $K_a=0$ unless one weight is $1/2$; with that weight labeled $c=1/2$, it forces $K(u_1,u_2)=0$.

Section 6 already excludes $K_a=0$. Thus put
$$
c=\tfrac12,\quad a+b=\tfrac12,\quad ab\ne0,\quad
K_a=\begin{pmatrix}0&0&p\\0&0&q\\p&q&0\end{pmatrix}.
$$
Set $\alpha=1-a,\ \beta=1-b$. The exact active forms are
$$
P(X,Y,Z)=\tfrac{ab}{2}(X-Y)^2(2\alpha X+2\beta Y-3Z),
$$
$$
N_a(X,Y,Z)=\tfrac{ab}{2}(X-Y)
\{p(\alpha X+aY)-q(bX+\beta Y)\}.
\tag{8.1}
$$
The second follows by substituting the same moments into (1.7). In particular, if its pullback by the first two independent polars vanishes identically, then
$$
\alpha p-bq=0,\qquad ap-\beta q=0.
$$
Their determinant is $-\alpha\beta+ab=-1/2$, so $p=q=0$, which Section 6 excludes.

Write the cross columns and means as
$$
U=(A,B,C),\quad V=(D,E,F_1),\qquad
d_0=aA+bB+C/2,\quad d_1=aD+bE+F_1/2.
$$
At the first two active points the active forms in (8.1) vanish. The highest and second identities give
$$
A^2D=B^2E=0,\qquad
2d_0AD+d_1A^2=2d_0BE+d_1B^2=0.
\tag{8.2}
$$

### 8.1 Both $A$ and $B$ are nonzero

Then $D=E=0$ and $d_1=0$, hence $F_1=0$. If $d_0\ne0$, at each of the first two active points $N_a$ vanishes to order at least two, because both of its first two polar arguments vanish there. Since $R$ is nonzero there, (6.1) forces $S$ to have a double zero at each. It also vanishes at the third active point and at the zero double base. This gives at least six zeros, impossible for its nonzero degree five. Thus $d_0=0$, so $N_a$ vanishes identically, already excluded.

### 8.2 Exactly one of $A,B$ is nonzero

By interchanging the first two active points suppose $A\ne0$, $B=0$. Equations (8.2) give $D=0,d_1=0$, and hence $F_1=-2bE$. The mixed equation in (6.2) gives $CE=0$. If $E\ne0$, then $C=0$; the first equation in (6.2) becomes $aA^2=2a^2A^2$, forcing $a=1/2$ and $b=0$, impossible. Hence $E=F_1=0$.

The first equation of (6.2) now gives $C=bA$. The highest equation at the zero double base gives
$$
0=P(A,0,bA)=\tfrac{ab}{2}A^3(1-b),
$$
hence $b=1,a=-1/2$. Therefore $d_0=aA+C/2=0$. Again $N_a$ vanishes identically, a contradiction.

### 8.3 $A=B=0$

The mixed equation of (6.2) becomes
$$
C(aD+bE)=0.
\tag{8.3}
$$
At the zero double base, the first two active polars start as $Dt,Et$ and the third has value $C$. As before $R^2S$ has order at least five. The order-two coefficient of $P$ is $-3abC(D-E)^2/2$.

If $C\ne0$, it follows that $D=E$; (8.3) and $a+b=1/2$ give $D=E=0$. The Gram matrix is again a star centered on the third active vector plus the single diagonal entry $g$, of rank at most three, impossible. Thus $C=0$.

Now $w_0$ is orthogonal to all of $E_D$, and $d_0=0$. If $d_1=0$, the second identity forces $N_a$ to vanish identically, already excluded. If $d_1\ne0$, that identity gives
$$
R^2=-\tfrac3{d_1}N_a(p_1,p_2,p_3),
\tag{8.4}
$$
a quadratic expression in $p_1,p_2$ alone. The three distinct physical points $u_1,u_2,w_0$ are pairwise orthogonal. Their span is therefore one of the two reduced isotropic spaces $W_+$ or $W_-$, by the full isotropic-jet classification. The explicit conic lemma below shows that (8.4) is impossible. This excludes the last rank-three case.

## 9. The physical conics do not split off a squared point coordinate

**Lemma.** Let $r,s,t$ be the three roots of either
$$
P_+(z)=z^3-5z^2+\tfrac{32}{5}z-\tfrac85,\qquad
P_-(z)=z^3+27z^2+\tfrac{864}{5}z+\tfrac{864}{5}.
$$
For their three physical polars, no identity expresses the square of the $t$-polar as a quadratic expression in just the other two. Independent nonzero rescaling of the three representatives does not affect this assertion.

Use Sections 2–3 of [the isotropic-three-plane moment sections](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md). In its canonical basis,
$$
v(u)=E_\pm\lambda_u,\quad \lambda_u=(1,u,u^2)^{\mathsf T}\quad(P_\pm(u)=0),
$$
$$
E_\pm^{\mathsf T}Kv(z)=P_\pm(z)\psi_\pm(z).
$$
The unique quadratic relation of the nonsingular projected conic is $\psi^{\mathsf T}C_\pm\psi=0$, with
$$
C_+=\begin{pmatrix}279&121&608\\121&-521&-608\\608&-608&-1024\end{pmatrix},
\quad
C_-=\begin{pmatrix}-1769&1369&5024\\1369&-969&-5024\\5024&-5024&-1024\end{pmatrix},
$$
and $\det C_\pm=163840000\ne0$.

Put $B=(\lambda_r,\lambda_s,\lambda_t)$. It is invertible because the roots are distinct. After removing their common factor $P_\pm(z)$, the three physical polar coordinates are $B^{\mathsf T}\psi$. Their conic matrix is $B^{-1}C_\pm B^{-{\mathsf T}}$, whose inverse is $B^{\mathsf T}C_\pm^{-1}B$.

If the third coordinate square were a quadratic in the first two, uniqueness of the conic relation would make its matrix block diagonal between the third coordinate and the first two. Its inverse would have the same block decomposition. Therefore
$$
\lambda_r^{\mathsf T}C_\pm^{-1}\lambda_t
=\lambda_s^{\mathsf T}C_\pm^{-1}\lambda_t=0.
\tag{9.1}
$$
Write $P(z)=z^3-Sz^2+P_2z-Q$. The common annihilator of $\lambda_r,\lambda_s$ is spanned by
$$
\ell(t)=(rs,-(r+s),1)^{\mathsf T}
=(t^2-St+P_2,\ t-S,\ 1)^{\mathsf T}.
$$
Thus (9.1) requires $\lambda_t$ to be proportional to $C_\pm\ell(t)$. In particular
$$
(C_\pm\,5\ell(t))_1-t(C_\pm\,5\ell(t))_0=0.
\tag{9.2}
$$

All that remains is a small explicit remainder computation. For the plus case the first two components of $C_+5\ell(t)$ are
$$
1395t^2-6370t+8943,\qquad 605t^2-5630t+13857.
$$
Their combination in (9.2), reduced modulo $5P_+(t)$, is
$$
-5645t+11625.
$$
Hence a common root would be $t=2325/1129$ in lowest terms. This cannot be a root of the integer polynomial $5P_+$, since its denominator does not divide the leading coefficient $5$.

For the minus case the corresponding components are
$$
-8845t^2-231970t-1318481,\qquad
6845t^2+179970t+1026881,
$$
and the remainder modulo $5P_-(t)$ is
$$
-29965t-501535.
$$
A common root would therefore be $t=-100307/5993$ in lowest terms, again impossible by the rational-root denominator condition. This proves the lemma for every ordering of the three points. The earlier classification already excludes infinity from either isotropic triple.

## 10. Exhaustion and remaining scope

The active length-three algebra has exactly three partitions: $3$, $2+1$, or $1+1+1$. Its disjoint zero length-two algebra has exactly two: $2$ or $1+1$.

Section 2 excludes the active triple for either zero type. Sections 3–7 exclude active $2+1$ for both zero types. For three reduced active points and two reduced zero points, the entire case is the already proved [reduced-five-point exclusion](R150-appendix-essential-four-reduced-five-point-rank-three-branch-is-empty.md). Sections 6, 8 and 9 exclude three reduced active points with a zero double point. These six combinations exhaust the canonical rank-three alternative.

All counting used binary quintic divisors and local zero orders, so the argument includes any original support point at infinity. We conclude
$$
\boxed{\text{Under (1.1), every complete original critical point satisfies }
\operatorname{rank}H\in\{4,5\}.}
$$
This is a complete exclusion of one singular-second-moment branch of the canonical length-five problem. The remaining rank-four and rank-five branches, the inner-mean branch and higher essential dimensions still require the unchanged complete gradients and matched Bell analysis.
