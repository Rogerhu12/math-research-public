# R32：由完整高度解构造平面展开及全局尾部图

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

状态：**已证明，条件几何闭合工具**。输入是同一真实度量上的完整高度函数，不预先假定已有全局浸入或嵌入。真实 Darboux 方程使水平度量平直；精确周期给单值平面展开，内 cuff 的平盘两 jet 给抽象圆盘封口，正 Jacobian 和严格凸外边界最后推出全局图。有限 Fourier 投影方程、源 ODE 样本和“数值周期接近零”均不代替这些输入。

## 1. 假设、结论及正则性范围

令 $0<r_c<R<\infty$，并在

$$
A=(r_c,R]\times(\mathbb R/2\pi\mathbb Z)
$$

上给定实函数

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad E>0,\qquad h=h(r,\theta).
\tag{32.1}
$$

假设 $E$ 在每个紧子环带上为 $C^1$，$h$ 为单值、$2\pi$ 周期的 $C^2$ 函数。允许径向拼接圈，但这些圈在 $r>r_c$ 局部有限，且 $E,h$ 的上述导数跨缝连续。在每个开光滑片上，进一步要求 $E\in C^2$、$h\in C^3$。这组内部正则性仅用于经典曲率与结构方程；在可能聚积的内 cuff 上只使用下述一致两 jet 极限。

写

$$
P=h_r,\qquad Q=h_{rr},\qquad
\nu^2=1-\frac{P^2}{E}-\frac{h_\theta^2}{r^2}>0.
\tag{32.2}
$$

要求每个开光滑片满足**完整、未投影的真实 Darboux 方程**

$$
\det\nolimits_g(\operatorname{Hess}_g h)=K_g\nu^2,
\qquad K_g=\frac{E'}{2rE^2}.
\tag{32.3}
$$

行列式取在 $g$ 的正交标架中。由于式中各项仅用 $E,E'$ 和 $h$ 的两 jet，若它们跨缝连续，方程也连续延至各拼接圈。

在 $r\downarrow r_c$ 时要求以下极限对全部 $\theta$ 一致：

$$
\begin{gathered}
E\longrightarrow1,\qquad E'\longrightarrow0,\\
P,\ h_\theta,\ Q,\ P_\theta,\ h_{\theta\theta}
\longrightarrow0.
\end{gathered}
\tag{32.4}
$$

外切口的水平转角率定义为

$$
\Gamma=
\frac{1+Prh_{\theta\theta}/(r^2-h_\theta^2)}
{\sqrt E\,\nu}.
\tag{32.5}
$$

假设 $\Gamma(R,\theta)>0$。外边界所需的精确周期有下列两个确认入口。本定理已包含 (32.4)，所以第二入口使周期条件自动成立；第一入口也单独适用于尚未填盘的环带。

1. **单切口方式：** 在 $r=R$，平面标架的转角恰为 $2\pi$，且积分得到的位置周期恰为零，具体定义见第 4 节。若 $h(R,\theta)$ 和 $P(R,\theta)$ 都为 $\pi$ 周期，转角恰为 $2\pi$ 已经推出位置周期为零。
2. **完整 cuff 方式：** 直接使用全部 (32.4)。第 5 节证明，在 (32.1)–(32.3) 下，这些极限自动强制全环带的转角周期为 $2\pi$、位置周期为零。因此单切口条件在这一版本中是一个可复核的兼容性结论，不是额外存在性假设。

**定理。** 上述条件给出一个 $C^2$ 等距映射

$$
F=(X,h):A\longrightarrow\mathbb R^3
$$

以及常数 $C_c\in\mathbb R^2$、$\beta_c,h_c\in\mathbb R$，使它在内侧与

$$
F_{\mathrm{flat}}(r,\theta)
=\bigl(C_c+r(\cos(\theta+\beta_c),\sin(\theta+\beta_c)),\,h_c\bigr),
\qquad 0\le r\le r_c,
\tag{32.6}
$$

具有相同的全部两 jet。填盘后的定义域是抽象闭圆盘，$F$ 是其 $C^2$ 嵌入；水平投影 $X$ 把它一一映到一个严格凸闭域 $\overline\Omega$，且整个面是该域上的一个 $C^2$ 图。没有先使用全局嵌入性来证明这一结论。

这里“严格凸”只针对外边界及其所围的平面域。中间各个 $r$ 圈无需先证明严格凸或星形，$\Gamma$ 也无需在整个环带都为正。由 (32.2) 得到的正水平 Jacobian 才是全局图证明所需的内部条件。

## 2. Darboux 方程推出水平度量平直

定义正定度量

$$
q=g-dh\otimes dh.
\tag{32.7}
$$

其正定性由 (32.2) 等价地保证。下面的论证不假定 $q$ 已经来自某个平面投影。

在一个光滑片上，考虑人工乘积流形 $(A,q)\times\mathbb R$ 及其中的图

$$
\iota:x\longmapsto(x,h(x)).
$$

它的诱导度量是 $q+dh^2=g$。记 $v=\nabla_g h$，则矩阵求逆或直接代入给出

$$
\nabla_q h=\frac{v}{\nu^2},\qquad
1+|\nabla_qh|_q^2=\frac1{\nu^2}.
\tag{32.8}
$$

人工图向上的单位法向竖直分量因此为 $\nu$。乘积中的竖直单位向量平行，故与其取内积所得的高度 Hessian 恒等式为

$$
\operatorname{Hess}_g h=\nu\,\mathrm{II}_\iota.
\tag{32.9}
$$

也可直接计算连接差：

$$
\nabla^q_UV=\nabla^g_UV
-\frac{\operatorname{Hess}_g h(U,V)}{\nu^2}\nabla_g h,
\qquad
\operatorname{Hess}_q h=\frac{\operatorname{Hess}_g h}{\nu^2};
$$

人工图的 $\mathrm{II}_\iota=\nu\operatorname{Hess}_q h$ 与 (32.9) 相同。

取 $g$ 正交基 $e_1,e_2$。它们在乘积中水平分量的 $q$-Gram 行列式为

$$
\det\bigl(\delta_{ij}-dh(e_i)dh(e_j)\bigr)=\nu^2.
$$

乘积环境对此切平面的截面曲率为 $K_q\nu^2$。Gauss 方程遂给出

$$
K_g=K_q\nu^2+
\frac{\det_g(\operatorname{Hess}_g h)}{\nu^2},
$$

即

$$
\boxed{
K_q=\frac{K_g\nu^2-\det_g(\operatorname{Hess}_g h)}{\nu^4}.}
\tag{32.10}
$$

由 (32.3)，$K_q=0$。这是水平度量平直的证明，尚未构造任何欧氏三维浸入，因此不存在先假定结论的问题。

对 (32.1) 的曲率公式也可直接核算：令 $ds=\sqrt E\,dr$，则旋转型度量为 $ds^2+r(s)^2d\theta^2$，$r_s=E^{-1/2}$、$r_{ss}=-E'/(2E^2)$，故 $K_g=-r_{ss}/r$，等于 (32.3) 的表达式。

## 3. 显式标架、弱平直连接与局部展开

在全部 $A$ 上定义

$$
a=\sqrt{r^2-h_\theta^2},\qquad
D=\sqrt E\,r\nu,\qquad
b=-\frac{P h_\theta}{a},\qquad
c=-\frac D a.
\tag{32.11}
$$

$a,D$ 为正，且

$$
q=\alpha^2+\beta^2,\qquad
\alpha=b\,dr+a\,d\theta,\quad \beta=c\,dr,\qquad
\alpha\wedge\beta=D\,dr\wedge d\theta.
\tag{32.12}
$$

这些 1-形式为 $C^1$。设

$$
\Gamma=\frac{b_\theta-a_r}{c},\qquad
G=\frac{b\Gamma+c_\theta}{a},\qquad
\omega=G\,dr+\Gamma\,d\theta.
\tag{32.13}
$$

代入 (32.11) 可化成 (32.5)，这也是 [R30](R30-source-cut-to-cartesian-boundary-traces.md) 的切口转角公式。直接求导得第一结构方程

$$
d\alpha=\omega\wedge\beta,\qquad
d\beta=-\omega\wedge\alpha.
\tag{32.14}
$$

例如 $d\alpha=(a_r-b_\theta)dr\wedge d\theta=-c\Gamma\,dr\wedge d\theta$；第二式就是 $aG=b\Gamma+c_\theta$。

在每个开光滑片上，$K_q=0$ 与第二结构方程给 $d\omega=0$。连接 $\omega$ 在全部 $A$ 连续，所以这个结论也以零闭路积分的意义跨过各拼接圈。具体地，在任意紧矩形内仅有有限个拼接圈；先删去它们宽 $\epsilon$ 的条带，逐片用 Stokes 公式。各条带两侧的边界积分因 $\omega$ 一致连续而在 $\epsilon\to0$ 时互相抵消，短横边积分趋零，故原矩形的边界积分为零。有限划分随后给任意可缩闭路的积分为零。

在单连通覆盖

$$
\widetilde A=(r_c,R]\times\mathbb R
$$

上，固定基点及一个实角后，路径积分定义一个 $C^1$ 函数 $\gamma$，满足

$$
d\gamma=\omega,\qquad \gamma_r=G,\qquad \gamma_\theta=\Gamma.
\tag{32.15}
$$

连续闭形式的这一积分结论不需要跨缝的三阶导数：矩形积分为零先给路径独立，沿坐标段的微积分基本定理再给两个连续一阶导数。

取

$$
t=(\cos\gamma,\sin\gamma),\qquad n=Jt,\qquad
J(x,y)=(-y,x).
$$

由 $dt=n\omega$、$dn=-t\omega$ 及 (32.14)，向量值 1-形式

$$
\xi=t\alpha+n\beta
\tag{32.16}
$$

满足 $d\xi=0$。它为 $C^1$，所以积分给出 $C^2$ 映射 $X$，其导数为

$$
X_r=bt+cn,\qquad X_\theta=at,\qquad
\boxed{\det(X_r,X_\theta)=-ac=D>0.}
\tag{32.17}
$$

此时在覆盖空间上已有

$$
(dX)^T dX=q,\qquad (dX)^T dX+dh^2=g.
\tag{32.18}
$$

因此 $(X,h)$ 是局部 $C^2$ 等距浸入。向上法向的竖直分量为
$D/(r\sqrt E)=\nu>0$。平面旋转角和位置基点是此构造仅有的自由刚体规范。

## 4. 精确单切口周期传播到全环带

因为 $E,h$ 为 $2\pi$ 周期，$\omega$ 也是。由 (32.15)，

$$
\gamma(r,\theta+2\pi)-\gamma(r,\theta)=\Theta
\tag{32.19}
$$

是与 $r,\theta$ 都无关的常数。在某一切口验证

$$
\int_0^{2\pi}\Gamma(R,\theta)\,d\theta=2\pi
\tag{32.20}
$$

就得到 $\Theta=2\pi$，从而 $t,n,\xi$ 都为 $2\pi$ 周期。

于是

$$
X(r,\theta+2\pi)-X(r,\theta)=T
\tag{32.21}
$$

又是与 $r,\theta$ 都无关的常向量。在同一切口验证

$$
T=\int_0^{2\pi}a(R,\theta)t(R,\theta)\,d\theta=0
\tag{32.22}
$$

便使 $X$ 在整个环带上单值。这两个条件分别是旋转周期与平移周期；真实 Darboux 方程只使它们守恒，有限切口中很小的非零周期仍然是非零周期。

若 $H(\theta)=h(R,\theta)$、$P(R,\theta)$ 都为 $\pi$ 周期，则外切口的 $a,\Gamma$ 也为 $\pi$ 周期。由 (32.20)，每个半周的 $\Gamma$ 积分恰为 $\pi$，所以

$$
t(R,\theta+\pi)=-t(R,\theta),\qquad
a(R,\theta+\pi)t(R,\theta+\pi)=-a(R,\theta)t(R,\theta).
$$

这直接推出 (32.22)，而不是以数值积分接近零代替精确闭合。

### 4.1 外边界严格凸的充分性

当 (32.20)、(32.22) 与 $\Gamma(R,\theta)>0$ 成立时，外曲线的速度为 $a>0$，切向角严格增加一整周。固定 $\theta_0$ 并令 $n_0=Jt(R,\theta_0)$。函数

$$
u(\theta)=
\bigl(X(R,\theta)-X(R,\theta_0)\bigr)\cdot n_0
$$

的导数为

$$
u'(\theta)=a(R,\theta)
\sin\bigl(\gamma(R,\theta)-\gamma(R,\theta_0)\bigr).
$$

在切向角前半周上它严格为正，后半周严格为负。起终值都为零，故每个中间点有 $u>0$。因此任意切线的严格左半平面包含曲线全部其它点，曲线没有重合点，每个法向方向又恰出现一次。它遂是一个严格凸有界域 $\Omega$ 的正向边界，绕 $\Omega$ 内每点一周，绕外点零周。

本段只用了外切口；没有把每个中间圈的凸性加入定理假设。

## 5. 完整内 cuff 也会自动消除周期

这一节可独立于 (32.20)、(32.22) 使用。先在覆盖空间中保持第 3 节的局部构造。

由 (32.4)、(32.11)，下列极限一致成立：

$$
\begin{gathered}
a\to r_c,\quad a_r\to1,\quad a_\theta\to0,\\
b\to0,\quad c\to-1,\quad
b_r,b_\theta,c_r,c_\theta\to0,\\
\Gamma\to1,\qquad G\to0.
\end{gathered}
\tag{32.23}
$$

例如

$$
a_r=\frac{r-h_\theta P_\theta}{a},\qquad
a_\theta=-\frac{h_\theta h_{\theta\theta}}a,
$$

且

$$
\begin{aligned}
D_r=
\frac{E'a^2+2E(r-h_\theta P_\theta)-2rP^2-2r^2PQ}{2D}
\longrightarrow1,\\
D_\theta=-\frac{E h_\theta h_{\theta\theta}+r^2PP_\theta}{D}
\longrightarrow0.
\end{aligned}
$$

因此 $c_r=-D_r/a+Da_r/a^2\to0$；其余各式同样只用 (32.4) 中列出的导数。没有使用未假定的三阶 cuff 极限。

$G$ 有界且趋零，$r_c$ 又为有限端点，故 $\gamma(r,0)$ 收敛。结合 $\Gamma\to1$，在每个固定有限角区间上

$$
\gamma(r,\theta)\longrightarrow\gamma_c+\theta.
\tag{32.24}
$$

恒定旋转周期 (32.19) 在 $r\downarrow r_c$ 的极限为 $2\pi$，故它本来就恰为 $2\pi$。从而 $t,n,\xi$ 为 $2\pi$ 周期，(32.21) 中的 $T$ 有定义且为常向量。

又因为 $X_r$ 一致有界，$X(r,0)$ 有极限。由 $X_\theta=at$ 及 (32.24)，极限曲线满足

$$
X_c'(\theta)=r_c t_c(\theta),\qquad
t_c=(\cos(\gamma_c+\theta),\sin(\gamma_c+\theta)).
$$

记 $n_c=Jt_c$，有 $n_c'=-t_c$，所以

$$
X_c(\theta)=C_c-r_c n_c(\theta).
\tag{32.25}
$$

这是一条真正闭合的圆。因此 (32.21) 的极限为零，即 $T=0$。完整 cuff 条件自动强制全环带的两个精确周期，不需再逐层求数值闭合。

这一结论是**完整真实高度解的必要兼容性**：若某个有限切口的准确转角周期不是 $2\pi$，或位置周期不是零，即使差极小，它也不可能在完全保留该切口数据的同时延成满足 (32.2)–(32.4) 的同一个真实解。局部 mean-root 修正可以修复切口兼容性，但修后的数据仍须另外找到真实径向轨道。

## 6. 全部两 jet 与平盘匹配

$P$ 近 cuff 有界，故 $h(r,0)$ 有有限极限；由 $\|h_\theta\|_\infty\to0$，全部角上的高度一致趋于同一个常数 $h_c$。

将 (32.23) 代入 (32.17) 及其一阶导数，得

$$
\begin{aligned}
X&\to C_c-r_c n_c,&
X_r&\to-n_c,&
X_\theta&\to r_c t_c,\\
X_{rr}&\to0,&
X_{r\theta}&\to t_c,&
X_{\theta\theta}&\to r_c n_c.
\end{aligned}
\tag{32.26}
$$

所用的准确公式为

$$
\begin{aligned}
X_{rr}&=(b_r-cG)t+(bG+c_r)n,\\
X_{r\theta}&=a_r t+aG n,\\
X_{\theta\theta}&=a_\theta t+a\Gamma n.
\end{aligned}
\tag{32.27}
$$

令 $\beta_c=\gamma_c-\pi/2$，则 $-n_c(\theta)=(\cos(\theta+\beta_c),\sin(\theta+\beta_c))$。式 (32.26) 与平盘 (32.6) 的全部平面两 jet 相同，而 (32.4) 与 $h\to h_c$ 支付高度的全部两 jet。

在拼接圈 $r=r_c>0$，极坐标是普通局部光滑坐标。一致的一阶、二阶导数极限及逐坐标积分表明，按 (32.6) 填入内侧后，函数及其一阶导数可微，其二阶导数连续，所以 $F$ 为 $C^2$。在 $r=0$ 使用平盘的 Cartesian 坐标，映射就是一个平面刚体映射加常高度，因而没有极坐标奇点。

填盘的水平 Jacobian 处处为正：在环带中由 (32.17)，在平盘中为旋转矩阵的正行列式，接缝处由极限一致。其诱导度量在内盘为欧氏度量，与 (32.1) 以 $E\to1,E'\to0$ 的 $C^1$ 数据接合。

## 7. 正 Jacobian 与外边界绕数推出全局图

现在把填盘后的定义域记为抽象闭圆盘 $\mathcal D$。目前只已知 $X:\mathcal D\to\mathbb R^2$ 为 $C^2$ 局部保向微分同胚，且外边界一一映成第 4.1 节的严格凸曲线。下面证明其全局单射，不预先假设曲面嵌入。

取 $y\notin X(\partial\mathcal D)$。集合 $X^{-1}(y)$ 位于内部；局部逆定理使它是离散集，紧致性使它有限。每个原像附近的局部度都为 $+1$。

可直接用绕数积分得到计数恒等式。在去掉各原像的小互不相交圆盘后的 $\mathcal D$ 上，拉回闭 1-形式

$$
\eta_y=
\frac{(X_1-y_1)\,dX_2-(X_2-y_2)\,dX_1}
{|X-y|^2}.
\tag{32.28}
$$

Stokes 公式使外边界积分等于各个小圆边界的正向积分之和。局部保向微分同胚使每个小圆的积分为 $2\pi$，故

$$
\#X^{-1}(y)
=\operatorname{wind}(X|_{\partial\mathcal D},y)
=
\begin{cases}
1,&y\in\Omega,\\
0,&y\notin\overline\Omega.
\end{cases}
\tag{32.29}
$$

内部点也不能映到 $\partial\Omega$：如果有这样的点，局部逆给出的开像会包含 $\overline\Omega$ 外的点，与 (32.29) 矛盾。外边界本来已经一一覆盖 $\partial\Omega$，于是 $X$ 是 $\mathcal D\to\overline\Omega$ 的双射。紧空间到 Hausdorff 空间的连续双射为同胚；局部逆又使内部逆为 $C^2$。

边界的 $C^2$ 逆也不需要额外角向高阶迹。若要在边界外应用普通开集逆定理，可对任何 $C^2$ 分量 $Y(r,\theta)$ 用

$$
\widetilde Y(R+s,\theta)
=6Y(R-s,\theta)-8Y(R-2s,\theta)+3Y(R-3s,\theta)
\tag{32.30}
$$

作充分小 $s\ge0$ 的延拓。零阶、一阶和二阶径向匹配分别使用
$6-8+3=1$、$-6+16-9=1$、$6-32+27=1$，混合导数也相同。因此这是 $C^2$ 延拓，且 $X$ 的正行列式在足够小邻域仍保持。普通逆定理便给边界附近的 $C^2$ 逆。

所以

$$
f=h\circ X^{-1}
$$

是 $\overline\Omega$ 上的 $C^2$ 函数，$F(\mathcal D)$ 恰是其图。$X$ 的全局单射也使 $F$ 全局单射；紧致性与浸入性给出 $C^2$ 嵌入。这完成第 1 节定理。$\square$

注意 (32.30) 只证明一般 $C^2$ 图能局部延伸，不提供延拓曲率预算，也不保证其二阶径向边界迹具有两个角导数。[R27](R27-explicit-star-shaped-graph-extension.md) 的显式受控外延仍需其单独列明的较光滑 Cartesian 边界迹条件。

## 8. 全环带半周对称时，中心与径向无关

若 $h(r,\theta+\pi)=h(r,\theta)$ 在整个 $A$ 成立，则 $a,b,c,\Gamma,G$ 都为 $\pi$ 周期。连接积分给

$$
\gamma(r,\theta+\pi)-\gamma(r,\theta)=\pi.
\tag{32.31}
$$

这里左侧先由周期性知道为常数，再由一个精确切口的半周转角，或由 (32.24) 的 cuff 极限确定为 $\pi$。

于是 $t,n$ 反周期，而 $X_r,X_\theta$ 也反周期。因此

$$
C(r,\theta)
=\frac{X(r,\theta)+X(r,\theta+\pi)}2
\tag{32.32}
$$

对 $r,\theta$ 的两个偏导都为零，故是**同一个常向量**。与 cuff 极限比较，它就是 $C_c$。这证明所有径向圈具有共同的中心对称中心；只验证外圈中心或若干数值圆心，不能推出此结论。

共同中心不自动使每个中间圈星形；本定理的全局图证明不需要这项附加性质。

## 9. 参数族、物理相位与固定平盘

假设在固定度量 $g$、固定定义域上，$h_t$ 连续依赖紧参数集中的 $t$，其依赖是包括 cuff 极限在内的 $C^2$ 连续，并逐个满足以上条件。选择连续的基点位置和标架角规范。

正定性在紧闭域及参数集上给 $\nu_t$ 的共同正下界。由 (32.11)–(32.13)，系数及连接连续依赖高度两 jet；沿固定有限路径积分 (32.15)、(32.16)，再使用 (32.17)、(32.27)，得到 $X_t$ 在 $C^2$ 拓扑下连续。内盘的中心、相位与常高度也连续，因此填盘后的 $F_t$ 是同一度量上的 $C^2$ 连续嵌入族。

特别地，令内盘中心为水平原点，对已经构造的一个解定义物理相位族

$$
F_\phi(r,\theta)
=\mathcal R_\phi F_0(r,\theta-\phi),
\tag{32.33}
$$

其中 $\mathcal R_\phi$ 是绕竖直轴的三维旋转。因为 $g$ 不依赖 $\theta$，全部 $F_\phi$ 对同一个 $g$ 等距。对 (32.6) 的平盘，两次角移相消，所以每个内盘材料点逐点固定。该公式使用真实物理角 $\theta$；计算坐标若不是 $\theta$，须先作正确坐标转换。

这一结论支付条件性的全相位图与固定平盘，不支付闭曲面的握持幅度、欧氏非全等量或其它接缝。

## 10. 与曲率、整图延拓及当前数据的接口

由本结果构造的 $F$ 是实际 $C^2$ 等距图，因而可真正使用 [R31](R31-complete-height-curvature-transfer.md) 的

$$
\mathrm{II}=\frac{\operatorname{Hess}_g h}{\nu}
$$

及其完整 Fourier/径向区间曲率门。若内部已连续证明 $|\kappa|\le K_{\rm in}$，且实际外边界的 Cartesian 三组迹满足 R27 的正则性与数据盒，则 R27 构造的辅助外环与该内图准确接合，并在远处为常值。所得整平面图的曲率界为

$$
K=\max(K_{\rm in},K_{\rm ext}).
$$

[R25](R25-entire-graph-curvature-and-reach.md) 于是给辅助整图 $\operatorname{reach}\ge1/K$，从而给原尾图内任意点对的法向弦条件。有限尾图有边，不能把这一句话误写成未经延拓的有边集合本身自动具有同样的 reach。整个闭面的跨片点对、其它接缝和弱标记仍按 R10、R11、R16、R24 分别核销。

当前已支付的 R30 邻近精确 stored 切口及其 $K_{\rm ext}<1.961$ 外环，仅是一个局部边界对象；它不提供满足 (32.3)、(32.4) 的真实径向高度轨道。R31 对 R26 新实背景的全部背景层 $|\kappa_0|\le8$，以及对 R23 真实小球的条件曲率界，也不能与那个旧 stored 切口静默拼成同一度量上的解。

实际应用仍需给出：同一个真实 $g$ 上满足完整全频 Darboux 方程的高度；有限头到精确深尾的匹配与全胞元包络；上述 cuff 极限；实际外切口的严格凸性及 Cartesian 迹；与强前缀的全部两 jet 接合。保存的有限 ODE 状态若有非零全频缺陷或径向插值缝，并不满足本定理。这里的完整证明消除了几何展开与全局图步骤的循环依赖，没有宣称本课题的强幅闭面已经完成。
