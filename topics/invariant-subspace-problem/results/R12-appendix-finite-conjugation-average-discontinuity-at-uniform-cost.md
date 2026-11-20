# R12 附录：有限共轭平均在统一成本球上的强不连续反例

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。高位块平均的强化由主会话提出，以下给出完整证明。

**状态：反例已证明。** 存在真实有限头下三角算子 $B_m$，满足
$$
\boxed{\ \|B_m\|\longrightarrow0,\qquad
c_A(B_m)\le2,\qquad
\Pi(B_m)\xrightarrow{\rm SOT}-\frac14 I.\ }
\tag{0.1}
$$
因此，有限共轭平均 $\Pi$ 即使限制在同一个有界 Deddens 成本球内，也不具有“输入算子范数收敛推出输出强收敛”的连续性。它不能仅靠全 Deddens 代数的收缩有限头强逼近自动延拓成保持同输入极限的平均。

反例仍在原 $L^2(\mathbb Z_2,\mu)$ Haar 模型上。它不影响对交换子专门选择的、已经同时控制原算子和平均误差的逼近构造。

## 1. 原算子与所用身份

采用 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R12](R12-normalized-powers-and-compact-commutant.md) 的原对象
$$
H=L^2(\mathbb Z_2,\mu),\qquad Af(y)=w(y)f(y-1),
$$
$$
w(0)=0,\qquad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=e^{-L_j},\quad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$
令
$$
\beta_n=\|A^n\|=\prod_{a=1}^n\alpha_{v_2(a)},\qquad
d_j=\beta_{2^j},\qquad N_j=\frac{A^{2^j}}{d_j}.
\tag{1.2}
$$
$E_j=e_{10}$ 表示仅作用于物理第 $j$ 位的 nilpotent。原模型的精确关系是
$$
\|N_j\|=\|E_j\|=1,\qquad
\|N_j-E_j\|=\eta_j=\frac{\alpha_{j+1}}{\alpha_j}
\le e^{-770\,16^j}.
\tag{1.3}
$$

$A_M$ 表示低 $M$ 位的原加权 nilpotent 头张量尾恒等；其矩阵在 $s\to s+1$ 上具有真实权重 $\alpha_{v_2(s+1)}$，最后一列为零。已有
$$
\|A-A_M\|=\alpha_M,\qquad \|A_M\|=\|A\|=\alpha_0<1.
\tag{1.4}
$$

Deddens 成本 $c_A$ 及整数共轭 $\Phi^q(X)=A^qXA^{-q}$ 的有界延拓使用 [负幂与共轭附录](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 的定义。它们满足
$$
\|X\|\le c_A(X),\qquad c_A(\Phi^q(X))=c_A(X).
\tag{1.5}
$$

## 2. 有限头平均的定义、相容性和多项式公式

若 $B$ 为低 $M$ 位的下三角矩阵提升，则
$$
\Phi^{2^M}(B)=B.
\tag{2.1}
$$
这是因为真实 $A^{2^M}$ 是 $I_{\rm head}$ 张量一个尾算子的标量倍数，因而与 $B$ 交换。定义
$$
\Pi(B)=2^{-M}\sum_{q=0}^{2^M-1}\Phi^q(B).
\tag{2.2}
$$
将 $B$ 提升到更细头后，旧周期整除新周期，所以 (2.2) 不依赖选用的足够细头。故 $\Pi$ 在全部有限头下三角核心上是良定义的线性映射，并有
$$
c_A(\Pi(B))\le c_A(B).
\tag{2.3}
$$

[有限平均与无损成本附录](R12-appendix-finite-conjugation-average-and-lossless-polynomial-head-cost.md) 给出两个原模型身份。对任意固定有限多项式 $p(z)=\sum_{d=0}^D a_dz^d$，只要 $2^M>D$，就有
$$
c_A(p(A_M))\le\|p(A)\|,
\tag{2.4}
$$
$$
\Pi(p(A_M))
=\sum_{d=0}^D\left(1-\frac d{2^M}\right)a_dA^d.
\tag{2.5}
$$
所有对象均为真实加权头；(2.4) 没有将 $J_{2^M}$ 替换为未加权 Jordan 块。

## 3. 单个位的相反平均

原归一化权重的精确无 carry 身份是
$$
E_j=\frac{A_{j+1}^{\,2^j}}{d_j}.
\tag{3.1}
$$
它把低 $j+1$ 位中第 $j$ 位为零的输入移到第 $j$ 位为一的相应输出；这 $2^j$ 步的权重乘积恰为 $d_j$。第 $j$ 位已为一的输入被 nilpotent 头截断。

由 (2.4)、(2.5)，
$$
c_A(E_j)\le1,\qquad
\boxed{\ \Pi(E_j)=\frac12N_j.\ }
\tag{3.2}
$$
事实上 $c_A(E_j)=1$，因为其普通范数为一。

对任意 $M>j$，再定义更细的真实头
$$
T_{j,M}=\frac{A_M^{\,2^j}}{d_j}.
\tag{3.3}
$$
同样有
$$
c_A(T_{j,M})\le1,\qquad
\boxed{\ \Pi(T_{j,M})=
\left(1-\frac{2^j}{2^M}\right)N_j.\ }
\tag{3.4}
$$
另一方面，幂差 telescoping 给
$$
\|T_{j,M}-N_j\|
\le\alpha_M\frac{2^j\alpha_0^{2^j-1}}{d_j}.
\tag{3.5}
$$
对每个固定 $j$，该误差随 $M\to\infty$ 趋零。

因此两个都非常接近 $N_j$ 的有限头算子，其平均却分别近于 $N_j/2$ 与 $N_j$。下面在高位上取块平均，把这个失真变为完整的强极限。

## 4. 高位块平均强趋 $I/2$

令 $m\ge1$，取
$$
I_m=\{m,m+1,\ldots,2m-1\},\qquad
\overline E_m=\frac1m\sum_{j\in I_m}E_j,\qquad
\overline N_m=\frac1m\sum_{j\in I_m}N_j.
\tag{4.1}
$$
对任何只依赖低 $k$ 位的有限柱输入 $f$，当 $m\ge k$ 时，
$$
E_jf=b_jf\qquad(j\in I_m),
$$
其中 $b_j\in\{0,1\}$ 是物理第 $j$ 位。相对于固定的低位输入，$(b_j-\tfrac12)$ 两两正交、均值为零、方差为 $1/4$。所以
$$
\left\|\left(\overline E_m-\frac12I\right)f\right\|^2
=\frac1{4m}\|f\|^2.
\tag{4.2}
$$
又 $\|\overline E_m\|\le1$，有限柱函数稠密，故
$$
\overline E_m\xrightarrow{\rm SOT}\frac12I.
\tag{4.3}
$$
由 (1.3)，
$$
\|\overline N_m-\overline E_m\|
\le\sup_{j\ge m}\eta_j\longrightarrow0.
\tag{4.4}
$$
从而
$$
\boxed{\ \overline N_m\xrightarrow{\rm SOT}\frac12I.\ }
\tag{4.5}
$$
这里使用的是原同一 Hilbert 空间上的独立高位计算，没有将弱收敛未经证明地升级为强收敛。

## 5. 选择同一个足够细头并完成反例

对每个 $m$，选整数 $M_m>2m$，足够大使
$$
\frac{\alpha_{M_m}}m
\sum_{j=m}^{2m-1}
\frac{2^j\alpha_0^{2^j-1}}{d_j}
\le2^{-m},
\tag{5.1}
$$
$$
2^{\,2m-1-M_m}\le2^{-m}.
\tag{5.2}
$$
每个 $m$ 的和只有有限项，且 $\alpha_M\to0$，因此这样的 $M_m$ 存在。两个要求均对这个共同头成立，不为不同求和项另换平均周期。

定义
$$
B_m=\frac1m\sum_{j=m}^{2m-1}\big(E_j-T_{j,M_m}\big).
\tag{5.3}
$$
每个 $E_j$ 都可提升到低 $M_m$ 位，因此 $B_m$ 是同一真实有限头的下三角矩阵。由 (3.2)、(3.4)，
$$
c_A(B_m)\le2.
\tag{5.4}
$$
由 (1.3)、(3.5)、(5.1)，
$$
\|B_m\|
\le\sup_{j\ge m}\eta_j+2^{-m}
\longrightarrow0.
\tag{5.5}
$$

利用平均的头相容性和 (3.2)、(3.4)，
$$
\begin{aligned}
\Pi(B_m)
&=\frac1m\sum_{j=m}^{2m-1}
\left[-\frac12+\frac{2^j}{2^{M_m}}\right]N_j\\
&=-\frac12\overline N_m+R_m,
\end{aligned}
\tag{5.6}
$$
其中
$$
\|R_m\|
\le\frac1m\sum_{j=m}^{2m-1}2^{j-M_m}
\le2^{\,2m-1-M_m}\le2^{-m}.
\tag{5.7}
$$
由 (4.5)，得到
$$
\Pi(B_m)\xrightarrow{\rm SOT}-\frac14I,
$$
完成 (0.1)。

若需要输出趋于恒等，可简单置 $D_m=-4B_m$，则
$$
\|D_m\|\to0,\qquad c_A(D_m)\le8,\qquad
\Pi(D_m)\xrightarrow{\rm SOT}I.
\tag{5.8}
$$
对每个非零固定输入 $f$，(0.1) 精确给出
$$
B_mf\longrightarrow0,\qquad
\Pi(B_m)f\longrightarrow-\frac14f.
\tag{5.9}
$$
所以失败发生在同一个实际输入上，无法用“各近似均具有统一成本”来消除。

## 6. 与收缩逼近结论的关系

$\Pi$ 对 Deddens 成本满足 (2.3)，但该成本拓扑不同于普通算子范数或强算子拓扑。本反例没有 $c_A(B_m)\to0$；实际上 (1.5)、(2.3) 和输出强极限推出
$$
\liminf_m c_A(B_m)\ge\frac14.
\tag{6.1}
$$
因此不与成本收缩性矛盾。

[全代数最优成本有限头逼近](R12-appendix-full-deddens-algebra-optimal-cost-finite-head-approximation.md) 允许对每个给定的 $X\in\mathcal D_A$，在同一个成本球内选择有限头强逼近。它没有规定这些有限头的平均极限。本稿证明，不能仅凭其强逼近和统一成本，自动补上该接口。

相反，[完整交换子的收缩逼近](R12-appendix-contractive-polynomial-density-of-full-haar-commutant.md) 先对一个真正交换子选择收缩多项式，再选择足够细头，使原算子及其平均都在算子范数中接近同一个多项式。那个额外的同目标误差估计仍然有效。

本稿没有产生非零紧交换子、localizing 的固定成本族或新的普通不变子空间。它准确关闭的是有限平均的自动连续化推理。
