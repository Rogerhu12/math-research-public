# R95：保持原残差及 Newton 方向的 Q/L 回缩

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：完整证明的有限方程坐标工具，附一个真实 W22 失败步的局部比较。** 本文不更换 tail 的物理度量、完整有限 shooting 残差、Jacobian、Newton 修正方向、分支 floor 或原来的接受条件。它把原来直线的 trial 改为一条一阶完全相同的曲线。新接口已实际执行固定节点比较，但没有得到新 DN、整尾或闭曲面解；尤其本次回缩仍不能让所比较的旧 trial8 通过原 floor .05。

依赖为 [R86](R86-geometric-momentum-prolongation.md) 的完整动量 root 与 [R89](R89-tail-fourier-product-variational-flow.md) 的有向微分公式。下文给出所需推导，不从数值局部表现预设全 shooting 收敛。

## 1. 一个物理节点上的精确坐标

固定一个射击节点的 $r,w,\mu>0$、方向 $\epsilon=\pm1$ 与角间隔 m，令

$$
W=w^2,\quad E=1+W,\quad k_j=mj,\quad
c_0=1,\ c_j=\sqrt2\cos(k_j\theta),\ s_j=\sqrt2\sin(k_j\theta).
$$

与原引擎相同，写

$$
P=-\sum_{j=1}^M\frac{k_jr^3Q_j}{\sqrt2w}s_j,\qquad
T=P_\theta,\qquad L=\sum_{j=0}^M L_jc_j,\qquad K=L-T.
$$

这里 T 只表示 $P_\theta$，并非另一状态未知量。定义

$$
S=1-WP^2,\qquad D=E S-W(1+K)^2,\qquad A=1+L+WT.
\tag{1}
$$

原角连接及其归一矩是

$$
\omega=\frac{1+W(1+K)T/S}{\sqrt D},\qquad
\mathcal M_i(Q,L)=\mathcal Q\!\left[\frac{\omega-1}{W}c_i\right].
\tag{2}
$$

$\mathcal Q$ 可以是准确角平均，也可以是原来同一个有限 N 点平均。以下使用当前有限模型时，不改变 N，也不去掉有限节点的 alias。原 state $y=(Q,\pi)$ 的 root 正是

$$
\mathcal M_0(Q,L)=0,\qquad
\mathcal M_j(Q,L)=\tau\pi_j\quad(1\le j\le M),
\qquad
\tau=\frac{\epsilon\sqrt{12}\mu}{\sqrt2 r^4W}.
\tag{3}
$$

在原允许分支 $A,D,S>0$ 内，R86 已给出

$$
B_{ij}:=\partial_{L_j}\mathcal M_i
=\mathcal Q\!\left[\frac{A}{D^{3/2}}c_ic_j\right].
\tag{4}
$$

角基在所选平均下独立时，B 为实对称正定矩阵；当前 $N>4mM$ 足以保证这一点。所有当前实际 floor 仍由原 engine 检查。

## 2. 去掉均值后仍是一个真实局部坐标图

设 $(Q^0,L^0)$ 满足 (3)，并有严格分支间隙。因为 $B_{00}>0$，隐函数定理给出邻域内唯一光滑均值函数

$$
L_0=\ell_0(Q,L_h),\qquad L_h=(L_1,\ldots,L_M),
$$

使 $\mathcal M_0=0$。于是定义

$$
\Psi(Q,L_h)=\bigl(Q,\tau^{-1}\mathcal M_h(Q,\ell_0(Q,L_h),L_h)\bigr).
\tag{5}
$$

它的 $L_h\mapsto\pi$ 微分为

$$
\frac1\tau\left(B_{hh}-B_{h0}B_{00}^{-1}B_{0h}\right).
\tag{6}
$$

括号是正定矩阵 B 的 Schur 补，故可逆；$\tau\ne0$。由于 (5) 的 Q 分量是恒等，整个 Jacobian 可逆。再次由逆函数定理，$(Q,L_h)$ 与 $(Q,\pi)$ 在这一点的邻域内是两套真实光滑坐标。

原 `toRaw` 使用的非均值 raw 坐标为

$$
R_j=\gamma L_j,\qquad
\gamma=\frac{\sqrt2w}{\sqrt{12}r^3}>0.
\tag{7}
$$

在固定节点上 $\gamma$ 为常数，所以改用 $(Q,R)$ 不影响局部可逆性。

这个证明只需当前点附近的严格正分支。它没有证明整个 raw 坐标域凸，也没有保证一个大回缩步的均值方程仍可解。

## 3. 原 Newton 方向的准确 raw 微分

令原完整 shooting Jacobian 给出的一个节点方向为
$\dot y=(\dot Q,\dot\pi)$。不重新求另一个 Newton 方向。对 (3) 直接求导：

$$
\boxed{\quad
B\dot L=
\begin{pmatrix}0\\\tau\dot\pi\end{pmatrix}
-\mathcal M_Q\dot Q.
\quad}
\tag{8}
$$

这里只解一个 $(M+1)$ 阶正定系统。原引擎已经给出 B；$\mathcal M_Q\dot Q$ 也不需要差分或额外 ODE。

为把最后一项完整说明，固定 L，记 $p=\dot P$、$t=\dot T$。由 (1)，

$$
\dot K=-t,\quad \dot S=-2WPp,\quad
\dot D=2W(1+K)t-2WEPp.
$$

对 (2) 的商逐项微分可得

$$
\partial_Q\frac{\omega-1}{W}[\dot Q]
 =F_Pp+F_Tt,
\tag{9}
$$

其中

$$
F_P=\frac{EP\omega}{D}
 +\frac{2W(1+K)TP}{S^2\sqrt D},
$$
$$
F_T=-\frac{ET+W(1+K)(WP^2+2K+K^2)/S}{D^{3/2}}.
\tag{10}
$$

例如未化简的 t 系数是

$$
\frac{1+K-T}{S\sqrt D}-\frac{\omega(1+K)}D.
$$

利用 $D=ES-W(1+K)^2$，通分后的分子变为
$-EST-W(1+K)[WP^2+2K+K^2]$，就是 (10)。p 系数由 $S,D$ 的上述导数直接得到。

具体有

$$
p=-\sum_j\frac{k_jr^3\dot Q_j}{\sqrt2w}s_j,\qquad
t=-\sum_j\frac{k_j^2r^3\dot Q_j}{\sqrt2w}c_j,
$$

所以

$$
(\mathcal M_Q\dot Q)_i=\mathcal Q[(F_Pp+F_Tt)c_i].
\tag{11}
$$

这就是原 `rhsWithJacobian` 中已有的权函数。新 helper 保留相同有限节点/余弦/正弦投影，只对给定方向计算一次 (11)，再求 (8)，不会把已知 Newton 修正偷换为另一个加权或截断修正。

最终 raw 方向为

$$
\dot z=(\dot Q,\dot R),\qquad \dot R_j=\gamma\dot L_j\quad(j\ge1).
\tag{12}
$$

$\dot L_0$ 同时保留，用于后面的均值初猜。

## 4. 回缩及其对原残差的作用

记 $z=(Q,R)$ 是原 state 对应的 raw 点。对 trial 参数 $\lambda$，先在 raw 坐标中走直线

$$
z(\lambda)=z+\lambda\dot z,
$$

重解**原来的**均值方程 $\mathcal M_0=0$，再按 (3) 投影回动量，得到 $y(\lambda)$。由第2节的局部图和链式法则，

$$
\boxed{\quad y(0)=y,\qquad y'(0)=\dot y,\qquad
y(\lambda)=y+\lambda\dot y+O(\lambda^2).\quad}
\tag{13}
$$

证明如下：$z(\lambda)$ 的导数由 (8)、(12) 正是原 state 到 raw 图的微分；再用其逆图，两个微分相乘为恒等。局部图是 C²，Taylor 公式给出二阶余项。这是完整有限状态的陈述，不只是保留 Q 的一阶项。

所有节点取这种回缩的直积，便得到全 shooting trial。额外的平均高度变量如有记录，仍沿原方向作线性更新；它们不进入这里的 $2M$ 形状/动量 root。

令 $\mathcal F$ 是原来的完整 shooting 残差，包含相同真实有限 ODE、相同端口及全部边界条件。只要所考察局部轨道处于严格分支，有限 RK/隐式 root 组成的 $\mathcal F$ 对状态是 C²。若原修正满足

$$
D\mathcal F(y)\dot y=-\mathcal F(y),
$$

则从 (13) 得

$$
\mathcal F(y(\lambda))=(1-\lambda)\mathcal F(y)+O(\lambda^2).
\tag{14}
$$

因此对于任何固定的原残差范数，$\mathcal F(y)\ne0$ 时足够小的正步具有与原 Newton 方向相同的一阶下降。若线性方程有求解误差 e，右侧相应多出 $\lambda e$；这里不把实际 LU/浮点误差假设为零。

同样，在一个真有限根附近，原 Jacobian 可逆且各坐标图二阶导数局部有界时，取完整步 $\lambda=1$ 仍有局部二次 Newton 收敛：普通 Newton 的新误差是旧误差平方量级，而 (13) 相对普通步的差是 $O(\|\dot y\|^2)$，仍为同一量级。该局部命题不保证当前远离根的 warm 收敛，也不保证原程序只试10档二幂步长就一定找到可接受步。

实际接线只需把 trial 构造改成 `retractTrial(states,cor.delta,lambda)`，后续仍调用同一个原 `evaluate(false)`、同一个残差范数和同一个接受准则。原 correction/Jacobian、最终边界、目标 H、物理 profile、N 与 floor 都不动。

## 5. node0 的 portRatio 是坐标变换的一部分

当前保存节点0采用外端口动量规范。其真实引擎输入使用 cell0 的最后 profile，x=1。设 $r_p=\texttt{cell0.portRatio}>0$，则送入 root 的坐标与方向必须同时满足

$$
\pi_{engine}=r_p\pi_{stored},\qquad
\dot\pi_{engine}=r_p\dot\pi_{stored}.
\tag{15}
$$

完成回缩后，再将新 $\pi_{engine}$ 除以 $r_p$ 保存。Q 不缩放。对 node i>0，使用 cell i−1 的第一个 profile，x=0，没有这一额外比例。

这是一个固定可逆对角线性坐标变换；将它放在 (13) 两侧，导数恒等仍成立。只缩放 state 或只缩放 direction 会破坏 (8)，不能视为等价实现。

准备回缩需要该节点的 root。尤其原 residual 的某种实现未必先在边界 node0 上调用 root；若新增准备阶段在此失败，只能记录为“trial 坐标构造失败”，不能倒推原 $\mathcal F$ 无定义或原轨道不是正分支。生产 hook 把准备和每步回缩都放在原 trial 的 try/catch 内，独立报告 node/cause，不把它伪标为某个 RK stage 的 ODE 失败。

## 6. 完整正域凸，不等于消均值后的域凸

固定物理节点以及一个 $0\le f<1$ 的检查 floor，完整 $(Q,L_0,L_h)$ 空间中

$$
S>f,\quad D>f,\quad A>f
$$

的允许域是凸的。对每个角，P、T、K、L 都是这些系数的仿射函数，而条件等价于

$$
|P|<\sqrt{(1-f)/W},
$$
$$
(1+K)^2+EP^2<(E-f)/W,
$$
$$
1+L+WT>f.
\tag{16}
$$

这些分别是开条带、开椭圆柱和开半空间的逆像；对所有角点或全圈取交仍凸。

但是本回缩不把 $L_0$ 当作自由直线变量：它在每个 trial 重解 $\mathcal M_0=0$。这一非线性均值图与完整凸域的交投影，不能仅由 (16) 推出凸性。因此不能声称 raw 直线自动保正，也不能声称回缩总比动量直线有更大 A。最终是否可接受，仍由该 trial 自己的原完整残差/branch 检查决定。

## 7. 均值初猜必须贴近当前均值分支

原 `initializeFromRaw` 每次从 $L_0=0$ 启动均值 Newton。这不影响它成功时所解的方程，但可能让第一步就在 branch 检查处拒绝，即使目标 raw 数据附近确有另一 $L_0$ 的允许根。特别是把 $\lambda=0$ 单独返回原 state，并不能据此宣称“任何小非零步的实际初始化都已连续”。

本次可直接使用的 v2 初始化只把起点改成

$$
L_0^{guess}=L_0+\lambda\dot L_0.
\tag{17}
$$

由 (8)，这与实际均值函数的 Taylor 一阶式相同，因此

$$
\mathcal M_0(Q(\lambda),L_0^{guess},L_h(\lambda))=O(\lambda^2),
\qquad
L_0^{true}(\lambda)-L_0^{guess}=O(\lambda^2).
$$

基线有严格分支间隙时，(17) 在足够小步内也处于同一允许域。标量均值导数 $B_{00}>0$，故标准局部 Newton 论证适用：在一个导数下界为正、二阶导数有界的邻域内，误差递推由 Taylor 公式给二次上界，足够近的起点收敛到唯一均值根。这里改变的是该同一方程的数值起点。

v2 保留原30次均值迭代、20档二幂回退、$8\cdot10^{-14}$ 相对停止阈值、原 $A,D,S$ floor 和相同动量投影。它没有降低 floor，也不将未收敛均值当作真实 root。v1 的默认零均值版本仍保存，绑定已经执行的第一个报告。

实际文件与入口：

- [方向与原零均值 helper](../scripts/78718-tail-geometric-newton-retraction.mjs)，6698 B，SHA256 `cb1bce1fc95af367db28326349997bedc0e0f7a486acc9a2ed6836d159fc1847`。
- [推荐的预测均值 v2](../scripts/78718-tail-geometric-newton-retraction-v2.mjs)，5457 B，SHA256 `2236a56fbd02d85888fe91f9dcfb094c16708fab97f1858f26026584c7fd1200`。

`createGeometricTrialHook(cells,{spacing})` 返回 `retractTrial`。对同一个 `states/cor.delta` 对象，只准备一次各节点方向，其后各二幂 trial 复用它。也导出单节点及全 shooting 的 `prepare...`/`step(lambda)`，可以只研究指定节点。模块导入本身不更改其他类或运行任何求解器。

## 8. 旧 W22 trial8/9 的真实固定节点比较

实际输入是 fast02 首次 W22 bootstrap 的保存 trial8、接受 trial9 的 iteration1 快照，以及同一个原 M15 尾 seed。只在 stage35/node36 重建原几何 warm；由

$$
\dot y=\frac{y_{trial8}-y_{warm}}{1/256}
$$

恢复该节点原 Newton 方向。它给出的 $1/512$ 直线步与实际保存 trial9 的最大坐标差仅 $2.22045\cdot10^{-16}$，因此这不是另选的一条改善方向。

在该节点 x=0、r≈0.473823542，原 warm 的 A 最小值约0.2025278781。比较结果为：

| 原方向的步长 | 原动量直线 A | Q/L 回缩 A | 原 floor .05 下的本节点情况 |
|---|---:|---:|---|
|1/16384|0.1994110090|0.1994111924|两者均通过|
|1/2048|0.1775819206|0.1775943523|两者均通过|
|1/512|0.1025425664|0.1027932150|两者均通过|
|1/256|0.0014904603|0.0030570586|两者均低于 .05；本 trial 仍不能接受|

末行两个 A 都是在独立局部诊断所用的 $10^{-10}$ floor 下真正求得，**没有**把这项较低 floor 接进当前生产。原 floor .05 的两个计算均如实拒绝。v2 回缩在末行用了2次均值 Newton，均值残差约 $5.20418\cdot10^{-18}$；再按其投影动量调用完整 root，回到同一正根。

对从 $1/16384$ 到 $1/256$ 的这些步，实际

$$
\|y_{retracted}-(y+\lambda\dot y)\|_\infty/\lambda^2
$$

在约17.2846至17.2906之间。它与 (13) 的二阶差一致，但有限观测本身不是二阶定理的证明；证明已经在第4节完成。这个数使用归一动量 state 的单位，不能作为曲面 metric 误差。

在 node0 还比较了“先乘 portRatio 在 engine 坐标回缩”与“由 helper 在 stored 坐标回缩再乘回”的同一计算。实际 portRatio≈6.7271713220，两种存储归一的最大浮点差约 $5.68435\cdot10^{-14}$；这是 state 数值换算差，不能当作物理坡度或 metric 差。

两次实际执行均没有 RK 步、ODE 轨道、shooting 残差评估、DN 或 BVP：

- v1：`1de53b/session84292 → b64bea exit0`，约4.007秒。末行在 `initializeFromRaw` 的零均值初猜处拒绝，即使放低 floor 也未到真正均值根；不能据此说均值根不存在。
- v2：`f63ce2/session51425 → 2a8976 exit0`，约3.412秒。预测均值起点消除了这一初始化伪拒绝，并得到上表的真实低 floor 正根。

首次 v1 启动曾因未设置现有 `CLOSING_TAIL_CACHE` 环境入口而在导入时 exit1；随后使用本题已有 `repro/source-root` 的实际依赖成功执行。没有据此拉取完整仓库或另开数学求解。

可复现程序和报告：

- [v1局部程序](../scripts/78718-tail-geometric-retraction-research.mjs)，6948 B，SHA256 `30807e2d4bb5dea5c114d363d80b2890a38453369f80c37108119eca7c2510f6`；[v1报告](../notes/2026-11-10-78718-tail-geometric-retraction-research-01.json)，16784 B，SHA256 `5b2e8da697e42200e58cc77f792c1a8b9f856e71e8bfcace79707b31bfe366e0`。
- [v2局部程序](../scripts/78718-tail-geometric-retraction-research-v2.mjs)，7035 B，SHA256 `685912c13791232bb9f747c1bfac0fe024eb9d6975df058af54d87738b1a3e67`；[v2报告](../notes/2026-11-10-78718-tail-geometric-retraction-research-02.json)，17937 B，SHA256 `9786c1f7397c5597436dc18a8c528f1e984dac72d698c67df27838758f05c8b7`。

因此当前已经实际确认：回缩会改变失败步的二阶几何轨迹，且均值起点必须处理正确；但这个具体大步仍不能跨过原 .05 floor。是否对完整 shooting 残差、其余节点或后续 H 延拓有帮助，须由保持原方程的真实下一计算回答。本文没有把局部正根或坐标重参数化支付为本题 G5 或闭曲面完成。

## 9. 零方向仍有浮点 roundtrip 偏置：实际定位

后续 fast05 在原 floor .05 下从冷 H/8 初猜下降至归一残差约 $3.336601164\cdot10^{-9}$，但十档回溯未达到原 $2\cdot10^{-9}$ 要求而自然停止；没有产生 prefix inner 图。为定位小步不再下降，取它自己保存的 iteration3/node12、node13，只执行本节 v2 的 `prepare` 后 `step(1)`，把全部 Newton 方向准确置零。**没有调用 `step(0)` 的直接返回分支**。

输入是 `notes/2026-11-10-78718-numerical-m15-w22-fast-05-iteration3-root-diagnostic-input.json.gz` 的原保存节点。两个节点都维持原 W22/N512、原物理 profile 和 .05 floor。实际得到：

| 节点 | Q 偏置 | 最大 $|\Delta\pi|$ | 高频半部最大 $|\Delta\pi|$ | 原 root 相对残差 |
| --- | ---: | ---: | ---: | ---: |
| 12 | 0 | $1.7763568394\cdot10^{-15}$ | $1.6515570134\cdot10^{-18}$ | $1.6508452209\cdot10^{-16}$ |
| 13 | 0 | $2.2204460493\cdot10^{-16}$ | $9.9030433044\cdot10^{-19}$ | $9.1934103534\cdot10^{-17}$ |

“高频半部”指此 M22 state 的后11个动量槽，所含频率为36至66。最大整体偏置都在频3。完整有符号逐分量差保存于报告，不把上述坐标差当作 metric 误差。

node13 的原 $L\to raw\to L$ 逐分量完全不变，node12 的最大差仅约 $2.02\cdot10^{-28}$，且两处均值都不变。直接把原 root 已有的 moments 投影回动量，已经产生几乎相同的差。因此这项偏置存在于浮点逆 root 与正向 moments 的 roundtrip；不能只归咎于均值求根阈值或 raw 缩放。

原节点 $y$ 的实际浮点 root 并不要求正向投影逐位等于 $y$。v2 把重新投影值绝对写回，因此即使方向为零、$\lambda$ 非零，这个与 $\lambda$ 无关的偏置仍会进入后续原残差。只在 $\lambda=0$ 返回原节点不能消去该问题。

首次诊断在输出脚本身份时把 `file:` URL 字符串当作普通路径，`e1840e/session43595 → 78ba81 exit1`，未形成成功报告；修正该输出处理后 `b5a5e5/session19888 → d74cee exit0`，约2.734秒。实际数学计算只有这两个节点的 root/mean，无 ODE、RK、DN、BVP 或完整 shooting 残差。

程序：[零方向诊断](../scripts/78718-geometry-retraction-roundtrip-research.mjs)。报告：[两个节点的真实差](../notes/2026-11-10-78718-geometry-retraction-roundtrip-01.json)，19,497 B，SHA256 `a362888d83a83af9c0fb6cfc445f7a91d9de6871224a28a122fcb55768e20287`。

## 10. 中心差分实现：实数等价、浮点零方向准确固定

固定一个节点。用 $D$ 表示 stored 坐标到 engine 坐标的线性归一：通常 $D=I$；node0 的动量块乘原 `portRatio`，Q 块不变。令 $\chi$ 为第3节中准确的 canonical-to-raw 局部坐标，$C=\chi^{-1}$ 为解准确均值后投影回 canonical 的逆坐标。对当前节点和原方向写

$$
z_0=\chi(Dy),\qquad
\dot z=D\chi(Dy)D\dot y,\qquad z_\lambda=z_0+\lambda\dot z.
\tag{18}
$$

原准确回缩是 $D^{-1}C(z_\lambda)$。定义中心式

$$
\widehat R_y(\lambda\dot y)
=y+D^{-1}\bigl(C(z_\lambda)-C(z_0)\bigr).
\tag{19}
$$

**准确等价证明。** 第3节已经在允许分支内证明 $C\circ\chi=I$，故 $C(z_0)=Dy$。代入 (19) 得

$$
\widehat R_y(\lambda\dot y)=D^{-1}C(z_\lambda).
\tag{20}
$$

所以这不是更换原残差、Newton 方向或数学 trial 曲线。第4节的 $y+\lambda\dot y+O(\lambda^2)$、同一方向的下降和局部二次 Newton 结论均不变。该证明需要准确局部坐标成立，与实现是否精确反演浮点 moments 是两个层次。

**浮点实现。** 新名 [centered-v3 helper](../scripts/78718-tail-geometric-newton-retraction-centered-v3.mjs) 在准备该次 Newton 时，额外保存一次与实际 trial 完全相同转换方法得到的 $\widetilde C(z_0)$。每次 trial 仍按 v2 的原均值方程、预测起点、30次迭代、20档回退、$8\cdot10^{-14}$ 阈值及原 floor 求 $\widetilde C(z_\lambda)$，但写回

$$
\pi_{trial}=\pi_{base}+
\frac{\widetilde C(z_\lambda)_\pi-
      \widetilde C(z_0)_\pi}{\mathrm{portRatio}}.
\tag{21}
$$

两个 engine 动量先相减，**随后才除一次原 portRatio**；不能各自变换后再次乘回。Q 保持原 $Q+\lambda\dot Q$，其它附加状态也保持原直线。方向与转换增量为零时保持原 binary 值，连 signed zero 也不重写。

当 $\dot y=0$，程序确实执行 trial 的正向转换；两次输入的 raw 与均值初猜相同，确定性运算得到相同的 $\widetilde C$，所以 (21) 的差准确为零。这消掉了 §9 的零方向偏置。它没有证明任意非零极小步的舍入误差为零，也没有证明病态前向 flow 的误差自动可控。

**必须保留的实际检查。** 在浮点中，(21) 输出的动量一般不逐位等于单独 raw trial 产生的 $\widetilde C(z_\lambda)_\pi$。因此 raw 构造时的正性不能代替随后对中心输出调用原 `evaluate` 时的真实 root/branch 检查；中心输出可能被原方程拒绝。新 helper 不修改原 F、Jacobian、Newton correction、容差或接受条件，也不把构造成功视为残差成功。构造异常仍由原 trial try/catch 如实报告。

新 helper 保持同一个 `createGeometricTrialHook`/`prepare...`/`step` API；只作为另名选择供后续 worker 使用，不修改已有 v1/v2 源或任何保存候选。

### 10.1 新 helper 的真实零方向检查

实际运行新的 [中心实现诊断](../scripts/78718-geometry-retraction-centering-research.mjs)，对同一 iteration3 的 nodes0、12、13 执行 $\dot y=0,\lambda=1$。三个新 helper 输出都经完整 Float64Array 字节比较与原保存节点一致；node0 使用了它自己的真实 portRatio，未以 ratio=1 替代。原 v2 在 node0 的最大动量偏置约 $1.77636\cdot10^{-15}$，新中心输出为零。

真实回执 `59fe85/session56827 → 1850d0 exit0`，约2.768秒；仍为0 ODE、0 RK、0 DN、0 BVP、0 shooting 残差评估。[报告](../notes/2026-11-10-78718-geometry-retraction-centering-01.json) 28,401 B，SHA256 `c51526a45c8711e338aa3549517c527cb9939191614c59a566eb7951f23450b9`。

这些节点偏置是否足以解释 fast05 的残差停滞，必须另用同一离散 stage 的实际 flow/Jacobian 比较。这里不把“零方向逐位固定”当作完整 shooting 收敛、原 H 延拓成功或本题 G5 完成。

### 10.2 同一 stage 的实际放大量

随后研究代理对同一保存状态的 stage12，只执行一次 base 的 flow/Jacobian 和一次零方向 roundtrip 节点的实际 flow。输入为 node13，目标为 node12；原 P8/S32 子步序列、W22/N512、.05 floor 和原 root 保持不变。这不是新的 shooting 解或另选方向。

若原 stage 映射为 $\Phi$，原残差为 $r=\Phi(y_{13})-y_{12}$，保存的零方向偏置为 $b_{13},b_{12}$，比较的是

$$
\Phi(y_{13}+b_{13})-(y_{12}+b_{12})-r
\quad\hbox{与}\quad
D\Phi(y_{13})b_{13}-b_{12}.
\tag{22}
$$

原归一尺度为 $0.0006419043268729995$。真实浮点结果是：

| 量 | 归一值 |
| --- | ---: |
| 原 stage 残差范数 | $3.3366011642270125\cdot10^{-9}$ |
| 零方向 roundtrip 后的 stage 残差范数 | $3.990094933515230\cdot10^{-9}$ |
| (22) 左侧实际差的范数 | $1.0814705032998263\cdot10^{-9}$ |
| (22) 右侧一阶预测的范数 | $1.2937064471963820\cdot10^{-9}$ |
| 实际差与一阶预测之差的范数 | $2.122359438965558\cdot10^{-10}$ |

因此零方向的坐标转换偏置已经在这条实际 stage 中产生与停止残差同量级的污染；这比单看节点的 $10^{-18}$ 高频差更有辨识力。这里仍是浮点定位，不是完整 flow 误差区间证明。一阶预测没有被当作实际非线性差。

该偏置的 Q 块准确为零。相关动量到动量块 $D\Phi_{\pi\pi}$ 的最大元素约 $1.970607\cdot10^6$；不能把约 $2.42110\cdot10^{13}$ 的 $D\Phi_{\pi Q}$ 最大值错误乘上动量偏置。报告分开保存四个块及频63贡献。

真实回执 `5a3873/session45893 → 544d27 exit0`，约3.086秒，2次单 stage flow、0完整 shooting、0 BVP。完整报告为 [stage12 偏置传播](../notes/2026-11-10-78718-tail-retraction-bias-stage-flow-01.json)，7,749 B，SHA256 `1faca30bc9249f0b0f8bffc8bb904ccb5f47c510c0416a98431c79f2131998ce`；同 stem 的 `-base-jacobian.f64.gz` 保存真实完整 Jacobian 与原输出，15,662 B，SHA256 `4f477ea21c3e1d98edd1dc76cf3346676a3a809eb49a68a0bef6cec321d61da9`。

centered-v3 在这两个零方向节点返回原字节，故这个特定零方向污染项消失；原 base 残差本身仍约 $3.34\cdot10^{-9}$，不会因此自动满足原容差。后续真实 Newton、H 延拓及最终 G5 必须分别完成。
