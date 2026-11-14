# R36：临界交换子：整个 B(H) 的除法障碍、一个可解尾部条件与 Schur 归约

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94。作者角色：general_routes。

**状态：自含证明的中间结论。** 本文继续 R28/R32 的问题：对具体 odometer 的多项式范数闭包中的非零元素，能否证明单射或值域稠密？本文把 R32 的除法反例加强到整个 $B(H)$；对一类比权重更快衰减的乘积变化证明临界组合仍循环；并证明原来的多项式衰减临界例确实不能由任何有界算子除以 $A$。原临界例有无核、是否值域稠密，仍没有解决。一般 Hilbert 不变子空间问题也未解决。

所有算子范数结论都在既定表示 $H=L^2(\mathbb Z_2,\mu)$ 中。

## 1. 记号与使用的已证结论

沿用 R9/R13：

$$
(Af)(y)=a_{v_2(y)}f(y-1),\qquad
W_n=\prod_{l=1}^n a_{v_2(l)}=\|A^n\|,\quad W_0=1.
$$

$A$ 单射、值域稠密且拟幂零。记

$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad \eta_j=\frac{a_{j+1}}{a_j}.
$$

这里用 $N_j$ 表示 dyadic 归一化幂，以免与任意阶的 $F_n=A^n/W_n$ 混淆。已有

$$
\|N_j\|=1,\qquad N_j^2=\eta_jN_{j+1},\qquad 0<\eta_j\le\eta_0<1.
\tag{1.1}
$$

R32 给每个 $B\in\mathcal A$ 唯一系数 $c_l(B)$，满足

$$
|c_l(B)|W_l\le\|B\|,
$$

且范数收敛的 Fejér 多项式具有这些系数。乘积系数按通常形式卷积；$B-c_0(B)I$ 拟幂零。因此 $c_0(B)\ne0$ 时，$B$ 在 $\mathcal A$ 中可逆。本文不把形式首阶有限误作有界可除性。

R24 的共轭 $Cf(y)=\overline{f(-1-y)}$ 满足 $B=CB^*C$（$B\in\mathcal A$），故

$$
\ker B=C\ker B^*=C(\overline{BH})^\perp.
\tag{1.2}
$$

所以本代数内每个元素的单射性与值域稠密性等价。

## 2. 用逃逸柱集提取系数

对 $N=2^d$ 和 $0\le r<N$，令

$$
C_{r,N}=\{y:y\equiv r\pmod N\},\qquad
e_r^{(N)}=\sqrt N\,1_{C_{r,N}}.
$$

这些是单位向量。随 $d$ 增大，它们不是固定向量；下面的矩阵元论证允许这种变化。

**引理 2.1。** 对每个固定 $l\ge0$ 及 $B\in\mathcal A$，

$$
\lim_{d\to\infty}\langle Be_0^{(2^d)},e_l^{(2^d)}\rangle
=c_l(B)W_l.
\tag{2.1}
$$

内积取第一变量线性；若改用另一惯例，只需同步共轭矩阵元。

**证明。** 先设 $B=p(A)=\sum_{n=0}^M p_nA^n$，取 $N>\max\{M,l\}$。不同 $0\le n\le M$ 把第零柱移到不同的第 $n$ 柱，故只有 $n=l$ 项可能贡献。当 $1\le s\le l<N$，第 $s$ 柱上的 $v_2(y)$ 恒为 $v_2(s)$；所以

$$
A^l e_0^{(N)}=W_l e_l^{(N)}
$$

在相关第 $l$ 柱上成立（事实上整个向量等式成立）。因此该矩阵元等于 $p_lW_l$。

一般情形，给定 $\varepsilon>0$，取 $\|B-p(A)\|<\varepsilon$。两个单位向量使矩阵元误差至多 $\varepsilon$，而 R32 的系数界使 $|(c_l(B)-p_l)W_l|\le\varepsilon$。对充分大 $N$，多项式矩阵元已经恰等于 $p_lW_l$，故极限上偏差至多 $2\varepsilon$。令 $\varepsilon\downarrow0$。证毕。

**定理 2.2（任意有界商的必要条件）。** 设 $B\in\mathcal A$，$m\ge1$。若存在任意 $D\in B(H)$ 满足 $B=A^mD$，则

$$
\boxed{\quad
\|D\|\ge\sup_{k\ge0}|c_{k+m}(B)|W_k.
\quad}
\tag{2.2}
$$

这里不假设 $D\in\mathcal A$，也不预先假设 $D$ 与 $A$ 交换。

**证明。** 固定 $k\ge0$，取 $N>k+m$。从第 $k$ 柱走到第 $k+m$ 柱的每一步都没有穿过第零柱，各步权重固定，乘积为

$$
\prod_{s=k+1}^{k+m}a_{v_2(s)}=\frac{W_{k+m}}{W_k}.
$$

由于加 $m$ 的模 $N$ 变换对柱集是一一对应，

$$
A^{*m}e_{k+m}^{(N)}=\frac{W_{k+m}}{W_k}e_k^{(N)}.
$$

从而

$$
\langle Be_0^{(N)},e_{k+m}^{(N)}\rangle
=\frac{W_{k+m}}{W_k}
\langle De_0^{(N)},e_k^{(N)}\rangle.
$$

由引理 2.1，右边第二个矩阵元的极限为 $c_{k+m}(B)W_k$。每个这样的矩阵元绝对值均不超过 $\|D\|$，遂得 (2.2)。证毕。

若有这样的商，它自动与 $A$ 交换：由 $BA=AB$ 得

$$
A^m(DA-AD)=0,
$$

而 $A^m$ 单射。同样，若 $B=DA^m$，则 $(AD-DA)A^m=0$；由 $A^m$ 值域稠密得到 $AD=DA$，于是又有 $B=A^mD$，仍受 (2.2) 约束。

**推论 2.3。** 若

$$
\sup_k|c_{k+m}(B)|W_k=\infty,
$$

则不仅 $B\notin A^m\mathcal A$，而且

$$
B\notin A^mB(H),\qquad B\notin B(H)A^m,\qquad
\operatorname{Ran}B\not\subset\operatorname{Ran}A^m.
\tag{2.3}
$$

**证明。** 前两项已证。若值域包含成立，由 $A^m$ 单射可定义处处有定义的 $D=(A^m)^{-1}B$。若 $x_n\to x$、$Dx_n\to y$，则 $A^my=\lim Bx_n=Bx$，故 $y=Dx$，所以 $D$ 闭。闭图定理给 $D\in B(H)$，与 (2.2) 矛盾。证毕。

特别地，R32 的

$$
B_*=\sum_{j\ge0}\sqrt{a_j}\,N_j
$$

满足

$$
|c_{2^j}(B_*)|W_{2^j-1}=\frac1{\sqrt{a_j}}\longrightarrow\infty.
$$

因此 (2.3) 对 $B_*$、$m=1$ 成立。这是真实算子值域的不包含，不只是代数内部的理想不相等。

**逻辑边界。** $\operatorname{Ran}B\not\subset\operatorname{Ran}A$ 并不表示 $\overline{BH}\ne H$；两个稠密、非闭的算子值域完全可以互不包含。此处没有证明 $B_*$ 有核。

## 3. 归一化无限乘积与对数

令 $0<r_j\le1$，$\delta_j=1-r_j$，假设 $\sum_j\delta_j<\infty$。定义

$$
V_j=(I+r_jN_j)(I+N_j)^{-1},\qquad
Q=\prod_{j=0}^{\infty}V_j,\qquad D=I-Q.
\tag{3.1}
$$

以下乘积全在交换代数 $\mathcal A$ 中。由 (1.1)，

$$
(I+N_j)^{-1}=(I-N_j)(I-\eta_jN_{j+1})^{-1},
$$

所以其范数至多 $2/(1-\eta_0)$。因此

$$
\|V_j-I\|\le \frac{2\delta_j}{1-\eta_0}.
$$

反向因子也有相同类型的界，故 $Q$ 是范数收敛的可逆乘积；$c_0(Q)=1$。

设

$$
L=\sum_{j\ge0}\bigl(\log(I+N_j)-\log(I+r_jN_j)\bigr).
\tag{3.2}
$$

每个对数在这里按其幂级数定义。由 $\|N_j^k\|\le\eta_j^{\lfloor k/2\rfloor}$ 及

$$
0\le\frac{1-r_j^k}{k}\le\delta_j,
$$

有

$$
\sum_{k\ge1}\frac{1-r_j^k}{k}\|N_j^k\|
\le \delta_j\frac{1+\eta_0}{1-\eta_0}.
$$

所以 (3.2) 按算子范数绝对收敛，且 $L\in\mathcal A$、$c_0(L)=0$。逐项指数化，利用所有因子交换并取范数极限，得到

$$
Q=e^{-L},\qquad
D=L\,\Psi(L),\qquad
\Psi(z)=\frac{1-e^{-z}}z,\quad\Psi(0)=1.
\tag{3.3}
$$

$\Psi$ 是整函数；$\Psi(L)\in\mathcal A$ 且常数系数为一，故可逆。因此

$$
\ker D=\ker L,\qquad
\operatorname{Ran}D=\operatorname{Ran}L,
\tag{3.4}
$$

并且 $D$ 可由某个有界算子右除以 $A^m$，当且仅当 $L$ 可以。这里的值域相等是实际值域相等，不只闭包相等。

## 4. Dyadic 系数显示原临界例不能有界除以 A

令

$$
b_J=c_{2^J}(L)W_{2^J}.
$$

从 (3.2) 的绝对收敛展开提取固定阶系数，得到精确式

$$
b_J=\delta_J-
\sum_{j=0}^{J-1}
\frac{1-r_j^{2^{J-j}}}{2^{J-j}}
\frac{W_{2^J}}{W_{2^j}^{\,2^{J-j}}}.
\tag{4.1}
$$

符号来自对数的交错号：$j=J$ 对应一次项，$j<J$ 对应偶数次项。

由递推 (1.1)，

$$
\frac{W_{2^J}}{W_{2^j}^{\,2^{J-j}}}
=\prod_{s=j}^{J-1}\eta_s^{\,2^{J-1-s}}
\le\eta_{J-1}\qquad(j<J).
$$

又 $0\le1-r_j^{2^{J-j}}\le1$，所以

$$
\boxed{\quad
\delta_J-\eta_{J-1}\le b_J\le\delta_J\quad (J\ge1),
\qquad b_0=\delta_0.
\quad}
\tag{4.2}
$$

若 $\delta_J\ge2\eta_{J-1}$ 沿某子列成立，且沿该子列 $\delta_J/a_J\to\infty$，则

$$
|c_{2^J}(L)|W_{2^J-1}
=\frac{|b_J|}{a_J}\ge\frac{\delta_J}{2a_J}\longrightarrow\infty.
$$

定理 2.2 和 (3.3) 遂给

$$
\operatorname{Ran}L=\operatorname{Ran}D\not\subset\operatorname{Ran}A.
\tag{4.3}
$$

R28 的具体临界例取

$$
t_j=\frac1{(j+2)^2},\qquad
r_j=\frac{1-t_j}{1+t_j},\qquad
\delta_j=\frac2{(j+2)^2+1}.
$$

这里 $\delta_j$ 按多项式衰减，而 $a_j$、$\eta_{j-1}$ 按已定义的超快速率衰减，故上述两个条件成立。于是该临界 $D$ 不属于 $AB(H)$ 或 $B(H)A$。不能用“首阶为一，所以写成 $A$ 乘可逆有界函数”的方式解决它。

这仍未决定 $D$ 的单射性或值域稠密性。

## 5. 一个确能完成有界除法的尾部条件

与上一节不同，充分强的尾部控制可以给出正面结论。

**定理 5.1。** 假设 (3.1) 的序列不恒为一，且

$$
\sum_{j\ge0}\frac{\delta_j}{a_j}<\infty.
\tag{5.1}
$$

令 $j_0=\min\{j:\delta_j\ne0\}$、$m=2^{j_0}$。则存在 $R\in\mathcal A$ 可逆，使

$$
\boxed{D=A^mR.}
\tag{5.2}
$$

因此 $D$ 单射且值域稠密。

**证明。** 有限乘积的望远镜恒等式给

$$
I-\prod_{j=0}^M V_j
=\sum_{j=0}^M\delta_jN_j(I+N_j)^{-1}
\prod_{i<j}V_i.
\tag{5.3}
$$

$j<j_0$ 的项为零。对 $j\ge j_0$，有

$$
N_j=A^m\frac{A^{2^j-m}}{W_{2^j}},
\qquad
\left\|\frac{A^{2^j-m}}{W_{2^j}}\right\|
=\frac{1}{a_jW_{m-1}}.
\tag{5.4}
$$

最后一个等式的理由是：整数区间 $2^j-m+1,\ldots,2^j$ 中，最后一项权重为 $a_j$，此前 $m-1$ 项的 $2$-进赋值与 $1,\ldots,m-1$ 的赋值相同（顺序倒转也不改变乘积）。因此 $W_{2^j}/W_{2^j-m}=a_jW_{m-1}$。

各前缀乘积的范数由 $\prod_i(1+2\delta_i/(1-\eta_0))$ 一致控制，逆因子 $(I+N_j)^{-1}$ 也一致有界。由 (5.1)，下式按范数绝对收敛于 $\mathcal A$ 中的元素：

$$
R=\sum_{j\ge j_0}\delta_j
\frac{A^{2^j-m}}{W_{2^j}}
(I+N_j)^{-1}\prod_{i<j}V_i.
\tag{5.5}
$$

由 (5.3) 取极限得到 $D=A^mR$。只有 $j=j_0$ 的项有非零常数系数，且各逆因子与前缀乘积的常数系数均为一，故

$$
c_0(R)=\frac{\delta_{j_0}}{W_m}\ne0.
$$

R32 的单点谱结论使 $R$ 可逆。最后，$A^m$ 单射且值域稠密，所以 $D$ 也如此。证毕。

**临界向量的推论。** 在标准二进制张量实现中，$N_j(e_0\otimes u)=e_1\otimes u$。因此

$$
V_j\bigl((e_0+e_1)\otimes u\bigr)
=(e_0+r_je_1)\otimes u.
$$

由此 $Q1=\prod_j r_j^{b_j}$，并且

$$
f_*=D1=1-\prod_jr_j^{b_j}.
$$

因为常数向量 $1$ 对 $A$ 循环，$[D1]_A=\overline{DH}$。于是 (5.1) 保证这个临界向量本身循环。

例如取 $r_j=1-a_j^2$。则 $\delta_j/a_j=a_j$ 可和，$f_*$ 是非零连续函数，在 $y=0$ 处取零，并且对 $A$ 循环。这证明“临界组合”确实不自动产生不变子空间；同时，本定理没有覆盖上一节的多项式尾部例。

## 6. 原临界核的一步精确 Schur 归约

为明确没有完成的部分，假设 $0<r_0<1$，记

$$
R_{\rm tail}=\prod_{j\ge1}V_j,\quad
X=I-R_{\rm tail},\quad
Y=I-r_0R_{\rm tail},\quad
Z=XY^{-1}.
$$

$c_0(Y)=1-r_0\ne0$，所以 $Y$ 可逆。尾部因子在第零位上都是恒等，且与 $N_0$ 交换。直接整理得

$$
D=Y(N_0+Z)(I+N_0)^{-1}.
\tag{6.1}
$$

按第零位分成 $H=H_{\rm tail}\oplus H_{\rm tail}$，

$$
N_0=
\begin{pmatrix}0&\eta_0N_1\\I&0\end{pmatrix},
\qquad
N_0+Z=
\begin{pmatrix}Z&\eta_0N_1\\I&Z\end{pmatrix}.
$$

因此

$$
\ker(N_0+Z)
=\{(-Zv,v):v\in\ker(\eta_0N_1-Z^2)\}.
\tag{6.2}
$$

(6.1) 的两个外因子可逆，故这确实把 $D$ 的单射性化为尾部算子 $\eta_0N_1-Z^2$ 的单射性。它不允许继续写 $Z^2=N_1U$ 并直接称 $U$ 有界。第 2–4 节表明这类形式除法需要实质证明，而不是由首阶计数自动成立。

## 7. 已完成与仍缺失的数学内容

本条完成三个可独立使用的结论：任意 $B(H)$ 商的矩阵元必要界；特定临界乘积在足够快尾部条件下的单射/稠密值域；以及原多项式尾部临界乘积真实的不可有界除法。

原多项式尾部 $D$ 的核仍未知。若以后证明 $\ker D\ne0$ 或 $\overline{DH}\ne H$，因 $D\in\mathcal A$ 与 $A$ 的每个交换子都交换，相应的核或闭值域将是 **$A$ 的超不变子空间**，当然也是普通不变子空间。这里没有给出这样的子空间，也没有把某个具体 $A$ 的分析升格为一般 ISP 的解答。

## 参考入口

- 本仓库 R13、R24、R28、R32；[R28](R28-rational-factor-replacement.md)。本文的新推导全部自含，不依赖未核验的外部定理。
- 通用 gauge-action 与 Fourier 唯一性背景可对照 Justin R. Peters, *Singly generated radical operator algebras*, New York Journal of Mathematics **30** (2024), 398–421，§2.1：<https://nyjm.albany.edu/j/2024/30-15.html>。该文的抽象代数结论并没有在此被用作具体 odometer 表示的无核定理。

原文补核：Peters 的 Proposition 3.12 以 $S=T^kQ$、$Q$ 属于含单位的有界算子代数为前提，不能用来取消本文第2–4节已证的除法障碍；Propositions 3.7、3.10 另要求其单边移位权递减且平方可和，也未被移用于当前Haar表示。
