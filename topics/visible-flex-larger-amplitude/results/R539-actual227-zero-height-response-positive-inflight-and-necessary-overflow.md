# R539：actual227 的零高响应、正高在途预算停止与完整必要读回超限

作者：ChatGPT（AI）；日期：2026-11-16 UTC。

**可信度：已证明（限本文完整返回的官方运行元数据、两份各一次读取的终态日志、原事件及冻结来源合同）；本次没有返回新的正高 native 接受、完整 physical full-DN、FD 或闭面证书。** 本文不重跑科学，不把单份超限摘要的身份当作已读正文，不把并行源已生成当作每个 worker 的科学进度。

本次 request227 真实执行 R531 的两个 cellflow worker 和 R538 的独立入口。零高原调用实际返回 `converged=true,residual=0`，外层计时 `182.227128751` 秒；其后 `s=0.015625` 的第二次调用只有在途事件返回。原总科学钟 18000 秒实际耗尽，wrapper 返回 124，科学 child 返回 -15，owned group 终态安静。必要 reader 尝试的完整正文是 **211682 B**，超过原 90000 B 限制，返回 70；唯一返回的必要 frame 只有 **1494 B**，明确 `summary_complete=false` 和 `transport_complete=false`。报告 job 成功转发该不完整 frame，未将其升级为科学成功。清理真实 `removed=false`，其直接断点是完整读回 marker 不存在。

## 1. 真正的运行、来源和唯一阅读范围

官方 [run 43860144962](https://github.com/Rogerhu12/math-research-public/actions/runs/43860144962) 是 `workflow_dispatch`、attempt 1、main，实际 source/head 都是 `5b5dd03b0d69c8a059282b963b7192679fd43f67`。workflow id 为 `420058779`，文件为 `.github/workflows/visible-larger-public-complete576-parallel-cellflow-full112.yml`。官方 `created_at` 与 `run_started_at` 都是 **11:42:44Z**，`updated_at` 是 **16:44:10Z**；终态 `completed/failure`。本次以官方字段为准，不把先前行政 POST 的客户端接收时刻当作科学起点。

| 对象 | 实际身份 | 终态与范围 |
| --- | --- | --- |
| compute job | [133274517805](https://github.com/Rogerhu12/math-research-public/actions/runs/43860144962/job/133274517805) | failure；科学步骤 12 返回 124，必要读回步骤 13 返回 70 |
| report job | [133451649161](https://github.com/Rogerhu12/math-research-public/actions/runs/43860144962/job/133451649161) | success；逐字输出那一份 1494 B 不完整必要 frame |
| 外层 request227 | `public-complete576-parallel-cellflow-full112-request.json` | 19994 B / `56c985a5513e9c403fb9a31f03e1a5982267684293e4b925c181d1f8d5246504` |
| 不变的内部 request224 | `public-six-control-input-support-contracted-trace-r273-request.json` | 88551 B / `6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980` |
| 内部原配方 | `actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json` | 21539 B / `0c9fa04642835dd37f9da5aeb03a35abae4be4e75283c3e2203a73dcec6544ea` |
| 实际 workflow | 上述 yml | 53746 B / `3305b7ec7fb77437e16d9bfb5d5993afaaa7eb6ad32370bb372fbeb6df822609` |
| 实际并行来源计划 | `r531-complete576-parallel-cellflow-source-plan.json` | 63026 B / `499616558f05865726aefa63c10842fa1a8a73172da557a18dbf7b8d574e61b7` |

16:45:15 UTC 的官方 jobs 元数据确认上述终态后，指定读者各取两 job 日志一次，随后只分段读取自身缓存，直到两份全文都已读完。没有取运行中日志，也没有为本文再请求任一日志。连接器返回的是解码后的日志文本；对该文本重新 UTF-8 编码所得身份如下，**不冒称 HTTP 原始压缩响应字节**：

| 连接器解码文本 | UTF-8 字节 | SHA-256 |
| --- | ---: | --- |
| compute 全文 | 208291 | `df0acdc1fb2341a845f29a86cb17239d074e6edd630d091bae8a6feaf6fce97e` |
| report 全文 | 9833 | `f7f1784b5767469466e5c0ba33e92fdfef591530a7951a6c0f4917fe2c9b0a5a` |

compute 日志内大量文字是 runner 打印的 shell/Python 源码。本文严格把这种源码回显、实际 JSON 事件和实际必要 frame 分开：回显的成功分支不证明该分支运行；source pin 表不是科学数组；本次没有将原日志、未返正文或临时科学文件放入 Git、artifact 或 release。这里只提交作者整理的完整结论与来源。

冻结合同参见 [R531 源与条件等价](R531-complete-current576-parallel-cellflow-source-and-conditional-equivalence.md)、[R531 完整接口](../notes/2026-11-16-complete576-parallel-cellflow-source-interface.md) 和 [R538 request227 实际编排](R538-request227-complete576-parallel-full112-executable-composition.md)。本次不修改这些来源，也不以本文补写它们的运行结果。

## 2. 实际源生成、路径和输入绑定

### 2.1 两层同 job 来源

原 request224 在本次实际 run 中作为字节不变的子合同使用；namespace `visible-original64-input-support-contracted-trace224` 和若干 `request224_*` event 名是该 producer 的历史身份，实际 `GITHUB_RUN_ID/GITHUB_SHA` 始终是本次 227 的真实值。不能把这些名字当成旧 224 job 的输出复用。

11:43:33.2011100Z 的 `request224_actual_private_source_views` 记录原层已生成，实际 receipt 是：

- `runtime-source-views/source-views.json`：106734 B / `ce469699683974d6ab0a841693376dfee40549b82294d44bb6197c643842ea52`；
- 原 public 150 件、generated 31 件、原层并集 181；
- 公共仓库路径保持原 `GITHUB_WORKSPACE`，实际执行源码在 `$RUNNER_TEMP/visible-original64-input-support-contracted-trace224/runtime-source-views/computations`；
- 原 request 与 recipe 被逐字复制到该实际 `HERE`，没有以旧身份标记新内容；
- 旧 210/211 生成文件按原完整 literal 计划重建，未冒充公共 Git 文件；它们的历史身份与当前实际入口分开；
- 原层生成声明 `scientific_code_executed_during_generation=false`，此声明只涵盖 source preparation。

11:43:33.4418091Z 的 R531 实际来源 receipt 为 `parallel-source-views/source-views.json`，11840 B / `bd5d468c8721a1f9fe2793940cb6e6443b841986124e35b95296b0e2e0cd5d47`。原八个 baseline 的实际字节被读取，四个新的公共 helper 被绑定，八个当前派生入口生成在同一真实 computations 目录。11:43:33.4474778Z 的 R538 entry binding 与 11:43:34.4416365Z 的 `request227_actual_parallel_source_identity` 明确绑定总并集 **193 = 181 + 4 + 8**。这些是本次真实生成/读取事件；计数不构成任意动态 import 的普遍完整性定理。

四个公共执行源仍为 R531 的原字节：

| 来源 | 字节 | SHA-256 |
| --- | ---: | --- |
| `geometry_20261116_complete576_parallel_cellflow.mjs` | 21284 | `9434c8f003b19745446fbc798f12efc464719474bad3385553cff3368be225aa` |
| `geometry_20261116_complete576_cellflow_pool.mjs` | 29074 | `ab6dff37f021cee82ace600ebc1e48ce32285f41a7a1f18b6f891aecff86369c` |
| `root_20261116_parallel_cellflow_necessary.py` | 20373 | `da99e600bbfb4fd557890dae335c59135a00f2ad179b8050b9f5018cf0080c95` |
| `root_20261116_parallel_cellflow_source_views.py` | 10495 | `b628d09aa75b0f3942549a2f9f24b4fa5cd618766c82b76adb565a64254e9149` |

八个实际派生来源在原 source receipt、launch 和 cleanup 事件中都保持同一身份：

| 实际文件 | 字节 | SHA-256 |
| --- | ---: | --- |
| `exact_20261116_parallel_input_support_contracted_trace_r273_current576_system.py` | 29888 | `1b51c672277ab1e0919bb00392bfc2634e36e7e64caa58b43d62d6781ca3385a` |
| `exact_20261116_parallel_input_support_contracted_trace_r273_current576_chain_qr.py` | 22153 | `9b20fab094c12c471f8c61a968a0dde0249ee1a1e71c30cdd2bb88a46bfc1b42` |
| `geometry_20261116_parallel_input_support_contracted_trace_r273_tail_client_hook.mjs` | 60059 | `6911a4b3224dc5b726d435f3b44e4127c05e8d8a15f6cdaccaf8872c932234ba` |
| `geometry_20261116_parallel_input_support_contracted_trace_r273_tail_client.py` | 23870 | `a8571e0c47c8f2e264c76ce3ee1554ca19cbcaa0366fbc6b7fdc2fe71e9856b2` |
| `geometry_20261116_parallel_input_support_contracted_trace_r273_height_path.py` | 24104 | `2c92d191b8cedecf235176209cc6eb7d432622d0f8f416bfe4572c1c12584a3b` |
| `geometry_20261116_six_control_parallel_input_support_contracted_trace_r273_full112.py` | 52339 | `525be2072fee4f53122d5802ef57d8b00f24e7b08408a3ed0441fd1872686311` |
| `root_20261116_parallel_input_support_contracted_trace_r273_run.py` | 15716 | `4c7e13df26c39ab881ac878429150b79e7536e55908d3ae69d097bba3c4afe19` |
| `root_20261116_six_control_parallel_input_support_contracted_trace_r273_scalar_readout.py` | 50519 | `fb8899e0da24ff8b6b7d5e728b3906c5096f57e0e93c0e511bfc506ddd32ea96` |

所有 `actual_literal_counts` 随原 source receipt 返回；每个新输出的 `existed_identically_before_prepare=false`。这证明本 job 真正创建了这些指定源视图，不能据此补写各 cellflow、各 engine 的 completed 数量。

11:43:34.4838744Z 的 workflow source-syntax 事件记录在 Actions 内检查了实际 workflow 的 10 个 bash、9 个 inline Python 块。本文作者没有在本地 import、AST、编译或执行这些科学模块。

### 2.2 原输入没有改为小模式或旧失败状态

11:43:38.7188878Z 的输入恢复事件绑定固定历史 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 下的四个数学输入与两个 native geometry 输入：

| 题内原路径 | 字节 | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz` | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` | `6a9dfda743c464af6ae1190208e7157fa66df30f` |
| `notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz` | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` | `d3aadef529d767c8facc26c399f458e903014512` |
| `notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz` | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` | `5b7093c4f088c738e1d074fcea851f631782ee31` |
| `notes/public-actions-43588155190-1-prepare112/T112-config.json` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` | `543d8364593985305438dda6a0c89b4b1a9c7ec5` |
| `notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` |
| `notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` | `b6c44fe237750f13c8b10366f15525b481a74e09` |

这些原件只在 Actions 恢复并读取；本文没有通过工具重新下载其大数组正文。两个 ready 输入保持原完整 provenance，不以来源计数代替几何真值。原事件的 `initialCheckpoint_present=false`、`failed91_95_103_checkpoint_not_consumed=true`、`original_config_not_rewritten=true`、`old_zero_J_is_only_initial_guess_data=true`、`rearchive_inputs=false` 全部保留。原 78 文件 source restore 的步骤也实际 success；它是上述 193 源之外的既有真实公共 source-root 恢复责任，不从并集数字省略。

原配方实际给出六词
`[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]`，
目标 `lambda=0.001`。原三 active p、三冻结 shape、112 物理模式、224 shape 列、226 状态含双 mean、576 个原 cell 均保留。没有加 low-three-root 前门，也没有把旧 native anchor 当成当前 native 解。

本次实际 launcher argv 仍明确 `jac-workers=2,max-nodes=1200,material-angles=4096,physical-angles=4096,node-heap=6144,outer-iterations=8`。R538 配方继续保原 32×10 迭代策略、`2e-9`、原 prefix/boundary/FD/full-DN 门和 height path；它们是本次原合同，本文没有为本次停止补设或放宽阈值。

## 3. 两个并行 worker 的实际范围

实际 env 是 `VISIBLE_R531_ACTUAL_REQUEST=227`、`VISIBLE_R531_CELLFLOW_WORKERS=2`、`VISIBLE_R531_CELLFLOW_WORKER_HEAP_MB=3072`。source binding 和 launch 明确：

1. 每个 worker 使用同一次实际 H、状态、target scales 和完整 profile 字值；profile 的原完整调用顺序被保留。
2. 原 engine 分配是 `engine_index % worker_count`；成功结果按原 n 顺序归并，完整 576 个 cell、每个 226×224 tangent、两 mean 及原 residual/max 组织不缩减。
3. 原 main Node heap 6144 MiB 不变；每 worker 的 3072 MiB 是 old-generation 限额。两个 worker 合计 6144 MiB **不是**全部进程 RSS、ArrayBuffer 或整个运行内存的上界。
4. 原 noJ 请求仍保求解初始化、当前迭代及 predictor 所需的内部完整 tangent，不能把请求不索回 J 当成内部不算 J。
5. 原 18000 秒总钟不按 worker、height 或 iteration 重启；额外 worker 的资源停止边界不承诺和串行相同。
6. 原 R523 的实际有限 A/T 支撑路径、14 个计数、全部 last observation/scope，以及 R471 和 R466 的原责任都保留。统计必须来自实际被执行的 engine，不能由两个 worker 的配置反推。
7. 原十 trial body、线搜索、全列末门、height path、FD 和最终物理 audit 合同未改；旧 stdin 协议 worker 没有被当成线程模块 import。

这些是实际绑定并进入 launcher 的来源合同。**本次完整必要正文没有返回**，因此每个 worker 的 attempted/completed/partial/unvisited 地址、每个 engine 的完整统计、正高 current J 进度并未由必要 frame 支付。不能用源文件存在或 job step 名称替代这些未返字段。

## 4. 唯一实际返回的零高科学响应

11:44:19.4956221Z 的 `request224_height_path_request_started` 是 native call 1：

| 字段 | 原值 |
| --- | --- |
| request_index / native_call | 1 / 1 |
| proposed_s / previous_converged_s / proposed_increment | 0.0 / null / 0.0 |
| H 形状 / dtype / order | [112] / `<f8` / C |
| H 字节 / SHA-256 | 896 / `d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5` |
| negative_zero_columns | [] |
| requested_jacobian / requested_audit | false / false |
| exact_H_star_copy / zero_request | false / true |
| original_client_calls_before | 0 |
| remaining_wall_clock_seconds | 17979.775758082 |
| 起始 response_observed / accepted / original_full_DN_accepted | false / false / false |

11:47:21.7389172Z 的 returned 事件确认该调用实际完成。它的 `phase=original-native-converged`、`accepted=true`、`response_observed=true`、`original_client_calls_after=1`。这里的 accepted 仅是原 height path 对这次 native response 的接受，原字段 `original_full_DN_accepted=false` 没有改变。

原 response 完整返回的科学范围为：

- `converged=true,residual=0,actual_nonlinear_solve=true,finite_tail_only=true`；
- `checkpoint_present=true,history_count=1`；
- `full_J_present=false,full_J_identity=null,full_J_scalar_count=null`；
- `audit_present=false`；
- `meanSlope=0.08000000000000027`、`meanSecond=-1.866666666666673`、两个 mean correction 都为 0；
- `original_request_seconds=182.227128751`；
- `original_client_all_requested_jet_J_and_residual_checks_passed=true`，其中 “requested J” 是本次 `jacobian=false` 的实际请求范围，不能改称完整 J 返回或最终 audit 通过。

原 checkpoint scope 明确是有限 Fourier/depth shooting 状态；far Robin 条件不是准确旋转 collar，未 audit 的 response 不是最终几何 audit。原 checkpoint 的 height JSON 身份是 225 B / `64c19f2662ac257bca17a036d0c4809671b09bf950df1d6c82b42461fabe7e56`，并明确 `checkpoint_JSON_preserves_pre_serialization_negative_zero_claimed=false`。原 H packet 的负零列是单独原字段，不能把它和 JSON 身份混同。

本次保存但未在必要 frame 展开的大对象身份为：

| 对象 | 字节 | SHA-256 |
| --- | ---: | --- |
| `full-DN/true-tail_0001.json.gz` | 10238 | `c132fa0bb99fe0c27cfed260c70935d354d92704da411ac8d05bd73efc5ab85d` |
| `height-path/request-001-trace.jsonl` | 1400 | `603b53fc3e1a5cdd1d1c3245eac56ae3872d5516ba81bdc2fbac73bc4b6b0f41` |
| 原 source 对象 canonical JSON | 16623 | `19977370b5df3e642ec6a193ee7422fc340d36d68d8307eb2906a523bd30a317` |
| 原 config 对象 canonical JSON | 1565 | `a7d9096523113dcba65abde5282bde09ab7b5c375f1ca27505a0632dec00b923` |

这里确实返回了该调用的全部六条 trace 事件、零条 trial 与 `original_trial_slice=null`；不是通过另取 raw 获得：

| 原 trace 时间 UTC | 事件 | 原返回内容 |
| --- | --- | --- |
| 11:44:19.496 | request | call 1，jacobian=false，audit=false |
| 11:44:19.501 | original_r273_current576_request_context | request.json 3405 B / `8137d77d2abebc417dfa8f1923c35f8812b848eb145aa9bb6c63fd94530e0d6b`；cold initialization、live predictor、fallback 保留；worker_last_not_assigned=true，seed_assigned=false |
| 11:44:19.521 | compact_storage_gc_before_solve | 真实同 call 的 GC 前后字段，详下表 |
| 11:47:15.357 | iteration | iteration=0，elapsed_ms=175861，norm=0，minA=1，minD=1 |
| 11:47:21.710 | tangent_predictor_ready | maxChartCondition=385639393697279100000 |
| 11:47:21.713 | response | elapsed_ms=182216，converged=true，residual=0，maxChartCondition=0 |

| GC 字段 | before | after |
| --- | ---: | ---: |
| rss | 588046336 | 587800576 |
| heapTotal | 116187136 | 105439232 |
| heapUsed | 109387976 | 79843504 |
| external | 258212725 | 258212725 |
| arrayBuffers | 255829746 | 254203921 |

原 `existing_failure_context` 在本次成功零高 response 后仍按其来源返回：iteration count 1、trial count 0、warm events []、located trial failures []、`cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source=false`；原 outer failure 不提供 stage radius/angle/D/S/A 的标志为 true；原 target fill 没有 DSA throw 的来源限定为 true。它还明确 `only_original_core_correction_call_replaced=true`、`separate_finite_trace_tangent_and_noJ_matched_withJ_flow=true`、原 root primal 算术/决策保留、原 local implicit product J 已由该独立 finite-trace 接口替换、observer 不改原 trial 决策、`original_evaluate_and_ten_trial_bodies_retained=false`、`actual_R531_withJ_stage_dispatch_and_original_n_reduction=true`、`original_ten_trial_body_retained=true`、`floating_point_cause_or_global_resolution_limit_claimed=false`。这些字段的真假有各自源级范围，不把历史名字解释成新增数学结论。

本次 182.227128751 秒是同一原 response 的真实外层计时。它不提供 root/dFlux/linear/IPC/worker 的分项时间，也没有在本文安排独立 benchmark。因此不能由它断言某个 helper 的确定加速倍数、并行效率或正高成本保证。

## 5. 第二次正高调用与原总钟的实际停止

11:47:21.7401752Z 返回了 native call 2 的 started 事件，原值全部如下：

| 字段 | 原值 |
| --- | --- |
| request_index / native_call / phase | 2 / 2 / request-in-flight |
| proposed_s / previous_converged_s / proposed_increment | 0.015625 / 0.0 / 0.015625 |
| H 形状 / dtype / order / 字节 | [112] / `<f8` / C / 896 |
| H SHA-256 | `fb6da818e40bcdaa0bc57ceb9a86d5ae2845132054389a2eac73ea866283a032` |
| negative_zero_columns | [] |
| requested_jacobian / requested_audit | false / false |
| exact_H_star_copy / zero_request | false / false |
| original_client_calls_before | 1 |
| remaining_wall_clock_seconds | 17797.533166877998 |
| accepted / response_observed / original_full_DN_accepted | false / false / false |

在两份实际返回日志中，没有第二次 `request224_height_path_request_returned`。这里的 started 行标志是当时状态；本文不把它当成整个未返 summary 的终态统计。本次没有取回正高 residual、各 iteration/J 次数、trial 表、每 worker 最后 cell、当前 max/min 或某个数值 exception。没有证据把第二次在途调用归因为 D/S/A 失败、NaN、源错、内存越界、线搜索拒绝或特定 worker。

16:43:59.7641074Z 的实际 process-return 事件为：

| 字段 | 原值 |
| --- | --- |
| phase | wall-clock-budget-partial |
| returncode | 124 |
| budget_exhausted | true |
| external_signal | null |
| process_status_sha256 | `cf13278b6a702edea020ea61c456be507a3014189bb28ac0063f0f8647358309` |
| scientific_acceptance_not_inferred_from_process_status | true |

1494 B frame 进一步真实返回 `scientific_wall_clock_seconds=18000`、`scientific_child_returncode=-15`、`wrapper_returncode=124`、`elapsed_seconds=18000.49249517`、`owned_group_quiescent_after_return=true`。科学 shell 随后明确 exit 124。这里是已有原科学钟耗尽的资源停止，不能改称完整原数学门失败，也不能用 124 普遍替代所有 run 的原因。

## 6. 原规则同步与两种 quiet 责任

本次 rules runner 仍为 `root_20261114_current576_rules_runner.py`，完整 SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`。11:43:56.5443215Z 的实际 baseline 更新只采用 request 中已读 README blob：

- 原 embedded 根 README：`6183b7f3eaa5edf22cd1a62fa19d84bf4ab3ba09`；
- 本次 reviewed 根 README：`21bd547f56590b7f2dd279d0297efb289a9b2783`；
- 题 README 两者同为 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；
- 原 period 为 2700 秒，pull/rebase 和规则变化停止策略保留。

完整返回的七次实际规则同步为：

| round | 事件 UTC | origin_main_read | published_commit |
| --- | --- | --- | --- |
| 0 | 2026-11-16T11:43:59.1089215Z | `dc326ad44f71296d4a069648030c25f4256ceabf` | `82bab15dbf13f167cd1347cddf68b689ecc24403` |
| 1 | 2026-11-16T12:29:02.3351277Z | `ef81c2183582bb82f6cf50c8fdbaa71df306a082` | `cf83d456d8a828b405190f73bb28e0f871e8ecc0` |
| 2 | 2026-11-16T13:14:05.6055189Z | `0482c61d2596a709b7aed3e08de698df66b4d603` | `7923ab9aacaae8546076bb8cb7f4c7aca4b22eb0` |
| 3 | 2026-11-16T13:59:08.7715042Z | `17669b1625319a40acb8e975f75eaf4b48b6f115` | `1379b70d249e362bce236054a1d0e8e41882593a` |
| 4 | 2026-11-16T14:44:12.2350537Z | `a04e5a75a147fdfe273542b2126003001c62ae93` | `e91273b47f9cd67d35c3de42492b5d16f6bb45a8` |
| 5 | 2026-11-16T15:29:18.3922972Z | `e44fbd47df917146e34067eb23a1c3554222e27b` | `91ee821ba34a537876a8dc2c1cb14f0774619b3e` |
| 6 | 2026-11-16T16:14:21.5579839Z | `dc66f663eaff7bffdb7213801832ffe3f4f99594` | `ee167dd15da660a4d59d0e65e5caf687ea3e9ad8` |

上述运行中行政同步不是更换当前科学 source head，也没有重启原科学钟。本文不从这些 commit 的存在外推其他 run 的成功。

16:44:01.0272809Z 的 rules-parent 必要事件完整返回：`quiescent=true,no_process_signalled=true,shared_runner_PGID_not_required_empty=true`；原 parent receipt 是 `rules-parent-owner.json` 2507 B / `b84eb517ae434b5fd2a4a6332d5083d2e5aa93700b34960d8c7181cf8f6d705f`。原 parent 的 `pid=3293,start_ticks=10711,pgid=2143,sid=2143`，实际 `current_PID_observation=null`、`same_recorded_process_still_present=false`、`wrapper_return_observed=true`、returncode 124。原 receipt 的实际 started/finally Unix 秒分别是 `1794829436.5438907` 与 `1794847439.7713718`。

因此，已返回的 scope 分别证明科学 wrapper 的 owned group 终态安静和原 rules parent 的精确 PID/startticks 对象已不在。共享 runner PGID 不要求为空，不对不属于本次的进程发信号。不能把这两条 quiet 真值再外推成缺失完整读回 marker 已存在。

## 7. 必要正文超限与实际返回的全部 fallback 范围

compute 的唯一 frame 是 `BEGIN_R531_PARALLEL_COMPLETE576_NECESSARY_SUMMARY` 到相应 END，实际打印时刻 16:44:00.8823528Z–16:44:00.8837795Z。report 逐字转发同一个 body。作者仅对这两份已缓存文本作 frame 提取与 UTF-8 哈希，二者 **逐字相同**：

| 对象 | 字节（不含最终 LF） | SHA-256 | 实际可读性 |
| --- | ---: | --- | --- |
| 全必要投影 | 211682 | `d7dc116ca43fc0a6f121939db00eae3ebb756ee3cc1060d5f43aea65eafe8fa2` | 只有身份返回，完整正文未返 |
| 唯一 fallback frame | 1494 | `825c1edaea948489859fc9692ddb1669ac51d4fc42ec6e0ac0a9fcc682fccb7b` | compute/report 全文返回且逐字相同 |

其 schema 是 `R531-original64-parallel-complete576-necessary-readback-v1`；保留 source_request_ancestor 224、actual_request 字符串 "227"、本 run/head、actual reader、immutable224 request 与 recipe 的完整 SHA。身份事件明确 `hash_includes_final_LF=false`。

除此之外，fallback 的全部字段是：

- `summary_complete=false,transport_complete=false`；
- 原 reason 是单份必要 summary 超过 90000 B，不允许 splitting/reassembly；
- `over_limit_projection_identity` 是上表 211682 B 身份；
- `original_acceptance_not_reclassified=true,raw_retained_until_runner_destruction=true`；
- process 整个对象是 §5 已列的 phase、18000 秒、-15/124、18000.49249517、budget true、external null、quiet true；
- adapter schema 为 `R531-six-control-parallel-cellflow-three-active-nonzero112-physical-DN-v1`，phase 为 `original-same-worker-height-path`；
- adapter `success=false,new_coupled_finite_acceptance=false,full_Cartesian_closed_surface=false`；
- adapter `prepared_sha256=74e0f6e3e75a72a205cbbac84fd7dc7fb503fe749ceee663f78c8d1084de4f1f`、`initial_collocation_max=6.8749454041621035e-06`；
- `no_partial_trial_table_claimed_complete=true`。

最后这个 prepared 身份是本次 adapter 所报告的当前准备结果，不是 §2 恢复的 4220043 B 历史输入身份，二者不混同。`initial_collocation_max` 不是正高 current J 或末端 native 残差。本次没有该当前 prepared payload 的正文，不能只凭其 SHA 移植别次准备状态。

reader shell 16:44:01.0314636Z 明确 exit 70。原 90000 B 限制保持，没有分片、对象/数字编码或删必要值凑返回。1494 B frame 的完整返回只证明这个 fallback 本身完整，不证明原必要范围完整。当前未付部分包括：

1. 原完整 height-path/positive trial 表、第二次响应或异常的详细实际范围；
2. 每 worker/每 engine 的 actual attempted/completed/partial/unvisited 及全部 last observation；
3. 14 个 R523 计数、root/finite-trace/zero-flux/收缩计数的实际本次全对象；
4. 本次正高 current residual/J、stage radius/angle/D/S/A、完整 native checkpoint 和 full338×112/两 mean 响应；
5. 原完整 FD、full-DN、尾 audit、闭面及连续几何证据。

这张清单说明尚未读回的责任，不断言这些内部对象一定已生成，也不从未返回断言它们一定未执行。原一阶资源停止是真实可读结论；它不能替这些未返科学字段作任何真假判定。

## 8. 清理的真正分支和 report 的用途

compute 官方 step 14 显示 success，但该步骤是 conditional cleanup reporter；其真正事件在 16:44:01.1986817Z：

- schema `request227-complete-parallel-conditional-owned-cleanup-v1`；
- actual_request 227、immutable ancestor224、外层 request SHA、actual parallel reader 与八源 binding 都匹配上述来源；
- 原/新增 source generation outcome 都是 success，scalar_step_outcome 是 failure；
- `removed=false`；
- `error="FileNotFoundError(2, 'No such file or directory')"`；
- 完整 traceback 的直接失败位置是 inline cleanup 第 37 行的 `read_bytes`，缺失文件为 `/home/runner/work/_temp/visible-original64-input-support-contracted-trace224/scalar-readout/readback-complete.json`；
- 原 reason 是 cleanup evidence incomplete，no active or unread payload is removed；
- `cleanup_is_not_an_original_scientific_acceptance_gate=true`、`no_artifact_release_or_git_raw_upload=true`。

源码回显中虽存在 `shutil.rmtree` 成功分支，实际没有走到；不能用步骤 success 写成已删除。quiet 已有真实独立观测，但完整 summary/marker 未付，所以临时 raw 保留到该 runner 生命周期终止。本文没有接着获取或保存这些未读 raw，也不声称观察到宿主最终销毁的时间。

report 的 16:44:08.4044253Z 身份事件明确 compute_result=failure、scalar_readback_outcome=failure、parallel_source_generation_outcome=success，并绑定实际 outer request SHA。其 `necessary_original_scalar_selection_only=true`、`complete_dyadic_witnesses_root_tapes_and_large_stdout_not_exported=true`、`large_array_payload_not_independently_recomputed=true`、`no_large_encoded_chunks_or_semantic_reassembly_protocol=true`、`no_raw_retention=true` 是报告传输的范围。它没有从 runner 取回原 211682 B 全文，也没有重新求原大数组。report 的 success 仅表示该唯一有界报告步骤完成。

## 9. 结论与后续使用边界

本次真正新增的可用事实是：同 run 的两层源和真实 193 源并集已生成/绑定；两个真实 cellflow worker 的当前入口已启动；零 H 原 native 响应真实 converged，iteration0 为 0 且 tangent predictor 已准备；下一正高 1/64 调用已实际发出；原总科学钟终止了仍在原 height-path 阶段的计算；两种已选 quiet 观测真实返回；完整必要正文超限并未返；清理没有删除未读 payload。

本次不能宣称正高收敛、当前全 J 或原 FD/full-DN 接受，也不能以程序并行配置推 stage 完成率。零高无外返 J/audit 的成功有其原请求范围；本文保留它，不删去真实进展，也不扩大其含义。后继若改读回表示，应针对这次实际完整必要范围的语义重复保全部已有选定值与未知/未访边界，不能以这个未返 211682 B 对象充当已读 fixture。后继若改计算，需新真实来源、输入/钟/门绑定，不追改本次已冻结 run。

本文只登记 actual227 的上述完整已返事实。R531 的条件等价、R538 的可执行来源及 R523/R471/R466 的限定算术责任仍各按其原文；本次没有补成它们未证明的完整舍入误差界或连续几何证书。
