# R105：由同一实际 Cartesian 图的小度量残差供应弧长修复

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明。** 本文给 [R103](R103-circle-arclength-metric-repair.md) 的稳定输入公式，
只使用同一实际 Cartesian 曲面及其自身目标度量。没有求解新曲线、改变 g，
也没有报告一个新候选通过。raw CP 的入口、RHS 速度或另一张旧图均不替代这些输入。

主要用处是：先形成相对目标的三个小残差，再求弧长修复所需的全部量，
避免把两个约为背景 a_s 的积分相减后才得到很小的交叉项。
小角振幅不能代替实际材料径向导数；该导数也从同一图的二 jet 计算。

## 1. 固定目标、实际图和三个残差

令 Y(s,psi) 是所检验的 C² Cartesian 图。共同材料角为

$$
u=\Theta(s,\psi),\qquad
\rho=\Theta_\psi>0,\qquad
\nu=\Theta_s,\qquad b=\nu/\rho,
\qquad D_s=\partial_s-b\partial_\psi.
\tag{1}
$$

Theta 是 C² degree-one lift。固定目标为

$$
g=\zeta(s)^2ds^2+a(s)^2du^2
=\zeta^2ds^2+a^2(\rho\,d\psi+\nu\,ds)^2,
\qquad a,\zeta>0.
\tag{2}
$$

这里 a、zeta、Theta 及其导数均取自该实际图所比较的同一数学目标。
zeta 允许实际径向重参数，不未经核对等同于程序中的 lambda 或其倒数。
沿用 R103 的 $a\in C^2$、$\zeta\in C^1$；没有增加对 Y 的 C³ 要求。

定义三个未归一的小残差

$$
\begin{aligned}
\Delta_{ss}&=|Y_s|^2-(\zeta^2+a^2\nu^2),\\
\Delta_{s\psi}&=Y_s\cdot Y_\psi-a^2\nu\rho,\\
N=\Delta_{\psi\psi}&=|Y_\psi|^2-a^2\rho^2.
\end{aligned}
\tag{3}
$$

在目标正交框架
zeta^(-1)D_s、(a rho)^(-1)partial_psi 中，原图的残差恰为

$$
\boxed{
\varepsilon_{rr}
=\frac{\Delta_{ss}-2b\Delta_{s\psi}+b^2N}{\zeta^2},
\qquad
f=\frac{\Delta_{s\psi}-bN}{a\zeta\rho},
\qquad
\Gamma=\frac{N}{a^2\rho^2}.}
\tag{4}
$$

**证明。** 用 D_sY=Y_s-bY_psi 展开平方和内积。
所有目标交叉项相消，因为 b rho=nu；
径向项的目标部分为 zeta²，材料角向项的目标部分为 a²。证毕。

标量 epsilon_rr 刻意不用 R82/R103 的字母 e；
后者表示一个空间速度误差向量，本稿没有混用二者。

记

$$
q=\sqrt{1+\Gamma}>0.
$$

R103 的径向法向速度误差和切向速度分别为

$$
d=\varepsilon_{rr}-\frac{f^2}{1+\Gamma},
\qquad
\tau_r=\frac f q.
\tag{5}
$$

因此原三个小残差已给出不可由任何保圈重参数化消除的 d。
这里没有把原径向残差 epsilon_rr 直接当成 d。

## 2. 材料径向变化只需要实际二 jet

因为混合导数相等，

$$
\rho_s=\nu_\psi=(b\rho)_\psi,\qquad
\rho_s-b\rho_\psi=\rho b_\psi.
\tag{6}
$$

于是目标单位径向导数

$$
h=\frac1\zeta D_s\Gamma
$$

准确等于

$$
\boxed{
h=
\frac{N_s-bN_\psi}{\zeta a^2\rho^2}
-\frac{2\Gamma}{\zeta}
\left(\frac{a_s}{a}+b_\psi\right).}
\tag{7}
$$

**证明。** 对 Gamma=N/(a²rho²) 使用商法则，再代 (6)：
D_s(a²rho²)/(a²rho²)=2a_s/a+2b_psi。证毕。

公式中

$$
\begin{aligned}
N_s&=2Y_\psi\cdot Y_{s\psi}
-2aa_s\rho^2-2a^2\rho\rho_s,\\
N_\psi&=2Y_\psi\cdot Y_{\psi\psi}
-2a^2\rho\rho_\psi,\\
b_\psi&=\frac{\nu_\psi\rho-\nu\rho_\psi}{\rho^2}.
\end{aligned}
\tag{8}
$$

它们只使用同一实际图的 Y_s、Y_psi、Y_spsi、Y_psipsi，
以及自身目标 a、a_s、rho、rho_s、rho_psi、nu、zeta。
没有要求 Y 的三阶导数，也没有把某个未投影速度、Galerkin RHS 或瞬时均值高度速度
当成保存图 Y_s。

实际区间计算宜先在对应的有限多项式/三角表达中形成 N，
再对该同一残差表达求导，或使用具有共同项消去的等价式 (8)。
仅知道 N 的 sup 很小，并不能推断 N_s 或 N_psi 小；
这些导数必须来自实际二 jet 或其准确残差表达。

## 3. 物理角原点和 rho 权原函数

固定同一条全局材料射线 u=0。若 Theta(s,0)=0，旧图中的积分下限就是 psi=0；
否则必须取

$$
\psi_0(s)=\Theta(s,\cdot)^{-1}(0).
\tag{9}
$$

下列完整周期积分取区间 [psi0,psi0+2pi]；
其数值当然不依周期起点，但部分原函数依赖这个材料原点。
定义

$$
\ell(s)=\frac1{2\pi}\int_{\psi_0}^{\psi_0+2\pi}\rho q\,d\psi,
\qquad
M(s)=\frac1{2\pi}\int_{\psi_0}^{\psi_0+2\pi}
\rho\frac{h}{2q}\,d\psi,
$$

$$
J(s,\psi)=
\int_{\psi_0(s)}^\psi
\rho(s,t)
\left[
\frac{h(s,t)}{2q(s,t)}
-\frac{M(s)}{\ell(s)}q(s,t)
\right]dt.
\tag{10}
$$

rho>0，故 ell>0。原函数的被积函数在整圈积分为零。
积分权必须是 rho dpsi=du；不采用未加权的等间距 psi 均值。

**命题。** R103 逐圈弧长修复的交叉速度缺口满足

$$
\boxed{\quad w=\frac f q-aJ.\quad}
\tag{11}
$$

所有右边在旧图的同一点 (s,psi) 求值；
取全域上确界时不需要先反解新角。

**证明。** 在物理角 u 中，
q_s/zeta=h/(2q)、ell_s/zeta=<h/(2q)>_u=M。
R103(23) 给 C/zeta=a times 原函数
integral_0^u [h/(2q)-(M/ell)q]dt。
利用 du=rho dpsi，恰为 aJ。
再代 tau_r=f/q，即得 (11)。证毕。

即使 psi0 随 s 移动，这一证明仍成立，因为 h 已按固定物理 u 求导，且部分积分也从固定
物理射线 u=0 起算。若改用固定 psi 的径向导数，就不能省掉 (7) 中的平流项，
也不能在对部分弧长求导时省掉移动下限项。

## 4. 直接由小残差给修复后的完整误差矩阵

将 (5)、(11) 代入 R103(11)，其中 f²/q² 精确相消，得到

$$
\boxed{
\widetilde{\mathcal E}
=
\begin{pmatrix}
\varepsilon_{rr}-2a(f/q)J+a^2J^2&
\ell(f/q-aJ)\\
\ell(f/q-aJ)&\ell^2-1
\end{pmatrix}.}
\tag{12}
$$

这是相对于原固定目标 g 的准确矩阵。
右上角同时保留原 f 与重排产生的 aJ，径向项同时保留它们的交叉积。
不是只把原 Gamma 替换成均值而保持原 E/F 不动。

若在一个连续区域内有

$$
|\varepsilon_{rr}|\le A,\quad |f|\le B,\quad
q\ge m>0,\quad |aJ|\le C,\quad
|\ell^2-1|\le U,\quad \ell\le L,
$$

则

$$
\|\widetilde{\mathcal E}\|_{op}
\le
\max\{A+2BC/m+C^2,\ U\}
+L(B/m+C).
\tag{13}
$$

**证明。** 先按 (12) 分别包住两个对角项和非对角项，
再用对角矩阵的最大绝对值范数加非对角矩阵范数。证毕。
实际包围若保留更多相关性，可直接评估 (12)，不必使用这个粗界。

另一方面，R103(13b) 仍给任何保圈重参数化的必要下界

$$
\mathcal E_{\rm any}\ge
\max\left\{\sup\left|
\varepsilon_{rr}-\frac{f^2}{1+\Gamma}
\right|,
\ \sup_s|\ell^2-1|\right\}.
\tag{14}
$$

所以即使 Gamma 的非均值项完全消失，不能把一个已经超容差的正常径向速度或周长
误差称为修复成功。

## 5. 原函数连续包围及计算收益的准确范围

式 (10) 的 integrand 含小量 h；没有单独积分两个背景大小为 a_s 的项再相减。
这就是本表示相对于直接弧长径向差的收益。
并未证明某个现成候选的 h 已小，或某个普通浮点积分自动是严格包围。

给定同一连续径向盒和覆盖一圈的角分割，若每段已经有
rho、q、h 的连续包围和完整积分的向外包围，则：

1. 由正 rho、q 得 ell 的正区间，由同段积分得 M 的区间；
2. 按 (10) 包围 integrand 及各部分积分；
3. 利用其准确零均值，J 同时等于从原点向前的积分和负的剩余反向积分。
   两个安全包围可取交集，不需假定有限舍入的总和字面为零；
4. 用 (4)、(7)、(12) 组合得到新图的连续 metric 包围。

这是一项条件的区间组合证明：每个包含关系由积分的单调性、正分母和准确恒等式推出。
它不要求新解一次 ODE，也不要求先存一张重新插值的新 Cartesian 曲面。
新映射已经由 R103 的准确弧长函数和唯一单调逆定义；
所有旧角都被新角遍历，因此同一连续原图上的包围覆盖整张新图。
若只能得到角采样或有限 FFT，上述组合尚不成为连续证书。

R103(25) 还给粗备选：若物理角具有准确的 k 重周期、q≥m，
且 |h|≤H，则

$$
|aJ|\le\frac{\pi a}{km}H.
\tag{15}
$$

不能仅凭求解器配置写了某个 spacing，就假定实际保存图和目标具有该准确对称；
k=1 始终是可用的保守选择。保留真实角频率原函数界可进一步收紧，见 R103(26)。

## 6. 实际使用边界

本稿与 R103 一起作用于同一个实际 C² Cartesian 图、自己的目标和自己的完整活动带。
在 prefix/tail 接缝需使用共同物理角和同一全局原点；真正 cuff 的完整两 jet 保持使
新映射在固定帽上延拓为恒等。全时像集和几何转移由 R103 付出，不从另一候选借取。

新的 raw CP 入口工具只提供那个 raw CP 自己的角向及周长信息。
若需要最终 Cartesian base 的 ell、d、J，必须由该 base 的 (3)、(8)、(10) 重新形成。
首个真实 inner 尚未在本稿中给出数值；当前求解器、目标、图及接受容差没有改变。

### 6.1 实际对称轴的必要量也排除任意保圈角修复

若实际保存图有准确的柱坐标奇偶表示

$$
Y=R(s,\psi)e_r(\psi)+T_c(s,\psi)e_\theta(\psi)+Z(s,\psi)e_z,
$$

其中 R、Z 是 cos(3j psi) 和，T_c 是 sin(3j psi) 和，
则在 psi=0 或 pi/3 的材料轴上，

$$
R_\psi=Z_\psi=T_c=(T_c)_s=0,\qquad
Y_\psi=(R+(T_c)_\psi)e_\theta,\qquad
Y_s=R_s e_r+Z_s e_z.
\tag{16}
$$

这些是有限多项式的准确奇偶恒等式，不是把浮点 sin(pi) 当成零。
对当前原 warp，nu 在这两轴也严格为零。
所以 f=0，且不可消法向残差成为

$$
d=\frac{R_s^2+Z_s^2}{\zeta^2}-1.
\tag{17}
$$

若从该新图自己的准确节点 jet 和自身目标 zeta 已给 |d| 的严格下界，
式 (14) 不仅约束原参数图，也约束任意保持同一径向层圈的角重参数化。
后者虽可改变轴点的新材料标签，但仍遍历那个同一旧几何点。

若生产目标转移以 lambda=1/zeta 记号表达，则 (17) 是
lambda²(R_s²+Z_s²)-1。未作该同一目标转移的 base 标量不能直接拒绝 common 图；
common 修正支持内还须使用 common 自己的 jet，不能借修正前的 base 值。
本推论只提供实际下一节点筛选的数学依据，没有加入新候选的数值结论。
