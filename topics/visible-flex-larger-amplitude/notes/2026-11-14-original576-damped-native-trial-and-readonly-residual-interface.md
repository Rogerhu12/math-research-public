# 原 576 段 R273 方向：原十试探与完整只读残差记录接口

- 作者：geometry agent
- 日期：2026-11-14
- 分类：可执行接口；源码与语法已核；本接口冻结时尚无 request59 科学结果
- 对应理论：[R273](../results/R273-complete-native-damped-square-root-chain.md)
- 前一实际结果：[actual57 原十试探](2026-11-14-actual57-original-ten-trial-no-decrease.md)

## 1. 本次对象和范围

新入口应用本次 **原 576 段完整保存系统**产生的一个 R273 阻尼方向。输入是 actual28 的原 J、完整 residual、cut、far、H、原 sigma 及同一基态；没有新 RHS/J/ODE，也没有把 actual57 的 1372 段方向或其 577 节点限制重贴新标签。

上游生产者是 `exact_20261114_original576_damped_chain_qr.py`。方向是完整原坐标的 `[577,224]` 数组，已经恢复 sigma 列坐标。原 cut/far 是 R273 目标中的软行，因此方向的 cut/far 分量可能不为零；试探必须原样使用，不能投影或改零。H、far graph 和 sigma 本身保持原字节。

本入口只做一次原始十步长线搜索。原 worker 首次 `initial` 注入同 actual23/28 完整基态，并置 `predicted=true`；原 first-with-J baseline 调用被明确替换为 actual28 已保存结果，first-correction 调用被完整新方向替换。原十试探正文、原非线性 no-J 求值、guard、严格范数下降、原失败语句都保留。

任何首次接受只产生可继续的完整 selected state。随后计划停止，不进行下一次 Newton 迭代、端点 J 或 fresh audit，不声明达到原 native 容差或课题完成。

## 2. 冻结来源

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_native_original576_damped_trial_replay.py` | 28,401 | `c337d880c29aaa865b6516fd679ffffe9410d30c893ff2f8e0cc4092f6adbec7` |
| `geometry_20261114_native_original576_damped_trial_replay_hook.mjs` | 68,273 | `c104ff11b356cb3993ffd5ae97988259b2f27c91e492c7736d7a96a9ad450e36` |
| `exact_20261114_original576_damped_system.py` | 10,616 | `c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207` |
| `exact_20261114_original576_damped_chain_qr.py` | 27,828 | `e1a35bd82433cfe6525047cb3ceb3d0c434c1ebaa62680cb0f1fdab0e76cfaec` |
| 借用的 `exact_20261114_native_damped_chain_qr.py` | 42,340 | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |

新 producer 顶层、原生方向 checkpoint 的 source 是 `e1a35…`；其 `factor_engine_source_sha256` 保留真实借用的 `9b951…`。两种身份不能混淆。

actual28 原 `result.json` 固定为 `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。本次方向 `result.json.gz` 必须实际生产后计算 SHA，由 CLI 传入；本接口不预填未来值。

## 3. 完整方向身份

Python 只构造 `Original576System(capture_directory)` 作已保存文件、分块、原字节和完整输入身份核对。它不调用 QR、原 native、RHS、J、ODE 或新残差计算。原 576 个 J 块仍需流读核完整来源，不能只拿一份小摘要冒完整输入身份。

新绑定 schema 是：

```text
actual28-original576-complete-linear-system-binding-v1
```

其中保存原 `CapturedArrays.binding`、原 9 个非 J 数组、完整 576 块清单、全 J 流身份、原边界/尺度以及新的 canonical matrix identity。`old_to_new` 是 `0..576` 恒等映射，不是 1372 段布局。

方向输出 schema：

```text
complete-native-original576-damped-square-root-direction-v1
complete-native-original576-damped-direction-arrays-v1
complete-native-original576-damped-direction-v1
```

依次用于 `result.json.gz`、`output-array-manifest.json.gz` 和 `native-direction-checkpoint.json.gz`。实际所用方向描述器是 `native_delta`，数组名 `complete-original-coordinate-delta`，shape `[577,224]`。checkpoint 保 `M=112,K=224,depth=original_depth=576`、恒等映射、完整 rows、每行 `negative_zero_columns`、原坐标 f64 SHA、eta 与 model scope；**没有 step_depth，也没有 restriction checkpoint**。

Python 和 Node 都将负零 sidecar 恢复后，与 raw 577×224 方向逐字节核对。完整 manifest 的所有描述器绑定在文件 SHA 中；真正重读的数值 payload 只有这一完整方向，不重新读取 QR 因子，也不声称已独立审过这些因子。factor inventory 的 129248 行、129248 列、258496 augmented rows、576 stages、577 nodes、577 个 penalty block 和129248个纯常数行只核完整生产者合同。

eta 由上游明确选取；本次工作流选择 `--eta 1`。trial CLI 不重选 eta，也没有 `--expected-eta`。它绑定实际 `eta_cli_text`、binary64 值/位和 checkpoint/spec 中的同一记录。L2/model gradient、exact linear defect、triangular diagonal 等数值都不作为新增试探门。

## 4. 原始调用及完整只读观察

### 4.1 原试探保持

原十步长仍为 $1,1/2,\ldots,1/512$，仍由原循环形成候选数组，并调用原 `evaluate(trial,target,false,scales)` 一次。记录器自己不形成 `base+alpha*delta`，不重新调用求值器，也不补一次 baseline。

原基态范数仍取 actual28 保存的 with-J 数值和 bits，明确标为 cached。原 trial 的目标、所有 stage/far/cut 残差、原 sigma 范数和原 guard 都由真实原代码求值。严格下降才选择状态；一轮全部拒绝则返回原 line-search-failed 消息。

### 4.2 两个只读插入点

在原 `evaluate` 的函数入口、任何原 stage flow 前，插入 `beforeNoJ`。在原完整 return 前插入 `afterNoJ`。两者仅对 `withJac=false` 启用；原返回语句及所有数学运算原文不变。

`beforeNoJ` 保存实际传入的全 577×224 states、target/sigma/far 来源 SHA，并记录相对原基态的逐字变化数、变化节点数和最多32个原始 word 对照。这个对照只比较 bits，不计算新候选或新的物理差量。

原 Float64Array 直接复制底层字节为 little-endian f64；负零与非有限 payload 保留。非有限 trial input 仍交原求值器处理，记录器不增加 finite-domain veto。保存元数据中的有限/非有限计数也不改变原验收。

若原求值器完整返回，保存：

| 数组 | shape | 来源 |
|---|---:|---|
| 实际 trial input | `[577,224]` | 原函数实际传入的数组 |
| 全 stage residuals | `[576,224]` | 原返回的 `residuals`，直接复制原字节 |
| far residual | `[1,112]` | 原返回的 `end`，直接复制原字节 |
| cut residual | `[1,112]` | 原函数未保留 cut 数组；返回后只读重写同一 `states[0][j]-target[j]` 减法，明确标记此范围 |

完整 `norm/minA/minD` 按原返回值及 f64 bits 保留。no-J 路径的 `minA/minD` 原为 Infinity 占位符，不能称其为实测 guard 裕量。

若原求值器在某 stage 抛错，完整 trial input 已在调用前落盘，原 callback 的 stage/rawCell/rawSegment/error 保留；不能伪造未返回的完整 residuals 或 norm。已有的原失败 stage input 记录也保持。

### 4.3 原尺度 argmax 诊断

记录器只读扫描已返回的 stage/far/cut residual，用相同 `Math.abs(r)/sigma`，按原 stage→far→cut 次序记录首次及全部并列最大位置。位置记录包含 global row、stage/rawCell/rawSegment、Q/Pi、mode、frequency、原 residual/sigma/scaled 值与 bits。

同时记录扫描范数与原返回 norm 的 bits 是否相同，**不将该相等关系或扫描结果用作门，也不替换原 norm**。全部 ties 和非有限行可放 gzip payload；遇 NaN 时明确 argmax 未定义。此设计区分全状态不变、非最大行改善、最大位置切换及原 guard 失败，冻结时不预定任何一种是 actual57 范数不变的原因。

### 4.4 原生事实和记录失败分开

原 evaluate 的实际进入数与返回数由两个观察点直接计数；不从完成回调数量推测。完整每次记录以原 trial callback 收尾。如果记录器文件写入、来源或序列检查发生问题，单列 `READONLY_TRIAL_OBSERVER_FAILURE` 与 `trial-observer-failure.json`，不把它冒作原数学 guard。

十次完整返回的新增 raw input/residual/cut/far 总量约20.7MB，全部放独立 `large-arrays/`，只归 artifact。所有数组有大小、shape、dtype、order、SHA和负零/非有限计数。每次小 JSON/gzip 记录完整引用；不删物理状态或残差来压缩报告。

## 5. 真实源码身份：不伪装 Function.toString

实际 public `tail.solve` 仍是原 split-adapter wrapper。实际 public `evaluate` **确实含两个只读插入**，其 `Function.toString()`、源全文和 SHA 单独保存并与实际 compiled source slice 核对。

另存恰好去掉两观察插入后恢复的原 evaluate 源，并把它作为与 actual23/28 旧 identity 的显式比较视图。新文件名是：

```text
restored-original-mathematical-identity-before-seed.json
actual-replay-method-identities.json
core-instrumentation.json
```

第一件只表示恢复后的原数学来源比较，不谎称 actual evaluate.toString 未改。后两件保实际 instrumented 源、原参考源、全部插入/替换、精确逆变换和来源 SHA。没有覆写函数的 `toString`。

已完成的纯文本验证将原 frozen engine 两处既有 source replacement 应用在原 core 文本上；重建 runtime core SHA 为 `f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f`，与 actual57 保存的原 runtime core 相同。再对新插入做精确往返：

| 范围 | SHA256 |
|---|---|
| 原十 trial 正文（新入口逐字保持） | `603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99` |
| 去观察后的原 evaluate | `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9` |
| 实际待编译的 observed evaluate | `cff3bf72887e95ead5623a60c4d04875ed7787cb5ec200dad6cf542fe5371606` |

这些检查只操作源字符串和语法。没有导入原数学模块、运行 constructor/native/RHS/J/ODE/solver、读新方向数据计算范数或生成候选。

## 6. CLI 与工作流合同

方向实际完成后计算真实结果 SHA。以下变量由工作流绑定已校验的原件，历史17/19/21/22/23路径沿原57接口；59 trial 不再需要41/54目录，也不直接消费57 QR目录。

```bash
C=topics/visible-flex-larger-amplitude/computations
QR_OUT="$VISIBLE_OUT/native-original576-damped-chain-qr"
QR_RESULT_SHA=$(sha256sum "$QR_OUT/result.json.gz" | cut -d' ' -f1)

python "$C/geometry_20261114_native_original576_damped_trial_replay.py" \
  --failed-directory "$FAIL17" \
  --cold-probe-summary "$COLD19" \
  --first-candidate-summary "$FIRST21" \
  --v2-candidate-summary "$V2_22" \
  --candidate-directory "$CANDIDATE23" \
  --capture-directory "$CAP28/native-correction-capture" \
  --direction-directory "$QR_OUT" \
  --direction-result-sha256 "$QR_RESULT_SHA" \
  --source-topic "$SOURCE_TOPIC" \
  --node-heap 6144 \
  --out "$VISIBLE_OUT/native-original576-damped-chain-original-trial"
```

Python spec 用完整 gzip 保存，Python/Node/launch/result 均绑定压缩文件 SHA，另记 raw JSON 大小与 SHA。Node 按 magic 解压。没有新增运行包：沿用原绑定器的 NumPy、原 TailClient 依赖及 Node24.22.1；trial 不调用新 QR 或 SciPy。

`result.json` schema 为 `original-native576-damped-trial-replay-result-v1`；小 summary 为 `original-native576-damped-trial-replay-summary-v1`。真实一轮接受保存完整 selected f64 gzip、全 rows/负零 checkpoint 和来源，随后计划停止标记：

```text
VISIBLE_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_ACCEPTED_STOP_V1
```

退出0表示这一原线搜索确有接受并观察到计划停止；**不表示 native 或课题完成**。十次拒绝保原失败并退出2。两种情况下始终上传完整 artifact。selected 的 `success/converged/native_tail_response/endpoint_J_computed/fresh_endpoint_audit_computed/task_completed` 均保持 false。

## 7. 已付与未付

已付：源码静态合同、Python AST、Node syntax、generated insertion program syntax、实际原 runtime source 重建、完整core/solve/evaluate插入精确逆变换、原十 trial 正文逐字身份。旧 `validate_capture` 仍原样消费 actual28 `result.json`。

未付：本次实际方向、其原十 trial、任何 selected state 或完整 native/J/audit；这些都须等同一公开仓库 Actions 的真实回执。本接口不把新原576表示必然更好、eta=1必然可行或 actual57 唯一失败原因当成已证结论。
