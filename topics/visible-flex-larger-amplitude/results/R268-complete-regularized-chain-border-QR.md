# R268. Complete regularized chain-and-border QR

This result proves an exact-arithmetic factorization of one fixed finite
linear model. It does not prove that a particular finite Jacobian is
the derivative of the original nonlinear problem, that a floating QR
has a small backward error, or that a BVP step will be accepted.

The implementation to which the algebra applies is
[`exact_20261114_regularized_block_qr.py`](../computations/exact_20261114_regularized_block_qr.py),
33,143 bytes, SHA256
`596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`.
The proof is complete here; it is not conditional on a separate review
or an additional numerical acceptance gate.

## 268.1. Fixed model, coordinates and claim

Fix a real matrix

$$
A=W_r J S^{-1},
\qquad H=A^{\mathsf T}A+\lambda^2 I,
\qquad \lambda>0,
$$

where J is the complete finite linear model, S is its fixed positive
diagonal coordinate scale, and W_r is its fixed row weighting. No
weights or coefficient blocks change during this factorization. Let
C be any positive diagonal matrix of the same size. Define

$$
M=\begin{bmatrix}A\\\lambda I\end{bmatrix}C^{-1}.
$$

Then

$$
M^{\mathsf T}M=C^{-1}HC^{-1}.
\tag{268.1}
$$

The variables in the original scaled model are z. We use t=Cz for the
column-scaled factorization. In particular the regularization rows in
t coordinates are lambda C inverse, not lambda I.

Write

$$
t=(x_1,\ldots,x_N,u),
\quad x_i\in\mathbb R^n,
\quad u\in\mathbb R^d,
\quad q=Nn+d,
$$

with N at least one. The q rows of A consist of N interval blocks of
n rows and one complete right-boundary block of d rows. In the current
implementation,

$$
n=338,\qquad N=698,\qquad d=109+3=112,
\qquad q=236036.
$$

The physical blocks are the interior physical node values after the
exact inlet and constant-variable chart has been applied. The border
u contains all109 free core coefficients and all3 global scalar
controls. This proof assumes that complete chart and complete finite
Jacobian as supplied; it does not reprove their construction.

After applying the fixed row and column scales, write the interval
rows of AC inverse as

$$
r_0=V_0x_1+G_0u,
$$

$$
r_j=U_jx_j+V_jx_{j+1}+G_ju,
\qquad 1\le j\le N-1,
$$

and its complete boundary rows as

$$
r_b=Bx_N+Ku.
$$

All matrices in these expressions are fixed. The argument permits
arbitrary global blocks G_j. In the present original model, G_0
contains the first-interval inlet-core injection L0 E and the first
shared-control block; later G_j contain the complete shared-control
blocks. B and K contain the complete physical, core and scalar columns
of the actual finite right boundary. There is no truncated boundary
or discarded global column in the theorem.

Partition C conformally, and put

$$
D_i=\lambda C_i^{-1},\qquad D_g=\lambda C_g^{-1}.
$$

The exact squared norm being factorized is therefore

$$
\begin{aligned}
\mathcal E(t)=\|Mt\|_2^2
={}&\|V_0x_1+G_0u\|_2^2\\
&+\sum_{j=1}^{N-1}\|U_jx_j+V_jx_{j+1}+G_ju\|_2^2\\
&+\|Bx_N+Ku\|_2^2
 +\sum_{i=1}^{N}\|D_ix_i\|_2^2+\|D_gu\|_2^2.
\end{aligned}
\tag{268.2}
$$

**Theorem 268-A.** Apply the two local physical QR transformations and
the complete pure-global accumulation specified below, then include
the complete terminal boundary and the final physical penalty. The
retained square block upper-triangular matrix R satisfies

$$
R^{\mathsf T}R=C^{-1}HC^{-1}.
\tag{268.3}
$$

Every physical penalty D_i is inserted exactly once and the global
penalty D_g exactly once. Intermediate carry matrices may be singular;
the construction never inverts them. R is nonsingular. Given any
original-coordinate right-hand side r, the two triangular solves

$$
R^{\mathsf T}w=C^{-1}r,
\qquad Rv=w,
\qquad z=C^{-1}v
\tag{268.4}
$$

are equivalent to Hz=r.

## 268.2. Orthogonal triangularization without a rank assumption

We use the following elementary fact. For any real m-by-p matrix X
with m at least p, there is an orthogonal matrix Q for which

$$
Q^{\mathsf T}X=\begin{bmatrix}T\\0\end{bmatrix},
$$

where T is p-by-p upper triangular. A diagonal entry of T may be
zero. To obtain Q, process columns from left to right. Within the rows
at and below the current diagonal position, orthogonal rotations
eliminate each entry below that position. Previously processed columns
remain zero in those rows. A pair of zero entries requires no rotation.
Thus this procedure works without division by an asserted nonzero
matrix pivot or any full-rank hypothesis.

If additional columns Y are present, the same Q is applied to them:

$$
Q^{\mathsf T}[X\ Y]
=\begin{bmatrix}T&Y_1\\0&Y_2\end{bmatrix}.
$$

Orthogonality gives, for every pair of coefficient vectors a,b,

$$
\|Xa+Yb\|_2^2
=\|Ta+Y_1b\|_2^2+\|Y_2b\|_2^2.
\tag{268.5}
$$

Only rows which are zero in all remaining columns can be discarded
without changing this identity. Zero entries in the first column block
do not justify discarding a row which remains nonzero in the border.

## 268.3. One local front and the pure-global term

Suppose the current carry at physical node i is

$$
F_{i-1}x_i+T_{i-1}u.
$$

For i from1 through N minus1, combine this carry with the once-only
physical penalty D_i and the next original interval. The local front
is the3n-by-(2n+d) matrix

$$
\mathcal F_i=
\begin{bmatrix}
F_{i-1}&0&T_{i-1}\\
D_i&0&0\\
U_i&V_i&G_i
\end{bmatrix},
\tag{268.6}
$$

acting on (x_i,x_{i+1},u). Triangularize its first n columns with one
orthogonal row transformation. The result has the form

$$
Q_i^{\mathsf T}\mathcal F_i=
\begin{bmatrix}
\widehat D_i&\widehat U_i&\widehat B_i\\
0&W_i&Y_i
\end{bmatrix},
\tag{268.7}
$$

where the lower block has2n rows. The first block column has rank n
because it contains the positive diagonal D_i. Hence the triangular
matrix Dhat_i is nonsingular. This fact does not require the old carry
F_(i-1) to be nonsingular.

Now apply a second orthogonal transformation only to the2n lower
rows, triangularizing the n columns of W_i:

$$
\widetilde Q_i^{\mathsf T}[W_i\ Y_i]
=\begin{bmatrix}
F_i&T_i\\
0&E_i
\end{bmatrix}.
\tag{268.8}
$$

Both row blocks here have n rows. The new carry F_i may have deficient
rank. No inverse of F_i, W_i, or the old carry is formed.

Equations268.5–268.8 give the exact identity

$$
\begin{aligned}
&\|F_{i-1}x_i+T_{i-1}u\|_2^2
 +\|D_ix_i\|_2^2
 +\|U_ix_i+V_ix_{i+1}+G_iu\|_2^2\\
&\quad=\|\widehat D_ix_i+\widehat U_ix_{i+1}
                    +\widehat B_iu\|_2^2
       +\|F_ix_{i+1}+T_iu\|_2^2+\|E_iu\|_2^2.
\end{aligned}
\tag{268.9}
$$

The last term is a pure-global quadratic contribution. It is generally
nonzero. Its rows have zero next-physical entries, not zero total
entries.

Keep a d-by-d global root Z_(i-1). Triangularizing the complete stacked
matrix

$$
\begin{bmatrix}Z_{i-1}\\E_i\end{bmatrix}
$$

gives a d-by-d triangular root Z_i and zero rows below it. Consequently

$$
Z_i^{\mathsf T}Z_i
=Z_{i-1}^{\mathsf T}Z_{i-1}+E_i^{\mathsf T}E_i,
\qquad
\|Z_iu\|_2^2
=\|Z_{i-1}u\|_2^2+\|E_iu\|_2^2.
\tag{268.10}
$$

This compression retains all pure-global energy. The rows discarded
after this complete global QR are zero in all d remaining columns.

## 268.4. Complete energy invariant and induction

Initialize

$$
F_0=V_0,\qquad T_0=G_0,\qquad Z_0=D_g.
$$

After processing the first m physical nodes, where
0 is at most m and m is at most N minus1, the invariant is

$$
\begin{aligned}
\mathcal E(t)
={}&\sum_{i=1}^{m}
 \|\widehat D_ix_i+\widehat U_ix_{i+1}+\widehat B_iu\|_2^2\\
&+\|F_mx_{m+1}+T_mu\|_2^2+\|Z_mu\|_2^2\\
&+\sum_{i=m+1}^{N}\|D_ix_i\|_2^2\\
&+\sum_{j=m+1}^{N-1}\|U_jx_j+V_jx_{j+1}+G_ju\|_2^2\\
&+\|Bx_N+Ku\|_2^2.
\end{aligned}
\tag{268.11}
$$

An empty sum is zero. At m=0 this is exactly268.2. If it holds for
m less than N minus1, take i=m+1. Replace the old carry, its physical
penalty and the next interval by268.9. Combine the resulting pure-global
term with the old global root using268.10. All other terms are
unchanged, giving268.11 with m replaced by m+1. This proves the
invariant by induction.

In particular

$$
Z_m^{\mathsf T}Z_m
=D_g^{\mathsf T}D_g+\sum_{i=1}^{m}E_i^{\mathsf T}E_i.
\tag{268.12}
$$

The global penalty is present initially and is not added again at
every interval. Each physical penalty D_i is removed from the
unprocessed sum when and only when its node is processed. The term for
D_N remains for the last front. Thus no penalty row is omitted or
duplicated.

The invariant includes all interval and complete boundary rows. It
does not treat the border as a collection of independent nodewise
parameters, and it never drops the shared-control coupling or an
inlet-core column.

## 268.5. The final boundary front

At m=N minus1, the only remaining non-fixed rows are the carry at
x_N, its physical penalty, the complete boundary, and the accumulated
global root. Stack them as

$$
\mathcal F_N=
\begin{bmatrix}
F_{N-1}&T_{N-1}\\
D_N&0\\
B&K\\
0&Z_{N-1}
\end{bmatrix},
\tag{268.13}
$$

of size (2n+2d)-by-(n+d). Apply orthogonal QR to all n+d columns.
Write its retained square upper triangle as

$$
R_N=\begin{bmatrix}
\widehat D_N&\widehat B_N\\
0&\widehat G
\end{bmatrix}.
$$

The complete last-front norm is

$$
\|\mathcal F_N(x_N,u)\|_2^2
=\|\widehat D_Nx_N+\widehat B_Nu\|_2^2
 +\|\widehat Gu\|_2^2.
\tag{268.14}
$$

Together with the fixed physical rows from268.11, this defines the
square chain-and-border matrix R by

$$
(Rt)_i=\widehat D_ix_i+\widehat U_ix_{i+1}
                         +\widehat B_iu\quad(1\le i<N),
$$

$$
(Rt)_N=\widehat D_Nx_N+\widehat B_Nu,
\qquad (Rt)_g=\widehat Gu.
\tag{268.15}
$$

Equations268.11 and268.14 prove

$$
\|Rt\|_2^2=\mathcal E(t)=\|Mt\|_2^2
\quad\hbox{for every }t\in\mathbb R^q.
$$

Both Gram matrices are symmetric. Their equality of quadratic forms
implies equality of matrices: the diagonal entries follow by taking
t to be a coordinate vector, and the off-diagonal entries by taking
the sum of two coordinate vectors and subtracting the two diagonal
identities. This proves268.3 without invoking an unrecorded boundary
or an inverse carry.

For nonzero t,

$$
t^{\mathsf T}R^{\mathsf T}Rt
=\|AC^{-1}t\|_2^2+\lambda^2\|C^{-1}t\|_2^2>0.
$$

Thus R is nonsingular. As an upper-triangular matrix in the stated
block order, its scalar diagonal entries and each square diagonal
block are nonzero and invertible in exact arithmetic. This conclusion
comes from the complete regularization, not from any rank assertion
about an intermediate carry. When N=1, there is no local loop and the
same final-front argument starts directly from F0,T0,Z0.

## 268.6. What is lost if a pure-global block is dropped

Equation268.9 already shows the local loss: discarding E_i removes
the nonnegative quadratic term

$$
\|E_iu\|_2^2=u^{\mathsf T}E_i^{\mathsf T}E_iu.
$$

The carry and subsequent physical fronts do not use the global root.
Therefore if any of these E blocks are omitted from its accumulation,
the remaining physical factors and future carry construction can be
the same, while the final total energy is reduced by exactly the sum
of the omitted pure-global energies. If I_g injects the border
coordinates into the complete t vector, the altered Gram matrix is

$$
C^{-1}HC^{-1}
-I_g\left(\sum_{i\in\mathcal O}E_i^{\mathsf T}E_i\right)I_g^{\mathsf T},
\tag{268.16}
$$

where O is the set of omitted blocks. In original z coordinates the
corresponding loss is that matrix difference multiplied by C on both
sides. If the omitted energy is nonzero, the method factors a different
quadratic model. A finite dimension reduction or an acceptable-looking
terminal triangular block does not restore the missing energy. Only
an actually zero omitted E contributes no loss; the construction
does not assume such a special case.

## 268.7. Two triangular solves and the original-coordinate residual

Equation268.3 is equivalent to

$$
H=C R^{\mathsf T}RC.
$$

For any r, let b=C inverse times r. Solve the transpose system first.
In physical-node order its formulas are

$$
\widehat D_i^{\mathsf T}w_i
=b_i-\widehat U_{i-1}^{\mathsf T}w_{i-1},
\qquad 1\le i\le N,
$$

where the subtracted term is absent for i=1. The complete border
equation is

$$
\widehat G^{\mathsf T}w_g
=b_g-\sum_{i=1}^{N}\widehat B_i^{\mathsf T}w_i.
$$

For the reverse solve, first solve Ghat u=w_g, then in decreasing
physical-node order solve

$$
\widehat D_i v_i
=w_i-\widehat B_i u-\widehat U_i v_{i+1},
$$

with the final term absent for i=N. Set v=(v1,...,vN,u), and return
z=C inverse times v. Then

$$
Hz=C R^{\mathsf T}RC(C^{-1}v)
=C R^{\mathsf T}Rv=C(C^{-1}r)=r.
$$

Conversely the unique solution of Hz=r produces these two unique
triangular solutions. This proves268.4, including both C factors and
all border transposes. There is no additional division by S in this
H solve: A already acts on the original scaled-z coordinates. Any
later conversion of a chosen z to physical coefficient coordinates
belongs to the original chart, separately from this solve.

For an approximate returned vector z, the relevant original residual
is

$$
\rho=A^{\mathsf T}(Az)+\lambda^2z-r.
\tag{268.17}
$$

It must be distinguished from the residual computed using a floating
stored R. Let z_star=H inverse times r. In exact arithmetic,

$$
\|z-z_\star\|_2\le\frac{\|\rho\|_2}{\lambda^2},
$$

because, with $e=z-z_\star$, one has

$$
\lambda^2\|e\|_2^2\le e^{\mathsf T}He=e^{\mathsf T}\rho
\le\|e\|_2\|\rho\|_2.
$$

For
$\phi(z)=\tfrac12 z^{\mathsf T}Hz-r^{\mathsf T}z$, completion of
the square also gives

$$
0\le\phi(z)-\phi(z_\star)
=\tfrac12\rho^{\mathsf T}H^{-1}\rho
\le\frac{\|\rho\|_2^2}{2\lambda^2}.
\tag{268.18}
$$

These are inner fixed-model posterior statements, consistent with
[R263](R263-projected-KKT-and-damped-model-error.md).
For the constrained model of
[R265](R265-full-angle-linear-inequality-damped-model.md), an actually
evaluated vector and nonnegative full-row multipliers can instead
provide the lower-bound witnesses of
[R267](R267-two-point-damped-model-posterior-bound.md).
A QR-generated vector is merely one possible witness or basis
generator there. No projected KKT smallness, constrained optimum, or
nonlinear step acceptance follows from finite triangular output alone.

## 268.8. Exact correspondence with the frozen implementation and scope

The named source implements these identities as follows:

| Mathematical object or operation | Source object or method |
|---|---|
| complete original finite blocks | `linear.L`, `linear.R`, `linear.P`, `BY`, `BC`, `BP`, original `chart.inlet` |
| fixed A and scales | original pinned `CompleteLinearization.operator`, `weights`, `S`, optional `C` |
| scale each complete column | `_scaled`: divide by S, multiply by the fixed row weights, divide by C |
| once-only regularization | `_penalty`: the actual diagonal `lambda/C` |
| first physical QR | `front` and `_qr_prefix(front,n)` in `factorize` |
| second physical QR and pure-global term | `remainder`, `carry`, `carry_global`, `pure_global` |
| complete pure-global accumulation | QR of `vstack((global_root,pure_global))` |
| final complete boundary | `last`, including `BY`, `column_stack((BC,BP))` and the global root |
| retained R blocks | `diagonal`, `next-physical`, `global-border`, `global-diagonal` |
| transpose and reverse solves | `_solve_H`, with the complete border updates |
| original-coordinate factor action | `_factor_normal_action`, applying C on both sides of the stored R-transpose R |
| actual original residual | original complete A and AT actions in `_solve_H` |

The module retains original input identities and records both the
factor-based residual and the independent original A/AT residual. It
also compares the supplied A/AT actions with the pinned original
reconstructed operator on each actual returned candidate. These are
actual implementation diagnostics when executed, not hypotheses to
be silently replaced by proxy residuals.

Ordinary floating block assembly, QR, triangular solution, norm
evaluation and hashing do not themselves certify the real-number
identities or the posterior bounds. A floating implementation may
have scaling, conditioning, rounding or resource problems even though
the exact construction is valid. In particular this result asserts no
floating stability rate, no derivative accuracy of the underlying J,
no BVP solution, no new native-tail response, no geometric amplitude,
and no altered original acceptance criterion. The complete original
model and every original scientific gate remain external requirements.
