# R633 — 原像锥补与同源合流矩阵的完整首 Bockstein

日期：2026-11-15。**状态：已证明。**

本篇继续 R620/R631 的同一个原来源 $\mathcal W_D$ 和完整目标
$\mathcal C_p$。先把 R631 的低十三阶投影扩大为原像锥的完整补投影，
其核准确是原来源中真正被 $t^s$ 整除的尾格。
随后，对同一个 $P=t^sR$ 和同一个实际修正 $Q$，
使用完整的合流 Vandermonde 块逐阶消元。

在显示的早阶条件下，这给出原首 Bockstein 核的**准确维数**，
而非环境列数的上界。特别，当 $p/D$ 严格大于 $625/49$ 时，
完整大目标的全部非单位 Smith 因子最终都恰为 $p$。
更小预算中，赋值至少二的因子与特征零核方向的总数也有准确求和公式。
本篇仍不分别判定这些方向的更高 Smith 指数。

全部 $q_n$ 高尾、$g/t/U_0$、charge 四十和 $\Upsilon$ 标准基均保留。
完整大目标中的结论不替代旧三块的同一个 $R$ 或旧 $d_2$。

## 1. 原来源、实际矩阵与全部帽

设
$$
p=6s-1>101,\qquad
f_D=\lfloor9D/2\rfloor+4<p,\qquad
n_0=s-13,\qquad m=p-78.
\tag{1}
$$
因此 $D<p$、$A_D<s$，并且
$$
D<p-73,\qquad 2D+2<p.
\tag{2}
$$
例如 $f_D<p$ 给 $D<2(p-4)/9$，由 $p>101$ 即得 (2)。

沿原定义
$$
\mathcal W_D
=\bigoplus_{n=0}^{D}Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=\frac{\{t h_7(t)\}^{A_n}(t-1)^{B_n}}{d(t)^{C_n}},
\qquad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4,\quad
e_{n+1}=f_n-3A_n-B_n+C_n,\quad
b_n=A_n+e_{n+1}.
\tag{3}
$$
原整基按首阶重排为
$$
C_{n,r}=Y^nq_n(t)t^{r-A_n},
\qquad A_n\le r\le b_n.
\tag{4}
$$
其首系数是 $\chi_nY^n$，其中
$\chi_n=7^{A_n}(-1)^{B_n}$ 为整单位。

记
$$
\mathcal I_r=\{n:A_n\le r\le b_n,\ 0\le n\le D\},
\qquad m_r=|\mathcal I_r|,
\qquad h_r=(m-6r)_+.
\tag{5}
$$
R620 已证明
$$
\mathcal I_r=[\rho(r),\min(D,4r+2)]\cap\mathbf Z,
\quad \rho(r)=\min\{n:b_n\ge r\},
$$
$$
b_{n+12}=b_n+50,\qquad
(b_0,\ldots,b_{12})=(4,8,13,15,21,24,30,32,37,41,47,48,54).
\tag{6}
$$
特别 $b_n$ 严格递增，$m_{r+1}\ge m_r-1$。

实际完整评价仍是
$$
\boxed{
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon})\in\mathcal C_p,}
\tag{7}
$$
其中 $a,c_*,U_0(0),\tau_0$ 都是原单位，
$t(w)=\tau_0w+O(w^2)$、$g(0)=1$。
原 $P_{134}/U_0$ 没有改动。

目标保留全部关系
$$
\mathcal C_p=
\mathcal O[w,\epsilon,\Upsilon]/
(w^s-p\epsilon,\epsilon^6-w\Upsilon,
w^{s-1}\epsilon^5-p\Upsilon,\Upsilon^s).
\tag{8}
$$
其标准基为
$$
\Upsilon^\jmath w^\rho\epsilon^\iota,
\quad 0\le\jmath<s,\quad0\le\rho<s,\quad0\le\iota\le5,
\quad(\rho,\iota)\ne(s-1,5).
\tag{9}
$$
目标秩为 $ps$。记剩余域为 $k$。

对带权理想
$$
I_\lambda(t,v)=
\langle t^rv^h:6r+h\ge\lambda\rangle,\qquad v=Y-1,
$$
原首核和首 Bockstein 是
$$
\mathscr K_m=\ker\bar\Phi
=\{\bar P\in\overline{\mathcal W}_D:\bar P(t,1+v)\in I_m\},
$$
$$
\beta_{\mathcal C}:\mathscr K_m\longrightarrow
\operatorname{coker}\bar\Phi,\qquad
\bar P\longmapsto[\overline{\Phi(P)/p}].
\tag{10}
$$
R620 给同一来源中的准确整提升 $P(t,1+v)\in I_m$，并给
$$
k_m:=\dim\mathscr K_m=\sum_r(m_r-h_r)_+.
\tag{11}
$$

## 2. 原像所在的真锥及其补投影

令 $\mathscr B$ 为 $k[w,\epsilon]$ 在 $\overline{\mathcal C}_p$ 中的实际像。
由 (8)–(9)，准确有
$$
\boxed{\mathscr B\simeq k[w,\epsilon]/I_p(w,\epsilon).}
\tag{12}
$$
确实，原生单项式 $w^r\epsilon^h$ 写成标准基时，令 $h=6j+i$，
它变为 $\Upsilon^j w^{r+j}\epsilon^i$。
因此 $\mathscr B$ 的标准单项式准确满足
$$
\jmath\le\rho.
$$
而 $w^{13}\mathscr B$ 的标准单项式准确满足
$$
\boxed{\jmath\le\rho-13.}
\tag{13}
$$
越过 $w^s$ 或 $w^{s-1}\epsilon^5$ 的项模 $p$ 为零，不能绕回补锥。

R631 的完整 regular 尾界表明，任意原列 (7) 模 $p$
只留下原权 $6r+i<p$ 的原生项。
具体地，其系数满足
$$
v_p(c_{r,i})\ge-\lfloor6r\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}.
$$
在标准 raw 基中，$w^r\epsilon^i$ 自带
$p^{\lfloor(6r+i)/p\rfloor}$。
第一带的普通系数整；第二带以后 R631 引理1给至少两次 $p$。
故这里用的是实际完整约化，得到
$$
\boxed{\operatorname{im}\bar\Phi\subset w^{13}\mathscr B.}
\tag{14}
$$

定义 $\Pi_{\rm out}$ 为 (9) 上的坐标投影，保留所有
$$
\boxed{\jmath>\rho-13.}
\tag{15}
$$
所有 $\Upsilon$ 层和所有 $\iota=0,\ldots,5$ 均保留。
由 (13)–(14)，
$$
\Pi_{\rm out}(\operatorname{im}\bar\Phi)=0.
\tag{16}
$$
所以 $\Pi_{\rm out}\beta_{\mathcal C}$ 是真正余核上的映射。
它比 R631 的 $\rho<13$ 投影更大；
新增的行利用了原像在 $w^{13}\mathscr B$ 内，
而不只利用其在 $w^{13}\overline{\mathcal C}_p$ 内。

## 3. 完整锥补核准确等于原 t^s 尾格

对同一准确整提升 $P(t,1+v)\in I_m$，
R631 已证明
$$
\overline{\Phi(P)/p}
\text{ 只由 }p\le6r+i<2p,\quad0\le i<p
\text{ 的第一权带给出。}
\tag{17}
$$
所有更高 regular 项在原整目标内至少被 $p^2$ 整除；
这里不再假设其低阶之外的系数整。

第一带单项式除以 $p$ 的准确 carry 为
$$
i+1=6j+t,\quad0\le t\le5,\qquad b=r+j-s,
$$
$$
\boxed{\frac{w^r\epsilon^i}{p}
=\Upsilon^j w^b\epsilon^t,\qquad
6b+t=6r+i-p.}
\tag{18}
$$
它是这一权带到真正标准基的单射。
条件 (15) 变为
$$
j>b-13\quad\Longleftrightarrow\quad r<s+13.
$$
除去原 $w^{13}$ 前缀后，锥补准确读取
$$
0\le r<s,\quad0\le i<p,\quad
m\le6r+i<L,\qquad L=2p-78.
\tag{19}
$$

为保持角坐标，考虑有限环
$$
\mathscr T=
k[t,v]/(t^s,v^p,I_L(t,v)).
\tag{20}
$$
原代入 $t=t(w)$、$v=g(w)e^{a\epsilon}-1$
给它与
$k[w,\epsilon]/(w^s,\epsilon^p,I_L)$ 的过滤同构。
证明如下。

$t$ 的首项为 $\tau_0w$，故保持普通 $s$ 阶理想。
又因 $s<p$，在目标中
$$
\{g(w)e^{a\epsilon}-1\}^p=0.
$$
这里 $g(w)^p=1$ 模 $w^s$，而截断指数的 $p$ 次幂为一模 $\epsilon^p$。
反代先解 $w=t^{-1}_{\rm comp}(t)$，然后用
$$
\epsilon=a^{-1}\log\!\left(\frac{1+v}{g(w)}\right),
$$
对一个 $p$ 次幂为零的单变量截断至 $p-1$ 次。
所用分母 $1,\ldots,p-1$ 都为单位。
这是单变量指数与对数的复合恒等；
不需要、也不使用两个独立幂零变量上的截断指数加法公式。
正反代入的首权分别是 $6$ 和 $1$，故同时保持 $I_L$。
所有所读普通系数位于 $w^{<s}$，R631 的界保证它们确实整。

乘 $c_*U_0e^{40a\epsilon}$ 在 (20) 中也是过滤单位。
结合 (17)–(19)，因此
$$
\ker(\Pi_{\rm out}\beta_{\mathcal C})
=\overline{\mathcal W}_D\cap(t^s,v^p,I_L).
\tag{21}
$$
因 $\deg_Y P\le D<p$，没有 $v^p$ 分量。
对 $r<s$，仍须杀掉的最小 $v$ 阶出现在 $r=s-1$，等于
$$
L-6(s-1)=p-73>D.
$$
所以 (21) 强迫所有 $t^{<s}$ 的 $Y$ 多项式系数准确为零。
反之，$t^s$ 整除显然使 (19) 全零。

**定理 1（准确锥补核）。**
$$
\boxed{\ker(\Pi_{\rm out}\beta_{\mathcal C})
=\overline{\mathcal W}_D^{(s)},\qquad
\mathcal W_D^{(s)}=\{P\in\mathcal W_D:t^s\mid P\}.}
\tag{22}
$$
由于 $A_D<s$，这是真正原列的尾格，具有基
$$
C_{n,s+r},\qquad r\ge0,\quad b_n\ge s+r.
\tag{23}
$$
故
$$
T_s:=\dim\overline{\mathcal W}_D^{(s)}
=\sum_{n=0}^D(b_n-s+1)_+,
$$
$$
\boxed{\operatorname{rank}(\Pi_{\rm out}\beta_{\mathcal C})=k_m-T_s,
\qquad \ker\beta_{\mathcal C}\subset\overline{\mathcal W}_D^{(s)}.}
\tag{24}
$$
这加强 R631 的 $\ker\beta_{\mathcal C}\subset\mathscr K_p$，
且保留全部高 $\Upsilon$ 行。

## 4. 剩余核中的同一真实 Q 与 P=t^sR

取 (23) 的一个实际整提升 $P=t^sR$。
这里 $R$ 只是该原来源除去共同 $t^s$ 的计算记号，
不是加入的新自由来源。
置
$$
c_s(w)=(t(w)/w)^s.
$$
由原关系 $w^s=p\epsilon$，
$$
\boxed{
\frac{\Phi(P)}p
=c_*w^{13}U_0e^{40a\epsilon}\,
\epsilon c_s(w)R(t(w),g(w)e^{a\epsilon}).}
\tag{25}
$$
其右端确实整：除去 $t^s$ 后的每个普通因子为
$t^r h_7^{A_n}(t-1)^{B_n}d^{-C_n}$，
$R618$ 的同一第二盘界适用于这些非负幂及 $(t/w)^s$。
按 R631 的权带估计，(25) 模 $p$ 落在 $w^{13}\mathscr B$ 中。

因此 $\beta_{\mathcal C}(\bar P)=0$ 当且仅当存在同一原
$\bar Q\in\overline{\mathcal W}_D$，使
$\bar\Phi(\bar Q)=\overline{\Phi(P)/p}$。
乘去共同单位，并使用
$$
w^{13}:\mathscr B/I_m\ \xrightarrow{\sim}\ w^{13}\mathscr B
$$
的单射，得到准确等价式
$$
\boxed{
Q(t(w),g(w)e^{a\epsilon})
=\epsilon c_s(w)R(t(w),g(w)e^{a\epsilon})
\pmod{I_m(w,\epsilon)}.}
\tag{26}
$$
这里没有把 $w^{13}$ 当单位；
使用的是它在所列商上的准确核。
原两边分别来自 $Q$ 和原 $P$ 的尾格，所有角和帽均不变。

定义
$$
\mathcal J_r=\{0\le n\le D:b_n\ge s+r\},
\qquad j_r=|\mathcal J_r|,
\qquad R_{\max}=b_D-s.
\tag{27}
$$
若 $R_{\max}<0$，定理1已经给 $\ker\beta_{\mathcal C}=0$。
以下先取 $R_{\max}\ge0$。
$\mathcal J_r$ 是原连续电荷的尾区间，且 $j_r=0$ 当 $r>R_{\max}$。
其相邻两阶至多失去一个电荷。

假设 (26) 中 $Q$ 和 $R$ 的所有较低首阶来源系数都已为零。
那么第 $w^r$ 阶的新系数，除去原单位 $\tau_0^r\chi_n$，
准确由下列函数给出：
$$
e^{an\epsilon}\quad(n\in\mathcal I_r),\qquad
\epsilon e^{an\epsilon}\quad(n\in\mathcal J_r).
\tag{28}
$$
右边还带同一个单位 $c_s(0)=\tau_0^s$。
原 charge 四十已由 (26) 的共同单位消去；
保留它时，节点只同时平移为 $a(n+40)$。

(28) 不忽略高尾。
此前来源系数已经为零时，它们的全部 $q_n/g/t/c_s$ 高尾才为零。
出现自由来源坐标以后，所有这些高尾必须进入后续右端；
第7节将逐阶支付它们。

## 5. 真合流块与普遍剩余核上界

置
$$
\boxed{M_r=|\mathcal I_r\cup\mathcal J_r|+|\mathcal J_r|.}
\tag{29}
$$
将 (28) 嵌入以下完整合流族：
对 $\mathcal I_r\cup\mathcal J_r$ 中每个节点取一个值列，
对 $\mathcal J_r$ 中每个节点再取一个一次导数列。
若 $\mathcal J_r\not\subset\mathcal I_r$，补的值列仅用于证明原子族独立；
不把它们加入来源。

该完整族前 $M_r$ 个 Taylor 系数，逐行乘 $h!$ 后，
就是节点 $an$、重数一或二的合流 Vandermonde 矩阵。
它的行列式为各不同节点之差的相应整数幂乘单位。
由 $D<p$ 和 $M_r\le2D+2<p$，所有节点差及所用阶乘都是单位。
所以当
$$
h_r\ge M_r
\tag{30}
$$
时，(28) 在真正的第 $r$ 阶目标中满列秩。

令
$$
r_\dagger=\min\{0\le r\le R_{\max}:h_r<M_r\},
\tag{31}
$$
若集合为空则置 $r_\dagger=R_{\max}+1$。

**定理 2（同源逐阶注入）。**
$$
\boxed{\ker\beta_{\mathcal C}
\subset\overline{\mathcal W}_D^{(s+r_\dagger)}.}
\tag{32}
$$
特别
$$
\boxed{
\dim\ker\beta_{\mathcal C}
\le\sum_{n=0}^D(b_n-s-r_\dagger+1)_+.}
\tag{33}
$$

**证明。**
定理1先把 $\bar P$ 放到实际尾格。
对 (26) 从 $r=0$ 开始归纳。
只要 (30) 成立，(28) 的满列块迫本阶所有 $Q$ 和 $R$ 新来源系数为零。
所以归纳假设在下一阶仍成立，全部已出现的高尾同时为零。
归纳至 $r_\dagger$，$R$ 的所有更低首阶系数皆零，
正是 (32)。若没有失败阶，(23) 的全部 $P$ 系数已被杀尽。
证毕。

这里没有将整矩阵假设为独立普通阶块；
逐阶单位块只在已实际归零的低来源之后使用。

## 6. 一个终端不等式即支付全部注入

由于 $\mathcal I_r$、$\mathcal J_r$ 在相邻两阶分别至多失去一个指标，
它们的并至多失去两个指标。
因此
$$
M_{r+1}\ge M_r-3.
\tag{34}
$$
而正的 $h_r$ 每阶减少六。
于是若 (30) 在终端 $R_{\max}$ 成立，它在全部更低阶也成立。

在终端，$\mathcal J_{R_{\max}}=\{D\}$，
且 $D\in\mathcal I_{R_{\max}}$ 当且仅当 $R_{\max}\ge A_D$。
故
$$
M_{R_{\max}}
=m_{R_{\max}}+1+\mathbf1_{R_{\max}<A_D},
$$
$$
h_{R_{\max}}=2p-6b_D-77
$$
只要右端满足下面的正下界。

**推论 3（完整大目标的准确 p-Smith 窗）。**
除 $b_D<s$ 已直接成立的情形外，若
$$
\boxed{
2p-6b_D-77
\ge m_{b_D-s}+1+\mathbf1_{b_D-s<A_D},}
\tag{35}
$$
则 $\beta_{\mathcal C}$ 单射。
原实际矩阵准确有
$$
\boxed{
N_D-k_m\text{ 个单位因子，}\quad
k_m\text{ 个恰为 }p\text{ 的因子，}\quad
\text{没有零列因子}.}
\tag{36}
$$
整余核的自由秩是 $ps-N_D$。

**证明。**
(35) 与 (34) 给 (30) 在整个真实尾格成立。
应用定理2，再使用 R620 已付的单位数和有限自由矩阵的首 Bockstein。
证毕。

(35) 是逐个 $p,D$ 可直接读的条件，不要求渐近。
它是充分条件，本篇不称其为单射的必要条件。

## 7. 完整联合修正矩阵：剩余核的准确公式

还能在一个显示的早阶条件下算出全部首 Bockstein 核。
设
$$
\boxed{h_r\ge M_r\qquad(0\le r<A_D).}
\tag{E}
$$
一个更容易使用的充分条件是
$$
\boxed{p\ge2D+6A_D+74.}
\tag{37}
$$
确实，对 $r<A_D$，
$$
h_r\ge p-78-6(A_D-1)\ge2D+2\ge M_r.
$$
当 $A_D=0$ 时 (E) 为空条件。
在 (1) 下，$D\ge72$ 时 (37) 自动成立：
$p\ge\lfloor9D/2\rfloor+5\ge9D/2+9/2$，
而 $2D+6A_D+74\le7D/2+151/2$。

考虑 (26) 的**实际联合矩阵**
$$
\mathcal L:
\overline{\mathcal W}_D\oplus
t^{-s}\overline{\mathcal W}_D^{(s)}
\longrightarrow k[w,\epsilon]/I_m,
$$
$$
(Q,R)\longmapsto
Q(t,g e^{a\epsilon})-\epsilon c_s R(t,g e^{a\epsilon}).
\tag{38}
$$
第二直和项仍按原尾基 (23) 呈示，不能任取环境 $R$。

当 $r\ge A_D$ 时，每个 $\mathcal J_r$ 电荷都满足 $A_n\le r$，
而 $b_n\ge s+r>r$，所以
$$
\mathcal J_r\subset\mathcal I_r,\qquad M_r=m_r+j_r.
\tag{39}
$$
于是 (28) 这时本身就是完整合流族，不需要补列。
前任意 $\min(h_r,m_r+j_r)$ 行的矩阵具有对应满秩：
可将其作为完整 $m_r+j_r$ 阶合流 Vandermonde 的首行段。
这是同一函数的系数恒等，不增加实际所读目标行。

令 $n_r=m_r+j_r$。
由 (6)、(27)，
$$
n_{r+1}\ge n_r-2.
\tag{40}
$$
因此 $h_r$ 与 $n_r$ 也只有一个自由坐标转换点：
一旦 $h_r<n_r$，此后再不会出现 $h_{r'}>n_{r'}$。

**定理 4（全实际首 Bockstein 的准确剩余维数）。**
在 (1)、(E) 下，
$$
\boxed{
\kappa_D(p):=\dim\ker\beta_{\mathcal C}
=\sum_{r\ge0}
\left\{(m_r+j_r-h_r)_+-(m_r-h_r)_+\right\}.}
\tag{41}
$$
等价地，
$$
\boxed{
\kappa_D(p)=
\sum_{r\ge0}\left(j_r-(h_r-m_r)_+\right)_+.}
\tag{42}
$$
两式均为有限和；所有项都由原帽 (3) 直接计算。

**证明。**
若 $b_D<s$，$j_r=0$，定理1即给结论。
以下设尾格非零。

先按 $r$ 消元 (38)。
在出现自由来源坐标以前，低来源已整齐归零：
对 $r<A_D$ 用 (E) 和第5节原子族的满列秩；
对 $r\ge A_D$ 用 (39) 的完整合流块。
这迫每个新来源系数为零，故其全部高尾也确为零。

第一次 $h_r<n_r$ 发生时必有 $r\ge A_D$。
从该阶开始，(39) 给本阶全部 $h_r$ 行满行秩。
保留 $n_r-h_r$ 个新自由来源坐标，
用其余真实列解掉低阶自由列产生的全部右端。
这个右端包括 $q_n$、$g$、$t$ 和 $c_s$ 的所有所读高尾。
所用列首阶恰为 $r$，所以不改变更低阶。

(40) 保证以后的每阶仍有足够真实列。
目标最后有约束的普通阶为 $n_0-1$，
而现在 $b_D\ge s>n_0-1$，所以不存在最大来源首阶之后的隐藏目标条件。
当 $h_r=0$ 后，本阶及更高实际来源坐标自由。
因此
$$
\dim\ker\mathcal L=\sum_r(m_r+j_r-h_r)_+.
\tag{43}
$$
这是完整同帽来源的消元，而非只求各对角块的维数之和。

再将 $\ker\mathcal L$ 投到 $P=t^sR$。
由 (26)，其像准确是 $\ker\beta_{\mathcal C}$；
其核是 $R=0$ 时的原 $\ker\bar\Phi=\mathscr K_m$。
所以有实际短正合列
$$
0\longrightarrow\mathscr K_m
\longrightarrow\ker\mathcal L
\longrightarrow\ker\beta_{\mathcal C}
\longrightarrow0.
\tag{44}
$$
由 (11)、(43) 得 (41)。
对每一阶作初等恒等变形即得 (42)。证毕。

于是，在 (E) 下，原有限自由物理矩阵准确有
$$
\boxed{
\begin{aligned}
\#\{\text{单位 Smith 因子}\}&=N_D-k_m,\\
\#\{\text{恰为 }p\text{ 的 Smith 因子}\}&=k_m-\kappa_D(p),\\
\#\{\text{赋值至少二的因子或零列方向}\}&=\kappa_D(p).
\end{aligned}}
\tag{45}
$$
最后一行是这个联合类别的准确数目；
它不区分 $p^2,p^3,\ldots$ 与特征零核。
没有借 (43) 宣称物理像整饱和。

## 8. 真实全预算的显式渐近系数

令 $D\to\infty$、$p=\alpha D+O(1)$，其中固定 $\alpha\ge9/2$，
始终满足原 (1)。
条件 (37) 最终自动成立，故可用准确公式 (41)。

对 $x=r/D$，在 $x\ge1/4$ 有
$$
m_r=D(1-6x/25)_++O(1),
$$
$$
j_r=D(1-\alpha/25-6x/25)_++O(1),
\qquad h_r=D(\alpha-6x)_++O(1).
\tag{46}
$$
在 $r<A_D$，$h_r\ge(\alpha-3/2)D+O(1)$，
而 $M_r\le2D+2$，所以此前无自由联合坐标。

设
$$
x_0=\frac{25(\alpha-1)}{144},\qquad
x_1=\frac{26\alpha-50}{138},\qquad
x_R=\frac{25-\alpha}{6}.
\tag{47}
$$
分别对应原 $h=m$、联合 $h=m+j$、尾格 $j=0$ 的转换点。
当 $\alpha<625/49$ 时，
$$
x_1<x_0<x_R.
$$
在 $x_1$ 到 $x_0$ 之间，(42) 的密度为 $m+j-h$；
在 $x_0$ 到 $x_R$ 之间，其密度为 $j$。
置 $C=625-49\alpha$。
这两块三角形的共同高度为 $C/600$，底边分别为
$$
x_0-x_1=\frac{C}{3312},\qquad
x_R-x_0=\frac{C}{144}.
$$
所以其总面积是
$$
\frac12\frac{C}{600}
\left(\frac{C}{3312}+\frac{C}{144}\right)
=\frac{C^2}{165600}.
$$
当 $\alpha\ge625/49$ 时，正面积为空。
原十二余类和端点取整只产生 $O(D)$ 误差。

**推论 5。**
$$
\boxed{
\dim\ker\beta_{\mathcal C}
=\frac{(625-49\alpha)_+^2}{165600}\,D^2+O(D).}
\tag{48}
$$
此外，由 R620，
$$
k_m=\frac{(25-\alpha)_+^2}{288}\,D^2+O(D).
\tag{49}
$$
故恰为 $p$ 的实际 Smith 因子数为
$$
\boxed{
\left\{\frac{(25-\alpha)_+^2}{288}
-\frac{(625-49\alpha)_+^2}{165600}\right\}D^2+O(D).}
\tag{50}
$$

若 $\alpha>625/49$，带固定严格余量，
则不仅 (48) 的主项为零，(35) 最终实际成立，
从而 $\ker\beta_{\mathcal C}=0$ **准确成立**。
确实，$\alpha<25$ 时终端满足
$$
h_{R_{\max}}-M_{R_{\max}}
=\left(2\alpha-25-\frac{\alpha}{25}\right)D+O(1)
=\frac{49\alpha-625}{25}D+O(1)>0.
$$
$\alpha\ge25$ 则尾格为空或仅有限厚度，直接用同一终端式即可。
本篇不从临界点 $\alpha=625/49$ 的零主项推出准确零核。

## 9. 原修正、旧截止与全局成本的范围

定理1、定理4和 (45) 全部属于原完整
$\mathcal W_D\to\mathcal C_p$。
$\Pi_{\rm out}$ 读取全部 $\Upsilon$ 层；
其中大量行在旧 $M=c_*U_0m_{13}J$ 截止之外。
因此本篇没有把完整目标的 $\ker\beta_{\mathcal C}$
等同于旧三块的 $K_2$，也没有以其单射判旧 $d_2$ 非零。

(26)、(38)、(44) 始终使用同一个原 $P$、同一个原 $Q$，
并支付全部高尾。它们不允许把旧问题的前两块、第三短尾、
两条十三行或同一个 $R$ 分别选取修正。
R597/R608 的指定旧 forcing 和实际余像保持原定义。

同样，准确有限目标的 Smith 数目不自动等于所有真饱和前缀的成本。
本篇没有新增列、没有给核基或其乘积赋中央零，
没有将 (48) 单独换成全 $D/k$ 的 Bost 严格不等式。
固定曲线的无穷素数主目标仍未完成。

## 依赖

- [R631](R631-original-first-bockstein-weight-band-and-exact-boundary-kernel.md)：
  全 regular 高尾的至少 $p^2$ 界、第一权带的准确 carry 单射、
  同一原首 Bockstein。
- [R620](R620-full-original-weighted-hilbert-function-and-thirteen-row-smith-window.md)：
  全部实际帽、准确 Hilbert 函数、同帽整提升和单位 Smith 数。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  用于 (25) 的同一第二盘和所有系数估计。
- [R612](R612-original-full-source-weighted-kernel-and-fixed-nodal-exit.md)、
  [R607](R607-original-integral-target-and-mixed-schur-decomposition.md)：
  完整物理矩阵与 $\mathcal C_p$ 的全部标准基和边界关系。

本篇是全参数证明；未增加素数扫描或未执行证书。
