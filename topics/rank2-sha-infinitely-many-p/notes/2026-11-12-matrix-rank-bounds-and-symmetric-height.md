# 矩阵秩下界对固定 CM 高度矩阵的实际范围

**可信度：文献范围核查；第 2、4、5 节的代数计算已证明。**
日期：2026-11-12。本文不把结构秩猜想当成输入。

## 1. 对象和问题

沿用 [R39](../results/R39-cm-height-linear-period-matrix.md) 的
$$
E:y^2=x^3-17x,\qquad P=(-1,4),\quad Q=(9,24),
$$
以及
$$
\mathfrak m=(O)+(P)+(Q)+([i]P)+([i]Q),\qquad
0\longrightarrow\mathbb G_m^4\longrightarrow
J=J_{\mathfrak m}\longrightarrow E\longrightarrow0.
\tag{1.1}
$$
$J$ 的维数为 $5$，没有非零连通 affine 商。
两个代数点 $b'_P,b'_Q$ 的投影为 $P,Q$，
其在 $J^2$ 中的联合群包为全群。
目标素数和局部对数分支均与 R37–R39 相同。
非紧时先使用 R37 §3.1 的代数 torus 修正；这不改变下列对数秩。

为避免 R39 式 (3) 的因子 $1/2$，在本文记
$$
N=2M_p=
\begin{pmatrix}a&b-ic\\b+ic&d\end{pmatrix},
\qquad
H=\begin{pmatrix}a&b\\b&d\end{pmatrix},
\tag{1.2}
$$
其中 $a=H_{PP}$、$b=H_{PQ}$、$d=H_{QQ}$、$c=j$。
R39 已证 $a,b,d,c$ 在 $\overline{\mathbb Q}$ 上线性独立，
R37 已证 $c\ne0$。
本文核查已发表的矩阵秩定理能否进一步推出
$$
\det H=ad-b^2\ne0.
\tag{1.3}
$$

## 2. 两个行列式必须分开

直接计算给
$$
\boxed{\det N=\det H-c^2.}
\tag{2.1}
$$
因此，若目标中的坏情形 $\det H=0$ 发生，
R37 的 $c\ne0$ 反而推出
$$
\det N=-c^2\ne0.
\tag{2.2}
$$
所以即使某个矩阵秩定理能证明 R39 的两行矩阵满秩，
该结论本身仍不排除 (1.3) 失败。
完整五行对数矩阵满列秩也不控制指定的对称化二阶 minor。

这个区别不是只由“线性独立弱于代数独立”一句话造成。
例如，在纯形式域 $\overline{\mathbb Q}(X,Y,Z)$ 中取
$$
a=X,\qquad b=XY,\qquad d=XY^2,\qquad c=Z.
\tag{2.3}
$$
四个数线性独立，$c\ne0$，$N$ 的四个条目也线性独立，
而 $\det H=0$、$\det N=-Z^2$。
这是检查逻辑蕴含的代数例子，不是实际椭圆曲线或实际 period 的反例。

### 2.1 对称化不是对原两列施加同一个代数行投影

令
$$
u=\log_J b'_P,\quad v=\log_J b'_Q,\quad
\theta_1=2\vartheta_P,\quad\theta_2=2\vartheta_Q.
$$
于是 $N_{ij}=\theta_i(u_j)$，其中 $u_1=u,u_2=v$。

假设存在一个代数 Lie 线性形式 $\psi_1$，使
$$
\psi_1(u)=a,\qquad\psi_1(v)=b.
\tag{2.4}
$$
由于单点 $b'_P$ 的群包为 $J$，AST 及第一式迫使
$\psi_1=\theta_1$。
第二式便要求 $\theta_1(v)=b$；
但真实值为 $b-ic$，与 $c\ne0$ 矛盾。

因此不能把 $H$ 直接视为原来两个代数列点经过另一个共同的代数行投影。
在更大的直积群中重新实现对称化，需要重新记录群包、重复列和独立秩，
不能无代价沿用原两列的群数据。

## 3. 通常的 Waldschmidt–Masser 定理：严格门槛为 1

Samit Dasgupta，
*Ranks of matrices of logarithms of algebraic numbers I:
the theorems of Baker and Waldschmidt–Masser*，
Essential Number Theory **2** (2023)，
[原文](https://arxiv.org/pdf/2303.02037)，Theorem 5.1，
给出了 $p$-adic 版本及证明。
其输入是
$$
A\in M_{m\times n}(\mathscr L_p),\qquad
\mathscr L_p=\{\log_p\alpha:\alpha\in\overline{\mathbb Q}^{\times}\}.
$$
若
$$
\operatorname{rank}A<\frac{mn}{m+n},
\tag{3.1}
$$
则经有理可逆行、列变换后出现一个 $m'\times n'$ 的零块，满足
$m'/m+n'/n>1$。

这里有两项独立的适用条件：

- 当 $m=n=2$ 时，右端恰为 $1$；一个奇异但非零的秩 $1$ 矩阵不满足严格不等式。
- R39 的第三类积分是非分裂半阿贝尔群的对数坐标。
  没有证明它们是普通代数数的乘法对数，不能直接套用上述 toric 定理。

形式上将矩阵扩大成 $5\times2$ 会把门槛改为 $10/7$，
但不能消除第二项；即使另行获得满列秩，也仍有第 2 节的 minor 障碍。
同样，不能把额外加入的代数 torus 点当成原来两列已经具有的独立信息。

## 4. 确实适用于一般代数群的 p-adic 下界

Michel Waldschmidt，
*Sous-groupes analytiques de groupes algébriques*，
Annals of Mathematics **117** (1983), 627–657，
[作者原文](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AnnMaths117-1983.pdf)。
所需位置为 §3(a)（印页 642；同一商秩记号亦见印页 646）
和 §6(a)、式 (6.1)（印页 652–653）。

若 $\Gamma\subset G(F)$ 有限生成，并在局部域 $F_v$ 上由紧子群
包含一个有限指数子群，定义
$$
\mu(\Gamma,G)=
\min_{\substack{H\subset G\text{ 代数子群}\\\dim H<\dim G}}
\frac{\operatorname{rank}_{\mathbb Z}(\Gamma/(\Gamma\cap H))}
{\dim(G/H)}.
\tag{4.1}
$$
记 $r_v$ 为其局部对数张成空间的维数、$d=\dim G$，并置
$$
\rho(G)=
\begin{cases}1,&G\text{ affine},\\2,&G\text{ 非 affine}.\end{cases}
$$
原文 §6(a) 明确说明，有限位同样满足
$$
r_v(\Gamma,G)\ge\frac{d\,\mu(\Gamma,G)}{\mu(\Gamma,G)+\rho(G)}.
\tag{4.2}
$$
这里的两个参数不能因 torus 核的存在而把 $\rho(J)$ 改成 $1$。

**在当前对象中的精确代入。**
先说明标量域，避免把代数根扩域后的群误当成五维的
$\mathbb Q_p$ 群。R39 的原始除子提升 $b_P,b_Q$ 均在 $J(K)$，
修正 torus 坐标为
$u_{U,V,p}=\prod_{\mathfrak q}\alpha_{\mathfrak q}^{r_{U,V,\mathfrak q}}$，
其中 $\alpha_{\mathfrak q}\in K^\times$、$r_{U,V,\mathfrak q}\in\mathbb Q$。
取正整数 $N$ 清除这些有理数的分母，则
$$
N b'_V=N b_V+
\left(\prod_{\mathfrak q}
\alpha_{\mathfrak q}^{N r_{U,V,\mathfrak q}}\right)_U
\in J(K).
\tag{4.3a}
$$
选代数根产生的挠点可再用一个整数消去。
在固定有限素数集外，这个 $N$ 也可以一次固定。
共同乘 $N$ 不改变任何所讨论的对数张成维数。

由于 $p$ 在 $K$ 分裂，$K_{\mathfrak p}=\mathbb Q_p$。
若上述点仍不紧，取 $J(\mathbb Q_p)$ 的紧开子群，
再共同乘一个整数，使两点在 $E(\mathbb Q_p)$ 中的像落入其投影。
相差的 torus 元素的坐标赋值都是整数，故 R37 §3.1 的修正
可使用 $\pi$ 的**整数**次幂，仍留在 $J(K)$；
所用分支满足 $\log(\pi)=0$，所以修正前后只差共同整数倍。
这样可在 $F=K$、$F_v=K_{\mathfrak p}=\mathbb Q_p$ 上直接应用 (4.2)，
无需引入 Weil restriction 或把扩域上的维数误算为 $5$。

现在取 $\Gamma$ 为这两个修正后的点生成的秩 $2$ 子群，
其投影是 $P,Q$ 的共同非零整数倍。
若一个真连通子群 $H\subset J$ 满射到 $E$，
则 $J/H$ 被 torus 核满射，因而是 affine 商。
由 R39 的无 affine 商性质只能有 $H=J$，矛盾。
所以每个真连通子群均包含在 torus 核内。
对非连通 $H$，其像至多是 $E$ 中的有限群。
由于 $P,Q$ 独立，$\Gamma\cap H$ 的秩为零。
因此所有 (4.1) 的分子为 $2$，分母最大为 $5$，且 $H=0$ 取到：
$$
\mu(\Gamma,J)=\frac25.
\tag{4.3b}
$$
局部紧性修正只将 $P,Q$ 同时替换为一个非零整数倍，
保留这个计算。于是
$$
\boxed{r_v(\Gamma,J)\ge
\frac{5(2/5)}{2/5+2}=\frac56.}
\tag{4.4}
$$
整数化以后只得到 $r_v\ge1$。
特别是这个已证明的一般群定理不强迫原两列的局部对数独立。

也可直接核原文 Theorem 1.1 的数值：
秩 $m=2$、群维 $d=5$、假设解析张成维数 $n=1$ 时，
要求的 $md>n(m+2d)$ 变成 $10>12$，并不成立。

## 5. CM 改良参数不能从 E 直接搬到 J

Damien Roy–Michel Waldschmidt，
*Autour du théorème du sous-groupe algébrique*，
Canadian Mathematical Bulletin **36** (1993), 358–367，
[原文](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/CanadianMathBull36-1993-358--367.pdf)，
§1，印页 359–361。
该论文的陈述使用复 Lie 群；本节只计算其代数参数，
不未经来源证明便把全部复结论替换为 $p$-adic 结论。

定义 $d_0(G),d_1(G)$ 为最大加法、乘法群**商**的维数，
$$
\alpha(G)=2\dim G-2d_0(G)-d_1(G).
\tag{5.1}
$$
$J$ 没有非零 affine 商，所以
$$
\alpha(J)=10.
\tag{5.2}
$$
不能用 torus 核维数 $4$ 代替 $d_1(J)=0$。

更强的是，对该文定义的任意数域 $F$，都有
$$
\boxed{\alpha_F(J)=10.}
\tag{5.3}
$$

**证明。** 令 $n=[F:\mathbb Q]$，取基 $\beta_1,\ldots,\beta_n$。
按该文定义，令
$$
b:\operatorname{Lie}(J^n)\longrightarrow\operatorname{Lie}J,\qquad
b(z_1,\ldots,z_n)=\sum_{j=1}^n\beta_jz_j,
$$
并令 $A$ 是满足 $\operatorname{Lie}A\subset\ker b$ 的最大连通代数子群。
则 $\alpha_F(J)=\alpha(J^n/A)/n$。

先证 $J^n$ 没有非零阿贝尔子簇。
若存在 $B\subset J^n$，它到 $E^n$ 的投影不可能为零，
因为从阿贝尔簇到 torus 的同态为零。
选择一个非零分量 $f:B\to E$，它满射到 $E$。
由 $B\to J$ 的对应分量，扩张 (1.1) 沿 $f$ 拉回后具有一个截面。
特别地，将 torus 按对应 $P$ 的特征推出，所得线丛
$f^\vee(P)\in B^\vee$ 必须为零。
但满射 $f$ 的对偶 $f^\vee:E^\vee\to B^\vee$ 的核有限，
不可能杀掉非挠点 $P$，矛盾。

再证 $A$ 没有非零 torus。
若有一个非零 cocharacter $\mathbb G_m\to A\to J^n$，
其像位于 $\mathbb G_m^{4n}$。
在整数 cocharacter 基中，它由整数向量 $m_{j,k}$ 给出。
切空间落在 $\ker b$ 意味着对每个 $1\le k\le4$，
$$
\sum_{j=1}^n\beta_jm_{j,k}=0.
$$
$\beta_j$ 的 $\mathbb Q$-独立性迫使全部 $m_{j,k}=0$，矛盾。
半阿贝尔子群若没有 torus 就是阿贝尔簇，
故结合上一段可得 $A=0$。
因此 $\alpha_F(J)=\alpha(J^n)/n=10$。证毕。

原文给出的 $\alpha_F(E)=1$（当 $F$ 包含 CM 域）确实是一个
真正改良，但 (5.3) 表明它不自动传递到当前非分裂广义 Jacobian。
这个结论不声称 $J$ 没有非平凡 endomorphism；
它只计算此处实际出现的参数。

## 6. 新近“refined logarithm”结果的准确范围

A. Burungale–C. Skinner–X. Wan，
*A refined non-vanishing of the p-adic logarithm of a rational point
on an abelian variety*，
[arXiv:2603.20886v2](https://arxiv.org/pdf/2603.20886)，2026。

Theorem 1.1 对所述 GL2 型情形证明单点的特征微分对数非零。
但涉及多个独立点、期望局部闭包维数的 Theorem 1.2
明确假设 Structural Rank Conjecture 5.2；
§5.1–§5.2 将 AST 给出的线性关系控制和实际矩阵秩分开。
因此该文不能作为无条件的 rank-two 高度行列式非零输入。
此外它讨论的对象是阿贝尔簇，不能省略 (1.1) 的非分裂 torus 扩张。

## 7. 本次核查留下的具体输入

R39 的实际进展是把目标高度条目化成固定有限对象的线性 period。
上述已证矩阵秩定理仍没有给出这些 period 的特定二次关系
$ad-b^2$ 非零。要沿这一接口继续，至少还须获得以下一种实质输入：

- 直接排除这个对称二次关系的已证 period 定理；
- 将这个**特定**二次式再次改写成一个代数群上的非零代数线性 period，
  并完整核对实际代数点和群包；
- 一个真正控制相应 Selmer 余核的算术输入，而非只证明非对称矩阵满秩。

第 2 节并不排除第二种办法；R37 已展示互易式可以线性化某些特定二次式。
这里记录的是当前通用矩阵秩下界的精确数值和缺失条件，
不是对所有可能的高度非零证明作不可能性断言。
