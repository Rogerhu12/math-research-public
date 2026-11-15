# R782 — 原 r=2 立方因子的常数项刚性、五个角型与完整非齐次接触矩阵

日期：2026-11-15。**状态：本文的真实来源分类与有限存在门已证明；五型矩阵的强接触可解性、原完整首次修正的余 normal 以及主目标仍未完成。**

本文保 R771 的实际非空窗口，进一步使用原来源的常数 charge。其结论不是另一个低阶块：在下述 $m_q=0$ 范围，任一实际强接触因子 $F$ 的 $Y^0$ 系数只能是固定 $d=1+8t$ 的幂；全部其余 Gauss 条件将 $F$ 归一后的来源压成五个显示系数格。每格的强接触问题都是右端固定为 $(-1,0,\ldots,0)$ 的实际 Hermite–Padé 方程。分裂系数域保至多十五个固定 mask，不能自动使用五型。

从旧因子得到这些条件是必要性。每型给出的立方返回也确实属于原 $\mathcal W_{3b}$，但它是一个新的真实候选；不替换已经固定的 $P_2=P^{\rm fact}+pR$，不把原三条中央零赋给归一因子或各显示系数列。

## 1. 原范围、来源及全部角帽

令 $\mathcal O$ 为 $\mathbf Z_p$ 或有限非分歧扩张，剩余域 $k$，保
$$
p=6s-1>101,\qquad f_D<p,\qquad
P^{\rm fact}=qt^2F^3\in\mathcal W_D,
\qquad q=d^{-C_D}Q,
\tag{1}
$$
$$
r=2,\qquad \ell=1,\qquad k_{\rm carry}=0,\qquad
s=2h+2,\qquad b=\deg_YF,\qquad
b_0=\deg_YF(0,Y)=3.
\tag{2}
$$
这里 $k_{\rm carry}$ 是旧 carry 指标，与剩余域 $k$ 区别。$F\in k[t,Y]$ 为原 primitive 不可约因子，
$$
F(0,1)=0,\qquad F_Y(0,1)\ne0,\qquad q(0,1)\ne0.
\tag{3}
$$
原 $F$ 的强接触、几何整性、曲线交数和 R750 的长度门照旧；本文不由线性方程自动推出这些附加性质。

写
$$
h_7=16t^2+4t+7,\qquad d=1+8t,
$$
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^n q_n(t)k[t]_{\le e_{n+1}},\qquad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
\tag{4}
$$
$$
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,\quad
f_n=\left\lfloor\frac{9n}{2}\right\rfloor+4,
$$
$$
e_{n+1}=f_n-3A_n-B_n+C_n.
$$
次数符号 $\le e_{n+1}$ 指实际多项式次数帽。

R491 的双向 Gauss 识别，在保留 $d$ 分母时准确是：$\deg_Y P\le D$、仅有 $d$ 极，并且
$$
\begin{array}{c|c|c}
\text{位置}&v(P=\sum P_nY^n)&\text{下界}\\ \hline
0,\ h_7(\alpha)=0&
\min_n(4\operatorname{ord}_\alpha P_n-n)&-2\\
1&\min_n(3\operatorname{ord}_1P_n-n)&-1\\
d=0&\min_n(2\operatorname{ord}_{d}P_n+n)&0\\
\infty&\min_n(9n-2\deg_tP_n)&-8 .
\end{array}
\tag{5}
$$
对有理系数，$\deg_t$ 是分子次数减分母次数。这些赋值对乘积严格相加；(5) 与全部原 canonical 列及十九角等价，不是只保六个必要测试。

R771 已付在 (1)–(3) 中
$$
m_F=-v_0(F)=3,\qquad m_q=-v_0(q)\in\{0,1\}.
$$
**本文另加且始终保留**
$$
\boxed{m_q=0.}
\tag{6}
$$
例如 $D=3b$ 时 $Q$ 无 $Y$，故 (6) 自动成立。一般 $D>3b$ 不自动如此；$m_q=1$ 不在本文五型必要性的范围。

由 $v_0(q)\ge0$，每个正 charge 系数均被 $t$ 整除，所以
$$
q(0,Y)=q(0,0)\in k^\times,\qquad Q_0(t):=Q(t,0)\ne0,
\qquad Q_0(0)\ne0.
\tag{7}
$$

## 2. 原常数 charge 迫 f0 只在 d 上有零

置 $f_0(t)=F(t,0)$。因 $F$ 不可约且 $F(0,1)=0$，$F$ 不是 $Y$，故 $f_0\ne0$。原 $n=0$ 列恰为 $k[t]_{\le4}$，于是
$$
t^2d^{-C_D}Q_0(t)f_0(t)^3\in k[t]_{\le4}.
\tag{8}
$$
若 $f_0$ 在代数闭包中有一个不在 $d=0$ 的零，则右侧除 $t^2$ 外还含该零的三次因子。若该零就是 $t=0$，总零阶至少为五；若不在 $0$，总次数也至少为五。$Q_0$ 是多项式，唯一分母为 $d^{C_D}$，故没有别处的极可以消除此矛盾。因此
$$
\boxed{f_0(t)=\lambda d(t)^c,\qquad
c\ge0,\quad\lambda\in k^\times.}
\tag{9}
$$
特别 $f_0(0)\ne0$，原 $F(0,Y)/(Y-1)$ 的常数项也非零。

定义
$$
\boxed{G(t,Y)=\frac{F(t,Y)}{\lambda d^c},\qquad [Y^0]G=1,}
\tag{10}
$$
$$
A(t)=d^{-C_D}Q_0(t)f_0(t)^3.
$$
由 (7)、(8) 得
$$
\boxed{A\in k[t]_{\le2},\qquad A(0)\ne0.}
\tag{11}
$$
准确的 scalar projection 是
$$
\boxed{
P_0=t^2A(t)G(t,Y)^3=t^2q(t,0)F(t,Y)^3
\in\mathcal W_{3b}.}
\tag{12}
$$

**证明 (12) 的来源范围。** 在每个 (5) 的赋值中，取 $q$ 的常数 charge 只能提高其值；因此 $t^2q(t,0)F^3$ 保原全部 Gauss 下界。其 $Y$ 次数是 $3b$，且仅有 $d$ 极。由 (5) 的双向识别，它属于 $\mathcal W_{3b}$，不是仅属于扩大后的环境格。原 $D\ge3b$，所以 $f_{3b}<p$ 仍成立。这里未证明 $G$ 本身是旧来源，也未更换原已经指定的整提升。$\square$

## 3. 两个端点亏损及有限角的准确预算

因 $G$ 的常数 charge 为 $1$，其各赋值均不大于零。令
$$
m_\alpha=-v_\alpha(G)\ge0
\quad(h_7(\alpha)=0),\qquad
m_1=-v_1(G)\ge0,
$$
$$
\delta_d=-v_d(G)\ge0,\qquad
\delta_\infty=-v_\infty(G)\ge0.
\tag{13}
$$
在 $0$ 仍有 $v_0(G)=-3$。将 (12) 代入 (5)，得到全部准确不等式
$$
\boxed{
\begin{aligned}
3m_\alpha&\le4\operatorname{ord}_\alpha A+2,\\
m_1&\le\operatorname{ord}_1 A,\\
3\delta_d&\le2\operatorname{ord}_d A,\\
3\delta_\infty+2\deg A&\le4 .
\end{aligned}}
\tag{14}
$$
最后一式保 $t^2$ 的无穷远成本 $4$。零角则为
$8+3(-3)=-1\ge-2$。

由 $\deg A\le2$ 立即有
$$
\boxed{\delta_d+\delta_\infty\le1.}
\tag{15}
$$
更精确地：

- $\delta_\infty=1$ 迫 $\deg A=0$，因此所有有限角亏损为零；
- $\delta_d=1$ 迫 $A$ 是 $d^2$ 的非零常数倍，因此 $\delta_\infty$ 及其余有限角亏损为零；
- 其余情形只有总次数至多二的 $A$ 可补有限角亏损。

若 $\delta_d=1$，达到 $v_d(G)=-1$ 的某个 charge 必为奇数，因为 $2\operatorname{ord}_d G_n+n=-1$。若 $\delta_\infty=1$，达到 $9n-2\deg G_n=-1$ 的 charge 同样必为奇数。这是实际端点项的奇偶限制，不是说 $G$ 可按奇偶平均。

因为 $F$ primitive，不被 $d$ 整除，某个 $F_n$ 在 $d$ 处为单位。因此
$$
2c-\delta_d=v_d(F)\le b,\qquad
\boxed{c\le\left\lfloor\frac{b+\delta_d}{2}\right\rfloor.}
\tag{16}
$$
(16) 保归一分母成本，未免费丢掉它。

## 4. 原 Fp 系数情形恰由五个固定角型覆盖

现在先取 $k=\mathbf F_p$。因 $p\equiv5\pmod6$，
$-3$ 非平方，而 $\operatorname{disc}(h_7)=-432$，故 $h_7$ 不可约；其两个几何角的阶相同，记为 $m_h$。

从 $A$ 删去所有不在 $(t-1)h_7d$ 上的因子，只提高无穷远预算而不损任何有限角条件。若 $\delta_d=0$，所含 $d$ 因子也可删去。保 (14) 后，剩余 mask 可以取为
$$
\boxed{A_*\in\{1,\ t-1,\ (t-1)^2,\ h_7,\ d^2\}.}
\tag{17}
$$
各 mask 的最大允许亏损如下；表中数字是上界，允许较小亏损，故五型可以重叠。
$$
\begin{array}{c|cccc}
A_*&m_h&m_1&\delta_d&\delta_\infty\\ \hline
1&0&0&0&1\\
t-1&0&1&0&0\\
(t-1)^2&0&2&0&0\\
h_7&2&0&0&0\\
d^2&0&0&1&0
\end{array}
\tag{18}
$$
例如 $h_7$ 消耗完整二次帽，(14) 给 $m_h\le2$；它不能同时支付 $t-1$ 亏损。$d^2$ 的 $\delta_d=1$ 同样消耗完整二次帽。

**定理 1。** 满足 (1)–(7) 的每个实际因子，经 (10) 归一后属于 (18) 的至少一型。每一型的全部系数如下。对 $1\le n\le b$，置
$$
a_n=\left\lfloor\frac n4\right\rfloor,\qquad
b_n=\max\left(0,\left\lceil\frac{n-m_h}{4}\right\rceil\right),\qquad
c_n=\max\left(0,\left\lceil\frac{n-m_1}{3}\right\rceil\right),
$$
$$
z_n=\left\lfloor\frac{n+\delta_d}{2}\right\rfloor,\qquad
K_n=\left\lfloor\frac{9n+\delta_\infty}{2}\right\rfloor,
$$
$$
r_n(t)=t^{a_n}h_7(t)^{b_n}(t-1)^{c_n}d(t)^{-z_n},
\qquad
E_n=K_n+z_n-a_n-2b_n-c_n .
\tag{19}
$$
则该型的准确系数格为
$$
\boxed{
G(t,Y)=1+\sum_{n=1}^bY^n r_n(t)p_n(t),
\qquad p_n\in k[t]_{\le E_n}.}
\tag{20}
$$
$E_n<0$ 时该组为空。

**证明。** 零角 $v_0(G)\ge-3$ 给
$\operatorname{ord}_0G_n\ge\lceil(n-3)/4\rceil=\lfloor n/4\rfloor$。
两个 $h_7$ 角和 $t=1$ 分别给 (19) 的 $b_n,c_n$。
$d$ 条件给 $\operatorname{ord}_dG_n\ge-z_n$；仅允许 $d$ 极。
无穷远给 $\deg G_n\le K_n$。
不同固定角互素，因而有限条件准确等价于 $G_n/r_n$ 为多项式；无穷远余帽正是 $E_n$。反方向逐条代回同样成立。
常数 charge 的有限条件和无穷远帽只允许常数，已由 (10) 规范成 $1$。$\square$

任何 (20) 中的 $G$ 都满足相应 Gauss 上界；若它另有实际 $b_0=3$，则零角为准确的 $-3$。取清去其最小 $d$ 分母后的 primitive $F$，则 (16) 仍成立。不可约性、$F_Y(0,1)\ne0$、所需几何与强接触是另外明确的条件。

## 5. 分裂系数域的至多十五个 mask 与逐系数帽

在一般允许的 $k$ 上，$h_7$ 可能分裂，两个 $m_\alpha$ 不能合并。
令 $\mathscr S$ 是 $(t-1)h_7d$ 在 $k[t]$ 中的 monic 不可约因子集合。可取所有
$$
\boxed{
A_*=\prod_{\varpi\in\mathscr S}\varpi^{e_\varpi},
\qquad e_\varpi\ge0,\qquad
\sum_{\varpi\in\mathscr S}e_\varpi\deg\varpi\le2.}
\tag{21}
$$
完全分裂时有四个不同线性因子，所以总数至多
$1+4+10=15$；未分裂时更少。允许保留冗余 mask，不凭五型漏掉交叉亏损。

给定 (21)，对每个 $h_7$ 几何角 $\alpha$ 置
$$
m_\alpha=\left\lfloor
\frac{4\operatorname{ord}_\alpha A_*+2}{3}\right\rfloor,\qquad
m_1=\operatorname{ord}_1 A_*,
$$
$$
\delta_d=\left\lfloor\frac{2\operatorname{ord}_d A_*}{3}\right\rfloor,
\qquad
\delta_\infty=
\left\lfloor\frac{4-2\deg A_*}{3}\right\rfloor.
\tag{22}
$$
这些数非负。公式 (19)、(20) 的逐系数版本是
$$
r_n=t^{\lfloor n/4\rfloor}(t-1)^{\max(0,\lceil(n-m_1)/3\rceil)}
d^{-\lfloor(n+\delta_d)/2\rfloor}
\prod_{\varpi\mid h_7}
\varpi^{\,\max(0,\lceil(n-m_\varpi)/4\rceil)},
\tag{23}
$$
$$
\boxed{
E_n=
\left\lfloor\frac{9n+\delta_\infty}{2}\right\rfloor
-\deg_t r_n.}
\tag{24}
$$
其中 $\deg_t r_n$ 保负分母次数；同一个不可约二次因子的两个根使用同一 $m_\varpi$。证明逐项同定理 1，所有角帽都在 (22)–(24) 中明列。

从旧 $A$ 删去外角因子得到 (21)，不会损失原 $G$ 的任何条件。反之，(21)–(24) 直接保证下节的真实立方返回。这是一般域的完整范围；不将模 $p$ 分裂情形冒称只有五型。

## 6. 每型的真实同预算返回

**定理 2。** 对 (18) 或 (21) 的一个 mask，取其显示格中的 $G$。若 $G$ 满足 (2)、(3) 的因子条件和真实接触条件，则
$$
\boxed{P_*=t^2A_*G^3\in\overline{\mathcal W}_{3b}.}
\tag{25}
$$
它有同一零曲线和同一接触支，且可以在原 $\mathcal O$ 上保持全部角帽整提升。没有增加 radial 预算或把 $G$ 的系数列免费加入原矩阵。

**证明。** 零角给 $v_0(P_*)\ge8-9=-1$。
在 $h_7$ 各角，由 (22) 得
$4\operatorname{ord}_\alpha A_*-3m_\alpha\ge-2$；
在 $1$ 给 $3\operatorname{ord}_1A_*-3m_1\ge0\ge-1$；
在 $d$ 给 $2\operatorname{ord}_dA_*-3\delta_d\ge0$；
无穷远给
$$
v_\infty(P_*)\ge-4-2\deg A_*-3\delta_\infty\ge-8.
$$
仅有 $d$ 极，$Y$ 次数至多 $3b$。由 (5) 的双向识别，得到 (25) 及全部十九角。对 (18) 各行，以上分别保实际次数 $0,1,2,2,2$ 的 mask 成本。

用 R491 的逐系数同时 Hensel 提升保每个有限角阶和无穷远次数；常数 charge 保为 $1$，固定 mask 使用其同一整因子。清分母后的乘积再按同一 Gauss 识别返回 $\mathcal W_{3b}$。这不需要任意选取高轴系数，也不要求先证明物理像饱和。$\square$

更具体地，记真实低轴为 $Y=g(t)$，且
$$
F(t,g(t))\in t^hk[[t]],\qquad h<s.
$$
则 (25) 的普通、第一 Euler、第二 Euler 部分分别至少从
$$
3h+2,\qquad2h+2=s,\qquad h+2
\tag{26}
$$
起，故在 (2) 的原相对首目标中全零。common charge 的低阶组合只提高这些阶，因而
$$
\boxed{P_*\in\ker\bar J\subset\ker\bar M.}
\tag{27}
$$
(27) 保原 $P_{134}/U_0$ 及两条十三行，不是只检一个未经原规范的值 jet。
但首核不等于第二核，(25) 未证明新候选有完整 $p^2$ 或 $p^3$ 提升。

## 7. 原强接触的五个完整非齐次矩阵

取 R434/R683 已付的同一实际低轴
$$
\rho(t)=d(t)\Theta(t)^{17},\qquad
g(t)\equiv\rho(t)\pmod{t^s},\qquad
\rho(0)=1,\quad \rho'(0)=154/15.
\tag{28}
$$
因 $h<s$，本节可用 $\rho$ 读取接触；不延长这个替换到真实高尾或下一位。

固定一个型及 $b,h$。将 (20) 或 (23) 中
$p_n(t)=\sum_{j=0}^{E_n}x_{n,j}t^j$，定义**实际目标素数上的**矩阵
$$
\boxed{
\mathsf H_{A_*,b,h}
(i;(n,j))
=[t^{\,i-j}]\bigl(r_n(t)\rho(t)^n\bigr),\quad
0\le i<h,\quad1\le n\le b,\quad0\le j\le E_n .
}
\tag{29}
$$
负次数系数按零计。所有 $r_n$ 仅在 $d$ 有极，$d(0)=1$，故这些读取均合法。

**定理 3。** 在给定 profile 内，
$$
\boxed{
G(t,g(t))\in t^hk[[t]]
\ \Longleftrightarrow\
\mathsf H_{A_*,b,h}\mathbf x=(-1,0,\ldots,0)^T.}
\tag{30}
$$
原候选必给 (30) 的解。反之，(30) 的解在另满足 primitive 不可约、$b_0=3$、原点光滑及原几何门时，按定理 2 给一个真实同预算 cube 首核候选。

**证明。** 由 (28)，在严格小于 $h$ 的每个位置可将 $g$ 换成 $\rho$。将 (20) 完整代入，常数 charge 正好为 $1$，各其余项的系数正好是 (29)；逐行消失等价于 (30)。反方向同样逐行成立。$\square$

右端常数 $-1$ 来自已证明的 (9)、(10)，不是任意指定的多项式。矩阵含每个来源的全部允许多项式乘子和重复幂；不能以 $\Theta$ 在实区间上的单调性、某个 Beta 正密度或普通两函数 Padé 性质证明它自动正规。

原 $\mathbf F_p$ 情形只须比较五个明确 augmented 矩阵
$[\mathsf H_{A_*,b,h}\mid(-1,0,\ldots,0)^T]$。
本文没有证明右端在像外，也没有把秩的期望值当实际证明。
特别不能由这里的 factor 参数个数直接推出原整个 $\mathcal W_D$ 的像或同 $R$ 不相容。

五型均保精确的模十二结构：
$$
r_{n+12}/r_n=t^3h_7^3(t-1)^4d^{-6},
\qquad E_{n+12}=E_n+47\quad(n\ge1).
\tag{31}
$$
所以相隔十二的实际评价列之比含
$$
343\,t^3\mathcal U(t),\qquad
\mathcal U=
h_7^3(t-1)^4d^{-6}\rho^{12}/343,
$$
$$
\boxed{\mathcal U(0)=1,\qquad
\mathcal U'(0)=2552/35\in k^\times.}
\tag{32}
$$
这是 R683 的同一真实 regular 单位；$p>101$ 的惯性范围排除了其坏素数。
(31)、(32) 给下一步实际矩阵的共同结构，未把各幂的高尾独立化。

## 8. scalar projection 对旧同 P 的真实影响

分类过程不能悄然替换既定提升。对原 (1) 的同一个整因子基准，取
$$
q_\Delta=q-q(t,0),\qquad
P_\Delta=t^2q_\Delta F^3=P^{\rm fact}-P_0.
\tag{33}
$$
由 (6)、(7)，$q_\Delta$ 的全部 $Y$ 系数均被 $t$ 整除；
因此在原支 $C$ 上，$t^2q_\Delta$ 的值及 $\mathcal E$ 导数都属于 $t^3k[[t]]$。
由 R755，$P_\Delta$ 是真实 primitive 相对首核方向，但其完整 Bockstein 一般不为零。

保原
$$
\eta_0=t^hu,\quad \eta=\eta_0+p\xi,\quad
t^s=p\epsilon b_s,\quad
e=(\mathcal EF)|_C,\quad
M=c_*U_0w^{13}J,\quad N_0=s-13=2h-11.
\tag{34}
$$
前两块只在原 $w^{13}$ 之后的合法行除显示单项，再换原 $t$；
第三块保持原物理 $w$。
R755 的全式给
$$
\boxed{
\widehat\beta_0(P_\Delta)=0,\qquad
\widehat\beta_1(P_\Delta)=
e^3q_{\Delta,C}\,t^hu
\left(b_su^2+6at^2\xi\right)
\pmod{t^{N_0}},
}
\tag{35}
$$
$$
\boxed{
\left[(c_*U_0)^{-1}M(P_\Delta)/p\right]^{(2)}
=0\pmod{w^{14}}.}
\tag{36}
$$

**证明。** R755 的 $C_3=e^3t^2q_{\Delta,C}$、
$C_4=e^3t^2(\mathcal Eq_\Delta)|_C+
\frac32e^2(\mathcal E^2F)|_Ct^2q_{\Delta,C}$ 均至少有 $t^3$。
代入其 $d_0=2$ 的完整首 Bockstein：
普通块为零；第二块的 $C_4$ 项从 $2h+1>N_0$ 起，
其余两项准确合成 (35)。
第三块的 native 项至少三阶，$C_3t^{-2}$ 至少一阶，
$C_4t^{h-2}$ 至少 $h+1$ 阶。
乘同一个 $w^{13}$ 后在 $\ell=1$ 的目标内全零，得 (36)。
没有删除实际 $\xi_0$、$b_s$ 高尾或行缩放。$\square$

(35) 从至少 $h+1$ 起，但仍可能位于原短截止内。因此 scalar projection 保值类和该第三块，却**不保整个首 Bockstein**。将 $A$ 再换为最小固定 mask 更是在构造新候选，不能把旧 $P_2$ 的 $R$ 随之免费运输。

若固定的是 $P_2=P^{\rm fact}+pR$，原所有修正仍共用这个 $R$，
包括 (35) 的实际 first-normal 尾、两条十三行以及下一位。
本文既未用五型重新选择 $\xi$，也未给这些 factor 列增加中央零。

## 9. 本篇完成的存在门与剩余指定像

在 (6) 的真实非空范围，任意原强接触 cube 都必须经过：

1. 常数 charge 刚性 (9) 和分母帽 (16)；
2. 全部有限角及无穷远的五型 (18)，或一般域至多十五 mask (21)；
3. 每个 charge 的完整次数帽 (19)、(23)、(24)；
4. 同一实际低轴的非齐次系统 (30)，及不可约、光滑和原几何门。

这些条件也给付清成本的立方返回 (25)，故是原来源上的存在问题，不是环境曲线搜索。尚未完成的是这些矩阵的真实强接触判定，以及在已有候选上把 (35) 和原指定 forcing 接入整个 $\mathcal W_D$ 的 full normal 像。不能以分类、factor 参数维数、一个裸边界非零或新候选的首核身份代替这个同 $R$ 问题。

依赖：
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R771](R771-original-r2-full-fiber-and-complete-boundary-compensation.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R768 的实际 r2 来源](../notes/2026-11-15-r768-actual-r2-cubic-fiber-and-full-two-output-source.md)。
