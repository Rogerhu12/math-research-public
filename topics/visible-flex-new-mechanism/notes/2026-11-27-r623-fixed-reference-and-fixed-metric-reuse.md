# 后继 97q 的固定几何参考、全相位和固定度量边界

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
状态：**下述复用规则是已证公式的直接推论与源码身份核对**；没有新科学执行，
没有把 59a4 的非圆范数移给 3bc1，也没有产生一个新的完成候选。

本文接 [59a4 的完整连续几何](2026-11-27-r623-current59a4-complete-reach-original-terminal.md)、
[当前 3bc1 原终态](2026-11-27-r582-normal311-original-terminal.md)、
[R604](../results/R604-normal-chord-stability-and-finite-parametric-norm-interface.md)、
[R622](../results/R622-longer-intrinsic-near-pairs-and-same-bound-reach.md) 和
[R33 的相位组装](../results/R33-elliptic-core-reach-and-reflected-phase-budget.md)。
相位组装、宏观预算和“改变 p 是设计而非等距变形”已有记录，本文不重新登记这些结论。
这里补清可实际减少后继费用的共同参考身份及固定 g 接口。

## 1. 可以固定已认证的圆参考，不必随每个新 mean 改它

把原 59a4 完整计算中的**圆比较面**记为 $G_*$，其已付结论为

$$
\rho_*\ge .060719999999999955,\qquad D_*\le1.6006822133969527.
$$

这里 $G_*$ 不是实际非圆面 $X_{59a4}$。它使用 59a4 的 `q[64:80]` 和 q96，
圆核心半径仍为 `.38`，角切向为圆切向。其全核心、中央柱、紧段、无限振荡尾、
完整 Cartesian 两帽及镜像均已接 R608/R599；因此能独立保留这个固定面的全域结论。

对未来候选 $X_q$，只要实际重新证明

$$
\sup_M|X_q-G_*|\le\delta_q,\qquad
\sup_M\|d(X_q-G_*)\|_{g_*}\le\alpha_q<1,\qquad
\sup_M\max_i|k_i(X_q)|\le K_q,\qquad g_*=G_*^*e,
$$

即可用相同的 $\rho_*,D_*$，以及新的 $\lambda_q=1+\alpha_q$、$\nu_q=\alpha_q$，
接 R604 或 R622；$D(X_q)\le D_*+2\delta_q$。参考自身的完整认证无需重做。
即使新的均值高度不再单调，$G_*$ 的 R599 前提仍是同一个已付事实；
新面能否由这些范数证明嵌入，取决于新的完整界及近远弦条件。

原 59a4 的 $\delta,\alpha,K$ 只属于它的实际 q / 材料。
3bc1 的全部16个 mean spline 系数以及帽高已经改变；其帽高为
`.6975711972395291`，而 $h_*=.6967930185437883$。
这条源日志事实说明它不能拿旧差值界直接代入。本文没有新算它相对于 $G_*$ 的范数。

## 2. `reference_q` 的完整依赖，及两种 reference_alpha

源码为
[`r582_same_field_mean_intervals_20261127.py`](../scripts/r582_same_field_mean_intervals_20261127.py)
和 [`r582_same_field_radial_intervals_20261127.py`](../scripts/r582_same_field_radial_intervals_20261127.py)。
调用 `SameFieldMeanGeometry(design, height_provider, reference_q=literal_59a4_q)`
可以表达上面的固定参考。**仅给 q 字符串不是完整参考身份**；必须同时固定下表。

| 固定部分 | 本次 $G_*$ 的准确含义 |
|---|---|
| 参考 mean 参数 | 97q SHA `59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45` 中的 `64:80` 与 q96；其余80个角/尾坐标不进入圆参考 |
| 径向坐标及接合 | 原 `L=.9, C=.036, CORE_HALF=.02, RC=.22`；`BACKGROUND_END=L-.08`；同一个 `[0,L]`、中央柱、镜像与 Cartesian 帽参数化 |
| 圆核心 | `design.reference_core_radius=backend.original.CIRCLE_RADIUS=.38`，不是当前 rounded ellipse 的周长半径 |
| 自由 mean 基 | 原 degree-5 spline、原 binary64 knot 序列、原 $4\chi(1-\chi)$ envelope，参数化宽为 $L-C$ |
| 固定 bump | 原左右口 `.06,.80`，同一个准确 flat bump，`mu=-.040019082162222074`、`nu=-.048942275258064924` |
| 完整高度尾 | 原 `AMP=.1, ELL=.2` 及全部正 delta 上的解析积分 $H$，不使用材料数值零 suffix 代替；R611 v2 对象仅供同一积分的向外评价 |
| 角原函数与轴 | 圆参考直接为 $a_*e_r+z_*e_z$；真实非圆场用原唯一零均值周期原函数。原点、z 轴、中央反射平面和帽中心固定 |
| 源及原证书 | 使用该原 run 绑定的 mean/radial/R611/原 profile 链；参考证据指向 run `45909787850` / job `140215094495`，不能只保一个 rho 标量而改底层公式 |

令 $\chi$ 为固定背景步函数，$B$ 为原 compact bump，$S_\alpha,S_z$ 为参考两 spline，
参考的完整定义是

$$
a_*(s)=\{(1-\chi(s))\,.38+\chi(s)(RC+L-s)\}
          \exp(S_\alpha(s)+\mu B(s)),
$$
$$
z_*(s)=(1-\chi(s))(CORE\_HALF+s)
       +\chi(s)(h_*+H(s))+S_z(s)+\nu B(s).
$$

原开 core 上取相同的准确常数/直线延拓。两完整帽是 $z=\pm h_*$、半径 RC 的盘。
这些公式及它们的二 jets 构成固定参考；求积精度变化只改善同一个 $H$ 的包围。

逐调用链可见：`SameFieldMeanGeometry.boxes` 的 reference 半径只取
`design.reference_core_radius`；`design.background_jets` 只读取固定 C 和
BACKGROUND_END。参考 mean 不读取 `design.p`、`epsilon`、Hermite A/C、当前
`current_core_radius` 或当前角自由参数。它检查实际 Hermite 的时钟不使这些数据进入参考公式。

两处同名属性必须分清：

- `mean.reference_alpha` 来自传入的 59a4 mean，只定义 $G_*$。
- `design.reference_alpha` 始终来自旧 `backend.Q[64:72]`，与旧 reference_mu、`.38`
  一起定义材料 seed 商的原冻结半径。传入新的比较面不会改它。

因此，在上述全部源/常数/坐标不变时，改变当前 p **不会暗改 $G_*$**。
同 p 的邻近 q 可以直接使用这个参考接口；每个新 q 的全部 C0/C1/K 仍须新付。
若 p 改变，新 rounded core 的完整角界、准确周长半径及角 jets 必须按新 p 支付，
旧 p 的 core 界不能复用。若 L、RC、core 高度、背景区间、primitive 规范或反射轴改变，
则原同材料对应和上表不再自动成立，不能靠 `reference_q` 一个参数声称参考仍相同。

候选帽高变化没有平移 $G_*$：当前帽是 $\pm h_q$，差为
$\delta_{\rm cap}=|h_q-h_*|$，同一盘上的导数差为零。把当前帽单独平移回旧高度
会修改候选，不能用这种操作偷消 C0 差。实际材料 hash 变化也不改变这个圆参考，
但新非圆场所有依赖材料的界与物理资格必须针对同一次构造对象重新支付。

## 3. 这是近邻参考；不能覆盖整个宏观设计阶段

原完整材料 hash 已包含 `knots || (A,A_s,A_ss,C,C_s,C_ss)` 的全部 binary64 端点，
而不是仅节点位置。同源下相同 hash 对应同一数学 quintic 场。
对新 q 的实际场观察可以沿用相同数学材料定义；原端点数组/积分 prefix 没保存而必须再生时，
再生仍完整计费。未得到同一个材料时不换标签、不移旧非圆界。

固定 $G_*$ 的优势限于近邻：R604/R622 均要求 $2\delta_q<d_*<2\rho_*$。
原宏观设计目标 p=.8、minor=.18、offset=.2 的 core 点为 $(1,0,z)$；
同一材料角下固定圆参考为 $(.38,0,z)$，所以 $\delta_q\ge .62$。
这不可能满足本参考已知 $\rho_*=.06072$ 的必要阈值。
因此未来升 p 后若共同参考门失效，必须用真实的新参考/一般非圆参考或完整点对方法继续，
不能只不断细分旧圆差值盒。这个判断不是对宏观曲面的排除。

R604 本身允许任意已认证 $C^2$ 闭参考，故以后可把一个真实新非圆候选作为下一参考。
届时还需相对于其真实诱导度量、法线和同材料坐标的范数接口；目前旋转参考 frame 代码
不因换一个 rho 标量就成为该一般接口。本文没有新建这项计算，也没有授予待构造参考的资格。

## 4. 全部相位不要求新的时间网格

对一个已经完整定义的实际闭 $C^2$ 场 $X$，令 $\tau_\phi$ 是材料角平移，
在两帽中心按平面旋转光滑延拓；$R_\phi$ 是同一轴的环境旋转。定义

$$
F_t=R_{\phi(t)}\circ X\circ\tau_{-\phi(t)},\qquad
\phi(t)=\pi t/2.
$$

这使用 R33 的同一个组装。当前帽并无正宽度冻结 body 圆环：`cap_collar_width=0`，
全部自由列一直定义到 L；其真实全平二 jets 接完整开圆盘，不能把数值零 seed suffix 当成圆领。
这些已经证明的 C2 接合足以使上述材料旋转在整个 M 上有定义。盘内每个材料点全程固定。
复合微分同胚与环境等距直接给

$$
F_t(M)=R_{\phi(t)}X(M),\qquad
\operatorname{reach}(F_t(M))=\operatorname{reach}(X(M)),\qquad D_t=D_0.
$$

紧面上的角平移在 C2 拓扑连续，所以 $t\mapsto F_t$ 连续。这里的全时间几何事实
不要求先把 metric 残差降到零；等距资格另由一个固定旋转不变 g 的全空间误差决定。
若 $\|g^{-1/2}(X^*e-g)g^{-1/2}\|\le\varepsilon$ 全域成立，同样的界准确传到全部 t。
因此今后的同一候选只需一次完整空间几何和连续 metric 证书；不应另起时间采样任务。

由已付 59a4 几何可以定义这一具体相位族并继承其空间 reach 和直径。
其 RC=.22 的固定帽盘直径为 .44，大于 $.2\times1.604583137587237$。
但这完全不支付大幅度：由于 $G_*$ 旋转等变，

$$
|R_\phi X\tau_{-\phi}-X|
\le |R_\phi(X-G_*)\tau_{-\phi}|+|X-G_*|\le2\delta.
$$

于是对整个像集的 Hausdorff 距离同样有 $\delta_{\rm hold}\le2\delta<.004$。
59a4 的真实 core 长直径 $2(.181+.2)>.76$，故这个已认证近圆相位族
$\delta_{\rm hold}/D<.006$。这是已有 C0 证书的直接纸上推论，无新场查询；
它说明小 p 面即使 metric 继续下降，也不能被包装成 README 的 $.3D$ 完成。
新 3bc1 尚无该 C0 证书，本文不把这个具体小幅上界移给它。
原 p=.8 / ball / strip 的宏观充分预算仍按 open.md 中已登记的 R565 范围推进。

## 5. 固定同一 g：必须固定完整函数，17个 mean 系数不够

当前 R582 实数表示是

$$
T=\frac{(-\sin(\theta+u),\ \cos(\theta+u),\ v)}{\sqrt{1+v^2}},
\quad X=a\,\mathcal P T+z e_z,\quad X_\theta=aT,
$$

其中 $\mathcal P$ 是**完整连续**零均值周期原函数。因此

$$
I_q=E_q ds^2+2a_q\widehat F_q ds\,d\theta+a_q^2d\theta^2,
\quad E_q=|X_{q,s}|^2,\quad\widehat F_q=X_{q,s}\cdot T_q.
$$

当前逆设计评价的目标为 $\bar g_q=\bar E_q(s)ds^2+a_q(s)^2d\theta^2$。
每步更改 q 后又取 mean，改变的是目标本身；有限 FFT / mean 数也不是完整连续目标的定义。
固定 17 个 mean 控制只固定 a/z；由于

$$
X_s=a_s\mathcal PT+a\mathcal P T_s+z_s e_z,
$$

角场及其径向导数变化仍改变 $\bar E_q$。这一点在原源码的 `ebar=eactual.mean_theta()`
及其完整参数导数中没有被删除。

未来一旦决定冻结某个设计，须明确固定一份连续

$$
g^{\rm target}=E_*(s)ds^2+a_*(s)^2d\theta^2.
$$

例如可由该设计的**固定实数场**和完整角积分定义 $E_*=\langle|X_{*,s}|^2\rangle$，
同时固定其 a；后续求积和加密只改善这些同一函数的评价，不重新选择它们。
完整定义包含该材料场、全部端点 jets / 原函数规范、q、p、mean、尾及源身份。
hash 识别函数的已付来源，但不把一组有限均值样本自动变成连续函数，也不使另一 mesh 成为同一目标。
必要的旧定义再生必须付费并满足身份；不能因当前实际场不同而把 E* 换成新 mean。

对新位置场相对于这个固定目标的真实归一误差矩阵是

$$
\begin{pmatrix}
E_q/E_*-1 & a_q\widehat F_q/(a_*\sqrt{E_*})\\
a_q\widehat F_q/(a_*\sqrt{E_*}) & a_q^2/a_*^2-1
\end{pmatrix}.
$$

若将 a 准确固定为 a*，右下角才恒零；上左项仍不得除以新 q 的 mean。
这是最短实际目标接口，包含角primitive/均值的连续误差与真实参数导数。
现有正常续算仍是逆设计，本文不改变它的算法或资格，也不称它已经开始固定 g 精化。

原 p 续接也不能被重命名为同 g 的形变。固定 minor=b=.18、offset=d=.2 时，开 core 有

$$
a_0(p)=d+\frac1{2\pi}\int_0^{2\pi}
\sqrt{p^2\sin^2\xi+b^2\cos^2\xi}\,d\xi,
\quad
a_0'(p)=\frac1{2\pi}\int_0^{2\pi}
\frac{p\sin^2\xi}{\sqrt{p^2\sin^2\xi+b^2\cos^2\xi}}\,d\xi>0.
$$

其 core 度量为 $ds^2+a_0(p)^2d\theta^2$，随 p 改变。
这只是原“设计续接”说明的显式公式，不是新等距障碍；本题实际形变参数是最终固定设计的相位。

## 6. 与 R618 的连接条件及最短未付输入

R618 已固定的是它自己实际397输入的
$E^{618}_*(r)dr^2+r^2d\theta^2$，包含原高度、真实连续 turning 根、canonical512、
原源/response 身份及全部核心/尾定义。它不是上述 59a4 圆参考的诱导度量，
也不是 3bc1 在当前有限 FFT 上的 mean。

即使在某段把 $r=a_*(s)$，也必须先证明 $a_*'\ne0$，并逐点匹配

$$
E^{618}_*(a_*(s))=E_*(s)/(a_*'(s))^2.
$$

当前 open core 有 $a_*'=0$，因此这个变换不能作为整个闭面的坐标等价。
原始材料面、核心与帽的图、同一高度函数和位置 primitive 还都须匹配；
不能把两个“固定旋转度量”标签当作同一目标证据。

故本线最短的下一数学输入是：在继续真实宏观逆设计的同时，把最后选定设计的一份完整连续
$E_*,a_*$ 接入其自己的固定目标位置求解与频率/网格精化；相位直接供应全部 t，几何以固定参考
服务局部后继，参考失效时再为真实新参考付费。R618 的固定 E 求解可继续独立推进，
只有上述完整函数/图等价真正建立后，才可把其收敛资格转给本线。

3bc1 目前仍只有自己的全 fine metric 观察 `3.722676721935829e-5`，未过阶段门；
本稿不为它新开旧空间几何包，也不削弱原完整物理、同 g 收敛、$.3D$ 或 $.03D$ 完成门。
