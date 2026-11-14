# R119 续篇：真实混合尾的角图、密度共轭和保型 canonical 框架

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇对实际非线性 exact-tail、整个 connector 和
已选双 bump，构造真正的角流共轭，并把完整 grounded Jacobi 方程及
普通密度源、两迹、mean/regular 列一起变换。型别零点保持为原背景的
$A(t)=0$；所有非线性 principal 变化保留在准确的角图和一个正标量
$\nu$ 中，没有将角 pullback 与恒等的同宽算子差假设为小。

这给下一步相对尾逆的实际 preconditioner。它尚未证明此新框架下的
全部高频 return/横截逆；特别不把 $\nu-1$ 小直接改成高频相位小。

## 1. 实际全相对 principal matrix 的准确判别式

用物理半径 $a$，$t=\log a+\text{常数}$，记
$A=aw_a/w$、$E=1+w^2$。保留 R119 的真实完整相对变量
$$
 P=u_\theta/(aw),\quad K=u_a/w,\quad U=P_\theta,\quad V=K_\theta,
 \quad J=1+K+EU,\quad Q=V-P,
$$
$$
 D=1-w^2(2K+K^2+EP^2),\qquad
 d=\frac{EQ}{J},\qquad v=\frac{\sqrt D}{J}.
 \tag{A.1}
$$
这里 $d$ 是角漂移，$v$ 是 principal 倍率，不与 grounded 高度混用。
实际相对方程是
$$
 P_t=K_\theta-(A+1)P,\qquad
 K_t=F=\frac{-A(2K+U+K^2+KU+w^2P^2)+EQ^2}{J}.
$$
对这一个真商式微分并约分，准确得到
$$
 F_U=-\frac{AD+E^2Q^2}{J^2}=-Av^2-d^2,
 \qquad F_V=\frac{2EQ}{J}=2d.
 \tag{A.2}
$$
因此 Jacobi 一阶系统的 principal matrix 为
$$
 \mathsf B=\begin{pmatrix}0&1\\-Av^2-d^2&2d\end{pmatrix},
 \qquad \operatorname{disc}\mathsf B=-4Av^2=-4AD/J^2.
 \tag{A.3}
$$
它的特征值是 $d\pm v\sqrt{-A}$。所有转折点仍准确由原 $A(t)=0$
给出；完整 mean 小根包含在 $K$ 内，没有改动这个结论。

不除以 $\sqrt A$ 的准确框架为
$$
 \mathsf T=\begin{pmatrix}1&0\\d&v\end{pmatrix},\qquad
 \mathsf T^{-1}\mathsf B\mathsf T
 =dI+v\begin{pmatrix}0&1\\-A&0\end{pmatrix}.
 \tag{A.4}
$$
它穿过 $A=0$ 仍合法。若 $N=\|P\|+\|K\|+\|U\|+\|V\|\le1/64$，
则可取 $\|d\|<3N$、$\|v-1\|<6N$，$\mathsf T$ 及其逆均小于2。
在真 Jacobi 方程中必须同时保留
$$
 \mathsf T^{-1}(\mathsf B\mathsf T_\theta+\mathsf C\mathsf T-\mathsf T_t),
 \quad
 \mathsf C=\begin{pmatrix}-(A+1)&0\\F_P&F_K\end{pmatrix};
 \tag{A.5}
$$
本篇没有删掉框架导数。

另有两个完整背景恒等式，说明没有隐藏 $A_t/A$ 奇异项：
$$
 (\partial_t-d\partial_\theta)\log v+d_\theta
 =\frac{A(1-v^2)-d^2}{E},
$$
$$
 d_t-d d_\theta-A v v_\theta
 =d\left[-1+\frac{A(w^2-v^2)-d^2}{E}\right].
 \tag{A.6}
$$
它们直接由同一 $P,K,U,V$ 方程、$w_t=Aw$ 推出；脚本以完整符号
变量及独立 $U_\theta,V_\theta$ 核到余项恒0。

## 2. 必须先用真实 grounded 动量

令真实北帽为 $F=(F_h,Z)$，$\mathsf S=F\cdot n>0$，并记
$$
 \mathfrak c=Z^2/\mathsf S^2,\qquad
 \kappa=\frac{w\mathfrak c}{Ea}>0,\qquad
 \mu=\frac{\kappa}{v}.
 \tag{A.7}
$$
对实际 grounded Jacobi 高度 $f=F\cdot\dot F/Z$，R119 (119.34) 的
物理版本准确给沿正 $a$ 方向的密度通量
$$
 \boxed{\quad p=\mu(f_t-d f_\theta).\quad}                 \tag{A.8}
$$
这里包含真实水平变化、$Z_a$ 和 normal/shear；不是把 raw 高度导数
直接命名为动量。相邻域使用相反 outward 方向时仍要翻号。

同一 grounded material 密度矩阵在 $(t,\theta)$ 中恰为
$$
 \boxed{\quad
 \mathsf M=\mu
 \begin{pmatrix}1&-d\\-d&d^2+Av^2\end{pmatrix},\qquad
 \det\mathsf M=A\kappa^2.
 \quad}                                                     \tag{A.9}
$$
证明如下。第一行由 (A.8) 已知。真实高斯方程给
$K_g=ww_a/(aE^2)=Aw^2/(a^2E^2)$。
R37 的 $\mathsf A=-\operatorname{cof}II/(\zeta_F^2\sqrt{\det g})$
及 $Y_z=Z/|F|$ 因而给
$\det(Y_z^2\mathsf A)=\mathfrak c^2K_g=A\kappa^2$。
二维 contravariant 密度的行列式在 $a\mapsto t$ 下不变，由此唯一
确定第二行。没有只比较一个方便的 principal 模型。

垂直平移是真正的 Jacobi 方向，所以 $Y_z$ 是当前真实算子的 ground
state。完整恒等式是
$$
 Y_z P(Y_zf)=\operatorname{div}(\mathsf M\nabla f).
 \tag{A.10}
$$
零阶项准确抵消，所有系数导数仍在 divergence 中。
因此对真实 ordinary grounded density source $s$，准确两迹系统是
$$
 \begin{split}
 f_t&=d f_\theta+\mu^{-1}p,\\
 p_t&=\partial_\theta(d p)-\partial_\theta(\mu A v^2f_\theta)+s.
 \end{split}                                               \tag{A.11}
$$
完整 mean 行特别为 $\langle p\rangle_t=\langle s\rangle$。

在 $A>0$ 的冻结 principal symbol 上，根是
$\lambda=i d\xi\pm\sqrt A\,v|\xi|$；**真实 conormal** 则给
$$
 p/f=\pm\kappa\sqrt A\,|\xi|.
 \tag{A.12}
$$
角漂移和倍率 $v$ 都准确抵消。该式只标识 principal symbol，
不据此省略完整非局部 return 或低阶项。

## 3. 在同一整条实际尾上构造真角流

先说明所用角流不是一个形式变换。整个无限尾的公共物理角宽可取
$\sigma_*=\tau-1$，$\tau=5177/400$。
源 R72 的完整连续局部解给
$$
 Y_{\rm true,j}\le2^{35}\delta_j^{-1}h_j^{-5}\zeta_j\|X\|,
 \quad w_{\min,j}\ge\epsilon\delta_j^7/256,
 \quad \zeta_j=\epsilon\delta_j^{39/4}.
$$
其中 $Y_{\rm true,j}$ 控制完整 $(p,\kappa)$ 的强一阶角 norm；
它由源 R72 (4.6)、(5.6) 直接相加，后项远小于前项。
把四状态和及所有分量保守付一个8，再用 R115 的
$h_j^{-5}\le2^{18}\delta_j^{-5/256}$，有
$$
 N_j\le2^{64}\delta_j^{443/256}\|X\|<2^{-164},\qquad j>128.
 \tag{A.13}
$$
这里 $\|X\|<1$，$\delta_{129}<2^{-132}$。
这还证明相对状态在真实平尾累积圆趋零，所以 $d\to0,v\to1$。
准确尾长为
$$
 \sum_{j>128}\ell_j/\sqrt{12}
 <2\sum_{j>128}\delta_j=2\delta_{128}<2^{-130}.
 \tag{A.14}
$$
已经安装的整个 connector 加双 bump 的长度小于132，且由前面续篇
其完整状态在大于 $\tau+1968$ 的实际角宽上小于 $2^{-8423}$。

从真实平尾累积圆开始，在每个有限段解
$$
 \phi_t(t,\eta)=-d(t,\phi(t,\eta)),\qquad
 \phi(t_f,\eta)=\eta.
 \tag{A.15}
$$
尾上 $\sigma_*$ 到 $\tau-2$ 的余宽给
$\|d\|,\|d_\theta\|<2^{-162}$；connector/bump 上可取 $2^{-8420}$。
所以整条实际区间有
$$
 \int (\|d\|+\|d_\theta\|)\,dt<2^{-289}.
 \tag{A.16}
$$
在复条带 $|\operatorname{Im}\eta|<\tau-3$ 上位移小于这个数，始终
留在所用系数条带内。ODE 积分及
$\phi_\eta=\exp(-\int d_\theta(t,\phi)dt)$ 给完整存在性、唯一性。
对更窄一单位条带作 Fourier Cauchy 估计，得到一个宽松统一界
$$
 \boxed{\quad
 \|\phi-\mathrm{id}\|_{\mathcal A_{\tau-4}}
 +\|\phi_\eta-1\|_{\mathcal A_{\tau-4}}<2^{-280}.
 \quad}                                                     \tag{A.17}
$$
无限端由 (A.13)–(A.16) 的绝对可积性取得；不以有限截尾替代。
实角下这是实际圆周微分同胚。由于 $d$ 奇且四重周期，$\phi$ 奇，
满足 $\phi(\eta+\pi/2)=\phi(\eta)+\pi/2$，所以既有反射规范保留。

## 4. 准确角图共轭，通量必须作为密度变换

置 $j=\phi_\eta>0$，准确取
$$
 \widetilde f=f\circ\phi,\qquad
 \widetilde p=j\,(p\circ\phi),\qquad
 \widetilde s=j\,(s\circ\phi).
 \tag{A.18}
$$
直接代入 (A.11) 后，所有角漂移项与 $j_t$ 项准确相消：
$$
 \boxed{\quad
 \widetilde f_t=\widetilde a^{-1}\widetilde p,\qquad
 \widetilde p_t=-\partial_\eta(\widetilde b\,\widetilde f_\eta)
                        +\widetilde s,
 \quad}                                                     \tag{A.19}
$$
其中
$$
 \widetilde a=(\mu\circ\phi)j,\qquad
 \widetilde b=(\mu A v^2\circ\phi)/j,
 \qquad \widetilde a\widetilde b=A(\kappa\circ\phi)^2.
 \tag{A.20}
$$
若只对 $p$ 作普通函数 pullback，不乘 $j$，就会多出错误的
$d_\theta$ source 并破坏 mean 行。

这个变换保留完整边界配对
$$
 \int f p\,d\theta=\int\widetilde f\widetilde p\,d\eta,
 \qquad \int p\,d\theta=\int\widetilde p\,d\eta,
 \qquad \int s\,d\theta=\int\widetilde s\,d\eta.
 \tag{A.21}
$$
高度的物理 mean 则是 $\int\widetilde f j\,d\eta$，不是把它无声换成
$\int\widetilde f\,d\eta$。全部 Fourier 模先整体变换，再作任何需要的
投影；因此低高交叉和 mean 都保留。

由 (A.17)，高度 pullback 及逆在实 $L^2$、$H^1$ 上 norm 均小于2；
分别改变变量并对一阶导使用 $1/2<j<2$ 即得。
插值给 $H^{1/2}$ 同界，配对对偶给密度在 $H^{-1/2}$ 的同界。
所以这是完整 $H^{1/2}\oplus H^{-1/2}$ 两迹的有界双向共轭。
本篇不声称它与恒等的同宽 operator norm 差趋零：高频仍须使用这个
真正的 pullback。

## 5. 支付退化幅度并保留完整 lower-order 行

令 $k=(\kappa\circ\phi)^{1/2}$，定义真正的 symplectic 幅度变量
$$
 f^\#=k\widetilde f,\qquad p^\#=k^{-1}\widetilde p,
 \qquad \nu=(v\circ\phi)/j>0,
 \qquad a_k=k_t/k,\quad q_k=k_\eta/k.
 \tag{A.22}
$$
于是整个系统准确变成
$$
 \boxed{\begin{split}
 f^\#_t&=a_k f^\#+\nu p^\#,\\
 p^\#_t&=-a_kp^\#-A\partial_\eta(\nu f^\#_\eta)
    +A[(\nu q_k)_\eta+\nu q_k^2]f^\#+k^{-1}\widetilde s.
 \end{split}}                                               \tag{A.23}
$$
这是原完整真算子的恒等变换；$a_k$、$q_k$、完整角乘积导数和源均保留。
principal admittance 在这个框架中准确为
$p^\#/f^\#=\pm\sqrt A\,|\xi|$；实际射线速度仍是
$\pm\nu\sqrt{-A}$，不能把 $\nu$ 或其真实相位变化删掉。

退化尾上 $\kappa\to0$，所以不能声称 (A.22) 在无权全尾 norm 中有
统一有界逆。对应的准确切口空间须使用
$$
 \|(f,p)\|_{\mathfrak B_\kappa}
 :=\|k\,(f\circ\phi)\|_{H^{1/2}}
   +\|k^{-1}j\,(p\circ\phi)\|_{H^{-1/2}},
 \tag{A.24}
$$
并单独保留完整尾的平盘平移标签 $\lambda$。
这个 norm 用的是显式真实几何系数及已构造角图，不包含一个未知逆。
没有将它当作原无权标签范数或自动套用 R74 的基态常数。

实际 regular 平移列在该框架为 $(f^\#,p^\#)=(k,0)$，并非一个可删掉的
纯常数列。将它代入 (A.23)，两行准确成立。
真实 mean flux 是 $\int k p^\#d\eta$；高度 mean 是
$\int k^{-1}f^\# j\,d\eta$。这些权必须和完整 source 一起带入后续 Schur。
在平尾端 $k\to0$ 不能由 canonical 迹趋零反推 $\lambda=0$。

## 6. 对真实高输入逆的下一项

实际混合尾与长正段现在可在 (A.18)、(A.22) 的真输出角图/幅度中
接合。尾的 principal 型别、真实 conormal、ordinary density source、
两迹 pairing 和 mean/regular 均已具体化。
R119 的更新后长段 DN 续篇已付同一切口的相对误差；仍需控制
(A.23) 在**实际** $\nu,a_k,q_k$ 下的全频 return 和完整强 source。
原点的 $2^{-40}$ 横截门不能因 (A.17) 很小而自动转授：
高频要用真实角图及真实射线相位作为 preconditioner。

[准确代数与门程序](../scripts/fourfold_actual_tail_angle_density_20261113.py) 与
[完整报告](../notes/2026-11-13-R119-actual-tail-angle-density-budget.json)
核 principal 恒等式、两个完整背景恒等式、真实角流预算和退化幅度账。
