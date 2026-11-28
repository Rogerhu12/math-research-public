# Run23: complete run19 half-width parameters with restoration-damping continuation

Prepared from complete bound source and parameter text on 2026-11-28 01:02:59 UTC. This document and the accompanying files prepare an independent scientific branch. They do not record a run23 execution, accepted point, complete report, root/mean result, checkpoint, error fee or continuous certificate. Root owns all publication, workflow and queue operations.

## 1. The single change and the exact baseline

Use the whole run19 supported seed with relative boundary total length **1/2**, profile delta **1/32**, initial metric damping **.01** and initial restoration damping **.01**. Keep the original full-wave seed. Keep the original statistics-before-geometry order. Do not import the run22 paired-halfwave seed or the separate geometry-first proposal.

The only new mathematical algorithm component is the already published, complete restoration-damping continuation policy. The new driver invokes it after the original completed restoration-direction update. It can choose the next restoration damping from actual values already produced by that direction. It adds no new field, Jacobian, adjoint, root, quadrature, geometry or acceptance evaluation. The original acceptance inequality, original failed-direction multiplication by four, domain checks, finite-iteration algorithms, budgets and return order are retained.

The exact original parents are:

| Complete parent | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json | 90652 | 242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67 | 9c4c28ef3c5b189e094c65f51038fafeef48bc48 |
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json | 80254 | 8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7 | 202b6ca81c72c009c34c04094ef234db2e337328 |
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json | 25057 | cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d | fac08bdbafbefd0e599687e2b7f0a5c6e71382e7 |

All three were published with the actual run19 launch at commit `543cfdf281c9bcd0f9b13197721b003a275c5967`. A whole parent is retained as scientific and parameter provenance. It is not an accepted-state input.

The new independent runner namespace is `fixed-fejer-restoration-continuation-bhalf-first`. The intended label is `parallel23`; the actual run ID, actual input records, model, point, policy decisions and final report/checkpoint identities remain null. The original necessary maker/reference stages keep their mathematical contracts and complete arguments. The seed boundary parameter lives in the science arguments, not in a renamed maker input.

## 2. Complete source identities and what “unchanged” means

Current complete entry source records:

| Runtime | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_restoration_continuation_so3_qp.py | 99763 | 9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699 | 1a50449bef3e207cc30797697a07e20437792d9b |
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_restoration_continuation_actions.py | 22152 | f2a9e38f62a3844b5d9ce8df9399f6702f37e6fc96c792d0dcb0bb61a80e1371 | e6d7013b4216935c05dad63eb7961f419f39a973 |
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_restoration_continuation_so3_report.py | 99757 | 14c2dfac957632fc46e2e6ed06a9475bcac5a9dda59692941b4553ada8c322f8 | 35a93e1063a121f9e2e59594d5b8cb4ff3a666d5 |
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_restoration_damping_continuation.py | 18684 | be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710 | 05eb88969c5e83cf2f01fcb3f02e40f4cbea0775 |

The complete current source binding is `topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-current-runtime-binding.json`, 64341 bytes, SHA256 `ad6980f8f1e57ce92eb442a57cc2c7f1584e9bec7c1ea876ce7a952e7ff2277c`, blob `2f6776c3c86578152d5dfcf856c3d216da35c725`. It contains both full scientific registries, all current runtime records and the full parent/patch provenance.

There are **138 scientific source roles**: every one of the original **137 role/name/SHA pairs is unchanged**, followed by the explicitly added `restoration_damping_policy` role. There are **19 current runtime responsibilities**. Three complete entry files, driver/reader/launcher, replace their corresponding runtime responsibilities; the complete published policy is added; all remaining fifteen current runtime records are unchanged. Scientific source-role count and runtime-responsibility count are different quantities. The driver itself is not smuggled into an old source-role pair.

The original lower normal, closure, stage/frame/J3 caches, physical geometry, material history transfer, original seed/mean/reference/scalar definitions and complete observer sources retain their whole identities. Existing old-family fee, mesh or refinement consumers are not silently declared compatible with this new driver. A consumer that pins the old 10fa entry requires an explicit whole-source adapter when it is used.

The independent source integration is fully recorded in:

- Source manifest: `topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-complete-entry-delivery.json`, 19448 bytes, SHA256 `d1bc3354d5a7aebcaf82abb8832e47b7e9690eacc90fa892f65b17358f57149e`, blob `f159d88086202555ad1d71575fc1cea522e59dac`.
- Complete source text reproducer: `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_sources.mjs`, 11011 bytes, SHA256 `bfd71bab0d94c8a81f2ed22fb67092ce4d01e7b30638d4bbc5cd1a8b6753641b`, blob `e19764480d1e0f5e3140befdf19a19d606b6132d`.
- Full integration note/proof: `topics/visible-flex-larger-amplitude/notes/2026-11-28-complete-restoration-continuation-entry.md`, 19961 bytes, SHA256 `d8c5ec7dc4522e87b448ba3bcd013628e373c776a1774d2c416c53c80ef543db`, blob `838f962c5453be7a881e81243c2910f5f0a52b71`.
- Original integration design: `topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-complete-integration-design.json`, 9970 bytes, SHA256 `66cef891231f05135c1202ffe95d64695de0d8b6cb4152c4551e0f0e46e827a5`, blob `03d7e0fca68437e64028adf78f3266b50f7f7ed2`.
- Original mathematical/source-design note: `topics/visible-flex-larger-amplitude/notes/2026-11-28-complete-restoration-continuation-source-design.md`, 24517 bytes, SHA256 `6f524129b8a595e2991f90624506f52fd5271304493152dc05820681eca127d5`, blob `28116820d3b4d0a8e61a5c71fa1d7164da0f601f`.

The old entry/parameter files remain original historical files; no original source or active job is overwritten.

## 3. Entire numerical parameter contract

The science ready contains one complete **157-word** argument vector. The pure ready contains one complete **7-word** vector. There is no added policy CLI flag or omitted default. Restoring the original namespace in each vector makes every word equal to the run19 parent. The only science argument word that changes is the output path at index71. Pure indices3 and5 change to the current report/readout namespace.

Important original values, in their literal CLI spellings:

| Item | Complete retained value |
|---|---|
| Current/frozen input dimensions | M160, J923, N2048 in the complete unchanged source/input contracts |
| Angle count, stage/angle block, working integration | 2048; 64; 8; order8 |
| Norm | jet-sum, radial length .05, angular transition24 |
| Torch threads | 4 |
| Metric start and work | damping .01, 1 direction, maxiter16 |
| Restoration start and work | damping .01, 4 directions, maxiter64 |
| Line search | 15 trials |
| Selected original rows | 192, with the original permanent/history union and appended rows retained |
| QP tolerances | atol0, rtol1e-6 |
| Reach | ratio .03, safety factor .992 |
| Active band | .025 |
| Marked diameter/witness/height budgets | 4.2; .9; 1.01 |
| Spectral measure | p4, epsilon .001, scale .05, legacy fraction .5 |
| Stop target | 1e-9 |
| Reference construction panels | 128 |
| Normal stages | all32 |
| Endpoint roots | tolerance2e-12, iterations24, backtracks18, Armijo1e-4 |
| Control radius | 2 |
| Seed boundary/profile | 1/2; 1/32 |
| Seed quadrature | radial8; profile16 |
| Mean root | maxiter128, tolerance2e-12, backtracks24, Armijo1e-4 |
| Scalar inverse | iterations64 |
| Envelope near-active rows | 32 |
| Independent branch | original flag retained |
| Original supported pending pairs | all5 pairs, unchanged and in original order |

All support/gamma endpoint words, complete Q definition/input path/input SHA, all source pins, full parameter arrays, norm definitions, permanent points, typed/history obligations and output cleanup/retention fields remain in the complete step object. This table does not replace that object.

The science full argument vector is reproduced here only for readable review; the actual whole ready is authoritative:

```json
[
  "--repo",
  "{repo}",
  "--reference-bundle",
  "{work}/fixed-fejer-reference/reference.npz",
  "--preparation-report",
  "{work}/fixed-fejer-reference/report.json",
  "--carrier",
  "{work}/fixed-fejer-reference/observations.npz",
  "--node-report",
  "{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
  "--scalar-input",
  "{work}/fixed-fejer-r690-inputs/fixed-scalar-input.json",
  "--angles",
  "2048",
  "--stage-block",
  "64",
  "--angle-block",
  "8",
  "--integration-order",
  "8",
  "--norm-kind",
  "jet-sum",
  "--radial-norm-length",
  ".05",
  "--angular-transition",
  "24",
  "--torch-threads",
  "4",
  "--damping",
  ".01",
  "--directions",
  "1",
  "--maxiter",
  "16",
  "--restoration-directions",
  "4",
  "--restoration-damping",
  ".01",
  "--restoration-maxiter",
  "64",
  "--line-trials",
  "15",
  "--active-rows",
  "192",
  "--qp-atol",
  "0",
  "--qp-rtol",
  "1e-6",
  "--reach-ratio",
  ".03",
  "--reach-safety-factor",
  ".992",
  "--active-band",
  ".025",
  "--marked-diameter-budget",
  "4.2",
  "--witness-lower-budget",
  ".9",
  "--amplitude-height-floor",
  "1.01",
  "--spectral-p",
  "4",
  "--spectral-epsilon",
  ".001",
  "--spectral-scale",
  ".05",
  "--legacy-fraction",
  ".5",
  "--target",
  "1e-9",
  "--outdir",
  "{work}/fixed-fejer-restoration-continuation-bhalf-first",
  "--panels",
  "128",
  "--endpoint-bubble-1-left",
  "1/32",
  "--endpoint-bubble-1-middle",
  "1/4",
  "--endpoint-bubble-1-right",
  "15/32",
  "--endpoint-bubble-2-left",
  "17/32",
  "--endpoint-bubble-2-middle",
  "3/4",
  "--endpoint-bubble-2-right",
  "31/32",
  "--endpoint-root-tolerance",
  "2e-12",
  "--endpoint-root-iterations",
  "24",
  "--endpoint-root-backtracks",
  "18",
  "--endpoint-root-armijo",
  "1e-4",
  "--moment-definition-sha256",
  "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
  "--moment-input",
  "{repo}/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
  "--moment-input-sha256",
  "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
  "--endpoint-control-radius",
  "2",
  "--gamma-left",
  "1/16",
  "--gamma-middle",
  "1/8",
  "--gamma-right",
  "3/16",
  "--moment-input-binding",
  "supported-smooth-triangle-reference",
  "--normal-stages",
  "32",
  "--seed-boundary-total-length",
  "1/2",
  "--seed-profile-delta",
  "1/32",
  "--seed-radial-quadrature-order",
  "8",
  "--seed-profile-quadrature-order",
  "16",
  "--seed-mean-maxiter",
  "128",
  "--seed-mean-tolerance",
  "2e-12",
  "--seed-mean-backtracks",
  "24",
  "--seed-mean-armijo",
  "1e-4",
  "--seed-scalar-iterations",
  "64",
  "--manifest",
  "{work}/fixed-fejer-reference/locations.json",
  "--material-envelope-binding",
  "{work}/fixed-fejer-reference/material-envelope-carrier-binding.json",
  "--envelope-near-active-rows",
  "32",
  "--independent-envelope-branch",
  "--pending-parallel-envelope-run",
  "45909290354/1",
  "--pending-parallel-envelope-source",
  "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
  "--pending-parallel-envelope-run",
  "45929088658/1",
  "--pending-parallel-envelope-source",
  "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
  "--pending-parallel-envelope-run",
  "45943410994/1",
  "--pending-parallel-envelope-source",
  "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
  "--pending-parallel-envelope-run",
  "45972294636/1",
  "--pending-parallel-envelope-source",
  "45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
  "--pending-parallel-envelope-run",
  "46011377225/1",
  "--pending-parallel-envelope-source",
  "46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
]
```

The whole pure vector is:

```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/fixed-fejer-restoration-continuation-bhalf-first/report.json",
  "--output",
  "{work}/postprocess/fixed-fejer-restoration-continuation-bhalf-first-readout.json",
  "--verify-final-bundle"
]
```

The two original metadata values `complete_original_parameter_metadata` and `pre_repair_current_runtime_source_records` are shared through an `exact-whole-parent-JSON-value-reference-v1` record. Each includes the whole parent file path, bytes, SHA256, Git blob and exact JSON pointer. This preserves the complete original value without embedding the same history yet again. It is not truncation, field deletion or replacement by a summary. Every other replaced current top-level value has its original key and pointer recorded in `complete_immediate_parent_metadata_recovery`; all original keys remain in the ready.

## 4. Policy input, eligibility and boundaries

The exact algorithm and ordinary scalar computations are in the unchanged whole policy source. The parameters do not redefine that implementation.

For a completed restoration direction, the policy uses the original starting and accepted complete finite-geometry violations, the original selected-row values and complete full-step predictions, the actual accepted alpha, the original selected-row metadata and their own point/model bindings. It does not substitute latest mutable progress data. The original driver has already evaluated these quantities before the policy call.

The eligible reduction is deliberately narrower than “an accepted trial”:

- The original direction is an accepted literal full step, alpha=1.
- Complete own-point/model bindings, full selected/predicted row lists and finite scalar values are present.
- The selected row origin agrees with the whole starting positive violation within the implemented scaled floating tolerance.
- The original whole positive violation strictly decreases and the predicted reduction is strictly positive.
- The actual-to-predicted reduction ratio is at least .75.

Only then can the next restoration damping decrease by a factor10, with floor1e-8 and without increasing the successful current value. Every unavailable, ineligible or inconsistent comparison follows the policy's exact unchanged retaining/validation behavior. A backtracked accepted step does not receive a guessed full-step prediction. An original failure keeps its original times4 update. Metric damping is untouched.

The exact mathematical monotonicity statement from the bound design concerns two exact QP minimizers on the same complete linear feasible set. Since the slack is constrained nonnegative, the appropriate comparison yields nonincreasing optimal slack as its regularization weight is reduced. It gives no monotonicity guarantee for a finite64-iteration QP result, a nonlinear complete trial, field curvature, Gram residual, step alpha or final feasibility. The actual rejected run19/run20 trials remain contrary to any claim that a smaller initial mu must improve true geometry. This preparation does not infer a cause from small Phi changes and does not fill an unpublished alpha or QP residual.

The new pure reader retains every old check and reconstructs the continuation decision from each completed direction's own report data. It adds the complete policy validation to its ordinary readout, while preserving the original report/final binding requirements. A partial report is not promoted to final by the extra policy record.

## 5. Formal and live observation

The science whole formal summary retains all **458** original selector pairs. The pure summary retains all **445**. Their relative ordering and scalar selector strings are unchanged; only current file paths change.

The live map retains exactly **48** scalar fields, the original6 normal fields and42 mathematical fields. The existing full observer source is unchanged. Current/initial/trial points and source/model identities remain separate. Existing six signed geometry families and last-completed-trial fields remain available under the same selectors. No new live field replaces an old one and the controller's48-field limit is not exceeded.

Policy decisions are complete in the original scientific report's new per-direction/top-level metadata and the new complete pure readout. They are not squeezed into an existing live scalar under a different meaning. The parameters do not request a second scientific evaluation to display policy data. Absent progress/report values remain absent/null with the original error semantics.

Current output paths are:

- Science report: `{work}/fixed-fejer-restoration-continuation-bhalf-first/report.json`.
- Complete command record: `{work}/fixed-fejer-restoration-continuation-bhalf-first-command.json`.
- Normal progress: `{work}/fixed-fejer-restoration-continuation-bhalf-first/actual-normal-evaluation-progress.json`.
- Mathematical progress: `{work}/fixed-fejer-restoration-continuation-bhalf-first/actual-mathematical-progress.json`.
- Pure readout: `{work}/postprocess/fixed-fejer-restoration-continuation-bhalf-first-readout.json`.

All original cleanup patterns, scratch-only raw storage and fixed reference-cache retention semantics remain in the actual complete steps.

## 6. Original and external history responsibilities

The five original supported CLI run/source pairs are kept byte-for-byte in the157-word science vector. No new source is inserted into the old transfer's PARENT_FAMILIES.

The original six external obligations are the exact prefix of the new list. They include the independently running/refined/terminated branches originally declared in run19. Actual runs19,20,21 are additionally recorded with their true old10fa complete scientific source, full published parameter/start records and unknown final/typed fields. They are not relabeled as the current9db3 family.

Actual run22 is also explicitly registered as an external obligation because the parent supplied its official start: run46090913581/1, job140811337445, created2026-11-28T01:00:48Z, head18081452c5181d958bb5432c4045c067bf1d1caa. Its whole driver remains095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec and its halfwave mechanism differs from this run23 full-wave seed. That known start is not a new actual run23 input or transferred field. The record is explicitly parent-provided evidence, not a new API poll. Its full source/parameter records are bound; future final/typed remain unknown.

There are therefore **10 external obligations**, in addition to the five supported CLI pairs. Dated in-progress snapshots in earlier parameter records are retained as dated history, not asserted to be the current API status.

The entire run17 terminal note was actually retrieved and its whole identity matched:

`topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-wide-seed-actual-mathematics.md`
—81523 bytes, SHA256 `2bdbea9519316f03bd8680d99a381d691810a3f880106f868bfbcc5277b415fc`, blob `d3858027922738a6df247eb109ccfd9d45850b80`, published commit `54ac2aa5bc33a4383bc6528f4f5213111daac113`.

It records official completed/cancelled, updated2026-11-28T00:53:34Z; the cancellation cause is unknown. Its two required inputs returned0. The scientific child did not naturally return. The last published current observation had3 accepted directions; the next52bca trial lacked returned statistics, geometry and decision. No final/checkpoint or complete typed history is manufactured from these facts. The complete note and original source obligation remain, including the complete original observed values; no old accepted point becomes this runner's initial point.

## 7. Full text reproduction and file identities

The three parameter objects use compact UTF-8 JSON plus exactly one newline. New whole bytes and SHA256 are explicit and are not claimed equal to the old parent's bytes. The difference is a serialization and declared current-source/namespace/policy mapping, not deleted scientific content.

The complete text constructor reads the whole original science/pure/display parents, the complete current source binding and whole17 terminal note. It constructs the same complete JSON objects, verifies their explicit whole hashes, and can write them into a separate generated tree. It performs no scientific import or numerical evaluation and is not a stage in the research queue. The source is retained for reproducibility, not made into an extra approval or fixture requirement.

```text
node scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_bhalf_parameters.mjs \
  --repo <complete-repository-root> \
  --output-directory <separate-generated-tree>
```

The output includes the topic-relative paths. To run from a repository root, use the full topic-prefixed script path shown in the table below.

| Artifact | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-science-complete-ready.json | 98798 | 95f7a9337ec20245b4c7f9c35ba74081b718643222a4c4023299532d7562d34f | 2fcf6bda73d3fc050fd8e9a9b81e97511031e18d |
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-pure-complete-ready.json | 88534 | 536b7ddb2ff5eaa71f7252e96061c1f44547a62618955efc45c4db5db854f686 | 189138a03de3aff0e2cc5644570b59b7bca49969 |
| topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-complete-display-correspondence.json | 30357 | 5e1ab150d09a0c8c893fb8ece293d2e3c6acf5a6077f2bd01cd0c8df5c5edc18 | 174a0d77589e9cb1742236c5c5cbc5b64f1ceee4 |
| topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_bhalf_parameters.mjs | 34358 | 81ea97e5577b2c96f29d3683312ed2f5c02357615a9a44ae9526ff2fca948faa | fe9800d95c4557348eb29e7567c794aba8a134ea |

The source preparer checked the exact JSON mapping: reversing the current namespace and restoring only the declared step id/script/scope gives the entire original step value; every original top-level key remains, both shared values point to their exact original whole parent/pointer, all137 role pairs match the source binding and every numerical argument/selector count is preserved. These are source/parameter text identity checks only. The actual Node CLI reproducer, Python AST, scientific solver, fixture, benchmark and physical-field computation were not run locally.

Root remains responsible for publication and a genuine public Actions execution. No reference, queue, running job or active scientific source was changed here. Complete run23 source and parameter preparation do not establish an actual policy reduction, speed improvement, convergence or continuous geometry claim.
