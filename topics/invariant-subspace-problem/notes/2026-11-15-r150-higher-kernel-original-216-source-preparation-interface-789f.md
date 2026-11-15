# 原 216 来源准备阶段：执行合同

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。

## 1. 新阶段的确切作用

本阶段实现[216 列与双映射数学接口](2026-11-15-r150-higher-kernel-216-column-and-two-mapper-interface-789f.md)的原来源准备部分。此时只冻结源码，尚未本地 AST 或数学执行；第一次真实解析和实际秩以 Actions 回执为准。

它恢复同一个原常单位来源集合 $P$（$4340$ 个）及补集 $H$（$1848$ 个），从原自然十七式构造全部 $1632$ 条反对称 Koszul 曲线在 $H$ 上的整数多项式坐标。随后实际计算

$$
\operatorname{rank}_{\mathbb F_{31}}\Phi_H(0)
$$

及一个 $1632$ 阶单位子式。如果实际得到满列秩，剩余 $216$ 个原坐标给出真实局部直和

$$
[\Phi_H(u),E_{216}]
\in \mathrm{GL}_{1848}\bigl(\mathbb Z_{(31)}[[u]]\bigr).
$$

这支付特征零也合法的来源缩减；没有把有限域消元数值升成有理数。后继可以直接取原 full Schur $S$ 的这 $216$ 列，而不求 $1632$ 阶级数逆。

本阶段不计算 $S E_{216}$、其 $202$ 列形式核、$O$ 的原始左核或 $D_{\rm high}$。回执相应标志始终为 false。

## 2. 冻结源与输入

代码路径：topics/invariant-subspace-problem/notes/2026-11-15-r150-higher-kernel-original-216-source-preparation-789f.py

- blob：cc39351a565aa38c9220dbf51fe5e8ea46fd3864
- 字节：18126
- SHA256：29c1fd1a5a79d6de469260ee408a9ae5778f709e089250688824d0eb79dbf8eb

五个输入完整身份：

| 参数 | 字节 | SHA256 |
|---|---:|---|
| primitive-equations | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| native-model | 128145 | 291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6 |
| paid-full-receipt | 72072 | d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e |
| paid-full-summary | 35730 | 2782f380fe5731fd4766fb05fa94a6fa38c36d2d5e491bd63dd1149adc3a9388 |
| generic-rank-proof | 9957 | b803d92f159bf26bc9b4a80bbaf5a150ff8f17e81e201b0a99e845b7777038e4 |

primitive 的当前临时文件沿用已经核验的字节。新恢复的两份历史字典同属提交
`8c6304e273e64b0544d3dd58bc0e48a672a87c36`：

- `topics/invariant-subspace-problem/notes/r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt`；
- `topics/invariant-subspace-problem/notes/2026-11-14-r150-infinity-first-jet-receipt-789f.json`。

这一步不恢复 forward/backward、旧 full operations、旧完整 Schur 层、旧有理 $29$ 来源或旧 p-adic 检查点。两份 paid 小文本与 Q13 入口相同，直接由 scripts 提供。

## 3. 身份链与新实际计算

先核原 primitive 的解压 SHA、全部 $4433$ 个原参数系数与 native 模型。由 prebasis 的 $3333$ 条原来源和旧 constantPivots 的 $1007$ 个原 witness，恢复完整来源、输出单位字典。它们必须逐一匹配已完成 full v2 回执中的三个完整字典 SHA；不能仅依赖数字 $4340$。

对每个 $i<j$、$f=1,m_0,\ldots,m_{10}$，构造

$$
f(F_j e_i-F_i e_j).
$$

每个非零系数都保原来源方程编号、真实乘子单项式、自然 $u$ 次数和完整整数。所有 $1632$ 列的原系数字典逐项检查，故反对称多项式身份证明它们是完整原自然来源核。本次另对 $136$ 个常项 base-pair 用原整数方程作实际乘法，核全部系数相消；其十一组一次倍由已核原坐标继承。

回执不会声称已经额外展开所有 $1632$ 列在每个自然阶数上的大矩阵乘法。它使用的完整自然身份准确命名为
`all1632NaturalSyzygiesProvedByVerifiedOriginalAntisymmetry`。

新有限域计算只用于**常数单位选择**：

1. 构造 $\Phi_H(0)\bmod31$ 的完整 $1848\times1632$ 矩阵。
2. 对其转置作 RREF，实际选出 $1632$ 个原 tail 行。
3. 对同一原方阵实际求 determinant，要求为非零模 $31$ 值。
4. 保存剩余 $216$ 个 tail 位置及其原 $6188$ 来源编号。

因为原多项式坐标本来为整数，这个非零模 $31$ 子式的常项在 $\mathbb Z_{(31)}$ 中可逆，故上述直和在 $\mathbb Z_{(31)}[[u]]$、$\mathbb Q[[u]]$ 与 $\mathbb F_{31}[[u]]$ 三处都合法。

完整原常秩 $4340$ 与泛秩 $4354$ 已付，因而后继 $27\times216$ Schur 泛秩为 $14$、形式核秩为 $202$。这两个数字是已证维数推论，不冒称本阶段已经算出该 Schur 的条目。

## 4. CLI 与回执

```text
--primitive-equations {work}/inputs/repo/original-primitive-integer-equations.json.gz
--native-model {work}/inputs/repo/native-normal-form-input.txt
--paid-full-receipt {work}/inputs/repo/infinity-first-jet-receipt.json
--paid-full-summary {scripts}/43731615668-full-infinity-original-dual27-v2-through21.json
--generic-rank-proof {scripts}/2026-11-15-r150-full-infinity-generic-rank-proof-source-789f.md
--out {work}/higher-kernel-original-216-source-preparation
--seconds 60
--memory-mib 512
```


无 native 编译，使用现有 python-flint 0.9.0。建议 outer timeout 为 $85$ 秒。RREF 是原生调用；若未返回则不能声称已保存其结果。每个完整阶段写入后原子保存清单，续接必须核源码/输入绑定及实际文件 SHA，不能只看文件存在。

主小回执：

`higher-kernel-original-216-source-receipt.json`

成功时为：

- `status=completed`；
- `outcome=complete-original-high216-source-direct-sum`；
- `actualKoszulTailConstantRank=1632`；
- `actualConstantUnitDeterminantModulo31` 为实际非零值；
- `highComplementSourceColumns=216`；
- `characteristicZeroSourceDirectSumProved=true`；
- `sourceDirectSumOverZ31PowerSeriesProved=true`；
- `all1632ExactOriginalCurveCoordinatesRetained=true`。

程序同时保留
`highSchurActuallyComputed=false`、
`allHigherKernelMapsComputed=false`、
`characteristicZeroHighSmithComputed=false`、
`characteristicZeroFullSmithComputed=false`、
`selectedLeadingCoefficientUnitProved=false`。

## 5. 后继读取的临时对象

- `complete-original-koszul-tail-polynomial-coordinates.json.gz`：完整 $\Phi_H(u)$ 原整数稀疏坐标、原 $H$、全部 family 顺序以及自然阶数。
- `complete-original-high216-source-profile.json`：同一原 $P,R_0,H$，实际 $1632$ 单位行、实际 determinant、$216$ 个剩余坐标，以及完整 RREF 字节哈希。
- `complete-stage-manifest.json`：两个已完成对象的字节、SHA 与 portable 数学绑定。

全部只在作业临时目录保留。永久输出仅本源、参数、实际小回执与 SHA。得到这份 profile 后，下一步仍必须在对应域中实际构造完整 Schur、两个原始映射及全部原乘回，不能预填特征零高核长度 $26$。
