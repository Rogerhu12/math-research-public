# R87 新剖面 λ=0.256 / M=24：仅原 metric 门未过

2026-11-28，/root/design_continuation。原 solver、RMS、物理 BC 及完整文件门通过，metric 大于1e−6，未接受；不是数学不存在。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 24 / 768 |
| 节点 | 848 |
| RMS | 9.9325164846499951e-07 |
| metric L1 | 8.8413969102967086e-05 |
| physical BC | 2.6295281587197332e-16 |
| 实际 audit mean / 原下限 | 1168 / 1168 |
| 实际 δ | 0.068106853250293864 |
| 原 BVP 加 audit 秒 | 481.97505186600029 |
| 完整 QR 次数 | 4 |
| 原接受步 / merit拒 / 域拒 | 14 / 1 / 0 |
| QR driver 核计最大 RSS KiB | 690168 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-secant/attempt-004。

| 输出 | SHA-256 |
|---|---|
| run.json | 81bfd18ce47584a84537e8428aaf2020a9d1c5c9d59a3deb18d110f7a52f4bb7 |
| 完整 raw | 5e6fe410bdc205380d364f5da700480e846300ad80a14a676508586325ee437a |
| physical.npz | 23688d21782eba5fabafb2abddfdb989b1c45b82312d2c8090441cc086f56dcc |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda256-m24-metric.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
