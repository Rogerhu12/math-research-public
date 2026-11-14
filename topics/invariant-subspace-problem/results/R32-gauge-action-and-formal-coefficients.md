# R32：等距圆作用、唯一形式系数与有界除法障碍

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94。

**状态：已证明的中间结论。** 精确描述具体 odometer 的多项式范数闭包中的系数与有限阶商代数。每个非零元素有有限首阶，代数没有零因子；但这些事实不意味着其每个非零元素作为 Hilbert 空间上的算子都单射或值域稠密。后者仍未证明。本条还给出首阶为一却不能在该代数内有界除以 $A$ 的明确元素。

**文献定位。** 圆作用用于单生成算子代数的 Fourier 唯一性与逼近，是已有一般方法：Justin R. Peters, *Singly generated radical operator algebras*, New York J. Math. 30 (2024), 398–421，§2.1 的 Lemma 2.3、Proposition 2.4；§3 还处理加权移位代数的无零因子性质。[出版社页面](https://nyjm.albany.edu/j/2024/30-15.html)，[原文](https://nyjm.albany.edu/j/2024/30-15v.pdf)。本轮核读了这些段落；下文给出本模型的作用实现和自含证明，不主张通用机制的新颖性，也不把该文关于特殊移位表示的结论直接移用于当前 Haar 表示。

## 1. 两个代数与圆作用

沿用 R9 的

$$
(Af)(y)=w(y)f(y-1),\qquad H=L^2(\mathbb Z_2,\mu),
$$

以及 R13 的 $W_n=\|A^n\|>0$。记

$$
\mathcal C=C^*(I,A),\qquad
\mathcal A=\overline{\{p(A):p\in\mathbb C[z]\}}^{\|\cdot\|}.
$$

$\mathcal A$ 是含单位的交换 Banach 代数，而 $\mathcal C$ 还包含伴随。下面不需要预先使用 $\mathcal C$ 的 UHF 识别。

对每个 $2$ 的幂阶单位根 $\zeta=e^{2\pi i r/2^m}$，令

$$
\chi_\zeta(y)=e^{2\pi i r T_m(y)/2^m},\qquad
(V_\zeta f)(y)=\chi_\zeta(y)f(y),
$$

其中 $T_m(y)=y\bmod2^m$。这是一个单位模字符，$V_\zeta$ 酉，且

$$
V_\zeta A V_\zeta^*=\zeta A.
\tag{1.1}
$$

直接验证即可：$\chi_\zeta(y)\overline{\chi_\zeta(y-1)}=\chi_\zeta(1)=\zeta$。

**命题 1.1。** 存在范数连续的等距圆作用

$$
\gamma_\zeta:\mathcal C\longrightarrow\mathcal C,\qquad
\gamma_\zeta(A)=\zeta A,\quad \zeta\in\mathbb T.
\tag{1.2}
$$

每个 $\gamma_\zeta$ 是 $*$-自同构，保持 $\mathcal A$。

**证明。** 先在 $A,A^*$ 的有限 $*$-多项式上，按 (1.2) 及 $\gamma_\zeta(A^*)=\bar\zeta A^*$ 代入。对稠密的 dyadic 单位根，(1.1) 表明它保持范数，因而不依赖多项式表示。对任意 $\zeta$ 取这些单位根的极限；有限多项式关于 $\zeta$ 连续，故同样保持范数，并且仍不依赖表示。于是唯一延伸到 $\mathcal C$，其逆为 $\gamma_{\bar\zeta}$。乘法、伴随及群作用关系从稠密多项式传递。

对任意 $B\in\mathcal C$，先用有限 $*$-多项式在范数上逼近，再用等距性控制逼近误差，即得 $\zeta\mapsto\gamma_\zeta(B)$ 的范数连续性。解析多项式在该作用下仍解析，故 $\mathcal A$ 被保持。证毕。

这并未声称对每个非 dyadic 的 $\zeta$ 都已在此具体表示中找到一个实现它的酉算子；证明只需要代数上的等距作用。

## 2. Fourier 系数、Fejér 逼近与唯一性

定义范数积分

$$
\Phi_n(B)=\frac1{2\pi}\int_0^{2\pi}
e^{-int}\gamma_{e^{it}}(B)\,dt,\qquad n\in\mathbb Z.
\tag{2.1}
$$

范数连续性使这个积分存在，且 $\|\Phi_n(B)\|\le\|B\|$。

**定理 2.1。** 对每个 $B\in\mathcal A$，存在唯一复数列 $(c_n(B))_{n\ge0}$，使

$$
\Phi_n(B)=
\begin{cases}
c_n(B)A^n,&n\ge0,\\
0,&n<0.
\end{cases}
\tag{2.2}
$$

并有

$$
|c_n(B)|W_n\le\|B\|,
\tag{2.3}
$$

$$
\sigma_N(B):=\sum_{n=0}^{N}
\left(1-\frac n{N+1}\right)c_n(B)A^n
\longrightarrow B\quad\text{于算子范数}.
\tag{2.4}
$$

**证明。** 对有限解析多项式，(2.2) 由 Fourier 正交性成立。因为 $\mathbb C A^n$ 是闭的一维子空间，范数逼近和 $\Phi_n$ 的连续性将结论推广到 $\mathcal A$；$A^n\ne0$ 保证标量唯一。(2.3) 由积分范数界得到。

式 (2.4) 等于用 Fejér 核对 $\gamma_{e^{it}}(B)$ 卷积并在单位元处取值。为明确所需逼近事实，Fejér 核非负、积分为一，其在任意不含 $0$ 的闭弧上的积分趋零。给定误差 $\epsilon>0$，先由范数连续性选近零小弧，使 $\|\gamma_{e^{it}}(B)-B\|<\epsilon$；该弧上的积分误差至多 $\epsilon$，其余部分至多 $2\|B\|$ 乘趋零的核质量。因此卷积按范数趋于 $B$。只有非负阶 Fourier 项存在，正好得到 (2.4)。证毕。

特别地，所有 $c_n(B)$ 都为零时，$B=0$。不存在非零的“所有形式系数都消失”的元素。这里的形式幂级数不必在任何非零标量圆盘内收敛；(2.4) 是带权算子范数结论，不是普通解析函数的收敛性声明。

## 3. 形式级数乘法、首阶与单点谱

**命题 3.1。** 对 $B,D\in\mathcal A$，

$$
c_n(BD)=\sum_{j=0}^n c_j(B)c_{n-j}(D).
\tag{3.1}
$$

因此

$$
B\longmapsto\sum_{n\ge0}c_n(B)z^n
\tag{3.2}
$$

是到形式幂级数代数 $\mathbb C[[z]]$ 的单射代数同态。

**证明。** 用 (2.4) 同时逼近两个因子；乘法在范数上连续，而每个固定阶的系数泛函由 (2.3) 连续。在有限多项式上应用通常的卷积公式后取极限，固定 $n$ 只涉及有限个系数，得到 (3.1)。单射性来自定理 2.1。证毕。

若 $B\ne0$，定义有限整数

$$
\operatorname{ord}(B)=\min\{n:c_n(B)\ne0\}.
$$

由 (3.1)，任意非零 $B,D$ 都满足

$$
\operatorname{ord}(BD)=\operatorname{ord}(B)+\operatorname{ord}(D),
\tag{3.3}
$$

其首系数是两首系数的乘积。因此 $\mathcal A$ 没有零因子。

同时，

$$
\boxed{\sigma_{B(H)}(B)=\{c_0(B)\}.}
\tag{3.4}
$$

自含证明如下。取多项式 $p_j(A)\to B$，并调整常数使 $p_j(0)=c_0(B)$；(2.3) 保证调整量趋零。于是 $D_j=p_j(A)-c_0(B)I$ 拟幂零，且它们与 $D=B-c_0(B)I$ 交换。对于交换算子 $X,Y$，二项式展开及谱半径公式给 $r(X+Y)\le r(X)+r(Y)$：先分别用 $(r(X)+\epsilon)^n$、$(r(Y)+\epsilon)^n$ 的常数倍控制幂范数，再展开并取 $n$ 次根即可。因此

$$r(D)\le r(D_j)+r(D-D_j)\le\|D-D_j\|\longrightarrow0.$$

这证明 (3.4)。若 $c_0(B)\ne0$，则 $B$ 可逆，且其逆仍在 $\mathcal A$ 中：对拟幂零的 $D/c_0(B)$ 使用按范数收敛的 Neumann 级数即可。

## 4. 有限阶闭理想与商代数

对 $m\ge1$，令

$$
J_m=\{B\in\mathcal A:c_0(B)=\cdots=c_{m-1}(B)=0\}.
$$

则 $J_m$ 是闭理想，并且

$$
\boxed{J_m=\overline{A^m\mathcal A}^{\|\cdot\|},\qquad
\mathcal A/J_m\cong\mathbb C[z]/(z^m),\qquad
\bigcap_{m\ge1}J_m=\{0\}.}
\tag{4.1}
$$

闭性来自有限个连续系数泛函，理想性来自 (3.1)。每个 $A^mD$ 的前 $m$ 阶系数为零，给出一个包含关系；反过来，$B\in J_m$ 的 Fejér 逼近多项式均可提出有限因子 $A^m$，给出另一个包含关系。截取前 $m$ 个形式系数是满射代数同态，核恰为 $J_m$，所以得到商代数同构。交集结论是系数唯一性。

没有由此分类 $\mathcal A$ 的全部闭理想，也没有证明 $J_m=A^m\mathcal A$；后一个等号事实上一般失败。

## 5. 首阶有限仍不足以有界除以 $A$

由于 $\sum_{j\ge0}\sqrt{a_j}<\infty$，下面的级数按算子范数绝对收敛：

$$
B_*=\sum_{j=0}^{\infty}\sqrt{a_j}\,F_{2^j}
=\sum_{j=0}^{\infty}\frac{\sqrt{a_j}}{W_{2^j}}A^{2^j}
\in\mathcal A.
\tag{5.1}
$$

它是非零的函数格正算子，$c_0(B_*)=0$，且 $c_1(B_*)=\sqrt{a_0}/W_1\ne0$，所以首阶恰为一。

**命题 5.1。** 不存在 $D\in\mathcal A$ 使 $B_*=AD$。

**证明。** 若存在，由唯一系数与 (3.1)，对每个 $j\ge0$ 必有

$$c_{2^j-1}(D)=\frac{\sqrt{a_j}}{W_{2^j}}.$$

应用 (2.3)，并注意 $W_{2^j}=W_{2^j-1}a_j$，得到

$$
\|D\|\ge |c_{2^j-1}(D)|W_{2^j-1}
=\frac1{\sqrt{a_j}}\longrightarrow\infty,
$$

矛盾。证毕。

所以 $A\mathcal A$ 是 $J_1$ 的真稠密子空间；有限首阶不能用来跳过有界除法问题。本命题只排除 $\mathcal A$ 内的商，尚未排除某个不属于该代数的有界交换子商。

## 6. 与当前不变子空间缺口的关系

R28 的临界交换子 $D=Q-q_0I$ 属于 $\mathcal A$。若它非零，本条确保其有有限首阶，而且它不会与 $\mathcal A$ 的另一个非零元素相乘为零。但若存在一个一般向量 $f\ne0$ 使 $Df=0$，这不是代数内部的零因子关系，(3.3) 并不排除它。

同样，$\overline{DH}$ 是否等于 $H$ 是此具体表示中的问题，不能由有限阶商代数或 (3.4) 决定。R24 的复对称性给 $\ker D=C(\overline{DH})^\perp$，因此单射性与稠密值域仍是同一个实质缺口。

本条给出可连续提取的系数、精确的有限阶代数和一个真实的除法反例，供继续处理该缺口；没有把无零因子误称为无非平凡普通不变子空间。
