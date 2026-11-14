# R44：外头的兼容保持高度、完整 mean 根与真实连续 Darboux 残差

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明（构造、误差公式及条件性核公式）。** 本文把外侧 $0,\ldots,11$ 胞元的一个明确连续高度候选，转成保留完整角平均的连续残差对象。其非均值高度导数是真实插值导数，不用 ODE 右端替换。所需输入是同一个 R26 实背景上的连续包络；已保存的 13port 或待运行的 109 点结果不自动支付这些输入。

本文没有声称实际外头的径向残差、Green 范数或非线性收缩已通过；也没有把深头 R43 的条件性结论外推到这里。

## 1. 固定对象与兼容保持的候选

固定一个有限实径向区间 $I=[r_a,r_b]\subset(0,\infty)$，其背景为

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad
w(r)>0,\qquad E=1+w^2.
\tag{44.1}
$$

这里 $r,w$ 是 R26 定义的实函数。为统一使用下文的经典曲率公式，取 $w\in C^2(I)$；仅构造 mean 根和 $C^2$ 高度时，$C^1$ 已够。逐原 source 段使用参数 $x$ 时，假设 $r_x>0$ 并记

$$
s=r_x/r,\qquad \ell=w_x/w,\qquad z=w^2,\qquad z_x=2z\ell.
\tag{44.2}
$$

给定一个明确的非均值高度

$$
\widehat h_\perp(r,\theta)
=\sum_{0<|m|\le m_*}H_m(r)e^{im\theta},
\quad H_{-m}=\overline{H_m},\quad H_m\in C^2(I),
\tag{44.3}
$$

所有频率可以限制为偶数。定义

$$
P=\frac{\widehat h_{\perp,\theta}}{rw},
\qquad
\overline K=\frac{\widehat h_{\perp,r}}w,
\qquad
K=c(r)+\overline K,
\qquad y=1+K,\quad T=P_\theta,\quad U=K_\theta-P.
\tag{44.4}
$$

此处 $\overline K$ 表示去均值部分，不是复共轭。未知标量 $c$ 将由完整连接平均唯一确定。无论怎样选择 $c$，都有精确恒等式

$$
P_x=sK_\theta-(s+\ell)P.
\tag{44.5}
$$

**证明。** 对 $rwP=\widehat h_{\perp,\theta}$ 求 $x$ 导数，再用
$\widehat h_{\perp,x}=r_xw\overline K$；$c$ 没有角导数。证毕。

因此此候选的第一行兼容残差恒为零。给定节点的 $H_m$、$\partial_rH_m$、$\partial_r^2H_m$ 后，可以在相邻真实半径间使用五次 Hermite 插值，得到 (44.3)。例如 $t=(r-a)/(b-a)$、$d=b-a$ 时，令

$$
\begin{aligned}
H_0(t)&=1-10t^3+15t^4-6t^5,\\
H_1(t)&=t-6t^3+8t^4-3t^5,\\
H_2(t)&=(t^2-3t^3+3t^4-t^5)/2 .
\end{aligned}
\tag{44.6}
$$

对任一非零模，取

$$
\begin{aligned}
H_m(r)={}&a_mH_0(t)+d\,b_mH_1(t)+d^2c_mH_2(t)\\
&+A_mH_0(1-t)-d\,B_mH_1(1-t)+d^2C_mH_2(1-t).
\end{aligned}
\tag{44.7}
$$

两端分别具有指定的三个真实径向 jet。公共节点使用相同 jet，便得到整体 $C^2$ 候选。端点 jet 可以来自保存场，但必须明确它们定义的是哪个实候选；不能把一个有限 root 的候选 slope 同时称作已认证的精确 trace。

## 2. 无小 $w$ 相减的完整 mean 方程

使用 R41 的连接式

$$
S=1-zP^2,\qquad
D=ES-zy^2,\qquad
L=y+ET,\qquad
N=1+\frac{zyT}{S},\qquad
\Omega=\frac{N}{\sqrt D}.
\tag{44.8}
$$

需要的真实分支为 $S,D,y,N,L>0$。引入

$$
\mathfrak a=2K+K^2+EP^2,\qquad
\mathfrak b=\frac{yT}{S},\qquad
u=z\mathfrak a,\qquad v=zP^2.
\tag{44.9}
$$

于是 $D=1-u$、$N=1+z\mathfrak b$。令

$$
C(u)=(1-u)^{-1/2}
=\sum_{n\ge0}a_nu^n,\quad
a_n=\frac{\binom{2n}{n}}{4^n},
\qquad
C_1(u)=\sum_{n\ge0}a_{n+1}u^n .
\tag{44.10}
$$

在同一 Wiener 代数

$$
\mathcal A_\tau=W_{\tau,1},\qquad
\|f\|_{\tau,1}=\sum_m(1+|m|)e^{\tau|m|}|f_m|
\tag{44.11}
$$

中，若 $\|u\|_{\tau,1}<1$、$\|v\|_{\tau,1}<1$，上述级数及 $S^{-1}$ 收敛。恒等式

$$
\boxed{\quad
\frac{\Omega-1}{z}
=\mathfrak a C_1(u)+\mathfrak b C(u)
 =:\mathcal F(P,\overline K,c,z)
\quad}
\tag{44.12}
$$

没有除以很小的 $w^2$ 的数值相减。它由
$C(u)-1=uC_1(u)$ 直接得到。$z=0$ 时右端仍有明确的连续代数极限；本外头的等价论证只使用 $z>0$。

记角平均为 $\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f\,d\theta$。完整 mean 方程是

$$
\mathcal M(r,c):=\langle\mathcal F(P,\overline K,c,z)\rangle=0.
\tag{44.13}
$$

它等价于 $\langle\Omega\rangle=1$，保留全部非线性产生的频率，未把平均换成有限角采样。

### 2.1 精确的 mean 导数

保持 $P,T,z$ 不变，对 $c$ 求导，有

$$
\partial_c\Omega=\frac{zL}{D^{3/2}},
\qquad
\boxed{\quad
\partial_c\mathcal M=\left\langle\frac{L}{D^{3/2}}\right\rangle .
\quad}
\tag{44.14}
$$

**证明。** $y_c=1$、$D_c=-2zy$，故

$$
\partial_c\Omega
=\frac{zT}{S\sqrt D}
+\frac{z y(1+zyT/S)}{D^{3/2}}
=z\frac{TD+yS+zy^2T}{SD^{3/2}}
=\frac{z(y+ET)}{D^{3/2}}.
$$

再用 $z$ 与角度、$c$ 无关，得到 (44.14)。证毕。

该归一导数在小 $w$ 时仍是 $O(1)$ 的量；不能用未归一平均方程的 $O(w^2)$ 导数造成的数值病态替代真实数学条件。

## 3. 完整连续 mean 根及有限卷积证书

**定理 44.1。** 给定 $C^1$ 的标量候选 $\widehat c(r)$、连续正半径 $d(r)$。假设在每个 $r\in I$ 及整个实区间
$|c-\widehat c(r)|\le d(r)$ 上，有同函数包络

$$
\|u\|_{\tau,1}\le\bar u<1,\qquad
\|v\|_{\tau,1}\le\bar v<1,\qquad
y\ge y_{\min}>0,\quad N\ge N_{\min}>0,\quad L\ge L_{\min}>0.
\tag{44.15}
$$

可以逐面板使用不同但严格正的常数。令

$$
\mu=\frac{L_{\min}}{(1+\bar u)^{3/2}},
\qquad
|\mathcal M(r,\widehat c(r))|\le\epsilon(r)<\mu d(r).
\tag{44.16}
$$

则 (44.13) 在该区间内有唯一实根 $c(r)$，

$$
|c(r)-\widehat c(r)|\le\epsilon(r)/\mu.
\tag{44.17}
$$

这个根是 $C^1$ 的；在分段表示中，只要实数据及公共 jet 一致，就给同一个 $C^1$ 根。

**证明。** $\|u\|<1$、$\|v\|<1$ 使 $D,S>0$，且 $D\le1+\bar u$。由 (44.14) 有 $\partial_c\mathcal M\ge\mu$。因此在左右端点，$\mathcal M$ 分别严格负、严格正；连续性与严格单调性给存在及唯一性。对根与 $\widehat c$ 积分此导数下界，得到 (44.17)。所有输入关于 $r$ 为 $C^1$，分母严格正；普通隐函数定理给局部 $C^1$ 根。唯一性将局部根拼为同一个根。公共节点的输入及其物理径向导数一致时，隐函数公式亦一致。证毕。

### 3.1 不用角采样的残差包络

对有限候选 $c=\widehat c$，$\mathfrak a,u,v,yT$ 都是有限 Laurent 多项式。取

$$
C_J^{\rm geom}(v)=\sum_{j=0}^Jv^j,\qquad
\mathfrak b_J=yT\,C_J^{\rm geom}(v),
$$

$$
C_N(u)=\sum_{n=0}^Na_nu^n,\qquad
C_{1,N}(u)=\sum_{n=0}^Na_{n+1}u^n.
\tag{44.18}
$$

则有限卷积多项式

$$
\mathcal F_{N,J}
=\mathfrak a C_{1,N}(u)+\mathfrak b_J C_N(u)
\tag{44.19}
$$

满足

$$
\begin{aligned}
\|\mathcal F-\mathcal F_{N,J}\|_{\tau,1}
\le{}&
\left(\|\mathfrak a\|_{\tau,1}
+\frac{\|yT\|_{\tau,1}}{1-\bar v}\right)
\frac{\bar u^{N+1}}{1-\bar u}\\
&+\frac{\|yT\|_{\tau,1}\bar v^{J+1}}
{(1-\bar v)\sqrt{1-\bar u}}
 =:\mathcal E_{N,J}.
\end{aligned}
\tag{44.20}
$$

**证明。** $0<a_n\le1$，所以两个二项级数的尾范数均至多
$\bar u^{N+1}/(1-\bar u)$。几何尾给
$\|\mathfrak b-\mathfrak b_J\|\le\|yT\|\bar v^{J+1}/(1-\bar v)$，
而 $\|C_N(u)\|\le(1-\bar u)^{-1/2}$。分解
$\mathfrak b C-\mathfrak b_JC_N
=\mathfrak b(C-C_N)+(\mathfrak b-\mathfrak b_J)C_N$，
用 Banach 代数乘法界即可。证毕。

因此可取

$$
\epsilon
=|(\mathcal F_{N,J})_0|+\mathcal E_{N,J}.
\tag{44.21}
$$

所有频率都由完整有限卷积和明确的无限尾界覆盖。系数含区间实数时，相同公式给整个径向面板的界，但前提是这些系数盒确实包围该面板上的同一个函数；不能把端点盒当成面板盒。

### 3.2 根的真实径向导数

以下下标 $x$ 为 source 导数，上标 $*$ 表示保持 $c$ 不变。令

$$
\begin{aligned}
\mathfrak a_x^*
 &=2y\,\overline K_x+z_xP^2+2EPP_x,\\
\mathfrak b_x^*
 &=\frac{\overline K_xT+yT_x}{S}
 +\frac{yT(z_xP^2+2zPP_x)}{S^2},\\
u_x^*&=z_x\mathfrak a+z\mathfrak a_x^* .
\end{aligned}
\tag{44.22}
$$

由 (44.12) 对同一完整级数求导，

$$
\partial_x^*\mathcal M
=\left\langle
\mathfrak a_x^*C_1(u)+\mathfrak b_x^*C(u)
+[\mathfrak a C_1'(u)+\mathfrak b C'(u)]u_x^*
\right\rangle,
$$

$$
\boxed{\quad
c_x=-\frac{\partial_x^*\mathcal M}
{\langle L/D^{3/2}\rangle}.
\quad}
\tag{44.23}
$$

这是实际根的导数，不是对若干保存的 root 数值作差分。对导数级数也有明确尾界，例如

$$
\sum_{n>N}n\bar u^{n-1}
=\frac{\bar u^N[(N+1)-N\bar u]}{(1-\bar u)^2}.
\tag{44.24}
$$

因二项系数不超过 $1$，(44.24) 同时控制 $C'$ 与 $C_1'$ 的相应截断尾；$S^{-2}$ 的几何导数尾同理。结合 $\mu>0$，(44.22)–(44.24) 是连续 $c_x$ 的可核销接口，没有以很小的 $w^2$ 为额外分母。

## 4. 实际 $C^2$ 高度及其有限全角残差

固定一个 mean 高度常数，定义

$$
\widehat h_0(r)
=\widehat h_0(r_a)+\int_{r_a}^{r}w(\rho)(1+c(\rho))\,d\rho,
\qquad
\widehat h=\widehat h_0+\widehat h_\perp.
\tag{44.25}
$$

由定理 44.1，$\widehat h\in C^2$，且其真实两分量为

$$
p=\widehat h_\theta/r=wP,\qquad
k=\widehat h_r=w(1+K).
\tag{44.26}
$$

尤其 $k_r$ 必须由 (44.25) 的实际导数和 (44.23) 计算。

定义完整源坐标残差多项式

$$
\boxed{\quad
\mathcal J
=L K_x-E s U^2
+\ell[2K+K^2+zP^2+(1+K)T].
\quad}
\tag{44.27}
$$

因为 $c,c_x$ 仅为 mean，而 (44.3) 为有限 Fourier 场，$\mathcal J$ 的最大角频率至多 $2m_*$。它不是角采样投影，也没有忽略新生成的高频。

记真实内蕴 Darboux 缺陷

$$
\mathscr D(\widehat h)
=\det(\operatorname{Hess}_g\widehat h)
-K_g\bigl(1-|\nabla_g\widehat h|^2\bigr).
\tag{44.28}
$$

**定理 44.2。** 在上述候选上，

$$
\boxed{\quad
\mathscr D(\widehat h)
=\frac{w^2}{r r_x E^2}\,\mathcal J .
\quad}
\tag{44.29}
$$

因此全角连续缺陷可以直接由有限多项式系数与同函数的实径向包络控制。

**证明。** 正交极坐标下

$$
\operatorname{Hess}_g\widehat h=
\begin{pmatrix}
(k_r-ww_rk/E)/E &(k_\theta-p)/(r\sqrt E)\\
(k_\theta-p)/(r\sqrt E)&(p_\theta+k/E)/r
\end{pmatrix},
$$

$$
K_g=\frac{ww_r}{rE^2},
\qquad
1-|\nabla_g\widehat h|^2=\frac{D}{E}.
\tag{44.30}
$$

将行列式减去 $K_gD/E$，用
$k(k+Ep_\theta)+D=E(1-p^2+kp_\theta)$，得到

$$
rE^2\mathscr D
=(k+Ep_\theta)k_r
-\frac{E(k_\theta-p)^2}{r}
-ww_r(1-p^2+kp_\theta).
\tag{44.31}
$$

代入
$k=w(1+K)$、$p=wP$、$w_r=w\ell/r_x$、$k_r=w[\ell(1+K)+K_x]/r_x$，
右端等于 $w^2\mathcal J/r_x$，即 (44.29)。证毕。

对任一真实面板 $I_j$，例如有可计算界

$$
\sup_{I_j,\theta}|\mathscr D|
\le
\sup_{I_j}\frac{w^2}{r r_x E^2}
\sum_{|m|\le2m_*}\sup_{I_j}|\mathcal J_m|.
\tag{44.32}
$$

也可按逐模、逐位置保留乘积以避免整面板极值错配。无论采用哪种界，都必须使用 (44.27) 的实际 $K_x$；将其替换为 Darboux 右端会把待认证残差人为置零。

## 5. 连接 curl、mean 方程与两行残差的准确关系

先允许 $P,K$ 是两个独立的足够光滑候选，不假定它们来自同一个高度。令

$$
\begin{aligned}
\mathcal R_P&=P_x-sK_\theta+(s+\ell)P,\\
\mathcal R_K&=\mathcal J/L,\\
\mathcal A_x&=\frac{szy(K_\theta-P)}{S\sqrt D}.
\end{aligned}
\tag{44.33}
$$

其中 $\mathcal A_x$ 是 source 坐标下的水平切向角径向连接；下标 $x$ 是名称中的坐标标识，右端本身不是对一个已定义的 $\mathcal A$ 再求导。则有完整恒等式

$$
\begin{aligned}
\Omega_x-\partial_\theta\mathcal A_x
={}&\frac{zL}{D^{3/2}}\mathcal R_K
+\frac{zy}{S\sqrt D}\,\partial_\theta\mathcal R_P\\
&+\left[
\frac{zEP N}{D^{3/2}}
+\frac{2z^2yTP}{S^2\sqrt D}
\right]\mathcal R_P .
\end{aligned}
\tag{44.34}
$$

**证明。** 把 $\Omega$ 看成 $P,T,K,z$ 的函数。除了 (44.14) 已算的 $\Omega_K$，直接求导得

$$
\Omega_T=\frac{zy}{S\sqrt D},
\qquad
\Omega_P=\frac{zEP N}{D^{3/2}}
+\frac{2z^2yTP}{S^2\sqrt D}.
\tag{44.35}
$$

当 $\mathcal R_P=\mathcal R_K=0$ 时，把 (44.33) 解出的 $P_x,K_x$ 与 $z_x=2z\ell$ 代入链式法则，恰得到
$\Omega_x=\partial_\theta[szy(K_\theta-P)/(S\sqrt D)]$；这也是 R41 的完整 source 流连接恒等式。一般情形仅使 $P_x$ 增加 $\mathcal R_P$、$T_x$ 增加 $\partial_\theta\mathcal R_P$、$K_x$ 增加 $\mathcal R_K$。连接右端只含当点场及角导数，不含这三个径向导数，因此其差恰为 (44.34)。证毕。

对第 1–4 节的兼容候选，$\mathcal R_P=0$ 且 $\langle\Omega\rangle=1$。对 (44.34) 取平均即得

$$
\boxed{\quad
\left\langle\frac{\mathcal J}{D^{3/2}}\right\rangle=0.
\quad}
\tag{44.36}
$$

这不是 $\mathcal J_0=0$。完整 mean 必须按真实正权保留。

**推论 44.3。** 在上述正分支上，如果 $\mathcal J/L$ 的**全部**非零 Fourier 系数为零，则 $\mathcal J=0$；如果 $\mathcal J$ 的全部非零 Fourier 系数为零，同样有 $\mathcal J=0$。

**证明。** 第一种情形为 $\mathcal J=L a(r)$。代入 (44.36)，由于
$\langle L/D^{3/2}\rangle>0$，得到 $a=0$。第二种情形为 $\mathcal J=a(r)$，而
$\langle D^{-3/2}\rangle>0$，结论相同。证毕。

只把某个有限 Galerkin 窗内的非零系数置零不满足这里的量词，除非该窗已经覆盖真实残差的全部频率，或其余频率另有严格控制。

### 5.1 一个量化 mean 缺陷界

记 $\mathcal J=\mathcal J_0+\mathcal J_\perp$。由 (44.36) 有

$$
\mathcal J_0
=-\frac{\langle(D^{-3/2}-1)\mathcal J_\perp\rangle}
{\langle D^{-3/2}\rangle}.
\tag{44.37}
$$

若 $D\le D_{\max}$、$\|u\|_{\tau,1}\le\bar u<1$，则

$$
|\mathcal J_0|
\le D_{\max}^{3/2}
\bigl[(1-\bar u)^{-3/2}-1\bigr]\,
\|\mathcal J_\perp\|_{\tau,1}.
\tag{44.38}
$$

这是因为 $(1-u)^{-3/2}$ 的二项系数非负，且
$\langle D^{-3/2}\rangle\ge D_{\max}^{-3/2}$。因此完整 mean 可以由非均值缺陷严格控制，没有独立设置 mean Dirichlet 零条件。

### 5.2 真实 Darboux 缺陷与解析源范数不同

(44.29) 不需要在 Wiener 代数中求 $L^{-1}$；有限多项式 $\mathcal J$ 已足以计算实际 Darboux 缺陷。若要把残差作为解析 Green 方程的源，则需要

$$
\mathcal R_K=\mathcal J/L
\tag{44.39}
$$

属于相应解析空间。实角上 $L>0$ 本身不能排除复条带内的零点。一个明确的充分门是

$$
a_L:=1+c-\|\overline K+ET\|_{\tau,1}>0,
\qquad
\|\mathcal R_K\|_{\tau,1}
\le\|\mathcal J\|_{\tau,1}/a_L .
\tag{44.40}
$$

若改用更紧的复域无零证书，也必须明示该证书。这里没有从实角正性免费得到解析逆。

## 6. 均值消元后的准确全频外头方程

令 $\mathscr P_\perp$ 去掉 mean，$c=c(P,\overline K)$ 为上述完整根。定义

$$
\mathcal N(P,K)=
\frac{
E s(K_\theta-P)^2+
\ell[(K+P_\theta)^2+
z(2KP_\theta+P_\theta^2-P^2)]
}{1+K+EP_\theta}.
\tag{44.41}
$$

于是准确的非均值系统可写为

$$
\begin{aligned}
P_x&=s\overline K_\theta-(s+\ell)P,\\
\overline K_x
&=-\ell(2\overline K+P_\theta)
+\mathscr P_\perp\mathcal N(P,c+\overline K).
\end{aligned}
\tag{44.42}
$$

**定理 44.4。** 假设所有频率保留，场满足前述正则性、mean 分支及正分母条件。则 (44.42) 连同定义 (44.25) 给完整 Darboux 高度；反过来，同一分支上的 Darboux 高度满足 (44.42)。

**证明。** 第一行给精确高度兼容。第二行等价于
$\mathscr P_\perp(\mathcal J/L)=0$，因为展开 (44.41) 得

$$
\mathcal J/L
=K_x+\ell(2K+P_\theta)-\mathcal N(P,K).
\tag{44.43}
$$

完整 mean 根使 (44.36) 成立。推论 44.3 给 $\mathcal J=0$，进而由 (44.29) 得完整 Darboux 方程。反向对完整方程去均值即得第二行，兼容性给第一行。证毕。

对兼容候选，(44.42) 的连续残差恰为

$$
\left(0,\ \mathscr P_\perp(\mathcal J/L)\right).
\tag{44.44}
$$

这在实际外头验证中消除了一个原本必须单独付界的源列：未知非线性和候选残差都只进入第二行。它没有消除新的外头传播、深头参数化及边界分母预算。

## 7. 外头两点核的准确形式

以下公式说明实际必须计算的对象，特别是怎样避免把极小的 node12 trace 当成外头误差界。

在真实 parity 约定 $P=P_m\sin(m\theta)$、$\overline K=K_m\cos(m\theta)$ 下，(44.42) 的背景线性矩阵为

$$
A_m(x)=
\begin{pmatrix}
-s-\ell&-ms\\
-m\ell&-2\ell
\end{pmatrix}.
\tag{44.45}
$$

从 node12 向外 cut 逐实段连接，记其基本矩阵为 $\Phi_m(x,t)$。每个有限模上，

$$
\det\Phi_m(x,a)
=\exp\!\int_a^x(-s-3\ell)\,dt
=\frac{r(a)w(a)^3}{r(x)w(x)^3}>0.
\tag{44.46}
$$

该行列式恒等式是两列一致性的校验；它不保证下述两点边界分母非零。

### 7.1 单模两源列

设内端线性 trace 由一个非零向量 $v_m$ 张成，选定补向量 $b_m$。考虑

$$
y_m'=A_my_m+f_m,\qquad
y_m(a)=v_m q_m+b_m\beta_m,\qquad
e_1^Ty_m(b)=\alpha_m.
\tag{44.47}
$$

这里 $a$ 是 node12、$b$ 是外 cut；没有假设 $v_m$ 可写成一个良态的高度斜率图。令

$$
d_m=e_1^T\Phi_m(b,a)v_m.
\tag{44.48}
$$

若 $d_m\ne0$，解的源核为

$$
G_m(x,t)
=\mathbf1_{t\le x}\Phi_m(x,t)
-\frac{\Phi_m(x,a)v_m}{d_m}\,e_1^T\Phi_m(b,t).
\tag{44.49}
$$

外、内边界提升分别为

$$
B^{\rm cut}_m(x)=\frac{\Phi_m(x,a)v_m}{d_m},
$$

$$
B^{\rm in}_m(x)
=\Phi_m(x,a)\left[
b_m-v_m\frac{e_1^T\Phi_m(b,a)b_m}{d_m}
\right].
\tag{44.50}
$$

**证明。** 变常数公式给
$y(x)=\Phi(x,a)(vq+b\beta)+\int_a^x\Phi(x,t)f(t)\,dt$。
代入外端约束，解出
$q=[\alpha-e_1^T\Phi(b,a)b\beta-\int_a^be_1^T\Phi(b,t)f(t)\,dt]/d$。
代回即得 (44.49)–(44.50)。证毕。

(44.49) 的两列分别控制独立的两个源分量。采用本文兼容候选时，(44.44) 只使用第二列；采用任意保存的 $P/K$ 插值时，不能省去第一列及其角导数影响。

### 7.2 真深头导数通常耦合频率

实际非轴对称深头不是逐模独立斜率。设真实参数化深头的线性 trace 提升为
$B:\mathbb R^d\to\mathcal Y$，$\mathcal Y$ 含所有非均值两分量；R43 后续参数化接口中 $d=46$。记 $R$ 为外 cut 的 $d$ 个实际有限约束组成的线性算子。允许内端还有完整 trace 缺陷 $\beta\in\mathcal Y$。

若所有传播与积分在所选解析空间中确有界，令

$$
\mathsf S=R\Phi(b,a)B .
\tag{44.51}
$$

若这个有限矩阵可逆，则准确的全频有限秩修正为

$$
G(x,t)=\mathbf1_{t\le x}\Phi(x,t)
-\Phi(x,a)B\mathsf S^{-1}R\Phi(b,t),
\tag{44.52}
$$

$$
B^{\rm cut}(x)=\Phi(x,a)B\mathsf S^{-1},
\qquad
B^{\rm in}(x)=
\Phi(x,a)[I-B\mathsf S^{-1}R\Phi(b,a)].
\tag{44.53}
$$

其证明与 (44.49) 完全相同，但 $q$ 为 $d$ 维参数，$\mathsf S$ 为实际 Schur 矩阵。公式允许 $B$ 耦合不同角频率；不把 canonical $\Xi$、非线性连接 $\Pi$ 和物理 $K$ 当成相同坐标。

有限频率公式是直接恒等式。要在全部频率上使用，必须用同一源、位置顺序和明确的条带空间付出 (44.52) 的有界性，才可按绝对收敛与支配收敛通过极限。单模恒等式或有限输出残差小，不自动给这个无限维门。

内端全部高模的两分量属于同一个真实参数化 trace。这里只施加 $R$ 中列出的外端约束；其他外端高高度是解的输出。任意把它们再固定为零，一般会把问题改成超定问题。

## 8. 残差、真深头反馈与外头固定点的接线

设 $\widehat y=(P,\overline K)$ 为本文候选，$\mathcal F(y)$ 表示 (44.42) 的非线性向量，即第一分量为零、第二分量为 $\mathscr P_\perp\mathcal N$。其残差为
$\widehat f=(0,\mathscr P_\perp(\mathcal J/L))$。

若真深头 trace 在参数 $q_0$ 附近为

$$
\mathcal D(q_0+\eta)
=\mathcal D(q_0)+B\eta+\mathcal R_D(\eta),
\tag{44.54}
$$

记 $\beta_0=\mathcal D(q_0)-\widehat y(a)$，$\alpha$ 为外端有限约束与候选之差。令

$$
f(e)=\mathcal F(\widehat y+e)-\mathcal F(\widehat y)-\widehat f.
\tag{44.55}
$$

那么真正待验证的联立积分系统可以写为

$$
e(x)
=\int_a^bG(x,t)f(e)(t)\,dt
+B^{\rm cut}(x)\alpha
+B^{\rm in}(x)[\beta_0+\mathcal R_D(\eta)],
\tag{44.56}
$$

$$
\eta
=\mathsf S^{-1}\left[
\alpha-R\Phi(b,a)(\beta_0+\mathcal R_D(\eta))
-\int_a^bR\Phi(b,t)f(e)(t)\,dt
\right].
\tag{44.57}
$$

**准确性。** 对 (44.56) 使用线性方程、边界提升和源核恒等式，结合 (44.57)，得到内端
$e(a)=B\eta+\beta_0+\mathcal R_D(\eta)$、
外端 $Re(b)=\alpha$ 以及
$e'=Ae+f(e)$。加回候选，恰是完整非均值外头方程与同一个真深头 trace。反向变常数公式给 (44.56)–(44.57)。因此它没有独立放松任何 trace 匹配条件。

在一个实际已核销的共同 Banach 盒上，如果 (44.56)–(44.57) 的映射及距离权收缩门通过，就由 Banach 定理得到完整外头解。其完整 mean 由定理 44.4 自动补回；node12 两侧同一 mean 分支的唯一性给相同 mean slope，mean 高度只需选一个统一积分常数。两侧的全部非均值 trace、完整 mean 及同一 Darboux 方程一致时，径向二阶 jet 也一致。

这里只给出准确映射，不声称当前 $\mathsf S^{-1}$、连续 $\widehat f$、深头参数 lift 或全频算子范数已经支付。R43 所需门与外头所需门必须分别核算。外头实核尚未产生时，不能用现有 node12 至 cuff 的213胞元核填入 (44.52)。

## 9. 对当前保存数据的具体意义

1. [13port 恢复包](../notes/2026-11-12-tail-outer-strong-m20-port-norms-recovery.json)给明确端点候选；它未给 (44.3) 的连续系数，也未给 (44.27) 的区间。
2. [109 原段端点工具](../computations/tail_outer_saved_segment_norms.py)只准备了严格真实半径上的点值。其结果可用于选择插值与细分位置，不能直接当作本定理的面板前提。
3. 下一真实数值输入是同一 $g$ 下的连续 $H_m,H_{m,r},H_{m,rr}$ 与 R26 背景。对这些输入，用 (44.18)–(44.24) 支付完整 $c,c_x$，再用有限 $\mathcal J$ 核算连续真实缺陷。
4. 未知修正的解析范数还须支付 (44.40)、实际外头传播/Schur 项，以及真深头参数化余项。对已知候选可以明示一次条带损失；对未知的迭代仍需同一个固定 Banach 空间，不能每次免费缩窄条带。

在完成这些实际门前，本结果只是已经证明的可执行数学接口；完整强幅度闭曲面、同问题精化、全时嵌入与 reach 的完成标准仍原样保留。
