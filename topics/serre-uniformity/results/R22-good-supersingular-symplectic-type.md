# R22：好超奇异的表示素数处辛类型，以及固定 CM 三族的相容条件

日期：2026-11-12；会话：serre-uniformity-astra-cont。

**状态：已证明的局部定理及全局必要条件；中间进展。** 下文完整证明表示素数 $p$ 处的辛类型公式，再与 $2$ 处已发表的判据比较。与 R13 的分母限制和 R25 的精确 $2$ 进惯性域条件合并后，三个族的全部配对符号均自动相容。因此局部定理本身独立成立，但这次全局比较未排除额外指数。

## 1. 局部命题

设 $p>3$、$p\equiv3\pmod4$，$E_1,E_2/\mathbb Q_p$ 有好超奇异约化，并有实际 $G_{\mathbb Q_p}$-同构 $\phi:E_1[p]\to E_2[p]$。记 $d(\phi)\in\mathbb F_p^\times$ 为 Weil 配对乘数，$\Delta_1,\Delta_2\in\mathbb Z_p^\times$ 为好约化模型的判别式。则
$$
\left(\frac{d(\phi)}p\right)=
\begin{cases}
1,&p\equiv7\pmod8,\\
\left(\dfrac{\Delta_1\Delta_2}p\right),&p\equiv3\pmod8.
\end{cases}\tag{S1}
$$
改变好模型只乘判别式以单位的十二次幂，不改变该符号。命题只在同构已存在时判断类型，不以此推导任意两条曲线必有挠点同构。

### 1.1 有限平坦延拓与特殊纤维的自同构

绝对分歧指数 $1<p-1$，所以 Raynaud 全忠实性将 $\phi$ 及其逆唯一延拓为 $\mathbb Z_p$ 上有限平坦群概形同构。Weil 配对也延拓；泛纤维上的乘数等式在整个模型上成立，因为有限平坦源的泛纤维概形稠密。于是特殊纤维上的群概形同构具有同一乘数。

设 $B/\mathbb F_p$ 超奇异。因 $p>3$，其 Frobenius 迹为零；Frobenius $\pi$ 满足 $\pi^2=-p$。令 $G=B[p]$。$\pi|_G$ 非零，因为 $\ker\pi$ 的阶为 $p$，小于 $G$ 的阶 $p^2$；而 $(\pi|_G)^2=0$。

Dieudonné 理论将 $G$ 对应到一个二维 $\mathbb F_p$ 向量空间 $M$，且该函子全忠实。$D(\pi)$ 是非零、平方为零的线性算子，所以秩为一。对任一在 $\mathbb F_p$ 上定义的群概形自同构 $\alpha:G\to G$，Frobenius 的自然性给 $\alpha\pi=\pi\alpha$，故 $D(\alpha)$ 落在这个幂零 Jordan 块的中心化子中：
$$D(\alpha)=aI+bD(\pi),\qquad a,b\in\mathbb F_p,\quad a\ne0.$$
取 $a,b$ 的整数提升，全忠实性给出
$$\alpha=[a]+[b]\pi\quad\text{在 }G\text{ 上}. \tag{S1a}$$
因此该自同构由 $B$ 上的实际同态 $a+b\pi$ 诱导。其对偶为 $a-b\pi$，次数为
$$\deg(a+b\pi)=a^2+p b^2.$$
同源对 Weil 配对的乘数是次数，故 $\alpha$ 的乘数模 $p$ 为 $a^2$。由此，**每个定义于 $\mathbb F_p$ 的 $B[p]$ 自同构的配对乘数都是平方**。这个论证不需要在协变、反变 Dieudonné 配对的约定之间作选择。

这里必须使用定义域 $\mathbb F_p$：$D(\pi)$ 在该域上是线性算子。扩到 $\overline{\mathbb F}_p$ 后，不能用同一个二维线性中心化子计算全部自同构。

### 1.2 用有限域同源度数计算该平方类

两条特殊纤维均有 Frobenius 多项式 $T^2+p$，由 Tate 有限域同源定理在 $\mathbb F_p$ 上同源。去掉同源的纯不可分 Frobenius 因子，可取一个次数 $m$ 不被 $p$ 整除的 $\mathbb F_p$-同源 $\psi:\widetilde E_1\to\widetilde E_2$：超奇异曲线没有非平凡几何 $p$ 挠点，故可分同源次数不含 $p$；而曲线定义于 $\mathbb F_p$，各次 Frobenius 扭曲仍是同一曲线。

$\psi[p]$ 是有限平坦群概形同构，Weil 配对乘数为 $m$。它与 $\widetilde\phi$ 相差一个定义于 $\mathbb F_p$ 的 $p$ 挠点群概形自同构，故
$$\left(\frac{d(\phi)}p\right)=\left(\frac mp\right).\tag{S2}$$
无需把 $\psi$ 提升成特征零椭圆曲线之间的同源。

## 2. 任何奇素数度步骤的次数都是模 $p$ 平方

把上述同源分解成定义于 $\mathbb F_p$ 的素数度循环同源和乘法同源 $[\ell]$。具体做法：若核的 $\ell$ 挠点含有 Frobenius 稳定直线，就先除去该阶 $\ell$ 子群；若不含稳定直线，它作为二维 $E[\ell]$ 的非零子空间只能是全部 $E[\ell]$，就先除去 $[\ell]$ 的核。迭代后次数严格减小，得到所需分解。

每个中间曲线仍有迹零。若循环步骤次数为奇素数 $\ell\ne p$，则 $T^2+p$ 在 $\mathbb F_\ell$ 有根，故
$$\left(\frac{-p}{\ell}\right)=1.$$
因为 $p\equiv3\pmod4$，二次互反律给 $(-p/\ell)=(\ell/p)$，所以该步骤次数为模 $p$ 平方。乘法同源的次数 $\ell^2$ 也是平方。因此
$$\left(\frac mp\right)=\left(\frac2p\right)^{v_2(m)}.\tag{S3}$$
若 $p\equiv7\pmod8$，右端立即为 $1$。

## 3. p≡3 mod8 时，每个有理 2-同源交换两种 2-挠点型

以下设 $p\equiv3\pmod8$。迹零曲线的 $\mathbb F_p$ 点数为 $p+1\equiv4\pmod8$，所以其有理 $2$ 挠点维数是 $1$ 或 $2$，不会为零。

令 $L=T_2(B)$，算术 Frobenius $\pi$ 满足 $\pi^2=-pI$、$\operatorname{tr}\pi=0$。一个有理 $2$-同源对应一个 $\pi$ 稳定的指数 $2$ 超格子 $L'\supset L$；其模 $2$ Frobenius 是否为恒等，决定目标曲线是否有全有理 $2$ 挠点。

若源曲线有全有理 $2$ 挠点，则 $\pi=I+2M$。代入关系得
$$M^2+M=-\frac{p+1}4 I\equiv I\pmod2.$$
因此 $M\bmod2$ 满足不可约多项式 $T^2+T+1$，没有不变直线。写 $L'=\mathbb Z_2(v/2)+\mathbb Z_2 w$。若 $M$ 在基 $(v,w)$ 中为 $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，则 $\pi$ 在 $(v/2,w)$ 中为
$$\begin{pmatrix}1+2a&4b\\c&1+2d\end{pmatrix}.$$
它模 $2$ 为恒等当且仅当 $c$ 为偶数，即 $M$ 保持 $v$ 所张的模 $2$ 直线；这不可能。因此目标曲线只有一维有理 $2$ 挠点。

若源曲线只有一维有理 $2$ 挠点，则 $\pi\bmod2$ 为非平凡幺幂矩阵，唯一稳定直线给出唯一有理 $2$-同源。选基使
$$\pi=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad a,b\text{ 奇},\ c\text{ 偶}.$$
由 $\det\pi=p$，有 $bc=-p-a^2\equiv4\pmod8$，所以 $4\mid c$。在对应超格子基 $(v/2,w)$ 中，矩阵为
$$\begin{pmatrix}a&2b\\c/2&-a\end{pmatrix}\equiv I\pmod2.$$
因此目标有全有理 $2$ 挠点。两方向的交换均已证明。

奇数度同源在 $2$ 挠点上是同构；乘法同源 $[2]$ 次数为 $4$，也不改变曲线型。因此 $v_2(m)$ 的奇偶性恰好记录两个端点是否有不同的有理 $2$ 挠点型。

对 $p>3$ 的短 Weierstrass 模型，三次多项式的判别式与椭圆曲线判别式相差平方 $16$。迹零保证三次多项式至少有一个有理根。其 Frobenius 置换只有恒等和对换两种可能；前者对应全有理 $2$ 挠点、判别式为平方，后者对应唯一有理 $2$ 挠点、判别式为非平方。因此
$$(-1)^{v_2(m)}=\left(\frac{\Delta_1\Delta_2}p\right).$$
结合 (S2)、(S3) 得 (S1)。

## 4. 与 2 处辛类型相容后的必要条件

回到 R16/R19 的实际同余 $E[p]\simeq A[p]$，$A:y^2=x^3-x$。其 $p$ 处都是好超奇异；$\Delta_A=64$ 为平方。设 $p\equiv3\pmod8$。

在 $2$ 处，$A$ 的惯性群为 $Q_8$。可用其有理 $2$-同源曲线
$$B:y^2=x^3-6x^2+x$$
验证：它的极小不变量是 $(c_4,c_6,\Delta)=(528,12096,512)$，属于 Freitas–Kraus v5 Table 5 的 Dd 行，半稳定缺陷为 $8$。有理 $2$-同源在任意奇 $p$ 挠点上是同构，故 $A$ 与 $B$ 的惯性核相同。

E 与 A 的全局同余保证它们在 $2$ 有同一惯性核。Freitas–Kraus v5 Theorems 8–9、Table 3 给出在 $(2/p)=-1$ 时的配对类型。以 A 的类型为基准（也可通过与 B 比较再乘以 $2$ 的平方类），得到：

| 极小类型 / R19 族 | $2$ 处辛类型 | $p$ 处类型 | 必要条件 |
|---|---|---|---|
| III，$\delta=6$ | $+1$ | $(Z/p)$ | $(Z/p)=1$ |
| $I_0^*$，$\delta=9$ | $-1$ | $-(Z/p)$ | $(Z/p)=1$ |
| $I_3^*$，$\delta=12$、$X$ 奇 | $-1$ | $(Z/p)$ | $(Z/p)=-1$ |
| III$^*$，$\delta=12$、$X$ 偶 | $+1$ | $(Z/p)$ | $(Z/p)=1$ |

其中 $\delta=6$ 时 $\widetilde c_4=3X\equiv-1\pmod4$，$I_3^*$ 时 $\widetilde c_4=3X\equiv1\pmod4$，使用 R19 的精确模 $4$ 条件。两个位置比较的是同一个全局 Galois 同构的配对乘数，所以必须相同。

若 $p\equiv7\pmod8$，两处都给辛类型 $+1$，这个比较本身不增加 $Z$ 的限制。它因此不能单独排除所有大 $p$。

### 4.1 与分母、精确惯性域比较：全部符号自动相容

R13 已给出：每个奇素数 $q\mid Z$ 满足 $q\equiv1$ 或 $-1\pmod{4p}$。前者同时有 $q\equiv1\pmod4$，后者有 $q\equiv-1\pmod4$。因此对任意有符号的奇整数 $Z$，如果其全部素因子满足这些条件，则
$$
Z\equiv\chi_{-4}(Z)\pmod{4p},\qquad
\left(\frac Zp\right)=\chi_{-4}(Z),
\tag{S4}
$$
其中第二式使用 $p\equiv3\pmod4$。负号也符合此式：$-1$ 在模 $4$ 和模 $p$ 下都贡献 $-1$。

对族 I，方程模 $4$ 给 $Z\equiv X^3-27W^2\equiv1\pmod4$，故表中的 $(Z/p)=1$ 已包含于 R13、R19。

对族 III，若 $X\equiv3\pmod4$、$W$ 偶，则 $Z\equiv3\pmod4$；若 $X\equiv2\pmod4$、$W$ 奇，则 $Z\equiv1\pmod4$。所以族 III 的两个符号也已包含于既有条件。

族 II 则由本次比较得到
$$
\boxed{p\equiv3\pmod8\quad\Longrightarrow\quad Z\equiv1\pmod4.}
\tag{S5}
$$
然而，R25 使用 Freitas–Kraus Theorems 17–18 的精确惯性域，已对**全部** $p>37$ 得到族 II 的 $Z\equiv1\pmod4$。因此式 (S5) 也没有额外排除力。三个族在 $2,p$ 两处的辛类型完全相容；这里不把这些相容恒等式重复算作新排除。独立成立的是 §1–§3 的好超奇异局部定理。

## 5. 引用与边界

- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. SMF 102 (1974), Corollaire 3.3.6(1)，用于小分歧泛纤维全忠实性。可直接核对 B. Conrad, *Finite Group Schemes over Bases with Low Ramification*, Compositio Math. 119 (1999), 239–320，Lemma 4.1，印刷页 288；[发表原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/30853786BAE52BEDBB47C6A698261059/S0010437X99000767a.pdf/finite-group-schemes-over-bases-with-low-ramification.pdf)，[DOI](https://doi.org/10.1023/A:1001788509055)。严格条件为 $e<p-1$，本文是 $e=1$。
- J. Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Invent. Math. 2 (1966), 134–144；[全文](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf)。只用 §3、Theorem 1(c)（印刷页 139）：同一 Frobenius 多项式的椭圆曲线在有限域上同源。
- Dieudonné 模及 Cartier 对偶的标准理论；可参见 M. Demazure, *Lectures on p-divisible groups*, LNM 302 (1972)；[Andrew Snowden 的有限群概形讲义](https://public.websites.umich.edu/~asnowden/teaching/2013/679/L06.html)。本文实际所需的中心化子、实际同态 $a+b\pi$ 及配对平方类计算已展开。
- N. Freitas, A. Kraus, *On the Symplectic Type of Isomorphisms of the p-Torsion of Elliptic Curves*, Memoirs AMS 277 (2022), no. 1361，DOI [10.1090/memo/1361](https://doi.org/10.1090/memo/1361)；[作者 v5](https://arxiv.org/pdf/1607.01218)，Theorems 8、9 和 Tables 3、5。作者提醒 arXiv 和正式版定理号不同，此处明确用 v5 编号。

### 5.1 后续核对的文献定位

完成上述推导后，核对到 N. Freitas–D. Mocanu, *Local points on twists of $X(p)$ with applications*, [arXiv:2509.04294v4](https://arxiv.org/abs/2509.04294v4)，2026-09-28。其 Proposition 8.1、Proposition 8.5、Lemma 8.12 和 Theorem 8.7 已分别包含有限平坦配对延拓、超奇异特殊纤维自同构只能为辛、$p\equiv7\pmod8$ 时同源次数为平方，以及相应局部反辛点排除。因此本文这些部分不声称为新的文献结论。

本结果仍独立写出了证明：使用已发表的 Raynaud/Conrad 与 Tate 定理、实际同态 $a+b\pi$ 的次数，以及 §3 的 $2$ 进格子计算，不把该新预印本的完整分类当作输入。本文另外明确计算了 $p\equiv3\pmod8$ 时两个给定好超奇异曲线之间的判别式平方类，并与本题的全部分母和二进惯性条件比较。

该预印本的全局 CM Hasse 反例应用在已解决的分裂 Cartan 情形使用无条件排除；其 §10 对非分裂情形明确另列猜想。这不是本题 Serre 一致性的完整证明。本文也没有声称排除仍满足这些必要条件的整数三元组。
