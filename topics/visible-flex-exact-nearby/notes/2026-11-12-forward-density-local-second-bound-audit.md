# 前向流水线的局部二阶费用与跨段累积：独立函数审查

2026-11-12，reproduce_newton。只审 scripts/fourfold_forward_density_pipeline.py 的 coefficient_norms、first_integral_and_local_second_bound、add_ordered_segment 三个函数；没有给仍在开发的 run_leaf/main 或整个流水线授予通过。

按上述顺序对三个完整 AST source segment 以两个换行连接、末尾补一个换行，所得1890字节的 SHA256 为4714d36775df8239d0f7542d145b1d91d6a6255fd235a58a2448c1bfde3d145e。阅读时整源 SHA 为14945657d1e4da97ab500856187378db31530aacd7a87e71e6cc86edae500a6c；整源后续增加入口不改变本审查范围，三函数若有改动则需另核。

## 准确的偶奇分解

设 ĝ(u,x)=Σᵢgᵢ(x)uⁱ，G=∫₋₁¹ĝ，J=∫₋₁¹ĝ_x(u)∫₋₁ᵘĝ(v)dv du。记 I_j=∫₋₁¹uʲdu，则 gᵢ′gⱼ 在 J 中的准确系数为

$$
B_{ij}=\frac{I_{i+j+1}-(-1)^{j+1}I_i}{j+1}.
$$

偶/偶的贡献恰为 G′G/2，奇/奇准确为零。其余两种顺序组合成

$$
J=\frac12G'G+
\sum_{\substack{e\ge0\ {\rm even}\\o\ge1\ {\rm odd}}}
\frac{2}{(e+o+2)(e+1)}
\left(g_o'g_e-g_e'g_o\right).
$$

因此在非负宽度 σ 的 Wiener 代数内，源码计算的

$$
\frac12\|G'\|_{A_\sigma}\|G\|_{A_\sigma}
+\sum_{e,o}\frac{2
\left(\|g_o'\|_{A_\sigma}\|g_e\|_{A_\sigma}
+\|g_e'\|_{A_\sigma}\|g_o\|_{A_\sigma}\right)}
{(e+o+2)(e+1)}
$$

是完整局部 J 的合法上界。它保留了偶次时间系数在准确 G 中的抵消，而不是直接用 A²/R 替代全部有限结构。σ≥0 是这里使用 Wiener 乘法代数的合同。若局部 J 不显式计算，这个完整界必须作为实际省略费用累加，不能因 J 小而设为零。

## 完整跨段乘积

add_ordered_segment 正确实现 C₂,new=C₂+G′C₁,old，然后才更新 C₁,new=C₁+G。负频率由准确实性共轭恢复，导数乘规范标签频率 ik。完整 Laurent 乘积的中心索引为 oldK+newK，所有非负频率0,…,oldK+newK均被加入；原 C₂ 的更高频率仍保留在2max(oldK,newK)的输出中。

所以该函数没有删掉最高乘积模，没有把新 C₁ 错放进本段交叉项，也没有将每段初值积分清零。零模取实部使用的是真实有限积的实性；所有 Arb 算术半径仍在球中。

结论：三个函数的显示公式与 R72 一致，未见实质缺口。本次为解析推导和源码核查，不是整个前向流水线的数值验收；真实密度误差、局部省略费用、累积球的保存、准确接缝和最终复合仍须由完整入口逐项支付。

