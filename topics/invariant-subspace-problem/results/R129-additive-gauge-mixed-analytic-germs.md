# R129：加性gauge的全部混合解析芽及忠实性

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。预留 R129。

状态：完整证明。固定实际 Haar 表示上的 $A$ 与 $\mathcal A=\overline{\mathbb C[I,A]}$。本稿证明：若 $X\in\mathcal A$ 具有真正解析的加性 dyadic gauge 差，则每个**实际非零**的混合解析芽 $F(A,X)$ 单射且值域稠密。此外，此二元解析演算不忠实当且仅当 $X$ 本来就是 $A$ 的一元解析芽。证明保留实际非零假设，不能把任意非零标量芽自动当作非零算子。

## 1. 假设、规范化及主结论

记 $\chi$ 为 $\mathcal A$ 的唯一特征，即形式常数项。先规范化

$$
\chi(X)=0.
$$

一般 $X$ 可减去 $\chi(X)I$；对应的标量芽应在 $(0,\chi(X))$ 附近定义，再平移第二变量到零点。不能对一个只在原点给定的小半径芽，未经说明就在非零字符处求值。

令 $G=\bigcup_{m\ge0}\mu_{2^m}$ 为全部 dyadic 单位根。对 $\zeta\in G$，$U_\zeta$ 是乘以特征 $y\mapsto\zeta^y$ 的酉算子，且

$$
\gamma_\zeta(T)=U_\zeta TU_\zeta^*,\qquad
\gamma_\zeta(A)=\zeta A.
$$

假定对每个 $\zeta\in G$ 都有真正收敛的一元解析芽 $D_\zeta$，满足

$$
\boxed{\gamma_\zeta(X)=X+D_\zeta(A).}
\tag{1.1}
$$

形式常数项在 gauge 下不变，所以 $D_\zeta(0)=0$。

**定理 1.1。** 对任意 $F\in\mathbb C\{z,w\}$，若实际算子 $F(A,X)\ne0$，则

$$
\boxed{\ker F(A,X)=0,\qquad
\overline{\operatorname{Ran}F(A,X)}=H.}
\tag{1.2}
$$

因此 $F(A,X)$ 作用于任意 $A$-循环向量后仍得到循环向量。

**定理 1.2。** 二元芽演算

$$
\operatorname{ev}_{A,X}:\mathbb C\{z,w\}\longrightarrow\mathcal A
$$

不忠实，当且仅当存在 $g\in\mathbb C\{z\}$ 使 $X=g(A)$。在规范化下可取 $g(0)=0$。特别地，若 $X$ 不是一元解析芽，则每个非零标量芽 $F$ 都给非零、单射、稠密像的实际算子。

## 2. 求值、cocycle 及已证实际接口

由于 $A,X$ 都在 $\mathcal A$ 中且字符为零，它们拟幂零。若

$$
F(z,w)=\sum_{m,n\ge0}f_{mn}z^mw^n
$$

在双圆盘内收敛，则 Cauchy 系数界及任意小的几何幂界给

$$
\sum_{m,n}|f_{mn}|\|A^m\|\|X^n\|<\infty.
\tag{2.1}
$$

所以求值按范数绝对收敛，乘法恒等式合法。解析单位的逆芽也可如此求值，故解析单位给 $\mathcal A$ 内真实单位。

一元解析演算忠实：非零 $r(z)=z^su(z)$、$u(0)\ne0$ 给单射的 $r(A)=A^su(A)$，不可能为零。由 (1.1) 和群作用，

$$
D_{\zeta\xi}(z)=D_\zeta(z)+D_\xi(\zeta z).
\tag{2.2}
$$

因此

$$
(T_\zeta P)(z,w)=P(\zeta z,w+D_\zeta(z))
\tag{2.3}
$$

定义一个真正群作用。它作用于 $\mathbb C\{z\}[w]$ 及 $K[w]$，其中
$K=\operatorname{Frac}\mathbb C\{z\}$ 是零点附近的亚纯芽域。由于 $D_\zeta(0)=0$，它保持关于 $w$ 的 monic distinguished 多项式：首项系数为 $1$，且在 $z=0$ 时等于 $w^d$。

本稿使用以下实际模型事实，均已在 R32、R88、R122 中证明：

- $\mathcal A$ 的连续形式系数忠实，且其形式乘法使它无代数零因子；
- 全部 $\mathcal A$ 元素对
  $$B(u,v)=\int u(y)v(-1-y)\,d\mu(y)$$
  对称；
- 每个闭 $A$-不变空间 $M$ 都有 $\overline{A^sM}=M$（$s\ge1$）；具体由强趋 $I$ 的高位平均 $2m^{-1}\sum_{j=m}^{2m-1}N_j$ 给出；
- 每个非零闭 $A$-不变空间的总本质支撑为全测。

于是对任意非零一元解析芽 $r$，

$$
\overline{r(A)M}=M.
\tag{2.4}
$$

因为解析单位及其逆都保持 $M$，再应用限制幂稠密性即可。

## 3. 将一般标量芽化为关于 $w$ 的有限多项式

设 $F\ne0$。提取最大公共 $z$ 因子，写

$$
F(z,w)=z^kF_0(z,w),\qquad F_0(0,w)\not\equiv0.
$$

若 $F_0(0,0)\ne0$，则 $F_0$ 为解析单位，主定理直接归于 $A^k$。否则 $F_0(0,w)$ 在 $w=0$ 有某个有限阶 $d\ge1$，并可写

$$
F(z,w)=z^kU(z,w)P(z,w),
\quad
P(z,w)=w^d+\sum_{i<d}p_i(z)w^i,
\quad p_i(0)=0,
\tag{3.1}
$$

其中 $U$ 是解析单位。

为给出本稿所需的准备步骤，可直接作标量残数构造。选小圆 $|w|=\rho$，使 $F_0(0,w)$ 在闭圆盘中只有零点 $0$，重数 $d$，且圆上无零点。对充分小的 $|z|$，Rouché 保证圆内零点总数仍为 $d$。定义

$$
s_m(z)=\frac1{2\pi i}\int_{|w|=\rho}
w^m\frac{\partial_wF_0(z,w)}{F_0(z,w)}\,dw,
\qquad1\le m\le d.
$$

它们关于 $z$ 解析，且 $s_m(0)=0$。Newton 恒等式从这些幂和构造出 monic $P$，对每个固定 $z$，其零点及重数恰与 $F_0(z,\cdot)$ 在圆内的零点一致。于是 $F_0/P$ 对每个固定 $z$ 可去掉所有这些零点。其联合解析性由 Cauchy 表示

$$
U(z,w)=\frac1{2\pi i}\int_{|\eta|=\rho}
\frac{F_0(z,\eta)}{P(z,\eta)(\eta-w)}\,d\eta
$$

给出。$U(0,0)\ne0$，缩小双圆盘即得解析单位。这证明 (3.1)，不必选择连续或解析的零点编号。

求值后，$A^k$ 单射、$U(A,X)$ 可逆，故

$$
\ker F(A,X)=\ker P(A,X).
\tag{3.2}
$$

并且 $F(A,X)\ne0$ 保证 $P(A,X)\ne0$。

## 4. monic 不可约因子与有限例外 gauge 集

先在域 $K$ 上分解

$$
P=\prod_{i=1}^sP_i^{e_i},
\tag{4.1}
$$

其中 $P_i\in K[w]$ 互不相同、monic、不可约，次数 $d_i\ge1$。

实际上每个 $P_i$ 的系数都属于 $\mathbb C\{z\}$，且 $P_i(0,w)=w^{d_i}$。证明如下：这些系数原为亚纯芽。对小的非零 $z$，$P_i(z,\cdot)$ 的根是 $P(z,\cdot)$ 根的一部分；因 $P(0,w)=w^d$，所有这些根一致趋于零。每个因子系数是其有限个根的基本对称函数，因此在穿孔邻域中有界且趋于相应零值。亚纯系数的奇点可去，得到断言。

$T_\zeta$ 是 $K[w]$ 的自同构，故保持不可约性；它也保持 monic 和 distinguished 规范化。定义

$$
H_i=\{\zeta\in G:T_\zeta P_i=P_i\}.
\tag{4.2}
$$

这是子群。若 $H_i=G$，则实际算子 $P_i(A,X)$ 被全部 $\gamma_\zeta$ 固定。任何这样的 $\mathcal A$ 元素必为标量：它与全部 dyadic 特征乘法算子交换，因而是一个乘法算子 $M_\varphi$；再与 $A$ 交换，由 $w>0$ 几乎处处和 odometer 遍历性，$\varphi$ 必为常数。

因为

$$
\chi(P_i(A,X))=P_i(0,0)=0,
$$

该标量只能为零。这将使 (4.1) 的整个实际乘积为零，与 $P(A,X)\ne0$ 矛盾。因此每个 $H_i$ 都是真子群。

Prüfer $2$ 群 $G$ 的每个真子群有限：若一个子群含有阶数无界的元素，就含全部 $\mu_{2^m}$，从而等于 $G$。所以全部 $H_i$ 有限。

令坏集

$$
E=\{\zeta\in G:\gcd_{K[w]}(P,T_\zeta P)\ne1\}.
$$

由唯一 monic 不可约分解，$\zeta\in E$ 当且仅当对某对 $i,j$ 有 $P_i=T_\zeta P_j$。固定 $i,j$ 时，这个集合若非空，就是 $H_j$ 的一个陪集，故有限。有限多个因子对给出

$$
E\text{ 有限，因而 }E\subseteq\mu_h
\text{ 对某个 }h=2^m.
\tag{4.3}
$$

此处只需要坏集包含于一个有限子群，不要求坏集本身是子群。

## 5. 结式提供真正解析的消去因子

固定 $\zeta\notin\mu_h$。$P$ 与 $Q=T_\zeta P$ 在 $K[w]$ 中互素，且都为次数 $d$ 的 monic 多项式。因此 Sylvester 结式

$$
r_\zeta(z)=\operatorname{Res}_w(P,Q)
\in\mathbb C\{z\}
$$

不是零芽。更具体地，Sylvester 线性映射把次数小于 $d$ 的两个系数向量 $(L,V)$ 送到 $LP+VQ$ 的次数小于 $2d$ 的系数向量。对其矩阵使用伴随矩阵，并作用于常数多项式 $1$ 的系数向量，得到

$$
\boxed{r_\zeta(z)=L_\zeta(z,w)P(z,w)
+V_\zeta(z,w)Q(z,w),}
\tag{5.1}
$$

其中 $L_\zeta,V_\zeta\in\mathbb C\{z\}[w]$。可能的固定符号可吸收进 $r_\zeta$；它不影响非零性。这个构造已经清除所有亚纯分母，右侧的两个系数都是实际合法的解析芽。

记 $S=P(A,X)$、$M=\ker S$。$M$ 闭且 $A$ 不变。由 (1.1)、(2.3)，

$$
Q(A,X)=\gamma_\zeta(S),\qquad
U_\zeta M=\ker Q(A,X).
$$

对 $x,y\in M$，求值 (5.1)，利用 $Sx=0$ 及全部有界因子的 $B$-对称与交换性，得到

$$
B(r_\zeta(A)x,U_\zeta y)=0.
\tag{5.2}
$$

例如余下的项是 $V_\zeta(A,X)Q(A,X)x$，可把 $Q$ 经 $B$ 配对移到右端，那里 $Q(A,X)U_\zeta y=0$。

由 (2.4)，$r_\zeta(A)M$ 在 $M$ 稠密。所以

$$
\boxed{B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_h).}
\tag{5.3}
$$

所有因子有界，故本节没有隐藏的无界乘法域问题。

## 6. 有限 Fourier 支撑排除核

若 $M\ne0$，对任意 $u,v\in M$，函数

$$
q_{u,v}(y)=u(y)v(-1-y)
$$

属于 $L^1$。式 (5.3) 说它的全部 $\mu_h$ 以外的 dyadic Fourier 系数为零（配对只多一个非零的 $\zeta^{-1}$ 因子）。有限柱条件期望的 Fourier 展开及其 $L^1$ 收敛说明，$q_{u,v}$ 只依赖 $y\bmod h$。

非零闭 $A$-不变空间 $M$ 的总本质支撑为全测。其证明是：以可数稠密族定义总支撑 $E$，由 $A$ 不变和 $w>0$ 得 $E+1\subseteq E$；保测性将其变成模零集不变，遍历性迫 $E$ 全测。

因此对每个模 $h$ 柱 $Q_i$，可以从可数稠密族选出 $u_i,v_i\in M$，使 $u_i(y)v_i(-1-y)$ 在 $Q_i$ 的一个正测子集非零。这个乘积已是柱常数，所以它在整个 $Q_i$ 上等于某个非零常数。对任意 $u\in M$，$u(y)v_i(-1-y)$ 也为柱常数，故 $u|_{Q_i}$ 是 $u_i|_{Q_i}$ 的标量倍数。

每个柱上的限制秩至多一，于是 $\dim M\le h$。然而实际 $A$ 单射、范数拟幂零，不可能有非零有限维不变空间：有限维限制仍单射且拟幂零，后者迫其为幂零，矛盾。因此 $M=0$。

由 (3.2)，$F(A,X)$ 单射。它属于 $\mathcal A$，所以 $F(A,X)^*=CF(A,X)C$；伴随核也为零，值域稠密。若 $\xi$ 对 $A$ 循环，则

$$
\overline{\operatorname{span}\{A^nF(A,X)\xi:n\ge0\}}
=\overline{F(A,X)H}=H.
$$

定理 1.1 得证。

## 7. 解析演算忠实性的完整分类

假设存在非零 $F\in\mathbb C\{z,w\}$，但 $F(A,X)=0$。按 §3 提取 $z^k$ 和解析单位，因为 $A$ 单射，得到某个 monic distinguished $P$ 满足 $P(A,X)=0$。

按 §4 在 $K[w]$ 中分解 $P$。$\mathcal A$ 的形式无零因子性质使至少一个 monic distinguished 不可约因子 $Q$ 满足

$$
Q(A,X)=0.
\tag{7.1}
$$

对每个 $\zeta$，$T_\zeta Q$ 也在 $(A,X)$ 处为零。若它与 $Q$ 不同，两个 monic 不可约多项式便互素。§5 的结式恒等式将给出某个非零一元解析芽 $r$ 满足 $r(A)=0$，不可能。因此

$$
T_\zeta Q=Q\qquad\text{对全部 }\zeta\in G.
\tag{7.2}
$$

设

$$
Q(z,w)=w^d+q_{d-1}(z)w^{d-1}+\cdots.
$$

比较 (7.2) 的 $w^{d-1}$ 系数，得到

$$
dD_\zeta(z)+q_{d-1}(\zeta z)=q_{d-1}(z).
$$

令 $g(z)=-q_{d-1}(z)/d$，则

$$
g(\zeta z)-g(z)=D_\zeta(z).
$$

所以 $X-g(A)$ 被全部 gauge 固定，因而为标量。又 $g(0)=0$ 且 $\chi(X)=0$，故该标量为零：$X=g(A)$。

反向，若 $X=g(A)$，则非零标量芽 $w-g(z)$ 求值为零。定理 1.2 得证。

这个论证不调用“形式代数根自动收敛”等额外定理，而是直接从有限 monic 因子的全 gauge 稳定性读出所需解析函数。

## 8. 可直接覆盖的实际元素

R122 的任何 $\mathcal A$ 内加性类元素都满足 (1.1)，所以本定理覆盖其全部实际非零的混合解析芽。例如：

- 任意 $\ell^1$ 系数的实际第一 chaos 临界乘子 $\sum_ja_jY_j$；
- R112 的范数收敛不交高位 Hadamard 块乘子，其每个固定 gauge 只改变有限多个块；
- 任意已有加性 cocycle 元素加上真正解析函数，以及固定的非零标量倍数。

主定理不要求这些元素具有正则尾渐近、正相位或某个统一幂型衰减。若它们不是一元解析芽，§7 同时保证每个非零二元标量芽的实际求值非零。

## 9. 忠实解析演算不等于忠实有界除法

本节给出一个明确边界，避免把 §7 扩成尚未证明的亚纯商判据。

取无限非零正系数

$$
a_j=2^{-j}\alpha_j^2,
\qquad X=\sum_ja_jY_j\in\mathcal A.
$$

它满足加性解析 gauge 条件。实际估计

$$
\left\|\frac{A^{2^j-1}}{d_j}(I+N_j)^{-1}\right\|
\le\frac{3W_{2^j-1}}{d_j}
=\frac3{\alpha_j}
$$

说明

$$
Z=\sum_j a_j\frac{A^{2^j-1}}{d_j}(I+N_j)^{-1}
\in\mathcal A,
\qquad AZ=X.
\tag{9.1}
$$

然而 $X$ 不是一元解析芽：若 $X=g(A)$、$g$ 在固定圆盘解析，取原始 $2^{j+1}$ 次单位根。有限 gauge 差的第 $j$ 项在半径 $\rho_j=d_j^{1/2^j}\to0$ 上有非零极点，所有低位项的极点半径更大，不能消去。它不可能等于在该固定圆盘解析的 $g(\zeta z)-g(z)$。这是有限有理函数的极点论证，与同日第一 chaos 解析返回稿相同。

于是本例的二元解析演算忠实，但非全纯商 $w/z$ 的实际闭商却有有界实现 $Z$。因此本稿的混合解析芽核定理与忠实性分类，没有给一般芽商的有界性分类。

本稿也不处理 $\mathcal A$ 外无界 $X$ 的任意混合解析演算；那里的共同定义域、闭包和单位因子可逆性需要另证。完整 Hilbert ISP 及实际 $A$ 的全部普通不变格仍未由本稿解决。
