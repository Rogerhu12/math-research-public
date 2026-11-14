# 固定 flat17 径向 Robin 线的实际有限模诊断

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已真实执行的浮点探索，非严格谱间隙证书。** 目的仅是检查 M14 新增高
support 系数附近的频率，是否同时出现同一径向背景、旧线性尾端口下的边界线
近重合。没有读取当前候选曲线、CP 或 tail 数组，没有新 tail 请求，没有启动
非线性 PDE，未触碰 root/独立者的活动求解会话，也没有改变 M15 的已选参数。

## 1. 真实对象和输入身份

几何背景仍为当前固定 flat17：五个 exact-binary 参数
$v_u=.17,v_d=.18,\varepsilon=.4,\eta=.05,
\delta=.07254443456654512$，一个 outward 周期，接 R21 固定的精确桥。
脚本用这些原二进浮点作为参数近似值，按原分段多项式计算周期的 $a,a_s,a_{ss}$。

桥的严格存在已由 R21 支付；本次仅用 Gauss–Legendre 积分和 brentq 浮点计算
该同一根的近似值。定义保持
$$
a_c=.6,\quad w=\frac12,\quad p=\frac\pi2-\arctan w,
\quad p_s=\frac{-7w/a_c}{(1+w^2)^{3/2}},\quad d=-Lp_s,
$$
$$
\varphi(t)=(3p+d)t^2-(2p+d)t^3,
\quad L\int_0^1\sin\varphi(t)\,dt=1-a_c.
\tag{1}
$$
这次浮点求根不是新的 exact-bridge 认证，不代替新候选的 metric-transfer。

右边界只取既有冻结线性 port：

`/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json`

该文件 5581 B，SHA256
`500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702`。
实际检查 `modes` 正好为 $3,6,\ldots,288$，共有96个 `linearSlope`；指定
参数的 cut、wCut 正好为原 binary .6、.5。旧 ready 输出中的 raw
`backgroundSlope` 与 .5 相差约 $1.7764\times10^{-15}$；本次曲面背景使用
(1) 的目标值，$D_n$ 仍是旧文件中的冻结数值。因此本次没有认证这点微小的
calibration 转移，也没有将旧 $D_n$ 宣称为当前非径向 $DT(H)$。

程序仅在终端内部读取所需 port；不输出整个数据文件或数组。

## 2. 比较的真实齐次边界线

R77 的精确位置/第二形式变换，对物理 Fourier 模 $n\ge2$ 给
$$
x=i n(n^2-1)(h+c f/v),\qquad
y=-(n^2-1)f/a,
\quad c=a_s,\ v=\sqrt{1-c^2}.
\tag{2}
$$
对实的径向模系数 $f,h$，写 $x=iX,y=Y$，则 $X,Y$ 都实。
R75 的真实 Sturm 方程等价于
$$
X_r=-nVY,\qquad Y_r=nX,
\quad \frac{dr}{ds}=H=\frac v{a^2},\quad
HV=\frac{a a_{ss}}{v^3}.
\tag{3}
$$
不通过指数放大的基本矩阵直接相减，而写
$X=R\sin\theta,Y=R\cos\theta$。由于非零齐次初值从不变成零向量，
此极坐标可沿区间连续提升；实际方程是
$$
\boxed{\quad
\theta_s=-n\left(\frac{a a_{ss}}{v^3}\cos^2\theta+
\frac v{a^2}\sin^2\theta\right),
\qquad
(\log R)_s=n\left(\frac v{a^2}-\frac{a a_{ss}}{v^3}\right)
\sin\theta\cos\theta.
\quad}
\tag{4}
$$
这由 $\theta_s=(YX_s-XY_s)/(X^2+Y^2)$ 和
$(\log R)_s=(XX_s+YY_s)/(X^2+Y^2)$ 直接推出。

左核心的径向线性条件是 $x(0)=0$。其非零线可取 $(X,Y)=(0,1)$，故
从周期起点以 $\theta_L=0$ 向前积分到周期/桥公共端点。

右 cut 的旧同模 slope $D_n$，按 R77 和 $\sigma=-1$ 给
$$
(X,Y)_{\rm cut}
=\left(n(a_cD_n-1),\ \frac w{a_c}(a_cD_n-n^2)\right)h.
\tag{5}
$$
其两分量不可能同时为零，因为 $n^2\ne1$。从其 atan2 方向向后积分整个
真实桥，到同一公共端点。两边在此 $a=1,c=0$，没有隐藏的变量或通量基转换。

本次记录的数为
$$
\omega_n=\left|\sin(\theta_L-\theta_R)\right|.
\tag{6}
$$
它是两个接口单位方向的 Wronskian 绝对值。对本次 **径向齐次背景和这份
冻结实 $D_n$**，$\omega_n=0$ 等价于存在非零解同时满足左 $x=0$ 和右 Robin
线。非零 $\omega_n$ 不等于整个 BVP 的有效逆范数：沿程放大、源列、其它
有限标量行、真正非径向模间耦合与完整无限尾均还在问题中。

## 3. 实际扫描与两档收敛观察

冻结程序：

`scripts/78718-geometry-radial-robin-scan-v1.py`

SHA256 `b3baa2244e6547f9f72b98e61d51f4fc3a51bbc2f191f65324e9b145f47eb863`。

实际执行命令为该脚本的 `--port` 取第1节文件、`--modes 21`，
`--report notes/2026-11-10-78718-geometry-radial-robin-scan-v1.json`。
作者真实调用 `6f6e37 / session91902`，由 `118d6a` 观察到**自然 exit0**。
约5.007秒；不是根据报告文件存在推断进程结束。

21个物理模为 $n=3,6,\ldots,63$，均用两档真正积分：

| 项目 | 第一档 | 第二档 |
|---|---:|---:|
| 桥积分 Gauss–Legendre 点数 | 32 | 64 |
| DOP853 rtol | $2\cdot10^{-10}$ | $2\cdot10^{-12}$ |
| DOP853 atol | $2\cdot10^{-12}$ | $2\cdot10^{-14}$ |
| 每个多项式区间的最大步长 | 区间长/30 | 区间长/60 |

周期按原全部分段端点切开；桥另在 $\varphi'$ 唯一内部零点切开。
报告保存每模两套方向差、(6)、两边 log 放大、实际 RHS 调用数及各输入身份。
两档的 signed 归一化 Wronskian 最大差约 $6.708\times10^{-10}$。
这是实际浮点重复计算的稳定性观察，不是严格误差包围。

第二档与本轮问题直接相关的诊断数为：

| 物理模 $n$ | 接口归一化线 Wronskian 绝对值 |
|---:|---:|
| 3 | $0.002677251824726448$ |
| 39 | $0.9995157537435089$ |
| 42 | $0.8413447895450545$ |
| 45 | $0.466895463098438$ |

在本次21模中最小值出现在 $n=3$。这里没有给它判作真正零模，也没有借此
改动固定 delta 或任何候选参数。

报告 18339 B，SHA256
`7ef8dafb7ae5ff029919fdf25b37c9964456ad084da0e86c7d0086ef5d4fef5d`。

## 4. 原剖面源与另一变量下的实际交叉核

另冻结
`scripts/78718-geometry-radial-robin-position-check-v1.py`，SHA256
`2e87aa7d0f5d1bae4cf05aec5c5fbde4288c9eef220f1eef5bb704d4d0aed4ef`。

作者真实调用 `10baf5 / session92557`，由 `bb6707` 观察到**自然 exit0**。
它作两件有限的浮点交叉核，不作为未参与者独审：

1. 将自含的 ramp 函数与原 `950f-prefix-flat-accel-screen.py::ramp` 在1002个
   包含分段端点的固定点比较，三个值 $w,I,w'$ 最大绝对差
   $4.440892098500626\times10^{-16}$。这不是全区间严格区间证明。
2. 对 $n=3,39,42,45$ 直接使用原物理位置方程
   $$
   f_s=-\frac{(n^2-1)c f+n^2v h}{a},\qquad
   h_s=\frac{(n^2-1)c^2f/v+n^2c h}{a},
   \tag{7}
   $$
   以另一组 DOP853 容差 $3\cdot10^{-13}/3\cdot10^{-15}$ 真正积分，
   各段结束按二范数重标以控制放大。在公共界面直接由 (2) 得方向
   $(X,Y)\parallel(nh,-f)$；按此算出的 (6) 与第3节 projective ODE 的
   四模最大差为 $3.931910352861223\times10^{-12}$。

该交叉核读取的只是第1节旧 port、第3节本次探索报告和程序源；没有候选
数组。报告为 `notes/2026-11-10-78718-geometry-radial-robin-position-check-v1.json`，
2437 B，SHA256
`d7621539d66015fcb976305b757a117e76cd56859bf25a82f6316495fd3c7b21`。
报告绑定其自身、原 flat 源、冻结主扫描程序、旧 port 和本次扫描输出的哈希。

## 5. 这次实际观察支持的范围

这次计算在声明的归一化与背景下，没有发现 $n=42$ 边界线近重合的迹象；
其接口正弦约 .84。因此“新增高 support 系数变大，是径向 $n=42$ Robin
线几乎共线造成的”目前没有来自本次计算的支持。

这不否定当前非径向 Jacobian 的高模耦合或近核，也不给当前 M14/M15 的
非线性 BVP 条件数；不证明全整数频率的相位门、真正无限尾 gap、实际
端点反馈可逆或 G5。旧 $D_n$ 是径向旧数值端口，不是新状态的实际
$DT(H)$。所有浮点诊断保持探索身份，原物理参数及数值组已冻结的 M15
计划不受本稿调整。

后续应优先追踪当前 projected-core 初始 metric 缺陷和真实 Galerkin 速度
的沿程累积，以及重新求出的同 $g$ 更高模曲线；仅在固定曲线上扩大速度
空间不能把固定的角向 metric $G$ 变成一个新解。

