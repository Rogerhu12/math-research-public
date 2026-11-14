# R412：实际三块评价的整满射范围与完整第二余核

日期：2026-11-14。**状态：已证明。** 本篇直接计算 R335/R338 的实际评价像，在一个明确的线性次数范围给出整满射，而非只给来源导子的饱和。乘回原 $G_0$ 后，全部十三行及二十六条跨界带都保留，Smith 因子及真正 $C_2$ 可以完整写出。该范围的双接触对偶实际上为零，不能据此判定两个原中央非零；后续非平凡配对必须在较小来源预算内研究。

## 1. 原整列、原三块与所需次数

沿用 R335/R338 的
$$
p=6s-1>83,\qquad1\le\ell<s-13,\qquad L=2s+\ell,
$$
$$
\Gamma_L=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\quad a_p\in\mathcal O^\times,
$$
$$
\mathscr R_{\rm phys}=g(w)e_2(a_p\epsilon),\qquad
t(w)=-bw+\cdots,\quad g(0)=1,
\quad b\in\mathcal O^\times.
\tag{1}
$$
$g,t$ 是原实际整正规化；全部所读三块均处于已付整性窗。$b=17$ 的原模型或 R403 同构后的 $b=1$ 模型均适用，不能只改其中一个 Gaussian 常数。

取同一旧来源
$$
\mathcal V_{\le D}=\bigoplus_{n=0}^{D}
\mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=\frac{(th_7)^{A_n}(t-1)^{B_n}}{(1+8t)^{C_n}},\quad
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2.
\tag{2}
$$
避免与 $B_n$ 强迫零指数相混，定义每个来源部分可用的最高首阶
$$
\boxed{b_n=A_n+e_{n+1}.}
\tag{3}
$$
$b_n$ 严格递增，并且 $b_n\ge4n+3$。后一个界可由十二个剩余类核定：
$$
(b_n-4n)_{0\le n<12}=(4,4,5,3,5,4,6,4,5,5,7,4),
\quad b_{n+12}=b_n+50.
\tag{4}
$$

令
$$
\rho(r)=\min\{n\ge0:b_n\ge r\},
$$
$$
\boxed{D_*=
\max\{1+\rho(s-1),\ 2+\rho(\ell-1)\}.}
\tag{5}
$$
这是一个显式充分阈值，不声称是实际评价满射的最小次数。

## 2. 真实整评价满射

记原相对评价为
$$
J_D:\mathcal V_{\le D}\longrightarrow\Gamma_L,
\qquad\Phi\longmapsto\Phi(\mathscr R_{\rm phys},t(w)).
\tag{6}
$$

**定理 1。** 若 $D\ge D_*$，则 (6) 是整满射；它有由原实际基列选出的 $L\times L$ 单位子式。

**证明。** 模 $p$ 后，$w^s=0$，但 $\epsilon$ 的两条非零块仍保留。把目标按普通 $w$ 次数过滤。在第 $r$ 个分次上，$0\le r<s$，目标维数是
$$
m(r)=\begin{cases}3,&r<\ell,\\2,&\ell\le r<s.\end{cases}
\tag{7}
$$
对应基为 $w^r,w^r\epsilon$，以及存在时的 $w^r\epsilon^2$。这重新排列的是整个目标基，没有删除高块。

固定 $r$，取 $n_0=\rho(r)$，再取 $m(r)$ 个相邻的实际次数
$$
n_0,n_0+1,\ldots,n_0+m(r)-1.
\tag{8}
$$
(5) 保证它们均不超过 $D$。每个所选次数都有真实基列
$$
\Phi_{n,r}=\mathscr R^nq_n(t)t^{r-A_n},
\tag{9}
$$
因为 $b_n\ge r$ 保证上界 $r-A_n\le e_{n+1}$。下界也成立：$r=0$ 时所选次数至多二，$A_0=A_1=A_2=0$；$r\ge1$ 时 $n_0\le r$（由 (4)），故
$$
A_n\le A_{n_0+2}\le\left\lfloor\frac{r+3}{4}\right\rfloor\le r.
$$
所以 (9) 没有用任何额外全纯角列，也没有负的 $t$ 次幂。

在同一个真实正规化中，(9) 的像从 $w^r$ 起。其该阶首项为
$$
\gamma_{n,r}w^r e_2(na_p\epsilon),
\quad
\gamma_{n,r}=(-b)^r(-1)^{B_n}7^{A_n}\in\mathcal O^\times.
\tag{10}
$$
所有 $g$ 的非恒定系数、$t$ 的高项、角纠正和普通系数进位都只进入更高 $w$ 阶；在模 $p$ 时普通 $w^s$ 项为零，而 (10) 中的真实 Gaussian 块没有被删除。特别没有把 $T$ 的 charge 改为一；当前所取的确全是旧的 $j=0$ 原列。

对 $m(r)=2$，(10) 的两个首项列在 (7) 上的行列式是
$$
a_p\prod_n\gamma_{n,r}\in\mathcal O^\times.
$$
对 $m(r)=3$，行列式是
$$
\frac{a_p^3}{2}\prod_n\gamma_{n,r}
\prod_{0\le i<j\le2}(j-i)
=a_p^3\prod_n\gamma_{n,r}\in\mathcal O^\times.
\tag{11}
$$
相邻次数的差只是一或二，所以无需假设整个 $D<p$。选取的列在不同 $r$ 上也各不相同，因为其真实首阶不同。总列数为 $\sum_rm(r)=2s+\ell=L$。

按 $r$ 从小到大排列这些列及目标基，得到一个分块下三角矩阵；各对角块由 (11) 为单位。故选出的原整矩阵方子式模 $p$ 可逆，其行列式在 $\mathcal O$ 中为单位。这个实际整方阵的逆同时处理所有更高 carry，给 (6) 的整右逆。不是只在模 $p$ 上逐阶消元后忽略高精度项。$\square$

由于 R406 的 $\mathcal W_{D,J}$ 包含全部 $j=0$ 原列，任何 $0\le J\le16$ 的实际两来源扩源评价在同一范围也整满射。无需给新 $T^j$ 列附加中央零假设。

一个便于核定的统一选择是
$$
D_0=\lfloor(s-1)/4\rfloor+2.
\tag{12}
$$
由 (4)，$b_{D_0-2}\ge s-1$，故 $D_0\ge D_*$。又
$$
f_{D_0}=\lfloor9D_0/2\rfloor+4
\le(9s+95)/8<6s-1=p.
\tag{13}
$$
因此 R408 的整个两来源导子饱和与本篇的实际评价满射可以同时使用；旧 R406 的十七倍充分界不覆盖这个自然线性次数范围。

## 3. 乘回原G0后的全部Smith因子

原完整矩阵仍为
$$
M=m_{13}J_D:\mathcal V_{\le D}\longrightarrow\Gamma_{L+13},
\quad m_{13}(F)=w^{13}F.
\tag{14}
$$
在实际整基 $e_r=w^r/p^{\lfloor r/s\rfloor}$ 中，
$$
m_{13}(e_r)=p^{\delta_r}e_{r+13},\quad
\delta_r=\lfloor(r+13)/s\rfloor-\lfloor r/s\rfloor.
\tag{15}
$$
因为 $s>13$ 且 $L+13<3s$，恰好两条完整区间
$$
r\in[s-13,s-1]\ \text{或}\ [2s-13,2s-1]
\tag{16}
$$
给 $\delta_r=1$，各有十三项。其余 $L-26$ 项的指数为零。

**定理 2。** 在定理 1 的范围，$M$ 的像准确是 $w^{13}\Gamma_L$，非零 Smith 因子恰为
$$
\boxed{\underbrace{1,\ldots,1}_{L-26},
\quad\underbrace{p,\ldots,p}_{26}.}
\tag{17}
$$
其余核的自由部分秩为十三，来源核自由秩为 $\operatorname{rank}_{\mathcal O}\mathcal V_{\le D}-L$。若 $N$ 表示来源秩，对每个 $h\ge1$，
$$
\boxed{\operatorname{length}_{\mathcal O}\ker(M\bmod p^h)
=h(N-L)+26.}
\tag{18}
$$

**证明。** $J_D$ 已整满射，故像等于 $m_{13}\Gamma_L$；它的整右逆使 $M$ 与 $m_{13}$ 加零列整等价。(15)–(16) 给全部非零因子。目标有 $L+13$ 行而秩为 $L$，所以有十三个自由余核方向；不是把来源维数误当目标长度。每个单位因子没有模 $p^h$ 核，每个 $p$ 因子贡献长度一，每个零列贡献长度 $h$，得到 (18)。$\square$

R335 的原始矩阵是 $c_*U_0M$，其中 $c_*U_0$ 为整个目标中的整单位。因为 $w^{13}\Gamma_L$ 是 $\Gamma_{L+13}$ 中的理想，乘该单位保持这个像。因此原 $P_{134}/U_0$ 和 charge 四十均未改变 (17)–(18)，也未删除任何边界。

## 4. 真正C2与同源双接触

按 R338 的定义
$$
C_1(M)=\operatorname{coker}\bar M,
\qquad C_2(M)=C_1(M)/\beta_1^M(K_1(M)).
\tag{19}
$$
由 (17)，$C_1$ 的二十六条有限方向恰是 $p$ Smith 因子的约化；首 Bockstein 将它们全部支付。因此
$$
\boxed{C_2(M)=\bigoplus_{r=0}^{12}k\,[e_r].}
\tag{20}
$$
这十三条是原完整目标的最初十三行，原矩阵在这些行恒为零。

更明确地，一个实际模 $p^2$ 左核 $\lambda_2$ 在 (17) 的单位行上为零，在 (16) 对应目标行上是 $p$ 倍，在最初十三行可任意。因此其约化 $\lambda_0$ 精确只支撑于 $r=0,\ldots,12$；这些任意约化也都可提升。此结论同样适用于原 $c_*U_0M$，因为其像未变。

于是所有真实第二 Bockstein
$$
d_2^M:\ker\beta_1^M\longrightarrow C_2(M)
$$
都为零：它们由实际 $MP/p^2$ 计算，而其最初十三行仍全为零。这里已商去整个首提升像，没有误用未商的 $C_1$。

将同一个实际 $P_2$ 和可提升左核代入 R406.(23) 的两个耦合向量 $(q,r)$，所有出现的 $\bar\lambda_{1,j+13}$、$\bar\lambda_{2,j+13}$ 都在 (20) 之外，所以
$$
\boxed{q=0,\qquad r=0.}
\tag{21}
$$
这是真实同源双线性像的计算，不是让两个向量自由变化的环境矩阵结论。若使用 R406 的多一行目标或次数三扩张，按其新的 $\ell_+$ 和 $D$ 核 (5)，同一证明继续给 (20)–(21)。

## 5. 两条完整中央仍保留的位置

(20) 解释了一个具体预算边界：将来源加大至 (5) 时，实际有限目标只剩原点十三行的自由余核；它不再有可读取 R403 两条 forcing 的二阶对偶。源上的整饱和和环境接触算子的原始性都不能改变 (21)。

这没有证明原 $S,T$ 的中央导数为零或非零。R403 的两个完整基准 $B_S,B_T$、全部 wrap，以及其与同一个低轴修正的合计仍是另一项需要证明的身份。若后续比较使用非零的实际 $C_2$ 接触，必须在 (5) 以下的来源预算中完成，并保留原行数与极零成本；不能在把来源扩大至整满射后还调用一个已经消失的非平凡对偶。

因此本篇支付了完整实际像的一段范围，并指出下一段要计算的明确有限对象，而不以某条路线的失效作为主课题完成。

## 依据

- R335 的完整 canonical 整基、实际公共 $G_0$ 与全深矩阵。
- R338 的原三块公式、完整十三行运输及真正第二余核定义。
- R403/R406 的共同两来源与不同 Gaussian charge；本篇的满射子式只取其中真实 $j=0$ 部分。
- R408 的全特征 $p$ 来源核，用于 (13) 的同时适用范围。

脚本 [check-r412-actual-staircase-surjectivity.py](../scripts/check-r412-actual-staircase-surjectivity.py) 核十二个 floor 类和实际选列条件。正文的块三角单位子式给全参数证明，无须目标素数扫描。
