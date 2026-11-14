# 准确仿射族的整核心复角图表：正对数因子、支撑与面积

2026-11-12。**本笔记所列连续几何分母门已证明并实际运行。**
径向变量与参数都为实数，只有角变量复化。该结论供应实际
R37 图表与修正系数，不声称已经验证 ODE 流、返回残差或精确等距族。

## 1. 同一对象与范围

原始输入为
`type_fixed_step02_d5_jet_interval_inputs.npz`，SHA256
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`；
准确方向为
`type_fixed_step02_d5_actual_parameter_direction.npz`，SHA256
`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。
这里 raw phase 与三个均值控制值先按准确实数作仿射组合，再乘
固定背景权重、作明确径向偶奇平均，并用 R33 无限原函数构造
$F=a\mathcal P T+Ze_z$。高度由实际斜率准确积分定义。

整个证书的域为

$$
|\delta|\le\operatorname{binary64}(.01),\qquad
|r|\le\operatorname{binary64}(.24),\qquad
|\operatorname{Im}\theta|\le\sigma=1/64.
$$

归一化圆坐标 $x=4\theta$ 对应宽度 $1/16$，不能把两种角坐标
的宽度混用。本包的实际支撑/图表结论只针对准确仿射族；R59
更大的独立控制盒只用来提供一个对该子族也有效的面积平方导数界。

令双线性量

$$
Q=F_z/r,\qquad S=F\cdot F,\qquad
G=(F_\theta\times F_r)\cdot(F_\theta\times F_r),\qquad
J=F\cdot(F_\theta\times F_r).
$$

$Q$ 在 $r=0$ 用准确奇性给出的连续延拓；复角中的点积是
**双线性点积**。下面只在估计向量时使用 Hermitian 范数。
实域上 $\nu=(F_\theta\times F_r)/\sqrt G$，
$h=J/\sqrt G$，$\zeta=J/(\sqrt G\sqrt S)$。

## 2. 不重新截断 primitive 的整条带导数界

把显式对称后的有限相位写成
$\beta=\sum b_k(r,\delta)\sin(4k\theta)$、
$\gamma=\sum g_k(r,\delta)\sin(4k\theta)$。
取每个系数及其径向导数的全核心绝对界 $B_{jk},\Gamma_{jk}$。
源码从完整闭样条 span 的凸包得到这些界，原始方向按
$|S_0^{(j)}|+\max|\delta|\,|V^{(j)}|$ 合并，再付背景权重乘积。
负、正半轴都在凸包范围内，故明确偶奇平均也被覆盖。

记 $n_k=4k$，并设

$$
I=\sigma+\sum_k(B_{0k}+\Gamma_{0k})\sinh(n_k\sigma),
\quad I_\gamma=\sum_k\Gamma_{0k}\sinh(n_k\sigma),
$$

$$
P_1=1+\sum_k n_k(B_{0k}+\Gamma_{0k})\cosh(n_k\sigma),
\quad P_2=\sum_k n_k^2(B_{0k}+\Gamma_{0k})\cosh(n_k\sigma),
$$

$$
X_1=\sum_k(B_{1k}+\Gamma_{1k})\cosh(n_k\sigma),\quad
X_\theta=\sum_k n_k(B_{1k}+\Gamma_{1k})\cosh(n_k\sigma).
$$

一个复角旋转的 Hermitian 算子范数为 $e^{|\operatorname{Im}\phi|}$。
对真实 $T$ 的两个旋转因子逐次求导，得到

$$
\|T\|\le e^I,\quad
\|T_\theta\|\le e^IP_1,\quad
\|T_{\theta\theta}\|\le e^I(P_2+P_1^2),
$$

$$
\|T_r\|\le e^IX_1,\qquad
\|T_{r\theta}\|\le e^I(X_\theta+X_1P_1).
$$

这里始终用 $F_\theta=aT$ 与
$F_{r\theta}=a_rT+aT_r$ 的准确无限角定义。沿竖直角线积分，
若实轴已有 $\|F\|\le F_0$、$\|F_r\|\le X_0$，则

$$
\|F\|\le F_c:=F_0+\sigma a_+e^I,
\qquad
\|F_r\|\le X_c:=X_0+\sigma(|a_r|_+e^I+a_+e^IX_1).
$$

不需要把有限 FFT primitive 当成实际 $F$。实轴输入证书已经
支付该实际 $F$ 的无穷角尾；这里的竖直积分是准确解析恒等式。

## 3. 二阶竖直 Taylor 门

对在实轴取实值的解析标量 $f$，其一阶竖直 Taylor 项是纯虚数。
若条带上 $|f_{\theta\theta}|\le M_2$，则

$$
\operatorname{Re}f(\theta+iy)
\ge f(\theta)-\tfrac12 y^2M_2. \tag{1}
$$

明确径向奇性给 $\gamma(0,\theta)=\gamma_\theta(0,\theta)=0$。
因此由径向积分，整个核心（包括 $r=0$）有

$$
|Q_\theta|\le a_+e^{I_\gamma}
 \sum_k\Gamma_{1k}\cosh(n_k\sigma),\qquad
|Q_{\theta\theta}|\le a_+e^{I_\gamma}
 \sum_k n_k\Gamma_{1k}\cosh(n_k\sigma).
$$

这用的是 $Q_\theta=a\sin\gamma/r$ 与
$Q_{\theta\theta}=a\cos\gamma\,\gamma_\theta/r$，没有在腰圈
直接除零。实轴 $Q$ 上界可取全核心 $F_{r,z}$ 的上界，所以也有
$|Q|\le Q_{0,+}+\sigma\sup|Q_\theta|$。

由准确恒等式 $T\cdot T=1$，

$$
S_{\theta\theta}=2a^2+2aF\cdot T_\theta,
\qquad |S_{\theta\theta}|\le2a_+^2+2a_+F_c\|T_\theta\|_+.
$$

实轴 $S\ge h_-^2$。令 $X=F_r$，原始二型系数
$n=F_{\theta\theta}\cdot(F_\theta\times X)$。两次准确求导给

$$
J_{\theta\theta}=-n+aF\cdot
\{T_{\theta\theta}\times X+a_rT_\theta\times T
 +2aT_\theta\times T_r+aT\times T_{r\theta}\}. \tag{2}
$$

已另用独立符号微分检验式 (2)，展开余项准确为零。
$|n|\le a_+^2X_c\|T\|_+\|T_\theta\|_+$，再对括号每项取范数
就得到 $J_{\theta\theta}$ 上界。复向量叉积仍满足
$\|u\times v\|\le\|u\|\|v\|$，因此不需要把实叉积不等式
未经说明地挪到复域。

$G_{\theta\theta}$ 使用 R59 完整592单元证书给出的
$265.0191783741035$ 上界。该证书的域包含本准确仿射子族。
实轴全核心面积下界已付，故对 $Q,S,J,G$ 分别应用式 (1)。

## 4. 实际有向输出与解析分支

全闭域上得到以下安全下界（严格松于 JSON 的向外端点）：

| 量 | 严格下界 |
|---|---:|
| $\operatorname{Re}Q$ | $.94248569$ |
| $\operatorname{Re}S$ | $.64513410$ |
| $\operatorname{Re}G$ | $.91127224$ |
| $\operatorname{Re}J$ | $.92958433$ |

四者都落在右半平面，因而采用在正实轴为实值的右半平面 Log，
得到唯一与实轴正平方根一致的周期解析分支。定义

$$
g_*=Qe^{-\frac12\operatorname{Log}S},\quad
h=Je^{-\frac12\operatorname{Log}G},\quad
\zeta=Je^{-\frac12(\operatorname{Log}G+\operatorname{Log}S)},
$$

$$
\ell=\partial_\theta\{\operatorname{Log}Q-
                  \tfrac12\operatorname{Log}S\}.
$$

实轴上 $u_z=F_z/|F|=rg_*$，故
$(\partial_\theta-\ell)u_z=0$；该公式准确贯穿腰圈。
全复条带上给

$$
.78870271<|g_*|<1.70358355,\qquad
|h|>.60953153,\quad |\zeta|>.51007583,\quad
|\ell|<2.90805284.
$$

其中 $|\ell|$ 用
$|Q_\theta|/\operatorname{Re}Q+
 a_+F_c\|T\|_+/\operatorname{Re}S$ 直接支付。
R59 的 $|n|>.28049754$ 同时适用。
任取较窄条带 $\sigma'<\sigma$，角导数还可由 Cauchy 给出
$\|\partial_\theta^j\ell\|_{\sigma'}\le
j!\,2.90805284/(\sigma-\sigma')^j$。
这不是径向或参数复化，也不提升原有径向样条正则性。

## 5. 有向实现、冻结输入与重放

全部多项式四则和非负求和向外计算；sinh/cosh 由准确有理 Taylor
指数区间及平方给出。平方根的 libm 值仅用于提出候选端点，随后
以准确 Fraction 平方比较并向对应方向移动到已证明端点。
源码重检三个输入的对象/参数/径向范围和通过标志，并用准确
Fraction 检查两个有限证书的径向区间确实连续拼满整个核心。
相位凸包的逐模式求和也逐字比较已冻结标量证书。

输入证书均在 `data/phase_ring_continuation/`：

- `type_fixed_step02_d5_affine_core_scalar_gate.json`：
  `d59cddb24b41f0d3862472785ad14da428b07b91944b065349c107486afb6c8c`。
- `type_fixed_step02_d5_affine_core_interval.json`：
  `278bf0e855f9b4a8bfebb37ff1564659c874f143b394bbb81503a228910dbf51`。
- `type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz`：
  `8602a50ee557309410c7f8a23a8b8602665b528d93dcb6f56dff1665f97929e2`。

新源 `scripts/fourfold_phase_affine_complex_chart.py` SHA256：
`0f0f27282edc5ef4baf29c3abfb3d67264216495d6e0821872a8da26e9f3cfde`。
新报告 `data/phase_ring_continuation/type_fixed_step02_d5_affine_complex_chart_1over64.json`
SHA256：`a1bfb82ee751e31a51a9997804ca2da68aaa4eb76b63081f1e4c0f9806e68a8f`。

从仓库根目录重放：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_complex_chart.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --scalar-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_affine_core_scalar_gate.json \
  --core-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_affine_core_interval.json \
  --strip-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz \
  --out /tmp/visible-D5-affine-complex-chart.json
```

这组界允许在整实际核心固定 $\nu,h,\zeta,g_*,\ell$ 的复角分支；
它不替代 R60 的 dense 残差、变分范数和 Wiener 尾，也不自行
支付正帽、全频逆或闭合可见精确弯曲族。
