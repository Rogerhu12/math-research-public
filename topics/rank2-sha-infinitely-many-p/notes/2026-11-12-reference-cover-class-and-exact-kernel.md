# 实际参考消期覆盖：亏格二类及其精确核

日期：2026-11-12。**状态：覆盖映射、差分形式下降、Hermite reduction
以及精确核反例均已证明。** 本篇没有把该固定类的 Cartier 非零
认作主课题中央系数的非零判据。

本文继续 [惰性解析半因子](2026-11-12-inert-central-mahler-half-factor.md)
§6 构造的实际 quartic 覆盖；不是从样本反向选择曲线或矩阵项。

## 1. 实际函数与两个不同的商

在 $E_1:y^2=x^3-x$ 上，令

$$
 A_R(z)=\sqrt{x(z)}\,R(x(z)^2)\,\sigma(z)^{17},\qquad
 S(z)=(x(z)^2+1)\sigma(z)^4,
$$

其中

$$
 R(X)=r_0X^3+r_1X^2+r_2X+r_3.
$$

实际目标的多项式是

$$
 R_*(X)=\frac15(X+1)(5X^2-2X+1)
       =X^3+\frac35X^2-\frac15X+\frac15.                     \tag{1.1}
$$

在固定曲线

$$
 C:\qquad y^2=x^3-x,\qquad v^4=\frac{x^2}{x^2+1}
                                                               \tag{1.2}
$$

上，$O$ 上方选择 $v\to1$ 的支。准确消期函数为

$$
 B_R=\frac{R(x^2)}{(x^2+1)^4}\,v,
 \qquad
 \frac{A_R(z)}{S(z)^{17/4}}=B_R(z).                           \tag{1.3}
$$

这里的四分之一次幂取常数项一的支。
令

$$
 w=\frac{x}{v^2},\quad w^2=x^2+1,\quad t=x+w.
$$

则

$$
 x=\frac{t-t^{-1}}2,\quad w=\frac{t+t^{-1}}2,\quad
 v^2=\frac{t^2-1}{t^2+1},\quad
 y^2=\frac{(t^2-1)(t^4-6t^2+1)}{8t^3}.                     \tag{1.4}
$$

故 $C$ 是 $\mathbb P^1_t$ 上的 $V_4$ 覆盖，三个二次商可准确写成

$$
 \begin{aligned}
 C_0:&\quad Y_0^2=t^4-1,
       &&Y_0=v(t^2+1),\\
 C_-:&\quad Y_-^2=2t(t^2-1)(t^4-6t^2+1),
       &&Y_-=4yt^2,\\
 C_+:&\quad Y_+^2=2t(t^2+1)(t^4-6t^2+1),
       &&Y_+=\frac{4t^2(t^2+1)yv}{t^2-1}.
 \end{aligned}                                                    \tag{1.5}
$$

右边的常数 $2$ 保留在 $\mathbb Q$ 模型中，未默默去掉二次扭转。
三者的亏格分别为 $1,3,3$，与 $g(C)=7$ 相容。

$B_R$ 本身在 $\mathbb Q(x,v)=\mathbb Q(C_0)$ 中；但展开所用的
加法微分 $dz=\omega_E=dx/(2y)$ 来自另一个商。
因此不能把 $B_R(z)$ 当作 $C_0$ 自己的不变微分所定义的 Taylor 展开。

## 2. 实际 second-kind 差分形式下降到亏格二

考虑不丢掉展开微分的形式

$$
                         \eta_R=B_R\omega_E.                \tag{2.1}
$$

由 (1.4)–(1.5) 直接计算

$$
 \omega_E=\frac{(t^2+1)^2v}{Y_+(t^2-1)}\,dt,
 \qquad
 \eta_R=\frac{R(x^2)}{(x^2+1)^4}(t^2+1)\frac{dt}{Y_+}.
                                                               \tag{2.2}
$$

在 $C_+$ 上取两个商坐标

$$
 u=t+t^{-1},\qquad
 Z=(t-t^{-1})\frac{Y_+}{t^2}.
$$

它们满足

$$
 D_+:\qquad Z^2=2u(u^2-4)(u^2-8),\qquad
                    \frac{du}{Z}=t\frac{dt}{Y_+}.            \tag{2.3}
$$

这是一个亏格二曲线。由于
$x^2=(u^2-4)/4$、$x^2+1=u^2/4$，得到准确下降式

$$
 \boxed{
 \eta_R=\frac{256}{u^7}
             R\!\left(\frac{u^2-4}{4}\right)\frac{du}{Z}.
 }                                                             \tag{2.4}
$$

也可从 involution 看出这一步的特征方向：在 $C_+$ 上
$(t,Y_+)\mapsto(1/t,Y_+/t^4)$ 把 $\eta_R$ 变为 $-\eta_R$。
所以它属于相应的亏格二余因子，不属于该 involution 的
$j=1728$ 椭圆商。

对实际 $R_*$，(2.4) 化为

$$
 \boxed{
 \eta_*=
    \frac{4(5u^4-48u^2+128)}{5u^5}\frac{du}{Z}.
 }                                                             \tag{2.5}
$$

它只有第二类极点。在 $u=0$ 的局部参数中，$u$ 是参数平方，
$du/Z$ 是单位微分；各极点阶均为偶数，故无留数。
其他有限点没有极点，无穷远处亦无留数。

## 3. 完整 Hermite reduction

记

$$
 f(u)=2u^5-24u^3+64u=Z^2.
$$

对每个整数 $m$，有

$$
 d(u^{-m}Z)=
 \bigl((5-2m)u^{4-m}+(24m-36)u^{2-m}
                  +(32-64m)u^{-m}\bigr)\frac{du}{Z}.        \tag{3.1}
$$

取 $m=7,5,3,1$ 依次消去 (2.4) 中的负幂，得到

$$
 \boxed{
 \begin{aligned}
 [\eta_R]=\frac1{12480}\bigl(&
 (1764r_0-204r_1-1980r_2-13932r_3)u\\
 &-(243r_0-113r_1-485r_2-3129r_3)u^3\bigr)\frac{du}{Z}
 \end{aligned}
 }                                                             \tag{3.2}
$$

作为代数 de Rham 类。式 (3.1) 提供了验证 (3.2) 的逐项三角消元，
没有使用数值积分。

特别地，对实际目标有

$$
 \boxed{[\eta_*]=\frac{17u^3-36u}{600}\frac{du}{Z}.}          \tag{3.3}
$$

这个特例的完整原函数为

$$
 \eta_*-\frac{17u^3-36u}{600}\frac{du}{Z}
 =d(UZ),\qquad
 U=-\frac{16}{45u^5}+\frac4{75u^3}-\frac{17}{1800u}.          \tag{3.4}
$$

在 $(u,Z)\mapsto(-u,iZ)$ 下，(3.3) 位于 $-i$ 特征的二维空间。
没有据此假定 $D_+$ 的 Jacobian 为 CM；该结论并不由一个四阶
automorphism 自动成立。

## 4. 已有一个准确的 Cartier 表达式，但它不是已证目标

设 $p\ge7$ 惰性，并在 $\mathbb F_p[u]$ 中写

$$
          f(u)^{(p-1)/2}=\sum_nc_nu^n.
$$

Cartier 对 $u^jdu/Z$ 的公式给

$$
 \boxed{
 \mathcal C(\eta_*)=
       \frac{17c_{p-4}-36c_{p-2}}{600}\frac{du}{Z}.
 }                                                             \tag{4.1}
$$

另一个 holomorphic 基方向的系数为零：$f$ 为奇多项式，
$(p-1)/2$ 为奇数，所以其幂中只有奇次项，而第二个方向所需下标
$2p-4,2p-2$ 均为偶数。
所有当前素数都不除 $600$，且 exact differential 的 Cartier 为零，
所以 (3.4) 可直接用于 (4.1)。

式 (4.1) 确实来自实际消期形式，但还不能据此断言它与
$\beta_{p+1}$ 的非零性等价。下一节给出准确的核，说明任何这种
比较都不能只通过 (2.4) 的 de Rham 类来定义。

## 5. 相同类、相同首项，目标 prime diagonal 却不同

取固定多项式

$$
                         K(X)=9X^2-15X+2.
$$

由 (2.4)、(3.1) 直接得到精确恒等式

$$
 \boxed{
 \eta_K=(144u^{-3}-2112u^{-5}+6656u^{-7})\frac{du}{Z}
             =d\left(-\frac{16Z}{u^7}\right).
 }                                                             \tag{5.1}
$$

因此 $R_*$ 与 $R_*+K$ 给完全相同的 de Rham 类。
相应截面 $A_{R_*}$、$A_{R_*+K}$ 的首项也都是 $z^4$，因为 $K$
没有三次项。更准确地，$A_K=9z^8+O(z^{12})$，所以相加并不改变
原来 $[z^4]A_{R_*}=1$ 的规范。

直接使用

$$
 x(z)=z^{-2}+\frac15z^2+O(z^6),\qquad
 \log(\sigma(z)/z)=-\frac1{60}z^4+O(z^8)
$$

可得对任意 $R$

$$
 [z^8]A_R=\frac{61}{60}r_0+r_1.                              \tag{5.2}
$$

于是

$$
 [z^8]A_{R_*}=\frac{97}{60},\qquad
 [z^8]A_{R_*+K}=\frac{637}{60}.
                                                               \tag{5.3}
$$

在第一个目标惰性素数 $p=7$ 处，两者分别为 $5$ 和 $0$ 模 $7$。
而 (5.1) 在 $7$ 处仍是整的 exact identity，故两者的 Cartier 类
完全相同。更具体地，$f\equiv2u^5+4u^3+u\bmod7$，
$c_3=1,c_5=5$，(4.1) 给两者同为 $du/Z\ne0$。

| 截面 | $z^4$ 首项 | 自然 de Rham 类 | Cartier 类（模 $7$） | $z^{p+1}$ 系数（模 $7$） |
|---|---:|---|---|---:|
| $A_{R_*}$ | $1$ | $[\eta_*]$ | $du/Z$ | $5$ |
| $A_{R_*+K}$ | $1$ | $[\eta_*]$ | $du/Z$ | $0$ |

这准确排除了下面的自然因子化：在这个固定、首项归一的截面族上，
把 prime diagonal，甚至只把它的非零性，定义为上述自然 de Rham
类及其 Cartier/Frobenius 数据的函数。

**范围。** $R_*+K$ 不是已证明属于 E17 的同一个有限 Schwartz
特征向量；本反例没有否定实际 $R_*$ 可能另有特殊的算术比较。
它说明若使用那个特殊特征，则必须在映射中保留相应的额外结构，
或者保留 exact primitive/参考 theta 信息，不能只保留 $[\eta_*]$。
这也不排除其他固定几何构造。

### 5.1 只增加原点纤维框架，仍不能恢复目标

取 $U=D_+\setminus\{u=0\}$，并以 $u=\infty$ 的点为基点。
函数

$$
                             F=-16Z/u^7
$$

在 $U$ 上正则，且在该基点为零：$Z$ 在无穷远的极点阶为五，
$u^7$ 的极点阶为十四，所以 $F$ 在此有九阶零点。
在 $U$ 上的秩二加法连接

$$
 \nabla_\eta=d-N\eta,\qquad
 N=\begin{pmatrix}0&1\\0&0\end{pmatrix}
$$

满足

$$
 (I+FN)^{-1}\nabla_{\eta+dF}(I+FN)=\nabla_\eta.
$$

且这个 gauge 在基点纤维上是恒等。因此 $\eta_*$ 与
$\eta_*+\eta_K$ 不仅给相同 de Rham 类，也给相同的**带基点纤维
框架的**加法连接。它们的内在 Frobenius 或 $p$-curvature 数据仍
不能区分 (5.3) 的两个 prime diagonal。

这个精确核已经落在九阶消失的原函数中；只保留原函数在基点的值
也不足够。若使用连接路线，需要说明如何保留并比较实际 theta
规范所指定的更高局部信息，而不能把一种 gauge 不变的判据直接
套给该 Taylor 系数。

## 来源与依赖

- [R51：实际 theta 截面](../results/R51-explicit-theta-section-and-central-square-constant.md)，
  包括 E17 到 E1 的准确四次缩放。
- [惰性解析半因子](2026-11-12-inert-central-mahler-half-factor.md)，§6，
  给出 (1.2)–(1.3) 的真实参考消期来源。
- [半因子首层](2026-11-12-inert-half-factor-first-layer.md)，
  说明目标同余仍是唯一的一次系数，不因其他下降阶乘项而增添条件。
- 本文全部覆盖等式、差分形式、Hermite reduction 与反例为显式代数
  恒等式；Cartier 公式采用通常 $\mathcal C(u^{pi-1}du)=u^{i-1}du$
  的规范。
