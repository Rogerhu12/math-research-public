# R294：新固定 j=0 曲线的完整三次同源下降，精确秩二

**已证明，2026-11-13。** 本篇把 R288 固定候选的秩确定为恰好二，证明只用实际有理三次同源、两个二次域的理想与单位，以及显式 Kummer 核计算。不使用解析秩、数值秩或 Sha 有限假设。

## 1. 结论

令
$$
E:y^2=x^3+17,\qquad E':Y^2=X^3-459.
$$
则
$$
\boxed{\operatorname{rank}E(\mathbf Q)
=\operatorname{rank}E'(\mathbf Q)=2.}
\tag{1}
$$
准确的两个三次同源 Kummer 像为
$$
\boxed{
\operatorname{im}\alpha_E
=\left\langle4+\sqrt{17},\,
\frac{5+\sqrt{17}}{5-\sqrt{17}}\right\rangle
\simeq(\mathbf Z/3)^2,
\qquad \operatorname{im}\alpha_{E'}=0.}
\tag{2}
$$
像取在相应二次域的乘法群模立方中。R288 的两个实际点
$$
P=(-2,3),\qquad Q=(-1,4)
$$
的 Kummer 像生成 (2)。这给独立于 R288 模 $19$ 证书的秩下界；上界也同时付清。

更准确地，原三次同源
$$
\phi(x,y)=\left(\frac{x^3+68}{x^2},\,
\frac{y(x^3-136)}{x^3}\right)
\tag{3}
$$
满足 $E'(\mathbf Q)=\phi E(\mathbf Q)$。其两个明确像为
$$
\phi P=(15,54),\qquad \phi Q=(67,548).
$$

## 2. 有理三次同源及完整 Kummer 核

先对任一非零非平方整数 $D$ 写
$$
E_D:y^2=x^3+D,\quad E_{-27D}:Y^2=X^3-27D,
\quad s=\sqrt D.
$$
定义
$$
\phi_D(x,y)=\left(\frac{x^3+4D}{x^2},
                   \frac{y(x^3-8D)}{x^3}\right),
$$
$$
\widehat\phi_D(X,Y)=
\left(\frac{X^3-108D}{9X^2},
      \frac{Y(X^3+216D)}{27X^3}\right).
\tag{4}
$$
直接代入方程可核两式落在所述曲线上；它们在光滑射影模型上延拓，并将原点送到原点。两者次数均为三。非恒定且保原点的椭圆曲线态射是群同态；这也可由原点对应的 Picard 同构得到。第一式的不变微分乘子为一，第二式为三。它们的复合为 $[3]$：两者均为保原点同态，复合的微分为三，与 $[3]$ 相同；特征零中微分为零的同态只能为零。因而 (4) 是实际互为对偶的同源。

定义
$$
\alpha_D:E_D(\mathbf Q)\longrightarrow
\mathbf Q(s)^\times/\mathbf Q(s)^{\times3},
\qquad \alpha_D(O)=1,\quad \alpha_D(x,y)=y+s.
\tag{5}
$$
有限有理点的 $x\ne0$，故 (5) 的值非零，且其范数为 $x^3$。

### 2.1 群同态不靠假设

一条非垂直直线 $y=mx+n$ 与曲线的三个交点横坐标是
$F(X)=X^3-m^2X^2-2mnX+D-n^2$ 的根，按交数计。由
$$
-m^3F(-(n+s)/m)=(n+s)^3
$$
得到这三个交点的 $y+s$ 乘积为立方。$m=0$ 的情形直接成立。又
$$
(y+s)(-y+s)=-x^3
$$
也是立方，所以弦切群律给 $\alpha_D(P+Q)=\alpha_D(P)\alpha_D(Q)$。
垂直线和与原点相交的情形由后一式及 $\alpha_D(O)=1$ 直接处理；重根按相同多项式恒等式处理。因此 (5) 确为群同态。

### 2.2 核准确是对偶同源像

对 (4) 的第二式，直接立方得到
$$
\boxed{y+s=\left(\frac{Y+9s}{3X}\right)^3.}
\tag{6}
$$
所以 $\widehat\phi_D E_{-27D}(\mathbf Q)\subset\ker\alpha_D$。
反过来，若一个有限点满足
$y+s=(u+vs)^3$，其中 $u,v\in\mathbf Q$，比较 $s$ 系数得到
$$
v(3u^2+Dv^2)=1.
$$
特别 $v\ne0$。置
$$
X=3/v,\qquad Y=9u/v.
$$
便有
$$
Y^2-X^3=27(3u^2v-1)/v^3=-27D.
$$
式 (6) 和范数关系说明该点经 $\widehat\phi_D$ 后的纵坐标为 $y$，横坐标为 $x$：横坐标的立方已相同，而有理数上的立方映射单射。故
$$
\boxed{E_D(\mathbf Q)/\widehat\phi_DE_{-27D}(\mathbf Q)
\simeq\operatorname{im}\alpha_D.}
\tag{7}
$$
对 $D'=-27D$ 应用同一构造，并把 $E_{729D}$ 通过
$(x,y)\mapsto(9x,27y)$ 与 $E_D$ 比较，即得
$$
\boxed{E_{-27D}(\mathbf Q)/\phi_DE_D(\mathbf Q)
\simeq\operatorname{im}\alpha_{-27D}.}
\tag{8}
$$
本篇的 $D=17$ 和 $D'=-459$ 都为非平方，故上述所有有限有理点情况均适用。

## 3. 实际 Kummer 值的支撑

若 $P\in E_D(\mathbf Q)$，可写
$$
x=X/Z^2,\qquad y=Y/Z^3,
\qquad X,Y,Z\in\mathbf Z,\quad
\gcd(X,Z)=\gcd(Y,Z)=1.
$$
这由整数 Weierstrass 方程在负赋值处的平方/立方分母立即得到。
在模立方群中，$y+\sqrt D$ 等于
$Y+Z^3\sqrt D$，因为 $Z^3$ 已是立方。

对不在 $2D$ 上的任何素理想 $\mathfrak l$，若其下面的有理素数整除 $Z$，则 $Y$ 为该处单位。否则，两个共轭因子
$$
Y+Z^3\sqrt D,\qquad Y-Z^3\sqrt D
$$
的差在该处为单位，故二者不能同时有正赋值；乘积为 $X^3$，所以每个因子的赋值均为三的倍数。因此
$$
\boxed{v_{\mathfrak l}(\alpha_D(P))\equiv0\pmod3
\quad(\mathfrak l\nmid2D),\qquad
N\alpha_D(P)\in\mathbf Q^{\times3}.}
\tag{9}
$$
这里仅用真实点给出的像的必要条件；不把一个任意 $S$-单位都宣称为 Selmer 类。

## 4. 实二次域：像恰为二维

取
$$
K=\mathbf Q(\sqrt{17}),\qquad
\mathcal O_K=\mathbf Z[(1+\sqrt{17})/2].
$$
Minkowski 的实二次域界为 $\sqrt{17}/2<3$，所以每个理想类有范数一或二的整理想代表。$2$ 分裂，而
$$
\pi_2=\frac{5+\sqrt{17}}2,\qquad N\pi_2=2
$$
使两个二上素理想均为主理想。因此 $h_K=1$。

其基本单位可取
$$
\varepsilon=4+\sqrt{17},\qquad N\varepsilon=-1.
\tag{10}
$$
给一个简短的最小性证明。若单位 $1<u<\varepsilon$，写
$u=(a+b\sqrt{17})/2$，则 $u'=\pm u^{-1}$，所以
$0<b=(u-u')/\sqrt{17}<3$。方程 $a^2-17b^2=\pm4$ 在 $b=1$ 时无解，在 $b=2$ 时仅有能够给 $u>1$ 的 $a=8$，正是端点 $u=\varepsilon$。故不存在这样的 $u$。将任一正单位除以适当的 $\varepsilon$ 次幂可落在 $[1,\varepsilon)$，所以
$\mathcal O_K^\times=\{\pm\varepsilon^j:j\in\mathbf Z\}$。特别 $\varepsilon$ 不是单位立方。

对 (9) 的 $D=17$，只有 $2$ 上两个分裂位及 $17$ 上一个分歧位可能有非三倍赋值。$17$ 位的范数指数等于其赋值，故范数为立方迫使该赋值也为三倍。类数一遂使每个真实 Kummer 值模立方可写
$$
\varepsilon^e\pi_2^a\bar\pi_2^b.
$$
范数条件给 $a+b\equiv0\pmod3$。所以
$$
\operatorname{im}\alpha_{17}
\subset\langle\varepsilon,\pi_2/\bar\pi_2\rangle.
\tag{11}
$$
右边两生成元独立：后一元在两个二上素理想的赋值分别为 $1,-1$；若其某次幂乘单位是立方，先看赋值迫使该次数被三整除，再看 (10) 迫使单位指数被三整除。因此右边准确为二维 $\mathbf F_3$ 空间。

现在使用真实点，直接有
$$
\alpha_{17}(Q)=4+\sqrt{17}=\varepsilon,
$$
$$
\alpha_{17}(P)=3+\sqrt{17}
=\varepsilon\pi_2\bar\pi_2^2
\equiv\varepsilon\frac{\pi_2}{\bar\pi_2}\pmod{K^{\times3}}.
\tag{12}
$$
所以 (11) 实际取等。这同时证明了 (2) 的第一部分及这两点模对偶同源像的独立性。

## 5. 虚二次域：对偶 Kummer 像为零

对 $D'=-459=-9\cdot51$，使用
$$
K'=\mathbf Q(\sqrt{-51}),\qquad
\alpha_{-459}(X,Y)=Y+3\sqrt{-51}.
$$
判别式为 $-51$。Minkowski 界
$$
\frac2\pi\sqrt{51}<5
$$
说明每个理想类有范数至多四的整理想代表。$2$ 惰性，故没有范数二的素理想，唯一范数四的理想 $(2)$ 为主理想。$3$ 上唯一素理想 $\mathfrak q_3$ 的平方为 $(3)$。又 $\mathfrak q_3$ 不为主理想，因为范数三元素要求
$a^2+51b^2=12$，无整数解。因此
$$
\operatorname{Cl}(K')\simeq\mathbf Z/2.
\tag{13}
$$
特别它没有三挠。

式 (9) 的潜在坏支撑现在为 $2,3,17$。其中 $2$ 惰性、$3$ 和 $17$ 分歧，各只有一个素理想；相应范数剩余次数为二、一、一，均与三互素。范数为立方遂使这些位的赋值也全部被三整除。结合 (9)，对每个实际 Kummer 值 $\alpha$ 都有
$$
(\alpha)=\mathfrak a^3.
$$
由 (13)，$[\mathfrak a]^3=1$ 强迫 $\mathfrak a=(b)$ 为主理想。于是 $\alpha/b^3$ 为单位。这个虚二次域的单位只有 $\pm1$，而二者均为立方。因此
$$
\boxed{\operatorname{im}\alpha_{-459}=0.}
\tag{14}
$$
没有遗漏三处或十七处的局部方向：它们正是上述分歧位，并已用完整范数条件逐一处理。

## 6. 从两个准确像到精确秩

由 (8)、(14)，$E'(\mathbf Q)=\phi E(\mathbf Q)$，故
$$
\widehat\phi E'(\mathbf Q)=[3]E(\mathbf Q).
$$
再由 (7)、(11)–(12)，得到
$$
E(\mathbf Q)/3E(\mathbf Q)\simeq(\mathbf Z/3)^2.
\tag{15}
$$
两个同源的有理核均为零：非原点核点的纵坐标分别涉及 $\sqrt{17}$ 与 $\sqrt{-459}$，都不有理。若一个有理点为三挠，其 $\phi$ 像先落在第二个有理核，再落在第一个有理核，故只能为原点。因此 $E(\mathbf Q)[3]=0$。

Mordell–Weil 定理下，(15) 的维数就是有理秩，给 $\operatorname{rank}E(\mathbf Q)=2$。同源保持有理秩，得到 (1)。R288 还已证明 $E(\mathbf Q)$ 的整个挠群为零；这里的秩证明只需要上面直接付清的三挠为零。

本篇不由三次同源或其一个初等下降断言其他素数处的 Sha 有限。它支付的是新固定候选的精确秩和实际三次下降像；无穷多个 $p$ 的目标仍须后续完整中央非零输入。

## 7. 证书与标准输入

`scripts/check-jzero-rational-three-descent.py` 精确核对两个同源方程、不变微分、(6) 的立方恒等式、显式逆构造及 (12) 的真实二上赋值生成元关系。理想类与单位的证明为 §§4–5 的统一论证。

标准输入仅为 Mordell–Weil 有限生成、椭圆曲线保原点态射的群同态性质和二次域 Minkowski 理想类界。可参阅 J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer, 2009，以及 J. Neukirch, *Algebraic Number Theory*, Springer, 1999，关于椭圆同源和理想类 Minkowski 界的章节；所需三次 Kummer 核在 §2 已直接证明。
