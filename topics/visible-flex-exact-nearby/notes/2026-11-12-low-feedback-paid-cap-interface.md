# Paid cap/interface inputs for the physical M4 feedback candidate

## Status and exact object

This note supplies the complete finite-matrix argument implemented in
`scripts/fourfold_phase_low_feedback_paid_inputs.py`. The implementation was
rebuilt after the execution environment became unavailable on 2026-11-12.
The earlier successful local output was not pushed. Its numerical values are
therefore not reconstructed here as a report: the branch workflow executes the
new source against the already published input arrays and writes a new report.

The object is the explicit symmetric exact affine graph with
\[
 \delta=-7789843107295549/4611686018427387904.
\]
Its object JSON has SHA256
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`.
Both physical ports are at \(r=\pm1/4\). The calculation keeps the angular
mean, the two regular mean variables, and the translation border.

The complete cap energy and full-output proofs and the quarter-cut
multipliers are rigorous inputs. The saved core DN array is still a floating
radial-transfer candidate. Certifying the exact dyadic matrix assembled from
that array does not certify the true core DN map.

## 1. Spaces and finite definitions

Use the orthonormal physical angular basis \(e^{4ik\theta}\). Let
\(P=P_N\), \(N=4\), retain every \(k=-N,\ldots,N\), and write \(n=2N+1\).
Finite retained vectors carry their Euclidean norm. On complete boundary
traces use the physical weights
\[
 w_0=1,\qquad w_k=\sqrt{4|k|}\quad(k\ne0)
\]
for \(H^{1/2}\), and reciprocal weights for \(H^{-1/2}\).
Each regular scalar carries its ordinary absolute-value norm.

Let \(K_{\rm raw}\) be the complete saved \(2n\)-by-\(2n\) dyadic core array
and let
\[
 K=(K_{\rm raw}+K_{\rm raw}^*)/2.
\]
No numerical entry of \(K_{\rm raw}\) is declared to be an exact true core
coefficient. Let \(C\) be the already certified \(n+1\)-dimensional cap
compression center. It contains the regular mean port. Let \(Y_c,S_c\)
denote the finite Toeplitz matrices of the saved real even polynomials for
\[
 Y=Y_z>0,\qquad S=YpY
\]
at the positive physical quarter cut; at the negative cap use its positive
height and the corresponding outward conormal. The already proved reflection
and conormal signs give the same two finite shear matrices.

Set \(J=\operatorname{diag}(Y_c,Y_c)\). On the \(2n+2\) retained boundary and
regular variables define
\[
 A_{\rm unb}
 =\begin{pmatrix}J^*KJ&0\\0&0\end{pmatrix}
  +C_{\rm left}+C_{\rm right}
  -\operatorname{diag}(S_c,S_c,0,0).
\]
Here \(C_{\rm left}\) acts only on the left \(n\) boundary variables and its
regular scalar; \(C_{\rm right}\) acts only on the disjoint right summand.
There is no deletion of either regular row or column.

The unit vector \(t\) has entries \(-1/2,+1/2,-1/2,+1/2\) at the left angular
mean, right angular mean, left regular mean, right regular mean, respectively.
The exact finite candidate is
\[
 A=\begin{pmatrix}A_{\rm unb}&t\\t^*&0\end{pmatrix}.                 \tag{1}
\]
All operations in (1) are exact algebraic operations on the published dyadic
arrays. The binary64 midpoint saved by the replay is only an approximation to
this exact expression; its selection error is recorded separately. The
directed inverse proof below is for the expression (1).

The true translation need not be an exact kernel of the saved floating core
array. The replay records the resulting gauge-equation defect; it does not
replace that defect by zero.

## 2. Directed finite inverse

Choose a binary64 matrix \(R\) by an ordinary numerical inversion of a
midpoint of (1). The choice need not be correct a priori. Reinterpret each
entry of \(R\) as its exact dyadic value and rigorously enclose
\[
 \varepsilon_R=\|I-RA\|_2,\qquad M_R=\|R\|_2.                      \tag{2}
\]
If \(\varepsilon_R<1\), the Neumann series proves
\[
 A^{-1}=(I-(I-RA))^{-1}R,\qquad
 \|A^{-1}\|_2\le B:=\frac{M_R}{1-\varepsilon_R}.                   \tag{3}
\]
A floating inverse or singular value by itself is not used as a proof.

For any finite matrix \(V\), the norm routine forms a directed enclosure of
the exact Hermitian Gram matrix \(H=V^*V\). Conjugate entries are symmetrized
as enclosures of the same exact entry and diagonal entries are restricted to
their mathematically real values. For each \(q=1,2,4,8,16\),
\[
 \|H\|_2^q=\rho(H^q)
 \le\|H^q\|_\infty
 \le\max_i\sum_j |(H^q)_{ij}|.
\]
The minimum of the resulting directed bounds, followed by the square root,
bounds \(\|V\|_2\). All powers and row sums are computed with Arb/Acb balls.
The proof uses the known Hermitian exact Gram matrix inside the enclosure,
not a floating eigendecomposition.

## 3. Fees already paid at the same port

Let \(\rho_C\) be the complete true cap-compression radius supplied by the
published complementary-energy certificate. Because the two cap blocks act
on disjoint summands, their direct sum has error at most \(\rho_C\), rather
than \(2\rho_C\).

The multiplier report gives complete Wiener errors
\[
 \|Y-Y_{\rm poly}\|_{A_0}\le e_Y,\qquad
 \|S-S_{\rm poly}\|_{A_0}\le e_S,
\]
including all retained-coefficient errors, angular aliases, the infinite
primitive error, and the unretained Fourier tail. Projection is contractive
on \(L^2\), and multiplication has \(L^2\) norm at most its \(A_0\) norm.
Thus the **projected** true height \(\widehat Y=PYP\) obeys
\[
 \|\widehat Y-Y_c\|\le e_Y,\qquad
 \|\widehat Y\|\le y+e_Y,\quad y=\|Y_c\|.
\]
At fixed \(K\),
\[
 \|\widehat J^*K\widehat J-J^*KJ\|
 \le \|K\|(2y e_Y+e_Y^2),                                      \tag{4}
\]
and the two disjoint shear errors have norm at most \(e_S\).
Relative to a core error later measured from \(K_{\rm raw}\), its finite
symmetrization costs
\[
 e_{\rm sym}=(y+e_Y)^2\|K-K_{\rm raw}\|.                          \tag{5}
\]
Consequently the complete currently paid finite-matrix fee is
\[
 e_{\rm paid}
 =\rho_C+\|K\|(2y e_Y+e_Y^2)+e_S+e_{\rm sym}.                     \tag{6}
\]
Equations (4)--(6) concern the retained product with projected heights.
They do not turn an omitted height trace into a retained one.

Let \(E_{\rm rest}\) collect **all** still unpaid perturbations in this same
finite realization, including the true core radial error and the change
resulting from actual high-channel elimination. The only concluded
conditional inverse statement is
\[
 B(e_{\rm paid}+\|E_{\rm rest}\|)<1
 \ \Longrightarrow\
 \|(A+E_{\rm paid}+E_{\rm rest})^{-1}\|
 \le\frac{B}{1-B(e_{\rm paid}+\|E_{\rm rest}\|)}.                  \tag{7}
\]
Here \(E_{\rm paid}\) denotes any actual matrix error bounded by (6).
The replay outputs
\[
 \eta_{\rm left}=B^{-1}-e_{\rm paid}.                            \tag{8}
\]
If every other unpaid term were zero, a true retained core DN error
\(\kappa\), measured from \(K_{\rm raw}\), would fit when
\[
 \kappa<\eta_{\rm left}/(y+e_Y)^2.                               \tag{9}
\]
This is explicitly a conditional allocation of the remaining budget.

## 4. Full high-output diagnostics

Finite input does not imply finite output. For a saved multiplier polynomial
\(p=\sum_{|m|\le L}c_m e^{4im\theta}\) and an input retained through \(N\),
the product has every output index from \(-L-N\) through \(L+N\).
The replay sums **all** these rows outside \(P_N\) into the exact weighted
Gram matrix
\[
 G_{ij}
 =\sum_{|k|>N} w_k^{\,2}\overline{c_{k-i}}c_{k-j},
 \quad -N\le i,j\le N.                                         \tag{10}
\]
Using reciprocal weights yields the \(H^{-1/2}\) version. Formula (10) has
no omitted row of the finite polynomial.

The complete height multiplier error has already been bounded as an
\(H^{1/2}\)-multiplier error \(e_{Y,1/2}\). A retained Euclidean input has
\(H^{1/2}\) norm at most \(\sqrt{\max(1,4N)}\) times its Euclidean norm.
Hence its additional complete high-height error is at most
\[
 \sqrt{\max(1,4N)}\,e_{Y,1/2}.
\]
For the shear, \(H^{-1/2}\) norm is no larger than \(L^2\) norm, so \(e_S\)
bounds its remaining complete high-output error. The independent cap
full-output report supplies the true cap high-output norm for the same
retained inputs and the same physical \(H^{-1/2}\) port.

These norms are useful actual coupling inputs. They are not simply added to
(6): a true high-output vector must first be propagated through the appropriate
high-block inverse or eliminated in the actual Schur complement. The physical
quarter-cut \(H^{1/2}\) contact cannot be replaced by the turning-root
\(H^{1/3}\) contact. Likewise the restricted high **body** inverse does not
automatically invert the complete boundary-feedback operator.

For a low input cutoff \(N\) and an output cutoff \(L_{\rm out}\), a multiplier
coefficient-tail argument must use indices beyond \(L_{\rm out}-N\).
Discarding coefficients beyond \(2N\) is not a general output-tail bound.

## 5. Reproducibility and outstanding work

From the topic directory:
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_low_feedback_paid_inputs.py \
  --bits 256 \
  --out notes/2026-11-12-actual-low-feedback-paid-cap-interface-M4.json
~~~

The runner hashes every JSON and every loaded NPZ, enforces the same exact
object/parameter and physical cuts, records the source and dependencies, and
saves its exact dyadic inverse candidate. The branch workflow publishes its
new JSON, NPZ and stdout as reproducible outputs. It does not reuse the
unpublished lost output as evidence.

The next missing mathematical inputs remain:

1. Directed propagation of the true two-channel retained core generator across
   every exact common spline span, followed by a true retained core DN error.
2. The full omitted-height and high-channel feedback in the same port and
   norm, with every angular mean and regular \(\xi/\lambda\) port retained.
3. Verification that their combined matrix fee satisfies (7).

The source therefore explicitly writes
`actual_core_radial_error_paid=false`,
`infinite_high_frequency_elimination_paid=false`, and
`rigorous_full_Schur_inverse=false`, regardless of whether (3) and (6) pass.
