# R643：保留真实均值高度的固定 E 联立系统与完整周期位置

2026-11-28，接
[R618](R618-fixed-metric-core-and-growing-post-response.md)及
[本次自然终态](../notes/2026-11-28-r618-centered-complete-state-natural-terminal.md)。
**状态：以下表示、周期位置恒等式及完整参数导数已证明；尚未取得新联立系统的根。**
固定目标仍为原 `86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`。
不扩大未经证明的旧单调根盒，不删近帽条件，不更换其连续 E。

## 1. 真正应保留的未知量与坐标病态

本次实际方向在 r=.22666666666666668 处有
W=9.386865694644854e-40、delta s=-7.92251682532487e-7，
原 lambda=s/W 盒将完整方向乘到 2.3696675946812992e-35。
实际同态 mean coefficient 约为 -7.06417e-24；背景消去后这些量仍被观察到。
因此只把 lambda 换一个名称、随后继续除同一个接近零的 mean coefficient，
并没有移除本次消元问题。

冻结完整旋转度量

\[
g_*=E(r)\,dr^2+r^2d\theta^2,
\qquad E=W^2+e_*.
\tag{1}
\]

写真实高度为

\[
Z(r,\theta)=h_*(r)+m(r)+f(r,\theta),\qquad h_*'=-W,
\tag{2}
\]

其中 f 是原同一 canonical 分拆的角场，m 是 **真实高度的均值修正**。
原 canonical512 与连续均值之间若有固定差额，仍按 R618(2)同时加减，
保持同一个 Z，不能只改其中一边。下面的局部公式不要求 f 的数值角平均
先舍入为零；其响应方向的正偶 Fourier 零均值仍可准确使用。

定义

\[
p=-W+m'+f_r,\quad q=f_\theta,\quad t=f_{\theta\theta},
\quad b=(r^2-q^2)^{1/2},\quad
u=(E-r^2p^2/b^2)^{1/2}>0,
\tag{3}
\]

u 是由高度与固定 E 决定的正平方根，不是额外自由变量。再置

\[
N=\frac rb+\frac{r^2pt}{b^3}>0,\quad a=N/u,\quad
C=Et+rp,\quad B=f_{r\theta}-q/r,\quad
M=r+pt-q^2/r,\quad\omega=\frac{r^2}{u^3b^3}.
\tag{4}
\]

保留 p_r=-W'+m''+f_{rr}，**不求除以**
\(c_0=\langle\omega C\rangle\) 的 m'' 隐式表达式。完整连接量直接是

\[
\boxed{D=Cp_r-E B^2-\tfrac12 E'M,
\qquad R=\omega D.}
\tag{5}
\]

它与原 R618 的 D 是准确同一量。事实上原分拆的 K_old 满足
K_old=C+WM、E'=2WW'+e_*'，代回原式即得 (5)。
式 (3)--(5) 中唯一的几何分母是正域的 r、b、u；没有 1/W、1/p 或 1/c0。
将 p 写成能量椭圆角

\[
p=(b\sqrt E/r)\sin\beta,\quad u=\sqrt E\cos\beta,
\quad-\pi/2<\beta<\pi/2
\tag{6}
\]

是等价的有限物理域描述；本表示仍用真实 m，因而自动保留
p_theta=q_r 的高度可积性，而不把各点 beta 当成任意独立变量。

## 2. 不除 mean coefficient 的六 jets 恒等式

令 angle brackets 表示整圈连续平均，Pi 表示周期零均值原函数：

\[
(\Pi h)_\theta=h-\langle h\rangle,
\qquad\langle\Pi h\rangle=0.
\tag{7}
\]

定义

\[
v=-pq/b,\quad
u_\theta=-\frac{r^2p f_{r\theta}}{u b^2}
           -\frac{r^2p^2q t}{u b^4},
\quad K=\frac{r^2pB}{u b^3}.
\tag{8}
\]

直接化简给

\[
b_r=\frac{r-qf_{r\theta}}b,\quad
v_\theta+u a=b_r,\quad
v a-u_\theta=bK,\quad
\boxed{a_r=K_\theta+R.}
\tag{9}
\]

最后一式可先用 N=r^2 M/b^3，将 a 与 K 写成
\(a=L M,K=L pB,L=r^2/(ub^3)\)，再求导。
由于 \(p_\theta=q_r=f_{r\theta}\)，M_r 中的 p t_r 与 (pB)_theta 中的
p p_{theta theta} 准确抵消；其余项正好是 (5)。因此右边虽然分开求导
会出现第三 jets，组合后的 R **仅需原完整六 jets 与真实 m',m''**。

令

\[
A=\langle a\rangle>0,\quad F=A-1,\quad G=\langle R\rangle.
\tag{10}
\]

由 (9) 和周期性，准确有 A_r=G。G 是 turning 方程的径向兼容量，
其计算不是调用旧 m'' 消元公式。F、G 在有限离散求解中都保留为真实行；
在连续方程 F 恒等于零时 G=F_r 自动为零。

## 3. 离解时也真正周期闭合的平面曲线

所有当前角场及其响应均为正偶模，故 p、b、u、a 为偶函数且有周期 pi，
K 为奇函数且有周期 pi。定义 normal angle 和 tangent frame

\[
\phi=\theta+\frac{\Pi a}{A},\qquad
\psi=\phi+\pi/2,\qquad
T=(\cos\psi,\sin\psi),\qquad JT=(-T_y,T_x).
\tag{11}
\]

这里 normal angle 的 phi(0)=0，与旧 Y_theta=R(-sin phi,cos phi) 规范一致，
没有误加 pi/2。因为

\[
\phi_\theta=a/A>0,\quad
\phi(\theta+\pi)=\phi(\theta)+\pi,
\tag{12}
\]

bT 是 pi 反周期函数，整圈平均准确为零。因此

\[
\boxed{Y=\Pi(bT),\qquad Y_\theta=bT}
\tag{13}
\]

在 **所有正域试值** 上都定义真正闭合、中心固定为零的平面曲线。
正转向与一次总转角给严格凸嵌入；这一步只证明每个水平截面，
并不由此宣称全部曲面已经嵌入或有规定 reach。

未满 turning 条件时必须使用 (11) 的 A，不能把原
psi=theta+pi/2+Pi(a-1) 的条件恒等式直接冒充新的真实曲线导数。
利用 (9)、K 的零均值、A_r=G，有

\[
\boxed{\psi_r=\frac{K+\Pi R}{A}-\frac{(\Pi a)G}{A^2}.}
\tag{14}
\]

于是实际连续位置导数是

\[
Y_r=\Pi\{b_rT+b\psi_rJT\}.
\tag{15}
\]

这已经覆盖周期相位、位置闭合和径向相位导数，未引入任何除 c0 的步骤。

### 可稳定计算的实际位置缺陷

置

\[
Q=\Pi R-(\Pi a)G/A,\qquad
\mathcal H=\frac{F}{A}(N T+u_\theta JT)+\frac bA QJT.
\tag{16}
\]

由 (9)、(11)--(15)，逐角求导并用所有向量的 pi 反周期性消掉积分常数，得到

\[
\boxed{Y_r=vT-uJT+\Pi\mathcal H,
\qquad S=\Pi\mathcal H/\sqrt E.}
\tag{17}
\]

特别地，(16) 避免先生成两个约为单位长度的向量再相减来求小 S。
在 F=G=0 时准确退回旧完整 S：
\(S=\Pi\{b(\Pi R)JT\}/\sqrt E\)。
离解时 (16) 中的两个 F 项与 G 项都必须保留。

对于真正的连续 X=(Y,Z)，由 Y_theta=bT 和 (17) 直接得

\[
\frac{|X_r|^2-E}{E}
 =2\,S\cdot(vT-uJT)/\sqrt E+|S|^2,
\quad
\frac{X_r\cdot X_\theta}{r\sqrt E}
 =\frac b r S\cdot T,
\quad |X_\theta|^2=r^2.
\tag{18}
\]

故联立 F=0、G=0、S=0 给原同一个 g_*，而非一个随试值改变的 E。
反过来，在这组正向、对称、固定中心的曲线规范下，正确的等距解具有 a 为其
真实转角导数，故 A=1、G=0 并满足 (17) 的零缺陷。
事实上连续 S=0 已通过 (9) 的 T 分量强制 a/A=a，从而 A=1；
额外 F、G 行保留标量兼容约束并服务有限离散求解，没有改变解集。

有限角 primitive、有限均值与实际连续函数仍有 alias、求积和舍入误差。
以上定理不宣称有限数组 (17) 已经自动等于实际 Y 的所有径向导数。
数值消费者须保存 F/G、输出角平均差和 Nyquist 观察，并继续消费同一位置的
实际双 stencil 与连续误差；不能用本恒等式跳过这些已有必要工作。

## 4. 原空间、均值端帽、硬核心与准确维数

当前旧固定 E 空间有

\[
1473=1129+224+96+23+1.
\tag{19}
\]

五项分别是原所有非mean响应、高 compact 模、真实 Gaussian tail、独立
j=4,6,...,48 核心 P0 lift 和 tau。H 与 amplitude 是冻结参考数据。
**旧空间没有独立 mean 坐标**；旧 s(r)、s_r(r) 都通过原 scalar elimination 得到。
固定 tau=1 后有 1472 条自由列；不能再把被冻结 H 算成 mean 自由列。

取本次原自然终态的真实 accepted z_star（SHA19519575...），令

\[
m_\star(r)=\int_{r_c}^r s_\star(v)\,dv.
\tag{20}
\]

这里 s_star 是该固定场的原连续同支定义，不是 pending 试值，也不是把数值
underflow 区改成零。此处准确嵌入命题以该连续种子在所论域上存在并有相应
正则性为前提；原有限节点通过不单独证明所有节点之间的分支存在。第1--3节
的联立位置定理适用于任意给定的真实 C2 均值函数，不依赖这一种子条件。
数值重建仍需保原 true-tail 积分与所有源误差。
使用固定 m_star 只在该种子的评价阶段调用原 mean 根；后续新 trial 与每条
参数方向都不再隐式求新的 m 或除 c0。

沿用 R618 的两个真实核心径向 lift A0、B0，满足

\[
(W A_0', (W A_0')')|_R=(1,0),\quad
(W B_0', (W B_0')')|_R=(0,1),\quad A_0(R)=B_0(R)=0.
\tag{21}
\]

它们都在真内尾前准确为零。对当前非mean z 的真实硬 tau1 核心 P，令

\[
zeta(P)=\tfrac12(e(P)-e_{*,R}),\qquad
zeta_1(P)=-\frac{2c+1}{R}\langle P_\theta^2\rangle
          -\tfrac12 e'_{*,R},\quad c=\frac\alpha{1+\alpha}.
\tag{22}
\]

(22) 是 R618(11)--(14) 在完整硬核心映射下的 mean 两迹；非线性 P1 仍保留
全部依赖至 2J 模，并未被均值函数代替。定义

\[
\boxed{m=m_\star+A_0\{zeta(P)-zeta(P_\star)\}
 +B_0\{zeta_1(P)-zeta_1(P_\star)\}
 +a_{\rm num}\sum_{k=1}^{94}c_k\Gamma_k.}
\tag{23}
\]

a_num=1e-5 仅是与旧高度列相同的参数数值单位，不是几何 amplitude 回退。
94 条自由 mean 径向函数具体为：

- 61 条原 bulk 径向函数 v_k，去掉其完整核心两迹；此处 P0[v_k]=0，
  P1[v_k]=d_k，所以 Gamma_k=v_k-B0 d_k。d_k 是原同 W、同 bulk 归一化
  的真实系数 k_core(alpha+2) core_B[k]/bulk_scale。
- 28 条原 compact quintic 径向函数；它们支撑在 r<=.65、核心两迹均为零。
- 4 条原真实 Gaussian 径向尾，含所有次数0,1,2,3；在整个
  (r_c,tail_right) 按准确函数定义，不截断为有限口的零延拓。
- 1 条固定平滑 plateau Gamma_94，r<=.50 时为零、r>=.65 时为1。
  它不改变核心两迹，但允许真实 m(R) 改变。

前 93 条在 R 的值为零；最后一条的两条径向迹为零。所有 Gamma 都在 cap
为无限阶零（compact/bulk 的支撑与 cap 还有正距离）；中段仍保留原 C4
quintic 正则性，不把它们误称跨全部内部结点 C-infinity。
(23) 在 z=z_star、c=0 时准确恢复同一个真实高度与六 jets。
有限实际种子评价的误差仍是原误差，不由这一函数恒等式消失。

因此新 J=48 空间具有

\[
\boxed{1472+94=1566}
\tag{24}
\]

条自由列。tau 仍硬等于1、原全部1472列保留。
两条核心 mean lift 是从属函数，不增两条自由列；不存在第二个任意均值常数。
cap 端 m(r_c)=0 及所有 jets 平坦保持被钉住的真开帽。

m(R) 没有被错误固定为零。它改变中央柱的共同高度中心及反射中心；
上帽仍由 (20)、(23) 钉住，中央柱长度不变。这是原固定 E 几何中的真实
连接自由度，不是重新加入全体竖直平移的规范。
球与跨片几何应在实际共同中心下计算，不能把一个未计算的 m(R) 直接省略。

## 5. 完整离解 Jacobian，不隐藏小除数

固定 E 后，每条参数方向的真实变化为

\[
\delta p=\delta m'+\delta f_r,\quad
\delta p_r=\delta m''+\delta f_{rr},\quad
\delta q=\delta f_\theta,\quad\delta t=\delta f_{\theta\theta}.
\tag{25}
\]

(23) 给 mean 方向；核心部分必须包含

\[
\delta zeta=\tfrac12\delta e(P),\quad
\delta e=-2\frac{\langle\delta P/u_R^3\rangle}{\langle u_R^{-3}\rangle},
\quad
\delta zeta_1=-2\frac{2c+1}{R}\langle P_\theta\delta P_\theta\rangle.
\tag{26}
\]

分母 mean(u_R^-3)>0 是核心严格单调 turning 根，和本次近帽 c0 是不同对象。

各点完整导数为

\[
\delta b=-q\delta q/b,
\quad\delta u=-\frac{r^2p}{u b^2}\delta p
 -\frac{r^2p^2q}{u b^4}\delta q,
\]
\[
\delta N=\frac{rq}{b^3}\delta q
 +\frac{r^2}{b^3}(t\delta p+p\delta t)
 +\frac{3r^2ptq}{b^5}\delta q,
\quad\delta a=\delta N/u-N\delta u/u^2,
\tag{27}
\]
\[
\delta C=E\delta t+r\delta p,\quad
\delta B=\delta f_{r\theta}-\delta q/r,\quad
\delta M=t\delta p+p\delta t-2q\delta q/r,
\]
\[
\boxed{\delta D=p_r\delta C+C\delta p_r-2EB\delta B-E'\delta M/2,
\quad\delta R=\omega\delta D-3R(\delta u/u+\delta b/b).}
\tag{28}
\]

(28) 的离解权重项不能丢掉。令
\(\delta A=\langle\delta a\rangle,\delta G=\langle\delta R\rangle\)，则

\[
\delta\psi=\frac{\Pi\delta a}{A}-\frac{(\Pi a)\delta A}{A^2},\quad
\delta T=JT\delta\psi,\quad\delta JT=-T\delta\psi,
\]
\[
\delta Q=\Pi\delta R-\frac GA\Pi\delta a
 -(\Pi a)\frac{\delta G}{A}
 +(\Pi a)\frac{G\delta A}{A^2}.
\tag{29}
\]

用 \(u_\theta=v a-bK\) 计算其方向可只用原六 jets：

\[
\delta v=-\frac{q\delta p+p\delta q}{b}+\frac{pq}{b^2}\delta b,
\]
\[
\delta K=\frac{r^2}{ub^3}(B\delta p+p\delta B)
          -K(\delta u/u+3\delta b/b),
\quad\delta u_\theta=a\delta v+v\delta a-K\delta b-b\delta K.
\tag{30}
\]

把 (27)--(30) 完整代入 (16)，包括
\(\delta(F/A)=\delta A/A^2\) 和 \(\delta(bQ/A)\)，给

\[
\delta S=\Pi\delta\mathcal H/\sqrt E,\quad
\delta Y=\Pi\{\delta b\,T+bJT\delta\psi\},\quad
\delta F=\delta A,\quad\delta G=\langle\delta R\rangle.
\tag{31}
\]

所有分母均是 r、b、u、A 和正核心根量。c0 只作为真实完整 Jacobian 中的
一个小系数出现，没有被删除，也没有被提前除掉。

若使用旧完整950工作径向点和256输出角点，原全部121600位置行仍保留；
每半径再加 F 与 rG 两条真实兼容行，合计123500行。
rG 与 F 都无量纲；固定正行单位只是求解数值单位，不授任何连续资格。
fine仍是原1728径向点与512角点、所有输出奇模和全部实际物理域检查。

## 6. 这条新输入的边界

这是对同一固定 g 的联立表示和真实周期位置构造。它消除的是在求解器外
提前用 W、c0 除掉 mean 的数值机制，不证明完整 Jacobian 可逆，也不保证当前
有限1566列已有所需根。近帽的真实退化、无限角带和函数空间问题仍需在
完整联立系统中解决，不能把坐标改善写成它们已经闭合。

后继必须从同一真实 accepted 种子执行完整新方程、全列解析 Jacobian、
全部位置与 F/G 行，并保原来源、必要种子重建及所有新费用。
当前在跑 R631 的新 R=.8 设计与本条仍是两个不同完整 E，不能互借接受状态。
