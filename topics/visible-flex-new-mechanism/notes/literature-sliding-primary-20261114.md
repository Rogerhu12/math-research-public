# 滑动相位路线：Sabitov 原文的准确输入

**状态：原始文献核验；没有从这些文献取得满足本题的闭曲面。** 本记录补充 `literature-20261114.md`，特别区分有边带的材料相位、闭曲面的内在圆群作用，以及尚需构造的非旋转实现。

## 1. 2021 年论文给出的是什么

I. Kh. Sabitov, *Bendable Surfaces without Visible Deformations of Their Shape*, Mat. Zametki 110:1 (2021), 119–130；英文版 Math. Notes 110:1, 126–134。

- [期刊页](https://www.mathnet.ru/eng/mzm13037)
- [实际核查的俄文全文](https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=eng&paperid=13037&what=fullt)

印刷页 126 的 Theorem 1 处理沿闭平面母线的圆柱面滑动，页 130 的 Theorem 2 处理等长母线的锥面；非圆情形的材料相位不是刚体运动。页 122–123 还通过刚体归一化固定母线的一小段来显示材料位移。

闭合问题没有被略去：页 130 的最后备注明确解释，给滑动锥面加球面区域，虽然边界像及所围体积不变，却不能因此得到闭等距弯曲，因为边界材料点在球帽内的距离改变。本文的圆领方案须另外证明完整边界参数、位置和二阶 jet 相容，不能只匹配边界像。

## 2. 2023 年论文对闭相位路线的条件结论

I. Kh. Sabitov, *Infinitesimal Sliding Bendings of Compact Surfaces and Euler’s Conjecture*, Sibirsk. Mat. Zh. 64:5 (2023), 1065–1082；英文版 Siberian Math. J. 64:5, 1213–1228。

- [期刊页](https://www.mathnet.ru/eng/smj7815)
- [实际核查的俄文全文](https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&option_lang=eng&paperid=7815&what=fullt)

印刷页 1066 列出四个定理。Theorem 1 给具有全局旋转度量的闭 $C^2$ 曲面一个切向无穷小弯曲；Theorem 2 区分球面情形该场何时是刚体场。Theorem 3 是条件命题：若球面上的旋转度量已有非旋转的 $C^2$ 浸入，则存在非平凡一阶、二阶滑动无穷小弯曲。Theorem 4 是局部版本。

这不是非旋转闭浸入的存在定理。印刷页 1081 的讨论仍把寻找这种实现列为待研究方向；其相反方向也是待研究问题。文中没有宏观位移、握持区或 reach 的定量结果。

## 3. 对本题实际构造的用法

下面是本课题的条件推论，不作为上述论文已经完成的结果：若已得到一个非旋转的闭嵌入 $F$，其固定度量有全局相位作用 $\rho_t$，且某开圆领/圆帽上满足
$$F(\rho_t p)=R_t F(p),$$
则
$$F_t(p)=R_t^{-1}F(\rho_t p)$$
有同一拉回度量，并在该开区逐点固定。其像是 $R_t^{-1}F(M)$，因此所有时刻的嵌入性和 reach 归结为初始像；材料位移仍须直接计算。该条件推论不补出所需非圆核心与圆领的精确等距过渡。

因此当前计算必须保留两个独立门槛：先完成同一固定度量下、完整边界二阶数据相容的半带/闭面，再验证握持直径、归一化位移和全局 reach。单独的滑动圆柱、非圆锥、局部旋转度量或二阶无穷小场均未达到这两个门槛。
