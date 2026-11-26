# R66. 三重高度迹的连续转角支付平面原函数闭合

会话：Astra-held10-06bbeb39-20261126 / seam_geometry。日期：2026-11-26。

本条针对当前 $3j$ 高度 Fourier 模的接缝构造，支付一个原先未显式量化的
平面原函数闭合项目。它不是新的 full-H 解或完整曲面证书。
已逐段核对 [R12](R12-height-metric-jets-determine-cartesian-seam.md)、
[R14](R14-mean-slope-from-turning-and-darboux.md) 和
[R20](R20-exact-circle-primary-distance.md)：R12 给已存在曲面的 Cartesian
接缝唯一性，R14 用真实闭曲线的转角数固定均值，R20 讨论圆弧的主频距离；
它们没有给出下面的三扇区平移闭合等式及其有限残差界。

## 1. 精确命题：一个连续转角条件同时消去平移闭合缺口

固定 $R>0$、$E>0$。给定实函数
$\zeta\in C^2(\mathbb R/(2\pi\mathbb Z))$、
$p\in C^1(\mathbb R/(2\pi\mathbb Z))$，二者都具有周期
$a=2\pi/3$。它们表示 cut 的完整高度和完整径向高度导数，
允许 $\zeta$、$p$ 含零模。

记

$$
G=R^2-(\zeta')^2,\qquad
d=EG-R^2p^2.
$$

假设整个角周期上 $G,d>0$。选择与标准圆相同的平面取向，定义

$$
v=\sqrt G,\qquad
\omega=\frac{R}{\sqrt d}
\left(1+\frac{Rp\zeta''}{G}\right),\qquad
I=\frac1{2\pi}\int_0^{2\pi}\omega(\theta)\,d\theta.
\tag{1}
$$

将平面视作复数，任取初始单位切向量 $T_0$ 和初始位置 $Y_0$，令

$$
T(\theta)=T_0\exp\left(i\int_0^\theta\omega(t)\,dt\right),
\qquad
Y(\theta)=Y_0+\int_0^\theta v(t)T(t)\,dt.
\tag{2}
$$

则 $Y$ 是正则 $C^2$ 平面曲线，并有：

1. 若 $I=1$，则 $Y$ 的位置和切向量在一周后都严格闭合；
   存在唯一中心 $O$ 使
   $Y(\theta+a)-O=e^{2\pi i/3}(Y(\theta)-O)$。
2. 若 $\nu\ge|I-1|$，则一周的位置闭合缺口满足

$$
\boxed{\ |Y(2\pi)-Y(0)|\le\frac{8\pi^2}{9}R\,\nu.\ }
\tag{3}
$$

这里没有要求平面曲线无自交。正则、转角数和几何嵌入是不同的项目；
本条不以 (3) 代替 reach 或嵌入证明。

### 证明

由 $\zeta,p$ 的三重周期性，$v,\omega$ 都是 $a$ 周期函数。
每个扇区的转角相同，记

$$
\Omega=\int_0^a\omega\,d\theta=aI,\qquad
\rho=e^{i\Omega},\qquad
C=\int_0^a vT\,d\theta.
$$

由 (2)，对所有 $\theta$ 有 $T(\theta+a)=\rho T(\theta)$。
三个扇区的位移因此分别是 $C,\rho C,\rho^2C$，所以

$$
\boxed{\ Y(2\pi)-Y(0)=C(1+\rho+\rho^2).\ }
\tag{4}
$$

若 $I=1$，则 $\rho=e^{2\pi i/3}$，括号为零；
同时 $T(2\pi)=T_0e^{2\pi iI}=T_0$。
又由周期性积分，

$$
Y(\theta+a)-Y(a)=\rho\bigl(Y(\theta)-Y_0\bigr).
$$

因 $\rho\ne1$，取且仅取

$$
O=Y_0+\frac{C}{1-\rho}
$$

便得到所述中心三重对称等式。

一般情况下，$|\rho|=1$，故

$$
|1+\rho+\rho^2|
=|1+2\cos\Omega|
=2\left|\cos(aI)-\cos a\right|
\le2a|I-1|\le2a\nu.
$$

由于 $\zeta'$ 为实数且 $G>0$，$0<v\le R$，所以 $|C|\le aR$。
代入 (4) 得 $2a^2R\nu=(8\pi^2/9)R\nu$，即 (3)。证毕。

上侧反射同时令 $\zeta,p$ 变号，(1) 的 $G,d$ 和乘积 $p\zeta''$ 不变，
所以同一个结论直接用于当前上尾。

## 2. 完整高度一 jet 与同一个 g 如何确定平面二 jet

以下是 R12/R14 在当前接口的明确使用合同，引用其已完成证明，不另计一份
独立存在性结果。

设两张实际 $C^2$ 曲面在同一 $R$ 方向下具有精确第一基本形式

$$
g_j=E_j(R)\,dR^2+R^2\,d\theta^2,
$$

并且 cut 上 $E_1=E_2=E$、$E_1'=E_2'=E'$。
假设两侧足够光滑以在各自内部使用 Gauss 方程且连续取边界极限，
完整高度一 jet 相同（先允许一次竖直常数平移），投影满足 $G,d>0$，
且整条 cut 上

$$
Q=E\zeta''+Rp\ne0.
$$

则存在一个固定平面欧氏等距变换，使完整 Cartesian 二 jet 相同。
若两侧水平投影取向相同，变换只需平面旋转与平移；取向相反时允许一次反射。

具体地，完整高度一 jet 已给出共同的
$\zeta,\zeta',\zeta'',p,p_\theta$。R14 的 Darboux 公式

$$
z_{RR}=\frac{E'}{2E}p+
\frac{(p_\theta-\zeta'/R)^2+
[E'/(2RE^2)]d}
{\zeta''+Rp/E}
\tag{5}
$$

在 $Q\ne0$ 时给出相同的高度二 jet。于是 $h=g-dz^2$ 的一 jet
完全相同。R12 的速度/有向曲率 ODE 和 Gram 分解给出同一平面迹及一阶，
其 Christoffel 公式再给出全部平面二阶。这里只剩一个初始平面位置和
初始切向量，即一个固定平面刚体变换；没有额外可任意选择的径向导数。

若不是从两张已存在曲面出发，而是先按 (1)–(2) 构造边界平面原函数，
第 1 节说明在当前三重高度数据及连续 $I=1$ 下，无须再加独立的
平移 holonomy 方程。它仍未证明所给高度数据能在整个径向环带延拓成
精确等距曲面；那需要实际 Darboux/尾问题的解。

## 3. 真实有限源码仍要支付什么

当前完整高度 Fourier 系数按 $3j$ 定义，因此真实有限函数具有严格三重周期；
这不是由某些浮点采样值接近相等推出来的。
若平面表示也仅保留 $m\equiv1\pmod3$ 的模式，则该**有限表示本身**
以原点为中心严格三重闭合，但这不能证明它就是 (2) 的等距平面原函数。
它与 (2) 的投影/积分误差，及其对度量一 jet 的影响，仍要量化。

具体执行时，(3) 中的 $\nu$ 必须取
`seam_cut_height_compatibility.py` 输出的连续
`continuous_turning.normalized_I` 区间：

$$
\nu=\max\{|I_--1|,\ |I_+-1|\},
$$

使用其严格端点或精确有理端点字段。不得直接把离散
`moments[0]`、原 root 采样残差或普通浮点转角求和放进 (3)。
源码离散量到真连续量的支付见
[当前均值源码相容说明](../notes/2026-11-26-seam-mean-source-compatibility.md)。

平面旋转只会旋转 (4) 的缺口，平移不改变缺口，因而不能消除非零 holonomy。
任意材料角平移也不能被当成自由接缝参数：它一般会改变已逐角配准的
高度余弦迹。只有保留全部既定数据的对称角移才不改变该合同；
在 R12 已有刚体自由度之外，没有借角移跳过误差支付的余地。
角起点改变不改变 $I$，所以不能把非整周的切向旋转变成闭合。
对尚未闭合的原函数，位置缺口的分量可以随起点改变；
这里不把它误说成逐分量不变，也不以择优起点代替完整位置/切向闭合。

对于两个近似场，依次需要：完整高度迹及非均值斜率误差、
连续转角误差及同严格均值分支、实际归一化 Darboux 残差、
实际度量一 jet/平面投影误差。只有这些量都已量化，才能应用 R14/R12
的有限误差链或显式尾侧 Hermite 修补。小的零阶 metric 本身不足以代替它们。

## 4. 执行状态

本条是已完成的精确等式和条件误差界证明，没有在新 accepted cut 上执行数值代入。
当前公共 runner 仍在恢复实际前缀/完整尾；不得把 (3) 的公式、工具准备或
warm 输入标作 full-H Cartesian 接缝通过。
