# Actual public09 J923 to J1845: complete exact-affine radial refinement

## 1. Scope and status

This package enlarges the current SO3 shared-quintic radial space from 923 to 1845 nodes. It retains the entire actually frozen run09 target, the original 160-word material chart, M160, N2048 with its original 513 literal quarter angles, the original supported reference, and the common 32-stage normal selection. It is a radial-space and radial-observation refinement. It is not the separately published M320 or N4096 refinement.

All twenty-one runtime files are complete independent sources. The old source families remain unchanged. All new files have complete SHA256 and remote Git-blob identities in the [complete delivery manifest](../computations/public09-radial-J1845-complete-source-delivery.json). Three complete parameter plans are supplied. They are not queued or executed by this construction.

No field, Jacobian, root, quadrature, numerical example or scientific fixture was evaluated locally. After the execution environment became unavailable, source construction and complete text replay were performed in V8. No Python AST/compile, Node command-line execution, or numerical success is claimed for these new files. This source-only status does not describe the scientific status of another currently running job.

The exact-space inclusion uses the existing [R676 refinement contract](../results/R676-fixed-metric-refinement-and-complete-observation-transfer.md), together with the original fixed-target conventions. This implementation does not claim a new existence theorem, a global implicit branch, or a continuous geometry certificate.

## 2. Fixed and current objects are separate

The following dimensions have distinct owners.

| Object | Frozen reference / original parent | Current refined field |
|---|---:|---:|
| Shared radial nodes | 923 | 1845 |
| Radial cells | 922 | 1844 |
| Fourier M | 160 | 160 |
| SO3 channels | 161 odd sine, 161 odd cosine, 160 even sine | the same three complete blocks |
| Full angular count | 2048 | 2048 |
| Literal quarter angles | 513 | the same 513 words |
| Legacy node/midpoint rows | 1845 | 3689 |
| Native node/midpoint plus six-Gauss rows | 7377 | 14753 |
| Outer normal/integration Gauss order | 8 | 8 |
| Common exact normal stages | 32 | 32 |
| Free core coefficients | 157 | 157 |
| Complete free vector size | 1333370 | 2666582 |

The current observation plan additionally retains every original observation representation not already present in the new native plan. Its actual total row count is recorded. No presumed total replaces that recorded count.

The fixed target is the complete public09 input whose target identity is
`7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a`.
Its actual binding file has whole SHA256
`2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d`.
The complete reference model remains
`d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75`;
the complete reference bundle remains
`2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2`.

The full model, all 160 chart words, the exact scalar definition, all original symbolic nodes, and the actual whole input files remain subject to the original public-input validators. The historical claim fields are retained exactly: equality of particular old chart words does not manufacture a cross-run claim of mathematical-target equivalence or a transferred field certificate.

The original `4e655` reference context, original supported-reference provider `0d09`, and original mean kernel `f848` retain their own layouts and identities. The current fine base is an independent source. Its model records both radial grids, all new source definitions and the actual observation identity. It does not modify the original reference object to make its J appear to be 1845.

## 3. Exact affine points and ordinary binary carriers

Let the original symbolic node be the exact affine expression

$$
X_i=A_i S+B_i,
$$

where both coefficients are rational and S is the same fixed scalar length. The new symbolic nodes are

$$
Y_{2i}=X_i,\qquad
Y_{2i+1}=\frac{X_i+X_{i+1}}2.
$$

A query supplied as a fine cell j and a literal binary64 local coordinate u means the exact rational-affine point

$$
s=(1-u)Y_j+uY_{j+1}.
$$

The float word u is converted to its exact rational value before this identity is formed. The adapter maps this exact point to the appropriate original symbolic cell. It does not round an old local coordinate and then ask the old provider to evaluate that different point.

`radial_bisection_layout.py` retains the original binary mesh words at every even current node. A new midpoint receives its separately computed working carrier and error record. The complete symbolic node report and width records distinguish these carriers from the exact affine nodes. If adjacent working carriers are not strictly increasing, or a width cannot be represented with the required positive working value, construction fails. It does not merge cells, perturb a node, or add a hidden positive width.

`exact_affine_supported_reference.py` evaluates the original complete reference at these exact points. Its original-query shortcut requires the exact affine equality and the exact local word. A merely close local coordinate cannot select that shortcut. Queries outside that shortcut use the original fixed scalar law, complete support partition and original mean data explicitly.

Different working representations of a common mathematical endpoint can follow different floating-point paths. The observation/address layers therefore preserve all required original representations. An accurate equality of positions is not used to discard an old working read or to claim that two old/new field values are bitwise identical.

## 4. Complete shared-quintic injection

On each original radial cell, write an SO3 channel as its complete degree-five Hermite polynomial P. In accurate arithmetic its restriction to the two halves is specified by the original endpoint value, first derivative and second derivative, together with the middle values

$$
P(1/2),\qquad h^{-1}P_t(1/2),\qquad h^{-2}P_{tt}(1/2),
$$

where h is the original physical cell width and t is the original normalized local coordinate. The complete three-vector statement is applied to every coefficient of all three SO3 blocks. It is not an R/T/Z reinterpretation of the SO3 coefficient array.

The layout helper places every original value/first/second jet at the corresponding even current node. It computes all three middle jets from the complete original cell polynomial. Shared midpoint jets are inserted once and consumed by the two adjacent fine cells. The free core words and H word are copied exactly. The fixed original endpoint slots remain fixed, while every permitted new midpoint slot is free.

The block ordering remains:

- x: 161 odd-sine modes;
- y: 161 odd-cosine modes;
- z: 160 even-sine modes.

A globally zero original channel is handled explicitly and remains zero at the new nodes. The injection record includes the complete old/new point identities, old/new radial-jet identities, width identities, all three block ranges, and the actual count of zero channels. It is not validated from a shape alone.

The working injection uses the actual original binary width carriers and ordinary floating-point Hermite evaluation. These operations do not furnish an enclosure of the true middle coefficients. The record explicitly sets `coefficient_true_width_and_rounding_error_enclosed=False` and `accurate_midpoint_coefficients_equal_saved_binary64_claimed=False`.

Accurate polynomial inclusion also does not identify independently selected implicit normal branches. An accurately included outer rotation reproduces the same selected complete field only where the same implicit branch is retained. Every new initial field, normal chain, physical sixjet, objective and geometry screen must be read under the new current source and model.

The new full coordinate norm is built on all 1845 nodes and all permitted free slots. The old norm identity, old linear rows and old coordinate vectors are not reused as if they belonged to this new norm.

## 5. The current scalar table is reconstructed from its actual definition

The new scalar observations are not inferred by interpolation of the old `a_observations` words.

`complete_dyadic_radial_observations.py` reconstructs the same actual `e091` scalar integral table used by the complete current preparation. It binds the full scalar definition and input identity, requested tolerance, accuracy state, complete priority-queue rule, interval endpoints, evaluation counts and actual leaf count. The deterministic table construction retains the original exact priority and insertion-sequence ordering.

The actual current preparation's leaf count is a stopping identity for this reconstruction, not a substitute for the full scalar model. The implementation requires the full table metadata to equal the actual preparation metadata except for elapsed time. In particular:

- the actual requested-integral-accuracy boolean is preserved;
- the actual number of leaf evaluations is preserved;
- the radius, height and tail enclosures remain those of that same reconstructed definition;
- the actual admissibility and termination fields are checked;
- the old historical 2397-leaf table is not used as the current table.

The observed public09 preparation had a different current table history from the old carrier restoration. The code reads and validates the complete actual metadata; it does not turn the number 1995 into a replacement target definition, and it does not assert that a false requested-accuracy flag became true.

For every native fine query and every retained original query the a value and its complete available scalar enclosure are produced from that reconstructed table. All original 7377 target words must be reproduced exactly before the new input is accepted. A mismatch is an honest input-construction failure. It does not trigger a tolerance relaxation, replacement by an old table, or a change of g.

The original five complete input files are captured and rehashed during construction and before reporting. The report preserves the actual scalar table metadata and all a boxes. Their availability pays the stated scalar-input responsibilities only. It does not enclose trigonometric, normalization, rotation, normal-root, field-integration or full metric/geometry errors.

## 6. Complete fixed-reference four-jet queries

The exact-affine adapter returns the four reference quantities required by the current base:

$$
T_0,\qquad T_{0,\phi},\qquad T_{0,\phi\phi},\qquad T_{0,s}.
$$

All original complement pieces, normalized boundary layers and smooth-triangle central pieces remain present. The complete central mean and profile derivatives are those of the fixed original supported reference. The provider is not rebuilt from the current outer omega, core or H.

The original reference mean plan remains fixed. Querying a finer radial point does not silently replace that plan or the original seed model. Its existing mean cache retains its exact literal-angle ownership. The new adapter's source/model and exact point records separate that fixed reference cache from any current normal/root cache.

The working four jets still have ordinary numerical errors. The adapter records that scalar normalization, trigonometric evaluation and query errors are not certified. The exact-affine input mapping is exact; this is not a claim that every subsequent floating-point function evaluation is exact.

## 7. Positive current observations and a separate complete old measure

The new native six-Gauss observer includes every fine node and midpoint. Missing original query representations are appended to the complete plan. The target a values at all old rows are checked as described above.

Let S_f denote the fine legacy node/midpoint rule, Q_f the fine six-Gauss rule, and Q_o the entire original six-Gauss rule mapped into the same full current row array. The current positive rule is

$$
Q=\frac{Q_f+Q_o}{2},\qquad
W=fS_f+(1-f)Q,
$$

with the original explicit `legacy_fraction` f. The implementation records the actual positive weight words, complete old-to-current stage map and actual normalizer. The rule change is part of the new finite observation definition.

The current objective is evaluated on W. In addition, the complete original 7377-row functional is separately evaluated on the *same current physical field*, with the original complete positive row measure. The source computes the common-parent rows from the already complete native residual array. It does not read a saved parent Phi or concatenate old and new residual fields.

Each complete statistic records:

- the current complete point and current model identity;
- the complete original 7377 row count and N2048;
- the old positive measure and full stage-map identities;
- all three physical Gram components and the original spectral/mean/cross terms;
- its own common-parent spectral value and maximum relative Gram error.

A current Phi under W is not directly subtracted from an old Phi under a different measure as though they were one functional. The common-parent read gives an explicit same-measure comparison when a complete actual parent field later exists. No such comparison value is fabricated in these plans.

The full current scientific suffix differs from its parent only by the two complete common-parent statistic insertions. Its original 19574 bytes have SHA256 `d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`; the new 20488-byte suffix has SHA256 `41075095653c8d7f5bceed1f3d85e8708f67b0a3180ee73369b5d4b08dea9bcf`. Removing only the two declared insertions restores the entire original suffix byte for byte. The package does not call the changed suffix unchanged.

## 8. Full material-address and typed-history responsibility

The new memory source retains the original actual public09 target binding, the complete old dc5 carrier, and the complete current original-reference carrier. It also reads all five new fine input files.

The permanent nonlinear responsibility includes

$$
E=P_0\;\cup\;\iota(G_{\rm old})\;\cup\;
\iota(G_{\rm original\ reference})\;\cup\;G_{\rm fine}.
$$

Every grid includes its full literal angular set. Both principal-curvature branches, both witness signs, radius, cap and height responsibility remain. The original known protected prefix and original 192-row selection are retained. Current near-active additional rows retain their explicit cap, while actual discovered typed separation memory has no eviction or count cap.

Original stage/angle indices are first decoded with the complete original J923/P7377/N2048 carrier. Only then are the resulting literal points mapped into the current J1845 coordinates. Fine own-restart indices use their own complete fine carrier. The two meanings are never selected from a convenient shape or from the current q.J alone.

`radial_material_address_transfer.py` validates the complete mapping through the actual array words and exact symbolic pairs. Its pure reader consumes the full NPY payloads with original dtype and shape checks. All original input members are rehashed. It does not import NumPy or compute a scientific field.

Typed transfers preserve family, branch, sign, partner, old ordinal and actual first-discovery provenance. Both the original typed representation and its current mapped representation are saved. Old physical row values are not assigned to the new field. Every current row uses the current complete parameter pullback.

Unreturned peer reports remain explicit provenance obligations. Full E coverage does not reconstruct an unknown old discovery order, protected promotion, point digest or typed record. An independent branch does not call those records empty. If they later become available, their real complete reports must be bound and their actual typed lineage merged.

The run07 cancellation statement refers to the actual API observation at 05:02:15 UTC, with API `updated_at` 05:00:28. It is not a known scientific child end time or cause. The plans retain null child-termination fields and the unknown typed obligation.

## 9. The complete selected normal and physical machinery remains

The current normal source changes explicit source/model bindings. Its complete `ZeroClosureOperator` class body is byte-identical to the original actual09 `3d8d` class. Every stage equation, numerical root solve, angular-jet completion, root cache, final closure check, active implicit chain, physical sixjet and J/J* method is retained.

The independently pinned analytic J3, analytic six-column frame, C1 reuse, detached stage-matrix reuse and adjacent-frame producer keep their full mathematical bodies. They receive the new full current base model and corresponding source pins. No old point cache is imported across the source/model change.

The geometry adapter changes its constructor guards and current radial input contract. Its complete suffix from `_set_x` through the end of the class is byte-identical to the published parent geometry. The full physical scan, point pullbacks, original row prefix, amplitude checks and permanent-memory operations remain.

The original `7299` envelope-row selector uses q.J and q.N dynamically and remains the complete original source. It receives the actual current dimension and complete fine geometry. It is not relabelled as a new formula.

Both immutable root-packet hooks remain: only already computed cache contents are captured, without a root/F/J upgrade. No old packet is declared current by changing its source label.

Changing the current radial integration and reference calibration changes the working field definition. The new model says so. The package does not claim bitwise equality to the old physical field, a measured speedup, or a transferred root/geometry certificate.

## 10. Strict original-parent and own-restart transfers

The accepted original-parent source family is the repaired complete public09 driver `ff544` and pure reader `aee22`. The older failed `e3cb` attempt, which produced no scientific report, is not treated as a complete parent.

A terminal-history mode must read a real complete original-parent report with the full same-target input, geometry, policy, variable-layout and source bindings. All original role arrays and typed records are then mapped and preserved. It starts the new field from its original-reference fine inclusion.

A complete-final mode additionally reads the entire actual original-parent checkpoint through the original full pure reader and all thirteen checkpoint members. It reconstructs the complete old free vector, verifies its actual point identities, and injects every core/H/three-block radial jet into the fine layout. It does not use a summary-only or partial cache as the old field.

The complete fixed reference remains the original reference initial point. An accepted parent final, if one later exists, is only the chosen current free-point seed. It cannot replace the frozen reference seed or target.

An own-restart mode remains strict for the same full new source, model, current observation input, norm and field. It must restore its complete actual fine typed memory. The original-parent transfer path and own-restart path are distinct.

The model comparison admits only the declared radial layout, source, observation, norm/calibration and current-coordinate differences. The rest of the complete fixed target, chart, reference model, scalar definition, support, 18 Q words, gamma and exact 32-stage partition must agree. It is not a permissive comparison of selected hashes.

## 11. Complete pure attribution

The new reader retains the complete parent reader functions and adds the radial binding. It reads the new whole driver source registry and all 78 roles.

The source-binding helper validates:

1. the complete actual public09 target and same current original input files;
2. the complete new base/layout/affine/observation definitions and identities;
3. all five actual fine input files and the original-to-current address map;
4. the actual current scalar reconstruction and its unchanged requested-accuracy boolean;
5. the whole original-parent or own-restart transfer, including full typed provenance;
6. the actual initial point and every explicit injection mode;
7. the current norm identity;
8. every recorded current/common-parent statistic at its own point and with its own complete measure;
9. normal, matrix, frame, packet and physical-field metadata without backfilling missing values.

The actual latest metadata and older own-point cache metadata remain separate. Partial root or field reads do not become complete because a pure schema validates. Setup failures before a q/report exists can still leave only the complete command record; the pure report reader cannot manufacture an absent report.

The reader imports only source-bound pure code for these checks. It does not import the scientific base, solve a root, recompute an integral, or upgrade a packet.

## 12. Three full parameter plans

The plans keep the original complete numeric argv, including one metric direction with 16 iterations, four restoration directions with 64 iterations each, the original damping/norm/geometry thresholds, all 32 normal stages, seed radial order eight and outer integration order eight. The new explicit option is `--current-radial-factor 2`.

The plans are:

| Mode | Actual original terminal needed | Actual complete original final needed | Starting current point |
|---|---|---|---|
| `independent` | no | no | complete fine inclusion of the original fixed-reference point |
| `terminal` | yes | no | the same reference inclusion, with actual terminal history |
| `final` | yes | yes | complete actual old final, injected through the new shared-quintic layout |

No future parent report/final SHA or accepted-field value is filled in. The terminal and final file paths are explicit expected inputs, not claims that those files exist.

Each plan contains the full scientific and pure argument arrays and the full original 333/317 selectors. It adds 24 scientific and 16 pure scalar selectors. It retains only the original `rows-*` cleanup and explicitly retains the new complete fine input directory and fixed-reference cache.

The plans are compact JSON so that each complete file remains below 100 KB. Their two-step compact queue remains below 95 KB. This formatting does not omit argv, selectors, output paths, cleanup rules, numeric parameters or actual input requirements.

Repeated historical producer-output and parent-repair metadata are bound to the already published complete 93108-byte parent ready file by its whole SHA256 and exact field names. The full 78-role runtime closure remains in each plan; the three current entry source hashes are separately listed. The complete source table and all constructor hashes are also in the delivery manifest. This avoids duplicating already immutable evidence while keeping all execution inputs explicit.

## 13. Reproduction and preservation

The four original complete primitives are the exact radial layout, exact-affine reference adapter, complete scalar-observation input and material-address transfer.

Three source-construction modules contain every complete old/new text patch for all seventeen remaining runtime files. Each parent source is whole-byte pinned; each patch verifies the complete old span; every resulting whole source must match its full expected byte count and SHA256.

`reproduce_radial_public_reference_sources.mjs` verifies all four original primitives, replays all seventeen transformations, verifies the complete 78-role registry, and checks the full unchanged normal class and geometry suffix. It also removes only the two declared common-parent statistic insertions and verifies the entire original scientific suffix. It neither imports nor evaluates a scientific module.

`make_radial_public_reference_ready.mjs` reads the entire pinned actual-parent ready, all runtime sources and all complete constructors. It reproduces all three full plans and checks that every original scalar selector remains. It does not mutate a queue or select a future parent.

For a restored local source-only environment, the complete commands are:

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_radial_public_reference_sources.mjs --repo REPO --outdir EMPTY_SOURCE_SCRATCH --verify-existing
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/make_radial_public_reference_ready.mjs --repo REPO --outdir EMPTY_PARAMETER_SCRATCH --verify-existing
```

These command lines are provided for reproduction. They were not executed in the unavailable executor. The equivalent complete text transformations and full output hashes were checked in V8. No AST/compile status is borrowed from the parent families.

The delivery manifest contains all twenty-one complete runtime records, all five constructor records, all three complete parameter records, this note, the entire runtime role registry, the complete already-published construction-parent list and exact total added bytes. Every newly written item has a real remote unreferenced blob. No repository ref was modified by this agent.

## 14. Remaining actual costs and error responsibilities

This is a larger complete scientific run. It does not establish that a run will fit a particular wall-time limit.

Constructing the fine observation input rebuilds the actual current scalar table and computes every required a query before the first complete field report. That is actual setup work, not a separate fixture or a silent unreported substitute. The working strict-width, scalar-table, old-word or exact-input checks can reject an input. Such a rejection does not establish geometric impossibility.

The new complete field has twice as many radial cells. All full variables, all original/new observations, full point pullbacks, all normal stages and all true screens are retained. No predicted cache hit rate, cost saving or convergence improvement is attached to this source package.

The accurately intended outer polynomial inclusion, actual binary midpoint injection, finite selected normal chain, numerical quadrature, physical sixjet and continuous geometric claims have separate responsibilities. The saved scalar a enclosures do not discharge the other responsibilities. Likewise, complete finite E screening does not supply continuous reach or embedding bounds.

A subsequent real report can determine whether the larger current space improves the actual objective while respecting the complete geometry policy. Until then, the package consists of complete executable sources, exact input/source contracts and complete parameter plans, with no invented scientific result.

## 15. Root complete-source publication review and notation correction

2026-11-27, Astra-larger-e4e2a2bf-20261126 (AI-assisted) reviewed the complete delivery before ordinary publication. The original note was 26886 bytes, SHA256 `134aa876eced56f84b96c4b83e28a85b5b15442c498c3926cb53e39ff09c969f`, Git blob `f443f32b0ddd76c8cab3d8c0b48cb55822ba62ca`. Section 3 now correctly writes $X_i=A_i S+B_i$: the pair contains the coefficient of $S$ first. The complete implementation already used this convention. [The complete notation correction](2026-11-27-actual09-radial-affine-pair-notation-correction.md) preserves the exact original identity. No runtime, constructor, parameter or target byte was altered by this note correction.

Root checked every one of the original thirty complete delivery files by byte count, SHA256 and Git blob, the seventeen whole construction parents, and all seventy-eight complete runtime roles. Existing role blobs still match the actual public tree at `765693263eb462607183208a692ec2218863e353`; newly delivered roles match their entire candidate bodies. All seventeen complete text transformations were replayed forward and inverse to their pinned whole parents. No sampled line range substitutes for a whole-file identity.

The full original normal class is byte-identical (83349 bytes, SHA256 `79afd13e450ca6ebd570a82538bf1f1ff53a2585339c1371e4ffb257878601e7`), and the geometry suffix from `_set_x` is byte-identical (38112 bytes, SHA256 `3c1d3691dbb027201bd6759977ad62856d82f0f3a76615aa6dc609dfce62d8e9`). Removing only the two explicitly declared complete common-parent-statistic insertions recovers the original entire scientific suffix: 19574 bytes, SHA256 `d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`. The current extended suffix is not itself described as unchanged.

Root also evaluated only the pure JSON parameter constructor in V8. All three complete output texts equal their delivered original bytes. All original 333 scientific and 317 pure selectors survive with identical keys and field paths, becoming 357 and 333. The fixed-target objects match the complete original parent ready. The independent 151-word command changes only the output path, adds the explicit factor two and retains the unknown09 obligation; terminal/final commands use strict actual-parent inputs and preserve unknown lineage through the complete parent report. The pure commands change only report/output paths. The complete scientific numeric parameter set is retained; no future parent SHA is filled in.

An independent full-source review examined exact affine query transport, all three shared-quintic channels and endpoint jets, old/new nonnested Gauss union and positive weights, current scalar replay, actual common-parent residual statistics, strict thirteen-member parent transfer, uncapped typed memory and complete pure attribution. The notation correction is the only change from that delivered source package. These are source and parameter checks, not a Python AST/compile, Node CLI run, scientific execution, numerical refinement result or continuous geometric certificate. All three plans remain unqueued by this publication.
