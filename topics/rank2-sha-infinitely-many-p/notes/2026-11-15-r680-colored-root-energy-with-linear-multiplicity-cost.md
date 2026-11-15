# R680 增补：按实际因子着色的根能量，重复次数只付线性成本

日期：2026-11-15。**状态：已证明。** 本增补加强 R680 的有限必要条件，
不更换任何原来源、中央条件或提升矩阵。

R680 的 $12/q^2$ 主成本可以完全去掉。
必须同时修改一个不可约因子内部的自项和根对项；
仅修改自项后仍把内部根对按 $m^2$ 计数，并不能得到下面的结论。

保 R672/R680 的原 $p=6s-1>101$、$D\ge3$、$f_D<p$、
$\mathcal W_D$、$\widehat P=d^{C_D}\bar P$、
$r=\operatorname{ord}_t\widehat P\ge1$。
对 $\bar P\in\ker\bar J$ 取 $\Delta=0$；
若只知 $\bar P\in\ker\bar M$，取 $\Delta=13$；
令 $H=s-\Delta$。
真正 primitive 第二、第三核仍须取较强的 $\Delta=0$。
原两个长 jet 是
$$
\widehat P(t,g),\quad(\mathcal E\widehat P)(t,g)\in t^H.
$$
全部十三行、同一个 $R$ 和下一位的范围与 R680 完全相同。

## 1. 着色根引理

设去掉 $t^r$ 和局部单位后，实际函数分解为
$$
f(t,Y)=U(t,Y)\prod_i\prod_{\alpha=1}^{c_i}
(Y-\psi_{i,\alpha}(t))^{m_i}.
$$
颜色 $i$ 标记同一个全局不可约因子；
同一颜色各根的重复次数都是 $m_i$。
根两两不同，$U$ 在原点为单位，$1\le m_i<p$。
令
$$
w(m)=
\begin{cases}
1,&m=1,\\
4(m-1),&m\ge2.
\end{cases}
\tag{1}
$$
于是
$$
m\le w(m)\le m^2,\qquad w(m)\le4m.
\tag{2}
$$

令
$$
h_{i,\alpha}=\operatorname{ord}_t(\psi_{i,\alpha}-g_0),
\qquad \bar h_{i,\alpha}=\min(h_{i,\alpha},s),
$$
其中 $g_0$ 为指定单位轴。定义同一着色能量
$$
\begin{aligned}
\mathscr E_w={}&
\sum_i w(m_i)\left\{
\sum_\alpha\bar h_{i,\alpha}
+6\sum_{\alpha<\beta}
\operatorname{ord}_t(\psi_{i,\alpha}-\psi_{i,\beta})\right\}\\
&+6\sum_{i<j}m_im_j
\sum_{\alpha,\beta}
\operatorname{ord}_t(\psi_{i,\alpha}-\psi_{j,\beta}).
\end{aligned}
\tag{3}
$$

**引理。** 若 $1\le S\le s$ 且
$f(t,g_0),f_Y(t,g_0)\in t^S$，则
$$
\boxed{\mathscr E_w\ge4S.}
\tag{4}
$$
这包括切向 Puiseux 根、任意真正重复因子及超过 $s$ 的接触。

**证明。** 在某个正实水平 $x$，令第 $i$ 个颜色有 $k_i$ 个活动根
（即 $h_{i,\alpha}\ge x$），总活动重数为
$M=\sum_i m_i k_i$。
用根差阶至少为两个接触阶的较小者，(3) 的积分下界在该水平的密度为
$$
A(x)=
\sum_i w(m_i)k_i(3k_i-2)
+6\sum_{i<j}(m_i k_i)(m_j k_j).
\tag{5}
$$
这里的积分只是有理分段常数的实数求和。

若某个颜色有 $k_i\ge2$ 个活动根，则
$$
w(m_i)k_i(3k_i-2)\ge4m_i k_i
$$
由 (2) 直接成立。
只有单根颜色可能对 $4M$ 产生亏量：
当 $m_i=1$ 时亏量为三，$m_i\ge2$ 时为四。

只要共有至少两个活动根，就有
$$
\boxed{A(x)\ge4M.}
\tag{6}
$$
如果它们全在一个颜色，已由上一式证明。
否则有至少两个活动颜色。
仅两个颜色且其总重数都为一时，跨色项恰为六，
准确支付两份三；若其中任一总重数至少二，
跨色项至少十二，超过所有可能的八份亏量。
三个以上活动颜色时，跨色项至少
$3l(l-1)\ge4l$，支付至多 $4l$ 的亏量。
这完整覆盖 (6)，不预设同一颜色只有一个局部分支。

若只有一个活动根，重数为 $m$，则
$$
A(x)=w(m)\ge4(m-1).
\tag{7}
$$

先假定全部 $h_{i,\alpha}\le s$。
若最近根唯一，对数导数的唯一最低项具有非零系数 $m_i$；
它在特征 $p$ 中为单位，故
$$
\operatorname{ord} f_Y(t,g_0)
=\sum_{i,\alpha}m_i h_{i,\alpha}-h_{\max}\ge S.
$$
由 (6)–(7)，逐水平有 $A(x)\ge4(M(x)-1)$，
积分给 (4)。
若最近根不唯一，则所有 $0<x\le h_{\max}$ 都至少有两个活动根，
(6) 直接给能量至少为
$4\operatorname{ord}f(t,g_0)\ge4S$。

最后支付截断。
至少两个不同根有 $h\ge s$ 时，在 $0<x\le s$ 仍可用 (6)，得至少 $4s$。
只有一个这样的根且其重数 $m\ge2$ 时，
它的自项 $w(m)s\ge4s$。
只剩唯一高根且 $m=1$：
无论其接触有限或为无穷，乘积求导均给
$$
\sum_{\text{其它根}}m_jh_j
=\operatorname{ord}f_Y(t,g_0)\ge S.
$$
该高根与同色其余根的系数为 $6w(1)=6$，
与异色根的系数为 $6m_j$；
根差阶准确等于其它根的较小接触阶。
所以这些交叉项已经给至少 $6S$。
全部情形均得 (4)。证毕。

## 2. 乘原完整判别式后，全局只剩线性损失

保 R680 的 $q$ 个实际点 $(0,\zeta)$，$\zeta\in\mu_q$，
其来源是同一个 $\widehat P$ 的 charge 同余恒等式。
令全局实际接触因子为 $F_i^{m_i}$，严格曲线为 $C_i$，并记
$$
\mathscr C=\sum_i m_iC_i,\qquad
B_{\rm ct}=\sum_i m_i\deg_YF_i.
$$
所有颜色都由这些同一个全局不可约因子确定，
不能为了改变能量而任意重分颜色。

R680 的同一原 Euler forcing 给
$$
\sum_{\zeta}\left\{\sum_{\psi\mid F_i,\zeta}\min(h_\psi,s)
+3\Delta_{i,\zeta}\right\}
\le3C_i^2+LC_i,\qquad LC_i\le8\deg_YF_i.
\tag{8}
$$
同色根对在 (3) 中恰为 $3w(m_i)\Delta_{i,\zeta}$，
所以可将 (8) **整体乘 $w(m_i)$**。
异色项仍用真实交数乘 $6m_im_j$。
由 (4)，得到准确式
$$
\begin{aligned}
4q(H-r)
&\le
3\sum_i w(m_i)C_i^2
+6\sum_{i<j}m_im_jC_iC_j
+\sum_i w(m_i)LC_i\\
&=
\boxed{
3\mathscr C^2
-3\sum_i\{m_i^2-w(m_i)\}C_i^2
+\sum_i w(m_i)LC_i.}
\end{aligned}
\tag{9}
$$
所有 $C_i^2\ge0$ 已由 R680 的原规范交数和伴随公式证明，
并非假定因子光滑。
又 $w(m_i)\le4m_i$，故
$$
\boxed{
4q(H-r)\le3\mathscr C^2+32B_{\rm ct}
\le3\mathcal B_D^2+32(D-n_*).}
\tag{10}
$$
最后使用 R680 已付的
$\mathscr C^2\le\mathcal B_D^2$、$B_{\rm ct}\le D-n_*$。

式 (9) 比 (10) 更强：
$m_i\ge2$ 时，负项准确为
$-3(m_i-2)^2C_i^2$；
$m_i=1$ 时该项为零。
没有以粗略的最大重复次数再制造一个二次主成本。

## 3. 加强后的原有限门

若 $r<H$，由 (10)、$r\le M_D=5D+4-(D\bmod2)$ 得
$$
\boxed{
p\le6(M_D+\Delta)-1
+\frac{9}{2q}\mathcal B_D^2+\frac{48D}{q}.}
\tag{11}
$$
若 $r\ge H$，原简单界
$p\le6(M_D+\Delta)-1$
更强，所以 (11) 是统一必要条件。
实际有限参数可保 (9) 的负项、实际 $n_*$ 和全部重数。

由于 $\mathcal B_D^2=47D^2/12+O(D)$，主阶加强为
$$
\boxed{p\le\frac{141}{8q}D^2+O(D).}
\tag{12}
$$
特别，任意原非零两长 jet 核均须满足
$$
\boxed{D\ge\left(\sqrt{\frac8{141}}-o(1)\right)\sqrt p.}
\tag{13}
$$
这是一般稠密混合 charge 也适用的必要下界，不需要有界重复次数。

在原低 $\ell$ 临界 $p/D^2\to47/8$ 下，
$q\ge4$ 仍被严格排除；
$q=3$ 的新主系数恰为
$$
141/24=47/8.
$$
因此不能丢掉线性项后再宣称 $q=3$ 不可能。
$q=1,2,3$ 的真实临界像及同一个 $R$ 的指定第二 forcing 仍开。

本增补没有免费返回 Euler forcing 为来源，
没有增加原中央零，也没有改变 R683 的实际整满射范围。
它仅将 R680 的重复因子成本改为正确的着色线性预算；
全部原角帽、$P_{134}/U_0$、两个十三行带和下一位按原文保留。
