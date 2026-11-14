# 非径向主符号核查：奇分母返回图和反周期传输

2026-11-12，visible-flex-exact-nearby / independent-audit。

**范围。** R25 已把真实径向背景的全四重逆改为 $17/n$，R28 已把
同尾、保作用量的真实径向均值改变归一为无频率的 Schwarzian 势。
本文研究剩余角依赖主符号的一条可能路线：能否仅从返回图接近奇分母
旋转，利用转折处的半整数相位，得到 $I+T$ 的有限损失逆。

下文给出的传输算子结论是完整证明。它们不是对本题实际曲面返回图的
已完成分析，也不是本题主目标的不存在性结论。

## 1. 奇阶周期传输的准确充分条件

对任一有界算子 $T$ 和奇数 $q$，有恒等式
$$
(I+T)\sum_{j=0}^{q-1}(-T)^j=I+T^q.
\tag{1.1}
$$
因此 $T^q=I$ 时，
$$
(I+T)^{-1}=\frac12\sum_{j=0}^{q-1}(-T)^j.
\tag{1.2}
$$
对圆周微分同胚 $R$，纯复合算子 $Tu=u\circ R$ 在 $R^q=\mathrm{id}$
时满足该条件；半密度算子
$$
T_Ru(\theta)=\sqrt{R'(\theta)}\,u(R(\theta))
\tag{1.3}
$$
也如此，因为沿一整周期的导数乘积是 $(R^q)'=1$。
有限次光滑复合在每个 Sobolev 阶上有界，故 (1.2) 给真正的同阶逆。

条件 $R^q=\mathrm{id}$ 是充分条件，不是必要条件。第 4 节给
非周期返回图仍有有限损失逆的明确情形。
也可直接使用 (1.1)：若在所用函数空间中实际付清
$\|T^q-I\|<2$，则 $I+T^q$ 可逆，再以 (1.1) 构造 $I+T$ 的逆。
但是微分同胚的 $C^\infty$ 接近不自动给这个算子范数界。

## 2. 任意接近奇分母旋转、具有完全相同旋转数的反例

固定互素 $p,q$，$q$ 为奇数；可以取本课题的 $p=11,q=89$。
圆周角记为 $\theta\in\mathbb R/(2\pi\mathbb Z)$。
令
$$
r(\theta)=\theta+\frac{2\pi p}{q},\qquad
v(\theta)=\sin(q\theta)\,\partial_\theta,
$$
$\Phi_\varepsilon$ 为 $v$ 的时间 $\varepsilon>0$ 流，并定义
$$
R_\varepsilon=r\circ\Phi_\varepsilon.
\tag{2.1}
$$
向量场的 $2\pi/q$ 周期性给 $r\Phi_\varepsilon=\Phi_\varepsilon r$。
于是
$$
R_\varepsilon^q=\Phi_{q\varepsilon},\qquad
R_\varepsilon\longrightarrow r
\quad\text{于每个固定 }C^k\text{ 拓扑}.
\tag{2.2}
$$
$R_\varepsilon$ 的旋转数准确等于 $p/q$：取向量场的任一零点，它在
$R_\varepsilon$ 下的 $q$ 步提升位移恰为 $2\pi p$。这是真正有该旋转
数的周期轨道；保向圆周同胚的旋转数因而为 $p/q$。
只要 $\varepsilon>0$，流在两个相邻零点之间非平凡，故
$R_\varepsilon^q\ne\mathrm{id}$。

考虑旋转平均
$$
Au=\frac1q\sum_{j=0}^{q-1}u\circ r^j.
$$
它与 $R_\varepsilon$ 的纯复合算子交换；由于 $R_\varepsilon'$ 也有
$2\pi/q$ 周期，它同样与 (1.3) 的半密度算子交换。
若源 $g$ 对 $r$ 不变，而完整方程有解，则 $Au$ 仍为解且对 $r$ 不变。
所以只需研究这个不变子空间。

在一个相邻固定点之间的区间 $0<\theta<\pi/q$，用
$$
t=\frac1q\log\tan\frac{q\theta}{2},\qquad
\theta(t)=\frac2q\arctan(e^{qt}).
\tag{2.3}
$$
有
$$
\frac{dt}{d\theta}=\frac1{\sin(q\theta)},\qquad
\theta'(t)=\operatorname{sech}(qt),\qquad
\Phi_\varepsilon(\theta(t))=\theta(t+\varepsilon).
\tag{2.4}
$$
旋转不变函数在商圆上不受 $r$ 作用，因此真实传输就化为这一平移。

取非零非负 $G\in C_c^\infty((0,\varepsilon/3))$。
令 $g(\theta(t))=G(t)$，并在商圆其余部分置零，再按 $2\pi/q$ 周期
延拓。其支持远离固定点，所以得到真正 $C^\infty(S^1)$ 源。

### 2.1 纯复合方程一般没有连续解

若
$$
u+u\circ R_\varepsilon=g
\tag{2.5}
$$
有连续解，旋转平均后可写成
$$
U(t)+U(t+\varepsilon)=G(t).
\tag{2.6}
$$
选 $t_0\in(0,\varepsilon/3)$ 且 $G(t_0)>0$。
对整数 $k\ne0$，$G(t_0+k\varepsilon)=0$。
当 $k\to+\infty$，$\theta(t_0+k\varepsilon)$ 趋于右端固定点；
连续性和 (2.6) 令 $U$ 的极限为零。
递推 $U(t+\varepsilon)=-U(t)$ 因而强迫
$U(t_0+k\varepsilon)=0$ 对全部 $k\ge1$ 成立。
在 $k=0$ 得 $U(t_0)=G(t_0)>0$；向负方向递推得到非零交替值，
不可能在左端固定点有极限。矛盾。

所以即使 $R_\varepsilon$ 任意 $C^\infty$ 接近奇分母旋转，且旋转数
完全相同，$I+T$ 也未必从光滑源满射到连续函数。
这排除了仅靠这些输入建立适用于全部源的通常 Sobolev tame 右逆：
若 $H^{s+\ell}\to H^s$ 对某个 $s>1/2$ 有右逆，光滑源的解将连续，
与上面的具体源矛盾。

### 2.2 保酉的半密度权也不能自动修复

半密度传输在 (2.3) 下作酉变换
$$
U(t)=\sqrt{\theta'(t)}\,u(\theta(t)),
\qquad
\widehat G(t)=\sqrt{\theta'(t)}\,g(\theta(t)).
\tag{2.7}
$$
链式法则恰把
$u+\sqrt{R_\varepsilon'}\,u\circ R_\varepsilon=g$
化为
$$
U(t)+U(t+\varepsilon)=\widehat G(t).
\tag{2.8}
$$
源 $\widehat G$ 仍非零、非负且支持在 $(0,\varepsilon/3)$。
在 Fourier 变量 $\xi$ 中，
$$
(1+e^{i\varepsilon\xi})\widehat U(\xi)
=\widehat{\widehat G}(\xi).
$$
在 $\xi_0=\pi/\varepsilon$，分母有单零点，而
$$
\operatorname{Re}\widehat{\widehat G}(\xi_0)
=\int\widehat G(t)\cos(\pi t/\varepsilon)\,dt
>\frac12\int\widehat G(t)\,dt>0.
$$
因此局部商具有 $|\xi-\xi_0|^{-1}$ 奇性，不属于 $L^2_\xi$。
Plancherel 定理排除 $L^2_t$ 解；(2.7) 为酉换元，故原方程也没有
$L^2$ 解。这里明确保留了实际传输的 Jacobian 幅度，没有靠删除权
制造反例。

## 3. 这个反例排除了什么，尚未排除什么

反例同时具备：

- 奇数 $q$ 和通常 $I+T$ 的反周期符号；
- 返回图与 $p/q$ 旋转任意接近；
- 准确相同的旋转数 $p/q$；
- 平滑保向返回图；在半密度版本中传输还为酉算子。

因此这些信息本身不能证明全源有限损失可逆。
局部特征坐标和一个平均作用量也不足以推出所需全局结论。

但本例并未证明本题实际非径向返回图有上述障碍。仍有几种不同的
真实可能性，需要对实际几何判断：

1. 实际 Gauss--Codazzi、反射对称或相位结构可能给更强的返回恒等式。
2. 实际返回数可能转为合适的无理数并具有可证明的光滑共轭，见第 4 节。
3. 全局源可能属于带额外兼容条件的真像空间，径向函数自由度或其它
   参数可能支付那些条件；这不能由“源很小”代替证明。
4. 完整传输可能含已控制的低阶或平滑项；需要分析同一个完整算子，
   不能从纯主符号反例直接宣布完整问题无解。

特别，本文没有要求“必须证明 $R^{89}=\mathrm{id}$ 才能前进”，而是
排除一种尚未付清的通用充分条件。若能直接证明真实 $I+T$ 的相应逆，
完全可以不经过有限阶周期条件。

## 4. 非周期返回图仍有有限损失逆的准确充分条件

设 $R$ 由一个光滑保向微分同胚共轭到角度 $\alpha$ 的旋转。
对纯旋转，若存在明确 $\gamma>0,\tau\ge0$，使
$$
\operatorname{dist}(k\alpha,\pi+2\pi\mathbb Z)
\ge\gamma(1+|k|)^{-\tau}
\quad(k\in\mathbb Z),
\tag{4.1}
$$
则
$$
|1+e^{ik\alpha}|
\ge\frac{2\gamma}{\pi}(1+|k|)^{-\tau}.
$$
逐 Fourier 模相除给
$$
\|(I+T_\alpha)^{-1}g\|_{H^s}
\le\frac{\pi}{2\gamma}\|g\|_{H^{s+\tau}}.
\tag{4.2}
$$
实际共轭的复合与半密度乘法在指定 Sobolev 阶的范数一并付清后，
(4.2) 给相应 $R$ 的真实有限损失逆。
因此 $R^q=\mathrm{id}$ 确实不是必要条件；例如二次无理旋转数的
合适有理缩放可任意接近 $p/q$ 并满足一个明确的有限指数下界，
虽然其常数不随接近过程统一。

本题若采用这条路线，必须从实际非径向系数获得返回图、真实幅度、
所用共轭和 (4.1) 的常数。R25 的径向奇分母算术或 R28 的径向作用量
本身不能支付这些新的输入。

