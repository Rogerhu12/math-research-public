# M12 critical 第一档：完整尾部低误差度量证书

作者与区间后台维护：`/root/independent_geometry`。状态：**完整运行已退出 0，全行、物理分区与输入身份已复核**。这是已冻结有限曲面的连续区间证书；不是对无限非线性 ODE 的存在断言，也不单独支付 G5。

## 1. 同一张实际有限图

本证书使用
`notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`，SHA256
`cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。
它有 18553 个节点、18552 个有限多项式跨，并另含实际 R6 collar。
相应闭图是 `notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json`，SHA256
`253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`。

本次仅收紧目标背景 $w(r)$ 的包含包；实际有限曲面、物理网格、端点两 jet、傅里叶系数与背景定义都没有变化。因此已经完成的同图曲率证书继续有效。新的 metric-only 输出明确 `curvature_evaluated=false`，没有用 0 作为虚假曲率占位。

## 2. 完整供应包与后台

原 M8 背景包经已审整 span overlay 依次接入 raw2、raw3 的精包及必要 point-Lipschitz 修包、13 段 raw0 phase 精包，最后以 span 4407 的局部修包覆盖该完整 span。最终 M8 包是
`notes/2026-11-09-db6f-audit-tail-lowmetric-final-packet.json`，含 6211 盒。

由已独审的精确物理半径换网格方法转移到本 M12 网格，得到
`notes/2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json`，SHA256
`791e3bfda7bac4f356f34718a9731e5db7cfe5dd402525261e4b123914523d59`，
对应多项式数据 SHA256
`a9173083636377a323ff9438481fd8a90c84772f9791b78c8542b7e209301cc8`。
全部 30971 盒包含 cuff/collar 与所有有限跨。工作容差只是选择包紧度的条件，结论来自实际连续 residual 后台。

后台是 `scripts/db6f-audit-tail-metric-only.py`，SHA256
`178d7b7b62deeff93d8e198f271736ac41f258c07b3d8b7a9bc111c909d5ebd6`。
其公式复用已审系数相消与 Fourier/Bernstein 区间方法，first fields 与冻结完整后台的前两项逐式相同。root 已对 M8 全部 5237 行完成 metric-only 与旧完整后台的独立回归，全部数学字段相同；stream 存储适配器也已有全量原始多项式按位比较。相关审稿分别为 `db6f-root-review-metric-only.md` 与 `db6f-root-review-tail-stream.md`（均带日期前缀）。

## 3. 实际完整运行

```bash
python scripts/db6f-audit-tail-metric-only.py \
  --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --packet notes/2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json \
  --out notes/2026-11-09-db6f-audit-tail-m12-critical-lowmetric-full.json \
  --progress 1000
```

实际退出码为 0，完成 30971/30971 盒，耗时约 1630.41 秒，进程峰值 RSS 为 334442496 字节。完整报告 SHA256 为
`83cf92351c83ce3275af9ac2fd975ecf87dc81e74379e2f1ccb2436374147056`，
逐行报告数据 SHA256 为
`06706fee1a59c4f0ce15ebde39af24e323bd077cf1819020ab660c8221c41f7d`。

连续尾部度量算子误差上界为

$$
\varepsilon_{\mathrm{tail}}\le2.334386824020345\cdot10^{-8}.
$$

三项坐标残差的全域上界分别为
`2.30554741767066e-8`、`1.260596908058862e-10`、`2.557602307542118e-13`。
最坏算子行是 packet row 27397，finite span 17148。

这些上界覆盖每个物理径向区间与全部角度；没有以节点采样代替连续验证。

## 4. 全行完成性与身份复核

另行运行 `scripts/db6f-audit-complete-metric-report.py`，输出
`notes/2026-11-09-db6f-audit-tail-m12-critical-lowmetric-complete-check.json`。
程序实际退出 0，逐行检查报告与多项式包的 span/row 一致，使用 Fraction 验证从 collar 的 span -1 到 finite span 18551 的每一 span 均由从 0 至 1 的无缝有序正长度子区间覆盖，无遗漏或额外行。全局度量与三项坐标残差分别等于逐行最大值。

同时重读校验了所有后台文件 SHA、manifest、包、数据、行数据，以及六项非空背景定义哈希。新的 metric 包与旧曲率包绑定相同的 checkpoint、有限源校准表、紧 alpha、cell0 A、inner A 和 outer B。该后处理不冒称重新计算了 Fourier/Bernstein 残差；其作用是证明本次实际输出完整、与冻结方法及同一张图绑定。

## 5. 与完整闭图及旧曲率证书合成

旧完整同图证书
`notes/2026-11-09-db6f-audit-tail-m12-critical-tight-full.json`
已覆盖全部尾部与 collar，给实际主曲率绝对值上界
`8.462559071292288`。它的曲率行与背景包未因本次 metric 计算而改动。

独立命名运行

```bash
python scripts/db6f-root-whole-metric-reach-v2.py \
  --closed-budget notes/2026-11-09-db6f-audit-closed-budget-m12-critical-r01-replay.json \
  --tail-certificate notes/2026-11-09-db6f-audit-tail-m12-critical-tight-full.json \
  --tail-metric-certificate notes/2026-11-09-db6f-audit-tail-m12-critical-lowmetric-full.json \
  --out notes/2026-11-09-db6f-audit-whole-metric-reach-m12-critical-lowmetric.json
```

也实际退出 0。与 root 自己的合成报告比较，除两份独立、同 SHA 的闭预算文件名不同外，所有数学和哈希字段逐项相同；比较记录为
`notes/2026-11-09-db6f-audit-whole-lowmetric-replay-comparison.json`。
新全曲面度量上界由前缀决定：

$$
\varepsilon_{\mathrm{whole}}
\le2.572118832449239\cdot10^{-8}.
$$

固定帽的目标度量是其自身诱导度量；活动带由 R17 的旋转与材料作用将同一界传递至全部时刻。保持原真实曲率上界，R10 与原完整 support/直径界给出

$$
\frac{\operatorname{reach}}D
\ge\frac{1407374883553280}{46687172903089131}
>0.03014478701622472.
$$

所用直径上界仍为 $98/25$。held、可见位移和严格非全等依赖同图已审公共接缝闭预算，不从本次局部背景修包重新推断。README 的固定背景高精度收敛要求继续单列；这个新证书不能替代它。
