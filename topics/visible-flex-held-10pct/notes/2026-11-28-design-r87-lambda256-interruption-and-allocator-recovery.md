# R87 λ=.256/M32：真实工程终态与完整状态的窄恢复

会话：Astra-held10-7c4e33ee-20261128。下列事实来自实际 tool/owner 返回和原日志；不将进程终止解释为数学失败或已证明的内存不足。

## 已实际返回的旧过程

唯一连续链的 tool session 80642 在 2026-11-28 19:21:14 UTC 真实结束：observer/controller 为 3，原 `.256/M32` child 为 −9，owned session 剩余进程为 0。实际运行 346.155172021 秒，子进程最大 RSS 为 1,092,364 KiB。完整第一 CSR/QR 和五次完整方向均曾返回。原 Newton 接受两步，步长依次为 1 与 1/4；这只表示原 Newton 步已接受，整个 BVP 的 RMS、物理边界和 metric 审计均未返回。

最新第二次 pre-J checkpoint 与第二次已接受 Newton 步保存的 x、Y、p、pscale 文件 SHA 相同：`97ec9d07c25d18cd7da7dbade7d5f0902fc1c48b3bbad2ee5b22abe432ed4279`，包含全部 1185 个节点、97 个状态分量与 32 个参数。第二次 pre-J 资源门曾真实通过；没有第二次完整 CSR 组装返回或 factor-start 记录，不能据此确定终止发生于偏导还是随后组装的哪条指令。仍以原 `.128/M24` 为最高全门接受锚。

第一次两类映射完成后，实际匿名 RSS 为 110,100,480 字节；第二次 J 前匿名 RSS 为 401,203,200 字节。旧 factor 的映射文件已经正常释放。owner 真实 join 后运行限定目录清理，返回 `removed=[]`，未删除任何场或检查点。现有 cgroup 限额/事件不可读，尚不能证明 −9 的原因，也不能从主机 MemAvailable 推出进程没有额外限制。

## 唯一新恢复

保持所有旧源码不动，增加两个独立入口：`prefix_csr_prefactor_budget_trim_driver.py` 在每次完整 J 的实际资源预算基线建立前调用既有 `collect_and_trim`；`prefix_csr_prefactor_trim_qr_driver.py` 在原完整 solve 前后调用同一函数。该函数仅执行 Python GC 与 libc `malloc_trim(0)`，释放已无引用对象和分配器中已空闲的页，不清除活缓存、字段、CSR 元素或 QR 因子。实际 RSS/匿名 RSS 的调用前后数值逐次保存；不能预先将这项方法说明称作已降低峰值。完整 CSR-before-QR/all-factor 映射、残差精化、两 store 的实际 DONTNEED 门、原 Newton/网格规则及唯一原 metric 审计观察器全部保留。

两个源静态编译和真实 `--help` 均返回 0，没有另组矩阵或重新验证已核矩阵。由上述完整未接受状态作 literal restart，目标仍为 `.256/M32`、角格 1024、q=warp=.012、RMS 容差 2e−7、物理边界 2e−9、metric 1e−6；不重新计算两源升模、割线或已完成两步，也不因为工程退出二分 λ。

该唯一恢复于 19:27:39.251748 UTC 真实启动，tool session 77523。命令、所有源和输入字节由相邻 JSON 绑定；outdir 为 `held10-design-work/R87-strict-lambda256-M32-trimmed-mapped-recovery-20261128`。此记录只登记启动与真实旧终态，新完整数学门尚待原返回。

原始小记录、完整命令、不可变输入 SHA 和实际阶段细节见 [JSON](2026-11-28-design-r87-lambda256-interruption-and-allocator-recovery.json)。所有数组只在 scratch；本记录不是曲面完成证明。
