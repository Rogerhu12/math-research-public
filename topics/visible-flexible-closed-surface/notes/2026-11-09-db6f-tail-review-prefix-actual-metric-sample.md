# 保存前缀多项式的实际一阶度量：独立静态审查

审查人 `/root/tail_theory`，2026-11-09。**全文公式与实现静态审查 PASS。** 被审脚本为 `scripts/db6f-audit-prefix-actual-metric-sample.py`，SHA256 `3b5435d2caef6655421acead3b6bbaa90d482890dc98d1842a34c04aa07c4aa4`。本审查没有重复完整采样运行。

作者独立采样输出 `notes/2026-11-09-db6f-audit-m15-affine-actual-metric-sample.json`，SHA256 `aa9845c1d849d754d08333beec1b8752c5f225725184d7978cf6cea62953e81c`，绑定辅助 M15 affine CP。其状态是 `UNSOLVED relative to the actual nonlinear DN`，`actual_nonlinear_tail=False`。本报告不将该辅助 CP 视作真实完整联解。

## 1. 保存多项式与旋转基

每个保存区间的六行系数按降幂排列，故 `evaluate_saved_pp` 的 value Horner 给五次多项式，derivative 分支依次乘 $5,4,3,2,1$ 并省略常数行，确为同一保存多项式的实际物理 $s$ 导数。区间选择在内部节点取右迹，末节点取最后区间右端。它没有用 BVP 右端替换非均值导数。

在随 $\psi$ 转动的水平正交基 $(e_r,e_\psi)$ 中，写

$$
u=a\cos\gamma+q\left(R_0+\sum_jR_j\cos m_j\psi\right),\quad
v=a\sin\gamma+q\sum_jT_j\sin m_j\psi,
$$

$$
z=h+q\sum_jZ_j\cos m_j\psi,
\qquad m_j=3j.
$$

旋转基导数给任意水平分量的运算

$$
\partial_\psi(u e_r+v e_\psi)
 =(u_\psi-v)e_r+(v_\psi+u)e_\psi.
$$

设 $\rho=1+\gamma_\psi$、$\rho_\psi=\gamma_{\psi\psi}$，则背景的第一、二阶角导数分量为

$$
(-a\rho\sin\gamma,\ a\rho\cos\gamma),
$$

$$
\bigl(-a\rho^2\cos\gamma-a\rho_\psi\sin\gamma,
      -a\rho^2\sin\gamma+a\rho_\psi\cos\gamma\bigr).
$$

单个非均值水平模的第一阶分量为

$$
q\bigl(-(mR+T)\sin m\psi,\ (R+mT)\cos m\psi\bigr),
$$

第二阶分量为

$$
q\bigl(-((m^2+1)R+2mT)\cos m\psi,
       -(2mR+(m^2+1)T)\sin m\psi\bigr).
$$

均值径向模分别贡献 $(0,qR_0)$ 和 $(-qR_0,0)$。竖直模贡献 $-qmZ\sin m\psi$ 与 $-qm^2Z\cos m\psi$。这些逐项等于 `fields` 中 `d`、`dd` 的定义，包括容易遗漏的 $T$、$R$ 交叉项及径向均值项。

## 2. 物理角坐标与实际径向导数

冻结图表为

$$
\theta=\Theta(s,\psi)=\psi+\gamma(s,\psi),\quad
\gamma=-e(s)\sin(3\psi)/3,
$$

$$
\rho=1-e\cos(3\psi),\qquad
\rho_\psi=3e\sin(3\psi),\qquad
\gamma_s=-e'\sin(3\psi)/3.
$$

审查了 spline 的物理长度缩放、末端 cutoff 的导数以及使用固定 `warp_reference_q` 的幅度。这与冻结 source chart 相同，未把嵌入未知量改写为物理度量参数。

在 $\rho>0$ 下，隐式链式法则给

$$
\left.\partial_s\psi\right|_\theta=-\gamma_s/\rho,
\qquad \partial_\theta\psi=1/\rho.
$$

记 $X_s|_\psi=U$、$X_\psi=d$ 和 $v_0=\gamma_s/\rho$，则真正物理坐标下的两个导数是

$$
F_s=U-v_0d,\qquad F_\theta=d/\rho.
$$

代码的 `Xu` 对背景及保存扰动系数取实际 $s$ 导数，再按上式组成 `Fs`、`Ft`，符号和因子均正确。它没有把 `Fs` 直接定义成源 Frenet 速度。

## 3. 平均高度的定义

曲线 Frenet 数据取实际 $d,dd$：单位切向 $T=d/|d|$，法向由 $dd$ 的正交投影归一化，$B=T\times N$，$\kappa=|dd-(dd\cdot T)T|/|d|^2$。正支路速度为

$$
V=\alpha N+\sqrt{1-\alpha^2}\,B,
\qquad \alpha=-a'/(a\kappa),\qquad W=V+v_0d.
$$

保存 Fourier 展开的竖直非均值项对均匀 $\psi$ 平均为零，因此按照该数值源图的平均高度定义，$h_s=\langle W_z\rangle_\psi$。这里平均变量是 $\psi$，不应无故加 $\rho$ 权重。`fields` 正确地只把这个均值加入 `Xu` 的竖直分量，所有非均值 $Z'_j$ 仍来自保存多项式。

实际脚本用有限均匀角求积计算这个平均，未给连续求积余项。因此它的第一度量是明确的数值采样诊断。平均高度绝对积分没有执行，也不是计算一阶度量所必需。

## 4. 度量统计和输入范围

相对于 $g=ds^2+a^2d\theta^2$，归一化误差矩阵三项为

$$
E=|F_s|^2-1,\quad F=F_s\cdot F_\theta/a,\quad
G=|F_\theta|^2/a^2-1.
$$

代码实现与此一致。实对称二阶矩阵的谱范数

$$
\frac{|E+G|+\sqrt{(E-G)^2+4F^2}}2
$$

也正确。另一个 `metric_fft_l1` 字段是每个误差分量的离散 FFT 系数绝对值和，再取分量和采样位置最大；它与真实采样谱范数字段分开保存。有限 FFT 的这个统计量不自动成为连续函数上界。

实际 source loader 仅用于载入完整保存系数及取得同一冻结 `profile`。被审 `fields` 没有调用源 `audit`、`frame`、`values`，也没有取源 RHS 替代任何非均值导数。端口 hash、物理参数/cut、chart、warp reference 及 profile 实现均独立绑定；这仍是原浮点桥/profile，不是精确桥根转移后的公共两jet闭图。

作者输出在 $5399\times1024$ 网格上的分量 FFT 统计量为 $1.302458505758324\cdot10^{-9}$，采样谱范数为 $1.3024585035167381\cdot10^{-9}$；前者与原保存审计差约 $-5.824\cdot10^{-15}$。本静态审查核对其字段、输入 hash 与数学含义，不宣称独立重跑了这些数值。

## 5. 结论的边界

该工具适合独立检查保存前缀插值图的 sampled actual first metric，并区分实际多项式导数与源方程右端。它不提供连续区间证书，不构造共享两jet完整 XYZ 图，不支付平均高度求积误差、真实尾匹配、全局嵌入或闭曲面完成门。辅助 affine CP 的小采样误差也不能代替真正耦合求解成功。
