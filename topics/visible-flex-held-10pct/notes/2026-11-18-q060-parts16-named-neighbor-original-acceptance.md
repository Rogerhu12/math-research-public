# q060 parts16：一个具名邻数初值通过原 native DN

## 真实接受及范围

**数值证据。** 对同一完整八维 call3 高度，新 parts16 失败态的一个
预先指定内部分量作正邻数初值后，未经修改的原 worker 在 iteration0
通过原严格 $2\times10^{-9}$ 门，返回残差
$1.8182055424338136\times10^{-9}$、208 个有限 height-jet Jacobian
分量及完整原 audit。observer 真实 exit0；没有调用 prefix solver。
这是该有限尾的一次实际接受，不是全闭面或同 $g$ 加密收敛结论。

原 native record 位于
`closed_work/q060-call3-parts16-neighbor-native-v2/seed_tail_0001.json.gz`，
SHA-256 为
`850f81a202d0092b8c7b44c4bcf86904fdf3d105101322140ce32a1d8a0251cf`。
原 audit 给 actualMetric
$4.6229862382674014\times10^{-8}$、fullD
$3.266795774508992\times10^{-4}$、minLeading
$.5219178057511858$。这些是原有限 audit 的诊断量，不能替代
完整前缀、接缝、闭合或连续角域证书。

## 新 parts16 状态上的一次定位

输入是[原 parts16 真实失败态](2026-11-18-q060-native-parts16-tail-terminal.md)，
SHA `c2c80ef0372cf5cccec24ab8e8c33b11bcd1b87c989d2a4e6f8e60d0986ae64a`。
原 locator 对全部 1152 段只做了一次 full-Jacobian replay，范数逐位
等于原停止值 $3.6679653980984485\times10^{-9}$。
session30623 真实 exit0，observer 时间 28.013 秒。

| 具名位置 | 分量 | 原有符号残差 | 原归一化残差 |
|---|---|---:|---:|
| stage86，cell0/segment3，$[.5625,.625]$ | mode3 动量（component8） | $+1.1368683772161603\times10^{-13}=+1$ ULP | $3.6679653980984485\times10^{-9}$ |
| stage87，cell0/segment3，$[.5,.5625]$ | mode12 动量 | $+6.821210263296962\times10^{-13}=+3$ ULP | $1.8182055424338136\times10^{-9}$ |

其余行更小。minA 在 stage80；该行残差只有
$9.08115615498282\times10^{-11}$，并非主峰。
far Robin 原始残差最大值为
$1.4173805797431319\times10^{-30}$。
这次唯一超过门的是 mode3 的一个 ULP，已经不同于旧 parts8 的
stage45/mode12 的 70 ULP。因此没有重启已停止的 $\alpha/\beta$ 候选族。

## 唯一预先指定的自由状态变化

`propose_named_tail_neighbor.mjs` 只把 node86/component8 的值
$-955.7444743589818$ 改为朝正方向的下一个 binary64 数
$-955.7444743589817$。它恰好等于 locator 记录的原 flow 输出。
程序逐项确认只有这一个状态标量变化；完整 $H$、两个边界节点、
raw-node 结构、原参数和配置不变。

对 $R_i=\Phi_i(X_{i+1})-X_i$，该变化只影响 row85、row86。
程序用原 `flowStateWithJacobian` 分别计算两行的变化前后值，保留原
动量 `portRatio`，再用原完整 `evaluate(..., true, scales)` 复核。
新的全残差逐位等于两行变化与未受影响最大行所预测的值，降至
$1.8182055424338136\times10^{-9}$。session32423 exit0；没有在这个
candidate-only 程序中调用 `dn.solve` 或构造接受响应。

完整初值文件 SHA 为
`bba17795e196c4df43d937b2c4a0048c5cc502c5e5144a3c7216e78383842e41`，
仍明确 `solver_success=false` 和 `candidate_only=true`。
它的通过只允许后续原生验收，不能自行算作求解接受。

## 首次接入暴露的 IO 元数据身份问题

首次 one-shot 原生入口在发送任何 DN 请求前退出：原 worker 的
`parameters` 字典会展开配置，因此含 `initialCheckpoint`、`traceFile`。
候选保留旧失败态的这两条路径，重启 ready 则保存新的输入和日志路径。
原 v1 把整个字典当作不应变化的物理参数，导致过严的全相等断言。
该次 session59329 observer exit2、native_calls=0，是工程接口问题，
不是数学求解失败。旧代码和记录完整保留。

独立 v2 不笼统忽略字段。它对每个允许 IO 字段逐项检查：旧 parameters
中的 presence/value 必须精确等于旧 cfg，新 parameters 中必须精确等于
新 cfg；只有经此映射核对的 IO 字段才从物理比较中取出。
所有其余 parameters 完整逐项相等。真实 v2 输出确认恰好只有
`initialCheckpoint`、`traceFile` 两个字段发生上述路径迁移。

`recovering_tail_client_v2.py` 也按相同 schema 修正自动恢复路径。
每次重启前保存**当前代** ready 与 cfg；用该上一代与新一代做 IO 映射，
再锁定全部非 IO parameters、完整其余 ready（cut、linearSlope 等）和
原源。首次 `_fixed_configuration` 继续锁全部非 IO 配置。
这避免第二次及后续 generation 错把上一代 cfg 对到第一代 ready。
没有修改已发布 v1、旧 owned overlay 或原 worker。
自动恢复生命周期本身尚未端到端触发；本条实际完成的是一次原生入口。

## 原 worker 独立完成接受

v2 one-shot 通过原 worker 既有 `initialCheckpoint` 协议加载候选。
shootingParts 仍为 16，因此走同网格节点复制。
独立同一 JavaScript 算术检查确认高度比值为 1，
`height[j]/radius**4 - state[0][j]` 全为正零，radius $.3$；
不存在会被加零改写的负零状态。

配置只换 initializer 和 trace 路径，$M=8$、N128、depth8、RK16、
parts16、原门与全部物理参数不变。实际向原 worker 发送原完整 $H$，
Jacobian/audit 均为 true。原 worker 自己完成求解、缓存与响应，
外部器没有合成 `converged` 或注入已接受 response。

session1187 于 2026-11-17 23:55:44 UTC 获真实 exit0；observer 时间
44.028 秒，probe 时间 42.213 秒。原记录只有 iteration0，其原范数即
$1.8182055424338136\times10^{-9}$。最终 1153 节点状态与候选逐项相同，
完整物理高度与原 call3 相同；实际 native record 含返回的完整 Jacobian
和 audit。这里使用实际返回结果，非仅依据请求标志。

## 后续与可再生来源

该接受态属于旧 call3 的 $H_{\rm new}$。原 prefix restart 产生的
$H_{\rm old}$ 必须重新由实际 worker 计算，不能借用这份响应。
旧内层 cubic 已丢失，因此后续带 raw-inner/DN-anchor 保存的新联立执行
是必要续接；新入口先冻结精确旧、新命令、同字节路径迁移及 parts16
配置，才启动。尚无新的 accepted prefix 或全闭面。

紧凑元数据为
`scripts/resume_transfer/q060_parts16_named_neighbor_native_execution.json`，
绑定定位、唯一候选、首工程终态、原 native 接受、全部源和输出哈希。
新增入口源为 `propose_named_tail_neighbor.mjs`、
`solve_original_tail_candidate.py`、`solve_original_tail_candidate_v2.py`、
`recovering_tail_client_v2.py` 与 `prepare_recovering_tail_source_v2.py`。
完整状态、排名表和原运行输出只留 scratch，不入 Git。
