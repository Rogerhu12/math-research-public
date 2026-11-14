# R110：实际新旧图的 C² 差分与完整几何比例的直接转移

2026-11-12，Astra-visible-flex-fd2d / root。
**状态：已证明的条件命题。** 本文给出完整数学证明和针对 R21/R25 的有理余量；
尚未给任何新的 M15/W22 闭图确认全部差分假设，不把本条件预算登记成新曲面的成功。
它不改变度量、求解容差、物理 source 或 README 完成标准。

## 1. 为什么使用实际图的差分

R21/R25 已对唯一指定的 M12 有限闭图证明曲率、正支撑、位移和全时 reach。
这些数值不能直接挪给另一幅有限图。另一方面，若新图与该实际旧图足够接近，
逐项对新图证明小的差分界就能给出**新图自己的**几何界。

R4 使用全空间微分同胚的导数控制。本文只比较同一材料面上的两个实际映射，
不要求构造环境空间延拓，不要求第三阶导数，也不以近似源方程的形式曲率代替实际二阶导数。
相邻课题 `visible-flex-exact-nearby` 的 R1 已有保几何余量的邻域工具；本文为当前两份实际有限图的
差分 consumer 给出独立完整证明、相应的可计算范数以及本题自己的有理预算，不主张一般稳定性思想新颖。

## 2. 同一材料面上的定量命题

设 $X:M\to\mathbb R^3$ 是闭 $C^2$ 嵌入，$M$ 同胚于 $S^2$，取其诱导度量
$h=X^*e$、全局单位法向 $n_X$ 和固定中心 $c$。假设

$$
|X-c|\le R,\qquad (X-c)\cdot n_X\ge\sigma>0,
\qquad |\kappa_i(X)|\le K.
\tag{1}
$$

令 $Y=X+u$ 为同一材料面上的 $C^2$ 映射。用**旧图的实际度量** $h$ 定义

$$
\varepsilon=\sup_M|u|,\qquad
\eta=\sup_{p\in M}\sup_{h(v,v)=1}|du(v)|<1,
\tag{2}
$$
$$
\beta=\sup_{p\in M}\sup_{h(v,v)=1}
|\nabla_h^2u(v,v)|.
\tag{3}
$$

这里对每个 Cartesian 分量使用 $h$ 的 Levi-Civita Hessian。
$X\in C^2$ 使 $h\in C^1$，Christoffel 系数连续，因而 (3) 只需二阶导数。
若程序给出 Hessian 的 Hilbert–Schmidt 范数上界，也可作 (3) 的上界。

定义

$$
\sigma'=\sigma-2R\eta-\varepsilon,\qquad
K'=\frac{K+\beta}{(1-\eta)^2}.
\tag{4}
$$

若 $\sigma'>0$，则 $Y$ 为嵌入，且

$$
(Y-c)\cdot n_Y\ge\sigma',\qquad
|\kappa_i(Y)|\le K',\qquad
\operatorname{reach}(Y(M))\ge\min\{\sigma',1/K'\}.
\tag{5}
$$

此外，如果已知 $\operatorname{diam}X(M)\le D_0$，则

$$
\operatorname{diam}Y(M)\le D_0+2\varepsilon.
\tag{6}
$$

### 证明第一基本形式和法向控制

对于 $h$ 单位向量 $v$，$|dX(v)|=1$，所以

$$
1-\eta\le|dY(v)|\le1+\eta.
\tag{7}
$$

因此 $Y$ 浸入。对整个路径 $X_s=X+su$，$0\le s\le1$，同式给浸入；
沿此路径由 $n_X$ 延续法向，得到 $n_{X_s}$。对任意 $h$ 单位向量，

$$
|n_{X_s}\cdot dX(v)|
=s|n_{X_s}\cdot du(v)|\le s\eta.
$$

故 $n_{X_s}$ 在旧切平面上的投影长度不超过 $s\eta$。
由于 $s\eta<1$，连续的法向不可能经过与 $n_X$ 垂直的向量，
于是 $n_{X_s}\cdot n_X>0$。特别地

$$
\sin\angle(n_Y,n_X)\le\eta,\qquad
|n_Y-n_X|^2\le2(1-\sqrt{1-\eta^2})\le4\eta^2.
\tag{8}
$$

最后一个较松的界在 $\eta=0$ 也成立；用
$1-\sqrt{1-z}=z/(1+\sqrt{1-z})$ 即可检查。
结合 $Y=X+u$ 得

$$
(Y-c)\cdot n_Y
\ge (X-c)\cdot n_X-|X-c|\,|n_Y-n_X|-|u|
\ge\sigma'.
\tag{9}
$$

### 证明曲率界

Euclidean 向量值 Hessian 的 Gauss 公式为

$$
\nabla_h^2X(v,v)=\mathrm{II}_X(v,v)n_X.
$$

将 $\nabla_h^2Y$ 与 $n_Y$ 点乘时，扣除的
$dY(\nabla^h_vv)$ 是新曲面的切向量。因此

$$
\mathrm{II}_Y(v,v)
=\mathrm{II}_X(v,v)(n_X\cdot n_Y)
 +n_Y\cdot\nabla_h^2u(v,v).
\tag{10}
$$

若 $h(v,v)=1$，右端绝对值不超过 $K+\beta$。
而 $Y^*e(v,v)\ge(1-\eta)^2$。对所有非零 $v$ 取正常曲率的绝对最大值，
便得 $|\kappa_i(Y)|\le K'$。这使用真实 $X,Y$ 的导数，与它们是否满足等距方程无关。

(9) 和 R10 的径向投影及平行面论证给 (5) 中的嵌入与 reach。
对任意两个材料点使用三角不等式即得 (6)。证毕。

## 3. 固定握持区、集合位移与全部时间

设 $X_t,Y_t$ 是同一参数范围的闭映射族，$\sup_{p,t}|Y_t(p)-X_t(p)|\le\varepsilon$。
则每个时刻 $d_H(Y_t(M),X_t(M))\le\varepsilon$。
Hausdorff 距离的三角不等式给

$$
d_H(Y_t(M),Y_0(M))
\ge d_H(X_t(M),X_0(M))-2\varepsilon.
$$

故

$$
\delta_{\rm hold}(Y)\ge\delta_{\rm hold}(X)-2\varepsilon.
\tag{11}
$$

这比较的是像集；材料点滑动不会被计入。
若同一闭材料子集 $H$ 在两个族中分别固定，则

$$
\operatorname{diam}Y_0(H)
\ge\operatorname{diam}X_0(H)-2\varepsilon.
\tag{12}
$$

固定性和 $H$ 的非空内部仍是具体构造的输入，不能从两个图接近自动推出固定性。

本题活动带的两族均具有 $X_\alpha=R_\alpha X_0\circ\tau_{-\alpha}$、
$Y_\alpha=R_\alpha Y_0\circ\tau_{-\alpha}$，其中 $\tau$ 平移物理材料角。
因此差分也按相同公式变化，且
$h_\alpha=\tau_{-\alpha}^*h_0$。
拉回与正交变换保持 (2)、(3) 的范数，包括 Hessian 的联络拉回。
故活动带只需初始相位的完整差分界，便覆盖全部相位。
固定帽若只发生与 $t$ 无关的竖直定位变化，则其 $du$、Hessian 都为零，位置差单独计入。

此论证不假设旧有限图的诱导度量恰好旋转不变，使用的是它随相位的**准确拉回关系**。
也不把适应性角 $\psi$ 当作材料角。新图本身的公共 Cartesian 两 jet 与全局 $C^2$
接合必须先由其真实定义保证。

## 4. 活动体积三阶矩也可由实际差分转移

取去掉固定帽凸起的旧图 $X$ 和新图 $Y$，并假设它们保持原来的三重旋转对称。
旧图满足 (1)，新旧差满足 (2)、(3)，且 $\sigma'>0$。
由上面的证明，全部 $X_s=X+su$ 都为同向正径向嵌入。
记其有界内部为 $\Omega_s$，以及

$$
A_3(s)=\int_{\Omega_s}(x+iy)^3\,dV.
$$

这里仍用固定原点的水平坐标，与帽标记的旋转轴相同。
对移动边界使用输运公式，或等价地对参数柱面应用散度定理，得

$$
A_3(1)-A_3(0)
=\int_0^1\int_M (X_s^x+iX_s^y)^3
\;u\cdot n_{X_s}\;dA_{X_s}\,ds.
\tag{13}
$$

参数柱面为 $C^1$，端面为 $C^2$，经典换元和散度定理适用；
无需新旧曲面在每条法线上的点对应，也无需它们围出的实体相互嵌套。

若以旋转轴原点为中心，$|X_s|\le R+\varepsilon$；由 (7)
$dA_{X_s}\le(1+\eta)^2dA_X$。
又由旧图的正支撑和散度定理，

$$
\sigma\operatorname{Area}(X(M))
\le\int_{X(M)}X\cdot n_X\,dA
=3\operatorname{Vol}(\Omega_0)
\le4\pi R^3.
\tag{14}
$$

正径向图的内部包含在半径 $R$ 的球中，故最后一步成立。
于是

$$
|A_3(1)-A_3(0)|
\le \frac{4\pi}{\sigma}\,
\varepsilon(R+\varepsilon)^3(1+\eta)^2R^3.
\tag{15}
$$

若右端小于 $\operatorname{Re}A_3(0)$，则
$\operatorname{Re}A_3(1)>0$。
在新图上加回 R16 同一三个固定凸起，其精确 $B_3>0$ 不随帽的竖直定位改变。
R16 的中心三阶张量恒等式给相位 $0$ 和 $\pi/3$ 的不变量之差为
$B_3\operatorname{Re}A_3(1)>0$，从而排除包括反射的全部刚体全等，并给 $\delta_E(Y)>0$。

这里不把“旧 $\delta_E>0$”直接转给新图；转移的是有宏观余量的活动三阶矩，
再在新图上重新应用同一个精确固定帽矩公式。
如果新图改了帽的形状、旋转对称或相位机制，本节不能直接使用。

## 5. R21/R25 的明确充分余量

对 R21 的唯一 M12 闭图，可用以下安全有理数：

$$
R=\frac{2131902881202937}{1125899906842624},\quad D_0=2R,
\quad \sigma=\frac{737}{1000},\quad K=\frac{105782}{12500},
\tag{16}
$$
$$
d_0=\frac{199891}{10^6}<\delta_{\rm hold}(X),\quad
h_0=\frac{17713}{5000}<\operatorname{diam}X(H),\quad
a_0=\frac{11}{25}<\operatorname{Re}A_3(X).
\tag{17}
$$

它们分别由 R21 的实际支撑、曲率、位移、握持与活动矩，以及 R25 的共同包围球给出。
去掉帽凸起后，帽变平、位置范数不增、曲率变零、支撑大于其正高度，
所以同一 $R,\sigma,K$ 也适用于未标记旧图。
若新帽仅竖直平移且使用同一凸起函数，帽上的差分为常向量；
因此该处无论使用有标记或无标记旧度量，两个导数范数都为零。
活动带上的有标记/无标记映射相同。

取充分阈值

$$
\boxed{\varepsilon\le10^{-4},\qquad\eta\le10^{-3},\qquad\beta\le1/10.}
\tag{18}
$$

用 (4)–(17)、$\pi<22/7$ 纯有理计算即可严格得到

$$
\frac{\operatorname{reach}(Y_t(M))}{D_Y}>.03,
\qquad \frac{\delta_{\rm hold}(Y)}{D_Y}>.05,
\qquad\frac{\operatorname{diam}Y(H)}{D_Y}>.2,
\qquad \operatorname{Re}A_3(Y)>0.
\tag{19}
$$

复现程序 `scripts/fd2d-geometric-closeness-budget.py` 以 Fraction 完成所有比较，
输出 `notes/2026-11-12-fd2d-geometric-closeness-budget.json`。
它明确标记 `CONDITIONAL_SCALAR_BUDGET_ONLY`；它不加载新曲面，也不证明任何实际差分范数。
数值显示只用于说明，正式阈值比较使用保存的有理数。

## 6. 如何应用以及尚缺什么

几何比较所需的是一个明确的全局 $C^2$ 参数对应；它不必保目标 $g$。
实际 consumer 可在这样共同的参数中比较保存的新旧 Cartesian 图：
合并两份径向网格，保留全部角频数和旋转基导数，
在每个闭小区间上对差分的一、二阶导数给连续上界。
协变 Hessian 中旧图的 Christoffel 系数必须由其实际一、二阶导数形成，
不能用近似目标度量的联络替代而不计误差。

如果两图使用不同的适应性角，必须说明所选对应在各块和接缝上确实为全局 $C^2$ 对应；
同一个角符号或相同网格索引本身不足以说明这一点。
若还要用这个对应比较同 $g$ 的度量误差，必须另回到公共物理材料角，不能把几何对应冒充保 $g$ 的对应。
如果这里只转移几何，活动块的像集都是各自初态绕同一轴的旋转，
故初态的支撑、曲率和两像 Hausdorff 接近直接覆盖所有相位；固定帽另付相同位置差。
这条像集论证不要求任意选择的比较对应与材料角平移交换。
prefix、tail、真实公共两 jet、圆领和帽都必须被覆盖，局部通过不构成全图转移。

只有这样的实际完整比较满足 (18) 后，(19) 才成为新图的几何证书。
这个结论仍不付同 $g$ 的全域 metric 上界、不付加密收敛，也不构造缺失的非线性尾。
本轮继续真实 M15/W22 联解；本定理的用途是使成功后的几何论证有一条更直接的可执行路径。
