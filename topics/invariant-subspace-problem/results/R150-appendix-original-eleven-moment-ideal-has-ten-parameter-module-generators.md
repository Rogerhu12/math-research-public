# The complete original moment ideal has ten generators over the full parameter ring

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Original equations and precise claim

Use the original matched cubic field $E$ and the global coordinates $(y,w,u)$ from
[R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md](R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md).
Set $B=E[y,w]$ and retain all six coordinates in each of $y,w$.

In
[R150-appendix-complete-original-twelve-gradient-low-normal-forms-over-all-parameters.md](R150-appendix-complete-original-twelve-gradient-low-normal-forms-over-all-parameters.md),
the complete original gradient ideal was transported to five equations
$$
F_i=\partial_{u_i}R'
$$
and twelve explicitly verified normal forms. Denote the six normal forms of $\partial_{w_j}R'$ by $W_j$.

The present exact result is that
$$
B[u]/(F_0,\ldots,F_4,W_0,\ldots,W_5)
$$
is generated over $B$ by the following ten original monomials:
$$
\boxed{
1,\ u_0,\ u_1,\ u_2,\ u_3,\ u_4,\
u_1u_4,\ u_2u_3,\ u_2u_4,\ u_3u_4.}
\tag{1}
$$
No parameter is inverted. This is a statement of ten module generators, not freeness or independence. It is valid before imposing the remaining six mean equations and remains a generating statement after any parameter base change, including $y\cdot w=1$.

These are exactly the original eleven Hankel-moment equations. Indeed, $H=T_w w+T_u u+c(y)$ with the fixed invertible matrix $(T_w,T_u)\in\operatorname{GL}_{11}(E)$. Thus the eleven $w,u$ derivatives are related to the original eleven $H$ derivatives by an invertible constant source matrix. Replacing the $w$ derivatives by $W_j$ uses the already verified constant corrections by the $F_i$ and preserves this ideal.

## 2. The six constant quadratic relations

All eleven equations have u-degree at most two, with fixed leading quadratics in $E[u]$. Write their leading parts as
$$
q_0,\ldots,q_4,\ \omega_0,\ldots,\omega_5.
$$
The $q_i$ have already been verified against the original pure cubic. Each $W_j$ is an exact normal form modulo the five $F_i$, so $\omega_j$ has only the ten mixed quadratic monomials.

Order those mixed monomials as
$$
u_0u_1,u_0u_2,u_0u_3,u_0u_4,u_1u_2,u_1u_3,
u_1u_4,u_2u_3,u_2u_4,u_3u_4.
$$
The new calculation reads every coefficient from the complete original $W_j$ row file, verifies the full compressed and logical SHA identities, and checks that these coefficients are fixed elements of $E$.

The resulting $6\times10$ coefficient matrix has exact rank $6$ over $E$. Its first six columns form a unit. Together with the original five-square unit for the $q_i$, this gives eleven independent quadratic leading relations. A degree-two complement is precisely the last four monomials in (1).

## 3. Every cubic is an original leading image

The complete cubic source map is
$$
E[u]_1^{\,11}\longrightarrow E[u]_3,\qquad
(\ell_0,\ldots,\ell_{10})\longmapsto
\sum_{i=0}^{10}\ell_i q_i^{\rm all}.
\tag{2}
$$
Here $q_i^{\rm all}$ lists the five $q_i$ and then the six $\omega_j$. The calculation retains all $55$ original source columns and all $35$ cubic output monomials.

Its rank is $35$. An actual square unit uses columns $0,\ldots,34$ in gradient-major order, with the five linear multipliers $u_0,\ldots,u_4$ for each gradient. Thus the witness already uses all linear multiples of the five $q_i$ and the first two $\omega_j$, while the calculation still retains the complete eleven-gradient source map.

It follows that
$$
(u_0,\ldots,u_4)^3\subset
(q_0,\ldots,q_4,\omega_0,\ldots,\omega_5).
\tag{3}
$$
The fixed homogeneous leading quotient therefore has Hilbert function
$$
(1,5,4)
$$
and dimension $10$. This homogeneous statement is not silently transferred to the full parameter deformation as freeness.

## 4. Why the finite-field witnesses prove exact E units

The single successful specialization used the coefficient prime $127$ and the field root $d=100$. The matched cubic vanishes at this root. Every rational denominator in every actual coefficient used in the two matrices is verified to be a $127$-unit.

The selected $6\times6$ determinant reduces to $1$. The selected $35\times35$ determinant reduces to $32$. Both are nonzero. These matrices consist of fixed $E$ constants; no mean or moment parameter has been specialized.

All $72$ entries in the two inverse identities for the six-dimensional unit and all $2450$ entries for the thirty-five-dimensional unit are verified over the residue field. A nonzero image proves that the respective original determinant is a nonzero element of the field $E$. Its exact inverse is consequently the adjugate divided by that same original determinant. This gives fixed exact $E$ source operators without expanding a very large rational $35\times35$ inverse.

## 5. Parameter-free degree reduction and source bound

Let $J_H=(F_0,\ldots,F_4,W_0,\ldots,W_5)$ in $B[u]$.

For any polynomial of u-degree $D\ge3$, apply the fixed cubic source operator from (2) to each leading monomial, multiplied by a monomial of degree $D-3$. Replacing the leading quadratics by the corresponding actual $F_i,W_j$ cancels its highest u-degree part and leaves lower u-degree, because all other terms of those equations have u-degree at most one. Repeat finitely.

At degree two, use the original five-square unit and the six additional mixed-quadratic unit relations. The resulting representative is in the $B$-span of (1). Every source coefficient constructed in this reduction has u-degree at most $\max(D-2,0)$. All inversions are fixed nonzero elements of $E$; arbitrary parameter coefficients remain polynomial.

This proves the ten-generator statement. Syzygies between the eleven equations can impose additional parameter-dependent relations among these ten generators, including relations of lower u-degree. Those relations are not discarded. The proof neither identifies the initial ideal of the deformed system exactly nor asserts flatness.

After quotienting also by the six original mean-gradient normal forms, the full critical algebra is a quotient of this ten-generated parameter module. Its ideal relations and their products still have to be handled. The same caution applies on the Bell-normalized base $y\cdot w=1$.

## 6. Actual execution and reproduction

The local exact consumer completed on 2026-11-16 at 05:27:37 UTC with exit code $0$ in $2.4527091679992736$ seconds. The budget was $120$ seconds and $1024$ MiB; actual maximum resident memory was $137508$ KiB.

The source is notes/2026-11-16-r150-original-eleven-moment-quadratics-complete-cubic-image-789f.py, blob 4fadfb182adbe117c3fcda39ba1eaa62e1e598bb, $11012$ bytes, SHA-256 396dacccfbe839d8964b4760b4955d3168c9823988570c4e35dbfc67d4683816.

The execution binding is 41ee91c353da2b8a33bbb631d46bc48e11709dcf42e131ebf4d417c7a3e98b63. The $2014$-byte complete small receipt has SHA-256 c4603bc4700a4e6226b2edcf4e90d5cfc0e0c4e3875568022db40cf88d34f019.

The complete temporary source model has $1653920$ gzip bytes, SHA-256 005484500176a294a3a14788843f1ad50031f2e2bce3e599c512e45ac5dacbb6. Its $3341015$ logical bytes have SHA-256 da5839f34930081d56df84d9d803daf2b226ac98de8364135463f6f94b6db1d2. It retains all eleven exact leading quadratics, all original source and output dictionaries, both actual field unit inverses, and the ten monomials.

Only source, parameters, execution identity/output hashes and this proof are committed. No temporary polynomial or matrix array is committed. The execution identity is notes/r150-nonrankone-execution-789f/20261116-local-eleven-moment-complete-cubic-image.json.
