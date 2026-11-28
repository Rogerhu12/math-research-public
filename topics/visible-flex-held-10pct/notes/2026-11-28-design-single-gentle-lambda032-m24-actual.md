# R87 新剖面 λ=0.032 / M=24：原完整有限门接受

2026-11-28，/root/design_continuation。通过未修改的 accepted_original：完整来源、raw/physical SHA、所有状态和参数形状、cubic、原 RMS/BC/metric 及实际 mean 均核过。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 24 / 768 |
| 节点 | 596 |
| RMS | 9.844208005706405e-07 |
| metric L1 | 1.7519170045267722e-07 |
| physical BC | 6.9175300042133e-15 |
| 实际 audit mean / 原下限 | 1168 / 1168 |
| 实际 δ | 0.068096504725549928 |
| 原 BVP 加 audit 秒 | 92.185491657997773 |
| 完整 QR 次数 | 1 |
| 原接受步 / merit拒 / 域拒 | 2 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 590796 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-secant/attempt-001。

| 输出 | SHA-256 |
|---|---|
| run.json | 7b69996a5911a82a0be1f24b44f2a036fd69210b6f1759d12087b7a6591a74d7 |
| 完整 raw | 20f0c99377b8336dff3b3ab2a334160b890a63b4bcb154e62e6519d080d08427 |
| physical.npz | 431aa561e5b0faa12fc88667a79371c544a1659100a2b795a83d9d9d5d72621f |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda032-m24-actual.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
