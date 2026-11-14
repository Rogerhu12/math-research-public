# R267 附录：所有 A 幂的共同有界倍数与 UHF 外的收缩强单位

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf8c51d 复核。AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的中间结果。** 本文在原 Haar 表示中构造非零收缩 $P\in A'$，使每个 $r\ge1$ 都有实际有界 $R_r\in A'$ 满足 $P=A^rR_r$，同时存在 $W_n\in\mathcal A$ 使 $PW_n$ 为收缩并强*趋于 $I$。这些共同倍数在 $A'$ 中具有同范数强*逼近能力，但与原 UHF 代数仅交于零。本文没有证明其中某个收缩强单位同时是慢 $S_N$ 或 $S_Y$ 的有界倍数，也没有为假想正常湮灭者付指定配对域。

## 1. 已有结果与本稿新增的量词

记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\qquad
\mathfrak C=A',
\qquad
\mathfrak U=\overline{\bigcup_m M_{2^m}}^{\|\cdot\|}.
$$
沿用原 Haar 空间、Walsh 真空 $1$、实际 $N_j,Y_j,V_j$。

[R23](../results/R23-strong-star-polynomials-and-tail-block-projections.md) 已构造多项式
$$
E_\ell=e_\ell(A),\qquad
\|E_\ell\|\le1,\qquad
E_\ell\longrightarrow I\quad\text{强*},
\tag{1.1}
$$
其最低非零 $A$ 次数 $b_\ell$ 趋于无穷。特别，对每个固定 $r$，充分大的 $E_\ell$ 准确属于 $A^r\mathcal A$。

[R44](../results/R44-critical-schur-division-and-kernel-regularity.md) §5 已证明
$\bigcap_r\operatorname{Ran}A^r$ 在 $H$ 中稠密。
本稿要构造的是同一个有界交换子 $P$ 和全部有界因子 $R_r$，以及这个 $P$ 的收缩强单位；不把原来的向量空间稠密性当成已有的算子因式。

定义代数理想
$$
\boxed{
\mathfrak F_A=\bigcap_{r\ge1}A^r\mathfrak C.
}
\tag{1.2}
$$
这里每个包含 $P\in A^r\mathfrak C$ 都要求某个全空间有界因子，不只是形式整除或值域闭包。

## 2. 参数为零的真实平顶块

对有限连续位块 $F=[m,m+q)$，定义
$$
T_F=\frac2{q+2}\sum_{j\in F}Y_j,
\qquad
T_F^0=\frac2{q+2}\sum_{j\in F}E_j.
\tag{2.1}
$$
$Y_j=N_j(I+N_j)^{-1}=(I-V_j)/2$，所以 $T_F\in\mathcal A$。
纯局部范数公式给
$$
\|T_F^0\|\le\frac{q+1}{q+2}.
\tag{2.2}
$$
真实关系
$$
\|Y_j-E_j\|\le4\eta_j,\qquad
\eta_j\le e^{-770\,16^j}
$$
于是给
$$
\|T_F-T_F^0\|
\le\frac8{q+2}\sum_{j\in F}\eta_j
\le8e^{-770\,16^m}.
\tag{2.3}
$$
故只要
$$
8e^{-770\,16^m}\le\frac1{q+2},
\tag{2.4}
$$
就有 $\|T_F\|\le1$。这是实际算子范数预算。

本构造选用 $Y_j$，使真空列准确为有限 Walsh 向量：
$$
\boxed{
t_F=T_F1
=\frac{q-\sum_{j\in F}\chi_j}{q+2}.
}
\tag{2.5}
$$
因此
$$
\mu_q:=\langle t_F,1\rangle=\frac q{q+2},
\qquad
\alpha_q:=\|t_F\|^2=\frac{q^2+q}{(q+2)^2}.
\tag{2.6}
$$
尤其
$$
1-\mu_q=\frac2{q+2}\le\frac2q,
\qquad
0\le1-\alpha_q=\frac{3q+4}{(q+2)^2}\le\frac3q.
\tag{2.7}
$$
$t_F$ 是非负普通函数；这不表示 $T_F$ 是自伴正算子。

若 $F_1,\ldots,F_n$ 互不交，则准确有
$$
T_{F_1}\cdots T_{F_n}1=t_{F_1}\cdots t_{F_n}.
\tag{2.8}
$$
因为 (2.5) 中每个字符只用本块位，而不同位的实际 $V_j$ 交换，
$V_{J_1}\cdots V_{J_n}1=\chi_{J_1\cup\cdots\cup J_n}$。
(2.8) 仅用于真空列，不作为全算子乘法同态。

## 3. 非零前向乘积及其收缩尾积

取
$$
q_\nu=2^{\nu+6},\qquad
\sum_{\nu\ge1}q_\nu^{-1}=\frac1{64}.
\tag{3.1}
$$
递归选择依次后移且互不交的块
$F_\nu=[m_\nu,m_\nu+q_\nu)$，使每块满足 (2.4)。
记
$$
T_\nu=T_{F_\nu},\qquad t_\nu=t_{F_\nu},\qquad
P_n=\prod_{\nu=1}^nT_\nu.
$$
每个 $P_n$ 是 $\mathcal A$ 中的收缩。其准确真空列为
$$
h_n=P_n1=\prod_{\nu=1}^nt_\nu.
$$
独立块给
$$
\|h_n\|^2=\prod_{\nu\le n}\alpha_{q_\nu},
\qquad
\langle h_n,1\rangle=\prod_{\nu\le n}\mu_{q_\nu}.
$$
对 $k>n$，
$$
\|h_k-h_n\|^2
=
\left(\prod_{\nu\le n}\alpha_{q_\nu}\right)
\left(
\prod_{n<\nu\le k}\alpha_{q_\nu}
+1-2\prod_{n<\nu\le k}\mu_{q_\nu}
\right).
\tag{3.2}
$$
由 (2.7) 的两个可和亏损，右侧随 $n\to\infty$ 一致趋零。
所以 $h_n\to h$ 于 $H$，且
$$
\boxed{
\|h\|^2\ge1-3\sum_\nu q_\nu^{-1}=\frac{61}{64},
\qquad
\langle h,1\rangle\ge1-2\sum_\nu q_\nu^{-1}=\frac{31}{32}.
}
\tag{3.3}
$$

$1$ 对 $\mathcal A$ 循环。对任意多项式 $p$，
$$
P_np(A)1=p(A)h_n\longrightarrow p(A)h.
$$
统一收缩界因而给全 $H$ 上的强极限
$$
P_n\longrightarrow P\in\mathfrak C,\qquad
\|P\|\le1,\qquad P1=h\ne0.
\tag{3.4}
$$

对每个固定 $n$，同一论证给实际尾积
$$
Q_n=\operatorname*{SOT-lim}_{k\to\infty}\prod_{\nu=n+1}^kT_\nu,
\qquad \|Q_n\|\le1,
\qquad P=P_nQ_n.
\tag{3.5}
$$
其真空列由对应的尾部普通函数乘积给出。(2.7)、(3.2) 使
$Q_n1\to1$，故
$$
Q_n\longrightarrow I\quad\text{强收敛}.
$$
因为 $Q_n$ 都为收缩，这自动加强为强*收敛。准确地，
$$
\|(Q_n^*-I)x\|^2
\le2\|x\|^2-2\operatorname{Re}\langle Q_n^*x,x\rangle
\longrightarrow0.
\tag{3.6}
$$

## 4. 每个有限积是一个 A 幂乘单位

固定 $\nu$。在 $A$ 的有限有理演算中，$Y_j$ 的最低项为
$A^{2^j}/d_j$，其中 $d_j=\|A^{2^j}\|>0$。
因此
$$
\boxed{
T_\nu=A^{2^{m_\nu}}U_\nu,\qquad
U_\nu\in\mathcal A\text{ 可逆}.
}
\tag{4.1}
$$
其单位常数值为 $2/[(q_\nu+2)d_{m_\nu}]\ne0$。
所有分母都是 $I+N_j$ 的单位。
$A$ 拟幂零，故这个有限有理函数除去最低幂后的非零常数项确实给
$\mathcal A$ 中的有界逆；没有对无限慢级数作这样的除法。

置
$$
k_n=\sum_{\nu=1}^n2^{m_\nu},
\qquad
U^{[n]}=\prod_{\nu=1}^nU_\nu.
$$
则
$$
P_n=A^{k_n}U^{[n]},
\qquad U^{[n]}\in\mathcal A\text{ 可逆},
\qquad k_n\to\infty.
\tag{4.2}
$$
由 (3.5)，给任意 $r\ge1$，选 $n$ 使 $k_n\ge r$，并定义
$$
R_r=A^{k_n-r}U^{[n]}Q_n\in\mathfrak C.
$$
这是实际有界算子，而且
$$
\boxed{P=A^rR_r=R_rA^r.}
\tag{4.3}
$$
所以 $0\ne P\in\mathfrak F_A$。

特别
$$
PH\subseteq\bigcap_{r\ge1}\operatorname{Ran}A^r,
\qquad
A^{-r}P=R_r
$$
为全域有界算子。不同 $r$ 的范数没有统一上界；本文也不从这一包含单独推导连续性、次数指数矩或一般闭乘子图范数；闭域上的图核心另由第 6.1 节的强单位论证给出。

## 5. 同一 P 的收缩强*单位

使用 (1.1) 的固定序列 $E_\ell$。
为每个 $n$ 选择 $\ell(n)\ge n$，使其最低非零次数
$b_{\ell(n)}\ge k_n$。于是准确有某个多项式 $B_n$ 满足
$$
E_{\ell(n)}=A^{k_n}B_n(A).
$$
令
$$
W_n=(U^{[n]})^{-1}B_n(A)\in\mathcal A.
\tag{5.1}
$$
则
$$
P_nW_n=E_{\ell(n)},
\qquad
PW_n=Q_nE_{\ell(n)}.
\tag{5.2}
$$
这里 $W_n$ 不是 $P_n$ 的有界逆：$P_n$ 含非零 $A$ 幂。
它是把 $P_n$ 准确送到既有收缩近似单位的有界右因子。

由 (1.1)、(3.6) 和统一收缩界，
$$
\boxed{
\|PW_n\|\le1,\qquad
PW_n\longrightarrow I\quad\text{强*}.
}
\tag{5.3}
$$
这同时给出：

1. $P$ 在整个 $H$ 上单射、像稠密。
2. $h=P1$ 循环，因为 $W_nh=PW_n1\to1$。
3. 对每个有限放大及任意闭 $A^{(d)}$ 不变旗
   $N\subset M$，诱导的 $P_{M/N}$ 单射、像稠密。

第三点中，所有 $W_n\in\mathcal A$ 保持旗，$P$ 是有界强多项式极限也保持旗；
(5.3) 下降为商上的收缩强单位。
若 $P_{M/N}x=0$，则这些单位全杀 $x$，迫 $x=0$；
像稠密由同一单位极限给出。

此外 $P$ 拟幂零：从任一 (4.3)，
$$
\|P^l\|^{1/l}
\le\|A^{rl}\|^{1/l}\|R_r\|\longrightarrow0.
\tag{5.4}
$$

## 6. 共同倍数理想在 A' 内的逼近能力

$\mathfrak F_A$ 是 $\mathfrak C$ 的代数理想，因为全部因子交换。
对任意 $F\in\mathfrak C$，
$$
PW_nF\in\mathfrak F_A,\qquad
\|PW_nF\|\le\|F\|,
\qquad
PW_nF\longrightarrow F\quad\text{强*}.
\tag{6.1}
$$
因此 $\mathfrak F_A$ 的单位球强*稠密于 $\mathfrak C$ 的单位球。
特别，没有非零正常泛函能够在 $\mathfrak F_A$ 上全为零、却在
$\mathfrak C$ 上非零。

$A$ 对这个代数理想还有准确的双向整除：
$$
\boxed{A\mathfrak F_A=\mathfrak F_A.}
\tag{6.2}
$$
只需证明反向包含。若 $F=A R_1\in\mathfrak F_A$，则对每个 $r$ 还有
$F=A^{r+1}R_{r+1}$。原 $A$ 单射，故
$R_1=A^rR_{r+1}$；于是 $R_1\in\mathfrak F_A$。
这不证明任意慢非解析符号 $S$ 在 $\mathfrak F_A$ 上满射。

对每个闭 $A$ 不变 $M$，$PM$ 稠密于 $M$，且
$$
PM\subseteq
\bigcap_{r\ge1}\operatorname{Ran}(A|_M)^r.
\tag{6.3}
$$
这里 $R_r$ 保持 $M$：$R_r$ 由 $\mathcal A$ 元与其有界强极限构成。
因此 (6.3) 是限制空间内部的实际原像，不是只在环境空间中取逆。

### 6.1 全部幂的共同原像在闭域中的图核心

设 $T$ 为一个闭算子，$\operatorname{Dom}T$ 被 $\mathcal A$ 保持，且
$TFx=FTx$ 对 $F\in\mathcal A$、$x\in\operatorname{Dom}T$ 成立。
对每个 $Q\in\mathfrak C$，R88 给一致有界的多项式强逼近 $p_\lambda(A)\to Q$。
若 $x\in\operatorname{Dom}T$，则
$$
p_\lambda(A)x\to Qx,\qquad
Tp_\lambda(A)x=p_\lambda(A)Tx\to QTx.
$$
闭性因此给 $Qx\in\operatorname{Dom}T$、$TQx=QTx$。
特别，$P,W_n,R_r$ 全部保持这个实际域。

令 $K_n=PW_n$。对 $x\in\operatorname{Dom}T$，
$$
K_nx\to x,\qquad TK_nx=K_nTx\to Tx,
$$
而
$$
K_n\operatorname{Dom}T
\subseteq P\operatorname{Dom}T
\subseteq\bigcap_{r\ge1}A^r\operatorname{Dom}T.
$$
所以全部 $A$ 幂的共同域内原像是 $T$ 的图核心。
对有限多个闭算子的共同域，使用范数
$\|x\|+\sum_i\|T_ix\|$，同一个证明成立。
这没有证明 $PH\subseteq\operatorname{Dom}T$，也没有证明 $TP$ 全域有界。

## 7. 与原 UHF 代数的交恰为零

本节不仅排除 $\mathfrak F_A\cap\mathcal A$，还排除整个 UHF 交。

[R174](../results/R174-last-column-boundary-state-and-negative-integer-shift.md)
§4 给原 UHF 的等距 $*$ 表示
$$
\pi_-:\mathfrak U\longrightarrow B(\ell^2(\mathbb N_0)),
\qquad
B=\pi_-(A),
$$
其中
$$
Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),
\qquad
\ker B^r=\operatorname{span}\{e_0,\ldots,e_{r-1}\}.
\tag{7.1}
$$
等距性来自每个有限矩阵头的完整张量表示，随后按范数延拓；
本节不要求把任意 $A'$ 元送入该表示。

设 $F\in\mathfrak F_A\cap\mathfrak U$。
对每个 $r$，取有界 $R_r\in\mathfrak C$ 使 $F=A^rR_r=R_rA^r$。
在原空间中有正序
$$
F^*F\le\|R_r\|^2(A^*)^rA^r.
\tag{7.2}
$$
(7.2) 的左右两元都属于 $\mathfrak U$。
仅对这两个正元应用 $\pi_-$，得到
$$
\pi_-(F)^*\pi_-(F)
\le\|R_r\|^2(B^*)^rB^r.
\tag{7.3}
$$
所以 $\pi_-(F)$ 杀掉 $\ker B^r$。
由 (7.1) 的根向量旗稠密，$\pi_-(F)=0$。
$\pi_-$ 等距，故 $F=0$。

于是
$$
\boxed{\mathfrak F_A\cap\mathfrak U=\{0\}.}
\tag{7.4}
$$
特别本稿的非零 $P$ 不属于 $\mathfrak U$，因而也不属于
$\mathcal A$。证明从未定义 $\pi_-(R_r)$，没有跨表示运输未知交换子。

(6.1) 与 (7.4) 相容：这里是同范数强*逼近，不能提升为范数逼近。
它也显示不能给这些无限阶共同倍数直接使用原 UHF 的忠实形式系数演算。

## 8. 真空原像与指定正常配对仍需分别处理

这个 $P$ 也没有真空原像。由 (4.3)，$\operatorname{Ran}P\subseteq\operatorname{Ran}A$。
而 R44 的准确值域式为
$$
f\in\operatorname{Ran}A
\quad\Longleftrightarrow\quad
f/w\in L^2(\mathbb Z_2).
$$
在柱 $2^d\mathbb Z_2$ 上 $w\le\alpha_d$，故
$$
\int w^{-2}\,d\mu\ge2^{-d}\alpha_d^{-2}\longrightarrow\infty.
$$
最后由真实比率 $\alpha_{d+1}/\alpha_d\le e^{-77016^d}$ 保证。
因此 $1\notin\operatorname{Ran}A$，进而
$$
1\notin\operatorname{Ran}P.
\tag{8.1}
$$

对任意正常泛函 $\phi$，原 R244 固定真空表示仍可提出：
$$
\phi(PF)=B(Fh_\phi,1)\qquad(F\in A').
\tag{8.2}
$$
利用有限 Walsh 列及 R88 的有界强逼近，(8.2) 等价于
$$
\sum_{J\ {\rm finite}}|\phi(PV_J)|^2<\infty.
\tag{8.3}
$$
这是全部有限集合的平方和，不只是每个固定次数层的平方和。
方向 (8.3)$\Rightarrow$(8.2) 先由有限 Walsh Riesz 表示构造 $h_\phi$，
再由 R176 §6 的有限 Walsh 乘子范数稠密性延拓到 $\mathcal A$，最后以 R88 的一致有界强多项式逼近和正常性延拓到 $A'$；反向由
$B(V_Jh_\phi,1)=B(h_\phi,\chi_J)$ 和 Parseval 得到。

不能把 (8.2) 的第二向量换成 $P1$ 来免费获得正则化。
准确地，
$$
\phi(PF)=B(Fk,P1)\quad(F\in A')
$$
等价于原泛函本身已有
$$
\phi(F)=B(Fk,1)\quad(F\in A').
$$
一向由 $P$ 的 $C$ 对称性直接得到；
另一向将第一式中的 $F$ 换为 $FW_n$，使用
$PW_n\to I$ 的统一收缩界、正常性和强收敛即可。
虽然 $P1$ 循环，这种参考向量替换会取消所需的正则化作用。

若 $\phi$ 是非零正正常慢湮灭者，
$\phi(S\mathcal A)=0$，则 (8.2) 一旦成立，
先由 R88 将湮灭式延拓为 $\phi(SA')=0$。在 (8.2) 中取 $SF$，得到 $B(FSh_\phi,1)=0$ 对全部 $F\in A'$ 成立；由 $1$ 循环和交换子的 $C$ 对称性，$Sh_\phi=0$。$S$ 的原全空间单射性于是迫 $h_\phi=0$；
再测试 $W_n$ 与 (5.3) 矛盾。
本稿尚未由湮灭矩方程推出 (8.3)，也未证明
$P\in S A'$。共同全部 $A$ 幂的有界整除，不能替代这两个真正剩余的条件。

## 已证依赖和核对范围

- R23：最低次数趋于无穷的收缩多项式强*单位。本稿已全文核对，未发现其中有共同非零无限阶算子的构造。
- R44 §5：幂值域交的原向量稠密性；本稿增加一个共同有界交换子及全部旗子商的强单位。
- R174 §§4--5：等距 UHF 边界表示与准确根向量旗，只用于 (7.2)--(7.4) 中的正序。
- R267 第三附录：前向乘积方法；本稿各有限因子含 $A$ 幂、不具全空间有界逆，以 R23 单位取代有限逆积。
- R244、R88：只用于第 8 节指定正常矩接口；主构造不假设正常湮灭者存在或不存在。
