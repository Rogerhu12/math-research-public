# 从 actual59 选中状态继续完整原生循环：current576 R273 接口

- 作者：geometry agent
- 日期：2026-11-14
- 分类：完整可执行接口；仅作源码、语法与原文往返检查；冻结时 request61 尚未运行
- 理论：[R273 完整阻尼平方根链](../results/R273-complete-native-damped-square-root-chain.md)
- 实际父输入：[actual59 原生首步与完整状态审计](2026-11-14-actual59-original576-first-native-step-and-state-audit.md)
- 父方向与原尺度账：[actual59 完整 QR 与两个 exact 读回](2026-11-14-actual59-original576-QR-and-two-exact-readbacks.md)

## 1. 本次执行的对象

actual59 的一次原始试探已经真实接受 $\alpha=1$，原范数从 `0.04177307820740199` 降到 `0.0001289424025918576`。完整 577×224 状态 raw SHA256 是：

```text
384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03
```

这个接受事实只说明一步严格下降。actual59 随后按其设计停止，没有达到原 native 容差、没有完整 endpoint J 或 fresh audit。本入口用这一真实状态继续原来的完整非线性循环，不将 selected checkpoint 改写为成功响应。

每次原 `evaluate(states,target,true,scales)` 完整返回、原范数仍未达到原容差时，唯一原语句

```javascript
const cor=correction(ev,states,target);
```

被同步 current576 R273 校正调用替换。新校正使用**当轮实际返回的完整 J、r、cut、far、sigma、H 与 states**；没有 actual28 的旧 baseline、旧 J 或旧 residual 替代当前值，也没有将旧 1372 段对象改标签。

随后仍由原代码形成十个候选，步长为 $1,1/2,\ldots,1/512$；原 no-J 求值、原 guard、严格原范数下降、原线搜索失败语句、原 `maxIterations=32` 和 `solveTolerance=2e-9` 保持。这里不对 L2、exact 线性缺陷、因子对角等诊断另设非线性接受门。

最终完整 endpoint sensitivity、height-jet Jacobian、原 finite audit 与原客户端最终检查都保持。R273 阻尼只作用于非线性方向，**不用于最终灵敏度方程**。即使非线性残差过线，若后续原 J 或审计失败，整个请求仍按真实失败保存，不称完整 native 成功。

## 2. 冻结源及原算法身份

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_native_current576_damped_solve.py` | 25,983 | `06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b` |
| `geometry_20261114_native_current576_damped_solve_hook.mjs` | 44,103 | `0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc` |
| `exact_20261114_current576_damped_system.py` | 22,749 | `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90` |
| `exact_20261114_current576_damped_chain_qr.py` | 21,013 | `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f` |
| 借用的 `exact_20261114_native_damped_chain_qr.py` | 42,340 | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |

完整原 finite array 整数核仍为 `exact_20261114_native_allrows_dyadic_residual.py`，SHA `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。该核的实际 exact 行账属于已保存有限数组；不自动升级为精确连续导数或真实非线性下降的证明。

launcher 硬钉 current adapter/QR 的实际 SHA；adapter 反向核定固定 basename 的 launcher/hook 当前字节，避免硬编码 SHA 相互循环。工作流另外钉全部发布源。原 78 个公开数学源由原 TailClient 的 public restore、source manifest 和 original ready 继续完整核验。

关键原身份：

| 对象 | SHA256 |
|---|---|
| 原 core 文件 | `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3` |
| 原 frozen engine 两项既有改写后的 runtime core | `f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f` |
| 原实际 `evaluate` | `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9` |
| 原 internal `solve` | `d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615` |
| 原十试探正文 | `603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99` |
| 原公开 split `tail.solve` 包装 | `283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a` |
| 原完整 `dn.solve` 包装 | `f80eaeff1cd31347ddfa9132fa42ff7b330297dc9fd37383b8727fb48ea46b8e` |

hook 记录真正插入后的 internal solve 原文与 SHA，并保留可逆还原的原比较文本。它不覆盖 `Function.toString`。公开 `tail.solve` 是 split 包装，不冒称其 `toString()` 就是内部已插入的 solve。

## 3. 最小 actual59 输入与恢复

`--selected-directory` 指 actual59 trial 原目录。需要以下 13 件文件；全部通过 actual59 固定 `result.json` 的完整 small-file inventory 核对原文件 SHA 与字节数：

```text
result.json
trial-replay-summary.json
trial-replay-spec.json.gz
selected-state-checkpoint.json.gz
selected-state.f64le.gz
trial-input-config.json
native_intent.json
native_ready.json.gz
native_capacity.json
restored-original-mathematical-identity-before-seed.json
core-instrumentation.json
actual-replay-method-identities.json
native_trials.jsonl
```

主要原件：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `result.json` | 10,047 | `c0a9b191e843e9036e84707ffa1855d5881dce13e4b71bf94812e9526b59d00e` |
| `trial-replay-summary.json` | 5,762 | `770b97e62eda7cbcc10b045c42298b95ef2c55a0f2dd5ac1930690175a156709` |
| `selected-state-checkpoint.json.gz` | 1,255,992 | `7659016c0218b8c2e9ba220ca81a0b410b7e38005ea609e417b9b534d76c3556` |
| `selected-state.f64le.gz` | 954,571 | `8ade070f746caed9a45c582c7485a060e55ee589858f5f88255d8ffd0d9112cb` |

完整 raw 是 1,033,984 bytes。Python 与 Node 各自恢复全部 checkpoint 行和 `negative_zero_columns`，与 raw 全字节核对，保实际 8 个负零。Node 原 worker 第一次声明 `let initial,predicted=false` 后，仅注入这个完整状态并置 `predicted=true`。原 worker 的 `last`、`tangentPredictor` 仍为 null；不把未完成响应装入缓存。

`predicted=true` 仅避免原首次初始化分支再作 amplitude/cut 修补，不表示已有旧 worker 的 tangent predictor。没有 `initialCheckpoint` 几何重映射，没有 H 截零、阈值截频或更换材料数据。**不要求、也不强迫 selected `Q0` 等于 target**；actual59 方向的 cut/far 是软行，它们的真实缺陷保留。

原实际 `rawNode` 是物理分块索引

```text
[0,72,144,216,288,360,432,504,576]
```

它有 9 项。577 是 shooting states 的节点数，不是 `rawNode` 的长度。两者均原样保留。

启动不需要 full actual28、actual17–23 历史大包或 actual59 QR 因子；完整历史经 actual59 已锁定的小原件和正式审计承接。原 TailClient 通常所需的 public78 源和两份 frozen calibration 资产仍照原链恢复，不能省略。

## 4. 每轮当前 with-J 快照

每个实际发生校正的原迭代目录为：

```text
iteration-000/
  snapshot/
    core-instrumentation.json
    flow-return-metadata.json.gz
    context.json.gz
    array-manifest.json
    result.json
    large-arrays/...
  qr-launch.json
  qr.stdout.log
  qr.stderr.log
  qr-exit.json
  qr/...
  returned-correction.json
```

`result.json` 最后写入，只在整份 snapshot 完成后出现。失败不补造缺失数组。所有原数组直接复制实际 Float64Array 底层 little-endian binary64 words；负零与实际非有限 payload 不先经 JSON 改写。

| 数组 | shape | 来源 |
|---|---:|---|
| `base-states` | `[577,224]` | 当前原 solve 的 states |
| `stage-residuals` | `[576,224]` | 当前原 `ev.residuals` |
| `stage-out` | `[576,224]` | 当前原 `ev.flows[n].out` |
| `original-scales` | `[1,577]` | 本次原 `scaleFor(target)` 的实际 scales |
| `cut-residual` | `[1,112]` | 原 evaluate 未存数组；只读用同式 `states[0][j]-target[j]` 留副本 |
| `end-residual` | `[1,112]` | 当前原 `ev.end` |
| `original-far-graph` | `[1,112]` | 原 `graphs[576]` |
| `physical-height` | `[1,112]` | 同一完整请求 H |
| `cut-target` | `[1,112]` | 当前原 target |
| `stage-jacobians` | `[576,224,224]` | 当前原 `ev.flows[n].J` |

J 每四段流写一个原 raw chunk；其它数组也按原行顺序分块。manifest entry 保 name、dtype/order、完整 shape、total bytes/raw SHA、completed 和每个 chunk 的 array/index/row range/file/bytes/SHA。所有 raw 都在 `large-arrays/`，只进 Actions artifact，不逐轮送进 Git。

`flow-return-metadata.json.gz` 另保原 576 个 returned `meanHeight/minA/minD` 数值及 bits，包含 rawCell/rawSegment。它不是新流积分，也没有增加第十一个数学数组。

首次实际 correction 的 `base-states` 必须是 actual59 selected raw SHA；后续迭代只绑定其真实当前状态，不要求继续等于父状态。H、原 sigma、far graph 与 target 的原 bytes 身份固定；cut/far residual 不要求为零。

### 4.1 当前 schema 与来源

```text
current-native576-withJ-snapshot-result-v1
current-native576-withJ-snapshot-context-v1
current-native576-withJ-snapshot-arrays-v1
```

context 包含完整 `original_sources`、`numerical_configuration`、parameters/rawNode/cells、graphs/gains/far SHA、全部 raw array SHA、actual59 父四件收据、当前 core 插入记录，以及 `native_call/nonlinear_iteration/snapshot_sequence`。

父数 MB selected payload 不在每轮重新复制；每轮 snapshot 自己的完整当前 states 原 bytes 独立保存。`current_state_sha256`、snapshot result/context/manifest SHA 是本轮实际生成，不能预填未来值或套用 actual28。

### 4.2 with-J 与 no-J 的 minA/minD

原 product-flow 的 with-J 路径在每个 RK 子级读取 `rhsWithJacobian(...).root.e.minA/minD` 并归约，所以它们与 no-J 路径的 `+Infinity` 初始占位符来源不同。但原 D/S/A guard 使用 `>floor`，源码未把所有非有限情况单独声明为这个元数据的统一 finite 定理。因此适配器不新增 minA/minD 必须有限的门。

记录使用与冻结 byte helper 相同的 `numberRecord`：原 `float64le_hex`；有限值保原 JSON 数；非有限 `value:null`；分类精确为 `NaN`、`positive-infinity`、`negative-infinity`、`negative-zero` 或 `finite`。只核 record 与其原 words 相符。当前残差 norm 及 QR 所需完整数学数组仍须满足有限输入合同；这与记录 guard 元数据的范围不同。

## 5. 同步 JS → Python → 当前方向

Node 用 `spawnSync`、`shell:false` 调新 QR CLI；stdout、stderr 是当轮独立文件描述符，不转发给原 worker 的 JSON stdout 协议。没有通过 shell 拼接命令，没有把 child 输出混作 native response，也没有额外求一次 baseline、RHS、J 或 ODE。

```bash
python computations/exact_20261114_current576_damped_chain_qr.py \
  --snapshot-directory "$ITER/snapshot" \
  --snapshot-result-sha256 "$ACTUAL_SNAPSHOT_RESULT_SHA" \
  --eta 1 \
  --out "$ITER/qr" \
  --max-factor-bytes 2147483648 \
  --exact-workers 2
```

consumer 的新 binding 是 `current-native576-complete-linear-system-binding-v1`。其 constructor 只核当前已保存 bytes、有限输入、schema 和来源，不执行原 RHS/J/ODE 或 QR。真正因子计算在新 entry 中调用冻结 R273 引擎；factor 源身份仍是 `9b951…`，不能写成新 entry 自己重新实现的算法。

方向输出：

```text
complete-native-current576-damped-square-root-direction-v1
complete-native-current576-damped-direction-arrays-v1
complete-native-current576-damped-direction-v1
```

分别用于 QR `result.json.gz`、gzip array manifest、`native-direction-checkpoint.json.gz`。实际 `native_delta` 是完整 `[577,224]` 原 Q/Pi 坐标，已经恢复 sigma 列坐标；它不是某 1372 方向的限制。两端逐字核 current snapshot result/context/manifest、完整 binding、current state、原 sources、source producer、eta、matrix identity、raw delta 和 checkpoint 负零。

bridge 不重新读取所有 QR 因子做第二次数值求解，也不冒称自己独立审过因子。完整因子、纯常数、formed model、exact 行账和原输入副本保留在当轮 QR artifact 中，供真实回执后审计。新方向只按其实际完成、完整有限数组及来源交给原十试探；不以 model L2 或 exact 缺陷大小作为新增门。

原 Riccati `maxChartCondition` 在这个校正方法中没有计算，因此返回 `null` 并明确记录，不能伪填 0 或冒称它是当前全系统条件数。原 history/progress 可原样保留这个诊断值；数学返回的 delta 完整不变。

## 6. 完整原循环、最终审计及记录边界

### 6.1 `native_call=1` 的精确含义

这里是一个真实原 worker protocol 请求，带完整 H、`jacobian:true,audit:true`。`native_call=1` 是该请求号，不是非线性迭代数。每轮另外记录原 `it` 和 snapshot sequence。

已只读核原调用链：`createCompactTailDN.solve` 先调用一次 `tail.solve`，随后 `cutJets`、`audit(sol)`、`heightJetJacobian`。`audit` 遍历真实 physical jets 与原 RK，并不调用 `tail.solve`；`heightJetJacobian` 使用 `tangentGraphAtCut` 和 cut 上正负扰动，只在缺保存 J 时可能 `evaluate(...,true)`，不调用 nonlinear correction。frozen `actualSlopeJacobian` 包装调用实际 cut 局部 J 与 tangent graph，也不重新启动 native solve。

因此当前原 final audit/endpoint 路径没有第二次 protocol 请求或第二个 nonlinear solve，不需要把其假造为 `native_call=2`。同时，单个请求内部的所有原循环迭代仍完整执行。若未来源的调用结构变化，必须新 source identity 明确适配，不能静默沿用本合同。

### 6.2 本次实际保存范围

每个到达 correction 的当前 with-J 迭代完整保存 states、J、r、out、cut、end、H、sigma/far 和 returned flow 标量。原 solver 若在容差分支直接 break，那个最后 with-J 不由 bridge 额外复制一套完整 J；原 progress/response、已保存线性化和最终 J 流程仍原样执行。

本入口没有 actual59 的两个 no-J observer 插入；**不声称导出了本次每一个 no-J 候选的全 577 states 和全部 r**。原 trial callback 的 alpha、norm、guard 和原失败段数据仍保；原 frozen accepted-trial recovery 继续保存真实选中的状态。完整 current states/r/J 捕获发生在下一次到达 correction 的真实 with-J 点。当前源码中 `evaluate` 原文完全不变。

若原 line search、当轮 with-J、QR、最终 sensitivity 或 audit 失败，失败对象分别保在原 native trace/iteration/response、当轮 snapshot/QR stderr/partial factors 或 bridge-failure；没有 planned one-step STOP。只有原 TailClient 真正返回完整有效响应且 worker 成功退出，launcher 才置 `native_accepted:true`。

这仍只是本次完整有限尾的 native 成功；`accepted_prefix`、`complete_tail_matching`、课题 `task_completed` 不随之置 true。

## 7. 顶层 CLI 与资源

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_native_current576_damped_solve.py \
  --selected-directory "$ACTUAL59_TRIAL" \
  --source-topic "$RESTORED_SOURCE_TOPIC" \
  --eta 1 \
  --node-heap 6144 \
  --exact-workers 2 \
  --max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/native-current576-damped"
```

`ACTUAL59_TRIAL` 可来自已公开原 trial 小目录；`RESTORED_SOURCE_TOPIC` 仍按原 public78恢复链，含 `repro/source-root`。计算段不需要 GitHub token；取件/出版依旧由工作流各自处理。

静态 shape 字节预算：每份当前十-array snapshot 为 234,318,472 raw bytes，其中 J 为 231,211,008 bytes。冻结 R273 引擎按 $D=576,K=224$ 的完整 factor/constant 公式为 464,891,392 bytes；另有 QR 输入副本、direction、exact ledger、JSON/gzip 和日志，不能只按这两项之和称全部输出上限。

资源预算应覆盖原最多 32 次校正的真实完整输出。Node heap、因子存储上限和 workflow 时间是显式资源设置，不改原 32 迭代、原十步长或原 scientific 门。所有逐轮大 raw 和因子保持 artifact-only；publisher 需递归识别每层 `large-arrays/`。小元数据也不得截断字段来假装完整现场。

## 8. 本地验证范围与最终差异

已完成 Python AST、Node syntax；另外纯字符串重建原 frozen runtime core，再执行新源码改写程序及反向还原。没有 import 原 native/scientific 模块，没有调用 constructor、RHS、J、ODE、QR、norm 或候选算术。

纯文本检查确认：唯一 correction 语句可逆；原 evaluate 与十试探正文 SHA 完全相同；原 full solve 其余字节和 final sensitivity/audit 源未变；loader 插入可逆；first-initial 插入程序语法及 source-only fixture 往返通过。实际 current snapshot 和 QR 身份须等 Actions 原件产生，不能由这些源码检查预先宣称通过。

相对 root 已读 launcher SHA `494df5a2a30831d2d3237dd49dde3d996e74c03e681bbc9f3ec9ad4eb7d0f7d8`，最后只将两处未冻结的 source 占位替换为真实 `695c2…/ac048…`。相对 hook SHA `173645a7df42ae814ddc800bdcbfb7f1229ca4f61080a925bd47c75a3a8f7e77`，最后只对齐 numberRecord 的 JSON 值与分类名称；原数值 bits 和算法表达式未变。

本接口冻结没有新数值回执，不预测完整 native 必定成功。后续必须根据真实每轮状态、方向、原十试探及最终 J/audit 报告继续。

## 9. 终端中断后的文本保全

本接口已写入暂存文件，但在取其首次 SHA256 前终端不可用。此发布文本从完整已写内容恢复，并新增本节说明；没有声称与尚未取 SHA 的旧暂存文件逐字相同。两份运行源码分别重新计算完整 UTF-8 SHA256，确与终端已冻结的 `06b8c44c…`、`0933ee81…` 完全一致，既有 AST、Node syntax 和纯源码往返检查仍对应这两份字节。接口经小于 100KB 的纯文本 blob 保全，不在 connector 中运行科学计算，也不改 branch/tree。
