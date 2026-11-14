# R50：中心频带的精确支持与分块全频头部比较定理

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明。** 本文把 R33 的完整源恒等分解与真实有限频带相接，证明二次中心线性项的严格零块，给出复用现有真实核的安全分带法及完整 641 行条件存在定理。它修正的是比较算子的频率聚合；不更换真实方程、度规、连续角宽、辅助中心或深尾图。

本文不宣称当前 641 行数值门已经通过。R49 给出的旧标量比较算子两循环障碍依旧成立；这里定义的是保留更多实际支持信息的新比较算子。完整 mean、乘法逆和变化的二次项从未被删除。

## 1. 同一个全频空间与辅助中心

沿用 [R33](R33-full-head-forcing-on-a-variable-analytic-strip.md) 的物理归一变量

$$
u_1=Bp/V,\qquad u_2=\kappa_\perp/V
$$

和每个胞元的强范数

$$
\|u\|_{\mathcal X_n}
=\sum_{m\in2\mathbb Z\setminus\{0\}}(1+|m|)
\left[
\sup_{r\in I_n}e^{\tau(r)|m|}|u_{1,m}(r)|
+\sup_{r\in I_n}e^{\tau(r)|m|}|u_{2,m}(r)|
\right].
\tag{50.1}
$$

两个分量分别先取径向 supremum，再对全部 signed 频率求和；频率投影不增加这个范数。

固定 R38/R39 对应的真实 46 模辅助低解 $L$，并要求本文全部输入使用同一个 $g,V,B,\tau,L$。它的非均值支持满足

$$
\operatorname{supp}_\theta L
\subset\{m\in2\mathbb Z:2\le|m|\le92\},
\qquad \|L\|_{\mathcal X_n}\le1.
\tag{50.2}
$$

完整 mean 是 R33 的唯一小根，不是独立的第 47 个非均值模式。
将全新变化按**实际不相交的频率支持**分成

$$
\begin{aligned}
\Lambda_{\mathrm L}&=\{m:2\le|m|\le92\},&
\Lambda_{\mathrm N}&=\{m:94\le|m|\le184\},\\
\Lambda_{\mathrm R}&=\{m:186\le|m|\le8190\},&
\Lambda_\infty&=\{m:|m|\ge8192\},
\end{aligned}
\qquad m\in2\mathbb Z .
\tag{50.3}
$$

对应变量记为 $v_{\mathrm L},v_{\mathrm N},v_{\mathrm R},v_\infty$，总变化为 $v$。前面三块各有 213 个胞元范数，最后一块保留原无限窗的单个全域范数。深参数仍独立保留全部 46 维；其归一半径记为 $r_z$。

## 2. 二次主部的严格频率支持

R33 §16 给出的完整恒等式为

$$
f(L+v)-f(L)=DQ(L)v+Q(v)+R(L+v)-R(L).
\tag{50.4}
$$

这里 $Q$ 恰为

$$
Q(u)=\mathscr P_\perp
\left[
Ed_1(\partial_\theta u_2-u_1/B)^2
+\epsilon_\lambda d_\lambda
\left\{(u_2+\partial_\theta u_1/B)^2
+w^2\left(2u_2\partial_\theta u_1/B
+(\partial_\theta u_1/B)^2-(u_1/B)^2\right)\right\}
\right].
\tag{50.5}
$$

所有径向系数 $E,d_1,d_\lambda,w,B,\epsilon_\lambda$ 与 $\theta$ 无关。角导数保留 Fourier 支持，乘法使频率相加。因此，$DQ(L)v$ 的任一输出模式均满足

$$
m=j+b,\qquad j\in\operatorname{supp}_\theta L,\quad
b\in\operatorname{supp}_\theta v .
\tag{50.6}
$$

投影 $\mathscr P_\perp$ 只删除 $m=0$，不产生新频率。

**引理 50.1。** 在 (50.2) 下，$DQ(L)$ 关于 (50.3) 的支持表如下。行是输出，列是输入；$0$ 表示真实算子严格为零，$\ast$ 只表示可能非零。

| 输出 / 输入 | $\mathrm L$ | $\mathrm N$ | $\mathrm R$ | $\infty$ |
|---|---:|---:|---:|---:|
| $\mathrm L$ | $\ast$ | $\ast$ | $0$ | $0$ |
| $\mathrm N$ | $\ast$ | $\ast$ | $\ast$ | $0$ |
| $\mathrm R$ | $0$ | $\ast$ | $\ast$ | $\ast$ |
| $\infty$ | $0$ | $0$ | $\ast$ | $\ast$ |

**证明。** 由 (50.6)，必有 $||m|-|b||\le|j|\le92$。低输出 $|m|\le92$ 迫使 $|b|\le184$；低输入也迫使输出 $|m|\le184$。近端输出 $|m|\le184$ 与无限输入 $|b|\ge8192$ 的差至少为 $8008>92$，故相应两向均为零。表中其余块未被此条件排除；例如 $m=94,b=92,j=2$ 和 $m=8192,b=8190,j=2$ 给相邻块的实际非零频率关系。故整个表成立。证毕。

若中心仅取真实线性模式 $\pm2$，跨块主线性项进一步只经过 $92\leftrightarrow94$、$184\leftrightarrow186$、$8190\leftrightarrow8192$ 三对界面频率。本文的完整中心仍包含其余 45 模及非线性低修正，故实际联合证明使用带宽 92 的表，不能把整个中心当作模式 2。

### 2.1. 这些零块在真实传播后仍为零

R29/R33 的背景线性系统、真实 $\phi/\psi$ Green 核、因果高传播和 canonical/物理变量变换都按同一个 $m$ 分解。其系数只依赖真实径向坐标。于是它们与上述频率投影交换。

因此先做 $DQ(L)$ 再做线性传播不会改变 (50.6)，不会把 $\mathrm R$ 输出重新变成低输出。低 far evaluation 也只读取低 46 模，所以其中心线性项同样只依赖 $v_{\mathrm L}+v_{\mathrm N}$。

真实非线性深尾图 $D(z)$ 并不是上述背景线性算子。它的边界提升和导数仍按完整 R18/R43 界保留；本引理不删除任何深参数列。

## 3. 两材料、固定质量与完整余项的量词

中心拆分仍为 $L=L_{2,\mathrm{lin}}+R_c$，其中 $R_c$ 的支持也在 $\Lambda_{\mathrm L}$。R33 §16.7 使用先逐模取径向 supremum 的固定非负质量 $\eta_j$，满足

$$
\eta_j=0\quad(j\notin\Lambda_{\mathrm L}),
\qquad \sum_j\eta_j\le1.
\tag{50.7}
$$

若变化的固定谱质量为 $x_b$，修正中心产生的源质量由
$3(\eta*x)_m$ 和真实材料 $\varepsilon(r)(d_1+d_\lambda)$ 支配。
对主模式 2，相应质量为 $(x_{m-2}+x_{m+2})/2$，真实材料仍为 R33.101 的 $g_1d_1+g_\lambda d_\lambda$。把 $x$ 限制到任一真实频块后，上述卷积支持恰满足引理 50.1。

固定质量的定义顺序没有改变：每个 $x_b,\eta_j$ 已经先取所要求的径向 supremum，再按非负级数求和。本文没有把点态 $\sum_m|f_m(r)|$ 冒充 $\sum_m\sup_r|f_m(r)|$，也没有免费提升角宽。两种材料分别保持真实源系数；若沿用已证明的合并材料上界，只是进一步的正比较。

完整剩余项 $R=f-Q$ 包含全部 mean 根及整个乘法逆。令 $A_n=\sup_{I_n}V/w$，$t=\|v\|_{\mathcal X_n}$，且

$$
A_n(1+t)\le1/64.
\tag{50.8}
$$

R33 的实际余项界给

$$
\|Q(v)\|_{\mathcal Y_n}\le\tfrac32t^2,\qquad
\|DQ(v)\|\le3t,
\tag{50.9}
$$

$$
\|R(L+v)-R(L)\|_{\mathcal Y_n}
\le216A_nP(t),\qquad
P(t)=t+t^2+t^3/3 .
\tag{50.10}
$$

若余项核已经包含点态 $a(r)=V(r)/w(r)$，则外乘 $216P(t)$，不再乘一遍 $A_n$。

**(50.9)–(50.10) 始终使用所有频块的总 $t$。**
例如两个相邻高频可相减产生低频，因此 $Q(v)$ 的高到低部分不能删去。完整 mean 的导数会依赖全频输入，乘法逆也有无限支持；故表中的零项不能借给 $R$。这是二次主部与完整方程之间的必要区别。

## 4. 从已有十一窗核得到两个真实频块

现有高核的比较频窗为

$$
[94,96],[98,104],[106,112],[114,128],[130,192],
[194,256],[258,512],[514,1024],[1026,2048],
[2050,4096],[4098,8190].
\tag{50.11}
$$

它们都是偶数频率窗。编号从 0 开始，原 maximizing band 6 是 $258$ 至 $512$。

设 $\Gamma_{kn}^{(b)}$ 是旧窗 $b$ 对真实源胞元 $n$ 到输出胞元 $k$ 的已证明算子上界。定义

$$
H^{\mathrm N}_{kn}
=\max_{0\le b\le4}\Gamma_{kn}^{(b)},\qquad
H^{\mathrm R}_{kn}
=\max_{4\le b\le10}\Gamma_{kn}^{(b)} .
\tag{50.12}
$$

这里实际变量仍按 $184/186$ 分开。旧窗 $[130,192]$ 的整窗上界可以分别用于真实子集 $[130,184]$ 与 $[186,192]$，因为频率限制是范数不增的投影。两个真实变量没有重叠，也没有声称新做了端点 184 的基本解积分。

**引理 50.2。** (50.12) 分别给 $\Lambda_{\mathrm N}$ 和 $\Lambda_{\mathrm R}$ 的真实因果源算子上界。

**证明。** 在固定源胞元把已先取径向 supremum 的源谱质量记为 $q_m\ge0$。对属于旧窗 $b$ 的单个频率，真实传播后的强质量至多为 $\Gamma_{kn}^{(b)}q_m$。在近端实际支持上相加，得到

$$
\sum_{m\in\Lambda_{\mathrm N}}
\Gamma_{kn}^{(b(m))}q_m
\le H^{\mathrm N}_{kn}\sum_{m\in\Lambda_{\mathrm N}}q_m.
$$

远端同理。旧窗 4 内的两个真实子集分别使用同一个有效上界，不改变其实际不相交性。证毕。

若已有逐旧窗的纯低响应 $b_{k,b}^{\mathrm{pure}}$ 或真实 far 响应 $b_{k,b}^{\mathrm{far}}$，则按两个覆盖分别取和。窗 4 的整窗响应上界在两个比较和中各计一次，是允许的保守重复；不能把重复的比较上界解释成重复的实际模式。

这个构造只消费原真实矩阵和原源包。新的派生程序保留原传播运算次序，逐项检查两组最大值的最大值等于旧完整 $\Gamma$，并复核旧纯低响应及缩放后的旧 far 响应。新分组没有自动通过非线性联合门。

## 5. 完整 641 行比较映射

记半径为 $l_n,a_n,b_n$（分别对应低、近端、其余中窗），无限窗半径为 $h$，深参数归一半径为 $r_z$。此处 $a_n,b_n$ 只是本节半径符号，不替代 R33 的点态背景系数。定义

$$
s_n=l_n+a_n,\qquad t_n=l_n+a_n+b_n+h.
\tag{50.13}
$$

令
$C^0=M+3C$、$F^0=F_M+3F_C$，其余四核 $Q,R,F_Q,F_R$、$\beta_k,\beta_z$、$\gamma_\infty$ 与真实独立 far 球 $Z$ 完全沿用 R42/R43。低和 far 行的 $R,F_R$ 已包含点态 $V/w$。对高行仍用

$$
K_n(t)=3t+\tfrac32t^2+216A_nP(t).
\tag{50.14}
$$

一个完整且保守的正映射为

$$
\begin{aligned}
\Phi_{\mathrm L,k}
&=\sum_n[C^0_{kn}s_n+\tfrac32Q_{kn}t_n^2
+216R_{kn}P(t_n)]+\beta_kr_z,\\
\Phi_{\mathrm N,k}
&=b_k^{\mathrm{pure,N}}+b_k^{\mathrm{far,N}}
+\sum_nH^{\mathrm N}_{kn}K_n(t_n),\\
\Phi_{\mathrm R,k}
&=b_k^{\mathrm{pure,R}}+b_k^{\mathrm{far,R}}
+\sum_nH^{\mathrm R}_{kn}K_n(t_n),\\
\Phi_\infty
&=b_\infty^{\mathrm{pure}}+b_\infty^{\mathrm{far}}
+\gamma_\infty\sum_nK_n(t_n),\\
\Phi_z
&=Z^{-1}\sum_n[F^0_ns_n+\tfrac32F_{Q,n}t_n^2
+216F_{R,n}P(t_n)]+\beta_zr_z .
\end{aligned}
\tag{50.15}
$$

共有 $3\cdot213+2=641$ 行。第一版只在低/far 中心线性项使用严格支持；高行的 $3t_n$ 仍保守包含所有输入。这已是完整有效的比较映射。

若需进一步收紧，高行中心线性项的 $3t_n$ 可依次替换为
$3(l_n+a_n+b_n)$、$3(a_n+b_n+h)$、$3(b_n+h)$，对应近端、其余中窗、无限窗；其二次项和完整余项仍用全 $t_n$。这些替换直接来自引理 50.1，不能同时改动纯低或 far 边界项。

## 6. 完整导数门与条件存在

取提案总域 $t_n\le\rho$。对非负差向量 $W$，记

$$
S_n=W_{\mathrm L,n}+W_{\mathrm N,n},\qquad
T_n=W_{\mathrm L,n}+W_{\mathrm N,n}
+W_{\mathrm R,n}+W_\infty .
\tag{50.16}
$$

定义

$$
D_{kn}=3\rho Q_{kn}+216(1+\rho)^2R_{kn},\quad
D^F_n=3\rho F_{Q,n}+216(1+\rho)^2F_{R,n},
$$

$$
k'_n=3(1+\rho)+216A_n(1+\rho)^2 .
\tag{50.17}
$$

对真实固定点算子差的正导数上界可取

$$
\begin{aligned}
(JW)_{\mathrm L,k}
 &=\sum_n[C^0_{kn}S_n+D_{kn}T_n]+\beta_kW_z,\\
(JW)_{\mathrm N,k}
 &=\sum_nH^{\mathrm N}_{kn}k'_nT_n
+4b_k^{\mathrm{far,N}}W_z,\\
(JW)_{\mathrm R,k}
 &=\sum_nH^{\mathrm R}_{kn}k'_nT_n
+4b_k^{\mathrm{far,R}}W_z,\\
(JW)_\infty
 &=\gamma_\infty\sum_nk'_nT_n+4b_\infty^{\mathrm{far}}W_z,\\
(JW)_z
 &=Z^{-1}\sum_n[F^0_nS_n+D^F_nT_n]+\beta_zW_z.
\end{aligned}
\tag{50.18}
$$

高 far 项在 (50.15) 中使用整个独立参数球的统一值，因而写成常数；其真实参数导数仍由 (50.18) 的 $4b^{\mathrm{far}}$ 列支付。$J$ 是真实算子的导数上界，不能因比较映射的常数写法而删掉该列。

**定理 50.3。** 假设所有核、纯低响应、真实深图提升和 reference 身份确已包围同一个实对象，且原全频 Green 映射在 R33 空间中有定义。若存在严格正的 641 个半径 $x$ 和 641 个距离权 $W$，满足

$$
\Phi_i(x)<x_i,\qquad
\max_nt_n<\rho,\qquad
A_n(1+t_n)<1/64,
\tag{50.19}
$$

$$
\|z_{\rm aux}\|_{38}+Zr_z<Z,\qquad
\max_i\frac{(JW)_i}{W_i}<1,
\tag{50.20}
$$

则原完整非线性头部在该闭盒内有唯一解，含全部偶 Fourier 频率、完整 mean 和真实 R18 深尾接合。浅端的高频高度是输出，不另加为零的 Dirichlet 条件。

**证明。** (50.4)、两材料固定谱质量界及频率投影不增性给低/far 行；引理 50.2、完整 $K_n$ 和原无限窗核给其余行，故 (50.15) 是完整算子的逐块包络。(50.19) 使闭盒不变，并确保完整 mean 和乘法逆的同一解析分支。独立深域由 (50.20) 第一式包含。

在以 $W_i$ 加权的积 Banach 范数中，沿闭盒内任意线段积分真实导数；(50.18) 及 (50.20) 给严格小于 1 的 Lipschitz 常数。Banach 不动点定理给存在与唯一性。线性 Green 构造的边界约束和完整深图是原固定点方程的一部分，故不动点满足它们。mean 由同一个唯一小根恢复；一个统一高度积分常数按原 cuff 约定固定。由 R33/R43 的正则性与真实流等价结论得到原全频头部，而不是仅有限投影解。证毕。

427 维的正因子提案可使用 $(s_n,t_n,z)$ 生成候选半径和权，但最终应逐项核算 (50.19)–(50.20) 的原 641 行。降维提案本身不是新的存在门。

## 7. 当前小诊断的准确范围

只读浮点四胞元诊断重组了 source 15 到 output 12 的十一条旧带响应。原最大值约为 $14.4661463601$，来自带 6；旧近端覆盖 $0,\ldots,4$ 的最大值约为 $7.47622825\cdot10^{-8}$，来自 $94$ 至 $96$ 带。与现有低 corr edge 的旧两循环乘积约 $1.20008464$ 相比，近端对应浮点乘积约为 $6.20214\cdot10^{-9}$。

上述浮点读数本身只是定位信息。随后完整分带派生程序 tail_middle_frequency_split.py 已真实完成，session 47121 正式退出 0，输出 [完整分带包](../notes/2026-11-12-tail-r50-split-middle-r1.json.gz)。在导出向上 dyadic 之前，22,791 个原因果核值、全部纯低响应和缩放后的原 far 响应均逐位复现。近端该 edge 的内部严格上界为

$$
H^{\mathrm N}_{12,15}
\le 7.476228247980188\cdot10^{-8}.
$$

文件中的各 $\Gamma$ 再向上舍入为 32 位 dyadic，相对放大严格小于 $2^{-31}$；后续联合门使用文件内上界，不使用以上浮点显示。共享窗 $[130,192]$ 的两个比较覆盖仍分别明示。

该作业约 70 秒，峰 RSS 为 68,544 KiB；没有做新的 ODE、source 积分或频窗端点 184 的积分。它完成了 (50.12) 和相应纯低/far 分带输入，尚不表示 (50.19)–(50.20) 的完整 641 行门已经通过。所有旧失败包保留。
