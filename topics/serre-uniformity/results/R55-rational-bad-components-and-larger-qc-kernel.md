# R55. 坏素数处真正可达的分量与更大的 QC 零高度核

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 对 $p>37$，R28 所用的是 $\mathbb Z_p^{\rm ur}$ 上的约化最小正则模型，而不是分歧扩张后的稳定模型。本文在这个确切模型上证明：

1. 一个几何分量 $C_j$ 可由 $X_{\rm ns}^+(p)(\mathbb Q_p)$ 的点特化到其光滑部分，当且仅当其标号 $j$ 为 $\mathbb F_p$ 中的超奇异不变量。
2. 每个这样的光滑分量开集在 $\mathbb F_p$ 上同构于 $\mathbb A^1$，有恰 $p$ 个 $\mathbb F_p$ 点，且全部可提升到 $\mathbb Q_p$ 点。
3. 若 $s_p$ 为 $\mathbb F_p$ 中超奇异 $j$ 的个数，则 R54 的真实坏纤维有限靶集只有至多 $s_p=O(\sqrt p\log p)$ 个向量。可以把 R45 的几何积分核扩大到一个秩至少 $a-s_p$ 的整数格；在此格中，真实坏 $p$ 局部高度在全部 $\mathbb Q_p$ 点上恒零。

最后一项不要求线丛在所有几何分量上同时积分平凡化。它使用 QC 必要方程实际需要的局部点值条件，从而恢复原积分核省掉的一部分有效方向。全文仍未证明剩余有限靶集的辅助逆像只有 CM 点。

## 1. 确切模型、分量与忘却映射

令 $X=X_{\rm ns}^+(p)/\mathbb Q_p$。使用 Edixhoven–Parent (2024), Theorem 3.4 的最小正则正规交叉模型 $\mathscr Y$，以及 Corollary 3.2 中的收缩
$$\pi:\mathscr Y\longrightarrow\mathscr X,$$
其中 $\mathscr X$ 是约化的最小正则模型。先在 $\mathbb Z_p^{\rm ur}$ 上描述几何特殊纤维。

Theorem 3.4 给出中央 Igusa $j$-直线，重数为 $(p-1)/2$。在每个超奇异 $j$ 上有一条水平支链；每条支链包含唯一一个最终保留的重数 $1$ 分量，以下记为 $F_j$。

- 对 $j\ne0,1728$，原支链有一个重数 $p+1$ 的分量，其两个外侧分量的重数分别为 $1$ 和 $(p+1)/2$；保留的是重数 $1$ 的末端 $F_j$。
- 若 $j=0$ 超奇异，支链中的相应重数为 $(p+1)/3$、$1$、$(p+1)/6$；仍只保留重数 $1$ 的末端。
- 若 $j=1728$ 超奇异，Theorem 3.4 的正规交叉模型已将中间的可缩分量去掉；剩下一个重数 $1$ 的 $\mathbb P^1$ 与中央分量相交。
- 普通 $j=0$ 上的额外链全部收缩，不产生另一个保留分量。

各 $F_j$ 都是几何 $\mathbb P^1$，并且与将被收缩的分量并集恰在一个几何点相交。Corollary 3.2 及其证明把其余分量全部收缩到同一个点 $P$，保留分量的像为 $C_j$。因此
$$\pi:F_j\setminus\{q_j\}\xrightarrow{\sim}C_j\setminus\{P\},
\tag{1.1}$$
其中 $q_j$ 是上述唯一交点。所有非光滑点都集中在 $P$。记
$$U=\mathscr X^{\rm sm},\qquad U_j=C_j\cap U.$$
于是
$$U_j\otimes\overline{\mathbb F}_p\simeq\mathbb A^1_{\overline{\mathbb F}_p}.
\tag{1.2}$$
即使 $C_j$ 在 $P$ 自身有奇点，其正规化仍是 $F_j$，且 $P$ 的逆像只有 $q_j$ 一个几何点。

这里的 $F_j$ 是**未分歧基底上正则化后保留的末端分量**。它可能是解奇点时新增的例外曲线，不等同于分歧基变换后稳定模型中的 Drinfeld 曲线。Edixhoven–Parent 的引言特别提醒这些最终的约化片段通常没有原始细模意义；上述论证只使用该文实际给出的正则模型与收缩。

不过标号 $j$ 仍有严格的几何来源。构造 $\mathscr Y$ 的起点是 Katz–Mazur 模曲线；其忘却态射到 $j$-直线经过基变换、Galois 商及解奇点保留。所有位于超奇异标号 $j$ 之上的水平支链均在特殊纤维上常值映到该 $j$。收缩 $\pi$ 在去掉异常集后是同构，故忘却 $j$ 在 $U$ 上仍为态射，且
$$j|_{U_j}=j\quad\text{在特殊纤维上。}\tag{1.3}$$
这里不声称忘却态射延拓过收缩点 $P$；后面的局部点均不经过该点。

最小正则模型的唯一性使 $\mathbb Q_p$ 的未分歧 Galois 作用在上述模型上具有规范下降数据；它与忘却 $j$ 相容。等价地，可从 $\mathbb Z_p$ 上的最小正则模型作未分歧基变换得到该模型。下降可在一个有限未分歧扩张上处理：模型及同构均有限表示，唯一性给 cocycle，相应射影模型及其光滑开集作有效下降。因此几何 Frobenius 对分量的置换，按 (1.3) 及每个超奇异标号唯一一个保留分量，恰为
$$C_j\longmapsto C_{j^p}.
\tag{1.4}$$
在 $\mathbb F_{p^2}$ 中几何与算术 Frobenius 互为逆，且置换相同；本文只使用这个二阶置换。

## 2. 全部 $\mathbb Q_p$ 点确实位于该光滑开集

### 引理 1

每个 $x\in X(\mathbb Q_p)$ 通过真性延拓到 $\mathscr X$，且其特化属于 $U(\mathbb F_p)$。

**证明。** 延拓由真性给出。R33 从同一个正规交叉模型的实际收缩证明
$$p\in\mathfrak m_P^\rho,\qquad
\rho=\frac{p-\left(\frac{-3}{p}\right)}6>1.
\tag{2.1}$$
若一个 $\mathbb Z_p$ 截面经过 $P$，局部同态把 $\mathfrak m_P$ 送入 $(p)$，则 (2.1) 给 $p\in(p)^\rho$，与 $v_p(p)=1$ 矛盾。相同论证可先在任意有限未分歧扩张上实施，赋值仍为 $1$。由 §1，去掉 $P$ 后全部特殊纤维都光滑，故特化在 $U$。证毕。

这一步使用的是未分歧基底的截面。分歧度较大的扩域点可能经过 $P$，本文没有将它们纳入相同点值结论。

## 3. 可达分量的完全识别

置
$$S_p=\{j\in\mathbb F_p:j\text{ 超奇异}\},\qquad s_p=|S_p|.$$

### 定理 2

R54 的可达分量集合 $I_p$ 恰为 $S_p$。更强地，对每个 $j\in S_p$，
$$U_j\simeq\mathbb A^1_{\mathbb F_p},\qquad
|U_j(\mathbb F_p)|=p,
\tag{3.1}$$
并且 $U(\mathbb Z_p)\to U(\mathbb F_p)$ 为满射。因而
$$|U(\mathbb F_p)|=p\,s_p,$$
且 $X(\mathbb Q_p)$ 由这 $p\,s_p$ 个光滑剩余圆盘覆盖。

**证明。** 若 $x\in X(\mathbb Q_p)$ 特化到 $U_j$，引理 1 说明特化点在 $U(\mathbb F_p)$。光滑点属于唯一的几何不可约分量；Frobenius 固定该点，必固定其分量。由 (1.4)，$j^p=j$，所以 $j\in S_p$。

反过来取 $j\in S_p$。则 $C_j$ 及其正规化 $\widetilde C_j$ 下降到 $\mathbb F_p$。由 (1.1)，$\widetilde C_j$ 几何上是 $\mathbb P^1$，且边界 $\widetilde C_j\setminus U_j$ 只有一个几何点。这唯一点被 Frobenius 固定，故为一个 $\mathbb F_p$ 有理点。一个光滑射影几何亏格零曲线若有一个有理点，则由该点的一阶极点 Riemann–Roch 系统同构于 $\mathbb P^1$。因此
$$U_j=\widetilde C_j\setminus\{\text{一个 }\mathbb F_p\text{ 点}\}
\simeq\mathbb A^1_{\mathbb F_p}.$$
这证明 (3.1)，并完全包含 $j=0,1728$ 的额外自同构情形，因为这两种支链已在 §1 按 Theorem 3.4 的真实模型处理。

$U/\mathbb Z_p$ 光滑，故每个 $\mathbb F_p$ 点都由 Hensel 引理提升为 $\mathbb Z_p$ 点，其泛纤维给 $X(\mathbb Q_p)$ 点。所以每个 $j\in S_p$ 均可达。各几何 $U_j$ 互不相交，非 Frobenius 稳定的分量没有 $\mathbb F_p$ 点，计数随即得到。证毕。

这个充分性证明直接在确切正则模型上提升，不需要先猜测某个椭圆曲线提升会落在哪条例外分量，也不把稳定约化的尾分量当作 $\mathbb Z_p$ 光滑分量。

## 4. 有效的类数计数与有限靶数

以 $h(D)$ 表示判别式 $D<0$ 的虚二次序类数。对 $p>37$，已发表的经典计数为
$$\boxed{\quad
s_p=
\begin{cases}
\frac12h(-4p),&p\equiv1\pmod4,\\
2h(-p),&p\equiv3\pmod8,\\
h(-p),&p\equiv7\pmod8.
\end{cases}\quad}\tag{4.1}$$

为明确其原始输入，可直接用 Treneer (2017), equation (3.2) 和 Theorem 3.2：若 $H_D$ 是相应 Hilbert 类多项式，$S_p^{\rm lin}(X)$ 是素域超奇异不变量的平方自由乘积，则
$$\begin{cases}
H_{-4p}(X),&p\equiv1\pmod4,\\
H_{-p}(X)H_{-4p}(X),&p\equiv3\pmod4
\end{cases}
\equiv S_p^{\rm lin}(X)^2\pmod p.
\tag{4.2}$$
比较次数得到
$$2s_p=h(-4p)\quad\text{或}\quad2s_p=h(-p)+h(-4p).$$
第二种情形中，序 $\mathbb Z[\sqrt{-p}]$ 在最大整环中的导子为 $2$。其类群到最大序类群的核大小为 $(\mathcal O_K/2)^\times$ 的大小，因为 $(\mathbb Z/2)^\times$ 平凡且两序的单位均为 $\{\pm1\}$。当 $p\equiv3\pmod8$，$2$ 惰性，该大小为 $3$；当 $p\equiv7\pmod8$，$2$ 分裂，该大小为 $1$。这给 (4.1)。本次使用的是该已发表多项式恒等式与完整的次数、导子推导，而非搜索摘要中的类数公式。

还可给一个直接有效上界。对负基本判别式 $D<-4$，Dirichlet 类数公式为
$$h(D)=\frac{\sqrt{|D|}}\pi L(1,\chi_D).$$
设 $N=|D|$。在完整模周期上 $\sum_{n=1}^N\chi_D(n)=0$；由 Abel 求和，$N$ 以后的调和尾和绝对值至多 $1$，而前段至多 $1+\log N$。因此
$$0<L(1,\chi_D)\le\log N+2.$$
代入 (4.1)，得到
$$s_p\le
\begin{cases}
\dfrac{\sqrt p}\pi(\log(4p)+2),&p\equiv1\pmod4,\\[3pt]
\dfrac{2\sqrt p}\pi(\log p+2),&p\equiv3\pmod8,\\[3pt]
\dfrac{\sqrt p}\pi(\log p+2),&p\equiv7\pmod8.
\end{cases}\tag{4.3}$$
特别地 $s_p=O(\sqrt p\log p)$，这里的上界常数有效，不借 Siegel 型无效下界。

由定理 2，R54 的有限谱靶集准确地取自
$$\mathcal B_p=\{\beta_j:j\in S_p\},\qquad
|\mathcal B_p|\le s_p.
\tag{4.4}$$
不同分量的 $\beta_j$ 可以重合，所以不把向量个数断言为恰等于 $s_p$。但是每个分量都被真实 $\mathbb Q_p$ 点实现；不能再仅以“这个分量不可达”删掉其中任何一个分量标签。

## 5. 从全部几何分量积分核扩大到真实局部点值核

沿用 R54 的整个容许整数格 $\Lambda_A$，其秩为 $a-1$。由 (4.1) 知 $S_p$ 非空，固定 $j_0\in S_p$，按 R54 在此分量归一化截面，记
$$b_j(F)=k_j(F)-k_{j_0}(F).$$
定义
$$\mathcal K_{p,\mathbb Q_p}
=\{F\in\Lambda_A:b_j(F)=0\text{ 对全部 }j\in S_p\}.
\tag{5.1}$$

### 定理 3：更大的真实 QC 方向格

有
$$\boxed{\quad
\mathcal K_A\subseteq\mathcal K_{p,\mathbb Q_p},\qquad
\operatorname{rank}\mathcal K_{p,\mathbb Q_p}\ge a-s_p.
\quad}\tag{5.2}$$
对每个 $F$ 属于此格，令 $G=2F$，并使用 R54 的同一归一化，则全部非辅助局部高度在全部相应局部点上为零；因此全部有理点满足 R47 形式的真实必要方程
$$\sum_f\operatorname{Tr}\bigl(c_fz_f(x)(G_fz_f(x)-\xi_{G,f})\bigr)
-H_{D,G,\ell}(x)=0.
\tag{5.3}$$
可取至少 $a-s_p$ 个独立真实方程，且它们在每个辅助圆盘上仍具有 R49 的 $\mathbb Q_\ell$ 代数独立性。

**证明。** (5.1) 是到 $\mathbb Z^{s_p-1}$ 的整数线性映射之核，所以秩至少为 $(a-1)-(s_p-1)=a-s_p$。若方向在原 $\mathcal K_A$ 中，其所有几何分量阶都相同，当然满足 (5.1)。

对坏 $p$ 处任一实际局部点，定理 2 说明它位于某个 $j\in S_p$；R54 的真实局部式给
$$\lambda_p(\widetilde s_{2F}(x_p))=-b_j(F)\log_\ell(p)=0.$$
好素数处的归一化与 R47–R54 相同，因此其余非辅助项也为零。全局 Poincaré 高度恒等式给 (5.3)。

R45 为整个 $\Lambda_A$ 已保证对应和平移消去互补商，故全局高度仍能通过 Heegner 商对数同构计算。R49 的 NS 曲率与局部高度独立性论证不要求在所有几何分量上积分平凡化；对本格独立方向直接适用。证毕。

此格中某些方向可在 $j\notin\mathbb F_p$ 的几何分量上有非零垂直阶，它们的线丛未必在整个 $U$ 平凡。这不会影响 (5.3)：这些几何分量没有 $\mathbb Q_p$ 点，而全局高度恒等式只用实际局部点处的值。

## 6. 谱缺陷中的加强，以及 Galois 不变的原积分核

固定 $j_0\in S_p$ 后，R54 的 $\beta_{j_0}=0$。置
$$C_{p,\mathbb Q_p}=\operatorname{span}_{\mathbb Q}\{\beta_j:j\in S_p\}\subseteq C.$$
由迹配对和 (5.1)，
$$C_{p,\mathbb Q_p}=(\mathcal K_{p,\mathbb Q_p}\otimes\mathbb Q)^\perp,
\qquad\dim C_{p,\mathbb Q_p}\le s_p-1.$$
所以新增的真实方程给以下集合包含链（不声称每一步都是严格包含）
$$\begin{aligned}
X(\mathbb Q)
&\subseteq\Delta_\ell^{-1}(-\log_\ell(p)\mathcal B_p)\\
&\subseteq\Delta_\ell^{-1}(C_{p,\mathbb Q_p}\otimes\mathbb Q_\ell)\\
&\subseteq\Delta_\ell^{-1}(C\otimes\mathbb Q_\ell).
\end{aligned}\tag{6.1}$$
在新的零高度核之外，只需补上
$$\dim C_{p,\mathbb Q_p}\le s_p-1=O(\sqrt p\log p)$$
个方向，就能按 R54 §5 的联合分支方式恢复完整有限靶集条件。

还有一个独立的下降改善。因为实际截面定义于 $\mathbb Q$，其垂直阶满足
$$k_{j^p}(F)=k_j(F).$$
所有超奇异不变量位于 $\mathbb F_{p^2}$，故几何分量的 Frobenius 轨道数为
$$t_p=\frac{n+s_p}{2}.$$
原始 $\Phi_A$ 的像已落在轨道常值向量模常数中，因此
$$\operatorname{rank}\Phi_A\le t_p-1,\qquad
\operatorname{rank}\mathcal K_A\ge a-t_p.
\tag{6.2}$$
(6.2) 控制全部几何分量的积分平凡化；(5.2) 则直接使用 $\mathbb Q_p$ 可达分量，给更强的真实点值方程数。

## 7. 对排根的实际作用与边界

R54 中的可达分量参数已经从未知子集 $I_p$ 精确识别为 $S_p$，特殊自同构、共同交点和原正规交叉模型的多重分量均已包含。由此把零坏高度方向的余维从 $O(p)$ 降到 $O(\sqrt p\log p)$，且无需统一整数指数或单位 jet 假设。

每个坏分量标签都有真实 $\mathbb Q_p$ 点，并不意味着每个谱靶值都在辅助素数 $\ell$ 处被某个共同根实现，更不意味着存在有理点。要完成 O5，仍须证明实际 $\Delta_\ell$ 的有限靶逆像及其他全局条件不支持非 CM 有理点。本文没有用局部满可达性替代这一跨素数的全局问题。

## 8. 已核验的原始来源

- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058，DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)，[原刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.4，pp.1038–1039：确切未分歧基底上正规交叉模型，含 $j=0,1728$；其证明 pp.1040–1042 给例外分量；Corollary 3.2，p.1042，及证明与 Figure 7，pp.1043–1044：收缩后约化最小正则模型。引言 pp.1017–1018 区分这些新增约化片段与分歧稳定模型的原 Drinfeld 分量。
- S. Treneer, **Weierstrass points on $X_0^+(p)$ and supersingular $j$-invariants**, *Research in the Mathematical Sciences* **4**, article 25 (2017)，DOI [10.1186/s40687-017-0115-z](https://doi.org/10.1186/s40687-017-0115-z)，[原刊全文](https://link.springer.com/article/10.1186/s40687-017-0115-z)。§3，equation (3.2)、Proposition 3.1、Theorem 3.2 及完整证明，给 (4.2) 和由次数得到的准确计数。
- D. Burde, **Algebraic Number Theory**, [作者讲义](https://homepage.univie.ac.at/Dietrich.Burde/papers/burde_71_ant.pdf)，§5.2，Corollary 5.2.5，供经典 Dirichlet 类数公式的归一化核对；本文的调和尾和上界已自行证明。
- 仓库 [R28](R28-bad-reduction-norm-interface.md)、[R33](R33-hecke-norm-and-component-data.md)、[R43](R43-neron-height-from-integral-correction.md) 给同一模型的收缩重数、实际垂直截面和局部 splitting；[R45](R45-heegner-quotient-integral-directions.md)、[R47](R47-heegner-logarithms-global-height.md)、[R49](R49-independent-qc-functions-and-saturated-degree.md)、[R54](R54-hecke-spectral-defect-and-finite-target.md) 给容许方向、完整高度、独立性与有限谱靶。

本次新推导是从确切正则模型证明可达分量的等价性、$\mathbb A^1$ 下降与 Hensel 满可达，再把它应用到真正的 QC 点值核。类数计数本身是经典已知事实，不作新颖性声称。
