# R575 — 固定原函数七塔的代数独立与两个原负矩的完整 Dirac 缺陷

日期：2026-11-14。**状态：已证明。**

本篇保持原 $b=17$ 的 $f_4=x\sigma^6$、$f_1=-xy\sigma^6$。
首先证明它们的七个固定原函数在整个
$\mathbf C(z,x,y,\zeta,\sigma)$ 上代数独立。
其次，为这七个原函数构造原普通地点的实际有限阶分布：
全 Frobenius 公式的原点 Dirac 缺陷，只有两项不被 $\mu_6$ 型自动杀掉，
而这两项恰是 R533/R540 的原负二 $I_4$ 与原负五 $I_1$。

没有由此证明两个负矩非零，也没有由原 $S/T$ 中央失败推出它们为零。
有限阶分布仍不是有界测度；全部饱和 jet 与惰性格成本仍须另付。

## 1. 七个固定的特征零来源

令 $D=d/dz$，保持
$$
Dx=2y,\qquad Dy=3x^2,\qquad y^2=x^3+b,\qquad
g=\zeta=\sigma'/\sigma,\qquad Dg=-x,\qquad b=17.
$$
定义
$$
U_{4,r}(z)=\frac1{(r-1)!}\int_0^z(z-t)^{r-1}f_4(t)\,dt
\quad(r=1,2),
$$
$$
U_{1,r}(z)=\frac1{(r-1)!}\int_0^z(z-t)^{r-1}f_1(t)\,dt
\quad(r=1,\ldots,5).
\tag{1}
$$
它们都是固定的整函数；不存在随 $p$ 改选原函数的自由常数。
准确归一为
$$
D^rU_{\ell,r}=f_\ell,\qquad
D^jU_{\ell,r}(0)=0\quad(0\le j<r).
\tag{2}
$$
其中两条原 principal 来源记为
$$
F_4=U_{4,2},\qquad F_1=U_{1,5}.
$$
原首项为
$$
F_4=\frac{z^6}{30}-\frac{bz^{12}}{1155}+\cdots,\qquad
F_1=\frac{z^6}{720}+\frac{bz^{12}}{554400}+\cdots,
$$
$$
F_4-24F_1=-\frac{bz^{12}}{1100}+\cdots.
\tag{3}
$$
所以它们不是因为首项成比例就成为同一个来源。

## 2. 两个初等的有理原函数障碍

先令
$$
K_0=\mathbf C(E)(z)=\mathbf C(z,x,y).
$$
这里 $z$ 在椭圆函数域上超越：若有代数关系，沿任一非零周期
$z\mapsto z+n\lambda$ 固定所有椭圆系数，会给同一多项式无穷多个根。

**引理一。** $K_0$ 中不存在 $Dc=x$ 的有理函数。

证明如下。若 $c$ 关于 $z$ 有有限极点，取其首一不可约极点因子
$q(z)\in\mathbf C(E)[z]$。$Dq$ 的 $z$ 次数小于 $\deg q$；
为了使 $Dc=x$ 没有该极点，必须 $q\mid Dq$，因而 $Dq=0$。
若 $m=\deg q>0$，比较 $z^{m-1}$ 系数给
$Da_{m-1}=-m$。椭圆函数的导数不可能是非零常数：
它若有极点，导数仍有极点；没有极点则它本来就是常数。

故 $c$ 是 $z$ 的多项式。
其最高系数的导数为零，所以为常数；
若次数大于一，下一系数再次迫使椭圆函数有非零常数原函数。
因此最多
$c=a_1z+a_0$，其中 $a_1\in\mathbf C$、$a_0\in\mathbf C(E)$。
这要求
$$
Da_0=x-a_1.
$$
右边仅在 $O$ 有二阶极点，所以 $a_0$ 只能在 $O$ 有单极点。
椭圆曲线上不存在具有唯一单极点的非恒定有理函数，矛盾。证毕。

**引理二。** 在 $K_1=K_0(g)$ 中，对于任意非零
$F\in K_0$，方程
$$
(D+6g)P=F
\tag{4}
$$
没有有理解。

首先，实际 $g$ 在 $K_0$ 上超越。
否则对一个有限代数扩张取迹，$Dg=-x$ 会给 $K_0$ 中 $x$ 的有理原函数，
与引理一矛盾。

若 (4) 的 $P$ 有有限 $g$ 极点，取其首一不可约因子 $q(g)$。
因为 $Dg=-x$ 不增加 $g$ 次数，
$\deg_gDq<\deg_gq$。
该极点的最高阶不能由 $6gP$ 抵消，故仍须 $q\mid Dq$，
于是 $Dq=0$。
若 $m=\deg_gq$，比较次最高系数便得到
$Da_{m-1}=mx$，又违背引理一。
故 $P$ 是 $g$ 多项式。
但 $6gP$ 的最高次数比 $DP$ 高一，不能等于不含 $g$ 的非零 $F$。
证毕。

## 3. 同一 sigma charge 6 上没有遗漏的代数原函数

令
$$
K=K_1(\sigma)=\mathbf C(z,x,y,g,\sigma).
$$
这是实际亚纯函数域，常数域恰为 $\mathbf C$。

实际 $\sigma$ 在 $K_1$ 上也超越。
若它代数，取范数将给某个 $a\in K_1^\times$ 及非零整数 $n$，
使
$$
Da/a=ng.
$$
然而任何有理 $a(g)$ 在 $g=\infty$ 的对数导数都是
$Da_{\rm lead}/a_{\rm lead}+O(g^{-1})$，不可能有正一次项 $ng$。

进一步，对任意 $0\ne F\in K_0$，
$$
\boxed{D v=F\sigma^6\quad\text{在 }K\text{ 中无解}.}
\tag{5}
$$
为完整排除有理 $\sigma$ 分母，取有限非零 $\sigma$ 极点的首一因子
$q(\sigma)$，次数为 $m$。
若此极点在 $Dv$ 中消失，必须 $q\mid Dq$；
比较最高系数给 $Dq=mgq$。
因 $q\ne\sigma$，其常数项 $a_0\ne0$，于是
$Da_0/a_0=mg$，已证明不可能。
所以 $v$ 只能是 $\sigma$ 的 Laurent 多项式。
比较 $\sigma^6$ 系数，正得到 (4)，矛盾。

同一结论也排除代数原函数：
若 $v$ 在 $K$ 的有限扩张中满足 (5)，取迹并除以扩张次数
就会给 $K$ 中的有理原函数。
这里排除了整个 rational/algebraic primitive，不是仅检查了某个低次猜测。

## 4. 七个真实积分的完整代数独立性

定义实际整函数
$$
J_{4,j}(z)=\int_0^z t^j f_4(t)\,dt\quad(j=0,1),
$$
$$
J_{1,j}(z)=\int_0^z t^j f_1(t)\,dt\quad(j=0,\ldots,4).
\tag{6}
$$
其七个被积函数在 $\mathbf C$ 上线性独立。
确实，一个常数线性组合若为零，将给
$$
x\bigl(A(z)-yB(z)\bigr)=0,\qquad
\deg A\le1,\quad\deg B\le4.
$$
$z$ 在 $\mathbf C(E)$ 上超越且 $y$ 非恒定，故所有系数都为零。

由 (5)，任意非零常数线性组合的被积函数，都没有 $K$ 中的原函数。
下面给所用加性积分引理的证明，以免把有限个 Taylor 系数当成独立性。

**加性积分引理。**
设常数域为代数闭域 $C$ 的微分域 $L$ 中有 $f_1,\ldots,f_n$，
没有非零 $C$ 线性组合在 $L$ 中有原函数。
若 $Dy_i=f_i$ 且所取实际扩张不增常数，
则 $y_1,\ldots,y_n$ 在 $L$ 上代数独立。

按变量数归纳。若最后一个 $y_n$ 在前面的有理函数域上代数，
对迹操作给该有理函数域中的 $f_n$ 原函数。
一个关于最后一个先前变量 $y_{n-1}$ 的有理原函数不能有有限极点：
首一极点因子 $q$ 满足 $\deg Dq<\deg q$，
因而极点相消会迫使 $Dq=0$，
与常数域不增加矛盾。
因此它是 $y_{n-1}$ 多项式。
最高系数为常数；若次数至少二，下一系数使 $f_{n-1}$
在更小的有理函数域中有原函数，归纳假设排除之。
故至多为常数倍 $y_{n-1}$ 加一个较小域中的函数。
逐次消去，得到某个非零常数线性组合的 $f_i$ 在 $L$ 中有原函数，
仍矛盾。引理得证。

把此引理用于 (6)，得到七个 $J$ 在 $K$ 上代数独立。
而 (1) 的整个三角变换为
$$
\boxed{
U_{\ell,r}
=\frac1{(r-1)!}
 \sum_{j=0}^{r-1}(-1)^j\binom{r-1}{j}
 z^{r-1-j}J_{\ell,j}.
}
\tag{7}
$$
两块的对角分别是
$1,-1$ 和 $1,-1,1/2,-1/6,1/24$，均非零。
因此
$$
\boxed{
U_{4,1},U_{4,2},U_{1,1},\ldots,U_{1,5}
\text{ 在 }K\text{ 上代数独立}.
}
\tag{8}
$$
特别 $F_4,F_1$ 在整个原椭圆、sigma 函数字段上代数独立。

原 $S,T$ 属于 $K$；
[R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)
已付它们的代数独立性。
所以 $S,T,F_4,F_1$ 的真实超越次数为四，
而 $S,T$ 与完整七塔的真实超越次数为九。

## 5. 实际复增长和 tame 型

每个 $f_4,f_1$ 都是非零 degree $6$ 的整 theta 来源。
完整准周期公式在基本平行四边形外给 $\exp(O(|z|^2))$ 上界；
在整个周期格上，$f_4$ 有四重零、$f_1$ 有单零，
故其整函数阶恰为二。
积分的上界与导数的 Cauchy 下界因此给
$$
\boxed{\operatorname{ord}_z U_{\ell,r}=2.}
\tag{9}
$$

在 $\mu_6$ 作用下，$f_4$ 的型为 $4$、$f_1$ 的型为 $1$。
固定零初值的积分准确给型 $\ell+r$。
七塔的第一阶及型如下：

| 来源 | 积分次数 $r$ | 首 $z$ 次数 | tame 型 |
|---|---:|---:|---:|
| $U_{4,1}$ | 1 | 5 | 5 |
| $F_4=U_{4,2}$ | 2 | 6 | 0 |
| $U_{1,1}$ | 1 | 2 | 2 |
| $U_{1,2}$ | 2 | 3 | 3 |
| $U_{1,3}$ | 3 | 4 | 4 |
| $U_{1,4}$ | 4 | 5 | 5 |
| $F_1=U_{1,5}$ | 5 | 6 | 0 |

因此两个指定的 $F_4,F_1$ 都是 $w=z^6$ 的整函数，阶恰为 $1/3$。
其余五塔在本篇的算术呈示中保持原 $z$ 型。
即使复分析上可以除首 $z$ 幂后写成 $w$ 函数，
也不能免费把其 Amice 变换除以 $\log(1+T)$：
后者有真正的 $p$ 幂挠点零，须另付消去。

## 6. 原普通地点的两个完整缺陷

现在使用 R533/R529 已付的原完整 $\mathcal S_6$ 普通核心。
对原固定射线上的 $p$，写
$$
\beta=\bar\pi_0^{-1},\qquad
\kappa=\pi_0/\bar\pi_0,\qquad v_p(\kappa)=1,\qquad
\Omega=\Omega_{p,17}.
$$
原 $f=f_\ell$ 的有界测度 $\mu_f$ 满足
$$
\mu_f|_{p\mathbf Z_p}=\beta[\kappa]_*\mu_f,\qquad
\mathcal A_{\mu_f}(T)=f(\Omega\log(1+T)).
\tag{10}
$$
不从另一 Frobenius 根或反射地点猜测此标量。

对 (1) 中每个实际 $r$，定义原单位测度及其质量
$$
\tau_{\ell,r}=1_{\mathbf Z_p^\times}(t)t^{-r}\mu_f,\qquad
I_{\ell,r}=\tau_{\ell,r}(1).
\tag{11}
$$
$\mu_6$ 型严格给
$$
\boxed{
I_{\ell,r}=0
\text{ 除了 }(\ell,r)=(4,2),(1,5).
}
\tag{12}
$$
这两个例外恰为原 $I_4,I_1$，不是正四、正一矩。

更准确地，
$$
\tau_{\ell,r}-I_{\ell,r}\delta_0
\quad\text{的 }0,1,\ldots,r\text{ 次矩全部为零}.
\tag{13}
$$
第一个非零正矩在 $r+d_\ell$，
其中 $d_4=4,d_1=1$；
其值是
$(1-\beta\kappa^{d_\ell})\Omega^{d_\ell}f_\ell^{(d_\ell)}(0)$，
在当前 $p>19$ 时是单位。

定义实际分布
$$
\boxed{
\rho_{\ell,r}
=\sum_{n\ge0}
 \beta^n\kappa^{-rn}[\kappa^n]_*
  \bigl(\tau_{\ell,r}-I_{\ell,r}\delta_0\bigr).
}
\tag{14}
$$
对每个 $C^r$ 测试，取原点 $r$ 阶 Taylor 多项式。
(13) 把它整项杀掉，余项在 $\kappa^n\mathbf Z_p$ 上是
$o(|\kappa|^{rn})$，故 (14) 的每项趋零。
同一 Taylor 余项范数给统一的连续泛函界。
因此 (14) 在每个 $C^r$ 测试上收敛，定义阶至多 $r$ 的分布。
这里不声称分布范数中的各项趋零；在固定局部解析测试上则有更强的几何收敛。

它的正矩为
$$
\rho_{\ell,r}(t^m)=
\begin{cases}
0,&0\le m\le r,\\[2mm]
\displaystyle
\frac{\mu_f(1_{\mathbf Z_p^\times}t^{m-r})}
 {1-\beta\kappa^{m-r}},&m>r.
\end{cases}
$$
用 (10) 识别第二行，并保零初值，得到
$$
\boxed{
\mathcal A_{\rho_{\ell,r}}(T)
=\Omega^{-r}U_{\ell,r}(\Omega\log(1+T)).
}
\tag{15}
$$
所以 (14) 是 (1) 那个固定原函数本身的算术呈示，
没有另选常数来制造 scalar core。

在 (14) 的每一个有限截断上先作真正的域限制，
再取极限。$n=0$ 的单位部分被 $p\mathbf Z_p$ 切掉，
而其 Dirac 项保留；于是完整等式是
$$
\boxed{
\rho_{\ell,r}|_{p\mathbf Z_p}
=\beta\kappa^{-r}[\kappa]_*\rho_{\ell,r}
-I_{\ell,r}\delta_0.
}
\tag{16}
$$
对任意深度 $m\ge1$，令 $a=\beta\kappa^{-r}$，有
$$
\boxed{
\rho_{\ell,r}|_{p^m\mathbf Z_p}
=a^m[\kappa^m]_*\rho_{\ell,r}
-I_{\ell,r}(1+a+\cdots+a^{m-1})\delta_0.
}
\tag{17}
$$
所有原点质量都显示保留。

因此，两指定负矩的准确含义是
$$
\boxed{
I_4=0\iff F_4\text{ 的 (16) 中 Dirac 缺陷为零},\qquad
I_1=0\iff F_1\text{ 的 (16) 中 Dirac 缺陷为零}.
}
\tag{18}
$$
另外五塔的 scalar 公式则已由 (12) 无条件支付。
若两个原 $I$ 都为零，完整七塔均有准确的原普通核心，
但这不是已经得到原 $S/T$ 中央假设推出两 $I$ 为零的桥。

## 7. 它们确实不是有界测度

$\tau_{\ell,r}$ 非零，因为其第一个非零正矩是上述单位。
可取某个固定单位紧开集 $B$，使 $\tau_{\ell,r}(B)\ne0$。
同一个完整系列在其真实缩小像上给
$$
\boxed{
\rho_{\ell,r}(\kappa^nB)
=\beta^n\kappa^{-rn}\tau_{\ell,r}(B).
}
\tag{19}
$$
右边的赋值为 $v_p(\tau_{\ell,r}(B))-rn$，无下界。
所以所有这些实际原函数分布都不是有界测度，
即使相应 $I_{\ell,r}=0$ 也不例外。
删去或改变一个原点 Dirac 项不能改变 (19)。

乘积的原 Amice 呈示可以准确作卷积：
单项式 $\prod U_{\ell,r}^{d_{\ell,r}}$ 的实际分布阶至多
$\sum r\,d_{\ell,r}$，再乘 $S,T$ 的有界测度不会降低这项阶数。
这给同一 ordinary monomial 呈示；它并不自动给全部饱和前缀的界。
当来源次数增长到 $D$ 时，分布阶也随 $D$ 增长，
不能把固定有限阶的逐素数估计误算为所有乘积仅 $O(k)$ 的全球代价。

R418 的四坐标或更多坐标预算，只有在同一惰性、ordinary 饱和格
及全部乘积成本支付后才可使用。
本篇不把 (8) 的真实独立性冒充这些尚未支付的格条件。

## 8. 与原 Cartier 两行和主目标的准确接点

[R570](R570-original-global-negative-moment-cartier-lines-and-polynomial-primitives.md)
的全局非 exact Cartier 行，是 (18) 中同一两个缺陷的第一层：
其准确系数仍是 $I_4$ 或 $I_1$ 乘原 $\Omega,\mathfrak h,b^s$ 单位。
所以它没有换成另一负权、另一局部地点或某个可任意归一的原函数。

[R573](R573-original-six-torsion-jets-and-two-complete-theta-quotients.md)
又给这两个第一层系数在原同一 $P_1$ 的常数、一次 jet 中的准确出现，
并保下一 jet 的真实单位。
本篇把对应的两个特征零原函数及其完整 ordinary 缺陷也固定下来。

仍未支付的两步都保留：

1. 对原实际 $S/T$ 等全中央行，建立到这些指定 $I_i$ 或单位行的合法比较；
2. 用新的真正算术条件排除两个指定值同时消失，或支付可用的完整多坐标 jet 门。

不能把 R567 的 native 残差当成整个算术总行，
也不能因存在七个 scalar/finite-order 形式就删掉原 mixed 补域。

## 9. 精确证书

[check-r575-fixed-primitives-and-complete-dirac-defects.mjs](../scripts/check-r575-fixed-primitives-and-complete-dirac-defects.mjs)
用 108 项符号检查核对七个实际积分变换、全部零初值、
两个指定原函数的六阶/十二阶系数，以及 (16)–(17)
在有限截断中的整个支持与边界项。
所有 Dirac 质量保留。

代数独立性来自第 2–4 节的完整域论证明，不由有限 jet 检查代替。
证书没有进行新的素数扫描，也没有声称原主目标已完成。
