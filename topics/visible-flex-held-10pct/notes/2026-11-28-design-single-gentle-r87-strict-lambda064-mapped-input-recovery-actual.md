# R87 新剖面 λ=0.064 / M=24：原完整有限门接受

2026-11-28，/root/design_continuation。通过未修改的 accepted_original：完整来源、raw/physical SHA、所有状态和参数形状、cubic、原 RMS/BC/metric 及实际 mean 均核过。

本条是已登记低 λ 场的必要输入恢复，不是新的 λ 前沿；较严容差按实际执行值记录。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 24 / 768 |
| 节点 | 1134 |
| RMS | 1.9779458545532175e-07 |
| metric L1 | 1.284368451621618e-07 |
| physical BC | 2.6538521277607947e-19 |
| 实际 audit mean / 原下限 | 1168 / 1168 |
| 实际 δ | 0.068097465711786459 |
| 原 BVP 加 audit 秒 | 314.88332218699998 |
| 完整 QR 次数 | 2 |
| 原接受步 / merit拒 / 域拒 | 4 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 664340 |

q=warp=.012，仍是同一新单级温和剖面。实际原门为 RMS≤1.9999999999999999e-07、metric≤1e−6、
physical BC≤2.0000000000000001e-09、bc_tol=9.9999999999999995e-08、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-strict-mapped-material-continuation-20261128/attempt-000。

| 输出 | SHA-256 |
|---|---|
| run.json | 696a79d114b835ec8bc4eb8a1a3acd5a166fe5bd39003c53e0d89a36e8ff6449 |
| 完整 raw | b5945fee2e832037379d2108c5f997d1c426e3de13ab99cec34bab4cb9ef377d |
| physical.npz | af16685f7421761c472d053eb12bef5d62347c03ce0a6dfd629d5c392acad699 |

[同名实际 JSON](2026-11-28-design-single-gentle-r87-strict-lambda064-mapped-input-recovery-actual.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
