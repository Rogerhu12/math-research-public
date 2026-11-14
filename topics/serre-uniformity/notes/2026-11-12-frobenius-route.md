# Frobenius、虚二次自扭曲与统一性缺口

日期：2026-11-12。会话：serre-uniformity-astra / frobenius。

本笔记不声称解决主问题。下列有限群与迹的论证给出完整证明；明确标注的局部惯性定理、Hasse 界、开像定理等为已证外部输入。自扭曲的解释是已有标准结构，不计为新的文献突破。定量的固定特征 CRT 障碍另登记为 `results/R6-fixed-character-frobenius-obstruction.md`。

## 1. 非分裂 Cartan 的矩阵模型

设 $p$ 为奇素数，固定非平方元 $\delta\in\mathbb F_p^\times$。令
$$
C=\left\{c(a,b)=\begin{pmatrix}a&\delta b\\b&a\end{pmatrix}:(a,b)\ne(0,0)\right\},
\qquad w=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
把 $\mathbb F_{p^2}=\mathbb F_p(\sqrt\delta)$ 按基 $1,\sqrt\delta$ 看作二维空间，则 $C$ 是乘法群 $\mathbb F_{p^2}^\times$。其正规化子为
$$
N=C\sqcup Cw,
$$
其中 $w$ 对应域自同构 $z\mapsto z^p$。证明正规化子恰为此群：一个正规化 $C$ 的线性映射也正规化 $C$ 张成的代数 $\mathbb F_{p^2}$，从而在此代数上诱导一个 $\mathbb F_p$ 自同构；自同构只有恒等与 Frobenius。减去这两个可能后，剩余线性映射与该代数交换，故是其中非零元素的乘法。

直接相乘得
$$
c(a,b)w=\begin{pmatrix}a&-\delta b\\b&-a\end{pmatrix},
\quad \operatorname{tr}(c(a,b)w)=0,
\quad (c(a,b)w)^2=(a^2-\delta b^2)I.
$$
同时
$$
\operatorname{tr}(c(a,b))^2-4\det(c(a,b))=4\delta b^2.
$$
所以 $C$ 中元素的特征多项式判别式只能是零或非平方元；$N\setminus C$ 中元素的迹必为零。反方向不能随意使用：迹为零的元素也可能在 $C$ 中。

## 2. 二次特征一定是虚二次特征

设 $E/\mathbb Q$，且 $\bar\rho_{E,p}(G_{\mathbb Q})\subset N$。定义
$$
\varepsilon:G_{\mathbb Q}\xrightarrow{\bar\rho_{E,p}}N\longrightarrow N/C=\{\pm1\}.
$$
取复共轭 $c$。Weil 配对给出 $\det\bar\rho_{E,p}(c)=-1$，并且 $c^2=1$。如果 $\bar\rho(c)$ 在 $C$ 中，其平方为 $1$ 意味着它在域 $\mathbb F_{p^2}$ 中等于 $1$ 或 $-1$，相应矩阵的行列式都为 $1$，矛盾。因此
$$
\varepsilon(c)=-1.
$$
特别地，$\varepsilon$ 非平凡，其核固定一个虚二次域 $K$。

这一步对所有奇素数成立，不需要非 CM 假设。

## 3. 好素数处的精确迹限制

仍采用 $a_q(E)=q+1-\#E(\mathbb F_q)$。若 $q\ne p$ 为好素数，则
$$
\operatorname{tr}\bar\rho(\operatorname{Frob}_q)\equiv a_q(E)\pmod p,
\qquad \det\bar\rho(\operatorname{Frob}_q)\equiv q\pmod p.
$$
由第 1 节：

- 若 $\varepsilon(q)=-1$，则 $p\mid a_q(E)$。
- 若 $a_q(E)\not\equiv0\pmod p$，则 $\varepsilon(q)=1$，且 $a_q(E)^2-4q$ 模 $p$ 是零或非平方元。

由 Hasse 界 $|a_q(E)|\le2\sqrt q$，若 $q<p^2/4$ 且 $\varepsilon(q)=-1$，便有整数等式
$$
a_q(E)=0.
$$
因而，找到一个好素数
$$
q\ne p,\quad q<p^2/4,\quad\varepsilon(q)=-1,\quad a_q(E)\ne0
$$
足以排除该非分裂 Cartan 像。这里最重要的限制是素数必须同时满足三个条件，不能只找一个小的惰性素数。

## 4. 额外局部推论：$p$ 在 $K$ 中惰性

**已证输入。** 对 $p>13$，如果 $\bar\rho_{E,p}(G_{\mathbb Q})\subset N$，则上述 $\varepsilon$ 在 $p$ 不分歧。这是 Zywina 的 Lemma 2.3(i)，其证明用到椭圆曲线在 $p$ 的惯性像限制。本文不将该局部输入冒充为纯有限群结论。

**推论。** 在上述假设下，
$$
\varepsilon(\operatorname{Frob}_p)=-1;
$$
因此 $p$ 在虚二次域 $K$ 中惰性。

**证明。** 因 $|N|=2(p^2-1)$ 与 $p$ 互素，野惯性在模 $p$ 表示中平凡，惯性像为循环群。$\varepsilon$ 在 $p$ 不分歧，故此循环群在 $C$ 中。另一方面，$\det\bar\rho$ 是模 $p$ cyclotomic 特征，且其在 $I_p$ 上的像等于整个 $\mathbb F_p^\times$。惯性像不能全由标量组成，因为标量矩阵的行列式都是平方。

取惯性像中非标量元素 $t\in C$，以及算术 Frobenius 的一个提升 $F$。温和惯性关系给出
$$
\bar\rho(F)t\bar\rho(F)^{-1}=t^p.
$$
将 $t$ 识别为 $\lambda\in\mathbb F_{p^2}^\times\setminus\mathbb F_p^\times$，则 $t^p\ne t$。若 $\bar\rho(F)\in C$，左侧因 $C$ 交换而等于 $t$，矛盾。所以 $\bar\rho(F)\notin C$，即所需结论。证毕。

本证明还说明了为什么不能把“$\varepsilon$ 在 $p$ 不分歧”替换成“$\bar\rho$ 在 $p$ 不分歧”：后者通常不成立，而且整个推论正是使用了非平凡惯性。

## 5. 残余自扭曲的显式构造

令
$$
J=\begin{pmatrix}0&\delta\\1&0\end{pmatrix}.
$$
则 $J$ 与 $C$ 交换，而 $JwJ^{-1}=-w$。于是对每个 $g\in G_{\mathbb Q}$，
$$
J\bar\rho_{E,p}(g)J^{-1}
=\varepsilon(g)\bar\rho_{E,p}(g).
$$
设 $E^{\varepsilon}$ 是相应二次扭曲，则有 $G_{\mathbb Q}$ 模同构
$$
E[p]\simeq E^{\varepsilon}[p].
$$
这是 Cartan 正规化子的经典自扭曲解释。其源流及素数幂推广可见 Frengley 的 Proposition 3.4；本文在素数层用上述矩阵给出全部证明。

### 非 CM 时不能把这个同构提升为有理同源

设 $E/\mathbb Q$ 无 CM，而 $\varepsilon$ 非平凡。取 $\overline{\mathbb Q}$ 上的扭曲同构 $\phi:E\to E^{\varepsilon}$，使
$$
g(\phi)=\varepsilon(g)\phi.
$$
无 CM 意味着 $\operatorname{End}_{\overline{\mathbb Q}}(E)=\mathbb Z$，从而
$$
\operatorname{Hom}_{\overline{\mathbb Q}}(E,E^{\varepsilon})=\mathbb Z\phi.
$$
若其中非零元素 $n\phi$ 在 $\mathbb Q$ 上定义，取 $\varepsilon(g)=-1$ 的 $g$，则 $n\phi=g(n\phi)=-n\phi$，故 $2n\phi=0$，矛盾。因此
$$
\operatorname{Hom}_{\mathbb Q}(E,E^{\varepsilon})=0.
$$
特别地，二者不在 $\mathbb Q$ 上同源。有限挠点同构并不自动来自椭圆曲线的同源；缺失的恰是某种对 $E$ 和 $\varepsilon$ 统一的模 $p$ 同余刚性。

### 与主问题等价的一种重述

采用已证的 $p>37$ 子群约化，则存在绝对的 Serre 一致性界，当且仅当存在绝对常数 $B$，使非 CM 椭圆曲线在 $p>B$ 时不能与任何非平凡二次扭曲具有同构的 $p$ 挠点 Galois 模。

一个方向由上面的 $J$ 构造得到。反方向所需的有限群事实如下：满射的 $\rho:G_{\mathbb Q}\to\mathrm{GL}_2(\mathbb F_p)$ 不可能有非平凡二次自扭曲。若 $A\rho(g)A^{-1}=\varepsilon(g)\rho(g)$，对 $\rho(g)=I+e_{12}$ 或 $I+e_{21}$ 取迹，可知 $\varepsilon(g)=1$，因为 $p$ 奇且这两个矩阵的迹为 $2$。因此 $A$ 与这两个初等矩阵都交换，只能是标量矩阵。再代入全部 $g$，得到 $\varepsilon=1$，矛盾。

因此，将这里的有限挠点自扭曲“直接提升”只是在另一个语言中重述未解决部分。一般 Frey–Mazur 猜想会给出所需提升，但不能将其作为无条件完成。

## 6. 已核查的分歧支集信息及有限线性筛

Zywina 的 Lemma 2.3 给出下列候选素数集合：
$$
S(E)=\{2:v_2(j(E))\in\{3,6,9\}\}
\cup\{r\ge3:v_r(j(E)-1728)>0\text{ 且为奇数}\}.
$$
$\varepsilon$ 在 $p$ 及 $S(E)$ 以外不分歧。由 Lemma 2.5，可以写成
$$
K=\mathbb Q(\sqrt{-D}),\qquad D>0\text{ 为平方自由整数},\qquad D\mid\prod_{r\in S(E)}r.
$$
还要保留在 $2$ 的实际判别式条件，不能误把 $D$ 的素因子集合与二次域判别式的素因子集合完全等同。

设 $r_1,\ldots,r_s$ 为候选素数，去掉 $p$，并写 $D=\prod r_i^{e_i}$、$e_i\in\mathbb F_2$。对满足 $q\nmid2p\prod r_i$ 且 $0<|a_q(E)|<p$ 的好素数 $q$，第 3 节给出
$$
\sum_i e_i\frac{1-(r_i/q)}2=\frac{1-(-1/q)}2\quad\text{于 }\mathbb F_2.
$$
第 4 节还给出一条 $p$ 处的约束
$$
\sum_i e_i\frac{1-(r_i/p)}2
=1+\frac{1-(-1/p)}2\quad\text{于 }\mathbb F_2.
$$
有限计算可据此排除候选 $p$ 或候选 $K$，但 $S(E)$ 与可用的好素数均依赖 $E$，所以这不是统一界。

## 7. 固定特征的 CRT 障碍与它不说明什么

完整论证见 R6。其核心为
$$
E_X:y^2=x^3-x+4M_X,\qquad
M_X=\prod_{3\le q\le X}q.
$$
这些无 CM 曲线在所有奇素数 $q\le X$ 与 $y^2=x^3-x$ 有相同良好约化，故固定二次特征 $\chi_{-4}$ 的惰性素数在此窗口内全给零迹。与此同时，
$$
h(j(E_X))=2X+o(X),\qquad v_2(j(E_X))=6.
$$
这证明“无 CM + 固定虚二次域”不足以给绝对的有限 Frobenius 窗口，也不足以给次线性于 $h(j)$ 的统一窗口。

这里不能省略的限定是：R6 没有证明 $\chi_{-4}$ 是某个实际异常模 $p$ 表示的商特征。本族通常不满足某一指定 $p$ 所要求的所有 Tate 赋值条件。故 R6 不是对“实际异常子族存在更强素数界”这一可能路线的否定。

## 8. Chebotarev 到底还差什么

R6 第 4 节证明：对每个固定无 CM $E$ 和非平凡二次特征 $\chi$，存在好素数 $q$，满足 $\chi(q)=-1$、$a_q(E)\ne0$。该证明经有限扩张 $\mathbb Q(E[\ell])K$ 使用 Chebotarev；其中辅助素数 $\ell$ 已依赖 $E$，扩张的判别式还依赖 $E,K$。

因此，定性存在性不能推出 $q<p^2/4$。即使获得有效界，也必须逐项控制域判别式、辅助素数和导子的依赖，不能只把它们写进一个看似绝对的常数。即使 $K=\mathbb Q(i)$ 固定，R6 已说明曲线因子仍无法删除。

实际异常子族的可推进问题应准确写成：

> 设 $p>37$，$E/\mathbb Q$ 无 CM，实际模 $p$ 像是 $N_{\rm ns}(p)$，商特征为 $\varepsilon$。利用全部异常像条件，证明存在好素数 $q\ne p$，使 $q<p^2/4$、$\varepsilon(q)=-1$ 且 $a_q(E)\ne0$。

该断言若被证明，将排除剩余像。它在本笔记中尚未得到证明。特别地，单独的 $h(j)\ge p\log(2p-1)$ 下界方向不能给所需的小素数上界。

## 9. 文献及核查定位

- D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, [作者 PDF](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)：Lemma 2.3（分歧）、Lemma 2.5（虚二次特征表达）、Lemma 2.6（迹条件）；§5 将二次扭曲比较与依赖导子的 Sturm 界连接。这里只把这些作为已证标准输入，没有声称其常数独立于曲线。
- S. Frengley, *Congruences of elliptic curves arising from non-surjective mod $N$ Galois representations*, arXiv:2111.05813v2 (2022)，[原文](https://arxiv.org/pdf/2111.05813)：Proposition 3.4（Cartan 正规化子与二次扭曲同余），Lemma 4.1（与非平凡二次扭曲有理同源的 CM 条件）。本笔记第 5 节在所需范围独立展开证明。
- P. Habegger, *Singular moduli that are algebraic units*, Algebra & Number Theory **9** (2015), 1515–1524，[原文](https://msp.org/ant/2015/9-7/ant-v9-n7-p01-s.pdf)：引言明确记录 CM $j$ 整性的标准事实。
- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. **15** (1972), 259–331：逐曲线开像定理。
