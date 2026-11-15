# R239：不可分离的完整三阶圆可同时支付例外端芽的四个能量门

日期：2026-11-15。完整纸面存在证明；没有运行真实 profile 积分、参数求根、符号目标或几何计算。

本稿在 [R238](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md) 的准确标量归约上，构造真正有限宽度的 profiles，使 $L_c=L_s=M_c=M_s=0$。关键不是把渐近首项设零，而是对保留全部真实积分的一个归一化函数使用非退化隐函数定理。

来源：[R183 八平移与完整四槽第三阶](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R233 四尺度三矩圆](R233-four-scale-moment-circles-cancel-both-exceptional-leading-energies.md)、[R235 双完整 block 的不可分离构造](R235-nonseparable-complete-third-order-circles-with-zero-exceptional-leading-energies.md)、[R237 完整下一 mixed 层](R237-complete-next-mixed-layer-after-exceptional-leading-cancellation.md)及 R238。

## 1. 完整结论及范围

给定任意正活动区间 $I=[\ell,r]\Subset(0,\infty)$，存在非退化、归一、$C^\infty$ 三矩圆 $(F,G)$，使：

1. 任意常数 $GL(2,\mathbb R)$ 换基都不能把它变成两个支撑不交的 profiles；
2. 完整第三 hook 在其整个 profile 平面上为零；
3. R231 的两领先能量与 R237 的两下一层能量全部准确为零；
4. 对任意已给定的真实 $M=0,T=\kappa\mathfrak H$ 几何，只要 I 是其共同合法区间，两个二阶及四个第三阶完整 range 均成立。

第 3 项使用 R237 的 $b=0$ 算子。若用于其实际例外 germ，还需该固定 I 满足 $x+k_e/h_e>0$；本稿不改变已经给定的合法几何或右锚来取得这个条件。

最终目标度量由本稿最终第一 profile F 定义。在以下构造过程中改变节点、宽度或角度，是选择新的 profiles 及相应目标；不声称保持 R193 或另一先前指定的同一个目标度量。

本稿没有支付第四 ruling 的全部剩余层、完整 period 或 joint 系统，也不继承旧第一包 $g=0$、F8 通量读出或特定平端解析类。

## 2. 四节点与固定偶 bump

先在一个任意小的正开区间 J 内选定中心 $c>0$。参数为

$$
\zeta\in[1/5,1/4],\qquad
\xi_0=0,\quad\xi_1=\zeta,\quad\xi_2=1,\quad\xi_3=2,
\qquad a_i=c+\delta\xi_i,
\tag{1}
$$

其中 $\delta>0$ 将足够小。固定一个非零实偶函数
$\chi\in C_c^\infty((-1,1))$。取固定 $\rho>0$ 足够小，例如

$$
\rho(c+1)<1/100.
\tag{2}
$$

定义

$$
\psi_\delta(y)=\chi\left(\frac{y-1}{\rho\delta}\right),
\qquad
u_{ij}(x)=\psi_\delta\left(\frac{x-3j\delta}{a_i}\right),
\quad 0\le i\le3,\ 0\le j\le7.
\tag{3}
$$

该微包的中心和宽度分别为

$$
X_{ij}=c+\delta(\xi_i+3j),\qquad
\ell_i=\rho\delta a_i.
\tag{4}
$$

当 $\delta$ 足够小且 $a_i<c+1$，每个半支撑宽度小于 $\delta/100$。同一基本四包的最小中心间距至少 $\delta/5$；相邻完整四包的间隙中心差至少 $\delta$。故全部 32 个微包支撑严格不交，且可同时置于 J 内。这个结论在上述紧 $\zeta$ 区间及足够小的正 $\delta$ 上一致成立。

相对节点的重心权为

$$
\nu_i=\frac1{\prod_{m\ne i}(\xi_i-\xi_m)},
\qquad
(\nu_0,\nu_1,\nu_2,\nu_3)
=\left(-\frac1{2\zeta},\frac1{\zeta(1-\zeta)(2-\zeta)},
-\frac1{1-\zeta},\frac1{2(2-\zeta)}\right).
\tag{5}
$$

写 $s_i=\operatorname{sign}\nu_i=(-,+,-,+)$，并令

$$
v_i=\delta^{-3}\nu_i,
\qquad w_i=|v_i|a_i^3,
\qquad b_j=(-1)^j\binom7j^{1/3}.
\tag{6}
$$

完整八复制 pair 是

$$
f=\sum_{j=0}^7\sum_{i=0}^3b_j\sqrt{w_i}\,u_{ij},\qquad
g=\sum_{j=0}^7\sum_{i=0}^3b_js_i\sqrt{w_i}\,u_{ij}.
\tag{7}
$$

所有表达式均是有限的真实光滑 profiles。即使幅度在 $\delta\downarrow0$ 时增大，对每个最终选定的正 $\delta$ 它们都有限，最后再作共同正归一化。

## 3. 三矩与全部第三阶对每个参数准确成立

四个不同尺度的重心权恒满足

$$
\sum_i v_i a_i^m=0,\qquad m=0,1,2.
\tag{8}
$$

R233 的尺度公式因而说明每个基本 pair 的三交叉矩准确为零，两对角三矩相等。平移的矩变换是同一三维上三角变换，所以每个 j 仍分别满足三矩；乘 $b_j$ 及相加保持它们。

每个微包内 $g=s_if$，故第三 hook 的完整限制准确为零。R183/R233 已付：对于任意这样的基本三矩 pair，四个完整第三 ruling 槽在其整体平移量上是次数至多六的多项式，且不同完整三矩包之间的真实第二场和 forcing 可按同一右锚相加。

因此

$$
\sum_{j=0}^7 b_j^3j^m
=\sum_{j=0}^7(-1)^j\binom7j j^m=0,
\qquad 0\le m\le6,
\tag{9}
$$

支付全部四个第三槽。节点 $\zeta$ 与基本形状 $\psi_\delta$ 虽然变化，但对每一个固定参数，八份仍是同一个基本 pair 的真实平移，所以 (9) 始终适用。

这一继承包含真实 s-history 与两 collar 条件，不是只消某个局部 cubic density。随后固定的正交变换保持整个第三槽张量为零。

## 4. 真实 bulk 的一致展开

沿用 R238 的 $\mathcal G,\mathcal D,E$，以及

$$
S(u)=\frac14\int x^4((\mathcal G(u,u)/x)'')^2,
\qquad
\mathfrak T(u)=\frac14\int x^4(\mathcal G(u,u)/x)''
(\mathcal D(u,u)/x)''.
$$

R235/R238 给两个完全局部的准确式

$$
S(u)=\frac1{64}\int x^6W^2(u''')^2,
\qquad
\mathfrak T(u)=-\frac1{64}\int
x^5W(3x^2u''-5xu'+4u)(u''')^2,
$$

$$
W=x^2u''-2xu'+2u.
\tag{10}
$$

令

$$
I_\chi=\int_{-1}^1(\chi'')^2(\chi''')^2>0,
\qquad K=\frac{I_\chi}{64\rho^9}>0.
\tag{11}
$$

正性理由很短：若该积分为零，则 $(\chi''^2)'=2\chi''\chi'''=0$，由零 collar 得 $\chi''=0$，再由紧支撑得 $\chi=0$，矛盾。

对 $u(x)=\chi((x-X)/\ell)$，在 (10) 中令 $x=X+\ell y$。S 的括号在提出 $\ell^{-9}/64$ 后，零阶和一阶为

$$
X^{10}I_\chi
+\ell X^9\left[
10\int y(\chi'')^2(\chi''')^2
-4\int\chi''\chi'(\chi''')^2\right].
\tag{12}
$$

$\mathfrak T$ 在提出 $-\ell^{-9}/64$ 后，对应为

$$
3X^9I_\chi
+\ell X^8\left[
27\int y(\chi'')^2(\chi''')^2
-11\int\chi''\chi'(\chi''')^2\right].
\tag{13}
$$

固定偶 bump 使两个一阶积分均为奇函数积分，准确为零。所有余项都是 X、$\ell$ 的有限多项式，系数是同一个固定 $\chi$ 的有限真实积分。

将 (4) 代入，得到

$$
\boxed{
S(u_{ij})=K\delta^{-9}
\left[c+\delta(\xi_i+30j)+\delta^2R^S_{ij}(\delta,\zeta)\right],
}
$$

$$
\boxed{
\mathfrak T(u_{ij})=-3K\delta^{-9}
\left[1+\frac{27j}{c}\delta+\delta^2R^T_{ij}(\delta,\zeta)\right].
}
\tag{14}
$$

各 R 在 $\delta=0$ 附近以及 $\zeta\in[1/5,1/4]$ 的稍大紧邻域上有实解析延拓，连同所需参数导数一致有界。其依据是换元后的有限多项式和 $a_i^{-1}$，且 $a_i$ 一致远离零；不是仅有一个未控的逐点渐近符号。

## 5. 八份幅度权怎样进入真实四个标量

按 R238 记

$$
P=E(A,X),\quad Q=E(X,X),\quad U=E(A,Y),\quad V=E(X,Y).
$$

由于 (7) 是完整三矩 pair，X、Y 紧，R238 的真实总体边界项准确为零。所以这四个原能量可按其准确微包 bulk 公式求和。幅度四次为

$$
(b_j\sqrt{w_i})^4=B_j\delta^{-6}\nu_i^2 a_i^6,
\qquad B_j=b_j^4=\binom7j^{4/3}>0.
\tag{15}
$$

置

$$
B=\sum_jB_j>0,\qquad
\bar d=\frac{\sum_j3jB_j}{B},
$$

$$
Q_m=\sum_i\nu_i^2\xi_i^m,
\qquad S_m=\sum_is_i\nu_i^2\xi_i^m,
\qquad m=0,1.
\tag{16}
$$

不需评价任何根式权重。事实上 $B_j=B_{7-j}$ 给 $\bar d=21/2$，但下面保留符号即可。

由 (14)、(15) 逐项收集，四个**真实原能量**具有一致展开

$$
P=KB\delta^{-15}
\left[c^7S_0+\delta c^6(7S_1+10\bar d S_0)+\delta^2R_P\right],
$$

$$
Q=KB\delta^{-15}
\left[c^7Q_0+\delta c^6(7Q_1+10\bar d Q_0)+\delta^2R_Q\right],
$$

$$
U=-3KB\delta^{-15}
\left[c^6S_0+\delta c^5(6S_1+9\bar d S_0)+\delta^2R_U\right],
$$

$$
V=-3KB\delta^{-15}
\left[c^6Q_0+\delta c^5(6Q_1+9\bar d Q_0)+\delta^2R_V\right].
\tag{17}
$$

R 同样实解析并有一致导数界。特别地，八平移的均值项没有被忽略；它们在下一行列式中准确抵消。

设

$$
D_0(\zeta)=S_0Q_1-S_1Q_0.
$$

则 (17) 给

$$
UQ-PV=-3K^2B^2c^{12}\delta^{-29}
\left[D_0(\zeta)+\delta R_F(\delta,\zeta)\right].
\tag{18}
$$

例如一阶交叉中两个 $19\bar d S_0Q_0$ 相消，剩下
$7S_0Q_1+6S_1Q_0-6S_0Q_1-7S_1Q_0=D_0$。

## 6. 准确简单根

由 (5) 的有限有理代数，

$$
S_0=\frac{3-\zeta}{\zeta(2-\zeta)^2}>0,
\tag{19}
$$

$$
\boxed{
D_0(\zeta)=
-\frac{2N(\zeta)}{8\zeta^3(1-\zeta)^3(2-\zeta)^2},
\qquad
N(\zeta)=2-9\zeta-3\zeta^2+5\zeta^3-3\zeta^4.
}
\tag{20}
$$

可直接把 $A_i=\nu_i^2$ 代入

$$
D_0=2[-\zeta A_0A_1-2A_0A_3+(1-\zeta)A_1A_2-A_2A_3]
$$

核对 (20)。端点和导数为

$$
N(1/5)=72/625>0,\qquad N(1/4)=-95/256<0,
$$

$$
N'=-9-6\zeta+15\zeta^2-12\zeta^3
\le-9+15/16<0
\quad(1/5\le\zeta\le1/4).
\tag{21}
$$

故有唯一 $\zeta_0\in(1/5,1/4)$，使 $N(\zeta_0)=0$，且
$D_0'(\zeta_0)\ne0$。这是准确纸面隔离和单根结论，不是研究求根计算。

## 7. IFT 支付的是有限正宽度的完整原能量

对 $\delta>0$ 定义

$$
\mathcal F(\delta,\zeta)
=-\frac{\delta^{29}(UQ-PV)}{3K^2B^2c^{12}}.
\tag{22}
$$

由 (18)，它有实解析延拓

$$
\mathcal F(\delta,\zeta)=D_0(\zeta)+\delta R_F(\delta,\zeta)
$$

到 $\delta=0$ 的一个开邻域。这个延拓只用于有限维隐函数定理；$\delta=0$ 或负 $\delta$ 不解释为实际重叠 profiles、负宽度能量或真实路径。

由 (21)，存在 $\delta_0>0$ 和实解析函数 $\zeta(\delta)$，满足

$$
\zeta(0)=\zeta_0,\qquad
\mathcal F(\delta,\zeta(\delta))=0
\quad(|\delta|<\delta_0).
\tag{23}
$$

选任何足够小的正 $\delta$。它仍在 §2 的严格正支和支撑开域内；(22) 的乘子非零，故

$$
\boxed{UQ-PV=0}
\tag{24}
$$

对该实际有限宽度 pair 精确成立。这里的 U、Q、P、V 是参数变化后的全部真实原积分；没有把参数变化只放进主系数而冻结 profile 本身。

又由 (17)、(19)，

$$
P>0,\qquad Q>0,\qquad
t=-P/Q\longrightarrow-S_0(\zeta_0)/Q_0(\zeta_0)\in(-1,0).
\tag{25}
$$

严格 $|S_0|<Q_0$ 来自两种符号的正权均非零。缩小 $\delta_0$ 后，实际 t 一致远离 $0,\pm1$。因此 $Z=U+tV=0$，且没有退化到 R235 排除的零角情况。

## 8. 四门同时为零与严格不可分离

为已选有限正 $\delta$ 取

$$
\alpha=\tfrac12\arcsin t\in(-\pi/4,0),\qquad
\beta=\pi/2-\alpha.
\tag{26}
$$

R238 (5)、(6) 与 (24) 说明两个旋转 pair 都满足

$$
L_c=L_s=M_c=M_s=0.
\tag{27}
$$

其整个三阶性质由 §3 保留。现在按 R235 的放置方法，在给定 I 内先选两个不交正小区间 J、HJ，H>0；上述构造放在 J，第二份取其正伸缩 H 的同构拷贝。第一份用角 $\alpha$，第二份用 $\beta$，再相加。

领先能量在正伸缩下乘 H，次层能量保持零次；两种能量均按完整三矩 block 相加，真实左二次尾交叉由 $E(x^2,Z)=0$ 支付。因此合成 pair 仍满足 (27)。完整二、三阶 forcing 的跨 block 项按 R235 已付的紧第二场论证为零，所有原 s-history 保持同一个起点。

令

$$
\varrho=\frac{\cos\alpha-\sin\alpha}{\cos\alpha+\sin\alpha}>1.
$$

在四种实际非零微包上，合成 profile 的 projective 方向分别为

$$
\varrho,\quad-\varrho^{-1},\quad-\varrho,\quad\varrho^{-1}.
\tag{28}
$$

它们两两不同。任意 $GL(2,\mathbb R)$ 对实射影线是双射，故不能把四方向变成只含两条坐标轴的方向集合。于是任何常数换基都不能得到不交支撑的两 profile。

合成后的三矩 Gram 是相等正对角且交叉零。作共同正归一化得到结论中的 $(F,G)$；它不改变 (27)、第三阶恒等或 (28)。

## 9. 已付与未付

本稿通过同一有限参数 $\zeta(\delta)$ 对真实 profiles 的完整积分准确支付四个能量门。固定偶 bump 的作用仅是使一致展开的一阶宽度项消失；真实八平移幅度及其均值都完整进入 (17)、(18)。

这说明 R237 的新门也不能作为所有合法、不可分离三矩圆的普遍否定。它仍可排除未支付 (24) 的特定冻结圆，但不能据此推一般刚性。

同时，四个能量零只消掉 R231、R237 已确定的两层。更低的完整 mixed/ruling 项、第四 period、global joint 以及后续 Taylor 阶仍须独立支付。本稿没有声称有第四阶解，也没有把未计算的余项当作零。
