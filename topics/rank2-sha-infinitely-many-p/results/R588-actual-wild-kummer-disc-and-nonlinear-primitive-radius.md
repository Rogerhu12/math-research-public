# R588 — 原 wild Kummer 圆盘上的七积分独立与全非线性半径障碍

日期：2026-11-14。**状态：已证明。**

本篇将 R580 的常数线性障碍推进到真正多项式。
在原 sigma 决定的、次数准确为 $p$ 的 wild Kummer 域上，
R575 的七个实际积分仍然代数独立。
因此，任何真正含这些积分的原九坐标多项式，
即使系数依赖 $p$，并乘除任意整数次原 Gaussian，
都恰有原坏半径，而且不属于该闭边界的 Tate 代数。

这里的基域包含原 $S_{34},T_{72}$ 和 degree $136$ 来源，
后者记为 $S_{136}$；它不是原函数 $U_{\ell,r}$。
结论没有给这些来源或乘积新增中央零，
也没有将解析半径等同于有限饱和前缀的 jet 范数。
原 R578 的同一 $\mathcal D_\psi$ forcing、同一个 $R$、
两条十三行与真正 $d_2$ 继续开放。

## 1. 原固定来源与整个闭半径区间

保持同一个 $b=17$ 模型及加法坐标：
$$
y^2=x^3+b,\qquad D_zx=2y,\qquad D_zy=3x^2,\qquad
D_z^2\log\sigma=-x,
$$
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6.
\tag{1}
$$
所有积分仍取零初值。固定
$$
p\equiv5\pmod6,\qquad p>19,\qquad d=p+1,
$$
$$
c=[z^d]\log(\sigma/z),\qquad a=6c,\qquad
S=p^{-p/(p^2-1)},\qquad \rho=p^{-1/(2p)}.
\tag{2}
$$
R301 经同一个 $b=17$ 单位缩放给
$v_p(c)=v_p(a)=-1$，并且 $S<\rho$。
$c$ 是这个实际 sigma 的系数，不是可调的 Gaussian 参数。

令
$$
\mathscr E=\exp(cz^d),\qquad
H_\sigma=\frac{\sigma}{z\mathscr E}.
\tag{3}
$$
先按形式幂级数理解 (3)。
R301 的完整删项界及 R580 的同一来源识别给
$$
H_\sigma,H_\sigma^{-1},\quad W=z^2x,\quad Y_0=-z^3y
\in\mathbf C_p\langle z/\rho\rangle ,
\tag{4}
$$
其中前三个实际单位的相应 Gauss 范数均为一。
具体地，
$H_\sigma=\exp\{\log(\sigma/z)-cz^d\}$，
删项对数的 $\rho$ 范数严格小于 $p^{-1/(p-1)}$；
$W,Y_0$ 来自原形式对数的整逆，首项均为一。
所以 (4) 保留完整原 sigma、椭圆坐标和全部高尾。

工作于代数闭完备系数域 $\mathbf C_p$。
这同时覆盖原任意有限系数扩张，包括分歧扩张。
以下每个
$$
\boxed{S\le R\le\rho,\qquad R\in|\mathbf C_p^\times|}
\tag{5}
$$
都使用准确的闭圆盘代数
$$
\mathcal T_R=
\left\{\sum_{n\ge0}u_nz^n:\ |u_n|R^n\longrightarrow0\right\},
\qquad F_R=\operatorname{Frac}(\mathcal T_R).
\tag{6}
$$
导数 $D=D_z$ 保持 $\mathcal T_R$，
因为 $|n|_p\le1$。
每个 $F_R$ 通过原点 Laurent 展开嵌入 $\mathbf C_p((z))$，
故其常数域准确为 $\mathbf C_p$。

## 2. 边界极点、准确半径与 degree p

先记录以后会用两次的闭圆盘事实。

**无极点引理。**
若 $q,h\in\mathcal T_R$、$v\in F_R$ 满足
$$
Dv+qv=h,
\tag{7}
$$
则 $v\in\mathcal T_R$。

证明：若 $v$ 在闭盘内某点 $z_0$ 有 $m>0$ 阶极点，
则 $Dv$ 的最高极点阶为 $m+1$，系数为非零的
$-m$ 倍首极系数；$qv$ 至多有 $m$ 阶极点，
而 $h$ 正规，不能相消。
这也包括 $|z_0|=R$ 的边界点：
在该点的小局部盘中，Tate 函数仍有正规的局部展开。
一元 Weierstrass 分解把一个 Tate 分母写成单位乘有限多项式；
$\mathbf C_p$ 代数闭，全部相关零点都在上述闭盘中。
逐个消去后，分母只剩 Tate 单位。
因此 $v\in\mathcal T_R$。证毕。

现在完整计算 (3) 的 Gaussian。
若 $s_p(n)$ 为 $n$ 的 $p$ 进位数字和，Legendre 公式给
$$
\begin{aligned}
v_p(c^n/n!)+nd\frac{p}{p^2-1}
&=-n-v_p(n!)+\frac{np}{p-1}\\
&=\frac{s_p(n)}{p-1}.
\end{aligned}
\tag{8}
$$
当 $n=p^j$ 时右边恒为 $1/(p-1)$，不趋于无穷。
在任意较小半径增加的线性正项使它趋于无穷；
在任意较大半径，沿同一序列线性项变为负。
所以
$$
\boxed{\operatorname{rad}(\mathscr E)=S,\qquad
\mathscr E\notin\mathcal T_S.}
\tag{9}
$$
这里包括闭边界失败，没有仅用开盘的收敛半径。

另一方面，
$$
\mathscr E^p=\exp(pc z^d)\in\mathcal T_\rho^\times.
\tag{10}
$$
确实 $v_p(pc)=0$，而在闭 $\rho$ 盘上指数的加权赋值至少为
$$
\frac{p+1}{2p}>\frac1{p-1}.
$$
指数及其负值均在指数收敛盘内，
所以 (10) 与其逆都是真正的 Tate 单位。

对任意 (5)，若 $\mathscr E\in F_R$，
它满足
$$
D\mathscr E-cd z^{d-1}\mathscr E=0.
$$
无极点引理迫 $\mathscr E\in\mathcal T_R\subseteq\mathcal T_S$，
与 (9) 矛盾。因此
$$
\mathscr E\notin F_R.
\tag{11}
$$

定义实际域
$$
\boxed{K_R=F_R(\mathscr E)\subset\mathbf C_p((z)).}
\tag{12}
$$
由 (10)，$\mathscr E$ 是 $X^p-\exp(pc z^d)$ 的根。
系数域包含 $\mu_p$，故 $F_R(\mathscr E)$ 已包含该多项式全部根。
该扩张可分且正规；其自同构群是
$\mathscr E\mapsto\zeta\mathscr E$ 的 $\mu_p$ 子群。
$p$ 为素数，而 (11) 排除次数一，所以
$$
\boxed{[K_R:F_R]=p,\qquad
\operatorname{Gal}(K_R/F_R)=\mu_p.}
\tag{13}
$$
这同时证明多项式不可约。
相应 Tate 代数
$\mathcal T_R[X]/(X^p-\exp(pc z^d))$
是整的有限 étale 代数；在 $\mathbf C_p$ 上，$p$ 与 $X$ 都可逆。
没有把它当作一个拆开的 $p$ 份圆盘。

其实际导数为
$$
D\mathscr E=cd z^{d-1}\mathscr E.
\tag{14}
$$
每个 $\mu_p$ 自同构都与 $D$ 交换。
由于 (12) 使用实际形式根，它仍嵌入
$\mathbf C_p((z))$，所以 $K_R$ 的常数域准确是 $\mathbf C_p$。
后文添入实际积分时，同一个 Laurent 展开也保证常数域不增加。

## 3. 基域包含哪些真实来源

由 (3)–(4)，
$$
x,y,z,\zeta=\sigma'/\sigma
=\frac1z+cd z^{d-1}+\frac{DH_\sigma}{H_\sigma}
\in F_R,
\qquad
\sigma=zH_\sigma\mathscr E\in K_R.
\tag{15}
$$
因此原固定多项式 theta 来源都在 $K_R$，特别
$$
\boxed{S_{34},\ T_{72},\ S_{136}\in K_R.}
\tag{16}
$$
这里 $S_{136}$ 是 R466/R469 的原 degree $136$ 来源；
它和 $S_{34},T_{72}$ 的真实代数维数仍为二。
(16) 没有把第三来源当作独立变量，也没有说任何
$U_{\ell,r}$ 已经在这个域内。

所有 (15)–(16) 都由同一个完整原 sigma 写出。
没有将 Gaussian 自由替换成另一来源，
没有在这个解析扩张中改变原整数来源格或新增算术中央假设。

## 4. 非中央 Stokes 也排除任意积分常数

取 R575 的七个固定单积分
$$
J_{4,j}=\int_0^z u^j f_4(u)\,du\quad(j=0,1),
\qquad
J_{1,j}=\int_0^z u^j f_1(u)\,du\quad(j=0,\ldots,4).
\tag{17}
$$
下面所需的断言比单独的常数线性无相消多保留一个积分常数。

**引理。**
对任意不全为零的七个 $\mathbf C_p$ 系数及任意
$C\in\mathbf C_p$，
$$
\boxed{
\mathscr E^{-6}
\left(\sum_j u_jJ_{4,j}+\sum_j v_jJ_{1,j}-C\right)
\notin\mathcal T_S.
}
\tag{18}
$$

为证明，仍用 R580 的实际
$$
A_4=z^2f_4,\qquad A_1=z^5f_1,\qquad
E_i(A_\ell)=(zD-i)^{-1}A_\ell,\qquad
K_{\ell,i}=\mathscr E^{-6}E_i(A_\ell).
$$
原固定零初值准确给
$$
E_i(A_4)=z^iJ_{4,1-i}\quad(i=0,1),\qquad
E_i(A_1)=z^iJ_{1,4-i}\quad(i=0,\ldots,4).
\tag{19}
$$
七个积分按 $\mu_6$ 型分为以下五组：

| $i$ | 型 $-i\bmod6$ | 该组实际单积分 |
|---:|---:|---|
| $0$ | $0$ | $J_{4,1},J_{1,4}$ |
| $1$ | $5$ | $J_{4,0},J_{1,3}$ |
| $2$ | $4$ | $J_{1,2}$ |
| $3$ | $3$ | $J_{1,1}$ |
| $4$ | $2$ | $J_{1,0}$ |

因为 $d$ 是六的倍数，$\mathscr E$ 的型为零。
$\mu_6$ 投影及乘 $z^i$ 都保持 $\mathcal T_S$。
若 (18) 左边属于 $\mathcal T_S$，
则每一个非零组必使
$$
\sum_\ell c_{\ell,i}K_{\ell,i}
-\mathbf1_{i=0}C e^{-az^d}
\in\mathcal T_S.
\tag{20}
$$

R580 的完整 Stokes 和在 $i=0,1$ 的两个非中央余类
$r=6,12$ 上有实际矩阵
$$
\begin{pmatrix}
\mathcal S_{4;i,6}&\mathcal S_{1;i,6}\\
\mathcal S_{4;i,12}&\mathcal S_{1;i,12}
\end{pmatrix}
\equiv
\begin{pmatrix}
1&1\\
-4b/35&6b/35
\end{pmatrix}\pmod p,
\qquad
\det\equiv\frac{2b}{7}\ne0.
\tag{21}
$$
对 $i=2,3,4$，单行 $\mathcal S_{1;i,6}$ 为单位。
这些是完整无限和，不是截断后的首项猜测。
$p>19$ 保 $0<6,12<d$ 及所有 R580 非中央分母条件。

每一非零组都因 (21) 有一个非零 Stokes 行；
允许系数在 $\mathbf C_p$ 中也不改变这一点，
因为矩阵在该域仍可逆。
该余类等于非零常数倍的 R580 模型
$$
z^r\sum_{h\ge0}
\frac{(-a)^h z^{dh}}{((r-i)/d)_{\overline{h+1}}}
$$
加一个 $\mathcal T_\rho$ 函数。
该模型在 $S$ 边界的加权系数不趋零，故不属于
$\mathcal T_S$。
R580 的完整尾界和 $h=p^n$ 边界计算在系数扩张后逐项保持；
乘任何非零常数也不会将非趋零序列变成趋零。

最后，$C e^{-az^d}$ 仅有 $r=0\bmod d$ 部分。
它对刚用的 $r=6,12$ 投影均为零，
不能消掉 (21) 的非中央障碍。
对 (20) 作对应 $\mu_d$ 投影即得矛盾。
这些投影保持闭盘 Tate 代数，包含所有边界项。
引理得证。

这一证明尤其说明：在后续有理原函数问题中，
不能靠改积分常数绕开 R580。

## 5. 七个被积微分在整个 Kummer 域上没有原函数

**定理 1。**
七个 (17) 的被积函数的任意非零常数线性组合，
在 $K_R$ 中没有原函数；
在它的任何有限代数扩张中也没有原函数。

令 $\mathcal J$ 为一个非零常数线性组合，
并假设存在 $v\in K_R$ 满足
$$
Dv=D\mathcal J.
\tag{22}
$$
(1)、(3) 给
$$
D\mathcal J=\mathscr E^6 h,\qquad h\in\mathcal T_\rho.
\tag{23}
$$
具体地，两个被积族在去掉 $\mathscr E^6$ 后分别为
$$
z^{4+j}W H_\sigma^6,\qquad
z^{1+j}W Y_0 H_\sigma^6,
$$
所以 (23) 在原点也正规，不藏一个椭圆极点。

取 (13) 的真实特征六投影
$$
v_6=\frac1p\sum_{\zeta\in\mu_p}
\zeta^{-6}\gamma_\zeta(v).
\tag{24}
$$
这是域上的投影；不声称它是原整数格上的单位算子。
因为 $p>19$，$6$ 是非零模 $p$ 特征，
而
$$
K_R=\bigoplus_{j=0}^{p-1}F_R\mathscr E^j,
$$
所以 $v_6=\mathscr E^6 u$，其中 $u\in F_R$。
导数与投影交换，故
$$
Dv_6=\mathscr E^6h,\qquad
Du+6cd z^{d-1}u=h.
\tag{25}
$$
无极点引理给 $u\in\mathcal T_R$。
另一方面，(22)、(24) 给
$D(\mathcal J-v_6)=0$。
两者属于同一个实际 $\mathbf C_p((z))$，
因此
$$
u=\mathscr E^{-6}(\mathcal J-C)
$$
对某个 $C\in\mathbf C_p$ 成立。
这与 (18) 及 $\mathcal T_R\subseteq\mathcal T_S$ 矛盾，
证明 $K_R$ 中无解。

若一个有限扩张中有原函数，
对它取域迹并除以扩张次数。
特征零使导数与迹交换，所得即为 $K_R$ 中的原函数，
仍矛盾。证毕。

因此，七个实际被积微分在
$\Omega^1_{K_R}/dK_R$ 中给出七个常数线性独立的类。
这里使用的是原 degree $p$ wild 域，
不是普通地点的 Verschiebung 模型，也不是全 theta 的免费代数化。

## 6. 完整加性积分引理与七塔代数独立

应用 R575 §4 的加性积分引理。
为明确常数域及代数扩张的量词，重述所用论证：

若微分域 $L$ 的常数域是代数闭域 $C$，
$f_1,\ldots,f_n\in L$ 没有非零 $C$ 线性组合的 $L$ 原函数，
且实际积分扩张不增加常数，
那么这些积分在 $L$ 上代数独立。
按积分个数归纳；
假设最后一个积分代数，对迹操作先得到前面有理积分域中的原函数。
这个有理函数关于任一先前积分不能有有限极点：
首一极点因子 $q$ 的导数次数严格小于 $\deg q$，
极点相消迫 $Dq=0$，违反无新常数。
故它是该积分的多项式。
最高系数为常数，次数若至少二，
比较下一系数便给先前某个被积函数在较小域中的原函数；
归纳排除之。
逐个消元后，只可能是前面积分的常数线性组合加上 $L$ 中一项，
遂违反原假设。

这里取 $L=K_R$、$C=\mathbf C_p$。
第 2 节已付常数域；
所有实际积分生成的域仍嵌入 $\mathbf C_p((z))$，
所以常数不增加；
定理 1 已付全部非零常数组合的原函数排除。
因此
$$
\boxed{
J_{4,0},J_{4,1},J_{1,0},\ldots,J_{1,4}
\text{ 在 }K_R\text{ 上代数独立。}
}
\tag{26}
$$

R575 的固定零初值变换为
$$
U_{\ell,r}
=\frac1{(r-1)!}
\sum_{j=0}^{r-1}(-1)^j\binom{r-1}{j}
z^{r-1-j}J_{\ell,j}.
\tag{27}
$$
两块均为可逆三角矩阵，系数在 $F_R$；
再取原正幂规整
$$
V_{4,r}=z^{2-r}U_{4,r}\ (r=1,2),\qquad
V_{1,r}=z^{5-r}U_{1,r}\ (r=1,\ldots,5).
\tag{28}
$$
$z$ 在 $F_R$ 中非零可逆，所以 (27)–(28) 仍可逆。
这里仅在域论中使用 $z^{-1}$；
实际 (28) 全为正幂，未在原分布或整数格中除 log。
于是得到主结论
$$
\boxed{
V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5}
\text{ 在每一个 }K_R\text{ 上代数独立， }S\le R\le\rho.
}
\tag{29}
$$

## 7. 原九坐标所有真正含塔的多项式

现在回到实际常系数来源，而不在目标中增加自由列。
令
$$
\Phi=P(S_{34},T_{72},
 V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5}),
\qquad P\in\mathbf C_p[X,Y,Z_1,\ldots,Z_7].
\tag{30}
$$
假定 $P$ 真正含某个 $Z_i$。
原 $S_{34},T_{72}$ 的代数独立性保证按 $Z$ 收集后，
至少一个正 $Z$ 次数的系数仍非零。
这里 R418 的特征零独立性也可在 $\mathbf C_p$ 上使用：
实际归一的系数有理，对任意固定多项式次数，
所有可能关系由一个有限列数的有理系数线性系统给出；
其秩由某个有限行子式达到。
若在 $\mathbf C_p$ 中有非零核，就在 $\mathbf Q$ 中已有非零核，
与 R418 矛盾。

更一般地，可以让 (30) 的系数属于包含 $S_{136}$ 的真实原来源代数，
但须先按其实际关系收集，
并要求正 $Z$ 次数的实际系数至少一个非零。
不把三个基础生成元的关系误当成新的独立维数。

对任意整数 $m$，
$\mathscr E^m\Phi$ 在 $K_R[Z_1,\ldots,Z_7]$ 中仍对应一个非恒定多项式。
由 (29)，其实际值在 $K_R$ 上超越，特别不属于 $F_R$ 或 $\mathcal T_R$。
在 $R=S$ 就得到完整闭边界排除：
$$
\boxed{\mathscr E^m\Phi\notin\mathcal T_S
\quad\text{对每个 }m\in\mathbf Z.}
\tag{31}
$$

所有基础 theta 来源都在每个半径 $<S$ 的盘解析。
七个积分也如此：
对一个系数作有限次原函数只引入有限个随次数线性增长的整数分母，
其赋值损失为 $O_p(\log n)$，不改变开收敛半径。
有限乘积、和以及 $\mathscr E^m$ 因而均在每个半径 $<S$ 的盘解析，
给 $\operatorname{rad}(\mathscr E^m\Phi)\ge S$。

若该半径严格大于 $S$，
可选择
$$
S<R<\min\{\rho,\operatorname{rad}(\mathscr E^m\Phi)\},
\qquad R\in|\mathbf C_p^\times|.
$$
则 $\mathscr E^m\Phi\in\mathcal T_R$，
与同一个 (29) 矛盾。
故
$$
\boxed{
\operatorname{rad}(\mathscr E^m\Phi)=S,\qquad
\mathscr E^m\Phi\notin\mathbf C_p\langle z/S\rangle .
}
\tag{32}
$$
这允许任意多项式次数、任意依赖 $p$ 的常数系数，
并且保任意整数 Gaussian 次数；没有要求次数小于 $p$。

由 (3)–(4)，乘除 $(\sigma/z)^m$
只是在相应 $\mathscr E^m$ 之外再乘一个完整
$\mathcal T_\rho$ 单位及其逆。
所以 (32) 对这个真实 sigma 参考也保持。
若使用 $\sigma^m$ 而不是 $(\sigma/z)^m$，
只需保住原点的实际有限零阶或先清该有限极点，
不得擅自改积分常数。

(30) 与 $\mathscr E^m$ 均是 $w=z^6$ 的级数。
因此共同 $w$ frame 中的准确半径及闭边界是
$$
\boxed{S^6=p^{-6p/(p^2-1)}.}
\tag{33}
$$

## 8. 与真实饱和格、中央及原 forcing 的界限

(29)–(32) 新排除的是整个非线性解析相消：
原七塔不但常数线性独立，
而且在包含完整原 sigma 与基础 theta 来源的实际 wild Kummer 域上
仍代数独立。
因此，不能靠任意有限多项式组合及整数 Gaussian 重标，
把这些真正含塔的来源延拓到更大盘。
这个结论比 R580 的线性限制严格更强。

它仍不是有限整数矩阵的饱和结论。
一个给定来源的完整级数在远处有坏分母，
不代表在指定次数预算下，
同一饱和前缀已经有可读的非整首系数。
本篇没有计算相应前缀的 Smith 因子，
没有由半径等式宣布 R583 的主高度常数最优，
也没有取代 R579/R581/R583/R584 的全部量词和范数格。

证明完全不使用某个原中央或 Dirac 缺陷为零，
因此即使这些指定值同时为零，
上述非中央 wild 障碍仍在。
它不证明这些指定算术值非零，
也不提供原 $S/T/S_{136}$ 中央到两负矩的尚缺比较。

原 R577/R578 的完整修正问题仍需在同一个
$\mathcal W_D$ 上处理：
$\mathcal D_\psi$ 的真实像、
同一个 $R$ 的低行与高延拓、
全部 $P_{134}/U_0$、两条十三行和真正 $d_2$ 均保留。
不得把 (24) 的域上 $1/p$ 投影搬进该整数来源，
或把一个新解析域当成已付的原物理像。

## 依赖

- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：
  原首坏 sigma 系数、完整较大盘及同一单位缩放。
- [R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)：
  七个实际零初值积分、正幂规整和加性积分引理。
- [R580](R580-same-charge-primitive-towers-and-unit-noncentral-stokes-matrix.md)：
  两条完整非中央 Stokes 行、$2b/7$ 单位、真实闭边界失败。
- [R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)：
  两个基础来源的实际代数独立性及全次数预算的准确范围。

本篇为全参数证明，没有新增素数扫描或把有限数值检查当成结论。

