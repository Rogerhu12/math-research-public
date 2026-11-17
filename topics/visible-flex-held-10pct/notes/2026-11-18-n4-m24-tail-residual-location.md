# n4 M24 失败尾的主残差位于最高保留模式，不能用分量 ULP 解释

维护日期：2026-11-18（UTC+8）。本条只读重放
[M24/parts8 的已记录失败态](2026-11-18-n4-actual-m24-parts8-terminal.md)，
完整有限态哈希为
`9c68be03e16f46074e41f25fd8e0247dacb145004939206b0339fbde827e19e8`。
标量证据为
[eta010_q010_m24_residual_location.json](../scripts/resume_n4_tail/eta010_q010_m24_residual_location.json)。

## 重放保持原路径

使用 [locate_actual_tail_residual.mjs](../scripts/resume_m3/locate_actual_tail_residual.mjs)
读取原完整 stage 状态、cut height、配置和缩放；评估实际 Newton 所使用的
完整 flow Jacobian 路径，不进行 Newton 更新。
引擎使用已经独立检查的 n4 共享 periodic 源，原 $N=512$、M24、parts8，
共 576 个 stage。重放范数精确等于保存的
$5.410937798428335\times10^{-9}$，根量和原门也相同。

## 主导行与次大行

编号均沿原程序的零基索引。

| 项目 | 主导行 | 次大行 |
|---|---:|---:|
| stage | 28 | 44 |
| physical cell | 0 | 0 |
| segment | 5 | 3 |
| 段内区间 | $[0.375,0.5]$ | $[0.375,0.5]$ |
| 物理 Fourier 模式 | 96 | 4 |
| 分量类型 | 动量变量 | 动量变量 |
| 原缩放残差 | $5.4109377984\times10^{-9}$ | $1.6067146907\times10^{-9}$ |
| 未缩放带符号差 | $-2.0354742129\times10^{-12}$ | $1.7763568394\times10^{-15}$ |
| 原缩放量 | $3.7617771423\times10^{-4}$ | $1.1055832437\times10^{-6}$ |

主导行保存值为 $1.2750842429\times10^{-15}$，flow 值为
$-2.0341991286\times10^{-12}$。保存分量的一个 Float64 ULP 为
$1.9721522631\times10^{-31}$，因此这个差不是保存分量的一个或几个 ULP。
这不排除 flow 内部消去或积分舍入的影响；本次重放并未证明主误差的最终来源。

次大行是约 $-7.809$ 的低模动量，其差为该分量的两个 ULP，已经低于
原 $2\times10^{-9}$ 门。不能把另一个分支的一 ULP 主导机制搬来解释本 n4 状态。

最小 $A=0.9425451582746428$ 出现在 stage 31；其局部残差约
$1.47\times10^{-13}$，与主导残差位置不同。最深端边界残差仅
$2.07\times10^{-27}$。这支持先检查最高模式的分段 flow 误差，不能归咎于
深端边界不满足，也没有给出实际尾不存在的结论。

## 可复现性与限制

定位程序哈希为
`72133319edd9897801beaf88114ddfa5ef93a66bcc95d100c342ab28ac811efc`。
采集程序 [record_tail_residual_location.py](../scripts/resume_n4_tail/record_tail_residual_location.py)
只保留三个具名标量行、原门、源与输出哈希；完整可再生排序表留在 scratch。
后续可用原嵌套规则加密至 parts16，并将这里的失败完整迭代态仅作为初值。
任何新状态仍须重新通过全部原方程与原门，本条不将旧失败态改判为接受。
