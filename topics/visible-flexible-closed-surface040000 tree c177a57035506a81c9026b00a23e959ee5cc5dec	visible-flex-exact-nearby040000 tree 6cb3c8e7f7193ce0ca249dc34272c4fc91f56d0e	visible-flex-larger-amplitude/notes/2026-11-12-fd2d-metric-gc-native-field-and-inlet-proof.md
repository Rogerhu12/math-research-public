# 真实小分支的原生 C1 场、两种计算坐标和初值连续后验

2026-11-12，fd2d / metric_closure。

本次直接消费 numerical 已闭存的
`2026-11-12-fd2d-numerical-gc-design-p148-small-01-{field.npz,polynomial.npz,report.json,candidate.json}`。
没有重求 BVP、旧 ODE、frame 或位置。

**已证明的部分：** 下述共享 C1 场定义、完整两坐标残差恒等式、全前缀原生字段界、全材料角初值界 $d_0,k_0$。
**数值诊断：** 整个真实前缀的非配点残差和 R119 sampled-cell surrogate。
后者没有被写成连续残差证书；当前尾仍是线性 initializer，未付完整 cut 平均模失配或强目标闭核。

## 1. 实际输入和准确有限定义

该次完整有限求解正常结束，238 个节点、237 个 span，原生变量是

$$
\eta=\log(n/n_r),\qquad \zeta=m/n_r,
\qquad n_r=\frac{\sqrt{1-a_s^2}}a.
\tag{1}
$$

95 个实系数的顺序为

$$
[\eta_0,\eta_2,\ldots,\eta_{94},\zeta_2,\ldots,\zeta_{94}],
$$

分别乘 cos、sin，无额外 $\sqrt2$。真实 T 为 `.013443199905959788`；reference T 为 `.013443229317710758`。本消费者固定这一真实 T，不将外层 T 变化称为同 g 加密。

每个系数由保存的 shared binary64 节点、值及 **`sol.sol(mesh,1)` 真一阶 x 导数**定义准确三次 Hermite 多项式；另存的 RHS 没有替换定义导数。对 $h=x_1-x_0,t=(x-x_0)/h$：

$$
y=y_0+h d_0t+[3(y_1-y_0)-h(2d_0+d_1)]t^2
+[-2(y_1-y_0)+h(d_0+d_1)]t^3.
\tag{2}
$$

全部 binary 数按准确有理数解释，因此相邻 span 的值和一导准确一致。此定义与独立舍入的原 `sol.c` 明确区分。

实际物理场定义为 (1) 的逆变换

$$
n=n_r e^\eta,\quad m=n_r\zeta,\quad
l=n_r e^{-\eta}(\zeta^2+\kappa),
\qquad \kappa=-\frac{aa_{ss}}{1-a_s^2}.
\tag{3}
$$

保留整个指数函数，不先把 n 再投影到有限 Fourier 空间。字段 C1 及 $a\in C^2$、正分母足以给连续 $l$ 和所需角导；没有假定全局 $a_{sss}$ 或 $l_s$ 存在。

原数据 SHA：field 为
`a1dea96f1c97fcf993b5ffb777ec0aa3eca53a22520d6f3037e78756761ef8a1`，
原 polynomial 为
`39074348a0a0060b37fc398b3d243f61df7ce503a05ad7b1bf722588a8f0db4c`。
准确共享场 manifest 为 `2026-11-12-fd2d-metric-gc-p148-small01-native-field.json`，绑定实际中央 circle-base 参数及原准确 μ/矩包。

## 2. x、s、ξ、u 的准确区别

真实物理径向长度是 $s=S(x,T)$，而原生三次多项式的自变量是固定计算 x。记

$$
J=S_x>0,\quad
u=U(x,\xi)=(1-\beta(x))U_{seed}(\xi)+\beta(x)\xi,
\quad q=U_\xi>0,\quad w=U_x/q.
\tag{4}
$$

β 在固定 x 区间 `[.58,1.4]` 上用 quintic step。原驱动模板的 chart 字符串用字母 s；新 manifest 明确它在该 T-design 计算中实际接收 x。不能将它另改为 $\beta(S(x))$。

对任意字段 f，固定物理材料角的导数是

$$
\partial_s f\big|_u=\frac{f_x-wf_\xi}{J},
\qquad f_u=f_\xi/q.
\tag{5}
$$

实际图仍按 R119 在固定 u 上解原 skew frame ODE。若用 x 作为积分变量，只将物理径向生成矩阵乘 J；不添加移动角连接来定义另一张有限残差图。

## 3. 保留背景相消的残差与清分母式

令 $a'=a_s,a''=a_{ss}$，$v^2=1-a'^2$，$c=a'/a$。直接微分 $n_r=v/a$ 得

$$
\frac{(n_r)_s}{n_r}=c(\kappa-1),\qquad
\kappa=-aa''/v^2.
$$

把 (3)、(5) 代入 R119 的两条 Codazzi 残差，准确得到

$$
\begin{aligned}
E_\eta={}&\frac{\eta_x-w\eta_\xi}{J}
-\frac{e^{-\eta}\zeta_\xi}{aq}
-c\{e^{-2\eta}\zeta^2+\kappa\operatorname{expm1}(-2\eta)\},\\
E_\zeta={}&\frac{\zeta_x-w\zeta_\xi}{J}
-\frac{e^{-\eta}[2\zeta\zeta_\xi-(\zeta^2+\kappa)\eta_\xi]}{aq}
+c(1+\kappa)\zeta,
\end{aligned}
\tag{6}
$$

$$
\mathcal R_n=n_r e^\eta E_\eta,\qquad
\mathcal R_m=n_r E_\zeta.
\tag{7}
$$

式 (6) 把准确旋转背景的零项先消去，避免计算 $\kappa(e^{-2\eta}-1)$ 时不必要的大数相减。它没有改变数学函数。

再定义只含加、减、乘及指数多项式的分子

$$
\begin{aligned}
P_n={}&aqv^2\eta_x-av^2U_x\eta_\xi-Jv^2e^{-\eta}\zeta_\xi\\
&-Ja'q\{v^2e^{-2\eta}\zeta^2-aa''\operatorname{expm1}(-2\eta)\},\\
P_m={}&aqv^2\zeta_x-av^2U_x\zeta_\xi\\
&-Je^{-\eta}\{2v^2\zeta\zeta_\xi-(v^2\zeta^2-aa'')\eta_\xi\}
+Ja'q(v^2-aa'')\zeta.
\end{aligned}
\tag{8}
$$

逐项乘 (6) 的共同分母 $Jaqv^2$，立刻得到

$$
\boxed{\mathcal R_n=\frac{e^\eta P_n}{Ja^2qv},\qquad
\mathcal R_m=\frac{P_m}{Ja^2qv}.}
\tag{9}
$$

因此现有 finite radial polynomial × 完整 Fourier 的区间后端可以先合并 (8) 的系数，再包围正分母。指数的有限 Taylor 多项式与显式余项也能保持 (8) 中的背景相消。

## 4. 全前缀、全角原生界

三次 Hermite 的 Bernstein 系数准确为

$$
b_0=y_0,\quad b_1=y_0+hd_0/3,
\quad b_2=y_1-hd_1/3,\quad b_3=y_1.
$$

它们的凸包包含整个 span 的值。第一导的 Bernstein 系数是 $3(b_{j+1}-b_j)/h$。因此对每个 Fourier 振幅取这四个有理数的绝对值最大值，再对所有模式求绝对和，严格包围完整角圈；角导再分别乘 $2j$ 或 $(2j)^2$。

`fd2d-metric-gc-native-bounds.py` 已用准确有理运算遍历全部 237 span。向外取少量数字的结果为

| 字段 | 完整前缀与全部 ξ 的严格上界 |
|---|---:|
| $|\eta|$ | .009133427792148 |
| $|\zeta|$ | .012378247533130 |
| $|\eta_x|$ | .339949346932890 |
| $|\zeta_x|$ | .523183711622114 |
| $|\eta_\xi|$ | .025218933195491 |
| $|\zeta_\xi|$ | .038125518691184 |
| $|\eta_{\xi\xi}|$ | .134351665510959 |
| $|\zeta_{\xi\xi}|$ | .174398154775912 |

逐 span 的向外 binary64 上界及准确端点存在 `...native-bounds-01.rows.json.gz`；summary 保存各全局上界的准确有理值。

若 $|z|\le M<1$，由 Taylor 余项及 $e^M\le(1-M)^{-1}$，

$$
\left|e^z-\sum_{k=0}^N\frac{z^k}{k!}\right|
\le\frac{M^{N+1}}{(N+1)!(1-M)}.
\tag{10}
$$

上述真实 η 界使整个前缀 $e^{\pm\eta}$ 的六阶余项不超过 $1.061674\cdot10^{-18}$。对 $e^{-2\eta}$ 在 (10) 中用 $2M$；不能直接套用前一个较小数字。

这些原生界不自动成为小 Codazzi 残差：大项仍须按 (8) 先相消，且目标及图册多项式余项另付。

## 5. 全材料角的实际初始 $d_0,k_0$

本候选的首段准确是中央圆柱，$a(0)=a_0,a'(0)=a''(0)=0$，故 $n_r(0)=1/a_0$。真实 circle-base 中央曲率为

$$
n_{true}=\frac1{a_0}+\sum_jc_j(\cos2j\xi-\mu_j),\qquad m_{true}=0.
$$

保存的原生场给 $n_{field}=e^{\eta_0}/a_0,m_{field}=\zeta_0/a_0$，于是准确相消式

$$
n_{true}-n_{field}
=\sum_jc_j(\cos2j\xi-\mu_j)-\frac{\operatorname{expm1}(\eta_0)}{a_0}.
\tag{11}
$$

η 的共享初始振幅均为准确 dyadic。程序把 Laurent 系数统一为整数除以同一个 $2^p$，以 Python 整数卷积准确形成六阶指数多项式，最后用共同分母 $2^{6p}6!$ 相加。保留 Laurent 指标 $j=-282,\ldots,282$，基底是 $e^{2ij\xi}$，即实际角频率到 $\pm564$；所有剩余模式由 (10) 的一致余项支付。

式 (11) 的有限多项式系数与准确 μ/a0 区间相减后求绝对和，得到

$$
\sup_\xi|n_{true}-n_{field}|
\le1.631982389200216\cdot10^{-16}.
\tag{12}
$$

这里初端指数余项仅 $2.4370\cdot10^{-29}$。ζ 的真实极小非零系数也全部保留，并非直接置零。

在**物理材料角 u**下，真实初始 frame 与场期望的角连接之差为反对称矩阵，算子范数等于

$$
\|D_0\|=a_0\sqrt{(n_{true}-n_{field})^2+m_{field}^2}
\le a_0(|n_{true}-n_{field}|+|m_{field}|).
$$

所以实际完整角后验是

$$
\boxed{d_0\le1.638645511272696\cdot10^{-16},\qquad k_0=0.}
\tag{13}
$$

第二项准确为零，因为初始位置定义就是真实中央曲线，$X_{0,u}=a_0e_{2,0}$。固定 seed 图册整圈双射，故完整 ξ 覆盖同时是完整 u 覆盖。

## 6. 真三次场的非配点诊断

原求解报告的 residual screen 取节点及中点。它们正是该 collocation 方法的插值约束位置，不能据该屏幕的小数值推断内部残差。

本次 `fd2d-metric-gc-design-native-screen.py` 在每个真实 span 的

$$
t=0,\quad \tfrac12-\tfrac{\sqrt{15}}{10},\quad\tfrac14,
\quad\tfrac12,\quad\tfrac34,\quad
\tfrac12+\tfrac{\sqrt{15}}{10},\quad1
$$

及512角点，直接消费 (2)、真导数、完整指数和 (5)。全237格都执行，得到

$$
\max|\mathcal R_n|\approx6.9824660438\cdot10^{-6},\quad
\max|\mathcal R_m|\approx1.3157594151\cdot10^{-5}.
$$

峰位于 cell190，$x\approx1.2033748320,\xi\approx.8344855486$。这与该次求解器的 rms 残差 $1.93345\cdot10^{-5}$ 一致；有限 BVP 仍是按其给定容差真实收敛，不是计算失败。

将每格采样最大值暂代连续上确界，R119 的诊断 surrogate 给 metric 约 $4.93285\cdot10^{-6}$。报告明确 `is_upper_bound=false`。这个数既不能作为合格全域证书，也不能证明实际 ODE 图的 metric 失败；残差在实际 frame/位置积分中可能相消，root 的直接固定 u 后处理和局部 primitive 后验可进一步利用这一点。

cut 未纳入的 n 平均模约 $1.00717\cdot10^{-7}$ 仍保留，不能用这次 finite success 略去真实 nonlinear DN 或接缝。

## 7. 固定 u 的物理求值接口

```python
from fd2d_gc_native_log_physical import PhysicalNativeLogField
model = PhysicalNativeLogField(
    'notes/2026-11-12-fd2d-metric-gc-p148-small01-native-field.json')
v = model.evaluate_material(x, u_array)
```

单个 x、多材料角时，`n,m,l,n_u,m_u,l_u,n_s_material,m_s_material` 是向量；`a,ap,app,J,physical_s` 是相应径向标量。`evaluate(x_array,xi_array)` 给外积网格，矩阵形状为 `(len(x),len(xi))`。

材料逆映射在 $u$ 与 $U_{seed}^{-1}(u)$ 之间用单调 bracket/Newton 求值；两个端点给 β=1/0 的准确对应，混合 map 单调且位于两 map 之间，所以该 bracket 有效。实际6个x、33个u的查询最大数值残差约 $1.35\cdot10^{-17}$。它是浮点评估器，不将此点值残差当成全域 interval 证书。

## 8. 闭存身份

| 实体 | SHA-256 |
|---|---|
| `scripts/fd2d_gc_native_log_field.py` | `33c7fb7bf9a28aa1819adba9bd2fb6ceeb233b701e3706da4321f584d12f46d6` |
| `scripts/fd2d_gc_native_log_physical.py` | `86351ac3da7edd2c2aa98a31e9cbbf9e1f3b911e3d8b724e811b7c02390da619` |
| `scripts/fd2d-metric-gc-design-native-screen.py` | `ce0303cdf38fcac6478bd88aee0bc689c6fe2c90dfafe64629cd055b06758b5b` |
| `scripts/fd2d-metric-gc-native-bounds.py` | `d12c24c18d12495e118e48fd1c503c60cab5aea3fd21385f36314c8a43aa5513` |
| `notes/2026-11-12-fd2d-metric-gc-p148-small01-native-field.json` | `df05c14e863ce3725eb9e3567811f0aced0c13cf3542a0282e5014204814ce72` |
| `notes/2026-11-12-fd2d-metric-gc-p148-small01-native-screen-01.json` | `de0cb8f6a89d88c76101ff17d3d9cfb7705855bfd57626db530b67ff6971a5de` |
| `notes/2026-11-12-fd2d-metric-gc-p148-small01-native-bounds-01.json` | `87630475bce0ed8336d379b573571df3a92c2f2db7e9987b2e0792b42babb299` |
| `notes/2026-11-12-fd2d-metric-gc-p148-small01-native-bounds-01.rows.json.gz` | `7f87fcfa1ebd99c455ba48c631debd14d948b51ce75d3945fb0a28864372c834` |

screen session22590 自然 exit0，8.72秒；物理查询 session11588 exit0；完整原生界及初值证书 session96154 自然 exit0，4.31秒。源数值求解器、既有中央 provider 与旧失败数据均未改。
