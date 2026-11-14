# 同一半步：完整新 H 审计后，第二次前缀首 J 仍被外部 SIGKILL

这是一条实际执行失败记录，不是数学失败或收敛结论。

## 已观察到的执行

`loop-margin325-half-actual-r2` 于 2026-11-14 07:51:37.452885 UTC 启动，07:55:16.238411 UTC 由原监督进程 `wait4` 收到退出。原始返回为 `−9`、终止信号为 `9`，外层返回 `137`。实际墙钟 218.792568 秒，峰值 RSS 503680 KiB；监督进程收到的信号列表为空，没有自动重启。

这次使用的是刚真实求解并完成原完整审计的新半步 H，而非旧 A 的审计。第一条实际 H 请求与该包逐位相等，原 exact-audited-H 分派确实复用了这同一个 H，且 `live_client_started=false`。所有记录到的前缀心跳都没有直接子进程；因此这次执行不再有闲置 Node 尾 worker 叠加。

完整 Jacobian 需要 `2 ceil((2590−1)/24)=216` 个原回调。最后一条完成记录为第 60 个（201.926 秒），随后仅有未完成后续调用的日志。完整矩阵、QR factor、线性解和 Newton trial 的计数均为零；不能称为半步在数学上停滞。首个 scaled collocation/BC 残差同前次重试：0.08984367968223199 / 6.514698234559324e−8。

## 保存及重试

`strong-work/margin325-half-r2-recovery/index.json` 对 23 件、10410317 bytes 的实际输出和原 argv 逐件保存 SHA256；包括完整 iterate-0001 的 x/y/p/cubic 分块、同 H 包、身份记录及真实退出。该目录为完整本地 hardlink 保存。本条小包只收真实事件、计划和索引，不把可重算大块复制一遍，也不声称其已经外部发布。

同一半步已经于 08:02:16 UTC 启动 `r3`。仅把现有 CLI 的 radial/collocation 批量 24 改为 12，把隔离 RHS 线程 4 改为 2，以降低临时矩阵峰值；仍为全部 13 个物理方向的同一半步、M32、1280 角、35 个参数、2590 初节点及原所有数学验收门。同一个新 H 完整审计包和释放闲置 worker 入口保留。不因外部 kill 缩成四分之一步。

## 资源事实和未知原因

本任务 J/QR arena 已通过原 `--disk-temporary-parent` 放在 strong-work 真磁盘；没有误用 /tmp 的 tmpfs。07:59 附近 host 的 `/proc/meminfo` 报可用约 1.62 GB、Shmem 约 4.07 GB；另只读观测 /tmp 占 3.0 GB、/dev/shm 占 430 MB。未动共享环境中的他人文件。当前命名空间没有可读 cgroup 挂载，故不知道实际信号来源或具体资源上限；不能把 SIGKILL 确定归为 OOM。

[r2 真正 wait4 退出](2026-11-14-strong-resume-half-prefix-second-sigkill-r1/resource.json)、[最后 J 事件](2026-11-14-strong-resume-half-prefix-second-sigkill-r1/disk-events.jsonl)、[完整保存索引](2026-11-14-strong-resume-half-prefix-second-sigkill-r1/preservation-index.json)、[同数学候选的 r3 计划](2026-11-14-strong-resume-half-prefix-second-sigkill-r1/same-design-smaller-batch-retry-plan.json)均在本地。r3 的未来结果须单独依真实输出记录，本条没有宣称它接受或完成。
