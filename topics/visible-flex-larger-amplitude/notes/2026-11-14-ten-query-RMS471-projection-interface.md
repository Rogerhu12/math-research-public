# Ten-query continuation from the actual request32 warm

This is the executable continuation selected from
[the actual request32 record](2026-11-14-actual-request32-nine-query-warm-and-RMS471.md).
It retains the seven original left RMS angular grids and original
collocation midpoint473/477 grids, and adds the complete left RMS471
grid that actually blocked steps `1/16` through `1/128`. The input is
the new request32 warm, not a restart from request29 or the original
699-node preparation. This entry produces another unaccepted warm and
a fresh complete affine boundary FD; it does not declare a new native
tail or BVP acceptance.

## 1. Independent frozen sources

| New source | Bytes | SHA256 |
| --- | --- | --- |
| `computations/geometry_20261114_ten_query_domain_operator.py` | 27,338 | `5c9b145862a4f12cbbc5334e1b96e540458a58908c4889b966979995700d5dbd` |
| `computations/geometry_20261114_ten_query_projection_warm.py` | 13,061 | `90e22ebbd0089970a77986f1be9352a1ec1581346a2fe2ef25478720136f6941` |
| `computations/geometry_20261114_ten_query_projection_response.py` | 2,964 | `15cf929502d30658ddeb31efac3633f27ca17879746dd3d0879e7759d23757bc` |

The original nine-query sources and every earlier numerical producer
remain unchanged. The new operator is an explicit independent version
of the frozen nine-query implementation, with the new query list,
schema, source identity and descriptive metadata. It does not mutate
the old operator module's constants at runtime. It verifies the old
implementation-origin source SHA
`34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854`
and records both that provenance and its own current source.

AST checks passed on all three new files. A static comparison of the
operator's capture, query readout, constructor, verification and export
functions found the same AST as the frozen nine-query functions after
only version-word substitutions in strings. In particular the complete
Gamma/Pi formulas, nodal J/P chain, exact-coordinate scaling, forward
and transpose operations, real query formulas and implementation-check
thresholds were not changed. No numerical module was imported or
scientific computation run during these checks.

## 2. Typed query order and complete coordinates

The operator schema is
`captured-ten-query-original-RMS-and-collocation-midpoint-domain-v1`.
Its declared order is:

| Groups | Kind | Intervals | Fraction |
| --- | --- | --- | --- |
| `0..7` | `left-RMS` | `471,472,473,475,477,479,480,481` | `0.17267316464601146` |
| `8..9` | `collocation-midpoint` | `473,477` | `0.5` |

All 2048 original physical angles are retained in every group. The
combined B has 20,480 rows and the original 236,036 scaled-coordinate
columns. Its possible local support is 4,059 columns: the physical
coordinates at nodes471 through482 and all three global controls.
These dimensions follow from the declared layout; runtime counts and
actual stored byte identities are still reported by Actions.

Only endpoint capture is deduplicated, to eight distinct intervals.
Different query kinds with the same interval ID are never merged. The
two original midpoint endpoint pairs are in the same declared capture.
The original complete Jacobian construction remains unique; the
operator records the required original return values rather than
constructing a second whole Jacobian. If a shared endpoint is returned
in two original chunks, the frozen capture only deduplicates it when
the actual J/P bytes agree.

The new left RMS471 query is the original cubic Hermite interpolant at
the original left RMS station. The retained midpoint bases are direct
`state.middle[j]` and `problem.mid[j]` values. The midpoint direction is

$$
\delta y_m=\frac{\delta y_L+\delta y_R}{2}-\frac{h}{8}(\delta f_R-\delta f_L).
$$

The two full nodal RHS Jacobians, their shared scalar-control columns,
the query's direct scalar derivative and the coordinate scale appear
exactly as in the actual nine-query operator. Any exact inlet chain is
handled by the unchanged general coordinate rule; all ten selected
queries here are interior. All global core and control variables remain
in the original complete residual and A operator.

The `unchanged_left_component_model_sha256` compatibility field refers
to the component built by the frozen generic left-RMS compiler on this
current input and eight-query list. It does not assert that the new
component has the numerical bytes of the previous seven-query model.
The new full model hash includes the actual new base, all typed queries,
new source identity, actual Gamma/Pi and compiled row identities.

## 3. Exact parent and producer binding

The first parent pair is fixed to the original actual request32 bytes:

| Parent item | SHA256 |
| --- | --- |
| `mixed-query-warm/warm-001.json.gz` | `7f5e8d5f888b79c4ce0c0db91c9bc4e27bb9ef0c7554c0f578431ddbbecb578e` |
| `mixed-query-warm/driver-status.json` | `a6224f936f261168ef05a3b51fa3b1318b6d25eacf6653c412d2c33a8731d56e` |

Both expected hashes must be supplied on the CLI and match the real
files. The parent status must identify the same completed one-step
unaccepted warm, with `optimization_progress=true`, its matching warm
SHA, and false scientific acceptance flags. Its entire identity must
equal the corresponding fields in the saved warm producer. The full
producer ledger, all 20 actual parent source hashes, original mesh,
field representation, complete scalar formula and actual control
values are checked. The complete old producer object is retained under
`resume_producer`, without relabelling any of its old query counts,
schemas or outcomes.

The new warm schema is
`exact-constraint-ten-typed-query-feasible-projection-warm-v1`.
Its current ledger contains 22 sources: the two new numerical producer
files and all 20 sources of the parent. A later output of this same
frozen entry can be resumed only through its matching complete status,
warm, input and source identities. The initial parent remains clearly
distinguished from that actual later parent.

The new entry consumes only `--parent-status` and
`--expected-parent-status-sha` before forwarding every original option
to the frozen engine. Those are actual provenance checks, not new
scientific acceptance thresholds. The original CLI still requires one
model, damping270, at most 200 LSMR iterations and projection sweeps,
at most 17 trial steps, and the original angle counts. All current query
aliases enter the live intent before it is written, so the saved intent,
status identity and warm producer retain the same current alias fields.
The harmless extra query-order alias in the original request32 intent
is preserved as original provenance; its files are not rewritten.

## 4. Unchanged direction algorithm and original nonlinear checks

The independent entry retains the complete actual weighted A, b and
positive-damping model, original column preconditioner, full raw LSMR
direction, C-local Hildreth projection, complete-row radial repair and
same-model feasible-segment selection. The reserve remains one half of
each actual base beta-squared value. Every one of the 20,480 linear
slacks is checked after every repair and combination. No complete-QP
optimality or small original KKT residual is inferred from local
projection stationarity.

The selected direction is restored to the exact original coordinates
with the original single division by the coordinate scale. Its actual
full A action, true model derivative and actual model decrease are
retained. The real trial uses fresh original nodal RHS values and the
actual original nonlinear midpoint construction. All original nodes,
collocation midpoints, both full RMS grids, the original uniform rho
guard, complete boundary residual and fixed-weight merit check remain.
The original 17 trial steps are not extended.

The same read-only original midpoint observer wraps the actual
residual evaluation once. It reads the original returned middle and
midpoint RHS arrays, preserves bad original rows and full angular
readouts, and reports unchanged original return flags and residual
bytes. Observer or export exceptions are diagnostics only; an
exception from the original mathematical evaluation still propagates.
No extra whole flow or whole Jacobian call is made by this observer.

## 5. Exact Actions CLI

With the same public inputs used for requests30 and32, and the actual
request32 parent pair:

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_ten_query_projection_warm.py" \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED699" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --resume "$ACTUAL32_WARM" \
  --expected-resume-sha 7f5e8d5f888b79c4ce0c0db91c9bc4e27bb9ef0c7554c0f578431ddbbecb578e \
  --parent-status "$ACTUAL32_STATUS" \
  --expected-parent-status-sha a6224f936f261168ef05a3b51fa3b1318b6d25eacf6653c412d2c33a8731d56e \
  --out "$VISIBLE_OUT/ten-query-warm" \
  --iterations 1 --lsmr-iterations 200 --damping 270 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200

python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_ten_query_projection_response.py" \
  --accepted "$ACCEPTED96" \
  --prepared "$VISIBLE_OUT/ten-query-warm/warm-001.json.gz" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --out "$VISIBLE_OUT/physical-response"
```

The second command is run only if the first actually saves that new
warm. It does not convert a failed/no-progress status into a warm. The
old baseline inputs retain their original hashes:

```text
accepted96:
b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff
prepared699:
0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714
true zero-H T112 anchor:
e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51
T112 config:
01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5
```

Scientific execution is restricted by the original engine and domain
operator to this public repository's Actions. The 1200-second allowance
is a work budget, not permission to accept a larger residual. No
full-H direction helper or nonlinear native-tail solve is invoked by
this experiment.

## 6. Expected actual output and interpretation

The ordinary saved outputs remain `optimization-intent.json`,
`model-000.json`, original operator checks, raw and selected directions,
all-query linear margins, every actual trial's typed angular readout,
`driver-status.json`, and a new warm only after real accepted descent.
`domain-operator/manifest.json` retains every B/Gamma/Pi row block,
original endpoint factors, actual bases, the original two midpoint
rows and stations, and their byte hashes. Angular chunks remain at most
256 rows. Git's file-size publication policy is not a mathematical
failure condition.

The actual report must distinguish RMS471 from midpoint471 and retain
both query kinds at intervals473/477. It must report all other original
bad nodes, midpoints or RMS points even when the ten modeled query grids
remain positive. A successful model step or FD does not replace the
original final BVP gates or a later geometric readout.

The response entry consumes the new warm and actually repeats the
original complete Rphi directions, centered steps, Richardson estimates
and `5e-5` implementation check. It uses the genuine completed zero-H
T112 Jacobian as an explicitly affine map, records the actual new native
height and preserves all its coefficients. It neither relabels an old
FD pass nor calls a nonzero height solved. The next mathematical
acceptance still requires a true nonlinear response, final native audit
and all original complete-field acceptance conditions.
