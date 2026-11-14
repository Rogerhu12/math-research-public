# Nineteen-query continuation: add the original midpoint480 grid

- Author: ChatGPT (GPT-6 Astra Pro), amplitude subtask.
- Classification: independent finite optimization implementation and source interface.
- Status: source, complete diffs and static interface checks are complete. The new nineteen-query calculation has not run.
- Scope: an optimization warm for the same complete finite equations. No nonlinear native-tail solution, accepted complete BVP, closed surface or research completion is claimed.

## 1. The actual reason for this change

[The actual request63 receipt](2026-11-14-actual-request63-nearest-midpoint480.md)
records an accepted optimization step at alpha1/128. At the nearest
rejected trial, alpha1/64, all original nodes and every existing eighteen
modeled angle grid were valid. The only original collocation-midpoint
failure was interval480. Its saved minimum beta squared was
-0.011295551381192093 at physical-angle index162, with four negative
values on the original 2048-angle grid. The original midpoint RHS was
nonfinite, so the full RMS scan was not executed at that rejected trial.

This independent configuration adds that original midpoint480 grid and
retains all earlier queries. Left-RMS480 remains a different query at its
original station. No farther failed point from a larger rejected trial
is added. These are observations from request63, not a prediction that
the new nineteenth-query direction will permit a larger nonlinear step.

The new model starts at the **saved actual63 warm**, not at the base of
the actual63 optimization model and not at its rejected alpha1/64 trial.
Consequently, the new A, row weights, complete B and fixed-model objective
will be freshly formed at the new actual base. They are not assumed to
equal the matrices or weights of request63.

## 2. Four independent frozen sources

All four old eighteen-query files remain unchanged. The new files are:

| File in computations | Bytes | SHA256 |
|---|---:|---|
| geometry_20261114_nineteen_query_domain_operator.py | 29481 | 945114799a2cf564c59b463e1429b55119d4ad421bc5f3414c7143333e43d35e |
| geometry_20261114_nineteen_query_condensed_warm.py | 40216 | 63ec6bd0da782933ad01628c686499d6325fa10df2c624f97c6f131a233e8d39 |
| geometry_20261114_nineteen_query_condensed_response.py | 2613 | 6b497ddec4dbf9a307f5501b352fc520d115f08a9eb7d5e8b6cb8dd03cf965bb |
| geometry_20261114_nineteen_query_collocation_observer_warm.py | 16720 | 7fee2874557ca6681743bc5607a2ea59a72c2b3f474bc9fc701898569bb62282 |

The domain source pins its implementation origin to the original
eighteen-query domain SHA
ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051.
The warm imports the frozen eighteen-query warm as its parent, with SHA
b9f7d9150c57cff485f5f891881870095fc91f7a58fd40f63544e6bb9c3ef335.
Its recursive SOURCE_NAMES/FROZEN ledger retains all preceding sources.
The read-only execution wrapper pins the new warm SHA, and the new FD
entry consumes the new producer schema and its complete actual ledger.

The current mathematical schema is
`exact-constraint-nineteen-query-condensed-complete-H-warm-v1`.
The domain schema is
`captured-nineteen-query-original-RMS-and-collocation-midpoint-domain-v1`.
Current metadata names the nineteenth-query source. The complete old
eighteen-query and earlier producer subtrees are preserved verbatim.

Eight complete mathematical function ASTs were compared against the
frozen eighteen-query implementation: query_value,
selected_actual_angles, the domain constructor, evidence, the original
C projection bridge, the complete-H selection function, and the captured
linearization constructor/operator. All eight are identical. Twelve
separate observer functions are also identical. Comments, current source
identities, the declared query tuple, parent pins and descriptive output
fields change; no old mathematical source was edited or executed locally.

## 3. Query order and unchanged complete support

The first thirteen blocks are the original left-RMS grids, in this order:

~~~text
467, 468, 469, 470, 471, 472, 473, 475, 477, 479, 480, 481, 482
~~~

Each uses the original left-RMS fraction
0.17267316464601146 and all 2048 original physical-phi angles. The next
six blocks are original collocation midpoints:

~~~text
473, 475, 477, 480, 481, 482
~~~

Every row carries a query index, kind, interval, station and fraction.
The two kinds are never represented as one common fraction. Inserting
midpoint480 before the old midpoint481/482 changes those last two query
indices, so consumers must read the typed query declarations rather than
reuse old row numbers.

There are 19 times 2048, or **38912**, finite inequality rows. All
midpoint cells already occur among the thirteen left-RMS cells. Thus the
one original endpoint capture still covers the same thirteen unique cells
and the same seventeen physical nodes467 through483. No new node or
second complete Jacobian is requested. The full reduced dimension is
236036, and the B support contains the seventeen complete physical-node
blocks plus all three global scalar controls: **5749 coordinates**.

The baseline C projection continues to correct nodes471 through482 and
all three global controls, **4059 coordinates**. Its effective offset
remains the complete expression c+B_out*z0_out, including outside nodes
467,468,469,470 and483. The existing full-vector radial repair and
same-objective backup selection may rescale the outside direction too;
the final outside direction is not claimed unchanged. The complete-H
candidate retains the affine optimal response of every outside variable,
including free core coordinates, through the original R270 elimination
and complete-chain recovery.

## 4. Original midpoint identity and complete derivative chain

For the new query, the base value is taken directly from
`state.middle[480]` and its station directly from `problem.mid[480]`.
It is not rebuilt as an average of nodal positions, substituted with the
left-RMS point, or taken from a newly evaluated whole-field RHS. The
original midpoint formula is retained for the derivative and for the
separately reported reconstruction difference:

$$
y_m=\frac{y_L+y_R}{2}-\frac{h}{8}(f_R-f_L).
$$

Let J_L,J_R denote the physical endpoint Jacobians and P_L,P_R their
global scalar-control columns, all from the one original complete A
construction. For physical nodal variations and the shared control
variation, the derivative is

$$
\delta y_m=
\left(\frac12I+\frac h8J_L\right)\delta y_L+
\left(\frac12I-\frac h8J_R\right)\delta y_R+
\frac h8(P_L-P_R)\delta p.
$$

If Gamma is the original query beta-squared derivative with respect to
physical query state, and Pi is its direct scalar derivative, the blocks
are

$$
B_L=\Gamma\left(\frac12I+\frac h8J_L\right),\qquad
B_R=\Gamma\left(\frac12I-\frac h8J_R\right),\qquad
B_p=\frac h8\Gamma(P_L-P_R)+\Pi.
$$

The complete exact-coordinate chart is retained, and column scaling by
its S is applied once. The general inlet chain remains in the frozen
constructor. The new midpoint uses already captured endpoints480 and481.
Forward and transpose actions use the same compiled rows. The original
whole-direction complex-chain, adjoint and local/full implementation
checks remain unchanged. These are finite implementation checks; they
do not establish continuous all-angle positivity or complete BVP success.

Export includes the actual original midpoint arrays and stations,
typed B/Gamma/Pi blocks, all beta-squared rows, local/global column maps,
original endpoint J/P bytes, source ledger and model identity. Changing
the declared query set does not relabel the old eighteen-query output.

## 5. Exact first parent and later own-schema continuation

The initial parent is the completed public request63 run43646179305,
source db6d728f30ee2d0c9ea62c96c622d8d85d2354b2:

| Original file | Bytes | SHA256 |
|---|---:|---|
| eighteen-condensed-warm/warm-001.json.gz | 4799943 | 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a |
| eighteen-condensed-warm/driver-status.json, original decoded bytes | 1810333 | 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46 |

The published directory is
`notes/public-actions-43646179305-1-condensedqp/`.
The workflow preserves the compressed warm bytes. It accepts either
public original status JSON or its gzip alias, decompresses an alias and
checks the **original JSON byte SHA** before writing the parent copy.
It does not parse and reserialize the status to manufacture matching
bytes. If both aliases exist, their decoded bytes must agree.

The independent warm validates the pair again. An eighteen-query parent
must be this exact actual63 pair. After a real nineteenth-query step is
saved, an own-schema parent may be supplied with its own explicit actual
warm and status SHA values. The original producer/source set, frozen
scalar identity, complete mesh and field representation, constant-state
conditions, status identity and progress assertions remain checked by
the original validator. The old twelve-query main is not called; its
validator is bound explicitly to the current and parent schemas.

One invocation requests exactly one model. This interface does not
silently increase iterations, treat a warm as an accepted BVP, or approve
a future parent that has not yet been produced.

## 6. Unchanged optimization and scientific checks

The intended request64 budgets are unchanged from request63:

| Parameter | Value |
|---|---:|
| damping lambda | 270 |
| original LSMR iterations | 200 |
| baseline C projection sweeps | 200 |
| maximum local working rows | 512 |
| local dual sweeps | 200 |
| complete model calls | 1 |
| overall budget seconds | 1200 |
| complete-H candidate seconds | 600 |
| original-trial reserve seconds | 90 |
| final recovery reserve seconds | 30 |
| original backtracking trials | 17 |
| material-angle check count | 4096 |
| original physical domain angles per selected query | 2048 |

The original complete A, A-transpose, B and B-transpose readbacks,
same-fixed-objective C/H comparison, original feasible-ray backup,
nonlinear gdot/merit requirement, all-node and original midpoint checks,
both complete RMS scans, core/material-angle guards and boundary checks
are retained. Full RMS is still skipped whenever the original engine
cannot evaluate the required finite midpoint RHS; the observer records
that scope instead of asserting an unperformed check.

The col-location observer calls each original evaluate and weights
method exactly once and reads only already returned arrays. It records
the complete physical argmax, component, station, signed residual and
the original fixed model row weight. It neither calls a new RHS/J/model
action nor changes any returned vector, finite flag, merit or gate.
Diagnostic exceptions remain observer reports only.

The new FD wrapper repeats the original complete Rphi directional and
Richardson checks on the actual newly saved warm with its exact SHA.
It retains the true zero-H T112 Jacobian as an explicitly affine map.
This is not a native nonlinear solve at the new warm's H. The original
5e-5 implementation threshold and all original directions and step
levels remain unchanged. No old FD pass is relabelled as a new one.

## 7. Executable one-model call and output contract

After the unchanged public78 source and actual M112 preparation are
restored, the warm call is:

~~~sh
python -u "$C/geometry_20261114_nineteen_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$ACTUAL_ZERO_T112_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT63/warm-001.json.gz" \
  --expected-resume-sha 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a \
  --parent-status "$VISIBLE_PARENT63/driver-status.json" \
  --expected-parent-status-sha 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46 \
  --out "$VISIBLE_OUT/nineteen-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
~~~

The actual warm filename is read from the original driver status and its
bytes checked against the status SHA before calling:

~~~sh
python -u "$C/geometry_20261114_nineteen_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$ACTUAL_ZERO_T112_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
~~~

The output directory contains the original driver status, saved warm,
model and trial records, complete typed-domain export, condensed result
and array manifest, optional stored local root, and both read-only
midpoint and collocation-location observations. All original failures
remain in the Actions artifact. A saved optimization warm continues to
carry success=false and new_coupled_finite_acceptance=false.

The same existing condensedqp push trigger and single lane are used.
There is no second dispatch in this source or workflow draft. The draft
adds four current source pins and compile entries, selects the actual63
parent paths and pair, invokes the independent19 wrapper, and verifies
the current19 output schema before the real fresh FD. The public78
restoration, original accepted/prepared/anchor/config files, dependencies,
thread settings, upload behavior and ordinary publisher remain unchanged.

The complete local source diff and static syntax checks were performed
before delivery: four Python ASTs, the eight full mathematical function
comparisons, twelve observer-function comparisons, all31 request source
pins, eleven Bash run blocks and six inline-Python ASTs. No scientific
module was imported and no scientific calculation was run locally.
