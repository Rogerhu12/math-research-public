# Ogus 扩张与 adelic 复形：单个素数的 Sha 证书为何尚不能传播

日期：2026-11-13。**状态：§2–4 的线性代数和范畴例子已证明；没有构造椭圆曲线的非有限 Sha，也没有证明本课题的跨素数有限性。** 本笔记补充既有 compatible-system-selmer-independence 笔记，不重复 adjoint 或 Larsen–Pink 的范围核查。

## 1. 两个已发表定理之间的准确区别

Andreatta–Barbieri-Viale–Bertapelle, *Ogus realization of 1-motives*, Journal of Algebra **487** (2017), 294–316，Theorem 3.3.5，证明数域上 1-motives 至同源的 filtered Ogus realization 满忠实。其引言明确把 essential image 的刻画列为未解决问题。[作者全文](https://arxiv.org/pdf/1610.04341)，[DOI](https://doi.org/10.1016/j.jalgebra.2017.05.033)。这里的过滤是权过滤，满忠实比较的是两个已经来自 1-motive 的对象之间的 Hom。

Chiarellotto–Mazzari, *Extensions of Filtered Ogus Structures*, Applied Categorical Structures **28** (2020), 143–148，Proposition 3.2、Remark 3.6，则计算该范畴的 Ext，并证明扩张层面的 mixed-motive realization 并非满。例如
$$
\operatorname{Ext}^1_{\mathrm{FOg}(\mathbb Q)}
 (\mathbb Q,\mathbb Q(1))
 =\frac{\prod_p'\mathbb Q_p}
 {\{((1-p^{-1})b)_p:b\in\mathbb Q\}}
$$
不可数，而相应 motivic Ext 为可数的 $\mathbb Q^\times\otimes\mathbb Q$。[已发表作者 offprint](https://nimath.github.io/files/myart08_2020.pdf)，[DOI](https://doi.org/10.1007/s10485-019-09576-8)。

下面直接给出固定椭圆对象的版本，因此不需要从这个 Tate 对象的例子猜测椭圆情形。

## 2. 固定椭圆对象上的完整 Ext 计算

固定 $E/\mathbb Q$，令 $D=T_{\mathrm{dR}}([0\to E])$ 为其二维有理 de Rham realization。对所有好素数 $p$，其 Ogus Frobenius 记作
$$
F_p:D_p\to D_p,\qquad D_p=D\otimes_\mathbb Q\mathbb Q_p.
$$
使用同调型 convention 时 $D$ 的权为 $-1$。因此 $F_p$ 的特征值为权 $-1$ 的 Weil 数，特别地 $1-F_p$ 可逆。这个结论也可在对偶约定下由权 $+1$ 得到；关键只是权不为零，故特征值不为 $1$。

对任意局部向量族 $b=(b_p)_p$，$b_p\in D_p$，在同一个有理空间
$$
V=D\oplus\mathbb Q e
$$
上定义局部 Frobenius
$$
F_{b,p}(v,t)=\bigl(F_pv+(1-F_p)b_p\,t,\ t\bigr).
\tag{2.1}
$$
权过滤为 $W_{-1}V=D$、$W_0V=V$。每个矩阵可逆，其两个 graded pieces 就是原 $D$ 和平凡对象。故它定义一条 filtered Ogus 扩张
$$
0\longrightarrow D\longrightarrow V_b
\longrightarrow\mathbf1\longrightarrow0.
\tag{2.2}
$$
如采用在 almost-all-place 数据上取 2-colimit 的定义，向量族只需在某个余有限好素数集合上给定；忘掉任意有限多个素数不会改变对象。

### 2.1 分裂判据

扩张 (2.2) 在 filtered Ogus 范畴中分裂，当且仅当存在一条**有理**向量 $a\in D$，使
$$
b_p=a\quad\text{对几乎所有 }p.
\tag{2.3}
$$

证明：一个有理 section 必有 $1\mapsto(a,1)$ 的形式。要求它与所有但有限多个 $F_{b,p}$ 交换，准确等于
$$
F_pa+(1-F_p)b_p=a.
$$
因为 $1-F_p$ 可逆，这恰等价于 (2.3)。反向也由同一公式成立。

同理，两条扩张 $V_b,V_c$ 以恒等映射诱导于 subobject 和 quotient 而等价，当且仅当某个 $a\in D$ 满足 $c_p-b_p=a$ 对几乎所有 $p$ 成立。只需把一般的有理上三角换基 $(v,t)\mapsto(v+at,t)$ 代入 (2.1) 即得。

因此本例中扩张的自由度是局部向量族对**对角有理向量**取商；并不由固定的 de Rham 维数或半单 Frobenius 特征多项式控制。

### 2.2 不可数性与缺失的代数化

选 $0\ne v\in D$，只考虑 $b_p\in\{0,v\}$ 的二元向量族。这样的族有 $2^{\aleph_0}$ 个。若两族等价，差必须几乎处处等于同一个 $a\in\{0,v,-v\}$；对任意给定族，可能的等价二元族至多可数，因为还只允许有限处的改变。因此这些族仍给出不可数多个 Ext 类。

另一方面，在 1-motives 至同源的范畴中，以 $[0\to E]$ 为 subobject、$[\mathbb Z\to0]$ 为 quotient 的扩张，正是点所给的 $[\mathbb Z\xrightarrow{P}E]$，允许有理化。其类组成 $E(\mathbb Q)\otimes\mathbb Q$，是可数集合。因此上述 Ogus Ext 的大多数类不能来自这样的 1-motive。

这一结论只用基数和 (2.1) 的完整换基计算。它没有声称任意一条指定的二元族都非 motivic，也没有把 (2.1) 实现为一组全球 $G_\mathbb Q$-表示。

### 2.3 固定 de Rham 空间与完整特征多项式仍不够

所有这些扩张都有同一个 $V_{\rm dR}=D\oplus\mathbb Q$、同一个权过滤，并且逐素数满足
$$
\det(T-F_{b,p})=(T-1)\det(T-F_p),
$$
与 $b$ 无关。甚至每个单独的局部 $F$-isocrystal 扩张都分裂：允许局部 section $(b_p,1)$ 即可。缺的是一个同时适用于几乎所有素数的有理 section。

特别地，任何对 $p=2$、$3$ 或其他固定有限集合的指定，在这个范畴中都被 2-colimit 忘掉。故不能使用 Ogus 全忠实性，把单个 $p$ 的 Selmer 满射证书传到其他素数。

## 3. 与实际 Selmer 群的连接，及其没有支付的部分

实际 Bloch–Kato Selmer 类 $c_p\in H^1_f(\mathbb Q,V_pE)$ 给出全球 Galois 扩张
$$
0\longrightarrow V_pE\longrightarrow W_{c_p}
\longrightarrow\mathbb Q_p\longrightarrow0.
$$
来自 $P\in E(\mathbb Q)$ 的 Kummer 类是固定 1-motive $[\mathbb Z\xrightarrow P E]$ 的 $p$-adic realization。这确实提供了跨 $p$ 的同一个几何对象。

但是已知的共同对象只给
$$
E(\mathbb Q)\otimes\mathbb Q_p
\hookrightarrow H^1_f(\mathbb Q,V_pE).
$$
其余商仍为 $T_p\Sha(E)\otimes\mathbb Q_p$。要从一个 $p_0$ 传播有限性，需额外证明所有相关 $p$ 的全球 Selmer 扩张均来自同一个合理的 motivic Ext 空间，或者证明其维数独立于 $p$。

§2 指出：即使将半单相容表示加强为共同 de Rham 空间、权过滤和所有好素数的 Frobenius，**目标 realization 范畴的 Ext 本身仍过大**。满忠实不能补上这个缺少的满射。这里不排除额外的全球几何条件能刻画 essential image；只是不能把它当作已经由满忠实给出。

## 4. 一个有限自由 adelic 复形也不足以传播维数

另一个具体误用是：先把所有 $p$ 的对象装入一个有限表示的 $\widehat{\mathbb Z}$ 复形，再把有限表示误当作维数独立。下面给出完整反例。

令
$$
R=\widehat{\mathbb Z}=\prod_p\mathbb Z_p,
\qquad e_p=\begin{cases}0,&p=2,3,\\1,&p\ge5.\end{cases}
$$
$e=(e_p)_p\in R$ 是幂等元。考虑集中于次数 $1,2$ 的有限自由复形
$$
C^1=R^2\oplus R^2,\qquad C^2=R^2,\qquad
d(x,y)=(1-e)y.
\tag{4.1}
$$
直接计算得到
$$
H^1(C)=R^2\oplus(eR)^2,\qquad H^2(C)=(eR)^2.
$$
各项以及上同调都是有限生成投射 $R$-模，复形是 perfect，Euler 特征恒为 $-2$。

经第 $p$ 个投影 $R\to\mathbb Z_p\to\mathbb Q_p$ 取 fibre：在 $p=2,3$，微分对第二个直和因子为恒等，因此
$$
\dim H^1(C\otimes_R\mathbb Q_p)=2,\qquad H^2=0;
$$
在每个 $p\ge5$，微分为零，因此
$$
\dim H^1(C\otimes_R\mathbb Q_p)=4,\qquad\dim H^2=2.
$$
固定的首个 $R^2$ 在每个 fibre 都给同一二维子空间。这与“已知 Mordell–Weil 的共同二维子空间”形式一致，但仍容许所有其他素数有额外二维缺陷。

这只是有限自由复形的代数反例，**不是某条曲线的 Selmer complex**。它说明一个共同的 $\widehat{\mathbb Z}$-perfect complex 或一致的有限生成性，比所需的共同有理复形弱得多。若真有固定有限维 $\mathbb Q$ 复形，其各个 $\mathbb Q_p$ base change 的上同调维数当然完全相同，因为域扩张平坦，矩阵的有理秩不会改变；困难仍是为实际 Selmer complex 构造这种有理来源。

## 5. 本次得到的具体结论

对固定 $E$，有理点和由它们组成的 1-motives 已提供真实的跨素数相容对象；原仓库关于 Kummer 塔的结果继续适用。这里新增的是椭圆 Ogus Ext 的完整显式计算，以及有限自由 adelic 复形的例子。二者都准确说明：单个 $2$-adic 或 $3$-adic Sha 有限性不能仅由所核的 realization 全忠实性、共同 Frobenius 半单化、共同 de Rham 维数或 adelic perfectness 传播到无穷多个素数。

还需的正向桥梁必须约束**全球 Selmer 扩张的 essential image 或整个 Selmer 维数**；它不能只约束已经由固定点产生的 Kummer 子空间。
