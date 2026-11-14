# R273 原试探若接受：从真实 selected 状态继续原 native 的合同

- 作者：`geometry`；日期：2026-11-14 UTC。
- 分类：只读源码审查与条件接口；未实现或执行新的继续求解器。
- 适用父源：request57，公开源提交 `adbdf144b14ae7adc71df09948a5c05f8a30e8b8`。
- 本文不假定 request57 已接受任何试探，也不把一次严格下降等同于完整 native 成功。

## 1. 真实父入口

父入口是 [R273 原十次试探接口](2026-11-14-native-damped-chain-original-trial-interface.md)，不再采用旧52的 producer pin。

| 父文件 | SHA256 |
|---|---|
| `geometry_20261114_native_damped_chain_trial_replay.py` | `ebd3110e7ba9b2edeca155370d2c7fd6f02d3757ae285379d54a2b4a39793ccd` |
| `geometry_20261114_native_damped_chain_trial_replay_hook.mjs` | `884d2d44439151d0dbc5d474e20ebe5c024e577396088f01717d33a522b50323` |
| `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |

父 result、spec、summary 的 schema 分别是 `original-native-damped-chain-trial-replay-result-v1`、`original-native-damped-chain-trial-replay-spec-v1`、`original-native-damped-chain-trial-replay-summary-v1`。完整 spec 是 gzip 文件，身份是其压缩字节 SHA。一次接受的计划停止标记是 `VISIBLE_NATIVE_DAMPED_CHAIN_TRIAL_REPLAY_ACCEPTED_STOP_V1`。

实际 trial result、方向 result 与 selected 文件的 SHA 均须来自已经生成的原件。本文不填未来值，不以一个父源码提交代替实际输出身份。

## 2. 可复用的是注入切点，不是旧 seed 的身份

原 [candidate-seeded 入口](../computations/geometry_20261114_native_candidate_seeded_solve.py) 及其 hook 已提供明确切点：一个全新原进程完成 constructor/ready/source/capacity 核对后，在第一请求的 `let initial,predicted=false` 后设置 `initial=<完整实际selected状态>` 与 `predicted=true`。原 solve、evaluate、Riccati correction、trial、容差和端点计算保持原源。

其旧 `restoreBoundCandidate` 函数专门绑定 actual23 的候选 SHA、历史 packet 与状态。后继不得只换一个常量便把 selected 冒充旧候选；必须用新的 selected 身份读取层，保留第一次注入与原握手的结构。新继续过程也不设置原 `last` 或 `tangentPredictor`，不伪造已有完整成功响应。

`predicted=true` 在此仅用来防止原 request loop 再对已核状态作 amplitude prediction 或 cut correction；它不说明该 seed 是精确解，也不取消原 solve 中的任何 residual、guard 或验收。

## 3. selected 状态必须逐字节恢复

若父 replay 真有一条原试探接受，消费以下实际证据。

| 原件 | 必须保留的事实与身份 |
|---|---|
| 父 result | 完整 SHA、新 producer/hook、`replay_completed=true`、`trial_accepted=true`、一次请求和正常 worker 退出、真正的计划停止消息 |
| summary 与试探记录 | 原 alpha 顺序；唯一 accepted 是实际最后记录；真实有限 `trialNorm < baseNorm`；完整原 guard 与尺度来源 |
| `selected-state-checkpoint.json.gz` | `original-native-one-trial-selected-state-v1`；source/hook/spec/direction/capture/step/direct/matrix 身份；实际 eta 与 R273 model scope |
| `selected-state.f64le.gz` | 压缩与未压缩 SHA、完整 `[577,224]` 原坐标二进制、f64 little-endian、C 顺序、负零原位 |
| checkpoint rows | node0…576完整、每行224项、合法负零侧表；编码后与 selected binary 全字节相同 |
| H / parameters / rawNode | 同完整 H、原参数、原节点与原方向约定，不插值、不重网格、不重新求初猜 |
| 原 graphs/gains/scales/far | 与父 trial 使用的原构造器字节与记录一致，不用 R273 的列坐标或内部缩放替代 |

恢复时直接采用 selected binary。不能重新计算 `base + alpha*delta` 生成“同一个”状态；该计算的浮点次序与真实原 trial 有可能不同。JSON 只提供独立的完整行与负零身份核对。

所有 selected 状态的来源标志仍是 `success=false,converged=false,native_tail_response=false`。继续入口不能在调用真实 native 前把这些标志改成成功。

### R273 的 cut/far 分量不可投影

R273 阻尼最小二乘把 cut/far 行纳入完整目标，但其方向不必恰好消掉这些线性残差。即使原 nonlinear trial 接受，selected 的 cut Q 也未必逐字等于原 target。

因此后继不应继承 actual23 专属的“初始 cut 残差恰为零”假设，不把 selected 的 cut/far 分量改零，也不重施线性边界修补。完整 H/target/far 保持原值；原 evaluate 会把真实残差计入原尺度 norm，原 native 门继续决定是否收敛。

## 4. 从新状态重新运行原完整计算

后继完整请求仍是同一 `TailClient.solve(H,jacobian=True,audit=True)`。此次不能使用 actual28 cached baseline，不能把父57 no-J trial 数值改标签称 fresh with-J，也不能把 actual54 的固定基点 J 用作新状态导数。

原 `dn.solve` 必须在实际 selected 状态重新 evaluate，并重新形成当前原 J/correction。state 的224项只含原 shape Q/Pi；原 flow 从新 shape 自行积分 mean。旧41/54的中间 mean、cut jets、endpoint Jacobian 和 audit 都不移植到新状态。

父 selected 的 no-J trialNorm 是一次真实严格下降见证。新的 with-J 基态 norm 应独立报告；不能要求它逐位等于父 no-J norm 作额外门。已有 [stage J 生成与传播范围说明](2026-11-14-native-stage-J-generation-and-propagation-scope.md) 区分原 no-J 与 with-J 的浮点 RK 路径；相同状态和配置身份不自动使两次标量逐位相同。

完整成功只能由原请求正常返回并通过其既有完整校验来确认。即使原 tail solve 已达到容差，若后续 cutJets、heightJetJacobian 或 fresh audit 失败，仍要记为完整 native 请求失败。必须保存原响应、最后实际 iteration/checkpoint、全部 trial、trace、stderr 与新 seed 身份。

## 5. 若原 Riccati 在新状态再次失败

这种最薄继续恢复原 Riccati correction；它没有将 R273 变成完整的外层迭代算法。一次新方向通过原试探，不证明后续原 Riccati 在新状态可用。

若第 k 轮失败，下一处理对象必须是**该轮真实当前状态**的完整 J、r、边界、原 sigma 和原 source。该状态可能已经经过后继原求解的若干次接受，不能默认仍是最初 selected 状态。若已有原进度与完整数组，就精确绑定这些原件；若没有保全完整 J，只能针对已明确绑定的实际失败状态另做必要原读出，不能用旧28/54矩阵补名。

之后可以对新的同状态有限系统再使用 R273 或其他经选择的数值表示，并再次交回原非线性 trial。但这需要新的 actual matrix/result/state 身份和真实原验收，不是本文已经实现的继续算法，也不保证原式收敛。

## 6. 本文完成范围

已只读核公开57两源及其正式接口，且正式接口 SHA 与冻结 `44d4c42e44bdd5cc7ac5eb9ccaa0ef3c2d39af43078622262c6628edfbac3866` 相同；同时核了旧 seeded hook 的唯一 initial 注入位置与 `predicted=true` 语义。

未写新的 selector、workflow 或继续 wrapper，未改任何冻结源，未执行 RHS/J/ODE/QR 或其他本地科学计算。实际57若全拒，就没有 selected 状态可供本合同恢复；下一动作应据原 trial 真实失败信息选择。
