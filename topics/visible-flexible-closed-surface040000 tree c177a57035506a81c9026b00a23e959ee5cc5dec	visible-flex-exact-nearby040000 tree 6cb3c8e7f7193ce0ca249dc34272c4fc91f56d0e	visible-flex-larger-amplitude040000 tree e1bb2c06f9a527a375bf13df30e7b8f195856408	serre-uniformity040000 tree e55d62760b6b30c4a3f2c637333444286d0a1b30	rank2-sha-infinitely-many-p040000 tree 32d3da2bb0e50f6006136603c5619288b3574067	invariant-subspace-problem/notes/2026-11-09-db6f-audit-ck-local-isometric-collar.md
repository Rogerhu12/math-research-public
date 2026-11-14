# 解析 Gauss–Codazzi 给出的局部共同度量鞍领：周期重构、贴柱与非量化点对余量

作者：/root/independent_geometry，与 /root 共同提出并核对系统，2026-11-09。状态：以下是完整的局部解析存在证明，尚待未参与推导者全文独立审查。没有运行求解器、RK、源积分、数值优化或当前 M15 后端，也没有读取 M15 候选态。

**本稿已不再使用具有固有相位度量缺陷的 normal-offset 模板。** 它在一条预先固定的径向度量上证明真实局部等距图存在，并证明可以与原柱带 $C^2$ 接合。宽度只证明存在，没有算出任何可使用的数值下界；没有连接到固定圆领或帽，没有完整闭曲面，也没有全闭面 reach 结论。

## 1. 定理与精确范围

设

$$
\gamma:\mathbb R/(2\pi\mathbb Z)\longrightarrow\mathbb R^2\times\{0\}
$$

是实解析、单位速度、严格正曲率的凸闭曲线，按逆时针方向参数化。设其平面外法向为 $\nu$、曲率为 $\kappa_0>0$，因而
$\gamma''=-\kappa_0\nu$。先固定任意常数 $A_4>0$，令

$$
a(s)=1+A_4s^4,\qquad
g=ds^2+a(s)^2d\theta^2.
\tag{1}
$$

**局部定理。** 存在统一的 $\epsilon>0$ 和实解析周期浸入
$F:(-\epsilon,\epsilon)\times S^1\to\mathbb R^3$，满足

$$
F(0,\theta)=\gamma(\theta)+b e_z,\qquad
F_s(0,\theta)=e_z,\qquad F_{ss}(0,\theta)=0,
\tag{2}
$$

以及精确度量恒等式

$$
F_s\cdot F_s=1,\qquad F_s\cdot F_\theta=0,\qquad
F_\theta\cdot F_\theta=a(s)^2.
\tag{3}
$$

缩小 $\epsilon$ 后，它是嵌入；其高斯曲率为

$$
K(s,\theta)=-\frac{a''(s)}{a(s)}
=-\frac{12A_4s^2}{1+A_4s^4}<0
\quad(0<|s|<\epsilon).
\tag{4}
$$

把 $s\ge0$ 的部分接到高度 $b$ 的原竖直柱带，可得到完整 Cartesian 两阶连续的真实局部等距鞍领。

对本题 Poisson 或 N7 核，曲线支持函数的平均值为 $1$，所以周长为 $2\pi$；正曲率使弧长重参数化及其逆都实解析，满足上述单位速度假设。这里不把法向角直接误当弧长材料角。

若以中心柱带和上下镜像小鞍领组成带边面 $G_0$，定义

$$
G_\alpha(u,\theta)=R_\alpha G_0(u,\theta-\alpha),
\tag{5}
$$

则它们对同一径向度量精确等距，且对所有相位保持嵌入；其 $C^2$ 连续性也成立。若核心有 C3 对称性，构造继承该对称性，可取本题的相位范围 $[0,2\pi/3]$。

下面还证明：给定平面曲率半径下界 $m>0$，任意 $\tau<m$ 都可以在足够小、但未量化的同一 $\epsilon$ 上成为整个保留柱带及两局部鞍领的**法向点对半径**。这包括任意两点，不只同一小坐标盒；但它不等于宣称一个带边曲面已经支付无边界闭面的 reach。

## 2. 正确阶数的解析 Cauchy 问题

第二基本形式采用坐标系数，而不是正交框架系数：

$$
\mathrm{II}=L\,ds^2+2M\,ds\,d\theta+N\,d\theta^2.
$$

取初始法向

$$
n_0=e_z\times\gamma'=-\nu,
$$

即平面内法向。初始数据为

$$
M(0,\theta)=0,\qquad N(0,\theta)=\kappa_0(\theta)>0.
\tag{6}
$$

Gauss 方程可以显式解出

$$
L=\frac{M^2-a a''}{N}.
\tag{7}
$$

相应 Codazzi 系统为

$$
\begin{aligned}
M_s&=L_\theta-\frac{a'}aM,\\
N_s&=M_\theta+\frac{a'}aN+a a'L.
\end{aligned}
\tag{8}
$$

这里的 $N$ 是 $F_{\theta\theta}\cdot n$，不是把 $N/a^2$ 漏除的正交系数。把 (7) 在 $\theta$ 方向展开，第一式成为

$$
M_s=
\frac{2M}{N}M_\theta
-\frac{M^2-a a''}{N^2}N_\theta
-\frac{a'}aM.
\tag{9}
$$

第二式代入 (7) 后同样只含 $s,\theta,M,N$ 及它们的一阶 $\theta$ 导数。因此它是**一阶 $s$、一阶 $\theta$ 的解析系统**。并没有把含二阶 $\theta$ 导数的原 Frenet 位置演化直接套入一阶 Cauchy–Kowalevski 定理。

令

$$
U=(M,V),\qquad V=N-\kappa_0(\theta).
$$

则 $U(0,\theta)=0$，且 $N_\theta=V_\theta+\kappa_0'(\theta)$。
在任一初始点附近，(8)–(9) 可写成

$$
\partial_sU=\mathcal H(s,\theta,U,\partial_\theta U),
\tag{10}
$$

其中 $\mathcal H$ 对全部变量实解析。分母只有 $a$、$\kappa_0+V$ 的幂；初值上 $a=1$，且周期正曲率有
$\kappa_{\min}>0$，所以分母不为零。最高 $s$ 导数的系数是恒等矩阵，初始线在这个正常形中非特征。$a''(0)=0$ 不破坏这个非特征条件。

### 2.1 外部定理的实际核查

本次实际打开并阅读了 Tsogtgerel Gantumur 的 McGill 官方作者讲义：

*Math 580 Lecture Notes 2: The Cauchy-Kovalevskaya Theorem*，2011-10-03，§4，Theorem 18，印刷页 9–10。

[作者官方原文](https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf)

该定理给出正常形一阶解析系统、解析零初值的唯一局部解析解。它允许右端依赖其余变量的一阶导数，因此正好适用于 (10)。非零解析初值已通过 $V=N-\kappa_0$ 明确化为零初值。本文只调用这一清楚的一阶版本。

1875 年 Kowalevsky 论文 *Zur Theorie der partiellen Differentialgleichungen*，卷 80，页 1–32 的 [出版社书目页](https://www.degruyterbrill.com/document/doi/10.1515/9783112342428-001/html) 也已核到；该页正文不可访问，没有声称读完 1875 年原证明。上述现代作者讲义的定理文本与证明可以访问；未下载 PDF，未渲染页面。

### 2.2 统一宽度、周期性与实值性

对初始圆周每一点使用 Theorem 18，局部解析唯一性使相邻初始角区间上的解在共同邻域一致。取有限个较小角区间覆盖紧圆周，再把 $s$ 宽度缩到这些邻域的共同正下界，就得到统一
$|s|<\epsilon_0$ 的周期解。

周期性不是额外边界猜测：把 $\theta$ 换成 $\theta+2\pi$ 后，方程和初值相同，局部唯一性给相同解。实初值和实系数同样保证实轴上的解为实值；可通过复共轭后的唯一性说明。再由紧性和连续性缩小宽度，保证

$$
N(s,\theta)\ge\kappa_{\min}/2>0.
\tag{11}
$$

若 $\kappa_0$ 有 $2\pi/3$ 周期，同样的唯一性给 $M,N$ 的 $2\pi/3$ 周期。这是标量系数的周期性；空间框架的 C3 等变性将在重构中单独核对。

## 3. 从周期第二基本形式重构周期位置图

设空间框架矩阵 $E=(e_1,e_2,n)$ 的三列依次为两个切向量与法向量。对每个 $\theta$ 解线性常微分方程

$$
E_s=E\Omega_s,\qquad
\Omega_s=
\begin{pmatrix}
0&0&-L\\
0&0&-M/a\\
L&M/a&0
\end{pmatrix},
\tag{12}
$$

初值

$$
E(0,\theta)=(e_z,\gamma'(\theta),n_0(\theta)).
\tag{13}
$$

$\Omega_s$ 反对称，初值为正向正交框架，所以解一直在 $SO(3)$ 中。解析系数与解析参数初值使 $E$ 联合解析：例如其 Volterra 迭代级数在较小复邻域上按阶乘界一致收敛。系数与初值的周期性又直接给 $E$ 的 $2\pi$ 周期。

希望同时成立的角方向连接矩阵是

$$
\Omega_\theta=
\begin{pmatrix}
0&-a'&-M\\
a'&0&-N/a\\
M&N/a&0
\end{pmatrix}.
\tag{14}
$$

不能仅因为写出了 (14) 就假定框架满足它。定义兼容量

$$
W=E_\theta-E\Omega_\theta.
$$

直接求导得

$$
W_s=W\Omega_s-E\mathcal C,\qquad
\mathcal C=(\Omega_\theta)_s-(\Omega_s)_\theta+
[\Omega_s,\Omega_\theta].
\tag{15}
$$

$\mathcal C$ 是反对称矩阵，三个上三角元恰为

$$
\begin{aligned}
\mathcal C_{12}&=-a''-\frac{LN-M^2}{a},\\
\mathcal C_{13}&=-M_s+L_\theta-\frac{a'}aM,\\
\mathcal C_{23}&=\frac1a
\left(-N_s+M_\theta+\frac{a'}aN+a a'L\right).
\end{aligned}
\tag{16}
$$

由 (7)–(8)，$\mathcal C=0$。在 $s=0$，有
$a'=0,M=0,N=\kappa_0$；而平面 Frenet 公式是
$\gamma''=\kappa_0 n_0$、
$(n_0)_\theta=-\kappa_0\gamma'$。
所以 (13) 的角导数正好等于
$E(0,\theta)\Omega_\theta(0,\theta)$，即 $W(0,\theta)=0$。
齐次线性 ODE $W_s=W\Omega_s$ 给

$$
E_\theta=E\Omega_\theta
\quad\text{在整个小带成立。}
\tag{17}
$$

最后定义位置，而不沿 $\theta$ 积分：

$$
F(s,\theta)=\gamma(\theta)+b e_z+
\int_0^s e_1(t,\theta)\,dt.
\tag{18}
$$

该式直接保证位置周期性；不存在一个尚未核对的沿圆周积分闭合项。由 (12)，$F_s=e_1$。设
$Z=F_\theta-a e_2$，则由 (17)

$$
Z_s=(e_1)_\theta-a'e_2-a(e_2)_s
=(a'e_2+Mn)-a'e_2-Mn=0.
$$

初值 $Z(0,\theta)=\gamma'-e_2=0$，所以

$$
F_\theta=a e_2.
\tag{19}
$$

框架正交性立即给 (3)，从而 $F$ 是正则浸入。又
$F_{ss}\cdot n=L$、
$F_{s\theta}\cdot n=M$、
$F_{\theta\theta}\cdot n=N$，因此所重构的第二基本形式确实就是 (7)–(8) 的坐标系数，(4) 也随之成立。

若 $\gamma(\theta+2\pi/3)=R_{2\pi/3}\gamma(\theta)$，初始空间框架同样旋转等变，标量连接系数有 $2\pi/3$ 周期。ODE 唯一性给
$E(s,\theta+2\pi/3)=R_{2\pi/3}E(s,\theta)$；再由 (18)，位置图具有相同 C3 等变性。没有把标量周期与向量周期混为一谈。

## 4. 完整两阶贴柱与最初的向外项

初值处 $a'=a''=0,M=0$，故 $L=0$。从 (18)–(19) 得到

$$
F=\gamma+b e_z,\quad
F_s=e_z,\quad F_{ss}=0,\quad
F_{s\theta}=0,\quad F_{\theta\theta}=\gamma''.
\tag{20}
$$

这些正好是原竖直柱面在整条边界圈上的全部二阶数据。把 $s\le0$ 一侧换成精确柱面
$\gamma(\theta)+(b+s)e_z$，拼接后仍为 $C^2$，而不是只匹配平均值或法向二阶分量。

还可以明确算出第一个非平凡位置项。由
$a'(0)=a''(0)=a'''(0)=0$、$a''''(0)=24A_4$ 及 (7)–(8)，有

$$
L(0)=L_s(0)=0,\qquad
L_{ss}(0,\theta)=-\frac{24A_4}{\kappa_0(\theta)}.
$$

故

$$
F(s,\theta)=
\gamma(\theta)+(b+s)e_z+
A_4s^4\,\rho_0(\theta)\nu(\theta)+O(s^5),
\qquad \rho_0=1/\kappa_0.
\tag{21}
$$

余项对紧圆周一致，并可对任意预先固定有限阶角导数取一致界。特别地，
$F-F_{\mathrm{cyl}}=O(s^4)$、
$F_s-e_z=O(s^3)$、
$F_{ss}=O(s^2)$，所以拼接后的 $C^2$ 小扰动结论不是只从位置连续性猜得。

这与 R29 所写的平顶四阶入口首项一致；但此处给出的是解析存在证明，不是只把形式展开当成真解。

### 4.1 与正 Frenet 分支的局部关系

固定 $s$ 的空间曲线以速度 $a(s)$ 由 $\theta$ 参数化。其曲率在入口严格为正，小带内仍可保持非零，记 Frenet 框架为 $T,\mathcal N,\mathcal B$。由 (3) 及其 $\theta$ 导数，

$$
F_s\cdot T=0,\qquad
F_s\cdot\mathcal N=-\frac{a'}{a\kappa}.
$$

入口时 $\mathcal B=e_z=F_s$，故缩小小带后正号保持：

$$
F_s=
-\frac{a'}{a\kappa}\mathcal N+
\sqrt{1-\frac{(a')^2}{a^2\kappa^2}}\ \mathcal B.
\tag{22}
$$

所以 CK 重构也满足所需的正 Frenet 分支。逻辑顺序是先解合法的一阶 Gauss–Codazzi 系统，再验证位置图的 Frenet 表达；没有反过来对不符合阶数要求的位置 PDE 使用 CK。

## 5. 统一小带上的嵌入性、相位与上下拼接

先取一个已经由第 2–4 节得到的固定小开带。$F$ 在每个
$(0,\theta)$ 附近是嵌入，因为它是浸入；入口整圈 $\gamma$ 本身无自交。若任意缩小宽度都不能全局嵌入，就存在两列不同参数
$(s_j,\theta_j),(t_j,\psi_j)$，其中
$s_j,t_j\to0$，而它们的像相同。紧性给角度收敛子列，极限满足
$\gamma(\theta_*)=\gamma(\psi_*)$，故两极限角度相同。两参数最终都落在这一入口点的一个局部嵌入坐标盒内，矛盾。这证明某个统一宽度上的全局嵌入。

对实际中心柱带，用材料经线 $u$ 写

$$
G_0(u,\theta)=
\begin{cases}
\gamma(\theta)+u e_z,&|u|\le b,\\
F(u-b,\theta),&b\le u<b+\epsilon,\\
QF(-u-b,\theta),&-b-\epsilon<u\le-b,
\end{cases}
\qquad Q=\operatorname{diag}(1,1,-1).
\tag{23}
$$

在下接缝，$-\!QF_s(0)=e_z$、$QF_{ss}(0)=0$，所以也是完整 $C^2$ 接合。度量精确为

$$
g_*=du^2+a_*(u)^2d\theta^2,\qquad
a_*(u)=
\begin{cases}
1,&|u|\le b,\\
1+A_4(|u|-b)^4,&|u|>b.
\end{cases}
\tag{24}
$$

同一紧性反证可从整条已嵌入的中心闭柱带出发，证明缩小 $\epsilon$ 后上下拼接整体无自交：若碰撞参数趋于中心带，其极限必为中心柱的同一点，再与该点的局部嵌入性矛盾。这里中心带包括两个边界圈，并没有漏掉跨接缝的近点对。

(5) 的每个像就是 $R_\alpha G_0$ 的像，因此嵌入性对全部相位一致。拉回度量时，$\theta\mapsto\theta-\alpha$ 保持 (24)，而 $R_\alpha$ 为欧氏等距，故共同度量是精确的。周期函数平移对 $C^2$ 范数连续，给所需的相位连续性。

这个带边活动族本身的像仍是整体旋转关系；只有将它接到逐点固定的外部后，才可能得到完整闭族的 $E(3)$ 非平凡性。本稿没有省略这一步。

## 6. 保留活动片的非量化全点对余量

下面的稳定性结论专门保留“所有点对”量词。设平面核心的曲率半径全角不小于 $m>0$。对原柱面任意两点 $P,Q$，外法向 $N_P$ 满足

$$
2|(Q-P)\cdot N_P|\le\frac1m|Q-P|^2.
\tag{25}
$$

理由是平面凸曲线内滚动半径 $m$ 的圆盘给同样平面弦界，而不同高度只增加右边的弦长平方。此前正面接缝稿 §4.1 给了由支持函数 $h-m$ 的凸性直接推出这个全角滚动盘界的证明。

**小带点对引理。** 对任意固定 $\tau<m$，可进一步缩小同一个 $\epsilon>0$，使 (23) 的整个有限保留活动片都满足

$$
2|(Q-P)\cdot N_P|\le\frac1\tau|Q-P|^2
\quad(P\ne Q).
\tag{26}
$$

证明：在一个固定较大开带中，拼接图 $G_0$ 是 $C^2$ 浸入；缩小后已为嵌入。若不存在所述 $\epsilon$，则对 $\epsilon_j\downarrow0$，可选两点使 (26) 失败。参数都落在固定紧域内，取子列后，它们的极限位于中心柱带。

若极限点不同，法向点对商连续，(25) 给商的极限至多 $1/m<1/\tau$，矛盾。

若极限点相同，选同一局部参数坐标，参数差为 $v_j\to0$。$C^2$ Taylor 展开一致给

$$
\begin{aligned}
G(x_j+v_j)-G(x_j)
&=DG(x_j)v_j+\tfrac12D^2G(x_j)[v_j,v_j]+o(|v_j|^2),\\
N(x_j)\cdot DG(x_j)v_j&=0.
\end{aligned}
$$

浸入性在紧域上给一阶奇异值正下界。再取单位参数方向的收敛子列，法向点对商的上极限是极限点某个方向的法曲率绝对值，至多 $1/m$；接缝处完整两阶数据也是原柱面，所以该结论覆盖边界极限。仍矛盾。证毕。

这个论证给出了真实正宽度的存在，但没有算出它。因此不能把它当作在宽度 $.005$ 上已经完成的数值证书。

### 6.1 支持与曲率的同一宽度选择

若核心的径向支持下界为 $m_0>0$，中心柱面满足
$G_0\cdot N\ge m_0$，最大主曲率绝对值不超过 $1/m$。由 $C^2$ 紧性，对任何

$$
\sigma<m_0,\qquad K_*>1/m,\qquad
\delta_0>0,\qquad \epsilon_{\max}>0,
$$

可在同一缩小的宽度上同时保证

$$
G_0\cdot N\ge\sigma,\qquad
|\kappa_i|\le K_*,\qquad
\|G_0-G_{\mathrm{cyl}}\|_{C^0}\le\delta_0,\qquad
0<\epsilon\le\epsilon_{\max}.
\tag{27}
$$

这些只是严格余量的开放性，并不需要把 $A_4$ 送到零。$A_4$、整个公式 (1) 和相位范围始终预先固定；只在同一个精确解析解上选取足够小的定义子带。

## 7. 对新的 Poisson 双帽条件模型的具体应用

取 R27 的 $q=.99,r=.1$ 核，沿用正面几何稿的
$b=.01$、辅助包围 $B=.09$、球帽半径 $.1$、球心高 $\pm.3$、$\chi=.01$ 小帽，以及射线补充推荐的固定圆领半径区间 $[.34,.36]$、高度 $\pm.1$。

本例

$$
m=\frac{104}{995}>\frac9{100},\qquad
m_{0,\mathrm{lo}}>.65,\qquad
\frac1m=\frac{995}{104}<10.
$$

先固定例如 $A_4=1$，或任意其他预先规定的 $A_4>0$。第 6 节允许选取一个未量化的 $\epsilon>0$，同时满足

$$
\begin{gathered}
\epsilon\le.005,\quad
\|G_0-G_{\mathrm{cyl}}\|_{C^0}\le10^{-6},\\
G_0\cdot N\ge.6,\quad |\kappa_i|\le10,\quad
\tau_{\mathrm{active}}=.09>.0756.
\end{gathered}
\tag{28}
$$

这里 $\tau_{\mathrm{active}}$ 是 (26) 的任意点对半径，不把带边片误称为完整闭面。原柱带在 $|u|\le b$ 完全不动，其真实共同度量已经由 (24) 支付。

基准柱点的高度满足 $|u|\le.015<B$，故它位于活动包围柱中；$10^{-6}$ 的全位置余量保证真实局部等距片仍位于 $E_\alpha^B+\varepsilon\overline B_3$，其中原预算 $\varepsilon=.005$。这只传递位置包含，不拿 $C^0$ 误差来传递 reach；点对式已由另一个完整证明支付。

它与固定小帽的竖直距离下界至少为

$$
.3-.1-.01-.005-10^{-6}=.184999>2(.09).
$$

与新圆领的水平分离至少为
$m_{0,\mathrm{lo}}-.36-10^{-6}>2(.09)$。圆领与帽、两圆领、两帽之间的旧距离界仍大于 $2(.09)$。所以，结合球面和平面的点对公式，**所有保留片上任意两个点**仍统一满足半径 $.09$ 的法向点对式。对全部相位同样成立。

由此得到的是一组已经具有精确共同度量的带边活动片，加上两个固定帽片和两个固定圆领；这组分离片仍没有连接成闭面。若未来完成满足同一单向包围的闭连接，原初始点对和半相位支持见证就可调用既有的强比例转移：

$$
D_0<2.51518578393841,\qquad
\frac{\delta_E}{D_0}>.05109026903944,\qquad
\frac{\delta_{\mathrm{hold}}}{D_0}>.20712850442174.
$$

当前不能把这些条件式数字写成一个已存在闭等距族的测量。

所有保留片各自具有正支持，不意味着其未知连接能保持相同正下界；甚至仍需检查更强的全局正支持位置相容条件。因此本稿不把各片支持界取最小后调用 R10。新增连接及其混合点对、或真正完整的 R10 假设，继续另付。

## 8. 已前进的接口与仍然明确的缺口

这条解析构造支付了此前 normal-offset 接缝未支付的一件核心事项：**局部活动片确实对同一个预先固定的度量精确等距，且与原柱带有完整两阶接合。** 它有真实负高斯曲率，符合非凸连接所需的局部几何。

但下列量没有由 CK 自动给出：

- 没有可用的数值 $\epsilon$ 下界或解析范数常数，没有一张已导出的局部网格。
- 没有证明该解可延续到固定圆领半径 $.36$，更没有到达其平面两阶数据。
- 没有固定桥连接到偏轴球帽，没有连通闭嵌入。
- 没有所有新连接点的法向点对界，没有全闭面 reach。
- 没有最终全图度量误差/加密证书；局部解析等距不代付 G5。
- 没有读取、解释或修改当前 M15 优化轨迹；未来完整独立复跑角色不变。

这是对新 Poisson 双帽条件模型的局部正面存在结论，同时也适用于已审 N7 核。它不把一般 Cauchy–Kowalevski 存在定理的“某个邻域”偷换成已经具有所需宏观尺寸的连接段。

## 9. 来源与审查分工

仓库来源：

- R27：Poisson 曲线、支持/曲率半径和固定参数。
- R28：有限解析 N7 核及严格正曲率。
- R29：共同径向度量、旋转与材料移位机制、平顶入口和完整圆领两阶接口。
- notes/2026-11-09-db6f-audit-positive-collar-and-connection-bvp.md：滚动圆盘证明、位置包围与仍待闭合的问题。
- notes/2026-11-09-db6f-audit-positive-collar-radial-interface.md：旧圆领径向冲突与新 $[.34,.36]$ 的必要投影分离。

外部定理只采用第 2.1 节明确核读的作者官方 Theorem 18。周期拼接、框架平坦性、位置周期重构、嵌入性、两阶接合以及全点对小带余量均在本文中给出论证。

本稿由 root 提出 Gauss–Codazzi 入口后共同核对；不能将 root 对同一推导的审读包装成未参与者独审。正式独审仍须由未参与本推导的代理完成。本文无数值后端执行记录，也没有把纯理论核查标为一次实际求解。
