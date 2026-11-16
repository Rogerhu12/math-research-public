# R525 — actual224：零高完整响应、正高一次原试步接受、原总钟停止与必要读回超限

作者：ChatGPT / amplitude（AI）。日期：2026-11-16 UTC。

**可信度：已证明（限已返回的官方元数据、两份终态日志内实际必要体、独立原事件及冻结源码的控制流结论）；未返回的 107463 字节必要正文未读，完整正高求解、末端 FD/full-DN 与几何接受均未完成或未获返回证据。** 本文是 actual224 的实际读回结论，不是新实验或数值计算。

本次新事实是：原零高请求真实返回 converged=true / residual=0，完整请求用时 **328.594023019 秒**；第一份正高请求 $s=1/64$ 的 iteration 0 已完成当前切向快照及原线性方向，并在原 trial 0、step 1 接受一次更新，残差读数从 **196395.0911309943** 到 **5181.565456345417**。这次内部 Newton 接受没有成为该高度的完整接受。随后实际原有限切向调用抛出 `finite-trace-direction-resource-budget`，原 18000 秒作业总钟停止；最后完整接受高度仍为 $s=0$。

必要摘要另有独立断点：原 reader 实际选出的正文为 **107463 B / 053ab840e3330c3345c0489b15c14e7bccd05759ede9c7989276d62358cf9e13**，超过原 90000 B 上限，故返回 70。compute 与 report 实际打印的是同一份 **1505 B / 3a911640573757772216834025102ecb3e818d72246c6ed00fdeb5e11f4c3ccc** 超限说明，summary_complete=false、transport_complete=false。以下正高进展来自另行真实打印的原事件，不是从超限正文摘要或 SHA 推复原文。

## 1. 官方运行身份与一次终态读取

正式 R524 入口发布头为 `498c03a7753a6f6caf66b563b2319cd42a447aaf`。actual224 实际运行头为 `23176ac678ea92882fa38ec6ddcc09e98742ac89`；原[官方绑定](../notes/2026-11-16-request224-official-run-binding.md)已分别说明后者是前者直接子提交且本题 subtree、整个 .github 与根 README 均相同。这里始终用实际运行头绑定，不把发布头当实际 GITHUB_SHA。

| 字段 | 实际返回值 |
| --- | --- |
| repository | Rogerhu12/math-research-public |
| workflow | .github/workflows/visible-larger-public-six-control-input-support-contracted-trace-r273.yml |
| workflow ID | 420005321 |
| run / attempt | 43851068999 / 1 |
| event / branch | workflow_dispatch / main |
| created / started | 2026-11-16T10:41:14Z |
| updated | 2026-11-16T15:42:21Z |
| compute job | 133243448382 — completed / failure |
| report job | 133411010593 — completed / success |
| actual source | 23176ac678ea92882fa38ec6ddcc09e98742ac89 |

官方来源：[run](https://github.com/Rogerhu12/math-research-public/actions/runs/43851068999)、[compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43851068999/job/133243448382)、[report](https://github.com/Rogerhu12/math-research-public/actions/runs/43851068999/job/133411010593)。15:42:24 UTC 的自然 jobs 轮询确认两个 job 已终态后，本结论唯一读者各取一次原日志；没有取本 run 的运行中日志，没有再次取终态日志。

连接器返回的是**解码文本**。本文记录的以下身份是返回文本 UTF-8 重编码身份，不声称为 GitHub HTTP 原字节：

| 返回文本 | UTF-8 bytes | SHA256 |
| --- | --- | --- |
| compute | 160423 | b87028235dbdbf90b222064df146d5e52099af2a6ca43deddb96bb90ba255a27 |
| report | 9105 | 5f2ed18fe52135fadf9906d3e3cc25b66863724f5bf26c33bd2a8f93cadbbb72 |

compute 第 11 步原科学与第 12 步必要读回均 failure；随后条件清理步骤本身完成但其实际 removed=false。report 的 success 仅表示传输现有小正文完成，report 原事件仍明确 compute_job_result=failure、scalar_readback_step_outcome=failure，不表示科学或完整必要读回成功。

## 2. 本次实际来源、输入与原合同

本次实际源码生成事件返回 150 件原公开 source、31 件同 job 生成 source（21 件历史视图及 10 件当前视图），合计 **181** 件；source_generation_complete=true。完整 source receipt 身份为 **106734 B / 59f6b8e993f01a7bfdbdb3cf01c4d549f6675153db2fb325ca387226709c2fc8**。该完整 receipt 仅以身份被打印，不把其 106734 B 正文冒作本结论完整取回。

原 request 为 **88551 B / 6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980**，原 recipe 为 **21539 B / 0c9fa04642835dd37f9da5aeb03a35abae4be4e75283c3e2203a73dcec6544ea**，当前 source plan 为 **36611 B / 9a184000c0b8e81dc3d247e39b873a2c66cc7be4a42cfa01090df8ebf2fd7326**。public 与隔离临时目录的 request/recipe/plan 字节身份分别相同；原 GITHUB_WORKSPACE 保留，实际 imports 使用隔离临时 computations 的 HERE。

10 件当前生成入口的已绑定身份如下。这是 source 身份表，不是这些程序的数学成功表。

| 当前 source basename | bytes | SHA256 |
| --- | --- | --- |
| geometry_20261116_original64_input_support_contracted_finite_trace_loader.mjs | 12041 | `208fae784a8922b0d2c1fd16b0740ea4580e6050f5989243942d0d40c75b7a7f` |
| exact_20261116_original64_input_support_contracted_finite_trace_tail_base.py | 20312 | `cdce0914ca0b27ad5171cbd950f7ddf56cfc82040bff81596f4fa4a16c421f2e` |
| geometry_20261116_input_support_contracted_trace_r273_tail_client_hook.mjs | 55119 | `a1ed1ac6b02bc01c5d0261dd5e9e361c0a831798f42e981f2e96f72ffff0d83c` |
| exact_20261116_input_support_contracted_trace_r273_current576_system.py | 29352 | `465a8789867037e2e4fe8af80462790e8af67a799aad5e5a027f76385a775f70` |
| exact_20261116_input_support_contracted_trace_r273_current576_chain_qr.py | 22093 | `75ff9ef6b212c9b7338479fa262d783a169d3833ee012bf25d64b00725471294` |
| geometry_20261116_input_support_contracted_trace_r273_tail_client.py | 20997 | `aa9139a85d3debf268568167249c23af0f12a31b4ad7352da7e8e80a64f26fe1` |
| geometry_20261116_input_support_contracted_trace_r273_height_path.py | 23988 | `e5b52b2bc1b2068dc264ea26ac01a8b0c9adff3e17c28dce1008365f0011e1ee` |
| geometry_20261116_six_control_input_support_contracted_trace_r273_full112.py | 50982 | `0a1a7cca83bdd0b3738df6e92f2534a280cd00b1a17e218b75256dd6283e342d` |
| root_20261116_six_control_input_support_contracted_trace_r273_run.py | 14990 | `3ce47137edc42df9e97997d6819860deedea74909970dfcac9bdab1ce89fda2d` |
| root_20261116_six_control_input_support_contracted_trace_r273_scalar_readout.py | 49693 | `e9be110da50ccdb71dc066bc246aea78564b793d9e82580280c3813abf93712f` |

原 R523 新 flow 为 `geometry_20261116_original64_input_support_finite_trace_flow.mjs`，SHA256 `14c691bec5ca228495027185ed642730d90d17ce65467ac76662c9407cd7d960`；小 helper 为 `geometry_20261116_finite_trace_actual_input_support_linear.mjs`，SHA256 `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3`。实际 launcher 明确登记其 factory `createOriginal64InputSupportFiniteTraceVariationalEngine` 与 backend `original64-noJ-primal-zero-flux-input-support-finite-root-variation-v1`。原 R471 variation 与 R466 contraction 字节保持；后者 helper SHA256 为 `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59`。

R523 的已刊条件结论仍只是：每次实际 finite A 与实际使用的 T 前缀核完后，以该次真实行非零地址组织工作；所有未省乘加保持原 j 顺序，完整 226 行 × 224 列及两 mean 均保留。资格不符走原完整循环，非有限中间值不由 finite 输入排除，NaN payload 不声称逐词相同。该局部条件不自动成为 whole-run 等价、全局误差或提速证明。原 R466 名义系数切向的适用对象及未证明舍入导数/邻分支不变性也没有因本次实际执行而消失。详见 [R524 完整入口](R524-actual-input-support-complete-original-full112-composition.md)及[原接口](../notes/2026-11-16-request224-actual-input-support-full112-interface.md)。

实际 source 事件记录原六参数为 [0.41654476801167684, 0.23884336093393582, 0.5270922473095916, -0.13437878055563054, -0.005765450212224129, 0.4141025261683763]，lambda_target=0.001。无新低三根门、无已接受 native anchor 宣称。原恢复 commit 为 `8bd267107cc8710d371f3b62c02986655ac965b0`，实际原输入恢复事件逐件给出：

| 历史 source path（相对本题） | bytes | SHA256 | Git blob |
| --- | --- | --- | --- |
| notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` | `6a9dfda743c464af6ae1190208e7157fa66df30f` |
| notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` | `d3aadef529d767c8facc26c399f458e903014512` |
| notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` | `5b7093c4f088c738e1d074fcea851f631782ee31` |
| notes/public-actions-43588155190-1-prepare112/T112-config.json | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` | `543d8364593985305438dda6a0c89b4b1a9c7ec5` |
| notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` |
| notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` | `b6c44fe237750f13c8b10366f15525b481a74e09` |

这些大数学输入只在 Actions 临时使用，本文只保已打印身份；没有通过 connector 再下载输入全文。实际事件 initialCheckpoint_present=false、failed91_95_103_checkpoint_not_consumed=true、original_config_not_rewritten=true、old_zero_J_is_only_initial_guess_data=true、rearchive_inputs=false。

原执行参数未因本次停止放宽：112 个物理尾频率、576 个当前场 cell、226 状态及224形状列、338×112 输出责任；jac_workers=2、max_nodes=1200、material_angles=physical_angles=4096、node_heap=6144、outer_iterations=8、原 inner_trial_count=17、native_max_iterations=32、native_trial_count=10；collocation_tolerance=1e-6、boundary_tolerance=1e-11、native_tolerance=2e-9、boundary_FD_tolerance=5e-5。原 science_step_timeout=330 min、compute_job_timeout=350 min，真正科学总钟仍18000秒。

上述 jac_workers 参数是冻结原入口参数，**不是 R531 两个 cellFlow worker 的实际并行声明**。actual224 没有借本次后继227身份或统计补付任何并行执行。

## 3. 第一份原请求：零高确实收敛，外部没有索取完整 J/audit

10:42:27.3314411Z 原 request_started 给出 request_index=native_call=1、s=0、increment=0、zero_request=true、exact_H_star_copy=false、jacobian=false、audit=false；请求 H 的实际896字节 binary64 身份：

`d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5`。

shape=[112]、dtype=<f8、order=C、negative_zero_columns=[]。开始时 remaining_wall_clock_seconds=17976.075695497；尚未接受且 response_observed=false 是该开始事件的时点状态，不能误作随后结果。

10:47:55.9431822Z 原 request_returned 独立事件明确 phase=original-native-converged、accepted=true、response_observed=true、original_client_calls_after=1、original_request_seconds=328.594023019。其原响应：

| 字段 | 实际值 |
| --- | --- |
| converged / residual | true / 0 |
| actual_nonlinear_solve / finite_tail_only | true / true |
| checkpoint_present / history_count | true / 1 |
| full_J_present / full_J_identity / full_J_scalar_count | false / null / null |
| audit_present | false |
| meanSlope | 0.08000000000000027 |
| meanSecond | -1.866666666666673 |
| meanSlopeCorrection / meanSecondCorrection | 0 / 0 |
| original_client_all_requested_jet_J_and_residual_checks_passed | true |
| original_full_DN_accepted | false |

“所有本次已请求检查通过”中的量词受 jacobian=false、audit=false 限制。它不等于完整 endpoint 338×112 / 最终 audit 已付。外部没有索取完整 J 也不表示初始化内部切向工作可跳过：原 trace 真实给出 iteration0 norm=0、minA=minD=1，随后 tangent_predictor_ready。该零高状态仍是原有限 Fourier/depth shooting 状态，far Robin 条件不是精确旋转 collar；原 checkpoint scope 明文如此。

原 trace 返回6条：请求、原current576请求上下文、求解前compact GC、iteration0、predictorready、response。关键时间为：

| UTC / 原 elapsed_ms | 原事件 |
| --- | --- |
| 10:42:27.331Z | request：jacobian=false、audit=false |
| 10:42:27.337Z | original_r273_current576_request_context；原冷启动/实时预测/fallback保留，worker_last_not_assigned=true、seed_assigned=false |
| 10:47:48.973Z / 321642 | iteration0：norm0、minA1、minD1 |
| 10:47:55.883Z | tangent_predictor_ready；maxChartCondition=385639393697279100000 |
| 10:47:55.884Z / 328553 | response：convergedtrue、residual0、响应自身maxChartCondition0 |

两处 maxChartCondition 是不同原事件的不同字段，本文分别保留，不互相覆盖。无原 trial（original_trial_count=0、original_trials=[]）。本次零高用时可与既有事实并列，但没有独立分项计时或完整新统计，故不能把其差额全部归给 R523，也不从零高耗时推出正高或整条任务必完成。

## 4. 第一份正高：原当前方向已返回，一个原试步被接受，随后预算停止

10:47:55.9446859Z 开始 request_index=native_call=2。实际 proposed_s=proposed_increment=0.015625，previous_converged_s=0；这是第一份正高尝试。请求 H 的896字节身份为：

`fb6da818e40bcdaa0bc57ceb9a86d5ae2845132054389a2eac73ea866283a032`。

shape/dtype/order同前，negative_zero_columns=[]，zero_request=false、exact_H_star_copy=false；外部仍jacobian=false、audit=false。开始时剩余17647.464300811秒；结束所记录请求耗时17647.627305618秒。elapsed、remaining是原记录的不同采样时点，不据相减制造额外预算。

原8条 trace 与1条 trial 全部由这份独立返回事件选出，关键内容如下：

| UTC / elapsed_ms | 实际事件及完整决定值 |
| --- | --- |
| 10:47:55.943Z | request call2，jacobianfalse、auditfalse |
| 10:47:55.949Z | 真实current576请求；原cold/predictor/fallback保留，worker_last_not_assigned=true、seed_assigned=false |
| 10:47:56.012Z | tangent_warm_predictor：modes112、stages576，maxChartCondition385639393697279100000，maxRelativeCorrection3.844494357362678e+252；原scope只称初猜 |
| 10:47:56.031Z | compact_storage_gc_before_solve；原事件保求解前内存快照，非科学验收 |
| 15:10:58.060Z / 15782117 | iteration0：norm196395.0911309943、minA0.9315748352465438、minD0.9999646599422697 |
| 15:11:23.024Z / 15807081 | 同iteration0 correction：相同norm/minA/minD，chartCondition=null |
| 15:14:54.866Z | 原trial0、step1、kindaccepted；baseNorm196395.0911309943、trialNorm5181.565456345417 |
| 15:14:54.992Z / 16019049 | iteration1 accepted-trial-recovery-only，acceptedFromIteration0、acceptedTrial0、acceptedStep1、norm5181.565456345417 |
| 15:42:03.410Z | failure：Error: finite-trace-direction-resource-budget |

其中 trial 来自独立 original_trials，不把它伪充 trace 的第9条。actual current correction progress 事件还真实给出 native_call=2、nonlinear_iteration=0、snapshot_completed=true、linear_direction_returned=true；source_current_withJ_norm 为 value196395.0911309943、float64le_hex=`01e3a2ba58f90741`、classification=finite。actual_error_text=null、original_error_text_complete=true。原源明确这是 progress，不是完整最终readback。

该事件指向 `call-0002/current-corrections.jsonl`，**14098 B / 9043343ff19ea3ac66ddee3ca9dc984dcd67b9d69b9def48bdce17fe29c102d2**。它的完整正文没有返回。故可以据已返回字段断言此次iteration0 snapshot及linear direction确实返回；不能据此补出全部14计数、每engine当前未完地址、全部338×112或审计。

15:42:04.0574145Z 原 request_returned 的 phase 为 protocol-or-record-partial，accepted=false、response_observed=true、original_client_calls_after=2，original_full_DN_accepted=false。原响应 failed=`Error: finite-trace-direction-resource-budget`；lastIteration 指刚才iteration1的accepted-trial-recovery-only状态。actual_nonlinear_solve=true、finite_tail_only=true、checkpoint_present=true，但history_count=null、full_J_present=false、full_J_identity=null、full_J_scalar_count=null、audit_present=false。原checkpoint_scope为 **FAILED Newton state; retained only for diagnosis and possible initial guesses.** 这不是新的接受父状态。

原Python最外表述是 FloatingPointError，文字为 `Actual complete finite tail rejected`，内含上述资源error与lastIteration。异常路径实际经过：
`height_path.py:351 owner.solve` → `full112.py:417 self.client.solve` → `tail_client.py:321 original.TailClient.solve` → `tail_base.py:273`。
随后原height路径第392行另给 `ValueError('Not an unambiguous identity-bound original mathematical refusal')`。这两个原异常都保留；外层“rejected”这个通用单词不能覆盖内部资源原因，也不能把协议分责异常变成数学不可能证明。

原 existing_failure_context 明确 original_iteration_event_count=3、original_trial_event_count=1、original_located_trial_failures=[]；cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source=false。原 outerfailure 没有给出实际 stage/radius/angle/D/S/A 失败地址；`actual_stage_radius_angle_D_S_A_not_supplied_by_outer_failure=true`。没有在本结论中猜一个失败 cell，或以相邻运行补地址。

## 5. 原阶段终态、未完成责任及超限读回

15:42:04.0597317Z 原height_path_finished真实为：

- phase=protocol-or-record-partial、complete_endpoint=false；
- last_converged_s=0.0、last_converged_call=1；
- request_count=2、resource_partial=true；
- original_full_DN_accepted=false。

内部一次试步接受与高度路径accepted是两个层次；本次只有零高路径请求成为完整接受。原完整endpoint未到达；完整当前H星响应、其末端FD/full-DN与最终物理审计的全链接受不能宣称。针对未返摘要的任何其他内部量，本文只标未获证据，不能由缺少输出反推每个下游文件完全不存在。

15:42:04.3641033Z wrapper实际记录 phase=wall-clock-budget-partial、returncode124、budget_exhausted=true、external_signal=null，process_status_sha256=`6c0f228e03e38fe0485b4b312c8427fb5f2a8188db89a92910bff528b02b6fce`。已返回1505字节正文进一步保全 process：

| 字段 | 实际值 |
| --- | --- |
| phase | wall-clock-budget-partial |
| scientific_wall_clock_seconds | 18000 |
| scientific_child_returncode | -15 |
| wrapper_returncode | 124 |
| elapsed_seconds | 18000.956826378002 |
| budget_exhausted | true |
| external_signal | null |
| owned_group_quiescent_after_return | true |

其中child_returncode=-15与external_signal=null不冲突：前者是实际child返回，后者是wrapper记录的外部信号字段；原wrapper预算耗尽可以终止其自有child而没有外来取消。本文不把124统一当某个非线性拒绝，亦不把 -15 单独解释为用户取消。

完整必要正文没有通过原上限。其 attempted identity 与实际小正文身份在首段已列；hash均不含帧分隔LF。实际compute frame与report frame内正文逐字同一；report又核其bytes/SHA并保failure来源。报告未逐片回传107463正文、没有大对象编码、没有用SHA找回被留在临时树的正文。

小正文adapter只返回：schema=`six-control-input-support-contracted-trace-r273-height-path-three-active-nonzero112-physical-DN-v1`、phase=original-same-worker-height-path、success=false、new_coupled_finite_acceptance=false、full_Cartesian_closed_surface=false、prepared_sha256=`2ca1f4d544718c7689625aedbe7d07c43ecba6efb1d2f9decb31c0464e285b3e`、initial_collocation_max=6.8749454041621035e-06。这个collocation值是被选出的初始量，不能升格为全部域/边界误差界；prepared仅已回SHA，没有虚补字节数或全文。

超限范围尤其包括：完整当前finite-trace/root/linear14计数、所有last_observation与fallback地址、原source/rules详细必要对象、完整current-correction细节、全部FD/full-DN逐项scope。原源码确实选择这些范围不等于本次全部返回。本文保存已回“原接受不重分类”、no_partial_trial_table_claimed_complete=true、raw_retained_until_runner_destruction=true，不补造其丢失内容。

## 6. 完整已返事件的必要身份与临时数据边界

下表是独立已打印事件去时间戳、无终LF的UTF-8身份。它们用于区分事件本身与它们指向的临时大文件；不需要保存事件原raw到Git。

| 原实际事件 / 时刻 UTC | 必要行 bytes（去时间戳、无 LF） | SHA256 |
| --- | --- | --- |
| request224_height_path_request_returned / 2026-11-16T10:47:55.9431822Z | 4506 | `57ef77e84ec70a38c0aff6fb1cec65106310a5234fbd3017d8673ddd1832bde1` |
| request224_current_correction_progress / 2026-11-16T15:42:03.9908305Z | 621 | `f5980f3cdaaf058c1729602ba12299281227c99f3ddfadbdac8ea85f6417176d` |
| request224_height_path_request_returned / 2026-11-16T15:42:04.0574145Z | 8559 | `4279b24964a9357dbdc4f9e723f411b7d92e3bfc114297b5d8769512219988fb` |
| request224_height_path_finished / 2026-11-16T15:42:04.0597317Z | 397 | `7a1137721e94f95a73316614074aed5e3a639d3e9861a5c2facfa1518662748f` |
| request224_height_path_full112_process_returned / 2026-11-16T15:42:04.3641033Z | 325 | `ec11e01fab7d15236fd30ce955162dd8025b5497496118ad5492beebfdccca44` |
| request224-original-rules-parent-readback-v1 / 2026-11-16T15:42:05.3063759Z  | 959 | `d6b659e092f7a5f62650ddadf0a0c6c08eb8d0b270468bc24bb251c4d809454c` |
| request224-conditional-owned-cleanup-v1 / 2026-11-16T15:42:05.5110276Z  | 1184 | `8761f99e9a2995e5483c8c6fb66f40e74273303bcb76e18c7dfcff28d52c721c` |

已回临时科学数据身份如下。这里只保返回身份和scope，不恢复、重新求值或再发布raw：

| 原临时文件 | bytes | SHA256 / 边界 |
| --- | --- | --- |
| full-DN/true-tail_0001.json.gz | 10114 | a0674d251420fdf9cb0b99c281344280ed0676f9bfd425c34d0acb1e8ef80d39 |
| height-path/request-001-trace.jsonl | 1397 | dfca82e33093237d438f8a38ddd76886c5d1d6a72c6c381cdc5bac4804870fbd |
| height-path/request-001-trials | null | 原trial_count0，没有把未生成当空文件 |
| full-DN/true-tail_0002.json.gz | 1281542 | bac75124973b6ffcc7e4a7e45cdb86f0a3737f17567e7efb50c1da9ff557aed9 |
| height-path/request-002-trace.jsonl | 4444 | 3e3f7acbf0dfc2e8308ca2e0d3580e7c2429783a7c006929dbb7d480a63d8ddc |
| height-path/request-002-trials.jsonl | 155 | f115b576fb683ed7337182024e0254e3255c293c5afe615dcac6e0926e4b7b97 |
| height-path/height-path-status.json | 17925 | 8c480b9a9855148cfffef8cb3300bd72c76188c5332d173c5c1edbb4b111e526 |
| call-0002/current-corrections.jsonl | 14098 | 9043343ff19ea3ac66ddee3ca9dc984dcd67b9d69b9def48bdce17fe29c102d2 |

两个请求返回的 original_source_identity 均为canonical_JSON_bytes16349 / `63e3bf3c68d15b8bffabfcd1e5b793339846eab23a9b8b5c223d1a69fad95dde`；original_config_identity 均1565 / `a7d9096523113dcba65abde5282bde09ab7b5c375f1ca27505a0632dec00b923`。这是原对象规范JSON身份，不冒底层所有浮点原始词。两个checkpoint_height_JSON_identity分别225 / `64c19f2662ac257bca17a036d0c4809671b09bf950df1d6c82b42461fabe7e56`与2578 / `205c33d3f6f15da2d1641d6860cf4104533fdf29cfa1c69b512f1b58a235f9c6`；原字段 checkpoint_JSON_preserves_pre_serialization_negative_zero_claimed=false，故不从JSON宣称序列化前负零恢复。

## 7. 原规矩同步、真实quiet和条件清理

原同步runner SHA256为 `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`；实际明确baseline更新将根README旧blob `6183b7f3eaa5edf22cd1a62fa19d84bf4ab3ba09`更新到已读 `21bd547f56590b7f2dd279d0297efb289a9b2783`，本题README仍 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。原2700秒pull/rebase与规则变化停止责任保留。日志实际给出7个completed轮次：

| round / UTC | origin_main_read | published_commit |
| --- | --- | --- |
| 0 / 2026-11-16 10:42:03 UTC | 8bfb9ad7be5eeaa470c0cd7eecaa401c95c1cd10 | 23873c4978fdba1d7f097685ff0de513fa59b4f4 |
| 1 / 2026-11-16 11:27:05 UTC | 40eeef92de9f7cb7868062a3697baa8d427f644f | 9d4348a0b8ac340114a4511f2e2fa6ba1686baa2 |
| 2 / 2026-11-16 12:12:08 UTC | 06a5005564d46c708d81ae0be1841ac5c2ab5198 | d0d923853c15915cf727485bdabf6a9aed023dc5 |
| 3 / 2026-11-16 12:57:11 UTC | 23d90b608b9222ad14192480429add143b4a41c9 | 4f91916290708d7b28be9538042450a159d3e6c9 |
| 4 / 2026-11-16 13:42:13 UTC | 1cf46b9f2d16cd3592238d343bff53a936200b23 | f181057be45a8c5bb695af51d7d0ece2f3aea7be |
| 5 / 2026-11-16 14:27:16 UTC | 7e1f2156f2993d0870c7c88e67d4ad7dd1be5bd7 | 08bd7d1a64dc73fdaf0870559738eb4b902aac6a |
| 6 / 2026-11-16 15:12:19 UTC | 7eedf292bf5821829c756a02fcbb7408d118ea20 | c7e29a16b237a452f719c69bfd4e3d77a863d4dc |

这些轮次不是科学source热更新声明；科学source始终按实际运行头与同job绑定闭包。完整rules必要对象没有因1505摘要而返回。

实际规则父readback为 quiescent=true、no_process_signalled=true、shared_runner_PGID_not_required_empty=true。其父身份 pid3103/start_ticks5719/pgid1971/sid1971；当前PID观察null、same_recorded_process_still_present=false、wrapper_return_observed=true。原 `rules-parent-owner.json` 为534 B / `52685b1bcc2e866435e264562b5b617de39fad62389bc588e10cb67c20da5209`，实际started_unix_seconds1794825720.5456154、finally_recorded_unix_seconds1794843724.4022133、wrapper_returncode124。这里根据真实PID/startticks确认，不要求共享runner PGID全空，不声称对子进程树任意未知进程做了信号清理。

科学wrapper必要小正文同时记录 owned_group_quiescent_after_return=true。**quiet并不替代完整必要读回**。条件cleanup读 `scalar-readout/readback-complete.json` 时实际FileNotFoundError；schema=`request224-conditional-owned-cleanup-v1`、scalar_step_outcome=failure、source_view_generation_outcome=success、removed=false。原异常栈明确落在 `<stdin>:29` 的read_bytes，以及pathlib读取缺失marker。

冻结workflow只有在同run/source/request/recipe/reader的完整marker、完整single-summary、fresh科学ownerquiet和规则parentabsent等均成立时才调用shutil.rmtree。此次marker缺失就进入原保留分支；日志没有删除成功事件。**已知的是cleanup未删除、原策略留至runner销毁；没有将runner最终销毁的时刻或raw仍可持久取得补为事实。** 没有artifact/release/Git raw上传。本结论只刊作者说明、源码与实际身份，不把必要raw或临时数组造为detachedGit对象。

## 8. 可直接使用的结论与仍未付范围

本次实际补到的范围是：实际R523来源闭包被成功生成和绑定；原零高有限tail请求完整收敛并给出两mean；第一份正高原current576 iteration0快照和方向真实完成；原trial0/step1实际接受；原资源停止、双job小正文、PID分责和未清理范围均有真实返回。

本次没有补到：正高请求完整收敛、s=1 endpoint、当前全部FD与原full-DN末门、完整物理审计、真实全闭面、未返回107463必要正文中的全部计数与地址。原末状态仍失败诊断checkpoint，不能作为下一次已接受父对象；若未来使用数字作初猜，必须显式新输入来源与完整fresh求解，不能把该内部试步或quiet当接受迁移。

零高328.594秒是原请求实际用时；正高当前iteration0事件仍到15782117ms才出现。两者足以提示零高与正高计算责任差异，但本次没有root/dFlux/linear分项计时，也没有完整14计数读回，故不能给R523占比、whole-run速度、剩余时间可完成性或条件数因果解释。尤其chartCondition=null不等于无穷、失败或零；warm predictor超大修正只保原初猜字段，原真实trial与预算记录才说明此次实际走到哪里。

后继仍须保持全部原列/mean/物理域/末门；必要传输的固定语义重复可独立修表示，不能抬90000上限、删失败地址或把完整正文拆片回来。这个表示问题与本次已真实执行的数值进展分别记账，不相互覆盖。
