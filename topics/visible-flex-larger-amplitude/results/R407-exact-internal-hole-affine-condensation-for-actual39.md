# R407. Exact internal-hole elimination for the actual39 complete affine QP

## Status and source boundary

This result specializes the arbitrary-support theorem already proved in
[R270](R270-exact-local-support-damped-QP-condensation.md) to the actual
noncontiguous support of the new39-query model. R270 does not require a
contiguous support in its general theorem. The frozen implementation
`root_20261114_complete_local_qp_condensation.py`, however, explicitly
requires a contiguous run of complete physical nodes. That implementation
condition is the concrete issue addressed here.

The new adapter is
[root_20261115_noncontiguous_local_qp_condensation.py](../computations/root_20261115_noncontiguous_local_qp_condensation.py),
13361 bytes, SHA256
`b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4`.
It changes support binding and the construction of the central affine
front. It inherits the complete affine solve, the original orthogonal
prefix routine, the subsequent free-core and local QR, all local actions,
and the original full-system recovery. Its source dependency is the
unchanged40393-byte original condensation source, SHA256
`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`.
The complete factor remains
`exact_20261114_regularized_block_qr.py`, SHA256
`596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`.

This is an exact-real algebra proof and a read source implementation
statement. There has been no new scientific execution, compile, import,
numerical verification, or actual39 result as part of this publication.
Public repository Actions must pay all actual numerical work. No new
fixture, scientific audit, line-search gate, or acceptance threshold is
introduced.

The motivation is the actual171 observation in
[R361](R361-actual171-real37-to38-sixteen-pairs-and-right459-barrier.md):
its last nearest rejected trial passed the selected38 linear rows and
decreased its own merit, but failed the real RIGHT-RMS459 nonlinear
domain. That observation does not give a new warm parent. Request191
starts independently from the actual98 original31 payload, preserves
the selected38 queries, and adds that complete RIGHT query. It does not
resume the deleted actual171 final field.

## 1. Original model and the exact support

Use the original scaled step coordinates \(z\), the same fixed complete
matrix \(A\), residual \(b\), and positive damping \(\lambda\):

\[
 H=A^TA+\lambda^2I,\qquad g=A^Tb,\qquad
 f(z)=f_0+g^Tz+\tfrac12z^THz,\qquad f_0=\tfrac12\|b\|^2.
 \tag{407.1}
\]

Thus \(H\succeq\lambda^2I\). The complete model still has236036
coordinates:698 noninitial physical nodes of338 coordinates each,
109 free-core coordinates, and3 scalar controls. The index convention
here is the physical one-based node number used by the original
complete factor and the query reports.

The actual39 operator retains22 LEFT and16 MID queries in their
original order and appends RIGHT-RMS459 at the original fraction
0.8273268353539885. Its real Hermite capture uses endpoints459 and460.
The exact union of complete physical blocks is

\[
 {\cal N}_L=\{459,460\}\cup\{462,463,\ldots,491\}.
 \tag{407.2}
\]

There are32 such physical nodes. Together with all3 controls,

\[
 |L|=32\cdot338+3=10819.
 \tag{407.3}
\]

Every one of the39 queries keeps all2048 angle rows, so the complete
inequality operator has79872 rows. The remaining4059-row constant
part and the original complete236036-column model retain their
meanings. No inequality row is discarded or replaced by an aggregate.

The338 coordinates of node461 are absent from \(L\) and belong to its
complement \(E\). They are still original optimization variables.
The other exterior coordinates are nodes1 through458, nodes492
through698, and the109 free-core coordinates. In particular,

\[
 B=(B_L,0_E),\qquad Bz+c=B_Lz_L+c.
 \tag{407.4}
\]

The new domain source is
`geometry_20261115_thirty_nine_query_domain_operator.py`,
SHA256
`0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d`.
Its complete source interface is published with request191. Here the
support in (407.2) is the contract to which the adapter is applied;
the adapter itself does not inspect or recompute the query rows.

Appending a zero B block for461 to the caller's local layout would
break the existing exact-support contract of
`geometry_20261114_condensed_local_inequality_qp.py`
(SHA256
`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`).
That library requires equality of its local index vector and the
actual domain index vector. The adapter leaves both vectors equal to
(407.2) plus the3 controls. The continuous cover below is only an
internal elimination device.

## 2. The complete affine front, including the hole

In exact arithmetic let \(R^TR=H\), and solve

\[
 R^Th=g.
\]

Then

\[
 f(z)=\tfrac12\|Rz+h\|^2+f_0-\tfrac12\|h\|^2.
 \tag{407.5}
\]

As in R270, every orthogonal transformation must act on the full
augmented matrix \([R\mid h]\). The pure-global root and its affine
column are part of this matrix.

The original factor stores a positively scaled root \(R_C\).
The unchanged affine implementation solves
\(R_C^Th=g/C\), componentwise for the positive scale \(C\), and folds
\(C\) back into every physical, neighbor, and border column:
\(\overline R=R_C\operatorname{diag}(C)\). Its complete original
linear-term residual is read back. This description identifies the
existing computation; it does not assert an exact identity between a
rounded factor and the exact \(H\) in (407.1).

First use the original elimination of the two exterior physical
chains with internal retained cover

\[
 {\cal N}_{\rm cover}=\{459,460,461,\ldots,491\}.
\]

The original left physical back substitution and right complete
orthogonal transformations conditionally minimize nodes1 through458
and492 through698. They leave all112 border variables, including the
109 free-core variables. Their entire pure-global remainder and the
whole original affine column remain.

The cover has33 physical nodes. The resulting original central front
has11266 rows and11267 columns, the last column being affine:

\[
 33\cdot338+112=11266.
 \tag{407.6}
\]

Its variable-column order is the109 free-core variables, the33
physical blocks in cover order, and the3 controls. The code invokes
the original contiguous binder only on this honest internal cover;
it then restores the actual caller's10819 local indices before the
original constructor records or saves those local indices.

The adapter preserves the cover dimensions until the original
central front has been completely built. It does not shorten the
allocation while the original physical and global rows are being
placed. All original physical couplings through461 are therefore
present before the additional elimination.

## 3. Conditional elimination of node461

Let \(x\in\mathbb R^{338}\) be the hole coordinates at node461, and
let \(y\) contain all remaining central variables, in the order

\[
 y=(\xi_{109},\ z_{{\cal N}_L},\ p_3).
\]

Permute only the variable columns of the complete central front so
that the338 \(x\) columns come first; leave the affine column last.
Write the resulting squared norm as

\[
 \tfrac12\|Kx+Dy+a\|^2.
 \tag{407.7}
\]

In exact arithmetic the central homogeneous form is positive
definite. This follows either from the successive conditional
minimization in R270 or by minimizing the original positive definite
form over the already eliminated coordinates. Consequently its
square root is nonsingular, and \(K\) has full column rank.

Choose an orthogonal \(Q\) giving the complete prefix transformation

\[
 Q^T[K\ D\mid a]=
 \begin{pmatrix}
  T&U&c\\
  0&S&d
 \end{pmatrix},
 \tag{407.8}
\]

where \(T\) is338 by338, upper triangular and nonsingular. The
transformation of \(D\) and \(a\) is the same \(Q^T\) used for \(K\).

**Proposition407-A.** For every fixed \(y\), the unique minimizing
hole value is

\[
 x_*(y)=-T^{-1}(Uy+c),
 \tag{407.9}
\]

and

\[
 \tfrac12\|Kx+Dy+a\|^2
 =
 \tfrac12\|T(x-x_*(y))\|^2+
 \tfrac12\|Sy+d\|^2.
 \tag{407.10}
\]

In particular the conditional minimum is exactly the remaining
affine squared norm \(\tfrac12\|Sy+d\|^2\).

**Proof.** Orthogonality in (407.8) preserves the complete squared
norm. Its upper338 components are \(Tx+Uy+c\), while all lower
components are independent of \(x\). Since \(T\) is invertible, its
upper components vanish at exactly (407.9). Substituting this value
or completing that square proves (407.10). QED.

Discarding the leading338 rows and338 columns *after* the complete
rotation therefore represents their conditional minimum. It does
not delete any original unrotated equation. It does not set \(x=0\),
\(g_{461}=0\), or its response to zero. It does not remove a border
or affine column. The constant \(f_0-\tfrac12\|h\|^2\) from (407.5)
is unchanged. All residual rows left after the rotation, including
any rows that no longer depend on physical variables, remain.

For the actual support, the remaining front has10928 rows and10929
columns:

\[
 11266-338=10928=109+10819.
 \tag{407.11}
\]

Its variable order is exactly109 free-core coordinates followed by
the actual10816 physical coordinates and3 controls. The original
constructor can now perform its unchanged109-core prefix
elimination and then its10819-dimensional local QR.

More generally the adapter accepts ascending complete physical
blocks with several missing interior blocks. It moves all missing
cover columns to the front and performs the same complete prefix
operation. If there are no missing blocks, it returns the original
central affine front unchanged. This is an interface generality;
the presently motivated use has the single hole461.

## 4. Equality with the original arbitrary-support Schur problem

Write \(u=z_L\), \(v=z_E\), using the true \(L\) from (407.2).
The coefficients of the exact reduced problem are still those of
R270:

\[
 \widehat H=H_{LL}-H_{LE}H_{EE}^{-1}H_{EL},
 \qquad
 \widehat g=g_L-H_{LE}H_{EE}^{-1}g_E,
 \tag{407.12}
\]

\[
 \widehat f_0=f_0-\tfrac12g_E^TH_{EE}^{-1}g_E,
 \qquad
 v_*(u)=-H_{EE}^{-1}(g_E+H_{EL}u).
 \tag{407.13}
\]

The completed root satisfies, in exact arithmetic,

\[
 \tfrac12\|\widehat R u+\widehat h\|^2+
 f_0-\tfrac12\|h\|^2
 =
 \widehat f_0+\widehat g^Tu+\tfrac12u^T\widehat H u.
 \tag{407.14}
\]

**Proposition407-B.** Eliminating the two exterior physical chains,
then the interior hole461, then the109 free-core coordinates gives
the same conditional minimum as minimizing over all of \(E\)
simultaneously. Every original inequality remains \(B_Lu+c\ge0\),
and \(\widehat H\succeq\lambda^2I\).

**Proof.** For each fixed \(u\), all the eliminated coordinates
range freely over their original real vector spaces. The strictly
convex coercive quadratic has a unique conditional minimizer.
Successive exact minimizations over a partition of those
coordinates have the same infimum as their joint minimization;
each step has the unique minimizer provided by its positive
definite square. Proposition407-A supplies the previously missing
interior step. The original R270 left, right and core steps supply
the other partitions.

No inequality involves an exterior coordinate, so these
minimizations do not change feasibility. Finally, applying the
same conditional minimization to the homogeneous quadratic gives

\[
 u^T\widehat H u
 =\min_v (u,v)^TH(u,v)
 \ge \min_v\lambda^2(\|u\|^2+\|v\|^2)
 =\lambda^2\|u\|^2.
\]

This proves the Hessian bound and the claimed equivalence. QED.

The displayed Schur subtraction is a characterization, not the
prescribed floating implementation. The adapter uses the original
complete square root and its orthogonal transformations.

## 5. Full recovery includes the hole and its original gradient

Let \(E_L\) denote the coordinate embedding from the true local
space to the complete236036-dimensional space. The exact recovery
identity from R270 remains

\[
 Hz=E_L(\widehat H u+\widehat g)-g.
 \tag{407.15}
\]

**Proposition407-C.** The unique solution of (407.15) has
\(z_L=u\) and \(z_E=v_*(u)\).

**Proof.** At \(z=(u,v_*(u))\) the exterior part of \(Hz+g\) is zero,
and its local part is \(\widehat H u+\widehat g\), by
(407.12)-(407.13). This vector satisfies (407.15). Positive
definiteness of \(H\) gives uniqueness. QED.

The inherited implementation starts its right-hand side with the
complete original \(-g\), then adds the condensed force only at
`self.local_indices`. Those are the true10819 indices. Therefore
the entire461 block of the recovery right-hand side remains
\(-g_{461}\). The original complete `solve_H`, and its mandatory
same-\(A\), same-\(A^T\) readback, are unchanged.

The returned full vector is used as actually recovered. Its local
coordinates are never overwritten with the requested \(u\).
The recorded local mismatch is retained. The exterior-gradient
diagnostic masks only the actual local coordinates, so it includes
all338 coordinates of461 together with every other exterior
coordinate. Original constraints, the original whole quadratic,
and nonlinear merit/domain evaluations remain based on that full
returned vector.

For an arbitrary actually returned pair \((\widetilde u,\widetilde v)\),
let

\[
 r_E=H_{EE}\widetilde v+H_{EL}\widetilde u+g_E.
\]

The exact a posteriori relations are

\[
 \widetilde v-v_*(\widetilde u)=H_{EE}^{-1}r_E,\qquad
 \|\widetilde v-v_*(\widetilde u)\|\le\|r_E\|/\lambda^2,
 \tag{407.16}
\]

\[
 f(\widetilde u,\widetilde v)-\widehat f(\widetilde u)
 =\tfrac12r_E^TH_{EE}^{-1}r_E
 \le\|r_E\|^2/(2\lambda^2).
 \tag{407.17}
\]

These are the existing R270 posterior statements. They apply at the
actually returned local coordinates, not automatically at the
requested \(u\). The inherited binary64 diagnostic values are not
validated enclosures. No extra acceptance test is created from
(407.16) or (407.17).

## 6. Source implementation and numerical scope

The adapter verifies the frozen original condensation source and
calls its original constructor. Its two substantive overrides are:

1. `_bind_support` checks complete ascending physical blocks and
   all3 controls, constructs the honest contiguous internal cover,
   invokes the original binder for that cover, and then sets the
   public local index vector and local dimension back to the actual
   support. It records every missing block, the complete column
   permutation, and both dimensions. No free-core coordinate becomes
   a local inequality coordinate.

2. `_central_front` first invokes the original method on the entire
   cover. It copies all variable columns in the recorded permutation
   and the affine column verbatim, invokes the inherited
   `_qr_prefix` on the missing physical columns, and takes only the
   fully rotated trailing affine block. Only after that operation
   does it change the live retained count and central dimension to
   the actual support dimensions. The original constructor then
   continues with its own core and local QR.

The original prefix routine uses its complete QR and applies the
corresponding orthogonal action to every trailing variable column
and the affine column. The existing finite-dimension, finite-value
and nonsingular-diagonal failure behavior is retained. The new
source is named in the report before the inherited constructor
forms the model identity; it does not claim to be the old source.

The updated actual39 warm source binds the adapter SHA alongside
the old condensation and original local-QP SHAs. The associated
observer binds the final warm source SHA
`568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9`.
Those request191 sources and their full request/workflow closure
are published in that independent entry. This proof does not
supply a hidden fallback to the old contiguous-only call.

Several numerical layers remain separate:

- the rounded complete factor and its relationship to the original
  \(A^TA+\lambda^2I\);
- the finite complete affine solve and its full linear-term
  readback;
- the extra338-column QR, its finite orthogonal transformations
  and the later109-core/local QR;
- the local root, local gradient, local optimization and possible
  nonzero original optimality residual;
- the complete recovery, its local mismatch and its original
  full-gradient readback;
- every original nonlinear query, domain, merit and fresh FD
  evaluation of the resulting field.

An exact identity for (407.1) does not merge these layers into an
IEEE word identity or a validated original-H error bound. The
adapter expressly records a new binary64 operation order. It does
not assert the same trajectory as the old38 model, the same
rounded condensed model as some different elimination order, a
QP optimum, or a successful nonlinear step.

The full cover and its copies increase actual memory and QR work.
Their real cost counts within the original entry's explicit
budgets. A started complete QR retains the original deadline
semantics and reports an overrun if it crosses the declared time.
There is no speed guarantee and no predeclared actual completion.
Temporary front identities and the necessary original diagnostics
belong to the same actual run. Regenerable matrices or raw
certificates are not committed, released, encoded into logs, or
uploaded as retained artifacts.

## 7. What this pays, and what remains

This result pays the exact internal-hole conditional-minimization
argument and its concrete complete-affine source adapter for the
actual39 support. It closes the specific contiguous-binder defect
without changing the true B layout or freezing461. It preserves
the original complete objective, all original inequality rows,
the original free-core response, and the complete recovery.

It does not pay request191's actual model or FD, any successful
new trial, a full nonzero112 field, native/fullDN/final audit,
the fixed450 reconstruction, a complete closed C² embedding,
same-metric error, held separation, Euclidean noncongruence,
reach, or the README's final refinement. Those remain the
unchanged responsibilities in [open.md](../open.md). The complete
topic remains unfinished and work continues after this
individually published conclusion.
