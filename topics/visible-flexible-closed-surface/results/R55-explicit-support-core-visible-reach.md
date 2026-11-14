# R55：显式固定 H 支撑函数环带的有效可见幅度与全时间厚度

**状态：已证明，完整未参与者独立审查通过。** 2026-11-10 UTC。
作者 root / Astra-visible-flex-db6f0b0e；独立全文审查 coupled_prefix；
root 已完整读回独立审稿十三节后采纳。

存在一个共同光滑度量上的联合 C∞ 精确等距嵌入环带族，实际固定闭片 H 有内部，
以整个初态直径 D 计，有 H/D>1/4、δ_hold/D>3/50、全时间 reach/D>25/408 和全 E(3) 商 δ_E>0。
显式参数区间、实际材料弧长、完整像 Hausdorff 见证、含边界全法锥和两段共同存在时间均已核。
材料域仍有两条边界；δ_E 没有有效下界，有限领宽 δ 仅作非循环的严格存在性选择。
本结果不支付闭合、主 G5、新网格或最终完整数值重跑。

## 采用与来源锁

- 作者最终 v2：notes/2026-11-10-db6f-root-explicit-support-core-visible-reach-v2.md，
  commit 5eefd7fdec025686fd60a80d9d541228855f48dc，
  blob 2821bcdff72884b94018b807a81c1608ae004f93，23285 UTF-8 B，
  SHA256 8bea37845fe8b28ab2b5ac5c8f15474c5a96984ad13df2cdcc5951b0582c43db。
- [完整独立审查](https://github.com/Rogerhu12/math-research/blob/25cc8a1965556181e23bbfad9f140a1493ab0197/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-prefix-review-explicit-support-core.md)：
  commit 25cc8a1965556181e23bbfad9f140a1493ab0197，
  blob d511057f785520143c0588bf8be80c3e59c54d8e，20060 UTF-8 B，
  SHA256 04596cdfe694afdbcfe253c9bcc3c8c63508f5e5e03806837b1a9d20cf409068。
- 独审覆盖全部十三节并完整核 R50/R48 的实际应用；未参与本构造推导。
  v1 的唯一问题是零材料距离处的严格号，v2 已修正为全域弱号、正距离严格。
  独立者按三项明确替换重建 v2 全文逐字相同，附录字节未变。
- 作者冻结附录2577 ASCII B，SHA256 89177bfdeeff086902af009e32144960d121f2fee52358ded2753e9bd01369b0；
  00:05:49 UTC 独立单个 V8 cell 正常完成18项有理门，作者回执 commit 4fb6974b0f22167897165cc9f04e9a8d4f725245。
- 未参与者于00:13:58 UTC从固定v1源实际重跑18项有理门全部通过；
  自有回执 commit a41f34466b97722ec7d14365be3483d78d82a837，
  SHA256 22928cf0aea6579137e0e8b0dc4d8517181f79311835b79a6aa8fc8520590039。
  00:24:36 的 v2 全文同字节核不是第二次附录执行。
- 0 PDE/BVP/轨迹/网格程序执行；有限有理比较与完整数学证明分别记账。

下方逐字保留已审 v2 的全部十三节；其中历史“拟证明”状态由本采用记录更新。
不要求 C3，也不把新几何当作 flat17 的同一加密。

---

## 1. 准确结论及依赖边界

下面给一个固定材料环带 M、一个固定光滑度量 g 和联合 C∞ 的精确等距嵌入族
F_t，0≤t≤1。若 D=diam F_0(M)，拟证明

$$
D<51/25,\qquad
\operatorname{diam}F_0(H)/D>1/4,\qquad
\delta_{\rm hold}/D>3/50,
\tag{1}
$$

$$
\operatorname{reach}F_t(M)\ge1/8,\qquad
\operatorname{reach}F_t(M)/D>25/408>3/100,
\qquad \delta_{\rm E}>0.
\tag{2}
$$

H 是一个逐点固定、有非空内部的闭材料片。
这里的 D 始终包含整个圆柱和新增领圈。
δ_hold 是整张像的 Hausdorff 距离，未用材料点位移代替；
δ_E 对全部 E(3)，包括反射取商。

核心的参数区间显式固定为 τ∈[0,4/25]，t=25τ/4。
新增领的固定正宽 δ 由已有定理的共同寿命和一个统一低阶界选择；
本文没有把这个 δ 的存在转换成可执行的十进制数值。
两条边界、实际闭合、PDE 数值实现及主 G5/独立全流程仍未支付。

存在理论只用以下已全文独审输入：
- [R50 非减 Q](../results/R50-increasing-q-smooth-flat-entry.md)，
  作者 a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b，
  完整独审 0fbb537133c97af06cf55ca3939f002f5cfb17ad。
- [R48 非增 Q](../results/R48-monotone-flat-collar-smooth-data.md)，
  作者 9daa8aba8a341855811d2f1c164bfb3ca7eab0bc，
  完整独审 15b02049c367e344901fb13264a950f8ff5bf933。

本稿重新支付具体初值、两段组合、全图几何和有效位移，不从 R51 移用其常数。
不要求 C3。角周期为2π，所有实际位置和材料参数都在下面定义。
几何分工曾核对支撑函数/弧长的结构公式；本稿的有效参数、滚动球、
C² 稳定性及完整组合由 root 推导，另需未参与者审查。

## 2. 完全指定的光滑切换函数

令多项式阶跃在实轴上定义为

$$
P(x)=
\begin{cases}
0,&x\le0,\\
10x^3-15x^4+6x^5,&0<x<1,\\
1,&x\ge1.
\end{cases}
\tag{3}
$$

它是 C²、非减，0≤P≤1。中间区间

$$
P'=30x^2(1-x)^2,\qquad
P''=60x(1-x)(1-2x),
$$

故

$$
0\le P'\le15/8,\qquad |P''|\le10/\sqrt3<6.
\tag{4}
$$

取 ε_m=1/100；令

$$
k_m(s)=
\begin{cases}
c_m\exp[-1/(1-(s/\varepsilon_m)^2)],&|s|<\varepsilon_m,\\
0,&|s|\ge\varepsilon_m,
\end{cases}
\qquad \int_{\mathbb R}k_m=1.
\tag{5}
$$

正归一化常数 c_m 由此唯一确定。定义 η_m=k_m*P。
它是实际指定的 C∞ 非减函数，仍有(4)的导数界，
在 x≤−ε_m 恒0、x≥1+ε_m 恒1。
这里用正核卷积，不用有限多项式拼接冒充 C∞。

在 φ∈[−π,π] 上置

$$
\chi(\phi)=\eta_m\!\left(\frac{|\phi|-2/5}{8/5}\right),
\qquad
\psi(\phi)=\chi(\phi)\sin\phi,
\tag{6}
$$

然后2π周期延拓。由于 χ 在 |φ|≤48/125 恒0，
绝对值在0处的折点不影响光滑性。
在 |φ|≥252/125 时 χ 恒1，而252/125<3<π，
故 ψ 在周期接缝邻域就是 sinφ。它确为整个材料圆上的 C∞ 函数。

χ 偶、ψ 奇，所以

$$
\int_0^{2\pi}\psi\,d\phi=0,\qquad
|\psi|\le1,\qquad
\psi=0\text{ 在 }|\phi|\le48/125.
\tag{7}
$$

在正半轴过渡区，
ψ+ψ''=χ''sinφ+2χ'cosφ；负半轴给同一绝对值界。
由(4)及尺度8/5，

$$
|\psi+\psi''|
\le \frac6{(8/5)^2}+\frac{2(15/8)}{8/5}
=\frac{75}{16}.
\tag{8}
$$

还需一个有效的支持见证。卷积正性及单调性给 η_m(x)≥P(x−1/100)。
在 φ=π/2，利用π>3，

$$
\frac{5\pi}{16}-\frac14-\frac1{100}
>\frac{271}{400},
\qquad
\psi(\pi/2)>P(271/400)>\frac45.
\tag{9}
$$

最后一个不等式是明确有理多项式比较，附录源码逐字核它。
π>3 可由内接正六边形得到；下文用到的π<22/7也可由
∫_0^1 x⁴(1−x)⁴/(1+x²)dx=22/7−π>0直接证明。
没有浮点三角采样门。

## 3. 整个有效参数区间上的真实闭凸曲线

对每个 τ∈[0,4/25]，定义支持函数及曲率半径

$$
h_\tau(\phi)=1+\tau\psi(\phi),\qquad
\rho_\tau=h_\tau+h_\tau''
=1+\tau(\psi+\psi'').
\tag{10}
$$

(8) 给整个闭参数区间上的有效界

$$
\frac14\le\rho_\tau\le\frac74.
\tag{11}
$$

定义真实平面位置

$$
\widehat\gamma_\tau(\phi)
=h_\tau e_r(\phi)+h_\tau' e_\phi(\phi),
\quad e_r=(\cos\phi,\sin\phi),\quad
e_\phi=(-\sin\phi,\cos\phi).
\tag{12}
$$

直接微分：
widehatγ' =ρ e_φ，故正则、实际位置周期，周长

$$
\int_0^{2\pi}\rho_\tau\,d\phi
=\int_0^{2\pi}h_\tau\,d\phi=2\pi.
\tag{13}
$$

下面的支持证明同时排除自交。
若 q 是任意光滑周期函数且 q+q''≥0，则对角差绝对值≤π的 α、β，

$$
q(\beta)-\{q(\alpha)e_r(\alpha)+q'(\alpha)e_\phi(\alpha)\}
                   \cdot e_r(\beta)
=\int_\alpha^\beta(q+q'')(s)\sin(\beta-s)\,ds\ge0.
\tag{14}
$$

β<α时，积分方向与正弦符号同时改变，仍非负。
为任何两个圆上角都选最短角lift，即得到所有支撑半平面的不等式。
对 q=h_tau，(11)使不同角的右侧严格为正
（相差π也有开区间严格正），
故(12)是严格凸闭线，其支持函数确为 h_tau。
也可由所有半平面交的支撑点唯一性得到同一结论：
若支持函数可微，支撑点的径向/切向坐标必须是 q、q'。

取共同单位速率材料坐标

$$
u_\tau(\phi)
=\phi+\tau\left\{\int_0^\phi\psi(v)\,dv+\psi'(\phi)\right\}.
\tag{15}
$$

这里 ψ'(0)=0，故归一化 u_tau(0)=0；u_tau'=ρ_tau>0，
且 u_tau(φ+2π)=u_tau(φ)+2π。
它是完整圆周上的度数1光滑微分同胚。
逆函数 φ_tau(u) 对(τ,u)联合光滑，定义

$$
\gamma_\tau(u)=\widehat\gamma_\tau(\phi_\tau(u)).
\tag{16}
$$

于是 |γ_tau'|=1，T_tau=e_φ(phi_tau)，
内法向ν_tau=e_z×T_tau=−e_r(phi_tau)，曲率

$$
\kappa_\tau=1/\rho_\tau,\qquad
4/7\le\kappa_\tau\le4.
\tag{17}
$$

所有角向高阶范数在固定紧τ区间上一致有限。
在 |φ|≤3/10，ψ及其全部导数和从0的积分均为0，
故 u_tau=φ、γ_tau(u)=e_r(u)，同时是材料和空间的实际恒等。

## 4. 滚动球与原圆柱的全法锥不等式

固定 R=1/4，令 q_tau=h_tau−R。
由(11)，q_tau+q_tau''=ρ_tau−R≥0，且
q_tau≥1−4/25−1/4=59/100>0。

由(14)，K_q定义为所有支撑半平面的交，
是含正圆盘的有界凸体，支持函数为q_tau，
支撑点为q_tau e_r+q_tau' e_φ。
原凸体K_h的支持函数h_tau=q_tau+R，
因此

$$
K_h=K_q+\overline B_R.
\tag{18}
$$

这个等式直接由 Minkowski和的支持函数相加及凸体由支持函数决定得到。
特别地，对原曲线任一点 p=widehatγ_tau(α)，
其外法向 n=e_r(α)，闭球

$$
\overline B(p-Rn,R)\subset K_h
\tag{19}
$$

真正包含在凸体内。对任何另一个边界点 q，有

$$
n\cdot(q-p)\le0,\qquad
(-n)\cdot(q-p)\le |q-p|^2/(2R).
\tag{20}
$$

第二式来自 q不在(19)的开球内。这个全点对界不只是局部曲率界。

对任意闭区间 J，定义真实参考圆柱

$$
B_\tau(r,u)=(\gamma_\tau(u),r),\qquad (r,u)\in J\times S^1.
\tag{21}
$$

给定p及任何满足所有可行一阶方向条件
ν·DB_tau(p)v≤0的向量ν，
其水平分量必是曲线法向的一个有符号倍数，
竖直分量与所有可行径向位移的内积非正。
故对任意q，由(20)精确得到

$$
\nu\cdot\{B_\tau(q)-B_\tau(p)\}
\le \frac{|\nu|}{2R}|B_\tau(q)-B_\tau(p)|^2.
\tag{22}
$$

此式包括上下边界的整个一侧法锥。
最近点的一阶必要条件与(22)给参考圆柱的 reach≥R：
若d<R，两不同像点到同一z的距离平方之差至少
(1−d/R)倍弦长平方，矛盾。
没有把边界位移强制为全切平面的正交向量。

## 5. 可用于扰动的全局参数弦及 Hessian

对两个法向角 α、β，取 δφ∈[0,π] 的最短法向角弧。
(18)给曲线弦在该弧中点切向上的投影至少
2R sin(δφ/2)。
也可直接把ρ=(ρ−R)+R积分；
ρ−R≥0，且该弧上的切向投影cos(s−mid)非负。

设d_u是两个材料弧长坐标的最短差。
这一法向短弧的长度最多(7/4)δφ，而d_u不超过任何一条连接弧长。
因此

$$
|\gamma_\tau(u)-\gamma_\tau(v)|
\ge\frac{2R}{\pi}\delta\phi
\ge\frac{2}{7\pi}d_u\ge\frac1{11}d_u.
\tag{23}
$$

最后使用π<22/7；当d_u>0时最后比较严格，d_u=0时只取弱界。无需假定最短法向角弧也是最短弧长弧。
参考圆柱的竖直、水平弦正交，故对最短角lift差z=(Δr,Δu)，

$$
|B_\tau(q)-B_\tau(p)|\ge\frac1{11}|z|.
\tag{24}
$$

同时DB_tau的两列是正交单位向量，且
B_rr=B_ru=0、B_uu=κν，由(17)得

$$
|D^2B_\tau[z,z]|\le4|z|^2.
\tag{25}
$$

这些界对任意J和全部τ有效。

## 6. 显式的带边 C² 扰动 reach 引理

设F在同一J×S¹上联合光滑，记E=F−B_tau。
假定0<ε≤1，11ε<1，并且在平直(r,u)参数中

$$
\|DE\|_{\rm op}\le\varepsilon,\qquad
|D^2E[z,z]|\le\varepsilon|z|^2.
\tag{26}
$$

沿最短角lift直线段积分及(24)给

$$
|F(q)-F(p)|
\ge(1-11\varepsilon)|B_\tau(q)-B_\tau(p)|>0.
\tag{27}
$$

DB的最小奇异值为1，故F还为浸入，进而是紧域上的嵌入。

在p处，以参考正交框架(e_z,T,ν_0)定义一个真实线性映射A：
A e_z=F_r、A T=F_u、A ν_0=F_r×F_u。
两列误差最多ε，第三列误差最多2ε+ε²≤3ε，所以

$$
\|A-I\|_{\rm op}\le5\varepsilon,\qquad
\|A\|_{\rm op}\le1+5\varepsilon.
\tag{28}
$$

A只在p处固定。对任意满足F的可行一阶方向条件的向量ν，
ν_0^*=A^Tν满足B的相同条件，因为A DB(p)=DF(p)。
故可对ν_0^*使用(22)，包括边界全部法锥。

函数F−AB在p的一阶导数为0。
由(25)、(26)、(28)，沿同一可行参数直线段的二阶界为21ε，
于是

$$
F(q)-F(p)=A\{B(q)-B(p)\}+\mathcal R,\qquad
|\mathcal R|\le(21/2)\varepsilon |z|^2
\le(2541/2)\varepsilon |\Delta B|^2.
\tag{29}
$$

所以

$$
\nu\cdot\Delta F
\le\frac{|\nu|}{2}
 \left\{\frac{1+5\varepsilon}{R}+2541\varepsilon\right\}
 |\Delta B|^2.
\tag{30}
$$

利用(27)和R=1/4，令

$$
R_\varepsilon
=\frac{(1-11\varepsilon)^2}{4+2561\varepsilon}.
\tag{31}
$$

便得到 ν·ΔF≤|ν||ΔF|²/(2R_ε)。
对最近点作同一距离平方比较，严格证明
reach F(J×S¹)≥R_ε。
此引理处理整张有边曲面而非仅其中心曲线或局部曲率。

以下固定

$$
\varepsilon=1/1000,\qquad
R_\varepsilon=\frac{978121}{6561000}>\frac18.
\tag{32}
$$

这给稍后的新增领一个明确允许的C²误差门。

## 7. 固定的小 Q 剖面及两段实际 PDE

令 h_0=1/100，ε=1/1000如(32)，固定

$$
q_*=\varepsilon/100=1/100000.
\tag{33}
$$

这里 q_* 只是新曲率剖面的幅度，与 flat17 的嵌入未知量q无关。
设E_+(x)=exp(−1/x)于x>0、否则0，取固定光滑非减阶跃

$$
S(x)=\frac{E_+(x-1/4)}
           {E_+(x-1/4)+E_+(3/4-x)}.
\tag{34}
$$

它在x≤1/4恒0、x≥3/4恒1。
对待选δ，定义同一个径向剖面

$$
Q_\delta(r)=
\begin{cases}
0,&r\le0,\\
q_*S(r/\delta),&0\le r\le\delta,\\
q_*\{1-S((r-\delta)/\delta)\},&\delta\le r\le2\delta,\\
0,&r\ge2\delta.
\end{cases}
\tag{35}
$$

各拼点附近都为常数，所以Qδ全C∞。
令a''=Qδ/a，a(0)=1、a'(0)=0，负r延为a=1。
在0≤r≤1/2上有

$$
1\le a\le1+q_*r^2/2<2,\qquad
0\le a'\le q_*r,\qquad
0\le a''\le q_*.
\tag{36}
$$

这是先由a''≥0得a≥1，再积分a''≤q_*所得的真实ODE界；
正有界解可以延拓，故没有在界成立前假设全窗存在。

r≤0的实际圆柱为Bτ(r,u)=(γτ(u),r)。
在r=0给正交框架e_1=e_z、e_2=Tτ、N=ντ及

$$
M_0=L_0=0,\qquad C_0=\kappa_\tau>0,\qquad
X_0=0,\quad Y_0=1/\kappa_\tau.
\tag{37}
$$

(11)、(15)–(17)给所需所有光滑角范数的统一界及
Y_0≥1/4。它们对整个τ∈[0,4/25]有效。

先把上升剖面q_*S(r/δ)在r≥δ后延为常数q_*，
用R50得到与δ无关的共同T_up。
a、a'、μ=a'/a、β=aa'的界只用(36)，不含Q'。
背景P=0。上升能量在交接Q=q_*处给实际X、Y的统一H4界：
Y的H4本来非加权，X=QZ又由加权Z控制
（固定q_*>0；这里只需界有限并对δ统一）。
正Y下界也保持。

先只考虑0<δ<min(1/2000,T_up/2)的全部交接数据；
这些数据在一个统一H4有界集内且Y有同一正下界。
R48对其给共同T_down，仍不依δ。
下降剖面用(35)后半段，并从真实交接数据起步。
在r=δ附近两剖面同为q_*，a同值同导数，
唯一性给两实际解在一个开邻域上重合。
这里不要求Q对δ的高导数有界，也不把δ当作被动参数使用。

两段统一低阶角范数和Y正下界，连同物理方程

$$
L=(M^2-Q)/C,\quad
M_r=L_u-\mu M,\quad C_r=M_u+\mu C+\beta L
\tag{38}
$$

给某个K_*≥1，使整个两段上

$$
|M_r|+|C_r|\le K_*.
\tag{39}
$$

这个K_*可对上述全部候选δ和全部τ共同选择：
右端只用一次角导数、Q、μ、β，完全不含Q'。
下降存在窗可预先取不超过1/4，使(36)持续覆盖；
高角阶仅影响其自身界，不再次缩短低阶共同寿命。

现在才固定一个正数

$$
0<\delta<
\min\{1/2000,\ T_{\rm up}/2,\ T_{\rm down}/2,\
                         \varepsilon/(200K_*)\}.
\tag{40}
$$

于是整个[0,2δ]及全部τ确在共同存在区间内，并且

$$
|M|\le\varepsilon/100,\quad
|C-C_0|\le\varepsilon/100,\quad
1/2<C<5.
\tag{41}
$$

这由(39)自r=0积分得到，C_0∈[4/7,4]。
(40)是非循环选择：先固定τ全区间、q_*与统一数据界，
再统一两个寿命和K_*，最后选δ。
选定以后g、材料域及整个t区间均固定，δ不会随t或网格改变。

## 8. 完整位置、周期和开平坦接合

从实际初始位置Bτ(0,u)和(37)的框架解

$$
F_r=e_1,\quad (e_1)_r=LN,\quad
(e_2)_r=(M/a)N,\quad
N_r=-Le_1-(M/a)e_2.
\tag{42}
$$

反对称框架方程保正交。
Gauss式LC−M²=−Q=−aa''和(38)正是角关系

$$
F_u=ae_2,\quad
(e_1)_u=a'e_2+MN,\quad
(e_2)_u=-a'e_1+(C/a)N,\quad
N_u=-Me_1-(C/a)e_2
\tag{43}
$$

的兼容条件。对角关系的误差作r微分，
代入(38)、(42)得到齐次线性系统；初始误差全为0。
故(43)成立，真实诱导度量正是

$$
g=dr^2+a(r)^2du^2.
\tag{44}
$$

原初始位置、框架及系数均真实周期，ODE唯一性使F本身周期，
不只是第二形式周期。没有待事后修补的平移monodromy。
两个存在定理的初值参数结论适用，因为a、Q对τ固定；
F因而联合C∞依赖(r,u,τ)。

在r≤δ/4的正侧Q=0、a=1。
M=0、C=κτ(u)是(38)的实际平稳解。
唯一性及(42)给F=Bτ，故与负r原柱在开邻域完全一致，
全部Cartesian jet匹配。

固定材料域

$$
M=[-h_0,2\delta]\times S^1.
\tag{45}
$$

在r≥7δ/4及稍向外的开邻域，Q=0且a为仿射函数。
因为中段Q严格正，a'(2δ)>0且a(2δ)>1。
(41)给C>0，所以LC=M²，第二形式是非零秩一。
这是有限平坦领，仍不是零第二形式的平面帽接口。

## 9. 实际 C² 误差逐项支付

本节把E=F−Bτ在整个(45)上带入§6，不能只用抽象连续性。
在正r≤2δ<1/1000上，由(33)、(36)、(41)，

$$
a'<\varepsilon/100000,\quad
a-1<\varepsilon/200000000,\quad
|L|\le2\{(\varepsilon/100)^2+\varepsilon/100\}
<\varepsilon/20.
\tag{46}
$$

C下界用1/2，Q≤q_*=ε/100。
由(42)径向积分，

$$
|N-\nu_\tau|
<3\varepsilon/50000,\quad
|F_r-e_z|<\varepsilon/20000,\quad
|e_2-T_\tau|<\varepsilon/100000.
\tag{47}
$$

例如|N_r|≤|L|+|M|/a<3ε/50，
乘r<1/1000便给第一式。
另有F_u−T=(a−1)e_2+(e_2−T)，
故两列误差之和小于

$$
\varepsilon\left\{
1/20000+1/200000000+1/100000\right\}<\varepsilon.
\tag{48}
$$

这支付DE的算子范数门。

真实二阶位置式是

$$
F_{rr}=LN,\qquad
F_{ru}=a'e_2+MN,\qquad
F_{uu}=-aa'e_1+CN.
\tag{49}
$$

参考柱只有B_uu=C_0ντ非零。
由(41)、(46)、(47)及C_0≤4，分别有

$$
|E_{rr}|<\varepsilon/20,\qquad
|E_{ru}|
<\varepsilon(1/100000+1/100)<\varepsilon/50,
\tag{50}
$$

$$
|E_{uu}|
<\varepsilon\{2/100000+1/100+12/50000\}
<\varepsilon/50.
\tag{51}
$$

因此对任意方向z，

$$
|D^2E[z,z]|
\le\{\max(\varepsilon/20,\varepsilon/50)
                         +\varepsilon/50\}|z|^2
<\varepsilon|z|^2.
\tag{52}
$$

负r原柱上E=0，接缝是开重叠，所以(48)、(52)在完整固定域成立。
这些误差没有使用Q'或更高径向截止导数。
§6遂证明全部时间的实际嵌入及

$$
\operatorname{reach}F_t(M)\ge R_\varepsilon>1/8.
\tag{53}
$$

可以保守报告≥1/8；不是把中心曲线的reach直接移到新曲面。

## 10. 真正固定的 H 及整个初态直径

定义同一个闭材料片

$$
H=[-3/400,-1/400]\times[-3/10,3/10]\subset M.
\tag{54}
$$

角区间按S¹解释。它有非空二维内部，完全在原负r柱面内。
§3给γτ(u)=e_r(u)在这一整角区恒等，所以F_t|H=F_0|H。

在r=−1/200取角±3/10的两点，距离

$$
2\sin(3/10)>2\{3/10-(3/10)^3/6\}
=591/1000.
\tag{55}
$$

初态τ=0的中心曲线是单位圆。
径向速度恒为1，每个图点到对应中心圈的距离最多h_0+2δ。
于是完整新图的初态直径

$$
D\le2(1+h_0+2\delta)
<1011/500<51/25.
\tag{56}
$$

因此

$$
\operatorname{diam}F_0(H)/D
>\frac{591/1000}{51/25}>\frac14,
$$

$$
\operatorname{reach}F_t(M)/D
>\frac{1/8}{51/25}=\frac{25}{408}>\frac3{100}.
\tag{57}
$$

D包括两段新领与整个旧柱；没有用周长、宽度或只含核心的直径代替。

## 11. 有效握持像位移与全欧氏群非平凡性

取终态τ=4/25，并选原柱中r=−1/200、
其法向角为φ=π/2的真实点p。
它的材料角是u_tau(π/2)；这不影响像距离的见证。
由(12)，p的水平y坐标正是h_tau(π/2)。
(9)给

$$
p_y>1+\frac4{25}\frac45=1+\frac{16}{125}.
\tag{58}
$$

对初态整张图：负r部分的y≤1，正r新增领的点距相应单位圆点≤2δ，
故其所有点均满足y≤1+2δ。
沿固定y方向的投影已经给欧氏距离下界，因此

$$
\operatorname{dist}(p,F_0(M))
>16/125-2\delta>127/1000.
\tag{59}
$$

这是真实像点到完整初态像的距离；没有把同一个材料点的运动长度充作Hausdorff距离。
于是

$$
\delta_{\rm hold}/D
>\frac{127/1000}{51/25}=\frac{127}{2040}
>\frac3{50}>\frac1{20}.
\tag{60}
$$

握持片全程固定，所以未做任何欧氏对齐。

还需独立排除全E(3)族。
两条边界的长度分别为2π和2πa(2δ)>2π。
任何将完整有边像映到初态的欧氏等距，
必把边界分量映到边界分量并保持长度，因而底边只能映到底边。

初态底边是单位圆。
对τ>0，若γτ也是圆，则其周长2π迫使半径1，
支持函数须为1+b_x cosφ+b_y sinφ。
但τψ在一个开弧恒0，又不恒零，不能是一阶正弦余弦组合。
所以底边非圆，矛盾。这个判据包括所有反射，
没有预先假定刚体保轴、材料标号或H。

对两固定紧像，若E(3)商Hausdorff下确界为0，
一列逼近刚体的平移部分有界，正交部分属于紧群O(3)；
取子列极限即给真实全等，与上面矛盾。
故每个τ>0相对初态的商距离严格正，特别δ_E>0。
本稿没有声称任意两个非零τ均两两不全等，也没有给δ_E的有效正数。

## 12. 完成边界与可重现对象

本稿的核心hτ、核k_m、材料反解及τ范围完全指定。
无需隐函数求根选择有效形变量，也不只证明一阶非平凡。
q_*=1/100000、共同Q剖面的公式也固定。
δ仍由(40)的严格存在性选择，尚无计算过的有效十进制半径；
没有运行PDE或生成这张新图的网格。

所述整体g与M在选定一次δ后对全部t固定，等距是精确恒等式。
它不是把δ随网格缩小来压低缺陷，也不是 flat17 的一次加密。
证明包含全部时间、全部曲面和边界最近点，而非端点采样。

材料域仍有两条边界，末端是非零秩一II的平坦领。
真正的固定帽/正曲率桥和完整闭曲面没有构造出来。
因此即使完整独审通过，也只是本题的有边中间结论，
不支付README完成门、主G5、新闭图网格或最终独立全流程。

## 13. 冻结的有限有理检查源

以下源码只核本文已经列出的有限有理不等式，不计算曲线/PDE数组。
正文冻结时不预签运行结果；实际固定回读后的作者执行另存回执。
它不能替代支持函数凸性、滚动球、法锥扰动、PDE组合和全E(3)的全文独审。

```javascript
(() => {
"use strict";
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>Q(-a[0],a[1]),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
const pow=(a,n)=>{let r=Q(1n);while(n--)r=mul(r,a);return r;};
const lt=(a,b)=>a[0]*b[1]<b[0]*a[1],eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const fmt=a=>a[0]+"/"+a[1],rows=[];
const pass=(name,a,b)=>{if(!lt(a,b))throw Error(name);rows.push({name,left:fmt(a),right:fmt(b),result:"PASS"});};
const equal=(name,a,b)=>{if(!eq(a,b))throw Error(name);rows.push({name,left:fmt(a),right:fmt(b),result:"PASS"});};
const one=Q(1n),eps=Q(1n,1000n),tau=Q(4n,25n),delta=Q(1n,2000n);
const S=x=>add(sub(mul(Q(10n),pow(x,3)),mul(Q(15n),pow(x,4))),mul(Q(6n),pow(x,5)));
equal("support derivative bound",add(div(Q(6n),pow(Q(8n,5n),2)),div(mul(Q(2n),Q(15n,8n)),Q(8n,5n))),Q(75n,16n));
equal("curvature radius margin",mul(tau,Q(75n,16n)),Q(3n,4n));
pass("fixed grip inside zero window",Q(3n,10n),Q(48n,125n));
pass("periodic saturation before pi",Q(252n,125n),Q(3n));
pass("positive support witness",Q(4n,5n),S(Q(271n,400n)));
pass("positive C margin",Q(1n,2n),sub(Q(4n,7n),div(eps,Q(100n))));
pass("upper C margin",add(Q(4n),div(eps,Q(100n))),Q(5n));
pass("normal radial Hessian",mul(Q(2n),add(pow(div(eps,Q(100n)),2),div(eps,Q(100n)))),div(eps,Q(20n)));
pass("mixed Hessian error",mul(eps,add(Q(1n,100000n),Q(1n,100n))),div(eps,Q(50n)));
pass("angular Hessian error",mul(eps,add(add(Q(2n,100000n),Q(1n,100n)),Q(12n,50000n))),div(eps,Q(50n)));
pass("full derivative error",mul(eps,add(add(Q(1n,20000n),Q(1n,200000000n)),Q(1n,100000n))),eps);
pass("full directional Hessian",add(div(eps,Q(20n)),div(eps,Q(50n))),eps);
const reach=div(pow(sub(one,mul(Q(11n),eps)),2),add(Q(4n),mul(Q(2561n),eps)));
pass("perturbed reach",Q(1n,8n),reach);
const D=Q(51n,25n),held=sub(mul(tau,Q(4n,5n)),mul(Q(2n),delta));
pass("whole initial diameter",mul(Q(2n),add(add(one,Q(1n,100n)),mul(Q(2n),delta))),D);
equal("held support lower bound",held,Q(127n,1000n));
pass("held ratio",Q(3n,50n),div(held,D));
const grip=mul(Q(2n),sub(Q(3n,10n),div(pow(Q(3n,10n),3),Q(6n))));
pass("grip ratio",Q(1n,4n),div(grip,D));
pass("reach ratio",Q(3n,100n),div(Q(1n,8n),D));
return {kind:"exact BigInt rational gates only",count:rows.length,rows,geometry_arrays:false,pde_solver:false,terminal_execution:false};
})()
```
