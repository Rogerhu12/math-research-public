# 高阶椭圆单位理想：来源状态和精确适用范围

**状态：来源审计与条件比较；不登记为无条件新结果。**

R30 已独立证明，在其记号下
$$
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff q_p\le2
\iff\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)
\not\subset(T-p).
$$
以下核查将右端改写成高阶椭圆单位理想的候选接口。其额外输入是
$$
\tag{H}
\operatorname{Fitt}_{\Lambda,i}(\mathcal A_p)\Lambda_{(T-p)}
=\mathfrak C^{\mathrm{ell}}_{i,p}\Lambda_{(T-p)}
\quad(i\ge0).
$$
本文已检查 Ohshita II 的陈述和适用条件，但尚未确认其出版状态，也未在仓库内重证其核心下界。按课题 README 对尚未公认论证的要求，**(H) 暂列待补来源或证明的输入**。R30 的证明完全不使用它。

## 1. 已核来源与不能直接替换的地方

1. Ohshita 的第一篇发表于 *Kyoto Journal of Mathematics* **53** (2013), 845–887，DOI [10.1215/21562261-2366118](https://doi.org/10.1215/21562261-2366118)。其比较给高阶椭圆单位理想对 Fitting 理想的上界；此单向结论不能独自给出 (H)。
2. 第二篇 *On higher Fitting ideals of Iwasawa modules of ideal class groups over imaginary quadratic fields and Euler systems of elliptic units II* 的 [arXiv 原文](https://arxiv.org/pdf/1710.04568) Corollary 1.2 正是所需两向高度一比较。当前检索未确认出版版本；“未确认”不等于判定其数学结论错误或没有发表。
3. 作者的一般篇 *On higher Fitting ideals of certain Iwasawa modules associated with Galois representations and Euler systems* 已发表于 *Kyoto Journal of Mathematics* **61** (2021), 1–95，DOI [10.1215/21562261-2020-0004](https://doi.org/10.1215/21562261-2020-0004)。已读作者的 [RIMS-1792 原稿](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1792.pdf)：§2 主定理的塔为 $\mathbb Q$ 的圆分 $\mathbb Z_p$ 扩张；Remark 10.1 对虚二次椭圆单位的说明只引第一篇的相应结论。不能仅凭标题中的“一般 Galois 表示”把它直接套到这里的单 $\pi$ 塔。若出版版扩大了这一步，还须以该版的准确陈述为准。
4. Burns–Kurihara–Sano 的 Rubin–Stark/Fitting 结果与 Bley 的 ETNC 定理提供另一条已出版候选路线；目前仍需核实理想定义、层间控制与字符。未把这条路线默认等同于 (H)。

以下保留具体字符与局部条件核查，以免之后重复；所有使用 (H) 或 Ohshita II 核心比较的推论均只按条件比较记录。

## 2. Ohshita II 的字符和塔假设逐项核对

使用 Tatsuya Ohshita，*On higher Fitting ideals of Iwasawa modules of ideal class groups over imaginary quadratic fields and Euler systems of elliptic units II*，[arXiv:1710.04568](https://arxiv.org/pdf/1710.04568)，Theorem 1.1、Corollary 1.2、Definitions 4.4–4.5。所核 PDF 标示修订日期 2021-06-15。

原文的 $X$ 是**处处无分歧**类群 Iwasawa 模，所以此处对应 $\mathcal A_p$，并非 R27 的 $M_p$。原文有限层基域 $K_0$ 取为 $K_1=K(E[\pi])$；其记作 $\psi$ 的有限字符取为本文 $\widetilde\chi$，不是无限 Hecke 字符 $\psi_E$，也不是 $\widetilde\chi^{-1}$。原文把 $\psi$ 分量定义为张量到 $\mathbb Z_p[\operatorname{Im}\psi]$ 的分量，与本文“$\Delta$ 通过 $\widetilde\chi$ 作用”的约定一致。

适用条件如下。

1. $K$ 为虚二次域，$K_1/K$ 有限交换。CM 理论和 R12 给 $\Delta\simeq\mathbb F_p^\times$，故 $p\nmid|\Delta|$。$K_\infty/K$ 交换且 $\Gamma\simeq\mathbb Z_p$，完全属于该文允许的一变量情形。
2. 在 $\mathfrak p$ 处，$K_1/K$ 全分歧，次数 $p-1$；$\widetilde\chi$ 在全 tame 惯性群上忠实，因而在分解群上非平凡。
3. 在 $\bar{\mathfrak p}$ 处，$[\pi]$ 是好约化椭圆方案上的 étale 同源：其微分 $\pi$ 是该处单位。因此 $E[\pi]$ 在该处未分歧。算术 Frobenius 在此挠点直线上的标量为 $\bar\pi\bmod\pi$。R7 的非异常性给
   $$
   \bar\pi\not\equiv1\pmod\pi,
   $$
   因为 $\#E(\mathbb F_p)=(1-\pi)(1-\bar\pi)$。所以 $\widetilde\chi$ 在 $\bar{\mathfrak p}$ 的分解群上也非平凡。
4. $K_1$ 不包含 $\mu_p$。否则 $K(\mu_p)/K$ 作为其子扩张应在 $\bar{\mathfrak p}$ 未分歧，但该圆分扩张在此处全分歧、次数 $p-1>1$，矛盾。特别地，$p$ 不整除 $K_1$ 的单位挠子群阶；原文仅在 $K_0\supset\mu_p$ 时施加的额外 $\omega$ 条件不触发。

若采用 Ohshita II Corollary 1.2，则其结论为所有 $i\ge0$ 的
$$
\operatorname{Fitt}_{\Lambda,i}(\mathcal A_p)
\sim\mathfrak C^{\mathrm{ell}}_{i,p}.
\tag{5.1}
$$
这里 $I\sim J$ 的准确含义是两向包含允许乘以高度至少二的理想。任何这样的误差理想在高度一的 $\mathfrak P$ 处都变成单位理想，所以
$$
\operatorname{Fitt}_{\Lambda,i}(\mathcal A_p)\Lambda_{\mathfrak P}
=\mathfrak C^{\mathrm{ell}}_{i,p}\Lambda_{\mathfrak P}.
\tag{5.2}
$$
这一步不假设 $\mathcal A_p$ 没有有限子模；可能的伪零误差在此局部化中已消去。

在额外比较 (H) 下，R30 的中心 Fitting 判据与 (5.2) 合起来给 $\Sha[p^\infty]$ 有限当且仅当 $\mathfrak C^{\mathrm{ell}}_{2,p}\not\subset(T-p)$。更一般地，
$$
q_p=\min\{i\ge0:\mathfrak C^{\mathrm{ell}}_{i,p}
\not\subset(T-p)\}.
\tag{5.3}
$$

评价 $F(T)\mapsto F(p)$ 的核恰为 $(T-p)$：评价收敛，而整幂级数除以首一线性多项式的余项就是 $F(p)$。所以这个条件比较真正要求非零评价，不要求单位评价。

作为对照，Ohshita Corollary 1.4 另给全局最小生成元数的准确比较。结合 (3.2)，
$$
c_p\le2
\quad\Longleftrightarrow\quad
\mathfrak C^{\mathrm{ell}}_{2,p}=\Lambda.
\tag{5.4}
$$
由 R7，右侧等价于 $\Sha[p^\infty]=0$。因此“理想不是中心素理想的子集”和“理想等于整个局部环”分别对应本题的有限目标与更强的零目标，不能混用。

## 3. Euler 导数的辅助素数与仍需证明的非零性

Ohshita Definitions 4.2、4.4–4.5 以至多 $i$ 个良序辅助素理想的 Kolyvagin 导数，在有限层对所有允许的同态取值，再取投射极限，构造 $\mathfrak C^{\mathrm{ell}}_{i,p}$。因此第 2 个理想涉及至多两个辅助素因子的 Euler 导数；它不是原单个 $\Phi$ 的普通二阶微分，也不是任意一次有限层取值。

辅助素理想 $\mathfrak l$ 的条件见该文 Definition 3.3；其中必含
$$
N\mathfrak l\equiv1\pmod {p^N}.
\tag{6.1}
$$
若预先固定有限个 $\mathfrak l$，则连 $N=1$ 的条件也只可能覆盖有限个 $p$，因为这些 $p$ 都整除固定非零整数
$$
\prod_{\mathfrak l}(N\mathfrak l-1).
$$
这没有禁止辅助素数随 $p$、层数与精度变化；原 Euler 系统论证正允许这样选择。Chebotarev 所保证的无限辅助素数集合却不自动保证相应导数在指定中心 $T=p$ 非零。

当前新的明确开放目标是
$$
\#\{p:\mathfrak C^{\mathrm{ell}}_{2,p}\not\subset(T-p)\}=\infty.
\tag{6.2}
$$
在额外比较 (H) 下，它与初级有限等价，保留非零有限 Sha 的可能性。即使完全补足 (H) 的可引用来源或仓库内证明，(6.2) 的跨素数非零性仍是另一个缺口。本文不把辅助素数的无穷存在、逐 $p$ 的 Euler 系统构造或伪同构分类，误记为主问题完成。

