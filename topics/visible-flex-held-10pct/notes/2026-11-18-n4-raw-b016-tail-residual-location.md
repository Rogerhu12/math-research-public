# n4 raw 新宽度尾：原停止残差逐位重放，集中于多个高模内部阶段

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 实际定位

对[首轮实际尾未过门](2026-11-18-n4-raw-b016-actual-parts16-terminal.md)保留的完整失败状态，以原 full-Jacobian flow 路径和原 stage scale 重放全部 $1152$ 个阶段。得到

$$
1.1391523014166158\times10^{-8},
$$

与原停止值逐位一致。未运行 Newton、未改变状态、未改变物理参数、求积、分片或原 $2\times10^{-9}$ 门。

最大行是 stage $18$，原 cell $0$、segment $7$ 的区间 $[0.8125,0.875]$，物理 mode $76$ 的 momentum 分量。其 state 为 $-751.0491913098218$，flow 为 $-751.0491913098192$，有符号差

$$
2.6147972675971687\times10^{-12}
=23\,\mathrm{ULP}.
$$

该行的 scale 为 $0.0002295388653778327$；一 ULP 对应归一误差 $4.95283609311572\times10^{-10}$。所以这不是先前 m3 的单个一 ULP 停止机制，也不是另一条旧 n4 mode96 的状态。

邻 stage $19$ 的同 mode $76$ momentum 为 $-1122.2135248792556$，残差为 $-2.5011104298755527\times10^{-12}$，即 $-11$ ULP、归一值 $1.1033592976817877\times10^{-8}$。同段还有 stage $20$ 的 mode $76$ 残差 $8.1526454262\times10^{-9}$、stage $22$ 的 mode $80$ 残差 $4.1749887453\times10^{-9}$。多个内部阶段超过原门；不能用修正一个值后的局部下降冒充完整接受。

## 为什么必须检查相邻行与全残差

原 stage 残差依赖本节点状态和后一个节点经原 flow 的像。只改变 stage $18$ 的内部状态，会影响 stage $17,18$，不会改变 stage $19$ 的残差。因此单独修正最大行，即使把这一行变成零，完整最大残差仍至少为上述 $1.1033592977\times10^{-8}$。它可作为新的初猜，随后是否接受仍需原完整 Newton、全残差和最终 audit。

原最小 minA 为 $0.9922920982513689$，位置在 stage $63$，与主残差行不同。该最小 minA 阶段本身的归一残差仅 $1.6452318482\times10^{-15}$；本次停止没有表现为 minA 接近零。这里也不把局部正裕量升级成闭尾存在性结论。

## 来源与范围

复用已登记的 [locate_actual_tail_residual.mjs](../scripts/resume_m3/locate_actual_tail_residual.mjs)，SHA-256 为 72133319edd9897801beaf88114ddfa5ef93a66bcc95d100c342ab28ac811efc。实际输入为 M20、N512、parts16 的 raw 新宽度失败尾，SHA-256 为 e8afa8dd44d14d7671ba8575bd43aed63add5e1ba55f09d19146bb3b5b91da5d；没有套用别的前缀或尾状态的定位结果。

[raw_primaryb016_lam002_m20_residual_location.json](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_residual_location.json) 由既有 [record_tail_residual_location.py](../scripts/resume_n4_tail/record_tail_residual_location.py) 保留两个主行、最低 minA 行、实际源与输出哈希、完整重放值和命令。完整状态与可再生行表留在 scratch。独立观察器记录返回码 $0$、总耗时 $68.05955015$ 秒。后续局部 flow-relaxation 初猜仍使用原完整 DN 求解与所有接受门，其结果另外记录。
