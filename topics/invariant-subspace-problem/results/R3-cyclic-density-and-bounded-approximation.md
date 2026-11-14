# R3. 稠密循环向量不能延拓到所有向量：一个定量反例和严格循环障碍

日期：2026-11-12。状态：**已证明的路线障碍；不解决完整 Hilbert 不变子空间问题，不宣称文献新颖性。**

严格循环代数部分属于经典理论，参见 Mary R. Embry, *Strictly cyclic operator algebras on a Banach space*, Pacific J. Math. **45** (1973), 443–452，Lemma 2.1、Theorems 3.1–3.2，及下面给出的自含证明。原文：<https://msp.org/pjm/1973/45-2/pjm-v45-n2-p08-s.pdf>。

全文内积对第一变量线性。对 $T\in B(H)$，称 $x$ 循环，如果
$$
\overline{\{p(T)x:p\in\mathbb C[z]\}}=H.
$$
大括号内本来就是线性子空间。所有闭包均为范数闭包，除非另有说明。

## 1. 每个非零多项式向量都循环，算子仍有许多闭不变子空间

**命题 1。** 令 $H=L^2([0,1],dt)$，$Tf(t)=tf(t)$，$\mathcal D=\mathbb C[t]\subset H$。则：

1. $\mathcal D$ 是稠密的 $T$-不变线性子空间；
2. 每个非零 $p\in\mathcal D$ 都是 $T$ 的循环向量；
3. 对每个可测集 $E\subset[0,1]$，满足 $0<|E|<1$ 时，
   $$M_E=\{f\in H:f=0\text{ a.e. on }E^c\}$$
   是非零真闭 $T$-不变子空间，而且 $M_E\cap\mathcal D=\{0\}$。

**证明。** 多项式在 $C[0,1]$ 中一致稠密，而连续函数在 $L^2[0,1]$ 中稠密，因此第 1 条成立。

设 $p\ne0$，且 $g$ 与 $\{t^np:n\ge0\}$ 正交。于是
$$
0=\int_0^1t^np(t)\overline{g(t)}\,dt
 =\langle t^n,\overline p\,g\rangle
\qquad(n\ge0).
$$
因为 $p$ 在 $[0,1]$ 上有界，所以 $\overline p\,g\in H$。由多项式稠密性，$\overline p\,g=0$ a.e.。非零多项式只有有限个零点，故 $g=0$，证明第 2 条。

$M_E$ 是正交投影 $f\mapsto1_Ef$ 的像，因而闭；该投影与 $T$ 交换，所以 $M_E$ 不变。$1_E\ne0$、$1_{E^c}\ne0$ 证明它非零且真。若非零多项式属于 $M_E$，则它在正测度集 $E^c$ 上几乎处处为零，矛盾。∎

特别地，$f=1_{[0,1/2]}$ 可以由非零多项式 $p_j$ 在 $L^2$ 中逼近；每个 $p_j$ 都循环，但 $f$ 不循环。

这排除了如下推理：先在一个稠密的代数核心中证明每个非零向量循环，再仅凭稠密性把循环性延拓到 Hilbert 完备化。

## 2. 上述失败有不可消去的误差放大下界

**命题 2。** 保持上述 $T$，令 $E=[0,1/2]$、$f=1_E$。对任意多项式 $p,q$，设
$$
\delta=\|p-f\|_2,\qquad \varepsilon=\|qp-1\|_2.
$$
则
$$
\boxed{\quad \|q(T)\|\,\delta\ \ge\ \frac1{\sqrt2}-\varepsilon.\quad}
$$

**证明。** 在 $E^c$ 上 $f=0$，因此
$$
\begin{aligned}
\frac1{\sqrt2}
 &=\|1\|_{L^2(E^c)}\\
 &\le\|1-qp\|_{L^2(E^c)}+\|qp\|_{L^2(E^c)}\\
 &\le\varepsilon+\|q\|_{L^\infty[0,1]}\|p-f\|_2.
\end{aligned}
$$
而乘法算子 $q(T)$ 的范数恰为 $\|q\|_{L^\infty[0,1]}$。∎

因此，即使 $p_j\to f$、$q_j(T)p_j\to1$ 同时成立，也必有
$$
\liminf_j\|q_j(T)\|\,\|p_j-f\|_2\ge\frac1{\sqrt2}.
$$
试图使用
$$
\|q_j(T)f-1\|
\le\|q_j(T)\|\,\|f-p_j\|+\|q_j(T)p_j-1\|
$$
传递循环性的证明，在这个例子中不可能使右侧两项同时趋零。这是定量障碍，而不只是“循环性未必闭”的提醒。

## 3. 交换算子代数的严格循环向量迫使伴随有特征向量

记
$$
\mathcal A=\operatorname{Alg}_{\mathrm{WOT}}(T)
 =\overline{\mathbb C[T]}^{\mathrm{WOT}}.
$$
这是含单位的交换、WOT 闭算子代数，也因而是范数闭的 Banach 代数。这里的交换性不能省略：若 $A\in\mathcal A$，则 $A$ 与 $T$ 及每个 $p(T)$ 交换；再让 $p(T)$ 在 WOT 下趋于任意 $B\in\mathcal A$，得到 $AB=BA$。同样，先固定一个多项式再取极限，随后固定 $A$ 再取极限，证明 $AB\in\mathcal A$。

**引理 3。** 若存在 $x\in H$ 满足 $\mathcal A x=H$，则 $T^*$ 有非零特征向量。更一般地，此结论对任意包含 $T,I$ 的交换范数闭算子代数 $\mathcal A$ 成立。

**证明。** 评估映射
$$
E_x:\mathcal A\longrightarrow H,\qquad E_x(A)=Ax
$$
有界且满射。它也是单射：若 $Ax=0$，则对任意 $y=Bx$，交换性给出 $Ay=ABx=BAx=0$，所以 $A=0$。开映射定理给出有界逆 $E_x^{-1}$。

非零含单位交换复 Banach 代数 $\mathcal A$ 存在连续特征标 $\chi:\mathcal A\to\mathbb C$。为明确此标准步骤：取一个代数极大真理想 $J$；$J$ 必闭，因为若其闭包含单位，则 $J$ 中有距单位小于 $1$ 的可逆元，矛盾。于是 $\mathcal A/J$ 是复 Banach 除代数。复 Banach 代数中每个元素的谱非空，而除代数中 $a-\lambda1$ 不可逆意味着 $a=\lambda1$，故 $\mathcal A/J=\mathbb C$。商映射即所需 $\chi$，且 $|\chi(A)|\le\|A\|$。谱非空这一基本事实也可直接由 resolvent 的解析性、无穷远处 Neumann 级数和 Liouville 定理证明。

令 $\ell=\chi\circ E_x^{-1}\in H^*$。它非零，因为 $\ell(x)=\chi(I)=1$。若 $y=Ax$，则
$$
\ell(Ty)=\chi(TA)=\chi(T)\chi(A)=\chi(T)\ell(y).
$$
由 Riesz 表示定理写 $\ell(y)=\langle y,v\rangle$，其中 $v\ne0$，得到
$$
T^*v=\overline{\chi(T)}v.
$$
同时 $\ker\ell$ 是一个余维一的闭 $T$-不变子空间。∎

这正是严格循环理论的经典机制。这里不是把一个未证的外部不变子空间定理作为黑箱。

## 4. 无伴随特征值时，几乎所有目标都要求无界的逼近算子范数

**命题 4。** 假定 $H$ 可分且 $\sigma_p(T^*)=\varnothing$。对每个 $x\ne0$，$\mathcal A x$ 是一个真、第一纲的 $F_\sigma$ 线性子空间。如果 $x$ 循环，则它还是稠密子空间。对其补集中的每个 $y$，任何满足
$$
p_j(T)x\longrightarrow y
$$
的多项式序列都必有
$$
\boxed{\quad\|p_j(T)\|\longrightarrow\infty.\quad}
$$
所以，对一个固定循环向量，必须付出趋于无穷的算子范数的目标构成稠密 $G_\delta$ 集。

**证明。** 引理 3 给出 $\mathcal A x\ne H$。对整数 $m\ge1$ 定义
$$
C_m(x)=\{Ax:A\in\mathcal A,\ \|A\|\le m\}.
$$
$B(H)$ 的闭范数球是 WOT 紧的，$\mathcal A$ 是 WOT 闭的，且 $A\mapsto Ax$ 从 WOT 连续到 $H$ 的弱拓扑。因此 $C_m(x)$ 弱紧，特别是范数闭。

由于 $\mathcal A x=\bigcup_m C_m(x)$ 是真线性子空间，任意 $C_m(x)$ 都没有内点：否则包含它的线性子空间 $\mathcal A x$ 也有内点，从而等于 $H$。故所有 $C_m(x)$ 都是闭无处稠密集。这证明第一纲 $F_\sigma$ 断言；循环性则立即给出稠密性。

现取 $y\notin\mathcal A x$。若 $\|p_j(T)\|$ 不趋于无穷，则存在范数有界子列。可分 Hilbert 空间上，有界算子序列有 WOT 收敛子列（在可数稠密向量对上用对角抽取）。其极限 $A$ 属于 $\mathcal A$，而 $p_j(T)x\to y$ 在范数下成立，迫使 $Ax=y$，矛盾。∎

等价地，对 $y\notin\mathcal A x$ 和任意有限 $R$，存在严格正的逼近下界
$$
\inf\{\|Ax-y\|:A\in\mathcal A,\ \|A\|\le R\}>0.
$$
这里使用了对应集合的范数闭性；若 $x$ 循环，该下界随着 $R\to\infty$ 才可能趋零，命题不给出统一速率。

若 $p_j(z)=\sum_k a_{j,k}z^k$ 且 $R\ge\|T\|$，则
$$
\|p_j(T)\|\le\sum_k|a_{j,k}|R^k.
$$
因此上述残余目标也不可能由加权系数和一致有界的多项式逼近。

## 5. 另一等价的失控形式：范数为一但强趋零的多项式算子

**命题 5。** 若 $x$ 是 $T$ 的循环向量且 $T^*$ 没有特征值，则不存在有限常数 $C$ 使
$$
\|p(T)\|\le C\|p(T)x\|\qquad(p\in\mathbb C[z]).
$$
而且存在多项式 $p_j$ 满足
$$
\|p_j(T)\|=1,\qquad p_j(T)\xrightarrow{\mathrm{SOT}}0.
$$

**证明。** 若存在上述 $C$，则评估映射在范数闭代数 $\mathcal A_0=\overline{\mathbb C[T]}^{\|\cdot\|}$ 上有下界。其像因而闭；又由 $x$ 循环而稠密，所以等于 $H$。引理 3 导致 $T^*$ 有特征向量，矛盾。

因此可取非零 $p_j(T)$，归一化后使 $\|p_j(T)\|=1$、$\|p_j(T)x\|<1/j$。对任意固定多项式 $q$，
$$
\|p_j(T)q(T)x\|=\|q(T)p_j(T)x\|\le\|q(T)\|/j\longrightarrow0.
$$
$\mathbb C[T]x$ 稠密，而 $\|p_j(T)\|=1$ 一致有界，故强趋零成立。∎

## 6. 对完整问题的意义和边界

若存在没有非零真闭不变子空间的 $T$，则每个非零向量都循环，而且 $T^*$ 没有特征值：$T^*$ 的特征向量会给出 $T$ 的不变超平面。因此命题 4、5 必然适用于该反例的每个非零向量。

这些结论既没有构造这样的 $T$，也没有排除其存在。它们具体说明两条路线的缺口：

- 稠密核心上每个非零向量循环，不足以证明完备化后每个非零向量循环；命题 2 给出了一个不能消去的误差放大下界。
- 若把“无界但可逐次选择的循环逼近”加强为“所有目标均有范数有界的逼近”，则已经进入严格循环理论，并迫使存在不变超平面。这种加强不可能保留一个真正的 ISP 反例。

尚未得到的关键点，是在一般 $T$ 下构造一个非零非循环向量，或控制足够特殊的一族逼近，使所得极限有非零且真闭的循环空间。上述 Baire 结论没有提供这种控制。
