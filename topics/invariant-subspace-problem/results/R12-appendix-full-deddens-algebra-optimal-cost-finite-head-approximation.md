# R12 附录：全 Deddens 代数的最优统一成本有限头逼近

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下全代数逼近、端点成本控制及有限输入刻画均已证明。** 对原 Haar 算子的任意 $X\in\mathcal D_A$，存在真实有限头下三角矩阵 $C_m$ 强趋 $X$，且逐项 $c_A(C_m)\le c_A(X)$。证明使用相同尾常向量的真实压缩：成本端点的两段分别由 $\Phi^q(X)$ 和 $\Phi^{q-2^m}(X)$ 实现。后一段需要已经证明的负幂域保持，不能由形式除法替代。

本稿加强 [收缩有限头核心附录](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md) 的普通算子范数强稠密性：现在对一个给定的实际 Deddens 算子，有限头逼近保持其最优统一 Deddens 成本。它不声称有限共轭平均对这种逼近连续，也不从该逼近推出 localizing 或普通不变子空间结论。

## 1. 原对象与已付接口

固定 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R12](R12-normalized-powers-and-compact-commutant.md) 的原算子
$$
H=L^2(\mathbb Z_2,\mu),\qquad Af(y)=w(y)f(y-1),
$$
$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\quad
\alpha_j=e^{-L_j},
$$
$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$
写
$$
\beta_0=1,\qquad \beta_n=\|A^n\|
=\prod_{a=1}^n\alpha_{v_2(a)}.
\tag{1.2}
$$
特别地 $0<\alpha_j\le\alpha_0=e^{-20}<1$。

定义
$$
\mathcal D_A=
\{X\in B(H):\|A^\ell Xf\|\le C\|A^\ell f\|
\text{ 对全部 }\ell\ge1,f\in H\},
$$
$$
c_A(X)=\inf\{C:\text{上述全部不等式成立}\}.
\tag{1.3}
$$
[负幂与共轭附录](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 已在这个原算子上证明：
$$
\|X\|\le c_A(X),
\tag{1.4}
$$
$$
X\operatorname{Ran}A^k\subseteq\operatorname{Ran}A^k,\qquad
\|A^{-k}XA^kf\|\le c_A(X)\|f\|,
\tag{1.5}
$$
以及
$$
\Phi^q(X)=A^qXA^{-q}
$$
在其原稠密定义域上的有界延拓构成 $\mathcal D_A$ 的整数作用，且
$$
c_A(\Phi^q(X))=c_A(X)\qquad(q\in\mathbb Z).
\tag{1.6}
$$
对 $q<0$，(1.5) 保证表达式有定义；(1.6) 不是未经证明地将正幂最优常数等同于独立的负幂最优常数。

对 $N=2^m$，用
$$
H\simeq\mathbb C^N\otimes L^2(\mathbb Z_2,\mu),\qquad
f\mapsto\big(N^{-1/2}f(r+Nz)\big)_{0\le r<N}
\tag{1.7}
$$
写算子块。尾常函数 $\mathbf1$ 的范数为一。定义
$$
b_{rs}^{(m)}=\langle X_{rs}\mathbf1,\mathbf1\rangle,\qquad
B_m(X)=\big(b_{rs}^{(m)}\mathbf1_{\{r\ge s\}}\big)_{r,s<N}
\otimes I_{\rm tail}.
\tag{1.8}
$$
置
$$
\delta_m=\frac{N\alpha_m}{\beta_{N-1}}.
\tag{1.9}
$$

**主定理。** 对任意 $X\in\mathcal D_A$，
$$
B_m(X)\xrightarrow{\rm SOT}X,\qquad
c_A(B_m(X))\le(1+2\delta_m)c_A(X),
\tag{1.10}
$$
且 $\delta_m\to0$。因此
$$
\boxed{\ C_m(X)=\frac{B_m(X)}{1+2\delta_m},\quad
c_A(C_m(X))\le c_A(X),\quad
C_m(X)\xrightarrow{\rm SOT}X.\ }
\tag{1.11}
$$
每个 $C_m$ 对 $X$ 线性，取值于有限维的真实有限头下三角空间。

## 2. 全 Deddens 代数的上三角块小量

在 (1.7) 下，
$$
A=J_N\otimes I+e_{0,N-1}\otimes B^{\rm tail}_m,\qquad
(B^{\rm tail}_mg)(z)=w(Nz)g(z-1),
$$
$$
\|B^{\rm tail}_m\|=\alpha_m,
\tag{2.1}
$$
其中 $J_Ne_s=\alpha_{v_2(s+1)}e_{s+1}$ 对 $s<N-1$ 成立，最后一列为零。

设 $Y\in\mathcal D_A$，$c=c_A(Y)$。取 $r<s<N$ 及任意尾输入 $g$，在 Deddens 不等式中使用
$$
n=N-s,\qquad f=e_s\otimes g.
$$
输入走 $n$ 步恰跨一次头边界，因此
$$
A^n(e_s\otimes g)
=\frac{\beta_{N-1}}{\beta_s}
e_0\otimes B^{\rm tail}_mg.
\tag{2.2}
$$
另一方面，$Y(e_s\otimes g)$ 的第 $r$ 分量经过这 $n$ 步不跨边界，到达 $d=N-s+r<N$，相应分量为
$$
\frac{\beta_d}{\beta_r}\,Y_{rs}g.
$$
不同头分量的输出头位置不同，所以该分量范数不超过全输出范数。故
$$
\|Y_{rs}g\|
\le c\alpha_m
\frac{\beta_r\beta_{N-1}}{\beta_s\beta_{N-s+r}}\|g\|.
$$
利用 $\beta_j$ 单调递减且不超过一，
$$
\boxed{\ \|Y_{rs}\|\le
c_A(Y)\frac{\alpha_m}{\beta_{N-1}}
\qquad(r<s).\ }
\tag{2.3}
$$
这对全部尾输入成立，特别适用于同一个尾常向量；并未更换源向量来取得上界。

令
$$
\mathcal T_m(X)=
\big(\langle X_{rs}\mathbf1,\mathbf1\rangle\big)_{r,s<N}
\otimes I_{\rm tail}.
$$
这是尾常向量压缩再提升，因而
$$
\|\mathcal T_m(X)\|\le\|X\|,\qquad
\mathcal T_m(X)\xrightarrow{\rm SOT}X.
\tag{2.4}
$$
后一式可在有限柱输入上直接检验：当输入只依赖低 $k$ 位、$m\ge k$ 时，左端作用等于 $Q_mXf$，其中 $Q_m$ 是低 $m$ 位条件期望投影，且 $Q_m\to I$ 强收敛。统一范数控制再推广到全 $H$。

由 (2.3) 及矩阵范数不超过 $N$ 倍最大元素绝对值，
$$
\|B_m(X)-\mathcal T_m(X)\|\le\delta_m c_A(X).
\tag{2.5}
$$

## 3. 有限头精确成本及两个端点

[有限头成本附录](R12-appendix-contractive-deddens-core-and-exact-finite-head-cost.md) 已证明：若 $B=(b_{rs})\otimes I_{\rm tail}$ 下三角，则 $B\in\mathcal D_A$，且
$$
c_A(B)=\max_{t\in\mathbb Z_2}\|K_B(t)\|,
$$
$$
K_B(t)_{rs}=
b_{rs}\frac{\beta_s}{\beta_r}
\prod_{a=s+1}^{r}w(t+a)\quad(r\ge s),\qquad
K_B(t)_{rs}=0\quad(r<s).
\tag{3.1}
$$
空乘积为一。

固定 $q=t\bmod N\in\{0,\ldots,N-1\}$。在 $w(t+1),\ldots,w(t+N-1)$ 中，至多一项的赋值达到 $m$。若 $q>0$，该项位于
$$
k=N-q,\qquad v=w(t+k)\in\{\alpha_m,\alpha_{m+1},\ldots,0\}.
\tag{3.2}
$$
其余权重均由低头数字决定。矩阵 $K_B(t)$ 关于 $v$ 仿射，矩阵范数为凸函数，所以其最大值由 $v=0$ 或 $v=\alpha_m$ 给出。端点零也由实际取值的极限达到。若 $q=0$，没有可变项，可将两个端点视为相同。因此 (3.1) 只需核查至多 $2N$ 个明确有限矩阵。

以下固定 $B=B_m(X)$，记 $c=c_A(X)$。

## 4. 零端点：两段各用一次没有 carry 的真实共轭

先设 $q>0$，$k=N-q$。当 $v=0$ 时，所有跨过 $k$ 的下三角元素消失，$K_B(q,0)$ 分为两个对角块。

若 $r,s<k$，$A^q$ 在这两个头位置上均不跨边界。真实块计算给
$$
(\Phi^q(X))_{r+q,s+q}
=\frac{\beta_{r+q}\beta_s}{\beta_r\beta_{s+q}}X_{rs}.
\tag{4.1}
$$
故对 $r\ge s$，其尾常向量压缩正是 $K_B(q,0)_{rs}$。

若 $r,s\ge k$，则改用负向 $k$ 步，两端同样不跨边界。由于 (1.5) 已保证负幂定义域保持，
$$
(\Phi^{-k}(X))_{r-k,s-k}
=\frac{\beta_{r-k}\beta_s}{\beta_r\beta_{s-k}}X_{rs}.
\tag{4.2}
$$
其尾常向量压缩在 $r\ge s$ 时也正是第二块的 $K_B(q,0)_{rs}$。

注意 (4.1)、(4.2) 的输入和压缩尾向量均为原来的 $\mathbf1$。没有将 $B^{\rm tail}_m\mathbf1$ 或其逆像替换成 $\mathbf1$，也没有假定 $X_{rs}$ 与尾算子交换。之所以可以保持这个输入，是两段分别选择了没有 carry 的方向。

令 $F_q$ 为上述两个压缩块的直和，并将其头指标移回 $0,\ldots,k-1$ 与 $k,\ldots,N-1$。由 (1.4)、(1.6)，
$$
\|F_q\|\le c.
\tag{4.3}
$$
$K_B(q,0)$ 就是 $F_q$ 各块的下三角部分。对 (4.1)、(4.2) 中的两个真实共轭应用 (2.3)，其被删除的上三角每个元素绝对值至多
$c\alpha_m/\beta_{N-1}$。于是
$$
\boxed{\ \|K_B(q,0)\|\le c(1+\delta_m).\ }
\tag{4.4}
$$
当 $q=0$ 时只需 $F_0=\mathcal T_m(X)$，同一估计直接成立。

## 5. 另一端点：跨段矩形的显式小量

从 $v=0$ 改为 $v=\alpha_m$，两段内部元素不变。只增加 $s<k\le r$ 的下三角矩形。对该矩形，
$$
|K_B(q,\alpha_m)_{rs}|
=|b_{rs}|\frac{\beta_s}{\beta_r}\,
\alpha_m
\prod_{\substack{s<a\le r\\a\ne k}}w(q+a).
\tag{5.1}
$$
乘积中各项不超过一，$|b_{rs}|\le\|X\|\le c$，而
$\beta_s/\beta_r\le1/\beta_{N-1}$。因此
$$
|K_B(q,\alpha_m)_{rs}|
\le c\frac{\alpha_m}{\beta_{N-1}}.
$$
矩形的矩阵范数至多 $\delta_m c$，结合 (4.4)，
$$
\|K_B(q,\alpha_m)\|\le c(1+2\delta_m).
\tag{5.2}
$$
由精确端点公式 (3.1)–(3.2)，得到 (1.10) 的成本估计。

最后，由原权重显式式子有
$$
20\,16^j\le L_j\le100\,16^j.
$$
精确赋值计数给
$$
-\log\beta_{2^m-1}
=\sum_{j=0}^{m-1}2^{m-j-1}L_j
\le\frac{100}{14}(16^m-2^m),
$$
从而
$$
\frac{\alpha_m}{\beta_{2^m-1}}
\le e^{-(90/7)16^m},\qquad
\delta_m\le 2^m e^{-(90/7)16^m}\longrightarrow0.
\tag{5.3}
$$
(2.4)–(2.5) 证明 $B_m(X)\to X$ 强收敛，再作 (1.11) 的标量归一化即得主定理。

## 6. 固定成本球的精确有限头闭包

令
$$
\mathcal K_C=\{X\in\mathcal D_A:c_A(X)\le C\},
$$
并令 $\mathcal L$ 为全部真实有限头下三角矩阵提升之并。则对每个 $C\ge0$，
$$
\boxed{\ \mathcal K_C=
\overline{\mathcal L\cap\mathcal K_C}^{\rm SOT}.\ }
\tag{6.1}
$$
正向包含由主定理；反向包含来自 Deddens 不等式对强极限的保持。这里保持的是同一个固定成本 $C$，不是依赖近似精度而增大的成本。

这还给出同输入插值的完整有限头化。固定任意有限组原空间向量
$f_1,\ldots,f_k$，定义
$$
\Gamma_C(f_1,\ldots,f_k)=
\{(Xf_1,\ldots,Xf_k):X\in\mathcal K_C\}\subset H^k.
\tag{6.2}
$$
由 $\|X\|\le C$，$\mathcal K_C$ 是算子范数球的子集。它也是 WOT 闭的：若 $X_i\to X$ 弱算子收敛，则对每个固定 $\ell,f$，
$A^\ell X_if$ 弱趋 $A^\ell Xf$，范数弱下半连续保留全部定义不等式。因此 $\mathcal K_C$ 是 WOT 紧凸集，$\Gamma_C$ 是 $H^k$ 中弱紧、从而范数闭的凸集。

结合 (6.1)，
$$
\boxed{\ 
\Gamma_C(f_1,\ldots,f_k)=
\overline{\{(Bf_1,\ldots,Bf_k):
B\in\mathcal L,\ c_A(B)\le C\}}^{\,\|\cdot\|_{H^k}}.
\ }
\tag{6.3}
$$
因此给定目标 $g_1,\ldots,g_k$，存在真正的 $X\in\mathcal D_A$ 满足
$c_A(X)\le C$ 且 $Xf_i=g_i$ 对全部 $i$ 成立，当且仅当：对每个 $\epsilon>0$，存在同一有限头下三角 $B$，成本仍不超过 $C$，且
$$
\sum_{i=1}^k\|Bf_i-g_i\|^2<\epsilon^2.
\tag{6.4}
$$
这些有限头问题的成本由至多 $2N$ 个矩阵范数约束准确给出；输入始终为原来的 $f_i$，并没有替换成它们的条件期望。

若精确有限输入插值的最小成本有限，该最小值也能达到。证明是取成本趋向下确界的实际插值算子，由统一范数界取 WOT 聚点，再用同样的弱闭性保留插值与最优成本。该存在性不意味着任意目标都具有有限成本。

## 7. 尚未付出的接口

主定理及 (6.3) 将任意既有 Deddens 插值的成本无损化为有限头凸约束。它们不提供对任意递推目标的统一可行成本；这一点仍须沿同一条实际输入序列另证。

尤其不能从 $B_m(X)\to X$ 强收敛及统一 $c_A$ 界，推出有限共轭平均 $\Pi_m(B_m(X))$ 也趋向所希望的输出。平均涉及随头深变化的共轭次数，不是一个已经证明连续的固定算子。对交换子的专门构造可以同时控制原算子及平均；一般有限头逼近不自动拥有该性质。
