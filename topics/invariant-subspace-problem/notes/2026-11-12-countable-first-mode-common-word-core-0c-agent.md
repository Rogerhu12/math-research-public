# 可数个实际一阶乘子的共同自然域与不变限制上的同时图逼近

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整接口，不编号研究记录。

本稿把有限模式正则化扩为一个固定可数族。每个正则子有界并与 $A$ 交换，同一族在 SOT 中趋于单位；每个正则子的范围同时落入全部有限 mixed-word 自然域。单个无限乘积的单射性或稠密像不在结论中。

## 1. 结论及所用实际输入

给定可数个 R125 的实际闭一阶
$$
X_\nu=c_\nu I+\sum_{j\ge0}a_j^{(\nu)}V_j,\qquad
a^{(\nu)}\in\ell^2,\qquad \nu\ge1.
$$
一个 word 是有序乘积 $w=X_{i_q}\cdots X_{i_1}$，使用逐步作用的真实自然域。空 word 为单位。记
$$
\mathscr D_\infty=\bigcap_{w\ {\rm finite}}\operatorname{Dom}w,
\qquad \mathfrak C=\{A\}'.
$$

**定理。** 存在非零收缩 $S_n\in\mathfrak C$，使
$$
S_n\longrightarrow I\quad{\rm SOT},\qquad
S_nH\subseteq\mathscr D_\infty,\qquad
wS_n\in\mathfrak C\cap B(H)
\tag{1.1}
$$
对每个 $n$ 和每个有限 word 成立。

因此，对任意闭 $A$ 不变子空间 $M$，
$$
\overline{\mathscr D_\infty\cap M}=M.
\tag{1.2}
$$
若 $x\in M$ 原本属于某个 word $w$ 的自然域，则同一族给
$$
S_nx\to x,\qquad wS_nx\to wx.
\tag{1.3}
$$
对有限组 words 是联合图逼近，对全部可数 words 是每个图半范数上的逼近。相同结论适用于有限矩阵放大后的闭不变限制。

证明只用以下已有实际输入：$\mathfrak C$ 交换且强闭；每个闭一阶与全部有界交换子真实域交换；有限柱是其通常伴随的图核心；非负系数一阶加适当实标量后为最大增生算子。这些分别由 R88、R125、R128 给出。

## 2. 正分量预解式与有限因子包

把每个系数列的实部、虚部分为正负四部分。所有所得非零非负 $\ell^2$ 列组成一个可数族。给对应正一阶加有限实常数，得到最大增生的 $Y_j$，使
$$
R_j(t)=(I+tY_j)^{-1}\in\mathfrak C,\qquad
\|R_j(t)\|\le1,\qquad
R_j(t)\xrightarrow[t\downarrow0]{\rm SOT}I.
\tag{2.1}
$$
所有预解式交换并保持每个闭 $A$ 不变子空间。每个 $X_\nu$ 在公共有限柱上是有限个 $Y_j$ 加标量单位的线性组合。

这里补齐真实域。若 $X_\nu$ 需要正分量 $Y_{j_1},\ldots,Y_{j_k}$，取任意正参数，置
$$
P=\prod_{l=1}^kR_{j_l}(t_l).
$$
域交换及预解式恒等式给
$$
PH\subseteq\bigcap_l\operatorname{Dom}Y_{j_l},\qquad
Y_{j_l}P=
\frac{I-R_{j_l}(t_l)}{t_l}
\prod_{h\ne l}R_{j_h}(t_h)\in\mathfrak C\cap B(H).
\tag{2.2}
$$
若 $y$ 属于这些正分量域，有限线性组合 $z$ 已在 $H$ 中定义。与有限柱 $v$ 配对，真实伴随核心给
$$
\langle z,v\rangle=\langle y,X_\nu^*v\rangle.
$$
该核心的通常伴随等于 $X_\nu$，故 $y\in\operatorname{Dom}X_\nu$ 且 $X_\nu y=z$。因此
$$
\boxed{PH\subseteq\operatorname{Dom}X_\nu,\qquad
X_\nu P\in\mathfrak C\cap B(H).}
\tag{2.3}
$$
有限族所需的正分量合并成一个包，便同时正则化整个有限族。参数不必相同。

## 3. 强收敛的无限乘积

取单位球中的可数稠密族 $(h_j)$，令 $h_1=1$。选择序列 $i_1,i_2,\ldots$，使每个所需正分量指标出现无穷多次。若全部 $X_\nu$ 都是常数，直接取 $S_n=I$；以下正分量列表非空。

对每个 $n,k\ge1$，由 (2.1) 选择 $t_{n,k}>0$，使
$$
\|(R_{i_k}(t_{n,k})-I)h_j\|
\le2^{-n-k}\qquad(1\le j\le n+k).
\tag{3.1}
$$
每次只有有限个强收敛条件。令
$$
P_{n,K}=\prod_{k=1}^KR_{i_k}(t_{n,k}).
$$
所有因子为收缩。对固定 $h_j$，当 $K_2>K_1$ 且 $n+K_1\ge j$ 时，望远镜求和给
$$
\|(P_{n,K_2}-P_{n,K_1})h_j\|
\le\sum_{k=K_1+1}^{K_2}2^{-n-k}.
\tag{3.2}
$$
故对每个 $n$，有限乘积强收敛到收缩 $S_n\in\mathfrak C$。

若 $j\le n$，全部因子都受 (3.1) 控制，因此
$$
\|(S_n-I)h_j\|\le2^{-n}.
\tag{3.3}
$$
稠密性与统一范数界给 $S_n\to I$ 强。又因 $h_1=1$，
$\|(S_n-I)1\|<1$，所以每个 $S_n\ne0$。

必须还保留有限因子剥离。对任意有限指标集 $F$，省去其中因子的其余乘积仍由 (3.2) 强收敛到某个收缩 $Q_{n,F}\in\mathfrak C$。交换性给准确式
$$
\boxed{
S_n=P_{n,F}Q_{n,F},\qquad
P_{n,F}=\prod_{k\in F}R_{i_k}(t_{n,k}).
}
\tag{3.4}
$$
没有对无限乘积取逆，也没有把所有因子同一时刻用于一个无穷无界乘法。

## 4. 全部有限 words 的实际域

固定长度 $q$ 的 word $w=X_{i_q}\cdots X_{i_1}$。每个正分量出现无穷多次，故可选 $q$ 个互不重叠的有限因子包 $P_1,\ldots,P_q$，每个包都包含该 word 所需的全部正分量。

由第2节，每个 $P_l$ 将全部 $H$ 送入所有这些 $X_{i_j}$ 的域，并使 $X_{i_j}P_l$ 成为有界交换子。由 (3.4)，
$$
S_n=P_1\cdots P_qQ,\qquad Q\in\mathfrak C,\quad\|Q\|\le1.
$$
逐次作用 word 时，每一步都保留一个尚未使用的包，作为下一步的全域正则子。已经产生的有界因子仍在交换代数中。真实域归纳遂给
$$
\boxed{
wS_n=(X_{i_q}P_q)\cdots(X_{i_1}P_1)Q
\in\mathfrak C\cap B(H).
}
\tag{4.1}
$$
同时每个中间值都在下一算子的域内。这证明 (1.1)，结论针对自然 word 域，不只是多项式的某个形式最大图域。

## 5. 不变限制与闭最大多项式

每个 $S_n$ 和 $wS_n$ 都保持任意闭 $A$ 不变子空间 $M$。因而
$$
S_nM\subseteq\mathscr D_\infty\cap M,\qquad
wS_nM\subseteq M.
$$
由强趋单位得到 (1.2)。

若 $x$ 本来属于 $w$ 的自然域，一阶与有界交换子的域交换逐次给
$$
wS_nx=S_nwx.
$$
于是 (1.3) 成立。各个自然 word 不必先被假定为闭算子。

对每个已经由 R186 构造的有限模式闭最大多项式 $P$，其与有界交换子的真实域交换也适用。$S_nH$ 位于其自然多项式域中，所以
$$
S_nx\to x,\qquad PS_nx=S_nPx\to Px
\qquad(x\in\operatorname{Dom}P).
$$
因此 $\mathscr D_\infty$ 是这些既有闭实现的共同图核心；在其不变限制上也成立。这不把原先未必闭的自然多项式直接宣布为闭算子。

有限放大 $I_d\otimes S_n$ 仍为收缩、仍强趋单位，且保持所有放大后的恒等式。因此同一族也给每个有限放大闭不变限制上的共同域密度与图逼近。

## 6. 不得外推的性质

本稿没有证明某个固定 $S_n$ 单射或值域稠密。使用的是整个族的强单位逼近。对每个非零 $M$，至少充分多的 $S_n|_M$ 非零，但这不意味着单个无限乘积在所有限制上都是 quasiaffinity。

如果原列表含有一个系数不在 $\ell^1$ 的一阶 $X_\nu$，则每个非零 $S_n$ 都在 UHF 之外：否则 (4.1) 给 $S_nX_\nu$ 在有限柱上的有界实现，与 R171 的非零 UHF 最高系数障碍矛盾。这与 R203 相容。

共同自然幂域不等于逐项系数部分和的收敛类。本稿没有证明
$$
\sum_{j<m}a_j^{(\nu)}V_jx\longrightarrow X_\nu x
$$
对全部共同域向量成立；也没有使有限柱条件期望保持未知 $M$。因此这里的密度不自动排除慢平方有界分支，更不解决负整数边界中标准右移逆域在核内的密度。

内部输入：R125 的实际一阶及伴随图核心，R128 的正分量最大增生预解式，R171 的 UHF 最高系数障碍，R186 的有限模式闭最大多项式图。无限乘积、有限因子剥离及全部 finite-word 自然域的证明均已在本文给出。
