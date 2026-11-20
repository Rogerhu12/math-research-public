# R138 补篇：真实旋转场能量、转折处正平方与完整端点型

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明：**在 R138 的同一径向 frame 构造上，完整物理 Codazzi Jacobi 方向有一个无需高度图的旋转场能量。其角缺陷满足只含一次径向积分的明确方程；能量误差由原中心 residual、真实初始缺陷和物理源控制，方向只用角向 $L^2$。正曲率能量还控制沿真实特征漂移的旋转场，常数没有 $1/K$，可一直到 $K=0$ 的端点。

本文给出原 root/outer 数据必须代入的完整边界二次型，以及平面内圈的一个确实成立的刚性推论。当前候选的实际 root 并未被认作平面；193 行、高 stable 输入、独立 mean 和初始 frame 匹配仍保留。没有执行数值计算，也没有宣告当前全正区 inverse 已证。

## 1. 同一物理对象与一个更短的角缺陷方程

沿用 [R138](R138-residual-sensitive-Codazzi-frame-and-geometric-Jacobi-bridge.md) 的全部物理记号：
$$
g=e^2dr^2+a^2d\theta^2,\quad
O=(X,Y,n),\quad n=Y\times X,\quad
Z=O_\theta-O\Omega_\theta,\quad P=F_\theta-aY.
\tag{E.1}
$$
$F_r=eX$；$\mathrm{II}=\begin{psmallmatrix}A&B\\B&C\end{psmallmatrix}$，
$AC-B^2=K$，$C\ne0$。所有角积分均在真实物理 $2\pi$ 圆上。曲率的四重对称不把环境向量 frame 的周期改成 $\pi/2$。

固定 metric，取完整方向
$$
\dot{\mathrm{II}}=
 \begin{pmatrix}\alpha&b\\b&c\end{pmatrix},\qquad
\alpha=(2Bb-Ac)/C,\qquad
f=(f_B,f_C)=(\delta R_B,\delta R_C).
\tag{E.2}
$$
同一径向构造的变分 $\delta O$ 满足正交性微分。因此有唯一环境向量场 $\omega$ 使
$$
\delta O=\omega\times O.
$$
这里 $\omega\times O$ 按列作用。比较径向 frame 方程，准确得到
$$
\omega_r=e(-bX+\alpha Y).
\tag{E.3}
$$
定义完整角缺陷
$$
H=\omega_\theta-a(-cX+bY).
\tag{E.4}
$$
若 $T=\delta Z$，则等价地
$$
H\times O=T-\omega\times Z.
\tag{E.5}
$$
但直接对 (E.4) 径向求导更好：
$$
\boxed{\quad
H_r=a(f_CX-f_BY)+e(-bZ_X+\alpha Z_Y).
\quad}
\tag{E.6}
$$

**证明。** 将
$X_\theta=b_0Y+aBn+Z_X$、
$Y_\theta=-b_0X+aCn+Z_Y$、
$X_r=eAn$、$Y_r=eBn$
代入 $\partial_\theta\omega_r-\partial_r[a(-cX+bY)]$。
$X,Y$ 系数分别为
$a[c_r-\gamma b_\theta-\beta(\alpha-c)]=af_C$
和
$-a[b_r-\gamma\alpha_\theta+2\beta b]=-af_B$。
法向系数为 $ea(C\alpha-2Bb+Ac)=0$；余下恰是 (E.6)。

(E.6) 不含 $\omega$，不含方向的角导数，也不需 base residual 的角导数。它是同一真实物理源 $f$ 的公式。若输入来自 moving 算子或 WVC，仍先使用 R138 的 (J.32)--(J.34)；不能在这里把协变源或 $\eta_*-\eta_c$ 的主部差删掉。

令 $\|\cdot\|_2$ 为真实角圆的 $L^2$ 范数，并定义
$$
k_2=e\|(b,\alpha)\|_2,\quad V_2=\|\omega\|_2,\quad H_2=\|H\|_2.
$$
R138 的 $\zeta_0$ 控制 $\|Z\|_\infty$。对 $r\ge r_0$，有
$$
\begin{split}
V_2(r)&\le V_2(r_0)+\int_{r_0}^r k_2(t)\,dt,\\
H_2(r)&\le H_2(r_0)+
 \int_{r_0}^r\{a\|f\|_2+\zeta_0k_2\}(t)\,dt.
\end{split}
\tag{E.7}
$$
反向使用相应绝对积分。没有未知 inverse 常数。初始 $H_2(r_0)$ 是实际角向 frame 匹配的费用，不能仅凭 $f=0$ 设成零。

连续径向分片逐片使用这些式子；真实曲率 jump 输入按其分布源进入 $f$，并在 (E.7) 中加上对应的 $H$ jump。不能将独立 jump 端口改成普通 $dr$ 源。

## 2. 带完整 residual 误差的环境能量恒等式

固定环境点 $p$，置 $G=F-p$。引入一形式
$$
\lambda=G\cdot(\omega\times d\omega).
\tag{E.8}
$$
普通微分给
$$
d\lambda=
\{F_r\cdot(\omega\times\omega_\theta)
-F_\theta\cdot(\omega\times\omega_r)
+2G\cdot(\omega_r\times\omega_\theta)\}\,dr\wedge d\theta.
$$
把 $F_\theta=aY+P$、(E.3)--(E.4) 代入。前两项的理想部分相消，而且
$$
e(-bX+\alpha Y)\times a(-cX+bY)
=-ea\,\det(\dot{\mathrm{II}})\,n
$$
，因为 $X\times Y=-n$。所以
$$
\boxed{\quad
d\lambda=\{-2ea(G\cdot n)\det(\dot{\mathrm{II}})+\mathcal E\}\,
dr\wedge d\theta,
\quad}
\tag{E.9}
$$
其中完整误差是
$$
\boxed{\quad
\mathcal E=eX\cdot(\omega\times H)
-P\cdot(\omega\times\omega_r)
+2G\cdot(\omega_r\times H).
\quad}
\tag{E.10}
$$

设 $G_\infty(r)=\sup_\theta|G(r,\theta)|$，并使用 R138 的
$\pi_0\ge\|P\|_\infty$。Cauchy--Schwarz 逐项给
$$
\int_I\!\int|\mathcal E|\,d\theta\,dr
\le
\boxed{\quad
\mathfrak E=
\int_I\{eV_2H_2+\pi_0V_2k_2+2G_\infty k_2H_2\}\,dr .
\quad}
\tag{E.11}
$$
结合 (E.7)，右侧由指定中心的 frame residual 包络、方向的角 $L^2$、完整物理源及初始数据直接构造。没有方向角导数或先验全频逆。若 base 与方向初始角缺陷均为零，base Codazzi residual 为零且 $f=0$，则 $P=Z=H=0$，此误差准确为零。

## 3. Gauss 约束的正平方与真实端点式

写
$$
u=B/C,\qquad \kappa=K/C^2,\qquad d=b-uc.
$$
由 (E.2) 得逐点准确恒等式
$$
\boxed{\quad
Q:=-\det(\dot{\mathrm{II}})
=d^2+\kappa c^2 .
\quad}
\tag{E.12}
$$
当 $K>0$ 时 $Q$ 正定。当 $K=0$ 时它仍非负，但不能用它单独控制 $c$。另外，正曲率处有
$$
Q\ge
\frac{K}{A^2+2B^2+C^2}\,|\dot{\mathrm{II}}|_{\rm HS}^2.
\tag{E.13}
$$
证明可将 $\mathrm{II}$ 正交对角化为同号 $\lambda_1,\lambda_2$；
线性 Gauss 式为 $\lambda_2\alpha+\lambda_1c=0$，比较两个二次型即得 (E.13)。

在所用闭圆柱 $I=[r_L,r_R]$ 上，若已证某固定符号
$\sigma\in\{-1,1\}$ 使
$$
s=\sigma G\cdot n>0,
$$
定义
$$
\mathscr Q=\int_I\!\int ea\,s\,Q\,d\theta\,dr.
\tag{E.14}
$$
这里要求的是已构造 frame 的 support；不需要存在一个全域正的 $n\cdot k$。若要认作实际浸入的 support，还须支付 R138 的 $P$ 误差。

写
$$
\mathcal B(r)=\int \lambda(\partial_\theta)(r,\theta)\,d\theta .
$$
Stokes 定理及 (E.9) 给
$$
\boxed{\quad
2\mathscr Q
=\sigma\{\mathcal B(r_R)-\mathcal B(r_L)\}
-\sigma\int_I\!\int\mathcal E\,d\theta\,dr .
\quad}
\tag{E.15}
$$
若所用实现还允许 $F,O,\omega$ 自身有真实接口跳，则需另加各接口两侧 $\lambda$ 的有向差；准确连续修补中心及连续 frame 构造本身没有这项。
若 $\zeta=\omega\cdot n$、$\omega_X=\omega\cdot X$、
$\omega_Y=\omega\cdot Y$，完整端点密度是
$$
\boxed{\quad
\lambda(\partial_\theta)=
a\{[\zeta(G\cdot X)-(G\cdot n)\omega_X]b
 +[\zeta(G\cdot Y)-(G\cdot n)\omega_Y]c\}
+G\cdot(\omega\times H).
\quad}
\tag{E.16}
$$
这同时保留 $b,c$ 的 mean、所有角模、真实 frame 和角缺陷。

用 R138 的 $\mathfrak M_Q=(D\Psi)^{-1}$，本题端点域准确是原
$\mathcal B_L\mathfrak M_Q(b,c)$、
$\mathcal B_R\mathfrak M_Q(b,c)$ 以及原 high stable/regular 和独立 affine/source 行。实际低端 193 行见 R138 (J.28)；(E.16) 应在这个完整域上估计。不能把 root 的非mean moving even 行直接改写成 $c=0$，也不能把 WVC 辅助 cooperative Robin 线当成实际 high graph。

实际端帽如果提供准确匹配的 frame 方向，可从该端向内初始化，使其初始角缺陷为零；只有完整物理两迹及对应实际端帽已经匹配时，才能使用
[完整物理匹配定理](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)。
一般 periodic curvature 数据单独不提供这个初值。

## 4. 能量控制旋转的常数无需除以 $K$

(E.12) 的优点比粗界 (E.13) 更强。对真实物理漂移
$$
D=\partial_r-\gamma u\,\partial_\theta,\qquad \gamma=e/a,
$$
(E.3)--(E.4) 给
$$
\boxed{\quad
D\omega=e\{-dX+(ud-\kappa c)Y\}-\gamma uH .
\quad}
\tag{E.17}
$$
对 $K\ge0$，二维矩阵的 operator norm 不超过其
Hilbert--Schmidt norm，故
$$
|-dX+(ud-\kappa c)Y|^2
\le(1+u^2+\kappa)(d^2+\kappa c^2)
=(1+A/C)Q.
\tag{E.18}
$$
这一步在 $K=0$ 处仍成立，且没有除以 $\kappa$。

记
$$
q_2(r)^2=\int Q\,d\theta,\quad
L(r)=\tfrac{\gamma}{2}\|u_\theta(r)\|_\infty,\quad
m(r)^2=1+\sup_\theta A/C.
$$
角向分部积分后得到
$$
\frac{d}{dr}V_2
\le L V_2+e\,m\,q_2+\gamma\|u\|_\infty H_2
\tag{E.19}
$$
的上 Dini 导数版本，因而适用于 $V_2=0$ 的点。
若 $s_{\min}(r)=\min_\theta s(r,\theta)>0$，令
$$
C_G^2=\int_I\frac{e\,m^2}{a\,s_{\min}}\,dr,\qquad
\Lambda=\int_I L\,dr.
$$
由 (E.14) 和 Cauchy--Schwarz，
$$
\boxed{\quad
\sup_I V_2
\le e^\Lambda
\left\{V_2(r_L)+C_G\sqrt{\mathscr Q}
+\int_I\gamma\|u\|_\infty H_2\,dr\right\}.
\quad}
\tag{E.20}
$$
反向初始化有相同绝对系数界。只要 $C$ 有原图正间隙、support 有正下界且所列系数有界，$C_G$ 就在简单转折端点有限；不出现 $\int dr/K$。这是可以直接消费的真实旋转场能量估计，未先假定正区 inverse。

(E.20) 不把 $\sqrt K\,c$ 的控制升级为无权 $c$ 控制。当前完整输入窗、turning-point trace、所有 source 和同一边界图仍需原强/弱估计；本文没有以这个能量替代那些域。

## 5. 一个真正的边界消失机制及其近似费用

先给无需数值的准确推论。设 base 完全满足 Gauss--Codazzi，且方向 $f=0$，同一实际 frame/位置方向已匹配，故 $P=Z=H=0$。假定：

1. $K>0$ 在开圆柱内。
2. 内圈 $F(r_L,\theta)$ 在一个平面 $\Pi$ 内，物理方向准确满足 $c(r_L,\theta)=0$；并存在 $p\in\Pi$ 和符号 $\sigma$ 使第 3 节的 support 在所用圆柱上为正。
3. 外圈的旋转方向为常向量，即 $\omega_\theta(r_R,\theta)=0$。

则 $\dot{\mathrm{II}}=0$，相应真实等距方向只有整体 Euclidean 刚体。

**证明。** 取 $p\in\Pi$，记其单位法向为 $\xi$。
因为 $c=0$，内圈上 $\omega_\theta=abY$ 与平面相切，
所以 $\omega\cdot\xi$ 是常数。减去一个常旋转后，
$\omega$ 在该圈也与平面相切。于是 $G,\omega,\omega_\theta$
三个向量都在同一二维平面，内圈 $\lambda(\partial_\theta)=0$。
外圈由第 3 条同样为零。由 (E.15) 得 $\mathscr Q=0$，
(E.12) 及 $K>0$ 给 $\alpha=b=c=0$，再由 frame 与位置方程得到
$\delta F=\omega_0\times F+t_0$。内端取极限由连续性覆盖。
若另有实际持握条件，按原规范去掉这些整体刚体。

这个推论没有要求 $n\cdot k$ 在整个正区同号。它也没有声称当前真实 root 满足第 2 条，或当前外部 regular graph 自动等价于第 3 条。

更一般地，在任一实际端圈上选固定平面法向 $\xi$ 和该平面内的 $p$，记
$$
\delta_\Gamma=\|G\cdot\xi\|_\infty,\qquad
\tau_\Gamma=\|Y\cdot\xi\|_\infty,\qquad
G_\Gamma=\|G\|_\infty .
$$
通过减去一个整体常旋转，把该圈的 $\langle\omega\rangle_\theta$ 取为零。令
$$
\Theta=\|\omega_\theta\|_2,\qquad
\Theta_n=\|\omega_\theta\cdot\xi\|_2.
$$
真实 $2\pi$ 圆上的 Poincaré 常数为 $1$，故
$\|\omega\|_2\le\Theta$、
$\|\omega\cdot\xi\|_2\le\Theta_n$。由 (E.4)，
$$
\begin{split}
\Theta&\le a\|(b,c)\|_2+H_2,\\
\Theta_n&\le a\{\|c\|_2+\tau_\Gamma\|b\|_2\}+H_2 .
\end{split}
\tag{E.21}
$$
将三个向量相对于 $\xi$ 分解，准确得到可用边界费用
$$
\boxed{\quad
|\mathcal B(r)|
\le\delta_\Gamma\Theta^2+2G_\Gamma\Theta\Theta_n .
\quad}
\tag{E.22}
$$
这是真实端点迹和几何缺陷的界。对平面内圈、$c=H=0$，
右侧为零；在实际 moving 边界上则先用完整 $D\Psi$ 计算 $c$，
包括独立 mean 与角图变化。

一个常旋转会同时改变 (E.16) 和 (E.10) 中相应项；(E.15)
始终不变。使用 (E.22) 的规范时，(E.7) 的初始旋转数据也取同一个规范，不能只改边界而保留旧初值费用。

## 6. 对当前正区真正留下的可检验条件

对同一个完整 homogeneous 边界域，若逐项证明
$$
\sigma\{\mathcal B(r_R)-\mathcal B(r_L)\}\le b_*\mathscr Q,
\qquad
\mathfrak E\le e_*\mathscr Q,\qquad b_*+e_*<2,
\tag{E.23}
$$
则 (E.15) 给 $\mathscr Q=0$。若 $K>0$ 在开区间，
齐次曲率核随即为零。若原同一闭实现另外已有 index-zero
Fredholm 性，才可据此推出该实现的可逆性；定量 source/strong
常数仍须按同一范数导出。

(E.23) 的内容现已是具体表达式：边界用 (E.16)，base/source
误差用 (E.7)、(E.11)，旋转量可用在转折处有限的 (E.20)。
近乎平面的真实边界还可使用 (E.21)--(E.22)。
这里没有用“当前 inverse 的范数”定义任何一项。

尚不能删除的当前量是实际 support、完整初始/外部 frame
匹配、193 加 high 边界域上的符号或费用，以及把现有弱输入窗
接到这些能量迹的费用。单有小 Codazzi residual 并不使任意初始
$H$ 小；单有标量 Dirichlet 正性也不决定 (E.16) 的符号。
本补篇完成具体几何能量及非循环传播估计，未添加新振幅条件，
也未把这些尚未核值的量写成全局 existence。

