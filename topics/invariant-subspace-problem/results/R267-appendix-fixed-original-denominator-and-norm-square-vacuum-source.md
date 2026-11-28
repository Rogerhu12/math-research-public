# R267 附录：同参数平方曲线的固定原分母与原真空列接口

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的固定分母与范数平方来源；实际列上界及强子列仍未付。** 本文继续[已刊全因子同参数构造](R267-appendix-all-factor-complex-parameter-odd-target-and-norm-square-source.md)，证明其零参数目标准确为原 $C$ 乘以一个已经构造的固定有界分母的平方：
$$
P(0)=C Q_*^2.
\tag{1}
$$
$Q_*$ 在全部原有限放大闭不变旗子商上单射、像稠密。因而原文的 $X(s)^2\to P(0)$ 是同一固定原二次目标 $C Q_*^2$ 的算子范数近似，不仅是一个未识别的奇目标近似。仍没有构造满足 $V^2=CQ_*^2$ 的有界 $V$。

## 1. 固定同一实际构造，分清两个尾指标

固定原 Haar 尾 $C=A^{(m_0)}$，其中 $m_0\ge0$，$\Omega=1$，$c=\|C\|$。沿用前稿的
$$
Z_\nu(z)=(1-\zeta_\nu)F_\nu+z\zeta_\nu C/c,\qquad
d_\nu=(\nu+2)!-(\nu+1)!,\qquad
K=\sum_{\nu\ge0}d_\nu\zeta_\nu.
$$
特别 $d_0=1$，而全部 $\nu\ge1$ 的 $d_\nu$ 都为偶数。令
$$
T(z)=\operatorname*{SOT^*\!-\!lim}_{L\to\infty}
\prod_{\nu=1}^{L-1}Z_\nu(z)^{d_\nu/2}.
\tag{2}
$$
前稿 §4 已支付每个 $T(z)$ 的全旗单射、稠像，及 $T$ 的算子范数全纯性。

把第零个有限块 $F_0$ 的起点另记为 $b_0\ge1$，长度为 $q_0$：
$$
F_0=\frac2{q_0+2}\sum_{j=b_0}^{b_0+q_0-1}
\frac{C^{2^j}}{\|C^{2^j}\|},\qquad K_0=2^{b_0}.
\tag{3}
$$
$b_0$ 是相容族第零块的选择参数，**不是**原 Haar 尾指标 $m_0$。尤其 $K_0$ 是正偶数，包括 $m_0=0$ 时也如此。

从实际有限多项式精确提出最低幂：
$$
(1-\zeta_0)F_0=C^{K_0}G_0(C),
\tag{4}
$$
$$
G_0(z)=\frac{2(1-\zeta_0)}{q_0+2}
\sum_{j=b_0}^{b_0+q_0-1}
\frac{z^{\,2^j-K_0}}{\|C^{2^j}\|}.
$$
这里 $G_0(0)>0$，全部指数均为偶数。

## 2. 固定分母的真实平方、偶性及全旗范围

在零点取 $G_0$ 的解析平方根芽 $g_0$，规范为
$g_0(0)=\sqrt{G_0(0)}>0$。因为 $G_0$ 偶且该规范解析芽唯一，$g_0$ 也偶。

原 $C$ 拟幂零，故此芽的幂级数在 $C$ 上算子范数收敛，并且
$$
g_0(C)^2=G_0(C).
$$
$g_0(C)$ 及其逆都属于 $\overline{\mathbb C[I,C]}^{\|\cdot\|}$。这里只对有非零常数项的有限多项式单位取解析根，未对 $C$ 取分数幂。

定义两个实际有界算子
$$
R_0=C^{K_0/2}g_0(C),\qquad
\boxed{Q_*=R_0T(0).}
\tag{5}
$$
前稿的原定义 $P(z)=C Z_0(z)T(z)^2$ 及 (4) 直接给
$$
R_0^2=(1-\zeta_0)F_0,\qquad
\boxed{C Q_*^2=C(1-\zeta_0)F_0T(0)^2=P(0).}
\tag{6}
$$
这些是全域有界算子的精确乘法，保留全部原 carry 和完整无限尾积。

设 $U$ 为首位符号，$\gamma(F)=UFU$。原式 $\gamma(C)=-C$、$g_0$ 偶以及前稿的 $\gamma(T(0))=T(0)$ 给
$$
\boxed{\gamma(Q_*)=(-1)^{K_0/2}Q_*.}
\tag{7}
$$
所以 $Q_*^2$ 为 $\gamma$ 偶，而 $CQ_*^2$ 为 $\gamma$ 奇。没有任意更换零点根支。

核全旗性质：在任意非零原有限放大闭不变旗子商上，原 $C$ 的诱导算子单射、像稠密；其正整数幂仍如此。$g_0(C)$ 及其逆都保持该旗，故其诱导算子是有界单位。$T(0)$ 的同一实际强单位和全旗结论已经由前稿 §3–4 支付。因此 (5) 中的每个诱导 $Q_*$ 都单射且像稠密。这一步没有从全空间 quasiaffinity 自动下降到商。

此外 $Q_*$ 属于原共同幂理想
$$
\mathfrak F=\bigcap_{a\ge1}C^a C'.
\tag{8}
$$
确切地，对 (2) 的 $z=0$ 尾积，任意有限前缀都能提出指数
$\sum_{\nu=1}^{L-1}2^{b_\nu}d_\nu/2$ 的 $C$ 幂；该指数趋于无穷。前缀余因子有界，剩余真实强极限尾积是收缩，故对任意固定 $a$ 可以实际写出 $T(0)=C^a B_a$，$B_a\in C'$ 有界。再乘固定 $R_0$ 即得 (8)。

## 3. 同一固定原目标的算子范数近似

前稿 §4 构造的同一 $X(s)$，$s\ne0$，保持
$$
X(s)^2=P(s^2),\qquad X(-s)=-X(s).
$$
结合其 §2 的完整参数 Lipschitz 界与 (6)，对 $0<|s|\le1$ 有
$$
\boxed{
\|X(s)^2-CQ_*^2\|\le cK|s|^2.
}
\tag{9}
$$
$Q_*$ 不依赖 $s$。每个 $X(s)$ 各自有界且在全部原旗上为 quasiaffinity；(9) 不提供 $\sup_{s\to0}\|X(s)\|$。

令
$$
p=Q_*\Omega,\qquad f_s=X(s)\Omega.
$$
$p$ 对原 $C$ 循环：$Q_*$ 与 $C$ 交换且像稠密，而 $\Omega$ 循环。使用 R24 的全空间连续双线性式 $[x,y]=\langle x,Jy\rangle$，以及全部 $C'$ 的 $J$ 对称，准确得到
$$
[C^k f_s,f_s]-[C^{k+1}p,p]
=[C^k(X(s)^2-CQ_*^2)\Omega,\Omega].
$$
因此有同一列的全矩预算
$$
\boxed{
\sup_{k\ge0}
\frac{|[C^k f_s,f_s]-[C^{k+1}p,p]|}{\|C^k\|}
\le cK|s|^2.
}
\tag{10}
$$
这里 $\|\Omega\|=1$，且原 $C$ 单射使各分母非零。

若某个 $s_j\to0$ 给 $f_{s_j}\to f$ 强收敛，(10) 就给
$[C^kf,f]=[C^{k+1}p,p]$ 对全部 $k$。于是[单前向列定理 §2](R267-appendix-single-forward-column-compactness-and-original-stable-root.md)的两列闭图证明直接适用：
$$
\Gamma S=
\overline{\left\{
\bigl(a(C)p+b(C)f,\ a(C)f+b(C)Cp\bigr):
a,b\in\mathbb C[z]\right\}}.
\tag{11}
$$
图顺序为 $(x,Sx)$。该闭包是稠密定义、单射、像稠密的闭算子，满足
$$
\operatorname{Dom}S^2=\operatorname{Dom}S,\qquad
S^2=C|_{\operatorname{Dom}S},\qquad Sp=f.
\tag{12}
$$
(11) 的单值与可闭性只用循环 $p$ 及 (10) 的极限矩；闭包后的稳定域由
$(x_n,S_0x_n)\to(x,Sx)$ 同时给
$(S_0x_n,Cx_n)\to(Sx,Cx)$ 支付。未声称 $Q_*H\subseteq\operatorname{Dom}S$ 或 $SQ_*$ 有界。

## 4. 原 $m_0=0$ 也只需同一真空列

这里明确核验把 $\Omega$ 列搬到首位本征源的固定有界单位，对每个原尾 $m_0\ge0$ 都适用。

在该原尾的第一物理位，完整原矩阵为
$$
C=\begin{pmatrix}0&C_1\\cI&0\end{pmatrix},
\qquad
\Omega=\frac1{\sqrt2}\binom{\Omega_1}{\Omega_1},
\qquad
e_+=\binom{\Omega_1}{0}.
\tag{13}
$$
$c$ 是该尾的第一权，等于 $\|C\|$；$C_1$ 是完整下一尾，不作压缩。由 (13)，
$$
(I+C/c)e_+=\sqrt2\,\Omega.
$$
所以
$$
\boxed{
F_+=\sqrt2(I+C/c)^{-1}\in C',\quad
F_+\Omega=e_+,\quad Ue_+=e_+.
}
\tag{14}
$$
其逆有界来自 $C$ 拟幂零。这也逐尾核实了
[R267 原 Cayley 式 (1.3)](R267-disjoint-odd-walsh-block-accretive-regularizers-and-contractive-strong-units.md)
的同一真空来源；不存在 $m_0\ge1$ 的额外限制。

若 $X(s_j)\Omega$ 强收敛，则实际同一列
$$
X(s_j)e_+=F_+X(s_j)\Omega
\tag{15}
$$
也强收敛。取 $H^\pm(s)=\gamma(X(s))\pm iX(s)$，前稿的准确全域界为
$$
\|H^+(s)H^-(s)\|\le2cK|s|^2,\qquad
X(s)^2\to P(0).
$$
由 $Ue_+=e_+$，两列 $H^\pm(s_j)e_+$ 同时强收敛，且由固定酉 $U$ 相连。前稿 §6 / [首位超不变稿 §3](R12-appendix-first-bit-gauge-zero-divisors-and-single-forward-column-hyperinvariants.md)
的连续双线性转置证明即给原同一 $C$ 的非平凡超不变子空间。若列极限为零，该证明用 $P(0)$ 单射处理，不借平方范数控制奇列。

本构造事实上还可直接排除 (15) 的零强极限。$P(0)$ 保持函数正锥，$\gamma(P(0))=-P(0)$，且 $P(0)$ 单射。故 $P(0)e_+$ 是非零非负的奇首位支持函数，而 $Je_+$ 是该奇半柱上的正常数。于是
$$
\eta:=[P(0)e_+,e_+]>0.
$$
由 $J$ 对称和平方范数收敛，
$$
[X(s)e_+,X(s)e_+]=[P(s^2)e_+,e_+]\to\eta.
$$
特别对充分小的 $s$，
$$
\|X(s)\Omega\|\ge\frac{\sqrt{\eta/2}}{\|F_+\|}.
\tag{16}
$$
这是同一列的下界，仍未支付其上界或强紧性。

## 5. 尚未支付的实际输入

本文新增的是已经固定的 $Q_*$、原精确身份 (6)、同一原二次目标的范数费用 (9)，以及无需先控制逆列的真空来源 (10)、(15)。$Q_*$ 是实际有界全旗分母，而不是由一个未知根反推出的形式分母。

下一实际任务仍是同一 $X(s)\Omega$ 的强收敛子列，或直接构造有界 $V\in C'$ 满足 $V^2=CQ_*^2$。当前没有任何统一列上界、紧性或有界平方分子结论。$X(s)^2$ 的范数收敛、(16) 的非零下界和各固定参数的全旗单射稠像都不能代替它。
