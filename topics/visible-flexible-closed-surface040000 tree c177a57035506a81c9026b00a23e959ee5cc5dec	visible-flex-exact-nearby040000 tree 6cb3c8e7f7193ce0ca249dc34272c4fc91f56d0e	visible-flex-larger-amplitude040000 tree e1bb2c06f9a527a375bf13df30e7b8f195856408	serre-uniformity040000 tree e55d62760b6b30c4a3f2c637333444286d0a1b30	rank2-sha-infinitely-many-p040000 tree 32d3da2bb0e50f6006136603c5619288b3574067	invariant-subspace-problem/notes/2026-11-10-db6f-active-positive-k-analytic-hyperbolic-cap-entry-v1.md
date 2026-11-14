# 活动正曲率与周长收缩：局部角解析和双曲解拼成的实际全圈帽入口

**状态：完整作者证明，待未参与者全文独审。** 2026-11-10，独立几何分工。

本文从已经精确闭合、具有固定 H 的光滑凸柱核出发，构造一个实际的
共同非径向度量短领。新领中的正 Gauss 曲率区域包含真正变形中的自由 bump；
非解析角点被保留在负曲率通道中。新领的上边界总周长严格小于柱核周长，
其曲率积分为正；全部位置、框架、周期、全 jet 贴接和正宽嵌入均在下文支付。

这一结果仍然有两条边界，不是一个有心帽，更不是闭曲面。
它不解决从这些负曲率通道到正则中心的剩余问题。
不读取优化数组，不运行 BVP、tail、RK、PDE、曲面网格或任何大数据。

## 1. 固定的实际输入和本稿范围

使用以下固定来源：

- R51 作者正文
  [be7b380055c1906a1abacfc5682da0e372ef8579](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)，
  完整独审
  [5597dffd479f6ca0c80f3cba871862a319af20e9](https://github.com/Rogerhu12/math-research/blob/5597dffd479f6ca0c80f3cba871862a319af20e9/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-smooth-core-fixed-h-reach-v1.md)。
- R50 退化入口作者正文
  [a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b](https://github.com/Rogerhu12/math-research/blob/a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-increasing-q-smooth-flat-entry-v1.md)，
  完整独审
  [0fbb537133c97af06cf55ca3939f002f5cfb17ad](https://github.com/Rogerhu12/math-research/blob/0fbb537133c97af06cf55ca3939f002f5cfb17ad/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-increasing-q-smooth-flat-entry-v1.md)。
- 固定正 K 扇区的有限传播与真实短桥作者稿
  [4c436678284b17a5e14f8629ce706bab5a1425c0](https://github.com/Rogerhu12/math-research/blob/4c436678284b17a5e14f8629ce706bab5a1425c0/topics/visible-flexible-closed-surface/notes/2026-11-10-db6f-nonradial-mixed-curvature-collar-v1.md)。
  本稿的新变系数系统、活动正 K 解析片及其拼接不由该稿代替审查。

R51 给真实的平面单位速率族 gamma_tau(u)，u 属于 R/(2pi Z)，
tau 在一个固定紧区间中，gamma_0=e_r，并有

$$
|\gamma_\tau'|=1,\qquad
\frac9{10}\le\kappa_\tau\le\frac{11}{10},\qquad
|\gamma_\tau(u)-\gamma_\tau(v)|\ge\frac35|\Delta u|
\quad(|\Delta u|\le\pi).
\tag{1}
$$

omega=2pi/3、eta=pi/48。
位置及全部角导数在 |u-j omega|<=eta 上等于单位圆，
且 gamma_tau 具有材料 C3；每个非零 tau 的曲线不是圆。
原柱图与握持集合为

$$
G_\tau(r,u)=\gamma_\tau(u)+r e_z,\quad -1/10\le r\le0,
$$

$$
H=\bigcup_{j=0}^2\{|u-j\omega|\le\eta,\ -3/40\le r\le-1/40\}.
\tag{2}
$$

H 逐点固定，有内部，diam H>=sqrt(3)>3/2。

本稿还使用这个输入的一个已经明确写出的额外性质。
R51 的自由 bump 是

$$
h(u)=
\exp\left\{\frac4{(c-a)^2}
-\frac1{(u-a)(c-u)}\right\}\quad(a<u<c),
\tag{3}
$$

在区间外为0，其中 (a,c)=(omega/8,omega/4)；
控制 bump 使用同样的公式于 (3omega/8,5omega/8)。
控制函数再乘以正弦、余弦并作 omega 周期复制。
因此全部初始角数据在有限集合

$$
\mathcal S=\{\,\omega/8,\omega/4,3\omega/8,5\omega/8\,\}
               +\omega\mathbb Z
\quad\bmod 2\pi
\tag{4}
$$

之外局部实解析。初始位置的积分常数不妨碍局部角解析性。
在每个与 S 保持正距离的紧角区上，可选对整个紧 tau 族共同的复邻域。
这是从实际指定 bump 的公式得到的性质，不假设任意 C-infinity 数据都解析。
此外，R51 首扇区位移约束对有限参数 (tau,alpha) 是解析映射：
其被积的正弦、余弦对这些参数整，且在固定有限区间上一致可积。
同一个可逆 Jacobian 因而也给解析隐函数 alpha(tau)。必要时把已有参数区间
限制为一个更小但非零的固定紧区间，其复邻域内初始参数依赖解析。
没有改动原族或它的闭合方程。

结论是：存在固定 T>0 和实际 C-infinity 嵌入族
F_tau:[-1/10,T] cross S^1 -> R^3，
它精确保留 (2)，具有共同 g=dr^2+a(r,u)^2 du^2 和 C3；
新领同时具有活动的正 K 区及负 K 区，上边界长度小于2pi；
全时 reach>=1/6，初态整图 D<9/4，故 reach/D>2/27、
diam H/D>2/3；每个非零 tau 与初态在全 E(3) 下不全等。
未给有效 0.05D 幅度，未借后续强支持核的证书。

## 2. 一个固定、平均为负的角系数

令

$$
\mathcal C=\{\pi/4,\pi/2,3\pi/4,5\pi/4\},\qquad
\varepsilon_0=10^{-6},
$$

$$
P(u)=\prod_{c\in\mathcal C}
       \sin^2\left(\frac{3u-c}{2}\right),\qquad
k(u)=\varepsilon_0-P(u).
\tag{5}
$$

P 是解析三角多项式，周期 omega，零点恰是 (4)；
0<=P<=1、|P'|<=6，所以 |k|<1、|k'|<=6。
在每个非解析角点 k=epsilon_0>0，并在其开邻域为正。

平均值可以精确算出。写 t=3u，将相差 pi 的两因子配对：

$$
P=\frac1{32}(1-\sin2t)(1-\sin t)
       \left(1+\frac{\cos t-\sin t}{\sqrt2}\right).
$$

用整周期正交关系，

$$
\boxed{\quad
\langle P\rangle=\frac{8+3\sqrt2}{256}>\frac1{32},
\qquad
\langle k\rangle<-\frac1{33}.
\quad}
\tag{6}
$$

这里 angle brackets 表示 (2pi)^(-1) 的角平均。
第二个严格门由 10^(-6)<1/32-1/33 得到。

自由 bump 中点 u_c=pi/8 满足

$$
P(u_c)=\sin^4(\pi/16)\sin^2(3\pi/16)\sin^2(7\pi/16)
\ge\frac{441}{16777216}>\varepsilon_0 ,
\tag{7}
$$

使用 sin x>=2x/pi 于 [0,pi/2]。
因此自由 bump 的一个真正开子区有 k<0。
选其中某个 u_* 不等于中点，便有 h'(u_*)!=0。
在该区控制 bump 恒为零，故精确有
kappa_tau=1+tau h'，不是只在一阶成立。

固定一个光滑正函数 k_h，周期 omega，满足

$$
k_h=k\ \text{当 }P\le3\varepsilon_0/4,\qquad
k_h\ge\varepsilon_0/8,\qquad k_h\le\varepsilon_0 .
\tag{8}
$$

一个具体选择是在 3epsilon_0/4<=P<=7epsilon_0/8
之间用平端阶跃把 k 平滑混合到常数 epsilon_0/4，
并在 P>=7epsilon_0/8 后保持这个常数。
混合区内 k 已介于 epsilon_0/8 和 epsilon_0/4 之间，所以 (8) 成立。
k_h 只用于存在和比较的辅助双曲问题，不替换最后固定的 k。

## 3. 固定共同度量及完整非径向 Gauss–Codazzi

令 q_star=1/100，使用固定的非减平端阶跃 S：
S=0 于 x<=1/4，S=1 于 x>=3/4，0<=S<=1。
对最后统一选出的 delta 定义

$$
q_\delta(r)=q_{\rm star}S(r/\delta),\qquad
a_{rr}=\frac{q_\delta k(u)}a,\quad a(0,u)=1,\quad a_r(0,u)=0 .
\tag{9}
$$

在旧核 r<=0 取 a=1。所有时间使用同一个 (9)。
辅助问题 a_h 则把 k 换成 k_h。
两个标量问题在 k=k_h 的开角区上逐点具有相同初值和方程，
所以 a=a_h，并且全部角导数也相同。

对实际 g=dr^2+a(r,u)^2du^2，设

$$
\mu=a_r/a,\qquad \beta=aa_r,\qquad \nu=a_u/a,\qquad Q=aa_{rr}.
$$

第二基本形式 L dr^2+2M drdu+C du^2 的完整方程为

$$
LC-M^2=-Q,\qquad
M_r=L_u-\mu M,\qquad
C_r=M_u+\mu C+\beta L-\nu M .
\tag{10}
$$

最后的 -nu M 不能遗漏。
例如非零 Christoffel 除径向情形的三项外还有
Gamma^u_{uu}=a_u/a；代入 Codazzi 即得 (10)。
内在曲率仍为 K=-a_{rr}/a，允许 a 依赖 u。

在 C>0 的区域，写 X=M/C、Y=1/C。
由 (10) 精确得到

$$
\begin{aligned}
X_r={}&X X_u-q k Y Y_u-q k_uY^2
 -2\mu X-\beta X^3+\beta q k X Y^2+\nu X^2,\\
Y_r={}&X Y_u-Y X_u-\mu Y-\beta YX^2+\beta q kY^3+\nu XY .
\end{aligned}
\tag{11}
$$

此处 q=q_delta。
(11) 在 k 任意符号、包括 k=0 时都是关于 X,Y 的合法多项式正常形。
它的使用需要 C 非零，不要求 K 非零。
以下实际解一直有 C>=4/5，因此没有在 C=0 处强行使用它。

root 复算了 (10)–(11) 及下一节的 V 变量代换，确认其符号并提出
严格正 k 重叠的要求；这些是作者讨论贡献，不把 root 计为本稿这部分的
未参与者独审。

## 4. 正 k 的光滑退化入口：变系数版本

本节对固定 C-infinity 的 k_h>=c>0 证明所需全圈存在性；
它不把尚未证明的非径向推广当作 R50 的原陈述。

暂写 k=k_h、a=a_h，令

$$
V=\sqrt k\,Y,\qquad d=k_u/(2k).
$$

则 (11) 等价于

$$
\begin{aligned}
X_r={}&X X_u-q V V_u-q dV^2
 -2\mu X-\beta X^3+\beta q XV^2+\nu X^2,\\
V_r={}&X V_u-V X_u-\mu V-\beta VX^2
 +\beta qV^3+(\nu-d)XV .
\end{aligned}
\tag{12}
$$

初值 X_0=0、V_0=sqrt(k)/kappa_tau>0。

### 4.1 正则化、主部和能量

令 q_e=q_delta+e，0<e<=1/100，sigma=q_delta'/q_e，
保留同一个实际 a_h、mu,beta,nu，并写 X=q_e Z、Z_0=0。
精确代换给

$$
\begin{aligned}
Z_r={}&q_eZ Z_u-V V_u-\sigma Z
 -2\mu Z-\beta q_e^2Z^3+\beta q_eZV^2-dV^2+\nu q_eZ^2,\\
V_r={}&q_eZ V_u-q_eV Z_u-\mu V-\beta q_e^2VZ^2
 +\beta q_eV^3+q_e(\nu-d)ZV .
\end{aligned}
\tag{13}
$$

这是近似 PDE；不声称 q_e k_h=aa_rr。
它与 R50 具有完全相同的主部和阻尼，新增项只是零阶项。
特别地，第二行中每个含最高阶 Z 的非运输项仍带 q_e；
第一行的 -dV^2 虽不带 q_e，但其高阶能量外面带 q_e。

对整数 s>=4 取

$$
E_s=q_e\|Z\|_{H^s}^2+\|V\|_{H^s}^2+\|Z\|_{H^{s-1}}^2 .
\tag{14}
$$

最高交叉项在加权 Z、未加权 V 两式间抵消。
权重与阻尼合起来给 -q_delta'||Z||_{H^s}^2，
低阶另给 -2sigma||Z||_{H^{s-1}}^2。
低阶 Z 方程中的 V partial_u^s V 用 V 的 H^s 范数直接控制。
对新增项逐项检查：

- 加权最高阶 -dV^2 用 sqrt(q_e)Z_s 与 sqrt(q_e)V_s 控制；
  低阶部分只需 V 的 H^{s-1}。
- nu q_e Z^2 的最高阶 Z 项外面至少有 q_e；
  低阶 Z 的 H^{s-1} 是未加权的。
- 第二行 q_e(nu-d)ZV 的最高阶 Z 项有 q_e，
  可配对 sqrt(q_e)Z_s 与 V_s，绝无除以 q_e 的损失。
- mu,beta,nu,d 的角导数只是给定系数。
  用一维乘积和交换子估计，其高阶范数作为已知的加性系数进入 tame 估计。

因此，在控制 E_4 的有界球内，

$$
E_s'+q_\delta'\|Z\|_{H^s}^2
 +2\sigma\|Z\|_{H^{s-1}}^2
\le C_s(E_4,\text{系数低阶})
 \{E_s+\text{系数高阶常数}\}.
\tag{15}
$$

寿命只由有限个低阶角范数、V_0 的正下界、
q_star 和给定系数界决定，不需要 q_delta' 的上界。

对 (13) 的整个右端作 Fourier Galerkin 投影。
(14) 的权重 q_e 仅依 r，故投影在能量配对中可自伴移除；
这里特意先用 V=sqrt(k_h)Y，而不对带角权 k_h 的能量假装投影可交换。
(15) 先给 E_4 的统一时间，再在同一时间上控制全部高阶。
每个未加权的 Z 的 H^j 范数由 E_{j+1} 控制，不从 q_e 项中除出来。
V_r 的低阶范数统一有界，故共同缩短时间使 V 保持正。

### 4.2 实际变量极限、唯一性及参数

在实际变量 X=q_eZ、V 中，q_delta'Z 与 -q_e sigma Z 精确抵消，
得到 (12) 的投影版本而无 q_delta' 项。
X_r、V_r 的任意有限角范数因而统一有界。
先对每个 e 取全局 Galerkin 极限，再令 e 趋零；
角紧致性和这些时间界给实际 X,V 的极限，满足 (12) 的 q=q_delta 版本。
由 V>0、k_h>0 回收 Y=V/sqrt(k_h)、C=1/Y、M=X/Y，
并用 (10) 回收 L。方程在固定光滑系数下逐阶给 r 的 C-infinity 正则性。

任意光滑物理解也具有所需唯一性。
其 X 方程可写成沿速度 -X 的运输方程

$$
X_r-X X_u=A_0(r,u)X
   +q_\delta\{-V V_u-dV^2+\beta XV^2\},
\tag{16}
$$

其中 A_0=-2mu-beta X^2+nu X。
零初值及逐角阶运输估计给

$$
\|X(r)\|_{H^j}\le C_j\int_0^r q_\delta(s)\,ds
\le C_j r q_\delta(r).
\tag{17}
$$

若 q 先恒零至 r_*，先用 q=0 的三角系统唯一，
然后 (17) 的右边可换为 C_j(r-r_*)q(r)。
所以在 q>0 上任意物理解的 Z=X/q 均为 O(r-r_*)，
可从 r_*+h 开始对两个解作 (14) 的差估计，再令 h 趋零。
sigma 的项仍有利，给任意光滑物理解的唯一性，而不只证明某个近似序列唯一。

对固定 q,k_h,a_h，参数 tau 只改变初值。
对 (13) 差商、再逐阶微分 tau，主部与权重相同，sigma 不被微分。
新增源项是已控制的低阶参数导数乘积；
因此同一时间上实际 X,V、进而位置图 C-infinity 依赖 tau。
以上正则化只是存在证明，不是本稿运行过的 PDE 计算。

### 4.3 统一寿命与 delta 的顺序

a_h 的各阶角导数由逐角微分 (9) 的标量积分方程控制。
右端只含 q_delta 及 k_h 的角导数，不含 q_delta'。
故 mu,beta,nu 的所需角范数在固定小窗中对 delta 统一；
d 是一次固定的光滑函数。
(15) 先给统一 T_h>0，再选择 delta，避免先截止后用其高导数决定寿命。

## 5. 正 k 重叠中的局部有限传播

取一个开区间 I，在其闭包上 k>=c_I>0。
两套解只要在这里使用同一个 a,k,q，
其 Z,V 差的主部就是

$$
\zeta_r=A\zeta_u-V_1v_u-\sigma\zeta+\text{低阶},\qquad
v_r=A v_u-q_eV_1\zeta_u+\text{低阶},
\quad A=q_eZ_1 .
\tag{18}
$$

新系数 nu,d 只贡献零阶差项；(14) 的局部差能量可直接使用。
共同缩短时间，使真实正则化解在相关区间上
|X_e|<=1/4、Y_e<=2。这里 0<k<1 且 q_e<=1/50<1/16，
故

$$
|A|+\sqrt{q_e}|V_1|
=|X_e|+\sqrt{q_e k}\,Y_e\le3/4<1 .
\tag{19}
$$

在 I_r=(u_-+r,u_+-r) 上取
q_e||zeta||_{H^s(I_r)}^2+||v||_{H^s(I_r)}^2
+||zeta||_{H^{s-1}(I_r)}^2。
配对主通量为

$$
A(q_e\zeta_s^2+v_s^2)-2q_eV_1\zeta_s v_s ,
$$

其绝对值由 (19) 乘配对能量密度控制；
未加权低阶 zeta 运输速度也小于1。
两个端点以速度1内缩，所以端点总贡献非正。
权重导数及阻尼仍是 -q_delta' 和 -2sigma。
低阶 zeta 的 v_u 直接用高一阶 v 控制；
全部变系数交换子和新增零阶项由 C E_s 控制。
由初始差为零、Gronwall 得两解在 I_r 中相同。

这个论证对每个固定 e 的真实光滑 PDE 解进行，
不对有限 Fourier 投影声称有限传播。
最后取实际 X,V 的极限，得到 q=0 退化入口也适用的局部相同性。

下节的解析解也能参加这个比较。
在解析片上对相同 a 先以 q_e 取代 q，
令 X_e(0)=0。沿 (16) 的局部特征线、在比解析片稍小的区间中，
逐角微分给

$$
|\partial_u^j X_e(r,u)|
\le C_j\int_0^r q_e(s)\,ds
\le C_j r q_e(r).
\tag{20}
$$

初值各阶 X_e 均为零；系数及解析解的角导数有统一上界。
缩短时间保证这些特征线留在原解析片。
所以 Z_e=X_e/q_e 的所有所需角范数统一有界。
只在 k>=c_I>0 的重叠中定义 V_e=sqrt(k)Y_e，
(18) 的同一局部能量即可比较解析解与双曲解。
没有在 k=0 处使用 d=k_u/(2k)。

## 6. 局部角解析片及统一 CK 寿命

使用 Nishida 原讲义的 Chapter III §2，Hypothesis 2.1 与 Theorem 2.1，
印刷页64–65，以及拟线性应用印刷页72–73：

[原作者讲义](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/bb/b2/bbb2303a-1e17-4807-a319-290a5b030b2f/n_nishida-102.pdf)。

这里只使用其演化变量连续、角变量解析的版本，不要求 q_delta 关于 r 解析。
原讲义的差估计为 C/(rho-rho')，寿命由这个常数、初始球和解析宽度决定。

令 A={P>=epsilon_0/3}。这是与有限 S 保持正距离的紧集。
由 §1，为 A 选有限多个实开角区 J_l，
其稍大的复邻域上初始 X_0=0、Y_0=1/kappa_tau
对所有 tau 解析，且 Y_0 及其倒数都有共同界。
实角上 kappa>=9/10；缩小共同复邻域可使复 Y_0 也远离0。

k 是整个函数。标量 (9) 在这些复邻域上对 r 作积分，
由 |a-1| 的小窗 bootstrap 保持 a 远离0。
再留出一个复边界间距，用 Cauchy 估计控制 a_u。
a,a_r,a_u 的解析范数因而对 delta 统一，
mu,beta,nu,q_delta k,q_delta k_u 的解析范数也统一。
这里从始至终没有 q_delta'。

在每个 J_l 内，取嵌套复邻域上的有界全纯函数空间 B_rho。
它们满足乘积不等式以及

$$
\|\partial_u f\|_{\rho'}
\le\frac{C_J}{\rho-\rho'}\|f\|_\rho .
\tag{21}
$$

将 (11) 减去其初值，视为未知 (X,Y-Y_0) 的一阶拟线性系统。
其系数是已给解析函数及 X,Y 的多项式。
在一个固定小球内，乘积、(21) 和均值公式给
C/(rho-rho') 的局部 Lipschitz 界，并给右端在零点的统一界。
因此 Nishida 的三条假设逐项成立。

得到每个片的实际角解析解，允许该片包含 k<0、k=0 和 k>0。
取有限个片的最小寿命，得 T_a>0，与 delta 的高径向导数无关。
实系数和实初值由唯一性给实解；缩短时间保持 C=1/Y>0。
参数依赖也可在同一次存在论证内支付：用 §1 的解析 alpha(tau)，
把 B_rho 换为在角复邻域与一个固定小参数复圆盘的乘积上有界全纯的函数空间。
方程不含 tau 导数，(21) 只损失角半径；参数圆盘保持固定。
因此同一个寿命给联合角/参数解析解，Cauchy 估计给实 tau 的全部阶导数。
有限个参数圆盘覆盖选定实紧区间即可，不按导数阶重新选择时间。

为作第5节比较，在同一实际 a 上将 q 换成 q_e，
同样得到统一寿命和角解析范数。
对 X_e,Y_e 的方程没有 q_delta' 项，故在较小复邻域中
所有有限角阶及一阶时间导数统一有界。
紧致性给 e 趋零的物理极限，解析唯一性将其识别为上面的实际解析解。
这些近似仍不被称为几何。

两个解析片在重叠上的实际解相同：
在任意紧含于重叠的更小复邻域上，初值和方程相同，
直接用同一解析尺度唯一性。故片间没有另一个待调相位。

## 7. 真正的全圈拼接与位置 monodromy

用全圈辅助双曲解处理 P<epsilon_0/2，
用 §6 的解析解处理 P>epsilon_0/2。
切换集合

$$
\mathcal K=\{u:P(u)=\varepsilon_0/2\}
\tag{22}
$$

是有限集：P 是非恒定的三角多项式，所以这个水平集不可能含区间，
且其代数表示给有限个零点。

每个切换点可放入一个固定开区间 I，
其闭包满足

$$
\varepsilon_0/3<P<3\varepsilon_0/4 .
\tag{23}
$$

这里 k>=epsilon_0/4，k_h=k，a_h=a，
而初始数据真实角解析。
解析解和辅助双曲解使用同一个原柱曲率初值。
第5节的正则化比较，随后 e 趋零，给两解在 I_r 中相同。

先固定这些有限区间，并在各区间中选包含切换点的更小开区间。
再统一缩短 T，使这些较小区间留在 I_r 中。
于是切换处有一个完整时空开邻域，两个物理解逐点相同。
因此拼接后的 L,M,C 是整个圆周上的 C-infinity 函数，
满足同一个 (10)，不是沿一条曲线只配上几个 jet。

所有初始数据、k,k_h 和 a 具有周期 omega。
解析片可先在一个基本扇区中选，再复制；
其解由解析唯一性一致，双曲解由 §4 唯一性一致。
故拼成的 L,M,C 以 omega 为周期。

最后从同一个实际原柱位置和框架出发，**在整个圆周上一次性**积分

$$
\begin{aligned}
F_r&=e_1,&(e_1)_r&=L N,&
(e_2)_r&=(M/a)N,&N_r&=-L e_1-(M/a)e_2,\\
F(0,u)&=\gamma_\tau(u),&
e_1(0,u)&=e_z,&e_2(0,u)&=\gamma_\tau'(u),&
N(0,u)&=e_z\times\gamma_\tau'(u).
\end{aligned}
\tag{24}
$$

与此兼容的角方程为

$$
F_u=a e_2,\quad
(e_1)_u=a_r e_2+M N,\quad
(e_2)_u=-a_r e_1+(C/a)N,\quad
N_u=-M e_1-(C/a)e_2 .
\tag{25}
$$

把 (24)–(25) 交叉微分，三个框架相容式正是 (10)。
角误差满足径向齐次线性系统，初值为0，故 (25) 真实成立。
这也直接证明实际诱导度量恰为 dr^2+a^2du^2。

周期性由 (24) 的周期系数及实际周期初值继承；
C3 则由 u 平移 omega 后的初值刚体转动和同一个 ODE 唯一性继承。
没有只拼 II 却漏掉位置闭合；位置积分常数始终固定于 gamma_tau(u)。

在 0<=r<=delta/4，q=0、a=1。
X=0、Y=1/kappa_tau 是该开段的解，
两种存在理论的唯一性均使物理解等于它。
于是 F=gamma_tau+r e_z 在一个开柱领上成立，
与旧核全部 jet 接合。

## 8. 先统一寿命，再一次固定所有尺度

辅助双曲寿命 T_h 由 §4 先给；
有限解析片寿命 T_a 由 §6 先给。
两类解的实际 X,Y 方程都没有 q_delta'，
故由统一角界可先获得 M_r,C_r 以及参数 tau 导数的统一界。

选择一个与 delta 的高径向导数无关的小时间 T_1，
使全部物理片上同时有

$$
|M|\le1/10,\qquad 4/5\le C\le6/5,
\tag{26}
$$

并使正则化比较中的 (19)、第7节的开重叠宽度都成立。
再选一次固定正 T<min(T_h,T_a,T_1,1/100)，
同时满足第9节的一个参数导数小量门，最后取 delta=T/2。
因此整个 [0,T] 已在所有存在、匹配和几何预算的统一窗口中。
没有逐个 tau 重新选度量，也没有先以尖截止决定一个不够长的 CK 寿命。

## 9. 正 K 区确实包含活动形变，并且总周长开始收缩

对最后的实际图，

$$
\boxed{K(r,u)=-q_\delta(r)k(u)/a(r,u)^2.}
\tag{27}
$$

r>3T/8 时 q_delta=q_star。
(4) 附近有 k>0，故有实际负 K 通道；
(7) 的自由 bump 子区有 k<0，故有实际正 K 开片。

选 §2 的 u_*，其中 h'(u_*)!=0 且 k(u_*)<0。
在这个角区初始 C_tau(0,u_*)-C_0(0,u_*)=tau h'(u_*)。
第8节的参数导数界给某个统一有限 B，

$$
\left|\partial_\tau C_\tau(r,u_*)
        -\partial_\tau C_\tau(0,u_*)\right|\le Br .
$$

再使固定 T<|h'(u_*)|/(2B)（B=0 时无须此门），
则对每个允许的非零 tau，

$$
|C_\tau(r,u_*)-C_0(r,u_*)|
\ge\frac12|\tau h'(u_*)|>0 .
\tag{28}
$$

特别在 r 属于 (3T/8,T) 的正 K 片中，实际第二形式随时间改变；
这些正 K 片不是全部固定参考图。
这里没有把一阶非零替代真实有限 tau：对 tau 的积分和 (28) 已给全部
充分小非零 tau 的结论。

设 ell(r)=int a(r,u)du，是实际材料圈的周长。
§10 将证明 |a-1|<=10^(-6)、a>=1/2。
因而 ||1/a-1||<=2*10^(-6)，且 <|k|><=1。
用 (6)，

$$
\left\langle\frac{k}{a}\right\rangle
<-\frac1{33}+2\cdot10^{-6}<-\frac1{34}.
\tag{29}
$$

所以

$$
\ell''(r)=q_\delta(r)\int\frac{k}{a}\,du
\le-\frac{2\pi}{34}q_\delta(r).
\tag{30}
$$

初值 ell(0)=2pi、ell'(0)=0；q 在末段严格为正，
故 ell(T)<2pi。更具体地，

$$
\ell(T)\le2\pi-\frac{25\pi q_{\rm star}T^2}{2176}.
\tag{31}
$$

这是实际整圈长度收缩。
同时整个新领的 Gauss 曲率积分为

$$
\int_0^T\int K\,a\,du\,dr=-\ell'(T)>0 .
\tag{32}
$$

所以并非只在固定小扇区塞入一个局部正 K，而在总曲率和平均周长方向上
仍完全向外扩张。

## 10. 全时嵌入、含边界 reach 和全图比例

### 10.1 固定共同度量的低阶估计

在 |k|<1、q<=1/100 下，对 (9) 先以 a>=1/2 作 bootstrap：

$$
|a_{rr}|\le1/50,\quad |a_r|\le r/50,\quad
|a-1|\le r^2/100.
\tag{33}
$$

在 T<=1/100 上，最后一界严格保持 a>=1/2，
故 bootstrap 延拓成立；特别 |a-1|<=10^(-6)、|a_r|<=1/5000。

令 v=a_u。由角微分的标量方程，

$$
v_{rr}=\frac{qk_u}{a}-\frac{qk}{a^2}v,\qquad v(0)=v_r(0)=0.
$$

若 B_v=sup |v|，则 |k_u|<=6 给

$$
B_v\le\frac3{50}T^2+\frac1{50}T^2 B_v
\quad\Longrightarrow\quad
B_v\le\frac3{499999}<\frac1{1000}.
\tag{34}
$$

这些界只由共同标量 a 得出，与任何 PDE 网格无关。

### 10.2 实际坐标 Hessian 和全弦长

非径向 g 的真实 Gauss 公式为

$$
F_{rr}=L N,\qquad
F_{ru}=a_r e_2+M N,\qquad
F_{uu}=-aa_r e_1+a_u e_2+C N .
\tag{35}
$$

由 (26)、|qk|<=1/100，

$$
|L|\le\frac{M^2+|qk|}{C}\le1/40.
$$

法向矩阵 [[L,M],[M,C]] 的算子范数至多13/10。
由 (33)–(34)，切向二次项对参数方向 h 的范数至多

$$
\{(1+a)|a_r|+|a_u|\}|h|^2
\le(3/5000+1/1000)|h|^2<\frac1{100}|h|^2.
$$

所以整个新领的坐标 Hessian 范数小于131/100<3/2；
旧柱核是11/10，因此整张新环带可统一取

$$
\|D^2F[h,h]\|\le\frac32|h|^2.
\tag{36}
$$

从 (35) 沿 r 积分，与 G_tau=gamma_tau+r e_z 比较：

$$
\|D(F_\tau-G_\tau)\|
\le T(1/40+1/10+1/5000)<T/4<1/10 .
\tag{37}
$$

给任意两点选 |Delta u|<=pi 的 lift，参数间直线留在带内。
由 (1) 和 (37) 得

$$
|F_\tau(r,u)-F_\tau(s,v)|
\ge\frac12\sqrt{(r-s)^2+(\Delta u)^2}.
\tag{38}
$$

故全部时间都为嵌入。

若空间点 y 有两个不同最近点 p=F(x)、q=F(x')，
共同距离为 d，则沿参数可行直线 v=x'-x 的单侧极小点条件给
(y-p) dot DF(x)v<=0。这在两条边界也成立。
由 (36) 的 Taylor 余项，

$$
|q-p|^2=2(y-p)\cdot(q-p)
\le\frac32 d |v|^2.
$$

(38) 的平方给 |q-p|^2>=(1/4)|v|^2，
所以 d>=1/6。紧像总有最近点，因此

$$
\boxed{\operatorname{reach}(F_\tau)\ge1/6.}
\tag{39}
$$

这个论证包含边界的全近点法锥，并明确使用弦长常数的平方，
不是只核无边法线。

### 10.3 整个初态直径、握持与 E(3)

Fr=e1 始终为单位向量，初态 gamma_0 是单位圆，
故对整个初态像可粗估

$$
D\le2(1+1/10+T)\le111/50<9/4 .
\tag{40}
$$

由 (2)、(39) 得 diam H/D>2/3、reach/D>2/27>0.03。

下边界长度为2pi，上边界由 (31) 严格较短。
任何把两个整像对应的 E(3) 元素都保留其内禀边界长度，
所以必须把下边界对应到下边界，不能交换。
初态下边界是圆，而非零 tau 的下边界 gamma_tau 不是圆，
因此两个整像不可能全等。反射也包括在这个判断内。

## 11. 精确的全局缺口与 C=0 问题

本稿从旧柱核真实延伸出共同非径向度量的混合类型领，
活动区能够进入正 K，而所有新图仍有 C>=4/5。
因此在这个有限范围内，进入活动正曲率区不必先穿过 C=0，
也不必给非解析全圈数据硬套椭圆 Cauchy 理论。

不过 a 在当前领中仍接近1，绝不是正则中心。
对本稿**这个固定不变的 k**，在每个 u 属于 S 处 k=epsilon_0>0，
若继续坚持 q>=0 与同一方程，则 a_rr>=0、a_r>=0、a>=1 沿该射线成立。
所以不能把本稿的剖面原样迭代便声称圈会在有限处整体收成一个帽点。
后续必须真正处理这些通道、改变桥的系数/覆盖，或解决新的函数边值匹配。

这不是所有非径向帽的禁止定理，也没有证明任何全局路线必经内部 C=0。
如果将来出现 C=0，(11) 的来源正常形不能在那里继续假设有效；
必须另选合法 Cauchy chart，核覆盖与位置周期，并支付该处实际 C² 正则性。
目前没有完成这一步。

镜射帽本身的 C² 与插入开柱的 L=0 条件仍须分别核：
前者可不迫 L=0；后者必须匹配柱核 F_rr=0。
本稿只在原柱接口有真实的 Q=0 开重叠，不把未知帽接口当作已存在。

## 12. 贡献、独审与运行来源

作者提出按有限非解析角集选择 signed k、局部解析/双曲覆盖和全圈实际恢复。
root 参与核验非径向 Codazzi 的 -nu M 项及 X,V,Z 方程，
并强调正 k 缓冲必须离零和完整位置/框架初值。
本稿明确记录这项数学讨论贡献；后续完整独审须由未参与者支付。

已有 R50/R51 及固定正 K 短桥的审查只作为准确输入。
本稿新证明的签名系数、辅助正 k 延拓、解析覆盖、局部比较、活动正 K、
全周长收缩和最终几何范围均须另审。
本版未执行任何 PDE、BVP、tail、RK、曲面数组或网格。
纯常数检查若另做，将以本版固定文本和实际时间另出回执，
不把旧程序运行绑定到本稿。


## 附录 A. 固定的纯代数与有理门检查源

以下源以 Q(sqrt(2),i) 中的精确 Laurent 多项式乘法核 (6) 的平均系数
及 P(0)，再核本稿使用的有理常数门。
它不求解任何 PDE，不生成曲面数组，不证明局部存在、有限传播或帽闭合。
实际执行须另给固定正文回读与时间回执，不能以源码存在冒充执行。

```javascript
(() => {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;};
  const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
  const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>f(-a[0],a[1]);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>f(a[0]*b[1],a[1]*b[0]);
  const zero=f(0),one=f(1);
  const equal=(a,b)=>a[0]*b[1]===b[0]*a[1];
  let pass=0;
  const eq=(a,b)=>{if(!equal(a,b))throw Error("rational equality "+pass);pass++;};
  const lt=(a,b)=>{if(!(a[0]*b[1]<b[0]*a[1]))throw Error("rational strict "+pass);pass++;};
  const ca=(a,b)=>a.map((x,j)=>add(x,b[j]));
  const qp=(a,b)=>[add(mul(a[0],b[0]),mul(f(2),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
  const cm=(a,b)=>{
    const rr=qp(a.slice(0,2),b.slice(0,2)),ii=qp(a.slice(2),b.slice(2));
    const ri=qp(a.slice(0,2),b.slice(2)),ir=qp(a.slice(2),b.slice(0,2));
    return [sub(rr[0],ii[0]),sub(rr[1],ii[1]),add(ri[0],ir[0]),add(ri[1],ir[1])];
  };
  const cz=()=>[zero,zero,zero,zero];
  const ce=(a,b)=>{if(a.some((x,j)=>!equal(x,b[j])))throw Error("algebraic identity "+pass);pass++;};
  const angles=[
    [[zero,f(1,2)],[zero,f(1,2)]],
    [[zero,zero],[one,zero]],
    [[zero,f(-1,2)],[zero,f(1,2)]],
    [[zero,f(-1,2)],[zero,f(-1,2)]]
  ];
  let poly=new Map([[0,[one,zero,zero,zero]]]);
  for(const [co,si] of angles){
    const plus=[mul(f(-1,4),co[0]),mul(f(-1,4),co[1]),mul(f(1,4),si[0]),mul(f(1,4),si[1])];
    const minus=[plus[0],plus[1],neg(plus[2]),neg(plus[3])];
    const factor=new Map([[0,[f(1,2),zero,zero,zero]],[1,plus],[-1,minus]]);
    const next=new Map();
    for(const [n,a] of poly)for(const [m,b] of factor)next.set(n+m,ca(next.get(n+m)||cz(),cm(a,b)));
    poly=next;
  }
  ce(poly.get(0),[f(1,32),f(3,256),zero,zero]);
  let atZero=cz();for(const a of poly.values())atZero=ca(atZero,a);
  ce(atZero,[f(1,32),f(1,64),zero,zero]);
  const eps=f(1,1000000),q=f(1,100),T=f(1,100);
  lt(eps,sub(f(1,32),f(1,33)));
  lt(mul(f(2),eps),sub(f(1,33),f(1,34)));
  lt(eps,f(441,16777216));
  lt(add(q,q),f(1,16));
  eq(add(f(1,4),mul(f(1,4),f(2))),f(3,4));
  lt(f(3,4),one);
  eq(mul(q,mul(T,T)),eps);
  eq(mul(f(1,50),T),f(1,5000));
  eq(div(mul(f(3,50),mul(T,T)),sub(one,mul(f(1,50),mul(T,T)))),f(3,499999));
  lt(f(3,499999),f(1,1000));
  lt(add(f(3,5000),f(1,1000)),f(1,100));
  eq(div(add(f(1,100),f(1,100)),f(4,5)),f(1,40));
  eq(add(f(13,10),f(1,100)),f(131,100));
  lt(f(131,100),f(3,2));
  lt(add(add(f(1,40),f(1,10)),f(1,5000)),f(1,4));
  lt(f(1,2),sub(f(3,5),mul(T,f(1,4))));
  eq(div(mul(f(1,2),f(1,2)),f(3,2)),f(1,6));
  eq(mul(f(2),add(add(one,f(1,10)),T)),f(111,50));
  lt(f(111,50),f(9,4));
  eq(div(f(1,6),f(9,4)),f(2,27));
  lt(f(3,100),f(2,27));
  eq(mul(f(1,34),mul(f(5,8),f(5,8))),f(25,2176));
  return {pass,fail:0,exact_field:"Q(sqrt(2),i)",pde_runs:0,geometry_arrays:0};
})()
```
