# 第二权的整系数公式及新增一次 Iwasawa 系数

**可信度：全部公式已证明；无穷素数非零仍未证明。** 日期：2026-11-12。本文把 R24 的新增权 $2p-1$ 变成一个完整的有限系数公式，并明确保留 $(2p-2)!$ 的一个 $p$ 因子。最后在 R24 的显式 LT 基下，给出 $g_1\bmod p$ 的公式。

## 1. 固定数据与三个新系数

沿用 R17–R19：
$$
t=-x/y,\quad
A(t)=\frac{\log_E(t)}t
=\sum_{k\ge0}\frac{C_k}{4k+1}t^{4k},
\quad C_k=(-1)^k\binom{2k}{k}17^k,
$$
$$
R(t)=\operatorname{Tr}_{M/K}\frac{\alpha}{1-\alpha^2t^2},
\quad\operatorname{Tr}_{M/K}\alpha=0,
\quad L(t)=\log A(t),
$$
以及旧的四个系数
$$
b_j(p)=[t^{p-1}]R(t)L(t)^j\qquad(0\le j\le3).
$$
因此 $R\in t^2\mathcal O_{K,\mathfrak p}[[t]]$。仍设 $p\ge13$ 为 good split 素数、$p\ne17$，并写
$$
p=4r+1,\quad m=2p-1,\quad C=C_r,
\quad u_{2,p}=\frac{(2p-2)!}{p}\in\mathbb Z_p^\times.
$$

在达到次数 $2p-4$ 之前，$A$ 的系数分母只有 $4r+1=p$ 可能被 $p$ 整除。删去这唯一一项，定义整多项式
$$
A_{\mathrm{reg},p}(t)=
\sum_{\substack{0\le k\le2r-1\\k\ne r}}
\frac{C_k}{4k+1}t^{4k}
\in1+t^4\mathbb Z_p[t],
\qquad L_{\mathrm{reg},p}=\log A_{\mathrm{reg},p}.
\tag{1}
$$
只需要 $L_{\mathrm{reg},p}$ 到次数 $2p-4$；这些系数均 integral。确实，形式对数中的幂次数至多 $(2p-4)/4<p$，其分母没有 $p$ 因子。

令
$$
B_j(p)=[t^{2p-2}]
R(t)A_{\mathrm{reg},p}(t)L_{\mathrm{reg},p}(t)^j,
\qquad j=0,1,2.
\tag{2}
$$
这三个系数均在 $\mathcal O_{K,\mathfrak p}$ 中。因为 $R$ 至少从 $t^2$ 开始，求值只涉及 (1) 已声明为整的有限次数范围。

## 2. 带完整阶乘的第二权公式

记 R24 的对数矩为
$$
\lambda_n=\delta^n\log\Phi(O).
$$
对任意正整数 $n$，Lagrange 反演和 $d\log\Phi/dt=2R$ 给出
$$
\lambda_n=2(n-1)![t^{n-1}]R(t)A(t)^{-n}.
\tag{3}
$$
具体地，若 $z=tA(t)$，则
$$
[z^n]\log\Phi(t(z))
=\frac1n[t^{n-1}]\frac d{dt}\log\Phi(t)\,A(t)^{-n};
$$
乘以 $n!$ 就得到 (3)。

**命题 1。** 在上述所有素位有
$$
\boxed{\quad
\begin{aligned}
\lambda_{2p-1}\equiv2u_{2,p}\Bigl\{
&p\bigl(B_0-2pB_1+2p^2B_2\bigr)\\
&-(2p-1)C
\left(b_0-2pb_1+2p^2b_2-\frac43p^3b_3\right)
\Bigr\}
\pmod{\mathfrak p^4}.
\end{aligned}\quad}
\tag{4}
$$
这里每个 $b_j,B_j$ 都是一个明确的有限系数，没有在 $\alpha^{-1}$ 这个单位处代入无限形式对数。

**证明。** 在所需的次数范围内，
$$
A(t)=A_{\mathrm{reg},p}(t)+\frac Cp t^{p-1}
+O(t^{2p-3}).
$$
平方或更高次出现的特殊项 $Ct^{p-1}/p$ 已有次数至少 $2p-2$；再乘 $R\in t^2\mathcal O[[t]]$ 后不影响目标次数 $2p-2$。因此可准确线性化为
$$
\begin{aligned}
[t^{2p-2}]R A^{-m}
={}&[t^{2p-2}]R A_{\mathrm{reg},p}^{-m}\\
&-\frac{mC}{p}[t^{p-1}]
R A_{\mathrm{reg},p}^{-m-1}.
\end{aligned}
\tag{5}
$$
因为 $m=2p-1$，两个指数分别为
$$
A_{\mathrm{reg},p}^{-m}
=A_{\mathrm{reg},p}\exp(-2pL_{\mathrm{reg},p}),
\qquad
A_{\mathrm{reg},p}^{-m-1}
=\exp(-2pL_{\mathrm{reg},p}).
$$
第一项乘上的 $2(2p-2)!$ 含一个 $p$ 因子，故模 $p^4$ 只保留指数展开的 $j=0,1,2$ 项。第二项的分母 $p$ 抵消这个因子，故需保留 $j=0,1,2,3$。所有可能出现的 $j$ 都小于 $p$，$j!$ 均为单位，所以被省略的项确实达到所称精度。

在第二项的目标次数 $p-1$ 处，乘上 $R$ 后只需要对数到 $p-3$ 次。此范围内 $A_{\mathrm{reg},p}=A$，所以
$$
[t^{p-1}]R L_{\mathrm{reg},p}^j=b_j.
$$
最后代入 (3)、(5)，并保留
$(2p-2)!=p u_{2,p}$，即得 (4)。$\square$

## 3. 与第一 Frobenius 层的低阶对偶

令 $h_p=\bar\pi\bmod p$，并采用第一层笔记的多项式
$$
J_p(X)=h_p^{-1}
\sum_{\substack{0\le k\le2r\\k\ne r}}
\binom{2r}{k}68^{2r-k}\frac{X^{4k+1}}{4k+1}.
$$
该笔记已经证明
$$
\frac{b_0}p\equiv-\operatorname{Tr}_{M/K}J_p(\alpha)
\pmod{\mathfrak p}.
\tag{6}
$$

**命题 2。** 第二权的新最低项满足
$$
\boxed{\quad
B_0\equiv-h_p\operatorname{Tr}_{M/K}J_p(\alpha)
\equiv h_p\frac{b_0}p
\equiv h_pb_1\pmod{\mathfrak p}.
\quad}
\tag{7}
$$
最后一个同余使用 R17 已证明的秩二整除 $b_0-pb_1\in\mathfrak p^2$；前两个不需要额外使用该整除。

**证明。** 令 $A_{*,p}$ 在 (1) 上额外加入 $k=2r$ 的最后一项。由于该项次数为 $2p-2$，它不改变 $[t^{2p-2}]RA_{\mathrm{reg},p}$。对 $0\le k\le2r$，
$$
C_k=\binom{-1/2}{k}68^k
\equiv\binom{2r}{k}68^k\pmod p.
$$
把 $k$ 换成 $2r-k$，并使用
$4(2r-k)+1\equiv-(4k+1)\pmod p$，得到有限 Laurent 多项式恒等式
$$
X^{2p-1}A_{*,p}(X^{-1})
\equiv-h_pJ_p(X)\pmod p.
\tag{8}
$$
另一方面，由 R18 的有理 $R$，
$$
B_0=
\operatorname{Tr}_{M/K}
\bigl(\alpha^{2p-1}A_{*,p}(\alpha^{-1})\bigr).
$$
这里增加的 $k=2r$ 项乘上 $\operatorname{Tr}\alpha=0$，故等式准确成立。对 (8) 取 trace，再用 (6)，即得 (7)。$\square$

此外 $C\equiv h_p\pmod p$。可直接比较
$h_p=\binom{2r}{r}68^r$ 与 $C=(-1)^r\binom{2r}{r}17^r$：二者比值为 $(-4)^r\equiv1$，最后一步是素数 $p=4r+1$ 处 $2$ 的补充二次互反律。它也由 R24 对 Hasse 标量的微分计算得到。

## 4. 首权失效时，明确测出新增的 $g_1$

现在假设首权未达到旧门槛，即
$$
\lambda_p\in\mathfrak p^4.
\tag{9}
$$
R17 和 (3) 给出
$$
b_0\equiv pb_1-\frac{p^2}2b_2
+\frac{p^3}6b_3\pmod{\mathfrak p^4}.
\tag{10}
$$
定义完全整的有限量
$$
\begin{aligned}
\mathcal D_p={}&B_0+(2p-1)Cb_1\\
&-p\left(2B_1+\frac32(2p-1)Cb_2\right)\\
&+p^2\left(2B_2+\frac76(2p-1)Cb_3\right).
\end{aligned}
\tag{11}
$$
把 (10) 代入 (4)，得到
$$
\lambda_{2p-1}\equiv2u_{2,p}p\mathcal D_p
\pmod{\mathfrak p^4}.
\tag{12}
$$

采用 R24 的显式 LT 基，写
$$
H_p(T)=(T-p)^2G_p(T),\qquad
G_p(T)=g_0+g_1T+\cdots.
$$
R24 §6 证明：在 (9) 下，$g_0\in p^2\mathbb Z_p$，
$\lambda_{2p-1}\in p^3\mathbb Z_p$，而且
$$
g_1\equiv\frac{\lambda_{2p-1}}
{4p^3h_p(h_p-1)}\pmod p.
$$
因此 (12) 同时证明 $\mathcal D_p\in\mathfrak p^2$。Wilson 定理又给
$$
u_{2,p}=\frac{(2p-2)!}{p}
\equiv(p-1)!(p-2)!\equiv-1\pmod p.
$$
于是有明确公式
$$
\boxed{\quad
g_1\equiv
-\frac{\mathcal D_p}{2p^2h_p(h_p-1)}\pmod p,
\qquad\text{若 }\lambda_p\in\mathfrak p^4.
\quad}
\tag{13}
$$
分母除去已说明的 $p^2$ 后为单位，因为 $h_p\ne0,1$（R7 的统一非异常性）。所以这确实是可计算的 integral quotient，而不是一个未定义的模 $p$ 除法。

由 R24，若 (9) 成立且 (13) 非零，便有
$$
v_p\lambda_{2p-1}=3,
\qquad\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
$$
这段使用 R24 的中心零点阶论证先得到有限；后续 R25 已通过有限 Selmer 与原始 Galois 模比较，将同一条件加强为整个初级部分为零。

## 5. 目前新增的信息及尚未消去的量

公式 (13) 检测的是 $G_p$ 的一次系数。它不是 R20 已有的 $g_0$ 条件的重复：R24 已证明存在形式上允许的情形 $g_0\in p^2$、$g_1$ 为单位，此时第一权失败而第二权给出有限性证书。

本次已把这个新方向表达为固定 $R,A$ 的有限系数，并准确处理了第二权首次出现的 $p$ 分母。首层 Frobenius 也确实解释了 (7) 的必要相消。然而仍需控制 (11) 除以 $p^2$ 以后的值：三个新系数 $B_0,B_1,B_2$ 与旧 $b_1,b_2,b_3$ 的组合可能进一步相消。四层 Frobenius 递推可以继续代入这些有限量，但其多项式长度仍随 $p$ 增长，目前没有证明该组合在无穷多个 $p$ 处非零。

## 依赖

- R17、R18：四层截断整性、固定有理 $R$ 与零 trace。
- R19：$d\log\Phi/dt=2R$ 及对数矩。
- R24：显式 LT 基、全权单位矩、两个权的 Selmer 有限性判据及 $g_1$ 规范。
- 第一 Frobenius 层笔记：式 (6) 所用的精确首层 Frobenius trace。

本文的 Lagrange 反演、单个分母层的分离和有限 Laurent 多项式比较均已给出完整推导。
