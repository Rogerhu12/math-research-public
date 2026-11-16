# 原负水平约束对 cubic 原函数格的二次首项截除

日期：2026-11-16。**状态：以下同一全球来源中的首项截除、显式临界值门及退化零纤维的自动情形已证明。完整 $K_1$ 的余像、物理第 $s$ 系数和其它 Bockstein 行仍未判定。**

本注接[原负水平零 charge](2026-11-16-r872-native-primitive-zero-charge-and-negative-horizontal-value.md)、[原零纤维前三层](2026-11-16-r872-native-zero-fiber-three-layer-quotient.md)和[实际 native 配对](2026-11-16-r872-native-primitive-bockstein-value-and-normal-pair.md)。保持这些文献的原 $r=3$、$\tau\in\{1,2,3\}$、$D\ge4b$、$p>D+40$、$T=s-13>3$、同一个 $F$ 与全部十九角。

## 1. 全球零 charge 与局部二次帽必须同时使用

置
$$
L=Y\partial_Y+40,\qquad
\mathscr J_3=L^{-1}(\mathcal W_D\cap F^3k(t)[Y]),
\qquad z_-=C\cdot H_- .
$$
取 $J\in\mathscr J_3$，始终写同一个来源等式
$$
LJ=F^3A.
\tag{1}
$$
原全局负水平结论已经证明
$$
z_-\ge1\quad\Longrightarrow\quad [Y^0]J\equiv0 .
\tag{2}
$$
这不是只说零纤维的一个值为零。

因为原 $F$ 不可约且不是 $Y$，$F(t,0)\not\equiv0$。
在原单项式来源框中取 (1) 的零 charge，准确得到
$$
40[Y^0]J=F(t,0)^3[Y^0]A.
$$
故
$$
\boxed{
z_-\ge1\quad\Longrightarrow\quad [Y^0]A\equiv0 .
}
\tag{3}
$$
这里不需要把 $F(t,0)$ 认成任一边界处的单位：
等式是在同一个函数域中使用其非零性。
原固定 $d(t)$ 因子也没有删除或更换。

另一方面，原零角已经给
$$
A=t^2(a_0+a_1Y)+O(t^3).
$$
所以 (3) 进一步给
$$
\boxed{A=t^2a_1Y+O(t^3).}
\tag{4}
$$
这是实际全球来源的限制；底 DVR 上允许的另一列 $t^2$ 不再是可独立采用的全球方向。

## 2. 一个固定临界值给准确的 t³ 门

只在记录零纤维系数时，将 $F(0,Y)=F_0(Y)$ 规范为 monic。
相应 $t$ 单位同时作用于 $A$，不改变 (3)、(4) 或下述零／非零门。
定义同一原 charge 四十的临界值
$$
\boxed{
v_1(F_0)=\left(L^{-1}(YF_0^3)\right)(1).
}
\tag{5}
$$
若 $F_0^3=\sum_{n=0}^9c_nY^n$，它就是
$$
v_1(F_0)=\sum_{n=0}^9\frac{c_n}{41+n}.
\tag{6}
$$
所有分母都是原单位，因为 $p>211$。

现在再要求 $J\in K_1$。同一个物理分支 $\psi(t)$ 满足 $\psi(0)=1$，
已付值门是 $\operatorname{ord}_tJ(t,\psi(t))\ge T>2$。
由于 (1)、(4) 的 $t^2$ 来源系数恰为
$a_1L^{-1}(YF_0^3)$，准确有
$$
\boxed{a_1\,v_1(F_0)=0.}
\tag{7}
$$
没有给这两个因子分别添加算术条件。

于是得到原全子格上的实际像限制：
$$
\boxed{
z_-\ge1,\quad v_1(F_0)\ne0
\quad\Longrightarrow\quad
A\in t^3,\qquad J\in t^3k[[t]][Y]
\quad\text{对全部 }J\in\mathscr J_3\cap K_1.
}
\tag{8}
$$
后一断言使用 $L^{-1}$ 不改变 $t$ 阶。
它意味着这个原子格不能改变任一修正的完整 $t^1,t^2$ 来源多项式，
不仅仅不能改变某个有限纤维的商值。

为把 (5) 的未知范围写清，设
$$
F_0=(Y-1)(Y^2+\alpha Y+\beta),\qquad
(Y^2+\alpha Y+\beta)^3=\sum_{j=0}^6g_jY^j .
$$
有限四项差分给
$$
\boxed{
v_1(F_0)
=-6\sum_{j=0}^6
\frac{g_j}{(41+j)(42+j)(43+j)(44+j)} .
}
\tag{9}
$$
其中升幂系数依次是
$$
(g_0,\ldots,g_6)=
(\beta^3,\,3\alpha\beta^2,\,
3\beta^2+3\alpha^2\beta,\,
\alpha^3+6\alpha\beta,\,
3\alpha^2+3\beta,\,3\alpha,\,1).
$$
所以可能保留非零二次首项的情形，在 $z_-\ge1$ 下必须落在
这个**明确的非零三次多项式方程**上。
它不是恒等式：例如 $\beta^3$ 的系数为
$-6/(41\cdot42\cdot43\cdot44)\ne0$。
本注没有排除该三次方程在实际 $F_0$ 上成立。

## 3. 退化有限纤维 Y²(Y−1) 的门自动满足

允许原另外两根合并于零：
$$
F_0=Y^2(Y-1).
\tag{10}
$$
原物理根 $1$ 仍然简单。$R_0=(0,0)$ 是原未吹起图中的负水平交点，
故 $F(t,0)$ 在 $t=0$ 消失；由 $C\ne H_-$ 得 $z_-\ge1$。
不要求 $C$ 在 $R_0$ 光滑，也不要求 $t$ 在那里非分歧。

这里 (6) 精确为
$$
\boxed{
v_1=\frac1{50}-\frac3{49}+\frac3{48}-\frac1{47}
=-\frac6{47\cdot48\cdot49\cdot50}\in k^\times .
}
\tag{11}
$$
所以 (8) 对 (10) 的全部真实 $\mathscr J_3\cap K_1$ 自动成立。

这也准确排除一个只在局部 DVR 可见的误用。
确有多项式恒等式
$$
\boxed{
L\bigl(Y^6(Y-1)^4\bigr)
=F_0^3(50Y-46).
}
\tag{12}
$$
左边的 primitive 在整个有限三次纤维上为零，
但右边的余乘子在物理点 $Y=1$ 为 $4$。
若只看局部临界值，会留下一个“值为零而 normal 首值不为零”的二次方向。
然而其 $a_0=-46$ 违反全球 (3)，所以它不可能是本窗口原
$\mathscr J_3\cap K_1$ 的二次首项。
这一步使用真正的全球负水平约束，不是给退化纤维额外赋值。

## 4. 对原 native 行及同 R/S 的准确影响

(8) 下，原四个 Euler 读取加强为
$$
W_1\in w^{3h+3},\qquad
W_2\in w^{2h+3},\qquad
W_3\in w^{h+3}.
\tag{13}
$$
因此对 $\tau=1,2,3$ 全部情形，
$$
\boxed{
\bar\Lambda_0\beta_1(J)
=\frac{5042}{a}[w^s]W_0(J).
}
\tag{14}
$$
特别 $\tau=1$ 原来可能出现的
$9U(0)u(0)^2e_0\alpha_A/a$ 由 (8) 真正消失。
这没有把第 $s$ 值项删掉，也没有把 (14) 当成第一余类全部为零。

同一子格仍满足 $\Pi(J)=0$；在其全部原首 carry 带通过后仍只有
$W_0\in w^s$，不是 $W_0\in w^{s+1}$。
所以固定 $P$ 改 $R$、或固定 $P,R$ 改 $S$ 时，
低来源多项式在 (8) 下保持，但后续 native 页仍沿真实 (14) 改变，
其它 normal 与高 carry 也必须用同一个 $J$ 处理。

当 $v_1(F_0)=0$ 时只保 (3)、(4)、(7)，不能照搬 (8)。
当 $z_-=0$ 时也不能删除另一个二次 primitive 列。
这些界限与原有限纤维商、完整连接核和全 $K_1$ 高前缀相容；
没有从未加前缀的满射推出受限像。

本注仅作完整符号证明，无新增数值运行。
