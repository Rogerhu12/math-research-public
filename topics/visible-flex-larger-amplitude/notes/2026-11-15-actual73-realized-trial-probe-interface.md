# Actual73 末轮真实试步：一次原 no-J 求值接口

- 日期：2026-11-15 UTC。
- 类型：独立 Actions 实验源码与输入/输出合同；尚无本次实验结果。
- 作者：geometry；精确有限数组分解由 exact_refinement 的独立消费者完成。
- 范围：原 actual73 末轮实际完整状态、完整方向和固定原试步 $\alpha=1/512$。不改变 $g$、全部 $H$、远端图、原尺度、root 策略、原科学阈值或原冻结求解源码。

## 1. 已有事实与本次问题

原第 73 轮有三次真实 fresh-withJ 和三次完整 R273 方向。末轮在原十个试步中全部未得到严格的原范数下降，其中最后三个试步的**范数标量**与基态相同。原输出没有保存这三个试步的完整状态和残差，故这个标量事实不能推出每个状态词或每一行残差相同。

已付 R276 账显示，末轮保存矩阵的精确有限数组模型在全部十个原步长上均严格下降。因此本次不是再寻找一个线性下降区间，也不先更换阻尼参数。只补缺少的真实输入和输出：用末轮原状态与方向，逐字执行原 $1/512$ 试步表达式，再调用一次原 `evaluate(false)`，保存实际舍入后的全部状态和全部返回残差。

正式依据见：

- `2026-11-15-actual73-noJ-primal-native-line-search-failure.md`。
- `2026-11-15-actual73-complete-QR-exact-affine-infinity-and-byte-readback.md`。
- `2026-11-15-actual73-r276-iteration002-original.json.gz`：12,153 B，SHA256 `b7812e06716bb1d22d4d32ff6ca12c62cb926dd9df12f41c199988f933ccd029`。

本接口不预先认定状态形成舍入、root 舍入、切向误差或其它任何一项为唯一原因；新输出也不是一次完整原生求解成功。

## 2. 三个独立冻结源码

所有文件位于同一个 computations 目录；旧 73 源保持原字节。当前交付草稿位于 `/tmp/native-realized-trial83-source/`。

| 源码 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_native_realized_trial_probe.py` | 30,617 | `305f5db2c6bc0fef85bd3115045531b1b366334b33300852634692a537f7d9cb` |
| `geometry_20261115_native_realized_trial_probe_hook.mjs` | 37,135 | `c03f59e4c3b6555a7a47187f1905a70f1e5a92dafacc222c327f4913c3ccdce0` |
| `geometry_20261115_fetch_actual73_realized_selected.py` | 17,288 | `51f865285ab348792842a3d1419135fd1c9ae8ece5c853d13776f252e43d4056` |

取件器沿用原完整 ZIP 验证和发布内核 `exact_20261114_fetch_pinned_public_artifact.py`，SHA256 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。只替换固定 tuple、公开身份注记及选择性提取函数。它不读取凭证，不打印签名 URL，不启动原科学模块。

原四个本地运行依赖继续硬锁：

| 原依赖 | SHA256 |
|---|---|
| `exact_20261114_true_tail_client.py` | `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09` |
| `exact_20261114_seeded_zero_tail_client.py` | `a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776` |
| `tail_frozen_worker.mjs` | `3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054` |
| `tail_resumable_engine.mjs` | `1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8` |

原公开 78 source 恢复、原 Node 24.22.1 / 6 GiB heap、原 TailClient 构造/ready/capacity 身份沿已执行的 69/73 路径。新的原 no-J 科学步骤不带 GitHub token；只取件与原 publisher 步骤使用各自授权环境。

## 3. 唯一真实父对象

原 run `43657001633`、source `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`，artifact `14141540502`：

- 名称 `visible-mainline-nojprimalnative-43657001633-1`。
- ZIP 1,752,742,419 B。
- ZIP SHA256 `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9`。

| 父件 | 实际 SHA256 |
|---|---|
| 原 native `result.json` | `ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394` |
| `iteration-002/snapshot/result.json` | `2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92` |
| 末轮完整 577×224 base raw | `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |
| `iteration-002/qr/result.json.gz` | `9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff` |
| 末轮完整 577×224 delta raw | `4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a` |
| 完整 576×224×224 保存 J raw stream | `1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4` |

末轮失败 checkpoint 的 JSON 字面完整状态重新打包后必须与 base raw 完全相同；本实际状态没有负零，不能把这个已核事实推广到其它状态。完整 delta 的负零通过 raw bytes 与原 checkpoint 的 `negative_zero_columns` 双重还原，包含原来的 25 个负零词。`rawNode` 是原九个物理边界 `[0,72,144,216,288,360,432,504,576]`，不是 577 项假想索引。

这仍是原失败现场，不是成功 anchor、缓存尾响应或新的 accepted 状态。

## 4. 选择性取件范围

取件器在 Actions 下载并核完整原 ZIP 和公开 tuple，再只提取下列原件；未选择 payload 不解压、不冒全 payload CRC 审计。所有已提取原件逐长度、CRC、SHA 核完，最终只读；十个 snapshot raw stream 另核完整有序 chunk 覆盖与 stream SHA。

1. native 根 `result.json` 和 14 个原记录：summary、输入/runtime config、intent、ready、capacity、原 live 身份、原 method 身份、core receipt、trace、trials、`current-corrections.jsonl`、`native_0001.json.gz`、primal installation。
2. 最后 snapshot 六个 metadata 件，以及其全部十个数组。完整 J 只供独立精确消费者使用；新 native probe 不读取 J payload。
3. 最后 QR 共 16 件：result、input binding、array manifest、完整 delta、完整 checkpoint；九份 `original_arrays` 原输入副本；已付 exact report 和 signed-e ledger。

其中两份已有精确账硬锁：

- `current576-exact-readback.json.gz`：158,691 B，SHA256 `36a0a1fde40e95ce7e33f18bc55d68d0fa16c30f6132429aa6feb39a71111a97`。
- `large-arrays/current576-all-exact-rows.jsonl.gz`：5,727,359 B，SHA256 `2d3f377c0126562375420bb174ced9d5d6b8201beae8fd3efda8d9a4a8fa94c4`。

不取 QR 因子、纯常数能量阵、其它迭代 J 或 worst-witness payload。保留九份 QR 原输入副本和 corrections JSONL 是为了直接兼容已冻 R276 binder 的完整来源核对，不把存在完整 manifest 当成所有 payload 已取回。

## 5. 原试步与唯一原求值

没有可选步长。源码固定 `k=9`，从原 core 检查下列整段原表达式唯一存在：

```javascript
const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
```

新 hook 使用完全相同的状态/方向词、乘法、加法和 typed-array 存入顺序。它不以 Python 重算试步，不先合并两操作，不清零 cut/far，不阈值化 $H$。原 trace 中同一 call/iteration/trial 的 `step` 和分类绑定为实际原件；原 norm 相等的旧标量只作为既有事实。

实际状态在调用前写出。随后恰一次：

```javascript
ev = dn.tail.evaluate(trial, target, false, scales);
```

`target`、`scales`、完整 $H$ 和 far graph 都来自原 raw；原 live constructor 的完整 source/config/ready/capacity、全部 graphs/gains/cells/profile breakpoints、physical raw-node 索引与原件逐项核。用原公式回核 $H\mapsto target$ 和 gains→scales 的字节身份，不以新尺度代替。

没有 `TailClient.solve`、fresh J、R273 求方向、重复 baseline、完整 Newton、endpoint sensitivity、cutJets 或 audit。原 no-J 的 ordinary/cusp/profile 路径保持原函数；actual73 的独立 matched-withJ 方法本次没有调用。

## 6. 原 source 观察的可逆范围

三个独立 source-only 观察都有完整原/新 source SHA 和精确剔除还原，不伪装或覆盖 `Function.toString`。

1. 原 worker 只替换请求循环，保原 constructor、ready 和冻结编译主体。协议收到已核 spec SHA 后执行本 probe 一次并退出。
2. 原 evaluate 的唯一 `cellFlow(n,states[n+1],withJac)` 前后增加 stage 观察回调。原 residual、cut/far、norm、guard catch 和算式一字不变。还原后的原 evaluate function SHA 为 `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。
3. 原 `78718-tail-fourier-root-momentum.mjs` 只在两个原成功 return 处观察该次真实返回对象；保原 root Newton、回溯、`8e-14`/`5e-12` 策略和所有算术。正常 return 不替换原对象；fallback 仍创建原同一字面对象，只给它局部名称以先观察再返回。原磁盘 SHA 为 `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`。

root 观察不再次调用 root/RHS/geometry/profile，也不改任何返回数组。每个实际成功 root return 记录 profile index、原 x、输入 full-state 长度/SHA、err/scale/iterations/fallback、L 和 moments 的原数组 SHA、原 `g` 所有数值字段以及原 minA/minD/minS/maxQuad。数值使用 `numberRecord` 保存 value/classification/原 f64 bits。每个 stage 独立 gzip；不会为一个大 JSON 累积整次运行。

原 guard 在 root 完成之前抛错时，不编造缺少的成功 root 返回；保存已经得到的记录和实际 error 的 stage/rawCell/rawSegment。观察 I/O 错误在回调内部单列为 `observer_io_failure`，不转成原科学 guard。失败与部分输出都保留，既不截断原字段，也不冒完整返回。

## 7. 输出数组、残差与 argmax

`array-manifest.json` schema 为 `actual73-iteration2-realized-noJ-trial-output-arrays-v1`。`arrays` 是 descriptor 列表；每项 `{name,file,bytes,sha256,dtype:'<f8',order:'C',shape}`。全部 raw 位于 `large-arrays/`，作为完整 artifact 原件，不要求进 Git。

| name | shape | 来源 |
|---|---|---|
| `base-states` | `[577,224]` | 原末轮 raw 状态 |
| `native-delta` | `[577,224]` | 原末轮 raw 方向，含负零 |
| `trial-states` | `[577,224]` | 本次原 JS 表达式实际生成、调用前保全 |
| `original-scales` | `[1,577]` | 原尺度 |
| `cut-target` | `[1,112]` | 原 target |
| `physical-height` | `[1,112]` | 原完整 H |
| `original-far-graph` | `[1,112]` | 原 far Robin graph |
| `saved-stage-residuals` | `[576,224]` | 原末轮保存 r |
| `saved-cut-residual` | `[1,112]` | 原末轮保存 cut |
| `saved-end-residual` | `[1,112]` | 原末轮保存 far |
| `trial-stage-out` | `[576,224]` | 本次原 ev.flows 的完整 out |
| `trial-stage-residuals` | `[576,224]` | 本次原 ev.residuals |
| `trial-cut-residual` | `[1,112]` | 原求值不返回 cut 阵；对未变输入按原 `trial[0][j]-target[j]` 逐项保存 |
| `trial-end-residual` | `[1,112]` | 本次原 ev.end |
| `trial-mean-height-increments` | `[1,576]` | 本次各原 flow.meanHeight |

前十阵在原调用前写出；后五阵仅在该调用完整返回后存在。原 no-J 的 minA/minD 聚合量可能为 $+\infty$ 占位，按原 bits 保存，不增加 finite 门。原真实 `ev.norm` 单独保存；事后扫描原 r/cut/far 与原 scales 只给诊断 argmax 和 reconstructed norm，不回写原 norm，也不改变原验收。

`actual_noJ_residual_readback.worst` 带 kind、stage/rawCell/rawSegment 或 boundary node、column、Q/Pi block、1-based mode、frequency、global row，及原 residual/scale/normalized scalar 的 bits。全状态是否改变、多少词改变、调用是否保持输入、原记录 norm 是否逐 bits 重现，都作为实际诊断，不预填答案。

## 8. 机器读取合同

- `result.json`：schema `actual73-iteration2-realized-noJ-trial-probe-result-v1`。
- `summary.json`：schema `actual73-iteration2-realized-noJ-trial-probe-summary-v1`。
- `input-binding.json.gz`：schema `actual73-iteration2-realized-noJ-trial-input-binding-v1`。
- `realized-trial-spec.json.gz`：schema `actual73-iteration2-realized-noJ-trial-probe-spec-v1`。

result 的 `summary`、`array_manifest`、`input_binding` 均为真实文件 descriptor。其 `completed` 只指一次原调用和完整记录成功；`evaluation_returned` 明确原调用是否返回；`original_noJ_evaluate_calls` 记录实际次数。`native_accepted` 和 `task_completed` 始终 false。

summary 的实际原范数字段是 `actual_original_noJ_norm`，argmax 字段是 `actual_noJ_residual_readback`。`actual_original_noJ_norm_equals_saved_trial_bits` 只报告本次与原 73 标量是否相同，不要求相同；独立精确消费者不得把这个诊断变为门。`original_evaluation_error` 与 `observer_io_failure` 分开保留。

完整来源 binding 包含原 context、九份原 snapshot 数组描述、完整保存 J descriptor、原方向 binding/完整 delta descriptor/checkpoint 身份、原 selected-trial 记录、真实 alpha。未把机器绝对路径写入这个便携 binding；内部 spec 可有本次读取路径。

## 9. CLI 与后续精确分解

```bash
python computations/geometry_20261115_fetch_actual73_realized_selected.py \
  --run-id 43657001633 --artifact-id 14141540502 \
  --artifact-name visible-mainline-nojprimalnative-43657001633-1 \
  --expected-size 1752742419 \
  --expected-sha256 3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9 \
  --out "$RUNNER_TEMP/actual73-selected"

P73="$RUNNER_TEMP/actual73-selected"
python computations/geometry_20261115_native_realized_trial_probe.py \
  --native-directory "$P73/native-noj-primal-current576-damped" \
  --native-result-sha256 ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394 \
  --snapshot-directory "$P73/native-noj-primal-current576-damped/iteration-002/snapshot" \
  --snapshot-result-sha256 2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92 \
  --direction-directory "$P73/native-noj-primal-current576-damped/iteration-002/qr" \
  --direction-result-sha256 9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff \
  --source-topic "$VISIBLE_SOURCE_TOPIC" --node-heap 6144 \
  --out "$VISIBLE_OUT/actual73-realized-trial"
```

取件命令保原冻结 transport parser 的全部五个显式 tuple flags；只传 `--out` 不满足该原 parser。新 adapter 的固定 `PIN` 与显式 CLI tuple 两者必须相同；没有放宽原元数据或 ZIP 校验。

由 Actions 对本次真实 `result.json` 算 SHA，再交独立 `exact_20261115_native_realized_step_affine_decomposition.py`。它读取真实 trial/base f64 词，精确形成 $h=\widehat y_{trial}-\widehat y_{base}$；保存的旧 signed-e 给理想 $r+\alpha A\delta$，新完整 J 作用只用于 $Ah$。差 $A(h-\alpha\delta)$ 包含原乘法、加法及 typed-array 存入的**整个状态形成效应**，不能仅命名为“最后加法舍入”。实际 no-J 残差与 $r+Ah$ 的差仍包括这个有限切向模型与原求值的差异，不能凭一轮输出自动给某种唯一原因。

该消费者的算术、完整行账和最终 scope 由其独立冻结源码负责。它不再次调用原 no-J，不重 J，不重乘 $J\delta$，不把小 exact 缺陷作为新的原生验收门。

对应完整合同见 `2026-11-15-actual73-realized-step-exact-decomposition-interface.md`。已冻结消费者为 52,459 B，SHA256 `3570aa9f6bb3b24eb28678a57f88b145a8725a3a7bda05fe14a0860e136c917d`；不预写其本次 result SHA。

## 10. 预算、失败保全与静态验证范围

本次原科学量严格为一次完整 576-stage no-J；不是十次试步，不是 baseline+trial 两次。可沿 69 单 no-J 的 35 分钟 step / 80 分钟 job 初始预算；精确消费者在其独立阶段有显式 1,800 秒预算。若同 job 合并两者，workflow 必须给两阶段真实总量留余量，不以时间截段替代完整原对象。

原 ZIP 必须完整下载核 SHA，但只保需要的约一轮 J/输入/方向/既有 e 账；没有原 32 轮因子空间需求。原件、完整新 raw、root gzip packets、源观察 receipt 和失败日志均保 artifact。publisher 的 Git 小件路由不得把 `large-arrays/` 原文件误当需要入库的文本。

本地已做三份源码 Python AST / Node syntax，以及 22 项纯 source-string 检查：三处观察可逆、原 worker loop 可逆、原 trial 表达式唯一、evaluate 次数为一、生成的观察模块语法有效、原源码 SHA 保留。`check_source_only.mjs` 只提取文本变换函数，在隔离上下文对原 source 文本操作；没有导入/构造任何科学 engine，没有设置假 Actions 环境，没有运行 root、RHS、ODE、J、trial 或精确点积。

静态验证不是本次科学结果。当前没有 probe result SHA、范数、argmax 或原 root 读数可报告；这些只在公开 Actions 完成后按真实输出登记。

主控完整读三源/接口，源码SHA不变；合并[83接线](2026-11-15-request83-workflow-handoff.md)使用120分钟job。22项源码文本检查见[原静态回执](2026-11-15-request83-source-roundtrip-static.json)，无本地科学执行。
