# Complete independent restoration-damping continuation entry

Prepared at 2026-11-28 00:57:30 UTC. Intended independent branch: run23. These complete sources implement the already published success-dependent restoration policy in the whole run19/run20 scientific family. They do not modify run22's paired-halfwave sources, any running job, or the geometry-first ordering proposal. No new actual report, damping decision, accepted point, final checkpoint, speed measurement or scientific conclusion is supplied.

## 1. Implemented family and exact scope

The complete parent driver is `fullclosed_fixed_fejer_meridian_batched_so3_qp.py`, 99,313 bytes, SHA256 `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f`, blob `8bba3e30bb8e843fd725a2d19f8966b984acc4ae`. The complete parent reader is 99,382 bytes, `8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49`, blob `9cd36fd99113d285fc47f17bad929647c8fc6de3`. Its complete launcher is 22,136 bytes, `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`, blob `168b1a1d7bc58793985138eb8a02a6e3911d74cc`.

The reused policy is the original complete `fixed_fejer_restoration_damping_continuation.py`: 18,684 bytes, SHA256 `be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710`, blob `05eb88969c5e83cf2f01fcb3f02e40f4cbea0775`. It has not been rewritten or numerically evaluated here. The prior complete integration design (9,970 bytes, `66cef891231f05135c1202ffe95d64695de0d8b6cb4152c4551e0f0e46e827a5`, blob `03d7e0fca68437e64028adf78f3266b50f7f7ed2`) and full mathematical/source note (24,517 bytes, `6f524129b8a595e2991f90624506f52fd5271304493152dc05820681eca127d5`, blob `28116820d3b4d0a8e61a5c71fa1d7164da0f601f`) remain complete provenance.

Three independent new runtime files implement the integration. All 137 original scientific role/path/SHA pairs remain exactly in their original order. The sole additional role is `restoration_damping_policy`, giving 138. The current runtime table has 19 responsibilities: the original 18 with actual new driver/reader/launcher records, plus the unchanged published policy. The other 15 runtime records are unchanged complete files. No old source file is overwritten or relabeled.

The exact current schemas are:

- report: `complete-fixed-fejer-restoration-continuation-observed-envelope-SO3-QP-v1`;
- pure readout: `actual-fixed-fejer-restoration-continuation-envelope-SO3-readout-v1`;
- launcher command record: `public-actions-complete-fixed-fejer-restoration-continuation-SO3-command-v1`.

The normal operator, whole field model, frozen Fejer target, full-wave seed, full variable layout, coordinate norm, both mean calculations, every normal stage, root/frame/J/J* implementation, material memory, typed rows, complete geometry, and observer are the unchanged parent modules. The algorithm change is a declared rule for the damping used in a later restoration direction.

## 2. Every driver change and its timing

The complete driver has four exact text substitutions. Three are the already published implementation design; the fourth declares the new report schema. The full inverse of these substitutions gives every byte of the original 10fa source.

| Change | Actual complete-source location | Meaning |
| --- | --- | --- |
| Add one literal source role | `SOURCE_PINS`, new line31 | The original full source check reads and hashes the entire policy file with all other source roles. |
| Load policy and initialize its declaration | New lines788–789, after the complete report object | The policy source identity is taken from the actual `report.source_sha256_by_role` map and its full definition is saved before the original first report write and initial residual. |
| Apply next-restoration rule | New line1088, after the complete original acceptance/failure block | It consumes the completed direction record and actual model identity, records the decision, and returns only the next restoration damping. |
| New independent schema | New line30 | Old reports cannot masquerade as this new algorithm's reports. |

The insertion after the unchanged failure block is exactly:
```python
if phase == 'restoration':
    restoration_damping=restoration_policy.after_original_update(record,report,restoration_damping)
```
It follows, rather than replaces, the original `if not record['accepted']` block. Thus an unsuccessful restoration direction first receives its original multiplication by four. The policy receives that actual post-block value; it does not reinterpret a failed direction as accepted or undo the original failed-direction update.

All original line trials, point construction, field residual, statistics, domain checks, true finite geometry, acceptance inequalities, accepted bundle writing, observer calls, loop breaks and halving of alpha remain byte for byte. The original metric-phase damping update also remains byte for byte. A metric direction never calls the new post-update function.

The new call precedes only the original final direction timing/counter fields, `damping_after_direction`, appending the direction to the report, the phase count increment, cache clearing, resource release, and `save_report()`. Their order remains unchanged. The added scalar work is therefore included in the original direction elapsed time, and the existing `damping_after_direction` records the actual value that will be used next.

The original trial ordering remains residual → statistics → conditional geometry. In particular, the metric descent early-rejection rule still skips geometry in its original circumstances. No geometry-first reorder is hidden in this family.

## 3. Exact already-returned data consumed by the policy

The policy imports only `hashlib`, `json`, `math` and `sys`. It has no field object, tensor, linear operator, integration plan, root solver, file reader or new array evaluation. The source check and pure reader use the original normal source-reading infrastructure; they are not new scientific calls.

The input values have concrete original producers:

| Consumed record | Original producer and interpretation |
| --- | --- |
| `record.actual_damping` | Actual damping passed to the original complete `qp.solve`. |
| `record.accepted`, `accepted_alpha` | Original nonlinear trial acceptance and literal alpha; written only after that unchanged decision. |
| `record.starting_geometry` | The complete finite geometry object used at the beginning of this direction. |
| `record.accepted_geometry` | The actual complete finite geometry object returned for the accepted candidate; not a latest mutable observation. |
| `record.complete_selected_inequalities` | Original full selected row metadata, including the retained geometry/amplitude prefix and appended permanent typed rows. |
| `record.selected_linear_physical_g` | Already computed after the original QP, by the existing full row product and `physical_g + row_normalization_scale * product`. No new product is made. |
| `record.qp`, `coordinate_step_norm` | Existing QP diagnostics and already computed step norm; retained as evidence, not converted into an exact-optimality assertion. |
| `report.model_identity_sha256` | Actual complete current model identity already bound by the driver. |

The relevant original row writer is `complete_material_envelope_rows.py`, 13,744 bytes, SHA256 `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7`. Its full original metadata is copied and extended, including all selected rows; it does not replace the geometry `source_binding`. The complete geometry source `so3_fixed_fejer_batched_missing_angle_geometry.py`, 88,163 bytes, SHA256 `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135`, writes the actual model into that binding and writes each complete row set's current full point. This makes the policy's own-point/model comparisons actual available interfaces, not proposed new report fields.

For a qualifying direction the policy requires a genuine original accepted restoration step with literal \(\alpha=1\). The complete starting and accepted finite geometry must have the same current model as the report; the selected row point must equal the starting geometry point; the accepted point must have its own valid identity. Both complete value lists must be present, finite, equally long, and agree with the retained selected-row count. A missing or ineligible scientific observation leaves the original next damping unchanged.

## 4. The decision is an explicit algorithm choice

Using the existing complete finite-geometry maximum and complete selected lists, define
\[
G_0=\max(0,g_{\mathrm{whole,start}}),\qquad
G_1=\max(0,g_{\mathrm{whole,accepted}}),
\]
\[
M_0=\max(0,\max_i g_i),\qquad
M_1=\max(0,\max_i(g_i+Dg_i[p])).
\]
The complete selected list is preserved. It is not quietly enlarged or reduced for this policy, and a selected maximum is not called a whole-surface certificate.

The full-step prediction is \(P=G_0-M_1\), and the actual finite decrease is \(A=G_0-G_1\). The declared working tolerance is
\[
\eta=64\,\epsilon_{\mathrm{binary64}}
 (1+|G_0|+|G_1|+|M_0|+|M_1|).
\]
Only if the original accepted full step has all required own-point/model evidence, \(G_0>0\), \(G_1<G_0\), \(|M_0-G_0|\le\eta\), \(P>\eta\), and \(A/P\ge3/4\), may the next restoration damping become
\[
\mu_{\mathrm{next}}
 =\min\{\mu,\max(10^{-8},\mu/10)\}.
\]
Otherwise it remains the value produced by the original success/failure rule. At or below the floor a qualifying success cannot increase damping. A rejected direction or an accepted shortened step retains the original rule immediately.

The comparisons are ordinary working binary64 algorithmic comparisons. They are not directed bounds and do not pay a root, metric, quadrature or continuous geometry fee. QP convergence status, projected-gradient norm and product counts are retained in the decision evidence, but there is no additional KKT or fixture gate. In particular, a finite 64-advance QP run is not asserted to be an exact optimum.

The exact comparison theorem remains limited to a fixed common linear feasible set and exact QP minimizers: decreasing the regularization parameter cannot increase the optimal nonnegative common slack \(\tau\). That statement neither gives an order for finite-iteration QP results nor proves monotonicity of the next nonlinear full-geometry value. The feasible set changes after a new point, and the actual line-search branch can change. The already observed rejection of lower-damping or later trials is therefore not erased or contradicted by this implementation.

This rule is intended to avoid indefinitely keeping a large restoration regularization after a genuine, full, well-predicted accepted step. Whether the current public branch ever meets its condition, whether it reduces damping, and whether the subsequent original-budget solve improves remain actual execution questions. No prior unknown alpha, QP residual, prediction or damping decision is filled in.

## 5. Complete pure-reader integration

The new reader has four declared policy insertions and four necessary source/path/schema substitutions. All other bytes reverse exactly to the 8027 parent. Its four policy insertions are:

1. Append `restoration_damping_policy / validate_report` to the existing complete helper loop.
2. Dispatch the policy's stdlib validator with the actual whole policy SHA, after the existing module and function file identity checks.
3. Retain the complete per-direction `restoration_damping_continuation` object in each direction readout.
4. Add the complete pure policy validation result at the top level of the readout.

Every original geometric, row, metric, trial, full-source, model, input, packet, normal/frame/closure diagnostic, final-bundle and reported-completion check is retained. The new validator does not substitute for any of those checks.

For each recorded completed restoration direction, `validate_report` begins from the report's actual initial restoration damping, checks the used damping against the continuation from the previous completed direction, reconstructs the original accepted/failure baseline, recomputes the complete scalar policy decision from that direction's own recorded data, and compares the entire saved decision and actual `damping_after_direction`. A complete report must also match the final restoration damping. An incomplete report validates only its recorded completed directions and never reconstructs a pending or unreturned direction.

The original report appends a direction only after the policy call and final direction fields. Thus a first-F failure or an incomplete report with no completed directions legitimately has an empty decision list; that is not filled from a live progress file. Future decisions and reduction counts are absent until they actually exist.

The ordinary pure reader remains callable with its full original seven-argument invocation, using the actual new report namespace and new complete reader source. No scalar projection is silently substituted for the full policy readout.

## 6. Why the unchanged lower source family is reused intact

The following actual complete consumers were read through their relevant interfaces:

- `fixed_fejer_meridian_source_binding.py`, 41,894 bytes, `3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68`: `validate_current_model` iterates its exact lower source bindings and verifies the complete existing q model/policies. `read_actual` validates each original snapshot at its own point. No lower source or model changed.
- `fixed_fejer_meridian_root_packets.py`, 73,723 bytes, `c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4`: its entry validator uses the actual report caller SHA and complete actual source map. Its caller loader reads the whole literal current registry, so the added actual policy role is retained rather than hidden.
- `fixed_fejer_batched_geometry_report_binding.py`, 12,136 bytes, `9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06`: it still binds the same complete geometry, normal, detached-meridian policy, exact stage partition, angle block and each scan's own point.
- The shared complete transfer remains `b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc`. The five supported peer CLI pairs and the original independent/restart distinctions are unchanged.
- The shared scalar observer remains the complete `321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5` source. It receives the actual new driver/report identity through its existing API.

These uses justify reusing the existing complete lower modules, not pretending the new driver has the old source SHA. The new reader and launcher explicitly bind the new whole driver. Old 10fa-only accurate-fee, mesh, refinement or other report consumers do not automatically accept the new driver; any such future adaptation must bind this complete new family. This source delivery does not claim that adaptation has already occurred or that any fee result exists.

## 7. Full numerical parameter and history boundary

The isolated comparison is the full run19 bhalf numerical baseline: \(b/S=1/2\), \(\delta=1/32\), initial metric damping \(.01\), initial restoration damping \(.01\). The complete parameter parent is 90,652 bytes, SHA256 `242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67`, blob `9c4c28ef3c5b189e094c65f51038fafeef48bc48`. Its whole pure parent is 80,254 bytes, `8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7`, blob `202b6ca81c72c009c34c04094ef234db2e337328`.

No CLI option or default was added or removed in either parser. The complete original 157-word science and seven-word pure invocation retain their numerical semantics. The original 458/445 formal projections and all 48 live mappings remain valid for their original fields; the policy adds its full report/readout records without removing a previous field.

All free coordinates, both mean obligations, the 32 stages, all root iterations/backtracks, the entire observation/permanent union, uncapped typed rows, the selected prefix, metric/restoration direction allowances, 16/64 inner advance budgets and 15 line trials remain. No time cutoff, fewer trials, lower-dimensional problem, dummy probe or separate replay gate is introduced.

The original independent branch does not inherit a prior accepted field just because the q model is mathematically unchanged. All five supported original peer CLI declarations and the full external history obligations remain genuine prior-source obligations. Unknown complete report, final checkpoint, typed discovery order or accepted history stays unknown. A future same-source restart must pass the existing whole new-schema/new-source complete-final contract; no partial progress or accepted bundle is promoted to final.

This source delivery itself is unqueued and leaves all future run/input/model/point/report/checkpoint and policy-decision values null. Root owns the complete actual ready/queue/public launch. The existing numerical choices do not establish that run23 has run or that its conditional policy has fired.

## 8. Reproducible whole source construction

The MJS constructor reads the three exact full parent source files and the exact complete policy, applies all declared literal substitutions, checks their whole inverses, and writes the three entire new runtime files. It verifies the expected whole output byte counts and hashes and confirms that the complete source registry is exactly the original ordered 137 pairs plus the sole policy pair. It never imports Python or any scientific module.

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_sources.mjs --repo <complete-repository> --output-directory <generated-tree>
```

This is an archival source-text constructor, not a new Actions scientific step or a precondition added to the solver. The present work used only whole-source reading, literal text/JSON construction and exact inverse/hash comparisons. No independent local execution of the MJS, no Python AST/compile, numerical fixture, scientific solve or performance measurement is claimed.

Complete new records:

- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_restoration_continuation_so3_qp.py`: 99763 bytes; SHA256 `9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699`; full Git blob `1a50449bef3e207cc30797697a07e20437792d9b`.
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_restoration_continuation_so3_report.py`: 99757 bytes; SHA256 `14c2dfac957632fc46e2e6ed06a9475bcac5a9dda59692941b4553ada8c322f8`; full Git blob `35a93e1063a121f9e2e59594d5b8cb4ff3a666d5`.
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_restoration_continuation_actions.py`: 22152 bytes; SHA256 `f2a9e38f62a3844b5d9ce8df9399f6702f37e6fc96c792d0dcb0bb61a80e1371`; full Git blob `e6d7013b4216935c05dad63eb7961f419f39a973`.
- `topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-current-runtime-binding.json`: 64341 bytes; SHA256 `ad6980f8f1e57ce92eb442a57cc2c7f1584e9bec7c1ea876ce7a952e7ff2277c`; full Git blob `2f6776c3c86578152d5dfcf856c3d216da35c725`.
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_sources.mjs`: 11011 bytes; SHA256 `bfd71bab0d94c8a81f2ed22fb67092ce4d01e7b30638d4bbc5cd1a8b6753641b`; full Git blob `e19764480d1e0f5e3140befdf19a19d606b6132d`.

The final manifest additionally binds this whole note, the unchanged policy/design/mathematical note, all current source-role identities and full parent recovery. Every new file is below 100,000 bytes. The original driver/reader bodies have not been shortened to fit: the new driver is 99,763 bytes and the new pure reader is 99,757 bytes.
