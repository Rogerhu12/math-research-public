# R262：Hermite RMS 域梯度与投影正阻尼下降恒等式

## 1. 范围与假设

本结果给出有限维代数恒等式及其完整证明。它不证明当前大核 BVP 有解，
不把优化器驻点当作原方程的零点，也不更改原数值接受门。

固定一个严格递增网格 `s_i`、一个单元长度 `h=s_{i+1}-s_i>0`、该单元中
的固定分数 `t∈[0,1]` 和一个固定 physical angle `phi`。在一次模型与其
trial 中这些值均不随未知量变化。所有物理 Fourier 系数、允许的 core 系数
及全部全局 scalar 参数都保留。

令 `Y_i` 为节点物理系数，`p` 为全局参数，原有限 ODE 为

\[
 f_i=f(s_i,Y_i,p).
\]

假定当前节点处在该 ODE 的光滑实分支内。以下求导针对实际返回的 scalar
字段 `a(s,p)` 与 `nu(s,p)`；`nu` 是原源称作 `ap` 的字段，不额外假定一个
独立有限积分实现的 `a` 对 `s` 求导恰等于 `nu`。

在固定角处，记实际几何角导数为

\[
 d=F_\phi,\qquad e=F_{\phi\phi},\qquad
 Q=d\cdot d>0,\qquad v=d\times e,\qquad W=v\cdot v>0.
\]

原 Frenet 域余量为

\[
 b=\beta^2=1-\left(\frac{\nu}{a\kappa}\right)^2,
 \qquad a>0.
\]

这一个余量不能替代原源其它域条件。尤其原 uniform-phi core density、
scalar 条件、全部节点、中点和两组 RMS 查询仍须真实检查。

## 2. 完整局部域导数

### 命题 262-A

有恒等式

\[
 \kappa^2=\frac{W}{Q^3},\qquad
 b=1-\frac{\nu^2Q^3}{a^2W}.
 \tag{262.1}
\]

任意变分满足

\[
\begin{aligned}
 \delta b={}&-rac{2\nu Q^3}{a^2W}\,\delta\nu
 -\frac{3\nu^2Q^2}{a^2W}\,\delta Q
 +\frac{2\nu^2Q^3}{a^3W}\,\delta a
 +\frac{\nu^2Q^3}{a^2W^2}\,\delta W,\\
 \delta Q={}&2d\cdot\delta d,\\
 \delta W={}&2v\cdot(\delta d\times e+d\times\delta e).
\end{aligned}
\tag{262.2}
\]

这些式子没有除以 `nu`，所以在 `nu=0` 时仍有效。

**证明。** 将 `e` 分解为沿 `d` 和垂直于 `d` 的部分：

\[
 n=e-\frac{e\cdot d}{Q}d.
\]

三维 Gram 恒等式给出
`W=Q(e·e)−(d·e)^2=Q(n·n)`。原曲率为 `sqrt(n·n)/Q`，故
`kappa^2=W/Q^3`，得到 (262.1)。对 (262.1) 逐项用乘积及商法则，再对
`Q=d·d` 与 `W=(d×e)·(d×e)` 用双线性法则，即得 (262.2)。所有分母在
假设内非零。证毕。

令 `c=nu^2/a^2`。为直接生成系数梯度，可等价写成

\[
\begin{aligned}
 g_d&=-\frac{6cQ^2}{W}d+\frac{2cQ^3}{W^2}(e\times v),\\
 g_e&=\frac{2cQ^3}{W^2}(v\times d),\\
 g_a&=\frac{2\nu^2Q^3}{a^3W},\qquad
 g_\nu=-\frac{2\nu Q^3}{a^2W}.
\end{aligned}
\tag{262.3}
\]

这里用了标量三重积
`v·(delta d×e)=delta d·(e×v)` 和
`v·(d×delta e)=delta e·(v×d)`。

固定 physical angle 时，原有限 Fourier 几何的两个角导数是系数向量的
线性映射，记为 `d=D_1 Y`、`e=D_2 Y`。因此

\[
 g_Y=D_1^Tg_d+D_2^Tg_e,\qquad
 g_p^{\rm direct}=a_p^Tg_a+\nu_p^Tg_\nu.
 \tag{262.4}
\]

若原源在随角旋转的正交框架中返回 `d,e`，该框架在此固定角处不随未知量
改变，且旋转保内积和有向叉积，故上述证明和梯度不变。不能因它是旋转框架
而漏掉源 `jet` 本身已有的基向量角导数。

选择某一个实际最坏采样角后，对该**固定角**求导即可，不需求 `argmin`
的导数。若下一 trial 的最坏角改变，仍由完整实际角网格的原域检查处理。
本结论不把固定采样角的梯度冒充全连续角最小值的可微性结论。

## 3. 通过真实 Hermite 查询与 exact chart 拉回

定义标准三次 Hermite 基函数

\[
 h_{00}=(1+2t)(1-t)^2,\quad h_{10}=t(1-t)^2,\quad
 h_{01}=t^2(3-2t),\quad h_{11}=t^2(t-1).
\]

原 RMS 查询物理值是

\[
 Y_t=h_{00}Y_i+h h_{10}f_i+h_{01}Y_{i+1}+h h_{11}f_{i+1}.
 \tag{262.5}
\]

### 命题 262-B

写原节点 Jacobian 为

\[
 J_i=\partial_Y f(s_i,Y_i,p),\qquad
 P_i=\partial_p f(s_i,Y_i,p).
\]

在当前常值 core/control 增广和原 RHS 不显含 core 的表示下，完整变分为

\[
\begin{aligned}
 \delta Y_t={}&(h_{00}I+h h_{10}J_i)\delta Y_i
 +(h_{01}I+h h_{11}J_{i+1})\delta Y_{i+1}\\
 &+h(h_{10}P_i+h_{11}P_{i+1})\delta p.
\end{aligned}
\tag{262.6}
\]

令 (262.4) 在真实查询 `Y_t`、查询位置的 scalar 字段处求值，则完整域
covector 的两个物理节点块和全局参数块为

\[
\begin{aligned}
 g_L&=(h_{00}I+h h_{10}J_i)^Tg_Y,\\
 g_R&=(h_{01}I+h h_{11}J_{i+1})^Tg_Y,\\
 g_p&=h(h_{10}P_i^T+h_{11}P_{i+1}^T)g_Y+g_p^{\rm direct}.
\end{aligned}
\tag{262.7}
\]

**证明。** 对 (262.5) 求导时，网格、查询分数和基函数固定，而两个 `f`
必须各用其真实链式导数 `J delta Y+P delta p`。合并各类变分，得到
(262.6)。再将 (262.6) 代入 `delta b=g_Y·delta Y_t+g_p^direct·delta p`，
对同一节点/参数收集系数，得到 (262.7)。证毕。

这个证明也说明仅插值节点方向、或固定旧 nodal RHS 后求导都会漏项。
在 `t=1/2` 时，(262.5) 为原
`(Y_i+Y_{i+1})/2−h(f_{i+1}−f_i)/8`；两组 RMS 分数也完全适用。

再令 `q` 为 R256 的精确约束坐标。它把内节点物理状态作为独立量，把
全局 `p` 只存一份，并在入口用自由 core 的注入矩阵 `E` 定义

\[
 \delta r_j=\delta c_j,\qquad
 \delta t_j=-2j\,\delta c_j,\qquad \delta z_j=0.
\]

因此，若单元左端是入口，`g_L` 还须拉回为 `E^T g_L`；展开到分量就是
`g_{r_j}−2j g_{t_j}`。其余节点物理块放入各自的独立坐标，全局 `g_p`
只放一次。若原局部 RHS 没有显式 core 列、且单元不邻入口，则该局部
查询 covector 的显式 core 块为零。这不意味着完整 BVP 对 core 不敏感：
完整 collocation 和右边界仍耦合全部自由 core。

若未来改变表示使 RHS 显含 core，必须在 (262.6) 增加相应节点链，不能
沿用这里的零显式 core 列。当前接口对此结构做明确检查。

## 4. 投影正阻尼最小化与真实下降

令 `R(q)` 为当前完整优化残差，包括全部物理 collocation 和全部右边界行。
当 native map 仅以某个已完成响应的 affine 图参与 warm 时，必须明确
`R` 就是该 affine warm 残差，不能冒称所有新 H 的真实 native map 已求解。

固定本模型的正行权重 `W_r` 和正坐标尺度 `S`，写

\[
 b_0=W_r R(q),\qquad A=W_r D R(q)S^{-1},\qquad z=S\delta q.
\]

选择有限个域 covector，把其 scaled 行记为 `B`，即每行
`g_q S^{-1}`。令 `P` 为 `ker B` 的正交投影，`P=P^T=P^2`。
这里只限制**本次优化方向**的一阶域变动；没有把 `B z=0` 添加到原科学
方程或最终验收。

### 命题 262-C

给定 `lambda>0`，受限问题

\[
 \min_{z=Pz}\frac12\|Az+b_0\|^2+
                    \frac{\lambda^2}{2}\|z\|^2
 \tag{262.8}
\]

有唯一的 `z`。其精确解满足

\[
 b_0^T A z=-\|A z\|^2-\lambda^2\|z\|^2.
 \tag{262.9}
\]

故非零精确解给出原加权残差 merit 的严格一阶下降方向。

**证明。** (262.8) 的 Hessian 在 `ran P` 上为 `A^T A+lambda^2 I`
的限制，其二次型至少为 `lambda^2 ||z||^2`，故严格正定并强制有唯一极小值。
在该子空间的一阶最优条件为

\[
 P[A^T(Az+b_0)+\lambda^2z]=0.
\]

左乘 `z^T`，用 `z=Pz` 与 `P=P^T`，得到
`||Az||^2+b_0^TAz+lambda^2||z||^2=0`，即 (262.9)。
若 `z!=0`，右端严格负。证毕。

实际 LSMR 截停时不能直接援用精确最优条件。必须仍算真实
`gdot=b_0^T A z`，只把有限且 `gdot<0` 的方向送入原实际 merit / 完整域
回溯。预测下降仍为

\[
 -\alpha\,gdot-\frac{\alpha^2}{2}\|A z\|^2,
\]

正则项不加入非线性真实 merit。若 `z=0` 或 projected stationarity 成立而
原 `R` 非零，只能报告此优化器停滞，不能宣称 BVP 成功。

对于被保护的固定查询，`Bz=0` 使
`b(q+alpha delta q)=b(q)+O(alpha^2)`，其中使用该查询链的二阶光滑性。
这没有给出统一可用步长，更没有保证其它角或其它查询保持正值。每个 trial
仍须重算原节点 RHS、真实 Hermite 中间值和全部原域条件。

## 5. 列预条件与伴随的次序

### 命题 262-D

设 `C` 为任意正对角矩阵。以环境变量 `v` 参数化
`z=P C^{-1}v`，则 (262.8) 等价于最小化

\[
 \left\|
 \begin{bmatrix}A P C^{-1}\\\lambda P C^{-1}\end{bmatrix}v
 -\begin{bmatrix}-b_0\\0\end{bmatrix}\right\|^2.
 \tag{262.10}
\]

其伴随为

\[
 \begin{bmatrix}A P C^{-1}\\\lambda P C^{-1}\end{bmatrix}^T
 \binom{u}{w}
 =C^{-1}P(A^T u+\lambda w).
 \tag{262.11}
\]

**证明。** `C` 可逆，所以映射 `v -> P C^{-1}v` 的像恰是 `ran P`：
任取 `z=Pz`，可用 `v=Cz` 作为原像。将该参数化代入 (262.8) 即得
(262.10)。所有产生同一 `z` 的环境变量具有同一目标值，环境零空间只是
冗余参数化，不改变唯一的 scaled 物理方向。最后对欧氏内积移项，并用
`C^{-T}=C^{-1}`、`P^T=P`，得到 (262.11)。证毕。

因此恢复方向必须是 `z=P(solution/C)`，不能交换通常不对易的 `P,C^{-1}`。
罚项必须实际计算 `lambda P C^{-1}v`，不能在声称 (262.8) 等价时悄换成
`lambda C^{-1}v` 或使用未投影解的范数。

可以取 `C_j=sqrt(||A e_j||^2+lambda^2)`。它是合法的正预条件；它通常
**不是** `(262.10)` 投影后算子的精确列范数，输出须如实标记。该选择只
影响迭代，不改变 (262.10) 表示的优化问题。

数值实现对多个近相关保护行若使用阈值选取 retained row space，必须记录
该阈值、retained rank 和原行 leakage。此时上述证明适用于实际 retained
space 的投影，不自动证明被舍弃数值方向的所有原 covector 都精确消失。
这仍只影响优化器；原物理 collocation、BC 和全域检查均不删除。一个非零
保护行可直接规范化构造投影，无需数值 rank 判定。

## 6. 当前实际问题与独立接口

request17 的真实限制点见
`notes/2026-11-14-request17-warm-continuation-decision.md`。该点是
interval473 / fraction `0.17267316464601146` / 原 physical-phi 网格 index0，
不是材料角积分网格。两节点位置都在当前三个 scalar bump 支撑之外，
所以当前该行的显式参数块为零；代码仍按完整 (262.7) 生成和检查它，不
用这个特例删掉一般参数链。

独立源 `computations/geometry_20261114_hermite_domain_constraints.py` 提供：

- `HermiteDomainRow(problem,state,interval,fraction,angle_index)`：使用原
  spline 查询、原 `q.jet`、真实两节点完整 Jacobian，生成全部 exact-coordinate
  梯度。保留原法向量表达式的 `beta^2`，另报告交叉积等价表达式的舍入差；
- `row.verify(state)`：用完整原 nodal RHS 与原 spline 重算三类 complex
  方向，并保留三个中心差分层；不将 complex 坐标送入会转实数的 chart；
- `TangentProjector(rows,dimension)`：对显式 scaled optimizer 行生成投影；
- `projected_regularized_operator(A,norms,lambda,P)`：严格提供
  (262.10)、(262.11)，另给正预条件及其真实标签；
- `verify_projected_operator(...)`：供实际完整 A 的消费端核伴随、动作与
  行 leakage，不生成新的科学接受标准。

该独立 CLI 只消费真实保存 warm，核原四输入和全部 producer SHA，检查
一个查询梯度。它不产生新 warm、不调 Node、不解 native tail、不运行新的
完整 collocation 最小化。具体接线见同名接口 note。源只有 AST 静态检查，
本结果不声称已有此新梯度或投影求解的 Actions 数值回执。
