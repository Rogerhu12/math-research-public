# R556 — 原混合中央差的真实 carry 交支、两个 odd37 核与完整残差

日期：2026-11-14。**状态：已证明。**

本篇处理 R548 中原样保留的 $h(\Phi _1-\Phi _2)$，不把另一个
归一管的中央零用来替换它。先将它化为同一个原测试的 native
反对称行，再把 R536 的确切三支 carry 与其反射逐点相交。
共同部分准确只有两个范数为 $37$ 的真实方向；它们改变原 $Y$，
所以第一权、四个 Mellin 单位条件和全部 $\kappa^{-n}$ 一并运输。

细分同一固定 ray 后，两个方向在 $\rho _0,\eta,h$ 上均有
绝对标量核心 $\beta=-\lambda$。在共同 carry 上用此核心归一，
所有事件严格下降到五个正交伴随，自由的第六变量可以作真正的
完整 Mellin 展开。两个独有支、常数 log 质量及原补域均保留。
另外给出原反证条件控制的**同一 native 总行**，以及一个明确
深交域上实际残差的严格一阶公式。

## 1. 同一个来源、确切 q 与原测试

全部规范沿用 R536、R541、R544、R548、R553、R557。
特别
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
b=17,\quad \lambda=-\bar\pi _0^{-1},\quad
\beta=-\lambda,\quad \kappa=p\lambda^2,\quad d=p-1.
\tag{1}
$$
$p\ge71$ 属于原普通 ray，原全部固定坏集仍删除。
本篇的 $Y$ 是未双倍的原观察 $Y_s$，不与 R548 的 $2Y_s$ 混用。

原输入是 $(\xi _1,\xi _2,\xi _3,x,c,d_0)$，并设
$$
\begin{aligned}
A&=\delta\xi _1+2\delta\xi _2+(3+\omega)\xi _3+(2-\omega)x,\\
Y&=A+c+2d_0,\qquad W=A+3\delta c+4d_0,\\
M&=c+(2+3\omega)d_0,\qquad
L=(1+3\omega)c+d_0=(W-Y)/2.
\end{aligned}
\tag{2}
$$
令
$$
\rho _0=-\nu_\sigma^{\otimes6}/84,\qquad
\eta=\omega^2H_*\rho _0,\qquad h=\eta+\rho _0/2,\qquad
\Delta=\rho _0-\eta.
\tag{3}
$$
$H$ 是 R541 的同一个真实二乘二酉矩阵，固定前四输入。
$R_c$ 只反射 $c$。本篇 $h$ 不是 R536 §9 的旧三阶来源。

以下使用 R536 的完整行
$$
\begin{aligned}
C&=(\xi _1-\xi _3+x)/\delta,\\
D_4&=\xi _1+\omega^2\xi _2-2\omega\xi _3,\qquad F=D_4+C+M,\\
H_1&=-\xi _1+2\xi _2+\omega\xi _3+(1+\omega)x,\\
G&=13H_1+(3-2\omega)F .
\end{aligned}
\tag{4}
$$
写 $\zeta_j=\omega^{2j}$，
$$
D_j=F-\zeta_jC,\quad E_j=F+13\zeta_jC,\quad
\Gamma_{n,j}=\{C,F\ {\rm unit},D_j\in p^n\},\quad
\Gamma_n^{(3)}=\coprod_{j=0}^2\Gamma_{n,j}.
\tag{5}
$$
令 $\widehat P_p=\mathcal R_pP_p$ 为 R536 已付的准确六次多项式，
所有 $u_j=(1+\lambda\kappa^j)^{-1}$、七行右逆和 $p$ 依赖完整保留。
实际测试是
$$
\boxed{
q=\mathfrak q_{n,p}
=\frac1{3b\Omega^6}\sum_{j=0}^2
1_{\Gamma_{n,j}}\,
\widehat P_p(D_j/\kappa^n,E_j,G),\qquad n\ge1.
}
\tag{6}
$$
域外按零延拓。此后不将 $q$ 换成任意多项式。

记
$$
\ell=1_{Y\ {\rm unit}}d\log\langle Y\rangle
      -1_{W\ {\rm unit}}d\log\langle W\rangle,\qquad
a=q\ell,\qquad f=1_{L\ {\rm unit}}a.
\tag{7}
$$
再令 $u=u_1=(\omega c+(1-\omega)d_0)/2$、
$P_1=P_{u,\kappa}$，$\Phi_j=f\circ P_j$ 仍取 R544 的三个实际轴。

R557 的完整结论是
$$
(\pi_4)_*(q\mu)=\beta^n(\pi_4)_*\mu,\qquad
\pi_4=(Y,W,W',G),\quad \mu=\rho _0,\eta,h.
\tag{8}
$$
(8) 不允许额外添加不属于 $\pi_4$ 的 $u$ 条件。
特别它没有给 $\eta$ 或 $h$ 的未知中央赋零。

## 2. 同一 native 反对称行的原算术返回

R544 的完整两态矩阵给
$$
(R_c)_*\rho _0=-\rho _0,\qquad (R_c)_*\eta=\rho _0+\eta,
$$
$$
\Delta-(R_c)_*\Delta=3\rho _0.
\tag{9}
$$
因此对**同一个** (7) 的实际测试，准确有
$$
\boxed{
\Delta(a-a\circ R_c)
=3\rho _0(a)
=3\beta^n\{J'_S(0)-6\delta J'_T(0)\}.
}
\tag{10}
$$
最后一步只使用原 $Y_*\rho _0=S$、$W_*\rho _0=6\delta T$
和 (8)。不是先换成 $q\circ P_j^{-1}$ 的另一条权。
在原 $J'_S=J'_T=0$ 反证条件下，(10) 的完整 native 总行为零。

同一两态矩阵还给 $K_u\Delta=2h$；外部标量仍是 $\lambda$，所以
$$
\boxed{\Delta|_{\{u\in p\}}=2\lambda(P_1)_*h.}
\tag{11}
$$
R548 的完整反射关系及 $u_1R_c=\omega^2u_2$ 给
$$
h(\Phi_1-\Phi_2)=h((f-f\circ R_c)\circ P_1).
\tag{12}
$$

在 $u\in p$ 上，直接解原行得到
$$
c=(2+\omega)d_0+2\omega^2u,\qquad
L=4\omega d_0+2(2-\omega)u,
$$
$$
L\circ R_c=2(1-2\omega)d_0-2(2-\omega)u.
\tag{13}
$$
由于 $p>19$，$N(1-2\omega)=7$ 为单位，故
$$
u\in p:\qquad L\ {\rm unit}\ \Longleftrightarrow\
L\circ R_c\ {\rm unit}\ \Longleftrightarrow\ d_0\ {\rm unit}.
\tag{14}
$$
置 $\mathcal B=\{u\in p,\ L\ {\rm unit}\}$。结合 (11)–(14)，得到
本篇的实际接口
$$
\boxed{
h(\Phi_1-\Phi_2)
=\frac1{2\lambda}\int_{\mathcal B}(a-a\circ R_c)\,d\Delta.
}
\tag{15}
$$
它与 (10) 是同源、同一反对称测试的局部行和总行。

这里不能由 (10) 删除 $\mathcal B$ 的补域。精确地，
$\{u\in p,L\in p\}=\{c,d_0\in p\}$，且后者在 $R_c$ 下稳定。
因此原两中央零时，(15) 等价于
$$
\boxed{
h(\Phi_1-\Phi_2)
=-\frac1{2\lambda}\int_{\{u\ {\rm unit}\}}(a-a\circ R_c)\,d\Delta
-\frac3{2\lambda}\int_{\{c,d_0\in p\}}a\,d\rho _0.
}
\tag{16}
$$
这是完整补域，没有省略第三来源的未控部分。

第二项已经是原六 sigma 来源。记 $S_\kappa$ 只共同缩放 $(c,d_0)$，
则其准确式为
$$
\boxed{
\int_{\{c,d_0\in p\}}a\,d\rho _0
=\beta^2\int_{A\ {\rm unit}}
(q\circ S_\kappa)\,
d\log\frac{A+\kappa(c+2d_0)}
             {A+\kappa(3\delta c+4d_0)}\,d\rho _0.
}
\tag{17}
$$
两分母和分子单位域同为 $A$ 单位。$q\circ S_\kappa$ 的全部 carry
及 $\kappa^{-n}$ 保留。
其 log 可以在这个真实域展开为
$\log(1-2\kappa L/(A+\kappa(3\delta c+4d_0)))$；
没有借此把其积分认作原完整中央。

## 3. 原 q 与反射 q 的全部真实交支

记
$$
F'=F\circ R_c=F-2c,\qquad
G'=G\circ R_c=13H_1+(3-2\omega)F',\qquad
q_c=q\circ R_c,\quad \ell_c=\ell\circ R_c.
\tag{18}
$$
$C,D_4,H_1,A$ 都不含 $c,d_0$。

在 $\mathcal B$ 中，(13)–(14) 给 $c,d_0$ 均单位。
若原 $q$ 和反射 $q_c$ 同时可能非零，则
$F^3\equiv F'^3\equiv C^3\pmod {p^n}$，$C,F,F'$ 均单位。
三个立方根的差为单位，而 $F'-F=-2c$ 是单位。
故 $\tau=1$ 这一支严格不可能；唯一可能的两支是
$$
\boxed{
J_\tau=(1-\tau)F-2c=F'-\tau F\in p^n,
\qquad \tau=\omega,\omega^2.
}
\tag{19}
$$
两支互不相交。这个论证保深度 $n$，不只是模 $p$ 的必要条件。

定义
$$
\mathcal C_{\tau,j,n}
=\mathcal B\cap\Gamma_{n,j}\cap\{J_\tau\in p^n\},
\qquad
\mathcal C_{\tau,n}=\coprod_j\mathcal C_{\tau,j,n},
$$
$$
\mathcal A_+=\mathcal B\cap
(\Gamma_n^{(3)}\setminus R_c\Gamma_n^{(3)}),\qquad
\mathcal A_-=\mathcal B\cap
(R_c\Gamma_n^{(3)}\setminus\Gamma_n^{(3)}).
\tag{20}
$$
因此 (15) 的整个非零候选支撑准确分成两个独有支和两个共同支：
$$
\boxed{
\begin{aligned}
2\lambda\,h(\Phi_1-\Phi_2)
={}&\int_{\mathcal A_+}q\ell\,d\Delta
-\int_{\mathcal A_-}q_c\ell_c\,d\Delta\\
&+\sum_{\tau=\omega,\omega^2}\int_{\mathcal C_{\tau,n}}
(q\ell-q_c\ell_c)\,d\Delta .
\end{aligned}}
\tag{21}
$$
多项式在某些点自行消失不影响此分区；没有假设在支撑内处处非零。

在 $\mathcal C_{\tau,j,n}$ 中，令 $k$ 唯一满足
$\zeta_k=\tau\zeta_j$。于是 $k\ne j$，六个 $(j,k)$ 都是真实
交支。全部权的准确变换是
$$
\boxed{
D_k'= \tau D_j+J_\tau,\quad
E_k'=\tau E_j+J_\tau,\quad
G'=\tau G+13(1-\tau)H_1+(3-2\omega)J_\tau .
}
\tag{22}
$$
由 $\widehat P_p$ 六次齐次及 $\tau^6=1$，在该支上
$$
\boxed{
q_c=\frac1{3b\Omega^6}\widehat P_p\left(
\frac{D_j}{\kappa^n}+\frac{\tau^{-1}J_\tau}{\kappa^n},
E_j+\tau^{-1}J_\tau,
G+13(\tau^{-1}-1)H_1+(3-2\omega)\tau^{-1}J_\tau
\right).
}
\tag{23}
$$
这是同一个 R536 准确多项式，没有丢掉 $J_\tau/\kappa^n$。
$H_1$ 无任何自动深度限制；即使 $J_\tau$ 深 $n$，
(23) 的第一平移仍一般是单位阶。

## 4. 两个实际 odd37 方向及固定 ray

采用 Hermitian 行内积 $\langle r,s\rangle=r\bar s^{\,t}$。
(4) 给 $N(F)=13$、$\langle F,c\rangle=1$。
因此
$$
N(J_\tau)=37,\qquad
\langle J_\tau,C\rangle=0,\qquad
\langle Y,J_\tau\rangle=-2,\quad
\langle W,J_\tau\rangle=-6\delta.
\tag{24}
$$
它们确实改变原第一观察。

两个原整行及乘 $H$ 后的整行为
$$
\begin{array}{c|rrrrrr}
 &\xi_1&\xi_2&\xi_3&x&c&d_0\\ \hline
J_\omega&
-2\omega&-2-\omega&-1-3\omega&-1-\omega&-1-\omega&5+4\omega\\
J_{\omega^2}&
2&-1-2\omega&2-\omega&-\omega&\omega&1+5\omega\\
J_\omega H&
-2\omega&-2-\omega&-1-3\omega&-1-\omega&3+5\omega&-1-2\omega\\
J_{\omega^2}H&
2&-1-2\omega&2-\omega&-\omega&-1+3\omega&3 .
\end{array}
\tag{25}
$$
每行恰有五个非零模二系数，故均给相同的标准 odd37 半特征。
(25) 已支付 $\eta$ 的半整数 $H$ 在本轴上的完整消分母；
其余五方向若需 $[2]$ 覆盖，不改变本轴的 degree 或半特征。

现将原固定 ray 细分为
$$
\boxed{\pi_0\equiv1\pmod {37}.}
\tag{26}
$$
这与全部旧条件兼容。确切地，设旧模数为 $M_{\rm old}$，
旧实际代表为 $\pi_*$；已有模数的素因子中无 $37$。
在 $\mathcal O_K/37$ 中取
$$
t\equiv(1-\pi_*)M_{\rm old}^{-1}\pmod {37},
\qquad
\pi_{\rm new}=\pi_*+M_{\rm old}t.
\tag{27}
$$
它是模 $37M_{\rm old}$ 的单位类，保持所有旧 primary 和普通规范，
并在 $37$ 上为一。原 ray-class/Chebotarev 论证应用于这一固定类，
仍给无穷多个不同的普通有理素数；只继续删除既有有限坏集和 $37$。
这是固定有限细分，不随 $p,n$ 或未来测试变化。

同时保 R558 已固定的 $\pi_0\equiv-1\pmod{M_3}$ 及 $p\nmid C_3$。
其整数 $M_3$ 满足 $M_3\equiv1\pmod{37}$，故 (27) 对含该条件的
旧模数仍合法。这里沿用 R558 已给出的 $N_0,M_3$，不因本篇新增
$37$ 而重新定义它们。两篇合用仍是同一个固定无限 ray。

**定理1。** 在 (26) 的同一 ray 上，对
$\mu=\rho _0,\eta,h,\Delta$ 和全部 $m\ge0$，
$$
\boxed{
\mu|_{\{J_\tau\in p^m\}}
=\beta^m(P_{J_\tau,\kappa^m})_*\mu,\qquad
\tau=\omega,\omega^2.
}
\tag{28}
$$
其余五变量及全部真实测试保持。

**证明。** 原奇半特征的完整 theta 群规范使用模 $2N$。
(26) 与原模二条件给
$g_\pi=\pi_0/\bar\pi_0\equiv1\pmod {74}$。
因此在 odd37 的完整 Heisenberg 表示上，两生成元及其中心均逐个固定。
特别其 $37$ 次幂的奇半特征负号没有因只看模 $37$ 而遗漏。
不可约性迫整个 $K_{37}$ 为同一个标量。

真实锚为 $\sigma(\gamma_{37}z)$，
$\gamma_{37}=7+3\omega$，$N(\gamma_{37})=37$。
$\gamma_{37}$ 模二非零，故其拉回恰属于这个标准 odd37。
因 $\gamma_{37}$ 在当前 $p$ 为单位，它的完整测度核心由原 sigma
直接为 $\beta$；所以整个 odd37 的绝对标量就是 $\beta$，
不是另一个未定的二次号。

(25) 及正交 Gram 消去证明每个来源沿本轴都属于此完整 odd37
与其余系数空间的张量格。逐系数使用已定标的 whole 核即得 (28)；
线性组合给 $h,\Delta$。没有由边际非零或有限素数取样定相位。证毕。

另有准确几何
$$
\operatorname{Gram}(J_\omega,J_{\omega^2})
=\begin{pmatrix}37&-35\omega\\-35\omega^2&37\end{pmatrix},
\quad\det=144,\qquad
J_\omega+\omega J_{\omega^2}=2\omega^2c,
$$
$$
J_\tau R_c=-\tau J_{\tau^{-1}}.
\tag{29}
$$
两轴不正交；(28) 不允许把任意两次限制当成交换的独立矩形。
在 $\Gamma_n^{(3)}$ 上，两轴同时深 $n$ 会迫 $F,c$ 都深，
所以确实被 $F$ 单位排除。

## 5. 新核心使共同区域真正下降到五伴随

固定 $\tau,j,n$，记 $J=J_\tau$。对任意原行 $r$ 定义
$$
r_\perp=r-\frac{\langle r,J\rangle}{37}J,\qquad
a_r=\frac{\langle r,J\rangle}{37}.
\tag{30}
$$
令 $t=J(\xi)$，则原格在 $p$ 处正交分裂为 $\xi_\perp$ 与自由 $t$。
$37$ 为单位，所以这一分裂在原整格中没有损失；
其他五方向可选任意完整整基。

写 $P=P_{J,\kappa^n}$。所有行准确运输为
$$
r(P\xi)=r_\perp(\xi_\perp)+\kappa^n a_rt.
\tag{31}
$$
在 (20) 的共同支中，$J(P\xi)=\kappa^nt$ 自动深 $n$。
因为 $n\ge1$，实际事件逐项严格等价：
$$
\boxed{
P^{-1}\mathcal C_{\tau,j,n}
=\mathcal E_{\tau,j,n}\times\mathbb Z_p,
}
$$
$$
\boxed{
\mathcal E_{\tau,j,n}
=\{\,C\ {\rm unit},\ u_\perp\in p,\ L_\perp\ {\rm unit},\
F_\perp-\zeta_jC\in p^n\,\}.
}
\tag{32}
$$
$F(P\xi)$ 单位由最后一条件和 $C$ 单位自动得到。
(32) 中没有条件依赖自由 $t$。
特别 $u$ 深仅是深一，不被擅自提高为深 $n$。

同样，四个原 Mellin 单位条件准确成为
$$
Y_\perp,\quad W_\perp,\quad (Y\circ R_c)_\perp,\quad
(W\circ R_c)_\perp\quad\hbox{各自单位},
\tag{33}
$$
因为在每一行中被加回的 $\kappa^na_rt$ 都深。
这些是四个不同的条件；没有把它们相认。

为显示完整第一权，(24) 及反射行给
$$
\begin{aligned}
Y(P\xi)&=Y_\perp-\frac{2\kappa^n}{37}t,&
W(P\xi)&=W_\perp-\frac{6\delta\kappa^n}{37}t,\\
(Y\circ R_c)(P\xi)&=(Y\circ R_c)_\perp+
 \frac{2\tau^{-1}\kappa^n}{37}t,&
(W\circ R_c)(P\xi)&=(W\circ R_c)_\perp+
 \frac{6\delta\tau^{-1}\kappa^n}{37}t.
\end{aligned}
\tag{34}
$$
核心没有固定 $Y$；(34) 正是不能省略的变化。

原 $q$ 的准确输入为
$$
\boxed{
(q\circ P)(\xi)=\frac1{3b\Omega^6}
\widehat P_p\left(
\frac{F_\perp-\zeta_jC}{\kappa^n}+a_Ft,\
F_\perp+13\zeta_jC+\kappa^na_Ft,\
G_\perp+\kappa^na_Gt
\right),
}
\tag{35}
$$
其中
$$
a_F=(11-13\tau^{-1})/37,\qquad
a_G=-2(3-2\omega)/37.
$$
反射的 $q_c\circ P$ 必须将 (23) 全式再按 (31) 代入；
特别其中 $J/\kappa^n$ 变成自由的 $t$，$H_1$ 变成
$H_{1,\perp}+\kappa^na_{H_1}t$。
故两权都是自由 $t$ 的至多六次整多项式，但一般不相等。

(28) 于是给完整共同项
$$
\boxed{
\int_{\mathcal C_{\tau,j,n}}(q\ell-q_c\ell_c)\,d\Delta
=\beta^n\int_{\mathcal E_{\tau,j,n}\times\mathbb Z_p}
\{(q\ell-q_c\ell_c)\circ P\}\,d\Delta.
}
\tag{36}
$$
这一次事件确实与自由积分轴分离；来源本身不被假定为独立乘积。
所有归一后的正交伴随域在 (32) 内明确保留。

## 6. 自由 odd37 轴上的完整条件展开

沿 (32) 的自由 $t$，可使用整个 odd37 的标准整基
$$
B_j(z)=
\begin{cases}
\sigma(z)^{37}x_\wp(z)^{(37-j)/2},&j=1,3,\ldots,37,\\
-\sigma(z)^{37}y_\wp(z)x_\wp(z)^{(34-j)/2},&j=0,2,\ldots,34,
\end{cases}
\tag{37}
$$
其中 $y_\wp=\wp'/2$。其首项均为 $z^j$。
指标集合为 $\mathcal I=\{0,1,\ldots,35,37\}$，恰三十七个；
不能误用只有 $0,\ldots,36$ 的 jet 来漏掉 $\sigma^{37}$。

因此整个来源沿 $J$ 有唯一完整分离
$$
\Delta=\sum_{j\in\mathcal I}\nu_{B_j}\otimes\Lambda_{\tau,j}.
\tag{38}
$$
这里 $\Lambda_{\tau,j}$ 是实际五变量条件来源，不给它们另加算术
身份或单位质量。它们整有界：基 (37) 是原整 theta 格中的全纯
基，而按首次数消元只需 $j!\Omega^j$、$j\le37$；
当前 $p\ge71$ 使这些三角分母均为单位。
全部高矩因此由同一三十七个条件来源决定，不再增加隐藏输入。

在 (33) 某行 $r_\perp$ 单位的区域，准确且一致收敛地
$$
d\log\langle r_\perp+\kappa^na_rt\rangle
=d\log\langle r_\perp\rangle
+d\sum_{m\ge1}\frac{(-1)^{m+1}}m
 \left(\frac{\kappa^na_rt}{r_\perp}\right)^m.
\tag{39}
$$
将 (35) 与反射的完整六次多项式乘入 (39)，即可对自由 $t$ 逐项
积分；每一项是 (38) 的真实条件矩和原伴随测试。
截到 $m=R$ 后，余项赋值统一至少
$$
\boxed{(R+1)n-\lfloor\log_p(R+1)\rfloor.}
\tag{40}
$$
理由是所有其余系数和事件均整，且
$mn-\lfloor\log_pm\rfloor$ 对 $m\ge1$ 单调不减。

(39) 的常数 log 项乘的是完整加权条件质量
$\int(q\circ P)\,d\Delta(t,\xi_\perp)$ 或其反射版本。
它们一般不为零。R557 在原 $\mathcal D_n$ 上证明的零质量不能
搬到 (32)。这里把这些常数项连同所有四个独立单位条件保留。

## 7. 原 carry 不强迫第一四输入深：四条真实 Mellin 边界

在前四输入上，完整框架 $(C,D_4,H_1,A)$ 的行列式是
$$
17+3\omega,\qquad N(17+3\omega)=247=13\cdot19.
\tag{41}
$$
它在当前处为单位。所有 (5)、(18)–(23) 的 carry 和 $u$ 条件
都不涉及这个框架中的 $A$。
所以它们在集合意义上不限制 $A$，更不能推出四个原 sigma 都深。
此处仅说真实事件的自由坐标，不把前四个 sigma 的来源说成独立乘积。

由 (13)，四个原观察准确为
$$
\begin{aligned}
Y&=A+(4+\omega)d_0+2\omega^2u,\\
W&=A+(4+9\omega)d_0+6(1-\omega)u,\\
Y\circ R_c&=A-\omega d_0-2\omega^2u,\\
W\circ R_c&=A+(4-9\omega)d_0-6(1-\omega)u.
\end{aligned}
\tag{42}
$$
在 $\mathcal B$ 中 $u$ 深、$d_0$ 单位；四个非单位边界的模 $p$
根 $A/d_0$ 依次为
$$
\boxed{-4-\omega,\quad-4-9\omega,\quad\omega,\quad-4+9\omega.}
\tag{43}
$$
六个两两差的范数为
$$
64,\ 12,\ 100,\ 76,\ 324,\ 112 .
$$
所以当前 $p>19$ 下四条边界两两不交。真实残差是四个单边界区域
加四行全单位区域，不能给整个 strip 一个公共 Mellin 单位条件。

在四行全单位区域，准确有
$$
\ell-\ell_c
=d\log\frac{Y(W\circ R_c)}{W(Y\circ R_c)}.
\tag{44}
$$
在其余四个边界各有相应指示函数消去一项，仍按 (7)、(18) 原样读；
(21)、(36) 对这些边界都成立。

## 8. 同一实际混合 f 的严格一阶残差

定义真正的共同伴随
$$
\boxed{
Z_* =W-3\delta Y=(1-3\delta)A+(4-6\delta)d_0.
}
\tag{45}
$$
它不含 $c$，在 $R_c$ 下固定；它同时正交于两个 $J_\tau$，
以及原 $C,F,G$ 三方向。$N(Z_*)=936$，
本篇不为它增加未付单轴核心。

在 $\mathcal B$ 内，若 $Z_*\in p^r,\ r\ge1$，则四个 (42) 全部单位。
例如若 $Y$ 深，由 $W=3\delta Y+Z_*$ 知 $W$ 也深，
这与 $W-Y=2L$ 单位矛盾。反射的两行由 (14) 同理。
因此 (44) 在这个真域自动有效，并且
$$
\boxed{
\ell-\ell_c
=d\log\left(1+\frac{2cZ_*}{W(Y\circ R_c)}\right).
}
\tag{46}
$$
分子除 $Z_*$ 外均单位，所以当 $Z_*\ne0$ 时，(46) 的逐点赋值
恰为 $v_p(Z_*)$；$Z_*=0$ 时两边同时为零。

进一步保真实深交域
$$
\mathcal K_{\tau,j;n,r}
=\mathcal C_{\tau,j,n}\cap
\{J_\tau\in p^{n+r},\ H_1\in p^r,\ Z_*\in p^r\},
\qquad r\ge1.
\tag{47}
$$
(23) 的三个完整平移量此时都在 $p^r$：
第一项使用 $J_\tau/\kappa^n$，其深度恰至少 $r$；
其他两项保 $H_1$ 和 $J_\tau$。
由于 $\widehat P_p$ 及全部参数系数整，
$$
\boxed{q_c-q\in p^r\mathcal O\quad\hbox{逐点于 }(47).}
\tag{48}
$$
这没有把 $J_\tau$ 仅深 $n$ 的一般共同支误当成误差小。

写 $q\ell-q_c\ell_c=q(\ell-\ell_c)+(q-q_c)\ell_c$。
单位 log 属于 $p\mathcal O$；(46) 的平方及以上项在 $p^{2r}$。
故在 (47) 的**原 native 测试**上严格有
$$
\boxed{
q\ell-q_c\ell_c
\equiv\frac{2d\,q\,c\,Z_*}{W(Y\circ R_c)}
\pmod {p^{r+1}}.
}
\tag{49}
$$
对 (47) 任意附加的真实紧开子域，以 $\Delta$ 积分仍保此界，
因为来源整有界，且 (15) 的 $2\lambda$ 是单位。
(28) 的核心也保 $Z_*$，所以 (49) 可与 (36) 同时使用，
只需完整转置 $H_1$ 和其余事件。

(49) 是实际原混合行的固定一阶负矩接口；它没有把右侧的积分
认成单位，更没有由逐点非零推出积分非零。
(47) 外的共同部分、(21) 的两个独有支、(43) 的各边界仍存在。

## 9. 本篇支付的连接与保留的终局条件

本篇给出的原算术输入是 (10) 的同一 native 总行；
所需实际局部项是 (15)，其全补域精确在 (16)–(17)。
共同 carry 的六个 $(j,k)$ 交支压成两条真实 odd37 轴，
其完整半特征、固定 ray、绝对核心和原 $Y/W$ 变化均在 (24)–(36)。
应用核心后，共同支的整个事件确实下降到五伴随，得到 (38)–(40)
的完整条件展开，而非先删 cut 再作形式 Taylor 展开。
(49) 另给同一实际测试在显示深交域上的严格赋值余项。

尚须控制 (21) 的独有支、一般共同支的常数 log 质量以及
(16) 的完整补域，或对 (49) 的同源首行给出足够的整体关系。
本篇没有把第三来源的未知中央或十二条外谱赋零；
也没有把非零子域、whole scalar 核或有限条件空间当成主目标完成。

## 依赖与精确证书

- [R536：原七行右逆和确切三支测试](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)。
- [R544：完整 S3 核与原混合测试](R544-original-s3-and-exact-mixed-unit-complement.md)。
- [R548：整来源反射及全谱](R548-original-whole-third-source-cm-reflection-and-complete-positive-spectrum.md)。
- [R553：原 Norm2 双张量与实际单位域](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)。
- [R557：同一 q 对第三来源的完整返回](R557-third-source-common-carry-zero-mass-and-central-rows.md)。
- [R558：同一固定无限单位 ray](R558-third-source-exact-second-order-and-common-affine-unit-ray.md)。
- [精确脚本](../scripts/check-r556-native-carry-odd37-intersections.js)。
- [完整坐标、Gram、半特征及边界证书](../scripts/check-r556-native-carry-odd37-intersections.json)。

证书使用 BigInt 的 $\mathbb Q(\omega)$ 精确运算，直接核 (22)、
(24)–(25)、(29)、(41)–(43)、(45) 的全坐标，含反射后原观察的
全部系数。它不重做 R536 的右逆，也不以数值秩或样本素数代替证明。
