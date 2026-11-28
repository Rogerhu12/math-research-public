# R12 附录：首位符号对称、实际平方分式的零因子与单前向列的直接超不变桥

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：下列有界零因子构造与实际强列充分条件均已证明。** 本文直接产生所选原 Haar 尾自身的非平凡超不变空间，包括最初原算子 $m_0=0$，无需先返回上一尾。实际平方分子或列紧性仍未构造；本文不声称普通 ISP 已完成。

## 1. 原全空间的符号对称及连续双线性形式

固定原 Haar 尾 $C=A^{(m_0)}$，在 $H=L^2(\mathbb Z_2,\mu)$ 上写为
$$
(Cf)(y)=w_{m_0}(y)f(y-1).
$$
令
$$
U f(y)=(-1)^{y\bmod2}f(y),\qquad
\gamma(F)=UFU.
\tag{1}
$$
$U=U^*=U^{-1}$。加减一翻转首位，而权乘子与 $U$ 交换，故原算子准确满足
$$
UCU=-C,\qquad \gamma^2=\mathrm{id}.
\tag{2}
$$
若 $F\in C'$，共轭其交换式便知 $\gamma(F)\in C'$；所以 $\gamma$ 是原全交换子代数上的复线性、等距、自反代数自同构。

以下所有转置都使用 [R24 §1](R24-complex-symmetric-moments-and-escape.md) 的原反射共轭
$$
(Jf)(y)=\overline{f(-1-y)},\qquad
[x,y]=\langle x,Jy\rangle
=\int_{\mathbb Z_2}x(s)y(-1-s)\,d\mu(s).
\tag{3}
$
内积第一变量线性。

这是全 $H$ 上连续、非退化、对称的复双线性形式，且
$$
|[x,y]|\le\|x\|\|y\|.
$$
R24 的原循环复对称证明给出
$$
F^*=JFJ,\qquad [Fx,y]=[x,Fy]\quad(F\in C',\ x,y\in H),
\qquad C'\ \text{交换}.
\tag{4}
$$
因此 (4) 同时适用于 $\gamma(F)$ 及下面的所有有界线性组合。没有在未知闭根的域上使用这个换位，也没有把一般循环性单独当成交换子交换的理由。

本文称闭子空间超不变，是指它被全部 $F\in C'$ 保持。

## 2. 同一有界平方分式直接给两个非零零因子

**定理 2.1。** 若存在有界 $P,V\in C'$，满足
$$
P\ne0,\qquad V^2=CP^2,
\tag{5}
$$
则原 $C$ 有非零真闭超不变子空间。若 $P$ 是 quasiaffinity，则可以明确取
$$
E=\gamma(V)P,\qquad F=V\gamma(P),\qquad
K_\pm=E\pm iF,
\tag{6}
$$
并有
$$
\boxed{K_+\ne0,\qquad K_-\ne0,\qquad K_+K_-=0.}
\tag{7}
$$
特别，
$$
\boxed{
0\ne\overline{\operatorname{Ran}K_+}
\subseteq\ker K_-\ne H
}
\tag{8}
$$
是实际全空间中的有界算子像与核。

**证明。** 若 $P$ 不单射，则 $\ker P$ 已是非零真闭超不变空间；若 $P$ 单射但像不稠密，则 $\overline{\operatorname{Ran}P}$ 具有同样性质。这里 $P\ne0$，且 (4) 保证所有交换子保持这些空间。

余下可设 $P$ 单射稠值。原 $C$ 单射稠值，所以 $CP^2=V^2$ 单射稠值，进而 $V$ 也单射稠值。其 $\gamma$ 变换具有相同性质，故 (6) 中 $E,F$ 都是非零 quasiaffinity。

利用 (2)、(4)、(5)，所有乘法在原有界代数中给出
$$
E^2=\gamma(V)^2P^2
=-C\,\gamma(P)^2P^2
=-F^2.
\tag{9}
$$
因此 $(E+iF)(E-iF)=E^2+F^2=0$。

还必须排掉其中一个因子本来为零的可能。由 $\gamma^2=\mathrm{id}$ 及交换性，
$$
\gamma(E)=F,\qquad\gamma(F)=E,\qquad
\gamma(K_\pm)=\pm iK_\mp.
\tag{10}
$$
若任意一个 $K_\pm=0$，(10) 使两个都为零，再将它们相加、相减便得 $E=F=0$，与上述单射性矛盾。故 (7) 完整成立。

(7) 给 (8)；两个 $K_\pm$ 均属于 $C'$，又 $C'$ 交换，所以其像闭包与核都被全部 $C'$ 保持。证毕。

此处没有对 $P^{-1}V$ 作任何未付的乘积或域相交。与[同一最大商闭根定理](R12-appendix-same-flat-denominator-maximal-stable-root-and-all-flag-cores.md)相比，新增的是原尾内部的明确有界零因子及 (8)，而非重复最大商的闭性。

## 3. 一个首位本征源上的强列也直接给原超不变空间

**定理 3.1。** 设 $A_n\in C'$ 每个各自有界，并且
$$
A_n^2\longrightarrow C\quad\text{强}.
\tag{11}
$$
取任意非零 $p\in H$，满足 $Up=\varepsilon p$，其中 $\varepsilon\in\{1,-1\}$。若某个子列
$$
A_{n_j}p\longrightarrow v\quad\text{强},
\tag{12}
$$
则同一个原 $C$ 有非平凡闭超不变子空间。这里不要求 $p$ 循环，也不要求整个 $(A_n)$ 一致有界。

**证明。** 定义实际有界算子
$$
H_n^\pm=\gamma(A_n)\pm iA_n.
$$
由 (2)、(4)、(11)，
$$
H_n^+H_n^-=\gamma(A_n^2)+A_n^2\longrightarrow0
\quad\text{强}.
\tag{13}
$$
并且
$$
\gamma(H_n^+)=iH_n^-,\qquad
H_n^+p=(\varepsilon U+iI)A_np,\qquad
H_n^-p=-i\varepsilon U H_n^+p.
\tag{14}
$$
注意 $\varepsilon U+iI$ 是 $\sqrt2$ 倍的酉算子。

先设 $v\ne0$。则沿同一子列，两列均强收敛：
$$
H_{n_j}^+p\to f=(\varepsilon U+iI)v\ne0,\qquad
H_{n_j}^-p\to g=-i\varepsilon Uf\ne0.
\tag{15}
$$
对任意固定 $B\in C'$，必须按全空间连续形式 (3) 作如下完整换位：
$$
[BH_n^+p,H_n^-p]
=[H_n^-BH_n^+p,p]
=[B(H_n^-H_n^+)p,p]\longrightarrow0.
\tag{16}
$$
第一步使用 $H_n^-\in C'$ 的 (4)，第二步使用原交换子交换性。右边由 (13) 趋零；左边由 (15) 的两次强收敛及 (3) 的连续性趋于 $[Bf,g]$。故
$$
[Bf,g]=0\quad(B\in C').
$$
于是
$$
\mathcal M=\overline{\{Bf:B\in C'\}}
$$
含非零 $f$，被 $C'$ 保持，并包含于 $(Jg)^\perp$，故为真闭超不变空间。

若 $v=0$，不能丢掉该情况。对所有 $B\in C'$，(4) 给
$$
[BA_{n_j}p,A_{n_j}p]=[BA_{n_j}^2p,p]
\longrightarrow[BCp,p].
$$
左边由 (12) 趋零。因此
$$
\mathcal M=\overline{\{BCp:B\in C'\}}\subseteq(Jp)^\perp
$$
也是非零真闭超不变空间：$Cp\ne0$ 来自原单射性。证毕。

整个证明只涉及原有界 $A_n,H_n^\pm,B$。未调用一个极限闭根与其 $\gamma$ 变换的域相交，亦未将弱收敛的两列通过双线性乘积。

## 4. 原 $P\Omega$ 一列的准确首位归约

设 $P\in C'$ 是任意已付的 quasiaffinity。记 $\Omega=1$。取原正规化幂 $N_0=C/\|C\|$ 及
$$
V_0=(I-N_0)(I+N_0)^{-1},\qquad
F_+=\frac{I+V_0}{\sqrt2}=\sqrt2\,(I+N_0)^{-1}.
\tag{17}
$$
这些都是原范数多项式代数中的有界算子；$N_0$ 拟幂零，所以 $F_+$ 为有界单位。

准确真空来源是
[R267 §1，式 (1.3)](R267-disjoint-odd-walsh-block-accretive-regularizers-and-contractive-strong-units.md)：
$$
V_0\Omega=\chi_0.
$$
因此
$$
F_+\Omega=e_+:=\frac{\Omega+\chi_0}{\sqrt2},\qquad Ue_+=e_+.
\tag{18}
$$
这里保留实际 $V_0$ 的全部 carry，并非有限头压缩或仅由 $\Omega$ 循环性猜出的前像。

置
$$
\widehat p=P\gamma(P)e_+.
\tag{19}
$$
$P\gamma(P)$ 单射，故 $\widehat p\ne0$；又 $\gamma(P\gamma(P))=P\gamma(P)$，所以 $U\widehat p=\widehat p$。同一个实际来源满足
$$
\boxed{
A_n\widehat p
=\gamma(P)F_+\,A_nP\Omega.
}
\tag{20}
$$
右侧仅施加固定的原有界算子；因此 $A_{n_j}P\Omega$ 有强极限时，(20) 也有强极限。定理 3.1 直接适用，即使该变换后的极限为零。

由此得到
$$
\boxed{
A_n^2\to C\text{ 强},\quad
P\in C'\text{ 为 quasiaffinity},\quad
A_{n_j}P\Omega\text{ 强收敛}
\ \Longrightarrow\
C\text{ 有非平凡闭超不变空间}.
}
\tag{21}
$$
(21) 对 $m_0=0$ 同样成立。它增强了[单前向列闭根定理](R267-appendix-single-forward-column-compactness-and-original-stable-root.md)在指定有界分母源上的直接原格返回；不否定该稿的两列闭根及真实稳定域结论。

特别，已构造的同一 $P_t$ 可取作 $P$。实际 $Y_N^2=CD_N\to C$ 强*，故只需同一 $Y_NP_t\Omega$ 的强子列。(21) 同样适用于实际 $A_n=CW_n$，只要已经证明 $CW_n^2$ 是强*趋于 $I$ 的收缩。这里仍不把相应列预算当成已付。

## 5. 同一相容族还给明确的算子范数乘积余项

对[相容有理根族](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)及其[实际复相位版本](R267-appendix-complex-phase-factors-finite-changes-and-log-branch-signs.md)，写
$$
Z_\nu=(1-\zeta_\nu)F_\nu+
\zeta_\nu e^{i\theta_\nu}C/c,\qquad
0<\zeta_\nu\le\epsilon_\nu/8,\qquad c=\|C\|.
$$
每个 $F_\nu$ 只含偶数次原幂，故 $\gamma(F_\nu)=F_\nu$，从而
$$
\|\gamma(Z_\nu)-Z_\nu\|\le2\zeta_\nu.
\tag{22}
$$
对合法整数尾
$$
D_N=\operatorname*{SOT^*\!-\!lim}_{K\to\infty}
\prod_{\nu=N}^{K-1}Z_\nu^{d_\nu/M_N},
\qquad
b_N=\frac1{M_N}\sum_{\nu\ge N}d_\nu\epsilon_\nu,
$$
所有有限因子及其 $\gamma$ 变换都是收缩。逐次幂与乘积望远镜、再取强极限，给
$$
\boxed{
\|D_N-\gamma(D_N)\|
\le\frac2{M_N}\sum_{\nu\ge N}d_\nu\zeta_\nu
\le b_N/4.
}
\tag{23}
$$
所以取 $H_N^\pm=\gamma(Y_N)\pm iY_N$，有完整同源恒等式及范数界
$$
\boxed{
H_N^+H_N^-=C(D_N-\gamma(D_N)),\qquad
\|H_N^+H_N^-\|\le c\,b_N/4\longrightarrow0.
}
\tag{24}
$$
这是两个真实全尾算子的乘积余项，比这里所需的强零更定量；未删除未来尾积，也未将相位版本当成正锥保持算子。由 $\gamma(H_N^+)=iH_N^-$，两因子范数相等；每个都非零，否则同时为零会迫 $Y_N=0$。

(24) 仍不单独给 (15) 的强子列或某个非零极限因子。实际后继必须支付 (20) 中的原列来源，或直接构造 (5) 的原有界分子。奇切口、无限相位和一般非固定分母的来源费用均未在本稿自动关闭。
