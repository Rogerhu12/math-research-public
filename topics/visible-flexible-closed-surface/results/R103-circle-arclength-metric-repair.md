# R103：逐圈弧长归一保持完整像集，及固定目标 g 的全 E/F/G

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明；尚未用于任何新候选的数值通过声明。**
原 M15/W22 主源、参数和目标度量均不改。本稿不以“换图”二字宣称误差消失：
目标 g 始终按同一个物理材料坐标固定，改变的是近似嵌入与材料的对应。
它严格保留周长均值误差，并计算归一映射的径向变化所引入的全部交叉项。

## 1. 坐标和固定目标

先在物理材料角 u 中写实际 C² 图

$$
X:I\times\mathbb R/(2\pi\mathbb Z)\longrightarrow\mathbb R^3,
\qquad X_u\ne0.
\tag{1}
$$

I 为紧径向区间，不包含极点。固定目标为

$$
g=\zeta(s)^2\,ds^2+a(s)^2\,du^2,\qquad a,\zeta>0.
\tag{2}
$$

允许原保存的径向变量不是目标的单位弧长：zeta 必须取实际目标供应器所定义的径向系数，
不能把程序中某个名为 lambda 的量未经核对直接代入。为下述常规坐标求导，取
a 为 C²、zeta 为 C¹；这没有增加对曲面 X 的 C³ 要求。

记实际基本形式和角向速度为

$$
E=|X_s|^2,\qquad F=X_s\cdot X_u,\qquad G=|X_u|^2,
\qquad v=|X_u|,\qquad T=X_u/v,
$$

$$
q=\frac va=\sqrt{1+\Gamma},\qquad
\Gamma=\frac G{a^2}-1,\qquad
\tau=X_s\cdot T=\frac Fv.
\tag{3}
$$

这里 T 是单位切向，区别于 R82 中未归一的材料角切向。

## 2. 准确的逐圈归一及仅 C² 的证明

定义部分弧长、总周长和归一角

$$
\mathcal S(s,x)=\int_0^x v(s,t)\,dt,\qquad
\mathcal L(s)=\mathcal S(s,2\pi),\qquad
\ell(s)=\frac{\mathcal L(s)}{2\pi a(s)},
$$

$$
A(s,x)=\frac{2\pi\mathcal S(s,x)}{\mathcal L(s)},\qquad
\chi(s,\cdot)=A(s,\cdot)^{-1}.
\tag{4}
$$

周期延拓后，A、chi 都是 degree-one lift，且固定 0。置

$$
\widetilde X(s,u)=X(s,\chi(s,u)).
\tag{5}
$$

**命题 1。** A 和 chi 联合为 C²，且对每个 s 都是保向圆周微分同胚；
Phi(s,u)=(s,chi(s,u)) 是整个带的 C² 微分同胚。只需要 X 属于 C²。

**证明。** v 正且连续，紧区间给统一正下界；A_x=2pi v/L>0，周期和满射性显然。
需要解释 A 的二次 s 导数：不能直接假定 X_ssu 已存在。

对于光滑 X，先有

$$
\mathcal S_s=\int_0^x T\cdot X_{su}\,du.
$$

第二次求导后，把唯一的 X_ssu 项对 u 分部积分，得到

$$
\begin{aligned}
\mathcal S_{ss}(s,x)
={}&\int_0^x
\frac{|X_{su}|^2-(T\cdot X_{su})^2}{v}\,du\\
&+\bigl[T\cdot X_{ss}\bigr]_{u=0}^{u=x}
-\int_0^x T_u\cdot X_{ss}\,du,
\\
T_u={}&\frac{(I-TT^T)X_{uu}}v.
\end{aligned}
\tag{6}
$$

式 (6) 只含 X 的二 jet。对 C² 数据在紧带上作保持周期的光滑 C² 逼近；
正下界在逼近中保持。S、S_s 和 (6) 右边均一致收敛，
所以极限 S 的二次 s 导数正是 (6)，并且连续。
另外 S_x=v、S_xx=T·X_uu、S_sx=T·X_su 连续。
故 S 是 C²；L>0 给 A 是 C²，联合反函数定理给 chi 是 C²。证毕。

这一步适用于真实共享两 jet 的 C² 图。若输入 raw PP 只是逐 span 的多项式，
它只逐 span 适用；不能用这个命题删除保存系数的实际接点 jump。

## 3. 固定目标下的完整度量公式

下文把新点 (s,u) 对应的旧角记为 x=chi(s,u)，所有右边都在 (s,x) 求值。
定义准确的弧长径向缺口

$$
\mathcal C(s,x)=
\mathcal S_s(s,x)
-\frac{\mathcal L_s(s)}{\mathcal L(s)}\mathcal S(s,x).
\tag{7}
$$

对 A(s,chi)=u 求导，得到

$$
\chi_u=\frac{\mathcal L}{2\pi v}=\frac{\ell}{q},
\qquad
\chi_s=-\frac{\mathcal C}{v}.
\tag{8}
$$

所以

$$
\widetilde X_s=X_s-\mathcal C T,\qquad
\widetilde X_u=a\ell T.
\tag{9}
$$

令

$$
w=\frac{\tau-\mathcal C}{\zeta},\qquad
d=\frac{E-\tau^2}{\zeta^2}-1.
\tag{10}
$$

**命题 2。** 相对于不变目标 (2) 的正交框架，
新图的准确误差矩阵为

$$
\boxed{
g^{-1/2}(\widetilde X^*e-g)g^{-1/2}
=
\begin{pmatrix}
d+w^2&\ell w\\
\ell w&\ell^2-1
\end{pmatrix}.}
\tag{11}
$$

**证明。** 把 X_s 分解为 tau T 加垂直于 T 的向量。
式 (9) 只把其沿 T 的系数从 tau 改成 tau-C；垂直分量的平方是 E-tau²。
因此

$$
\widetilde E=E-\tau^2+(\tau-\mathcal C)^2,\qquad
\widetilde F=a\ell(\tau-\mathcal C),\qquad
\widetilde G=a^2\ell^2.
\tag{12}
$$

依次除以 zeta²、a zeta、a² 即得 (11)。证毕。

这精确消除了角向项中的所有非均值起伏，留下的是每圈实际周长的相对误差 ell²-1。
E、F 没有被省略；它们由同一个真实径向缺口 C 决定。
原图的径向法向速度 E-F²/G 也没有被改变。

可直接用于全域上界的一项推论是：若

$$
|d|\le d_*,\quad |w|\le w_*,\quad
|\ell^2-1|\le m_*,\quad 0<\ell\le\ell_*,
$$

则

$$
\|\text{式 (11)}\|_{op}
\le \max\{d_*+w_*^2,m_*\}+\ell_*w_*.
\tag{13}
$$

这是对角部分与非对角部分算子范数的三角不等式；
若实际区间相关性更好，可直接对 (11) 的两个特征值作包围。

全域检验不必先在每个新角反解 chi：
对固定 s，x=chi(s,u) 遍历同一完整圆周，所以 (11) 在旧变量 (s,x) 上取上确界即可。

### 3.1 任意保圈重参数化也不能消掉的两项

对任何保向 C¹ 变换 (s,u)→(s,chi(s,u))，只要 s 不变，
由链式法则准确地有

$$
\widetilde E-\frac{\widetilde F^2}{\widetilde G}
=E-\frac{F^2}{G}.
\tag{13a}
$$

所以 d 是这个重参数化类的点态不变量。任意正定 2×2 矩阵 H 的 Schur 补
$H_{11}-H_{12}^2/H_{22}=1/(H^{-1})_{11}$ 位于 H 的最小和最大特征值之间；
应用于目标归一后的实际 Gram 矩阵，得到其误差算子范数至少为 |d|。

总周长同样不变。若全圈目标归一误差至多 epsilon<1，
则角向长度密度在 a sqrt(1-epsilon) 与 a sqrt(1+epsilon) 之间。
积分给 |ell²-1|≤epsilon；若 epsilon≥1，下侧界自动成立，上侧界仍由同一积分得到。
因此任何这样的材料重排都满足

$$
\boxed{
\sup\|g^{-1/2}(X_{\rm new}^*e-g)g^{-1/2}\|_{op}
\ge
\max\left\{\sup|d|,\ \sup_s|\ell(s)^2-1|\right\}.}
\tag{13b}
$$

这不是只对本文某个选择的上界，而是整个保圈重排类的必要下界。
特别是不能用角向归一修复一个已经超容差的实际径向法向速度。
若本文的 w 恰为零，则 (11) 为对角矩阵，达到 (13b) 的下界；
一般 w 非零时不声称本文的重排已经最优。

## 4. 周长均值误差必须独立保留

由 (4) 准确地有 ell=<q>，平均是物理材料角 u 的平均。
一般并没有 ell=1；归一只能把角向误差变成常数。
若把目标 a 改为 a ell，当然会让该项变成零，但这是改目标 g，本稿不这样做。

一个可用于严格实际计算的均值估计如下。设 ||Gamma||∞≤epsilon<1，记

$$
\overline\Gamma=\langle\Gamma\rangle,\qquad
R=\frac12\left\langle
\frac{\Gamma^2}{(1+\sqrt{1+\Gamma})^2}
\right\rangle.
$$

恒等式 sqrt(1+x)=1+x/2-x²/[2(1+sqrt(1+x))²] 给

$$
\ell=1+\frac{\overline\Gamma}{2}-R,\qquad
0\le R\le
R_*:=\frac{\epsilon^2}{2(1+\sqrt{1-\epsilon})^2}.
\tag{14}
$$

从而

$$
|\ell^2-1|
\le|\overline\Gamma|+2R_*
+\left(\frac{|\overline\Gamma|}{2}+R_*\right)^2.
\tag{15}
$$

因此只有在真实物理角均值也小的时候，残留角误差才可能比原来的角振幅小得多。
不能把一个有限 FFT 的零频显示为零，或一个未加权的适应性角均值，替代这个量。

## 5. 与 R82 输运的完整连接：无需对误差多求一个角导数

为引用 [R82](R82-normalized-angular-metric-transport.md)，
改用目标的单位径向参数 $dr=\zeta\,ds$，材料角仍为 u。
假设所考察曲线处在 R82 正根域，取其准确未投影速度 V，并令

$$
e=\frac{X_s}{\zeta}-V,\qquad |V|=1,\qquad V\cdot T=0.
\tag{16}
$$

R82 的输运公式在这里为

$$
\frac1\zeta\Gamma_s
=\frac2{a^2}X_u\cdot e_u,
\tag{17}
$$

右边在仅 C² 时按 R82 的乘积弱导数解释。
定义只含连续量的标量

$$
Z=T_u\cdot e,\qquad
\tau_r=\frac{\tau}{\zeta}=T\cdot e.
\tag{18}
$$

**命题 3。** 准确地有

$$
\frac a\zeta q_s=\partial_u\tau_r-Z,\qquad
\frac a\zeta\ell_s=-\langle Z\rangle,
\tag{19}
$$

以及式 (10) 的全部交叉缺口为

$$
\boxed{
w(s,x)=\tau_r(s,0)+
\int_0^x\left[
Z(s,t)-\frac{\langle Z\rangle}{\ell(s)}q(s,t)
\right]dt.}
\tag{20}
$$

另外

$$
d=2V\cdot e+|e|^2-(T\cdot e)^2.
\tag{21}
$$

**证明。** 由 T_u=κ|X_u|nu 及 R82 的 V·nu=-(a_r/a)/κ，
有 T_u·V=-a_r q。对 v=a q 求径向导数：

$$
v_s=\partial_u(X_s\cdot T)-T_u\cdot X_s
=a_s q+\zeta(\partial_u\tau_r-Z).
$$

减去 a_s q 即得 (19) 第一个式子；对 u 求平均得第二个式子。
这一证明只用 X 的二 jet，tau_r 实为 C¹，所以不需对连续 e 单独求经典导数。

积分第一个式子并代入 (7)，利用
L_s/L=a_s/a+ell_s/ell，得到

$$
\frac{\mathcal C}{\zeta}
=\tau_r(x)-\tau_r(0)-\int_0^x Z\,dt
+\frac{\langle Z\rangle}{\ell}\int_0^x q\,dt.
$$

代 w=tau_r-C/zeta 得 (20)。
最后 X_s/zeta=V+e、V垂直T，展开 (10) 即得 (21)。证毕。

式 (20) 去掉了在 (17) 表面上出现的额外角导数：
新交叉项由曲线单位切向的变化 T_u 与真实速度缺口 e 的乘积及一个角原函数控制。
纯切向误差 e=fT 给 Z=0；弧长归一把它的非均值部分消掉，
只剩用于固定角原点的 tau_r(s,0)。
若有实际的镜面对称，使该原点处 X_s 与 T 正交，则该常数也为零。
这些话不是把非零法向投影误差一起消掉；式 (20)、(21) 保留了它。

特别地，若 e=0，则 ell 沿径向恒定、w=d=0，
新诱导度量恰为 zeta² ds²+a² ell(0)² du²。
只有当实际初始周长已经是 2pi a(0) 时，才由此得到准确原目标 g。
它说明一种纯材料对应误差可以被修正，不提供一个尚未求出的 e=0 闭图。

对非零 e，均值的累计变化也没有被隐藏：

$$
|\ell(s)-1|
\le|\ell(s_0)-1|
+\int_{s_0}^{s}\frac{\zeta(t)}{a(t)}
|\langle Z(t,\cdot)\rangle|\,dt
\quad(s\ge s_0).
\tag{21a}
$$

反向区间同样取积分绝对值。这正是 (19) 的积分，
既保留入口周长误差，也保留沿程产生的真实均值漂移。

## 6. 从 Gamma 的径向变化给 chi_s 的有效界

不必处在 R82 正根域也可直接从实际二 jet 计算这一节。
置

$$
B(s,x)=\int_0^x(q(s,t)-\ell(s))\,dt,\qquad
\sigma=q_s-\frac{\ell_s}{\ell}q.
\tag{22}
$$

则

$$
\mathcal C=a\int_0^x\sigma\,dt
=a\left(B_s-\frac{\ell_s}{\ell}B\right),\qquad
\chi_s=-\frac{\int_0^x\sigma\,dt}{q(s,x)},
\tag{23}
$$

其中 x=chi(s,u)，并且

$$
q_s=\frac{\Gamma_s}{2q},\qquad
\ell_s=\left\langle\frac{\Gamma_s}{2q}\right\rangle.
\tag{24}
$$

### 6.1 只用实际连续上界的估计

设 q≥m>0，且 q、Gamma_s 具有共同周期 2pi/k，k≥1 为整数；
k=1 总可使用。假设

$$
\left\|\frac{\Gamma_s}{\zeta}\right\|_\infty\le h.
$$

则

$$
\boxed{
\frac{|\mathcal C|}{\zeta}
\le\frac{\pi a}{km}h,\qquad
\frac{|\chi_s|}{\zeta}
\le\frac{\pi}{km^2}h.}
\tag{25}
$$

**证明。** sigma 在一个周期上的积分为零。
其以 0 为起点的原函数，绝对值不超过其一个周期 L¹ 范数的一半。
又

$$
\int_{\rm period}|\sigma|
\le\int_{\rm period}|q_s|
+\frac{|\ell_s|}{\ell}\int_{\rm period}q
\le2\int_{\rm period}|q_s|.
$$

这里使用 period 长度乘 |ell_s| 不超过该周期的 ∫|q_s|。
再用 (24) 给
integral_period |q_s|≤pi zeta h/(km)；
代入 (23) 即得 (25)。证毕。

所以原 Gamma 的小角振幅本身不足以保证径向交叉项小，必须控制实际材料导数 Gamma_s/zeta。
例如把圆柱写成

$$
X(s,u)=
\bigl(\cos\varphi(s,u),\sin\varphi(s,u),s\bigr),\qquad
\varphi=u+\frac{\epsilon}{k}\sin(\omega s)\sin(ku),
$$

其中 0<epsilon<1。角误差在所有 omega 下都至多 2epsilon+epsilon²，
但归一映射的径向速度可为 epsilon omega/k 量级。
这个例子仍是 C∞ 且其像就是同一圆柱；完整公式会精确消掉原有切向径向速度。
它仅说明不能用角幅度代替径向变化去估计 (25)。

### 6.2 保留角频率改善的原函数界

若 sigma 的完整 Fourier 系数满足

$$
J(\sigma)=\sum_{n\ne0}\frac{|\widehat\sigma_n|}{|n|}<\infty,
$$

则其零均值原函数的 sup 不超过 J，锚在 0 的原函数不超过 2J。
若 sigma 为偶函数，原函数为奇函数，锚定不再多付 2。
因此一般有

$$
|\mathcal C|\le2aJ(\sigma),\qquad
|\chi_s|\le\frac{2J(\sigma)}m,
\tag{26}
$$

偶对称时删去两个因子 2。这是直接逐项积分 Fourier 级数的证明。
可以对 (20) 中的零均值源同样使用该界。
“完整 Fourier 系数”包括未截尾；仅用采样 FFT 取若干项只能作数值诊断。

## 7. 保存的角图、径向平流和准确消去

实际保存角记为 psi，物理材料角为

$$
u=\Theta(s,\psi),\qquad
\rho=\Theta_\psi>0,\qquad
\nu=\Theta_s,\qquad b=\nu/\rho.
\tag{27}
$$

目标在该图中为

$$
g=\zeta^2ds^2+a^2(\rho\,d\psi+\nu\,ds)^2.
\tag{28}
$$

故 (17)、(25) 中的材料径向导数是

$$
\frac1\zeta D_s\Gamma
=\frac1\zeta(\partial_s-b\partial_\psi)\Gamma,
\tag{29}
$$

不能改为固定 psi 的导数。一般角变换在此图中的表示
Xi(s,psi)=Theta(s,·)^(-1)(chi(s,Theta(s,psi))) 满足

$$
\chi_u=\frac{\rho(s,\Xi)\Xi_\psi}{\rho(s,\psi)},\qquad
\chi_s=\nu(s,\Xi)+\rho(s,\Xi)\Xi_s-\chi_u\nu(s,\psi).
\tag{30}
$$

这是对 Theta(s,Xi)=chi(s,Theta(s,psi)) 求两个导数的直接结果，
完整保留了原 warp 的非对角项。

当前原 warp 满足 Theta(s,0)=0，下面给计算 (11) 的更短等价公式。
令 Y(s,psi)=X(s,Theta(s,psi))，记

$$
\widehat v=|Y_\psi|,\quad
\widehat T=Y_\psi/\widehat v,\quad
\widehat{\mathcal S}(s,\psi)=\int_0^\psi\widehat v(s,t)\,dt,\quad
\mathcal L=\widehat{\mathcal S}(s,2\pi),
$$

$$
\widehat{\mathcal C}
=\partial_s\widehat{\mathcal S}
-\frac{\mathcal L_s}{\mathcal L}\widehat{\mathcal S},\qquad
\widehat\tau=Y_s\cdot\widehat T.
\tag{31}
$$

实际积分中的

$$
\partial_s\widehat v=
\frac{Y_\psi\cdot Y_{s\psi}}{|Y_\psi|}
$$

只含保存图的二 jet。正确的物理量是

$$
\tau=\widehat\tau-b\widehat v,\qquad
\mathcal C=\widehat{\mathcal C}-b\widehat v.
\tag{32}
$$

第一式来自 D_sY=Y_s-bY_psi。
第二式由固定物理上限 u 时 psi_s=-b 的积分上限求导得到；
下限 psi=0 固定，因为 Theta(s,0)=0。
所以平流项恰好在差 tau-C 中相消，而不是事先忽略。

于是 (11) 可完全在原保存角中计算为

$$
w=\frac{\widehat\tau-\widehat{\mathcal C}}{\zeta},
\qquad
d=\frac{|Y_s|^2-\widehat\tau^2}{\zeta^2}-1,
\qquad
\ell=\frac1{2\pi a}\int_0^{2\pi}|Y_\psi|\,d\psi.
\tag{33}
$$

径向法向速度中 b 同样相消，因为从 Y_s 减去的是角切向向量。
这说明具体实现可使用原图的完整 Cartesian 二 jet 与目标 a、zeta，
不必先反解每个新角，也不必通过近似 PDE 的 mean-height 速度替代保存图的真实 Y_s。

式 (15) 的物理均值若在该角图中计算，须使用

$$
\overline\Gamma
=\frac1{2\pi}\int_0^{2\pi}\Gamma(s,\psi)\rho(s,\psi)\,d\psi.
\tag{34}
$$

这是必须保留的权重，普通等间距 psi 平均一般不同。

## 8. cuff 的完整 C² 恒等及固定帽

假设活动带在 cuff s=s_c 与一个旋转参考图

$$
X_{rot}(s,u)=(R(s)e_r(u),z(s)),\qquad R>0
$$

有完整 Cartesian 两 jet 相等；其材料角已是同一 u。
对参考图，S=R(s)u、L=2pi R(s)，所以 A(s,u)=u、chi(s,u)=u。
这里圆周重参数化的恒等性不需要预先假定 R=a；
若二者不相等，相应周长误差仍由 (11) 的 ell²-1 保留。

由 (4)、(6)，A 的所有总阶数不超过二的导数只依赖该圈 X 的完整两 jet。
因此在 cuff 上真实 A 与恒等映射具有同样两 jet，逆映射也满足

$$
\chi=u,\quad \chi_s=0,\quad\chi_u=1,\quad
\chi_{ss}=\chi_{su}=\chi_{uu}=0.
\tag{35}
$$

这只需在 cuff 本身匹配完整两 jet；不要求活动带内预先有一条开旋转领。
在帽上延拓 Phi 为恒等映射，便得到整个参数球面的 C² 微分同胚。
所有固定帽点保持原有材料标记，帽的诱导目标度量也完全不变。

若原图在中央由镜像组成，亦可在整个带的带符号径向坐标上直接定义 (4)；
命题 1 给穿过中央的 C² 性。镜像使 v、A、chi 关于径向反射相容，
不会制造中央的新接缝。

逐圈版本要作用于整个活动部分，包括 prefix、tail 与 collar，
不能在一个非圆的 prefix/tail cut 突然改回恒等。
共同的完整两 jet 与同一个物理角原点使 (4)、(6) 在各径向图的接缝上按链式法则相合。
若某局部角图带有角偏移，须先把积分原点运输到同一条全局材料射线 u=0；
独立地把每张局部图的零点都当成新原点，可能产生额外扭转，本文没有省略它。

## 9. 全时间映射及全部像集几何不变

设原闭族在活动部分使用 R17/R21 的物理材料相位

$$
X_\alpha(s,u)=R_\alpha X_0(s,u-\alpha),
$$

并以满足共同两 jet 的固定帽闭合。对归一后的基线定义新族

$$
\widetilde X_\alpha(s,u)
=R_\alpha\widetilde X_0(s,u-\alpha)
=R_\alpha X_0(s,\chi(s,u-\alpha))
\tag{36}
$$

且帽仍固定不动。这里刻意重建同一物理 u 相位；
一般不能把它写成旧整族右复合同一个与相位可交换的 Phi。

**命题 4。** 在 §§2、8 假设下，新族是 C² 拓扑连续的闭嵌入族，
当且仅当旧族具有相应的嵌入性；每个相位的完整像集合准确相同。
它具有同一固定帽 H，且 D、diam(H)、reach、held 和含反射的 delta_E 全都不变。
若 (11) 在基线的全域有相对于 g 的界 epsilon，则相同界覆盖全部相位。

**证明。** 对每个固定 s，chi(s,·) 是整个圆的双射，
故新旧活动部分的像都等于 R_alpha X_0(I×S¹)。
帽逐点相同，(35) 保证固定帽接合处的全两 jet；于是完整像相同。
参数映射也由带上的保向微分同胚及帽上的恒等组合，
所以闭性与嵌入性保持。像集性质和 H 的逐点固定立即给各几何量相同。

目标 (2) 在物理 u 平移下不变；(36) 的 pullback 是新基线 pullback 的相位平移。
因此误差算子在对应目标正交框架中共轭，基线的全域界覆盖所有相位。
空间旋转不改欧氏度量。紧域上 X0 的二阶导数一致连续，
故相位平移在 C² 范数中连续；帽固定及统一接合给整个闭族的 C² 连续性。证毕。

这个几何转移只使用同一实际图的像集相等，不挪用另一旧候选的几何证书。
目标 g 始终没有右复合 Phi：若同时这样变更目标，误差只会作坐标共轭，不能产生本稿的改善。

## 10. 只在入口使用时的固定 cutoff 版本

若暂时只可靠计算了入口 chi0(u)，也可取固定 C² cutoff c(s)∈[0,1]，
在入口邻域 c=1、圆领邻域 c=0，且在拼接端有相应零一二阶端迹，定义

$$
\chi(s,u)=u+c(s)\eta(u),\qquad\eta=\chi_0-id.
\tag{37}
$$

因为 chi_u=(1-c)+c chi0'>0，这仍是保向 C² 微分同胚。
令 p=1+c eta'、b0=c' eta；右边在旧点 (s,chi) 求值，则准确地有

$$
\widetilde E=E+2Fb_0+Gb_0^2,\qquad
\widetilde F=p(F+Gb_0),\qquad
\widetilde G=p^2G.
\tag{38}
$$

因此归一到固定目标后，令 e=E/zeta²-1、f=F/(a zeta)、
gamma=G/a²-1、beta=a b0/zeta，有

$$
\frac{\widetilde E}{\zeta^2}-1
=e+2f\beta+(1+\gamma)\beta^2,\qquad
\frac{\widetilde F}{a\zeta}=p[f+(1+\gamma)\beta],
$$

$$
\frac{\widetilde G}{a^2}-1=p^2(1+\gamma)-1.
\tag{39}
$$

尤其不能只估算 beta 小便忽略 cutoff 区的角向项。
在 c=1 的区域，入口精确归一给

$$
\widetilde\Gamma(s,u)
=\ell(0)^2-1+
\chi_0'(u)^2\bigl[
\Gamma(s,\chi_0(u))-\Gamma(0,\chi_0(u))
\bigr].
\tag{40}
$$

括号内由 R82 沿同一物理材料线的实际输运源积分给出；
若原保存图只是逐 span 定义，还必须加对应 jump。
在 cutoff 区 (40) 不成立，必须使用完整 (39)。
逐圈方案的优势是不用任意选择 c，也自动在真正平接的 cuff 上成为两 jet 恒等；
它的代价则是需要计算每圈真实弧长及径向变化。

## 11. 对下一实际候选的使用范围

第一真 inner 仍先用现有工具检查其真实入口，再对自身 Cartesian base 作连续 metric 检查。
若原图已经通过目标，不为这个变换增加生产步骤。
若实际瓶颈主要是角向非均值误差，可先在原图二 jet 上只读计算
ell²-1、d、w，再用 (11) 判断是否确有改善空间。

严格采用时，所需的是完整角积分及原函数的连续包围、同一目标的 a/zeta、
原图自己的全部 cuff 两 jet，以及该同一图的几何结论。
有限角采样或 FFT 可以定位，不能替代这些连续量。
若新图的周长均值或 (11) 的 E/F 仍超原容差，则此路线没有通过；
不因像集相同而放宽 G5，也不通过改变 a、物理尾层或 taper 来压低缺陷。

本稿尚未对任何新 inner 报告这些数值，未改变当前求解器或闭后端。
