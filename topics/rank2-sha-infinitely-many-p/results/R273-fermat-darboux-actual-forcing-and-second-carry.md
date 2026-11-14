# R273 — 原余项的 Fermat 共轭、无 $P_8$ 极的四个算子与第二单位 carry

日期：2026-11-13。**状态：实际曲线覆盖、四个有理微分算子恒等式、原十七维来源的准确 Laurent 像、带 theta 权的完整 Mellin 转置、原完整径向函数的第二单位 carry 及固定双极均已证明。未证明这些新观察行由原三条中央零强迫为零。主目标仍未完成。**

本篇把 R272 的实际非齐次余项接到 R264/R268 的原连接。四个算子都没有 $P_8$ 根处分母，但这不消去 R272 的强迫、实际四次覆盖或 theta 连接。以下用 $\mathcal F=S_8^{17}$ 表示椭圆 theta frame，用 $F_{\rm rad}=a_8e^Z$ 表示 R252/R272 的径向来源，避免把两个函数混同。

## 1. 原角参数上的精确二阶共轭

沿用
$$
y^2=x^3-x,\qquad x'=2y,\quad y'=3x^2-1,
$$
$$
u=x^{-1/2},\quad t=-y/x^{3/2}=\sqrt{1-u^4},\quad
s=u^4,\quad q=2(1-t).
\tag{1}
$$
原点分支为 $u=z+O(z^5)$、$t(0)=1$。直接微分得
$$
u'=t,\quad t'=-2u^3,\quad q'=4u^3,\quad
q''=12u^2t,\quad q(4-q)=4u^4.
\tag{2}
$$
记
$$
\mathscr L=q(4-q)\partial_q^2+(5-2q)\partial_q-3/16.
$$
对任意形式函数 $V(q)$，链式法则给准确特征零恒等式
$$
\boxed{\partial_z^2(q^{1/4}V)=4u^2q^{1/4}\mathscr LV.}
\tag{3}
$$
例如一阶导数的系数为
$q''+(q')^2/(2q)=4u^2(5-2q)$，零阶系数为 $-3u^2/4$；二阶系数由 (2) 给出。

因此齐次解是 $q^{-1/4}$ 和 $zq^{-1/4}$。其中唯一原点正规、常数为一的解为
$$
h(q)=\frac z{q^{1/4}}
=\sum_{j\ge0}\frac{(3/4)_j}{j!4^j(4j+1)}q^j.
\tag{4}
$$
这也可直接由 $\mathscr Lh=0$ 的递推证明。对 $p=4r-1$，R272 的 $h_+$ 正是 (4) 到 $r-1$ 的截断，并满足 $\mathscr Lh_+=0\pmod p$。

这里的 $q^{1/4}$ 不是原椭圆函数域中的有理 gauge。准确令
$$
w=(q/4)^{1/4},\quad v=(1-q/4)^{1/4},\quad
v^4+w^4=1,\quad u=\sqrt2wv,
$$
$$
q^{1/4}=u/v.
\tag{5}
$$
这是 R257 同一实际 Fermat 四次曲线上的分歧函数。式 (3) 保留这层覆盖；没有用一个单值椭圆函数替代它。

## 2. 原 $\mathcal K$ 的四个准确有理算子

置 $U=x^2$。R264/R268 已构造固定多项式 $P=P_8(U)$、$A=A_8(U)$ 及
$$
a_*=-\frac{583401555}{2^{32}},\qquad
f=\frac P{(U-1)^8},\qquad
R=\frac xy\frac AP,
$$
满足
$$
\mathcal Kf=0,\qquad
\mathcal K=\partial_z^2+\frac{68xy}{U-1}\partial_z+
\frac{1088x}{U-1},
$$
$$
R'+a_*=\frac1{(U-1)P^2}.
\tag{6}
$$
完整多项式规范等价于
$$
1=a_*(U-1)P^2-(U+1)AP
 +4U(U-1)(A'P-AP').
\tag{7}
$$
这里多项式上的撇号指 $\partial_U$。$P(0)=1$，其最高系数为
$$
h_0=[U^8]P=\frac{2231529755}{70587};\qquad
[U^8]A=a_*h_0.
\tag{8}
$$
所有系数及 (7) 的证明沿用 R264；本篇证书同时再次代入 (7)。

定义四个一阶算子，系数一律放在左边：
$$
\boxed{\mathcal A=
\frac P{(U-1)^8}
+\frac{yA}{a_*(U-1)^9}\partial_z,}
\tag{9}
$$
$$
\boxed{\mathcal B=
\frac{a_*P+8UA'+2A}{a_*(U-1)^8}
+\frac{yA}{a_*(U-1)^9}\partial_z,}
\tag{10}
$$
$$
\boxed{\mathcal C=(U-1)^8
\{a_*P(U-1)+4U(U-1)A'-(33U+1)A-yA\partial_z\},}
\tag{11}
$$
$$
\boxed{\mathcal D=(U-1)^8
\{a_*P(U-1)-4U(U-1)A'+(1-35U)A-yA\partial_z\}.}
\tag{12}
$$
再置
$$
\chi=\frac{xA(U)^2}{a_*}.
\tag{13}
$$

**定理 1。** 在原椭圆函数域的非交换微分算子环中，准确有
$$
\boxed{\begin{aligned}
\mathcal K\mathcal A&=\mathcal B\partial_z^2,\\
\mathcal C\mathcal A&=1-\chi\partial_z^2,\\
\mathcal A\mathcal C&=1-\chi\mathcal K,\\
\partial_z^2\mathcal C&=\mathcal D\mathcal K.
\end{aligned}}
\tag{14}
$$
尤其 $\mathcal A$ 和 $\mathcal C$ 在相应齐次解空间上互逆。四个显示算子均没有 $P$ 根处分母。

**证明。** 令 $g=fR/a_*=yA/[a_*(U-1)^9]$。由 (6)，
$f$ 与 $fz+g$ 是 $\mathcal K$ 的两个解：后者的 Wronskian 为 $f^2(1+R'/a_*)$，其对数导数准确为 $-68xy/(U-1)$。所以
$\mathcal K\mathcal A$ 的常数项和一阶项都为零。其最高两项分别为 $g$ 和 $f+2g'+68xyg/(U-1)$，后者化简为 (10) 的零阶项，证明第一式。

R268 的准确 gauge 矩阵为
$$
G=\begin{pmatrix}f&fR\\ f'&(fR)'+a_*f\end{pmatrix},
\qquad \det G=(U-1)^{-17}.
$$
它的逆矩阵第一行作用于 $(H,H')$，正是 (11)。于是
$\mathcal Cf=1$、$\mathcal C(fz+g)=z$。$\mathcal C\mathcal A-1$ 消去 $1,z$，且二阶系数为
$$
-(U-1)^{17}(fR)^2/a_*=-xA^2/a_*=-\chi.
$$
故第二式成立。同理 $\mathcal A\mathcal C-1$ 消去 $\mathcal K$ 的两个解，最高系数也是 $-\chi$，得到第三式。将第二式左乘 $\mathcal A$、第三式右乘 $\mathcal A$，或直接比较系数，得
$\mathcal B=\chi^{-1}\mathcal A\chi$。相同计算给
$\mathcal D=\chi^{-1}\mathcal C\chi$ 及第四式；$A$ 的零点分母全部取消，简化后正是 (12)。因此 (14) 是整组有理恒等式，不能只取其主符号。$\square$

固定系数的分母和 $a_*^{-1}$ 在所有惰性 $p>31$ 均为单位；这一点只涉及固定系数，不意味着在每个空间点算子都无极。$U=1$ 的实际极继续由 (9)--(12) 显示。

## 3. 原十七维来源的准确二十五维像

仍取 R239/R264 的原截面
$$
\mathcal F=S_8^{17}=W D_0,\quad
D_0=U^8(U-1)^8,\quad W=-y\vartheta\sigma^{67}.
\tag{15}
$$
原正型空间为 $\{WP_0:\deg P_0\le16\}$。将 (11) 作用到它的实际角函数 $P_0/D_0$，有
$$
\boxed{\begin{aligned}
\mathcal C(P_0/D_0)=U^{-8}\big[&-4U(U-1)A P_0'\\
&+\{4U(U-1)A'+(31U-33)A+a_*P(U-1)\}P_0\big].
\end{aligned}}
\tag{16}
$$
由于 $[U^8]A=a_*[U^8]P$，$P_0=U^{16}$ 时最高的 $U^{17}$ 项恰好取消。因此
$$
\boxed{\mathcal C\big(D_0^{-1}\mathbb Q[U]_{\le16}\big)
\subset\bigoplus_{j=-8}^{16}\mathbb Q U^j.}
\tag{17}
$$
这个 $25\times17$ 矩阵秩恰为十七，$\partial_z^2\mathcal C$ 的秩恰为十六。原水平源 $P_0=U^8P$ 准确送到常数一。

这些秩不使用目标素数样本：对给定有限空间逐项使用 (16)，证书保存完整有理矩阵及一个非零十七阶 minor。其次 $\partial_z^2$ 在椭圆有理函数上的核只有常数，因为非恒定有理函数必有极，而二阶导数不可能消去最高极。因此第二个核只由 $f$ 张成。

乘回 $\mathcal F$ 后，(17) 不是一个新的无极十七维空间。在 $O$ 处，它允许至多六十四阶极。在 $T_0=(0,0)$，$U$ 的零阶为四，$\mathcal F$ 的零阶为三十四，因此 $\mathcal F U^{-8}$ 仍至少有二阶零；在 $T_\pm=(\pm1,0)$，(17) 没有分母。故这个原二十五维像只有 $O$ 处的固定极。

若 $p>67$ 为惰性素数，$d=p+1>68$。其负 Laurent 项为 $z^{-4},\ldots,z^{-64}$，没有一项处于 $d$ 的中央余类。乘原 Gaussian $e^{-cz^d}$ 后，这些负单项仍不贡献任何中央系数。因而在这个固定空间上，原完整中央变换可按去掉原点有限主部后的正规部分定义。**必须先完成全部乘法和算子聚合，再去主部**；把某个主部提前删除后再乘固定函数，所得中央行可能改变。

## 4. theta frame 和全部 Mellin 交换项

令
$$
\nabla=\partial_z-\mathcal F'/\mathcal F,\quad
\mathcal K_{\mathcal F}=\mathcal F\mathcal K\mathcal F^{-1},
\quad \mathcal A_{\mathcal F}=\mathcal F\mathcal A\mathcal F^{-1},
$$
其余三个算子同理。准确将 (9)--(12) 中的 $\partial_z$ 换成 $\nabla$ 即得这些算子，且
$$
\boxed{\begin{aligned}
\mathcal K_{\mathcal F}\mathcal A_{\mathcal F}&=\mathcal B_{\mathcal F}\nabla^2,\\
\mathcal C_{\mathcal F}\mathcal A_{\mathcal F}&=1-\chi\nabla^2,\\
\mathcal A_{\mathcal F}\mathcal C_{\mathcal F}&=1-\chi\mathcal K_{\mathcal F},\\
\nabla^2\mathcal C_{\mathcal F}&=\mathcal D_{\mathcal F}\mathcal K_{\mathcal F}.
\end{aligned}}
\tag{18}
$$
这是实际 theta 来源的恒等式；没有把 $\partial_z$ 当成协变导数。

下面给可直接用于 (18) 的全变量转置。置
$$
c=68c_0,\quad d=p+1,\quad \mathcal E=z\partial_z,
\quad W_0=z\mathcal F'/\mathcal F-dcz^d,\quad t=du.
$$
对一个实际 $i^j$ 型聚合 $Y$，记 $V=Y/z^j$，并定义
$\mathcal J^{[j]}(Y;u)=\mathcal J_c(V;u)$；负 Laurent 项按上一节的范围处理。$j$ 是准确选取的除阶，不可以随意模四更换。

对任一保持此型的一阶算子 $a+b\nabla$，写 $B=b/z$，则
$$
\boxed{\begin{aligned}
\mathcal J^{[j]}((a+b\nabla)Y;u)
={}&\mathcal J_c(aV;u)+(t+j)\mathcal J_c(BV;u)\\
&-\mathcal J_c((\mathcal EB+BW_0)V;u)
-du\mathcal J_c(BV;u-1).
\end{aligned}}
\tag{19}
$$
证明只用完整 Euler 恒等式
$\mathcal J_c(\mathcal EZ)=du\mathcal J_c(Z)$ 和
$\mathcal J_c(cz^dZ;u)=u\mathcal J_c(Z;u-1)$；乘子 $B$ 的导数不能省去。

更一般，若要转置 $z^2B\nabla^2$，置
$$
g_0=\mathcal J_c(BV),\quad
g_1=\mathcal J_c((\mathcal EB+BW_0)V),
$$
$$
g_2=\mathcal J_c\big((\mathcal E^2B+2W_0\mathcal EB
+B(W_0^2+\mathcal EW_0))V\big).
$$
完整公式为
$$
\boxed{\begin{aligned}
\mathcal J^{[j]}(z^2B\nabla^2Y;u)
={}&(t+j-1)(t+j)g_0(u)-(2t+2j-1)g_1(u)+g_2(u)\\
&+du\{(d-2t-2j+1)g_0(u-1)+2g_1(u-1)\}\\
&+d^2u(u-1)g_0(u-2).
\end{aligned}}
\tag{20}
$$
例如 (18) 第二式中的余项必须取 $B=\chi/z^2$ 后使用 (20)。它包括 $\mathcal EB,\mathcal E^2B$、全部 $W_0$、质量和两条负移权；不是一个数 $\chi$ 乘原中央函数。对 (17) 的实际正型输入取 $j=0$ 时，这些分开项的原点极至多六十八阶，所以同一 $p>67$ 界足够。

三阶的 $\mathcal K\mathcal A$、$\partial_z^2\mathcal C$ 可直接使用 R269 的完整三阶式，或顺次使用 (19)--(20)。两种次序在先聚合全部项时相同。原三曲线在 R269 的 $Z_3,Z_2,Z_1,Z_0$ 和 CM 质量仍全部存在；(18) 没有把它们化成裸 de Rham 的 $\ell(Q)$。

## 5. 原完整径向函数的第二单位 carry

回到 R272，令 $p=4r-1>31$，并保留原函数
$$
F_{\rm rad}=a_8(q)e^{Z(q)},\qquad
a_8=\frac15(1-q/2)(1-q/4)(1+q-q^2/4)((1-q/2)^4+4),
$$
$$
[q^n]Z=\frac{34}{n4^n}\frac{(1/2)_n}{(3/4)_n}.
\tag{21}
$$
仍按 R272 的实际定义
$$
U=q^{-r}\{\log F_{\rm rad}-[\log F_{\rm rad}]_{<r}-a_0H/p\},
\quad H=q^rh_+,\quad a_0=p[q^r]Z.
\tag{22}
$$

**定理 2。** 原 $U$ 在次数小于 $3r-1$ 时全部整，但下一系数满足
$$
\boxed{p[q^{3r-1}]U
=p[q^p]\log F_{\rm rad}\equiv\frac{337}{20}\pmod p.}
\tag{23}
$$
这在所有惰性 $p>31$ 都是单位，故该系数赋值恰为 $-1$。只取 theta 部分时，右端是 $17$。

**证明。** 对 $n<p$，(21) 的 Pochhammer 比值在 $r\le n<2r$ 恰有一个分母 $p$，其他 $n$ 都整。R272 原 $a_0H/p$ 已准确消去这一整个负一层；固定 $a_8$ 的对数在 $n<p$ 也整。因此得到所说较长的整窗口。

在 $n=p$，$\{1/2+j:0\le j<p\}$ 中唯一被 $p$ 整除的项为 $p/2$；其余剩余类乘积为 $-1$。同理 $3/4+j$ 的唯一坏项为 $p/4$。Wilson 定理给
$$
\frac{(1/2)_p}{p}\equiv-\frac12,\qquad
\frac{(3/4)_p}{p}\equiv-\frac14\pmod p.
$$
于是
$$
p[q^p]Z\equiv\frac{34\cdot2}{4}=17\pmod p.
\tag{24}
$$
另一方面，对任意固定 $a(q)\in1+q\mathbb Z_p[q]$，将其在代数闭包分解为 $\prod(1-\alpha q)$，有
$$
p[q^p]\log a=[q^{p-1}]a'/a
\equiv-\sum\alpha^p=\big(-\sum\alpha\big)^p
\equiv a'(0)\pmod p.
$$
原 $a_8'(0)=-3/20$，故 (24) 加上实际角因子后正是 $337/20$。所减两个多项式次数都小于 $p$，不改变此项。$337$ 是 $1\pmod4$ 的素数，故不属于本惰性集合。$\square$

R272 的特征零共轭也精确说明这一位置为何是新共振：
$$
q^{-r}\mathscr L_0(q^rV)=\mathscr LV+
p\{(2-q/2)V'+rV/q-(p+4)V/16\}.
\tag{25}
$$
其 $q^j$ 方程中 $[q^{j+1}]V$ 的系数是
$$
(j+r+1)(4j+p+4).
$$
第一次新整除发生在 $j=3r-2$，准确系数为 $p(4p-1)$。因此不能把 $\mathscr L\bar U=\mathcal T_p^{\rm full}$ 从 R272 的整截断当作无穷整级数方程；下一共振留下 (23) 的实际单位。

## 6. 全 forcing 在另一端的真双极

R272 (14) 的全右端是
$$
\mathcal T_{p,r}+q^{-r}\mathscr L_0
(\log a_8-[\log a_8]_{<r}).
\tag{26}
$$
它模 $p$ 在 $q=4$ 的留数准确为 $4^{-r}$。theta 部分的多项式 $\mathcal T_{p,r}$ 没有这个极，不能替代 (26)。在特征零里，对
$$
Y=q^{1/4}U
$$
必须把 (25) 的全部 $p$ 修正一起代入 (3)，故
$$
\boxed{Y''=4u^2q^{1/4}
\big[\text{(26)}-p\{(2-q/2)U'+rU/q-(p+4)U/16\}\big].}
\tag{27}
$$
没有把原强迫改为齐次方程。

令 $\xi$ 为实际 (5) 覆盖在 $q=4$ 处的局部加法参数。此处
$$
q=4-\xi^4+O(\xi^8),\qquad q^{1/4}=\gamma+O(\xi^4),\quad\gamma^4=4.
$$
原 $a_8$ 有简单 $q$ 零，$\vartheta$ 在这个映到椭圆 $O$ 的分支非零，故
$$
Y=c_\gamma\log\xi+\text{正规项}+O(\xi^4\log\xi),\qquad
c_\gamma=4\gamma^{-p}.
\tag{28}
$$
这里正规项可以依赖 $p$；只陈述局部最高极，未删除完整 log germ。

由 (6)--(8)，在同一点有
$$
f=h_0+O(\xi^4),\quad R/a_*=-\xi+O(\xi^{69}),\quad
\frac{68xy}{U-1}=-68/\xi+O(\xi^3).
\tag{29}
$$
更准确地，
$R/a_*+\xi=\xi^{69}/(69a_*h_0^2)+O(\xi^{73})$。
这也证明 $\mathcal A\xi$ 从 $\xi^{69}/(69a_*h_0)$ 起，不能用其表面的一阶阶数估计局部作用。

将 (28)--(29) 代入真正的 $\mathcal K\mathcal A$，得到
$$
\boxed{\mathcal K\mathcal AY
=-\frac{69h_0c_\gamma}{\xi^2}+O(\log\xi)+O(1).}
\tag{30}
$$
这是准确的非零双极。$h_0$ 的分子素因子为 $5,7,13,37,41,53,61$，分母素因子为 $3,11,23,31$；所以 (30) 最高系数在全部惰性 $p>31$ 都是单位。乘回 $\mathcal F$ 后要保它在该分支的实际 theta gauge；本篇不把未规范化的复周期值称作 $p$ 单位。

## 7. 与原中央问题的准确接点

式 (14)、(18) 现在给出了从真实二阶自由方程到原 $\mathcal K$ 的完整有理接口，而且原 $P_8$ 的 apparent poles 已取消。式 (23) 和 (30) 都使用 R272 的完整 $a_8e^Z$，没有以任意余项或有限素数样本替换原来源。

但 $Y$ 的原点 $i$ 型是 $i$，而原三曲线的中央来源为 $i$ 不变型；即使再作导数返回该型，也必须使用 (19)--(20) 及 R269 的准确实际运输。固定双极在另一分支非零不等于原 $p$ 依赖中央投影非零。R62 已经给出非中央单位与中央零可以并存的精确结构；R182 的原完整失败则控制全体 $[w^{rp^n}]$，不控制本篇乘子产生的所有列。

所以接下来的可检验问题是：将 (27)--(30) 的真实聚合送入 R62 的原中央 $P_0$ 或 R182 的全部原中心深度条件后，哪些完整行确实由原三曲线控制。不能只引用双极、(17) 的秩或 (14) 在齐次解上的互逆来结束。

## 证书与依赖

[精确脚本](../scripts/check-fermat-darboux-actual-second-carry.py) 和
[输出](../scripts/check-fermat-darboux-actual-second-carry.json) 核实原 (7)、四个非交换算子的每一阶系数、全部十七列、两个准确秩、Fermat 共轭、一般参数共振式、原 carrier 及固定极。全部是有理恒等式，没有目标素数扫描。

依赖：R264 的实际 $\mathcal K$ 与 $P_8,A_8$；R268 的有理 gauge 和 de Rham 规范；R269 的实际三阶及原曲线返回；R252/R257 的原径向函数与 Fermat 覆盖；R272 的完整强迫、整窗口和实际来源共轭。本篇不修改这些已发表来源。
