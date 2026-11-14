# 文献现状与定理适用范围核查

日期：2026-11-12（UTC+8）。子任务：literature_scope。

**状态：文献核查与路线分析。主目标尚未得到证明。** 本文把“原文已核对的定理范围”与“本会话给出的新证明”分开；没有把新近预印本的声称自动视为可调用定理。

## 1. 本题精确地是已有公开问题

William Stein，*The Birch and Swinnerton-Dyer Conjecture: A Computational Approach*，在线稿 2007-05-25，Problem 2.16：固定一个 $E/\mathbb Q$，要求其秩至少为 2，且无穷多个素数的 Sha-primary 群有限。原始页面：

<https://www.wstein.org/books/bsd/bsd/node24.html>

因此问题没有被“无穷多对 $(E,p)$”的定理自动解决。该页 Theorem 2.14 的 Gross–Zagier–Kolyvagin 假设是**解析秩**至多 1；不能将其替换成仅有 Mordell–Weil 秩至多 1。

另一个逻辑区分：所有 $p$ 的 primary 群分别有限，不自动推出整个扭群有限，还需证明只有有限多个非零 primary 群。主代理另行给出结构证明并修订课题背景；这不更改主目标。

## 2. 非 CM 曲线的单素数计算已经很强，但仍是单素数

William Stein、Christian Wuthrich，*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*，Math. Comp. **82** (2013)，1757–1792，DOI `10.1090/S0025-5718-2012-02649-4`。核对的是作者保存的出版版：

<https://wstein.org/papers/mcom2649-iwasawa-alg.pdf>

关键定位：

| 位置 | 已核对内容 | 与本题的差距 |
|---|---|---|
| Theorem 1.1，p.1758 | 非 CM、导子至多 30000、秩至少 2、好普通 $5\le p<1000$、模 $p$ 满像的 1534422 对满足 $\Sha[p]=0$ | $p$ 有统一有限上界 |
| Theorem 12.3，p.1788 | 曲线 389a 的大批好普通 $p<48859$ 满足 $\Sha[p]=0$，列出未算出的 $p=16231$ | 仍为有限多个 $p$ |
| Theorem 6.1，p.1776 | $\operatorname{ord}_T f_{E,p}\ge r$；等号等价于 $p$-进高度非退化且 $\Sha[p^\infty]$ 有限 | 两条件不能互相省去 |
| Theorems 7.3–7.4，p.1778 | Kato 的整除给 $f_{E,p}\mid p^mL_p(E,T)$，满像时可取 $m=0$ | 未给秩二系数对无穷多 $p$ 的非零性 |

Algorithm 11.1 的终止或成功输出不是无条件的全称结论；成功时输出的界有证明，尚未证明每个所需输入都成功。不可把“逐一验证可行”换成“有无穷多个成功的输入”。

### 一个直接可用的路线约化

对于固定非 CM $E$，设已证 $r\ge2$。在上述好普通、Kato 整除及下降定理适用的 $p$，若
$$
[T^2]L_p(E,T)\ne0,
$$
则 $r=2$ 且 $\Sha(E/\mathbb Q)[p^\infty]$ 有限。证明是：Kato 整除与下降给
$$
2\le r\le\operatorname{ord}_Tf_{E,p}
\le\operatorname{ord}_TL_p(E,T)\le2.
$$
于是等号成立，调用 Theorem 6.1 的等号判别即可。这里**不需预先假设高度非退化**；它由等号一并推出。

剩下的真正未知点是：给固定曲线证明上述二阶系数对无穷多个 $p$ 非零。把它写成假设不算完成。要求系数是单位更强，可用于获得 Sha 消失；仅有限性目标只需非零。

## 3. 主猜想没有替代秩二非消失问题

Kazuya Kato，*p-adic Hodge theory and values of zeta functions of modular forms*，Astérisque **295** (2004)，117–290，尤其 Theorem 17.4。官方目录与出版信息：

<https://www.numdam.org/item/AST_2004__295__117_0/>

本文核对其出版元数据和上节出版论文对 Theorem 17.4 的精确应用；没有声称在本会话重证 Kato 全文。Euler 系统给向主猜想的一向整除及 Selmer 上界；对 $L(E,1)=0$ 的秩二情形，需进一步的消失阶信息。

Christopher Skinner、Eric Urban，*The Iwasawa Main Conjectures for $\mathrm{GL}_2$*，Invent. Math. **195** (2014)，1–277。作者稿：

<https://www.math.columbia.edu/~urban/eurp/MC.pdf>

Theorem 1 / Theorem 3.6.4：在普通性、模 $p$ 不可约、存在 $q\Vert N$ 且模 $p$ 表示在 $q$ 分歧等假设下，特征理想与 $p$-进 $L$ 函数生成理想在反转 $p$ 后相等；加大像条件得到整系数等式。其 Theorem 2 / 3.6.11 的 BSD 数值应用明确含 $L(E,1)\ne0$。

对本题而言，即使得到
$$
(f_{E,p})=(L_p(E,T)),
$$
仍须确定其在 $T=0$ 的阶数，不能把理想相等本身读作 $\operatorname{ord}_T L_p=r$。

Peter Schneider，*p-adic height pairings. II*，Invent. Math. **79** (1985)，329–374。作者目录：

<https://ivv5hpp.uni-muenster.de/u/pschnei/publ/pap/>

对本课题所需的精确等号判别，采用已核对的 Stein–Wuthrich Theorem 6.1 陈述（合并 Schneider、Perrin-Riou、Jones 的贡献），不把“高度非退化”单独当成 Sha 有限的无条件证明。

## 4. CM 方向已知的跨素数界没有强到有限性

John Coates、Zhibin Liang、R. Sujatha，*The Tate-Shafarevich group for elliptic curves with complex multiplication II*，Milan J. Math. **78** (2010)，395–416。原稿：

<https://arxiv.org/pdf/1005.4206>

Theorem 1.1 令 $t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]$，证明对任意 $\epsilon>0$ 及充分大的好普通素数有
$$
t_p\le(1/2+\epsilon)p-r.
$$
这是跨 $p$ 的无条件定理，但其右端随 $p$ 增大，不能迫使 $t_p=0$。Theorems 1.2–1.3 则对具体 CM 秩 3、秩 2 曲线给出 $p<30000$ 的计算结果，不提供无限性。

前篇：Coates–Liang–Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication*，J. Algebra **322** (2009)，657–674，DOI `10.1016/j.jalgebra.2009.04.039`；其原始版本 arXiv:0901.3832。其高权 Hecke 值判据由本课题另一子任务详细核对。

## 5. 广义 Kato 类的秩二结果：非零性不能由已知秩直接取代

Francesc Castella、Ming-Lun Hsieh，*On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*，Forum Math. Sigma **10** (2022)，e12：

<https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864>

核对 Theorem A、式 (1.9)–(1.10)：在辅助二次域、伴随扭曲非零、模 $p$ 不可约与分歧等明确条件下，广义 Kato 类非零推出 $\mathbb Q_p$-Selmer 维数为 2；反向从 Selmer 维数为 2 并结合非零局部化推出类非零。不能将其中的 Selmer 维数条件换成 $\operatorname{rank}E(\mathbb Q)=2$。

Castella 后续文章 *Nonvanishing of generalised Kato classes and Iwasawa main conjectures*，Springer Proceedings in Math. & Stat. **527** (2026)，23–50，作者稿：

<https://web.math.ucsb.edu/~castella/GKC-IMC.pdf>

Theorem A 对好普通 $p>3$、绝对不可约残余表示、有适当乘法约化素数等条件给相同方向的结论，并识别其张成的局部化核。这放宽适用假设，未证明固定秩二曲线在无穷多个 $p$ 上的类非零。

### CM 版本须用最新版本

Francesc Castella，*Generalised Kato classes on CM elliptic curves of rank 2*，作者主页标 American J. Math. 待刊，作者稿日期 2026-02-13：

<https://web.math.ucsb.edu/~castella/Kato-Schoen.pdf>

Theorem B 在 $p\ge5$ 分裂、$L(E,s)$ 中心有正偶数阶零及适当辅助 Hecke 特征选择下给
$$
\kappa_p\ne0\Longrightarrow
\dim_{\mathbb Q_p}\operatorname{Sel}(\mathbb Q,V_pE)=2.
$$
其反向也先假设 Selmer 维数为 2。Theorem C 的显式基构造另假设 $\Sha[p^\infty]$ 有限及两个 $p$-进零点阶条件，故不能用该基反向“证明”同一个有限性假设。

旧作者稿 `Kato-cm.pdf` 为 2022-06-17 版本，主定理编号与新版不同；本任务以新版为准。对于已经知道 $r=2$ 的曲线，Kummer 嵌入只给 Selmer 维数 $\ge2$，没有提供上界。

## 6. 2026 年新稿：记录范围，不未经核查采用

### 6.1 Banwait，2026-09-08

Barinder S. Banwait，*Second derivatives of $p$-adic $L$-functions and the Shafarevich–Tate group of rank-two CM elliptic curves*，arXiv:2609.08431v1：

<https://arxiv.org/abs/2609.08431>；<https://arxiv.org/pdf/2609.08431>。

官方网页在检索工具中返回不可访问，但终端从官方 PDF URL 下载成功，已提取文本核对 §§1、3、13–16 的相关陈述。作者主页将其列为 submitted；本会话未逐行验证其全部证明，也没有将其结果用于主结论。

Theorems A/B 是 CM 曲线的逐素数判据：正规化二阶系数为单位，与相应正规化调节子为单位且 Sha-primary 消失相联系；后者又与高权 Hecke 值组合的赋值条件相联系。§1.1–1.2 明说没有证明任何秩二曲线的整体 Sha 有限，也没有给无穷多素数定理。该稿的数值样本约 8050 个素数检查不提供无限性证明。

其问题部分询问是否有固定代数对象控制所有坏素数，尚没有构造该对象。其开头把“秩至多1”写得过宽；本任务使用解析秩/低 Selmer 余秩的精确版本。

### 6.2 Chan-Ho Kim，2026-10 修订

Chan-Ho Kim，*On the arithmetic of Tate-Shafarevich groups via Kolyvagin's conjecture*，arXiv:2609.15328v2（2026-10-24 修订，稿内日期 2026-10-27）：

<https://arxiv.org/abs/2609.15328>；<https://arxiv.org/pdf/2609.15328>。

同样由终端从官方地址取得文本；核对 Introduction、Theorem 1.1、Corollary 1.6、§4.2–4.3。尚未逐行核查全篇，故不未经证明用作本课题输入。

Theorem 1.1 的形式是**有限性与导出 Heegner 点的精确群归属等价**。在其非 CM、大像及好约化条件下，选定 $k,\partial,n$，要求形如
$$
P_n\in p^\partial\bigl(E(\mathbb Q)+p^kE(K[n])\bigr).
$$
Corollary 1.6 对半稳定曲线的好素数 $p\ge5$、残余不可约情形给 Selmer 的结构和生成描述；它没有去掉上述点归属问题。Question 4.6 明确保留寻找迫使归属成立之原理的问题。Theorem 4.7 的有限域判据还依赖相关 Mordell–Weil 子群的约化，而非仅仅完整有限域点群；不能把“局部可解”直接换成所需全局子群归属。

### 6.3 OpenAI 的低余秩预印本

课题 README 所列结果族的输入为某个 $q^\infty$-Selmer 余秩属于 $\{0,1\}$。本任务只用 Kummer 正合列就能断定 $r\ge2$ 曲线不满足此输入。因此无论这些新稿最终审查如何，该输入范围本身不涵盖本课题；无需为此先调用未经验证的新稿。

### 6.4 Calonge Fabregat，2026-11-06

Miquel Calonge Fabregat，*Elliptic units, derived Heegner classes and the p-adic Birch and Swinnerton-Dyer quotient of CM elliptic curves of rank two*，arXiv:2611.09192v1：

<https://arxiv.org/abs/2611.09192>；<https://arxiv.org/pdf/2611.09192>。

已核对 Introduction、Hypotheses 5.1、Lemma 5.2。其跨素数比较 $q_p=q_\infty\in\mathbb Q$ 明确仍是猜想。Theorems A/B 预先假设 $\Sha(E/\mathbb Q(i))[p^\infty]$ 有限及 $\det H\ne0$。Theorem C 使用的 (H5) 更直接是 $c_2(p)\ne0$；Lemma 5.2(2) 正是从这个输入推出有限性。Theorem D 另需相关导出 Heegner 向量的正式对数非零。因此其精确比较公式没有提供本题所缺的跨 $p$ 非消失。只作范围核查，未采用该新稿的未独立验证证明。

## 7. 一篇看似直接解决本题的声称已被具体反驳

Destrempes–Malinin，arXiv:1703.02215v2，声称几乎所有素数的 primary 群消失。核查发现其统一有界坐标抬升引理不成立，完整反证见：

- `results/R5-uniform-lifting-obstruction.md`：固定有限代数点集不能覆盖所有素数处任意大的 $\ell$-幂扭点；Chebotarev 与点数比较给出矛盾。
- `notes/2026-11-12-destrempes-malinin-audit.md`：另定位横坐标差与群差混淆，以及单个素理想上的同余被不合法地带入全局迹。

这些反证只否定该稿的证明路线，不否定 BSD 或其最终消失猜想。

## 8. 当前可明确列出的未闭合步骤

1. 固定一个秩二非 CM 曲线，证明 $[T^2]L_p(E,T)\ne0$ 对无穷多个合适的 $p$ 成立；已有主猜想与逐素数精确计算没有给出这个横向非消失结论。
2. 对 CM 曲线，把随 $p$ 改变的高权 Hecke 值赋值界改进到等于秩；目前所核对的统一界为 $O(p)$，不足以迫使余秩为零。
3. 在广义 Kato 类路线中，证明固定曲线的 $\kappa_p$ 对无穷多个 $p$ 非零；不能把二维 Selmer 条件先当作已知。
4. 在导出 Heegner 点路线中，证明点位于指定全局子群；不能用所有局部点组成的较大群代替全局子群的约化。

截至本次核查，没有找到能直接引用、满足本题完整量词且已有可核实证明的定理。这是本次检索与核查结论，不是对所有未见文献的穷尽断言。
