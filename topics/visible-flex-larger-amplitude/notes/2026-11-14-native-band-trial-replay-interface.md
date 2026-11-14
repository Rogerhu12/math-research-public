# 同一 native 基态的一次原试步重放接口

2026-11-14。此入口只准备一次原线搜索；没有在本地运行数值，也尚未产生新原生试步结果。真实 request34 的带状校正虽然 `dgbtrf/dgbtrs info=0`，其原尺度线性缺陷仍很大，故**本接口不用于调度该方向**。它为后续同一实际矩阵上得到的有效完整方向保留原非线性试步路径。

独立源：

- `../computations/geometry_20261114_native_band_trial_replay.py`
- `../computations/geometry_20261114_native_band_trial_replay_hook.mjs`

原 capture、band、worker、engine、方程源、容差及已发布结果一律不改。输入 producer 的文件名和 SHA、完整 result SHA 都显式绑定；默认 producer 是已冻结的 `geometry_20261114_native_captured_band_correction.py`，其源 SHA 为 `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`。后继均衡/误差修正源可使用相同完整方向输出契约，必须显式给其真实文件及 SHA，不能冒用旧 producer。

## 1. 使用哪个基态与哪一个评估

基态就是 request23 已完成 no-J 探针的全 577×224 states；负零侧表恢复后 bit SHA 是

`6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8`。

原 H 112 项、原 `H/rCut^4`、原所有 graph/gain、far Robin、576 个 stage 的配置和原 residual scales 全部保持。原 H 非零，既不设阈值，也不通过幅比映射为零。原 scale bit SHA 为

`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`。

线搜索的基态范数、minA、minD 来自真实 request28 已完整返回的原 `evaluate(...,true,...)`。原 norm 为 `0.04177307820740199`。它们以原 binary64 bits 绑定并**作为缓存复用，不是这次新求值**。新入口明确记录：

```text
baseline_is_cached_from_actual28 = true
new_baseline_evaluations = 0
new_J_evaluations = 0
new_corrections = 0
```

`baseline-reuse.json`、初始 worker trace、最终 summary 和 Python result 都区分这项缓存。原 progress 回调仍会收到第 0 次 history 行；应结合该缓存来源记录解释，不能将其列为一次新 withJac 计算。原最终 endpoint Jacobian 与 fresh audit 均未执行。

缓存绑定来自 capture 的真实完整结果：

| 文件 | SHA256 |
|---|---|
| `result.json` | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| `capture-summary.json` | `48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1` |
| `capture-manifest.json` | `3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3` |

另保 `capture-begin.json`、`capture-spec.json`、`core-instrumentation.json`、`seed-binding.json`、`original-live-identity-before-seed.json`；它们都按上述固定 result 的完整清单逐字节核 SHA/大小。这里只需这 8 件有界 metadata，**不需要再次下载/载入 231 MB 完整 J**。

## 2. 对原核心文本的确切修改范围

同一次 loader 只对原 engine 已完成其原 stable-graph/recovery 替换后的 core 做以下变更：

1. 首个 `const ev=evaluate(states,target,true,scales);` 改为绑定上述缓存基态的读取。
2. 首个 `const cor=correction(ev,states,target);` 改为读取已保存的完整原坐标方向。
3. 在原十档线搜索之后、原 `if(!accepted)throw ...` 之前插入结果保存/计划停机观察器。

这不是声称加载后原完整 solve 不变。上述两处调用替换和观察器在独立 `core-instrumentation.json` 中明确记录；所有磁盘原源与原 ready manifest 不变，加载后的源 SHA 单独记录。逐一反向移除这些修改必须恢复原 runtime core 全文；原 runtime core SHA 还必须与 request28 相同。

以下原十档试步正文逐字节保留：

```javascript
for (let k = 0; k < 10; k++) {
  // 原文中的 lambda = 2**(-k)、states + lambda * delta；
  // 原 evaluate(trial, target, false, scales)；
  // 原 momentum D/S/A、root-solver 及其余所有域异常处理；
  // 原严格 test.norm < ev.norm；
  // 原 trialDiagnostic 与 accepted-trial recovery 回调。
}
```

上面代码块只说明保留范围，不是替换实现。实际来源文本的十档循环 SHA 在纯字符串检查中为

`603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99`。

每个实际 trial 仍调用原 `evaluate(false)`，保持原全 576 stage/112 cut/112 far 与原尺度；失败位置仍由原 evaluate 报出。没有新 Armijo、缩步范围、容差、guard 或截频。saved-direction 的 `maxChartCondition` 写 `null`，因为这次没有计算 Riccati chart；不得将旧 chartCondition 或不存在的 full-system condition 填进去。

## 3. 完整方向输入契约

`--band-directory` 只需 3 件：

- `result.json`：CLI 必须显式给 `--band-result-sha256`。
- result 所列 `direction-checkpoint.json.gz`。
- result 所列 `output-array-manifest.json`。

producer 使用如下已经建立的完整输出契约：

```text
result.schema = original-captured-native-full-band-correction-v1
result.source_sha256 = 显式给定 producer SHA
result.diagnostic_completed = true
result.linear_direction_computed = true
result.lapack_factor_info = result.lapack_solve_info = 0
result.M/K/depth/dimension = 112/224/576/129248
result.native_accepted = false
result.new_J_calls = result.original_native_calls = result.nonlinear_trials = 0

checkpoint.schema = complete-original-native-band-direction-v1
checkpoint.source_sha256 = 同一 producer SHA
checkpoint.input_binding = 同 actual28 的 result/summary/manifest/core/全部 raw-array SHA
checkpoint.rows = 全 577 个有序节点，每个 state 224 项及 negative_zero_columns
checkpoint.delta_float64le_sha256 = 全原坐标方向 bytes SHA
```

checkpoint 的完整 δ 恢复后必须全 finite、形状及 bit SHA 与 result 和 manifest 相同。这里不将 LAPACK info0 或方向全 finite 视为线性质量通过，更不视为 native 接受。原方程缺陷由 producer 的完整原尺度读数和实际精确行证据判断；接口不另设数值容差。当前 request34 的 direction 虽满足结构契约，实际质量不足，不能因此自动派发。

作为当前字节格式实物，request34 result SHA 是
`5e0d6d7f1b9ddc03565fdd62075d9b8d79a89d15078915e591732a0ce46d7dac`；
checkpoint SHA 是
`7c5864155fb20215ab634f31f29263c45629c27c376cdcfc84e2596ccb75f6c8`；
δ bit SHA 是
`cca90e77f21a1783e6d27ee83781cb19156f7575ba141ce7983aa0b1b2493e5b`。
这些只是绑定示例，**不是当前调度请求**。

## 4. 输出和停止语义

新增 `trial-replay-records.jsonl` 保留每个真实原 trial 的 index、步长、基态范数、原 rejection kind/error/stage/rawCell/rawSegment 或实际 trial norm，另保关键数值的 binary64 bits。如果原回调给出失败 stage 的输入，保存全 224 项 `<f8` gzip，正负零及实际非有限值都由原位模式表示，不以 JSON 的零或 null 覆盖。

若原严格范数下降条件接受某一步：

- 原 accepted callback 和 recovery-only progress 仍先执行。
- 保存全 577×224 `selected-state.f64le.gz` 和 `selected-state-checkpoint.json.gz`，包括原 H、全部参数、rawNode、方向/基态/来源 SHA、负零侧表；非有限项若出现则也保其位模式，不能静默改成零。
- 新观察器抛 `VISIBLE_NATIVE_BAND_TRIAL_REPLAY_ACCEPTED_STOP_V1`，原 worker 原 catch 会如实返回 failed；Python 识别这一**计划诊断停机**。
- summary 的 `trial_accepted=true` 只表示一次原 trial 下降。`native_accepted=false`、`success=false`、`converged=false`、`native_tail_response=false`、`task_completed=false` 保持，下一 Newton、endpoint J、fresh audit 均未支付。

若十步全拒绝，保存完整实际 summary，然后返回原失败行；原错误 `multiple-shooting line search failed at ...` 原样抛出，退出码仍为 2。若原 guard/回调/I/O 或身份检查使流程提前停止，保全已经观察到的 records 并标 `replay_completed=false`，不把缺失试步补成失败或通过。

原协议 request 仍携带 `jacobian=true,audit=true`，以保留原调用身份；计划停机发生在这些末端工作之前，最终报告明确二者未计算。没有设置原 worker 的 last/完整 response cache，没有伪造 tangentPredictor。

## 5. Actions CLI

沿用 25/28 的原公开数据输入。`BAND` 指将来实际足够好的完整方向目录；producer/source/result 三项都用真实冻结值。

```bash
python "$C/geometry_20261114_native_band_trial_replay.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --band-directory "$BAND" \
  --band-result-sha256 "$ACTUAL_BAND_RESULT_SHA256" \
  --band-source-file "$FROZEN_DIRECTION_PRODUCER_FILENAME" \
  --band-source-sha256 "$FROZEN_DIRECTION_PRODUCER_SHA256" \
  --source-topic "$REPO/topics/visible-flexible-closed-surface" \
  --node-heap 6144 \
  --out "$OUT/native-band-one-trial-replay"
```

所有数值只在本公开仓库 Actions。wrapper 保留原完整 TailClient 握手、容量/source/config/ready 检查，Popen 只对唯一 frozen worker 插入独立 hook；无关 Git 子进程不受影响。输出目录必须独立且空。原 source tree 仍按原 client 的窄数据恢复方式提供，不要求全克隆。

本地只做 AST、`node --check` 和纯源字符串插入/反插入检查；没有导入或执行原数值模块。科学结论依实际后续 Actions 回执，不能从源码检查推导。
