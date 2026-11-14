# Complete R270 condensed-QP warm interface

This independent producer makes one actual optimization warm step from the
completed request42 field. It retains the original complete nonlinear
equations, exact inlet/constant-state coordinate chart, scalar design
variables, original all-query domain checks, and original boundary FD
consumer. It changes the algorithm that chooses a direction.

It does not call the native tail. It does not declare the warm accepted
as a full prefix/tail BVP, as a closed surface, or as the required
large-amplitude same-metric family.

The mathematical reduction is
[R270](../results/R270-exact-local-support-damped-QP-condensation.md).
The square-root library is documented separately in
[its interface note](2026-11-14-complete-local-QP-condensation-library-interface.md).
The first actual parent is recorded in
[the request42 note](2026-11-14-actual-request42-complete-QR-32-row-warm.md).

## Frozen source identities

| Independent source | Bytes | SHA-256 |
| --- | ---: | --- |
| geometry_20261114_condensed_local_inequality_qp.py | 17551 | ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173 |
| geometry_20261114_condensed_projection_warm.py | 28324 | 5d398d3d702e0fd93af3777504fc1d4e918110c7e5f0683601eac5d21c49914a |
| geometry_20261114_condensed_projection_response.py | 2600 | 461b0d48068dba6cfcb62974c1e8f16889b1bd8ca5bd4b86e1bf6a3e09ac83b8 |
| root_20261114_complete_local_qp_condensation.py | 40393 | 84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b |

The original complete block QR remains
**596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722**.
The original C/feasible-segment engine remains
**7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152**.
The new wrapper pins all existing scientific dependencies and the two new
numerical modules. No existing solver file is edited.

All four new sources were read statically before publication. The terminal
was unavailable, so these frozen sources have no claimed local AST or
numerical execution. The public Actions lane compiles the source before
execution and supplies the actual computational receipt. Source review is
not an extra research acceptance gate.

## Exact problem and actual first parent

The first parent pair is the preserved request42 output:

| Input | SHA-256 |
| --- | --- |
| warm-001.json.gz | 3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317 |
| driver-status.json | 26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04 |

They occur under
[the original request42 output](public-actions-43623850723-1-twelvequeryqr/twelve-query-qr-warm).

The entry checks both original file hashes, the actual status naming the
warm, the whole original producer ledger, all preserved source hashes,
the unchanged 699-node mesh and field representation, and the original
complete scalar formula with the actual live global controls. The actual
parent is still unaccepted. A later completed checkpoint from the new
own schema can be resumed through the same entry after the same paired
status and producer checks; a prepared or unfinished object cannot be
invented as a parent.

All original accepted/prepared/config/zero-response input hashes remain
the original fixed values. The full T112 zero-height response/J is used
as the explicitly affine inner map. It is not a ready linear graph or a
claimed solution at the newly generated endpoint height.

The physical problem has M=T=112, a 338-component physical state, 109 free
core coefficients, and three global scalar controls. The exact reduced
chart has 236036 variables. The original 12 query groups have 24576
inequalities: nine left RMS groups at intervals 470, 471, 472, 473, 475,
477, 479, 480, and 481, and original collocation-midpoint groups at 473,
475, and 477, each with 2048 physical angles. Their complete B depends
on the retained 13 physical nodes 470–482 and all three control columns:
4397 local coordinates. The free core and the remaining physical nodes
are eliminated through the complete quadratic, not fixed to previous
values.

The old C projection remains a separately retained baseline. Its 4059
correction coordinates are nodes 471–482 and the global controls, with
the complete outside affine offset. That baseline restriction is never
applied to the new condensed candidate.

## Model, scaling, and affine elimination

Within one model let A denote the original weighted complete Jacobian in
the original scaled z coordinates, and let b be the same weighted
residual. The fixed quadratic is

    f(z) = 0.5 ||b + A z||^2 + 0.5 lambda^2 ||z||^2,
    lambda = 270,
    H = A^T A + lambda^2 I,
    g = A^T b.

The wrapper obtains g from the original A-transpose action. It constructs
one complete frozen block-QR factor with the same original A and row
weights. Its extra column preconditioner is explicitly none. The original
chart scale and the old C algorithm's column preconditioner are not
silently inserted into the new local coordinates.

The condensation library receives that completed live factor, original
g, and the full original B local-index vector. It retains the affine term
through the full transposed triangular solve, all 216 right-exterior
orthogonal eliminations, the whole pure-global square root and affine
column, and elimination of all 109 free-core columns. It produces an
upper triangular 4397-dimensional root, its affine column, the local
gradient, and the local center. It does not form a subtractive normal
Schur complement, use an approximate full center to erase g, discard a
pure-global term, or rebuild the original whole-field Jacobian.

In exact real arithmetic, R270 identifies this local quadratic with the
minimum over all outside variables. In the actual implementation the
rounded local root is not automatically identical to the original
floating-point A-transpose-A model. That distinction is preserved in
the library report, the one complete recovery, and the final original
A/AT/B readouts.

## Bounded local inequality algorithm

The new helper operates on all 4397 local coordinates and every original
selected B row. It retains:

- The feasible local part of the actual old C candidate.
- The strictly feasible local zero vector.
- The local unconstrained center and its original all-row radial repair.
- Every actual working-set candidate, its original all-row slack, and its
  all-row radial repair.
- The best actual feasible local candidate and a final minimization along
  the feasible segment from the C local vector to that candidate.

The local zero vector is not a zero full direction: its outside
coordinates are subsequently optimized with the complete affine
conditional response.

For a working constraint row r, the helper obtains the whole local
inverse v=Q-inverse r. It normalizes r and v by the square root of r-dot-v.
The nonnegative working dual uses the actual normalized rows and inverse
columns. The sign convention is the constraint c+B-local u >= 0, with

    u = local_center + Q-inverse B-working^T mu,
    mu >= 0.

Each dual coordinate update minimizes that one nonnegative coordinate.
The default is 200 cyclic sweeps for each added working row. The current
actual full slack is reread through the original local B action. The next
row is the largest current negative slack divided by c among nonworking
rows, considering all 24576 rows. Working-set membership never deletes
a row from feasibility verification.

The first declared budget allows at most 256 working rows. This is an
explicit computational budget of a new optimizer, not a changed physical
equation or scientific threshold. No 24576-dimensional dense dual Gram
matrix or 24576 complete global-chain inverse calls are formed. Each
new inverse has 4397 entries. The actual working Gram is kept without
silently symmetrizing it or adding a ridge; its asymmetry is reported.
A bounded coordinate sweep or a row-budget stop is not called a QP
optimum.

The helper preserves each original local inverse RHS, returned inverse,
and actual local residual array, in addition to the normalized working
rows, inverse columns, row scales, full working Gram, and dual. These
actual arrays are stored separately from the compact warm provenance.
Multiplying normalized values back by their scales is not substituted
for preservation of the original pre-normalization bytes.

Every feasibility repair here acts on the local vector before recovering
the outside conditional optimum. Its scaled nonnegative multipliers are
only a valid possible choice of algebraic posterior evidence, not an
assertion that radial repair preserves KKT stationarity.

## One complete recovery, actual comparison, and original trials

Only the final selected local candidate is recovered through the
library's one original complete H solve. The full right-hand side keeps
the original g and the embedded local force. The actual recovered local
entries are not overwritten with the requested values. The library
records their mismatch, the original complete H residual, and the
outside gradient from that original residual.

The wrapper then evaluates the actual complete A, AT, B, and B-transpose.
It applies the unchanged original full-vector radial and feasible-segment
safeguard to the recovered candidate. It compares the original complete
quadratic objective of this result with the already saved old C result
and uses the smaller actually evaluated one.

A later full-vector radial repair or mixture with the original raw-ray
backup can change the conditionally optimal outside response. The entry
records whether that happens and does not call the resulting vector an
exact conditional optimum. The original all-row feasibility and actual
descent requirements remain in force.

The original nonlinear engine then applies its actual 17 trial levels,
including fresh nodal RHS and nonlinear cubic-Hermite midpoint
construction, the original material-chart guard, both original RMS
query families, and the midpoint observer. No linear QP slack is
substituted for those nonlinear domain checks. The original scalar
controls remain one global vector and the original inlet/constant-state
identities remain exact by the same reduced chart.

The full-model R267 readout uses the actual original gradient and
stationarity vector. The new wrapper retains original C zero-dual
evidence, the recovered full candidate's evidence, and the finally
selected full candidate's evidence. It reports the best finite stored
lower-bound evaluation and the resulting cross-point gap. These are
ordinary floating-point evaluations of exact algebra, not validated
enclosures. A large or nonfinite diagnostic posterior is recorded; it
does not create a new BVP acceptance threshold.

## Deadlines and failure preservation

The declared candidate deadline is the smaller of the new candidate
budget and the original overall deadline less the original trial
reserve. The local optimizer stops 30 seconds earlier, reserving time
to start the final complete recovery under the frozen factor's own
deadline. Once a frozen original H solve has begun, its mandatory
complete readback follows that original source's policy.

The first planned values are:

| Budget or algorithm parameter | Value |
| --- | ---: |
| Overall original warm budget | 1200 seconds |
| Condensation/local-QP candidate budget | 600 seconds |
| Original trial and preservation reserve | 90 seconds |
| Complete recovery start reserve | 30 seconds |
| Maximum local working rows | 256 |
| Local dual sweeps per working stage | 200 |
| Original LSMR limit | 200 |
| Original baseline C sweeps | 200 |
| Original nonlinear trial levels | 17 |
| Original model count | 1 |
| Lambda | 270 |

The original C direction is retained before attempting the new
candidate. A declared factorization, condensation, local numerical, or
deadline failure is recorded with its full available report and the
original C result remains available. The original nonlinear scientific
checks are still run on the actual selected direction. Parent/source
identity checks are not bypassed.

All source and result reports distinguish a completed optional model
from fallback after an error. No failed optional module is relabelled
as having produced a valid condensed solution.

## Stable CLI

Use the original actual input files, not regenerated substitutes. With
the computations directory as the working directory:

    python geometry_20261114_condensed_projection_warm.py \
      --accepted "$ACCEPTED96" \
      --prepared "$PREPARED699" \
      --tail-anchor "$ACTUAL_ZERO112" \
      --tail-config "$CONFIG112" \
      --resume "$ACTUAL42_WARM" \
      --expected-resume-sha 3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317 \
      --parent-status "$ACTUAL42_STATUS" \
      --expected-parent-status-sha 26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04 \
      --out "$OUT/condensed-warm" \
      --iterations 1 --damping 270 --lsmr-iterations 200 \
      --projection-sweeps 200 --line-search-steps 17 \
      --budget-seconds 1200 --angles 4096 --jac-workers 2 \
      --condensed-budget-seconds 600 \
      --condensed-trial-reserve-seconds 90 \
      --condensed-recovery-reserve-seconds 30 \
      --condensed-max-working 256 --condensed-dual-sweeps 200 \
      --condensed-store-root

The fresh complete affine FD entry is:

    python geometry_20261114_condensed_projection_response.py \
      --accepted "$ACCEPTED96" \
      --prepared "$OUT/condensed-warm/warm-001.json.gz" \
      --tail-anchor "$ACTUAL_ZERO112" \
      --tail-config "$CONFIG112" \
      --out "$OUT/physical-response" --angles 4096

The second command consumes only a real newly saved warm from the first
command. It recomputes the original directions, step ladder, Richardson
comparison, and unchanged 5e-5 implementation threshold. It does not
rewrite an earlier FD report's warm SHA.

## Output contract and later continuation

The producer schema is
**exact-constraint-twelve-query-condensed-complete-H-warm-v1**.

On a successful warm step the original driver-status records one accepted
warm step and the actual latest file, normally warm-001.json.gz. Its top
scientific success and new coupled finite acceptance remain false. The
full original producer subtree of request42 is retained unchanged inside
the new producer ledger. Each new frozen numerical dependency is added
to the current ledger.

Additional outputs include:

| Output | Meaning |
| --- | --- |
| condensed-live-model-binding.json | The original A object/weights/g/B/parent identities used by the new module |
| condensed-QP-result.json.gz | Complete original computed metadata and references to preserved arrays |
| condensed-array-manifest.json | Every actual array part and original byte hash |
| condensed-versus-C-comparison.json | Actual same-full-objective selection, posterior, and fallback status |
| condensed-QP-summary.json | Small scalar/metadata summary; complete arrays and histories remain in the result |
| condensed-root directory, when requested | Raw local root/affine/gradient/center/recovery evidence and library reports |

The optional raw local-root files can exceed the repository's individual
file-publication limit. They stay in the complete Actions artifact and
are identified in the library manifest; the Git publisher must not
turn an artifact size policy into a numerical acceptance rule.

No accepted full field or true nonlinear native response is fabricated
by this interface. Later work must use the actual returned checkpoint,
the actual new FD report, and the original true-tail/full-BVP path
before any geometry, closure, isometry, or held-amplitude completion
claim.
