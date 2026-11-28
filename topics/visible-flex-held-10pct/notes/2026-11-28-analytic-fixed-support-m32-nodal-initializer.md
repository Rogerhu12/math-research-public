# M32 原固定 support：从真实完整节点检查点生成未接受初猜

本记录接续[第二次实际进程中断](2026-11-28-analytic-fixed-support-m32-recovery-interrupted.md)。恢复仅使用该进程保存的完整 1497 节点 `last-nodal-jac-input.npz`，没有把最后的中点 Jacobian 输入当成完整节点返回，也没有把 exit 137 推断成某个已证明的内核原因。

独立入口为 [`recover_fixed_support_nodal.py`](../scripts/resume_20261128/analytic/recover_fixed_support_nodal.py)，SHA-256 `eaa7bee41ae3224074bcfa70ac24f9b35076e05ac22a2ff2602b26ca348f085a`。本次实际 session 94207 正常退出 0。全部原始 `x/y/p/pscale` 的形状、dtype 与逐元素字节在导入、保存、重新读取后逐项相同：1497 个节点、97 个状态分量、32 个参数及 31 个尺度。所有真实接受 M24 源节点和全部原 chart breaks 均仍在网格上，break 到最近节点的最大距离为 0。

入口按真实 SHA 依次追溯：第二次中断 run → 第一次中断 run → 实际通过原门槛的 M24 固定 metric 源；检查同一完整 profile、literal chart、物理尾参数、核心设置、gauge、warp reference、mean、分支区间和边界归一化。最后完整节点检查点 SHA 为 `5a28d53fb0bb8e8921574fec93ac82f0c11e133715ad525908c634fec4123af0`。其 manifest 的 `source_run` 是该进程真正的输入 run，不被错误解释为输出 run 自身。

初猜只在原保存节点以 block 64 评价完整原 RHS，以这些导数定义 Hermite cubic。没有重建或合并网格，没有插值修改保存的状态，没有 inlet 修补，没有重新缩放参数，没有组装完整 Jacobian，也没有执行 Newton/BVP。物理问题仍为 λ = .002、δ = .06413464112662924、gauge q = .06、warp_reference_q = .06（实际 warp_e = .48）、mean 1168、原线性 Robin 端条件。

| 实际返回量 | 数值 |
|---|---:|
| 原节点数 | 1497 |
| 原完整节点参数给出的 q_actual | .060000491077815986 |
| 初猜原 scaled BC 最大值，仅诊断 | 7.404054655461849e−9 |
| 执行秒数 | 22.44392300400068 |
| 峰 RSS，KiB | 393172 |

生成的 `initial.npz` SHA 为 `5dc8cd5089bb004f5e669d02aef79cb6541ce47ef2f4a396728eafffca51b6f7`，实际目录为 `held10-analytic-work/fixed-lambda002-m32-nodal-recovery-v1`。完整执行记录保存为[相邻 JSON](2026-11-28-analytic-fixed-support-m32-nodal-initializer.json)，SHA `0a4da2a37894cb874e7dd887385db7d125ca350ae5c4179bb91a953e904c221c`。

状态明确为 `unaccepted_fixed_support_complete_nodal_recovery_initializer`。节点处原域检查和初始 BC 诊断不替代完整 RMS、原非线性求解、物理 BC 与完整 metric audit。M32 仍无实际接受返回，尚无 M24→M32 的完整六 jet 收敛比较。后继须由独立、保原 nodal 数组的恢复入口接入已核低临时内存完整矩阵装配，在明确资源窗口内执行全部原门槛。
