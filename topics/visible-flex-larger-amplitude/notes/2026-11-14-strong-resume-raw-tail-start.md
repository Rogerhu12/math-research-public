# 原完整尾快照的保守失配与真实 raw 状态重启

margin325 候选的本地实际 r2 于 2026-11-14 06:27:44 UTC 启动，51.7404 秒后在尾工厂初始化退出 1。实际错误是原 `readFullFlowTangentSnapshot` 的完整 tail/physical/backend/source identity 拒绝；前缀 J/QR 尚未开始。这不能记成非线性数值失败或接受结果。

已查出一个足以造成拒绝的真实差异：原 snapshot 的 adapter MJS 树有 52 项，当前稳定源码树有 61 项；原 52 个文件全部 SHA 相同、没有缺失，另外 9 项是后来加入的诊断模块。原 `strong_exact_stage_engine.mjs` 明确保守散列整个计算目录的 MJS 树，因此无关诊断源增加也会产生缓存 miss。固定 source revision/manifest、frozen reference ready 和 calibration ledger 的 SHA 均与旧记录相同。尚未取得当前全新 snapshot，故不先断言其余每个浮点身份字段也逐位一致。完整新增文件列表、哈希和退出记录在配套 JSON。

新 `strong_20261114_raw_tail_start_actual_bvp.py` 是明确的 raw-state 启动入口：在原全切线 client 安装处关闭可选 `checkpoint_snapshot` 预载，保留原 checkpoint 的全 577×64 状态、完整 H、全部非 IO 参数和 raw-node；所有原 MJS、身份比较器、全 H 非线性求解、变分 J、正性、line search、物理 BC、RMS 和最终 audit 均不改。当前工厂以后新算出的切线仍正常保存和消费。仅删除命令行 manifest 不够，因为原 packet 的 `fullFlowTangentSnapshot` 也会自动触发预载；此入口显式选择不用该可选初猜，不伪造其身份。

r3 已于 06:34:37 UTC 真启动。原 raw warm 检查报告全部非 IO 参数、完整状态和 raw-node 相同；首次实际新 H 的第一系数为 −2.9802342542638402e−5（A 的约 1.05470339 倍）。原 harmonic warm 后，首轮 576-stage 完整 Newton residual 为 5214.026677，完整全步被原 line search 接受，下降到 0.0392571520。其完整 iteration checkpoint 已真实落盘；写本条时仍在下一轮完整 J，不称作完整尾收敛，更不称作新前缀或课题完成。后续继续该进程与原最终门。
