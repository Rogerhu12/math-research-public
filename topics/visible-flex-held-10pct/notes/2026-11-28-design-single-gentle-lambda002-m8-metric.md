# R87 新剖面 $\lambda=.002/M8$：仅原 metric 门未过

2026-11-28，/root/design_continuation。以新单级温和剖面真正接受的
$\lambda=0/M8$ 场为源，原完整 BVP 在 $\lambda=.002$ 收敛，RMS 和物理边界
均通过；**metric L1 为 $2.6743628130377957\times10^{-6}>10^{-6}$，
该有限模态场没有被接受。**

| 项目 | 实际值 |
|---|---:|
| 节点 | 580 |
| 原 RMS | $9.873777538800396\times10^{-7}$ |
| 原 physical BC | $4.287830672511499\times10^{-11}$ |
| 原 metric L1 | $2.6743628130377957\times10^{-6}$ |
| audit 角点 | 512 |
| 实际 $\delta$ | .06809578114722738 |
| 原 Newton 接受步 / 拒绝 | 3 / 0 |
| QR driver 实际末尾最大 RSS | 174256 KiB |

$q=\mathrm{warp}=.012$，原所有状态、支撑控制列及 $\delta$ 列完整保留。
实际控制器判定为 metric-only failure，继承此收敛但未接受的完整 raw/physical
只作 Newton 初猜，按原完整 core-lift 身份升至 $M=16$、仍求同一 $\lambda=.002$。
没有将这次谱门失败当成不存在，没有放宽 $10^{-6}$，没有缩小 $\lambda$。
这组新剖面输入不等于旧两级剖面的已登记失败链。

实际目录为
/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-low-modes/attempt-000。

| 输出 | SHA-256 |
|---|---|
| run.json | 141a38f7b1760178f3caf69ac5e15399569f49273675e7b05e1b1716dd9daf1c |
| inner-00.npz | 74648f39bfa7bb023a7b2cfbfa56132385270e9a7ef441dcd80624c5f0c33892 |
| physical.npz | 1235e2fcf0e1759d68011c5cbaf86989d934d8f9b5f44110ba4ab761d3b50dda |

[同名 JSON](2026-11-28-design-single-gentle-lambda002-m8-metric.json)
保存闭合的本次 run、raw、physical、QR 记录 SHA，原 source/input SHA、
实际执行命令与原 dispatch 单行字节 SHA。整个仍在增长的调度日志没有被冒称冻结。
本条仍不涉及真实非线性尾、闭合、连续几何或 README 完成标准。
