# 非分裂像、分歧互反律与类域论：继续研究

日期：2026-11-12。子代理 nonsplit_frobenius。状态：R15 已给完整必要条件；主要目标未解决。

## 1. 本轮已写入的完整结果

`../results/R15-ramification-splitting-and-cube-numerator.md` 给出：

- 若商域为 $K=\mathbb Q(\sqrt{-D})$，每个奇分歧素数 $q$ 都满足 $(-p/q)=1$。$q=3$ 可能有野惯性，证明通过在奇阶循环野惯性像中开平方，修正 Frobenius 提升，完整处理这一点。
- 将上述条件与 $p$ 在 $K$ 中惰性相乘，得到 $p\bmod8$ 与 $D\bmod8$ 的精确必要限制；无需把 $2$ 处假设成温和。
- $p\equiv1\pmod3$ 时，$j=A^3/B^p$ 且 $p\nmid AB$。$2,3$ 处也没有额外立方自由因子；关键是潜在好约化扩张的分歧指数 $e$ 不被 $3$ 整除，而判别式变换给 $12\mid e v_q(\Delta)$。

这些是新增的实际全局像必要条件，不是 R6/R7 的有限窗口构造的重写。

## 2. 类域论可达到的一个精确陈述

下面的命题也有完整证明，但它的作用是精确说明类域论路线还需要什么。它本身不给 $p$ 上界。

**命题。** 在 R15 的假设下，将 $C$ 识别为 $\mathbb F_{p^2}^{\times}$，得到满射特征
$$
\lambda:G_K\longrightarrow\mathbb F_{p^2}^{\times}.
$$
则 $\lambda^{12}$ 在 $K$ 的所有不位于 $p$ 上方的有限素数处不分歧，并在 $p$ 上方至多温和分歧，故对应一个模 $p\mathcal O_K$ 的射线类群特征。其像的阶为
$$
\frac{p^2-1}{12}.
\tag{2.1}
$$
此外，$\theta=\lambda^{12(p-1)}$ 是反圆分特征，像的阶为
$$
m_p=\frac{p+1}{\gcd(p+1,12)},
\tag{2.2}
$$
并且它经过导子 $p$ 的二次序 $\mathcal O_p=\mathbb Z+p\mathcal O_K$ 的环类群 $\operatorname{Pic}(\mathcal O_p)$ 分解。

**证明。** 取 $w\nmid p$。

若 $E$ 在 $w$ 潜在乘法，R2 表明模 $p$ 惯性像由标量 $\pm I$ 组成，所以 $\lambda^{12}$ 在该惯性群上平凡。

若 $E$ 在 $w$ 潜在好约化，其有限惯性像忠实地作用于一个好约化特殊纤维。限制到 $G_K$ 后像落在循环群 $C$ 中，因而为循环自同构群。椭圆曲线的有限阶自同构的阶只能是 $1,2,3,4,6$（包括剩余特征 $2,3$）；故它的阶整除 $12$，$\lambda^{12}$ 仍在惯性上平凡。这里不能说整个原惯性群都循环：$2$ 处可能有四元数群，$3$ 处可能有非交换的十二阶群；我们只用了它与 $C$ 的交是循环群。

在 $p$ 上方，$\lambda$ 的阶整除 $p^2-1$，所以野惯性作用平凡，导子指数至多为 $1$。由于 $p$ 在 $K$ 中惰性且不分歧，唯一的 $p$ 进局部域是 $K_p/\mathbb Q_p$ 的不分歧二次扩张。全局类域论现在给出所称的射线类群特征。$\lambda$ 满射，且 $p>3$ 时 $12\mid p^2-1$，故其十二次幂的像阶为 (2.1)。

复共轭在 $C$ 上作用为 $a\mapsto a^p$，于是
$$
\boxed{\theta^c=\lambda^{12p(p-1)}=\lambda^{-12(p-1)}=\theta^{-1}},
$$
因为指数 $12p(p-1)+12(p-1)=12(p^2-1)$。像阶由循环群幂映射公式给出 (2.2)。

最后说明环类群分解。$p$ 以外的局部单位已被杀死。在 $p$ 处，局部 Artin 互反下 $\lambda$ 在单位上的限制经过 $\mathbb F_{p^2}^{\times}$。任意群同态 $\mathbb F_{p^2}^{\times}\to\mathbb F_{p^2}^{\times}$ 都把其唯一的阶 $p-1$ 子群 $\mathbb F_p^\times$ 送入自己；因此 $\lambda^{p-1}$ 杀死 $\mathbb Z_p^\times$。它也杀死 $1+p\mathcal O_{K_p}$，故 $\theta$ 杀死
$$
\mathcal O_{p,p}^{\times}
=\mathbb Z_p^\times(1+p\mathcal O_{K_p}).
$$
在其他有限素数处，$\mathcal O_p$ 局部等于 $\mathcal O_K$，其单位也被杀死。这正是环类群的 idèle 描述。证毕。

**关于有限自同构阶的补充。** 可用椭圆曲线自同构分类，也可对任意有限阶自同构 $u$ 在一个不同于剩余特征的 Tate 模上考虑特征多项式：$u$ 的特征多项式为 $X^2-tX+1$，$t\in\mathbb Z$、$|t|\le2$。有限阶保证特征值为单位根；故只出现上述六种阶。这不排除非循环的有限自同构群，但足以控制其循环子群的指数。

## 3. 为什么环类群的阶不会自动给矛盾

记 $w_K=|\mathcal O_K^\times|\in\{2,4,6\}$。因为 $p$ 惰性，导子为 $p$ 的环类数公式为
$$
|\operatorname{Pic}(\mathcal O_p)|
=h_K\,\frac{p+1}{w_K/2}.
\tag{3.1}
$$
环类群到普通类群的核是循环群，阶为 $(p+1)/(w_K/2)$。这来自
$$
(\mathcal O_K/p\mathcal O_K)^\times/
\bigl((\mathbb Z/p\mathbb Z)^\times\operatorname{im}\mathcal O_K^\times\bigr)
$$
的显式描述；分母中单位贡献的额外指数为 $w_K/2$。

对于 $w_K=4$，$K=\mathbb Q(i)$ 且 $p\equiv3\pmod4$，所以 $w_K/2=2$ 整除 $\gcd(p+1,12)$。对于 $w_K=6$，$K=\mathbb Q(\sqrt{-3})$ 且 $p\equiv2\pmod3$，所以 $w_K/2=3$ 同样整除 $\gcd(p+1,12)$。其余情形 $w_K/2=1$。

因此对所有允许的 $K,p$，都有
$$
m_p\mid\frac{p+1}{w_K/2}.
$$
所以 (2.2) 所要求的阶**已经整除环类群中一个显式循环子群的阶**。有限阿贝尔群只要含有一个阶被 $m_p$ 整除的元素，就有一个循环商 $\mathbb Z/m_p\mathbb Z$：分解到 Sylow 子群和循环因子即可逐个素数取商。

结论是：单凭“存在阶 $m_p$ 的环类群特征”以及环类数公式，不能迫使 $h_K$ 大、不能迫使 $h_K=1$，也不能给 $p$ 上界。若继续此路，必须使用该特征的**具体局部限制、权与有理迹提升性质**，而不只是类群的阶。

## 4. 若强行提升为 CM Hecke 特征，缺口在哪里

残余二面体表示给出了一个有限阶 $\lambda$，并不自动给出来自 $\mathbb Q$ 上 CM 椭圆曲线的特征零表示。即使构造出适当的代数 Hecke 特征并取 theta 级数，其系数域也可能严格大于 $\mathbb Q$。模 $p$ 约化的迹落在 $\mathbb F_p$，不推出特征零迹为有理数。

一个准确的区分是：

- $\bar\rho_{E,p}$ 是 $\mathbb F_p$ 上定义的二维表示；
- 某个 CM theta 级数的系数域在 $p$ 上方可有剩余次数 $1$，所以它也可能给 $\mathbb F_p$ 上的同一残余表示；
- 由二者模 $p$ 同构推出 $E$ 在特征零是 CM，正是需要额外同余刚性的步骤。

用 Faltings 同源定理代替最后一步不成立：只有一个有限层 $p$ 挠点，没有完整的 Tate 模同构。用环类数 $h_K$ 代替也不成立，第 3 节已说明简单的阶计数无效。

## 5. 立方分子与广义 Fermat 方程路线

对 $p\equiv1\pmod3$，R15 给 $j=A^3/B^p$。将 $j=c_4^3/\Delta$ 与
$$
c_4^3-c_6^2=1728\Delta
$$
结合，确实会产生形如
$$
x^3-y^2=d^3 z^p
$$
的带参数方程。但潜在好约化素数留下的系数 $d$ 不受统一控制。它不能被默认为只支持 $2,3$：例如惯性阶 $4$ 的素数可以任意变化，而且正是商二次域分歧支集的一部分。

即使再用 R15 要求这些分歧素数分裂于 $\mathbb Q(\sqrt{-p})$，可用素数仍无穷多；现有论证没有给 $d$ 的大小或素因子数量以统一上界。因此这里尚未得到一个固定系数的广义 Fermat 问题。

## 6. 新文献核查

1. D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Bull. London Math. Soc. **54** (2022), 2404–2417，[正式页面](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.12701)、[作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)。重点核查 Lemma 2.3、Remark 2.4、Lemma 2.5 和 §5。Remark 2.4 还说 $p\equiv1\pmod4$ 时，商特征的分歧支集恰是文中候选集合（去掉 $p$），而不仅是包含于它。
2. L. Furio, D. Lombardo, *Serre's uniformity question and proper subgroups of $C_{ns}^+(p)$*, [v2 HTML](https://arxiv.org/html/2305.17780v2)，2025-11-25；[作者发表列表](https://people.dm.unipi.it/lombardo/Publications.php) 标明 Algebra & Number Theory to appear。其 §3.2 Theorem 3.11 的无 canonical subgroup 结论可以导出 R15 的潜在超奇异性，但 R15 已另外给出所需普通约化排除，不依赖这个额外输入。
3. M. Bisatt, L. Furio, D. Lombardo, *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, [arXiv:2603.04021v2](https://arxiv.org/abs/2603.04021)，2026-06-08。摘要声称：无 CM 全局曲线的 $p$ 进像是某个 $p^n$ 层非分裂正规化子的完整逆像。已向主代理报告它与提升/变形方向相关；本轮不把尚未确认发表的新结果当作必要输入。
4. Furio–Lombardo 2026 年已发表的 *On 7-adic Galois representations for elliptic curves over $\mathbb Q$*，[期刊页面](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70193)，Introduction 仍明确把 Serre 一致性列为开放问题；现有研究没有检索到公认的完整解决。

## 7. 当前确切边界

已完成的是分歧支集的一组新显式限制及一个类域论层面的精确归约。仍缺一个将这些条件与“来自有理系数的椭圆曲线”结合的统一全局定理。特别是 $K=\mathbb Q(i)$、$p\equiv3\pmod4$ 的情形与全部新限制相容；因此不能将 R15 或第 2 节的环类群陈述登记为主目标完成。

## 8. 后续完成的 R20 与检验边界

主代理指定继续比较 $K$ 与去掉分母后的判别式平方类，已完成
`../results/R20-exact-quotient-field-and-small-unit-tests.md`。
当 $p\equiv1\pmod4$ 时，按实际既约分数 $j=a/b$ 取 $n=a-1728b$，并令
$m=\operatorname{sf}(|\operatorname{oddpart}(n)|)$，则
$$
K=\mathbb Q(\sqrt{-2^\delta m}),\qquad
\delta=\mathbf 1_{\{v_2(j)\in\{3,6,9\}\}}.
$$
这同时处理了 $q=3$、$p$ 是否在候选支集中以及 $2$ 处基本判别式指数 $2$ 与 $3$ 的区别。对固定 $j$，该同余类中的所有异常素数共享这个商域。

R20 还给出适用于任意异常 $p>37$ 的显式单位检验：$v_2(j)=0$ 时 $2$ 在 $K$ 中分裂，$D\equiv7\pmod8$ 且 $(-7/p)=-1$；$v_3(j)=0$ 时 $3$ 分裂且 $D\equiv2\pmod3$，再按 $j\bmod3$ 得 $(-11/p)=-1$ 或 $(-2/p)=-1$。证明构造了同 $j$ 的实际好约化二次扭曲，并完整数点。

尝试将这些条件与 $p$ 处超奇异性拼成矛盾时，必须注意一些表面上独立的条件其实相容。例如 $p\equiv1\pmod4$ 时，好超奇异约化有 $a_p=0$、$\#E(\mathbb F_p)=p+1\equiv2\pmod4$；其 $2$ 挠点 Frobenius 因而可以是换位，判别式为非平方，这与 R5 的 $p$ 惰性及 R20 的商域公式并不冲突。不能将这种局部相容性包装成一个排除所有 $p$ 的论证。
