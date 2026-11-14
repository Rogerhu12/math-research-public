# actual25：完整同 RK 初猜进入原 native 后，十个原校正试步均在 stage 13 出域

2026-11-14，公开仓库 Actions **真实数值失败**，已完整保全。失败发生在原 Newton iteration 0 的校正回溯，不是恢复输入、首次初猜注入、最终切口 Jacobian 或 audit 后处理阶段。

## 1. 本次实际身份

| 项 | 实际值 |
| --- | --- |
| Run | [43607404925](https://github.com/Rogerhu12/math-research-public/actions/runs/43607404925) |
| Job | `132484959081`，`Mainline nativeseed` |
| Source | `4d384dc563749e7e8b9680e234fbb1b61251873a` |
| Artifact | `14118968502`，`visible-mainline-nativeseed-43607404925-1` |
| Artifact ZIP | `2,449,354` B；SHA256 `480f69d0efa896e754af1ff24b4475886246353fe4e0e799f0c8729c86df94bb` |
| 输出子目录 | `native-actual23-seeded-full` |
| Python entry SHA | `afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7` |
| Hook SHA | `22fa88aaaf2385a34dc3a373138f1b7fec08c903fd7151717b1f3dfb4d707e8d` |

入口与改变范围见 [独立 native seeded solve 接口](2026-11-14-native-candidate-seeded-solve-interface.md)。本次只在原首次请求的 `let initial,predicted=false` 后恢复并赋入 [actual23](2026-11-14-public-same-RK-candidate-v3-actual23.md) 完整候选，设置 `predicted=true`。原数学 worker、原 solve、所有十个 trials、原域、原容差 `2e-9`、完整 DN Jacobian/audit 请求均未更改。

首次请求保留 actual17 的全部 112 个真实非零 H，`jacobian=true`、`audit=true`。原进程只收到一次实际 native 请求。没有重新算 zero solve，没有 `initialCheckpoint` 几何重映射，没有高度阈值化或比例预测。

## 2. 原 withJac 基态评估成功返回；原 correction 的十次 trial 全拒绝

原 trace 的实际顺序为：

| UTC | 原事件与返回值 |
| --- | --- |
| 14:56:50.579 | `request`，call 1，完整 H、Jacobian 与 audit 均请求 |
| 14:56:50.671 | 唯一 `actual23_complete_candidate_initial_assignment`，577×224 状态，恢复 9,546 个负零 |
| 15:07:36.946 | iteration 0 的原 `evaluate(...,true,...)` 返回，`elapsed_ms=646367` |
| 15:08:12.227 | 原 `correction` 完成，`elapsed_ms=681648`，写下原程序的 `chartCondition` |
| 15:08:14.985—15:08:40.245 | 原十个 trial 全部触发守卫拒绝 |
| 15:08:40.246 | 原失败事件：`Error: multiple-shooting line search failed at 0.04177307820740199` |

原 iteration 0 的实际读数：

| 量 | 值 |
| --- | ---: |
| 原归一残差 `norm` | `0.04177307820740199` |
| 原 withJac 返回 `minA` | `0.9999999999759498` |
| 原 withJac 返回 `minD` | `0.9999999999999858` |
| 原 correction 报告 `chartCondition` | `8.810946110232247e59` |

该 `norm` 与 actual23 的完整原 no-J norm **数值完全相同**。因此，本次保留了已观察到的初猜改善，并且原带 Jacobian 的基态评估真实返回了同一残差和上述分支余量。这里的带 Jacobian **stage flow 评估**不等于最终已返回完整切口 `heightJetJacobian`。

十条 trial 记录分别为 `trial=0,…,9`，`step=2^-trial`，即 `1, 1/2, 1/4, …, 1/512`。每一条均为：

```text
kind = momentum-guard-rejection
error = Error: momentum branch D/S/A rejected
stage = 13
rawCell = 0
rawSegment = 7
baseNorm = 0.04177307820740199
```

stage 13 是原程序的零起始 stage 编号。**没有 accepted trial；没有 residual-not-decreasing 行；没有任何 trialNorm 返回。**这些候选先在原 momentum 守卫处失败，尚未完成各自的全尾残差评估。原程序记录的是合并的 D/S/A 消息，本包没有提供哪一个分量先失败、内部 RK 子步或角索引，不能把这些未记录的细节补成事实。

`chartCondition` 是原浮点程序给出的图表条件数报告，不是严格奇异性证明。原输出也没有给出使该最大值出现的 stage；不能把它直接标成 stage 13 的条件数。

## 3. 失败保全与身份核对

实际 response 只有 `failed`、`lastIteration` 和失败 checkpoint 等字段。没有最终切口 DN `heightJetJacobian`，也没有 audit 返回。本次失败发生在原 `tail.solve` 内，因此不能称为已完成 native、已通过切口 J、已通过审计或已接受 BVP。

原 Node worker 正常传回失败后退出码为 0；原客户端正确将 `failed` 拒绝，Python/数值 step 退出码为 2。`result.success=false`、`original_client_validation_passed=false`。整个 launcher 记录用时 `724.263116042` 秒，stderr 为空。

逐件核对了 `result.json` 所列的 15 件输出的实际 SHA 与字节数。`native_0001.json.gz` 和 `native_iteration.json.gz` 的全部参数、H、rawNode、577×224 states 与 rawStates 数值相同；rawStates 精确等于对应 rawNode 的 states。

这份 iteration 0 失败 checkpoint 的 129,248 项实数与 actual23 注入候选全部相等，未发生已接受的状态更新。原普通 JSON 保存会将负零写为 0，故它与恢复后的输入恰有 9,546 项符号零的位模式差别；不能把普通 JSON checkpoint 说成保持了输入 signed-zero 字节。注入前的完整字节身份已由 `seed-binding.json`、唯一原 trace 事件及 actual23 原 chunks 保留：

```text
candidate states  6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8
all physical H    c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f
original scales   ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc
original far      395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54
```

原 live methods、graph/gain、far boundary、stage layout 的记录 SHA 为 `de9bbf01981f1605c0342817ea520005bf2d0a05f5a755986d50b718b16089a7`，与 actual23 原件相同。`instrumentation.json` 真实记录只插入首次初猜赋值，并可逐字删除该插入以恢复原 compiled worker。

关键输出身份：

| 文件 | SHA256 |
| --- | --- |
| `result.json` | `f5f4acdb055c6964fd591ac2da566bc581607b1d32ebc8096af557f4a3f8abbf` |
| `native_0001.json.gz` | `b836abc69da476967d3b464462fed55f90f10a54d966dd7d1a1fc379f0a55ddc` |
| `native_iteration.json.gz` | `2e7edf5566f6cd80f7217d8e6a07d3c64d3f3a88050b8e11d782b5c8415d07a5` |
| `native_trace.jsonl` | `dd1ddbbc7c00911c354fe34baadad331b3145b7cfbdc0c151a08628522b21218` |
| `native_trials.jsonl` | `6bb65a50911bd095c70985bbbdaa321d21d495e808881f7cff05f5f682470f57` |
| `seed-binding.json` | `5a60e750c9fae905ee7351d94b66bfb7eb86944c264da05ed37ea1116589355e` |

## 4. 当前缺口与下一项有因检查

本次把问题定位到：**同一个已经有效的完整初猜，在原校正计算后，全部十个既有步长均于 stage 13 出域。**这既不是“初始场不能进入原 flow 域”的失败，也不是某个已经算完的 trial 残差没有下降。它尚未确定是原图表消元的浮点损失、该原校正本身过大、stage 13 的局部域尺度，还是这些因素共同造成。

当前包没有保存原 correction 的完整 delta、各 stage Jacobian、线性校正残差或失败 trial 的 stage input。仅由本包不能证明某一种替代线性算法必能成功，也不能证明增添更小步长会给出有效进展。

下一项直接有因的检查应继续绑定此同一 H 和同一完整 seed，在一次原 withJac/原 correction 回放中保留所有 stage 的原 J、原残差、原 delta、原 scaleFor，并实际读取线性方程缺陷 `J_n delta_(n+1) - delta_n + residual_n` 及两端边界缺陷、最大方向位置和 stage 13 的失败输入/守卫详情。这样才可区分校正线性求解质量与非线性步长域问题；不必更换 H、重做 zero solve、重算 initializer 或提前实现新 H 的全耦合包装。此段是据真实失败点确定的后续计算目标，**尚未执行**；原方程、原守卫和原完成标准保持不变。
