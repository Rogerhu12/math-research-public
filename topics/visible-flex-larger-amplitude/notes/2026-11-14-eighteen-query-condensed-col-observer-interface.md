# Eighteen original query grids after the actual60 left-RMS 467 failure

- Classification: independent numerical implementation and provenance interface; no new numerical result or final scientific acceptance.
- Author: amplitude agent.
- Date: 2026-11-14 UTC.

## 1. Concrete reason for this independent entry

The [actual60 report](2026-11-14-actual-request60-left-RMS467-limits-seventeen-query-continuation.md) records one successful optimization step at alpha `1/64`. During that execution, from the actual58 parent, the nearest rejected step `1/32` had finite original nodes and midpoints, positive margins on all seventeen modeled query grids, a decreasing original fixed-weight merit, and all right-RMS queries valid. Its sole original RMS-domain failure was left-RMS interval 467, beta squared `-0.006303834965005084` at phi zero. The actual/predicted merit-decrease ratio was `1.0006534006460601`.

This entry adds exactly that original left-RMS query, at all 2048 original angles, and starts from the newly saved actual60 field. It retains the existing twelve left-RMS grids and all five original midpoint grids. The midpoint480 failures at larger rejected steps are recorded in the actual60 report and are not added to this entry without a nearer limiting observation.

This changes the finite inequality model used to choose a warm direction. It does not alter the original nonlinear residual equations, the scalar profile, the tail configuration or the original acceptance criteria. A new model can still fail at another original query or at a finite step on a currently modeled query; the original complete trial checks remain authoritative.

## 2. Four independent frozen sources

The files belong under `computations/`. Frozen seventeen-query sources are unchanged.

| New source | Bytes | SHA256 |
|---|---:|---|
| `geometry_20261114_eighteen_query_domain_operator.py` | 29265 | `ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051` |
| `geometry_20261114_eighteen_query_condensed_warm.py` | 39705 | `b9f7d9150c57cff485f5f891881870095fc91f7a58fd40f63544e6bb9c3ef335` |
| `geometry_20261114_eighteen_query_condensed_response.py` | 2613 | `5885daeced8a8961f7f12d259ed5479683e7fd8dc2cccb8a2873ac9424918c9e` |
| `geometry_20261114_eighteen_query_collocation_observer_warm.py` | 16720 | `6ad75ce4b350aee4ae52afe2c6045f50d657931419ef7c4b46d0758db3acd1ca` |

The operator is an independent copy of the frozen seventeen-query implementation, with the declared left interval tuple, its identity/labels, the new parent origin and no other mathematical code changes. It pins the original captured full-angle operator `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` and the complete original seventeen-query operator `5bb4f214d4d2505185448a9162c0d995bdb6c37168e6d9542dfe6202e8f21a41`. The warm source includes the full old producer source chain and pins its immediate frozen parent warm source `f8131287af5d10653692f6e5b7c3cf8ee1d4f17757c3017007b20061598f317b`.

The complete numerical backends are unchanged:

| Role | Frozen source / SHA256 |
|---|---|
| Original complete chain QR | `exact_20261114_regularized_block_qr.py`, `596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722` |
| R270 complete affine condensation | `root_20261114_complete_local_qp_condensation.py`, `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b` |
| Local complete-H inequalities | `geometry_20261114_condensed_local_inequality_qp.py`, `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173` |
| Original full projection/trial engine | `geometry_20261114_full_angle_projection_warm.py`, `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152` |
| Fixed-support C baseline | `geometry_20261114_fixed_support_halfspaces.py`, `0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68` |
| Original complete new-warm FD consumer | `geometry_20261114_constrained_trust_response.py`, `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78` |

There is no local import or numerical fixture execution in preparing this change. All four files pass AST parsing; old source hashes and the complete source diffs were checked. Actual numerical checks and any warm advancement must run in this public repository's Actions.

## 3. Exact first parent and subsequent own-schema parents

The first parent is the completed actual60 pair from [run 43640358327](https://github.com/Rogerhu12/math-research-public/actions/runs/43640358327), source `da346d172715761d7da23da84c92d97a92b438de`, not its earlier input and not a prepared baseline.

| Parent artifact member | Original bytes | SHA256 |
|---|---:|---|
| `seventeen-condensed-warm/warm-001.json.gz` | 4783279 | `bc7cadbc17f17832785ace32b011136fd43c04147d450d557730de0f05d40a23` |
| `seventeen-condensed-warm/driver-status.json` | 1577692 | `5b419af7340777328184d7699cf1a4de539cd608c889f6e4f81fe549b253a922` |

The public bounded archive is `notes/public-actions-43640358327-1-condensedqp/seventeen-condensed-warm/`. Its status can be stored as `driver-status.json.gz`; gzip must restore the exact original JSON bytes and original uncompressed hash above. The consumer binds the warm basename, paired status identity and entire original producer. It does not accept a parsed/reserialized replacement under the old status hash.

The new optimizer schema is:

`exact-constraint-eighteen-query-condensed-complete-H-warm-v1`.

Its first-parent branch accepts the old seventeen-query schema only with the hard-pinned actual60 pair. Subsequent invocations accept a completed own-schema eighteen-query pair with explicit actual warm and original status SHA values. The original full producer/source/profile/constant-state validation remains. The complete parent producer stays intact under `resume_producer`; annotation only updates the current producer.

Each invocation performs one model iteration. Use `--iterations 1` and a new output directory. The wrapper's unique complete-linearization/candidate construction is not a multi-model execution contract. If further continuation is supported by a real result, a fresh invocation should bind that new field and original status rather than silently increasing the original loop count.

The unchanged original accepted96/prepared699 and T112 zero-J references remain provenance and the affine boundary reference. They are not relabeled as an accepted eighteen-query field or a new nonlinear native solve.

## 4. Typed query list and complete support

The declared left-RMS tuple is:

`(467,468,469,470,471,472,473,475,477,479,480,481,482)`.

Its fraction is the original `0.17267316464601146`. The original midpoint tuple is:

`(473,475,477,481,482)`.

The latter uses fraction `0.5` and directly reads each original `state.middle[j]` and `problem.mid[j]`. It is not replaced by an RMS query or a newly sampled spline midpoint. Every block has an explicit `kind`, `interval`, fraction, station and query index. Query order is all thirteen left-RMS blocks followed by all five midpoints; every block contains original physical phi indices `0..2047`.

Thus there are 36864 inequality rows, 236036 complete scaled-coordinate columns, and 5749 local columns from all physical components at nodes 467–483 and the three global controls. Capture intervals are deduplicated only for endpoint recording. All eighteen query blocks remain distinct; no midpoint is merged with a left-RMS block at the same interval.

The original A is still constructed once. `capture_queries` asks its unchanged endpoint recorder for the thirteen unique intervals. The read-only left-component view compiles the thirteen left-RMS blocks from that same capture; the complete operator restores the original capture and complete node list before constructing the five original midpoint blocks. Both original J and parameter-P blocks for the new endpoint467/468 pair are retained, and all shared-node and global-control transpose contributions use the original scatter-add convention. There is no auxiliary complete Jacobian construction.

For each original query, B retains all nodal RHS dependencies, the exact inlet chart if relevant, the complete global-control dependence and the direct scalar terms. The original midpoint chain remains:

$$
\delta Y_{\mathrm{mid}}=\tfrac12(\delta Y_L+\delta Y_R)-\tfrac h8(\delta f_R-\delta f_L).
$$

The inverse coordinate scaling is applied once. Existing matrix actions, transpose actions, adjoint checks, typed original-complex-chain checks and full array export loops all use the complete new block list. Their original implementation thresholds remain `5e-12` for adjoint/local action checks and `5e-5` for the independent original complex chain; these are implementation checks, not relaxed or additional scientific acceptance gates.

## 5. C baseline and complete-H candidate remain different computations

The original C projection retains nodes 471–482 plus the three controls, or 4059 coordinates. It retains the complete outside contribution in each affine row:

$$
c+B_{\mathrm{out}}z_{0,\mathrm{out}}+B_Sz_S\geq0.
$$

The new outside nodes explicitly include 467,468,469,470 and483. In particular, the new left-RMS467 block cannot silently drop either endpoint merely because both lie outside the C correction support. Negative effective offsets and computed zero local rows remain recorded outcomes of that restricted binary64 model; they are not used to change the original equations or declare a complete scientific failure.

The full-H candidate uses all 5749 local coordinates and the complete affine optimal response of the exterior variables. Original free-core109 and every pure-global contribution remain in the factor and condensation. The library dynamically reads the complete local support, so no frozen condensation source needs a size edit. It retains original g from the actual A-transpose b, the affine column, the complete factor identities, and its one final complete-H recovery/readback. It does not freeze the exterior raw direction to the C candidate.

Both candidates are compared using the same original full objective. The original feasible ray, full-vector radial repairs, feasible segment selection, fresh original A/AT/B/BT evidence, R267 ordinary-float diagnostics and complete nonlinear backtracking remain. Whole-vector radial scaling may change exterior components; the output does not claim the final outside vector stayed unchanged.

There is no new scalar, core, Fourier or nonlinear-boundary parameter. Damping is the original algorithmic model penalty, not a changed metric. All original field/core/control modes, endpoint conditions, nonlinear domain guards and final scientific standards remain.

## 6. Exact Actions invocation

Use the public source restoration and actually completed M112 preparation and T112 references already used in request60. The first-parent warm and status must be restored into `VISIBLE_PARENT60` with the exact bytes in Section 3. The new output directory is `eighteen-condensed-warm`.

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_eighteen_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT60/warm-001.json.gz" \
  --expected-resume-sha bc7cadbc17f17832785ace32b011136fd43c04147d450d557730de0f05d40a23 \
  --parent-status "$VISIBLE_PARENT60/driver-status.json" \
  --expected-parent-status-sha 5b419af7340777328184d7699cf1a4de539cd608c889f6e4f81fe549b253a922 \
  --out "$VISIBLE_OUT/eighteen-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

After the original warm succeeds, the workflow reads `driver-status.json`, requires the new eighteen-query schema, one accepted optimization step and true `optimization_progress`, and validates the `latest_warm_file` basename and actual `latest_warm_sha256`. That identifies the file for the unchanged actual-warm FD:

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_eighteen_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

The CLI budgets are unchanged from actual60. The number eighteen counts typed algorithmic query grids; it does not change the original seventeen nonlinear trial allowance. No native worker is started by this warm/FD pair.

## 7. Read-only observer and final output identities

The separate collocation observer is the previous frozen read-only implementation with the new producer import and actual source pin. The original evaluate method and weights method execute exactly once per original request. The observer reads original returned collocation/vector/state/RHS arrays and the original model's already returned W. It locates the maximum over all physical intervals/components, including rows outside B, and preserves their signed values, component identity, stations and frozen row weight.

A nonfinite complete physical array has no defined complete maximum; the saved report distinguishes that case from an otherwise finite physical residual followed by an original RMS-domain rejection. Observer exceptions record diagnostics and leave the original returned state/vector/finite flag and decision intact. It performs no extra RHS, J, profile, boundary, model or trial call.

The mathematical producer ledger remains the complete eighteen-query ledger. Current observer provenance has its own actual source field, and all old producer/observer subtrees stay unchanged. The full midpoint observer is also retained, reading original returned middle/fm without an extra whole-flow evaluation.

Expected artifacts retain the prior layout:

- `eighteen-condensed-warm/driver-status.json`, current intent and actual `model-000.json`, including every original trial and typed actual-query readout.
- `warm-001.json.gz` only after a real original warm decrease passes its complete domain checks; `success` and `new_coupled_finite_acceptance` remain false.
- Complete `domain-operator/` B/Gamma/Pi/beta chunks, original endpoint factors and original midpoint inputs with actual byte identities.
- `condensed-QP-summary.json`, the full compressed result, original C/H comparison, complete array manifest and `condensed-arrays/` payloads.
- `condensed-root/` raw local-root/affine/gradient/recovery arrays when requested; memory-only complete chain factors are not misrepresented as exported files.
- Read-only `midpoint-observer/` and `collocation-observer/` original reports and payloads.
- `physical-response/response-check.json` with the new warm SHA, full consumed-source set and newly recomputed original Richardson checks.

Large intermediate arrays are artifact data. Bounded publication must preserve original SHA metadata and may transparently gzip a large JSON status; it must not alter the original status identity or claim omitted payloads were independently audited.

The FD still uses the actual complete T112 zero-H Jacobian held explicitly affine. It recomputes every original direction, step and Richardson level on the new actual field; it does not relabel an older pass or claim a new nonlinear native solution. Successful warm and FD output remains an unaccepted field needing the original complete full-DN, refinement and geometric criteria.
