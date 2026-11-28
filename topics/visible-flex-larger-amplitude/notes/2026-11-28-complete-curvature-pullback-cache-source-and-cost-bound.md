# Complete same-point curvature-pullback reuse: source evidence and bounded implementation

Prepared 2026-11-28. This is a complete source delivery for a later explicitly bound scientific entry. It does not modify or resume any running job. No new physical field, root, derivative, trial, timing sample, AST, Python import, fixture or numerical benchmark was executed while preparing it. The only executed transformations were complete text reads, literal replacements, SHA calculations and whole inverse text comparisons.

## 1. Result and its exact scope

The original inequality selector computes the same complete curvature pullback again when one curvature point/branch/cotangent is paired with several different diameter partners. Its diameter pullbacks already have a local cache. The new complete selector adds a bounded cache for the *returned numerical curvature pullback*, within one call of the original row builder.

This acts during **build_rows / selected-row preparation**. It does not cache or skip a trial's complete nonlinear geometry scan. In particular it does not explain the previously observed tens of minutes between trial-statistics and trial-geometry events. No percentage speedup, six-hour completion guarantee, or measured cache-hit rate is claimed.

Two complete, separate source variants are delivered:

| Intended normal family | Complete selector | Bytes | SHA256 | Git blob |
|---|---|---:|---|---|
| Original full-wave, including the current restoration-policy family | fullclosed_point_inequalities_v2_complete_curvature_cache.py | 35982 | 73daaf2ada7c0da523a6a3064519a0d7002b613a99369a12626d5efc73afd7bb | 37225367dd7ceee178d500260d1893397394f17c |
| Paired half-wave current family | fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py | 35982 | f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112 | a8c04e0044ae95d1debd4d96dcd753430f0fd797 |

The half-wave variant differs from the complete full-wave selector in exactly two whole-source pins. It does not broaden an allowlist or accept an arbitrary endpoint class.

Full-wave pins:

- normal: 76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d;
- detached meridian helper: eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de.

Half-wave pins, taken from the complete 67,013-byte binding 6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638, blob 4f20af6e3663bdf69aca7193bc29624dc706411c:

- normal: c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac;
- detached meridian helper: f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e.

Using the full-wave variant with the half-wave producer would disable its optional cache and retain original pullbacks. That is not the proposed half-wave integration: the separately pinned half-wave file must be selected.

The three original input/field layers remain distinct: the fixed mathematical target, the chosen full-wave or half-wave seed, and the current complete outer variable point. No old target, seed, report, accepted point or typed history is reinterpreted by this optimization.

## 2. Source evidence for the repeated operation

The complete parent is:

- path: scripts/resume_20261120/fullclosed_point_inequalities_v2.py;
- topic prefix: topics/visible-flex-larger-amplitude;
- complete bytes: 12,166;
- SHA256: e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8;
- exact readable restoration commit: 3d1f7b396e735e07f1dceca825aa69f963c105dc.

In that parent, add_candidates constructs a separate row for each selected curvature-location/diameter-location pair. Curvature value and its six-slot cotangent are carried unchanged when only the diameter partner changes. The original selection keeps all protected rows, then separated primary rows, and only afterward eligible alternative diameter partners, subject to the unchanged 192-row cap.

The parent radius_covector function caches the full returned diameter pullback by radius index. In contrast, the original row loop executes point_module.pullback or pullback_at for dk on every row, before looking up dD. The loop then computes, in its original order,

    gradient = reach_ratio * (diameter * sign(kappa) * dk + abs(kappa) * dD)
    row = transpose(gradient)
    norm = norm(row)
    C_row = row / norm
    bound = (safety - current_product) / norm

The new source preserves all of these arithmetic expressions and their order, all row metadata, every bound, every transpose, every original matrix flush/discard operation, and the original dD cache.

The currently bound geometry source 5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135 maps both selector pullback paths to the complete q.point_vjp. Its native current normal implementation, 76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d, builds the complete physical six-jet function with an active point tensor, forms the full six-slot scalar pairing, differentiates it, and returns the entire native free-coordinate NumPy gradient.

The corresponding _implicit_jet_value retains all 32 stages and all upstream control/frame/zero-target dependencies. A repeated numerical point_vjp request can therefore reconstruct an expensive derivative graph even though its complete input and selected root state have not changed. This statement is about the code path. It is not a measurement of how many repeated rows an actual run selected.

## 3. Why the reuse preserves the row problem

Write X(x) for the six physical jets at the selected literal point and c for the actual six-slot curvature cotangent already obtained by the original selector. The requested native pullback is

    dκ(x;c) = D X(x)^T c.

For a selected diameter D_i, the original reach row uses

    d[reach_ratio D_i |κ|]
      = reach_ratio [D_i sign(κ) dκ + |κ| dD_i].

Changing only D_i and dD_i does not change dκ. Thus the same complete dκ may be used in several rows, while each row still uses its own diameter, diameter derivative, normalization and right-hand side.

The implementation does not identify nearby points, equal-looking radii, approximately equal cotangents, angular aliases, grid points with arbitrary points, or different eigenbranches. It requires an exact key containing the original tagged call, actual literal material address and all 18 binary64 cotangent words. Grid and arbitrary call tags remain different even if they happen to address the same physical coordinates.

The stored value is a complete gradient actually returned by an earlier original point_vjp in this same row-building invocation. A hit copies those exact stored words. It does not approximate or reconstruct a missing component and does not reuse a derivative graph. As with existing literal-value caches, this is not a claim that an unexecuted fresh AD recomputation has been measured to produce the same working words.

All scientific failures in the original pullback remain outside the optional-cache exception handlers. On a cache miss, unavailable key, unsupported family, tracking ambiguity, source mismatch, allocation failure or oversized value, the original complete call is made. A missing root or angular matrix is not computed by the cache to make a key.

## 4. Exact dependency and tracking boundary

The scope binds the same q object, its complete canonical model, its base model, its fixed seed model, all participating producer objects and their actual source methods/files. The actual model is checked by canonical JSON SHA against its identity, not just by object identity or a schema string.

The point binding retains the existing normal's immutable bytes owner. On a possible cache lookup it checks:

- q._current_x is the same complete selected object;
- the point SHA is unchanged;
- the direct bytes owner, native float64 layout and complete size satisfy the existing immutable-owner validator;
- the original row-builder x and prepared.x contain every identical uint64 word, including signed zeros.

The physical key also includes the actual complete integration carriers, fixed core, frozen Q carrier, frequencies, full layouts, exact normal partition, query arrays, selected root/control/frame/J3 words, every actual 9-by-9 angular matrix, fixed mean values, fixed radial values, reference calibration values, and fixed provider core/height.

The already consumed singleton integration-reference NPZ is bound by actual path, byte length and whole SHA. No new reference file or mean batch is generated for the cache. This avoids substituting only a model label for the actual working reference values.

The original numerical point_vjp needs reverse-gradient mode enabled internally. The new scope preserves this precondition. It does not incorrectly require the whole row builder to run under no_grad. It invokes the existing strict environment probe inside a temporary no_grad context solely to detect outer transforms, inference, forward AD, tracing, compilation, dispatch/function modes, autocast and unavailable probes; that context ends before any original scientific call. The original pullback runs in its original mode.

Caller inputs and cached outputs are plain finite native float64 NumPy arrays. A retained gradient must have exactly q.free_size coordinates, C-contiguous layout and stride 8. Stored numerical words are immutable bytes, and a hit returns a fresh full-size copy. No Torch tape, tensor requiring gradients, or mutable alias to a cached gradient is retained.

## 5. Confirmed full-wave / half-wave interface

Both complete families were retrieved and their whole hashes checked. The following eleven complete method texts were compared without AST execution and are identical between the two families:

- normal: _select_point, _get_roots, _implicit_jet_value, _point_query, point_vjp, _run_chain;
- detached meridian helper: _source_binding and _words;
- reference calibration: reference_data;
- seed reference: _means and _radial.

The actual normal constructor sets identity = canonical(model). The root cache uses canonical float.hex angle keys. _get_roots stores order 1 or 2; point_vjp requests curvature=True and its active implicit path requests angular order 2. The adjacent matrix producer installs all stage jacobian arrays together and assigns jacobian_order=2 only after complete production.

Therefore a first original point_vjp can populate the previously absent complete nine-by-nine matrices. The cache forms its stored key **after** that original return. A later matching request can then have the same complete post-return dependency key. The pre-return key being unavailable is an ordinary miss, not a failure or a request to precompute matrices.

reference_data uses tuple(phi.hex()) keys. The seed mean cache uses the individual hex key. The seed radial cache uses the same complete array SHA convention implemented locally by the selector: contiguous dtype, complete shape and all data bytes. These are actual matching interfaces, not conjectured field names. This source correspondence does not assert that a future selected-row list has duplicates or that the cache has achieved a hit.

## 6. Bounded resource and truthful accounting

The retained numerical gradient payload is limited to 64 MiB. For the current M160/J923 layout:

    n = 3M + 2 = 482
    free_size = (M - 3) + (3J - 3)n + 1 = 1,333,370
    one float64 gradient = 10,666,960 bytes

At most six such gradients fit in the retained payload limit. Original caller/output temporaries and small keys/records are outside this specifically declared numerical-payload bound. No raw numerical cache is written into Git.

The already selected row list is read only to count exact future repetitions of the small literal/cotangent key. A gradient with no later repetition is not stored. A first-and-only request bypasses the large dependency-key work and calls the original producer directly. This is not a new row-selection rule; every original candidate and row still executes in its original position.

Among eligible repeated requests, retained entries use LRU eviction. Capacity failure only changes whether a later request recomputes the original pullback. It never drops a row or changes an iteration budget. All entries are released in finally at the end of the original row loop.

The complete prefix metadata gains one record:

    complete_curvature_pullback_cache

It records every row's original-return or prior-return origin, actual dependency-key SHA and stored-gradient SHA where applicable; actual request, original-attempt/return and numerical-hit counts; retained payload accounting; exact source bindings; optional failures; and scope closure.

A hit is not counted as a new original point_vjp, a new root solve or a new execution of all 32 implicit stages. Existing q counters continue counting actual original work. The new logical request count permits row requests and actual numerical work to be distinguished.

The pure function validate_complete_curvature_pullback_cache(value, *, selected_rows, current_full_point_sha256, model_identity_sha256) checks this source and its own row/point/model attribution. It requires successful record accounting and verifies that each claimed hit points backward to a matching prior original return. It performs no F/J/root operation. It can be consumed with the complete source already present; it is not a standalone admission workflow.

## 7. Cost statement and limits

Let R be the actual number of curvature pullback requests from the unchanged selected row list, and let U be the number of distinct full requests whose required dependencies remain unchanged. If every repeated value remains in the cache, the original point_vjp count can drop from R to U. With the actual 64-MiB policy, the exact count is R minus the actual number H of validated numerical hits, where

    0 <= H <= R - U.

No value of R, U or H from an unfinished run is invented here. If all selected curvature requests are distinct, H=0. The new guard/hash/copy cost is real, and no speedup is guaranteed. In that case the first-and-only fast path avoids hashing large numerical states for those requests.

One valid hit avoids the original complete point_vjp computation for that exact request, including its original field graph and reverse pullback. It does not avoid the row's vector combination, full coordinate transpose, norm, normalization, output write, or matrix flush.

This optimization belongs to the time interval between a current-geometry return and the completed row/QP preparation. It does not apply to a trial's q.residual or complete screen.scan. The known long trial intervals must be investigated separately; neither the 64-step QP budget nor damping is inferred to be their bottleneck.

## 8. Minimum complete source integration

Only the complete selector contains a changed numerical execution policy. The normal, base, seed, analytic frame, closure cache, stage matrices, root-packet implementation and accurate mathematical field definitions remain their actual existing whole sources.

A runnable entry must nevertheless propagate the real new identity through the strict source boundary:

1. Select exactly one of the two complete selector files for its actual normal family.
2. In a new complete geometry source, change the selector file path and SELECTOR_SHA256. Its row selection, field scans and geometry formulas remain the complete original text.
3. Bind that actual geometry source in the complete scientific driver's source registry.
4. Bind the new complete geometry in the pure batched-geometry source reader, and propagate the real driver/launcher/reader pins.
5. Preserve all parent source pairs explicitly as history or aliases as required by the actual registry; do not claim an unchanged original registry after replacing current roles.
6. Give any accurate downstream input reader the actual new entry source identity if it hard-pins the old driver. The unchanged physical normal/seed sources alone do not make a different driver pass an old hardcoded guard.

No CLI numerical parameter, row cap, source parent, typed record, physical target, 32-stage budget, Newton budget, geometry domain, line-search order or acceptance inequality is removed. No queued/running entry was edited. No complete runnable family or future run number is asserted by this source-only package.

## 9. Complete reproduction and restoration

The complete reproducer is:

- topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_complete_curvature_pullback_cache_selector.mjs
- 31587 bytes;
- SHA256 8fae1016ae056ea68f6620b2ab51bcfef339face0793986db5409a69f3d18c4d;
- Git blob 11a6e7e4e51cb98f33a4b480bf3037c3c8098944.

Its exact interface is:

    node reproduce_complete_curvature_pullback_cache_selector.mjs \
      --source-root REPOSITORY \
      --output-directory OUTPUT_DIRECTORY

It reads the whole exact parent above, applies all three explicit literal changes, and writes both complete variants. It checks the forward whole-byte SHA and reverses every change to recover the complete original source. The half-wave variant is additionally reversed through its two exact source-pin substitutions to the full-wave variant.

The three source changes are: insert the complete optional cache implementation; wrap only the original dk call site with lookup/actual-return storage and finally cleanup; append the actual cache metadata. Original numerical row expressions remain text-identical after removing the added indentation. No complete source body is replaced by an excerpt.

The earlier 35,522-byte draft blob 1cef9253f591fa450c9c163230adafc7d56288ef and 35,597-byte intermediate blob 44190d53aa8ddd2452fe8ba612c91fac66ca1adc were never admitted or executed. The final full-wave source additionally requires contiguous returned gradients and bypasses large key work for first-and-only requests. The final identities in section 1 are authoritative for this delivery.

## 10. Separate source-level opportunities, not implemented in this selector

Two other concrete repetitions were found. They address field/root evaluation rather than this row cache and require independent complete source integration.

### 10.1 Second-order frame upgrades

The normal's _run_chain(existing=...) already preserves old eta value/first jets, J3, and old controls/frame lower jets. It does not re-run Newton. It does, however, ask the analytic frame for all three angular components and then overwrite its first two components with the actual retained lower frame.

The current analytic frame producer d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd computes six control columns and three original total reductions per column for order 2. On an upgrade, twelve of these eighteen totals are discarded by the original caller's explicit lower-jet overwrite.

A precise follow-up interface can retain the current C1 value cache and produce only the new second component on each true miss, then combine it with each actual stage's old two components. It must retain every intermediate needed by the second-component formula, all six columns, the original coefficient rounding conventions, full data/control provenance, all 32 stages, and all original forced stage/final residual re-reads. Active parameter differentiation must continue through the original full path.

The existing C1 scope already caches repeated complete previous-control words. Therefore no multiplication by 32 is justified as an actual saving. The bound is twelve avoided total reductions per *actual uncached upgraded frame calculation*, not twelve times every stage regardless of cache hits. No implementation of this proposal is silently included here.

### 10.2 Coefficients evaluated but not consumed

The complete base source 552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3 unconditionally produces six rotation coefficient functions. Its Horner loops have 13, 12 and 11 updates for each of two coefficient families: 72 updates in total. The normal _corrected_jets order-0 path uses only A/B; order 1 uses only A/B/Az/Bz unless another requested derivative needs more.

An explicit maximum-needed-derivative interface could evaluate the exact same required scalar expressions and Horner sequences while omitting only unused coefficient functions. It would use 26 polynomial updates for order 0 and 50 for order 1 rather than 72. Required output tensors, scalar expressions, reduction shapes and order would remain unchanged. The analytic derivatives of independently rounded coefficient polynomials must remain the derivatives of those actual polynomials; an independently rounded Az must not be substituted for the derivative of A.

This is an arithmetic-count observation, not a measured time share. It has not been implemented, benchmarked, or combined with the current selector.

## 11. What existing caches already remove

The following existing mechanisms were actually read and must not be counted again as new savings:

- Geometry _set_x retains _grid, _extra_grid and _field_cache at the same current point; _ensure_grid does not recompute an already retained complete grid.
- The normal's root cache retains each literal angle's complete selected stages and only upgrades a lower angular order when needed.
- An existing first-order branch upgrade reuses the original value/first root jets and J3.
- C1 detached scopes already reuse identical complete previous-control words within the same data scope.
- The fixed seed's _means caches literal-angle roots, and its _radial caches exact radial-query batches.
- The original selector already caches returned diameter covectors.

The parent-provided published event boundaries for run22 show distinct statistics, geometry, row/QP and trial phases. They are not a profiler attribution and were not converted here into estimates of any kernel's percentage cost.

## 12. Execution status

Complete source text, source identities, inverse literal reproduction and the specified full-wave/half-wave interfaces have been read and bound. No actual cache hit, performance gain, full final report, accepted step, typed-history transfer, root enclosure or continuous certificate has been produced by this package. Future run/report/field/point/output identities remain unknown. All raw numerical values stay in runner memory or the existing runner scratch files.
