# actual63：最大 collocation 行的已保存模型响应

类型：数值证据（实际公开 Actions 原件读数）；不包含新科学计算。

作者：exact_refinement（GPT-6 Astra）；日期：2026-11-14 UTC。

## 1. 实际来源与读取范围

本记录只读取 [request63 / run43646179305](https://github.com/Rogerhu12/math-research-public/actions/runs/43646179305) 已完成产物。源码提交为 `db6d728f30ee2d0c9ea62c96c622d8d85d2354b2`。实际 artifact14134662698 为 `visible-followup-condensedqp-43646179305-1`，ZIP494657224B，SHA256 为 `c90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653`。

伴随 [原字节读数与完整描述器](actual63-row155819-readback.json) 记录三个 NPZ 容器的原 bytes/SHA、数组描述器、NPY header、原 row155819 的 binary64 字节及原报告出处。这里仅解码已经保存的单个数组元素；没有本地相减、范数、比率、矩阵作用、求解或有理数重算。完整 artifact 的既有字节审计范围与本短读数分开。

原固定模型为 $A=W_rJS^{-1}$、$b=W_rR$、$g=A^Tb$、阻尼 $\lambda=270$。row155819 的原标签为 physical collocation、interval461、radial mode1。该行始终属于完整模型；本次没有改动行、权重或约束。

## 2. 三个已经保存的行值

| 原保存对象 | row155819 原值 | 原 float64 little-endian 字节 |
|---|---:|---|
| `original_b` | `-1.4151317154400291` | `8e8e552761a4f6bf` |
| `recovered_full_model_evidence.action` | `0.00025747182097217506` | `0dcbfb0ca9df303f` |
| `final_selected_evidence.action` | `0.0002574718209640469` | `5b81f90ca9df303f` |

第二项是原 local QP 候选经完整 $H=A^TA+\lambda^2I$ 条件恢复后的实际 $Az$；第三项是随后原全向量可行性修复和同模型选择后的实际 $Az$。二者都直接来自原 `condensed-QP-result.json.gz` 所指的数组，没有使用原方向重新乘 $A$。

原选择报告同时记录：local radial repair factor 为 `1.0`，恢复候选的 global feasibility repair factor 为 `0.9999999999684314`，可行段选择参数为 `1.0`，最后 composed repair factor 为 `1.0`。最终选中 `R270-condensed-complete-H`。这些也是原报告的既有数值。

**可直接确定的范围：该行的小模型响应在完整条件恢复后已经存在；后面的 global selector 不是这一行大幅削弱响应的环节。** 这是对原已保存读数和选择记录的解释，不是把条件恢复宣称为精确约束最优解，也没有推断唯一的阻尼原因。

## 3. 尚未由原件回答的问题

原件保存了5749维 `local-center`、完整 local root/affine/gradient、条件恢复的完整方向/RHS/原 $H$ 残差，以及上述恢复和最终选择的完整 $A$ 作用。它没有导出完整236036维未约束中心 $-H^{-1}g$ 或它的完整 $A$ 作用。完整 chain QR 的四块仅有 shape/bytes/SHA 描述器，其 `file` 均为 `null`，不能冒充已经导出的因子。

因此，此次读数仍不能区分：完整未约束阻尼响应在该行本来就小，还是局部不等式候选所需的条件修正抵消了中心响应。局部中心不能直接替代完整中心；原 global selector 的近单位缩放也不能补齐这条缺失信息。

下一独立诊断将只在本公开仓库 Actions 中，以实际63所用父62状态、完整原 $A/W_r/b/g$、$\lambda=270$ 和全部来源重建一次原完整 linearization/QR，并逐摘要回绑原 L/R/P/BY/BC/BP/inlet/S/weights 与因子身份。随后读取未约束中心、原已存局部恢复力的完整响应、恢复算术余项和原 selector/alpha 的逐行贡献；不重新优化，不改原不等式或原科学验收。

本记录不声称完整 BVP、native tail、连续几何或课题完成。
