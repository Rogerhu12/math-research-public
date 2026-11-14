# 全方向半步的外部 SIGKILL 与保持同设计的续算

**可信度：实际进程记录；没有新接受前缀。** 2026-11-14 07:38:45 UTC，半步 r1 的原 supervisor 通过 `wait4` 观测到自身子进程由信号 9 终止：`exitcode=-9`，外层真实返回 137。此前没有向 supervisor 发停止信号，记录的 `received_supervisor_signals=[]`。子进程峰 RSS 498652 KiB，wall 1133.85 秒。原因没有确定，不能仅按这些数据断言内存上限，也不是数学域失败。

终止前，完整半步 H 已由原非线性尾工厂收敛至 `1.4996029718764438e-9`，并已返回完整 J/snapshot。前缀仅进入首次 J 装配；2590 节点、batch24 共需216次 J callback，最后心跳记录195次。首次完整矩阵尚未返回，没有因子分解、Newton 方向或试步。初始 scaled collocation 最大值 `0.08984367968223199`、边界最大残差 `6.514698234559324e-8`，不能据此说“半步也停滞”。

完整最初 iterate、本轮 H/J/snapshot、全部 sidecars 以及退出/心跳/ownership 等27件文件共约30MB，已在 `strong-work/margin325-half-r1-recovery` 用硬链接保留并记 SHA。本小归档保留索引、原计划、真实退出及关键事件；不声称大恢复 sidecars 都在本小包内。完整本轮尾响应另在 `2026-11-14-strong-resume-tail-half-scaling-r1/` 保存。

保持全部13方向半步、35参数、1280角网和原接受条件。已于07:42:39 UTC启动对刚收敛本轮 H 的原完整 audit；待该真实审计完成，使用现有 exact-audited-H 及 `--release-tail-worker-between-responses` 入口，使前缀 J/QR 期间闲置 Node 退出。旧 A 的审计绝不移植到新 H；第一 H 的完整精确匹配和以后新 H 的原非线性/J/审计都保留。这个资源安排不把当前半步缩为四分之一步。
