# 公开文献核查：范围、已撤回路线与可定位缺口

日期：2026-11-12（北京时间）。分工：`literature_audit`。这是文献核查和研究入口笔记；没有给出完整 Hilbert 不变子空间问题的答案，也没有独立验证任何外部 Lean proof artifact。

## 1. 检索结论及使用边界

截至本次检索，没有找到可以直接采用的、公认的完整复 Hilbert 空间 ISP 解答。2025 年 Chalendar–Partington 综述仍将该问题作为开放问题；2026 年 OpenAI 结果处理超不变子空间及指定有限因子中的不变投影，其具体模型明确保留普通不变子空间。2026 年 10 月的 Fang–Hou–Jiang–Zhang 工作继续给出等价化和特定充分条件。

这里“没有找到”是本次检索范围内的结论，不是一个关于所有现有文献的数学定理。不能把尚未公认的声称当作已证结果，也不能因为没有找到外部认可就称某篇稿件已被证伪。

## 2. 2026 年 OpenAI 模型明确保留普通不变子空间

原始来源：OpenAI, *Backward intertwiners and a transitive commutant*, 2026-09-27，固定仓库版本 `1581d4cbdd69a0faf34b2089614fe2a814316a6a`。

- [论文目录](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026)
- [原始 PDF 链接；不保存进本仓库](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf)
- [形式化范围说明](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/293.md)

已读取根代理下载的原 TeX `introduction.tex`、`conclusion.tex`，其中对应 §1.2 和 §6.1 的文字直接确认下述区别。模型为

$$
H_0=L^2(\mathbb Z_2,\mu;\ell^2(\mathbb Z)),\qquad
(Sf)(x)=S_xf(x),\qquad S_xe_j=\beta_j(x)e_{j+1}.
$$

Theorem 1.1 给出的每个纤维 $S_x$ 的不变格由坐标尾部构成。因此，对任意 $h\in\mathbb Z$，

$$
L^2\!\left(\mathbb Z_2;
\overline{\operatorname{span}}\{e_j:j\ge h\}\right)
$$

是 $S$ 的非零真闭不变子空间。另一个与 $S$ 交换的算子 $V$ 把这些尾部向后移动；$S,V$ 与全部标量乘子生成的代数传递。正是这项更强的共同不变要求排除了超不变子空间。本文主结论不是 $S$ 没有普通不变子空间。

形式化范围说明中的两个链接

- [ComparatorChallenges/BackwardIntertwiners.lean](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/BackwardIntertwiners.lean)
- [ComparatorChallenges/HyperinvariantSubspaces.lean](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/HyperinvariantSubspaces.lean)

确实量化所有闭复线性子空间并表述换位代数传递。但它们是 comparator statement 文件，以 `by sorry` 结束；阅读陈述文件不等于检查了另外提供的证明。本次未运行 comparator，也未核验完整 proof artifact。这个限制不构成对数学结论的否定。

伴随论文 *Invariant-projection counterexamples for every irrational rotation* 的限定是“投影属于指定的有限因子”。它不能直接排除 $B(H)$ 中其余正交投影。

## 3. 已撤回的等价化不能使用

László Kérchy and Carl Pearcy, *Hyperinvariant subspaces of block-triangular operators on Hilbert space*, [arXiv:2503.13005](https://arxiv.org/abs/2503.13005)。v1 为 2025-03-17，v2 为 2025-03-29 的撤回版本。

原文声称普通不变子空间存在可推出超不变子空间存在，从而两问题等价。arXiv 作者备注明确说明 Hari Bercovici 为 Theorem 3 提供了反例。因此不能把这篇稿件与 2026 年超不变子空间的否定答案拼接成完整 ISP 的否定答案。

## 4. Neville 的肯定证明声称：两个独立的可验证问题

Charles W. Neville, *A Proof of the Invariant Subspace Conjecture for Separable Hilbert Spaces*, [arXiv:2307.08176v2](https://arxiv.org/abs/2307.08176v2)，2023-07-21；[HTML 全文](https://arxiv.org/html/2307.08176v2)。

注意：题目 README 来源段将 Neville 的稿件写作“声称反例”，与这里读到的原文不符。原文声称的是肯定证明。本分工不修改 README，由根代理处理。

### 4.1 有限并一般不是线性子空间

Theorem 12.4 的证明，式 (12.6) 定义

$$
V_2=V_1\cup\operatorname{span}\{h_3\}\cup V_{3,m_3+1},
$$

随后把它视为闭线性子空间。有限并确实保持闭性，但一般不保持线性。例如在 $H^2$ 中，$\operatorname{span}(1+z)\cup zH^2$ 包含 $1+z$ 和 $z$，却不包含它们的和 $1+2z$。

### 4.2 把并改成和仍不能得到严格包含

在 $H^2$ 取

$$
V_1=0,\quad V_3=H^2,\quad h_1=1,\quad h_3=1+z.
$$

这符合原证明在此处使用的线性独立和消失阶条件 $m_1\le m_3$，事实上二者阶均为零；但

$$
\operatorname{span}(1+z)+zH^2=H^2.
$$

所以不能从线性独立直接推出 $h_1\notin V_2$。这个例子证明其具体论证步骤不成立，不是否定任何一般的中间子空间定理。

还有一个不依赖于所选 $h_1,h_3$ 的障碍。取有无穷多个零点、但零点不含 $0$ 的 Blaschke 内函数 $\theta$，例如零点 $a_n=1-2^{-n}$。令

$$
V_1=\theta H^2,\qquad V_3=H^2.
$$

$V_1$ 是闭的乘 $z$ 不变子空间，因为乘内函数在 $H^2$ 上等距。商空间无限维：任意有限组不同零点处的求值泛函在商空间上线性独立，这由多项式插值验证。另一方面，对每个整数 $m\ge1$，都有

$$
\theta H^2+z^mH^2=H^2.
$$

证明：$\theta(0)\ne0$。给定 $f\in H^2$，取 $f/\theta$ 在零点 Taylor 展开的前 $m$ 项组成多项式 $p$，则 $f-\theta p$ 在零点至少消失 $m$ 阶，故属于 $z^mH^2$。于是 $f\in\theta H^2+z^mH^2$。这说明通过添加某个有限 jet 的尾部来构造真中间子空间的修补，在这类输入上仍会得到整个 $H^2$。

## 5. Khalil 等 2024 年稿件：错误发生于固定有界泛函的构造

Roshdi Khalil, Abdelrahman Yousef, Waseem Ghazi Alshanti, Ma'mon Abu Hammad, *The Invariant Subspace Problem for Separable Hilbert Spaces*, Axioms **13** (2024), 598，2024-09-02，[期刊原文及 notice](https://www.mdpi.com/2075-1680/13/9/598)，DOI `10.3390/axioms13090598`。

本次访问时，期刊页有 Editorial Office 正调查相关质疑的 notice；没有据此声称已经撤稿。

Theorem 1 构造单位向量 $y_n$，满足

$$
y_n\perp\operatorname{span}\{Tx,T^2x,\ldots,T^nx\}.
$$

式 (20)—(22) 又试图给出一个固定有界线性泛函 $f$，使

$$
f(y_n)=1+\frac12+\cdots+2^{-(n-1)}\longrightarrow2.
$$

**直接证明该步不能成立。** 其反证假设保证 $\operatorname{span}\{T^kx:k\ge1\}$ 稠密。给定 $z\in H$ 和 $\varepsilon>0$，可选有限尾轨道组合 $z_0$，使 $\|z-z_0\|<\varepsilon$。当 $n$ 大于 $z_0$ 使用的最大次数时，

$$
|\langle y_n,z\rangle|
=|\langle y_n,z-z_0\rangle|
\le\|z-z_0\|<\varepsilon.
$$

因此整个序列 $y_n\rightharpoonup0$，每个固定有界线性泛函都满足 $f(y_n)\to0$。原文对式 (20) 的赋值没有给出线性相容性及连续性的证明，而且所需结论与已证弱收敛矛盾。仅仅逐个 $f_n$ 有界并不足以定义这种 $f$。

这里识别的是一处完整、自包含的局部反驳；没有声称它排除了所有可能的修补或所有不同证明。

## 6. Enflo 稿件：保持来源状态准确

Per H. Enflo, *On the invariant subspace problem in Hilbert spaces*, [arXiv:2305.15442](https://arxiv.org/abs/2305.15442)。首次提交 2023-05-24，本次检索可见最新版本 v2 为 2024-04-06，27 页。

原稿声称肯定解决 Hilbert ISP。本次没有逐行审查该证明，也没有找到可以可靠引用、且精确定位已证实缺口的原始评审材料。因此这里仅记为未确立的完整证明声称；不称其为已证伪或已撤稿。

## 7. 可靠研究入口

### 7.1 2025 年综述与普适算子

Isabelle Chalendar and Jonathan R. Partington, *Recent perspectives on the Invariant Subspace Problem*, [arXiv:2507.21834v1](https://arxiv.org/html/2507.21834v1)，2025-07-29。

- §1 明确仍把 Hilbert ISP 作为开放问题。
- Theorem 2.5：任意小范数、秩至多一的扰动产生不变半空间。
- Theorem 3.1：满射且核无限维的 Hilbert 算子满足 Caradus 普适性准则。
- Theorem 3.4：使用 $W_2$ 的极大不变子空间余维为一给出 ISP 的等价化。

引用 Theorem 3.4 时不直接抄录该综述证明中的 $W_n^*W_n$ 系数：对其定义 $W_nf(z)=(1+\cdots+z^{n-1})f(z^n)$，在单项式正交基上直接计算是 $W_n^*W_n=nI$，不是页面显示的 $(n+1)I$。这个系数笔误不影响满射结论。

### 7.2 小秩小范数扰动的原始来源

Adi Tcaciuc, *Invariant subspace problem for rank-one perturbations: the quantitative version*, [arXiv:2006.11954v2](https://arxiv.org/abs/2006.11954)，2020-06-23；J. Funct. Anal. **283** (2022), no. 5, 109548。

结论是对任意无限维复 Banach 空间上的有界 $T$ 及 $\varepsilon>0$，存在 $\operatorname{rank}F\le1$、$\|F\|<\varepsilon$，使 $T+F$ 有无限维且无限余维的不变子空间。另有 Vladimir Müller, *Invariant half-spaces for rank-one perturbations*, [arXiv:2006.10507](https://arxiv.org/abs/2006.10507)，2020-06-18，给出同类结论。

这些结果已经保证近似不变半空间存在。真正需要的额外步骤是防止子空间随扰动趋零而退化；仅令扰动趋零不自动得到原算子的不变子空间。

### 7.3 Rosenblum/Hankel/矩递推等价化

Junsheng Fang, Bingzhe Hou, Chunlan Jiang, Yuanhang Zhang, *The invariant subspace problem and Rosenblum operators I*, [arXiv:2506.15270v1 HTML](https://arxiv.org/html/2506.15270v1)，arXiv 标头为 2025-06-18，本次所见正文日期为 2026-08-24。由于二者不同，引用具体内容时应同时保留版本链接，不能仅按最初提交日期推断正文版本。

Theorem 4.4 给出：若 $r(A)<1$，则 $A$ 有非平凡闭不变子空间，当且仅当存在非零 $f,g$，使

$$
\sum_{n\ge0}\langle A^nf,g\rangle z^n
$$

是有理函数。

这里有理性推出不变子空间不必再依赖 Hankel 理论。它给出非零多项式 $q$ 和 $N$，满足

$$
\langle A^nA^Nq(A)f,g\rangle=0\qquad(n\ge0).
$$

若 $x=A^Nq(A)f\ne0$，则 $x$ 的闭循环子空间是 $g^\perp$ 中的非零闭不变子空间。若 $x=0$，则非零向量 $f$ 被非零多项式消去，其循环子空间有限维，在无限维 $H$ 中为真。反向从不变子空间 $M$ 取 $0\ne f\in M$、$0\ne g\in M^\perp$，生成函数为零即可。

因此这条路线的核心是构造一对满足最终矩递推的非零向量；不能把等价重述记成已得到这样的一对。

同作者续篇 *The invariant subspace problem and Rosenblum operators II*, [arXiv:2610.11202](https://arxiv.org/abs/2610.11202)，2026-10-08，继续给出 Sobolev 圆盘代数上的约化及特定条件下的结论。本次只核对检索可得的摘要，未将其全文定理作为已检查依赖。

## 8. 下一步

不把超不变结论和撤回等价化拼接；不以不变半空间的弱极限非退化为隐含假设；针对 2026 年模型考察 $S+\lambda V$ 或 $S,V$ 的共同不变子空间时，必须独立分析普通不变性，不能使用全部标量乘子的共同不变性来替代。
