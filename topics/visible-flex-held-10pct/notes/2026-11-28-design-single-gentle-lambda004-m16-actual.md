# R87 新剖面 λ=0.004 / M=16：原完整有限门接受

2026-11-28，/root/design_continuation。实际原 BVP 已通过原 RMS、物理 BC、metric 和完整文件门；这是同一个新单级温和剖面的数值设计场。原 source/input、raw/physical SHA、全部数组形状、参数尺度及实际 mean 下限都经未修改的 accepted_original 校验。

| 量 | 实际值 |
|---|---:|
| 模态 / 求解角格 | 16 / 512 |
| 节点 | 581 |
| 原 RMS | 9.989113785481928e-07 |
| 原 metric L1 | 1.0382373259402284e-07 |
| 原 physical BC | 2.3658467985337005e-19 |
| 原 audit mean | 784 |
| 实际 δ | 0.068095817552539697 |
| 原 BVP 加 audit 秒 | 76.581758139000158 |
| 完整 QR 次数 | 2 |
| 原 Newton 接受步 / merit拒 / 域拒 | 4 / 0 / 0 |
| QR driver 全程核计最大RSS KiB | 312236 |

q=warp=.012，原门仍为 RMS≤1e−6、metric≤1e−6、physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000。没有因本次通过而减少状态、支撑列、δ列、域检查或真实角度 mean。δ 仍在新 R87 扩盒 [.063,.069]。

本次工作目录：/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-low-modes/attempt-002。

| 输出 | SHA-256 |
|---|---|
| run.json | e80248658e0f746a0651a0e007250a041c2b8b7567c70742d972225e227030ec |
| 完整 raw | a1e19e85aa3dc8be993b6e009afe5ca76607961f908ed43952c58d9e3662e020 |
| physical.npz | e58f4b17610ee90e116b1d0e0b073b738a87fa5362768a099adef50dbfd01213 |

[同名实际 JSON](2026-11-28-design-single-gentle-lambda004-m16-actual.json)含实际命令单行来源、原 source/input、所有门和完整QR小摘要。未把仍在增长的外层日志冒称冻结；数组未入 Git。

本次是有限线性-port 数值场。λ=1 准确圆弧、实际非线性 DN、同一最终 g 的精化、连续全域几何、闭合与 README 完成标准尚未由本条支付。原控制器从真实接受场继续后继λ，不等待阶段报告。
