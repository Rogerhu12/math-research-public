# R239 附录：两种正权全部出生与任意高度的严格相邻 Gram 系数一

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / root / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：以下完整主定理已证明。实际 MP、Hahn/Schur 恒等式、两端费用和自足 Toda 耦合最大原理共同给出任意高度、整个两值 primitive 空间的严格系数 $1$。更小的最优统一常数仍开，普通 ISP 未完成。
- 输入：[完整固定块 MP](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §10；[两种权全高度二](R239-appendix-two-weight-groups-full-height-two-sharp-primitive-gram-bound.md) §2 的完整正交串；[任意权倒数对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)。


## 主定理：整个实际 primitive 空间的全部相邻阶

取任意有限组大小 $M,N\ge0$、$M+N\ge2$ 和正数 $a,b$，在原正交 Boolean 基上定义
$$
D=a\sum_{j=1}^{M}E_j+b\sum_{j=M+1}^{M+N}E_j.
$$
给定出生 $s\ge0$，令 $h=M+N-2s\ge2$、$K_s=\ker D\cap\mathcal H_s$，并令
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2},\qquad
\Gamma_n=P_{K_s}F_n^{-1}|_{K_s},\qquad0\le n\le h.
$$
$F_n$ 在整个输入层上的逆存在；这一步由有限正权的标准满射阶梯支付，不能先把 $F_n$ 压到 $K_s$ 再取逆。

**对全部 $1\le n<h$，严格有**
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1}.}
\tag{T}
$$
严格性指差在完整 $K_s$ 上正定。结论保留两组的全部表示重数、全部出生和全部高度；允许 $a=b$ 或某组为空。若只需要从任一更长梯读取前几个合法高度，应用其完整高度的结论即可。

相应未除阶乘的真实第一下降比较常数严格小于 $((n+1)/n)^2\le4$，由同一完整 MP 坐标的合法同余得到。这里只覆盖两种权，不将有限两值模型当成全部有限正权或原连续尾。

下面 §§1–6 给全部实际归约及精确端点，§8 完整证明决定性的比较；§7 保留更小最优常数的准确开放问题。

## 1. 真正的双串及完整最小逆

在任意两种正权、任意有限重数的模型中，分别对两个等权组作标准正交升降串分解。每条双串同时约化删除、伴随、所有完整层 Gram 及其完整逆。原 primitive 空间在每个相关双串上为一维；其全部重数保留在正交直和中。

将较短的串长记为 $q$，归一化较长串的权为一，短串权平方为 $z>0$。设相对出生为 $t$，高度为 $h\ge2$，则唯一写成
$$
t=q-\delta,\qquad
L=q+h-2\delta,\qquad
0\le\delta\le\min(q,\lfloor h/2\rfloor).
\tag{1.1}
$$
$L$ 是较长串长度。这个参数区间恰好保证 $L\ge q$ 及双串 primitive 非零。

按完整层取逆后才压缩的约定，令
$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_t}}{(n!)^2},
\qquad
\Gamma_n=P_{K_t}F_n^{-1}|_{K_t},
\qquad0\le n\le h.
$$
记该 primitive 线上的本征值为 $\gamma_n$，$\gamma_0=1$。采用既有完整 MP 稿的共同头坐标 $f(R)=\binom{|R|}{\delta}$，未归一费用准确为
$$
H_n(z)=\min_F
\sum_{\substack{0\le r\le q\\0\le n+r-\delta\le L}}
\frac{\binom qr z^r}{\binom L{n+r-\delta}}|F(r)|^2,
\tag{1.2}
$$
其中
$$
F(r)=\binom r\delta+P(r),\qquad\deg P<\delta,
\quad F(r)=0\text{ 于所有非法 }r.
\tag{1.3}
$$
$\delta=0$ 时 $F=1$。池和头的置换平均保源且不增范数，因此 (1.2) 是整个输入层的最小值；不是限制试探源的上界。原始源归一后
$$
\gamma_n=H_n/H_0,
\qquad
c_n(z):=\frac{\gamma_n^2}{\gamma_{n-1}\gamma_{n+1}}
=\frac{H_n^2}{H_{n-1}H_{n+1}}.
\tag{1.4}
$$

## 2. 全部边段同时保留的 Hahn 归约

对每个 $0\le n\le h$ 定义
$$
u=(\delta-n)_+,\qquad v=(\delta-h+n)_+,\qquad
d=\delta-u-v,\qquad Q=q-u-v,
\tag{2.1}
$$
$$
A=|n-\delta|,\qquad B=|h-n-\delta|.
\tag{2.2}
$$
这里 $u,v$ 至多一个非零，且
$$
Q-d=t\ge0,\qquad A+B+2d=h.
\tag{2.3}
$$

非法低端是 $r=0,\ldots,u-1$，非法高端是 $r=q-v+1,\ldots,q$。故 (1.3) 的全部允许多项式恰为
$$
F(r)=\frac1{\delta!}
\left(\prod_{i=0}^{u-1}(r-i)\right)
\left(\prod_{j=0}^{v-1}(r-q+j)\right)
p(r-u),
\tag{2.4}
$$
其中 $p$ 遍历所有首一的 $d$ 次复多项式。空积为一。这是精确参数化：固定首项与这些强制根后，剩余的 $d$ 个低次参数均保留。

对 $x=0,\ldots,Q$ 写
$$
w_{Q,A,B,z}(x)=z^x(x+1)_A(Q-x+1)_B,
\tag{2.5}
$$
其中 $(y)_j=y(y+1)\cdots(y+j-1)$ 是上升阶乘，$(y)_0=1$。令
$$
\mathfrak h_d(Q,A,B;z)
=\min_{p\text{ 首一},\,\deg p=d}
\sum_{x=0}^{Q}w_{Q,A,B,z}(x)|p(x)|^2.
\tag{2.6}
$$
全部权严格正；$Q\ge d$ 保证该最小范数严格正。

**定理 1。** 所有合法阶，包括两端，均准确满足
$$
\boxed{
H_n(z)=\frac{q!}{L!(\delta!)^2}\,z^u
\mathfrak h_d(Q,A,B;z).
}
\tag{2.7}
$$

证明只需逐项消因子。令 $r=u+x$。将 (2.4) 代入 (1.2)，除去 $|p(x)|^2/\delta!^2$ 后，系数为
$$
\frac{q!}{L!}z^{u+x}
\frac{(n+r-\delta)!\,r!}{(r-u)!^2}
\frac{(L-n-r+\delta)!\,(q-r)!}{(q-r-v)!^2}.
$$
若 $n\ge\delta$，第一商是 $(x+1)_{n-\delta}$；若 $n<\delta$，则 $u=\delta-n$，第一商是 $(x+1)_u$。两者均为 $(x+1)_A$。完全相同的高端核算给第二商 $(Q-x+1)_B$，遂得 (2.7)。

这一归约没有把非法阶乘作形式延拓，也没有在边段保留错误数量的优化参数。

## 3. 完整 Hankel 商及一个有限 Schur 恒等式

对固定 $Q,A,B,z$，定义
$$
Z_k=
\sum_{0\le x_1<\cdots<x_k\le Q}
\prod_{i<j}(x_j-x_i)^2\prod_{i=1}^k w_{Q,A,B,z}(x_i),
\qquad Z_0=1.
\tag{3.1}
$$
Cauchy–Binet 把它准确写成矩矩阵行列式
$$
Z_k=\det\left[\sum_{x=0}^Q x^{i+j}w_{Q,A,B,z}(x)\right]_{i,j=0}^{k-1}.
$$
因而完整首一最小化的 Schur 补给
$$
\boxed{\mathfrak h_d=Z_{d+1}/Z_d.}
\tag{3.2}
$$
$Z_d>0$，包括 $d=0$。这是关于秩变量 $x$ 的 Gram 行列式，不是声称高度序列 $H_n$ 满足全 Hankel 正性。

下面 $s_\lambda$ 表示通常的 Schur 多项式；$c^{[a]}$ 表示把变量 $c$ 重复 $a$ 次。可用半标准表定义，或用 Jacobi–Trudi 行列式
$$
s_\lambda=\det[h_{\lambda_i-i+j}]
$$
定义；$h_r$ 为完全齐次多项式，$h_0=1,h_r=0$ 于 $r<0$。

**有限恒等式。** 对 $1\le k\le Q+1$，
$$
\boxed{
Z_k=
\left(\prod_{j=A}^{A+k-1}j!\right)
\left(\prod_{j=B}^{B+k-1}j!\right)
z^{k(k-1)/2}
 s_{((Q-k+1)^k)}(z^{[A+k]},1^{[B+k]}).
}
\tag{3.3}
$$

证明。令 $T=Q-k+1$。对粒子组 $x_1<\cdots<x_k$，置
$$
\mu_i=x_{k+1-i}-(k-i),\qquad1\le i\le k.
$$
这给 $\mu\subseteq(T^k)$ 的双射，且 $\sum x_i=|\mu|+k(k-1)/2$。Weyl 的有限 Vandermonde 维数式逐因子给
$$
s_\mu(1^{[A+k]})
=\frac{\prod_{i<j}(x_j-x_i)\prod_i(x_i+1)_A}
{\prod_{j=A}^{A+k-1}j!}.
\tag{3.4}
$$
矩形补分区 $\mu^c=(T-\mu_k,\ldots,T-\mu_1)$ 对应反向粒子 $Q-x_k,\ldots,Q-x_1$，所以
$$
s_{\mu^c}(1^{[B+k]})
=\frac{\prod_{i<j}(x_j-x_i)\prod_i(Q-x_i+1)_B}
{\prod_{j=B}^{B+k-1}j!}.
$$
将两式代入 (3.1)。矩形的分支恒等式
$$
s_{(T^k)}(X,Y)=\sum_{\mu\subseteq(T^k)}s_\mu(X)s_{\mu^c}(Y)
\tag{3.5}
$$
遂给 (3.3)。式 (3.5) 可直接把半标准表按两个有序字母表切开；剩余的矩形斜形旋转 $180$ 度并反转有限字母表，得到补分区的表。Schur 对字母的对称性使反转不改值。故这里不需一个新的无限级数恒等式。

由 (2.7)、(3.2)、(3.3)，得到一个已经覆盖所有边段的逐段 Schur 商：
$$
\boxed{
H_n=\frac{q!}{L!(\delta!)^2}\,
z^{u+d}(A+d)!(B+d)!
\frac{s_{(t^{d+1})}(z^{[A+d+1]},1^{[B+d+1]})}
{s_{((t+1)^d)}(z^{[A+d]},1^{[B+d]})}.
}
\tag{3.6}
$$
空分区的 Schur 多项式为一。

## 4. 矩形的秩对偶及全阶固定形状

所需的经典有限维矩形对偶是
$$
\boxed{
\frac{s_{(T^k)}(z^{[a]},1^{[N-a]})}{s_{(T^k)}(1^{[N]})}
=
\frac{s_{(T^a)}(z^{[k]},1^{[N-k]})}{s_{(T^a)}(1^{[N]})},
\qquad0\le a,k\le N.
}
\tag{4.1}
$$
给出其所需的有限维证明，以免把边段当作解析延拓。

令 $P_j$ 为 $\mathbb C^N$ 上前 $j$ 个坐标的正交投影，$U$ 在 $U(N)$ 上按概率 Haar 测度积分。标准矩形 Schur 模的字符恒等式给
$$
\frac{s_{(T^k)}(z^{[a]},1^{[N-a]})}{s_{(T^k)}(1^{[N]})}
=
\int_{U(N)}
\det\!\left(I_k+(z-1)(U^*P_aU)|_{\operatorname{Ran}P_k}\right)^T\,dU.
\tag{4.2}
$$
这里的均值身份可直接如下核验。取
$v=(e_1\wedge\cdots\wedge e_k)^{\otimes T}$，在
$\operatorname{Sym}^T(\bigwedge^k\mathbb C^N)$ 中取其酉轨道的线性包 $V$。
它是最高权 $(T^k)$ 的矩形 Schur 模：最高权空间在外幂张量模型中只有一维；任一与酉作用交换的正交投影把 $v$ 映到其倍数，所以 $v$ 生成的模块不可约。其字符为 $s_{(T^k)}$，维数为 $s_{(T^k)}(1^{[N]})$（有限 Weyl 字符式，亦可由半标准表基得到）。
因此轨道秩一投影的平均与酉作用交换，且迹为一，准确等于 $I_V/\dim V$。对 $I+(z-1)P_a$ 的矩阵系数取迹，外幂行列式公式就给 (4.2)。

Sylvester 身份 $\det(I+XY)=\det(I+YX)$ 把被积行列式换成
$$
\det\!\left(I_a+(z-1)(UP_kU^*)|_{\operatorname{Ran}P_a}\right).
$$
再将 $U$ 换成 $U^*$；Haar 概率不变，便得 (4.1)。$T=0,a=0,k=0$ 的空维情形也是一。这一证明只用有限维酉平均和 Schur 模的字符身份，没有运输原研究中的无限维不变格或范数。

写
$$
\lambda=(t^{\delta+1}),\qquad\mu=((t+1)^\delta).
$$

**定理 2（全阶固定矩形商）。** 对全部 $0\le n\le h$，
$$
\boxed{
H_n(z)=\frac{q!}{L!(\delta!)^2}\,
n!(h-n)!\,z^\delta
\frac{s_\lambda(z^{[n+1]},1^{[h-n+1]})}
{s_\mu(z^{[n]},1^{[h-n]})}.
}
\tag{4.3}
$$
所有分母在 $z>0$ 时严格正。

在 $\delta\le n\le h-\delta$，有 $u=v=0,d=\delta,A+d=n,B+d=h-n$，故这是 (3.6)。
若 $n<\delta$，则 $u=\delta-n,v=0,d=n$，(3.6) 的分子分母分别是
$$
s_{(t^{n+1})}(z^{[\delta+1]},1^{[h-\delta+1]}),
\qquad
s_{((t+1)^n)}(z^{[\delta]},1^{[h-\delta]}).
$$
对二者分别使用 (4.1)。所生的维数常数用有限乘积
$$
D_N(T,k):=s_{(T^k)}(1^{[N]})
=\prod_{i=1}^k\prod_{j=1}^T
\frac{N+j-i}{T+k-i-j+1}
$$
核算。逐因子消去给
$$
\frac{D_{h+2}(t,k+1)}{D_h(t+1,k)}
=\frac{\binom{h+t+1}{t}}{\binom hk}.
\tag{4.4}
$$
所以取 $k=n$ 与 $k=\delta$ 的比值，恰把
$\delta!(h-\delta)!$ 换成 $n!(h-n)!$，给出 (4.3)。

最后，(1.2) 中作 $r\mapsto q-r$ 并对多项式取 $F(r)\mapsto(-1)^\delta F(q-r)$，合法零约束和首项均保持，得到
$$
H_n(z)=z^qH_{h-n}(z^{-1}).
\tag{4.5}
$$
Schur 的齐次性给同一个反转：分子分区次数为 $t(\delta+1)$，分母次数为 $(t+1)\delta$，差为 $t-\delta=q-2\delta$。将已证低端代入 (4.5)，恰恢复 $z^\delta$，证明剩余全部高端。证毕。

## 5. 相邻问题的准确固定形状接口

令
$$
S_i^+(z)=s_\lambda(z^{[i]},1^{[h+2-i]}),\qquad
S_i^-(z)=s_\mu(z^{[i]},1^{[h-i]}),
$$
并定义合法内部的 Turán 比
$$
\mathcal T_i^+=\frac{(S_i^+)^2}{S_{i-1}^+S_{i+1}^+},
\qquad
\mathcal T_i^-=\frac{(S_i^-)^2}{S_{i-1}^-S_{i+1}^-}.
$$
对 $1\le n<h$，(4.3) 准确化成
$$
\boxed{
c_n(z)=
\frac{n(h-n)}{(n+1)(h-n+1)}
\frac{\mathcal T_{n+1}^+(z)}{\mathcal T_n^-(z)}.
}
\tag{5.1}
$$
因此若写
$$
X_n=\frac{(n+1)(h-n+1)}{\mathcal T_{n+1}^+},\qquad
Y_n=\frac{n(h-n)}{\mathcal T_n^-},
$$
则 $c_n=Y_n/X_n$。一般系数 $1$ 的实际相邻比较现在恰为 $Y_n\le X_n$，并没有因两个 Schur 多项式各自为正而自动成立。

相关文献入口：Suvrit Sra，*Monotonicity of Turán-ratios of symmetric polynomials*，v1，2026-10-07，§2，[作者原文](https://suvrit.github.io/papers/sym-turan/sym-turan-v1.pdf)。该文讨论单个固定分区的重复变量 Turán 比。本稿的定理 1、2 及下面端点结论均不引用其新单调性定理作为前提；两个不同矩形比之商由下一节的自足 Toda 计算与耦合最大原理处理，不能只引用各自单调性。

## 6. 全高度的精确权比端点

固定 $q,h,\delta$。记
$$
K=\frac{q!}{L!(\delta!)^2}.
$$
对任意正权有限格点 $w_x=b_xz^x$，$b_x>0$，(3.1) 中 $Z_k$ 的最低次项唯一来自 $x_i=i-1$。因此
$$
\frac{Z_{d+1}}{Z_d}
=(d!)^2 b_d z^d\,(1+O(z)),\qquad z\downarrow0.
\tag{6.1}
$$
这是有限多项式商的严格渐近，余项常数只需对当前固定参数有限；不声称对增长的 $q,h$ 一致。

在 (2.7) 中使用 (6.1)，或直接保留 (2.4) 的全部强制根，可写得更简洁。置
$$
r_n=\min(\delta,h-n).
$$
则
$$
\boxed{
H_n(z)=
\frac{q!\,r_n!(q-r_n)!}
{(\delta!)^2((q-\delta)!)^2
 \binom L{n+r_n-\delta}}
 z^{r_n}(1+O(z)).
}
\tag{6.2}
$$
分母指标总合法：当 $r_n=\delta$ 时为 $n$；否则为 $h-\delta\le L$。

为直接核验系数，最低未被零约束与自由根杀掉的格点恰为 $r_n=u+d=\delta-v$。首一因子在该点的绝对值是
$$
|F(r_n)|=\frac{r_n!(q-r_n)!}{\delta!(q-\delta)!}.
$$
乘以该点的真实二项式权即得 (6.2)。最小化可能使较低点出现小修正；(6.1) 证明这些修正不会改变所列首项。

等价的两段表达式为
$$
H_n(z)\sim
\begin{cases}
\displaystyle\frac{\binom q\delta}{\binom Ln}z^\delta,
&0\le n\le h-\delta,\\[8pt]
\displaystyle\frac{q!\,(h-n)!(q-h+n)!}
{(\delta!)^2((q-\delta)!)^2\binom L{h-\delta}}
z^{h-n},
&h-\delta<n\le h.
\end{cases}
\tag{6.3}
$$
$z\to\infty$ 的完整首项由 (4.5) 得到，特别是
$$
H_n(z)\sim\frac{\binom q\delta}{\binom L{h-n}}z^{q-\delta}
\quad(\delta\le n\le h).
\tag{6.4}
$$
对 $n<\delta$，反转 (6.3) 的第二行给幂 $z^{q-n}$ 和同一显式阶乘系数。

于是全部合法相邻比的低端极限准确为
$$
\boxed{
\lim_{z\downarrow0}c_n(z)=
\begin{cases}
\displaystyle\frac{n(L-n)}{(n+1)(L-n+1)},&n<h-\delta,\\[8pt]
0,&n=h-\delta\quad(\delta>0),\\[4pt]
\displaystyle\frac{(h-n)(q-h+n)}{(h-n+1)(q-h+n+1)},&n>h-\delta.
\end{cases}
}
\tag{6.5}
$$
仅在 $1\le n<h$ 读取各分支。高端为
$$
\boxed{\lim_{z\to\infty}c_n(z)=\lim_{z\downarrow0}c_{h-n}(z).}
\tag{6.6}
$$
过渡阶的零不是源 Gram 被省略造成的：相邻三个真实最小范数的最低 $z$ 次数在此恰产生一个额外正幂。

## 7. 整个两值空间、严格系数一及尚未闭合的最优常数

对任何实际双组大小，§1 的所有双串与全部表示重数同时保留。因而 (4.3)、(5.1)、(6.2)–(6.6) 都可逐块用于整个 primitive 空间，而非只用于原先的一条池固定试探线。

下一节给出自足 Toda 恒等式及耦合最大原理，使用 (5.1) 和 (6.5)–(6.6) 的严格小于一端点，证明全部块的 $c_n(z)<1$。按上述有限正交分解，因而得到整个 primitive 空间上的
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1},\qquad1\le n<h.
$$
这一步保留完整逆与全部表示重数，且不限组大小、出生或高度。

取饱和块 $\delta=0$、组大小 $(q,q+h)$；固定 $n$，令权比趋相应端点再令 $q\to\infty$。由 (6.5)–(6.6)，任何对所有组大小和权比成立的统一上界至少为
$$
\max\left\{\frac n{n+1},\frac{h-n}{h-n+1}\right\}.
\tag{7.1}
$$
已证高度二到四达到对应的严格统一上界；下一节的系数一尚未达到它。一般高度仍需进一步证明
$$
c_n(z)<\max\left\{\frac n{n+1},\frac{h-n}{h-n+1}\right\}
\tag{7.2}
$$
或给出真反例；本稿的端点值不控制内部 $z$，单个 Schur Turán 比的单调性也不控制 (5.1) 的商。

此外，高度序列的全 Hankel 正性早已在两类权的非饱和模型中被排除，不能把 (3.1) 的秩变量 Hankel 行列式误认成所需的高度矩表示。原连续尾的完整窄源、非 primitive 返回成本和普通 ISP 仍保持原来的开放状态。


## 8. 自足 Toda 身份与两个矩形的耦合最大原理

本节所用的单分区 Toda 恒等式见 Suvrit Sra，*Monotonicity of Turán-ratios of symmetric polynomials*，v1，2026-10-07，Lemma 2.1（第2–3页）。为满足本课题对尚未公认预印本的使用要求，以下从有限行列式完整重证该身份；不把其单调性定理作为黑箱。随后比较的是本稿两个不同维数、不同矩形的真实费用。

### 8.1 从有限交替式直接计算 Toda 身份

固定变量数 $N\ge2$ 和补零至 $N$ 项的分区 $\lambda$。为避免与前面的整数 $t=q-\delta$ 混淆，本节用 $\theta=\log z>0$。置
$$
S_i(z)=s_\lambda(z^{[i]},1^{[N-i]}),\qquad
f_i(\theta)=\log S_i(e^\theta),
$$
$$
u_i=2f_i-f_{i-1}-f_{i+1},\quad
\alpha_i=i(N-i),\quad
\kappa(\theta)=\frac1{4\sinh^2(\theta/2)}.
$$
所有 $S_i$ 在正变量上严格正。我们证明
$$
\boxed{f_i''=\alpha_i\kappa(1-e^{-u_i}),\qquad1\le i<N.}
\tag{8.1}
$$
端部 $f_0$ 为常数、$f_N=|\lambda|\theta+f_0$，故二阶导数为零。

令 $a_j=\lambda_{N-j}+j$，$0\le j<N$，则 $a_0<\cdots<a_{N-1}$。设 $D_i(\theta)$ 的第 $j$ 行为
$$
(1,a_j,\ldots,a_j^{N-i-1},\ e^{a_j\theta},a_je^{a_j\theta},\ldots,a_j^{i-1}e^{a_j\theta}).
$$
重复变量的交替式可由 $s_\lambda(x)=\det[x_j^{a_k}]/\det[x_j^k]$ 逐组取相等变量的极限直接得到。把逐次普通导数改成 $(x\partial_x)^r$ 只是各组内的上三角列变换；其对角系数为 $r!x^r$。于是准确有
$$
D_i=C_i e^{i(N-1)\theta/2}
[2\sinh(\theta/2)]^{i(N-i)}S_i(e^\theta),
\qquad
C_i=\prod_{r=0}^{N-i-1}r!\prod_{r=0}^{i-1}r!.
\tag{8.2}
$$
$i=0,N$ 时也是同一有限 Vandermonde 恒等式。特别，$D_i>0$。

定义有限指数和及其 Hankel 行列式
$$
g(\theta)=\sum_{j=0}^{N-1}\frac{e^{a_j\theta}}{\prod_{k\ne j}(a_j-a_k)},\qquad
K_i=\det[g^{(r+s)}]_{r,s=0}^{i-1},\qquad K_0=1.
$$
对 $K_i$ 用 Cauchy–Binet，对 $D_i$ 沿最后 $i$ 列展开，两边的同一 $i$ 元指数子集逐项相同，内部 Vandermonde 配对给符号 $(-1)^{i(i-1)/2}$。因此
$$
K_i=(-1)^{i(i-1)/2}\frac{D_i}{\Delta(a)},\qquad
\Delta(a)=\prod_{j<k}(a_k-a_j)>0.
\tag{8.3}
$$
Hankel 行列式求导时，除最后一行外每一行的导数都与下一行重复，所以只剩最后行升一阶的子式；再按列求导同样只剩最后列升一阶。对相邻的 $(i+1)$ 阶矩阵使用 Desnanot–Jacobi 身份，即得
$$
K_iK_i''-(K_i')^2=K_{i-1}K_{i+1}.
$$
故 $\tau_i=D_i/\Delta(a)=(-1)^{i(i-1)/2}K_i>0$ 满足
$$
(\log\tau_i)''=-\frac{\tau_{i-1}\tau_{i+1}}{\tau_i^2}.
\tag{8.4}
$$
由 (8.2)，$C_{i-1}C_{i+1}/C_i^2=\alpha_i$，幂因子相消后右边为 $-\alpha_i\kappa e^{-u_i}$；左边为 $f_i''-\alpha_i\kappa$。这完整证明 (8.1)。

令 $B_i=\alpha_i e^{-u_i}$，并置 $B_0=B_N=0$。对 (8.1) 作两次相邻差，由 $2\alpha_i-\alpha_{i-1}-\alpha_{i+1}=2$ 得
$$
\boxed{u_i''=\kappa(2-2B_i+B_{i-1}+B_{i+1}).}
\tag{8.5}
$$
这里没有使用关于 $u_i'$ 的符号结论。

### 8.2 两个不同矩形的准确耦合

回到 §§4–5 的两族：正族变量数为 $h+2$、分区为 $(t^{\delta+1})$；负族变量数为 $h$、分区为 $((t+1)^\delta)$。用上标 $+,-$ 区分它们的 $u_i,B_i$。令
$$
X_n=B^+_{n+1}>0\quad(0\le n\le h),\qquad
Y_n=B^-_n>0\quad(1\le n<h),\qquad Y_0=Y_h=0.
$$
§5 已证明实际相邻比恰为 $c_n=Y_n/X_n$。置
$$
v_n(\theta)=\log c_n(e^\theta),\qquad
D_n=Y_n-X_n=X_n(e^{v_n}-1),\quad1\le n<h,
$$
并定义 $D_0=-X_0<0,D_h=-X_h<0$。这里 $D_n$ 是标量差，不是原删除算子。

由于
$$
v_n=\log\frac{n(h-n)}{(n+1)(h-n+1)}+u^+_{n+1}-u^-_n,
$$
两族 (8.5) 中的常数 $2\kappa$ 准确相消，得到封闭的比较式
$$
\boxed{v_n''=\kappa(2D_n-D_{n-1}-D_{n+1}),\qquad1\le n<h.}
\tag{8.6}
$$
即使某个分区为空、其 Turán 比恒一，这个身份仍成立。

在 $\theta=0$，重复变量全为一，两个 Turán 比均为一，所以
$$
v_n(0)=\log\frac{n(h-n)}{(n+1)(h-n+1)}<0.
\tag{8.7}
$$
另一方面，§6 的每个固定参数端点都严格小于一或等于零。对第一分支，$n<h-\delta\le L$ 给两个正真分式；第三分支也有 $0<h-n<\delta\le q$。反转公式给 $z\to\infty$ 的相同结论。因此存在有限 $R>0$，使所有 $v_n(\theta)<0$ 于 $\theta\ge R$；由连续性，也存在 $\varepsilon>0$，使它们于 $[0,\varepsilon]$ 全严格为负。

### 8.3 正部和的凸性排除所有内部反向比较

在任意这样的区间 $[\varepsilon,R]$ 上令
$$
w(\theta)=\sum_{n=1}^{h-1}(v_n(\theta))_+\ge0.
$$
固定一个非零符号不变的局部区间，置 $I_n=\mathbf1_{\{v_n>0\}}$、$I_0=I_h=0$。由 (8.6)，准确有
$$
w''=\kappa\left[
\sum_{j=1}^{h-1}D_j(2I_j-I_{j-1}-I_{j+1})
-D_0I_1-D_hI_{h-1}\right]\ge0.
\tag{8.8}
$$
理由逐项成立：$I_j=1$ 时 $D_j>0$、括号系数非负；$I_j=0$ 时 $D_j\le0$、括号系数非正。两个端部的额外项也非负，因为 $D_0,D_h<0$。

零点不会破坏此不等式。对光滑函数 $v$，凸近似 $\varphi_\epsilon\to(\cdot)_+$ 的链式公式
$$
(\varphi_\epsilon(v))''
=\varphi_\epsilon'(v)v''+\varphi_\epsilon''(v)(v')^2
$$
中第二项非负；取极限得到 $(v_+)''\ge\mathbf1_{\{v>0\}}v''$ 的分布式。等价地，跨零时正部的一阶导数只增加非负跳跃。故 (8.8) 在整个区间以分布意义成立，$w$ 为凸函数。

但 $w(\varepsilon)=w(R)=0$。凸性给 $w\le0$，与 $w\ge0$ 合并，得到 $w\equiv0$。所以全部 $v_n\le0$，即 $c_n\le1$。

严格性也由同一真实边界给出。若某个内部点 $\theta_0>0$ 有 $v_n(\theta_0)=0$，它是最大值，故 $v_n''(\theta_0)\le0$。此时 $D_n=0$ 而邻项均非正；(8.6) 迫两邻项也为零。逐邻传播最终遇到严格负的 $D_0$ 或 $D_h$，矛盾。于是
$$
\boxed{c_n(z)<1\quad(z>1,\ 1\le n<h).}
$$
$z=1$ 已由 (8.7) 给严格性；$0<z<1$ 使用 $c_n(z)=c_{h-n}(z^{-1})$。这完成全部正权比的比较。

### 8.4 回到完整源与原权范围

每个双串的源 Gram 都在 §1 保留，且实际全逆按两个组的正交约化分解。比较不是只在某个选定源上成立，而是在每条实际 primitive 线及其全部重数上成立。有限正交直和遂给主定理 (T)。

若令未归一阶乘的原像 Gram 为 $\widetilde H_n=(n!)^{-2}\Gamma_n$，则 (T) 准确等价于
$$
\widetilde H_n\widetilde H_{n+1}^{-1}\widetilde H_n
\prec\left(\frac{n+1}{n}\right)^2\widetilde H_{n-1}.
$$
这正是同一 primitive 坐标中的真实第一下降比较。没有改变内积，没有先压缩再取逆，也没有从两种权推断任意多种权。原连续尾的通用有限权归约仍要求覆盖全部有限正权模型；本定理完成其中全部两值模型的任意高度部分。


## 复算入口

[有限对称层的精确有理MP与固定Schur商对照](../notes/2026-11-13-two-weight-all-heights-exact-mp-schur-check-0c.py)保存参数与生成步骤：h=2..7、全部δ、q=δ/δ+1/δ+3、a=1/2,1,3及全部n共963例。它复查恒等式，不承担任意参数定理的证明；主定理由上述完整代数和最大原理证明。
