# R96. 原全级权三提升的尖锐留数格及非零 Hecke 交换子

## 结论

在原全 \(68\) 级模曲线上，令
\[
S_p=\left[K^p/(sJ^{p+2})\right]_{\le p-3},\qquad
\nu_p=S_p(t)t^{-p-2}\,\mathfrak f_e\,dt.
\]
这里 \(\mathfrak f_e=M_e\omega\) 是原权一全局截面，
没有另取一个 Taylor 多项式代替它。
\(\nu_p\) 是真正全局的权三亚纯尖形式；全部内点极点位于
\(\mathcal C=\lambda^{-1}(1/2)\)。

对各 CM 标记 \(x\)，其留数准确为
\[
A_{x,p}=[t^{p+1}]M_xS_pK,\qquad
B_{x,p}=[t^{p+1}]M_xS_pL.
\]
原标记的向量为 \((C_{p+1},0)\)。
其他标记满足
\[
A_{x,p}\in p^{-1}\mathcal O,\qquad
pA_{x,p}\equiv\kappa_pM_x(0)\pmod p,\qquad
B_{x,p}\in\mathcal O,
\quad\kappa_p=p[t^{p+1}]K\in\mathbb Z_p^\times.
\]

遗忘映射的次数为 \(D=19584\)，Hodge 线丛次数为 \(D/2=9792\)。
原截面在每个好位整，其特殊纤维因原分支 \(t^4\) 系数为一而非零。
故每个目标惰性 \(p\) 至少有 \(9792\) 个实际 CM 标记满足
\(M_x(0)\bmod p\ne0\)，从而 \(v_pA_{x,p}=-1\)。
整个留数向量准确需要一个 \(p\) 才整，且局部降极点/Čech
构造证明一个 \(p\) 也足够；这是真实形式的尖锐损失。

设 \(h_p=S_pt^{-p-2}\)，实际同源分支满足
\(t_j'=(s(t_j)/s(t))c_j^2/p\)。未归一的几何 Hecke 像是
\[
\mathscr T_p\nu_p
=\sum_jc_jM_e^{\rm tr}(t_j)h_p(t_j)t_j'\,\omega\,dt
=\sum_jc_jM_e^{\rm tr}(t_j)
 (h_p(t_j)t_j'-h_p(t))\,\omega\,dt.
\]
全部标签运输仍保留。这一像确实非零：
取一个 \(M_x(0)\ne0\) 的最大 CM 阶标记，其 degree-\(p\)
邻点只有一条上升同源回到极点纤维，另外 \(p\) 条到导子 \(p^2\)；
唯一极点支不能被正则支消去。

更强地，这个缺陷在 de Rham 上同调中也非零。
任意有限 CM pole support 上的类 \(c\)，只要有一个 CM 留数非零，
就不能在扩大开曲线后满足 \(T_\ell c=\lambda c\)
（任意奇素数 \(\ell\nmid68\)、任意标量 \(\lambda\)）。
证明选择某个 CM 域非零留数支撑中的最大 \(\ell\)-conductor 深度 \(r\)；
其下降邻点的深度为 \(r+1\)，只有一个 ascending 分支回到原点，
其余目标深度 \(r+2\) 的留数全零。
因此新点的 Hecke 留数是原非零留数的可逆同源拉回，
而 \(c\) 在该点的留数为零。
该局部格分类及层标签运输均在完整证明 §4.1 给出。
exact/Bol 修正、或所有 CM 留数均零的类，不能消去这一缺陷；
这里明确不排除纯 parabolic 类。

## 指定中央方向

整化后的全局类 \(p[\nu_p]\bmod p\) 因其他标记而非零，
但在原标记其留数已属于 \(p^2\mathcal O h_1\)。
原目标仍准确是
\[
p^{-1}\operatorname{Res}_{x_0}\nu_p
=(C_{p+1}/p)h_1.
\]
选择该留数直和分量不自动给保留 Hecke 的全局整提升。
这说明已知的其他分量非零，不能直接用于原中央非零。

## 证明与来源

[完整证明](../notes/2026-11-12-actual-level-cm-residue-lattice-and-hecke-defect.md)
含所有尖点的整性、特殊纤维零数、准确留数、
整对数复形的一层成本，以及真实上升同源的极点和上同调留数证明。
根端全文独审通过；Kodaira–Spencer 的原始出版公式也已核对。
本结果仍未证明无穷多个 \(p\) 的中央导数非零。
