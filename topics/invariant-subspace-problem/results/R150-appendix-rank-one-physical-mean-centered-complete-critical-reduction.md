# R150 appendix — exact centered reduction for every rank-one physical mean

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved algebraic equivalence**. No essential-dimension bound is assumed.

## 1. The fixed-mean linear highest equation

Let $y=a\,v(s)$ be a nonzero physical mean, including $s=\infty$.
Keep the original $K$, and put
$$
p=Ky,\qquad p_y(z)=y^{\mathsf T}Kv(z).
$$
In particular $y^{\mathsf T}Ky=0$.
Let $J_2,J_3$ be the original coefficient matrices of $k(z,t)^2$
and $k(z,t)^3$, where $k(z,t)=v(z)^{\mathsf T}Kv(t)$.
Both are invertible by the
[exact third-moment Schur calculation](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md).

If $B_y$ denotes multiplication by the binary quintic $p_y$,
from degree ten to degree fifteen, define the linear map
$$
L_y(M)=J_3^{-1}B_yJ_2M.
\tag{1.1}
$$
Sequences on the right are identified with their original
Hankel tensors. Thus $L_y(M)$ is a physical Hankel cubic and
$$
L_y(M)(Kv(z),Kv(z),Kv(z))
=p_y(z)\,v(z)^{\mathsf T}KMKv(z).
\tag{1.2}
$$
The definition is homogeneous and includes both projective charts.
Since multiplication by a nonzero polynomial and both $J_i$
are injective, $L_y$ is injective.

Because $y$ itself is physical, $y^3$ is Hankel and its original
polar is $p_y^3$. The complete highest equation
$$
T_3(Kv(z))=0,\qquad T_3=y^3-6yH+4V,
$$
therefore has the unique solution
$$
V=\frac32L_y(H)-\frac14y^3.
\tag{1.3}
$$
This uses all sixteen highest coordinates.

## 2. Centering the second cumulant

Put
$$
\boxed{M=H-\frac12y^2.}
\tag{2.1}
$$
Here $M$ is still physical Hankel: this use of rank-one mean
is essential. Since $L_y(y^2)=y^3$, equations (1.3) become
$$
\boxed{
H=M+\frac12y^2,\qquad
V=\frac32L_y(M)+\frac12y^3,\qquad
T_3=6\bigl(L_y(M)-yM\bigr).
}
\tag{2.2}
$$
Products such as $yM$ are symmetric tensor products, normalized
so that their diagonal polynomial is $(y\cdot r)M(r,r)$.

For each fixed nonzero physical $y$, every original highest
solution is given uniquely by the eleven Hankel coefficients
of $M$ in (2.2). In particular the remaining third tensor
depends linearly on those eleven coefficients.

Let
$$
A_y(M)=(L_y(M))_p.
\tag{2.3}
$$
Contraction of a physical cubic by a fixed vector is again
a physical Hankel quadratic. On its eleven coefficient
sequences the exact matrix is
$$
\boxed{A_y=B_y^{\mathsf T}J_3^{-1}B_yJ_2.}
\tag{2.4}
$$
Indeed $(B_y)_{nm}=p_{n-m}$ with zero coefficients outside
$0,\ldots,5$, so $B_y^{\mathsf T}V$ has entries
$\sum_i p_iV_{m+i}$, exactly the indicated contraction.

## 3. Every original low gradient is retained

The original complete normalized mean gradient is
$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp
       +4V(p,p,\cdot)-8V:(KHK),
$$
where
$$
F=\frac12y^{\mathsf T}Ky,\quad
b=p^{\mathsf T}Hp,\quad
\tau_2=\operatorname{tr}((KH)^2).
$$
Its vanishing is equivalent to all six original first gradients
because their omitted common factor is the invertible $3K$.

The original second-gradient quadric is
$$
N=T_{3,p}-F(y^2-2H)+4HKH,
$$
and all eleven second gradients vanish exactly when
$N(Kv(z),Kv(z))$ is the zero polynomial.

Substitute (2.2) and use $F=0$. Direct tensor contraction gives
$$
\boxed{
N=4MKM+6A_y(M),
}
\tag{3.1}
$$
and
$$
\boxed{
\Gamma=
2\operatorname{tr}((KM)^2)y+
8MKMp-
12L_y(M):(KMK).
}
\tag{3.2}
$$

Here is the cancellation explicitly. Write $b_M=p^{\mathsf T}Mp$
and $L=L_y(M)$. Then
$$
\begin{aligned}
HKH&=MKM+\operatorname{sym}(y\,Mp),\\
T_{3,p}&=6L_p-4\operatorname{sym}(y\,Mp),\\
\operatorname{tr}((KH)^2)&=\operatorname{tr}((KM)^2)+b_M,\\
HKHp&=MKMp+\frac12b_My,\\
V(p,p,\cdot)&=\frac32L(p,p,\cdot),\\
V:(KHK)&=\frac32L:(KMK)+\frac34L(p,p,\cdot)
                         +\frac12b_My.
\end{aligned}
\tag{3.3}
$$
In the first line $\operatorname{sym}(y\,Mp)$ means
$(y(Mp)^{\mathsf T}+(Mp)y^{\mathsf T})/2$.
The full matrix expansion actually gives
$HKH=MKM+\operatorname{sym}(y\,Mp)$, as written.
The $L(p,p,\cdot)$ terms in the mean gradient cancel.
The coefficients of $b_My$ are $(-2+2)+4-4=0$.
Equations (3.1) and (3.2) follow.

Consequently **complete original criticality for fixed physical
$y$ is equivalent to the following seventeen equations in $M$**:
$$
\boxed{
[\,v(z)^{\mathsf T}K(4MKM+6A_y(M))Kv(z)\,]_{z^m}=0
\quad(0\le m\le10),\qquad
\Gamma=0.
}
\tag{3.4}
$$
All six equations (3.2) are homogeneous quadratic equations
in $M$. The eleven equations in (3.4) have a quadratic part
and a linear part. No essential-dimension assumption, support
ansatz, positivity or low-gradient omission occurs here.

## 4. A trace form of the reduced scalar

Let
$$
e=B_yJ_2M,\qquad
q_y(M)=e^{\mathsf T}J_3^{-1}e
      =M^{\mathsf T}J_2A_yM,\qquad
\tau_3(M)=\operatorname{tr}((KM)^3).
$$
The exact Schur scalar on (2.2) is
$$
\boxed{
R_3\!\left(y,M+\frac12y^2\right)
=-8\tau_3(M)-18q_y(M).
}
\tag{4.1}
$$

To verify this, write $d$ for the coefficient vector of $p_y^3$.
Its $J_3^{-1}$ image is the physical sequence $y^3$.
Therefore
$$
d^{\mathsf T}J_3^{-1}d=0,\qquad
d^{\mathsf T}J_3^{-1}e=0,
$$
since these pairings evaluate $p_y^3$ and $p_yJ_2M$ at the
physical source of $y$, where $p_y$ is zero.
For $H=M+y^2/2$, the original Schur linear vector is
$\ell=-2d-6e$, so its quadratic contribution is $-18q_y(M)$.

Meanwhile, with $c_M=p^{\mathsf T}MKMp$,
$$
p^{\mathsf T}HKHp=c_M,\qquad
\operatorname{tr}((KH)^3)=\tau_3(M)+\frac32c_M.
$$
Thus the complete low Schur part
$12c_M-8\operatorname{tr}((KH)^3)$ is exactly $-8\tau_3(M)$,
proving (4.1).

At every complete critical point in this rank-one-mean section,
$$
q_y(M)=0,\qquad \tau_3(M)=0.
\tag{4.2}
$$
For the first identity, consider the allowed physical path
$y(t)=ty$, $H(t)=M+t^2y^2/2$, with its unique highest solution.
Formula (4.1) reads $-8\tau_3(M)-18t^2q_y(M)$.
Its derivative at $t=1$ must vanish at a complete critical
point, giving $q_y(M)=0$.
The original weighted Euler identity gives $R_3=0$ at such
a point; (4.1) then gives $\tau_3(M)=0$.
These scalar necessary conditions do not replace (3.4).

## 5. The zero-third-tensor kernel is exactly two-dimensional

The linear map $D_y=L_y-y(\cdot)$ in (2.2) has kernel exactly
the physical tangent quadratic space
$$
\ker D_y=
\operatorname{span}\{u^2,\operatorname{sym}(u\,u_1)\},
\qquad y=a u,
\tag{5.1}
$$
where $u_1$ is any genuine local first jet at $s$.

The inclusion from right to left follows by differentiating the
physical identities for $J_2,J_3$ at $s$.
For the reverse inclusion, $D_y(M)=0$ is precisely the original
condition $T_3=0$ after (2.2).
The Hankel-difference proof in §4 of the
[nonzero-mean zero-third-moment classification](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)
forces $H$ into this tangent quadratic space, and hence also $M$.
This argument includes infinity and requires no critical
equations beyond $T_3=0$.

Thus $D_y$ has rank nine for every nonzero physical mean.
The tangent space in (5.1) is contained in $\ker A_y$ because
$K(u,u)=K(u,u_1)=0$.
No equality with the full kernel of $A_y$ is asserted.

## 6. Exact author calculation and continuing scope

The accompanying
[BigInt verifier](../notes/2026-11-14-rank-one-centered-critical-reduction-verify.js)
reconstructs the full third tensor, every second-gradient
matrix entry, every first-gradient component and the low
Schur scalar from the unchanged original $K$.
It checks both physical charts with symbolic amplitude,
symbolic source, eleven free Hankel $M$ coefficients and
sixteen free Hankel cubic coefficients.
All 170 exact coefficient identities passed; the
[execution record](../notes/2026-11-14-rank-one-centered-critical-reduction-verification.json)
states the code-mode execution accurately.

This reduction remains valid in essential cubic dimensions
four, five and six, which are the remaining dimensions after
the complete low-dimensional classification.
It does not solve (3.4), and it does not claim a new matched
Bell-value or natural-power conclusion.
