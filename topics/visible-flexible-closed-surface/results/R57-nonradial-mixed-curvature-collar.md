# R57：实际非径向混合曲率短领、退化入口有限传播与全图厚度

**状态：已证明，完整未参与者全文独立审查通过。** 2026-11-10 UTC。
作者 independent_geometry_continued_2；独立新证明审查 root / Astra-visible-flex-db6f0b0e。

从R51实际固定H柱核出发，存在共同光滑非径向度量上的真实全圈环带族，
保旧H及材料C3，新领同时包含固定正K开片和活动负K开片。
整个初态D<9/4、H/D>2/3，全时间reach≥1/6、reach/D>2/27；
含边界近点与全部E(3)非全等均已证明。
退化入口的有限传播和实际位置/框架开重叠完整支付，不是形式第二形式拼接。

本结果仍有两条边界，没有帽中心、有效像幅度、完整帽BVP、闭面、PDE数值或G5。
C3只为此实例属性，不是README新门；不同新共同g不混作flat17的加密。

## 采用和来源

- 作者固定正文：
  notes/2026-11-10-db6f-nonradial-mixed-curvature-collar-v1.md，
  commit 4c436678284b17a5e14f8629ce706bab5a1425c0，
  blob 7714bd76ba9e67e9b4b9d4554d706b43f18eb02b，23797 UTF-8 B，
  SHA256 d509320eebbab4cf194729d7e128d4bda7ddf779a4f410bfdadc52b8d9c29f3a。
- [完整独立审查](https://github.com/Rogerhu12/math-research/blob/86904cea8a88bd190027da243a4cf077b9fee206/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-root-review-nonradial-mixed-curvature-collar.md)：
  commit 86904cea8a88bd190027da243a4cf077b9fee206，
  blob e5c797f3a6913093e81f2a548dd281689591e7e1，11022 UTF-8 B，
  SHA256 d83c55c86ae6461198285145ac18b4eeafe8bcc1a281ab0877d246a1aea2d8ff。
  root未参与新增局部能量、非径向构造或常数推导，完整接受§1–§10。
  root曾参与输入R50的一般理论讨论，故本次不冒称重认证R50；
  R50的未参与完整独审0fbb5371独立保留。
- 作者从固定1612B唯一JS围栏实际执行24项有理门，00:52:50 UTC全部通过，
  回执 baa1486edec1c004b7ad364e39d12f662045318e。
- root独立从固定全文提取同一源，于00:56:17 UTC实际V8完成24 PASS/0 FAIL，
  自有回执身份root-independent-nonradial-mixed-collar-rational-01记于上述完整审稿§11。
  源SHA256 f5e5fff2a864303be90c74aa48eb0c27cea59493c454fed529307d15431b4236。
- 0 PDE、BVP、矩阵、轨迹、曲面数组、网格或终端数学执行。
  有限常数运行不替代完整局部传播、位置和全几何证明。

下方逐字保留作者全部十节及附录；历史待审状态由本采用记录更新。

---

## 1. 固定输入与实际结论

### 1.1 已存在的柱核输入

使用下面两个固定版本：

- 光滑退化负曲率入口作者稿
  [a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b](https://github.com/Rogerhu12/math-research/blob/a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-increasing-q-smooth-flat-entry-v1.md)；
  完整独审
  [0fbb537133c97af06cf55ca3939f002f5cfb17ad](https://github.com/Rogerhu12/math-research/blob/0fbb537133c97af06cf55ca3939f002f5cfb17ad/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-increasing-q-smooth-flat-entry-v1.md)。
- 实际光滑固定 H 柱核作者稿
  [be7b380055c1906a1abacfc5682da0e372ef8579](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)；
  完整独审
  [5597dffd479f6ca0c80f3cba871862a319af20e9](https://github.com/Rogerhu12/math-research/blob/5597dffd479f6ca0c80f3cba871862a319af20e9/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-smooth-core-fixed-h-reach-v1.md)。

第二个来源已经给出真实的、同一材料弧长 u 属于 R/(2pi Z) 下的平面凸曲线族
gamma_tau。把其参数限制在一个固定的、非零紧区间中，包含 tau=0。可直接使用：

$$
\begin{gathered}
\gamma_0(u)=(\cos u,\sin u,0),\qquad
|\gamma_\tau'(u)|=1,\qquad
\frac9{10}\le\kappa_\tau(u)\le\frac{11}{10},\\
|\gamma_\tau(u)-\gamma_\tau(v)|\ge
\frac35\,|\Delta u|,\qquad |\Delta u|\le\pi .
\end{gathered}
\tag{1}
$$

令 omega=2pi/3、eta=omega/32=pi/48。
在每个材料角区 |u-j omega|<=eta，j=0,1,2，上述曲线的
**位置、材料参数及全部角导数**等于 gamma_0。曲线具有材料 C3 对称；
每个非零 tau 的 gamma_tau 不是圆。该来源的闭合约束和 IFT 已经完整支付，
这里不重新把一个尚未闭合的平面曲线当输入。

原柱核为

$$
G_\tau(r,u)=\gamma_\tau(u)+r e_z,\qquad -\frac1{10}\le r\le0 .
\tag{2}
$$

固定握持区域取原来源中的

$$
H=\bigcup_{j=0}^2
 \left\{|u-j\omega|\le\eta,\quad
 -\frac3{40}\le r\le-\frac1{40}\right\}.
\tag{3}
$$

它有材料内部，且各时间逐点相同。取相同 r 上的三个中心角点即得
diam F_tau(H)>=sqrt(3)>3/2。

### 1.2 本稿支付的实际输出

存在一个固定 T>0 和一个以 (r,u) 为所有时间共同材料坐标的族

$$
\widetilde F_\tau:
\left[-\frac1{10},T\right]\times S^1\longrightarrow\mathbb R^3
\tag{4}
$$

满足：

1. 整族 C-infinity，逐点保留 (2)、(3)；度量与 tau 无关，保持材料 C3。
2. 位置图真实全圈闭合；新领含三片固定的正 K 开区域，并含负 K 开区域。
3. 整个有边环带在每个时间嵌入；下界
   reach >= 1/6 对整个像、包括两条边界的最近点成立。
4. 对整个初态像的直径 D，有 D<9/4，
   diam H/D>2/3，reach/D>2/27>0.03。
5. 每个非零 tau 的整个像与 tau=0 的像在全部 E(3) 下不全等。

这里只有两条边界；没有有效的 0.05D 幅度证书，没有闭合帽、G5、网格或数值 PDE。
正 K 片固定不变，形变仍由原来的非圆核心及其真实负 K 延拓承担。
选任一允许的 tau_* 非零并令 tau=t tau_*，即可得到 t 属于 [0,1] 的整族。

## 2. 一次固定的径向负 K 参考领

取 q_star=1/100。固定一个光滑非减阶跃 S，满足

$$
0\le S\le1,\qquad S(x)=0\ (x\le1/4),\qquad
S(x)=1\ (x\ge3/4).
\tag{5}
$$

例如用标准函数 exp(-1/x) 在 (0,1) 上归一成阶跃，再线性换元即可。
对尚待选择的 delta>0 设

$$
Q_\delta(r)=q_{\rm star}S(r/\delta),\qquad
a''=\frac{Q_\delta}{a},\quad a(0)=1,\quad a'(0)=0.
\tag{6}
$$

这是一个实际标量常微分方程。对 0<=r<=1/100，

$$
1\le a,\qquad 0\le a'\le q_{\rm star}r,\qquad
0\le w:=a-1\le\frac{q_{\rm star}}2 r^2,\qquad
0\le a''\le q_{\rm star}.
\tag{7}
$$

定义

$$
b(r)=\sqrt{1-a'(r)^2},\qquad
z(r)=\int_0^r b(s)\,ds,\qquad
F_{\rm rev}(r,u)=a(r)e_r(u)+z(r)e_z .
\tag{8}
$$

这里 b 是竖直速度，不是旧 ruled 环带的尺度参数。
(7) 保证 b>0，且 (8) 的度量为 dr^2+a^2 du^2。
使用 e_1=F_r、e_2=F_u/a、N=e_1 cross e_2 的定向，

$$
L_{\rm rev}=-\frac{a''}{b},\qquad
M_{\rm rev}=0,\qquad C_{\rm rev}=a b>0,\qquad
K_{\rm rev}=-\frac{Q_\delta}{a^2}.
\tag{9}
$$

R50 在这个实际 a 上，从 (2) 的位置与框架、M(0)=0、
C(0,u)=kappa_tau(u)>0 出发，给出真实周期的负 K 领
F_tau^hyp，具有共同 dr^2+a^2 du^2。
下面所有缩小时间都先使用 R50 对 delta 的统一寿命，
不借 a''' 或 Q_delta' 的上界决定寿命。

具体地，可以先确定一个正 T_0，与 delta 的高径向导数无关，
使所有这些族、以及第3节的正则化解，在 0<=r<=T_0 上存在，并有：

$$
|M_\tau|\le\frac1{10},\qquad
\frac45\le C_\tau\le\frac65 .
\tag{10}
$$

原因不是连续依赖一句话：R50 的混合角 Sobolev 能量对 Q_delta、
mu=a'/a、beta=aa' 的低上界统一；其实际 X=M/C、Y=1/C
方程没有 Q_delta'/Q_delta 项，故 X_r、Y_r 的低角范数有统一上界。
由初值 M=0、C=kappa_tau 及 (1) 再统一缩小 T_0，即得 (10)。
同理可使正则化解满足第3节的 (13)。数据 tau 在固定紧区间中，故这些选择
同时适用于所有时间。

r<=delta/4 时，a=1、Q=0，实际图恰为原柱图的开延长。
这是与旧柱核的开重叠，因而所有 jet 都接合，而不只是两 jet 相等。

## 3. 退化入口的局部有限传播

本节给真正需要的局部结论；不把全圆周唯一性直接改称有限传播。

### 3.1 正则化系统及统一速度

记 mu=a'/a、beta=aa'。在 R50 的正则化中取

$$
q=Q_\delta+\epsilon,\qquad 0<\epsilon\le\frac1{100},\qquad
\sigma=\frac{Q_\delta'}q .
$$

由于这里 X(0)=0，其标量背景 P 恒为零，故 X=qZ、Z(0)=0。
R50 的精确正则化系统化为

$$
\begin{aligned}
Z_r={}&qZ Z_u-Y Y_u-\sigma Z
       -2\mu Z-\beta q^2 Z^3+\beta q ZY^2,\\
Y_r={}&qZ Y_u-qY Z_u-\mu Y-\beta q^2 YZ^2+\beta qY^3 .
\end{aligned}
\tag{11}
$$

它只是实际 X,Y 方程的近似系统；不声称 q=Q+epsilon
与同一个 a 满足 Gauss 几何关系。

对每个固定角阶，R50 在同一时间上有统一的全局角 Sobolev 上界。
需要未加权的 Z 的第 k 阶上界时，使用其第 k+1 阶混合能量，
不是从 q||Z||_{H^k}^2 除以趋零的 q。
实际变量 X=qZ 的方程中 sigma 精确抵消，Y 的方程也没有 sigma。
因此统一缩短 T_0 后可保证

$$
|X_\epsilon|\le\frac14,\qquad
0<Y_\epsilon\le2 .
\tag{12}
$$

又 q<=1/50<1/16，所以对每个正则化解

$$
|qZ|+\sqrt q\,Y\le\frac14+\frac14\cdot2
=\frac34<1 .
\tag{13}
$$

这些控制只用 Q 的低上界和角数据，未用 Q' 的大小。

### 3.2 移动区间上的差能量

取两个 (11) 的光滑解，记差为 zeta=Z_1-Z_2、y=Y_1-Y_2。
它们有相同的 q,mu,beta，且两个初始曲率在某开角区
I=(u_-,u_+) 完全相同。
最高角导数的差系统为

$$
\begin{aligned}
\zeta_r&=A\zeta_u-Y_1 y_u-\sigma\zeta
              +\text{低阶差项},\\
y_r&=A y_u-qY_1\zeta_u+\text{低阶差项},
\qquad A=qZ_1 .
\end{aligned}
\tag{14}
$$

例如其余运输差为 q zeta (Z_2)_u-y(Y_2)_u 和
q zeta (Y_2)_u-qy(Z_2)_u。零阶多项式由 (11) 相减得到。
在第二行，所有含最高阶 zeta 的这类系数均带 q；
在第一行，其最高阶 y 项在能量中有外面的 q 权。
这是下面估计不产生 1/q 的原因。

令 I_r=(u_-+r,u_+-r)，并取一个固定整数 s>=4：

$$
E_s(r)=\sum_{k=0}^s\int_{I_r}
       \left(q|\partial_u^k\zeta|^2+|\partial_u^k y|^2\right)du
       +\sum_{k=0}^{s-1}\int_{I_r}|\partial_u^k\zeta|^2du .
\tag{15}
$$

对每个配对的最高阶 (zeta_k,y_k)，主通量为

$$
\mathcal F_k
=A(q\zeta_k^2+y_k^2)-2qY_1\zeta_k y_k .
\tag{16}
$$

在变量 (sqrt(q) zeta_k,y_k) 中，这个二次型的矩阵为

$$
\begin{pmatrix}A&-\sqrt q Y_1\\-\sqrt q Y_1&A\end{pmatrix}.
$$

由 (13)，|mathcal F_k|<=3/4 (q zeta_k^2+y_k^2)。
未加权低阶 zeta 能量的运输通量是 A zeta_k^2，也由 (13) 控制。
I_r 的两个端点各以速度1内缩，给负的端点总密度。
因此所有端点主通量与移动端点项之和非正。

这里有两个不能略去的内部项：

- 对加权 zeta_k^2，权重导数与 -sigma zeta_k 合起来是
  (q'-2q sigma)zeta_k^2=-Q_delta' zeta_k^2<=0；
  未加权低阶另有 -2sigma zeta_k^2<=0。
- 未加权第 k<=s-1 阶 zeta 方程中的 -Y_1 partial_u^{k+1} y
  不再分部积分，而在区间内直接以 Cauchy 不等式估计。
  k+1<=s，所以它由 (15) 的 y 的 H^s 范数控制。

其余角交换子、系数导数和 (14) 的低阶差项，使用统一的高一至两阶角
上界及一维乘积估计，全部被 C_s E_s 控制。
例如加权最高阶中的 q zeta_k y_k 可写成
sqrt(q)(sqrt(q) zeta_k)y_k；第二行中的 q zeta_k y_k 同理。
不需要把未加权的最高阶 zeta_k 由加权项单独控制。
低阶 zeta 部分直接使用 (15) 的 H^{s-1} 项。

因此得到与 epsilon 及 Q_delta' 大小无关的局部估计

$$
E_s'(r)\le C_s E_s(r).
\tag{17}
$$

初始 Z_1=Z_2=0，且 Y_1=Y_2 在 I 中连同全部角导数相同，
所以 E_s(0)=0。(17) 给两个正则化解在 I_r 中逐点相同。

R50 的实际 X_epsilon,Y_epsilon 极限在任意有限角阶中连续，
故物理解也在相同的锥域

$$
u\in I_r,\qquad 0\le r<T_0
\tag{18}
$$

完全相同。这里有限传播指两个已存在解在初始相同扇区的内缩锥中相同，
没有用数值有限模板代替这个结论。对每个固定 epsilon，先取 R50 的全局
Galerkin 极限，得到 (11) 的真实光滑解，才在移动区间上作 (15) 的估计；
不对带全局 Fourier 投影的有限系统声称局部支撑性质。最后再令 epsilon 趋零。

### 3.3 从系数相同到真实位置相同

将第二个解取为 (8) 的旋转参考。原曲线在
I_j=(j omega-eta,j omega+eta) 上连实际位置与单位切向都等于圆。
由 (18)，在

$$
|u-j\omega|<\eta-r
\tag{19}
$$

内，实际 L,M,C 与参考完全相同。框架的径向方程是

$$
(e_1)_r=L N,\qquad
(e_2)_r=(M/a)N,\qquad
N_r=-L e_1-(M/a)e_2,\qquad F_r=e_1 .
\tag{20}
$$

固定一个满足 (19) 的 (r,u)，其整条径向线 0<=s<=r 仍满足 (19)。
(20) 的两个初始位置和框架也相同，故常微分方程唯一性给

$$
F_\tau^{\rm hyp}(r,u)=F_{\rm rev}(r,u)
\quad\text{在 (19) 的整个开域内}.
\tag{21}
$$

积分常数在 r=0 的原材料位置处固定；没有事后平移单独一片。
这也给全部框架与全部 jet 的开重叠。

## 4. 固定正曲率参考片与全圈实际公式

取一个 C-infinity 偶函数 B_0(x)，满足 0<=B_0<=1，
B_0=1 当 |x|<=1/2，B_0=0 当 |x|>=1。
可由 (5) 的阶跃得到。定义周期 chi，使每个扇区内

$$
\chi(u)=1-2B_0\left(\frac{2(u-j\omega)}{\eta}\right)
\quad\text{当 }|u-j\omega|<\eta/2,
\tag{22}
$$

其余角度 chi=1。三个支撑互不相交，且在端点全 jet 为常值。
于是 chi 以 omega 为周期，-1<=chi<=1，

$$
\chi=-1\text{ 在 }|u-j\omega|\le\eta/4,\qquad
\chi=1\text{ 在全部支撑外}.
$$

记 K_1=||chi'||_infty、K_2=||chi''||_infty。
它们是一次固定的有限常数，不随 tau、T 或 delta 改变。

先按第2、3节选定统一 T_0。再选择一次正 T，满足

$$
\begin{gathered}
T<\min(T_0,\,1/100,\,\eta/4),\\
T(K_1+2)\le1,\qquad
T^2(K_2+2K_1+2)\le1,
\end{gathered}
\tag{23}
$$

并固定 delta=T/2。这些选择没有循环：
T_0 先于 delta，随后 (23) 只涉及固定角 cutoff 和低阶常数。
于是 Q_delta 在 r>=3T/8 时等于 q_star，w(T)>0。

在固定扇区中先写一张真实参考曲面

$$
F_*(r,u)=R(r,u)e_r(u)+z(r)e_z,\qquad
R(r,u)=1+\chi(u)w(r).
\tag{24}
$$

整个新族的实际位置公式为

$$
\boxed{\quad
\widetilde F_\tau(r,u)
=F_\tau^{\rm hyp}(r,u)+(\chi(u)-1)w(r)e_r(u),
\qquad 0\le r\le T.
\quad}
\tag{25}
$$

r<=0 则保持 (2)。

(25) 不是一个不经核验的法向插值：
在 chi-1 的全部支撑及其开邻域，由 T<eta/4 和 (21)，
F_tau^hyp=F_rev，所以 (25) **恰好等于实际固定图 (24)**。
在支撑外 (25) 恰好等于已有的实际等距图 F_tau^hyp。
支撑边界有开重叠，故所有 jet 真正贴接。

初始 Q=0 的开段上 w=0，两种图都等于原柱，故 r=0 也为开重叠。
位置、周期与 C3 都由实际公式保持；没有只给周期 II 却漏掉位置 monodromy。
材料变量 (r,u) 从头至尾相同，没有随时间重做角弧长。

## 5. 全局共同度量、正则性与真实曲率符号

由 (24) 直接求导，

$$
(F_*)_r=\chi a'e_r+b e_z,\qquad
(F_*)_u=w\chi'e_r+R e_\theta.
$$

因此整张 (25) 的共同度量有同一个明确公式

$$
\boxed{
g=
\left(1+(\chi^2-1)a'^2\right)dr^2
+2\chi\chi' w a'\,dr\,du
+\left((1+\chi w)^2+w^2\chi'^2\right)du^2 .}
\tag{26}
$$

在 chi=1 的区域它正是 dr^2+a^2 du^2，
而在那里 F_tau^hyp 确实有这个度量；在其余区域由实际 F_* 得到。
所以 (26) 对全角、全时间严格成立。

其行列式为

$$
\det g=R^2(b^2+\chi^2a'^2)+b^2w^2\chi'^2>0 .
\tag{27}
$$

严格正性来自 b>0、R>=1-w>0。
这给正则浸入，而不是只用度量的形式正定代替真实构造。

在 chi=-1 的开核心扇区，R=2-a、r 仍是经线弧长，
实际形系数及曲率为

$$
L_*=\frac{a''}{b},\qquad M_*=0,\qquad
C_*=(2-a)b>0,\qquad
\boxed{K_*=\frac{Q_\delta}{a(2-a)}>0}
\quad(Q_\delta>0).
\tag{28}
$$

在 chi=1 的开区域，

$$
\boxed{K=-Q_\delta/a^2<0}\quad(Q_\delta>0).
\tag{29}
$$

例如 r 位于 (3T/8,T) 时两个符号都出现在实际开片中。
(22) 的过渡区由实际图 (24) 决定；不预设它只有某一种曲率符号。

当 chi 非常数时，(26) 一般有非零 dr du 项，并不是同一径向
warped metric 的改名。本稿没有把已审径向 mixed-flux 守恒不当地套给 (26)。
若另用共同法向测地坐标消交叉项，所得角向系数通常依赖 u；
这仍不付帽边值匹配。

## 6. 全时 Hessian 的真实预算

以下均在固定坐标 (r,u) 的通用覆盖上，对欧氏参数向量 h 使用 |h|。
先看负 K 图。在定向 (9) 下，

$$
(F^{\rm hyp})_{rr}=L N,\quad
(F^{\rm hyp})_{ru}=a'e_2+M N,\quad
(F^{\rm hyp})_{uu}=-aa'e_1+C N .
\tag{30}
$$

由 0<=M^2,Q<=1/100、C>=4/5，

$$
|L|=\frac{|M^2-Q|}{C}\le\frac1{80}.
$$

法向二次型矩阵 [[L,M],[M,C]] 的对称算子范数至多其最大绝对行和，
故至多 13/10；这里不是把三项绝对系数任意粗加。
切向二次项由

$$
|2a'h_rh_u e_2-aa'h_u^2 e_1|
\le(1+a)|a'|\,|h|^2
\le\frac3{10000}|h|^2
$$

控制。因此整段负 K 领上

$$
\|D^2F_\tau^{\rm hyp}[h,h]\|
\le\frac{13003}{10000}|h|^2<\frac43|h|^2.
\tag{31}
$$

原柱核的相应上界是 11/10。

记 Delta=(chi-1)w e_r。实际导数为

$$
\begin{aligned}
\Delta_{rr}&=(\chi-1)a''e_r,\\
\Delta_{ru}&=a'\{\chi'e_r+(\chi-1)e_\theta\},\\
\Delta_{uu}&=w\{(\chi''-\chi+1)e_r+2\chi'e_\theta\}.
\end{aligned}
\tag{32}
$$

利用 (7)、(23) 及 2|h_rh_u|<=|h|^2，

$$
\begin{aligned}
\|D^2\Delta[h,h]\|
&\le q_{\rm star}
 \left\{2+T(K_1+2)+\frac{T^2}{2}(K_2+2K_1+2)\right\}|h|^2\\
&\le\frac7{200}|h|^2.
\end{aligned}
\tag{33}
$$

于是整个新环带，包括旧柱核和全部贴接处，有

$$
\boxed{\quad
\|D^2\widetilde F_\tau[h,h]\|
\le\frac{821}{600}|h|^2<\frac32|h|^2 .
\quad}
\tag{34}
$$

这使用实际坐标 Hessian；没有把只有法向曲率的界误当全 Hessian。

## 7. 全局弦长、嵌入及全部边界近点的 reach

将柱图 G_tau=gamma_tau+r e_z 延长为全参数带上的比较图。
原柱核上差恒为零。由 (30) 从 r=0 积分，

$$
\begin{aligned}
|(F_\tau^{\rm hyp})_r-e_z|&\le T/80,\\
|(F_\tau^{\rm hyp})_u-\gamma_\tau'|
&\le T(1/10+1/10000),
\end{aligned}
$$

因此 ||D(F_tau^hyp-G_tau)||<=T/4。
又由 (7)、(23)，

$$
\|D\Delta\|\le2q_{\rm star}T+
 \frac{q_{\rm star}}2T^2(K_1+2)\le T/40 .
$$

故全参数带

$$
\|D(\widetilde F_\tau-G_\tau)\|\le11T/40\le11/4000<1/10.
\tag{35}
$$

给任意两个材料点，选 |Delta u|<=pi 的角 lift。
两个 lift 之间的直线段留在参数带内。由 (1)、(2)，

$$
|G_\tau(r,u)-G_\tau(s,v)|
\ge\frac35\sqrt{(r-s)^2+(\Delta u)^2}.
$$

沿这条参数线段对 (35) 积分，得到真实空间弦长下界

$$
\boxed{\quad
|\widetilde F_\tau(r,u)-\widetilde F_\tau(s,v)|
\ge\frac12\sqrt{(r-s)^2+(\Delta u)^2}.
\quad}
\tag{36}
$$

所以不同材料点的像不同；联合 (27)、紧致性与光滑性，整张图嵌入。

下面处理包括边界的全近点问题。设空间点 y 有两个不同的最近点 p=F(x)、
q=F(x')，共同距离为 d。仍取上述最短角 lift，v=x'-x。
由 p 的单侧极小点条件，沿可行路径 x+t v、0<=t<=1，

$$
(y-p)\cdot DF(x)v\le0 .
\tag{37}
$$

这在 r=-1/10 或 r=T 的边界上仍然成立，不要求 y-p 垂直整张切平面。
Taylor 定理与 (34) 给

$$
q-p=DF(x)v+R,\qquad |R|\le\frac34|v|^2 .
$$

等距离恒等式和 (37) 因而给

$$
|q-p|^2=2(y-p)\cdot(q-p)
\le\frac32\,d\,|v|^2 .
$$

而 (36) 给 |q-p|^2>=(1/4)|v|^2。因此 d>=1/6。
像是紧集，每一点都有最近点，故

$$
\boxed{\operatorname{reach}(\widetilde F_\tau)\ge1/6 .}
\tag{38}
$$

这里空间弦长换算明确使用 co-Lipschitz 常数的平方。
(37) 已覆盖有边盘/环带的全近点法锥；没有把无边曲面的双侧法线公式套到边上。

## 8. 全图直径、H 与 E(3)

在 tau=0 时，负 K 图就是旋转参考。在旧柱核及新领上统一粗估为

$$
|\widetilde F_0|
\le1+\frac1{10}+T+q_{\rm star}T^2 .
$$

所以对整个初态像，

$$
D\le2(1+1/10+T+q_{\rm star}T^2)
\le\frac{1110001}{500000}<\frac94 .
\tag{39}
$$

由 (3)、(38)，

$$
\frac{\operatorname{diam}\widetilde F_\tau(H)}D>\frac23,
\qquad
\frac{\operatorname{reach}(\widetilde F_\tau)}D>
\frac{2}{27}>\frac3{100}.
\tag{40}
$$

D 在这里是整个新图的初态直径，并非只取旧柱核的直径。

最后核全部 E(3)。下边界的长度固定为 2pi。
chi-1 的支撑总长度至多3eta，故

$$
\int_0^{2\pi}\chi\,du\ge2\pi-6\eta=\frac{15\pi}8>0 .
$$

上边界由 (26) 的实际角长度给

$$
\begin{aligned}
\ell_+
&=\int_0^{2\pi}
 \sqrt{(1+\chi w(T))^2+w(T)^2\chi'^2}\,du\\
&\ge2\pi+w(T)\int_0^{2\pi}\chi\,du>2\pi .
\end{aligned}
\tag{41}
$$

任何把两个整像对应的欧氏刚体运动，包括反射，都把内禀边界对应到内禀边界，
并保留各边界长度；因此不可能交换上下两条边界。
它必把 tau=0 的下边界圆映到非零 tau 的下边界 gamma_tau，
这与该 gamma_tau 非圆矛盾。

故整像在全部 E(3) 下非全等。紧致性还给每个固定非零 tau 的刚体商
Hausdorff 距离严格为正，但本稿没有有效下界，也没有把材料点移动当像距离。
不继承 root 后续强支持核的任何数值幅度或整体证书。

## 9. 这一步如何用于帽问题，以及它未做什么

本构造已经实际接到同一非圆、固定 H 的柱核上。
它第一次在本光滑 bump 分支中直接加入正 K 开片，而不要求把整圈非解析
角数据交给一个正 K Cauchy 演化；那些正 K 片由固定参考位置承担，
开重叠由局部有限传播和径向框架唯一性支付。
在正 K 核心扇区，其实际横向半径 2-a 正在减小；
在活动角区，其半径度量 a 正在增大。

因此它给非径向帽接线一个真实的起始模块。
但 T 很短，整个域还是环带；没有径向圈坍缩为正则中心，
没有完整 cap 的共同度量/第二形式/位置边值匹配，
也没有证明这种短桥可以反复堆积直到闭合。
所有正 K 片在各时间固定，不意味着未知后续帽也已固定或已存在。

特别区分两个接口事实：

- 若一个已存在的帽在平面边界上满足 F_r 为固定垂直方向，
  则 M=0、a'=0；反射另一帽时，边界 C² 可成立而不迫 L=0。
  法向 N 位于该平面内，所以反射保留 L N。
- 若要在两帽间插入开柱核，柱核的 F_rr=0。
  帽还必须在同一材料坐标中匹配 L=0；
  C>0、M=0 时由 Gauss 方程这等价于相应 a''=0。
  只有 a=1、a'=0 不能省掉这个两 jet 条件。

这两条只是准确的后续接口，未把帽 BVP 变成已解结论。
主 flat17 数据未读取或分析；本稿不改变任何已固定数值任务。

## 10. 证明和执行来源

新结论的来源为第3节的局部差能量、第4至5节的实际拼接公式，
以及第6至8节逐项几何估计。R50/R51 只提供已经独审的实际输入及统一寿命，
其独审报告没有预先审过本稿。

root 要求优先推进真正非径向接口并要求完整核有限传播和位置重叠；
本稿的局部证明与新构造尚须另由未参与者全文独审。
文中纯有理常数可另以小脚本核验；这里尚无本版实际程序回执。
没有终端数学执行、PDE 数组、求解器、网格或截图，也没有借旧运行绑定新文本。


## 附录 A. 本版纯有理常数检查源

下列完整 JavaScript 仅核24项有理恒等式与严格门，
不构造实际曲面数组、不求解 PDE、不证明有限传播。
本版实际执行时间和固定源哈希必须由另行回执给出，
不能把源码存在当成已经运行。

```javascript
(() => {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;};
  const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
  const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>add(a,f(-b[0],b[1]));
  const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>f(a[0]*b[1],a[1]*b[0]);
  let count=0;
  const eq=(a,b)=>{if(a[0]*b[1]!==b[0]*a[1])throw Error("equality gate "+count);count++;};
  const lt=(a,b)=>{if(!(a[0]*b[1]<b[0]*a[1]))throw Error("strict gate "+count);count++;};
  const q=f(1,100),T=f(1,100);
  eq(add(q,q),f(1,50));
  lt(f(1,50),f(1,16));
  eq(add(f(1,4),mul(f(1,4),f(2))),f(3,4));
  lt(f(3,4),f(1));
  eq(div(q,f(4,5)),f(1,80));
  eq(add(f(6,5),f(1,10)),f(13,10));
  eq(add(f(13,10),f(3,10000)),f(13003,10000));
  lt(f(13003,10000),f(4,3));
  eq(mul(q,add(add(f(2),f(1)),f(1,2))),f(7,200));
  eq(add(f(4,3),f(7,200)),f(821,600));
  lt(f(821,600),f(3,2));
  lt(add(add(f(1,80),f(1,10)),f(1,10000)),f(1,4));
  eq(mul(q,f(5,2)),f(1,40));
  eq(add(f(1,4),f(1,40)),f(11,40));
  eq(mul(f(11,40),T),f(11,4000));
  lt(f(11,4000),f(1,10));
  lt(f(1,2),sub(f(3,5),f(11,4000)));
  eq(div(mul(f(1,2),f(1,2)),f(3,2)),f(1,6));
  eq(mul(f(2),add(add(add(f(1),f(1,10)),T),mul(q,mul(T,T)))),f(1110001,500000));
  lt(f(1110001,500000),f(9,4));
  eq(div(f(3,2),f(9,4)),f(2,3));
  eq(div(f(1,6),f(9,4)),f(2,27));
  lt(f(3,100),f(2,27));
  eq(sub(f(2),mul(f(6),f(1,48))),f(15,8));
  return {kind:"exact-rational-constant-gates",pass:count,fail:0,pde_runs:0,arrays_generated:0};
})()
```
