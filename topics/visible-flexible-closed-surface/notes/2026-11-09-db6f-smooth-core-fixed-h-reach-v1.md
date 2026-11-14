# 实际光滑固定 H 圆柱核：鞍领、有限平坦端与全时间 reach/D>1/18

**状态：完整作者推导，待全文独审；非减 Q 定理的审查身份另列。**
2026-11-09，独立几何分工。
这是一个真实的有边环带族，材料域始终有两条边界。
它给精确共同度量、材料 C3、逐点固定的开握持片、全 E(3) 非全等，
以及全时间 reach/初态直径>1/18。
没有有效的0.05D像位移下界，也没有闭曲面。

新稿不修改旧正 C epicycle、R44/R45或水平核心解析稿。
不读主优化数组，不运行 PDE、BVP、tail、RK 或网格。
非解析局部 bump 不能偷偷使用原角解析 CK；
本稿明确使用新的非减 Q 定理，再接已审的非增 Q 定理。

## 1. 固定依赖

- 非减 Q 的完整作者证明：
  [a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b](https://github.com/Rogerhu12/math-research/blob/a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-increasing-q-smooth-flat-entry-v1.md)，
  blob f992cc801bc78e58c3ac174a5f6daaf2d22eff34，15,164 B；
  冻结本稿时，它仍待未参与者全文独审。
- 已完整独审的非增 Q 定理：
  [9daa8aba8a341855811d2f1c164bfb3ca7eab0bc](https://github.com/Rogerhu12/math-research/blob/9daa8aba8a341855811d2f1c164bfb3ca7eab0bc/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-monotone-flat-collar-smooth-data-v1.md)，
  独审 [15b02049c367e344901fb13264a950f8ff5bf933](https://github.com/Rogerhu12/math-research/blob/15b02049c367e344901fb13264a950f8ff5bf933/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-monotone-flat-collar-smooth-data-v1.md)。
- 本稿采用两个定理的准确正 C 范围。第一个定理的任何未付审查不由第二个代替。
  以下几何应用本身也须另外全文审查；其有理常数检查不替代存在论证。

主 PDE 的背景消去与混合能量在作者侧与 root 有讨论；
本文不把 root 的采纳读稿计为该部分未参与者独审。
本稿新的平面核、两扇区约束、边界非全等与 reach预算在下面完整推导。

## 2. 一个显式定义、精确闭合的局部平面核族

归一基础圆半径为1，omega=2pi/3。
在水平平面令

$$
\gamma_0(\theta)=(\cos\theta,\sin\theta,0),\quad
T_0=(-\sin\theta,\cos\theta,0),\quad
\nu_0=(-\cos\theta,-\sin\theta,0)=e_z\times T_0 .
\tag{1}
$$

第一扇区取不交区间
I_f=(omega/8,omega/4)、I_c=(3omega/8,5omega/8)。
对开区间 (a,c) 定义

$$
\mathcal B_{a,c}(\theta)=
\begin{cases}
\exp\{4/(c-a)^2-1/[(\theta-a)(c-\theta)]\},&a<\theta<c,\\
0,&\text{其余}.
\end{cases}
\tag{2}
$$

令 h=B_{I_f}、chi=B_{I_c}。
先在第一扇区定义
f_1=chi(nu_0)_x、f_2=chi(nu_0)_y，
再把 h,f_1,f_2分别作为标量以omega周期复制。
它们在扇区边界的邻域恒零，故复制后全为 C-infinity。

令

$$
f_{\tau,\alpha}=\tau h+\alpha_1f_1+\alpha_2f_2,\qquad
T_{\tau,\alpha}=\cos f_{\tau,\alpha}T_0+
                         \sin f_{\tau,\alpha}\nu_0 .
\tag{3}
$$

T始终是水平单位向量，并满足材料 C3。
固定首扇区的两个真实位移分量：

$$
\int_0^\omega T_{\tau,\alpha}\,d\theta
=\gamma_0(\omega)-\gamma_0(0).
\tag{4}
$$

其对 alpha的 Jacobian 是

$$
G_{ij}=\int_0^\omega \chi(\nu_0)_i(\nu_0)_j\,d\theta,
\qquad i,j\in\{x,y\}.
\tag{5}
$$

G严格正定：非零线性组合 a cos(theta)+b sin(theta)
不可能在 chi>0 的整个开弧上恒零。
因此有限维光滑隐函数定理给真实 alpha(tau)，alpha(0)=0，
使 (4) 对一个正参数邻域精确成立。
不要求它只在一阶成立，也没有用采样行列式替代可逆性。

定义

$$
T_\tau=T_{\tau,\alpha(\tau)},\qquad
\gamma_\tau(\theta)=\gamma_0(0)+\int_0^\theta T_\tau(x)\,dx .
\tag{6}
$$

(4) 与被积函数 C3给

$$
\gamma_\tau(\theta+\omega)=R_z(\omega)\gamma_\tau(\theta),
\qquad
\gamma_\tau(\theta+2\pi)=\gamma_\tau(\theta).
\tag{7}
$$

所以位置真实闭合，积分锚点始终是同一个gamma_0(0)。
由于 |T_tau|=1，theta本身就是共同单位速率材料坐标；
没有另一个待修复的弧长 gauge或随时间变化的周长。

把同一参数区间缩小，使

$$
\|f_\tau\|_\infty\le1/100,\qquad
\|f_\tau'\|_\infty\le1/10.
\tag{8}
$$

曲率为

$$
\kappa_\tau=1+f_\tau'\in[9/10,11/10],
\qquad \gamma_\tau''=\kappa_\tau\nu_\tau,\quad
\nu_\tau=e_z\times T_\tau .
\tag{9}
$$

每条曲线因此严格凸且单射。
也可直接由下面的全局弦长界验证单射；
凸性则由正曲率和总转角2pi给出：
对任意起点，以其内法向投影位移，
导数在切向转角0到pi时为正、pi到2pi时为负，
投影从0回到0而在中途严格为正，故每条切线都是严格支撑线。

取最短角差 Delta_theta<=pi。沿该角弧积分 (8) 得

$$
|\gamma_\tau(\theta)-\gamma_\tau(\phi)|
\ge(2/\pi-1/100)\Delta_\theta
>\frac35\Delta_\theta.
\tag{10}
$$

这里 2sin(Delta_theta/2)>=(2/pi)Delta_theta。
所用 pi<22/7 可由
int_0^1 x^4(1-x)^4/(1+x^2) dx=22/7-pi>0 直接证明。

每个非零tau的gamma_tau都不是圆：
在自由区控制函数恒零，有f_tau=tau h不恒零；
但在固定邻域f_tau=0。
若长度2pi的严格凸单位速率曲线为圆，则半径1、曲率恒为1，
迫使f_tau'=0且f_tau恒零，矛盾。
这对全部充分小非零tau成立，不仅是一阶非平凡性。

最后固定一个充分小的tau_1>0并令tau=t tau_1，t在[0,1]。
所有后续常数和径向选择都对这一个固定紧时间族统一，
不再随t改变tau范围。

## 3. 真正固定的圆柱材料 H

令 h_0=1/10，初始圆柱带为

$$
F_\tau^{\rm cyl}(r,\theta)=\gamma_\tau(\theta)+r e_z,
\qquad -h_0\le r\le0 .
\tag{11}
$$

它精确诱导 dr^2+dtheta^2。
初始框架与第二形式为

$$
e_1=e_z,\quad e_2=T_\tau,\quad N=\nu_\tau,\qquad
L=M=0,\quad C=\kappa_\tau>0.
\tag{12}
$$

在每个 jomega两侧的 |theta-jomega|<=omega/32 上，
T_tau=T_0。
由首扇区完整位移约束和首尾倒积分，gamma_tau=gamma_0
在这些整个邻域中成立，而非仅在三个端点成立。

定义闭材料集合

$$
H=\bigcup_{j=0}^2
\{(r,\theta):-3h_0/4\le r\le-h_0/4,\ 
                         |\theta-j\omega|\le\omega/32\}.
\tag{13}
$$

角区间按周期解释。H有非空内部，且
F_tau|H=F_0|H。
在 r=-h_0/2 的 theta=0与omega两点相距sqrt3，故

$$
\operatorname{diam}F_0(H)\ge\sqrt3>3/2.
\tag{14}
$$

本稿的固定握持区来自精确位置和共同单位速率材料theta，
不靠刚体对齐，也不把材料点滑动计为像变形。

## 4. 一个先升后降、实际固定的共同曲率剖面

取 E(x)=exp(-1/x)于x>0、E(x)=0于x<=0，定义固定非减光滑阶跃

$$
S(x)=\frac{E(x-1/4)}{E(x-1/4)+E(3/4-x)} .
\tag{15}
$$

S=0于x<=1/4，S=1于x>=3/4，0<=S<=1。
在中间区间，分子递增、另一项递减，故S'非负。

对待选delta>0，定义同一个径向函数

$$
Q_\delta(r)=
\begin{cases}
0,&r\le0,\\
S(r/\delta),&0\le r\le\delta,\\
1-S((r-\delta)/\delta),&\delta\le r\le2\delta,\\
0,&r\ge2\delta .
\end{cases}
\tag{16}
$$

它在拼点附近为常数，故全C-infinity；
上半程非减，下半程非增。
它在[3delta/4,5delta/4]恒为1，
在r<=delta/4和r>=7delta/4为0。

令

$$
a_\delta''=Q_\delta/a_\delta,\qquad
a_\delta(0)=1,\quad a_\delta'(0)=0 .
\tag{17}
$$

在负r部分取a=1。
在固定窗0<=r<=1/2内，标量ODE连续延拓且

$$
1\le a_\delta\le1+r^2/2<2,\qquad
0\le a_\delta'\le r,\qquad 0\le a_\delta''\le1 .
\tag{18}
$$

证明只用a''非负得a>=1，再积分a''<=1；
有界正解不能在此窗失效。
所以mu=a'/a、beta=aa'也有与delta无关的统一界。
对所有时间使用的共同度量就是

$$
g_\delta=dr^2+a_\delta(r)^2\,d\theta^2 .
\tag{19}
$$

## 5. 先统一两段寿命，再选择 delta

上升段使用 §1的非减Q定理。
为了不循环选择时间，先在固定窗把Q_up=S(r/delta)
延为恒1，并相应解其标量a方程。
它的所有低阶系数界仍由(18)控制，初值(12)不依delta。
X_0=M_0/C_0=0，Y_0=1/kappa_tau，
其所需低阶角范数对紧时间族统一有界。
故先得一个与delta无关的T_up>0。

在r=delta时Q_up=1；
非减定理的混合能量给实际X,Y的统一H4界和Y统一正下界。
这些界不依delta，所以可把所有可能的交接初值放入
已审非增Q定理的同一个有界数据族。
该定理给共同T_down>0，不依delta。
下降段使用(16)后半段和在r=delta已经得到的实际初值。
两段都在r=delta附近的Q=1开领内：
唯一性及同一a初值使其实际解在重叠上完全相同。

现在才取

$$
0<\delta<\min(1/200,T_{\rm up}/2,T_{\rm down}/2).
\tag{20}
$$

于是整个[0,2delta]已经位于两个定理的共同存在区间内。
实际第二形式C>0，且联合C-infinity依赖(r,theta,tau)。

两段的低阶角界和Y正下界给M,C的统一C1角界。
由于原方程

$$
M_r=((M^2-Q)/C)_\theta-\mu M,\qquad
C_r=M_\theta+\mu C+\beta(M^2-Q)/C
\tag{21}
$$

不含Q'，它们还给一个与delta无关的常数K_*，
使 |M_r|+|C_r|<=K_*。
再把同一个delta取到
2delta K_*<1/10，即得到整个两段上

$$
|M|\le1/10,\qquad 4/5\le C\le6/5 .
\tag{22}
$$

这次缩小不破坏已经统一的两段寿命。
它同时对全部时间有效；不是逐个tau选择不同delta。

上述选择后，delta、a_delta、完整材料域
M_delta=[-h_0,2delta]×S^1 和tau范围全部固定。
这是一个同一精确几何的存在性选择，没有把delta作为随后网格加密的参数。

## 6. 实际位置、周期、全 jet贴柱及有限平坦端

在r=0给(11)–(12)的实际位置和正交标架，解

$$
F_r=e_1,\quad(e_1)_r=LN,\quad
(e_2)_r=(M/a)N,\quad N_r=-Le_1-(M/a)e_2,
\qquad L=(M^2-Q)/C .
\tag{23}
$$

Gauss–Codazzi保证与角方程

$$
F_\theta=ae_2,\quad
(e_1)_\theta=a'e_2+MN,\quad
(e_2)_\theta=-a'e_1+(C/a)N,\quad
N_\theta=-Me_1-(C/a)e_2
\tag{24}
$$

的兼容。角误差满足齐次径向线性系统，初值为0。
因此(19)是实际诱导度量。
周期初值和周期系数使位置与标架真实周期；
(7)的C3也由同一个ODE唯一性保留。
没有留下可事后调整的平移monodromy或出口高度。

在r<=delta/4，Q=0、a=1，(12)是平稳的第二形式解。
唯一性和(23)遂给精确F=gamma_tau+r e_z。
所以与原负r圆柱是开重叠上的完全相等，全部Cartesian jet匹配。
H始终位于原圆柱内，故逐点固定。

在r>=7delta/4，Q=0，a为正斜率仿射函数。
因为Q在中间区间严格正，a'(2delta)>0且a(2delta)>1。
第二形式此时满足LC-M^2=0且C>=4/5，
故是非零秩一；终端并非平面端。
其锥角2pi a'(2delta)<2pi/100，仍需真正后续接合。

## 7. 全时间实际 Hessian 小于2

在正r部分，由(18)、(20)、(22)，

$$
0\le a'<1/100,\quad a<2,\quad |M|\le1/10,\quad C\le6/5.
\tag{25}
$$

因为0<=Q<=1、0<=M^2<=1/100，
|M^2-Q|<=1；结合C>=4/5，

$$
|L|\le5/4 .
\tag{26}
$$

实际二阶导数为

$$
F_{rr}=LN,\quad
F_{r\theta}=a'e_2+MN,\quad
F_{\theta\theta}=-aa'e_1+CN .
\tag{27}
$$

不能把这些绝对值粗加后仍声称Hessian<2。
对任意参数方向h=(h_r,h_theta)，法向系数是对称矩阵

$$
\mathcal S_{\rm coord}=\begin{pmatrix}L&M\\M&C\end{pmatrix}.
$$

其算子范数不超过
max(|L|,|C|)+|M|<=5/4+1/10=27/20。
切向系数为
2a'h_rh_theta e_2-aa'h_theta^2 e_1。
它的范数不超过
|a'|(h_r^2+(a+1)h_theta^2)
< (3/100)|h|^2。
因此

$$
|D^2F[h,h]|\le(27/20+3/100)|h|^2
=(69/50)|h|^2<2|h|^2 .
\tag{28}
$$

负r圆柱部分的Hessian范数最多11/10，
所以整个固定材料域、全部时间均可取方向二阶Taylor常数 H_*=2。
(28) 用实际正交框架的法向和切向分解，不依赖Q'的大小。

## 8. 全局空间弦长、嵌入及含边界的 reach

把共同参考图延为
B_tau(r,theta)=gamma_tau(theta)+r e_z，
在整个[-h_0,2delta]上定义。
由(10)，

$$
|B_\tau(p)-B_\tau(q)|
\ge(3/5)\sqrt{(\Delta r)^2+\Delta_\theta^2}.
\tag{29}
$$

在负r部分F=B。在正r部分，(23)及(26)给

$$
|F_r-e_z|\le(5/4)r\le(5/2)\delta.
$$

由F_{r theta}=a'e_2+MN和(25)，

$$
|F_\theta-\gamma_\tau'|
\le r(1/100+1/10)\le(11/50)\delta.
$$

所以一阶差的算子范数不超过(68/25)delta<17/1250<1/10。
沿两个材料点的可行最短角lift直线段积分，
由(29)得到整个域的实际空间弦长下界

$$
|F_\tau(p)-F_\tau(q)|
\ge\frac12\sqrt{(\Delta r)^2+\Delta_\theta^2}.
\tag{30}
$$

共同正度量给正则性，(30)给全局单射；
故全部时间都是真正嵌入。

为核reach，令z为任意空间点、F(p)为其一个最近点，
d=|z-F(p)|。若p在材料边界，仍可沿通向任意其他参数q的
可行最短角lift线段使用一侧极小条件：

$$
(z-F(p))\cdot DF(p)(q-p)\le0.
\tag{31}
$$

(28)的Taylor余项与(30)的平方给

$$
(z-F(p))\cdot(F(q)-F(p))
\le d\,\frac{2}{2}|q-p|^2
\le4d\,|F(q)-F(p)|^2.
$$

于是

$$
|z-F(q)|^2-|z-F(p)|^2
\ge(1-8d)|F(q)-F(p)|^2.
\tag{32}
$$

当d<1/8时，其他不同像点均严格更远。
紧性保证最近点存在，故

$$
\boxed{\ \operatorname{reach}F_\tau(M_\delta)\ge1/8
\quad\text{对全部 }t\in[0,1].\ }
\tag{33}
$$

这个证明包含有边图的全部近点法锥方向，
没有要求边界最近点的位移垂直整个切平面。
co-Lipschitz常数1/2在(32)中已经平方；
也没有套用无边闭曲面的reach定理。

## 9. 完整初态直径、固定H比例及全E(3)非全等

初态的gamma_0是单位圆。
径向速度恒为1，所以任一点到对应gamma_0(theta)的距离
不超过h_0+2delta。由(20)，

$$
D:=\operatorname{diam}F_0(M_\delta)
\le2(1+h_0+2\delta)<111/50<9/4.
\tag{34}
$$

结合(14)、(33)，

$$
\frac{\operatorname{diam}F_0(H)}D>2/3,\qquad
\frac{\operatorname{reach}F_t(M_\delta)}D>1/18>3/100
\quad\text{对全部 }t.
\tag{35}
$$

D是完整新图的初态直径。没有用环宽或中心曲线直径归一。
尺度整体乘b时，reach>=b/8、D<9b/4，比例不变。

还需对整个欧氏群排除刚体族。整个材料域有两个边界分量：
底边r=-h_0的长度为2pi，顶边r=2delta的长度为2pi a(2delta)>2pi。
任何空间全等限制为两张嵌入有边曲面的内在等距，
必须把边界分量映到边界分量，且保持其长度。
故它不能交换这两个分量，底边必须映到底边。

若某非零tau完整像与初态全等，其底边gamma_tau-h_0e_z
就必须与初态的单位圆全等。
这与§2已证gamma_tau非圆矛盾。
该论证不依赖刚体定向，包含全部反射。
对固定的两个紧像，若刚体商Hausdorff下确界为0，
逼近刚体的平移有界、正交部分紧，
子列极限会产生真实全等，仍矛盾。
因此每个非零tau给严格正delta_E，并有严格正的握持像Hausdorff变化。

没有由这一非全等论证得到有效delta_hold/D或delta_E/D下界。
特别是不能把gamma材料点的位移代作整张曲面的Hausdorff距离。

## 10. 已付与未付

在§1的新存在定理通过完整独审后，本稿将给一个实际C-infinity有边族：
同一固定g精确等距，全时间嵌入，逐点固定的H具有非空内部且尺寸>2D/3，
全E(3)下非平凡，并且全部时间reach/D>1/18。
角向位置闭合与末端有限平坦也都由真实方程支付。

它仍有两条边界，出口有非零秩一II和小锥角。
没有指定的R43接缝或封帽，不能宣布闭曲面。
参数tau_1、delta虽严格存在且一经选择全族固定，
本文未给其有效数值半径，也未给0.05D像幅度。
没有几何网格、PDE数值解、主flat17的G5或最终独立全流程运行。

文末纯有理源只核常数。
其执行与固定正文绑定另存小回执，不充作PDE求解或未参与者全文审查。

## 11. 冻结的纯有理检查源

以下 10 个门只核本文明确使用的常数。
正文冻结时不预报运行结果；实际固定回读后执行的时间、源哈希与结果另存小回执。
不存在PDE或几何数组的计算，不把原作者执行算作未参与者重跑。

```javascript
(() => {
 "use strict";
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;};
 const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");
  if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
 const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>add(a,Q(-b[0],b[1]));
 const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
 const lt=(a,b)=>a[0]*b[1]<b[0]*a[1],fmt=a=>a[0]+"/"+a[1],rows=[];
 const pass=(name,a,b)=>{if(!lt(a,b))throw Error(name);rows.push({name,left:fmt(a),right:fmt(b),result:"PASS"});};
 const delta=Q(1n,200n),aPrime=mul(Q(2n),delta);
 pass("core chord",Q(3n,5n),sub(Q(7n,11n),Q(1n,100n)));
 pass("a upper",add(Q(1n),div(mul(aPrime,aPrime),Q(2n))),Q(2n));
 pass("diagonal maximum",Q(6n,5n),Q(5n,4n));
 pass("normal plus tangent Hessian",add(Q(27n,20n),Q(3n,100n)),Q(2n));
 const derivativeError=mul(mul(Q(2n),delta),add(Q(5n,4n),add(Q(1n,100n),Q(1n,10n))));
 pass("full derivative error",derivativeError,Q(1n,10n));
 pass("remaining global chord",Q(1n,2n),sub(Q(3n,5n),derivativeError));
 pass("whole initial diameter",mul(Q(2n),add(Q(1n),add(Q(1n,10n),mul(Q(2n),delta)))),Q(9n,4n));
 pass("grip chord squared",mul(Q(3n,2n),Q(3n,2n)),Q(3n));
 pass("grip diameter ratio",Q(1n,5n),div(Q(3n,2n),Q(9n,4n)));
 pass("reach ratio",Q(3n,100n),div(Q(1n,8n),Q(9n,4n)));
 return {kind:"exact BigInt rational inequalities",count:rows.length,rows,
  geometry_arrays:false,pde_solver:false,terminal_execution:false};
})()
```
