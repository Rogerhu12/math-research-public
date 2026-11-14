# R148：用两个线性矩构造准确满足 Codazzi 的全边界 lifting

**状态：已证明。** 本结论给固定正度量上的线性构造，不声称 Gauss 方程、曲率限制、位置闭合或强闭曲面已经得到。它针对任意切换权重造成的高角 Codazzi 强迫：先对完整角函数准确解两条 Codazzi，再把非线性 Gauss 留给后续求解。所有积分与 Fourier 系数在本定理中均指准确对象；数值实现必须另付积分、截断及端点误差。

## 1. 度量、端点与需要满足的必要条件

在固定物理材料坐标 $(s,u)\in[C,L]\times\mathbb R/(2\pi\mathbb Z)$ 上，令
$$
g=ds^2+a(s)^2du^2,\qquad a\in C^2[C,L],\quad a>0,
\qquad c=a'/a.
$$
给定实的 $\pi$ 周期两端三场 $(n_C,m_C,l_C)$、$(n_L,m_L,l_L)$。在当前 D2 情形中 $n,l$ 对 $u$ 为偶函数、$m$ 为奇函数，因而 $m$ 的角均值为零。给定一个已知 baseline $l^b(s,u)$，它在两端分别取指定的 $l$ 迹。若需要保留一整段端点 collar，可直接要求 baseline 在这些 collar 上等于指定准确模型的 $l$。

固定非负函数 $b\in C^1[C,L]$，在两端的开放邻域为零。另假定存在一个内部开放区间 $F$ 与常数 $0<\eta\le1$，在其中
$$
a a''-(a')^2\ge-4(1-\eta),\qquad b>0. \tag{1}
$$
另要求 $M_0=\int_C^L(a')^2b>0$，以处理零模。这里的条件仅用于以下显式控制构造的非退化；不要求其它部分曲率、$a'$ 符号或 $|a'|\le1$。常斜率平坦区间 $|a'|<2$ 是 (1) 的一个充分例子，却不是必要条件。

当前候选的末段是 phase bridge，不能把它误称为开放的 $a'=-1$ 平坦 collar。当前可用的依据是：受保护中央柱结束处 $a'=a''=0$，其后两厘米不受半径 bump 改变。连续性直接给这个保护邻域内某个 $F$ 满足 (1)，例如取 $\eta=1/2$ 后足够靠近柱端；$b$ 可从柱端后的一个更小零邻域之外开始为正，从而保持整个中央柱不变。选择 $b$ 在其它实际 $a'\ne0$ 的区间也为正即可保证 $M_0>0$。此存在性陈述不冒充已计算出某个特定数值区间的界。

两条物理 Codazzi 方程等价于
$$
(a^2m)_s=a l_u,\qquad (an)_s=m_u+a'l. \tag{2}
$$
因此零 Fourier 模式必须满足
$$
a_L^2m_{L,0}=a_C^2m_{C,0}. \tag{3}
$$
D2 数据自动满足 (3)。本构造不通过修改边界均值来隐藏这一条件。

## 2. 非零角模的准确两矩条件

使用 $e^{iku}$ 的 Fourier 约定，只有偶整数 $k$ 出现。记
$$
J(s)=\int_s^L a(r)^{-2}\,dr,\qquad I=J(C),\qquad a_C=a(C),\ a_L=a(L).
$$
对任意指定的 $l_k(s)$，从左端数据解 (2) 得唯一函数
$$
m_k(s)=\frac{a_C^2m_{C,k}+ik\int_C^s a(t)l_k(t)\,dt}{a(s)^2}, \tag{4}
$$
$$
n_k(s)=\frac{a_Cn_{C,k}+ik\int_C^s m_k(r)\,dr+
\int_C^s a'(t)l_k(t)\,dt}{a(s)}. \tag{5}
$$
交换三角区域中的积分，得
$$
\int_C^L m_k(r)\,dr=a_C^2m_{C,k}I+
ik\int_C^L a(t)J(t)l_k(t)\,dt.
$$
故 $k\ne0$ 时，(4)–(5) 满足两个右端迹，当且仅当
$$
\int_C^L a l_k=\frac{a_L^2m_{L,k}-a_C^2m_{C,k}}{ik}, \tag{6}
$$
$$
\int_C^L(a'-k^2aJ)l_k=a_Ln_{L,k}-a_Cn_{C,k}-ik a_C^2m_{C,k}I. \tag{7}
$$
这是真正完整的两端条件，没有舍弃 $n$ 或 $m$ 的均值以外模式。

定义减去 baseline 的两个目标
$$
T_{1,k}=\frac{a_L^2m_{L,k}-a_C^2m_{C,k}}{ik}-\int_C^L a l^b_k,
$$
$$
T_{2,k}=a_Ln_{L,k}-a_Cn_{C,k}-ik a_C^2m_{C,k}I
-\int_C^L(a'-k^2aJ)l^b_k. \tag{8}
$$

## 3. 明确可逆的 Gram 控制

令
$$
\mu(s)=a(s)b(s),\quad A=\int_C^L\mu>0,\quad
q_k(s)=\frac{c(s)}{k^2}-J(s),\quad
\bar q_k=\frac1A\int_C^L\mu q_k,
$$
$$
V_k=\int_C^L\mu(q_k-\bar q_k)^2. \tag{9}
$$
则每个非零偶 $k$ 都有 $V_k>0$。事实上
$$
q_k'=\frac{k^2+a a''-(a')^2}{k^2a^2},
$$
在 (1) 的区间内因此满足
$$
q_k'\ge\frac{\eta}{a^2}>0\qquad (|k|\ge2). \tag{10}
$$
所以 $q_k$ 不可能在正权重支撑上恒定。

这种正性还对全部偶波数一致。任取两个有正距离 $d$ 的闭子区间 $F_1<F_2\Subset F$。若 $a\le a_*$ 于 $F$，记 $M_j=\int_{F_j}\mu>0$，则由方差恒等式
$$
V_k=\frac{1}{2A}\iint\mu(s)\mu(t)(q_k(s)-q_k(t))^2\,ds\,dt
$$
及两矩形 $F_1\times F_2,F_2\times F_1$ 得
$$
V_k\ge \frac{M_1M_2}{A}
\left(\frac{\eta d}{a_*^2}\right)^2>0. \tag{11}
$$
该界不因 $|k|\to\infty$ 退化，也不要求更改当前物理度量。

现在明确定义
$$
x_k=\frac{T_{1,k}}A,\qquad
y_k=\frac{T_{2,k}/k^2-\bar q_k T_{1,k}}{V_k},
$$
$$
l_k(s)=l^b_k(s)+b(s)\{x_k+y_k(q_k(s)-\bar q_k)\}. \tag{12}
$$
第一矩的增量是 $Ax_k=T_{1,k}$。因为 $a'-k^2aJ=k^2a q_k$，第二矩的增量准确为
$$
k^2\int\mu q_k\{x_k+y_k(q_k-\bar q_k)\}
=k^2(\bar q_k T_{1,k}+y_kV_k)=T_{2,k}.
$$
所以 (6)–(7) 同时成立。所有分母是已经明确正的 $a,A,V_k$，从未除以未知第二基本形式分量 $n$。

## 4. 零模、实性及 D2

令
$$
M_0=\int_C^L(a')^2b>0,\qquad
T_0=a_Ln_{L,0}-a_Cn_{C,0}-\int_C^L a'l^b_0.
$$
取
$$
l_0=l^b_0+\frac{T_0}{M_0}a'b. \tag{13}
$$
于是 $(an_0)_s=a'l_0$ 给正确右端迹；$m_0=a_C^2m_{C,0}/a^2$ 则由 (3) 给正确右端迹。$M_0>0$ 是第1节明确列出的条件。如果整个度量为常半径，则应改为保留必要条件 $a_Ln_{L,0}=a_Cn_{C,0}$，而不能用 (13) 除以零。

对于实数据，负模等于正模的复共轭，所有实的控制权重只依赖 $k^2$，故构造仍为实函数。对于 D2 数据，$n_k,l_k$ 为实偶系数，$m_k$ 为纯虚奇系数；$m_k/(ik)$ 与 $ikm_k$ 为实偶系数。由 (8)、(12) 和 (4)–(5) 可见 D2 完整保留。$k=\pm1$ 从未被允许混入这条非退化论证。

## 5. 完整函数、正则性及 collar

有限 Fourier 数据时，上式直接给实际有限函数的准确线性 Codazzi 解。若输入是完整无限函数，则不得先截断其边界高模后称为原边界解。

下面给一个足以合法逐项求导的明确条件。令 $\mathcal A^r$ 表示 Fourier 绝对和 $\sum_k(1+|k|)^r|f_k|$ 有限的周期函数空间。若全部边界数据属 $\mathcal A^{r+2}$，baseline 及其一阶 $s$ 导数在 $[C,L]$ 上连续取值于 $\mathcal A^{r+2}$，其中 $r\ge1$，则以上构造给 $l\in C^1_s\mathcal A^{r+2}$、$m\in C^1_s\mathcal A^{r+1}$、$n\in C^1_s\mathcal A^r$。

证明如下。$q_k$ 及其 $s$ 导数对 $|k|\ge2$ 一致有界，(11) 给 $V_k$ 一致正下界。(8) 中经 $k^2$ 归一化的第二目标为
$$
\frac{T_{2,k}}{k^2}=\frac{a_Ln_{L,k}-a_Cn_{C,k}}{k^2}
-\frac{i}{k}a_C^2m_{C,k}I-\int a q_k l^b_k.
$$
所以 (12) 及其 $s$ 导数由 baseline、$m_{C/L,k}/k$ 与 $n_{C/L,k}/k^2$ 的统一常数控制。公式 (4) 最多损失一个角导数，(5) 最多再损失一个；(2) 同时给相应 $s$ 导数的同样界。绝对一致收敛遂允许积分、角微分和径向微分交换，(2) 点态成立。此条件用于本构造的充分函数空间；不是给课题完成标准额外增设 C³ 或 C⁴ 验收门。具体有限或解析边界可直接按其实际定义消费。

由于 $b$ 在端点开放邻域为零，完整 $l$ 与 baseline 在那里完全相等，所有已有的端点 $l$ jets 均保留。若某一端 collar 内 baseline 是一个满足相同度量 (2) 的准确模型，且该模型在端点的 $n,m$ 也正是指定数据，则 (4)–(5) 的线性初值唯一性（右端可向左解）说明全部 $(n,m,l)$ 在该 collar 上与该模型相等。该结论保留的是整个准确角函数，不只是有限采样或部分迹。

## 6. 固定物理域上的参数导数

若 $a$、baseline 与边界数据依赖有限参数 $p$，而物理端点、$b$ 及非退化保护区间固定，则所有公式可准确求参数导数。对任一参数方向，用点号表示方向导数：
$$
\dot J(s)=-2\int_s^L\dot a/a^3,
\qquad \dot q_k=\dot c/k^2-\dot J,
\quad \dot\mu=\dot a b,\quad \dot A=\int\dot\mu,
$$
$$
\dot{\bar q}_k=\frac{\int(\dot\mu q_k+\mu\dot q_k)-\bar q_k\dot A}{A},
$$
$$
\dot V_k=\int\dot\mu(q_k-\bar q_k)^2+
2\int\mu(q_k-\bar q_k)\dot q_k. \tag{14}
$$
最后一式中 $\dot{\bar q}_k$ 项由零均值准确消失。进而
$$
\dot x_k=(\dot T_{1,k}-x_k\dot A)/A,
$$
$$
\dot y_k=\frac{\dot T_{2,k}/k^2-\dot{\bar q}_kT_{1,k}
-\bar q_k\dot T_{1,k}-y_k\dot V_k}{V_k}. \tag{15}
$$
把 (14)–(15) 代入 (12)，再对 (4)–(5) 求导，即得完整参数列。这里 $T$ 的导数包括边界值、$a_C,a_L,I$ 及 baseline 各项；不能把改变物理度量的导数误当成单纯 lifting 权重导数。零模 (13) 按商法则处理即可。

## 7. 对后续有限求解的范围

若在固定物理角 $u$ 使用有限 Fourier correction，则 (2) 的角微分及仅依赖 $s$ 的系数不会产生新的角模式；准确 Codazzi lifting 的高角 forcing 因而为零。有限 correction 仍须满足自己的完整线性 Codazzi，而非线性 Gauss 残差
$$
G=nl-m^2+a''/a
$$
仍必须全角计算并求解。若改在非均匀移动角图中表示 correction，链式漂移与 $U_\xi^{-1}$ 可重新产生高模；本定理不替这些模式免单。

本结论也没有给 $n$ 正性、主曲率上界、metric 后验、位置或标架 monodromy、切口实际高度、全局 reach、强位移比或网格。即使 II 在两端准确 collar 相同，实际 Cartesian 图仍须按 R117/R126/R133 的条件完成位置和二 jet 接合。数值化时，任意积分或无限角函数近似都要如实保留缺陷，不能把本准确线性构造当作已经完成非线性闭曲面。


## 8. 实际有限原型及其未完成部分

`fd2d_codazzi_moment_lifting_probe.py` 已以 coast09 末态的同一 38 参数和同一物理度量真实运行。固定材料角上 1024 采样定义 63 个非零偶模（最大整数波数126）的明确有限边界多项式；它不是原无限边界的无损表示。16点分片 Gauss 构造控制后，以独立24点规则消费相同控制，右端材料迹缺陷为 $2.107\times10^{-10}$，Gram 的有限最小 $V_k$ 约 $.05748$，没有观察到数值奇异。

该原型仍不是可用非线性解：左、右完整边界的实际截断最大误差分别为 $.07043469$ 和 $6.1155\times10^{-5}$；格内 Gauss 最大残差约 $11.8781$，虽形式主曲率样本约 $4.45325$，不能由这个样本推断实际位置曲率或合格几何。报告明确保留这些误差，以及积分并非准确积分的限制。完整控制、源身份和真实退出见 `notes/2026-11-12-fd2d-codazzi-moment-lifting01-report.json` 与对应 closed-manifest。该实际结果支持直接使用完整函数 lifting 的必要性，不把低角多项式冒充全边界解。
