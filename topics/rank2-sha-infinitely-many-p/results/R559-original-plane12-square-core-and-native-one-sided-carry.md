# R559 — 原十二范数平面的完整平方核心、同域单支与保 K 的六度核

日期：2026-11-14。**状态：已证明。**

本篇在 R556 的同一原六输入和同一个准确 carry 测试内，支付
$\mathscr D=F-c$ 方向的完整两层核心。它不是 $D_j=F-\omega^{2j}C$
方向，也不把 $D_j$ 深替换成 $\mathscr D$ 深。
在真实 $\mathscr D$ 深子域上，所有事件可与该方向分离；实际
$\kappa^{-n}$、四个原 Mellin 单位条件、常数 log 质量和五个伴随
仍全部保留。另用一个不改变原观察的真实 $C$ 旋转，将三支平均
严格化为一支，再把原 $\rho_0$ 接到 R533 的完整两变量六度核，
不遗忘第二输出 $K$。

本篇没有证明原剩余补域消失，也没有给辅助负矩赋非零值。课题
主目标未完成。

## 1. 原输入、准确测试及 native 行

沿用 [R556](R556-native-mixed-carry-odd37-cores-and-complete-residual.md)、
[R557](R557-third-source-common-carry-zero-mass-and-central-rows.md)
的全部规范和固定坏集：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\quad\Omega=\Omega_p\in\mathcal O^\times .
\tag{1}
$$
$p\ge71$ 属于已固定的普通射线。本篇不再细分射线；
R556 的模 $37$ 条件与 R558 的既定 $M_3$ 条件原样保留。

原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。置
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Y&=A+c+2d_0,\qquad W=A+3\delta c+4d_0,\\
L&=(1+3\omega)c+d_0,\qquad
u=(\omega c+(1-\omega)d_0)/2,\\
C&=(\xi_1-\xi_3+x)/\delta,\qquad H_0=\delta C,\\
D_4&=\xi_1+\omega^2\xi_2-2\omega\xi_3,\qquad
F=D_4+C+c+(2+3\omega)d_0,\\
H_1&=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\\
G&=13H_1+(3-2\omega)F .
\end{aligned}
\tag{2}
$$
这里 $Y$ 是未双倍的原输出。来源始终是
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\eta=\omega^2H_*\rho_0,\quad h=\eta+\rho_0/2,\quad
\Delta=\rho_0-\eta=\tfrac32\rho_0-h .
\tag{3}
$$
$H$ 固定前四输入，在 $(c,d_0)$ 上等于
$$
H=\frac12
\begin{pmatrix}-1-\omega&-1-2\omega\\2+\omega&-1-\omega\end{pmatrix}.
$$
$R_c$ 仅反射 $c$；完整源关系为
$$
(R_c)_*\rho_0=-\rho_0,\qquad (R_c)_*h=h .
\tag{4}
$$
本篇 $h$ 不等于 R536 §9 的旧三阶来源。

令 $\zeta_j=\omega^{2j}$，$D_j=F-\zeta_jC$，
$E_j=F+13\zeta_jC$，
$\Gamma_{n,j}=\{C,F\text{ 为单位},D_j\in p^n\}$。
以下始终使用 R536 已付的原准确六次多项式
$\widehat P_p=\mathcal R_pP_p$，包括全部
$(1+\lambda\kappa^j)^{-1}$ 和七行右逆：
$$
q=\frac1{3b\Omega^6}\sum_{j=0}^2
1_{\Gamma_{n,j}}\widehat P_p(D_j/\kappa^n,E_j,G),\qquad n\ge1.
\tag{5}
$$
绝不将其替换成模 $p$ 多项式。令
$$
\ell=1_{Y\in\mathcal O^\times}d\log\langle Y\rangle
-1_{W\in\mathcal O^\times}d\log\langle W\rangle,\quad a=q\ell ,
$$
$$
\mathcal B=\{u\in p\mathcal O,\ L\in\mathcal O^\times\},\qquad
I=h(\Phi_1-\Phi_2).
$$
R556 已对原样的 $\Phi_1,\Phi_2$ 支付
$$
2\lambda I=\int_{\mathcal B}(a-a\circ R_c)\,d\Delta ,
\qquad
\Delta(a-a\circ R_c)=3\beta^n(J'_S-6\delta J'_T).
\tag{6}
$$
第二式控制完整总行，不自动控制第一式的局部行。

## 2. 保原观察的 C 投影与准确单支

以 $\langle r,s\rangle=\sum r_i\bar s_i$ 记物理行的 Hermitian 积。
$N(C)=1$。定义完整酉旋转
$$
\mathcal R_C=I+(\omega-1)\bar C^{\,t}C,\qquad
\mathcal P_C=\frac{I+(\mathcal R_C)_*+(\mathcal R_C^2)_*}{3}.
\tag{7}
$$
它把 $C$ 变为 $\omega C$，固定整个 $C^\perp$，而
$$
Y,W,L,u,c,F,H_1,G,\ \mathscr D:=F-c\ \in C^\perp .
\tag{8}
$$
它也固定 R556 的两个 $J_\tau$、$Z_*$，与 $R_c,H$ 及
$u$ 方向的真实缩放交换。式 (5) 在此旋转下只把
$j$ 换成 $j+2$，其准确多项式和所有分母不变。因此 (6) 的
**整个实际测试**可用
$$
\rho^C=\mathcal P_C\rho_0,\qquad
h^C=\mathcal P_Ch,\qquad
\Delta^C=\tfrac32\rho^C-h^C
$$
替换原来源，而无任何 Mellin 单位条件的移动。

在 $H_0$ 方向，整个 odd degree $3$ 空间的整基为
$$
B_0=-y_\wp\sigma^3,\quad B_1=x_\wp\sigma^3,\quad B_3=\sigma^3,
\qquad\text{型分别为 }0,1,3.
\tag{9}
$$
因而 $\mathcal P_C$ 正好杀掉 $B_1$，保留 $B_0,B_3$。
这是全空间投影，不是少数 Taylor 系数的约消。

对投影后来源，三支积分相等。设
$$
D_0=F-C,\quad E_0=F+13C,\quad
\mathcal E_n=\{D_0\in p^n,\ C\in\mathcal O^\times\},
$$
$$
q_0=\frac1{b\Omega^6}\widehat P_p(D_0/\kappa^n,E_0,G)
\quad\text{在 }\mathcal E_n\text{ 上}.
\tag{10}
$$
三支平均的 $1/3$ 准确抵消，不能再留一个 $1/3$。
分别对 (6) 的两个线性积分作此单支化，再在第二项用 $R_c$
换元。由 (4) 得
$$
\boxed{
2\lambda I=
\int_{\mathcal E_n}q_0\ell
\left\{
\tfrac32(1_{\mathcal B}+1_{\mathcal B^c})\,d\rho^C
+(1_{\mathcal B^c}-1_{\mathcal B})\,dh^C
\right\},\quad
\mathcal B^c=R_c\mathcal B .
}
\tag{11}
$$
$\mathcal B$ 与 $\mathcal B^c$ 不交：两条 $u_1,u_2$ 同深会迫
$c,d_0$ 同深，与 $L$ 为单位矛盾。在 $\mathcal B$ 上，
$\mathcal E_n$ 与 $R_c\mathcal E_n$ 也不交，因为两个 $D_0$
相差 $2c$，而 R556 已证该域内 $c$ 为单位。

(11) 是对完整积分的线性整理。它并不宣称 R556 原三支的
六个 $j\ne k$ 逐点交集为空。此时没有附加 $\mathscr D$ 深条件。
[R560](R560-native-single-branch-and-seven-conditional-moments.md)
沿 (11) 的 $D_0$ 方向继续；本篇以下支付不同的 $\mathscr D$ 方向。

## 3. 实际十二范数轴及完整六坐标格

由 (2) 直接有
$$
\mathscr D=F-c=D_4+C+(2+3\omega)d_0,\qquad
N(\mathscr D)=12,\qquad \mathscr D\perp c,H_0 .
\tag{12}
$$
取第一整数覆盖
$$
R=2\delta\mathscr D,\qquad N(R)=144.
$$
在原六输入上的完整行是
$$
R=(4+4\omega,\ 2-2\omega,\ 6+4\omega,\ 2,\ 0,\ -8+2\omega).
\tag{13}
$$
乘原 $H$ 后仍为整数行：
$$
RH=(4+4\omega,\ 2-2\omega,\ 6+4\omega,\ 2,\ -9-3\omega,\ 5+4\omega).
$$
两行均给 standard even 半特征。于是整个原两态在该轴属于
同一个完整 $\mathcal S_{144}$，不是只知道其一条边际。

为保留所有余坐标，置
$$
Y_0=Y-c+\mathscr D/12,\quad
W_0=W-3\delta c+\delta\mathscr D/4,\quad
G_0=G-(3-2\omega)c+(3-2\omega)\mathscr D/12,
$$
$$
(T_1,T_2,T_3)=12\delta(Y_0,W_0,G_0).
\tag{14}
$$
这些均与 $c,H_0,R$ 正交。完整 frame 为
$(c,H_0,R,T_1,T_2,T_3)$；后三行为
$$
\begin{pmatrix}
-34+2\omega&-71-\omega&15+62\omega&49+60\omega&0&20+49\omega\\
-42+6\omega&-63+9\omega&9+72\omega&51+66\omega&0&30+69\omega\\
-26-234\omega&325+533\omega&-143-104\omega&-117+130\omega&0&-130+169\omega
\end{pmatrix}.
$$
其行列式和范数准确为
$$
\det=8895744+25069824\omega,\qquad
N(\det)=2^{16}3^{11}13^3\,19.
\tag{15}
$$
均为当前处单位。对 $\eta$ 使用 $2c,2T_1,2T_2,2T_3$ 的共同
覆盖即可清其半系数；$H_0,R$ 不必增加层数。
因此后三轴的全部耦合和全部隐藏域仍在，不靠边际决定联合源。

## 4. whole S144 平方：中心相位与绝对锚

令 $K_N$ 为外部 $\lambda$ 已提出的标准完整核心，
$\mathsf T_{t,N}$ 为 canonical theta 平移。在当前射线上
$$
g_\pi=\pi_0/\bar\pi_0
\equiv91+72\omega\pmod{288},\qquad
g_\pi^2\equiv217+144\omega\pmod{288}.
\tag{16}
$$
第一式可直接由模 $32$ 的 $27+8\omega$ 与模 $9$ 的 $1$ 合成；
没有引入新的射线。

定义
$$
P_{2,N}=\frac14\sum_{t\in E[2]}\mathsf T_{t,N},\qquad
B_{2,N}=2P_{2,N}-I .
$$
在标准 Schrödinger 基 $e_j$，$j\bmod144$ 中，完整计算给
$$
B_{2,144}e_j=(-1)^j e_{73j+72},\qquad B_{2,144}^2=I,
$$
$$
B_{2,144}XB_{2,144}=-X^{73},\qquad
B_{2,144}ZB_{2,144}=-Z^{73}.
\tag{17}
$$
两处负号都属于真实中心，不能只保索引置换。
其 CM 完整 lift 为 $73+144\omega$。与 (16) 比较，
$$
217+144\omega\equiv145(73+144\omega)\pmod{288},\qquad
(145^2-1)/144=146\in2\mathbb Z .
\tag{18}
$$
因此完整 Heisenberg 交织相同，不残留中心字符。
不可约性交织只剩一个标量。

用真实 $\sigma(12z)\in\mathcal S_{144}$ 定此绝对标量。
其归一核心为 $-1$，故平方为 $+1$；
又每个 $t\in E[2]$ 满足 $12t\in6\Lambda$，全部实际半特征为正，
所以 $B_{2,144}\sigma(12z)=\sigma(12z)$。
于是得到 whole 空间恒等式
$$
\boxed{K_{144}^2=B_{2,144},\qquad K_{144}^4=I.}
\tag{19}
$$
所附脚本检查全部 $144$ 列及 (17) 的两负中心相位。

### 4.1 在原两态上的准确作用

这里还需要把 $B_2$ 搬回原输入，不能从 (19) 猜其来源矩阵。
$R/2$ 在前四输入中有三个奇系数，末输入系数是 $-4+\omega$，
而 $c$ 系数为零。因此在共同原 pair 的 $\mathcal S_4\otimes
\mathcal S_4$ 覆盖上，四个平移的实际权是
$\varepsilon(0)=1,\varepsilon(t)=-1$（$t\ne0$），只作用于 $d_0$。
三个共享 sigma 的半特征恰给此权，$-4+\omega$ 对二挠点的
置换保该权。完整四维计算为
$$
\frac14\sum_{t\in E[2]}\varepsilon(t)\mathsf T_{t,4}
=\frac{I-R_{d_0}}2 .
\tag{20}
$$
原 pair 同时反射 $(c,d_0)$ 为正，故在原两态上
$R_{d_0}=R_c$。因此
$$
P_{2,144}\rho_0=\rho_0,\qquad
P_{2,144}\eta=-\rho_0/2,\qquad
B_{2,144}=-R_c
\quad\text{在 }\operatorname{span}\{\rho_0,\eta\}\text{ 上}.
\tag{21}
$$
(20) 的矩阵为
$\frac12(e_1-e_3)(e_1-e_3)^t$，完整固定了符号和系数。

由 (19)–(21)，对原两态的任意线性组合 $\mu$、任意 $m\ge0$，
$$
\boxed{
\mu|_{\{\mathscr D\in p^{2m}\}}
=\lambda^{2m}(P_{\mathscr D,\kappa^{2m}})_*
(-R_c)^m\mu .
}
\tag{22}
$$
$P_{\mathscr D,s}$ 只把物理 $\mathscr D$ 乘 $s$，固定 (14) 的五个
正交伴随。特别
$$
(-R_c)^m\Delta=\tfrac32\rho_0-(-1)^m h .
\tag{23}
$$
上述算子与 $\mathcal P_C$ 交换，所以同式对投影后来源成立。

原 $c$ 核为 $\lambda R_c$，且 $c\perp\mathscr D$，故还得到
真正完整矩形
$$
\boxed{
\mu|_{\{c\in p^r,\ \mathscr D\in p^{2s}\}}
=\lambda^{r+2s}(P_{c,\kappa^r}P_{\mathscr D,\kappa^{2s}})_*
(-1)^sR_c^{r+s}\mu,\qquad r,s\ge0 .
}
\tag{24}
$$
例如 $r=s=1$ 的来源返回是 $-\lambda^3\mu$，但物理矩形是
$(c,\mathscr D)$ 的深度 $(1,2)$，不是共同缩放。
(21) 只在原两态上使用；以后增加 $K_Hh^C$ 时不能自动延长
$B_2=-R_c$。

## 5. 原独有支在 D 深域的准确运输

以下 $\mathscr D$ 简写为 $t$，与 $D_0,D_j$ 区别。任意行写成
$r=r_\perp+a_rt$，其中 $a_r=\langle r,\mathscr D\rangle/12$。
所需完整系数为
$$
\begin{array}{c|c}
r&a_r\\ \hline
Y,\ Y\circ R_c&-1/12\\
W,\ W\circ R_c&-\delta/4\\
u&-(4+5\omega)/24\\
L,\ d_0&-(1+3\omega)/12\\
H_1,\ G&(-3+2\omega)/12\\
c,\ C&0 .
\end{array}
\tag{25}
$$
特别 $Y_\perp=Y_0+c$、$W_\perp=W_0+3\delta c$，
$Y^c_\perp=Y_0-c$、$W^c_\perp=W_0-3\delta c$，
以及
$$
G_\perp=13H_{1,\perp}+(3-2\omega)c .
$$

固定 $m\ge1,\ 2m\ge n$，令 $\epsilon=\kappa^{2m}$。
对 (6) 加上真正的 $\mathscr D\in p^{2m}$ 限制后用 (22)。
来源变为
$$
\lambda^{2m}\Delta_m^C,\qquad
\Delta_m^C=\tfrac32\rho^C-(-1)^m h^C .
\tag{26}
$$
所有原 $u$ 深和 $L$ 单位事件准确变成
$$
\mathcal B_\perp=\{u_\perp\in p,\ L_\perp\text{ 为单位}\};
$$
四个 Mellin 单位事件分别是
$Y_\perp,W_\perp,Y^c_\perp,W^c_\perp$ 为单位。
不能只留一个 $Y$ 单位事件。

原 $F=c+t,F\circ R_c=-c+t$。由于 $2m\ge n$，两实际单支为
$$
\mathcal E_+=\{c-C\in p^n,\ C\text{ 为单位}\},\qquad
\mathcal E_-=\{-c-C\in p^n,\ C\text{ 为单位}\}.
\tag{27}
$$
它们不交，并且现在确实不依赖自由 $t$。
这一步使用 $\mathscr D$ 深；它没有在完整域上先把 $F$ 换成 $c$。

写 $a_G=(-3+2\omega)/12$。准确 carry 权为
$$
Q_+(t)=\frac1{b\Omega^6}\widehat P_p\left(
\frac{c-C}{\kappa^n}+\kappa^{2m-n}t,\
c+13C+\epsilon t,\ G_\perp+\epsilon a_Gt\right),
$$
$$
Q_-(t)=\frac1{b\Omega^6}\widehat P_p\left(
\frac{-c-C}{\kappa^n}+\kappa^{2m-n}t,\
-c+13C+\epsilon t,\
G_\perp-2(3-2\omega)c+\epsilon a_Gt\right).
\tag{28}
$$
四个实际观察仍为
$$
Y_\perp-\epsilon t/12,\quad W_\perp-\epsilon\delta t/4,\quad
Y^c_\perp-\epsilon t/12,\quad W^c_\perp-\epsilon\delta t/4 .
\tag{29}
$$
令 $\ell_+(t),\ell_-(t)$ 分别用 (29) 的前两项、后两项组成
原样的带单位指标中央差。则 (6) 中这一真实子域的完整值为
$$
\boxed{
2\lambda I_m=\lambda^{2m}
\int_{\mathcal B_\perp}
\left\{1_{\mathcal E_+}Q_+(t)\ell_+(t)
-1_{\mathcal E_-}Q_-(t)\ell_-(t)\right\}\,d\Delta_m^C .
}
\tag{30}
$$
(30) 的五个伴随、两支支撑、三个准确 carry 参数和全部 log
质量都显示出来。其余 $\mathscr D$ 浅环带及单位域仍是
$I-I_m$，没有被该公式删除。

### 5.1 自由轴的真实首行与严格误差

若 $\ell_0=2m-n\ge1$，令 $Q_\pm^0=Q_\pm(0)$、
$\ell_\pm^0=\ell_\pm(0)$。在 (27) 的对应域内，准确多项式整性给
$$
Q_\pm(t)-Q_\pm^0\in p^{\ell_0}\mathcal O.
$$
所有保留的单位 log 属于 $p\mathcal O$；(29) 的 log 差属于
$p^{2m}\mathcal O$。因此逐点并且积分后都有
$$
\boxed{
Q_\pm(t)\ell_\pm(t)-Q_\pm^0\ell_\pm^0
\in p^{\ell_0+1}\mathcal O .
}
\tag{31}
$$
这里没有先假设常数 log 质量为零。

故首行确是完整条件零次测度
$(\mathrm{forget}\ \mathscr D)_*\Delta_m^C$ 对
$$
1_{\mathcal B_\perp}
(1_{\mathcal E_+}Q_+^0\ell_+^0-1_{\mathcal E_-}Q_-^0\ell_-^0)
$$
的积分。更高行由 (28) 的有限多项式与
$\log(1+\epsilon a_rt/r_\perp)$ 的收敛级数给出，全部条件
$t^j$ 矩保留。R557 只在其原 $\mathcal D_n$ 网格支付的零质量
不能直接放到这个不同的五伴随域上。

## 6. 原 rho 的完整六度双核：不遗忘 K

原 $\rho_0$ 的 $c$ 输入是独立原 sigma。对 $H_0$ 取完整 (9)
分解、再用 $\mathcal P_C$，所以存在两个实际四变量整来源
$\Lambda_0,\Lambda_3$，使整个六变量来源准确等于
$$
\boxed{
\rho^C=
\nu_\sigma(c)\otimes
\{\nu_{B_0}(H_0)\otimes\Lambda_0(R,T_1,T_2,T_3)
+\nu_{B_3}(H_0)\otimes\Lambda_3(R,T_1,T_2,T_3)\}.
}
\tag{32}
$$
原 $-1/84$ 已包含在 $\Lambda_j$ 中。二者不同，未声称质量为单位。
系数提取使用 odd3 完整基及 $0,3$ 阶矩，$3!\Omega^3$ 为单位，
所以 (32) 在整 Amice 格上成立。

置两个真实输出
$$
H_{\rm out}=\delta(c-C)=\delta c-H_0,\qquad
K_{\rm out}=\delta(c+C)=\delta c+H_0 .
\tag{33}
$$
它们各范数 $6$、互相正交，并均与 $R,T_1,T_2,T_3$ 正交。$(c,H_0)\mapsto(H_{\rm out},K_{\rm out})$
行列式 $2\delta$ 为当前处单位。
(32) 两条完整生成核是
$$
\boxed{
\sigma(\delta(h+k))B_0(k-h),\qquad
\sigma(\delta(h+k))B_3(k-h),
}
\tag{34}
$$
均在整个 $\mathcal S_6\otimes\mathcal S_6$ 中；四个伴随的
$\Lambda_j$ 原样张量保留。这里 $h,k$ 只是解析变量，与来源 $h$
区别。在指数生成函数中同时乘原 $\Omega$。

令 $a_0=2+\omega$，则 $\delta=-\omega^2a_0$。用
[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)
的完整两个核，逐项准确有
$$
\sigma(\delta(h+k))B_0(k-h)=-\omega^2F_B(-h,k),
$$
$$
\sigma(\delta(h+k))B_3(k-h)=-\omega^2F_P(-h,k).
\tag{35}
$$
这是全函数恒等式，不是忘记 $K$ 后的边际。
R533 的实际外积式、whole $\mathcal S_6$ 核 $\beta$、
所有真实双单位或独立环带条件都可在此使用。

例如若原固定负矩
$$
I_4=\int_{\mathcal O^\times}z^{-2}d\nu_{f_4},\qquad
I_1=\int_{\mathcal O^\times}z^{-5}d\nu_{f_1}
$$
同时为零，则 (34) 在 $H_{\rm out}$ 单位上的
$H_{\rm out}^{-2}$ 与 $H_{\rm out}^{-5}$ 两条条件行，
对任意完整 $K_{\rm out}$ 测试都为零；反射及 $-\omega^2$ 常数
按 (35) 保留。$H_{\rm out}^{-1}$ 条件行则由整个 $\mathcal S_6$
缺少型 $5$ 无条件为零。这些说法不是 $I_1,I_4$ 已非零的证明，
也不允许把混合 $Y$ 单位域遗漏。

事实上原完整单支条件是
$$
D_0=c+\mathscr D-C
=(H_{\rm out}+\delta\mathscr D)/\delta\in p^n .
\tag{36}
$$
只有在 (30) 已付的 $\mathscr D\in p^{2m},2m\ge n$ 子域上，
它才等价于 $H_{\rm out}\in p^n$，并由 $C$ 单位等价得到
$K_{\rm out}$ 为单位。不能在 (11) 的完整域免费这样替换。
原观察也仍为
$$
Y=Y_0+\frac{H_{\rm out}+K_{\rm out}}{2\delta}
-\frac{\mathscr D}{12},\qquad
W=W_0+\frac32(H_{\rm out}+K_{\rm out})
-\frac{\delta\mathscr D}{4}.
\tag{37}
$$
这两式明确说明 $K_{\rm out}$ 仍在原 Mellin 条件中。

## 7. 完整范围与复现

本篇新增的是 whole $\mathcal S_{144}$ 的含中心平方恒等式、
原两态的真实两层矩形、同一个 native carry 子域的准确自由轴
转置，以及保四伴随的 R533 双核连接。C 投影后的全域单支
(11) 与不同的深子域 (30) 分开陈述。

原 $I$ 仍须和其完整补域联立；(31) 的首行不自动为零，
(32) 的两伴随不能按质量合并，(36) 的斜条件也不能删去。
本篇不增加任何未识别算术来源的中央零。

精确证书：
- [check-r559-plane12-square-core-and-native-carry.js](../scripts/check-r559-plane12-square-core-and-native-carry.js)
- [check-r559-plane12-square-core-and-native-carry.json](../scripts/check-r559-plane12-square-core-and-native-carry.json)

脚本仅用 BigInt 有理数与 $\mathbb Q(\omega)$ 运算，检查原 frame、
全部投影系数、两个完整 theta 中心、四半周期加权矩阵、
$C$ 旋转的真实不变量以及 $H_{\rm out},K_{\rm out}$ 的完整正交关系。
运行方式为 node 加脚本路径；证书保全部 $144$ 列，不依赖浮点或采样。
