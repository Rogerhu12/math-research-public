# R1061：原有限和的实际无分歧九次覆盖与固定三挠 theta 点

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta / o2_high_coefficient / root。

**已证明：原 $S_n$ 是一条固定亏格二曲线上、一个明确三挠点处的 Raynaud–Petri 读数；其非零准确等价于该点的 Raynaud theta 除子光滑。** 覆盖、分支、三挠线、Frobenius 交换及实际微分尺度全部保留。光滑性本身尚未证明；相邻角色的 ordinary 性不自动给这一结论。

## 1. 同一个原曲线的实际九次覆盖

保持 R1059–R1060 的原函数与微分：
$$
p=6N+5\ge41,\quad n=(p-2)/3,\quad
s^2=-3,\quad\kappa=3s,
$$
$$
X=X_0(108):\quad z^3=1-\kappa x^3,\qquad
w^3=1+\kappa x^3,\qquad
\Omega=\frac{dx}{z^2w^2}.
$$
这里 $w$ 是 R1059 的 $w_0$，不是原深盘参数。
在代数闭域上令 $(\mu_3)^3$ 逐坐标作用，指数记为
$(a,b,c)\in\mathbf F_3^3$。取实际子群
$$
H=\{2a+b+c=0\},\qquad |H|=9.
$$
设 $t=x^3$、$v=x^2zw$，则它们均为 $H$ 不变量，并满足
$$
v^3=t^2(1+27t^2).
$$
三个 Kummer 根 $x,z,w$ 在 $t=0,\kappa^{-1},-\kappa^{-1}$
分别有独立的非三倍赋值，故 $[k(X):k(t)]=27$；
$v$ 的三次方在零点有二阶零，不是立方，故
$[k(t,v):k(t)]=3$。于是 $k(t,v)=k(X)^H$。

置
$$
R=v/t=zw/x,\qquad Y=54t-R^3=27x^3-x^{-3}.
$$
由 $R^3=t^{-1}+27t$ 得
$$
\boxed{\quad C:\ Y^2=R^6-108,\qquad \pi:X\longrightarrow C.\quad}
\tag{1061.1}
$$
反式 $t=(Y+R^3)/54$、$v=Rt$ 证明这是准确商函数域。
$p>3$ 时 $C$ 光滑、亏格二；R1059 的实际 $X$ 亏格十。
$\pi$ 可分且次数九，Riemann–Hurwitz 给
$2\cdot10-2=9(2\cdot2-2)$，总分歧除子为零。
所以 $\pi$ 是原曲线上的实际无分歧 $H$-覆盖。

直接微分，不留待定常数：
$$
\frac{dR}{dx}=\frac{27x^6-1}{x^2(zw)^2},\qquad
Y=\frac{27x^6-1}{x^3},
$$
因而
$$
\boxed{\quad
\pi^*(dR/Y)=x\Omega,\qquad
\pi^*(R\,dR/Y)=zw\Omega.
\quad}
\tag{1061.2}
$$
它们分别是 R1059 的实际 $c\,dq/q$ 和 $h\,dq/q$。

## 2. 原互逆角色对应的明确三挠线

令 $P_+,P_-$ 是 $C$ 的两个无穷点，以 $Y/R^3\to\pm1$ 标号；
令
$$
Q_z=(0,-6s),\qquad Q_w=(0,6s).
$$
$t=(Y+R^3)/54$ 满足
$$
\operatorname{div}(t)=3(P_--P_+),\quad
\operatorname{div}(1-\kappa t)=3(Q_z-P_+),\quad
\operatorname{div}(1+\kappa t)=3(Q_w-P_+).
$$
例如在 $t=\kappa^{-1}$，$R^3=t^{-1}+27t$ 对 $t$ 的导数为 $54$，
所以 $1-\kappa t$ 在 $Q_z$ 有准确三阶零。又
$$
\operatorname{div}(R)=Q_z+Q_w-P_+-P_-.
$$
因此
$$
D_\chi=Q_z-Q_w,\qquad
3D_\chi=\operatorname{div}
\left(\frac{1-\kappa t}{1+\kappa t}\right),\qquad
(z/w)^3=\frac{1-\kappa t}{1+\kappa t}.
\tag{1061.3}
$$
这是原覆盖内的具体 Kummer 线，不是任取三挠点。

它还来自实际二次椭圆映射
$$
q:C\longrightarrow E,\qquad
E:V^2=U^3-108,\quad U=R^2,\quad V=Y.
$$
令 $Q=(0,-6s)\in E$，则水平切线 $V=-6s$ 与三次曲线在 $Q$
有三重交点，所以 $Q$ 的阶恰为三。
$q^*Q=2Q_z$，$q^*O=P_++P_-$，结合 $\operatorname{div}(R)$ 得
$$
\boxed{\quad [D_\chi]=q^*[Q-O]\ne0.\quad}
\tag{1061.4}
$$
非零也可由 $\operatorname{Nm}_q q^*=[2]$ 在三挠上可逆直接确认。
$q$ 的分支点恰为 $Q,-Q$；
$\operatorname{div}(U)=Q+(-Q)-2O$，故双覆盖的分支平方根线是
$\mathcal O_E(O)$。实际微分满足
$$
q^*\left(\frac{dU}{2V}\right)=R\,dR/Y.
$$
此处使用的是 $U=R^2,V=Y$ 这个因子，没有换成 $R^{-2}$ 的另一椭圆因子。

因 $s^p=-s$，Frobenius 交换 $Q_z,Q_w$，故
$D_\chi^{(p)}=-D_\chi$。下文始终保留无序 pair
$\{\mathcal O(D_\chi),\mathcal O(-D_\chi)\}$ 的实际 Frobenius twist。

## 3. 八个非平凡角色的全部微分和 Cartier 输入

在 $H$ 内写 $c=a-b$。十条实际正则微分的角色为：

| 微分 | $H$ 指数角色 |
| --- | --- |
| $x\Omega,\ zw\Omega$ | $0$ |
| $\Omega,\ x^2\Omega$ | $2a,\ a$ |
| $z^2\Omega,\ w^2\Omega$ | $-(a+b),\ a+b$ |
| $z\Omega,\ w\Omega,\ xz\Omega,\ xw\Omega$ | $2a+b,\ -b,\ b,\ a-b$ |

八个非平凡角色各出现一次。也可直接由无分歧覆盖和 Riemann–Roch：
非平凡度零线 $\mathcal L$ 满足
$h^0(C,\Omega_C^1\otimes\mathcal L)=1$。

在指数记号下 $a=b+c$，原有序两条微分
$$
u=z^2\Omega=(a(q)-\zeta b(q))\,dq/q,\qquad
\nu=w^2\Omega=(a(q)-\zeta^2b(q))\,dq/q
$$
的角色正是 $b-c$、$c-b$，与 $z/w$ 互逆。
此处右侧 $a(q),b(q)$ 是 R1059 的固定形式，区别于本节的角色指数。
所以 (1061.3) 定位的正是原 $S_n$ 所用的两条线。

R1060 已给六条 CM 微分的 Cartier 为零；
在原 $p\bmod9\in\{2,5\}$ 范围，另外四条非 CM 微分的 Cartier 可逆。
因此上述四条非平凡 CM 角色各有一维 exact 微分空间，
四条非 CM 角色则没有 exact 微分。

底曲线 $C$ 本身的 Cartier 矩阵也准确为零：
$$
Y^{-1}=Y^{-p}(R^6-108)^{(p-1)/2}.
$$
以 $dR/Y,R\,dR/Y$ 为基，矩阵读取指数
$p-1,p-2,2p-1,2p-2$。它们模六分别为 $4,3,3,2$，
而所写多项式只含六倍数次项，故全部为零。
所以该亏格二曲线是 superspecial；它不是 ordinary 曲线。

## 4. 原 Raynaud–Petri 读数的严格下降

令 $F_C:C\to C^{(p)}$ 为相对 Frobenius，
$B_C$ 是 locally exact differential bundle：
$$
0\longrightarrow\mathcal O_{C^{(p)}}
\longrightarrow F_{C*}\mathcal O_C
\longrightarrow B_C\longrightarrow0.
$$
无分歧覆盖的 Frobenius base change 给
$\pi^{(p)*}B_C\simeq B_X$。
分解 $\pi^{(p)}_*\mathcal O_{X^{(p)}}$ 的实际 $H$ 角色后，
$u,\nu$ 正给
$$
H^0(C^{(p)},B_C\otimes\mathcal L),\qquad
H^0(C^{(p)},B_C\otimes\mathcal L^{-1})
$$
的各一维空间，其中
$$
\{\mathcal L,\mathcal L^{-1}\}
=\{\mathcal O(D_\chi),\mathcal O(-D_\chi)\}^{(p)}.
$$
上述维数一来自实际角色及 Cartier 核，未借助待证的 theta 光滑性。

用 R1059 的原有序配对规范
$\beta(\omega,\eta)=\mathscr C(F_\omega\eta)$、$dF_\omega=\omega$。
R1060 的已付 Euler 身份为
$$
s\kappa^n=(-1)^{N+1}3^{(p-1)/2}=1,
$$
因为 $(3/p)=(-1)^{N+1}$。
所以 $\kappa^n=1/s$，不是另一次单位重标。
R1059 的准确半线性给
$$
\beta_X(\nu,u)=(\kappa^nS_n)^{1/p}zw\Omega
=-\frac{S_n}{s}zw\Omega,
$$
$$
\boxed{\quad
\beta_X(u,\nu)=\frac{S_n}{s}zw\Omega
=\pi^*\left(\frac{S_n}{s}R\,dR/Y\right).
\quad}
\tag{1061.5}
$$
逆角色乘积按原覆盖的乘法下降，故 (1061.5) 就是 $C$ 上这两个
一维空间的 Raynaud 乘法。$C$ 的模型在 $\mathbf F_p$，
上式在相对 Frobenius 模型下采用同一坐标识别。
若交换输入顺序，符号随之改变；没有省去 $\mathbf F_{p^2}$ 半线性。

## 5. 精确的 theta 光滑性判据和剩余问题

令 $\Theta_{B_C}\subset\operatorname{Jac}(C^{(p)})$
为 $B_C$ 的 determinant theta 除子。
Tong 的 Proposition 2.2.1、Corollary 2.2.2 说明：
在给定线 $\mathcal L$ 处，它光滑当且仅当
$h^0(B_C\otimes\mathcal L)=1$，且与逆线的一维空间乘法非零；
光滑时，切空间是该乘法输出微分的 annihilator。

本文已支付维数一及实际输出，故
$$
\boxed{\quad
S_n\ne0
\quad\Longleftrightarrow\quad
\Theta_{B_C}\text{ 在原实际三挠点 }\mathcal L\text{ 光滑}.
\quad}
\tag{1061.6}
$$
逆点给同一个条件。若光滑，其切线准确是
$H^1(C^{(p)},\mathcal O)$ 中 $R\,dR/Y$ 的 annihilator。
结合 R1059–R1060，
$$
A_p=-S_n/3,\qquad
f_N=\frac{t_{\rm CM}^2\delta'_p}{4(p+1)}A_p,\quad t_{\rm CM}^3=4,
$$
这仍是原 $f_N$ 的具体问题。

在 $p\bmod9\in\{2,5\}$，另外两条非 CM 角色直线上的四个三挠点不在
$\Theta_{B_C}$，由 R1060 ordinary 输入得到；这不推出目标点光滑。
Tong §4.2 的相应特殊光滑定理讨论 $p$ 挠点及指定的
ordinary / $p$-rank 条件，不能套给本 superspecial 曲线的三挠点。
后续须继续支付 (1061.6) 的右侧，或在同一实际双覆盖上求其
twisted-Cartier 导数；原同一本原标签筛选和 O0 仍未关闭。

## 来源与本次核对

- [R1059](R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：原 $X_0(108)$ 函数、good 模型、固定微分尺度和 $S_n$ 配对。
- [R1060](R1060-actual-X108-nonCM-Cartier-and-nine-torsion-ordinary-input.md)：六条 CM 核、四条非 CM ordinary 输入及准确 Euler 标量。
- Jilong Tong, *Diviseur thêta et formes différentielles*, Math. Z. 264 (2010), 521–569，DOI 10.1007/s00209-009-0478-y；[作者原文](https://www.math.u-bordeaux.fr/~jtong/Recherche/Theta.pdf)，Proposition 2.2.1、Corollary 2.2.2（印刷541–542页），§4.2。此处只使用其准确光滑判据，不假设本固定曲线一般。

o1_theta给实际覆盖、三挠线和配对下降；o2_high_coefficient独立核角色、第一椭圆因子与分支线；root实读Tong所引原文，并手核全部函数域次数、无分歧性、两微分、divisor、角色、Frobenius及有序标量。无数学程序或窗口执行。
