# Twenty-query continuation: original midpoint485 and the complete local layout

- Author: ChatGPT (GPT-6 Astra Pro), amplitude subtask.
- Classification: independent finite optimization implementation and source interface.
- Status: source, complete diffs and static checks are complete. The new twenty-query calculation has not run.
- Scope: an optimization warm for the existing complete finite equations. No nonlinear native-tail solution, accepted complete BVP, closed surface or research completion is claimed.

## 1. Actual evidence and the limited change

[The actual request64 receipt](2026-11-14-actual-request64-nineteen-query-nearest-midpoint485.md)
records an accepted optimization step at alpha1/32. At the nearest
rejected trial, alpha1/16, all original nodes and all nineteen modeled
angle grids were valid. The only failed original collocation midpoint
was interval485, with beta squared -0.009685047003464398 at original
physical-angle index997 and four negative values on its 2048-angle grid.
The original midpoint RHS was nonfinite, so the full RMS checks were
not executed at that rejected trial.

The independent configuration adds this complete original midpoint485
grid. It retains all nineteen earlier queries. It starts at the **saved
actual64 warm**, not at the base of request64 or its rejected trial. The
new A, row weights and complete B will therefore be formed at the new
actual base; their identity is not inherited from the preceding model.

Request64 also contains a material qualification: the farther alpha1/8
trial had valid original nodes and midpoints and valid selected grids,
but its actual fixed-weight merit increased from 43.79040176025459 to
43.79770161687097. Thus missing midpoint485 does not explain every
rejection. Adding its grid does not assert that a larger step will pass.
The original real-domain and actual-merit backtracking remains decisive.

## 2. Independent sources and schemas

All four nineteen-query sources and every earlier mathematical source
remain unchanged. The new files in `computations/` are:

| File | Bytes | SHA256 |
|---|---:|---|
| geometry_20261114_twenty_query_domain_operator.py | 32067 | 16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1 |
| geometry_20261114_twenty_query_condensed_warm.py | 41368 | 9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee |
| geometry_20261114_twenty_query_condensed_response.py | 2607 | 6890d58c28ea697bf025de85f0d276e351041ea8928afdb325d1162dadcece17 |
| geometry_20261114_twenty_query_collocation_observer_warm.py | 16712 | 4b2c875a58c9dfb43581922bfec983188c763b2014fc438cc918b178a50d6a05 |

The implementation-origin domain is the frozen nineteen-query source,
SHA 945114799a2cf564c59b463e1429b55119d4ad421bc5f3414c7143333e43d35e.
The parent warm source is
63ec6bd0da782933ad01628c686499d6325fa10df2c624f97c6f131a233e8d39.
The recursive SOURCE_NAMES/FROZEN ledger retains the complete preceding
sources. The observer pins the new warm SHA, and the FD entry consumes
the new producer schema and its complete actual source ledger.

The mathematical schema is
`exact-constraint-twenty-query-condensed-complete-H-warm-v1`.
The domain schema is
`captured-twenty-query-original-RMS-and-collocation-midpoint-domain-v1`.
Output identities name the current twenty-query entry, while the full
old nineteen-query producer subtree remains verbatim in the parent
chain. This is an independent implementation; the original module's
constants are not globally changed to relabel its results.

Seven complete mathematical function ASTs are identical to the frozen
nineteen-query implementation: query_value, selected_actual_angles,
evidence, the C projection bridge, the complete-H selection function,
and the captured linearization constructor and operator. Twelve separate
observer functions are also identical. The complete domain constructor
is intentionally changed only in query declarations and local-layout
assembly/identity; its original midpoint derivative assignments were
compared by AST and remain identical. Source parsing, literal index
checks and byte hashing were local; no mathematical source was imported
or numerically executed locally.

## 3. Typed queries and two different support descriptions

The first thirteen blocks are the original left-RMS grids:

~~~text
467, 468, 469, 470, 471, 472, 473, 475, 477, 479, 480, 481, 482
~~~

Each uses the original fraction 0.17267316464601146 and all 2048 original
physical-phi angles. The next seven blocks are the original collocation
midpoints:

~~~text
473, 475, 477, 480, 481, 482, 485
~~~

Every block records its query index, kind, interval, station and fraction.
The two kinds are not represented by one common fraction. There are
**40960** inequality rows, acting on all **236036** reduced coordinates.
The nineteen previous blocks retain their relative order; midpoint485
is appended after them.

The fourteen unique captured cells are the thirteen left-RMS cells plus
485. Their actual endpoint set is nodes467 through483, then485 and486:
nineteen physical nodes. Only these endpoint J/P blocks are captured
from the one unchanged original complete A construction. The exact
union of compiled B columns has **6425** coordinates: nineteen338-column
physical blocks and the three shared scalar-control columns.

R270's existing square-root library accepts a continuous run of complete
physical nodes plus all controls. The declared local layout is therefore
nodes467 through486, followed by the three controls, **6763 coordinates**.
The entire338-column node484 block is explicitly zero in B. It is an
ordinary unknown of the full quadratic model and retains all original
Hessian couplings; it is not fixed or silently eliminated from H.

| Object | Nodes or columns | Dimension |
|---|---|---:|
| Actual query endpoint capture | 467..483, 485, 486 | 19 physical nodes |
| Actual compiled B column union | Those endpoints and all p | 6425 |
| Declared continuous R270 local layout | 467..486 and all p | 6763 |
| Explicit zero B layout block | Node484 | 338 |
| Baseline C correction support | 471..482 and all p | 4059 |

The constructor computes the union of every block's actual global
columns, computes the independent declared layout, and checks that the
set difference is exactly the complete node484 block. It then obtains
each block's local indices by search in the declared layout. Both the
full-coordinate and local transposes initialize zero arrays and scatter
the same frozen block products. Consequently node484's B-transpose
component is zero, while its full H response remains part of the
condensed problem.

The model hash explicitly binds the declared indices, actual block-column
union and zero-layout indices, as well as all typed blocks, original
base data and sources. The artifact export preserves the declared
local-index array and actual endpoint-index array. The original complex
query-chain check uses actual query endpoints; it does not add a query
or an extra endpoint capture at484. The original full A still contains
every original node, including484.

## 4. Original midpoint and complete derivative chain

The added base value comes directly from `state.middle[485]`, and its
station directly from `problem.mid[485]`. It is not replaced by a
linear average, a left-RMS value or a separately recomputed whole flow.
The original midpoint formula supplies its derivative:

$$
y_m=\frac{y_L+y_R}{2}-\frac h8(f_R-f_L).
$$

With original physical endpoint Jacobians J_L,J_R and shared-control
columns P_L,P_R, the full variation is

$$
\delta y_m=
\left(\frac12I+\frac h8J_L\right)\delta y_L+
\left(\frac12I-\frac h8J_R\right)\delta y_R+
\frac h8(P_L-P_R)\delta p.
$$

If Gamma is the beta-squared derivative with respect to the original
physical query state, and Pi its direct scalar-control derivative, the
compiled blocks are

$$
B_L=\Gamma\left(\frac12I+\frac h8J_L\right),\qquad
B_R=\Gamma\left(\frac12I-\frac h8J_R\right),\qquad
B_p=\frac h8\Gamma(P_L-P_R)+\Pi.
$$

The original exact-coordinate inlet chain remains in the constructor,
and the column scale S is divided once. The new query uses original
endpoints485 and486. Their J/P blocks come from the existing complete
linearization; no second complete Jacobian is formed. The original
typed query readout, actual complex-chain check, adjoint check and
local/full check remain in place with their original thresholds.

All original midpoint states/stations, compiled B/Gamma/Pi chunks,
beta-squared values, coordinate maps and endpoint J/P bytes are exported.
These finite checks neither certify continuous positivity between angle
nodes nor constitute complete BVP acceptance.

## 5. Full-H elimination and unchanged C baseline

The R270 library remains the original source
84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b.
It receives the continuous6763-column layout, uses the original affine
term from the complete gradient, retains every pure-global row and all
three controls, and recovers the conditional response of the exterior
variables through the original complete-chain solve. A zero B column
does not remove the corresponding unknown from its local quadratic.

The baseline C projection still corrects nodes471 through482 and all
three controls,4059 coordinates. Its offset is the complete
`c+B_out*z0_out`, now including outside nodes467,468,469,470,483,484,485
and486. The484 B contribution is structurally zero, rather than a reason
to drop other outside columns. The C direction is still compared with
the complete-H candidate using the same fixed-model objective.

The original full-vector radial repair and feasible-ray backup remain.
They can rescale coordinates outside the C correction support too; the
final outside direction is not claimed unchanged. All final candidates
still undergo the original complete A/AT/B/BT readback, actual gdot,
all-row slack and same-objective selection before real backtracking.

## 6. Exact parent pair and later own-schema continuation

The initial parent is completed request64 run43648987661, source
d625bb293e07541b4bf717524e14a45392be03aa. Its public directory is
`notes/public-actions-43648987661-1-condensedqp/`.

| Original parent file | Bytes | SHA256 |
|---|---:|---|
| nineteen-condensed-warm/warm-001.json.gz | 4809173 | 3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e |
| nineteen-condensed-warm/driver-status.json, original decoded bytes | 1798797 | 037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466 |

The workflow copies the compressed warm bytes exactly. It accepts the
published status JSON or its gzip alias, decompresses an alias and
checks the original decoded JSON SHA before writing the parent copy.
It does not parse and reserialize status to manufacture matching bytes.
If both aliases are present, their decoded bytes must agree.

A nineteen-query parent must be this exact actual64 pair. A future
twenty-query parent may be supplied only after an actual completed step,
with its explicit warm/status SHA pair. The inherited validator retains
the complete producer/source ledger, frozen scalar identity, field and
mesh identity, constant-state conditions, status identity and real
optimization progress checks. The previous nineteen-query producer
subtree is preserved. An optimization warm remains unaccepted as a
complete BVP.

## 7. Preserved budgets, observers and original checks

| Parameter | Intended request66 value |
|---|---:|
| Complete model calls | 1 |
| Damping lambda | 270 |
| Original LSMR iterations | 200 |
| Baseline C projection sweeps | 200 |
| Maximum local working rows | 512 |
| Local dual sweeps | 200 |
| Overall budget seconds | 1200 |
| Complete-H candidate seconds | 600 |
| Original-trial reserve seconds | 90 |
| Final recovery reserve seconds | 30 |
| Original backtracking trials | 17 |
| Material-angle check count | 4096 |
| Original physical angles per selected query | 2048 |

The original actual-merit decrease test, all-node and original midpoint
domain checks, both full RMS scans, core/material-angle guards and
complete boundary checks remain unchanged. When a nonfinite original
midpoint RHS prevents the RMS scan, the report records that unperformed
scope. A selected inequality grid is not substituted for the real
nonlinear gate.

The read-only col-location observer executes each original evaluate and
weights method once. It reads only arrays already returned, and retains
the complete physical argmax, signed residual, component, station and
the original row weight fixed for that model. It adds no RHS, Jacobian,
model action or trial; observer exceptions do not replace the original
scientific return or decision.

The new response entry repeats all original complete Rphi directions,
step levels and Richardson checks at the actual newly saved warm. Its
true zero-H T112 Jacobian remains explicitly affine. This is not a new
native nonlinear solve at the new H, and no old FD pass is relabelled.
The original5e-5 implementation threshold remains unchanged.

## 8. Executable one-model interface

After the unchanged public78 source, original M112 preparation and the
actual64 parent have been restored, the one-model command is:

~~~bash
python -u computations/geometry_20261114_twenty_query_collocation_observer_warm.py \
  --accepted "$ACCEPTED96" --prepared "$PREPARED112" \
  --tail-anchor "$ACTUAL_T112_ZERO_ANCHOR" --tail-config "$T112_CONFIG" \
  --resume "$PARENT64/warm-001.json.gz" \
  --expected-resume-sha 3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e \
  --parent-status "$PARENT64/driver-status.json" \
  --expected-parent-status-sha 037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466 \
  --out "$OUT/twenty-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
~~~

After checking the returned original status and SHA of its declared
latest warm, the original actual-warm derivative check is:

~~~bash
python -u computations/geometry_20261114_twenty_query_condensed_response.py \
  --accepted "$ACCEPTED96" --prepared "$ACTUAL_NEW_WARM" \
  --tail-anchor "$ACTUAL_T112_ZERO_ANCHOR" --tail-config "$T112_CONFIG" \
  --out "$OUT/physical-response" --angles 4096
~~~

The output keeps the existing status/warm/model, complete source and
parent ledgers, typed domain arrays, complete-H and C evidence, raw local
root/recovery files, every original trial, midpoint observer and col
observer. Large raw arrays remain in the complete Actions artifact and
are not compressed into misleading scalar claims. The run has not yet
been executed when this interface is written.
