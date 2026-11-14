# R186. 原第一范数块与双中央导数的整系数约束

日期：2026-11-12。**状态：本文的精确恢复、模 $p^3$ 整条件及单位
Jacobian 已证明。** 本篇为单份完整结果。所有系数来自原
$A_2,B$ 两行；两条完整中央零性仍是假设，本篇不由这些有限条件
推出其不可能。

## 1. 原曲线与完整第一块

固定
$$
p=4r-1\ge7,\qquad p\ne11,\qquad R=r(p-1).
\tag{1}
$$
使用 R162、R184 的原规范
$$
a(s)=e^{t(s)},\quad b=sa,\quad
\mathcal A=a^{17}P(s),\quad B=a^{17}Q(s),\quad D_0=B-\mathcal A.
$$
这里 $P,Q$ 是已经严格认定的固定多项式，
$$
P(s)=s+O(s^2),\quad Q(s)-P(s)=-22s^2+O(s^3).
$$
置
$$
V(s)=Q(s)/P(s)-1,\qquad v_0=V'(0)=-22,\qquad S=V^{-1}.
\tag{2}
$$
本篇所有逆函数均取原点分支。由于 $v_0\in\mathbb Z_p^\times$，
$S\in s\mathbb Z_p[[s]]$。定义两个固定的特征零形式芽
$$
H(y)=\mathcal A(S(y)),\qquad
L(y)=\log\frac{v_0H(y)}{y}.
\tag{3}
$$
于是 $H'(0)=v_0^{-1}$，$L(0)=0$。这里的“固定”指其有理系数
不随 $p$ 改变；并不声称 $H,L$ 在全部次数上 $p$ 整。

令 $F(A)=B(s(A))$ 为原图像，其中 $s(A)$ 是
$\mathcal A(s)$ 的逆函数，并置
$$
G(A)=\frac{F(A)-A}{A^2},\qquad G(0)=v_0.
$$
R184 的完整第一齐次范数块有系数
$$
c_j=-\frac{p}{p-j}[A^j]G(A)^{p-j}\qquad(0\le j<p),
\qquad C_p(y)=\sum_{j=0}^{p-1}c_jy^j.
\tag{4}
$$
特别 $c_0=22^p$。这些 $c_j$ 全在 $\mathbb Q\cap\mathbb Z_p$：
可在 R180 取 $N=pr-1$，其整准备多项式与固定范数在
$A$-次数 $<pr$ 一致；本处只读取 $j<p$。

要区分两种截断。R180 的 $n=1$ 原多项式只保留
$j\le(p-1)/2=2r-1$。本篇的 $C_p$ 读取全部 $j<p$，是完整
第一齐次块。以下模 $p^3$ 恢复使用到 $j=3r-1$，不能只用
$n=1$ 已保留的较短块。本文不把延长读取免费算成原多项式源的
新前缀或次数收益。

## 2. 第一块是固定原芽的负 p 次幂

准确恒等式为
$$
\boxed{\quad
c_j=-[y^j]\left(\frac{y}{H(y)}\right)^p\quad(0\le j<p),
\qquad
C_p(y)\equiv22^p e^{-pL(y)}\pmod {y^p}.
\quad}
\tag{5}
$$
证明可直接使用形式留数。由 $y=A G(A)$、$A=H(y)$，对
$j<p$ 有
$$
\begin{aligned}
[y^j](y/H(y))^p
&=\operatorname{Res}H(y)^{-p}y^{p-j-1}\,dy\\
&=\operatorname{Res}A^{-j-1}G(A)^{p-j-1}
                         \{G(A)+AG'(A)\}\,dA\\
&=\left(1+\frac{j}{p-j}\right)[A^j]G(A)^{p-j}.
\end{aligned}
$$
这正是 (4) 的负号。因 $p$ 为奇数且 $v_0=-22$，第二式随即
得到。没有对 $j=p$ 使用分母 $p-j$ 的式子。

因此在 $\mathbb Q_p[y]/(y^p)$ 中，原固定芽可准确恢复为
$$
\boxed{\quad
L(y)\equiv-\frac1p\log\bigl(C_p(y)/22^p\bigr)\pmod {y^p}.
\quad}
\tag{6}
$$
有限形式对数的分母小于 $p$；(6) 中唯一显式的额外 $p$ 分母
是前面的 $1/p$。这不是由范数系数的整性推断 $L$ 整。

## 3. 与 R185 的同一整轴准确对接

记 R185 的实际整轴为
$$
f(\xi)=g_{A_2}(\xi),\qquad g(\xi)=g_B(\xi),\qquad
T(\xi)=g(\xi)/f(\xi)-1.
$$
则 $f,g\in\xi\mathbb Z_p[[\xi]]$，$f'(0)=g'(0)=1$，
$T'(0)=v_0$。原曲线在同一坐标中的准确式是
$$
\mathcal A=\psi(\xi)^{17}f(\xi),\qquad
B=\psi(\xi)^{17}g(\xi),\qquad
\psi(\xi)=\Gamma|_{\rm curve}.
$$
R185 (24) 给
$$
\psi(\xi)=e^{u_0\xi^r}\{1+O(\xi^{pr})\},\qquad
v_p(u_0)=-1,\qquad \xi=w+O(w^{R+1}),\quad w=z^4.
\tag{7}
$$
最后一个换元使 $w^r-\xi^r=O(\xi^{pr})$，因此 (7) 的误差阶在
换元后仍保持。以下置
$$
b_*=17u_0,\qquad v_p(b_*)=-1.
\tag{8}
$$

在 (4) 作同一轴的 Lagrange 换元，得到对全部 $0\le j<p$ 的
**准确特征零公式**
$$
\boxed{\quad
c_j=-[\xi^{p-1}]
 T(\xi)^{p-j-1}T'(\xi)
 \left(\frac{\xi}{f(\xi)}\right)^p
 e^{-p b_*\xi^r}.
\quad}
\tag{9}
$$
确实，$G=T/\mathcal A$，所以负整数幂的 Lagrange 公式先给
(9) 中的 $\psi^{-17p}$。所需次数小于 $p<pr$，(7) 允许把它
准确替换成显示的指数。这里没有对次数 $17p$ 套用 R185 的
Stokes 赋值定理。

指数只需四项：
$$
e^{-p b_*\xi^r}
\equiv\sum_{h=0}^{3}\frac{(-p b_*)^h}{h!}\xi^{rh}
                         \pmod{\xi^p}.
\tag{10}
$$
对给定 $j$，更只需 $h\le\lfloor j/r\rfloor$。又因为
$f/\xi\in1+\xi\mathbb Z_p[[\xi]]$，
$$
\left(\frac{\xi}{f}\right)^p
\equiv1-p\log(f/\xi)\pmod{(p^2,\xi^p)}.
\tag{11}
$$
对数与指数在此有限截断中只有小于 $p$ 的阶乘和整数分母，
所以 (11) 是整截断环内的式子。

## 4. 从真实范数块整地恢复前三组中央轴

令
$$
N=3r-1<p,\qquad
Y(\xi)=V\bigl(s(w=\xi)\bigr)\pmod{\xi^{N+2}}.
\tag{12}
$$
这里 $s(w)$ 是原椭圆曲线的固定换元。R54 的正式群界，或原
$s=x_E^{-2}$ 的 Hurwitz 展开，给其至 $R$ 阶的整性；而
$N+1=3r\le R$。因此 $Y/\xi\in v_0+\xi\mathbb Z_p[\xi]$
在所需范围内。由 (7)，$Y=T\pmod{\xi^{N+2}}$。多读取这一阶
是必要的：下面 $\xi/Y$ 至 $\xi^N$ 的系数需要 $Y$ 至
$\xi^{N+1}$，不能在除去一次 $\xi$ 时损掉该边界。

在 $\mathbb Q_p[\xi]/(\xi^{N+1})$ 中定义
$$
K_p(\xi)=
\left[
 \frac{C_p(Y(\xi))}{22^p}
 e^{p b_*\xi^r}
 \left(\frac{v_0\xi}{Y(\xi)}\right)^p
\right]_{\le N}.
\tag{13}
$$
方括号表示取指定有限截断。由 (5) 以及
$H(Y)=\psi^{17}f$，准确得到
$$
\boxed{\quad
K_p=(f/\xi)^{-p}\pmod{\xi^{N+1}},\qquad
K_p-1\in p\xi\mathbb Z_p[\xi].
\quad}
\tag{14}
$$
后一断言来自 $N<p$：在特征 $p$ 下，任何
$1+\xi\mathbb F_p[[\xi]]$ 的 $p$ 次幂至 $\xi^{p-1}$ 都为
$1$。它不是从形式常数项为 $1$ 自动推出。

置
$$
\mathcal R_p=(K_p-1)/p\in\xi\mathbb Z_p[\xi]/(\xi^{N+1}).
$$
定义以下真正的整多项式表达式（指数亦按 $\xi$-次数截断）：
$$
\mathcal E_N(\mathcal R)=
\left[
 e^{-\mathcal R}
 \left\{1+\frac p2\mathcal R^2+
 p^2\left(\frac{\mathcal R^4}{8}-\frac{\mathcal R^3}{3}\right)\right\}
\right]_{\le N}.
\tag{15}
$$
则
$$
\boxed{\quad
f/\xi\equiv\mathcal E_N(\mathcal R_p),\qquad
g/\xi\equiv(1+Y)\mathcal E_N(\mathcal R_p)
                 \pmod{(p^3,\xi^{N+1})}.
\quad}
\tag{16}
$$
证明是在有限截断中展开
$$
-\frac1p\log(1+p\mathcal R)
\equiv-\mathcal R+\frac p2\mathcal R^2
                         -\frac{p^2}{3}\mathcal R^3\pmod{p^3},
$$
再取指数。因为 $N<p$，出现的相关阶乘分母均为单位。
(15) 的 $\mathcal R^4/8$ 是二次指数项，不能删去。

计算 (16) 需原 $C_p$ 的系数至模 $p^4$，因为 (14) 后有一次
真正除以 $p$。其余精确有理输入 $Y,pb_*$ 可在同样精度计算。
所读取的最大系数指标为 $3r-1$；更高 $c_j$ 不会回流。

## 5. 两条实际模 p³ 中央条件

对 $H(\xi)\in\mathbb Z_p[\xi]/(\xi^{N+1})$，定义
$$
\mathcal D_{b_*}(H)=
 [\xi^{r-1}]H-b_*^{-1}[\xi^{2r-1}]H
                       +2b_*^{-2}[\xi^{3r-1}]H.
\tag{17}
$$
R185 的同一组轴权给
$$
\begin{aligned}
\frac{J_{A_2}'(0)}{\lambda_{17,1}}
&\equiv\mathcal D_{b_*}
          \bigl(\mathcal E_N(\mathcal R_p)\bigr)\pmod{p^3},\\
\frac{J_B'(0)}{\lambda_{17,1}}
&\equiv\mathcal D_{b_*}
          \bigl((1+Y)\mathcal E_N(\mathcal R_p)\bigr)\pmod{p^3}.
\end{aligned}
\tag{18}
$$
这里 $b_*^{-1}\in p\mathbb Z_p^\times$，
$\lambda_{17,1}\ne0$。因此两条**完整**中央零性蕴含右边两条
明确整多项式同余为零。反过来，只知这两条有限同余，不能推出
完整导数为零。

模 $p^2$ 时可只取 $N=2r-1$，并在 (15) 删去显式 $p^2$
项；(17) 也只保留前两项。模 $p$ 则只需 $N=r-1$。
所以这三个精度使用同一原块，不是给每个精度另选任意轴。

## 6. 两个指定整系数的单位 Jacobian

本节进一步证明这些有限条件没有在系数换元中变奇异。令
$$
a_j=c_j/p\qquad(1\le j<r).
$$
这些 $a_j$ 为整。事实上 (3) 的 $L_j=[y^j]L$ 在 $j<r$
时整，由 (5) 有
$$
a_j\equiv v_0 L_j\pmod p.
\tag{19}
$$
这里 $t(s)$ 的第一个 $p$ 分母出现在 $s^r$，而 $P,V,S$
在本范围整，故所述低阶整性有直接来源。

令 $\omega(y)=w(S(y))$，则
$\omega(y)=y/v_0+O(y^2)$。在小于 $r$ 的次数内置
$$
M(y)=(y/\omega(y))^r,\qquad M(0)=v_0^r.
$$
因 $\psi^{17}=1+O(\xi^r)$、$f,g$ 从一次开始，
$f_r$ 与 $(g-f)_r$ 仍是原两行在 $w$ 中的这些系数。
Lagrange 公式准确给
$$
\begin{aligned}
f_r&=\frac1{r v_0}[y^{r-1}]e^L(1+yL')M(y),\\
(g-f)_r&=\frac1{r v_0}[y^{r-2}]e^L(2+yL')M(y).
\end{aligned}
\tag{20}
$$
所以第一行对 $L_{r-1}$ 的系数为 $v_0^{r-1}$；
第二行不含 $L_{r-1}$，对 $L_{r-2}$ 的系数亦为
$v_0^{r-1}$。

当 $r\ge3$ 时，把 (18) 两行相减，使用行
$\mathcal D_{b_*}(\mathcal E_N)$、
$\mathcal D_{b_*}(Y\mathcal E_N)$。其对变量
$(a_{r-1},a_{r-2})$ 的 Jacobian 模 $p$ 是三角矩阵，且
$$
\boxed{\qquad
\det\frac{\partial(\text{这两行})}
         {\partial(a_{r-1},a_{r-2})}
 \equiv v_0^{\,2r-4}\in\mathbb F_p^\times.
\qquad}
\tag{21}
$$
其余原系数保持固定时，改变 $c_j=p a_j$ 保持
$K_p\equiv1\pmod p$，故 (15)–(18) 仍定义整系数函数。
(20) 先给模 $p$ 的唯一解，随后普通多变量 Hensel 逐位提升
给模 $p^3$ 的唯一解。因此两条条件对这两个整归一系数构成
一个准确的 Hensel 图；对应原 $c_j$ 的精度是模 $p^4$。

对 $p=7,r=2$，第二行首层直接为
$(g-f)_2=v_0\not\equiv0\pmod7$，故该素数的两个首层不能同时
消失；不使用不存在的 $a_0$ 变量。

式 (21) 是**实际范数系数条件**的单位 minor。它没有把这些
系数当成原有限多项式源的独立列，也没有证明相应六层条件可直接
计入整消失前缀格的指数。要获得那类收益，仍须在原全前缀矩阵中
构造并核对相应整变换。

## 7. 精确校准与依赖

[配套精确校准脚本](../scripts/check-first-norm-block-central-interface.py)
直接由原有理 $P,Q,t$ 展开构造数据，对 $p=7,19,31$ 校准：

- 原 Newton 系数与 (5) 的负幂系数逐项相等；
- 全部 $c_j$ 的 $p$ 整性；
- (6)、(14) 的有限截断准确相等；
- (16) 的模 $p^3$ 恢复；
- (21) 的两变量单位 minor。

这些计算只校准已经给出的形式证明，不以数值模式代替恒等式。
两个非退化情形的 Jacobian 行列式分别为
$7\pmod {19}$、$2\pmod {31}$，与 (21) 相符。

- [R162：原两行的准确平面](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- [R180：整准备多项式及原截断](R180-original-theta-multiple-precision-source-polynomials.md)。
- [R184：完整原范数、齐次支撑及 Lagrange 系数](R184-cyclotomic-norm-source-and-exact-degree-support.md)。
- [R185：同一整轴泛函及完整中央检验](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
