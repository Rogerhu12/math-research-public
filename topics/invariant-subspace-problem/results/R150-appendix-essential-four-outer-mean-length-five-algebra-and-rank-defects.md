# R150: the essential-four outer-mean branch and its original length-five algebra

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved structural reduction; no Bell-nonzero exclusion is asserted.**
The reduction retains all original Hankel moments, all jets and the original form $K$. It covers singular second moments without dividing by a possibly nonunit element.

## 1. Original objects and exact hypotheses

Use the original six-dimensional space, $v(t)=(1,t,t^2,t^3,t^4,t^5)^{\mathsf T}$ and the original invertible symmetric $K$ in [the complete cubic Schur reduction](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md). The original moments are $y$, $H=(H_{i+j})$ and $V=(V_{i+j+k})$. Put
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)H(r,r)+4V(r,r,r),
\qquad M=H-\tfrac14yy^{\mathsf T}.
$$
Assume
$$
\operatorname{rank}(y_{i+j})_{0\le i\le2,\ 0\le j\le3}=3,\qquad
W=\operatorname{ess}(T_3),\quad\dim W=4,\qquad y\notin W. \tag{1.1}
$$
Support reduction does not yet require complete criticality. The unchanged original gradient equations are imposed in Section 6. The inner-mean case $y\in W$ and essential dimensions five and six are outside the conclusion.

## 2. Canonical common support and a unique original divisor

For a quadric $q(r)=r^{\mathsf T}Qr$ vanishing on the original rational normal curve, the dimension-independent identities in [the conormal reduction](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md), Sections 1–2, give
$$
\operatorname{span}\{Qy:q\in I_2(v)\}=\mathbb C^6,\qquad
\tfrac16q(\partial_r)T_3=-4MQy.
$$
Their hypotheses are exactly the rank-three condition on the mean. Since second derivatives of a cubic supported on $W$ lie in $W$, $\operatorname{Ran}M\subseteq W$. The full tensor identity is
$$
V(r,r,r)=\tfrac14T_3(r)+\tfrac18(y^{\mathsf T}r)^3
                 +\tfrac32(y^{\mathsf T}r)M(r,r). \tag{2.1}
$$
Thus $E=W\oplus\mathbb Cy$, of dimension five, supports $y,H,V$.

In fact $V$ has essential space exactly $E$. If a covector $\ell$ on $E$ gives $\partial_\ell V=0$, put $a=\ell(y)$. The coefficient of the square of the independent variable $y^{\mathsf T}r$ in this derivative is $3a/8$, so $a=0$. The remaining coefficients of the first and zeroth powers of that variable are $(3/2)\partial_\ell M$ and $(1/4)\partial_\ell T_3$. The latter vanishes only if $\ell|_W=0$, by the definition of essential space. Together with $\ell(y)=0$, this gives $\ell=0$. Consequently the first flattening has rank five; merging its repeated columns gives
$$
\operatorname{rank}(V_{i+n})_{0\le i\le5,\ 0\le n\le10}=5. \tag{2.2}
$$

Here is a finite apolar proof which needs no moment-extension assumption. Let $S=\mathbb C[X_0,X_1]$ and let $\Lambda:S_{15}\to\mathbb C$ take the original moment values $V_j$ on the monomials. Put
$$
I_k=\{g\in S_k:\Lambda(gS_{15-k})=0\},\qquad b_k=\dim S_k/I_k.
$$
The pairing gives $b_k=b_{15-k}$. Once $I_k\ne0$, the elementary two-shift inequality
$\dim(X_0I_k+X_1I_k)\ge\dim I_k+1$ implies $b_{k+1}\le b_k$. Let $a$ be the first nonzero annihilator degree. From (2.2), $b_5=5<6$, hence $a\le5$. Minimality and symmetry give $b_{a-1}=a=b_{16-a}$; moreover $b_a\le a$. Monotonicity therefore gives
$$
a\ge b_5=5\ge b_{16-a}=a.
$$
Thus $a=5$ and $\dim I_5=1$. Its generator $g$ defines a unique length-five divisor $D$ on $\mathbb P^1$.

Polynomial division and the Chinese remainder theorem express the original $\Lambda$, hence $V$, in the complete curve jets along $D$. Each highest local coefficient is nonzero: otherwise deleting one order at that block gives an annihilator of degree below five. Length-five jets impose five independent conditions on binary quintics, again by division in a chart avoiding the support. Their five curve vectors are independent and their span is exactly the flattening image $E$. We have proved
$$
E=E_D,\qquad \deg D=5, \qquad D\text{ is uniquely determined by the original }V. \tag{2.3}
$$
All multiplicity partitions and any original point at infinity are retained.

## 3. A faithful algebra, including nonunit normalization

Choose a projective chart avoiding the finite support of $D$. Set
$$
\mathcal A=\mathbb C[t]/(g(t))
       \simeq\prod_i\mathbb C[\varepsilon_i]/(\varepsilon_i^{n_i}),
\qquad \sum_i n_i=5.
$$
Let $u(t)$ be the original six-coordinate homogeneous curve vector in this chart. Its components form a basis of binary quintics; chart change alters only jet coordinates and invertible local coefficients, not the original tensors or $K$. Write $X_r=r^{\mathsf T}u(t)\bmod g$. The complete original jets give a functional $\nu$ such that
$$
V(r,r,r)=\tfrac18\nu(X_r^3).
$$
Its top value on each local block is nonzero. Thus $(X,Y)\mapsto\nu(XY)$ is nondegenerate: an element of local order $j$ pairs nontrivially with $\varepsilon^{n-1-j}$, and different blocks are orthogonal.

There is a unique covector $\lambda$ on $E$ annihilating $W$ and satisfying $\lambda(y)=1$. Extend it to the ambient space and set $L=X_\lambda\in\mathcal A$; different extensions have the same jets, so give the same $L$. Contracting (2.1) with this very $\lambda$ gives
$$
H=2V(\lambda,\cdot,\cdot),\qquad
y=8V(\lambda,\lambda,\cdot),\qquad
8V(\lambda,\lambda,\lambda)=1.
$$
Therefore, for every original covector $r$,
$$
\boxed{\nu(L^3)=1,\quad
y^{\mathsf T}r=\nu(L^2X_r),\quad
H(r,r)=\tfrac14\nu(LX_r^2),\quad
V(r,r,r)=\tfrac18\nu(X_r^3).} \tag{3.1}
$$
Let $\alpha(X)=\nu(L^2X)$, $\mathcal A_0=\ker\alpha$, and $\pi_L(X)=X-\alpha(X)L$. Since $\alpha(L)=1$, $\pi_L$ is a projection with kernel $\mathbb CL$. Expanding its cube yields the complete third moment
$$
\boxed{T_3(r)=\tfrac12\nu\bigl(\pi_L(X_r)^3\bigr).} \tag{3.2}
$$
The actual four-variable space is $\mathcal A/\mathbb CL$, represented by $\mathcal A_0$. No inverse of $L$ has been used.

## 4. Exhaustive second-moment rank defects

Since binary quintics map onto $\mathcal A$ and the Frobenius pairing is nondegenerate,
$$
\operatorname{rank}H=\operatorname{rank}m_L. \tag{4.1}
$$
The mean functional $\nu(L^2\cdot)$ is supported on a divisor of length $\operatorname{rank}m_{L^2}$. Blockwise, if $L$ has local order $k_i$, multiplying by $L^2$ deletes exactly $\min(2k_i,n_i)$ top moment orders. A support of length at most two would force the $3\times4$ mean catalecticant to have rank at most two. Thus $\operatorname{rank}m_{L^2}\ge3$.

Put $a=\sum_i\min(k_i,n_i)$ and $b=\sum_i\min(2k_i,n_i)$, with $k_i\ge n_i$ for a zero block. Then $a\le b\le2$ and $\operatorname{rank}H=5-a$. Exactly these cases remain:

| Rank of original $H$ | Exact defect of the same $L$ |
|---:|---|
| 5 | $L$ is a unit on every block. |
| 4 | $L$ vanishes at one reduced point, or has a simple zero in one block of length at least two; it is a unit on all other blocks. |
| 3 | $\mathcal A=\mathcal A_{\rm act}\times\mathcal A_{\rm zero}$ with lengths three and two; $L$ is a unit on the first factor and identically zero on the second. The length-two factor may be reduced or a double point. |

Indeed, rank three implies $a=b=2$. A proper positive local order $0<k_i<n_i$ would give $\min(2k_i,n_i)>k_i$, impossible. Thus all defects are entire zero blocks. Rank four gives one order-one defect and exactly the alternatives shown. Ranks below three are impossible. These are necessary types; no claim is made that each type satisfies the remaining original gradients.

## 5. Exact central cubic singularities

On $\mathcal A_0$ put $P_L(Z)=\nu(Z^3)/2$. Its derivative in direction $Y$ is $(3/2)\nu(Z^2Y)$. The Frobenius annihilator of $\mathcal A_0=\ker\nu(L^2\cdot)$ is exactly $\mathbb CL^2$. Therefore
$$
[Z]\in\operatorname{Sing}V(P_L)
\iff Z\ne0,\quad \nu(L^2Z)=0,\quad Z^2\in\mathbb CL^2. \tag{5.1}
$$
These are also the critical-scheme equations: they are precisely the four partial derivatives under the nondegenerate pairing. Euler's identity supplies the cubic equation. Since $\nu(L^3)=1$, $L^2\ne0$.

If $H$ has rank five, let $\tau(X)=\nu(L^3X)$ and divide the coordinates by the unit $L$. Then $\tau(1)=1$ and the cubic is $\tau(Z^3)/2$ on $\ker\tau$. Equation (5.1) becomes $Z^2=c1$. When $c\ne0$, scale to $c=1$. In each local block, one of $Z-1,Z+1$ is a unit, so $Z=1$ or $-1$ there. Thus
$$
Z=2e-1,\qquad e^2=e,\qquad \tau(e)=\tfrac12. \tag{5.2}
$$
Idempotents select whole local blocks. Complementary idempotents give the same projective point. These are ordinary double points: the Hessian $3\tau(ZYY')$ on $\ker\tau$ has radical exactly $\mathbb CZ$, because its radical equation is $ZY\in\mathbb C1$ and $Z^{-1}=Z$. The three-dimensional projective tangent Hessian is nondegenerate.

If $c=0$, square-zero elements in a length-$n$ block are exactly $\varepsilon^{\lceil n/2\rceil}\mathbb C[\varepsilon]/(\varepsilon^n)$. Let $U$ be their direct sum and $q=\sum_i\lfloor n_i/2\rfloor$. If $U\ne0$, $\tau|_U\ne0$ by its nonzero top local values. Hence the square-zero singular set is $\mathbb P(U\cap\ker\tau)$, with vector dimension $\max(q-1,0)$. At length five, $q\le2$:

| Partition | Square-zero projective singular points |
|---|---|
| $5$ | Exactly one |
| $4+1$ | Exactly one |
| $3+2$ | Exactly one |
| $3+1+1$ | None |
| $2+2+1$ | Exactly one |
| $2+1+1+1$ | None |
| $1+1+1+1+1$ | None |

At each of the four possible extra points $m_Z$ has rank two. For $5$ and $4+1$, the trace-zero element has initial order three and two respectively, because the top value of $\tau$ is nonzero. For $3+2$ and $2+2+1$, both socle components must be nonzero and their ranks add to two. Also $\tau$ is nonzero on $\ker m_Z$, so restricting the Hessian to $\ker\tau$ preserves rank two; removing its radial direction preserves that rank. These extra points are not ordinary double points. The table and (5.2) exhaust all geometric singular points, but do not replace complete criticality.

## 6. Remaining physical equations and matched Bell values

At an original complete critical point the full highest equation remains
$$
0=T_3(Kv(z))
=\tfrac12\nu\left([k_z-\nu(L^2k_z)L]^3\right),\qquad
k_z(t)=u(t)^{\mathsf T}Kv(z)\bmod g(t), \tag{6.1}
$$
as a polynomial identity in the physical $z$. All six mean and eleven second-moment gradients remain. The complete tensor identities in [the four-jet low-gradient calculation](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md), Sections 1–3, are dimension independent. Pairing the unchanged complete mean gradient with $\lambda$ gives $\mathcal Q_{F_0^2}(y,H)=0$.

When $H$ has rank five, the original second-gradient tensor
$$
N=T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH,\qquad F=\tfrac12y^{\mathsf T}Ky
$$
is nonzero. To see this, suppose $N=0$. Its cross block in $E=W\oplus\mathbb Cy$ gives $MKy=0$. Here $M$ is invertible on $W$ because $H=M+yy^{\mathsf T}/4$ has rank five. Thus $Ky$ annihilates $W$ and $T_{3,Ky}=0$. The remaining $W$ block gives $MKM=-FM/2$, whose trace on $W$ is $\operatorname{tr}(KM)=-2F$. The unchanged original Hankel identity instead gives $\operatorname{tr}(KM)=-F/2$. Hence $F=0$; $K$ then vanishes on $W$, between $W$ and $y$, and on $y$, making all five-dimensional $E$ totally isotropic. A nondegenerate symmetric form in dimension six has no such subspace. This contradiction proves $N\ne0$, and the physical projection lies on the genuine quadric $v(z)^{\mathsf T}KNKv(z)=0$.

For each unchanged matched direction $r$, on the original Schur critical section,
$$
\boxed{B_r=T_3(r)=\tfrac12\nu\left([X_r-\nu(L^2X_r)L]^3\right).} \tag{6.2}
$$
Equations (6.1), the full low gradients and (6.2) are an exact finite-algebra formulation of this entire branch. No new normalization, restricted mean, deleted jet or assumed unit was inserted.

The remaining task is to impose these original equations simultaneously on the seven divisor types and the three rank cases. A cubic surface in projective three-space can contain a rational curve despite having only finitely many singular points; the plane-cubic exclusion from the already settled essential dimensions at most three does not apply here. No Bell power identity, Bell-nonzero exclusion, or Hilbert invariant-subspace theorem has been proved by this reduction.
