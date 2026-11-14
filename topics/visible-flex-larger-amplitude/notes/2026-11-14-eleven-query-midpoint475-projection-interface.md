# Eleven-query continuation from actual request35

**Status: executable independent source and static interface check.**
No eleven-query numerical run is asserted here. Every scientific
evaluation belongs to the public repository's Actions.

[Actual request35](2026-11-14-actual-request35-ten-query-step-and-midpoint475.md)
accepted a complete-domain warm step of `1/16`. At the nearest rejected
step `1/8`, all ten modeled angular grids were positive; the only bad
original collocation midpoint was interval475, with beta-squared
minimum `-0.09677364082856954` at phi0 and six negative angles. The new
entry adds exactly that complete midpoint grid. It continues the actual
request35 output, without returning to the old preparation or changing
the original ten-query source.

## 1. Independent files and source identities

All paths below are relative to this topic.

| File | Bytes | SHA256 |
| --- | --- | --- |
| `computations/geometry_20261114_eleven_query_domain_operator.py` | 27,346 | `55358acb92bac869ba2ca1daf2da7772d57be31ccd1fcfd9f7324af80f8ea20b` |
| `computations/geometry_20261114_eleven_query_projection_warm.py` | 13,402 | `6aed0dda5515945c73413884fb98d1719eb23fc40ff6b7388805f6108816c298` |
| `computations/geometry_20261114_eleven_query_projection_response.py` | 3,128 | `85d0bb81ee969d621c1e2d52a314ad4674caccf1585aa1a079bd453aaa8de3c1` |

The operator is an independently named copy of the ten-query
implementation with an explicit three-midpoint list and new schema,
source identity, row order and count. Its construction, original query
evaluation, actual-angle readout, verification and export kernels are
AST-identical to the frozen ten-query versions after omitting only
string literals. It does not mutate constants in the old module.
The direct implementation origin is bound to ten-query operator SHA
`5c9b145862a4f12cbbc5334e1b96e540458a58908c4889b966979995700d5dbd`.

The warm entry retains original engine SHA
`7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`
and original observer entry SHA
`94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228`.
It binds its direct ten-query parent entry to
`90e22ebbd0089970a77986f1be9352a1ec1581346a2fe2ef25478720136f6941`.
The original generic captured operator and complete residual, exact
coordinates, regularized LSMR, C projection, feasible-segment selection,
backtracking and boundary functions remain frozen.

## 2. Exact parent and original problem inputs

The first eleven-query call requires this actual pair:

| Input | SHA256 |
| --- | --- |
| Actual35 `ten-query-warm/warm-001.json.gz` | `24ca673e64fb60d1d5206ec742ce08c653b390bafd5ecd3ffbe54f0b1c1cd25a` |
| Actual35 `ten-query-warm/driver-status.json` | `214d4eed229c8b63af29bda765dca4506de1646a3addcbd02d0b626068ebf1ff` |
| Original accepted96 source | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| Original complete prepared699 input | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| Completed real zero-H T112 response/J | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| Original T112 configuration | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

The actual35 pair is from public run43616658549. The entry reads and
checks the caller-declared SHA for both files, then checks the above
first-parent identities. The status must record one accepted warm step,
actual optimization progress, the matching latest warm hash and false
BVP acceptance flags. Every status identity value must equal the
corresponding value in the complete warm producer.

The preserved producer checks also bind the original accepted96,
prepared699, true zero-H anchor and tail configuration; all original
699 mesh points; the full physical representation; the complete scalar
formula and actual current three parameters; and the complete source
set. The prior producer subtree is never rewritten. The new current
source ledger contains the twenty-two prior producer files plus the
new warm entry and new operator, for twenty-four files.

The actual M112 field still has 338 physical and 453 augmented rows at
699 nodes, with 236,036 exact-coordinate variables. Exact inlet
relations and constant global core/control variables are retained. The
small current height is an actual nonzero finite input; it is not
thresholded to zero or replaced by the original preparation.

## 3. Typed query set and reuse of the original factors

| Group | Kind | Interval | Fraction |
| --- | --- | --- | --- |
| `0` | Left RMS | `471` | `0.17267316464601146` |
| `1` | Left RMS | `472` | Same left RMS fraction |
| `2` | Left RMS | `473` | Same left RMS fraction |
| `3` | Left RMS | `475` | Same left RMS fraction |
| `4` | Left RMS | `477` | Same left RMS fraction |
| `5` | Left RMS | `479` | Same left RMS fraction |
| `6` | Left RMS | `480` | Same left RMS fraction |
| `7` | Left RMS | `481` | Same left RMS fraction |
| `8` | Original collocation midpoint | `473` | `0.5` |
| `9` | Original collocation midpoint | `475` | `0.5` |
| `10` | Original collocation midpoint | `477` | `0.5` |

Every group contains all 2048 original physical-phi grid points.
Consequently B has an expected 22,528 rows, not ten rows or eleven
single-angle constraints. The unique endpoint-capture intervals remain
`(471,472,473,475,477,479,480,481)`. They cover the same twelve physical
nodes471 through482. The expected local support remains 4,059 columns:
twelve times338 physical columns plus three global controls. Adding
midpoint475 does not expand that node set because its endpoints475 and
476 were already required by the existing left RMS475 block.

The base of every midpoint block is directly the actually returned
`state.middle[j]` and `problem.mid[j]`. No RMS interpolation or plain
nodal average is substituted. With the original nodal physical J/P
factors, the derivative is

$$
\delta y_m=\frac{\delta y_L+\delta y_R}{2}
+\frac{h}{8}(\delta f_L-\delta f_R).
$$

For the query's physical gradient Gamma and direct scalar-control
gradient Pi, the stored physical blocks are

$$
B_L=\frac12\Gamma+\frac h8\Gamma J_L,\qquad
B_R=\frac12\Gamma-\frac h8\Gamma J_R,
$$

$$
B_p=\frac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

The exact inlet chart is retained by the generic implementation, and
the coordinate scale divides each actual column exactly once. All
forward, transpose, local and global actions use the same frozen
compiled rows. Shared nodes and global controls scatter-add in the
transpose. The three midpoint blocks reuse original endpoint J/P
values captured during the one original full A construction. They
do not trigger another complete Jacobian or a nonlinear tail call.

The operator schema is
`captured-eleven-query-original-RMS-and-collocation-midpoint-domain-v1`;
the warm schema is
`exact-constraint-eleven-typed-query-feasible-projection-warm-v1`.
Each query retains its kind, interval, fraction, station and group index
in the model, verification, original-angle trial readout and export.
The generic top-level fraction is null, because the mixed query kinds
do not share one fraction. All current aliases are added to the live
identity before writing the first intent, so the later status and warm
carry the same values. The entire old `resume_producer` is excluded from
current-alias rewriting.

## 4. Unchanged algorithm and acceptance scope

This changes only the finite optimizer query set. The entry uses the
same complete positive-damping model, lambda270, original column
diagonal, at most200 LSMR iterations with the original tolerances, and
at most200 cyclic Hildreth sweeps. The selected reserve is the original
algorithmic theta1/2. Radial repair, the feasible original-ray backup
and the same-model segment minimization are unchanged. All complete
rows are rechecked after repair and composition.

The local C projection is not relabeled as the full-H model optimizer;
its multipliers are not full-model KKT multipliers. The actual complete
model derivative and original full gradient are retained, and the
penalty is not added to the actual nonlinear merit. Each real trial
recomputes the full original nodal and midpoint RHS. It retains the
original seventeen possible step sizes, fixed-weight merit/ratio,
whole-mesh two-RMS test and uniform-phi rho guard.

The midpoint observer calls the original residual evaluator exactly
once and reads its returned arrays. Its diagnostic exception handler
does not intercept an original mathematical evaluation failure, alter
the finite flag, alter residual bytes, or create a new science gate.
Real nonlinear failure on an already selected grid remains possible;
the complete original backtracking is therefore retained.

Before projecting, the original actual B/transpose and full complex
Hermite-chain checks run with their unchanged implementation
thresholds. They include the actual whole LSMR direction and the seeded
direction. The export retains original Gamma/Pi, all compiled rows,
all original beta values, all original endpoint J/P factors and the
three actual midpoint input arrays, with typed metadata and raw hashes.
Artifact parts keep the existing at-most256-angle row chunks. There is
no artifact-size mathematical rejection.

Every saved field still declares false BVP and closed-surface acceptance.
The complete real zero-H T112 Jacobian is explicitly held affine. The
fresh response entry runs every original full Rphi FD direction and
Richardson step with the unchanged `5e-5` implementation threshold at
the newly saved warm. The new warm's hash and full producer are bound;
neither an old FD pass nor its input hash is relabeled. No actual
nonlinear native solution or new native Jacobian at the new height is
asserted.

## 5. Exact Actions invocation

Run from this topic's `computations` directory with the original inputs
restored under the variables below. The source itself verifies the
public repository and the GitHub Actions environment.

```bash
python geometry_20261114_eleven_query_projection_warm.py \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED699" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --resume "$ACTUAL35/ten-query-warm/warm-001.json.gz" \
  --expected-resume-sha 24ca673e64fb60d1d5206ec742ce08c653b390bafd5ecd3ffbe54f0b1c1cd25a \
  --parent-status "$ACTUAL35/ten-query-warm/driver-status.json" \
  --expected-parent-status-sha 214d4eed229c8b63af29bda765dca4506de1646a3addcbd02d0b626068ebf1ff \
  --out "$VISIBLE_OUT/eleven-query-warm" \
  --iterations 1 --lsmr-iterations 200 --damping 270 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200
```

If that step produces a real progressed warm, run:

```bash
python geometry_20261114_eleven_query_projection_response.py \
  --accepted "$ACCEPTED96" \
  --prepared "$VISIBLE_OUT/eleven-query-warm/warm-001.json.gz" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --out "$VISIBLE_OUT/physical-response"
```

The warm writes its current intent, full model, LSMR and selected
directions, typed B/gradient/factor exports, all trial angular margins,
original midpoint observer arrays, paired status and actual new warm.
The expected 22,528-row and twelve-node figures are a declared interface
size, not an already executed check. The actual job must report its
measured sizes, timings, source hashes, original-domain outcomes,
decrease, new H and FD result.

## 6. Reusing one frozen entry for later consecutive models

The original engine intentionally accepts only `--iterations 1` and
implements exactly one model. Merely increasing that flag is invalid.
The eleven-query wrapper also accepts a genuine preceding output of
its own schema, provided its paired status identifies that exact warm,
records one real progressed warm step, and matches the complete current
source ledger and producer. Only the first parent of the older ten-query
schema has the fixed actual35 hard lock above.

Consequently later consecutive models can use the very same frozen
entry in separate subprocesses and output directories. Each call uses
the actual previous `warm-001.json.gz` and `driver-status.json`, with
their actual file hashes; it constructs a new original complete model
at that field and refreshes then freezes that model's weights. It saves
the model and actual warm before another call starts. The corresponding
fresh FD entry remains the same frozen source.

A short external orchestrator can stop on a real missing progressed
warm, an original domain/implementation failure, the planned model
count, or its total computational budget while preserving every
completed stage. Such orchestration must retain separate actual
statuses; it must not overwrite the paired first-stage status, flatten
the producer chain, fabricate one stage's acceptance from another, or
subtract merits across refreshed weight systems. No such multi-stage
execution is asserted by this interface note, and no change to the
frozen original engine is needed to support it.
