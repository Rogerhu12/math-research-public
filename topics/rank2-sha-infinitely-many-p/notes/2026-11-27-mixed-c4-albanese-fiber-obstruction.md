# 原双椭圆 mixed C4 候选到 S 的 Albanese 纤维障碍

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明的方向筛选。** 本笔记排除一个此前仅作为候选的映射：
由原二挠谱曲线的双椭圆 involution 构成的 mixed order4 商，
不能有到原 $I_9/I_3$ 曲面 $S$ 的 dominant rational map。
特别不能把它的 genus2 Albanese 纤维擅自赋予一个到原 $S$ 纤维的
degree3 商。这里只关闭这个明确候选；不排除其它真实对应。

## 1. 原曲线、实际双覆盖和两个分歧点

沿 R1029 取
$$
 C:w^2=(z^3-4)(z^3-16),\qquad
 \iota(z,w)=(4/z,8w/z^3).
$$
其实际双椭圆商可写为
$$
 r:C\longrightarrow E_+,\qquad E_+:V^2=U^3-432,
$$
$$
 U=\frac{12(z^2+z+4)}{(z+2)^2},\qquad
 V=\frac{36w}{(z+2)^3}.
 \tag{1}
$$
代入原方程核得 $V^2=U^3-432$，两函数被 $\iota$ 固定。
由 $U$ 的次数及 $C$ 的函数域可知这是 degree2 商，不是仅有
相同 $j$ 的替代曲线。

$\iota$ 的不动点须 $z^2=4$。
在 $z=2$，$w^2=-32$，$\iota$ 保持 $w$，得到两个不动点；
在 $z=-2$，$\iota$ 把非零 $w$ 取负，没有不动点。
故全部分歧像正是
$$
 P_0=\left(\frac{15}{2},\frac{9\sqrt{-2}}4\right),\qquad -P_0.
 \tag{2}
$$
没有漏掉无穷点；degree2 Riemann–Hurwitz 也给总分歧数2。

$P_0$ 为非挠点。事实上在 $\mathbf Q(\sqrt{-2})$ 上作准确同构
$$
 x=-U/2,\qquad y=-\sqrt{-2}\,V/4,
$$
得到 $y^2=x^3+54$，而(2)的像是
$$
 (-15/4,\,9/8)\in\{y^2=x^3+54\}(\mathbf Q).
$$
Lutz–Nagell 的整性结论说明这不是挠点。
所以 $2P_0,4P_0$ 都非挠。

## 2. mixed 商的真实 Albanese 纤维

在 $C\times C$ 上令
$$
 \tau(P,Q)=(\iota Q,P),\qquad \tau^4=1.
$$
令 $X$ 为该 order4 商的任意光滑射影解消。
映射
$$
 b=r(P)+r(Q)\in E_+
 \tag{3}
$$
被 $\tau$ 固定，因而给 $X\to E_+$。

其一般纤维在取商前是
$r(P)+r(Q)=b$ 的光滑曲线。投影到第一个 $C$ 是双覆盖，
在 $r(P)=b\mp P_0$ 的四个点分歧，故亏格为5。
只要 $b\notin\{0,2P_0,-2P_0\}$，这些分歧点彼此不同，
且 $C\times C\to E_+$ 在该纤维上平滑：
临界点只能使两个 $r$ 的微分同时为零，恰给这三个和。

同样在这个开集上，order4 作用无不动点。
$\tau$ 不动要求 $P=Q$ 且 $P$ 为 $r$ 的分歧点，给
$b=\pm2P_0$；$\tau^2=(\iota,\iota)$ 的不动点给
$b=0,\pm2P_0$。所以该开集上的商是一族真正光滑 genus2 曲线，
由
$$
 (2\cdot5-2)/4=2
$$
直接得亏格2。因此其 Jacobian 在以下三个点之外都有好约化：
$$
 \boxed{\{0,2P_0,-2P_0\}.}
 \tag{4}
$$
不需要断言这三点的具体退化型，包含关系(4)已足够。

另外 $H^0(C,\Omega^1)$ 的 $\iota=+1$ 部分是一维。
$\tau$ 在两个 $C$ 因子的微分上交换并作用 $\iota$，
其不变部分恰是该一维的对角部分。
所以 $q(X)=1$，(3)诱导 Albanese 到 $E_+$ 的一个同源。
一般纤维连接（上面的分歧双盖及其商都连接），故实际上这是
Albanese 纤维化，至多差原点平移。

## 3. 好 Jacobian 的椭圆商不能产生原乘法坏纤维

假设有 dominant rational map $X\dashrightarrow S$，
其中原 $S\to B$ 的两坏纤维位于
$T=(0,0),-T=(0,-1)$，分别为 $I_9,I_3$。
因为映射 dominant，$H^0(S,\Omega^1)\to H^0(X,\Omega^1)$
非零。两个 Albanese 都一维，故在(3)的基上它诱导
$$
 h:E_+\longrightarrow B
$$
的非零同源再接平移。记同源次数为 $d\ge1$。
其一般纤维上的映射是从 genus2 曲线到相应原椭圆纤维的非恒定映射。

在(4)之外，源 genus2 Jacobian 有好约化。椭圆曲线若是其非零商，
也有好约化：例如选择一个不同于剩余特征的 $\ell$，椭圆的
$H^1_{\rm et}$ 是该 Jacobian $H^1_{\rm et}$ 的直和子表示，
所以它的惯性作用平凡。这里是在特征零曲线基上的局部场；
也可直接以乘法纤维的非平凡 unipotent monodromy 得矛盾。

$h$ 是特征零的 étale 基映射。因此原 $I_9,I_3$ 的所有原像仍是
乘法坏约化，不能变成好纤维。这迫
$$
 h^{-1}\{T,-T\}\subset\{0,2P_0,-2P_0\}.
 \tag{5}
$$
左侧有 $2d$ 个不同点，故 $d\ge2$ 不可能。

若 $d=1$，左侧的两个点之差经 $h$ 变成 $2T$，是非零三挠。
但(4)中任何两个不同点之差是
$\pm2P_0$ 或 $\pm4P_0$，均非挠；同源不能把非挠点送成挠点。
这也矛盾。因此
$$
 \boxed{X\dashrightarrow S\text{ 的 dominant rational map 不存在}.}
 \tag{6}
$$

解消 rational map 的基点不改变一般 genus2 Jacobian 的好约化，
也不改变 Albanese 同源，所以不能用添上例外曲线避开此论证。
该排除不涉及 R1043 由原二同源和 $S_3$ 谱盖构造的真实对应及
新曲面 $\mathscr S'$；后者有完整方程和截面左逆，来源不同。
