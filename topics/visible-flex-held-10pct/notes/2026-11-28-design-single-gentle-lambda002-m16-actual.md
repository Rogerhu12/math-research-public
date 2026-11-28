# R87 新剖面 λ=0.002 / M=16：原完整有限门接受

2026-11-28，/root/design_continuation。实际原 BVP 已通过原 RMS、物理 BC、metric 和完整文件门；这是同一个新单级温和剖面的数值设计场。原 source/input、raw/physical SHA、全部数组形状、参数尺度及实际 mean 下限都经未修改的 accepted_original 校验。

| 量 | 实际值 |
|---|---:|
| 模态 / 求解角格 | 16 / 512 |
| 节点 | 580 |
| 原 RMS | 9.8737987257642128e-07 |
| 原 metric L1 | 5.6599749130925902e-08 |
| 原 physical BC | 4.5618888660984808e-14 |
| 原 audit mean | 784 |
| 实际 δ | 0.068095773962466674 |
| 原 BVP 加 audit 秒 | 45.233619598999212 |
| 完整 QR 次数 | 1 |
| 原 Newton 接受步 / merit拒 / 域拒 | 2 / 0 / 0 |
| QR driver 全程核计最大RSS KiB | 310192 |

q=warp=.012，原门仍为 RMS≤1e−6、metric≤1e−6、physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000。没有因本次通过而减少状态、支撑列、δ列、域检查或真实角度 mean。δ 仍在新 R87 扩盒 [.063,.069]。

本次工作目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-low-modes/attempt-001。

| 输出 | SHA-256 |
|---|---|
| run.json | 41350a3304db38d1429e679134bb60f4aee7bbd3891357b20d9c28713d9f871b |
| 完整 raw | 2ddf3fd9a3ac033279e6a9e3b3e9d0339492391fd29e8f21cf243045d6246aba |
| physical.npz | 67e7f27073d7323176a0b08e88996943ccb2e84ca6b13a5de726323517f257d6 |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda002-m16-actual.json)含实际命令单行来源、原 source/input、所有门和完整QR小摘要。未把仍在增长的外层日志冒称冻结；数组未入 Git。

本次是有限线性-port 数值场。λ=1 准确圆弧、实际非线性 DN、同一最终 g 的精化、连续全域几何、闭合与 README 完成标准尚未由本条支付。原控制器从真实接受场继续后继λ，不等待阶段报告。

本次 M8→M16 的原完整 exact-lift 转移还检查了全部参考六 jet；其真实 transfer 记录与 raw SHA 一并纳入 JSON。旧 M8 仅作未接受初猜，原 metric 失败保持登记。
