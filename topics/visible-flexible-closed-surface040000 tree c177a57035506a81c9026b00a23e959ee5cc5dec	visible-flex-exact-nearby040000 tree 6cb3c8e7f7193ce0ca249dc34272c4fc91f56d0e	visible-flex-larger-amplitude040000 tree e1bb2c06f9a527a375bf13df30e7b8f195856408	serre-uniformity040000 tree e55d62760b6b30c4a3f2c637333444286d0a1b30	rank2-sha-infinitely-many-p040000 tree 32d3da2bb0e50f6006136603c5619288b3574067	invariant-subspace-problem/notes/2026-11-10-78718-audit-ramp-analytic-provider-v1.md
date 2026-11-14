# 退化 ramp 的真正角解析 Cauchy provider：完整独立审查

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
可信度：**完整数学审查通过；有限符号/有理证书由审者真实重跑。**
审者没有参与原稿推导、参数选取或证明构造，也未参与主 M14 候选优化。本审不运行曲面 PDE、BVP 或其它新候选。

## 1. 对象、范围与最终意见

全文对象为 [geometry-ramp-analytic-provider-v1.md](2026-11-10-78718-geometry-ramp-analytic-provider-v1.md)，17,946 B，SHA256
`bb727afa2bc5ba13d1005df5d806757f69332d35c6ea172cfb7ac781a19d2402`。
本审覆盖原稿 §§0–9：精确 Gauss–Codazzi 变换、标量复特征、正系数和真实 Picard 差分收敛、解析类唯一性、实保号和复无零带、真实位置/标架闭角、仅 $a\in C^2$ 下的联合 $C^2$ 浸入、真实两侧二 jet 接合、输入族连续依赖、固定二进参数的系数界及未解边界。

配套冻结程序 [78718-geometry-ramp-provider-check.py](../scripts/78718-geometry-ramp-provider-check.py)，4,330 B，SHA256
`1700548362dafb80d23c38882bf5a92cd1b24008bf0284532de5e983ac72d638`，已全文读完并实际运行。有限代数通过不能替代收敛证明，下面独立补出全部环节。

**原稿所声明的局部 provider 命题通过，无实质订正项。** 给定真实周期位置与标架、角解析且有统一复带界的非特征输入 $b_0,p_0$，在明确正宽度上确有同一 $g=ds^2+a(s)^2du^2$ 的真正周期 $C^2$ 浸入。允许 $a''$ 为零、变号或在接口二次退化，不需径向解析，不需 $a'''$、$Q'$ 或 $L_s$。

这不是无条件闭面存在命题。实际 M14 入口的复带/范数、整个物理 ramp 的连续控制、指定远端数据、全域嵌入/reach、固定 $H$、幅度、源传输及无限尾均尚未支付。本审仅在原稿范围内通过，不扩大假设到题设全体 $C^2$ 候选，也不从解析类唯一性推出一般低正则刚性。

## 2. Gauss–Codazzi 变换：逐项核算

对 $g=ds^2+a^2du^2$，非零 Christoffel 符号为

$$
\Gamma^s_{uu}=-aa',\qquad
\Gamma^u_{su}=\Gamma^u_{us}=\mu=\frac{a'}a.
$$

取 $\mathrm{II}=Lds^2+2Mds\,du+Cdu^2$，$Q=aa''$。Gauss 与两个 Codazzi 条件分别是

$$
LC-M^2=-Q,\qquad M_s=L_u-\mu M,\qquad
C_s=M_u+\mu C+aa'L.
\tag{A1}
$$

例如 $\nabla_sh_{uu}=C_s-2\mu C$、$\nabla_uh_{su}=M_u-\mu C+aa'L$；另一个由 $\nabla_sh_{us}=M_s-\mu M$ 与 $\nabla_uh_{ss}=L_u-2\mu M$ 得到。符号与原稿一致。

在 $C\ne0$ 区域令 $b=aM/C$、$p=a/C$，反解为

$$
C=\frac ap,\quad M=\frac bp,\quad
L=\frac{b^2-Qp^2}{ap}.
\tag{A2}
$$

Gauss 方程即成恒等式。由第二 Codazzi 消去 $C_s$，精确得到

$$
-ap_s=pb_u-bp_u+a'p(b^2-Qp^2),
$$

即 $p_s=(bp_u-pb_u)/a-\mu p(b^2-Qp^2)$。第一 Codazzi 乘 $p$ 后为

$$
b_s-\frac{bp_s}{p}
=\frac1a\left(2bb_u-\frac{b^2}{p}p_u-Qpp_u\right)-\mu b.
$$

代入前式，$b^2p_u/(ap)$ 消去，得到

$$
b_s=\frac{bb_u-Qpp_u}{a}-\mu b(1+b^2-Qp^2).
\tag{A3}
$$

全部反向步骤只要求 $a,p\ne0$。解出系统且保持 $p\ne0$ 就得完整 (A1)，不是只得必要投影。演化系统自身是 $(b,p,b_u,p_u)$ 的多项式，仅有连续时间系数 $a^{-1},Q,\mu$，没有 $Q^{-1}$、$\sqrt Q$ 或 $Q'/Q$，不需跨曲率零点另选平方根支。

## 3. 标量主控的有效复存在

采用原稿的 $A,Q_*,\mu_*$、$R_0\ge1$ 和 $\rho>0$，置

$$
R=4R_0,\quad K=A\max(2,1+Q_*),\quad K_3=\mu_*(1+Q_*),
\quad\Lambda=\mu_*+3K_3R^2.
$$

取 $0<h\le\min(H,\rho/(8KR),1/(2\Lambda))$，零 $\Lambda$ 按无穷解释。常数有限，所以确有正 $h$。标量主控为

$$
w_s=Kww_z+\mu_*w+K_3w^3,
\qquad w(0,z)=\frac{R_0}{1-z/\rho}.
\tag{A4}
$$

复特征 $y_s=\mu_*y+K_3y^3$、$Z_s=-Ky$ 的初值为 $y_0=R_0/(1-z_0/\rho)$、$Z(0)=z_0$。在 $|z_0|\le\rho/2$ 有 $|y_0|\le R/2$、$|y_{0,z_0}|\le R/\rho$。

可直接给有限维 ODE 的完整复支，以独立排除延拓中的隐藏问题。若 $\mu_*=0$，则 $K_3=0$、$y=y_0$；否则令 $\alpha=(1+Q_*)R^2>0$，则

$$
y(s,z_0)=\frac{y_0e^{\mu_*s}}
{\sqrt{1-(1+Q_*)y_0^2(e^{2\mu_*s}-1)}}.
\tag{A5}
$$

平方根从 $s=0$ 的值 1 延伸。由 $2\mu_*h\le1/(1+3\alpha)<1$ 及 $e^t-1\le t/(1-t)$，

$$
\left|(1+Q_*)y_0^2(e^{2\mu_*s}-1)\right|
\le\frac\alpha4\frac{2\mu_*h}{1-2\mu_*h}
\le\frac1{12}<1.
$$

分母平方始终处于以 1 为中心、半径 $1/12$ 的盘内，故存在唯一与初值匹配的全纯平方根。公式 (A5) 在所需闭时间盘和初角盘的邻域给联合全纯解，不用无穷维存在定理。

沿复时间径向线 bootstrap：此前若 $|y|\le R$，则

$$
|y(s)|\le\frac R2e^{(\mu_*+K_3R^2)|s|}
\le\frac R2e^{1/2}<R.
$$

故全段不可能首次达到 $R$。变分 ODE 系数为 $\mu_*+3K_3y^2$，得到

$$
|y_{z_0}|\le\frac R\rho e^{\Lambda|s|}
\le\frac R\rho e^{1/2}<\frac{2R}\rho.
$$

积分给

$$
|Z-z_0|\le KRh\le\rho/8,
\qquad |Z_{z_0}-1|\le2KRh/\rho\le1/4.
\tag{A6}
$$

对 $|z|\le\rho/4$，在 $|z_0|=\rho/2$ 上有
$|(Z-z)-z_0|\le3\rho/8<\rho/2$。Rouché 给恰一个根，导数界保证简单。局部全纯逆在交叠处由根唯一性一致，故得到全盘联合全纯逆支。令 $w(s,z)=y(s,Z^{-1}(s,z))$ 即得真正 (A4) 解及 $|w|\le R$。

即使 $h$ 某项取等号，Rouché 和 ODE 估计仍有严格余量，故在闭时间端点也有全纯邻域。这里没有把 Taylor 值偷偷用到收敛半径之外。

## 4. 正系数双级数与标量迭代

将已有的全纯解展为 $w=\sum c_{jm}s^jz^m$。初始 $c_{0m}=R_0\rho^{-m}>0$。得到 $c_{j+1,m}$ 的递推只用时间阶数不超过 $j$ 的已知系数、角微分的正整数因子、乘法、加法和非负 $K,\mu_*,K_3$，再除以 $j+1$，所以所有 $c_{jm}\ge0$。

这是对真正全纯解的 Taylor 系数作归纳，不以形式递推代替存在，也不要求原 $b,p$ 径向解析。原 $a^{-1},Q,\mu$ 只连续，后面仅在实时间积分中使用它们的绝对值界。

记 $G=Kww_z+\mu_*w+K_3w^3$。标量 Picard 从 $w^{[0]}=w_0$ 开始，$w^{[n+1]}=w_0+\int_0^sG(w^{[n]},w_z^{[n]})$。正系数算子保持系数偏序，故

$$
0\preceq w^{[n]}\preceq w^{[n+1]}\preceq w.
\tag{A7}
$$

相邻差分也有全部非负双系数。每个有限迭代只含有限时间积分和角导数，事先没有无穷维存在问题。

## 5. 向量 Picard 的完整差分归纳

在任一实角中心 $u_*$，对初始解析函数先在半径 $r<\rho$ 的圆盘用 Cauchy，再令 $r\uparrow\rho$，得到每阶角 Taylor 系数界 $R_0\rho^{-m}$，对全部中心一致。

若两个分量由非负角级数 $v$ 主控，则第一行导数项至多 $A(1+Q_*)vv_z$，第二行至多 $2Avv_z$；代数项分别至多 $\mu_*v+\mu_*(1+Q_*)v^3$ 和 $\mu_*(1+Q_*)v^3$。所选 $K$ 同时覆盖两行。

差分不能只套统一较大上界。有限乘积恒等式为

$$
\prod_{j=1}^m x_j-\prod_{j=1}^m y_j
=\sum_{k=1}^m\left(\prod_{j<k}y_j\right)(x_k-y_k)
\left(\prod_{j>k}x_j\right).
\tag{A8}
$$

把当前、前次和相邻差分别用 $w^{[n]}$、$w^{[n-1]}$、$w^{[n]}-w^{[n-1]}$ 的相应角导数主控，(A8) 的非负卷积恰为对应标量单项式的差。用于 $bb_u,pp_u,pb_u,bp_u$ 时给
$w^{[n]}w_z^{[n]}-w^{[n-1]}w_z^{[n-1]}$；用于三次项给 $(w^{[n]})^3-(w^{[n-1]})^3$。角微分只把系数乘正整数，因此不破坏比较。

在每个实积分时刻使用 $|a^{-1}|\le A,|Q|\le Q_*,|\mu|\le\mu_*$，归纳得到

$$
|U^{[n]}|\preceq w^{[n]},\qquad
|U^{[n]}-U^{[n-1]}|\preceq w^{[n]}-w^{[n-1]},
\quad U=(b,p).
\tag{A9}
$$

首步是 $U^{[1]}-U^{[0]}=\int P(s,U_0,U_{0,u})$ 的直接绝对值界。实际角系数随实时间连续，积分中从未对 $Q(s)$ 作时间 Taylor 展开或求导。

## 6. 真实绝对一致收敛和双侧解

取 $r<\rho/4$。非负标量差分在 $0\le s\le h,|z|\le r$ 上被其 $s=h,z=r$ 值控制。因此

$$
\begin{aligned}
&\sum_{n\ge1}\sup_{0\le s\le h,|z|\le r}
\|U^{[n]}(s,u_*+z)-U^{[n-1]}(s,u_*+z)\|_\infty\\
&\le\sum_{n\ge1}(w^{[n]}-w^{[n-1]})(h,r)
\le w(h,r)-w_0(r)<\infty.
\end{aligned}
\tag{A10}
$$

右端与中心无关。每个有限原迭代本来就在整个角带定义且周期，取任意角点的实部为中心即得全角严格子带上的一致收敛；不同中心不会产生不同分支，也没有另欠单值性。

选 $r<r'<\rho/4$，用后一带的一致收敛和 Cauchy 估计，得到前一带上角导数的一致收敛。原多项式右端的时间系数连续，故在紧时间×严格子带上一致收敛。对积分方程过极限得到真正 $C^1_s$ 解，其时间导数就是声明的非线性右端。不是弱解、有限 Fourier 投影或有限 jet。

逐点级数主控给 $|b|,|p|\le R$；中心任意，故整个开带 $|\operatorname{Im}u|<\rho/4$ 的上确界也不超过 $R$。负时间写 $t=-s$，符号改变但绝对主控相同；两侧在零点的函数及由同一原方程给出的时间导数相同，拼成 $C^1_s$ 解。实初值与实系数的 Picard 迭代和共轭交换，故实轴上取实值。

## 7. 解析类唯一性与导数损失

两解 $U,V$ 若在共同角带 $r_c$ 和紧时间段有共同上界 $S$，差 $W$ 满足

$$
W_s=\mathcal A(s,u)W_u+\mathcal B(s,u)W.
$$

取 $r_1<r_c$。主矩阵可用

$$
\mathcal A=\frac1a\begin{pmatrix}b&-Qp\\-p&b\end{pmatrix},
$$

其行和范数不超过 $KS$。剩余系数由主矩阵差乘 $V_u$ 和代数项差给出，前者用 $S/(r_c-r_1)$ 控制。代数 Jacobian 两行和分别不超过
$\mu_*[1+3(1+Q_*)S^2]$ 和 $3\mu_*(1+Q_*)S^2$。因此存在统一有限 $C_A,C_B$，不需时间可微性。

把总带宽损失 $\Delta=r_1-r_*>0$ 分成 $n$ 份，每个算子从上一带到下一带的范数至多 $C_An/\Delta+C_B$。零初值 Duhamel 迭代的时间有序单纯形体积为 $|s|^n/n!$，得到

$$
\|W(s)\|_{r_*}\le2S\frac{|s|^n}{n!}
\left(\frac{C_An}{\Delta}+C_B\right)^n.
$$

组合导数可能落到中间系数，但这已被每一步的带损失算子范数包含，不需另列高阶系数界。由 $n!\ge(n/e)^n$，当 $C_A>0$、$|s|<\Delta/(2eC_A)$ 时右端趋零；$C_A=0$ 时 $(e|s|C_B/n)^n$ 也趋零。先在子带相等，再由解析恒等定理推广到共同带，按固定小时间步重启即覆盖紧时间段。

这个唯一性严格属于共同正解析带和共同有界的经典解类，没有推出一般 $C^2$ 浸入的 Cauchy 唯一性或刚性。

## 8. 实特征保号与复无零带

构造完成后才把第二行写成

$$
p_s-\frac ba p_u=\left(-\frac{b_u}{a}-\mu b^2+\mu Qp^2\right)p.
\tag{A11}
$$

实圆周向量场 $-b/a$ 时间连续、角 $C^1$，紧致性保证整段流存在，并给圆周微分同胚。由 $|b_u|\le4R/\rho$，括号绝对值至多

$$
\Lambda_p=\frac{4AR}\rho+\mu_*(1+Q_*)R^2.
$$

沿实际流解乘法方程，得 $p$ 保持初始符号，且所有实角点都满足
$|p(s,u)|\ge p_*e^{-\Lambda_p|s|}\ge p_{\min}>0$。流的全覆盖性不能省略；它保证这不是仅沿某条特征的结论。多项式存在迭代不含 $p^{-1}$，因此非零性没有被循环预设。

在 $|\operatorname{Im}u|\le\rho/8$，Cauchy 给 $|p_u|\le8R/\rho$。沿实点到复点的竖线积分，在

$$
|y|\le\sigma=\min\left(\frac\rho8,
\frac{\rho p_{\min}}{16R}\right)
$$

有 $|p(s,x+iy)-p(s,x)|\le p_{\min}/2$，从而 $|p|\ge p_{\min}/2$。这是明确正复带宽，足够用 (A2) 构造角解析第二形式；不必最初就要求整个 $\rho$ 带无复零。

## 9. 仅 $a\in C^2$ 时的完整标架兼容

(A2) 给 $L$ 对 $s$ 连续、对 $u$ 解析；$M,C$ 对 $s$ 为 $C^1$，角导数连续。$Q=aa''$ 仅连续足够。

令 $E=(d,T,N)$ 为列矩阵，连接为

$$
\Omega_s=\begin{pmatrix}0&0&-L\\0&0&-M/a\\L&M/a&0\end{pmatrix},
\quad
\Omega_u=\begin{pmatrix}0&-a'&-M\\a'&0&-C/a\\M&C/a&0\end{pmatrix}.
\tag{A12}
$$

$\Omega_s$ 连续且可对 $u$ 微分，$\Omega_u$ 可对 $s$ 微分，不要求 $L_s$。直接计算
$\mathcal R=(\Omega_s)_u-(\Omega_u)_s+\Omega_u\Omega_s-\Omega_s\Omega_u$
的三个独立上三角条目：

$$
\begin{aligned}
\mathcal R_{12}&=a''+(LC-M^2)/a,\\
\mathcal R_{13}&=M_s-L_u+\mu M,\\
\mathcal R_{23}&=(C_s-M_u-\mu C-aa'L)/a.
\end{aligned}
\tag{A13}
$$

它们恰由 Gauss/Codazzi 为零；下三角由斜对称给出，对角为零。全部微分仅为 $L_u,M_s,C_s,a''$，没有 $L_s,Q',a'''$。

以真实周期初始标架解 $E_s=E\Omega_s$。连续系数的线性 ODE 全段存在，斜对称保持正交与定向；参数微分由其积分方程给连续 $E_u$。令 $D=E_u-E\Omega_u$，(A13) 给 $D_s=D\Omega_s$。真实边界标架式给 $D(s_0)=0$，故 $D\equiv0$。

这支付全二维标架兼容，不只写出曲率为零后援引未经检查的低正则全局基本定理。周期初值和系数由径向 ODE 唯一性保证 $E(s,u+2\pi)=E(s,u)$。

## 10. 位置闭角、联合 $C^2$ 与两侧接合

必须给真实周期曲线 $\gamma_0$、真实周期正交标架，并满足原稿 (28)。任意 $b_0,p_0$ 不能暗中支付这些输入。

定义 $F(s,u)=\gamma_0(u)+\int_{s_0}^s d(\tau,u)d\tau$。由
$d_u=a'T+MN=\partial_s(aT)$ 及 $\gamma_{0,u}=a_0T_0$，得

$$
F_s=d,\quad F_u=aT,\quad F_s\times F_u=aN\ne0.
$$

故实际度量严格等于 $ds^2+a^2du^2$。位置本身周期，因为初始位置与被积函数周期；没有仅证明旋转闭合而漏掉平移闭合。二阶导数为

$$
F_{ss}=LN,\quad F_{su}=a'T+MN,\quad F_{uu}=-aa'd+CN.
$$

它们全连续，给联合 $C^2$ 浸入，不需对 $L$ 作径向微分。初始标架作为角 ODE 解确有局部角解析延拓，但不要求额外径向光滑。

另一侧若是同一度量的真实 $C^2$ 浸入，接口位置、定向标架、$M_0,C_0$ 相同且 $C_0\ne0$，则 Gauss 方程迫 $L_0=(M_0^2-Q_0)/C_0$ 相同。上述全部一、二阶位置导数便匹配，得到 $C^2$ 接合。这只支付给定真实另一侧的局部接口，不由形式 jet 列表推断一个尚不存在的另一侧，也不保证远端满足指定数据。

若 $\gamma_0$ 嵌入，边界局部浸入图加远离对角的紧致分离，给可能更窄的实际嵌入条带。这个宽度未量化在 $h$ 中，所以解析存在的整个宽度不能直接宣称嵌入，更不能给 reach 下界。

## 11. 同一度量输入族的连续依赖

固定 $a$ 和共同 $\rho,R_0,p_*$。每个有限 Picard 迭代由多项式、角微分和有限时间积分组成，对初始解析数据在严格子带拓扑下连续；角微分用更宽严格子带的 Cauchy 界。对所有输入，(A10) 的可求和标量尾部相同，故极限在每个严格子带一致连续依赖输入。

再由 Cauchy 与原系统得角导数、时间导数的连续依赖。统一 $p_{\min}$ 控制倒数，故 $L,M,C$ 在所需连续范数下连续。径向线性 ODE 的连续依赖配合上述二阶位置导数及初始曲线 $C^2$ 连续性，给输出浸入的 $C^2$ 连续性。

这只说明若已有统一受控的真实输入族，就有局部共同 $g$ 浸入族；没有构造实际非全等族或固定 $H$ 边值。参数只需连续，证明未额外使用参数可微性。

## 12. fixed flat17 的真实解析目标与系数界

本人直接读取了三个相关原源，不运行探索主函数：

| 原源 | B | SHA256 |
|---|---:|---|
| `950f-prefix-flat-accel-screen.py` | 6004 | `dca3d7fdd5495f4eeeea923522b3001499f48f4b770d262b43e6f88a80b8f6ef` |
| `db6f-prefix-flat-profile.py` | 2008 | `5066cd6d8f94d3b22c0450cc2016df6f90d04efb85d7a13bc833c11868eaaa4b` |
| `db6f-audit-metric-supplier.py` | 17450 | `de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0` |

前者的 `turn_ramp`、`ramp`、`FlatFlow.prefix_profile` 给分段公式；安装器只在 `ramp_law=flat` 时使用它，并加入全部 piece knot。目标供应器的头部、`q()`、`Target.__init__`、`a_prefix_poly` 明确用主参数的 exact binary rationals 定义解析目标，用 Fraction 重算 $T_u,T_d$，以精确有理系数构造分段多项式。不能以 flow 中舍入的 $T_u,T_d$ 或单点浮点求值替代该目标。

归一化 turn 参数低端为 $F'(t)=(3x^2-2x^3)/(1-\eta)$、$x=t/\eta$，中段为 $1/(1-\eta)$，高端反射同理。由 $F(0)=0,F(1)=1$ 得 $0\le w\le1$、$|w_u|\le1/[\varepsilon(1-\eta)]$。精确 $T_v=\delta/[v(1-\varepsilon)]$ 给

$$
1\le a\le1+\delta,\quad |a'|\le\max(v_u,v_d),\quad
|a''|\le\frac{v^2(1-\varepsilon)}{\delta\varepsilon(1-\eta)}.
$$

对固定程序常数本身的二进有理值，有

$$
\frac{399}{1000}<\varepsilon<\frac{401}{1000},\quad
\frac{49}{1000}<\eta<\frac{51}{1000},\quad
0<v_u,v_d<\frac{181}{1000},\quad
\frac9{125}<\delta<\frac3{40}.
$$

这里没有用方便的十进参数替换原度量。于是 $a<43/40$、$|a'|<1/5$，并有

$$
|a''|<\frac{(181/1000)^2(601/1000)}{(9/125)(399/1000)(949/1000)}<\frac34.
$$

所以 $A=1,Q_*=1,\mu_*=1/5,K=2$ 有效。代入 $R=4R_0$ 后，宽度恰为

$$
h\le\min\left(H,\frac\rho{64R_0},\frac5{2(1+96R_0^2)}\right).
$$

端点 $F'$ 的二次主项及反射给 $a''$ 在接平段端二次消失。分段端点匹配及原周期拼接至少保持所需 $C^2$。这些界仅覆盖第一 outward 周期四个 ramp 和相邻平段，不涵盖 bridge 或无限尾。

## 13. 有限程序的覆盖、实际回执和限制

冻结 checker 先核原稿 SHA，再检验 3 个 Gauss/Codazzi 恒等式、9 个标架曲率矩阵条目及 3 个旋转背景恒等式，共 15 项。其 `dr` 虽声明 $Q_s$，实际矩阵只求 $(\Omega_u)_s$ 而不求 $L_s$；§9 的直接矩阵计算说明无需 $Q$ 可微。

程序为代数化简把若干符号声明 nonzero，不构成定理额外假设。数学恒等式实际分母仅含 $a,p$，清分母的多项式恒等式延伸到 $Q=0,b=0$ 等允许值；旋转背景在 $|a'|<1$ 下取正实根支。

12 个 Fraction 检查覆盖固定二进参数的八项外包、加速度、$Q$、$\mu$ 和 Rouché 间隙。它们不求解 Picard 方程，不验证实际 M14 入口复带；无穷维收敛由前面的完整数学论证支付。

本人真实执行：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-geometry-ramp-provider-check.py \
  --out notes/2026-11-10-78718-audit-ramp-provider-check-01.json
```

工具 `dcb411` 自然 exit 0。报告 [audit-ramp-provider-check-01.json](2026-11-10-78718-audit-ramp-provider-check-01.json)，1,408 B，SHA256
`115c7995ac471399fddb712791b242e8b43ba4f282874d3486a4c8a395b75cc3`。
15 符号、12 有理检查全部通过，0 PDE、0 几何候选运行。工具 `75a5ea` 另只读核原稿、checker 和三原源大小/SHA。

此前三条只读源阅读请求曾被基础设施 transport 拒绝，没有进程回执；本人 `213cae` 的只读 `pwd` exit 0 后恢复。此事不构成数学脚本失败，不证明主 solver 状态，也未消费 root 主求解 session。首次保存本审稿时的 `861991` 为本地文本引号语法错误，未写出文件、未执行任何数学检查；本次改用不冲突的字符串界符保存正文，不修改被审源或实际证书。

## 14. 背景与尚待完成的全域任务

$\bar b=0,\bar p=(1-a'^2)^{-1/2}$ 满足系统，因为
$\bar p'=a'a''(1-a'^2)^{-3/2}=\mu Q\bar p^3$，第一行零。它与参考旋转曲面的同一度量相容，但不自动支付任意边界扰动的全段传播。

反复用 $R\mapsto4R,\rho\mapsto\rho/4$ 的最坏界，容许步长可能形成有限和。因此不能以逐点局部存在声称走完整个指定 ramp。当前主图仍需实际入口的 $\rho,R_0,p_*$、真实周期位置/标架及跨全段控制；有限 Fourier RHS、cut jet 或失败 CP 不能代付这些输入。

普通非齐次源、原选定传输/加权 Green、无限尾、远端帽、固定开 $H$、全时嵌入/reach 和幅度都保持为原问题。二次退化接口也没有被偷换成旧简单根传输模型。该稿的准确贡献是：在真实受控角解析输入下，有限阶曲率退化处的齐次非线性 Cauchy 延拓已从形式写法提升为带有效宽度的真正 $C^2$ 解。

**完整独审结论：原稿在其准确范围内通过，冻结正文无须实质修正；应登记为中间解析模块。**
