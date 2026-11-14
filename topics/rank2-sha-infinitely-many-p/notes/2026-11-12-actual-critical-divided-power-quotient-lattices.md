# 实际临界行的除幂商格与原 Frobenius frame 指数

日期：2026-11-12。状态：下面的实际评价映射、有限商、饱和格、
全部 Smith 指数及固定挠点投影后的端点原始性均已证明。
没有把这些环境格指数当作唯一指定临界系数的净损失，也没有
由此证明无穷多个素数的非零性。

本篇接合
[真实整 Frobenius](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)、
[Sym$^p$ 实际混合行](2026-11-12-gm-symmetric-power-bockstein-and-torsion-projection.md)
与
[固定 GM 束的 jet 格](2026-11-12-gm-bundle-jet-lattices-and-hodge-index.md)。
以下只取惰性 $p\ge7$，所有构造使用同一实际 Legendre 秩二 GM 束。

## 1. 从实际矩阵取得的两个坐标

令 $s=1-4t^2$。R68 的实际条目给

$$
U=\frac{F_{12}}{pa_ps},\qquad
V=-\frac{F_{22}}{b_ps},\qquad
H=V/t,
$$

其中 $a_p,b_p$ 是单位，且

$$
U,H\in1+t^2\mathbb Z_p[[t]],\qquad
B=U/H=1-t^2+\cdots,\quad b=B-1.
$$

实际固定 $M_1=t^4+\cdots$ 已在全部目标素数处整。置

$$
W=\frac{M_1U}{sH^2}=t^4+\cdots,\qquad
T=\frac{M_1U}{sH^{p+2}}=W/H^p.
\tag{1.1}
$$

这些是实际函数；$T$ 和 $U,H$ 依赖 $p$。把公共整单位 $s$ 及常数
$a_p,b_p$ 去掉后，原 Frobenius frame 的两个坐标是 $(pU,tH)$。
实际新坐标为

$$
X=H,\qquad Y=U-H,
\qquad
\binom X Y=
\begin{pmatrix}0&t^{-1}\\p^{-1}&-t^{-1}\end{pmatrix}
\binom{pU}{tH}.
\tag{1.2}
$$

因此它明确包含源 Hodge 的除 $p$ 以及 $V$ 的一阶零点所容许的
除 $t$，不只是原 frame 中的一个整可逆换基。

以下“对称幂格”均指所列 frame 中的**常系数齐次多项式格**及其
明确有限评价像。没有把它说成整个 $R$ 模评价的相同秩商；若允许
任意 $R=\mathbb Z_p[[t]]$ 系数，$Y=bX$ 会给额外关系。

## 2. 真实对称幂的有限商准确是完整临界 jet 格

令

$$
x=t^2,\qquad r=(p-3)/2,\qquad
\mathcal J=x^2\mathbb Z_p[x]/(x^{r+3}).
\tag{2.1}
$$

这是次数 $t^4,t^6,\ldots,t^{p+1}$ 的普通偶 jet 格，秩 $r+1$。
定义实际的齐次评价

$$
\operatorname{ev}_p:
\operatorname{Sym}^p(\mathbb Z_pX\oplus\mathbb Z_pY)
\longrightarrow\mathbb Q_p[[t]]/(t^{p+2}),
\qquad P\longmapsto T\,P(H,U-H).
\tag{2.2}
$$

它的单项式像准确为

$$
\operatorname{ev}_p(X^{p-j}Y^j)=Wb^j.
\tag{2.3}
$$

因为 $W=x^2+\cdots$、$b=-x+\cdots$，$j>r$ 的像在当前 jet 中为零，
而 $j=0,\ldots,r$ 的系数矩阵在 $x^2,\ldots,x^{r+2}$ 上为三角形，
对角元是 $(-1)^j$。故它不是只有模 $p$ 满秩，而是准确的整同构

$$
\operatorname{span}_{\mathbb Z_p}
 \{X^{p-j}Y^j:0\le j\le r\}
 \xrightarrow{\sim}\mathcal J.
\tag{2.4}
$$

源端截断核恰由 $j>r$ 的单项式生成。记这个实际对称幂像为
$\mathcal L_{\rm sym}$，则 $\mathcal L_{\rm sym}=\mathcal J$；
全部普通系数前缀都是实际饱和的三角格。

## 3. 除幂格的两端点只剩下一层 $p$

在同一特征零齐次空间中，除幂格为

$$
\Gamma^p=\operatorname{span}_{\mathbb Z_p}
 \left\{\frac{X^{p-j}Y^j}{(p-j)!j!}:0\le j\le p\right\}.
\tag{3.1}
$$

它按除幂加法公式对整线性换基稳定。对 $0<j<p$，分母是 $p$ 单位；
两个端点的分母 $p!$ 各含一层 $p$。所以
$\operatorname{Sym}^p\subset\Gamma^p$ 的完整商有长度 $2$。

在当前实际 jet 中，$Y^p/p!$ 的像阶数为 $2p+4$，完全消失；
$X^p/p!$ 的像则是 $W/p!$。因此除去单位阶乘后，实际像准确为

$$
\boxed{\quad
\mathcal L_\Gamma
=\mathbb Z_p\frac Wp
 \oplus\bigoplus_{j=1}^{r}\mathbb Z_p Wb^j,
\qquad
\mathcal L_\Gamma/\mathcal L_{\rm sym}\simeq\mathbb F_p.
\quad}
\tag{3.2}
$$

相对于普通 jet 格 $\mathcal J$，其 Smith 指数准确是一个 $-1$
及 $r$ 个 $0$。尤其剩下的 $p^{-1}$ 是这个明确评价商中真实的一层，
没有被未检查的饱和步骤吸收。

实际临界元素本身是除幂格中的原始元素

$$
\frac{(X+Y)^p}{p}=(p-1)!\,\gamma_p(X+Y).
$$

其像为

$$
\frac{WB^p}{p}
=\frac Wp+\sum_{j=1}^{r}\frac{\binom pj}{p}Wb^j
\quad\text{在 }\mathcal J\otimes\mathbb Q_p\text{ 中}.
\tag{3.3}
$$

所有混合系数均整，而 $W/p$ 的坐标为 $1$，故 (3.3) 在
$\mathcal L_\Gamma/\mathcal L_{\rm sym}$ 中非零。它的首项是
$t^4/p$；仅其指定的末项
$[t^{p+1}]WB^p/p=C_{p+1}/p$ 因实际算术整除而为整。
不能把该末项的整性当作整个源元素已落回 $\mathcal L_{\rm sym}$。

## 4. 原 Frobenius frame 的实际偶评价格

现在仍用同一个公共前因子 $T$，但直接评价原坐标 $(pU,tH)$：

$$
T\,(pU)^{p-j}(tH)^j.
\tag{4.1}
$$

若坚持使用未归一的原条目 $(F_{12},F_{22})$，各列只另外乘常数
$a_p^{p-j}(-b_p)^j$ 及公共函数 $s^p$。常数是单位；而在本临界
截断中 $s^p\equiv1\pmod p$，因为其首个可能非零 Frobenius 项
在 $t^{2p}$。乘 $s^p=1+ph$ 不但保持 $\mathcal J$，也保持
$\mathcal L_\Gamma$：它把 $W/p$ 变成 $W/p+hW$，逆操作同样整。
所以以下相对于两个格的 Smith 指数也适用于真正的原矩阵条目，
没有把一个任意函数换基默认当作同一常系数 section space。

由于 $T,U,H$ 都为偶函数，明确的 even 投影杀掉奇 $j$。
对 $j=2k$，准确有

$$
T\,(pU)^{p-2k}(tH)^{2k}
=p^{p-2k}W x^kB^{p-2k}.
\tag{4.2}
$$

$k>r$ 的像超过目标次数。对 $k=0,\ldots,r$，
$W x^kB^{p-2k}$ 的首项为 $x^{k+2}$，所以去掉所列 $p$ 幂后的
矩阵为整三角单位矩阵。记实际旧像为 $\mathcal L_{\rm old}$，得到

$$
\boxed{\quad
\mathcal L_{\rm old}\subset\mathcal L_{\rm sym}=\mathcal J,
\qquad
\operatorname{Smith}(\mathcal L_{\rm old},\mathcal J)
=(3,5,\ldots,p).
\quad}
\tag{4.3}
$$

指数长度准确为

$$
\sum_{k=0}^{r}(p-2k)
=(r+1)(p-r)=\frac{(p-1)(p+3)}4.
\tag{4.4}
$$

这已经是在同一真实临界 jet 中，经过明确 even 投影和截断后得到的
格指数；不是用整个对称幂的环境维数猜测它。

### 4.1 在同一除幂基中消元

为比较 $\mathcal L_{\rm old}$ 与 $\mathcal L_\Gamma$，不能仅把
两个指数相加后猜全部 Smith 因子。使用 (3.2) 的明确基即可准确消元。

$b=-x+\cdots$ 有整形式逆 $x=-b+\cdots$。对 $k\ge1$，

$$
x^kB^{p-2k}=(-1)^kb^k+O(b^{k+1}),
$$

所以旧格第 $k$ 列在除幂基中仍为 $p^{p-2k}$ 乘整列，首个非零
系数是单位，且没有 $W/p$ 分量。
对 $k=0$，在当前截断中

$$
p^pWB^p
=p^{p+1}\left(\frac Wp+
       \sum_{j=1}^{r}\frac{\binom pj}{p}Wb^j\right).
\tag{4.5}
$$

因为 $r<p$，每个所用 $\binom pj$ 都被 $p$ 整除；右侧括号为
首坐标 $1$ 的整列。于是整个矩阵准确分解成一个三角整单位矩阵乘

$$
\operatorname{diag}(p^{p+1},p^{p-2},p^{p-4},\ldots,p^3).
$$

因此

$$
\boxed{\quad
\operatorname{Smith}(\mathcal L_{\rm old},\mathcal L_\Gamma)
=(3,5,\ldots,p-2,p+1).
\quad}
\tag{4.6}
$$

最后的 $p\mapsto p+1$ 来自同一基中的实际二项式消元，未假设不同
饱和商的基可自动相容。

## 5. 原来的固定挠点投影不取消这层端点

R66 的两个 $256$ 标签和、旋转线性组合及准确归一化，只作用于
$M_1$ 的代数系数；$U,H,B$ 是公共 GM 函数。这些操作与 (2.2)
中的所有公共因子严格交换。投影后已经是本文所用的
$M_1=t^4+\cdots$，其首系数为 $p$ 单位。

因此 (2.4) 的三角单位、(3.2) 的 $W/p$ 原始端点、以及 (4.3)–(4.6)
都在**原实际投影之后**成立。固定角色正交并未把这一端点再变成
$p$ 的倍数。混合项同样保持实际三角秩；其总和可能在指定末项
发生抵消，正是仍待控制的算术问题。

## 6. 真正最后一个 vanishing jet 的准确范数

在各自所列的源商格中，先令 $x^2,\ldots,x^{r+1}$ 的全部前缀
系数准确为零，再取最后的 $x^{r+2}$ 系数。采用所列源基的系数
最大范数，$|p|_p=p^{-1}$。

对 $\mathcal L_{\rm sym}$，单位三角性迫使前 $r$ 个源坐标为零，
只剩原始基元 $Wb^r$。对 $\mathcal L_\Gamma$，第一行 $x^2$
首先迫使 $W/p$ 的坐标为零；随后同样只剩 $Wb^r$。
两者在最后系数的像都准确为

$$
\mathbb Z_p\,x^{r+2},
$$

所以真实最后 vanishing jet 的算子范数都为 $1$。

对原 frame 的商格，(4.2) 的三角性同样迫使 $k<r$ 的全部源坐标
为零，只留下 $k=r$ 的原始源基元，其像为

$$
p^3W x^rB^3=p^3x^{r+2}
\quad\text{在当前截断中}.
$$

故它的最后系数像准确为 $p^3\mathbb Z_p x^{r+2}$，最后 vanishing
jet 的算子范数为 $p^{-3}$。这是各自原 source quotient 格上的准确
范数；若先把旧评价像整体饱和成 $\mathcal J$，就已改变了源范数。

因此三种真实最后 vanishing 行的范数分别是

$$
\boxed{\quad 1,\quad1,\quad p^{-3}
\qquad(\mathrm{Sym},\Gamma,\mathrm{old}).\quad}
\tag{6.1}
$$

除幂端点的一层 $p^{-1}$ 不参与最后这个前缀核。
这并不计算所选单个元素 $\gamma_p(X+Y)$ 的末系数：
(3.3) 的 $W/p$ 坐标是 $1$，它本来就不属于这个 vanishing 前缀核。
两种问题不能互相替代。

## 7. 这一比较实际解决了什么

现在，指定非线性临界行已有一个明确的实际张量和有限商格：
对同一真实 Frobenius frame 作 (1.2) 的修改，取其常系数
$\Gamma^p$，通过 (2.2) 评价，再取规定的偶临界 jet。实际行是
(3.3) 中的那个原始除幂元素，其余下的 $p^{-1}$ 指数准确为 $1$。

同时，(4.3)–(4.6) 给出了原 frame 的同一评价像相对它的全部指数。
这些是指定有限格的精确事实，不能直接称为唯一数
$C_{p+1}/p$ 的净损失：公共前因子和新 frame 依赖 $p$，源空间的
次数是 $p$，而只取末系数与保留整个 vanishing-jet 前缀是不同操作。

后续仍需利用固定全局对象控制 (3.3) 的**指定末系数**，而不是仅
利用整个像中存在原始元素或最高混合项为单位。本文所给格与
精确指数可用于那一步的真实预算，但没有替代它。
