# R8：假想坏像曲线的有理同源孤立性与 Hecke 邻居的次数

**状态：已证明。** 这是 Lemos 的已有统一性定理及 R1 的像分类的推论，不声称文献创新，不算 Serre 一致性主问题完成。

日期：2026-11-12。会话：serre-uniformity-astra。

## 1. 结论

1. 设无 CM 的 $E/\mathbb Q$ 对某个 $p>37$ 的模 $p$ 表示不满射。则对任意非平凡有限循环子群 $C\subset E(\overline{\mathbb Q})$，都有 $j(E/C)\notin\mathbb Q$。若 $E'/\mathbb Q$ 与 $E$ 几何同源，则 $j(E')=j(E)$。
2. 对任意无 CM 的 $E/\mathbb Q$、任意素数 $\ell>37$、任意阶为 $\ell$ 的子群 $C\subset E[\ell]$，都有精确等式
   $$[\mathbb Q(j(E/C)):\mathbb Q]=\ell+1.$$
   这里无需假设 $E$ 是假想坏像曲线。
3. 特别地，若 $P\in X_{\rm ns}^+(p)(\mathbb Q)$ 是非 CM 点且 $p>37$，则素数 Hecke 对应 $T_\ell$（$\ell>37$, $\ell\ne p$）的 $\ell+1$ 个几何邻居形成一个 Galois 轨道，每个邻居的次数恰为 $\ell+1$。因此 $T_\ell(P)$ 是一个有理有效除子，但并不提供新的有理曲线点。

第 1 条依赖 Lemos Theorem 1.1；第 2 条依赖 R1 中 $\ell>37$ 时像为 $\mathrm{GL}_2(\mathbb F_\ell)$ 或完整 $N_{\rm ns}(\ell)$ 的分类。下面完整证明所有附加的同源、核、次数与对应步骤。

## 2. 同源模的秩一性质

### 引理 8.1

设 $E,E'/\overline{\mathbb Q}$ 几何同源且 $\operatorname{End}(E)=\mathbb Z$。则 $\operatorname{Hom}(E,E')$ 为秩一的自由 $\mathbb Z$-模。若 $\varphi_1,\varphi_2:E\to E'$ 是同度数同源，则 $\varphi_1=\pm\varphi_2$，因而两者的核相同。

**证明。** 固定一个非零同源 $\eta:E\to E'$，并记其对偶为 $\widehat\eta$。映射
$$\operatorname{Hom}(E,E')\longrightarrow\operatorname{End}(E)=\mathbb Z,
\qquad \varphi\longmapsto\widehat\eta\circ\varphi$$
是单射：若复合为零，则 $\varphi(E)$ 包含在有限群 $\ker\widehat\eta$ 中；由于 $E$ 连通，$\varphi$ 必为零。该像非零，因为 $\widehat\eta\circ\eta=[\deg\eta]$。于是 Hom 模同构于 $\mathbb Z$ 的一个非零子群。

取其生成元 $\psi$。若 $\varphi_i=[m_i]\circ\psi$，则
$$\deg\varphi_i=m_i^2\deg\psi.$$
同度数给出 $m_1=\pm m_2$，从而结论成立。证毕。

### 引理 8.2（不同同阶核给出不同的商 $j$）

设 $E/\overline{\mathbb Q}$ 无 CM，$C_1,C_2\subset E$ 是同阶的有限子群。若 $j(E/C_1)=j(E/C_2)$，则 $C_1=C_2$。

**证明。** 选择同构 $\alpha:E/C_1\simeq E/C_2$，将两个商同源都视作目标为 $E/C_2$ 的同源。它们同度数；由引理 8.1，仅相差一个符号，故核相同。证毕。

因此固定阶 $n$ 后，映射
$$C\longmapsto j(E/C)$$
在有限子群集合上是单射。如果 $E/\mathbb Q$，它还是 $G_{\mathbb Q}$-等变的。

## 3. 核的定义域等于商 $j$ 的定义域

对 $E/\mathbb Q$ 和有限子群 $C\subset E(\overline{\mathbb Q})$，令 $\mathbb Q(C)$ 表示使该子群整体有定义的最小数域，即其集合稳定子的固定域。它不是要求每个 $C$ 中的点逐一有定义的域。

### 引理 8.3

若 $E/\mathbb Q$ 无 CM，则
$$\mathbb Q(C)=\mathbb Q(j(E/C)).\tag{3.1}$$
特别地，若商的 $j$ 值有理，则 $C$ 是 $G_{\mathbb Q}$-稳定的。

**证明。** 对任意 $\sigma\in G_{\mathbb Q}$，商构造与基变换相容，给出
$$\sigma(j(E/C))=j(E/\sigma C).$$
若 $\sigma C=C$，右侧当然不变。反过来，若 $\sigma(j(E/C))=j(E/C)$，则 $C$ 与 $\sigma C$ 同阶且商 $j$ 相同，引理 8.2 给出 $\sigma C=C$。两个代数对象的 Galois 稳定子相等，固定域遂相等。证毕。

若 $C$ 为 $G_{\mathbb Q}$-稳定的有限子群，则它下降为 $E$ 上的有限 étale 子群概形，商椭圆曲线及商同源都在 $\mathbb Q$ 上有定义。这是特征零椭圆曲线的标准商构造；它也说明 (3.1) 没有把有理模点误当成未经下降的同源。

## 4. 由 Lemos 得到有理同源孤立性

采用以下既有定理。

**Lemos Theorem 1.1。** 若无 CM 的 $E/\mathbb Q$ 存在非平凡循环 $\mathbb Q$-同源，则对每个素数 $p>37$，$\bar\rho_{E,p}$ 满射。

### 定理 8.4

设无 CM 的 $E/\mathbb Q$ 对某个 $p>37$ 有非满模 $p$ 像。则任何非平凡有限循环子群 $C$ 都满足 $j(E/C)\notin\mathbb Q$。

**证明。** 若 $j(E/C)$ 有理，引理 8.3 说明 $C$ 为 $G_{\mathbb Q}$-稳定的，故给出非平凡循环 $\mathbb Q$-同源，与 Lemos 定理矛盾。

也可以只使用素数次数的情形：若 $\#C=n>1$，取素数 $r\mid n$。循环群 $C$ 的唯一阶 $r$ 子群是特征子群，所以同样 Galois 稳定，给出循环 $r$ 次 $\mathbb Q$-同源，仍由 Lemos 定理矛盾。这里不存在“次数无界所以不能应用”的问题。证毕。

### 推论 8.5

在定理 8.4 的假设下，若 $E'/\mathbb Q$ 与 $E$ 在 $\overline{\mathbb Q}$ 上同源，则它们几何同构。因此其有理几何同源类只有一个 $j$ 值；不同 $\mathbb Q$-同构类可以是该曲线的二次扭曲。

**证明。** 取引理 8.1 中 Hom 模的生成元 $\psi:E\to E'$。其核必须循环。否则，有限椭圆曲线子群的两个不变因子有公因子，从而存在素数 $r$ 使
$$E[r]\subseteq\ker\psi.$$
于是 $\psi$ 通过商映射 $[r]:E\to E$ 分解，即 $\psi=\theta\circ[r]=r\theta$，与其为 Hom 模的生成元矛盾。

若 $\deg\psi>1$，这个非平凡循环核的商有理 $j$ 值为 $j(E')$，违反定理 8.4。因此 $\deg\psi=1$，两曲线几何同构。无 CM 保证 $j(E)\ne0,1728$，所以同一 $j$ 值的 $\mathbb Q$-模型之间只涉及二次扭曲。证毕。

## 5. 大素数 Hecke 邻居的精确定义域次数

### 定理 8.6

对任意无 CM 的 $E/\mathbb Q$、素数 $\ell>37$ 以及阶 $\ell$ 子群 $C\subset E[\ell]$，
$$[\mathbb Q(C):\mathbb Q]
=[\mathbb Q(j(E/C)):\mathbb Q]=\ell+1.$$

**证明。** R1 的像分类给出
$$\operatorname{im}\bar\rho_{E,\ell}
\cong\mathrm{GL}_2(\mathbb F_\ell)
\quad\text{或}\quad N_{\rm ns}(\ell).$$
两种群都在 $\mathbb P^1(\mathbb F_\ell)$ 上传递。对 $\mathrm{GL}_2$ 这直接来自基变换；对 $N_{\rm ns}$，其 Cartan 子群 $\mathbb F_{\ell^2}^{\times}$ 已在非零向量上传递，故在一维 $\mathbb F_\ell$-子空间上也传递。这样的子空间恰有 $\ell+1$ 个，它们正是阶 $\ell$ 子群。

因此 $C$ 的 Galois 轨道大小为 $\ell+1$，即 $[\mathbb Q(C):\mathbb Q]=\ell+1$。另一等式由引理 8.3。证毕。

### 推论 8.7（在 $X_{\rm ns}^+(p)$ 上的解释）

设 $p>37$，$P\in X_{\rm ns}^+(p)(\mathbb Q)$ 非 CM，并取素数 $\ell>37$、$\ell\ne p$。则 $T_\ell(P)$ 的 $\ell+1$ 个几何邻居互不相同，构成一个 Galois 轨道，而且每个点的剩余域次数恰为 $\ell+1$。

**证明。** 取代表 $P$ 的 $E/\mathbb Q$ 及其有理非分裂正规化子级结构。每个阶 $\ell$ 子群 $C$ 在 $K=\mathbb Q(C)$ 上有定义，商同源在 $K$ 上有定义；由于 $\ell\ne p$，它诱导 $E[p]\simeq(E/C)[p]$，把原来的级结构输送到商曲线上，给出一个 $K$-点 $P_C$。

引理 8.2 保证不同 $C$ 对应不同 $j$ 值，因而邻居彼此不同。这个构造 Galois 等变，且定理 8.6 说明全部 $C$ 形成一个大小 $\ell+1$ 的轨道。最后
$$\mathbb Q(j(P_C))\subseteq\mathbb Q(P_C)\subseteq K,$$
两端都因定理 8.6 有次数 $\ell+1$，所以中间也相等。证毕。

## 6. 此结论排除什么、不排除什么

它排除了以下点数论证：从一个假想非 CM 有理点出发，反复应用循环 Hecke 对应得到越来越多有理曲线点，再超过 QC 的有理点上界。实际上，邻居首先离开了有理数域，而且大素数邻居的次数已经精确为 $\ell+1$。

它不排除 Hecke 方法。$T_\ell(P)$ 整体仍是 $\mathbb Q$-有理有效除子；Hecke 算子也仍作用在 $J(\mathbb Q)$ 上。利用这些算子构造 QC 函数、循环或高度关系，仍是完全有效的研究方向。

## 7. 来源

- P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. Amer. Math. Soc. 371 (2019), Theorem 1.1，DOI 10.1090/tran/7198：<https://arxiv.org/pdf/1702.01985>。
- L. Furio and D. Lombardo, *Serre's uniformity question and proper subgroups of $C_{\rm ns}^+(p)$*，相关已核查分类及准确版本见本课题 `R1-exact-remaining-image.md`：<https://arxiv.org/abs/2305.17780>。
