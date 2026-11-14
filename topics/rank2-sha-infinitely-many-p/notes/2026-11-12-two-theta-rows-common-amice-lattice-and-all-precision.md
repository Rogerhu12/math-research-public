# 两条实际秩二 theta 行的共同整格与全精度矩阵

日期：2026-11-12。状态：本文的共同商坐标、完整单位核、整行满射、
全精度截断及自然参数乘法公式均已证明。没有证明两条原中央导数
在无穷多个素数上不同时消失。

与 R151 的关系是明确的：本文把两真实行及全部多项式乘积放入同一个
可截断的局部矩阵，并保留自然 $w=z^4$ 的分母成本；它不把单列
Mellin 行等同于饱和 vanishing-jet 的评价范数。

## 1. 同一个实际输入和商参数

使用共同 $E_0:y^2=x^3-x$ 尺度。R51/R115/R117 已认证的两个截面满足

$$
A_2(z):=\frac{A(2z)}{16}=z^4+O(z^8),\qquad
B(z)=R(x(z)^2)A_2(z),
\tag{1.1}
$$

$$
R(X)=\frac{(X+1)Q_8(X)}{(X-1)H_1(X)H_2(X)},
$$
$$
\begin{aligned}
Q_8&=X^8+364X^6-1088X^5+1190X^4-1088X^3+364X^2+1,\\
H_1&=X^4+4X^3+70X^2+4X+1,\\
H_2&=X^4+20X^3-26X^2+20X+1.
\end{aligned}
\tag{1.2}
$$

两者的 theta 次数都是 $68$。固定普通素数
$p\equiv1\pmod4$、$p\ge13$、$p\ne17$，记

$$
d=p-1=4r.
\tag{1.3}
$$

在同一完整未分歧系数环 $\mathcal O$ 中选 R117 的整正式群同构

$$
t(T)=\exp_{E_0}(\Omega_p\log(1+T)),\qquad
\Omega_p\in\mathcal O^\times.
\tag{1.4}
$$

这里 $t=-x/y$，$[i]t=it$；乘法群上的相应作用则是
$[i]T=(1+T)^i-1$，不能替成 $iT$。
定义实际有理乘子给出的坐标

$$
V(T)=R(x(t(T))^2)-1.
\tag{1.5}
$$

由 R117 的准确首项，

$$
V=-22t^4+O(t^8)=-22\Omega_p^4T^4+O(T^5).
\tag{1.6}
$$

$22$ 在所有当前素数处为单位。于是有**整个整环**的等式

$$
\boxed{\quad
\mathcal O[[T]]^{\mu_4}
 =\mathcal O[[t^4]]
 =\mathcal O[[V]].
\quad}
\tag{1.7}
$$

第一步使用 (1.4) 的整可逆坐标和 $[i]t=it$；第二步是首系数为单位
的严格形式逆函数定理。不存在有限精度之后未控制的反向分母。

实际 $A_2$、$B$ 在此成为

$$
\mathcal A_2(T)=F(V(T)),\qquad
\mathcal B(T)=(1+V(T))F(V(T)),
$$
$$
F(V)\in V\mathcal O[[V]],\qquad F(V)=-V/22+O(V^2).
\tag{1.8}
$$

$F\in\mathbb Q[[V]]$ 本身固定不随 $p$ 改变：先把固定的 $A_2(z)$
和固定的 $V(z)$ 作为 $z^4$ 级数相互代换即可。
其在当前位的整性来自真实普通 sigma/Amice 整性及 (1.7)，不是
假定任意正次数 theta 在所有素数处都整。

记同一公共包络为

$$
\mathscr L=T^4\mathcal O[[T]]\cap\mathcal O[[T]]^{\mu_4}
            =V\mathcal O[[V]].
\tag{1.9}
$$

这是保留原四阶消失的整 Amice 格。实际输入是其中一个固定元素
$F(V)$；本文没有宣称其余任意元素仍来自原全局 theta 或 ODE。

## 2. 完整单位质量与真正 Mellin 导数核

任意 $X(T)\in\mathcal O[[T]]$ 对应唯一有界整测度 $\mu_X$。
在整个 $\mathbb Z_p$ 上定义

$$
m_p(x)=\mathbf1_{\mathbb Z_p^\times}(x),\qquad
f_p(x)=
\begin{cases}
\log\langle x\rangle/\log(1+p),&x\in\mathbb Z_p^\times,\\
0,&x\in p\mathbb Z_p.
\end{cases}
\tag{2.1}
$$

令 $M_p(X)=\int m_p\,d\mu_X$、$\Lambda_p(X)=\int f_p\,d\mu_X$。
两者均是整有界线性行。对 $j\ge0$，使用同一个实际 $V$ 定义

$$
M_j(X)=M_p(V^jX),\qquad L_j(X)=\Lambda_p(V^jX).
\tag{2.2}
$$

乘法是 Amice 乘法，对应完整的加法卷积。因此 (2.2) 没有先截掉
任何非单位支撑。对差分 $\Delta f(x)=f(x+1)-f(x)$，若
$V(T)^j=\sum_n v_{j,n}T^n$，其对偶核准确为

$$
M_j:\ \sum_n v_{j,n}\Delta^n m_p,
\qquad
L_j:\ \sum_n v_{j,n}\Delta^n f_p.
\tag{2.3}
$$

这是 Mahler 展开的平移公式。模任何 $p^N$ 时，§4 将把这些和变成
真正有限的和。

实际两条曲线已经给出

$$
M_0(F)=M_1(F)=0.
\tag{2.4}
$$

确实，$M_0(F)=J_{A_2}(0)=0$，而
$M_p(B)=M_0(F)+M_1(F)=0$。在 R117 的原曲线规范下，

$$
L_0(F)=\frac{17}{16}J_{17,p}'(0),\qquad
L_0(F)+L_1(F)=34^2J_{34,p}'(0).
\tag{2.5}
$$

第一式中的伸缩 $[2]$ 本来还给一个乘 $J_A(0)$ 的对数项；它因
真实质量零而消失。所有显示的常数都是当前位的单位。
所以两个目标的共同中央失败，准确是 $L_0(F)=L_1(F)=0$。
没有为 $j\ge2$ 添加未经证明的质量或斜率消失。

## 3. 同一格上首精度的完整行空间

### 3.1 核的准确 Mahler 次数

在全体 $x\in\mathbb Z_p$ 上有

$$
m_p(x)\equiv x^d\pmod p,
\qquad
\boxed{\quad
f_p(x)\equiv\frac{x^{2d}-x^d}{pd}\pmod p.
\quad}
\tag{3.1}
$$

右边是 $p$ 整值多项式。对单位，$x^d=1+pq$，其右边模 $p$ 为
$q/d$，正是 (2.1)；对非单位，分子的赋值至少为 $d$，除 $p$ 后
仍为零模 $p$。这一步保留了单位边界。

以 $\binom xn$ 为 Mahler 基，两个核模 $p$ 的最高非零次数分别为
$d$、$2d$，最高系数分别是

$$
d!\equiv-1\pmod p,\qquad
\frac{(2d)!}{pd}\equiv1\pmod p.
\tag{3.2}
$$

后一个式子中 $(2p-2)!/p\equiv-1$，再除 $d\equiv-1$ 即得。
因 $\Delta\binom xn=\binom x{n-1}$，(1.6)、(2.3) 说明

$$
\deg_{\rm Mahler}\overline M_j=d-4j,\qquad
\deg_{\rm Mahler}\overline L_j=2d-4j
\quad(0\le j<r),
\tag{3.3}
$$

最高系数分别为 $-v_4^j$、$v_4^j$，其中
$v_4=-22\Omega_p^4\in\mathcal O^\times$。
高于 $T^{4j}$ 的项只能降低 Mahler 次数，不能抵消这些首项。

### 3.2 整分裂满射与实际两行的准确指数

(3.3) 的 $2r$ 个次数互不相同，且最小为四。
以对应 $T^n$ 作为有限个源向量，所得到的模 $p$ 子矩阵为单位三角矩阵。
各核在 $x\mapsto ix$ 下不变；因此先施加真实平均

$$
e_4X(T)=\frac14\sum_{\zeta\in\mu_4}X((1+T)^\zeta-1)
\tag{3.4}
$$

不改变任一行的值，且保持 $T^4\mathcal O[[T]]$。
故这些源向量可全部取在 (1.9)。有限矩阵在 $\mathcal O$ 上的行列式
为单位，得到整分裂满射

$$
\boxed{\quad
\mathscr L\longrightarrow\mathcal O^{2r},\qquad
X\longmapsto(M_j(X),L_j(X))_{0\le j<r}.
\quad}
\tag{3.5}
$$

还有准确的完备性。Mahler 次数至多 $2d$ 的多项式核在 tame
$\mu_4$ 作用下有整分次旗标；第 $n$ 个一维分次的特征是 $\zeta^n$。
因四可逆，不变部分维数为 $2r+1$。除去在 $\mathscr L$ 上为零的
常数核后，维数为 $2r$，恰由 (3.3) 填满。

尤其，置

$$
\mathscr L_0=\ker M_0\cap\ker M_1\subset\mathscr L,
\qquad
\mathscr L_N=\{X\in\mathscr L_0:L_0(X),L_1(X)\in p^N\mathcal O\},
$$

则

$$
\boxed{\quad
\mathscr L_0/\mathscr L_N\simeq(\mathcal O/p^N)^2,
\qquad\operatorname{length}_{\mathcal O}(\mathscr L_0/\mathscr L_N)=2N.
\quad}
\tag{3.6}
$$

这是真正同一个整 Amice 包络中的指数，两个已知质量条件已经先取核。
若系数环剩余域无限，应使用显示出的长度而非写成有限集合的基数。
(3.6) 并不表示实际固定 $F$ 可以在这个包络中任意改变；它也不是
R151 饱和多项式截面格的 arithmeticity 常数。

## 4. 全部有限精度只需线性于 $Np$ 的共同截断

对 $s\ge1$ 定义整多项式

$$
E_s(X)=X^s\sum_{h=0}^{s-1}\binom{s+h-1}{h}(1-X)^h.
\tag{4.1}
$$

它满足 $E_s\equiv0\pmod{X^s}$、$E_s\equiv1\pmod{(X-1)^s}$，
次数至多 $2s-1$。固定精度 $N\ge1$，置

$$
\mathfrak f_N(x)=
\frac{E_{N+1}(x^d)}{d\log(1+p)}
\sum_{h=1}^{2N}\frac{(-1)^{h+1}}h(x^d-1)^h.
\tag{4.2}
$$

这是一个 $\mathcal O$ 整值多项式，并在**全体** $\mathbb Z_p$ 上满足

$$
\boxed{\quad
f_p\equiv\mathfrak f_N\pmod{p^N},\qquad
m_p\equiv E_N(x^d)\pmod{p^N},\qquad
\deg\mathfrak f_N\le d(4N+1).
\quad}
\tag{4.3}
$$

证明如下。单位处 $x^d-1\in p\mathbb Z_p$；对数尾项 $h>2N$ 在
除 $\log(1+p)$ 后的赋值至少
$h-v_p(h)-1\ge(h-1)/2\ge N$。
截断本身除 $\log(1+p)$ 后整，而 $E_{N+1}-1$ 至少有 $N+1$ 层，
故选择器不降低精度。
非单位处 $v_p(x^d)\ge d$，所以 (4.2) 的赋值至少
$d(N+1)-1-\lfloor\log_p(2N)\rfloor\ge N$。
这同时证明整值性，且没有对非单位使用 $\log x$。
最后，次数为 $d((2N+1)+2N)$。

整值多项式的 Mahler 展开是有限的，其系数都在 $\mathcal O$。
因此 $M_p(X)$、$\Lambda_p(X)$ 模 $p^N$ 只依赖

$$
X(T)\pmod{p^N,T^{d(4N+1)+1}}.
$$

对实际不变环 (1.7)，准确可改写为同一个有限商

$$
\boxed{\quad
\mathcal Q_{p,N}=
\mathcal O[[V]]/(p^N,V^{J_N+1}),\qquad
J_N=r(4N+1).
\quad}
\tag{4.4}
$$

因为整坐标变换保持 $T$-阶，$V$ 的阶恰为四；tame 平均在模
$p^N$ 商上仍然精确。于是乘 $V$、乘真实 $1+V$、乘实际固定 $F(V)$
以及取任意多项式乘积，均可在 (4.4) 中进行。
这里只用同一个普通周期框架；没有另行宣称所有条目已经消去周期。

## 5. 自然参数 $w=z^4$：准确分布和唯一可能的一层分母

把 $w$ 免费当成整 Amice 函数会有错误，因为

$$
w=\Omega_p^4\log(1+T)^4.
\tag{5.1}
$$

但可在实际局部解析分布中精确处理它。对有界测度 $\mu_X$，定义
$\nabla^k\mu_X(g)=\mu_X(g^{(k)})$。其 Amice 变换为
$\log(1+T)^kX(T)$。质量核在各个开闭剩余球上常数，而在单位球上

$$
f_p^{(k)}(x)=\frac{(-1)^{k-1}(k-1)!}{x^k\log(1+p)}
\qquad(k\ge1).
$$

非单位球上这些导数全为零。因此对全部 $a\ge1$，准确有

$$
\boxed{\quad
M_p(w^aX)=0,\qquad
\Lambda_p(w^aX)=
-\frac{\Omega_p^{4a}(4a-1)!}{\log(1+p)}
       \int_{\mathbb Z_p^\times}x^{-4a}\,d\mu_X(x).
\quad}
\tag{5.2}
$$

没有边界分布项：单位集合是 $p$ 进开闭集，各导数在各开球上定义。
特别地，$p\Lambda_p(w^aX)\in\mathcal O$；显示的阶乘可能增加整性，
而 $\log(1+p)$ 只有一层 $p$。它不能被无证删去。

负权核也有统一有限多项式。令

$$
0\le e_a<d,\quad e_a\equiv-4a\pmod d,
\qquad q_a=(4a+e_a)/d\in\mathbb Z_{>0}.
$$

则

$$
\mathfrak u_{a,N}(x)=E_N(x^d)x^{e_a}
 \sum_{h=0}^{N-1}(-1)^h\binom{q_a+h-1}{h}(x^d-1)^h
\tag{5.3}
$$

在全 $\mathbb Z_p$ 上模 $p^N$ 代表
$\mathbf1_{\mathbb Z_p^\times}x^{-4a}$，且
$\deg\mathfrak u_{a,N}\le d(3N-1)$，与 $a$ 的大小无关。
单位处这是 $(x^d)^{-q_a}$ 的整二项式展开；非单位由 $E_N$ 消去。

因此计算 (5.2) 乘 $p$ 后模 $p^N$，仍只需 (4.4)，外加所显示的
准确单位 $p/\log(1+p)$、$\Omega_p^{4a}$ 及整阶乘。
不随 $a$ 或源多项式次数增大而另扩 Amice 截断。

## 6. 全部实际混合列的共同有限矩阵

对任意 $a,b,c\ge0$，令

$$
X_{b,c}(V)=F(V)^{b+c}(1+V)^c.
\tag{6.1}
$$

它准确对应 $A_2^bB^c$，而不是把乘积的 Mellin 变换写成乘积。
对给定精度 $N$，在 (4.4) 中先算
$x_j^{b,c}=[V^j]X_{b,c}$。
把 §4、§5 中的多项式核展开为 Mahler 系数，并以实际 $V(T)^j$
配对，得到有限行

$$
\mathsf C^{(a)}_j=p\Lambda_p(w^aV^j)\pmod{p^N}
\qquad(0\le j\le J_N).
$$

于是

$$
\boxed{\quad
p\Lambda_p(w^aA_2^bB^c)
 =\sum_{j=0}^{J_N}\mathsf C^{(a)}_j x_j^{b,c}\pmod{p^N}.
\quad}
\tag{6.2}
$$

这对所有源次数 $D$ 及 $a+b+c\le D$ 同时成立。
它使用一个统一商环、实际固定 $F$ 和 $R$，保留所有自然参数幂和
完整单位边界；没有对每个混合列另选 theta 规范。

**一个实际不可略去的校准。** 取 $a=r-1$、$X=A_2$。
模 $p$ 在单位上 $x^{-4a}=x^4$，且
$\int x^4d\mu_{A_2}=24\Omega_p^4$。所以

$$
\boxed{\quad
p\Lambda_p(w^{r-1}A_2)
 \equiv-24\Omega_p^{p-1}(p-6)!\not\equiv0\pmod p.
\quad}
\tag{6.3}
$$

这来自原实际首项，并不要求先知道两条原中央导数中哪个非零。
故不能把它们的共同消失直接传播成所有混合列上同一 Mellin 行的消失。
该列总次数为 $r$，但其首消失阶也只有 $r$；它不是
$k\asymp D^2$ 前缀核中的一个截面。因而 (6.3) **不**被当作那个
深带饱和 jet 范数的下界。

## 7. 准确保留的全球缺口

现在两条真实秩二行在同一整格上的完整关系为 (2.4)、(2.5)，
全部精度和全部多项式混合列可由 (4.4)、(6.2) 处理。
这是原有有限 Newton 行的共同输入矩阵，不是新的自由测度模型。

但只从 $L_0(F)=L_1(F)=0$ 尚未得到 R151(4.4) 所需的同一前缀
线性关系对全部源列成立。高 $j$、乘积、以及 (5.2) 的负权行都有
显示出的真实数据；(3.5) 说明这些行在包络中并不自动受前两行控制。
把实际 $F$ 的固定 ODE 和全球初值接到这个共同有限矩阵，仍是待付步骤。
尤其 (3.6) 的长度不能直接从 vanishing-jet 的 maximal-minor 差中相减。

### 直接来源与独立核查

- [两真实行的全卷积](2026-11-12-two-rank-two-theta-linear-convolution.md)：
  (1.1)–(1.8) 的实际截面、$R$、周期尺度及原曲线常数。
- R38、R46、R63、R118：普通整 Amice、全部单位分支以及两条曲线的
  中央零和普通初级有限判据。
- R151：真实有限 Newton 行和需要支付的饱和混合列条件。
- 本文其余步骤是显示出的整形式坐标、Mahler 差分及有限对数/二项式
  计算；§3 的首系数和 §4 的全部精度尾界已由另一子代理独立复核。
