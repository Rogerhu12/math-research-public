# R5：完整凸核心角图与保像拉回

2026-11-10，visible-larger-astra-20261110。

**状态：已证明，中间结果。** 本结论是坐标和表示恒等式；不提供闭曲面、不解决边值方程，也不把有限 Fourier 投影当作精确等距变换。

## 命题一：无退化的完整核心图

设有限支撑谱 $h(\psi)=1+\sum_jq_j\cos(n_j\psi)$ 满足 $\rho_0=h+h''>0$，并令

$$
Q(\psi)=\sum_j\frac{1-n_j^2}{n_j}q_j\sin(n_j\psi),\quad
\gamma(\psi)=(h+ih')e^{i\psi}.
$$

取 $C^2$ 函数 $0\le b\le1$，入口两 jet 为 $(1,0,0)$，末端两 jet 为 $(0,0,0)$。则

$$
\theta=\psi+bQ,\qquad
\rho=\theta_\psi=(1-b)+b\rho_0>0
$$

定义每个径向位置上的全局圆周坐标。若 $a(0)=1$，参考图

$$
X_{\rm ref}=a(s)\{(1-b)e^{i\theta}+b\gamma(\psi)\}
$$

在入口严格等于完整核心，在末端严格等于圆周参考，且其全部二 jet 没有隐含接缝项。因而固定完整核心可用严格零入口扰动表示，不受所保留 Fourier 阶数影响。

**证明。** $\rho$ 是两个严格正函数的凸组合。$Q$ 周期且 $\theta(\psi+2\pi)=\theta(\psi)+2\pi$，故 $\theta$ 是圆周上保向微分同胚。直接代入 $b$ 的端点值及一、二阶导数即得参考图的端点断言。注意参考图自身不必等距；把实际图写成参考加未知扰动只是恒等分解。对任意实际图 $\widetilde F(s,\psi)$，置 $v=\theta_s/\rho$，链式法则给出

$$
F_s=\widetilde F_s-v\widetilde F_\psi,\quad
F_\theta=\widetilde F_\psi/\rho,
$$

$$
F_{ss}=\widetilde F_{ss}-2v\widetilde F_{s\psi}
+v^2\widetilde F_{\psi\psi}+(vv_\psi-v_s)\widetilde F_\psi,
$$

$$
F_{s\theta}=\frac{\widetilde F_{s\psi}-v_\psi\widetilde F_\psi-v\widetilde F_{\psi\psi}}{\rho},\qquad
F_{\theta\theta}=\frac{\widetilde F_{\psi\psi}}{\rho^2}-\frac{\rho_\psi\widetilde F_\psi}{\rho^3}.
$$

这些是同一实际映射在新旧坐标中的导数，所以按这些公式计算不会改变度量。证毕。

## 命题二：更换角图必须保留高度均值

设旧、新角图均如上严格保向，且物理径向坐标、长度和映射都不变。唯一函数 $\eta$ 满足 $\theta_o(s,\eta)=\theta_n(s,\psi)$。定义 $\widetilde F(s,\psi)=F_o(s,\eta)$，则该拉回精确保留像。它的第一导数由

$$
\eta_\psi=\rho_n/\rho_o,\qquad
\eta_s=(\theta_{n,s}-\theta_{o,s})/\rho_o
$$

决定，二阶导数由再次隐式微分唯一确定。若新参考竖直分量为零，且表示中的非零竖直 Fourier 模要求均值为零，则唯一正确的新竖直均值为

$$
H_n(s)=\operatorname{mean}_{\psi}\widetilde F_z(s,\psi).
$$

一般 $H_n\ne H_o$；保持旧均值会把像随 $s$ 竖直平移，通常改变诱导度量。

**证明。** 保向性和圆周周期给出唯一逆，故拉回逐点遍历原像。隐函数定理和链式法则给出上述导数。对等式 $\widetilde F=X_n+qY+H_ne_z$ 取竖直平均，使用 $X_{n,z}=0$ 与 $\operatorname{mean}Y_z=0$，得到均值公式及唯一性。因为 $C^2$ 正则性允许平均与 $s$ 微分交换，同样必须保持 $H_n'$、$H_n''$。删去 $H_n-H_o$ 后，新的径向导数增加 $(H_o'-H_n')e_z$，故除非发生特殊抵消，度量也随之改变。证毕。

全部二阶隐式公式和实现接口分别见 [角图说明](../notes/geometric-general-core-chart.md) 与 [拉回说明](../notes/geometric-checkpoint-core-pullback.md)。`computations/geometric-general-core-chart.py` 实现已知参考和导数，`computations/geometric-checkpoint-core-pullback.py` 同时输出高度均值及其一、二阶导数和有限投影误差。两种真实 checkpoint 的转换报告只验证这些表示操作；重设核心、缩放振幅或改变 profile 都必须另作新的求解。
