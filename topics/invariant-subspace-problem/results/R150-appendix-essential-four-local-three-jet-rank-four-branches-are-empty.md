# R150: every rank-four branch with a simple zero on a triple point is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved.** Under the original essential-four outer-mean length-five hypotheses, no complete critical point can have a simple zero of the same $L$ on a length-three local factor. The remaining length-two factor, on which $L$ is a unit, may be two distinct points or a double point. Both cases, including the reduced half-weight case, are excluded. A zero reduced point or a simple zero in a length-two factor is outside this statement.

## 1. Exact moments and allowed normalization

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), with
$$
\operatorname{rank}\operatorname{Cat}_{3\times4}(y)=3,\quad
\dim\operatorname{ess}(T_3)=4,\quad
y\notin\operatorname{ess}(T_3).
$$
The present case has
$$
\mathcal A=\mathbb C[t]/(t^3)\times\mathcal B,\qquad \dim\mathcal B=2.
$$
On the triple factor $L$ has a simple zero; on $\mathcal B$ it is a unit. First use $L$ as the local parameter on the triple factor, and divide the physical representative by $L$ on each unit factor. Thus $L=(t,1)$ and the active Frobenius functional $\tau$ on $\mathcal B$ satisfies $\tau(1)=1$, since $t^3=0$ on the other factor.

We may normalize the triple-factor functional to
$$
\nu_{\rm loc}(1)=\nu_{\rm loc}(t)=0,\qquad \nu_{\rm loc}(t^2)=1.
\tag{1.1}
$$
For completeness, start with highest value $q=\nu_{\rm loc}(t^2)\ne0$ and replace the local physical representative by $h(t)u(t)$, with
$$
h(t)=q(1+\eta_1t+\eta_2t^2),\qquad z=h(t)t.
$$
Keep the same covector $L$ and transform the functional by
$$
\widetilde\nu(f(z))=\nu\bigl(h(t)^{-3}f(h(t)t)\bigr).
\tag{1.2}
$$
Then $\widetilde\nu(z^2)=q/q=1$,
$$
\widetilde\nu(z)=q^{-2}\nu\bigl(t-2\eta_1t^2\bigr),
$$
and
$$
\widetilde\nu(1)=q^{-3}\nu\bigl(1-3\eta_1t+(6\eta_1^2-3\eta_2)t^2\bigr).
$$
Choose $\eta_1,\eta_2$ successively to kill these two lower values. Both are permitted invertible physical jet changes; (1.2) preserves the original $V,y,H$ because the three factors of $h$ cancel. Rename $z$ as $t$. No inverse of $L$ is used on the triple factor.

Let $u_0,u_1,u_2$ be its physical divided jets. For a covector $r$ put
$$
R=r(u_0),\quad S=r(u_1),\quad T=r(u_2).
$$
On the active factor let $X$ denote the restricted element of $\mathcal B$, and put $m=\tau(X)$. The exact original moments are
$$
y(r)=R+m,\qquad H(r,r)=\tfrac12RS+\tfrac14\tau(X^2),
$$
$$
V(r,r,r)=\tfrac38(R^2T+RS^2)+\tfrac18\tau(X^3).
\tag{1.3}
$$
Writing $P_{\mathcal B}(X)=\tau((X-m)^3)/2$ and $Z=S-m$, their complete cubic expands to
$$
T_3=P_{\mathcal B}(X)
+\tfrac32R\bigl[Z^2+m^2-\tau(X^2)\bigr]
+\tfrac32R^2(T-2Z)+R^3.
\tag{1.4}
$$

All subsequent equations are necessary coefficients of the unchanged complete gradients. We use the entire highest identity $T_3(Kv_{\rm hom}(s))=0$ and the original second-gradient tensor
$$
N=T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH,\qquad F=y^{\mathsf T}Ky/2.
\tag{1.5}
$$
Its pullback to the physical curve vanishes identically. In particular $T_{3,Ky}$ is one third of the directional derivative of the displayed cubic.

We also use the nonunit mean formula
$$
e_L-2L D_Ld-2d^2+4FLd=0,
\tag{1.6}
$$
where
$$
d(t)=\nu_s(L(s)^2k(t,s)),\quad
D_Lf(t)=\nu_s(L(s)k(t,s)f(s)),\quad
e_L(t)=\nu_s(L(s)k(t,s)^2).
$$
Its full derivation is given in [the rank-four quadruple-point exclusion](R150-appendix-essential-four-local-four-jet-rank-four-branch-is-empty.md), Section 2. It follows from the unchanged complete mean equation after $\mathcal Q_{F_0^2}=0$, by multiplying by the inverse of the nondegenerate Frobenius pairing of $\nu$. It never divides by $L$.

For the physical triple jets put
$$
A=K(u_0,u_2),\qquad K(u_1,u_1)=-2A.
\tag{1.7}
$$
The latter identity, as well as $K(u_0,u_0)=K(u_0,u_1)=0$, is a coefficient of the original isotropy $K(u(s),u(s))=0$.

## 2. A reduced active factor with non-half weights

Suppose $\mathcal B=\mathbb C^2$, supported at distinct points $v,w$ different from the triple base. Normalize $L(v)=L(w)=1$, and write the two nonzero weights as $a,b$, with $a+b=1$. Use $X=r(v)$ and $Y=r(w)$ in this section. Then
$$
m=aX+bY,\qquad m^2-\tau(X^2)=-ab(X-Y)^2,
$$
$$
P_{\mathcal B}=\tfrac{ab(b-a)}2(X-Y)^3.
\tag{2.1}
$$
Assume first $a\ne b$.

Let $c=K(u_0,v)$ and $d=K(u_0,w)$. At the triple base, $R=S=0$, so the highest identity gives $P_{\mathcal B}(c,d)=0$. Thus $c=d$. The constant coefficient of the mean equation (1.6) on the triple factor is
$$
ac^2+bd^2=2(ac+bd)^2.
\tag{2.2}
$$
Indeed its $L$ terms vanish at the base, and the local contribution to $e_L$ has zero constant coefficient. With $c=d$, (2.2) forces $c=d=0$.

At either of the two active points, $R=0$, and the active cubic in (2.1) is a nonzero constant times the cube of their mutual pairing. Hence
$$
k:=K(v,w)=0.
\tag{2.3}
$$
All pairings among $u_0,v,w$ vanish.

Now let $e=K(u_1,v)$, $f=K(u_1,w)$, $n=ae+bf$, and $\ell=aK(u_2,v)+bK(u_2,w)$. With (2.3), $F=0$, the active components of the polar mean are zero, and its local component is
$$
d_{\rm loc}=nt+(A+\ell)t^2.
$$
The local $t^2$ coefficient of (1.6) is exactly
$$
ae^2+bf^2=2n^2.
\tag{2.4}
$$
To verify it directly, $k_0(t)=K(u(t),u_0)=At^2$ and $k_1(t)=K(u(t),u_1)=-2At+O(t^2)$. The local contribution $2k_0k_1$ to $e_L$ is zero modulo $t^3$, whereas the active part is $(ae^2+bf^2)t^2$. Also $D_Ld=Ant^2$, so $L D_Ld=0$, and $d^2=n^2t^2$.

In the physical curve parameter $s$ at the triple base, the active polars begin $es,fs$. The order-three coefficient of (1.4) is solely the active cubic:
$$
\tfrac{ab(b-a)}2(e-f)^3.
$$
Every other term has order at least four, because $R$ has order at least two, while $Z$ and the active difference have order at least one. Hence $e=f$, and (2.4) then forces $e=f=0$.

The active polars now have order at least two. At the triple base,
$$
R=A s^2+O(s^3),\quad S=-2A s+O(s^2),\quad
T=A+O(s),\quad m=O(s^2).
$$
The order-four coefficient of (1.4) is
$$
\tfrac32 A(4A^2)+\tfrac32 A^3=\tfrac{15}{2}A^3.
$$
The active cubic and the $R(X-Y)^2$ term start at order at least six, and the remaining displayed corrections start at order at least five. Thus $A=0$.

The physical space $\operatorname{span}\{u_0,u_1,v\}$ is therefore a totally isotropic length-three jet space of type $2+1$. This is forbidden by [the complete isotropic-length-three classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md), Sections 3–5, including infinity. Every reduced non-half-weight case is excluded.

## 3. The active factor is a double point

Now $\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)$. Its nondegenerate functional can be normalized to $\tau(1)=\tau(\epsilon)=1$ by scaling the local parameter. Let $v_0,v_1$ be the resulting physical base and first jet. In its coordinates $(X,Y)$,
$$
\tau(X+Y\epsilon)=X+Y,\qquad
P_{\mathcal B}(X,Y)=Y^3.
\tag{3.1}
$$
Put $c=K(u_0,v_0)$, $d=K(u_0,v_1)$. The highest identity at the triple base forces $d=0$. The constant mean equation there is
$$
c^2+2cd=2(c+d)^2,
$$
so $c=0$ as well. Hence $u_0$ is orthogonal to both active jets.

The active Gram matrix has the form
$$
K_a=\begin{pmatrix}0&0\\0&h\end{pmatrix}
$$
by physical curve isotropy. The active polar mean is $d_a=(0,h)$ and $F=h/2$, since the base cross column is zero. In the active algebra, the contribution of the triple factor to $e_L$ is $2K(u_0,\cdot)K(u_1,\cdot)=0$, and its contribution to $D_Ld$ is also zero: both the constant cross value and the constant local polar mean vanish. The remaining unit-factor calculations are
$$
e_L=0,\qquad D_Ld=0,\qquad d_a^2=0,\qquad
4F d_a=(0,2h^2).
$$
Thus (1.6) forces $h=0$.

The original physical space $\operatorname{span}\{v_0,v_1,u_0\}$ is now totally isotropic of type $2+1$, again impossible. This excludes the entire divisor type $3+2$ with the simple zero on its triple factor.

## 4. Reduced active half weights: full preliminary equations

It remains that the two active points $v,w$ have $a=b=1/2$. Keep $X=r(v)$ and $Y=r(w)$, and put
$$
c=K(u_0,v),\quad d=K(u_0,w),\quad
e=K(u_1,v),\quad f=K(u_1,w),
$$
$$
g=K(u_2,v),\quad h=K(u_2,w),\quad k=K(v,w).
$$
Here $h$ is a cross pairing, not the active tangent pairing of Section 3.

Equation (1.4) factors exactly as
$$
T_3=\tfrac32R Q,
$$
$$
Q=(S-X)(S-Y)+R(T-2S+X+Y)+\tfrac23R^2.
\tag{4.1}
$$
The physical polar $R$ is nonzero. The full highest identity therefore yields the entire binary quadratic pullback identity $Q=0$.

Write
$$
m_0=(c+d)/2,\qquad n=(e+f)/2,\qquad \ell=(g+h)/2.
$$
The original polar mean and scalar are
$$
d_{\rm loc}=m_0+nt+(A+\ell)t^2,\quad
d_v=c+k/2,\quad d_w=d+k/2,\quad
F=m_0+k/4.
\tag{4.2}
$$
The local constant coefficient of (1.6) is $-cd$, so
$$
cd=0.
\tag{4.3}
$$
At either active point, that mean equation is
$$
-cf-de+2cd=0.
\tag{4.4}
$$
For an explicit check at $v$, its components are
$$
e_L=2ce+k^2/2,\qquad
D_Ld=cn+em_0+kd/2+k^2/4,
$$
$$
d_v=c+k/2,\qquad F=m_0+k/4.
$$
Substitution into $e_L-2D_Ld-2d_v^2+4Fd_v$ gives (4.4) exactly. The other point is symmetric.

The linear physical coefficient of $Q$ at the triple base is
$$
2A(c+d)+ed+fc=0.
\tag{4.5}
$$
Here $R$ has no constant or linear term, $S=-2As+O(s^2)$, and the active polars are $c+es+\cdots$, $d+fs+\cdots$.

Combining (4.3)–(4.5) gives
$$
cf+de=0,\qquad A(c+d)=0.
\tag{4.6}
$$
If $c\ne0$, then $d=f=A=0$. The physical space $\operatorname{span}\{u_0,u_1,w\}$ is a forbidden totally isotropic $2+1$ jet space. The case $d\ne0$ is symmetric. Consequently the only remaining possibility is
$$
c=d=0.
\tag{4.7}
$$

## 5. The unchanged second gradients close the half-weight case

Under (4.7), $m_0=0$, $F=k/4$, and the polar mean takes the values
$$
d_R=0,\quad d_S=n,\quad d_T=A+\ell,\quad d_X=d_Y=k/2.
$$
Using the exact factorization (4.1), its single symmetric contraction is
$$
T_{3,Ky}=
\tfrac12R\left[
(n-k/2)(2S-X-Y)+R(A+\ell-2n+k)
\right].
\tag{5.1}
$$
The other two terms in the original tensor $N$ are equally explicit:
$$
yy^{\mathsf T}-2H
=R^2+R(X+Y-S)+\tfrac12XY,
\tag{5.2}
$$
$$
4HKH=-\tfrac A2R^2+\tfrac14R(eX+fY)+\tfrac k8XY.
\tag{5.3}
$$
For (5.3), $4H$ sends $(R,S,T,X,Y)$ to the physical vector with coefficients $(S,R,0,X/2,Y/2)$; use $K_{11}=-2A$ and the zero base cross column.

Combining (5.1)–(5.3) gives the exact original form
$$
\boxed{
N=\tfrac R4\left[
(2(e+f)-k)S-fX-eY+
(g+h-2(e+f)+k)R
\right].
}
\tag{5.4}
$$
No coefficient has been discarded by a support restriction. The full eleven second-moment gradients say that the pullback of this form to the physical curve vanishes identically. Since $R$ is a nonzero binary quintic, the bracket must vanish identically.

The four physical vectors $u_0,u_1,v,w$ are independent, being the complete jets of a length-four divisor. The original $K$ is nondegenerate and the physical curve spans the ambient space, so their four polars $R,S,X,Y$ are independent. The coefficients in (5.4) therefore give
$$
e=f=k=0,\qquad g+h=0.
\tag{5.5}
$$
Finally, under (4.7) and (5.5), the local order-two coefficient of the highest quadratic identity $Q=0$ is
$$
4A^2+A^2=5A^2:
$$
the first term in (4.1) contributes $4A^2$, the $RT$ term contributes $A^2$, and every other term has higher order. Hence $A=0$.

Again $\operatorname{span}\{u_0,u_1,v\}$ is a totally isotropic original length-three jet space of type $2+1$, contrary to the complete classification. The reduced half-weight case is excluded.

## 6. Exhaustion and accurate scope

The unit factor of total length two is either reduced or a double point. Section 3 excludes the double-point case; Section 2 excludes all reduced non-half weights; Sections 4–5 exclude the reduced half weights. These exhaust the present canonical simple-zero-on-a-triple-point branch.

All calculations used local representatives of the original curve, its unchanged form $K$, and exact necessary consequences of the original complete gradients. The normalizations preserved the same $L$ and all moments by (1.2), and no support point at infinity was omitted. Thus every rank-four branch with a nonunit local block of length three is empty.

The remaining rank-four types have a simple zero on a block of length two, or have $L=0$ on an entire reduced point and a unit on the remaining length four. Rank five and the other essential-space branches remain separate. This exclusion by itself is not a matched Bell radical certificate and does not settle the Hilbert ISP.
