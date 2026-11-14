# 快解析逼近的 gauge 增量：混合解析芽、分式系数与全部闭商

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。根代理预留 R152。

状态：以下定理均有完整证明。本稿把 R129/R135 的真正解析加性增量，推广为 R151 的四次型解析逼近类。主证明保留一个真实尾误差与固定结式首阶；另给出分式域上的更强多项式系数版本。没有把全空间稠密像当作任意不变限制上的稠密像。

## 1. 假设、已证输入与结论

固定本题实际 Haar 表示中的算子 $A$，并记

$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\qquad \Gamma=\bigcup_{m\ge0}\mu_{2^m},
\qquad \gamma_\zeta(T)=U_\zeta T U_\zeta^*.
$$

这里 $U_\zeta$ 是乘以 $y\mapsto\zeta^y$ 的酉算子，
$\gamma_\zeta(A)=\zeta A$。记 $\chi$ 为 $\mathcal A$ 的唯一字符。
连续、忠实的形式系数映射记为

$$
\iota:\mathcal A\longrightarrow\mathbb C[[z]],
\qquad \iota(A)=z.
\tag{1.1}
$$

它是单射代数同态，满足
$\iota(\gamma_\zeta T)(z)=\iota(T)(\zeta z)$。
因此 $\mathcal A$ 没有代数零因子。

沿用 R151 的定义：$E\in\mathcal G$ 当且仅当存在真正收敛的一元解析芽 $f_n$，使

$$
\|E-f_n(A)\|\longrightarrow0,
\qquad
\tau_4(E-f_n(A))\longrightarrow+\infty,
\quad
\tau_4(T)=\liminf_{k\to\infty}\frac{-\log\|T^k\|}{k^4}.
\tag{1.2}
$$

约定 $\tau_4(0)=+\infty$；各 $f_n$ 的解析邻域可以不同。
本稿使用 R151 已完整证明的以下事实：

- $\mathcal G$ 是含全部真正解析演算的交换子代数，并被每个 $\gamma_\zeta$ 保持。
- 非零 $T\in\mathcal A$ 满足
  $$\tau_4(T)\le c_*\operatorname{ord}(T)^4,\qquad c_*:=100/15.$$
  因而 (1.2) 中的每个固定有限 jet 最终与 $E$ **精确相等**。
- 每个非零 $E\in\mathcal G$ 单射；对每个闭 $A$ 不变 $M$，
  $$\overline{EM}=M.$$
  这还对全部有限放大及其不变限制成立，来自真实不变子商的精确四次型。

还使用 R140 的如下单尾结论：若 $r(z)$ 是首阶 $\ell\ge1$ 的非零真解析芽，而 $K\in\mathcal A$ 满足

$$
\tau_4(K)>c_*\ell^4,
$$

则对每个闭 $A$ 不变 $M$，

$$
\overline{(r(A)+K)M}=M.
\tag{1.3}
$$

其依据是：若闭包真小于 $M$，在这个非零不变商上 $r(A_Q)=-K_Q$，而左边的型精确等于 $c_*\ell^4$，右边的型至少为 $\tau_4(K)$，矛盾。这里并未由全空间像稠密推出 (1.3)。

现在取 $S\in\mathcal A$，并规范化 $\chi(S)=0$。假定

$$
\boxed{D_\zeta:=\gamma_\zeta(S)-S\in\mathcal G
\quad(\zeta\in\Gamma).}
\tag{1.4}
$$

一般未规范化的 $S$，先减去 $\chi(S)I$，把第二变量的基点从 $(0,\chi(S))$ 平移到原点。

**定理 1.1（混合解析芽）。** 对任意 $F\in\mathbb C\{z,w\}$，只要实际演算 $F(A,S)\ne0$，就有

$$
\boxed{\ker F(A,S)=0,\qquad
\overline{\operatorname{Ran}F(A,S)}=H.}
\tag{1.5}
$$

它因而把每个 $A$ 循环向量送为循环向量。

**定理 1.2（忠实性）。** 演算 $F\mapsto F(A,S)$ 忠实，当且仅当 $S$ 不是 $A$ 的一元收敛解析芽。这个忠实性判据本身对任意字符为零的 $S\in\mathcal A$ 成立，不需要 (1.4)。

**定理 1.3（更强的多项式系数）。** 若 $P(t)\in\mathcal G[t]$，且实际有界算子 $P(S)\ne0$，则 $P(S)$ 单射且值域稠密。这里系数可以是不收敛标量幂级数的 $\mathcal G$ 元素。证明见 §7。

若另有 $S$ 非一元解析，则全部二元收敛解析芽分式具有 R135 的规范最大闭实现、原分母图核心、$C$ 自伴性及闭包代数运算；§8 给出准确域和验证。

## 2. 范数解析演算与有限多项式化

由于 $A,S$ 字符均为零，它们拟幂零。若

$$
F(z,w)=\sum_{i,j\ge0}a_{ij}z^iw^j
$$

在双圆盘内收敛，取严格更小的正数 $r,s$，用 Cauchy 系数界及拟幂零算子的几何幂界，可得

$$
\sum_{i,j}|a_{ij}|\|A^i\|\|S^j\|<\infty.
\tag{2.1}
$$

故求值范数绝对收敛、保乘法。解析单位及其逆芽都可求值，因此解析单位成为 $\mathcal A$ 中的有界单位。

令

$$
\sigma(z)=\iota(S)(z)\in z\mathbb C[[z]].
$$

对每个固定形式次数，(2.1) 及系数连续性给

$$
\iota(F(A,S))=F(z,\sigma(z)).
\tag{2.2}
$$

右边是合法形式代入，因为 $\sigma(0)=0$。若 $S=0$，其形式级数也为零；以下论证仍适用。

对非零标量芽 $F$，先提取最大的公共 $z$ 次幂，再作固定 $z$ 坐标的 Weierstrass 准备，得

$$
F(z,w)=z^kU(z,w)P(z,w),
\qquad
P(z,w)=w^p+\sum_{j<p}p_j(z)w^j,
\qquad P(0,w)=w^p,
\tag{2.3}
$$

其中 $U$ 是解析单位。R129 §3 已用小圆残数、Newton 恒等式和 Cauchy 公式给出此准备构造；不涉及改变 $A$ 的坐标。允许 $p=0$，此时只剩 $A^k$ 乘单位，结论直接成立。

以下取 $p\ge1$，记

$$
T=P(A,S),\qquad M=\ker T.
$$

$A$ 单射且 $U(A,S)$ 可逆，所以

$$
F(A,S)\ne0\Longrightarrow T\ne0,
\qquad \ker F(A,S)=\ker T.
\tag{2.4}
$$

由形式忠实性，

$$
P(z,\sigma(z))\ne0.
\tag{2.5}
$$

## 3. 形式因子的有限例外集

本节仅在形式 Laurent 域

$$
\widehat K=\mathbb C((z))
$$

上作有限多项式代数，不把这些形式因子求值为算子。
置

$$
\mathfrak P(z,w)=P(z,w+\sigma(z))\in\widehat K[w].
\tag{3.1}
$$

令 $\alpha_\zeta$ 对系数作 $z\mapsto\zeta z$，而固定变量 $w$。
将 $\mathfrak P$ 分解为有限个互异首一不可约因子：

$$
\mathfrak P=\prod_{i=1}^s f_i^{e_i}.
$$

每个稳定子

$$
H_i=\{\zeta\in\Gamma:\alpha_\zeta f_i=f_i\}
$$

都是子群。若 $H_i=\Gamma$，每个 Laurent 系数都被全部 dyadic 代换固定。
对任意整数 $n\ne0$，总可取 $\zeta$ 使 $\zeta^n\ne1$；故固定 Laurent 级数只能是常数。
于是 $f_i\in\mathbb C[w]$。因 $\mathbb C$ 代数闭且 $f_i$ 在 $\widehat K[w]$ 中不可约，必有

$$
f_i=w-c\qquad(c\in\mathbb C).
$$

由整除关系，$P(z,c+\sigma(z))=0$。取常数项得到 $c^p=0$，故 $c=0$，与 (2.5) 矛盾。
因此每个 $H_i$ 都是真子群。

Prüfer $2$ 群的真子群有限：若子群含有阶数任意大的元素，它就包含全部有限群 $\mu_{2^m}$，从而等于 $\Gamma$。
因此全部 $H_i$ 有限。

对固定 $i,j$，集合

$$
\{\zeta:\alpha_\zeta f_i=f_j\}
$$

若非空，就是 $H_i$ 的一个陪集，故有限。有限多个因子对表明：存在一个 dyadic 整数 $H_0=2^m$，使

$$
\gcd_{\widehat K[w]}(\mathfrak P,\alpha_\zeta\mathfrak P)=1
\qquad(\zeta\notin\mu_{H_0}).
\tag{3.2}
$$

坏集本身未必是子群，只需被这个有限子群包含。

令

$$
\delta_\zeta(z)=\sigma(\zeta z)-\sigma(z),
\qquad
\widehat Q_\zeta(z,w)=P(\zeta z,w+\delta_\zeta(z)).
\tag{3.3}
$$

变量代换 $w\mapsto w+\sigma(z)$ 将 $(P,\widehat Q_\zeta)$ 同时变成 $(\mathfrak P,\alpha_\zeta\mathfrak P)$。
所以对 (3.2) 中的每个 $\zeta$，形式结式

$$
\widehat R_\zeta(z)=\operatorname{Res}_w(P,\widehat Q_\zeta)
\in\mathbb C[[z]]
$$

非零。写

$$
r_\zeta=\operatorname{ord}\widehat R_\zeta<\infty.
\tag{3.4}
$$

因为 $P(0,w)=\widehat Q_\zeta(0,w)=w^p$，有 $r_\zeta\ge1$。

这里可能不收敛的是 $\delta_\zeta$ 与形式结式；下一节只求值真实解析逼近，没有把它们当成全纯演算。

## 4. 精确 jet、真实 Sylvester 恒等式与单个尾误差

固定 $\zeta\notin\mu_{H_0}$。由 (1.4)，取真正解析芽 $d_n$，使

$$
E_n=D_\zeta-d_n(A),\qquad
\|E_n\|\to0,\qquad\tau_4(E_n)\to\infty.
\tag{4.1}
$$

令 $\epsilon_n(z)=\iota(E_n)(z)=\delta_\zeta(z)-d_n(z)$。
R151 的系数上界说明，任意固定 $N$ 都有

$$
\epsilon_n\in z^N\mathbb C[[z]]
\quad\text{对充分大 }n.
\tag{4.2}
$$

特别可舍去有限项，使 $d_n(0)=0$。
定义真正解析系数的首一多项式及结式

$$
Q_n(z,w)=P(\zeta z,w+d_n(z)),
\qquad R_n(z)=\operatorname{Res}_w(P,Q_n)\in\mathbb C\{z\}.
\tag{4.3}
$$

结式是两组有限系数的整数多项式。若 (4.2) 取 $N=r_\zeta+1$，则

$$
R_n\equiv\widehat R_\zeta\pmod{z^{r_\zeta+1}},
\qquad\boxed{\operatorname{ord}R_n=r_\zeta}
\quad(n\text{充分大}).
\tag{4.4}
$$

不需要对各 $d_n$ 的解析半径、结式高阶系数或单位逆范数作一致估计。
有限 jet 的精确稳定已经固定了所需的唯一指数 $r_\zeta$。

对次数均为 $p$ 的 $P,Q_n$，Sylvester 系数矩阵把次数小于 $p$ 的 $(U,V)$ 映到 $UP+VQ_n$ 的次数小于 $2p$ 的系数向量。
对该矩阵用伴随矩阵，并作用于常数多项式 $1$ 的坐标向量，可得

$$
\boxed{R_n(z)=U_n(z,w)P(z,w)+V_n(z,w)Q_n(z,w),}
\tag{4.5}
$$

其中 $U_n,V_n\in\mathbb C\{z\}[w]$；固定的结式符号可一并吸收。
这已经是解析系数的真实恒等式，不含未知亚纯分母。

实际 gauge 变换为

$$
\gamma_\zeta(T)=P(\zeta A,S+D_\zeta).
$$

令

$$
K_n=\gamma_\zeta(T)-Q_n(A,S).
$$

由于 $P$ 关于第二变量为有限多项式，交换差幂公式给一个真实 $H_n\in\mathcal A$，满足

$$
\boxed{K_n=E_nH_n.}
\tag{4.6}
$$

例如写 $P(z,w)=\sum_{i=0}^p p_i(z)w^i$、$p_p=1$，并令 $Z_n=S+d_n(A)$，则可明确取

$$
H_n=\sum_{i=1}^p p_i(\zeta A)
\sum_{j=0}^{i-1}(Z_n+E_n)^{i-1-j}Z_n^j.
\tag{4.7}
$$

每个因子有界且交换。对每个固定 $n$，乘以有界交换因子只给幂范数增加 $O(k)$ 对数项，因此

$$
\tau_4\bigl(V_n(A,S)K_n\bigr)\ge\tau_4(E_n).
\tag{4.8}
$$

若乘积为零，左边按约定为无穷。$V_n,H_n$ 的范数即使随 $n$ 增长，也不影响这个逐个固定 $n$ 的不等式。

选择一个足够大的 $n$，同时满足 (4.4) 和

$$
\tau_4(E_n)>c_*r_\zeta^4.
\tag{4.9}
$$

将 (4.5) 求值，再由 (4.6) 代换，得到

$$
\boxed{
R_n(A)+V_n(A,S)K_n
=U_n(A,S)T+V_n(A,S)\gamma_\zeta(T).
}
\tag{4.10}
$$

这里只出现一个已经固定的尾 $E_n$。没有把它分成 $E_n$ 与 $\gamma_\zeta(E_n)$ 两项，因而没有二项 harmonic 估计的常数 $8$ 损失。

## 5. 不变限制上的稠密性与跨核 Fourier 论证

由 (4.4)、(4.8)、(4.9) 和 R140 的 (1.3)，算子

$$
L_\zeta:=R_n(A)+V_n(A,S)K_n
$$

满足

$$
\overline{L_\zeta M}=M.
\tag{5.1}
$$

$M=\ker T$ 是闭 $A$ 不变空间，全部 $\mathcal A$ 因子保持它。
同样，$U_\zeta M=\ker\gamma_\zeta(T)$。
令

$$
B(x,y)=\int_{\mathbb Z_2}x(t)y(-1-t)\,d\mu(t).
$$

所有有界交换子对 $B$ 对称。对 $x\in M$、$y\in U_\zeta M$，(4.10) 第一项因 $Tx=0$ 消失；第二项把 $\gamma_\zeta(T)$ 经 $B$ 移到右端后也消失。
故

$$
B(L_\zeta M,U_\zeta M)=0.
$$

以 (5.1) 取闭包，得到

$$
\boxed{B(M,U_\zeta M)=0
\quad(\zeta\notin\mu_{H_0}).}
\tag{5.2}
$$

下面重述所需的具体 Fourier 排核，避免把它当作一般抽象商空间结论。
对任意 $x,y\in M$，$x(t)y(-1-t)\in L^1$；由 (5.2)，它在有限群 $\mu_{H_0}$ 以外的全部 dyadic Fourier 系数都为零。
有限柱条件期望的 Fourier 展开及其 $L^1$ 收敛遂说明，此乘积仅依赖 $t\bmod H_0$。

若 $M\ne0$，其总本质支撑为全测：以可数稠密族定义支撑 $E$，由 $A$ 不变和真实权几乎处处严格正得到 $E+1\subseteq E$；保测性给模零集不变，再由 odometer 遍历性得全测。
在每个模 $H_0$ 柱上，从可数稠密族选 $x_0,y_0$，使 $x_0(t)y_0(-1-t)$ 在正测子集非零。它已经是柱常数，故在该整柱为非零常数。
对任意 $x\in M$，$x(t)y_0(-1-t)$ 也为柱常数，所以该柱上的 $x$ 是 $x_0$ 的标量倍数。
每柱的限制秩至多一，因而

$$
\dim M\le H_0.
$$

实际 $A$ 单射拟幂零，不存在非零有限维不变空间：其有限维限制会同时单射且幂零，矛盾。
故 $M=0$，由 (2.4) 得 $F(A,S)$ 单射。

全部 $\mathcal A$ 元素满足 $T^*=CTC$，其中 $Cx(t)=\overline{x(-1-t)}$。因此伴随核也为零，值域稠密。
若 $\xi$ 对 $A$ 循环，则

$$
\overline{\operatorname{span}\{A^nF(A,S)\xi:n\ge0\}}
=\overline{F(A,S)H}=H.
$$

定理 1.1 得证。此证明只在辅助算子 $L_\zeta$ 上使用了普遍限制稠密性，没有声称全部 $F(A,S)$ 已在每个不变限制上像稠密。

## 6. 忠实性：形式代数解收敛的自含证明

先证一个纯标量引理。

**引理 6.1。** 若 $\sigma\in\mathbb C[[z]]$ 满足某个非零关系

$$
p(z,\sigma(z))=0,\qquad p\in\mathbb C\{z\}[w],
$$

则 $\sigma$ 收敛于零点邻域。

**证明。** 在全部非零解析系数多项式关系中，取 $w$ 次数最小的 $p$。次数至少为1，且

$$
p_w(z,\sigma(z))\ne0,
$$

否则非零的 $p_w$ 是更低次数关系。记其形式阶为 $\ell\ge0$。
取 $N+1>\ell$，以 $s_N(z)$ 表示 $\sigma$ 的 $N$ 次截断，并写

$$
\sigma=s_N+z^{N+1}v,\qquad v\in\mathbb C[[z]].
$$

由于 $p_w(z,s_N)$ 与 $p_w(z,\sigma)$ 在低于 $N+1$ 的阶精确相同，

$$
p_w(z,s_N)=z^\ell b(z),\qquad b(0)\ne0.
$$

对第二变量作有限 Taylor 展开。原形式关系说明 $p(z,s_N)$ 可被 $z^{N+1+\ell}$ 整除：线性项有该阶，而全部高次项的阶至少为 $2(N+1)>N+1+\ell$。
因此除以这个有限 $z$ 次幂得到真正解析方程

$$
0=a(z)+b(z)v+
\sum_{k=2}^{\deg_w p}
z^{(k-1)(N+1)-\ell}c_k(z)v^k.
\tag{6.1}
$$

在 $z=0$ 处它是 $a(0)+b(0)v=0$，对 $v$ 的导数非零。
解析隐函数定理给唯一解析解，常数项等于原形式 $v(0)$。此处也可直接用小双圆盘上的收缩迭代：把方程写成 $v\mapsto v-b(0)^{-1}G(z,v)$，缩小邻域使其对 $v$ 的导数范数小于1；迭代的一致极限解析。
形式系数逐阶递推同样由 $b(0)\ne0$ 唯一确定，所以原形式 $v$ 就是这个解析解。
于是 $\sigma=s_N+z^{N+1}v$ 收敛。证毕。

现在若某个非零 $F\in\mathbb C\{z,w\}$ 满足 $F(A,S)=0$，先用 (2.3) 提取 $z^k$ 与单位。
$A$ 单射使 $P(A,S)=0$，形式忠实性给 $P(z,\sigma)=0$。
引理 6.1 得 $\sigma=g\in\mathbb C\{z\}$。
一元求值的形式级数是 $g$，故

$$
\iota(S-g(A))=0.
$$

再由形式忠实性得到 $S=g(A)$。
反向若 $S=g(A)$，非零芽 $w-g(z)$ 就在演算核中。
这证明定理 1.2，且整个论证不使用 (1.4)。

## 7. 强化：任意 $\mathcal G$ 系数多项式

本节给定理 1.3 的独立证明。它直接使用 R151 的限制稠密性，不要求把每个系数先近似为解析芽。

### 7.1 分式域和加性半线性作用

由 (1.1) 的忠实性，将

$$
K=\operatorname{Frac}(\mathcal G)
$$

视为 $\mathbb C((z))$ 的一个子域。此处只是代数分式域，不先把每个分式当作有界算子或闭算子。
Gauge 保持 $\mathcal G$，所以扩张为 $K$ 的自同构 $\alpha_\zeta$。
把 $D_\zeta\in\mathcal G$ 与其形式级数视为同一元素，定义

$$
\mathcal T_\zeta R(t)
=(\alpha_\zeta R)(t+D_\zeta),
\qquad R\in K[t].
\tag{7.1}
$$

增量满足 $D_{\zeta\xi}=D_\zeta+\gamma_\zeta(D_\xi)$，所以 (7.1) 是真正群作用。
它保持首一性、次数及不可约性。
形式求值还满足

$$
(\mathcal T_\zeta R)(\sigma)
=\alpha_\zeta(R(\sigma)),
\qquad \alpha_\zeta(\sigma)=\sigma+D_\zeta.
\tag{7.2}
$$

### 7.2 代数情形自动是有理情形

若 $\sigma$ 代数于 $K$，令

$$
p(t)=t^r+g t^{r-1}+\cdots\in K[t]
$$

为其首一最小多项式。由 (7.2)，$\mathcal T_\zeta p$ 也是同次数的首一最小多项式，故等于 $p$。
比较次高系数，得到

$$
\alpha_\zeta(g)+rD_\zeta=g.
$$

所以 $\sigma+g/r$ 被全部 Laurent 代换固定，必为常数。于是

$$
\boxed{\sigma\text{ 代数于 }K\Longrightarrow\sigma\in K.}
\tag{7.3}
$$

写 $\sigma=a/b$，其中 $a,b\in\mathcal G$、$b\ne0$。
形式忠实性把它变成真实有界恒等式

$$
bS=a.
\tag{7.4}
$$

设 $P(t)=\sum_{j=0}^p E_jt^j\in\mathcal G[t]$，且 $P(S)\ne0$。则

$$
b^pP(S)=\sum_{j=0}^pE_j a^j b^{p-j}\in\mathcal G
\tag{7.5}
$$

且非零，因为 $b$ 单射或由 $\mathcal A$ 无零因子可知。
R151 使 (7.5) 单射且在每个不变限制上像稠密。
其核包含 $\ker P(S)$，且对每个不变 $M$，其像包含关系为

$$
b^pP(S)M=P(S)b^pM\subseteq P(S)M.
$$

所以这一有理分支更强地给 $\overline{P(S)M}=M$，特别证明所需单射稠密结论。

### 7.3 超越分支的有限因子和真实清分母

若 $\sigma$ 超越于 $K$，则 $K[t]$ 的求值没有非零核。
对给定非零 $P\in\mathcal G[t]$，先在 $K[t]$ 中将其最高系数视为单位，再作有限首一不可约分解。

若某个首一因子 $f=t^d+g t^{d-1}+\cdots$ 的稳定子为全部 $\Gamma$，比较 $\mathcal T_\zeta f=f$ 的次高系数，仍得到

$$
\alpha_\zeta(g)+dD_\zeta=g,
$$

从而 $\sigma+g/d$ 为常数，迫使 $\sigma\in K$，矛盾。
因此所有因子的稳定子都有限；如 §3 的陪集论证，存在一个有限 dyadic 子群 $\mu_H$，使

$$
\gcd_{K[t]}(P,\mathcal T_\zeta P)=1
\qquad(\zeta\notin\mu_H).
$$

有限 Euclidean 算法给 $U,V\in K[t]$，满足 $UP+V\mathcal T_\zeta P=1$。
乘以有限多个系数分母的乘积，得到

$$
\boxed{D=U_0P+V_0\mathcal T_\zeta P,}
\quad
0\ne D\in\mathcal G,
\quad U_0,V_0\in\mathcal G[t].
\tag{7.6}
$$

这里只清有限个分母。右侧全部系数和 $D$ 都是已给的有界 $\mathcal G$ 元素。
所以 (7.6) 在实际 $S$ 上求值得

$$
D=U_0(S)P(S)+V_0(S)\gamma_\zeta(P(S)).
\tag{7.7}
$$

令 $M=\ker P(S)$。两项跨核配对与 §5 相同，给
$B(DM,U_\zeta M)=0$。
R151 的 $\overline{DM}=M$ 遂给 $B(M,U_\zeta M)=0$，除外根仅在 $\mu_H$ 中。
同一个 Fourier、满本质支撑及有限柱秩论证排除 $M\ne0$。
$C$ 对称性给稠密值域，定理 1.3 证毕。

本节从未假设 $K$ 的一般元素有界，也没有把 $K$ 上的形式单位直接视为 $\mathcal A$ 单位。
实际使用的始终是 (7.4) 或完全清分母后的 (7.6)。

## 8. 非一元解析情形的全部闭解析芽商

现在另假定 $S$ 不是 $A$ 的一元解析芽。定理 1.2 使

$$
\mathscr O=\mathbb C\{z,w\},
\qquad \widehat F=F(A,S)
$$

成为忠实的交换解析演算；定理 1.1 使每个非零 $\widehat F$ 单射稠密。
这是 R135 全部闭商论证的准确输入。其固定 $z$ 坐标 gcd/Bézout 引理是纯标量解析事实，与增量是否真解析无关。

为明确迁移后的域，给 $r=P/Q\in\operatorname{Frac}\mathscr O$、$Q\ne0$ 定义

$$
\operatorname{Dom}T_r
=\{x:\widehat Px\in\operatorname{Ran}\widehat Q\},
\qquad \widehat QT_rx=\widehat Px.
\tag{8.1}
$$

它单值、闭且稠密定义，定义域包含 $\operatorname{Ran}\widehat Q$。

### 8.1 固定坐标 Bézout 与双图逼近

R135 §2 的完整引理给解析 gcd 分解

$$
P=GP_1,\quad Q=GQ_1,\qquad
aP_1+bQ_1=z^m
\tag{8.2}
$$

其中全部量为收敛解析芽，$m\ge0$；共同 $z$ 因子已先提出。
其证明是在 $\operatorname{Frac}\mathbb C\{z\}[w]$ 中对首一准备多项式取 gcd，再用根有界性去掉因子系数的亚纯奇点，最后清除有限个 $z$ 极点。没有改变 $A$ 所对应的坐标。

因为 $\widehat G$ 单射，最大图方程等价于
$\widehat P_1x=\widehat Q_1y$。
R23 给 $E_n=e_n(A)\to I$ 强收敛、$\|E_n\|\le1$，且形式阶趋无穷；充分大 $n$ 可写 $E_n=A^m r_n(A)$。
置

$$
h_n=r_n(A)(\widehat b x+\widehat a y).
$$

由 (8.2) 直接得到两个图坐标同时收敛：

$$
(\widehat Q_1h_n,\widehat P_1h_n)
=(E_nx,E_ny)\longrightarrow(x,y).
\tag{8.3}
$$

$\widehat G$ 值域稠密，再将每个 $h_n$ 逼近为 $\widehat Gk_n$，便恢复原始分母的图核心：

$$
\boxed{
\operatorname{Graph}T_r
=\overline{\{(\widehat Qh,\widehat Ph):h\in H\}}.
}
\tag{8.4}
$$

参数空间还可缩为 $\mathbb C[A]1$，或全部有限柱向量，因为它们在 $H$ 中稠密，而 $h\mapsto(\widehat Qh,\widehat Ph)$ 有界。
准确的域核心是 $\widehat Q\mathbb C[A]1$ 或 $\widehat Q$ 作用于有限柱；不是未经证明地把原始有限柱全体放进 (8.1)。
若 $P=0$，最大实现为全域零算子，(8.4) 由 $\widehat Q$ 稠密像直接成立。

### 8.2 完整伴随域与闭包运算

核心算子 $T^{(0)}(\widehat Qh)=\widehat Ph$ 的通常伴随满足

$$
(v,w)\in\operatorname{Graph}(T^{(0)})^*
\iff\widehat P^*v=\widehat Q^*w.
$$

由于 $\widehat P^*=C\widehat PC$、$\widehat Q^*=C\widehat QC$，右边等价于
$\widehat P(Cv)=\widehat Q(Cw)$，即最大图。
(8.4) 说明 $\overline{T^{(0)}}=T_r$，故

$$
\boxed{T_r=CT_r^*C.}
\tag{8.5}
$$

任意有界交换子 $B\in\{A\}'$ 保持 (8.1) 的定义域，且 $T_rBx=BT_rx$：直接将 $\widehat Px=\widehat Qy$ 同乘 $B$ 即可。

分式等价 $PQ'=P'Q$ 时，利用单射的有界分母消去可见最大图相同；反向在 $\widehat Q\widehat Q'H$ 比较图并用解析演算忠实性，得到分式相等。
于是这给一个忠实的闭分式演算。

若 $r=P/Q$、$s=F/G$，自然和与自然乘积都在 $\operatorname{Ran}(\widehat Q\widehat G)$ 上有定义，并分别满足

$$
(T_r+T_s)(\widehat Q\widehat Gh)
=(\widehat P\widehat G+\widehat F\widehat Q)h,
\qquad
T_rT_s(\widehat Q\widehat Gh)=\widehat P\widehat Fh.
$$

(8.4) 说明这些核心图的闭包就是对应最大图；反向在整个自然域上乘共同有界分母，可直接验证它们包含在该最大图中。因此

$$
\boxed{
\overline{T_r+T_s}=T_{r+s},\qquad
\overline{T_rT_s}=T_{rs},\qquad
(T_r)^{-1}=T_{1/r}\ (r\ne0).
}
\tag{8.6}
$$

没有声称未经闭包的两个自然乘积域相同。

### 8.3 谱与循环性的准确范围

若 $r$ 非恒定，$P-\lambda Q$ 对每个 $\lambda\in\mathbb C$ 都是非零芽。
同域恒等式

$$
T_r-\lambda I=T_{(P-\lambda Q)/Q}
$$

与定理 1.1 给

$$
\boxed{\ker(T_r-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(T_r-\lambda I)}=H.}
\tag{8.7}
$$

像稠密也可直接看它包含 $\operatorname{Ran}(\widehat P-\lambda\widehat Q)$。
因此每点只可能属于预解集或连续谱。
实际判据仍为

$$
\lambda\in\rho(T_r)
\iff\exists B\in B(H):
(\widehat P-\lambda\widehat Q)B=\widehat Q,
\tag{8.8}
$$

以及

$$
T_r\text{ 有界}
\iff\exists B\in B(H):\widehat QB=\widehat P.
\tag{8.9}
$$

成立时 $B$ 自动与 $A$ 交换，由单射的分子或分母取消即可验证。
这些判据不能替换为标量分式全纯可除性。

对非零 $r$ 及 $x\in\operatorname{Dom}T_r$，还有

$$
\boxed{x\text{ 对 }A\text{ 循环}
\iff T_rx\text{ 对 }A\text{ 循环}.}
\tag{8.10}
$$

例如正向中，$\widehat Px$ 因 $\widehat P$ 稠密像而循环，又
$\widehat Px=\widehat QT_rx$ 属于 $\operatorname{cyc}_A(T_rx)$；反向对 $1/r$ 同理。

## 9. 实际覆盖与未证明范围

若 $B\in\mathcal A$ 的所有 dyadic 差都是真解析演算，而 $E\in\mathcal G$，则

$$
S=B+E
$$

满足 (1.4)。因此其全部实际非零混合解析芽 $F(A,B+E)$ 现在单射稠密；若 $B+E$ 非一元解析，§8 的完整闭商结论也适用。
这里没有对 $E$ 的系数缩放、首阶相对大小、相位或 R148 的固定常数 $8$ 作额外限制。
可用的 $\mathcal G$ 元素包括 R151 已逐项确认的超三次归一化幂系列、相应 Boolean 系列及 R148 的真实低位商实例；不能把任意范数收敛尾自动列入 $\mathcal G$。

§7 还处理 $\mathcal G$ 系数的有限多项式，清分母只发生在一个代数分式域内，并有明确的有界恒等式。
它没有给一般无限 $\mathcal G$ 系数幂级数的收敛判据，也没有给任意 $\mathcal A$ 元素的全部核作分类。

同样，本稿没有证明一般 $F(A,S)$ 在每个未知不变限制上像稠密；除 §7.2 的明确有理分支外，所用的普遍限制稠密性只属于辅助的非零 $\mathcal G$ 元素或 R140 的解析加快尾算子。

闭商有界当且仅当全纯的说法仍然错误：R129/R135 的非解析 $S$ 可满足 $S=AZ$、$Z\in\mathcal A$，使非全纯分式 $w/z$ 有界。
$1/z$ 则给无界但空谱的 $A^{-1}$。所以 (8.7) 也不能加强成任意闭商全平面谱。

完整 Hilbert ISP、实际 $A$ 的全部不变格，以及无额外尾结构的一般高阶核问题仍未由本稿解决。

依赖与交叉引用：

- [R151：四次型解析逼近类及所有不变子商](../notes/2026-11-12-quartic-analytic-approximation-gauge-stability-0c-agent.md)。
- [R140：不变子商的精确四次型](../notes/2026-11-12-invariant-subquotient-type-and-fixed-first-regularization-0c-agent.md)。
- [R129：加性解析 gauge 的混合芽、准备和 Fourier 排核](../notes/2026-11-12-additive-gauge-mixed-analytic-germs-0c-agent.md)。
- [R135：固定坐标解析 gcd 与完整闭商图](../notes/2026-11-12-additive-gauge-meromorphic-closed-quotients-0c-agent.md)。
- R23 的高阶强近似单位、R32 的形式忠实性与唯一字符、R88 的全部交换子 $C$ 对称结构。
