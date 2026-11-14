# R1：二模凸核心的精确大相位差及闭图传递条件

2026-11-10，visible-larger-astra-20261110 / geometric_amplification。

**状态：下述核心曲线、平坦环带、凸性优化和条件传递均已证明；完整闭曲面尚未构造。** 本文不是本题完成解。它给实际数值延拓一个比纯 `cos(2φ)` 更大的初始形状，并明确闭合后需要验证的几何不等式。

## 1. 精确核心及结论

固定

$$
0<a<\frac{\sqrt2}{3},\qquad c=\frac{a}{10\sqrt2},\qquad
h(\phi)=1+a\cos(2\phi)-c\cos(4\phi).
$$

以 $e_r=(\cos\phi,\sin\phi)$、$e_\phi=(-\sin\phi,\cos\phi)$ 定义

$$
\gamma(\phi)=h(\phi)e_r+h'(\phi)e_\phi.
$$

则它是一条 $C^\infty$ 严格凸、中心对称且关于两坐标轴对称的闭曲线，周长恰为 $2\pi$。记其所围凸体为 $K$，有：

$$
\rho_{\min}=1-\frac{3a}{\sqrt2},\qquad
\rho_{\max}=1+3a+\frac{3a}{2\sqrt2},
$$

$$
A:=\max|\gamma|=1+a-c,\qquad
B:=\min|\gamma|=1-a-c,\qquad \operatorname{diam}K=2A,
$$

$$
\boxed{d_H(\partial K,R_{\pi/2}\partial K)=2a.}
$$

平面曲线作为 $\mathbb R^2$ 或 $\mathbb R^3$ 中的集合，其 reach 恰为 $\rho_{\min}$。这不是未来闭曲面的 reach 声明。

例如 $a=19/50=0.38$ 时：

| 量 | 值（小数仅说明，精确式在上方） |
|---|---:|
| $c$ | $0.0268700576851\ldots$ |
| 相位 Hausdorff 差 $2a$ | $0.76$ |
| 最大核心半径 $A$ | $1.3531299423149\ldots$ |
| 最小核心半径 $B$ | $0.5931299423149\ldots$ |
| 最小曲率半径 $\rho_{\min}$ | $0.1938982694473\ldots$ |
| 最大曲率半径 $\rho_{\max}$ | $2.5430508652763\ldots$ |

若完整闭图随后做到 $D\le19/5=3.8$，并满足第 4 节的见证条件，则 $\delta_{\rm hold}/D\ge0.2$。核心所允许的曲率半径比 $0.03D=0.114$ 大；闭图其他各部分的曲率与全局法向管仍要验证。

## 2. 凸性、半径及 reach 的证明

直接求导得到

$$
\gamma'(\phi)=\rho(\phi)e_\phi,\qquad
\rho=h+h''=1-3a\cos2\phi+15c\cos4\phi.
$$

令 $x=\cos2\phi\in[-1,1]$，则

$$
\rho=1-15c-3ax+30cx^2.
$$

因 $c=a/(10\sqrt2)$，这条抛物线的顶点为 $x=1/\sqrt2$，最小值为 $1-3a/\sqrt2>0$；最大值在 $x=-1$，等于 $1+3a+15c$。曲率因此为 $1/\rho$，法向角严格转过 $2\pi$。也可直接把 $h$ 视作支撑函数：$h+h''>0$ 保证其包络为严格凸的光滑闭曲线，外法向正是 $e_r$。周长为 $\int_0^{2\pi}\rho\,d\phi=2\pi$。

在 $0<\phi<\pi/2$ 上，

$$
h'=-2\sin2\phi\,(a-4c\cos2\phi)<0,
$$

因为 $4c<a$。而

$$
\frac{d}{d\phi}|\gamma|^2=2h'\rho<0.
$$

故范数最大值在横轴端点，最小值在纵轴端点，分别为 $A=h(0)$ 与 $B=h(\pi/2)$。两种对称性来自 $h$ 的相应对称性。中心对称及 $|\gamma|\le A$ 给直径 $2A$，且 $(\pm A,0)$ 达到它。

为证明 reach，下界取任意 $0<r<\rho_{\min}$。对 $|t|<r$，平行曲线

$$
\gamma_t(\phi)=\gamma(\phi)+t e_r(\phi)
$$

的曲率半径为 $\rho+t>0$，支撑函数为 $h+t$，因此仍是严格凸的简单闭曲线。它们按 $t$ 严格嵌套：两参数相差 $u>0$ 时，外侧凸体是内侧凸体与半径 $u$ 圆盘的 Minkowski 和。法向管 $\gamma+t e_r$ 遂在 $|t|<r$ 单射。距曲线小于 $r$ 的任一点的最近点存在，最近线段垂直于切线；法向管单射保证最近点唯一。令 $r\uparrow\rho_{\min}$ 得 reach 下界。

反向上界可用最近点唯一性推出的滚动圆性质：若 reach 大于 $r$，每个内法线距离 $r$ 的球心对应唯一切点，其半径 $r$ 的开圆盘不与曲线相交。把曲线在切点写成弧长 Taylor 展开，则圆盘不交条件在二阶给 $\kappa\le1/r$。取曲率最大点，并令 $r$ 从 reach 下方趋近，得到 reach $\le1/\kappa_{\max}=\rho_{\min}$。嵌入到 $\mathbb R^3$ 后，最近点问题只取决于正交投影到原平面，故 reach 不变。

## 3. 相位差及最佳二模曲率预算

### 3.1 凸体边界的 Hausdorff 距离

对两个有内点的紧凸体 $K,L\subset\mathbb R^n$，

$$
d_H(\partial K,\partial L)=d_H(K,L)
=\max_{|u|=1}|h_K(u)-h_L(u)|.
$$

后一个等式由支撑超平面分离及 $K\subset L+\varepsilon\overline B$ 的等价条件证明。为核对第一个等式，令右端为 $\varepsilon$。若 $x\in\partial K$ 在 $L$ 外，其到 $L$ 的最近点在 $\partial L$，距离不超过 $\varepsilon$。若 $x$ 在 $L$ 内，取 $K$ 在 $x$ 的外支撑单位法向 $u$。从 $x$ 沿 $u$ 射线第一次离开 $L$ 的距离不超过

$$
h_L(u)-x\cdot u=h_L(u)-h_K(u)\le\varepsilon.
$$

故 $d(x,\partial L)\le\varepsilon$，交换 $K,L$ 同理。反向不等式由凸包运算不增 Hausdorff 距离得到。

旋转 $\pi/2$ 后的支撑函数为

$$
h_{R_{\pi/2}K}(\phi)=1-a\cos2\phi-c\cos4\phi.
$$

其与 $h$ 的差的绝对值最大为 $2a$，故边界 Hausdorff 距离恰为 $2a$。见证点可取旋转后核心的 $p=(0,A)$；原核心全部位于 $y\le B$，而 $q=(0,B)$ 在原核心上，所以 $d(p,\partial K)=A-B=2a$。

### 3.2 为什么选择 $c=a/(10\sqrt2)$

固定 $a>0$，在所有 $h=1+a\cos2\phi-c\cos4\phi$、$c\ge0$ 中优化最小曲率半径。

- 若 $0\le c\le a/20$，抛物线顶点在区间外，$\rho_{\min}=1-3a+15c$，随 $c$ 增大。
- 若 $c\ge a/20$，顶点在 $[-1,1]$，
  $$\rho_{\min}=1-15c-\frac{3a^2}{40c}.$$
  算术几何均值不等式给 $15c+3a^2/(40c)\ge3a/\sqrt2$，等号恰在 $c=a/(10\sqrt2)$。

在分界 $c=a/20$ 的值为 $1-9a/4<1-3a/\sqrt2$，所以以上选择是这一整个二模子族的全局最优。它将纯二频的 $\rho_{\min}=1-3a$ 改进到 $1-3a/\sqrt2$，同时相位差仍为 $2a$。

若预设完整图直径上界为 $D_*$，仅从核心的两项必要预算出发，

$$
2a\ge0.2D_*,\qquad 1-3a/\sqrt2\ge0.03D_*
$$

有非空解区间当且仅当

$$
\frac{D_*}{10}\le a\le \frac{\sqrt2}{3}(1-0.03D_*),
\qquad D_*\le\frac{100\sqrt2}{30+3\sqrt2}\approx4.129\ldots.
$$

这只是核心的可行区间；尾曲率、直径、真实闭合和见证条件不由它推出。

## 4. 把核心差传递到整个闭曲面

设某个完整初始闭曲面 $S\subset\mathbb R^3$ 包含本核心 $\partial K\times\{0\}$，活动区域在相位 $\pi/2$ 时的像确实包含 $p=(0,A,0)$。固定 $d=2a$。以下任何条件都足以保证

$$
d(p,S)=d,\qquad \delta_{\rm hold}\ge d.
$$

### 精确排除条件

对 $S$ 上每个点 $(x,y,z)$，若 $|z|<d$，要求

$$
\boxed{y\le A-\sqrt{d^2-z^2}.}
$$

则 $(A-y)^2+z^2\ge d^2$；若 $|z|\ge d$ 则距离下界自动成立。再加非负的 $x^2$，得 $|p-(x,y,z)|\ge d$。原核心点 $(0,B,0)$ 达到等号。

实际程序可对每个连续图块给 $y\le b_j$ 与 $|z|\ge z_j\ge0$，验证

$$
\bigl(\max\{A-b_j,0\}\bigr)^2+z_j^2\ge d^2.
$$

这是连续块证书的充分条件，有限节点采样只提供初筛。

### 更便于积分或 Taylor 估计的抛物线条件

若所有 $|z|\le d$ 的点满足

$$
\boxed{y\le B+\frac{z^2}{2d},}
$$

则 $A-y\ge d-z^2/(2d)\ge d/2$，从而

$$
(A-y)^2+z^2\ge d^2+\frac{z^4}{4d^2}\ge d^2.
$$

所以这也是充分条件。平坦核心入口若 $F_s=e_z$、$F_{ss}=0$，则横向变化为高阶，而 $z=s+o(s)$；只要有有效的三阶或积分余项，抛物线条件可在一个实际邻域验证。**仅有有限阶 jet 相同并不能代替对整个邻域的余项界。**

### 容易接入的平坦环带条件

用精确柱面 $\gamma\times[-\ell,\ell]$，其中 $\ell\ge d$。只要其余两侧的闭合部分分别全部位于 $z\ge\ell$、$z\le-\ell$，它们就不能降低核心见证距离。柱面自身始终满足 $y\le B$。这是简洁的充分构造条件，但加入长度会增加 $D$，不保证能达到本题比例。

## 5. 精确材料参数与全时相位

曲线的归一化弧长材料角为

$$
\theta(\phi)=\int_0^\phi\rho(u)\,du
=\phi-\frac{3a}{2}\sin2\phi+\frac{15c}{4}\sin4\phi.
$$

其导数为严格正的 $\rho$，并满足 $\theta(\phi+2\pi)=\theta(\phi)+2\pi$，故有光滑逆 $\phi(\theta)$。令 $\Gamma(\theta)=\gamma(\phi(\theta))$，则 $|\Gamma_\theta|=1$。于是

$$
F(s,\theta)=(\Gamma(\theta),s),\qquad
F_\alpha(s,\theta)=(R_\alpha\Gamma(\theta-\alpha),s)
$$

是同一平坦度量 $ds^2+d\theta^2$ 的精确光滑等距环带族，且 $\alpha\mapsto F_\alpha$ 在每个紧环带的 $C^k$ 拓扑连续。

由于 $\Gamma(\theta+\pi)=-\Gamma(\theta)$，该族的像以 $\pi$ 为周期，故参数 $\alpha\in[0,\pi]$ 覆盖整个相位周期，包含最大核心见证相位 $\pi/2$。当前 flat17 的三重对称族已经覆盖其整个 $[0,2\pi/3]$ 周期；单纯延长旧时间区间不能带来新像。

要把这里的环带族变成闭曲面族，必须真实求得相同旋转内蕴度量的过渡带，使两端完整 Cartesian 二阶 jet 与轴对称固定帽相容；既有二模核心的支撑、凸性或局部 Frenet 解都不能代替这一步。全局 reach 同样需要整个闭图的数据。固定帽上加入非旋转标记可沿已有 R16/R17 的矩方法证明 $\delta_E>0$，但不能只凭“有标记”而省略它与活动主体的非全等论证。

## 6. 生成器与来源

`computations/geometric-two-mode-core.py` 直接实现以上公式；默认 $a=19/50$、$D_*=19/5$，输出精确有理的 $\sqrt2$ 包围与各个几何量的有理包围，并可选输出开柱面 OBJ 供初猜或查看。程序不把开柱面标成完成解，不产生 PDF。

已有闭图的相位拼接参考 `topics/visible-flexible-closed-surface/results/R17-exact-finite-visible-closed-geometry.md` 与 R21。只读来源树在读取时的 HEAD 为 `6c42f984639961ee13f08f0e259daedd0a2439fd`；本证明中的核心公式独立于其数值数据。读取文件 SHA256：

- R17：`d7ad70cfb98d552ce0832555c230b644e49a21cd5cef2ae16a291013ad66e725`。
- R21：`3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c`。
- 现有 `notes/fixed_metric_mode3_core.py`：`a529904e265ddc95635c6c6601ea173eb0e1383a75e458d3eaee024fe7078ead`；它已接受任意整数 `base_mode≥2`，上述二模核心是其中 `base_mode=2, coefficients=(a,-c)` 的一个选择。
