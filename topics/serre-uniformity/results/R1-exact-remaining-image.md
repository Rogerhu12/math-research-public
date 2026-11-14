# R1：剩余像、模曲线目标与基本线性代数

日期：2026-11-12。状态：**已证明的归约与标准群论**；不声称解决主要目标，也不声称这些事实原创。

## 1. 文献输入的精确版本

Furio–Lombardo, *Serre's uniformity question and proper subgroups of $C_{ns}^+(p)$*, arXiv:2305.17780v2（2025-11-25），Theorem 1.5：若 $E/\mathbb Q$ 无 CM，$p>37$，则 $\bar\rho_{E,p}$ 的像或为 $\mathrm{GL}_2(\mathbb F_p)$，或共轭于**完整**非分裂 Cartan 正规化子。该文已列在 *Algebra & Number Theory* 的 forthcoming papers 中。

- 原文：https://arxiv.org/html/2305.17780v2#S1.Thmtheorem1.5
- 期刊录用目录：https://msp.org/soon/coming.php?jpath=ant

这比“包含于正规化子”强。Theorem 1.6 同时排除了文中指定的指数 $3$ 子群 $G(p)$ 对一切 $p>5$ 出现。本文不再将排除 $G(p)$ 列作未解任务。

因此主要目标等价于：存在绝对 $C\geq37$，使所有 $p>C$ 的 $X_{\mathrm{ns}}^+(p)(\mathbb Q)$ 没有非 CM、非尖点的点。说明如下。若像包含于 $N_{\mathrm{ns}}$，选择一组 $p$-挠点基后得到 Galois 稳定的 $N_{\mathrm{ns}}$ 轨道，故得到该模曲线的有理点。反之，一个非特殊有理 $j$ 的有理点确定稳定的基轨道；先取定义在 $\mathbb Q$ 的具有此 $j$ 的椭圆曲线，再选代表基，则其 Galois 像保持该轨道。椭圆曲线的自同构只有 $\{\pm1\}$，而 $-I\in N_{\mathrm{ns}}$，所以这里的自同构歧义不改变包含关系。$j=0,1728$ 为 CM，已排除。

## 2. 矩阵模型与正规化子的证明

以下只需奇素数 $p$。取非平方元 $d\in\mathbb F_p^\times$，设
$$J=\begin{pmatrix}0&d\\1&0\end{pmatrix},\quad
s=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
C=\{aI+bJ:(a,b)\ne(0,0)\}.$$

利用 $J^2=dI$，将 $\mathbb F_p^2$ 识别为 $\mathbb F_{p^2}$，则 $C$ 是该域非零元素的乘法作用，阶为 $p^2-1$。又 $sJs^{-1}=-J$，所以 $s$ 实现非平凡域自同构。

若 $g$ 正规化 $C$，它也正规化 $\mathbb F_p$-代数 $\mathbb F_p[C]\cong\mathbb F_{p^2}$。诱导的域自同构或为恒等，或为 Frobenius。第一种情形中，$g$ 是一维 $\mathbb F_{p^2}$-空间的线性自同构，故在 $C$ 中；第二种情形中 $gs$ 属于 $C$。因此
$$N:=N_{\mathrm{GL}_2(\mathbb F_p)}(C)=C\sqcup Cs,\qquad |N|=2(p^2-1).$$

于是 $N$ 没有阶为 $p$ 的元素。对 $aI+bJ\in C$，特征多项式判别式为 $4db^2$；$b=0$ 时为标量，$b\ne0$ 时为非平方元。对 $(aI+bJ)s\in Cs$，矩阵为
$$\begin{pmatrix}a&-db\\b&-a\end{pmatrix},$$
迹为零。

得到两个以后反复使用的结论：

1. $N$ 中有两个不同 $\mathbb F_p$-特征值的元素必在 $Cs$，两个特征值之比为 $-1$。
2. $C$ 中有一个 $\mathbb F_p$-特征值的元素必为标量。

## 3. 一个低次数方法的界限

假设像**等于** $N$。群 $C=\mathbb F_{p^2}^\times$ 已传递作用于非零向量，也传递作用于一维 $\mathbb F_p$-子空间。因此对任一非零 $P\in E[p]$，以及任一阶为 $p$ 的循环子群 $L$，有
$$[\mathbb Q(P):\mathbb Q]=p^2-1,\qquad
[\mathbb Q(L):\mathbb Q]=p+1.$$

这里 $\mathbb Q(L)$ 是该子群作为集合的最小定义域。等式由 Galois 轨道与定义域次数的对应直接得到。特别地，改到正规化子所给的二次域只会使像落在非分裂 Cartan 中，**不会**给出该二次域上的有理 $p$-同源。故不能直接套用固定次数数域上的有理同源界来排除本情形。

## 4. 仍缺少的命题

R1 没有给 $p$ 的任何绝对上界。必须另行排除完整正规化子对任意大的 $p$ 出现；单独排除其真子群、得到高度或导子依赖的界、计算固定有限个模曲线，都不完成课题。
