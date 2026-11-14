# R71. 项链同源的真实极化倍率及层 41 的完整特征多项式

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明，有限域运算附精确复算脚本。** 本文给 R68 所需的一个具体同源及其 Rosati 倍率，而不是给抽象同源随意指定一个次数。设
$$J_0=J_0(p^2),\qquad J_s=J_{\rm sp}^+(p),\qquad J=J_{\rm ns}^+(p).$$
用 Rebolledo–Wuthrich 的项链对应构造实际 $q:J_0\to J$，证明
$$q q^\dagger=2\varphi\lambda.$$
在 $p=41$，精确求出右侧在真实 $H^0(J,\Omega^1)$ 上的全部特征值、类型及重数，并得到
$$\det(q q^\dagger\mid H^0(J,\Omega^1))
=2^{108}3^8 5^8 113^8 461^6.$$
尤其对 $\ell\notin\{2,3,5,113,461\}$，该 $q$ 在 $\mathbb Z_{(\ell)}$ 同源范畴有明确右逆，真正的 $p^2$-new、Fricke $+$ 投影在该处为整。

有限置换模块、真实微分空间和 Heegner 商三者在下面逐一连接。一般层不能把完整 $J$ 的特征多项式照搬到实际 $A$；层 41 可用 R57 核查的 DLF 输入 $A=J$。本文不计算辅助局部高度、规范平移或共同根。

## 1. 真实对应、因子 4 和因子 2

记 $\varphi:J_s\to J$ 为把无序对子 $\{A,B\}$ 送到其中 $A,B$ 互为对跖点的项链之和；记 $\lambda:J\to J_s$ 为把项链送到其全部 $(p+1)/2$ 个对跖对子之和。定义及其在 Jacobian 上的延拓见 Rebolledo–Wuthrich（以下简称 RW）§4.1。

两端均用 Jacobian 的规范主极化定义伴随。RW Lemma 22 在实际模曲线对应上给
$$4\varphi=(\widetilde\pi_n)_*\pi_s^*,\qquad
4\lambda=(\pi_s)_*(\widetilde\pi_n)^*.
\tag{1.1}$$
因此
$$\boxed{\varphi^\dagger=\lambda.}\tag{1.2}$$
这是实际同态的等式：取 (1.1) 第一式的伴随得到 $4\varphi^\dagger=4\lambda$，而阿贝尔簇同态群无挠。不能把 (1.1) 的 $4$ 漏在一边，也不能因 RW 的另一对 $\psi,\mu$ 使用不同规范化而否定 (1.2)。

这里使用对应在模曲线上的闭包及诱导同态。一般纤维中的计数确定对应；在有额外自同构的点，不重新用没有重数的粗模点计数替换它。

有定义于 $\mathbb Q$ 的同构 $X_0(p^2)\simeq X_{\rm sp}(p)$。在非尖点上，它把
$$ (E,C),\quad |C|=p^2,$$
送到
$$\left(E/C[p],\ E[p]/C[p],\ C/C[p]\right).$$
后两者是不同的 $p$ 阶子群；反向由对应的两个 $p$ 同源构成一条核为循环群的 $p^2$ 同源。交换这两个子群恰对应 Fricke 对合 $w_{p^2}$。也可从群的共轭直接核对：$\operatorname{diag}(p,1)$ 将 $\Gamma_0(p^2)$ 共轭到两个非对角元都被 $p$ 整除的群，并将 Fricke 矩阵变成与 $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ 成比例的矩阵。

令
$$r=(X_{\rm sp}\longrightarrow X_{\rm sp}^+)_*:J_0\longrightarrow J_s.$$
这个曲线商映射的次数是 $2$，故
$$r r^\dagger=[2].\tag{1.3}$$
定义实际整同态
$$q=\varphi r:J_0\longrightarrow J.\tag{1.4}$$
由 (1.2)–(1.3)，
$$\boxed{\kappa:=q q^\dagger=2\varphi\lambda.}\tag{1.5}$$
所有对应都与远离 $p$ 的 Hecke 算子相容。

### 命题 1：$q$ 恰保留真正的 new、Fricke $+$ 部分

令 $e_0$ 为 $J_0$ 上 $p^2$-new、Fricke $+$ 的有理 Hecke 投影。则 $q(1-e_0)=0$，而 $q:e_0J_0\to J$ 为同源。因而在同源范畴
$$q^\dagger q=\kappa e_0,\qquad
e_0=q^\dagger\kappa^{-1}q.
\tag{1.6}$$
第一式的 $\kappa$ 通过 $q$ 的 Hecke 识别作用于源。

**证明。** $r$ 是 Fricke 商，故消去 Fricke $-$ 部分。为准确识别旧部分，置
$$G=\operatorname{PGL}_2(\mathbb F_p),$$
以 $T,S,N,B$ 分别表示 split Cartan、其正规化子、non-split 正规化子和 Borel。在全层微分中，$X_0(p)$ 来自 $B$ 不变量，而 $\mathbb C[G/B]=\mathbf1\oplus\mathrm{St}$；$\mathbf1$ 不贡献微分，因为 $X(1)$ 的亏格为零。故旧部分对应真正的 Steinberg 表示 $\mathrm{St}$。

在该表示中，$T$ 不变量为二维，由两个退化映射给出的 $p$ 层旧形式张成；$S$ 不变量为一维，$N$ 不变量为零。两条退化映射的独立性也直接见于 $f(z)$ 与 $f(pz)$ 的尖点展开。对应 $\varphi$ 通过同一全层曲线作用，故把旧的 $S$ 不变量送到零。这里不是仅以维数相等识别旧部分。

对真正 $p^2$-new 形式，Mercuri–Schoof Proposition 5.2 给一个绝对不可约的有限 $G$ 表示，它既非一维也非 $\mathrm{St}$。其 $S$ 与 $N$ 不变量同时为零或同时为一维；后一种恰是 Fricke $+$ 情形，见该文 Proposition 2.1。RW Theorem 15 及 §4.4–4.5 证明 $\varphi\lambda$ 在这些项链类型上非零，故 $\varphi$ 将这两条不变线同构。于是 $q$ 在每个 new、Fricke $+$ 因子上为同源，且没有其他保留因子。

$q$ 的对偶消去正交的互补部分；由 (1.5) 和同源可逆性得 (1.6)。证毕。

对 R45 的一般实际商，只须用 $q_A=e_Aq$、$\kappa_A=e_A\kappa$。本文下面的全 $J$ 谱在这时应限制到实际保留的新形式，不能自动保留全部类型。

## 2. 从项链矩阵到真实微分的证明连接

对固定的一般椭圆曲线，其项链集合是 $G/N$。令
$$U=\mathbb Q[G/N],\qquad
C_{v,w}=\#\{\text{$v,w$ 共有的对跖对子}\}.
\tag{2.1}$$
RW Proposition 14、§4.5 给
$$C_{v,v}=\frac{p+1}{2},\qquad C_{v,w}\in\{0,1\}\ (v\ne w),$$
并且真正对应 $\varphi\lambda$ 在一般纤维上恰由该矩阵给出。$C$ 对称、正定、$G$ 等变。

写 $\widetilde X=X(p)/Z$，其中 $Z$ 是标量子群。其几何纤维有两个连通分支。Mercuri–Schoof §5、Proposition 5.1 明确给出
$$V:=H^0(\widetilde X_{\mathbb C},\Omega^1),\qquad
H^0(J,\Omega^1)=V^N,
\tag{2.2}$$
及
$$V=\operatorname{Ind}_{H}^{G}W,\qquad
H=\operatorname{PSL}_2(\mathbb F_p),\quad
W=S_2(\Gamma(p)).
\tag{2.3}$$
这里 $\Gamma(p)$ 可同时加入 $-I$，它对上半平面和权二形式没有作用。

### 引理 2：同一个 $C$ 作用于每一条实际 $N$ 不变线

若 $\pi$ 为复不可约 $G$ 表示且 $\dim\pi^N=1$，记 $\lambda_\pi$ 为 $C$ 在 $U$ 中该表示上的标量。那么真正 $\varphi\lambda$ 在 $V^N$ 的每个 $\pi^N$ 副本上也以 $\lambda_\pi$ 作用。

**证明。** $U$ 是由同一全层覆盖的泛纤维构成的置换模块。$G$ 等变的矩阵 $C$ 等价于 $N$ 双陪集代数中的一个对应；该对应在任意 $G$ 模 $V$ 的 $N$ 不变量上都通过
$$V^N\simeq\operatorname{Hom}_G(U,V)$$
函子地作用。用 $U\simeq\bigoplus_{\pi^N\ne0}\pi$ 和
$$V\simeq\bigoplus_\pi\pi\otimes M_\pi$$
可见，它在 $\pi^N\otimes M_\pi$ 上是 $\lambda_\pi$ 乘恒等。这里 $U$ 的无重数性来自 Mercuri–Schoof Proposition 2.1；也见 RW §4.4。由 (2.1) 的泛纤维等式，这个双陪集对应正是实际 $\varphi\lambda$，不是另一个抽象的同谱算子。对微分采用拉回时，出现转置对应；$C$ 对称，标量不变。证毕。

故要得到实际 Jacobian 特征多项式，必须用 $M_\pi$ 的真实维数；不能把有限置换模块中的 $\dim\pi$ 当作这个重数。

## 3. 层 41 的真实重数：等变 Euler 特征

在 $p=41$，贡献 $N$ 不变量的非平凡类型为：

| 类型 | 参数 | $\dim\pi$ | 不同复表示的个数 |
|---|---|---:|---:|
| twisted Steinberg | $\mathrm{St}\otimes\chi_{41}$ | $41$ | $1$ |
| principal series | $\theta:\mathbb F_{41}^\times\to\mathbb C^\times$，$\theta(-1)=1$，$\theta^2\ne1$ | $42$ | $9$ |
| cuspidal | $\nu:\mathbb F_{41^2}^\times/\mathbb F_{41}^\times\to\mathbb C^\times$，$\nu$ 为奇字符，$\nu^2\ne1$ | $40$ | $10$ |

字符均按 $\theta\sim\theta^{-1}$、$\nu\sim\nu^{-1}$ 配对。PS 字符阶为 $4,5,10,20$，表示数依次 $1,2,2,4$；SC 字符阶为 $6,14,42$，表示数依次 $1,3,6$。这些都是实际有限 $G$ 类型；由 Mercuri–Schoof Proposition 5.2，它们与对应全局新形式的类型相连。

### 引理 3：真实全纯微分中的重数公式

设 $\pi$ 为特征标取实值的复 $G$ 表示。记 $I_2,I_3,I_p\subset H$ 为全层连通曲线到 $X(1)$ 的三个分支惯性群。则
$$\dim\operatorname{Hom}_G(\pi,V)
=\dim\pi^H+
\frac{\dim\pi-\dim\pi^{I_2}-\dim\pi^{I_3}-\dim\pi^{I_p}}2.
\tag{3.1}$$

**证明。** 连通 $X(p)\to X(1)\simeq\mathbb P^1$ 的甲板群为 $H$，三个分支指数为 $2,3,p$：它们分别来自 $\operatorname{PSL}_2(\mathbb Z)$ 的两个椭圆稳定子和抛物生成元 $\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ 模 $p$ 的阶。$p\ge5$ 时没有额外分支。

将底球面剖分，并令三个分支点都是顶点。非分支胞腔的提升均为自由 $H$ 轨道，分支顶点的提升是 $H/I_i$。由去掉三个点的球面的 Euler 特征为 $-1$，在复表示环中
$$[H^0]-[H^1]+[H^2]
=-[\mathbb C[H]]+\sum_{i=2,3,p}[\mathbb C[H/I_i]].$$
曲线连通且 $H$ 保定向，所以 $H^0,H^2$ 都为平凡表示；因此
$$[H^1]=2[\mathbf1]+[\mathbb C[H]]-
\sum_{i=2,3,p}[\mathbb C[H/I_i]].
\tag{3.2}$$
与 $\operatorname{Res}_H^G\pi$ 取内积并用 Frobenius reciprocity，得到 (3.1) 右侧的两倍。另一方面，$H^1=W\oplus\overline W$，而 $\pi\simeq\overline\pi$；故两个 Hodge 部分的内积相同。最后用 (2.3) 再次作 Frobenius reciprocity，得到 (3.1)。即使 $\pi|_H$ 可约，此推导仍逐项成立。证毕。

### 命题 4：各类型的准确重数

层 41 中，$\mathrm{St}\otimes\chi_{41}$ 的真实重数为 $3$；每一个 PS 复表示的真实重数为 $2$；SC 阶 $6,14,42$ 的每一个复表示的真实重数依次为 $3,4,3$。

**证明。** 以下所有非平凡表示都无 $H$ 不变量。$I_2$ 的非平凡元素在 $p=41$ 时为 split semisimple，$I_3$ 的两个非平凡元素为 nonsplit semisimple。用标准有限 $\operatorname{PGL}_2$ 特征标计算不变量平均值：

| 类型 | $\dim\pi$ | $\dim\pi^{I_2}$ | $\dim\pi^{I_3}$ | $\dim\pi^{I_{41}}$ | (3.1) 给的重数 |
|---|---:|---:|---:|---:|---:|
| $\mathrm{St}\otimes\chi_{41}$ | $41$ | $21$ | $13$ | $1$ | $3$ |
| 任意容许 PS | $42$ | $22$ | $14$ | $2$ | $2$ |
| SC 阶 $6$ | $40$ | $20$ | $14$ | $0$ | $3$ |
| SC 阶 $14$ | $40$ | $20$ | $12$ | $0$ | $4$ |
| SC 阶 $42$ | $40$ | $20$ | $14$ | $0$ | $3$ |

具体说，Steinberg 在 split、nonsplit、非平凡 unipotent 元素上的值为 $1,-1,0$；$\chi_{41}$ 在 $H$ 上平凡。PS 在 split 对合上的值为 $2\theta(-1)=2$，在 nonsplit 元素上为 $0$，在非平凡 unipotent 上为 $1$。SC 在 split regular 元素上为 $0$，在非平凡 unipotent 上为 $-1$，在 nonsplit 元素 $t$ 上为 $-\nu(t)-\nu(t)^{-1}$。

当 $t$ 的阶为 $3$，阶 $14$ 字符在其上平凡，特征标为 $-2$；阶 $6$、$42$ 的字符值是本原三次根，特征标为 $1$。例如 SC 阶 $14$ 的 $I_3$ 不变量维数为 $(40-2-2)/3=12$。代入 (3.1) 即得全表。证毕。

作为结果而非证明前提，总维数为
$$3+9\cdot2+1\cdot3+3\cdot4+6\cdot3=54.$$
这也与 R59、R64 的完整类型维数 $3+18+33$ 相符。

## 4. 有限域中的标量，直接由字符和确定

### 4.1 项链的可复算参数

取 $\delta=3\in\mathbb F_{41}$，它是非平方。每个项链唯一由其对跖 involution 确定。全部非分裂 involution 为
$$r_{a,d}(x)=a+\frac d{x-a},\qquad
a\in\mathbb F_{41},\quad d\in\mathbb F_{41}^{\times}\text{ 非平方},
\tag{4.1}$$
且 $r_{a,d}$ 交换 $\infty,a$。其矩阵为
$$\begin{pmatrix}a&d-a^2\\1&-a\end{pmatrix}.$$
之所以没有漏项，是非分裂 involution 不可能固定 $\infty$，故其左下元非零；归一化到 $1$ 后，迹零和非分裂条件恰为 (4.1)。非分裂 Cartan 的唯一二阶元的中央化子恰为其正规化子，故这确实是 $G/N$ 的 $820$ 个元素。

基点取 $r_0=r_{0,3}$。其稳定群 $N$ 由
$$\left\{I,\begin{pmatrix}t&3\\1&t\end{pmatrix}:t\in\mathbb F_{41}\right\}$$
以及这些元素左乘 $\operatorname{diag}(1,-1)$ 得到，共 $84$ 个射影元素。计算两 involution 的对跖对子交集即得到 (2.1) 的 $C$。

$N$ 在 $820$ 个项链上有 $21$ 个轨道，轨道长是一个 $1$、一个 $21$ 和十九个 $42$。取各轨道代表 $r_i$，径向矩阵为
$$Q_{ij}=\sum_{r\in O_j}C_{r_i,r}.
\tag{4.2}$$
每行和为 $420$，并有 $|O_i|Q_{ij}=|O_j|Q_{ji}$。这个 $21\times21$ 整矩阵是独立复算完整谱的一种小证书。下面进一步用字符和识别每一个因子，避免按多项式次数猜类型。

### 4.2 Principal series 的球函数

对偶字符 $\theta$，使用齐次函数模型
$$F(tv)=\theta(t)^2F(v),\qquad
(\pi_\theta(g)F)(v)=\theta(\det g)F(g^{-1}v).$$
其 $N$ 不变向量可取
$$F(x,y)=\theta(x^2-3y^2),\qquad F(1,0)=1.$$
Cartan 的不变性来自二次型的范数恒等式，正规化子反射的不变性来自 $\theta(-1)=1$。取
$$g_{a,s}=\begin{pmatrix}s&a\\0&1\end{pmatrix},\qquad
g_{a,s}r_0g_{a,s}^{-1}=r_{a,3s^2},$$
可直接算得 $(\pi_\theta(g_{a,s})F)(1,0)=\theta(s)^{-1}$。

$6$ 是 $\mathbb F_{41}^\times$ 的生成元。置
$$A_m=\sum_{a\in\mathbb F_{41}}C_{r_0,r_{a,3\cdot6^{2m}}},\qquad0\le m<20.$$
逐项计数得到
$$
(A_m)=(41,21,17,21,17,17,17,25,25,17,
25,17,25,25,17,17,17,21,17,21).
\tag{4.3}$$
将 $C$ 作用于上述不变向量并在 $(1,0)$ 取值，得到准确标量
$$\lambda_\theta=\sum_{m=0}^{19}A_m\theta(6)^{-m}.
\tag{4.4}$$
$s$ 和 $-s$ 给同一项链，因 $\theta$ 为偶字符，(4.4) 没有遗漏一个 $2$。当 $\theta$ 为平凡字符时得 $420$；当它为二次字符时，相应诱导表示的唯一 $N$ 不变线位于 $\mathrm{St}\otimes\chi_{41}$，得 $16$。

若 $\theta(6)=\zeta_d$，记 $c=\zeta_d+\zeta_d^{-1}$。其余值为
$$
\begin{array}{c|c}
d&\lambda_\theta\\\hline
4&32\\
5&12-16c\\
10&36\\
20&-4c^3-8c^2+16c+32.
\end{array}
\tag{4.5}$$
这些等式可直接将 (4.3) 模 $\Phi_d$ 化简验证，未使用浮点近似。

### 4.3 Cuspidal 的球函数，直接区分阶 $6,14,42$

在 $\mathbb F_{41^2}=\mathbb F_{41}(\sqrt3)$ 中，$\rho=4+\sqrt3$ 的像生成 $\mathbb F_{41^2}^\times/\mathbb F_{41}^\times$，其阶为 $42$。令 $\pi_\nu$ 的特征标为 $\chi_\nu$。$N$ 平均投影
$$e_N=\frac1{84}\sum_{n\in N}\pi_\nu(n)$$
秩为一，故球函数为
$$m_\nu(g)=\operatorname{Tr}(\pi_\nu(g)e_N)
=\frac1{84}\sum_{n\in N}\chi_\nu(gn).$$
于是
$$\boxed{\quad
\lambda_\nu=\frac1{84}\sum_{r\in G/N}C_{r_0,r}
\sum_{n\in N}\chi_\nu(g_rn),\quad}
\tag{4.6}$$
其中 $g_rr_0g_r^{-1}=r$。该式与代表选择无关，且 $m_\nu(1)=1$；因而没有附加的 $\dim\pi$ 因子。

为给 (4.6) 一个完全有限的证书，采用与 (4.4) 相同的 $g_r=g_{a,6^m}$。对每个 $g_rn$：标量矩阵贡献 $40$，非平凡 unipotent 贡献 $-1$，split regular 贡献 $0$；nonsplit regular 的一个特征值在上述射影乘法群中写为 $\rho^j$，则贡献 $-\nu(\rho)^j-\nu(\rho)^{-j}$。换另一个特征值只把 $j$ 换为 $-j$。

将前三类的常数项记为 $B$，最后一类按权重 $C_{r_0,r}$ 的计数记为 $H_j$。精确枚举给 $B=0$，以及
$$
\begin{split}
(H_j)=(&0,483,357,399,525,399,441,483,525,483,441,399,357,315,\\
&357,399,441,315,441,483,357,840,357,483,441,315,441,399,\\
&357,315,357,399,441,483,525,483,441,399,525,399,357,483).
\end{split}
\tag{4.7}$$
因此，当 $\nu(\rho)=\zeta_d$ 时，
$$\lambda_\nu=-\frac1{84}\sum_{j=0}^{41}H_j(\zeta_d^j+\zeta_d^{-j}).$$
模相应圆分多项式化简，记 $c=\zeta_d+\zeta_d^{-1}$，得到
$$
\begin{array}{c|c}
d&\lambda_\nu\\\hline
6&25\\
14&12c^2-4c+9\\
42&-4c^4+4c^3+20c^2-20c-3.
\end{array}
\tag{4.8}$$
这些是按明确局部字符确定的标量公式。特别地，阶 $14$ 和 $42$ 的识别并非仅由“三次、六次域的维数恰好匹配”得出。

## 5. 三种特征多项式及全部因子重数

定义
$$\begin{aligned}
F_2(X)&=X^2-40X+80,\\
F_3(X)&=X^3-83X^2+2035X-12769,\\
F_4(X)&=X^4-48X^3+544X^2-1792X+256,\\
F_6(X)&=X^6-94X^5+3159X^4-45828X^3\\
&\hspace{18mm}+275615X^2-613310X+212521.
\end{aligned}\tag{5.1}$$
$F_2,F_3,F_4$ 模 $3$ 不可约，$F_6$ 模 $11$ 不可约，故都在 $\mathbb Q$ 上不可约。脚本对这些有限域不可约性作精确核验。

由 (4.5)、(4.8) 的圆分 resultants，逐个表示的对应为：

| 类型 | $C$ 的标量或最小多项式 | 该类复表示数 | 每个在真实 $H^0(J,\Omega^1)$ 的重数 |
|---|---|---:|---:|
| trivial | $420$ | $1$ | $0$ |
| $\mathrm{St}\otimes\chi_{41}$ | $16$ | $1$ | $3$ |
| PS 阶 $4$ | $32$ | $1$ | $2$ |
| PS 阶 $5$ | $F_2$ 的两个根 | $2$ | $2$ |
| PS 阶 $10$ | $36$，两个不同表示有同一标量 | $2$ | $2$ |
| PS 阶 $20$ | $F_4$ 的四个根 | $4$ | $2$ |
| SC 阶 $6$ | $25$ | $1$ | $3$ |
| SC 阶 $14$ | $F_3$ 的三个根 | $3$ | $4$ |
| SC 阶 $42$ | $F_6$ 的六个根 | $6$ | $3$ |

这里 $\theta$ 与 $\theta^{-1}$ 给同一个表示，故对全部本原圆分根取 resultant 时，$F_d$ 出现平方。例如阶 $10$ 的 resultant 是 $(X-36)^4$，而径向特征多项式只含 $(X-36)^2$。不能将这两种重数混淆。

### 定理 5：层 41 的完整谱

径向矩阵的 $21$ 次特征多项式为
$$\det(X-Q)
=(X-420)(X-16)(X-25)(X-32)(X-36)^2F_2F_3F_4F_6.
\tag{5.2}$$
完整 $820$ 维项链置换模块的特征多项式为
$$\begin{split}
\det(X-C\mid U)={}&(X-420)(X-16)^{41}(X-32)^{42}
(X-36)^{84}(X-25)^{40}\\
&\cdot F_2^{42}F_4^{42}F_3^{40}F_6^{40}.
\end{split}\tag{5.3}$$
真实 $54$ 维 Jacobian 全纯微分空间上的特征多项式为
$$\boxed{\quad
\Psi(X):=\det(X-\varphi\lambda\mid H^0(J,\Omega^1))
=(X-16)^3(X-32)^2(X-36)^4(X-25)^3
F_2^2F_4^2F_3^4F_6^3.
\quad}\tag{5.4}$$
因而 R68 所需的真实 Rosati 倍率满足
$$\boxed{\det(X-\kappa\mid H^0(J,\Omega^1))=2^{54}\Psi(X/2).}\tag{5.5}$$

**证明。** 无重数置换分解使径向空间每个复表示恰给一条 $N$ 不变线，故 (4.5)、(4.8) 给 (5.2)；脚本还独立计算 (4.2) 的特征多项式核对该式。把各表示的实际维数 $1,41,42,40$ 代入，得 (5.3)。由引理 2 的真实对应连接及命题 4 的全纯重数，得到 (5.4)。最后用 (1.5)，每个标量乘 $2$，得到 (5.5)。证毕。

因此，(5.5) 的线性根为 $32,64,72,50$，重数分别为 $3,2,4,3$；非线性因子为 $\widehat F_i(X)=2^iF_i(X/2)$，其重数仍分别为 $2,4,2,3$（按 $i=2,3,4,6$ 排列）。这保留了每一个因子和乘数。

### 推论 6：极化分母的明确支撑

有
$$\boxed{\det(\kappa\mid H^0(J,\Omega^1))
=2^{108}3^8 5^8 113^8 461^6.}\tag{5.6}$$
所以 $\deg\kappa=2^{216}3^{16}5^{16}113^{16}461^{12}$。这里说的是 $J$ 上真实端同态 $\kappa$ 的次数，未给维数更大的源 $J_0\to J$ 虚构一个有限次数。

若 $\ell\notin\{2,3,5,113,461\}$，则
$$s=q^\dagger\kappa^{-1}\in
\operatorname{Hom}(J,J_0)\otimes\mathbb Z_{(\ell)},\qquad qs=1,
\tag{5.7}$$
且 $sq=e_0$ 在 $\mathbb Z_{(\ell)}$ 处为整。

**证明。** (5.1) 的常数项为 $80, -113^2, 2^8,461^2$。取 (5.4) 的常数项，并加上 (5.5) 的 $2^{54}$，恰得 (5.6)。$\kappa$ 为正 Rosati 对称的实 Hecke 元素，在 $H^{0,1}$ 上有相同特征值，故其作用于 $H^1$ 的行列式为 (5.6) 的平方，也就是其次数。

对不整除 (5.6) 的 $\ell$，Cayley–Hamilton 从 (5.5) 直接表达 $\kappa^{-1}$，分母是该常数项。因此 $\kappa^{-1}\in\operatorname{End}(J)\otimes\mathbb Z_{(\ell)}$，无需另求一个未知指数。代入 (1.5) 和 (1.6) 得 (5.7)。证毕。

## 6. 对实际高度输入的用途和边界

对一个实际新形式 $f$，先由 Mercuri–Schoof 的真实有限 $G$ 模 $V_f$ 确定 PS 或 SC 字符；再由 (4.4) 或 (4.6) 得其每个系数嵌入下的 $\kappa_f=2\lambda_f$。这提供 R68 (2.2) 的具体极化输入。并非只知道某个无标记多项式就宣称已将每个全局 Hecke 嵌入逐一编号。

仍须保留 R68 的微分坐标倍率：若标准新形式微分与目标微分满足 $q^*\omega_{J,f,\sigma}=a_{f,\sigma}\omega_{0,f,\sigma}$，则
$$\gamma_{J,f,\sigma}
=\frac{\sigma(\kappa_f)}{a_{f,\sigma}^2}\gamma_{0,f,\sigma}.$$
若明确用 $q^*$ 的逆像定义目标微分，才有 $a_{f,\sigma}=1$。选 $P_{J,f}=qP_{0,f}$ 作 Mordell–Weil 基时则为 $c_{J,f}=\kappa_fc_{0,f}$。本文的精确极化计算不消去规范平移 $\xi$ 和真实辅助局部高度。

层 41 的全部新、Fricke $+$ 因子属于 R45 的 $A$，所用非消失证据见 R57 对 DLF §5.3 的核查。因此本层可将 (5.4)–(5.7) 用于实际 $A=J$。一般 $p$，命题 1、引理 2 及字符和仍成立，但 R45 的维数下界不能保证某一完整类型块都落在 $A$。

配套脚本为 `scripts/necklace_chen_spectrum.py`。运行

```text
python topics/serre-uniformity/scripts/necklace_chen_spectrum.py 41
```

即可重建 $820$ 个非分裂 involution、$21$ 个轨道、径向矩阵、PS 与 SC 字符和、圆分 resultant、有限域不可约性、真实重数及 (5.6)。所有运算均为整数、有理数或有限域精确运算，不读取模形式数据库，不采用浮点特征值。仅需 SymPy；已有 python-flint 时用它加速特征多项式，缺少时回退到 SymPy。加 `--show-radial` 可打印整个 $21\times21$ 证书矩阵。

## 7. 已核对的原始来源

- M. Rebolledo and C. Wuthrich, **A moduli interpretation for the non-split Cartan modular curve**, *Glasgow Mathematical Journal* **60** (2018), 411–434，DOI [10.1017/S0017089517000180](https://doi.org/10.1017/S0017089517000180)。本次逐项核对的是 [2017-06-19 作者版本 PDF](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)，共 20 页：Corollary 3（p.4）的 $G/N$ 识别；§3.8、Proposition 14（p.12）的对跖 Gram 配对；§4.1、Theorem 15（pp.12–13）的真实对应和同源；§4.4–4.5（pp.15–16）的有限群作用及 $\varphi\lambda=C$；Lemma 22（p.18）的两条因子 $4$ 等式。本文没有把作者版本页码误记为刊物页码。
- P. Mercuri and R. Schoof, **Modular forms invariant under non-split Cartan subgroups**, *Mathematics of Computation* **89** (2020), 1969–1991，DOI [10.1090/mcom/3503](https://doi.org/10.1090/mcom/3503)，[作者持有的出版抽印本](https://reneschoof.github.io/mcom3503.pdf)。§2、Proposition 2.1（pp.1971–1972）的表示分类及 $T,S,N$ 不变量；§3–4（pp.1973–1976）的具体表示模型；§5、Proposition 5.1（pp.1976–1977）的全层诱导模和实际微分不变量；Proposition 5.2（p.1978）的全局新形式有限 $G$ 类型。本文第 3 节的重数另由等变 Euler 特征完整证明，没有以数据库维数代替它。
- R57、R59、R64 给层 41 的真实 Heegner 商及局部类型接口；R68 给标准新形式、Heegner 高度系数和一般同源极化传输。本文新补的是实际项链同源的倍率、按字符标记的层 41 精确谱，以及 (5.7) 的明确整投影。
