# 实际 binary 曲率的 R54/R67 条件比例预算

本条仅支付 **R54 的精确 $1/5$ 与实际 R53 核心字面 binary64 `.2` 之间的参数定义差异**。它代入既有 [R54](../results/R54-transverse-held-arc-and-short-cylinder-window.md) 的圆弧弦长/整像握持公式和 [R67](../results/R67-universal-threefold-marker-and-euclidean-noncongruence.md) 的条件直径/reach 预算，不重证这两项结果，也不构造或假报一个 $\lambda=1$ 场。

已检查此前 R54、R67、实际 true-core 参数语义及本题 notes：此前已有实际 $k$ 的 binary 定义，但未见下面这组针对该 $k$ 的 R54 比例舍入支付。实际定义见 [true-core 证书说明](2026-11-20-m24-r53-true-core-jet-certificate.md)，其中周期仍为真实 $2\pi/3$，参数采用字面 binary 实数。

## 1. 精确输入及保护材料窗

取

$$
k=\frac{3602879701896397}{18014398509481984},\qquad
k-\frac15=\frac{1}{90071992547409920}>0.
$$

因此不能把已登记的 $k=1/5$ 数值下界直接改标签。这里使用实际 $k$、$S=1/2$、$w_H=27/50$、$\alpha_1=9/20$。保持 R54 原材料区间

$$
I=L+[-9/200,99/200],\qquad L=\pi/3.
$$

整个相位扫窗仍为

$$
\bigcup_{0\le\alpha\le9/20}(I-\alpha)
=L+[-99/200,99/200],
$$

距半宽 $S$ 的两端各有准确 $1/200$ 余量；这部分不依赖曲率恰为 $1/5$。任意允许的正柱长仍使 $H$ 有二维内点。

## 2. 只用明确有理夹逼

沿 R54 使用经典界

$$3<\pi<22/7,\qquad 433/250<\sqrt3<7/4.$$

平方核对为 $(433/250)^2=187489/62500<3$ 和 $(7/4)^2=49/16>3$。对下文两个准确有理数 $0<x<1$，使用

$$x-x^3/6<\sin x<x.$$

没有调用浮点 `sin`、`sqrt` 或 `pi`。程序全部比较用 Python `Fraction`；输出小数仅供阅读。

R54 的核心中心公式给

$$
|O|>\frac1k-\frac{2\pi}{3\sqrt3}
>\frac1k-\frac{2(22/7)}{3(433/250)}>0.
$$

于是圆弧水平弦与三重整像握持下界分别满足

$$
\begin{aligned}
\operatorname{diam}H
&\ge\frac2k\sin\left(\frac{27k}{100}\right)\\
&>\frac2k\left[\frac{27k}{100}-\frac16\left(\frac{27k}{100}\right)^3\right]
>\frac{5397}{10000},
\end{aligned}
$$

以及

$$
\begin{aligned}
\delta_{\rm hold}
&\ge\sqrt3|O|\sin\left(\frac{9k}{40}\right)\\
&>\left(\frac{433}{250k}-\frac{44}{21}\right)
\left[\frac{9k}{40}-\frac16\left(\frac{9k}{40}\right)^3\right]
>\frac{2953}{10000}.
\end{aligned}
$$

第一式的有理下界约为 $0.53973756$，对所取阈值的严格余量约 $3.756\times10^{-5}$；第二式的有理下界约 $0.29531458339285716$，余量约 $1.4583392857\times10^{-5}$。这些小数不参与判断。完整准确分子/分母、正系数、正 sine 下界和严格 margin 见[实际执行 JSON](2026-11-28-analytic-binary-core-curvature-held-budget.json)。

这里仍是 R54 的 **完整紧像 Hausdorff 下界**，没有换成某个材料点位移。

## 3. 与同一个完整直径/reach 预算的接口

条件仍是实际整图已经支付 R67 所需的完整初始直径和全时 reach：

$$
D\le\frac{67251}{25000}=2.69004,\qquad
\operatorname{reach}(F_t(M))\ge\frac{10}{123}\quad(0\le t\le1).
$$

由上节的较小明确阈值，直接得到

| 比例 | 准确下界 | 对 README 阈值的准确正余量 |
|---|---:|---:|
| $\operatorname{diam}H/D$ | $>8995/44834$ | $141/224170$ 高于 $1/5$ |
| $\delta_{\rm hold}/D$ | $>14765/134502$ | $3287/336255$ 高于 $1/10$ |
| $\min_t\operatorname{reach}(F_t(M))/D$ | $\ge250000/8271873$ | $184381/827187300$ 高于 $3/100$ |

显示小数依次为约 $0.20062898693$、$0.10977531933$、$0.03022290115$。D 的前提、全时 reach 的前提以及柱和帽的成本并没有在本条重新认证，也没有从导出的有限网格推得。

## 4. 同一曲率用于握持规范和非圆性

真实握持规范仍应使用这个实际 $k$ 和真实弧心：

$$F_\alpha=R_{-(1-k)\alpha}G_\alpha+O-R_{k\alpha}O.$$

R54 的局部圆弧代数对任何正 $k$ 成立，故这里不需把 $k$ 替换成 $1/5$。浮点评价的弧心或旋转矩阵不成为新的数学定义常数。

同时 $0<k<1$ 且 $k\ne1$ 已准确核对。若未来真实 $\lambda=1$ 核心确实单位材料速度、总长 $2\pi$ 并有该保护弧，它不可能是整圆：该总长的正曲率圆必须曲率恒为 $1$。因此 R67 所用非圆核心条件仍可条件性接入；这不声称已有这样的完整核心/BVP 返回，也不提供新的 $\delta_E$ 数值。

## 5. 实际执行和未付责任

独立脚本 `scripts/resume_20261128/analytic/check_binary_curvature_held_budget.py` 只执行上述 Fraction 算术，已真实 exit 0；没有 BVP、尾、网格、连续几何或 metric 计算。它绑定 R54/R67 与实际 true-core 参数语义说明的 SHA。所有 `lambda_one_field_available_or_constructed`、`new_continuous_metric_or_geometry_certificate`、`completion_criteria_passed` 均为 false。

尚待真实 $\lambda=1$ 原完整场、完整非线性全高度尾、公共 Cartesian 二jet、全图几何前提和同一问题精化。本条只消除参数定义的这一个小缺口，不能作为课题完成。
