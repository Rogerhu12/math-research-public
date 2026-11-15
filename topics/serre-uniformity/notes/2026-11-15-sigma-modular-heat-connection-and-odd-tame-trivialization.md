# 原 sigma 的模参数 heat 连接、奇部分可分平凡化和首 p 边界源

日期：2026-11-15。状态：**以下恒等式、可分平凡化、允许 p 的零 p 曲率与首 p 截断方程已证明；原 critical 共同非零仍未证明。**

本篇研究的是模参数方向，不是把固定曲线上的六个 theta 截面误当作六维 D_z 稳定空间。固定曲线的真实闭包与 Hurwitz 高块仍按已有笔记；本篇不重跑计算，不改变原 c=0 规范，不增加素数扫描。

## 1. 家族及两个完全不同的导数

先在特征零中用一般 Weierstrass 家族
$$
y^2=x^3-\frac a4x-\frac b4,\qquad
D_zx=2y,\quad D_zy=3x^2-\frac a4,
\tag{MH1}
$$
以及原 Weierstrass sigma
$$
\sigma=z+O(z^5),\qquad D_z^2\log\sigma=-x.
$$
这里的二次指数仍为零。原课题正是 (a,b)=(0,4)。

令
$$
L=6b\partial_a+\frac{a^2}{3}\partial_b,\qquad
\Delta=a^3-27b^2.
\tag{MH2}
$$
原 sigma 的 heat 方程为
$$
L\sigma=\frac12D_z^2\sigma+\frac{a z^2}{24}\sigma,
\qquad L\Delta=0.
\tag{MH3}
$$
这与 Bunkova, arXiv:1701.00848v2, 式 (1) 的 Q_2 完全同规范；
也等于 Rodriguez Villegas, *On the Taylor coefficients of theta functions of CM elliptic curves*, 式 (2.8) 除二。文献中的模参数导数不可与本篇 D_z 混用。

记 eta=D_z log sigma。直接对 (MH3) 求 z 导数得到
$$
L\eta=-y-\eta x+\frac{az}{12},\qquad
Lx=2x^2+2\eta y-\frac a3,
$$
$$
Ly=3xy+\eta\left(3x^2-\frac a4\right).
\tag{MH4}
$$

## 2. 真实六维 heat 闭合及原规范

取一般家族上的六个截面
$$
S=\sigma^6,\quad F=x\sigma^6,\quad H=x^2\sigma^6,\quad
J=y\sigma^6,\quad G=-xy\sigma^6,\quad
R=(x^3+b/2)\sigma^6.
\tag{MH5}
$$
用 J 表示原 y sigma^6，避免与下节辅助曲线坐标 Y 重名。
它们在原 (0,4) 上就是原 degree-six 空间的同一截面；
R=(x^3+2)sigma^6。

定义
$$
\mathcal H=L-\frac1{12}D_z^2-\frac{az^2}{4}.
\tag{MH6}
$$
其作用完整为
$$
\begin{array}{c|l}
U&\mathcal H U\\ \hline
S&-\frac52 F\\
F&-H-\frac{7a}{24}S\\
H&-\frac16 R+\frac b4S-\frac{5a}{12}F\\
J&\frac12G\\
G&\frac{5a}{24}J\\
R&-\frac{3b}{4}F-\frac{3a}{8}H+\frac{a^2}{6}S .
\end{array}
\tag{MH7}
$$

可统一核对所有行。若 q=q(x,y,a,b)，则
$$
\begin{aligned}
\sigma^{-6}\mathcal H(q\sigma^6)
={}&Lq-\frac1{12}D_z^2q-\eta D_zq-\frac52xq.
\end{aligned}
\tag{MH8}
$$
(MH8) 使用 L log sigma=(eta^2-x)/2+az^2/24，
且 D_z^2(q sigma^6)/sigma^6
=D_z^2q+12eta D_zq+(36eta^2-6x)q。
逐项代入 (MH4) 与 (MH5)，eta 项全消，恰得 (MH7)。
例如 q=x 的剩余项为 -x^2-7a/24，
q=-xy 的剩余项为 (5a/24)y；
q=x^3+b/2 必须保留 L(b/2)=a^2/6。

这不与固定曲线闭包笔记矛盾。事实上
$$
La=6b,\qquad (La)(0,4)=24\ne0\pmod p.
\tag{MH9}
$$
因此 a=0 的理想不被 L 保持；不能在先置 a=0 后继续把 L 当作原 D_z，或据 (MH7) 声称一个固定宽度的原 Taylor 递推。

## 3. 辅助原曲线与矩阵方向

在原模参数轨道 Delta=-432 上设
$$
X=a/3,\qquad Y=b.
$$
则
$$
Y^2=X^3+16,\qquad LX=2Y,\qquad LY=3X^2.
\tag{MH10}
$$
这是同一 E27 模型，微分为 dX/(2Y)。以下用
D=L|_{\Delta=-432} 表示这条辅助曲线的平移导数；
原 CM 点对应 P_0=(X,Y)=(0,4)。

令函数列 Phi=(J,G)^t，并设
$$
\mathcal O_z=\frac1{12}D_z^2+\frac{3Xz^2}{4},\qquad
M=\begin{pmatrix}0&1/2\\5X/8&0\end{pmatrix}.
\tag{MH11}
$$
(MH7) 的奇部分准确写成
$$
D\Phi=\mathcal O_z\Phi+M\Phi.
\tag{MH12}
$$
本文平凡化的是**值向量连接** D-M：
若 DU=MU 且 Phi=U Psi，则
(D-\mathcal O_z)Psi=0，限于未截断的特征零形式方程。

矩阵转置与负号不能省略。若把 (J,G) 看成行基，
其基作用矩阵是 M^t；水平**系数**连接是 D+M^t，
由 U^{-t} 平凡化。以下列向量 (u,2Du)^t 属于 D-M 的约定，
并未把它当成 D+M^t 的水平系数。

由 M 的两行可知，(u,2Du)^t 水平当且仅当
$$
D^2u=\frac5{16}Xu.
\tag{MH13}
$$

## 4. 显式可分覆盖与完整水平矩阵

令 r 为变量，置
$$
P=r^8+14r^4+1,\quad
Q=r^4(r^4-1)^4,\quad
T=r^{12}-33r^8-33r^4+1.
$$
两个准确多项式恒等式为
$$
P^3-108Q=T^2,\qquad
\frac d{dr}\left(\frac{P^3}{108Q}\right)
=\frac{P^2T}{27r^5(r^4-1)^5}.
\tag{MH14}
$$
取常数 alpha,beta 满足
$$
\alpha^3=-4/27,\qquad \beta^2=-4/27,
$$
并在覆盖
$$
v^6=r(r^4-1)
\tag{MH15}
$$
上定义
$$
X=\alpha P/v^8,\qquad Y=\beta T/v^{12}.
\tag{MH16}
$$
由 (MH14) 及 v^{24}=Q，立即有
$$
Y^2-X^3=16,\qquad
-\frac{X^3}{16}=\frac{P^3}{108Q}.
\tag{MH17}
$$
令
$$
c=\frac{3\beta}{2\alpha},\qquad D=c v^2\frac d{dr}.
\tag{MH18}
$$
常数满足 c^2=9alpha/4。对 (MH16) 求导给
DX=2Y、DY=3X^2，所以 (MH18) 正是 (MH10) 的延伸，
没有另选辅助微分。

这里给出水平解的直接验证，不依靠单值群名称。
由 v^6=r^5-r 得
$$
\frac{v''}{v}=-\frac{5P}{36v^{12}},
\tag{MH19}
$$
其中撇号仅指 d/dr。令
$$
u_1=v^{-1},\qquad u_2=rv^{-1}.
\tag{MH20}
$$
由 D(v^{-1})=-c v'，
$$
\frac{D^2u_1}{u_1}
=-c^2v^3v''
=\frac{5c^2P}{36v^8}
=\frac5{16}X.
$$
并且
$$
u_1Du_2-u_2Du_1
=u_1^2Dr=c.
\tag{MH21}
$$
由于 (MH13) 没有一阶项，(MH21) 与第一解等式给第二解等式；
亦可直接微分验证。因此
$$
U=\begin{pmatrix}
u_1&u_2\\2Du_1&2Du_2
\end{pmatrix},\qquad
DU=MU,\qquad \det U=2c\ne0.
\tag{MH22}
$$
在函数域中这就是完整的水平基。

为解释有限单值来源而非作为证明前提：
令 t=-X^3/16，(MH13) 化为
$$
t(1-t)u_{tt}+\left(\frac23-\frac76t\right)u_t
+\frac5{576}u=0,
$$
即参数 (-1/24,5/24;2/3) 的 Gauss 方程。
指数差为 (1/3,1/2,1/4)；(MH14) 正给八面体类型的显式覆盖。
本篇需要的代数恒等式已在 (MH14)--(MH22) 直接证明，
不从“有限单值”四字偷推出一个未经检查的整模型。

## 5. 所有允许 p 的零 p 曲率和原点单位

现取任意 p=6N+5>=41，在代数闭包 k 上约化上述式子。
所有显示常数只需除 2、3，alpha,beta,c 都是单位。

在 E27 上 D 是处处正则非零的平移向量场。
D^p 仍是正则导数，故 D^p=dD，d 属于 k。
曲线的三次 CM 自同构 (X,Y)->(zeta X,Y) 将 D 共轭成
zeta^{-1}D；于是将 D^p 共轭成 zeta^{-p}D^p。
由于 p≡2 mod 3，zeta^{-p}≠zeta^{-1}，迫 d=0：
$$
D^p=0\quad\hbox{在 }k(E27)\hbox{ 上}.
\tag{MH23}
$$

(MH14) 的有理映射次数为 24，(MH15) 的 Kummer 步数至多为 6。
因此由 (MH16) 所得函数域扩张有限，次数只有 2、3 因子；
在 p>=41 时可分。也可由 (MH14) 的非零导数直接核其可分性。
D 唯一延伸到每个连通函数域分量；延伸后的 D^p 是一个
在基域为零的导数。有限可分扩张没有非零的基域导数，故延伸后
D^p 仍为零。

(MH22) 将 D-M 化为普通 D，因此
$$
(D-M)^p=0,\qquad
\psi_{D-M}(D)=(D-M)^p-\nabla_{D^p}=0.
\tag{MH24}
$$
对偶连接 D+M^t 同样零 p 曲率。
这是模参数奇连接的结论，绝不是原 sigma^6 的 z 方向零 p 曲率。

在 P_0 上，P(r_0)=0。对 p>=41，P 没有重根：
P'=8r^3(r^4+7)，共同根将迫 48=0。
此外 r_0≠0、r_0^4≠1，故 v 与 v^{-1} 均为单位，
T(r_0)^2=-108Q(r_0) 也是单位。
(MH16) 给 X 对 r-r_0 的零阶为一，覆盖在归一化后的 P_0 上不分歧。
于是 u_1,u_2 都是单位，且 det U=2c 是单位。
特别 U^{-1}(0,1)^t 的两个分量
$$
(-u_2,u_1)^t/(2c)
\tag{MH25}
$$
也都是单位。这些是连接的单位，尚未识别为原 f_i 或 g_j。

## 6. 首 p Taylor 截断并非无源水平截断

这一节固定所有阶乘，给出进入原有限种子时不能省略的项。

记一般家族的普通导数
$$
j_n=D_z^nJ(0),\qquad g_n=D_z^nG(0),\qquad
s_n=D_z^n\sigma(0).
$$
原 sigma 是在 Z[1/6,a,b] 上的 Hurwitz 级数
（Bunkova 上述文献 Corollary 3.4；R697 的原普通导数规范与此一致）。
六个截面也如此。可由
$$
A=\sigma'^2-\sigma\sigma''=x\sigma^2,\qquad
G=\sigma A^2\sigma'-\frac12\sigma^2AA',
\quad
J=\frac12\sigma^4A'-\sigma^3A\sigma'
\tag{MH26}
$$
直接核奇部分：这些是 sigma 及普通导数的多项式。
在 Hurwitz 环中约化后，D_z^p 满足 Leibniz 公式。
由 sigma(0)=0、sigma'(0)=A(0)=1，(MH26) 给
$$
j_p=0,\qquad g_p=s_p\pmod p.
\tag{MH27}
$$

原 Hasse 多项式为
$$
\mathscr A_p(a,b)
=[x^{p-1}](x^3-ax/4-b/4)^{(p-1)/2}.
\tag{MH28}
$$
同一 sigma 的普通导数满足
$$
s_p=\mathscr A_p\pmod p.
\tag{MH29}
$$
这里可给不依赖数值的 q-expansion 核对。
Rodriguez Villegas 式 (2.16) 的 completed theta 第 p 个普通导数的
p-adic q-expansion，逐项由 (2m+1)^p≡2m+1 及 2^{p-1}≡1，
约化为第一个导数的 q-expansion，即 1。
从 completed theta 去掉二次指数时，每个非零二次指数项都带
p!/(r!(p-2r)!)（0<r< p/2），因而被 p 整除；
sigma 的低普通导数及该二次指数 q-expansion 均在 p 处整。
所以 s_p 的 q-expansion 也是 1。
s_p 与 (MH28) 同为权 p-1 的整模形式；Hasse 的 q-expansion 是 1，
固定权的 q-expansion 原理给 (MH29)。没有将原 c=0 sigma 改成另一个规范；
completed theta 仅用于证明这一整系数同余。

只在合法有限范围内定义
$$
\Phi_{<p}(z)=
\sum_{n=0}^{p-1}\binom{j_n}{g_n}\frac{z^n}{n!}
\quad\hbox{于 }k(E27)[z]/(z^p).
\tag{MH30}
$$
两个函数都为奇函数。对 (MH12) 逐个普通导数取值，
再截断并保留 n=p-2 的遗漏项，
由 (p-2)!≡1 得
$$
\boxed{
(D-\mathcal O_z-M)\Phi_{<p}
=\frac{\mathscr A_p}{12}z^{p-2}\binom01
\quad\bmod z^p.
}
\tag{MH31}
$$
唯一遗漏的非零高普通导数是 (j_p,g_p)^t=(0,A_p)^t；
n=p-1 为偶数，相关向量严格为零。
(MH31) 因而没有用到任何未经许可的完整普通 Taylor 模 p 级数。

令 Psi_{<p}=U^{-1}Phi_{<p}，则
$$
\boxed{
(D-\mathcal O_z)\Psi_{<p}
=\frac{\mathscr A_p}{12}z^{p-2}U^{-1}\binom01.
}
\tag{MH32}
$$
零 p 曲率的有限奇连接已准确消去，Hasse 边界源仍保留。

## 7. 原 Cartier 常数只在横向导数进入

保留原
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\ne0.
$$
由 (MH28) 的单项抽取，
$$
\mathscr A_p(0,4)=0,\qquad
(\partial_a\mathscr A_p)(0,4)
=\frac{N+1}{4}B=\frac B{24},
$$
所以
$$
(D\mathscr A_p)(P_0)=B.
\tag{MH33}
$$
第一式由 x^3-1 的幂只含三的倍数次数；
第二式选择一个 -ax/4、2N+1 个 x^3 和 N 个 -b/4 即得，
并使用 N+1≡1/6 mod p。

因此 (MH32) 的右侧在 P_0 本身为零，但其第一次辅助 D 导数为
$$
\frac B{12}z^{p-2}U(P_0)^{-1}\binom01.
\tag{MH34}
$$
(MH25) 证明此源向量的两个分量为单位。
这仍是同一个 B，不能作为一个新算术单位重新计数。

## 8. 尚缺的真实桥

(MH7) 与 (MH22)--(MH34) 给出了真实家族、固定微分、矩阵方向、
可分平凡化及合法首 p 边界源。
它独立于“继续同一个固定曲线 Hurwitz 核的高块”，
但尚未证明它迫使
$$
f_i g_{N-1-i}\ne0
$$
对某个 i 成立，更未证明
$$
\mathbf1_{(6i+7,p+1)=1}
 P_{6i+6}(1/\sqrt{-3})f_i g_{N-1-i}\ne0.
$$
上述 f_i,g_j 始终是原 (a,b)=(0,4) 的 F、G 的系数。

具体缺口是：有限奇连接的单位矩阵 U 与 (MH34) 的横向源，
必须经原 oscillator heat 方程转成**固定原曲线**上所需的临界支撑信息。
仅把 U^{-1} 乘到函数列、把 a=0 当作 D 稳定切片，
或者删去 (MH31) 的 Hasse 边界源，都不能完成这一步。
原 Legendre 权和 primitive 标签也尚未随此变换运输。

本篇不声称未筛全零已经排除，不声称同本原三单位已找到，
不改变主课题的真实高度与全 p 完成标准。

## 原文与已有依赖

- Bunkova, *Weierstrass sigma function coefficients divisibility hypothesis*,
  arXiv:1701.00848v2, 式 (1)、Corollary 3.4：
  https://arxiv.org/pdf/1701.00848
- Rodriguez Villegas, *On the Taylor coefficients of theta functions of CM elliptic curves*,
  1993-11-24, 式 (2.8)、(2.9)、(2.16)：
  https://frvillegas.github.io/pdf/frv-cm-theta.pdf
- R697：原 degree-six theta 空间、c=0 Gaussian 与普通导数。
- R770：真正同标签 f/g、primitive 和 Legendre 目标。
- R765：原 Cartier 单位 B 和首个非整普通系数。
- notes/2026-11-15-sigma-stable-space-research.md：
  固定原曲线 D_z 闭包，不能与本篇 L 闭合混用。
- notes/2026-11-15-sigma-Hurwitz-block-rigidity.md：
  原固定曲线高块刚性；本篇首 p 截断的边界项不能据此删除。

