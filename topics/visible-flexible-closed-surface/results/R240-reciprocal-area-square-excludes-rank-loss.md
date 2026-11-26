# R240：倒面积平方的连续有限成本排除秩亏

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本条说明当前新增面积防塌行的一项准确连续性质，并给出其完整固定 $g$ 的 J/JT。它不把当前有限求积成本提升为连续证书，不证明已得到准确等距族。

## 1. 正则图、固定目标及成本

设 $\Omega$ 是二维正则材料图的闭区域，例如紧环带 $[b,S]\times\mathbb S^1$。每个内部点有完整小圆盘；边界点有固定正开角的小扇形或半圆盘包含于 $\Omega$。紧光滑边界的环带满足此条件，角变量接缝使用圆周上的局部坐标处理。

设固定目标度量为

$$
g=ds^2+a(s)^2du^2,\qquad a\in C^1,\quad a>0,
$$

并令 $X:\Omega\to\mathbb R^3$ 为 $C^2$ 映射，边界处按通常的单侧 $C^2$ 图理解。定义

$$
w=X_s\times X_u,\qquad
\sigma=\frac{|w|}{a},\qquad
\eta=\sigma^2.
$$

$\sigma$ 是实际面积元相对于目标面积元的比值；$\eta$ 是目标归一化 Gram 行列式。两者不能混称。取固定常数 $0<\sigma_*\le1$，定义

$$
\Phi(\sigma)=\left(\frac{\sigma_*}{\sigma}-1\right)_+
\quad(\sigma>0),\qquad \Phi(0)=+\infty.
$$

设密度 $\omega$ 非负可测，且每个拟检查点附近存在 $\omega_0>0$，使 $\omega\ge\omega_0$ 几乎处处。正的连续目标密度是这一条件的特例。准确连续成本为

$$
\mathcal B(X)=\int_\Omega \omega(s,u)\Phi(\sigma(s,u))^2\,ds\,du.
\tag{1}
$$

这里的密度必须是固定正目标密度；不能换成在秩亏处一起消失的实际曲面面积密度而沿用下文结论。

**定理。** 若 (1) 有限，则 $w$ 在上述正则图的所有点均非零。若图紧，则存在 $\sigma_{\min}>0$；其数值不能只从当前离散样本推断。

## 2. 为什么 $C^2$ 给出所需 Lipschitz 性

在任意紧小图中，$X_s,X_u$ 为 $C^1$，所以 $w$ 为 $C^1$。模长映射满足

$$
\big||w(p)|-|w(q)|\big|\le|w(p)-w(q)|.
$$

因为 $a$ 为 $C^1$ 且在小图中有严格正下界，$|w|/a$ 局部 Lipschitz；这在 $w=0$ 处也成立，不需给单位法向作不合法延拓。

例如若该小图中 $a\ge a_0>0$，且各 $M$ 是对应位置导数范数的真实上界，则可取

$$
\begin{aligned}
L_s&=\frac{M_uM_{ss}+M_sM_{su}}{a_0}
+\frac{\|a_s\|_\infty M_sM_u}{a_0^2},\\
L_u&=\frac{M_uM_{su}+M_sM_{uu}}{a_0},\qquad
L=\sqrt{L_s^2+L_u^2}.
\end{aligned}
\tag{2}
$$

在内部小圆盘或边界的局部凸扇形上，$L$ 控制 $\sigma$ 的 Lipschitz 常数。该估计只需 $X$ 的前两阶导数及固定 $a$；$\sigma$ 本身不必在零点可微。本条没有声称已对当前完整数值场支付 (2) 的具体连续数值。

## 3. 零点必使准确二维积分发散

反设 $\sigma(p)=0$。在 $p$ 附近选取上述正开角扇形，开角记为 $\alpha>0$；内部可取 $\alpha=2\pi$，光滑边界可用半圆或更小固定扇形。

若相应 Lipschitz 常数 $L=0$，则 $\sigma$ 在此邻域恒等于零，$\Phi^2=+\infty$ 在正测度集合上成立，故 (1) 立即发散。

否则 $L>0$，在距 $p$ 为 $r$ 处有 $\sigma\le Lr$。取半径 $r_0>0$ 足够小，使 $Lr_0\le\sigma_*/2$ 且 $\omega\ge\omega_0$。对 $0<r<r_0$，若 $\sigma>0$ 则

$$
\Phi(\sigma)=\frac{\sigma_*}{\sigma}-1
\ge\frac{\sigma_*}{2\sigma}
\ge\frac{\sigma_*}{2Lr}.
$$

若某些点仍有 $\sigma=0$，同一个下界按 $+\infty$ 的定义继续成立。因此

$$
\mathcal B(X)
\ge \frac{\omega_0\sigma_*^2}{4L^2}
\int_0^{r_0}\int_0^\alpha r^{-2}\,r\,d\theta\,dr
=+\infty,
$$

矛盾。故图内所有点非退化。紧图上的正连续 $\sigma$ 取得严格正最小值。证明不假设零点孤立，也不假设空间曲面凸或某种反射对称。

若某端口已由完整端函数证明非退化，可直接消费该端口结论；否则上述半圆/扇形证明同时处理正规窗口端部。坐标极点 $a=0$ 不在本定理的正则图假设内，不能将极坐标面积因子的消失判成曲面秩亏；必须改用真正正则坐标图再应用此结论。

这也说明选择平方倒面积项的具体原因：若只用 $\log^2\sigma$，二维模型 $\sigma\sim r$ 的局部积分为 $\int_0^{r_0}r\log^2r\,dr<\infty$，不能用同一论证排除零点。

## 4. 近等距时新增项自动消失

令 $G_X=(DX)^{\mathsf T}DX$，并用固定目标度量归一化：

$$
H=g^{-1/2}G_Xg^{-1/2}.
$$

若在某点 $\|H-I\|_{\rm op}\le\varepsilon<1$，则两个特征值均不小于 $1-\varepsilon$，所以

$$
\sigma=\sqrt{\det H}\ge1-\varepsilon.
$$

当前取 $\sigma_*=1/2$。当谱度量误差不超过 $1/2$ 时，$\sigma\ge1/2$，新增残差恰为零；准确等距时更有 $\sigma=1$。因此该项不删去准确等距解，也不更改本题等距目标。

反向推论不成立：例如 $H=\operatorname{diag}(t,t^{-1})$ 对所有 $t>0$ 都给 $\sigma=1$，但 $t$ 很小时度量误差很大。所以完整原度量行必须保留。面积正性也不推出曲率门槛、嵌入、非局部 reach 或 held。

## 5. 固定 g 的完整微分及伴随

在 $w\ne0$ 的实际点上令 $N=w/|w|$。对任何完整位置扰动 $\delta X$，且固定 $a$，有

$$
\delta\sigma=
\frac{(X_u\times N)\cdot\delta X_s+(N\times X_s)\cdot\delta X_u}{a}.
\tag{3}
$$

取一个明示的非负固定求积权重 $\omega_i$，残差 $r_i=\sqrt{\omega_i}\Phi(\sigma_i)$。活动区 $0<\sigma_i<\sigma_*$ 的微分为

$$
\delta r_i=-\sqrt{\omega_i}\frac{\sigma_*}{\sigma_i^2}\,\delta\sigma_i.
\tag{4}
$$

非活动区 $\sigma_i>\sigma_*$ 微分为零。等号 $\sigma_i=\sigma_*$ 处采用固定的零广义导数约定；残差连续分段光滑，平方目标在该处为 $C^1$，因为残差本身为零。值和所有 J/JT 都使用同一活动集约定。

若 $c_i$ 为该残差的余切，令 $\mu_i=-c_i\sqrt{\omega_i}\sigma_*/(a_i\sigma_i^2)$（只在活动区），则位置两 jet 的伴随增量为

$$
(\delta X_s)^*\mathrel{+}=\mu_i(X_u\times N),\qquad
(\delta X_u)^*\mathrel{+}=\mu_i(N\times X_s),
$$

其他四个位置 jets 的新增伴随为零。然后按原完整径向和角向基的伴随传播至所有 Cartesian 列。没有冻结实际法向、投影背景或丢弃原来的任一行。

若目标 $a$ 本身也是待变化的设计变量，则 (3) 还需增加 $-\sigma\,\delta a/a$；本条实现对应的是已经冻结 $g$ 的 Cartesian 阶段，不适用于把该项省略的 $g$ 设计求导。

## 6. 与当前实际离散工作的严格区别

当前实现 `6a65-geometry-area-ratio-barrier.py` 的数学行即 (3)/(4)，$\sigma_*=.5$，新增权重沿原完整 metric 求积权重。原 13 行和全部 5292 列保持，新的 14 行目标另立真实基线，并分别报告原 13 行成本和面积成本。全部实际试步要求每个已计算点的 $|w|>0$，否则明确拒绝该数值域。

有限个求积点上的有限成本或正 $\sigma_i$ 不能证明准确积分 (1) 有限，也不能排除格间秩亏。当前代码中的 `continuousAreaLowerBoundCertified=false` 保持。即使所有采样点的新增行已经为零，也仍需对完整连续场支付严格正面积；本定理仅给出了准确连续积分一旦被证明有限时的逻辑后果。

因此本条是已有实际 14 行求解的数学依据，不是本题完成证书。仍须继续完整后段求解、固定前缀的准确修正、全域几何及同一 $g$ 的跨时间族。
