# R4：CM 曲线 $y^2=x^3-17x$ 的精确秩证书

**可信度：已证明。** 这里完整证明一条适用于 CM 路线的固定曲线的代数秩恰为 $2$，并证明两给定点独立。没有使用 $\Sha$ 有限性、解析秩或 $p$-adic 高度猜想。结论不包含无穷多个 $p$ 的 $\Sha[p^\infty]$ 有限性。

## 1. 陈述

设
$$
E:\ y^2=x^3-17x,\qquad
T=(0,0),\quad P=(-1,4),\quad Q=(9,24).
$$
则
$$
E(\mathbb Q)_{\rm tors}=\{O,T\}\simeq\mathbb Z/2\mathbb Z,
\qquad \operatorname{rank}E(\mathbb Q)=2,
$$
且 $P,Q$ 线性无关。该曲线在 $\mathbb Q(i)$ 上具有复乘自同态
$$
[i](x,y)=(-x,iy),\qquad [i]^2=[-1].
$$
本文不声称 $P,Q$ 生成全部自由部分。

Coates–Liang–Sujatha 的 *The Tate–Shafarevich group for elliptic curves with complex multiplication II*（arXiv:1005.4206，2010，Theorem 1.3）所列五条曲线中，$D_2=17$ 正是此曲线。以下秩证明独立于该文的秩计算。

## 2. 挠点与两点独立性：有限域证书

判别式为
$$
\Delta=64\cdot17^3,
$$
故 $3,5,41$ 都是好约化素数。直接列出每个 $x$ 的 $y$ 值可得

| 素数 | $x$ 依次取值 | 对应的可行 $y$ |
|---|---|---|
| $3$ | $0,1,2$ | $\{0\},\varnothing,\{1,2\}$ |
| $5$ | $0,1,2,3,4$ | $\{0\},\{2,3\},\{2,3\},\{1,4\},\{1,4\}$ |

加入 $O$，得到
$$
\#E(\mathbb F_3)=4,\qquad \#E(\mathbb F_5)=10.
$$
好约化处的素于剩余特征的挠点约化映射是单射：约化核的形式群上，乘以剩余特征的单位整数是可逆级数。于是：$3$-初等部分在模 $5$ 处必须为零；$5$-初等部分在模 $3$ 处必须为零；其他素数的挠点同时注入两个有限群。故有理挠子群的阶至多为 $\gcd(4,10)=2$。由于 $T$ 确为非零二阶点，挠子群恰为 $\{O,T\}$。

在 $\mathbb F_{41}$ 中，标准弦切法给出

| $j$ | $j\bar P$ | $j\bar Q$ |
|---|---|---|
| $0$ | $O$ | $O$ |
| $1$ | $(40,4)$ | $(9,24)$ |
| $2$ | $(23,38)$ | $(32,30)$ |
| $3$ | $(23,3)$ | $(32,11)$ |
| $4$ | $(40,37)$ | $(9,17)$ |
| $5$ | $O$ | $O$ |

例如倍点斜率分别为
$$
\lambda_P=\frac{3\cdot40^2-17}{2\cdot4}=29,
\qquad
\lambda_Q=\frac{3\cdot9^2-17}{2\cdot24}=3
\quad\text{in }\mathbb F_{41},
$$
再应用 $x(2A)=\lambda_A^2-2x(A)$、$y(2A)=\lambda_A(x(A)-x(2A))-y(A)$ 即得到表中第二行倍点。后面的行可用同一群律验证。

两个五阶循环群的非零点的 $x$ 坐标集合分别为 $\{40,23\}$ 与 $\{9,32\}$，没有交集。因此
$$
\langle\bar P,\bar Q\rangle\simeq(\mathbb Z/5\mathbb Z)^2.
$$
若 $P,Q$ 相关，$H=\langle P,Q\rangle$ 的无挠秩至多为 $1$。由于其挠子群被 $2$ 消灭，$2H$ 是无挠循环群或零群。但 $2$ 在 $\langle\bar P,\bar Q\rangle$ 上可逆，所以 $2H$ 的约化像仍为 $(\mathbb Z/5\mathbb Z)^2$，不是循环群，矛盾。故 $P,Q$ 独立，已得到秩下界 $2$。

## 3. 二次同源下降的具体映射

下面给出秩上界，包含需要的下降核与指数计算，不依赖软件下降。

令 $b=-17$，并写成
$$
E:\ y^2=x^3+bx,
\qquad E':\ Y^2=X^3-4bX=X^3+68X.
$$
存在二次同源
$$
\phi:E\longrightarrow E',\qquad
\phi(x,y)=\left(x+\frac b x,\ y\left(1-\frac b{x^2}\right)\right),
$$
及其对偶
$$
\psi:E'\longrightarrow E,\qquad
\psi(X,Y)=\left(\frac{X-4b/X}{4},\ \frac{Y(1+4b/X^2)}8\right).
$$
这两式在 $x=0$、$X=0$ 处延拓为 $O$，且都把 $O$ 映到 $O$。代入方程可验证它们是非恒定的椭圆曲线态射，因此是群同态；各核分别为 $\{O,T\}$、$\{O,T'\}$，其中 $T'=(0,0)\in E'(\mathbb Q)$。直接代入倍点公式给出
$$
\psi\phi=[2]_E.
$$
例如两边的横坐标都是
$$
\frac{(x^2-b)^2}{4x(x^2+b)},
$$
纵坐标都是
$$
\frac{x^6+5bx^4-5b^2x^2-b^3}{8y^3}.
$$

定义平方类映射
$$
\alpha:E(\mathbb Q)\longrightarrow\mathbb Q^\times/\mathbb Q^{\times2},
\quad
\alpha(O)=1,\quad \alpha(T)=b,\quad \alpha(x,y)=x\quad(x\ne0),
$$
以及同样定义的 $\alpha'$，但将曲线换成 $E'$，故 $\alpha'(T')=-4b=68$。

### 3.1 平方类映射是同态

若一条非竖直直线 $y=mx+c$ 与 $y^2=x^3+bx$ 相交于三个横坐标 $x_1,x_2,x_3$（切线按重数计算），则
$$
x^3-m^2x^2+(b-2mc)x-c^2=0
$$
给出 $x_1x_2x_3=c^2$。第三交点是前两点之和的负元，所以在所有横坐标非零的情形，$\alpha(A+B)=\alpha(A)\alpha(B)$。

剩下的情形也直接成立：负元不改变横坐标；与 $T$ 相加满足 $x(A+T)=b/x(A)$；若 $A+B=T$，应用后一公式于 $B=T-A$，有 $x(A)x(B)=b$。再加上 $T+T=O$ 和 $O$ 的定义，覆盖所有情形。因此 $\alpha$ 是同态；同一论证适用于 $\alpha'$。

### 3.2 核恰是同源像

由 $E'$ 的方程可知，对 $X\ne0$，
$$
x(\psi(X,Y))=\left(\frac{Y}{2X}\right)^2.
$$
反过来，若 $(x,y)\in E(\mathbb Q)$ 且 $x=u^2\ne0$，令
$$
v=y/u,\quad X=2u^2+2v,\quad Y=2uX.
$$
因为 $v^2=u^4+b$ 且 $b\ne0$，$X\ne0$。直接计算得到
$$
X^2-4b=4u^2X,\qquad (X,Y)\in E'(\mathbb Q),\qquad \psi(X,Y)=(x,y).
$$
$O$ 在像中，而 $\alpha(T)=b=-17$ 不是平方类 $1$。因而
$$
\ker\alpha=\psi(E'(\mathbb Q)).
$$

同样，$X(\phi(x,y))=(y/x)^2$。若 $S=(X,Y)\in E'(\mathbb Q)$ 且 $X=s^2\ne0$，令
$$
w=Y/s,\quad x=(s^2+w)/2,\quad y=sx.
$$
利用 $w^2=s^4-4b$，有 $x\ne0$、$x^2-s^2x+b=0$，从而 $(x,y)\in E(\mathbb Q)$ 且 $\phi(x,y)=S$。由于 $\alpha'(T')=68$ 不是平方，得到
$$
\ker\alpha'=\phi(E(\mathbb Q)).
$$

## 4. 两个平方类像的精确计算

先说明一个小的整性事实。对方程 $y^2=x(x^2+b)$，若素数 $\ell$ 不整除整数 $b$，则 $v_\ell(x)$ 必为偶数：当 $v_\ell(x)>0$ 时，$v_\ell(x^2+b)=0$；当 $v_\ell(x)<0$ 时，$v_\ell(x^2+b)=2v_\ell(x)$。两种情形分别给出 $2v_\ell(y)=v_\ell(x)$ 或 $3v_\ell(x)$。因此 $x$ 的平方类只可能含整除 $b$ 的素因子，另加一个符号。

对 $E$ 而言，因 $b=-17$，必有
$$
\operatorname{im}\alpha\subset\{1,-1,17,-17\}.
$$
点 $P=(-1,4)$ 给出 $-1$，点 $T$ 给出 $-17$。由于像是子群，这四个平方类全部出现，故
$$
|\operatorname{im}\alpha|=4.
$$

对 $E'$ 而言，$b'=68=4\cdot17$，可能的素因子为 $2,17$。而 $Y^2=X(X^2+68)$ 强迫非零 $X$ 为正；$\alpha'(T')=68$ 也为正。因此
$$
\operatorname{im}\alpha'\subset\{1,2,17,34\}.
$$
$T'$ 给出平方类 $17$，而 $(2,12)\in E'(\mathbb Q)$ 给出 $2$。所以四个平方类也全部出现，
$$
|\operatorname{im}\alpha'|=4.
$$

## 5. 指数与精确秩

记 $A=E(\mathbb Q)$、$B=E'(\mathbb Q)$。第 3–4 节给出
$$
|A/\psi B|=4,\qquad |B/\phi A|=4.
$$
因为 $\psi\phi=[2]$，映射 $B/\phi A\to\psi B/2A$ 满射，其核为
$$
\ker\psi/(\ker\psi\cap\phi A).
$$
非零的 $T'\in\ker\psi$ 不在 $\phi A$ 中，因为 $\alpha'(T')=17$ 非平凡。因此这个核的阶为 $2$，进而
$$
|\psi B/2A|=\frac42=2,
\qquad |A/2A|=|A/\psi B|\,|\psi B/2A|=8.
$$
Mordell–Weil 定理与第 2 节的挠子群计算给出
$$
|E(\mathbb Q)/2E(\mathbb Q)|=2^{r+1},
\qquad r=\operatorname{rank}E(\mathbb Q).
$$
故 $2^{r+1}=8$，即 $r=2$。连同第 2 节的有限域独立性证书，所有命题均证毕。$\square$

## 6. 与主问题的接口

这使 CM 路线可以始终固定同一条精确秩 $2$ 曲线。本文仅计算了**有理点的同源商**，没有计算所有局部可解覆盖的 Selmer 群，因此不能从第 4 节的像大小推出 $\Sha[2]=0$；这两件事必须区分。

CLS 的公开论文为 <https://arxiv.org/abs/1005.4206>，原文 <https://arxiv.org/pdf/1005.4206>。其 Theorem 1.3 覆盖的是有限范围 $p<30000$；R4 不把这个有限范围延伸成无穷集合。一般的 Mordell–Weil、同源与群律背景可参看 J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer, 2009；本文已展开所用下降映射、核和所有指数计算。
