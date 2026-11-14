# 固定 g 上的真实尾边值振幅 continuation

状态：**数值初猜路径，尚未执行本次 continuation。** 作者 `/root/coupled_prefix`，2026-11-09。目标仍是 M15 自由 cut 仿射 prefix 预测对应的宏观边值；不更改物理度量或最终问题。

## 1. 固定目标与模索引

从辅助 CP 的 `predicted_cut_height` 原样读取 $H^{\rm target}$。这是已经包含 $\sigma q$ 的物理 height 系数；DN 的原 `solve(height)` 内部只做一次除以 $r_{\rm cut}^4$。控制器不再乘除 $r,w,m$。存储下标 $j=0,\ldots,M-1$ 的路径为

$$
H_j(s)=s^{j+1}H_j^{\rm target},\qquad 0<s\le1.
$$

物理 Fourier 频率是 $3(j+1)$；幂次用谐波编号 $j+1$，不是频率 $3(j+1)$。当 $s=1$ 时显式复制冻结的原目标向量，避免以累计更新误差代替目标。辅助 CP 与上一次原 prefix restart 实际请求仅有最大 $1.6941\cdot10^{-21}$ 的重算舍入差；本控制器严格绑定 CP 所存向量，最终 prefix 仍会做它自己的原实际 BC 校正。

## 2. 原方程与初猜路径

保留原 M15/N256、depth12、p8/s32、solveTolerance $2\cdot10^{-9}$、guard .05 及全部 g 参数。仅清除旧 `initialCheckpoint`，从 $s=.25$ 的原线性 shooting 初猜开始；不再次把已停滞的 FAILED 宏观状态作为第一步。

每次请求都由同一个已审原 trial worker 解真实有限非线性 DN，`jacobian=False,audit=False` 仅省去额外输出端口 tangent 和几何审计，原 shooting Newton 仍用原全 Jacobian、原 RK、原 root、原 guard 和原残差。成功必须同时满足 `converged=True` 和原归一 residual 严格小于原 tol。$s<1$ 的成功都明确是 WARM ONLY，不匹配整个目标 prefix，不是宏观联解。

起始步长 $.125$，最大 $.2$；成功若至多3个 Newton history 节点，下次步长最多乘1.5；超过7个则减半。失败时从最后成功的 $s$ 减半目标增量，保留完整失败响应。原 worker 只有 `sol.converged` 才更新 `last`，并且每次初猜复制其数组，因此失败状态不会覆盖最后成功状态。若首个小边值也失败，则继续将起始 s 减半；这是换一个更小的初始化请求，不改方程。

有限诊断预算为最大64次请求、最小步长 $1/4096$；达到预算的状态必须标为 UNCONVERGED，可从最后成功 CP 用显式 `--resume-checkpoint/--resume-scale` 在新 stem 继续。不得将预算耗尽说成不存在原解。恢复时逐值检查保存请求确实等于同一固定目标路径上的 $H(s)$，并要求真实 residual 已过原 tol。

到 $s=1$ 后，再明确调用原 `jacobian=True,audit=True` 请求。它完成时也只支付目标有限 DN；原 prefix 仍为 UNSOLVED，随后必须在原真实耦合器里重新校正最终 BC。

## 3. 保存与代码范围

控制器 `db6f-prefix-tail-amplitude-continuation.py` 只调度边值请求、检查原成功条件、调整 s 步长并保存账本。底层 worker/core/split 与已审 trial 版本相同。

派生 `db6f-prefix-tail-continuation-client.py` 只把完整响应的写入改为先写/fsync 临时文件，再用同文件系统 hard link 原子发布新名字（拒绝覆盖已有响应），并正确记录自身源 hash；不改请求、缓存、worker 或数学。差分绑定在 `2026-11-09-db6f-prefix-tail-continuation-source-map.json`。

当前迭代态沿用已审 worker 的原子 recovery checkpoint。每个完成响应按唯一 call 编号保存；响应回到控制器后才把这一 call 的 trace/trials 原子改名为闭文件，再发下一请求，避免持续累积成大日志。控制器 progress 也以原子替换写入，含当前请求 s、最后成功 s/CP/hash、所有完成/失败响应。启动 input-bindings 不改写，完成 reproduction 单独写入。所有单文件小于5MB，完整数值响应 gzip 存盘。
