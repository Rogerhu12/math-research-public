# 唯一模态衰减初猜的实际有限结果

2026-11-17，constructive_model；独立 residual-only 读者为 geometry_amplification。按冻结计划只生成一次、只评价一次新初值，没有参数扫描、Jv/伴随重测或非线性迭代。

保持同一准确 Hold g、923节点、1845个真实节点/五次中点、M160、同R/S/H/core与解析圆 lift。原819个 prefix 节点三jet逐字保留，尾部改为计划给出的固定 $\zeta e^{-\lambda_jt}$ 三jet衰减。所有模态（含均值）的 rates 一次固定，范围为 `.8546129472389244..273.47614311645583`；使用同一 a(1) carrier `1.1701203489027292`。该模式是新的初猜设计，不是线性化尾方程的已证稳定子空间。

生成实际耗时2.134724715秒。切口解析公式与被保留 literal 三jet的最大普通浮点差为 `3.3882e-21/1.3878e-17/4.4409e-16`，末端公式本身三jet字面0。结构检查确认准确 core 条件、固定前三参数及 terminal q 三jet全零；物理 lift 依旧全解析。

独立读者使用已核对的 FFT 角值算子，在2048角、全部1845个节点/真实中点评价一次，所得实际点值为：

| 项目 | 数值 |
|---|---:|
| 全部点的归一 Gram 算子范数最大值 | 0.6551089574780629 |
| 节点最大值 | 0.654891689915142 |
| ss / sφ / φφ 分量绝对最大值 | .655109 / .282959 / .301317 |
| 点值归一 Gram determinant 最小值 | .6626282663808325 |
| 紧 lift 区最大 Gram | .010309783303406594 |
| 保留 prefix 最大 Gram | 3.612387315167883e-5 |

全峰在实际五次中点 $s=1.3480413751845672,\phi=0$。与旧长五次桥约147.406的最大 Gram 相比，此次温启动明显降低了残差；**.655仍远超目标，未接受**。原 prefix 的最大值已在真实节点 $s=1$，因此若仅修改尾或仅换共同二导，不可能消掉这个保留节点下界。新 fullclosed 空间本来允许全部 interior prefix 未知量变化，未在本条锁死它们。

这次只检查了3,778,560个实际 stage/角点，没有连续域认证；点值 determinant 正不代表完整浸入。R648/R651/R652的旧开放场证书没有转给该候选。独立读出只用一次 residual，耗时1.702868325秒，总2.87217636秒，没有任何 Jv、Jᵀ 或 CS 调用。

## 完整身份

- 固定生成计划 `parallel-model-fullclosed-mode-damped-plan.md`：SHA256 `9343c6fa2dc57b609b44e7579c0c04c6ede5651e438d27fddd8ccb9f981f2ff0`；内含完整CLI。
- 生成源 `parallel-model-fullclosed-mode-damped-warm.py`：`632d6cfc5f3113bc6f64c340fe9d066a1614c5b0bd649a357bdea2d0d94af6e8`。
- 新 bundle `parallel-model-fullclosed-mode-damped-warm.npz`：`9bf60ea31f40239cb657a01a93242e32a024f448d1ebffaf22515de52c022cbd`。
- 生成报告 `parallel-model-fullclosed-mode-damped-warm.json`：`17697da3d5994f52c21ee481576c78fa67b7cc33152a78e1ee1202a4ea02ad19`。
- 独立读者源：`48624cf05c616a513da68d7db755fea00dfb8ac068b594d42fc300e3f082fd35`；它消费的同FFT源为 `7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211`。
- 独立报告 `parallel-geometry-fullclosed-mode-damped-residual.json`：`b361a25451390db061e489de1df6aef39725928e7390ffe346819c063f3b692e`。
- 同一次完整残差数组 `parallel-geometry-fullclosed-mode-damped-residual.npy`：`f0c3a300dcb5f20ac8d4995a657b39869aa0adb3eb0c5085dd87f76e086454c1`。

以上原始数据均留仓库外。此次由固定生成定义得到一个实际较温和初猜；后续任何求解预算或新参数选择另行明确，不从本条预报成功。
