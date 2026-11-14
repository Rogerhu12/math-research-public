# 从最新未接受迭代恢复真实全 H：入口准备

**状态：启发式/数值证据（实际输入读取）；没有新的尾解或前缀接受。**
作者：strong_amplitude（GPT-6 Astra Pro，AI 辅助），2026-11-14。

## 具体问题与实现

本轮 half r4 已经通过三个内部 Newton 更新，但原 `--tail-warm-checkpoint` 恢复入口要求首次物理 Dirichlet 向量与 warm 包的 `cutHeight` 逐位相同。`iterate-0004` 的 H 已经变化。因此不能把初始 half-H 的已审计标签直接用于最新 iterate，也不能改这个比较器来绕过真实新 H 的求解。

新源 `computations/strong_20261114_audit_iterate_H.py` 从原始完整 raw manifest 和带原 SHA256 的 binary64 y 块读取

$$H_j=-q\,Y_{2M+1+j}(s_{\rm cut}),\qquad j=0,\ldots,M-1.$$

这里使用原 `finite_neck_terminal_v1` 的 $\sigma=-1$，不改状态、gauge、角坐标、有限连接段或物理尾参数。真正执行时，旧完整 tail packet 只作为原工厂的 warm 状态；原 `WeightedTailPort.solve(H,jacobian=True,audit=True)` 必须在新的全部 H 上重新收敛、生成完整 J 并通过原 audit。新 packet 与 ready 才能供现有 exact-H/释放闲置 worker 入口使用。此过程本身不接受前缀。

## 已实际执行

2026-11-14 09:01:27 UTC 执行了 `--prepare-only`：0.66130 秒、进程实际 exit 0、峰 30440 KiB。读取并校验的是 r4 第三个内部更新的完整 97×2590 y；32 个物理 H 相对最初已审计 half-H 的最大变化为 **2.0725751635990023e−9**。完整 H、来源 chunk 哈希、原 config 哈希、真实 argv/log/exit 在同名 `-r1/` 中。

这次只进行了读取和配置准备，**没有启动 Node，没有计算新的 nonlinear tail 或 J/audit**。当前 session 28520 的 r4 没有中断；生成的两阶段恢复计划仅在原进程真正结束后、选择明确恢复点时使用。

## 恢复路径与限度

`loop-margin325-half-r4-iter4-recovery-plan.json` 给出两个完整本地 argv：先对 iterate0004 的真实 H 求解审计，再以新包恢复原 35 参数、全部 13 个物理方向同一半步和原全部验收门。第二阶段保留 `--release-tail-worker-between-responses`、原 strict raw 恢复及 complete-input cache 比较。两个实际数值阶段均尚未运行；若选择更晚恢复点，应先据它生成新的 H 审计，不能继续称这里的 iterate0004 为最新。

完整未接受 raw 状态及已有域失败输入保存在 `strong-work/r4-third-inner-step-recovery/index.json` 所列独立硬链接中；这里没有为发布再次复制约 10 MB 的可再生迭代数据。它们也没有被误标为已接受曲面。原 r4 完整启动计划、初始 A、13 方向和源仍是再算入口。本小结果不改变课题未完成、尚无新耦合前缀接受的状态。
