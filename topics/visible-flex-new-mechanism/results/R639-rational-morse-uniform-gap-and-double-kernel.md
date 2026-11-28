# R639：有理 Morse 中心、全部整数的共同谱隙与真实双核平尾

2026-11-28。**本稿给一个比 R633 更强的参考背景：除第二、第三角模的两条指定核外，其余全部整数角模的参考逆不损失角阶。** 方法是在一个有理 Morse 谱中先作统一的小常势平移，再在充分左侧正区恢复两条指定核。恢复的代价对全部 $j\ge4$ 同时受控，因此原谱可能具有的额外 Pell 零模也全部被移开。

本稿不把这个参考逆直接称为状态相关逆或非线性解。它支付的是 Hu 体源逆比较中必须具有的一个实际输入：同一角阶上的参考 Green 界。R633 的 $j^2$ 界本身不能替代该输入，因为负曲率组件上的比较项是零阶势差，不能在一个固定 Sobolev 源空间中直接对 $\delta V\,\mathcal G_*$ 作小范数 Neumann 逆。

本稿最后关于非零端口的推论使用 R637 已由实际公开 Actions 成功支付的严格全线球输入；具体运行和准确有理包围由 R637 正文登记。

## 1. 一个有理参数族及其完整谱

取实数 $s>2$，设

$$
A=s^2,\qquad
B(s)=\frac{(5s-4)(s-2)}{20},\qquad
\eta(s)^2=\frac{36s-27}{20},
$$
$$
\rho_s(X)=s^2(e^{-X}-e^{-2X})-B(s),\qquad
H_{j,s}=-\partial_X^2+\eta(s)^2-j^2\rho_s(X).
                                                               \tag{1}
$$

这里 $B>0$，而

$$
\max\rho_s=\frac{7s-4}{10},\qquad
\eta(s)^2-\max\rho_s=\frac{22s-19}{20}>0.               \tag{2}
$$

R630 的 Morse 化约逐项适用于 (1)。其全部离散能级为

$$
E_{j,N}(s)=\eta(s)^2+j^2B(s)-\frac{(js-N)^2}{4},
\quad N=2n+1>0,\quad N<js,                              \tag{3}
$$

本质谱从 $\eta(s)^2+j^2B(s)$ 开始。对每个 $j$，离散能级简单；这些断言使用的自然实现为整条 $X$ 轴上的 $L^2(dX)$ 实现。

置

$$
U_{j,N}=36-14j^2+10jN,\qquad
V_{j,N}=8j^2-5N^2-27.
$$

准确恒等式为

$$
20E_{j,N}(s)=sU_{j,N}+V_{j,N}.                         \tag{4}
$$

故对所有 $s>2$，$(j,N)=(2,1),(3,3)$ 都是零能。相应未归一化核为

$$
\psi_2(X)=t^{s-1/2}e^{-2st},\qquad
\psi_3(X)=t^{(3s-3)/2}e^{-3st}\bigl[(3s-2)-6st\bigr],
\quad t=e^{-X}.                                       \tag{5}
$$

现在令 $s=p/q$，其中 $p,q$ 为互素正整数。由 (4)，

$$
20q E_{j,N}=pU_{j,N}+qV_{j,N}\in\mathbb Z.
$$

所以每个**非零**离散能级都满足

$$
|E_{j,N}|\ge d_s:=\frac1{20q}.                        \tag{6}
$$

本质谱也与零有统一距离。可以把 $d_s$ 缩小为与本质谱阈值的最小值；在本文所用 $s$ 的邻域内，(6) 已更小。这里没有声称有理参数只具有两条零模：$pU+qV=0$ 可能还给额外整数解。下一节会同时处理它们，不需要枚举该 Pell 型方程。

### 1.1 二次无理行程角

唯一负曲率组件的行程角为

$$
T_s=\int_{\rho_s>0}\sqrt{\rho_s}\,dX=\pi\alpha_s,
\qquad \alpha_s=\frac s2-\sqrt{B(s)}.                 \tag{7}
$$

取 $s$ 于 $\sqrt5$ 的一个固定小闭邻域，例如
$11/5\le s\le23/10$。在其中 $0<\alpha_s<1$，共轭数
$\alpha_s'=s-\alpha_s$ 位于 $(1,2)$。它们满足

$$
10q\alpha^2-10p\alpha+7p-4q=0.                       \tag{8}
$$

若 $B(s)$ 不是有理数的平方，则 $\alpha_s$ 为二次无理数。对 $j\ge1$，取最靠近 $j\alpha_s$ 的整数 $m$。此时 $0\le m/j\le3/2$，且 $|m/j-\alpha_s'|<2$。由 (8) 的非零整数分子，

$$
\frac1{j^2}
\le\left|10q(m/j)^2-10p(m/j)+7p-4q\right|
\le20q\left|m/j-\alpha_s\right|.
$$

结合 $|\sin\pi x|\ge2\operatorname{dist}(x,\mathbb Z)$，得到

$$
\boxed{|\sin(jT_s)|\ge\frac1{10qj}\quad(j\ge1).}       \tag{9}
$$

这一次是全部正整数，且只损失一阶角导数。

所需有理参数可以任意逼近 $s_0=\sqrt5$。具体地取 $q=2^k$，取奇数 $p$ 且 $p-2q$ 不被 $5$ 整除，并令 $p/q$ 逼近 $s_0$。每十个连续整数中都有这种 $p$，所以误差可取 $O(2^{-k})$。因 $5p-4q$ 不被 $5$ 整除，

$$
v_5(B(p/q))=-1,
$$

故 $B(p/q)$ 不可能是有理平方。此选择同时保留有理谱量子 (6) 和二次无理角界 (9)。

## 2. 两个左正区控制准确恢复第二、第三核

本节先固定一个上述有理 $s$；所有常数允许依赖这个固定选择。令 $t=e^{-X}$。固定非负且不恒为零的

$$
\chi\in C_c^\infty((-1/10,1/10)).
$$

对有限 $L>3$，取

$$
\chi_{1,L}(X)=\chi(t-L),\qquad
\chi_{2,L}(X)=\chi(t-L-1),\qquad
\zeta_\tau=\tau_1\chi_{1,L}+\tau_2\chi_{2,L}.           \tag{10}
$$

它们位于严格正曲率区。另引入小常数 $\varepsilon>0$，令

$$
\eta_\varepsilon=\sqrt{\eta^2+\varepsilon},\qquad
\mathcal P_{\varepsilon,\tau}
=\exp(-2\eta_\varepsilon X+2\zeta_\tau),
$$
$$
Q_{\varepsilon,\tau}
=\zeta_\tau''-2\eta_\varepsilon\zeta_\tau'
                       +(\zeta_\tau')^2,
$$
$$
H_{j,\varepsilon,\tau}
=H_{j,s}+\varepsilon+Q_{\varepsilon,\tau}.              \tag{11}
$$

这里仍准确固定 $\rho_s$。因此 (7) 的负区及其行程角都不变。

在 $(\varepsilon,\tau)=(0,0)$ 附近，第二、第三模的简单零能有光滑实延拓 $e_2(\varepsilon,\tau),e_3(\varepsilon,\tau)$。把 (5) 各自作 $L^2$ 归一化，Hellmann–Feynman 给

$$
\partial_{\tau_i}e_j(0,0)
=\int\psi_j^2(\chi_{i,L}''-2\eta\chi_{i,L}')\,dX
=\int W_j\chi_{i,L}\,dX,
$$
$$
W_j=(\partial_X^2+2\eta\partial_X)(\psi_j^2).
                                                               \tag{12}
$$

记这个 $2\times2$ 矩阵为 $A_L$。

### 2.1 满秩和恢复代价的指数

由 (5)，当 $t\to\infty$ 时

$$
W_2=c_2t^{2s+1}e^{-4st}(1+O(t^{-1})),\qquad
W_3=c_3t^{3s+1}e^{-6st}(1+O(t^{-1})),                 \tag{13}
$$

其中 $c_2,c_3>0$；$L^2$ 归一化只改变这些正数。由于 $dX=-dt/t$，(12) 的两行分别具有尺度

$$
a_2(L)=c_2L^{2s}e^{-4sL},\qquad
a_3(L)=c_3L^{3s}e^{-6sL}.
$$

准确地，

$$
\operatorname{diag}(a_2(L),a_3(L))^{-1}A_L
\longrightarrow
\begin{pmatrix}
C_2&e^{-4s}C_2\\
C_3&e^{-6s}C_3
\end{pmatrix},
\quad
C_2=\int\chi(y)e^{-4sy}dy>0,\quad
C_3=\int\chi(y)e^{-6sy}dy>0.                            \tag{14}
$$

极限行列式为 $C_2C_3(e^{-6s}-e^{-4s})\ne0$。所以对所有充分大的有限 $L$，$A_L$ 可逆，且存在固定常数 $C,M$，

$$
\|A_L^{-1}\|\le C L^M e^{6sL}.                        \tag{15}
$$

这里只需要上界，故允许把 $L$ 的负幂统一放大为 $L^M$。注意两个 bump 的 $X$ 宽度为 $O(L^{-1})$，其固定阶导数只产生 $L$ 的固定幂，不产生新的指数。

有限维隐函数定理因而给一条光滑曲线 $\tau=\tau(\varepsilon)$，

$$
\tau(0)=0,\qquad
e_2(\varepsilon,\tau(\varepsilon))
=e_3(\varepsilon,\tau(\varepsilon))=0.                 \tag{16}
$$

固定这个 $L$ 后，缩小一次正的 $\varepsilon$ 范围，可以取有限常数 $C_L\ge1$，满足

$$
\|Q_{\varepsilon,\tau(\varepsilon)}\|_\infty
\le C_L\varepsilon,
\qquad C_L\le C L^M e^{6sL}.                           \tag{17}
$$

例如先用 $\|\tau(\varepsilon)\|\le2\|A_L^{-1}\|(1,1)\|\varepsilon$，再展开 (11)；二次项通过缩小这个有限的 $\varepsilon$ 范围吸收。以后先选一次 $L$，再选一次 $\varepsilon$；不会把 $L\to\infty$ 当最终曲面的一个极限部件。

## 3. 对所有额外零模同时有效的质量估计

这一节给 (17) 不会重新制造高频零能的实际估计。它同时包含每个低整数 $j\ge4$，不只是一条 $j\to\infty$ 渐近式。

考虑

$$
\widetilde H_j=H_{j,s}+\varepsilon+\theta Q,
\quad 0\le\theta\le1,\quad
Q=Q_{\varepsilon,\tau(\varepsilon)},
$$

并假定 $\varepsilon+\|Q\|_\infty\le d_s/4$。若 $u$ 是一个归一化实特征函数，$\|u\|_2=1$，其特征值满足 $|E|<d_s/2$，则有以下统一界。

### 3.1 固定截面上的幅值

全线能量身份给

$$
\|u'\|_2^2
=E-\eta^2-\varepsilon-\theta\int Q u^2
                         +j^2\int\rho_su^2
\le Cj^2.
$$

一维 $H^1$ 不等式因此给

$$
|u(X)|^2\le2\|u\|_2\|u'\|_2\le Cj
\quad\text{对所有 }X.                                  \tag{18}
$$

常数与 $j,L,\theta,\varepsilon$ 无关，只需上述固定的小扰动界。

### 3.2 左正区的显式屏障

当 $t\ge2$ 时，

$$
-\rho_s=s^2(t^2-t)+B\ge s^2(t-1)^2.
$$

由 (2) 及小扰动条件，特征方程的正系数满足

$$
\eta^2+\varepsilon+\theta Q-j^2\rho_s-E
\ge j^2s^2(t-1)^2.                                    \tag{19}
$$

在整个 $t\ge2$ 区间，左 $L^2$ 解没有零点：若有一个零点，将该零点以左的正势方程乘以 $u$ 积分，会迫 $u$ 恒为零。于是可把其符号取正。

定义

$$
b_j(t)=\exp\{-js[t-2-\log(t/2)]\}.
$$

它满足 $b_j(2)=1$，并有

$$
\frac{\partial_X^2b_j}{b_j}
=j^2s^2(t-1)^2-js t
\le\eta^2+\varepsilon+\theta Q-j^2\rho_s-E.
$$

对正势一维算子使用最大值原理，结合左端 $u,b_j\to0$，可得

$$
|u(X)|\le |u(-\log2)|b_j(t).
$$

也可先在有限区间加一个趋于零的常数屏障，再令左端移到 $-\infty$；正势排除了负内极小值。因而由 (18)，

$$
|u(X)|^2\le Cj\exp\{-2js[t-2-\log(t/2)]\}.
                                                               \tag{20}
$$

令 $K_L=\operatorname{supp}\chi_{1,L}\cup\operatorname{supp}\chi_{2,L}$，并置

$$
\mathfrak a_L=(L-1/10)-2-\log((L-1/10)/2).
$$

由于 $K_L$ 的 $X$ 长度不超过 $C/L$，(20) 给

$$
\int_{K_L}|u|^2dX
\le M_{j,L}:=\frac{Cj}{L}e^{-2js\mathfrak a_L}.         \tag{21}
$$

对充分大的同一个有限 $L$，函数 $x\mapsto xe^{-2s\mathfrak a_Lx}$ 在 $x\ge4$ 上递减。因此

$$
\boxed{\sup_{j\ge4}M_{j,L}
\le M_L:=\frac{4C}{L}e^{-8s\mathfrak a_L}.}             \tag{22}
$$

这里的常数和不等式没有遗漏有限多个小整数。结合 (17)，

$$
C_LM_L\le C L^{M'}e^{-2sL}\longrightarrow0.
                                                               \tag{23}
$$

选择并固定一个使 $A_L$ 可逆且 $C_LM_L<1/2$ 的有限 $L$。该选择支付了全部额外零模的共同控制，不要求知道这些零模的具体编号。

## 4. 一次有限常势平移清除全部额外零能

在上节固定的 $L$ 后，取足够小但严格正的 $\varepsilon$，使 (16)、(17) 成立，且

$$
(1+C_L)\varepsilon<d_s/4.                             \tag{24}
$$

记最终中心为

$$
H_j^\sharp=H_{j,s}+\varepsilon+Q_{\varepsilon,\tau(\varepsilon)}.
$$

分两种原谱情况。

**原来没有零能的模式。** 原谱到零的距离至少 $d_s$。有界自伴扰动的谱距离估计和 (24) 给

$$
\operatorname{dist}(0,\operatorname{spec}H_j^\sharp)
\ge3d_s/4.
$$

**原来有零能的模式。** 简单零能与其余谱至少相距 $d_s$。沿 $H_{j,s}+\varepsilon+\theta Q$，$(-d_s/2,d_s/2)$ 中始终只有这一条简单特征值，记为 $\lambda_j(\theta)$；其余谱仍距零至少 $3d_s/4$。起点 $\lambda_j(0)=\varepsilon$。对 $j\ge4$，Hellmann–Feynman、(17)、(21)、(22) 给

$$
|\lambda_j(1)-\varepsilon|
\le\int_0^1\left|\int Q|u_{j,\theta}|^2\right|d\theta
\le C_L\varepsilon M_L<\varepsilon/2.
$$

所以所有额外零模都被移到

$$
\varepsilon/2<\lambda_j(1)<3\varepsilon/2.
$$

而 $j=2,3$ 的指定零能由 (16) 准确恢复。于是

$$
\dim\ker H_2^\sharp=\dim\ker H_3^\sharp=1,\qquad
\ker H_j^\sharp=0\quad(j\ge4),
$$
$$
\boxed{\|(H_j^\sharp)^{-1}\|_{2\to2}\le\gamma^{-1}
\quad(j\ge4),\qquad
\gamma=\min(\varepsilon/2,3d_s/4)>0.}                  \tag{25}
$$

第二、第三模在各自核正交补上也具有统一的正谱距。其有限维对称 border 因而同样有一个固定常数的逆界。该常数可能很大，但与 $j$ 无关；这才是同角阶的参考输入。

### 4.1 正 buffer 压缩所需的径向权也不损失角阶

设 $\nu=r_X/r$ 是下一节的真实径向速度。其左端与 $1+t$ 可比，右端有正有限极限，有限中心上也有正上下界。对新势的固定小邻域，直接配方给

$$
V_0^\sharp-j^2\rho_s\ge c j^2\nu^2-Cj^2.
$$

故 $H_j^\sharp u=F$ 的能量身份给

$$
j^2\|\nu u\|_2^2
\le C\bigl(|\langle F,u\rangle|+j^2\|u\|_2^2\bigr).
                                                               \tag{26a}
$$

先用 (25) 于普通 $F$，得到 $\|\nu\mathcal G_jF\|\le C_\gamma\|F\|$。对称性再给 $\|\mathcal G_j\nu F\|\le C_\gamma\|F\|$。把后者代回 (26a)，对 $u=\mathcal G_j\nu F$ 用 $|\langle\nu F,u\rangle|\le\|F\|\|\nu u\|$ 并吸收，便得

$$
\|\nu\mathcal G_j\nu F\|_2\le C_\gamma\|F\|_2.
                                                               \tag{26b}
$$

在双 border 中，紧支撑标量列的能量配对只增加一个固定有限项，同一证明适用。因此 (25) 已经支付正 buffer 压缩所需的双径向权，不是把一个无权谱隙直接搬到不相容的物理源范数。

## 5. 从 Schrödinger 势返回真实半径和 profile

不能只停在 (25)。令

$$
\mathcal P^\sharp=e^{-2\eta_\varepsilon X+2\zeta_{\tau(\varepsilon)}},
\qquad
V_0^\sharp=\eta^2+\varepsilon+Q_{\varepsilon,\tau(\varepsilon)}.
$$

取左正规的正解

$$
(\psi_1^\sharp)''=(V_0^\sharp-\rho_s)\psi_1^\sharp.
                                                               \tag{26}
$$

再缩小 (24) 的 $\varepsilon$，使 $V_0^\sharp-\rho_s>0$。由左正规渐近，$\psi_1^\sharp$ 和其导数在左端为正并趋于零；方程 (26) 遂给全线 $\psi_1^\sharp>0$、$(\psi_1^\sharp)'>0$。在控制支撑外，

$$
r=(\mathcal P^\sharp)^{-1/2}\psi_1^\sharp
=e^{\eta_\varepsilon X}\psi_1^\sharp,
$$

故 $r_X>0$；在有限控制区上，$\zeta\to0$ 于 $C^1$，也保持 $r_X>0$。定义

$$
\boxed{r=(\mathcal P^\sharp)^{-1/2}\psi_1^\sharp,
\qquad w(r(X))=\lambda\mathcal P^\sharp r_X,\quad\lambda>0.}
                                                               \tag{27}
$$

左、右正规渐近给 $r(-\infty)=0$、$r(+\infty)=\infty$；故 (27) 是真实严格单调径向变换，并给 $w>0$。

直接微分 (26) 得

$$
w_r=-\lambda\mathcal P^\sharp\rho_s r/r_X,
\qquad
L_j\bigl((\mathcal P^\sharp)^{-1/2}\psi\bigr)
=-\frac{\lambda\sqrt{\mathcal P^\sharp}}{r_X}H_j^\sharp\psi,
                                                               \tag{28}
$$

其中 $L_j=(w\partial_r)'-j^2w_r/r$。因此 (25) 不是任意势的抽象结论：它产生同一个真实 $w$ 的第二、第三角模核及其余整数模逆。还准确有

$$
\sqrt{-\frac{w_r}{rw}}\,dr=\sqrt{\rho_s}\,dX
\quad\text{于负区},                                  \tag{29}
$$

所以新的恢复控制没有改变 (7)、(9)。

### 5.1 留下真正紧支撑的两个 profile 控制

为了在有限截段接尾后恢复两条核，需要再次使用 R633 的四 bump 方法。这里的背景已经含有限 $\zeta_{\tau(\varepsilon)}$，但可以在比它更左的一个固定正区区间选新的四个 bump。那里背景正是常系数密度 $e^{-2\eta_\varepsilon X}$。

四个响应权仍为

$$
D^*(\psi_2^2),\quad D^*(\psi_3^2),\quad
D^*((\psi_1^\sharp)^2),\quad D^*(\psi_1^\sharp\phi_1),
\qquad D^*=\partial_X^2+2\eta_\varepsilon\partial_X,
$$

其中 $\phi_1=\psi_1^\sharp\int_X^{X_0}(\psi_1^\sharp)^{-2}$。左端渐近的指数分别为

$$
e^{-4st},\quad e^{-6st},\quad e^{-2st},\quad t^{-1}.
$$

最后一项的首系数为 $(1+2\eta_\varepsilon)/(2s)$，非零；前三项首系数也非零。这四个函数线性独立。按 R633 §2 的点值矩阵与窄 bump 积分论证，可以选四个有限支持使其响应矩阵满秩。

用两行固定 $\psi_1^\sharp$ 在支持右侧的值和导数，再用另外两行作第二、第三谱参数，得到一个真正的两参数族 $w_\mu$：它在一个固定物理半径紧区间外与 $w$ 完全一致，所有负组件的 profile 与行程角均固定，且

$$
\left(\int f_jL'_{j,w}[\partial_{\mu_i}w_\mu]f_j\,dr\right)_{j=2,3;i=1,2}
$$

可逆。把参数邻域再缩小，使对应势差的 $L^\infty$ 范数小于 $\gamma/4$，则 $j\ge4$ 的统一隙也保留。这里紧支撑是实际物理 $r$ 中的紧支撑，不只是 $X$ 坐标中写了一个紧支撑势。

## 6. 真正两端全平的共同零角阶参考逆

把上节中心替换到 R633 的有限截段、正 cone head、固定选定 Hu 平尾构造中。这里只说明相对 R633 必须更改和实际得到的输入。

1. 所有负组件的角界现在都是 $c_m/j$：中心用 (9)，平尾用 R633 §3 的二次无理角。反射空间包含所有余弦整数模，不加 half-turn。
2. 中心的 $B_0$ 从 $Cj^2$ 改成固定的 $C\gamma^{-1}$。正 buffer 的压缩小量因此为 $C\gamma^{-1}m^2e^{-S}$；用一次有限的左右截点和有限 head 长度即可共同支付。中心不会再把 $j^2$ 加到直接 Green 块上。
3. 平尾选择、末端 Robin 相位、两端点指数的同一个自然实现、有限界面矩阵和 tail Schur 求和仍使用 R633 已证明的全部整数版本。它们本来就没有角阶损失。
4. 第二、第三模的有限频率 $C^1$ 收敛及上节真实紧支撑双控制，恢复准确双核。恢复参数可以取得任意小，使 $j\ge4$ 的共同隙/压缩逆不被破坏。

于是存在一个有限 $0<a<b$ 和真正 $C^\infty$ 正 profile $w_*$，两端所有 jets 为零，使

$$
\dim\ker L_2=\dim\ker L_3=1,\qquad \ker L_j=0\quad(j\ge4),
$$

并且对 R633 (6) 的同一物理加权范数、每个固定紧区间
$[\gamma_-,\gamma_+]\Subset(0,1)$，存在固定 $M,M',C$，

$$
\boxed{\|\mathcal G_jF\|_{\gamma,-M'}
\le C\|F\|_{\gamma,M}\quad(j\ge2).}                    \tag{30}
$$

第二、第三模分别含一条有限维对称 row/column。所有常数可以依赖已固定的 $s,L,\varepsilon$ 和所选有限连接几何；它们不依赖角频率。径向一、二阶恢复仍是 R633 (8)，不是额外声称椭圆二阶增益。

零模及第一余弦模用 R629 §4 的自由内帽显式逆：源满足两个固定矩，内帽允许高度常数和 $\beta r\cos\theta$。若要在任意源的体源空间上作比较，可再加入两个固定紧支撑源列 $B_0,B_1$，其标量分别去掉这两个源矩；它们由准确非线性曲率矩在求解后消除。反射使第一正弦矩自动为零。该有限维增广不改变 (30) 的角阶。

因此，把参考逆用于 Hu §13 的两指数 block 求和时，所得共同源空间上的参考增广逆具有同角阶界；$\delta V\mathcal G_*$ 的比较才具有作小范数估计的基础。是否已支付状态相关类型校正、真实倾斜尾坐标与非线性三矩校正，仍须另外证明，不能从 (30) 省略。

## 7. 与非零端口兼容

这一节使用 R637 的严格参考输入

$$
\beta_{\mathrm{ref}}(\sqrt5)>1/3
$$

及 R635 的准确边界消去。这个严格输入已由实际 run 46123270834 支付；不用此前普通 50 位探索替代它。

对 $s$ 在 $\sqrt5$ 的固定小邻域，(1)、(5) 和左正规 $j=1$ 径向解光滑依赖 $s$。在 $X=0$ 作

$$
r(0)=w(r(0))=f_2(r(0))=f_3(r(0))=1
$$

的统一归一化后，R637 的端口积分在两端具有同一个可积主导函数：左端为 $e^{-2st}$ 乘固定幂的上界，右端为严格正指数率的衰减；这些严格率在该小闭邻域中保持正。参数的有限阶导数只再增加固定幂或对数。故

$$
s\longmapsto\beta_{\mathrm{ref}}(s)
$$

连续。可以先选第 1.1 节的一个有限 dyadic 有理 $s$，使端口变化小于 $1/48$。

固定此 $s$，再固定第 3 节的有限 $L$。当 $\varepsilon\downarrow0$ 时，恢复控制 $\zeta_{\tau(\varepsilon)}\to0$ 于每个固定 $C^k$ 范数；第二、第三简单核及 $j=1$ 左正规解连续依赖参数。控制区固定有限，区外的 Morse 方程和其渐近指数在紧参数集内一致受控。因此同一主导收敛论证给

$$
\beta_{\mathrm{center}}(s,\varepsilon)
\longrightarrow\beta_{\mathrm{ref}}(s).
$$

在同时满足 (24)、(25) 的条件下，选一次严格正的有限 $\varepsilon$，使第二次端口变化小于 $1/48$。

最后 R637 对真实连接/head/全平尾的绝对积分估计只使用固定 $j=2,3$ 的正区衰减和真实尺度，不要求 $s=\sqrt5$。同样把有限截点、head 长度和双核恢复参数选到第三次端口变化小于 $1/48$。最终同一个全平 profile 满足

$$
\boxed{\beta_*>
\frac13-\frac3{48}=\frac{13}{48}>\frac14,}             \tag{31}
$$

同时保留 (30)、二次无理角界以及真正紧支撑双谱控制。

这些顺序选择全部在构造某一个固定有限背景时完成，不声称 $s$、$L$ 或 $\varepsilon$ 是最终固定度量连续变形族的参数。也不把形式二阶系数 (31) 等同于有限转角、宏观 Hausdorff 位移或 README 完成条件。

## 8. 当前实际新增输入

本稿把新机制的参考数据推进到：同一真实两端全平正 profile、相邻第二/第三核、非零二阶倾斜端口（使用 R637 的严格输入）、全部整数角频率的零角阶参考逆、每个负组件的一阶小除数界，以及两个真实紧支撑谱控制。

仍待完成的非线性输入是：在允许内帽真实倾斜的状态空间中，把类型、特征返回、三矩余核和两个核列放入同一个残差校正逆，并实际解出非零嵌入。有限几何与宏观量化也未由本稿支付。
