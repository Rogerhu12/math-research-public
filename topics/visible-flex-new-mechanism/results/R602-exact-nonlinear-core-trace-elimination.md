# R602 核心非线性余项的全角显式消元及可实现修正

日期：2026-11-26。状态：严格核心接口；主课题未完成。

本条继续 [R597](R597-nonlinear-core-trace-and-realizable-free-order.md)，
把其中真实核心方程进一步完全解出。它不改变当前已冻结的八模续接输入，
不把核心端的准确等式当成主体边值问题的解。

## 1. 同一准确核心数据

采用 R597 的全部假设，特别是 $1/2<\alpha<1$、
$W=k(R-r)^{-\alpha}(1+O(R-r))+O(1)$ 的导数一致展开、
$P=Wf_r$ 的足够角 jets 与径向一阶一致延伸，以及
$\langle f\rangle=0$、$f(R,\theta)=0$。记
$$
P_0=P(R,\cdot),\qquad P_1=P_r(R,\cdot),\qquad
c=\frac{\alpha}{1+\alpha},\qquad
S=\langle(P_0)_\theta^2\rangle . \tag{1}
$$
角均值均为同一材料角的 $1/(2\pi)$ 均值。
特别地，$\langle P_0\rangle=\langle P_1\rangle=0$。
由真实 turning 根唯一给定
$$
\langle u^{-1}\rangle=1,\qquad
u^2=e_R+2P_0>0 . \tag{2}
$$
R597 已支付此根的存在、唯一、正域与实际 $e'_R$ 极限；以下不另增一个独立的度量参数。
把 R597 的完整端式写成
$$
(A_t)_R=-RP_1+c u^2(P_0)_{\theta\theta}-(P_0)_\theta^2,
\qquad
D_R=(A_t)_R-\frac R2e'_R, \tag{3}
$$
$$
e'_R=-2\frac{\langle P_1/u^3\rangle+
\langle(P_0)_{\theta\theta}/u\rangle/[R(1+\alpha)]}
{\langle u^{-3}\rangle}. \tag{4}
$$

## 2. 全角条件的唯一显式解

在上述准确身份与零均值类中，$D_R(\theta)\equiv0$ 当且仅当
$$
\boxed{
P_1=P_1^*(P_0):=
\frac{c(e_R+2P_0)(P_0)_{\theta\theta}
-(P_0)_\theta^2+(2c+1)S}{R}.
} \tag{5}
$$
此时真实径向度量导数为
$$
\boxed{e'_R=-\frac{2(2c+1)}R S.} \tag{6}
$$

**必要性。** 若 $D_R=0$，(3) 说明 $(A_t)_R$ 是角常数。
周期分部积分给
$$
\langle u^2(P_0)_{\theta\theta}\rangle
=2\langle P_0(P_0)_{\theta\theta}\rangle=-2S . \tag{7}
$$
又因 $\langle P_1\rangle=0$，(3) 的均值为
$\langle(A_t)_R\rangle=-(2c+1)S$。
故 (6) 被强制，再由 (3) 逐角解出 (5)。这也证明唯一性。

**充分性。** (7) 先给 $\langle P_1^*\rangle=0$。
代 (5) 入 (3) 得 $(A_t)_R=-(2c+1)S$。
还须核对同一 turning 根确实给出 (6)，不能任意指定 $e'_R$。
由 $u_\theta=(P_0)_\theta/u$，有准确恒等式
$$
I:=\langle(P_0)_{\theta\theta}/u\rangle
=\langle(P_0)_\theta^2/u^3\rangle . \tag{8}
$$
因此
$$
\begin{aligned}
R\langle P_1^*/u^3\rangle
&=cI-I+(2c+1)S\langle u^{-3}\rangle\\
&=-\frac{I}{1+\alpha}+(2c+1)S\langle u^{-3}\rangle.
\end{aligned} \tag{9}
$$
(4) 中两项 $I/[R(1+\alpha)]$ 准确相消，得到 (6)，于是完整 $D_R=0$。
这消掉的是全部角频率及常数项，不是有限个投影。

非圆核心 $P_0\not\equiv0$ 时 $S>0$，故 (6) 严格为负；
圆核心则 $P_0=0$、$e_R=1$，(5) 给 $P_1^*=0$、$e'_R=0$。
这些是端部身份，均不单独支付主体曲率、嵌入性或 reach。

## 3. 可实施的完整参数导数

设 $H=\delta P_0$ 是零均值方向。对 (2) 隐微分，
$$
\delta e_R=-2\frac{\langle H/u^3\rangle}{\langle u^{-3}\rangle}.
\tag{10}
$$
因此完整导数为
$$
\boxed{
\delta P_1^*=
\frac{c\{(\delta e_R+2H)(P_0)_{\theta\theta}
+(e_R+2P_0)H_{\theta\theta}\}
-2(P_0)_\theta H_\theta
+2(2c+1)\langle(P_0)_\theta H_\theta\rangle}{R}.
} \tag{11}
$$
以及
$$
\delta e'_R=-\frac{4(2c+1)}R
\langle(P_0)_\theta H_\theta\rangle . \tag{12}
$$
对 (11) 作均值，$\delta e_R\langle(P_0)_{\theta\theta}\rangle=0$，
其余项由分部积分相消，故 $\langle\delta P_1^*\rangle=0$。
正域 (2) 内普通隐函数定理给 $e_R$ 的光滑参数依赖，
所以 (11) 是真实导数；不能在数值实现中冻结 turning 根再对其余项求导。

## 4. 不改变 $P_0$ 的实际高度修正

令 $r_a<r_b<R$，选一个明定的 $C^\infty$ 径向函数 $\chi$，
在 $r\le r_a$ 恒为 0、在 $r\ge r_b$ 恒为 1。
例如令
$$
\sigma(t)=\begin{cases}0,&t\le0,\\ e^{-1/t},&t>0,\end{cases}
\qquad
\chi(r)=\frac{\sigma((r-r_a)/(r_b-r_a))}
{\sigma((r-r_a)/(r_b-r_a))+
\sigma((r_b-r)/(r_b-r_a))} . \tag{13}
$$
分母处处正，故定义准确且两端全平。
对任意满足第1节的当前高度，定义
$$
\boxed{
\widetilde f=f+
\frac{\chi(r)(R-r)^{\alpha+2}}{k(\alpha+2)}
\{P_1^*(P_0)-P_1\}.
} \tag{14}
$$
该修正在 $r\le r_a$ 恒零，保留全部已定义的内尾和开握持区。
由 (5) 与原 $P_1$ 的零均值，$\langle\widetilde f\rangle=0$。
R597 的准确自由阶计算给
$$
\widetilde P_0=P_0,\qquad
\widetilde P_1=P_1^*(P_0). \tag{15}
$$
直接核也可：设 $B=(P_1^*-P_1)/[k(\alpha+2)]$，在核心附近 $\chi=1$，则
$$
W(\delta^{\alpha+2}B)_r
=-k(\alpha+2)B\delta+o(\delta),
\qquad
\partial_r[W(\delta^{\alpha+2}B)_r]
\longrightarrow k(\alpha+2)B . \tag{16}
$$
这里最后一步使用 R597 要求的导数一致展开；仅有无导数的 $o(\delta)$ 不足以求其导数。
(15) 及第2节于是给修正后完整核心 $\widetilde D_R\equiv0$。

在正则核心变量 $x=(\delta/d)^{1-\alpha}$ 中，修正阶为
$x^{(\alpha+2)/(1-\alpha)}$，指数严格大于 5。
按 R597 的核心自由阶结论，它在已经满足 R576 核心匹配门的候选上保持该 $C^2$ 匹配。
它并不使一个尚未满足那些门的任意高度自动成为闭合 $C^2$ 面。

修正一般改变连接段的完整 $D$、turning $E$ 与重构位置，
必须把 (14) 的径向、角向和参数导数全部带入原非线性残差与几何观察。
不能只把旧的核心残差列设为零，也不能沿一次声称固定 $g$ 的弯曲逐张改变 (14) 的背景度量。
本条允许在静态设计阶段使用它；最终仍须冻结一个完整 $g$。

若原高度依赖参数 $q$，修正导数为
$$
\delta\widetilde f=\delta f+
\frac{\chi\delta^{\alpha+2}}{k(\alpha+2)}
\{\delta P_1^* -\delta P_1\}, \tag{17}
$$
其中 (11) 给 $\delta P_1^*$。
若 $k,R,\alpha$ 也作为设计参数变化，还必须另对 (14) 的整个径向系数求导；
(17) 只针对它们固定的当前参数空间。

## 5. 有限角表示、全角端式与当前实际缺口

若 $P_0$ 为最高角频率 $J$ 的偶、$\pi$ 周期三角多项式，
则 $e_R$ 虽是由完整积分定义的非线性标量，仍不引入新角频率。
(5) 的最高频率至多 $2J$。
所以现有 $J=16$ 核心可准确形成最高32的从属核心修正。
这些18至32模在 $r\le r_a$ 恒零；它们不冒充尚未构造的高模内尾齐次解，
也不需要把低模内尾口借给它们。
这仍没有给整个主体的18至32方程求解，也没有控制32以上的非线性泄漏。

实现时乘积必须按确切三角系数卷积或足以无混叠的角网求出。
turning 标量 (2) 是真正连续角积分；一次有限求积所得根、(5) 的浮点值与近零的 $D_R$
只是该输入的数值观察，除非另外给出严格求积、浮点和端值误差界。
公式的准确身份不能把这些误差免费认证。

当前八模首终态的主体最大高模在 $m=18$、$r\approx.332$，
而核心 $m=4$ 的非线性余项也尚未消尽。
若选择 $r_a>.332$，(14) 根本不改变前一个已见峰；
因此本条提供的是准确核心条件的消元，不能取代下一完整主体求解。
这两项原数值观察的身份见
[八模首自然终态收据](../notes/2026-11-26-r594-eight-mode-weak-natural-final.md)。
