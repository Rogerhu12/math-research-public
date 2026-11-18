# n4 完整 H：同一状态的实际 DN、审计和边界 Jacobian

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 实际接受

在[完整 H 入口](2026-11-18-n4-native-raw-fullH-entry.md)之后，原 raw coupler 已实际得到以下两份成功响应；原程序随即继续前缀联立，没有在此停止。

| 原 worker 请求 | 返回时间 UTC | 原完整残差 | 实际返回 |
| --- | --- | --- | --- |
| call1：jacobian=false，audit=true | 2026-11-18 04:43:12 | `1.6177547370043463e-9` | 原 cut 两阶数据和完整原 audit32 |
| call2：jacobian=true，audit=false | 2026-11-18 04:45:09 | `1.6177547370043463e-9` | 原 cut 两阶数据及 1240 个 height-jet Jacobian 条目 |

两份响应均由原 DN 实际返回 `converged=true`，严格通过原 `2e-9` 门。第一份从未接受的半幅 checkpoint 初始化，直接求完整 H；第二份是原 coupled outer loop 对同一完整 H 的后续请求。这不是仅通过一个候选残差，也不是通过缩小目标来领取完整 H 的接受。

## 为什么两份响应属于同一个有限状态

两次请求的全部 20 个 H 分量逐字节相同，目标哈希始终为 `bd560bebd4d0f41405b713a89507f4973e6f791b39b4d60e863caa0c98acfe11`。两份完整 checkpoint 的 2305 个节点、每节点 40 个原状态分量，共 92200 个 binary64 值逐字节相同；包括 node0。完整状态哈希为 `df690e43aac00d27cd0645e9d41e84755a3089c1efd8b11178bb4bff6bd23ed3`。

各响应的 checkpoint 又分别与对应最后完整 native Jacobian 批次的所有 stage 输入逐字节对应。两个最终完整输入 wire 也相同，SHA-256 为 `56ceae52907ce1df45f40e21c721ce7825122edaa5335107e5df781f937f0228`。这处比较对象是实际非零状态输入，不是静态零占位模板。

两份保存的 cut jets 数值完全相同。第二份返回了全部 $20(3\cdot20+2)=1240$ 个有限边界 Jacobian 条目，全部有限；第一份完整 audit32 在同一状态已经实际执行并返回。因此这里明确记录的是由原请求流程分两次返回、但目标和完整状态均相同的 DN、审计和边界 Jacobian。

## 有限审计数值

原 audit32 的采样 metric 为 `2.6534685559909995e-10`，`fullD=2.0949575838452885e-5`，`normalizedFullDefect=7.194942729895937e-8`，`minLeading=0.9615807616266421`，`minD=0.9998895992827143`。其余原标量包括 `formalCurvature=8.001785963293237`、`maxPhysicalPV=1.884621429960101e-5` 和 `holonomy=1.8538771888538456e-20`。

末次原 shooting 检查给出 `minA=0.9615807599706772`。原 cut 返回的均值一阶、二阶修正分别为 `3.040063190346365e-7` 和 `3.199381822326571e-5`。这些值是该有限实际尾的原程序输出；`fullD` 没有被附加一个原程序不存在的验收门，有限采样也没有升级为连续角度或无限尾证书。

两份响应之前累计完成 11 个 native 批次，其中 6 个全 Jacobian 批次、5 个标量候选批次；四进程包装器的 44 个原 CLI 子进程全部退出 0。所有分片输入、输出和日志均保留并核对哈希。本文不把尚在运行的整个 coupler 记为进程终态。

## 可追溯记录与仍在进行的部分

两份原始响应分别是 scratch 中的 `seed-tail_0001.json.gz`（SHA-256 `337dcf81db9c5812670518868b11b5230863a08430866ae0809e364210bb0a2a`）和 `seed-tail_0002.json.gz`（`3ffe4520bef36b837e9303481c1729f41d5b8a4bca45fcd93efd0ad74314f597`），均位于 `n4_work/native-raw-fullH-v1`。原完整 H、原物理尾、M20、N512、parts32、RK16、生产 floor=.05 和全部原接受条件不变。

紧凑记录为 `scripts/resume_n4_tail/native_raw_fullH_response_pair.json`，只读 collector 为 `record_native_fullH_response_pair.py`；实际只读会话 `41556`、终态 `afa0e4` 退出 0。collector 复用已冻结的原字节输入检查器，核对源、实际响应、完整状态、原请求、所有完成批次与分片文件，并保存截至 call2 的不可变日志前缀。没有重跑模型、root、flow、Jacobian 或 audit。

这使当前 raw 前缀的完整 H 真正进入了原非线性尾，而不是继续停留在线性 DN 条件下。原前缀内解、后续真实 H 的更新、完整两阶 seam 和前缀 metric 仍由正在运行的原 coupler 继续完成。本条不声明实际 raw 前缀已经通过全部终态门，也不声明圆化参数 1、精确保护圆弧、闭族、连续误差界或 10% 指标完成。
