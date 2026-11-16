# R842 补注：原 Euler 原函数的提升缺陷与唯一零 charge 修正

日期：2026-11-16。**状态：以下同预算完整核、唯一可修方向和实际高前缀限制已证明。没有据此判断原受限类 $[b_0]$ 的零或非零。**

本注接 [R836](../results/R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)
的同一来源提升，以及
[原全边界与负纤维 mask](2026-11-16-r842-negative-fiber-global-mask-and-same-source-boundary.md)。
它精确检查逐 charge 积分能否替代那个提升：一般不能。
可由原零 charge 截面修复的提升差，恰好只有显示的一条直线。
此结论属于原全局格，而非只在原点截断后比较常数项。

## 1. 原格、不可约条件与真实单位逆

沿用原十九角曲面 $X$、几何整曲线 $C=(F=0)$ 及
$$
\mathcal H_m=H^0(X,\mathcal O_X(mC)),\qquad
N=\mathcal O_C(C),\qquad
\mathcal E=Y\partial_Y,\qquad e=\mathcal EF.
\tag{1}
$$
$X$ 几何连通，$H^0(X,\mathcal O_X)=k$。
$F$ 是原清极模型中的实际方程，$b=\deg_YF>0$，
$F_0(t)=F(t,0)\ne0$。
原点 $P=(0,1)$ 满足 $e(P)\ne0$，所以 $e|_C$ 是整曲线上非零的截面。
不允许把 $F$ 换成任意一个形式幂或只保一条局部分支。

保 $3b<p$。按原全局 Euler 框架，
$$
\mathcal H_m=\mathcal H_m^0\oplus\mathcal H_m^{>0},
\qquad
\mathcal E\mathcal H_m=\mathcal H_m^{>0}
\quad(m\le3).
\tag{2}
$$
正 charge 单位逆 $\mathcal E_+^{-1}$ 只在第 $n$ 个原 charge 上除以
$n\in\{1,\ldots,3b\}$，因此保持同一十九角格。
它不是对 $C$ 上任意函数选择一个原函数。

原限制序列准确给
$$
\begin{aligned}
\ker[\mathcal H_3\to H^0(C,N^3)]&=F\mathcal H_2,\\
\ker[\mathcal H_2\to H^0(C,N^2)]&=F\mathcal H_1,\\
\ker[\mathcal H_1\to H^0(C,N)]&=kF.
\end{aligned}
\tag{3}
$$
这些等式只使用同一有效 Cartier 除子的截面序列；
没有在清极以后加入额外分母。
原高前缀和同一个物理 $q\,t^r$ 返回另保，不由 (2) 自动继承。

## 2. 所有提升差的完整零 charge 判据

对任意 $L\in\mathcal H_1^{>0}$ 定义
$$
I_L=\mathcal E_+^{-1}(F^2L)\in\mathcal H_3^{>0}.
\tag{4}
$$
$F^2L$ 没有零 charge，故 (4) 有唯一意义，并且
$\mathcal EI_L=F^2L$。

**定理。** 以下两条件等价：
$$
\begin{array}{ll}
\text{(i)}&
\exists V\in\mathcal H_3^0,\quad (I_L+V)|_C=0;\\
\text{(ii)}&L\in k e .
\end{array}
\tag{5}
$$
若 $L=c e$，唯一修正及修正后的完整来源分别为
$$
\boxed{
I_L=\frac c3(F^3-F_0^3),\qquad
V=\frac c3F_0^3,\qquad
I_L+V=\frac c3F^3 .
}
\tag{6}
$$

**证明。** 设 (i) 成立。由 (3)，存在 $K\in\mathcal H_2$ 使
$I_L+V=FK$。由于 $\mathcal EV=0$，
$$
F^2L=eK+F\mathcal EK.
\tag{7}
$$
限制到整曲线 $C$ 后，$e|_C\cdot K|_C=0$。
$e|_C$ 非零，故 $K|_C=0$。由第二条 (3)，
$$
K=FM,\qquad M\in\mathcal H_1.
$$
将它代入 (7)，在原截面环中约去非零的 $F$，得到
$$
FL=2eM+F\mathcal EM.
\tag{8}
$$
再限制到 $C$。因为 $2$ 为单位、$C$ 整且 $e|_C\ne0$，
有 $M|_C=0$。
最后一条 (3) 因而给
$$
M=c_0F,\qquad c_0\in k.
$$
这里的标量结论来自 $\mathcal H_0=k$，不是把 $M/F$ 的局部正则性
直接升级为常数。
代回 (8)，得
$FL=3c_0Fe$，所以 $L=3c_0e\in ke$。

反过来，若 $L=ce$，原乘积法则
$\mathcal E(F^3)=3F^2e$ 和零 charge 投影给第一式 (6)。
$F_0^3$ 确实属于 $\mathcal H_3^0$：原角格按 charge 分解，
$F_0\in\mathcal H_1^0$，且原截面乘法不改变预算。
于是后两式 (6) 也在原格中成立。

若还有另一个零 charge 修正，它与 (6) 之差是一个在 $C$ 上为零的
$k(t)$ 函数。$C$ 不是底纤维，投影 $C\to\mathbf P^1_t$ 占优，
故 $k(t)\hookrightarrow k(C)$，这个差只能为零。
修正唯一。证毕。

整个论证可以先在代数闭包上核对，再下降回原 $k$；
显示的 $F,L,V$ 和唯一标量关系均保持原定义域。

## 3. 提升自由不会下降为曲线上的积分算子

R836 中同一对
$$
G|_C=V_0,\qquad(\mathcal EG)|_C=V_1
$$
的全局实现相差 $F^2\mathcal H_1$。
这个自由对两条实际曲线值确实不可见，但对 (2) 的原函数并不可见。

取实际 $G=F^2e$。它满足
$$
G|_C=0,\qquad(\mathcal EG)|_C=0,
$$
而
$$
\boxed{
\left.\mathcal E_+^{-1}(F^2e)\right|_C
=-\frac13F_0^3\ne0 .
}
\tag{9}
$$
因此 $\mathcal E_+^{-1}$ 不能下降为
$\mathcal H_3/F^2\mathcal H_1$ 上的原曲线值算子。
这不是说 $F^2e$ 已通过原三长窗：
这里检查的是 R836 的两条曲线值提升自由，
其后仍须支付同一 $3\eta$ 修正和实际第三长行。

定理还准确量化了这个缺陷。定义
$$
\mathscr D:
\mathcal H_1^{>0}\longrightarrow
H^0(C,N^3)/\operatorname{res}_C(\mathcal H_3^0),
\qquad
L\longmapsto[I_L|_C].
$$
则
$$
\boxed{\ker\mathscr D=ke,\qquad
\mathcal H_1^{>0}/ke\ \hookrightarrow\
H^0(C,N^3)/\operatorname{res}_C(\mathcal H_3^0).}
\tag{10}
$$
所以仅添几列零 charge 补偿，不能把所有原提升差都消掉。

若同时使用 R833 的完整负水平资料
$$
z_-=C.H_-,\qquad
\dim\mathcal H_1^0=z_-+1,\qquad
\dim\mathcal H_1=\frac{\kappa+\chi}{2}+1,
$$
则这条真实缺陷映射的秩准确为
$$
\boxed{\operatorname{rank}\mathscr D
=\frac{\kappa+\chi}{2}-z_--1.}
\tag{11}
$$
原 $r=2$ 全 profile 中 $z_-\le2$。
(11) 是完整格上的结论，不能据此断言相同秩保留到高前缀子空间
$\mathscr W_T$ 或原三长核。

## 4. 原点前缀与后续相容式

在原 $r=2$ 资料中
$$
F_0(t)=\lambda\,d(t)^cH(t),\qquad d(0)=1,\qquad
\deg H\le2,\qquad F_0\ne0 .
$$
故 (9) 在 $P$ 的准确阶为
$$
\operatorname{ord}_P(I_e|_C)
=3\operatorname{ord}_{t=0}F_0\le6.
\tag{12}
$$
特别，只要实际 $T>3\operatorname{ord}_0F_0$
（例如 $T>6$），这个原函数并不保持 $T$ 阶零前缀。
本注不将 $T>6$ 偷加到所有尚未分类的小参数情形；
始终可直接用 (12) 的准确门。

对这一条 $L=e$，(6) 的真实零 charge 项确能修回零曲线值。
对其余 $L$，定理说明：即使不要求高前缀，
原 $\mathcal H_3^0$ 也不能完成这种修复。
若某个实际构造先取同一个 $G$ 满足
$\mathcal EG=FA$，再写
$G=\mathcal E_+^{-1}(FA)+G^0$，这个表达仍然合法；
但改变 $F^2\mathcal H_1$ 提升时，$A$ 和 $G^0$ 必须一起变化，
不能只把积分符号搬到曲线商中。

因此后续仍使用 R842 的同一个
$\omega_1\in\mathcal Q_T$、允许的
$\sigma\in\mathcal Q'_T$、唯一 $V_1$ 及同一全局 $G$。
本注没有增加原中央零，没有把局部补偿视为 $\mathcal Q'_T$ 的任意值，
也没有判断完整正水平、底无穷远和原点短行的和。

依赖：
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R833](../results/R833-original-euler-image-and-negative-horizontal-cokernel.md)；
[R836](../results/R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)；
[原全 Euler 框架](2026-11-15-original-global-euler-frames-and-complete-alpha-residue-pair.md)。
全文为原截面格中的精确恒等，不需新数值运行。
