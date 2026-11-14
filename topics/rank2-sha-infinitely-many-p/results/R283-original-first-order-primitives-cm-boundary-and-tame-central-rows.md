# R283 — 原三源的一阶原函数、真实 CM 边界补偿与普通 tame 中央行

日期：2026-11-13。**状态：以下固定特征零原函数、两个真实奇 $i$ 型块、原 $A/B$ 的准确三阶极、全纯原函数的边界与 CM 补偿、原 $H$ 原函数的十六角色轨道，以及带普通周期和 tame 移权的完整中央行均已证明。原三个中央零被保真地返回两个全纯奇块；没有把原函数的 CM 投影非零或有限轨道当作原曲线中央非零。**

本篇的代数恒等式在特征零成立。最后的 Mellin 转置只取普通素数 $p\equiv1\pmod4$，不把 R278 的惰性素数同一个 $p$ 搬到这里。

## 1. 原角原函数与完整一阶恒等式

沿用 R277 的原来源
$$
S_A=A_{17}(2z)/16=\vartheta^{68}Q_A(s),\qquad
S_B=A_{34}=\vartheta^{68}Q_B(s),\qquad
S_H=A_{136}=\vartheta^{68}tQ_H(s),
\tag{1}
$$
其中
$$
x'=2y,\quad y'=3x^2-1,\quad y^2=x^3-x,\quad
u=x^{-1/2},\quad s=u^4=x^{-2},\quad t=-y/x^{3/2}.
$$
原点支取 $u=z+O(z^5),t=1+O(z^4)$，故 $u'=t$、$s'=4u^3t$。
所有 $Q$、下述 $B$ 和 $Z$ 均采用 R277 的精确系数。

令
$$
(1-s)B_i'-\frac12B_i=Q_i,\qquad i=A,B,
$$
$$
Z_A=tB_A(s)-a_0,\quad Z_B=tB_B(s)-b_0,\quad
Z_H=\int_0^sQ_H(v)\,dv,
\tag{2}
$$
其中
$$
a_0=-\frac{1248227362551868}{22563055139625},\qquad
b_0=\frac{727339049799116}{7521018379875}.
\tag{3}
$$
三条 $Z_i$ 都从 $s^2/2$ 起。定义实际原函数
$$
\boxed{G_i=\frac{\vartheta^{68}Z_i}{4u^3}.}
\tag{4}
$$
因此 $G_i=z^5/8+O(z^9)$，这里的原函数常数已固定为原点零。

写 $\zeta=\sigma'/\sigma$。由 $\vartheta^2=x\sigma^2$，准确有
$$
\frac{\vartheta'}\vartheta=\zeta+\frac yx.
$$
令
$$
\boxed{
\mathcal L=\partial_z-\mathcal W,
\qquad
\mathcal W=68\frac{\vartheta'}\vartheta+3\frac yx
=68\zeta+71\frac yx.
}
\tag{5}
$$

**定理 1。** 三条原来源满足完整特征零恒等式
$$
\boxed{\mathcal L G_A=S_A,\qquad
\mathcal L G_B=S_B,\qquad \mathcal L G_H=S_H.}
\tag{6}
$$

**证明。** 对 (4) 求导。$Z_A'=Q_A/t,Z_B'=Q_B/t,Z_H'=Q_H$ 是关于 $s$ 的导数，所以 $\vartheta^{68}Z_i' s'/(4u^3)$ 正是 (1)。其余两项是
$68(\vartheta'/\vartheta)G_i-3(u'/u)G_i$。
而 $u'/u=-y/x$，故余项恰为 $\mathcal W G_i$。$\square$

若设 $N_i=G_i/z$、$E=z\partial_z$，则同一恒等式是
$$
S_i=-\mathcal W G_i+(E+1)N_i.
\tag{7}
$$
原首权 $z^{p-1}$ 处的因子确实是 $p$；完整 Mellin 的因子并不固定为 $p$。
本篇使用真正的 $G_i$ 和 (6)，不把 $G_i/z$ 宣称为整个形式群上的有界测度。

## 2. 原 $A/B$ 的三阶极与两条合法全纯原函数

令 $\alpha=1+i$。R280 的真实范数二公式为
$$
w=s(\alpha z)=-\frac{4s}{(1-s)^2},\qquad
t(w)=\frac{1+s}{1-s},\qquad
u(\alpha z)=\frac{\alpha u}{t}=-\frac{\alpha x}{y}.
\tag{8}
$$
特别地，在 $T_0=(0,0)$ 附近，$s\to\infty,w\to0$，但 **$t(w)\to-1$**。
不能在这个点重新选成原点的 $+1$ 支。

置 $U=x^2$。从 (4)、(8) 得到准确拉回
$$
\boxed{
G_i(\alpha z)=\frac\alpha{16}\sigma^{136}y\,
\frac{(U-1)^{35}}U\,
Z_i\!\left(-\frac{4U}{(U-1)^2}\right),
}
\tag{9}
$$
其中 $Z_{A/B}$ 的 $t$ 仍按 (8) 代入。

对 $i=A,B$，(9) 唯一的非全纯部分为
$$
\boxed{
G_A(\alpha z)=G_A^{\rm hol}+\frac{\alpha a_0}{8}R_T,\qquad
G_B(\alpha z)=G_B^{\rm hol}+\frac{\alpha b_0}{8}R_T,
\quad R_T=\sigma^{136}\frac y{x^2}.
}
\tag{10}
$$
$R_T$ 在 $T_0$ 恰有三阶极，在原点从 $z^{137}$ 起；它没有别的极。
两个 $G_i^{\rm hol}$ 都属于 $\sigma^{136}y\mathbb Q(i)[U]_{\le32}$。

**证明。** 将 (9) 的 $Z_i=tB_i-c_i$ 写成
$$
\frac\alpha{16}\sigma^{136}y\left\{
\frac{(U-1)^{34}(U+1)}U B_i(w)
-c_i\frac{(U-1)^{35}}U\right\}.
$$
$B_i$ 次数十六，所以除了 $U=0$ 没有分母；在 $U=0$ 两项各贡献 $c_i/U$。
减去 $2c_i/U$ 后是多项式。原点 $G_i=O(z^5)$ 保证其次数至多三十二。
这也直接证明 (10) 的全部主部，未仅按多项式总次数判断。$\square$

第三来源的 $Z_H$ 是从 $s^2$ 起的十七次多项式，所以 (9) 已经全纯。
此外定义
$$
S_{AB}=b_0S_A-a_0S_B,\qquad
B_{AB}=b_0B_A-a_0B_B.
\tag{11}
$$
$B_{AB}(0)=B_{AB}'(0)=0$，故
$$
\boxed{
G_{AB}=b_0G_A-a_0G_B=-\frac14\vartheta^{68}yB_{AB}(s)
}
\tag{12}
$$
是原椭圆曲线上的全纯 untwisted 来源。
这是原 $A/B$ 的合法常数线性组合，不依赖未知中央值。

## 3. 两个真实奇 $i$ 型块与一维边界

记 $W=-y\vartheta\sigma^{67}$。两个原有限块分别是
$$
\boxed{
\mathcal V_i^-=-x\vartheta\sigma^{67}\mathbb Q(i)[U]_{\le16},\qquad
\mathcal V_i^+=\sigma^{68}y\mathbb Q(i)[U]_{\le16}.
}
\tag{13}
$$
两者的全局 $i$ 特征均为 $i$，维数均为十七；前者带原二挠 twist，后者无 twist。
实际有
$$
G_H=(-x\vartheta\sigma^{67})P_H^G(U),\qquad
P_H^G=-\frac14U^{17}Z_H(1/U),
$$
$$
G_{AB}=\sigma^{68}yP_{AB}^G(U),\qquad
P_{AB}^G=-\frac14U^{17}B_{AB}(1/U).
\tag{14}
$$
两个多项式均为十五次。

范数二拉回后，整个奇 $i$ 型空间为
$$
\sigma^{136}y\mathbb Q(i)[U]_{\le33}.
$$
真实归一 $T_0$ 平移的角作用是
$$
\mathcal J_iP=U^{33}P(1/U).
\tag{15}
$$
(9) 直接给
$$
G_{AB}(\alpha z)\in\mathcal J_i^{+},\qquad
G_H(\alpha z)\in\mathcal J_i^{-}.
\tag{16}
$$
二者各自所在块维数十七。这里只对实际全纯组合使用 (15)，没有把 (10) 的极自动放入这个有限块。

在两个块上，同一个 $\mathcal L$ 有如下准确矩阵：
$$
\boxed{
\mathcal L((-x\vartheta\sigma^{67})P)
=W\{-4(17P-UP')\},
}
\tag{17}
$$
$$
\boxed{
\mathcal L(\sigma^{68}yP)
=\sigma^{68}\{4U(U-1)P'+(70-68U)P\}.
}
\tag{18}
$$
(17) 在 $U^j$ 基上对角为 $-4(17-j)$，$0\le j\le16$。
(18) 是 $18\times17$ 真矩阵 $M_u$，第 $j$ 列只有
$$
(M_u)_{j,j}=70-4j,\qquad
(M_u)_{j+1,j}=4j-68.
\tag{19}
$$
两式可直接对 (13) 求导，并用 $y^2=x(U-1)$ 核实。

特别地，(18) 的像有一个准确边界。对 $P=\sum_{j=0}^{17}p_jU^j$，定义
$$
\boxed{
\ell(P)=\sum_{j=0}^{17}
\frac{4^{17-j}}{(35-2j)\binom{34-2j}{17-j}}p_j.
}
\tag{20}
$$
则 $\ell(U^{17})=1$、$\ell M_u=0$，且
$$
\operatorname{im}M_u=\ker\ell.
\tag{21}
$$
若原正权多项式为 $P_i(U)=U^{17}Q_i(1/U)$，准确有
$$
\boxed{\ell(P_A)=-a_0/2,\qquad \ell(P_B)=-b_0/2.}
\tag{22}
$$

**证明。** (20) 的相邻系数满足
$(70-4j)\ell_j+(4j-68)\ell_{j+1}=0$。
$M_u$ 最后十七行的行列式为 $(-4)^{17}17!$，所以秩十七。
若暂容许 $-U^{17}B_i(1/U)/4$ 的十七次项，(18) 仍返回 $P_i$；
其最高系数为 $-B_i(0)/4$，第十七列仅贡献 $2U^{17}$。
于是得到 (22)。这也证明边界恰为原函数常数所记录的障碍。$\square$

## 4. 用真实 CM 来源保留原 $A/B$ 的两条条件

只取 $S_{AB}$ 会丢掉原两条条件中的一条。下面以已知实际 CM 来源支付这条边界。

令 $\beta=4-i$，采用 R248 的原除法多项式
$$
\begin{aligned}
Q_\beta(U)&=U^4+(12-20i)U^3+(-10+28i)U^2-(20+12i)U+1+4i,\\
K_\beta(U)&=(4-i)U^4+(-12+20i)U^3+(28+10i)U^2-(20+12i)U-i.
\end{aligned}
$$
$\sigma(\beta z)=\sigma^{17}K_\beta$、
$x(\beta z)=xQ_\beta^2/K_\beta^2$ 和 $\vartheta(2z)=\sigma^4(U+1)$ 给
$$
\boxed{
C_\beta:=\vartheta(2\beta z)
=\sigma^{68}P_{C\beta}(U),\qquad
P_{C\beta}=UQ_\beta^4+K_\beta^4.
}
\tag{23}
$$
其质量规范为 $C_\beta(0)=1$，而 (20) 的准确值是
$$
\boxed{
e_\beta=\ell(P_{C\beta})
=\frac{194313797443214851}{4512611027925}
-\frac{218295166992512}{31556720475}i\ne0.
}
\tag{24}
$$
设
$$
c_A=-\frac{a_0}{2e_\beta},\qquad
c_B=-\frac{b_0}{2e_\beta}.
\tag{25}
$$
由 (21)，存在唯一实际全纯原函数
$$
\boxed{
G_A^{\rm CM},G_B^{\rm CM}\in\mathcal V_i^+,
\qquad
\mathcal L G_i^{\rm CM}=S_i-c_iC_\beta.
}
\tag{26}
$$
它们可由 (19) 从最高次数向下递推，无新的未知原函数。
其原点首项为 $-c_i z/4$，并准确满足
$$
\boxed{b_0G_A^{\rm CM}-a_0G_B^{\rm CM}=G_{AB}.}
\tag{27}
$$
本篇证书给出两条多项式的全部精确系数。

(26) 中的 $C_\beta$ 是真实 $\vartheta$ 单位缩放；不把一般 $\vartheta^{68}$ 称为秩零参考。
除固定有限坏素外，所有有理和 Gaussian 系数都在原整格中；没有按目标 $p$ 改选来源。

## 5. 原 $H$ 原函数的真实 CM5 运输与全部十六角色

本节先使用固定 $\pi=2+i,\bar\pi=2-i$，不将这个非 primary 的 $\pi$ 当作普通素位 Frobenius。
令 $\mathscr M_i=[\pi]_*[\bar\pi]^*$ 作用于 $\mathcal V_i^-$，采用 R248 原 theta lift。

给出可重算的完整纤维式。置
$$
Q_\pi=U-(1-2i),\quad K_\pi=\pi U-i,
$$
$$
P_\pi=Q_\pi^2
\{Q_\pi K_\pi+4U(Q_\pi'K_\pi-Q_\pi K_\pi')\}/\pi,
\tag{28}
$$
共轭下标同理。对目标 $U=a$ 的五次纤维
$$
f_a(U)=UQ_\pi^4-aK_\pi^4,
\qquad U_{\bar\pi}=UQ_{\bar\pi}^4/K_{\bar\pi}^4,
$$
从 R248 的正权真迹乘以准确的 $x/y$ 比，得到第 $j$ 列在 $a$ 的值
$$
\boxed{
a^8(a-1)^8\operatorname{Tr}_{f_a}
\left[
\left(\frac{P_{\bar\pi}}{P_\pi}\right)^{17}
\frac{U_{\bar\pi}^{\,j}}{U_{\bar\pi}^8(U_{\bar\pi}-1)^8}
\frac{Q_{\bar\pi}^3K_{\bar\pi}P_\pi}
 {Q_\pi^3K_\pi P_{\bar\pi}}
\right].
}
\tag{29}
$$
输出全纯且属于 (13)，所以多项式次数至多十六。
十七个准确纤维唯一确定矩阵；另一个独立纤维核查原迹。
这里的有限迹包括原 frame，未由形式相似另选一个矩阵。

令 $N_i=\mathscr M_i/(2+i)$。精确计算得到
$$
\boxed{N_i^{16}=1,\qquad
\det(X-N_i)=(X+1)(X^{16}-1).}
\tag{30}
$$
双重角色为 $-1$。其两个真正 CM 基向量是
$$
\boxed{
G_0(\beta z),\quad G_0(\bar\beta z),
\qquad G_0=-x\vartheta\sigma^3,
}
\tag{31}
$$
因为在 $-x\vartheta\sigma^{67}$ frame 中，它们的多项式准确为
$Q_\beta^3K_\beta$ 和共轭。

**定理 2。** (14) 的原 $G_H$ 在 $N_i$ 下的 Krylov 秩恰为十六。
全部十六角色投影非零；其 $-1$ 投影是
$$
\boxed{
\Pi_{-1}G_H=aG_0(\beta z)+\bar aG_0(\bar\beta z),
}
\tag{32}
$$
$$
a=-\frac{21155876867859}{1286339269178163200}
-\frac{208102787314109}{7718035615068979200}i.
$$
这个 CM 投影的实际一阶 jet 为
$$
\boxed{[z]\Pi_{-1}G_H=\frac{200236036963}{1079445540569088}\ne0.}
\tag{33}
$$

证书在 $\mathbb Q(i)$ 中计算十六列真实轨道，并给出其 $34\times32$ 实化矩阵的非零 $32$ 阶子式。
由于 (30) 只有十六个不同特征值，这准确证明全部角色出现，不是有限目标素数扫描。
(32) 则用 $\Pi_{-1}=16^{-1}\sum_{j=0}^{15}(-1)^jN_i^j$ 逐系数核实。

这个轨道并不与 (17) 的连接交换。若 $M_+$ 为 R248 的正块真实 CM5 矩阵，$L_i=\operatorname{diag}(-4(17-j))$，准确有
$$
\boxed{
\operatorname{rank}(M_+L_i-cL_i\mathscr M_i)=17,
\quad c=1,\ \pi/\bar\pi,\ \bar\pi/\pi.
}
\tag{34}
$$
所以原 $S_H$ 的一个中央零不能经 (17) 或 (30) 自由搬到 (32)。

另一个真实块 $\mathcal V_i^+$ 的 CM5 矩阵也保存在同一证书中。
它在纤维 $f_a$ 上的权是
$$
\boxed{
\operatorname{Tr}_{f_a}\left[
\left(\frac{K_{\bar\pi}}{K_\pi}\right)^{65}
\frac{Q_\pi P_{\bar\pi}}{Q_{\bar\pi}P_\pi}
U_{\bar\pi}^{\,j}\right].
}
\tag{35}
$$
这是 $\sigma^{68}$ 比和 $y$ 比相乘后的准确式。
其两个 CM 方向为 $(\sigma^4y)(\beta z)$ 及共轭，原多项式为
$Q_\beta K_\beta D_\beta$ 及共轭，其中
$D_\beta=\{Q_\beta K_\beta+4U(Q_\beta'K_\beta-Q_\beta K_\beta')\}/\beta$。
这两条线的实际 CM5 特征值是 $1-2i$，因此不能借用 (30) 的归一相位。
若按此标量归一为 $N_i^u$，则准确有
$$
\boxed{
(N_i^u)^{16}=1,\qquad
\det(X-N_i^u)=(X-1)^2(X+1)(X-i)(X+i)
(X^4-i)^2(X^4+i).
}
\tag{35a}
$$
这只含十二个不同角色，最小多项式为 $(X^4-1)(X^8+1)$。
尤其这里没有 $X^4=-1$ 的四个角色；两个真实奇块不能仅按同为十七维而互换。

实际原输入并没有遗漏这整个块。准确的轨道秩为
$$
\boxed{
\dim\langle(N_i^u)^jG_{AB}\rangle
=\dim\langle(N_i^u)^jG_A^{\rm CM}\rangle
=\dim\langle(N_i^u)^jG_B^{\rm CM}\rangle=12,
}
\tag{35b}
$$
$$
\boxed{
\left\langle (N_i^u)^jG_A^{\rm CM},
(N_i^u)^jG_B^{\rm CM}:0\le j<16\right\rangle
=\mathcal V_i^+.
}
\tag{35c}
$$
证书给出三个单输入的非零 $24$ 阶实化子式和双输入的非零 $34$ 阶实化子式。
(35a) 给出单输入十二维的上界，(13) 给出联合十七维的上界，因而这些子式恰好证明 (35b)–(35c)。
这是同一两条原来源经 (26) 已付 CM 补偿后的实际轨道；其完整中央观察仍按下面 (38)–(40)，不能从轨道张成自动读作所有行中央零。

## 6. 普通完整中央行：tame $1$、原周期与移权

以下取普通好素数 $p$，$d=p-1$。所有固定分母和 (24) 的坏素只排除有限集合。
令 $\Omega_0\in\mathcal O^\times$ 为 R266 的真实普通周期，
原 Amice 规范为 $G(\Omega_0\log(1+T))$，按实际形式群解释。
对有界原测度 $\nu_G$ 定义
$$
M_{G,j}(v)=\int_{\mathbb Z_p^\times}
\omega(x)^j\langle x\rangle^{dv}\,d\nu_G(x).
\tag{36}
$$
原 principal 行为 $M_{G,0}$。

对 (13) 的奇来源 $G$，$G(iz)=iG(z)$，故正确的导数观察是 tame $1$：
$$
\boxed{
M_{G',0}(u)=\Omega_0^{-1}M_{G,1}(u+1/d).
}
\tag{37}
$$
这是 Amice 上 $\partial_z=\Omega_0^{-1}(1+T)\partial_T$ 的逐测度恒等式。
完整单位核和周期没有消失，也没有把相邻权写成相同 principal 角色。

$\mathcal WG$ 作为原点 germ 是有界来源：由 (5)、(17)–(18)，它准确等于
$G'-\mathcal LG$，右侧是导数测度与已付有限 theta 来源之差。
它通常不是同一个有限 theta 块中的全局截面；本篇不将该连接乘法删除。

令
$$
J_\vartheta(u)=M_{\vartheta,0}(u),\qquad
J_\vartheta(0)=1-b_{\mathrm F}^{-1}\in\mathcal O^\times,
$$
其中 $b_{\mathrm F}$ 是 R266 的普通 Frobenius 单位，
不同于 (3) 的固定有理边界数 $b_0$。
定义真正的线性连接泛函
$$
\boxed{
\Phi_p(G;u)=
\frac{\Omega_0^{-1}M_{G,1}(u+1/d)-M_{\mathcal WG,0}(u)}
 {J_\vartheta(u)}.
}
\tag{38}
$$
(6)、(26) 给出全部 $u$ 的精确关系
$$
\boxed{
\Phi_p(G_H;u)=\frac{M_{S_H}(u)}{J_\vartheta(u)},\qquad
\Phi_p(G_i^{\rm CM};u)=
\frac{M_{S_i}(u)}{J_\vartheta(u)}-c_i((2\beta)^d)^u,\quad i=A,B.
}
\tag{39}
$$
最后一项使用真实 $C_\beta=\vartheta(2\beta z)$，所以其完整质量和尺度单位均已支付。

**定理 3。** 原三来源的单位质量均为零。其三个完整中央导数同时为零，当且仅当下列真实连接观察成立：
$$
\boxed{
\begin{aligned}
\Phi_p(G_H;0)&=0,&\quad \Phi_p'(G_H;0)&=0,\\
\Phi_p(G_A^{\rm CM};0)&=-c_A,&
\Phi_p'(G_A^{\rm CM};0)&=-c_A d\log_p(2\beta),\\
\Phi_p(G_B^{\rm CM};0)&=-c_B,&
\Phi_p'(G_B^{\rm CM};0)&=-c_B d\log_p(2\beta).
\end{aligned}}
\tag{40}
$$
其中质量等式本来就由原来源的质量规范成立；导数等式与原三个零逐条等价。
由 (27)，也可等价地保留 $G_H,G_{AB},G_A^{\rm CM}$ 三条观察：前两条导数为零，最后一条是 (40) 的已知非齐次 CM 对数。

**证明。** 对 (39) 在 $u=0$ 求值和求导。
原质量零使参考导数在原 $S_i$ 一侧准确相消；补偿来源有非零质量，故其尺度导数必须保留。
$a_0,b_0,c_A,c_B$ 都非零，而 (27) 给出所述可逆常数换基。$\square$

真实范数二拉回同样保留这条观察。若
$\widetilde G(z)=G(\alpha z)$、
$\widetilde{\mathcal W}=\alpha\mathcal W(\alpha z)$，则
$$
(\partial_z-\widetilde{\mathcal W})\widetilde G
=\alpha(\mathcal LG)(\alpha z).
$$
因此 (38) 的未除参考分子变为
$$
\boxed{
\alpha(\alpha^d)^u\,
\{\Omega_0^{-1}M_{G,1}(u+1/d)-M_{\mathcal WG}(u)\}.
}
\tag{41}
$$
这里的 $\alpha$ 正是 tame $1$ 在移位后得到的真实单位因子；有质量时导数还含 $d\log_p\alpha$ 项。

最后，(32) 的已知 CM 原函数也有不省质量的全行。令 $J_i=M_{G_0',0}$，则
$$
\boxed{
M_{(\Pi_{-1}G_H)',0}(u)
=\{a\beta(\beta^d)^u+\bar a\bar\beta(\bar\beta^d)^u\}J_i(u).
}
\tag{42}
$$
它的导数包括 $J_i'$ 项以及两个尺度对数；$J_i$ 是该实际奇参考的导数行，不能替成 $J_\vartheta$ 或 $J_8$。
(40) 约束的是带 $\mathcal W$ 的完整连接观察，而 (42) 只是一条已知 CM 导数行。
二者之间仍须通过真正的 $T_p$、连接交换差及原环带支付，(34) 表明这一步不是形式交换。

## 7. 精确证书与下一接口

证书为
`scripts/check-original-first-order-i-block-and-cm5.py` 及同名 JSON。
它重算 (29)、(35) 的原有限迹，保存两个真实奇块的全部矩阵、(10) 的主部与全纯部分、(14) 和 (26) 的原多项式、(20) 的余核、(24) 的真实 CM 边界及 (32) 的全部精确数据。
本次完成三十项精确恒等式检查，并保存 (35b)–(35c) 的全部秩证书。
所有结论使用固定有理或 Gaussian 算术；没有枚举目标素数。

现在原三零已经成为 (40) 的三条完整、可逐系数检查的观察。
后续可对这同一组原函数使用真实 $T_p$ 与导数转置；须保留 (38) 的 tame 移权、(41) 的质量和 (10) 的极支，不能只取其 CM 角色或单位环带之外的值。

依赖：[R248](R248-ray17-conjugate-trace-and-original-yang-projections.md)、
[R263](R263-ordinary-complete-bridges-and-actual-cartier-convolution-defect.md)、
[R266](R266-actual-ordinary-theta-trace-closure-and-paid-source-return.md)、
[R277](R277-original-three-source-low-adjoint-and-branch-pole-cancellation.md)、
[R280](R280-minimal-normtwo-frame-and-actual-ordinary-cartier-blocks.md)、
[R282](R282-true-prime-core-mellin-transfer-and-original-primitive-orbit.md)。
