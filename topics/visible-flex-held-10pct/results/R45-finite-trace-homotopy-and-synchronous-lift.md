# R45：完整余弦到圆弧迹的有限空间路径与同步 lift

维护：Astra-held10-7322d0de-20261118 / root，2026-11-18（UTC+8）。

分类：**已证明的解析结构结论与表示恒等式**。本条没有运行新的核心、BVP、
尾、均值积分或 metric。它为接续已接受 q060 原余弦有限图规定一条
新的设计路径，不给出这条路径上实际解的存在性或数值接受。

## 1. 精确定义及假设

沿用 R44 真积分定义的偶、三重对称 $C^4$ 控制。周期为
$T_0=2\pi/3$，局部变量为 $x=\phi-\pi/3$，按该周期取中心代表。
固定 $0<a<a+b<T_0/2$，令 $\chi=1$ 于保护弧 $|x|\le a$，
$\chi=0$ 于 $|x|\ge a+b$，并令 $W=1-\chi$。所有以下控制使用
**同一个**控制窗口；主形变的窗口可以有另一个已固定宽度。

原零迹列写为

$$
B_j(\phi)=W(\phi)\{\cos(3j\phi)-d_{0j}-d_{1j}\cos(3\phi)\}.
$$

两个迹列为 $T=S_A-S_B$、$U=S_B$。它们的精确定义满足

$$
T(\pi/3+x)=1-\cos x,\qquad U(\pi/3+x)=\cos x
\quad (|x|<a).
$$

$B_j,T,U$ 的真平均矩与真 $\cos(3\phi)$ 矩均为零。这里的
$d_{ij}$ 和 $S_A,S_B$ 使用定义积分，不把浮点投影的数值零视为
解析恒等式。既有定义、真矩与组合曲率预算见
[R44 完整定义](R44-circle-trace-controls-complete-two-missing-directions.md)、
[圆弧迹组合](../notes/2026-11-18-m3-circle-trace-combinations.md)和
[R44 真积分接口](../notes/2026-11-18-r44-integral-oracle-interface.md)。

对任意固定整数 $M\ge4$ 定义 $M-1$ 列：

$$
C_j^\lambda=(1-\lambda)\cos(3j\phi)+\lambda B_j,
\qquad 2\le j\le M-2,
$$
$$
C_{M-1}^\lambda=(1-\lambda)\cos(3(M-1)\phi)+\lambda T,
\qquad
C_M^\lambda=(1-\lambda)\cos(3M\phi)+\lambda U,
\quad 0\le\lambda\le1.
$$

q060 的 $M=8$ 对应保留 $B_2,\ldots,B_6$ 与最后两条新迹方向。
这是改变有限物理空间的路径；$\lambda=0$ 为完整原余弦七列，
$\lambda=1$ 为 R44 新空间，不能把后者称为旧 raw 空间的坐标变换。

## 2. 全路径的有限列独立性

**命题。** 对每个 $\lambda\in[0,1]$，以上 $M-1$ 列线性独立，
且始终具有真低两矩为零、偶对称、三重对称和 $C^4$ 正则性。

**证明。** 正则性、对称性和两矩条件由线性组合直接保留。
设 $\sum_{j=2}^M z_j C_j^\lambda=0$。

若 $0\le\lambda<1$，限制到保护开弧得到

$$
(1-\lambda)\sum_{j=2}^M(-1)^jz_j\cos(3jx)
+\lambda z_{M-1}
+\lambda(z_M-z_{M-1})\cos x=0.
$$

频率 $0,1,6,9,\ldots,3M$ 互不相同。这些余弦在任一开区间
线性独立：有限余弦和实解析，在开区间恒零先推出全域恒零；再在
$x=0$ 取各阶偶导数，得到关于不同频率平方的 Vandermonde 系统，
其行列式非零。因此每个高频系数
$(1-\lambda)(-1)^jz_j=0$，从而所有 $z_j=0$。
该论证包括 $\lambda=0$。

若 $\lambda=1$，保护开弧上先有

$$
z_{M-1}+(z_M-z_{M-1})\cos x=0.
$$

因为 $a>0$，常数与 $\cos x$ 在该开弧上独立，故最后两系数为零。
剩下 $\sum_{j=2}^{M-2}z_jB_j=0$。由 $a+b<T_0/2$，
存在非空开区间 $W>0$；在那里除以 $W$ 得

$$
\sum_{j=2}^{M-2}z_j\cos(3j\phi)-A-B\cos(3\phi)=0
$$

（$A,B$ 为相应系数和）。不同频率的解析独立性再次给所有
$z_j=0$。证毕。

**固定 $M$ 的定性推论。** 取一个周期上的标准 $L^2$ 内积，
这些列的 Gram 矩阵连续依赖 $\lambda$，且每一点正定。
等价地，单位系数球面与 $[0,1]$ 上的
$\|\sum z_jC_j^\lambda\|_{L^2}^2$ 是连续正函数；紧性给出某个
严格正的全路径下界。因此固定有限空间不会因 $\lambda\to1$
出现列秩丢失。

本条没有计算该下界。它不提供可用条件数，也不证明带离散残差、
入口／尾边界和参数尺度的实际 BVP Jacobian 可逆。
不能借用其他空间的 R42/R43 数值条件数。固定非零对角
parameter scales 不改变解析列秩，但可能改变数值条件与 Newton
步长度量；这里没有支付其定量估计。

## 3. 真主矩规范与表示 gauge 分开

固定主形变的窗口、相位和参数。若主支持函数的定义
$f_\lambda=(1-\lambda)f_0+\lambda f_1$ 且
$f_0=\cos(3\phi)$，令 $P_\lambda$ 为它的真 $\cos(3\phi)$ 系数，
则

$$
P_\lambda=(1-\lambda)+\lambda P_1.
$$

已有真主矩绑定给该 q060 目标 $P_1>0$，所以在整个闭区间
$P_\lambda>0$。对任意固定 $Q_*>0$ 定义

$$
q_{\rm support}(\lambda)=\frac{Q_*}{P_\lambda}.
$$

本次承接原 q060 的实际规范取字面 binary64 `.06` 所代表的精确
实数

$$
Q_*=\frac{1080863910568919}{18014398509481984}
=\frac3{50}-\frac1{25\cdot2^{54}}.
$$

不能将该原机器输入默认为精确十进制 $3/50$；若另选 $3/50$，
解析命题仍成立，但应作为另一个幅值规范记录。

由于所有 $C_j^\lambda$ 的该真矩为零，精确定义核的主系数恒为
$q_{\rm support}P_\lambda=Q_*$。这里引用的是已有
[主矩匹配推导](../notes/2026-11-18-m3-circle-primary-matched-amplitude.md)
及 [q060 绑定](../notes/2026-11-18-q060-m8-circle-trace-design-binding.md)，
没有重算旧矩或扫描新幅度。

拟议有限表示独立保留 $q_g=.06$ 的表示 gauge、原 parameter
scales 和 warp reference；$q_{\rm support}$ 作为定义核的 seed
幅值另传。两个量的语义不能混合。浮点实现的主矩误差、除法舍入
及路径上每个核的正曲率半径下界均需分别核验。
该规范不保证中间有限投影入口具有定义核的同一支持函数或真矩。

## 4. 同步启用 lift 的入口恒等式

旧 q060 已接受有限图没有完整 exact-core lift。仅证明
$\lambda=0$ 的定义核等于原余弦核，不能证明新实现承接了同一张
有限图；尤其不能直接开启一个原来不存在的带外修正。

以下是明确的表示方案。固定原材料图、有限场评价算子
$\mathcal B$、表示 gauge $q_g$ 和原背景。
记入口背景为 $b(\psi)$，定义曲线在该材料图中的位置为
$\Gamma_\lambda(\psi)$。设原入口系数投影为 $\mathcal P$，定义

$$
I_\lambda=q_g^{-1}\mathcal P(\Gamma_\lambda-b),\qquad
H_\lambda=\Gamma_\lambda-b-q_g\mathcal B I_\lambda.
$$

下列恒等式不依赖 $\mathcal P$ 是否为精确正交投影；它依赖
同一个 $I_\lambda$ 同时出现在边界与 $H_\lambda$ 中。
令参考几何为

$$
G_\lambda(s,\psi)=G_{\rm bg}(s,\psi)
+\lambda a(s)\chi_{\rm rad}(s)H_\lambda(\psi),
$$

且入口仍为 $Y(0)=I_\lambda$。在原入口归一化
$G_{\rm bg}(0,\psi)=b(\psi)$、$a(0)\chi_{\rm rad}(0)=1$
下，完整有限入口是

$$
F_\lambda(0,\psi)
=(1-\lambda)\{b+q_g\mathcal B I_\lambda\}
+\lambda\Gamma_\lambda.
$$

于是 $\lambda=0$ 恢复原无 lift 的有限投影入口；
$\lambda=1$ 在表示代数中恢复真定义曲线，中间入口通常不同于
$\Gamma_\lambda$。不能把定义核的弧长、支持函数、曲率或真矩证书
直接移给这个中间有限入口。

若原背景、材料图、有限场、gauge 和物理径向 profile 都保持相同，
在 $\lambda=0$ 将任意完整旧 $Y(s)$ 原样放入，整个显式有限场
$G_{\rm bg}+q_g\mathcal B Y$ 的表达式都相同，而不只入口相同。
实际程序仍须使用原 cosine 构造、原无 lift 分支与原保存数据
核对机器身份；不能用新积分实现的数学等价替代它。
旧 BVP 的有限边界残差也不因这条恒等式自动变成零。

## 5. 参数导数、两 jet 与均值的边界

在一个固定 $\lambda$ 下，核心控制参数保持背景、材料图、gauge
和径向 profile 不变，因此

$$
D H_\lambda=D\Gamma_\lambda-q_g\mathcal B\,D I_\lambda.
$$

参考 lift 对核心控制的 $H,H_\psi,H_{\psi\psi}$ 变分以及
径向导数中的 $(a\chi_{\rm rad})'D H$ 项，都要乘同一个
$\lambda$。入口的 $D I_\lambda$ 不乘 $\lambda$，因为边界仍是
$Y(0)=I_\lambda$。Frenet/state Jacobian 必须使用包含相同部分 lift
的实际 frame。改变物理 profile 的 $\delta$ 列另包含径向图和
profile 的变化，不能按上述“固定 profile 控制列”公式漏项；
拟议实现继续保留原有该列差分定义。

若原径向 cutoff 在实际 cut 邻域恒零，则它及前两导数都为零，
显式 lift 的完整二 jet 在那里消失。这保留原尾接口的表示形式；
不表示新的演化状态或实际 tail 数据等于旧值。

虽然这个 planar $H_\lambda$ 没有直接的竖直分量，改变参考几何
仍会改变 Frenet 速度的竖直均值。因此 $\lambda>0$ 的均值高度
必须由原完整高度积分重新构造和审计，不能插值或复用旧均值轨迹。
部分 lift 下也不能沿用完整 lift 专用的“入口误差全为零”元数据；
未计算的实际入口误差应明确标为未计算，保留的 unlifted
projection 诊断应标明它所对应的表示。

## 6. 接续范围

本条只支付新的有限列路径、真主矩规范及同步表示的代数关系。
尚未支付任何 $\lambda>0$ 的核心／Frenet 域、实际 Jacobian 条件、
完整 mean、真尾、有限 metric 或连续几何。路径改变定义核与有限
参考表示，属于新设计，不是固定同一 $g$ 的精化序列。

先检查原完整 q060 的 $\lambda=0$ 机器身份，再检查唯一预声明的
$\lambda=.02$ 模型入口。实际源码、输入和检查计划见
[模型入口记录](../notes/2026-11-18-q060-finite-trace-path-entry-plan.md)；
本条没有执行这些检查，更没有重新运行已失败的 $\lambda=1$
大跨步。合格端点的实际联立、全闭合、同 $g$ 精化和 README
全部验收仍须继续完成。
