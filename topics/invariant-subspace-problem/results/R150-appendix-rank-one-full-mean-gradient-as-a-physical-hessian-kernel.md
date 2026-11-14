# R150 appendix — the full rank-one mean gradient is a physical kernel of one quadratic matrix

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved exact identities**, valid in every essential dimension.

## 1. A matrix depending only on the centered second tensor

Keep the original $K,J_2,J_3$.
For a physical Hankel quadratic $M$, let
$$
h_M(z)=v(z)^{\mathsf T}KMKv(z)=J_2M
$$
in coefficient notation, and let $C_M:S_5\to S_{15}$ be
multiplication by this homogeneous degree-ten polynomial.
Define
$$
R_M=C_M^{\mathsf T}J_3^{-1}C_M,\qquad
\tau_2(M)=\operatorname{tr}((KM)^2),
$$
$$
\boxed{
G_M=\tau_2(M)K^{-1}+4MKM-6R_M.
}
\tag{1.1}
$$
This is a symmetric six by six matrix whose entries are
homogeneous quadratic forms in the eleven coefficients of $M$.
It depends on $M$, not on the mean.

Let $y=a v(s)\ne0$ be any physical mean and use the exact
centered highest solution
$$
H=M+\frac12y^2,\qquad
V=\frac32L_y(M)+\frac12y^3,\qquad
T_3=6(L_y(M)-yM).
\tag{1.2}
$$

**Theorem.** The complete normalized original mean gradient is
$$
\boxed{\Gamma=2G_MKy.}
\tag{1.3}
$$
Hence the six original mean-gradient equations are exactly
$G_MKy=0$.

To prove it, write $p=Ky$.
Commutativity of multiplication of binary forms gives
$$
B_yJ_2M=C_Mp,\qquad
L_y(M)=J_3^{-1}C_Mp.
$$
Moreover
$$
L_y(M):(KMK)=C_M^{\mathsf T}L_y(M)=R_Mp.
\tag{1.4}
$$
Indeed the degree-ten coefficients of $h_M$ are the
anti-diagonal sums of $KMK$, and the $i$th entry of the
left side is $\sum_{j,k}L_{i+j+k}(KMK)_{jk}$.
This is precisely the $i$th entry of $C_M^{\mathsf T}L$.

Substituting (1.4) in the
[complete centered gradient](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md),
$$
\Gamma=2\tau_2(M)y+8MKMp-12L_y(M):(KMK),
$$
gives (1.3). The omitted factor between $\Gamma$ and the
actual original six gradients is the fixed invertible $3K$,
so their zero sets are unchanged.

## 2. An equivalent contraction of the complete third tensor

The same mean gradient also has the exact form
$$
\boxed{
\Gamma=-2\bigl(\tau_2(M)y+T_3:(KMK)\bigr).
}
\tag{2.1}
$$
For the normalized symmetric product,
$$
(yM):(KMK)
=\frac13\bigl(\tau_2(M)y+2MKMp\bigr).
$$
Use $T_3=6(L_y(M)-yM)$ to obtain (2.1).

In particular, at a complete critical point,
$$
T_3:(KMK)=-\tau_2(M)y.
\tag{2.2}
$$
The left side belongs to $\operatorname{ess}(T_3)$.
Therefore
$$
\boxed{
\tau_2(M)\ne0\ \Longrightarrow\
y\in\operatorname{ess}(T_3).
}
\tag{2.3}
$$
A rank-one mean outside the essential space necessarily has
$\tau_2(M)=0$, as well as the zero contraction in (2.2).

These conclusions use the full mean vector.
They are not obtained by retaining only a directional mean
derivative or only the highest equation.

## 3. The same matrix is an exact mean Hessian at zero mean

There is also a direct interpretation in the original Schur
scalar. Hold an arbitrary Hankel $M$ fixed, and temporarily
let $x$ range over the entire six-dimensional mean space.
The terms quadratic in $x$ in the full
$R_3(x,M)$ are exactly
$$
6F_0(x)\tau_2(M)+12(Kx)^{\mathsf T}MKM(Kx)
 -18(C_MKx)^{\mathsf T}J_3^{-1}(C_MKx).
$$
By (1.1), this is $3x^{\mathsf T}KG_MKx$.
The remaining nonconstant terms in $x$ have degrees four or six.
Consequently
$$
\boxed{\nabla_x^2R_3(0,M)=6KG_MK.}
\tag{3.1}
$$
This identity does not assume that $(0,M)$ is critical.
Combining (1.3) and (3.1), a rank-one mean in a complete
centered critical point is a physical null direction of
this precise mean Hessian.

This Hessian description is an algebraic equivalence for the
six mean equations. It does not make them sufficient for
complete criticality; the eleven second-gradient equations
remain in force.

## 4. Exact fixed-mean coefficient interface

The accompanying
[integer generator](../notes/2026-11-14-rank-one-centered-integer-system-generator.js)
uses the already published exact $J_3$ adjugate and determinant.
For any supplied integer physical mean it constructs all
seventeen original low equations in the eleven centered
Hankel variables $m_0,\ldots,m_{10}$.

It performs BigInt arithmetic and does not invert a numerical
matrix. It computes
$$
L_{\rm num}=\operatorname{adj}(J_3)B_yJ_2,
$$
so $L_y=L_{\rm num}/D$ with $D=\det J_3$.
The raw second-gradient coefficients are those of
$$
4D\,MKM+6B_y^{\mathsf T}L_{\rm num}M,
$$
after evaluation on the original physical polars.
The raw mean coefficients are
$$
2D\tau_2(M)y+8D\,MKMKy
 -12(L_{\rm num}M):(KMK).
$$
Each resulting equation is divided only by the greatest common
divisor of its integer coefficients.
The recorded signed factor $\sigma$ satisfies
$$
D\cdot(\text{original equation})
=\sigma\cdot(\text{stored primitive equation}).
\tag{4.1}
$$
Thus no original equation is dropped.

The
[fixed-mean data](../notes/2026-11-14-rank-one-zero-infinity-centered-systems.json)
contains the two means $y=e_0$ and $y=e_5$.
For each it records eleven linear coefficients and sixty-six
quadratic coefficients per equation, with the exact monomial
ordering and the factors (4.1).
It also includes the complete sixteen by eleven
$L_{\rm num}$ matrix, so the highest tensor is recoverable
without recomputing $J_3$.

The data were generated by exact BigInt arithmetic.
As an author consistency check, all 2,970 equation and
highest-map coefficients agree modulo $103$ with a separate
direct construction from the original formulas.
That comparison is a check of the coefficient interface,
not a proof that its critical equations have been solved.

## 5. The exact remaining mathematical task

The
[zero-$A_yM$ theorem](R150-appendix-rank-one-mean-zero-centered-linear-section-has-zero-third-tensor.md)
has already proved that any rank-one-mean critical point with
$A_yM=0$ or $MKM=0$ has $T_3=0$.
The complete low-essential-dimension work also leaves only
essential dimensions four, five or six when $T_3\ne0$.

In that remaining branch the original problem is still
$$
G_MKy=0,\qquad
v(z)^{\mathsf T}K(4MKM+6A_yM)Kv(z)\equiv0,
$$
with $A_yM\ne0$ and $MKM\ne0$.
The identities above provide an exact matrix and coefficient
interface to those equations.
They do not assert a new higher-dimensional Bell-value
vanishing, natural Jacobian power or operator conclusion.
