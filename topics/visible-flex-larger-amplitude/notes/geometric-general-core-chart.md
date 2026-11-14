# 固定强核心的完整角图与无入口投影误差接口

2026-11-10，visible-larger-astra-20261110 / geometric_amplification。

**状态：坐标及参考图恒等式已证明，代码的实际导数检查已完成；尚未给出新的 BVP 或闭图解。** 文件为 `computations/geometric-general-core-chart.py`，只依赖 NumPy。

## 1. 完整支撑谱的材料角图

令固定核心支撑函数为

$$
h(\psi)=1+\sum_jq_j\cos(n_j\psi),\qquad
\rho_0=h+h''>0.
$$

其弧长角为

$$
\theta_0(\psi)=\psi+Q(\psi),\qquad
Q(\psi)=\sum_j\frac{1-n_j^2}{n_j}q_j\sin(n_j\psi).
$$

取 $0\le b(s)\le1$，入口两 jet 为 $(b,b',b'')=(1,0,0)$，尾切口为 $(0,0,0)$。定义

$$
\theta(s,\psi)=\psi+b(s)Q(\psi),\quad
\rho=\theta_\psi=(1-b)+b\rho_0>0.
$$

由严格正性和 $2\pi$ 周期性，这是每个 $s$ 上真正的一周角坐标。程序默认用一条五次平滑截止函数，调用者可通过 `transition_start`、`transition_end` 指定在归一化 $s/L$ 中何处从 1 变到 0。它只定义数值坐标，不改变物理度量 $ds^2+a(s)^2d\theta^2$。

全部角导数为

$$
\theta_s=b'Q,\quad\theta_{ss}=b''Q,\quad
\rho_\psi=bQ'',\quad\rho_s=b'Q',\quad\rho_{\psi s}=b'Q''.
$$

这里 $Q'=\rho_0-1$。定义

$$
v=\theta_s/\rho,\quad
v_s=(\theta_{ss}-v\rho_s)/\rho,\quad
v_\psi=(\rho_s-v\rho_\psi)/\rho.
$$

对任何实际图 $\widetilde F(s,\psi)$，物理切向量是

$$
F_s=\widetilde F_s-v\widetilde F_\psi,
\qquad F_\theta=\widetilde F_\psi/\rho.
$$

其二阶导数与现有 adaptive Frenet 代码一致：

$$
F_{\theta\theta}=\frac{\widetilde F_{\psi\psi}}{\rho^2}
-\frac{\rho_\psi\widetilde F_\psi}{\rho^3},
$$

$$
F_{s\theta}=\frac{\widetilde F_{s\psi}-v_\psi\widetilde F_\psi-v\widetilde F_{\psi\psi}}{\rho},
$$

$$
F_{ss}=\widetilde F_{ss}-2v\widetilde F_{s\psi}
+v^2\widetilde F_{\psi\psi}+(vv_\psi-v_s)\widetilde F_\psi.
$$

所以时间相位作用仍必须在材料角 $\theta$ 上实施；直接平移 $\psi$ 不等于材料角平移。

## 2. 为什么同时更换数值参考图

仅改用完整 $\theta_0$ 还不消除旧表示的入口 Fourier 截断。旧参考为 $a(s)e^{i\theta(s,\psi)}$；在入口，实际核心

$$
\gamma(\psi)=(h+ih')e^{i\psi}
$$

是有限 Fourier 多项式，但差 $\gamma-e^{i\theta_0}$ 通常不是。把差投影到有限谱仍会留下入口度量误差。

本模块默认改用

$$
\boxed{X_{\rm ref}(s,\psi)
=a(s)\bigl[(1-b(s))e^{i\theta(s,\psi)}+b(s)\gamma(\psi)\bigr].}
$$

它是数值表示中的已知参考，**不声称该参考本身等距**。实际图仍为 $X_{\rm ref}$ 加 Fourier 未知扰动和单独积分的高度均值。Frenet RHS 使用实际曲线的切向量、曲率与标架，并减去这个参考的真实 $s$ 导数。因此换参考不改原几何方程。

若 $a(0)=1$，入口参考恰为 $\gamma$，而末端参考恰为 $a e^{i\psi}$。故固定核心问题的入口扰动向量严格为零，任意 Fourier 截断阶数都保留同一完整核心。端点 $b'=b''=0$ 保证参考的一、二阶导数没有隐藏截止项。

模块也提供 `reference='round'`，便于与旧表示比较；这个选项不能用严格零入口，仍需投影。

## 3. 所实现的全部导数

令 $z=e^{i\theta}$。代码先计算

$$
z_\psi=i\rho z,\quad z_{\psi\psi}=(i\rho_\psi-\rho^2)z,
\quad z_s=i\theta_s z,\quad z_{ss}=(i\theta_{ss}-\theta_s^2)z,
$$

$$
z_{s\psi}=(i\rho_s-\theta_s\rho)z,
$$

$$
z_{s\psi\psi}
=\{i\rho_{\psi s}-2\rho\rho_s+i\theta_s(i\rho_\psi-\rho^2)\}z.
$$

核心导数为 $\gamma_\psi=i\rho_0e^{i\psi}$、$\gamma_{\psi\psi}=(i\rho'_0-\rho_0)e^{i\psi}$。令 $B=(1-b)z+b\gamma$，则

$$
B_s=(1-b)z_s+b'(\gamma-z),
$$

$$
B_{ss}=(1-b)z_{ss}-2b'z_s+b''(\gamma-z),
$$

$$
B_{s\psi}=(1-b)z_{s\psi}+b'(\gamma_\psi-z_\psi),
$$

$$
B_{s\psi\psi}=(1-b)z_{s\psi\psi}+b'(\gamma_{\psi\psi}-z_{\psi\psi}).
$$

再乘 $a(s)$ 并用乘积法则，即得接口 `pos,p1,p2,s1,s2,sp,spp`。这些导数包含参考的所有移动项；不能在新的参考下继续使用旧的单余弦背景导数。

`parameter_jvp` 对完整支撑系数方向 $\dot q$ 作解析求导。它保持物理 profile、长度 $L$ 和截止权 $b$ 不变；例如 $\dot z=i\dot\theta z$，所有其余导数由上式直接微分。若 BVP 参数改变 $L$，还要另外包括 $b$ 对长度的变化；不能把这个固定长度接口当作全参数导数。

`profile_jvp` 提供在角图与长度固定时，对 $(a,a',a'')$ 的参考向量导数。它利用参考图对该三元组的线性关系，便于以后固定区间上的多控制 profile 求解。这个方法不包含 Frenet 标架对 profile 的显式响应，使用者仍要把它与原 frame JVP 合成。

## 4. 使用与不能沿用的旧接口

```python
chart = GeneralCoreChart(coefficients, frequencies, flow.end,
                         reference='core-blend')
g = chart.geo(s, angular_count, flow.profile)
dqg = chart.parameter_jvp(s, angular_count, flow.profile, direction)
initial_state = chart.initial(flow)  # exactly zeros, if a(0)=1
```

`attach_to_adaptive_flow(flow,...)` 可以直接替换现有 adaptive Flow 的 `geo` 与 `physical_base`。它要求该 Flow 的 `frame`、RHS、Jacobian、C² 插值和 height 积分确实消费这些字段；旧的常角 `PlanarSymmetryFlow` frame 不满足此条件。代码只检查已有 `geo` 以避免最直接的误用，调用者仍应使用已知 adaptive 类。

接入 BVP 时应覆盖旧的单余弦 `initial`、入口 Jacobian 和 `seed`。对固定核心，`initial(p)` 恒为零，其参数 Jacobian也恒为零。新的真实解需保存全部 core 系数、频数、$b$ 的区间和参考种类；旧的 `warp_reference_q` 单值无法标识这个角图。

旧 checkpoint 的 Fourier 系数表示的是旧参考和旧角坐标下的扰动，不能直接作为新表示的同一图。若要沿用，须先在共同材料角上重建实际位置，再减去新参考并投影；径向导数、额外高度均值和入口的变化也要一致处理。零扰动可以作为新问题的粗初猜，但它通常不是解。

## 5. 实际检查范围

运行 `python computations/geometric-general-core-chart.py` 对 $N=4,r=.15$ 的强核心、非恒定测试 profile 和非端点角度，实测：

- $s$、角度及混合导数与中心差分的最大差约 $1.5\times10^{-9}$；
- 完整支撑参数 JVP 与中心差分的最大差约 $1.8\times10^{-9}$；
- 入口位置与完整核心公式的差为 0，归一化入口角向度量误差不超过 $4.5\times10^{-16}$；
- 末端材料角恒等，入口和末端的 $\theta_s,\theta_{ss}$ 全为 0。

这些检查验证实现的微分接口；它们不是 BVP 成功、全图等距或固定度量加密收敛的证据。
