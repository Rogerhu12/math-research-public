# R517 — 原切向两 charge 返回、全 Γ 转置与分歧微分

日期：2026-11-14。**状态：已证明。** 本篇将 R514 的三次 forcing 接到另一族有准确成本的实际来源。切向算子
$\mathcal V_F=(\mathcal EF)\delta_t-(\delta_tF)\mathcal E$
在整个原有限目标上有整链式恒等式，因此得到同一个真实 $\mathcal H_2$ 的完整转置方程；它在模 $p^2$ 及原 $M$ 中仍保留全部 Gaussian、低行高尾和两次 carry。

这族来源统一需要两个 charge；同 $D$ 的另一个充分窗明确保
$4r-D\ge14$。三层局部转置完全写出，不能通过删除最高 normal 层把它缩成一个未经支付的镜轴行。

最后，$e^2\mathcal F_F$ 在通常的简单分歧点确实有简单极；
$e^2\mathcal F_F\,dt$ 则是一个准确的二次 Kähler 微分。后者支付分歧微分对象，并不把前者变成 R511 的二倍截面。

## 1. 同一实际来源和切向算子

保 R495、R498、R502、R507、R511、R514 的原对象。
$$
p=6s-1>83,\qquad 1\le\ell<s-13,\qquad
\Gamma_\ell=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2).
\tag{1}
$$
原来源为
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,
\quad d=1+8t,\quad
D_0=3b+\deg_YQ\le D,\quad b=\deg_YF.
\tag{2}
$$
$F,Q$ 是 R491 支付的同一整提升，$F(0,1)=0$、
$F_Y(0,1)Q(0,1)\in\mathcal O^\times$。为简洁省去波浪号。
其约化曲线 $C$、十九次吹起 $X$、正规分支 $Y=\psi(t)$ 均不变。
若继续调用 $f_D<p$ 的几何或首核结论，保这一原假设。

记
$$
\delta_t=t\partial_t\quad(Y\text{ 固定}),\qquad
\mathcal E=Y\partial_Y,\qquad
e=\mathcal EF,\quad a_0=\delta_tF,
$$
$$
\boxed{\mathcal V_F=e\delta_t-a_0\mathcal E.}
\tag{3}
$$
于是
$$
\mathcal V_F(F)=0,\qquad
\mathcal V_F(F^jH)=F^j\mathcal V_F(H).
\tag{4}
$$

$\mathcal H_2$ 是 R511 同一整二倍截面格，逐 charge 的固定角整除及次数帽给出
$$
\mathcal H_2=\bigoplus_{i=0}^{2b}
Y^iD_i(t)\mathcal O[t]_{\le m_i}.
\tag{5}
$$
负次数项省去。十九个中间角全部包含在 $D_i,m_i$ 中。
因此它有限自由、准确约化为 $H^0(X,\mathcal O_X(2C))$，并且
$$
\boxed{\mathcal E\mathcal H_2\subset\mathcal H_2.}
\tag{6}
$$
在 (5) 的显示基上 $\mathcal E_2$ 就是整数 $i$ 的对角矩阵。
这不是增补自由 normal 列；$\mathcal H_2$ 的三个局部 normal 系数仍来自同一个实际截面。

## 2. 两 charge 的完整整返回

使用 R514 (3) 对 $\mathcal W_D$ 的准确未清分母判据。
对任意 $H\in\mathcal H_2$，所有对应角值满足
$$
\begin{array}{c|ccccc}
v&v_0&v_{h_7}&v_1&v_d&v_\infty\\ \hline
v(\mathcal V_FH)-3v(F)\text{ 的下界}
&0&-4&-3&-2&0 .
\end{array}
\tag{7}
$$
因为 $\mathcal E$ 不改变角阶；每个非零有限角的一次
$\delta_t$ 最多损一个普通阶，在 $0$ 和 $\infty$ 则不损。
这里 $H$ 保 $v(H)\ge2v(F)$。

取固定多项式
$$
\boxed{\mathfrak m_2=Y^2t(t-1)^2h_7^2,\qquad
h_7=7+4t+16t^2.}
\tag{8}
$$
其准确 Gauss 值为
$$
(v_0,v_{h_7},v_1,v_d,v_\infty)(\mathfrak m_2)
=(2,6,4,2,4).
\tag{9}
$$

**定理 1。** 同一来源的整线性算子
$$
\boxed{
\mathcal T_F:\mathcal H_2\longrightarrow\mathcal W_{D_0+2},
\qquad
H\longmapsto d^{-C_D}t^rQ\,\mathfrak m_2\mathcal V_FH
}
\tag{10}
$$
有定义。因此其像在 $\mathcal W_{D+2}$ 中；
若 $D_0+2\le D$，则已在原 $\mathcal W_D$。

**证明。** (7)、(9) 保乘积每个原 Gauss 值不低于 (2)。
$Y$ 次数至多 $D_0+2$，仍只允许原 $d$ 分母。
R514 的双向判据逐列恢复准确 $q_n$ 与次数帽，故得 (10)。$\square$

这里没有从整来源算子推断其物理像 $p$ 饱和。
如果使用扩大后格上那些以 $f_D<p$ 为假设的结果，
须另保 $f_{D+2}<p$。旧 $\mathcal W_D$ 的左行也不自动杀扩大后的两条 charge。

### 十九个中间角

置 $u=\max_i(\deg F_i-4i)$。对
$G=\mathfrak m_2\mathcal V_FH$ 使用固定 ambient 帽
$$
\deg_YG\le3b+2,\qquad
\deg_tG_i\le3u+4i .
$$
实际斜次数还多一个单位的余量，因为 $\deg_t\mathfrak m_2=7$、
$\deg_Y\mathfrak m_2=2$。按 R495 的每个累计值，有
$$
\begin{array}{c|c|c}
\text{链}&j\text{ 的范围}&V_j(G)-3V_j(F)\text{ 的下界}\\ \hline
0,\ h_7\text{ 两根的 }Y=\infty&1,\ldots,4&j\\
1\text{ 的 }Y=\infty&1,\ldots,3&j\\
d=0,\ Y=0&1,2&2-j\\
t=\infty,\ Z=0&1,2&j+2 .
\end{array}
\tag{11}
$$
有限 $Y=\infty$ 链的 ambient 次数增二抵消 $Y^2$；
在 $h_7,1$ 处两份角零支付一次求导后余 $j$，
$0$ 处直接由一份 $t$ 得 $j$。
$d$ 处一次求导最多损 $j$，$Y^2$ 给二；
无穷远权 $(-j,4j+1)$ 给乘子 $j+2$，原求导不增加次数。

故
$$
G\in H^0\!\left(X,\mathcal O_X(3C+2\pi^*S_\infty)\right).
\tag{12}
$$
这里与 R514 一样是拉回类 $\pi^*S_\infty$，不是严格变换。
(12) 没有将 $G$ 放回未增加预算的 $\mathcal H_3$。

### 纯 Gauss 清极预算的准确最小性

在只要求一个固定多项式乘子补齐 (7) 的整个最坏范围内，
两个 $Y$ 次数确为最小。准确要求是
$$
v_0(m)\ge0,\quad v_{h_7}(m)\ge4,\quad v_1(m)\ge3,
\quad v_d(m)\ge2,\quad v_\infty(m)\ge0.
\tag{13}
$$
若 $m=\sum m_i(t)Y^i$ 的 $Y$ 次数不超过一，
各个非零系数都须满足这些条件。
$i=0$ 时，$m_0$ 必须被 $h_7(t-1)d$ 整除，次数至少四，
但无穷远要求次数不超过零。
$i=1$ 时，必须含 $t(t-1)^2h_7^2d$，次数至少八，
但无穷远要求次数不超过四。两者都不可能。
(8) 则满足 (13)。

这是**固定多项式乘子补齐全部最坏 Gauss 损失**的最小性。
对有额外消去或额外 $r$ 缓冲的个别实际因子，不能用它排除更小成本。

## 3. 保同 D 的另一充分窗

令
$$
\mathfrak n_0=(t-1)h_7d.
$$
它的次数是四。由 (7)，$\mathfrak n_0\mathcal V_FH$
在全部有限原角均不低于 $3v(F)$，
在无穷远最多低八。

因此若
$$
\boxed{r\ge4,\qquad v_0(P^{\rm fact})\ge14,}
\tag{14}
$$
则
$$
\boxed{
\mathcal T_F^{(0)}(H)
=d^{-C_D}t^{r-4}Q\,\mathfrak n_0\mathcal V_FH
\in\mathcal W_D
\quad(H\in\mathcal H_2).
}
\tag{15}
$$
除去 $t^4$ 恰在无穷远补回八，在 $0$ 损十六；
(14) 使其仍不低于原界 $-2$。
$Y$ 次数不增，且 $r\ge4$ 保没有新 $t$ 分母。
同样应用原双向判据，得到全部原列帽。

仅用原参数的充分条件是
$$
\boxed{4r-D\ge14.}
\tag{16}
$$
这也迫 $r\ge4$，因为 $D\ge0$。不能只保 $r\ge4$ 就调用 (15)。

(15) 的前缀已变为 $t^{r-4}$。
若要在 R498 的高块表示它，必须保它真实产生的低行和全部高尾。
下一节的全目标公式直接包含这些项，不需要把它伪装成纯高块来源。

## 4. 全 Γ 中的准确链式恒等式

令 $\operatorname{ev}$ 为 R498 相对框中的实际代入：
$$
\operatorname{ev}(H)=H(t(w),Y_{\rm phys}),\qquad
Y_{\rm phys}=g(w)e_2(a\epsilon).
$$
在这个相对框中 $J$ 正是这个代入在原来源上的限制。
共同 carrier、charge $40$ 和原 $U_0$ 在第6节完整恢复。

R507 的整单位 $\nu=\delta_t\log w$ 与合法导子给
$$
\mathsf N(w)=w,\qquad\mathsf N(\epsilon)=s\epsilon,
\qquad
\mathsf D=\nu\mathsf N,\qquad \mathsf D(t)=t .
\tag{17}
$$
$\mathsf D$ 保 (1) 的全部三个关系。
写
$$
U=Y_{\rm phys}^{-1}\mathsf D(Y_{\rm phys})\in\Gamma_\ell.
$$
准确链式法则是
$$
\mathsf D\,\operatorname{ev}(H)
=\operatorname{ev}(\delta_tH)+U\operatorname{ev}(\mathcal EH).
$$
对 $F$ 也使用同一 $U$ 后相消，得到

**定理 2。**
$$
\boxed{
\operatorname{ev}(\mathcal V_FH)
=\operatorname{ev}(e)\,\mathsf D\,\operatorname{ev}(H)
-\mathsf D\,\operatorname{ev}(F)\,\operatorname{ev}(\mathcal EH).
}
\tag{18}
$$
这是整个 $\Gamma_\ell$ 的整恒等式，因而在模 $p^2$ 和更高精度都成立。
其中没有删除 $a s\epsilon$、把 $\epsilon$ 当微分常量，
或提前令原 raw $\bar\Gamma$ 中的 $\zeta^3$ 为零。

设 $\mathsf A_2:\mathcal H_2\to\Gamma_\ell$ 是这个实际有限矩阵，
$\mathsf M_f$ 表示完整目标上乘 $f$。
对 (10) 令
$$
c=\operatorname{ev}(d^{-C_D}t^rQ\mathfrak m_2).
$$
则 (18) 成为准确整矩阵等式
$$
\boxed{
J\mathcal T_F
=\mathsf M_{c\,\operatorname{ev}(e)}
\,\mathsf D\,\mathsf A_2
-\mathsf M_{c\,\mathsf D\operatorname{ev}(F)}
\,\mathsf A_2\mathcal E_2 .
}
\tag{19}
$$
对 (15)，只将 $c$ 换成
$\operatorname{ev}(d^{-C_D}t^{r-4}Q\mathfrak n_0)$；
所有低行高尾仍在同一等式内。

(19) 的每个对象都是已指定的有限自由来源或原目标上的整矩阵。
在原合法基 $w^j\epsilon^i$、
$n=j+is=0,\ldots,L-1$ 中，
$$
\mathsf D=\mathsf M_\nu\,\operatorname{diag}(0,1,\ldots,L-1),
\qquad L=2s+\ell.
\tag{20}
$$
矩阵乘法次序如写出的一样，不能交换 $\nu$ 与对角微分。

## 5. 同一真实来源上的完整转置

设 $\lambda$ 是所用实际 $J$ 矩阵的真左行，
取系数环 $\mathcal O/p^m$，$m=1,2$ 或任意已付精度。
(10) 必须在该矩阵的真实来源内：或有两个 charge 余量，
或使用扩大后的矩阵；(15) 则按 (14) 保同 $D$。

由 (19) 得到
$$
\boxed{
\mathsf A_2^{\,T}\mathsf D^{\,T}
\mathsf M_{c\,\operatorname{ev}(e)}^{\,T}\lambda
=
\mathcal E_2^{\,T}\mathsf A_2^{\,T}
\mathsf M_{c\,\mathsf D\operatorname{ev}(F)}^{\,T}\lambda .
}
\tag{21}
$$
它是同一个 $\mathcal H_2$ 的全部列方程。
特别对 (5) 中 charge 为 $i$ 的真实基列 $H_{i,j}$，
$$
\boxed{
\left\langle\lambda,\,
c\,\operatorname{ev}(e)\,
\mathsf D\operatorname{ev}(H_{i,j})\right\rangle
=
i\left\langle\lambda,\,
c\,\mathsf D\operatorname{ev}(F)\,
\operatorname{ev}(H_{i,j})\right\rangle .
}
\tag{22}
$$
右边的 $i$ 来自原有限来源，不是补入一个自由 Euler 输出。
$\mathcal T_F(F^2)=0$ 给 (21) 中一条确定的冗余关系；
没有据此声称这是全部核，或声称切向物理像饱和。

(21) 为实际原列测试增加了一组显示的微分转置形式。
它仍不是“目标 $\mathcal P$ 保原来源像”的断言；
R507 的目标 Smith 共振不能替代其右边及原 $\mathcal H_2$ 的完整像。

## 6. 原 M 与十三行边界不动

保原整分解
$$
M=c_*U_0m_{13}J.
$$
对 $\Gamma_{\ell+13}$ 中的真正模 $p^m$ 左行 $\lambda_M$，
使用整拉回
$$
\boxed{
\lambda_J=
m_{13}^{\,T}\mathsf M_{c_*U_0}^{\,T}\lambda_M .
}
\tag{23}
$$
若 $\lambda_M$ 杀所用原 $M$ 的全部来源，则 $\lambda_J$ 杀同一 $J$，
所以可在 (21) 中直接使用它。

(23) 没有对 $m_{13}$ 作非整逆，
也没有把微分直接穿过 $U_0$ 或 charge $40$。
因此原 $P_{134}$、十三自由行、两条十三行 carry、
$U_1/p$ 和第三精度都按原矩阵保留。
若要将 (21) 改写成直接作用在 $M$ 目标的微分，
仍须使用 R507 的有序
$\mathsf N+13+U_0^{-1}\mathsf N U_0$，
不能省去这些零阶项。

## 7. 几何真行的三层切向转置

本节在 R502/R511 的低 $\ell$ 范围工作：
$$
1\le\ell\le r<h,\qquad
0\le k<\ell,\qquad
S=s-r=2h-k,\qquad q=h-k .
$$
取 R498 通过所有原列测试的真实高块行
$$
\Phi=(A+B\zeta+C_2\zeta^2)
\frac{dt\wedge d\zeta}{\zeta^3},
\qquad
A-2\eta_0B\text{ 正则},\quad
\operatorname{pole}(A)\le q .
\tag{24}
$$
使用同一个完整 $t^rQ/d^{C_D}$ 规范化；
(10) 仍有 $t^r$ 前缀，故没有待删的低行输出。

置 $n=F$。沿 $C$ 记
$$
e=(\mathcal EF)|_C,\quad
f_2=(\mathcal E^2F)|_C,\quad
f_3=(\mathcal E^3F)|_C,\quad
m=(\mathfrak m_2)|_C.
$$
在 $P$ 处 $e$ 是单位。正常坐标变换给
$$
\boxed{
\Phi=(\alpha+\beta n+\gamma n^2)
\frac{dt\wedge dn}{n^3},\quad
\alpha=e^2A,\quad
\beta=eB+\tfrac12f_2A,\quad
\gamma=C_2 .
}
\tag{25}
$$
证明可用
$\zeta^{-1}=e/n+f_2/(2e)+O(n)$：
$d\zeta/\zeta^3$ 的主部为
$e^2dn/n^3+(f_2/2)dn/n^2$；
$d\zeta/\zeta^2$ 的主部为 $e\,dn/n^2$；
$d\zeta/\zeta$ 的留数为一。
所有双线束框保持互为对偶。

在 $(t,n)$ 坐标中，因 $\mathcal V_F(n)=0$，
$$
\mathcal V_F=e(t,n)\delta_t\big|_n .
$$
对任何实际 $H\in\mathcal H_2$ 写
$$
H=h_0+h_1n+h_2n^2\pmod{n^3}.
$$
定义下列三个**无 $e$ 分母**的系数：
$$
\boxed{
\begin{aligned}
Z_0={}&m e^3A,\\
Z_1={}&m\left[e^2B+
\left(2e^2+\tfrac32ef_2\right)A\right],\\
Z_2={}&m\left[eC_2+(2e+f_2)B+
\left(2e+2f_2+\tfrac12f_3\right)A\right].
\end{aligned}}
\tag{26}
$$
这里系数 $2$ 来自真实乘子的 $Y^2$，没有将它忽略。

**定理 3。** (10) 被原真行杀掉的完整局部条件准确为
$$
\boxed{
\operatorname{Res}_P
\left[
\widehat A\,h_2+\widehat B\,h_1+\widehat C\,h_0
\right]dt=0
\quad\text{对每个真实 }H\in\overline{\mathcal H}_2,
}
\tag{27}
$$
其中
$$
\boxed{
\widehat A=-(\delta_t+1)Z_0,\qquad
\widehat B=-(\delta_t+1)Z_1,\qquad
\widehat C=-(\delta_t+1)Z_2 .
}
\tag{28}
$$

**证明。** 将
$\mathfrak m_2(t,n)e(t,n)(\alpha+\beta n+\gamma n^2)$
按 $n$ 展开到二阶。其三个系数恰为 (26)。
例如
$\partial_n e=f_2/e$，
$\partial_n^2e=(ef_3-f_2^2)/e^3$，
$\mathfrak m_2(t,\psi e^\zeta)=m e^{2\zeta}$。
代入 (25) 后，二阶展开中的 $e$ 分母准确相消，得到 (26)。

于是原配对是
$\operatorname{Res}(Z_0\delta_t h_2+
Z_1\delta_t h_1+Z_2\delta_t h_0)dt$。
用
$\operatorname{Res}f\delta_t h\,dt
=-\operatorname{Res}(\delta_t+1)f\,h\,dt$
即得 (27)–(28)。$\square$

等价地，若使用原体积形式
$\omega=dt\wedge dY/Y$，则
$$
\operatorname{div}_\omega\mathcal V_F=e.
$$
这是因为
$(\delta_t+1)e-\mathcal E a_0=e$。
所以未换坐标的完整形式转置为
$-(\mathcal V_F+e)$，但必须作用于整个乘了
$\mathfrak m_2$ 的行。它不是只对 $A$ 层求导。

(27) 保三层实际 normal 系数；它们不能自由任取。
尤其 $\widehat A$ 一般非零，
不能为了得到镜轴二层形式而将 $h_2$ 项删掉。
对 (15) 应优先使用全目标 (21)，
或先支付其真实低行消元及所有高尾后再转为局部形式。

## 8. 最高极被准确传送，尚未消除全局 normal 相容性

$m=t\cdot\text{单位}$。
因此 (28) 给
$$
\operatorname{pole}(\widehat A)\le q-1,\qquad
\operatorname{pole}(\widehat B),
\operatorname{pole}(\widehat C)\le S-1.
\tag{29}
$$
每个系数的 $t^{-1}$ 项都为零，因为 $\delta_t+1$ 杀它。

若 $A$ 的实际极阶是 $q_A\ge3$，则
$$
\boxed{\operatorname{pole}(\widehat A)=q_A-1.}
\tag{30}
$$
最高系数是原最高系数乘单位
$-(2-q_A)(m/t)(P)e(P)^3$。
因 $q_A\le q<S<p$，这里不会出现另一个特征 $p$ 共振。
若 $q_A\le2$，则 $\widehat A$ 的主部为零。

R505 已识别由 $A$ 给出的真正接触行
$\operatorname{Res}Ae^2H\,dt$ 属于
$H^0(C,K_X|_C(qP))$。
所以当 $\chi=-K_XC\ge4$ 时，非零接触行的极阶必至少为
$\chi$；(30) 说明它不能仅靠切向最高层的形式相消逃逸。
该最高层变换在这些实际接触主部上是单射的。

然而这不等于 (27) 的整个泛函非零。
$h_0,h_1,h_2$ 仍来自一个全局二倍截面，
后两项可能与第一项配合。
(29) 的零留数也不意味着可以任意删除某个 normal 层。
真正未付的是同一有限 $\mathcal H_2$ 的全局联合像，
不是局部最高系数是否为单位。

## 9. forcing 的准确二次微分与不可省的分歧极

保 R514 的
$$
A_0=6(1-t),\quad B_0=-(1+2t),\quad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2},
$$
$$
K_F=e^3\mathcal R+
A_0(e\mathcal V_Fa_0-a_0\mathcal V_Fe)+B_0e^2a_0.
\tag{31}
$$
这里的 $e,a_0$ 在 (31) 先是原多项式，随后限制到 $C$。
沿 $C$ 有
$K_F=e^3\mathcal F_F$，
$\mathcal F_F=\mathcal R-\mathcal P\log\psi$。

在 $C$ 的微分中定义
$$
\Omega_F=\frac{K_F}{e}\,dt
=e^2\mathcal F_F\,dt.
$$
用 $\mathcal V_F|_C=e\,t\,d/dt$，得到
$$
\boxed{
\Omega_F
=e^2\mathcal R\,dt+
A_0t(e\,da_0-a_0\,de)+B_0ea_0\,dt.
}
\tag{32}
$$
右边对 $F$ 及其导数仅为二次，且是准确的 Kähler 微分表达。
所以在 $C\cap\{Yd\ne0\}$ 上它是正则 Kähler 微分的像，
也给一条正则对偶化微分。$e=0$ 不产生新的对偶化微分极。

也可用原残数表达直接证明：
$$
\Omega_F=K_F\,\operatorname{Res}_C
\frac{dt\wedge dY/Y}{F}
=K_F\,\frac{dt}{YF_Y}.
\tag{33}
$$
在光滑的垂直分歧点，$F_t\ne0$，故
$dt/e=-dY/(YF_t)$ 正则。
若 $C$ 在别处奇异，本段说的是曲线自身的 Kähler/
对偶化微分；不把它冒称正规化上处处无极。

相反，标量 $e^2\mathcal F_F=K_F/e$ 一般真的有极。
取一个光滑简单分歧点 $Q$，并假设
$$
t(Q)\notin\{0,1,-1/8\},\qquad
Y(Q)\ne0,\qquad F_t(Q)F_{YY}(Q)\ne0.
\tag{34}
$$
此时 $e=0$，而
$$
K_F(Q)=A_0(Q)\,a_0(Q)^2\,(\mathcal E^2F)(Q)
=A_0(Q)t(Q)^2F_t(Q)^2Y(Q)^2F_{YY}(Q)
\ne0.
$$
在 $Q$ 的均匀化参数中 $e$ 恰有一重零，故
$$
\boxed{\operatorname{ord}_Q(e^2\mathcal F_F)=-1.}
\tag{35}
$$
与此同时 $dt$ 有一重零，(32)–(33) 正好支付它。
(34) 是准确的条件性局部陈述，没有假定每个实际 $F$ 都必有这样的点。

因此 (32) 的二次微分身份不能替换成
$e^2\mathcal F_F\in H^0(C,N_C^2(-hP))$。
若存在 (34) 的点，这个替换甚至在该点就失败。
任何在 $Q$ 为单位的固定角乘子都不能消去 (35)；
R514 的三次来源返回也不能先除以 $e$ 再免费降低到镜轴二倍来源。

## 10. 与原 forcing 和下一精度的真实接口

R514 付清的三次来源给完整行方程
$$
\operatorname{Res}
\left[
\tfrac12 A(\mathcal E^2G)|_C+
B(\mathcal EG)|_C+
C_2(\mathfrak m_3|_C)e^3\mathcal F_F
\right]dt=0,\qquad G=\mathfrak m_3K_F .
$$
本篇 (21)、(27) 是同一原真行还须满足的切向来源方程。
(31)–(33) 将 forcing 的切向微分与分歧残数位置明确给出，
但没有删除该三次来源的两个 normal 项。

要用真正模 $p^2$ 左行提取 R507 的除 $p$ forcing，
应使用全目标 (21)，连同 R502 的活 $V_1$、
R481 的同一个首次修正和 R479 的边界；
不能只对 (32) 或三次方程的最后一项除 $p$。
三条原完整中央没有传播到 $\mathcal T_F(H)$、
$\mathcal T_F^{(0)}(H)$ 或任何二次微分。

本篇新增两个 charge 的真实整返回、其最小固定清极预算、
原全目标转置和分歧处的准确微分对象。
原左行在同一二倍来源上的三层兼容以及跨 $p$ 非零仍待推进。
