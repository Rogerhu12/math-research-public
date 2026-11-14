# 2026-11-14 来源核对：定义、已有对象与可复用接口

核对者：`repo_sources`；全部结论按原文范围记录，不把数值前缀、条件引理或微小精确解当成本课题完成。

公开仓库读取基准为 `ee26c0a65a2e63c15f2ccfba6714181584416542`。以下仅以该公开提交中真实读取的 Markdown 为依据；没有下载网格或大数组。其他来源核查保留在公开工作树以外，未纳入公开提交。

## 1. 不可混用的量

来源：`topics/visible-flexible-closed-surface/README.md`。

- $D=\operatorname{diam}F_0(M)$，是完整初始闭面直径。
- $H$ 是闭子集，可不连通，但有内点、$\operatorname{diam}F_0(H)\ge .2D$，并且 $F_t|_H=F_0|_H$。
- $\delta_{\rm hold}=\max_t d_H(F_t(M),F_0(M))$，不作刚体对齐；**材料点在同一像上滑动完全不计**。
- $\delta_E=\max_t\min_{A\in E(3)}d_H(AF_t(M),F_0(M))$，包括反射。
- reach 必须覆盖完整闭面和全部时间；主曲率半径只给局部必要信息，不能代替全局法向单射半径。
- 同一度量、参数与时间范围下增加数值分辨率才是本题要求的精化；改变层数/尺度比/背景度量压小固有误差不算。

## 2. 已有闭族状态

| 来源 | 实际已报告范围 | 对本课题的限制 |
|---|---|---|
| `visible-flexible-closed-surface/results/R114-actual-noncircular-repair-to-original-tolerance.md` | 固定原 $g$、全域全时 metric $\le1.2566772507606437\times10^{-9}$；$D\le3.787020263961937$；reach$/D>.03120330942723168$；held$/D>.05278322519892998$；$\delta_E>0$；三个完整网格 | 原文明确 `exact_isometric_family_proved=false`、`infinite_refinement_convergence_proved=false`。只给有限加密降至原 $2\times10^{-9}$ 容差的证据；幅度远低 .3 |
| `visible-flex-larger-amplitude/HANDOFF.md` 和 `open.md` 的 true A | 三个完整网格，$D_{cloud}=3.9774592667$，九相位最大点云 Hausdorff $.2506381375$，比值 $.06301463338$ | 点云与有限相位不是全部连续几何证明；全连续 reach 仍有未覆盖对/预算缺口；幅度远低 .3 |
| 同一 larger-amplitude 的新球核心/free3 | 实际接受到 $s=.99$，M96；核心 $G\simeq .96$，前缀直径样本约 $3.50037$；完整材料 DN 和尾闭合仍在做 | 是前缀，不是新的完整闭族。不能把该核心幅度除以仅前缀直径后当完成 |
| `visible-flex-exact-nearby/HANDOFF.md`、`open.md` | 固定最后中心有完整部分残差、有限逆/帽矩阵/相位计算；明确“主目标未完成” | 尚欠全频全源全 mean 逆、真实共轭/Schur、完整非线性 $F=0$ 与最终闭几何；不能把条件预算当严格精确闭族 |

R114 的完整对象清单：
`visible-flexible-closed-surface/notes/2026-11-12-fd2d-metric-m12-repaired-closed-map-v2.json`，SHA256 `7cc24cf74d61da9415e3b63b460c5ed1af4681974c6ee84b31771e4facf519bc`。
其底图先经 $Y=X\circ\Phi$ 的全局材料微分同胚修复，活动片再用
$$F_t=R_{\alpha(t)}\circ Y\circ\tau_{-\alpha(t)},\qquad \alpha(t)=2\pi t/3.$$
固定帽逐点不动。$\Phi$ 不必与 $\tau$ 交换；同像集几何可以精确转移，但材料点轨迹不同。纯活动核心的像只是刚体旋转，$\delta_E=0$；完整固定破轴帽是非全等性所需的一部分。

## 3. 已存在的可直接复用数学模块

### 3.1 强中央平面核及正分支演化

来源：`visible-flexible-closed-surface/results/R115-fixed-perimeter-elliptic-support-core-family.md`、`R29-c3-mechanism-interface-and-convex-held-envelope.md`。

支撑函数 $h(\phi)$ 给
$$\rho=h+h''>0,\quad \Gamma=h n+h't,\quad \sigma(\phi)=a_0^{-1}\int_0^\phi\rho.$$
在材料角下 $|\gamma_\sigma|=a_0$；柱段 $X(s,\sigma)=\gamma(\sigma)+s e_z$ 精确诱导 $ds^2+a_0^2d\sigma^2$。零均值支撑修正保持周长，改变核心形状不必改变共同材料度量。

R115 的明确椭圆基准 $A=1.4,B=.5$ 给 $\rho_{\min}=5/28$；其带修正窗口给中央支持差 $A_p-B_p\ge .902$、曲率半径 $\rho\ge1061/7000$。这已经是强局部几何，瓶颈主要在完整闭合。

现有 Frenet 正分支方程为
$$F_s=\alpha N+\beta B,\quad \alpha=-\frac{a'}{a\kappa},\quad \beta=\sqrt{1-\alpha^2}>0.$$
其前提 $|a'|<a\kappa$ 涉及角圈的**最小**曲率，和 reach 所限的最大主曲率不同。越来越扁的凸核可能使最小曲率很小，过渡所需高度反而上升。该方程的完整无限维解存在和实际尾匹配不能从有限 ODE 存在自动推出。

### 3.2 精确平坦弯尾，已有全非线性端口

来源：`visible-flexible-closed-surface/results/R128-exact-flat-developable-tail-with-fixed-collar.md`。

取奇函数 $\alpha(y)$ 在 $|y|\le c$ 恒零、$|\alpha|<\pi/2$，定义
$$X'(y)=\cos\alpha(y),\quad Z'(y)=\sin\alpha(y),\quad X(0)=Z(0)=0,$$
$$F(r,u)=(r\cos u,X(r\sin u),Z_c-Z(r\sin u)).$$
则准确 $F^*e=dr^2+r^2du^2$，$r\le c$ 的开圆领固定；相位 $R_\theta F(r,u-\theta)$ 仍同度量且逐点固定圆领。主曲率为 $0,\alpha'(y)$；平面投影单射给真实环带嵌入。

这一模块已包含完整位置、标架、六项二 jet 及参数导数。原文实例 $r_c=.32,c=.34,a=.8,A\le1.2$ 给曲率峰 $\le4725/736$。它只是有边尾，不能直接替换旧非平尾度量，不能从此推导未知核心或完整闭面的 reach。

实现：`visible-flexible-closed-surface/scripts/fd2d_flat_developable_tail.py`。若尝试新构造，优先调用这条准确尾而非重新做薄缺陷近似。

### 3.3 显式精确可弯鞍环已经存在

来源：`visible-flexible-closed-surface/results/R44-explicit-flexible-ruled-saddle-annulus.md`。

令球面曲线 $d(u)$ 单位速率，$c'=b d\times d'$，则 $F(v,u)=c(u)+vd(u)$ 诱导
$$g=dv^2+(b^2+v^2)du^2.$$
文中给实际闭合中心圈、四个约束的隐函数族、固定三片及严格非全等性。然而这是有两个边界的环带，$K=-b^2/(b^2+v^2)^2<0$，不能直接 $C^2$ 接内蕴平帽；有效大参数区间和 .3D 像位移均未给出。重新得到同一局部方程不会突破本题。

### 3.4 共同材料度量与闭合接口

来源：`visible-flex-larger-amplitude/results/R240-canonical-material-metric-and-refinement.md`、`R239-material-cut-mean-and-planar-matching.md`。

固定 $a(s)$、常数周长与材料角后，核心法向角系数可以随加密调整：
$$g_c=ds^2+a(s)^2\rho_c(\phi)^2d\phi^2,\quad \theta=\Phi_c(\phi),\quad \Phi_c'=\rho_c,$$
$$Q_c^*g_c=ds^2+a(s)^2d\theta^2.$$
只有改变 $a(s)$ 才实际改变该共同材料目标；不能把非线性角变换径向不变地延到帽心而默认光滑。

R239 的闭合条件包括：完整材料高度、完整非均值斜率、同一正分支及投影 turning number。满足它们可推出均值唯一、单个平面刚体配准以及非特征 Darboux 分支下的完整 Cartesian 六 jet 一致。有限截频行相等不能自动代替完整函数相等。

## 4. 对新机制工作的具体建议与证据边界

以下是从来源差距作出的研究建议，不声称已经得到新解或已证明文献从未尝试。

1. **把真正的闭合端口作为优化变量。** 单独把椭圆加扁、提高中央支持差不够；已有核已给约 .9–.96 的绝对差。新方案需要降低完整封口/过渡对直径和见证球的代价，并保留精确平坦尾或另一已解尾的完整二 jet。
2. **若继续相位机制，先做完整包络预算。** 两个固定帽可共同充当不连通 H；无须让每一个帽单独达到 .2D。见证点到所有过渡和帽的距离都必须计算，不能只用中心圈支撑差。
3. **优先考察改变拓扑或非正 Frenet 分支的闭合。** 当前主要对象是两帽的球面型正分支。环面/多边界模块或允许空间回折的过渡可以作为真正不同的搜索空间，但目前没有精确闭合证明，也不能免费继承旧 reach。该项只是待验证路线。
4. **保留材料与像的区别。** 对完整闭面仅作自等距重参数化时所有像相同，held=0；相位加空间旋转只有在固定区域真正逐点静止时才给本题握持族。新的“长杆放大”必须展示像位移和可变相对位姿，不计标签速度。
