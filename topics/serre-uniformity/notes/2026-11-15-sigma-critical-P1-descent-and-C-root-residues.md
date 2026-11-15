# 原临界五次源的 P1 下降与 C 根留数

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：下列下降与各类局部留数式已证明；指定 CM 值及原 same-h 三单位仍开放。**
本文沿用 [CR 的原五次源](2026-11-15-sigma-critical-Cartier-residues-on-original-X6.md)
的 $p=6N+5\ge41$、$A=U\mathfrak a(U^3)$、$C=\mathfrak c(U^3)$、
$D=1-8U^3$、$X_6:x^3+y^3=2$ 及全部原尺度。
设
$$
Z=1-\kappa U^pJ=D(A'C-AC'),\qquad T=C/A.
\tag{HC1}
$$
prime 仍是 $\partial_U$。PC 给出的实际恒等式为
$$
T'=-\frac{Z}{DA^2},\qquad Z'=-\kappa U^{p-1}A.
\tag{HC2}
$$
没有将 $C$ 改作第二个水平周期，或把 $Z$ 改成一。

## 1. 五次源本身下降到原 x 直线

由 $U=xy/2$ 和 $dy=-x^2dx/y^2$，直接约去 $y$ 得
$$
\boxed{
\beta=\left(\frac AC\right)^5\frac{dy}{y^3-1}
=-\frac{x^7(2-x^3)}{32(1-x^3)}
 \left(
 \frac{\mathfrak a(x^3(2-x^3)/8)}
      {\mathfrak c(x^3(2-x^3)/8)}
 \right)^5dx.
}
\tag{HC3}
$$
也就是说，$\beta$ 是 $X_6\to\mathbf P^1_x$ 下一个真正有理微分的 pullback。
几何上这是 $y\mapsto\zeta y$ 的实际商；$U^5dy$ 的角色是
$\zeta^6=1$。这里正是五次幂使下降成立，没有删除周期分母。

该三次覆盖可分，故 Cartier 也直接在 $\mathbf P^1_x$ 上计算。
右端在无穷远的 Laurent 指数都是 $7$ 模三，因此不可能有 $x^{-1}dx$
项。三个原无穷远点在 $x$ 直线上都不分歧，所以它们的 $\beta$ 留数
全部为零；CR 的极阶界遂说明 $\operatorname{Car}(\beta)$ 在那里正则。
全部 Cartier 极点只可能来自真正的 $C$ 根和 $x^3=1$。

若写 $\operatorname{Car}(\beta)=F(x)dx$，则 $x\mapsto\zeta x$ 的
角色交换还给 $F(\zeta x)=F(x)$，故 $F\in k(x^3)$。
这仍不意味着其在 $x=0$ 的值非零。

## 2. 非 cusp 的简单 T 零：消去全部 C 导数

先取 $D(a)\ne0$ 且 $T$ 在 $U=a$ 有简单零的实际点。
包括 $C$ 为单根、$A$ 为单位的情况，也包括 $C$ 有二重零而
$A$ 有简单零、约去公因子后 $T$ 为单零的情况。
在后一种情况，$A^2/Z$ 在该点是正则单位。

由 (HC2) 与 $\alpha_0=-x^2dU/D$，
$$
\beta=T^{-5}\alpha_0
=T^{-5}\frac{x^2A^2}{Z}\,dT.
$$
因此完整留数为
$$
\boxed{
\operatorname{res}_{U=a}\beta
=\left.
\frac1{4!}\left(-\frac{DA^2}{Z}\partial_U\right)^4
                 \left(\frac{x^2A^2}{Z}\right)
\right|_{U=a}.
}
\tag{HC4}
$$
$U$ 在非 cusp 有限点是 etale 参数；所以式中没有漏掉局部分歧因子。
所有表面上的 $A^2/Z$ 零除零均先在函数域约去，才在点上评价。
这把 $C$ 的全部导数从留数中消去；$C$ 仅指定评价点。
所剩 $A,J$ 及其导数是真实输入，不能把它们的值当作任意单位。

若 $A,C$ 都是单根，则 $A/C$ 正则，该点没有 $\beta$ 极点。
PC 已证明 $A$ 在 $D\ne0$ 的根都简单，$C$ 的根至多二重，
故这里没有遗漏更高公因子。

## 3. C 二重零而 A 为单位

在这个剩余的非 cusp 情形，$T$ 有二重零，且 (HC2) 给
$$
Z(a)=0,\qquad Z'(a)=-\kappa a^{p-1}A(a)\ne0.
$$
选择 etale 局部平方根 $v^2=T$；因 $T$ 为二重零，$v$ 本身是局部参数。
于是
$$
\partial_v=-\frac{2vDA^2}{Z}\partial_U,\qquad
\frac{\alpha_0}{dv}=\frac{2v x^2A^2}{Z}.
$$
两式的右端在该点均正则，导子前的系数为单位。
完整九阶公式为
$$
\boxed{
\operatorname{res}_{U=a}\beta
=\left.
\frac1{9!}\left(-\frac{2vDA^2}{Z}\partial_U\right)^9
                    \left(\frac{2v x^2A^2}{Z}\right)
\right|_{v=0}.
}
\tag{HC5}
$$
换 $v$ 的符号不改变留数。

若只希望使用 $A,J$ 的有限 jet，可先由 (HC2) 作唯一的有限积分
$T(a)=0$、$T'=-Z/(DA^2)$，再开平方；所需阶数严格小于 $p$，
所有积分分母及 $9!$ 都是单位。
特征 $p$ 中的积分差可能是 $(U-a)^p$ 的函数，不能说它全局不存在；
但这些差从阶 $p$ 开始，而极阶最多十，故不改变本式。

## 4. cusp：保留可能的十一阶极点

令 $d^3=1/8$，在一个实际 cusp 写
$$
W=x^3-1,\quad U=d(1-W^2)^{1/3},\quad
y=y_c(1-W)^{1/3},\quad y_c^3=1.
$$
则
$$
\alpha_0=\frac{y_c}{3W}(1-W)^{-2/3}dW.
\tag{HC6}
$$
PC 给 $A(d)=d a_*$，其中 $a_*\in k^\times$，而
$C(d)=c_*:=\mathfrak c(1/8)$ 与所选 $d$ 无关。

若 $c_*\ne0$，$\beta$ 在该点是简单极点，准确留数为
$$
\operatorname{res}\beta
=\frac{y_c}{3}\left(\frac{d a_*}{c_*}\right)^5.
\tag{HC7}
$$
在 $\mathbf P^1_x$ 的记法，$x=b$、$b^3=1$ 时这就是
$$
\boxed{\operatorname{res}_{x=b}\beta
 =\frac{b^2}{96}\left(\frac{a_*}{c_*}\right)^5.}
\tag{HC8}
$$
因此 $c_*\ne0$ 时整个 $\operatorname{Car}(\beta)$ 确实非零。
这仍没有排除其 $x=0$ 值被其他实际极点贡献抵消。

若 $c_*=0$，PC 的方程迫 $C$ 在每个 $U=d$ 简单为零，$A(d)$ 为单位，
所以 $T$ 在 $U=d$ 是简单零，而在 $W$ 中是二重零。
必须使用完整十一阶极部。由 (HC6) 精确得
$$
\boxed{
\operatorname{res}\beta
=\frac{y_c}{3}[W^{10}]
 \left(\frac{W^2}{T(d(1-W^2)^{1/3})}\right)^5
 (1-W)^{-2/3}.
}
\tag{HC9}
$$
这里括号内是单位级数；(HC2) 中 $Z/D$ 的零因子先相消后给
$T$ 的有限 jet，因而本式也只需原 $A,J$ 的有限导数。
没有把 (HC8) 在 $c_*=0$ 处当成有意义的除法。

## 5. 余下的实际算术

(HC3)--(HC9) 给原 $C^{-5}$ 源一个不含未知正则微分的、覆盖所有极点
类型的 Hermite / 留数描述；特别双根、公共根和 cusp 分歧都没有删去。
但 (HC4)、(HC5)、(HC9) 的实际值以及它们对 $x=0$ 的加权总和仍须控制。
原 $Z=1-\kappa U^pJ$、$A'$ 等数据在这些式中真实存在。
本篇不以 $\kappa$ 单位或整个 Cartier 微分非零替代指定值非零，
也没有把未筛平方卷积替代原 primitive / Legendre 同标签向量。
