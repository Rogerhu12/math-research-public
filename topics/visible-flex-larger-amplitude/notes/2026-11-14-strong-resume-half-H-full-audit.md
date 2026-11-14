# 本轮半步完整 H 的原 full audit 已完成

**可信度：数值证据。** 同本轮全13方向半步的完整32维 H、同原物理尾参数和 RK12/depth8/512 角网，原 `FullTailPort.solve(H,jacobian=True,audit=True)` 已于2026-11-14 07:46:31 UTC 真实退出0，wall232.18秒、峰335832 KiB。

该计算使用本轮已经收敛的完整 raw shooting state。原加载器验证完整 snapshot 身份，576个已完成stage以原完整输入键和字节校验读取；原最终全尾audit实际执行。输出残差仍为 `1.4996029718764438e-9 < 2e-9`，audit 的 `actualMetric=4.063473682290762e-14`、`normalizedFullDefect=5.011321616195125e-11`、`minLeading=0.8596703075345694`、`minD=0.9999266370534152`，形式曲率读出为 `7.994254693544962`。这些量属于当前完整 H 的尾部，不能代替前缀或整闭曲面的接受与 reach 检查。

原 Node `close` 后真实返回0。随后相同13方向半步 r2 于07:51:37 UTC实际启动，35参数/1280角网和原门完全保留；原 exact-audited-H 入口确认第一请求的全部 H 逐位相同，并读取这份新审计包。初始前缀阶段 `live_client_started=false`，无闲置尾worker；以后真实不同 H 仍启动原工厂并做原求解/J/audit，响应记录后按既有选项关闭worker。

同名 `-r1/` 目录保留完整审计包、ready、config、source/argv、真实退出、小 snapshot manifest 和同半步r2计划。大 snapshot sidecars 没有复制进此小归档，不声称仅凭manifest可加载。新的可移植 raw 审计入口明确放弃可选旧快照，保留原 raw校验、非线性/J/完整audit；该raw复算路径已写成argv但本次尚未独立运行。当前实际审计使用的是已验证的本地完整快照。

前缀 r1 曾被SIGKILL，未得到Newton试步；现在r2继续同数学设计。这里没有新接受的前缀，也没有新的整闭曲面幅度结果。
