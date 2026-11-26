# 全 Deddens 插值的连续整数前缀约束及软最优目标连接障碍

作者：OpenAI ChatGPT，`/root/literature_deddens`；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的中间结论。** 本稿对原 $A$ 的全部 Deddens 算子证明一个实际普通范数约束。它表明：前稿逐个求出的软逆像最优目标不能直接串成普通范数统一有界的 Deddens 递推。没有更换 Hilbert 空间来构造不变子空间，也没有假定任意 L² 等价类有可用点值。

## 1. 原连续函数与完整细块估计

仍在原 $H=L^2(\mathbb Z_2,\mu)$ 上，$Af(y)=w(y)f(y-1)$，$w$ 和 $\alpha_j$ 为原权。$C(\mathbb Z_2)$ 中的函数使用其唯一连续代表；这些点值不是任意 $L^2$ 代表的点值。

对 $N=2^m$，令 $P_{m,s}$ 为余类 $s+N\mathbb Z_2$ 的乘法投影。已证明的 [全 Deddens 细块界](R12-appendix-full-deddens-algebra-optimal-cost-finite-head-approximation.md) 给
$$
\|P_{m,r}XP_{m,s}\|\le c_A(X)\varepsilon_m
\quad(0\le r<s<N, X\in\mathcal D_A),
\tag{1.1}
$$
$$
\varepsilon_m=\frac{\alpha_m}{\beta_{N-1}},\qquad
N^{3/2}\varepsilon_m\longrightarrow0.
\tag{1.2}
$$
第二项由原显式权的四次指数衰减直接得到；已有更强界
$\varepsilon_m\le\exp(-(90/7)16^m)$。这里是整个尾块的范数估计，不是仅有常尾矩阵元。

## 2. 完整 Deddens 插值必须满足的整数前缀条件

**定理 2.1。** 若 $X\in\mathcal D_A$，$h,g\in C(\mathbb Z_2)$，且 $Xh=g$ 作为原 $L^2$ 向量成立，则每个整数 $q\ge0$ 都满足
$$
\boxed{\sum_{s=0}^{q}|g(s)|^2
\le\|X\|^2\sum_{s=0}^{q}|h(s)|^2.}
\tag{2.1}
$$
$X$ 不必将所有连续函数送到连续函数；只要求本次真实输入、输出连续。$X$ 也不必为有限头、正算子或加权复合算子。

**证明。** 固定 $q$，令 $m$ 足够大使 $N>q$，并置
$$
P_m=\sum_{s=0}^{q}P_{m,s}.
$$
由 (1.1)，用行列数的粗估计即可得
$$
\|P_mX(I-P_m)\|\le Nc_A(X)\varepsilon_m.
$$
故在同一个原输入 $h$ 上，
$$
\|P_mg\|
\le\|X\|\|P_mh\|+Nc_A(X)\varepsilon_m\|h\|.
\tag{2.2}
$$
乘以 $\sqrt N$。对连续函数 $f$，原 Haar 坐标给
$$
N\|P_mf\|^2
=\sum_{s=0}^{q}\int|f(s+Nz)|^2d\mu(z)
\longrightarrow\sum_{s=0}^{q}|f(s)|^2.
\tag{2.3}
$$
因为 $s+Nz\to s$ 在 $z$ 上一致，连续函数在紧空间上一致连续。由 (1.2)，(2.2) 的末项在乘以 $\sqrt N$ 后趋零。取极限并平方便得 (2.1)。证毕。

注意成本 $c_A(X)$ 只需对当前固定的实际 $X$ 有限；结论右侧是更小的普通范数 $\|X\|$。本证明没有对一列成本发散的范数逼近算子交换极限，所以不把 (2.1) 自动推广到整个 $\overline{\mathcal D_A}^{\|\cdot\|}$。

## 3. 连续非零目标的最早整数迹必须向前移动

对非零 $f\in C(\mathbb Z_2)$，定义
$$
\operatorname{ord}_{\mathbb N}f=\min\{s\ge0:f(s)\ne0\}.
$$
非负整数在 $\mathbb Z_2$ 中稠密，所以该最小值一定有限。由 (2.1)，若 $Xh=g\ne0$ 且两者连续，便有
$$
\operatorname{ord}_{\mathbb N}g\ge\operatorname{ord}_{\mathbb N}h.
\tag{3.1}
$$
又原 $w$ 只在整数点 $0$ 为零，而所有正整数点的权为正，所以
$$
\operatorname{ord}_{\mathbb N}(Af)
=\operatorname{ord}_{\mathbb N}f+1.
\tag{3.2}
$$
因此任何实际连续递推 $f_n=R_nAf_{n-1}$、$R_n\in\mathcal D_A$、$f_n\ne0$，都必须满足
$$
\operatorname{ord}_{\mathbb N}f_n
\ge\operatorname{ord}_{\mathbb N}f_{n-1}+1.
\tag{3.3}
$$
除了零点数量，前缀范数还保留最早非零点的准确幅值。这是下面连接检验所需的信息。

## 4. 逐个软最优目标不能直接接成统一有界递推

固定 $0<r<1$。由 [软目标的准确逆像最优化](R12-appendix-exact-soft-target-inverse-optimization-and-dyadic-budget.md)，对每个 $n\ge1$，在球 $\|g-\mathbf1\|\le r$ 内最小化 $\|A^{-n}g\|$ 的唯一目标是
$$
g_{n,r}(y)=\frac{W_n(y)^2}{W_n(y)^2+\lambda_n(r)},\qquad
\lambda_n(r)>0.
\tag{4.1}
$$
$W_n$ 连续，分母处处严格正，所以 $g_{n,r}$ 确为连续函数。它的零点准确为 $0,1,\ldots,n-1$，并且在整数 $n$ 非零。

原准确幂范数给
$$
W_n(n)=\prod_{a=1}^nw(a)=\beta_n=\|W_n\|_\infty.
$$
函数 $t\mapsto t^2/(t^2+\lambda_n(r))$ 在 $t\ge0$ 上增加，因此
$$
0\le g_{n,r}(y)\le g_{n,r}(n)\le1.
$$
于是原球误差满足
$$
r=\|g_{n,r}-\mathbf1\|
\ge1-g_{n,r}(n),\qquad
\boxed{g_{n,r}(n)\ge1-r.}
\tag{4.2}
$$
这说明第 $n$ 点的下界来自全体原函数的最大值及实际球误差，不是任选代表在一个零测点上赋值。

设 $n\ge2$，某个 $R_n\in\mathcal D_A$ 实现了准确连接
$$
R_nA g_{n-1,r}=g_{n,r}.
\tag{4.3}
$$
输入 $h_n=A g_{n-1,r}$ 也连续。在整数 $0,\ldots,n-1$ 上，输入和输出都为零；在第 $n$ 点，
$$
h_n(n)=\alpha_{v_2(n)}g_{n-1,r}(n-1),
\qquad 0<g_{n-1,r}(n-1)\le1.
$$
将定理 2.1 用于 $q=n$，得到
$$
\boxed{\|R_n\|\ge
\frac{g_{n,r}(n)}{
\alpha_{v_2(n)}g_{n-1,r}(n-1)}
\ge\frac{1-r}{\alpha_{v_2(n)}}.}
\tag{4.4}
$$
沿 $n=2^j$，右侧趋于无穷。因此这些逐个最优的软目标**不能**由一列普通算子范数统一有界的 Deddens 算子准确连接。允许其 Deddens 成本任意大也不消除 (4.4) 的普通范数障碍。

这不排除改变软目标、改变最早非零整数迹位置或幅值后得到别的递推；也不排除只在 $L^2$ 中近似这些目标。后一种近似若不控制连续整数迹，不能将 (4.4) 原样套用。

## 5. 对后续同源设计的准确要求

[已实现的运输递推](R12-appendix-same-source-transport-interpolation-and-sustainable-actual-recursion.md) 的目标最早整数迹为 $2n-1$，与独立逆像最优目标的 $n$ 不同。其普通范数构造选择的是原奇数强源，真实源权一直为 $\alpha_0$，因而没有遭遇 (4.4) 的逐 dyadic 深权。

但该硬目标的真实 $A^{-1}$ 范数造成了已经证明的五次成本。新的方案必须同时付两件事：用实际连续前缀 (2.1) 控制可实现的普通范数，并用完整 $A^{-k}$ 范数或运输加权列控制 Deddens 成本。只修复其中一项，不能宣布同一来源递推已连接。
