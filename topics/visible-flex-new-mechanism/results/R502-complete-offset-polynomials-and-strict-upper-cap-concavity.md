# R502 — 固定真实凹图的完整 offset 多项式与高端区间的严格凹性

日期：2026-11-16。**只作原式纸面推导；没有执行新的积分、符号、求根、profile、rank、开发或科学任务。**原 cap15、三原子和四原子账户保持闭合。

本稿支付一个对固定真实凹图的完整符号结论。若只改变原紧化中的非负常数尾 $C$，则
$$
I(C):=\frac{\operatorname{Im}E(C)}{\sqrt{B+2C}},
\qquad B=\int_0^1(R')^2\,dr,
$$
是一个真实三次多项式，而且
$$
\boxed{
I''(C)<0\quad\text{只要}\quad C\ge0,\ B+2C\ge1.
}
$$
因此在当前端高度 $H\ge1$ 的 offset 区间，虚部零点有严格的至多两根分类。若固定图本身 $B\ge1$，此结论覆盖全部 $C\ge0$。

凹性不意味着最多一根，也不意味着完整复余量不能为零。原实部仍须在同一个候选 $C$ 上检验。本稿给出它的完整四次多项式表达及首项 $C^4/5$，不把这一项当成有限 $C$ 的符号证明。

## 1. 固定图与真正变化的量

采用 [R495](R495-complete-concave-cap-graph-and-one-sided-first-atom-collapse.md)、[R496](R496-monotone-complete-cap-phase-and-the-strict-H-ge-two-obstruction.md) 和 [R499](R499-complete-cap-weighted-comparison-and-improved-end-height-obstruction.md) 的同一原凹图。
$$
R(0)=R(1)=0,\qquad R>0,\qquad d=R'\ \text{递减},\qquad d(1)=-1.
$$
记
$$
p=R-rd,\qquad p(1)=1,\qquad
0\le p'\le\frac{3p}{r},\qquad p\ge r^3.
\tag{1}
$$
所有函数属于原允许范围或其已付弱曲率紧化。特别地，曲率原子对应的线性 $R$ 段保留在整个积分区间内。左侧正斜率可以无界；本稿不使用全域 $|d|\le1$。

一次固定整个 $R,d$，令
$$
B=\int_0^1d^2\,dr,\qquad L(r)=1-r,\qquad C\ge0.
$$
实际变化量准确为
$$
y_C=B+2C,\qquad b_C=\sqrt{y_C},\qquad
H_C=\frac{1+B}{2}+C,
$$
$$
A_0(r)=\frac12\int_0^r(d^2-B)\,ds,\qquad
A_C=A_0+CL,
$$
$$
U_0=A_0-Rd+\frac r2(d^2+B),\qquad U_C=U_0+C,
$$
$$
W_C=d^2+y_C,\qquad Z_C=A_C-i b_C R .
\tag{2}
$$
$U_C=U_0+C$ 与 $A_C=A_0+C(1-r)$ 不可互换。两者的差别正是完整端归一和 $b_C$ 的真实变化。

原完整积分仍是
$$
\boxed{
E(C)=\frac12\int_0^1Z_C^3(4U_C-3Z_C)\,dr.
}
\tag{3}
$$
这是同一个 cap 的真实原式，不是只取其某一段、某个 $A_j$ 或 principal 部分。由原 Af 比较，$B\ge1/5$，所以 $b_C>0$。

在真正有限平端类别中，$C=0$；$C>0$ 是保留完整原积分的远左微小尾紧化参数。它不能被当成免费修改一个旧冻结 cap 的自由常数。本稿的必要条件在较大的原紧化类上成立，因此也约束真正允许 cap。

## 2. 完整虚部恰为一个三次多项式乘正因子

原 R496/R499 身份给
$$
\boxed{
I(C)=\frac{\operatorname{Im}E(C)}{b_C}
=\int_0^1R\,W_C
\{r\,y_CR^2-3rA_C^2-2A_CR^2\}\,dr.
}
\tag{4}
$$
定义以下固定图上的真实函数：
$$
\begin{aligned}
Q_0&=rBR^2-3rA_0^2-2A_0R^2,\\
Q_1&=2(2r-1)R^2-6rL A_0,\\
Q_2&=-3rL^2,\qquad W_0=d^2+B.
\end{aligned}
$$
因为
$$
r\,y_CR^2-3rA_C^2-2A_CR^2
=Q_0+C Q_1+C^2Q_2,
$$
所以
$$
\boxed{
I(C)=I_0+I_1C+I_2C^2+I_3C^3,
}
\tag{5}
$$
其全部系数为
$$
\begin{aligned}
I_0&=\int R W_0Q_0\,dr,\\
I_1&=\int R(2Q_0+W_0Q_1)\,dr,\\
I_2&=\int R(2Q_1+W_0Q_2)\,dr,\\
I_3&=2\int RQ_2\,dr
=\boxed{-6\int_0^1r(1-r)^2R\,dr<0}.
\end{aligned}
\tag{6}
$$
这里没有重新作数值积分；(5)(6)只是原(4)的逐项参数展开。

尤其
$$
\boxed{
I'''(C)=-36\int_0^1r(1-r)^2R\,dr<0.
}
\tag{7}
$$
但(7)单独不能把 $I''(0)$ 判为负。本稿下一节用真实 Af 约束支付所需范围，而不从负首项猜整个三次式凹。

也须区分：被证明严格凹的是 $I(C)=\operatorname{Im}E(C)/b_C$。
$\operatorname{Im}E(C)$ 另有随 $C$ 改变的正平方根因子；本稿没有声称它本身是三次多项式或严格凹函数。两者零点准确相同。

## 3. 真实二阶导数的当前状态表达

由(5)(6)，或者直接对(4)微分两次，得到
$$
\boxed{
\frac12 I''(C)
=\int_0^1 R
\left\{
-3rL^2(d^2+y_C)
+4(2r-1)R^2
-12rL A_C
\right\}\,dr.
}
\tag{8}
$$
例如 $I_2$ 是(8)在 $C=0$ 的值；替换
$y_C=B+2C$、$A_C=A_0+CL$ 后，新线性项准确为
$-18C\int rL^2R=3I_3C$。原 $C$ 的两个来源都保留。

R496 的端势比较在当前 $C$ 上仍给
$$
\boxed{
A_C\ge\frac{y_C-1}{2}R.
}
\tag{9}
$$
其证明保 $A_C(0)=C\ge0$：
令 $Y=A_C-(y_C-1)R/2$，则
$$
Y(0)=C,\quad Y(1)=0,\quad
2Y'=(d+1)(d-y_C).
$$
$d$ 递减且 $d+1\ge0$，所以 $Y'$ 至多由正转负，两端非负推出(9)。

以下只限当前 $y_C\ge1$，因而 $A_C\ge0$。
同时凹图在右端的切线给
$$
0<R\le1-r=L.
\tag{10}
$$

## 4. $H_C\ge1$ 区间的严格凹性

把(8)大括号记为 $Q_C(r)$。

当 $0<r\le1/2$ 时，
$$
4(2r-1)R^2\le0,\qquad -12rL A_C\le0,
$$
而第一项严格为负，所以 $Q_C(r)<0$。

当 $1/2<r<1$ 时，由(9)(10)，
$$
\begin{aligned}
Q_C(r)
&\le-3rL^2(d^2+y_C)+4(2r-1)L^2\\
&=rL^2\left\{5-\frac4r-3d^2-3(y_C-1)\right\}\\
&\le rL^2\left\{5-\frac4r-3d^2\right\}.
\end{aligned}
\tag{11}
$$
对 $1/2<r\le4/5$，最后的大括号非正。

剩下 $4/5\le r<1$。此时必须使用真实 Af 的 $p\ge r^3$，而不是再给 $d$ 加一个假上界：
$$
d=\frac Rr-\frac pr
\le\frac{1-r}{r}-r^2
=-\left(r^2+1-\frac1r\right)<0.
\tag{12}
$$
故
$$
5-\frac4r-3d^2
\le-\frac{P(r)}{r^2},
$$
其中
$$
\begin{aligned}
P(r)
&=3(r^3+r-1)^2-5r^2+4r\\
&=3r^6+6r^4-6r^3-2r^2-2r+3.
\end{aligned}
\tag{13}
$$
这个多项式在 $[4/5,1]$ 严格为正。完全有理的检查为
$$
P(4/5)=\frac{4563}{15625}>0,
$$
以及
$$
\begin{aligned}
P'(r)
&=18r^5+6r^2(4r-3)-4r-2\\
&\ge18(4/5)^5+6(4/5)^2(1/5)-6\\
&=\frac{2082}{3125}>0 .
\end{aligned}
\tag{14}
$$
所以(11)在该末段也严格为负。

合并三段，$Q_C\le0$ 几乎处处，且在一个非空开区间严格为负。因 $R>0$，(8)得到
$$
\boxed{
C\ge0,\quad y_C=B+2C\ge1
\quad\Longrightarrow\quad I''(C)<0.
}
\tag{15}
$$
等价地，令
$$
C_{\rm hi}=\max\left\{0,\frac{1-B}{2}\right\}.
$$
则 $I$ 在整个 $[C_{\rm hi},\infty)$ 严格凹。若 $B\ge1$，这就是全部 $C\ge0$。若 $B<1$，原低端区间
$0\le C<(1-B)/2$ 尚未由本稿判定凹性。

(12)是本证明与任意凹图的关键区别。仅凭凹性、三次负首项或 $H>3/5$ 不能删掉它。

## 5. 零点分类和原实部仍须满足的条件

由(6)，$I(C)\to-\infty$，$I'(C)\to-\infty$。
结合(15)，在 $[C_{\rm hi},\infty)$：

- $I$ 至多有两个不同零点，不能一般改成“至多一个”。
- 若 $I(C_{\rm hi})>0$，则恰有一个更大的零点；它是简单根，导数严格为负。
- 若 $I(C_{\rm hi})=0$，则根据 $I'(C_{\rm hi})$ 的号，可能没有其它根，或有且仅有一个更大的简单根。
- 若 $I(C_{\rm hi})<0$ 且 $I'(C_{\rm hi})\le0$，则没有该区间的根。若 $I'(C_{\rm hi})>0$，唯一极大值可以为负、零或正，分别对应没有根、一个相切根或两个简单根。

这些是严格凹三次式的完整可能性分类，不选择其中未经证明的一支。

[R499](R499-complete-cap-weighted-comparison-and-improved-end-height-obstruction.md) 已证明
$H_C\ge H_*\Rightarrow\operatorname{Im}E(C)<0$。所以真正可能的虚部根还必须满足
$$
\boxed{
0\le C<H_*-\frac{1+B}{2}.
}
\tag{16}
$$
若右边不正，全部非负 offset 已经排除。
对于 $B<1$，(16)仍可能包括 $H_C<1$ 的低端部分；本稿不把高端凹性搬到那里。

完整实部在同一个固定图上是
$$
\boxed{
\operatorname{Re}E(C)
=\frac12\int_0^1
\left\{
4U_CA_C^3-3A_C^4
+y_CR^2(18A_C^2-12U_CA_C)
-3y_C^2R^4
\right\}\,dr.
}
\tag{17}
$$
它是一个至多四次的真实多项式，其四次项准确为
$$
[C^4]\operatorname{Re}E
=\frac12\int_0^1\{4L^3-3L^4\}\,dr
=\boxed{\frac15}.
\tag{18}
$$
式(17)保原 $U_C,A_C,y_C$ 的全部变化，不只保(18)。

完整 $E(C)=0$ 必须在同一个 $C$ 同时满足(5)和(17)。
严格凹性没有支付这个共同零点问题。正的四次首项也没有判定有限 $C$ 上的实部；尤其不能在一个虚部根处未经证明地宣布实部为正或负。
原完整五门还包含另外三个实条件，不能由某个复零点自动代付。

## 6. 左尾、原子段和实际适用范围

所有积分都在同一个完整 $r\in[0,1]$ 图上。固定图而改变 $C$ 的参数恒等式来自原恢复式(2)，并未换锚。真有限平端只有 $C=0$；紧化中的 $C>0$ 保留远尾的真实常数作用。

弱曲率原子产生的线性 $R$ 段在(4)、(8)、(17)中逐段原样保留。证明只使用(1)、凹图右端切线、有限能量和完整 $A_C$ 的端值，不要求 $d'<0$ 处处成立，也不把任一侧 $r$ 乘一个 Dirac 符号来替代整段积分。

本稿新增支付的是：

1. 原 offset 参数在完整虚部和实部中的三次、四次结构及全部系数入口；
2. 当前 $H_C\ge1$ 范围的严格凹性(15)，包括原 $B<1$ 但 offset 已进入该范围的情况；
3. 该区间中虚部根的准确分类及与 R499 高度必要门的交集。

真正尚欠的是同图上(5)与(17)的共同零点判别，以及其与原全部五门的联立。这里没有把新的必要条件称作完整无解证明，也没有据已闭的有限搜索追加新的起点或计算。
