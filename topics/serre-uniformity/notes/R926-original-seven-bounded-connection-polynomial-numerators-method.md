# R926 execution method: seven bounded connection numerators

This consumer implements R922 §§2–4 for the seven **already completed** R905 connections. The mathematical result is R926-original-seven-bounded-connection-polynomial-numerators. It uses the final R922 proof, SHA256 75e0e04e986203598b556403b4ea8eec3706da838e934ae11810c5abda569731, and the independently certified R905 endpoint.

The original order is $D_1,D_2,D_3,D_4,D_5,X,D_N$. No new choice of a connection, 543-dimensional gauge, divisor representative, frame or basis is made. All finite arrays use the original auxiliary prime $\ell=1000000753$. They are not 41-adic values or expanded characteristic-zero coordinates.

## 1. The four completed stages for each divisor

For every $D$, consume only the following original R905 stages and their common source metadata:

1. The exact regular-connection DAG.
2. The complete bundle unit graph, including the original $F_D(z)$ and the already certified inverse $F_D(a)^{-1}$.
3. The complete quotient and $h_a$-division model.
4. The complete full-principal-parts solution, including all 670 coefficients and the original 543 selected rows and columns.

The connection DAG itself already contains the original differential basis indices and the actual auxiliary $a$. It points to the same completed full solution. Thus the consumer does not download or rebuild the old $544\times670$ principal-parts matrix merely to recover those indices. It does not import the original R905 mathematical core.

The source is actual run **43893738459**, source **f4589d2b0d8f5e2a914ca165a601351d09c303a9**, configuration **fe220a1b3216cd28a16d0d3c1916f4660b7708c39a129e8696ba285c2c9e7136**. Its successful final certificate is SHA256 **24045a35dcd878cad48d28aea20bce7077161b0eb9dc86113a54ba83bc71d4a4**. Its 14,778-byte manifest is SHA256 **b11afeda52eb05af86a6fe162484854c29e0764acb26fb383f3f04d214b63fb0**.

## 2. Preserve the original coefficient vector

The first 146 columns of $F_D$ have section weights $n_i=2$; the last 126 have $n_i=3$. The old bundle field column_weights records the corresponding splitting weights $1$ and $0$, not these section weights.

With $t=z-a$, the already certified differential basis is

$$
t^k\theta_i\,dz,\qquad 0\leq k<n_i.
$$

Use the actual DAG basis.indices and the same 670 solution coefficients to form

$$
c_i(t)=\sum_k c_{ik}t^k.
$$

The resulting three coefficient vectors are a new storage form of the same original connection. The original selected rows, columns, unselected zero coordinates and differential frame $dz$ are recorded. No principal-parts solve is repeated.

The required relation is

$$
F_D(a+t)^t x_D(t)=c_D(t).
$$

The transpose is part of the original trace-dual convention.

## 3. One new norm on the whole degree-272 divisor

Let $Q_D$ and $L_a$ be the completed quotient and division matrices from R905. Its canonical quotient representatives are the literal free rows in $V_2$. Multiplication by $\tau$ is the unchanged normal-coordinate embedding $V_2\to V_3$. Form

$$
Z_D=Q_D L_a T_\tau E_D.
$$

The implementation selects the corresponding columns of the existing $L_a$, then multiplies by $Q_D$. It does not recompute $L_a$, the quotient, a primitive element, a Krylov inverse or the characteristic relation of the old primitive element.

The new matrix $Z_D$ is multiplication by $\tau/h_a$ on **all** of $H^0(\mathcal O_D)$, of dimension 272. Its action on the stored algebra unit is multiplied back against the canonical coordinates $Q_D(\tau h_a)$.

Compute the characteristic polynomial of this new full matrix using FLINT's exact modular nmod_mat.charpoly. Reverse its 273 coefficients to obtain

$$
d_D(a+t)=\det(I-tZ_D)=\frac{\det F_D(a+t)}{\det F_D(a)}.
$$

The normalization is $d_D(a)=1$. The entire characteristic polynomial is retained, including zero eigenparts and their multiplicities. A lower actual degree of $d_D$ is reported without deleting those parts. No disjointness of $D$ and $H$ is assumed.

This is a new determinant norm of a new multiplication operator. It is not a reconstruction of the old R905 primitive polynomial.

## 4. Resumable Taylor vectors and the bounded numerator

Read the original $F_D(a)^{-1}$. Use the actual source $a$ and the translated coefficients

$$
F_D(a+t)=\sum_{m=0}^3F_mt^m.
$$

When $a=0$, this is the original coefficient list with no shift arithmetic. The existing inverse is never recalculated.

For $0\leq r\leq273$, form only the new right-hand sides and vectors

$$
x_r=F_0^{-t}\left(c_r-\sum_{m=1}^{\min(3,r)}F_m^t x_{r-m}\right).
$$

Complete blocks of 16 vectors are immutable stages; the last block has two vectors. A block carries its exact previous-block reference, the original inverse source and the original coefficient-vector source. Continuation starts after the last complete block and does not replay completed vectors.

Set

$$
y_D=(d_Dx_D)\bmod t^{274}.
$$

A lower triangular scalar convolution matrix applies the denominator to the 274 vectors. Verify every bound

$$
\deg y_{D,i}\leq271+\epsilon_i.
$$

Save both the explicit $t=z-a$ coordinates and the translated original $z$ coordinates. No extra scalar normalization is introduced.

## 5. Complete global acceptance

The Taylor prefix alone is not an acceptance test. Check the full polynomial equality

$$
F_D^t y_D=d_Dc_D
$$

on all 272 rows and all **277** possible coefficients $t^0,\ldots,t^{276}$. The left side may have degree 276; the right side has degree at most 274, so the final two rows of polynomial coefficients are also actually checked to be zero.

These full products are stored in immutable coefficient blocks of size 16. Their sources are the original $F_D$, the exact original $c_D$ source, and the new denominator and numerator. This is the mathematical exit of the consumer, not an additional independent test task.

The exact characteristic-zero expression remains

$$
d_D=\det F_D/\det F_D(a),\qquad
y_D=\operatorname{adj}(F_D^t)c_D/\det F_D(a).
$$

The original inverse is a unit at the actual place, so the finite arrays are the images of this source-bound expression. The output does not claim its characteristic-zero coefficients have been expanded.

## 6. Source transport, recovery and output

The standard-library wrapper first reads the pinned actual R905 manifest, expands the exact selected plain specs and verifies all four source stages for each divisor against the same R905 configuration. This gives 28 mathematical input stages, the successful final certificate, the three metadata files and the original manifest: 33 selected members. It does not copy the old retained-input carrier or unrelated trace stages.

The complete expanded file map and input references enter the new mathematical tag. Every new stage uses the new R926 source SHA and configuration. Original R905 bytes and tags remain unchanged.

The public request allows at most 300 minutes and a divisor prefix from one through seven. These are scope controls outside the mathematical tag. A complete final result requires all seven original divisors; a shorter completed prefix is honestly incomplete.

An atomic current file records the active divisor and next uncompleted Taylor index. The content-named stage manifest lists all complete stages. Restore binds the actual manifest and preserves complete blocks; it never overwrites a newer current state with a historical incomplete final certificate. The standard-library wrapper performs only IO, schema, source identity and recorded-certificate verification.

## 7. Boundaries

This producer is independent of the new shared $R=M_gG^{-1}$ computation. It neither computes $R$ nor waits for its numerical result.

It does not yet evaluate $d_D(U)$ or $y_D(U)$ in the R885 target algebra. In particular, $F_D(a)$ being a unit is not a claim that the future target denominator $d_D(U)$ is a unit. It computes no Hecke calibration, non-$p$ contribution, endpoint value, Poincare period or height.

The corrected R922 target coordinate remains $V=K(U)/P_U(U)$. No numerator column is reinterpreted as a divided coordinate. The later target transport must retain the complete quotient rule and the old inverse of $P_U$.

All new arithmetic runs only in the authorized public repository Actions.
