# R270: exact condensation of the complete damped quadratic to the inequality support

## Status and scope

This is a complete statement in finite-dimensional exact real algebra.
It uses the same fixed full operator A, residual vector b, and positive
damping lambda as R263/R265/R268. No numerical execution, change to a
frozen solver, new acceptance gate, or prediction about request42 is
part of the result.

The central conclusion is that when B has zero columns outside a
specified coordinate set L, the complete inequality-constrained
quadratic is exactly equivalent to a strictly convex quadratic on L.
Every outside coordinate is minimized conditionally and then restored.
It is not held fixed. The actual twelve-query support has4397
coordinates, whereas the complete model has236036.

The same result can be obtained without subtracting two normal
matrices: preserve the complete QR root, its pure-global remainder,
and the original affine term, eliminate the exterior physical chain,
then eliminate only the free-core global coordinates. A dense24576
by24576 dual Gram or24576 separate whole-chain inverse calls is not
required by this algebra.

The original source to which the interface discussion refers is
[exact_20261114_regularized_block_qr.py](../computations/exact_20261114_regularized_block_qr.py),
SHA256
`596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`.
Its exact root identity is proved in
[R268](R268-complete-regularized-chain-border-QR.md).
The actual full-angle operator remains the one frozen in the
[twelve-query interface](../notes/2026-11-14-twelve-query-fixed-support-RMS470-interface.md).

## 1. Fixed problem and the support hypothesis

Fix a real matrix A, a vector b, and lambda>0. Define

$$
H=A^TA+\lambda^2I,\qquad
g=A^Tb,\qquad f_0=\tfrac12\|b\|_2^2,
$$

and

$$
f(z)=f_0+g^Tz+\tfrac12 z^THz
    =\tfrac12\|b+Az\|_2^2+\tfrac{\lambda^2}{2}\|z\|_2^2.
\tag{270.1}
$$

Thus H is symmetric positive definite and H>=lambda^2 I.

The coordinates z are the original scaled step coordinates. In the
current application A=Wr J S^{-1}, where S is the positive chart
step scale and Wr is fixed during this model. Bounds involving
lambda^2 below apply in these z coordinates. They are not an
unqualified statement about the unscaled physical coefficient norm.

Let L be a set of coordinate indices, let E be its complement, and
write z=(u,v) after a coordinate permutation, where u=z_L and v=z_E.
Assume every complete inequality row satisfies

$$
B=(B_L,\ 0),\qquad Bz+c=B_Lu+c.
\tag{270.2}
$$

No row is discarded. In particular rows whose supports overlap
different query cells, and all repeated physical angles, remain in B.

Use the block notation

$$
H=\begin{pmatrix}
H_{LL}&H_{LE}\\H_{EL}&H_{EE}
\end{pmatrix},\qquad
g=\begin{pmatrix}g_L\\g_E\end{pmatrix}.
$$

Define

$$
\widehat H=H_{LL}-H_{LE}H_{EE}^{-1}H_{EL},
\qquad
\widehat g=g_L-H_{LE}H_{EE}^{-1}g_E,
$$

$$
\widehat f_0=f_0-\tfrac12 g_E^TH_{EE}^{-1}g_E.
\tag{270.3}
$$

These are formulas in exact real algebra. They do not prescribe
forming the subtraction in floating arithmetic.

## 2. Exact equivalence and exterior response

**Theorem270-A.** For each u, the unique minimizer over all exterior
coordinates is

$$
v_*(u)=-H_{EE}^{-1}(g_E+H_{EL}u).
\tag{270.4}
$$

Writing

$$
\widehat f(u)=\widehat f_0+\widehat g^Tu+
             \tfrac12u^T\widehat H u,
$$

one has the exact completion identity

$$
f(u,v)=\widehat f(u)+
\tfrac12\bigl(v-v_*(u)\bigr)^T
H_{EE}\bigl(v-v_*(u)\bigr).
\tag{270.5}
$$

Moreover

$$
\widehat H\succeq\lambda^2 I.
\tag{270.6}
$$

Consequently the complete problem

$$
\min_z f(z)\quad\hbox{subject to }Bz+c\ge0
$$

and the condensed problem

$$
\min_u\widehat f(u)\quad\hbox{subject to }B_Lu+c\ge0
\tag{270.7}
$$

have the same infimum, and their minimizers correspond by
u -> (u,v_*(u)). If the feasible set is nonempty, each problem has a
unique minimizer. The exterior coordinates are the affine response
(270.4); they are not frozen to their raw direction or to zero.

**Proof.** H_EE is positive definite because it is a principal
submatrix of H. At fixed u, the exterior gradient is
H_EE v+H_EL u+g_E. Setting it to zero gives (270.4), and expanding
the square about that point gives (270.5) and the coefficients in
(270.3).

For any u, minimize the homogeneous quadratic over v. Completion
with g=0 gives

$$
u^T\widehat H u=
\min_v
\begin{pmatrix}u\\v\end{pmatrix}^{T}
H
\begin{pmatrix}u\\v\end{pmatrix}
\ge
\min_v\lambda^2(\|u\|_2^2+\|v\|_2^2)
=\lambda^2\|u\|_2^2.
$$

This proves (270.6). The inequalities depend only on u, so (270.5)
proves both directions of the minimization equivalence. A nonempty
closed feasible polyhedron and the coercive strictly convex
quadratic in (270.6) have a unique minimizer. Restoring the unique
exterior response proves the corresponding full uniqueness. QED.

This argument does not use a dense inverse. It identifies which
response an implementation must retain.

## 3. The affine term cannot be omitted from a square-root construction

Suppose an invertible square root R satisfies R^T R=H. The root alone
contains no record of g. Define h by the triangular equation

$$
R^T h=g.
\tag{270.8}
$$

Then

$$
f(z)=\tfrac12\|Rz+h\|_2^2+
      f_0-\tfrac12\|h\|_2^2.
\tag{270.9}
$$

**Proof.** Expanding the norm gives quadratic term H and linear term
R^T h=g; the stated constant cancels the additional norm of h. QED.

All later orthogonal eliminations must apply their transformations
to the affine column h as well as to the matrix columns. Eliminating
homogeneous R rows while omitting h would in general solve a
different quadratic.

An alternative exact description uses the true unconstrained center

$$
z_c=-H^{-1}g,\qquad u_c=(z_c)_L,
$$

for which

$$
\widehat g=-\widehat H u_c,\qquad
\widehat f(u)=f(z_c)+
\tfrac12(u-u_c)^T\widehat H(u-u_c).
\tag{270.10}
$$

This identity follows by applying the block equations for Hz_c=-g.
It requires the exact center. A computed center with a small
nonzero original residual cannot be declared an exact center and
used to erase the remaining linear term. Equation(270.8), with the
original g, is an affine construction that does not make that
assumption. Floating treatment is addressed in Section9.

## 4. Exact chain root and the actual support counts

Index the noninitial physical nodes by i=1,...,N. The current
values are

$$
n=338,\quad N=698,\quad d=112.
$$

Write the global border as w=(xi,p), with free-core coordinates
xi of dimension109 and scalar controls p of dimension3.
The actual root supplied by the R268 construction has energy

$$
\|Rz+h\|_2^2
=
\sum_{i=1}^{N}
 \|D_i z_i+S_i z_{i+1}+T_iw+h_i\|_2^2
+\|R_gw+h_g\|_2^2,
\tag{270.11}
$$

where S_N=0 and there is no z_{N+1}. Each D_i and R_g is upper
triangular and nonsingular in exact arithmetic, because R is a
nonsingular block upper triangular matrix.

The actual complete inequality support L consists of physical
nodes470 through482 and the three p coordinates. Hence

$$
\ell=(482-470+1)n+3=4397,
$$

while

$$
Nn+d=236036.
$$

The exterior set E contains physical nodes1 through469, physical
nodes483 through698, and all109 free-core variables. The latter
remain optimization variables until they are conditionally
eliminated. Keeping only p in the final condensed variable does
not hold the core fixed.

The root term R_g includes every pure-global remainder accumulated
in the original QR. It may not be dropped when the left chain is
eliminated. The complete h_g from (270.8) must also remain.

For this block root, (270.8) can itself be solved without forming a
dense R. Its physical forward equations are

$$
D_1^Th_1=g_1,\qquad
D_i^Th_i=g_i-S_{i-1}^Th_{i-1}\quad(i>1),
$$

followed by

$$
R_g^Th_g=g_w-\sum_{i=1}^{N}T_i^Th_i.
\tag{270.12}
$$

These equations use the original g=A^Tb, not a fabricated zero
linear term or a separately regularized physical RHS.

## 5. Elimination of the left exterior

Fix the retained physical variables and w. For i=469,...,1,
successively set

$$
z_i=-D_i^{-1}(S_i z_{i+1}+T_iw+h_i).
\tag{270.13}
$$

Every left physical square in (270.11) is then exactly zero.
No later physical row contains an earlier z_i, so those equations
do not change the retained rows.

**Lemma270-B.** The exact conditional minimum over physical
nodes1 through469 equals the sum of physical rows470 through698
and the unchanged global square. Its unique left response is
(270.13).

**Proof.** All removed summands are nonnegative. The displayed
back substitution makes all of them zero simultaneously, so the
remaining sum is the minimum. Nonsingular D_i gives uniqueness.
The global square contains w alone and is untouched. QED.

This is a completion statement for the affine rows Rz+h.
It would be incorrect to set homogeneous rows Rz to zero when
their affine h_i is present. It would also be incorrect to remove
the global square because its variables appear in removed
physical rows. The pure-global contributions from those rows
are already retained by R_g.

## 6. Reverse square-root elimination of the right exterior

Set r=482. Start at the final physical row with

$$
U_N=D_N,\quad V_N=T_N,\quad a_N=h_N.
$$

At a reverse step i=N,...,r+1, the two relevant row blocks are

$$
\begin{aligned}
&D_{i-1}z_{i-1}+S_{i-1}z_i+T_{i-1}w+h_{i-1},\\
&U_i z_i+V_iw+a_i.
\end{aligned}
$$

Their stacked squared norm can be written

$$
\left\|
\underbrace{\begin{pmatrix}S_{i-1}\\U_i\end{pmatrix}}_{F_i}
z_i+
\underbrace{\begin{pmatrix}
D_{i-1}&T_{i-1}\\
0&V_i
\end{pmatrix}}_{G_i}
\begin{pmatrix}z_{i-1}\\w\end{pmatrix}
+
\begin{pmatrix}h_{i-1}\\a_i\end{pmatrix}
\right\|_2^2.
\tag{270.14}
$$

The coefficient of z_i has full column rank. This follows from
positive definiteness of the conditional quadratic, equivalently
from the Schur complement of the original nonsingular physical
suffix. No inverse of U_i is needed.

Take an orthogonal O_i such that

$$
O_i^T F_i=\begin{pmatrix}K_i\\0\end{pmatrix},
$$

where K_i is nonsingular upper triangular. Apply that same
orthogonal transformation to all remaining columns and the
affine column:

$$
O_i^T
\left[
G_i\ \begin{pmatrix}h_{i-1}\\a_i\end{pmatrix}
\right]
=
\begin{pmatrix}
L_i&M_i&t_i\\
U_{i-1}&V_{i-1}&a_{i-1}
\end{pmatrix}.
\tag{270.15}
$$

Therefore the energy in (270.14) is exactly

$$
\|K_i z_i+L_i z_{i-1}+M_iw+t_i\|_2^2+
\|U_{i-1}z_{i-1}+V_{i-1}w+a_{i-1}\|_2^2.
\tag{270.16}
$$

Minimization over z_i removes the first square, with response

$$
z_i^*=-K_i^{-1}(L_i z_{i-1}+M_iw+t_i).
\tag{270.17}
$$

Induction gives one final retained row block
U_r z_r+V_rw+a_r. The rows470 through481 and the original global
row remain. Their total row and column count is

$$
13n+d=4506.
$$

If the reverse conditional factors are retained, the right exterior
is reconstructed in forward physical order483 through698 using
(270.17). Nothing in this operation fixes those variables to their
incoming warm values.

Every step preserves the original squared norm plus a nonnegative
conditional square. This supplies an energy invariant: after
eliminating any suffix, the new retained energy is the exact
conditional minimum over that suffix, and the discarded terms
are the conditional-completion squares. Applying the same
orthogonal matrices to the affine column proves the invariant for
the full quadratic, not just its Hessian.

## 7. Elimination of the109 free-core variables

After Sections5 and6, let the central affine root be

$$
\mathcal R
\begin{pmatrix}x\\xi\\p\end{pmatrix}+a,
$$

where x contains the13 retained physical nodes. Permute its
columns so that the109 core variables are first:

$$
K\,xi+D u+a,\qquad u=(x,p).
\tag{270.18}
$$

Here K has4506 rows and109 columns, and D has4506 rows and4397
columns. The central homogeneous quadratic is positive definite,
so K has full column rank.

Let K=U_c R_c be a thin QR, with orthonormal columns U_c and
nonsingular upper triangular R_c. Define the orthogonal projector

$$
P_c=I-U_cU_c^T.
$$

Then the exact conditional core response is

$$
xi_*(u)=-R_c^{-1}U_c^T(Du+a),
\tag{270.19}
$$

and the remaining energy is

$$
\|P_c(Du+a)\|_2^2.
\tag{270.20}
$$

**Proof.** Decompose Du+a into its orthogonal projections onto
Ran(K) and its orthogonal complement. The choice(270.19) cancels
the first component uniquely. The remaining component is
(270.20), and the Pythagorean identity gives the nonnegative
conditional-completion square. QED.

A full orthogonal completion of U_c gives a4397-by4397 local
square root and an affine vector. It is not necessary to form
that dense root. Directly from (270.20),

$$
\widehat H=D^TP_cD,\qquad
\widehat g=D^TP_ca.
\tag{270.21}
$$

The constant term also includes the scalar constant in (270.9).
All exterior variables have now been minimized exactly, so
Theorem270-A proves that these are exactly the Schur coefficients
in (270.3). In particular the resulting local Hessian remains
positive definite with lower bound lambda^2 in original z
coordinates.

The projector P_c is an orthogonal projector onto the complement
of the core-column range. It is unrelated to the physical-to-
material angular projection used in the boundary equations.

## 8. Recovery without retaining every reverse conditional factor

A second exact recovery formula can use the original complete
H inverse once per selected local candidate. Let E_L embed a local
vector in the complete coordinate space and define

$$
r_L(u)=\widehat H u+\widehat g.
$$

Solve

$$
H z=E_L r_L(u)-g.
\tag{270.22}
$$

**Lemma270-C.** The unique solution satisfies z_L=u and
z_E=v_*(u).

**Proof.** Its exterior block equation gives the response(270.4)
with its own local block z_L. Substituting that response in the
local block equation yields

$$
\widehat H z_L+\widehat g=r_L(u)
=\widehat H u+\widehat g.
$$

Invertibility of the condensed Hessian implies z_L=u. QED.

Thus one complete recovery solve can replace storage of all
reverse conditional factors. It does not require a complete H
inverse for every inequality row. This formula retains the
original g; it does not presume that a previously computed center
was exact.

An implementation must distinguish its exact algebra from its
rounded outputs. In particular if a numerical recovery yields a
small mismatch in z_L, the original all-row constraints must be
checked on the actually recovered full vector. Silently declaring
that vector equal to the requested u would not preserve the
finite calculation's identity.

## 9. Exact posterior control of a nonoptimal exterior response

For a given u and any returned exterior vector v, define its
original exterior gradient

$$
r_E=H_{EE}v+H_{EL}u+g_E.
$$

Equation(270.4) gives r_E=H_EE(v-v_*(u)). Hence

$$
\|v-v_*(u)\|_2\le\frac{\|r_E\|_2}{\lambda^2},
$$

and

$$
0\le f(u,v)-\widehat f(u)
=\tfrac12r_E^T H_{EE}^{-1}r_E
\le\frac{\|r_E\|_2^2}{2\lambda^2}.
\tag{270.23}
$$

These follow from H_EE>=lambda^2 I. They require the residual of the
original complete quadratic, not a preconditioned residual or the
residual of a different rounded root.

The complete KKT and cross-point posterior formulas in
[R263](R263-projected-KKT-and-damped-model-error.md) and
[R267](R267-two-point-damped-model-posterior-bound.md) also remain
available after restoring the full vector and original multipliers.
Theorems270-A through270-C introduce no replacement acceptance
test. Ordinary floating values of such bounds are not validated
enclosures unless their arithmetic error has separately been paid.

The actual QR source reports rounding, original-operator residuals
and memory-only factor identities. Those reports do not assert the
exact equality of a rounded R^T R to the exact-real H represented
by the original input. A future condensed implementation must
retain this distinction. In particular:

- It must use the original g=A^Tb or the complete affine
  construction(270.8), not erase a center residual.
- It must bind the exact current model inputs, scales, damping,
  factor-source identity and complete local support.
- The original full A/AT model action, all-row B action and
  nonlinear trial must be evaluated on the actual restored vector.
- Full QP optimality, full BVP acceptance and geometric conclusions
  do not follow merely from a successful condensed solve.

## 10. Work, storage and a minimal source interface

This section is an interface analysis, not an implemented or
benchmarked solver.

The current frozen factor object exposes the final factor arrays
`diagonal`, `upper`, `border` and `global_diagonal`, together with
its input/source identity and original-operator readbacks. These
are the arrays representing D_i, S_i, T_i and R_g in (270.11).
The caller must consume them before its existing `close()` clears
the factor. The original physical-input array named `R` inside the
class is not the final square-root factor.

A separate adapter can:

1. Bind the current full model and all4397 actual local indices;
   verify that every complete B row is represented on that support.
2. Obtain g from the original A^T b and solve the full triangular
   system(270.8), or retain equivalent exact affine data.
3. Leave the left prefix conditionally recoverable, perform216
   reverse physical eliminations, and preserve the complete R_g
   and h_g.
4. Build the4506-row central representation, eliminate only the109
   core columns, and expose the local Hessian/gradient through
   (270.21), with all p coordinates retained.
5. Supply the existing block-sparse local B actions without
   forming a dense full dual Gram.
6. Restore the outside response by the saved affine conditionals
   or one complete solve(270.22), and read the original complete
   objective, residuals and constraints on the actual result.

The reverse physical fronts have2n rows and n eliminated columns,
with n+d remaining variable columns and one affine column. The
work is of order (N-r)n^2(n+d). The thin core QR has4506 rows and109
columns. If D retains its chain-and-border layout, local actions
Dq, D^Tq and U_c/U_c^T actions need only the thirteen retained
physical blocks and the small core basis. They do not traverse
all236036 coordinates.

Explicitly storing one dense4397-by4397 double matrix would take
154668872 bytes, before extra work arrays. The projector form
(270.21) can avoid forming that matrix. The existing twelve-query
B rows occupy133496832 bytes and retain their local block layout;
a dense24576-by24576 dual matrix is unnecessary.

These counts do not establish an execution time, a particular
QP algorithm's convergence, or adequate memory under every
simultaneously retained artifact/factor configuration. A local
active-set, projected, primal-dual or other finite solver still
has to address all24576 inequalities. Condensation reduces the
dimension and cost of each model action; it does not itself
justify truncating the constraints to a prescribed number.

If the optional positive diagonal factor-column scale C is used,
the R268 factor satisfies R_C^T R_C=C^{-1}HC^{-1}. One may first
fold its columns back to R_bar=R_C C in original z coordinates,
or work consistently in t=Cz with g_t=C^{-1}g and
B_L C_L^{-1}t_L+c. Mixing the t root with untransformed B or g would
change the quadratic. The actual request40 configuration used
C=I.

## 11. What the current evidence supports

Request40 supplied a real example where complete-H inverse
residuals were small, the sixteen-row working subproblem had
small original stationarity and complementary products, yet1804
complete slacks were negative before a strong global repair.
That supports inspecting the already dispatched32-row continuation.
It does not establish that request42 fails, that a larger fixed
row count must fail, or that a new condensed solver should replace
the current experiment before its actual outcome is read.

The present theorem gives an exact alternative representation of
the same fixed finite quadratic if later full-row work warrants
it. It preserves all physical modes, all global controls, the free
core response, the original outside optimal response and every
inequality. It makes no claim about the original nonlinear
Darboux problem, true-tail solvability, same-metric refinement,
closed-surface construction, or the topic's completion criteria.
