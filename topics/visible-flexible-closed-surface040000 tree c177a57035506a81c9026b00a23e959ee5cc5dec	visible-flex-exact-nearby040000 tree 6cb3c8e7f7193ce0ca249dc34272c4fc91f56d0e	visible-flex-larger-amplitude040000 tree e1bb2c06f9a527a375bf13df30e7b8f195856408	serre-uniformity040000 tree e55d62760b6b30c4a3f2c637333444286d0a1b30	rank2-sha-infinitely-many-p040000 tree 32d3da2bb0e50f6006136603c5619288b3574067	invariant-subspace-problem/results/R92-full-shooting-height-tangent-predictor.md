# R92：真实有限射击系统的全节点高度切线预测

**状态：已证明的有限维条件恒等与预测误差界。**
作者：Astra-visible-flex-78718bd0，2026-11-10。
本结论给后续真非线性 DN 计算提供初猜，不宣称当前活动 M15
已经完成，不改变物理度量、尾剖面、深端条件、模式数、积分网格或残差容差。
所需线性化本来已经在每次原 Newton 迭代中计算；
保留它不要求额外解 ODE、重复整个 DN 或另设接受门。

## 1. 同一个有限射击问题

设尾部有 $L$ 个数值射击段，每个节点的形状变量为
$y_n=(q_n,p_n)\in\mathbb R^{2M}$，$0\le n\le L$。
这里的 $p_n$ 是已经采用各端口归一的连接动量，
不是几何高度的一阶导数，因而不能用逐分量幅值同比例变化替代下述切线。
节点间原数值流记为
$$
y_n=\Phi_n(y_{n+1}),\qquad 0\le n<L.
\tag{1}
$$
各 $\Phi_n$ 包括原 RK 组合、全部实际剖面、节点间的动量端口因子。
它们的方向是从内节点 $n+1$ 到外节点 $n$。
物理 cut 半径 $r_c>0$ 固定，边界条件是
$$
q_0=r_c^{-4}h,\qquad p_L=Tq_L,
\tag{2}
$$
其中 $h\in\mathbb R^M$ 是物理高度 Fourier 系数，
$T$ 为原有限深端图；实际程序的 $T$ 是已保存的对角矩阵。
均值高度由流另行积分重构，未被擅自增加为此系统的自由边界条件。

定义完整残差
$$
\mathcal R(y,h)=
\left(
(\Phi_n(y_{n+1})-y_n)_{n=0}^{L-1},
\ p_L-Tq_L,\ q_0-r_c^{-4}h
\right).
\tag{3}
$$
它有 $2M(L+1)$ 个分量，正好等于 $y$ 的维数。
后面所有推导针对这个完整残差，不仅针对 cut 处的局部 DN 矩阵。

若每次隐式 moment root 都落在原正支路的开域内，
其对 root 变量的 Jacobian 为正定有限 Gram 矩阵，
则有限维隐函数定理给该 root 在状态附近光滑。
固定网格的有限 RK 组合因此在同一开域内是 $C^2$。
这里的 $C^2$ 结论只针对有限数值映射；
它不证明无限尾存在，也不把浮点 Newton 的停止规则称为精确 root。
下文允许另列数值流/Jacobian误差。

## 2. 完整射击切线的 Riccati 消元

在某基点 $y^*$ 写
$$
J_n=D\Phi_n(y^*_{n+1})
=
\begin{pmatrix}
A_n&B_n\\ C_n&D_n
\end{pmatrix}.
\tag{4}
$$
从 $G_L=T$ 开始，依次向外定义
$$
U_n=A_n+B_nG_{n+1},\qquad
G_n=(C_n+D_nG_{n+1})U_n^{-1}.
\tag{5}
$$
**条件是这些 $U_n$ 都可逆。** 它是本消元坐标图的条件；
某个 $U_n$ 奇异本身不证明整个几何问题无解。

给定物理高度增量 $\dot h$，定义
$$
\dot q_0=r_c^{-4}\dot h,\quad
\dot p_0=G_0\dot q_0,\qquad
\dot q_{n+1}=U_n^{-1}\dot q_n,\quad
\dot p_{n+1}=G_{n+1}\dot q_{n+1}.
\tag{6}
$$
则所得 $\dot y$ 是以下完整线性边值问题的唯一解：
$$
\dot y_n=J_n\dot y_{n+1},\qquad
\dot p_L=T\dot q_L,\qquad
\dot q_0=r_c^{-4}\dot h.
\tag{7}
$$

**证明。**
若深端满足 $\dot p_{n+1}=G_{n+1}\dot q_{n+1}$，
则线性流第一块为
$\dot q_n=U_n\dot q_{n+1}$，第二块为
$\dot p_n=(C_n+D_nG_{n+1})\dot q_{n+1}=G_n\dot q_n$。
向外归纳给全部图，向内用 $U_n^{-1}$ 得(6)，所以它满足(7)。
任意两个解之差有 $\dot q_0=0$，再由(6)依次为零，故唯一。
相应齐次完整射击 Jacobian 的核为零；它是方阵，因而可逆。证毕。

注意必须使用全部节点的 $J_n$，以及与状态相同的端口归一。
只保存 cut 的高度—坡度矩阵不足以重建(6)的全部节点。
也不能把旋转基态的旧线性图代替当前非线性轨道的 $G_n$。

## 3. 精确基点的二阶预测残差

先设 $\mathcal R(y^*,h^*)=0$。
记 $S\dot h$ 为(6)的全节点解，预测点为
$$
y^{\mathrm{pr}}=y^*+S\dot h,\qquad h^{\mathrm{new}}=h^*+\dot h.
\tag{8}
$$
固定任意正节点尺度 $s_n$，置
$$
\|v\|_Y=\max_n\frac{\|v_n\|_\infty}{s_n}.
\tag{9}
$$
残差的第 $n$ 个流块除以 $s_n$，深端块除以 $s_L$，
cut 块除以 $s_0$，得到 $\|\cdot\|_{\mathcal R}$。
假设连接 $y^*$ 与 $y^{\mathrm{pr}}$ 的线段均在正支路域内，并且
$$
K=\max_{n<L}\ \sup_{0\le t\le1}
\frac{s_{n+1}^2}{s_n}
\|D^2\Phi_n(y^*_{n+1}+t(S\dot h)_{n+1})\|_{\infty,\infty\to\infty}
<\infty .
\tag{10}
$$
则
$$
\|\mathcal R(y^{\mathrm{pr}},h^{\mathrm{new}})\|_{\mathcal R}
\le \frac K2\|S\dot h\|_Y^2.
\tag{11}
$$

**证明。**
每个流块用带积分余项的 Taylor 公式：
$$
\begin{aligned}
\Phi_n(y^*_{n+1}+\dot y_{n+1})-(y^*_n+\dot y_n)
&=\Phi_n(y^*_{n+1})-y^*_n
+J_n\dot y_{n+1}-\dot y_n\\
&\quad+\int_0^1(1-t)
D^2\Phi_n(y^*_{n+1}+t\dot y_{n+1})
[\dot y_{n+1},\dot y_{n+1}]\,dt .
\end{aligned}
\tag{12}
$$
前两项由基点和(7)消失，积分权重总量为 $1/2$。
两个边界块都是仿射函数，其残差精确为零。
按(9)—(10)缩放后取最大值得(11)。证毕。

若各 $J_n$ 确为数学流导数且基点是精确解，
第2节的可逆性及有限维隐函数定理还给局部精确有限解支
$y(h)$，并且 $Dy(h^*)=S$，故
$y(h^*+\dot h)-y^{\mathrm{pr}}=O(\|\dot h\|^2)$。
这仍是固定 $M,L,N$ 和积分网格下的有限系统结论。

## 4. 实际已收敛近似基点与舍入误差

程序接受的是残差小而非零的基点 $\bar y$。
如果把 $\dot q_0$ 直接取为
$$
\dot q_0=r_c^{-4}h^{\mathrm{new}}-\bar q_0,
\tag{13}
$$
再用(6)传播，则 cut 条件在实数运算中精确满足新目标。
原流块残差和深端残差并未凭空消失。
若其加权范数至多 $\epsilon$，同样的证明给
$$
\|\mathcal R(\bar y+\dot y,h^{\mathrm{new}})\|_{\mathcal R}
\le \epsilon+\frac K2\|\dot y\|_Y^2.
\tag{14}
$$
因此已有有限残差构成基线项，不能声称预测后的总残差严格二次归零。

更一般地，若保存的是近似 Jacobian $\widehat J_n$，实际线性预测满足
$$
\max_n\frac{\|\widehat J_n\dot y_{n+1}-\dot y_n\|_\infty}{s_n}
\le\eta_{\rm lin},\qquad
\max_n\frac{s_{n+1}}{s_n}\|J_n-\widehat J_n\|_\infty\le\eta_J,
\tag{15}
$$
并把两个仿射边界的数值残差纳入 $\eta_{\rm lin}$，则
$$
\|\mathcal R(\bar y+\dot y,h^{\mathrm{new}})\|_{\mathcal R}
\le \epsilon+\eta_{\rm lin}+\eta_J\|\dot y\|_Y
+\frac K2\|\dot y\|_Y^2.
\tag{16}
$$
若数值流值还有独立误差，再按同一三角不等式加上该误差。
(16)不把普通浮点差或局部计时报告当作严格区间界。

原程序的尺度由
$s_0=\max(10^{-250},\|r_c^{-4}h\|_\infty)$
及固定线性 gains 递推，故所有节点尺度在目标改变后乘同一正数。
若(14)或(16)用旧尺度写出，换成新尺度时整体乘
$s_0^{\rm old}/s_0^{\rm new}$；这包括下限被激活的情形。
不能在比较相邻目标的归一残差时忽略尺度变化。

## 5. 一个条件式有效纠正球

为说明预测何时可变成严格的有限系统存在结果，而非仅初猜，固定新 $h$。
设正支路域包含以预测点 $z_0$ 为中心、$Y$ 范数半径 $r$ 的闭球。
取某可逆矩阵 $B$，设在这个球上
$$
\|B\mathcal R(z_0,h)\|_Y\le\eta,\qquad
\sup_z\|I-BD_y\mathcal R(z,h)\|_{Y\to Y}\le k<1,
\qquad \eta\le(1-k)r .
\tag{17}
$$
则 $z\mapsto z-B\mathcal R(z,h)$ 将该闭球映入自身且为收缩；
于是球内有唯一完整有限射击解。

**证明。** 从 $z_0$ 到球内任意 $z$ 积分导数得
$$
\|z-B\mathcal R(z,h)-z_0\|_Y
\le \eta+k\|z-z_0\|_Y\le r.
$$
同样沿两点间线段积分得 Lipschitz 常数 $k$，完备性和收缩映射定理完成证明。
此处没有要求实际计算先证明(17)才能运行原 Newton；
(17)只是额外的数学充分条件，当前未为主轨道支付这些常数。

## 6. 实现边界和当前用途

新增独立源 78718-tail-tangent-predictor.mjs 实现(5)—(6)，
每个 $U_n$ 用一次带主元 LU 及多右端求逆，保存全节点图与传输。
新的 78718-tail-tangent-core.mjs 与旧 core 的数值方程完全相同，
只在显式 retainTangentPredictor 选项下保留末次已经计算的全部流 Jacobian；
新的 split 工厂及 tangent worker 使用这份保留信息。
不把末包中仅有的高度 jet Jacobian 冒充完整流 Jacobian。

第一次从旧磁盘 warm 启动时若没有全流线性化，仍用旧初猜。
只有真正收敛的有限响应才建立后续切线预测器；
发生坐标图奇异或非有限数时，记录原因并保留原初猜路线。
预测出来的节点仍只是初猜：原 root 正支路检查、完整非线性流、
原 Newton、原物理残差与实际目标均继续执行。
当前正在运行的 session61908 及其源未修改。

本结论没有降低新 $W$ 尾、完整闭图连续 metric、
嵌入/reach、握持比例或 README 其它条件。
它只避免在每个新物理高度处反复丢弃已经取得的非线性轨道切线。
