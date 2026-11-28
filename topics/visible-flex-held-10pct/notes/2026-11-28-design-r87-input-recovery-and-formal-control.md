# R87 必需输入恢复与正式阶段控制

**性质：必要输入恢复和执行入口准备，不是新数学结论。** scratch 目录在当前工作区视图不可读后，只恢复当前 R87 路线所需的原 70 份源码、port/chart 和已发表的线性校准；没有回算旧 $q=.06$ 支，也没有重跑已登记的根搜索。

新入口 `scripts/resume_20261128/design/restore_single_gentle_inputs.py` 顺序调用原历史源恢复、稀疏源安装、多段 profile 安装、共享源安装、原 port 导出和原 reference chart 生成。TTY 55603 实际 exit 0，耗时 300.152428739 秒。全部历史文件均由原 manifest 核哈希；chart `dc85dda…` 与 M24 port `42369d…` 恢复一致。公开小记录内嵌的两份 calibration 和 root-profile 经原 JSON 序列化后，逐字 SHA 分别等于 `1f2ea915…`、`d2d00683…` 和 `bf3233a3…`；所有原校准输入/源码绑定再次核同。只有通过逐字 SHA 才落回原路径。

M8 port 另用原 exporter 从当前明确配置真实生成，前八条斜率与原 M24 port 相同；其 JSON SHA 为 `2936d369…`，不假称与旧路径记录逐字同。原完整线性 seed 实际 exit 0，2.387569206 秒、峰 84732 KiB，得到 415 节点、完整 $25\times415$ 状态及全部 8 参数；raw SHA `f368c3ad…` 与遗失旧未接受初猜逐字一致。这仍是未接受初猜。

新严格 $\lambda=0/M8$ 原 BVP 于 2026-11-28 17:30:22 UTC 以 TTY 81483 实际启动。`tol=2e-7` 加强径向求解，原 BC、physical BC、全部域、完整模态和 metric 门保持；完整 QR 与原 chord-step/nodal checkpoint 入口不变。此记录落笔时尚未看到终态，不能预报通过。其后只把必要重生场作为继续 $\lambda=1$ 的输入，不重复登记为新设计前沿。

独立 `run_design_stage_control.py` 保留原 bootstrap/lifted-secant、全部接受与失败分支。新 `--stop-after-stages` 和 `--stop-request` 在每次已完成阶段的真实接受锚更新后、每个新子进程前以及资源等待中检查。停止请求必须准确匹配 scope、绝对 outdir、nonce 和 `stop_after_stage` 动作；正在求解的原 BVP 先完成，其接受决定不会被截断。正式停止另以 exit 4 和 `design_stopped_on_explicit_request` 记录，不作数学失败或 λ 二分；原 bootstrap 的滞后 `result` 在这个真实边界同步到实际锚。没有未来日志占位或人为 FileExists 屏障。

新 controller 仅实际通过 compile/help，尚未用于 BVP；其生产控制将在后继原阶段中使用，不另为流程重跑数学计算。全部精确命令、源 SHA、恢复记录 SHA、当前 λ0 命令和实际初猜绑定见[小记录](2026-11-28-design-r87-input-recovery-and-formal-control.json)。可再生数组留在 scratch，不入 Git 或 Release。
