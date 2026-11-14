# R325：三个真零来源的加权归一化、47次关系与40次导子

日期：2026-11-13。**状态：全部为特征零原加权代数的完整结论。三个实际来源的分次函数域、归一化、Hilbert 函数、唯一关系的加权次数及导子首次出现次数均已证明；未把有理导子直接当作任意素数处的 primitive 整格。**

## 1. 同一原 S 的三个来源

固定 R294–301 的 $E:y^2=x^3+b$，$b=17$，$\delta=\sqrt{-3}$，
以及原次数34、原点首项 $z^6$ 的 $S$。置
$$
A=S(z),\qquad B=S(\delta z),\qquad C=S(2z),
\qquad \deg(A,B,C)=(1,3,4).                         \tag{1}
$$
这里次数记录实际 theta charge 与34之比。下述代数记为
$$\mathcal T=\mathbb Q[A,B,C].$$
这与 R309 由 $S,H_3,H_5$ 生成的等权代数不同。R314/R319 的完整缩放公式
保证：若原完整中央导数消失，则 (1) 按各自 charge 定义的三个完整中央导数
同时消失；本文没有额外假定两个质量一参考的导数为零。

置
$$t=-b/x^3,\quad f(t)=B/A^3,\quad h(t)=C/A^4,
\quad q_7(t)=16t^2+4t+7.$$
R314/R319 的实际 sigma 同源公式说明 $f,h\in\mathbb Q(t)$；它们包含全部
carrier，非只对角变量进行替换。把 $A$ 看作次数一的分次函数域参数，于是
$$\mathcal T\subset\mathbb Q(t)[A],\qquad B=A^3f,quad C=A^4h.  \tag{2}$$
该分次解释避免混淆不同 charge。也可在实际 theta 截面代数中作相同构造。

## 2. 完整极点表与分次函数域

设 $r_+,r_-$ 为 $q_7$ 的两个根。实际极点阶如下；零表示没有极：

| $t$ | $0$ | $\infty$ | $1$ | $-1/8$ | $r_+$ | $r_-$ |
|---|---:|---:|---:|---:|---:|---:|
| $h=C/A^4$ | 3 | 2 | 1 | 2 | 3 | 3 |
| $f=B/A^3$ | 2 | 0 | 2 | 1 | 2 | 2 |
| $t:E\to\mathbb P^1$ 的分歧指数 | 6 | 3 | 2 | 1 | 1 | 1 |

**证明。** R297 的原 $S$ 零除子为：原点六阶；两个非零核三挠点各二阶；
三个二挠点各二阶；$x^3=8b$ 的六点各一阶；两组 CM 七同源核的十二点各一阶。
其总次数 $6+4+6+6+12=34$，没有遗漏零点。上表各列正是这些轨道在 $t$ 线的像。

$[2]$ 在三挠点及两个 CM 七核上置换，在二挠点处落到原点，
在所列六挠点处落到非零三挠点。因此 $C/A^4$ 在 $E$ 上的极阶依次是
$18,6,2,2,3,3$；除以表中分歧指数即得第一行。
$[\delta]$ 杀掉所列三挠点，在二挠点和两个 CM 七核上置换，
并将所列六挠点送到非零二挠点。所以 $B/A^3$ 的极阶为
$12,0,4,1,2,2$，给第二行。各映射在特征零中不分歧，所述零阶精确。
分母的零点已经列完，故没有其他极点。$\square$

于是
$$[\mathbb Q(t):\mathbb Q(f)]=9,\qquad
[\mathbb Q(t):\mathbb Q(h)]=14.$$
中间扩张 $[\mathbb Q(t):\mathbb Q(f,h)]$ 同时整除9和14，因此
$$\boxed{\mathbb Q(f,h)=\mathbb Q(t),\qquad
\operatorname{Frac}_{\rm gr}(\mathcal T)=\mathbb Q(t)(A).}       \tag{3}$$
这一步排除了参数化具有隐藏的多重覆盖。

## 3. 归一化是一个明确的有理除子截面环

在 $\mathbb P^1$ 上定义
$$
\boxed{D=\frac34([0]+[r_+]+[r_-])
 +\frac12([\infty]+[-1/8])+\frac23[1],
\qquad \deg D=\frac{47}{12}.}                                 \tag{4}
$$
两个七核点的和在 $\mathbb Q$ 上有定义，故 $D$ 在 $\mathbb Q$ 上有定义。

**定理1。** $\mathcal T$ 在 (3) 中的整闭包为
$$
\boxed{\mathcal N=\bigoplus_{n\ge0}
A^nH^0(\mathbb P^1,\mathcal O(\lfloor nD\rfloor)).}             \tag{5}
$$
特别
$$
\boxed{\dim_{\mathbb Q}\mathcal N_n
=1+3\left\lfloor\frac{3n}{4}\right\rfloor
  +2\left\lfloor\frac n2\right\rfloor
  +\left\lfloor\frac{2n}{3}\right\rfloor.}                     \tag{6}
$$

**证明。** 表中的极阶除以各自次数3或4后，逐点取最大值，正好得到 (4)。
所以 $A,B,C$ 都属于 (5)。截面环 (5) 是正规环：各齐次元素在每个点满足
$v_P(g)+nD_P\ge0$；取公分母后这是离散赋值环的交，连同非负次数条件
给出整闭性。$12D$ 为正次数整除子，故截面环有限生成。

须另付 $\mathcal N$ 对 $\mathcal T$ 的有限性。考虑同次数的三个截面
$$A^{12},\qquad B^4=A^{12}f^4,\qquad C^3=A^{12}h^3.$$
它们在 $\mathcal O(12D)$ 中没有共同零点：在 $D$ 支撑以外，第一项不为零；
在支撑中的每一点，极点表至少有一项达到 (4) 的最大斜率，故第二或第三项
的截面值不为零。相应正次数理想在 $\mathcal N$ 中的根为无关理想。
因此 $\mathcal N/(A^{12},B^4,C^3)\mathcal N$ 有限维，按次数提升一组有限基，
即得 $\mathcal N$ 在 $\mathbb Q[A^{12},B^4,C^3]$ 上有限生成，从而在
$\mathcal T$ 上有限。由 (3) 二者同分式域；正规性和有限性证明 (5)。
最后 $\mathbb P^1$ 上非负次数整除子的截面维数为次数加一，给 (6)。$\square$

这里没有使用“所有足够高次都自动属于原代数”的断言。原代数与归一化之间
仍有真实的射影奇点粘合条件。

## 4. 唯一关系的加权次数恰为47

**定理2。** 存在不可约的加权齐次多项式
$F(X,Y,Z)\in\mathbb Q[X,Y,Z]$，变量权为 $(1,3,4)$，使
$$\boxed{\mathcal T\simeq\mathbb Q[X,Y,Z]/(F),\qquad\deg F=47.} \tag{7}$$
其 Hilbert 级数与典范位移为
$$
\boxed{H_{\mathcal T}(v)=\frac{1-v^{47}}{(1-v)(1-v^3)(1-v^4)},
\qquad\omega_{\mathcal T}\simeq\mathcal T(39).}                \tag{8}
$$

**证明。** 由 (3)，$\mathcal T$ 是维数二的域子环。从三个变量的多项式环到它
的核是高度一齐次素理想，故由单个不可约齐次 $F$ 生成。记其次数为 $e$。
自由分解给 $H_{\mathcal T}=(1-v^e)/((1-v)(1-v^3)(1-v^4))$，
其第 $n$ 次维数的线性主项是 $en/12$。
有限双有理扩张 $\mathcal T\subset\mathcal N$ 的余核支撑维数至多一，
故不改变二者 Hilbert 函数的线性主项。(6) 的主项是 $47n/12$，从而 $e=47$。
三变量带权多项式环的典范模位移为 $-1-3-4=-8$；用上述长度一自由分解取
对偶，得到超曲面典范模位移 $47-8=39$。$\square$

特别，原加权次数小于47时，所有 $A^iB^jC^k$（$i+3j+4k=n$）线性独立。
本定理确定整个关系理想，虽不要求把可能很大的 $F$ 系数展开。

## 5. 导子首次出现于40次，准确为五维

记实际导子理想
$$\mathfrak c=(\mathcal T:\mathcal N)
=\{a\in\mathcal T:a\mathcal N\subset\mathcal T\}.$$
以下位移约定为 $M(q)_n=M_{n+q}$。

**定理3。** 作为分次 $\mathcal N$ 模，
$$
\boxed{\mathfrak c\simeq\omega_{\mathcal N}(-39),\qquad
(\omega_{\mathcal N})_m
\simeq H^0(\mathbb P^1,\omega_{\mathbb P^1}(\lceil mD\rceil)).} \tag{9}
$$
因此
$$\boxed{\mathfrak c_n=0\ (n<40),\qquad
\dim\mathfrak c_{40}=5.}                                      \tag{10}$$
对于 $n\ge40$，令 $m=n-39\ge1$，完整维数为
$$\boxed{\dim\mathfrak c_n
=-1+3\left\lceil\frac{3m}{4}\right\rceil
 +2\left\lceil\frac m2\right\rceil
 +\left\lceil\frac{2m}{3}\right\rceil.}                        \tag{11}$$

**证明。** 正规二维分次环 $\mathcal N$ 为 Cohen–Macaulay。
分次局部对偶和 $\mathbb P^1$ 的 Serre 对偶给
$$
(\omega_{\mathcal N})_m
 =H^1(\mathbb P^1,\mathcal O(\lfloor-mD\rfloor))^*
 =H^0(\mathbb P^1,\omega_{\mathbb P^1}(\lceil mD\rceil)).
$$
这些等式与齐次乘法相容。它也是 Watanabe 的分次典范模公式在本题的形式，
不是把 $\lceil mD\rceil$ 误换成 $\lfloor mD\rfloor$。

有限双有理扩张的典范模满足
$\omega_{\mathcal N}=\operatorname{Hom}_{\mathcal T}
(\mathcal N,\omega_{\mathcal T})$。在共同分式域中，任意这样的线性映射
由乘一个分式给出；因 $1\in\mathcal N$，
$\operatorname{Hom}_{\mathcal T}(\mathcal N,\mathcal T)$ 正是实际导子。
结合 (8)，得 $\omega_{\mathcal N}=\mathfrak c(39)$，证明 (9)。

当 $m\le0$ 时，$D$ 非负，所以
$\deg(K_{\mathbb P^1}+\lceil mD\rceil)\le-2$，没有全局截面。
当 $m=1$ 时，$\lceil D\rceil$ 为表中的六个点，
$\deg(K+\lceil D\rceil)=4$，截面维数为5。
当 $m\ge1$ 时，该次数非负，维数为次数加一，给 (11)。$\square$

### 5.1 将抽象同构落实为原分式域中的五个乘子

这一步表明 (10) 是原导子，非另一个等维空间。取 (7) 的任一规范化 $F$，令
$$P(y,z)=F(1,y,z),\qquad
Q(t)=t(t-1)(1+8t)(16t^2+4t+7).$$
因为 $f$ 非常数且特征零，$f'\ne0$；$P_z(f,h)\ne0$。
超曲面的残数形式在参数 $(A,t)$ 中为
$$
\eta_{\mathcal T}=\frac{dX\wedge dY}{F_Z}
 =A^{-39}\frac{f'(t)}{P_z(f(t),h(t))}\,\frac{dA}{A}\wedge dt.
                                                               \tag{12}
$$
而 $H^0(\omega(\lceil D\rceil))$ 的一组有理基为
$t^jdt/Q(t)$，$0\le j\le4$：五个有限点只允许简单极，
无穷处的简单极条件恰给 $j\le4$。
将其与 (12) 比较，原导子40次部分的一组基就是
$$
\boxed{A^{40}\frac{P_z(f,h)}{f'(t)}\frac{t^j}{Q(t)},
\qquad j=0,1,2,3,4.}                                          \tag{13}
$$
(9) 证明这些分式确实属于 $\mathcal T_{40}$，且乘全部 $\mathcal N$ 仍在
$\mathcal T$。因 $40<47$，它们各自的原单项式表示唯一。
若交换 $f,h$ 作坐标，残数形式给相同导子，只改变一个非零常数。

## 6. 原点消失阶、格成本与当前用途

在 $t=0$，$t$ 的原形式阶为6，$A$ 的原形式阶也是6。由 (5)，
任意 $T\in\mathcal N_n$ 均满足
$$\boxed{\operatorname{ord}_{z=0}T
\ge6\left(n-\left\lfloor\frac{3n}{4}\right\rfloor\right).}    \tag{14}$$
所以这套代数的正次数部分没有原点单位；不能免费使用 R314/R319 中的单位
返回来消去它的正次数成本。归一化累计维数为
$$\sum_{n\le N}\dim\mathcal N_n=\frac{47}{24}N^2+O(N),$$
但把这些维数计入原有限核前，仍须支付 (9) 的导子以及实际整数分母。

全部构造在 $\mathbb Q$ 上有限呈示，因此存在一个固定有限坏素数集，使 (5)、
(7) 及有限组导子生成式可以同时下降到相应局部化整数环。这里的存在性不等于
已经求出了该集合，更不等于原有限 $q^2$ 或五块目标的 Smith 商为单位。
R322 仍须在实际原幂格中完成这些比较；R324 的第五块唯一 Smith 因子
及源的 $p^4$ 补偿也仍须保留。

本篇的已付输入是：完整参数场、准确归一化、关系次数47、原导子起点40及其
五个真实有理乘子。它没有从同一缩放中央零制造新的独立 Stokes 条件，也没有
证明原完整中央导数对无穷多个 $p$ 非零。

## 来源与依赖

- R297：原 $S$ 全部固定挠零除子；R314、R319：实际倍点与范数三 carrier、完整中央缩放。
- K. Watanabe, *Some remarks concerning Demazure's construction of normal graded rings*, Nagoya Math. J. **83** (1981), 203–211，Theorem 2.8；[原文](https://doi.org/10.1017/S0027763000019498)。本文已给本题所需的曲线对偶证明。
- R324：原 $U$ 连接的首强迫行与同一五块有限目标，不能用 (5) 省略其原格代价。
