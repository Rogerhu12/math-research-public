# R119 续篇：共同低锥方向在 κ∈[3/4,1] 的真实负方向

2026-11-14，visible-exact / tail_connector（0df957a82d09）。

**状态：已证明。** 第73—77束的共同低锥方向不能直接扩展成全部缩放频率上的正型。本篇对其完整两态矩阵给出严格反例：在整个实际 $x$ 区间、全部 $\tau\in[0,1/80]$ 和 $\kappa\in[3/4,1]$ 上，其行列式为负；保留实际 $e=1/B>0$ 后仍如此。这个点态计算进一步产生真实径向控制积分的负方向。对第71束的同一个非径向联合背景，在一个新的未占用支集上，整个负窗的完整物理 crossing 也保留负方向，包含 $D\Gamma^*$ 两列和支集外响应。

这否定的是“第73束同一方向可覆盖全尾”的具体推论，不是否定第73—77束已经明确限定的低锥结论。本文不声称构造了整个网络的近核；恰恰因此，不能从低锥局部正型反推所有真实近核都有低频定位。其余 $\kappa$ 必须另行控制。

## 1. 同一方向与原物理单位

仍取实际未占用区间 $I\subset[7/16,15/32]$、中心 $c$，
$$
j\ge8193,\quad J=j+5,\quad\delta=\delta_j,\quad
Q=7+Bf(x),\quad f=30x^2(1-x)^2,\quad
dt=a\,dx,\quad a=\Delta/B,
$$
$$
80<\Delta<3J,\quad e=B^{-1}<2^{-190},\quad
\tau=\Delta^{-1},\quad\kappa=M^2/B.
\tag{O.1}
$$
固定材料坐标、原 fixed-stop 和实际腰尺度。用第73束完整有限 $e$ 的 $F=f+7e$、$\mathcal A_\phi$，原样取
$$
\rho=2^{-1024}J^{-8},\qquad
f_\rho=\rho^7(1-((x-c)/\rho)^2)_+^{14},\qquad
\psi=2^{-720}F^{9/2}\mathcal A_\phi^*
                         [-f_\rho'/\Delta-f_\rho].
\tag{O.2}
$$
因此 $\psi$ 仍是真 $C^9$ compact 方向，$\|\psi^{(l)}\|_\infty\le\rho^{4-l}$、$\|\psi^{(l)}\|_1\le2\rho^{5-l}$，$0\le l\le4$，两个实际 radial phase 准确 annihilate。没有翻转其号数或另造一个方向。

径向自然两态及真实核为
$$
Y=(u,u_x/\Delta),\quad u=\sqrt{\mu_0}h,\quad\mu_0=w/r,
\qquad Y_x=\Delta A_eY,
$$
$$
A_e=\begin{pmatrix}0&1\\
(F+e)^2/4-\kappa F-\tau F'/2&0\end{pmatrix},\qquad
\mathcal K_{\rm rad}=B^2Y^TK_eY,
$$
$$
K_e=\begin{pmatrix}(F+e)^2/4-\kappa F&(F+e-2\kappa)/2\\
(F+e-2\kappa)/2&1\end{pmatrix}.
\tag{O.3}
$$
第73束 (M.7)—(M.8) 定义的 $C_e$ 满足准确积分恒等式
$$
\int\psi\mathcal K_{\rm rad}dt
=2^{-720}B\Delta^3\int f_\rho F^{9/2}Y^TC_eY\,dx.
\tag{O.4}
$$
这是完整 height/total-flux 两态的物理型，不是单独的主符号或其中一条波支。$B\Delta^3=aB^2\Delta^2$ 保留真实材料测度。

## 2. 全 τ、全区间的严格负行列式

先令 $e=0$。使用第73束相同的准确变量
$$
z=x(1-x),\quad v=1-2x,\quad v^2=1-4z,\quad
c_0=450z^6+\tau^2(5-8z),
$$
$$
D=z^3(1-4z)^2c_0^2>0,
\qquad C^{\rm num}=DC_0,
\qquad P^{\rm num}=\det C^{\rm num}/\kappa^2.
\tag{O.5}
$$
完整矩阵由协变微分 $\mathcal DC=\tau C_x+A_0^TC+CA_0$ 重建；每次约化都模去 $v^2-(1-4z)$，实际导数 $v\partial_z-2\partial_v$ 保持这一约束。

在整个矩形
$$
\mathcal R=
[63/256,255/1024]\times[1/16,1/8]
              \times[0,1/80]\times[3/4,1]
\tag{O.6}
$$
上，新的完整 Bernstein 计算得到
$$
\boxed{\quad -P^{\rm num}>2^{-54}.\quad}
\tag{O.7}
$$
多重次数为 $(46,1,14,3)$，全部 **5640** 个有理系数严格正；最小值为
$$
\frac{
346521719707556136935480594011004988009125957469957360895190912162905639583868664967268738221961298071399493426383284280831
}{
4436271510593303775325462694628933925498299320601306520272767328983394092489000996863959049766623324955825937538245714926358652518400000000
},
$$
约为 $7.811102609028828\cdot10^{-17}$。不是角或参数网格采样。矩形甚至允许 $z,v$ 独立，故覆盖实际曲线。

第73束同一个完整分母界 $0<D<2^{-24}$ 随即给
$$
\det C_0/\kappa^2<-2^{-6}.
\tag{O.8}
$$
形式极限 $\tau=0$ 的因子
$F^2(F-4\kappa)^2(F^2-4F\kappa-1)$ 也呈现负号，但 (O.7) 已实际支付全部非零 $\tau$ 项，不以这个极限代替真实参数。

## 3. 实际 e>0 的负号与完整状态

同一两个准确物理解 $h=1$（$M^2=0$）和 $h=e^t$（$M^2=1$）给
$$
\det C_e=\kappa(\kappa-e)P_e(\kappa).
\tag{O.9}
$$
此式是系数全纯的准确多项式除法，不除以 $e$。第73束已证明：在 $|e|\le2^{-24}$、$|\kappa|\le1$，$\|C_e\|<2^{30}$；每个商系数小于 $2^{64}$，商次数至多4。因此在现在所需的**单位** $\kappa$ 盘上应使用 $|P_e|<5\cdot2^{64}<2^{67}$，而不能沿用四分之一盘的 $2^{65}$。

Cauchy 给实际 $e<2^{-190}$ 的
$$
|P_e-P_0|<2^{92}e<2^{-98}.
$$
由 (O.8)，$P_e<-2^{-7}$。当 $3/4\le\kappa\le1$，
$\kappa(\kappa-e)>1/4$，所以
$$
\boxed{\quad \det C_e<-2^{-9},\qquad
\lambda_{\min}(C_e)<-2^{-39}.\quad}
\tag{O.10}
$$
第二式用 $C_e$ 的实对称性与 $\|C_e\|<2^{30}$。负行列式已经保证两个本征值异号；不需要另外假设某个对角元为正。初探中该对角元的 Bernstein 系数并非全正，新的 native 如实保留这个非必要检查的结果。

现在选中心处一个实单位负向量 $Y_c$。第67束完整 phase 商系数的0—5阶界为 $2^{520}$；在本 $|\kappa|\le1$、$|\tau|\le1/80$ 上，第73束实际式的有限乘法微分给
$$
\|(C_e)_x\|<2^{600}.
\tag{O.11}
$$
具体只需 $b_0,b_1$ 至二阶、$(\log F^{9/2})'$ 至三阶以及 $\mathcal D^sK_e$ 至一次 $x$ 导数、$s\le3$。后三组可分别放宽到 $2^{20},2^{30}$；在 (M.8) 的有限乘积中，最大次数 $520+20+30+5=575<600$ 已含两个状态求和。没有对真实 Jacobi 解索取一个未知复径向域。

由 (O.3)，$\|A_e\|<4$。在 $|x-c|\le\rho$，真实基本矩阵 $U$ 满足 $\|U\|<2$、$\|U-I\|<8\Delta\rho$。故
$$
\|U(x,c)^TC_e(x)U(x,c)-C_e(c)\|
<2^{610}J\rho<2^{-400}<2^{-40}.
$$
整个实际解 $Y(x)=U(x,c)Y_c$ 因而满足 $Y^TC_eY<-2^{-40}$。用 $F>1$、$\int f_\rho dx>\rho^8/8$，(O.4) 给
$$
\int\psi\mathcal K_{\rm rad}dt
<-2^{-763}B\Delta^3\rho^8.
\tag{O.12}
$$

按原中心物理波状态
$Z_M=(\sqrt{k_M}u,u_t/\sqrt{k_M})$、$k_M=\sqrt{7M^2-16}$，准确有
$$
Z_M=(\sqrt{k_M}(Y_c)_1, B(Y_c)_2/\sqrt{k_M}),\quad
\|Z_M\|^2\le B^2/M,
$$
因为 $2M<k_M<3M$、$M^2\le B$、$B>3$。所以存在实际非零中心两迹，使
$$
\boxed{\quad
\int\psi\mathcal K_{\rm rad}dt
<-d_-\|Z_M\|^2,\qquad
d_-=2^{-800}\rho^8\Delta^3M/B .\quad}
\tag{O.13}
$$
可取一个 $L^2$ 归一的真实 $\cos M\theta$，并按同一 $Y_c$ 指定两迹。实共轭的 $\pm M$ 同时保留。

每个实际 $B>2^{190}$ 都有这样的四重模。取 $M=4\lfloor\sqrt B/4\rfloor$，则 $M\le\sqrt B$ 且 $M\ge(7/8)\sqrt B$；故 $49/64\le\kappa\le1$，包含于 (O.6)。由原 $B>80/a$，这个 $M$ 还严格处于第69—71束的真实 middle 下限以上。

## 4. 同一非径向联合对象上的完整负窗反例

取第71束已经构造的当前联合 $\Gamma^*(\mathbf a,\Omega)$ 和 $\mathcal X\le2^{-1048576}$。只要求本次所选支集尚未使用；原其余允许参数保持任意当前值。把 (O.13) 的物理中心两迹原样作为实际非径向 Jacobi 解的中心输入。之后的解不作 Fourier 截断，保留全部输出、两个 mean、两个真实根和 normal shear。

此处不用第69—71束正向量的结论；只消费它们对**任意**满足 (O.2) jet/支集条件方向已经证明的误差恒等式及能量估计。记原完整邻胞和
$$
\mathcal N_{i|j}<2^{-20010}2^{-(31867/256)(j-8193)},\qquad
P_j=2^{-42}\delta^{-231/128}.
$$
完整型减 (O.13) 的径向直接积分，共有以下四项。每项除以 $d_-\|Z_M\|^2$ 后的充分界为
$$
\begin{array}{c|c}
\text{实际项}&\text{完整相对上界}\\ \hline
\text{局部实际系数及真解与参考解的差}
 &2^{4100}J^{26}\delta^{-2}\mathcal N_{i|j}\mathcal X\\
\text{整个负窗的固定参数 gauged 响应}
 &2^{12600}J^{42}\delta^{-35}\mathcal N_{i|j}\mathcal X\\
\text{联合两列 }D\Gamma^*\text{ 的直接 metric 项}
 &2^{13600}J^{50}\delta^{-43}\mathcal N_{i|j}\mathcal X\\
\text{全部参数列引起的背景响应}
 &2^{174000}J^{42}\delta^{-35}\mathcal N_{i|j}\mathcal X^2.
\end{array}
\tag{O.14}
$$

这些费用可逐项复算。第69束 (L.16) 用任意 $\rho$ 的实际支集界，给第一项未除 $d_-$ 的 $2^{115}\Delta Bn\rho^5/M$；$n\le4\mathcal N_{i|j}\mathcal X$、$\kappa\ge3/4$ 随即给第一行。其余三行依次使用：第70束完整能量 $2^{7800}J^{16}\delta^{-32}$ 与 $2^{832}\mathcal N_{i|j}\mathcal XP_j\rho^5$；第71束强能量放宽为 $2^{8440}J^{20}\delta^{-34}$ 与 $|D\Gamma_i^*|_1<2^{1130}J^4\delta^{-6}\mathcal N_{i|j}\mathcal XP_j\rho^5$；同篇全部参数背景响应 $2^{161204}\mathcal N_{i|j}\mathcal X^2P_j\rho^5$。

核常数分别用 $2^{24}$ 与 $2^{40}$。共同除法费用只有
$$
\rho^{-3}=2^{3072}J^{24},\qquad
B/M<2\sqrt B<2^5J^{1/2}\delta^{-3/4},\qquad\Delta^{-3}<1.
$$
因此后三行未放宽的 bits 为 $12491,13445,172863$，真实 $\delta$ 逆幂分别为 $35$ 以下、$43$ 以下、$35$ 以下。这里没有丢掉 $\rho^5$，也没有把 $\Gamma^*$ 的全局列和改成单层偏导。原 radial 相位变化在新的支集上准确为0；故没有一个额外未付的径向补偿项。

首层 (O.14) 的四个 log2 上界分别为
$-1047728,-768503,-701815,-1655679$。更深层中，最大 $J$ 次数50给比值小于 $65/64$，最坏指数 $31867/256-43-1/32>81$。所以四项均小于 $2^{-20}$，且无限尾继续衰减。全部误差之和小于 $d_-\|Z_M\|^2/2$，得到
$$
\boxed{\quad
\mathfrak G_{I_i,\psi}^{\rm joint}(Z_M)
<-\tfrac12d_-\|Z_M\|^2<0 .\quad}
\tag{O.15}
$$
这个型按第71束 (C.31) 完整定义，包含 $\Psi_{\rm tot}$、$\widehat z_{\rm tot}$、两个 $D\Gamma^*$ 列、两根和所有支集外响应。端点局部 gauge 为0，故它正是整个负窗原 physical height/total-flux 的 crossing；未把 principal 端角固定为恒等。沿原 anchor 参数的真实导数只再乘其正幅度 $r_a/N_a$，负号不变。

## 6. 对全网路线的准确影响

第73—77束在 $\kappa\le1/4$ 的共同正型保持成立。新的 (O.15) 表明，同一方向在原允许对象内部已有真实负向量，不能把它当作任意混频块的 PSD 控制。三段定理依赖低 incoming 包的量词也不能直接扩大。

本篇只是在单个完整负窗中指定合法的物理中心迹；尚未证明这个向量同时满足其余网络的全部外条件，故不称其为全网反例或近核。下一条合法路线必须给其它 $\kappa$ 的统一 packet 控制，或由实际全网 Schur 证明相关状态不会出现，并同时支付外部响应和源。正片 elliptic 性本身不限制 incoming 的 Fourier 支撑：完整 unitary Cayley 对每个高频 incoming 都有真实两端 graph。

ordinary/weak 源、total/bare 端荷及 mean 方程未因这个齐次反例而改变；它不授任何新的源逆。新的精确生产源与原生记录分别为[源码](../scripts/fourfold_common_low_direction_obstruction_20261114.py)和[实际预算](../notes/2026-11-14-R119-common-low-direction-obstruction-budget.json)。
