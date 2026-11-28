# Phi：两层完整 Schur 修正后的三阶标量及实际最高系数

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 当前边界和真正新输入

继续[二阶核秩二及 790 次上界](../results/R150-appendix-unit211-Phi-zero-second-kernel-Schur-rank-two-and-degree-upper-bound-790.md)的同一原 $B_{22}$、固定次数对偶和
$$
N(t)=H_0+tH_1+t^2H_2+t^3H_3+O(t^4),
\qquad
\det N(t)=t^{802}P(t^{-1},Q).
$$
此前三层实际秩依次为 $14,5,2$，故目前只有
$$
789\le\deg_uP\le790.
$$
本次仅计算新增 $H_3$、两层完整消元修正及最后一维标量。该标量若非零，原 QQ 次数就是 790；不以旧模 789 次为预设答案。

固定此前已返的十四阶和五阶原行列 minor，不重跑旧三阶、八阶或二十二阶秩，不重跑 Hungarian 或模 determinant。

## 2. 原十四阶块的三阶系数

令 $A=H_0[I,J]$，并沿用完整
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14},
\qquad UH_0=0,\quad H_0V=0.
$$
$U,V$ 的补坐标块都是 $\Delta I_8$。第一层完整 Schur 补写成
$$
S(t)=t\Delta^{-2}S_1+
t^2\Delta^{-3}W_2+
t^3\Delta^{-4}W_3+O(t^4),
$$
其中 $S_1=UH_1V$，此前已经完整返回
$$
W_2=\Delta UH_2V-
(UH_1[:,J])\operatorname{Adj}(H_1[I,:]V).
$$
本次新增的完整三阶分子为
$$
\begin{aligned}
W_3={}&\Delta^2UH_3V\\
&-\Delta(UH_2[:,J])\operatorname{Adj}(H_1[I,:]V)\\
&-\Delta(UH_1[:,J])\operatorname{Adj}(H_2[I,:]V)\\
&+(UH_1[:,J])\operatorname{Adj}
 H_1[I,J]\operatorname{Adj}(H_1[I,:]V).
\end{aligned}
\tag{1}
$$
最后一项来自 $A(t)^{-1}$ 的一阶变化，不得省略。

## 3. 第二层五阶消元也必须完整支付

此前把 $S_1=D_rT_1D_c$ 的实际内容尺度全部运输，并构造完整三维核 $\widehat U,\widehat V$。本次保持同一对象，记
$$
K_2=\widehat U W_2\widehat V,\qquad
\operatorname{rank}_{\mathbb Q(Q)}K_2=2.
$$
取已固定的五阶原子块
$$
B=S_1[I_2,J_2].
$$
这里是 $S_1$ 的原条目，不是忽略内容尺度的 $T_1$。由已有五阶 adjugate 和 $D_r,D_c$ 构造多项式 $\operatorname{Adj}_5,\Delta_5$，并完整返回
$$
B\operatorname{Adj}_5=\operatorname{Adj}_5B=\Delta_5I_5.
\tag{2}
$$

第二层真正的下一系数是
$$
\widehat U W_3\widehat V-
(\widehat U W_2[:,J_2])B^{-1}
(W_2[I_2,:]\widehat V).
\tag{3}
$$
所以不能只把 $W_3$ 在旧三维核中收缩。

## 4. 最后一维核及新标量

仅用已付 $K_2$ 的独立列 $(0,1)$，在预定 QQ 点 $Q=2,3,5,7$ 选择一个非零二阶原行 minor。对这个新二阶块用显式 adjugate 返回双向身份，得到完整的一维左右核 $u,v$。公共内容的每次除法都乘回，并完整验证
$$
uK_2=0,\qquad K_2v=0.
$$

令
$$
u\widehat U=g_L\ell,\qquad
\widehat Vv=g_Rr
$$
是逐向量精确除公共内容后的原多项式身份。$g_L,g_R$ 非零且只用于函数域尺度，不作物理单位。实际只收缩一行一列：
$$
\boxed{
\Theta=
\Delta_5\,\ell W_3r-
(\ell W_2[:,J_2])\operatorname{Adj}_5
(W_2[I_2,:]r).
}
\tag{4}
$$
实现将 $\ell U$、$Vr$ 提前合成，直接计算 (1)–(4) 的标量和五列交叉项，不生成大的八阶 $W_2,W_3$。完整返回低一阶 $\ell W_2r=0$。

如果 $\Theta\ne0$，原 $\det N$ 在 $t=0$ 的阶恰为十二，从而 $\deg_uP=790$。如果 $\Theta=0$，则阶至少十三；结合已付模下界，即得 $\deg_uP=789$。这两种输出都是真实结果，不把后一种当作应有答案。

## 5. 可选但同源的实际 u790 系数返回

为准确区分原 QQ 次数与 $Q=2,p=1009$ 的降次，源同时从已经构造的块恒等式恢复实际系数 $L_{790}(Q)=[u^{790}]P$。

设
$$
a_{14}=\det A,\quad a_5=\det B,\quad
a_2=\det K_2[I_3,J_3],
$$
$$
d_U=\det\widehat U[:,I_2^c],\qquad
d_V=\det\widehat V[J_2^c,:],
$$
并记最后一维核在补坐标上的非零值为 $\alpha,\beta$。令 $\varepsilon$ 是三层原行列置换符号的乘积。完整块 determinant 公式给
$$
L_{790}
=
\frac{\varepsilon\,a_{14}a_5a_2\,g_Lg_R\,\Theta}
{\Delta^{20}\Delta_5d_Ud_V\alpha\beta}.
\tag{5}
$$
指数二十来自第一层 $t^8\Delta^{-16}$、第二层 $t^3\Delta^{-3}$ 和末一维的一次 $\Delta^{-1}$。式 (5) 的三个小块 determinant 都由已成 adjugate 标量、实际行交换符号和内容尺度精确给出，没有重算二十二阶 determinant。

如果 $\Theta\ne0$，程序对 (5) 完整取消并要求分母仅为非零有理常数，再逐项精确除法返回。因此得到真实 QQ$[Q]$ 原系数，而不是函数域未付极点。该系数的 1009 整性、在 $Q=2,3,5,7$ 的是否为零及模值均小量输出。旧实际模次数 789 要求 $L_{790}(2)\equiv0\pmod{1009}$，但不预设 $L_{790}(2)$ 在 QQ 中为零。

如果 $\Theta=0$，(5) 是零多项式，直接由旧下界支付 789。所有 $Q$ 零纤维和整 $H_{42}$ 都保留。

## 6. 资源与依赖

建议文件：
2026-11-28-unit211-Phi-zero-original-twenty-two-third-kernel-scalar-and-exact-degree-8542.py。

仍只读取同六件小源码：直接原二十二列源 4080 字节必要定义前缀及其递归五个前缀。无历史 JSON。固定总 120 秒 / 1 GiB，所有前缀共享绝对截止。只输出 SHA、少量索引、完整返回数、秩及次数结论，不保存可重算系数或矩阵载荷。

完整三阶标量形成后立即打印已经成立的 789 或 790 次结论，再进行 (5) 的系数取消。后者若未完成，前一已成次数结论不因此撤销；不会把附加系数过程设为数学登记门槛。

数学源尚未执行。
源 18858 字节，SHA256 e8c964ee3a74c9992fe4154c5c58965fa12516fc13e6537ec8864abdce51e85b。
