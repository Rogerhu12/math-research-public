# 固定背景高度 helper 与 alpha 高度转移的独立审查

审查者：`/root/independent_geometry`。状态：**限定作用域内 PASS**，实际网格半径输入已运行；未认证完整数值顶点误差，未支付 G5。

## 1. 冻结对象与实际运行

全文审查的数值 helper 是
`scripts/db6f-tail-sample-background-height.mjs`，SHA256
`106061533820a1639387b33b535408d312ade7a8337d59ed8c2b48ec80bc08a4`。
审查不依赖其作者的自审。实际运行使用已认证 M8 有限图的 76 个网格半径，包含保存的精确 binary cuff 与 cut，输出
`notes/2026-11-09-db6f-visible-m8-heights.json`，SHA256
`475006a9aa34cd590dbde257e873a901525c55656fa3deb1f3efccc17f0675f5`。
命令实际退出码为 0，耗时约 2.81 秒。

输入绑定另由 `scripts/db6f-audit-height-inputs.py` 重读检查，报告为
`notes/2026-11-09-db6f-audit-height-inputs.json`。本次实际 manifest 与紧 alpha 所绑定 checkpoint 的**全部 56 个参数键和值相同**，并非仅接受 helper 的物理键子集。四个背景源文件、manifest、有限校准表、紧 alpha、半径表与 helper 的 SHA 均重新验证。helper 实际重建并逐一比较了 160 个有限源校准二进系数，且固定 `calibrationSteps=512`、`protectCell=160`、正方向。

## 2. 数值方法的静态审查

`entry.integrate` 的槽 0、1 是径向密度的两部分，槽 4、5 是相同密度乘以源斜率的两部分。因此在同一源段上，径向距离为槽 0 加 alpha 乘槽 1，高度增量为槽 4 加 alpha 乘槽 5。weighted wrapper 已把权重乘入相应 B 槽，helper 没有再次乘权重或漏乘。

遍历顺序是从 cut 向内，cell 递增、cell 内 segment 递减，径向与高度均用 Kahan 累加。对内部物理半径，反解使用从候选源坐标至该段外端的径向积分；这个函数随源坐标递减，44 次二分的分支方向正确。高度以 cut 为共同零点，避免借用有限深尾的任意绝对高度 gauge。

上尾完整坐标应使用

$$
z=H_c+\int_r^c w(s)\,ds-V_z(r,\theta),
$$

下尾反射这个**完整 z 坐标**。helper 的 gauge 字段与此相同。cuff 使用有限源累计高度；精确无限深部遗漏由原 R15 的源斜率界给出单独贡献

$$
640\,2^{-280}.
$$

这不是对有限求积、反解、alpha 代表值与二进舍入总误差的界。

本次 76 个查询的最大数值径向残差为
`4.812122922359663e-15`，同一高度积分拆分前后最大差为
`1.734723475976807e-17`。这些量是诊断值。helper 明确输出
`heightIntervalCertificate=false`，审查没有将诊断值解释成严格误差条。

## 3. alpha 代表值的单独严格贡献

独审短稿
`notes/2026-11-09-db6f-tail-height-alpha-transfer.md`，SHA256
`5bb6b9b576d8baf11c53469fdc66c662faa36de47a94ca246e70ef706fda3700`，以及
`scripts/db6f-tail-height-alpha-transfer.py`，SHA256
`e7ef728b71297917a8fce2c4dff299b7f0661ca045f7aa656e775df0c94b66ef`。

令源密度为 $q_\alpha=a+\alpha b>0$，其中 $a,b\ge0$，且 $0\le w\le W$。
取 $\alpha_2\ge\alpha_1$，同一物理半径所对应的源坐标满足 $x_2\ge x_1$，径向守恒给出

$$
\int_{x_1}^{x_2}q_{\alpha_1}
=(\alpha_2-\alpha_1)\int_{x_2}^{\xi_1}b.
$$

高度差是两个非负量之差，而两者均不超过
$W(\alpha_2-\alpha_1)\int b$，故系数为 1 的界正确，不需要乘 2。
稿中另分别覆盖仅较短径向像已进入 cuff 常值延拓，以及两幅图均已进入常值延拓的情况。可积无限源由非负积分极限通过；没有以有限层数替换原背景。

在已审紧 alpha 输出端点上进行纯 Fraction 组合，独立命令

```bash
python scripts/db6f-tail-height-alpha-transfer.py \
  --out notes/2026-11-09-db6f-audit-height-alpha-transfer-replay.json
```

实际退出码为 0，重放 JSON 与作者原 JSON **逐字节相同**，SHA256 都是
`411af35301c3dd91f44f098a523687284c6f63a37a1aa9e8c11a5ab329245e2f`。
另用独立输入核查脚本重新组合有理上界，得到 alpha 代表值单独造成的精确源高度差

$$
\sup_{r\le c}|\Delta H(r)|<4.56\cdot10^{-14}.
$$

其二进诊断显示值为 `4.5542191364571383e-14`。这里认证的是改变 alpha 的贡献；实际网格仍是已证明连续图的数值离散近似。

## 4. 复现实际输入核查

```bash
python scripts/db6f-audit-height-inputs.py \
  --samples notes/2026-11-09-db6f-visible-m8-heights.json \
  --alpha-replay notes/2026-11-09-db6f-audit-height-alpha-transfer-replay.json \
  --out notes/2026-11-09-db6f-audit-height-inputs.json
```

此命令也已实际退出 0。完整的网格闭合、方向及离散嵌入由单独 PLY 验证器检查；本稿不重复或扩大那些结论。
