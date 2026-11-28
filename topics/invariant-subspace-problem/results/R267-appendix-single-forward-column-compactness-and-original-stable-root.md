# R267 附录：实际平方近似的单前向列紧性与原稳定闭根

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的实际来源充分条件；前向列上界和紧性尚未支付。** 本文只要求同一实际平方近似在一个固定循环源上的前向列有强收敛子列，不要求整个算子列一致有界，不要求逆向的 $Q_N(t)\Omega$ 有界或有强子列。由所得两列构造闭根时，不附加循环源属于根的实际值域。

这与[已刊单逆向列接口](R267-appendix-single-actual-denominator-column-compactness-and-stable-root.md)分别使用不同的真实来源：该稿从 $Q_N(t)\Omega$ 的极限得到 $Sq=p$；本文从前向列的极限得到 $Sp=f$。本文不宣称两个尚未付的紧性条件等价。

## 1. 原算子及同一平方来源

固定原 Haar 尾
$$
C=A^{(m_0)},\qquad \Omega=1,\qquad
(Jh)(y)=\overline{h(-1-y)},\qquad
[x,y]=\langle x,Jy\rangle.
\tag{1}
$$
$C$ 有界、单射、像稠密，$\Omega$ 对 $C$ 循环。由
[R24 §1](R24-complex-symmetric-moments-and-escape.md)，
$C^*=JCJ$，且每个实际有界交换子 $F\in C'$ 都满足
$F^*=JFJ$。

设 $A_n\in C'$ 是实际全域有界算子，每个 $n$ 各自有界，满足
$$
A_n^2\longrightarrow C\quad\text{强}.
\tag{2}
$$
固定一个对 $C$ 循环的向量 $p\in H$。不要求 $p=\Omega$；后面将使用已经付出单射稠值来源的 $p=P_t\Omega$。置
$$
f_n=A_np.
$$
同一个 $A_n$ 的 $J$ 对称和交换性给对全部 $k\ge0$ 的准确恒等式
$$
[C^kf_n,f_n]=[C^kA_n^2p,p].
\tag{3}
$$
特别有完整归一化矩误差
$$
\boxed{
\sup_{k\ge0}
\frac{|[C^kf_n,f_n]-[C^{k+1}p,p]|}{\|C^k\|}
\le
\|(A_n^2-C)p\|\,\|p\|\longrightarrow0.
}
\tag{4}
$$
$C$ 单射，故这里的分母均非零。没有将一列换成另选的有限矩匹配向量。

## 2. 单前向列定理及精确两列图

**定理。** 在 (1)–(2) 下，若存在严格递增的 $n_j$，使
$$
A_{n_j}p\longrightarrow f\quad\text{于 }H,
\tag{5}
$$
则原 $C$ 有一个闭、稠密定义、单射且像稠密的算子 $S$，满足
$$
\boxed{
\operatorname{Dom}S^2=\operatorname{Dom}S,\qquad
S^2=C|_{\operatorname{Dom}S},\qquad Sp=f.
}
\tag{6}
$$
其实际图由下面两列给出完整核心：
$$
\boxed{
\Gamma S=
\overline{\left\{
\left(a(C)p+b(C)f,\ a(C)f+b(C)Cp\right):
a,b\in\mathbb C[z]
\right\}}.
}
\tag{7}
$$
本稿图顺序固定为 $(x,Sx)$。

**证明。** 由 (4) 和强收敛 (5)，连续双线性式给
$$
[C^kf,f]=[C^{k+1}p,p]\qquad(k\ge0).
\tag{8}
$$
这里只通过指定向量的两次强极限；不从弱收敛通过平方。

先把 (7) 中未闭包的集合记为线性关系 $\mathcal R_0$。其第一坐标域
$$
D_0=\mathbb C[C]p+\mathbb C[C]f
$$
因 $p$ 循环而稠密。任取两组多项式，记
$$
x=a(C)p+b(C)f,\quad u=a(C)f+b(C)Cp,
$$
$$
y=c(C)p+d(C)f,\quad v=c(C)f+d(C)Cp.
$$
用 $C$ 的双线性对称性及 (8) 的多项式线性延拓，逐项展开得到
$$
[u,y]=[x,v].
\tag{9}
$$
其中 $ac$ 项由对称性相等，$bd$ 项将一个 $C$ 移到另一坐标后相等；$ad$ 和 $bc$ 两个交叉项分别使用
$[e(C)f,f]=[e(C)Cp,p]$。两个交叉项均被保留。

若 $(0,u)\in\mathcal R_0$，则 (9) 给 $[u,y]=0$ 对全部 $y\in D_0$ 成立。因为 $JD_0$ 稠密，所以 $u=0$。故 $\mathcal R_0$ 确为单值算子 $S_0$ 的图，其公式为
$$
S_0\bigl(a(C)p+b(C)f\bigr)
=a(C)f+b(C)Cp.
\tag{10}
$$
(9) 还给 $JD_0\subseteq\operatorname{Dom}S_0^*$ 及
$S_0^*Jy=JS_0y$。因此 $S_0$ 可闭。置 $S=\overline{S_0}$，便得到 (7) 的真实闭图。

原公式 (10) 同时给
$$
S_0D_0\subseteq D_0,\qquad S_0^2x=Cx\quad(x\in D_0).
\tag{11}
$$
现在核闭包后的完整自然域。对 $x\in\operatorname{Dom}S$，取 $x_\ell\in D_0$，使
$x_\ell\to x$、$S_0x_\ell\to Sx$。由 (11)，
$$
S_0(S_0x_\ell)=Cx_\ell\longrightarrow Cx.
$$
闭图性说明 $(Sx,Cx)\in\Gamma S$。所以
$Sx\in\operatorname{Dom}S$、$S^2x=Cx$。由自然平方域总包含于 $\operatorname{Dom}S$，这恰好证明 (6) 的域等式，而不只是核心上的形式平方。

$C$ 单射使 $S$ 单射。$S_0f=Cp$，且
$$
\overline{\mathbb C[C]Cp}
=\overline{C\,\mathbb C[C]p}
=\overline{\operatorname{Ran}C}=H.
\tag{12}
$$
于是 $\operatorname{Ran}S$ 稠密。此处用的是循环 $Cp$ 位于根的值域，未使用或证明 $p\in\operatorname{Ran}S$。

同一核心满足 $CD_0\subseteq D_0$、$S_0C=CS_0$。按图闭包延拓，得到
$C\operatorname{Dom}S\subseteq\operatorname{Dom}S$ 及该域上的 $SC=CS$。证明完毕。

(7) 没有被自动识别为某个最大有界分式图。这里只证明 $J$ 对称可闭及其图闭包，没有额外宣称完整 $J$ 自伴性。

## 3. 返回原 Haar 普通不变格

若 $m_0\ge1$，令 $\alpha=\alpha_{m_0-1}>0$。原上一尾准确为
$$
A^{(m_0-1)}
=\begin{pmatrix}0&C\\ \alpha I&0\end{pmatrix}.
$$
置 $R=\alpha^{-1/2}S$，则 $\operatorname{Dom}R^2=\operatorname{Dom}R$，且
$R^2=\alpha^{-1}C$ 于这个同一域。于是
$$
\mathcal M=\{(Ry,y):y\in\operatorname{Dom}R\}
\tag{13}
$$
是上一原尾的非零真闭不变子空间，因为
$$
A^{(m_0-1)}(Ry,y)
=(Cy,\alpha Ry)
=(R(\alpha Ry),\alpha Ry)\in\mathcal M.
$$
闭性来自 $R$ 闭；域稠密给非零；图不含非零第一坐标垂直向量，故为真子空间。

再使用
[原共同坐标旗定理 §6](R12-appendix-all-ordinary-invariant-common-coordinate-flags-and-stable-closed-roots.md)
的实际有限头张量提升，便得到原候选 $A=A^{(0)}$ 的非平凡普通闭不变空间。尤其可以从 $C=A^{(1)}$ 出发。对 $m_0=0$，第2节仍给整尾的闭根，但本文不虚构一个更早的原尾块。

本论证始终在原 Haar 模型内，没有使用负整数边界算子的核或值域替代。也没有将原 $J$ 自动下降到任意未知旗子商。

## 4. 应用到已构造的同一 $Y_NP_t\Omega$

[同一相容有理根稿 §6](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)
已构造实际 $Y_N,D_N\in C'$，满足
$$
Y_N^2=CD_N,\qquad
\|D_N\|\le1,\qquad D_N\longrightarrow I\quad\text{强*}.
\tag{14}
$$
固定原同族 $t\in\mathbb Q_{>0}$，令
$$
p=P_t\Omega,\qquad f_N=Y_NP_t\Omega.
\tag{15}
$$
$P_t$ 在原空间单射稠值，且与 $C$ 交换，所以 $p$ 循环。取第2节的 $A_n=Y_N$，即得：
$$
\boxed{
\text{只要同一列 }Y_NP_t\Omega
\text{ 有强收敛子列，就得到 (6)–(13) 的原闭根及原不变格。}
}
\tag{16}
$$
无需 $\sup_N\|Y_N\|<\infty$，也无需 $\sup_N\|Y_NP_t\|<\infty$。

还有同源的显式全部移位误差。令
$$
b_N=\frac1{M_N}\sum_{\nu\ge N}d_\nu\epsilon_\nu.
$$
原构造在 $\Omega$ 上付 $\|(D_N-I)\Omega\|\le b_N$。实际交换性使
$$
\|(Y_N^2-C)p\|
=\|C(D_N-I)P_t\Omega\|
\le\|C\|\,\|P_t\|\,b_N.
$$
所以 (4) 的右端可取
$$
\|C\|\,\|P_t\|\,\|P_t\Omega\|\,b_N.
\tag{17}
$$

当 $\delta_N<t$ 时，
[固定分子与实际分母稿](R267-appendix-fixed-numerator-actual-denominators-and-odd-cut-contractions.md)
又给准确关系
$$
f_N=C D_N Q_N(t)\Omega.
\tag{18}
$$
逆向列有强子列当然经 (18) 付前向列有强子列；本文不逆转这个推论。$C$ 的像不闭，而 (18) 没有提供 $C^{-1}$ 的统一源费用，故不能据前向强极限自动生成 $Q_N(t)\Omega$ 的有限或紧子列。

## 5. 预设实际平方因子 $C W_n^2$ 的接口

另一可以直接试作的来源是：预先选择实际 $W_n\in C'$，每个 $n$ 有界，并证明
$$
Z_n=CW_n^2,\qquad \|Z_n\|\le1,\qquad
Z_n\longrightarrow I\quad\text{强*}.
\tag{19}
$$
特别可以考虑 $W_n\in\overline{\mathbb C[I,C]}^{\|\cdot\|}$ 中的可逆元，但定理本身不需要其可逆。

定义前向平方近似
$$
A_n=CW_n.
$$
全域有界乘法及交换性准确给
$$
A_n^2=CZ_n\longrightarrow C\quad\text{强*},
\qquad \|A_n^2\|\le\|C\|.
\tag{20}
$$
因此对任一固定循环 $p$，实际需要支付的列可以直接取为
$$
\boxed{C W_n p.}
\tag{21}
$$
若它有一个强子列，第2节立即适用；不要求控制 $W_np$，更不要求未正则化的 $W_n\Omega$。

若 $p=P_t\Omega$，并且 (19) 的原真空误差为
$\|(Z_n-I)\Omega\|\le e_n$，则同源全矩误差为
$$
\sup_{k\ge0}
\frac{|[C^kCW_np,CW_np]-[C^{k+1}p,p]|}{\|C^k\|}
\le
\|C\|\,\|P_t\|\,\|p\|\,e_n.
\tag{22}
$$
这里只使用同一个实际 $W_n,P_t,Z_n$。

给定一个可逆解析单位后取其解析平方根，本身不会支付 (21) 的费用。本文既没有证明某种预选 $W_n$ 满足全部 (19)，也没有给 (21) 的一致范数或紧性。

## 6. 保持的来源边界

本稿的完整结论是一个原模型内的单前向列充分条件及其精确图核心。实际后继可以直接估计 $Y_NP_t\Omega$，也可以设计新的 $W_n$ 并估计 $CW_nP_t\Omega$；无需先解决逆向列。

[指定分离选择的实际列结果](R267-appendix-separated-choice-actual-vacuum-column-divergence.md)已给 $Y_NP_t\Omega$ 在偶切口范数发散，以及逆向 $Q_N(t)\Omega$ 在全切口范数发散。前一结论尚未排除前向奇切口的强子列；不能把逆向全切口界直接移到本文的前向列。

若以有限头条件期望 $E_L$ 验证强紧性，仍需真实支付同一前向列的两个预算：列范数一致有界，以及
$\lim_{L\to\infty}\sup_n\|(I-E_L)A_np\|=0$。这些预算在本文未付。平方强*收敛、每个单独算子有界或所有移位双线性矩趋于目标，都不能代替这一来源。

所得根只被证明在其两列图闭包的稳定域上平方为 $C$；没有自动得到 $P_tH\subseteq\operatorname{Dom}S$、$SP_t$ 有界或 $p\in\operatorname{Ran}S$。原普通 ISP 完成标准仍未达到。
