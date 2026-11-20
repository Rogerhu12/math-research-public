# R150: the rank-four unit two-plus-one complement of a double zero is empty

Author: Astra-ISP-b2a9acde-20261120 / r150_structure, with root. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-20 UTC.

**Status: proved, with an explicit exact univariate verification source.** In the original essential-four outer-mean length-five reduction, no complete critical point has a simple zero of the same $L$ on a double-point factor and a unit complement of type $2+1$. The proof covers zero local weights, half weights, all vanishing pairing cases and points at infinity. Its computational step is an exact rational calculation from displayed original equations and univariate gcds; it uses no finite-field or floating-point inference.

## 1. The same physical factors and original low gradients

Use [the length-five reduction](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md), under its rank-three mean-catalecticant, essential-four and outer-mean hypotheses. The present support consists of an active double point $v_0,v_1$, an active simple point $v_2$, and a distinct double point $w_0,w_1$ on which $L$ has a simple zero.

Normalize the unit factors by the same $L$. Their algebra and Frobenius functional are
$$
\mathcal B=\mathbb C[t]/(t^2)\times\mathbb C,\qquad
\tau(1_{\rm dbl})=a,\quad \tau(t)=1,\quad \tau(1_{\rm pt})=b,
$$
$$
a+b=1,\qquad b\ne0.
\tag{1.1}
$$
The local weight $a$ may be zero. On the nonunit double factor use the allowed normalization $\nu(1)=0,\nu(\epsilon)=1,L=\epsilon$ from [the double-zero formulation](R150-appendix-essential-four-double-zero-rank-four-isotropic-active-branch-is-empty.md), Section 1. Its change of representative explicitly preserves $y,H,V$ and the same $L$.

For covector coordinates
$$
X=r(v_0),\quad Y=r(v_1),\quad Z=r(v_2),\quad R=r(w_0),\quad S=r(w_1),
$$
put $m=aX+Y+bZ$. The exact moments and cubic are
$$
y(r)=m,\qquad H(r,r)=\tfrac14(aX^2+2XY+bZ^2+R^2),
$$
$$
V(r,r,r)=\tfrac18(aX^3+3X^2Y+bZ^3)+\tfrac38R^2S,
$$
$$
T_3=P(X-Z,Y)+\tfrac32R^2(S-m),
\tag{1.2}
$$
where, writing $\delta=1-2b=a-b$,
$$
P(D,Y)=Y^3-3bDY^2-\tfrac32b\delta D^2Y-\tfrac12ab\delta D^3.
\tag{1.3}
$$

Write the active Gram matrix and the two cross columns as
$$
K_a=\begin{pmatrix}0&0&A\\0&C&B\\A&B&0\end{pmatrix},\qquad
U=(u,v,w),\qquad V_1=(U_0',U_1',U_2').
\tag{1.4}
$$
The entries zero in the active Gram matrix follow from physical curve isotropy. The zero double factor has $K(w_0,w_0)=K(w_0,w_1)=0$; its remaining diagonal entry is unrestricted.

Let
$$
m_0=\tau(U),\quad m_1=\tau(V_1),\quad
d=K_a(a,1,b)^{\mathsf T}=(bA,C+bB,aA+B),\quad
F=abA+bB+C/2.
$$
The unchanged complete mean equations give
$$
E_a+U^2-2m_0U=0,\qquad \tau(U^2)=2m_0^2,
$$
$$
\tau(UV_1)=\tau(Ud)-2Fm_0+2m_0m_1.
\tag{1.5}
$$
These are exact coefficients of $e_L-2L D_Ld-2d^2+4FLd=0$ in the faithful length-five algebra. In the active coordinates,
$$
\begin{aligned}
(E_a)_0={}&-b\delta^2A^2-2b\delta AB+2bAC,\\
(E_a)_1={}&2b^2\delta AB-2b(1+2b)AC-2b\delta B^2+6bBC+2C^2,\\
(E_a)_2={}&-a\delta^2A^2-2\delta^2AB-2bAC-2\delta B^2+2BC.
\end{aligned}
\tag{1.6}
$$

We retain the complete physical highest identity from (1.2). The complete second-gradient tensor is
$$
N=N_a+m_0R(S-m)+\tfrac12(m_1-F)R^2+\tfrac12\tau\bigl(U\cdot(X+Yt,Z)\bigr)R,
\tag{1.7}
$$
where $(X+Yt,Z)$ denotes the two components of the active algebra. Here
$$
N_a=T_{P,Ky}-F(yy^{\mathsf T}-2H_a)+4H_aK_aH_a,\qquad
H_a=\tfrac14\begin{pmatrix}a&1&0\\1&0&0\\0&0&b\end{pmatrix}.
\tag{1.8}
$$
The contraction $T_{P,Ky}$ is one third of the directional derivative of $P$. Formulas (1.5)–(1.8) follow directly from the original tensors, with all original moments retained.

At the physical double base $w_0$ one has $R=S=0$. Consequently
$$
P(u-w,v)=0,\qquad N_a(U)=0.
\tag{1.9}
$$
All calculations below use necessary consequences of the unchanged full gradients. The full Gram form on the five-dimensional original support has rank at least four.

## 2. A zero active difference

Put $D_0=u-w$. If $D_0=0$, (1.3) and (1.9) give $v=0$. Then $m_0=u=w$, and the square equation in (1.5) gives $m_0^2=2m_0^2$, so $U=0$.

The active mean equation is now $E_a=0$. Its complete classification for a physical active $2+1$ support is [the rank-three exclusion](R150-appendix-essential-four-all-rank-three-second-moment-branches-are-empty.md), Section 3: either $K_a=0$, or $b=1/2$ and $C=0$. That classification used only this active mean equation, so applies unchanged here.

If $K_a=0$, the active cross matrix $(U,V_1)$ has rank at most one; at least two active vectors lie in the radical of the full five-dimensional Gram form, impossible. In the other case, $v_0,v_1$ are totally isotropic and $w_0$ is orthogonal to both. Their span is an original totally isotropic length-three jet space of type $2+1$. The [complete isotropic-jet classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md), Sections 3–5, excludes it. Thus $D_0\ne0$ from now on.

## 3. The complete half-weight case

Suppose $a=b=1/2$. Then
$$
P(D,Y)=Y^2(Y-\tfrac32D).
$$
The square equation in (1.5) is
$$
m_0^2=\tfrac14D_0^2+D_0v-v^2.
\tag{3.1}
$$

First suppose $v=0$. Equation (3.1) gives $m_0=\pm D_0/2$. Thus $U$ has exactly one of the forms
$$
(q,0,0)\quad\text{or}\quad(0,0,q),\qquad q\ne0.
\tag{3.2}
$$
In either case $U^2-2m_0U=0$, so $E_a=0$ and $C=0$ by the active mean classification. The original active second-gradient form is then
$$
N_a=\tfrac{2B-A}{4}Y^2-\tfrac B2XY,\qquad F=A/4+B/2.
\tag{3.3}
$$

For $U=(q,0,0)$, the highest equation at $v_0$ gives $U_0'=A$. The original second-gradient identity at that point, using (1.7), gives $m_1=F$. The mixed mean equation in (1.5) gives $U_0'/2+U_1'=m_1$, and comparison with $\tau(V_1)=m_1$ then gives
$$
V_1=(A,\ B/2-A/4,\ 0).
$$
At the physical zero double base the active coordinates have expansions
$$
X=q+U_0's+O(s^2),\quad Y=U_1's+O(s^2),\quad Z=O(s^2).
$$
The $R^2(S-m)$ term has order at least four there. The order-two coefficient of the highest identity is therefore $-3q(U_1')^2/2$, forcing $U_1'=0$ and $B=A/2$. At the active simple point, $R=0$ and the highest equation gives $B^2(B-3A/2)=0$. Hence $A=B=0$ and $V_1=0$. The cross matrix has rank at most one and $K_a=0$, contradicting the Gram rank bound.

For $U=(0,0,q)$, the mixed mean equation gives $U_0'/2+U_1'=0$. The same local highest order-two calculation is now $3q(U_1')^2/2=0$, so $U_1'=U_0'=0$. Both cross columns are supported only at the active simple-point coordinate. Since $C=0$, the full Gram matrix is a star centered at that coordinate plus the possible diagonal entry $K(w_1,w_1)$. Its rank is at most three, again impossible.

It remains in the half-weight case that $v=3D_0/2$. Equation (3.1) gives $m_0^2=-D_0^2/2$, and
$$
U=(m_0-D_0,\ 3D_0/2,\ m_0-2D_0).
$$
The three active equations (1.5)–(1.6) give
$$
AC=-3D_0^2/2,\qquad C(3B+2C)=0,\qquad
-AC+2BC=-9D_0^2/2.
$$
Thus
$$
B=2A,\qquad C=-3A,\qquad A^2=D_0^2/2,
\tag{3.4}
$$
so $A\ne0$. For general $C$ at $b=1/2$, the exact active form is
$$
N_a=\tfrac{2B-A+2C}{4}Y^2-(B/2+C)XY
+\tfrac C2YZ-\tfrac C4XZ+\tfrac C4X^2.
$$
Insert (3.4) and the displayed $U$. Direct cancellation of $m_0$ gives
$$
N_a(U)=\frac{9}{16}AD_0^2\ne0,
$$
contrary to (1.9). Every half-weight case has now been excluded.

## 4. Rational parameterization of the remaining necessary equations

Assume $b\ne1/2$ and $D_0\ne0$. Use ratios by $D_0$ for every Gram entry and both cross columns; all the necessary equations are homogeneous in these pairings. Rename the normalized pairings $A,B,C,u,v,w,V_1$. Thus $u-w=1$.

Set
$$
\rho=v-b,\qquad \sigma=m_0.
$$
Then
$$
U=(\sigma-\rho,\ \rho+b,\ \sigma-\rho-1).
\tag{4.1}
$$
The highest and square equations at $w_0$ become
$$
2\rho^3=b(3\rho+1),\qquad \sigma^2=b-\rho^2.
\tag{4.2}
$$
Because $b\ne0$, $\rho\ne0$ and $3\rho+1\ne0$. Put $\theta=\sigma/\rho$. Solving (4.2) gives
$$
D_\theta=3\theta^2+1,\qquad
\rho=-\frac{\theta^2+1}{D_\theta},\qquad
b=\frac{(\theta^2+1)^3}{D_\theta^2},\qquad
\sigma=\theta\rho.
\tag{4.3}
$$
Here $D_\theta\ne0$ and $\theta^2+1\ne0$. Also
$$
b-\tfrac12=\frac{(\theta^2-1)^2(2\theta^2+1)}{2D_\theta^2},
$$
so the already excluded half-weight case contains every $\theta=\pm1$ and every $2\theta^2+1=0$.

In (1.5), the three active mean equations now have the target vector
$$
E_a=
\begin{pmatrix}
b-2\rho^2\\
2\rho(\rho+b)\\
b-2\rho^2-2\rho-1
\end{pmatrix}.
\tag{4.4}
$$
The necessary original value $N_a(U)=0$ is the linear equation
$$
n_AA+n_BB+n_CC=0,
\tag{4.5}
$$
with
$$
\begin{aligned}
n_A={}&2b[(1-4b)\rho^2+(2-6b)\rho+\delta-ab
-\sigma(\rho+1)\delta],\\
n_B={}&2b[4\rho^2+3\rho+1-b-\sigma(2\rho+1)],\\
n_C={}&4\rho^2-b-2\sigma\rho.
\end{aligned}
\tag{4.6}
$$
These coefficients are $4N_a(U)$, obtained from the original tensor (1.8). The attached verifier reconstructs them directly from $y,H,V$. Their last coefficient has the exact factorization
$$
n_C=-\frac{(\theta-1)(\theta+3)(\theta^2+1)^2}{D_\theta^2}.
\tag{4.7}
$$

## 5. The two exceptional parameter values $\theta=0,-3$

At $\theta=0$, (4.3) gives $a=0,b=1$, $\rho=-1$, $\sigma=0$, and $U=(1,0,0)$. Equation (4.5) is $2B+3C=0$. The last active mean equation gives $C(A+3C/2)=0$. If $C\ne0$, then $A=B=-3C/2$, and the middle active mean equation is $2C^2=0$, impossible. Therefore
$$
B=C=0,\qquad A^2=1.
$$
The highest equation at the active double base gives $U_0'=A$. Its first jet gives $U_1'=0$. The original second-gradient value at that base then gives $U_2'=0$. Thus $V_1=(A,0,0)$. The full Gram matrix is a star centered on $v_0$ plus the possible $w_1$ diagonal entry, of rank at most three, impossible.

At $\theta=-3$, the parameters are
$$
a=-27/98,\quad b=125/98,\quad \rho=-5/14,\quad \sigma=15/14.
$$
Here $n_C=0$, so we do not divide by it. Equation (4.5) gives $B=(117/98)A$. After this substitution the three equations (4.4) are a linear system in $A^2,AC,C^2$, with determinant $-47500/16807\ne0$. Its unique values are
$$
A^2=-686/475,\qquad AC=234/175,\qquad C^2=-11070/16807.
$$
They contradict the rank-one identity because
$$
(AC)^2-A^2C^2=\frac{9936}{11875}\ne0.
$$
Thus $\theta=0,-3$ are also excluded.

## 6. An explicit three-by-three source and its determinant exceptions

For every remaining parameter $n_C\ne0$. Put
$$
\alpha=-n_A/n_C,\qquad \beta=-n_B/n_C,\qquad C=\alpha A+\beta B.
$$
Substitute into the three original mean equations (1.6). In the monomials $(A^2,AB,B^2)$ their coefficient matrix is
$$
\mathcal M=
\begin{pmatrix}
-b\delta^2+2b\alpha&
-2b\delta+2b\beta&0\\
-2b(1+2b)\alpha+2\alpha^2&
-2b(1+2b)\beta+2b^2\delta+6b\alpha+4\alpha\beta&
-2b\delta+6b\beta+2\beta^2\\
-a\delta^2-2b\alpha&
-2\delta^2-2b\beta+2\alpha&
-2\delta+2\beta
\end{pmatrix}.
\tag{6.1}
$$
Its target is (4.4). Define
$$
f=2\theta^3+2\theta^2+\theta-1,\qquad
g=7\theta^4+4\theta^3+11\theta^2+2.
$$
The exact determinant is
$$
\det\mathcal M=
\frac{16(\theta-1)^4(\theta+1)^6(\theta^2+1)^6
(2\theta^2+1)f}{(\theta+3)^3D_\theta^8}.
\tag{6.2}
$$
If $f=0$, Cramer's numerator for the $A^2$ column is
$$
-\frac{8(\theta-1)^4(\theta+1)^5(\theta^2+1)^4g}
{(\theta+3)^3D_\theta^6}.
\tag{6.3}
$$
Every other displayed factor is nonzero in the present case. Exact rational Euclidean division gives $\gcd_{\mathbb Q[\theta]}(f,g)=1$. Consequently (6.3) is nonzero at every root of $f$, whereas the left side of the Cramer identity $(\det\mathcal M)A^2$ is zero. Thus this entire determinant-zero case is inconsistent.

Suppose now $f\ne0$, and denote the unique solution of (6.1) by
$$
L=A^2,\qquad M=AB,\qquad Q=B^2.
$$
The first entry and its required rank-one relation are
$$
L=-\frac{D_\theta^2g}
{2(\theta+1)(\theta^2+1)^2(2\theta^2+1)f},
\tag{6.4}
$$
$$
M^2-LQ=
\frac{\theta^2(\theta+3)^2D_\theta^2F_7}
{16(\theta+1)(\theta^2+1)^4(2\theta^2+1)f^2},
\tag{6.5}
$$
where
$$
F_7=15\theta^7+15\theta^6+54\theta^5+14\theta^4
+47\theta^3-17\theta^2+12\theta-12.
\tag{6.6}
$$
All factors outside $F_7$ in (6.5) are nonzero here. Hence $F_7=0$. Exact rational division also gives $\gcd(F_7,g)=1$. Therefore $g\ne0$ and (6.4) gives $A\ne0$. This explicitly handles the potential division by $A$.

Equations (6.2)–(6.5) are identities from the three displayed original mean equations and their original $N_a(U)$ constraint; they are not an independently chosen presentation.

## 7. The highest equations determine the other cross column

Put
$$
\lambda=L,\qquad q=M/L=B/A,\qquad h=\alpha+\beta q=C/A.
$$
These are rational functions of $\theta$, obtained solely by the three-by-three system above.

The two local values of the normalized cross element $U$ are
$$
U_0=\sigma-\rho
=-\frac{(\theta-1)(\theta^2+1)}{D_\theta},\qquad
U_2=\sigma-\rho-1
=-\frac{\theta(\theta+1)^2}{D_\theta}.
$$
They are nonzero in the present case. Hence $U$ is a unit in the active $2+1$ algebra. Write $U_1=\rho+b$.

At the active double base, its first jet, and the active simple point, the active cubic evaluated on the original Gram kernel, divided by $A^3$, is the element with components
$$
p_0=\tfrac12ab\delta,\qquad
p_1=\tfrac32b\delta(aq-h),
$$
$$
p_2=q^3-3bq^2-\tfrac32b\delta q-\tfrac12ab\delta.
\tag{7.1}
$$
These follow directly by substituting the three normalized Gram columns
$(0,0,1)$, $(0,h,q)$ and $(1,q,0)$ into (1.3), taking the physical first derivative at the double point for $p_1$.

The original highest equations on all these active jets read
$$
A^3(p_0,p_1,p_2)+\tfrac32U^2(V_1-Ad_{\rm bar})=0,
\qquad
d_{\rm bar}=(b,h+bq,a+q).
$$
Thus the second cross column is exactly $V_1=A V_{\rm bar}$, where
$$
V_{\rm bar}=d_{\rm bar}-\tfrac{2\lambda}{3}
\left(
\frac{p_0}{U_0^2},
\frac{p_1}{U_0^2}-\frac{2U_1p_0}{U_0^3},
\frac{p_2}{U_2^2}
\right).
\tag{7.2}
$$
No local derivative or active moment is omitted; the middle term is the ordinary inverse of $U^2$ in the dual-number factor.

Let
$$
\tau V_{\rm bar}=a(V_{\rm bar})_0+(V_{\rm bar})_1+b(V_{\rm bar})_2,
\qquad F_{\rm bar}=ab+bq+h/2,
$$
$$
n_{\rm base}=\tfrac12b\delta\,[a(a+q)-h/2].
$$
Here $A^3 n_{\rm base}$ is precisely $N_a$ at the active double base. Now use the original full tensor (1.7) at that point and divide by the already nonzero $A$. Its necessary value is the following completely specified rational function:
$$
\boxed{
\Psi(\theta)=
\lambda n_{\rm base}
+\sigma U_0((V_{\rm bar})_0-b)
+\tfrac12(\tau V_{\rm bar}-F_{\rm bar})U_0^2
+\tfrac12bU_2U_0=0.
}
\tag{7.3}
$$
The four terms in (7.3) are respectively the active $N_a$, the $m_0R(S-m)$ term, the $(m_1-F)R^2/2$ term, and the $\tau(U X_{\rm act})R/2$ term. Thus this source is the original eleven-gradient system, not an auxiliary replacement.

## 8. Exact univariate contradiction and reproducible verification

Let $R_{28}$ be the primitive numerator with positive leading coefficient of the explicitly defined rational function (7.3), after cancellation. Its degree is 28. Its denominator has only the already excluded factors
$$
(\theta+1)^3(2\theta^2+1)D_\theta^4 f g^2
$$
and a nonzero rational constant. The exact characteristic-zero calculation is
$$
\boxed{\gcd_{\mathbb Q[\theta]}(F_7,R_{28})=1.}
\tag{8.1}
$$
Consequently (6.6) and (7.3) cannot both hold.

The companion exact source [unit two-plus-one double-zero verifier](../notes/2026-11-20-essential-four-unit-two-plus-one-double-zero-verify.py) makes this calculation fully reproducible. It constructs $P$ and $N_a$ from the original $y,H,V$ in (1.2), checks all three active mean coefficients in (1.6) and all three coefficients in (4.6), forms the exact matrix (6.1), and verifies (6.2), (6.4), and (6.5). It then derives (7.2) from the three original highest equations, reconstructs the original value (7.3), and performs the three univariate rational gcds
$$
\gcd(f,g),\qquad \gcd(F_7,g),\qquad \gcd(F_7,R_{28}),
$$
all equal to one. It separately checks the rational inconsistency at $\theta=-3$.

For the final gcd, integer primitive pseudo-division is also sufficient: repeatedly replace a current polynomial $P$ by
$$
\operatorname{lc}(Q)P-
\operatorname{lc}(P)\theta^{\deg P-\deg Q}Q
$$
until its degree is below that of $Q$, remove the nonzero integer content, and continue. Each step preserves a common complex root. The exact rational gcd in (8.1) is independently reproducible from these source formulas without retaining computed remainder tables. The verification retains source equations and a bounded result; recomputable intermediate remainder tables are unnecessary.

This is a univariate calculation over $\mathbb Q$ with every original source and every division exception stated. No finite-field ideal membership is lifted to characteristic zero.


The source was executed with no arguments in [Actions run 44723783966](https://github.com/Rogerhu12/math-research-public/actions/runs/44723783966), job 136245961458, from commit fae69f6c767bdfbca9ba3ecfa396353fb91a66dd, using SymPy 1.13.3 and mpmath 1.3.0. All stated source identities and three rational gcd assertions passed in 20.22139929 seconds. The root fetched the original job log and matched the frozen source SHA-256 36c48f8dc03ebb77324b3ca4b02d80d96f7db81b6e2db80eb392c01c476ad188. The bounded one-line result has SHA-256 479440043b53266b03df195bc560dc2bac9f71a326f282d0fcbdc414ce4a5b98; the decoded job-log SHA-256 is 9a91e6f92ff9d612e7402f9e458cc44716cae2925c317a36afdd57d1284b80d2. Only source, parameters and these run identities/hashes are retained. The same job performed a successful actual pull and verified both unchanged README blobs at 2026-11-20 10:59:14 UTC.

## 9. Exhaustion and accurate remaining scope

Section 2 handles the zero active difference. Section 3 handles every half weight. In the remaining parameterization, $D_\theta=0$ and $\theta^2+1=0$ are algebraically impossible, the half-weight roots are already excluded, Section 5 handles $\theta=0,-3$, Section 6 handles all determinant zeros and the possible $A=0$ case, and Sections 7–8 give the contradiction in every remaining case.

Therefore the entire rank-four simple-zero-double branch with unit complement of type $2+1$ is empty. All calculations preserve the same original physical jets, the same $L$, the original $K$ and the complete gradients; a support point at infinity is covered by the local parameter arguments.

For a simple zero on a double factor, the remaining unit length-three complement is now the reduced three-point case. The different rank-four family with an isolated zero point and a split unit length-four complement, rank five, and the other essential-space branches remain open. This exclusion alone is not a global matched Bell radical certificate or a solution of the Hilbert ISP.
