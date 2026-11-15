# R150: uniform source bound 8655 over every power of 31

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-15.  
Status: exact degree-reduction theorem for every existing original congruence solution; it does not assert all-precision solvability.

The [new original maximal-minor theorem](R150-appendix-new-original-maximal-minor-degree8769-and-unit-leading-coefficient.md) proves, for its explicitly specified **new** original row and column sets $I_*,J_*$,

$$
H_*=8835,\quad \deg D_*=8769,\quad
\operatorname{lc}(D_*)\in\mathbb Z_{(31)}^\times,
$$

where $B_*=A[I_*,J_*]$ and $D_*=\det B_*$. Its original natural determinant has order $66$, all its original-column replacement determinants have order at least $66$, and all its cofactors have order at least $55$.

Write $D=\mathbb Z_{(31)}$. The original source weights and cost are

$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad
\operatorname{cost}(x)=\max_{x_\ell\ne0}(\deg x_\ell+a_\ell-10).
$$

Thus $\max a_\ell=55$ and $\max(a_\ell-10)=45$. The output weight of $m^\beta$ is $10|\beta|$. No new numerical matrix calculation is needed for this corollary.

## 1. Integral common-factor identities

Use the already proved affine common factor

$$
K=K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4
$$

from the [full common-multiplier proof](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md). Rescale $K$ to be monic.

Keep $D_*=\det B_*$ without rescaling the determinant or its adjugate. Its coefficients belong to $D[s]$ and its leading coefficient is a unit. Normalize only the known factor $K$ to be monic. This $K$ belongs to $D[s]$, since its original leading coefficient $5^{16}$ is a $31$ unit. Monic division gives the quotient

$$
d_*=D_*/K,\qquad q=\deg d_*=8769-158=8611
$$

in $D[s]$, with a unit leading coefficient. The remainder is zero over $\mathbb Q[s]$ and therefore zero over $D[s]$. This convention keeps every adjugate identity below exact for the original $B_*$.

For every original column define

$$
P_\ell=\operatorname{adj}(B_*)A_{\ell,I_*}/K\in D[s]^{4354}.
$$

The numerator is an original maximal replacement minor, so it is divisible by $K$ over $\mathbb Q[s]$. Division by the monic $K$ shows the quotient already lies in $D[s]$. The exact identity is

$$
A_{J_*}P_\ell=d_*A_\ell
\tag{1}
$$

on all $4367$ original output rows. The selected outputs are injective on the generic image, so the adjugate identity on $I_*$ pays this complete identity.

Let $n\ge1$, let $R_n=D/(31^n)$, and suppose an original polynomial solution

$$
Ax=b\pmod{31^n}
$$

is given. The highest coefficient of $d_*$ is a unit in $R_n$, so every nonbasic source coefficient can be divided by $d_*$:

$$
x_\ell=d_*v_\ell+r_\ell,\qquad \deg r_\ell<8611
\quad(\ell\notin J_*).
$$

Use (1) to transfer each $d_*v_\ell$ into the original basic columns. This preserves the given congruence on every original output.

Put $\tau(b)=\max_i(\deg b_i+b_i^{\rm wt})$. The same calculation over $\mathbb Q[s]$ or over $R_n[s]$ gives

$$
\boxed{\operatorname{cost}(y)\le\max\{8655,\tau(b)+1\}.}
\tag{2}
$$

Here are all three bounds. Nonbasic sources have cost at most

$$
q-1+45=8655.
$$

By the original-column replacement bound in the cited new-minor theorem, the original-column transfer branch is at most

$$
8835+55-66-158-11=8655.
$$

By the cofactor bound in that theorem, the target branch is at most

$$
8835+\tau(b)-55-158-10-8611=\tau(b)+1.
$$

For the finite-ring argument, $\operatorname{adj}(B_*)b_{I_*}$ is divisible by $K$ modulo $31^n$ because a solution exists. Its quotient $T$ is defined by monic division in $R_n[s]$. In fact the transferred solution gives
$$
K d_* y_{J_*}=K\left(T-\sum_{\ell\notin J_*}P_\ell r_\ell\right).
$$
Multiplication by monic $K$ is injective on $R_n[s]$, so
$$
d_*y_{J_*}=T-\sum_{\ell\notin J_*}P_\ell r_\ell.
$$
Thus no divisibility of the unscaled target over $\mathbb Q[s]$ is assumed before an existing congruence is used. Both $K$ and $d_*$ have unit leading coefficient, so multiplication preserves the degree of every nonzero polynomial even though $R_n$ may have zero divisors. Thus the displayed degree subtraction is legitimate at every precision.

For the original $h_0t_\nu$, $\tau\le64$, so every existing mod-$31^n$ solution can now be reduced to the single fixed source bound

$$
\boxed{B=8655.}
$$

This does not assert that a solution exists at every precision. It removes the former need to assume a unit leading coefficient for the old chosen minor before performing this degree reduction.

## 2. Exact quantifiers and the relation to the earlier bound

Fix an integer $e\ge0$ and a fixed original polynomial target $b$. If $31^e b$ is solvable modulo arbitrarily large powers $31^n$, then (2) places all those solutions in one finite coefficient module, independently of $n$.

The finite integral linear-system argument then gives an exact solution

$$
Ay=31^e b,\qquad y\in D[s]^{6188},
\qquad
\operatorname{cost}(y)\le\max\{8655,\tau(b)+1\}.
$$

One may prove this by the Smith form of that finite coefficient matrix over the DVR $D$, or by the separatedness of its finitely generated cokernel under $31$-adic completion. The exponent $e$ is kept fixed throughout.

The previously proved rational source bound $8531$ for the common-multiplier targets remains better as a rational degree bound. The new number $8655$ has a different purpose: its reduction is now paid uniformly over every $D/(31^n)$, without an unproved leading-unit hypothesis.

The earlier single congruence modulo $31^6$ remains a single finite-precision certificate. Neither the new minor nor the fixed-degree mechanism turns it into all-precision solvability or proves that the original multiplier $h_0$ is sufficient.


## 3. What is newly paid

The old fixed-source descent needed a unit leading coefficient for a chosen original maximal minor. This condition has now been proved for the new $I_*,J_*$, and every existing congruence solution of the original low-weight targets admits the fixed bound $8655$ at every precision.

The calculation does not change the source cost $8531$ already available for the known rational common-multiplier solutions. It also does not identify the coefficients of those solutions, fix their denominator exponent, or prove all-precision solvability for the smaller target multiplier $h_0$.

All polynomial identities are on the complete original $4367$ outputs and use the complete original $6188$ source coordinates. The old order-$243$ minor and its still separate Plücker coordinate are not used in this finite-ring reduction.
