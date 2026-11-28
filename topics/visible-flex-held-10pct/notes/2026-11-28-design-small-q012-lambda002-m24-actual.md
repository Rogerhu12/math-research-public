# 小 q 原设计：λ=.002/M24 的真实全门返回

从真 q=warp=.012、λ=.002、M24 的完整 615 节点原 nodal checkpoint `ef8e0342…` 逐位恢复，独立原命令以 RHS32、已核完整 CSR/QR、原完整方程/入口/mean/物理边界和全部验收门运行。此前该场首个完整 QR 方向后进程被 −9 终止；原因没有证实，也没有数学失败判断。因为没有保存更后的状态，此次必要恢复确实重新计算该 checkpoint 之后的第一完整 J；M8/M16 已付步骤没有重算。

实际子进程于 2026-11-28 14:15:50 UTC 返回 0。原 BVP 在 615 节点通过，RMS 为 9.974606330775772e−7；原 metric 为 1.407536801700711e−7；物理 BC 为 1.9420074062002312e−15；原 mean 1168。原 raw/physical、原 source/input、实际包装命令 source 的 SHA 均重新核过。原 finite gate、prefix gate 和 complete initializer gate 全部为真。

独立 observer 只观察真实自有子会话，不修改数学求解。它逐身份采样 RSS，并在真 join 之后记录 kernel RUSAGE_CHILDREN：最终最大 RSS 为 518732 KiB，原数值运行 80.27182643499691 秒；所有 owned descendants 已回收。这个 kernel 峰不等于此前在日志某一时点看到的峰，也不用于反推此前 −9 的原因。

这只是新 q=.012 输入上的有限前缀结果。小 q 并没有免掉原 metric 所需的 M24；实际径向节点比 q=.06 的 879 点少。当时接着以该真场续入 λ=.004，并计划在 λ=1 后续 q/warp 到 .06；此后 R87 新物理 profile 的 q=.012 已另立为可选最终 g，不再强制回 .06。两条物理输入不混作割线，最终仍须完整 nonlinear DN、闭合、族、reach 和题目其余标准。相邻 JSON 给出可再生命令及全部来源绑定。
