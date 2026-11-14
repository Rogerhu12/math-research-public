# 无有理 CM 基点的无限层族与无基点 QC

日期：2026-11-12；会话：`serre-uniformity-astra/2026-11-12`。

**状态：下列 F1、F2 已证明；全层无基点 geometric QC 的实现仍是待做方向。** 本笔记仅使用 R9 的有理 CM 点分类，不断言这里的曲线没有非 CM 有理点。

## F1：没有有理 CM 点的层不是有限例外

设
$$
M=8\cdot3\cdot7\cdot11\cdot19\cdot43\cdot67\cdot163
 =16488700536.
$$
对任意素数 $p\equiv1\pmod M$，有 $p>163$，且
$$
X_{\rm ns}^+(p)(\mathbb Q)_{\rm CM}=\varnothing.
$$
这样的素数 $p$ 有无穷多个。

**证明。** 由 $p\equiv1\pmod8$，$\left(\frac{-1}{p}\right)=\left(\frac{-2}{p}\right)=1$。对
$$
q\in\{3,7,11,19,43,67,163\},
$$
有 $q\equiv3\pmod4$，二次互反律给出
$$
\left(\frac{-q}{p}\right)=\left(\frac{p}{q}\right)=1,
$$
最后一步使用 $p\equiv1\pmod q$。这涵盖所有九个类数一虚二次域；余下非基本判别式 $-12,-16,-27,-28$ 与对应基本判别式仅相差平方因子。因此对十三个有理 CM 判别式 $\Delta$ 均有 $\left(\frac{\Delta}{p}\right)=1$。R9 证明这些分裂情形在 $X_{\rm ns}^+(p)$ 上没有有理 CM 点，得到结论。

无穷性甚至不必使用 Dirichlet 定理。给定任意有限个已经列出的素数 $q_1,\dots,q_r\equiv1\pmod M$，令
$$
A=Mq_1\cdots q_r.
$$
取圆分多项式 $\Phi_M(X)$。因 $M>1$，$\Phi_M(0)=1$，故 $\Phi_M(A)$ 与 $A$ 互素；又 $A>2$，利用复根绝对值为 $1$ 得 $\Phi_M(A)>1$。选择任一素因子 $q\mid\Phi_M(A)$。它既不整除 $M$，也不是任何 $q_i$。

模 $q$ 的多项式 $X^M-1$ 平方自由，因为 $q\nmid M$。其分解 $\prod_{d\mid M}\Phi_d(X)$ 的各因子因而两两互素。$A\bmod q$ 是 $\Phi_M$ 的根，却不能是任何真因子阶 $d\mid M$ 的单位根，所以它在 $\mathbb F_q^\times$ 中的乘法阶恰为 $M$。从而 $M\mid q-1$，找到一个新的所需素数。证毕。

这是存在性证明；没有展开次数很大的 $\Phi_M$，也没有生成大型数据。

## 这对现行算法的含义

Hashimoto–Lido–Lombardo–Mascot–Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves* (2026), §3 的主体实现假设已知 $b\in X(\mathbb Q)$，§6.8 的具体模运算选择一个有理 CM 点作为 $b$。[作者预印本](https://arxiv.org/abs/2608.10919)。

F1 证明：用“在每个足够大层任选一个已知有理 CM 点”来启动算法，不能覆盖所有层。这不是少数小层的例外。若 Serre 一致性成立，则 F1 中足够大的层实际上没有任何有理点，因而也不可能选取有理基点。

这不是对 QC 有限性本身的反驳。Dogra–Le Fourn 的有限性定理可在假设有理点存在时应用；若不存在则主目标已满足。但为了不预先知道答案地执行统一算法，应采用无有理基点版本，而不能将“假设存在基点”和“已知可计算基点”混为一谈。

## F2：正次数有理除子给出有限纤维的替代映射

设 $X/\mathbb Q$ 是亏格至少 $1$ 的光滑射影几何连通曲线，$D$ 是次数 $d>0$ 的 $\mathbb Q$ 有理除子。则
$$
\iota_D:X\longrightarrow J=\operatorname{Pic}^0(X),
\qquad x\longmapsto[d\cdot x-D]
$$
是定义于 $\mathbb Q$ 的非恒定态射，且其几何纤维有限。

**证明。** 对称性与除子的有理性给出 $\mathbb Q$ 上的 Picard 态射。为验证纤维，在 $\overline{\mathbb Q}$ 上选择任意 $b\in X(\overline{\mathbb Q})$，并记 $\iota_b(x)=[x-b]$。则
$$
\iota_D(x)=[d]\iota_b(x)+[d\cdot b-D].
$$
正亏格曲线的 Abel–Jacobi 映射 $\iota_b$ 是闭嵌入，而 $[d]:J\to J$ 是有限同源。因此平移后的上述复合非恒定且每个几何纤维有限。证明没有把辅助的几何点 $b$ 当作有理基点。证毕。

对本课题的 $X_{\rm ns}^+(p)$，可以无条件取
$$
D=j^*(\infty),
$$
即 $j$ 映射的极除子。这是正次数的有理尖点除子，即使所有单个尖点均非有理也存在。因此 F1 并未造成“没有任何替代 Abel–Jacobi 映射”的逻辑障碍。

## 尚需落实的部分

八月预印本 Remark 3.0.8 已提出上述 $\iota_D$ 替代，并指出具体问题在于其 line bundle rigidification 使用了有理基点，需要修改；替代映射只有有限纤维，不必单射。本笔记只证明 F2，不声称已经移植该文全部积分 torsor 算法。

下一步应明确：用 $D=j^*(\infty)$ 或更低次数有理除子时，如何构造定义于 $\mathbb Q$ 的提升、如何固定其线丛平凡化，以及如何在有限纤维下将 QC 解集回拉到曲线。即使这些步骤完成，还需证明随层一致排除非 CM 候选；F1、F2 都没有解决这一最终缺口。
