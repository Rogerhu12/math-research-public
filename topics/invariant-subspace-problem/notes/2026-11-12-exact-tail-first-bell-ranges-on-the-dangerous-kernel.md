# 危险平方核上的准确尾像等式及尾投影闭像

日期：2026-11-12（UTC）。作者：kernel。
状态：完整短补充，接 R144 平方核附录与 R208 头图附录；不声称尾限制像已经稠密。

## 1. 原 Haar 核及真实单位

设
$$
u=a\chi_0+\sum_{j\ge1}a_j\chi_j,\qquad a\ne0,\qquad (a_j)\in\ell^2.
$$
此处保留危险点态平方识别所需的常数项 $a_*=0$。令
$$
X=X_u,\qquad
B_2=\sum_{j\ge0}a_j^2(I-V_j^2),\qquad
Y=(a^2I-B_2)^{1/2},\qquad\chi(Y)=a,
$$
并置
$$
M=\ker(X-Y).
$$
R144/R176 证明它就是危险点态平方的实际闭核；$M$ 闭、对全部有界交换子不变，
且 $M\subseteq\operatorname{Dom}X$、$X|_M=Y|_M$。

删去首物理位，写
$$
W=X_{\sum_{j\ge1}a_j\chi_j},\qquad
Z=\sum_{j\ge1}a_j^2(I-V_j^2).
$$
$W$ 按 $I_2\otimes W$ 作用于原空间，下文在原空间省略张量恒等符号。
完整自然域上 $X=aV_0+W$，因而 $M\subseteq\operatorname{Dom}W$ 且
$$
W_M:=W|_M=(Y-aV_0)|_M\in B(M).
\tag{1}
$$

$Y$、$V_0$ 都在实际范数代数 $\mathcal A$ 中，且交换。由
$$
Y^2-a^2V_0^2=-Z
$$
以及 $\chi(Y+aV_0)=2a\ne0$，
$$
J:=Y+aV_0,\qquad J^{-1}\in\mathcal A
\tag{2}
$$
均为真实有界算子。这里使用 $\mathcal A$ 的唯一字符结构及已经选定的全纯平方根，
没有以形式常数非零替代实际逆。

还要核对单位双向保持同一个 $M$。对 $R=J$ 或 $J^{-1}$，
真实第一阶域交换给 $R\operatorname{Dom}X\subseteq\operatorname{Dom}X$，
且 $XRf=RXf$；$R$ 与 $Y$ 交换。因此
$$
(X-Y)Rf=R(X-Y)f=0\qquad(f\in M).
$$
所以 $JM\subseteq M$、$J^{-1}M\subseteq M$，从两向包含得到
$$
JM=J^{-1}M=M.
\tag{3}
$$

## 2. 原核上的实际像相等

在 $M$ 上，所有相关作用均已由 (1) 支付定义域：
$$
W_MJ_M=-Z_M,\qquad
W_M=-Z_MJ_M^{-1}.
\tag{4}
$$
结合 (3)，立即得到准确的集合等式
$$
\boxed{W_M M=Z_M M.}
\tag{5}
$$
两边都是实际像，不是值域闭包。等价地，
$$
\overline{\operatorname{Ran}W_M}
=\overline{\operatorname{Ran}Z_M}.
\tag{6}
$$
这个共同闭子空间受 $J_M$ 及其逆保持，因为这些有界算子与 $Z_M,W_M$ 交换。
因此在原 $M$ 中，尾第一阶与尾 Bell 项的限制稠密像问题完全相同。

## 3. 从原核到旧头图尾空间

令 $p_0,p_1:H=\mathbb C^2\otimes\widehat H\to\widehat H$ 为两个普通物理坐标投影。
沿用 R208 头图附录的闭尾投影空间
$$
L=\overline{p_0M}=\overline{p_1M}.
\tag{7}
$$
为完整说明两个闭包相同，真实首位矩阵为
$$
N_0=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad t=\eta_0N_1.
$$
$N_0M\subseteq M$ 给 $p_0M\subseteq p_1M$ 及 $t\,p_1M\subseteq p_0M$。
于是 $tL_1\subseteq L_0\subseteq L_1$，其中 $L_i=\overline{p_iM}$。
$L_1$ 为闭尾移位不变空间。为避免把原模型定理无证换到尾模型，
这里把所需的 R12/R23 机制写出。用 $\alpha_r$ 表示原径向权，尾算子
$B=N_1$ 的径向权为
$
\beta_r=\frac{\alpha_{r+1}}{\alpha_1}\quad(r\ge0).
$
这些权正、递减，而且
$\beta_{r+1}/\beta_r=\eta_{r+1}\to0$。R12 的 dyadic 精确幂计算因而在该尾模型给
$
F_k=\frac{B^{2^k}}{\|B^{2^k}\|},\qquad
\|F_k-E_k^{\rm tail}\|=\eta_{k+1}\longrightarrow0.
$
尾 Haar 参考向量仍为每位 $(e_0+e_1)/\sqrt2$，故有限柱独立性及统一范数界给
$E_k^{\rm tail}\to I/2$ 于 WOT，也即 $2F_kx\rightharpoonup x$。
对每个 $x\in L_1$，不变性使
$
2F_kx
=B\left(\frac{2B^{2^k-1}x}{\|B^{2^k}\|}\right)\in BL_1.
$
$BL_1$ 的范数闭包是弱闭的，所以 $\overline{BL_1}=L_1$。
$t=\eta_0B$ 且 $\eta_0\ne0$，于是 $\overline{tL_1}=L_1$，两坐标闭包确实相同。
该证明只对实际径向尾移位使用归一化幂；没有把未知 $W$ 或 $Z$ 的全空间稠密性下传。

需要的另一个已付接口是 $W|_L$ 真正有界。旧首位四阶 monic 消元把
$p_iM$ 放入实际闭尾核 $\mathcal K=\ker\Delta$；
R176 保证 $\mathcal K\subseteq\bigcap_n\operatorname{Dom}W^n$ 及
$W|_{\mathcal K}\in B(\mathcal K)$。因 $L\subseteq\mathcal K$，
且 $p_iM$ 受实际尾作用保持，得
$$
W_L:=W|_L\in B(L),\qquad Z_L:=Z|_L\in B(L).
\tag{8}
$$
没有仅从 $W_M$ 有界就无损穿过一个可能不闭的坐标投影。

对于 $f\in M$，真实张量域给
$$
p_iW_Mf=W_Lp_if,\qquad p_iZ_Mf=Z_Lp_if.
$$
因此 (5) 甚至在每个实际投影像上给
$$
\boxed{W_L(p_iM)=Z_L(p_iM)\qquad(i=0,1).}
\tag{9}
$$
现在才能利用 (7)、(8) 取两次普通范数闭包：
$$
\overline{W_L(p_iM)}=\overline{W_LL},\qquad
\overline{Z_L(p_iM)}=\overline{Z_LL}.
$$
所以
$$
\boxed{N=\overline{W_LL}=\overline{Z_LL}.}
\tag{10}
$$
这里 $N$ 正是 R208 头图附录 (E.3) 的共同闭像。
它加强该附录 (E.4) 的 $ZL\subseteq N$ 为在 $N$ 中稠密。

## 4. 尚未越过的边界

(5) 是原核 $M$ 上的准确像等式；(9) 是真实坐标投影像上的准确等式。
在没有进一步控制坐标原像的情况下，不由它们宣称
$W_LL=Z_LL$ 的未闭集合等式。

也不由 (10) 宣称 $N=L$。
旧尾子商 $L/N$ 上的 $W,Z$ 同时为零依然是准确的剩余问题。
本补充只说明两种缺陷具有相同闭像，不能用其中一个全空间算子的稠密像取消这个缺陷。
