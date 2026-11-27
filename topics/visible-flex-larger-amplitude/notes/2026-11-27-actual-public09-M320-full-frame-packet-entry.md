# Actual run09: complete M160 → M320 analytic-frame/J3/packet entry

## Status and exact scope

This is a complete source and parameter delivery for the already returned run09 fixed target. It enlarges the **current free Fourier space** from M=160 to M=320. The original reference problem, full 160-word fixed material chart, exact scalar definition, supported smooth-triangle reference seed, N=2048 observer, J=923 radial nodes, outer eight-node Gauss rule and common 32-stage normal chain remain fixed.

The package does not supply an M320 field or an accepted direction. No F, J, root, quadrature, scientific array operation or numerical fixture was executed locally. Its 17 complete runtime files passed source-only AST/compile and complete reproduction before the executor was lost. After that loss, all 17 were reconstructed in memory from immutable complete source inputs, compared to their previously recorded whole SHA256 values and protected as remote unreferenced Git blobs. Every runtime byte is unchanged.

The four complete source-construction files in this delivery are a new reconstruction path. The earlier scratch-only Python construction programs are not claimed to have survived. The new JavaScript transformation itself was replayed in V8 and produced all 17 exact runtime outputs. Its filesystem CLI has not been executed in the unavailable executor. These facts are separate from the earlier actual AST/compile checks of the unchanged Python runtime files.

The existing mathematical scopes include the frequency inclusion in [R678](../results/R678-frequency-only-refinement-and-identical-parent-functional.md) and the fixed-target refinement framework in [R676](../results/R676-fixed-metric-refinement-and-complete-observation-transfer.md). The complete parent sources supply the independently registered reference-centred, analytic-frame and full implicit-chain definitions. This entry implements frequency inclusion in that actual family. It does not identify frequency expansion with N or radial-mesh refinement.

## 1. Returned target and actual parent sources

The complete actual target identity is:

`7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a`.

The whole actual input binding is:

`2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d`.

The original complete run09 reference model has identity:

`d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75`.

The complete original actual-input validator is `actual_public_reference_input_binding.py`, SHA256 `306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a`. The complete original current memory source remains `2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb`. Its whole public return, all six actual input files, complete reference model, scalar parameters, fixed chart and old/current carrier evidence remain required. No current-target identity is reconstructed from a boolean or from matching only three fixed core words.

The actual M160 parent family is the repaired complete driver `fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py`, SHA256 `ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5`, with whole pure reader `read_run09_public_reference_analytic_frame_so3_report_v2.py`, SHA256 `aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32`. The repaired geometry SHA is `e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13`.

The earlier e3cb attempt failed during setup because its geometry getter requested `all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained`, while the actual adjacent producer declares `all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained`. Its complete child log is 6387 bytes, SHA256 `33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de`. It produced no report or scientific field. This delivery uses the repaired actual family. It does not reinterpret the earlier failed setup as a completed physical parent.

The whole parameter parent is `run09-public-reference-analytic-frame-v2-complete-ready.json`, 93108 bytes, SHA256 `2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f`. A future terminal report or final checkpoint from those repaired sources is not supplied by this package.

## 2. Two frequency layouts are explicit

The fixed reference continues to use M0=160. Its context, parent problem, complete reference model, original core, frequencies and supported-seed provider remain the original objects. The current problem uses M=320.

The complete base exposes separate reference and current frequency data. Its current core and rotation arrays use the enlarged layout; `reference_freq` and the full original parent core continue to define the material chart. The normal operator's `_chart` uses `reference_freq`. This is the only mathematical method change needed in that normal source: it prevents a 320-mode current core layout from silently replacing the frozen 160-mode material chart.

The first three current core coefficients remain fixed by the original constraints. All other original free core coefficients remain free, and the additional 160 current core coefficients are also free. The entire original radial slot mask is retained. No variable is deleted or made ineffective by replacing the current field with a seed.

For J=923, the original radial mask contains 3J−3=2766 free slots. The x, y and z rotation channels have lengths M+1, M+1 and M respectively, so the total channel count is n=3M+2. Therefore:

| Quantity | Original current space | Enlarged current space |
|---|---:|---:|
| Current M | 160 | 320 |
| Rotation channels per free radial slot | 482 | 962 |
| Free core coordinates | 157 | 317 |
| Free radial slots | 2766 | 2766 |
| Height coordinates | 1 | 1 |
| Total free coordinates | 1,333,370 | 2,661,210 |

The unchanged observer still has N=2048 and 513 quarter-circle angles. This package neither doubles those angles nor changes the radial mesh.

## 3. Exact inclusion of every original free word

The complete layout source is `so3_frequency_refinement_layout.py`, SHA256 `ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27`. It checks the whole layout, mesh digest, original and current sizes, mask and source. Its Actions-only array inclusion copies the actual binary64 words and records the whole original/new point hashes, each rotation-block hash and the height words.

For each free radial slot the three original channel blocks are copied separately:

| Component | Basis | Original half-open channel range | Current half-open channel range |
|---|---|---|---|
| x | odd sine | [0,161) | [0,161) |
| y | odd cosine | [161,322) | [321,482) |
| z | even sine | [322,482) | [642,802) |

The added channels are zero at the inclusion point. They remain genuine free variables in the current solver. Copying the old 482-channel row into one current 482-channel prefix would incorrectly move the y and z coefficients; the implementation explicitly excludes that operation.

The original 157 free core words are copied to the first 157 current core slots; the added 160 current core modes start at zero. The actual old height word is copied to the last current coordinate. The new vector is a different-sized array and has its own shape-sensitive digest, even when its accurate Fourier series represents the included old function.

In accurate arithmetic, the three retained Fourier sums are identical term by term and all added terms vanish. The radial Hermite representation uses the same nodes and derivative slots, so the accurately represented angular velocity and its required radial/angular derivatives agree at the included point. The fixed chart, scalar metric and reference seed are unchanged.

The selected normal lift is an implicit construction. Exact inclusion of the underlying field requires the same compatible complete branch of all 32 stage equations. The source does not infer that branch equality, a root certificate or numerical bitwise equality merely from zero added modes. Ordinary matrix multiplication reductions, trigonometric evaluation, root tolerances and the enlarged current norm can produce different working words. All current fields, roots, Phi and geometry are reread.

## 4. Frozen reference points have an explicit inclusion relation

The source distinguishes three objects:

1. the original frozen M160 reference point;
2. its included M320 frozen reference point;
3. the optional included current point obtained from a genuinely returned parent final checkpoint.

The third object never replaces either of the first two.

The transfer's `_frozen_initial_points` reconstructs the entire original free reference vector from the complete fixed parent core, the original zero rotation coefficients and the fixed seed height. It applies the complete layout inclusion and compares the entire new vector to `base.initial()`. It retains both shape-sensitive point hashes and the full inclusion record.

The new fixed-Q input and reference-centering calibration bind the included M320 frozen point. Their definitions therefore have new canonical identities. The pure compatibility check is allowed to normalize those dependent identities only after the explicit complete point relation has passed. It does not pretend that a 1,333,370-component point hash equals a 2,661,210-component point hash.

The calibration source is independently complete. Its baseline verifies the original 160 core words, the zero added core modes, zero rotations and fixed height in the enlarged layout. Its fixed chart remains M160. All original current-closure lift terms remain in the six physical jets.

## 5. Whole model compatibility precedes history or checkpoint transfer

The new source binding validates the complete actual current model and all five complete frame/matrix working-policy definitions against their actual sources. It invokes the actual original public09 source binding to validate an original M160 parent.

The comparison uses the complete normalized objects. The only normalized differences are the declared current frequency layout, source/schema identities, explicitly verified frozen-point-dependent identities, and the complete already checked frame/matrix policy source identities. The fixed reference model, scalar/profile/chart, mesh, reference seed, fixed Q words, gamma support, common partition, control dimensions, radial observer and current input target remain equal.

The source accepts neither the earlier strict7c family under a new label nor another run merely because its first three core coefficients or mesh happen to agree. The original run09 input validator and the whole actual binding remain in the path.

The complete M320 current coordinate norm is rebuilt for all 2,661,210 free variables. An old norm identity, old gradient, old Gram matrix, cached old QP rows or old damping interpretation is not imported. The requested numeric solver parameters, including the chosen mu, are preserved as explicit new-current-coordinate parameters.

## 6. Complete history and typed discovery lineage

N, J and the radial observation carrier are unchanged here. The complete actual memory source and selector are reused byte for byte. The permanent nonlinear responsibility continues to include all P0 and the full old/current grid union. No old index is reinterpreted under a new N, because N remains 2048.

For each specified genuine terminal parent, the new transfer captures and hashes the whole report and runs the actual complete parent pure reader. It verifies the source family, full target and model relation. It recursively rereads the actual inherited input reports rather than relying on counts copied into the final report. Each complete prior preparation must retain the exact same frozen reference definition.

The original full address walker reads all applicable inherited reports. All three complete role arrays are checked as subsets of the resulting permanent memory. The full typed rows are retained without the near-active candidate cap: location, family, branch, witness sign, partner, ordinal, first-discovery source-point hash and the complete previous row remain in the new provenance. They are locations and typed obligations for the new field, not inherited physical values or feasibility claims.

The new pure reader rereads these same actual report sources and verifies the complete transfer record. Same-source restart preserves its own complete memory and prior annotations.

Run07 was observed via the API as completed/cancelled at 2026-11-27 05:02:15 UTC; that is an observation time. The API updated-at value was 05:00:28. The scientific child's termination time and cause are not known from those observations. No complete step4 physical report or typed state was returned. Unknown peer provenance remains an explicit obligation, and is never recorded as empty memory. The current finite envelope keeps all covered material locations; it does not fabricate missing discovery order or protected labels.

## 7. Full checkpoint inclusion

The final-point mode requires the same genuine complete parent report for both the memory and the checkpoint arguments. It passes the report and history checks first. The checkpoint must contain the exact original 13-member schema and match both actual final-point digests recorded by the original report.

The transfer checks the full original model, M160 and 482 rotation channels, whole radial mesh, complete fixed core, every structural zero, all core words, all three complete rotation blocks and the actual final height. It reconstructs the entire original free vector and applies the layout's three-block inclusion. It calls the current `q.unpack` and checks every resulting core/rotation/height word and every newly zero mode.

This operation does not run a root or claim a field value. The first M320 F/root/Phi/geometry evaluation occurs through the unchanged complete scientific program after the initial report and full point provenance have been recorded.

A successful original final, if it exists, is a possible starting point; it is not automatically discarded on a source change. The independent plan also remains a legitimate distinct source branch at the frozen original reference point. It does not pretend to have consumed an unreturned peer terminal state.

## 8. The complete scientific program is retained

The actual driver from `def save_report():` through EOF is byte-identical to the repaired parent. Its SHA256 is:

`d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`.

This retains the complete Phase I/common-slack process, all original positive and mean Gram rows, full geometry and amplitude prefix, appended envelope rows, true nonlinear scans, actual line search, original normal-root failure handling and both record-only immutable packet hooks. No current-control or multiplier-chain component is removed.

The five analytic frame/J3/cache numerical method bodies remain their complete original implementations under independent full source identities. The normal operator retains all complete stage solves, selected root records, angular derivative systems, active implicit upstream chains and the six physical jets. `_chart` is the explicitly necessary fixed-reference-frequency change.

The geometry is independently source bound. Its C1 guard names the actual new C1 source, not the inherited ba3d source. Its adjacent guard reads the actual selected-J3 policy key. This closes both concrete historical cross-file interface defects without inventing compatibility aliases.

All packets describe their own actual point, angle order and available 32-stage roots and matrices. Capturing a packet performs no F/J/root evaluation or derivative upgrade. No larger-space parent norm, physical value or error certificate is inferred from a packet.

## 9. Complete executable parameter modes

The three ready files copy every original numerical solver/observation option from the full 93108-byte parent. The added explicit option is `--current-modes 320`; `--angles 2048`, the common 32 stages, outer integration order 8, seed radial order 8, 1 metric direction with maxiter16 and 4 restoration directions with maxiter64 remain. No whole-field budget or constraint row is reduced.

Every plan retains all 333 original scientific scalar selectors and all 317 original pure selectors. It adds 11/6 actual M-layout scalars, for 344/323 in total. Every original output path pattern and row-cache cleanup pattern is retained under its independent new output directory. The pure reader always uses the existing original reference bundle as its controller parent, so an initial scientific failure remains readable without requiring a new final bundle.

| Plan | Complete scientific argv words | Pure argv words | Required new actual parent |
|---|---:|---:|---|
| independent | 151 | 7 | none; peer obligations declared |
| terminal | 140 | 7 | genuine complete ff544/aee22 terminal report |
| final | 144 | 7 | that same complete report and its whole final checkpoint |

All three full plan files are below 100000 bytes. Each entire two-step compact queue is below 95000 bytes. The terminal/final plans contain paths to the intended parent outputs, but intentionally have null actual parent report/final hashes until the files exist and the runtime validates them. They are complete conditional plans, not claims of a future result.

The new readout exposes `analytic_stage_jacobian.frequency_refinement` with the reference/current M, layout identity, actual input mode and current initial point. It separately exposes the whole fixed point relation. Missing field results remain missing; a valid initial source/model binding does not become a scientific success.

## 10. Source construction and recovery

The complete new construction path consists of:

- `public_reference_frequency_binding_additions.py`: full model and frozen-point compatibility functions;
- `public_reference_frequency_transfer_additions.py`: full recursive history, point reconstruction and 13-member checkpoint inclusion functions;
- `reproduce_public_reference_frequency_sources.mjs`: complete deterministic construction of all 17 runtime sources, exact input/output hashes, all 74 runtime role checks and optional stdlib-only AST/compile;
- `make_public_reference_frequency_ready.mjs`: complete deterministic construction of all three ready plans from the actual whole parent.

The source reproducer reads the immutable, already published angular-refined source bodies only as source-construction material. It produces the explicit N2048/M320 runtime family described above. No N4096 field or observer is loaded into the M320 runtime.

With the complete repository script directory and all four construction files present:

`node reproduce_public_reference_frequency_sources.mjs --source-directory SCRIPT_DIRECTORY --template-directory SCRIPT_DIRECTORY --output-directory OUTPUT_DIRECTORY --python-executable python3`

The optional Python invocation parses and compiles complete source text with the standard library. It imports no scientific runtime module. `--verify-existing` verifies previously written complete outputs instead of writing them.

The plan constructor is:

`node make_public_reference_frequency_ready.mjs --parent-ready PARENT_READY --generated-directory OUTPUT_DIRECTORY --construction-directory SCRIPT_DIRECTORY --output-directory READY_DIRECTORY`

It never selects a future returned parent. It produces all three complete modes and verifies complete source digests and scalar-selector retention.

The V8 replay performed after the environment loss verified all 17 whole runtime results, not only edited fragments. It also verifies the complete source-role table and unchanged scientific suffix as strings. The new filesystem CLI, optional new AST invocation and new plan CLI were not run after the loss; no such result is claimed. The earlier source-only 17-body reproduction and 74-role verification remain valid for the exact unchanged runtime bytes.

## 11. Limits and next interface

The delivery is a complete executable implementation, not a root or embedding certificate. It does not pay continuous inverse/root errors, exact whole-angle uniqueness, numerical norm-factorization errors, curvature/reach errors or whole-domain geometric conditions. More modes can change conditioning and cost; no measured acceleration or better convergence is asserted.

Radial refinement needs a separate source family with exact affine nodes, a true current/reference radial-grid split, exact provider queries and complete old/new radial address union. Merely evaluating old cell/u coordinates after rounding would not implement that contract. N refinement likewise has its own complete observer and history-index contract and is not silently combined here.

If M and N are later combined, both definitions must coexist in the complete model and pure compatibility checks. The fixed target and chart must remain bound to the same full actual reference; original addresses and typed lineage must be transported under both declared maps. This package makes neither combined-refinement nor radial-refinement claims.

## 12. Root完整复核与发布范围（2026-11-27 08:13 UTC）

root已从实际公开Git blob完整读取25件交付文件，逐一核其完整字节数/SHA；17运行体与74个role的全部源码身份都匹配。又以保留的四件完整构造源在V8中实际重放**仅文本构造**：17件运行体逐字等于交付；三份ready按构造器原声明顺序重放后，全部完整字节也分别等于36b54aec0cb6a9d9570c4f779a32a9aa32fdcd5f896922eae4e596e49653f654 / 40cd7b152f355f426727c1216b16f62dcfca0313a1336778c043719984a89e22 / 7ee87ba53e6f59b39b4ae498d7893078f0336a14e50dc879b30a0d8a143c6852。构造辅助对象的键顺序按实际CLI保留，不把值相同但序列化顺序不同冒充字节相同。

全部原333/317 selector、完整数值参数、outputs/cleanup及独立mode的全部未知来源责任逐项保留；三mode的science argv为151/140/144，pure各7。19574 B的完整科学后缀逐字等于实际修复父源，SHA为d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376。新增独立量是current M320；reference M160、N2048/J923/32段及全原问题均保。原父真实返回不存在时，terminal/final模式只保完整条件入口，不填写其未来SHA或结果。

本次新复核没有执行Python数值模块、数组包含、F/J/root、科学积分或fixture；没有声称失联后的文件CLI或新AST/compile已运行。此前17运行体的实际AST/compile/完整再生检查属于失联前记录；这里通过逐字同一性保留该事实。新四件云端构造路径是新完整源，不冒充恢复了丢失的八件旧scratch Python构造器。

本次刊全25文件（其中3件通用完整源已存在且字节相同）及本说明；三种方案均未加入当前队列，未作M320科学返回声明。当前09的science/pure/全实际mean批费原队列完整不改。下一真实准入必须消费已经返回且可核的父；或采用明确独立参考分支，保全其未知并行来源义务。精化实际通过、整面连续度量/曲率/法向管和最终闭面交付仍欠。

当前公开main读取点为 `d990f197a7d196e1400d7cbf997a4cf2c36b7ee8`，双README完整SHA仍为581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 / 3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d；这是云端只读核查，不称git pull。执行环境恢复后立即真部分克隆/pull；Actions已存在的实际pull及失联前本机pull全保HANDOFF与第31轮说明。
