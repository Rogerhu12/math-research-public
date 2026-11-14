# 真实整数流中的精确 Stokes 滤子与有限 Euler jet 代价

日期：2026-11-12。状态：本文的精确线性滤子障碍、Wronskian 及有限
Euler 滤子的最优归一化损失均已证明。这里没有排除一般非线性
vanishing-jet 格，也没有由一个滤子范围结论宣布主问题无解。

## 1. 与实际整数 ODE 相同的系数字段

使用 R57 的四变量流及其有限个固定 CM 缩放：

$$
u'=v,\quad v'=-2Du^3,\quad L'=Du^2,\quad\theta'=L\theta,
\qquad (u,v,L,\theta)(0)=(0,1,0,1).
\tag{1.1}
$$

可取参数 $D=1,16,-7+24i,-7-24i$，使实际 $A_1$ 是这些流坐标的
固定整多项式；也可附加 $D=17$ 的同一有限组。
令 $\mathcal F$ 为这些实际复亚纯函数和 $z$ 生成的有理函数域，
常数域为 $\mathbb C$。它在 $D_z=d/dz$ 下封闭，因为 (1.1) 为
多项式系统。任意固定有限组 CM 缩放的 sigma/theta 坐标都可再加入。

**增长引理。** $\mathcal F$ 中每个非零函数的 Nevanlinna 阶至多为 $2$。

**证明。** 椭圆 sigma 与 theta 可写成一个二次指数乘 Jacobi theta
级数。其绝对值由

$$
C e^{C|z|^2}\sum_{n\in\mathbb Z}
             e^{-c n^2+C|n||z|}\le C'(1+|z|)e^{C''|z|^2}
$$

控制，故它们的整函数阶至多为 $2$；任意固定复缩放不改变这个上界。
$u=\sigma/\theta=1/\sqrt{x}$ 在复平面为单值亚纯函数：$x$ 的零和极点
均为偶阶，所以平方根可穿过它们延拓；它通常在二倍格上而非原格上
周期。$v=u'=-yu^3$，$L=\theta'/\theta$ 也为亚纯函数。
theta 的导数由 Cauchy 估计具有相同的阶上界，椭圆 $x,y$ 亦可表示为
上述整函数及其导数的商。

Nevanlinna 特征满足
$T(r,fg)\le T(r,f)+T(r,g)$、
$T(r,f+g)\le T(r,f)+T(r,g)+O(1)$ 以及
$T(r,1/f)=T(r,f)+O(1)$；最后一个等式直接来自 Jensen 公式。
所以有限有理运算保持阶至多 $2$。
微分封闭性已经由 (1.1) 保证，不需要另假定一个无界的函数族。
$\square$

因此下文允许的系数包括真实整数 ODE 中的任意有理表达式，
不是只允许 $\mathbb C(z)$。但是没有把新的 incomplete-gamma 或
Stokes 模型本身偷偷加入系数字段。

## 2. 每个非中央模型都在该字段之外

固定 $d\ge3$、$a\in\mathbb C^\times$。对 $0<j<d$，定义

$$
E_0=e^{-az^d},\qquad
E_j=z^j\sum_{h\ge0}
      \frac{(-a)^hz^{dh}}{(j/d)_{\overline{h+1}}}.
\tag{2.1}
$$

这正是前篇 Stokes 分解的模型。令

$$
\mathscr L=D_z+ad z^{d-1}.
$$

逐系数或直接积分，准确有

$$
\mathscr LE_0=0,\qquad
\mathscr LE_j=d z^{j-1},\qquad
E_j(z)=d e^{-az^d}\int_0^z t^{j-1}e^{at^d}\,dt.
\tag{2.2}
$$

**引理。** $E_j$ 是阶准确为 $d$ 的整函数，因而 $E_j\notin\mathcal F$。

**证明。** 沿线段估计积分给
$|E_j(z)|\le C(1+|z|)^j e^{2|a||z|^d}$，故阶至多 $d$。
选一条射线 $z=r e^{i\phi}$，使 $a e^{id\phi}=-|a|$。
沿此射线，积分趋于非零常数

$$
e^{ij\phi}\int_0^\infty t^{j-1}e^{-|a|t^d}\,dt
 =\frac{e^{ij\phi}}d|a|^{-j/d}\Gamma(j/d).
$$

于是 $E_j$ 沿该射线增长为非零常数倍的 $e^{|a|r^d}$，阶至少 $d$。
整函数的最大模阶与 Nevanlinna 阶相同（由 Poisson/Jensen 的
$\log M(r)\le3T(2r)+O(1)$ 可直接比较），所以 §1 的上界排除其属于
$\mathcal F$。$\square$

只在 $\mathbb C(z)$ 上也可不使用增长：若 $E_j$ 有理，(2.2) 使它
不能有任何有限极点，故为多项式；最高次数与右边次数 $j-1<d-1$
矛盾。复增长论证将这个初等结论扩到了真实 ODE 字段。

## 3. 精确滤子必须同时消去中央模型

**定理。** 设 $P\in\mathcal F[D_z]$ 为有限阶线性微分算子。
如果 $P E_j=0$ 对某个 $0<j<d$ 成立，则 $P E_0=0$。
算子的阶数、系数和 $a,d$ 都可依赖 $p$；不存在统一阶数假设。

**证明。** 因 $\mathscr L$ 为首一的一阶算子，可作右 Euclidean 除法

$$
P=Q\mathscr L+r,\qquad Q\in\mathcal F[D_z],\quad r\in\mathcal F.
$$

应用于 $E_j$，得到

$$
0=P E_j=Q(dz^{j-1})+rE_j.
$$

若 $r\ne0$，右边强迫 $E_j=-Q(dz^{j-1})/r\in\mathcal F$，与 §2
矛盾。因此 $r=0$，而 $\mathscr LE_0=0$ 立即给 $PE_0=0$。
整个证明没有把未知的 Stokes 常数先当成非零代数数。$\square$

同一结论适用于有限表达式中允许的 $p$ 进常数系数：取这些有限个
常数生成的特征零有限生成域，选一个到 $\mathbb C$ 的域嵌入。
实际 ODE 与模型参数 $a$ 的 Taylor 系数为有理数，所以正式恒等式
在此嵌入下保持，继而适用上述增长与 Ore 论证。
这里不需要、也没有使用一个连续的 $p$ 进到复数的嵌入。

对实际惰性 $p$，$d=p+1\ge8$。前篇已经证明非中央常数
$\mathcal S_4\equiv1\pmod p$，所以它必非零。
因此若尝试以真实整数流的有理系数微分算子精确杀掉这一整块
$\mathcal S_4E_4$，也会杀掉待检测的 $E_0$ 模型。
这个结论比只在裸椭圆函数上限制系数更强，但仍限于精确的线性
微分消去，不涉及有限 jet 近似或一般非线性多项式关系。

## 4. 明确的 Wronskian：问题不是最低 jet 缺秩

令 $d=4r$，并记 $s=r-1$。Stokes 模型为
$E_0,E_4,\ldots,E_{4s}$。对 Wronskian 使用导数行 $0,\ldots,s$。
有完全显式的等式

$$
\boxed{\quad
W(E_0,E_4,\ldots,E_{4s})
 =d^s4^{s(s-1)/2}\left(\prod_{m=1}^{s-1}m!\right)
   z^{3s(s+1)/2}E_0.
\quad}
\tag{4.1}
$$

**证明。** 若首列是非零函数 $f$，则

$$
W(f,f_1,\ldots,f_s)
 =f\,W\bigl((D_z-f'/f)f_1,\ldots,(D_z-f'/f)f_s\bigr).
$$

可先把每列除以 $f$，再展开常数首列来证明这个恒等式。
取 $f=E_0$，由 (2.2) 变成 $E_0W(dz^3,dz^7,\ldots,dz^{4s-1})$。
单项式 Wronskian 是其指数的 Vandermonde：指数差给
$4^{s(s-1)/2}\prod_{m=1}^{s-1}m!$，总次数是
$\sum_{l=1}^s(4l-1)-s(s-1)/2=3s(s+1)/2$。$\square$

当 $d=p+1$ 时，(4.1) 的数值前因子是 $p$ 进单位，因为 $s<p$。
等价地，在次数 $0,4,\ldots,d-4$ 取系数的最低 jet 矩阵是三角形，
对角为 $1,d/4,d/8,\ldots,d/(d-4)$，全部为单位。
所以不能将 §3 的障碍解释为这些最低 jet 向量本身不独立。

若允许把 $E_4,\ldots,E_{4s}$ 自己加入系数，当然可以用其 Wronskian
构造一个精确滤子而保留 $E_0$；§3 说明这样的系数不在原来的
整数流字段里。它也不能免费继承原流的整体整性或收敛界。

## 5. 有限 Euler jet 滤子的最小归一化损失

有限截断仍可实际构造滤子。记 $\mathscr E=zD_z$，对整数 $M\ge1$ 置

$$
\mathcal N_{p,M}=\{n:1\le n\le M,\quad4\mid n,\quad d\nmid n\},
$$

$$
P_{p,M}(X)=\prod_{n\in\mathcal N_{p,M}}(X-n)\in\mathbb Z[X].
\tag{5.1}
$$

算子 $P_{p,M}(\mathscr E)$ 准确杀掉次数 $\le M$ 的全部非中央单项式。
由于 $z'=1$，它确实属于原整数 ODE 加上坐标 $z$ 后的整微分算子。

设 $Q(X)\in\mathbb Z_p[X]$ 也杀掉这些单项式，即 $Q(n)=0$ 对所有
$n\in\mathcal N_{p,M}$ 成立。逐个用首一因子 $X-n$ 作整系数除法，得

$$
Q=P_{p,M}V,\qquad V\in\mathbb Z_p[X].
\tag{5.2}
$$

因此对任意中央次数 $m\in d\mathbb Z_{\ge0}$，都有最优界

$$
\boxed{\quad
v_p(Q(m))\ge
\sum_{n\in\mathcal N_{p,M}}v_p(m-n)=:\gamma_p(m;M).
\quad}
\tag{5.3}
$$

该界由 $Q=P_{p,M}$ 取得，故不是一个松估计。
为使中央系数的乘子成为单位，至少要支付 $p^{-\gamma_p(m;M)}$
这一归一化，不能把滤子整系数与其目标值原始性混为一谈。

对中央常数 $m=0$，有尤其简洁的准确公式

$$
\boxed{\quad
\gamma_p(0;M)
 =v_p(\lfloor M/4\rfloor!)-v_p(\lfloor M/d\rfloor!).
\quad}
\tag{5.4}
$$

这是将所有正四倍数的乘积除以其中的正 $d$ 倍数；$4,d$ 都是单位。
第一笔损失恰发生在 $M=4p$：非中央指数 $4p$ 已是 $p$ 的倍数。
所以当 $M\ge4p$ 时，不存在同时满足这些消去条件而又 $Q(0)$ 为单位
的整 Euler 多项式滤子。

更一般地，若 $m=dh\le M$、$h\ge1$，令
$U=\lfloor M/4\rfloor$、$V=\lfloor M/d\rfloor$，则

$$
\gamma_p(dh;M)
 =v_p((rh-1)!)+v_p((U-rh)!)
    -v_p((h-1)!)-v_p((V-h)!).
\tag{5.5}
$$

确实，先取全部 $1\le k\le U$、$k\ne rh$ 的差 $(rh-k)$，再除去
$k=r\ell$、$\ell\ne h$ 的差；$r=d/4$ 为单位。
例如对第一中央次数 $m=d$，第一笔损失恰在
$M=d+4p=5p+1$ 发生。此时 $M/4=r+p$，(5.5) 的第一分子阶乘才含
一个 $p$，而分母尚不含 $p$。

这些是可直接用于实际前缀 jet 矩阵的整数算子及准确饱和成本。
它们只给 Euler 多项式这一明确子类的最优代价；一般包含多个 ODE
坐标的非线性 vanishing-jet 矩阵，仍须计算其真实前缀行格和 minors，
不能用 (5.4) 替代整个更大格的结论。

## 6. 饱和有限 jet 投影确实存在，但它属于除幂算子

不能把 §5 的 $\mathbb Z_p[X]$ 限制扩大到所有整 jet 算子。
下面给一个实际的原始投影，说明这个区别。

记 $r=d/4$、$M_4=\lfloor M/4\rfloor$，令整数函数

$$
\epsilon(n)=\begin{cases}1,&r\mid n,\\0,&r\nmid n.\end{cases}
$$

取其 Newton 插值多项式

$$
Q_{p,M}(Y)=\sum_{k=0}^{M_4}\Delta^k\epsilon(0)\binom Yk
 \in\mathbb Q[Y].
\tag{6.1}
$$

所有 $\Delta^k\epsilon(0)$ 都是整数，且对 $0\le n\le M_4$，
$Q_{p,M}(n)=\epsilon(n)$。于是

$$
\Pi_{p,M}=Q_{p,M}(\mathscr E/4)
\tag{6.2}
$$

在只含四倍数次幂、截断次数 $\le M$ 的 jet 空间上，准确是中央
$d$ 倍数次幂的投影。在普通系数基或 Hurwitz 基上，它的矩阵都只是
相同的 $0/1$ 对角矩阵。因此它的范数为 $1$，像与核均为饱和整格；
其非零 minors 为单位。这是具体有限投影，不是仅声称存在。

形式算子可写为除幂形式

$$
\binom{\mathscr E/4}{k}
 =\frac1{k!}\prod_{l=0}^{k-1}(\mathscr E/4-l).
$$

它在四倍数 monomial 上的特征值为整数 $\binom nk$，所以即使算子
系数带 $k!$ 分母，仍保持该整 jet 格。对于全幂次的相似构造，
$\binom{\mathscr E}{k}=z^kD_z^k/k!$ 给同样的直接验证。

§5 的代价并未消失，而是成为原全局 Euler 多项式表达的分母。
若 $p^tQ_{p,M}(X/4)\in\mathbb Z_p[X]$，因为其常数项为 $p^t$，
(5.3) 强迫

$$
t\ge\gamma_p(0;M).
\tag{6.3}
$$

例如 $M=4p$ 时，在 (6.1) 中

$$
\Delta^p\epsilon(0)
 =\sum_{l=0}^{3}(-1)^{p-lr}\binom p{lr}\equiv-1\pmod p,
$$

因为 $p=4r-1$。所以最高项确实带一个 $p$ 分母，而所有更低
Newton 项的 $k!$ 为单位。这是 (6.3) 首次出现的明确实例。

它还能由真实 ODE 给出全局候选。对固定 Euler 原函数
$\mathscr H$，有 $\mathscr E\mathscr H=A$，故

$$
\Pi_{p,M}\mathscr H
 =\mathscr H+P_{p,M}^{\mathrm{flow}}(z,u_j,v_j,L_j,\theta_j),
\tag{6.4}
$$

其中 $P_{p,M}^{\mathrm{flow}}$ 是一个有理系数多项式，可逐次用
R57 的整导子实际生成：在 (6.2) 展开后，以
$\mathscr E^k\mathscr H=\mathscr E^{k-1}A$ 替换每个 $k\ge1$。
所以这不是只能在数值 jet 上定义的抽象操作。
但 (6.3) 仍是其 Euler 表达必须追踪的分母；在更大 ODE 多项式格中
是否有额外整关系消去这些分母，需要另证。

这个最直接构造的算子阶数至多 $M_4$，而任何标量 Euler 多项式
若杀掉指定非中央次数，其次数至少为
$M_4-\lfloor M/d\rfloor$。使用 R57 的向量场，每次微分使总次数
至多增加 $2$，再乘 $z$ 至多再增 $1$，所以 (6.4) 的直接全局多项式
次数至多为一个固定常数加 $3M_4$。这是线性阶数／线性截断的
明确构造，并没有给低次数、远高接触阶的全局截面。

最后，令 $M\to\infty$ 时，这些有限投影在逐系数意义下趋于 $P_0$，
但 $P_0$ 依赖 $d=p+1$，也不是环同态：它可同时杀掉 $z^4$ 与某个
互补幂，却保留它们乘积 $z^d$。
对一般多项式 $F(\mathscr H,\text{流坐标})$，不能把对 $\mathscr H$
逐系数投影替换成对整个原 vanishing-jet 矩阵的一个固定基变换。
真实前缀核、全局截面次数和系数分母仍须一起计算。

## 7. 对继续研究的准确输入

现在有两个不同而互补的结论：§3 排除了原固定流系数字段内的精确
线性滤子；§5–6 给出了有限 Euler 滤子的实际公式、饱和 jet 投影及
其全局多项式表达所需归一化。
它们仍允许使用随截断增长的非线性整格，或另一个真正代数的
Frobenius/period 比较。若推进后一条，必须证明它保持实际中央投影，
而不是因为 §4 的最低 jet 行列式为单位就先认定所有高 jet 原始。

依赖的既有结论：R57 的固定整数流；
[全余类 Stokes 分解](2026-11-12-inert-euler-primitive-stokes-decomposition.md)
中的模型、真实余项界和 $\mathcal S_4\equiv1\pmod p$。
