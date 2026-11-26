# R571 温和相位振荡尾、全平核与外端 shooting 的换号机制

状态：**已证明的固定输入族与线性外端匹配机制。不是有限等距族；曲率预算仅支付凸底域尾 patch。** 2026-11-26。

R569 的首份实际传递虽成功得到线性种子，但在外端归一后观察到很大的二阶导数。本笔记换一个明确的新输入，先完整支付它的全平核和外端匹配机制；不将背景曲率较小推断为种子 C2 代价较小，更不将线性匹配当作有限返回。

## 1. 新固定输入族与连续局部厚度

固定
$$
r_c=\frac{11}{50},\qquad \ell=\frac15,\qquad A=\frac45,\qquad
\delta=\frac{r-r_c}{\ell},\qquad 0<\delta\le\frac25.
$$
对 $\varphi\in[0,2\pi]$ 定义
$$
w_\varphi(r)=A\exp\left[-\frac{2-\sin(\delta^{-1}+\varphi)}{\delta}\right],
\qquad
h_\varphi(r)=h_c-\int_{r_c}^r w_\varphi(t)\,dt. \tag{1}
$$
在 $r\le r_c$ 令 $w=0,h=h_c$。每个固定相位是一份固定度量
$$
g_\varphi=(1+w_\varphi^2)dr^2+r^2d\theta^2.
$$
$\varphi$ 是设计控制；改变它或把旧 R566 的 $\delta^{-2}$ 相位改成这里的 $\delta^{-1}$ 都是换输入，不是同 g 精化。幅度也由旧 $0.1$ 改为这里的 $0.8$。

第6节的连接区可能有 $a(s)>0.30$；在那里仍用 (1) 的同一个有限公式延伸定义所有 $r>r_c$ 的 $w_\varphi(r)$。这是公式本身的延伸，没有另设 cutoff；本节定量 Hessian 和 graph reach 预算仍只覆盖 $r\le0.30$。

各固定阶导数都是 $w$ 乘有限负幂与有界三角函数，故 $r_c$ 处全平，且这个估计在 $\varphi$ 上一致。令 $u=\delta^{-1}$，
$$
\partial_\delta\log(w/A)
=\frac{2-\sin(u+\varphi)}{\delta^2}
 -\frac{\cos(u+\varphi)}{\delta^3}. \tag{2}
$$
因此
$$
|w_r'|\le\frac A\ell e^{-1/\delta}(3\delta^{-2}+\delta^{-3}).
$$
在 $x=1/\delta\ge5/2$ 上分别取 $x^2e^{-x}$ 与 $x^3e^{-x}$ 的最大值，得到
$$
\|D^2 h_\varphi\|_{\rm op}
 \le K_1:=75e^{-5/2}+108e^{-3}
 =11.533378280521717\ldots. \tag{3}
$$
角 Hessian 项 $|w|/r\le(40/11)e^{-5/2}<K_1$。另外
$$
|h-h_c|\le0.064e^{-5/2}<0.005254.
$$
由 R566 已证明的凸底域 graph 最近点唯一性论证，对整个 $r\le0.30$ 的闭圆盘图像，
$$
\operatorname{reach}(\operatorname{graph}h_\varphi)\ge1/K_1>0.08670.
$$
若实际扰动后的曲面仍是同一凸底域上的图像 $h_\varphi+v$，且已连续验证
$\|D^2v\|_{\rm op}\le4$，同一局部 patch 的 reach 至少
$1/(K_1+4)>0.0643>0.061$。这不包括闭面跨块点对。

$K=w w_r'/(r(1+w^2)^2)$ 无限次变号。零点对应
$$
F(u)=u\cos(u+\varphi)+\sin(u+\varphi)-2=0.
$$
在正余弦周期中心 $F>0$，相邻余弦零点 $F=-1,-3$，故有无限零趋向 $u=\infty$。若同时 $F=F'=0$，则
$\sin(u+\varphi)=4/(u^2+2)$、
$\cos(u+\varphi)=2u/(u^2+2)$，
由平方和得 $u^4=12$。此值小于 $u\ge5/2$，故定义域内所有这些曲率零均简单。

## 2. 同一正权转化

仍求二阶角模
$$
(wf')'-4w'f/r=0,\qquad f=r^4y.
$$
置 $u=\delta^{-1}$、$r(u)=r_c+\ell/u$，得到
$$
(py_u)'+\varepsilon p y=0, \tag{4}
$$
$$
p_\varphi(u)=4u^2r(u)^8e^{-u(2-\sin(u+\varphi))},\qquad
\varepsilon(u)=\frac{0.48}{r(u)^2u^4}. \tag{5}
$$
这里保留实际 $r(u)$，没有常半径近似。

在 $u\ge100$，
$$
(\log p)'=u(\cos(u+\varphi)-\eta_\varphi(u)),
$$
$$
\eta_\varphi(u)=\frac{2-\sin(u+\varphi)}u-\frac2{u^2}
                  +\frac{1.6}{r(u)u^3}.
$$
逐项估计给
$$
0<\eta_\varphi<0.031,\qquad |\eta_\varphi'|<0.011.
$$
所以每个大周期有唯一最大值
$$
\alpha_n(\varphi)\in
(\pi/2+2\pi n-\varphi-0.04,\ \pi/2+2\pi n-\varphi)
$$
及唯一最小值
$$
\gamma_n(\varphi)\in
(3\pi/2+2\pi n-\varphi,\ 3\pi/2+2\pi n-\varphi+0.04).
$$
存在性来自端点符号；唯一性来自零点附近
$-\sin(u+\varphi)-\eta_\varphi'$ 的确定符号，其他位置不可能有零。
对 $n\ge17,\varphi\in[0,2\pi]$，$\alpha_n>100$，相邻最大值间长度在6和7之间，权 $p$ 先降后升。

## 3. 复用已证明的单谷 Dirichlet/Green 引理

R569 第4–5节的引理只要求正权单谷、cell 长小于7，与具体振荡公式无关：

- 零 Dirichlet 的加权 Poincare 常数可取 $C_0=49/2$，不含 contrast；
- 零势插值 $H_L,H_R$ 满足 $0\le GH_i\le C_0H_i$；
- 若 $\varepsilon_{\max}C_0\le1/2$，含势准确插值满足
  $H_i\le H_i^\varepsilon\le2H_i$；
- 记 $R_*=\int_Ip^{-1},K=1/R_*$，准确 DtN 有
  $K\le-D_{LR}\le2K$，
  $D_{ii}\le K-\varepsilon_{\min}\int_IpH_i^2$。

这些是已证明的无共振和 Green domination；没有假设新的未检查 resolvent。

取某 cell 左端 $a=\alpha_n$，令 $C_a=4r_c^8a^2$。在 $a\le u<a+7$，
$$
e^{-21}C_a e^{-a(2-\sin(u+\varphi))}
 \le p(u)\le2C_a e^{-a(2-\sin(u+\varphi))}, \tag{6}
$$
$$
a^{-4}\le\varepsilon(u)\le10a^{-4}. \tag{7}
$$
证明 (6) 时，幂因子之比在1与2之间，而指数中 $u-a<7$、$1\le2-\sin\le3$，故额外损失至多 $e^{-21}$。(7) 用 $0.22<r<0.222$ 即得。

左右各长 $1/2$ 的端窗满足 $\sin(u+\varphi)\ge3/4$，长1的谷窗满足 $\sin(u+\varphi)\le-3/4$。与 R569 相同的积分估计给
$$
R_*\ge\frac1{2C_a}e^{11a/4},\quad K\le2C_a e^{-11a/4},
$$
$$
\int pH_L^2,\ \int pH_R^2
 \ge\frac{e^{-21}C_a}{16}e^{-5a/4}. \tag{8}
$$
端窗中对应 $H_i\ge1/2$：其电阻占比至多
$e^{21}e^{-3a/2}<1/2$。又 $\varepsilon_{\max}C_0\le245a^{-4}<1/2$，所以
$$
D_{LL},D_{RR}
 \le-\frac{e^{-21}C_a}{32a^4}e^{-5a/4}<0. \tag{9}
$$

## 4. 真实非零全平核、唯一性和相位连续性

设 $k_n=-D_{n,LR}>0$、
$V_n=-(D_{n-1,RR}+D_{n,LL})>0$。
前一个 cell 左端与当前相差小于7，由 (8)–(9) 得保守统一界
$$
\frac{k_{n-1}}{V_n},\frac{k_n}{V_n}
 \le \mathcal R(a):=512e^{42}a^4e^{-3a/2}<1/64,\qquad a\ge100. \tag{10}
$$
例如前一耦合的直接系数是 $128e^{21+77/4}$，小于 (10) 的系数。
$a^4e^{-3a/2}$ 在 $a\ge100$ 递减；于100处可用
$512\cdot10^8e^{-108}<512\cdot10^8 2^{-108}<1/64$
直接核查。

准确通量匹配仍是
$$
k_{n-1}y_{n-1}+V_ny_n+k_ny_{n+1}=0.
$$
令 $y_n=(-1)^{n-17}x_n$，$x_{17}=1$，则
$$
\rho_n=x_n/x_{n-1}
 =\frac{k_{n-1}}{V_n-k_n\rho_{n+1}}.
$$
R569 的同一证明给区间 $[0,1/32]$ 上的映入和 Lipschitz 常数 $<10^{-3}$。
从有限 $\rho_{M+1}=0$ 反推再取极限，得到真实正比值和逐 cell 准确 ODE 解，所有通量及高阶导数均匹配。准确 DtN 的截断界为
$$
|\rho_n-\rho_n^{(M)}|\le\frac1{32}10^{-3(M-n+1)}. \tag{11}
$$

由 $\rho_n\le1024e^{42}\alpha_n^4e^{-3\alpha_n/2}$，充分大时
$\rho_n\le e^{-\alpha_n}$。cell 长小于7，故
$|y_n|\le C e^{-\alpha_n^2/14}$。系数及其固定阶导数仅按 $u$ 的幂增长，逐 cell Gronwall 至多损失 $e^{C_k u}$，于是对任意固定 $k$，
$$
|d^k f/dr^k|\le C_k e^{-c_k/\delta^2}\longrightarrow0. \tag{12}
$$
因此 $f$ 向平帽零延拓为 C-infinity，非零，因为归一 $y(\alpha_{17})=1$。
它亦可沿普通 ODE 唯一延伸到整个 $r_c<r\le0.30$。

全平解空间准确是一维。若 $f_1,f_2$ 都全平，则
$$
w(f_1f_2'-f_1'f_2)
$$
恒定，而在 $r_c$ 极限为0，故 Wronskian 为0，二者线性相关。

有限 cell ODE、端点根和 DtN 均连续依赖 $\varphi$；(10)–(11) 一致，故归一种子随 $\varphi$ 连续。全平估计也可在紧相位区间一致选取，因此端点零延拓保持所需的 C2 连续依赖。

仍令
$$
A_V=w(4f-rf_r)/3,\qquad
V=A_V\cos2\theta\,e_r-\frac{A_V}2\sin2\theta\,e_\theta
  +f\cos2\theta\,e_z.
$$
R569 的直接三项度量核验完全适用，所以这是准确非零全平无穷小等距场。当前数值逆设计的 $e^{-\kappa/\delta}$ 型自由包络不会渐近排除它，因为 (12) 除以该包络仍全平。

## 5. 相位绕一圈时，归一种子反号

$\varphi=0$ 与 $2\pi$ 给完全相同的 w 和线性 ODE，但
$$
\alpha_{17}(2\pi)=\alpha_{16}(0).
$$
$\alpha_{16}(0)>100$，所以同一对角占优证明也适用于这一个前邻 cell。真实稳定模在相邻最大值间反号。对 $\varphi=0$ 的归一种子，

更直接地，$y_{17}=1,y_{18}=-\rho_{18}$，在第17个结点的准确通量式给
$$
k_{16}y_{16}=-(V_{17}-k_{17}\rho_{18})<0,
$$
其中 $k_{17}/V_{17}<1/64$、$0<\rho_{18}<1/32$。故无需更换归一起点便得到
$$
y_0(\alpha_{17}(0))=1,\qquad y_0(\alpha_{16}(0))<0.
$$
一维唯一性因此给
$$
f_{2\pi}
 =\frac{f_0}{y_0(\alpha_{16}(0))},
$$
即首尾是同一真实解的**负倍数**。这里不是从网格符号推断；负号由正 Riccati 比值和准确接口匹配证明。

## 6. 一个真实外端 shooting 条件必有零

给定随 $\varphi$ 连续、$2\pi$ 周期的一族旋转连接面
$$
X_\varphi(s,\theta)=a_\varphi(s)e_r+z_\varphi(s)e_z,
$$
其内端与 $r=0.30$ 的尾在开邻域准确重合，外端是同半径 R 的开柱，并在连接区满足 $a>0,z'>0$。二阶角模的径向和竖直分量 $(A,C)$ 沿此区满足
$$
aA'=-3a'A-4z'C,\qquad a'A'+z'C'=0. \tag{13}
$$
这是连续参数的正则二维 ODE，因而从尾口到核心的传递线性且连续。在开柱上 $C'=0,A'=-4C/a$；轴向恒定的椭圆核心变化要求
$$
\Psi(\varphi):=C_{\rm core}(\varphi)=0. \tag{14}
$$
由于连接面首尾相位完全相同，而种子乘一个负数，
$\Psi(2\pi)$ 与 $\Psi(0)$ 反号，或二者已经为0。中值定理给某个固定
$\varphi_*\in[0,2\pi]$ 满足 (14)。此时 $A_{\rm core}\ne0$，否则 (13) 的唯一性使种子恒零。

上述连续周期连接族确实可以构造，不是额外的存在性假设：取固定平滑非增半径 a(s)，开柱处 a=R，尾口开邻域 a(s)=r_0+(s_0-s)，$r_0=0.30$。令 q(s)=-a'(s)，选 q 从核心的0变到尾口的1，且积分为 $R-r_0$。取光滑 cutoff $\chi$，在开柱为1、在尾口为0，并使 $\chi=0$ 的区域 q>0。固定 c>0，置
$$
z_\varphi'(s)=c\chi(s)+(1-\chi(s))q(s)w_\varphi(a(s)). \tag{15}
$$
它处处正、在核心等于c，在尾口等于w；积分只决定一个相位相关的帽高。所有参数依赖周期连续，且整个开尾口的 jets 准确一致。可选择 C-infinity 的 q、chi，故没有有限 jet 拼接缺口。

因此 (14) 是已付存在性的真实线性射击零。将正半部经开柱镜射，可得到闭旋转球面上的非零光滑无穷小场，两个开平帽均固定，核心给轴向恒定二阶角模。此闭面陈述没有给出所需全局定量 reach 或有限幅度。

在 R=0.38 的圆核起点，固定 ellipse q=0.18、offset=0.2，p=0.18+epsilon 的非径向一阶要求
$A_{\rm core}=\epsilon/2,C_{\rm core}=0$；达到 (14) 后可归一到该值。均值半径变化 $\epsilon/2$ 属于旋转度量的设计变化。

## 7. 已付和下一实际非线性接口

已付的是：相位族中每个固定输入的全平振荡与局部图 reach 预算、真实一维全平线性核、连续参数依赖、以及某个相位能支付核心的线性 shooting。后续实际运行应报告新种子的 outer jets、数值传递误差、C2 峰和实际 $\varphi_*$，而非凭较小背景 Hessian 宣称条件数已好。

在固定选定的相位与径向函数后，单位 T 的有限尾方程仍是
$$
X=r\Pi_\theta T+Z(r)e_z,\quad
X_r\cdot T=0,\quad |X_r|^2=1+w_{\varphi_*}^2.
$$
线性种子给 $\delta u=3A_V/(2r)\sin2\theta,\ \delta v=-2f/r\sin2\theta$，但它没有解掉二阶及以后。单调中段上的错误外端符号也不能靠这条纸证忽略，必须实际求出 (14) 的零。

全频率非线性逆、有限幅度分支、固定 g 精化、闭面全相位 reach 和 .3D 握持门仍未支付。相位控制族不是课题要求的固定 g 弯曲族；只有选定一张非轴对称的旋转度量嵌入后，其材料相位动作才有后续固定 g 含义。本文不是完成。

