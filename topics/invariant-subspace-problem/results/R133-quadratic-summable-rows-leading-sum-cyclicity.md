# R133：可和二阶行与非零首行和排核

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**以下条件定理的证明已闭合。** 依赖 R130/R131 的实际二阶闭 C 自伴乘子；本稿重新检查 gauge 同域和 R124 的特殊有界除法，不从纯模型猜测定义域。

## 1. 结论与精确假设

记

$$
f=a_*+\sum_{j\ge0}a_j\chi_j+
\sum_{0\le i<j}b_{ij}\chi_i\chi_j,
\qquad
a\in\ell^2,\quad \sum_{i<j}|b_{ij}|^2<\infty.
\tag{1.1}
$$

把 b 对称延到 i≠j，b_{ji}=b_{ij}。假设每个固定行绝对可和：

$$
\sum_{j\ne i}|b_{ij}|<\infty\qquad(i\ge0).
\tag{1.2}
$$

不要求各行和的总和有限，不要求 f∈L∞。令

$$
\tau_0=a_0+\sum_{j>0}b_{0j}.
\tag{1.3}
$$

**定理1.1。** 若 τ₀≠0，则 f 对 A 循环。更准确地，R131 的闭乘子 X_f 满足，对每个 λ∈C，

$$
\boxed{\ker(X_f-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H.}
\tag{1.4}
$$

更一般地，若 f 不依赖第0到 k−1位，且

$$
\tau_k=a_k+\sum_{j>k}b_{kj}\ne0,
\tag{1.5}
$$

同样成立。“不依赖低 k 位”要求所有带低于 k 的索引的非恒定系数为零；不允许仅从低行和为零推出这一结构。

## 2. 实际二阶闭乘子接口

使用

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad V_j1=\chi_j.
$$

有限部分为

$$
X_n=a_*I+\sum_{j<n}a_jV_j+
\sum_{i<j<n}b_{ij}V_iV_j.
\tag{2.1}
$$

R130 的真实进位次数权界和 R131 的 Dirac/Nelson 证明给一个闭算子 X_f，具有：

1. 有限 chaos 域 𝓓 及有限柱分别为图核心；
2. X_nx→X_fx 对每个 x∈𝓓成立；
3. X_f*=CX_fC，包含定义域等式；
4. 每个 T∈{A}' 保持 DomX_f，并与 X_f 在域上交换；
5. X_f1=f，且 closure RanX_f=closure C[A]f。

这些结论没有假设 (1.2)。本稿额外的行可和性用于下一节的 gauge 差。

## 3. 每个 gauge 差是实际有界算子

固定 dyadic ζ，其阶为 N=2^m。令 U_ζ 为乘以 ζ^{y mod N} 的酉算子，
γ_ζ(T)=U_ζTU_ζ*。若 j≥m，则 γ_ζ(V_j)=V_j。

因此对于 n≥m，

$$
\begin{aligned}
\Delta_{\zeta,n}
&=\gamma_\zeta(X_n)-X_n\\
&=\sum_{i<m}a_i(\gamma_\zeta(V_i)-V_i)\\
&\quad+\sum_{i<j<m}b_{ij}
\bigl(\gamma_\zeta(V_i)\gamma_\zeta(V_j)-V_iV_j\bigr)\\
&\quad+\sum_{i<m}\sum_{m\le j<n}
b_{ij}(\gamma_\zeta(V_i)-V_i)V_j.
\end{aligned}
\tag{3.1}
$$

前两项有限，第三项只有有限个低行。由 (1.2) 及 ∥V_j∥≤6，
它按算子范数收敛。因此

$$
\Delta_{\zeta,n}\longrightarrow\Delta_\zeta\in\mathcal A
\quad\text{于范数}.
\tag{3.2}
$$

它通常不是真正解析芽；本稿不作该假设。

U_ζ双向保持𝓓。先在𝓓使用 (2.1)、(3.2) 取极限，再取双方闭包：
γ_ζ(X_f) 的图核心为 U_ζ𝓓=𝓓，而 X_f+Δ_ζ 是有界扰动，同样以𝓓为图核心。因此

$$
\boxed{\gamma_\zeta(X_f)=X_f+\Delta_\zeta,\qquad
U_\zeta\operatorname{Dom}X_f=\operatorname{Dom}X_f.}
\tag{3.3}
$$

这是闭算子的同域等式，不仅是有限柱上的形式恒等式。

## 4. 零余数消失使有界除法合法

对固定 N 定义余数投影

$$
\mathcal E_{s,N}(T)=\frac1N\sum_{\xi^N=1}
\xi^{-s}\gamma_\xi(T),\qquad0\le s<N.
$$

每个有限 Δ_{\zeta,n} 都是 γ_ζ−I 的像，所以

$$
\mathcal E_{0,N}(\Delta_{\zeta,n})=0.
$$

投影有界，(3.2) 给

$$
\boxed{\mathcal E_{0,N}(\Delta_\zeta)=0.}
\tag{4.1}
$$

这比常数项为零强，且正是本证明所需的实际结构。

R124 的真实有限头压缩给：对任何 T∈𝓐，

$$
\mathcal E_{s,N}(T)=A^sB_s,\qquad
B_s\in\overline{\mathbb C[I,A^N]},
\quad
\|B_s\|\le W_s^{-1}\|\mathcal E_{s,N}(T)\|.
\tag{4.2}
$$

这里有界商来自物理头0到s的压缩与范数极限，不是一般形式除法。

先取 k=0。由 (4.1)—(4.2)，

$$
\Delta_\zeta
=\sum_{s=1}^{N-1}A^sB_s
=A\,U_\zeta',
\qquad
U_\zeta'=\sum_{s=1}^{N-1}A^{s-1}B_s\in\mathcal A.
\tag{4.3}
$$

其常数特征就是 Δ_ζ 的普通一次形式系数。注意 V_j 的常数项为1，
V_0 的一次系数为 −2/d₀，而 j>0 的 V_j 没有一次项。
因此 (3.1) 的连续系数极限给

$$
\chi(U_\zeta')
=\gamma_1(\Delta_\zeta)
=-\frac{2(\zeta-1)}{d_0}
\left(a_0+\sum_{j>0}b_{0j}\right)
=-\frac{2(\zeta-1)}{d_0}\tau_0.
\tag{4.4}
$$

若 τ₀≠0、ζ≠1，U_ζ' 的特征非零，由 R32 它是𝓐单位。

一般情形 (1.5) 令 h=2^k。所有有限 X_n 属于 A^h 的范数代数，
因此 Δ_ζ也属于该代数。当 ζ^h≠1，其阶 N>h，只有余数
h,2h,…,N−h 可能出现；零余数仍由 (4.1) 消失。于是

$$
\boxed{
\Delta_\zeta=A^hU_\zeta',\quad
U_\zeta'\in\mathcal A^\times,\quad
\chi(U_\zeta')
=-\frac{2(\zeta^h-1)}{d_k}\tau_k\ne0.
}
\tag{4.5}
$$

当 ζ^h=1，所有原有限部分都被固定，Δ_ζ=0。有限例外群恰为 μ_h。

本节不能删掉 (4.1)：仅知道某个𝓐元素首阶为1，通常不允许直接除以 A；
这里是 gauge 差的零余数严格消失，才使 (4.3) 合法。

## 5. 同域跨核完成证明

固定 λ，令 M=ker(X_f−λI)。它闭且 A 不变。由 (3.3)，

$$
U_\zeta M=\ker(X_f-\lambda I+\Delta_\zeta),
$$

两核内向量均属于同一个定义域。利用 C 对称性，对 v∈M、
z∈U_ζM，

$$
B(\Delta_\zeta v,z)
=B((X_f-\lambda I+\Delta_\zeta)v,z)
=B(v,(X_f-\lambda I+\Delta_\zeta)z)=0.
\tag{5.1}
$$

每个闭 A 不变空间的 A^h 值域稠密；𝓐单位及其逆保持 M。因此 (4.5) 给

$$
\overline{\Delta_\zeta M}=M
\qquad(\zeta^h\ne1).
$$

从 (5.1) 得 B(M,U_ζM)=0。R122 的 Fourier 机制遂适用：
任意 v,w∈M 的 L¹ 乘积 v(y)w(−1−y) 只含 μ_h 的字符，
所以在 h 个物理柱上为常数。非零闭 A 不变空间的总支撑全测，
逐柱选择非零乘积便使每个柱上的限制秩至多1，故 dimM≤h。
A 单射拟幂零不允许非零有限维不变空间，故 M=0。

C 自伴性再给 ker(X_f−λI)*=C ker(X_f−λI)=0，所以值域稠密。
取 λ=0，结合 §2 第5项得到 f 循环。定理1.1完成。

## 6. 一个无界且每行无限支撑的明确二阶循环向量

取纯二阶系数

$$
b_{ij}=\frac1{(i+j+2)^2}\quad(i<j),\qquad a_*=a_j=0.
\tag{6.1}
$$

其平方和有限：按较大指标 j 分组，和不超过
∑_{j≥1}j(j+2)^{-4}<∞。每个固定行绝对可和，但每行都有无限支撑；
全系数绝对和却无穷，因为对 i<j 有
(i+j+2)^{-2}≥(2j+2)^{-2}，故每个 j 的和至少为
j/(2j+2)²，调和级数发散。

对应 f∈H_{=2} 没有本质有界代表。事实上其前 m 位条件期望是
有限 Walsh 多项式，全部系数为正，故在前 m 位皆为0的正测柱上
等于 ∑_{i<j<m}b_{ij}→∞。若 f∈L∞，条件期望的 L∞范数应被
∥f∥∞一致控制，矛盾。

但

$$
\tau_0=\sum_{j>0}\frac1{(j+2)^2}>0,
$$

所以本定理证明这个具有全部无限行的无界二阶向量对 A 循环，
并证明它的实际闭乘子在每个复数处都单射且值域稠密。

## 7. 直接扰动推论与边界

对任意满足 (1.1)—(1.2) 的 f，所有

$$
f+z\chi_0,\qquad z\ne-\tau_0,
$$

都循环。这里至多留下一个未由本判据处理的参数；不是说那个参数一定非循环。

一般 τ₀=0 的无限行情形仍未由本稿解决。非零高行和不能自动代替
(1.5) 中“不依赖全部较低位”的假设，因为更低余数分量的商可能仍不可继续有界除法。

没有把全部平方可和二阶系数都称为逐行绝对可和，也没有把 C 自伴性本身当作 gauge 同域的充分条件。完整 ISP 目标保持开放。
