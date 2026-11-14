# R116 同 g 中央曲率族：实际 provider 与固定材料参数 JVP

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

本文件交付 R116 §6 的可计算中央初值。它以 R115 的准确
$A=7/5,B=1/2,p_1=1/200$ 支撑曲线为种子，保留相同的 $a_0$ 和材料角 $u$。
这是中央曲线、中央柱和其参数切线；没有由此得到完整强目标闭面、非线性尾匹配或全域 reach。
旧 M12 同 g 修复与本文件的新强目标参数族是不同研究对象。

## 1. 实际文件与接口

源码 `scripts/fd2d_metric_curvature_core.py`，SHA256
`7aa0d7173cc25891a7d422056d64b81e1daa2e40552043a1881627933eae2ad0`。

```python
from fd2d_metric_curvature_core import CurvatureCore, SupportSeed

seed = SupportSeed()
core = CurvatureCore(["3/5000", "-1/2500", "1/5000", "-1/10000"], seed=seed)

material = core.evaluate(u)
material_direction = core.jvp(u, v)
reference = core.evaluate_reference_angle(theta)
reference_direction = core.jvp_reference_angle(theta, v)

state_values = reference["gc_values"]
direction_values = reference_direction["gc_values"]
```

对 N 个角点，最后两项的形状都是 `N × 14`，列依次为

| 列 | 内容 |
|---|---|
| 0、1 | 正向法曲率 n、混合曲率 m |
| 2–4 | X 的 xyz |
| 5–7 | e1 的 xyz |
| 8–10 | e2 的 xyz |
| 11–13 | N=e1×e2 的 xyz |

这与 `fd2d-gc-ellipse-flow.py` 和其 hybrid 入口的列序相同。
`jvp` 字典中相同名字的字段表示参数方向导数；没有对原始度量求导。
无需完整大 Jacobian 时直接使用 JVP；`parameter_jacobian(u)` 可按参数维堆叠列，
得到 `J × N × 3` 或 `J × N × 14` 的对应数组。

位置接口同时返回 `X_u`、`X_uu`、`X_s`、`X_ss`、`X_su`。
偏心角入口保留这些材料导数，并额外给 `X_theta`、`X_theta_theta`、`X_s_theta`，
以及 `u`、`u_theta`、`u_theta_theta`、`ell_reference`。
`n_u`、`m_u` 与偏心角的 `n_theta`、`m_theta` 也明确区分。

## 2. 准确定义及稳定的增量位置

记准确种子为 $\gamma_*(u)$，速度恒为 $a_0$，单位切向为 $T_*$，
内法向为 $N_*=e_z\times T_*$。R115 给出它的弧长反函数与全部中央两 jet。
令

$$
q_j(u)=\frac{a_0}{2j}\sin(2ju),\qquad
\delta(u)=\sum_jd_jq_j(u),\qquad
n_d(u)=n_*(u)+\sum_jd_j\cos(2ju).
$$

定义

$$
T_d=\cos\delta\,T_*+\sin\delta\,N_*,\qquad
N_d=\cos\delta\,N_*-\sin\delta\,T_*.
$$

由于 $\delta'=a_0(n_d-n_*)$，有 $T_d'=a_0n_dN_d$。
实际位置使用准确等式

$$
\gamma_d(u)=\gamma_*(u)+a_0\left[
\int_0^u(T_d-T_*)(v)\,dv-
\frac12\int_0^\pi(T_d-T_*)(v)\,dv\right].
\tag{1}
$$

这与 R116(7) 相同，因为种子已具有相同的中心规范。
数值求积时直接计算

$$
T_d-T_*=-2\sin^2(\delta/2)T_*+\sin\delta N_*;
$$

没有把两个量级为 1 的完整切向或位置相减。`d=0` 的位置直接返回种子，
不会重新对完整种子切向求积。中心平移项保留；不能只积分局部切向差而漏掉它。

对任意 $u$，先把它按反中心对称化到 $[0,\pi)$，计算 (1) 中的小增量，再乘回符号。
这与 $T_d(u+\pi)=-T_d(u)$、$\gamma_d(u+\pi)=-\gamma_d(u)$ 的准确恒等式一致。
零均值偶曲率参数使总转角保持 $2\pi$，闭合与共同周长不靠一次数值积分猜测。
R116 §6 的正曲率论证给出准确嵌入性。

中央两 jet 为

$$
X=\gamma_d+s e_z,\quad X_u=a_0T_d,\quad
X_{uu}=a_0^2n_dN_d,\quad
X_s=e_z,\quad X_{ss}=X_{su}=0.
\tag{2}
$$

因此整个中央柱的度量准确为 $ds^2+a_0^2du^2$，与 d 无关。
中央标架取 $e_1=e_z,e_2=T_d,N=N_d$，第二基本形式分量为 $m=0,n=n_d$。
它与 R116 的正 n 分支、径向标架方程一致。

## 3. 固定材料 u 的参数导数

给定参数方向 v，令

$$
Q_v(u)=\sum_jv_jq_j(u),\qquad C_v(u)=\sum_jv_j\cos(2ju).
$$

则

$$
\dot T=N_dQ_v,\qquad \dot N=-T_dQ_v,\qquad
\dot n=C_v,\qquad\dot m=0,
$$

并且

$$
\begin{aligned}
\dot X&=a_0\left[\int_0^uN_dQ_v\,dv-
\frac12\int_0^\pi N_dQ_v\,dv\right],\\
\dot X_u&=a_0N_dQ_v,\\
\dot X_{uu}&=a_0^2(C_vN_d-n_dT_dQ_v).
\end{aligned}
\tag{3}
$$

$\dot e_1=\dot X_s=\dot X_{ss}=\dot X_{su}=0$；
$\dot e_2=\dot T$、$\dot N$ 按上式。
对 n 的材料角导数直接得到
$\dot n_u=-\sum_j2jv_j\sin(2ju)$。
全部 JVP 用这些表达式求值，没有有限差分或 Fourier 截断。

这里 d 是曲率系数；它与 R115 的支撑系数 p 不同。
种子的法向角反函数不随 d 重新求导：曲率扰动已直接定义在固定材料 u 上。

## 4. 所有 d 共用的偏心角入口

基准偏心角始终是原 $A=7/5,B=1/2$ 椭圆的同一个 $\theta$。
它既不是每个 d 自己的法向角，也不是非椭圆支撑种子的所谓偏心角。
取

$$
u(\theta)=\frac{S_E^{\rm ecc}(\theta)}{a_0},\qquad
u_\theta=\frac{\ell_E(\theta)}{a_0},\qquad
u_{\theta\theta}=\frac{\ell'_E(\theta)}{a_0}.
$$

位置和参数导数均使用

$$
X_\theta=X_u u_\theta,\qquad
X_{\theta\theta}=X_{uu}u_\theta^2+X_u u_{\theta\theta}.
\tag{4}
$$

因为此坐标变换与 d 无关，(4) 对 JVP 同样成立。
中央目标角度量准确为 $\ell_E(\theta)^2d\theta^2$，
后续同一径向背景则写为 $ds^2+(a(s)/a_0)^2\ell_E(\theta)^2d\theta^2$。
Gauss–Codazzi 中使用 $b^{-1}\partial_\theta$，相位与尾 Fourier 角仍是材料 u。

## 5. 参数窗与数值代表的范围

构造器把输入的二进制浮点数或有理数字符串保留为准确有理系数。
它要求充分正曲率条件 $\sum|d_j|<200/787$，但这本身不表示落在 R116 的强中央窗。
`summary()` 另外按有理上界 $a_0<201/200$ 检查

$$
T_0\le\frac1{20},\qquad
\frac{201}{200}\sum_j\frac{|d_j|}{2j}\le\frac1{2000}.
$$

这足以支付 R116(9)。形状位移也给出有理上界

$$
\frac{11}{7}\left(\frac{201}{200}\right)^2
\sum_j\frac{|d_j|}{2j},
$$

由 (1)、$|T_d-T_*|\le S_0$ 和 $\pi<22/7$ 直接推出。
这个窗只支付中央几何余量，不能替代整核的 slab、held、球包、尾条件或全域法球。

数值 seed 使用 longdouble 的分段 Gauss 求积和带单调括号的弧长反函数。
$a_0$ 独立按准确椭圆积分定义计算，并非用求积结果重新选定周长。
曲线增量用有限 Gauss 求积；实际数值输出不是区间包围。
GC/BVP 必须继续检验其投影后实际 X 导数和完整 E、F、G。

## 6. 已完成的有限核对

检查源码 `scripts/fd2d-metric-curvature-core-check.py`，SHA256
`72ee6d339eea860fc1c4bf5ca56aed240155d063df2f7ad6451119357179a21a`。
实际报告 `2026-11-12-fd2d-metric-curvature-core-check-01.json`，SHA256
`bf0bfc408cb0b21061b07f86297fc73c4fe8e8ac429397f0c4e161d2cb1046a7`。
会话 77936 自然 exit 0，11.95 秒。

真实例子取 $d=(3/5000,-1/2500,1/5000,-1/10000)$，属于上述中央窗。
257 个角点的结果如下。

| 核对项 | 实测值 |
|---|---:|
| 材料角相对 metric 误差 | $2.168404344971009\times10^{-19}$ |
| 共用偏心角相对 metric 误差 | $2.710505431213761\times10^{-19}$ |
| 标架正交误差 | $1.0842021724855044\times10^{-19}$ |
| 反中心 / 镜像位置误差 | $4.98\times10^{-19}$ / $5.53\times10^{-19}$ |
| 增量求积加密后的最大位置差 | $2.7601943339676196\times10^{-18}$ |
| 加密后的第二 jet 差 | $6.403157042478017\times10^{-17}$ |
| 加密后位置 JVP 差 | $2.0328790734103208\times10^{-20}$ |

固定材料 u 的中心参数差分从步长 .001 降到 .0003，
位置 / 一 jet / 二 jet 导数差分别由
$1.26\times10^{-10},2.36\times10^{-10},8.03\times10^{-10}$
降为 $1.13\times10^{-11},2.12\times10^{-11},7.23\times10^{-11}$，
与中心差分的二阶截断比例一致。偏心角二 jet 的相同核对也呈相同比例。
另用 70 位不完全椭圆积分独立计算三个种子点，最大位置差 $4.08\times10^{-19}$。
`d=0` 位置确实逐位等于同一 seed 入口，没有重新积出整条曲线。

这些有限核对用于确认接口和数值求值，没有把样点误差提升为连续证书。
准确同 g 中央族、闭合、凸性窗与参数公式由 R115、R116 和本文 (1)–(4) 支付。
