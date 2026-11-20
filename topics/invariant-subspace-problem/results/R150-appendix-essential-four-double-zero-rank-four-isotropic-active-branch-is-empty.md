# R150: an isotropic active triple is impossible in the rank-four double-zero branch

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved restricted branch exclusion.** In the original essential-four outer-mean rank-four case where the same $L$ has a simple zero on a length-two factor, its complementary unit length-three support cannot be totally isotropic for the original $K$. The case with a nonzero active Gram form remains open.

## 1. The same double factor and exact equations

Use [the original length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md). The present algebra is
$$
\mathcal A=\mathcal B\times\mathbb C[\epsilon]/(\epsilon^2),\qquad \dim\mathcal B=3,
$$
with $L$ a unit on $\mathcal B$ and of order one on the double factor. Normalize the unit factor by the same $L$, so its Frobenius functional $\tau$ satisfies $\tau(1)=1$.

On the double factor use $L$ as local parameter. A local physical rescaling and reparameterization normalizes its functional to $\nu(1)=0,\nu(\epsilon)=1$: if the original top value is $q\ne0$, use $h(\epsilon)=c(1+\eta\epsilon)$ with $c^2=q$, the parameter $z=h(\epsilon)\epsilon$, and the transformed functional $\widetilde\nu(f(z))=\nu(h^{-3}f(h\epsilon))$. Its top value is $q/c^2=1$, and the constant value is killed by the unique choice of $\eta$. This preserves the original $y,H,V$ and the same covector $L$.

Let $u_0,u_1$ be these double-point jets and write $R=r(u_0),S=r(u_1)$. For the active element $X$, set $m=\tau(X)$. The exact original moments and cubic are
$$
y(r)=m,\qquad H(r,r)=\tfrac14\bigl(\tau(X^2)+R^2\bigr),
$$
$$
V(r,r,r)=\tfrac18\tau(X^3)+\tfrac38R^2S,
$$
$$
T_3=P_\tau(X)+\tfrac32R^2(S-m),\qquad
P_\tau(X)=\tfrac12\tau((X-m)^3).
\tag{1.1}
$$
Physical curve isotropy gives $K(u_0,u_0)=K(u_0,u_1)=0$.

Let the two active cross columns be $U=K(u_0,\cdot)$ and $V_1=K(u_1,\cdot)$, regarded as elements of $\mathcal B$. Put
$$
d_0=\tau(U),\quad d_1=\tau(V_1),\quad
d=K_{\rm act}y,\quad F=\tfrac12\tau(d).
$$
The active part of the unchanged complete mean equation is
$$
E_{\rm act}+U^2-2d_0U=0,
\tag{1.2}
$$
where $E_{\rm act}=e-2Dd-2d^2+4Fd$ is the ordinary active unit-factor mean expression. Its double-factor coefficients are
$$
\tau(U^2)=2d_0^2,
$$
$$
\tau(UV_1)=\tau(Ud)-2Fd_0+2d_0d_1.
\tag{1.3}
$$
For a direct source, apply the general nonunit mean identity
$e_L-2L D_Ld-2d^2+4FLd=0$ to $L=(1,\epsilon)$. On the active factor the double contribution to $e_L$ is $U^2$ and that to $D_Ld$ is $d_0U$. On the double factor, $d=d_0+d_1\epsilon$, $e_L=\tau(U^2)+2\tau(UV_1)\epsilon$, and the constant coefficient of $D_Ld$ is $\tau(Ud)$. These give (1.2)–(1.3) exactly.

## 2. A totally isotropic active support must be one of the two reduced triples

Assume $K_{\rm act}=0$. The [complete isotropic-length-three classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md) says that the active divisor consists of the three distinct roots of exactly one of
$$
P_+(t)=t^3-5t^2+\tfrac{32}{5}t-\tfrac85,\qquad
P_-(t)=t^3+27t^2+\tfrac{864}{5}t+\tfrac{864}{5}.
$$
In particular the active algebra is reduced. Let its physical representatives be $v_1,v_2,v_3$, its nonzero weights $w_i$, and $\sum_iw_i=1$.

We also record that these two root sets are disjoint. Their integer polynomial difference is
$$
5P_--5P_+=8(20t^2+104t+109).
$$
The remainder of $5P_+$ modulo $20t^2+104t+109$ is $5399(t+1)/20$, whereas the latter quadratic has value $25$ at $t=-1$. Hence the two cubics have no common root.

Since $K_{\rm act}=0$, $d=F=E_{\rm act}=0$. Equation (1.2) is now the componentwise identity
$$
U_i^2=2d_0U_i\quad(i=1,2,3).
\tag{2.1}
$$

## 3. All possible cross columns are excluded

If $d_0=0$, (2.1) gives $U=0$. The active Gram block is zero and its two-column cross matrix $(U,V_1)$ has rank at most one. Thus at least two active vectors lie in the radical of $K|_{E_D}$. This contradicts its rank at least four: for a five-dimensional subspace of the original nondegenerate six-dimensional space, that radical has dimension at most one.

Now suppose $d_0\ne0$. Let $I$ be the nonzero index set of $U$. Equation (2.1) gives
$$
U_i=2d_0\ (i\in I),\qquad U_i=0\ (i\notin I),\qquad
\sum_{i\in I}w_i=\tfrac12.
\tag{3.1}
$$
Both $I$ and its complement are nonempty.

At an active physical point $v_i$ all three active polars vanish, because $K_{\rm act}=0$. Thus the unchanged highest identity (1.1) gives $U_i^2(V_1)_i=0$. Consequently
$$
(V_1)_i=0\quad(i\in I).
$$
The second equation of (1.3) reduces to $\tau(UV_1)=2d_0d_1$. Its left side is zero by the preceding vanishing. Hence $d_1=0$.

If $I$ has two elements, its complement is a singleton with nonzero weight. Since $\tau(V_1)=d_1=0$, the remaining entry of $V_1$ is also zero. The cross matrix again has rank at most one, contradicting the same Gram rank bound.

If $I$ has one element, $u_0$ is orthogonal to the other two active physical points. Those two points are also mutually orthogonal. The three distinct points consisting of them and the double base $u_0$ therefore form a totally isotropic reduced length-three divisor. By the complete classification they must be the roots of $P_+$ or $P_-$. The active triple was already one of these, and the two root sets are disjoint. Thus the new triple must be the same active root set, forcing the double base to equal its remaining active point. This contradicts the disjoint factors of the original divisor. A point at infinity is excluded as well by the same classification.

All alternatives have been exhausted. The complementary unit length-three support cannot be totally isotropic.

## 4. Accurate remaining scope

This proves an empty branch of the simple-zero-on-a-double-point rank-four problem, with all its original low moments retained. It does not assume that the active Gram form vanishes in general. The nonisotropic active case, a zero reduced point with unit length-four complement, and rank five remain open.
