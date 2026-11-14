# Nine-query candidate using the two actually observed collocation midpoints

Request29 saved a decreased complete warm and located its nearest domain
limitation at the original collocation midpoint of interval473. The
midpoint of477 was also actually invalid at larger rejected steps. The
seven modeled left RMS grids remained positive at those trials. See
[`2026-11-14-actual-request29-observed-seven-query-warm.md`](2026-11-14-actual-request29-observed-seven-query-warm.md)
for the original values, all failed trials and their saved midpoint bytes.

This independent candidate retains all seven left RMS queries and adds
the two observed midpoint queries. Each query retains the complete
original2048-angle physical grid. It changes only the finite optimizer's
domain model; the full original equations and every nonlinear acceptance
condition remain unchanged. It starts at the actual request29 warm and
does not wait for, or consume an uncomputed output of, the separate
complete-H experiment.

## 1. Exact input and typed query list

The first parent must be the actual request29
`observed-seven-warm/warm-001.json.gz`, SHA256
`f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9`.
The independent entry checks the entire preserved producer ledger, all
original699 nodes and M112/N2048 coefficients, the full scalar formula
and actual three constant controls, and the explicit unaccepted flags.
The original accepted96, prepared699, completed true zero-H T112 J and
T112 configuration bindings are unchanged. No parent metadata is
relabeled.

The row order is explicit:

| Query indices | Kind | Intervals | Fraction and station source |
| --- | --- | --- | --- |
| `0..6` | `left-RMS` | `472,473,475,477,479,480,481` | Original fraction `0.17267316464601146` and original spline query |
| `7` | `collocation-midpoint` | `473` | Fraction `0.5`, directly `state.middle[473]` and `problem.mid[473]` |
| `8` | `collocation-midpoint` | `477` | Fraction `0.5`, directly `state.middle[477]` and `problem.mid[477]` |

The matrix has18,432 rows. Its coordinate dimension remains236,036 and
its possible local support remains3,721 columns: the same eleven
physical nodes and three global controls already used by request29.
The two added midpoint endpoint pairs were already in the original
seven-query capture.

An interval may occur twice because its left RMS query and its original
collocation midpoint are different queries. Every query description,
factor/block identity, exported row part, complex-chain check and actual
trial readout records its kind, query index, interval, fraction and
station. A heterogeneous row list does not advertise one shared RMS
fraction: its top-level fraction is null, with the complete per-query
specification supplied instead.

## 2. Preserve the actual midpoint construction and full derivative

`geometry_20261114_mixed_query_domain_operator.py` first invokes the
frozen original `FullAngleDomainOperator` to compile the seven original
left RMS blocks unchanged. It keeps those actual B/Gamma/Pi arrays and
their source/model identity. It then compiles the two midpoint blocks
from the original returned middle states, not from a separately
interpolated approximation or a linear average of the endpoints.

For an original cell of length $h$, let its physical endpoint directions
be $d y_L,d y_R$ and let the single global control direction be $d p$.
The original returned collocation midpoint is

$$
 y_m=\frac{y_L+y_R}{2}-\frac h8(f_R-f_L).
$$

With the original endpoint physical/control Jacobians $J_L,P_L,J_R,P_R$,
its full direction is

$$
 d y_m=
 \left(\frac12I+\frac h8J_L\right)d y_L
 +\left(\frac12I-\frac h8J_R\right)d y_R
 +\frac h8(P_L-P_R)d p.
$$

If Gamma is the original beta-squared derivative with respect to the
physical query coefficients and Pi is its direct scalar-control
derivative, the new unscaled blocks are

$$
 \begin{aligned}
 B_L&=\tfrac12\Gamma+\tfrac h8\Gamma J_L,\\
 B_R&=\tfrac12\Gamma-\tfrac h8\Gamma J_R,\\
 B_p&=\tfrac h8(\Gamma P_L-\Gamma P_R)+\Pi.
 \end{aligned}
$$

The general local assembly retains the exact free-inlet-core injection
if a query uses the inlet. The present two new queries are interior
cells. Global controls remain shared, their two nodal RHS chains and
direct query contribution are both present, and the original coordinate
scale divides each final column once. No actual physical mode, core
unknown, control or original collocation/boundary row is removed.

The midpoint's value and station are read directly from `state.middle`
and `problem.mid`. Reconstructing the displayed formula from the saved
nodal data is a diagnostic comparison only. Its result is not substituted
for the actual original midpoint bytes.

Only the single original complete Jacobian is constructed. The capture
observes its original calls unchanged and retains the same eleven-node
J/P factors, including the per-cell source of any shared endpoint.
The new midpoint Gamma/Pi compilation uses the original linear q.jet
unit columns; it does not invoke another whole-flow Jacobian. Forward
and transpose actions share the same frozen nine compiled row blocks,
and shared nodes/controls are scatter-added.

## 3. Complete implementation checks and original nonlinear trials

The new mixed operator retains the original implementation thresholds:
`5e-12` for full/local adjoint consistency and `5e-5` for the independent
original complex-chain comparison. It checks the actual complete LSMR
direction and a seeded direction including local physical, core and
global-control coordinates. No complex direction is sent through the
real-only exact-coordinate pack/expand path.

The independent check evaluates the original complex endpoint RHS only
at the same eleven captured nodes. For left RMS queries it uses the
original spline construction. For a midpoint it uses precisely
the original midpoint expression above, with its original station. Its
worst-row and per-query reports always identify the query kind. It also
records the complex real-part discrepancy from the saved original query;
it does not assert bitwise identity between different floating evaluation
paths.

The original C-weighted Hildreth projection, full positive-damping model,
radial feasibility repairs and same-model feasible-segment selection
remain unchanged. There is one model with lambda270, at most200 LSMR
iterations,200 projection sweeps and the original seventeen trial
steps. The same one-half linear margin reserve is an algorithmic choice,
not a scientific tolerance.

All original complete nodal, midpoint, both RMS-query and uniform-density
checks remain decisive. All actual trial RHS and residual merits are
recomputed by the frozen original evaluator. The added linear inequalities
do not replace any of these original tests, and their finite angular
grids do not certify the continuous domain.

The actual selected-query trial readout now reports all nine typed grids.
Its two midpoint values are again taken directly from that same trial's
returned `state.middle` and `problem.mid`. It performs no additional
whole-flow or Jacobian call. The request29 read-only midpoint observer
also remains active, preserving any actual bad midpoint rows and their
complete original angular arrays with the same diagnostic-only exception
handling. A failure outside the nine modeled queries remains an original
failure and is not hidden.

## 4. Independent entry, output identity and preservation

The new warm entry is
`geometry_20261114_mixed_query_projection_warm.py`. Its schema is
`exact-constraint-nine-typed-query-feasible-projection-warm-v1`.
It wraps the original frozen engine without editing its file.

The engine still counts one full angular grid per declared query. The
new entry gives it the nine-query interval order, including the two
repeated interval IDs, and supplies a capture adapter that deduplicates
only the endpoint capture to the original seven distinct cells. It
does not weaken the engine's original row-count check. Query kind and
station are carried separately and remain authoritative for the actual
construction.

The complete current source ledger includes the new mixed operator and
entry, the original observer, original seven-query entry, original
projection engine and all original mathematical dependencies. Every
entire `resume_producer` subtree is preserved. The current intent is
updated before its first write, so its saved value and status identity
remain consistent. A later genuine output can be resumed only with the
same complete fields and exact new producer ledger.

`domain-operator/manifest.json` binds all nine full B/Gamma/Pi grids and
their source/query identities. Row parts include kind in both their
filename and manifest metadata. The original midpoint input states and
stations are separately preserved in
`original-collocation-midpoint-inputs.npz`. Original endpoint factors,
base fields, layout and all original finite beta arrays remain present.
The exporter uses at most256 angular rows per part and does not turn a
publication-size policy into a mathematical failure gate.

The original C-projection multipliers remain multipliers of that local
projection problem. No complete-H optimum or small complete-model KKT
residual is asserted. The separate complete-H branch remains an
independent computation from the same actual request29 parent.

## 5. New actual FD and scientific scope

`geometry_20261114_mixed_query_projection_response.py` actually reruns
the original complete affine Rphi derivative check on the new saved
warm. All original directions, centered steps, Richardson estimates and
the `5e-5` implementation threshold are retained. Its response binds
the actual new warm SHA and complete source ledger. No old pass or old
input hash is renamed.

The completed true T112 zero-H Jacobian is still held explicitly affine.
No actual new height is thresholded to zero, no nonlinear native solve
is performed here and no fresh nonlinear tail J or final audit is
claimed. All saved outputs remain `success=false`,
`new_coupled_finite_acceptance=false` and not a complete closed surface.
Every original final coupled/physical/native/closed-surface requirement
remains outstanding until actually satisfied.

## 6. Frozen source identities and exact CLI

Only AST parsing, source reads and byte hashing were performed locally.
All scientific execution belongs to this public repository's Actions.

| New source | Bytes | SHA256 |
| --- | ---: | --- |
| `geometry_20261114_mixed_query_domain_operator.py` | 26,683 | `34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854` |
| `geometry_20261114_mixed_query_projection_warm.py` | 10,173 | `d74d7a1c86cb131d262025cffa079a1a01a1ed7e5128ea339744c61cf4cfeac6` |
| `geometry_20261114_mixed_query_projection_response.py` | 2,829 | `5c871d96966a681e4fce607c0491db337c319854b568c5a038e46a560a0fa87c` |

The original observed-seven entry, seven-query entry, projection engine
and full-angle operator stay byte-for-byte frozen. With the same original
input files as request29:

```sh
python computations/geometry_20261114_mixed_query_projection_warm.py \
  --accepted "$ACCEPTED96" --prepared "$PREPARED699" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --resume "$ACTUAL29_WARM" \
  --expected-resume-sha f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9 \
  --out "$OUT/mixed-query-warm" --iterations 1 --lsmr-iterations 200 \
  --damping 270 --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200

python computations/geometry_20261114_mixed_query_projection_response.py \
  --accepted "$ACCEPTED96" --prepared "$OUT/mixed-query-warm/warm-001.json.gz" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --out "$OUT/physical-response"
```

The response runs only if a real new complete warm is saved. The actual
future result must report its full domain checks, new direction and
merit change; this interface asserts no numerical progress in advance.
