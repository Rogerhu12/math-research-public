# 固定 balanced 法向计算角的真实中央曲线、轴差及参数两jet

2026-11-12，fd2d / metric_closure。

**可信度分开：** §1–6 是准确中央曲线及导数的完整证明；§7 的连续曲率区间是带明确余项的计算证明；A/B/gap 在本文件所绑 check 中仍是浮点积分求值。这里没有完成整个前缀 BVP、真实非线性尾或强目标闭曲面。旧 accepted6 的大 L1 没有被当作淘汰依据。

## 1. 固定数据与两个不同基点

固定 R118 的准确函数 $\rho=\rho_*(\phi)$ 及原周长常数 $a_0$。它们满足

$$
\frac{57}{250}<\rho<\frac{317}{100},\qquad
\int_0^{\pi/2}\rho=a_0\frac\pi2,
$$

以及准确的 seed 轴截距 $A_*=281/200=1.405$、$B_*=99/200=.495$。所有参数共用

$$
u=U(\phi)=\frac1{a_0}\int_0^\phi\rho(t)\,dt,
\qquad U'=\rho/a_0>0.
\tag{1}
$$

这是**固定 seed 的法向角**到物理材料角的转换。改变中央曲率参数不改变 $U$，也不改变物理度量。

准确常数的输入是

- `2026-11-12-fd2d-balanced-moments-taylor-01.json`；
- `2026-11-12-fd2d-balanced-weighted-means-01.json`。

第一包虽然未达到额外要求的 $10^{-24}$ 宽度偏好，带显式 Taylor 余项的区间仍有效。第二包已经正常完成，95 个模式都有严格 dyadic 端点。相应证明在 `2026-11-12-fd2d-balanced-exact-moment-intervals.md`，这里不重算其矩和 DFT。

定义

$$
\mu_j=\frac1{2\pi a_0}\int_0^{2\pi}\rho(\phi)\cos(2j\phi)\,d\phi,
\quad \psi_j=\cos(2j\phi)-\mu_j,
\quad Q_j(\phi)=\int_0^\phi\rho(t)\psi_j(t)\,dt.
\tag{2}
$$

这些均值是准确积分，非某个浮点采样均值。有限的 dyadic 输入区间只用于包围它们。

两个基点必须显式区别：

| `base_kind` | 基曲率 $n_0$ | 基转角 $\vartheta_0$ | 基曲线 |
|---|---|---|---|
| `balanced_seed` | $1/\rho(\phi)$ | $\phi$ | R118 的 $\gamma_*$ |
| `circle` | $1/a_0$ | $U(\phi)$ | $a_0(\cos U,\sin U,0)$ |

旧 log accepted6 的 $d$ 只能按第一行解释。新 continuation 可按第二行从 $c=0$ 开始；它准确包含半径 $a_0$ 的圆，不需要用有限 Fourier 系数抵消 seed 的无限谱。

## 2. 准确闭曲线与 D2 对称

对有限真实参数 $d=(d_1,\ldots,d_J)$ 定义

$$
P_d=\sum_j d_j\psi_j,\qquad
\delta_d=\sum_jd_jQ_j,\qquad n_d=n_0+P_d,
\qquad \vartheta_d=\vartheta_0+\delta_d.
\tag{3}
$$

令

$$
T_0=(-\sin\vartheta_0,\cos\vartheta_0,0),\quad
N_0=(-\cos\vartheta_0,-\sin\vartheta_0,0),
$$

$$
T_d=\cos\delta_d\,T_0+\sin\delta_d\,N_0,\qquad
N_d=\cos\delta_d\,N_0-\sin\delta_d\,T_0.
\tag{4}
$$

实际中央位置定义为

$$
\gamma_d(\phi)=\gamma_0(\phi)
+\int_0^\phi\rho(t)(T_d(t)-T_0(t))\,dt
-\frac12\int_0^\pi\rho(t)(T_d(t)-T_0(t))\,dt.
\tag{5}
$$

最后一项固定共同的半周中心。实现中使用

$$
T_d-T_0=-2\sin^2(\delta_d/2)T_0+\sin\delta_dN_0
\tag{6}
$$

避免小参数时直接相减两个接近的单位向量。

证明如下。$\rho\psi_j$ 是偶函数，$\pi$ 周期，且关于 $\pi/2$ 对称。由 (2) 其整周积分为零，所以四分之一周积分也准确为零。因此

$$
Q_j(0)=Q_j(\pi/2)=0,\quad Q_j(\phi+\pi)=Q_j(\phi),
\quad Q_j(-\phi)=-Q_j(\phi),\quad Q_j(\pi-\phi)=-Q_j(\phi).
\tag{7}
$$

两种基转角均满足 $\vartheta_0(\phi+\pi)=\vartheta_0(\phi)+\pi$、$\vartheta_0(-\phi)=-\vartheta_0(\phi)$。故 $\rho T_d$ 半周反号，整周积分准确为零。式 (5) 的两jet 及任意高阶导数在接缝一致，且

$$
\gamma_d(\phi+\pi)=-\gamma_d(\phi),\qquad
\gamma_d(-\phi)=\operatorname{diag}(1,-1,1)\gamma_d(\phi).
$$

又 $\delta'_d=\rho P_d$，两种基点都满足 $\vartheta_0'=\rho n_0$，所以

$$
\gamma'_d=\rho T_d,\qquad \vartheta'_d=\rho n_d.
\tag{8}
$$

由于 $\rho>0$，曲线对所有有限 $d$ 都是准确闭合的正则解析浸入。它是否嵌入另由真实曲率/几何判断，不由保守 L1 窗的失败决定。

如果 $n_d>0$，则 $\vartheta_d$ 一周严格增加 $2\pi$，曲线严格凸且嵌入。这里也可直接验证支持性质：在任一基点的外法向 $\nu_0=-N_d(\phi_0)$ 上，弦投影是 $-\int\rho\sin(\vartheta-\vartheta_0)$。转角差在 $[0,\pi]$ 时严格为负；在 $[\pi,2\pi]$ 时用准确闭合把它改写为剩余弧上同号积分，仍严格为负。故每个点是该法向的唯一支持点，没有不同参数点相交。

## 3. 物理材料角、计算角与中央两jet

式 (1)、(8) 给出

$$
X_u=a_0T_d,\quad X_{uu}=a_0^2n_dN_d,
$$

$$
X_\phi=\rho T_d,\quad
X_{\phi\phi}=\rho'T_d+\rho^2n_dN_d,
\quad n_u=\frac{a_0}{\rho}n_\phi.
\tag{9}
$$

用于当前中央平坦段的初始数据为

$$
e_1=e_z,\quad e_2=T_d,\quad N=e_1\times e_2=N_d,
\quad m=l=0,\quad X_s=e_z,\quad X_{ss}=X_{su}=0.
\tag{10}
$$

它有准确中央度量 $ds^2+a_0^2du^2$。将其用于其他 profile 时须满足相应中央 $a'(0)=a''(0)=0$ 条件，不能把 (10) 当作任意目标的自由二jet。

另外保留原 $A=7/5,B=1/2$ 椭圆的共同偏心角 $\theta$，令其速度 $\ell_E$。它只定义同一个材料标记

$$
u_\theta=\ell_E/a_0,\quad u_{\theta\theta}=\ell_E'/a_0,
\quad X_\theta=X_u u_\theta,\quad
X_{\theta\theta}=X_{uu}u_\theta^2+X_u u_{\theta\theta}.
\tag{11}
$$

这不是变化后曲线自己的法向角或偏心角。接口的 `X_u/X_uu` **始终**表示物理材料导数；`X_phi/X_phi_phi` 和 `X_theta/X_theta_theta` 使用不同键。

## 4. 完整参数 JVP

给定方向 $v$，写

$$
Q_v=\sum_jv_jQ_j,\quad n_v=\sum_jv_j\psi_j.
$$

固定 $\phi$、固定 $u$ 或固定共同 $\theta$ 时，材料变换均不依赖 $d$，所以同一个参数微分给

$$
\dot T=N_dQ_v,\quad\dot N=-T_dQ_v,
$$

$$
\dot X=\int_0^\phi\rho N_dQ_v
-\frac12\int_0^\pi\rho N_dQ_v,
$$

$$
\dot X_u=a_0N_dQ_v,\quad
\dot X_{uu}=a_0^2(n_vN_d-n_dT_dQ_v),
$$

$$
\dot X_\phi=\rho N_dQ_v,\quad
\dot X_{\phi\phi}=\rho'N_dQ_v+
\rho^2(n_vN_d-n_dT_dQ_v).
\tag{12}
$$

共同 $\theta$ 的参数两jet由 (11) 对 $d$ 微分得到。中央 $e_1,l,m$ 的 JVP 为零。全部式子是准确有限维解析导数；实现没有用有限差分生成 JVP。

## 5. 真实轴差、梯度与可微性

由 (7) 及对称性，两个轴截距是

$$
A(d)=A_0-\int_0^{\pi/2}\rho(T_d-T_0)_x,
\quad B(d)=B_0+\int_0^{\pi/2}\rho(T_d-T_0)_y.
\tag{13}
$$

它们也等于

$$
A(d)=\int_0^{\pi/2}\rho\sin\vartheta_d,\qquad
B(d)=\int_0^{\pi/2}\rho\cos\vartheta_d.
\tag{14}
$$

无论曲率是否正，(13) 都给两个准确轴截距，且是 $d$ 的解析函数。曲率为正时，§2 证明它们确实是两个轴方向的支持值。其梯度为

$$
A_j=-\int_0^{\pi/2}\rho(N_d)_xQ_j,
\qquad B_j=\int_0^{\pi/2}\rho(N_d)_yQ_j.
\tag{15}
$$

因此可以把 $G(d)=A(d)-B(d)$ 直接作为完整 BVP 的幅度方程，梯度为 $A_j-B_j$。这没有把真实非圆幅度替换为系数范数。

还可给全参数的二阶界。记 $L=a_0\pi/2$，$S(v)=\sum_j|v_j|(1+|\mu_j|)$，则准确零均值给

$$
|Q_v(\phi)|\le S(v)\min\left(\int_0^\phi\rho,
\int_\phi^{\pi/2}\rho\right).
$$

对 (15) 再微分得

$$
A_{vw}=\int_0^{\pi/2}\rho(T_d)_xQ_vQ_w,
\quad B_{vw}=-\int_0^{\pi/2}\rho(T_d)_yQ_vQ_w,
$$

$$
|G_v|\le\frac{\sqrt2 L^2}{4}S(v),\qquad
|G_{vw}|\le\frac{\sqrt2 L^3}{12}S(v)S(w).
\tag{16}
$$

这些界由将积分变量换为准确 seed 弧长、积分 $\min(t,L-t)$ 及其平方得到，故不依赖采样。

第一方向还有严格非退化性。$\psi_1=\cos2\phi-\mu_1$ 在四分之一周严格下降，其加权均值为零，所以 $Q_1>0$ 于内部。在任意严格凸参数处，$0<\vartheta_d<\pi/2$，从而

$$
\partial_{d_1}G=\int_0^{\pi/2}\rho
(\cos\vartheta_d+\sin\vartheta_d)Q_1>0.
\tag{17}
$$

特别是 circle-base 的圆起点，真实 gap 方程沿第一方向可以局部解出。这里只证明幅度约束自身非退化，不据此宣称整个 BVP 有解。

## 6. 可直接调用的接口与数值范围

源：`scripts/fd2d_balanced_curvature_core.py`。

```python
from fd2d_balanced_curvature_core import FixedBalancedGeometry, BalancedCurvatureCore

geometry = FixedBalancedGeometry()
curve = BalancedCurvatureCore(c, base_kind='circle', geometry=geometry)
axes = curve.axis_intercepts_and_jacobian()
# axes['A'], axes['B'], axes['gap']
# axes['A_jacobian'], axes['B_jacobian'], axes['gap_jacobian']

n_data = curve.curvature(phi)
# n, n_phi, parameter_basis, rho_seed

data = curve.evaluate_normal_angle(phi)
material_data = curve.evaluate_material(u)
reference_data = curve.evaluate_reference_angle(theta)
jv = curve.jvp_normal_angle(phi, direction)
material_jv = curve.jvp_material(u, direction)
reference_jv = curve.jvp_reference_angle(theta, direction)
```

`gc_values` 一直使用 `N×14` 列序 `[n,m,X,e1,e2,N]`。每次参数变化可重建轻量 `BalancedCurvatureCore`，共用 `geometry`；固定 Q/轴积分节点会缓存。实际已测完整轴梯度每次约 1.62 ms。

所有 finite Gauss 积分是准确式 (2)、(5)、(12) 的数值求值。实现将原本准确的轴端点、零季度原函数值用于对称延拓；这不是把采样拟合成新定义。各常数用严格区间的 longdouble 代表，报告其代表误差，但这些常数误差没有涵盖整个积分器与三角函数的舍入。点求值 `point_evaluation_is_interval_certified=false` 保留。后续严格消费者必须消费准确积分定义并支付所用误差。

## 7. 实际 accepted6 与圆起点

输入为

`2026-11-12-fd2d-numerical-gc-bvp-log-start-01-accepted6-central-d.json`

（SHA `c536409940559e0ad87182db2e6c7073d5118a026f4474dde28c302cfc4c959e`）。它是真实第六次 accepted 的 47 个参数，L1 约 2.8818986894；原 BVP 未收敛，尚无 nonlinear tail。没有把后来的准确均值冒写为该次旧运行的输入。

在 `balanced_seed` 加准确均值的**明确新中央定义**下，实际计算为

| 量 | 结果及可信度 |
|---|---|
| $A$ | 1.4083426705732187，浮点积分 |
| $B$ | .49841532877753786，浮点积分 |
| $A-B$ | .9099273417956808，浮点积分 |
| 全角中央曲率 | 严格包含于 $[.1455720383644044,6.39291250274204]$ |
| 最小中央曲率半径 | 严格大于 .1564232264356944，故大于 .136 |
| 曲线凸性 | 由上述正曲率和 §2 严格成立 |

曲率计算证明不依赖 Gauss 积分。取四分之一周 2048 格、2049 个准确角度的 60 位区间值，所有 $\rho,\mu,d$ 都按上述准确定义。再用

$$
|\rho'|\le Dk+2|u_2|+4|u_4|,
\quad |n'|\le\frac{Dk+2|u_2|+4|u_4|}{(57/250)^2}
+\sum_j2j|d_j|=:L_n
$$

以及每点到网格距离不超过 $\pi/(4\cdot2048)$，把严格点值区间扩大 $L_n$ 倍该距离。D2 对称覆盖整周，且 (1) 是全局单调角映射，所以同时覆盖全部物理材料角。这是完整覆盖的连续区间，不是把 16384 点样本最值当作全域界。

旧有限均值与准确均值的曲率差准确为常数

$$
n_{\rm exact\ means}-n_{\rm old\ binary\ means}
=\sum_jd_j(\mu_j^{\rm old}-\mu_j)
\in[-1.13519997465148,-1.13319046093841]\,10^{-15}.
$$

这个式子只比较两条明示的中央曲率公式；原有限 solver 还含自己的投影和迭代误差，不能据此替它证明完整旧场。

circle-base 的 $c=0$ 准确有 $A=B=a_0$、gap 为零；数值 $a_0=1.0040828380214688$，首 gap 导数约 .3641181918671076，其严格正号已由 (17) 证明。

记录的有限求值检查：64 到 128 个 Gauss panels（每格24阶）轴差变化在工作精度为零，位置最大变化 $4.34\cdot10^{-19}$；方向有限差分步长由 $10^{-4}$ 减半时，位置、两jet及 gap 导数误差按二阶下降。物理角逆变换误差 $3.47\cdot10^{-18}$，中央 metric 浮点误差 $2.17\cdot10^{-19}$。这些仅说明所用数值求值正常，不替代精确积分误差界。

## 8. 实体、运行与身份

全部路径相对于本课题：

| 实体 | SHA-256 |
|---|---|
| `scripts/fd2d_balanced_curvature_core.py` | `d67571b9b6ae8139626cc445cf12e417d9e549e3e410c0254b73dd122d0b8fb4` |
| `scripts/fd2d-metric-balanced-curvature-core-check.py` | `f99d4817e261d3f534990b8c814421d7be6b98876d5e407976d1ff52f85adf4a` |
| `notes/2026-11-12-fd2d-metric-balanced-curvature-core-check-01.json` | `d46a3ca892e36b34252b3e87bb24bcb06db89c4bb76e6e43811dfab040822c89` |
| `notes/2026-11-12-fd2d-metric-balanced-curvature-core-accepted6-definition.json` | `48c5d1e0bd83e896be992260ef1fe90e5749c99eb8fe20ba594e1ad51f74e499` |
| `notes/2026-11-12-fd2d-metric-balanced-curvature-core-circle-definition.json` | `b3f7b8a4b83f26eed1c302dd67e9e42e7829e6ac059fba8d9b993fd1497afbd7` |

正式 check 的 session 96833 自然 exit0，约17.73秒。早先一次命令在解析时遇未闭括号，exit1；第一次实际完整求值在序列化 `actual_iteration` 时把 dict 当 int，session70952 exit1。其已经写出的准确 definition 没有删除或覆盖；最终 run 逐字核对相同定义后完成报告。两个失败均是本次 check 的代码/元数据错误，未宣称为数学失败或外部 kill。

本交付是强目标完整 BVP 所需的真实 `initial_geometry` 与可微 gap provider。中央严格凸、局部曲率半径和轴幅度不能代替完整活动核的球包、嵌入、reach、尾两jet或全域 metric 后验。
