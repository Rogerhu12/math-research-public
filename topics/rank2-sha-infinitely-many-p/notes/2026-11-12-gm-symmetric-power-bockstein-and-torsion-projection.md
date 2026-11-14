# GM 的对称幂除素数缺陷与实际挠点投影

日期：2026-11-12。状态：本文各线性代数命题、实际投影的三角秩、
临界行的有限和及其最后一项均已证明。没有证明总和对无穷多个素数非零。

使用 [R68 的真实整 Frobenius](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)
及 [R66 的固定除法单位模型](../results/R66-full-weight-one-and-fixed-division-unit-model.md)。
本篇先解释为何模 $p$ 的秩二 Frobenius 子空间不能未经计算就保留到
模 $p^2$，再把那个计算准确代入本题的 $68$ 挠点、$256$ 项组合。
所需一般线性代数在下面直接证明，不以表示论文献中的范围约定作输入。

## 1. 特征 $p$ 的准确短正合列

设 $k$ 是特征 $p>2$ 的域，$V=kX\oplus kY$。
存在自然的 $\operatorname{GL}(V)$ 等变短正合列

$$
0\longrightarrow V^{(1)}
 \stackrel{\mathrm{Fr}}\longrightarrow\operatorname{Sym}^{p}V
 \stackrel{q}\longrightarrow
 \operatorname{Sym}^{p-2}V\otimes\det V
 \longrightarrow0,
\tag{1}
$$

其中 $\mathrm{Fr}(X^{(1)})=X^p$、
$\mathrm{Fr}(Y^{(1)})=Y^p$，而准确的商映射是

$$
q(X^{p-j}Y^j)=
\begin{cases}
jX^{p-j-1}Y^{j-1}\otimes(X\wedge Y),&1\le j\le p-1,\\
0,&j=0,p.
\end{cases}
\tag{2}
$$

**证明。** (2) 的 $p-1$ 个非零像是右端的一组基，
所以满射且核正好是 $kX^p+kY^p$。
对角矩阵的等变性由次数直接给出。
在 $Y\mapsto Y+cX$ 下，所需系数恒等式是
$j\binom ij=i\binom{i-1}{j-1}$。
在 $X\mapsto X+cY$ 下，所需恒等式是

$$
(i+j)\binom{p-i}{j}
  =i\binom{p-i-1}{j}\quad\text{在 }k\text{ 中}.
$$

后一式从整数恒等式
$\binom{p-i-1}{j}
=(p-i-j)\binom{p-i}{j}/(p-i)$ 约化得到；
$i=0,p$ 的端点另由 $(X+cY)^p=X^p+c^pY^p$ 核对。
对角矩阵和这两类 unipotent 变换生成 $\operatorname{GL}_2$，
从而得到 (1)。$\square$

对特征 $p$ 基上的秩二向量丛及连接，同一构造按局部基黏合。
$\nabla(v^p)=pv^{p-1}\nabla v=0$ 表明左端是带 Cartier
典范连接的 Frobenius 拉回；右端的连接是
$\operatorname{Sym}^{p-2}\nabla\otimes\nabla_{\det}$。
因此它确实适用于 GM 丛，但商的秩是 $p-1$。

## 2. 模 $p^2$ 的混合缺陷确实充满该商

在 $\mathbb Z_p[X,Y]$ 中定义

$$
\mathcal C_c(X,Y)=
\frac{(X+cY)^p-X^p-c^pY^p}{p}
=\sum_{j=1}^{p-1}\frac{\binom pj}{p}
             c^jX^{p-j}Y^j.
\tag{3}
$$

它整，并有

$$
\frac{\binom pj}{p}
\equiv\frac{(-1)^{j-1}}j\pmod p.
\tag{4}
$$

故在 (2) 的商中

$$
q(\overline{\mathcal C_c})
=\sum_{j=1}^{p-1}(-1)^{j-1}c^j
       X^{p-j-1}Y^{j-1}\otimes(X\wedge Y).
\tag{5}
$$

当 $c$ 遍历 $\mathbb F_p^\times$ 时，(5) 张成全部 $p-1$ 维商。
更准确地，对 $1\le k\le p-1$，

$$
\frac1{p-1}\sum_{c\in\mathbb F_p^\times}
c^{-k}q(\overline{\mathcal C_c})
=(-1)^{k-1}X^{p-k-1}Y^{k-1}\otimes(X\wedge Y).
\tag{6}
$$

这只用 $\sum_{c\ne0}c^r$ 的有限域正交关系。
所以一般的除 $p$ 缺陷不只落在 (1) 的两个端点。

### 2.1 不存在自然的秩二 Lie 稳定饱和提升

这一障碍在模 $p^2$ 已出现。令
$A=\mathbb Z/p^2\mathbb Z$、
$\mathcal V=A X\oplus A Y$、
$\mathcal S=\operatorname{Sym}^{p}\mathcal V$。
不存在一个秩二自由直和因子 $W\subset\mathcal S$，同时满足：

1. $\overline W=kX^p+kY^p$；
2. $W$ 对 Lie 算子 $E=Y\partial_X$ 稳定。

**证明。** 若存在，可取
$f=X^p+pr$、$g=Y^p+ps$ 为 $W$ 的基，其中 $r,s$ 是次数 $p$
的多项式。模 $p$ 有 $Ef=0$，而 $W$ 是直和因子，
故 $Ef=p(af+bg)$，其中 $a,b\in A$。
右端的 $X^{p-1}Y$ 系数为零。左端为

$$
Ef=pX^{p-1}Y+pEr.
$$

$Er$ 的 $X^{p-1}Y$ 系数只能来自 $r$ 的 $X^p$ 项，
其微分又有一个因子 $p$。因此左端该系数准确为 $p\ne0$，
矛盾。$\square$

这个结论排除的是按一般线性换基自然提升的两维表示；
它**不**排除某个特殊 GM 系统利用额外方程、允许依赖基参数的
非恒定规范，构造另外的相对对象。特别不能据此宣称所有有限维
几何实现都不存在。

## 3. 代入本题的真实整行

以下取惰性 $p\equiv3\pmod4$、$p\ge7$。
R68 已给同一实际 crystalline 矩阵的整函数
$U=U_p$、$V=V_p$，置

$$
H=V/t,\qquad B=U/H,\qquad
W=\frac{M_1U}{(1-4t^2)H^2}.
\tag{7}
$$

它们满足

$$
H,U\in1+t^2\mathbb Z_p[[t]],\qquad
B=1-t^2+O(t^4),\qquad
W=t^4+O(t^6),
\tag{8}
$$

且全部为偶级数。实际中央系数准确是

$$
C_{p+1}=[t^{p+1}]WB^p,\qquad C_{p+1}\in p\mathbb Z_p.
\tag{9}
$$

记 $b=B-1$、$r=(p-3)/2$。因
$\operatorname{ord}_t(Wb^j)=4+2j$，
二项式展开给出**特征零完全相等**的有限式

$$
\boxed{\quad
\frac{C_{p+1}}p
=\frac{[t^{p+1}]W}{p}
+ \sum_{j=1}^{r}\frac{\binom pj}{p}
                    [t^{p+1}]Wb^j.
\quad}
\tag{10}
$$

其中 $[t^{p+1}]W/p$ 整：在 (9) 中，所有 $1\le j<p$
项均带 $p$，而 $Wb^p$ 的次数太高。
因此 (10) 可逐项模 $p$，得到

$$
\frac{C_{p+1}}p\equiv
\frac{W_{p+1}}p+
 \sum_{j=1}^{r}\frac{(-1)^{j-1}}j
                    [t^{p+1}]Wb^j\pmod p.
\tag{11}
$$

这与 R68 的 $\Delta_p(B)$ 完全一致，而非另一条猜测比较：
由于系数属于 $\mathbb Z_p$，令
$\Delta_p(f)=(f(t)^p-f(t^p))/p$，则

$$
\Delta_p(B)
=\Delta_p(b)
+ \sum_{j=1}^{p-1}\frac{\binom pj}{p}b^j,\qquad
\operatorname{ord}_t\Delta_p(b)\ge2p.
\tag{12}
$$

所以 $W\Delta_p(b)$ 不影响目标次数，剩余部分正是 (10)。
式 (4) 解释了截断对数的全部系数，不可把它们一起遗漏。

## 4. 原来的 $256$ 项投影不逐项杀掉混合部分

R66 的实际固定 $M_1$，来自 $68$ 阶标签的指定两个 $256$ 项和，
再取固定线性组合并归一化。这些操作作用在除法单位的代数系数上。
$U,V,H,B$ 都是共同 Legendre 族的函数，不依赖所选挠点标签。
因此该线性组合与乘以

$$
\frac{U}{(1-4t^2)H^2}\,b^j
$$

严格交换。投影以后第 $j$ 个混合级数准确是 $Wb^j$；
没有可再援用的角色正交关系使它整体为零。

更精确地，由 (8)

$$
Wb^j=(-1)^j t^{4+2j}+O(t^{6+2j}).
\tag{13}
$$

故 $Wb,\ldots,Wb^r$ 在
$\mathbb F_p[t]/(t^{p+2})$ 中线性独立：按首次非零次数排列，
它们的系数矩阵为三角形，对角元均为单位。
实际挠点投影后的这个有限 jet 子空间维数仍为
$(p-3)/2$。这里证明的是明确的三角秩；没有把它误作任意
微分模或相对 cohomology 实现的最小秩。

### 4.1 最后一个实际临界项恒为单位

对最大的 $j=r$，次数 $4+2r=p+1$，故

$$
[t^{p+1}]Wb^r=(-1)^r.
$$

它在 (11) 的贡献恒为

$$
\boxed{\quad
\frac{(-1)^{r-1}}r[t^{p+1}]Wb^r
=-\frac1r=\frac23\quad\text{在 }\mathbb F_p.
\quad}
\tag{14}
$$

因此真实投影并未把整个混合缺陷消掉。要证明首层有限性，
准确还需证明

$$
\frac{W_{p+1}}p+
 \sum_{j=1}^{r-1}\frac{(-1)^{j-1}}j
                    [t^{p+1}]Wb^j
\ne-\frac23\pmod p
\tag{15}
$$

对无穷多个惰性素数成立。已知最高项非零不能单独排除这个抵消。

## 5. 与主目标的严格接口

R66 的准确规范是

$$
C_{p+1}=
\frac{(p+1)!}{24\,17^{p-3}}\beta_{p+1}^2,
\qquad \beta_{p+1}=[z^{p+1}]A_1(z).
\tag{16}
$$

因为 $(p+1)!/p\equiv-1\pmod p$，(11) 的非零准确等价
$\beta_{p+1}\not\equiv0\pmod p$；这给 R50/R54 中的惰性初级
有限性充分条件。它仍是首层判据，不是完整 $J'_{A,p}(0)$ 的
必要条件。

本篇的新增点是：把一般的 Sym$^p$ 混合商、实际整
Frobenius 行、原挠点组合和最终有限和完全接合，并明确保留
一个恒为单位的末项。进一步的正面推进必须控制 (15) 的实际
余项，或在更深完整导数证书中得到新的跨素数约束。
