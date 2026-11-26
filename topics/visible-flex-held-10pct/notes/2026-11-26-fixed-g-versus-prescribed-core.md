# 固定目标度量与额外规定入口曲线：两种不同的精化问题

维护：Astra-held10-06bbeb39-20261126 / fixed_metric。

**状态：下面的度量独立性和离散维数解释已由公式及实际源核实；尚无本条新固定度量 BVP 的收敛结果。** 本条不撤销此前「冻结所有有限核心系数」接口的计算对象，但纠正把那个更强问题的兼容债当成原固定度量问题必有障碍的解读。所有旧数值结果仍按它们原有的来源及范围使用。

## 1. 物理目标度量并不包含核心形状系数

令 $a=a_\delta(s)>0$ 为已经固定的完整前缀轮廓。令 $X(s,\theta)$ 为曲面，$T,N,B$ 是每条 $s$ 常值曲线的单位 Frenet 标架，$\kappa>0$ 是其空间曲率。完整连续方程为

$$
X_s=\alpha N+\beta B,
\qquad \alpha=-\frac{a'}{a\kappa},
\qquad \beta=\sqrt{1-\alpha^2}>0. \tag{1}
$$

设入口 $X(0,\theta)=\Gamma(\theta)$ 为单位速闭曲线，$a(0)=1$。在方程有足够正则的解、Frenet 标架有定义的范围内，(1) 直接给出

$$E=|X_s|^2=1,\qquad F=\langle X_s,X_\theta\rangle=0.$$

写 $G=|X_\theta|^2$。Frenet 公式 $\partial_\theta N=-\kappa\sqrt G\,T+\tau\sqrt G\,B$ 及 $\partial_\theta B=-\tau\sqrt G\,N$ 给出

$$
\partial_sG
=2\langle X_\theta,\partial_\theta X_s\rangle
=-2\alpha\kappa G=2\frac{a'}aG.
$$

因此 $G/a^2$ 对 $s$ 不变；由入口条件 $G(0)=1$ 得

$$\boxed{X^*e=ds^2+a_\delta(s)^2d\theta^2.} \tag{2}$$

这里的目标度量只读 $a_\delta$，不读 $\Gamma$ 的支撑函数系数。核心系数会影响 (1) 能否全局求解及末端条件能否满足；它们不因这种外在影响成为 (2) 的参数。这个计算不证明 BVP 可解，也不绕过前缀、真实尾和接缝的全部误差。

### 实际源对应

恢复清单里的 `fixed_metric_mode3_bvp.py::SupportBVP.flow` 在 `fixed=True` 时无条件返回 `fixed_flow`。`fixed_flow` 由冻结的 `cfg`、`port`、固定表示尺度 `q_gauge` 生成；`profile` 只读轮廓。核心未知由

$$q_{\rm actual}=q_{\rm seed}e^{p_0},\qquad c_j=s_jp_j$$

解码，再交给 `PlanarSupportCore` / `MaterialFlattenedSupportCore`。此处 $q_{\rm gauge}$ 是状态表示的固定除数；$q_{\rm actual}$ 是入口未知曲线的首系数，两者不可混淆。

`950f-prefix-warped-bvp.py::WarpedFlow` 的角图幅度是 `8*warp_q`，不是 `8*q_actual`。当前固定 `warp_q=.06`、完整 chart 和轮廓后，数值材料图 $\theta=\Theta(s,\psi)$ 也不依赖 $c_j$。同一个目标度量在这组坐标中是

$$
\bigl(1+a^2\Theta_s^2\bigr)ds^2
+2a^2\Theta_s\Theta_\psi\,ds\,d\psi
+a^2\Theta_\psi^2d\psi^2. \tag{3}
$$

不能把 $a,\delta$、bridge、尾部 valley/warp 或背景校准设置的变化归入这个结论；它们确实能改变目标度量。

## 2. R53 材料核心仍有固定入口度量

原支撑函数可写成

$$h(\varphi)=1+\sum_{j\ge1}a_j\cos(3j\varphi),\qquad h+h''>0.$$

常数项 $1$ 固定周长 $2\pi$；三重对称排除了平移的一次谐波。按弧长 $\theta$ 参数化的原核心满足 $|\Gamma_\theta|=1$。

R53 的材料圆化不是把任意 Fourier 近似误当单位速曲线。其精确定义先构造相位 $\phi_{h,\lambda}(\theta)$，再定义

$$\Gamma_{h,\lambda}'(\theta)=i e^{i\phi_{h,\lambda}(\theta)}.$$

所以对每个允许的 $h$、固定的 $\lambda,S,b,k$，仍有 $|\Gamma_{h,\lambda}'|=1$。旋转对称决定的原点与反射规范固定刚体自由度。有限 Gauss 积分只是该精确定义的数值评价，其误差仍须单列。

当 $\lambda=1$、`curvature_blend=1` 且目标曲率 $k$ 固定时，保护窗内 $\phi'=k$；准确圆弧的半径和材料窗不随未知 $a_j$ 改变。窗外形状、圆弧中心位置及全局闭合仍由解决定。反之 $\lambda=.002$ 不提供准确圆弧；本条不能把当前低 $\lambda$ 结果升级成固定握持区或 10% 解。

## 3. 一个不依赖离散阶数的固定度量 BVP

允许核心系数随离散变化，必须先明确它们是哪一个完整问题的未知量。以下是有意义的新序列，而不是把已经声明固定的入口曲线悄悄换掉。

一次性固定：完整 $a_\delta$（包括 bridge）、完整真实尾背景及连续深尾定义、对称阶数、$\lambda,S,b,k$、材料图、高度原点、刚体规范、最终相位时间区间。未知为满足统一正性和分支条件的支撑函数 $h$、前缀场 $X$、尾场，以及由相同场唯一确定的均值原函数。

方程是：入口 $X(0)=\Gamma_{h,\lambda}$、完整未投影的 (1)、原真实尾方程、全部共同 Cartesian 两 jet、深端闭合，以及声明的统一规范。不另加可调均值、ODE forcing 或可移动的物理尾背景。选非零分支可使用例如首系数落在一个预先指定、与零隔开的闭区间；该区间只是支线选择条件，不是每层重新优化几何预算的许可。

现在 $h_M=1+\sum_{j=1}^M a_{j,M}\cos(3j\varphi)$ 是同一个未知 $h$ 的近似；$a_{j,M}$ 的变动与场节点变动具有相同身份，都是求近似解。它不是在网格加密时重新选目标度量。若外部另外规定了每个 $a_j$ 或整个入口曲线，那么这些量就必须固定，那是下一节的更强问题。

必须将这一新序列与旧 design-only 序列分开。旧 design-only 中 $p_0$ 改 $\delta$，因此改变 $g$，仍不能称为同一度量收敛。新 `fixed=True` 中 $p_0$ 改入口首系数而不是 $\delta$；是否实现同一完整问题，须看代码路径及完整背景绑定，不能仅看 `fixed` 标签。

## 4. M 条兼容债属于哪一个问题

令 $n=3M+1$、$K$ 为径向节点数。原有限问题有 $n(K-1)$ 条内部 collocation、$n$ 条入口方程和 $M$ 条真实终端条件。未知为 $nK$ 个场值及 $M$ 个核心系数。

如果入口曲线也是未知，入口消元为 $Y_0=I_M(p)$，仍有 $n(K-1)+M$ 个未知；保留原全部方程是平方系统。对固定 $g$ 没有凭空出现 $M$ 条额外条件。

若把已求得的有限向量 $p_*$ 解释成**精确规定的入口曲线**，就删除了 $M$ 个真实未知，才得到旧 `FrozenPhysicalField` 的矩形系统与

$$\eta=r_T-C A^{-1}r_E.$$

这个等式及旧接口完全有效；它检测的是更强的固定入口问题。即使它在有限精度下显示不可消的小量，也不能因此推出原固定度量 BVP 无解。反过来，允许核心系数变化也不保证收敛；它仅恢复了原几何问题允许的未知量。

## 5. 不能省略的同一极限核与全场检验

要让第 3 节成为 README 第 5 条的实质证据，至少须实际给出：

1. 每层相同的完整轮廓、真实尾背景、圆弧/时间数据和规范；物理参数改动另起设计序列。
2. 共同模式系数及新增尾系数的 Cauchy 检查；首系数统一远离零，并验证支线未跳到圆面。
3. 在同一材料坐标上的完整 $\Gamma_M$ 和全曲面 $F_M$ 的位置、一阶、二阶差量下降。可使用带统一曲率半径正下界的充分加权 Fourier 范数；单纯逐项系数趋稳不足以证明 $C^2$ 收敛。
4. 完整未投影 metric 残差、真实 DN/均值/Cartesian 接缝残差随径向、角频率及时间精化下降。投影内 RMS 下降不替代这些量。
5. 当前 $\lambda<1$ 的解即使同 $g$ 收敛，也不自动支付准确圆弧或握持条件。完整最终 $\lambda=1$ 候选必须独立完成全闭合、全时 reach、整像变化和 $\delta_E>0$。

数值 Cauchy 序列本身仍不是严格存在证明；若只取得可复算的收敛证据，必须如实标为数值结论。本条没有新 BVP 终态、没有放宽任何实际接受门，也没有将旧变化 $\delta$ 的序列重命名成同 $g$。

## 源码定位

- 原恢复清单：`scripts/nonlinear_tail/m3_coupled_seed_deliverable/m3_source_recovery_manifest.json`。
- 对应恢复源：`notes/fixed_metric_mode3_bvp.py`、`notes/fixed_metric_mode3_flow.py`、`scripts/950f-prefix-warped-bvp.py`、`scripts/950f-prefix-adaptive-chart-bvp-v2.py`。
- 当前 R53 定义：`scripts/resume_transfer/material_flattened_support_core.py`，特别 `_phase_fields`、`_position_integral`、`evaluate`。
- 旧较强问题接口：`scripts/resume_n4/frozen_physical_field_refinement.py`；本轮明确标成 linear DN 的可执行分支：`scripts/resume_20261126/fixed_m3_linear_field.py`。

本条只对这些实际数学定义作依赖辨析。后续执行采用新返回的真实场，不能将失去的旧 scratch 数组假称为已恢复，也不能搬用旧场的 R60/R62 连续常数。
