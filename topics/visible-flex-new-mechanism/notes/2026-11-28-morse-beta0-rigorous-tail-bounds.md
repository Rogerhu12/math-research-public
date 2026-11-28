# Morse 全线参考 $\beta_0$ 的显式尾界与球积分输入

2026-11-28。**以下两条尾界已由正积分直接证明。** 紧区间球积分 source 已准备，尚须读取一次实际成功输出，才能把全文最后的严格有理区间登记为结论。本稿仅涉及 R630 的左正规全线参考，不是 R633 真平尾端口的结论。

## 1. 精确被积式

沿用 R630 的 $s=\sqrt5$、$\eta$、$\beta=\sqrt{\eta^2+B}$，令

$$
\alpha_1=(s-1)/2,\quad \alpha_2=s-1/2,\quad
\kappa_3=(3s-3)/2,\quad
a=\beta-s/2+1/2,\quad b=1+2\beta,\quad t=e^{-X}.
$$

定义

$$
\Psi(t)=e^{-st}(2st)^\beta U(a,b,2st),\qquad
R(t)=t^{-\eta}\Psi(t),\qquad
\nu(t)=\eta+st-\beta+
2sat\,\frac{U(a+1,b+1,2st)}{U(a,b,2st)}.
$$

R630 已证明 $\nu>\eta>3/2$。归一化 $r(0)=w(r(0))=f_2(0)=f_3(0)=1$ 后，令

$$
C_*=\frac{\nu(1)R(1)^3}
 {2e^{-2s}e^{-3s}(-3s-2)}.
$$

这里 $C_*<0$；source 会用实球严格检验 $|C_*|<10^4$，而非把先前浮点值当成已知界。

写

$$
k_2=\eta-\alpha_2+2st,\qquad P=3s-2-6st,
$$
$$
Q=(\eta-\kappa_3+3st)P+6st,\qquad
\mathcal H=\frac{k_2Q}{\nu^2}
 -\frac{9k_2P}{\nu}-\frac{4Q}{\nu}+12P.
$$

从 R628 的 $w^2$ 无关部分直接代入 $dr=r_XdX$ 得

$$
\boxed{\beta_0=\int_0^\infty \mathcal I(t)\,dt,\qquad
\mathcal I(t)=
-C_*\,t^{\alpha_2+\kappa_3-\eta-1}e^{-5st}
\Psi(t)^{-3}\mathcal H(t).}                             \tag{1}
$$

式 (1) 保留同一个 $r$、同一个 $w$ 和同一个核归一化。

## 2. 两个全局正下界

Tricomi 正积分是

$$
U(a,b,z)=\Gamma(a)^{-1}
\int_0^\infty e^{-zu}u^{a-1}(1+u)^{b-a-1}\,du.
$$

在这里

$$
2<s<9/4,\quad 3/2<\eta<5/3,\quad 3/2<\beta<5/3,
$$
$$
7/8<a<7/6,\qquad b-a-1=\beta+s/2-1/2>0.
$$

分别用 $(1+u)^{b-a-1}\ge1$ 和
$(1+u)^{b-a-1}\ge u^{b-a-1}$，得到对所有 $t>0$ 都有效的

$$
\Psi(t)\ge e^{-st}(2st)^{\alpha_1},\qquad
\Psi(t)\ge C_\Gamma e^{-st}(2st)^{-\beta},
\quad C_\Gamma=\frac{\Gamma(2\beta)}{\Gamma(a)}.          \tag{2}
$$

还有一个不依赖数值特殊函数的粗常数

$$
C_\Gamma>\frac12.
$$

确实
$\Gamma(a)<1/a+\int_1^\infty ue^{-u}du<8/7+1<3$，
而
$\Gamma(2\beta)>\int_1^\infty u^2e^{-u}du=5/e>5/3$。

## 3. 统一多项式上界

由上述参数范围，

$$
|k_2|\le1/4+(9/2)t,\qquad
|P|\le19/4+(27/2)t,
$$
$$
|Q|\le(3/8+(27/4)t)(19/4+(27/2)t)+(27/2)t.
$$

利用 $\nu^{-1}<2/3$，当 $0<t\le1$ 时有

$$
|k_2|<5,\quad |P|<19,\quad |Q|<144,
$$
$$
|\mathcal H|
<\frac49(5)(144)+6(5)(19)+\frac83(144)+12(19)
=1502<1600.                                            \tag{3}
$$

当 $t\ge1$ 时，同一证明给

$$
|\mathcal H(t)|<1600t^3.                                \tag{4}
$$

## 4. 小 $t$ 尾小于 $10^{-4}$

假设待球值检验的 $|C_*|<10^4$。对 $0<t<1$，使用 (2) 的第二界以及
$C_\Gamma^{-3}<8$、$(2s)^{3\beta}<(9/2)^5<2000$，得到

$$
|\mathcal I(t)|
<256000000000\,
t^{\alpha_2+\kappa_3-\eta+3\beta-1}.
$$

指数大于 $29/6>4$，所以当 $\delta=1/1024$ 时

$$
\int_0^\delta|\mathcal I(t)|\,dt
<\frac{256000000000}{5}\delta^5
=\frac{51200000000}{2^{50}}<\frac1{10000}.                \tag{5}
$$

这不是以浮点积分估计的误差项。

## 5. 大 $t$ 尾小于 $10^{-8}$

使用 (2) 的第一界。指数准确简化为

$$
\alpha_2+\kappa_3-\eta-1-3\alpha_1
=s-\eta-\frac32<-\frac34.
$$

由 $s>2$ 和 (4)，在 $t\ge1$ 有

$$
|\mathcal I(t)|<16000000\,t^3e^{-4t}.
$$

因此

$$
\int_{12}^\infty|\mathcal I(t)|\,dt
<16000000\,e^{-48}
\left(\frac{12^3}{4}+\frac{3\cdot12^2}{16}
      +\frac{3\cdot12}{32}+\frac3{128}\right)
<10^{-8}.                                               \tag{6}
$$

最后一步例如由 $e^3>20$（指数级数前九项已大于 20）得
$e^{48}>20^{16}>6\cdot10^{20}$，而括号小于 $461$。

## 6. 唯一剩下的有限球积分

独立 source 为
scripts/morse_beta0_ball_integral_20261128.py。它只在准确公共仓库的真实 Actions 环境执行，使用 python-flint 的 Arb/Acb 球算术；在
$[1/1024,12]$ 上对 (1) 积分，并记录每段球包围、真实 callback/特殊函数调用及耗时。

依照 [官方 acb API](https://python-flint.readthedocs.io/en/latest/acb.html)，source 在任何复球未严格包含于 $\operatorname{Re}t>0$ 时返回非有限球；幂运算传递 analytic flag。这样不会把跨过幂或 $U$ 分支切线的复邻域谎报为解析。分母若可能含零，球除法也返回非有限包围，要求积分器继续细分。

[FLINT 的积分定义](https://github.com/flintlib/flint/blob/main/doc/src/acb_calc/index.md) 给出有限段积分的严格包围；精度目标不替代输出球的实际半径。source 只在所有段均得到有限包围后，取其精确 dyadic 上下界，加上 (5)、(6) 的有理绝对尾界，再进行准确有理数比较。

若该实际输出成功，则证明的结论是

$$
\boxed{\frac13<\beta_0<\frac38}                           \tag{7}
$$

于 R630 的全线左正规参考。未读取成功输出前，(7) 仍标为待完成的计算输入。即使 (7) 已完成，R633 真平尾端口的连续性和尾贡献也仍须单独证明。
