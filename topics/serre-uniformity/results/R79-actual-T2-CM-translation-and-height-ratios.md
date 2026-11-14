# R79. 真实 T₂ 平移的 CM 除子公式及层 41 的 Heegner 比例平方

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明；层 41 的非消失和比例平方附精确证书。** 本文计算 R14、R33 的实际规范平移，而非只计算 Hecke 作用的迹。对
$$
X=X_{\rm ns}^+(41),\qquad d=\deg D=20,\qquad
F=27T_2+4\,\mathrm{id},
$$
有 $\operatorname{Tr}(T_2)=-8$、$\operatorname{Tr}(F)=0$，且在真实 $J(\mathbb Q)$ 中
$$
\boxed{\quad
3\eta_{D,F}
=162U_{-7}+1620B_{-8}+120B_{-4}+8U_{-3}.
\quad}\tag{0.1}
$$
这里 $U_\delta=[20P_\delta-D]$ 来自 $X$ 上真正的有理 CM 点（$\delta=-7,-3$），而
$$B_\delta=q[\widetilde P_\delta-\infty]\qquad(\delta=-4,-8)$$
来自 R71 **实际项链同源** $q:J_0(41^2)\to J$。后两个源点的 CM 域在 $41$ 分裂；它们的像是一个次数 $20$ 的 CM 除子减 $D$，不是 $X$ 上一个有理 CM 点。

对全部八个 Hecke 系数域，$B_{-4}$、$B_{-8}$ 的投影均非零；如果
$$B_{-8,f}=s_fB_{-4,f},\qquad s_f\in E_f^\times,$$
则本文从已发表的高度公式和实际模符号计算得到 $s_f^2$，并精确验证它确为 $E_f$ 中的平方。证书给出一个平方根，不据此选择真实点比例的正负号。

## 1. 对应与除子：两个作用必须区分

先在一个一般素数
$$p\equiv1\pmod8,\qquad p\ge17$$
上工作。写
$$
X=X_{\rm ns}^+(p),\quad Y=X_{\rm sp}^+(p),\quad
J=\operatorname{Jac}(X),\quad d=(p-1)/2.
$$
$D$ 是 $X$ 全部几何尖点之和。它定义于 $\mathbb Q$，这些尖点形成一个 Galois 轨道，每个尖点在 $j:X\to\mathbb P^1$ 下的宽度为 $p$。见 Rebolledo–Wuthrich（RW）§3.2。

令
$$r_C:X_0(p^2)\simeq X_{\rm sp}(p)\longrightarrow Y$$
为忘掉两条 $p$ 阶子群次序的次数二映射。令 $\mathfrak\varphi$ 为 RW §4.1 的实际 incidence 对应：
$$
(E,\{A,B\})\longmapsto
\sum_{\mathfrak v:\ A,B\text{ 在 }\mathfrak v\text{ 中互为对跖点}}
(E,\mathfrak v).
\tag{1.1}
$$
它在除子上的作用用 $\mathfrak\varphi$ 表示，在 Jacobian 上的同态用 $\varphi$ 表示。置
$$\mathfrak q=\mathfrak\varphi\circ(r_C)_*,\qquad q=\varphi r.$$
所以 $\mathfrak q$ 将一个点除子送到次数 $d$ 的有效除子，$q$ 将次数零类送到次数零类。RW Lemma 8 给一般纤维的次数 $d$；紧化 incidence 曲线的投影有限，特殊纤维按拉回长度计数，仍有同一次数。

这里 $q$ 正是 R71 的同态：
$$q^\dagger=r^\dagger\lambda,\qquad qq^\dagger=2\varphi\lambda.$$
没有把 $q$ 替换为 $q^\dagger$，也没有把 RW Lemma 22 中经过全层覆盖的 $4$ 加到单边。

### 引理 1：实际尖点像

有除子等式
$$\boxed{\mathfrak q(\infty)=D.}\tag{1.2}$$

**证明。** $r_C(\infty)$ 是一个有理尖点。$\mathfrak\varphi$ 定义于 $\mathbb Q$、保持尖点，其像是定义于 $\mathbb Q$、次数 $d$ 的有效尖点除子。目标的全部 $d$ 个尖点属于单个 Galois 轨道，所以各系数相同；总次数迫使每个系数都是 $1$。这同时核对了尖点的特殊化重数，而非只比较一般点的集合。证毕。

## 2. 两个分裂 CM 源点及其真实像

$p\equiv1\pmod8$ 保证 $p$ 在
$$K_{-4}=\mathbb Q(i),\qquad K_{-8}=\mathbb Q(\sqrt{-2})$$
中分裂。这两个域类数一。对 $\delta=-4,-8$，取 CM 椭圆曲线 $E_\delta$，以及 CM 环作用在 $E_\delta[p]$ 上的两条特征线 $A_\delta,B_\delta$。无序对子
$$x_\delta=(E_\delta,\{A_\delta,B_\delta\})\in Y(\mathbb Q)$$
是有理的：Galois 正规化 CM 环，故保持这对特征线。取其一个有序提升
$$\widetilde P_\delta\in X_0(p^2)(K_\delta).$$
在 $X_0(p^2)$ 的解释下，这是一个普通的水平 CM $p^2$ 同源点；换取共轭素理想只交换两条线，所以 $r_C(\widetilde P_\delta)$ 不变。

定义实际除子与点
$$
Z_\delta=\mathfrak q(\widetilde P_\delta)
       =\mathfrak\varphi(x_\delta),\qquad
B_\delta=[Z_\delta-D]=q[\widetilde P_\delta-\infty]\in J(\mathbb Q).
\tag{2.1}
$$
后一等式来自 (1.2)。在 $p=41$，源点可具体取
$$
\widetilde P_{-4}=(E_{-4},\ker((5+4i)^2)),\qquad
\widetilde P_{-8}=(E_{-8},\ker((3+4\sqrt{-2})^2)).
\tag{2.2}
$$
两元素的范数都为 $41$；其平方的核为循环 $41^2$ 群。

### 引理 2：粗模重数

$Z_{-8}$ 是 $j=8000$ 纤维中两条 CM 特征线互为对跖点的 $d$ 个不同项链点之和，每点重数 $1$。

令 $E_2$ 为 $X$ 上稳定子阶二的椭圆点的约化除子，则
$$\boxed{E_2=Z_{-4}.}\tag{2.3}$$
此处也是 $d$ 个不同点，每点重数 $1$。

**证明。** 对 $\delta=-8$，自同构仅有标量 $\{\pm1\}$，RW Lemma 8 的 $d$ 个项链直接给 $d$ 个粗模点。incidence 投影在这些点局部不分歧，故重数一。

对 $\delta=-4$，非标量自同构 $i$ 在射影 $p$ 挠群上是分裂对合。RW Lemma 10 证明，它固定一个无定向项链当且仅当其两条特征线互为对跖点；恰有 $d$ 个这样的项链。它分别固定这 $d$ 个项链，不在它们之间产生额外识别。

还须核对 incidence 对应的粗模拉回重数。源对子 $\{A_{-4},B_{-4}\}$ 的非标量稳定子是同一个 $C_2$；每个 incidence 三元组及其目标项链的稳定子也是该 $C_2$。在一个复形变圆盘上，三个对象均取同一个稳定子的商，故 incidence 到源的局部映射为同构，没有额外的二倍分歧。于是每点系数仍为 $1$。这些点恰为全部阶二椭圆点，得到 (2.3)。证毕。

设
$$\epsilon_3=\frac{1-\left(\frac{-3}{p}\right)}2.$$
RW Proposition 12 给阶三椭圆点除子
$$E_3=\begin{cases}P_{-3},&\epsilon_3=1,\\0,&\epsilon_3=0.\end{cases}\tag{2.4}$$
存在时 $P_{-3}$ 是 $j=0$ 上的唯一阶三椭圆点，因此定义于 $\mathbb Q$。其项链由惰性的 CM Cartan 给出。

## 3. 真正的 T₂ 对角相交除子

令 $Z_2$ 为 $X\times X$ 上的通常 $T_2$ 对应，$Q_2=\Delta^*Z_2$ 为固定点除子。不是对模多项式的根简单地计数：这里要同时保留模结构和各局部相交长度。

置
$$\epsilon_7=\frac{1-\left(\frac{-7}{p}\right)}2.$$
若 $\epsilon_7=1$，令 $P_{-7}\in X(\mathbb Q)$ 为 $j=-3375$ 上由完整 CM Cartan 给出的点。

### 定理 3

有实际有效除子等式
$$\boxed{Q_2=2\epsilon_7P_{-7}+Z_{-8}.}\tag{3.1}$$
当 $\epsilon_7=0$ 时第一项缺席，不给不存在的点赋值。

**证明：非尖点的完备枚举。** 一个固定的非尖点给次数二的自同源 $\alpha$。其整数迹 $t_\alpha$ 满足 $t_\alpha^2<8$，因此
$$t_\alpha^2-8\in\{-8,-7,-4\}.$$
三个数都是基本判别式，所以 $\mathbb Z[\alpha]$ 已为完整 CM 环。没有额外的非极大整环情形。

在非分裂 Cartan 正规化子 $N$ 中，Cartan 之外的每个元素射影阶都是二：将其写成 $z\mapsto az^p$，平方为标量。Cartan 内的非标量元素均无 $\mathbb F_p$ 特征线。因此 $N$ 中每个非平凡的分裂半单元素必为对合。

- 判别式 $-4$ 的次数二自同源为 $1\pm i$ 的单位倍。因 $p\equiv1\pmod8$，$i\in\mathbb F_p$；其两个特征值之比为 $\pm i$，射影阶四，故不可能保留任何项链。这里也检查了利用额外单位更换目标同构的所有可能。
- 判别式 $-7$ 有两个不同的次数二核，来自 $(1+\sqrt{-7})/2$ 及其共轭。其射影像不是对合，因为迹为 $1$。若 $p$ 分裂，前述群论排除一切固定项链；若 $p$ 惰性，该元素属于唯一非分裂 Cartan，故只保留其唯一无定向项链。两个核分别给 $P_{-7}$ 处的一个分支。
- 判别式 $-8$ 只有一个次数二核，来自 $\sqrt{-2}$。由于 $p\equiv1\pmod8$，它在模 $p$ 下是分裂对合。RW Lemma 10 的证明只用分裂对合的群论，故固定项链恰为两条特征线互为对跖点的 $d$ 个项链，即 $Z_{-8}$。

判别式 $-7,-8$ 的非标量自同构都不存在。各 Hecke 分支在复局部参数下的导数是 $\bar\alpha/\alpha$ 或其逆，均不等于 $1$；对 $-8$，它就是 $-1$。故其图与对角线横截，每个分支的相交长度为一。$-7$ 的两个分支给总重数二。唯一 $-7$ 项链对 Galois 稳定（或由定义于 $\mathbb Q$ 的固定点除子的唯一该 $j$ 支点看出），因此 $P_{-7}$ 确为有理点。

**证明：尖点不贡献。** RW §3.7 将此实际 Hecke 对应识别为：整数正行列式二矩阵、模 $p$ 落在 $N$ 的双陪集。若一个尖点固定，可左乘某个 $\Gamma$ 元素，得到一个行列式二的整矩阵固定 $\mathbb P^1(\mathbb Q)$ 中的一个点。它有有理特征值；特征值又是代数整数，所以两特征值为 $1,2$ 或 $-1,-2$。模 $p$ 后的射影特征值比为 $2$ 或 $1/2$，不为 $\pm1$。这与 $N$ 中分裂非平凡元素只能为对合矛盾。故没有尖点分支，证明完备。证毕。

由 (3.1)，$\deg Q_2=d+2\epsilon_7$。Lefschetz 公式（R33 (2.5)）于是给出
$$
\boxed{\operatorname{Tr}(T_2|H^0(X,\Omega^1))
=3-\frac d2-\epsilon_7.}\tag{3.2}
$$
在 $p=41$，$d=20$、$\epsilon_7=1$，所以迹为 $-8$。这由实际固定点证明，亦与 R74 的真实模符号矩阵吻合。

## 4. 典范除子：保留椭圆点项和整系数等式

令 $K_X$ 为一个典范除子。通过 $j$ 的 Riemann–Hurwitz 公式，有
$$\boxed{
6K_X\sim(p-6)D-3E_2-4E_3.
}\tag{4.1}$$
这是实际线性等价，不是仅有次数恒等式。

**证明。** 在 $j=0$ 上，除 $E_3$ 外的点分歧指数为三；在 $j=1728$ 上，除 $E_2$ 外的点分歧指数为二；尖点指数为 $p$，其余没有分歧。写
$$j^*(0)=3A_0+E_3,\qquad j^*(1728)=2A_{1728}+E_2,\qquad j^*(\infty)=pD.$$
则
$$K_X\sim-2pD+2A_0+A_{1728}+(p-1)D.$$
乘六，并用 $j^*(0)\sim j^*(1728)\sim pD$ 消去两个 $A$，得 (4.1)。等价地，实际亚纯六重微分
$$\frac{(dj)^6}{j^4(j-1728)^3}$$
的除子正是右侧。这还固定了椭圆点的负号。证毕。

记
$$K_D=[dK_X-(2g-2)D],\qquad
U_\delta=[dP_\delta-D]\quad(\delta=-7,-3,\text{ 存在时}).$$
因 $d$ 为偶数，将 (4.1) 乘 $d/2$，并用次数等式整理，得到真实 $J(\mathbb Q)$ 中的整关系
$$\boxed{
3K_D=-\frac{3d}{2}B_{-4}-2\epsilon_3U_{-3}.
}\tag{4.2}$$
这里没有在 $J(\mathbb Q)$ 中擅自除以二或三。尤其 $p=41$ 时
$$g=54,\qquad 3K_D=-30B_{-4}-2U_{-3}.\tag{4.3}$$

## 5. R33 的规范平移及一次 2F

取整数 $a,b$，满足
$$
F=aT_2+b\,\mathrm{id},\qquad
a\operatorname{Tr}(T_2)+bg=0.
\tag{5.1}
$$
以实际对称对应 $Z=aZ_2+b\Delta$ 表示 $F$，双次数为 $n=3a+b$。因为
$$\Delta^*\mathcal O(\Delta)=\omega_X^{-1},$$
对角拉回的 Picard 类为 $aQ_2-bK_X$。沿尖点的范数为 $\mathcal O(nD)$。因此 **R33 (1.3) 的同一规范平移** 恰为
$$\eta_{D,F}=[d(aQ_2-bK_X)-2nD].\tag{5.2}$$
它在 R14 中进入第二坐标的方式是
$$h_{D,F}(z)=f_F(z)-\alpha^{-1}\eta_{D,F},\qquad \alpha f_F=F,$$
所以 R47 的 Jacobian 第二坐标是 $Fu_D(x)-\eta_{D,F}$。

利用 (3.2)、(5.1)，(5.2) 可重写为
$$
\eta_{D,F}
=a[dQ_2-(d+2\epsilon_7)D]-bK_D
=2a\epsilon_7U_{-7}+adB_{-8}-bK_D.
\tag{5.3}
$$
结合 (4.2)，得到这个整个剩余类上的实际整关系
$$
\boxed{
3\eta_{D,F}
=6a\epsilon_7U_{-7}+3adB_{-8}
+\frac{3bd}{2}B_{-4}+2b\epsilon_3U_{-3}.
}\tag{5.4}
$$
对一般层，这是一条完整 $J$ 上的公式；若只保留 R45 的实际 $A$，必须投影全部点与算子，并另检查该方向确实由 $A$ 支撑。不能用全 $J$ 的公式代替未获保证的 $A$ 方向。

### 层 41 的精确特化

此时 $\epsilon_7=\epsilon_3=1$。取
$$F=27T_2+4\,\mathrm{id},\qquad n=85.$$
其迹为 $27(-8)+4(54)=0$。而
$$\deg(27Q_2-4K_X)=27(22)-4(106)=170=2n,$$
独立核对 R33 的次数零条件。$F$ 非零：若为零，$T_2$ 的特征值会全部是非整有理数 $-4/27$，与 Hecke 特征值为代数整数矛盾。R57 的实际输入在这里给 $A=J$。

公式 (5.4) 就是 (0.1)。在 $J(\mathbb Q)\otimes\mathbb Q$ 中可写为
$$
\eta_{D,F}
=54U_{-7}+540B_{-8}+40B_{-4}+\frac83U_{-3}.
\tag{5.5}
$$
若需要完全没有有理系数的平移，直接取 $3F$；其规范平移就是 (0.1) 右侧的实际点。

R30、R47 使用 **$G=2F$ 一次**。由平移的可加性，
$$
\boxed{
\eta_{D,G}
=108U_{-7}+1080B_{-8}+80B_{-4}+\frac{16}{3}U_{-3}
}\tag{5.6}
$$
于 $J(\mathbb Q)\otimes\mathbb Q$，或将两边乘三得到 $J(\mathbb Q)$ 中的精确等式。这里没有再次外乘 $d$ 或 $d^2$；$u_D(x)=[20x-D]$ 已含该尺度。

本文没有证明 $F$ 属于 R45 的零坏高度核。若直接用这个方向，R54 的有限坏高度靶值必须保留；(5.6) 是其真实全局平移，不能据此把所有非辅助局部项设为零。

## 6. 两个实际 B 点在全部 54 条特征线上非零

用 R74 相同的实际模符号空间：

    M = msinit(1681, 2, -1);
    N = msnew(M);
    W = msatkinlehner(M, 1681, N);
    P = N[1] * matker(W - matid(117));
    H = mshecke(M, 2, P) + 2*mshecke(M, 3, P);

这是 star $-$、new、Fricke $+$ 的 $54$ 维空间；star 不能与 Fricke 混淆。$H$ 的不可约特征因子次数为
$$2,3,3,4,4,8,12,18,$$
且无重因子。对 $\delta=-4,-8$ 定义实际整数行
$$
v_\delta
=\sum_{a=1}^{|\delta|-1}\chi_\delta(a)
\,\operatorname{mseval}\!\left(M,P,
\left[\frac a{|\delta|},\infty\right]\right).
\tag{6.1}
$$
以 $v_\delta H^j$、$0\le j<54$ 为行的矩阵记为 $\mathcal K_\delta$。完整从零复算给
$$
\boxed{
\det\mathcal K_{-4}\equiv414,\qquad
\det\mathcal K_{-8}\equiv520\pmod{1009}.
}\tag{6.2}
$$
$6=\operatorname{den}(H)$ 在模 $1009$ 可逆，两个非零行列式严格证明两行在每条特征线上均非零。

R74 §3 的定向与 Gauss 和论证同样适用于这两个原始奇二次特征：
$$
\mathcal L_\delta(\Phi_f^-)
=-\tau_\delta L(f\otimes\chi_\delta,1),\qquad
\tau_{-4}=2i,\quad\tau_{-8}=2\sqrt2\,i.
\tag{6.3}
$$
没有额外的 star 投影二倍。因此
$$L(f\otimes\chi_{-4},1)\ne0,\qquad
L(f\otimes\chi_{-8},1)\ne0$$
对全部 $54$ 个共轭新形式成立。

### 偶判别式的来源必须另核

Gross–Zagier (1986) I §3 明确在正文中假设 $D$ 为奇数，故不能只引用该版本覆盖 $-4,-8$。这里使用 **Cai–Shu–Tian (2014), Theorem 1.1**：它对任意虚二次判别式 $D$ 陈述公式，条件为环类导子与 $N$ 互素、$N$ 的素因子满足相应 Heegner 条件；没有 $D$ 奇的限制。

本例环类导子为一、类数一、$41$ 分裂、$(D,1681)=1$，该定理全部条件成立。其精确式为
$$
L'(1,f/K_\delta)
=\frac{8\pi^2(f,f)_{\Gamma_0(N)}}{u_\delta^2\sqrt{|\delta|}}\,
\widehat h_{K_\delta}(y_{\delta,f}),\qquad
y_{\delta,f}=e_f[\widetilde P_\delta-\infty],
\tag{6.4}
$$
其中 $u_{-4}=2$、$u_{-8}=1$。文献的 $2^{-\mu(N,D)}$ 在此为一。

R57 核对的 DLF 输入给全部 $L'(f,1)\ne0$。于是 (6.3)–(6.4) 证明所有 $y_{\delta,f}$ 非零。R71 的 $q$ 在真正 new、Fricke $+$ 部分为同源，故
$$\boxed{B_{-4,f}\ne0,\qquad B_{-8,f}\ne0\quad\text{对每个 }f.}\tag{6.5}$$
实际上 $B_{-4}$ 和 $B_{-8}$ 各自都生成整个 $J(\mathbb Q)\otimes\mathbb Q$ 作为 $\mathbb T_{\mathbb Q}$ 的秩一模。

这里 $47$ 在 $K_{-4}$、$K_{-8}$ **均惰性**。本文没有把 R75 的分裂 $47$ 的公式直接用于它们；它们的非零 $47$ 进自高度由 (6.5) 与 R77 已证的各因子高度非退化性推出。

## 7. 实际点比例的精确平方，保留单位与极化因子

对每个 Hecke 因子，$J_f(\mathbb Q)\otimes\mathbb Q$ 是秩一 $E_f$-模，所以由 (6.5) 有唯一
$$s_f\in E_f^\times,\qquad B_{-8,f}=s_fB_{-4,f}.\tag{7.1}$$
$E_f$ 全实，任一实嵌入下，极化高度中的比例为 $\sigma(s_f)^2$。

源上的 $y_{\delta,f}$ 也属于有理 Mordell–Weil 子空间：$q$ 在该 new、Fricke $+$ 因子上是定义于 $\mathbb Q$ 的同源，而 $q y_{\delta,f}=B_{\delta,f}$ 已有理；用有理定义的反向同源后张量 $\mathbb Q$ 即得。因此同一个 $s_f$ 也给 $y_{-8,f}=s_fy_{-4,f}$，可在共同的有理子空间上比较下述两个二次域的高度。

将 (6.4) 对两个判别式相除。$L'(f,1)$、Petersson 范数消去，两个二次域到 $\mathbb Q$ 的共同基变换尺度也消去，得到
$$
\sigma(s_f)^2
=\frac{u_{-8}^2\sqrt8}{u_{-4}^2\sqrt4}
\frac{L(f^\sigma\otimes\chi_{-8},1)}
     {L(f^\sigma\otimes\chi_{-4},1)}
=\frac{\sqrt2}{4}
\frac{L(f^\sigma\otimes\chi_{-8},1)}
     {L(f^\sigma\otimes\chi_{-4},1)}.
\tag{7.2}
$$
从源搬到 $J$ 时，两边同乘 R71 的同一个 $\sigma(\kappa_f)$，所以取消；没有将 $q$ 冒充保持主极化的同构。若改成微分对数坐标，相同的切映射因子也在这个点比例中取消。

在同一条模符号特征线上，(6.3) 给
$$
\frac{\mathcal L_{-8}(\Phi_{f^\sigma}^-)}
     {\mathcal L_{-4}(\Phi_{f^\sigma}^-)}
=\sqrt2\,
\frac{L(f^\sigma\otimes\chi_{-8},1)}
     {L(f^\sigma\otimes\chi_{-4},1)}.
$$
因此
$$
\boxed{
s_f^2
=\frac14\,\frac{v_{-8,f}}{v_{-4,f}}\in E_f^\times.
}\tag{7.3}
$$
两个行在同一特征线上的比不受其模符号周期或向量归一化影响。关键的 $1/4$ 来自 $-4$ 的额外单位；漏掉它会改变点比例。

### 完整可复算的八域证书

令 $h_f$ 为 $H=T_2+2T_3$ 在 $E_f$ 中的像。对每个不可约因子 $f_H(X)$，脚本直接求出
$$\rho_f(X)\in\mathbb Q[X],\qquad \deg\rho_f<\deg f_H,$$
使在相应真实模符号子空间上
$$v_{-4}\rho_f(H)=v_{-8}/4.$$
然后在 $E_f=\mathbb Q[X]/(f_H)$ 中给出 $r_f$，并**用精确代数运算核对**
$$r_f^2=\rho_f(h_f).$$
实际点比例满足 $s_f\in\{r_f,-r_f\}$。这是每个数域一个符号，共八个符号；不允许在各共轭嵌入上任意独立选号。

例如次数二因子为
$$f_H(X)=X^2-2X-31,$$
其准确平方为
$$
\rho_f(h_f)=\frac{3h_f+14}{4}
=\left(\frac{h_f+5}{4}\right)^2.
\tag{7.4}
$$
换用 $h_f=1+4\sqrt2$ 的表示，这个因子上的实际比例为
$$s_f=\pm\left(\frac32+\sqrt2\right).$$
其余七域的完整有理系数均保存在证书中；最大次数为 $18$。本文不通过浮点近似或数域识别猜测这些系数。

独立 Python 检查器只用整数与有理数运算。它逐域核对平方恒等式，并以 $\prod_{g\ne f}g(H)$ 作投影因子，严格核对
$$
4v_{-4}\rho_f(H)\prod_{g\ne f}g(H)
=v_{-8}\prod_{g\ne f}g(H).
\tag{7.5}
$$
这最后一个核对在 $\mathbb Q$ 上进行，不仅是若干模素数抽样。

## 8. 接入 R47 的 ξ，而不丢掉真实局部高度

在每个因子用 $P_f=B_{-4,f}$ 作有理 Mordell–Weil 基向量；必要时乘整数成为实际点，并相应缩放全部坐标。写
$$
U_{-7,f}=r_{7,f}P_f,\qquad
B_{-8,f}=s_fP_f,\qquad
U_{-3,f}=r_{3,f}P_f.
\tag{8.1}
$$
由 R47 的对数同构，这些也是相应对数坐标。$G=2F$ 的规范平移坐标准确为
$$
\boxed{
\xi_{G,f}
=108r_{7,f}+1080s_f+80+\frac{16}{3}r_{3,f}.
}\tag{8.2}
$$
算子的特征值为 $G_f=54a_2(f)+8$。所以真实全局二次项是
$$
\sum_f\operatorname{Tr}_{E_f\otimes\mathbb Q_{47}/\mathbb Q_{47}}
\!\left(
c_fz_f(x)\left((54a_2(f)+8)z_f(x)
-108r_{7,f}-1080s_f-80-\frac{16}{3}r_{3,f}\right)
\right),
\tag{8.3}
$$
其中 $z_f$ 始终来自 $u_D(x)=[20x-D]$，$c_f$ 对此基非零（R77）。

式 (8.3) 必须再减去同一规范的完整辅助局部高度，并保留该方向的有限坏高度靶值。本文已把一个实际 $\xi$ 化为指定 CM 点的准确线性组合，且算出其中 $s_f$ 的精确平方；尚未用自高度决定 $s_f$ 的符号，也未计算 $r_{7,f},r_{3,f}$、局部高度的迭代积分或 CM 根的导数。因此本结果不声称完成共同根排除。

## 9. 复算文件和来源

复算无需 Sage 或 Magma。PARI/GP 2.19.0 的两个脚本从实际模符号空间重新开始；Python 检查器仅用标准库。

- scripts/p41_small_cm_twists.gp：全部空间、两个 twist rows、精确秩及模 $1009$ 行列式；本次从零运行约 $4.4$ 秒。
- scripts/data/p41_small_cm_certificate.json：两条实际整数行，复用并以 SHA256 固定 R74 的 Hecke 矩阵。
- scripts/verify_p41_small_cm_certificate.py：独立核对 (6.2)。
- scripts/p41_cm_height_ratios.gp：逐个真实 Hecke 子空间求 (7.3)，并计算、验证平方根。
- scripts/data/p41_cm_ratio_certificate.json：$6H$ 的完整整数矩阵、八个系数域、$\rho_f$ 和一个未经点符号选择的平方根。
- scripts/verify_p41_cm_height_ratios.py：独立在 $\mathbb Q$ 上核对 (7.5) 与八个平方恒等式。

小 CM 非消失证书的 SHA256 为

    717ca26634c9613a3d8677dda68895d7d945cca370563b76c299e820d24c5f51

八域比例证书的 SHA256 为

    28f49fe984a43b2e9f556e7030f1afa14cc777c304cde8e8a2731c11afad9899

原始来源及准确用途：

1. M. Rebolledo and C. Wuthrich, **A moduli interpretation for the non-split Cartan modular curve**, *Glasgow Mathematical Journal* **60** (2018), 411–434，DOI [10.1017/S0017089517000180](https://doi.org/10.1017/S0017089517000180)；[作者 2017-06-19 版本](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。作者版 §3.2 p.7 给尖点及宽度；Lemma 8 p.8、Lemma 10 p.9 给对跖计数与分裂反射；Proposition 12 p.10 给椭圆点；§3.7 pp.11–12 给实际 Hecke 与双陪集的识别；§4.1 pp.12–13、Lemma 22 p.18 给真实项链对应。
2. L. Cai, J. Shu and Y. Tian, **Explicit Gross–Zagier and Waldspurger formulae**, *Algebra & Number Theory* **8** (2014), 2523–2572，DOI [10.2140/ant.2014.8.2523](https://doi.org/10.2140/ant.2014.8.2523)；[已发表全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)。pp.2524–2525 的数据与 Theorem 1.1 直接用于 (6.4)；其中 $u^2\sqrt{|D|}$ 明确保留。p.2534 的例子将一般系数域的 Theorem 1.5 接到普通 $X_0(N)$ 和真实尖点基点，没有奇判别式限制。
3. B. Gross and D. Zagier, **Heegner points and derivatives of L-series**, *Inventiones Mathematicae* **84** (1986), 225–320，[作者保存的期刊全文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01388809/fulltext.pdf)。I §3 p.227 的奇判别式限制是本次核查到的适用范围，故没有单独依赖该版本处理 $-4,-8$。
4. [PARI/GP 官方模符号文档](https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html)：用于实际空间、star、Fricke、new 和路径评价的可复算定义。Gauss 和的定向、Hecke 特征线判据及原始 Manin 来源详见 R74。
5. 仓库 R14、R33：实际规范平移；R47：含 $d$ 的对数坐标与一次 $2F$；R54：非零坏高度靶值；R57：层 $41$ 的实际 $A=J$；R68、R71：真实极化及项链同源；R74：模符号空间及定向；R77：$47$ 进高度各因子非退化。
