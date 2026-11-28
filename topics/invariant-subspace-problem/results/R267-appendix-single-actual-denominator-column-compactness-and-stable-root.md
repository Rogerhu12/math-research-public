# R267 附录：同一实际分母的单真空列紧性与原闭稳定根

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：准确的实际来源充分条件；单列紧性尚未证明。** 使用[全切口平方收缩](R267-appendix-all-cut-square-contractions-and-unconditional-strong-square-limit.md)中同一个 $Q_N$。本文将此前要求的整个算子列强收敛，减弱为一个指定向量列的强收敛子列；证明不要求 $\sup_N\|Q_N\|<\infty$。区别于[同一有界分子分母的最大根](R12-appendix-same-flat-denominator-maximal-stable-root-and-all-flag-cores.md)，这里从实际单列极限构造两列图核心，没有假设或构造全域有界的平方分子分母等式。

## 1. 固定来源及全部移位矩的同一误差

令 $C=A^{(m_0)}$ 为原 Haar 尾，$\Omega=1$ 为其单位循环向量。记原共轭为
$$
(Jh)(y)=\overline{h(-1-y)},\qquad
[x,y]=\langle x,Jy\rangle.
\tag{1}
$$
这是连续、对称、非退化的复双线性式。[R24 §1](R24-complex-symmetric-moments-and-escape.md) 已付 $C^*=JCJ$，以及每个实际有界交换子 $F$ 都满足 $F^*=JFJ$。

固定 $t\in\mathbb Q_{>0}$，沿用同一个 $P_t,Q_N,D_N$，定义
$$
p=P_t\Omega,\qquad q_N=Q_N\Omega.
\tag{2}
$$
$P_t$ 在原空间单射稠值，且与 $C$ 交换，所以
$$
\overline{\{a(C)p:a\in\mathbb C[z]\}}
=\overline{P_t\mathbb C[C]\Omega}
=\overline{\operatorname{Ran}P_t}=H.
\tag{3}
$$
特别 $p\ne0$ 且 $p$ 对原 $C$ 循环。

取任一 $N_0$ 使 $\delta_{N_0}<t$，记 $K=\|Q_{N_0}^2\|$ 以及
$$
b_N=\frac1{M_N}\sum_{\nu\ge N}d_\nu\epsilon_\nu
<\frac{2^{-N-5}}{M_N}.
\tag{4}
$$
全切口平方稿给
$$
Q_N^2\longrightarrow C^{-1}P_{2t}\quad\text{强*},
\qquad
\|(Q_N^2-C^{-1}P_{2t})\Omega\|\le Kb_N.
\tag{5}
$$
这里的原逆表示已经支付的有界来源。

由同一个 $Q_N$ 的 $J$ 对称性及交换性，对每个 $k\ge0$，
$$
[C^{k+1}q_N,q_N]=[C^k C Q_N^2\Omega,\Omega],
\qquad
[C^kp,p]=[C^kP_t^2\Omega,\Omega].
\tag{6}
$$
因此完整归一化移位矩有统一误差
$$
\boxed{
\sup_{k\ge0}
\frac{|[C^{k+1}q_N,q_N]-[C^kp,p]|}{\|C^k\|}
\le \|C\|K b_N.
}
\tag{7}
$$
(5)–(7) 在 $N\ge N_0$ 的合法尾列上使用。原 $C$ 单射，故分母 $\|C^k\|$ 非零。此式保同一实际 $q_N$、固定循环 $p$ 及完整原 $C$，不是另外选取的有限矩匹配向量。

## 2. 只需这一列的强子列

**定理 2.1。** 若存在严格递增的 $N_j$，使
$$
q_{N_j}=Q_{N_j}\Omega\longrightarrow q
\quad\text{于 }H,
\tag{8}
$$
则原 $C$ 有一个闭、稠密定义、单射稠值的算子 $S$，满足
$$
\operatorname{Dom}S^2=\operatorname{Dom}S,\qquad
S^2=C|_{\operatorname{Dom}S}.
\tag{9}
$$
其图具有显式的两列核心
$$
\boxed{
\Gamma S
=
\overline{\left\{
\bigl(a(C)q+b(C)p,\ a(C)p+b(C)Cq\bigr):
a,b\in\mathbb C[z]\right\}}.
}
\tag{10}
$$
本文的图顺序是 $(x,Sx)$。

**证明。** 因为 (8) 是强收敛，连续双线性式允许将其两次代入。由 (7)，
$$
[C^{k+1}q,q]=[C^kp,p]\qquad(k\ge0).
\tag{11}
$$
不使用弱平方极限，也不需要 $Q_{N_j}$ 的一致算子范数。

先将 (10) 中未闭包的集合视为线性关系 $\mathcal R_0$。其第一坐标域
$$
D_0=\mathbb C[C]q+\mathbb C[C]p
$$
由 (3) 稠密。任取两组多项式，写
$$
x=a(C)q+b(C)p,\quad u=a(C)p+b(C)Cq,
$$
$$
y=c(C)q+d(C)p,\quad v=c(C)p+d(C)Cq.
$$
原 $C$ 的双线性对称性，连同 (11) 的多项式线性延拓，直接给
$$
[u,y]=[x,v].
\tag{12}
$$
确切地，展开的 $ac$ 项和 $bd$ 项各自由对称性相等；$ad$、$bc$ 两项分别使用
$[e(C)p,p]=[e(C)Cq,q]$。所以这里保留了两个交叉项。

若 $(0,u)\in\mathcal R_0$，则 (12) 给 $[u,y]=0$ 对全部 $y\in D_0$ 成立。$JD_0$ 稠密，因而 $u=0$。故该关系确为单值算子 $S_0$ 的图，且
$$
S_0(a(C)q+b(C)p)=a(C)p+b(C)Cq.
\tag{13}
$$
(12) 还说明对每个 $y\in D_0$，
$Jy\in\operatorname{Dom}S_0^*$ 且 $S_0^*Jy=JS_0y$。
所以 $\operatorname{Dom}S_0^*$ 稠密，$S_0$ 可闭。记 $S=\overline{S_0}$，这就是 (10) 的实际闭图。

由 (13)，$S_0D_0\subset D_0$ 且
$$
S_0^2x=Cx\qquad(x\in D_0).
\tag{14}
$$
现在付闭包后的自然域。给定 $x\in\operatorname{Dom}S$，取
$x_n\in D_0$ 使 $x_n\to x$、$S_0x_n\to Sx$。又
$$
S_0(S_0x_n)=Cx_n\longrightarrow Cx.
$$
因此 $(Sx,Cx)$ 也在同一个闭图 $\Gamma S$ 中。这证明
$Sx\in\operatorname{Dom}S$、$S^2x=Cx$，从而 (9) 中完整的自然平方域等式成立，而不只是核心上的形式平方。

域由 (3) 稠密。$C$ 单射及 (9) 使 $S$ 单射；另一方面
$S(a(C)q)=a(C)p$，所以 (3) 也付 $\operatorname{Ran}S$ 稠密。特别 $q\ne0$。
同一核心还给 $CD_0\subset D_0$、$S_0C=CS_0$；取图闭包后得
$C\operatorname{Dom}S\subset\operatorname{Dom}S$ 及实际域上的 $SC=CS$。证毕。

(10) 同时明确了什么被证明：只有该两列多项式图的闭包，没有把它自动识别为某个此前的最大有界分式图，也没有从 $J$ 对称可闭性宣称完整 $J$ 自伴性。

## 3. 返回原 Haar 普通不变格

若 $m_0\ge1$，令 $\alpha=\alpha_{m_0-1}>0$。原上一尾的真实首位块为
$$
A^{(m_0-1)}
=\begin{pmatrix}0&C\\ \alpha I&0\end{pmatrix}.
$$
取 $R=\alpha^{-1/2}S$。由 (9)，其完整域稳定且 $R^2=\alpha^{-1}C$ 于该域。于是
$$
\mathcal M=\{(Ry,y):y\in\operatorname{Dom}R\}
\tag{15}
$$
是 $A^{(m_0-1)}$ 的非零真闭不变空间：
$$
A^{(m_0-1)}(Ry,y)
=(Cy,\alpha Ry)
=(R(\alpha Ry),\alpha Ry)\in\mathcal M.
$$
闭性来自 $R$ 闭，非零来自域稠密，真性来自图不含非零第一坐标垂直向量。

再按[原共同坐标旗定理](R12-appendix-all-ordinary-invariant-common-coordinate-flags-and-stable-closed-roots.md) §6 的实际有限头张量式提升，即得原候选 $A=A^{(0)}$ 的非平凡普通闭不变空间。因此可以直接在 $C=A^{(1)}$ 上应用本定理；不存在把负整数边界模型移回原 Haar 的步骤。

定理 2.1 对 $m_0=0$ 同样给原整尾的闭根；此时本文不把上一尾块当作已存在的原候选。这里也没有将原 $J$ 下降到任意未知子商，或宣称所构造 $S$ 自动给每个旗商上的闭根。

## 4. 准确尚欠的单列来源

本稿没有证明 (8)。平方稿的 (5) 与本稿完整的 (7) 都不付 $q_N$ 的强紧性；即使这一列仅有界，也不能让其弱聚点通过双线性平方。

一个可直接使用的充分预算是：这一列有界，且对原有限头条件期望 $E_L$ 有
$$
\lim_{L\to\infty}\sup_{N\ge N_0}
\|(I-E_L)Q_N\Omega\|=0.
\tag{16}
$$
每个 $E_L$ 有限秩，故该预算付相对强紧性并给 (8)。这只是将实际所需向量费用写明；本文没有取得 (16)，也没有用 $Q_N^2$ 的能量估计代替它。

与旧要求相比，(8) 不需要 $Q_N$ 在全 $H$ 上一致有界，甚至不要求它们在所有柱向量上收敛。另一方面，(10) 不自动付 $P_tH\subset\operatorname{Dom}S$ 或 $SP_t$ 有界；不能因此倒推一个同一 $P_t$ 的有界平方分子。实际单列强紧性仍是新的未完成输入，原普通 ISP 完成标准不变。
