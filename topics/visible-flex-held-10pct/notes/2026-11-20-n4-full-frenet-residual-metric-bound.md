# 实际完整 Frenet 速度残差如何控制固定度量误差

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：解析恒等式与充分界；没有新增数值执行。** 本文逐项使用原 [adaptive Flow.frame/geo/audit 源](../../visible-flexible-closed-surface/scripts/950f-prefix-adaptive-chart-bvp-v2.py) 的真实角向长度、曲率、正根与 moving-chart convection。它适用于已经有度量缺陷的实际场，不预先假定该场等距。它为 [固定全部物理参数的场校正](2026-11-20-n4-fixed-physical-field-refinement.md) 指出必须观察的未投影量，不把有限采样界升级为连续证书。

## 1. 与原源码相同的几何量

目标固定度量为
$$
g_0=ds^2+a(s)^2d\theta^2,\qquad a(s)>0,
$$
其中 s 是实际子午弧长，a 是同一个已冻结物理 profile。

先在材料坐标 $(s,\theta)$ 中写实际场为 F。记
$$
d=F_\theta,\quad \ell=|d|>0,\quad T=d/\ell,
$$
$$
w=F_{\theta\theta}-(F_{\theta\theta}\cdot T)T,\quad
N=w/|w|,\quad \kappa=|w|/\ell^2>0,\quad B=T\times N.
$$
这里的 $\ell$ 是 **实际 $|F_\theta|$**，没有把它替换成目标 a。定义与原 frame 相同：
$$
\alpha=-\frac{a_s}{a\kappa},\qquad
\beta=+\sqrt{1-\alpha^2},\qquad
V=\alpha N+\beta B,\qquad
R=F_s-V. \tag{1}
$$
要求原 Frenet 域 $|\alpha|<1$ 成立。正则性可取 F 关于角变量至少 C³、所用混合导数连续、a 至少 C¹；更弱时只要后续 $R_\theta$ 和各链式求导有定义也可用。本文不据此替候选支付正根域或曲率正性。

**关键核对。** 原 frame 在计算参数 $\psi$ 中用
$\mathrm{lam}=|P_\psi|$、
$\kappa=|P_{\psi\psi}-(P_{\psi\psi}\cdot T)T|/\mathrm{lam}^2$。
曲率不依赖正向重参数化，故这与上面的材料坐标定义相同。即使实际 G 已经不等于 $a^2$，公式 (1) 仍用实际曲率。

## 2. 已有角向度量缺陷不会被省掉

记
$$
E=|F_s|^2,\qquad Q=F_s\cdot F_\theta,\qquad G=|F_\theta|^2.
$$
用 Q 表示混合度量系数，以免与映射 F 混淆。因为 V 是单位向量并垂直于 $F_\theta$，逐点有
$$
E-1=2V\cdot R+|R|^2,\qquad Q=R\cdot F_\theta. \tag{2}
$$

由 $F_\theta\cdot V=0$，
$$
F_\theta\cdot V_\theta
=-F_{\theta\theta}\cdot V
=-\alpha\kappa G
=\frac{a_s}{a}G. \tag{3}
$$
式 (3) 的右侧是 $(a_s/a)G$，**不是 $aa_s$**。只有在额外已知 $G=a^2$ 时才会等于后者。本证明始终保留实际 G。

于是
$$
G_s=2F_\theta\cdot(F_s)_\theta
=\frac{2a_s}{a}G+2F_\theta\cdot R_\theta,
$$
从而得到对已有 metric 缺陷也成立的精确身份
$$
\boxed{\partial_s(G/a^2)=
        \frac{2}{a^2}F_\theta\cdot R_\theta.} \tag{4}
$$

式 (4) 的意义是：除去目标 profile 的精确乘法因子后，角向长度缺陷由完整速度残差的角导数驱动。没有出现一个可以擅自丢掉的 $(G-a^2)$ 项；它已经由对 $G/a^2$ 求导精确消去。

## 3. 一个不需先假定小缺陷的充分界

设
$$
u(s,\theta)=|F_\theta|/a>0.
$$
由式 (4)，
$$
u_s=\frac{F_\theta\cdot R_\theta}{a|F_\theta|},
\qquad |u_s|\le\frac{|R_\theta|}{a}. \tag{5}
$$
这里用的是原域保证的实际 $|F_\theta|>0$；没有用 $u\approx1$ 除法，也没有线性化。

允许入口本身有实际有限误差，记
$$
b_0=\sup_\theta|u(0,\theta)-1|,\qquad
b(s)=b_0+\int_0^s\frac{\|R_\theta(\sigma,\cdot)\|_\infty}
                              {a(\sigma)}\,d\sigma,
\qquad r(s)=\|R(s,\cdot)\|_\infty .
$$
沿固定材料角积分式 (5)，得 $|u-1|\le b$，于是
$$
\boxed{
\begin{aligned}
|E-1|&\le 2r+r^2,\\
|Q|/a&\le r(1+b),\\
|G/a^2-1|&\le 2b+b^2.
\end{aligned}} \tag{6}
$$
这些式子对任意非负 r、b 成立。完整 unit-speed 核和精确入口定义给 $b_0=0$；实际反函数/求积/插值误差若没有支付，则应使用其真实入口误差或界，不能仅凭声明令 $b_0=0$。

在 $g_0$ 正交归一基中，度量差矩阵是
$$
\begin{pmatrix}E-1&Q/a\\Q/a&G/a^2-1\end{pmatrix}.
$$
因此相对 operator 范数可再由
$$
\max\{\,2r+r^2+r(1+b),\
         2b+b^2+r(1+b)\,\} \tag{7}
$$
控制。这只是充分界；R 在 Frenet 分量上的抵消可能使实际 metric 远小于这个上界。不能因 (6) 较大反推实际 metric 不通过。

若这些上界对整个 t 区间一致，且所有原域条件也一致，则可逐个 t 使用同一结论。有限 t 采样不自动给这个一致性；闭合、C² 连续族、嵌入与 reach 也不由本条推出。

## 4. moving 材料角图与真实 mean 必须一并保留

原实际数值坐标为 $(s,\psi)$，材料角是
$$
\theta=\theta(s,\psi),\qquad
\rho=\theta_\psi>0,\qquad v=\theta_s/\rho.
$$
把尚未加竖直 mean 的完整场写成 P；它包括背景、有限状态和完整 reference lift。最终场为
$$
\widehat F(s,\psi)=P(s,\psi)+m(s)e_3.
$$
固定材料角求导的算子是
$$
D_s=\partial_s-v\partial_\psi,\qquad
D_\theta=\rho^{-1}\partial_\psi .
$$
因为 $\rho_s=(v\rho)_\psi$，这两个算子交换，它们正是实际材料坐标的坐标导数。

原源码的速度为
$$
W=V+vP_\psi.
$$
所以应当用的完整残差是
$$
\boxed{R=P_s+m'e_3-W,\qquad
       R_\theta=\rho^{-1}\partial_\psi R.} \tag{8}
$$
它等于 $D_s\widehat F-V$。式 (4)—(7) 全部使用这个 R；不能只把 $P_s-V$ 叫作残差，也不能对 $\psi$ 求导后漏除 $\rho$。

在 $\psi$ 图中，式 (4) 的正确写法为
$$
(\partial_s-v\partial_\psi)
 \left(\frac{|P_\psi|^2}{a^2\rho^2}\right)
 =\frac{2}{a^2}\frac{P_\psi}{\rho}\cdot
                      \frac{\partial_\psi R}{\rho}. \tag{9}
$$
所以 b(s) 中的积分对应固定材料角路径；使用各 s 全角 supremum 之后才可直接作一维径向积分。

原 continuous mean 规范是
$m'(s)=(2\pi)^{-1}\int W_z(s,\psi)\,d\psi$，即均匀 $\psi$ 平均。这里不换成带 $\rho$ 权的平均，也不添加一个可调 mean 斜率或接缝常数。参考转移时保持同一个 m(0)。

公式 (8) 实际上允许任何明确定义的 C¹ 函数 m，但必须使用**该实际图的真实导数 $m'$**。如果 m 只是一个有限 Gauss 求积实现，不能未经误差分析就宣称该实现的导数严格等于 continuous mean。设真实导数与所用 mean 速度有误差 $e_m(s)$，则残差必须加 $e_m e_3$；r 的预算需加 $|e_m|$。该修正与角无关，所以不改变 $R_\theta$。实际 mean 二 jet 和位置积分误差仍另行验收。

## 5. 与现有实际 audit 对应的直接诊断

原 adaptive.audit 取实际物理 quintic 的
$Y=\mathrm{sol}(s)$、$Y_s=\mathrm{sol}'(s)$，再形成

$$
P_s=g[\mathrm{s1}]+q_g\,\mathrm{values}(Y_s,B).
$$

因此式 (8) 中的 $P_s$ 可以从现有对象直接得到。**不能用 flow.fun 返回的投影速度替换实际插值导数 $Y_s$**，否则会先把径向表示缺陷人为消掉再报告小残差。参考 lift 的 $g[\mathrm{s1}]$ 也不能省略。

下面只说明有限采样诊断的算法，未执行。mean_velocity 应是该实际图采用的 mean 导数；若填入有限角平均，必须标为该离散 mean 规范下的采样诊断，并另列 mean 的连续误差。

~~~python
Y = physical.sol(s)
Ys = physical.sol(s, 1)
B, B1, B2 = flow.basis(N)
fr = flow.frame(s, q_gauge * Y, B1, B2)
g = fr["geo"]
Ps = g["s1"] + q_gauge * flow.values(Ys, B)
Ps[:, :, 2] += mean_velocity[:, None]
R = Ps - fr["V"]                     # fr["V"] includes v * P_psi
Rhat = np.fft.fft(R, axis=1) / N
k = np.fft.fftfreq(N, d=1.0/N)        # every Cartesian integer frequency
coeff_norm = np.linalg.norm(Rhat, axis=2)
r_trig_l1 = np.sum(coeff_norm, axis=1)
rpsi_trig_l1 = np.sum(np.abs(k)[None, :] * coeff_norm, axis=1)
~~~

若使用真 Fourier 系数且加权和收敛，并有真实的 $\rho\ge\rho_*>0$，则
$$
\|R\|_\infty\le\sum_k|\widehat R_k|,\qquad
\|R_\theta\|_\infty\le
 \rho_*^{-1}\sum_k |k|\,|\widehat R_k|.
\tag{10}
$$
有限 DFT 只给对应三角插值的系数。它可能混叠未分辨高频；原 frame 的非线性正根使 R 即使在有限状态下也不必为有限三角多项式。故上述代码的结果仅为采样/插值诊断，没有连续余项证书。若 $\rho_*$ 也只是节点最小值，仍须明确其采样性质。

尤其应保留三个 Cartesian 分量的全部频率。平面径向/切向基含额外的角频率偏移，不能只计算高度块的 $4j$ 或 $3j$ 模态就称完整 $R_\theta$。

为了诊断“原 projected RMS 已小但 full metric 未过”，可在同一实际候选上比较：现有 full metric 的三个分量、式 (8) 的完整 R、其高频壳和 $|k|$ 加权壳，以及提高评价角点后的变化。仅提高评价点不会修正实际场；只有增加场表示并满足新方程或改变设计，才可能降低相应未投影缺陷。后者若改变 q/c/g，必须另开设计序列，不能接进固定参数加密曲线。

## 6. 本条解决的范围

本条严格保留原 frame 以实际长度计算曲率的规则，因此公式不以现有等距约束为前提。它解释了固定物理设计后为什么需要控制完整速度残差的角导数，也给出可用于将来连续误差预算的显式积分界。它不证明某一冻结核存在精确可闭合解、不宣称当前材料圆化候选的 metric 主因已经定位，也没有为任何实测数值重新发证。

定义依据为原 Flow.geo/frame/audit 的实际源码（本次只读 Git blob 7c299ca34faa3b0b3470ac4a8c3a587d8c6b9f4d；n4 loader 的频率替换不改变这里的 frame 公式）、[R49](../results/R49-frenet-mean-invariance-under-exact-reference-transfer.md) 的共同 mean 和正根定义，以及本日固定参数场校正接口。所有新数值执行仍需实际原终态、完整 metric/真实尾/mean 与非mean 两 jet 门；当前失联 n4 作业状态不变。
