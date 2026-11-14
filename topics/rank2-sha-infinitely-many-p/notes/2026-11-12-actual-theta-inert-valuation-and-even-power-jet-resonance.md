# 实际 theta 连接的全部惰性赋值与偶次幂共同 jet 共振

日期：2026-11-12。**状态：以下赋值公式、截断整性、原源格的共同
行变换及块共振均已证明。** 共振不使用两条中央导数同时消失，
而且只控制指定的源次数块；本文未得到 R159 所需的严格惰性预算。

## 1. 保留 R162 的固定输入

在 $E_0:y^2=x^3-x$ 上，沿 R162 的原点支，记

$$
s=x^{-2},\qquad
\mathcal A(s)=A_2=P(s)e^{W(s)}=sZ(s),\qquad
Z(s)=p_0(s)e^{W(s)},\qquad p_0=P/s.
\tag{1.1}
$$

其中 $P$ 是 R162 显示的固定次数十六多项式，
$p_0\in1+s\mathbb Z[1/5][s]$，且

$$
W(s)=\sum_{m\ge1}w_ms^m,\qquad
w_m=\frac{17}{m}\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
\tag{1.2}
$$

两条真实行仍满足

$$
B=(1+V)A_2,\qquad
V(s)=\frac{(1+s)Q_8(s)}{(1-s)H_1(s)H_2(s)}-1
     \in s\mathbb Z[[s]],\qquad V'(0)=-22.
\tag{1.3}
$$

$H_1,H_2,Q_8$ 是 R117/R162 的原整多项式，常数项均为一。
因此 (1.3) 的整性不含任何周期选择。

本篇 $p\ge7$ 且 $p\equiv3\pmod4$。第 2–3 节也包含 $p=11$；
涉及共同行的范数等距时另删这个固定素数，因为 $V'(0)=-22$。
所有赋值采用 $v_p(p)=1$。

## 2. 每个系数的精确赋值

对正整数 $m,h$，令

$$
\epsilon_h(m)=
\mathbf1_{\{\,p^h/4<(m\bmod p^h)<3p^h/4\,\}}.
\tag{2.1}
$$

这里余数取 $0,\ldots,p^h-1$。有全范围的准确式

$$
\boxed{\quad
v_p(w_m)=-v_p(m)+\sum_{h\ge1}(-1)^h\epsilon_h(m).
\quad}
\tag{2.2}
$$

和式有限：$p^h>4m$ 时相应指标为零。

**证明。** 对 $q=p^h$，计算 (1.2) 中分子、分母被 $q$ 整除的次数。
若 $q\equiv1\pmod4$，两个根在 $j\bmod q$ 中分别是

$$
j_N=(q-1)/4,\qquad j_D=(3q-3)/4.
$$

若 $q\equiv3\pmod4$，它们分别是

$$
j_N=(3q-1)/4,\qquad j_D=(q-3)/4.
$$

写 $m=aq+r$、$0\le r<q$。区间 $0\le j<m$ 内每个根出现
$a+\mathbf1_{r>j_N}$ 或 $a+\mathbf1_{r>j_D}$ 次。
完整的 $a$ 个块相消，差值在 $q\equiv1\pmod4$ 时为
$\mathbf1_{q/4<r<3q/4}$，在 $q\equiv3\pmod4$ 时为其负值。
惰性 $p$ 给 $q\equiv(-1)^h\pmod4$，再保留外面的 $1/m$，
便得到 (2.2)。常数 $17$ 在这些素数处为单位。$\square$

若 $m=p^ab$、$p\nmid b$，(2.2) 等价于

$$
v_p(w_m)=-a+(-1)^a
              \sum_{h\ge1}(-1)^h\epsilon_h(b).
\tag{2.3}
$$

因为前 $a$ 个余数为零，而
$\epsilon_{a+h}(p^ab)=\epsilon_h(b)$。

## 3. 偶指数截断的准确一层余量

**命题。** 对每个整数 $H\ge1$，

$$
\min_{1\le m<p^H}v_p(w_m)=
\begin{cases}
-H,&H\text{ 为奇数},\\
-H+1,&H\text{ 为偶数}.
\end{cases}
\tag{3.1}
$$

边界项另为

$$
v_p(w_{p^H})=-H.
\tag{3.2}
$$

**证明。** 写 $m=p^ab$，其中 $0\le a\le H-1$、$b<p^{H-a}$。
由于 $p>4$，(2.3) 的和式至多含 $H-a$ 项。
$a$ 偶数时，负号项至多 $\lceil(H-a)/2\rceil$ 个；
$a$ 奇数时，负号项至多 $\lfloor(H-a)/2\rfloor$ 个。
因此损失最多是

$$
a+\begin{cases}
\lceil(H-a)/2\rceil,&a\text{ 偶},\\
\lfloor(H-a)/2\rfloor,&a\text{ 奇}.
\end{cases}
$$

对 $0\le a\le H-1$ 取最大值，准确是奇 $H$ 时的 $H$、
偶 $H$ 时的 $H-1$。

两个界均可达到。$H$ 偶数时取 $m=p^{H-1}$，所有
$\epsilon_h(1)$ 都为零；$H$ 奇数时取
$m=p^{H-1}(p+1)/4$，其 $a=H-1$ 为偶数，且剩余部分恰有
$\epsilon_1=1$、其余为零。最后 $m=p^H$ 再直接用 (2.3)，
得到 (3.2)。$\square$

令

$$
G(s)=\log Z(s)=\log p_0(s)+W(s).
$$

由于 $p_0'/p_0\in\mathbb Z_p[[s]]$，

$$
v_p([s^m]\log p_0)\ge-v_p(m).
\tag{3.3}
$$

所以，当 $H=2a\ge2$ 时，(3.1) 给

$$
p^H G(s)\in
p\,s\mathbb Z_p[s]/(s^{p^H}).
\tag{3.4}
$$

在这个有限幂零环中取形式指数，得到

$$
\boxed{\quad
Z(s)^{-p^{2a}}\equiv1
\pmod{p,\ s^{p^{2a}}}\qquad(a\ge1).
\quad}
\tag{3.5}
$$

这是有限 jet 恒等式，无需在边界圆盘上解释形式指数的收敛。
具体地，(3.4) 的非恒定部分属于 $p$ 倍整系数理想；
指数第 $j$ 项的赋值至少为 $j-v_p(j!)\ge1$。
因此所有非恒定系数均落在 $p\mathbb Z_p$。

这里必须保持截断 $m<p^H$。(3.2) 说明不能把 (3.4) 所用的
$W$ 界延长到 $m=p^H$。本篇也不声称
$[s^{p^H}]G$ 恰有该赋值，因为 $\log p_0$ 与 $W$ 在该项可能抵消。

## 4. 同一个固定 gauge 作用于全部原列

原平面源与 R162 相同，整幺三角换基后是

$$
\mathcal A^jV^c,\qquad 0\le c\le j\le D.
\tag{4.1}
$$

仍以 $X=\mathcal A(s)=w+O(w^2)$ 为输出参数。令

$$
\gamma(s)=\frac{V'(s)}{\mathcal A'(s)}
\in\mathbb Q[[s]],\qquad\gamma(0)=-22.
\tag{4.2}
$$

把每一个源输出都乘以同一个固定形式单位 $\gamma(s(X))$。
这没有增加源变量，也没有逐列更换输入。
对任意原输出 $f(X)$，

$$
\operatorname{ord}_X(\gamma f)=\operatorname{ord}_Xf;
\quad
[X^k](\gamma f)=\gamma(0)[X^k]f
\quad\text{若 }\operatorname{ord}_Xf\ge k.
\tag{4.3}
$$

因此所有准确前缀核完全相同；交回原整系数源格后，
饱和前缀格也相同。对 $p\ne11$，其第 $k$ 阶 quotient norm
准确相等。该论证只使用 $\gamma(0)$ 为单位，
不要求 $\gamma$ 的高阶系数整。

记变换后的同一个完整矩阵为

$$
\widetilde{\mathcal B}_{k;(j,c)}
=[X^k]\gamma(s(X))X^jV(s(X))^c.
$$

若 $M=k+1-j>0$，则有准确式

$$
\boxed{\quad
\widetilde{\mathcal B}_{k;(j,c)}
=[s^{M-1}]V(s)^cV'(s)Z(s)^{-M}.
\quad}
\tag{4.4}
$$

若 $M\le0$，条目为零。证明是同一个留数换元：

$$
\begin{aligned}
\widetilde{\mathcal B}_{k;(j,c)}
&=\operatorname{Res}_{s=0}
  \gamma(s)V(s)^c\mathcal A(s)^{j-k-1}\mathcal A'(s)\,ds\\
&=\operatorname{Res}_{s=0}V(s)^cV'(s)\mathcal A(s)^{-M}\,ds.
\end{aligned}
$$

这个共同 gauge 消除了 R162(4.1) 显示的 $c/(k-j)$。
它并未消除连接：完整的 $Z^{-M}=p_0^{-M}e^{-MW}$ 仍在式中，
且 $M=k+1-j$ 随原源次数 $j$ 变化。

## 5. 准确的块共振与唯一边界项

令 $M=p^{2a}$、$a\ge1$，并取 $k=j+M-1$。
由 (3.5) 与 $V\in s\mathbb Z_p[[s]]$，

$$
\widetilde{\mathcal B}_{k;(j,c)}
\equiv[s^{M-1}]V^cV'
=\frac{M}{c+1}[s^M]V^{c+1}\pmod p.
\tag{5.1}
$$

式中的有理写法保留了分母 $c+1$。于是，对所有 $c\ge0$，

$$
\boxed{\quad
\widetilde{\mathcal B}_{j+p^{2a}-1;(j,c)}
\equiv(-22)^{p^{2a}}\,
       \mathbf1_{c=p^{2a}-1}\pmod p.
\quad}
\tag{5.2}
$$

确实：

- $c+1<M$ 时，(5.1) 的赋值至少
  $2a-v_p(c+1)\ge1$；
- $c+1>M$ 时，$V^cV'$ 的起阶大于 $M-1$，
  因而 (4.4) 的条目原本就为零；
- $c+1=M$ 时，右边准确为 $[s^M]V^M=(-22)^M$。

故在实际源范围 $0\le c\le j$ 中，
$j<p^{2a}-1$ 的整个次数 $j$ 块在第
$k=j+p^{2a}-1$ 行均被 $p$ 除。
当 $j=p^{2a}-1$ 时，$c=j$ 已经给出一个单位；
更大 $j$ 也必须保留 $c=p^{2a}-1$ 这一列。
不能将“$M$ 是偶次 $p$ 幂”误写成所有源列无条件消失。

## 6. 这条共同关系已付与未付的部分

本篇的赋值及矩阵都是原两条 theta 行的准确输入。
特别是 (4.3) 保证共同 gauge 对全部 $D,k$ 的原饱和
前缀范数无损，(5.2) 也不是任意局部指数模型的类比。

但是同一行 $k$ 中，其他 $j'$ 的真实指数是
$M'=k+1-j'$；它们通常不等于同一个 $p^{2a}$。
(5.2) 只支付指定块，尚未把这些相邻块放在同一个原饱和
前缀中完成联合消元。更重要的是，全部推导不使用
$J'_{17,p}=J'_{34,p}=0$；它不能独自产生只在“所有素数失败”
假设下才出现的严格全素数预算。

仍需对 R159 的真实平面源证明惰性总成本满足
$a_I+2b_I<2$，或找到能等价触及这一门槛的统一前缀关系。
本篇不声称已经得到该不等式。

## 依赖

- [R162 完整固定方程与矩阵](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)；
  本篇只使用其中已经逐式证明的 (1.2)–(1.4)、(2.3) 和原源格。
- [R158 原饱和格与平面输入](2026-11-12-ordinary-falling-factorial-saturated-jets.md)。
- [R159 全跳跃 slopes 与平面门槛](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)。
