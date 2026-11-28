# Complete polynomial row-operation right return and a native cyclic candidate

Date: 2026-11-28 UTC.

## 1. Scope and fixed inputs

This note accompanies the isolated files
**original_row_operation_right_return.py** and
**check-original-row-operation-right-return.py**.

The module does not compute a new Hermite form, bind a production engine, or
change the current v15 run. It consumes the entire same-invocation polynomial
matrices and the actual coefficients of the recorded row operations. The
software checker uses fixed small examples only. No software PASS, original
geometric PASS, rank-306 speed improvement, or total peak-memory bound is
asserted before an actual public Actions receipt.

Write \(R=k[t]\), where \(k\) is the caller's unchanged original finite field.
The fixed original pair-reset source is
**original_pair_reset_row_reduction.py**, SHA256
ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f.
The fixed original full polynomial left division is
**original_polynomial_row_reduction.py**, SHA256
9e3413176d9cce5fa00836ee05ea450483c60a786407b40fcef2ae226f009936.

The accepted square matrices are \(M,P,H,C\in R^{n\times n}\). The input \(M\)
is the complete original denominator multiplication matrix. The recorded
operations \(E_1,\ldots,E_s\) have the asserted intermediate return

\[
P=E_s\cdots E_1M,\qquad H=CP.
\tag{1}
\]

The caller must retain all coefficients, rows and nilpotent lengths. A digest
does not reconstruct an operation and is never used as a substitute for its
coefficients. The transient transcript is not serialized as a mathematical
cache.

## 2. Exact reverse-right return

Starting at \(C\), replay the original operations in reverse chronological
order, each time multiplying on the right. The result is

\[
U=CE_s\cdots E_1,\qquad UM=H.
\tag{2}
\]

The complete right-action formulas follow by multiplying the corresponding
elementary matrices. In the table \(u_i,u_j\) are the old columns.

| Original simultaneous row operation | Right multiplication on the current columns |
|---|---|
| Swap rows \(i,j\) | Swap columns \(i,j\) |
| Row \(i\leftarrow i+f\,j\) | Column \(j\leftarrow u_j+f u_i\) |
| Row \(i\leftarrow c\,i\), \(c\in k^\times\) | Column \(i\leftarrow c u_i\) |
| Rows \((i,j)\leftarrow(a i+b j,c i+d j)\), \(ad-bc=1\) | Columns \((i,j)\leftarrow(a u_i+c u_j,b u_i+d u_j)\) |

Both outputs in the last line must use both **old** columns. Updating the
first column before computing the second would be incorrect.

The pinned original Bézout record is \((s,t,-v,u)\), with \(su+tv=1\).
Consequently its right return is
\((s u_i-v u_j,t u_i+u u_j)\). This is not forward replay and is not left
multiplication of \(C\).

The module admits only the exact original kinds swap, add, scale and bezout,
with their full arities and distinct row indices. It rejects a nonconstant
or zero scale and a Bézout block whose determinant is not one. The sealed
transcript contains the actual same-ring polynomials. Its canonical hash is
recomputed before consumption to detect a changed transcript. This hash is
supplementary evidence, not the mathematical return.

## 3. Complete acceptance gates

The public return checks all of the following in the unchanged coefficient
ring:

\[
H\text{ is monic full upper HNF},\quad
CP=H,\quad UM=H,\quad
\operatorname{rem}_H(M)=0.
\tag{3}
\]

The remainder is obtained from the current
**original_ys_divisor_ideal_tools._hermite_remainder_rows** entry point, so an
already installed native complete-return wrapper is honored. Products use
the current complete product wrapper when bound. There is no residue-field
projection, rational-function inverse, clearing of denominators, or omitted
coordinate.

The equation \(UM=H\) proves
\(\operatorname{row}_R(H)\subseteq\operatorname{row}_R(M)\).
The complete remainder proves the reverse inclusion. Thus the returned HNF
is the complete original module, and the monic determinant and length
\(\deg\prod_iH_{ii}\) include every nonreduced factor.

Even an incorrectly supplied intermediate \(P\) cannot pass merely by
matching a determinant. The replay construction gives \(U=CE_s\cdots E_1\).
Since \(H=CP\) is nonsingular, \(C\) is nonsingular over \(k(t)\). Equations
(2)--(3) therefore imply

\[
C(E_s\cdots E_1M-P)=0
\quad\Longrightarrow\quad E_s\cdots E_1M=P.
\tag{4}
\]

This cancellation is a proof only; the software does not invert \(C\).

Private scratch matrices and vectors are explicit copies. Input values and
mutability are preserved. The resource object limits actual operation
count, stored polynomial-coefficient cells, retained column/output cells,
scalar column updates, and optionally elapsed time. Those are configurable
work budgets, not a mathematical dimension cutoff. Intermediate scalar
products, matrix serialization, native workspaces and preexisting caller
objects prevent these counters from being a total process peak-memory bound.

## 4. Software capture is the pinned original algorithm

The checker authenticates all 15 original dependency files. It copies the
source of the pinned original reducer into an isolated namespace and inserts
one call into its nested record function. That call stores the same actual
coefficients whose digests the original code already records, including the
exact original-field embedding after whole prime-subfield descent.

Removing the inserted statement and restoring the local function name must
give the original source **byte for byte**. In full mode every arithmetic
statement is unchanged. In prefix mode the source ends only after the
original complete whole-unshifted-Popov stage; the added return reports the
whole matrix and verifies every column bound. No original module function is
rebound.

The checker compares complete \(H,U,C\), every product and the determinant
length against the untouched original reducer, the untouched full
polynomial left-division routine, and Sage's complete transformation return.
The exact Sage 10.6 oracle signature is
hermite_form(self, include_zero_rows=True, transformation=False).
With transformation=True it returns the pair \((H,U)\) with \(UM=H\).
Its is_hermite default is row_wise=True, lower_echelon=False, namely the
same monic upper row HNF used here. The implementation makes a private copy,
runs its Euclidean Hermite algorithm with monic normalization, and freezes
the returned \(H,U\). Thus the checker's explicit copy(M) call and both
keyword arguments are supported; no reversal matrix belongs in this
independent oracle call. The reversal used by the separate function-field
routine has a different API and is not imported here.

This was verified in
[matrix_polynomial_dense.pyx, Sage 10.6](https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_polynomial_dense.pyx),
Git blob f1f6ac44e54ac7446850969d4bf88f5bbfb62132,
218464 bytes, SHA256
a4e90baf42706a9b842558af1087dba87362f09d36c53978495365737f88b127.

The examples include:

- A genuine complete Popov basis which is not Hermite.
- Nonprime quadratic coefficients and an immutable caller matrix.
- Repeated irreducible primary factors.
- Exact whole prime-subfield descent and the original prime coefficient ring.
- The second original quadratic characteristic.
- Unit determinant.
- A source forcing the original simultaneous Bézout extraction.
- The same return after installing the actual native complete-return wrapper.

The rejection cases include changed complete \(P,C,H\), a wrong full module
with the same determinant, a false empty operation transcript, a changed
sealed coefficient, wrong rank or ring, invalid operations, and an
insufficient actual work budget.

A fixed request has a 420-second software budget. Its fixtures are small;
neither the helper's interface nor its mathematics has a quotient-length
cutoff of 256. The test does not execute the original geometric input.

## 5. Why the original Popov checkpoint can support a whole quotient

The actual pinned popov routine is stronger than weak Popov. After distinct
leading positions it reduces every other entry in every pivot column, sorts
the pivot rows, and checks

\[
P_{jj}\text{ monic of degree }d_j,\qquad
\deg P_{ij}<d_j\quad(i\ne j).
\tag{5}
\]

The original row leading-position checks are also retained. Thus the full
quotient has the standard monomial basis

\[
\mathcal B=\{t^a e_j:0\le a<d_j\},\qquad
\delta=\sum_jd_j.
\tag{6}
\]

No nilpotent factor is removed. Multiplication by \(t\) shifts a basis
monomial except at a column boundary. At that boundary, replacing
\(t^{d_j}e_j\) with
\(-\bigl(P_j-t^{d_j}e_j\bigr)\) is already a full normal remainder by (5).
This one-step statement uses the complete column reduction; distinct
leading positions alone would not suffice. Columns with \(d_j=0\) are
handled by reducing \(e_j\) with the corresponding whole row of \(P\).

The current files implement only the reusable final return (1)--(4).
They do not claim that quotient construction or a subsequent Krylov
algorithm is already a tested production optimization.

## 6. Conditional cyclic gate and native implementation route

Let \(T\) be multiplication by \(t\) on (6), and let
\(e=\operatorname{rem}_P(e_{n-1})\). The proposed gate is the **complete**
rank of the matrix with columns

\[
K=(e,Te,\ldots,T^{\delta-1}e).
\tag{7}
\]

If and only if all \(\delta\) columns are independent, solve simultaneously
for \(T^\delta e\) and every \(\operatorname{rem}_P(e_i)\). This yields a
monic degree-\(\delta\) relation \(q(T)e=0\) and polynomials
\(\deg f_i<\delta\) with \(\operatorname{rem}_P(e_i)=f_i(T)e\).

Then the complete upper HNF candidate consists of

\[
e_i-f_i(t)e_{n-1}\quad(0\le i<n-1),\qquad
q(t)e_{n-1}.
\tag{8}
\]

It has quotient length exactly \(\delta\), and every row has zero complete
remainder modulo \(P\). This proves equality of the two modules, including
nilpotents. A complete polynomial division of these rows by \(P\) gives
\(C\), after which (2)--(4) certify the original \(U\) and all original
denominator returns. If (7) is singular this special gate simply does not
apply; it does not license dropping quotient coordinates or changing the
generator. No cyclicity assertion has been made about the actual MD.

There is a fixed Sage 10.6 native route for the prime-field case. Its source
matrix_modn_dense_template.pxi implements
echelonize(algorithm="linbox_noefd") by FFPACK, returning the complete rank
and pivot information. For GF(29),
matrix(..., implementation="linbox") uses the contiguous
Matrix_modn_dense_float representation. A single augmented native echelon
calculation on \([K\mid T^\delta e\mid e_0\mid\cdots\mid e_{n-2}]\) can certify
the cyclic gate and solve all right-hand sides. The returned coordinates
must still pass the full original-ring products, divisions and replay.
This is not a randomized minimal-polynomial assumption.

The exact reviewed 10.6 sources are:

- [matrix_modn_dense_template.pxi](https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_modn_dense_template.pxi),
  Git blob 74198ed0e57a481ec87a2ea777c88e5849845e35,
  SHA256 3a1a5c768678504d56a927c4b31224d7735890da0f9d5fc5f2d3d4af4ac6a2a7.
- [matrix_modn_dense_float.pyx](https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_modn_dense_float.pyx),
  Git blob 13dedf8441cd76213b155029baa7ec889f1d6827,
  SHA256 36f67504e5bf3cd161826e2cd941bccf59b96e90193fe523fb1dd4b68fc02d0b.

At the observed earlier \(\delta=3670,n=306\), one native float square
matrix uses about 54 MB of coefficient storage and the indicated augmented
matrix about 58 MB. Those figures exclude copies, the sparse multiplication
operator, native workspaces, polynomial matrices, and the replay transcript.
A dense Python/Sage-object matrix is not the proposed storage. Construction
of the Krylov columns and the whole polynomial coordinate return may still
be substantial; no timing or production feasibility is inferred from the
storage estimate.

## 7. Optional exact scalar-content reduction

The reviewed original reducer and current official denominator helper do
not extract a common polynomial content from all entries of MD. The
fraction normalizer's common scalar cancellation between numerator and
denominator is a different operation.

If a future invocation computes the **actual** monic content \(h\ne0\) of
all entries and verifies \(M=hM_0\), it may calculate
\(H_0=UM_0\), then return

\[
H=hH_0,\quad UM=H,\quad
\deg\det H=n\deg h+\deg\det H_0.
\tag{9}
\]

The complete column HNF bounds remain true after multiplication by \(h\).
All thick factors of \(h\) are retained in the returned matrix. The original
input remainders and all \(XMD=YMN\) identities must still be checked against
the original \(MD\). If a transcript was produced for \(M_0\) with
\(P_0=E_s\cdots E_1M_0\), the original intermediate is \(P=hP_0\);
\(C\) and \(U\) do not change. This is compatible with (1)--(4).

There is a cheaper complete content certificate within the actual
normalization. Let \(D=(D_1,\ldots,D_n)\) be the original denominator's full
integral coordinates, let \(M_D\) be its complete multiplication matrix,
and let \({\bf 1}\in R^n\) be the caller's actual unit coordinates. The
original multiplication table has coefficients in \(R\), and it gives

\[
{\bf 1}M_D=D.
\tag{10}
\]

If \(h_D\) is the monic gcd of all \(D_i\), then \(D=h_DD_0\) with
\(D_0\in R^n\), and linearity of the **same** complete multiplication table
gives \(M_D=h_DM_{D_0}\). Therefore \(h_D\) divides every entry of \(M_D\).
Conversely, the monic gcd \(h_M\) of the entries of \(M_D\) divides every
coordinate of \({\bf 1}M_D=D\). The two monic contents are exactly equal:

\[
\gcd(D_1,\ldots,D_n)=\gcd\{(M_D)_{ij}:1\le i,j\le n\}.
\tag{11}
\]

The proof does not assume that the first basis vector is the unit. It uses
the complete original unit vector \({\bf 1}\), which may have several
nonzero polynomial coordinates. The current
OriginalAffineIdealEngine authenticates this unit through the complete
identity \(M_{\bf 1}=I_n\); the same original multiplication/table return
also gives (10). This applies in either actual affine chart.

A future implementation may consequently compute the content from the
\(n\) original denominator coordinates, then verify all exact quotients in
\(M_D=h_DM_0\), rather than discovering the gcd by scanning \(n^2\) entries.
This is an exact complete-algebra identity, not a coordinate or residue
projection. The final \(H,U,\det H\), length, all original remainders, and
all paired \(XMD=YMN\) returns in (9) remain mandatory.

No actual content or content degree has yet been read from v15. This note
does not assert that (9) is nontrivial on that input.

## 8. Published request and exact scope

The fixed public request selects 18 source files and 420 seconds through the existing complete-quadratic API workflow. The helper is 16595 bytes / SHA256 ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225; the checker is 19453 bytes / SHA256 aab13e7e58d1700157456e39ae616bd1405237ad45f6e592383f18dacf6e8d4e. The selector adds precisely one fixed branch; deleting it recovers the previous selector byte for byte. Its SHA256 is 2bacbb98b9f93ca77d5d146118fa3ba9e06e5dd57cb9ca9f9654aec23e403df2. Request SHA256: 901459b583fa9364cbb4b6639b99a3d487a44769a039430cde7b445ddca9b560.

At publication this is an implemented software request, with no execution receipt or PASS yet. The unique heavy original production remains v15, run46112816717/job140879915022/sourcee959b4331bb9cd3871c9f05b101d47f2dba9e962; at 2026-11-28 06:15:26 UTC step 4 was still in progress and the log endpoint still returned BlobNotFound. The isolated check does not replace, restart, or alter that input. Recomputable matrices, transcripts, and Actions logs are not committed.
