# R70：有符号闭合种子的法向自链数为三与分离接口限制

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。
状态：**已证明，已由未参与者全文独审；仍为中间结论。**
root 独立检查了原文的交叉符号约定并指出本例精确值应为 $3$；
该讨论不充当未参与者独审。

本稿只限制既定空间曲线及其既定法向作为**分离**接缝的可能性。
README 允许其它拓扑，因此不能把本结果当作整个闭曲面问题的否定。

## 1. 原始来源与适用对象

Mohammad Ghomi、Matteo Raffaelli，
*Topology of closed asymptotic curves on negatively curved surfaces*，
2025-09-19 修订，作者原文：
<https://ghomi.math.gatech.edu/Papers/asymptotic.pdf>。

本文直接核对该原文的 Theorem 1.2（印刷页 2）、Darboux 式 (2)
（页 3）、一般位置及交叉符号定义（页 4）、该定理证明 §3.1
（页 5–6）。其公式为

$$
\operatorname{Lk}(\Gamma,n)
=\operatorname{Cr}(\Gamma_e)
 +\frac12\#\{\langle e,n\rangle=0\}\,
                         \operatorname{sgn}\tau_g.
\tag{1}
$$

这里 $\Gamma$ 是嵌入 $C^3$ 负高斯曲率曲面上的闭渐近曲线，
$n$ 是曲面单位法向，$e$ 为给出正则、只有横截双点投影的方向，
$\tau_g=(n^\perp)'\cdot n$、$n^\perp=n\times T$，导数按弧长。
上支、下支按 $e$ 方向高度区分；交叉符号是
$\operatorname{sgn}\langle T_{e,+}\times T_{e,-},e\rangle$。
后文逐一验证本例全部条件，不以“随机方向”代替验证。

取已完整证明且独审的
[R68](R68-signed-curvature-closed-seed.md)
中的 $\gamma,B,d,T,N$。记

$$
a=\frac{2\sqrt6}{5},\quad
\rho=\sqrt{1-\frac{24}{25}\cos^2t},\quad
\vartheta=2t+\frac{13}{6}\sin2t,
\quad B=(\rho\cos\vartheta,\rho\sin\vartheta,a\cos t).
\tag{2}
$$

该稿的解析与严格整数区间证明给出：$\gamma=\int B\times B_tdt$
是正则闭嵌入；$N=-B$；$d' =\alpha T-N$；$T'=-\alpha d$；
并有 $X=\gamma_x(\pi/2)>1/2$、$Y=\gamma_y(\pi/2)<-1$。

实际直纹图 $F(r,u)=\gamma(u)+rd(u)$ 在某个统一小宽度上是解析嵌入。
这由闭曲线的嵌入性、$d\perp T$ 以及紧致局部图论证得到。
其度量 $a_g^2=(1+r\alpha)^2+r^2$，故
$K=-1/a_g^4<0$。$r=0$ 是闭渐近曲线，曲面法向为 $n=N=-B$。
所以 (1) 所需的真实负曲率曲面确实存在，不是假想的未来帽。

由 $n^\perp=N\times T=-d$，

$$
\tau_g=(-d')\cdot N=1.
\tag{3}
$$

曲率零点不影响此处的全圈 Darboux 标架。

## 2. 沿 x 轴投影的完整一般位置检查

取 $e=e_x$，投影为 $\gamma_e(t)=(\gamma_y(t),\gamma_z(t))$。
种子稿已经证明四条开四分弧分别位于互不相交的区域

$$
(Y,0)\times(0,\infty),\quad
(2Y,Y)\times(-\infty,0),\quad
(2Y,Y)\times(0,\infty),\quad
(Y,0)\times(-\infty,0).
\tag{4}
$$

每条弧的 $y$ 坐标严格单调，且 $y_t$ 在开弧内从不为零。
所以各弧投影单射，不同弧内部不相交，也不碰 $z=0$ 的端点。
四个端点投影为

$$
(0,0),\qquad (Y,0),\qquad (2Y,0),\qquad (Y,0).
$$

因此唯一投影重合是 $t_+=\pi/2$ 与 $t_-=3\pi/2$，且恰为双点。
这两点的空间高度分别为 $+X$ 与 $-X$，所以 $t_+$ 确为上支。

竖分量的精确速度是

$$
\gamma_{z,t}=\frac{97}{75}\cos2t-\frac{26}{25}\cos4t.
$$

在 $t=0,\pi$ 它等于 $19/75>0$；在 $t=\pi/2,3\pi/2$
等于 $-7/3$。因此端点投影也全部正则。
在唯一交叉处，三维写出的投影切向为

$$
V_+=(0,-a,-7/3),\qquad V_-=(0,+a,-7/3).
$$

其叉积满足

$$
\langle V_+\times V_-,e_x\rangle=\frac{14a}{3}>0.
\tag{5}
$$

双点因而横截，交叉符号为正。以上还证明没有任何切线平行 $e_x$，
没有三重点、切触双点或未计入的投影重合。于是

$$
\boxed{\operatorname{Cr}(\gamma_e)=1.}
\tag{6}
$$

## 3. 法向 x 分量恰有四个简单零点

由 $n_x=-\rho\cos\vartheta$ 且 $\rho>0$，只须计数
$\cos\vartheta=0$。在 $[0,\pi/2]$，

$$
\vartheta'=2+\frac{13}{3}\cos2t
$$

恰有一个零点 $t_*\in(0,\pi/2)$，即
$2t_*=\arccos(-6/13)$。因此 $\vartheta$ 先严格增、再严格减，
端值为 $0,\pi$。由于 $\vartheta'(\pi/2)=-7/3<0$，其最大值
严格大于 $\pi$。另一方面，

$$
\vartheta(t_*)
=\arccos(-6/13)+\frac{\sqrt{133}}6
<\frac{2\pi}{3}+2<\frac{3\pi}{2}.
\tag{7}
$$

第一不等式使用 $-6/13>-1/2$ 及 $133<144$；最后一个只需
$\pi>12/5$。故第一四分区恰有一次 $\vartheta=\pi/2$，且发生在
严格增加区，因而为简单零点；既没有 $3\pi/2$，也没有其它余弦零点。

由 $\vartheta(\pi-t)=2\pi-\vartheta(t)$，第二四分区恰有一次
$\vartheta=3\pi/2$，也是简单零点。又
$\vartheta(t+\pi)=\vartheta(t)+2\pi$，后半圈完全重复。
所有四分端点的余弦均为 $\pm1$。最终得到

$$
\boxed{\#\{n_x=0\}=4,\quad\text{且全部简单。}}
\tag{8}
$$

故本选择 $e_x$ 也满足 (1) 证明中需要的横截计数条件。
若严格把原文“随机方向”理解为几乎处处的方向，还可使用以下稳定性：
正则投影切向在紧圈上有正下界；横截双点由二维隐函数定理持续，
高度差与交叉行列式仍正；离开对角线与已知双点邻域的紧参数对空间
具有正的投影分离，局部单调图则排除对角线附近的新双点。
四个简单法向零点各自持续，余下紧区间无新根。
因此 $e_x$ 的某个开方向邻域内计数仍为 $1$ 与 $4$；
取其中的原文一般位置方向即得相同自链数。

## 4. 自链数与接合含义

把 (3)、(6)、(8) 代入原定理，得到

$$
\boxed{\operatorname{Lk}(\gamma,N)=1+\frac42=3.}
\tag{9}
$$

现在设一个至少 $C^2$ 的闭嵌入定向曲面 $S$ 包含这条曲线，沿曲线的法向与
$N$ 一致，并假设 $\gamma$ 在 $S$ 上分离。分离的一侧闭包是
以 $\gamma$ 为唯一边界的紧致定向曲面 $\Sigma\subset S$。
由 $S$ 的管状邻域，足够小的法向推移
$\gamma_\varepsilon=\gamma+\varepsilon N$ 与 $S$ 不相交，
因而也与 $\Sigma$ 不相交。按链接数的相交数定义，
$\operatorname{Lk}(\gamma,\gamma_\varepsilon)=0$，与 (9) 矛盾。

将 $N$ 整体换为 $-N$ 不改变该限制：在曲线的管状邻域内把法向
向量连续旋转半圈，两个小推移保持与原曲线不交，所以链接数不变。
因此该固定曲线和切平面场不能作为闭嵌入曲面的分离接口；
特别不能一侧由它单独围出帽。

结论仍不排除它成为正亏格曲面的非分离曲线；没有在此构造该闭面。它也不否认另选
自链数为零的曲线或改变边界切平面场后存在分离接合。
二阶共同度量修正稿中的真实参考条带保持同一边界法向，所以同样
受 (9) 约束；此观察不影响该稿已经证明的局部有限 jet 命题。

本稿没有构造闭等距族，没有提供有效变形幅度或全闭面 reach，
不支付 README 完成标准中的任何尚未闭合门。


## 5. 全文独立审查与正式范围

原作者冻结稿为
[geometry-signed-seed-self-link-v1](../notes/2026-11-10-78718-geometry-signed-seed-self-link-v1.md)，
6374 B，SHA256
`4c2e66feac8f94a782776d93cef38efb9d151710ea593d45eea2802a2e0694ae`。
root 已全文读取（工具 `72317b`、后再读 `8c142f`），并核原文公式与交叉符号；
root 参与过符号讨论，不将此自核算作未参与者审查。

未参与者 independent_audit 的
[全文独立审稿](../notes/2026-11-10-78718-audit-signed-seed-self-link.md)，
13453 B，SHA256
`77114e815825859a46c03615a65d00817b6844c49ac30b44ad018ac59fd343c4`。
root 已全文核读（工具 `1c4828`）。审者另行直接读取作者原文的定理、
Darboux 定义、交叉约定及完整定理证明；所有符号与范围通过，无数学订正。
本正式稿纳入独审已证明的固定投影方向开放稳定性，并明示未知闭面仅需 $C^2$。

链接数公式应用于已构造的实际解析负曲率条带；分离接合的拓扑结论
则应用于任何相同曲线、切平面场的闭嵌入 $C^2$ 曲面，不增加主问题正则性要求。
本稿无新增程序或 ODE/PDE 执行。它给出一个特定接口的障碍，
不支付闭面等距族、可见幅度、全时 reach 或 README 的完成标准。
