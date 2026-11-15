# R150 附录：2751 原单位块的完整列内容与单一结构块

Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。2026-11-15。

## 范围和实际输入

本结论只对原七个未定来源方向的同一个整数单位系统 $UX=E$ 作精确坐标缩放和结构分析，不声称新的有理核，也不重新做已完成的1567次消元。前序见[精确低填充消元](R150-appendix-exact-low-fill1541-and-original-seven-core2751.md)。

输入是 run43679903558 临时文件 seven-exact-low-fill-core-and-backsubstitution.json.gz：80674893B，SHA256 54288bdab2af917695df1a9e2e681cafffaee435ef0fcc86d766f058324d94ba，binding 044ea5d75d28042c53c2db1896ec186173b6b320e598cc35208d761f48dbdad0。它保留2751行列、全部424921个非零整数项、七个右端、原输出/来源编号及1567步完整逆代图。原单位块的模65521非奇异证书不受这些可逆有理变换影响。

## 精确列内容及坐标还原

对每列取实际全部非零整数系数的正最大公约数
$$
h_j=\gcd_i |U_{ij}|,\qquad U_c=U\operatorname{diag}(h_j^{-1}).
$$
程序逐一检查全部424921项被对应 $h_j$ 整除；因此 $U_c$ 是整数矩阵，而且
$$
UX=E\quad\Longleftrightarrow\quad U_cZ=E,\qquad
Z=\operatorname{diag}(h_j)X.
$$
得到 $Z$ 后必须先还原 $X=\operatorname{diag}(h_j^{-1})Z$，再使用原1567步逆代图。直接把缩放坐标交给旧逆代图会改变原来源，故不允许。七个右端在这一步完全不变。

全部2751列中，2700列的内容大于1；内容的中位位数为118，最大2144。系数最大位数从3693降为3691；全部非零系数位数之和从537252566降为465478525。七个右端的最大位数仍为3677。故这一步虽减少总整数体积，却没有消除最大系数高度；不能据此承诺直接有理求解会完成。

## 结构图没有继续分裂

程序在同一非零支撑上验证完美匹配，再求匹配诱导的有向图强连通分量及块依赖次序。实际只有一个2751维强连通分量，全部块间依赖检查通过。列乘非零有理数保持支撑，故上述结论同时适用于缩放前后。

这只排除按当前精确非零支撑作无填充块三角分解得到更小子块，不排除进一步代数消元、换基或别的精确解法。

## 实际执行与复现身份

- 源码：[七方向列内容与SCC](../notes/2026-11-15-r150-seven-low-fill-column-content-scc-789f.py)，SHA256 8e0a275784d765b87f80af43432a63e30273693728f04a14574de58d6ce97b83。
- 同一临时 session run43679903558，step seven-low-fill-content-scc，execution source 2c62c8149d07d9519b3613087ab7f59f271e99fb；自选参数30秒/2048MiB，无新主元或求解。
- 数学实际2.8077270069989027秒，总墙钟2.9212525700004335秒，exit0。实际 python-flint 0.9.0、FLINT 3.6.0（release30600）。
- [小回执](../notes/r150-infinity-remote-session-789f/43679903558-seven-low-fill-content-scc.json)保原参数和全部身份。原完整回执1836B，SHA256 638be93d7406618b48766f64b6ffda7d8e8e7cbc705c151449153c43f9eb1e8e；本步 binding 63419ca6d607815ca50d4cf2ba0f6c74855339441e5da4289c1fca03fca7e8ed。
- 临时列内容文件109635B，SHA256 1b8ce16d22d6435ae3c61ec00a4b7cd2a583bc17c1b93231e0011b3a3d3fab2e；临时结构文件24656B，SHA256 14d2437c71752c91a3a62b7809ade432899cf9bad3e7fef7e6dceb31a9a6732b。

可重算大数据仍只留本 job 临时目录。当前真核仍29条、同选有理秩仍4318至4325；七方向的完整原整数残差尚未支付。接续应测矩阵自身的行内容及七个右端的真实分母费用，再选择能保存内部进度的精确求解。

