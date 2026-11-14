# R14：椭圆指数叶的模 p 闭合条件并不是目标 trace 条件

**可信度：本文的向量场计算及非代数性证明已完成。** 本结果检查一个具体的算术代数化尝试，不是对所有几何方法的不可能性断言。尚未证明无穷多个 $p$ 的初级有限性。

R6、R13 将目标表达为固定椭圆函数的移动下标导数。自然的问题是：如果这些导数在几乎所有普通素数处都有过高的整除性，能否借助 Bost 的代数化定理产生矛盾？以下实际计算最直接的椭圆指数叶，指出其 $p$-闭合条件与目标高精度 trace 条件之间尚无已证明的桥。

## 1. 固定代数群与其一维叶

取
$$
E/K:y^2=x^3-17x,\quad K=\mathbb Q(i),\qquad
G=\mathbb G_a\times E.
$$
令 $z$ 为 $\mathbb G_a$ 的坐标，$D_a=\partial_z$。在 $E$ 上取与 $\omega=dx/(2y)$ 对偶的不变向量场 $\delta$，即
$$
\delta x=2y,\qquad \delta y=3x^2-17.
$$
它延拓为全椭圆曲线上处处非零的正则向量场。两个因子的向量场彼此交换。固定一维 Lie 子空间及其平移不变分布
$$
\mathfrak h=K(D_a+\delta),\qquad D=D_a+\delta.
$$
复嵌入下，过单位元的解析叶为
$$
z\longmapsto (z,\xi(z)),\qquad
\xi(z)=(\wp(z),\wp'(z)/2),
$$
其中以群同态方式在格点处补上无穷远点。由于第一坐标为 $z$，该叶与复平面全纯同构，具有 Liouville 性质。

## 2. 普通素数处的 p-闭合条件直接失败

令 $p\ge5$、$p\ne17$。在一个位于 $p$ 上的好约化素理想处，将向量场约化到特征 $p$。加性群上有
$$
\overline D_a^{,p}=0.
$$
这是因为 $\partial_z^p$ 在特征 $p$ 仍为导子且消去 $z$，所以在多项式环及其分式域上均为零。椭圆曲线上则有
$$
\overline\delta^{,p}=H_p\overline\delta,
$$
$H_p$ 为微分 $\omega$ 对应的 Hasse 不变量。这一不变导子恒等式及 Cartier 系数公式详见 `notes/2026-11-12-cm-pcurvature-jets.md`。对当前模型可以明确写成
$$
H_p=[x^{p-1}](x^3-17x)^{(p-1)/2}.
$$
两个向量场交换，二项式展开的中间项在特征 $p$ 消失，故
$$
\boxed{\ \overline D^{,p}=H_p\overline\delta.\ }\tag{1}
$$

**命题。** 约化后的 Lie 直线 $\overline{\mathfrak h}$ 对 $p$ 次幂稳定，当且仅当 $H_p=0$。

**证明。** 若 $\overline D^{,p}=c(\overline D_a+\overline\delta)$，比较两个直积因子中的分量，第一分量给 $c=0$，第二分量随后给 $H_p=0$。反向由 (1) 直接成立。对任意常数倍 $a\overline D$，其 $p$ 次幂为 $a^p\overline D^{,p}$，所以验证生成元已足够。$\square$

更具体地，当 $p\equiv1\pmod4$ 时，提取上述系数得到
$$
H_p=\binom{(p-1)/2}{(p-1)/4}(-17)^{(p-1)/4}\ne0\pmod p.
\tag{2}
$$
二项式系数的阶乘均由小于 $p$ 的正整数构成，且 $p\ne17$，故右边确为单位。因此在**每一个**这些分裂普通素数处，$\overline{\mathfrak h}$ 都不 $p$-闭合。当 $p\equiv3\pmod4$ 时，指数方程没有整数解，$H_p=0$，所以惰性超奇异素数处则闭合。这里在剩余域为 $\mathbb F_{p^2}$ 的位上仍使用特征 $p$ 的 restricted $p$ 次幂，不能换成一个未经说明的 $p^2$ 次条件。

这次计算没有用到 R6 的 $a_{(p-3)/2}$，也没有用到任何 Sha 假设。它给出的是约化类型的判据。仅从一个 trace 标量的高阶整除，不能把 (2) 的非零 Hasse 不变量改成零。

## 3. 这个解析叶确实不代数

**命题。** 第 1 节的叶不是 $\mathbb G_a\times E$ 中的一条代数曲线。

**证明。** 若它是一条代数曲线，投影到第一因子是非恒定映射，故该曲线的函数域是 $\mathbb C(z)$ 的有限扩张。椭圆因子的 $x$ 坐标限制后就是 $\wp(z)$，于是 $\wp(z)$ 应当代数于 $\mathbb C(z)$。

选择一个非零多项式关系
$$
A_d(z)\wp(z)^d+\cdots+A_0(z)=0,
\qquad A_j\in\mathbb C[z],\quad A_d\ne0.
$$
在 $A_d(\zeta)\ne0$ 的有限点 $\zeta$，$\wp$ 不可能有极点：若极点阶为 $m>0$，最高次项的极点阶为 $md$，其余项最多为 $m(d-1)$，不能相消。因此 $\wp$ 的所有有限极点必须位于非零多项式 $A_d$ 的有限零点集合。事实上 $\wp$ 在格 $\Lambda$ 的每一个点都有二阶极点，与此矛盾。$\square$

## 4. 与 Bost 定理的准确关系

Bost 的代数化定理要求一个固定代数分布在几乎所有素理想处对 $p$ 次幂稳定，并要求适当的复解析 Liouville 条件；对代数群的不变分布，其 Lie 子空间版本更给出等价。出处：J.-B. Bost, *Algebraic leaves of algebraic foliations over number fields*, **Publ. Math. IHÉS 93** (2001), 161–221, Theorems 2.1、2.3；[期刊原文](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf)。作者后来的综述 *Evaluation maps, slopes, and algebraicity criteria*，ICM 2006 proceedings，Theorems 6.2、6.3，重述了所用版本；[作者文本](https://www.imo.universite-paris-saclay.fr/~jean-benoit.bost/Accueil_files/ICM06BostDef.pdf)。

当前显式叶满足复解析条件，但其算术闭合条件在所有分裂普通素数处失败，且这些素数无穷。定理的逆否命题只再次确认有无穷个闭合失败的素数；它没有说明同一素数的 R6 trace 是模 $\mathfrak p^2$、$\mathfrak p^3$ 还是 $\mathfrak p^4$ 非零。

若改为固定有理函数 $R\in K(E)$ 在 $E\times\mathbb P^1$ 中的图，该图本来就代数，不能仅凭这个代数性推断所需的移动下标非零。若使用除 $p$ 后的误差算子，还须面对 jet 笔记已证明的事实：$(\delta^p-H_p\delta)/p$ 模 $p$ 一般不再是导子。

因此这条具体尝试没有闭合 O3。未来若要利用算术代数化，必须另行构造一个固定的代数对象，并证明“假想的几乎所有 $p$ 额外 Sha 余秩”如何强迫其适用的全局闭合或半径条件；现有单点 trace 关系没有提供这一比较。
