# R29：四次 CM 同余的全局辛符号与残余特征处的独立计算

日期：2026-11-12。状态：**已证明的必要条件；中间进展**。

沿用 R24：$p>37$、$p\equiv7\pmod{12}$，$K=\mathbb Q(i)$，$E_0/\mathbb Q$ 无 CM，$d$ 为非零有符号平方自由整数，且
$$
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3-dx.
$$
其像为完整 $N_{\rm ns}(p)$。本结果给出所有惯性阶为 $4$ 的奇惰性素数处必须共同满足的辛符号；若 $p\mid d$，还独立计算 $p$ 处的符号。只引用已经发表的 Freitas–Kraus (2022) 判据，不调用 2025–2026 年新的局部可解性分类。

## 1. 全局符号及主结论

对一个 Galois 同构 $\phi:E_0[p]\to A_d[p]$，写
$$
e_{A_d,p}(\phi P,\phi Q)=e_{E_0,p}(P,Q)^{\mu(\phi)},
\qquad
\kappa=\left(\frac{\mu(\phi)}p\right)\in\{\pm1\}.
$$
$\kappa=+1$ 表示辛，$-1$ 表示反辛。这里采用通常允许平方乘子的定义。完整正规化子的中心化子为标量，故所有全局同构具有同一个 $\kappa$。

对每个 $q\mid d$、$q\equiv3\pmod4$、$q\ne p$，令
$$
\delta_q=v_q(\Delta_{E_0}^{\min}),\qquad
u_q=\Delta_{E_0}^{\min}/q^{\delta_q},\qquad
u'_q=64(d/q)^3.
$$
两单位的平方类不依赖极小模型的选择。定义
$$
r_q=\begin{cases}0,&\delta_q\equiv3\pmod4,\\1,&\delta_q\not\equiv3\pmod4,\end{cases}
\qquad
t_q=\begin{cases}0,&(u_q/q)=(u'_q/q),\\1,&(u_q/q)\ne(u'_q/q).\end{cases}
$$

**定理。**

1. 对所有上述 $q$（包含满足条件的 $q=3$），
   $$
   \boxed{\kappa=
   \left(\frac qp\right)^{r_q}
   \left(\frac2p\right)^{t_q}.}
   \tag{29.1}
   $$
   因此各素数给出的右端必须一致。
2. 若 $p\equiv7\pmod{24}$，则
   $$
   \boxed{\kappa=+1.}
   \tag{29.2}
   $$
   特别地，若 $q\mid d$、$q\equiv3\pmod4$、$q\ne p$ 且 $(q/p)=-1$，则 $r_q=0$。对 $q\ge5$，这强迫 $E_0$ 在 $q$ 为 III 型，不能为 III$^*$ 型。
3. 假设 $p\mid d$。由 R24，$E_0,A_d$ 在 $p$ 均为 III 型，且 $v_p(c_4(E_0))=1$。令
   $$
   R_p=\frac{c_4(E_0)}{48d}\in\mathbb Z_p^\times,
   \qquad
   t_p=\frac{1-(R_p/p)}2\in\{0,1\}.
   $$
   则有一个不依赖新局部分类的公式
   $$
   \boxed{\kappa=\left(\frac2p\right)^{t_p}.}
   \tag{29.3}
   $$
   因而在 $p\equiv19\pmod{24}$、$p\mid d$ 时，所有上述奇惰性 $q\ne p$ 都满足实际的两处兼容条件
   $$
   \boxed{
   \left(\frac qp\right)^{r_q}(-1)^{t_q}
   =\left(\frac{R_p}p\right).
   }
   \tag{29.4}
   $$

## 2. 为什么全局只有一个符号

把 Cartan $C$ 识别为乘法群 $\mathbb F_{p^2}^\times$。与 $C$ 交换的矩阵是同一域的乘法算子；再与一个 Cartan 外的半线性映射交换，强迫该域元素满足 $x^p=x$。所以
$$
\operatorname{Cent}_{\mathrm{GL}_2(\mathbb F_p)}(N)=\mathbb F_p^\times I.
$$
任意两个全局同构之比为这样的标量，其行列式为平方，故不改变 $\kappa$。同时，一个全局同构限制到各局部群时，Weil 乘子仍为同一个 $\mu(\phi)$；因此任何能确定局部辛类型的素数都必须给同一个符号。

## 3. 奇惰性素数的已发表判据

R24 给出：$q\mid d$ 的奇素数处，两曲线均温和潜在好约化，最小好约化惯性阶为 $4$；$A_d$ 的极小判别式赋值为 $3$，单位部分为 $64(d/q)^3$。

Freitas–Kraus, *On the symplectic type of isomorphisms of the p-torsion of elliptic curves*, Memoirs AMS **277**, no. 1361 (2022), Theorem 5，适用于 $q\equiv3\pmod4$、惯性阶 $4$、$p\ge5$、$q\ne p$。它断言局部同构的辛符号为
$$
(q/p)^r(2/p)^t,
$$
其中 $r$ 比较两个极小判别式赋值模 $4$，$t$ 比较两个单位判别式的平方性，且局部不能同时有两种类型。按上面的具体定义代入，正得到 (29.1)。该已发表定理允许 $q=3$，并非只对 $q\ge5$ 的公式。

## 4. $2$ 处是四元数惯性，故 $p\equiv7\pmod{24}$ 时全局必须辛

首先证明在本题的实际同余中，$A_d$ 在 $2$ 的最小好约化惯性群恰为 $Q_8$。

$A_d$ 的 $j=1728$，所以潜在好约化。其有限惯性像约化模 $p$ 忠实；又惯性行列式为 $1$，所以该像嵌入
$$
N\cap\mathrm{SL}_2(\mathbb F_p),\qquad
|N\cap\mathrm{SL}_2(\mathbb F_p)|=2(p+1).
$$
由于 $p\equiv1\pmod3$，$3\nmid2(p+1)$。椭圆曲线在剩余特征 $2$ 的潜在好约化惯性阶可能为 $1,2,3,4,6,8,24$；排除含 $3$ 的阶后，只剩 $1,2,4,8$。

商域 $\mathbb Q(i)$ 在 $2$ 分歧，所以惯性不能全部落在 Cartan 中。这排除阶 $1,2$：阶 $2$ 的非平凡保原点自同构只有 $[-1]$，在模 $p$ 上是标量。

阶 $4$ 也不可能。Freitas–Kraus 的 Proposition 6、Table 5（条目 C4）给出：在 $2$ 处惯性阶为 $4$ 时，极小不变量赋值只能为
$$
(v_2(c_4),v_2(c_6),v_2(\Delta))=(5,8,9)
\quad\text{或}\quad(7,11,15).
$$
尤其 $c_6\ne0$。但 $j(A_d)=1728$ 强迫 $c_6=0$，矛盾。故惯性阶为 $8$。其中只有一个非平凡二阶元素，且不存在八阶保原点自同构（见 R21 §5 的端同态特征多项式论证），所以它为四元数群 $Q_8$。

$E_0[p]\simeq A_d[p]$ 使两曲线在 $2$ 的惯性核相同，因而好约化惯性域相同。Freitas–Kraus 的 Theorem 8 给出：同一四元数惯性域的两条曲线，当 $(2/p)=1$ 时只能辛同构。$p\equiv7\pmod{24}$ 正满足 $(2/p)=1$，于是全局 $\kappa=+1$，得到 (29.2)。

代回 (29.1)，此时单位判别式项自动消失。若 $(q/p)=-1$，便必须 $r_q=0$。当 $q\ge5$ 时，III、III$^*$ 的判别式赋值分别为 $3,9$，对应 $r_q=0,1$，得到陈述中的排除。

## 5. 一个有限群概形引理：$\mathbb F_p$ 超奇异 $p$ 挠点的自同构只能有平方乘子

**引理 29.1。** 设 $S/\mathbb F_p$ 超奇异，$p>3$，因此 $a_p(S)=0$。则每个定义在 $\mathbb F_p$ 上的有限群概形自同构
$$
S[p]\longrightarrow S[p]
$$
对 Weil 配对的乘子都是 $\mathbb F_p$ 的平方。

**证明。** 使用经典 Dieudonné 理论及其与 Cartier 对偶的相容性。$D(S[p])$ 是一个二维 $\mathbb F_p$ 空间；因基域为 $\mathbb F_p$，$F,V$ 都是线性算子。Frobenius 与 Verschiebung 在 $S$ 上满足
$$
\pi+\pi^\vee=[a_p]=0,
\qquad \pi\pi^\vee=[p],
$$
所以在 $D(S[p])$ 上有 $V=-F$、$F^2=0$。$F\ne0$：椭圆曲线 Frobenius 的核阶为 $p$，不能杀死阶为 $p^2$ 的整个 $S[p]$。于是 $F$ 是一个非零的二阶幂零 Jordan 块。

与 $F,V$ 交换的可逆矩阵恰为
$$
aI+bF,\qquad a\in\mathbb F_p^\times,\ b\in\mathbb F_p,
$$
其行列式为 $a^2$。Weil 配对对应 Dieudonné 模上的非退化交替形式；二维空间中该形式的乘子就是行列式（采用反变约定时可能取逆，不影响平方性）。因此每个自同构的乘子为平方。证毕。

这里必须使用有限群概形和配对，不能仅看几何点：超奇异曲线在特征 $p$ 的几何 $p$ 挠点不足以保留所需信息。

## 6. $p\mid d$ 时独立计算 $p$ 处的辛符号

由 R24 引理 24.1，$E_0,A_d$ 在 $p$ 的极小判别式赋值都是 $3$，故为 III 型。在 $\mathbb Q_p$ 上使用短极小模型
$$
E_0:y^2=x^3-\frac{c_4}{48}x-\frac{c_6}{864},
\qquad v_p(c_4)=1,\quad v_p(c_6)\ge2.
$$
令 $\varpi^4=p$、$L=\mathbb Q_p(\varpi)$。$L$ 的剩余域仍为 $\mathbb F_p$。变换 $x=\varpi^2X$、$y=\varpi^3Y$ 给出好约化模型；其特殊纤维分别为
$$
\overline E_0:Y^2=X^3-bX,
\quad b=\overline{c_4/(48p)},
\qquad
\overline A_d:Y^2=X^3-b'X,
\quad b'=\overline{d/p}.
\tag{29.5}
$$
常数项在 $L$ 的赋值至少为 $2$，所以约化为零；$b,b'$ 都非零。

由于 $e(L)=4<p-1$，Raynaud 全忠实性把任意 $\mathbb Q_p$ 上的 $p$ 挠点同构延拓到好约化模型。Weil 配对在模型上延拓，且一般纤维的乘子等式因有限平坦性在整个模型上成立。因此约化得到定义在 $\mathbb F_p$ 上、具有**同一 Weil 乘子**的有限群概形同构
$$
\overline E_0[p]\simeq\overline A_d[p].
$$

$p\equiv3\pmod4$，所以 $\mathbb F_p$ 的四次幂子群等于平方子群。因此 (29.5) 的两个 $j=1728$ 曲线：

- 若 $b/b'$ 为平方，则它们在 $\mathbb F_p$ 上同构，存在乘子为 $1$ 的同构；
- 若 $b/b'$ 为非平方，则它们属于两个不同的 $\mathbb F_p$ 同构类。这两个类由有理的 $2$ 同源
  $$
  Y^2=X^3-b'X\longrightarrow Y^2=X^3+4b'X
  $$
  联系，因为 $-4$ 在 $\mathbb F_p$ 中为非平方。其在 $p$ 挠点上的 Weil 乘子为 $2$。

这两条约化曲线都超奇异。由引理 29.1，任意两个有限群概形同构之间只能改变一个平方乘子。所以辛符号分别为 $1$、$(2/p)$。因 $b/b'=R_p$，便得到 (29.3)。当 $p\equiv19\pmod{24}$ 时 $(2/p)=-1$，该符号就是 $(R_p/p)$；与 (29.1) 比较，得到 (29.4)。

上述证明完整处理了残余特征本身，没有将只能用于 $q\ne p$ 的 Freitas–Kraus Theorem 5 误用于 $q=p$。

## 7. 哪些部分重复、哪些确实增加了条件

在本节 $K=\mathbb Q(i)$ 的条件下，R15 的奇分歧素数限制没有可用的奇素数：$K$ 只在 $2$ 分歧。$q\mid d$ 是四次参考特征的分歧，而不是商二次域的奇分歧。因此不能从 R15 自动得到 (29.1) 或 III$^*$ 的排除。

R24 的分子平方类和导子也不区分奇 $q$ 处的 III 与 III$^*$：二者判别式赋值均为奇数、导子指数均为 $2$；将局部曲线二次扭曲一次可交换它们，而不改变 $j$。故上面的符号条件确实要求来自不同地方的同一个全局同构相容，包含 R24 没有记录的模 $4$ 赋值与单位信息。

不过，在 $p\equiv7\pmod{24}$、$p\mid d$ 时，(29.3) 给的 $p$ 处符号也是 $+1$，与 $2$ 处的 (29.2) 完全一致，**二者不构成新的相互矛盾**。这部分的作用是独立证明并核对残余特征处的条件。$p\equiv19\pmod{24}$ 时 (29.4) 则把 $p$ 处单位与全部奇惰性加性素数联系起来。

这些条件仍允许所有右端同时为 $+1$，或在第二个同余类中同时为同一个 $-1$。没有证明它们对每个非 CM 参数都会冲突，因此没有排除所有大的 $p$。

## 8. 已发表来源

1. N. Freitas, A. Kraus, *On the symplectic type of isomorphisms of the p-torsion of elliptic curves*, Memoirs of the American Mathematical Society **277** (2022), no. 1361，[出版页](https://doi.org/10.1090/memo/1361)，[与发表版本对应的作者全文](https://arxiv.org/pdf/1607.01218)：Theorem 5；Theorem 8；Proposition 6、Table 5。本文逐一核对了素数、惯性阶与同一惯性域的假设。
2. M. Demazure, *Lectures on p-Divisible Groups*, Lecture Notes in Mathematics **302** (1972)，Dieudonné 模与 Cartier 对偶，[出版页](https://doi.org/10.1007/BFb0060741)。这里只使用经典反等价、对偶及 Frobenius–Verschiebung 相容性；所需二维矩阵计算在引理 29.1 全部给出。
3. M. Raynaud (1974), *Schémas en groupes de type $(p,\ldots,p)$*，Théorème 3.3.3、Corollaire 3.3.6(1)；其准确范围和原文链接见 R21、R24。
