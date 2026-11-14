# R8：显式 strict Kummer 类、Selmer 核与广义 Kato 类的比较

**可信度：已证明。** 本文完整证明 strict Selmer 核的正合列，并在 Castella 的已证定理下得到一个逐素数等价判据。显式非零向量本身并不证明 $\Sha[p^\infty]$ 有限；需要补充的比较公式在最后明确列出。

## 1. 曲线、局部对数与记号

固定 R4 的曲线和两个点
$$
E:y^2=x^3-17x,\qquad P=(-1,4),\quad Q=(9,24).
$$
R4 证明 $\operatorname{rank}E(\mathbb Q)=2$ 且 $P,Q$ 独立。因此 $P,Q$ 构成 $E(\mathbb Q)\otimes_{\mathbb Z}\mathbb Q_p$ 的基，不需要它们在整数上生成全部自由部分。

令 $p$ 为好约化素数。记
$$
V_pE=T_pE\otimes_{\mathbb Z_p}\mathbb Q_p,\quad
W_p=E(\mathbb Q)\otimes_{\mathbb Z}\mathbb Q_p,\quad
U_p=E(\mathbb Q_p)\widehat\otimes\mathbb Q_p.
$$
帽号表示先取 $p$-进完备化再张量 $\mathbb Q_p$。局部 Kummer 理论把 $U_p$ 识别为 $H^1_f(\mathbb Q_p,V_pE)$。令
$$
S_p=\operatorname{Sel}(\mathbb Q,V_pE),\qquad
S_p^0=\ker\bigl(\operatorname{res}_p:S_p\to U_p\bigr),
$$
$$
D_p=T_p\Sha(E/\mathbb Q)\otimes_{\mathbb Z_p}\mathbb Q_p,
\qquad t_p=\dim_{\mathbb Q_p}D_p.
$$
使用通常的 Kummer 正合列
$$
0\longrightarrow W_p\longrightarrow S_p
\longrightarrow D_p\longrightarrow0.
\tag{1}
$$
这个正合列以及 $t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]$ 的说明见 R1；特别地，$t_p=0$ 等价于该初级部分有限。

选定 Néron 微分后，椭圆曲线的形式对数在一个足够小的开子群上给出到 $\mathbb Q_p$ 的局部同构。由于 $E(\mathbb Q_p)$ 是紧的一维 $p$-adic Lie 群，这个开子群的指数有限。先乘一个使点进入该子群的整数，再除以该整数，可把对数延拓成
$$
\ell_p:U_p\xrightarrow{\ \sim\ }\mathbb Q_p.
\tag{2}
$$

**引理 1。** 若 $R\in E(\mathbb Q)$ 非扭，则 $\ell_p(R)\ne0$。特别地，$W_p\to U_p$ 满射。

**证明。** 取非零整数 $N$，使 $NR$ 落在形式对数单射的足够小开子群中。若 $\ell_p(R)=0$，则 $\log_E(NR)=0$，从而 $NR=O$。由于 $E(\mathbb Q)\to E(\mathbb Q_p)$ 在点上单射，这也在 $E(\mathbb Q)$ 中成立，与 $R$ 非扭矛盾。

由 (2)，$U_p$ 一维。$P$ 非扭，故其像非零，因而 $W_p$ 的像为整个 $U_p$。$\square$

这里没有声称二维 $W_p$ 到一维 $U_p$ 单射。每一个非扭有理点的局部像非零，与存在 $\mathbb Q_p$ 系数的非零核向量并不矛盾。

## 2. 显式 strict 类和完整正合列

定义
$$
v_p=\ell_p(Q)P-\ell_p(P)Q\in W_p.
\tag{3}
$$
通过 (1) 也把它视为 $S_p$ 中的 Kummer 类。

**命题 2。** 对每个好素数 $p$，$v_p\ne0$，且有短正合列
$$
0\longrightarrow\mathbb Q_pv_p
\longrightarrow S_p^0
\longrightarrow D_p
\longrightarrow0.
\tag{4}
$$
因此
$$
W_p\cap S_p^0=\mathbb Q_pv_p,\qquad
\dim_{\mathbb Q_p}S_p^0=1+t_p.
\tag{5}
$$

**证明。** $P,Q$ 是 $W_p$ 的基，且由引理 1 两个对数都非零，故 (3) 非零。同时
$$
\ell_p(v_p)=\ell_p(Q)\ell_p(P)-\ell_p(P)\ell_p(Q)=0,
$$
所以 $v_p\in S_p^0$。

引理 1 给出 $W_p\to U_p$ 满射；其定义域二维、值域一维，故核一维。该核包含非零的 $v_p$，因而恰为 $\mathbb Q_pv_p$。这证明 (4) 的左端和中间核的断言。

为证明右端满射，任取 $d\in D_p$。由 (1)，可以选 $s\in S_p$ 映到 $d$。再利用 $W_p\to U_p$ 满射，选 $w\in W_p$ 满足 $\operatorname{res}_p(w)=\operatorname{res}_p(s)$。于是 $s-w\in S_p^0$，且它在 $D_p$ 的像仍是 $d$。这证明满射并完成 (4)。取维数得到 (5)。$\square$

特别地，我们对所有好 $p$ 都已构造一个非零 strict 类；(4) 显示它与额外的 $\Sha$ Tate 模方向可以同时存在。这种构造本身不给出 $t_p=0$。

## 3. Castella 定理给出的准确等价条件

此节的外部输入是 F. Castella，*Generalised Kato classes on CM elliptic curves of rank 2*，American J. Math. 最终稿，[arXiv:2204.09608v3](https://arxiv.org/html/2204.09608v3)，Theorem B（正文 Theorem 6.3.1）及 §1.3。

该定理适用于 $p\ge5$、好普通约化的 CM 曲线，要求 $L(E,s)$ 在 $s=1$ 有正的偶数阶零点。取该定理中的辅助 Hecke 角色满足式 (1.5) 和 Theorem A 的 (i)–(ii)；原文在 Theorem B 后说明这些选择存在。它给出的类 $\kappa_p$ 满足
$$
\kappa_p\in S_p^0,\qquad
\kappa_p\ne0\ \Longrightarrow\ \dim_{\mathbb Q_p}S_p=2.
\tag{6}
$$
当 $\dim S_p=2$ 时，还给出
$$
\kappa_p\ne0\quad\Longleftrightarrow\quad
\operatorname{res}_p:S_p\to U_p\text{ 非零}.
\tag{7}
$$
这里引用已证定理的这些准确结论，不把该文的 big class 非扭性直接当作特定权重的非消失。

**命题 3。** 对 $E17$ 及每个 $p\equiv1\pmod4$、$p\ne17$，按上述选择构造 $\kappa_p$，则
$$
\kappa_p\ne0
\quad\Longleftrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{8}
$$
在这两个等价条件成立时，存在唯一的 $A_p\in\mathbb Q_p^\times$，使
$$
\kappa_p=A_pv_p.
\tag{9}
$$

**证明。** 先检查外部定理对曲线的假设。曲线在 $K=\mathbb Q(i)$ 上具有 CM；所列 $p$ 好且分裂，所以为普通约化。根数为 $+1$，见局部输入 note。若 $L(E,1)\ne0$，Gross–Zagier–Kolyvagin 的解析秩零结论会给出代数秩零，与 R4 矛盾。因此 $L(E,1)=0$；函数方程使其零点阶为正偶数。这些事实满足外部定理。

若 $\kappa_p\ne0$，由 (6) 得 $\dim S_p=2$。R4 给出 $\dim W_p=2$，所以 (1) 中 $D_p=0$。R1 的有限性等价条件给出 $\Sha[p^\infty]$ 有限。

反过来，若该初级部分有限，则 $D_p=0$，由 (1) 得 $\dim S_p=2$。引理 1 表明 restriction 已在 $W_p$ 上非零，故 (7) 给出 $\kappa_p\ne0$。这证明 (8)。

在等价条件成立时，(4) 给出 $S_p^0=\mathbb Q_pv_p$；而 $\kappa_p\in S_p^0$ 非零。因此存在唯一非零标量 $A_p$ 满足 (9)。$\square$

## 4. 显式点路线尚缺的独立比较

命题 3 的式 (9) 是在等价条件已经成立之后的结论，不能循环地拿它证明同一有限性。若要用 $P,Q$ 给出新的有限性证明，足够另行证明：对无穷多个所列 $p$，存在一个已证明非零的标量 $A_p$，使
$$
\boxed{\quad
\kappa_p=A_p\bigl(\ell_p(Q)P-\ell_p(P)Q\bigr),\qquad A_p\ne0.
\quad}
\tag{10}
$$
这里需要补足两个内容：首先，$\kappa_p$ 必须落在已知的 $W_p$ 直线上，而不是仅知属于可能更大的 $S_p^0$；其次，必须给出 $A_p$ 的独立非零性。若其表达式仍把所需二阶 $p$-adic $L$ 系数非零或 $\Sha[p^\infty]$ 有限作为输入，就未证明新的蕴含。

本文证明了 (4)、(8) 和满足条件后的 (9)，**没有证明 (10) 在无穷多个 $p$ 上无条件成立**。因此它给出了准确的研究接口，未完成课题的无穷素数目标。
