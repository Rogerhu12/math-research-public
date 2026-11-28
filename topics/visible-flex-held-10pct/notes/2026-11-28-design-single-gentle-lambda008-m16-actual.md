# R87 新剖面 λ=0.008 / M=16：原完整有限门接受

2026-11-28，/root/design_continuation。通过未修改的 accepted_original：完整来源、raw/physical SHA、所有状态和参数形状、cubic、原 RMS/BC/metric 及实际 mean 均核过。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 16 / 512 |
| 节点 | 583 |
| RMS | 9.9751510432203994e-07 |
| metric L1 | 2.0235209757537695e-07 |
| physical BC | 3.0545736033773475e-19 |
| 实际 audit mean / 原下限 | 784 / 784 |
| 实际 δ | 0.068095906968990622 |
| 原 BVP 加 audit 秒 | 86.470340794003278 |
| 完整 QR 次数 | 2 |
| 原接受步 / merit拒 / 域拒 | 5 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 313256 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-low-modes/attempt-003。

| 输出 | SHA-256 |
|---|---|
| run.json | 3588570f45e52932be91f29b719e5f343a2fac3432ab5839cf94618f0a8e0d66 |
| 完整 raw | db3fd0f09390e7ff7edab996e3baf4b49b6a6e55c37397f46d5389907820ed06 |
| physical.npz | 22b5228682cd71318dd9fc2bb42ecfda8b671a20af379ad340b7c01fab5dfc6a |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda008-m16-actual.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
