# R12 附录：闭稳定根的伴随域包含迫有界，以及原实际闭实现的限制

日期：2026-11-27（台北时间，UTC+8）。作者：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro；literature_deddens 分证，根会话复核）。

状态：以下一般闭域引理及其原尾应用均有完整证明。
新输入是通常伴随域的实际包含，不是仅有反线性对称性，也不是一般闭算子的幂在其域上有界。
本稿不为未知普通不变子空间诱导的根图自动补出该输入。R161 附录A已在通常伴随同域和有界自交换子形式下处理平方图核心；这里的稳定域结论去掉了有界自交换子假设、只保伴随域包含，并处理任意有限幂。

## 1. 一阶伴随域包含与有限幂有界

**定理 1.1。** 设 $T$ 是复 Hilbert 空间 $H$ 上稠密定义的闭算子，记
$\mathcal D=\operatorname{Dom}T$。假设
$$
T\mathcal D\subseteq\mathcal D,\qquad
\mathcal D\subseteq\operatorname{Dom}T^*,
\tag{1.1}
$$
并且对某个整数 $q\ge2$ 及 $K\ge0$ 有
$$
\|T^q x\|\le K\|x\|\qquad(x\in\mathcal D).
\tag{1.2}
$$
则 $\mathcal D=H$ 且 $T\in B(H)$。

以下给出完整常数和所有中间域。
由闭图定理存在 $a,b\ge0$，使
$$
\|T^*x\|\le a\|Tx\|+b\|x\|
\qquad(x\in\mathcal D).
\tag{1.3}
$$
若可取 $a=0$，则 $\|T\|\le b$。否则可增大 $a$ 使 $a\ge1$，并令
$$
S_{q-1}(a)=\sum_{j=0}^{q-2}a^j.
$$
此时有可用的显式界
$$
\boxed{
\|T\|\le
\max\left\{
2bS_{q-1}(a),\;
2^{1-1/q}a^{(q-1)/2}K^{1/q}
\right\}.
}
\tag{1.4}
$$
当 $q=2$ 时还可直接用更好的界
$$
\boxed{
\|T\|\le\frac{b+\sqrt{b^2+4aK}}2.
}
\tag{1.5}
$$

**证明。** 给 $\mathcal D$ 配完整图范数
$\|x\|_T=(\|x\|^2+\|Tx\|^2)^{1/2}$。
限制映射 $T^*:\mathcal D\to H$ 具有闭图：若
$x_n\to x$ 于 $\|\cdot\|_T$ 且 $T^*x_n\to y$ 于 $H$，
则 $x_n\to x$ 于 $H$；$T^*$ 的闭性给 $x\in\operatorname{Dom}T^*$、$T^*x=y$。
因此闭图定理确实给 (1.3)。不要求 $T^*$ 本身保持 $\mathcal D$。

对任意 $y\in\mathcal D$，域稳定性使
$Ty\in\mathcal D\subseteq\operatorname{Dom}T^*$；同时 $T^2y$ 已有实际定义。
通常伴随关系和 (1.3) 在 $Ty$ 上的应用给
$$
\boxed{
\|Ty\|^2
=\langle T^*Ty,y\rangle
\le\bigl(a\|T^2y\|+b\|Ty\|\bigr)\|y\|.
}
\tag{1.6}
$$
等号右端本为非负实数；最后一项按绝对值估计。
若 $a=0$，除去 $\|Ty\|=0$ 的平凡情形，即得
$\|Ty\|\le b\|y\|$。下面取 $a\ge1$。

固定 $0\ne x\in\mathcal D$，记 $s_j=\|T^jx\|$，$0\le j\le q$。
因为整个 $T$ 轨道留在 $\mathcal D$，(1.6) 对 $T^jx$ 都合法，给
$$
s_{j+1}^2\le a s_j s_{j+2}+b s_j s_{j+1}
\qquad(0\le j\le q-2).
\tag{1.7}
$$
若 $s_1=0$，所需界直接成立。
否则置 $r_1=s_1/s_0$。当
$$
r_1>2bS_{q-1}(a)
\tag{1.8}
$$
时，(1.7) 逐次保证 $s_2,\ldots,s_q$ 都非零，并给
$$
r_{j+1}:=\frac{s_{j+1}}{s_j}
\ge\frac{r_j-b}{a}.
$$
详细归纳为
$$
r_j\ge a^{-(j-1)}
\left(r_1-b\sum_{\ell=0}^{j-2}a^\ell\right)
\ge\frac{r_1}{2a^{j-1}}
\qquad(2\le j\le q).
\tag{1.9}
$$
每一步括号严格为正，所以不存在在使用比值之前先出现零分母的情形。
于是
$$
K\ge\frac{s_q}{s_0}
=\prod_{j=1}^q r_j
\ge\frac{r_1^q}{2^{q-1}a^{q(q-1)/2}}.
\tag{1.10}
$$
这给 (1.4) 中第二项；若 (1.8) 不成立，则给第一项。
若某个 $s_j=0$，它同样只能落在 (1.8) 不成立的分支。
因此包括 $K=0$、$b=0$ 和所有零幂范数的情形都已涵盖。

当 $q=2$，直接由 $s_2\le Ks_0$ 代入 (1.7)，得到
$r_1^2-br_1-aK\le0$，即 (1.5)。

现在 $T$ 在稠密域 $\mathcal D$ 上具有通常范数的统一界。
对任意 $x\in H$ 取 $x_n\in\mathcal D$、$x_n\to x$；
该界使 $Tx_n$ Cauchy。闭性迫 $x\in\mathcal D$ 并给出其唯一极限。
故 $\mathcal D=H$，证明完毕。

## 2. 原尾全部整幂根：伴随域包含不可能

取原尾 $B_m$，有限重数 $k\ge1$，并置
$\mathcal B=I_k\otimes B_m$。
设 $T$ 闭、稠密定义、域 $\mathcal D$ 满足
$$
T\mathcal D\subseteq\mathcal D,\qquad
T^q x=\lambda\mathcal B^p x\quad(x\in\mathcal D),
\qquad \lambda\ne0, p\ge1, q\ge2.
\tag{2.1}
$$
若 $q\nmid pk$，则
$$
\boxed{\mathcal D\not\subseteq\operatorname{Dom}T^*.}
\tag{2.2}
$$
否则定理1.1适用，取
$K=|\lambda|\|B_m^p\|$，得到全域有界 $T$。
(2.1) 随即是全域有界根身份，与已证
$$
X^q=\lambda(I_k\otimes B_m^p)
\quad\Longleftrightarrow\quad q\mid pk
$$
矛盾。此处不用先假设 $T$ 与 $\mathcal B$ 域交换：有界根的整除定理本来就没有该前提。

若另有原共轭 $\mathcal C=I_k\otimes C_m$ 使
$$
T=\mathcal C T^*\mathcal C
\quad\text{（包含定义域的完整等式）},
\tag{2.3}
$$
则 $\operatorname{Dom}T^*=\mathcal C\mathcal D$。
因此在 $q\nmid pk$ 时，这两个真实域必不可比较：
$$
\boxed{
\mathcal D\not\subseteq\mathcal C\mathcal D,
\qquad
\mathcal C\mathcal D\not\subseteq\mathcal D.
}
\tag{2.4}
$$
因为任一包含施加反线性对合 $\mathcal C$ 就给反向包含，遂成为等号，再违反 (2.2)。
特别，没有满足 (2.1)--(2.3) 且 $\mathcal C\mathcal D=\mathcal D$ 的根。
反线性对称性 (2.3) 单独不包含这种域稳定性，本稿没有省略该差别。

## 3. 同一实际闭算子的闭限制或闭部分

本节给定理1.1能直接使用的来源形式，避免另行制造不相容的根域。

设 $S$ 是 $H$ 上稠密定义的闭算子，并且
$$
\operatorname{Dom}S\subseteq\operatorname{Dom}S^*.
\tag{3.1}
$$
令 $E\subseteq H$ 为闭空间，$T$ 是 $E$ 上稠密定义的闭算子，满足
$$
\operatorname{Dom}T\subseteq E\cap\operatorname{Dom}S,
\qquad Tx=Sx\in E\quad(x\in\operatorname{Dom}T).
\tag{3.2}
$$
这是真实闭部分条件，不预设 $E$ 约化 $S$。
对 $x,y\in\operatorname{Dom}T$，(3.1) 给
$$
\langle Ty,x\rangle_E
=\langle Sy,x\rangle_H
=\langle y,S^*x\rangle_H
=\langle y,P_ES^*x\rangle_E.
$$
所以
$$
\boxed{
\operatorname{Dom}T\subseteq\operatorname{Dom}T^*,
\qquad T^*x=P_ES^*x\quad(x\in\operatorname{Dom}T),
}
\tag{3.3}
$$
其中 $T^*$ 是 $E$ 上的通常伴随。

若再有 $T\operatorname{Dom}T\subseteq\operatorname{Dom}T$ 及
$\|T^q x\|\le K\|x\|$，则定理1.1在同一个 $E$ 上给出
$$
\operatorname{Dom}T=E,\qquad T\in B(E).
\tag{3.4}
$$
特别，$E=H$ 时，任何这样的闭限制 $T\subseteq S$ 也被涵盖。

对未知原不变子空间/子商只能得到 (3.4)。
除非已经证明 $E$ 连同其算子与整个有限放大原尾有界同构，
不能把全尾的整除条件 $q\mid pk$ 施于 $E$ 上的限制；这一步不在本引理中自动成立。

## 4. 已有原模型哪些闭实现实际满足这个输入

本节只列已登记且真正支付通常伴随域的闭实现。

1. **R161 的整个第一阶闭乘子。** 对任意复杂 $\ell^2$ 系数
   $u=a_*+\sum_j a_j\chi_j$，R125/R161 的同一个最小闭实现 $X_u$ 满足
   $\operatorname{Dom}X_u=\operatorname{Dom}X_u^*$。
   对任意有界 $F$，$S=X_u+F$ 仍闭，且
   $\operatorname{Dom}S=\operatorname{Dom}S^*$，因为
   $S^*=X_u^*+F^*$ 的域保持不变。
   所以这些原实际算子的每个满足 (3.2) 的闭稳定部分都适用。

2. **R212/R236 已识别的中央闭实现。** 在既定慢平方共振框架中，
   $T=X-Y$、$M=\ker T$、$K=(M\oplus CM)^\perp$。
   R212 的中央闭域稿及 R236 的二阶域稿已明确支付
   $\operatorname{Dom}T_K=\operatorname{Dom}T_K^*$；
   它来自整个域的三块分解及有界外块，不来自形式压缩。
   因而对这个已识别的 $T_K$，或其满足 (3.2) 的真正闭部分，
   若以后取得稳定域上的有界有限幂身份，便可应用定理1.1。

上述结论不识别 R231 的未知头像底空间所诱导的任意根为某个 $X_u+F$ 或 $T_K$ 的闭部分。
也没有从新完整交换子分母障碍中的 $C$ 自伴 $X_f$ 推出
$\operatorname{Dom}X_f=\operatorname{Dom}X_f^*$。
未知根的真正额外任务现在是证明 (1.1) 的伴随域包含，或找到另一种能支付同源全域分母的特殊根方程。

## 5. 已证输入与范围

- [原尾全部整幂有界根及闭根真实域](../results/R12-appendix-all-integer-power-root-multiplicity-and-closed-root-domains.md)；
- [R161：完整第一阶通常伴随同域](../results/R161-first-chaos-adjoint-domain-and-selfcommutator.md)；
- [R212：中央闭域与自然商图](../results/R212-appendix-central-closed-domain-maximal-graph-and-recursion-defect.md)；
- [R236：真实二阶通常伴随域与中央闭实现](../results/R236-appendix-second-order-adjoint-domains-and-bounded-central-products.md)。

一般闭稳定算子只满足某次幂有界时，本稿不作有界性断言。
关键使用发生在 (1.6)：$Ty$ 必须属于通常伴随域，且 $T^*$ 在原 $T$ 图范数中有统一界。
这个输入对上列实际闭实现已付，对未知普通 $M$ 诱导的根仍须单独验证。
