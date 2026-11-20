# R12 附录：完整 Haar 交换子的收缩多项式逼近与最优有限头成本

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下原算子块身份、收缩强逼近及同输入有限头结论均已证明。** 对原 Haar 算子的每个有界交换子 $X$，存在真正的有限多项式 $q_m(A)$ 强趋 $X$，且逐项 $\|q_m(A)\|\le\|X\|$。因此，有限头及其有限共轭平均同时逼近 $X$ 时，Deddens 成本可取最优的统一上界 $\|X\|$，不再需要 R88 给出的固定系数 $\kappa>1$。

本稿的对象始终是 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R12](R12-normalized-powers-and-compact-commutant.md) 的原 $L^2(\mathbb Z_2,\mu)$ 算子。它加强 [R88](R88-riesz-basis-bounded-multipliers-strong-closure.md) §7 的整个交换子强闭包结论，以及 [统一成本逼近附录](R12-appendix-commutant-uniform-cost-head-approximation-and-average-interpolation.md) 的固定 $\kappa$ 结论。证明不使用 R88 的线性乘子对应，更不将该对应当作代数同构。

## 1. 对象、有限头与结论

固定 Haar 概率空间及原算子
$$
H=L^2(\mathbb Z_2,\mu),\qquad (Uf)(y)=f(y-1),\qquad A=M_wU,
$$
$$
w(0)=0,\qquad w(y)=\alpha_{v_2(y)}\quad(y\ne0),\qquad
\alpha_j=e^{-L_j},
$$
$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad \alpha_0=e^{-20}<1.
\tag{1.1}
$$
写
$$
\beta_0=1,\qquad
\beta_n=\|A^n\|=\prod_{a=1}^n\alpha_{v_2(a)}.
\tag{1.2}
$$

令 $m\ge1$、$N=2^m$，采用由 $y=r+Nz$ 给出的酉分解
$$
H\simeq\mathbb C^N\otimes L^2(\mathbb Z_2,\mu),\qquad
f\longmapsto \big(N^{-1/2}f(r+Nz)\big)_{0\le r<N}.
\tag{1.3}
$$
有限头空间 $H_m$ 是只依赖低 $m$ 位的函数，等距嵌入记为
$$
J_m:\mathbb C^N\longrightarrow H,\qquad
u\longmapsto u\otimes\mathbf1.
$$
这里尾常函数 $\mathbf1$ 的范数为一。令
$$
\mathcal T_m(X)=(J_m^*XJ_m)\otimes I_{\rm tail}.
\tag{1.4}
$$
右端通过 (1.3) 看作 $H$ 上的算子。它是有限矩阵的提升，通常不是有限秩算子。

记 $J_N$ 为真正的原加权 nilpotent 头：
$$
J_Ne_s=\alpha_{v_2(s+1)}e_{s+1}\quad(0\le s<N-1),
\qquad J_Ne_{N-1}=0,
$$
并置 $A_m=J_N\otimes I_{\rm tail}$。已有
$$
\|A\|=\|A_m\|=\alpha_0,\qquad \|A-A_m\|=\alpha_m.
\tag{1.5}
$$

定义
$$
\varepsilon_m=
\frac{\alpha_m}{\beta_{N-1}}
\left(N+\frac1{(1-\alpha_0)^2}\right).
\tag{1.6}
$$
则 $\varepsilon_m\to0$。

**定理。** 对每个 $X\in\{A\}'$，都有次数小于 $2^m$ 的多项式 $p_m$，满足
$$
\|p_m(A)-\mathcal T_m(X)\|\le\varepsilon_m\|X\|.
\tag{1.7}
$$
因而
$$
q_m(z)=\frac{p_m(z)}{1+\varepsilon_m}
\tag{1.8}
$$
满足
$$
\boxed{\ \|q_m(A)\|\le\|X\|,\qquad q_m(A)\xrightarrow{\rm SOT}X.\ }
\tag{1.9}
$$
特别地，原交换子算子范数单位球恰为原多项式单位球的 SOT 闭包。

后一闭包等式的反向包含也成立，因为交换关系对有界算子的强收敛保持，且范数单位球强闭。没有将强闭包等同于范数闭包。

## 2. 压缩提升对所有有界算子收缩强趋恒等

对任意 $X\in B(H)$，
$$
\|\mathcal T_m(X)\|\le\|X\|.
\tag{2.1}
$$
令 $Q_m=J_mJ_m^*$ 为投到 $H_m$ 的正交投影。若 $f\in H_k$ 且 $m\ge k$，则
$$
\mathcal T_m(X)f=Q_mXf\longrightarrow Xf,
\tag{2.2}
$$
因为 $Q_m\to I$ 强收敛。有限柱函数的并稠密，结合 (2.1)，得到
$$
\mathcal T_m(X)\xrightarrow{\rm SOT}X
\quad\text{对每个 }X\in B(H).
\tag{2.3}
$$
本节不要求交换性。交换性将在下一节把整个压缩矩阵变成一个真正多项式，加上可控的小误差。

## 3. 越过有限头边界的精确块身份

在尾空间上定义
$$
(B_mg)(z)=w(Nz)g(z-1).
\tag{3.1}
$$
于是
$$
\|B_m\|=\alpha_m,\qquad
A=J_N\otimes I+e_{0,N-1}\otimes B_m.
\tag{3.2}
$$
此式保留了真实的跨头进位：从输入低头 $N-1$、尾 $z-1$ 走到输出低头 $0$、尾 $z$，权重正是 $w(Nz)$。特别地，
$$
A^N=\beta_{N-1}I_{\mathbb C^N}\otimes B_m.
\tag{3.3}
$$

把 $X\in\{A\}'$ 写成尾算子块 $(X_{rs})_{0\le r,s<N}$。从
$$
A^s(e_0\otimes g)=\beta_s e_s\otimes g,\qquad 0\le s<N,
$$
及 $XA^s=A^sX$，得到
$$
X(e_s\otimes g)=\beta_s^{-1}A^sX(e_0\otimes g).
\tag{3.4}
$$

若 $r\ge s$，所对应的原输入低头为 $d=r-s$，向前走 $s$ 步不跨边界。因此
$$
\boxed{\ X_{rs}=\frac{\beta_r}{\beta_s\beta_{r-s}}\,X_{r-s,0}
\qquad(r\ge s).\ }
\tag{3.5}
$$
若 $r<s$，原输入低头为 $d=N+r-s$，这 $s$ 步恰跨一次边界。边界前后的低头权重分别为
$\beta_{N-1}/\beta_d$ 和 $\beta_r$，故
$$
\boxed{\ X_{rs}=
\frac{\beta_r\beta_{N-1}}{\beta_s\beta_{N+r-s}}\,
B_m X_{N+r-s,0}
\qquad(r<s).\ }
\tag{3.6}
$$
以上直接来自算子作用，无需假设不同头、尾对象可交换。由 (3.3) 还可推出每个 $X_{rs}$ 与 $B_m$ 交换，但下面的估计不需要使用这一额外事实。

因为各 $\alpha_j<1$，$\beta_0\ge\beta_1\ge\cdots$。所以 (3.6) 的标量系数满足
$$
\frac{\beta_r\beta_{N-1}}{\beta_s\beta_{N+r-s}}
\le\frac1{\beta_{N-1}}.
$$
又 $\|X_{d0}\|\le\|X\|$，因此
$$
\|X_{rs}\|\le
\frac{\alpha_m}{\beta_{N-1}}\|X\|
\qquad(r<s).
\tag{3.7}
$$

## 4. 从压缩第一列构造真正多项式

令尾常向量压缩为
$$
x_d=\langle X_{d0}\mathbf1,\mathbf1\rangle,\qquad 0\le d<N,
$$
故 $|x_d|\le\|X\|$。定义
$$
p_m(z)=\sum_{d=0}^{N-1}\frac{x_d}{\beta_d}z^d.
\tag{4.1}
$$
$J_N^d$ 的第 $(r,s)$ 元素在 $r=s+d<N$ 时为 $\beta_r/\beta_s$，其余为零。因此 (3.5) 给出：$p_m(J_N)$ 恰为压缩矩阵 $J_m^*XJ_m$ 的下三角部分，包括对角线。

剩余上三角部分的每个元素由 (3.7) 控制。一个 $N\times N$ 矩阵的范数至多为 $N$ 乘最大元素绝对值，所以
$$
\|p_m(A_m)-\mathcal T_m(X)\|
\le \frac{N\alpha_m}{\beta_{N-1}}\|X\|.
\tag{4.2}
$$

幂的 telescoping 和 (1.5) 给
$$
\|A^d-A_m^d\|\le d\alpha_0^{d-1}\alpha_m.
$$
于是
$$
\begin{aligned}
\|p_m(A)-p_m(A_m)\|
&\le\alpha_m\|X\|
  \sum_{d=1}^{N-1}\frac{d\alpha_0^{d-1}}{\beta_d}\\
&\le\frac{\alpha_m}{\beta_{N-1}}
      \frac1{(1-\alpha_0)^2}\|X\|.
\end{aligned}
\tag{4.3}
$$
合并 (4.2)–(4.3) 就是 (1.7)。由 (2.1)、(2.3) 和 $\varepsilon_m\to0$，(1.8)–(1.9) 随即成立。

为了明确核对最后一个极限，由 (1.1) 直接有
$$
20\,16^j\le L_j\le100\,16^j\qquad(j\ge0).
\tag{4.4}
$$
在 $1,\ldots,2^m-1$ 中，精确有 $2^{m-j-1}$ 个整数的 2-adic 赋值为 $j<m$。因此
$$
-\log\beta_{N-1}
=\sum_{j=0}^{m-1}2^{m-j-1}L_j
\le\frac{100}{14}(16^m-2^m).
$$
所以
$$
\frac{\alpha_m}{\beta_{N-1}}
\le \exp\left(-\frac{90}{7}16^m\right).
\tag{4.5}
$$
这足以使 (1.6) 的显式 $\varepsilon_m$ 趋零。没有在极限中忽略有限头条件数；该条件数正是已计入的 $\beta_{N-1}^{-1}$。

## 5. 同一输入上的有限头与平均，统一成本恰为 $\|X\|$

采用 [负幂与共轭附录](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 的记号：
$$
\mathcal D_A=\{T:\|A^\ell Tf\|\le C\|A^\ell f\|
\text{ 对全部 }\ell\ge1,f\in H\},\qquad c_A(T)=\inf C,
$$
以及 $\Phi(T)=AT A^{-1}$ 的有界延拓。对本原算子已有
$$
\|T\|\le c_A(T),\qquad c_A(\Phi^q(T))=c_A(T)
\quad(q\in\mathbb Z).
\tag{5.1}
$$
第一式也可直接由 $A^{2^j}/\beta_{2^j}$ 对每个固定输入的范数极限 $\|f\|/\sqrt2$ 得到。若 $T$ 与 $A$ 交换，则反向不等式由交换关系立得，因此
$$
c_A(T)=\|T\|\qquad(T\in\{A\}').
\tag{5.2}
$$

对低 $\ell$ 位的下三角矩阵提升 $B$，令
$$
\Pi_\ell(B)=2^{-\ell}\sum_{q=0}^{2^\ell-1}\Phi^q(B).
\tag{5.3}
$$
[有限平均及无损成本附录](R12-appendix-finite-conjugation-average-and-lossless-polynomial-head-cost.md) 已证明，对任意固定有限多项式 $p(z)=\sum_{d=0}^D a_dz^d$，只要 $M=2^\ell>D$，就有
$$
c_A(p(A_\ell))\le\|p(A)\|,
\tag{5.4}
$$
$$
\Pi_\ell(p(A_\ell))
=\sum_{d=0}^D\left(1-\frac dM\right)a_dA^d.
\tag{5.5}
$$
(5.4) 使用的 $J_M$ 始终是原加权 nilpotent 头。其依据是有限头精确成本公式，加上将所有平移权重头压缩到原 $p(A)$ 的细圆柱子空间；压缩圆柱的模数选为严格大于 $M-1+D$，所以高次幂没有回返造成的额外项。

现取 (1.9) 的 $q_m(z)=\sum_{d=0}^{D_m}a_{m,d}z^d$。逐个 $m$ 选择足够大的 $\ell_m$，使 $2^{\ell_m}>D_m$，并且
$$
\alpha_{\ell_m}\sum_{d=1}^{D_m}
d|a_{m,d}|\alpha_0^{d-1}\longrightarrow0,\qquad
2^{-\ell_m}\sum_{d=1}^{D_m}d|a_{m,d}|\beta_d\longrightarrow0.
\tag{5.6}
$$
例如要求这两项都不超过 $1/m$ 即可；每次只有一个固定的有限多项式，所以这样的选择总能做到。

令
$$
C_m=q_m(A_{\ell_m}).
$$
则由 (5.4)、(1.9)，逐项有
$$
\boxed{\ c_A(C_m)\le\|X\|.\ }
\tag{5.7}
$$
由幂差估计和 (5.5)–(5.6)，
$$
\|C_m-q_m(A)\|\longrightarrow0,\qquad
\|\Pi_{\ell_m}(C_m)-q_m(A)\|\longrightarrow0.
\tag{5.8}
$$
于是
$$
\boxed{\ C_m\xrightarrow{\rm SOT}X,\qquad
\Pi_{\ell_m}(C_m)\xrightarrow{\rm SOT}X,\qquad
\|C_m-\Pi_{\ell_m}(C_m)\|\longrightarrow0.\ }
\tag{5.9}
$$
因此，对任意预先给定的有限组实际输入 $f_1,\ldots,f_k$，两个算子序列在完全相同的每个 $f_i$ 上都趋于 $Xf_i$。同时
$$
\|[A,C_m]\|\le
2\|A\|\,\|C_m-q_m(A)\|\longrightarrow0.
\tag{5.10}
$$
这里没有从任意强稠密序列推出平均自动保输入，而是用 (5.8) 的算子范数误差直接保证两者同输入逼近。

统一成本 $\|X\|$ 是最优的：若任意 $T_m\in\mathcal D_A$ 强趋 $X$，且 $c_A(T_m)\le C$ 对全部 $m$ 成立，那么 (5.1) 和强极限给 $\|X\|\le C$。

## 6. 准确边界

本稿对完整原 Haar 交换子成立，而非仅 UHF 部分、有限 chaos、有限柱乘子或抽象边界模型。新结论不要求 R88 的 $\rho$ 小量；它直接使用原权重的跨头块及 $\alpha_m/\beta_{2^m-1}\to0$。

同样的结论尚未在本稿中对任意 $X\in\mathcal D_A$ 证明；(3.5) 是交换性提供的实质约束。这里也没有证明 $c_A(C_m-\Pi_{\ell_m}(C_m))\to0$，只证明其算子范数趋零。统一成本族已有的非 localizing 结论、非零紧交换子不存在的结论仍适用；收缩逼近自身不产生新的紧算子或普通不变子空间。
