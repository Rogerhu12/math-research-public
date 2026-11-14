# Actual55：actual54 保存方向的原十次非线性试探全部被拒绝

- 分类：**数值证据**；原公开 Actions 的真实失败回执及独立字节审计。不是存在性证明，也不是新接受的 tail 或闭曲面。
- 作者：ChatGPT / exact_refinement。
- 日期：2026-11-14（UTC）。
- 科学计算位置：本公开仓库 Actions run [43636504089](https://github.com/Rogerhu12/math-research-public/actions/runs/43636504089)，source `6b7e9846ab9062614618856d4d6772c847a303c2`，job `132574360104`。
- 独立审计：[actual55 byte audit](2026-11-14-actual55-original-ten-trial-rejection-byte-audit.json)。本地只读取已保存值、核文件/原始字节/源码文本，没有计算 $y+\alpha\delta$、RHS、Jacobian、范数或有理残差。

## 1. 本次确定的结论

actual55 真正把 [actual54 的完整新 1372 段系统方向](2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md) 限制到原 577 个节点，交给原 native 十次 line search。原 trial 循环、每次 `evaluate(..., false, ...)`、guard 与严格原 norm 判据均保留，原目标 $H$、far graph、graphs/gains/scales 和容差保持原身份。

十个步长 $1,1/2,\ldots,1/512$ 全部在原非线性求值内部失败。其中九次记录为 `momentum branch D/S/A rejected`，一次记录为 `momentum Newton line search failed`。**没有任何一个 trial 返回完整的 `trialNorm`，因此本次证据不是“十个完整残差都没有下降”，而是这十次候选都没有完成原求值及其后面的完整 merit 比较。**

最终保存的原错误为：

```text
Error: multiple-shooting line search failed at 0.04177307820740199
```

结果明确记录 `replay_completed=true`，但 `trial_accepted=false`、`native_accepted=false`、`selected_state=null`、`task_completed=false`。`worker_exit_code=0` 只表示按预定协议完整保全了这次拒绝回执，不能解释为数学求解成功。

## 2. 本次计算与缓存各是什么

本次只复用已经完成的两个对象：actual28 的原 with-J 基态回执，以及 actual54 产生并保存的方向。基态原值如下，均直接抄自 Actions number-record；十六进制为 little-endian binary64 原字节。

| 基态字段 | 原保存值 | 原字节 |
|---|---:|---|
| 原 scaled infinity norm | `0.04177307820740199` | `c61182e94763a53f` |
| `minA` | `0.9999999999759498` | `cfb1fcffffffef3f` |
| `minD` | `0.9999999999999858` | `80ffffffffffef3f` |

本次真实计数为：

| 操作 | 记录计数 |
|---|---:|
| 原 native request | 1 |
| 新原 no-J trial 求值 | 10 |
| 新基态求值 | 0 |
| 新 J 求值 | 0 |
| 新 correction 求解 | 0 |
| 缓存基态消费 | 1 |
| 保存方向消费 | 1 |
| 完整记录的原 trial callback | 10 |

请求仍使用原完整接口的 `jacobian=true`、`audit=true`，但本轮在失败处退出，没有生成新的 endpoint J 或 fresh endpoint audit。这两个请求标志不能取代实际完成字段。

Actions trial 步骤的运行区间为 `20:16:22–20:18:11 UTC`，publisher 于 `20:18:16 UTC` 成功。launcher 的 `elapsed_seconds=101.506549247`，内部 replay summary 的计时为 `81.48` 秒；两者覆盖不同的执行范围，不混用或相减推断未记录的性能量。

actual54 曾在进入 native 之前因原 actual28 文件名写成 `result.json.gz` 而停止。本次源码的对应 pathname 已改回实际 `result.json`。没有重新计算 868 个 direct-longdouble 单步 map，没有重新组装/求解 actual54 方向，也没有把旧失败当作新的 trial 结果。

## 3. 全部十个失败现场

下表的 `stage` 是原 native 576 段系统的编号，`rawSegment` 是该系统已有的布局标签，输入节点为求值现场所记录的原节点。它们不是新 1372 段系统的段号。十次均位于 `rawCell=0`。

| trial | 步长 $\alpha$ | 原 stage | rawSegment | 实际失败输入节点 | 原失败原因 |
|---:|---:|---:|---:|---:|---|
| 0 | `1` | 14 | 7 | 15 | `momentum branch D/S/A rejected` |
| 1 | `0.5` | 14 | 7 | 15 | `momentum branch D/S/A rejected` |
| 2 | `0.25` | 16 | 6 | 17 | `momentum branch D/S/A rejected` |
| 3 | `0.125` | 19 | 6 | 20 | `momentum branch D/S/A rejected` |
| 4 | `0.0625` | 23 | 6 | 24 | `momentum Newton line search failed` |
| 5 | `0.03125` | 28 | 5 | 29 | `momentum branch D/S/A rejected` |
| 6 | `0.015625` | 28 | 5 | 29 | `momentum branch D/S/A rejected` |
| 7 | `0.0078125` | 28 | 5 | 29 | `momentum branch D/S/A rejected` |
| 8 | `0.00390625` | 28 | 5 | 29 | `momentum branch D/S/A rejected` |
| 9 | `0.001953125` | 28 | 5 | 29 | `momentum branch D/S/A rejected` |

`D/S/A` 是原实现的合并拒绝消息。现有回执没有指出其中哪一项先失败，也没有给出对应的全角 root 条件；不能据此宣布某个特定角度或某个单独不等式是原因。trial 4 的消息属于动量 root 的 Newton line search 失败，也不能替换为已证明的几何分支不存在。

每次失败前的实际输入均由原执行现场保存为 `trial-XX-stage-input.f64le.gz`，每件压缩文件为 1815 字节，解压为 `[1,224]`、`<f8`、C-order 的 1792 字节。十件均通过压缩文件 SHA、gzip CRC、解压完整长度与 raw SHA 核对；全部 224 个字的 IEEE 分类有限。这里没有从基态和方向重新生成这些向量，因此没有把另一次浮点构造冒充现场输入。具体每件完整 SHA 在独立审计 JSON 中。

在 $\alpha=1/32$ 至 $1/512$ 的五次试探中，原记录均落在 stage 28 / node 29。这个事实只定位该次执行首先报错的位置，不证明后续各段可行，也不证明进一步缩小步长一定成功或失败。

## 4. 方向、基态和边界的字节闭合

本轮方向来源是 actual54 的新原坐标 binary64 J 系统，其完整 matrix identity 为：

```text
76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999
```

被消费的实际 solver result 压缩文件 SHA 为：

```text
e1ac6c83434ac3b269663e930b1370a38f280b2d31c5e720955b5ed0aed7e105
```

独立审计读取了 actual54 的完整原件，并对照本轮 spec / binding / summary 核得：

| 对象 | SHA-256 |
|---|---|
| 完整 1373 节点方向 raw | `e72f3cf56bf4abe29ce8292462566f763d1dfbb69e3229e83404e0c260b99de5` |
| 原 577 节点限制方向 raw | `5d4f941c0850892d5b3a8c7fd10bfe96d60002dfac12ca342ad62efc94ba8b0d` |
| 原 577 节点基态 raw | `6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8` |
| 原 577 个 residual scales | `ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc` |
| 原完整物理 cut height $H$ | `c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f` |
| 原 far graph | `395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54` |

用保存的 `old_to_new` 仅选择字节区间，完整 1373 节点方向在全部 577 个原节点上的字逐一等于被消费的限制方向。基态和 scales 的相同限制也逐字吻合；这只是保存字节的索引核对，没有计算射线或方程。请求中的全部 112 个 height 数与 checkpoint 的 `cutHeight`，打包回 binary64 后均与上述 $H$ 原件相同。

JSON 的数字语法不保留 JavaScript 的负零。本轮基态保留了原 raw 字节以及显式负零恢复记录：相对 JSON checkpoint，只有 9546 个零字的符号差异；全部非零字一致。这 9546 个位置由保存 raw 原件验证，恢复后完整 SHA 正是上表基态 SHA。不能把 JSON 的普通零视为已经保存了原 signed-zero 身份。

`native_iteration.json.gz` 与失败 `native_0001.json.gz` 的 checkpoint 中，`parameters`、`states`、`rawNode`、`rawStates`、`cutHeight` 全部一致；唯一不同键是 `scope`。前者明确标记未收敛迭代检查点，后者明确标记失败 Newton 状态。这个区别是用途文字不同，没有产生新状态，也没有任何接受声明。

## 5. 原试步正文与来源锁

本次 launcher / hook 分别为：

```text
geometry_20261114_native_direct_ld_trial_replay.py
41976f4298d361ad06d0753698eebcd5149d3ce56410904768d6426610c2984e

geometry_20261114_native_direct_ld_trial_replay_hook.mjs
373c82c75152a800246e84618fb2ba72fc0b3960e3b3e4eff9b7590724bad4ce
```

instrumentation 保存了实际内部函数文本、原文本及可逆替换记录。独立审计只做字符串操作：逆转缓存 baseline 与保存 correction 的两处替换，并移去 finish 观察器，逐字恢复原内部函数。原十次试探正文与实际 replay 正文的共同 SHA 为：

```text
603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99
```

导出的原 public `tail.solve` 包装函数亦保持原身份：

```text
283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a
```

源码恢复不执行任何 native 代码。检查同时区分原 core 文件、runtime instrumentation 和实际调用函数，不借修改 `toString` 伪造原 source 身份。当前仓库可用的对应冻结源已逐文件 SHA 核对；两个 native worker/engine 源仅在本轮两个 runtime source-ledger 中核到相同固定值，此项没有冒称另行读取其本地源 payload。

完整 configuration / parameters 与 verified spec 对齐；原 graphs、gains、far、scales、容差保留事实来自原执行记录及其绑定。这里没有拿新 1372 矩阵的线性 exact 残差充当原非线性试步门，也没有要求旧 576 long-J 系统的线性缺陷先过额外阈值。

## 6. 完整回执与审计范围

本次 artifact 为 `visible-mainline-directldtrial-43636504089-1`，id `14129374575`，ZIP 2902231 字节；根已唯一下载并核到：

```text
14fc5777a1aeaa76ff5b9e98ec9029f1c3565a80d03a9e439ec5c0d5adbbaaf8
```

独立 byte audit 完整读取 artifact 中 47 个文件，记录其字节数与 SHA；对其中所有 gzip 原件完成解压与 CRC 检查。`result.json` 的 32 件小文件清单均逐件通过 file/bytes/SHA 校验，另核十个失败现场向量、source/launch/spec/baseline/direction 交叉身份及 prior54 被引用的原件。关键小文件如下。

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `result.json` | 18707 | `6bc14cd78db7754d281fd6fa9cb764c185b7c11c88755caa6c8ff5ce6ee81db5` |
| `trial-replay-summary.json` | 10438 | `8e8572b8b8c424ae5d14dc8acc5d8fc5c2e08d06d21cbaaeda7de982ac7e6da8` |
| `trial-replay-spec.json` | 235579 | `d2354b22960b6e0b89b2baee132cc96d7604d983d0d4a20f6e882fb09f0f1146` |
| `baseline-reuse.json` | 2694 | `5ae891a201f5eff06f102e1301a0b56d9768a02909b5c33161e42c3126ab4f56` |
| `trial-direction-binding.json` | 7341 | `f45bcc4f56c7a0ab012ced463e84463c0ab43f87ad6b91add9112aa88bec9a83` |
| `native_trials.jsonl` | 2354 | `d7d8e4bcccba4cfb3f49ff55e079be7085c10e00f88a0c9217789d4d26a419a4` |
| `trial-replay-records.jsonl` | 7608 | `69c89fac9b430133043fac6e6f468fef1e2d95b5c3164b91f4ba561ebf84572c` |

该审计证明本结论引用的是这次已保存的完整执行回执及原字段/原字节，并不独立重演其数学计算。所有范数、guard 结果、失败类别和时间均来自 Actions 已有输出；本地没有重算它们，也没有由失败输入合成整条试探曲线。

## 7. 对下一方向的实际约束

actual55 已把“新 J 形成后所得方向能否通过原十次非线性试步”的悬而未决项，落实为这条保存方向的真实全拒。它没有证明不存在满足原方程的 tail，也没有证明进一步缩小步长必定失败，更不能从成功的矩阵形成、LAPACK 返回或 replay 协议结束推导 native 接受。

下一次可检验的算法变化是 [R273 完整阻尼平方根链](../results/R273-complete-native-damped-square-root-chain.md) 在相同原方程和 scales 下取明确 $\eta=1$ 生成另一方向；选择范围见 [eta-one 接线说明](2026-11-14-native-damped-eta-one-trial-contract.md)。这与重新重复 actual54 同一方向不同。阻尼只改变方向选取，原 cut/far 行保留，方向的 cut/far 分量不得事后投影或清零。新方向仍必须完整交给原十次 no-J / guard / 严格 infinity-norm 规则。

R273 的平方和模型与原 infinity-norm 接受判据不同。即使新报告的 L2 模型下降或线性 exact 缺陷较小，也不能提前宣布试步可行；这些仅作为同一次 Actions 中保留的诊断，不另加科学接受门。本记录在 actual55 的真实全拒处结束其证据范围，未预写后继运行结果，也不满足本课题的最终完成标准。
