# m3 圆化 λ=.0002：真实尾验证仍未过原门

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：有限真联立的失败记录；没有接受圆化 prefix。

保持已登记 β₀=4.625/q=.040 接受态、圆化 a=.21/b=.08、补弧
转接 .16、严格主频锁定、M8、尾 depth8/parts8/steps16/N128，
将前次 λ=.002 缩至 .0002。旧接受 prefix 与 final tail 的 hash
以及完整命令、来源均记在同名 scalar record 中。

两次原实际尾调用（预热及 Jacobian）都通过原 2e-9 门，残差
1.3767973594052425e-9。随后前缀内解返回到候选真实尾验证路径，
第三次尾调用在 iteration 2 line search 失败，归一化残差为
5.506859394593783e-9；对应 minA=.7423002337027597、
minD=.9994287798009251。完整 summary 明确 solver_success=false。
与 λ=.002 的 Frenet 正根域失败不同，本次没有在那一处终止，
但真实候选尾并未接受，故仍不是新圆化锚点。

本笔不把几倍浮点单位的可能性称为已证残差下限，不放宽射击门，
不把已通过的旧 warmup 尾移植为新核心的解。下一次尝试保持
物理参数与 λ=.0002，仅将 multiple-shooting parts8→16，利用
原 worker 的 warm remesh 检查更细有限射击表示；仍须完整 actual
边界验证与 2e-9 终门。它不是只凭网格改变便完成的同 g 证明。

复现用已发布 `continue_round_core.py`，输入 β4.625/q040 接受态
及其 final tail、原 actual port，`--homotopy .0002`。完整命令、
三个真实尾 response 的状态/末次迭代/审计及哈希保存在
`scripts/resume_m3/round_core_lam00002_failed_record.json`。没有将
失败场数组写入仓库。
