# R150 appendix: complete original residue rank 21, an external factor of degree 60, and source bounds 8471 and 8595

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.

Status: a proved characteristic-zero factor from a completed first-precision calculation on all original 56 rows. The subsequent precision-two calculation is unfinished. No exact degree-120 projection gcd is asserted.

## 1. The exact original matrix and the already paid upper divisor

Let $A$ be the original $4367$ by $6188$ source matrix over $\mathbb Q[s]$. Keep the original source multiplier degree at most three and all original outputs of degrees one through five. Let

$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8.
$$

The [original projection reduction](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md) gives the complete original polynomial matrix

$$
B_{\rm out}\in\mathbb Q[s]^{56\times22}
$$

whose full maximal-minor gcd outside $\Sigma_0$ is the exact original projection divisor $\Omega$. Every row is retained. The source-level equivalence is over $\mathbb Q[s,\Sigma_0^{-1}]$, with all discarded denominators supported on $\Sigma_0$.

The independently completed three-minor computation supplies a genuine upper divisor $U$ for the full gcd:

$$
\Omega\mid U,\qquad
U=f^2,\qquad
f\text{ monic and squarefree},\qquad
\deg f=60,\qquad
\gcd(f,\Sigma_0)=1.
\tag{1.1}
$$

The equality $U=f^2$ is an actual exact factorization of the paid characteristic-zero polynomial, not a conjectural lift of a finite-field factor.

The identities fixing these polynomials are:

| Object | Identity |
|---|---|
| Original core semantic binding | ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba |
| Original 56 by 22 core logical SHA256 | 752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8 |
| Actual upper coefficient SHA256 | 150089b4e115b8d975d4e4eb13492779a692a6af258094f852af22b7f34e652d |
| Squarefree degree-60 factor coefficient SHA256 | c2e27cf7e732257b695a6fa655f24b2305fd817a779baa3965a2eccc5f663dc2 |

The complete upper certificate retains three exact original 22 by 22 determinants. The present lower argument uses all 56 rows and is independent of which three determinants supplied (1.1).

## 2. The completed calculation over the whole squarefree algebra

Work in

$$
E=\mathbb Q[s]/(f).
$$

Because $f$ is squarefree, this is a finite product of fields. The program only treats an entry as a pivot when it is a unit in the entire algebra $E$. If an entry were nonzero but noninvertible, the code would split the support by an exact coprime gcd decomposition; no such split occurred in this completed phase.

The actual calculation completed 21 unit Schur pivots on the whole original 56 by 22 matrix. After these pivots the complete retained block had shape

$$
35\times1
$$

and every entry was exactly zero in $E$. Thus

$$
\operatorname{rank}_{\mathbb Q[s]/(h)}B_{\rm out}=21
\quad\text{for every monic irreducible }h\mid f.
\tag{2.1}
$$

The upper bound in (2.1) uses all original residual rows. The lower bound uses the 21 pivots that are units simultaneously on all factors of $f$. In particular, the statement does not assume that $f$ is irreducible.

The exact profile verified

$$
\sum_{j=1}^{21}j(34+j)=11165
$$

retained-row Schur coordinate products. All original 56 rows and 22 columns were present before the elimination. The input's constant row normalizations and all 1232 original polynomial coordinates were checked. The exact zero residual gate is the only route in the source from this first-precision mode into the later precision-two replay, and the actual receipt records that transition.

## 3. The true lower factor and the still unresolved multiplicity

Equation (2.1) means that every full 22 by 22 minor vanishes modulo each $h\mid f$. Since $f$ is squarefree, their gcd is divisible by $f$. Together with (1.1),

$$
\boxed{f\mid\Omega\mid f^2,\qquad 60\le\deg\Omega\le120.}
\tag{3.1}
$$

More precisely, the residue corank is one at every irreducible factor $h\mid f$. The original matrix has generic column rank 22, so its local Smith form has exactly one positive invariant factor there. Its exponent is either one or two by (1.1). Equivalently,

$$
\Omega=fg,\qquad g\mid f,\qquad g\text{ monic and squarefree}.
\tag{3.2}
$$

No choice between those exponents has yet been made. The later precision-two replay had completed only five of the 21 already selected pivots when the run reported failure. It does not alter the independently completed first-precision assertions above, and it does not prove $\Omega=f^2$.

## 4. A smaller common multiplier for all nine actual targets

Write $\Delta_A$ for the monic full affine determinantal divisor of the original $A$. The [actual quotient-defect calculation](R150-appendix-original-quotient-defect-one-and-affine-degree299.md), combined with the original coefficient-prime carrier, proves

$$
\deg\Delta_A\le299.
$$

The complete known common factor is

$$
K=K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad \deg K=158,\qquad K\mid\Delta_A.
$$

Let $R_{\rm out}$ be the part of $\Delta_A/K$ outside $\Sigma_0$. Then

$$
\deg R_{\rm out}\le141.
$$

The exact original cokernel sequence, with $W$ the normal-degree-at-least-two target submodule, is

$$
0\longrightarrow W/(L\cap W)
 \longrightarrow V/L
 \longrightarrow (V/W)/((L+W)/W)\longrightarrow0,
\qquad L=\operatorname{im}A.
$$

Its torsion lengths subtract exactly because the induced map of the equal-rank free quotients is a surjection and hence an isomorphism. Therefore $\Omega\mid R_{\rm out}$, and the external target divisor divides $R_{\rm out}/\Omega$. This is the [full original PID argument](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md).

It already suffices to remove the proved factor $f$. Put

$$
M_{60}=R_{\rm out}/f.
$$

This is an actual nonzero polynomial, defined from the same original determinantal divisors. It obeys

$$
\deg M_{60}\le81.
\tag{4.1}
$$

For the nine original squares

$$
t_j=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10,
$$

use the already proved local multiplier

$$
h_*=s^3F_+^2F_-^2E_8,\qquad\deg h_*=23.
$$

All critical local memberships for $h_*t_j$ are already paid. Outside $\Sigma_0$, the exponent of $M_{60}$ dominates the exact cokernel length difference. The same local-to-global argument gives

$$
\boxed{
M_{60}h_*t_j\in\operatorname{im}_{\mathbb Q[s]}A
\quad(2\le j\le10),\qquad
\deg(M_{60}h_*)\le104.
}
\tag{4.2}
$$

This uses one common multiplier for all nine targets. Its coefficients are not newly expanded here, and $M_{60}$ is not asserted to be constant.

## 5. Rational source cost 8471, with the original chosen minor unchanged

Keep the original chosen minor used in the rational source theorem:

$$
H=8770,\quad
8527\le\deg D\le8640,\quad
v_\infty D\ge130,
$$

with all original-column replacements and cofactors of order at least 125. The source weights remain $20+10|\alpha|$ for $m^\alpha N_i$ and $25+10|\alpha|$ for $m^\alpha\Gamma_i$, so $\max(a_\ell-10)=45$.

The complete common factor may now be taken to be $Kf$, of degree 218. Thus the degree $q$ of the same original determinant quotient satisfies

$$
8309\le q\le8422.
$$

For $b=M_{60}h_*t_j$, its weighted target degree is at most

$$
\tau(b)\le81+23+20+20=144.
$$

The three original remainder-and-transfer bounds are consequently

$$
\begin{aligned}
\text{nonbasic sources}&\le8422-1+45=8466,\\
\text{original-column transfer}&\le8770+55-125-218-11=8471,\\
\text{target adjugate branch}&\le8770+144-125-218-10-8309=252.
\end{aligned}
$$

Therefore (4.2) has original source representatives of cost at most

$$
\boxed{8471.}
\tag{5.1}
$$

No new source columns or output rows have been substituted for the original ones.

## 6. The factor is 31-integral, and the uniform finite-precision cost is 8595

Put $D_0=\mathbb Z_{(31)}$. The new original maximal minor $B_*$ already satisfies

$$
D_*=\det B_*,\qquad
\deg D_*=8769,\qquad
\operatorname{lc}(D_*)\in D_0^\times,\qquad H_*=8835.
$$

Its original determinant and replacements have natural order at least 66, and its cofactors at least 55. The original determinant $D_*$ is kept exactly as defined; it is not rescaled in the source identities.

Since $f\mid\Omega\mid\Delta_A\mid D_*$ and $f$ is monic, Gauss' lemma applied to the monic polynomial $D_*/\operatorname{lc}(D_*)$ proves

$$
f\in D_0[s].
$$

Rescale only $K$ to be monic and define $K'=Kf$. Then $K'$ is monic in $D_0[s]$, has degree 218, and divides every original maximal replacement minor. Consequently

$$
d_*=D_*/K'\in D_0[s],\qquad
\deg d_*=8551,\qquad
\operatorname{lc}(d_*)\in D_0^\times.
$$

For every original source column,

$$
P_\ell=\operatorname{adj}(B_*)A_{\ell,I_*}/K'\in D_0[s]^{4354},
\qquad
A_{J_*}P_\ell=d_*A_\ell
$$

on all original outputs. The first integrality statement follows by monic division; the full-output identity follows from the paid generic-image injectivity of the selected output coordinates.

For any existing original congruence solution modulo $31^n$, division of every nonbasic coefficient by $d_*$ remains valid over $(D_0/31^n)[s]$. The same three branches now give

$$
\begin{aligned}
8551-1+45&=8595,\\
8835+55-66-218-11&=8595,\\
8835+\tau(b)-55-218-10-8551&=\tau(b)+1.
\end{aligned}
$$

Hence the [uniform finite-precision source theorem](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md) improves to

$$
\boxed{\operatorname{cost}(y)\le\max\{8595,\tau(b)+1\}.}
\tag{6.1}
$$

The proof preserves its exact quantifiers. The existence of a solution is assumed at each precision being reduced. For fixed $e$, solvability of $31^e b$ at arbitrarily high precision then yields an exact $D_0[s]$ solution within the same bound by the finite coefficient-module argument. This does not assert any new all-precision solution, a new fixed denominator exponent, or exact membership of $h_0$ merely from a finite congruence.

## 7. Actual computation and the precise completed boundary

Actual run: 43756208221. Step:

    complete-original56-local-outside-gcd-300-second

Execution source:

    8e4025c0ef0ee422077b1fc66ece96d97c3c40e9

Mathematical elapsed time: 288.930271448 seconds. The raw mathematical receipt has 6043 bytes and SHA256

    26917bb0ac3058ce08c57b18f91bca119b42ad866c4264e98ad9d4a02a7382cc.

The actual [small receipt](../notes/r150-source-kernel-session-789f/43756208221-complete-original56-local-outside-gcd-300-second.json) records the complete first-precision profile, the exact zero-residual transition, and then five completed replay pivots at precision two. Its whole checkpoint generation is 27. The total 16210 verified Schur products split as 11165 first-precision products and 5045 later replay products.

The frozen consumer source has SHA256

    0e111c2334bf62e4b4404d84c8af5e9f62ee99a6b64f766bad541c126b1e7fa4

and semantic binding

    862cca4d82af7c8031de01117b2f18516c0d3622a73b4e794c4f3280a0fe9850.

The process ended with status failed and exit code 1 during the unfinished later computation. The conclusions of this appendix depend only on the verified first-precision transactions that had already completed and been saved. The complete outside gcd and the exponent-two replay remain open at this record.
