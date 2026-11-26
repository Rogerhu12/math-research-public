# 全 Deddens 范数闭包自伴核中的任意加权复合算子

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的中间结论。** 本稿将前一自伴核分类从平移生成代数推进到任意可测非奇异自同构的加权复合算子，并给准确距离。仍未分类全闭包的所有自伴元素，也未解决普通不变子空间问题。

## 1. 全闭包的双向细块小量

沿用原 $H=L^2(\mathbb Z_2,\mu)$、$Af(y)=w(y)f(y-1)$，置
$$
\mathcal D=\mathcal D_A,\quad
\mathcal R=\overline{\mathcal D}^{\|\cdot\|},\quad
\mathcal C=\mathcal R\cap\mathcal R^*,\quad
\mathcal M=\{M_b:b\in L^\infty\}.
$$
令 $P_{m,r}$ 为余类 $r+2^m\mathbb Z_2$ 的乘法投影。由 [全 Deddens 细块界](R12-appendix-full-deddens-algebra-optimal-cost-finite-head-approximation.md) 及范数逼近，
$$
Y\in\mathcal R\quad\Longrightarrow\quad
\max_{0\le r<s<2^m}\|P_{m,r}YP_{m,s}\|\longrightarrow0.
\tag{1.1}
$$
对 $Y\in\mathcal C$ 同时用于 $Y,Y^*$ 得
$$
\nu_m(Y):=\max_{r\ne s}\|P_{m,r}YP_{m,s}\|\longrightarrow0.
\tag{1.2}
$$
因此对任意 $X\in B(H)$，
$$
\operatorname{dist}(X,\mathcal C)\ge\limsup_m\nu_m(X).
\tag{1.3}
$$
这里取最大块的映射关于算子范数为 $1$-Lipschitz；没有把任意算子的全部非对角块相加而遗漏维数损失。

## 2. 对加权复合算子可以无损拼合全部块

设 $\sigma$ 是 $\mathbb Z_2$ 上的可测非奇异自同构，模零取逆。令 $V_\sigma$ 为其标准酉实施：
$$
(V_\sigma f)(y)=J_\sigma(y)^{1/2}f(\sigma^{-1}y),\qquad
J_\sigma=\frac{d(\mu\circ\sigma^{-1})}{d\mu}.
$$
所有等式都模零理解。给定 $v\in L^\infty$，置 $X=M_vV_\sigma$。令
$$
F=\{y:\sigma^{-1}y=y\},\quad
F_m=\{y:y\bmod2^m=\sigma^{-1}(y)\bmod2^m\}.
$$
于是 $F_m\downarrow F$。细块 $P_{m,r}XP_{m,s}$ 的输出支持是
$$
E_{rs}=
\{y:y\bmod2^m=r,\ \sigma^{-1}(y)\bmod2^m=s\}.
$$
这些集合对不同的 $(r,s)$ 两两不交，其逆像也两两不交。因此这些块有两两正交的终空间及初空间；更直接地，
$$
\sum_{(r,s)\in I}P_{m,r}XP_{m,s}
=M_{v\mathbf1_{\cup_{(r,s)\in I}E_{rs}}}V_\sigma.
$$
酉性给
$$
\boxed{\nu_m(X)
=\left\|v\mathbf1_{F_m^c}\right\|_\infty
=\left\|X-\sum_rP_{m,r}XP_{m,r}\right\|.}
\tag{2.1}
$$
这是加权复合结构的特殊性质，不对一般 $B(H)$ 算子成立。

在固定点集 $F$ 上，$J_\sigma=1$ 几乎处处：对于每个可测 $E\subset F$，有 $\sigma^{-1}E=E$ 模零，故两测度在 $F$ 上一致。因此
$$
M_{v\mathbf1_F}V_\sigma=M_{v\mathbf1_F}\in\mathcal M.
\tag{2.2}
$$

**定理 2.1（准确距离）。**
$$
\boxed{
\operatorname{dist}(M_vV_\sigma,\mathcal C)
=\operatorname{dist}(M_vV_\sigma,\mathcal M)
=\|v\mathbf1_{F^c}\|_\infty.}
\tag{2.3}
$$
特别地，$M_vV_\sigma\in\mathcal C$ 当且仅当 $v=0$ 几乎处处于 $F^c$，此时该算子已经是乘法算子。

**证明。** (1.3)、(2.1) 与 $F_m^c\uparrow F^c$ 给左侧至少为右侧。在 (2.2) 中取乘法逼近，其误差恰为右侧，且 $\mathcal M\subset\mathcal C$。两距离的上下界吻合。证毕。

## 3. 实际位于平移生成代数之外的例子

定义保 Haar 测度的 involution $\sigma$：同时交换每一对相邻二进位，
$$
(y_0,y_1,y_2,y_3,\ldots)
\longmapsto(y_1,y_0,y_3,y_2,\ldots).
$$
它的固定点要求每一对位相同，测度为 $\lim_k2^{-k}=0$。故 $V=V_\sigma=V_\sigma^*$ 为自伴酉算子，(2.3) 给
$$
\operatorname{dist}(V,\mathcal C)=1.
\tag{3.1}
$$
证明它确实超出此前范围。记
$$
\mathcal B=\overline{\operatorname{span}
\{M_bU^t:b\in L^\infty,\ t\in\mathbb Z_2\}}^{\|\cdot\|},
\qquad U^tf(y)=f(y-t).
$$
对任意固定 $t\in\mathbb Z_2$，
$$
\mu\{y:y-\sigma(y)=t\}=0.
\tag{3.2}
$$
事实上
$$
y-\sigma(y)=\sum_{k\ge0}(y_{2k+1}-y_{2k})4^k.
$$
每一位差属于 $\{-1,0,1\}$，概率分别为 $1/4,1/2,1/4$，相互独立。这样的 $4$-进展开至多唯一：若两展开不同，最低差异位的非零系数属于 $\{-2,-1,1,2\}$，不能被更高的 $4$ 的倍数抵消。因此固定 $t$ 至多指定一个位差序列，其概率不超过 $\lim_k2^{-k}=0$。

定义收缩块提取
$$
\mathcal Q_m(X)=\sum_r VP_{m,r}V^*XP_{m,r}
=V\!\left(\sum_rP_{m,r}V^*XP_{m,r}\right).
\tag{3.3}
$$
括号内是对 $V^*X$ 的块对角条件期望，故 $\|\mathcal Q_m\|\le1$；且 $\mathcal Q_m(V)=V$。

对单项 $M_bU^t$，(3.3) 只保留输出点满足
$$
\sigma^{-1}(y)\bmod2^m=(y-t)\bmod2^m
$$
的部分。其支持随 $m$ 递减到 $\{y:y-\sigma^{-1}(y)=t\}$，由 $\sigma^{-1}=\sigma$ 和 (3.2) 为零测。因此
$$
\mathcal Q_m(M_bU^t)\mathbf1\longrightarrow0
\quad\text{于 }L^2.
$$
对任何有限平移和 $Z$ 同样成立。于是
$$
\|V-Z\|\ge\|\mathcal Q_m(V-Z)\mathbf1\|\longrightarrow1.
$$
取范数闭包并用 $Z=0$ 得
$$
\boxed{\operatorname{dist}(V,\mathcal B)=1.}
\tag{3.4}
$$
所以定理 2.1 的适用范围确实包含前一具体代数之外的算子。

## 4. 剩余范围

加权复合算子能够无损拼合细块，是因为它把每个可测输入片送到单一可测输出片。任意算子的非对角块没有这种共同正交性，不能用 (2.1) 替换其三角截断估计。故本稿没有推出整个 $\mathcal C=\mathcal M$。

这一子类已处理完毕；后续正向工作转向同一实际输入的非复制运输插值，不再用未知不变子空间的正交投影属于 $\mathcal D$ 或 $\mathcal R$ 作为未经支付的假设。
