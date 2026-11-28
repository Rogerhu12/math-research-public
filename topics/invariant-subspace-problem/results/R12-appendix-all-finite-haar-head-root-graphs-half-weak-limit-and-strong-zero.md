# 全部原 Haar 有限头平方根图的半弱极限与强图零

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

接 [精确有限头吸收与临界 pair](R12-appendix-exact-haar-head-absorption-and-critical-root-graph-pair.md)。本篇研究完整有限 pair 不断吸收后的实际根图，而非仅比较相同模长正负闭合的两个根图。

## 1. 定理与准确范围

固定原尾 $C=A^{(m_0)}$，令 $P_L$ 为前 $L$ 位柱函数投影，$N=2^L$，

$$
C_L=P_LCP_L=J_L+\mu_LE_L.
$$

对每个 $L$，任意选择一个有限矩阵平方根 $S_L^2=C_L$，允许分支随 $L$ 任意变化。令 $\Pi_L$ 为
$\Gamma S_L=\{(S_Lx,x):x\in P_LH\}$ 在 $H\oplus H$ 中的正交投影，并在 $(P_LH\oplus P_LH)^\perp$ 上延零。

则对全部这些选择统一成立：

$$
\boxed{\quad \Pi_L\xrightarrow{\rm WOT}\frac12I.\quad}
\tag{1.1}
$$

更准确地，存在只依赖原物理权、与根分支无关的柱乘法投影 $F_L$，使

$$
(\Pi_L-F_L)\xi\longrightarrow0\quad(\xi\in H\oplus H),
\qquad F_L\xrightarrow{\rm WOT}\frac12I.
\tag{1.2}
$$

因此若 $\xi_L\in\Gamma S_L$ 且 $\xi_L\to\xi$ 于范数，则 $\xi=0$。结论也适用于任意趋于无穷的高度子列。

同样的结论适用于前文 $D^{[L]}$ 的全部直和根：任意选择其已吸收头根及各未吸收 Walsh 块根，所得全空间闭根图投影仍满足 (1.1)–(1.2)，任意强收敛的移动图向量仍只能趋于零。

这关闭的是这些具体有限吸收图的强图极限。没有排除原 $C$ 的其他非块对角闭根或未知旗商来源。

## 2. 全根分支对应的 Fourier 子矩阵全部非奇异

考虑有限 companion

$$
\mathcal B_L=\begin{pmatrix}0&C_L\\I&0\end{pmatrix}
$$

的交错基
$c_{2k}=(e_k,0)$、$c_{2k+1}=(0,e_k)$。它是长度 $2N$ 的完整正加权循环：偶步权为 $1$，奇步为原低头权，最后闭合为 $\mu_L$。

写 $\beta_{L,k}=\prod_{j=1}^k a_{v_2(j)}$、$\beta_L=\beta_{L,N-1}$、
$r_L=(\mu_L\beta_L)^{1/N}$。其对角平衡权为

$$
w_{2k}=\frac{\beta_{L,k}}{r_L^k},\qquad
w_{2k+1}=\frac{\beta_{L,k}}{r_L^{k+1/2}}.
\tag{2.1}
$$

于是 $\mathcal B_L=\sqrt{r_L}\,W_LU_{2N}W_L^{-1}$，$W_L=\operatorname{diag}(w_j)$，$U_{2N}$ 为酉循环移位。

$C_L$ 简单谱迫任意 $S_L$ 与它同时对角化。故其根图恰由 $W_L$ 乘以 $2N$ 阶 Fourier 矩阵的 $N$ 个列所张成；列指标集合 $\mathcal S$ 从每一对 $\{j,j+N\}$ 中恰选一个。特别 $\mathcal S$ 在模 $N$ 的每类中恰有一个元素。

这一列选择使任意 $N$ 行子矩阵都非奇异。它是 Alexeev–Cahill–Mixon 的 prime-power full-spark 定理的一个特殊情形；参见作者公开原文 [*Full spark frames*](https://borisalexeev.com/pdf/spark.pdf)，Theorem 9。
下面给出本篇所需情形的独立奇偶证明。

写 $s_j=j+N\varepsilon_j$，$0\le j<N$、$\varepsilon_j\in\{0,1\}$。广义 Vandermonde 行列式

$$
\det(z_k^{s_j})_{0\le j,k<N}
=P(z_0,\ldots,z_{N-1})\prod_{i<j}(z_j-z_i)
$$

中 $P$ 为整数系数多项式，合流极限给

$$
P(1,\ldots,1)
=\frac{\prod_{i<j}(s_j-s_i)}{\prod_{j=0}^{N-1}j!}\in\mathbb Z.
$$

因 $v_2(s_j-s_i)=v_2(j-i)$，此整数为奇数。令 $\zeta=e^{2\pi i/(2N)}$。在
$\mathbb Z[\zeta]/(1-\zeta)\cong\mathbb F_2$ 中，所有 $\zeta^k$ 都变为 $1$，所以 $P$ 在任何 $N$ 个不同 $2N$ 次单位根上的值都非零；Vandermonde 因子也非零，证毕。

任意这样的未归一 Fourier 子式 $\Delta$ 是次数至多 $N$ 的非零代数整数，全部共轭的 Hadamard 上界为 $N^{N/2}$。代数范数给

$$
|\Delta|\ge N^{-N(N-1)/2}.
\tag{2.2}
$$

因此对任意 $N$ 行集合 $I$，若 $F_I$ 为所选列在这些行上的方阵、$F_{I^c}$ 为剩余行，则可统一取

$$
\|F_{I^c}F_I^{-1}\|\le C_N,
\qquad C_N=N^{(N^2+3)/2}.
\tag{2.3}
$$

这里的费用含全部根分支、全部行选择；没有用一个特殊连续行 Vandermonde 代替中位权行。

## 3. 原物理 balance 权的中位分布

原前缀反转给

$$
w_jw_{2N-1-j}=\frac{\sqrt{r_L}}{\mu_L}.
$$

令

$$
h_L=\frac12\log\frac{\sqrt{r_L}}{\mu_L}.
$$

因此权按中位 $e^{h_L}$ 成对对称。选择 $I_L$ 为 $N$ 个最大权的行；若有中位相等权，成对各选一个。令 $F_L$ 为这一选择在两个原物理分量上的柱乘法投影。

下面证明中位带在每个固定低柱向量上的质量消失，且所选半边的条件 Haar 质量趋于 $1/2$。

写 $k=\sum_{j=0}^{L-1}b_j2^j$。ruler 前缀的实际二进分块给

$$
-\log\beta_{L,k}=\sum_{j=0}^{L-1}b_jd_j,\qquad
d_j=-\log(a_j\beta_j).
\tag{3.1}
$$

直接代入原 $\alpha$，并使用前文已证明的 $r_L$ 式，得

$$
d_j=100\,16^{m_0+j}
+O_{m_0}(8^j+(j+1)2^j),
$$

$$
-\log r_L=100\,16^{m_0}8^L
+O_{m_0}(4^L+L+1).
$$

故对全部 $k$、两个交错分量 $\varepsilon\in\{0,1\}$，一致有

$$
\frac{\log w_{2k+\varepsilon}-h_L}{100\,16^{m_0+L}}
=
\sum_{\ell=1}^{L}
\left(b_{L-\ell}-\frac12\right)
(2^{-\ell}-16^{-\ell})
+O_{m_0}(2^{-L}).
\tag{3.2}
$$

注意这是反向的高位序列，不是一个固定低位支集。

令独立公平 Bernoulli 变量为 $B_\ell$，并置

$$
X=\sum_{\ell\ge1}(B_\ell-\tfrac12)(2^{-\ell}-16^{-\ell}).
\tag{3.3}
$$

$X$ 对称且无原子。无原子性可直接证明：固定尾变量，前 $r$ 个正系数的同一和值所对应的子集构成反链，因此其个数至多
$\binom r{\lfloor r/2\rfloor}$。这个反链界由随机排列的最大链至多遇到一个成员立即得到。条件点概率至多
$2^{-r}\binom r{\lfloor r/2\rfloor}\to0$；再对尾积分，得到无原子性。故 $\Pr(X>0)=\Pr(X<0)=1/2$。

若固定任意 $q$ 个原低位 $b_0,\ldots,b_{q-1}$，它们在 (3.2) 中只占最后 $q$ 项，总影响趋于零。其余公平位仍收敛到 (3.3)。因此在每个固定低位柱条件下，(3.2) 的正半边概率趋于 $1/2$，宽度任意趋零的中位带概率趋于零。由有限柱函数稠密，

$$
F_L\xrightarrow{\rm WOT}\tfrac12I.
\tag{3.4}
$$

## 4. 全部根图在固定来源上逼近同一物理半质量旗

取实际对数带宽

$$
b_L=\frac{100\,16^{m_0+L}}{L}\qquad(L\ge1).
$$

由 $N=2^L$ 及 (2.3)，

$$
\eta_L=C_Ne^{-b_L}\longrightarrow0.
\tag{4.1}
$$

令 $T_L$ 为物理中位带
$|\log w_j-h_L|\le b_L$ 的柱投影。由 (3.2)–(3.3)，对每个固定柱向量 $\xi$，

$$
\|T_L\xi\|\longrightarrow0.
\tag{4.2}
$$

按 $I_L^c,I_L$ 排行，原根图可写成一个真正的有限图

$$
\operatorname{Ran}
\begin{pmatrix}L_L\\I\end{pmatrix},
\qquad
L_L=W_{I_L^c}F_{I_L^c}F_{I_L}^{-1}W_{I_L}^{-1}.
$$

对于低于中位带的全部行，(2.3) 给对应行算子范数至多 $\eta_L$；对于高于中位带的全部列，同理给对应列算子范数至多 $\eta_L$。前者说明根图向量在远低权坐标的分量至多 $\eta_L$ 倍全范数；后者说明每个远高权向量到根图的距离至多 $\eta_L$ 倍原范数。

所以对任意固定柱向量 $\xi$，

$$
\|(\Pi_L-F_L)\xi\|
\le\sqrt2\,\eta_L\|\xi\|+2\|T_L\xi\|
\longrightarrow0.
\tag{4.3}
$$

整个估计与根分支无关。$\Pi_L,F_L$ 都是压缩，故由稠密性延伸到全部 $H\oplus H$。这证明 (1.2)，再由 (3.4) 得 (1.1)。

这里没有声称整个有限根图在算子范数下接近一个单独最高位支集投影；原权在中间存在进位跳变，(3.2) 的完整中位分布是必要的。

## 5. 真正的强图结论与有限吸收范围

设 $\xi_L\in\Gamma S_L$、$\xi_L\to\xi$。则

$$
\|(I-\Pi_L)\xi\|\le\|\xi-\xi_L\|\to0.
$$

另一方面，由 (1.1) 与投影恒等式，

$$
\|(I-\Pi_L)\xi\|^2
=\|\xi\|^2-\langle\Pi_L\xi,\xi\rangle
\longrightarrow\tfrac12\|\xi\|^2.
$$

故 $\xi=0$。这已允许两个图坐标都随高度变化，不是固定输入发散的较弱陈述。

对 $D^{[L]}$ 的全域直和根，其图投影在 $P_LH\oplus P_LH$ 上就是本篇 $\Pi_L$；余下根图投影作用于固定 $\xi$ 的范数不超过
$\|((I-P_L)\oplus(I-P_L))\xi\|\to0$。所以所有未吸收尾分支任意变化也不改变结论。

特别，这些投影没有任何强收敛子列；任意选择分支后的逐层投影变化不可能在算子范数中绝对可和，否则强极限应为投影，与 (1.1) 矛盾。

原 $D^{[L]}\to C$ 的迹范数收敛与每个高度根的完整平方关系仍然成立。本篇表明这条有限吸收路线尚不能提供任何非零强图源。原非块对角非局部根域、未知原不变旗及其他未登记正向来源，仍须继续研究。
