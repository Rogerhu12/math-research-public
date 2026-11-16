# Complete six mean relations and nine generators on the original Bell-normalized base

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Complete original setting

Work over the original matched cubic field
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
and the complete polynomial coordinates $(y,w,u)$ with original Bell polynomial $\mathcal B=y\cdot w$. No mean or moment coordinate is fixed.

The preceding exact results are:

1. [The complete twelve-gradient normal forms](R150-appendix-complete-original-twelve-gradient-low-normal-forms-over-all-parameters.md), including all original source corrections.
2. [Ten parameter-module generators for the original eleven moment equations](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md).

Write
$$
F_k=\partial_{u_k}R',\qquad
G^w_j=\partial_{w_j}R',\qquad
G^y_i=\partial_{y_i}R'.
$$
The already verified normal forms are
$$
N^y_i=G^y_i-\sum_k\lambda^y_{ik}F_k,\qquad
W_j=G^w_j-\sum_k\lambda^w_{jk}F_k.
\tag{1}
$$
Here $\lambda^y$ is linear in $y$, while $\lambda^w$ consists of fixed elements of $E$.

The moment ideal $(F,W)$ is exactly the transported original eleven Hankel-gradient ideal. Its quotient is generated over $E[y,w]$ by
$$
1,\ u_0,\ldots,u_4,\ v_1,v_2,v_3,v_4,
\quad
(v_1,v_2,v_3,v_4)=(u_1u_4,u_2u_3,u_2u_4,u_3u_4).
\tag{2}
$$
No freeness of these ten generators is assumed.

## 2. Exact six-by-ten original relations

Let $C$ be the actual constant $6\times6$ coefficient matrix of the six $W_j$ on the eliminated mixed monomials
$$
u_0u_1,u_0u_2,u_0u_3,u_0u_4,u_1u_2,u_1u_3.
$$
The new calculation computes $C^{-1}$ over $E$ and verifies all $72$ entries of its left and right inverse identities.

For each $N^y_i$, let $\alpha_i$ be its row of coefficients on those same six monomials. Set
$$
\mu_i=\alpha_i C^{-1},\qquad
\widehat G_i=N^y_i-\sum_j\mu_{ij}W_j.
\tag{3}
$$
All six eliminated coordinates vanish exactly. The remaining coefficients give a complete $6\times10$ matrix in the ordered monomials (2).

The code verifies all $96$ original coefficient identities, one for each of the sixteen original low coordinates of each of the six rows. It also computes
$$
\nu_{ik}=\lambda^y_{ik}-\sum_j\mu_{ij}\lambda^w_{jk}
\tag{4}
$$
and verifies all $30$ composed source coordinates. Combining (1)--(4) gives the complete original source identity
$$
\boxed{
G^y_i-\widehat G_i
 =\sum_{k=0}^4\nu_{ik}F_k
  +\sum_{j=0}^5\mu_{ij}G^w_j.}
\tag{5}
$$
Every coefficient in $\mu,\nu$ is linear only in $y$, with fixed coefficients in $E$. Thus this transport divides only by fixed field constants.

It follows that the complete original seventeen-generator gradient ideal is exactly
$$
(F_0,\ldots,F_4,G^w_0,\ldots,G^w_5,
  \widehat G_0,\ldots,\widehat G_5).
\tag{6}
$$
The original sixteen third-moment variables remain eliminated by the original constant Schur equivalence. Consequently the full original Jacobian problem is retained.

## 3. Four actual symmetric invertible coefficient matrices

The complete six-row vector has the form
$$
\widehat G
 =a(y,w)+L(y,w)u+
   T_1y\,v_1+T_2y\,v_2+T_3y\,v_3+T_4y\,v_4,
\tag{7}
$$
where $a$ has weight $5$, $L$ has weight $3$, and
$$
T_\ell\in E^{6\times6}.
$$
The matrices $T_\ell$ are read from all exact coefficients of the actual six-row output. Their symmetry is checked entrywise over $E$:
$$
T_\ell^T=T_\ell\qquad(\ell=1,\ldots,4).
$$
In particular, the part of (7) quadratic in $u$ is the $y$ gradient of
$$
\frac12\sum_{\ell=1}^4(y^TT_\ell y)v_\ell.
$$
This statement concerns that quadratic part and does not claim that every lower-order reduction commutes with parameter differentiation.

All four $T_\ell$ are invertible over $E$. The actual calculation checks every rational denominator and evaluates the original matched coefficient field at prime $127$, root $d=100$. Each complete $6\times6$ matrix has residue rank $6$. Therefore each original determinant is a nonzero fixed element of $E$.

This does not imply that the four vectors $T_1y,\ldots,T_4y$ are linearly independent for every nonzero $y$. No such assertion is used.

## 4. Exact unnormalized Bell source identity

Set
$$
\eta(y,w)^T=w^TT_1^{-1}.
$$
This row vector uses only a fixed field inverse. Its pairing with the first quadratic coefficient of (7) is exactly
$$
\eta^TT_1y=w^Ty=\mathcal B.
$$
Define
$$
c_\ell=\eta^TT_\ell y\quad(\ell=2,3,4),\qquad
a_*=\eta^Ta,\quad L_*=\eta^TL.
$$
Multiplying the full original identity (5) gives
$$
\boxed{
\mathcal B\,v_1+\sum_{\ell=2}^4c_\ell v_\ell
 +L_*u+a_*
 =\eta^TG^y
  -\sum_k(\eta^T\nu)_kF_k
  -\sum_j(\eta^T\mu)_jG^w_j.}
\tag{8}
$$
This is an identity before Bell normalization. The coefficient of $v_1$ is exactly the original Bell polynomial, not a generic parameter minor.

All coefficients in (8) are polynomial in $y,w$ over $E$. The identity introduces no mean or moment parameter denominator. Its original source terms have the correct common weighted degree $7$.

## 5. Nine generators over the complete Bell-normalized parameter ring

Let
$$
B_1=E[y,w]/(y\cdot w-1).
$$
The ten-generator statement (2) survives this parameter base change. In the quotient by the full original gradient ideal, equation (8) now solves $v_1$ with coefficient $1$. Hence the complete normalized critical algebra is generated over $B_1$ by
$$
\boxed{
1,\ u_0,\ u_1,\ u_2,\ u_3,\ u_4,\
u_2u_3,\ u_2u_4,\ u_3u_4.}
\tag{9}
$$

This is global on the entire base $y\cdot w=1$. It neither selects a coordinate chart nor inverts an additional parameter minor. Arbitrary further base change preserves these nine generators because the reductions are explicit polynomial source identities.

The algebra need not be free or nonzero. Parameter relations, the products of all original generators, and all remaining ideal consequences are retained. In particular, (9) does not yet prove the normalized ideal is the unit ideal or that a power of the Bell polynomial belongs to the unrestricted original Jacobian ideal.

## 6. Actual execution and reproduction

The complete consumer finished on 2026-11-16 at 05:38:32 UTC, exit code $0$, elapsed time $150.14140405000217$ seconds. Its budget was $600$ seconds and $4096$ MiB; actual maximum resident memory was $346208$ KiB.

Source: notes/2026-11-16-r150-original-six-mean-relations-in-ten-generators-789f.py. Blob 2f5614fad567b3268459d0067088cca66cdfc0d1. Size $13864$ bytes. SHA-256 bc73895e4c08f77461c0ae1be3495ee82f8866275492662a5c4382baa773b7fd.

The exact original streaming/arithmetic helper is the preceding v2 NF source, checked by its full source SHA-256 before import. Both parent models and all twelve complete original row files are checked by their compressed and logical SHA-256 and their original semantic bindings.

The new binding is 2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0. The complete small receipt is $4239$ bytes with SHA-256 f9dfaf8761b70a756515898b796dbdcad78267ad0d5a487712af35d301ec5d34.

The final indexed model is $1395$ gzip bytes, SHA-256 bd300391aff8f1f95860cbf614feb6a53f8a16c2d855b5fdf1df178d7337f061. Its $2812$ logical bytes have SHA-256 9961cbd32e7dc693bdfb1ab5819ca419372d6e297ca5af23149ae480d6dac4a1. It binds the six complete parameter rows, the full original source coefficients, the exact $C^{-1}$ and all four coefficient matrices.

The four-matrix file is $2208219$ gzip bytes, SHA-256 1928d85c9cb6a40cbbf038e39d65bd0b72dffe900d0da6c600070966444acc12; its logical SHA-256 is 7c37ad0846331a5ad9bf96d7c0086e2c65d65fe8831081dc34c778365592197d.

The execution identity is notes/r150-nonrankone-execution-789f/20261116-local-six-mean-ten-generator-relations.json. Only sources, parameters, execution identity/output hashes and this proof are committed; all coefficient arrays are temporary.
