# run02 当前可观察状态：只读记录

记录时间：2026-11-10 05:08:12.569607 UTC。这是运行状态观察，不是新的数学结论或 BVP 成功证据。完整元信息在 [同名 JSON](2026-11-10-78718-numerical-run02-observable-state-01.json)，10,802 B，SHA-256 `6223537c974e291142cb8ed3af87ab70d251dc32dcdb65521874ae2fad90c578`；本次实际只读工具回执为 `906746`，自然退出 0。主进程工具会话 `44394` 仍由 root 持有；本代理没有取得该会话的自然退出。

## 直接观察

- guard 保存的事件只有 `started`，其事件内 elapsed 为约 0.000557 秒。该文件 mtime 为 04:07:30.927779 UTC，距离本次观察为 3641.641828 秒。这是**文件年龄**，不能冒充当前进程的实测 elapsed 或存活心跳。
- tail worker 的实际 trace 保存了绝对时间：第一次 DN 请求为 04:07:37.003 UTC，响应为 04:10:10.703 UTC；该次响应记录 `elapsed_ms=153700`。这是首个已结束 DN 调用的耗时，不能外推为当前内层 BVP 耗时或子阶段。
- producer 最新的持久化元信息是 04:10:11.165630 UTC 的 reproduction。它仍是 `RUNNING_ORIGINAL_TRUE_OUTER`，含一次 before-call 审计、没有 after-call 审计、没有已完成的 spectral-coordinate 调用。检查时 CP、原 summary 和 guard-completion 均不存在。单独 first-DN 审计文件由我们的审计器写出，不计作 producer 的活动信号。
- 这次针对共享输出路径的 `statvfs` 测得 available 为 46,165,999,616 B。它是观察时该路径的磁盘状态，**不是 guard 的最近轮询记录**。当前 guard 文件没有暂停或恢复事件。声明的资源配置为 DATA 每进程 6 GiB、Node heap 1536 MiB、磁盘暂停阈值 512 MiB、恢复阈值 768 MiB；这不是实测 RSS。

## 为什么不能由文件静默判断活跃状态

原 guard 每约 2 秒轮询磁盘，但只在启动、磁盘暂停/恢复、异常或结束时写记录；它不保存绝对 wall-start、最近轮询时间、运行中的 monotonic elapsed、RSS 或 CPU。选定 BVP 包装器只在调用之前及其返回/异常后的 `finally` 写审计；它没有内层 Newton 或网格迭代心跳。在该 affine 内层 BVP 返回前，也不必再次请求 tail worker。因此，当前文件不能识别它正在 Jacobian、LU、线搜索还是其它内层步骤；文件不变也不能证明活着、死锁或退出。

本次没有检查其它执行命名空间的 PID，没有发送信号、注入监视器、修改源码、改变参数或启动第二个求解。root 持有会话的真实工具结果与最终退出仍是运行出口证据。
