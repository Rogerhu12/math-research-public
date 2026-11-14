# R106 补充：同一实际参数管的完整前腿射线管与全时变分界

2026-11-12，constructive-route。

**状态：完整证明并已执行准确有理核验。** 本篇把已经完成的全部 550 段
真实缺陷积分、全部实时间的有限参考导数证书、R80 的真实固定时间参数源
接在同一个对象上，得到实际射线的全时域界。24 个 BigInt 有理门已实际通过。
没有用端点导数代替中间时刻，也没有用八条浮点射线代替连续角带。

对准确中心
$$
p_0=-7789843107295549/4611686018427387904,\qquad
I_\eta=[p_0-\eta,p_0+\eta],\quad \eta=10^{-9},
$$
完整前腿 $\tau\in[-\pi/2,\pi/2]$、整个复标签带 $|\Im x|\le1/1024$，
以下真实射线 $\Theta$ 满足
$$
\boxed{\quad
\operatorname{Re}\Theta_x>0.027370368>0.027,\qquad
|\Theta_x|<1.052629632<1.06,\qquad
|\Theta_{xx}|<1100,\qquad |\Im\Theta|<1/900 .
\quad} \tag{106T.1}
$$
这里 $x$ 是周期 $2\pi$ 的初始标签，$\Theta$ 是物理角；准确首值是
$\Theta(-\pi/2,x,p)=H_5(x)/4$，并非 $\Theta(-\pi/2,x,p)=x$。
因此 (106T.1) 中的导数不再额外乘四。

## 1. 三项实际输入及其身份

全部输入均为已经发布的小 UTF8 证书；本次逐字 SHA256 核对后才执行有理门。

| 输入 | 已付内容 | SHA256 |
|---|---|---|
| notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json | 原 CI 完成输出逐字核验；全 550 段、555 叶的真实缺陷累计 | f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52 |
| notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json | 全 550 段参考导数、全部 549 个 base 与 Q 接缝、准确两端时间 | d1dd69ac94f5912c828a6e22856badcb69bf324fdc7fc9a43f05493161363dc9 |
| data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_certificate.json | R80 完整实际参数管、两支和反射、物理复角带上的参数源 | 08b6fb2f3be32b7d2657d756e547134dcb55a54bb67a89d5f44a7fcd2f9f6e76 |

有限参考的证明是
notes/2026-11-12-step5-forward-reference-derivative-complete.md，
SHA256 fe8e80dbcd97c912456908c213fa8ddec779103e9b1e3b490d573a650b483894。
其原完整有向报告 SHA256 为
87aeff7e8824c7d6301c6f33cbeea506e584004c5bee1591512a556348cbfd8c。

同一参考 descriptor 的 SHA256 必须为
097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052；
原完整 g0 index 的 SHA256 为
4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45。
实际 affine 对象的 SHA256 为
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，
origin 和 direction 仍为 0d17500a…、8db5d57d…。
有理核验器拒绝不同 descriptor、不同中心、未完成覆盖或未验证输出。

参考记为 $Y(\tau,x)$，具有准确实性和提升周期
$$
Y(\tau,x+2\pi)=Y(\tau,x)+\pi/2.
$$
完整实时证书给，在 $S=1/512$ 的标签带上，
$$
\operatorname{Re}Y_x>m=3/100,\qquad |Y_x|<M=21/20. \tag{106T.2}
$$
它还逐字验证全部接缝连续，首值严格为 $H_5/4$。$Y_\tau$ 可在有限接缝处
跳变；下文只需分段连续可积的时间向量场，不要求把该有限参考冒充跨接缝全纯。

原 g0 完整流水线在标签带 $S_g=1/256$ 支付真实
$\int\sup|g_0|$。保存的 R72 内带为 $3/1024$，余量为 $1/1024$，
其和恰为 $S_g$。向外取显示球的上端点得
$$
A_c=
\frac{409256398925551511672190910308412520603}{10^{46}}
>4.0925639892555151167219091030841252\,10^{-8}.
\tag{106T.3}
$$
这里精确分母的幂次由报告中的完整有理字符串重放核对；计算不用显示近似值。
本篇只使用 $A_c$ 的实际真实源模界，不使用最终 endpoint 的逆导数或参数范数。
原 $E_c$ 亦逐字保留供身份复核，但不将它重复加到已经包含真实源的 $A_c$。

## 2. 物理角、固定时间和参数归一

R80 的 $f_\sigma(\tau,\theta,p)$ 是物理角速度 $d\theta/d\tau$，
固定时间为
$$
r=t(p)\sin\tau,\qquad -\pi/2\le\tau\le\pi/2.
$$
其 $\partial_p f_\sigma$ 固定的是 $\tau,\theta$，已经包含 $t'(p)$、
$r_p=t'(p)\sin\tau$、端点 Q 消根和整个无限原函数的真实参数导数。
R80 在 $| \Im\theta|\le1/56$ 和准确 $p_0\pm1/2000000$ 上证明
$$
|\partial_p f_\sigma|<20. \tag{106T.4}
$$
当前 $I_\eta$ 的准确分数包含关系已实际核验。

选择与原前向流水线一致的支，定义每个实际 $p$ 的标签缺陷
$$
g(\tau,x,p)=
\frac{f_\sigma(\tau,Y(\tau,x),p)-Y_\tau(\tau,x)}
     {Y_x(\tau,x)}. \tag{106T.5}
$$
$Y$ 与 $p$ 无关。因而在固定物理时间 $\tau$，
$$
g_p=\frac{f_{\sigma,p}(\tau,Y,p)}{Y_x}. \tag{106T.6}
$$
式 (106T.6) 没有四倍因子。若一段采用 $u\in[-1,1]$、$\tau=c+hu$，
对应源是 $h f_p/Y_x$；沿整个前腿积分的时间总长度仍是
$\sum 2h=\pi$。不能从 endpoint 归一化再借一个四倍因子。

由实性及 (106T.2) 沿竖线积分，
$$
|\Im Y(\tau,x)|\le M|\Im x|,\qquad
MS=21/10240<1/56. \tag{106T.7}
$$
所以 (106T.4) 在整个参考像上适用，而非仅在实角节点适用。
实参数的微积分基本定理与 $|Y_x|\ge m$ 给
$$
\int_{-\pi/2}^{\pi/2}\sup_{|\Im x|\le S}
 |g(\tau,x,p)|\,d\tau
\le A_c+\eta\frac{20\pi}{m}
<A_c+\eta\frac{44000}{21}
=:A_{\rm box}<\overline A=\frac{107}{50000000}.
\tag{106T.8}
$$
仅在最后一步使用已证有理 $\pi<22/7$。没有借用复参数解析性；
R80 给真实整盒 $C^2$ 实参数族，已足够应用此 MVT。
$g_0$ 的已付带更宽，限制到 $S$ 不增加其模界。

## 3. 完整真实坐标流与接缝

令
$$
S_X=15/8192,\qquad R=S-S_X=1/8192.
$$
实际有理核验给 $2A_{\rm box}<R$。对每个 $p\in I_\eta$，解
$$
X_\tau=g(\tau,X,p),\qquad X(-\pi/2,x,p)=x. \tag{106T.9}
$$
标准逐段 Picard 构造可以直接由本处有限不等式证明：在任一已存在的时间段，
只要像仍在 $S$ 内，就有 $|X-x|\le\int\sup_S|g|\le A_{\rm box}$。
由于 $A_{\rm box}<R/2$，该像距离边界始终有正余量，解延拓覆盖全时间。
Cauchy 导数界在更小带上给局部 Lipschitz 常数，保证唯一性；
各个接缝连续地传递同一首值，时间导数仅分段满足方程即可。
由解析 ODE 的 Picard 迭代，$X$ 对初始标签全纯。因此
$$
|X(\tau,x,p)-x|<\overline A
\quad(|\Im x|\le S_X,\ -\pi/2\le\tau\le\pi/2). \tag{106T.10}
$$

定义
$$
\Theta(\tau,x,p)=Y(\tau,X(\tau,x,p)).
$$
在每个开段上链式给
$\Theta_\tau=Y_\tau+Y_xX_\tau=f_\sigma(\tau,\Theta,p)$；
接缝两侧同一 $Y$ 值与同一 $X$ 值，所以 $\Theta$ 连续。
准确首值为 $H_5/4$。它因而是同一个真实几何向量场的完整前腿解，
不是新定义的有限近似。实性、提升周期和实参数连续性也由唯一性保留。

这一论证付的是所有中间时刻的流，没有把全返回的最终误差反推为
任意子时间的误差。

## 4. 一、二阶标签导数与实际角像

现在取 $s=1/1024$，$d=S_X-s=7/8192$。
对全纯函数 $X-x$ 使用完整圆盘 Cauchy 界：
$$
|X_x-1|\le\delta_1=\overline A/d
=\frac{6848}{2734375}<0.00251,
$$
$$
|X_{xx}|\le\delta_2=2\overline A/d^2
=\frac{112197632}{19140625}<6. \tag{106T.11}
$$
像位于标签带 $s+\overline A<S$。写
$$
C_Y=\frac{M}{S-s-\overline A}.
$$
对 $Y_x$ 的 Cauchy 界给 $|Y_{xx}|\le C_Y$，然后
$$
\operatorname{Re}\Theta_x
=\operatorname{Re}\{Y_x(\tau,X)[1+(X_x-1)]\}
>m-M\delta_1
=\frac{213831}{7812500},
$$
$$
|\Theta_x|<M(1+\delta_1)=\frac{8223669}{7812500},
$$
$$
|\Theta_{xx}|
<C_Y(1+\delta_1)^2+M\delta_2
=\frac{1934594494853376}{1776291015625}<1100. \tag{106T.12}
$$
所有乘积均保留，未将 $X_x$ 当作 1。对复标签真实角像，(106T.7) 给
$$
|\Im\Theta|<M(s+\overline A)
=\frac{8221101}{8000000000}<1/900. \tag{106T.13}
$$
同一凸带内沿线段积分还给
$$
|\Theta-Y|
<M\overline A=\frac{2247}{10^9}<2.25\,10^{-6},
$$
$$
|\Theta_x-Y_x|
<C_Y\overline A+M\delta_1
=\frac{1252440778}{253755859375}<1/200. \tag{106T.14}
$$
这两式比较的是同一时刻、同一原始标签，并未把近似 $Q$ 解释为真实 Jacobian。

## 5. 接 R106 的准确用途与范围

在固定实际参数时，$r=t(p)\sin\tau$ 与标签无关。因此远离端点时，
$\Theta_x$ 也正是按径向参数重写的同一射线标签 Jacobian；
(106T.1) 可直接作为 R106 沿射线相位积分的连续输入。
根处的时间延拓已有 R80 的真实 Q 消根门，本篇不另引入一个跨根的
负曲率平方根。

初始标签仍是准确有限 $H_5$ 所给的标签。若 R104 使用 R101 的最终
共轭标签，必须继续支付该完整再参数变换及对应 $\mathscr G_H$，
不能把本篇当前标签默认当成最终 frame。R101 证明的最终实参数在
$I_\eta$ 内，所以参数范围本身没有新的缺口。

本篇没有计算非均值首相位 $b$ 的完整乘子范数，没有支付两个根的
有限部积分，也没有给出 R104 的强 $4/3$ 余项或全低 Schur 逆。
回腿按 R77 是实际半返回的再次复合；(106T.1) 不允许不计实际初值像
而把第二次传播的 strip 或常数免费复制。

## 6. 实际执行与可重放源

源为 scripts/fourfold_subprincipal_true_ray_budget_exact.mjs，
报告为 notes/2026-11-12-R106-actual-all-time-ray-tube.json。
源先逐 UTF8 SHA256 验证 §1 三个输入，再读取每一个显示球的
“中心加显示半径”作为准确向外有理上界，执行全部 24 个 gate。
近似十进制仅用于阅读，判定完全由约分 BigInt 的整数交叉乘法完成。

本次相同 checkedReport/computeRayBudget 的纯实现已在 V8 真正执行，
输出 complete=true。执行器失联期间没有重造旧 density/ODE 报告。
Node CLI 仅是相同纯实现的文件读取重放入口；native CLI 尚未运行。

在课题目录可写到新路径重放：

~~~sh
node scripts/fourfold_subprincipal_true_ray_budget_exact.mjs \
  . /tmp/R106-actual-all-time-ray-tube.json
~~~

冻结报告绑定源的完整 SHA256，并保存全部准确分数、24 个通过标志、
实际三输入及原 g0 index / descriptor / 几何对象身份。
