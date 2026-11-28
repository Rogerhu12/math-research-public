# R87 新剖面 λ=0.032 / M=16：仅原 metric 门未过

2026-11-28，/root/design_continuation。原 solver、RMS、物理 BC 及完整文件门通过，metric 大于1e−6，未接受；不是数学不存在。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 16 / 512 |
| 节点 | 596 |
| RMS | 9.8497611720024364e-07 |
| metric L1 | 1.6539305290029657e-06 |
| physical BC | 2.0026031711124716e-19 |
| 实际 audit mean / 原下限 | 784 / 784 |
| 实际 δ | 0.06809650689229084 |
| 原 BVP 加 audit 秒 | 95.801408403996902 |
| 完整 QR 次数 | 2 |
| 原接受步 / merit拒 / 域拒 | 4 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 315160 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-secant/attempt-000。

| 输出 | SHA-256 |
|---|---|
| run.json | 865b21bfc6dd018dbff98b06d3f73e259ac2fbe78b4b7af247cd06443e8a6a0f |
| 完整 raw | 6f002bcd5131474ba9bb1f20015714e1501823347d1426b333f74a29d5aa9a4b |
| physical.npz | 3431abaf198a953fa93e2038a0f501ec62e2a015840d3a82607eb26a73a1f4cf |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda032-m16-metric.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
