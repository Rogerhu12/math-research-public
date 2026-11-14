# R429 — 原来源两深度网格、倒 sigma 的严格符号与真实 norm-three 分组

日期：2026-11-14。**状态：已证明。** R339 的实际非零深域可以再限制到
只有两个独立深度：五个无权深 sigma 输入共用 $n$，全部原 Theta 对的
两个 sigma 输入共用 $r$。对每个原普通好素数，原 norm-three 展开的
次数 $m$ 可在任意 $K+1$ 个连续正整数中选择，$K=(p-7)/6$，使每个
任意深的两深度网格都有真实中央导数非零域。新证明只要求完整聚合
系数非零，不声称该系数是单位。也可从 $3,6,\ldots,3(K+1)$ 选择
$m$，使全部 Theta 输入逐三项准确组成 R424 的原来源 $L/J_{12}$。
原完整中央零到这些隐藏输入域的运输仍须另证。

## 1. 同一个原目标和两深度输入域

沿用 R339、R427 的原 $E_b:y^2=x^3+b$、$b=17$、sigma、
$\Theta=x\sigma^2$、$\delta^2=-3$、$\gamma=(5+\delta)/2$，以及
$$
p>7,\qquad p\equiv1\pmod6,\qquad p\ne17,\qquad
K=(p-7)/6,\qquad d=p-1.
\tag{1}
$$
目标仍是同一固定来源
$$
S=-\frac1{84}\sigma(z)\sigma(2z)\sigma(\delta z)
                 \sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z).
\tag{2}
$$
任取正整数 $m$，只对原 $\sigma(2z)$ 使用准确展开
$$
\sigma(2z)=\delta^m\sigma(2\delta^{-m}z)
                       \prod_{h=1}^m\Theta(2\delta^{-h}z).
\tag{3}
$$
原输入与尺度完整保留：
$$
\boldsymbol c=(\delta,2\delta,\gamma,\bar\gamma,2\delta^{-m}),
\quad q_h=2\delta^{-h},\quad C_m=-\delta^m/84,
$$
$$
Q_m=\Omega^{-2m}\prod_{h=1}^m
 \left(X_{h,+}X_{h,-}-\frac{X_{h,+}^2+X_{h,-}^2}{2}\right),
\quad
Y=x_0+\sum_{i=1}^5c_iX_i+
          \sum_{h=1}^m q_h(X_{h,+}+X_{h,-}).
\tag{4}
$$
同一原测度为 $C_mY_*(Q_m\nu_\sigma^{\otimes(6+2m)})$。

本篇只用其中明确的两深度域
$$
\boxed{\mathcal D_{m;n,r}=
\{x_0\in\mathbf Z_p^\times,\quad
 X_i\in p^n\mathbf Z_p\ (1\le i\le5),\quad
 X_{h,+},X_{h,-}\in p^r\mathbf Z_p\ (1\le h\le m)\}.}
\tag{5}
$$
取 $n,r\ge1$，则原输出 $Y$ 自动为单位。
记这一域原 principal 函数为 $J_{m;n,r}(u)$。
所有这些域的质量均为零：五个不在权 $Q_m$ 中的 sigma 深输入
各自质量为零。这里不是对 Theta 的相加输出单独施加 $p^r$ 条件。

## 2. 倒 sigma 每个系数的严格符号

写同一曲线的实际展开
$$
\sigma(z)=zA_b(z^6),\qquad
A_b(w)=\sum_{j\ge0}\alpha_jw^j,\qquad
A_b(w)^{-1}=\sum_{j\ge0}\beta_jw^j,\qquad
\alpha_0=\beta_0=1.
\tag{6}
$$
这里对 $b=17$ 使用有理系数；本节事实上适用于任意正有理 $b$。

**引理。** 对每个 $j\ge0$，
$$
\boxed{(-1)^j\beta_j>0.}
\tag{7}
$$

证明：设
$$
x(z)=z^{-2}+\sum_{j\ge1}a_jz^{6j-2}.
$$
同一原曲线的 $x''=6x^2$ 与首项给
$$
a_1=-b/7,\qquad
a_j=\frac{\sum_{i=1}^{j-1}a_i a_{j-i}}{(6j+1)(j-1)}
\quad(j\ge2).
\tag{8}
$$
比较 $z^{6j-4}$ 即得递推：左侧与 $12x$ 交叉项的系数差为
$6(6j+1)(j-1)$。于是归纳有
$$
a_j=(-1)^j b^j u_j,\qquad
u_1=1/7,\quad
u_j=\frac{\sum_{i=1}^{j-1}u_i u_{j-i}}{(6j+1)(j-1)}>0.
\tag{9}
$$
由 $(\log\sigma)''=-x$ 以及原 CM 规范无二次项，
$$
\log A_b(w)=
 \sum_{j\ge1}\frac{(-1)^{j+1}b^ju_j}{6j(6j-1)}w^j.
$$
所以
$$
\boxed{\log\frac1{A_b(-w)}
 =\sum_{j\ge1}\frac{b^ju_j}{6j(6j-1)}w^j}
\tag{10}
$$
的每个系数严格为正。对其形式指数，每个系数非负，且仅第一项
$b w/210$ 的 $j$ 次幂已经给出
$$
(-1)^j\beta_j\ge\frac{(b/210)^j}{j!}>0
\qquad(j\ge1).
$$
这证明 (7)。这是原 sigma 的完整递推证明，不依赖其任意有限
Taylor 扫描，也不假定 sigma 本身的所有系数有某种符号。证毕。

## 3. 有限选择 m，支付所有 Theta 聚合后的非零

定义真正的有理多项式
$$
P_K(a)=[w^K]\frac{A_b(w)}{A_b(aw)}
      =\sum_{j=0}^K\alpha_{K-j}\beta_j a^j.
\tag{11}
$$
其最高系数准确是 $\beta_K$，故 (7) 给
$$
\boxed{\deg P_K=K.}
\tag{12}
$$
置
$$
a_m=\delta^{-6m}=(-27)^{-m}\qquad(m\ge1).
\tag{13}
$$
这些有理数两两不同。因此至多 $K$ 个不同的正整数 $m$ 能满足
$P_K(a_m)=0$。特别地：

- 任意给定 $m_0\ge1$，在 $m_0,m_0+1,\ldots,m_0+K$ 中至少有一个
  $m$ 满足 $P_K(a_m)\ne0$；
- 更一般，任意 $K+1$ 个不同正整数中都能如此选择；
- 可取 $1\le m\le K+1$，也可取
  $m\in\{3,6,\ldots,3(K+1)\}$。

这一步在 $\mathbf Q$ 中成立，故在每个原普通 $p$ 处仍是非零
等式；没有用有限域乘法阶、Artin 型条件或模 $p$ 猜测。

由原准确乘积 (3)，全部 Theta 的真实聚合为
$$
\boxed{\mathcal E_m(z):=\prod_{h=1}^m\Theta(2\delta^{-h}z)
 =\frac{\sigma(2z)}{\delta^m\sigma(2\delta^{-m}z)}
 =\frac{A_b((2z)^6)}{A_b(a_m(2z)^6)}.}
\tag{14}
$$
因此其完整 $6K$ 次系数是
$$
\boxed{[z^{6K}]\mathcal E_m=2^{6K}P_K(a_m)\ne0.}
\tag{15}
$$
这里已相加全部 Theta 指数碰撞。没有只挑一组低次数单项式，
也没有从 R427 的个别单位系数推断完整聚合仍是单位。

## 4. 两变量解析函数和同一实际非零系数

保持原 sigma 全测度 core
$$
\nu_\sigma|_p=\lambda_\sigma[\kappa]_*\nu_\sigma,\qquad
\lambda_\sigma=\varepsilon^3/\bar\pi\in\mathcal O^\times,\qquad
\kappa=p/\bar\pi^2,\quad v_p(\kappa)=1.
$$
令 $\mathcal G_m(T,U_1,\ldots,U_m)$ 为 R427(8) 的完整解析函数，
并把所有 Theta 对深度同步：
$$
\begin{aligned}
\mathcal H_m(T,U)
={}&\mathcal G_m(T,U,\ldots,U)\\
={}&C_md\,U^{2m}
 \int_{x_0\in\mathbf Z_p^\times}\int
 \log_p\left\langle x_0+T\sum_{i=1}^5c_iX_i+
                         U\sum_{h=1}^m q_hZ_h\right\rangle
 d\nu_\sigma(x_0)\prod_i d\nu_\sigma(X_i)
                         \prod_h d\nu_\Theta(Z_h).
\end{aligned}
\tag{16}
$$
全部 Theta 都保留完整测度；$U^{2m}$ 是全部原二次权的真实缩放。
R427 的逐对等深返回给
$$
\boxed{J'_{m;n,r}(0)
 =\lambda_\sigma^{5n+2mr}\mathcal H_m(\kappa^n,\kappa^r).}
\tag{17}
$$
这是 (5) 中原 $6+2m$ 个 sigma 输入的返回，不是把一个新联合的
相同边际当成原输入域。

R427 已付在 $(p\mathcal O)^2$ 上的完整解析性；也可直接从 log
第 $R$ 项分母只贡献 $-v_p(R)$ 得到一致收敛。五个 sigma 的零
质量杀掉 log 常数项。

考虑明确的系数 $[T^5U^{2m+6K}]\mathcal H_m$。五个 sigma 正矩
都从一次开始，故 $T^5$ 强制它们的指数全是一。Theta 块的总指数
准确为 $6K$，总 log 指数为 $5+6K=p-2$，是奇数。
又有 $C_m\prod_i c_i=1$。完整多项系数与正矩阶乘相消，得
$$
\boxed{
[T^5U^{2m+6K}]\mathcal H_m
=d(p-3)!\,I_{-(p-2)}\,\Omega^{p-2}\,2^{6K}P_K(a_m).}
\tag{18}
$$
其中是 R339 的同一个原单位负矩
$$
I_{-(p-2)}
 =\int_{\mathbf Z_p^\times}x^{-(p-2)}d\nu_\sigma(x)
 \equiv(1-\lambda_\sigma\kappa)\Omega\pmod p.
\tag{19}
$$
它为单位；$d,(p-3)!,\Omega,2$ 也为单位。按第3节选择 $m$ 后，
(18) 严格非零。**本篇不声称 $P_K(a_m)$ 或 (18) 是单位**，
也不声称其赋值在 $p$ 间一致有界。

## 5. 原非零域只需两个独立深度

**定理。** 对每个 (1) 中的普通好素数，按第3节选择 $m$。
任意 $n_0\ge1$，都存在整数 $n,r\ge n_0$，使
$$
\boxed{J'_{m;n,r}(0)\ne0.}
\tag{20}
$$
还可预先指定任意 $D\ge0$，并分别要求 $n\ge r+D$ 或
$r\ge n+D$；在这两个指定区域各自仍存在一个非零域。

证明：若全部 $n,r\ge n_0$ 的值均为零，由 (17) 的非零 core
因子，$\mathcal H_m$ 在
$\{\kappa^n:n\ge n_0\}\times\{\kappa^r:r\ge n_0\}$ 上为零。
固定 $r$，一变量解析恒等定理使 $T$ 方向恒零；再随 $r\to\infty$
对 $U$ 方向使用同一定理，得到 $\mathcal H_m=0$，与 (18) 矛盾。

若只假定 $n\ge r+D$ 的全部值为零，固定任意 $r\ge n_0$ 后，
仍有趋于零的无限 $T$ 零点，故同一论证成立。交换两个方向，
即得另一指定区域的结论。证毕。

两深度始终独立。本篇没有把 $n=r$ 上的所有值赋为非零，也没有
从二变量非零推断其对角限制非零。若全部深 sigma 输入同步，
会重新组成原未展开的五 sigma 块；那个单深度限制是另一个问题。
展开次数 $m$ 与系数指数随 $p$ 变化，但曲线、原目标 (2) 和原
输入恒等式始终不变。

## 6. 可同时保留原 L/J12 的完整 norm-three 来源

利用第3节对任意 $K+1$ 个不同正整数的选择，取
$m=3\ell$、$1\le\ell\le K+1$ 且 $P_K(a_m)\ne0$。
R424 的真实来源为
$$
E_{26}(z):=\frac{L(z)}{J_{12}(z)}
 =\frac{\sigma(3\delta z)}{3\delta\sigma(z)}
 =\Theta(z)\Theta(\delta z)\Theta(3z).
\tag{21}
$$
对每个 $j=1,\ldots,\ell$，置 $q=2\delta^{-3j}$。
原连续三项的尺度是 $\delta^2q,\delta q,q$，
而 $\delta^2=-3$、$\Theta$ 为偶函数，故准确有
$$
\Theta(2\delta^{-(3j-2)}z)
\Theta(2\delta^{-(3j-1)}z)
\Theta(2\delta^{-3j}z)=E_{26}(2\delta^{-3j}z).
$$
因此
$$
\boxed{\mathcal E_{3\ell}(z)
 =\prod_{j=1}^{\ell}E_{26}(2\delta^{-3j}z).}
\tag{22}
$$
每份 $E_{26}$ 都是 R424 中同一个固定 norm-three 来源的单位尺度
推前；(22) 逐项来自原 Theta 对，没有更换二次权或隐藏输入。

当所有这 $6\ell$ 个原成对 sigma 输入处于深度 $r$，完整返回仍是
(17)；聚合后只把每个 (22) 的输入尺度乘 $\kappa^r$，
并保留原权因子 $\kappa^{6\ell r}$ 及 sigma core 因子
$\lambda_\sigma^{6\ell r}$。不能把它改读为仅限制某个 $E_{26}$ 输出
落在 $p^r$ 的事件。

## 7. 已付范围与下一准确接口

本篇把 R339 的独立隐藏深度缩到两个，并可同时让第二块由原
$L/J_{12}$ 的实际 norm-three 三元组组成。R424 的
$$
\int \mathbf1_{Y\in\mathbf Z_p^\times}(p-1)\log_p\langle Y\rangle
            \,\varphi(X)\,d\nu_H
=-\frac23J'_S(0)\int\varphi\,d\nu_{B_{38}}
$$
已经允许任意完整第二输出测试。要据此使用 (20)，仍须证明
(5) 的两个原输入块可以在保留输出、全部权及补域的条件下，
进入这条真实联合恒等式。相同边际或 (22) 的相同因子名称
都不足以免费完成该运输。

- [R339：同一原目标、原二次权及负矩单位](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R427：对内等深返回及完整多变量函数](R427-original-paired-depth-grid-and-unit-collapsed-theta-coefficients.md)。
- [R424：原 H 条件中央与真实 norm-three 三元组](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。

