# Complete 7908-domain ordinary adjoint Grams from the exact completed pilot

This is a fixed-background, complete-input covariance consumer. It expands
the four actually successful closed quarters of public run
43664278200, using the same complete 257-state, 97-input physical adjoint
Hermite proposal from run 43662865692. It proves no boundary-adjoint inverse,
no full high-to-low cap estimate and no infinite-dimensional BVP inverse
by itself.

## C.1 Exact object and existing mathematical calculation

The candidate index has SHA256
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
The complete continuous repair has definition SHA256
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.
The fixed physical parameter is $\eta_0$, the original $\nu$, and the
repaired M32 background at $\delta=0$. This is not a transfer to a moving
nonlinear background.

The actual full adjoint proposal native has SHA256
acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7.
Its seven array receipts include all 1977 shared nodes, every 257 by 97
state, and both original one-sided derivatives on all 1976 intervals.
They define an exact piecewise Hermite trial. No new QR, finite solve,
state, derivative or intrinsic target is computed here.

The four-quarter native has SHA256
eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb.
Its nine gates and actual child return code zero are checked separately
from later publication status. Its complete row indices are
$0,64,4096,7907$. Every saved signed matrix and coefficient-model array
is reused byte for byte.

The original core source SHA256 is
689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc.
The actual four-quarter source SHA256 is
ae3b90c15e65343a0d5bdeb80cba4d6eb2a6f519155bff9a175b0f48a2f72310.
The new range source calls that source's unchanged
actual_row function. The formal residual formulas, angular Fourier
normalization, exact radial Legendre integration, complete Hessian
transpose, all infinite coefficient tails and all Young weights are
therefore those in the published complete97 ordinary-adjoint Gram
contract. This document specifies the additional coverage and summation
proof.

## C.2 Disjoint assignment and exact original slice identity

Let $I_i=[a_i,b_i]$, $0\le i<7908$, be the original ordered closed
quarters. The old complete quarter consumer supplies

$$
a_0=\frac9{10},\qquad
b_i=a_{i+1},\qquad
b_{7907}=\frac{25}{8}.
\tag{C.1}
$$

Group $g$, $0\le g<32$, receives the integer range

$$
[248g,\min(7908,248(g+1)))
\setminus\{0,64,4096,7907\}.
\tag{C.2}
$$

These groups are pairwise disjoint and contain exactly 7904 indices.
The four actual pilot rows complete the 7908-element set. No pilot row
belongs to a new numerical range.

The preparation consumer first validates every original scalar row,
all 64 original native midpoint rows, the exact full adjoint proposal
and the actual pilot. It then packages the literal binary64 nodes,
states and derivatives needed for each group. Packaging does not select
new scientific numbers. Each array slice has both a file SHA256 and a
SHA256 of its contiguous original little-endian binary64 values. Its
global first and last node indices, complete original seven-array
receipts, original quarter hashes and original complete Hessian row
hashes are recorded.

The closed node slice includes the complete Hermite intervals meeting
the assigned radial range. The only left extrapolation permitted is
the original first Hermite polynomial on the tiny strip between
$9/10$ and the original first binary64 node. Every other intersection
lies within its actual original node interval. The entire first
quarter, not merely its left endpoint, obeys this same original
Hermite convention.

Slicing changes array indices, not the exact trial. The old pilot
function computes all true intersections with original Hermite nodes
and complete local Hessian cells. After this computation the range
wrapper restores the global node and Hessian indices in metadata.
No coefficient, interval, weight, residual or covariance entry is
changed by this relabelling.

## C.3 Local Hessian representation

All 1341 complete native-point Hessian source rows and the same
physical-background native are validated. Their original coefficient
bounds $E_\infty,E_1,Z_{BB},Z_{BC},Z_{CC}$ are saved as outward
enclosures. Reading their upper endpoints is a further nonnegative
upper enclosure; it does not change the represented exact operator.

For every closed intersection the complete formal ordinary residual
and the complete true residual satisfy the old contract

$$
r_{\mathrm{formal}}=-z_r-A_{\mathrm{phys}}^*z,\qquad
r_{\mathrm{true}}=r_{\mathrm{formal}}-H_R^*z.
\tag{C.3}
$$

The independent even mean is retained. In particular the $Z_{BC}$ term
acts on the adjoint B component in the C equation. Its mean contribution
is not projected away. All actual $4j$ angular derivative factors and
all infinite coefficient remainders remain in the unchanged core
calculation.

## C.4 Nine full signed covariance bounds on every quarter

For each of the nine quantities

- the finite ordinary residual;
- its full coefficient remainder;
- the complete Hessian adjoint term;
- the complete formal ordinary residual;
- the complete true adjoint ordinary residual;
- the B and C trial fields;
- their two angular derivatives,

the actual quarter calculation supplies a symmetric 97 by 97 Loewner
upper bound $G_{i,k}$. For every real input vector $\lambda$,

$$
\int_{I_i}
 \|T_k(r)\lambda\|_{L^2_\theta}^{\,2}\,dr
\le \lambda^T G_{i,k}\lambda.
\tag{C.4}
$$

The angular measure is normalized on the circle. Physical nonmean sine
and cosine amplitudes have square weight $1/2$, and the even mean has
square weight one. The radial measure and exact Legendre factors
$|I|/(2n+1)$ have already been paid on every actual intersection.

The saved upper triangle is an exact symmetric dyadic matrix $C$ with
an exact nonnegative dyadic diagonal slack $\sigma$. Its meaning is
$G=C+\sigma I$. Signed off-diagonal entries are not replaced by
entrywise absolute values. The slack bounds the operator norm of the
complete symmetric enclosure radius by its maximum absolute row sum.
Consequently the saved matrix is a valid covariance upper bound even
when the selected midpoint matrix alone would not be positive.

## C.5 Complete source Gram by true radial disjointness

For each fixed quantity $k$, define

$$
G_k^{\mathrm{all}}=\sum_{i=0}^{7907}G_{i,k}.
\tag{C.5}
$$

The interiors of the actual intervals are disjoint. Endpoints have
zero radial measure. Thus (C.4) gives

$$
\int_{9/10}^{25/8}
 \|T_k(r)\lambda\|_{L^2_\theta}^{\,2}\,dr
\le \lambda^T G_k^{\mathrm{all}}\lambda.
\tag{C.6}
$$

This summation uses disjoint radial integration. It does not claim
orthogonality between different residual terms at one point, between
different input columns, or between a source and an endpoint defect.
Those correlations were already retained in each full signed matrix
and the complete positive Young estimates.

The finish consumer reads every original native/process/array receipt,
checks the exact integer union and the full rational edge chain (C.1),
and sums directed matrix enclosures. It makes one final symmetric
dyadic plus diagonal-slack enclosure of each complete matrix. It does
not multiply by interval lengths again. Its optional trace square
root is merely a Hilbert--Schmidt upper bound for that known
97-input operator; the complete matrix is retained for subsequent
direction-sensitive contraction.

## C.6 Actual process identity and recovery

Preparation, ranges and finish use distinct actual process records.
The original mathematical sources, actual pilot native, complete
candidate and original proposal arrays remain pinned. A native with
a real successful child and complete mathematical gates remains
reusable if a subsequent summary or Git publication fails.
Publication completion is not substituted for a mathematical gate.

Each range writes its actual native after every newly completed
quarter. Its immutable array and original quarter identity are checked
before resuming a prefix. A genuine mathematical failure remains
recorded and does not silently trigger the same failed calculation.
Reruns preserve all preceding complete native bytes and associated
array receipts. The original pilot is never recomputed.

Every public worker performs actual pull and both README difference
checks at its checkpoint interval, at most ten minutes during a
running child. Changes of reviewed rules require the separately
reviewed rules mechanism. Non-fast-forward pushes use the existing
real pull/rebase/retry publisher.

Large original proposal arrays, slices and new signed covariance
arrays remain in public Actions artifacts. Repository notes contain
complete native or original-byte parts and bounded small process
summaries. Every new plain-text summary is measured before writing
and limited to 60000 UTF8 bytes.

## C.7 Exact remaining scope

The complete source covariance (C.6) is a new actual input to the
published full-cap-adjoint posterior identity. It does not yet pay
the true left endpoint, outer Robin, independent outer mean,
high-output Fourier Gram or their joint same-input contraction.

The final cap high-to-low operator requires those additional
covariances, the complete physical Green/Hessian resolvent, and the
corresponding finite193 right-boundary Poisson matrix. Unknown high
feedback, the negative high BVP inverse, the coupled low/high Schur
problem and nonlinear background changes remain separate obligations.
