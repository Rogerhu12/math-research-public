# R72：小缺陷坐标的两阶时间有序积分

2026-11-12，visible-exact-astra-f6a2。

**已证明：带完整三阶余项的流恢复公式。** 在 R68 的同一个参考坐标中，
只需积分小场及一个有序二次项，就能将真实流误差从一阶总缺陷降到三阶。
它不要求每个参考段重新构造高次轨迹，也不把各段初值误差重置为零。
本结果的实际输入仍须来自完整两腿和完整初值复带；当前单段场包不代付它们。

## 1. 同一个参考坐标和完整小场

采用 [R68](R68-reference-coordinate-defect-flow.md) 的全部假设。沿两腿的
共同递增时间取 $t\in[a,b]$，准确参考 $Y(t,x)$ 在所有接缝上连续，
$q=Y_x$ 在初值标签带 $\mathcal S_S$ 非零。定义

$$
 h(t,x)=\frac{f(t,Y(t,x))-Y_t(t,x)}{Y_x(t,x)},\qquad
 X_t=h(t,X),\quad X(a,x)=x.
 \tag{1}
$$

令 $\widehat h$ 为实际选出的近似场，关于标签全纯且具有 $2\pi$ 周期，关于时间分段连续。
后面的各 $\widehat g_j$ 保持同一标签周期；实际有限 Fourier 选择自动满足此条件。
全部时间与标签 Fourier/Taylor 截尾、原始无限 primitive、真实场近似和
算术舍入必须包含在逐时界内：

$$
 \sup_{\mathcal S_S}|h|,\ \sup_{\mathcal S_S}|\widehat h|\le M(t),
 \qquad \sup_{\mathcal S_S}|h-\widehat h|\le\eta(t).
 \tag{2}
$$

这里两个场共用 $M$；若已知 $\widehat M\ge|\widehat h|$ 和误差 $\eta$，
可安全取 $M=\widehat M+\eta$。记

$$
 A(t)=\int_a^tM(v)\,dv,\quad E(t)=\int_a^t\eta(v)\,dv,
 \quad A=A(b),\ E=E(b).
 \tag{3}
$$

选择 $0\le\sigma<S$，写 $R=S-\sigma$，并假设

$$
 A\le R/2,\qquad d=R-A>0.                              \tag{4}
$$

定义真实小场的两个时间有序积分

$$
 V_1(t,x)=\int_a^t h(v,x)\,dv,
 \qquad
 V_2(t,x)=\int_a^t h_x(v,x)V_1(v,x)\,dv.                \tag{5}
$$

用 $\widehat h$ 同样定义 $\widehat V_1,\widehat V_2$。
第二式的顺序不能颠倒，通常也不能用
$\tfrac12 V_{1,x}(t,x)V_1(t,x)$ 替代。

## 2. 完整三阶流余项

对所有 $|\operatorname{Im}x|\le\sigma$，R68 给
$|X(t,x)-x|\le A(t)$。由全纯 Cauchy 估计，在从 $x$ 到 $X(t,x)$ 的
整条线段上可用

$$
 |h_x(t,\cdot)|\le M(t)/d,\quad
 |h_{xx}(t,\cdot)|\le2M(t)/d^2,\quad
 |h_x(t,x)|\le M(t)/R.                                  \tag{6}
$$

这些界只来自小缺陷场 $h$；没有重新引入真实大场的变分增长。
令 $u=X-x$。先由积分恒等式得

$$
 |u(t)-V_1(t)|
 \le\int_a^t\frac{M(v)}d A(v)\,dv
 =\frac{A(t)^2}{2d}.                                    \tag{7}
$$

在同一带内，对真实 $h(v,x+u(v))$ 作二阶 Taylor 积分公式，得到

$$
\begin{aligned}
u(t)-V_1(t)-V_2(t)
={}&\int_a^t h_x(v,x)[u(v)-V_1(v)]\,dv\\
 &+\int_a^t u(v)^2\int_0^1(1-s)h_{xx}(v,x+s u(v))\,ds\,dv.
\end{aligned}                                          \tag{8}
$$

全部线段都距外边界至少 $d$。代入 (6)–(7)，使用
$\int_a^tM(v)A(v)^2\,dv=A(t)^3/3$，可得更细的界
$A(t)^3/(6Rd)+A(t)^3/(3d^2)$。特别地

$$
 \boxed{\sup_{\mathcal S_\sigma}
 |X(t,x)-x-V_1(t,x)-V_2(t,x)|\le\frac{A(t)^3}{2d^2}.}
 \tag{9}
$$

这是真实非线性流的余项，不是只对截断幂级数成立的恒等式。
同样，由 (5) 和 $x$ 处的 Cauchy 界，

$$
 |V_1|,|\widehat V_1|\le A(t),\qquad
 |V_2|,|\widehat V_2|\le\frac{A(t)^2}{2R}.               \tag{10}
$$

## 3. 近似小场的误差如何进入

在同一 $x$ 处，(2) 和 Cauchy 给

$$
 |V_1-\widehat V_1|\le E(t),\quad
 |h_x-\widehat h_x|\le\eta(t)/R.
$$

将二次项之差准确写成

$$
 V_2-\widehat V_2
 =\int_a^t\bigl[(h_x-\widehat h_x)V_1
             +\widehat h_x(V_1-\widehat V_1)\bigr]\,dv,
$$

并用 $(AE)'=ME+\eta A$，得到

$$
 |V_2(t)-\widehat V_2(t)|\le A(t)E(t)/R.
$$

因此完整坐标误差满足

$$
 \boxed{\sup_{\mathcal S_\sigma}
 |X(t,x)-x-\widehat V_1(t,x)-\widehat V_2(t,x)|
 \le E(t)\left(1+\frac{A(t)}R\right)+\frac{A(t)^3}{2d^2}.}
 \tag{11}
$$

不需要将 $(2)$ 中的近似误差再乘一个真实场的指数增长因子。
若计算所得两积分还被有限 Fourier 投影或近似求积，必须再加它们相对
准确 $\widehat V_1+\widehat V_2$ 的完整误差；“积分一个有限多项式”
本身不授权在乘积时删掉最高 Fourier 模。

## 4. 全部时间段的准确拼接

为第 $j$ 段使用局部坐标 $u\in[-1,1]$，物理时间可正向或反向。
若 $\tau=\tau_{c,j}+h_j u$，将半宽的有符号因子放进小场，准确定义

$$
 g_j(u,x)=\frac{h_j f(\tau(u),Y_j(u,x))
                         -\partial_uY_j(u,x)}{\partial_xY_j(u,x)}.
 \tag{12}
$$

返回腿即使 $h_j<0$，局部积分仍从 $-1$ 到 $1$；没有把它错当正向
物理时间。完整界是对这些局部小场按 $du$ 积分，等价于共同递增时间。
选定近似 $\widehat g_j$，令

$$
 G_j(u,x)=\int_{-1}^u\widehat g_j(v,x)\,dv,
 \quad G_j^+(x)=G_j(1,x),
$$
$$
 J_j(x)=\int_{-1}^1\partial_x\widehat g_j(u,x)G_j(u,x)\,du.
 \tag{13}
$$

若前一段结束的两个累计积分为 $(C_1,C_2)$，新端点准确为

$$
 \boxed{
 C_{1,\rm new}=C_1+G_j^+,
 \qquad
 C_{2,\rm new}=C_2+(\partial_xG_j^+)C_1+J_j.}
 \tag{14}
$$

右侧用更新之前的 $C_1$。证明只需将段内的首积分写成
$C_1+G_j(u)$，代入第二个积分。这个交叉项保留了全部先前时间；
把每段 $C_1$ 清零会漏掉它。所有腿与真正参考跳跃仍须满足 R68 的
准确接缝合同，本文不允许拿 (14) 掩盖未匹配的参考。

若 $\widehat g_j$ 是明确的有限时间/Fourier 多项式，(13)–(14)
都是有限代数运算，任意次数增长可直接保留，也可付费投影；
利用等间距 DFT 做有限乘积时，必须用足够 padding 或显式付清回卷。

## 5. 真实物理返回与 Wiener 误差

令

$$
 W(x)=x+\widehat V_1(b,x)+\widehat V_2(b,x),
 \quad B=E(1+A/R)+A^3/(2d^2).
$$

由 (4)、(10)，$|W-x|\le A+A^2/(2R)\le5R/8$，故 $W$ 与 $X(b,x)$
及它们的线段仍在外标签带内。记

$$
 Q_*\ge\sup_{|\operatorname{Im}z|\le\sigma+A+A^2/(2R)}|Y_x(b,z)|.
$$

准确流是 $y(b,x)=Y(b,X(b,x))$，因而

$$
 |y(b,x)-Y(b,W(x))|\le Q_* B.                           \tag{15}
$$

对任意 $0\le s<\sigma$，应用 R63 的包含平均模的两边界 Hardy 界：

$$
 \boxed{\|4y(b,\cdot)-4Y(b,W(\cdot))\|_{A_s}
 \le4Q_*B\sqrt{2\coth(\sigma-s)-1}.}                    \tag{16}
$$

若计算中另用有限端点函数代替准确复合 $Y(b,W)$，其整个连续带误差
也必须加入 (15)；若只有节点值，不能直接写 (16)。这个真实端点可接
R63 的固定 $H$ 局部逆和 R31 的共轭误差，但实际参数导数、横截、
KAM 小量门、全 PDE 反馈和非线性闭曲面仍各自需要证明。

本结果没有宣称当前 δ₅ 的 $A,E,Q_*$ 已完成计算。它给出下一实际
残差汇总所用的准确公式及清楚的三阶误差，避免为同一目的反复构造
整个高次两腿参考。主目标继续。
