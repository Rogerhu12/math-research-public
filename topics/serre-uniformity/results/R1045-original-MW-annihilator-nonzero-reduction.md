# R1045：真实 MW 消去保留原 CM 圆盘的单位尺度

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
global_route / root；residue 与 Euler 两半分别经 o2_high_coefficient、
o1_theta 独立纸审。

**已证明：R1037 的真实本原 Mordell–Weil 消去泛函，
作用于 R1044 的整个原 CM 圆盘轮廓后，约化不是零多项式。**
因此原 $p\varepsilon$ 共同尺度在这个实际消去后仍准确，
即 R1033 的 $M=1$ 不因这次 MW 消去而丢失。

这里不宣称最高列 $J_0$ 的值为单位，不宣称最低 $w$ 次数
是一，也没有由非零多项式推出原正赋值子盘只有 CM 点。
证明保留完整的 $\overline{\mathcal Q}^2\lambda$，没有用一个
简化的裸首项取代实际消去向量。

先证明的纯代数断言适用于全部
$p=6N+5\ge41$。几何应用在本文只消费 R1044 已付清的
$p\equiv11\bmod12$ 情形；另一行须由其自己的实际几何接入。

## 1. 纯代数的原有限多项式及实际对应

令
$$
p=6N+5\ge41,\qquad \ell=2N+2=(p+1)/3.
$$
$\ell$ 总为偶数；本篇纯代数部分不要求 $N$ 奇。
在特征 $p$ 中，令 $Q$ 是下列有限多项式的单首归一化：
$$
\frac{Q(y)}{Q(0)}
=\sum_{i=0}^{N}
 \frac{(-N)_i^2}{(2N+3)_i\,i!}y^i,
\qquad A(b)=bQ(b^3),\qquad r=1-b^3 .
\tag{1045.1}
$$
所有显示的分母为单位，最高系数非零。
它满足
$$
y(1-y)Q''+\frac43(1-2y)Q'-\frac{25}{36}Q=0.
\tag{1045.2}
$$
从这个 ODE 的 $y=0$ 递推，次数 $\le N$ 的多项式解由
常数项唯一确定。反射 $y\mapsto1-y$ 保持该 ODE，
比较最高系数给
$$
Q(1-y)=(-1)^NQ(y).
\tag{1045.3}
$$
所以 $Q(0)Q(1)\ne0$。
在其它点，若 $Q,Q'$ 同时为零，ODE 的递推会使所有
直到次数 $N<p$ 的系数为零，矛盾。
因此 $Q$ 和 $A$ 的根都简单，且 $A$ 的根避开 $r=0$。

直接对 $A=bQ(b^3)$ 求导，(1045.2) 等价于
$$
\mathcal LA=0,\qquad
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b.
\tag{1045.4}
$$
这正是 R1023/R1037 原 $p\equiv11\bmod12$ 族的 $A$，
不是一个只拥有相同次数的替代多项式。

置
$$
\lambda(b)=-\frac{6(b+1)}r
=\frac4{b-1}-\frac2{b-\zeta}-\frac2{b-\zeta^2},
\quad \zeta^2+\zeta+1=0,
\tag{1045.5}
$$
$$
\mathscr F(b)=\frac{6(b^p+1)}{r^{\ell+1}A(b)^2}.
\tag{1045.6}
$$
(1045.4) 使 $\mathscr F$ 在各 $A$-根的简单极部为零。
具体地，$f=r^{4N+2}$ 满足 $f'/f=4b^2/r$，
且 $A''/A'=4b^2/r$ 于 $A=0$；
又
$$
\mathscr F=-\frac{f\,\lambda(b^p)}{A^2},
$$
其中 $\lambda(b^p)$ 的导数为零。
故存在准确的部分分式分解
$$
\mathscr F=\sum_{A(s)=0}\frac{d_s}{(b-s)^2}+R(b),
\tag{1045.7}
$$
$R$ 在全部 $A$-根正则，只在三个 $r=0$ 点有极，
并且 $R=O(b^{-2})$ 于无穷远。
原算子和原首 log 源满足
$$
\boxed{\quad
\overline{\mathcal Q}\lambda=-R,\qquad
\bar v=(1-\overline{\mathcal Q})\lambda=\lambda+R.
\quad}
\tag{1045.8}
$$
这就是 R1023/R1037 的完整源。
也可从 R1037 的系数固定 quotient 定义直接核准：
更换 $\lambda$ 的多项式代表后，差含 $A^p$，
除 $A^2$ 后在根集的值仍为零。
所以 (1045.8) 没有丢掉一个 polynomial remainder。

## 2. 更强的纯代数正交断言

定义原 new 多项式空间
$$
\mathcal T_{\rm new}
=\left\{
T_+(b^3)+b^2T_-(b^3):
\deg T_+\le N,\ \deg T_-\le N-1
\right\}.
\tag{1045.9}
$$
其维数为 $2N+1=\ell-1$，所有次数小于
$\deg A=3N+1<p$。

对 $T\in\mathcal T_{\rm new}$，令
$$
F_T=T/A,\qquad
\mathcal B_T(a)
=-\frac12\sum_{A(s)=0}\frac{T(s)a(s)}{A'(s)}
\tag{1045.10}
$$
（$a$ 只需在根集正则）。

本篇核心定理是
$$
\boxed{\quad
T\ne0,\quad \mathcal B_T(\lambda+R)=0
\quad\Longrightarrow\quad
\text{不存在 }\gamma\in k\text{ 使 }
(b-1)^\ell\mid T-\gamma A .
\quad}
\tag{1045.11}
$$
这里 $k$ 可为任何包含这些数据的完美系数域，或其代数闭包。
证明用完整根集的 residue，并不需要把每一个根单独定义在
某个固定有限域上。

在原几何中，R1037 的系数固定映射是
$$
T_c\equiv\frac{f\,c(b^p)}{A'}\pmod A,\qquad \deg T_c<\deg A.
\tag{1045.12}
$$
R1036/R1044 的准确 $B$-公式给
$$
B(c,a)=\mathcal B_{T_c}(a).
\tag{1045.13}
$$
实际 normalized new 向量 $c$ 的指数类是 $0,1\bmod3$；
因为 $p\equiv2\bmod3$，其 $T_c$ 正好落在 (1045.9)。
$c(b^p)$ 的外部系数保持不变，不能擅自改成一般的 $c^p$。
该映射可逆，故 $c\ne0$ 时 $T_c\ne0$。

## 3. 保留全部 $Q^2$ 的 residue 计算

设反面 contact 成立，写
$$
T-\gamma A=O((b-1)^\ell),\qquad
F_T(1)=\gamma.
\tag{1045.14}
$$
先核准 $\gamma\ne0$。
若 $\gamma=0$，$T$ 在 $b=1$ 有至少 $\ell$ 重零。
它只有 $\ell-1$ 个不同的单项式次数，全部小于 $p$。
前 $\ell-1$ 个 Taylor 方程的矩阵是 falling-factorial
Vandermonde；其 determinant 是
$\prod_{e<e'}(e'-e)$ 乘阶乘单位，非零。
所以 $T=0$，与假设矛盾。

### 3.1 简单极部给 $3\gamma$

由 (1045.9)，
$$
F_T(1)+F_T(\zeta)+F_T(\zeta^2)=0.
$$
又 $F_T=O(b^{-1})$、$\lambda=O(b^{-2})$ 于无穷远。
因此全局 residue 定理和 (1045.5) 给
$$
\begin{aligned}
\mathcal B_T(\lambda)
&=\frac12\sum_{\xi^3=1}\operatorname{Res}_{b=\xi}
 F_T\lambda\,db\\
&=\frac12\bigl(4F_T(1)-2F_T(\zeta)-2F_T(\zeta^2)\bigr)
=3\gamma.
\end{aligned}
\tag{1045.15}
$$

### 3.2 原 $R$ 的完整高极部

同样，$F_TR=O(b^{-3})$ 于无穷远，且 $R$ 在全部 $A$-根正则。
在三个 CM 点，$\mathscr F-R$ 正则。
所以
$$
\boxed{\quad
\mathcal B_T(-R)
=-\frac12\sum_{\xi^3=1}
 \operatorname{Res}_{b=\xi}F_T\mathscr F\,db.
\quad}
\tag{1045.16}
$$
这个 $-R$ 正是完整 $\overline{\mathcal Q}\lambda$。
下面并未将 $\overline{\mathcal Q}^2\lambda$ 从指定 $c$ 中删除。

置 $y=b^3$，并将 $T$ 写成 (1045.9)。
三个 CM 点到 $y=1$ 均不分歧，trace of differentials 保留完整三点。
对 $b^a db$，只有 $a\equiv2\bmod3$ 的项保留，
其 trace 为 $y^{(a-2)/3}dy$。
因此恰好只有
$T_+b^{p-3}db$ 和 $T_-b^{-1}db$ 两项留下：
$$
\sum_{\xi^3=1}\operatorname{Res}_{b=\xi}F_T\mathscr F\,db
=
6\operatorname{Res}_{y=1}
 \frac{y^{\ell-2}T_+(y)+y^{-1}T_-(y)}
 {(1-y)^{\ell+1}Q(y)^3}\,dy .
\tag{1045.17}
$$
trace 的三条分支与 $db=dy/(3b^2)$ 的 $1/3$ 已相消，
没有另乘或漏掉一个三。

令 $x=y-1$。因为 $\ell$ 偶，
$(1-y)^{-(\ell+1)}=-x^{-(\ell+1)}$。
从 (1045.16) 得
$$
\mathcal B_T(-R)
=3[x^\ell]\frac{y^{\ell-2}T_+(y)+y^{-1}T_-(y)}{Q(y)^3}.
\tag{1045.18}
$$
在所需次数 $\le\ell<p$ 内，$\ell\equiv1/3\bmod p$
使 $y^{\ell-2}\equiv y^{-5/3}$。
所有分数幂都指 $y=1$ 处常数项一的实际形式根，
也可用 $3\ell=p+1$ 和 Frobenius 直接核这个有限截断，
不涉及超过 $p$ 的 binomial 分母。

置
$$
H(y)=\frac{T_+(y)}{Q(y)}
       +y^{2/3}\frac{T_-(y)}{Q(y)}.
$$
因为 $F_T=y^{-1/3}H$，(1045.14) 给
$$
H(y)=\gamma y^{1/3}+\eta x^\ell+O(x^{\ell+1}).
\tag{1045.19}
$$
于是
$$
\boxed{\quad
\mathcal B_T(-R)=3\gamma S_0+\frac{3\eta}{Q(1)^2},
\qquad
S_0=[x^\ell]\frac{y^{-4/3}}{Q(y)^2}.
\quad}
\tag{1045.20}
$$

## 4. 完整原系数 $S_0$ 准确等于一

(1045.3) 与 $\ell$ 偶给
$$
S_0=[z^\ell]\frac{(1-z)^{-4/3}}{Q(z)^2}.
$$
在次数 $\le\ell<p$ 中，
$$
(1-z)^{-4/3}\equiv(1-z)^{2\ell-2},
$$
因为 $2\ell-2\equiv-4/3\bmod p$。
故可计算同一个 rational function
$$
W(z)=\frac{(1-z)^{2\ell-2}}{Q(z)^2}.
\tag{1045.21}
$$
分子次数 $2\ell-2$，分母次数 $2N=\ell-2$；
$Q$ 单首且 $2\ell-2$ 偶，所以 polynomial part 的次数是
$\ell$，最高系数准确为一。

每个 $Q$-根 $\alpha$ 不为 $0,1$。
写其 double 与 simple principal parts 为
$$
\frac{a_\alpha}{(z-\alpha)^2}
+\frac{b_\alpha}{z-\alpha}.
$$
由 (1045.2)，
$$
\frac{b_\alpha}{a_\alpha}
=
\frac{4}{3(1-\alpha)}
+\frac{4(1-2\alpha)}{3\alpha(1-\alpha)}
=\frac4{3\alpha}.
\tag{1045.22}
$$
因此这一 **完整** 双极部加简单极部在 $z=0$ 的
$z^\ell$ 系数为
$$
\frac{a_\alpha}{\alpha^{\ell+2}}
 \left(\ell+1-\frac43\right)=0.
$$
每个根都包含，全部 proper parts 的该系数均为零。
加回 polynomial part，严格得到
$$
\boxed{\quad S_0=1.\quad}
\tag{1045.23}
$$
这不是从有限素数值推断，也没有只选一个 CM 或 SS 点。

由假设 $\mathcal B_T(\lambda+R)=0$、(1045.15) 和 (1045.20)，
$$
0=\mathcal B_T(\lambda)-\mathcal B_T(-R)
=-\frac{3\eta}{Q(1)^2}.
$$
所以 $\eta=0$。
(1045.19) 遂使 $F_T-\gamma$ 的零阶提高为 $\ell+1$：
$$
\boxed{\quad (b-1)^{\ell+1}\mid T-\gamma A.\quad}
\tag{1045.24}
$$
唯一使用正交性的地方就是这个 **额外的一阶**。
没有假设原 new contact determinant 对所有 $p$ 非零。

## 5. Euler 算子严排这额外一阶

令
$$
\mathcal E=\{0,3,\ldots,3N\}\cup\{2,5,\ldots,3N-1\},
\quad |\mathcal E|=2N+1=\ell-1,
$$
$$
\vartheta=b\partial_b,\qquad
P_{\mathcal E}(\vartheta)=\prod_{e\in\mathcal E}(\vartheta-e).
\tag{1045.25}
$$
它杀掉整个 (1045.9)。
其微分阶数为 $\ell-1$，系数在 $b=1$ 正则。
所以 (1045.24) 及 $\gamma\ne0$ 迫
$$
Y=P_{\mathcal E}(\vartheta)A
\quad\text{在 }b=1\text{ 至少有二重零}.
\tag{1045.26}
$$

为准确识别这个有限多项式，置
$$
P_i=\prod_{e\in\mathcal E}(3i+1-e).
$$
直接将两组等差因子分开，有
$$
P_0=\frac{(3N-1)!}{3^{N-1}(N-1)!}\ne0,
$$
$$
\frac{P_i}{P_0}
=\frac{(4/3)_i(2/3)_i}
 {(1/3-N)_i(2/3-N)_i},
\qquad 0\le i\le N.
\tag{1045.27}
$$
最后的 $i=N$ 也保留；每个分母在此范围都为单位。
将 (1045.1) 的系数代入，因
$2N+3\equiv4/3\bmod p$，得到完整恒等式
$$
Y(b)=Q(0)P_0\,b\,G(b^3),
$$
$$
\boxed{\quad
G(y)=\sum_{i=0}^{N}
 \frac{(-N)_i^2(2/3)_i}
 {(1/3-N)_i(2/3-N)_i\,i!}\,y^i .
\quad}
\tag{1045.28}
$$
$G(0)=1$、$\deg G=N$。
没有在这里使用无限超几何函数或其复 Gamma 值。

记
$b_1=1/3-N$、$b_2=2/3-N$、$\theta=y\partial_y$。
从相邻有限系数的比值直接核得
$$
\left[
\theta(\theta+b_1-1)(\theta+b_2-1)
-y(\theta-N)^2(\theta+2/3)
\right]G=0 .
\tag{1045.29}
$$
最高 $y^{N+1}$ 项因 $(N-N)^2=0$ 也消失，
所以这是整个多项式的 ODE。

(1045.26) 迫 $G(1)=G'(1)=0$。
若 $G\ne0$，令 $j\ge2$ 为其在 $y=1$ 的最小非零次数。
必有 $j\le N<\ell<p$。

把 (1045.29) 写在 $y=1+x$。
最高普通三阶导数的系数首项是 $-x$，
普通二阶导数的常数系数是
$$
(b_1+b_2-2)-(2/3-2N)=-5/3.
$$
所以若 $G=a_jx^j+\cdots$，最低 $x^{j-2}$ 系数准确为
$$
-a_jj(j-1)\left(j-\frac13\right)
=-a_jj(j-1)(j-\ell).
\tag{1045.30}
$$
四个因子都非零，矛盾。
故二重零不可能；(1045.24) 被排除，
从而证明纯代数断言 (1045.11)。

## 6. 原完整圆盘上的真实 MW 应用

现回到 R1044 已完整证明的 $p=12g-1>37$ 原几何，
并取 R1026/R1037 的同一个绝对阈值 $C_*$：
当 $p>C_*$，原
$$
v=\varepsilon^{-1}e_1\log P,\qquad
P=(p-1)(3-N_{\rm deck})[c_1-c_0]
$$
的负 $\delta$ 首分量为单位。
R1035–R1037 在实际整 Lie 格中构造了
$$
\mathcal Q=\varepsilon^{-2}\Phi\Pi,\qquad
D=\frac{\delta-\delta^{-1}}{\zeta-\zeta^2},
$$
以及真正的本原整 MW 消去泛函
$$
\Lambda_{\mathcal Q}(w)=B(v,\mathcal QD e_1w)
                    =B(D\mathcal Qv,e_1w).
\tag{1045.31}
$$
它杀掉整个原 MW 对数空间及其饱和格，不只是一个普通标量的
$v$ 直线；这个事实完全消费 R1036/R1037，未在本篇缩弱量词。

其约化 row 是
$$
\boxed{\quad
c=D\overline{\mathcal Q}\bar v
 =D\overline{\mathcal Q}
       (1-\overline{\mathcal Q})\lambda .
\quad}
\tag{1045.32}
$$
R1037 的精确 kernel 和负 $\delta$ 单射给 $c\ne0$；
它属于原 new 空间。
由于 $D\overline{\mathcal Q}$ 对 $B$ 反自伴，
$$
B(c,\bar v)=0.
\tag{1045.33}
$$
这一步保留了 (1045.32) 的完整
$\overline{\mathcal Q}^2\lambda$。

若 $\overline{\Lambda_{\mathcal Q}(\mathcal H(w))}$ 是零多项式，
R1044 的全部实际系数旗标和准确 contact 判据给
$$
(b-1)^{4g}\mid T_c-\gamma A
\quad\text{某 }\gamma\in k.
$$
这里 $\ell=4g$，(1045.13)、(1045.33) 满足纯代数断言的
正交假设，且 $T_c\ne0$。
(1045.11) 给矛盾。
因此
$$
\boxed{\quad
\overline{\Lambda_{\mathcal Q}(\mathcal H(w))}\ne0,
\qquad
\deg\overline{\Lambda_{\mathcal Q}(\mathcal H(w))}
\le4g-1 .
\quad}
\tag{1045.34}
$$

R1033 已在同一个原 $w=(a-1)/p^3$ 圆盘上证明全部系数整，
包括所有 $p$ 倍积分次数和 formal/log 的完整尾。
(1045.34) 遂证明至少一个实际系数为单位。
所以
$$
\boxed{\quad
\min_n v_p\!\left(
[w^n]\frac{\Lambda_{\mathcal Q}(\log\operatorname{Abel}(P(w)-c_1))}
                  {\varepsilon}\right)=1.
\quad}
\tag{1045.35}
$$
这是实际 MW 消去后的 $M=1$，不是从全型的 $M=1$ 自动传递。

同一证明还有精确的更强范围：
任何原 new 整泛函，若在这个同一 Lie 格中本原且杀掉
$e_1\log P$，其 row 的约化 $c\ne0$ 满足
$B(c,\bar v)=0$，便同样具有非零的完整原约化轮廓。
特别适用于满足这些条件的实际 new MW 消去泛函。
这不声称任意 Néron 商换格都保留本原性。

## 7. 尚须完成的真实事项

(1045.34) 不规定哪个 $w$ 次数有单位系数。
最高列 $J_0$ 或最低线性系数仍可能为零；
本篇也没有将全 new jet determinant 宣称为单位。
证明只排除了与原 $\bar v$ 正交的非零 new row
落在完整 contact 核内。

所以仍须计算原低系数，或给能够排除
$v_p(w)>0$ 非零根的进一步实际论证。
非零多项式及原 $M=1$ 不能独自推出该子盘唯一零点。
$p\equiv5\bmod12$ 的应用亦须先支付它自己的双无穷/两中心
全部系数旗标；纯代数部分不代替那个几何接口。
O0 的完整全局覆盖和 Serre 一致性的绝对界仍未由本文完成。

## 来源与计算范围

- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)：
  原 $A,Q,\lambda,\mathscr F,R$ 及完整首 log 源。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)、
  [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：
  实际 $B,\mathcal Q,D,v$、系数固定的 $T_c$、
  真整本原性和全部 MW 消去量词。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md)：
  完整原系数旗标及其 contact 等价，没有只取几个参考列。
- [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)：
  原 $p\varepsilon$ 尺度、所有分母、原参数及完整收敛尾界。
- [R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)：
  原负 $\delta$ 首列的绝对阈值 $C_*$。

全部新恒等式由完整 residue、原有限多项式和纸面 ODE 递推证明。
没有数学程序执行，没有重复有限素数窗口，也没有引用未经重建的
新预印本断言。
