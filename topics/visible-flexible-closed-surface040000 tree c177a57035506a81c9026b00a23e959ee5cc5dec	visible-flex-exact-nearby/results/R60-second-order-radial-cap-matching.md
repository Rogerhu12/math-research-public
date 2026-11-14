# R60：单谐波径向帽的全二阶匹配与非倍频共振

**状态：已证明；v2全文经未参与者root独立审查后正式采纳。**
2026-11-10；Astra-visible-flex-78718bd0 / geometric_closure。

本稿给出实际正则圆盘上的二阶等距变分，连同一个真正平面闭柱边族的
完整两阶数据；不只消去平均模态。准确谱假设为：某个整数 $n\ge2$
共振，而 $2n$ 不共振。末节证明这些条件可在同一个固定 $C^\infty$
旋转帽上同时实现，保留开圆柱入口与圆球开核心。

这个结果不构造精确非线性等距族。固定非零参数下的三阶截断缺陷不随
空间加密消失，所以它不支付本题 G5，也没有闭面、固定开 $H$ 或目标比例。

## 1. 来源与符号

使用正式 [R58](../results/R58-radial-cap-linear-matching-conditions.md)
中的完整 Gauss–Codazzi、真实柱边和球心规范，以及正式
[R59](../results/R59-second-order-mean-compatibility.md) 的平均恒等式。
R59 已由未参与者 independent_audit 全文审查，本次作者不把自己采用
该恒等式称为对它的独立重认证。

另读了旧作者稿
[无限线性模](../notes/2026-11-10-db6f-smooth-radial-cap-infinite-linear-modes-v1.md)。
本稿末节只需要其有限步骤的思路；所需的相位跨越、梯度独立和几何
输入均在本文完整证明，不以无限极限结论作为依赖。该旧稿现已另审并登记为R61。

固定

$$
g=dr^2+a(r)^2du^2,\qquad 0\le r<T,\qquad u\in\mathbb R/(2\pi\mathbb Z),
\tag{1}
$$

以及旋转基态

$$
F_0(r,u)=(a(r)\cos u,a(r)\sin u,Z(r)),\qquad
b=Z_r=\sqrt{1-a_r^2}>0.
\tag{2}
$$

假设去中心区 $a>0$、$a,b$ 光滑；入口一个开区间内 $a=b=1$；
中心附近以 $\rho=T-r$ 有

$$
a=\sigma\sin(\rho/\sigma),\qquad b=a/\sigma,
\qquad t=\tan(\rho/(2\sigma)).
\tag{3}
$$

中心使用真正 Cartesian 材料坐标 $w=t e^{iu}$。
第二形式分量的约定为
$II=L\,dr^2+2M\,dr\,du+C\,du^2$，基态

$$
L_0=-a_{rr}/b,\qquad M_0=0,\qquad C_0=ab.
\tag{4}
$$

记

$$
P=aa_{rr}/b^3,\qquad R=b/a^2,
\qquad \mathcal L_N z=(z_r/R)_r+N^2Pz.
\tag{5}
$$

对 $N\ge2$，从球核心的 $v_N=t^N$ 向入口延伸
$\mathcal L_Nv_N=0$，定义 $D_N=(v_N)_r(0)$。
中心稳定分支是一个一维实空间，故 $D_N=0$ 与其归一化无关。

## 2. 主命题：条件全二阶可解

假设对某个整数 $n\ge2$ 有

$$
D_n=0,\qquad D_{2n}\ne0.
\tag{6}
$$

则存在全盘光滑向量场 $V,W$，使

$$
\widetilde F_\tau=F_0+\tau V+\tau^2W
\quad\text{满足}\quad
\widetilde F_\tau^*g_{\mathbb R^3}=g+O(\tau^3)
\tag{7}
$$

于任意固定 $C^k$ 范数。$V$ 不是无穷小刚体运动。还能同时构造一个
真正单位速率、同材料周长 $2\pi$、严格凸且 $n$ 折对称的平面闭曲线族
$\Gamma_\tau(u)$，其圆柱图

$$
F^{\rm cyl}_\tau(r,u)=\Gamma_\tau(u)+r e_z
\tag{8}
$$

在入口开柱上与 (7) 的参数零、一、二阶系数完全相同。
这个结论包括真正中心的全部光滑性、边位置闭合、标架和第二形式两阶，
不只是径向 ODE 某个端点的有限残差。

## 3. 第一阶及二阶强迫的准确频率

由 $D_n=0$，取唯一满足 $v(0)=1,v_r(0)=0$ 的正则实解
$\mathcal L_n v=0$。令

$$
p=\frac{v_r}{nR},\qquad
\zeta_1=v\cos(nu),\qquad x_1=p\sin(nu).
\tag{9}
$$

于是

$$
p_r=-nPv,\qquad v_r=nRp,
\quad x_1=a m_1,\quad\zeta_1=bc_1/a,
\quad \ell_1=\frac{a_{rr}}{ab^2}c_1.
\tag{10}
$$

这给完整线性 Gauss–Codazzi。入口 $p=0,v=1$，所以
$m_1=\ell_1=0,c_1=\cos(nu)$。球核心存在非零常数 $d$ 使

$$
v=d t^n,\qquad p=-\sigma d t^n,
\qquad II_1=\operatorname{Re}(-\sigma d\,w^{n-2}dw^2).
\tag{11}
$$

特别地，第一阶在真实中心解析。

按照无阶乘的展开 $II_\tau=II_0+\tau II_1+\tau^2II_2$，二阶
Gauss 方程为

$$
\ell_2=\frac{a_{rr}}{ab^2}c_2+S,
\qquad S=\frac{m_1^2}{ab}-\frac{a_{rr}c_1^2}{a^2b^3}.
\tag{12}
$$

代入 (9) 后恰有

$$
S=S_0+S_2\cos(2nu),
\tag{13}
$$

$$
S_0=\frac12\left(\frac{p^2}{a^3b}-\frac{a_{rr}v^2}{b^5}\right),
\qquad
S_2=-\frac12\left(\frac{p^2}{a^3b}+\frac{a_{rr}v^2}{b^5}\right).
\tag{14}
$$

入口开柱上 $S_0=S_2=0$。球核心上由 (3)、(11) 精确得到

$$
S_2=0,\qquad
S_0=\frac{\sigma^3d^2t^{2n}}{a^4}
=\frac{d^2}{16\sigma}t^{2n-4}(1+t^2)^4.
\tag{15}
$$

所以倍频强迫在球核心**恒零**；它可能在非球桥段非零。

## 4. 零模与真正中心

令 $x_{2,0}=0$，并置

$$
z_0(r)=\int_0^r ba_rS_0\,ds.
\tag{16}
$$

R59 定理的假设全部由 (1)–(3)、(9)–(11) 满足，故
$\int_0^Tba_rS_0dr=0$。因此 (16) 在两个端点都取零。
在入口开柱上 $z_0=0$。在球核心，利用中心零值积分得到

$$
z_0=\frac{d^2}{4}
\left(\frac{t^{2n-2}}{2n-2}-\frac{t^{2n+2}}{2n+2}\right).
\tag{17}
$$

对应二阶零模为

$$
c_{2,0}=\sigma z_0,\quad m_{2,0}=0,
\quad \ell_{2,0}=S_0-\frac{\sigma z_0}{a^2}.
\tag{18}
$$

它是一个真正光滑的 Cartesian 张量：正交径向、角向分量
$A_0=\ell_{2,0}$、$B_0=c_{2,0}/a^2$ 都是 $t^2$ 的解析函数，
并且 $A_0-B_0$ 被 $t^2$ 整除。后一点在 $n>2$ 时直接由首项阶数成立；
在 $n=2$ 时，(15)、(17) 给

$$
S_0(0)=\frac{d^2}{16\sigma},\qquad
\lim_{t\to0}\frac{\sigma z_0}{a^2}=\frac{d^2}{32\sigma},
$$

所以常数项也抵消。
具体写 $w=x+iy$、$t^2=x^2+y^2$ 以及
$\lambda=2\sigma/(1+t^2)$，张量 (18) 等于

$$
\lambda^2\left[
B_0(dx^2+dy^2)
+\frac{A_0-B_0}{t^2}(x\,dx+y\,dy)^2\right],
\tag{19}
$$

从而在中心解析。这一步核的是完整二阶零模张量，强于仅有
$c_{2,0}=O(\rho^2)$ 的必要阶数。

## 5. 非零倍频的精确非齐次边值问题

写 $N=2n$，求

$$
\zeta_2=z_0+z\cos(Nu),\qquad x_2=y\sin(Nu).
\tag{20}
$$

二阶 Codazzi 为

$$
y_r=-N(Pz+aS_2),\qquad
z_r=NRy+ba_rS_2.
\tag{21}
$$

消去 $y$ 得

$$
\boxed{\quad
\mathcal L_Nz=(a^2a_rS_2)_r-N^2aS_2 .\quad}
\tag{22}
$$

柱边需要 $y(0)=0$，由 $a_r(0)=0$ 等价于 $z_r(0)=0$；
$z(0)$ 由中心正则性决定，并不先指定。

令 $q_N$ 为齐次方程 $\mathcal L_Nq_N=0$ 的入口解
$q_N(0)=1,(q_N)_r(0)=0$；令 $z^p$ 为 (22) 的零 Cauchy 初值解。
因为源在球核心恒零，两者在该核心分别写成

$$
q_N=A_qt^N+B_qt^{-N},\qquad z^p=A_pt^N+B_pt^{-N}.
\tag{23}
$$

$B_q\ne0$：否则 $q_N$ 属于中心正则分支，同时入口导数为零，
这就意味着 $D_N=0$，与 (6) 矛盾。于是唯一选择

$$
\alpha=-B_p/B_q,\qquad z=z^p+\alpha q_N
\tag{24}
$$

消去增长支。由 (21) 还原

$$
y=\frac{z_r-ba_rS_2}{NR},\qquad
c_{2,N}=\frac ab z\cos(Nu),\quad
m_{2,N}=\frac ya\sin(Nu),
\tag{25}
$$

再用 (12) 取 $\ell_{2,N}$。这确实满足两条 (21)：将 (25) 微分，
正是 (22)；没有丢失原方程。

球核心上 $z=d_2t^N,y=-\sigma d_2t^N$，从而

$$
II_{2,N}=\operatorname{Re}(-\sigma d_2 w^{N-2}dw^2),
\tag{26}
$$

在中心解析。与 (19) 相加，给一个全盘光滑 $II_2$。
在入口开柱上 $z=\alpha,y=0,z_0=0$，所以

$$
\ell_2=m_2=0,\qquad c_2=\alpha\cos(2nu).
\tag{27}
$$

## 6. 柱边不是形式闭合：构造真正曲线族

取

$$
f_1(u)=\frac{\sin(nu)}n,\qquad
f_2(u)=\frac{\alpha\sin(2nu)}{2n},
\tag{28}
$$

并将平面识别为复数，定义

$$
T_\tau(u)=i\exp i\bigl(u+\tau f_1(u)+\tau^2f_2(u)\bigr),
\qquad
\Gamma_\tau(u)=1+\int_0^uT_\tau(s)ds.
\tag{29}
$$

$|T_\tau|=1$ 精确成立。令 $\omega=2\pi/n$，则
$T_\tau(u+\omega)=e^{i\omega}T_\tau(u)$，故

$$
\int_0^{2\pi}T_\tau(u)du
=\left(\sum_{j=0}^{n-1}e^{ij\omega}\right)
\int_0^\omega T_\tau(u)du=0.
\tag{30}
$$

因此曲线真实闭合，包含所有高阶参数项。其曲率恰为

$$
\kappa_\tau=1+\tau\cos(nu)+\tau^2\alpha\cos(2nu),
\tag{31}
$$

小 $|\tau|$ 时处处为正。它在 $C^\infty$ 中接近单位圆，因而是严格凸
嵌入；也可用正曲率与总转角 $2\pi$ 证明严格凸性。
其 $n$ 折旋转中心可以随参数平移，但 (29) 已给固定材料锚点；这不影响
任何匹配。

圆柱族 (8) 的第二形式恰为 $L=M=0,C=\kappa_\tau$，与 (10)、(27)
逐阶一致。首点位置、切向与 $e_z$ 规范可以同时选取，故并非只匹配了曲率
而忘记位置或标架。

## 7. 二阶 Gauss–Codazzi到实际光滑二阶位置场

在整个圆盘选择光滑定向正交切标架与法向构成 $E_0$，不用极点奇异标架。
令固定度量的正交余标架为 $\theta=(\theta^1,\theta^2,0)^T$。
以二阶第二形式构造反对称连接

$$
\Omega_\tau=\Omega_0+\tau\Omega_1+\tau^2\Omega_2.
$$

完整的零、一、二阶 Gauss–Codazzi 已经证明，故

$$
d\Omega_\tau+\Omega_\tau\wedge\Omega_\tau=O(\tau^3),
\quad
d\theta+\Omega_\tau\wedge\theta=0.
\tag{32}
$$

最后一式对每阶精确成立，因为第一基本形式固定而各阶第二形式对称。
在空间规范下记 $\Psi_j=E_0\Omega_jE_0^{-1}$。
由 (32)，

$$
d\Psi_1=0,\qquad d\Psi_2+\Psi_1\wedge\Psi_1=0.
\tag{33}
$$

先积分 $dU_1=\Psi_1$，再积分

$$
dU_2=U_1\Psi_1+\Psi_2.
\tag{34}
$$

(33) 正好使第二个右端也闭。圆盘单连通，两个积分全局存在且光滑。
锚点处按照真实柱边标架族的两阶数据选常数后，
$E_\tau=(I+\tau U_1+\tau^2U_2)E_0$ 是到二阶正交的标架：
这一点也直接由反对称连接和锚点的正交性沿路径保持得到。

由 (32) 的无挠式，一形式 $U_1dF_0,U_2dF_0$ 都闭，故可积分

$$
dV=U_1dF_0,\qquad dW=U_2dF_0.
\tag{35}
$$

锚点积分常数同样取真实曲线 (29) 的两阶系数。
于是 $d\widetilde F_\tau=E_\tau\theta$ 到二阶成立，标架正交性给 (7)。
在入口开柱，位置/标架的各阶径向和角向 ODE 与 (8) 的真实 Taylor
系数相同，初始锚点亦相同，故由 ODE 唯一性在整个开柱上一致。
由于 $c_1=\cos(nu)\ne0$，$V$ 不能是无穷小刚体运动。

若只关心一个近似族，紧圆盘的嵌入在 $C^1$ 小扰动下保持，故 (7)
对小参数确实给光滑嵌入。但其度量的三阶缺陷仍然存在，不能称精确等距。

## 8. 完整非零模的 Fredholm 兼容式

上述倍频非共振为何有效，可用一个一般公式说明。设某一非零模 $N$
的二阶强迫为 $S_N$，在入口开柱为零，且实际中心阶数使以下端项存在并为零。
若 $v_N$ 是中心正则齐次解、$D_N=0$，则任何同时满足柱边零导数和
中心正则性的 (22) 解必须满足

$$
\boxed{\quad
\int_0^T
\bigl(a^2a_r(v_N)_r+N^2av_N\bigr)S_N\,dr=0.
\quad}
\tag{36}
$$

证明是把 (22) 乘 $v_N$，减去 $z\mathcal L_Nv_N$ 并积分。
Green 端项为 $(v_Nz_r-z(v_N)_r)/R$；它在柱端、正则球心都为零。
再对源项 $(a^2a_rS_N)_r$ 积分分部，得到 (36)。

在本文的 $N=2n$ 源中，$S_N$ 在球核心精确为零，所以无须额外猜测
中心端项。若 $D_{2n}=0$，(36) 就是不能跳过的额外条件；本稿不证明它自动为零。
若 $D_{2n}\ne0$，(24) 的构造则解决了完整边值问题。

## 9. 谱假设 (6) 在同一个光滑帽上确实可以实现

下面给有限步骤的存在证明，不使用无限模态极限。

### 9.1 一个带保留双曲窗口的帽

在轴高坐标 $Z$ 定义

$$
A_h(Z)=\sqrt{1+Z^2},\qquad
A_s(Z)=\sqrt{33-(Z-8)^2},\qquad H=8+\sqrt{33}.
$$

取一个固定光滑阶跃 $\chi$，在 $x\le0$ 为零，在 $x\ge1$ 为一，且在
两个端点全阶平坦。先于 $1/4<Z<1/2$ 将常数一光滑混合到 $A_h$，
再于 $15/4<Z<17/4$ 将 $A_h$ 光滑混合到 $A_s$。具体可取

$$
B(Z)=
\begin{cases}
1+\chi(4Z-1)(A_h-1),&Z\le15/4,\\
(1-\chi(2Z-15/2))A_h+\chi(2Z-15/2)A_s,&15/4\le Z\le17/4,\\
A_s,&Z\ge17/4.
\end{cases}
\tag{37}
$$

混合区两个半径都为正，故 $B>0$。它在 $[0,H)$ 光滑，具有真实开柱入口
和球面正则极点。所有变化只紧支于 $(1,3)$，且在 $C^2$ 中充分小，所以
那里始终 $A_{ZZ}/A>0$。不同 $Z$ 高度不同，故对应旋转帽始终嵌入。

在线性变量 $y=A\zeta$ 下，模态方程为

$$
y_{ZZ}+(N^2-1)q_Ay=0,\qquad q_A=A_{ZZ}/A.
\tag{38}
$$

入口条件是 $y(0)=1,y_Z(0)=0$。右端正则支从固定球核心向左延伸。
在 $Z=3$ 取两支 Wronskian 记为 $W_N(A)$，其零集恰是 $D_N=0$。

### 9.2 一个真实改变光学长度的控制

定义

$$
\mathcal S(A)=\int_1^3\sqrt{q_A}\,dZ.
$$

对紧支变分 $f$，直接微分并两次积分分部得

$$
D\mathcal S_A[f]=\int_1^3G_Af\,dZ,
\qquad
G_A=\frac12\left[((AA_{ZZ})^{-1/2})_{ZZ}
-q_A(AA_{ZZ})^{-1/2}\right].
\tag{39}
$$

在纯 $A_h$ 区，$(AA_{ZZ})^{-1/2}=A_h$，所以 $G_{A_h}=0$。
在 $Z_*=21/8$ 的小邻域取截止 $\eta=1$，支集位于 $(5/2,11/4)$，
令 $p(Z)=(Z-Z_*)^4\eta(Z)$。对充分小的 $\varepsilon>0$，
$A^{(0)}=B+\varepsilon p$ 仍满足全部几何条件，且

$$
G_{A^{(0)}}(Z_*)=-6\varepsilon A_h(Z_*)^4<0.
\tag{40}
$$

因为 $p$ 的零至三阶导数在该点为零、四阶为 $24$，(40) 从 (39)
逐项微分直接得到。取一个非负非零、支集足够小的 $f_*$，便有
$D\mathcal S_{A^{(0)}}[f_*]<0$。因此某个小闭参数区间中的
$A_s=A^{(0)}+sf_*$ 有不同端点光学长度，且在一个固定窗口
$J\subset(5/4,3/2)$ 仍精确等于 $A_h$。

### 9.3 命中一个整数模态

在 $[1,3]$ 作 Liouville 变换
$\xi=\int_1^Z\sqrt{q_{A_s}}$、$U=q_{A_s}^{1/4}y$，得

$$
U_{\xi\xi}+(\omega_N^2-V_s)U=0,\qquad
\omega_N=\sqrt{N^2-1},
\quad
V_s=\frac{q_{ZZ}}{4q^2}-\frac{5q_Z^2}{16q^3}.
\tag{41}
$$

$q$ 有共同正下界，且这条光滑有限参数曲线有共同 $C^4$ 界。
写 $U=\varrho\cos\vartheta,U_\xi=-\omega_N\varrho\sin\vartheta$，
则

$$
\vartheta_\xi=\omega_N-(V_s/\omega_N)\cos^2\vartheta,
\quad
\vartheta(3,s)=\vartheta(1)+\omega_N\mathcal S(A_s)+O(\omega_N^{-1}),
\tag{42}
$$

余项对参数一致。左右两个实际 Cauchy 直线及端点 Liouville 变换都不依赖
$s$，因为变化紧支于 $(1,3)$。对于任意充分大的整数 $N$，两个参数端点的
连续相位 lift 相差超过 $\pi$；中值定理使其命中固定的右正则目标直线
模 $\pi$，也即 $W_N(A_s)=0$。选一个这样的整数并记为 $n\ge2$，帽记 $A_*$。

### 9.4 保留 $n$，排除 $2n$

若 $W_{2n}(A_*)\ne0$，已完成。否则两个不同模态都共振。
在保留窗 $J$ 上，令 $\theta=\arctan Z$；每个共振模态的
$\zeta_N=y_N/A_h$ 写成

$$
\zeta_N=\alpha_N\cos(N\theta)+\beta_N\sin(N\theta),
\quad(\alpha_N,\beta_N)\ne(0,0).
$$

对 $f\in C_c^\infty(J)$，Wronskian 的导数是一个非零常数倍的
$\int_JK_Nf$，其中

$$
K_N=
\left(\frac{y_N^2}{A_h}\right)_{ZZ}
-q_{A_h}\frac{y_N^2}{A_h}
=\frac{2N^2}{A_h^3}
\left[(\beta_N^2-\alpha_N^2)\cos(2N\theta)
-2\alpha_N\beta_N\sin(2N\theta)\right].
\tag{43}
$$

这个变分式来自
$(\delta y_Z\,y-\delta y\,y_Z)_Z=-(N^2-1)\delta q\,y^2$，
$\delta q=(f_{ZZ}-qf)/A$，并两次积分分部。
括号振幅为 $\alpha_N^2+\beta_N^2>0$。对 $N=n,2n$，乘以 $A_h^3$
后为不同频率的非零三角函数，故在任何非空 $J$ 上线性独立。
因而存在 $f,g\in C_c^\infty(J)$，使

$$
(s,t)\longmapsto
\bigl(W_n(A_*+sf+tg),W_{2n}(A_*+sf+tg)\bigr)
$$

在原点的 Jacobian 可逆。有限维隐函数定理给任意足够小的非零 $\eta$
的一个真实剖面，其两个 Wronskian 精确为 $(0,\eta)$。
小扰动保留入口、中心和嵌入性。把这一个剖面固定，再改用经线弧长 $r$，
就得到满足 (1)–(6) 的同一个共同度量。

因此本稿不是对一个可能空的谱假设作条件推导；至少一类真实光滑帽满足它。
但 $n$、扰动参数及二阶场均为存在性对象，本文尚未给有效数值常数。

## 10. 下一道真实缺口：三阶共振模态

若继续按无阶乘约定展开，Gauss 的三阶强迫为

$$
S^{(3)}=
\frac{2m_1m_2-\ell_1c_2-\ell_2c_1}{ab}
=\frac{2m_1m_2-2(a_{rr}/(ab^2))c_1c_2-Sc_1}{ab}.
\tag{44}
$$

它含 $n$ 和 $3n$ 模；$n$ 本来就是共振模。因此 (36) 对其 $n$ 分量
成为一个新的实际兼容条件，不能通过自由选择柱边三阶 $n$ 振幅自动消去。
本文没有证明该三次系数为零；也没有由二阶可解推出全阶形式可解或收敛。

本稿的所有数学推导为纸面证明。附带代数核验若执行，仅核 (14)、(15)、
(17)、(19)、(22)、(41) 的符号恒等式；不产生数值帽、PDE 解、网格、
闭面或本题完成证据。后续应先独审本篇，再研究 (44) 的真实共振积分和
非线性消除机制，而非将本稿当作阶段性完成。

## 11. v2 订正与实际代数核验

v1 保留不改。未参与本稿推导的 root 全文审查指出 (19) 两项之间漏排加号；
v2 只在该公式补出 `+`，数学构造和其余正文未改。审稿结论另由 root 保存。

作者已在本环境实际运行 `python scripts/78718-geometry-check-second-order-cap.py`，
正常退出 0，7 个精确 SymPy 恒等式全部通过。这里只核代数，不运行 ODE、PDE、
谱求解或几何数组。

核验源码 SHA256：`f48f118525db19f463ea90c94bfc4cc1b722161e5aa9da3fe62ad99dd37a4216`。


## 12. 正式采纳记录

完整独审见 `notes/2026-11-10-78718-root-review-second-order-cap.md`。
审者逐节核一阶与二阶Gauss–Codazzi、真正中心、非共振消增长支、闭柱边、
全盘标架及位置积分、Prüfer相位和有限维谱控制；v1式(19)加号缺失已在v2订正。
所有原文其余数学范围保留。二阶近似不满足固定非零参数下的G5，不是精确帽或闭面。
