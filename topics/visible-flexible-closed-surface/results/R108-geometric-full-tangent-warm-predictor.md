# R108：同一全射击切线的几何初猜与二阶预测界

2026-11-10，Astra-visible-flex-78718bd0 / independent_audit。

**状态：有限维条件命题已证明；另名可选实现已写，尚未实际运行这个新初猜。**
本结果把 [R92](R92-full-shooting-height-tangent-predictor.md) 的自身全射击切线
与 [R95](R95-same-residual-geometric-newton-retraction.md) 的中心化 Q/L 回缩组合，
只改变下一次真实 DN 的初猜。
它保留同一个物理高度目标、有限方程、原 mean/root 分支和阈值、端口归一、
深端 Robin 条件、原 RK 网格以及全部原非线性接受条件。

与现有模块的区别是明确的：活动 `partition-centered-worker` 已在 Newton **trial**
中使用 centered-v3，但新高度的 **warm predictor** 仍是 R92 的 $(Q,\pi)$ 直线。
本文提供后一位置的可选几何路径，不重复实现原 Newton trial。
当前 fast07 及其源没有改动；没有为本文另跑 DN、整尾或某个 stage。

## 1. 原完整切线及其已有输入

沿用 R92 的记号。共有 $L$ 个射击段，每节点
$y_n=(Q_n,\pi_n)\in\mathbb R^{2M}$，原数值流方向是

$$
y_n=\Phi_n(y_{n+1}),\qquad 0\le n<L.
\tag{1}
$$

各 $\Phi_n$ 包含原全部 RK 子步、真实 profile 和动量端口因子。
边界为

$$
Q_0=r_c^{-4}h,\qquad \pi_L=TQ_L.
\tag{2}
$$

在某个自己的已收敛有限响应 $\bar y$ 上，R92 用全部已计算的
$J_n=D\Phi_n(\bar y_{n+1})$，从原深端图 $T$ 做 Riccati 消元。
在该消元所需矩阵可逆时，对新目标 $h_1$，其全节点方向 $v$ 满足

$$
v_n=J_nv_{n+1},\qquad
v_{L,\pi}=Tv_{L,Q},\qquad
v_{0,Q}=r_c^{-4}h_1-\bar Q_0.
\tag{3}
$$

具体是 R92 式 (5)–(7) 的唯一解，没有重新选择方向或改变物理参数。
令 $h_0=r_c^4\bar Q_0$，则沿参数 $\lambda$ 的目标可写成

$$
h_\lambda=h_0+\lambda(h_1-h_0).
\tag{4}
$$

即使已收敛基点对原请求的 cut 条件还有有限小残差，这个定义也使基点的 cut 条件
相对 $h_0$ 精确；原流块和深端残差仍完整保留，不能把它们置零。

所需的是该响应的**全部流 Jacobian**。一个末包仅有 cut 的 height-jet Jacobian，
不能据此恢复 (3)；本文实现只消费原 worker 内存中已经保留的
`linearizedFlowJacobians`，不会用旧旋转态线性图代替。

## 2. 同一方向在 raw Q/L 中的表达

固定节点 n。令 $D_n$ 为 stored 坐标到当前 engine 坐标的线性变换：
Q 块恒等；通常动量块也恒等，只有 node0 的动量乘该节点实际 `portRatio`。
令

$$
z_n=\chi_n(D_n\bar y_n)=(Q_n,R_n),\qquad
R_{n,j}=\frac{\sqrt2w_n}{\sqrt{12}r_n^3}L_{n,j},\quad j\ge1.
\tag{5}
$$

这里 $L_0$ 已由同一个零均值连接矩方程消去。
R95 §§1–3 在严格正分支内证明 $\chi_n$ 是局部光滑坐标，
其逆 $C_n$ 的实际计算就是重解**原来的**均值方程，再投影回动量。

为明确第一阶方向没有被替换，原完整矩方程在 engine 坐标中是

$$
\mathcal M_0(Q,L)=0,\qquad
\mathcal M_j(Q,L)=\tau_n\pi_j,\quad
\tau_n=\frac{\epsilon\sqrt{12}\mu_n}{\sqrt2r_n^4w_n^2}.
\tag{6}
$$

在原正支路上，关于所有 $L_j$ 的导数是正定 Gram 矩阵

$$
B_{ij}=\mathcal Q\!\left[\frac{A}{D^{3/2}}c_ic_j\right].
\tag{7}
$$

所以从 (3) 的同一个节点方向，解

$$
B\dot L_n=
\begin{pmatrix}0\\\tau_n(D_nv_n)_\pi\end{pmatrix}
-\mathcal M_Q(v_n)_Q
\tag{8}
$$

就得到

$$
\dot z_n=D\chi_n(D_n\bar y_n)D_nv_n
=\left((v_n)_Q,
\frac{\sqrt2w_n}{\sqrt{12}r_n^3}\dot L_{n,h}\right).
\tag{9}
$$

$\mathcal Q$ 仍是原来的有限 N 点平均，式 (8) 的 $\mathcal M_Qv_Q$
使用 R95 式 (9)–(11) 的完整同节点微分。
这些运算不改变角投影或原 alias，不做新的 ODE。

### 均值只作一阶预测，然后必须重解

对 $z_n+\lambda\dot z_n$，均值初值取

$$
L_{n,0}^{\rm guess}=L_{n,0}+\lambda\dot L_{n,0}.
\tag{10}
$$

在固定节点附近，$B_{00}>0$ 给出唯一光滑均值函数，(8) 给其准确一阶导数。
因此 (10) 同真正均值的误差是 $O(\lambda^2\|v_n\|^2)$。
这只说明它是局部良好起点，不表示 mean 本身线性，也不自动保证某个有限大步仍在正支路。
实现复用原 centered-v3/v2 的均值方程、原30次迭代、20档回退、原阈值及 floor。
求根失败仍是构造失败，不能把初值当作已经求出的均值。

## 3. 中心化回缩和两个边界

对所有节点，先使用 R95 的中心式

$$
\mathscr R_{\bar y}(\lambda v)_n
=\bar y_n+D_n^{-1}
\left\{
C_n(z_n+\lambda\dot z_n)-C_n(z_n)
\right\}.
\tag{11}
$$

准确坐标满足 $C_n\circ\chi_n=I$，所以这与普通 raw 回缩精确相同。
但在浮点实现中，两个正向投影先作差再写回原动量，可以消除 R95 §9 的零方向 roundtrip 偏置。
node0 的两个 engine 动量先相减，再除一次真实 `portRatio`；不各自换坐标后再补差。

因为 Q 在两套坐标中都是同一个 Q，准确地有

$$
(\mathscr R_{\bar y}(\lambda v)_n)_Q
=\bar Q_n+\lambda(v_n)_Q.
\tag{12}
$$

为了不给原仿射深端条件增加二阶漂移，定义实际几何预测曲线为

$$
\mathscr G_{\bar y}(\lambda v)_n
=\begin{cases}
\mathscr R_{\bar y}(\lambda v)_n,&0\le n<L,\\
\bar y_L+\lambda v_L,&n=L.
\end{cases}
\tag{13}
$$

由于 (12)，这只需要把最后一个节点的动量块恢复为原线性预测值；
Q 块本来已经相同。

### 命题 1：准确边界、零步和一阶方向

在上述局部坐标存在的范围内，

$$
\mathscr G_{\bar y}(0)=\bar y,\qquad
\left.\frac d{d\lambda}\mathscr G_{\bar y}(\lambda v)\right|_{\lambda=0}=v,
\tag{14}
$$

且

$$
(\mathscr G_{\bar y}(\lambda v)_0)_Q=r_c^{-4}h_\lambda,
\tag{15}
$$

$$
(\mathscr G_{\bar y}(\lambda v)_L)_\pi
-T(\mathscr G_{\bar y}(\lambda v)_L)_Q
=\bar\pi_L-T\bar Q_L.
\tag{16}
$$

**证明。** 在每个节点对 (11) 求导，$DC_n(z_n)D\chi_n(D_n\bar y_n)=I$，
再乘回 $D_n^{-1},D_n$，就给相同的 $v_n$；在深端 (13) 已是直线。
零步在 (11) 中两项完全相同。由 (12) 和 (3) 得 (15)；
由 (13) 和 $v_{L,\pi}=Tv_{L,Q}$ 得 (16)。证毕。

式 (16) 保留已收敛近似基点自己的深端小缺陷；并非悄悄把它宣称为零。
若实际线性求解在该边界有舍入误差，则相应多出其线性边界误差，仍须计入原残差。

### 命题 2：二阶预测性及可量化偏差

取原 R92 的正节点尺度 $s_n$，使用

$$
\|v\|_Y=\max_{0\le n\le L}\frac{\|v_n\|_\infty}{s_n}.
\tag{17}
$$

若固定基点的回缩在所用方向邻域内为 $C^2$，且

$$
\sup_{0\le t\le1}
\|D_v^2\mathscr R_{\bar y}(tv)\|_{Y,Y\to Y}\le2C_R,
\tag{18}
$$

则

$$
\boxed{\quad
\|\mathscr G_{\bar y}(v)-(\bar y+v)\|_Y
\le C_R\|v\|_Y^2.
\quad}
\tag{19}
$$

**证明。** 对固定基点的映射 $v\mapsto\mathscr R_{\bar y}(v)$
在原点使用 Taylor 积分余项。其值是 $\bar y$、一阶导数是恒等，故

$$
\mathscr R_{\bar y}(v)-\bar y-v
=\int_0^1(1-t)D_v^2\mathscr R_{\bar y}(tv)[v,v]\,dt.
\tag{20}
$$

积分权重为 $1/2$，给上界 $C_R\|v\|_Y^2$。
由 (12)，此偏差的全部 Q 块为零。
(13) 只将深端偏差的动量块也置零，因此在 (17) 的逐节点最大范数中不会增大偏差。
这里不需要乘上可能很大的 $\|T\|$。证毕。

若基点为准确有限根且 R92 的完整 Jacobian 可逆，隐函数定理给自身有限解支
$y(h)$，其一阶导数正是 (3)。于是

$$
y(h_1)-\mathscr G_{\bar y}(v)=O(\|h_1-h_0\|^2).
\tag{21}
$$

证明是 R92 的 $y(h_1)-\bar y-v=O(\|h_1-h_0\|^2)$ 与 (19) 相加，
并使用有限维线性切线映射的有界性。
本结论仍只关乎固定有限模式、网格与深端图下的系统，不能升级为无限尾存在定理。

## 4. 对原完整残差的二阶界

令 $\mathcal F(y,h)$ 为 R92 式 (3) 的完整残差，包含所有射击流块和两端条件。
固定与 (17) 相容的残差尺度。
设基线流和深端误差不超过 $\varepsilon$；原 Jacobian 和线性求解误差分别按 R92 的
$\eta_J,\eta_{lin}$ 控制。令 $K$ 是原流沿 canonical 预测线段的二阶常数，
即 R92 式 (10) 的常数。

再设 $\bar y+v$ 到 $\mathscr G_{\bar y}(v)$ 的连接线段也在同一可定义域内，且

$$
\|D_y\mathcal F(y,h_1)\|_{Y\to\mathcal F}\le L_F
\tag{22}
$$

在这条线段上成立。则

$$
\boxed{\quad
\|\mathcal F(\mathscr G_{\bar y}(v),h_1)\|_{\mathcal F}
\le\varepsilon+\eta_{lin}+\eta_J\|v\|_Y
+\left(\frac K2+L_FC_R\right)\|v\|_Y^2.
\quad}
\tag{23}
$$

**证明。** R92 的完整 Taylor 证明给

$$
\|\mathcal F(\bar y+v,h_1)\|_{\mathcal F}
\le\varepsilon+\eta_{lin}+\eta_J\|v\|_Y+\frac K2\|v\|_Y^2.
$$

沿 (22) 所用线段积分一阶导数，并使用 (19)，得到两次残差的差不超过
$L_FC_R\|v\|_Y^2$；两式相加即得。证毕。

若 mean/root、方向换坐标、中心作差或流值另有数值误差，应按同样范数另加其影响。
式 (23) 没有把浮点停止阈值当成准确求根，也没有宣称本轮主轨道已经有这些严格常数。
使用旧目标的尺度写出本式时，换到新目标的原尺度仍须乘 R92 §4 给出的统一尺度比。

### 为什么没有“必然比直线更好”的结论

这两个预测共享一阶项，差别首先出现在二阶。
令 $a(v,v)=D_v^2\mathscr G_{\bar y}(0)[v,v]$。
在准确基点与切线下，$C^2$ Taylor 展开给

$$
\mathcal F(\mathscr G_{\bar y}(v),h_1)
=\frac12\left\{
D_y^2\mathcal F(\bar y,h_0)[v,v]
+D_y\mathcal F(\bar y,h_0)a(v,v)
\right\}
+o(\|v\|_Y^2).
\tag{24}
$$

$h$ 只在 cut 块仿射出现，所以没有额外的混合二阶项。
canonical 直线只有大括号第一项；新项可能抵消它，也可能同向增加它。
因此 (23) 是二阶阶数的保留，**不是误差常数的改善证明**。
同样，raw 大步的允许域不因这个构造而自动凸；新均值初猜或者最终中心输出
仍可能被原分支 floor 拒绝。将其实际接入，只是一种有数学控制的可选初猜实验。

## 5. 已保存源码的准确接线

新增两份源，原文件和活动 worker 均不修改：

- [方向返回 companion](../scripts/78718-tail-tangent-predictor-with-direction.mjs)：
  同原 `78718-tail-tangent-predictor.mjs` 的 Riccati/LU、矩阵乘法、方向及 state 加法顺序，
  只在返回对象中额外返回已有的 `direction: delta`。
- [几何切线 warm](../scripts/78718-tail-geometric-tangent-predictor.mjs)：
  消费上述方向，直接调用既有 centered-v3 的 `prepareGeometricShootingRetraction`，
  然后按 (13)、(15) 处理边界。

保留已有 delta 有实际目的：不能先形成浮点 `base+delta`，再用它减去 base 恢复小方向，
那样会再丢失一次低位。companion 不重新求任何 ODE，也不改变原方向的算术表达式。

新模块导出

```javascript
createPhysicalHeightTangentPredictor(
  solution, farGraph, radius,
  {cells: dn.tail.cells, spacing: cfg.spacing}
)
```

返回对象仍有 `.maxChartCondition` 和 `.predict(height)`，后者仍返回
`{states, diagnostics}`，因此可作为将来新 worker 的显式可选项。
可选 `.predict(height,{lambda})` 仅把同一方向用于 (4) 的中间步；默认 $\lambda=1$。
没有为它新增任何物理 config 字段。

具体保证与限制如下。

1. node0 的 engine/profile/x/portRatio 选择完全交给原 centered-v3 全节点 helper，
   使用自己的实际 cell，不把 ratio 换成 1。
2. 在 $\lambda=1$，node0 的全部 Q 槽最后取 companion 中直接除出来的 `height/radius**4`，
   包括高模；这是原 R92 的同一 binary Dirichlet 值。
3. 深端动量取原 canonical tangent 的同一值。准确算术下保持 (16)；
   浮点中保留原线性运算舍入，不冒称深端缺陷逐位完全相同。
4. $\lambda=0$ 直接复制基点，不作新的 root 或 raw roundtrip。
   完全相同的 binary cut 目标且全方向为零时，也直接复制基点。
   其它非零方向仍使用中心式，不能由这两个分支宣称任意小步没有舍入误差。
5. mean/raw 构造异常仍抛给原 worker 的 warm fallback。
   构造成功后仍必须调用原完整非线性 `solve/evaluate`，包括中心输出自己的 root/branch 检查。
   新输出不是一次已接受的 Newton 步，也不是 DN 响应。

模块报告 canonical 与几何初猜的最大坐标差、边界重新赋值差、基点准备 A/D 和准备耗时。
这些是 state 坐标和初猜诊断，不是曲面 metric 或 reach。
它不调用 stage flow，额外成本来自有限节点的 root、方向 SPD 解和原 mean 重求；
实际总成本尚未测量，不能把“零 ODE”写成“零计算成本”。

本轮仅实际完成两件新源的 `node --check`：`ba35ae exit0`、`98fb50 exit0`；
以及 `24b3cf exit0` 对 companion 去掉新增注释/返回字段后同原文本的直接相等检查。
这只确认源码/语法范围，不构成新初猜的实际性能或收敛证据。

## 6. 当前 call9 到 call10 的真实范围

只读活动 fast07 已有 trace 的一个完整行前缀，得到以下事实；
本次没有消费 root 的求解器工具会话，也没有重新计算任何原 flow。

| 已有请求 | 目标幅度 | 最大相对切线增量 | 首 shooting norm | 首 min A | 首最坏段 |
| --- | ---: | ---: | ---: | ---: | ---: |
| call9 | $25/32$ 原 h | $.1599746712$ | $913.7334261$ | $.4306465$ | 84 |
| call10 | $107/128$ 原 h | $.1637126381$ | $792.6071596$ | $.3740379$ | 84 |

call9 由原程序随后真实降到 $1.0528345037\cdot10^{-9}$ 并收敛。
在所读取的 call10 前三次完整迭代中，norm 为约 $792.61,391.57,195.96$，
min A 为约 $.3740,.08990,.10297$。它们仅是该观察前缀的状态，
不能外推 call10 后来的自然结果，也不是整曲面 metric。

约 $.16$ 的全节点相对增量并不处在已经量化为“二阶项可忽略”的范围。
它使换一条二阶路径成为合理的数值尝试，但原 trace 没有给出 $C_R,K,L_F$，
也没有给新路径的实际初始残差。
尤其 call10 的最小 A 是在后续 Newton 过程中降低，不能只由此归因于 warm 坐标。
本结果因此只说**可能改变初猜及后续迭代路径，改善与否未知**。

保存的纯标量上下文见
[几何切线 warm 的既有 trace 上下文](../notes/2026-11-10-78718-geometric-tangent-warm-trace-context.json)。
它记录所读活动文件前缀的长度、SHA 和观察时刻；后续追加不在该前缀身份内。
没有把 active trace 锁住或覆盖，也没有把已收敛中间高度的包称为原高度成功。

## 7. 当前使用边界

这是另一份可选 warm 工具，供将来显式选用；当前 fast07 不换源。
必须等自己的真实已收敛响应及其全部已算流 Jacobian 才能建立这个预测器。
如果当前磁盘包未存全流 Jacobian，不能用高度 jet 矩阵或旧图来代替，
也不为本文另跑整尾来补造它。

无论选择哪种初猜，原高度真正求得之后仍须计算自己有限表示的角投影/XYZ metric、
完整前缀/接缝/无限尾预算和全部几何；R108 不支付这些完成条件。
原 h 的真实包一到，仍优先执行既备的尾部自身误差诊断。
