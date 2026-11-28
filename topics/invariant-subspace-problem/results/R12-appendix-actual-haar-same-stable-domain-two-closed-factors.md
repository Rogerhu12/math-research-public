# 原 Haar 算子的同一稳定闭域双因子与完整进位返回

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本文承接[完整进位的实际值域与一维余项](R12-appendix-physical-median-two-intervals-and-actual-carry-range-rank-one-residue.md)，在每个原 Walsh 块根的同一最大稳定域上，构造两个闭算子 $S,T$，使真正原 Haar 尾满足 $TS=C|_{\mathcal D}$。两者都只比原块根差一个有界迹类算子；但它们不同，也没有得到 $S^2=C$。以下逐项支付实际定义域、首行伴随来源及乘积的方向。

## 1. 保留的原对象与满射右因子

固定同一原尾 $C=A^{(m)}=D+K$。沿用[原全 Walsh 块](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md)的
$$
Q_{-1}H=\mathbb C\Omega,\qquad
u_j=q_{j,0},\quad v_j=q_{j,2^j-1},\qquad
D_jv_j=-\mu_ju_j.
$$
$u_0=v_0$ 与 $\Omega$ 正交，不合并这两个一维块。
令
$$
X=\overline{\operatorname{span}}\{\Omega,v_0,v_1,\ldots\},\qquad
P_0=\Omega\Omega^*,\qquad r=2^{-1/2}.
$$
前稿构造了实际有界 $L=P_XLP_X$、$\|L\|\le4$ 和有界泛函
$$
\psi(c\Omega+\textstyle\sum_j t_jv_j+x_\perp)
=\mu_0c-\sum_j\mu_jr^{-j}t_j,\qquad x_\perp\in X^\perp,
\tag{1}
$$
使
$$
CL=K+\Omega\psi,\qquad
\mathcal V=I-L,\qquad C\mathcal V=D-\Omega\psi.
\tag{2}
$$
$\mathcal V$ 满射，$\ker\mathcal V=\mathbb C\Omega$。
取前稿的实际右逆 $\mathcal U$：在 $X^\perp$ 上为恒等，在 $X$ 上为
$$
\mathcal U z=
J_X\!\left(0,-\operatorname{diag}(a_j/\mu_j)\,
\mathcal A J_X^{-1}z\right).
\tag{3}
$$
这里 $\mathcal A:\mathbb C\oplus\ell^2\to\ell^2$ 是前稿已实际付清原逆权的有界全行，
$\|\mathcal A\|\le1$，$1/2\le\mu_j/a_j<1$。因此
$$
\|\mathcal U\|\le2,\quad
\mathcal V\mathcal U=I,\quad
\mathcal U\mathcal V=I-P_0,\quad
\operatorname{Ran}\mathcal U=\Omega^\perp,
\tag{4}
$$
$$
\mathcal U-I=P_X(\mathcal U-I)P_X.
\tag{5}
$$
第二个乘积身份也可从 $\mathcal V|_{\Omega^\perp}$ 的单射和 (3) 直接得到。
没有把这个非交换右逆当作 $C$ 的交换子。

## 2. 所有块根共同拥有的小首行和小末列

每个有限块任取完整平方根 $R_j^2=D_j$。
$D_j$ 的谱简单，任何这样的根都与 $D_j$ 交换；在原平衡坐标中，
$$
R_j=\sqrt{r_j}\,Z_j W_j Z_j^{-1},
\tag{6}
$$
其中 $W_j$ 是某个酉平方根，$r_j=(\mu_j\beta_j)^{1/2^j}$。
原前缀反转身份给
$$
Z_ju_j=u_j,\qquad
Z_jv_j=(r_j/\mu_j)v_j,\qquad
I\le Z_j\le(r_j/\mu_j)I.
\tag{7}
$$
特别对于全部分支，不需选主根，
$$
\boxed{\quad
\|R_jv_j\|\le\sqrt{r_j},\qquad
\|R_j^*u_j\|\le\sqrt{r_j}.
\quad}
\tag{8}
$$
这里 (7) 的上下界也可直接由原权核实：用[统一中位间隙](R12-appendix-uniform-walsh-root-median-gap-and-trace-class-physical-polarization.md)的
$d_i=-\log(a_i\beta_{i,2^i-1})$，置 $\Lambda_j=-\log r_j$、
$A=100\,16^m,\ B=105\,8^m,\ H_0=150\,2^m$。$i<j$ 时
$
\Lambda_j-\frac{d_i}{2^i}
=A(8^j-8^i)-B(4^j-4^i)+H_0(j-i)+\frac{\varepsilon_j}{2^j}>0,
$
因为 $B/A\le21/20$ 而 $(8^j-8^i)/(4^j-4^i)\ge7/3$。
这里 $\varepsilon_j=\log(a_j/\mu_j)>0$，与原 carry 系数 $\delta_j=\mu_j-\mu_{j+1}$ 区分。
对 $Z_j$ 的第 $k$ 个对角元有
$\log Z_{j,k}=\sum_{i<j}\operatorname{bit}_i(k)(2^i\Lambda_j-d_i)$；
故最小值在 $k=0$、最大值在所有位为一的末列。$j=0$ 无此和，直接有 $Z_0=I$、$r_0=\mu_0$。
这说明两端确控制全部原行，不仅是端点值恒等式。

第一式在 (6) 的右端使用最大对角列，第二式在其伴随使用最小对角行。
它们不能换成未经支付的全部块范数界。

在常数块取 $\gamma^2=\mu_0$，$R\Omega=\gamma\Omega$；
令 $R=\gamma P_0\oplus\bigoplus_{j\ge0}R_j$ 为最大直和，记
$$
\mathcal D=\operatorname{Dom}R
=\{x:\sum_j\|R_jQ_jx\|^2<\infty\}.
\tag{9}
$$
此 $R$ 闭、稠密定义，有限个整块是图核心，且
$$
R\mathcal D\subset\mathcal D,\qquad
\operatorname{Dom}(R^2)=\mathcal D,\qquad
R^2x=Dx\quad(x\in\mathcal D).
\tag{10}
$$
原准确费用
$-\log r_j=100\,16^m8^j+O_m(4^j+j+1)$
特别支付
$$
\sum_j(1+r^{-j})\sqrt{r_j}<\infty,\qquad
\sum_jr^{-2j}r_j<\infty.
\tag{11}
$$
由 (8)，$R|_X$ 延伸为整个 $X$ 上的迹类算子。
更准确地，
$$
\boxed{\quad X\subset\mathcal D,\qquad
\|RP_X\|_1\le|\gamma|+\sum_j\sqrt{r_j}.\quad}
\tag{12}
$$
这是实际域包含：先用有限整块截断，源在 $X$ 中范数收敛，
像由 (8) 收敛，再用 $R$ 闭性；不只是形式列和。

## 3. 一个真实有界行支付秩一余项

置
$$
\psi_{\rm t}=-\sum_j\mu_jr^{-j}v_j^*,\qquad
\psi=\mu_0\Omega^*+\psi_{\rm t}.
$$
定义全 $H$ 上的行泛函
$$
\eta\Omega=0,\qquad
\eta|_{Q_jH}=-r^{-j}u_j^*R_j.
\tag{13}
$$
(8)、(11) 给真实伴随来源费用
$$
\|\eta\|^2
=\sum_jr^{-2j}\|R_j^*u_j\|^2
\le\sum_jr^{-2j}r_j<\infty.
\tag{14}
$$
在每个完整有限块上，
$u_j^*D_j=-\mu_jv_j^*$，故
$$
\eta R=\sum_j\mu_jr^{-j}v_j^*=-\psi_{\rm t}
\qquad\text{在 }\mathcal D\text{ 上}.
\tag{15}
$$
延拓步骤是整块图核心：若 $x_n\to x$ 且 $Rx_n\to Rx$，
则左侧由 $\eta$ 有界而收敛，右侧由 (1) 的有界行收敛。
因此 (15) 不是形式矩阵乘法；$\eta R|_{\mathcal D}$ 确有所示的有界全域延拓。

令
$$
R'=R-\gamma P_0,\qquad
T=R'+\Omega\eta,\qquad \operatorname{Dom}T=\mathcal D.
\tag{16}
$$
$T$ 是闭算子；$T-R=\Omega(\eta-\gamma\Omega^*)$ 为秩一有界算子。
由 $R'\Omega=0$、$\eta\Omega=0$ 及 (10)，
$T\mathcal D\subset\mathcal D$，从而
$\operatorname{Dom}(T^2)=\mathcal D$。
保全部三项作乘法，
$$
T^2=R'^2+\Omega\eta R'
=D-\mu_0P_0-\Omega\psi_{\rm t}
=D-\Omega\psi=C\mathcal V
\quad\text{在 }\mathcal D.
\tag{17}
$$
每个 $R_j$ 可逆，所以 $\ker T=\mathbb C\Omega$。

由 (8)、(13)，有进一步的真来源
$$
\|TP_X\|_1
\le \tau_m,\qquad
\tau_m:=\sum_j(1+r^{-j})\sqrt{r_j}<\infty.
\tag{18}
$$
常数列为零，末列 $v_j$ 的范数至多
$\sqrt{r_j}+r^{-j}\sqrt{r_j}$，这付清 (18)。

## 4. 同域、闭性与实际非对称乘积

(5)、(12) 给关键的定义域身份
$$
\boxed{\quad
\mathcal U^{-1}(\mathcal D)=\mathcal V^{-1}(\mathcal D)=\mathcal D,\quad
\mathcal U\mathcal D=\mathcal D\cap\Omega^\perp,\quad
\mathcal V\mathcal D=\mathcal D.
\quad}
\tag{19}
$$
这里 $\mathcal U^{-1}(\mathcal D)$ 表示逆像，不表示 $\mathcal U$ 满射。
两个逆像身份分别因 $(\mathcal U-I)H\subset X\subset\mathcal D$ 与 $(\mathcal V-I)H=-LH\subset X\subset\mathcal D$。
$\mathcal U$ 和 $\mathcal V$ 均保持 $\mathcal D$；
用 (4) 对 $\mathcal D\cap\Omega^\perp$ 及 $\mathcal D$ 分别取原像，得其余两式。

定义
$$
S=T\mathcal U,\qquad \operatorname{Dom}S=\mathcal D.
\tag{20}
$$
这恰是自然乘积定义域，已由 (19) 支付。
若 $x_n\to x$、$Sx_n\to y$，
则 $\mathcal Ux_n\to\mathcal Ux$；
$T$ 闭给 $\mathcal Ux\in\mathcal D$、$T\mathcal Ux=y$，
再用 (19) 得 $x\in\mathcal D$。所以 $S$ 确闭。

又 $\mathcal U\mathcal D\subset\mathcal D$、$T\mathcal D\subset\mathcal D$，
故 $S\mathcal D\subset\mathcal D$。
所有下述自然乘积 $S\mathcal V$、$TS$、$T^2$ 的定义域均恰为 $\mathcal D$；
特别 $\operatorname{Dom}(TS)=\mathcal D$，没有漏掉内外层的域条件。
由 (4)、$TP_0=0$ 和 (17)，得到
$$
\boxed{
S\mathcal V=T,\qquad
TS=T^2\mathcal U=C\mathcal V\mathcal U=C
\quad\text{在 }\mathcal D.}
\tag{21}
$$
因 $\operatorname{Ran}\mathcal U\subset\Omega^\perp$、
$\ker T=\mathbb C\Omega$，$S$ 单射。
(19) 和 $T\Omega=0$ 给
$$
\operatorname{Ran}S=T(\mathcal D\cap\Omega^\perp)=T\mathcal D
=\operatorname{Ran}T.
\tag{22}
$$
原 $C$ 稠值且 $\mathcal D$ 在 $H$ 中稠密，故 $C\mathcal D$ 稠密。
(21) 给 $C\mathcal D\subset\operatorname{Ran}T$，
所以 (22) 的两个像都稠密。

最后，(5)、(18) 给
$$
S-T=T(\mathcal U-I)\ \text{有全域迹类延拓},\qquad
\|S-T\|_1\le3\tau_m.
\tag{23}
$$
因此 $S-R$、$T-R$ 都有有界迹类延拓。
$\mathcal D$ 上三者的图范数等价，原有限整块也是 $S,T$ 的图核心。
全部结论对每块任意平方根分支成立。

## 5. 此次返回的准确意义

本稿得到了原算子的完整双因子乘积
$$
\overline{TS}=C,\qquad
TS=C|_{\mathcal D},\qquad
S\mathcal V S=C|_{\mathcal D},
\tag{24}
$$
其中 $\mathcal D$ 同时对 $S,T,\mathcal U,\mathcal V,C$ 稳定。
最后一个稳定性也直接来自 $TS=C|_{\mathcal D}$。
原进位所有行列及非零秩一项已用 (1)–(21) 精确返回。

两个因子并不相同：
$T$ 有核 $\mathbb C\Omega$，$S$ 单射。
$\mathcal V$ 是满射有核的非交换因子，(24) 不能删除中间的 $\mathcal V$。
本稿没有证明 $ST=C$、$S^2=C$，也没有证明 $S$ 与原 $C$ 交换；
因此不能用 $S$ 的图直接产生原伴随矩阵的不变图。

这与已刊[最大本质图距](R12-appendix-walsh-root-maximal-essential-distance-and-no-bounded-angle.md)
没有冲突：此处支付的是两个不同的闭因子，而不是一个有界扰动的原平方根。
真正原闭根所需的两坐标相容或场外二次分子仍须继续支付。
