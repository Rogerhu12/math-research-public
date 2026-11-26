# R1047：原实际 MW 消去格的饱和系数映射与共同零点界

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；root。

**状态：已证明。** R1045/46 的全轮廓非零不仅适用于已命名的
$\Lambda_{\mathcal Q}$：原新部中整个实际 MW 消去格，到前
$(p-2)/3$ 个 CM 系数的映射都是饱和单射。
若该格的秩为 $r_{\rm ann}$，原单位闭盘内全部共同零点的重数和至多
$(p-2)/3-r_{\rm ann}+1$。特别地，同一原盘的有理点至多
$(p-2)/3$ 个，非中心有理点至多 $(p-5)/3$ 个。

这里使用实际全部 MW 消去，并不恢复 R575 已撤回的旧秩零商。
这个随 $p$ 增长的点数界不排除任一非中心候选，不完成 Serre 主目标。

## 1. 保持原对象、尺度与实际消去格

令
$$
p=6N+5>\max\{37,C_*\},\qquad
n_0=2N+1=(p-2)/3,
$$
其中 $C_*$ 是 R1026 的同一个绝对常数。
使用 R1035/37 和 R1038/40 已构造的真实最低型整 Lie 格
$\mathscr L=M_L$、其完美对称型 $B$、以及原 $\delta_*$。
可在一个足够大的有限未分歧整数环 $W$ 上工作；记其分式域为
$K_0$，剩余域为 $k$。原系数固定的 Frobenius 约定保持不变。

由于 $p>3$，原新部是整直和因子
$$
\mathscr L^{\rm new}
=\ker(1+\delta_*+\delta_*^2:\mathscr L\to\mathscr L).
\tag{1047.1}
$$
保留同一个 $P=(p-1)D_0$ 和完整对数
$$
v=\varepsilon^{-1}e_1\log P\in\mathscr L^{\rm new}.
\tag{1047.2}
$$
它的约化是 R1023/38 的全部 $\lambda+R_p$，不能删除返回项。

令 $\mathscr M\subset\mathscr L\otimes_WK_0$ 为原全部有理
Mordell–Weil 点的归一对数所张成的 $K_0$-空间。
对 p5 行，先按 R1038 减去实际 prime-to-$p$ Teichmüller 挠点，
然后才在 formal/good BT 上施 $e_1$；所得对数就是这里使用的对象。
乘整数进入形式群不会改变所张成的空间。
定义
$$
\Sigma
=\{c\in\mathscr L^{\rm new}:B(c,x)=0
                      \text{ 对每个 }x\in\mathscr M\},
\qquad r_{\rm ann}=\operatorname{rank}_W\Sigma.
\tag{1047.3}
$$
这是实际消去空间与整格的交，故是饱和自由子模。
特别地，$\Sigma/p\Sigma\to\mathscr L^{\rm new}/p\mathscr L^{\rm new}$
为单射。又因 $v\in\mathscr M$，每个 $c\in\Sigma$ 都满足
$B(c,v)=0$。

R1037/40 的真实 $c= D\mathcal Qv$ 属于 $\Sigma$ 且为本原向量；
因而
$$
r_{\rm ann}\ge1.
\tag{1047.4}
$$
这里用的是已经证明的全 MW 及其饱和格消去，而非只与单个
$\log P$ 正交。本文不把这两个不同空间混为一谈，也不声称
已算出 $r_{\rm ann}$。

原 $c_1$ 是有理 CM 点，原盘参数与 Lie 值函数为
$$
w=(a-1)/p^3,\qquad
\mathcal H(w)=\frac{e_1\log[P(w)-c_1]}{p\varepsilon}.
\tag{1047.5}
$$
R1033/39 给完整的整 Tate 级数及全部积分尾项：
$$
\mathcal H\in\mathscr L\langle w\rangle,
\quad \mathcal H(0)=0,
\quad \overline{\mathcal H}(w)
=\sum_{n=1}^{n_0}V_nw^n.
\tag{1047.6}
$$
对 $c\in\Sigma$ 置
$$
F_c(w)=B(c,\mathcal H(w))\in W\langle w\rangle.
\tag{1047.7}
$$
原盘内每个有理点 $x$ 都满足 $F_c(w(x))=0$：
$[x-c_1]\in J_1(\mathbf Q)$，其对数在 $\mathscr M$ 中；
除以非零的 $p\varepsilon$ 不改变零值。

## 2. 全部实际消去格的系数映射无额外 p 分母

**定理 1047.1。** 映射
$$
\begin{split}
\mathcal J:\Sigma&\longrightarrow W^{n_0},\\
c&\longmapsto
\bigl([w]F_c,\ldots,[w^{n_0}]F_c\bigr)
\end{split}
\tag{1047.8}
$$
为单射，且像是饱和子模。等价地，它模 $p$ 后仍为单射。

**证明。** 设 $\bar c\in\Sigma/p\Sigma$ 非零。
饱和性保证它在原 $\mathscr L^{\rm new}/p\mathscr L^{\rm new}$
中也非零。由 $B(c,v)=0$，其约化与完整原 $\bar v$ 正交。

R1044 的 p11 旗标和 R1046 的 p5 旗标，分别在原实际模型上给出
$$
B(\bar c,\overline{\mathcal H}(w))=0
\quad\Longleftrightarrow\quad
(b-1)^{2N+2}\mid T_{\bar c}(b)-\gamma A(b)
\quad\text{对某个 }\gamma\in k.
\tag{1047.9}
$$
$T_{\bar c}$ 仍用该两文的原插值、原 Frobenius 与 Serre 尺度；
新部条件给 $T_{\bar c}=T_+(b^3)+b^2T_-(b^3)$。
R1045 的纯代数命题适用于任意 $k$-系数的新部非零向量，
并已证明：与完整 $\bar v$ 正交时，右侧 contact 不可能成立。
该命题不要求 $\bar c$ 本身形如 $D\bar{\mathcal Q}\bar v$。
因此 $\overline{F_c}\ne0$。

结合 (1047.6)，$\overline{F_c}$ 的所有非零系数都在
$1\le n\le n_0$。所以 $\overline{\mathcal J}$ 的核为零。
在离散赋值环上，模 $p$ 满列秩意味着某个
$r_{\rm ann}\times r_{\rm ann}$ 子式为单位；对这些行作逆矩阵
给 $\mathcal J$ 一个整左逆，故像为整直和因子，特别饱和。
$\square$

这同时证明：任取 $\Sigma$ 的整基 $c_1',\ldots,c_{r_{\rm ann}}'$，
多项式 $\overline{F_{c_i'}}$ 在 $k[w]$ 中线性独立，且每一个
本原整线性组合仍保持原尺度 $M=1$。
这里没有把某个最高或最低单系数宣称为单位。

## 3. 不遗漏无限尾的共同零点引理

为避免把多项式约化的根数冒充完整解析函数的根数，下面直接证明
所需 Tate 代数引理。根均在 $\mathbf C_p$ 中，计解析重数。

设 $f=\sum_{n\ge0}a_nw^n\in\mathcal O_{\mathbf C_p}\langle w\rangle$，
其 Gauss 范数为一，令 $h$ 为满足 $|a_h|=1$ 的最大下标。
若 $|\alpha|\le1$ 且 $f(\alpha)=0$，置
$$
b_n=\sum_{j\ge0}a_{n+1+j}\alpha^j.
\tag{1047.10}
$$
因为 $a_n\to0$，这个和收敛，$b_n\to0$，且所有 $b_n$ 都整。
直接比较系数，并以 $f(\alpha)=0$ 处理常数项，得到
$$
f(w)=(w-\alpha)\sum_{n\ge0}b_nw^n.
\tag{1047.11}
$$
对 $n\ge h$，$b_n$ 都在极大理想中；而
$b_{h-1}=a_h+$ 极大理想中的元素，为单位。
因此除去每个盘内根后，最大的单位下标准确下降一。
重复除法证明盘内根的重数和不超过 $h$，也证明商始终整且
Gauss 范数为一；不需要先假设完整根集有限。

现在设 $f_1,\ldots,f_r$ 都满足上述条件，且其约化是次数至多
$n_0$ 的线性独立多项式。以每个公共根在这些函数中的最小重数
计数，令共同零点的总重数为 $q$。它有限，因为已受 $f_1$ 的
有限根数控制。由所有这些公共根组成首一多项式
$$
D(w)=\prod_\alpha(w-\alpha)^{\min_i\operatorname{ord}_\alpha(f_i)},
\qquad\deg D=q.
\tag{1047.12}
$$
$D$ 的系数整；逐次使用 (1047.11)，有
$f_i=Dg_i$，其中 $g_i$ 整、Gauss 范数为一。
$\overline D$ 是次数为 $q$ 的首一多项式，所以
$$
\overline f_i=\overline D\,\overline g_i,
\qquad \deg\overline g_i\le n_0-q.
\tag{1047.13}
$$
原约化的线性独立性在剩余域扩张后仍保持；乘以非零
$\overline D$ 是单射。因此 $r$ 个 $\overline g_i$ 仍线性独立。
次数至多 $n_0-q$ 的多项式空间维数是 $n_0-q+1$，从而
$$
\boxed{\quad q\le n_0-r+1.\quad}
\tag{1047.14}
$$
这份证明处理的是原完整限制级数及其全部根；模 $p$ 多项式
只用来控制整除后的维数。

## 4. 原有理点的实际后果及剩余任务

应用 §3 于 $\Sigma$ 的任一整基所给的 $F_c$，由 §2 得
$$
\sum_{|\alpha|\le1}
 \min_{c\in\Sigma}\operatorname{ord}_\alpha(F_c)
\le \frac{p-2}{3}-r_{\rm ann}+1.
\tag{1047.15}
$$
和只取公共零点；任一基与整个格给出相同的公共零点和最小重数。
所有原有理点都是这些公共零点，而 $w$ 在该实际盘上是参数，
所以不同盘内点有不同的 $w$。故
$$
\boxed{\quad
\#\{x\in X_1(\mathbf Q):x\text{ 在原 }|w|\le1\text{ 盘内}\}
\le\frac{p-2}{3}-r_{\rm ann}+1
\le\frac{p-2}{3}.
\quad}
\tag{1047.16}
$$
中心 $c_1$ 是一个公共零点，至少贡献一重。因此非中心有理点数至多
$$
\boxed{\quad
\frac{p-2}{3}-r_{\rm ann}\le\frac{p-5}{3}.
\quad}
\tag{1047.17}
$$
同样的界适用于原 $v_p(w)>0$ 深盘，特别包括 R317/R378 满足
$v_p(w)=m+3k-3$ 的实际整数候选；仍保留那些结果的全部适用假设。
不把不同盘或不同全局分支自动计入同一个参数盘。

本结果第一次用 R1045/46 的已证原单位尺度和 R1037/40 的实际
全 MW 消去，付清了这个点数结论的两个不同输入。
它不依赖 R378 更正前的秩零商，也不要求简单商的额外 Néron 格
单位比较。原最低单位项、正赋值非中心根的排除，以及 O0 的全部
全局覆盖，仍须继续解决。

## 来源与依赖

- [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)、[R1039](R1039-original-p5-complete-CM-normal-jet-and-rational-disc-scale.md)：原盘、准确归一、完整积分尾和 Tate 整性。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)、[R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：实际全部 MW 的本原消去。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md)、[R1046](R1046-original-p5-complete-CM-flag-and-MW-nonzero-reduction.md)：两行同一实际系数空间与完整 contact 判据。
- [R1045](R1045-original-MW-annihilator-nonzero-reduction.md)：任意新部非零、与原完整 $v$ 正交的行不能满足 contact。

本文只使用上述已登记输入与 §3 的完整解析除法证明；没有数学程序执行或旧窗口重算。
