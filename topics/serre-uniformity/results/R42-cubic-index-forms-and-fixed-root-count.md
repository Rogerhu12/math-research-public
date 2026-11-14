# R42：三次最大整环、原始指标方程与固定分母根的解数界

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的精确结构及定量有限性。** 本文确定 R37、R40 中非 Galois 三次子域的最大整环判别式。对 R19 的三个固定 CM Fermat 族，进一步证明相应代数整数在整基中的两个非平凡坐标必互素，并得到一个精确的三次指标方程。应用 Evertse 已发表的 Thue–Mahler 解数定理，可对固定的带符号整数 $Z$、跨全部素数指数 $p$ 的解给出显式数目上界，无须假定 Mordell–Weil 秩为一。这个数目界不限制最大可能的 $p$，也不排除随 $Z$ 变化出现孤立的任意大指数解，因此没有完成 O6 或主问题。

## 1. 三次域判别式：普通分支与射线分支

沿用 R37 或 R40 的记号。令 $H/\mathbb Q$ 为实际曲线的 $2$ 除法域，故
$$
\operatorname{Gal}(H/\mathbb Q)\simeq S_3.
$$
令 $F=H^{A_3}$ 为唯一二次子域，$D_F$ 为其带符号基本判别式；令 $L$ 为任意非 Galois 三次子域，$D_L$ 为 $\mathcal O_L$ 的带符号判别式。

**命题 42.1。** 对 R37、R40 的实际数据，
$$
\boxed{
D_L=
\begin{cases}
D_F,&\text{普通、处处不分歧的 }H/F\text{ 分支},\\
4D_F,&\text{在 }(2)\text{ 处温和三次分歧的射线分支}.
\end{cases}}
\tag{42.1}
$$
具体而言：

- R37 的族 I、II、III 奇 $X$ 为普通分支，III 偶 $X$ 为射线分支。
- R40 的 $v_2(A)=1,2$ 为普通分支，$v_2(A)=3$ 为射线分支。

### 1.1 在局部分解群至多为 C2 的地方

R37、R40 已直接证明，每个相关的奇坏素数处，整个 $H/\mathbb Q$ 分解群 $D_\ell$ 都至多为 $C_2$。普通分支的素数 $2$ 也有同一性质。这里需要整个分解群结论，只有惯性阶至多为 $2$ 并不自动给出以下局部代数描述。

若 $D_\ell=1$，则
$$
L\otimes\mathbb Q_\ell\simeq\mathbb Q_\ell^3,\qquad
F\otimes\mathbb Q_\ell\simeq\mathbb Q_\ell^2.
$$
两者的局部判别式指数都为零。

若 $D_\ell=C_2$，它在三个三次嵌入上以一个固定点和一个二元轨道作用。设对应的局部二次域为 $K_\ell$，则
$$
L\otimes\mathbb Q_\ell\simeq
\mathbb Q_\ell\times K_\ell,\qquad
F\otimes\mathbb Q_\ell\simeq K_\ell.
$$
最大整环的直积判别式等于各因子判别式之积，所以
$$
v_\ell(D_L)=v_\ell(D_F).
\tag{42.2}
$$
这包括 $K_\ell/\mathbb Q_\ell$ 在 $2$ 处可能野分歧的情形；没有把二次分歧误当成温和分歧。

其余奇素数在 $H/\mathbb Q$ 中不分歧，因此两边指数都为零。即使某个这样的素数有三次 Frobenius，其局部扩张仍不分歧，故不改变判别式。

### 1.2 射线分支的素数 2

在射线分支，R37、R40 给出
$$
F\otimes\mathbb Q_2/\mathbb Q_2
\quad\text{为非分歧二次域},
$$
且三次子扩张 $L\otimes\mathbb Q_2/\mathbb Q_2$ 为完全、温和分歧的三次域。温和扩张的不同指数为 $e-1=2$，且其剩余次数为 $1$，所以
$$
v_2(D_L)=2,\qquad v_2(D_F)=0.
\tag{42.3}
$$
结合其他素数处的 (42.2)，得 $|D_L|=4|D_F|$。

最后，$D_L>0$ 当且仅当 $L$ 全实；这又等价于二次预解式 $F$ 为实二次域。因此 $D_L,D_F$ 同号，得到带符号的 (42.1)。普通分支完全同理。这给出了最大整环判别式的局部证明，无须额外假定选取的三次多项式生成最大整环。

## 2. R19 多项式生成的子整环有多大指标

下面只考虑 R19 的实际整数解。设
$$
X^3-27W^2=cZ^p,\qquad
g(T)=T^3-XT-2W,
\tag{42.4}
$$
其中 $c=1$ 对应 I、III，$c=8$ 对应 II；R19 的全部原始性、奇偶性和 $p>37$ 条件均保留。特别地，
$$
|Z|>1,\quad \gcd(Z,6p)=1,\quad
\gcd(X,W)=1,\quad 3\nmid X.
\tag{42.5}
$$
R37 已证明 $g$ 不可约，且其分裂域群为 $S_3$。

令 $\theta$ 为 $g$ 的一个根，$L=\mathbb Q(\theta)$。写
$$
d_0=\operatorname{sf}(Z),\qquad
Z=d_0 z_0^2,\qquad z_0\in\mathbb Z_{>0}.
$$
定义正整数
$$
J=J(Z,p)=
\sqrt{\frac{|Z|^p}{|d_0|}}
=
|d_0|^{(p-1)/2}z_0^p
=
|Z|^{(p-1)/2}z_0.
\tag{42.6}
$$
平方根为整数，是因为 $p$ 奇。

**命题 42.2。** 对各个分支，最大整环判别式及指标如下：

| R19 分支 | $D_F$ | $D_L$ | $[\mathcal O_L:\mathbb Z[\theta]]$ |
|---|---:|---:|---:|
| I | $d_0$ | $d_0$ | $2J$ |
| II | $8d_0$ | $8d_0$ | $2J$ |
| III，$X$ 奇 | $4d_0$ | $4d_0$ | $J$ |
| III，$X$ 偶 | $d_0$ | $4d_0$ | $J$ |

**证明。** 前两列来自 R37 的二次基本判别式表和 (42.1)。因 $g$ 首一且 $\theta$ 为代数整数，
$$
\operatorname{disc}(\mathbb Z[\theta])
=\operatorname{disc}(g)=4cZ^p.
$$
整环判别式和子整环判别式满足
$$
\operatorname{disc}(g)
=
[\mathcal O_L:\mathbb Z[\theta]]^2D_L.
\tag{42.7}
$$
逐行相除，再取正平方根，即得表中最后一列。这里分子分母同号，所以负 $Z$ 也给出同样的正指标公式。证毕。

特别地，每个奇 $q\mid Z$ 都满足
$$
v_q\bigl([\mathcal O_L:\mathbb Z[\theta]]\bigr)
=
\left\lfloor\frac{p\,v_q(Z)}2\right\rfloor.
\tag{42.8}
$$
素数 $2$ 的指标指数则在 I、II 中恰为 $1$，在 III 中为 $0$。

因此，Fermat 多项式的判别式在 $Z$ 处包含极高次幂，而最大整环判别式只保留平方自由部分；这些高次幂精确地进入指标。两者没有矛盾。任何将 $g$ 直接当作最大整环整基多项式的论证，都会丢掉 (42.7) 中这个巨大指标。

## 3. 三次指标形式及其不可约性

取任意整基
$$
(1,\omega,\eta)
$$
作为 $\mathcal O_L$ 的 $\mathbb Z$ 基。这样的整基总存在：$1$ 是格 $\mathcal O_L$ 中的原始向量，因为有理数若为代数整数便是整数，所以 $1$ 不能被任何整数 $n>1$ 在 $\mathcal O_L$ 中整除。

写
$$
\theta=a+u\omega+v\eta,\qquad a,u,v\in\mathbb Z.
\tag{42.9}
$$
设
$$
I_L(U,V)=
\det\bigl[\,1,\ U\omega+V\eta,\ (U\omega+V\eta)^2\,\bigr]_{(1,\omega,\eta)}.
\tag{42.10}
$$
这里右边是三个列向量相对于指定整基的坐标行列式。由于 $\mathcal O_L$ 对乘法封闭，$I_L$ 是整系数齐次三次式。给 $U\omega+V\eta$ 加上整数 $a$ 只对列作行列式不变的操作，故
$$
|I_L(u,v)|=[\mathcal O_L:\mathbb Z[\theta]].
\tag{42.11}
$$

**引理 42.3。** $I_L$ 在 $\mathbb Q$ 上不可约，且
$$
\operatorname{disc}(I_L)=D_L.
\tag{42.12}
$$

**不可约性证明。** 若非零 $(u,v)\in\mathbb Q^2$ 满足 $I_L(u,v)=0$，则
$$
1,\quad u\omega+v\eta,\quad (u\omega+v\eta)^2
$$
在 $\mathbb Q$ 上线性相关。于是 $u\omega+v\eta$ 的次数至多为 $2$。它属于三次域，故其次数只能为 $1$ 或 $3$，所以它必须在 $\mathbb Q$ 中。这与 $1,\omega,\eta$ 线性无关且 $(u,v)\ne(0,0)$ 矛盾。

齐次三次式若在 $\mathbb Q$ 上可约，必有一个有理线性因子，从而有一个有理射影零点。因此 $I_L$ 不可约。

**判别式证明。** 令 $\sigma_1,\sigma_2,\sigma_3$ 为 $L$ 的三个嵌入，并置
$$
\Delta_0=
\det
\begin{pmatrix}
1&\sigma_1\omega&\sigma_1\eta\\
1&\sigma_2\omega&\sigma_2\eta\\
1&\sigma_3\omega&\sigma_3\eta
\end{pmatrix},
\qquad
\Delta_0^2=D_L.
$$
由 Vandermonde 行列式公式，
$$
I_L(U,V)
=
\frac{
\prod_{i<j}
\bigl((\sigma_j\omega-\sigma_i\omega)U+
      (\sigma_j\eta-\sigma_i\eta)V\bigr)}
{\Delta_0}.
\tag{42.13}
$$
三个线性因子两两系数行列式均等于 $\pm\Delta_0$。乘积三次式的判别式为这三个行列式的平方之积，故其值为 $\Delta_0^6$。三次式整体乘以 $\Delta_0^{-1}$ 会将判别式乘以 $\Delta_0^{-4}$，最终得到 $\Delta_0^2=D_L$，即 (42.12)。

在第 2 节各分支，$D_L$ 的每个素数赋值都小于 $4$。因此 $I_L$ 的系数也互素：若所有系数都被某个素数 $\ell$ 整除，其判别式会被 $\ell^4$ 整除。后面应用的定理只要求不可约，不需要额外依赖这个系数原始性结论。

## 4. Fermat 原始性强迫指标方程的两个变量互素

上节的“指标形式系数互素”和本节的“解坐标互素”是两件不同的事。计数时必须证明后者。

**引理 42.4。** 对 (42.9) 中的坐标，必有
$$
\boxed{\gcd(u,v)=1.}
\tag{42.14}
$$

**证明。** 设素数 $\ell$ 同时整除 $u,v$。

若 $\ell\ne3$，由 $\operatorname{Tr}_{L/\mathbb Q}(\theta)=0$ 有
$$
3a+u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)=0,
$$
故 $\ell\mid a$。于是 $\theta/\ell\in\mathcal O_L$。它的最小多项式为
$$
T^3-\frac X{\ell^2}T-\frac{2W}{\ell^3}.
$$
代数整数的首一最小多项式有整系数，因此
$$
\ell^2\mid X,\qquad \ell^3\mid2W.
$$
若 $\ell$ 奇，则 $\ell\mid X,W$；若 $\ell=2$，则 $4\mid X,W$。两者均违反 $\gcd(X,W)=1$。

若 $\ell=3$，不能从迹直接除以 $3$，须另作论证。在
$\mathcal O_L/3\mathcal O_L$ 上，$\theta$ 的乘法映射等于标量 $a$ 的乘法映射。因此它的特征多项式模 $3$ 为
$$
(T-a)^3=T^3-a^3.
$$
但在特征零上，$\theta$ 的乘法特征多项式正是
$$
g(T)=T^3-XT-2W.
$$
比较模 $3$ 的 $T$ 系数，得 $3\mid X$，与 (42.5) 矛盾。所有素数都被排除，故 $\gcd(u,v)=1$。证毕。

结合前两节，实际数据给出下列**原始三次指标方程**：
$$
\boxed{
I_L(u,v)=
\begin{cases}
\pm2J(Z,p),&\text{I、II},\\
\pm J(Z,p),&\text{III},
\end{cases}
\qquad \gcd(u,v)=1.}
\tag{42.15}
$$
形式的判别式 $D_L$ 及其数域只依赖 $Z$ 的平方类和相应类域选择，不随指数 $p$ 任意增长；增长集中在这个原始 Thue–Mahler 方程的右端。

## 5. 固定 Z 时的精确候选数域数目

固定一个带符号整数 $Z$，满足 $|Z|>1$、$\gcd(Z,6)=1$，并固定四个分支 I、II、III 奇 $X$、III 偶 $X$ 中的一支。

若分支所需的模 $4$、模 $8$ 条件或二次域条件不成立，则没有实际解。以下只考虑这些必要条件成立且 R37 已排除循环边界的情形，因此 $F$ 是真正的二次域。

### 5.1 普通分支

令
$$
G_0=
\operatorname{Cl}(F)/
\big\langle[\mathfrak q]:\mathfrak q\mid2Z\big\rangle,
\qquad
r=\dim_{\mathbb F_3}(G_0/3G_0).
\tag{42.16}
$$
R37 的类域论论证给出：符合所需不分歧和指定完全分裂条件的 $S_3$ 扩张，恰对应于 $G_0$ 的指数 $3$ 子群。非零线性泛函
$$
G_0/3G_0\longrightarrow\mathbb F_3
$$
共有 $3^r-1$ 个；两个非零泛函核相同，当且仅当它们相差乘以 $-1$。因此精确候选数目为
$$
\boxed{N_Z=\frac{3^r-1}{2}.}
\tag{42.17}
$$
每个 $S_3$ 扩张的三个三次子域共轭，定义同一个 $\mathbb Q$-同构类；不同正规闭包不能给出同构的三次域。因此 (42.17) 也是三次域 $L$ 的 $\mathbb Q$-同构类数目。

### 5.2 射线分支

令
$$
G=
\operatorname{Cl}_{(2)}(F)/
\big\langle[\mathfrak q]:\mathfrak q\mid Z\big\rangle,
\qquad
V=G/3G,\qquad r=\dim_{\mathbb F_3}V.
\tag{42.18}
$$
令 $J_2\subseteq V$ 为
$$
(\mathcal O_F/2\mathcal O_F)^\times\simeq C_3
\longrightarrow G\longrightarrow V
$$
的像。为避免与 (42.6) 的整数 $J$ 混淆，这里给惯性像加下标 $2$。

若 $J_2=0$，候选数域数目为零，这正是 R37 的精确射线障碍。若 $J_2\ne0$，则 $J_2$ 是一维子空间。线性泛函 $V\to\mathbb F_3$ 在此子空间上非零的个数为
$$
2\cdot3^{r-1}.
$$
再次除以相同核的两个泛函，得到
$$
\boxed{N_Z=3^{r-1}\quad(J_2\ne0).}
\tag{42.19}
$$
R37 已证明二次共轭在这个射线类群商上取逆，所以这些类域都在 $\mathbb Q$ 上为 $S_3$ 扩张；不需要额外筛去循环六次域。

这里的 $N_Z$ 只计数抽象候选数域。它们可能没有任何 (42.15) 的解，或有指标方程解但不满足 R19 的其他系数条件，所以 $N_Z>0$ 不蕴含 Fermat 解存在。

## 6. 已发表的 Thue–Mahler 计数输入

Evertse 的 Theorem 1 给出以下统一结论：

> 若 $K$ 为数域，$S$ 含全部无限位且 $|S|=s$，$F(U,V)\in\mathcal O_S[U,V]$ 为在 $K$ 上不可约的 $m\ge3$ 次二元齐次式，则 $F(u,v)\in\mathcal O_S^\times$ 的 $\mathcal O_S^2$ 解至多组成 $(5\cdot10^6m)^s$ 个 $\mathcal O_S^\times$ 缩放轨道。

来源为 J.-H. Evertse, *The number of solutions of the Thue–Mahler equation*, J. reine angew. Math. **482** (1997), 121–149, Theorem 1。作者公布的原文已核对：定理出现在正文第 3 页，其前一段明确说明 $K=\mathbb Q$ 时每个这样的轨道恰有两个互为相反数的原始整数对。[原文](https://pub.math.leidenuniv.nl/~evertsejh/95-Thue-Mahler.pdf)；[作者的发表目录](https://pub.math.leidenuniv.nl/~evertsejh/publications.shtml)。

这里也可直接检查“至多两个”：若两个互素整数对满足
$(u',v')=\lambda(u,v)$、$\lambda\in\mathbb Q^\times$，则分子分母互素的表达式 $\lambda=a/b$ 先由整数性强迫 $b=1$，再由新一对坐标互素强迫 $|a|=1$。所以 $\lambda=\pm1$。

对 $K=\mathbb Q$、三次式 $m=3$，若有限素数集合为 $\mathcal S$，便得到
$$
\#\{(u,v)\in\mathbb Z^2:
\gcd(u,v)=1,\
0\ne I_L(u,v)\text{ 仅由 }\mathcal S\text{ 中的素数组成}\}
\le
2(15\,000\,000)^{|\mathcal S|+1}.
\tag{42.20}
$$
末尾的 $+1$ 是实无限位。这个界对形式的系数、数域判别式及右端各素数的指数都统一。

## 7. 固定带符号 Z、跨全部 p 的解数界

写
$$
t=\omega(|Z|)
$$
为 $Z$ 的不同素因子数。因 $Z$ 奇，素数 $2$ 不在此计数中。

**定理 42.5。** 固定一个带符号整数 $Z$ 及第 5 节的一支。令 $N_Z$ 为 (42.17)、(42.19) 中的候选数域数；若必要条件不成立或相应类群商没有允许的商，令 $N_Z=0$。

令 $\mathcal T_Z$ 为满足该分支全部 R19 条件的三元数据
$$
(p,X,W),\qquad p>37\text{ 为素数},
$$
的集合；$Z$ 固定，$p$ 可遍历全部素数。则
$$
\boxed{
|\mathcal T_Z|\le
\begin{cases}
2(15\,000\,000)^{t+2}N_Z,&\text{I、II},\\
2(15\,000\,000)^{t+1}N_Z,&\text{III 奇或偶 }X.
\end{cases}}
\tag{42.21}
$$
特别地，四个分支统一可使用较简洁的界
$$
|\mathcal T_Z|\le2(15\,000\,000)^{t+2}N_Z.
\tag{42.22}
$$

**证明。** 对每个候选三次域的 $\mathbb Q$-同构类，固定一个代表 $L$ 及整基 $(1,\omega,\eta)$。

每个实际数据 $(p,X,W)$ 给出 $g(T)=T^3-XT-2W$ 和一个对应的候选域。它在指定代表 $L$ 中恰有一个根：若非 Galois 三次域包含两个根，因三根和为零便包含第三根，从而包含次数为 $6$ 的整个分裂域，不可能。因此该数据唯一确定 (42.9) 的坐标。

由引理 42.4，此坐标对 $(u,v)$ 原始。由 (42.15)，I、II 中 $I_L(u,v)$ 的素数支持包含于
$$
\mathcal S=\{2\}\cup\{q:q\mid Z\},
$$
其基数为 $t+1$；III 中指标为奇数 $J$，可取
$\mathcal S=\{q:q\mid Z\}$，其基数为 $t$。逐域应用 (42.20)，分别得到 (42.21) 中不含 $N_Z$ 的因子。

还需检查多个实际数据不会落在同一坐标对而漏计。因为迹为零，
$$
a=-\frac{u\operatorname{Tr}(\omega)+v\operatorname{Tr}(\eta)}3.
\tag{42.23}
$$
若右端为整数，$a$ 便唯一；若不是整数，该坐标对根本不来自实际数据。于是 $(u,v)$ 唯一确定 $\theta$，继而确定其首一最小多项式 $g$、以及 $X,W$。

最后，固定分支的 $c$ 和固定的 $|Z|>1$ 后，
$$
|\operatorname{disc}(g)|=4c|Z|^p
$$
唯一确定 $p$。故实际数据到“候选域及原始坐标对”的映射为单射。对 $N_Z$ 个候选域求和即得结论。证毕。

这个证明没有使用 Mordell–Weil 秩、生成元或椭圆可除序列；因而不会遇到 R34 指出的高秩原始点可以具有任意深局部分母的问题。所使用的全局输入是固定三次形式的 Thue–Mahler 原始解数界。

## 8. 这个指标归约实际增加了什么

(42.1) 明确区分多项式判别式和最大整环判别式，并把 R37/R40 的类域限制转成精确的三次域判别式。对于 R19，(42.15) 又加入了原始三次指标方程，不再只有“某个三次类域存在”的必要条件。

由 (42.21)，固定带符号的 $Z$ 和一支后，即便全部允许的 Mordell–Weil 群秩都不受控，跨所有 $p$ 的实际解总数也有一个由 $t$ 和精确类群商决定的显式上界。这比只写“归约到一个 Thue–Mahler 方程”多给出了原始性证明、候选域的完整计数、以及对指数统一的解数结论。

仍须保留以下三个界限：

1. **原始坐标不等于指标为一。** $\gcd(u,v)=1$ 只允许使用原始 Thue–Mahler 计数；它不把 $I_L(u,v)$ 变成单位。实际上 (42.15) 精确要求指标随 $p$ 很快增长。
2. **解数界不等于最大指数界。** (42.21) 允许有限个非常大的 $p$，甚至允许固定 $Z$ 的唯一解恰出现在巨大指数处。不能由一个绝对或相对的解数上界，推导最大解位置的上界。
3. **固定 Z 不等于允许 Z 变化。** 各 $Z$ 的候选类群商和三次指标形式都可能变化；本文没有给出所有 $Z$ 的统一消失结论，也没有证明相关类群的 $3$ 秩统一有界。

特别地，$\mathbb Z[\theta]$ 按定义当然是单生成整环；我们没有证明、也不需要 $\mathcal O_L=\mathbb Z[\theta]$。因此这条路线目前不提供“最大整环不能单生成”的矛盾。真正剩余的强化方向是限制 (42.15) 右端在固定或变化指标形式上出现的最大指数，或利用额外 Frobenius 同余排除这些极高素数幂指标；单靠最大整环判别式和原始性尚不能完成这一步。

## 9. 来源和核对范围

- 仓库 R19：精确整数族、原始性和固定 CM 同余等价。
- 仓库 R37：固定参考曲线的 $S_3$ 分裂域、各处完整分解群、普通/射线类群商，以及基本判别式表。
- 仓库 R40：可变四次 CM 参考曲线的相同局部类域结构；本文第 1 节对它也适用。第 2–7 节的显式指标和计数只对 R19 的固定参考三族断言。
- Evertse (1997), Theorem 1：唯一新增的外部定量输入，已核对作者原文的常数、不可约性假设、$S$ 含全部无限位以及按 $S$-单位缩放轨道计数的定义。
- 最大整环局部判别式、指标形式、坐标原始性和类群商计数的推导均在本文展开；没有把未证明的变指数 Fermat 定理、单生成性猜想或条件性高度界作为输入。
