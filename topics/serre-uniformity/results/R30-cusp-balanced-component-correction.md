# R30. 尖点闭包的平衡交数与坏素数处统一乘二修正

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 对 $X_{\rm ns}^+(p)$、$p\ge17$，令 $D$ 为全部尖点之和、$d=(p-1)/2$。R28 对任意次数零族使用分量群指数，统一可取乘子 $p-1$；对于 R14、R18 的**这个特定规范平移族**，乘子 **$2$ 已足够**。关键是尖点闭包在超奇异分量 $C_i$ 上的交数恰为 $6/e_i$，从而 $u_D=[dx-D]$ 的分量像被 $2$ 消去，R14 的规范平移常量亦然。

本文计算的是已发表正则模型上的交数与 Néron 分量。没有声称乘二之后最终拉回线丛自动在整个光滑开集平凡；R28 的剩余垂直向量条件仍须保留。

## 1. 记号与所用模型

固定 $p\ge17$，令 $R=\mathbb Z_p^{\rm ur}$，$K=\mathbb Q_p^{\rm ur}$，剩余域为 $\overline{\mathbb F}_p$。也可对这些环作完备化。令
$$\sigma:\mathcal Y\longrightarrow\mathcal X$$
为 Edixhoven–Parent (2024) 的正规交叉模型到最小正则模型的收缩：$\mathcal Y$ 是 Theorem 3.4 的模型，一般不约化；$\mathcal X$ 是 Corollary 3.2 的模型，特纤维约化。记
$$U=\mathcal X^{\rm sm},\qquad \mathcal X_k=\sum_i C_i,\qquad U_i=C_i\cap U.$$
各 $C_i$ 对应一个超奇异 $j_i$，设
$$e_i=\begin{cases}3&j_i=0,\\2&j_i=1728,\\1&\text{其他。}\end{cases}$$
只对实际超奇异的例外值使用 $2$ 或 $3$。R28 已从该正规交叉树完整计算
$$L=-\bigl(C_i\cdot C_j\bigr)
=(p-1)\operatorname{diag}(1/e_i)
-12(1/e_i)_i(1/e_i)_i^{\mathsf t},\tag{1.1}$$
以及
$$\sum_i\frac1{e_i}=\frac{p-1}{12}=\frac d6,\qquad
\Phi=\{z\in\mathbb Z^n:\sum_i z_i=0\}/L\mathbb Z^n.\tag{1.2}$$
特别地 $(p-1)\Phi=0$，且 $[z]=0$ 当且仅当所有 $e_i z_i$ 模 $p-1$ 同余。

令 $D_K$ 为 $X=X_{\rm ns}^+(p)_K$ 的全部尖点之和，次数 $d$；其在 $\mathcal Y$、$\mathcal X$ 上的水平闭包分别记为 $D_{\mathcal Y},D_{\mathcal X}$。二者都是有限平坦 Cartier 除子。

## 2. 尖点在正规交叉模型上的位置

**引理 1。** 在 $\mathcal Y$ 上，$D_{\mathcal Y}$ 只与中央 Igusa 分量 $A$ 相交，且
$$D_{\mathcal Y}\cdot A=1.\tag{2.1}$$

**证明。** 先核实这一位置描述所需的 $j$-映射。Edixhoven–Parent (2021), §2.2 的半稳定模型从 Katz–Mazur 模型经闭点吹起、基扩张和正规化构造；每一步仍带有原模问题的遗忘 $j$-映射。Edixhoven–Parent (2024), Theorem 3.4 的证明再取保持 $j$ 的 Galois/模群商，并解消其奇点。这些商映射下，不变的 $j$-映射下降；解消后仍保留该映射。因此正规交叉模型 $\mathcal Y$ 上确有延拓泛纤维遗忘映射的态射
$$j:\mathcal Y\longrightarrow\mathbb P^1_R.$$
这里没有在已经收缩了中央分量的 $\mathcal X$ 上假设 $j$-映射仍处处正则。

Theorem 3.4 的中央 Igusa 分量是 $j$-线，其 $j=\infty$ 支集为单一点。全部其他分量位于有限的超奇异 $j$ 值或普通例外值 $j=0$ 之上。因 $D_K$ 在泛纤维正是尖点支集，其所有特化位于 $j=\infty$，故 $D_{\mathcal Y}$ 只遇到 $A$ 的该点，而不遇到其他分量。此论断只用支集，不需要把 Igusa 模解释中的可能纯不可分参数化识别为某个指定局部参数。

$A$ 在 $\mathcal Y_k$ 中的重数是 $N=(p-1)/2=d$。由有限平坦性，水平除子 $D_{\mathcal Y}$ 与整个纤维的交数等于其次数 $d$，所以
$$d=D_{\mathcal Y}\cdot\mathcal Y_k
=N(D_{\mathcal Y}\cdot A)=d(D_{\mathcal Y}\cdot A).$$
因此交数为 $1$。这也说明它在该正则点与 $A$ 横截，但不意味着 $D_{\mathcal Y}\to\operatorname{Spec}R$ 为 étale：该纤维分量的重数是 $d$。证毕。

这段证明使用已发表构造中的遗忘映射及给出的分量位置，并自行计算水平交数；不依赖 2026 年未公认的模解释或交数公式。

## 3. 最小正则模型上的尖点交数

**定理 2。** 对每个超奇异分量，
$$\boxed{\quad r_i:=D_{\mathcal X}\cdot C_i=\frac6{e_i}.\quad}\tag{3.1}$$
即一般分量为 $6$，$j=1728$ 分量为 $3$，$j=0$ 分量为 $2$。

**证明。** $D_{\mathcal Y}$ 是 $D_{\mathcal X}$ 的严格变换，投影公式给出
$$D_{\mathcal X}\cdot C_i=D_{\mathcal Y}\cdot\sigma^*C_i.$$
由引理 1，右侧等于 $A$ 在 $\sigma^*C_i$ 中的系数。

计算该系数可直接使用 R28 §6 的 Schur 补。在消去除 $A$ 与保留分量 $F_i$ 以外的全部分量后，有效交数是
$$A^2=-\frac13,\qquad A\cdot F_i=\frac2{e_i},\qquad
F_i^2=-\frac{p-1}{e_i}.$$
总拉回 $\sigma^*C_i$ 与 $A$ 的交数为零。在其严格变换 $F_i$ 的系数为 $1$、其他保留分量系数为零的条件下，若 $A$ 的系数为 $c_i$，消去其他被收缩分量后的正交条件为
$$\frac2{e_i}-\frac{c_i}{3}=0.$$
所以 $c_i=6/e_i$，得到 (3.1)。这是总拉回的正交方程，不能把一般垂直线丛从 $\mathcal Y$ 生硬限制到 $\mathcal X$ 来替代。证毕。

检验总次数：$\sum_i r_i=6\sum_i1/e_i=d$，与 $D_K$ 的次数一致。全部尖点在 $\mathcal X$ 的共同奇点相遇也不妨碍 R28 的有限平坦范数；它已允许 $D$ 穿过分量交点。

## 4. 无基点 Abel–Jacobi 映射的分量像被二消去

令 $\mathcal J$ 为 $J=\operatorname{Pic}^0_{X/K}$ 的 Néron 模型，$\mathcal J^0$ 为恒等分量。态射
$$u_D:X\longrightarrow J,\qquad x\longmapsto[dx-D_K]$$
延拓到 $u_D:U\to\mathcal J$。

**定理 3。**
$$\boxed{\quad[2]\circ u_D:U\longrightarrow\mathcal J^0.\quad}\tag{4.1}$$
更精确地，$u_D(U_j)$ 的分量类为
$$z^{(j)}_i=d\,\mathbf1_{i=j}-\frac6{e_i}.\tag{4.2}$$
当 $e_j$ 为奇数时它恰有阶 $2$；当 $e_j=2$ 时它为零。于是只要存在超奇异 $j=1728$，该分量上的 $u_D$ 本身已进入恒等分量。

**证明。** 取 $b\in U_j(R)$，存在性来自 Hensel 性。水平截面 $b$ 在 $C_j$ 上交数为 $1$，在其他分量上为零；所以线丛 $\mathcal O(db-D_{\mathcal X})$ 的多度数为 (4.2)。由 Picard/Néron 分量群描述，这就是 $u_D(b)$ 的分量类。它在整个连通 $U_j$ 上相同。

直接将 (1.1) 乘以 $e_j\mathbf e_j$，其中 $\mathbf e_j$ 是第 $j$ 个坐标单位向量，得到
$$L(e_j\mathbf e_j)
=(p-1)\mathbf e_j-12(1/e_i)_i
=2z^{(j)}.\tag{4.3}$$
所以该类被 $2$ 消去。其是否为零也可精确检验：
$$e_i z_i^{(j)}=-6+d e_j\mathbf1_{i=j}.$$
因 $p\ge17$ 时至少有两个超奇异分量，R28 的零类判据说明它为零当且仅当 $2d\mid d e_j$，即 $e_j$ 偶数。证毕。

式 (4.3) 还给出一个直接的实际线丛族。以 $\gamma:U\hookrightarrow\mathcal X\times_RU$ 为对角图，$d\gamma-D_{\mathcal X}\times_RU$ 在第一变量的多度数为 (4.2)，故
$$
\mathcal O\left(2d\gamma-2D_{\mathcal X}\times_RU
+\sum_j e_j(C_j\times_kU_j)\right)\tag{4.4}
$$
具有每个分量次数零，并代表 $2u_D$。对角图在该空间上是 Cartier 除子：它附近第一个曲线坐标位于光滑开集，而整个空间正则。

## 5. R14 的规范平移也被二消去

回到 R14 的假设。令 $a:J^\vee\to J$ 为 Abel–Jacobi 拉回的自对偶同构，$f:J\to J^\vee$ 是实际同态，满足
$$\deg\bigl((u_D,fu_D)^*\mathcal P\bigr)=0.$$
R14 定义实际次数零线丛类 $\eta_D\in J(K)$、平移
$$c_D=-a^{-1}\eta_D,\qquad h_D(t)=f(t)+c_D.$$
其关键恒等式为：对任意 $b\in X(K)$，
$$\eta_D=d\kappa_b+a\bigl((f+f^\vee)e_b\bigr),\qquad
e_b=[db-D_K],\quad
\kappa_b=[(i_b,fi_b)^*\mathcal P].\tag{5.1}$$
次数零假设保证这里的 $\kappa_b$ 属于 $J(K)$；R14 已证明 (5.1) 和基点独立性，不需要在 $J(K)$ 中解乘 $d$ 方程。

**定理 4。** $\eta_D$、$c_D$ 的 Néron 分量类均被 $2$ 消去，并且
$$\boxed{\quad[2]\circ h_D\circ u_D:U\longrightarrow\mathcal J^{\vee,0}.\quad}\tag{5.2}$$

**证明。** 取 $b\in U(R)$。由定理 3，$e_b=u_D(b)$ 的分量类被 $2$ 消去。所有 Jacobian 同态及 $a$ 都延拓为 Néron 模型之间的同态，因此保持恒等分量并诱导分量群同态。

另一方面 $2d=p-1$ 消去整个 $\Phi$，故 $d\kappa_b$ 的分量类被 $2$ 消去。式 (5.1) 的两项均被 $2$ 消去，因此 $\eta_D$ 如此，$c_D=-a^{-1}\eta_D$ 亦如此。对每个分量的 $u_D$，其经 $f$ 的像被 $2$ 消去；加上 $c_D$ 后仍然如此，得到 (5.2)。证毕。

此论证允许 $f$ 有非平凡反对称部分，且没有使用 Hecke 对应的额外性质。实际应用中，$f$ 可取来自 R18 的实际对应线丛。关键是 R14 的次数零条件和规范平移，不能把定理 4 套到任意未经修正的仿射态射上。

## 6. 实际族与范数：不再需要乘 $p-1$

令 $\mathscr T$ 为 R18 实际族 $\mathcal T_D$ 在 $\mathcal X\times_RU$ 上的任意线丛延拓，其泛纤维 Picard 类为
$$v_D=a\circ h_D\circ u_D=F\circ u_D-\eta_D.$$
记它在参数分量 $U_j$ 上、第一变量分量 $C_i$ 的次数为 $\delta_i^{(j)}$。由定理 4，$[\delta^{(j)}]\in\Phi$ 被 $2$ 消去。

固定一个分量指标 $i_0$。R28 的精确阶判据保证
$$a_{ij}:=\frac{e_i\delta_i^{(j)}-e_{i_0}\delta_{i_0}^{(j)}}{d}\in\mathbb Z.\tag{6.1}$$
这些列向量满足 $La^{(j)}=2\delta^{(j)}$。故令
$$A=\sum_{i,j}a_{ij}(C_i\times_kU_j),\qquad
\mathscr T^\circ=\mathscr T^{\otimes2}\otimes\mathcal O(A),\tag{6.2}$$
便得到实际的全分量次数零族，其 Picard 类是 $2v_D$。

**定理 5（简化后的范数修正）。** 令 $\mathcal E_D$ 为 R28 的评价—范数表达式，则
$$
\boxed{\quad
\mathcal E_D(\mathscr T^\circ)
\simeq\mathcal E_D(\mathscr T)^{\otimes2}\otimes
\mathcal O_U\left(\sum_j e_j\delta_j^{(j)}U_j\right)
\simeq(u_D,2h_Du_D)^*\mathcal P^{\rm ext}.
\quad}\tag{6.3}
$$
全部同构保持泛纤维的自然识别，无 $d$ 次根或未检查的单位因子。

**证明。** R28 的公式给出修正系数
$$b_j=d a_{jj}-\sum_i r_i a_{ij}.$$
令 $t_j=e_{i_0}\delta_{i_0}^{(j)}$。用 $r_i=6/e_i$、$\sum_i\delta_i^{(j)}=0$ 和 $\sum_i1/e_i=d/6$，计算
$$
\sum_i r_i a_{ij}
=\frac6d\sum_i\left(\delta_i^{(j)}-\frac{t_j}{e_i}\right)
=-t_j.
$$
又 $d a_{jj}=e_j\delta_j^{(j)}-t_j$，所以 $b_j=e_j\delta_j^{(j)}$。这证明第一同构；第二同构由 R28 定理 3 得到。R28 已独立证明有限平坦范数、泛纤维同构的单位延拓、任意延拓和列常数的消去，故这里没有新的下降歧义。证毕。

若 R14 的一个泛纤维平凡化截面 $s$ 在原范数线丛上的垂直系数为 $n_j$，则在 (6.3) 左侧，$s^{\otimes2}$ 的系数精确为
$$\boxed{\quad k_j=2n_j+e_j\delta_j^{(j)}.\quad}\tag{6.4}$$
单分量开集上乘 $p^{-k_j}$ 得到实际积分 torsor 截面；全 $U$ 存在同一个积分平凡化当且仅当所有 $k_j$ 相等。这里仍不能仅由 $\mathscr T^\circ$ 的第一变量多度数零推断 (6.4) 常值。

## 7. 范围和后续数学缺口

R28 给任意次数零族的坏约化修正，R30 额外使用全部尖点构成的基准和 R14 的特定规范平移，把其通用乘子 $p-1$ 改为绝对乘子 $2$。这一结论是对每个 $p\ge17$ 成立的几何公式，不是有限层数值观察。它在每个奇数辅助素数处都是单位乘子；但 $u_D$ 自身仍含 $[d]$，所以没有消除辅助素数整除 $d$ 时的一阶退化问题。

即使乘二修正已经显式，仍需计算实际对应族的 $\delta_i^{(j)}$ 与全局平凡化的 $n_j$，并理解 (6.4)；更进一步的 QC 共同零点排除还包含局部高度和迭代积分项。本文没有从分量群计算推出这些分析条件，也没有达到 Serre 一致性问题的完成标准。

## 8. 原始来源及使用范围

- B. Edixhoven and P. Parent, **Semistable reduction of modular curves associated with maximal subgroups in prime level**, *Documenta Mathematica* **26** (2021), 231–269, DOI [10.4171/DM/814](https://doi.org/10.4171/DM/814)；[作者保存的已发表全文](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)。§2.2（pp. 238–240）说明从 Katz–Mazur 模型经吹起、基变换、正规化构造半稳定模型；Igusa 分量来自原模型、Drinfeld 分量位于超奇异点之上。本文只使用这些保持遗忘 $j$-映射的构造事实。
- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058, DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)；[期刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.4 给中央 $j$-线、分量位置与重数；其证明给保持 $j$ 的商与解消；Corollary 3.2 给向约化最小正则模型的收缩。上述尖点交数及统一乘二结论由本文推导，而非原文定理的逐字引用。
- 仓库 R14：规范平移恒等式 (5.1)、实际有理线丛及泛纤维平凡化。R18：实际对应线丛族与范数刚性化。R28：全部剩余类交矩阵、分量群判据、有限平坦范数与积分单位性证明。
