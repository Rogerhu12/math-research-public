# R64：一般外头的完整 mean 根与兼容高度缺陷界

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明，条件性定量工具。** 本结果在 R44 的一般完整 mean 方程上给出只需有限二次平均和标量级数尾的连续证书，不要求归一强范数小于 $1/32$。其条件仍须由同一个实际径向候选的连续包围核销；有限连接根的数值收敛和端点正分母不能代替该门。

实际动机是 cell0 的保存 M20 内部候选：原段端的归一 $W_{1/64,1}$ 范数可达约 $0.432$，而真实几何分母仍可正。内头 R58 的小球及其参数域不改变。本文不是将大外头域套回 R33，也不声称已经得到准确外头解。

## 1. 输入和记号

取同一个真实背景 $g=E\,dr^2+r^2d\theta^2$，其中 $E=1+w^2$、$w>0$，并取一个明确的非均值 $C^2$ 高度 $H$。在原 source 坐标 $x$ 上令

$$
P=\frac{H_\theta}{rw},\qquad \bar K=\frac{H_r}{w},\qquad
s=\frac{r_x}{r}>0,\qquad \ell=\frac{w_x}{w},\qquad z=w^2,
\qquad T=P_\theta .
\tag{64.1}
$$

所有场及背景包围必须属于同一个连续径向表示。特别地，$\bar K_x$ 是该表示的实际导数。R48 的分段正权积分高度可以作为输入，只要各段共享同一物理二阶端点 jet。

记 $\|\cdot\|_0=\sum_m|f_m|$，而 $\|\cdot\|_\tau=\sum_m(1+|m|)e^{\tau|m|}|f_m|$。两者都是 Banach 代数范数，后者的含义与 R44 一致。所有以下上、下界均可在一个完整真实径向面板上同时成立。

完整 mean 仍由 R44 定义。令 $K=c+\bar K$、$y=1+K$，以及

$$
\begin{aligned}
A&=2K+K^2+EP^2,&u&=zA,&v&=zP^2,\\
S&=1-v,&D&=1-u,&L&=y+ET,\\
N&=1+\frac{zyT}{S},&
\mathcal M(c)&=\left\langle A C_1(u)+\frac{yT}{S}C(u)\right\rangle ,
\end{aligned}
\tag{64.2}
$$

其中 $C(u)=(1-u)^{-1/2}$、$C_1(u)=(C(u)-1)/u$，在零点取连续值 $1/2$。这是完整角平均，没有角采样、均值截断或对小 $z$ 的数值相减。

## 2. 在 $c=0$ 的快速完整平均界

设 $p_0\ge\|P\|_0$、$k_0\ge\|\bar K\|_0$、$t_0\ge\|T\|_0$。令

$$
A_0=2k_0+k_0^2+Ep_0^2,\qquad
U_0=zA_0<1,\qquad V_0=zp_0^2<1,\qquad
Y_0=(1+k_0)t_0.
\tag{64.3}
$$

对 $0\le q<1$ 定义两个无相减正函数

$$
f(q)=\frac{q(2+\sqrt{1-q})}{2\sqrt{1-q}(1+\sqrt{1-q})^2},
\qquad
g(q)=\frac{q}{\sqrt{1-q}(1+\sqrt{1-q})}.
\tag{64.4}
$$

定义准确的有限二次平均

$$
q_0=\left\langle\frac{\bar K^2+EP^2}{2}+\bar K T\right\rangle .
\tag{64.5}
$$

若 $P,\bar K$ 是有限 Fourier 场，此数只需完整二次卷积的零系数。对当前实 cosine 高度，写 $\bar K=\sum_{m>0}k_m\cos m\theta$、$P=\sum_{m>0}p_m\sin m\theta$，则

$$
q_0=\frac14\sum_{m>0}(k_m^2+Ep_m^2)
       +\frac12\sum_{m>0}m k_m p_m.
\tag{64.6}
$$

保留此式的符号与相消，不能将每一项先独立取绝对值再称为同样紧的平均值。

**引理 64.1。** 有

$$
|\mathcal M(0)-q_0|
\le A_0 f(U_0)+Y_0\frac{g(U_0)+V_0}{1-V_0}
=:\mathcal E_0 .
\tag{64.7}
$$

**证明。** 正系数展开给
$\|C_1(u)-1/2\|_0\le C_1(U_0)-1/2=f(U_0)$、
$\|C(u)-1\|_0\le g(U_0)$。又

$$
\left\|\frac{C(u)}{1-v}-1\right\|_0
\le\frac{g(U_0)+V_0}{1-V_0}.
$$

将 (64.2) 分为 $A/2+yT$ 与这两项余量。$c=0$ 时 $\langle\bar K\rangle=\langle T\rangle=0$，其主平均正是 (64.5)。Banach 代数乘法界和零系数的范数界给 (64.7)。公式 (64.4) 由 $1-\sqrt{1-q}=q/(1+\sqrt{1-q})$ 直接整理，故小 $z$ 时没有消去有效数字的相减。证毕。

## 3. 一般单调根门

取任意明确 $d>0$。在 $|c|\le d$ 上对 $i=0,\tau$ 记

$$
k_i^*=k_i+d,\qquad
U_i^*=z(2k_i^*+(k_i^*)^2+Ep_i^2),\qquad
V_i=zp_i^2,
\tag{64.8}
$$

其中 $k_i,p_i$ 分别为相应范数的连续上界。还取
$\lambda_i\ge\|\bar K+ET\|_i$，应按完整系数 $k_m+Em p_m$ 计算以保留相消。假设

$$
\begin{gathered}
U_i^*<1,\quad V_i<1\quad (i=0,\tau),\\
y_*=1-d-k_0>0,\qquad
L_*=1-d-\lambda_0>0,\\
N_*=1-\frac{z(1+d+k_0)t_0}{1-V_0}>0,\qquad
a_\tau=1-d-\lambda_\tau>0.
\end{gathered}
\tag{64.9}
$$

真实角上 $S,D,y,N,L$ 因此全正，且角 Wiener 逆 $L^{-1}$ 有界。令

$$
\mu_d=\frac{L_*}{(1+U_0^*)^{3/2}},\qquad
\epsilon_0\ge |q_0|+\mathcal E_0 .
\tag{64.10}
$$

**定理 64.2。** 如果

$$
\epsilon_0<\mu_d d,
\tag{64.11}
$$

则存在唯一的完整 mean 根 $c\in(-d,d)$，并且

$$
|c|\le c_*:=\epsilon_0/\mu_d<d.
\tag{64.12}
$$

该根随同一个 $C^2$ 高度候选和 $C^1$ 背景连续、$C^1$ 地变化；共有物理两阶 jet 的分段候选给同一个 $C^1$ 根。

**证明。** R44 的准确公式 $\mathcal M_c=\langle L D^{-3/2}\rangle$ 给 $\mathcal M_c\ge\mu_d>0$。引理 64.1 和 (64.11) 使 $\mathcal M(-d)<0<\mathcal M(d)$，故存在唯一根并有 (64.12)。严格余量及隐函数定理给局部 $C^1$ 性。若不同连续面板使用不同 $d$，这些区间都以零为中心；公共点较小区间包含于较大区间，其根由唯一性相同。公共物理 jet 的导数亦相同，故局部根拼接。没有对归一 $p_\tau+k_\tau$ 施加 $1/32$ 小球条件。证毕。

## 4. 完整径向残差和 mean 导数

以下可将 (64.8)–(64.10) 中的 $d$ 换成已证 $c_*$，得到更紧的根处域界及 $\mu_*>0$。定义 R44 的完整非线性项

$$
\mathcal N=
\frac{Es(K_\theta-P)^2+
\ell\big((K+T)^2+z(2KT+T^2-P^2)\big)}{L}.
\tag{64.13}
$$

对 $i=0,\tau$，令 $u_i\ge\|K_\theta-P\|_i$、
$b_i\ge\|\bar K_x+\ell(2\bar K+T)\|_i$、$k_i^*=k_i+c_*$。则

$$
\begin{aligned}
N_i^*&=
\frac{Esu_i^2+|\ell|\big[(k_i^*+t_i)^2+
z(2k_i^*t_i+t_i^2+p_i^2)\big]}{1-c_*-\lambda_i},\\
R_i^*&=b_i+N_i^* .
\end{aligned}
\tag{64.14}
$$

这是完整非均值残差

$$
R_\perp=\bar K_x+\ell(2\bar K+T)-\mathscr P_\perp\mathcal N
\tag{64.15}
$$

的 $i$ 范数上界。全部 mean 和有理分母产生的高频都包含在 $N_i^*$ 中。

令 $U_0^*$ 使用根处 $c_*$，并取

$$
W_0^*=(c_*+\lambda_0)(1-U_0^*)^{-3/2}
              +(1-U_0^*)^{-3/2}-1,
\qquad
a^*=\frac{W_0^*R_0^*}{\mu_*}.
\tag{64.16}
$$

则实际 mean 导数及完整有限 $\mathcal J$ 满足

$$
|c_x|\le a^*+2|\ell|c_*+N_0^*=:c_x^*,
\qquad
\|\mathcal J\|_\tau\le(1+c_*+\lambda_\tau)(R_\tau^*+a^*).
\tag{64.17}
$$

**证明。** 高度兼容和完整 mean 根给 R44 的准确加权恒等式
$\langle\mathcal J D^{-3/2}\rangle=0$。写
$\mathcal J/L=a+R_\perp$，其中
$a=c_x+2\ell c-\langle\mathcal N\rangle$。
由于 $\langle R_\perp\rangle=0$，

$$
a=-\frac{\langle(LD^{-3/2}-1)R_\perp\rangle}
         {\langle LD^{-3/2}\rangle}.
$$

零条带无角权范数给 (64.16)，再取 $\mathcal J=L(a+R_\perp)$ 的 $\tau$ 范数即得 (64.17)。$\bar K_x$ 始终是实际候选导数，未用右端将残差置零。证毕。

因此全部角上的物理 Darboux 缺陷、非均值第二源和 mean 二阶偏差分别有

$$
|\operatorname{Darboux}(H+h_0)|
\le\frac{w^2}{r r_xE^2}\|\mathcal J\|_\tau,
\qquad
\|\text{第二物理源}\|_\tau\le\frac{w}{r_x}R_\tau^*,
\tag{64.18}
$$

$$
|h_{0,rr}-w_r|\le\frac{w}{r_x}(c_x^*+|\ell|c_*).
\tag{64.19}
$$

非均值物理二阶导数应优先直接计算同一系数中的 $\bar K_x+\ell\bar K$，再乘 $w/r_x$；这保留真实径向相消。

## 5. 应用范围

定理 64.2 与第 4 节只需要有限 Fourier 输入、完整 true-background 面板和实际候选导数，不要求未知准确径向解被截断成有限频率。得到的 $h_0$ 保留完整 mean 根，候选的全部连续缺陷得到显式上界。接到准确解仍需真实外 Green/Schur、内头完整 trace 和映射收缩预算。

单切口自由 cuff 的 mean 高度常数按 [mean 平移说明](../notes/2026-11-12-tail-mean-height-translation-and-one-cut.md) 处理。本定理只补完整 mean 根及其导数，不增加题目没有规定的绝对高度条件。
