# CM trace、固定 Fermat quotient 与高阶非 Wieferich 素数

日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

**状态：本笔记中的形式群计算及有限原子障碍已证明；没有证明无穷多个 $p$ 的 Sha 有限性。** 接续 [R6](../results/R6-cm-trace-recurrence.md)、[R8](../results/R8-strict-selmer-comparison.md) 及 [有限 jet / $p$-curvature 笔记](2026-11-12-cm-pcurvature-jets.md)。这里只研究能否把跨 $p$ 的非消失问题降到有限个固定数或固定点的 Fermat quotient；不修改已经登记的结论。

## 1. 待替换的标量究竟是什么

固定
$$
E:y^2=x^3-17x,
\qquad P=(-1,4),\quad Q=(9,24),\quad K=\mathbb Q(i).
$$
沿用 R6 的 $f=34(1+i)$、$F=K(E_f)=K(u)$、$v^2=u^3-17u$ 及
$$
a_n=\operatorname{Tr}_{F/K}(vB_n(u)).
$$
CLS 原文的单位数因子须按 CLS II §4 勘误删除；正确公式为
$$
c_p^+(E)=-\frac{2a_{(p-3)/2}}{f^p(p-1)!}.
\tag{1}
$$
对 $p\equiv1\pmod4$、$p\ne17$，分母及 $2$ 都是 $p$-adic 单位。因此 R6 所用的充分条件准确是
$$
a_{(p-3)/2}\notin\mathfrak p^4
\quad\Longleftrightarrow\quad v_p(c_p^+(E))<4.
\tag{2}
$$
以下没有把一个已知非零的局部对数擅自认作式 (1) 的标量。

## 2. 固定点的对数确实有低精度 Fermat quotient 公式

这部分是直接计算，对任意 $E_D:y^2=x^3-Dx$ 成立。取无穷远点的参数 $t=-x/y$，由曲线方程得到
$$
x=\frac{1+\sqrt{1+4Dt^4}}{2t^2},
\qquad
\omega=\frac{dx}{2y}=\frac{dt}{\sqrt{1+4Dt^4}}.
$$
因此正规化形式对数为
$$
\log_E(t)=
\sum_{k\ge0}\frac{(-1)^k\binom{2k}{k}D^k}{4k+1}\,t^{4k+1}
=t-\frac{2D}{5}t^5+\cdots.
\tag{3}
$$
若 $p\ge7$、$p\nmid2D$ 且 $t\in p\mathbb Z_p$，则
$$
\log_E(t)\equiv t\pmod{p^5}.
\tag{4}
$$
证明：除首项外，令 $m=4k+1\ge5$；第 $m$ 项的赋值至少是 $m-v_p(m)\ge5$。级数在 $p\mathbb Z_p$ 收敛，故逐项估计给出式 (4)。

现在取 $D=17$，令 $N_p=\#E(\mathbb F_p)$。由于 $E$ 有有理的非零 $2$-torsion 点，$N_p$ 为偶数。Hasse 界在 $p\ge7$ 给出 $0<N_p<2p$；其中唯一可能的正 $p$ 倍数是奇数 $p$，故
$$
p\nmid N_p.
\tag{5}
$$
对任意 $R\in E(\mathbb Q)$，$[N_p]R$ 属于形式群。定义
$$
\varepsilon_p(R)=\frac{t([N_p]R)}p\in\mathbb Z_p,
\qquad
\ell_p(R)=\log_E(R).
$$
这里全局点上的局部对数通过任一进入形式群的整数倍定义；由于同态性，与整数倍的选择无关。由式 (3)–(5)，
$$
\ell_p(R)\equiv N_p^{-1}t([N_p]R)\pmod{p^5},
\qquad
\frac{\ell_p(R)}p\equiv
\frac{\varepsilon_p(R)}{N_p}\pmod{p^4}.
\tag{6}
$$
特别地，$\varepsilon_p(R)$ 为单位恰好表示 $[N_p]R\in E_1\setminus E_2$，亦即通常的 elliptic non-Wieferich 条件。这里 $E_j$ 指 $t$ 的赋值至少为 $j$ 的形式群过滤。

式 (6) 是固定点的实际公式，但并没有给出
$$
c_p^+(E)/p^2
\stackrel{?}{=}
\text{某个关于 }\varepsilon_p(P),\varepsilon_p(Q)\text{ 的固定表达式}.
\tag{7}
$$
右侧若只含两点的一行局部对数，已知作用只是产生 R8 的 strict 向量
$$
\ell_p(Q)P-\ell_p(P)Q.
$$
得到非零向量不等于给 strict Selmer 群设维数上界。若另引入高度或 derived Heegner 类，需要独立证明比较式及其非零系数，不能以所要证明的 Sha 有限性作为比较式的前提。两个点分别 non-Wieferich，也不会自动排除由它们组成的多项式或行列式相消。

## 3. 一个确实固定的 elliptic trace 函数

令 $\Lambda=\Omega_\infty\mathbb Z[i]$，$P_f=(u,v)$，并为各 $\sigma\in\operatorname{Gal}(F/K)$ 选择满足
$$
P_f^\sigma=(\wp(z_\sigma),\wp'(z_\sigma)/2)
$$
的 $z_\sigma\in\mathbb C/\Lambda$。定义
$$
g(z)=\sum_\sigma\wp(z+z_\sigma,\Lambda).
\tag{8}
$$
这是一个特定的 elliptic function；本笔记**不声称它已经等同于完整 CLS / Katz 测度**。后者还可能含正规化、$p$-depletion 及其他算子。

函数 $g$ 在 $0$ 正则，且 Taylor 系数属于 $K$。这是因为式 (8) 是定义在 $F$ 上的平移有理函数的 trace，而 $\delta x=2y$、$\delta y=3x^2-17$ 定义在 $K$ 上。R6 的导数公式进一步给出
$$
g^{(2n+1)}(0)=2a_n.
\tag{9}
$$
函数 $g$ 必有极点：在任何 $-z_\sigma$ 处，同一平移类的每一项都有首部 $1/(z+z_\sigma)^2$，合计首项系数是正整数重数，不能相消。

事实上它的奇部
$$
g_{\rm odd}(z)=\frac{g(z)-g(-z)}2
$$
也有极点。若 $P_f^\tau=-P_f^\sigma$，则 $u^\tau=u^\sigma$；因为 $F=K(u)$，这强制 $\tau=\sigma$，于是 $v^\sigma=-v^\sigma$，与 $v\ne0$ 矛盾。所以该 Galois orbit 与其负 orbit 不交，奇部的两组极点不会相消。由式 (9)，
$$
g_{\rm odd}(z)=2\sum_{n\ge0}a_n\frac{z^{2n+1}}{(2n+1)!}
\tag{10}
$$
在原点附近成立。

### 已证明：整个 moment 序列不能来自有限个原子

固定一个 good ordinary $p$。取在足够大的 $p$-adic 系数域上的形式群同构
$$
\iota_p:\widehat{\mathbb G}_m\longrightarrow\widehat E,
\qquad
\log_E(\iota_p(T))=\Omega_p\log(1+T),
\quad\Omega_p\ne0.
$$
令 $G_p(T)=\widehat g(\iota_p(T))$。不存在有限组 $c_j\in\mathbb C_p$、$b_j\in\mathbb Z_p$ 使
$$
G_p(T)=\sum_{j=1}^s c_j(1+T)^{b_j}
\tag{11}
$$
成为形式幂级数恒等式。换言之，这个具体 Amice 型函数的整条 moment 序列不能由有限原子给出。

**证明。** 若式 (11) 成立，令 $\beta_j=b_j/\Omega_p$ 并形式代入 $T=\exp(z/\Omega_p)-1$，得到
$$
g(z)=\sum_{j=1}^s c_j\exp(\beta_jz).
\tag{12}
$$
所有 Taylor 系数等式都位于有限生成的特征 $0$ 域 $K(c_1,\ldots,c_s,\beta_1,\ldots,\beta_s)$。该域可嵌入 $\mathbb C$，并且嵌入可固定既定的 $K\hookrightarrow\mathbb C$：先为有限超越基选取代数独立的复数，再延拓到有限代数扩张即可。于是所有 Taylor 恒等式保持，且式 (12) 左侧仍是式 (8) 的复解析函数。右侧是整个复平面上的整函数。原点附近的等式由亚纯函数恒等原理延拓到全平面，迫使 $g$ 无极点，与上面的极点计算矛盾。证毕。

由奇部极点，还可排除对所有 $n$ 同时成立的有限指数表示
$$
a_n=\sum_{j=1}^s d_j\lambda_j^n
\tag{13}
$$
（系数允许在任一特征 $0$ 扩域中）。同样嵌入有限生成系数域到 $\mathbb C$ 后，右侧至多指数增长，故式 (10) 将定义整函数，仍与奇部的极点矛盾。这也排除以有限个固定矩阵的幂给出整条 $a_n$ 序列的表示，因为矩阵幂的复范数至多指数增长。

**范围限制。** 此处只排除对整条序列成立的有限原子 / 固定矩阵幂表示。它不排除单个随 $p$ 移动的下标 $n=(p-3)/2$ 模 $\mathfrak p^4$ 有特殊公式，不排除先除以阶乘后的其他模型，也不排除经过额外算子的 Katz 测度存在有用恒等式。特别地，不能用此引理宣称“所有 Fermat quotient 路线均不可能”。

形式群同构与 theta 测度的标准参照是 K. Bannai–S. Kobayashi，*Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*，§3.1（[arXiv:math/0610163](https://arxiv.org/abs/math/0610163)）。上面的非原子结论是本笔记给出的证明，不依赖把式 (8) 与他们的全部测度识别。

## 4. Lozano–Robledo 的精确类似式没有提供固定底数

Á. Lozano–Robledo，*Bernoulli–Hurwitz numbers, Wieferich primes and Galois representations*，JNT 130 (2010), 539–558，[作者文本](https://production.wordpress.uconn.edu/alozano/wp-content/uploads/sites/490/2014/01/lozano_robledo_BH.pdf)，Theorem 1.3 / Corollary 6.9 给出
$$
BH_p^{p-2}\in\mathcal O_{K,\mathfrak p}^{\times}
\quad\Longleftrightarrow\quad
v_{\mathfrak p}((\pi')^{p-1}-1)=1,
\qquad p=\pi\pi'.
\tag{14}
$$
这里的底数 $\pi'$ 随 $p$ 改变，且原文全局假设排除 $D_K=-3,-4$。此外 $BH_p^{p-2}$ 来自最小导子的 CM 曲线 $A_0$，所用 Hecke 幂次 $p+(p-2)=2p-2$，并非式 (1) 的 $E_{17}$、幂次 $p$ 的数。式 (14) 本身没有给二者的比较。关于该文 Theorem 1.2 的 adjoint 变形与本题标准表示的区别，见 [独立范围核查](2026-11-12-inert-deformation-scope.md)。

所以不能把式 (14) 的右侧换成某个固定代数数的 Fermat quotient，也不能把它左侧直接换成 $c_p^+(E)/p^2$。这两个转换各需新的已证明恒等式。

## 5. 较弱的高阶 non-Wieferich 条件是否已能无条件解决

核对到的 primary 结果如下；它们没有给出所需的无条件跨 $p$ 结论。

1. J. H. Silverman，*Wieferich’s criterion and the abc-conjecture*，JNT 30 (1988), 226–237，[DOI](https://doi.org/10.1016/0022-314X(88)90019-4)，Theorems 1–2：固定乘法底数及 $j=0,1728$ 曲线上固定非扭点的无穷多个 non-Wieferich 素数，是在 $abc$ 下证明。故 $E_{17}$ 的 $j=1728$ 允许适用其曲线范围，但没有消除假设。Theorem 2 的准确重述也见 U. Kühn–J. S. Müller，[作者文本](https://www.math.uni-hamburg.de/home/js.mueller/abc-elliptic-2012-11-12.pdf)，Theorem 1.9；该文推广仍需相应高度–radical 猜想。

2. J. F. Voloch，*Elliptic Wieferich primes*，JNT 81 (2000), 205–209，[作者文本](https://www.math.canterbury.ac.nz/~f.voloch/Pdfs/wief.pdf)，Theorem 1：若几乎所有相关素位的深度至少 $2$，则无穷多个的深度至少 $3$；乘法群与椭圆曲线各有一版。证明以“几乎所有恰为 $2$”导出固定高亏格曲线上的无穷点，再用 Faltings。这个结论的方向是**强迫有更深的素位**，不能倒过来推出无穷多个深度至多 $3$ 的素位。它与“几乎所有深度至少 $4$”完全相容。该文 Theorem 2 的无条件有限性属于函数域；最后关于数域上某个固定深度界的讨论仍明确使用 $abc$。

3. N. Fellini–M. Ram Murty，*Wieferich primes in number fields and the conjectures of Ankeny–Artin–Chowla and Mordell*，JNT 285 (2026), 209–229，[正式发表页](https://www.sciencedirect.com/science/article/pii/S0022314X26000193)，[arXiv:2508.08472](https://arxiv.org/abs/2508.08472)，Theorem 2.2 使用 Masser 的数域 $abc$；Theorem 2.3 改用“super-Wieferich 素理想只有有限多个”作为假设。后者确实比调用完整 $abc$ 更具体，但并未证明该假设。它也不提供本题的无条件固定深度上界。

这里不以检索不到定理作为任何一般不可能性证明。准确结论只是：上述最直接的已核查工具，都不足以把模 $\mathfrak p^4$ 的需求无条件闭合。特别是把本题的门槛从“单位”放宽到“赋值至多 $3$”，并不能直接调用这些定理得到无穷性。

## 6. 仍可继续攻击的精确接口

若能独立证明一个**精确等式**，把适用的二次 leading term 或 derived class 比较系数等同于一个固定非零代数倍的 $\log_p(\alpha)$（$\alpha$ 为固定非扭乘法元素）或固定非扭点的 $\log_E(R)$，则精确非零性可能已足够，无须要求该对数的最低层是单位。这与只知道某个模 $p^2$ 的 Fermat quotient 同余式有本质差别。

现在尚未得到这样的等式。已得到的是式 (6) 的局部对数计算、式 (8)–(13) 的全 moment 有限原子障碍，以及式 (14) 为什么不是式 (1) 的替代品。对角值 $a_{(p-3)/2}\bmod\mathfrak p^4$ 的低层特殊公式仍是开放的实际攻击方向。
