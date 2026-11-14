# 两条复边界上的真实场 Fourier 重构

2026-11-12，root。此引理用于整物理角场的批量时间 jet，不把有限节点的球误差
当作连续角误差。当前只给完整误差公式和预算器；真实场的全部外域仍须另证。

## 1. 约定与真实输入

物理角 θ 的周期为 `2π/q`，本题 `q=4`。设 g 全纯于闭带
`|Im θ|≤Sₒ` 的邻域，整带有真实上界 `|g|≤M`。
取 `0≤S<Sₒ`，`N≥2` 个等距点 `θj=2πj/(qN)`，在上下边界
`θj±iS` 获得真实值近似，两个边界各自的平均绝对节点误差不超过 ε。
节点近似可以是球的准确中点，但 ε 必须同时支付算术、输入和真实无限 primitive 误差。

记 `g(θ)=Σ gk exp(iqkθ)`。正 k 用下边界，负 k 用上边界；例如

\[
 \widetilde g_k=e^{-qkS}\frac1N\sum_{j=0}^{N-1}
      \widetilde g(\theta_j-iS)e^{-2\pi ikj/N},\qquad 0\le k<N/2.
\]

零模可用任一边界。只选 `K<N/2`，不在两个边界重复使用 Nyquist 模。

## 2. 所有 alias 和节点误差

准确 DFT 给

\[
 e^{-qkS}\operatorname{DFT}_k[g(\theta_j-iS)]
 =\sum_{\ell\in\mathbb Z}g_{k+\ell N}e^{q\ell NS}.
\]

由真实外带 Cauchy 界 `|gk|≤M exp(−q|k|Sₒ)`，对 `k≥0` 有

\[
 |\widetilde g_k-g_k|\le
 \epsilon e^{-qkS}+M\left\{
 \frac{e^{-qkS_o}}{e^{qN(S_o-S)}-1}
 +\frac{e^{qkS_o}}{e^{qN(S_o+S)}-1}\right\}.
 \tag{1}
\]

负 k 取绝对值后同式。两个分式分别是正、负无穷 alias 列的完整几何和。
`S=0` 也合法，此时回到实轴重构；若内复带使节点误差放大，必须用更高精度
真实 primitive/root，不能只提高最终 DFT 的工作精度。

双边界的好处是节点误差随 `|k|` 按 `exp(−q|k|S)` 衰减，避免把节点球的
同一半径作为所有 Fourier 模的白噪声，再被内带复合及高阶导数放大。

## 3. 完整内带与导数

对 `0≤s<Sₒ`，令 `P_K=Σ_|k|≤K g̃k exp(iqkθ)`。j 次物理角导数的
Wiener 范数误差（从而整个 `|Im θ|≤s` 的一致误差）不超过

\[
 \sum_{|k|\le K}(q|k|)^j e^{q|k|s}\,\operatorname{err}_k
 +2M\sum_{k=K+1}^{\infty}(qk)^j e^{-qk(S_o-s)}.
 \tag{2}
\]

j=0 时零模因子约定为一，j>0 为零。
预算源 `fourfold_boundary_fourier_budget.py` 原生 Arb 计算 j=0,1,2。
尾的无穷矩和是准确几何导数；设 `r=exp(−q(Sₒ−s)),m=K+1`：

\[
 \begin{aligned}
 \sum_{k=m}^{\infty}r^k&=r^m/(1-r),\\
 \sum_{k=m}^{\infty}kr^k&=r^m\{m/(1-r)+r/(1-r)^2\},\\
 \sum_{k=m}^{\infty}k^2r^k&=r^m\{m^2/(1-r)+2mr/(1-r)^2
                  +r(1+r)/(1-r)^3\}.
 \end{aligned}
\]

因此可以只批算真实 f，再对已付清误差的 Fourier 多项式乘 `iqk` 得到 fθ、fθθ；
不能对未付 alias 的离散数组直接微分并声明得到真实导数。

## 4. 时间变量及完整矩形余项

设真实 `f(u,θ)` 在 `|u|≤R,|Im θ|≤Sₒ` 全纯且 `|f|≤M`，
保留 `0≤i<m` 个时间系数。对每个系数用 (1)–(2)，其模界取 `M/R^i`，
并用该时间系数实际节点误差 εᵢ。评价于 `|u|≤r<R` 时，有限项误差分别乘 rᶦ。
未保留的全部时间项另支付

\[
 M\frac{(r/R)^m}{1-r/R}
 \sum_{k\in\mathbb Z}(q|k|)^j e^{-q|k|(S_o-s)}.
 \tag{3}
\]

于是时间尾包括所有角模，有限时间项包括全部 Fourier 尾和 alias，没有遗漏
“时间和角次数同时超限”的角落。源中的 `time_fourier_budget` 正按此公式实现。
只要后续完整参考外像保持 `|Im Y(u,x)|≤s`，这些一致场误差就可用于非均匀
`θ=Y(u,x)` 的评价；该外像本身以及误差对 x 的解析域仍须真实证明。

目前 R59 的已证外带针对实 r、实参数。它不能直接充当这里的复时间外域。
需要另以实际 D/M/W 的全角 Fourier/time 界证明复时间 D 不为零，并保留
真实 Q、平方根分支、参数区间和整个参考状态管，之后才可填入实际 M 与 Sₒ。
