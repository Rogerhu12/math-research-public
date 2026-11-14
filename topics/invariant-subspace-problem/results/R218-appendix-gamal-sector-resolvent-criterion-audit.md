# R218A：Gamal 扇区预解判据的逐条件核对

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：条件核对及不适用证明完整。只排除下文点名的两个充分判据直接应用于当前慢符号；不宣称所有预解增长方法均失效。本判据核对只需 R217 的全圆周粗界；R218 另已证明全圆周具有同一精确预解型 $\mathsf K$。

## 1. 一手来源与当前输入

核对来源：Maria F. Gamal’, *On existence of hyperinvariant subspaces for quasinilpotent operators with a nonsymmetry in the growth of the resolvent*, arXiv:2404.04348v1（2024-04-05）。

- 原文与版本：<https://arxiv.org/abs/2404.04348v1>。
- 已直接读取全文的 HTML：<https://arxiv.org/html/2404.04348v1>，重点 Theorem 3.1、式 (3.1)、Theorem A 与式 (3.4)。

R217（原始证明稿 [R217](R217-slow-symbol-entire-order-and-directional-resolvent-growth.md)）对逐位任取 $X_j\in\{N_j,Y_j\}$、任意复杂相位且 $|c_j|=(j+1)^{-2}$ 的
$$T=\sum_{j\ge0}c_jX_j$$
给出 $\sigma(T)=\{0\}$ 及以下**整个圆周一致**的界：
$$
\frac1r e^{1/(256r)}
\le\|(re^{i\theta}I-T)^{-1}\|
\le\frac2r e^{128/r},
\qquad 0<r\le1/256,\quad \theta\in\mathbb R.
\tag{1.1}
$$
下面只使用 (1.1)。后续 R218 已将它加强为全圆周一致的精确型 $\mathsf K=\Gamma(1/4)^4/(32\pi)$，但本判据排除无需这一加强。

## 2. 原文 Theorem 3.1 的两个必要假设

原定理取两个互不相交的扇形，半开角分别为 $\beta_1,\beta_2>0$，再取 $\beta>\max(\beta_1,\beta_2)$，记
$$\alpha=\frac{\pi}{2\beta}>0.$$
其假设同时要求：

1. 四条边界射线上，预解范数被某个固定 $C_0\exp(c_0/r^\alpha)$ 控制；
2. 在每个扇形内，对**每一个** $c>0$，都有
   $$\sup_z e^{-c/|z|^\alpha}\|(zI-T)^{-1}\|=\infty.$$

满足这些条件时，定理构造 bicommutant 中两个互相相乘为零而所有正幂均非零的算子；原文 Corollary 3.2 据此得到超不变子空间格不为全序。这里保留第2条的“每一个 $c$”量词，不能将它改成“存在一个较小的 $c$”。

## 3. 对全部指数参数的排除

**命题。** 满足 (1.1) 的算子不满足该 Theorem 3.1 的假设，无论选取哪些扇形和 $\beta$。

证明分三种情况。

### 3.1. $0<\alpha<1$

任意射线上的 (1.1) 下界给
$$
\log\|(re^{i\theta}I-T)^{-1}\|
\ge\frac1{256r}+\log\frac1r.
$$
若第1条假设成立，则这个量至多 $\log C_0+c_0/r^\alpha$。两边乘 $r$，令 $r\downarrow0$，得到 $1/256\le0$，矛盾。因此连一条边界射线都不能满足要求的上界。

### 3.2. $\alpha=1$

取例如 $c=129$。由 (1.1)，对整个穿孔小圆盘有
$$
e^{-129/|z|}\|(zI-T)^{-1}\|
\le\frac2{|z|}e^{-1/|z|},
$$
右边有界且趋于0。在扇形中远离0的剩余部分，预解函数的范数由紧性一致有界。因此第2条假设对这个 $c$ 失败。此处只用了有限上型，绝未比较不同方向的型常数。

### 3.3. $\alpha>1$

对任意固定 $c>0$，有
$$
e^{-c/|z|^\alpha}\|(zI-T)^{-1}\|
\le\frac2{|z|}\exp\left(\frac{128}{|z|}-\frac{c}{|z|^\alpha}\right)\longrightarrow0
$$
且在整个穿孔小圆盘一致。远离0仍用紧性。因此第2条假设对每个 $c>0$ 都失败。三种情况穷尽 $\alpha>0$，命题得证。

## 4. 原文所引 Theorem A 也不适用

该文末尾 Theorem A 是其参考文献 [S]（B. M. Solomjak, *Calculuses, annihilators and hyperinvariant subspaces*, J. Operator Theory 9 (1983), 341–370）中一个结果的转述。我们只核对 Gamal’ 原文准确列出的版本，不声称核对了 Solomjak 全文。

这个版本的式 (3.4) 要求在某个互补闭角域中有多项式预解上界 $K/r^N$。即使角域退化成单条射线，(1.1) 也立即排除这样的上界：
$$
\frac{r^{-1}e^{1/(256r)}}{Kr^{-N}}
=K^{-1}r^{N-1}e^{1/(256r)}\longrightarrow\infty.
$$
故该 Theorem A 不能直接应用于当前 $T$。

## 5. 结论的边界

本核对使用了具体定理的精确指数和量词，而不是从“所有方向的阶相同”推断所有非对称机制不可能。(1.1) 本身只给每个方向严格正且有限的预解型；R218 另已证明全空间算子范数在全部方向具有同一精确型 $\mathsf K$。固定 Haar 有限柱向量的局部型见 R221；局部向量增长与全空间范数增长必须区分，这一补充不影响本文对两个具体判据的排除。

尤其，本文不排除针对单向量、某个未知不变限制、另一个交换算子或其他轮廓函数的增长判据。也没有从当前充分条件失败推出慢符号的普通不变子空间不存在。有限秩 Haar-normal 湮灭泛函与普通 Hilbert ISP 的缺口保持原样。
