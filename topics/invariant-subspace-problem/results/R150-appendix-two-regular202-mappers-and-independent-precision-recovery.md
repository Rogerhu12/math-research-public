# R150：同一原高核商的两个 202 维正规映射及独立精度回收

作者：Astra-ISP-789f / normal_annihilator。AI 辅助，模型 GPT-6 Astra Pro。

## 1. 本次实际结论

本次在 $\mathbb F_{31}[[u]]$ 中完成两个正规形式核的规范 $21$ 阶截断：

$$
N_H(u)\in\operatorname{Mat}_{216\times202},\qquad
N_O(u)\in\operatorname{Mat}_{231\times202}.
$$

它们分别满足同一原矩阵的高源小系统和外来源小系统：
$$
S_HN_H=0,\qquad S_O^TN_O=0.
$$
两个映射均在实际原自由坐标上规范为 $I_{202}$，其余自由块的正次系数均为零。完整乘回保留了高源小系统的全部 27 行与外来源小系统的全部 29 行，未删除自由余行。

这一步付的是两个小形式核的具体系数与规范自由坐标；完整 6188 原来源运输、完整 1834 外来源左核运输，以及最后的 $202\times202$ 配对将由独立后继消费。它们尚未作为本次实际计算完成项报告。

## 2. 可重现实际记录

实际 Actions run 为 43740928483，step 为 higher-two-regular202-mappers-preparation，执行源为 c3c2932fc50a3b17bca8eaaa7f73fcdd6f11afa8。数学耗时 7.464637823999965 秒，墙钟 7.529191257999855 秒，退出码为 0。实际 Python-flint 版本为 0.9.0。

原小回执为：

[43740928483-higher-two-regular202-mappers-preparation.json](../notes/r150-source-kernel-session-789f/43740928483-higher-two-regular202-mappers-preparation.json)。

原临时完整回执为 11358 字节，SHA-256：
7a65b17569fb81463a06d4318d9088ee94b6635bed4156ce6008558937dcfac6。

数学输入绑定：
7d781d083a66e7cb2b66426ea47753b7a50e7de5e10426642eb4246de6c46cca。

生成器：

[2026-11-15-r150-higher-two-regular202-mappers-preparation-789f.py](../notes/2026-11-15-r150-higher-two-regular202-mappers-preparation-789f.py)。

该源码 22703 字节，SHA-256：
a2e8fa4aa6d26c74b2f8000fb33fcda4b558021ab674582eecbd2c86edb9847e。

源模块的直和基础是：

[原 Koszul 来源直和及 216 列约化](R150-appendix-original-koszul-source-direct-sum-and-216-column-reduction.md)。

此处 216 个原补来源、原 1848 尾字典、4340 个原单位来源及其输出字典均与已付结果逐项一致。新程序未重算先前的大消元。

## 3. 高源映射

由同一原 4340 常单位消元得到
$$
A=
\begin{pmatrix}
U&V\\W&Z
\end{pmatrix},
\qquad
S=Z-WU^{-1}V.
$$
原 $1848\times1632$ Koszul 尾矩阵与补列 $E_{216}$ 组成局部单位换基。因此
$$
S_H=SE_{216}
$$
为 $27\times216$ 系列，泛秩为 14，其完整形式核秩为 202。

父任务已保存原自然矩阵到 $u^{32}$，原小 Smith 正指数为
$$
1^4,\ 3,\ 4^3,\ 5,\ 6,\ 7,\ 8,\ 10,\ 11.
$$
本次每层实际选择常数单位行列、保存其单位逆，并对完整 Schur 残块先核常数项为零，再除 $u$。14 个正方向全部退出后，剩余 202 列由实际回代送回原 216 坐标。没有使用一个未经验证的固定 14 阶小子式来推断逆极点。

最大累计除 $u$ 次数为 11。由各层完整单位回代，原 $32$ 阶输入给出 $N_H$ 的 $0,\ldots,21$ 项。对这些实际系数共核验
$$
22\cdot27\cdot202=119988
$$
个小系统产品，全部为零；202 个原自由坐标在第零阶为单位阵、其余 21 阶全零。

## 4. 外来源左映射

同一所选来源补集 $J^c$ 有 1834 个原坐标。原 Koszul 曲线的外投影
$$
O=\Pi_{J^c}\Phi
$$
有 1632 列，泛秩为 1632。原常数单位秩为 1603。消该实际单位块后，余矩阵 $S_O$ 为 $231\times29$，其转置的完整形式核秩为 202。

父任务保留原自然系数至 $u^{35}$，完整正谱为
$$
1^2,\ 2^{10},\ 3^3,\ 4^3,\ 5,\ 6,\ 8^2,\ 9,\ 10^2,\ 11,\ 12,\ 13,\ 14.
$$
本次对 $S_O^T$ 作相同的实际单位 Schur、整块除 $u$ 与原坐标回代。29 个正方向全部退出，最大累计损失为 14，故得到 $N_O$ 的 $0,\ldots,21$ 项。

对全部
$$
22\cdot29\cdot202=128876
$$
个外来源小系统产品逐项核验为零。它的 202 个自由坐标在实际 231 尾字典上同样规范为单位阵。

## 5. 为什么两项精度损失不相加

两个映射使用独立输入：$N_H$ 来自 full32，$N_O$ 来自 O35。实际回代分别付清 11 和 14 的损失，因此两者各自保留 $21$ 阶。

随后两个原常单位回填分别只使用 $U^{-1}$ 与外单位块的转置逆。这些逆在 $u=0$ 已是单位，不再引入负 $u$ 次数。因此后继完整原坐标映射各自仍保留 $0,\ldots,21$。

若记完成原坐标运输后的映射为 $K_H$ 与 $\Lambda_O$，则
$$
D_d=\sum_{i=0}^d\Lambda_{O,i}^T
(K_{H,d-i}|_{J^c}),\qquad 0\le d\le21,
$$
只读两映射各自已经保留的系数。不存在把损失写成 $11+14$ 的串联步骤。

## 6. 实际临时对象与后继范围

| 临时对象 | 字节 | SHA-256 |
|---|---:|---|
| complete-high216-kernel202-series.bin | 959992 | 8bda14424b2f95cf9a88490f70bba11fab1b3da736fc623912354636ec4e2301 |
| complete-outside231-left202-series.bin | 1026652 | 1ff1a899f7a9bf0ababa2a0bb15cf2132e3757a0a00ab717154f4488aee79c02 |
| high202-native-heads.bin | 960896 | a27ccfcf95192fde8b2c0caff8bd515da30e2bed28f97f1e71a7b655dc074b3d |
| outside202-native-heads.bin | 1033998 | 0dcdcbf1edb733f92eef1568c3734342eb427b8c8d8eacc6446f08f882878ca1 |
| prepared-two-original-mapper-transports.json | 34344 | 5a1892f8787b85b788b9e940d11e4ebe597485097df9513e56f2be688dd98555 |

所有数组仅在本 job 临时保存。已提交源码、参数和实际散列足以重建；大数组不进入 Git 或 Release。

本次实际完成字段为 all119988OriginalHighSmallProductsVerified、all128876OriginalOutsideSmallProductsVerified、all202HighFreeCoordinatesVerified、all202OutsideFreeCoordinatesVerified 和 independentPrecisionLossesVerified，均为 true。

original202SourceTransportComplete、original202OutsideLeftTransportComplete、higherQuotientActuallyComputed、characteristicZeroHighSmithComputed 和 selectedLeadingCoefficientUnitProved 在本次回执均为 false。下一原坐标运输和配对的成功结论必须引用其自己的实际完整回执。
