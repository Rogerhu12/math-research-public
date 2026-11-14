# M15 global-Z 初猜的沿程度量误差来自何处

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**严格部分：** 同一材料角图中的竖直 Hermite 修正给出的完整度量差公式。
**实际数据部分：** 原有 UNSOLVED M15 warm 的42点有限浮点分解。
没有新 BVP、tail、流积分、优化或候选；不将比较函数当作已经求解的曲面。

R84 已证明这一 warm 的完整入口圆周角向误差低于 $2\cdot10^{-9}$。
numerical 的新42点诊断却在内区得到约 $1.154\cdot10^{-6}$。两者没有
矛盾：原初猜为匹配一份旧真实尾高度，在整条经线上增加了竖直 quintic
Hermite 修正。它在入口有零两jet，内区则会直接改变角向长度。

## 1. 真实构造与本次比较的对象

仍使用
`notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`，SHA256
`cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`。
状态为 `UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS`，不是联解成功输出。

原 `scripts/db6f-prefix-prepare-matched-cut-warm.py::hermite_coefficients`
只改15个竖直模，完整 R/T 系数、度量、chart、自由参数不动。设 $L$ 为
保存的物理终点，则其未舍入的数学修正为
$$
\Delta F=\beta(s)h(\psi)e_z,\qquad
\beta(s)=10(s/L)^3-15(s/L)^4+6(s/L)^5,
\quad h(\psi)=q\sum_{j=1}^{15}\delta_j\cos3j\psi.
\tag{1}
$$
每个 $\delta_j$ 的准确有理值保存在相应 `-preparation.json` 的
`exact_delta_Z`。原过程将“旧系数加准确局部化后的(1)”逐系数舍入到
binary64；它没有重新求 BVP。

本地没有读取原 affine CP。为避免把舍入后的两个对象默认为相同，本次
比较函数明确**定义**为
$$
F_*:=F_{\rm warm}-\beta h e_z.
\tag{2}
$$
这是对保存 warm 的数学减法，不是写入的新初猜，也不声称与未读取的
affine 源逐字相同。旧 preparation 中逐系数舍入误差的准确上界另保留；
其显示量级为 $5.2215249770\cdot10^{-12}$。若采用此上界 $r$，在一个
局部坐标 $t=s-s_i\ge0$ 的 PP 区间内，(2)与旧 affine 的每个 Z 状态值
之差满足
$$
|\Delta Y_{Z,j}|\le r\sum_{k=0}^{5}t^k,
\qquad
|\partial_\psi\Delta F_z|
\le |q|\frac{3M(M+1)}2r\sum_{k=0}^{5}t^k.
\tag{3}
$$
这由每个局部幂系数误差的三角不等式得到；后一个对全部15模求和。
本次不重新核验缺失旧 affine 的每个系数。以下几何差公式则对(2)准确
成立，不依赖它是否与旧 affine 相等。

## 2. 同一 warp 下完整 E/F/G 差公式

沿用 R82 的 $u=\Theta(s,\psi)$、$\rho=\Theta_\psi$、
$b=\Theta_s/\rho$，以及 $D_s=\partial_s-b\partial_\psi$、
$D_u=\rho^{-1}\partial_\psi$。比较的两图共享这些物理坐标与同一 $a(s)$。
令
$$
\zeta=D_u(\beta h)=\frac{\beta h_\psi}{\rho},\qquad
\chi=D_s(\beta h)=\beta'h-b\beta h_\psi.
\tag{4}
$$
特别不能在一般角位置把 $\chi$ 简化为 $\beta'h$。
记 $v_*=D_sF_*$、$T_*=D_uF_*$，其竖直分量分别为 $v_{*,z}$、$T_{*,z}$。
由(2)直接得到
$$
D_sF_{\rm warm}=v_*+\chi e_z,\qquad
D_uF_{\rm warm}=T_*+\zeta e_z.
$$
因而三个相对 metric 分量的准确变化为
$$
\begin{aligned}
\Delta E&=2\chi v_{*,z}+\chi^2,\\
\Delta(F/a)&=\frac{\chi T_{*,z}+\zeta v_{*,z}+\chi\zeta}{a},\\
\Delta\Gamma&=\Delta(G/a^2)
=\frac{2\zeta T_{*,z}+\zeta^2}{a^2}.
\end{aligned}
\tag{5}
$$
证明就是展开这两个向量的范数和内积，不使用等距假设。对原分段 PP，
公式逐 span 适用，符合 R82 的节点范围说明。

对 $G$，也可用原固定图角导数写成
$$
\Gamma_{\rm warm}-\Gamma_*
=\frac{2\beta h_\psi(F_*)_{z,\psi}+\beta^2h_\psi^2}{a^2\rho^2}.
\tag{6}
$$
本次把右端线性项和平方项分别计算，不从小高度本身猜测 metric 变化。

在入口，$\beta(0)=\beta'(0)=\beta''(0)=0$，故完整两jet不变；这解释
为何 R84 的入口上界可以同时成立。另一方面，所有 $s$ 上的两条材料轴
$\psi=0,\pi/3$ 都有 $h_\psi=0$。所以这项 global-Z 修正对两轴的
$\Gamma$ **准确为零**，即使轴外的角向误差已经很大。
两轴上的 $E$ 未必不变，因为 $\chi=\beta'h$ 一般不为零。

## 3. 原42点结果与本次实际分解

复用 numerical 已做的42个物理位置，来源为
`notes/2026-11-10-78718-numerical-m15-warm-next-mode-diagnostic.json`。
本次不重复其各个高模 RHS 比较，只重建同一 warm 的 $F_\psi$，计算
(2)、(6)的新量。角采样数为4096；所有 FFT 数仍是有限诊断，不是本稿
的连续区间包围。

真实 **f0bea3 自然 exit0**，约0.593秒，给出：

- 原 warm 在这42点的最大 $G$-FFT $\ell^1$：
  $1.1540536397368633\cdot10^{-6}$。
- 去除已记录 Hermite 增量后的(2)在同42点最大值：
  $1.302470791742017\cdot10^{-9}$。
- 高度增量 $h$ 的 Fourier $\ell^1$ 约为
  $1.2985622216825283\cdot10^{-5}$；$h_\psi$ 的相应范数约为
  $3.98077762820935\cdot10^{-5}$。

原 worst $s=1.4531514246070452$ 处，$\beta\simeq0.8608239293$，
具体分解为

| 量 | 该圆周的采样 Fourier $\ell^1$ |
| --- | ---: |
| 保存 warm 的 $\Gamma$ | $1.1540536397\cdot10^{-6}$ |
| 比较函数 $F_*$ 的 $\Gamma$ | $8.5220066785\cdot10^{-11}$ |
| (6)线性项 | $1.1551892069\cdot10^{-6}$ |
| (6)平方项 | $1.2205538097\cdot10^{-9}$ |
| (6)两项先相加再取范数 | $1.1539686531\cdot10^{-6}$ |

在该圆周的一个最大绝对值采样角 $\psi\simeq0.50007773685$，
保存 warm 的 $\Gamma\simeq-1.07895346990\cdot10^{-6}$。
线性贡献约 $-1.08002118098\cdot10^{-6}$，平方贡献约
$+1.09044350118\cdot10^{-9}$，而 $F_*$ 自身约
$-2.27324825630\cdot10^{-11}$。
因此这组数据中的主要误差是高度增量与已有竖直角导数的线性交叉项，
不是高度增量平方。

向量重建与(6)的最大浮点相差为 $3.60\cdot10^{-16}$。这一小数只说明
本次重算的一致性，不是把所有浮点图变成准确连续证书。
程序为 `scripts/78718-geometry-warm-hermite-g-decomposition-v1.py`，7350 B，SHA256
`c71d1ad76d0676ce2d6cd8e0a47e32c3d877f8a8d9189052afc4601170c016ae`。
报告 `notes/2026-11-10-78718-geometry-warm-hermite-g-decomposition-v1.json`，32590 B，SHA256
`4131c0dc01dae72016086f43ba08f9108a9f755936fae59346d8457b60959850`。

## 4. 与 R82 和当前真 BVP 的关系

对任何保存状态，raw Frenet 方向满足 $|V|=1$、$V\cdot T=0$。
因此，把新计算出的 projected RHS 临时当作径向速度时，可能已经有很小
的 $E,F$ 误差；但保存 warm 的真实系数导数不因此等于该 RHS。
R82 的完整缺口 $e=F_s-W$ 中仍有插值导数减 RHS 项。

这一区别在共享的42点报告中很明显，直接读取其已有标量（fc4e40），
原 M15 速度投影的最大采样 $E,F/a$ 分别约为
$1.429\cdot10^{-10},5.177\cdot10^{-11}$；保存 warm 自身导数却给
$2.959\cdot10^{-5},3.556\cdot10^{-5}$。保存导数与原 RHS 的速度差
约 $2.034\cdot10^{-4}$。在最大 $G$ 的该点，保存的 $E,F/a$ 仍分别
约为 $2.257\cdot10^{-5},3.491\cdot10^{-5}$。

所以小的 projected-source $E,F$ 不是“这一 warm 已近似等距”的证明。
真实 BVP 需要调整整条曲线，使保存导数实际跟随原方向场及真实尾边界，
从而按 R82 控制沿程相对角向误差。因为 $V$ 和投影 RHS 都非线性依赖
当前几何，不能预先说最后的解恰好就是(2)，或只需机械删去 Hermite 增量。
它可能同时调整 R/T、Z 和自由 support 参数。

固定同一保存曲线只提高速度投影阶数并不改变 $G$；这解释了 numerical
原 M15/16/18/22 比较中 $G$ 完全不动。当前主要步骤仍是已经启动的
真正 M15 联解，而不是根据这份已知被改过的初猜之大 $G$ 立即再升频。
最终新输出需使用它自己的 metric、共同图与 reach，不能借本次入口
或比较函数的数值。

