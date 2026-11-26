# 原 Haar 模型及任意可分重数的自伴 Deddens 核与有限成本不变投影

日期：2026-11-27（UTC+8；核查于 2026-11-26 UTC）。会话：`Astra-ISP-8542378f-20261127`，分工 `literature_deddens`；AI-assisted，GPT-6 Astra Pro。

**状态：第 2–5 节为完整证明的中间结论。** 原普通 Hilbert ISP 未完成。这里刻画原 Deddens 代数的整个自伴核，并证明真实不变投影若有有限 Deddens 成本，必然只是显然的常值重数投影。任意可分重数的推广由主会话提出，第 5 节用可数对角积分写全，不使用有限秩假设。没有假设未知不变空间被 Deddens 代数保持，也没有声称其正交投影具有有限成本。

## 1. 本次一手文献核对

本次直接核对以下作者／期刊页面，未找到可以直接采用的、公认的完整普通复 Hilbert ISP 答案。

- I. Chalendar、J. R. Partington，*Recent perspectives on the Invariant Subspace Problem*，现为 [arXiv:2507.21834v2](https://arxiv.org/abs/2507.21834v2)，2026-10-23；[全文 §1](https://arxiv.org/html/2507.21834v2) 仍明确说 Hilbert 情形开放。作者注记为修正笔误、更新参考文献。旧审计所引 v1 可改引这一版本；这不是完整解答。
- Per H. Enflo，*On the invariant subspace problem in Hilbert spaces*，[arXiv:2305.15442](https://arxiv.org/abs/2305.15442) 仍列 2024-04-06 的 v2，27 页，声称肯定解答。本次没有逐行重审该稿，不将声称升级为可用定理，也不称其已被证伪。
- Charles W. Neville，*A Proof of the Invariant Subspace Conjecture for Separable Hilbert Spaces*，[arXiv:2307.08176](https://arxiv.org/abs/2307.08176) 仍列 2023-07-21 的 v2。旧审计中针对具体步骤的反例未因出现新版本而失效；本次没有重做这些反例。
- Khalil 等，*The Invariant Subspace Problem for Separable Hilbert Spaces*，Axioms 13 (2024), 598，[期刊原页](https://www.mdpi.com/2075-1680/13/9/598) 仍显示编辑部正在调查相关质疑的 notice；页面没有给出撤稿标记。不能把调查 notice 写成撤稿。
- L. Kérchy、C. Pearcy，*Hyperinvariant subspaces of block-triangular operators on Hilbert space*，[arXiv:2503.13005](https://arxiv.org/abs/2503.13005) 仍显示 2025-03-29 撤回，作者注记 Theorem 3 有 Hari Bercovici 的反例。不能用它把超不变子空间反例接成普通 ISP 反例。
- J. Fang、B. Hou、C. Jiang、Y. Zhang，*The invariant subspace problem and Rosenblum operators II*，[arXiv:2610.11202](https://arxiv.org/abs/2610.11202)，2026-10-08，摘要给出 Sobolev 圆盘代数约化及指定条件下的结论，未声称解决全部普通 Hilbert ISP。本次只核对摘要，不把全文未读定理列为依赖。

这项文献核对的判断限于实际查到的来源；下列模型内证明不依赖任何未确立的完整解答声称。

## 2. 原算子、成本与全尾块估计

沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的同一个 Haar 空间和权：
$$
H=L^2(\mathbb Z_2,\mu),\qquad (Af)(y)=w(y)f(y-1),
$$
$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=e^{-L_j},\quad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{2.1}
$$
写
$$
\beta_n=\|A^n\|=\prod_{a=1}^n\alpha_{v_2(a)},\qquad \beta_0=1,
$$
$$
\mathcal D_A=\{X\in B(H):c_A(X)<\infty\},\qquad
c_A(X)=\inf\{C:\|A^nXf\|\le C\|A^nf\|\ (n\ge1,f\in H)\}.
\tag{2.2}
$$
令 $N=2^m$，在原分解
$$
H=\mathbb C^N\otimes L^2(\mathbb Z_2),\qquad
f\mapsto\big(N^{-1/2}f(r+Nz)\big)_{0\le r<N}
\tag{2.3}
$$
下记 $X=(X_{rs})$。每个 $X_{rs}$ 都是**完整尾空间上的算子**，而不是尾常向量压缩。

[最优成本有限头逼近稿](R12-appendix-full-deddens-algebra-optimal-cost-finite-head-approximation.md) §2 已证
$$
\|X_{rs}\|\le c_A(X)\frac{\alpha_m}{\beta_{N-1}}
\qquad(0\le r<s<N).
\tag{2.4}
$$
这里重写所需短论证。取 $n=N-s$ 和实际输入 $e_s\otimes g$。其 $A^n$ 像恰跨一次低头边界，范数至多
$$
\frac{\beta_{N-1}}{\beta_s}\alpha_m\|g\|.
$$
而 $X(e_s\otimes g)$ 的第 $r$ 分量经过这 $n$ 步没有跨边界，成为第 $N-s+r$ 分量，范数为
$$
\frac{\beta_{N-s+r}}{\beta_r}\|X_{rs}g\|.
$$
不同初始低头的输出低头不同，故该分量范数不大于全部输出范数。Deddens 不等式给
$$
\|X_{rs}\|\le c_A(X)\alpha_m
\frac{\beta_r\beta_{N-1}}{\beta_s\beta_{N-s+r}}
\le c_A(X)\frac{\alpha_m}{\beta_{N-1}},
$$
最后使用 $1\ge\beta_0\ge\cdots\ge\beta_{N-1}>0$。

原权给出的显式估计为
$$
\frac{\alpha_m}{\beta_{N-1}}
\le \exp\!\left(-\frac{90}{7}16^m\right).
\tag{2.5}
$$
例如由 $20\,16^j\le L_j\le100\,16^j$ 及
$-\log\beta_{N-1}=\sum_{j<m}2^{m-j-1}L_j$
立即得到 (2.5)。因此 $N\alpha_m/\beta_{N-1}\to0$。

## 3. 整个自伴核恰为乘法 MASA

记 $\mathcal D_A^*=\{Y^*:Y\in\mathcal D_A\}$，以及
$$
\mathcal M=\{M_b:b\in L^\infty(\mathbb Z_2,\mu)\}.
$$

**定理 3.1。**
$$
\boxed{\mathcal D_A\cap\mathcal D_A^*=\mathcal M.}
\tag{3.1}
$$
更准确地，若 $X,X^*\in\mathcal D_A$，令 $P_{m,r}$ 为第 $r$ 个低 $m$ 位圆柱的乘法投影，并令
$$
\Delta_m(X)=\sum_{r=0}^{N-1}P_{m,r}XP_{m,r}.
$$
则
$$
\boxed{\|X-\Delta_m(X)\|
\le (N-1)\frac{\alpha_m}{\beta_{N-1}}
\max\{c_A(X),c_A(X^*)\}\longrightarrow0.}
\tag{3.2}
$$

**证明。** 对 $r<s$ 用 (2.4)；对 $r>s$ 将 (2.4) 用于 $X^*$，注意 $(X^*)_{sr}=X_{rs}^*$。于是每个非对角块的范数至多
$$
b_m=\frac{\alpha_m}{\beta_{N-1}}
\max\{c_A(X),c_A(X^*)\}.
$$
对尾向量族 $u=(u_s)_{s<N}$，若 $Y=X-\Delta_m(X)$，则
$$
\|(Yu)_r\|\le b_m\sum_{s\ne r}\|u_s\|.
$$
标量矩阵在对角线为零、其余元素为 $b_m$，其 $\ell^2_N$ 范数为 $(N-1)b_m$。所以得到 (3.2)；也可由行和、列和同为 $(N-1)b_m$ 的 Schur 估计得到同一界。

固定任意低 $k$ 位圆柱投影 $P_{k,a}$。当 $m\ge k$ 时，它是若干 $P_{m,r}$ 的和，因而与 $\Delta_m(X)$ 交换。因此
$$
\|[X,P_{k,a}]\|\le2\|X-\Delta_m(X)\|\longrightarrow0,
$$
从而 $[X,P_{k,a}]=0$。所有圆柱集合生成 Borel $\sigma$ 代数；通过指标函数的强极限，$X$ 与每个可测集合的乘法投影交换。

为使最后的乘法结论自含，令 $b=X\mathbf1$。对每个可测 $E$，
$$
X\mathbf1_E=\mathbf1_Eb,\qquad
\|\mathbf1_Eb\|_2\le\|X\|\mu(E)^{1/2}.
$$
若 $|b|>\|X\|+\varepsilon$ 在正测集合上成立，这个不等式在该集合上矛盾。因此 $b\in L^\infty$ 且 $\|b\|_\infty\le\|X\|$。再对简单函数用线性、对全 $L^2$ 用稠密性，得 $X=M_b$。

反向，原恒等式
$$
A^nM_b=M_{b(\cdot-n)}A^n
$$
给 $c_A(M_b)\le\|b\|_\infty$，对 $\bar b$ 同样成立，所以 $M_b\in\mathcal D_A\cap\mathcal D_A^*$。事实上 [负幂与等距共轭稿](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 的 $\|X\|\le c_A(X)$ 还给
$$
c_A(M_b)=\|b\|_\infty.
$$
证毕。

此结论要求 $X$ 和 $X^*$ 各自有**一个固定的全正幂成本**。没有把原算子范数闭包或仅强闭包也说成满足 (3.1)。

## 4. 任意真实普通不变投影的成本必然无限

**推论 4.1。** 设 $M\subset H$ 为闭的 $A$-不变子空间。若其正交投影 $P_M$ 属于 $\mathcal D_A$，则 $M=0$ 或 $M=H$。等价地，任何非零真闭 $A$-不变子空间都必须满足
$$
\boxed{c_A(P_M)=\infty.}
\tag{4.1}
$$

**证明。** 因 $P_M=P_M^*$，定理 3.1 给 $P_M=M_{\mathbf1_E}$，其中 $E$ 可测。$A$-不变性正是
$$
(I-P_M)AP_M=0.
$$
代入原 $A=M_wU$，并使用 $w>0$ 几乎处处，得到
$$
\mathbf1_E(y-1)\le\mathbf1_E(y)\quad\text{a.e.}
$$
两边积分相等，故事实上相等。odometer 的遍历性推出 $\mu(E)=0$ 或 $1$。也可不用遍历性名称：平移不变的指标函数被每个
$2^{-m}\sum_{q=0}^{2^m-1}U^q$
固定，而这些平均强趋常函数投影，所以指标函数为常数。证毕。

这说明不能把“$P_M$ 是一个有界投影”替换成“$P_M$ 具有有限 Deddens 成本”，即使只要求有限而不要求预先给定的统一上界。

## 5. 任意非零可分重数的完整版本

固定一个非零可分 Hilbert 空间 $K$，允许 $\dim K=\infty$，令
$$
H_K=L^2(\mathbb Z_2;K),\qquad A_K=A\otimes I_K.
$$
Deddens 成本仍用全部正整数幂定义。第 2 节的全部低头块计算不变，只把尾空间换成 $L^2(\mathbb Z_2;K)$。因此
$$
\boxed{\mathcal D_{A_K}\cap\mathcal D_{A_K}^*
=\{M_B:B:\mathbb Z_2\to B(K)\text{ 弱算子可测且本质一致有界}\}.}
\tag{5.1}
$$
右侧是相对于原 Haar 变量的全部可分解算子，不把 $B(K)$ 的范数可测性设为额外条件。

为补全从交换圆柱投影到可分解性的步骤，取 $K$ 的有限或可数正交基 $(e_j)$。若 $X$ 与全部标量乘法投影交换，则每个标量块 $X_{ij}:L^2\to L^2$ 同样交换；第 3 节给 $X_{ij}=M_{b_{ij}}$。对只有有限个有理复坐标的向量 $u,v\in K$，相应标量乘子的函数为 $\sum_{i,j}\overline v_i b_{ij}(y)u_j$，其本质上确界不大于 $\|X\|\|u\|\|v\|$。这些 $u,v$ 构成可数集，可以一次去掉全部零测例外。于是几乎每个 $y$ 上，该矩阵在稠密的有限支撑向量空间定义范数至多 $\|X\|$ 的算子，并唯一延为 $B(y)\in B(K)$。矩阵元素可测保证弱算子可测；由 $K$ 可分，$y\mapsto B(y)f(y)$ 对每个强可测向量场 $f$ 也是强可测。先对简单 $K$ 值函数、再由稠密性可得 $X=M_B$。

反向由原恒等式 $A_K^nM_B=M_{B(\cdot-n)}A_K^n$ 立即成立，且 $c_{A_K}(M_B)=\operatorname*{ess\,sup}_y\|B(y)\|$。

**推论 5.2。** 若 $M\subset H_K$ 是闭的 $A_K$-不变子空间，且 $c_{A_K}(P_M)<\infty$，则存在一个固定闭子空间 $E_0\subset K$，使
$$
\boxed{M=L^2(\mathbb Z_2;E_0).}
\tag{5.2}
$$

**证明。** (5.1) 给 $P_M=M_{P(y)}$，其中 $P(y)$ 是弱算子可测的正交投影场。原不变性等价于
$$
(I-P(y))P(y-1)=0\quad\text{a.e.}
$$
故 $P(y-1)\le P(y)$。对可数正交基中的每个 $e_j$，函数
$$
d_j(y)=\langle(P(y)-P(y-1))e_j,e_j\rangle
$$
非负，且 Haar 平移不变性给 $\int d_j\,d\mu=0$。所以每个 $d_j=0$ 几乎处处；去掉这可数族的零测例外并集后，正算子 $P(y)-P(y-1)$ 的全部对角元为零。其正平方根于是消去每个 $e_j$，因而算子为零。因此
$$
P(y)=P(y-1)\quad\text{a.e.}
$$
对全部可数矩阵元素用 odometer 遍历性，得到 $P(y)=P_0$ 几乎处处，其中 $P_0$ 是固定正交投影。取 $E_0=\operatorname{Ran}P_0$ 即得 (5.2)。反向显然成立，非零投影的成本为 $1$。证毕。

本结论没有声称一般真实不变旗子商的投影具有有限成本。它只精确刻画该额外成本假设究竟允许哪些投影。

## 6. 尚未闭合的目标

本稿没有给出未知 $A$-不变空间，也没有排除它们。整个 Deddens 代数的最优有限头插值、负幂域保持及等距共轭可以继续用于**实际同一来源**的费用问题；但用其成本闭球来控制未知正交投影，会直接落入 (4.1) 的障碍。

尚需推进的是非复制递推的真实最优费用或另一种普通不变子空间构造。全代数的强稠密、固定成本球的弱紧，以及有限共轭平均的存在，都没有支付这一剩余步骤。
