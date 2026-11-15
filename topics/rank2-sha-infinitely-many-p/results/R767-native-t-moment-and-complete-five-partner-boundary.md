# R767 — 原 t 首行的完整五伙伴收缩、纯 rank-one 来源及浅域四核

日期：2026-11-15。**状态：已证明。**

沿 R764 的同一个最终测试 $q_N^*$，本文支付三个可同时使用的完整结果。

首先，原正一 t 矩的整个 Y 来源恰为 $-22D_{\omega,17}/21$，没有 primitive 余项；最终 q 只给它乘原 $\beta^N$。因此每个完整 t 环带的真实 Y-unit 负一行都非零。

其次，对 R764 共同外部域，t 可以合法收缩而保留全部五个伙伴，所得来源有显示的二张量式。对仍含 t 的浅独占域，不能使用这个边界代替整联合；本文给出同一原来源的完整四核公式处理它们。

最后，每条实际条件 Y 来源的全部五个坐标，准确由原正 $5,11,17,23,29$ 矩经固定单位三角逆读取；两条算术线和全部三维 primitive 块均保留。整个有限分割的坐标之和是显示的纯 $D_\omega$ 向量。这个非零总行没有被混同于原 $J'_S$ 或 $J'_T$。

## 1. 原完整框架与可用的 C 平均

保 R764 的参数、全部原普通射线与最终整逆：
$$
b=17,\quad\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0},\quad q=q_N^*.
\tag{1}
$$
原来源仍为
$$
e_0=-\nu_\sigma^{\boxtimes6}/84,\qquad
h_W=\omega^2\mathcal T_*e_0.
$$
使用 R764 的整数框架
$$
S=\delta\mathfrak s,\quad T=\delta\mathfrak t,\quad
C_0=\delta C,\quad B=\mathfrak B,\quad \xi_2,\quad d.
\tag{2}
$$
这是实际输出 $S,T$，不与原单变量曲线来源 $S_{34},T_{72}$ 混用。
六个度数为 $6,6,3,3,1,1$，全部半特征及其绝对核心已经由 R764 支付。

在这五/六输出中，原权和观察的准确式为
$$
\begin{aligned}
C&=C_0/\delta,\\
F&=S/\delta-B+\omega^2\xi_2+(2+3\omega)d,\\
G&=13B+26\xi_2+(3-2\omega)F,\\
Y&=-\frac{4\delta}{3}B+2\delta\xi_2+S/\delta+2d,\\
P&=-\frac{4\delta}{3}B+2\delta\xi_2
       +(2+3\omega)S/\delta+4d .
\end{aligned}
\tag{3}
$$
q 的每个真实六支都是把 $F-\zeta C$、$F+13\zeta C$、
G 代入原完整次数逆后求 $\zeta\in\mu_6$ 的和。
故纯 $C_0\mapsto\epsilon C_0$，其余五输出不动时，
$$
q\circ P_{C_0,\epsilon}=q\qquad(\epsilon\in\mu_6).
\tag{4}
$$
R764 的 Y、P、全部三 CD/O 条件、E 或 $E_\perp$ 条件都不含 $C_0$。
所以在这些**实际测试**中，可以对来源施加整个六角平均
$$
\mathscr P_C=\frac16\sum_{\epsilon\in\mu_6}(P_{C_0,\epsilon})_*.
\tag{5}
$$
这来自逐点换元 (4)，不从某个边际质量推断。
若后续加入不保 (4) 的测试，应使用下一节未平均的全式。

## 2. 三 sigma 的完整 Hesse 恒等式

用 $(u,v,w,z)$ 表示 (2) 前四个实际输出的生成变量。
原四个选定 sigma 的生成函数准确为
$$
G(u+v;w,z)\,\sigma(\delta(u-v)),
$$
其中
$$
\boxed{
G(r;w,z)=-\prod_{j=0}^{2}
 \sigma(r+\omega^jw-\omega^{-j}z).
}
\tag{6}
$$
前面的负号是原三个系数 $1,-\omega^2,\omega$ 的乘积，必须保留。

记原 odd degree 3 基为
$$
P_3=\sigma^3,\qquad Q_1=x_b\sigma^3,\qquad B_3=-y_b\sigma^3.
\tag{7}
$$
它们的首项依次为 $z^3,z,1$，型依次为 $3,1,0$。
定义
$$
\Psi(w,z)=B_3(w)B_3(z)+3bP_3(w)P_3(z),\qquad
\Pi(w,z)=P_3(w)B_3(z)-B_3(w)P_3(z).
$$
则整个三变量恒等式为
$$
\boxed{
G(r;w,z)
=-\Psi(w,z)P_3(r)
 -3Q_1(w)Q_1(z)Q_1(r)
 -\Pi(w,z)B_3(r).
}
\tag{8}
$$

**证明。** 三个平移和为零；每个轴都是标准 odd degree 3，交叉极化消失。因此 G 在整个
$(\mathcal S_3^{\rm odd})^{\boxtimes3}$ 中。
按 r 的完整三基展开，r 的 $P_3,Q_1,B_3$ 系数的总型分别为 $0,2,3$，相应伙伴空间分别是
$$
\langle B_3\otimes B_3,\ P_3\otimes P_3\rangle,\quad
\langle Q_1\otimes Q_1\rangle,\quad
\langle P_3\otimes B_3,\ B_3\otimes P_3\rangle .
$$
在 $r=0$，三倍 CM 加法式给
$$
\prod_{j=0}^2\sigma(w-\omega^jz)
=\sigma(w)^3\sigma(z)^3(y_b(w)-y_b(z))
=\Pi(w,z).
$$
由于 $B_3(0)=1$，这定出 (8) 最后一项。
在 $w=z$，(6) 为
$-\sigma(r)\sigma(r+\delta w)\sigma(r-\delta w)$。
原两点加法及
$$
\sigma(\delta w)=\delta x_b(w)\sigma(w)^3,\qquad
\Theta(\delta w)=(x_b(w)^3+4b)\sigma(w)^6
$$
分别定出 Q 系数 $-3Q_1(w)^2$ 和 P 系数
$-B_3(w)^2-3bP_3(w)^2$。再用 $w=z=0$ 定标，
得到 (8) 的全部常数。因使用完整有限空间，这证明整个函数，而非只验有限个 Taylor 系数。证毕。

## 3. 六度外积与完整浅域四核

保 R533 的整基
$$
f_1=-x_by_b\sigma^6,\quad f_3=-y_b\sigma^6,\quad
f_4=x_b\sigma^6,\quad f_2=x_b^2\sigma^6,
$$
$$
H=(x_b^3-2b)\sigma^6,\qquad h_6=\sigma^6.
\tag{9}
$$
对两个变量 u、v，写 $F\wedge G=F(u)G(v)-G(u)F(v)$，并定义
$$
K_P=H\wedge f_4+2f_1\wedge f_3,\qquad
K_B=H\wedge f_1+6b f_3\wedge f_4,
$$
$$
K_Q=(H+6bh_6)\wedge f_2 .
\tag{10}
$$
R533 的完整两核和原 sigma 加法式准确给
$$
\boxed{
\begin{aligned}
P_3(u+v)\sigma(\delta(u-v))&=-\delta K_P(u,v),\\
B_3(u+v)\sigma(\delta(u-v))&=-\delta K_B(u,v),\\
Q_1(u+v)\sigma(\delta(u-v))&=-\delta K_Q(u,v).
\end{aligned}}
\tag{11}
$$
前两式用 $a=2+\omega=-\omega\delta$ 及
$\omega^2a=-\delta$ 从 R533 搬来，保实际方向号。
第三式由
$\sigma(\delta u)^2\sigma(\delta v)^2
 [x_b(\delta v)-x_b(\delta u)]/\delta$
直接化简；它包含 $H+6bh_6$，未丢质量项。

结合 (8)、(11) 和原 $-1/84$，整个未平均来源为
$$
-\frac{\delta}{84}\,
 \sigma(\xi_2^\vee)\sigma(d^\vee)
 \{\Psi K_P+3Q_1(w)Q_1(z)K_Q+\Pi K_B\}.
\tag{12}
$$
这里 $\xi_2^\vee,d^\vee$ 只是对应生成变量，不是新的输出。

对 (12) 施加合法的 (5)：
$B_3(w)$ 保留，$P_3(w),Q_1(w)$ 被杀。
于是得到**完整六输出**恒等式
$$
\boxed{
\mathscr P_C e_0
=-\frac{\delta}{84}\,
 \nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)
 \boxtimes
 \{B_3(B)K_P(S,T)-P_3(B)K_B(S,T)\}.
}
\tag{13}
$$
(13) 中函数乘积均表示不同实际输出上的张量来源；
可施加任意同 (4) 相容的原混合切集。

特别，按 T 的完整来源展开，令
$$
\begin{aligned}
U_0(S,B)&=f_4(S)B_3(B)-f_1(S)P_3(B),\\
U_1(S,B)&=2f_3(S)B_3(B)+H(S)P_3(B),\\
U_3(S,B)&=-2f_1(S)B_3(B)-6b f_4(S)P_3(B),\\
U_4(S,B)&=6b f_3(S)P_3(B)-H(S)B_3(B).
\end{aligned}
\tag{14}
$$
则
$$
\boxed{
\mathscr P_C e_0
=\frac{\delta}{84}
 \nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)
 \boxtimes
 (H_T\otimes U_0+f_{1,T}\otimes U_1
       +f_{3,T}\otimes U_3+f_{4,T}\otimes U_4).
}
\tag{15}
$$
由 R764 的 $\mathcal T$ 在 T、$C_0$ 上同时乘 $\omega^2$，相同四项在
$\mathscr P_C h_W$ 中的乘数分别为
$$
\boxed{(\omega^2,\ \omega,\ \omega^2,\ \omega).}
\tag{16}
$$
因此仍含 T 的浅独占门须配对整个 (15)、(16)，不能只留下 $U_1$。
这里没有给 $f_3$ 的负三矩、H 的中央或任何单项赋零。

## 4. 合法保五伙伴的 t 正一边界

记 $\pi$ 忘 T 而保
$(S,C_0,B,\xi_2,d)$。采用原归一
$\int X^j\,d\nu_F=\Omega^jF^{(j)}(0)$。
$T=\delta\mathfrak t$，而 $f_1'(0)=1$；
(15) 其他三个 T 来源的一阶矩为零。因此
$$
\boxed{
\Omega^{-1}\pi_*(\mathfrak t\,\mathscr P_C e_0)
=\mathcal M_5
:=\frac1{84}\,
 \nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)
 \boxtimes\bigl(2\nu_{f_3}(S)\boxtimes\nu_{B_3}(B)
             +\nu_H(S)\boxtimes\nu_{P_3}(B)\bigr).
}
\tag{17}
$$
同样
$$
\boxed{
\Omega^{-1}\pi_*(\mathfrak t\,\mathscr P_C h_W)=\omega\mathcal M_5 .
}
\tag{18}
$$
这保整个五变量来源，不是只给质量或某条一维边际。

若不作 C 平均，准确的未删边界是
$$
\frac1{84}\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)\boxtimes
 \{2\nu_{f_3}(S)\otimes\nu_\Psi(C_0,B)
                       -\nu_H(S)\otimes\nu_\Pi(C_0,B)\}.
\tag{19}
$$
(17) 正是对 (19) 作 (5) 的结果。

R764 的共同域
$$
\mathcal D^\infty_{n,N}
=\{Y\ {\rm unit},\
 \widehat{\mathfrak s},\widehat d\in p^N,\
 \widehat{\mathfrak s}/2-3\widehat d\notin p^n\},
\quad
\widehat{\mathfrak s}=S/\delta-Y/17,\quad\widehat d=d-Y/17
\tag{20}
$$
以及 $q,P,E_\perp$ 都不含 T。
所以对其中任何完整五变量测试 f，真正有
$$
\boxed{
\int_{\mathcal D^\infty_{n,N}} f\,q\,\mathfrak t\,de_0
=\Omega\int_{\mathcal D^\infty_{n,N}} f\,q\,d\mathcal M_5 .
}
\tag{21}
$$
若左边另附 $\mathfrak t$-unit，右边准确再乘
$1-\beta\kappa$；这是全 t 核保五伙伴后的一阶矩 depletion。
精确第 m 环带再乘 $\beta^m\kappa^m$，其他测试按 R764 真实缩放转置。
该因子没有从某个裸边际猜得。

## 5. 原全 Y 首行恰为一条已识别 rank-one 线

本节先不切 CD 或 E。在原指数生成函数中，由原物理系数，
$$
\Omega^{-1}Y_*(\mathfrak t e_0)
=S_{34}(z)
 \left\{\frac1\delta\zeta(\delta z)
 -\frac{\omega^2}{\delta}\zeta(\gamma z)
 +\frac{\omega}{\delta}\zeta(\bar\gamma z)-\zeta(z)\right\},
\quad \gamma=3+\omega .
\tag{22}
$$
由于 $\langle\mathfrak t,Y\rangle=0$，所有共同 $\zeta(z)$ 项严格消去；这是原正交方向，不是把一个连接项遗漏。

保完整 division 常数
$$
r=(2-6\delta)/7,\qquad
\sigma(\delta z)=\delta x_b\sigma^3,\qquad
\sigma(\gamma z)=\gamma\sigma^7(X-rb),\qquad
X=x_b^3,
\tag{23}
$$
以及共轭式。用 $x_b'=2y_b$ 得
$$
\begin{aligned}
(22)
={}&\sigma^{34}x_by_b(X+b)(X-8b)\\
&\quad\cdot
 \left\{\frac2{\delta^2}(X-rb)(X-\bar rb)
 -\frac{6\omega^2X(X-\bar rb)}{\delta\gamma}
 +\frac{6\omega X(X-rb)}{\delta\bar\gamma}\right\}\\
={}&\frac2{21}\sigma^{34}x_by_b
 (X+b)(X-8b)(11X^2-32bX-16b^2).
\end{aligned}
\tag{24}
$$
所用原 $S_{34}$ 是
$\sigma^{34}x_b^2(X+b)(X-8b)(X-rb)(X-\bar rb)$。
最后一行的四次多项式准确为
$$
11X^4-109bX^3+120b^2X^2+368b^3X+128b^4 .
$$
因此由 R732 的全相位规范，
$$
\boxed{\Omega^{-1}Y_*(\mathfrak t e_0)=-\frac{22}{21}\nu_{D_{\omega,b}}.}
\tag{25}
$$
两条 source 身份已在原全函数层面核定，未从一个正矩猜负矩。

R764 又给
$$
\mathfrak t=\frac{W-W'}{1-4\omega}.
$$
所以 $(Y,\mathfrak t)$ 通过原
$\pi_4=(Y,W,W',G)$ 因子化。
最终 q 的完整 $\pi_4$ 返回立即给
$$
\boxed{
\Omega^{-1}Y_*(\mathfrak t q_N^*e_0)
=-\frac{22}{21}\beta^N\nu_{D_{\omega,b}},
\qquad
\Omega^{-1}Y_*(\mathfrak t q_N^*h_W)
=-\frac{22\omega}{21}\beta^N\nu_{D_{\omega,b}} .
}
\tag{26}
$$
对原真实中性测试 $\zeta_N^{(715)}$，这两条完整来源都为零；
没有把该中性方向的其他混合矩也赋零。

由 R735，原
$$
I_{\omega,-1}=\int_{\mathcal O^\times}Y^{-1}\,d\nu_{D_{\omega,b}}
$$
严格非零。因此同一 q 的实际单位行是
$$
\boxed{
\int_{Y\ {\rm unit}}\frac{\mathfrak t}{Y}\,q\,de_0
=-\frac{22}{21}\beta^N\Omega I_{\omega,-1}\ne0 .
}
\tag{27}
$$
更完整地，令 $r_n=(-\kappa)^n$。R764 的整 Y/t 核给
$$
\boxed{
\begin{aligned}
&\int_{\substack{Y\in p^n,\ \mathfrak t\in p^m\mathcal O^\times}}
 1_{Y/r_n\ {\rm unit}}
 \frac{\mathfrak t/\kappa^m}{Y/r_n}\,q\,de_0\\
&\qquad=-\frac{22}{21}\lambda^n\beta^{m+N}
 (1-\beta\kappa)\Omega I_{\omega,-1}\ne0 .
\end{aligned}}
\tag{28}
$$
这是归一后的真实有界测试。若用未归一的 t 或 $Y/p^n$，
必须恢复相应 $\kappa^m$、$r_n/p^n$ 尺度；(28) 没有隐藏它们。
同一个矩形的未乘 $\mathfrak t/Y$ 的中央行仍由 R764(19) 回原 $J_S$。
两种测试不能互代。

## 6. 同一条件来源的全部五个坐标

令 $\mathcal U$ 是任一 R764 返回后的有限齐次伙伴域，先不附 Y-unit。允许其中含精确 t 环带、三条 CD/O 失败门及完整移动 E 门；每条行都在 $Y^\perp$。
定义真正条件来源
$$
\mathcal L_{\mu,\mathcal U}
=\Omega^{-1}Y_*\bigl(1_{\mathcal U}\mathfrak t\,q\,\mu\bigr).
\tag{29}
$$
若 $\mathcal U$ 不含 t，(17)–(21) 给其精确五变量积分；
若含 t，须使用整个 (15)、(16)，不能提前忘 T。

原整 Y 线丛、全部纯伙伴门和正阶伙伴收缩按 R745/R752 保持第一轴标准 $\mathcal S_{34}$，没有 Y 的 p-primary 扭移。
每条实际 q 块总次数为 $0\bmod6$；乘 $\mathfrak t$ 后角型为5。
所以
$$
\boxed{
\mathcal L_{\mu,\mathcal U}
=\sum_{j=0}^4 c_j(\mu,\mathcal U)\,\Xi_j,\qquad
\Xi_j=-b^j\sigma_b^{34}x_b^{13-3j}y_b .
}
\tag{30}
$$
这些是 R732 的整个五维空间，不仅是其中两条已识别线。

下面给出实际坐标的完整、无 $\zeta$ 公式。
置 $r_i=5+6i$，并定义原正矩
$$
\boxed{
m_i(\mu,\mathcal U)=
 \frac{\displaystyle\int
 Y^{r_i}\mathfrak t\,1_{\mathcal U}q\,d\mu}
 {b^i r_i!\Omega^{r_i+1}},
 \qquad 0\le i\le4 .
}
\tag{31}
$$
在 (20) 等 t 独立域中，(31) 等于
$$
\frac1{b^i r_i!\Omega^{r_i}}
 \int Y^{r_i}1_{\mathcal U}q\,d\mathcal M_5
\tag{32}
$$
于 $\mu=e_0$；对 $h_W$ 乘 $\omega$。
因此 (31) 是显示低度张量上的真实五个正矩，不是未定义的“某五个系数”。

用形式变量 $w=bz^6$ 定义固定有理级数
$$
X_0(w)=1+\sum_{n\ge1}a_nw^n,\quad
a_1=-1/7,\quad
a_n=\frac{\sum_{j=1}^{n-1}a_ja_{n-j}}{(6n+1)(n-1)}\ (n\ge2),
$$
$$
Q_0(w)=\exp\!\left(-\sum_{n\ge1}
 \frac{a_n}{6n(6n-1)}w^n\right),\qquad
Y_0(w)=1-\sum_{n\ge1}(3n-1)a_nw^n .
\tag{33}
$$
这些分别是原 $x_bz^2,\sigma_b/z,-y_bz^3$ 的准确级数；
递推来自 $x_b''=6x_b^2$，无额外规范。

定义下三角矩阵
$$
\boxed{
\mathbb T_{ij}=
\begin{cases}
[w^{i-j}]\,Q_0(w)^{34}X_0(w)^{13-3j}Y_0(w),&i\ge j,\\
0,&i<j .
\end{cases}}
\tag{34}
$$
则 $\mathbb T_{ii}=1$，且原完整坐标准确为
$$
\boxed{
(c_0,c_1,c_2,c_3,c_4)^t
=\mathbb T^{-1}(m_0,m_1,m_2,m_3,m_4)^t .
}
\tag{35}
$$
只需 (33) 至 $w^4$。这给一个固定五阶整逆，不新增依 p、N 的拟合或坏集。
原 $p>163$ 已使所有显示阶乘和固定小分母为单位。
q 的整性与 (31) 还给 $m_i,c_i\in\mathcal O$；
有限 p-torsion Fourier 表达中可能出现的分母不被据此单项删除。
固定每个实际 p、N、n、m 后，R745/R752 的有限伙伴译与正矩收缩给这些系数的代数性；原每个齐次 q 块的 $\Omega^{-d}$ 与 (31) 的正矩周期完全抵消。因此 $c_j\in\overline{\mathbf Q}\cap\mathcal O$，不是任意未识别的 $\mathbf C_p$ 条件质量。这里没有用有限谱投影与无限对数极限交换。

## 7. 两条算术投影与完整 primitive 系数

令 $\mathbb N$ 为 R732 的完整 normalized CM13 算子在 (30) 的降幂基中的矩阵。
它等于该篇 $b=1$ 升幂矩阵反转行列顺序；因所有 $\Xi_j$ 具有同一六次缩放因子，这个矩阵与 b 无关。
其特征/最小多项式是
$(T+1)(T+\omega^2)(T^3+\omega)$。

对 (35) 的**实际条件坐标列** c 定义
$$
\mathbb P_6=\frac{\mathbb N^3+\omega I}{\omega-1},\quad
\mathbb P_-=\frac{\mathbb N+\omega^2I}{\omega^2-1}\mathbb P_6,\quad
\mathbb P_\omega=\frac{\mathbb N+I}{1-\omega^2}\mathbb P_6 .
$$
令
$$
\begin{aligned}
v_-&=(1,13,-156,-104,64)^t,\\
v_\omega&=(1,-109/11,120/11,368/11,128/11)^t,\\
a_-&=(\mathbb P_-c)_0,\qquad
a_\omega=(\mathbb P_\omega c)_0,\qquad
c_{\rm prim}=c-a_-v_--a_\omega v_\omega .
\end{aligned}
\tag{36}
$$
于是整条来源的唯一分解为
$$
\boxed{
\mathcal L_{\mu,\mathcal U}
=a_-D_{-,b}+a_\omega D_{\omega,b}
 +\sum_{j=0}^4(c_{\rm prim})_j\Xi_j .
}
\tag{37}
$$
(31)、(34)、(36) 是其五个真实条件矩到全部谱分量的明确有限线性公式。
最后一项落整个三维 primitive 块；没有由其质量零删除。
若将 CM 算子搬回未收缩的原混合域，仍须运输完整纤维和单位条件。
这里先完成 (29) 的实际来源，再按全来源身份 (37) 分解。

R735/R761 可以在已知实际系数后应用于 (37) 的单位负一行；
本篇未证明任何指定 $\mathcal U$ 的 $a_\omega$ 或 $a_-$ 已非零。
裸 (26) 的系数不能替代它。

## 8. 所有浅域、共同深域和外补项的五维守恒式

R764 的返回域使用
$$
H_{j,m}=\widehat{\mathfrak s}-\omega^{2j}\kappa^m\mathfrak t,
$$
$$
\widehat d\in p^N,\quad
H_{j,m}\in p^N,\quad
H_{j,m}/2-3\widehat d\notin p^n .
\tag{38}
$$
原 E 门仍是
$E_\perp+(17+3\omega)\omega^{2j}\kappa^m\mathfrak t$
的相应深/浅条件。所有这些行都在 $Y^\perp$，所以每个有限
Boolean 原子都可用 (29)–(37)。

当 $m<N$ 且 t unit 时，三个 CD 原子互斥；
$N\le m<n$ 时保不同失败门；
$m\ge n$ 时共同域 (20) 才允许用 (17) 收缩。
在前两个范围，(15) 的四个 T 来源完整保留，包括 H、$f_3$；
不能从共同深首项倒删浅域。

令 $\mathcal P$ 为这些实际条件及其补集形成的任意**完整有限分割**，在未附 Y-unit 的伙伴空间上取值。由 (26)、(29) 的线性性，
$$
\boxed{
\sum_{\mathcal U\in\mathcal P}c(e_0,\mathcal U)
=-\frac{22}{21}\beta^N v_\omega .
}
\tag{39}
$$
若分割只在 $\mathfrak t$-unit 上完整，则右边乘 $1-\beta\kappa$。
对 $h_W$ 的整个总和再乘 $\omega$，但一般含 t 的单原子
不能各自乘 $\omega$；其正确来源乘数是 (16)。

对实际负一行，(39) 准确给
$$
\boxed{
\sum_{\mathcal U\in\mathcal P}
 \int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{\mathcal L_{e_0,\mathcal U}}
=-\frac{22}{21}\beta^N I_{\omega,-1}\ne0 .
}
\tag{40}
$$
有限深尾仍在分割中，不以 $\beta$ 为单位的环带级数删除。
尤其 (39) 的算术投影给
$\sum a_-=0,\ \sum a_\omega=-22\beta^N/21$，
primitive 坐标总和为零；这不等于每个分量为零。

由此，R764 同域首项、浅独占域以及域外部分有同一个真实五维来源系统。
已付非零的是完整总行 (27)、(28)、(40)。
主中央假设仍只控制对应原未乘 $\mathfrak t/Y$ 的 Mellin 导数；
它尚未给所有补原子的负一行零。本文没有把这个差别隐藏为一个“条件质量”假设。

## 9. 与 R764 同域首项的直接接口

在 (20) 及其合法 E 门上，
$P=b_YY+a\widehat{\mathfrak s}+2\widehat d$，$a=1+3\omega$，
$P-b_YY\in p^N$。所以
$$
\int_{\mathcal D^\infty_{n,N}}\frac{\mathfrak t}{P}q\,de_0
=b_Y^{-1}\Omega
 \int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{\mathcal L_{e_0,\mathcal U}}
 +p^N\mathcal O .
\tag{41}
$$
$\mathcal U$ 是 (20) 去掉 Y-unit 后的同一个伙伴门，
并保同一个 $E_\perp$ 条件。
将 (37) 代入 (41)，得到实际同域 $W_j-W_k$ 首项的全部两算术坐标和 primitive 坐标。
若需精确原观察，可直接用 (21) 的 $1/P$ 五变量积分；
(41) 只是明示误差的比较式。

R764 的高阶对数尾及其 $\lambda^n\beta^m\kappa^m$ 系数原样保留。
本篇不把 (41) 的误差、原 E 浅门、$I/O/X$ 或原 T 外部项赋零。

## 依赖与可复现范围

- [R764](R764-y-preserving-six-axis-and-three-cd-exterior-domains.md)：整框架、whole 核、实际 CD/O/E 门及全部缩放。
- [R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)：六度整基和两个完整外积核。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：同一个实际 $q_N^*$、整性与 $\pi_4$ 返回。
- [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)、[R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：五维全谱、原 $D_\omega$ 规范及真实负一非零。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)、[R752](R752-native-mod-p-two-source-closure-and-point-inertia-extraction.md)：纯伙伴有限门与真实正矩收缩的来源范围。
- [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)：primitive 块的完整算术范围；本篇保其实际条件系数。
- [最终 q 的 T 不变性](../notes/2026-11-15-final-carry-t-invariance-and-same-weight-states.md)：全部真实列、六支和系数范围。

固定 reader 脚本为
[check-r767-native-five-coordinate-reader.py](../scripts/check-r767-native-five-coordinate-reader.py)。
它从 R732 的 producer 重建五个完整十三纤维，随后生成
(34)–(36) 的固定有理矩阵并核 (24)–(25)。
它不输入旧生成数据、不输出文件，也不计算或猜测任何条件矩数值。
本文各恒等式已由以上完整代数证明；公开执行的实际 run/hash 另按回执登记。

## 公开执行回执

固定 reader 已在公开 Actions run **43723237144**、job **132839529955** 成功执行，来源提交 `07198aedd0bd8a6f8ad010c56212f3d97bad8ccc`，`python-flint==0.9.0`，命令为 `python3 topics/rank2-sha-infinitely-many-p/scripts/check-r767-native-five-coordinate-reader.py --workers=4`。它重建原五个十三点纤维、验证全部三投影和固定三角逆，并精确验证原 t 行为 `−22 Dω/21`；退出码0，stdout 2528字节，未生成输出文件。

- Producer SHA-256：`34b96e8c416f51a019f0229c5a6aaba70d60ee054d342af3be47e1e460137e63`。
- 完整 stdout SHA-256：`c0c2558b60e0c13167d9c31c4ea537ecbe7c0cafef9cbb2d21e78d9748c3b43f`。
- 固定依赖 producer 为 [R732 脚本](../scripts/check-r732-original-type-five-cm13.py)，SHA-256 `d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469`。

计算仅补充本文固定恒等式的可复现记录；实际条件矩未被执行器填写。按根规矩15，输出数据不入仓库或Release，只保上述producer、参数、run和哈希。
