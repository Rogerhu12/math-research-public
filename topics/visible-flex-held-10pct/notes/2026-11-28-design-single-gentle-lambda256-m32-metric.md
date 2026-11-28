# R87 新剖面 λ=0.256 / M=32：仅原 metric 门未过

2026-11-28，/root/design_continuation。原 solver、RMS、物理 BC 及完整文件门通过，metric 大于1e−6，未接受；不是数学不存在。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 32 / 1024 |
| 节点 | 850 |
| RMS | 9.9324272546622891e-07 |
| metric L1 | 1.2858438818876804e-06 |
| physical BC | 2.6144028623331512e-19 |
| 实际 audit mean / 原下限 | 1552 / 1552 |
| 实际 δ | 0.068107136690425951 |
| 原 BVP 加 audit 秒 | 419.99758199800272 |
| 完整 QR 次数 | 2 |
| 原接受步 / merit拒 / 域拒 | 6 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 1145472 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-high-modes/attempt-000。

| 输出 | SHA-256 |
|---|---|
| run.json | d3cbc1415e0a638a113ef832edaf615907501678b8928a5d27ffbca2de8fc9ab |
| 完整 raw | 2ba3f8ceb400e84c4c15f7135b8c54fe75786ab1ff623b6b6400d9190428468c |
| physical.npz | c211519be3ffae5069fe086f7ec2871b845dfa54dae4e4d59435f6865048acdc |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda256-m32-metric.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
