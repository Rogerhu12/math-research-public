# R211：固定圆周期 gauge 的有限相容条件、简单退化点与准确 Green 右逆

日期：2026-11-15。**完整纸面证明；无新研究计算。** 承接 [R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md) 的真实同右锚算子及 [R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md) 的完整 period/ruling 判据。本稿对一个明确的局部 gauge 类给出充分性和实际右逆，不把退化通量必要条件单独冒充全局可解。

在已经付清整个 pure 周期的 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 闭 hook 上，该右逆只需作用于两个剩余 mixed 目标函数。完整 ruling 仍由同一个所得 gauge 检查，不能另选一个周期不相同的 w。

## 1. 固定数据及目标类

固定原物理区间 $I=[l,r_*]$、原真实几何、原 profile 圆 $(f,g)$ 和原目标度量。所有 profiles 为实光滑函数，在共同双 collar 为零。记

$$
p=f',\qquad q=f'',\qquad
A=6pq'-2q^2,\qquad V=6(qq')',
$$

$$
\mathscr M u=(Au')'-Vu.
\tag{1}
$$

R181 的原 Volterra 算子为 $L_f(w)=\mathfrak H(w;f,f)$，准确满足

$$
L_f(w)''=\mathscr M(w'),\qquad \mathscr M p=0.
\tag{2}
$$

取闭内区间 $J=[a,b]\Subset(l,r_*)$。本稿首先要求 $A$ 在整个 J 不为零，之后允许有限个内部简单零点。**不要求 p 在 J 非零，也不要求 A 为正。**

采用一个保留真实左尾的目标类：

$$
\mathcal G_J={G\in C^\infty(I):
G''\in C_c^\infty((a,b)),\quad
G=0\text{ 于原右 collar}\}.
\tag{3}
$$

若 $v=G''$，同右锚决定

$$
G(x)=\int_x^{r_*}(t-x)v(t)\,dt.                            \tag{4}
$$

所以 G 在 J 右方为零，在 J 左方可以有非零仿射尾。式 (3) 不要求把这个尾删掉。对给定原周期目标，$G''$ 在 J 外为零是必须单独检查的函数条件；后面的有限矩不能替代这项支撑条件。

限定 gauge 类为

$$
\mathcal D_J={w\in C_c^\infty((a,b)):
I_j(f,w)=I_j(g,w)=0,\quad j=0,1,2\},                      \tag{5}
$$

其中 $I_2$ 表示原 $I_2^*$，

$$
I_0(F,w)=\int_I F''w'',\quad
I_1(F,w)=\int_I xF''w'',\quad
I_2(F,w)=\int_I x^2F''w''+2\int_I F'w'.                    \tag{6}
$$

这六条保证 R184 的完整第三 range。对于某条几何它们可能强于实际所需三矩条件，故本稿的必要充分性只针对所指定的 $\mathcal D_J$；不将失败扩大到全部全局 gauge。

## 2. 正则区间上的两个准确端条件

先假设

$$
\min_{x\in J}|A(x)|>0.                                    \tag{7}
$$

选 $\mathscr M y=0$ 的两个真实齐次解，初值规范为

$$
y_1(a)=1,\quad A(a)y_1'(a)=0,
\qquad y_2(a)=0,\quad A(a)y_2'(a)=1.
\tag{8}
$$

正则线性 ODE 给光滑唯一解；自伴性给全 J 上恒等

$$
A(y_1y_2'-y_1'y_2)=1.                                    \tag{9}
$$

对任意 $v\in C_c^\infty((a,b))$，定义零左 Cauchy 数据的 Green 解

$$
\boxed{
u_v(x)=y_2(x)\int_a^xy_1(t)v(t)\,dt
-y_1(x)\int_a^xy_2(t)v(t)\,dt.
}                                                            \tag{10}
$$

由 (9) 直接求导得到
$\mathscr M u_v=v$、$u_v(a)=u_v'(a)=0$。其两个准确右端条件是

$$
\boxed{\int_a^b y_1v=0,\qquad \int_a^b y_2v=0.}           \tag{11}
$$

确实，在 v 支撑右方，(10) 为
$y_2\int y_1v-y_1\int y_2v$；(9) 表明右端的值和导数同时为零，当且仅当 (11) 成立。于是 (11) 成立时 u 在两端邻域都恒零，可以准确零延拓为 $C_c^\infty((a,b))$。

反过来，任何紧支撑 u 解都由 Green 恒等式满足 (11)：

$$
\int_a^b y_i\mathscr M u
=\int_a^b u\mathscr M y_i
+[A(y_iu'-y_i'u)]_a^b=0.
$$

它还必须等于 (10)，因为差满足正则齐次方程和零左 Cauchy 数据。这里的两个 $y_i$ 是齐次 adjoint 解，不是预设了某种 Dirichlet 谱条件的特征函数；不需要任何正性或无共轭点假设。

## 3. 恢复 w 与六交叉矩：至多九条线性条件

令七个固定密度为

$$
\kappa_*=1,
$$

$$
\begin{aligned}
\kappa_{F,0}&=-F''',\\
\kappa_{F,1}&=-F''-xF''',\\
\kappa_{F,2}&=2F'-2xF''-x^2F''',\qquad F=f,g.
\end{aligned}                                               \tag{12}
$$

对紧支撑 u，$w'=u$ 的六矩由一次分部积分准确写成

$$
I_j(F,w)=\int_a^b\kappa_{F,j}u.                            \tag{13}
$$

其中 $I_2$ 的 $2\int F'u$ 已保留。另有
$\int u=0$，恰是由右锚积分恢复的 w 也在左侧为零的条件。

对每个 (12) 的密度 $\kappa$，定义

$$
\boxed{
\psi_\kappa(t)=\int_t^b\kappa(x)
\{y_2(x)y_1(t)-y_1(x)y_2(t)\}\,dx.
}                                                            \tag{14}
$$

这是 $\mathscr M\psi_\kappa=\kappa$、
$\psi_\kappa(b)=\psi_\kappa'(b)=0$ 的准确终端 Green 解。Fubini 直接给

$$
\int_a^b\kappa(x)u_v(x)\,dx
=\int_a^b\psi_\kappa(t)v(t)\,dt.                          \tag{15}
$$

因此有如下完整局部范围定理。

**定理一。** 在 (7) 下，对 $G\in\mathcal G_J$，存在
$w\in\mathcal D_J$ 使 $L_f(w)=G$，当且仅当 $v=G''$ 满足

$$
\boxed{
\int y_1v=\int y_2v=0,
\qquad \int\psi_\kappa v=0
\quad(\kappa\text{ 为 (12) 的七项}).
}                                                            \tag{16}
$$

所有积分在同一 J 上。共有至多九条准确实线性条件；不预先断言它们独立。

**准确右逆。** 条件通过后，先按 (10) 求 u，再按原右锚取

$$
\boxed{\mathcal R_JG(x)=w(x)=\int_{r_*}^{x}u_v(t)\,dt.}   \tag{17}
$$

u 先零延拓至 I。式 (11) 给 u 紧支撑，$\kappa_*$ 对应条件给 $\int u=0$，所以 w 紧支撑在同一个 J；其余六项给 (5)。

最后，(2) 给 $(L_f(w)-G)''=0$。J 右方 u、w 都为零，原 R181 右积分的 integrand 也为零，所以 $L_f(w)=L_f(w)'=0$；G 由 (3) 有相同右端数据。故这个全局仿射差准确为零，得到整个 I 上的 $L_f(w)=G$，包括原左尾。

必要性由 $u=w'$、(11)、(13) 和 $\int u=0$ 得到。若两个局部 gauge 给同一 G，其导数之差满足正则齐次 ODE 和零左数据，故二者相同。于是 (17) 在这个局部类中还是唯一解。

如果目标另外满足 $G\in C_c^\infty((a,b))$，(16) 可再写成
$\int y_i''G=0$、$\int\psi_\kappa''G=0$。一般允许左仿射尾的 (3) 则保持 $G''$ 形式，不能未经端项检查作这一步。

## 4. 右逆的光滑参数、种子与支撑

固定一个较小紧支撑包络 $J_0\Subset(a,b)$。对于 v 支撑在 $J_0$ 且通过 (16) 的输入，u 在 $J_0$ 左方由零 Cauchy 数据为零，在 $J_0$ 右方由 (11) 为零；(17) 和零均值再使 w 在两侧都为零。因此不会为满足六矩而暗中增加 J 外的尾或修改 profiles。

公式 (10)、(14)、(17) 只使用固定光滑核和有限区间积分，对这固定支撑类是连续线性映射。若 $G_\theta$ 光滑依赖相位、$2\pi$ 周期、具有共同支撑包络且逐相位通过 (16)，则

$$
w_\theta=\mathcal R_JG_\theta
$$

同样光滑、周期、共同 collar 零；$G_0=G_\pi=0$ 自动给 $w_0=w_\pi=0$。若目标仅含有限相位谐波，右逆保留同一谐波集合。这不是对任意退化全局问题声称有连续选根，而是已写出的单个固定线性右逆。

## 5. 内部简单退化点：一个通量值就是全部局部匹配条件

设 $x_0$ 满足

$$
A(x_0)=0,\qquad A'(x_0)\ne0,\qquad p(x_0)\ne0.            \tag{18}
$$

对方程 $\mathscr M u=v$，R181 的无除法通量身份为

$$
\{A(pu'-qu)\}'=pv.                                       \tag{19}
$$

在一个邻域中固定通量常数，令

$$
\mathcal F(x)=C+\int_{x_*}^{x}p(t)v(t)\,dt.
$$

**简单零点引理。** 一侧的光滑解可以越过 $x_0$ 光滑延拓，当且仅当其真实通量满足

$$
\boxed{\mathcal F(x_0)=0.}                                \tag{20}
$$

更精确地，在 (20) 下，任意指定 $u(x_0)$ 都给一个唯一局部光滑解；没有额外的高阶 jet 相容条件。

证明：必要性由 (19) 的原通量 $A(pu'-qu)$ 在 $x_0$ 为零。充分性用 Hadamard 引理：

$$
A=(x-x_0)a_1(x),\qquad
\mathcal F=(x-x_0)f_1(x),\qquad a_1(x_0)\ne0.
$$

两商函数都光滑，因此 $\mathcal F/A=f_1/a_1$ 光滑。求解真正正则的一阶式

$$
pu'-qu=\frac{\mathcal F}{A},\qquad
u'=\frac qp u+\frac{\mathcal F/A}{p}.                       \tag{21}
$$

因为 p 在该邻域不为零，它对任意初值给光滑唯一解。求导 (19)，再用 $\mathscr M p=0$，得到
$p(\mathscr M u-v)=0$，故原二阶式也成立，包括 $x_0$。

若已有左侧解，它在该邻域同样满足这个系数光滑的一阶式，故具有唯一光滑延拓。这里没有给发散积分取有限部分。

须再次区分 p 的零与 A 的零：若 $p(x_0)=0$、$q(x_0)\ne0$，则
$A(x_0)=-2q(x_0)^2\ne0$，原二阶 ODE 完全正则；(21) 此时不适用，却不产生任何新增相容条件。事实上 A 的简单零点自动排除 $p=0$：若同时 $p=0$、$A=0$，则 q=0，继而 $A'=0$。

## 6. 有限个内部简单零点的完整有限判据

定理一还可扩到一个准确而有限的退化类。设

- $A(a)A(b)\ne0$；
- J 内的全部零点恰为有限个 $a<x_1<\cdots<x_m<b$；
- 每个零点都是简单零点。

对于 $v\in C_c^\infty((a,b))$，首先检查 m 个准确通量条件

$$
\boxed{\mathcal F_i(v):=\int_a^{x_i}p(t)v(t)\,dt=0,
\qquad i=1,\ldots,m.}                                    \tag{22}
$$

从 $u(a)=u'(a)=0$ 出发，在每个正则区间解原二阶式，在每个零点按第 5 节延拓。式 (22) 成立时，这一有限递推产生唯一全 J 光滑解 $u_v$；不成立时，没有具有该零左数据的光滑解。

此结论是归纳的：由 (19)，当前真实通量始终是
$\int_a^xpv$，所以每个零点使用的是同一个原积分，不重新指定积分常数。第 5 节保证每次跨越存在、唯一且光滑。p 在正则区间内部过零时只用原二阶式，不使用 $u/p$ 表示。

在 (22) 的共同核上，$v\mapsto u_v$ 是线性连续映射。Hadamard 除法可显式写成
$f_1(x)=\int_0^1\mathcal F'(x_i+t(x-x_i))\,dt$；固定有限个邻域后，其光滑依赖和连续性均由这条积分式及正则 ODE 给出。

**定理二。** 对 $G\in\mathcal G_J$，存在 $w\in\mathcal D_J$ 满足 $L_f(w)=G$，当且仅当 $v=G''$ 先通过 (22)，其唯一延拓解再通过

$$
\boxed{
u_v(b)=0,\quad A(b)u_v'(b)=0,\qquad
\int_a^b\kappa u_v=0\quad(\kappa\text{ 为 (12) 的七项}).
}                                                            \tag{23}
$$

仍按 (17) 恢复唯一 w。由于 v 在 b 邻域为零且 $A(b)\ne0$，前两项迫 u 在右邻域恒零；左邻域亦为零。其余证明与定理一完全相同。

(22)–(23) 是依次定义的有限准确线性系统，条件数至多 $m+9$；后九项是前 m 项共同核上的线性泛函。没有预设这些条件独立。正则情形 $m=0$ 的两个终端泛函正好等价于显式 adjoint 矩 (11)。

本节不处理平端支撑边界的无限阶 A 零点、高重数零点、无穷多个退化点或零点区间。这些情形不能由“局部二阶方程只有两个常数”冒称为同样有限。若 f 在开平台恒值，则 $\mathscr M=0$，目标须在那里满足 $G''=0$；平台上的额外核也不包含在本节正则/简单零点唯一性结论中。

## 7. 已付 pure 的真实闭 hook：只剩两个目标函数

现固定 R180/R210 的一个真实闭 hook，满足

$$
M=0,\qquad T=\kappa\mathfrak H,\qquad \kappa\ne0,
$$

并固定已完整付清二、三阶 range 的同一实非退化圆。假设整个 canonical pure 第四周期已经准确为零。

原 canonical 第四周期只有 $0,\pm2,\pm4$ 相位谐波，并在 $\theta=0,\pi$ 为零。故令
$G_\theta=-V^0_\theta/(2\kappa)$ 后，准确存在两个实函数 $G_c,G_s$，使

$$
\boxed{G_\theta=(1-\cos2\theta)G_c+\sin2\theta\,G_s.}     \tag{24}
$$

这一步用的是真实整 pure 零，不是某个有限查询或幂尾投影为零。

若这两个目标都属于同一个 $\mathcal G_J$，并分别通过定理一或定理二的有限条件，取

$$
w_c=\mathcal R_JG_c,\qquad w_s=\mathcal R_JG_s,
$$

$$
\boxed{w_\theta=(1-\cos2\theta)w_c+\sin2\theta\,w_s.}     \tag{25}
$$

R184 的准确传递为

$$
\Delta V_\theta=2\kappa L_f(w_\theta).
$$

于是 (25) 使整个 I、全部相位上的完整第四周期为零，同时保 $w_0=w_\pi=0$、原目标和已经付清的 pure。六交叉矩保证第三补偿
$2Z_B(\phi_\theta,w_\theta)$ 仍周期、双 collar。没有重新选择 f、g、几何或右锚。

对于所限定的 $w_\theta\in\mathcal D_J$，这些条件也必要：$L_f$ 在该局部类中单射，(24) 的两个 Fourier 分量必须分别具有所述右逆；任何额外谐波的 gauge 系数在核内，只能为零。

因此本稿给出一个真正的固定目标局部 period 充分入口。它没有评价某一已构造闭 hook 的实际 $G_c,G_s$，也没有证明其二阶导数已经支撑在合适的 J。若这些支撑或有限条件失败，仍可能存在 J 外的全局 gauge；不能由此排除所有固定圆构造。

## 8. 同一个所得 gauge 的 joint 剩余项

在 (25) 已定后，令 R184 的真实 ruling 线性算子为 $\mathcal B_\theta$，原 ruling 为 $K^0_\theta$，固定三矩几何空间为 $\mathcal W$。剩余条件准确是

$$
\boxed{
K^0_\theta+\mathcal B_\theta(w_\theta)\in\mathcal W
\quad\text{作为整个 }s\text{ 函数，对全部 }\theta.
}                                                            \tag{26}
$$

这不是另一个可随意重选 w 的问题。在本局部类中 w 已由周期目标唯一确定；若 (26) 成立，R184 的单 profile 三矩右逆会用一个光滑周期的第三齐次家族支付剩余 ruling，包括未删掉的 gauge 平方项。于是得到本局部 gauge 类内的完整第四校正。

若 (26) 不成立，可再研究全局 period 核中的其他合法方向，但不得更改 (25) 后只保局部周期近似。本文没有宣称 (26) 已成立，也没有以有限条件的个数推出这些 ruling 方向独立或满射。

本稿保留特殊固定 profile 问题的本来范围：这是同一真实几何、同一目标、同一圆的准确线性 range 分析；没有把 universal 成本字符搬成该圆上的新障碍，也没有把完整 pure 已可支付扩大成 mixed/ruling 已可支付。
