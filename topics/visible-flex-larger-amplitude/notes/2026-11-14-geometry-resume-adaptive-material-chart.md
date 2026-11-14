# 完整核心到物理尾角图：精确链式法则与实际投影费用

作者：ChatGPT（GPT-6 Astra Pro，geometry_design）；2026-11-14 UTC。

**可信度。** 下文角图、度量和边界维数的恒等式已证明。后面的数字是对已接受 M96 开放前缀末点的实际坐标转换和 Fourier 投影，属于数值证据；没有在这些虚拟转角位置延伸曲面，也没有求解新的全尾 BVP。

## 1. 一张在完整尾切口回到材料角的明确图

设完整核心支撑函数为

$$
h(\psi)=1+\sum_{m=1}^{M}c_m\cos(2m\psi),\qquad
\rho_0(\psi)=1+\sum_{m=1}^{M}(1-4m^2)c_m\cos(2m\psi)>0.
$$

记

$$
Q(\psi)=\sum_{m=1}^{M}\frac{(1-4m^2)c_m}{2m}\sin(2m\psi),
\qquad \Theta(s,\psi)=\psi+b(s)Q(\psi).
$$

给定实际物理区间 $[s_0,s_1]$，令 $u=(s-s_0)/(s_1-s_0)$，在区间内取

$$
b=1-10u^3+15u^4-6u^5;
$$

在左、右两侧分别延长为常数 $1,0$。由于
$b_u=-30u^2(1-u)^2\le0$，有 $0\le b\le1$，且两端 $b_s=b_{ss}=0$。因此

$$
\Theta_\psi=(1-b)+b\rho_0>0.
$$

同时 $\Theta(s,\psi+2\pi)=\Theta(s,\psi)+2\pi$，故每条纬线上的材料角图是全局保向微分同胚。左端保留完整核心弧长角，右端满足 $\Theta=\psi$，并在 $s$ 方向连同一、二阶 jet 回到恒等图。这一性质使用全部 $M$ 个核心系数。

若材料坐标下的曲面为 $F(s,\theta)$，令
$\widetilde F(s,\psi)=F(s,\Theta(s,\psi))$，则

$$
\widetilde F_s=F_s+\Theta_s F_\theta,
\qquad \widetilde F_\psi=\Theta_\psi F_\theta.
$$

所以原 $ds^2+a(s)^2d\theta^2$ 在此图中的三个系数是

$$
\widetilde E=1+a^2\Theta_s^2,\quad
\widetilde F=a^2\Theta_s\Theta_\psi,\quad
\widetilde G=a^2\Theta_\psi^2.
$$

若 $V$ 是物理材料方向的 Frenet 速度，实际坐标 ODE 必须为

$$
\partial_s\widetilde F=V+v\widetilde F_\psi,
\qquad v=\Theta_s/\Theta_\psi.
$$

这条切向传输项由链式法则唯一确定。改变 $b$ 是同一物理度量的坐标选择；后续数值加密应保存所选的具体图，另外记录任何图的变化。

## 2. 旧有限场的完整二 jet 转换

已接受旧场使用 $\theta=\phi+Q(\phi)$。令 $\phi=\eta(s,\psi)$ 解
$\eta+Q(\eta)=\Theta(s,\psi)$。写 $r=\rho_0(\eta)$，$r'=\rho_0'(\eta)$，则

$$
\eta_\psi=\Theta_\psi/r,\quad \eta_s=\Theta_s/r,
$$

$$
\eta_{\psi\psi}=(\Theta_{\psi\psi}-r'\eta_\psi^2)/r,
\quad \eta_{s\psi}=(\Theta_{s\psi}-r'\eta_s\eta_\psi)/r,
\quad \eta_{ss}=(\Theta_{ss}-r'\eta_s^2)/r.
$$

例如

$$
\widetilde F_{ss}=F_{ss}+2F_{s\phi}\eta_s+F_{\phi\phi}\eta_s^2+F_\phi\eta_{ss}.
$$

另外两项由同样的链式法则给出。源码先转换所有 Cartesian 向量，再把平面分量旋转到新 $\psi$ 的极基；没有把极基系数直接当作固定 Cartesian 分量。

## 3. 实际代价：位置很小不等于二 jet 投影很小

输入为已接受的 $s=0.984$、M96 完整前缀，SHA
`3ac8c8efa20670342021487a197443f6e1b2ad60f35c7bf2864f355a06424b69`。
完整核心和已冻结二阶节点 jet 均保留。此次探针取明确的过渡区间
$[0.984,2.32948]$，但所有行都转换同一个 $s=0.984$ 端点 jet；第二个数只是探针图的参数，没有在该位置得到曲面。

8192 个统一角点上的结果如下。表内误差是相对于未截谱链式转换结果的向量最大值。

| 图中位置 | 重投影模数 | 位置误差 | 角二阶 jet 误差 | 重构材料度量误差 |
|---|---:|---:|---:|---:|
| $u=1/2$，$b=1/2$ | 96 | $2.1067\times10^{-8}$ | $7.6235\times10^{-3}$ | $3.9199\times10^{-8}$ |
| 同上 | 192 | $2.1042\times10^{-8}$ | $7.7463\times10^{-3}$ | $3.9084\times10^{-7}$ |
| 同上 | 384 | $6.7410\times10^{-13}$ | $4.1284\times10^{-7}$ | $6.7190\times10^{-8}$ |
| 同上 | 768 | $2.2087\times10^{-14}$ | $1.0734\times10^{-8}$ | $6.6942\times10^{-8}$ |
| $u=1$，$b=0$ | 96 | $2.1436\times10^{-8}$ | $2.2469\times10^{-2}$ | $5.4914\times10^{-8}$ |
| 同上 | 192 | $2.2040\times10^{-8}$ | $2.2414\times10^{-2}$ | $2.1549\times10^{-7}$ |
| 同上 | 384 | $2.0885\times10^{-8}$ | $2.2580\times10^{-2}$ | $6.2317\times10^{-7}$ |
| 同上 | 768 | $3.0990\times10^{-14}$ | $8.2373\times10^{-8}$ | $6.6517\times10^{-8}$ |

未截谱转换的材料度量误差仍约 $6.65\times10^{-8}$。原核心最小密度约 $0.166$，材料角逆映射能够拉伸已有角频率。此实验说明：直接把旧端态转成材料角再保留 96 个模，不能继承旧场的二 jet。新的 M96 自适应图全局 BVP 需要重新解全部前缀；上面的投影只能作带有已测误差的初猜。

## 4. 真正 96 条物理尾条件的增广维数

为了让边界保持纯左端、纯右端，可把完整核心系数 $c\in\mathbb R^M$ 与三个实际 scalar-profile 控制 $p\in\mathbb R^3$ 增广为常数状态 $c_s=p_s=0$。物理 Fourier 状态有 $3M+2$ 项，因此总数为 $4M+5$。

左端分别施加：支撑常数项为 1（一条）、$T_m+2mR_m=0$（$M$ 条）、全部 $M+1$ 个高度系数为零、$c_m-R_m=0$（$M$ 条）、三个固定低核心系数。总共 $3M+5$ 条。右端完整物理尾 D-N 提供 $M$ 条非均值斜率条件。M96 时是 389 个状态、293 条左条件、96 条右条件，左边界零空间维数 96。

若控制改变物理切口长度 $L(p)$，应另用固定计算区间 $x\in[0,1]$、$s=L(p)x$，并把所有 ODE 右端乘 $L(p)$；不能把不同切口长度直接放在同一个固定物理终点上。当前本文件只给出结构和实际角图算子，没有声称已实现完整三控制全尾求解。

在真正切口 $b=b_s=b_{ss}=0$ 时，若原尾反射符号为 $\sigma\in\{-1,1\}$，尾的全部物理高度系数可直接取

$$
H_m=\sigma Z_m,\qquad m=1,\ldots,M.
$$

这里的余弦归一化为 $Z=Z_0+\sum Z_m\cos(2m\theta)$。原尾 $r_s=\sigma/\sqrt E$，所以非均值条件为
$Z_{m,s}=\operatorname{DN}(H)_m/\sqrt E$。均值、一阶和二阶 Cartesian 接合还需实际消费完整新尾，不能由维数配平或这一条斜率条件代替。

## 复现

源码 `computations/geometry_20261114_adaptive_material_chart.py`，完整读出
`notes/2026-11-14-geometry-resume-adaptive-material-chart-r2.json`。
实际命令的核心参数为
`--angular 8192 --modes 96 192 384 768 --fractions .5 1`，输入与二阶 jet 的哈希已写入读出。

本次没有新闭面、全族 reach 或全闭直径结论。
