# 变化二次商域：associated characters 的文献接口与 R58

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态。** 精确核验 Momose 与 Larson–Vaintrob 的适用对象、量词及 GRH 依赖。本文第 3 节是已发表定理在实际完整非分裂正规化子像上的推论，不另编号。新证明的环类群分裂、小分裂素数理想阶与显式判别式增长界已完整收入 [R58](../results/R58-ring-class-splitting-and-small-split-primes.md)。它们仍没有同时控制变化的商域与指数。

## 1. 本课题的对象与两个不同的“可约”

设 $E/\mathbb Q$ 无 CM，$p>37$，且模 $p$ 像为完整 $N_{\rm ns}(p)$。令 $K$ 为正规化子到 $N/C$ 的二次商域。由 R5，$K$ 虚二次而 $p$ 惰性。限制到 $G_K$ 后：
$$
\operatorname{Im}\bar\rho_{E,p}|_{G_K}=C\simeq\mathbb F_{p^2}^{\times}.
$$
这个二维表示在 $\mathbb F_p$ 上不可约；扩张系数域到 $\mathbb F_{p^2}$ 后才分解为 $\lambda\oplus\lambda^p$。两者不可混用：

- $K$ 上有理的 $p$ 同源，要求一条 $\mathbb F_p$ 直线被 $G_K$ 保持。
- 一维 associated character 允许先将系数扩张到 $\overline{\mathbb F}_p$。

在本题前者不存在，后者确实存在。二次基变换把正规化子像降到 Cartan，并未把非分裂 Cartan 变成 $\mathbb F_p$ 上的对角群。

## 2. 原始文献的精确接口

### 2.1 Momose：要求实际的有理同源

F. Momose, *Isogenies of prime degree over number fields*, Compositio Math. **97** (1995), 329–348，[已发表原文](https://www.numdam.org/item/CM_1995__97_3_329_0.pdf)。

Theorem A 的对象为 $X_0(p)(k)$ 的非尖点，角色是 $\mathbb F_p^\times$ 值同源特征；大于一个依赖固定 $k$ 的有效常数后，得到三型分类。Theorem B 对非虚二次类数一的二次 $k$ 给出有限性，至多留下一个有关 Siegel 零点的无效例外。Lemma 1 的主理想同余是后续同源特征方法的类域论入口。

**本题不能直接代入 Theorem A/B。** $E_K[p]$ 的完整非分裂 Cartan 像没有稳定的 $\mathbb F_p$ 直线；$\lambda$ 取值于 $\mathbb F_{p^2}^\times$。Lemma 1 背后的 idèle 互反论证可以在重新证明局部权后使用，但不能据此把它的 $\mathbb F_p$ 同源分类也搬过来。

若改为基变换到项目除法域 $M/K$，残余像降为标量，确实有有理 $p$ 同源；但
$$
[M:K]=p+1,\qquad [M:\mathbb Q]=2(p+1).
$$
这没有给固定次数的同源问题。把 $M$ 记成“某个数域”会隐藏一个正随待排除素数增长的参数。

### 2.2 Larson–Vaintrob：允许扩系数的一维特征

E. Larson and D. Vaintrob, *Determinants of subquotients of Galois representations associated with abelian varieties*, J. Inst. Math. Jussieu **13** (2014), 517–559，[作者预印本 v4](https://arxiv.org/pdf/1110.0255)，[已发表 DOI](https://doi.org/10.1017/S1474748013000182)。以下编号在作者原文直接核验。

Theorem 1 = Theorem 6.4：固定数域 $k$ 后，存在仅依赖 $k$ 的有效有限素数集合 $S_k$。对 $\ell\notin S_k$，若 $E[\ell]\otimes\overline{\mathbb F}_\ell$ 可约，取其一维特征 $\psi$，则有两种可能：

1. 存在定义在 $k$、CM 域包含于 $k$ 的 CM 椭圆曲线 $E'$，使相应特征满足 $\psi^{12}=(\bar\psi')^{12}$。
2. $k(\sqrt{-\ell})$ 的 GRH 失败，$\psi^{12}=\chi_\ell^6$；并且 $\ell\equiv3\pmod4$、原表示已经在 $\mathbb F_\ell$ 上可约。

有限集合的有效性见 Remark 1.1 与 §7。**Theorem 7.9 展示的较小显式界以 GRH 为假设**；不能原样称为无条件。Remark 7.8 指明可换无条件 Chebotarev，Remark 7.10 给不依赖 GRH 的 $B_{\rm char}(k,g)B_{\rm rat}(k,g)$ 界；这些量仍依赖 $k$。

### 2.3 近期算法化结果也没有改变表示的系数域条件

B. S. Banwait and M. Derickx, *Explicit isogenies of prime degree over number fields*, Algebra Number Theory **19** (2025), 1147–1197，[作者版本和期刊资料](https://arxiv.org/abs/2203.06009)，[DOI](https://doi.org/10.2140/ant.2025.19.1147)。该文把 Momose 分类显式化并实现算法；一般算法依赖 GRH，半稳定子范围无条件。其输入仍是数域上的有理 $p$ 同源，故不是本题 $E_K[p]$ 的直接算法。

此处只使用作者摘要核验算法范围，没有声称已逐行核验其全部实现或把其定理用于 R58。

## 3. Larson–Vaintrob 对本题实际给出的无条件推论

**推论。** 固定任意虚二次域 $K$，若 $h_K>1$，则所有以 $K$ 为商域的实际完整非分裂正规化子异常素数都落在一个有效有限集合 $S_K$ 中。本结论不要求 GRH，也不限于 $p\equiv1\pmod{12}$。

**证明。** 令 $p\notin S_K$。$E_K[p]$ 扩系数后的一维特征 $\lambda$ 符合 Theorem 6.4 的对象。第二分支要求原表示在 $\mathbb F_p$ 上可约，而完整 $C$ 在 $\mathbb F_p$ 上不可约，立即矛盾。

也可用 R21 的惯性型独立排除第二分支：
$$
\lambda^{12}|_{I_p}=\omega_2^{12}
\quad\hbox{或}\quad\omega_2^{12p},
\qquad
\chi_p^6|_{I_p}=\omega_2^{6(p+1)}.
$$
相等要求 $p+1\mid6$，与 $p>37$ 不相容。这一路同样没有以 GRH 为前提。

故第一分支成立，存在 $E'/K$，其 CM 域包含于 $K$。由于 $K$ 本身二次虚域，这个 CM 域就是 $K$。设 $\mathcal O\subseteq\mathcal O_K$ 为 $E'$ 的 CM 序。复乘主定理给
$$
K(j(E'))=H_{\mathcal O},\qquad
[H_{\mathcal O}:K]=h(\mathcal O).
$$
但 $E'$ 定义在 $K$，所以 $j(E')\in K$，从而 $h(\mathcal O)=1$。序类群到 $\operatorname{Cl}(K)$ 的标准满射强迫 $h_K=1$，矛盾。证毕。

这个推论的准确量词是
$$
\boxed{\forall K\text{，若 }h_K>1,
\quad\exists\text{有效有限 }S_K,
\quad\forall E\text{ 及对应异常 }p,
\quad p\in S_K.}
$$
它没有把 $\forall K\,\exists S_K$ 换成一个不依赖 $K$ 的有限集合。即使 $[K:\mathbb Q]=2$ 固定，类数、判别式和检测素理想仍可增长。

复乘主定理的环类域表述亦见 Momose 原文 §1 对序及其环类域的设定；此处已展开导致 $h_K=1$ 的全部逻辑，不把“存在 CM 参考特征”直接等同于“原曲线有 CM”。

## 4. 本轮 R58 的内容及其与文献接口的差别

[R58](../results/R58-ring-class-splitting-and-small-split-primes.md) 专门使用 $p\equiv1\pmod{12}$，把残余特征从十二次幂降到
$$
\mu=\lambda^2,
\qquad
\nu=\mu/\chi_p=\lambda^{1-p}.
$$
其证明不调用未求值的 $S_K$，而对当前实际 $(E,p,K)$ 给出三个直接可检验的必要条件：

1. $\mu$ 在所有 $p$ 外素数不分歧；$\nu$ 在 $p$ 的惯性像为完整的阶 $p+1$ 循环群。这包括 $2,3$，并不是把温和惯性结论外推到野惯性。
2. 模 $p$ 序类群正合列的核上，$\nu$ 是同构，因此
   $$
   \operatorname{Pic}(\mathbb Z+p\mathcal O_K)
   \simeq C_{p+1}\times\operatorname{Cl}(K),\qquad H_p=HM.
   $$
3. 对任意非主分裂素理想 $\mathfrak q\mid q$，若 $[\mathfrak q]$ 的阶为 $r$，实际局部二次好约化扭曲的整数迹强迫
   $$
   p<4q^{r/2}.
   $$

第 3 条利用了 $\beta^{2r}\equiv\alpha^2$ 后两支平方根具有同一符号；若整数迹差为零，便迫使局部 Frobenius 的特征零二次域恰为 $K$，进而 $\mathfrak q$ 主，矛盾。这与直接把残余特征提升成一个 CM 特征零特征不同。

不使用有效 Chebotarev，R58 还给出
$$
h_K>1\Longrightarrow
p<4\bigl(2|D_K|^{5/2}\bigr)^{h_K/2},
$$
以及显式的 $|D_K|$ 增长下界。它有效地排除了列出的十七个完整商域子范围，但允许商域判别式和小素数理想类阶共同增长。

## 5. 严格保留的缺口

环类群分裂并不强迫 $h_K=1$。例如若 $\gcd(h_K,p+1)=1$，相应有限交换群正合列按阶数互素本来就分裂。非主分裂素数处的迹界增加了算术信息，但只给阶数下界。

有限域有理性也不能直接提升成有理系数的 CM 特征零对象。[此前 classfield-signature 笔记](2026-11-12-classfield-signature-cont.md) 已构造实际权二 CM 新形式：残余表示具有本题的 $\mathbb F_p$ 有理性、完整正规化子像和正确 $p$ 处局部类型，而系数域仍为 $\mathbb Q(\sqrt3)$。那个构造不是椭圆曲线反例，却足以阻止这一步形式推理。

当前剩余的具体问题是：能否从实际 $E/\mathbb Q$ 的整数迹和变化环类群之间，再取得一个不随 $K$ 类阶增长的约束。R58 本身以及上述已发表 fixed-field 定理均未提供该约束。
