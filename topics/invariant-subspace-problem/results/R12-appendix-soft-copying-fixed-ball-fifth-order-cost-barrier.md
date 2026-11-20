# R12 附录：复软复制返回非零球的五次费用下界

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：下列最优成本及五次下界均已证明。** 这是对硬截断复制机制的完整扩展：允许任意有界复相位、软截断、有界放大，以及按同一真实输入自适应选择各算子。只要全部算子保持复制结构、普通算子范数一致有界，并使递推返回同一个不含零的固定闭球，其累计对数 Deddens 成本仍有五次下界。本文不把这一结论扩大到任意 Deddens 选择或任意源依赖重排。

内部对象见 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 与 [Deddens 完整边界](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md)。硬截断原型见 [硬复制费用附录](R12-appendix-adaptive-hard-cut-copying-fifth-order-cost-barrier.md)。以下重写所需全部核心证明。

## 1. 原权、全部复制算子与主定理

令

$$
H=L^2(\mathbb Z_2,\mu),\qquad Uf(y)=f(y-1),\qquad A=M_wU,
$$

$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=e^{-L_j},
$$

$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad\alpha_0=e^{-20}.
\tag{1.1}
$$

对任意有界可测复函数 $q$，定义

$$
R_q=\alpha_0^{-1}(I+U)P_{\rm odd}M_q,\qquad
p(z)=q(2z-1).
\tag{1.2}
$$

$q$ 在偶数上的取值不影响 $R_q$。Deddens 最优常数记为

$$
c_A(X)=\inf\{C:\|A^\ell Xf\|\le C\|A^\ell f\|,
\ \ell\ge1,\ f\in H\},
\tag{1.3}
$$

并在不存在有限常数时记为无穷。

**精确单步公式：**

$$
\boxed{\|R_q\|=\frac{\sqrt2}{\alpha_0}\|p\|_\infty,}
\tag{1.4}
$$

$$
\boxed{c_A(R_q)=
\operatorname*{ess\,sup}_{z}
|p(z)|\sqrt{\alpha_0^{-2}+w(2z)^{-2}}.}
\tag{1.5}
$$

后式在零点外理解，其单点取值不影响本质上确界。因此

$$
R_q\in\mathcal D_A
\iff p(z)/w(2z)\in L^\infty,
\qquad |p(z)|\le c_A(R_q)\alpha_{1+v_2(z)}
\quad\text{a.e.}
\tag{1.6}
$$

现在取任意序列 $R_{q_i}\in\mathcal D_A$，允许它按全部此前真实输入与输出自适应选择，并令

$$
f_i=R_{q_i}Af_{i-1}\quad(i\ge1).
\tag{1.7}
$$

假设存在有限 $K$ 使 $\|p_i\|_\infty\le K$；由 (1.4)，这恰是复制算子的普通算子范数一致有界。置 $K_0=\max(1,K)$。

**主定理。** 若存在 $f_*\ne0$ 和 $0<r<\|f_*\|$，使全部 $f_i$（$i\ge1$）属于同一个闭球 $B(f_*,r)$，则存在 $0<\rho\le1$、$0<\delta<1$，使每个 $n\ge1$ 都满足

$$
\boxed{
\sum_{i=1}^n\log c_A(R_{q_i})
\ge
\frac{20\delta^5}{(1-\delta)^4}n^5
+n\log\rho
-n(n-1)\log K_0.}
\tag{1.8}
$$

这些常数依赖固定球、初始向量与统一普通范数界，不依赖 $n$。有界放大只产生二次修正，不能抵消五次项。

## 2. 单步最优成本的直接证明

在每个奇输入格 $2z-1$，$R_q$ 把输入送到奇输出 $2z-1$ 与偶输出 $2z$，两个系数都为 $\alpha_0^{-1}p(z)$。不同输入的输出对互不相交，因此直接得到 (1.4)。

令

$$
h_\ell(x)=\prod_{b=1}^{\ell}w(x+b),\qquad
\|A^\ell f\|^2=\int h_\ell(x)^2|f(x)|^2\,d\mu(x).
\tag{2.1}
$$

在这些加权范数中，上述奇输入列的两个系数为

$$
\alpha_0^{-1}p(z),\qquad
\alpha_0^{-1}p(z)\,
\frac{h_\ell(2z)}{h_\ell(2z-1)}.
$$

而

$$
\frac{h_\ell(2z)}{h_\ell(2z-1)}
=\frac{w(2z+\ell)}{w(2z)}
\quad\text{a.e.}
\tag{2.2}
$$

分子至多 $\alpha_0$。当 $\ell$ 为奇数，特别是 $\ell=1$ 时，分子恒为 $\alpha_0$。由于各列的输出对不交，加权算子的范数正好是列范数的本质上确界。因此对全部 $\ell$ 的最佳常数已在 $\ell=1$ 取到，恰为 (1.5)。这也证明 (1.6)，没有将复相位替换成正系数。

## 3. 同一初始输入的精确乘积

置

$$
g_i(z)=f_i(2z),\qquad g_0(z)=f_0(2z).
$$

由奇数权等于 $\alpha_0$，与 (1.2)、(1.7) 逐项计算得

$$
g_i(z)=p_i(z)g_{i-1}(z-1),\qquad
f_i(2z+1)=g_i(z+1).
\tag{3.1}
$$

因此对于 $s=1,2$，

$$
\|f_i\|_s=\|g_i\|_s.
\tag{3.2}
$$

令

$$
P_n(x)=\prod_{i=1}^n p_i(x+i).
\tag{3.3}
$$

从 (3.1) 递推可得

$$
g_n(z)=g_0(z-n)P_n(z-n),
\qquad
\|f_n\|_s=\|g_0P_n\|_s
\quad(s=1,2).
\tag{3.4}
$$

全部 $P_n$ 都乘在同一个真实 $g_0$ 上。不存在每步重新挑一个便宜输入的步骤。

## 4. 固定非零球给正测的大乘积集合

令 $M=\|f_*\|+r$，$d=\|f_*\|(\|f_*\|-r)>0$。对球内每个 $f_i$，

$$
\|f_i\|_2\le M,\qquad
\operatorname{Re}\langle f_i,f_*\rangle\ge d.
\tag{4.1}
$$

取一个有界函数 $h$，使 $\|h-f_*\|_2\le d/(2M)$。则

$$
\operatorname{Re}\langle f_i,h\rangle\ge d/2,
\qquad
\|f_i\|_1\ge a_1:=\frac{d}{2\|h\|_\infty}>0.
\tag{4.2}
$$

这一步只用有界函数在 $L^2$ 中稠密，不要求原中心或输入有界。

$g_0$ 不可能为零，否则 (3.1) 使所有输出为零。选择 $0<\rho\le1$，使

$$
\rho\|g_0\|_1\le a_1/2.
$$

定义

$$
S_n=\{x:|P_n(x)|\ge\rho\}.
\tag{4.3}
$$

由 (3.4)、(4.2)，有

$$
\int_{S_n}|g_0P_n|\,d\mu
\ge a_1-\rho\|g_0\|_1\ge a_1/2.
$$

再由 $\|g_0P_n\|_2\le M$ 及 Cauchy–Schwarz，

$$
\mu(S_n)\ge\left(\frac{a_1}{2M}\right)^2.
\tag{4.4}
$$

适当减小右端后固定 $0<\delta<1$。这一正测下界不使用任何未知尾速率。

因为每个 $|p_i|\le K_0$，在 $S_n$ 上对全部 $1\le i\le n$ 有

$$
|p_i(x+i)|\ge \theta_n,\qquad
\theta_n:=\rho K_0^{-(n-1)}.
\tag{4.5}
$$

## 5. 从软权阈值到真实 dyadic 计数

记 $c_i=c_A(R_{q_i})$。球条件保证 $c_i>0$。对固定 $n$ 和每个 $i\le n$，令 $j_i^{(n)}$ 为使

$$
c_i\alpha_{j+1}<\theta_n
\tag{5.1}
$$

成立的最小整数 $j\ge0$。由于 $\alpha_j\to0$，该整数存在。

在 $z\in2^{j_i^{(n)}}\mathbb Z_2$ 上，由 (1.6)，

$$
|p_i(z)|\le c_i\alpha_{j_i^{(n)}+1}<\theta_n
\quad\text{a.e.}
$$

所以 (4.5) 表明 $S_n$ 几乎处处避开

$$
-i+2^{j_i^{(n)}}\mathbb Z_2.
\tag{5.2}
$$

因此这些圆柱的并集测度不超过 $1-\delta$。正测的 $S_n$ 还排除 $j_i^{(n)}=0$，因为深度零圆柱是整个空间。由最小性，

$$
c_i\alpha_{j_i^{(n)}}\ge\theta_n,\qquad
\log c_i\ge L_{j_i^{(n)}}+\log\theta_n.
\tag{5.3}
$$

这里的深度可以依赖 $n$；以下计数只对固定 $n$ 的有限族进行，所以没有把它们误当成预先固定的序列。

从 (5.2) 的有限族中取最大且互不相交的圆柱 $D_1,\ldots,D_Q$，设其测度为 $u_t$。每个 $D_t$ 是原族中的一个圆柱，并且

$$
\sum_tu_t\le1-\delta.
$$

它们覆盖全部整数点 $-1,\ldots,-n$。一个测度为 $u_t=2^{-k_t}$ 的同余类，在这 $n$ 个连续整数中至多有 $nu_t+1$ 个点。因此

$$
n\le n\sum_tu_t+Q,\qquad Q\ge\delta n.
\tag{5.4}
$$

由于 $u\mapsto u^{-4}$ 凸，

$$
\begin{aligned}
\sum_{i=1}^n16^{j_i^{(n)}}
&\ge\sum_tu_t^{-4}\\
&\ge\frac{Q^5}{(\sum_tu_t)^4}
\ge\frac{\delta^5n^5}{(1-\delta)^4}.
\end{aligned}
\tag{5.5}
$$

原公式 (1.1) 给 $L_j\ge20\,16^j$：$j=0$ 为等号；对 $j\ge1$，用 $90\,8^j\le45\,16^j$ 可得

$$
L_j-20\,16^j
\ge\frac{85}{3}16^j+300\,2^j-\frac{850}{3}>0.
$$

将 (5.3)、(5.5) 求和，并代入
$\log\theta_n=\log\rho-(n-1)\log K_0$，即得 (1.8)。

所有算子不等式只需在一个共同满测集上使用。所构造圆柱的中心仍是准确的整数 $-i$；在原软权的零测例外上如何选代表不影响测度计数。

## 6. 收缩软权的更弱假设

若所有 $|p_i|\le1$，则无需固定球，只假设

$$
\inf_n\|f_n\|_2\ge a>0
\tag{6.1}
$$

也足够。选 $0<\rho\le1$ 使 $\rho^2\|g_0\|_2^2\le a^2/2$。由 (3.4)，集合 $S_n=\{|P_n|\ge\rho\}$ 上的 $|g_0|^2$ 积分至少为 $a^2/2$。固定 $g_0$ 的积分绝对连续性因此给 $\mu(S_n)\ge\delta>0$。

由于每个因子至多一，$S_n$ 上各 $|p_i(x+i)|\ge\rho$。§5 可取不依赖 $n$ 的阈值 $\theta_n=\rho$，于是

$$
\sum_{i=1}^n\log c_i
\ge\frac{20\delta^5}{(1-\delta)^4}n^5+n\log\rho.
\tag{6.2}
$$

这包括任意收缩硬 cut 和软 cut，以及任意复相位。

## 7. 与原幂预算的比较及剩余范围

由原连续区间的 $2$-进阶计数，

$$
-\log\|A^n\|
=nL_0+\sum_{r\ge1}(L_r-L_{r-1})
\left\lfloor\frac n{2^r}\right\rfloor.
$$

若 $k=\lfloor\log_2n\rfloor$，用 $L_r\le100\,16^r$（$r\ge1$）得到

$$
-\log\|A^n\|
\le20n+100n\sum_{r=1}^k8^r
\le\frac{940}{7}n^4.
\tag{7.1}
$$

该范数公式的等号在 $0$ 的充分小正测邻域上取得，不是单点上确界。

对递推 (1.7)，标准 Deddens 移动次序给

$$
\|f_n\|\le
\|R_{q_n}\|
\left(\prod_{i=1}^{n-1}c_i\right)
\|A^n\|\,\|f_0\|.
\tag{7.2}
$$

对 $n\ge2$，固定球还给 $\|R_{q_n}\|\ge(\|f_*\|-r)/(\|A\|M)>0$，所以不能靠最后一个普通算子范数趋零抵消累计费用。将 (1.8) 用于前 $n-1$ 步，五次项压过 (7.1) 的四次项与有界放大的二次修正。故这个统一有界复制家族不能以 (7.2) 得到趋零的矛盾预算。

这并不声称真实输出范数发散；(7.2) 是一个可能很大的上界。本文证明的是：只在该复制家族内软化 cut、调整复相位、进行有界放大或自适应选深度，都不能完成所需费用桥。正向推进必须使用不同的来源重排或其他结构；任意有限头下三角选择和一般 Deddens 选择仍不在本稿的排除范围内。
