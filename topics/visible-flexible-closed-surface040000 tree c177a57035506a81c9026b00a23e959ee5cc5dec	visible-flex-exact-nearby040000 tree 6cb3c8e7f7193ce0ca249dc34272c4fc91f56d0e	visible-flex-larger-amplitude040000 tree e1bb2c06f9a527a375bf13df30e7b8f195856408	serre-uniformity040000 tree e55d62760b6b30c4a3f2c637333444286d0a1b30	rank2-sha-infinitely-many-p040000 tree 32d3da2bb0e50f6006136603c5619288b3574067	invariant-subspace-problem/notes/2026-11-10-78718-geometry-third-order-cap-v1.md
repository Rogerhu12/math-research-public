# 三阶共振标量为零时的完整正则帽与真实柱边三阶匹配

**状态：完整作者条件性证明，待未参与者全文独立审查。**  
2026-11-10；Astra-visible-flex-78718bd0 / geometric_closure。

本稿把 [三阶兼容稿](2026-11-10-78718-geometry-cubic-cap-v1.md) 的
标量必要条件提升为准确范围内的三阶可解充分条件。严格假设
$\mathfrak C_n=0$ 不由近似浮点零支付；本稿不声称已经构造精确非线性
等距帽、闭面或固定开 $H$。

## 1. 定理与完整输入

沿用 [二阶帽 v2](2026-11-10-78718-geometry-second-order-cap-v2.md)
的共同径向度量

$$
g=dr^2+a(r)^2du^2,\quad
F_0=(a\cos u,a\sin u,Z(r)),\quad
b=Z_r=\sqrt{1-a_r^2}>0,
\tag{1}
$$

其中入口是开单位圆柱，中心是半径 $\sigma$ 的开球核心。令
$P=aa_{rr}/b^3$、$R=b/a^2$、
$\mathcal L_Nz=(z_r/R)_r+N^2Pz$，共振门 $D_N$ 按二阶稿定义。
给定一个整数 $n\ge2$，要求

$$
D_n=0,\qquad D_{2n}\ne0,\qquad D_{3n}\ne0,
\qquad \mathfrak C_n=0.
\tag{2}
$$

这里 $\mathfrak C_n$ 由唯一规范二阶解及三阶稿公式 (4)、(7) 精确定义。

**定理。** 在 (1)–(2) 下，存在全盘光滑向量场 $V_1,V_2,V_3$，使

$$
F^{[3]}_\tau=F_0+\tau V_1+\tau^2V_2+\tau^3V_3,
\qquad (F^{[3]}_\tau)^*g_{\mathbb R^3}=g+O(\tau^4)
\tag{3}
$$

于每个固定 $C^k$ 范数。$V_1$ 非刚体。
入口开柱的全部零至三阶位置系数，等于一个真正同周长、严格凸、
$n$ 折对称的平面曲线族 $\Gamma_\tau$ 的圆柱图
$\Gamma_\tau(u)+r e_z$ 的对应系数。全部场在真实 Cartesian 中心光滑。

本定理只给有限阶等距。固定非零 $\tau$ 后，(3) 的第四阶度量缺陷不会
因为网格加密而自动消失。

## 2. 前两阶及三阶源

二阶稿已构造全盘光滑 $II_1,II_2$，记其模态为

$$
x_1=p\sin(nu),\quad \zeta_1=v\cos(nu),\qquad
x_2=y\sin(2nu),\quad\zeta_2=z_0+z\cos(2nu),
\tag{4}
$$

并取 $v(0)=1,p(0)=0$。对无阶乘展开，三阶 Gauss 源为

$$
S^{(3)}=T_n(r)\cos(nu)+T_{3n}(r)\cos(3nu),
\tag{5}
$$

其中

$$
T_n=\frac{py}{a^3b}-\frac{a_{rr}v}{b^5}(2z_0+z)
-\frac v{b^2}(S_0+S_2/2),
$$

$$
T_{3n}=-\frac{py}{a^3b}-\frac{a_{rr}v}{b^5}z-\frac{vS_2}{2b^2}.
\tag{6}
$$

开柱上两项源恒零。三阶 Codazzi 对每个频率 $N$ 是

$$
q_r=-N(P\xi+aT_N),\qquad
\xi_r=NRq+ba_rT_N,
\tag{7}
$$

这里 $x_3=q\sin(Nu),\zeta_3=\xi\cos(Nu)$。
消元给

$$
\mathcal L_N\xi=(a^2a_rT_N)_r-N^2aT_N.
\tag{8}
$$

一旦解出 (7)，三阶第二形式由

$$
c_3=(a/b)\zeta_3,\quad m_3=x_3/a,
\quad\ell_3=(a_{rr}/(ab^2))c_3+S^{(3)}
\tag{9}
$$

定义，因而满足完整三阶 Gauss–Codazzi。

## 3. 球核心源具有真实解析阶数

在球核心记 $t=\tan(\rho/(2\sigma))$，$\rho=T-r$，则

$$
a=\frac{2\sigma t}{1+t^2},\qquad b=a/\sigma,
\quad v=d t^n,\quad p=-\sigma d t^n,
\quad z=d_2t^{2n},\quad y=-\sigma d_2t^{2n}.
\tag{10}
$$

二阶零模为

$$
z_0=\frac{d^2}{4}
\left(\frac{t^{2n-2}}{2n-2}-\frac{t^{2n+2}}{2n+2}\right).
\tag{11}
$$

代入 (6) 精确给 $T_{3n}=0$。设 $H_3=bT_n$，则

$$
H_3=\frac{d^3}{32\sigma}t^{3n-5}(1+t^2)^3
\left(\frac{2-n}{n-1}-2t^2-\frac{n+2}{n+1}t^4\right)
+\frac{dd_2}{4\sigma}t^{3n-3}(1+t^2)^3.
\tag{12}
$$

所以

$$
\boxed{\quad T_n(t)=t^n f(t^2),\quad f\text{ 在 }0\text{ 附近解析}.\quad}
\tag{13}
$$

核查最低阶不能跳过：除以 $b=2t/(1+t^2)$ 后，第一项通常从
$t^{3n-6}$ 开始。$n\ge3$ 时 $3n-6-n=2n-6$ 为非负偶数；
$n=2$ 时 (12) 括号的常数项准确为零，使最低幂升到 $t^2$，仍等于
$t^n$ 乘 $t^2$ 的解析函数。第二项从 $t^{3n-4}$ 开始，同样满足 (13)。

## 4. 共振 $n$ 模在中心的显式正则 particular

本节只讨论球核心，写 $T=T_n$、$N=n$。从 (7) 与
$dr/dt=-2\sigma/(1+t^2)$ 得

$$
q_t=-\frac{n\sigma}{t}\xi
+\frac{4n\sigma^2t}{(1+t^2)^2}T,
$$

$$
\xi_t=-\frac n{\sigma t}q
+\frac{4\sigma t(1-t^2)}{(1+t^2)^3}T.
\tag{14}
$$

置 $U=\xi+q/\sigma$、$V=\xi-q/\sigma$，系统解耦为

$$
U_t+\frac ntU
=\frac{4\sigma t((n+1)+(n-1)t^2)}{(1+t^2)^3}T,
$$

$$
V_t-\frac ntV
=-\frac{4\sigma t((n-1)+(n+1)t^2)}{(1+t^2)^3}T.
\tag{15}
$$

因此取

$$
U(t)=t^{-n}\int_0^t
\frac{4\sigma s^{n+1}((n+1)+(n-1)s^2)}{(1+s^2)^3}T(s)\,ds,
$$

$$
V(t)=t^n\left[c-\int_0^t
\frac{4\sigma s^{1-n}((n-1)+(n+1)s^2)}{(1+s^2)^3}T(s)\,ds\right]
\tag{16}
$$

便给实际解，再令 $\xi=(U+V)/2,q=\sigma(U-V)/2$。
由 (13)，两个积分的被积函数分别为 $s^{2n+1}$ 和 $s$ 乘 $s^2$ 的
解析函数。因此没有对数项，且

$$
U=t^{n+2}u(t^2),\qquad V=t^n(c+t^2v_*(t^2)),
\quad u(0)=2\sigma f(0).
\tag{17}
$$

$c$ 正是可加中心正则齐次 $n$ 模的一维自由度；增长支 $t^{-n}$ 已被排除。

## 5. 不是只核极坐标有界：三阶张量在中心解析

以 $w=x+iy=t e^{iu}$ 为中心材料坐标，并记
$\lambda=2\sigma/(1+t^2)$，则 $g=\lambda^2|dw|^2$。
三阶张量的迹为 $T(t)\cos(nu)$，按 (13) 是真正解析函数
$\operatorname{Re}(w^n)f(|w|^2)$。

扣去迹部分 $\tfrac12T\cos(nu)g$ 后，把无迹部分写为
$\operatorname{Re}(Q(w,\bar w)dw^2)$。从 (9)、(14) 的实际分量逐项换算得

$$
Q=\lambda^2\left(\frac T4-\frac{\sigma V}{2a^2}\right)e^{i(n-2)u}
+\lambda^2\left(\frac T4-\frac{\sigma U}{2a^2}\right)e^{-i(n+2)u}.
\tag{18}
$$

注意从 $r$ 变到 $\rho$ 时，混合分量变号；这个符号已经包含于 (18)。
第一项的径向系数是 $t^{n-2}$ 乘 $t^2$ 的解析函数，故对应
$w^{n-2}$ 乘 $|w|^2$ 的解析函数。

第二项必须多核一个抵消。由 (17) 与
$a^2=4\sigma^2t^2/(1+t^2)^2$，有

$$
\frac{\sigma U}{2a^2}
=\frac{f(0)}4t^n+O(t^{n+2}),\qquad
\frac T4=\frac{f(0)}4t^n+O(t^{n+2}).
$$

所以括号是 $t^{n+2}$ 乘 $t^2$ 的解析函数，对应
$\bar w^{n+2}$ 乘 $|w|^2$ 的解析函数。于是 (18) 在中心解析。
这证明由 (16) 构造的是一个真正光滑二次型，不只是极坐标解的增长阶数。

## 6. 把中心 particular 延到整个帽，并使用唯一缺失的标量条件

从第 4 节任取 $c$（例如 $c=0$），将实际解通过去中心光滑区唯一延到
入口，记为 $\xi^p$。它在中心正则，入口开柱上的源为零。

用第一阶正则解 $v$，归一为 $v(0)=1,v_r(0)=0$。对 (8) 积分并作
两次端项核对，恰得

$$
\left[\frac{v(\xi^p)_r-\xi^pv_r}{R}\right]_0^T
=-\mathfrak C_n.
$$

中心端项由第 5 节为零；入口 $R(0)=1$。因此

$$
(\xi^p)_r(0)=\mathfrak C_n.
\tag{19}
$$

假设 (2) 给柱端所需的零导数。再减去 $\xi^p(0)v$，可选择唯一规范解

$$
\xi_n(0)=(\xi_n)_r(0)=0.
\tag{20}
$$

这只是去掉一个可用三阶振幅重标消除的同频齐次项，不改变源或共同度量。
用 (7) 还原 $q$ 后，入口整个开柱上 $\xi_n=q_n=0$。

这个论证说明 $\mathfrak C_n=0$ 对该共振模不仅必要，也确实充分，
并没有另藏一个中心或柱端条件。

## 7. 非共振 $3n$ 模

$T_{3n}$ 在球核心恒零。先在该核心选零解，再将其按 (7) 向入口延伸，
得一个中心正则 particular $\xi^p_{3n}$。令 $v_{3n}$ 是核心
$t^{3n}$ 向外延伸的齐次解。因 $D_{3n}\ne0$，唯一取

$$
\xi_{3n}=
\xi^p_{3n}-\frac{(\xi^p_{3n})_r(0)}{D_{3n}}v_{3n}
\tag{21}
$$

便令柱端导数为零。其球核心为某个常数乘 $t^{3n}$，所以三阶张量
在那里恰为 $\operatorname{Re}(-\sigma c_*w^{3n-2}dw^2)$，真正光滑。
记 $\gamma=\xi_{3n}(0)$，则入口开柱有

$$
\ell_3=m_3=0,\qquad c_3=\gamma\cos(3nu).
\tag{22}
$$

三阶没有其他强迫模态；其余全部取零。第 6 节与本节合成完整光滑 $II_3$。

## 8. 真正闭柱边族到三阶

记二阶柱边系数为 $\alpha$。在平面复坐标定义

$$
\phi_\tau(u)=u+\frac\tau n\sin(nu)
+\frac{\alpha\tau^2}{2n}\sin(2nu)
+\frac{\gamma\tau^3}{3n}\sin(3nu),
$$

$$
T_\tau(u)=i e^{i\phi_\tau(u)},\qquad
\Gamma_\tau(u)=1+\int_0^uT_\tau(s)ds.
\tag{23}
$$

严格有 $|T_\tau|=1$、
$T_\tau(u+2\pi/n)=e^{2\pi i/n}T_\tau(u)$，故整圈积分为零。
因此 (23) 是真正同材料周长的闭曲线族，不是只到三阶闭合。
其准确曲率为

$$
\kappa_\tau=1+\tau\cos(nu)+\alpha\tau^2\cos(2nu)
+\gamma\tau^3\cos(3nu).
\tag{24}
$$

小参数时它是严格凸嵌入。柱图 $\Gamma_\tau+r e_z$ 的第二形式零至
三阶与已构造 $II_j$ 完全一致，并可在一个锚点配准位置、切向与 $e_z$。

## 9. 三阶位置积分

选圆盘上的全局光滑正交标架 $E_0$ 及固定余标架 $\theta$。由
$II_0+\tau II_1+\tau^2II_2+\tau^3II_3$ 构造连接
$\Omega_\tau=\sum_{j=0}^3\tau^j\Omega_j$。
刚证明的完整 Gauss–Codazzi 给

$$
d\Omega_\tau+\Omega_\tau\wedge\Omega_\tau=O(\tau^4),
\qquad d\theta+\Omega_\tau\wedge\theta=0.
\tag{25}
$$

置 $\Psi_j=E_0\Omega_jE_0^{-1}$，令 $U_0=I$，递归积分

$$
dU_j=\sum_{k=1}^jU_{j-k}\Psi_k,
\qquad j=1,2,3.
\tag{26}
$$

每一步右端为闭形式，因为 (25) 的相应阶曲率为零，低阶式 (26) 已成立。
圆盘单连通，故全局光滑积分存在。锚点常数取 (23) 的真实柱标架
的相应 Taylor 系数。反对称连接从锚点保持形式正交性，
$(\sum_{j=0}^3\tau^jU_j)E_0$ 到三阶正交。

无挠式使每个 $U_jdF_0$ 闭，故可积分

$$
dV_j=U_jdF_0\quad(j=1,2,3),
\tag{27}
$$

位置锚点常数取真实柱边 (23) 的系数。所得 (3) 的诱导度量精确消掉
一、二、三阶项。在入口开柱，全部位置与标架系数满足与真实柱族相同的
ODE 和同一锚点值，故逐阶全圈、整个开柱一致。
这证明定理。

## 10. 证明与数值的界线

本文是条件性正向结论：它完整支付由 (2) 到 (3) 的逻辑，包含真正中心、
全盘位置积分和真实闭柱边。它没有严格证明某个具体剖面的
$\mathfrak C_n=0$。

同日两参数浮点搜索找到 $n=4$ 的一阶共振/三阶量联合近似零；这只可作为
后续精确参数存在或更高阶研究的种子。该搜索不建立非线性帽族，不建立
固定开 $H$，也不把有限阶度量缺陷称为可用网格加密消去的误差。

即使严格支付了 (2)，四阶及更高阶仍须处理。下一项最有意义的问题是
找到能够一次控制完整非线性函数方程的结构，或证明一个适用于这些
参数的真正收敛机制，而非不断累加未经收敛控制的形式阶数。
