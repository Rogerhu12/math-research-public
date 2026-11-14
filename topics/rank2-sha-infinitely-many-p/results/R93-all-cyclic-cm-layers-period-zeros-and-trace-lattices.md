# R93. 全循环 CM 层穷尽周期零点，并给准确野迹格

## 结论

固定惰性 \(p\ge7\)，令 \(e_r=p^{r-1}(p+1)\)、
\(\delta_r=(p^r-1)/(p^{r-1}(p^2-1))\)。
原 CM 曲线全部循环 \(p^r\) 商的参数 \(t_H\) 满足
\[
v_p(t_H)=1/e_r,\qquad v_p(c_H)=\delta_r.
\]
它们互异，构成一个完全分歧的完整 Galois 轨道，次数 \(e_r\)；
目标局部 CM 阶为 \(\mathbb Z_p+p^r\mathbb Z_{p^2}\)，
Galois 群为 \(C_{p+1}\times C_{p^{r-1}}\)。

在同一实际晶体规范中，所有 \(K\) 的开单位盘零点恰为奇数层，
所有 \(J=L/t\) 的零点恰为正偶数层。它们都简单。
准确 Newton 顶点为
\[
K:\left(\frac{p^{2k}-1}{p-1},-k\right),\qquad
J:\left(\frac{p(p^{2k}-1)}{p-1},-k\right),\quad k\ge0.
\]
奇层 \(E'=M_e/(sK)\) 的留数非零；偶层
\(I'=M_eK/(sL^2)\) 同时有非零二阶极部和对数留数。
偶层留数不消失的局部单位准确为 \(1+4=5\)。

不同指数与完整迹理想为
\[
\Delta_r=r e_r-1-\sum_{s<r}e_s,\qquad
\operatorname{Tr}_{B_r/B}(\mathfrak m_{B_r}^j)
=p^{\lfloor(j+\Delta_r)/e_r\rfloor}\mathcal O_B.
\]
特别 \(\operatorname{Tr}\mathcal O_{B_r}=p^{r-1}\mathcal O_B\)。
\(k\) 阶 Hasse-jet 增厚的余核长度为
\(\binom{k}{2}\Delta_r\)；高层既非驯分歧，也不能免费反演 jets。

## 证明与审查

[完整证明](../notes/2026-11-12-all-cyclic-cm-layers-and-period-newton-polygons.md)
从真实 Serre 商的挠点估值独立推出目标 Newton 多边形，
再用估值分母证明轨道穷尽。Yu 的局部环类域与标准 period-map
纤维分类接到实际 \([K:L]\)，没有只比较映射的度数。
不同理想由全部角色的导子准确计数，迹理想直接由迹对偶证明。

根端撰写并完成计算；第二位研究者全文独审了高层穷尽性、
偶层留数和所有不同/迹/Hermite 公式。外部原文与定理位置见全文。

## 与主问题的关系

这些是实际全同源塔的几何和整格输入。
单支非零留数可以在完整迹中相消，仍须证明真实 theta/Hecke
关系对指定中央行或完整深度证书的跨素数非零约束。
没有从全层周期零点分类推出 \(\Sha[p^\infty]\) 无穷素数有限性。
