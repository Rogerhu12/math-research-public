# R38：UHF 内的交换子恰为解析闭包，完整交换子严格更大

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94。

**状态：已证明的中间结论。** 本条识别具体 C* 代数内部的全部交换子，并证明 R37 构造的一个有界交换子不属于该 C* 代数。没有由交换子变大推出非平凡不变子空间；所构造的算子本身仍单射且值域稠密。

## 1. 结论

在 R9 的 Haar 表示中，记

$$
A=M_wU,\quad (Uf)(y)=f(y-1),\qquad
\mathcal C=C^*(I,A),\qquad
\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|}.
$$

R31 已证明 $\mathcal C$ 是具体二进 UHF 代数。R32 构造等距圆作用 $\gamma_\zeta(A)=\zeta A$ 及 Fourier 投影 $\Phi_n$，并证明其 Fejér 和按范数收敛。

**定理 1.1。**

$$
\boxed{\{A\}'\cap\mathcal C=\mathcal A.}
\tag{1.1}
$$

此外存在明确的非零有界算子 $Y$，满足

$$
Y\in\{A\}',\qquad
Y\notin\mathcal C,\qquad
r(Y)=0,\qquad
\ker Y=\{0\},\quad\overline{YH}=H.
\tag{1.2}
$$

$Y$ 由 R37 的有序乘积构造，例如取其参数 $s_j=0$、$t_j=1/(j+2)$。以下重新给出 (1.1) 的完整证明及 $Y\notin\mathcal C$ 的证明；其存在、拟幂零性和单射稠密性质见 R37 的完整构造。

## 2. C* 代数的齐次分量都是单个加权平移

**引理 2.1。** 若 $S\in\mathcal C$ 满足

$$\gamma_\zeta(S)=\zeta^nS\qquad(\zeta\in\mathbb T),$$

其中 $n\in\mathbb Z$，则存在连续函数 $b\in C(\mathbb Z_2)$，使

$$S=M_bU^n.$$

**证明。** 对低 $m$ 位的标准矩阵单位 $e_{r,s}\otimes I$，有

$$
\gamma_\zeta(e_{r,s}\otimes I)=\zeta^{r-s}(e_{r,s}\otimes I).
\tag{2.1}
$$

先对阶数足够高的 dyadic 单位根验证：R32 的字符乘法酉在输入 $s+2^mz$ 与输出 $r+2^mz$ 之间的相位比恰为 $\zeta^{r-s}$。再由圆作用的范数连续性推广到任意 $\zeta$。

同时，若 $r-s=n$，

$$
e_{r,s}\otimes I=M_{\mathbf1_{\{T_m(y)=r\}}}U^n.
\tag{2.2}
$$

因为在该输出柱上，$y-n=s+2^mz$，没有改变尾坐标。

由 R31，取局部矩阵 $S_m\to S$ 于范数。施加范数至多一的 Fourier 投影 $\Phi_n$，有 $\Phi_n(S_m)\to S$。式 (2.1)—(2.2) 表明每个 $\Phi_n(S_m)$ 均为 $M_{b_m}U^n$，其中 $b_m$ 是连续柱函数。平移酉性给

$$\|M_{b_m-b_l}U^n\|=\|b_m-b_l\|_\infty.$$

连续函数的本质上确界等于其上确界，因为 Haar 测度具有满支集。因此 $(b_m)$ 一致 Cauchy，收敛到连续函数 $b$，从而 $S=M_bU^n$。证毕。

本引理并未把整个 $U$ 放入 $\mathcal C$；只有带适当系数的齐次加权平移属于它。

## 3. 齐次交换子的遍历刚性

若 $S=M_bU^n$ 与 $A=M_wU$ 交换，则几乎处处有

$$
b(y)w(y-n)=w(y)b(y-1).
\tag{3.1}
$$

当 $n\ge1$ 时，设 $w_n(y)=\prod_{j=0}^{n-1}w(y-j)$。它几乎处处严格正，且满足同一余循环恒等式

$$w_n(y)w(y-n)=w(y)w_n(y-1).$$

所以有限可测函数 $b/w_n$ 在平移 $y\mapsto y-1$ 下不变。该平移在 $\mathbb Z_2$ 的 Haar 测度下遍历，因此 $b/w_n$ 几乎处处为常数 $c$，得到 $S=cA^n$。

这里即使 $b/w_n$ 未必可积，遍历性仍适用：对它的有界可测函数或复平面有理矩形的逆像应用不变性即可。Haar 平移 $1$ 的遍历性也可从有限阶字符直接验证，非平凡字符在该平移下的特征值都不等于 $1$。

当 $n=0$ 时，(3.1) 直接给 $b(y)=b(y-1)$，所以 $S=cI$。

当 $n=-p<0$ 时，令

$$
v_{-p}(y)=\left(\prod_{j=1}^{p}w(y+j)\right)^{-1}
\quad\text{（几乎处处定义）}.
$$

它同样满足 (3.1)。因此 $b/v_{-p}$ 遍历不变，必为常数 $c$。但 $v_{-p}$ 本质无界：例如 $w(y+1)$ 在趋向 $y=-1$ 的正测度赋值环上任意小，而其余 $p-1$ 个权不超过 $a_0$。由于 $b$ 有界，只能 $c=0$，故 $S=0$。

综上，$\mathcal C$ 中的齐次交换子恰为

$$
\{S:\gamma_\zeta(S)=\zeta^nS,\ SA=AS\}
=
\begin{cases}
\mathbb C A^n,&n\ge0,\\
\{0\},&n<0.
\end{cases}
\tag{3.2}
$$

## 4. 用 Fejér 逼近识别全部相对交换子

设 $S\in\{A\}'\cap\mathcal C$。每个 $\gamma_\zeta(S)$ 都与 $A$ 交换，因为它与 $\gamma_\zeta(A)=\zeta A$ 交换。因此每个 $\Phi_n(S)$ 也与 $A$ 交换。由 (3.2)，其负阶分量为零，非负阶分量为 $c_nA^n$。

R32 的范数 Fejér 逼近于是把 $S$ 写为 $A$ 的多项式的范数极限，即 $S\in\mathcal A$。反向包含显然，因为所有多项式及其范数极限都与 $A$ 交换。这证明 (1.1)。

这个识别只适用于 $\mathcal C$ 内部。不能把任意 $B(H)$ 中的交换子未经证明放进 $\mathcal C$；下一节给出明确的反例。

## 5. R37 的强乘积极限不在解析范数闭包中

采用 R37 的记号，令 $0\le s_j\le t_j<1$，$s,t\in\ell^2$，并且

$$\sum_{j\ge0}(t_j-s_j)=+\infty.$$

令 $F_j=A^{2^j}/\|A^{2^j}\|$。把

$$
g_j(b)=\frac{1+t_j(-1)^b}{\sqrt{1+t_j^2}}
$$

换成

$$
h_j(b)=\frac{1+s_j(-1)^b}{\sqrt{1+s_j^2}}
$$

的有理算子记为 $V_j$。它属于 $\mathcal A$ 且可逆；其常数系数为 $h_j(0)/g_j(0)>0$，所有非常数项的最低次数为 $2^j$。

R37 证明有限乘积 $Y_N=\prod_{j<N}V_j$ 强趋非零 $Y$，并对每个 $N$ 有分解

$$
Y=Y_N Z_N,\qquad
\|Z_N\|\le C_N,\qquad C_N\longrightarrow1.
\tag{5.1}
$$

同时

$$
q_N:=c_0(Y_N)=\prod_{j<N}\frac{h_j(0)}{g_j(0)}
\longrightarrow0.
\tag{5.2}
$$

**命题 5.1。** $Y\notin\mathcal A$。

**证明。** 反设 $Y\in\mathcal A$。因每个 $Y_N$ 的逆仍在 $\mathcal A$ 中，(5.1) 给 $Z_N=Y_N^{-1}Y\in\mathcal A$。故可以合法地对它应用 R32 的连续系数界：

$$
|c_l(Z_N)|\le C_N/W_l.
\tag{5.3}
$$

固定任意 $r\ge0$。当 $2^N>r$ 后，$Y_N/q_N$ 的前 $r$ 阶形式系数不再变化：新增因子除去常数后，其首个非常数阶至少为 $2^N$。记这些固定系数为 $b_0,\ldots,b_r$。由系数卷积，

$$
c_r(Y)=q_N\sum_{l=0}^{r}b_l\,c_{r-l}(Z_N).
$$

结合 (5.2)—(5.3)，

$$
|c_r(Y)|\le q_NC_N\sum_{l=0}^{r}\frac{|b_l|}{W_{r-l}}
\longrightarrow0.
$$

因此 $Y$ 的每个固定形式系数都为零。R32 的唯一性迫使 $Y=0$，与 R37 的 $Yg=h\ne0$ 矛盾。证毕。

这里没有从强收敛 $Y_N\to Y$ 直接传递范数连续的系数泛函。论证先反设 $Y\in\mathcal A$，再利用可逆有限因子使所有 $Z_N$ 也在该代数中，最后用其统一范数控制。

由于 $Y$ 与 $A$ 交换，若 $Y\in\mathcal C$，定理 1.1 将迫使 $Y\in\mathcal A$。故实际上 $Y\notin\mathcal C$。R37 已证明 (1.2) 中的其余性质，完成定理的第二部分。

## 6. 当前意义与边界

完整交换子代数严格大于多项式的范数闭包，即使后者已经具有唯一形式系数、无零因子和全部有限阶商。R37 的有界强乘积正好给出这个差异的明确见证。

然而 $Y$ 自身单射、值域稠密、拟幂零，不能用其核或闭值域构造真不变子空间。本条没有证明完整交换子等于多项式的强闭包，也没有判定 R28 的可和尾临界算子是否有核。
