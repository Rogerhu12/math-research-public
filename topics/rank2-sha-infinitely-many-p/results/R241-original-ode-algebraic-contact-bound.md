# R241 — 原径向 ODE 对低次原因子的有效接触界

日期：2026-11-13。**状态：已证明。** 本篇将原径向微分方程实际用于 R238 的高接触因子，得到有限次数的明确上界，并排除一个完整的低次核范围。没有从双完整中央零构造深关系；主目标未完成。

以下一律使用原 $A,C=B-A$，同一个第一带前缀，以及原图 $\phi$。参数和 theta 单位均保留原初值。

## 1. 原 theta 单位与不能延拓的模 p 方程

取 $p=4r-1\ge19$。R224 的原有理参数 $s$ 给
$$
A=\Pi(s)Y(s),\qquad C=\Pi(s)\mathcal Z(s)Y(s),
\qquad Y=e^\Lambda,\quad Y(0)=1,
\tag{1}
$$
其中 $\Pi=s+O(s^2)$、$\mathcal Z=-22s+O(s^2)$。它们准确为
$$
\begin{aligned}
H_1&=1+4s+70s^2+4s^3+s^4,\\
H_2&=1+20s-26s^2+20s^3+s^4,\\
Q_8&=1+364s^2-1088s^3+1190s^4-1088s^5+364s^6+s^8,\\
\Pi&=\frac15s(1-s)^2(1+s)
 (1-2s+5s^2)(5-2s+s^2)H_1H_2,\\
\mathcal Z&=\frac{(1+s)Q_8}{(1-s)H_1H_2}-1.
\end{aligned}
\tag{2}
$$
直接取消 (2) 中的因子可见：$\Pi$ 与 $\Pi\mathcal Z$ 都是次数十六的多项式，系数在 $\mathbf Z[1/5]$ 中。特别原有限源没有在本篇变成任意的有理系数族。

原方程为
$$
4s(1-s)\Lambda''+(3-5s)\Lambda'=17,
\qquad \Lambda'(0)=17/3.
\tag{3}
$$
设 $\Lambda'=\sum a_ns^n$，则
$$
a_0=17/3,\qquad
(4n+3)a_n=(4n+1)a_{n-1}\quad(n\ge1).
\tag{4}
$$
故 $a_0,\ldots,a_{r-2}$ 都是 $p$ 单位；$Y$ 的 $s^n$ 系数在 $0\le n<r$ 都 $p$ 整。这里积分和指数所需的整数不超过 $r-1<p$，也都是单位。

**共振引理。** 在 $\mathbf F_p[[s]]$ 中，没有任何单位 $Y_*(s)$ 满足
$$
\mathscr D(Y_*):=
4s(1-s)(Y_*Y_*''-(Y_*')^2)
 +(3-5s)Y_*Y_*'-17Y_*^2=0.
\tag{5}
$$

**证明。** 若有这样的单位，令 $\Omega=Y_*'/Y_*\in\mathbf F_p[[s]]$。由 (5)
$$
4s(1-s)\Omega'+(3-5s)\Omega=17.
$$
常数项已经强制 $\Omega_0=17/3$；这个初值不是另行加给一个未知分支的假设。其余系数满足 (4)。在 $n=r-1$ 处，左系数 $4n+3=p=0$，而右侧是
$$
(p-2)\Omega_{r-2}=-2\Omega_{r-2}\ne0.
$$
矛盾。因而 (5) 甚至对任意非零常数项的单位都无解，尤其对本篇 $Y_*(0)=1$ 的分支无解。$\square$

这个结论并不否认原特征零解；它的第一个相应系数具有真实 $p$ 分母。原 $Y$ 的整截断
$$
Y_{<r}=[Y]_{<r}\bmod p
$$
仍满足 $\mathscr D(Y_{<r})\in s^{r-1}\mathbf F_p[[s]]$，因为低于 $r-1$ 的每个方程只读取原 $Y$ 的前 $r$ 个整系数。

## 2. 原高接触因子给一个确定的正规代数分支

继续用原图
$$
\phi(A)=c(f^{-1}(A))=-22A^2+O(A^3)
\quad\text{在 }\mathbf F_p[[A]]\text{ 中}.
$$
该图与原特征零曲线的整截断在 $A$ 次数小于 $r$ 时相同，这是 R196 的第一带轴式；不在更高次数使用这个等同。

设 $d\ge3$、$d<p$，且有依赖 $C$ 的不可约 $F\in\mathbf F_p[A,C]$，满足
$$
e=\deg F\le d/2,\qquad
h=v_\phi(F)>e(d-1).
\tag{6}
$$
R238 的 resultant 论证给
$$
\mu=v_\phi(F_C)\le e(e-1),
\qquad h>2\mu.
\tag{7}
$$
若 $h<+\infty$，完备离散赋值环 $\mathbf F_p[[A]]$ 中的 Newton–Hensel 迭代产生一个根
$$
F(A,\psi(A))=0,\qquad
\operatorname{ord}_A(\psi-\phi)=h-\mu=:L.
\tag{8}
$$
它在 $\operatorname{ord}_A(\psi-\phi)>\mu$ 的球中唯一。简要证明：第一步修正为 $-F/F_C$，阶恰为 $h-\mu>\mu$；Taylor 余项阶至少 $2(h-\mu)>h$，后续修正严格更深。迭代收敛且第一步最低项不被改变。两个此球中的根相减，再用 $F_C$ 的首项，给唯一性。

若 $h=+\infty$，取 $\psi=\phi$、$L=+\infty$。所有系数仍在 $\mathbf F_p$，没有引入未控制的常数域扩张。

由 (6)—(7)，
$$
L>e(d-e)\ge2.
\tag{9}
$$
因此 $\psi=-22A^2+O(A^3)$。置 $v_0=-22$，则
$$
u_\psi(A)=\frac{\psi(A)}{v_0A}=A+O(A^2)
$$
是严格参数。令 $a_\psi(u)$ 为其逆，并定义
$$
q(s)=\frac{\mathcal Z(s)}{v_0}=s+O(s^2),\qquad
Y_\psi(s)=\frac{a_\psi(q(s))}{\Pi(s)}.
\tag{10}
$$
分子、分母都有一次零，首系数都是一，故
$$
Y_\psi\in1+s\mathbf F_p[[s]].
\tag{11}
$$
而且由定义
$$
F(\Pi(s)Y_\psi(s),\Pi(s)\mathcal Z(s)Y_\psi(s))=0.
\tag{12}
$$
这是原多项式因子给出的实际分支，不是自由选择的 ODE 解。

## 3. 与原 theta 的准确截断比较

令
$$
K=\min(L,r).
$$
原图只在 $A^r$ 之前与实际曲线等同；(8) 因而给
$$
\psi(A)-C(A)=O(A^K)
\tag{13}
$$
在这个共同的整截断中成立。将 (13) 除以 $v_0A$，再用严格逆参数，损失一阶；最后在 (10) 除以 $\Pi(s)$，再损失一阶。于是准确有
$$
Y_\psi(s)-Y_{<r}(s)\in s^{K-2}\mathbf F_p[[s]].
\tag{14}
$$
可以直接核对：把原 $A(s)$ 代入 $u_\psi$，与原 $q(s)=C(s)/(v_0A(s))$ 的差为 $O(s^{K-1})$，所以
$a_\psi(q(s))-A(s)=O(s^{K-1})$；再除首阶为一的 $\Pi$ 得 (14)。

(5) 的二阶导数项带因子 $s$，所以把一个单位改变 $O(s^M)$，其 $\mathscr D$ 值只可能从 $s^{M-1}$ 起改变。因此 (14) 与 §1 的原截断方程给
$$
\mathscr D(Y_\psi)\in s^{K-3}\mathbf F_p[[s]].
\tag{15}
$$
这里 $K\ge3$；没有把两次除以参数的损失省掉。

## 4. 有限次数的 resultant 上界

由 (2)、(12)，$Y_\psi$ 满足一个非零多项式关系，分别对 $s,Y$ 的次数至多 $(16e,e)$。取其中在该分支上为零的一个不可约因子 $H(s,Y)$，并记
$$
a=\deg_s H\le16e,\qquad b=\deg_Y H\le e<p.
\tag{16}
$$
有 $b\ge1$，且 $H_Y\ne0$。不可约性和 $b<p$ 保证关于 $Y$ 的可分性；因而 $H_Y(s,Y_\psi)$ 是非零形式级数，允许在分式域中作隐式微分。

令 $D=H_Y$。将 $Y'=-H_s/D$ 和二阶隐式微分代入 (5)，清去 $D^3$，得到多项式
$$
\begin{aligned}
\mathcal K(s,Y)={}&4s(1-s)\bigl[
Y(-H_{ss}D^2+2H_{sY}H_sD-H_{YY}H_s^2)
-H_s^2D\bigr]\\
&-(3-5s)YH_sD^2-17Y^2D^3.
\end{aligned}
\tag{17}
$$
它准确满足
$$
\mathcal K(s,Y_\psi)=H_Y(s,Y_\psi)^3\,\mathscr D(Y_\psi).
\tag{18}
$$
逐项看 (17)，
$$
\deg_s\mathcal K\le3a,\qquad
\deg_Y\mathcal K\le3b-1.
\tag{19}
$$
常数或低次数的导数为零时只会降低次数。

共振引理与 (11) 保证 $\mathscr D(Y_\psi)\ne0$。因此 $H$ 不整除 $\mathcal K$，其非零 resultant
$$
R(s)=\operatorname{Res}_Y(H,\mathcal K)
$$
满足
$$
\deg R\le b(3a)+a(3b-1)=a(6b-1).
\tag{20}
$$
同一 Sylvester 构造给无分母的 $R=UH+V\mathcal K$，$U,V\in\mathbf F_p[s,Y]$。代入正规分支后，$V(s,Y_\psi)$ 为整形式级数，所以
$$
\operatorname{ord}_s\mathcal K(s,Y_\psi)
\le\operatorname{ord}_s R\le\deg R.
$$
结合 (15)、(18)—(20)，得到本篇的有效接触界
$$
\boxed{\quad
\min(h-\mu,r)\le a(6b-1)+3
\le16e(6e-1)+3.
\quad}
\tag{21}
$$
这个界使用了原 ODE 的实际非零共振。只凭形式因子或模 $p$ 维数计数不能得到 (21)。它也保留了隐式导数可能在原点消失的情况：$H_Y$ 的三次因子只增加左侧消失阶，未被当成单位删除。

## 5. 一个完整的原低次核排除范围

沿用 R238 的
$$
k=rq+s,\quad 0\le s<r,\quad q\le p-2,
\qquad V_d=\ker(j_{k,1}|_{E_d\bmod p}).
$$

**定理。** 若 $d<p$ 且
$$
q\ge97,\qquad r-2(q-1)>d(d-1),
\tag{22}
$$
则
$$
\boxed{V_d=0.}
\tag{23}
$$

**证明。** 若 $V_d\ne0$，R238 给一个满足 (6) 的原共同因子，且 $qe\le d$。特别 $d\ge q\ge97$，所以 §2 的 $d\ge3$ 条件自动满足。

先比较两个具体界。由 (22) 和 $d\ge qe$，
$$
\begin{aligned}
r&>d(d-1)+2(q-1)\\
&\ge q^2e^2-qe+2q-2
>96e^2-16e+3.
\end{aligned}
\tag{24}
$$
最后一个严格不等式对所有 $q\ge97,e\ge1$ 成立；两边之差为
$(q^2-96)e^2+(16-q)e+2q-5>0$。
所以 (21) 的 $r$ 选项不能实现最小值，必有
$$
h-\mu\le96e^2-16e+3.
\tag{25}
$$
另一方面，(6)—(7) 与 $d\ge qe$ 给
$$
h-\mu>e(d-e)\ge(q-1)e^2\ge96e^2.
$$
这与 (25) 矛盾，因为 $-16e+3<0$。$\square$

若不满足 (22)，仍可在找到实际低次候选因子后使用 (21)，而不必把所有 $q$ 混在一起。比如一旦 $r>16e(6e-1)+3$，该因子的实际接触就必须满足
$h-\mu\le16e(6e-1)+3$。

## 6. 与主目标的边界

这里支付的是原 ODE 对低次关系的一个真实限制。它没有给出 R223 所需的 primitive 深关系或正比例深 Smith；相反，(23) 排除了其中一个候选范围。条件 (22) 也不覆盖重要的 $q=2$ 带。

因此接下来的主任务仍是在 $q=2$ 等实际带上计算 R238 的同一前缀首次障碍 $\omega_G$，并研究双完整中央零是否给其真实核。不能把本篇的代数分支、接触上界或共振障碍当成已经获得了无穷多个好素数。

依赖：R196 的原图与第一带截断；R224 的原参数、$\Pi,\mathcal Z$ 及仿射径向 ODE；R238 的唯一高接触因子、准确导数接触与首次提升。本文所用 Hensel 迭代、次数界和共振矛盾均已在正文证明。
