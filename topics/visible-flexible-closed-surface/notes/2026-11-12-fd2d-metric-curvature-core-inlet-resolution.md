# R116 中央入口的有限 Fourier 分辨率与共用角反解

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

## 1. 新支撑种子的实际入口分辨率

准确中央初值由 `fd2d_metric_curvature_core.py` 定义。
`fd2d-metric-curvature-core-inlet-screen.py` 将其在**所有 d 共用的原椭圆偏心角 θ**上投影，
保留原 GC 的 D2 奇偶列规范，分别以 longdouble 和实际 binary64 系数构造有限 Fourier 曲线。
metric 由投影后的 X 的实际角导数形成；没有用辅助 frame 的正交关系代替它。
这里只计算中央入口，没有径向 ODE 或 BVP。

检查源码 SHA256 为
`74ce1a6416dfe0add130ded57de7569b32c20e0df15059ac9a8dca2aacac09f6`。
真实报告 `2026-11-12-fd2d-metric-curvature-core-inlet-screen-01.json` 的 SHA256 为
`915071b740c762b042108a6a8ffab17d9406a57bb72c011535f2c1143b4a8d81`。
会话 35328 自然 exit 0，7.69 秒。

下面是 $d=0$、准确 R115 $p_1=.005$ 支撑种子、2048 角点、binary64 系数的实测值。
M 是 θ 的最大 Fourier 频率，不是曲率参数 d 的数量。

| M | 实际投影位置 metric | n 投影误差 | 实际曲线曲率误差 | 第二位置 jet 误差 |
|---:|---:|---:|---:|---:|
| 31 | $5.0965247903\times10^{-5}$ | $3.4009762103\times10^{-3}$ | $2.1276550963\times10^{-3}$ | $6.0978114864\times10^{-4}$ |
| 63 | $2.7985808062\times10^{-8}$ | $3.1649015815\times10^{-6}$ | $2.3544263928\times10^{-6}$ | $6.3137965082\times10^{-7}$ |
| 95 | $2.0950201860\times10^{-11}$ | $3.3746069832\times10^{-9}$ | $2.6496897077\times10^{-9}$ | $6.9444238608\times10^{-10}$ |
| 127 | $1.8255037239\times10^{-14}$ | $3.8071217186\times10^{-12}$ | $3.0679916073\times10^{-12}$ | $7.9489865211\times10^{-13}$ |

因此该支撑种子在 M=63 的有限位置入口已经超过 $2\times10^{-9}$，
不能把此前纯椭圆 M=63 的行为移到新种子。
M=95 和 127 的中央位置 metric 有余量，可供后续真实 BVP 选择；
这不说明径向推进后仍有同样误差，也不支付完整尾接合。

窗口例子 $d=(3/5000,-1/2500,1/5000,-1/10000)$ 的结果很接近，
M=95 和 127 的实际 metric 分别为 $2.0950863657\times10^{-11}$、$1.8122656154\times10^{-14}$。
1024 与 2048 点独立采样后，前 127 模的最大原始系数差小于 $3.01\times10^{-19}$。
这是有限求值比较，不是一个连续 Fourier 余项证书。
所有较差的 M=31/63 记录都在报告中保留。

## 2. 材料角和共用偏心角必须正确转换

中央未知量是
$n_d(u)=n_*(u)+\sum_jd_j\cos(2ju)$。
在 θ 网格上，它是 $\cos(2j\,u(\theta))$，不能直接替成 $\cos(2j\theta)$。
固定 θ 的参数方向导数无需对 u 再求导，因为这个坐标变换与所有 d 无关。

令 $u_\theta=\ell_E/a_0$。GC 中

$$
\frac1a\partial_u=\frac1b\partial_\theta,
\qquad b=(a/a_0)\ell_E.
$$

把 θ 表示送回材料 u 的尾 Fourier 数据时，可以用同一个 $\theta(u)$ 重采样；
也可以计算带权积分

$$
\widehat f_k=\frac1{2\pi}\int_0^{2\pi}
f(\theta)e^{-ik u(\theta)}u_\theta(\theta)\,d\theta.
$$

直接对 θ 做 FFT 后把系数叫作 u 系数，会给出不同的尾边值问题。
二 jet 的逆转换是

$$
X_u=\frac{X_\theta}{u_\theta},\qquad
X_{uu}=\frac{X_{\theta\theta}}{u_\theta^2}
-\frac{X_\theta u_{\theta\theta}}{u_\theta^3}.
$$

## 3. 实际共用逆角 helper

`scripts/fd2d_metric_reference_angle.py` 的 SHA256 为
`29e9ddd4af2e0a791a42bb75e9639eb463fa43110ac7b7d45bbc4ea51f77b92d`。

```python
from fd2d_metric_curvature_core import SupportSeed
from fd2d_metric_reference_angle import reference_angle_from_material

seed = SupportSeed()
coordinate = reference_angle_from_material(u, seed=seed)
theta = coordinate["theta"]
```

它返回 `theta`、`theta_u`、`theta_uu`，分别满足

$$
\theta_u=\frac{a_0}{\ell_E},\qquad
\theta_{uu}=-\frac{a_0^2\ell'_E}{\ell_E^3}.
$$

它反解的是原椭圆的 `arc_nodes`，不是支撑种子的 `seed_arc_nodes`。
求解使用同一 longdouble 单调弧长表和括号；准确函数定义仍是原椭圆弧长反函数。
实际 `2026-11-12-fd2d-metric-curvature-core-inverse-angle-check-01.json`
覆盖 547 个正、负、跨周期和轴点，正反复合材料角误差为
$3.469446951953614\times10^{-18}$，
一、二阶链式误差为 $1.0842021724855044\times10^{-19}$、
$1.5720931501039814\times10^{-18}$。
这些是数值代表的有限检查，没有给尾 Fourier 转换自动附加连续证书。
