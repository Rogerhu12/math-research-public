# R12 附录：原交换子的统一成本有限头逼近与平均保输入

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下统一成本与同输入逼近已证明。** 结论针对原 Haar 算子 $A$ 的全部有界交换子，不是边界模型。它不从普通 Deddens 强稠密性推导平均保持输入，而是先使用 R88 已支付的交换子逼近，再做可控的准确有限头提升。

## 1. R88 的准确来源及使用范围

所用原文为

[R88：全次数 Riesz 基、有界乘法与完整交换子强闭包](R88-riesz-basis-bounded-multipliers-strong-closure.md)。

仓库完整路径是 topics/invariant-subspace-problem/results/R88-riesz-basis-bounded-multipliers-strong-closure.md。本稿使用其 §1 主定理第 3 项、式 (1.10)，以及式 (1.11) 的原交换子范围。

具体对象为

$$
H=L^2(\mathbb Z_2,\mu),\qquad
A=M_wU,\qquad Uf(y)=f(y-1),
$$

$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=\exp\left(
-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}
\right).
\tag{1.1}
$$

置

$$
\mathscr C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$

令 $\eta_j=\alpha_{j+1}/\alpha_j$，并定义

$$
\rho=2\sum_{j\ge0}\eta_j10^{j/2}<3e^{-770}<1,\qquad
\kappa=\frac{(1+\rho)^3}{1-\rho}.
\tag{1.2}
$$

R88 的已付结论是：对每个 $X\in\mathscr C$，令 $f=X1$，令 $f_m$ 为其低 $m$ 位条件期望，则存在对应 $Y_m=X_{f_m}\in\mathcal A$，满足

$$
Y_m\longrightarrow X\quad{\rm SOT},\qquad
\sup_m\|Y_m\|\le\kappa\|X\|.
\tag{1.3}
$$

这里 $Y_m$ 是范数闭代数 $\mathcal A$ 的元素，不把它自动当成一个有限次数多项式。本稿在 §3 显式完成后续多项式逼近。

## 2. 另外两个已付接口与结论

Deddens 最优常数为

$$
c_A(T)=\inf\{C:\|A^nTf\|\le C\|A^nf\|,
\quad n\ge1,\ f\in H\}.
\tag{2.1}
$$

令 $A_m=J_N\otimes I$（$N=2^m$）为原权的 nilpotent 截断，其中

$$
J_Ne_s=\alpha_{v_2(s+1)}e_{s+1}\quad(s<N-1),
\qquad J_Ne_{N-1}=0.
\tag{2.2}
$$

它满足 $\|A-A_m\|=\alpha_m$。所用新接口来自：

- [有限头最优成本](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md)：有限头下三角矩阵属于 $\mathcal D_A$，最优成本由至多 $2N$ 个端点矩阵精确计算。
- [有限共轭平均与无损成本](R12-appendix-finite-conjugation-average-and-lossless-polynomial-head-cost.md)：有限头下三角算子 $B$ 的有限共轭平均 $\Pi(B)$ 是真正的 $A$ 多项式；对任意有限次数多项式 $p$，有
  $c_A(p(A_m))\le\|p(A)\|$。若 $\deg p<N$，把系数乘 $N/(N-d)$ 后再取原截断，可使有限平均准确等于 $p(A)$。

**主定理。** 对任意 $X\in\mathscr C$，存在一列真正的有限头下三角算子 $C_\ell$，使

$$
\boxed{c_A(C_\ell)\le\kappa\|X\|\quad\text{对全部 }\ell,}
\tag{2.3}
$$

$$
\boxed{
C_\ell\longrightarrow X,\qquad
\Pi(C_\ell)\longrightarrow X
\quad{\rm SOT},}
\tag{2.4}
$$

并且可以同时要求

$$
\boxed{\|C_\ell-\Pi(C_\ell)\|\longrightarrow0.}
\tag{2.5}
$$

每个 $\Pi(C_\ell)$ 都是原 $A$ 的有限次数多项式。这里的常数是固定的 $\kappa\|X\|$；本文不把它未经证明改成 $\|X\|$。

## 3. 从 R88 的范数闭元素到真多项式

$X=0$ 时取 $C_\ell=0$。以下设 $X\ne0$，记

$$
K=\kappa\|X\|>0.
$$

从 (1.3) 取 $Y_\ell\to X$ SOT、$\|Y_\ell\|\le K$。给定正数 $\delta_\ell\to0$，由 $Y_\ell\in\mathcal A$，选真多项式 $q_\ell$ 使

$$
\|q_\ell(A)-Y_\ell\|<\delta_\ell,\qquad
\|q_\ell(A)\|\le K+\delta_\ell.
$$

令

$$
p_\ell=\frac{K}{K+\delta_\ell}\,q_\ell.
\tag{3.1}
$$

于是

$$
\|p_\ell(A)\|\le K,\qquad
\|p_\ell(A)-Y_\ell\|<2\delta_\ell.
\tag{3.2}
$$

因此

$$
p_\ell(A)\to X\quad{\rm SOT}.
\tag{3.3}
$$

此处范数逼近和缩放都已支付，未把 R88 的 $Y_\ell$ 简写成一个并不存在的有限多项式。

## 4. 同时保原算子与平均像的准确有限头提升

固定 $\ell$，写

$$
p_\ell(z)=\sum_{d=0}^{D_\ell}a_{\ell,d}z^d.
$$

取 $N=2^m>D_\ell$，定义

$$
p_{\ell,N}(z)=
\sum_{d=0}^{D_\ell}\frac{N}{N-d}a_{\ell,d}z^d,
\qquad
B_{\ell,N}=p_{\ell,N}(A_m).
\tag{4.1}
$$

它是原低 $m$ 位下三角矩阵张量尾恒等。有限平均准确给

$$
\Pi(B_{\ell,N})=p_\ell(A).
\tag{4.2}
$$

记

$$
e_{\ell,N}
=\sum_{d=1}^{D_\ell}
|a_{\ell,d}|\frac{d}{N-d}\,\beta_d,
\qquad \beta_d=\|A^d\|.
$$

则

$$
\|p_{\ell,N}(A)-p_\ell(A)\|\le e_{\ell,N}\to0
\quad(N\to\infty).
\tag{4.3}
$$

无损成本界给

$$
c_A(B_{\ell,N})\le\|p_{\ell,N}(A)\|
\le K+e_{\ell,N}.
\tag{4.4}
$$

还需控制未平均的 $B_{\ell,N}$。若 $N\ge2D_\ell$，各系数因子 $N/(N-d)$ 至多为 $2$。由幂差望远镜估计，

$$
\|p_{\ell,N}(A_m)-p_{\ell,N}(A)\|
\le
2\alpha_m
\sum_{d=1}^{D_\ell}
d|a_{\ell,d}|\alpha_0^{d-1}.
\tag{4.5}
$$

对固定 $\ell$，(4.3) 与 (4.5) 都趋零。因此可选择一个真正的 $N_\ell=2^{m_\ell}$，同时满足

$$
\|B_\ell-p_\ell(A)\|\le\varepsilon_\ell,\qquad
c_A(B_\ell)\le K+\varepsilon_\ell,
\qquad
\Pi(B_\ell)=p_\ell(A),
\tag{4.6}
$$

其中 $\varepsilon_\ell>0$ 预先取为趋零，$B_\ell=B_{\ell,N_\ell}$。这里 $N_\ell$ 对同一个多项式同时支付系数校正、原截断误差与成本，没有分别换用不同的输入来源。

最后定义

$$
t_\ell=\frac{K}{K+\varepsilon_\ell},\qquad
C_\ell=t_\ell B_\ell.
\tag{4.7}
$$

则

$$
c_A(C_\ell)\le K,\qquad
\Pi(C_\ell)=t_\ell p_\ell(A).
\tag{4.8}
$$

由于 $t_\ell\to1$、$\|p_\ell(A)\|\le K$，(3.3) 给
$\Pi(C_\ell)\to X$ SOT。同时，由 (4.6)，

$$
\|C_\ell-\Pi(C_\ell)\|
=t_\ell\|B_\ell-p_\ell(A)\|
\le\varepsilon_\ell.
\tag{4.9}
$$

所以 $C_\ell\to X$ SOT，并证明 (2.3)–(2.5)。

(4.9) 是普通算子范数结论；本稿不声称差
$C_\ell-\Pi(C_\ell)$ 的 Deddens 成本趋零。

## 5. 同一个有限输入族的插值确实被保留

由主定理，对任何固定有限输入族 $f_1,\ldots,f_t\in H$，

$$
\max_{a\le t}\|C_\ell f_a-Xf_a\|\to0,\qquad
\max_{a\le t}\|\Pi(C_\ell)f_a-Xf_a\|\to0.
\tag{5.1}
$$

而平均造成的差有统一实际上界

$$
\max_{a\le t}
\|(C_\ell-\Pi(C_\ell))f_a\|
\le\varepsilon_\ell\max_{a\le t}\|f_a\|.
\tag{5.2}
$$

这个序列依赖于原交换子 $X$，不依赖于随后拿来测试的固定输入族。保输入的理由是 (4.9) 与两者趋向同一个 $X$，不是一般强稠密性所允许的错误推断。

还可读出

$$
\|[A,C_\ell]\|
\le2\|A\|\varepsilon_\ell,
\tag{5.3}
$$

因为 $\Pi(C_\ell)$ 真正交换 $A$。这只是近似交换，不把 $C_\ell$ 宣称成交换子。

## 6. 准确开放范围

该结果为原全部有界交换子提供了统一成本的有限头来源，并同时支付有限平均对同一输入的误差。它使用了 R88 对原 Haar $A$ 的强近似，未使用边界模型或未经证明的全 $\mathcal D_A$ 保成本逼近。

以下问题仍未由本稿解决：

1. 任意 $X\in\mathcal D_A$ 是否都有相同类型的统一 $c_A$ 有限头逼近。
2. 对交换子是否可以将固定常数 $\kappa$ 进一步降为 $1$。
3. 如何从这些保成本、保输入的来源构造普通问题所需的非零闭不变量或实际费用矛盾。

已有结论排除了交换子中的非零紧算子，也排除了统一 Deddens 成本族在整个不含零球上的 localizing 性。因此不能把本稿的强近似升级为一个非零紧极限，或据此宣布统一成本 localizing。若寻找紧性或收敛选择，必须落实到额外受控的真实输入族，而不是擅自扩大到整个球。
