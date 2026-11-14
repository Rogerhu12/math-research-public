# M15 首个振幅延拓请求：执行中断与原方程恢复

可信度：**执行记录；未完成数值求解**。2026-11-09，coupled_prefix。

## 中断证据

原 stem 为 `2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-01`。它从线性初猜请求同一固定度量的 $s=1/4$ 边值，原 M15、N256、depth12、p8、steps32、tol $2\cdot10^{-9}$、projectionFloor $.05$ 均不变。

在 10:58 UTC，本代理自己的 `write_stdin(session_id=11849)` 返回 `Unknown process id`；root 的独立查询也不可用。本代理随后扫描自己的 `/proc`，未见匹配的 controller 或 worker。最后的 trace、trial、原子 checkpoint 都已停止更新。工具没有提供实际退出码或信号，故**不知道退出原因，也不能把它记为 exit 0、原方程不收敛或 OOM**。当时 `memory.events` 仍是先前已知的 oom=9、oom_kill=2，没有新增 OOM 证据。

最后一次完整原子 checkpoint 是 10:42:42 的 iteration 4：normalized residual $292.71994277008594$，minA $0.9145614796914862$，minD $0.9978508773278302$。10:45:09 最后记录的 trial 为 $\lambda=1/8$，其 residual $301.4418731558783$ 未下降。之后没有已记录的接受步，也没有完整 DN response 或最终 reproduction。

原 progress 的 `RUNNING_WARM_CONTINUATION` 只是未及时结束的旧标签。单独的 `db6f-prefix-amplitude-continuation-01-interrupted.json` 以 `INTERRUPTED_EXECUTION_UNAVAILABLE_EXIT_UNKNOWN` 取代这一执行状态解释，原文件字节不改。该记录绑定五份只读副本：最后 CP、trace、trials、空 run log 和旧 progress。恢复 CP 的 SHA256 是 `8266c8b9e66ffd57e3fce0c9e806a0c14533cd9b7795cca6bcfdb2fc205cd20a`。它仍明确为 **UNCONVERGED recovery only**。

## 已知成本与未保存的诊断

原单次请求的 `maxIterations=36`。已完成的四个迭代整轮间隔为约 243.10、237.18、237.16、251.48 秒；包括原全 Jacobian 计算和该轮的回溯残差评估。全 Jacobian 约 98–107 秒，单个真实 state-only 残差约 32–37 秒。最后记录距离首次请求约 1213.912 秒。

当前 checkpoint 保存了完整 states、物理 cutHeight、raw states 和 norm/minA/minD，**没有**保存 residual 向量或最坏 stage/分量。仅靠现存文件不能定位最坏分量；本文未另跑一次 Jacobian 或 residual 来补充它。较高的 norm 不能据此归因于舍入、某一 Fourier 模式或某一 raw 段。

复用深段 Jacobian 只会减少全 Jacobian 与 state-only 之间约 60–75 秒的差额的一部分，线搜的每个真实残差仍须全域计算。原循环最常需四次 trial，故单靠该改动的潜在整轮节省约为四分之一量级，尚无实际派生实现或成本测量。当前优先恢复原算法。

## 最小恢复计划

实际运行由 root 持有工具会话，避免重复启动。本代理没有启动恢复进程。

复用已审 `db6f-prefix-tail-trial-run.py`，传入上面的只读 iteration-4 CP。该 runner 只更换输出路径、恢复初猜和迭代预算；原 RK、moment root、guard、归一化、十档线搜、严格 residual 下降接受条件和 tol 不变。请求高度直接复制 CP 的 `cutHeight`，已按全部 15 个系数逐值核对为冻结 affine 目标的 $H_j(1/4)=(1/4)^{j+1}H_j(1)$。

原循环已完成 iteration 0–3；从 iteration 4 重新评价并继续，设 `--max-iterations 32`，保留原 36 轮总预算。被中断的 iteration 4 的未完成回溯不算一个已完成迭代。runner 请求最终 DN Jacobian，audit=False；这不会改变求根方程或停止判据，也不构成几何 audit。

精确命令、输入路径、来源哈希和固定源文件清单见 `db6f-prefix-amplitude-continuation-recovery-launch.json`。命令的输出 stem 是 `db6f-prefix-amplitude-recovery-s025-iter004-01`，与原中断输出完全分开。

只有这个恢复请求真正返回 `converged=True` 且原 residual 小于 $2\cdot10^{-9}$ 时，才能作为已审 continuation controller 的 `--resume-checkpoint`、`--resume-scale .25`。若成功，将原调用和恢复调用的总迭代数用于选择后续 step；不能把此 UNCONVERGED 输入本身作为成功的 last state。若失败，保留完整响应后，原控制器仍可从更小 $s$ 的线性初猜重新开始。任何 $s<1$ 的结果都只是尾 warm；即使 $s=1$ 目标 DN 成功，仍须原实际 prefix 外层校正。
