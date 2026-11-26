# 全 Deddens 范数闭包对 odometer 谱投影的统一距离

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的中间结论。** 这里处理全部 Deddens 范数闭包，不假设目标算子属于平移生成的具体 $C^*$ 代数。证明所有非平凡 odometer 谱投影与该闭包的距离至少为 $1/\pi$。没有证明全闭包的自伴核就是乘法 MASA，也没有得到原 $A$ 的非平凡普通闭不变子空间。

## 1. 原模型及一个对范数闭包有效的必要条件

沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的原 Haar 表示：
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),\qquad (Uf)(y)=f(y-1).
$$
权 $w$、测度、内积和算子均不改变。记
$$
\mathcal D=\mathcal D_A,\qquad
\mathcal R=\overline{\mathcal D}^{\|\cdot\|}.
$$
令 $p_j(y)$ 为第 $j$ 个二进位等于 $0$ 的指标函数，$P_j=M_{p_j}$；二进位从 $j=0$ 起编号。

[统一成本及范数闭包障碍 §6–8](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md) 已证明
$$
\|P_jX(I-P_j)\|
\le (c_A(X)+\|X\|)\eta_j
\quad(X\in\mathcal D),\qquad \eta_j\longrightarrow0.
\tag{1.1}
$$
因此对每个固定 $Y\in\mathcal R$，
$$
\|P_jY(I-P_j)\|\longrightarrow0.
\tag{1.2}
$$
证明只需先固定一个 $X\in\mathcal D$ 逼近 $Y$，取 $j\to\infty$ 后再令 $\|X-Y\|\to0$；不要求逼近序列的 Deddens 成本有统一上界。

特别地，对任意 $T\in B(H)$ 都有距离下界
$$
\boxed{
\operatorname{dist}(T,\mathcal R)
\ge\limsup_{j\to\infty}\|P_jT(I-P_j)\|.}
\tag{1.3}
$$
若 $T=T^*$，则相对 $P_jH\oplus(I-P_j)H$ 的两角互为伴随，所以
$$
\|[T,P_j]\|=\|P_jT(I-P_j)\|.
\tag{1.4}
$$
这一步没有把一般算子的交换子范数错误地当成单角范数。

## 2. Fourier 基及高位指标的一个准确系数

记 $G=\widehat{\mathbb Z_2}$，即全体有限阶连续字符组成的 Prüfer $2$ 群。它是可数群；其元素作为函数构成 $H$ 的标准正交基。定义
$$
\xi_m(y)=\exp\!\left(\frac{2\pi i(y\bmod2^m)}{2^m}\right),\qquad m\ge1.
$$
阶数至多 $2^m$ 的字符恰为循环群 $G_m=\langle\xi_m\rangle$，且 $G=\bigcup_mG_m$。

取 $N=2^{j+1}$。$p_j$ 在商 $\mathbb Z/N\mathbb Z$ 上恰为前 $N/2$ 个余类的指标函数。因此对任何 $\gamma\in G$，
$$
\left|\langle P_j\gamma,\gamma\xi_{j+1}\rangle\right|
=\left|\frac1N\sum_{r=0}^{N/2-1}e^{-2\pi ir/N}\right|
=\frac1{N\sin(\pi/N)}.
\tag{2.1}
$$
这里无论采用哪种内积线性约定，绝对值相同。最后一步使用几何级数分子 $1-e^{-\pi i}=2$；因 $0<\pi/N\le\pi/2$，分母没有符号歧义。特别地，
$$
\frac1{N\sin(\pi/N)}\ge\frac1\pi,
\qquad
\frac1{N\sin(\pi/N)}\longrightarrow\frac1\pi.
\tag{2.2}
$$

## 3. 任意非平凡 Fourier 谱投影的统一障碍

对任意子集 $S\subset G$，记 $Q_S$ 为闭子空间
$$
H_S=\overline{\operatorname{span}}\{\gamma:\gamma\in S\}
$$
的正交投影，即 $Q_S\gamma=\mathbf1_S(\gamma)\gamma$。

**定理 3.1。** 若 $\varnothing\ne S\ne G$，则对全部充分大的 $j$，
$$
\|[Q_S,P_j]\|
\ge\frac1{2^{j+1}\sin(\pi/2^{j+1})}.
\tag{3.1}
$$
因而
$$
\boxed{\operatorname{dist}(Q_S,\mathcal R)\ge\frac1\pi.}
\tag{3.2}
$$

**证明。** 固定 $\gamma_0\in S$、$\gamma_1\notin S$。其比值 $\gamma_1\gamma_0^{-1}$ 属于某个 $G_M$。对每个 $j+1\ge M$，$S$ 不可能在乘以 $\xi_{j+1}$ 下保持不变：若保持不变，它就对有限循环群 $G_{j+1}$ 的全部元素不变，而 $\gamma_0$ 与 $\gamma_1$ 在同一 $G_{j+1}$ 陪集中，和所选成员关系矛盾。

因此对每个这样的 $j$，存在某个 $\gamma=\gamma(j)\in G$ 满足
$$
\mathbf1_S(\gamma\xi_{j+1})-\mathbf1_S(\gamma)\in\{1,-1\}.
$$
在这对单位 Fourier 基向量之间取交换子的矩阵元，得到
$$
\big|\langle[Q_S,P_j]\gamma,\gamma\xi_{j+1}\rangle\big|
=\big|\langle P_j\gamma,\gamma\xi_{j+1}\rangle\big|
=\frac1{2^{j+1}\sin(\pi/2^{j+1})}.
$$
故 (3.1) 成立。由于 $Q_S$ 自伴，(1.4)、(1.3) 和 (2.2) 给 (3.2)。证毕。

注意，这里每层选取的 $\gamma(j)$ 可以变化；算子范数下界允许这种选择。不能把它换成对一个固定向量的强收敛论证，也不需要这样换。相反，$S$ 非平凡迫使**每个充分高的层**出现成员关系跳变，不只是某个子列出现。

## 4. 精确适用范围及闭代数后果

$U$ 在 Fourier 基上具有互异的特征值：
$$
U\gamma=\gamma(-1)\gamma.
$$
若两个连续字符在 $1$ 上相同，则它们在所有整数上相同，再由整数在 $\mathbb Z_2$ 中稠密得两字符相同。因此 $U$ 的每个特征空间都是一维，且这些空间的正交和等于 $H$。

所以每个 $T\in\{U\}'$ 都在此 Fourier 基上对角化。特别地，$\{U\}'$ 中的所有幂等元都是上述某个正交投影 $Q_S$。定理 3.1 给：
$$
\boxed{\mathcal R\cap\{U\}'\text{ 只含幂等元 }0,I.}
\tag{4.1}
$$
这覆盖全部谱投影，包括无限秩、无限余秩的投影，不限于紧算子，也不假设其属于 [平移生成的具体 $C^*$ 代数](R12-appendix-norm-closure-all-adic-translation-distances-and-concrete-crossed-product-core.md)。

还有两个直接推论：

1. 若 $T\in\mathcal R\cap\{U\}'$ 满足某个非零多项式 $p(T)=0$，则 $T$ 是标量。事实上，Fourier 对角值只能取 $p$ 的有限个根；每个实际出现的值所对应的谱投影都可由 Lagrange 插值写成 $T$ 的多项式，因而属于 $\mathcal R$。由 (4.1)，只有一个值能够出现。
2. 若 $T\in\mathcal R\cap\mathcal R^*\cap\{U\}'$，则 $\sigma(T)$ 连通。因为 $T$ 是正常算子，$C^*(I,T)\subset\mathcal R$。若其紧谱分成两个非空且相对既开又闭的部分，连续函数演算给一个非平凡谱投影，仍属于 $\mathcal R\cap\{U\}'$，与 (4.1) 矛盾。这里的正常性来自 Fourier 对角化，$T^*\in\mathcal R$ 则保证整个 $C^*(I,T)$ 位于 $\mathcal R$。

这些结论仍没有把 $\mathcal R\cap\mathcal R^*\cap\{U\}'$ 分类为标量。连续谱范围内的 Fourier 乘子没有因此被排除；不能把缺少非平凡谱投影替换成整个自伴代数只有标量。

## 5. 与全部自伴核问题的边界

已证明的精确自伴核 $\mathcal D\cap\mathcal D^*$ 等于物理空间的乘法 MASA；同一结论对 $\mathcal R\cap\mathcal R^*$ 的完整推广仍待证明。本稿进一步排除了其可能包含任何非平凡 odometer 谱投影，且给统一的算子范数距离。

本证明只依赖原模型中已付的高位角估计、实际 Fourier 基和一个有限几何级数。没有在完整 $B(H)$ 或完整 $\mathcal D$ 上假定连续紧群 gauge，也没有假定移动频率提取唯一决定算子；前稿的秩一反例已经表明后一假定在 $B(H)$ 上不成立。
