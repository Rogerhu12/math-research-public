# R150 附录：不同最高根簇的跨核排斥与实结构下的剪切碰撞

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已独立核查不同倾斜的完整域、实际最高标量结果式、全部字符配对及总支撑排斥。
状态：已证明，完整证明。以两个不同最高符号的有限结果式排除核共存；
实结构使一部分真正的首位切向碰撞单核为零。
任意复指数权的两种倾斜明确换到同一组实际 first。

## 1. 两个最高符号互素时，核不能共存

取任意复 $\ell^2$ first
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=c_*+\sum_j c_j\chi_j,
$$
并假设 $X_u$ 空谱。
$v$ 可以有全平面谱，也允许有界；不限制首位先后。

固定整数 $k\ge1$。
令标量多项式 $F(x,y),G(x,y)$ 关于 $y$ 首一，
次数分别为 $m,n\ge1$，且各自满足
$$
i+kj\le km\quad([x^iy^j]F\ne0),
$$
$$
i+kj\le kn\quad([x^iy^j]G\ne0).
\tag{1.1}
$$
记各自的最高权部分为 $F_0,G_0$，并置
$$
H_F(Z)=F_0(1,Z),\qquad H_G(Z)=G_0(1,Z).
$$
它们首一，次数分别为 $m,n$。
允许重根、零根。
唯一的最高符号条件是
$$
\boxed{\gcd_{\mathbb C[Z]}(H_F,H_G)=1.}
\tag{1.2}
$$

给任意正整数 $r,s$ 及两个任意复 $\ell^2$ 指数权
$$
w_\nu=b_{\nu,*}+\sum_j b_{\nu,j}\chi_j,\qquad \nu=1,2.
$$
令 $\mathsf P$、$\mathsf Q$ 分别是
$F(u,v)^r e^{w_1}$ 与 $G(u,v)^s e^{w_2}$
相对于各自循环基向量 $e^{w_\nu}$ 的 R186 规范最大 Bell 实现。

**定理 1（跨核排斥）。**
$$
\boxed{
\ker\mathsf P\ne0\quad\Longrightarrow\quad
\ker\mathsf Q=0,
}
\tag{1.3}
$$
反向亦然。
更准确地，两核 $M,N$ 总满足
$$
\boxed{B(M,U_\zeta N)=0
\quad\text{对每个 dyadic }\zeta.}
\tag{1.4}
$$
这里包括 $\zeta=1$，没有有限例外。

可分别在 $F,G$ 中加入任意常数移位；
它们不改变最高符号。
结论不要求 $H_F,H_G$ 各自简单，
只要求它们彼此没有共同根。

## 2. 实模式的单核定理

以下再假设 $u,v$ 实，即常数项和两条系数行均为实数。
对标量多项式 $F$，记 $\overline F$ 为逐个系数取复共轭的多项式；
$\overline H_F$ 同理。

**定理 2。**
若 $F$ 满足 (1.1) 且
$$
\boxed{\gcd(H_F,\overline H_F)=1,}
\tag{2.1}
$$
则对任意 $\lambda\in\mathbb C$、
整数 $r\ge1$ 和任意复 $\ell^2$ 指数权 $w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 非零且对原 }A\text{ 循环}.
}
\tag{2.2}
$$

特别，若最高部分是一个任意重数的单簇
$$
F_0(x,y)=(y-cx^k)^m,\qquad c\notin\mathbb R,
\tag{2.3}
$$
则 (2.1) 自动成立；
权严格低于 $km$ 的全部标量混合项均可任意加入。
没有首位平移互素、非退化根或首位先后要求。

### 2.1 一个完整的多项式组合族

若 $\Psi$ 的次数为 $k\ge1$、最高系数 $c\notin\mathbb R$，
$q$ 是任意非恒定标量多项式、次数 $m$，
且 $\deg g<km$，则
$$
\boxed{
[q(v-\Psi(u))-g(u)-\lambda]^r e^w
\text{ 对全部 }\lambda,\ r\ge1,\ w\text{ 循环}.
}
\tag{2.4}
$$
先除 $q$ 的非零最高系数即可。
$q$ 的重复根和任意复系数都允许；
$\Psi$ 的低阶系数及 $g$ 也允许任意复数。

$k=1$ 特别给：
若实 $u$ 的 $X_u$ 空谱、$v$ 任意实 $\ell^2$ first、
$c\notin\mathbb R$，则
$$
\boxed{q(v-cu)e^w\text{ 对每个非零标量多项式 }q\text{ 循环}.}
\tag{2.5}
$$
不宣称 $X_{v-cu}$ 本身空谱。
$q$ 为非零常数时用已知 $e^w$ 循环。

## 3. 两种复指数倾斜准确换到共同域

先证明定理 1。
对指数 $w_\nu$，令
$$
X_\nu=X_{u,b_\nu}=X_u+H_{a,b_\nu},\qquad
Y_\nu=X_{v,b_\nu}=X_v+H_{c,b_\nu}.
$$
[R176 §10](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)
给真实范数收敛的有界扰动
$$
H_{a,b}=\sum_j a_j(R_j(b)-V_j)\in\mathcal A,
$$
以及完整同域恒等式。
因此可固定
$$
X=X_1,\qquad Y=Y_1,
$$
并写
$$
X_2=X+K_X,\qquad Y_2=Y+K_Y,\qquad K_X,K_Y\in\mathcal A.
\tag{3.1}
$$
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
的全部混合词域在这些有界交换扰动下相同，
各规范最大图是相应自然混合图的闭包。

设 $B^{(1)}_{ij},B^{(2)}_{ij}$ 为两种完整联合规范 Bell 系数。
第一多项式为
$$
P(x,y)=\sum_{i,j\ge0}\frac{B^{(1)}_{ij}}{i!j!}
\partial_x^i\partial_y^jF(x,y)^r,
$$
第二个先按其自身倾斜构造，再代入 (3.1)：
$$
Q(x,y)=
\sum_{i,j\ge0}\frac{B^{(2)}_{ij}}{i!j!}
(\partial_x^i\partial_y^jG(x,y)^s)
\big|_{x\mapsto x+K_X,\ y\mapsto y+K_Y}.
\tag{3.2}
$$
这些都是 $\mathcal A[x,y]$ 中的有限多项式，
包括全部交叉 Bell 项。

令
$$
M_0=mr,\qquad N_0=ns.
$$
$P,Q$ 关于 $y$ 首一，次数分别为 $M_0,N_0$。
在权 $\operatorname{wt}x=1,\operatorname{wt}y=k$ 下，
正阶微分以及有界平移都严格降低权。
所以实际最高权部分精确是
$$
P_{\rm top}=F_0^r,\qquad Q_{\rm top}=G_0^s.
\tag{3.3}
$$
它们是标量多项式乘 $I$；
此处不只是最高系数字符相同。

固定任意 dyadic $\zeta$。
把 $U_\zeta\mathsf Q U_\zeta^*$ 写到共同 $X,Y$：
$$
Q_\zeta(x,y)
=(\gamma_\zeta Q)(x+D_X,y+D_Y),
\tag{3.4}
$$
其中 $D_X,D_Y$ 是实际有界解析 first 增量。
同域性及共同词域由 R186 保证。
(3.4) 的最高部分仍准确为 $G_0^s$。
本稿不取 $(Q_\zeta-P)/A^h$，所以没有首位因子或有限 gauge 例外。

## 4. 最高项为标量单位的实际结果式

取
$$
E_\zeta(x)=\operatorname{Res}_y(P,Q_\zeta)\in\mathcal A[x].
$$
有限 Sylvester 伴随矩阵给
$$
\boxed{
E_\zeta=A_\zeta P+B_\zeta Q_\zeta,
\qquad A_\zeta,B_\zeta\in\mathcal A[x,y].
}
\tag{4.1}
$$

令 $t$ 为形式变量，置
$$
\widetilde P(t,Z)
=t^{kM_0}P(t^{-1},t^{-k}Z),\qquad
\widetilde Q_\zeta(t,Z)
=t^{kN_0}Q_\zeta(t^{-1},t^{-k}Z).
$$
由 (3.3)，它们均为真正的 $\mathcal A[t,Z]$ 多项式，
关于 $Z$ 首一、次数分别为 $M_0,N_0$，且
$$
\widetilde P(0,Z)=H_F(Z)^r I,\qquad
\widetilde Q_\zeta(0,Z)=H_G(Z)^s I.
\tag{4.2}
$$
结果式的准确缩放为
$$
\operatorname{Res}_Z(\widetilde P,\widetilde Q_\zeta)
=t^{kM_0N_0}E_\zeta(t^{-1}).
\tag{4.3}
$$
左侧没有负 $t$ 次幂，其常数项为
$$
c_0 I,\qquad
c_0=\operatorname{Res}_Z(H_F,H_G)^{rs}\ne0.
\tag{4.4}
$$
因此
$$
\boxed{
E_\zeta(x)=c_0x^D I+\sum_{j<D}E_{\zeta,j}x^j,
\qquad D=kM_0N_0.
}
\tag{4.5}
$$
这是实际有限系数恒等式，
最高系数准确为同一个非零标量；
未把某些更高零字符系数略去。

因为 $X=X_{u,b_1}$ 仍空谱，$L=X^{-1}\in\mathfrak C$ 有界且拟幂零。
定义
$$
\rho_\zeta=c_0I+\sum_{j<D}E_{\zeta,j}L^{D-j}
=c_0(I+LK_\zeta).
\tag{4.6}
$$
$L$ 与 $K_\zeta\in\mathfrak C$ 交换，
故 $LK_\zeta$ 拟幂零。
所以
$$
\boxed{\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C.}
\tag{4.7}
$$
R88 给 $\rho_\zeta M=M$，其中 $M=\ker\mathsf P$。

## 5. 全部 dyadic 字符上的跨核配对

令 $N=\ker\mathsf Q$，$N_\zeta=U_\zeta N$。
取 R186 的共同正则器 $R$，
选择有限 $N_*$ 覆盖 (4.1) 的全部次数、中间自然词及 $X^D$。
在
$$
f\in R^{N_*}M,\qquad
g\in U_\zeta R^{N_*}N
$$
上，所有混合自然域均真实有定义，
且
$$
P(X,Y)f=0,\qquad Q_\zeta(X,Y)g=0.
$$
$L^D$ 为有界交换子，保持这些共同域。

将 (4.1) 作用于 $f$ 并左乘 $L^D$，
用原 $H$ 上完整 $C$ 自伴的 $Q_\zeta$ 作配对：
$$
\begin{aligned}
B(\rho_\zeta f,g)
&=B(Q_\zeta(X,Y)L^DB_\zeta(X,Y)f,g)\\
&=B(L^DB_\zeta(X,Y)f,Q_\zeta(X,Y)g)=0.
\end{aligned}
\tag{5.1}
$$
不把 $C$ 下传到 $M$ 或 $N$；
这里只在原完整算子域上使用伴随关系。

两个正则测试空间分别在 $M,N_\zeta$ 中稠密。
由 (4.7) 及 R88，
$$
B(M,U_\zeta N)=0
$$
对每个 dyadic $\zeta$ 成立。
这里无需再消去 $A^h$，也无需调用未知慢算子的限制稠密性。

### 5.1 全部 Fourier 系数为零确实排除两核共存

固定 $f\in M,g\in N$。
$L^1$ 函数
$$
h_{f,g}(y)=f(y)g(-1-y)
$$
的每个 dyadic Fourier 系数都由 (5.1) 为零
（$U_\zeta$ 在反射坐标处只多一个非零标量相位）。
Fourier 唯一性给
$$
f(y)g(-1-y)=0\quad\text{几乎处处}.
\tag{5.2}
$$

若 $M\ne0$，取其可数正交基 $\{f_i\}$，
令 $\Omega_M$ 为这些向量本质非零集合的并。
严格正权和 $A$ 不变性给
$\Omega_M+1\subseteq\Omega_M$ 模零；
平移保测度，使之为模零相等。
odometer 遍历性及 $\mu(\Omega_M)>0$ 给
$$
\mu(\Omega_M)=1.
$$
若 $N\ne0$，同样 $\mu(\Omega_N)=1$。

于是
$$
\bigcup_{i,j}
\{y:f_i(y)\ne0,\ g_j(-1-y)\ne0\}
=
\Omega_M\cap(-1-\Omega_N)
$$
模零为全空间。
但 (5.2) 使每个集合都为零测，
可数并仍为零测，矛盾。
这完整证明两核不能共存，得到定理 1。

## 6. 实结构、不同倾斜及单核

令
$$
J_0f=\overline f
$$
为逐点复共轭。
实际 $A$ 的权为实数，所以 $J_0A=AJ_0$。

因为 $u,v$ 实，有限柱上的截断恒等式及真实图核心给
$$
J_0X_{u,b}J_0=X_{u,\overline b},\qquad
J_0X_{v,b}J_0=X_{v,\overline b}.
\tag{6.1}
$$
这是包含完整定义域的等式。
共同混合词及闭图取闭包后，完整 Bell 实现因而满足
$$
\boxed{
J_0\mathsf P_{F-\lambda,r,b}J_0
=
\mathsf P_{\overline F-\overline\lambda,r,\overline b}.
}
\tag{6.2}
$$
若左侧核非零，右侧核也非零。

两个指数分别为 $w$ 与 $\overline w$，
通常并不是同一个倾斜。
定理 1 的 §3 已准确处理该差：
$$
X_{u,\overline b}-X_{u,b}
=H_{a,\overline b}-H_{a,b}\in\mathcal A,
$$
$v$ 行同理。
这些真实有界平移降低权，不改变最高符号
$H_F$ 与 $\overline H_F$。
所以在 (2.1) 下，定理 1 排除 (6.2) 的两核同时非零，
原核必须为零。

原空间完整 $C$ 自伴给稠密像，
$\xi=e^w$ 的真实循环图核心给 (2.2)。
此处 $J_0$ 用于实结构，$C$ 用于原双线性配对，
二者作用明确分开。

## 7. 一个此前确有首位碰撞的实例

取
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
\quad \frac12<\sigma\le1.
$$
它们实，$u$ 为空谱锚，$v$ 为独立全平面 first。
令
$$
F(x,y)=(y-ix^2)^2+4x^2.
$$
取 $k=m=2$，
$$
H_F(Z)=(Z-i)^2,\qquad
\overline H_F(Z)=(Z+i)^2
$$
互素。故
$$
\boxed{
[(v-iu^2)^2+4u^2-\lambda]^r e^w
\text{ 对全部 }\lambda\in\mathbb C,\ r\ge1,\ w\text{ 循环}.}
\tag{7.1}
$$

这个例子不满足此前剪切稿的首位互素条件：
$\Psi(x)=ix^2$、$\alpha=1$ 时，剪切边是
$$
H_{\rm sh}(Z)=Z^2+4,
$$
首位平移量 $2kc\alpha=4i$。
$H_{\rm sh}(Z)$ 与 $H_{\rm sh}(Z+4i)$ 共有根 $-2i$，
所以那一个最高字符结果式确实为零。
(7.1) 用两个不同最高簇的跨核排斥关闭此真实碰撞，
没有把各个点态因子已循环当作乘积循环。

相反，
$$
(v-u^2)^2-4u^2-\lambda
$$
的最高中心为实数1，复共轭不产生不同根簇；
这一实切向边仍未由本文关闭。

## 8. 旧范围扣除与边界

- R150 先前的 Newton、剪切和中间带只覆盖各自的横截或互素条件；
  §7 明确给它们留下的真实碰撞新例。
- (2.5) 不要求新的复杂 first 有空谱；
  与 R134/138 的既有空谱点态多项式子类相交时按旧来源计。
- 最高符号彼此互素是准确条件。
  “出现一个非实系数”本身不足：
  例如 $H=(Z-1)(Z-i)$ 与 $\overline H$ 仍有共同根1。
- 不从 $H$ 没有实根推出 (2.1)：
  $H=Z^2+1$ 与其共轭相同，含共轭成对的根。
- 两个独立全平面 first 且没有空谱锚时，
  §4 的实际有界拟幂零逆仍缺失。
- 实最高簇的首位切向碰撞、一般慢系数在未知限制中的稠密性继续保留。

完整 Hilbert 不变子空间问题未完成。
