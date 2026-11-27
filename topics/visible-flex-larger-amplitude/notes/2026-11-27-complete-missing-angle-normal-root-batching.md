# Complete missing-angle batching for the fixed Fejér geometry

## 1. Scope and exact complete sources

This independent geometry source changes the organization of already required normal-root work in the complete existing geometry scan. It is derived from the whole `so3_fixed_fejer_stage_point_geometry.py` (70709 bytes, SHA-256 `2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471`, Git blob `2677d379e87b359088177b244428894311348996`). The new complete source is `so3_fixed_fejer_batched_missing_angle_geometry.py` (88163 bytes, SHA-256 `51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898`, Git blob `e66b17a5384ec29e11415d4eb6a6549594277436`).

The original running source and all original running requests remain historical, immutable inputs. This source does not update a running job. Its caller must bind the complete actual new normal family and retain the full existing solver arguments and budgets. The root-owned new driver, launcher, pure reader and observer are separate complete components; this module supplies neither a reduced solver nor a stand-alone numerical test.

The exact complete runtime dependencies changed by this geometry are:

- `endpoint`: `fixed_fejer_detached_meridian_normal_lift.py`; 96276 bytes; SHA-256 `388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4`; Git blob `8a22b31dcc36d3160d4c968f9645600961a22abc`.
- `analytic_J3`: `fixed_fejer_meridian_analytic_stage_jacobian.py`; 25697 bytes; SHA-256 `223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811`; Git blob `7525e1f076c90b877d7574c8aea85dc12e02d973`.
- `stage_matrices`: `fixed_fejer_meridian_stage_matrices.py`; 61280 bytes; SHA-256 `f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791`; Git blob `57e215d6bd28e7df8d7172106df5caa209ebc78c`.
- `adjacent_matrices`: `fixed_fejer_meridian_adjacent_matrices.py`; 36766 bytes; SHA-256 `bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564`; Git blob `641da23cdb76029f343ab441d03625e190cc4ae1`.
- `reference_calibration`: `fixed_fejer_meridian_reference_calibration.py`; 11872 bytes; SHA-256 `aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3`; Git blob `2f816e1e3e617a1c8bf85bea8067f5aedd8e773e`.
- `closure_values`: `fixed_fejer_meridian_closure_values.py`; 59440 bytes; SHA-256 `2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0`; Git blob `2383f9c4bad43635e43fe409b048d3f74d2b9b8c`.
- `frame_C1`: `fixed_fejer_meridian_normal_frame_c1.py`; 37361 bytes; SHA-256 `c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246`; Git blob `5daa46fca67d3e90985fed092c37ec4eefd20421`.
- `meridian_values`: `fixed_fejer_detached_meridian_values.py`; 41030 bytes; SHA-256 `7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd`; Git blob `6ab29473b0d549539de69a064efb19af4227a867`.

The complete original memory, rows, fixed reference, Fejér chart, scalar profile, literal Q, core/rotation/height layout, curvature helpers and point selector remain in the parent body with their existing strict guards. The batching policy separately records the immediate complete geometry parent. The earlier physical-geometry derivation field remains historical provenance.

## 2. The actual repeated operation and chosen interface

In the whole parent, `GeometryScreen.scan` first completes its existing current grid and any historical extra grid. It then updates its permanent curvature and radius memories from the real grid extrema and pools. The dictionary union of those two actual memories is the explicit point loop. At a location absent from the current-point sixjet cache, the original `_point` calls the complete normal operator's `point_fields`. A genuinely new angle in that call otherwise starts a complete normal chain at a singleton angle.

The new implementation acts only after the original two memories and their union have been constructed. It supplies the original query-independent integration data through the complete independently bound interface:

```python
data = q.detached_meridian_values.integration_data(x, phi, curvature=True)
items = q._get_roots(data, phi, 2, need_linearization=False)
```

No dummy physical query is evaluated. The integration-data helper is a separate complete source owned by the lower-family implementation. That helper binds the actual immutable point, complete ordered angles and requested order and retains its strict plain-detached conditions. The actual new normal source is also bound as a whole file. The geometry calls its original point selection and original root cache entry; it does not replace the root solver.

## 3. Exact selection and original point order

The preparation enumerates the actual dictionary union in its original insertion order. It uses the original `_location` and `_key` representations, retaining the existing cell, literal radial word and literal angle semantics. It neither sorts the angles numerically nor changes signed-zero or historical address deduplication in the original memories.

For each original location, the preparation first checks whether its complete sixjets are already in the current-point field cache. Such a location needs no new root preparation. For a remaining location, an already cached root angle is left alone. In particular, an existing first-order root is not proactively upgraded: its original point call remains responsible for the original same-branch second-order upgrade. Only the first appearance of a truly absent literal root angle enters the new plan.

The plan stores every selected literal binary64 angle and its first original union position. It is partitioned by the unchanged actual `q.angle_block`. Each batch runs in that order. All angles use the same full actual outer point and the same original normal partition.

After preparation, the entire original explicit point loop still executes. Every original location is checked again by the original envelope membership check, every uncached field is read by the original point method, both principal curvature branches and all original amplitude quantities are read, all working pools and maxima are accumulated in their original order, and every point record is appended as before. The new code does not select a smaller geometry subset. It does not replace any explicit point by an angle-only result. The current and extra grid scans are unchanged.

## 4. Mathematical separation and working arithmetic

For a fixed full outer point and literal angle, the original normal problem has the same fixed scalar/reference data, the same six control coordinates, the same exact auxiliary normal partition of 32 stages (33 nodes in the declared request), the same stage equations and the same angular derivatives. Combining several angles along the existing angle dimension does not introduce a new physical equation.

In particular, the original complete `_total` reshapes by radial cell, quadrature node, angle and vector component. Its weighted sum is over quadrature nodes and its cumulative sum is over radial cells. It does not sum over the angle dimension. The original stage roots, normal planes, domains, Newton iteration limits, line searches, value and angular equations, implicit matrices and endpoint checks remain the complete normal implementation.

This mathematical separation is not a statement of identical binary64 results. A multi-angle tensor operation may use different arithmetic kernels or reduction scheduling from a singleton tensor operation. Batch-wide numerical failures can also return a different partial prefix: preparation occurs before the explicit point loop, whereas the parent interleaved root creation and physical point reads. A failure in an original batch operation is not silently converted to a success or replaced by a different numerical method. No singleton working-word equality, equal accepted steps, speedup or continuous root certificate is claimed.

All 32 stage-final original closure rereads and the original final physical endpoint reread remain in `_run_chain`. The new geometry does not alter `_get_roots`, `_run_chain`, `_implicit`, the sixjet formulas or the exact active upstream graph. The existing active J and transpose paths remain original. Every original outer variable, every permanent role, both witness signs, all geometric inequalities and every solver budget remain the caller's full original problem.

## 5. Complete and partial runtime records

Every scan starts a new `missing_angle_root_batches` record owned by that scan's actual complete point. The source-binding policy includes this module's whole SHA, the actual complete normal source SHA and the immediate complete geometry parent SHA.

The record includes the actual original union count and ordered-address canonical hash; original angle block and normal-stage count; locations already satisfied by the current-point field cache; actual existing cached angles and first-order angles left to the original upgrade; the whole ordered missing-angle plan; and every attempted batch.

Each attempted batch records its requested order, ordered literal angles, first union positions, actual point, complete before/after/delta dictionaries for the original normal and endpoint counters, and its real returned status. A returned batch preserves every actual root's original return record, including the exact normal partition, full stage count, endpoint residuals and the original final-equation flag. No raw root array is put into this compact provenance.

The original point loop maintains a separate count, incremented only after the original full geometric read and point record have completed. Root preparation completion is distinct from point-loop completion and from the original geometry's `complete` and `passed` fields. Empty missing-angle plans are honestly complete preparations without invented root computations.

The original scan exception policy remains unchanged. If an exception belongs to the original caught classes, the returned failed scan includes the honest preparation record and the original envelope's partial scope. An exception that the original scan did not catch still propagates; this module does not swallow interrupts, memory failures or original root exceptions to manufacture a geometry result. A failed batch is marked before propagation, with the actual counter deltas captured in `finally`.

## 6. Pure reader API and publication boundary

The complete geometry provides:

```python
validate_missing_angle_batches(
    record,
    model_identity=actual_model_identity,
    point_sha256=scan_point_sha256,
    geometry_complete=scan_complete,
)
```

This pure function validates exact source/policy/model/point identity, original order, complete planned batch slicing, actual counter deltas, returned root records and original point-loop coverage. It neither constructs a problem nor calls F, J, a root, a field or a quadrature. A partial result stays partial.

A caller that extracts only the pure functions must provide the exact source namespace: `__file__` for this whole geometry; `sha`, `canonical`, `math`; and `MISSING_ANGLE_BATCH_SCHEMA`, `MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256`, `ENDPOINT_SOURCE_SHA256`. It extracts `missing_angle_batch_policy` and `validate_missing_angle_batches` in that same namespace. Its outer reader must first verify the whole geometry source and bind the actual scan's model and point, as it does for the existing full geometry. No Torch or NumPy import is required by these two pure functions.

The full scientific report and all scientific arrays remain on the runner. A compact public summary may retain the validated policy identity, actual point identity, planned angle and returned batch counts, original point-read count and honest status. It must not publish the internal matrices or treat batch completion as a continuous geometry certificate. New root cache-hit counters include real reuse after preparation; they are not substituted for the number of physical points read.

## 7. Complete reversible source reproduction

`reproduce_fixed_fejer_missing_angle_geometry.mjs` contains every exact forward replacement, the complete parent identity and the expected complete result identity. It reconstructs the whole source text, reverses every replacement, and requires the entire original parent text and SHA to be restored. It never imports or evaluates a scientific Python module.

Its complete source-only command is:

```text
node scripts/resume_20261126/reproduce_fixed_fejer_missing_angle_geometry.mjs --source-directory scripts/resume_20261126 --generated-directory <scratch-generated-directory>
```

`--verify-existing` optionally compares an already generated full source. This reproducibility utility is not a new solver admission condition and is not inserted before the scientific workload.

The performed checks in preparing this delivery are complete cloud text replacement counts, whole UTF-8 bytes/SHA calculations and whole inverse text identity. No local Python AST or compilation, NumPy/Torch execution, numerical fixture, field evaluation or speed measurement is asserted. The new complete scientific entry must supply its own actual Actions results before a performance or numerical conclusion can be made.

## 8. Final dependency metadata correction

The prior prepared geometry candidate had SHA-256 `e61f35f97082de42020d967dc464c8bebafe9960e513f59be9f55a94069b91e7` and Git blob `0b80d60ed18f3234d8eadec634e8913f6cfed528`. Its complete source, reproducer, note and delivery manifest remain preserved under their original blob identities. The final geometry changes only its two dependency pins, from the prior normal/helper pair to the final complete normal `388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4` and helper `7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd`. The batching methods, pure batching validator, point loop and all numerical geometry text are unchanged. This exact two-pin replacement was compared against the entire new geometry text.

The lower helper's correction prevents an uninitialized `None` point from being labelled as a match to another uninitialized `None` point. Its whole source identity therefore changes; the complete normal and packet source pins change accordingly. This is a correction to actual metadata identity, not a new scientific computation or a change to the geometry's batching algorithm. This delivery makes no actual execution or performance claim for either prepared candidate.
