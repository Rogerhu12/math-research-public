# R7. 一个核心 Hausdorff 见证的入口加速度门槛

作者：visible-larger-astra-20261110 / geometric_amplification，2026-11-10。

**状态：已证明。** 本文给出平面凸核心沿竖直方向出发时，一个指定外法向见证点的局部遮挡判据。证明只用 $C^2$ 正则性和准确的等距恒等式。这个判据不构成整个 Hausdorff 距离的上界，不排除其他见证，不证明某一候选可闭合；严格低于门槛也只保证一个充分短的入口段。

## 1. 假设与准确的入口二 jet

设 $a\in C^2([0,S])$，$a_0=a(0)>0$。设

$$
F:[0,S]\times S^1\longrightarrow\mathbb R^3
$$

为 $C^2$ 等距浸入，满足

$$
|F_s|^2=1,\qquad F_s\cdot F_\theta=0,
\qquad |F_\theta|^2=a(s)^2. \tag{1}
$$

入口数据为

$$
F(0,\theta)=\gamma(\theta)\in\{z=0\},
\qquad F_s(0,\theta)=e_z, \tag{2}
$$

其中 $\gamma$ 是正向、严格凸的 $C^2$ 平面闭曲线，曲率处处为正。记 $n(\theta)$ 为向外单位法向，$\rho(\theta)>0$ 为曲率半径。由 (1)，$|\gamma_\theta|=a_0$，故

$$
\gamma_{\theta\theta}=-\frac{a_0^2}{\rho}\,n. \tag{3}
$$

**引理 1.** 上述假设强制 $a'(0)=0$。令 $k_0=a''(0)$，则

$$
\boxed{F_{ss}(0,\theta)=\frac{k_0\rho(\theta)}{a_0}\,n(\theta).} \tag{4}
$$

**证明。** 对 (2) 作角导数，得到 $F_{s\theta}(0,\theta)=0$。对 (1) 的最后一个恒等式作一次 $s$ 导数，有

$$
F_{s\theta}\cdot F_\theta=aa'. \tag{5}
$$

在入口代入即得 $a'(0)=0$。令 $W(\theta)=F_{ss}(0,\theta)$。对前两个等距恒等式各作一次 $s$ 导数，再代入入口数据，得到

$$
W\cdot e_z=0,\qquad W\cdot\gamma_\theta=0.
$$

因此存在连续实函数 $w$，使 $W=wn$。接下来确定 $w$；这一步不假定三阶混合导数存在。

由 $C^2$ 正则性及 $F_{s\theta}(0,\theta)=0$，一致地有

$$
F_\theta(s,\theta)-\gamma_\theta(\theta)
=\int_0^s F_{s\theta}(t,\theta)\,dt=o(s),
\qquad F_{s\theta}(s,\theta)=o(1).
$$

所以 (5) 给出一致极限

$$
\frac1sF_{s\theta}(s,\theta)\cdot\gamma_\theta(\theta)
=\frac{a(s)a'(s)}s
 -\frac{F_{s\theta}(s,\theta)\cdot
 (F_\theta(s,\theta)-\gamma_\theta(\theta))}s
\longrightarrow a_0k_0. \tag{6}
$$

取任意光滑周期测试函数 $\eta$，对 (6) 左边分部积分。因为 $e_z\cdot\gamma_\theta=0$，且
$(F_s(s,\theta)-e_z)/s\to W(\theta)$ 一致，所以

$$
\begin{aligned}
\lim_{s\downarrow0}\int_{S^1}\eta
 \frac{F_{s\theta}(s,\theta)\cdot\gamma_\theta}s\,d\theta
&=-\int_{S^1}W\cdot
 (\eta'\gamma_\theta+\eta\gamma_{\theta\theta})\,d\theta\\
&=\int_{S^1}\eta\,\frac{a_0^2w}{\rho}\,d\theta.
\end{aligned}
$$

与 (6) 比较，连续函数 $a_0^2w/\rho-a_0k_0$ 对所有测试函数的积分为零。因此它处处为零，得到 (4)。证毕。

这也加强了 [R6](R6-mirror-seam-nonzero-acceleration.md) 中从经典 Frenet 流直接求出的同一公式：这里并不需要对角二 jet 再作径向微分。

## 2. 指定外法向见证的局部门槛

固定入口点 $q=\gamma(\theta_*)$、$\rho_* =\rho(\theta_*)$，并取

$$
p=q+d\,n(\theta_*),\qquad d>0. \tag{7}
$$

凸性保证 $q$ 是核心上距 $p$ 最近的点，而且

$$
\operatorname{dist}(p,\gamma(S^1))=d. \tag{8}
$$

事实上，对任意 $x\in\gamma(S^1)$，支撑线不等式给出
$n(\theta_*)\cdot(x-q)\le0$，于是
$|p-x|\ge n(\theta_*)\cdot(p-x)\ge d$；等号要求 $x=q$。

**定理 2.** 在上述假设下：

1. 若 $k_0>a_0/(d\rho_*)$，则任意充分短的正入口段已经遮挡该完整见证：对所有充分小的 $s>0$，

   $$
   |F(s,\theta_*)-p|<d.
   $$

   因此每个含有这样一个入口段的整张曲面 $\Sigma$ 都有
   $\operatorname{dist}(p,\Sigma)<d$。
2. 若 $k_0<a_0/(d\rho_*)$，则存在 $\varepsilon>0$，使

   $$
   \operatorname{dist}\bigl(p,F([0,\varepsilon]\times S^1)\bigr)=d,
   $$

   并且该短入口段与闭球 $\overline B(p,d)$ 只在入口点 $q$ 接触。
3. 若 $k_0=a_0/(d\rho_*)$，二阶计算不能决定是否遮挡；仍须检查更高阶信息或直接的球外条件。

因此要由这个指定的 $p$ 保留全差值 $d$，必要条件是

$$
\boxed{a''(0)\le\frac{a(0)}{d\rho_*}.} \tag{9}
$$

**证明。** 令

$$
Q(s,\theta)=|F(s,\theta)-p|^2.
$$

在 $(0,\theta_*)$，有 $Q=d^2$，且 $Q_s=Q_\theta=0$。由引理 1，

$$
\boxed{Q_{ss}(0,\theta_*)
=2\left(1-\frac{d k_0\rho_*}{a_0}\right).} \tag{10}
$$

具体地，$Q_{ss}=2|F_s|^2+2(F-p)\cdot F_{ss}$，而入口 $F-p=-dn$、$F_s=e_z$。所以在固定的材料点上，$C^2$ Taylor 公式给出

$$
Q(s,\theta_*)=d^2+
\left(1-\frac{d k_0\rho_*}{a_0}\right)s^2+o(s^2). \tag{11}
$$

系数为负时立刻得到第 1 条。

为证明第 2 条，不能只检查这一条材料曲线；还要排除邻近角度。由 (2)–(3)，入口处的另两个二阶量为

$$
Q_{s\theta}=0,\qquad
Q_{\theta\theta}=2a_0^2\left(1+\frac d{\rho_*}\right)>0. \tag{12}
$$

若 (10) 严格为正，$(s,\theta)$ 二变量 Hessian 在该点正定。由连续性和二阶 Taylor 公式，在一个半邻域 $s\ge0$ 中存在 $c>0$，使

$$
Q(s,\theta)-d^2\ge c\bigl(s^2+|\theta-\theta_*|^2\bigr), \tag{13}
$$

其中角度取包含 $\theta_*$ 的局部坐标。另一方面，(8) 的最近点唯一。去掉这个角邻域后，紧性给出入口核心与球的严格正间隔；由 $F$ 连续性，这个间隔在某个共同的短径向区间内保持为正。与 (13) 合并，即得整个短入口段只在 $q$ 接触该闭球。等号情形下 (11) 的二阶项消失，因而不能用本文信息判定。证毕。

## 3. 两模强核心的数值门槛

取 [R1](R1-two-mode-core-phase-gap.md) 的核心

$$
h(\varphi)=1+\epsilon\cos2\varphi
 -\frac{\epsilon}{10\sqrt2}\cos4\varphi,
\qquad 0<\epsilon<\frac{\sqrt2}{3}. \tag{14}
$$

这里 $a_0=1$，令

$$
A=1+\epsilon-\frac{\epsilon}{10\sqrt2},\qquad
B=1-\epsilon-\frac{\epsilon}{10\sqrt2}.
$$

短轴核心点为 $q=(0,B,0)$，向外法向为 $e_y$；长轴点旋转 $\pi/2$ 后给出

$$
p=(0,A,0),\qquad d=A-B=2\epsilon.
$$

在 $q$ 处

$$
\rho_* =\rho_{\max}
=1+\left(3+\frac3{2\sqrt2}\right)\epsilon.
$$

由 (9)，这个相位见证保住核心差值 $2\epsilon$ 的入口必要条件为

$$
\boxed{k_0\le
\frac1{2\epsilon\left[1+(3+3/(2\sqrt2))\epsilon\right]}.} \tag{15}
$$

以下小数仅是精确公式 (15) 的近似显示。

| 核心参数 $\epsilon$ | $d$ | $\rho_*$ | 入口门槛 $1/(d\rho_*)$ |
|---|---:|---:|---:|
| $.38$ | $.76$ | $2.54305086527633$ | $.517405881121153$ |
| $.41$ | $.82$ | $2.66487067042973$ | $.457625283153159$ |

因此，对 $\epsilon=.38$，初始加速度 $k_0=.45$ 严格保留一个短入口段中的完整见证；$k_0=1.555\ldots$ 则必定立即损失这个完整见证。后者仍可能有其他相位或其他曲面点给出较大 Hausdorff 距离，本文没有估计其上界。增大核心幅度同时会降低这个入口门槛，不能只按核心差值增大就断言整图变化改善。

## 4. 从入口门槛到后续可计算护栏

对于给定候选，保护该见证的准确条件始终是

$$
|F(s,\theta)-p|^2\ge d^2
\quad\hbox{对所有 }(s,\theta). \tag{16}
$$

一个便于 profile 设计、但更强的充分条件是：对所有满足 $|z|<d$ 的曲面点 $(x,y,z)$，有

$$
y\le A-\sqrt{d^2-z^2}. \tag{17}
$$

此时 $(A-y)^2+z^2\ge d^2$，再加上 $x^2\ge0$ 即得 (16)；$|z|\ge d$ 的点自动满足 (16)。更简单但更保守的充分条件为

$$
y\le B+\frac{z^2}{2d},\qquad |z|<d, \tag{18}
$$

因为 $\sqrt{1-u}\le1-u/2$ 对 $u\in[0,1]$ 成立。

若对称性使短轴材料曲线写成 $(0,Y(s),Z(s))$，则这条曲线上的球外余量和其导数为

$$
E(s)=(A-Y(s))^2+Z(s)^2-d^2,
\qquad
E'(s)=-2(A-Y)Y'+2ZZ'. \tag{19}
$$

在 $Y<A$ 的区间内，要求 $Y'\le ZZ'/(A-Y)$ 是保证 $E$ 不下降的充分护栏。但它只控制该轴上的材料曲线，必须另外检查所有角度才能推出 (16)。初始 (19) 的二阶预算正是 (10)；这解释了先保持较小加速度、待高度建立以后再加速的设计方向，并未证明任何指定的后续控制必然成功。

即使整个带边前缀满足 (16)，闭合腿、端帽及握持区也仍须保持该球外条件，并分别完成同一度量的闭合、全族嵌入和 reach 检查。本文只提供一个可以准确检验的局部条件与后续护栏。
