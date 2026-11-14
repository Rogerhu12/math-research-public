# 真实 CM 图形的全深度分母账本与统一 jet 基线

日期：2026-11-12。**已证明，独立复核通过。** 本篇从 R170 的
实际 CM 递推出发，把所有旧分母的非线性传播一并计入，得到全部阶数、
全部次数源及真实饱和前缀的统一上界。它不使用原两中央失败条件，
因而仍不是 R159 所要求的严格收益。

## 1. 实际图形及准确递推输入

仍取同一平面 $a=\vartheta^4,b=\sigma^4$，在首项一的输出参数 $b$
中写

$$
a=f(b)=1+\sum_{k\ge1}c_kb^k.
$$

固定惰性 $p\ge7$，令

$$
r=(p+1)/4,\qquad R=r(p-1)=(p^2-1)/4.
$$

R170 的全部 Gaussian 乘法已经给出：

1. 若 $k\not\equiv r\pmod R$，则 $c_k$ 是
   $c_1,\ldots,c_{k-1}$ 的 $\mathcal O_{\mathbb Q_p(i)}$-整多项式。
2. 若 $k\equiv r\pmod R$，则 $pc_k$ 是相同先前系数的整多项式。
3. 每个出现的单项式 $\prod_jc_{i_j}$ 满足 $i_j<k$ 及
   $\sum_j i_j\le k$。重复因子按重数计数。

这些是原 $F_\beta$ 的系数方程，包含实际切向特征值 $\beta^4$ 和
横向特征值 $N\beta$；没有把分子替换为任意自由递推。
低阶 $c_i$ 在 $i<r$ 时整，首个 $c_r$ 的赋值恰为 $-1$。

## 2. 同时控制全部分拆的成本函数

对整数 $k\ge0$ 置 $n=\lfloor k/r\rfloor$，定义

$$
\boxed{\quad
e_p(k)=
\begin{cases}
0,&n=0,\\
n+\left\lfloor\dfrac{n-1}{p-1}\right\rfloor,&n\ge1.
\end{cases}
\quad}
\tag{2.1}
$$

此函数单调，且对任意非负整数 $i_1,\ldots,i_m$ 有

$$
\sum_j e_p(i_j)\le e_p\left(\sum_j i_j\right).
\tag{2.2}
$$

更准确地，删去 $i_j<r$ 的零成本因子后，若还剩 $q\ge1$ 个因子，
令 $n_j=\lfloor i_j/r\rfloor\ge1$、$N=\sum_jn_j$，则

$$
\sum_j e_p(i_j)
=N+\sum_j\left\lfloor\frac{n_j-1}{p-1}\right\rfloor
\le N+\left\lfloor\frac{N-q}{p-1}\right\rfloor.
\tag{2.3}
$$

因为 $N\le\lfloor(\sum i_j)/r\rfloor$ 且 $q\ge1$，(2.2) 随即成立。
若没有正成本因子，结论显然。这一估计保留了乘积中各个旧分母，
不是仅数一数新的共振位置。

## 3. 全部系数的统一界

**命题。** 对每个 $k\ge0$，准确原图形满足

$$
\boxed{\qquad v_p(c_k)\ge-e_p(k).\qquad}
\tag{3.1}
$$

对 $c_0=1$ 按零成本理解。证明按 $k$ 归纳。
非共振时，用第 1 节的整多项式以及 (2.2) 即得。

共振时写

$$
k=r\{1+t(p-1)\},\qquad n=1+t(p-1),\qquad t\ge0.
$$

此时 $e_p(k)=n+t$。必须证明在除这一次 $p$ 之前，每个先前系数
单项式的成本至多 $n+t-1$。

若有至少两个正成本因子，(2.3) 给

$$
\sum_j e_p(i_j)
\le n+\left\lfloor\frac{n-2}{p-1}\right\rfloor
=n+t-1.
\tag{3.2}
$$

若只有一个正成本因子 $c_i$，因 $i<k$ 且 $k$ 是 $r$ 的倍数，
$\lfloor i/r\rfloor\le n-1$。对 $t\ge1$，其成本甚至至多
$n+t-2$。对首个共振 $t=0$，所有 $i<r$ 都是零成本，
本来就没有正成本因子。没有正成本因子时成本为零。

因此所有情况都在一次除 $p$ 前留有至少一层余量，除后得到 (3.1)。
这一步处理了所有共振，而非只到第二个共振之前。未分歧扩域不改变
有理系数 $c_k$ 的 $p$ 赋值，故结论回到 $\mathbb Q_p$ 成立。

前两段的成本为

$$
e_p(k)=\lfloor k/r\rfloor\quad(k<pr),\qquad
e_p(pr)=p+1.
\tag{3.3}
$$

而一般有

$$
e_p(k)\le\frac{p}{p-1}\frac{k}{r}
                 =\frac{4p}{p^2-1}\,k.
\tag{3.4}
$$

这与旧 sigma 半径中的高度二成本一致，但这里是直接由同一个实际
图形和全部非线性递推推出的全阶系数账本。

## 4. 第二个共同共振的成本确实达到 p+1

记

$$
t(s)=\log a(s)=W(s)/17,\qquad
\tau_p=p[s^r]t(s)\pmod p\ne0.
$$

R171 的实际 Lagrange 公式为

$$
c_n=\frac1{1-n}[s^n]\exp((1-n)t(s))\qquad(n\ne1).
\tag{4.1}
$$

在所需次数 $\le pr<p^2$ 内，写

$$
t=t_{<r}+T/p,\qquad
t_{<r}\in s\mathbb Z_p[s],\quad
T\in s^r\mathbb Z_p[[s]],\quad [s^r]T\equiv\tau_p.
$$

这里只需要截断到 $pr$；$T$ 在这个范围的整性由 R163 的准确赋值
公式保证。令 $n=pr$、$c=1-pr\in\mathbb Z_p^\times$。则

$$
c_n=\frac1c[s^{pr}]
\exp(c t_{<r})
\sum_{q=0}^{p}\frac{c^qT^q}{p^q q!}.
\tag{4.2}
$$

当 $q=p$ 时，$T^p$ 的最低次数已经是 $pr$，因此这一项的贡献为
$c^{p-1}([s^r]T)^p/(p^p p!)$。乘 $p^{p+1}$ 后约化，用 Wilson
$(p-1)!\equiv-1$ 以及费马同余得到 $-\tau_p$。

其余 $q<p$ 项严格高至少一层。具体地，对任意整多项式
$A\in s\mathbb Z_p[s]$，指数级数的次数 $m$ 系数赋值至少
$-\lfloor m/(p-1)\rfloor$：其第 $j$ 个指数项满足 $j\le m$，
而 $v_p(j!)\le j/(p-1)$。
在 (4.2) 的该项中，剩余次数至多 $(p-q)r$，$q!$ 是单位，故乘
$p^{p+1}$ 后的赋值至少

$$
p+1-q-\left\lfloor\frac{(p-q)r}{p-1}\right\rfloor\ge1,
$$

因为 $r<(p-1)$。因此

$$
\boxed{\quad
p^{p+1}c_{pr}\equiv-\tau_p\not\equiv0\pmod p,
\qquad v_p(c_{pr})=-(p+1).
\quad}
\tag{4.3}
$$

故 (3.3) 在第二个共同共振上准确取到；把“每个共振只除一次 $p$”
误读成“所有系数只会有一层分母”会漏掉这里的 $p$ 个旧因子。
本篇没有声称 (3.1) 在其余所有位置都最优。

独立的有限校准直接从 $a=\exp(W/17)$、$b=sa$ 作真正的有理逆级数，
得到 $v_7(c_{14})=-8$、$v_{11}(c_{33})=-12$，与 (4.3) 一致；
对两素数至 $k=60$ 的全部实际系数也满足 (3.1)。这些数值只核查
新的共振端点，统一证明是上面的整递推与 (4.2)。

## 5. 从全部系数到全部真实前缀 jet

令 $E_D^{ab}=\mathbb Z_p[a,b]_{\le D}$，取任意源系数范数至多一的
$H$。在 $b$ 参数下，$H(f(b),b)$ 的第 $k$ 个系数是若干
$\prod c_{i_j}$ 的整线性组合，各单项满足 $\sum i_j\le k$。
因此 (2.2)、(3.1) 同时给出

$$
v_p([b^k]H(f(b),b))\ge-e_p(k)
\qquad\text{对所有 }D,k,H.
\tag{5.1}
$$

再把源限制到同一个实际饱和前缀核

$$
S_{D,k}=
E_D^{ab}\cap\{H:\operatorname{ord}_bH(f(b),b)\ge k\},
$$

得到准确的算子范数上界

$$
\boxed{\quad
\|\varphi_{D,k}^{ab}\|_p\le p^{e_p(k)}
\qquad(D,k\ge0).
\quad}
\tag{5.2}
$$

由于 $b(w)=w+O(w^2)$，在上述前缀核上第一个非零系数不变，
所以 (5.2) 也是真实 $w$ 平凡化中的 jet 范数。
这里只在消去全部较低阶之后运输该行；没有宣称未消前缀的所有
$w$ 系数自动满足相同的逐项界。

R167 的固定源嵌入又给原 $\mathcal A,B$ 全部前缀的相同上界
（惰性 $p\ge7$ 自动不是五）：

$$
\|\varphi_{D,k}^{\mathcal A,B}\|_p
\le\|\varphi_{17D,k}^{ab}\|_p\le p^{e_p(k)}.
\tag{5.3}
$$

这是无条件、真正对所有 $D,k$ 的共同上界。系数极点的精确等式
(4.3) 本身不能作为饱和核上范数的相反方向下界。

## 6. 实际全素数总成本与还缺的改善

若 $r>k$，则 $e_p(k)=0$。因此对惰性好位，由 (3.4) 有

$$
\sum_{p\equiv3\ (4)}\log^+\|\varphi_{D,k}\|_p
\le4k\sum_{\substack{p\le4k-1\\p\equiv3\ (4)}}
                      \frac{p\log p}{p^2-1}
=2k\log k+O(k).
\tag{6.1}
$$

最后一步仅用固定模数四的素数定理及分部求和：
$\sum_{p\le x,p\equiv3(4)}\log p/p=\tfrac12\log x+O(1)$，
而 $p/(p^2-1)-1/p=O(p^{-3})$ 给绝对收敛的误差。
普通处已有全部 jet 范数至多一，固定坏位另由 R159 的
$O(k+D)$ 成本处理。

(6.1) 给的是 $a_I=0,b_I=2$ 的基线。R159 对真实二维、阶
$\rho=1/2$ 平面的严格条件要求 $a_I+2b_I<2$，并首先需要
$b_I<2$；故这个基线本身不足。

目前已经支付的是“全部共振、全部旧因子、全部真实前缀”的
无条件成本。接下来必须使用原两个中央条件，在同一个源格上
证明确实更好的次数相关估计，或转而给原 Heegner 两标量的无穷非零。
不能把 (4.3) 的已知非中央分母当作中央斜率非零证书。

## 依赖和独立核查

- [R170 的原 CM 整映射与加权递推](2026-11-12-full-cm-theta-plane-and-sparse-resonance.md)。
- [R171 的真实逆图形与第一段传播](2026-11-12-theta-graph-nonlinear-propagation-and-common-blocks.md)。
- [R163 的全部相位赋值](2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)。
- [R167 的整源比较](2026-11-12-closed-theta-sigma-plane-and-integral-dynamics.md)。
- [R159 的全部跳跃斜率标准](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)。
- explicit_curve 独立核定了 (2.3)、所有共振端点、单因子／多因子的
  一层余量以及真实前缀下的参数运输。第二共振 (4.3) 用独立有理
  逆级数核对了两个边界样例。
