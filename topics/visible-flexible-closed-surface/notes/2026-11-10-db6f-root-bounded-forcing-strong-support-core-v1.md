# 有界 forcing 支撑函数核：同时有效的握持位移、刚体商位移与厚度

**状态：完整作者证明，待未参与者全文独审。** 2026-11-10 UTC。
作者 root / Astra-visible-flex-db6f0b0e。
本稿是新几何族，未把它冒充 R55 或 flat17 的一次同问题数值加密。
仍有两条边界，没有构造闭曲面、帽接合、PDE数值解或网格。

## 1. 准确命题与已审依赖

存在固定光滑材料环带 M、固定光滑度量 g 和联合 C∞ 的精确等距嵌入族
F_t:M→R³，t∈[0,1]，并存在逐点固定、有内部的闭材料片 H。
以完整初态 D=diam F_0(M) 计，本稿拟证明

$$
D<51/25,\qquad
\frac{\operatorname{diam}F_0(H)}D>\frac{197}{680}>\frac14,
\tag{1}
$$

$$
\frac{\delta_{\rm hold}}D>\frac{53}{204}>\frac14>\frac15,\qquad
\frac{\delta_{\rm E}}D>\frac7{136}>\frac1{20},
\tag{2}
$$

$$
\operatorname{reach}F_t(M)\ge\frac3{32},\qquad
\frac{\operatorname{reach}F_t(M)}D>\frac{25}{544}>\frac3{100}
\quad(0\le t\le1).
\tag{3}
$$

δ_hold 是整张像的 Hausdorff 距离，不作刚体对齐；
δ_E 对全部 E(3)，包括反射取商。结论(2)的第二式来自完整像直径的变化，
所以不预设允许刚体保持 H、坐标轴或材料标号。

几何参数明确为τ∈[0,9/10]，t=10τ/9；C²预算明确取ε=1/100000。
新领的正宽δ由两段统一存在寿命与一个统一低阶界最后选择，
尚无可执行的十进制数值。固定一次δ后，g、M及整个时间区间全程不变。

用到的已完整独审输入只有：

- [R50 非减Q的光滑平坦入口](../results/R50-increasing-q-smooth-flat-entry.md)，
  作者a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b，
  完整独审0fbb537133c97af06cf55ca3939f002f5cfb17ad。
- [R48 非增Q的光滑有限平坦领](../results/R48-monotone-flat-collar-smooth-data.md)，
  作者9daa8aba8a341855811d2f1c164bfb3ca7eab0bc，
  完整独审15b02049c367e344901fb13264a950f8ff5bf933。

R55 已审的支撑/扰动策略提供动机；本稿重新证明新 forcing、
可能不含原点的辅助凸体、全部新常数、实际初值应用及有效 δ_E。
不要求 C3，不读取主数值数据。

## 2. 完全指定的光滑 forcing

令

$$
E(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0,\end{cases}
\qquad
\sigma(x)=\frac{E(x)}{E(x)+E(1-x)}.
\tag{4}
$$

分母处处正；σ为C∞非减函数，x≤0时为0、x≥1时为1。
设

$$
g_*(s)=\sigma(20s-7)\,\sigma(15-10s).
\tag{5}
$$

于是0≤g_*≤1，支撑包含于[7/20,3/2]，在端点外有开零区；
g_*在[2/5,7/5]恒为1。各端无穷阶平坦。
先在[0,π]定义

$$
f(\phi)=g_*(\phi)-g_*(\pi-\phi),
\tag{6}
$$

再作奇延拓至[-π,0]，最后2π周期延拓至R。
由于3/2<π/2，两项的非零支撑不交，故

$$
|f|\le1,\qquad f(\pi-\phi)=-f(\phi),\qquad
\int_0^\pi f(s)\sin s\,ds=0.
\tag{7}
$$

f在0和π的两侧都有开零区，所以奇/周期拼接为实际C∞函数。
f奇且周期，总平均为0。

定义实轴上的确定积分

$$
\psi(\phi)=\int_0^\phi f(s)\sin(\phi-s)\,ds.
\tag{8}
$$

它是唯一满足ψ''+ψ=f、ψ(0)=ψ'(0)=0的光滑解。
奇性由ODE唯一性得到。由(7)，ψ(π)=0；奇性又给
ψ(-π)=0和ψ'(-π)=ψ'(π)。由于f周期，从±π相同的Cauchy数据出发，
ODE唯一性证明ψ为2π周期函数，全部jet一致。
因此ψ总平均为0，在|φ|≤7/20恒为0。

这里需要的周期不是数值闭合，也没有留下一级谐波的平移缺口。

## 3. 两个显式支持见证

定义

$$
I_*=\int_{7/20}^{3/2}g_*(s)\cos s\,ds.
\tag{9}
$$

整个积分区间在(0,π/2)，所以I_*>0。由g_*在[2/5,7/5]为1，

$$
I_*\ge\sin(7/5)-\sin(2/5)>\frac{59}{100}.
\tag{10}
$$

最后一式用交错Taylor界严格支付：在0<x≤3/2，

$$
\sin x\ge x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040},
\quad
\sin x\le x-\frac{x^3}{6}+\frac{x^5}{120}.
$$

分别代入x=7/5和x=2/5，所得有理差严格大于59/100；
附录逐项以BigInt检查。交错项绝对值单调下降，截断方向正确。
所用3<π<22/7可由内接正六边形及
∫_0^1 x^4(1-x)^4/(1+x²)dx=22/7−π>0得到。

在φ=π/2，第二项g_*(π−s)尚未进入积分区，因此

$$
\psi(\pi/2)=I_*.
\tag{11}
$$

反射换元给∫_0^π f(s)cos s ds=2I_*，故

$$
\psi(\pi)=0,\qquad \psi'(\pi)=-2I_*.
\tag{12}
$$

(11)用于整像握持位移，(12)用于刚体不变的直径增长。

## 4. 实际闭凸曲线与共同材料弧长

设τ∈[0,9/10]，

$$
h_\tau(\phi)=1+\tau\psi(\phi),\quad
\rho_\tau=h_\tau+h_\tau''=1+\tau f(\phi),\quad
\frac1{10}\le\rho_\tau\le\frac{19}{10}.
\tag{13}
$$

令e_r=(cosφ,sinφ)、e_φ=(-sinφ,cosφ)，定义

$$
\widehat\gamma_\tau(\phi)
=h_\tau e_r+h_\tau'e_\phi,\qquad
\widehat\gamma_\tau'=\rho_\tau e_\phi.
\tag{14}
$$

下面证明这确是整个闭严格凸曲线，不预设h或h−1/10相对原点为正。

对于任意C²周期函数q，令γ_q=q e_r+q'e_φ。
若q+q''≥0，则在任何|β−α|≤π的lift上，

$$
q(\beta)-\gamma_q(\alpha)\cdot e_r(\beta)
=\int_\alpha^\beta(q+q'')(s)\sin(\beta-s)\,ds\ge0.
\tag{15}
$$

β≥α时核非负；β≤α时积分方向和sin符号同时反转。
任意法向角对都可选这样的lift，所以每个γ_q(α)都属于
K_q=∩_β{x:x·e_r(β)≤q(β)}，并在α方向取等。
K_q非空；四个坐标轴半平面已给有界性，故K_q紧且凸。
其支持函数恰为q，因为每一方向已有实际等号点。
这里没有使用q>0，也没有假设原点属于K_q。

应用q=hτ，(13)使不同法向角的(15)严格正，
所以γ̂τ单射且每一方向的支持点唯一。
更完整地，对任意支持点x，使用β→α±的支持不等式可得
x·e_r(α)=hτ(α)、x·e_φ(α)=hτ'(α)；
因此该点必是γ̂τ(α)。凸体每个边界点有支持线，
其边界正是(14)。ρτ>0给光滑严格凸性。

定义共同材料角

$$
u_\tau(\phi)=\phi+\tau\left(\int_0^\phi\psi(s)\,ds+\psi'(\phi)\right).
\tag{16}
$$

uτ(0)=0、uτ'=ρτ>0；ψ平均为0和ψ'周期给
uτ(φ+2π)=uτ(φ)+2π。因此它是度数1的圆微分同胚，
其逆φτ(u)对τ,u联合C∞。令

$$
\gamma_\tau(u)=\widehat\gamma_\tau(\phi_\tau(u)).
\tag{17}
$$

则|γτ'|=1，总周长2π，曲率

$$
\kappa_\tau=1/\rho_\tau\in[10/19,10].
\tag{18}
$$

所有有限阶角向范数在紧τ区间统一有限；
这由固定光滑ψ和ρτ统一下界反复反函数微分得到。
在|u|≤3/10，ψ及其从0起的积分都为0，
所以u=φ、γτ(u)=(cos u,sin u)逐点不变。

## 5. 半径1/10的真实滚动球与全部边界法锥

取R=1/10、qτ=hτ−R。则qτ+qτ''=ρτ−R≥0。
上节(15)已证明K_q非空且支持函数就是q，
即使它不含原点或有退化方向也成立。
紧凸集的支持函数唯一确定集合，而Minkowski和的支持函数相加；
故

$$
K_{h_\tau}=K_{q_\tau}+\overline B_R.
\tag{19}
$$

在原曲线点p=γ̂τ(φ)，中心p−R e_r(φ)=γ_qτ(φ)属于K_qτ，
所以闭R球B(p−R e_r,R)实际包含在K_hτ。
另一边界点q不能位于该球内部。展开距离平方得到

$$
-e_r(\phi)\cdot(q-p)\le\frac{|q-p|^2}{2R},
\qquad e_r(\phi)\cdot(q-p)\le0.
\tag{20}
$$

考虑任何闭区间J上的参考柱面

$$
B_\tau(r,u)=(\gamma_\tau(u),r).
\tag{21}
$$

若向量v满足B在p处的全部可行一阶法锥条件，
其水平分量是外法向的实倍数；其竖直分量在内部为0，
在两端与任何可行Δr的乘积均非正。
依水平系数的正负分别使用(20)，可得全部点对

$$
v\cdot(B(q)-B(p))
\le\frac{|v|}{2R}|B(q)-B(p)|^2.
\tag{22}
$$

这包含上、下边界的全部单侧法锥。
取z的最近点p，v=z−B(p)自动满足这些一阶条件。
若|v|<R，则任意q≠p有

$$
|z-B(q)|^2-|z-B(p)|^2
\ge(1-|v|/R)|B(q)-B(p)|^2>0.
$$

紧性保证最近点存在，所以reach(Bτ)≥R。
这不是单靠局部曲率给全局reach。

## 6. 全局材料弦长及明确的C²稳定半径

取两法向角之间长度δφ≤π的短弧。
在中点切向上的投影与ρτ≥R给

$$
|\Delta\gamma|\ge2R\sin(\delta\phi/2)\ge(2R/\pi)\delta\phi.
$$

设du是最短材料角距离，所选法向短弧的材料长度至多(19/10)δφ，
故du≤(19/10)δφ，进而

$$
|\Delta\gamma|\ge\frac{2}{19\pi}d_u\ge\frac1{30}d_u.
\tag{23}
$$

由π<22/7，在du>0时最后一步严格；du=0时用弱号。
在区间×圆的最短材料lift中，ζ=(Δr,Δu)于是满足

$$
|\Delta B|\ge|\zeta|/30.
\tag{24}
$$

DB的两列正交单位，方向Hessian满足|D²B[z,z]|≤10|z|²。

**扰动引理。** 设F=B+E在同一材料域上，
‖DE‖op≤ε、|D²E[z,z]|≤ε|z|²，ε≤1、30ε<1。
则F是嵌入，且

$$
\operatorname{reach}F(M)\ge
R_\varepsilon=
\frac{(1-30\varepsilon)^2}{10+45950\varepsilon}.
\tag{25}
$$

证明：沿可行直线lift积分给|ΔE|≤ε|ζ|≤30ε|ΔB|，
故|ΔF|≥(1−30ε)|ΔB|，排除全部自交；DF满秩。
在固定p处令线性A把正交基(e_z,T,N_0=e_z×T)
映至(F_r,F_u,F_r×F_u)。叉积误差≤2ε+ε²≤3ε，
所以‖A−I‖op≤5ε。
G=F−AB在p的一阶导数为0，且

$$
|D²G[z,z]|\le(1+5\cdot10)\varepsilon|z|²=51\varepsilon|z|².
$$

A在此Taylor计算中固定。沿材料线段积分，

$$
|\Delta F-A\Delta B|
\le(51/2)\varepsilon|\zeta|²
\le22950\varepsilon|\Delta B|².
\tag{26}
$$

F的任何可行法锥向量v，经Aᵀ拉回成为B的同类法锥向量，
因为A DB(p)=DF(p)，包括全部单侧边界方向。
用(22)、|Aᵀv|≤(1+5ε)|v|及(26)得到

$$
v\cdot\Delta F\le
\frac{|v|}{2}(10+45950\varepsilon)|\Delta B|².
$$

再用弦长比较，得到半径(25)的全部法锥不等式。
与上一节相同的距离平方论证给唯一最近点和(25)。

以下固定

$$
\varepsilon=1/100000,\qquad
R_\varepsilon=\frac{99940009}{1045950000}>\frac3{32}.
\tag{27}
$$

附录检查这个严格有理比较。

## 7. 共同径向度量和非循环的两段寿命

令S(x)=σ(2x−1/2)，所以S=0于x≤1/4，
S=1于x≥3/4，中间非减且所有端点无穷阶平坦。
固定h0=1/100和q*=ε/100。
对待选δ>0，定义

$$
Q_\delta(r)=
\begin{cases}
0,&r\le0,\\
q_*S(r/\delta),&0\le r\le\delta,\\
q_*[1-S((r-\delta)/\delta)],&\delta\le r\le2\delta,\\
0,&r\ge2\delta.
\end{cases}
\tag{28}
$$

它是实际C∞剖面。令aδ由

$$
a''=Q_\delta/a,\qquad a(0)=1,\quad a'(0)=0
\tag{29}
$$

确定，负侧取a=1。Q在入口开零，故共同C∞。
a≥1、a''≤q*，所以在任何固定r≤1/2窗口，
a'≤q*r、a−1≤q*r²/2；系数a、a'、a''一致有界，不依δ高导数。

在r=0的实际柱面初值取L0=M0=0、C0=κτ(u)>0，
以及真实位置/标架

$$
F(0,u)=(\gamma_\tau(u),0),\quad
e_1=e_z,\quad e_2=T_\tau,\quad N=\nu_\tau=e_z\times T_\tau.
\tag{30}
$$

相对g=dr²+a²du²，Gauss–Codazzi原方程是

$$
L=(M²-Q)/C,\quad
M_r=L_u-\mu M,\quad
C_r=M_u+\mu C+\beta L,\qquad
\mu=a'/a,\quad\beta=aa'.
\tag{31}
$$

用X=M/C、Y=1/C。初值X0=0、Y0=ρτ∈[1/10,19/10]，
有统一全部角向范数。R50中的背景P精确为0，X0的H5门满足。
对上升后保持q*的剖面，R50给一个T_up>0，
独立于δ的高径向导数和τ。必要时缩小这个统一时间，使Y始终有统一正下界。

在真实r=δ交接处Q=q*>0。R50的E4界给Y的H4和√q* Z的H4，
X=q*Z于是也有统一H4界。这里没有在Q=0处除Q。
对所有先满足δ<min(1/2000,T_up/2)的候选，
交接数据处于同一个低阶有界集，Y有统一正下界。
因此R48给共同下降时间T_down>0，不依δ或τ；可预先取T_down≤1/4。

两定理给低阶界后，(31)的右端只含Q及一次角导数，不含Q'，
故存在一个统一K*≥1，使两段均有
|M_r|+|C_r|≤K*。所有系数仍在r≤1/2的窗口内。
至此才最终选一个固定

$$
0<\delta<
\min\{1/2000,\ T_{\rm up}/2,\ T_{\rm down}/2,\ \varepsilon/(200K_*)\}.
\tag{32}
$$

这先取得统一寿命和K*，后选δ，不以候选解反过来循环选其寿命。
积分给全τ及0≤r≤2δ：

$$
|M|\le\varepsilon/100,\quad
|C-C_0|\le\varepsilon/100,\quad
C>1/2,\quad C<11.
\tag{33}
$$

两段在r=δ附近的Q皆为常数q*，a亦由同一真实Cauchy数据确定；
原物理解唯一性给开重叠与全部jet相同。
全部高阶能量在同一低阶时间内控制，不按阶反复缩时。
选定δ后a,Q不随τ变，R50/R48的固定系数初值参数结论
给τ、r、u联合C∞。不对δ本身宣称参数定理。

## 8. 真实位置、共同度量、周期及有限平坦领

用(31)的实际解，从(30)解径向框架和位置：

$$
(e_1)_r=LN,\quad (e_2)_r=(M/a)N,\quad
N_r=-Le_1-(M/a)e_2,\quad F_r=e_1.
\tag{34}
$$

对应角系统为

$$
F_u=ae_2,\quad
(e_1)_u=a'e_2+MN,\quad
(e_2)_u=-a'e_1+(C/a)N,\quad
N_u=-Me_1-(C/a)e_2.
\tag{35}
$$

兼容条件恰是LC−M²=−aa''及(31)。
例如(e1)的混合导数中e2系数给Gauss，N系数给第一Codazzi；
e2的N系数给第二Codazzi。于是角方程误差满足齐次径向ODE，
在r=0真实数据使其为0，故(35)实际成立。
径向框架矩阵反对称，保持正交单位性，得到精确共同I=dr²+a²du²。

初始位置、标架和系数都是实际2π周期；
径向ODE唯一性使F本身周期，不只使II周期。
在入口Q=0、a=1的开段，M=0、C=C0是(31)的平稳解，
所以F=Bτ，与负侧柱面在开区完全相同。
在r≥7δ/4的开领，Q=0、a仿射，C>0使II为非零秩一。
中间Q严格正，故a'(2δ)>0和a(2δ)>1。

取共同材料域M=[−h0,2δ]×R/(2πZ)，负侧使用(21)。
它是连通环带，仍有两条边界；本文绝不把这个出口当作零II的平面帽。

## 9. 实际C²位置预算

由2δ<1/1000、q*=ε/100，

$$
a'<\varepsilon/100000,\qquad
a-1<\varepsilon/200000000.
\tag{36}
$$

(33)和Gauss式给

$$
|L|\le2\{(\varepsilon/100)^2+\varepsilon/100\}<\varepsilon/20.
\tag{37}
$$

由(34)，|N_r|<3ε/50，沿长度<1/1000积分得到

$$
|N-\nu_\tau|<3\varepsilon/50000,\quad
|e_1-e_z|<\varepsilon/20000,\quad
|e_2-T_\tau|<\varepsilon/100000.
\tag{38}
$$

于是E=F−Bτ的两列DE都小，列范数之和<ε。
真实二阶位置给

$$
E_{rr}=LN,\qquad E_{ru}=a'e_2+MN,\qquad
E_{uu}=-aa'e_1+(C-C_0)N+C_0(N-\nu_\tau).
\tag{39}
$$

用C0≤10，有

$$
|E_{rr}|<\varepsilon/20,\quad
|E_{ru}|<\varepsilon/50,
$$

$$
|E_{uu}|<
\varepsilon\left(2/100000+1/100+30/50000\right)
<\varepsilon/50.
\tag{40}
$$

对任意方向z，2|z_rz_u|≤z_r²+z_u²给
|D²E[z,z]|≤(1/20+1/50)ε|z|²<ε|z|²。
负侧E=0，接缝有真实开重叠，所以这是整张固定材料域上的C²门。
§6遂给每个τ的真实嵌入及全图、含全部边界的reach≥3/32。

## 10. 固定握持片及整个初态的直径

取

$$
H=[-3/400,-1/400]\times[-3/10,3/10]\subset M.
\tag{41}
$$

这是有二维内部的闭片；整个r区间在负侧，
而§4证明其材料角内的γτ逐点恒等于单位圆，所以Fτ|H=F0|H。

同一径向高度的角±3/10两点给

$$
\operatorname{diam}F_0(H)\ge2\sin(3/10)
>2(3/10-(3/10)^3/6)=591/1000.
\tag{42}
$$

在τ=0，r=0是单位圆。沿固定材料u的径向路径速度|Fr|=1，
所以完整图中每一点到该圆某点的距离最多h0+2δ。
因此包含负侧柱面和全部新增领的初态直径满足

$$
D\le2(1+h_0+2\delta)<1011/500<51/25.
\tag{43}
$$

(42)–(43)给H/D>197/680>1/4。
§9与(43)给全时reach/D>25/544>3/100。
没有用中心曲线直径或周长替代分母。

## 11. 有效握持下的完整像距离

在τ=9/10，取负侧r=−1/200、法向角φ=π/2的真实像点p。
其材料角由uτ(π/2)确定；Hausdorff见证只需一个真实像点。
由(11)和(14)，

$$
p_y=h_\tau(\pi/2)=1+\tau I_*>1+531/1000.
\tag{44}
$$

初态整个负侧柱面y≤1；正侧图点距相应单位圆点≤2δ，
所以完整初态像均满足y≤1+2δ<1+1/1000。
对每个初态像点q，

$$
|p-q|\ge p_y-q_y>53/100.
\tag{45}
$$

于是终态到初态的单向距离已给δ_hold>53/100，
结合(43)得δ_hold/D>53/204>1/4。
这是整个像的距离，不是材料轨迹长度。

## 12. 有效刚体商：用完整像的直径变化

仍取同一负侧r，φ=0和φ=π处的两个真实终态点。
由ψ(0)=ψ'(0)=0以及(12)，它们的水平位置精确为

$$
(1,0),\qquad (-1,2\tau I_*).
\tag{46}
$$

因此整个终态的直径D1满足

$$
D_1\ge\sqrt{4+(2\tau I_*)^2}
>\sqrt{4+(531/500)^2}>\frac94.
\tag{47}
$$

最后一个严格平方比较由附录精确核算。
对任意非空紧集K,L，选择K中两点的L中最近点并用三角不等式，
有diam K≤diam L+2d_H(K,L)；交换两者即得

$$
|\operatorname{diam}K-\operatorname{diam}L|\le2d_H(K,L).
\tag{48}
$$

任何A∈E(3)保持直径，包括反射；所以对所有A，

$$
d_H(AF_1(M),F_0(M))
\ge(D_1-D)/2>\frac12(9/4-51/25)=21/200.
\tag{49}
$$

其下确界也有同一个更强界：由于固定的D1>9/4、D<51/25，
数值(D1−D)/2本身严格大于21/200，且与A无关。
紧集间的最佳刚体确实可取到：任一有界Hausdorff代价列的平移有界，
O(3)紧，取子列并用Hausdorff连续性即可。
故按README的min定义，也有

$$
\delta_{\rm E}>21/200,\qquad
\delta_{\rm E}/D>7/136>1/20.
\tag{50}
$$

这里无需两边界长度识别、固定轴、固定握持片对齐或材料对应。
联合C∞族给Hausdorff连续性；刚体商距离由三角不等式也是连续的，
故在t∈[0,1]上的max存在。端点见证已足够证明(2)。

## 13. 已付范围与尚缺工作

(1)–(3)一旦全文独审核准，给真正的共同g精确环带族，
且同时达到README强位移比和目标厚度的数值范围。
但它仍有两条边界；正则帽、非平桥及闭曲面尚未构造。
有限flat出口的II非零，不能忽略真实位置、法向、完整II及共同材料匹配。

δ虽严格存在且固定一次，却尚非算出的有效十进制宽度。
本稿没有运行PDE、生成网格、核新的主数值候选或支付G5。
不能把R55和本稿不同ψ、不同τ/ε/g当作同一几何的两次加密；
也没有改变flat17的物理参数或继承其数值证书。

## 14. 冻结的有限有理检查源码

下列自包含V8表达式只检查文中有限有理比较。
它不采样曲线、PDE或reach，不代替上面的完整证明。
作者必须先冻结本稿并固定回读，再提取这个唯一代码围栏实际运行；
未参与者须从固定commit独立提取重跑并全文审证明。
执行时间、源码哈希和结果另记真实回执；本文不预填PASS。

```javascript
(() => {
  const abs=x=>x<0n?-x:x;
  const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>Q(-a[0],a[1]);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const pow=(a,k)=>{let z=Q(1);for(let j=0;j<k;j++)z=mul(z,a);return z;};
  const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
  const out=a=>a[0]+"/"+a[1];
  const rows=[];
  const gt=(name,a,b)=>{if(!(cmp(a,b)>0n))throw Error(name);rows.push({name,status:"PASS",left:out(a),right:out(b)});};
  const eq=(name,a,b)=>{if(cmp(a,b)!==0n)throw Error(name);rows.push({name,status:"PASS",left:out(a),right:out(b)});};
  const eps=Q(1,100000),tau=Q(9,10),R=Q(1,10),rmax=Q(19,10);
  const sx=Q(7,5),sy=Q(2,5);
  const low=sub(add(sub(sx,div(pow(sx,3),Q(6))),div(pow(sx,5),Q(120))),div(pow(sx,7),Q(5040)));
  const high=add(sub(sy,div(pow(sy,3),Q(6))),div(pow(sy,5),Q(120)));
  const ilow=sub(low,high);
  gt("plateau left",Q(2,5),Q(7,20));
  gt("plateau right",Q(3,2),Q(7,5));
  gt("Taylor integral lower",ilow,Q(59,100));
  eq("rho lower",sub(Q(1),tau),R);
  eq("rho upper",add(Q(1),tau),rmax);
  gt("material chord",div(Q(2),mul(Q(19),Q(22,7))),Q(1,30));
  gt("perturbation small",Q(1,30),eps);
  gt("normal cross column",mul(Q(3),eps),add(mul(Q(2),eps),pow(eps,2)));
  const reach=div(pow(sub(Q(1),mul(Q(30),eps)),2),add(Q(10),mul(Q(45950),eps)));
  eq("reach exact",reach,Q(99940009,1045950000));
  gt("reach absolute",reach,Q(3,32));
  gt("L budget",div(eps,Q(20)),mul(Q(2),add(pow(div(eps,Q(100)),2),div(eps,Q(100)))));
  gt("ru budget",Q(1,50),add(Q(1,100000),Q(1,100)));
  gt("uu budget",Q(1,50),add(add(Q(2,100000),Q(1,100)),Q(30,50000)));
  gt("directional Hessian",Q(1),add(Q(1,20),Q(1,50)));
  const H=mul(Q(2),sub(Q(3,10),div(pow(Q(3,10),3),Q(6))));
  eq("H chord",H,Q(591,1000));
  const Dloose=mul(Q(2),add(add(Q(1),Q(1,100)),Q(1,1000)));
  eq("whole initial diameter budget",Dloose,Q(1011,500));
  gt("diameter convenient bound",Q(51,25),Dloose);
  gt("H ratio",div(H,Q(51,25)),Q(1,4));
  eq("north increment",mul(tau,Q(59,100)),Q(531,1000));
  eq("held gap",sub(Q(531,1000),Q(1,1000)),Q(53,100));
  eq("held ratio",div(Q(53,100),Q(51,25)),Q(53,204));
  gt("held strong",Q(53,204),Q(1,4));
  gt("diameter witness",add(Q(4),pow(Q(531,500),2)),pow(Q(9,4),2));
  eq("rigid quotient gap",div(sub(Q(9,4),Q(51,25)),Q(2)),Q(21,200));
  eq("rigid quotient ratio",div(Q(21,200),Q(51,25)),Q(7,136));
  gt("rigid quotient strong",Q(7,136),Q(1,20));
  eq("reach normalized",div(Q(3,32),Q(51,25)),Q(25,544));
  gt("reach normalized target",Q(25,544),Q(3,100));
  return {check_count:rows.length,checks:rows};
})()
```
