# R80 的真实常 cap 段 6 应用

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

本包是 [R80](../results/R80-capped-source-positive-moment-refinement.md) 的独立实际应用，不修改已冻结的段 1 证明、源码或 primary。原 cell 0 / 段 6 的 16 叶在保存的实际 source 中全部处于 cap 分支，$w$ 为原 binary64 参数 $0.02$ 所定义的常数，$\partial_x\log w=0$。实际计算仍调用完整 `OuterCell.profile/integrand`；没有把 capped 积分替换成 uncapped 深胞元公式。

## 定位与同候选身份

原五矩相对半宽约为 $5.4134\times10^{-5}$。然而 bubble 的高度补偿分子包含相消，原 $\lambda_2$ 区间约为 $[-2.02212\times10^{-5},2.02272\times10^{-5}]$。这只是包围宽度，不是证明真候选有大 bubble 或发生几何失败。

新 [application 入口](../computations/tail_outer_remaining_piece_moment_application.py) 只将冻结 R80 工具的显式分段范围扩展到原全段候选 $0,2,4,6$，并记录独立 source 身份。原分支判定、Taylor 余项、非负根条带、全部真积分交集、完整均值、真实导数、全频率 $J$ 和 R77 均未修改。这个入口明确拒绝不同的八子段候选及 physical-$r$ 段 8。

重放之前，原旧矩和旧 bubble 包围仍逐位重现；随后交新真积分包围，按同一物理端点公式计算相同的实数候选。没有选择任何积分中点或改动 $H/g$。

## 正式终态

| 项目 | 覆盖 | tool / wait4 | 时间 | 实测峰 RSS |
|---|---:|---|---:|---:|
| 同 cap 真矩 | 16 原叶、16 Taylor 片 | 0 / 0 | 0.3799 s | 29012 KiB |
| 原 R64、完整 J、R77 重放 | 16 原叶 | 0 / 0 | 1.0170 s | 30288 KiB |
| 完整九段有理数合成 | 7563 连续叶 | 0 / 0 | 0.2566 s | 12784 KiB |

真矩七门全部通过，无未决分支条带；新 $I_b$ 的显示外包围为

$$
[4.701320041317401302493737867370598328962950088306130970694994
 \times10^{-7}\ \pm 8.30\times10^{-68}].
$$

同候选的 $\lambda_2$ 收紧到 $[1.127114080\times10^{-14}\pm6.23\times10^{-24}]$ 的显示包围。全部正式 dyadic 端点保存在主包，显示小数不替代原端点。

完整有限 $J$ 给物理 Darboux 缺陷上界 $2.571524073\times10^{-6}$。其主要旧零模包围可再由真实完整均值约束 R77 支付，得到

$$
\sup_{\text{原段6}}|\mathcal D_{\mathrm{physical}}|
<1.175148\times10^{-9}.
$$

保留高度频带内非均值部分小于 $1.175092\times10^{-9}$，高度带外部分小于 $3.025\times10^{-18}$，R77 零模部分小于 $5.588\times10^{-14}$。全部 $0,2,\ldots,80$ 频率、完整 mean 及逆分母保持。最小整叶均值导数大于 $0.9997092$，$D>0.9999899$，$L>0.9997244$，Wiener 分母下界大于 $0.9990973$。

**证明范围。** R80 的同积分/同候选结论给出合法的新场包围；原 16 叶真覆盖和全部 R64/有限 $J$/R77 门已完整实算，因此以上界对同一原候选全段有效。它没有把候选换成 PDE 二阶 jet，也没有宣称真外解或 Green/Schur 逆已付。

完整九段仍为 7563 叶，最大段转为原 physical-$r$ 段 8，全胞元候选的物理 Darboux 缺陷上界小于 $0.026296746763$。下一步须读取段 8 自己的物理-$r$ 表示与真叶，不可把本段的 source-$x$ 正矩方法直接套到不同候选。

## 完整文件

- [精确三步计划](2026-11-12-tail-r80-seg6-actual-prepared-plan.json)含所有 argv、源/输入 SHA 与旧 primary 定位。
- [真矩 summary](2026-11-12-tail-r80-cell0-seg6-capped-moments-r1-summary.json)、[全部积分叶](2026-11-12-tail-r80-cell0-seg6-capped-moments-r1-integrals.jsonl.gz)、[正式资源](2026-11-12-tail-r80-cell0-seg6-capped-moments-r1-resource.json)。
- [完整 R64/J/R77 summary](2026-11-12-tail-r80-cell0-seg6-refined-moments-fullJ-r1.json)、[全部有符号原叶流](2026-11-12-tail-r80-cell0-seg6-refined-moments-fullJ-r1-segment6.jsonl.gz)、[正式资源](2026-11-12-tail-r80-cell0-seg6-refined-moments-fullJ-r1-resource.json)。
- [九段合成](2026-11-12-tail-outer-cell0-components-R80-seg6-r1.json)、[正式资源](2026-11-12-tail-outer-cell0-components-R80-seg6-r1-resource.json)。

原粗包继续保存。完成后的重复 recovery 不列入稳定清单。
