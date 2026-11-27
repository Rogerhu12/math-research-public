# R1039 — 原 g 二盖的固定椭圆 Prym、非挠无穷边界和原两覆盖的双 Norm

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 本篇始终使用 R1031 的同一个原二 Selmer 类 g，
不另换曲线来源。给出其二盖的真实 elliptic Prym、一个固定非挠边界类，
以及任意原两覆盖点在该 Prym 曲线上诱导的准确 Norm 函数。
此外识别 R1031 的规范 Frobenius 束在原开集上的有限带符号置换表示。
这些是新的实际几何输入；尚未把该椭圆边界与原54图最高循环、
27对加权交或普通 p 的局部 AJ 等同。

## 1. 原二盖和两个真实商

特征零先在 $F=\mathbf Q(a)$ 上工作，$a^3=4$；
在惰性好素数 q 的约化中，a 取 $\mathbf F_q$ 中唯一的该立方根。
始终取光滑射影正规化：
$$
 C:\ w^2=(z^3-4)(z^3-16),\qquad
 g=z^2+az+a^2,
$$
$$
 \widetilde C:\quad s^2=g,\qquad
 w^2=(z^3-4)(z^3-16).
\tag{1}
$$
R1031 已证明 g 的半除子是非零二挠类
$L=[P_1-P_2]$，所以
$$
 \pi:\widetilde C\longrightarrow C
\tag{2}
$$
是连通 étale 二盖，$g(\widetilde C)=3$。
原两个同调 involution 写为
$$
 \iota(s,w)=(-s,w),\qquad \jmath(s,w)=(s,-w).
\tag{3}
$$
它们分别是 π 的 deck 和 w 符号的变换，必须区别。
$\jmath$ 的商为圆锥 $s^2=g(z)$；它有两个有理无穷点，
故为 $\mathbf P^1_F$。因此 $\jmath$ 在
$J_{\widetilde C}$ 上准确作用为 $[-1]$。

置
$$
 W_L=w/s.
$$
第三个 involution $\kappa=\iota\jmath$ 的商是
$$
 E_L^{(4)}:\quad W_L^2=(z-a)(z^3-16).
\tag{4}
$$
这是因为 $z^3-4=(z-a)g$。
该商不是只用 j 不变量辨认。其原点取 z=a 的分歧点，
具体变换为
$$
 \boxed{
 x_L=\frac{z-4a}{z-a},\qquad
 y_L=-\frac{3W_L}{(z-a)^2}.
 }
\tag{5}
$$
令 z=at；则
$$
 x_L^3-12x_L+20
 =\frac{9(t^3-4)}{(t-1)^3},
\qquad
 \frac{9W_L^2}{(z-a)^4}
 =\frac{9(t^3-4)}{(t-1)^3},
$$
所以(5)准确给固定有理模型
$$
 \boxed{E_L:\ y_L^2=x_L^3-12x_L+20.}
\tag{6}
$$
反向为
$$
 z=a\frac{x_L-4}{x_L-1},\qquad
 W_L=-\frac{y_L(z-a)^2}{3}.
\tag{7}
$$
在这些式子的分母处，按光滑射影曲线作唯一延拓。
记实际二度映射
$$
 r:\widetilde C\longrightarrow E_L.
\tag{8}
$$
r 有分歧：g 在(4)的 z=a_1、a_2 上各有两个简单零点，
共四个分歧点。它在 z=a 的两个原像处不分歧。
(6)的判别式为 $-2^8 3^5$，故所有 q≥5 都是这个固定模型的好素数。
a 只出现在显示的映射中；(6)没有遗漏随 q 变化的二次扭曲。

## 2. Prym 是 E_L，而不仅是有理同源因子

对有限二盖的图对应，准确有
$$
 \pi^*\pi_*=[1]+\iota,\qquad
 r^*r_*=[1]+\kappa.
$$
由 $\jmath=[-1]$，
$$
 \boxed{
 r^*r_*=[1]-\iota,\quad
 \pi^*\pi_*+r^*r_*=[2].
 }
\tag{9}
$$
这里是在 Jacobian 的同态中成立，因而同时是相应曲线图在
度零除子上的关系，不仅是在微分或一个 ℓ 实现上的关系。
并且
$$
 \pi_*r^*=0,\qquad r_*r^*=[2].
\tag{10}
$$
第一式可由 $\iota$ 对 r 的商作用为(6)的负映射得到：
$\pi_*\iota=\pi_*$、$\iota r^*=-r^*$，而 abelian variety
之间的 Hom 群无二挠。

r 分歧，所以 $r^*:E_L\to J_{\widetilde C}$ 没有非零核。
完整证明：若度零线丛 M 被 r 拉成平凡，Norm 给 $M^2=1$。
若 M 为非零二挠，其所定义的 étale 二盖
$E_M\to E_L$ 会因拉回平凡而使 r 通过 $E_M$ 分解。
两映射度数均为2，故中间映射度数1，迫 r 自身 étale，
与§1的四个分歧点矛盾。特征不为2，亦无遗漏的非约化核。

因此 r 的像是连通的一维 $\ker\pi_*$，并且
$$
 \boxed{
 r^*:E_L\xrightarrow{\sim}
 \operatorname{Prym}(\widetilde C/C)
 =(\ker\pi_*)^0.
 }
\tag{11}
$$
这给严格群同构，不必以一般 Prym 分类或一个尚未构造的 Chow 逆为输入。

## 3. 原无穷边界给固定非挠点

在 $\widetilde C$ 上取有理无穷点
$$
 P_\infty:\quad w/z^3\to1,\quad s/z\to1.
$$
其 π-conjugate 为 $\iota P_\infty$。由(5)，
$$
 r(P_\infty)=(1,-3),\qquad
 r(\iota P_\infty)=(1,3).
\tag{12}
$$
在 $F(\sqrt3)$ 上另取
$$
 P_0:\quad z=a,\ w=0,\ s=a\sqrt3.
$$
则 $r(P_0)=r(\iota P_0)=O$。
$\jmath$ 固定这两个点，所以它们是同一双有理商的分歧点；
该商为 $\mathbf P^1$，给
$$
 D_0=[P_0-\iota P_0],\qquad 2D_0=0.
\tag{13}
$$
两点不同且亏格正，$D_0\ne0$。
改变 $\sqrt3$ 把 $D_0$ 变为 $-D_0=D_0$，因此这个二挠
Jacobian 类在 F 上下降。$\widetilde C$ 有有理点 $P_\infty$，
可用该点 rigidify 度零线丛，故此处没有遗漏的 Picard 下降障碍。
同样论证在每个上述有限域中有效，即使 $\sqrt3\notin\mathbf F_q$。

令 $D_\infty=[P_\infty-\iota P_\infty]$。
对 $[P_\infty-P_0]$ 应用(9)，得到准确关系
$$
 \boxed{
 D_\infty-D_0
 =(1-\iota)[P_\infty-P_0]
 =r^*[(1,-3)-O].
 }
\tag{14}
$$
特别(14)位于真正的连通 Prym 中；无需把
$D_\infty$ 单独所在的连通分支默认为单位分支。

固定点 $P=(1,3)\in E_L(\mathbf Q)$ 非挠，可在原有理模型上
完全初等证明。群律给
$$
 2P=(1/4,-33/8).
\tag{15}
$$
对 $E_L:y^2=x^3-12x+20$，倍点公式为
$$
 x(2Q)=
 \frac{x(Q)^4+24x(Q)^2-160x(Q)+144}
 {4(x(Q)^3-12x(Q)+20)}.
\tag{16}
$$
若 $v_2(x(Q))=-2m$、$m\ge1$，分子四项的赋值分别为
$$
 -8m,\quad 3-4m,\quad 5-2m,\quad4,
$$
首项为唯一最小；分母括号中首项也为唯一最小，故
$$
 v_2(x(2Q))=-2m-2.
\tag{17}
$$
由(15)归纳，$2^nP$ 的 x 坐标有无界的2进分母，
且每次倍点均为有限非零点。因此 P 不可能是有限阶点。
由(11)、(14)，原 g 二盖的边界类 $D_\infty-D_0$ 也非挠。

这是原已固定谱覆盖上的具体非挠类；它没有声称
原 $\lambda$ 最高 Abel–Jacobi 扩张是一个 1-motive。

## 4. 任意原两覆盖点给 E_L 上的准确 Norm 函数

现取特征 q≥5，保持原常数域方向 $\delta^2=-3$。
设 R 是原 R1031(19) 的实际 $s_0=1$ 点，并保持
$$
 -3(x-\beta)=g\left(\frac R{z-2X}\right)^2,
\quad
 \beta=-u^2,\quad
 u=\frac{1-w/(z^3-4)}6.
\tag{18}
$$
这里用 $s_0$ 区别两二次式的射影坐标与(1)的平方根 s。
定义原二盖上的函数
$$
 \boxed{
 F_Q=\frac{sR}{z-2X}+\delta u.
 }
\tag{19}
$$
$\iota$ 取 s 的负号而固定原 C 上的一切。
用(18)可逐项得到
$$
 \boxed{
 \operatorname{Nm}_{\widetilde C/C}(F_Q)=3x.
 }
\tag{20}
$$
确实乘积是
$-gR^2/(z-2X)^2-3u^2=3(x+u^2)-3u^2$。
这个常数是 $+3$，不是 $-3$。

将原谱函数 R 用(1)的二次域表示为
$$
 R=A(z)+B(z)w,\quad A,B\in\mathbf F_q(z),
$$
并记
$$
 K=z^3-4,\qquad D=z-2X.
$$
在 $r$ 的域上，$w=sW_L$、$s^2=g$，所以
$$
 F_Q=
 \left(\frac\delta6+\frac{g B W_L}{D}\right)
 +s\left(\frac A D-\frac{\delta W_L}{6K}\right).
\tag{21}
$$
$\kappa$ 固定 $z,W_L$ 而取 s 的负号。因此另一个真实 Norm 为
$$
 \boxed{
 \begin{aligned}
 N_Q
 &=\operatorname{Nm}_{\widetilde C/E_L}(F_Q)\\
 &=-\frac1K-\frac{g\bigl(A^2-K(z^3-16)B^2\bigr)}{D^2}
   +\frac{\delta g W_L}{3D}\left(B+\frac A K\right).
 \end{aligned}
 }
\tag{22}
$$
证明直接将(21)的两项平方相减；
利用 $gW_L^2=K(z^3-16)$，
常数中的 $-1/12+(z^3-16)/(12K)$ 恰为 $-1/K$。
这一步保住原 $\delta$ 和 B 的符号，不能用另一个任意二次扭曲替换。

四阶群 $\langle\iota,\jmath\rangle$ 的 Norm 传递律给
$$
 \boxed{
 N_Q(z,W_L)N_Q(z,-W_L)
 =9\,\operatorname{Nm}_{C/\mathbf P^1_z}(x).
 }
\tag{23}
$$
因此(22)是在固定 E_L 上的实际有理函数，其全部零极除子
满足(23)的原重数关系。对两商取图、闭包及正规化后，
(20)–(23)仍是完整除子恒等式；没有只核有限点集。
R1036 的实际 q=11 点及其已执行的原(19)平方根可直接代入，
无需再枚举任何极除子或重跑该点的存在计算。
若将 R 取负，则 $F_Q$ 变成 $\iota F_Q$，因而 $N_Q$ 变成
$[-1]^*N_Q=N_Q(z,-W_L)$。所以已执行平方根中为匹配原 W
作的整体符号选择在这里也必须保留，不能在 Prym 上悄悄再交换两支。

## 5. 规范 Frobenius 束的真正有限覆盖

这一段说明 R1031 的 j 所描述的对象，避免把稳定束同构
误当最高 CM 动机的比较。原三次谱盖的 Galois 闭包 D/B 是 S3 盖；
其判别式平方类为
$$
 -3/X,
$$
在 T、−T 的赋值为奇数，故它在几何上也非循环。
把 g 的三个共轭记为 $g_1,g_2,g_3$。
它们的乘积为 $(3a/X)^2$，可选平方根满足
$$
 \sqrt{g_1}\sqrt{g_2}\sqrt{g_3}=3a/X.
\tag{24}
$$
在 D 上再加这三个平方根。

所得二次核是三符号乘积为1的群的 S3-稳定子群。
该二维 $\mathbf F_2$ 模在 S3 下不可约，故核只能是0或 V4。
核不为0：否则 g 在 $D=K_C(\sqrt d)$ 中为平方，
其中 d 为基域中的非平方判别式。平方在二次扩张中分裂的初等判据给
g 在 $K_C$ 中或者为平方、或者等于 d 乘平方。
前者与 L 非零矛盾；后者对 $K_C/k$ 取 Norm，
又与 Norm(g) 为平方、d 非平方及次数3矛盾。
所以完整群准确为
$$
 \boxed{V_4\rtimes S_3\simeq S_4.}
\tag{25}
$$
原 étale 二盖不增加两个谱分歧点上的 ramification；
相应惯性为 transposition。因此此正规盖仅在 T、−T
各有阶2惯性，Riemann–Hurwitz 给其亏格13。
这是真正的原 g 正规覆盖，不是 R1029 的六度全二谱盖本身。

在原 étale 开集上，rank3 的表示为
$$
 \rho=\operatorname{Ind}_{K_C/k}(\text{原二盖的 sign 字符}).
\tag{26}
$$
在上述盖上，用 $1/\sqrt{g_i}$ 作有序基，
R1031 的映射
$$
 j(F^*R)=g^{(q-1)/2}R^q
$$
变成坐标的 q 次幂；Galois 作用恰为三个基的置换和
乘积为1的符号改变。这是(25)的标准三维带符号置换表示，
不是从纯 CM 的 $H^1(C)$ 免费得到的某个高权实现。

更具体，取 $\ell\ne2,3,q$，令 $\mathcal V_\ell$ 为(26)的
有限 ℓ-adic 局部系，令 $j_U:U\hookrightarrow B$ 是该原 étale 开集的嵌入，
并在 B 上取中间延拓。有限推前及
π 的正负分解给
$$
 \begin{aligned}
 H^1(B_{\overline{\mathbf F}_q},j_{U*}\mathcal V_\ell)
 &\simeq
 H^1(\widetilde C_{\overline{\mathbf F}_q},\mathbf Q_\ell)^-\\
 &\simeq H^1(E_{L,\overline{\mathbf F}_q},\mathbf Q_\ell).
 \end{aligned}
\tag{27}
$$
第二个同构由实际的(9)–(11)给出；
第一式在谱分歧处使用有限推前的整个 stalk，
没有删去两个坏点的惯性信息。
同构与所述有限域上的 Frobenius 交换。
所以这个有限谱局部系的 parabolic 第一上同调，
真正由固定 E_L 的 Frobenius 控制；不能以
$J_C$ 的 CM 平方关系代替它。

## 6. 对主问题的准确用途和未付部分

(11)、(14)给一个已构造的原谱 Prym 和固定非挠边界；
(22)把任意已得原截面送进该同一椭圆曲线上的明确函数，
(27)标明规范 j 所需的实际 Frobenius 来源。
这些公式允许继续求真实 R 的极零关系及其一般 q 结构。

它们目前没有给出原27对的有权交值，也没有构造从这个
Prym 边界到原 $\eta_j^{-1}\widehat\psi^3\varepsilon^{-1}$
最高表示的混合对应。特别不能把(14)的椭圆非挠性直接替代
那个 Hodge 类型为 $(2,-1)$ 的原局部 AJ 非零。
q=11 原完整 shadow 仍被12杀掉，原倒6系数下仍为零。
后继必须沿(18)–(23)及原54图、真实 Cor 和最高投影继续，
而不是据一个新的 1-motive 点就宣称跨 p 完成。

## 内部依据

- R1029：同一个 C/B、原二挠谱域及其 S3 闭包。
- R1031 §§1–4：同一个 g、完整 Norm 类和两二次式。
- R1036：实际 q=11 唯一截面、完整格及真实极除子。
- [原两覆盖返回及实际回执](../notes/2026-11-27-original-q11-two-cover-lift-and-frobenius-line.md)：
  q=11 的精确平方根、原两式、Norm 符号与全部厚点返回。
