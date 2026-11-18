# 从完整有限 λ=.16 状态续接 λ=.32

**状态：已实际启动的数值续接，不是新解成功或严格存在性结论。**

λ=.16 的内解、真尾、原 BC、完整 prefix audit 与接缝都已完成。其 metric=$1.3837763095648974\times10^{-4}$ 尚高于最终目标；保留这一有限 continuation 锚，不将中间短缺改写为完成。原内解为 494 节点、2 次 mesh、5 次全步 Newton、零域/merit 拒绝。下一步据此预先选择 **λ=.32**，没有扫描 λ、增加 M 或重跑已接受的内解。

原 [通用 runner](../scripts/resume_m3/run_m3_trace_path_continuation.py) 的 SHA 仍为 `4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57`。本步保留原 M8、全部 8 参数和 base profile、7 个物理控制、`pscale`、gauge/warp=.06，以及原 BVP/Jacobian/五点域/Newton/BC/RMS/8outer/实际尾和后处理门。

旧完整 CP 是 `closed_work/m3-trace-path-lam016-seam-finish-v1/seed.json.gz`，SHA `770a54c6a1016f57e723091443a49c25bf9ebc9c7b81bca88b94600490fad8ec`。初猜使用保存物理 quintic 的全部 25 状态，做同基下新旧参考差回投及原 C² 入口修补；不把 raw 节点值冒称为逐位同一物理端点，不重做旧 mean-height 或初始 RMS。

主矩匹配唯一给出新定义核幅值 $q_{.32}=0.05722558496396052$。必要初猜的数值 core guard 是 lower=$.5064615035689665$、sample=$.5068257055358123$；有限投影修正最大 $1.5531231958885714\times10^{-15}$，入口残差 $3.3881317890172014\times10^{-21}$。投影修正不代表完整参考曲线的差界，数值 guard 不代表连续证书。

新完整 H 逐位匹配旧物理接缝 H，因此起始复用真实响应 `1470c291844bbc89cc9afe17d1a24a07aacad4728cf6fb92f8afb2da87961c57`。之后任何不同 H 都仍由原实际 worker/Jacobian/audit 处理。中间部分 lift 的入口不是定义积分核的精确曲线，不能据此调用最终 λ=1 圆弧的握持或 reach 结论。

121 个来源的 metadata 准备为 `f28bb7`、真实 exit 0。新 plan SHA：`36655808071ddf56a3dfd51cc98bd0572c3af0845b68db528ecb9dbb25c15bbc`。唯一 observer 为 **7336**、启动块 `398386`；2026-11-18 04:38:26 UTC 已观察到 running，目录为 `m3_work/trace-path-lam032-coupled-v1`。

[紧凑入口记录](../scripts/resume_m3/trace_path_lam032_coupled_entry.json) 保存全部必要参数、真实命令、原来源及初值数组/hash。本条不预认这一步的内解、真尾或完整 metric 终态；实际结果另记，最终固定 g 的加密收敛仍独立支付。
