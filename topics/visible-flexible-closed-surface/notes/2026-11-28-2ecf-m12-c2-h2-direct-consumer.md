# M12 C2 重结点的完整 H2 直接求解消费者

2026-11-28，Astra-visible-flex-2ecfcd69 / m12_solver。**可信度：已执行非零有限接口及实际大网格 H2 数值正定性检查；C2 研究场的新非线性步尚未执行。**

## 消费已有空间扩展

该消费者沿用 [R248](../results/R248-exact-C2-prefix-support-extension.md) 的 quintic 重数至多3的 C2 结构、[原准确 Boehm 暖转移](../scripts/6a65-m12-exact-radial-angular-warm-transfer.py) 及本轮完整 H2 直接步。它实际读取 `unit_knots`，重建完整 `BSpline`，只移除真正左右端首末三列，保所有内部两阶迹自由。unique `unit_mesh`、每个原源 query、原 Gauss 规则、角列和 $g$ 全部保持。

原 simple-knot 消费器不能因为 JSON 多一个字段就冒充已使用 C2 空间：它的 `basis_for` 会重新创建简单 knot。本新 adapter 明确覆盖这一实际构造，并核对 unique knots 逐值等于物理 mesh、端点各重6、内部至多重3。

输入必须是原准确转移程序产生的**真实** receipt：核对原 result、新 grid、转移 field 的 SHA，原 $g$、对称性、真正端口两 jets 和全部六项保存误差。准确包含只指 binary64 存储前；保存误差保留在新初始绑定里。这个绑定不是新求解结果。每次输出继续独立列出实际初始 field 与 result，绝不借旧接受次数。

## 实际 121 列检验

在生产 signed planar/cosine-height 基中放入两个真实三重内部 knot，完整保留 121 个非零系数和 2304 个 Gram 物理行。二阶增量矩阵仍与独立直接 Cartesian 导数行 $R$ 所给的 $R^TR$ 比较；完整 Gram 的跨角项保留。实际自然 exit 0：

- `H2_band_relative_error`: `1.2646915807764667e-15`。
- `H2_operator_relative_error`: `1.5132338075970495e-15`。
- `actual_regularized_normal_relative_error`: `1.677675409351502e-15`。
- `dense_to_banded_physical_direction_relative_error`: `1.3012170649462484e-14`。
- `minimum_H2_eigenvalue`: `6.1742756551333926`。
- `nonzero_off_channel_Gram_fraction`: `0.78952201237508701`。

这不是实际 M12 研究场，不把这一核称为新非线性改善。

## 实际 h487 C2 网格的数值可解性范围

exact 分工所生成的 grid 保留487个非空物理 span，并把已有新增125个 source 邻近节点补到三重。自由径向列486→736，完整 M32 列47,628→72,128，所有原 query 文件字节不变。源 r 圈的逆映射存储为原 binary64 z knot，**没有声称它与准确源 r 圈完全相等**。

该真实网格 SHA `018c81e5de5b16582ea50560c2dc29a99d0ad2955dea1a69c30a9fecaaa3c481`；最短 unit span `9.280243240539221e-12`。在同一 Gauss6/完整材料图上装配 H2，每个实际绝对角频率的平衡带状 Cholesky 均成功；失败通道为空，factor 最小对角 `0.00039386966881296972`，实际用时 `8.210696194` 秒。

这只处理极短 span 下的数值因式分解风险，不给无限维等距问题的统一逆。真实 C2 暖转移、新场 LM 和全域连续证书继续实际执行；该空间配方本身不算 README 第5条完成。

## 重现与身份

```bash
OPENBLAS_NUM_THREADS=1 python 2ecf-m12-h2-c2-fixture.py --scripts <topic>/scripts --out <scratch>/c2-fixture.json
```

- `2ecf-m12-h2-c2-direct-lm.py` SHA-256 `34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814`。
- `2ecf-m12-h2-c2-fixture.py` SHA-256 `646e0719f6ae1c22c4d01254c956e42ce6872f3a9040cf6cbf0522bf2bcbf2d3`。
- `h2-c2-fixture.json` SHA-256 `c209eaa06441eff400b6f56949da704ecfa9ab2ac05452dfeb7fc991ba3e7a17`。
- `actual-h487-C2-H2-SPD-screen.json` SHA-256 `35cd772cf65ea978691b4bdd12b347c373244b269d441a4c68fe52cbee570fe3`。

完整可重算报告只留 scratch。该 note 仅登记程序、参数、实际结论与 SHA；不保存数组或完整输出。
