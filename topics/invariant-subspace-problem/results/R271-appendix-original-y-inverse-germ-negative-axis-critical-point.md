# 原 Y 逆芽的首负轴临界点与同一领先半径障碍

日期：2026-11-15。作者：literature_audit / 789f。

**状态：已证明。** 本文单独处理原 $Y$ 有理函数，不将 $N$ 模型的导数恒等式直接用于 $Y$。两模型共用真实权参数，仅以最高位定义一个比较半径。证明原 $Y$ 逆芽也不能拥有领先指数小于 $(25/2)d^3$ 的完整复圆盘。它不改变已付的安全下界，不估计原 Green 列或回返费用。

## 1. 原函数与比较尺度

取 $m\ge10$、$d=2^m$、$q=d/2$，并令
$$
b_i=(i+1)^{-2},\quad
d_i=e^{-\Lambda_i},\quad
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i.
$$
特别 $d_0=e^{-20}$，记 $\beta=d_0^{-1}=e^{20}$。原有限 $Y$ 函数是
$$
F_Y(z)=\sum_{i=0}^{m-1}
b_i\frac{z^{2^i}}{d_i+z^{2^i}},
\qquad F_Y'(0)=\beta.
\tag{1.1}
$$
令 $\psi_Y$ 为其在零点的原解析逆芽，$\mathcal R_Y$ 为该逆芽的 Taylor 收敛半径。

与
[原 $N$ 首临界点证明](R271-appendix-original-n-inverse-germ-first-negative-critical-point.md)
使用同一个最高位比较数
$$
r_*=
\left(\frac{d_{m-1}}{d_0 q b_{m-1}}\right)^{1/(q-1)},
\qquad R=2r_*.
\tag{1.2}
$$
故
$$
q b_{m-1}\frac{r_*^{q-1}}{d_{m-1}}=\beta.
\tag{1.3}
$$
本文将证明
$$
\boxed{\mathcal R_Y<4\beta r_*.}
\tag{1.4}
$$
无需预设 $Y$ 的首临界点与 $N$ 的首临界点相同。

## 2. 比较区间内全部分母保持远离零

直接代入最高位权给
$$
-\log r_*
=\frac{\Lambda_{m-1}+\log(q/m^2)-20}{q-1}.
\tag{2.1}
$$
准确多项式除法为
$$
\frac{\Lambda_{m-1}}{q-1}
=\frac{25}{2}d^3-\frac54d^2-\frac52d+150m-130
+\frac{300m-260}{d-2}.
\tag{2.2}
$$
$m\ge10$ 时 $q/m^2\ge1$，且
$$
\frac{25}{2}d^3-\frac54d^2-\frac52d-130-\frac{20}{q-1}
\ge12d^3.
$$
所以
$$
r_*\le e^{-12d^3},\qquad R\le2e^{-12d^3}.
\tag{2.3}
$$
置 $\eta=e^{-11d^3}$。最低位有
$$
R/d_0\le2e^{20-12d^3}\le\eta.
\tag{2.4}
$$
最高位由 (1.3) 得
$$
\frac{R^q}{d_{m-1}}
=\frac{2^q\beta r_*}{q b_{m-1}}
\le2^qe^{20-12d^3}\le\eta,
\tag{2.5}
$$
其中用了 $q b_{m-1}=q/m^2\ge1$ 及 $q\log2+20\le d^3$。

若 $1\le i\le m-2$，记 $q_i=2^i\le d/4$。由
$\Lambda_i\le100q_i^4\le(25/16)d^3q_i$ 和
$\log R\le-11d^3$，
$$
\log\frac{R^{q_i}}{d_i}
\le-\frac{151}{16}d^3q_i
\le-11d^3.
\tag{2.6}
$$
故对所有 $0\le r\le R$，
$$
r/d_0\le\eta,\qquad
r^{2^i}/d_i\le\eta\quad(1\le i<m).
\tag{2.7}
$$
特别 $\eta<1/4$，原 $Y$ 函数在整段 $[-R,0]$ 的邻域内解析。最低位的分母是 $d_0-r>0$，其他位的分母是
$d_i+r^{2^i}>0$；这里没有越过有理函数的极点。

## 3. 原负轴分支确实遇到临界点

对 $r\in[0,R]$，真实导数为
$$
F_Y'(-r)
=\frac{\beta}{(1-r/d_0)^2}
-\sum_{i=1}^{m-1}
\frac{2^i b_i r^{2^i-1}/d_i}
{(1+r^{2^i}/d_i)^2}.
\tag{3.1}
$$
注意最低位的符号、分母和其余偶次位不同。

在 $r=R$，(2.7) 给最低项至多 $2\beta$。最高位的负项由
(1.3) 给出
$$
\frac{q b_{m-1}R^{q-1}/d_{m-1}}
{(1+R^q/d_{m-1})^2}
\ge\frac{\beta2^{q-1}}{(1+\eta)^2}
\ge\beta2^{q-2}.
$$
其余负项可以全部保留或仅删去作上界。因此
$$
F_Y'(-R)\le2\beta-\beta2^{q-2}<0.
\tag{3.2}
$$
另一方面 $F_Y'(0)=\beta>0$。令 $r_c$ 是连续函数
$r\mapsto F_Y'(-r)$ 在 $(0,R)$ 的第一个零点。它满足
$$
0<r_c<R,\qquad F_Y'(-r)>0\quad(0\le r<r_c).
\tag{3.3}
$$
无需证明区间外临界点的数目，也不需要假定这个零点是单零。

置 $w_c=F_Y(-r_c)$。由 (3.3)，$r\mapsto F_Y(-r)$ 从零严格递减至
$w_c$，所以 $w_c<0$。原函数本身又给
$$
F_Y(-r)
=-\frac{r}{d_0-r}
+\sum_{i=1}^{m-1}b_i\frac{r^{2^i}}{d_i+r^{2^i}}.
$$
后面的和非负，故
$$
0<|w_c|
\le\frac{r_c}{d_0-r_c}
\le2\beta r_c
<4\beta r_*.
\tag{3.4}
$$

## 4. 这是零点原逆芽的障碍

假设 $\mathcal R_Y>|w_c|$。那么原逆芽在包含线段
$[w_c,0]$ 的一个复邻域内解析。由于 (3.3) 且区间内没有极点，从零点出发的逆函数沿负轴唯一延拓，并满足
$$
\psi_Y(F_Y(-r))=-r\qquad(0\le r<r_c).
$$
取极限得 $\psi_Y(w_c)=-r_c$。在 $w_c$ 的邻域中继续原恒等式
$F_Y(\psi_Y(w))=w$，其导数给
$$
F_Y'(-r_c)\psi_Y'(w_c)=1,
$$
与 $F_Y'(-r_c)=0$ 矛盾。因此
$$
\mathcal R_Y\le|w_c|<4\beta r_*,
$$
证明 (1.4)。这个论证识别的是原零点分支，不是仅找到某个与原分支无关的临界值。

## 5. 对领先指数的准确结论

由 (1.4)、(2.1)–(2.2)，
$$
-\log\mathcal R_Y
>
\frac{25}{2}d^3-\frac54d^2-\frac52d
+150m-130+\frac{300m-260}{d-2}
+\frac{\log(q/m^2)-20}{q-1}
-20-\log4.
\tag{5.1}
$$
特别
$$
-\log\mathcal R_Y
\ge\frac{25}{2}d^3-\frac54d^2+O(d+m)
$$
作为下界的渐近表述成立。因而，对任何固定 $c<25/2$，
充分大的 $m$ 不可能让原 $Y$ 逆芽解析于整个
$|w|\le e^{-cd^3}$ 圆盘。输入尺度与输出尺度之间固定的 $d_0$ 因子不改变这个领先系数。

这与
[二阶安全半径增益](R271-appendix-inverse-germ-second-order-radius-gain-and-same-window-budget.md)
相容：后者是保原误差 $\varepsilon_m=e^{-d^3/4}$ 的实际安全下界，
本文是首负轴临界点给出的上界。两者都不提供尚缺的原强块 Green 逆列、普通右费用或 $N=M$ 结论。
