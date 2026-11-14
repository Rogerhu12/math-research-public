# R173：独立类秩控制的 gauge 轨道数与慢点态多项式的有限联合循环

日期：2026-11-12（UTC）。作者：literature。

状态：完整证明。固定 Laurent 系数的有限参数性质给逐步有限例外选择，进而把 R166 的未定大小有限轨道证书规范为秩控制的数量界。单个多方向算子的核仍不因此被排除。

## 1. 主结论与计数

沿用 R166 的设置：
$$
K=\operatorname{Frac}\iota(\mathcal G)\subseteq L=\mathbb C((z)),
\qquad \Gamma=\mu_{2^\infty},
$$
以及有限个
$$
S_1,\ldots,S_d\in\mathcal A,\qquad
\gamma_\zeta S_i-S_i\in\mathcal G.
$$
令 $\sigma_i=\iota(S_i)$，并记
$$
r=\dim_{\mathbb C}
\operatorname{span}_{\mathbb C}\{[\sigma_i]\}\subseteq L/K.
\tag{1.1}
$$
取任意非零实际演算
$$
T=F(S_1,\ldots,S_d)\ne0,\qquad
F\in\mathcal G[w_1,\ldots,w_d].
\tag{1.2}
$$

**定理1.1。** 可选两个嵌套的有限 gauge 族
$$
\mathcal Z_0\subseteq\mathcal Z_1\subseteq\Gamma,\qquad
1\in\mathcal Z_0,
$$
满足：

1. 若 $r\ge1$，则 $|\mathcal Z_0|\le r$；若 $r=0$，可取 $|\mathcal Z_0|=1$。
2. 对 $\mathcal Z_0$，
$$
\boxed{
\bigcap_{\zeta\in\mathcal Z_0}\ker\gamma_\zeta T=\{0\},
\qquad
\overline{\sum_{\zeta\in\mathcal Z_0}
\operatorname{Ran}\gamma_\zeta T}=H.
}
\tag{1.3}
$$
3. $\mathcal Z_1$ 比 $\mathcal Z_0$ 至多多一个元素，且
$$
|\mathcal Z_1|\le r+1
$$
（$r=0$ 时两者都可为 $\{1\}$）。
存在实际有界恒等式
$$
\boxed{
D=\sum_{\zeta\in\mathcal Z_1}
B_\zeta\gamma_\zeta T,\qquad
0\ne D\in\mathcal G,\quad B_\zeta\in\mathcal A.
}
\tag{1.4}
$$
因此 $\mathcal Z_1$ 具有 R169 的全部不变子商、有限放大约化 Koszul 正合及共同参数闭核心。
4. 在逐步构造中，固定此前所选 gauge 后，下一个 gauge 只需避开一个有限集合。
这不是关于整个笛卡尔积 $\Gamma^k$ 的全局有限坏集断言。

由 (1.3)，对任意循环向量 $g$，令 $f=Tg$，则
$$
\boxed{
\{U_\zeta f:\zeta\in\mathcal Z_0\}
\text{ 是联合循环族}.
}
\tag{1.5}
$$
选择的 gauge 族只依赖算子 $T$ 及其模式演算，不依赖循环向量 $g$。

下面逐项证明固定 Laurent 下界、有限例外、降维计数、消元算子的非零性与实际清分母。

## 2. 固定 Laurent 系数的有限参数性质

先取 $r\ge1$ 个独立方向，即其 $\sigma_1,\ldots,\sigma_r$ 在 $L/K$ 中对 $\mathbb C$ 线性无关。
R166 给它们在 $K$ 上代数无关。

写
$$
\alpha_\zeta c(z)=c(\zeta z),\qquad
h_{\zeta,i}=\sigma_i(\zeta z)-\sigma_i(z)\in K.
$$
在多项式环 $R=K[w_1,\ldots,w_r]$ 中，
$$
\Lambda_\zeta P(w)
=(\alpha_\zeta P)(w+h_\zeta).
\tag{2.1}
$$
R166 已证这是群作用，且 $R$ 没有非零真 $\Gamma$ 稳定理想。

### 2.1. 系数下界与有限卷积

若
$$
c(z)=\sum_{n\ge n_c}c_nz^n\in K\subseteq L,
$$
则
$$
\alpha_\zeta c(z)=\sum_{n\ge n_c}c_n\zeta^n z^n.
\tag{2.2}
$$
这里 $n_c$ 可为负数，但它是与 $\zeta\ne0$ 无关的固定有限下界。

又因 $\sigma_i\in\mathbb C[[z]]$，常数项在差中取消，
$$
h_{\zeta,i}
=\sum_{n\ge1}\sigma_{i,n}(\zeta^n-1)z^n.
\tag{2.3}
$$
所以所有 $h_{\zeta,i}$ 都有统一的非负次数下界，实际上阶至少一，或者恒为零。

固定一个有限次数多项式 $P\in R$。
(2.1) 只涉及有限多个 $K$ 系数及有限次的 $h_{\zeta,i}$ 乘积。
再乘任意固定的有限多个 $K$ 系数后，每个给定 $z^n$ 系数仍只含有限卷积项：
各 Laurent 因子均有固定下界，给定总次数后每个参与指数都有有限上下界。

由 (2.2)—(2.3)，这些有限项关于 $\zeta$ 都是整数幂的有限组合。
因此它们是有限 Laurent 多项式，允许有限个负 $\zeta$ 次数。

### 2.2. 线性子空间的有限例外引理

令 $V_p=K[w]_{\le p}$，这是有限维 $K$ 向量空间。
取任意 $K$ 线性子空间 $W\subseteq V_p$，以及 $\deg P\le p$。

**引理2.1。** 如果某个 $\Lambda_{\zeta_0}P$ 不属于 $W$，
则
$$
\{\zeta\in\Gamma:\Lambda_\zeta P\in W\}
$$
是有限集合。

证明：有限维线性代数给 $K$ 线性泛函
$$
\ell:V_p\longrightarrow K
$$
满足 $\ell(W)=0$ 且 $\ell(\Lambda_{\zeta_0}P)\ne0$。
在单项式基中，$\ell$ 只有有限个固定的 $K$ 系数。

将
$$
\ell(\Lambda_\zeta P)\in L
$$
按 $z$ 展开。
由 §2.1，每个固定 $z^n$ 系数是 $\zeta$ 的有限 Laurent 多项式。
因为在 $\zeta_0$ 处所得 Laurent 级数非零，
存在某个 $n$，对应的 Laurent 多项式 $q_n(\zeta)$ 不恒为零。

若 $\Lambda_\zeta P\in W$，则 $\ell(\Lambda_\zeta P)=0$，
特别 $q_n(\zeta)=0$。
非零有限 Laurent 多项式在 $\mathbb C^\times$ 中只有有限多个零点，
所以在其子集 $\Gamma$ 中也只有有限多个。
证毕。

这里没有把 $\alpha_\zeta$ 对 $K$ 的作用误当成对固定系数不作用。
负 Laurent 次数已包含在 (2.2) 的统一下界中。
也没有要求形式级数在某个复圆盘内收敛。

## 3. 每个真素理想只容纳有限个轨道成员

固定非零 $P\in R$，令 $p=\deg P$。
R166 的稳定理想定理给
$$
(\Lambda_\zeta P:\zeta\in\Gamma)=R.
\tag{3.1}
$$
所以任意真理想 $\mathfrak a\subsetneq R$ 都不可能包含全部轨道。

取
$$
W=\mathfrak a\cap V_p.
$$
这只是有限维 $K$ 向量空间 $V_p$ 的一个线性子空间，
不要求 $\mathfrak a$ 本身由低次数多项式生成。
由 (3.1)，存在 $\zeta_0$ 使 $\Lambda_{\zeta_0}P\notin W$。
引理2.1 因而给
$$
\boxed{
\{\zeta:\Lambda_\zeta P\in\mathfrak a\}\text{ 有限}.
}
\tag{3.2}
$$

特别，每个真素理想只有有限坏 gauge。
在以下递推中，一次只需要处理当前有限多个最小素理想，
故其坏集合的并仍有限。

## 4. 有限生成代数的降维工具

本节给计数所需的代数事实和实际用到的证明，
避免把“互素”直接换成“单位理想”。

### 4.1. Noether 性与有限最小素理想

$K[w_1,\ldots,w_r]$ 是 Noether 环。
可由一变量 Hilbert 基论证反复得到：
若系数环 Noether，一个多项式理想的首系数理想有限生成；
选实现这些首系数的有限多项式后，高次数项可逐次消去。
剩余次数有固定上界，落在有限自由系数模内，
其子模也有限生成。这就给整个多项式理想有限生成。

Noether 环中每个理想只有有限多个最小素理想。
一个简短的 Noether 归纳证明如下：
若有反例，取极大的反例理想 $I$。
它不是素理想，故存在 $a,b\notin I$ 而 $ab\in I$。
每个最小素理想必须包含 $a$ 或 $b$，
并因此是 $I+(a)$ 或 $I+(b)$ 的某个最小素理想。
这两个严格较大理想都不是反例，给出有限并，矛盾。

### 4.2. 非零素商使超越次数严格下降

设 $B$ 是有限生成 $K$ 整代数，$\mathfrak q\ne0$ 是素理想。
则
$$
\boxed{
\operatorname{trdeg}_K\operatorname{Frac}(B/\mathfrak q)
<
\operatorname{trdeg}_K\operatorname{Frac}B.
}
\tag{4.1}
$$

证明：从 $B/\mathfrak q$ 的有限生成元中选超越基
$\bar b_1,\ldots,\bar b_t$，并提升到 $B$。
提升后的 $b_i$ 仍代数无关。
若两个分式域的超越次数相等，则
$\operatorname{Frac}B$ 对 $K(b_1,\ldots,b_t)$ 代数。

取 $0\ne x\in\mathfrak q$。
它对该基域的最小多项式有非零常数项，
因为 $x$ 在分式域中非零。
清除有限个有理分母后，得到
$$
p_n(b)x^n+\cdots+p_1(b)x+p_0(b)=0,
$$
其中 $p_0$ 是非零 $K$ 系数多项式。
模 $\mathfrak q$ 后得
$$
p_0(\bar b_1,\ldots,\bar b_t)=0,
$$
与商中的超越基矛盾。
证毕。

### 4.3. 适合递推的维数计量

对真理想 $I\subsetneq R$，定义
$$
\delta(I)
=\max_{\mathfrak p\in\operatorname{Min}(I)}
\operatorname{trdeg}_K\operatorname{Frac}(R/\mathfrak p).
\tag{4.2}
$$
有限最小素理想使这个最大值有定义。
显然
$$
0\le\delta(I)\le r,\qquad \delta((0))=r.
$$

若 $f$ 不属于 $I$ 的任何最小素理想，
并且 $I+(f)$ 仍是真理想，则
$$
\boxed{\delta(I+(f))\le\delta(I)-1.}
\tag{4.3}
$$
事实上，每个包含 $I+(f)$ 的最小素理想 $\mathfrak q$
都包含某个 $I$ 的最小素理想 $\mathfrak p$。
因 $f\notin\mathfrak p$ 而 $f\in\mathfrak q$，
有严格包含 $\mathfrak p\subsetneq\mathfrak q$。
把 (4.1) 用于 $R/\mathfrak p$ 及其非零素理想
$\mathfrak q/\mathfrak p$，即得 (4.3)。

### 4.4. $\delta=0$ 时商确实有限维

如果 $\delta(I)=0$，每个最小素商 $R/\mathfrak p$ 都是有限生成、对 $K$ 代数的整代数。
其有限个生成元分别代数，所以它作为 $K$ 向量空间有限维；
有限维整代数又是域。
因此所有最小素理想均为极大理想，商的 Krull 维数为零。

还需证明整个商，而不只是其约化部分，有限维。
令 $B=R/I$，$\mathfrak n$ 为其 nilradical。
它是有限多个最小素理想的交，
故 $B/\mathfrak n$ 嵌入有限个有限 $K$ 域的乘积，因而有限维。

Noether 性使 $\mathfrak n$ 有限生成。
每个生成元幂零；有限个幂零生成元的可交换乘积计数表明
$\mathfrak n^N=0$ 对某个有限 $N$ 成立。
每个
$$
\mathfrak n^k/\mathfrak n^{k+1}
$$
是有限生成的 $B/\mathfrak n$ 模，因而是有限维 $K$ 空间。
有限滤过给
$$
\boxed{\dim_K(R/I)<\infty.}
\tag{4.4}
$$
使用的 nilradical 等于所有素理想之交，是通常的基本素理想刻画；
有限生成与幂零的步骤已在上面明确给出。

## 5. 从原多项式开始的逐步有限例外选择

现在固定非零 $P\in R$，并要求第一项就是原多项式：
$$
\zeta_1=1,\qquad I_1=(P).
$$
如果 $P$ 是 $R$ 的单位，$I_1=R$，所有计数立即以一项结束。

否则 $P\ne0$。
从 $I_0=(0)$ 出发，第一步已经避开其唯一最小素理想 $(0)$，
所以由 (4.3)，
$$
\delta(I_1)\le r-1.
$$

归纳设
$$
I_k=(\Lambda_{\zeta_1}P,\ldots,\Lambda_{\zeta_k}P)
$$
仍是真理想。
它有有限个最小素理想。
由 (3.2)，每个最小素理想只包含有限个新的轨道成员。
避开这些有限坏集合，选择 $\zeta_{k+1}$，则
$$
I_{k+1}=I_k+(\Lambda_{\zeta_{k+1}}P)
$$
或者已经是全环，或者满足
$$
\delta(I_{k+1})\le\delta(I_k)-1.
$$

因此至多使用 $r$ 个轨道成员，就得到以下二者之一：

- $I_q=R$；
- $I_q$ 是真理想、$\delta(I_q)=0$，从而 $R/I_q$ 是非零有限维 $K$ 代数。

这里 $1\le q\le r$，且 $\zeta_1=1$。

在第二种情形，全部最小素理想已经是极大理想。
再避开它们的有限坏 gauge 集合选择一项。
如果新理想仍真，则它包含在某个极大理想中；
该极大理想必须是原来包含 $I_q$ 的某个最小素理想，
与新项避开全部这些素理想矛盾。
所以
$$
\boxed{
I_q\text{ 零维或全环， }q\le r;
\qquad
I_m=R,\quad m\le q+1\le r+1.
}
\tag{5.1}
$$

每次有限坏集合由当时的 $I_k$ 决定。
当早期选择改变时，其最小素理想及坏集合也可能改变。
故本稿只声称逐步固定前面选择后的有限例外，
不声称整个 $\Gamma^q$ 只有有限个坏参数组合。

## 6. 零维商给非零单变量消元与全空间联合分离

暂先处理独立的实际模式 $S_1,\ldots,S_r$，
并取原 $P\in\mathcal G[w]\setminus\{0\}$。
令
$$
T=P(S_1,\ldots,S_r).
$$

若 §5 已在前 $q$ 项得到单位理想，可直接使用 §7 的快证书。
否则
$$
B=R/I_q
$$
是非零有限维 $K$ 向量空间。
在 $B$ 上考虑乘以 $w_1$ 的线性映射 $M_1$。
其特征多项式
$$
c(t)=\det(tI-M_1)\in K[t]
$$
是非零首一多项式。
由有限矩阵的 Cayley–Hamilton 恒等式，
$$
c(w_1)\in I_q.
$$
于是存在有限个 $A_i(w)\in K[w]$ 使
$$
c(w_1)=\sum_{i=1}^qA_i(w)\Lambda_{\zeta_i}P(w).
\tag{6.1}
$$

取全部系数的共同非零分母 $b\in\mathcal G$，令
$$
\rho=bc\in\mathcal G[w_1],\qquad
\widetilde A_i=bA_i\in\mathcal G[w].
$$
实际求值时，
$$
(\Lambda_{\zeta_i}P)(S)=\gamma_{\zeta_i}T
$$
是 R166 已核验的精确恒等式。因此
$$
\boxed{
\rho(S_1)
=\sum_{i=1}^q\widetilde A_i(S)\gamma_{\zeta_i}T.
}
\tag{6.2}
$$

$\rho$ 是非零多项式。
因为第一独立方向的 $\sigma_1$ 对 $K$ 超越，
$$
\rho(S_1)\ne0.
$$
所以 R152 的单方向核定理确实适用：
$\rho(S_1)$ 在全 $H$ 上单射稠密。

由 (6.2)，
$$
\bigcap_{i=1}^q\ker\gamma_{\zeta_i}T=\{0\}.
$$
又因实际系数都交换，
$$
\operatorname{Ran}\rho(S_1)
\subseteq\sum_{i=1}^q\operatorname{Ran}\gamma_{\zeta_i}T,
$$
故这些值域的和稠密。

没有把零维商的矩阵 $M_1$ 当成某个未经构造的有界 Hilbert 模型；
它只用于取得有限多项式恒等式 (6.1)。
也没有把全空间 $\rho(S_1)$ 的稠密性用于未知不变限制。

## 7. 再加至多一个轨道成员取得快证书

当 §5 得到 $I_m=R$ 时，按理想定义，有有限的
$$
C_i(w)\in K[w]
$$
满足
$$
1=\sum_{i=1}^mC_i(w)\Lambda_{\zeta_i}P(w).
\tag{7.1}
$$
清除所有系数的共同非零 $\mathcal G$ 分母 $D$，
再实际求值，即得
$$
\boxed{
D=\sum_{i=1}^m(DC_i)(S)\gamma_{\zeta_i}T,
\qquad 0\ne D\in\mathcal G.
}
\tag{7.2}
$$
全部实际系数 $(DC_i)(S)$ 在 $\mathcal A$ 中有界。

由 R151，
$$
I\in\overline{D\,\mathbb C[A]}^{\rm SOT}.
$$
因此这个至多 $r+1$ 项、包含原算子的有限轨道族，
在全部不变子商及有限放大上具有 R169 的闭关系复形结论：

- 共同核为零、总值域稠密；
- 全部 Koszul 层满足 $\ker\delta=\overline{\operatorname{Ran}\delta}$；
- 兼容向量组是共同参数列像的闭包。

这些结论使用的是快证书 (7.2)，
不是仅用前 $q$ 项的单变量消元算子 (6.2)。

## 8. 一般混合依赖模式与 $r=0$ 情形

回到 §1 的原来 $d$ 个模式。

由 R166 的常系数变换和关系分类，
可选 $r$ 个独立方向 $T_1,\ldots,T_r\in\mathcal A$，
并对原非零实际 $T=F(S)$ 有
$$
bT=P(T_1,\ldots,T_r),
\qquad
0\ne b\in\mathcal G,\quad
P\in\mathcal G[v_1,\ldots,v_r]\setminus\{0\}.
\tag{8.1}
$$
这是有限清分母后的实际恒等式。

若 $r\ge1$，对右侧应用 §§5–7。
因为每个 $\gamma_\zeta b$ 在全 $H$ 上单射，
$$
\ker\gamma_\zeta(bT)=\ker\gamma_\zeta T.
\tag{8.2}
$$
又因交换性，
$$
\operatorname{Ran}\gamma_\zeta(bT)
\subseteq\operatorname{Ran}\gamma_\zeta T.
\tag{8.3}
$$
所以前 $q\le r$ 项的共同核、总值域结论传回原 $T$。

快证书也传回，因为
$$
D=\sum_iC_i(T_1,\ldots,T_r)\gamma_{\zeta_i}(bT)
=\sum_i
[C_i(T_1,\ldots,T_r)\gamma_{\zeta_i}b]\,
\gamma_{\zeta_i}T.
\tag{8.4}
$$
括号内仍在 $\mathcal A$ 中。
这证明一般情形的 (1.3)—(1.4)。

若 $r=0$，原 $T$ 在代数分式域 $K$ 中。
非零 $T$ 有实际有限清分母式
$$
bT=D,\qquad b,D\in\mathcal G\setminus\{0\}.
$$
这本身是一项快证书；
它给 $T$ 单射，而共同 $C$ 对称性给 $T$ 值域稠密。
故此时可取 $\mathcal Z_0=\mathcal Z_1=\{1\}$。

## 9. 联合循环族的数目及其适用空间

设 $g$ 是循环向量，$f=Tg$。
对任意 $\zeta$，
$$
U_\zeta f=(\gamma_\zeta T)U_\zeta g.
$$
$U_\zeta g$ 仍循环，
所以
$$
\overline{\operatorname{span}}\{A^nU_\zeta f:n\ge0\}
=\overline{\operatorname{Ran}\gamma_\zeta T}.
$$
(1.3) 立即给 (1.5)。

因此：

- 独立类秩 $r\ge1$ 时，至多 $r$ 个 gauge 像联合循环；
- $r=0$ 时原向量已循环；
- 至多 $r+1$ 个 gauge 像对应的算子取得适用于全部不变子商的快证书。

前一条全空间联合循环，不能自动下降成某个未知子商中同样大小的循环族。
子商上的共同核与总值域结论使用后一族及其实际快证书。

当 $r\ge2$，这些数目界仍不意味着单个 $f$ 循环。

## 10. 具体应用：任意可和第一阶的点态多项式与指数权

本节给比二次式更一般、且不需预先判定独立类的应用。

设
$$
u=a_*+\sum_ja_j\chi_j,\qquad a\in\ell^1,
$$
以及
$$
w=c_*+\sum_jc_j\chi_j,\qquad c\in\ell^2.
$$
$e^w\in H$ 且循环。
令
$$
R_j=(I-e^{-2c_j}N_j)(I+e^{-2c_j}N_j)^{-1}.
$$
R160 给
$$
M_c:=\sup_j\|R_j\|<\infty,\qquad
\left(\prod_{j\in J}R_j\right)e^w=\chi_J e^w
$$
对有限不同位集合 $J$ 成立。

### 10.1. 有界乘子生成函数

定义
$$
\mathscr U(s)
=e^{sa_*}\prod_j
\bigl(\cosh(sa_j)I+R_j\sinh(sa_j)\bigr).
\tag{10.1}
$$
在每个紧 $s$ 集合上，因 $a\in\ell^1$，
各局部因子与 $I$ 的范数差之和有限且尾部一致趋零。
所以乘积局部一致按算子范数收敛，给 $\mathcal A$ 值整函数。

在有限位上，逐项使用不同位倾斜恒等式，
$$
\mathscr U_n(s)e^w
=e^{s(a_*+\sum_{j<n}a_j\chi_j)}e^w.
$$
右侧的第一阶截断一致收敛为有界 $u$，
左侧按算子范数收敛，故
$$
\boxed{\mathscr U(s)e^w=e^{su}e^w.}
\tag{10.2}
$$
这里没有把无限位倾斜映射当作点态乘法同态。

### 10.2. 前 $p$ 个对数累积量都是加性慢模式

在 $s=0$ 的一个小圆盘内，$\mathscr U(s)$ 接近 $I$，
可取 Banach 代数的局部解析对数。
各局部因子也一致接近 $I$；
其对数级数按范数绝对、局部一致收敛，
交换性给
$$
\log\mathscr U(s)
=sa_*I+\sum_j
\log\bigl(\cosh(sa_j)I+R_j\sinh(sa_j)\bigr).
\tag{10.3}
$$

令
$$
L_n(t)
=\left.\frac{d^n}{ds^n}
\log(\cosh s+t\sinh s)\right|_{s=0}.
$$
这是一个有限次数标量多项式。
对任意固定 $p$，
$$
K_1=a_*I+\sum_ja_jR_j,\qquad
K_n=\sum_ja_j^nL_n(R_j)\quad(2\le n\le p)
\tag{10.4}
$$
都按算子范数绝对收敛。
这是因为 $\sup_j\|R_j\|<\infty$，且
$$
\sum_j|a_j|^n<\infty
$$
对每个 $n\ge1$ 成立。

固定 dyadic gauge 后，充分高位 $N_j$ 不变，
所以每个 $\gamma_\zeta K_n-K_n$ 都仅是有限个真正一元解析函数的和。
于是
$$
\boxed{\gamma_\zeta K_n-K_n\in\mathcal G.}
\tag{10.5}
$$

从
$$
\mathscr U(s)
=\exp\left(\sum_{n\ge1}\frac{s^n}{n!}K_n\right)
$$
在零附近的有限阶系数比较可知：
$\mathscr U^{(k)}(0)$ 是 $K_1,\ldots,K_k$ 的有限 Bell 多项式。
这里每个固定阶只需有限项，不依赖无穷 Bell 级数在任意算子上的演算。

若 $q$ 是次数至多 $p$ 的标量多项式，
(10.2) 的有限阶导数给
$$
\boxed{
q(u)e^w=P_q(K_1,\ldots,K_p)e^w
}
\tag{10.6}
$$
其中 $P_q$ 是有限的常系数多项式。

### 10.3. 次数控制的联合循环数

假设 $p\ge1$ 且 $q(u)e^w\ne0$。
因为 $e^w$ 循环，(10.6) 的实际有界乘子非零。
它只有 $p$ 个加性慢模式，独立类秩至多 $p$。
定理1.1 因而给：

$$
\boxed{
q(u)e^w\text{ 与其至多 }p-1\text{ 个附加 gauge 像联合循环}.
}
\tag{10.7}
$$
并可再加至多一个 gauge，
使对应的至多 $p+1$ 个实际乘子具有全部不变子商上的快证书及 R169 闭关系正合性。

若实际类秩小于 $p$，可使用更小的秩界。
若 $q$ 为非零常数，向量本来就是 $e^w$ 的非零倍数，单独循环。

$p=2$ 时回收 R169 的慢平方两轨道结论。
$p\ge3$ 时没有假定高阶 Bell 系数属于 $\mathcal G$；
这里使用的是它们的有限多个对数累积量具有 $\mathcal G$ 增量。

## 11. 范围与未解决事项

1. 逐步有限坏集依赖已经选择的轨道成员，不能改写成整个参数笛卡尔积只有有限坏点。
2. $r$ 个轨道得到零维商或提前得到单位理想；不声称一定恰有 $r$ 个成员、也不声称商一定非零。
3. 零维消元算子经 R152 只在全空间使用。全部子商与复形闭核心需要额外那一步的 $\mathcal G$ 快证书。
4. 有限联合循环不等于任一成员单独循环。
5. 快证书不表示其非零分母有有界逆；强理想单位也不表示范数闭包包含 $I$。
6. 本稿没有给具体系数的类秩判定算法，也没有给每步有限坏集合的统一数值大小。
7. 点态多项式应用要求第一阶系数 $\ell^1$，以确保全程使用有界乘子。任意 $\ell^2$ 第一阶的高次点态式不能未经新的域证明直接搬用 §10。
8. 本课题的一般单核与完整 Hilbert 不变子空间问题仍未解决。

## 12. 依赖与新增内容

R166：独立类、半线性作用、稳定理想全环及一般模式的有限清分母归约。

R151：非零 $\mathcal G$ 元素的强主理想单位。

R152：单个加性慢方向上非零 $\mathcal G$ 系数多项式的全空间单射稠密。

R169：快证书的约化 Koszul 正合、共同参数闭核心及联合循环的算子到向量传递。

R147、R160：$e^w$ 循环及真实倾斜乘子恒等式。

本稿新证明的是固定 Laurent 系数的逐步有限例外引理、
从原多项式起步的秩计数、
至多 $r$ 个全空间联合分离轨道和至多 $r+1$ 个普遍快证书轨道，
以及可和第一阶点态多项式的次数控制应用。
