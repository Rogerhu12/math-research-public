# R87 新剖面 λ=0.128 / M=24：原完整有限门接受

2026-11-28，/root/design_continuation。通过未修改的 accepted_original：完整来源、raw/physical SHA、所有状态和参数形状、cubic、原 RMS/BC/metric 及实际 mean 均核过。

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | 24 / 768 |
| 节点 | 642 |
| RMS | 9.9192254122979041e-07 |
| metric L1 | 6.3560235491899154e-07 |
| physical BC | 6.8425527807710494e-17 |
| 实际 audit mean / 原下限 | 1168 / 1168 |
| 实际 δ | 0.068099944414526867 |
| 原 BVP 加 audit 秒 | 208.06506906200229 |
| 完整 QR 次数 | 2 |
| 原接受步 / merit拒 / 域拒 | 6 / 0 / 0 |
| QR driver 核计最大 RSS KiB | 597644 |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-secant/attempt-003。

| 输出 | SHA-256 |
|---|---|
| run.json | 7f8bfa03ec380ef87d0a2dcdfd10b9fac7ad24e94a515f2b8cf271cdb149ed88 |
| 完整 raw | 040f8f5f8f3c268a48f964e65fd8bada58451af3c6ad46d98d2e5c5a15c4b192 |
| physical.npz | dcc4457e7594a740745b7daefbdac3c33652bd93d943afbe7f2b6a5659758044 |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda128-m24-actual.json)记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
