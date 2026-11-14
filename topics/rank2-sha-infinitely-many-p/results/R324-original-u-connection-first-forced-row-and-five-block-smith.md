# R324：原 U 连接的首强迫行与五块整格中的准确 Smith 成本

日期：2026-11-13。**状态：以下固定 $E[6]$ primitive 的首坏分母、原物理前缀的唯一 Smith 因子，以及进入原五块除幂目标后的全部 $p$ 成本均已证明。该强迫行不在原中央轴；本篇不将它计成一个免费的中央非零或高深度条件。**

## 1. 固定原来源与精确 rational primitive

保持 $b=17$、$E_b:y^2=x^3+b$、$dz=dx/(2y)$。
记
$$
X=x^3,\qquad U=\Theta(z)\Theta(2z)^4,\qquad
g=\frac{S}{U}
=\frac{(X+b)(7X^2-4bX+16b^2)}
       {7X(X-8b)^3}.                                          \tag{1}
$$
这是 R320 的同一个原秩二来源，未更改其 theta 规范。

置三个实际有理函数
$$
f_A=\frac y{x^2},\qquad
f_X=\frac{yx}{X-8b},\qquad
f_3=\frac{yx}{(X-8b)^2}.
$$
直接用 $x'=2y,\ y'=3x^2$ 得
$$
\begin{aligned}
f_A'&=-1-\frac{4b}{X},\\
f_X'&=-1-\frac{60b}{X-8b}-\frac{432b^2}{(X-8b)^2},\\
f_3'&=-\frac7{X-8b}-\frac{162b}{(X-8b)^2}
                         -\frac{864b^2}{(X-8b)^3}.
\end{aligned}                                                   \tag{2}
$$
因此设
$$
R=\frac{f_A}{896b}-\frac{f_X}{128b}-\frac{9f_3}{112},
\qquad a=-\frac3{448b},\qquad c=-\frac3{112},
$$
有原恒等式
$$
\boxed{g=R'+a+\frac{c}{X-8b}.}                                  \tag{3}
$$
这也可由 R320 的四个特征列直接合成；所有常数都在 (3) 中。

令
$$
L_6(z)=\int_0^z\frac{dv}{x(v)^3-8b},\qquad
A(z)=U(z)\bigl(R(z)+az+cL_6(z)\bigr).                           \tag{4}
$$
所有函数在原点正规；$R(z)=3z/(448b)+O(z^7)$，
$L_6=z^7/7+\cdots$，所以
$$
A=z^7/7+\cdots,\qquad
\nabla_U A:=A'-\frac{U'}U A=S.                                \tag{5}
$$
$A$ 是规范局部 primitive，含有真实对数项；
这里没有把它当成全局全纯 theta 截面。

## 2. 直到六 p 的真实整性

固定
$$
p=6s-1>7,\qquad p\ne17,\qquad w=z^6.
$$
取 R301 的同一系数
$$
c_p=[z^{p+1}]\log(\sigma(z)/z),\quad
\kappa=34c_p,\quad a_p=p\kappa\in\mathbf Z_p^\times,
$$
以及
$$
\widehat U=e^{-\kappa w^s}U,\qquad
\widehat S=e^{-\kappa w^s}S,\qquad
\widehat A=e^{-\kappa w^s}A.                                  \tag{6}
$$

以下是所需的**有限整性**，比仅使用 Gauss 范数更明确：
$$
\widehat U,\ \widehat U^{-1}\in
\mathbf Z_p[[w]]\pmod{w^p}.                                   \tag{7}
$$
证明可完全从原参数 $u=x^{-1/2}$ 出发：
$$
z=\sum_{n\ge0}
\frac{(-1)^n\binom{2n}{n}b^n}{4^n(6n+1)}u^{6n+1}.              \tag{8}
$$
当 $0\le n<p$，分母唯一可能被 $p$ 整除的项是
$n=(5p-1)/6=5s-1$。此时 $n<p<2n$，
$\binom{2n}{n}$ 恰有一个 $p$，抵消 $6n+1=5p$。
所以 (8) 的相应前缀及其形式逆均整。
特别 $xz^2=(z/u)^2$ 在所需前缀整，常数为一。

写 $x=z^{-2}\sum a_nw^n$。由
$(\log\sigma)''=-x$，
$$
[w^n]\log(\sigma/z)=-\frac{a_n}{6n(6n-1)}.                      \tag{9}
$$
在 $n<p$ 中，(9) 唯一可能的坏项为 $n=s$。
另一方面
$$
U=(\sigma/z)^{34}(xz^2)^{17}(1-8bu^6)^4.
$$
两个后因子的对数在 $n<p$ 都整；去掉准确的
$34c_pw^s$ 后，$\log\widehat U$ 的这些系数均整。
指数化及取逆时只使用小于 $p$ 的阶乘，得 (7)。
同一论证也表明 $R(z)$ 的系数到 $z^{6p}$ 以前整。

## 3. 第一个坏分母在 z 的五 p 次，且余量是单位

原六挠积分在参数 $u$ 中为
$$
L_6=\int
\frac{u^6\,du}{(1-8bu^6)\sqrt{1+bu^6}}.                        \tag{10}
$$
它只含 $z^{6j+1}$。积分分母在 $p$ 处的第一个可能坏项因而是
$6j+1=5p$，即 $j=5s-1$。

设 $n=5s-2$，$h=(p-1)/2=3s-1$。由于 $h<n<p$，在模 $p$ 下
$$
\begin{aligned}
[v^n](1-8bv)^{-1}(1+bv)^{-1/2}
&=b^n\sum_{k=0}^{h}\binom hk8^{n-k}\\
&=b^n8^{n-h}9^h\\
&=b^n2^{p-2}=\frac{b^n}{2}.
\end{aligned}                                                   \tag{11}
$$
这里 $9^h=3^{p-1}=1$，且 $n-h=2s-1$；
没有遗漏几何级数的尾项。

(8) 的逆在此前整、首项为 $z$，故改回 $z$ 不改变首个坏系数的余量：
$$
\boxed{p[z^{5p}]L_6\equiv\frac{b^{5s-2}}{10}\pmod p.}            \tag{12}
$$
严格地说，(10) 在 $u^{5p}$ 之前的积分系数均整，
唯一坏项是该单项式；$u(z)^{5p}=z^{5p}+\cdots$。
因此其他项不能改变乘 $p$ 后的这个首余量。

由 (4)、(7) 和 $c=-3/112$，
$$
\boxed{
p[z^{5p}]\widehat A
\equiv-\frac{3b^{5s-2}}{1120}\not\equiv0\pmod p.}                \tag{13}
$$
其所有更低系数均整。若置
$$
r_*=5s-1,\qquad V=\widehat A/z,
$$
则 (13) 就是 $V$ 在 $w^{r_*}$ 的准确一层分母。

同时对 (3) 求该系数，$R'$ 的贡献被 $5p$ 整除，得到
$$
\boxed{
[w^{r_*}]g\equiv-\frac{3b^{5s-2}}{224}\in\mathbf F_p^\times.}    \tag{14}
$$
这是固定原 $S/U$ 的一个对所有这些 $p$ 成立的强迫行。

## 4. 原物理前缀恰有一个 Smith p

取有限自由格
$$
B=\mathbf Z_p[w]/(w^{5s}),
$$
以及完整连接算子
$$
\mathcal D
=1+6w\partial_w-\widehat W,\qquad
\widehat W=6w\,\frac{\partial_w\widehat U}{\widehat U}.            \tag{15}
$$
由 (7)，这确实是 $B$ 的整算子，$\widehat W(0)=0$。
两个 Gaussian 导数在 (5) 中准确抵消，所以
$$
\mathcal D V=\widehat S.                                      \tag{16}
$$

记 $M_{\widehat U}$ 为乘 $\widehat U$。有真正整共轭
$$
\boxed{
\mathcal D=M_{\widehat U}
 (1+6w\partial_w)M_{\widehat U}^{-1}.}                          \tag{17}
$$
两侧乘法矩阵均为对角一的下三角整矩阵。
中间算子的对角是 $1+6r$，$0\le r\le5s-1$。
这些数依次位于 $1$ 与 $5p$ 之间；若 $p\mid1+6r$，
因 $p\equiv-1\pmod6$，其倍数只能是 $5p$。
又 $p>7$，故该项赋值恰一。于是
$$
\boxed{\operatorname{coker}(\mathcal D:B\to B)
\simeq\mathbf Z_p/p\mathbf Z_p.}                              \tag{18}
$$

该余核的真实观察为
$$
\Lambda_*(F)=[w^{r_*}]\widehat U^{-1}F\pmod p.
$$
由 (14)，
$$
\Lambda_*(\widehat S)
=[w^{r_*}](S/U)\ne0.
$$
所以原物理前缀中的 $\widehat S$ 没有整 primitive；
其规范逆像恰在 (13) 那一角损一个 $p$。
这不是把一条抽象共振对角当成原输入：它的实际余核值已由 (11)–(14) 支付。

## 5. 进入同一五块除幂目标后的准确成本

现在使用原 $q=4$ 的**全部五块**目标，不挤入 R309 的三块目标：
$$
\Gamma=
\mathbf Z_p[w,\epsilon]/(w^s-p\epsilon,\epsilon^5).              \tag{19}
$$
它自由基为
$$
w^r\epsilon^j,\qquad0\le r<s,\quad0\le j\le4.
$$
嵌入 $B\otimes\mathbf Q_p$ 时，
$\epsilon=w^s/p$。原物理格 $B$ 在第 $j$ 块的坐标因此带准确因子 $p^j$：
$$
w^{js+r}\longmapsto p^jw^r\epsilon^j.                          \tag{20}
$$

Euler 算子在这里必须满足
$w\partial_w(\epsilon)=s\epsilon$；
故 (17) 的中间对角为
$$
1+6r+(p+1)j.
$$
唯一非单位仍是 $(r,j)=(s-1,4)$ 的 $5p$。
由于 $\widehat U$ 的系数整且常数为一，
乘 $\widehat U$ 和其逆均保持 $\Gamma$：
每一次往高块的进位只额外乘一个 $p$。
所以 (17)、(18) 在 $\Gamma$ 上也成立。

但是**原输入在该格中的位置已经不同**。
将 $\widehat S$ 先乘 $\widehat U^{-1}$，
其最后一角由 (14)、(20) 给
$$
p^4[w^{r_*}]g.
$$
它已被 $p$ 整除，所以 $\widehat S$ 在 $\Gamma$ 中确实有整逆像。
规范逆像最后一角准确为
$$
\boxed{
\frac{p^4[w^{r_*}]g}{5p}
=p^3\frac{[w^{r_*}]g}{5},
\qquad
p^{-3}\text{该坐标}\equiv
-\frac{3b^{5s-2}}{1120}\pmod p.}                               \tag{21}
$$
这是共轭后的坐标；乘回 $\widehat U$ 只在此余量上增加一个 $p^4$ 的倍数。
因此原 primitive 的真实最后角同样是 $p^3$ 乘单位。

结论是：

- 原物理格的连接映射恰损一个 $p$，且原 $S$ 确实检测到这个余核。
- 五块除幂格中，原输入的最后角先带 $p^4$；逆连接只除一个 $p$，
  留下准确的 $p^3$ 单位层。
- 第五块角 $(s-1,4)$ 对应
  $z^{5p-1}=z^{5(p+1)-6}$，不是原中央轴 $z^{h(p+1)}$，
  也不属于只有三块的 $q^2$ 前缀。
- 若要将它变成原完整中央非零或额外 Smith 深度，
  仍须在 R319/R322 的同一实际来源像中支付相应角向消去。
  不能删掉 (20) 后将 (14) 当成新增的免费中央单位。

本篇是全体 $p$ 的整矩阵证明，无需枚举素数或另设机械复跑门槛。
直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R319](R319-jzero-ramified-three-minimal-unit-and-mixed-scaled-return.md)、
[R320](R320-fixed-six-torsion-five-dimensional-trace-and-full-central-matrix.md)。

