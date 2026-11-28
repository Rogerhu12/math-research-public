# 原 Haar 有限头的精确吸收、完整临界 pair 与根图交叉来源

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本文接 [原 Walsh 全块表示](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md) 与 [有界图角度来源](R12-appendix-actual-walsh-graph-coordinates-and-small-trace-class-angle-solution.md)。原尾仍是 $C=A^{(m_0)}$，$a_j=\alpha_{m_0+j}$。这里只作真实有限头的精确吸收；不把有限根或迹范数收敛提升为无限闭图相容。

## 1. 任意固定头的完整吸收

取 $L\ge0$，$N=2^L$。将原常数块及 $Q_0,\ldots,Q_{L-1}$ 合并成真正的 $P_LH$，在其低 $L$ 位归一整数柱基上写

$$
D_L^+=P_LCP_L=J_L+\mu_L E_L,\qquad
E_L=u_L^+ (v_L^+)^*,
\tag{1.1}
$$

其中 $J_L$ 是原低头移位、$u_L^+=e_0^{(L)}$、$v_L^+=e_{N-1}^{(L)}$。$L=0$ 时 $J_0=0$，所以 (1.1) 是常数线上的 $\mu_0$。

所有剩余 $Q_m$，$m\ge L$，仍保原负闭合循环块
$D_m=J_m-\mu_m u_mv_m^*$。令

$$
D^{[L]}=D_L^+\oplus\bigoplus_{m\ge L}D_m,\qquad
K^{[L]}=C-D^{[L]}.
$$

头与每个尾块之间的实际源准确为

$$
K^{[L]}_{P_L,m}
=2^{-(m-L)/2}\delta_m\,u_L^+v_m^*,
\qquad
K^{[L]}_{m,P_L}
=-2^{-(m-L)/2}\delta_m\,u_m(v_L^+)^*.
\tag{1.2}
$$

其余不同 $m,n\ge L$ 的块仍为原
$2^{-|m-n|/2}\delta_{\max(m,n)}u_mv_n^*$。没有新的对角残项。

证明 (1.2) 只需原有限 Walsh 展开

$$
e_0^{(L)}
=2^{-L/2}\Omega+\sum_{j=0}^{L-1}2^{-(L-j)/2}u_j,
\qquad
e_{N-1}^{(L)}
=2^{-L/2}\Omega-\sum_{j=0}^{L-1}2^{-(L-j)/2}v_j.
$$

因此同一完整秩一和给

$$
\boxed{\quad
\|K^{[L]}\|_1
\le2(1+\sqrt2)\sum_{m\ge L}\delta_m
\longrightarrow0.
\quad}
\tag{1.3}
$$

任取 $D_L^+$ 的有限矩阵平方根及每个剩余 $D_m$ 的根，其直和仍是 $D^{[L]}$ 的稠密闭稳定根，定义域为原整块平方和域。此处只改变了有限头；$D^{[L]}\to C$ 甚至在迹范数中成立，但尚未给这些根的图收敛。

## 2. 第一个未吸收 pair 就是真正的下一头

将 $P_LH$ 与 $Q_LH$ 通过相同低头柱基识别为两个 $\mathbb C^N$。记

$$
D_+=J_L+\mu_LE_L,\qquad
D_-=J_L-\mu_LE_L,\qquad
\delta=\delta_L,\quad\mu=\mu_L.
$$

原 $P_{L+1}CP_{L+1}$ 在这两个块上的完整矩阵为

$$
\mathcal C_L=
\begin{pmatrix}
D_+&\delta E_L\\
-\delta E_L&D_-
\end{pmatrix}.
\tag{2.1}
$$

即

$$
\mathcal C_L
=J_L\otimes I_2+
E_L\otimes
\begin{pmatrix}\mu&\delta\\-\delta&-\mu\end{pmatrix},
$$

这里张量次序可按原低头/尾位作固定置换。尾位 Hadamard 变换将最后的真实 $2\times2$ 矩阵变为

$$
\begin{pmatrix}0&\mu_{L+1}\\a_L&0\end{pmatrix},
\tag{2.2}
$$

因为 $\mu+\delta=a_L$、$\mu-\delta=\mu_{L+1}$。所以 (2.1) 酉等价于长度 $2N$ 的原下一头循环移位：所有内部权均是原权，最后闭合为 $+\mu_{L+1}$。

特别该有限 pair 的完整平方根确实存在，可在其 $2N$ 个互异非零特征值上任意取平方根并作有限插值。这是在原 pair 上精确解平方关系，不是忽略 $\delta E_L$ 的线性近似。尚未声称其图必在任意旧根图的同一个有界 Riccati 坐标图内。

## 3. 临界 pair 的全部线性来源由一个真实根图角精确决定

任取 $R_+^2=D_+$、$R_-^2=D_-$。两平方谱分别满足
$z^N=+\mu\beta_L$ 与 $z^N=-\mu\beta_L$，互不相交，故相应 Sylvester 方程唯一。

关键完整身份为

$$
R_-(R_+-R_-)+(R_+-R_-)R_+
=D_+-D_-=2\mu E_L.
\tag{3.1}
$$

因此原负向来源的有限解恰是

$$
R_-X_{-+}+X_{-+}R_+=-\delta E_L,
\qquad
X_{-+}=-\frac{\delta}{2\mu}(R_+-R_-).
\tag{3.2}
$$

反向来源同理为
$X_{+-}=+\frac{\delta}{2\mu}(R_+-R_-)$。

定义各自真实缺陷算子

$$
G_\pm=(I+R_\pm^*R_\pm)^{-1/2},\quad
H_\pm=(I+R_\pm R_\pm^*)^{-1/2},\quad
V_\pm=R_\pm G_\pm.
$$

则图角度未知量准确为

$$
\boxed{\quad
Y_{-+}
=-\frac{\delta}{2\mu}
\left(H_-V_+-V_-G_+\right).
\quad}
\tag{3.3}
$$

括号是旧负根图的正交补等距列与正根图等距列的完整交叉 Gram：

$$
\begin{pmatrix}H_-\\-V_-^*\end{pmatrix}^{\!*}
\begin{pmatrix}V_+\\G_+\end{pmatrix}.
$$

令 $\Pi_\pm$ 为这两个 $N$ 维根图的正交投影。有限等维主角恒等式给出精确范数

$$
\boxed{\quad
\|Y_{-+}\|
=\frac{\delta}{2\mu}\,\|\Pi_+-\Pi_-\|
\le\frac{\delta}{2\mu}<\frac12.
\quad}
\tag{3.4}
$$

所以完整临界 pair 的线性角度不是任意最坏 Sylvester 输入，而是同一正负闭合根图的实际角。$N$ 仅在迹范数估计中出现：
$\|Y_{-+}\|_1\le N\delta/(2\mu)$。

对 $L=0$，两根为 $\pm\sqrt{\mu_0}$ 与 $\pm i\sqrt{\mu_0}$，
$\|\Pi_+-\Pi_-\|=\sqrt{2\mu_0}/(1+\mu_0)$，(3.4) 准确回到前文单项
$\delta_0/[(1+\mu_0)\sqrt{2\mu_0}]$。

## 4. 仍须支付的实际无限接口

有限头可以逐次精确吸收，且每次都有 (2.1)–(2.2) 的真正非线性 pair 根。尚需证明所选根图在原 Haar 空间中有可用的无限相容，而不是只在每一个有限维空间存在。

临界比例 $\delta_L/\mu_L\to1$ 仅说明不能把该来源作为任意小相对扰动；它既没有证明根图角 $\|\Pi_+-\Pi_-\|$ 不可和，也没有证明可和。下一真实费用应来自 (3.3) 的同源图角、完整 pair 吸收后的投影变化或相应非线性乘积。本文不以移动临界层本身宣告整个正向构造失败。
