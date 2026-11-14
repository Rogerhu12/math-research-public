# R440：原单位商 H38 的最大来源子格与三个真实核边界

日期：2026-11-14。**状态：已证明。** 原 $H_{38}=T/S$ 在物理原点为单位，但它不能免费乘整个既定来源格。本篇给其最大合法子格，证明该子格整且 $p$ 饱和；允许 $SQ$ 在模 $p^r$ 核而不要求 $Q$ 自身在核时，新增部分准确是原像与三个指定边界的交。其长度至多 $r+2$，界在原整满射范围实际达到。$H_{38}$ 在这三个边界上是一个明确单位剪切。本篇没有把这个局部单位降成整个 $C_2$ 上的自由自同构，也没有用边界扩大替代原完整中央基准。

## 1. 同一原有限自由来源

保持 R406/R408/R434 的
$$
p=6s-1>83,\quad1\le\ell<s-13,\quad L=2s+\ell,
\quad T_0=L+13<3s,
$$
$$
a=p\kappa\in\mathcal O^\times,\quad\alpha=36/17,
\quad\nu=\alpha-1=19/17.
$$
为免与 $a$ 混淆，原角多项式记作
$$
\mathfrak a(t)=t(t-1)h_7(t),\qquad d=1+8t.
$$
来源函数域中
$$
S=\mathscr R\mathfrak a/7,\qquad
H_{38}=T/S=7T/(\mathscr R\mathfrak a).
\tag{1}
$$
令
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}/d^{C_n},\qquad
\mathcal V_n=\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}},
$$
$$
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2,
\qquad\mathcal W_{D,J}=\bigoplus_{n=0}^D\bigoplus_{j=0}^J\mathcal V_nT^j.
\tag{2}
$$
以下取 $D\ge1$、$0\le J\le15$。乘 $H_{38}$ 后仍在已付的十七个真实 Kummer 部分内，不借 $T^{17}$ 换掉一个指数或增加负径向列。

## 2. 最大可乘子格恰为原 S 的倍数

对 $n\ge1$，写
$$
\Delta A_n=A_n-A_{n-1},\quad
\Delta B_n=B_n-B_{n-1},\quad
\Delta C_n=C_n-C_{n-1}.
$$
三个差均为零或一。定义真正的角多项式
$$
\boxed{F_n=(th_7)^{1-\Delta A_n}
(t-1)^{1-\Delta B_n}d^{\Delta C_n}.}
\tag{3}
$$
准确有
$$
q_nF_n=\mathfrak a q_{n-1},\qquad
e_{n+1}-e_n-\deg F_n=\mathbf1_{2\mid n}.
\tag{4}
$$

**定理 1（最大整域）。** 在同一来源函数域中，准确有
$$
\boxed{\begin{aligned}
\{P\in\mathcal W_{D,J}:H_{38}P\in\mathcal W_{D-1,J+1}\}
&=S\mathcal W_{D-1,J}\\
&=\bigoplus_{n=1}^D\bigoplus_{j=0}^J
 \mathscr R^nq_nF_n\mathcal O[t]_{\le e_n}T^j.
\end{aligned}}
\tag{5}
$$
第二行忽略共同单位 $1/7$，因此是同一个整子模。此子模在 $\mathcal W_{D,J}$ 中 $p$ 饱和；乘 $H_{38}$ 将其整同构到 $T\mathcal W_{D-1,J}$。

**证明。** 对一个分量直接用 (1)、(4)：
$$
H_{38}(\mathscr R^nq_nP(t)T^j)
=7\mathscr R^{n-1}q_{n-1}\frac{P(t)}{F_n(t)}T^{j+1}.
\tag{6}
$$
$1,T,\ldots,T^{16}$ 及固定 $j$ 下各 $\mathscr R^n$ 的独立性已由 R408 支付。$n=0$ 项产生不允许的 $\mathscr R^{-1}$，不能与其他项相消；$n\ge1$ 的各目标分量也互不相混。因此 (6) 属于所列目标，当且仅当每个 $P=F_nQ$ 且 $\deg Q\le e_n$。

所有 $F_n$ 都有 $p$ 单位首项系数，分母仅有固定好位单位。多项式除法由此保证 $P/F_n$ 属于 $\mathcal O[t]$，没有只在分式域成立的来源。用
$f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4$ 可得
$$
\deg F_n=4-3\Delta A_n-\Delta B_n+\Delta C_n,
$$
而 $f_n-f_{n-1}=4+\mathbf1_{2\mid n}$，这证明 (4) 的全部次数界。最后，乘 $F_n$ 的有界多项式矩阵有单位三角主子式，故像 $p$ 饱和；各分量直接和保留饱和性。乘 $H_{38}$ 后只把 (6) 中的 $Q$ 原样送入目标，系数七为单位，得到整同构。$\square$

特别，整个单块 $\mathcal V_nT^j$ 无需额外角因子就允许该乘法，当且仅当
$$
\boxed{n\equiv11\pmod{12}.}
\tag{7}
$$
这时 $F_n=1$ 且 $e_{n+1}=e_n$。其他余类至少需要 (3) 中的一个真实因子；偶数 $n$ 时即使除子消掉，目标还须保留 (4) 所示的一阶次数边界。

## 3. 原完整矩阵上的精确核商

令 $V=\mathcal W_{D-1,J}$，$Y=\Gamma_{T_0}$，并在同一目标上取原完整评价
$$
M:V\longrightarrow Y,\qquad M=c_*U_0m_{13}J.
\tag{8}
$$
整个 $G_0=\mathscr R^{40}h_0(t)$、$P_{134}$、$U_0$ 和两条十三行均保留。将来源经 $S$、$T$ 嵌入同一 $\mathcal W_{D,J+1}$ 后，记其评价为 $M_S,M_T$。实际乘法给
$$
M_S=S_{\rm phys}M,\qquad M_T=T_{\rm phys}M
=H_{\rm phys}M_S.
\tag{9}
$$
这里 $S_{\rm phys}=wU_S$、$U_S(0)=1$，且
$$
H_{\rm phys}=h(w)e_2(\nu a\epsilon),\qquad h(0)=1,
\tag{10}
$$
是原整目标的单位。公式中的普通级数按原 $w^s=p\epsilon$ 进位，不删除任何高尾。

在有限自由目标基
$$
e_r=w^r/p^{\lfloor r/s\rfloor},\qquad0\le r<T_0,
$$
上，乘 $w$ 恰在 $r=s-1,2s-1$ 两处乘 $p$，在最后一行 $r=T_0-1$ 为零，其余均是单位平移。因此，对每个整数 $m\ge1$，
$$
\boxed{\ker(w:Y/p^m\to Y/p^m)
=\langle p^{m-1}e_{s-1},\ p^{m-1}e_{2s-1}\rangle_k
 \oplus(\mathcal O/p^m)e_{T_0-1}.}
\tag{11}
$$
三个位置是真实原目标的末行，不是自由新增的接触列。

**定理 2（实际额外核）。** 在同一个 $V/p^m$ 上，
$$
\boxed{K_m(M_S)=K_m(M_T),}
\tag{12}
$$
并有准确短正合列
$$
\boxed{0\longrightarrow K_m(M)\longrightarrow K_m(M_S)
\xrightarrow{\ \bar Q\mapsto M Q\ }
\operatorname{im}(M\bmod p^m)\cap\ker(w\bmod p^m)
\longrightarrow0.}
\tag{13}
$$
特别
$$
\boxed{\operatorname{length}_{\mathcal O}
\bigl(K_m(M_S)/K_m(M)\bigr)\le m+2.}
\tag{14}
$$
对原第二次提升 $m=2$，新增长度至多四；不能把它计作与 $p$ 成比例的新容量。

**证明。** (10) 是整单位，故 (9) 立即给 (12)。因目标交换，乘 $U_S$ 保持乘 $w$ 的核，所以 $S_{\rm phys}v=0$ 当且仅当 $wv=0$。于是 (13) 的像准确等于所列交，其核就是 $K_m(M)$。满射由这个交的定义给出，不要求原 $J$ 满射。最后 (11) 的长度为 $m+2$，得到 (14)。$\square$

定理 1 保证 $S$ 来源嵌入模 $p^m$ 后仍单射，所以 (13) 确实描述实际 $P_m=SQ$ 的扩大，而不是呈示的额外模 $p$ 关系。特别允许 $SQ$ 在原核而 $Q$ 不在核是合法的；需要付出的量就是 (13) 中实际原像与边界的交，不能预先把它取成整个环境 (11)。

## 4. 原 H38 在三个边界上的完整单位剪切

写
$$
\xi_1=p^{m-1}e_{s-1},\quad
\xi_2=p^{m-1}e_{2s-1},\quad\zeta=e_{T_0-1}.
$$
在 (11) 上，实际乘子 (10) 准确作用为
$$
\boxed{H_{\rm phys}\xi_1=\xi_1+\nu a\xi_2,
\qquad H_{\rm phys}\xi_2=\xi_2,
\qquad H_{\rm phys}\zeta=\zeta.}
\tag{15}
$$
$\nu a$ 为单位，其剩余值并未被抹掉。

**证明。** 在两个 carry 生成元上，普通正 $w$ 次项至少再带一个 $p$，与已有的 $p^{m-1}$ 相乘后消失。Gaussian 的 $\epsilon$ 常数项只把第一条边界送到第二条，系数是 $\nu a$；下一次平移落在 $3s-1\ge T_0$，不属于原目标。最后一行被任何正次项送出目标，所以只保常数一。$\square$

这给出一个可检验的原边界配对：若已知某个真 $M Q\in(11)$，其第一 carry 系数在 $H-I$ 下由单位送到第二条。它不证明这个边界向量属于原像，更不证明检测它的行能提升为同一个原 $\lambda_2$。

## 5. 界在原整满射范围的准确取值

若原相对 $J:V\to\Gamma_L$ 整满射，则 (8) 的像是原理想 $w^{13}\Gamma_L$，整个单位 $c_*U_0$ 保持该理想。(11) 的三个生成元都属于它：对应的原输入位置分别为 $s-14,2s-14,L-1$，三处 $m_{13}$ 都没有额外 $p$。所以 (14) 在这段实际范围恰为等号。

同一 $M_S$ 的像是 $w^{14}\Gamma_L$，仍放在原长度 $T_0=L+13$ 的目标中。源最后一行被截掉，两条 carry 带各长十四。因此其非零 Smith 因子准确为
$$
\boxed{L-29\text{ 个单位},\qquad28\text{ 个 }p,}
\tag{16}
$$
目标自由余核维数十四；若源维数为 $N$，自由源核维数为 $N-L+1$。没有出现新的 $p^2$ Smith 因子。式 (13) 的长度 $m+2$ 在这里分别来自一个真实截断自由方向的长度 $m$ 和两个 carry 的长度一。

这与 R412 的完整原 $M$ 的 $L-26$ 个单位、二十六个 $p$、十三个自由目标行一致。即使额外核长度达到上界，也不能用它替代所需的有限二阶双侧缺陷。

## 6. 真正左核与 R438 完整中央仍是额外条件

原 $H_{38}$ 只在 (5) 的来源上支付了乘法。一般并未证明它保持整个 $\operatorname{im}\bar M$ 或首 Bockstein 像，故不能把 (15) 声称为整个 $C_2(M)$ 的自同构。

例如，对由两个实际子格 $SV,TV$ 生成的映射，正确的整左核条件是
$$
\boxed{\lambda M_S\equiv0\pmod{p^m},\qquad
\lambda H_{\rm phys}M_S\equiv0\pmod{p^m}.}
\tag{17}
$$
它们同时要求 $\lambda$ 与 $H_{\rm phys}^*\lambda$ 杀同一 $M_S$，不能只保其中一条或随意指定两个边界值。若继续使用 R438 的两个完整三权，还须保原 $U_1/p$、第三位基准和 R434 的固定实际高轴。本文新增的是原格的最大乘法域和实际边界核商，不是第三条中央零。
