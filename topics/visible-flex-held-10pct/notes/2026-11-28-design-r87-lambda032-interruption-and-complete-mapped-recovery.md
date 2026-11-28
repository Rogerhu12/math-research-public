# R87：同 λ=.032 的真实 −9 中断及完整映射恢复

原连续链在 2026-11-28 18:37:16.282520 UTC 真正结束：数学子进程返回 −9，控制器与 TTY 73924 返回 3，owner 清理后剩余活成员 0。`attempt-000` 尚无 raw/audit 返回，未通过原 BVP 门；原控制器正确记录工程中断且没有二分 λ。现有 cgroup 路径没有可读 memory.events 数值，不能将 −9 归因为已证 OOM 或数学失败。

结束前已完成 3 个完整 QR，并保存 5 个原 Newton 全步。最新完整 1051×73 状态、24 参数的 SHA-256 为 `904db0f97d8194bd4292497d29745cf420fc28c0a4053fb3d62cf229b08a634f`。它是一次原 Newton 步后的完整未接受 BVP 状态，不能当成已经通过 RMS/metric 的场。内核所见子进程最大 RSS 为 776332 KiB，最大单进程采样为 783998976 字节；这些有限观察不等于已知所有进程的总峰。

在真 owner join 后，把该最新状态独立保存在 `R87-strict-lambda032-M24-mapped-recovery-20261128-input`，连同原 run、checkpoint 元数据、控制器终态及回收回执。没有回头重算旧升模初猜或已完成的 5 个步。

2026-11-28 18:44:29.674572 UTC，唯一新 TTY 65581 实际续入同一个 $\lambda=.032$、$M=24$、角格 768、$q=\mathrm{warp}=.012$ 原方程，literal 恢复全部原节点与参数。原 RMS 容差 $2\times10^{-7}$、BC $10^{-7}$、物理 BC $2\times10^{-9}$、metric $10^{-6}$ 及全部原域、全模式、线搜索和 mesh 规则保持。RHS 分块为 8。

新入口复用此前已检查的完整 CSR 在 QR 前映射、全部 QR 持久数组在构造后映射及逐次真实清页规则。唯一新小源码 `prefix_mapped_chord_checkpoint_driver.py` 保留原 accepted-step checkpoint 逻辑，只把委托预算换为已冻 `prefix_csr_prefactor_budget_driver.py`；没有新增矩阵测试或替代方程。它的 SHA-256 是 `0ea037f2f8a0fffc437075b89eb7d8bcfd4e57a3e9f01dae3293b8807fb3a139`，compile 与组合 help 实际返回 0。

启动时实际 MemAvailable 2728595456 字节，超过该完整阶段预算 1867210752 字节；可用磁盘 8284680192 字节，超过完整 backing 加 512 MiB 余量的 922841775 字节。每次新 Jacobian 前仍按当前节点及实测 RSS 重新检查预算。原构造峰与完整线性求解的热页峰仍计入；不把映射逻辑字节当成额外可用 RAM，也不把清页说成消除了所有峰。

新命令记录 SHA-256 为 `0f0ae97127f44b68ba592270686709b8f2dbe55cd5cddf31dd142adb56a508a5`。仅在新 child 确认终态并实际 join 后，才用冻结的 `mapped_complete_storage_cleanup.py` 清理这个唯一 owner 的临时映射目录；原节点、场与验证证据均不在清理范围。本记录形成时新 BVP 尚未终结，不声称接受或新数学前沿。
