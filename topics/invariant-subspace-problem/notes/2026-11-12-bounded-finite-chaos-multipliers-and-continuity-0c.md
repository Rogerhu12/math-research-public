# 有限 Walsh 次数中的有界乘法：恰为有界函数，并必有连续代表

日期：2026-11-12（UTC）。会话：Astra-ISP-0c017065。预留 R92。

**状态：以下分类与应用已证明，并已通过独立逐段交叉核验。** 对每个固定有限 Walsh 次数，有界纯乘法向量、有界实际交换乘法向量、有界函数和连续函数四类恰好相同；实际乘子属于范数代数 $\mathcal A$。范数比较常数只依赖次数和固定模型，不依赖使用多少个位。

唯一的外部经典输入是 $c_0$ 上连续标量多项式的有限型一致逼近定理；文末给出已核读的原始研究论文与精确位置。本文不把这一经典输入当作本课题的新结果，其余从 Walsh 系数到算子及连续代表的搬运全部写明。

内部依赖：R88 的纯/实际有界乘法线性双射及其范数界；R32 的 $\mathcal A$ 唯一标量字符；R11 的常向量循环性。

## 1. 陈述及记号

令 $H_{\le p}$ 是 Walsh 次数至多 $p$ 的闭子空间。记 $E_j=e_{10}$，它们作用于不同的两点张量位。对有限柱
$$
f=\sum_S\widehat f(S)\chi_S
$$
定义纯乘子
$$
P_f=\sum_S\widehat f(S)\prod_{j\in S}(I-2E_j).
\tag{1.1}
$$
因为 $(I-2E_j)1=\chi_j$，并且不同位分离，有 $P_f1=f$。

对一般 $f\in H$，所谓纯有界乘子是有界算子 $P\in\{E_j:j\ge0\}'$ 且 $P1=f$；若存在则唯一，因为常向量在这些局部算子的联合多项式下循环。实际有界乘子是 $X\in\{A\}'$ 且 $X1=f$，亦由 $1$ 的循环性唯一。

**定理 1.1。** 对固定 $p<\infty$ 和 $f\in H_{\le p}$，以下等价：

1. $f\in L^\infty(\mu)$；
2. $f$ 的 $L^2$ 类具有连续代表；
3. $f$ 有纯有界乘子 $P_f$；
4. $f$ 有实际有界乘子 $X_f\in\{A\}'$；
5. 存在 $X_f\in\mathcal A=\overline{\mathbb C[I,A]}$ 且 $X_f1=f$。

连续代表唯一，记为 $f^{\rm c}$。此时
$$
c_0(X_f)=f^{\rm c}(0).
\tag{1.2}
$$
若该值非零，则 $X_f$ 可逆，因而 $f$ 对 $A$ 循环。

这个最后条件不是全部非零有界有限 chaos 的循环性判据；$f^{\rm c}(0)=0$ 的一般情形仍未由本条处理。

## 2. 维数无关的实立方体到复多圆盘界

以下只考虑次数至多 $p$ 的有限变量多项式 $P$。允许复系数。假设
$$
|P(x)|\le M\qquad(x\in[-1,1]^n).
\tag{2.1}
$$
将其分为齐次部分 $P=\sum_{k=0}^pP_k$。对固定实 $x$，多项式 $t\mapsto P(tx)$ 在 $[-1,1]$ 上模长至多 $M$。

若 $p\ge1$，在节点 $t_\ell=-1+2\ell/p$、$0\le\ell\le p$ 作 Lagrange 插值。每个基多项式的分子各系数模长之和至多 $2^p$，分母模长为
$(2/p)^p\ell!(p-\ell)!$。所以每个齐次系数满足
$$
\sup_{x\in[-1,1]^n}|P_k(x)|\le A_pM,\qquad
A_p=\frac{(2p)^p}{p!}.
\tag{2.2}
$$
$p=0$ 时取 $A_0=1$。

令 $L_k$ 为 $P_k$ 的对称实 $k$ 重线性形式，值可复。实极化公式给
$$
\|L_k\|\le\frac{k^k}{k!}A_pM.
\tag{2.3}
$$
把它复线性延拓，对 $z=x+iy$、$\|z\|_\infty\le R$，分别有
$\|x\|_\infty,\|y\|_\infty\le R$，因此
$$
|P_k(z)|\le
2^kR^k\frac{k^k}{k!}A_pM.
$$
于是
$$
\boxed{
\sup_{|z_j|\le R}|P(z)|
\le K_p(R)M,\qquad
K_p(R)=A_p\sum_{k=0}^p\frac{(2Rk)^k}{k!}.
}
\tag{2.4}
$$
约定 $0^0=1$。这些常数全部与变量数 $n$ 无关，也不要求多项式齐次。

## 3. 有限柱纯乘子的上界：显式联合酉膨胀

将一个两点空间等距识别为 $L^2(\mathbb T)$ 中的 $\operatorname{span}\{1,z\}$。乘以 $z$ 的酉算子在这个空间上的压缩为 $E=e_{10}$；对每个非负整数 $r$，
$$
E^r=P_{\{1,z\}}M_z^r|_{\{1,z\}},
$$
因为 $r\ge2$ 时两边都为零。

对有限个张量位取这些膨胀的张量积，得到任意多变量解析多项式 $Q$ 的精确压缩及范数界
$$
\|Q(E_0,\ldots,E_{n-1})\|
\le\sup_{|z_j|=1}|Q(z)|.
\tag{3.1}
$$
这一步是显式张量压缩，不需要对一般的交换收缩元组假设多变量 von Neumann 不等式。

设有限柱 $f$ 的符号为
$$
P(z)=\sum_S\widehat f(S)\prod_{j\in S}z_j.
$$
在实立方体内，多仿射插值表明 $P(x)$ 是顶点值的凸组合，所以
$$
\sup_{[-1,1]^n}|P|\le\|f\|_\infty.
$$
由 (1.1)，$P_f=P(I-2E_0,\ldots,I-2E_{n-1})$。在膨胀边界上
$|1-2z_j|\le3$，故 (2.4)、(3.1) 给
$$
\boxed{\|P_f\|\le K_p(3)\|f\|_\infty.}
\tag{3.2}
$$

## 4. 有限柱纯乘子的反向界：产品态与一变量外推

一位 $E$ 的数值域是半径 $1/2$、中心零的闭圆盘；直接取单位向量
$a e_0+b e_1$，期望为 $a\overline b$。特别，对每个实数
$t\in[0,2]$，可选一位单位态使
$$
\langle(I-2E)\psi,\psi\rangle=t.
$$
有限张量产品态因此给
$$
|P(t_1,\ldots,t_n)|\le\|P_f\|
\quad(t_j\in[0,2]).
\tag{4.1}
$$

对顶点 $x\in\{-1,1\}^n$，考察次数至多 $p$ 的一变量多项式
$$
q_x(t)=P(\mathbf 1+t(x-\mathbf 1)).
$$
当 $0\le t\le1/2$ 时，全部坐标在 $[0,1]$，故 $|q_x(t)|\le\|P_f\|$。在节点 $t_\ell=\ell/(2p)$ 作 Lagrange 插值并在 $t=1$ 评价，基多项式分子模长至多一，分母为
$(2p)^{-p}\ell!(p-\ell)!$。所以
$$
|q_x(1)|\le L_p\|P_f\|,\qquad
L_p=\frac{(4p)^p}{p!}.
$$
$p=0$ 时取 $L_0=1$。于是
$$
\boxed{\|f\|_\infty\le L_p\|P_f\|.}
\tag{4.2}
$$
这同样与变量数无关。

## 5. 有界有限 chaos 必有连续代表

令 $f\in H_{\le p}\cap L^\infty$，并记 $f_m$ 为对前 $m$ 位的条件期望。则
$$
\|f_m\|_\infty\le\|f\|_\infty,\qquad f_m\to f\text{ 于 }L^2.
\tag{5.1}
$$
它的多仿射符号记为 $P_m$。在有限支撑的实或复序列上，令
$$
P(x)=P_m(x_0,\ldots,x_{m-1})
\quad\text{当 }\operatorname{supp}x\subseteq[0,m).
\tag{5.2}
$$
此定义与 $m$ 无关：更高位符号项都含一个被设为零的坐标。由 §2，各齐次部分在 $c_{00}$ 的实单位球上维数无关有界；实极化和复化给连续多线性形式，故它们唯一延拓到复 Banach 空间 $c_0$。这样得到次数至多 $p$ 的连续标量多项式 $P$，满足
$$
P_m=P\circ\pi_m,
\tag{5.3}
$$
其中 $\pi_m$ 是前 $m$ 个坐标截断。

现在使用已核读的经典结论：

> $c_0$ 上的每个连续标量齐次多项式，都能在单位球上由有限型多项式一致逼近。

这是 Littlewood–Bogdanowicz–Pełczyński 结果的标准形式；Aron–Hervés–Valdivia 的原始研究论文明确给出该结论及所需的弱一致连续性/逼近论证，见文末来源。分别用于有限个齐次部分即可处理 $P$。

由该定理推出
$$
\|P-P\circ\pi_m\|_{B_{c_0}}\to0.
\tag{5.4}
$$
为把这一推论写明，先选有限型 $Q$ 使 $\|P-Q\|_{B_{c_0}}<\varepsilon$。$Q$ 只含有限个线性泛函 $\varphi_i\in c_0^*=\ell^1$，所以
$\|\varphi_i-\varphi_i\circ\pi_m\|\to0$，从而
$\|Q-Q\circ\pi_m\|_{B_{c_0}}\to0$。于是
$$
\|P-P\circ\pi_m\|_{B_{c_0}}
\le2\varepsilon+\|Q-Q\circ\pi_m\|_{B_{c_0}}.
$$

每个 $P_m-P_n$ 只使用有限坐标。在这些坐标取任意符号、其余坐标设零，是 $B_{c_0}$ 的元素。因此 (5.4) 给
$$
\|f_m-f_n\|_\infty\to0.
\tag{5.5}
$$
有限柱函数遂一致趋于一个连续函数 $f^{\rm c}$；由 (5.1)，它是 $f$ 的代表。Haar 测度对每个非空开集赋正测度，故连续代表唯一。这完整证明定理中的 $1\Rightarrow2$。

这里没有声称一般 $L^\infty$ 函数连续；有限 Walsh 次数正是把数据延拓为一个有限次数 $c_0$ 多项式的条件。

## 6. 从纯乘子回到有界函数及实际范数代数

若 $P\in\{E_j\}'$ 有界且 $P1=f\in H_{\le p}$，压缩到“前 $m$ 位任意、其余位常数”的子空间，得到有限头算子 $P^{(m)}$。它与低位全部 $E_j$ 交换，且
$$
P^{(m)}1=f_m,\qquad \|P^{(m)}\|\le\|P\|.
$$
有限局部代数的常向量循环性使 $P^{(m)}$ 恰等于 (1.1) 的 $P_{f_m}$。因此 (4.2) 给
$$
\|f_m\|_\infty\le L_p\|P\|.
$$
沿一个几乎处处收敛的 $L^2$ 子列取极限，得到
$f\in L^\infty$ 及 $\|f\|_\infty\le L_p\|P\|$。这证明 $3\Rightarrow1$。

反之，若 $f$ 有界，§5 给 $f_m\to f^{\rm c}$ 一致。差 $f_m-f_n$ 仍具有次数至多 $p$，所以 (3.2) 表明 $P_{f_m}$ 按算子范数 Cauchy。极限 $P_f$ 与全部 $E_j$ 交换，且 $P_f1=f$。因此
$$
L_p^{-1}\|f\|_\infty\le\|P_f\|\le K_p(3)\|f\|_\infty.
\tag{6.1}
$$

R88 的双向有界乘法对应给 $3\Leftrightarrow4$，并且实际乘子是纯乘子的有界线性像，常数只依赖固定模型。有限柱实际乘子 $X_{f_m}$ 全部属于 $\mathcal A$。由 (3.2) 和该线性像的范数界，
$$
\|X_{f_m}-X_{f_n}\|
\le C_{\rm model}K_p(3)\|f_m-f_n\|_\infty\to0.
\tag{6.2}
$$
所以极限 $X_f\in\mathcal A$，证明 $1\Rightarrow5$。其余方向显然，五项等价闭合。

## 7. 字符与明确的循环性条件

有限柱的实际乘子可由有限链插值写出。其一变量解析函数的常数项等于 $f_m(0)$：在有限链的第一坐标，所有正幂都为零，因此插值的常数系数就是首坐标值。R88 的实际有限柱实现使用常数项为一的可逆有理修正，故仍有
$$
c_0(X_{f_m})=f_m(0).
$$
字符 $c_0$ 在 $\mathcal A$ 上连续，而 (6.2) 及 $f_m\to f^{\rm c}$ 一致给
$$
c_0(X_f)=f^{\rm c}(0).
$$
由 R32，$\mathcal A$ 中的元素谱为其唯一字符值；因此
$f^{\rm c}(0)\ne0$ 时 $X_f$ 可逆。$X_f$ 与 $A$ 交换，且 $f=X_f1$，所以
$$
\overline{\{p(A)f:p\in\mathbb C[z]\}}
=X_f\overline{\{p(A)1\}}=H.
$$
这给真正的循环性，另一端可为任意 $L^2$，而不仅为有限 chaos。

例如 R88 的 Hadamard 二阶构造 $f$ 连续、纯二阶、Walsh 系数不绝对可和且 $f(0)=0$；本条统一解释 $1+f$ 的实际乘子可逆及其循环性。无需把有界有限 chaos 错当成 Walsh 系数的 $\ell^1$ 类。

## 8. 已核读的经典来源与适用条件

1. R. M. Aron, C. Hervés, M. Valdivia, *Weakly Continuous Mappings on Banach Spaces*, **Journal of Functional Analysis 52** (1983), 189–204, DOI [10.1016/0022-1236(83)90081-2](https://doi.org/10.1016/0022-1236(83)90081-2)。已核读[原文 PDF](https://mate.dm.uba.ar/~slassall/materias/optativas/trabajos/aron-herves-valdivia.pdf)：导言第190页明确陈述 $c_0$ 标量齐次多项式的有限型一致逼近；Theorem 2.9、Corollary 2.11 给弱一致连续性及对偶具有逼近性质时的逼近机制。
2. R. Aron, C. Boyd, Y. S. Choi, *Unique Hahn-Banach Theorems for Spaces of Homogeneous Polynomials*, **J. Austral. Math. Soc. 70** (2001), 387–400, DOI [10.1017/S1446788700002408](https://doi.org/10.1017/S1446788700002408)。已核读[期刊原文 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CA041104BF8C50E51C4C1857EDCC2E2C/S1446788700002408a.pdf/unique_hahnbanach_theorems_for_spaces_of_homogeneous_polynomials.pdf)：Theorem 5 及其证明明确使用 Littlewood–Bogdanowicz–Pełczyński 定理，并给 $c_0$ 多项式在有界集上的弱一致连续性与规范延拓的弱*连续性。

应用中已逐项核对：空间确为复 $c_0$，对象是有限次数的连续标量多项式；其齐次部分由维数无关实立方体估计和极化构造，未把一般可测函数当作 $c_0$ 多项式。公式 (5.4)—(5.5) 给出从经典结论到本 Haar 表示连续代表的独立推导。

## 9. 边界

本条分类有界乘法向量在有限 chaos 中的部分。一般有限 chaos 可以无界，此时两种乘法实现都无界；这不等于原向量不循环。反过来，$f^{\rm c}(0)=0$ 的有界有限 chaos 也不能仅凭乘子在 $\mathcal A$ 中就推出核或循环性结论。

一般双端至少二阶的无限秩矩分离、任意无限 Walsh 次数向量及完整 ISP 仍须继续。

