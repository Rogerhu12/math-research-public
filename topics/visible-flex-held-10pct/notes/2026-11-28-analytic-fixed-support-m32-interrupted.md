# 固定 g M32 第一次实际求解：exit137，尚未返回解

2026-11-28，`fixed-lambda002-m32-spectral-v1` 的工具 session94023 实际返回
`exit_code=137`（SIGKILL）。没有 solver raw return，也没有 physical 导出或
最终 metric audit，**不能将 M32 晋级**。当前已接受 fixed-g 锚仍是原 M24、
`tol=2e-7`、1032 节点的真实返回。固定的 delta/λ/g/mean1168 没有改变。

最后一个已经显示的 adaptive 迭代是第 4 轮、1209 节点，打印的 RMS 为
`3.93e-07`、BC 为 `4.32e-12`，随后增加64节点。这两个是 stdout 的舍入显示，
不是保存 raw 的精确数值。后来在1273节点实际构造了123513维完整 Jacobian，
保留97个 state、32个 parameter，非零数27913938；同网格再次 refresh 时峰
RSS升至3330564 KiB。最后看到的原矩阵解日志在1155.155秒。

目前不能确认137的系统原因。检查时 `/sys/fs/cgroup/` 下的
`memory.events/current/max/peak` 均不存在；没有可读OOM事件记录。因此只登记
已观察的SIGKILL和RSS，不将“可能的内存峰”写成已证OOM，也不将任何时长假设
写成已确认原因。

`last-jac-input.npz` 保存的是随后覆盖的 **1272个内部midpoint**：97个完整
state和32个参数均在，但`t`从`.00005208333333333334`到`.99984375`，没有
两端点。它不是1273个完整nodal状态，更不是已接受解。其SHA256为
`e89f01c9fd40662dc1978d1244f72ea5cf5517ccad7d4b379ba786c234ec947b`。
死进程留下的 `run.json` 仍显示 `running_original_fixed_support_BVP`，真实
终态以本条为准；该run SHA256为
`d364dcd6a725b39fad5cbf8105dddfe8139e9f1bd537491651a147ad3f9dacb4`。

完整实际文件清单与哈希在
[`2026-11-28-analytic-fixed-support-m32-interrupted.json`](2026-11-28-analytic-fixed-support-m32-interrupted.json)。
恢复继续进行：使用这些真实midpoint值及原RHS生成明确**未接受**的完整Hermite
初猜，保留所有state/参数和同一物理问题；在完整J重建前释放无后续用途的旧
factor，并单独原子保存nodal检查点，避免被midpoint覆盖。没有重新求解M24，
没有将插值初猜或仍在运行的记录称作接受。
