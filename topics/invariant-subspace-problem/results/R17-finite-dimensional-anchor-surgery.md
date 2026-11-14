# R17：有限维锚点修改的 Schur 补及精确缺陷代价

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94；并行推导：general_routes。

**状态：已证明的中间结论。** 对一般有界算子的近不变正交投影，计算固定有限维空间的删除或加入对弱极限和不变性缺陷的影响。单射的正弱极限下，删除固定锚点保持缺陷趋零，当且仅当已经有相应的不变性。本结果没有排除变化锚点或一般非支集方法，未解决 ISP，不主张文献新颖性。

## 1. 删除有限维空间：精确 Schur 补与精确缺陷极限

设 $P_n$ 是正交投影，

$$P_n\longrightarrow P\quad\text{于 WOT},\qquad
\varepsilon_n=\|(I-P_n)TP_n\|\longrightarrow0.\tag{1.1}$$

令 $E\subset H$ 为一个固定非零有限维子空间，$J:E\hookrightarrow H$ 为自然等距嵌入。假设

$$G=J^*PJ>0\quad\text{在 }E\text{ 上正定}.\tag{1.2}$$

考察强行删去 $E$ 的操作

$$\operatorname{Ran}Q_n=\operatorname{Ran}P_n\cap E^\perp,$$

其中 $Q_n$ 为该闭子空间的正交投影。它确实制造了固定非零核 $E\subset\ker Q_n$；问题是这一操作是否保留缺陷趋零。

### 命题 1：极限与缺陷的完整公式

对充分大的 $n$，令 $G_n=J^*P_nJ$，则 $G_n>0$，并有

$$
Q_n=P_n-P_nJG_n^{-1}J^*P_n.
\tag{1.3}
$$

其 WOT 极限为

$$Q=P-PJG^{-1}J^*P.\tag{1.4}$$

而调整后不变性缺陷满足精确极限

$$
\lim_{n\to\infty}\|(I-Q_n)TQ_n\|^2
=\left\|G^{-1/2}J^*TQT^*JG^{-1/2}\right\|.
\tag{1.5}
$$

**证明。** 有限维性使 $G_n\to G$ 于范数，故充分大时正定，且逆及逆平方根范数收敛。定义

$$V_n=P_nJG_n^{-1/2}:E\to H.$$

因为 $V_n^*V_n=I_E$，$V_n$ 等距，其值域为 $P_nE$。因此 $R_n=V_nV_n^*=P_nJG_n^{-1}J^*P_n$ 是投影到 $P_nE$ 的正交投影，且 $R_n\le P_n$。在 $\operatorname{Ran}P_n$ 中，向量与 $P_nE$ 正交当且仅当与 $E$ 正交，证明 (1.3)。

对固定 $x,y\in H$，有限维坐标 $J^*P_nx,J^*P_ny$ 分别按范数收敛于 $J^*Px,J^*Py$。因此 $\langle R_nx,y\rangle$ 收敛于 $\langle PJG^{-1}J^*Px,y\rangle$，得到 (1.4)。

为证明缺陷公式，利用 $Q_n\le P_n$ 和 $I-Q_n=(I-P_n)+R_n$，有

$$
(I-Q_n)TQ_n=(I-P_n)TQ_n+R_nTQ_n.
$$

第一项的范数至多 $\varepsilon_n$。由于 $V_n$ 等距，

$$\|R_nTQ_n\|=\|G_n^{-1/2}J^*P_nTQ_n\|.$$

而

$$
\|G_n^{-1/2}J^*P_nTQ_n-G_n^{-1/2}J^*TQ_n\|
\le\|G_n^{-1/2}\|\varepsilon_n\longrightarrow0.
$$

故调整后缺陷的范数与 $\|B_n\|$ 之差趋零，其中 $B_n=G_n^{-1/2}J^*TQ_n$。由于 $Q_n$ 是投影，

$$
B_nB_n^*=G_n^{-1/2}J^*TQ_nT^*JG_n^{-1/2}.
$$

右边是作用在固定有限维 $E$ 上的矩阵；由 $Q_n\to Q$ 于 WOT 及 $G_n^{-1/2}\to G^{-1/2}$ 于范数，该矩阵按范数收敛于 (1.5) 中的矩阵。取范数并使用 $\|B_n\|^2=\|B_nB_n^*\|$，便得到 (1.5)。证毕。

### 推论 1.1：标量极限下的代价与标量无关

若 $P=\alpha I$，其中 $0<\alpha<1$，则

$$Q=\alpha P_{E^\perp},$$

且

$$
\lim_n\|(I-Q_n)TQ_n\|
=\|P_E T P_{E^\perp}\|.
\tag{1.6}
$$

特别地，要使调整后的缺陷仍趋零，必须并且只须 $E^\perp$ **本来就已经是** $T$-不变子空间。把 $\alpha$ 选得很小并不降低 (1.6) 的极限代价。

**证明。** (1.2) 给出 $G=\alpha I_E$。把 $P$、$G$ 代入 (1.4)、(1.5)，标量 $\alpha$ 约去，即得 (1.6)。右端等于零当且仅当 $P_ETx=0$ 对全部 $x\in E^\perp$ 成立。证毕。

### 推论 1.2：非标量而单射的极限也不能绕过此障碍

若 $P$ 单射，则对每个有限维 $E$ 自动满足 (1.2)，并且 (1.4) 的 $Q$ 满足

$$\ker Q=E.\tag{1.7}$$

因此 (1.5) 的极限为零当且仅当 $T^*E\subset E$，亦即 $E^\perp$ 已经不变。

**证明。** 令 $W=P^{1/2}JG^{-1/2}$，则 $W^*W=I_E$，并且

$$Q=P^{1/2}(I-WW^*)P^{1/2}.$$

若 $Qx=0$，则 $(I-WW^*)P^{1/2}x=0$，所以 $P^{1/2}x\in P^{1/2}E$。$P^{1/2}$ 单射，故 $x\in E$。反向包含由公式直接成立，得到 (1.7)。最后，(1.5) 的右边为零当且仅当 $Q^{1/2}T^*J=0$，由 (1.7) 等价于 $T^*E\subset E$。证毕。

### 推论 1.3：强行加入有限维空间的对偶结论

在 $P=\alpha I$、$0<\alpha<1$ 的情形，令 $\widetilde Q_n$ 投影到 $\operatorname{Ran}P_n+E$。有限维增广保持该和闭，且

$$
\widetilde Q_n\longrightarrow P_E+\alpha P_{E^\perp}\quad\text{于 WOT},
$$

$$
\lim_n\|(I-\widetilde Q_n)T\widetilde Q_n\|
=\|P_{E^\perp}TP_E\|.
\tag{1.8}
$$

**证明。** $I-\widetilde Q_n$ 投影到 $\operatorname{Ran}(I-P_n)\cap E^\perp$。对 $T^*$、$I-P_n$ 应用命题 1 和推论 1.1，再取伴随，即得结论。证毕。

因此从标量 WOT 极限出发，无论用固定有限维删去或加入来制造 $0$ 或 $1$ 的特征空间，都需要事先控制一个真不变性条件。这里排除的是这一整类具体手术，**没有排除所有非支集投影方法**，也没有排除随 $n$ 变化或无穷维的锚点构造。

