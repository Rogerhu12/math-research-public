# 有限 gauge 证书的纯代数边界：抛物线轨道模

日期：2026-11-12（UTC）。作者：literature。
状态：完整的代数反模型说明；不编号。
它不是实际 Hilbert 算子反例，也不是不变子空间问题的反例。

## 1. 要检验的逻辑范围

R166、R169、R173 已得到实际加性慢模式的：

- 忠实多项式演算与关系分类；
- 单方向非零多项式的无核接口；
- 有限 gauge 轨道证书；
- 有限族的共同核零及约化 Koszul 正合；
- gauge 协变。

下面给一个纯代数模型，说明这些性质若只按代数形式使用，即使若干项被加强为全域可逆或普通正合，仍不能迫使每个非零多变量多项式作用无核。

模型没有 Hilbert 范数、通常伴随、共同共轭或真实 $A$ 的表示。
所以它只排除不使用这些额外结构的纯代数收尾。

## 2. 加性半线性环

沿用 R166 的一个秩二独立形式设置：
$$
K\subseteq L=\mathbb C((z)),\qquad
\sigma_1,\sigma_2\in\mathbb C[[z]],
$$
其在 $L/K$ 中的类对 $\mathbb C$ 线性无关。
$\Gamma=\mu_{2^\infty}$ 在 $K$ 上以
$$
\alpha_\zeta c(z)=c(\zeta z)
$$
作用，且
$$
h_{\zeta,i}=\alpha_\zeta\sigma_i-\sigma_i\in K.
$$

令
$$
R=K[x,y],\qquad
\Lambda_\zeta F(x,y)
=(\alpha_\zeta F)(x+h_{\zeta,1},y+h_{\zeta,2}).
\tag{2.1}
$$
R166 已证明这是半线性群作用，
且 $R$ 无非零真 $\Gamma$ 稳定理想。

取不可约多项式
$$
P(x,y)=y-x^2.
$$
其轨道为
$$
P_\zeta
=\Lambda_\zeta P
=y+h_{\zeta,2}-(x+h_{\zeta,1})^2.
\tag{2.2}
$$
每个 $P_\zeta$ 对 $y$ 首一且一次，
因此
$$
R/(P_\zeta)\simeq K[t]
$$
是整环，并有分式域
$$
F_\zeta:=\operatorname{Frac}(R/(P_\zeta))\simeq K(t).
\tag{2.3}
$$
例如可用参数
$$
x=t-h_{\zeta,1},\qquad y=t^2-h_{\zeta,2}.
\tag{2.4}
$$

这些主素理想有无穷多个不同成员。
否则有限轨道的稳定子在 Prüfer 群中有有限指数；
该群没有真有限指数子群，因而整个群固定 $(P)$，
违反非零真稳定理想不存在。
也可直接从 (2.2) 的一次 $x$ 系数及非恒定 $\sigma_1(\zeta z)$ 看出无穷多不同因子。

## 3. 忠实模与非零多项式的真实代数核

定义代数直和
$$
\mathscr M=\bigoplus_{\zeta\in\Gamma}F_\zeta.
\tag{3.1}
$$
元素只有有限多个非零分量。
$R$ 在每个分量上通过商映射及域中的乘法作用，
从而得到交换的 $\mathbb C$ 线性算子表示
$$
\rho:R\longrightarrow\operatorname{End}_{\mathbb C}(\mathscr M).
$$

这个表示忠实。
若 $F\in R$ 作用为零，则它在每个 $F_\zeta$ 中的像都为零，
所以
$$
F\in\bigcap_{\zeta\in\Gamma}(P_\zeta).
$$
非零有限多项式在唯一分解环 $K[x,y]$ 中只有有限多个不同不可约因子，
不能被无穷多个不同的 $P_\zeta$ 整除。
故交理想为零，$\rho$ 单射。

但是
$$
\boxed{\ker\rho(P)\ne\{0\}.}
\tag{3.2}
$$
因为 $\zeta=1$ 分量为 $F_1=\operatorname{Frac}(R/(P))$，
$P$ 在这个整个非零分量上恒为零。

同时 $\rho(P)$ 不是零算子，因表示忠实且 $P\ne0$。
所以“演算忠实且多项式环无零因子”在此并未排除非零演算的向量核。

## 4. 全部非恒定仿射线性式的一变量多项式甚至可逆

取
$$
\ell(x,y)=ax+by+c,\qquad a,b,c\in K,\quad(a,b)\ne(0,0).
$$
在参数 (2.4) 下，
$$
\ell
=bt^2+at+(c-ah_{\zeta,1}-bh_{\zeta,2}).
$$
若 $b\ne0$，这是次数二的多项式；
若 $b=0$，则 $a\ne0$，是次数一的多项式。
因此它在每个分量上都对 $K$ 超越。

于是对任意非零 $q\in K[s]$，
$$
q(\ell)\ne0\quad\text{在每个 }F_\zeta\text{ 中}.
$$
域内乘以非零元素可逆。
对每个有限支撑向量逐分量取逆，仍得到有限支撑向量，
所以
$$
\boxed{
\rho(q(\ell)):\mathscr M\to\mathscr M
\text{ 是全域双射}.
}
\tag{4.1}
$$

这里强于仅有单射或某种稠密值域。
特别所有非零一变量多项式 $\rho(q(x))$、$\rho(q(y))$ 都可逆，
但二维关系 $P=y-x^2$ 仍有非零核。

非恒定条件不可删：
若 $\ell\in K$ 为常数，当然存在非零 $q$ 使 $q(\ell)=0$。

## 5. gauge 协变真实成立

$\Lambda_\eta$ 将 $(P_\zeta)$ 映到 $(P_{\eta\zeta})$，
所以诱导域同构
$$
F_\zeta\longrightarrow F_{\eta\zeta},
\qquad
[f]\longmapsto[\Lambda_\eta f].
$$
它对 $K$ 是 $\alpha_\eta$ 半线性的，
而 $\alpha_\eta$ 固定 $\mathbb C$，所以它是 $\mathbb C$ 线性的。

按这些同构置换 (3.1) 的分量，得到
$$
U_\eta:\mathscr M\longrightarrow\mathscr M.
$$
其逆为 $U_{\eta^{-1}}$，群律由 $\Lambda$ 的群律得到。
并且
$$
\boxed{
U_\eta\rho(F)U_\eta^{-1}
=\rho(\Lambda_\eta F).
}
\tag{5.1}
$$

这是真正的代数群协变，不只是各分量的无关命名。
但本稿没有定义 Hilbert 内积，所以不称 $U_\eta$ 为酉算子。

## 6. 有限轨道证书和普通 Koszul 正合仍成立

R166 的稳定理想结论给某个有限族 $\zeta_1,\ldots,\zeta_m$
和 $A_i\in R$，使
$$
\sum_{i=1}^mA_iP_{\zeta_i}=1.
\tag{6.1}
$$
作用在 $\mathscr M$ 上，得到实际代数算子恒等式
$$
\sum_i\rho(A_i)\rho(P_{\zeta_i})=I_{\mathscr M}.
\tag{6.2}
$$
所以该有限族共同核为零，且其值域之和等于整个模。

它的 Koszul 复形甚至普通正合。
若 $\delta$ 为系数 $\rho(P_{\zeta_i})$ 的内乘微分，
$h$ 为系数 $\rho(A_i)$ 的外乘同伦，
外代数反对易式给
$$
\delta h+h\delta=I.
\tag{6.3}
$$
因此每个闭合代数链已经是边界，不需要取任何拓扑闭包。

此外，非零 $K$ 元素在整个模上可逆；
在任何 $R$ 子模及其商上仍可逆，
因为这些都是 $K$ 向量空间。
所以基域分母在代数子商上的性质也没有缺失。

尽管如此，(3.2) 的单个非零轨道成员仍具有非零核。
有限族的证书并不矛盾。

## 7. 对实际研究的准确意义

此模同时具有：

- 忠实的交换多项式表示；
- 非恒定 $K$ 仿射线性式的全部非零一变量多项式全域可逆；
- 完整半线性 gauge 协变；
- 基域分母在代数子商上的可逆性；
- 有限轨道单位证书及普通 Koszul 正合；
- 单个非零二维多项式的非零向量核。

因此，R166、R169、R173 的纯代数部分，
不能只靠重新排列这些性质就推出全部多变量单核结论。

模型明确没有以下实际输入：

1. 没有 Hilbert 范数，故没有有界算子、强收敛或闭值域问题；
2. 没有共同共轭 $C$ 或通常伴随结构；
3. 没有真实 $A$ 的连续权、进位、循环向量及正交投影；
4. 没有 R164 的强*渐近交换和 Calkin 忠实性；
5. 没有把模的代数直和宣称为 Hilbert 闭直和。

所以本稿不否定真实模型的任何无核猜想，
也不提供实际 $A$ 的非平凡不变子空间。
它只是精确指出：若继续单核路线，必须使用仍未进入纯代数推导的实际 Hilbert 结构。
