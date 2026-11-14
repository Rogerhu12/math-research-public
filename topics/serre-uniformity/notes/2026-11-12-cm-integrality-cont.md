# 固定 CM 分母与广义 Fermat 路线：第二轮完整归约和适用范围

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

## 1. 这轮实际推进了什么

固定 $A:y^2=x^3-x$，研究 $p>37$、$p\equiv3\pmod4$ 的 $E[p]\simeq A[p]$。R11 已处理 $j(E)$ 整数的情形；R13 把非 CM 情形压到非空的乘性分母集合。本轮不是再证明这两个结论，而是把剩余分母问题化为精确的整数方程。

- [R16](../results/R16-fixed-cm-discriminant-fermat.md)：全局极小判别式为 $\epsilon2^\delta b^p$，$\delta=6,9,12$；在 $3$ 处 $v_3(c_4)=1,v_3(c_6)\ge3$；归一化后只有 $X^3-27W^2=Z^p$ 或 $8Z^p$ 两个原始方程。给出不依赖高度上界的 Szpiro 比下界。
- [R19](../results/R19-converse-fermat-fixed-cm.md)：证明反向对应。三个整数族的精确模 $4$ 条件由显式整坐标变换得到，再由模性、不可约性及 Ribet 降层回到唯一层 $32$ 新形式。此后无需保留“检查局部导子”的隐含谓词。还排除全部 $p\equiv1\pmod4$ 指数。

这些是已证明的归约，不是已经求解变指数方程。R19 的证明特意处理了两个容易出错的环节：$q\equiv1\pmod p$ 并不阻止本题降层，因为当前层始终与 $p$ 互素；乘性点上的惯性不分歧也不等同于整个局部 Tate 扩张分裂。

## 2. 最终需要排除的三个显式整数族

对 $p>37$、$p\equiv3\pmod4$，要求
$$
|Z|>1,\quad \gcd(Z,6p)=1,\quad3\nmid X,\quad
\gcd(X,W)=\gcd(X,Z)=\gcd(W,Z)=1.
$$
剩余等价问题为以下三族的最终无解性：

| 族 | 方程 | 同余条件 | 对应 Frey 模型 |
|---|---|---|---|
| I | $X^3-27W^2=Z^p$ | $X\equiv1\pmod4$，$W$ 偶 | $y^2=x^3-Xx-2W$ |
| II | $X^3-27W^2=8Z^p$ | $X,W$ 奇；方程强制 $X\equiv3\pmod8$ | $y^2=x^3-Xx-2W$ |
| III | $X^3-27W^2=Z^p$ | $X,W$ 奇偶相反，$X\equiv2,3\pmod4$ | $y^2=x^3-4Xx-16W$ |

任何实际解都自动满足
$$
q\mid Z\Rightarrow q\equiv\pm1\pmod{4p},\qquad
Z\equiv\pm1\pmod9,
$$
以及 $X\equiv2\pmod3$ 或 $3\mid W$。R19 使这些限制成为已证全局必要条件；它们本身没有给出 $|X|,|W|,|Z|$ 的上界。

特别地，$\delta=6$ 的原始奇偶性不足以推出导子指数 $5$。$X=-1,W=0$ 给出 $y^2=x^3+x$，其 $f_2=6$。真正的条件是 $X\equiv1\pmod4$。$\delta=12$ 的两个有效分支分别为 $I_3^*$ 和 III$^*$，不能只从 $\delta$ 猜测 Kodaira 型。

## 3. Darmon–Merel 和 Bennett–Skinner 没有直接解决这里的方程

已经查阅两篇原始来源的陈述：

1. H. Darmon, L. Merel, *Winding quotients and some variants of Fermat's Last Theorem*, J. reine angew. Math. **490** (1997), 81–100，[DOI](https://doi.org/10.1515/crll.1997.490.81)，[作者存档](https://perso.imj-prg.fr/loic-merel/wp-content/uploads/merel-pub/winding.pdf)。其引言列出的基本族为 $x^n+y^n=2z^n$、$x^n+y^n=z^2$ 和 $x^n+y^n=z^3$。
2. M. A. Bennett, C. M. Skinner, *Ternary Diophantine Equations via Galois Representations and Modular Forms*, Canad. J. Math. **56** (2004), 23–54，[DOI](https://doi.org/10.4153/CJM-2004-002-2)，[期刊陈述](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/ternary-diophantine-equations-via-galois-representations-and-modular-forms/EE8F7CB50159F52DE5CCA7350CD8936C)。其研究的一般形式是 $Ax^n+By^n=Cz^2$，即两个变量具有相同的变指数。

本题的指数是 $(3,2,p)$。单纯交换变量、移项或把 $27=3^3$ 提出，不能制造第二个 $p$ 次幂。因此不能将这些定理当作本题全部指数的无解定理。若想调用其中某个特殊结论，必须先证明一个保留整数性、原始性及固定系数的新变换；本轮没有得到这种变换。

这里还有一个结构上的区别：若相应 Frey 曲线已有有理 $2$-同源，R8 等已有结果就能排除 $p>37$ 的非 CM 同余；本题的普通 Frey 曲线并不自动带有有理 $2$-挠点。其 $2$-挠点由三次式 $x^3-Xx-2W$ 的根决定，判别式方程没有强制该三次式在 $\mathbb Q$ 上有根。

## 4. 变成标准 $a^2+b^3=c^p$ 会破坏原始性

对系数为 $1$ 的方程，有恒等式
$$
(27W)^2+(-3X)^3=-27Z^p.
$$
令 $k=(p-1)/2$，定义
$$
a=3^{3k+3}W,\qquad b=-3^{2k+1}X,\qquad c=-27Z.
$$
则
$$
a^2+b^3
=3^{6k}\bigl((27W)^2+(-3X)^3\bigr)
=(-27Z)^p=c^p.
$$
但 $a,b,c$ 都被 $3$ 整除，所以标准方程的原始解分类不能直接用于这个三元组。

对系数为 $8$ 的方程，先有
$$
(27W)^2+(-3X)^3=-216Z^p.
$$
用 $k=(p-1)/2$ 和权缩放
$$
a=6^{3k}27W,\qquad b=-6^{2k}3X,\qquad c=-216Z
$$
同样得到 $a^2+b^3=c^p$，同样明显非原始。这里不能把普通公因子直接约掉：三个坐标分别以 $2,3,p$ 次幂出现，约去一个共同整数不保持方程形状。

这一计算只解释一个常见误用为何失败。它不排除未来使用允许 $S$-原始条件的更细定理；那种定理仍须覆盖随 $p$ 增长的这些 $3$ 进或 $2,3$ 进赋值。

## 5. 更接近本题的广义 Fermat 文献

N. Freitas, B. Naskręcki, M. Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113，[DOI](https://doi.org/10.1112/S0010437X19007693)，[作者全文](https://arxiv.org/html/1703.05058v3)，研究原始 $a^2+b^3=c^p$。该文将问题化到有限多个 $X(p)$ 扭曲上的点，处理 $p=11$（其中计算的完备性有明确 GRH 假设），并得到 $p=13$ 的部分结果。其第 2 节的模性降层和第 3—5 节的局部比较可作方法参考，但没有给出本题全部充分大 $p$ 的结论。

该文 Theorem 3.1 也提醒：在 $2$ 处，导子指数 $5$、四元数惯性像的曲线仍可能有不同惯性域。仅知道 $f_2=5$，不能在任意两个局部曲线之间直接断言挠点同构。R19 没有犯这个错误：它依靠全局权 $2$ 降层和层 $32$ 的一维性得到同构，不以局部导子相同代替局部表示相同。

N. Freitas, D. Mocanu, I. Sanchez-Rodriguez, *Revisiting the equation $x^2+y^3=z^p$*, [arXiv:2512.10781](https://arxiv.org/abs/2512.10781)（2025-12-11），继续研究上述扭曲的局部点。这也不是全部 $(2,3,p)$ 方程的统一解法，更不直接覆盖第 4 节的非原始缩放。

本轮没有把“固定指数下有限多个曲线”误写成“所有充分大指数无解”。R19 的层 $32$ 本身确实含有 CM 新形式；这正是与 FLT 降到空的权 $2$ 层空间不同的环节。

## 6. 核查 2025—2026 文献后仍不能补上的一步

E. Studnia, *Congruences modulo 23 to $y^2=x^3-23$ are trivial*, [arXiv:2507.20801v2](https://arxiv.org/html/2507.20801v2)（2025-09-30），在引言 Conjecture 2 明确区分固定曲线的 Frey–Mazur 问题和其固定素数 $23$ 结果。其后续导子控制使用特定惯性及秩零商假设；本题 $A$ 在 $p\equiv3\pmod4$ 处好超奇异，局部 Cartan 像完整，不能直接填入要求较小惯性像的分支。

M. Bisatt, L. Furio, D. Lombardo, *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, [arXiv:2603.04021v2](https://arxiv.org/abs/2603.04021)（2026-06-08），给出非分裂 Cartan 情形的更高 $p$ 次幂像结构。这种结构细化没有排除本题的完整模 $p$ 正规化子。

另核查了 L. Furio, D. Lombardo, *On 7-adic Galois representations for elliptic curves over $\mathbb Q$*, Proc. London Math. Soc. **133** (2026), e70193，[已发表全文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70193)（2026-08-12）。它将一个固定 $7$ 进层的点问题化为特定广义 Fermat 方程并解决，研究范围仍是固定指数。

这些来源的作用是核查适用条件和截至本轮的公开进展，没有把检索中没找到更强结果当作数学上的“不可能性定理”。

## 7. 为什么统一判别式界足够，而现有归约还不够

R16 已无条件证明：若有非 CM 同余曲线，令 $Q=\operatorname{rad}(Z)$，则
$$
|\Delta_{\min}|\ge2^6Q^p,\qquad N=2^5Q,\qquad Q\ge4p-1.
$$
因此
$$
\frac{\log|\Delta_{\min}|}{\log N}
\ge
\frac{6\log2+p\log(4p-1)}{5\log2+\log(4p-1)}.
$$
若另外证明仅对此特殊曲线族有统一上界 $|\Delta_{\min}|\le C N^\kappa$，固定 $C,\kappa$ 就足以限制 $p$。本轮没有证明这样的上界；把它标成 Szpiro 型假设是必要的，不能删去。

另一种足够的输入是直接证明第 2 节三个族在所有充分大的 $p\equiv3\pmod4$ 无非平凡原始解。R19 表明这不是一个宽松的必要条件问题：在列明的精确同余条件下，它已经与固定 $A$ 的非 CM 同余排除等价。

## 8. 可复用的已排除误区

- $f_2=5$ 不是只有一种 Kodaira 型；必须使用完整 Tate 表。
- 原始奇偶性不足以保证 $f_2=5$；R19 给出了精确模 $4$ 条件及反向验证。
- $v_3(c_6)\ge2$ 是不必要的损失：本题可直接证明 $\ge3$，由此得到系数 $27$ 的整方程。
- Ribet 降层到真实存在的 CM 新形式不是矛盾。
- 一般层提升只保证某个新形式，不能凭此保证其系数域为 $\mathbb Q$；本轮的反向构造从一条实际整数 Frey 曲线开始，避免了这个存在性跳跃。
- 第 4 节的重缩放得到非原始标准 Fermat 解，不能使用只讨论原始解的结论。

**未证明的核心只剩在这里明确提出：** 对第 2 节三个变指数整数族给出一个统一的全局排除。R16、R19 都没有声称完成这一步；子问题的结果和失败路线已完整记录，供继续研究使用。
