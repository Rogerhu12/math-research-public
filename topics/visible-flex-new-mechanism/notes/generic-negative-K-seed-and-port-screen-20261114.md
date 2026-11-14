# 通用负 K 径向度量、全角端口必要筛与凸核心预算

日期：2026-11-14。独占新增 `scripts/cosine_connector_radial_seed.py` 和 `scripts/cosine_connector_port_screen.py`。文件名前缀保留开发来源，但径向度量和必要筛并不依赖 C3，可用于新的 C2 椭圆平柱。本文没有运行研究候选优化，也没有给此前已被严格曲率门排除的 cos 候选求连接器。

## 1. 独立长度与准确开放端口

给定准确核心周长参数 `a0`、末圆领半径 `rc>0`、独立物理长度 `L>0`。取归一化坐标 `u=t/L`，开核心和开平尾的比例分别为 `c0,cf>0`，且 `c0+cf<1`。令 `q=1-c0-cf` 为活动部分比例。

活动部分分成三个比例 `f1,f2,f3>0`，和为一。定义径向收缩速度

\[
d(t)=-a'(t).
\]

在开核心段取 `d=0`。前两段活动区用

\[
S_5(x)=10x^3-15x^4+6x^5
\]

连接 `0 -> mu -> nu`；最后一段默认用

\[
S_{11}(x)=462x^6-1980x^7+3465x^8-3080x^9+1386x^{10}-252x^{11}
=2772\int_0^x y^5(1-y)^5\,dy
\]

连接 `nu -> 1`，在开平尾取 `d=1`。`S11` 的一至五阶导数在两端为零，且 `S11(1-x)=1-S11(x)`。要求 `mu>nu>0`。由于每段都在其端点值之间，`d≥0`，所以 `a` 单调不增。配置 `tail_smoothstep_order=5` 仅保留为显式不同的旧模型，不能把这项改动称为同度量精化。

定义

\[
A={f_1+f_2\over2},\quad B={f_2+f_3\over2},\quad C={f_3\over2},
\quad g=\mu-\nu>0.
\]

利用 `integral_0^1 S5=integral_0^1 S11=1/2`，活动区的平均速度为

\[
\bar d=A\mu+B\nu+C.
\]

总端口条件精确等价于

\[
a_0-r_c=L(q\bar d+c_f).
\]

因此长度无需被一个固定平均速度锁死，而可设

\[
\boxed{\nu={((a_0-r_c)/L-c_f)/q-Ag-C\over A+B},
\qquad \mu=\nu+g.}
\tag{1}
\]

只接受 (1) 给出 `mu>nu>0` 的设计。随后

\[
a(t)=a_0-\int_0^t d(x)\,dx
\]

满足全区 `a≥rc>0`；最初开放段准确 `a=a0`，最终开放段准确

\[
a(t)=r_c+L-t,\qquad a'=-1,\qquad a''=a'''=0.
\tag{2}
\]

默认 `c0=1/25,cf=3/50,(f1,f2,f3)=(1/4,7/20,2/5),g=3/10,tail_smoothstep_order=11`。如果去掉两个 buffer，并另固定 `mu=19/20,nu=13/20`，活动平均才是旧方案的 `583/800`；新接口不固定这个数。特别是椭圆长轴端口需要更大的 `L` 时，可通过较慢的 `mu,nu` 保留相同的负 K 机制。

本度量不要求 `|a'|≤1`。这个额外条件仅在将其解释为普通旋转参考母线时才需要。模块报告 slope 是否≤1，但不把所有非旋转实现都限制到这个参考子类。

## 2. 确切负 K 区和正则性

对 `g=dt²+a(t)²dtheta²`，

\[
K=-a''/a=d'/a.
\]

中间一段 `d:mu -> nu` 严格递减，内部有 `K<0`。其完整积分为

\[
\boxed{\int_{middle}K\,dA
=2\pi\int_{middle}d'\,dt=-2\pi g<0.}
\tag{3}
\]

这是准确公式，不是有限网格上碰巧出现几个负值。总半带积分仍为 `2pi`，与 `a'` 从 0 到 -1 相符。径向函数 `a` 为分段多项式 C3，因为前两段 `S5` 的一、二阶导数在端点均为零，末段 `S11` 更平坦；满足当前位置 C2 框架所需的度量正则性。

### 为什么本轮必须更改末段

设到开平尾起点的反向距离为 `delta`，R28 有限场在该处硬锁二 jet，因而 `u,v,beta-beta_tail=O(delta^3)`。令 `alpha=atan(v)`、`psi=theta+u`。积分性残差沿 T 的分量准确为

\[
R_T=\cos\beta\cos\alpha\,\psi_\theta
+\sin\beta\,\alpha_\theta-a'.
\]

因为 `beta_tail=±pi`，且 `mean(u_theta)=0`，对角取平均得到

\[
\operatorname{mean}R_T=-(1+a')+O(\delta^6).
\]

旧末段 S5 在 `nu != 1` 时给 `1+a'` 一个非零三阶首项，所以上述硬锁二 jet 的有限表示不能在尾端准确等距。这是当前有限表示与旧目标度量的局部失配，不是任意 C2 面的一般不存在定理。

新 S11 末段长度记为 `ell3`，则

\[
1+a'=(1-\nu)\left\{462(\delta/\ell_3)^6+O(\delta^7)\right\}.
\]

它消除三阶与六阶的直接冲突；尚未证明六阶系数及其余完整方程可解。末段修改不影响入口 `a'=c3*x^3+...` 的 `c3=-10*mu/ell1^3`，不影响中间负 K 积分，也不改变 (1) 中的 `mu,nu`。只有度量函数本身与准确身份改变。

在 `nu<1` 且这一末段 `|a'|<=1` 时，辅助旋转角 `acos(-d)` 在平尾的角差现在是三阶，可以 C2 接常值；这仍不提供整个旋转参考或非轴连接器。实际 R28 标量框架继续使用真实核心端口二 jet 和平尾常值构造自己的未知场。

## 3. 解析参数导数及冻结身份

新类接口：

```python
from cosine_connector_radial_seed import NegativeKRadialSeed

seed = NegativeKRadialSeed.from_core(core, length, cut_radius, config)
values = seed.evaluate(t)  # a, a_s, a_ss, a_sss, K
Jp = seed.parameter_jacobian(t, order=2, coordinate='physical')
# 或固定同一个归一化配点 u：
Ju = seed.parameter_jacobian(u, order=2, coordinate='normalized')
```

参数列固定为 `(a0,rc,L,gap)`。`order=0,1,2` 始终指物理径向导数 `a,a',a''`；`coordinate` 只指定做参数微分时固定 `t` 还是固定 `u=t/L`。

令 `F(u;mu,nu)=integral_0^u d`，则 `a=a0-LF`。`F,d,d_u,d_uu` 对 `mu,nu` 均线性。由 (1)，

\[
\nu_{a_0}={1\over Lq(A+B)},\quad
\nu_{r_c}=-{1\over Lq(A+B)},\quad
\nu_L=-{a_0-r_c\over L^2q(A+B)},\quad
\nu_g=-{A\over A+B},
\]

`mu` 的前三个导数相同，`mu_g=nu_g+1`。固定归一化点时，代码直接对 `a0-LF,-d,-d_u/L` 求导；固定物理 `t` 时，长度列还分别增加

\[
u d,\qquad {u d_u\over L},\qquad {u d_{uu}\over L^2}.
\tag{4}
\]

这些项不能因配点实现方便而遗漏。端口和内部接缝处所提供的 0–2 阶参数导数仍连续；没有声称三阶径向导数在移动接缝处也具有同样的参数可微性。

`from_core` 把数学 `a0` 绑定到冻结核心身份与准确周长积分定义。高精度计算同一个积分后数值末位发生变化，不改变 `definition_sha256`；真正改变 `L,rc,gap`、分段比例或 `tail_smoothstep_order` 会改变定义。新 schema 为 `negative-K-open-port-radial-metric-v2`，保存 `[5,5,11]`（或显式旧模型 `[5,5,5]`）及准确多项式。新设计阶段可以改变这些数，但固定度量加密必须保存整个定义、准确核心身份和物理区间。

## 4. 连续端口盒的通用输入

`cosine_connector_port_screen.py` 使用的每个 `PortCell` 含：

- `side,index`：正／负外侧和原角 cell 编号；
- `position`：真实端口位置的三维连续区间盒；
- `outward_velocity`：准确单位材料测地线初速度的连续区间盒；
- `theta`：该 cell 上真正材料角的区间，不能以构造角 phi 替代。

椭圆提供器只消费独立 `ellipse_frame_port.EllipticCylinderPort` 的准确 `A_exact,B_exact,width_exact` 与身份，不另写一个浮点核心求值器。它用

\[
v(\phi)=\sqrt{A^2\sin^2\phi+B^2\cos^2\phi},\qquad
\theta={2\pi\ell(\phi)\over P}
\]

构造连续材料角包围。每小段弧长使用端点梯形积分及 `h³ sup|v''|/12` 的定向余项，并和 `h[vmin,vmax]` 相交；前缀再用 `P-suffix` 收紧。正负端口准确为 `(A cosphi,B sinphi,±w)`，向外速度分别 `±ez`。

cos 提供器复用已冻结 `FrozenRibbon` 的弧长、位置和正 J 证书，再用真实 Frenet binormal 得到 `±B`。它覆盖完整原角圆，因为正 J 保证原角和材料角为同一个圆上的双射。

长度 `L` 必须从这些盒所表示的实际端口开始量到末圆领。椭圆平柱可准确延伸整个开核心 buffer；有限宽 cos 核不能据这个接口擅自越过已经认证的 `|s|≤w`。未来若把 cos 连接器的起点移到核心内部，须同步移动端口盒和物理长度，不能仅调整一个记号。

## 5. 弦长与帽高：必要 outer 和充分 inner 分开

固定末圆领材料位置

\[
Y(\theta)=(r_c\cos(\theta+\chi),r_c\sin(\theta+\chi),h).
\]

每条材料径向线具有准确长度 `L`，故必要

\[
d_{xy}(\theta)^2+(h-z(\theta))^2\le L^2.
\tag{5}
\]

一个 cell 的真实值满足 `dxy²∈[dl²,du²],z∈[zl,zu]`。

如果 `dl²>L²`，该 cell 已严格排除这个固定圆领、长度和相位。否则任何真实可行帽高都必须落在

\[
\left[z_l-\sqrt{L^2-d_l^2},\ z_u+\sqrt{L^2-d_l^2}\right].
\tag{6}
\]

对所有 cell 取交，得到必要高度集合的 **outer 包围**；这个交为空才给严格排除。区间算术对根号上界定向向外，不能拿 `d_upper` 替换这里的 `d_lower` 来缩窄后宣称无解。

另一方面，如果每个 cell 都有 `du²≤L²`，则

\[
\bigcap_{cells}
\left[z_u-\sqrt{L^2-d_u^2},\ z_l+\sqrt{L^2-d_u^2}\right]
\tag{7}
\]

中的每个高度都连续满足所有弦长不等式。这是 **只针对弦长条件的充分 inner 区间**。它为空或区间暂不能解析，均不排除真实连接器；即使它非空，也没有证明等距、嵌入或 reach。

若完整设计另要求帽高位于一个固定高度包络内，可同时和该包络相交。报告明确记录该额外条件，不把设计包络当成所有可能解的普遍限制。

## 6. 任意端口和方向的 R25 必要门

令 `K` 为核心的填充平面投影域，未来完整面要求投影在 `K+B_p`。对任一真实端口点 `x`、准确向外单位材料速度 `V` 和水平单位方向 `e`，记

\[
b=(e\cdot V)_+=\max(e\cdot V,0).
\]

若完整面的 reach≥tau，径向线为单位测地线，R25 的转向比较给出必要条件

\[
\boxed{e\cdot x+\tau(1-\sqrt{1-b^2})\le h_K(e)+p.}
\tag{8}
\]

当 `b>0` 时，曲率上界 `1/tau` 迫使切向从初始外向夹角转到非外向前至少有右侧所列的额外位移；当 `b=0` 时，(8) 只留下原投影包络条件。它不需要当前点是真 support 点，也不需要 `e·T=0`。R25 的 support 版本是在真实 support 点处进一步把 `e·x` 化简而得。

**此处是准确等距目标的必要筛。** 单位速和测地线两项假设不可省略。对于 R28 只有小度量残差的实际重构面，材料径向线一般不是其实际诱导度量的测地线；仅有 C0 度量误差或实际 shape operator 上界，均不能控制这条曲线的切向加速度。因此不能直接把 (8) 当作近似数值面的 reach 认证。要对那张实际近似面使用相同转向比较，必须另外控制实际径向线的完整空间曲率，或改用它的真正单位测地线。当前报告明确保留这个准确目标假设。

代码用原角 cell × 整个方向圆的 cell 覆盖来计算 (8)，不将一组有限方向点的通过称为全方向证明。每个方向 cell 的 support 函数也连续包围。椭圆准确使用

\[
h_K(e)=\sqrt{A^2e_x^2+B^2e_y^2}.
\]

一般 star 则用完整中心投影曲线各 cell 的点积包围，取所有下界的最大值和所有上界的最大值，分别得到对该方向 cell 统一有效的 support 下界与上界。

严格正的超额下界给出违反 (8) 的连续见证；超额上界为正而下界非正只是未解析。所有 cell 超额上界均≤0 才报告全角、全方向的这个必要门通过。椭圆柱有更强准确特例：端口投影本来就在 K，全部向外初速度竖直，因此 (8) 对所有方向准确成立，不需要用浮点网格猜这个事实。

默认所用 tau 是 `0.03` 乘已证的核心直径下界：椭圆为 `2A`，C3 cos 核可用两 tip 之间的 `sqrt(3)(1+a+b)`。若改用更强的 planned tau，报告会明确其失败不能普遍排除一个真实直径较小的候选。即使用必要 tau，support 排除也仍以所声明的完整投影包络为设计假设。

## 7. 凸 C3 上界与两瓣椭圆的不同预算

设 K 是以原点为旋转中心的凸 C3 平面域，`R=max|x|`。它包含某个最远点的三个 C3 轨道点，因而包含这三个点的正三角形，进一步包含半径 `R/2` 的圆盘。同时三个点的两两距离为 `sqrt(3)R`，所以

\[
D_{xy}\ge\sqrt3R,\qquad
R/2\le h_K(e)\le R.
\]

凸体 Hausdorff 距离等于 support 函数差的上确界，因此对任意相位旋转

\[
\boxed{d_H(K,R_\alpha K)\le R/2\le{D_{xy}\over2\sqrt3}
\approx0.288675D_{xy}.}
\tag{9}
\]

凸体边界的 Hausdorff 距也满足同一个上界：边界点若位于另一凸体外，用到凸体的距离；若位于内，沿自身的一个支撑外法线走到另一边界，其距离不超过对应 support 差。正三角形转 60 度可达到 (9)，圆角化不能提高这个普遍上界。

这排除了由一个凸 C3 平面核心本身贡献 `0.3D` 旋转像距见证的方案。它没有排除完整三维连接器贡献更大像距，也不把材料滑动误记为振幅：公开来源 README 的 `delta_hold` 明确是未经刚体对齐的 **Hausdorff 像距离**。

两瓣椭圆不受 (9) 限制。对 `A=1,B=7/25=.28`，90 度旋转后长轴端点到原填充椭圆的距离准确为 `1-B=18/25=.72`。如果未来完整面仍投影在该椭圆、满足 `|z|≤9/20=.45`，则

\[
D\le D_{env}={\sqrt{481}\over10}\approx2.1932,
\qquad {\delta_{hold}\over D}\ge {36\over5\sqrt{481}}>0.328.
\tag{10}
\]

一个被逐点固定的平盘 `r=11/50=.22` 给

\[
{\operatorname{diam}H\over D}\ge{22\over5\sqrt{481}}>0.200.
\]

椭圆平柱的最小主曲率半径为 `B²/A=49/625=.0784`，大于 `0.03Denv≈.0658`。这只说明准确核心的局部曲率与预算相容，不是完整 reach 下界。

取 `rc=.22,L=.9` 时，开平尾起始半径 `rc+cf L=.274` 小于 B，所以圆尾的整个平面投影能放入该椭圆。长轴端口的水平弦长至少 `.78`；R4 的曲率转向必要界用 `tau0=.03×2=.06` 还要求 `L≥.78+.06(pi/2-1)≈.8143`。`.9` 未被这个单点门排除。全材料角的弦长、高度交集仍须由上面连续筛在 Actions 上实际检查，不能从这个长轴算例推出。

本预算依赖整个连接器满足投影和高度要求，依赖真正的开放圆尾／平盘以及完整非局部几何证书。旧椭圆连接器失败没有被这些条件预算抹去；此次改变的是目标框架表示、保留准确端口和显式负 K 度量。

## 8. 已做开发检查与 Actions 入口

径向开发检查只使用人工 `a0=.7,L=.9,rc=.22,gap=.3`，分别检验固定 t 和固定 u 的解析参数导数、端点和接缝的径向 0–3 jet、准确负 K 积分、同一准确 a0 的加密身份不变，以及真实 L 改变能被 hash 检出。结果在 `notes/generic-radial-seed-check-20261114.json`，`passed=true`。

必要筛开发检查只用一个人工单位圆平柱和 64 个连续角 cell。`L=.5,rc=.8` 得到非空全角充分弦长高度区间；`L=.05` 给严格水平弦长排除；准确竖直端口的全方向转向门由恒等式通过。结果在 `notes/continuous-port-screen-check-20261114.json`，`passed=true`。没有在本地运行研究核心或参数扫描。

未来公开 Actions 的最小椭圆必要筛命令为：

```bash
python topics/visible-flex-new-mechanism/scripts/cosine_connector_port_screen.py \
  --ellipse-major 1 --ellipse-minor .28 --half-width .02 \
  --length .9 --cut-radius .22 --height-max .45 --padding 0 \
  --angular-nodes 1024 --direction-cells 24 \
  --out "$VISIBLE_OUT/ellipse-port-screen.json"
```

这条命令尚未在本笔记中执行或宣布通过。可行性筛不求连接器；通过后仍需实际 R28 BVP、同一准确度量加密、完整面嵌入和全时间 reach。

本轮统一使用中央半宽 `w=.02`。椭圆柱可准确延伸开核心 prefix，故不需要用 `w≥c0 L=.036` 来容纳它；中央核加 prefix 的实际高度仍须计入完整位置和高度预算。
