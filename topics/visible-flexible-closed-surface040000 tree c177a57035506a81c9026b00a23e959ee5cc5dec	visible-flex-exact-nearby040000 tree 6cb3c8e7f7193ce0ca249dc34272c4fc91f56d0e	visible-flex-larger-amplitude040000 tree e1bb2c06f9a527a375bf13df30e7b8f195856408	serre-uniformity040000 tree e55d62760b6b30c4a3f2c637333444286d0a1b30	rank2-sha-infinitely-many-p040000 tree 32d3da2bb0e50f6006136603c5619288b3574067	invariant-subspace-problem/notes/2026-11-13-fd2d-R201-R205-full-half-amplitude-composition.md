# R201 全半周期位置场与 R205 弯尾的真实幅度列接入

日期：2026-11-13。状态：**完整有限函数、所有参数列与一次真实非线性接受步已实现**。准确闭合与接合的数学基础分别是 [R201](../results/R201-half-period-mean-phase-closure-without-reflection.md)、[R205](../results/R205-complete-bent-annulus-cut-lifting-and-fixed-collar.md) 与 R206。这里记录它们的实际组合，明确准确函数与有限求积的区别；当前数值场远未达到全曲面完成标准。

本组不覆盖任何已冻结的 R201 平尾、R205 参考或 R195/R206 求解源。固定幅度诊断、变量幅度初值、接受态各有独立身份。所有计时来自 functions 纯 V8；本组没有创建操作系统子进程，因而没有补造 Node exit code。

## 1. 完整未知与实际输入

父输入是已发布的 `2026-11-13-fd2d-R201-half-period-actual-01-checkpoint.json`，其 931 个系数全部按位复制。它是 J=30、K=7、完整等价 64 角的非反射强 gap 0.8 有限场。新增最后一列是物理设计振幅 $A$：

$$
z=(z_{\rm old},A)\in\mathbb R^{932},\qquad A\in[0,6/5].
$$

这里 $A$ 是弯曲尾的设计参数，和运动族的旋转相位不同。原 cut-height 列仍为零基索引 450；$A$ 为索引 931。中央、角模、半径和高度各列均保留。旧 931 列在当前真实 $A$ 上重新计算，而非对旧 normal 补一列零。

原 481 维前缀含 theta/psi 的正弦列、径向高度、cut-height、rho；非反射扩展每径向 block 有 theta 常数、theta 余弦与 psi 余弦。没有追加纯 psi 常数规范列。每个物理 $s$ 至多涉及四个三次径向 block；相位与 primitive AD 也仅携带这些活跃角列及 $A$，不在角积分中传播全部 932 个零列。高度/rho/cut-height 在 Cartesian 组装中加入。

新增 A=.25 是**新参考下的基准场**，不是旧平尾场的同值重表达，也不是接受步。真实 Armijo 只比较这个新基准的完整目标与同一表示的试步。

## 2. R205 参考与内领高度

R205 对每个固定 $A$ 定义

$$
\alpha_A(y)=\operatorname{sgn}(y)A\,S_9\!\left(
\frac{|y|-17/50}{23/50}\right),
\quad
X_A'(y)=\cos\alpha_A(y),\quad H_A'(y)=\sin\alpha_A(y),
$$

其中 $S_9$ 在端点外截为 0、1。尾的位置为

$$
F_A(r,u)=\bigl(r\cos u,\ X_A(r\sin u),\
Z_c-H_A(r\sin u)\bigr).
$$

准确尾 metric 为 $dr^2+r^2du^2$，$r\le17/50$ 的区域全平。$Z_c$ 是**内平领高度**。外切口截面的平均高度通常不是 $Z_c$。

冻结参考提供完整 theta/psi 的值、$s$ 一二导、$u$ 一导，以及这八项关于 $A$ 的导数。它使用冻结的 B32 base 半径，故 clip loci 不随任何有限系数、rho 或 $A$ 改变。现 radius 设计函数仍由原 R196/R190 实体决定；不把参考的 base 半径替成未知半径而漏掉参数列。

记参考平均高度校正为 $m(s,A)$。完整位置组装的竖直均值使用

$$
z_0(s)-m(s,A),\quad z_{0,s}-m_s,\quad
z_{0,ss}-m_{ss}.
$$

因而 $A$ 列含 $(-m_A,-m_{sA},-m_{ssA})$。cut-height 列仍在内领给 $(1,0,0)$。这两列没有互相混用。

## 3. 半周期闭合与全部振幅相位导数

令 theta 与 raw psi 是完整函数

$$
\Theta=u+\vartheta,\qquad\psi,
$$

其中 $\vartheta,\psi$ 都是 $\pi$ 周期，可同时含正弦、余弦，theta 还可有径向常数。令

$$
\mathcal Z(s,z)=\int_0^\pi e^{i\psi(s,u,z)}\,du,\qquad
R=|\mathcal Z|>0,\qquad \beta=\arg\mathcal Z .
$$

用代数旋转而非 unwrap 选角定义 $\Phi=\psi-\beta$ 的 sin/cos，并令

$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi).
$$

R201 给 $|T|=1$、水平反半周期、竖直半周期且竖直半周期积分为零。所以完整闭合不依赖四分反射。引入 R205 参考和真实 $A$ 不改变这些代数恒等式，只要 $R>0$。当前 finite 网格的 $R>0$ 只作为实际数值定义域检查，不冒充全域连续下界。

全部参数微分都对完整 $\mathcal Z$ 求导。特别地，

$$
\mathcal Z_A=\int i\psi_A e^{i\psi},\qquad
\mathcal Z_{sA}=\int (i\psi_{sA}-\psi_s\psi_A)e^{i\psi},
$$

$$
\mathcal Z_{ssA}=
\int\left(i\psi_{ssA}-2\psi_s\psi_{sA}
-\psi_{ss}\psi_A-i\psi_s^2\psi_A\right)e^{i\psi}.
$$

所有积分范围都是完整 $[0,\pi]$。因此

$$
\beta_A=\Im\frac{\mathcal Z_A}{\mathcal Z},
$$

$$
\beta_{sA}=\Im\left(
\frac{\mathcal Z_{sA}}{\mathcal Z}
-\frac{\mathcal Z_s\mathcal Z_A}{\mathcal Z^2}\right),
$$

$$
\beta_{ssA}=\Im\left(
\frac{\mathcal Z_{ssA}}{\mathcal Z}
-\frac{\mathcal Z_{ss}\mathcal Z_A+2\mathcal Z_s\mathcal Z_{sA}}{\mathcal Z^2}
+\frac{2\mathcal Z_s^2\mathcal Z_A}{\mathcal Z^3}\right).
$$

再代入 $\Phi_A=\psi_A-\beta_A$ 及其 $s$ 一二导。theta 的 R205 振幅导也保留，不能只对 psi 做变化。程序通过这些式子计算 $T_A,T_{sA},T_{ssA},T_{uA}$。这里只需要已知显式参考的混合 $s,s,A$ 导数；未要求未知曲面额外具有三阶径向光滑性。

$A=0$ 时 R205 参考角/高度校正准确为零，故准确数学场恢复同系数的旧 R201 平尾表示。新增 clip 分割可改变有限求积舍入和求积误差；这里不声称两个有限程序逐位相同。

## 4. 完整半周期 primitive 与 Cartesian 二jet

对水平分量 $h=(x,y)$，

$$
Y_h(u)=\int_0^uT_h(v)\,dv-\frac12\int_0^\pi T_h(v)\,dv.
$$

对竖直分量，

$$
Y_z(u)=\int_0^uT_z(v)\,dv
-\frac1\pi\int_0^\pi(\pi-v)T_z(v)\,dv.
$$

这给完整周期的零均值 primitive。其 $s$ 一二导和每个参数列都对**同一完整积分与加权矩**求导。不能删除均值、冻结相位列或以 DFT 导数替换完整切向量。

令 $a$ 是原 rho 设计半径、$z$ 是含上节平均高度修正的均值，则

$$
X=aY+ze_z,\quad X_u=aT,\quad
X_s=a_sY+aY_s+z_se_z,
$$

$$
X_{ss}=a_{ss}Y+2a_sY_s+aY_{ss}+z_{ss}e_z,\quad
X_{su}=a_sT+aT_s,\quad X_{uu}=aT_u.
$$

因为 $a$ 不依赖 $A$，

$$
X_A=aY_A-m_Ae_z,
$$

$$
(X_s)_A=a_sY_A+a(Y_s)_A-m_{sA}e_z,
$$

$$
(X_{ss})_A=a_{ss}Y_A+2a_s(Y_s)_A+a(Y_{ss})_A-m_{ssA}e_z,
$$

并有 $(X_u)_A=aT_A$、$(X_{su})_A=a_sT_A+a(T_s)_A$、$(X_{uu})_A=a(T_u)_A$。实际程序同时保留原 rho 与高度列；没有在这些列上遗漏 $a,a_s,a_{ss}$ 或 $z,z_s,z_{ss}$ 的变化。

完整曲率使用实际 Gram 与实际 Cartesian 二jet。R203 guide 也使用实际 $X$ 及其全部列，包含两个 held 目标和正负 width 行。这里只有 proper half-turn 化简，没有 quarter reflection 化简。

## 5. clip 分片、cut 接合与求积作用域

每个原 uniform half-angle panel 再按冻结参考给出的 clip 位置分片。接口 `angularSubintervals(s,lo,hi)` 返回递增**端点数组**。相位、primitive 总积分、加权矩和查询点前的部分积分全都使用同样的 composite Gauss-8 分片。

这些角节点与权不依赖有限参数及 $A$，故完整参数列是实际有限求积函数的导数。clip 位置可以依赖物理 $s$；程序对完整函数的真 $s$ jets 求积，不能据此把有限求积软件本身的 $s$ 微分误差视为已付清。

在中央及 cut，所有新增 C² 径向样条的 0–2 jets 为零。R205 完整参考与均值给出准确尾的对应 jets。由 R201 primitive 的线性与全函数端点相等，得到完整 Cartesian 两jet 的准确接合条件及其 $A$ 列。该数学陈述沿用准确 B32/准确角积分语义；有限求积对直接尾公式的比较只是实现证据，不是连续证书。

固定 A=1 的 10 角检查，完整 Cartesian 二jet 最大差为 $1.22125\times10^{-14}$。新实际 A=.25、非反射父态的 5 角 cut 检查，二jet差 $4.96825\times10^{-15}$，振幅二jet差 $1.93179\times10^{-14}$。

## 6. 真 normal、R206 两个 global 与接受步

完整新有限 normal 在同一 A=.25 实际场重新计算。它有 932 列、103554 行；$A$ 梯度为 .11825037130657602，$A$ 对角为 .5462371563511391，$A$ 与旧列的 cross 向量 L2 范数为 6.685609160163872。显然不是旧 normal 的补零。

每个径向局部 block 有 31 列，J=30；原 cut-height 是 global border，A 是追加的第二 global。R206 对这份完整 scaled normal 求原阻尼问题：不删除任意交叉项，不更改列尺度，不增加隐蔽 shift。实际 off-band 非零数为 0；global Schur 为 .11599706374093888。实际原完整方程相对残差为 $6.98124\times10^{-16}$。

functions cell `g4:74` 在 120.294 秒完成，其中完整 normal 93.346 秒。lambda=1/900，首个 alpha=1 真非线性试步通过原 Armijo：

| 项目 | 新 A=.25 基准 | 真接受态 |
|---|---:|---:|
| 完整有限目标平方 | .05326148205290277 | .04230963749874404 |
| 振幅 A | .25 | .08755616431785693 |
| sampled metric maximum | .41234878110154516 | .37290604341358496 |
| sampled curvature maximum | 20.04622029984187 | 28.050337270963958 |
| sampled maximum absolute y | .8993070488670587 | .9177203653933255 |
| sampled minimum held distance | .5575320869989508 | .5787158555270133 |

真实实际/预测下降比为 .31302174295025814；接受态内领高度为 .5472930483797682。曲率最大值没有随综合目标单调下降，完整报告保留这个事实。该接受态尚不满足强目标，不能用平均目标下降替代全域上界。

固定 A=1 的较早诊断是另一明确新基准，完整有限目标约1.8635、sampled曲率约204.11；它从未被当作接受态。其父参数、参考身份及完整值另存于本组报告。

## 7. 实现小核与可重做入口

在真实非反射父参数、A=.25上，混合非零方向同时含新增 theta cos、psi cos、theta 常数、height、rho、cut-height 与 A。8 个物理点的完整 Cartesian 二jet JVP relative L2 为 $1.32549\times10^{-11}$，曲率 hinge JVP 为 $1.33371\times10^{-9}$。单独 A 列范数为10.353724051921544，单列二jet JVP 为 $7.68136\times10^{-10}$。中心差分步为2e-6；这些是有限实现检查。

可重做入口：

~~~sh
node scripts/fd2d-run-R201-R205-variable-amplitude.cjs \
  --input notes/2026-11-13-fd2d-R201-half-period-actual-01-checkpoint.json \
  --candidate notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
  --amplitude .25 \
  --out-prefix notes/replay-R201-R205-amplitude \
  --steps 1
~~~

该 Node CLI 是同已执行 factories/LM 的保存重放入口；本轮仅语法解析，实际执行来自上述 functions V8，不能冒为 Node 已跑。新 checkpoint 可直接续读，它明确保存幅度列、完整系数、径向 knots、中央实际轴、所有 source SHA、目标权重、inner-cuff 高度语义和表示定义。

全 A∈[0,6/5] 的尾/固定帽几何预算另见 `2026-11-13-fd2d-R205-continuous-amplitude-cap-inputs.md`。这不支付当前前缀的 metric、全 core 几何、非局部 reach、准确 B32 与有限标量求值差、完整角求积余项或最终全闭运动的误差预算。R193/R194/R197 的后验入口仍可对未来足够好的实际场分别消费。
