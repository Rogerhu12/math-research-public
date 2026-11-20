# R141 supplement: exact refinement and compact directed Gram propagation

2026-11-20, `visible-exact-astra-ac637-20261120`.

This supplement makes the first R141 certificate executable on the same
low193 comparison model already identified by the complete balanced
endpoint diagnostic `44721851908/1`.  The diagnostic remains a floating
diagnostic.  None of its propagation, QR, endpoint singular-value, or
matching singular-value targets is repeated or used as a directed bound.

The new owner is `fourfold_codazzi_low_centre_verified_green_owner.py`.
The additional pure module is
`fourfold_codazzi_low_centre_refined_green_math.py`.  It composes the
unchanged R141 core and the independently reviewed
`fourfold_codazzi_low_centre_shared_scalar_factors.py`.  Importing these
modules performs no scientific evaluation.  At registration only text,
AST, exact source hashes, and metadata construction have been checked.
No numerical inverse, residual, or point-transversality gate is asserted
to have passed by this supplement.

The completed centre-mean lower result `44727185157/1` is a whole read-only
input.  Its exclusion of the old small-centre sufficient recipe is
retained; neither that target nor the completed three original low-family
targets is recomputed.  Exclusion of that recipe does not imply singularity
of the actual operator and is not an inverse certificate.

## 1. The exact model is unchanged

Use the R141 order of raw coordinates: odd modes 1 through96, the independent
moving-phi even mean, and even modes 1 through96.  Set

\[
 N=193,\qquad p=97,\qquad q=96.
 \tag{C.1}
\]

The original155 comparison panels have true lengths \(h_i>0\).  The exact
comparison generator is

\[
 H_i=h_i^{\rm mid}A_i^{\rm mid},
 \tag{C.2}
\]

where both factors in (C.2) mean the **exact binary64 dyadic values** used to
define the successful prior model.  At the original320-bit definition
precision the owner materializes these values, checks every resulting
dyadic entry is exact, and reidentifies the entire published hash chain

`33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79`.

This is definition recovery, not a rerun of a completed bound.  The
comparison equation on panel \(i\) remains

\[
 x'=\bar A_i x+f,\qquad \bar A_i=H_i/h_i.
 \tag{C.3}
\]

In particular, a midpoint panel length never replaces the true physical
length in (C.3), integration, or a root coordinate map.

Let \(n_i^0\) be the complete prior equal-substep plan, with
\(\sum_i n_i^0=1424\).  Let \(b_i>0\) be the exact dyadic value of its saved
`q_balance`, and set

\[
 B_i=\operatorname{diag}(I_{96},b_iI_{97}).
 \tag{C.4}
\]

At768 bits the new owner forms a directed upper \(\mu_i\) for
\(\|B_iH_iB_i^{-1}\|_\infty\).  It starts with \(n_i=n_i^0\).  If the
directed comparison \(\mu_i\le4n_i\) is not established, it doubles that
parent's \(n_i\) once and checks the comparison again.  It requires

\[
 \mu_i/n_i\le4\quad\hbox{for every original panel},\qquad
 m:=\sum_i n_i\le1536.
 \tag{C.5}
\]

All of this plan is resolved before carrier propagation.  A failed guard
is an incomplete calculation with its complete prefix saved, not an
omitted panel or a changed matrix norm.  Every old cut is retained because
the only allowed change is an exact doubling.

The refined cell \(\nu=(i,k)\), \(0\le k<n_i\), has normalized coordinate
\(u\in[0,1]\) and exact map

\[
 \tau=(k+u)/n_i,\qquad
 h_\nu=h_i/n_i,\qquad H_\nu=H_i/n_i.
 \tag{C.6}
\]

Consequently \(H_\nu/h_\nu=H_i/h_i\), and the inserted transmissions are
raw identity transmissions.  The raw comparison BVP is exactly (C.3).
When \(n_i\) is not a power of two, \(H_\nu\) is an exact rational matrix,
not necessarily a dyadic matrix.  The implementation encloses that
unambiguous rational definition with directed division; it does not
replace it by its Arb midpoint.

`RefinedDomain` maps every box and both endpoints by (C.6), including the
variable-root collar.  `RefinedContext.centre_matrix` passes the mapped
original box to the same original coefficient provider.  The original
coefficient packets are retained.  **The new cuts do not narrow those
coefficient balls.**  The defect source is always

\[
 W_\Delta(r)=
 \bigl(A_L^c(r)-H_\nu/h_\nu\bigr)S_\nu^{-1}.
 \tag{C.7}
\]

The actual object is the same WVC hybrid centre, whose principal eta is
the original full-family eta and whose lower coefficients are those of
the repaired centre.  It is not silently identified with
\(DF(Q_{\rm repair})\).

## 2. Reference charts and exact boundary columns

At every one of the \(m+1\) true nodes, the existing same-reference scalar
provider encloses \(p_j,H_j\), \(1\le j\le96\).  Their binary64 midpoint
values only define new exact trial parameters \(p_j^t,H_j^t\).  Set

\[
 K_j^t=1-p_j^tH_j^t,\qquad
 T_j=\begin{pmatrix}K_j^t&-p_j^t\\H_j^t&1\end{pmatrix}.
 \tag{C.8}
\]

The mean column is the identity.  Interior blocks have determinant one
as exact rational matrices.  At the root replace the first column of each
block by \((1,0)^T\); at the outer boundary replace its second column by
\((-13/80,1)^T\).  The latter uses an exact rational, not a dyadic claim.
The resulting block determinants are checked to have positive directed
lower endpoints.  The first97 root columns and last96 outer columns are
therefore precisely the original homogeneous boundary carriers.

The actual AL propagation and singular-value diagnostic are not invoked
to obtain these charts.  The scalar reference point cache is cleared
after each node, so the chart proposals do not retain137000 mode/point
enclosures.  Only two binary64 parameters per mode/node are stored.

The pure module applies \(T\) and \(T^{-1}\) by their explicit2-by-2
blocks.  For \(d=K+pH\),

\[
 T^{-1}=d^{-1}\begin{pmatrix}1&p\\-H&K\end{pmatrix}.
 \tag{C.9}
\]

This avoids repeated full193-square inversion of fixed block charts.
There is no approximation in (C.9).

## 3. Streaming two-sided graph propagation

The R141 forward graph \(Z_\nu\in\mathbb R^{96\times97}\) starts at zero
at the root.  For

\[
 E_\nu=T_{\nu+1}^{-1}e^{H_\nu}T_\nu,
 \quad U_\nu=E_{11}+E_{12}Z_\nu,
 \tag{C.10}
\]

compute \(C_\nu=U_\nu^{-1}\) and

\[
 Z_{\nu+1}=(E_{21}+E_{22}Z_\nu)C_\nu.
 \tag{C.11}
\]

The backward graph \(Y_\nu\in\mathbb R^{97\times96}\) starts at zero at
the outer endpoint.  With
\(\widehat E_\nu=T_\nu^{-1}e^{-H_\nu}T_{\nu+1}\), set

\[
 V_\nu=\widehat E_{21}Y_{\nu+1}+\widehat E_{22},\qquad
 D_\nu=V_\nu^{-1},\qquad
 Y_\nu=(\widehat E_{11}Y_{\nu+1}+\widehat E_{12})D_\nu.
 \tag{C.12}
\]

Every inverse is an actual finite directed inverse with all entries
checked finite.  A pseudoinverse is never used.  For fixed parent \(i\),
all its \(H_\nu\) are identical; thus the forward pass computes
\(e^{H_i/n_i}\) once, and the backward pass computes
\(e^{-H_i/n_i}\) once.  These exact propagators are reused only within that
parent.  Each node's distinct charts and signed carriers are still used.

For the joined frame write

\[
 F_\nu=T_\nu
 \begin{pmatrix}I&Y_\nu\\ Z_\nu&I\end{pmatrix}=(L_\nu,R_\nu).
 \tag{C.13}
\]

Instead of a193-square inversion at every node, certify
\(W_\nu=(I-Z_\nu Y_\nu)^{-1}\), a96-square inverse.  The exact block
identity gives

\[
 F_\nu^{-1}=
 \begin{pmatrix}
 I+Y_\nu W_\nu Z_\nu&-Y_\nu W_\nu\\
 -W_\nu Z_\nu&W_\nu
 \end{pmatrix}T_\nu^{-1}
 =\binom{\ell_\nu}{\rho_\nu}.
 \tag{C.14}
\]

Multiplying the blocks verifies both sides of (C.14); in particular no
auxiliary frame-nullspace is being overlooked.  The same mixed-boundary
comparison BVP of R141 is invertible once these complete directed checks
succeed.  This is only the comparison BVP at this stage.

The forward pass stores the current \(Z\) enclosures and all \(C\).  The
backward pass keeps only the current \(Y\), constructs and stores
\(L,R,\ell,\rho\), and deletes each consumed \(Z\).  It also stores all
\(D\).  There is no all-node list of Python Arb matrices.

## 4. Compact matrix enclosures are outward enclosures

For each finite Arb entry \(a\), the storage procedure chooses a finite
binary64 midpoint \(m\) and reconstructs its exact dyadic value \(m_*\)
by its integer ratio.  It then obtains the directed nonnegative point

\[
 e=\sup|a-m_*|.
 \tag{C.15}
\]

A finite binary64 \(r\ge0\) is proposed.  Its exact dyadic value \(r_*\)
must satisfy the directed comparison \(r_*\ge e\).  If needed, the
proposal is moved upward by `nextafter`, with a fixed guard on the number
of attempts.  Failure saves an incomplete prefix.  Every accepted pair
therefore proves

\[
 a\subseteq[m_*-r_*,m_*+r_*].
 \tag{C.16}
\]

The private array stores exactly two8-byte binary64 values per entry.
Unpacking reconstructs the two exact dyadics and their enclosing interval
at the working precision.  It does not infer an error from a heuristic
number of significant digits.  All future recurrences consume these
enclosures, so every storage enlargement is paid.  In particular the
forward graph propagates its packed enclosure at the next step.

The operation is not a floating certificate: (C.16) is checked for every
entry using Arb, and all matrix inverses, exponentials, products,
covariances, and final comparisons use whole directed enclosures.  The
matrix of stored midpoints need not be PSD.  Positivity in a Gram argument
belongs to the exact matrix enclosed, never to that midpoint matrix.

`PackedMatrices` enforces an8GiB live payload cap and a200000-entry
decoded-matrix cache cap.  Packed arrays remain private in memory and are
never written to disk or published.  Scalar results record the number of
entries and the identical number of passed containment guards.

## 5. Local factors: common scalar and exact parent reuse

Within each refined cell use exactly four integration boxes.  In its
\(j\)-th box,

\[
 u=(2j+1+t)/8,\qquad -1\le t\le1,\qquad
 D=B_iH_\nu B_i^{-1}/8.
 \tag{C.17}
\]

By (C.5), \(\|D\|_\infty\le1/2\).  The shared-scalar supplement supplies
the exact finite signed Taylor terms through order16 and the entrywise
positive exponential tail for all omitted powers.  The common scalar is
preserved through each finite power; no wide-interval matrix exponential
is called.  The tail is computed and retained regardless of how small it
appears.

The implementation computes three point-matrix exponentials per parent
template: \(e^D,e^{-D},e^{|D|}\).  The latter uses the directed entrywise
majorant specified in the shared-scalar proof.  The remaining constants
are the signed and positive factorial powers and the complete variation
enclosure.  All these depend only on

\[
 (i,n_i,\text{four integration boxes},\text{order16},B_i,H_i).
 \tag{C.18}
\]

They are identical for all refined cells of that original parent and can
be reused exactly.  The cache key contains the parent and subdivision
count and the fixed integration/order parameters; the model token fixes
the original generator and balance.  Only one parent template is live.

For each distinct refined cell, the method reads its own complete signed
\(L_\nu,R_\nu,\ell_\nu,\rho_\nu\) and forms fresh midpoint columns and
rows.  Its four-box cache retains only the corresponding output matrix,
midpoint row matrix \(Y\), and signed product \(YV\), where \(V\) is the
complete local variation enclosure.  For **every source role and box**,
the raw source \(W(r)\) is freshly requested from the same original
provider and the factor is enclosed by

\[
 YB_iW+(YV)B_iW.
 \tag{C.19}
\]

No actual defect, correction, or high-return source is cached under the
identity of a different source.  Actual \(S_i\) remains in
\(S_iB_i^{-1}\) on the output; the trial \(B_i\) does not replace it.
The parent template never contains a cell's carrier or its actual source.

## 6. The complete Gram recurrences are unchanged

Use the R141 exact local factor notation \(O_L,O_R,I_L,I_R\).  Every
refined cell contributes the complete whole-box integrals

\[
 P_L=\int I_LI_L^*\,dr,\quad P_R=\int I_RI_R^*\,dr,
 \quad Q_L=\int O_L^*O_L\,dr,\quad Q_R=\int O_R^*O_R\,dr.
 \tag{C.20}
\]

All four boxes, their true masses, both cross-box orders, and both
same-box triangles of area \((h_\nu/4)^2/2\) are retained.  Refinement does
not discard interactions across inserted cuts; those occur in the R141
covariance recurrences using \(C_\nu,D_\nu\).

`complete_gram_norm_packed` implements exactly

\[
 A_0=0,\qquad A_{\nu+1}=C_\nu^*(A_\nu+Q_{L,\nu})C_\nu,
\]
\[
 B_m=0,\qquad B_\nu=Q_{R,\nu}+D_\nu^*B_{\nu+1}D_\nu.
 \tag{C.21}
\]

The root carry starts at \((R_aL_0)^*(R_aL_0)\) and is advanced by
\(C_\nu^*(\cdot)C_\nu\).  The outer carry starts at
\((\Theta R_bR_m)^*(\Theta R_bR_m)\) and is advanced backward by
\(D_\nu^*(\cdot)D_\nu\).  The complete body sum uses

\[
 \operatorname{tr}(A_\nu P_{L,\nu})+
 \operatorname{tr}(D_\nu^*B_{\nu+1}D_\nu P_{R,\nu})
 \tag{C.22}
\]

plus both local triangles.  Root97 and outer96 contributions are added
separately, exactly as in R141.  The outer covariance is released after
its complete norm has been formed.  Only the defect's body output
covariances remain for the later point certificate.

The exact \(Q_L,Q_R\) depend only on the model and actual \(S\), not on
the source.  One complete pair of their enclosures per cell is therefore
shared by all five roles.  Each role retains its own complete \(P_L,P_R\)
and both triangle bounds.  Reusing \(Q\) is a reuse of the same exact
integral with a valid whole enclosure, not an assumption that different
sources have the same covariance.

The point-receiver recurrences likewise remain

\[
 L_m^s=0,\quad L_\nu^s=P_{L,\nu}+C_\nu L_{\nu+1}^sC_\nu^*,
 \qquad
 R_0^s=0,\quad R_{\nu+1}^s=D_\nu(R_\nu^s+P_{R,\nu})D_\nu^*.
 \tag{C.23}
\]

They use the same defect packets and the same model token.  The unchanged
whole-box projection formula consumes their lazy decoded enclosures and
the complete body-only \(A,B\).  It covers every real point, not only
the newly inserted nodes, and never takes the trace of an arbitrary
\(L^2\) input.

## 7. Branch order, saved bounds, and limits of the claim

The owner first completes the exact comparison Green object, then the
entire true coefficient-defect body and193-atom bounds.  Each scalar is
saved as a complete integer decimal ball using `mid_rad_10exp(48)`.  The
strict condition is checked using the upper endpoint obtained by reading
that complete saved decimal ball:

\[
 \varepsilon<1.
 \tag{C.24}
\]

The enlarged saved upper is also the epsilon consumed by every subsequent
actual-source and point formula.  A favorable hidden unrounded epsilon
is not substituted for the published one.

If (C.24) is false, the declared branch has exactly two complete targets
and no actual-low inverse claim.  It does not infer singularity.  If it is
true, the owner forms the four remaining source packet families together,
one refined cell at a time, to share the parent and local-box constants:

1. ordinary raw \(L^2\) forcing;
2. transformed \(L^2\) forcing;
3. the full low second-kind correction \((A_L^c-D_f)S^{-1}\);
4. the actual centre low-from-high0 return source, without CFB.

Their complete norm conclusions are then formed and saved in the declared
order.  After each is consumed, its private source packets and norm
covariances are freed.  Finally all \(4m\) whole point boxes are evaluated
for actual weighted/raw projection bounds and the resulting positive
matching-angle lower.  The seven-target branch is complete only when
every one of these operations succeeds.

All original root97 and outer96 output atoms, including the independent
moving-phi mean, remain in the same Hilbert block.  This does not grant a
new physical-density/theta mean interpretation.  Input atoms are still
handled by the identity block in the R141 second-kind formula.

Neither branch proves the full CFB centre, the actual positive-family
inverse, the original finite \(Q_f/J_\rho\) bridge, the seven original
input ports, or either original RHS.  Those obligations are explicitly
false/unpaid in every result.  A successful low193 certificate supplies
the concrete inverse needed to test the complete high feedback; failure
of that loop may still require the full609 endpoint system of R137.

## 8. Capacity and operation plan

One matrix entry in the compact private payload costs16 bytes.  The
following counts are exact payload counts, not measured resident-memory
claims.  Put \(s=p^2+q^2=18625\).

| Live objects | Entries |
|---|---:|
| All node \(L,R,\ell,\rho\) and all \(C,D\) | \(2N^2(m+1)+sm\) |
| Five source \(P_L,P_R\) families and shared \(Q_L,Q_R\) | \(6sm\) |
| Retained defect output covariances | \(s(m+1)\) |
| Current other-source \(A,B\) and outer covariance | \((p^2+2q^2)(m+1)\) |

At \(m=1424\), their combined payload is5,728,443,200 bytes.  At the
declared1536-cell cap it remains below the8GiB payload guard.  The forward
temporary \(Z\) history is deleted during the backward pass, before
source packets are formed; it does not add to that peak.  Later point
source covariances are formed after the four other source families have
been freed.

Decoded Arb matrices use a200000-entry LRU cache.  Temporary full matrices,
the current graph, four current-cell factor boxes, and one parent template
are bounded separately by the fixed193-dimensional local operations.
The155 exact parent generators and original admitted context remain live.
The owner monitors Linux scientific-process peak RSS and enforces a14GiB
cap in addition to the8GiB payload guard.  A cap failure is reported with
its full current prefix.  No claim of actual memory consumption is made
until the public run supplies it.

The graph propagation needs310 point matrix exponentials: two per original
parent.  Each complete local-factor pass needs465: three per original
parent.  Thus the two-target branch needs at most775 such exponentials
(310+465).  The seven-target branch needs at most1705
(310+3·465): defect packets, the four-role packet pass, and point
observations.  Scalar reference-chart proposal evaluations are separate.
Every source, refined cell, and whole integration box is still evaluated.
The repeated constant exponentials eliminated by (C.18) are not new
mathematical targets and do not remove any contribution.

The fixed public runtime is Python3.12.14 and python-flint0.9.0.  Original
admission and model definition remain at320 bits; the new certificate is
at768 bits.  No NumPy/SciPy propagation is imported or executed.  The
scientific wall guard is16800 seconds, the child limit20100 seconds, and
the workflow limit350 minutes.  All work occurs in the repository's own
public Actions workflow.  Only one complete small outcome and its normal
execution/report receipts are published; no private matrix arrays or
separate artifacts are created.

For the underlying exact-midpoint, decimal-enclosure, directed
matrix-exponential and inverse APIs, see the primary documentation pinned
in the manifest:

- <https://python-flint.readthedocs.io/en/stable/arb.html>
- <https://python-flint.readthedocs.io/en/latest/arb_mat.html>
- <https://python-flint.readthedocs.io/en/latest/build.html>
- <https://flintlib.org/doc/arb_mat/arb_mat_exp.html>

These API references describe the runtime operations.  They do not assert
that this candidate's new mathematical gates will pass.
