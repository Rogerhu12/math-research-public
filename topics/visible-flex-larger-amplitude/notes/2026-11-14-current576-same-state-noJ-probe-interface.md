# 第 69 轮：实际第 61 轮末态的一次原生 no-J 对照接口

作者：geometry；日期：2026-11-14。分类：独立诊断入口、来源与输出契约。

状态：两份源码已冻结，仅做 Python AST、Node 语法及源码字符串往返检查；尚未执行本轮科学计算。计算只允许在 `Rogerhu12/math-research-public` 的 GitHub Actions。此说明不是新的数学验收门。

## 1. 本轮回答的问题及准确范围

第 61 轮的第 3 个非线性迭代（零基编号）已经产生完整 fresh-withJ 快照。该点的原记录 `norm` 为 `0.00007952539043101878`，其后原十个 no-J 试步均未严格降低这个基准。前一接受 no-J 读数和下一次 fresh-withJ 读数不能混作同一评估序列；本轮补的是在**完全相同的最后完整原状态**上，调用一次原 `evaluate(states, target, false, scales)`，与该快照已保存的 with-J `out/r/cut/end/mean/norm` 逐段对照。

本轮不产生新 Newton 方向，不构造 `base + alpha * delta`，不重放十个试步，不调用 `TailClient.solve`，不求新的 Jacobian，不改变原几何、有限方程、根求解、RK、graphs/gains、Robin 边界、H、target、scales 或 guard。原 no-J 例程内部按原代码推进状态及求根，是本轮唯一的一次完整科学评估。原构造器和 ready/容量/来源握手仍真实执行。

本轮固定第 61 轮实际末态，不能用第 28 轮、初始第 59 轮、某个 rejected trial 或另一个保存状态替代。此前保存的 J 只有其原描述器被绑定；本轮既不读取完整 J payload，也不将它标为新 J。

## 2. 冻结源码与纯源码检查

两源放在本题 `computations/` 下并列；当前交付原件位于 `/tmp/current576-noj69/`。

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `geometry_20261114_current576_same_state_noj_probe.py` | 21,595 | `fc2c61d35e6eb3b1e8d836f46b75c7dc5ec2f2f69bcd483410a289434637099b` |
| `geometry_20261114_current576_same_state_noj_probe_hook.mjs` | 25,386 | `dd361d6fa63286bd4b27983a19783b1fcabc665cef9a79f1834b709b128f8478` |
| `pure-source-check.json` | 753 | `2f984acda99ab593d9077e67847351885629a5b5c57d606a07c2fb57cb52558e` |

纯源码检查包括 Python `ast.parse`、`node --check`、冻结 worker 唯一 import 插入点、原请求循环起止锚唯一、替换后撤销能够逐字还原。没有导入或执行原构造器、RHS、J、ODE、QR 或本轮任何数学函数。运行时 hook 还会记录实际编译后的 worker 原文/插入后原文/原循环/新循环 SHA 及再次精确还原结果。

这两源沿用冻结 `true_tail_client.py` 和 `seeded_zero_tail_client.py` 的原身份函数；后者只提供配置和 ready/source 比较函数，并不构造它的缓存 client。主 client 始终是原 `TailClient`，其 `calls` 应为 0。运行环境沿原 Python + NumPy 和 Node `24.22.1`，Node heap 参数默认 `6144`。不需要本轮 QR、SciPy 求解或任何额外数学库调用。

## 3. 已有真实父件与原件选取

父公开 Actions run 为 `43645948199`，artifact 为 `14136633570`，名称 `visible-mainline-current576native-43645948199-1`。完整 ZIP 是 2,335,870,174 字节，SHA-256 为 `7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469`。本轮无需在本地取该大包；工作流可在 Actions 上先核完整 ZIP，再只提取以下原件，保留原相对目录和原字节。选取不意味着整个 artifact 的全部 payload 已被本入口审计。

三个固定身份为：

- `native-current576-damped/result.json`：`b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef`。
- `native-current576-damped/iteration-003/snapshot/result.json`：`5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286`。
- 该 snapshot 的完整 `base-states` 原 f64LE 流：`b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013`。

### 3.1 native 根目录的 12 件

`--native-directory` 指向父件的 `native-current576-damped/`。必须保留：

```text
result.json
current-correction-summary.json
current-input-config.json
native_runtime-config.json
native_intent.json
native_ready.json.gz
native_capacity.json
original-live-identity-before-selected-seed.json
actual-current-method-identities.json
core-instrumentation.json
native_trace.jsonl
native_trials.jsonl
```

除 `result.json` 自身固定 SHA 外，其余 11 件均从它的原 `small_output_files` 描述器核文件名、长度和 SHA，不自行重写 JSON 或压缩包。`current-correction-summary.json` 的第 4 条真实记录必须对应 `native_call=1/nonlinear_iteration=3/snapshot_sequence=3`、上述状态 SHA 和上述 snapshot 收据。

### 3.2 第 3 轮 snapshot 的元数据与九个非 J 原数组

`--snapshot-directory` 指向 `native-current576-damped/iteration-003/snapshot/`。除自身 `result.json` 外，按其 manifest/context 收据保留：

```text
array-manifest.json
context.json.gz
core-instrumentation.json
flow-return-metadata.json.gz
```

再从 `array-manifest.json` 的 `arrays` 中选择以下 **九个**数组的全部 chunks。以原 `file` 相对路径提取，不将 gzip 重新命名，不截断 chunk，不通过 JSON 浮点转写 raw payload。

| 原数组名 | 完整 shape | 用途 |
| --- | --- | --- |
| `base-states` | `[577,224]` | 本次完整输入，含全部负零 |
| `stage-residuals` | `[576,224]` | 已保存的原 with-J r |
| `stage-out` | `[576,224]` | 已保存的原 with-J 流出值 |
| `original-scales` | `[1,577]` | 原始各节点 sigma |
| `cut-residual` | `[1,112]` | 原入口实际缺陷，允许非零 |
| `end-residual` | `[1,112]` | 原远端实际缺陷 |
| `original-far-graph` | `[1,112]` | 原远端 Robin 图 |
| `physical-height` | `[1,112]` | 原完整非零物理 H |
| `cut-target` | `[1,112]` | 原 H 转换后的 target |

每个数组按 `<f8`、C 顺序、实际 shape、chunk 索引/行覆盖、逐 chunk 长度/存储 SHA/raw SHA、完整 raw 流 SHA 检查。输入已保存求解数组须有限；正 sigma 保原原件规则。`stage-jacobians` 的 `[576,224,224]` 描述器及 raw SHA 仍在原完整 manifest/context 内绑定，**不用提取其 payload**。无须 QR 因子、方向、exact ledger、旧 28/41 大数组或 59 selected 原件。原 `rawNode` 保物理块索引 `[0,72,144,216,288,360,432,504,576]`，并非改成 577 个节点索引。

同一个 snapshot 内的 core 证据与 native 根目录原 core 证据 SHA 必须相同。保留 `flow-return-metadata.json.gz` 的完整 576 行原 meanHeight/minA/minD 数值记录，供实际返回对照；不用由省略的数据重算它们。

## 4. 可直接接工作流的 CLI

```bash
python topics/visible-flex-larger-amplitude/computations/geometry_20261114_current576_same_state_noj_probe.py \
  --native-directory "$ACTUAL61/native-current576-damped" \
  --native-result-sha256 b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef \
  --snapshot-directory "$ACTUAL61/native-current576-damped/iteration-003/snapshot" \
  --snapshot-result-sha256 5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286 \
  --source-topic "$PUBLIC78/topics/visible-flexible-closed-surface" \
  --out "$VISIBLE_OUT/current576-same-state-noJ-probe" \
  --node-heap 6144
```

`$ACTUAL61` 是上述选取后的完整相对根；`$PUBLIC78` 按既有固定公开 source restore 流程提供。`--source-topic` 下的 `repro/source-root` 继续传给原 client，实际 consumed sources、适配器 SHA、ready 数学语义和容量报告必须与父记录一致。所有必要计算源从本次固定 checkout 读取；没有私库取件或后台未记录计算。

输出目录必须新建且为空，并位于两个只读输入目录之外。原取件凭据仅 fetch/publisher step 需要，科学 step 不需要令牌。整个科学 step 不调用 GitHub API。原两配置的 I/O 字段允许改为本轮输出位置，其余 `numerical_configuration` 逐语义一致。当前 ready/source/config 核完后才发送独立的诊断协议请求。

## 5. 只有请求循环被替换

hook 在冻结 `tail_frozen_worker.mjs` 的唯一动态 import 前插入源码变换，保留原 worker constructor、capacity loader、零参考 ready 及相关加载顺序。变换只替换原 stdin 请求循环；其余编译后的源码精确往返还原。原 core 文件 SHA 固定为 `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`，原 `evaluate.toString()` SHA 固定为 `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。

真实现场检查全部 parameters、576 个 cells/profile breakpoints、graphs/gains/far 原字节、公开方法实际源码身份。状态从 raw chunks 写回 `Float64Array` 后逐原行 raw bytes 比对；负零保留。H/r^4 及原 scaleFor 递推只作原身份对照，实际评估仍接收保存的 target/scales。入口软缺陷与远端缺陷不被归零，也没有阈值将某个 H 系数当作 0。

只发送一个 `same_state_noJ` 消息，唯一数值调用为：

```javascript
ev = dn.tail.evaluate(states, target, false, scales);
```

这里不装第 61 轮的 R273 correction replacement，因为没有任何 solve/correction 调用。公开 `tail.solve` 箭头与原内部 correction 的区分照实际源保留，不伪造 `toString()`，不把原记录的 instrumented solve 内部 SHA 当作本次被调用函数。原 `evaluate`、RHS、根方程、RK、缓存实现和所有原 guard 都保持原文。

若原 evaluate 抛出 guard/根求解异常，记录原 message、stack、stage/rawCell/rawSegment（若原异常提供），完整已进入的状态/target/scales 仍保存；不补造未返回残差。若发生身份/I/O/协议异常，保留真实 launcher/worker stderr 和已有证据，并按该类异常报告。原 evaluate 返回后不会因两路径差异大小被另行拒绝。

## 6. 完整输出与数值声明范围

launcher 元数据主要为：

```text
same-state-noJ-spec.json.gz
probe-input-config.json
verified-launch-intent.json
diagnostic-stdout.jsonl
launcher-result.json
original-constructor_{intent,ready,runtime-config,capacity,stderr,...}
```

其中 spec 是完整 gzip，绑定所有父件 receipt、实际原数组 descriptors 和输入绝对位置；输入不被复制成另一个数学场。原 constructor 的具体文件名按原 client 自动生成并完整保留。

hook 输出：

```text
worker-instrumentation.json
actual-primal-method-identities.json.gz
summary.json
complete-stage-comparisons.json.gz
array-manifest.json
large-arrays/actual-evaluate-input-states.f64le
large-arrays/actual-evaluate-input-target.f64le
large-arrays/actual-evaluate-input-scales.f64le
large-arrays/original-noJ-stage-out.f64le
large-arrays/original-noJ-stage-residuals.f64le
large-arrays/original-noJ-cut-residual.f64le
large-arrays/original-noJ-end-residual.f64le
large-arrays/noJ-minus-withJ-stage-out.f64le
large-arrays/noJ-minus-withJ-stage-residuals.f64le
large-arrays/original-noJ-mean-height-increments.f64le
```

后七个实际返回数组及完整逐段对照只在原 evaluate 返回时产生；mean 数组另要求原全部 meanHeight 字段实际存在。所有 raw 数组属于 artifact-only 的 `large-arrays/`，不应逐轮发布 Git。元数据保存完整 bytes/SHA/shape/order/dtype，负零和实际非有限输出按原 raw bits 保留。数值 record 明确区分有限、负零、NaN、正/负无穷。

`summary.json` 的 schema 为 `actual61-current576-same-state-noJ-comparison-v1`。其 scope 包括：

- 原保存 with-J norm 与本次原返回 no-J norm，分别保其原 double bits。
- 全部 576 段原 `out/r/mean`、原 cut/end 与逐段不同字数、普通浮点差和原 sigma 下差，附完整位置/原值/新值。
- 对两套已存在残差按原 stage/far/cut 顺序进行只读 norm/argmax 诊断，给 stage/rawCell/rawSegment、Q/Pi、模态/频率、global row。
- 诊断重建 norm 与原标量是否同 bits 仅作为输出事实，不用作新通过门。
- 原 no-J aggregate `minA/minD` 的 `+Infinity` 占位按原数记录；不是失败，也不据此冒称缺失的逐段下界。原 no-J flow 的 minA/minD 未返回时明确写 `available:false`。
- 调用前/后完整输入 state/target/scales hash 和是否被原调用改变，只读记录，不改原输入。
- 原始函数和 profile/source/capacity 身份，以及请求循环精确可逆还原；不把 `Function.toString` 改装成另一个对象。

这些差、除以 sigma 的值和 argmax 是 **Actions 中的 binary64 诊断**，不是有理、区间或真实 DF 误差证书。结果固定保留 `native_accepted:false`、`task_completed:false`、`difference_cause_proven:false`。原评估正常返回时 launcher 退出 0；原评估抛出科学异常时该摘要仍尽可能完整、launcher 退出 2；身份/I/O/程序异常另行非零并保原 traceback。`always()` artifact 应保存全部已产生文件，不能以 job success 冒完整原生收敛。

## 7. 源码已确认的差异与下一步判读

原两路径共享 lexical `evaluate`，但 `withJac` 分派不同的流推进方法：true 调 `engine.flowStateWithJacobian`；false 调 `engine.rk4`。两者均为 JavaScript Number/Float64Array 的 binary64 算术。实际 stage 的原逐角 root/RHS 方程、guards 及 profile 并未因此换成另一份数学模型。

已读冻结源码存在可具体定位的有限算术差别：ordinary 的 true 路径使用 `x=n*(1/steps)`，false 使用 `x=k/steps`；若干中间态使用 `(h/2)*ds` 与 `h*ds/2` 的不同括号。带 cusp 时，true 的整 profile `integrationGrid` 与 false 的逐普通区间 `withCuspAwareRK` 对原断点的拆分路径也须按原字节区分。原 engine/profile 有复用及按 x 的几何 memoization，但尚未用本次实际对照证明哪一项量化解释最后 norm 差。

因此本轮先保完整配对数组。若证据支持后续统一 primal 的独立有限算法，应将统一的 step schedule、根/RHS、状态括号及均值路径明确作为新的有限实现身份，并保持原方程/容差/guards、真实最终 audit；不能把新实现冒成旧保存 J 的逐字延续。当前不预选这个改法、不预选 eta、不运行新的求解，也不把本次可能出现的路径差异直接宣布为第 61 轮全回溯拒绝的唯一原因。

## 8. 关联现有原件与结论

- [第 61 轮实际原生循环和试步失败](2026-11-14-actual61-current-native-loop-and-trial-failure.md)。
- [第 61 轮四个 fresh QR 模型与原尺度 exact 读回](2026-11-14-actual61-four-current576-QR-models-and-exact-readback.md)。
- [同一 g 的精化入口及当前缺口](2026-11-14-same-metric-live-refinement-entry-and-current-gaps.md)。
- 冻结源码：本题 `computations/geometry_20261114_current576_same_state_noj_probe.py` 和同名 `_hook.mjs`。

本接口完成的是第 69 轮可直接调度的单次配对评估，没有宣布任何新的数学或原生求解成功结果。
