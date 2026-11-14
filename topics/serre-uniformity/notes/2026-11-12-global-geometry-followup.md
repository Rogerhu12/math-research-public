# 全局几何续查：二次 Chabauty 点数界、CM 点与 Hecke 对应

日期：2026-11-12。会话：serre-uniformity-astra；geometric_route。

**状态：下面两个点数/同源命题已证明；尚未得到排除全部非 CM 点的统一机制。** 不把 quadratic Chabauty（QC）集合有限误写成 Serre 一致性，也不把本笔记的障碍解释为 QC 方法整体不可行。

## 1. 已经越过的障碍与仍需完成的步骤

Dogra–Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*, Math. Ann. 380 (2021), 393–448，Theorem 1(2)，已经无条件证明：素数层 $p$ 的 $X=X_{\rm ns}^+(p)$ 若亏格至少二且 $X(\mathbb Q)\ne\varnothing$，则每个辅助好素数 $\ell\ne p$ 对应的 $X(\mathbb Q_\ell)_2$ 都有限。因此，不能把“尚未证明整个 Jacobian 的秩等于亏格”当作这里的主要未解决步骤。他们用适当商 $A$ 及 Chow–Heegner 映射处理了这个问题。

本次要检验的是：他们的 **定量上界**，加上 CM 点和 Hecke 算子，能否强到消灭剩余非 CM 点。答案是：以下直接拼接均不能闭合，但这仍留下可明确表述的全局非退化/排除问题。

原文：<https://link.springer.com/article/10.1007/s00208-020-02112-3>，Theorem 1、Proposition 3、§3.1 Corollary 2。2026 年直接用模形式进行 QC 的新算法进展另由 `2026-11-12-quadratic-chabauty-status.md` 核查。

## 2. DLF 的公开点数界无法被 CM 点“填满”

为避免符号冲突，本笔记用 $p$ 表示待排除的表示素数/模曲线层，用 $\ell$ 表示 QC 的辅助素数。

DLF §3.1 Corollary 2 在其陈述的假设下给出
$$\#X(\mathbb Q)< B_{p,\ell}:=
\kappa_\ell\left(\prod_{v\in T_0} n_v\right)
\#X(\mathbb F_\ell)\,F(g),\tag{2.1}$$
其中
$$F(g)=16g^3+15g^2-16g+10,\qquad
\kappa_\ell=1+\frac{\ell-1}{(\ell-2)\log\ell},$$
$T_0$ 是坏约化素数集合，$n_v$ 是相应局部 Kummer 像的有限基数。这里取 $\ell\ge3$。这是一条上界，不是已计算出的 QC 集合精确基数。

### 命题 QG1（点数上界与 CM 点规模的明确差距）

对 $p\ge19$，若 $X_{\rm ns}^+(p)(\mathbb Q)\ne\varnothing$，则 (2.1) 的右端满足
$$B_{p,\ell}>\frac{p^6}{6912}>
13\frac{p(p-1)}2\ge\#X_{\rm ns}^+(p)(\mathbb Q)_{\rm CM}.
\tag{2.2}$$
因此，仅用 (2.1) 和全部已知有理 CM 点，无法推导“不再有其它有理点”。

**证明。** Rebolledo–Wuthrich, *A moduli interpretation for the non-split Cartan modular curve*, Proposition 13，给出
$$g=\frac{p^2-10p+23+6\left(\frac{-1}{p}\right)
+4\left(\frac{-3}{p}\right)}{24}.
$$
因为两个 Legendre 符号都至少为 $-1$，
$$g\ge\frac{p^2-10p+13}{24}\ge\frac{p^2}{48}
\qquad(p\ge19).$$
最后一步等价于 $p^2-20p+26\ge0$，它在 $p\ge19$ 成立。

假设有有理点，则它在每个 $\mathbb Q_v$ 上也给出局部点，故每个 $n_v\ge1$；在好约化辅助素数 $\ell$ 处，其约化也保证 $\#X(\mathbb F_\ell)\ge1$。又 $\kappa_\ell>1$，且对实数 $g$ 有 $15g^2-16g+10>0$，从而
$$B_{p,\ell}>16g^3\ge p^6/6912.$$

$j:X_{\rm ns}^+(p)\to\mathbb P^1$ 的度为
$$\mu=[\mathrm{GL}_2(\mathbb F_p):N_{\rm ns}(p)]
=\frac{p(p-1)}2.$$
有理 CM $j$ 值共有十三个（例如 Zywina, *On the possible images...*, §1.9、Table 1）；每个几何纤维最多有 $\mu$ 个点，因此有理 CM 点总数不超过 $13\mu$。这里故意用很松的界，不需要证明每个 CM $j$ 恰对应一个正规化子级结构。

最后 $p^6/6912>13p^2/2$ 等价于 $p^4>44928$，它在 $p\ge19$ 已成立，因而更有 $p^6/6912>13p(p-1)/2$。证毕。

此命题说的是 **已公布公式本身不能提供点数耗尽论证**；它不排除通过更精细的共同零点计算得到远小于该公式的精确集合。

## 3. Hecke 对应不能从假想反例制造更多有理曲线点

以下用的是 Lemos 2019 的既有定理：若无 CM 的 $E/\mathbb Q$ 有非平凡循环 $\mathbb Q$-同源，则其模 $p$ 表示对每个 $p>37$ 都满射。出处：P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. AMS 371 (2019), Theorem 1.1，<https://arxiv.org/pdf/1702.01985>。

### 引理 QG2（有理目标 $j$ 自动使循环核有理）

设 $E/\mathbb Q$ 无 CM，$C\subset E(\overline{\mathbb Q})$ 是有限循环子群。若
$$j(E/C)\in\mathbb Q,$$
则 $C$ 是 $G_{\mathbb Q}$-稳定的，因而商映射 $E\to E/C$ 在合适的商曲线 $\mathbb Q$-模型上是一条 $\mathbb Q$-同源。

**证明。** 选取具有给定 $j$ 值的椭圆曲线 $E'/\mathbb Q$，以及把商 $E/C$ 识别为 $E'_{\overline{\mathbb Q}}$ 的同构；复合得到核为 $C$ 的同源
$$\varphi:E_{\overline{\mathbb Q}}\to E'_{\overline{\mathbb Q}}.$$
由于 $E$ 无 CM，$E'$ 也无 CM，而 $\operatorname{Hom}_{\overline{\mathbb Q}}(E,E')$ 是秩一的自由 $\mathbb Z$-模：左复合 $\widehat\varphi$ 将它单射到 $\operatorname{End}_{\overline{\mathbb Q}}(E)=\mathbb Z$，其像是非零子群。对任意 $\sigma\in G_{\mathbb Q}$，因为 $E,E'$ 均在 $\mathbb Q$ 上定义，$\sigma$ 给出这个秩一模的一个自同构，必为乘以 $1$ 或 $-1$。因此
$$\sigma\varphi=\pm\varphi,$$
从而 $\sigma C=\ker(\sigma\varphi)=\ker\varphi=C$。特征零下有限 $G_{\mathbb Q}$-稳定子群下降为 $\mathbb Q$ 上的有限 étale 子群概形；其椭圆曲线商及商同源在 $\mathbb Q$ 上存在。证毕。

循环假设只用于随后应用 Lemos；上述核稳定论证对任意有限核的同源也成立。

### 推论 QG3（假想坏像点的循环 Hecke 邻居全部非有理）

设 $E/\mathbb Q$ 无 CM，并且对某个 $p>37$ 有
$$\bar\rho_{E,p}\text{ 不满射}.$$
那么对每个非平凡有限循环 $C\subset E(\overline{\mathbb Q})$，都有
$$j(E/C)\notin\mathbb Q.$$

**证明。** 否则 QG2 给出非平凡循环 $\mathbb Q$-同源，与 Lemos Theorem 1.1 矛盾。证毕。

特别地，对任意素数 $r\ne p$，标准 Hecke 对应 $T_r$ 从该点产生的每个几何邻居都没有有理 $j$ 值，故没有一个是 $X_{\rm ns}^+(p)$ 的有理点。因而不能用“应用越来越多 Hecke 算子会制造越来越多有理点”来超过 QG1 所讨论的上界。

必须区分两件事：

- 单个邻居不有理；
- 全部邻居之和仍是 $\mathbb Q$-有理有效除子，$T_r$ 仍是 Jacobian 上的 $\mathbb Q$-有理算子。

第二点并未被排除，恰恰是使用 Hecke 对应构造 QC 函数的关键输入。

### 推论 QG4（有理几何同源类只有一个 $j$ 值）

在 QG3 的条件下，若 $E'/\mathbb Q$ 与 $E$ 在 $\overline{\mathbb Q}$ 上同源，则 $j(E')=j(E)$。

**证明。** 取秩一模 $\operatorname{Hom}_{\overline{\mathbb Q}}(E,E')$ 的生成元 $\psi$。其核是循环的：若核非循环，则存在素数 $r$ 使 $E[r]\subseteq\ker\psi$，于是 $\psi$ 通过 $[r]:E\to E$ 分解，导致 $\psi$ 在 Hom 模中能被 $r$ 整除，与生成元矛盾。若 $\deg\psi>1$，则 QG2/Lemos 再给出矛盾；故 $\deg\psi=1$，两曲线几何同构。证毕。

## 4. “Jacobian 由 Heegner 点生成”仍不识别曲线点

另一个可能的误用是：DLF 的商 $A$ 由解析秩一新形式构成，Heegner 类生成其有理点的相应分量，所以曲线上的有理点也必为 CM。

这里缺少实质的一步。以下线性代数明确说明了为什么。

### 引理 QG5（秩等于维数时的生成现象没有点的来源信息）

设 $A/\mathbb Q$ 是维数 $d$ 的阿贝尔簇，数域 $F\hookrightarrow\operatorname{End}_{\mathbb Q}(A)\otimes\mathbb Q$ 满足 $[F:\mathbb Q]=d$，且 $\operatorname{rank}A(\mathbb Q)=d$。则
$$A(\mathbb Q)\otimes\mathbb Q$$
是一个一维 $F$-向量空间。于是每个非零 $y$——无论它是否来自 Heegner 构造——都自动生成它：
$$A(\mathbb Q)\otimes\mathbb Q=Fy.$$

**证明。** $F$ 中每个非零元素在有理自同态代数中可逆，所以它在 $A(\mathbb Q)\otimes\mathbb Q$ 上可逆，给出 $F$-向量空间结构。该空间的 $\mathbb Q$-维数为 $d=[F:\mathbb Q]$，故其 $F$-维数为一。证毕。

因此，若 $i:X\to A$ 是所用的 Abel–Jacobi/商映射，那么对任意有理点 $P$ 都有 $i(P)=\alpha y$（模挠），这只是秩与乘法结构的自动后果。它不等价于 $P$ 在原曲线上是 CM 点。很多用于生成 $A(\mathbb Q)$ 的 Heegner 类本来就是高次数 CM 点的迹除子，而非一个有理 CM 曲线点。

要使此结构具有排除力，还须证明 $i(X)$ 与这个有理群的交点只有特定的 CM 类；或者提供足够强、统一于层数的系数/高度控制。现有生成结论没有给出这一额外陈述。只写 $i(P)=\alpha y$ 不会对 $\alpha$ 提供界。

## 5. 接下来真正需要的可检验全局输入

QC 仍是可能路线，但必须新增一个能辨认零点的统一结论，而不只是有限性。例如：

1. 对全部充分大 $p$，构造一组有效的 QC 函数和有限局部高度分支；证明每个不含 CM 点的 $\ell$-进剩余圆盘上无共同零点，并证明 CM 圆盘内没有额外有理零点。
2. 或者证明任何非 CM 有理点会产生超过已知全局上界的 **有理曲线点**。QG3 排除了简单的循环 Hecke 邻居方案，但不排除别的构造。
3. 或者在 Hecke/Heegner 生成结构中证明一个真正统一的高度下界—上界矛盾，而非仅证明投影点在既有 Mordell–Weil 模中。

2026 年 equationless 方法给出可计算的低阶局部函数，但“模辅助素数后次数至多二”不能直接推出每个圆盘最多两个零点：零多项式或重根必须单独处理，而且任何保留下来的有限非 CM 候选仍需排除。条件与 Hensel 认证由另一个笔记详细核查。

本次没有证明上述任一全局输入，故 O1 仍未闭合。QG1–QG5 的作用，是把点数、Hecke 与秩一生成这三个现成输入的逻辑力量精确限定下来，避免把未证明的统一排除藏在“充分多的对应/有限集”几个字里。

## 6. 其余原始来源

- M. Rebolledo and C. Wuthrich, *A moduli interpretation for the non-split Cartan modular curve*, Proposition 13：<https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf>。
- D. Zywina, *On the possible images of the mod $\ell$ representations associated to elliptic curves over $\mathbb Q$*, §1.9 and Table 1：<https://arxiv.org/pdf/1508.07660>。本笔记只用十三个有理 CM $j$ 值的既有分类。

## 7. CM 交点分离进入 QC 时，还需要哪些局部系数

本节把 Love–Studnia–Vonk 的交数方向与 QC 的零点问题接起来。文献中的新交数公式仅作方法定位；下面的解析命题均给出独立证明，不把 2026 年预印本当作本仓库未经证明的定理前提。

### 7.1. 分离给出标签，不给出整个圆盘的零点

Love–Studnia–Vonk, *Arithmetic intersections on non-split Cartan modular curves* (2026), Theorem B 的有限交数公式，其求和支撑由
$$m=\frac{\Delta_1\Delta_2-t^2}{4p^2}\in\mathbb Z_{>0}$$
控制。基本、互素判别式的固定 Heegner 对在 $8p^2>\Delta_1\Delta_2$ 时不贡献有限交数：此时只能有 $m=1$，相应的 $\log d$ 都为零，或者支撑为空。不能把这个观察扩大为所有 CM 点全不相交；同一 CM 域不同非极大整环的判别式对可能在导子素数处持续相交，见该文 §4.2。原文：<https://jonathanlove.info/Love_Studnia_Vonk.pdf>。

本课题另由初等交换子方法处理所需的 CM 分离，见 `notes/2026-11-12-cm-separation.md` 及其结果文件。这里仅使用如下可能获得的输出：对某个适合 QC 的好约化辅助素数 $\ell\ne p$，已知有理 CM 点在 $X(\mathbb F_\ell)$ 中的像互异。因此每个剩余圆盘中至多有一个已知有理 CM 点。

这句话不涉及另外两件事：

1. 这个 CM 点是否是某个 QC 函数的简单零点；
2. 不含已知 CM 点的圆盘是否含 QC 共同零点。

根节点的另一条计数论证考察辅助素数 $5$ 的 $j=0$ 纤维，给出随层 $p$ 线性增长的有限域点，因此需要处理的无已知 CM 点圆盘并不会因 CM 分离而消失。本节不重复该有限群计数。

### 7.2. 精确的解析设置：须覆盖每个局部高度分支

固定一个好约化辅助素数 $\ell$。设 $X(\mathbb Q_\ell)$ 的剩余圆盘为 $D_i$，各有参数 $T_i:D_i\simeq\mathbb Z_\ell$。对每个 $D_i$，允许有有限个分支 $b\in B_i$，分支内有有限个限制幂级数
$$F_{i,b,a}\in\mathbb Z_\ell\langle T\rangle.$$
这里 $\mathbb Z_\ell\langle T\rangle$ 的系数趋于零，故模 $\ell$ 约化是多项式。所需的 QC 包含关系是
$$X(\mathbb Q)\cap D_i\ \subseteq\
\bigcup_{b\in B_i}\{P\in D_i:F_{i,b,a}(T_i(P))=0\text{ 对所有 }a\}.\tag{7.1}$$

不能把某一个有利分支的排除冒充为对并集的排除。每个有理点只需属于某个分支，不必满足其他分支的方程。已知 CM 点也仅在与其相容的分支中保证给出零点。

以下仅假设所用函数及积分参数已经构造，并在需要时额外假设其模 $\ell$ 次数至多二。方程的构造、全局包含式 (7.1) 及这种次数性质，都不由 CM 分离本身推出。2026 年 equationless 方法的准确适用条件，见同日 `quadratic-chabauty-status.md`；特别不能删去所用算法的秩、积分满射或其他适用条件。

### 引理 QG6（已证明）：一个 CM 圆盘的二阶系数证书

设 $F_1,F_2\in\mathbb Z_\ell\langle T\rangle$，并且
$$F_1(0)=F_2(0)=0,\qquad
\bar F_i(T)=a_iT+b_iT^2\in\mathbb F_\ell[T].$$
若
$$a_1b_2-a_2b_1\ne0\quad\text{于 }\mathbb F_\ell,\tag{7.2}$$
则在整个 $\mathbb Z_\ell$ 上，两函数的共同零点恰为 $T=0$。

**证明。** 取 $b_1,b_2$ 的任意整数提升 $\widetilde b_1,\widetilde b_2$。由于两个函数的常数项精确为零，
$$G(T)=\frac{\widetilde b_2F_1(T)-\widetilde b_1F_2(T)}{T}
\in\mathbb Z_\ell\langle T\rangle$$
有定义，其模 $\ell$ 约化是非零常数 $b_2a_1-b_1a_2$。所以对每个 $t\in\mathbb Z_\ell$，$G(t)$ 都是单位。若 $t\ne0$ 且 $F_1(t)=F_2(t)=0$，则 $tG(t)=0$，矛盾。$t=0$ 已知为共同零点。证毕。

这个证书只使用第一、第二系数。在奇素数处，它们分别是 $F_i'(0)$ 和 $F_i''(0)/2$ 模 $\ell$。因此把已知 CM 点移至 $T=0$ 后，(7.2) 是两个 QC 条件的二阶系数矩阵满秩条件。它同时排除了该圆盘内所有未知局部共同零点。

还有更简单的充分条件：若某个 $F$ 满足 $F(0)=0$ 且 $\bar F=aT$、$a\ne0$，则 $F/T$ 在整个 $\mathbb Z_\ell$ 上是单位，同样只剩 $T=0$。对一组模 $\ell$ 次数至多二的函数，这两种情形恰好描述如下第一阶认证：共同模 $\ell$ 根只有 $0$，而且至少一个函数在 $0$ 的导数非零。确实，若没有非零线性约化而所有行 $(a_i,b_i)$ 的秩至多一，则所有非零约化都成比例于一个二次多项式 $T(a+bT)$；当 $a=0$ 时 $0$ 为重根，当 $a\ne0$ 时还有非零共同根 $-a/b$。若所有约化为零，则更不能给出认证。

### 引理 QG7（已证明）：没有已知 CM 点的圆盘需要共同根排除

设 $F_1,\ldots,F_m\in\mathbb Z_\ell\langle T\rangle$。若
$$\gcd\bigl(\bar F_1,\ldots,\bar F_m,T^\ell-T\bigr)=1
\quad\text{于 }\mathbb F_\ell[T],\tag{7.3}$$
则这些函数在 $\mathbb Z_\ell$ 上没有共同零点。

**证明。** $T^\ell-T$ 在 $\mathbb F_\ell$ 上恰有全部 $\ell$ 个元素为根，并且各根均为单根。故 (7.3) 等价于 $\bar F_1,\ldots,\bar F_m$ 在 $\mathbb F_\ell$ 中没有共同根。任何 $\mathbb Z_\ell$ 共同零点约化后会给出这样一个根，矛盾。证毕。

也可用 Euclid 算法给出的 Bézout 恒等式作为有限域证书。这个检验并不要求每个单独函数都无根。若某一对约化的 resultant 非零，也足以推出 (7.3)，但 (7.3) 更精确：共同的不可约高次因子不会产生 $\mathbb F_\ell$ 参数候选。

### 推论 QG8（已证明）：把分离与局部系数合成一个真正的点集认证

在 (7.1) 的设置中，设已知有理 CM 点集 $S$ 在模 $\ell$ 约化下单射。假设对每个 $i$ 和每个 $b\in B_i$，均已完成以下两类认证中的一种：

- 分支内所有函数满足 QG7，故这个分支的共同零点为空；
- $D_i$ 含有 $P_i\in S$，该点是分支内所有函数的精确零点。把参数移至 $P_i$ 为 $0$ 后，分支中存在 QG6 所需的两个函数，或者存在其后所述的非零线性约化函数。

则 $X(\mathbb Q)=S$。

**证明。** 取任意有理点 $P\in D_i$。由 (7.1)，它属于某个分支的共同零点集；该分支不可能是第一类。第二类由 QG6 或其线性情形迫使 $P=P_i\in S$。反向包含由 $S$ 的定义成立。证毕。

此命题只是把尚需的新输入明确成逐圆盘、逐分支的系数条件。如果对全部充分大层 $p$ 证明这些条件，才得到真正的一致性结论；目前并没有证明这种统一系数控制。

### 7.3. 为什么交数数据不能替代这些系数

即使所有已知 CM 点的剩余圆盘都互异、QC 集有限、约化次数至多二，这些信息也不蕴含 QG6 或 QG7。下列一变量模型已足以否定这种纯形式推理：

- 在含已知点 $T=0$ 的圆盘上，$F(T)=T(T-1)$ 仍有另一个局部零点 $1$；两点的参数甚至模 $\ell$ 就不同。
- $F(T)=T^2$ 的零点集虽然只有 $0$，但该零点并非简单根。
- 在没有指定 CM 点的另一个圆盘上，$F(T)=T$ 有一个简单零点。其他圆盘中所有 CM 点彼此分离，对这个方程没有约束。
- 两个在 $\mathbb Q_\ell[T]$ 中线性独立的函数 $F_1=T^2$、$F_2=T^2+\ell T$，约化却都为 $T^2$。因此“取两个独立 Hecke/QC 条件”也不自动使 (7.2) 非零。

这些是逻辑反例，并未声称它们是某层模曲线实际出现的 QC 函数。它们准确指出了缺项：CM–CM 相交长度控制已知点之间的距离；QG6 控制所选解析函数在一个已知点附近的系数；QG7 控制其他圆盘上的函数值。三个对象不同。将有限交数输入用于计算局部高度常数仍有价值，但还必须构造函数并证明这些系数条件，才能从“已知点可分辨”走到“没有未知点”。

### 引理 QG9（已证明）：精确重根也能给出整盘认证

简单根不是必要条件。设 $F\in\mathbb Z_\ell\langle T\rangle$ 已经**精确证明**能被 $T^e$ 整除，其中 $e\ge1$，且
$$\bar F(T)=uT^e,\qquad u\in\mathbb F_\ell^\times.$$
则 $F$ 在 $\mathbb Z_\ell$ 中的零点集恰为 $\{0\}$，尽管 $e>1$ 时该根并不简单。

**证明。** 写 $F=T^eU$。限制幂级数除去有限个起始零系数后仍是限制幂级数，故 $U\in\mathbb Z_\ell\langle T\rangle$；它的模 $\ell$ 约化是非零常数 $u$，因而 $U(t)$ 对所有 $t\in\mathbb Z_\ell$ 都是单位。于是 $F(t)=0$ 当且仅当 $t=0$。证毕。

特别地，若某个 QC 函数在已知 CM 点处精确满足 $F(0)=F'(0)=0$，并且 $\bar F=uT^2$，则一个函数已经足够排除该盘的其他零点。QG8 的第二类证书也可以替换为这个精确因子证书，证明完全相同。

这里“精确”不能删掉：$T^2$ 与 $T^2+\ell^M T$ 的系数模 $\ell^M$ 相同，但后者多出零点 $-\ell^M$。因此，若想利用某种 CM 对称性强制一阶系数消失，必须给出这种消失的数学证明；不能把有限精度计算中暂时看到的零当成精确零。本节没有证明实际 QC 函数在 CM 基点处自动满足这个条件。
