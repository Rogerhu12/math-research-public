# 有限固定底数、原根定理与模 $p^2$ 提升

状态：下列群论比较为已证明；所需的无穷素数输入未得到。本笔记核查 O8 的一个具体候选来源，不给新的 Sha 有限性结论。

## 1. 要检验的办法

有限候选曲线的抽屉原理本身已经合法。一个可能的算术来源是：先选有限多个互相独立的固定整数或固定点，再援引有限候选的原根定理，试图保证至少一个候选对无穷多个素数非 Wieferich。本步必须区分模 $p$ 的乘法阶和模 $p^2$ 的提升。

Heath–Brown 的 *Artin's conjecture for primitive roots*，Quart. J. Math. 37 (1986), 27–38，DOI [10.1093/qmath/37.1.27](https://doi.org/10.1093/qmath/37.1.27)，给有限候选的**模 $p$** 原根结论。其原文书目信息已核；定理范围也可在 Moree 的研究综述 *Artin's primitive root conjecture—a survey*，§6.1，印页 12，及参考文献 [222] 中核对：[作者预印本](https://arxiv.org/pdf/math/0412262)。这里只使用该结论的范围，不将综述当作一个额外的模 $p^2$ 定理。

## 2. 精确提升公式

令 $p$ 为奇素数，$a\in\mathbb Z$ 且 $p\nmid a$。定义
$$
d_p(a)=\operatorname{ord}_{\mathbb F_p^\times}(a),\qquad
q_p(a)=\frac{a^{p-1}-1}{p}\pmod p.
$$
则
$$
\operatorname{ord}_{(\mathbb Z/p^2\mathbb Z)^\times}(a)
=\begin{cases}
d_p(a),&q_p(a)=0,\\
p\,d_p(a),&q_p(a)\ne0.
\end{cases}                                                    \tag{2.1}
$$

证明。模 $p^2$ 的阶是 $d_p(a)$ 或 $p d_p(a)$，因为约化核的阶为 $p$。写 $a^{d_p(a)}=1+pc\pmod {p^2}$。由于 $d_p(a)\mid p-1$，有
$$
q_p(a)=\frac{p-1}{d_p(a)}c\pmod p,
$$
右侧的整数因子是模 $p$ 单位。因此两种情形恰按 $q_p(a)$ 是否为零区分。证毕。

特别地，
$$
a\text{ 是模 }p^2\text{ 原根}
\quad\Longleftrightarrow\quad
d_p(a)=p-1\ \text{且}\ q_p(a)\ne0.                            \tag{2.2}
$$
前一条件完全不包含后一条件。具体地，$7\bmod5$ 是原根，而 $7^4=2401\equiv1\pmod {25}$。更一般地，对每个模 $p$ 原根 $g$，$g^p\bmod p^2$ 仍约化到 $g$，却满足
$$
(g^p)^{p-1}\equiv1\pmod {p^2}.
$$
因此给定一个任意大的奇素数，模 $p^2$ 的 Teichmüller 子群就已经提供了具有最大 tame 阶、但没有任何 wild 一阶提升的元素。这个构造的整数代表随 $p$ 变化；它只反驳从 tame 阶到 wild 提升的逐素数推理，不声称反驳任何固定底数的无穷性猜想。

## 3. 多个底数的准确缺项

设 $a_1,\ldots,a_s$ 是预先固定的非零整数，$p\nmid\prod_i a_i$。Fermat 商满足
$$
q_p(ab)=q_p(a)+q_p(b),\qquad q_p(a^n)=nq_p(a)\pmod p.          \tag{3.1}
$$
故在群 $\langle a_1,\ldots,a_s\rangle$ 上，所需的第一层 wild 信息就是一个线性泛函
$$
(n_1,\ldots,n_s)\longmapsto\sum_i n_iq_p(a_i)\in\mathbb F_p.
$$
至少有一个底数非 Wieferich，当且仅当向量
$$
(q_p(a_1),\ldots,q_p(a_s))\ne0.                              \tag{3.2}
$$
各底数模 $p$ 的阶、乃至它们生成全部 $\mathbb F_p^\times$，都不决定 (3.2)：整个 Teichmüller 子群在约化下同构于 $\mathbb F_p^\times$，而 $q_p$ 在其上恒为零。互相独立的固定底数能否让 (3.2) 对无穷多个 $p$ 成立，仍需一个额外定理；本次核查的原根定理没有给出这个定理。

即使获得 (3.2)，还须另行证明该向量与本课题 $G_p\bmod(p,T)^2$ 或 R27 中心特征空间的算术关系。当前它们并未被识别。已知点非 Wieferich 在本仓库 strict Selmer 比较中只控制一个局部映射，不能直接约束整个相对类群的维数。

## 4. 小原根界不产生有限固定候选

McGown–Sorenson，*Computation of the least primitive root*，2023 修订稿，Theorem 4，证明模 $p^2$ 的最小正原根 $h(p)<p^{2/3}$：[原文](https://arxiv.org/pdf/2206.14193)。这个结论确实包含非 Wieferich 提升，但候选区间随 $p$ 增长，不能把它改写成某个预先固定的有限集合。

这里的量词差别可单独核对。条件
$$
\forall p\quad\exists a\le B(p):\ q_p(a)\ne0,
\qquad B(p)\longrightarrow\infty
$$
不蕴含存在固定 $a$ 对无穷多个 $p$ 成立；抽象关系可以每次仅由一个新的 $a$ 满足。只有 $B(p)$ 在某个无限素数集合上被同一个常数控制，才允许有限抽屉原理。

Katz，*Wieferich past and future*，Contemporary Mathematics 632 (2015), 253–270，§§3–8，明确把固定底数、固定椭圆点及若干点的联合分布写作猜想；见尤其 Conjectures 3.1、7.1、7.3、7.4：[作者稿](https://web.math.princeton.edu/~nmk/wieferich38.pdf)，[出版信息](https://doi.org/10.1090/conm/632/12632)。本笔记不把这些联合分布猜想当作已证明的有限候选输入；也不从没有检索到定理推断任何不可能性。

## 5. 与固定差分路线的接口

在固定整数 $a$ 的差分算子中，记
$$
b_p(a)=\frac{\log\langle a\rangle}{\log(1+p)}.
$$
对于 $p\nmid a$、$a\ne\pm1$，
$$
v_p b_p(a)=v_p(a^{p-1}-1)-1.
$$
所以 $q_p(a)\ne0$ 恰等价于 $b_p(a)\in\mathbb Z_p^\times$。这正是固定差分 Bost 笔记中不能从模 $p$ 原根性质推出的单位性。深度较大时出现的额外圆分 height-one 因子已经在该笔记中单独处理，本处不重复。

结论：有限候选的模 $p$ 原根定理和模 $p^2$ 的小原根上界都没有闭合这条路线。需要的新增输入仍须同时包含固定对象、无穷多个素数及目标的 wild 或 Selmer 控制。
