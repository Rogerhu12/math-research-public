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

## 7. 固定原 Prym 的无穷惰性超奇异素数

这一节给(6)的固定曲线一个新的无穷输入。它不从 Elkies 定理
“在任意实数域上有无穷超奇异素点”直接推剩余域次数1。
我们对一个真正的三同源商的 j 域重新使用其负 Norm 证明，
并支付两辅助素数的 Frobenius 以及最后的剩余次数奇偶性。

**命题。** 对任意有限有理素数集 S，都有
$$
 q\notin S,\qquad q\ge5,\qquad q\equiv-1\pmod3,
 \qquad a_q(E_L)=0.
\tag{28}
$$
因此这样的 q 无穷多。这里始终是(6)的准确有理模型，
不是 R1031 的另一非 CM 椭圆商，也没有换一个随 q 变化的扭曲。

### 7.1 一个真实的实三同源商及其 j 域

先付出这个曲线非 CM，避免把不同核的商 j 混同。
在5、7处原方程均好约化。在 x 依次取标准剩余元时，
$x^3-12x+20$ 的值分别为
$$
 \begin{array}{c|c|c|c}
 q&\text{全部多项式值}&\#E_L(\mathbf F_q)&a_q\\ \hline
 5&(0,4,4,1,1)&10&-4\\
 7&(6,2,4,4,1,1,3)&11&-3.
 \end{array}
\tag{29}
$$
表中的计数由每个非零平方给两点、零给一点，再加 O 得出。
两处均 ordinary；Frobenius 二次域分别为
$\mathbf Q(\sqrt{16-20})=\mathbf Q(i)$ 和
$\mathbf Q(\sqrt{9-28})=\mathbf Q(\sqrt{-19})$。
若 $E_L$ 有 CM，其二次端同态域在每个好 ordinary 约化中
都注入该约化的二次端同态域，因而必须等于这两个不同的域，
矛盾。这仅是固定曲线的非 CM 判定，不用两个有限素数代替(28)。

令 $C_3\subset E_L[3]$ 是一个复共轭稳定的循环三核。
它可直接在原实模型上选定：三除多项式除以3为
$$
 h_3(T)=T^4-24T^2+80T-48.
\tag{30}
$$
$h_3(0)<0<h_3(1)$，故有实根 $r\in(0,1)$。
此时 $r^3-12r+20>0$，点
$(r,\sqrt{r^3-12r+20})$ 为非零实三挠点，
它与负点组成所需核。取真实商
$$
 E'=E_L/C_3,\qquad j'=j(E'),\qquad F=\mathbf Q(j').
\tag{31}
$$
有 $j'\in\mathbf R$，故 F 有实嵌入。

四个循环三核给四个不同的商 j。完整理由是：
若两个商同构，则将同构与两个三同源复合，得到
$E_L$ 的度9端同态；因非 CM，它是 $\pm[3]$。
再与另一同源复合并在 Hom 群中消去[3]，
得两个同源相差符号，其核相同，矛盾。
因此
$$
 \operatorname{Stab}(j')=\operatorname{Stab}(C_3)
\tag{32}
$$
作为绝对 Galois 群的子群严格相等。
特别 F 位于 $\mathbf Q(E_L[3])$ 中，
且 F 的嵌入与 $C_3$ 的 Galois 轨道一一对应。
这一步使用真正的商 j，若只将原有理 j 扩域，便没有(32)。

原 $j(E_L)=-3072$ 为整数。模多项式
$\Phi_3(-3072,T)$ 首一且整系数，所以 j' 为代数整数。
j' 非 CM，亦不等于1728。以下没有范数分母问题。

将 S 扩大一次，纳入2、3、5、7、F 的分歧素数、
$E'$ 的全部坏素点下的有理素数，以及四个商 j 的
最小多项式判别式、指数和两两碰撞所需的有限坏素数。
所有扩大的对象均固定，不依赖后面选的辅助素数。
证明对扩大的 S 成立即满足原 S。

### 7.2 Elkies 所需负 Norm 的具体实区间

记 $P_D(T)$ 为判别式 $-D$ 的整环类多项式。
使用 Elkies 1989 原文 §2 Proposition 1 及其 Corollary、
§3 Proposition 2 及其 Corollary 中的以下精确事实。

若不同素数 $\ell_1\equiv1\pmod4$、
$\ell_3\equiv3\pmod4$，置 $L=\ell_1\ell_3$，
则 $P_L$ 与 $P_{4L}$ 都在模 $\ell_1$、模 $\ell_3$
下是首一多项式的平方。对
$$
 f_-(t)=j((1+it)/2),\qquad f_+(t)=j(it)\quad(t>0),
$$
二者均满足 $f_\pm(t)=f_\pm(1/t)$；
在 $t>1$ 上，$f_-$ 从1728严格降到 $-\infty$，
$f_+$ 从1728严格升到 $+\infty$。
$P_L$ 的两个实根为
$f_-(\sqrt L),f_-(\sqrt{\ell_1/\ell_3})$，
$P_{4L}$ 的两个实根为相应的 $f_+$ 值。
其余根成非实共轭对。

现在把 j' 的所有不同实共轭排列为
$r_1<\cdots<r_k$，其中 $k\ge1$。
这涵盖 F 可能有两个实嵌入和一对复嵌入的情形，
不把 F 默认为全实域。

若 $r_1<1728$，选 z 严格位于
$r_1$ 与 $\min(r_2,1728)$ 之间；当 $k=1$ 时右端取1728。
取 $t_0>1$ 使 $f_-(t_0)=z$。
由连续性，可选固定开区间 $I\ni t_0^2$，
使 $\ell_1/\ell_3\in I$ 时第二实根仍在同一区间内。
当两辅助素数充分大时，第一实根小于 $r_1$。
故 $P_L$ 仅在 $r_1$ 处取负，在其余实共轭处取正。

若 $r_1>1728$，选 z 严格位于
$\max(r_{k-1},1728)$ 与 $r_k$ 之间；$k=1$ 时左端取1728。
改用 $f_+$ 及 $D=4L$，得到 $P_D$ 仅在 $r_k$ 处取负。
j' 非 CM 保证 $r_i\ne1728$，所以两种情形已经穷尽。
每个非实共轭对贡献 $|P_D(\sigma j')|^2>0$。
因此存在一个固定开区间 I 和固定的两种选择之一
$D=L$ 或 $D=4L$，使
$$
 \ell_1/\ell_3\in I,\quad \ell_i\text{ 充分大}
 \quad\Longrightarrow\quad
 A_D=\operatorname{Nm}_{F/\mathbf Q}P_D(j')<0.
\tag{33}
$$
$A_D$ 是非零整数。

### 7.3 两个辅助 Frobenius 同时满足所有排除条件

置有限 Galois 扩张
$$
 \mathcal M=
 \mathbf Q\bigl(E_L[3],\,i,\,\sqrt{s}\ (s\in S)\bigr),
\tag{34}
$$
并用选定复嵌入的复共轭 c 作其 Galois 元素。
因为每个 s 是正有理素数，c 固定所有 $\sqrt s$；
在 i 上它为负；在 $E_L[3]$ 上，
$c^2=1$ 且由 Weil pairing 有 $\det(c)=-1$。
在特征3中其两个特征值遂准确为1、−1。

Chebotarev 素数定理对共轭类 $\{1\}$ 和 $[c]$
分别给正密度素数集。对任意固定 $0<a<b$，
这两个集在 $[aT,bT]$ 中的素数数目分别渐近于
正正常数乘 $(b-a)T/\log T$。
因此可令
$$
 \operatorname{Frob}_{\ell_1}=1,\qquad
 \operatorname{Frob}_{\ell_3}\in[c],\qquad
 \ell_1/\ell_3\in I
\tag{35}
$$
并令两素数任意大、避开 S 及 $\mathcal M$ 的分歧集。
这里只使用无条件的 Chebotarev 素数定理，不需要 GRH。

逐项看(35)的后果：
$$
 \begin{array}{c|cc}
 &\ell_1&\ell_3\\ \hline
 \bmod4&1&-1\\
 \bmod3&1&-1\\
 (s/\ell_i),\ s\in S&1&1.
 \end{array}
\tag{36}
$$
最后一行来自它们都固定正平方根，
不是事后另附一组可能不兼容的同余条件。
因此(35)已同时支付 Elkies 的比值区间、两个模4条件
和原全部 S 条件。定义二次字符
$$
 \chi(n)=(n/\ell_1)(n/\ell_3).
\tag{37}
$$
则 $\chi(-1)=-1$、$\chi(s)=1$ 对所有 $s\in S$ 成立；
$\chi$ 是 $\mathbf Q(\sqrt{-L})$ 的二次字符，
也控制 $D=4L$ 的同一二次域。

还有两个关键数学分支。
在 $\ell_1$，$E_L[3]$ 的 Frobenius 为恒等，
故 $a_{\ell_1}(E_L)\equiv2\pmod3$。
$\ell_1\ge5$，若超奇异则迹应为0，因此它 ordinary。
若 $\ell_3$ 超奇异，(36)立即给所需的新 q=$\ell_3$，
命题已证。以下只需处理 $\ell_3$ 也 ordinary 的分支。

在此分支，
$$
 \ell_1\ell_3\nmid A_D,\quad\text{且实际上 }\gcd(A_D,L)=1.
\tag{38}
$$
这里必须逐素点解释：若 $\ell_i\mid A_D$，
因 j' 整且 $\ell_i$ 不在坏集，有 F 的素点 v 满足
$P_D(j')\equiv0\pmod v$。
该根是某个判别式为 $-D$ 的 CM 椭圆曲线的好约化 j。
$\ell_i$ 在 $\mathbf Q(\sqrt{-L})$ 中分歧；
它不整除该 CM 环可能的导子2。
由 Deuring 约化判据，该根为超奇异 j。
于是 $E'$ 在 v 超奇异，而真实三同源将此传给 $E_L$
在 $\ell_i$ 的约化，与该分支的 ordinary 性矛盾。
所以这里没有把 ramified CM 相交误认为自动存在。

### 7.4 负 Norm 的奇数估值迫 q 在原 K 中惰性

由模 $\ell_i$ 的多项式平方和范数乘法，
$A_D$ 在两个模数下都是非零平方。
令 $N=-A_D>0$。由(33)、(37)、(38)，
$$
 \chi(N)=-1.
\tag{39}
$$
故存在有理素数 q，满足
$$
 v_q(N)\text{ 为奇数},\qquad \chi(q)=-1.
\tag{40}
$$
它不等于 $\ell_1,\ell_3$，且由 $\chi(s)=1$
可知 $q\notin S$。

整数范数的准确赋值公式为
$$
 v_q(N)=
 \sum_{v\mid q} f(v/q)\,
             v\bigl(P_D(j')\bigr).
\tag{41}
$$
每项非负。存在 v 上的正赋值，即 j' 模 v 是 $P_D$ 的根。
$\chi(q)=-1$ 说明 q 在相应 CM 二次域中惰性，
Deuring 判据再次给 $E'$ 模 v 超奇异。
由 q 处的真实三同源，$E_L/\mathbf F_q$ 也超奇异。
因 $q\ge5$，
$$
 a_q(E_L)=0,\qquad
 \operatorname{Frob}_q^2=-q\quad\text{在 }E_L[3]\text{ 上}.
\tag{42}
$$

假设 $q\equiv1\pmod3$。
$E_L[3]$ 上的特征多项式于是为
$T^2+1\in\mathbf F_3[T]$，它不可约。
其在四个循环三核上的作用没有不动点；
又由(42)知其射影平方为恒等，故循环型准确为
$$
 (2,2).
\tag{43}
$$
任何 Galois 不变的核轨道在这个元素下都由二循环组成。
由(32)，这就是 q 在 F 的嵌入集合上的作用。
q 已避开分歧及指数坏集，所以所有 $f(v/q)$ 都等于2。
于是(41)为偶数，与(40)矛盾。
只能有 $q\equiv-1\pmod3$，命题得证。

注意这不是将一个 F 上的任意超奇异素点宣称为次数1；
实际证明使用了特定非零范数的奇数估值，
以及同一个商 j 域中的完整四核 Frobenius 周期。
有限集 S 任意，故确得无穷多个不同的 q。

## 8. 同一个原 g 二盖的无穷精确最大 Frobenius 输入

对§7所得的 q，a 在 $\mathbf F_q$ 中是4的唯一立方根，
所以§1–5的原全部映射、g、两个 involution 及 Prym 识别
都在 $\mathbf F_q$ 上保持原规范。
记 $\mathrm F_q$ 为曲线的 q 次 Frobenius 同态。
$E_L$ 超奇异且迹0，故不是只有特征多项式相等，而是真同态等式
$$
 \mathrm F_q^2=[-q]\quad\text{在 }E_L.
\tag{44}
$$
这由 Cayley–Hamilton 在任一好 ℓ-adic Tate 模上成立，
以及 abelian variety 的同态到其 Tate 模的单射得到。

R1029 已对每个惰性 q≥5证明原 $J_C$ 的同一个等式。
π、r 定义于 $\mathbf F_q$，所以与 Frobenius 交换。
将(9)的
$[2]=\pi^*\pi_*+r^*r_*$
与 $u=\mathrm F_q^2+[q]$ 复合，两个右端项均为0。
故 $[2]u=0$。Jacobian 的 Hom 群无挠，得到
$$
 \boxed{\ \mathrm F_q^2=[-q]\quad\text{在 }J_{\widetilde C}.\ }
\tag{45}
$$
因而对上述无穷 q，
整个原 g 二盖在 $\mathbf F_{q^2}$ 上的六个第一上同调
Frobenius 根都为 −q；这不是仅 C 的纯 CM 因子，
也不需要假设 R1031 的另一非 CM 商与 $E_L$ 同时超奇异。

固定有理非挠点 $P=(1,3)$ 在这些有限域中满足
$$
 [q+1]\overline P=0,
\qquad
 [q+1](D_\infty-D_0)=0
 \quad\text{在 }J_{\widetilde C}(\mathbf F_q).
\tag{46}
$$
第一式用 $\mathrm F_q\overline P=\overline P$ 代入(44)，
第二式用真实的(14)。有理非挠性与有限域中的(46)并不冲突。

(45)还给可直接在函数域中使用的完整除子关系。
取原有理基点 $P_\infty$。
对任意几何点 Z，Abel 映射与 Frobenius 交换，所以
$$
 qZ+\mathrm F_q^2(Z)\sim(q+1)P_\infty
 \quad\text{在 }\widetilde C_{\overline{\mathbf F}_q}.
\tag{47}
$$
两个点相合时保留原重数；
不是只在点集上给一个相消关系。
若 Z 在 $\mathbf F_{q^2}$ 上，则
$(q+1)(Z-P_\infty)$ 为主除子。
若其除子在某个有限域上有定义，且需要函数也在同域上，
可用 $P_\infty$ 的 rigidification 和有限域 Hilbert 90
下降其一维函数空间，未引入额外平方根或改动原 g。

这些是(18)–(23)的原平方根盖所需的实际无限 Frobenius 输入。
本节没有证明 q+1 的素因子包含无穷多个不同素数，
没有替换原54图、27对的有权和，
也没有把(46)的椭圆 Kummer 类等同原
$\eta_j^{-1}\widehat\psi^3\varepsilon^{-1}$ 最高实现。
后继仍须用原 R、两二次式及双 Norm 作真正的对应；
特别不能由新的无限辅助 q 自动宣布普通 p 或主课题完成。

### §§7–8 的原始文献依据

- N. D. Elkies, *Supersingular primes for elliptic curves over real number fields*,
  Compositio Math. 72 (1989), 165–172：
  [原文](https://www.numdam.org/item/CM_1989__72_2_165_0.pdf)。
  实际调用其已发表的 §2 Proposition 1 / Corollary 与
  §3 Proposition 2 / Corollary；§7重新给出所需加强的全部范数论证，
  不把该文主定理中的任意剩余次数偷换为1。
- J.-P. Serre, *Quelques applications du théorème de densité de Chebotarev*,
  Publ. Math. IHÉS 54 (1981), 123–201：
  [原文](https://www.numdam.org/item/PMIHES_1981__54__123_0.pdf)。
  §7.3仅需固定有限 Galois 扩张的无条件 Chebotarev 素数定理，
  无需任何有效常数或 GRH。

## 9. 同一固定 Prym 的无穷 q≡−1 mod24 输入

本节强化§7的实际输入，得到
$$
 \boxed{\text{任给有限素数集 }S,\quad
 \exists q\notin S:\quad q\equiv-1\pmod{24},\
 a_q(E_L)=0.}
 \tag{48}
$$
它仍使用同一个固定 $E_L:y^2=x^3-12x+20$，
不假设同时超奇异性，也不从任意次数的素点推有理素数结论。

### 9.1 真正实循环24商的 j 域

固定一个本原实周期 $\Omega_{\mathbb R}$。
复解析参数 $\Omega_{\mathbb R}/24$ 给一个真阶24的实代数挠点；
其代数性来自 $E_L[24]$ 是有限代数群。
因此存在复共轭稳定的自由循环核
$C_{24}\subset E_L[24]$，阶恰24。
取实际商和它的模域
$$
 E_{24}'=E_L/C_{24},\qquad j_{24}=j(E_{24}'),\qquad
 F_{24}=\mathbf Q(j_{24})\subset\mathbf R .
 \tag{49}
$$
这里下标24只是同源次数，不是本课题另一条名为E24的CM曲线。

§7.1已给固定 $E_L$ 的非CM证明。
任意两个循环24核若给同一个商j，则两个24同源及一个目标同构
复合成度 $24^2$ 的 $E_L$ 端同态。
非CM使该端同态准确为 $\pm[24]$；
与另一同源复合并在Hom群中消去[24]，两个原核相同。
于是整个循环24核集合中
$$
 \operatorname{Stab}(j_{24})
       =\operatorname{Stab}(C_{24}),\qquad
 F_{24}\subset\mathbf Q(E_L[24]).
 \tag{50}
$$
其嵌入集合准确是所选核的Galois轨道。
商由该稳定核下降到 $F_{24}$，所以这里用的是实在同源模型。

经典循环模多项式 $\Phi_{24}(-3072,T)$ 首一整系数，
故 $j_{24}$ 整；同时 $j_{24}$ 非CM，不会是1728或任一环类多项式的根。
将 S 扩大，纳入2、3、原坏约化、$F_{24}$ 的分歧与指数、
全部商j的碰撞和所需模型的有限坏素数。
所有这些对象固定，不随辅助素数或q改变。

### 9.2 两辅助素数及真实奇数范数

在§7.2中把 $j',F$ 换成 $j_{24},F_{24}$。
只因至少一个实嵌入及全部不同的实共轭，
原两个实根区间仍给一个固定开区间 I；
当两辅助素数充分大且 $\ell_1/\ell_3\in I$ 时，
相应 $D=\ell_1\ell_3$ 或 $4\ell_1\ell_3$ 满足
$$
 A_D=\operatorname{Nm}_{F_{24}/\mathbf Q}P_D(j_{24})<0,
 \qquad A_D\in\mathbf Z\setminus\{0\}.
 \tag{51}
$$
这一步不要求 $F_{24}$ 全实，也不要求其次数为奇数。

取
$$
 \mathcal M_{24}=\mathbf Q(E_L[24],i,\sqrt{s}:s\in S).
$$
令 c 为选定复嵌入的复共轭。
Chebotarev素数定理在两个固定共轭类给
$$
 \operatorname{Frob}_{\ell_1}=1,\qquad
 \operatorname{Frob}_{\ell_3}\in[c],\qquad
 \ell_1/\ell_3\in I,
 \tag{52}
$$
且二者任意大并避全部坏集。
因为 c 固定正数平方根，而其Weil pairing行列式为−1，
这些条件同时给
$$
 \ell_1\equiv1\pmod{24},\quad
 \ell_3\equiv-1\pmod{24},\quad
 (s/\ell_i)=1\quad(s\in S).
 \tag{53}
$$
没有另添不相容的同余条件。
尤其两模4条件仍是Elkies所需的1、−1。

$\ell_1$ 的迹模24为2，故它不是超奇异素数。
若 $\ell_3$ 超奇异，直接取 $q=\ell_3$ 得(48)。
否则二者均ordinary，而在对应CM二次域中二者均分歧。
与§7.3相同的好约化/真实24同源/Deuring论证逐素点给
$\gcd(A_D,\ell_1\ell_3)=1$。
Elkies原文§2的两个平方多项式及§7.4的整数Norm论证，
现在给某个 $q\notin S$ 满足
$$
 a_q(E_L)=0,\qquad v_q(-A_D)\text{为奇数},\qquad
 q\nmid24.
 \tag{54}
$$
此处仍先以 $(q/\ell_1)(q/\ell_3)=-1$ 取得真正超奇异性，
再使用范数赋值；没有把(54)预设为某个次数一素点。

### 9.3 完整循环核作用迫出模24

在 $E_L[24]$ 上记 $A=\operatorname{Frob}_q$。
因 $q\ge5$、迹零，准确有
$$
 A^2=[-q].
 \tag{55}
$$
标量 $[-q]$ 保持每个循环24核。
因此 A 在整个核集合的每个周期长度只能是1或2，
在(50)指定的Galois轨道上也相同。
q 已避分歧/指数坏集，所以这些周期长度正是
$F_{24}$ 中所有剩余次数。

若没有固定核，则全部剩余次数为2，
整数Norm赋值公式
$v_q(-A_D)=\sum_{\mathfrak q\mid q}f(\mathfrak q/q)
v_{\mathfrak q}(P_D(j_{24}))$
为偶数，与(54)矛盾。
所以某个自由循环24核 C 在A下固定。
取其生成元 v，必有
$Av=\lambda v$，$\lambda\in(\mathbf Z/24\mathbf Z)^\times$。
将(55)作用于真阶24的 v 得
$$
 \lambda^2=-q\pmod{24}.
$$
每个模24单位的平方都等于1：模8是奇数平方，模3是非零平方，
再用中国剩余定理。因此 $q\equiv-1\bmod24$，
证明(48)。有限 S 任意，所得到的q无穷多个且不同。

### 9.4 原覆盖边界在同一素域中有理

(48)的q仍惰性于 $\mathbf Q(\sqrt{-3})$，
故§8整个 $J_{\widetilde C}$ 的真实等式 $F_q^2=[-q]$
及完整点除子关系(47)逐一适用。
此外 $q\equiv11\bmod12$，二次互反律给 $(3/q)=1$。
原唯一 $a^3=4$ 仍在 $\mathbf F_q$，所以
$$
 P_0=(z=a,\ w=0,\ s=a\sqrt3),\qquad
 \iota P_0=(a,0,-a\sqrt3)
 \tag{56}
$$
现在两个点本身均在 $\mathbf F_q$，
不仅其差 $D_0=[P_0-\iota P_0]$ 在该域有定义。
原 $D_\infty-D_0$、实际 $\delta$ 方向及双Norm不改变；
$\delta$ 仍须保留在准确的−3扭曲中。
同时 $24\mid q+1$，$d=(q+1)/3$ 被8整除。

本节支付的是原极边界和后继半Norm可用的无限素域输入。
它不证明q+1的素因子无穷，不把q作为目标ordinary p，
也不将(56)的有理性当作最高27权非零。
使用的外部事实仍仅为§§7–8已逐项列明的Elkies
两个环类多项式命题、Chebotarev素数定理及经典循环模多项式；
新增的模24结论由(49)–(55)完整给出。
