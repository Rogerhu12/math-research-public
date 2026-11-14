# R119 续篇：真实非零标签的联合解析根图与同空间 Airy 两迹比较

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇使用第8193层起首剪切为 $2^{128}$ 的
[新公共度量和完整局部解](R119-supplement-stronger-deep-first-shear-and-complete-local-map.md)，
以及其[真实全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)。
在每个实际 simple 转向根的一个固定缩放复邻域内，完整非线性
背景对径向和角变量联合解析。其实际特征坐标把完整 raw Jacobi
算子化为一个真实 Airy 主部和完整解析 potential；不是只匹配
principal symbol 或有限 root jets。

在这些**实际 canonical 截面和两态**中，负侧根块与同一径向
参考的相对 Cauchy 差在每个 $H^s\oplus H^s$、$|s|\le4$ 上
有界，没有角宽损失。若已构造的非线性尾满足
$\|X\|_{\mathcal X_{224}}\le2^{-262144}$，全部实际根块的相对
误差和小于 $2^{-97720}$。完整 mean、高度、conormal、ordinary
密度源和弱源的准确变换均保留。

这个结论没有把该条件称作**非线性**外边界已经匹配：前篇给出的
真实小输入仍是线性 regular 列。根块另一端是实际 constant
canonical 截面，在原坐标中一般为径向图。它与 strict 段、正型
两端 DN 及整个 mixed return 的接线仍须支付。下文也不从一个
径向—角混合图的存在，免费推出各向异性源范数不变。

## 1. 同一个真实根及可消费的输入

令 $e$ 是第 $j\ge129$ 个实际胞元中一个上升 quintic 的根。
以 $t=\log r$ 为共同材料径向坐标，物理半径为
$a_{\rm phys}=\rho(\Gamma)r$。写
$$
 Q=-A,\qquad b=|Q_t(t_e)|,\qquad
 x=\varsigma b(t-t_e),\qquad \varsigma\in\{1,-1\},
 \tag{J.1}
$$
其中 $x>0$ 指向负型一侧。由
[准确参考根证明 (F.5)--(F.8)](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)，
包括新 $2^{128}$ 首剪切在内，每个这样的根准确满足
$$
 Q(x)=xB_0(x)=x+(14d_0-1/28)x^2-d_0x^3-7d_0^2x^4,
 \quad0<d_0<2^{-10},\quad |B_0-1|<1/16\ (|x|\le1).
 \tag{J.2}
$$
到最近仅 $C^2$ 径向接缝的 $x$ 距离大于13。
$b>\delta_j^{-9/4}>2^{200}$，所以这里没有跨接缝使用解析性。
参数 bump 的支集与此根 germ 不交；$Q,b,t_e$ 在共同 $r$
坐标中不随 $\Gamma$ 改变。完整非径向解当然仍依赖全部参数。

以下全部 Fourier 系数取 $m\in4\mathbb Z$，含 $m=0$。
令 $\mathcal A_s^1$ 的 norm 为
$\sum_m(1+|m|)e^{s|m|}|u_m|$，向量取分量 norm 之和。
全标签篇的完整四态界给
$$
 N_j=2^{184}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \qquad n_j:=4N_j\|X\|_{\mathcal X_{224}},
 \qquad \|(P,K)(t_e)\|_{\mathcal A_4^1}\le n_j.
 \tag{J.3}
$$
这里 $\mu_j,\zeta_j,h_j$ 完全使用新尾的真实定义；尤其
$\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}$ 没有删除。
因真实角宽大于 $\tau_{128}+224>236$，使用宽4不增加输入
标签权。系数预算只用这一固定余宽，不从每个 Jacobi 输入再借角宽。

直接在第129层检查，随后在两个准确切换层分别检查，得到
$\sup_jN_j<2^{-30}$。故完整复标签球
$\|\mathbf a\|_{\ell^1_{224}}<2^{-8}$ 上，
$\|X\|<16\|\mathbf a\|<1/16$ 给 $n_j<2^{-32}$。
若另有本篇开头的真实 $X$ 条件，全标签篇 (U.25) 则给
$$
 n_j<2^{-102142},\qquad
 \sum_{e\ {m roots}}n_e
 \le16\|X\|\sum_{j\ge129}N_j
 <2^{160004}\|X\|.
 \tag{J.4}
$$
每胞两个上升 ramp 各有两个根，故这里的16是完整的四根计数
乘 (J.3) 的4。$(K_j^{\rm ref})^2>1$ 使 (U.25) 可直接用于
本式；未把有限8192层前缀从无限求和中去掉。

实际背景还满足 $|w|<1/16$ 在 $|x|\le1$：实根处由真实
$2K_j\mu_j\delta_j^{-1}$ 包络得到更强的 $|w_e|<2^{-64}$，
而 $w_x=\varsigma A w/b$ 只多乘 $e^{2/b}<2$。

## 2. 完整非线性方程的联合 CK 延拓

使用完整相对变量，而非截断到有限个角模：
$$
 U=P_\theta,\quad V=K_\theta,\quad E=1+w^2,\quad
 J=1+K+EU,
$$
$$
 P_t=V-(A+1)P,\qquad
 K_t=\frac{-A(2K+U+K^2+KU+w^2P^2)+E(V-P)^2}{J}.
 \tag{J.5}
$$
此处 $K_0$ 就是原 holonomy-one 小根的真 mean，不能清零。
本节直接解未投影的 (J.5)，不把有限 Galerkin 的完整压缩
leading inverse 偷换为逐点截断商式。

下面给出一个具体的 CK 收缩，避免引用没有常数的解析定理。
置 $\lambda=2^{12}/b<2^{-188}$。对在 $|x|<1$ 解析的
Fourier 系数定义
$$
 \|f\|_{\mathcal B^k}=
 \sum_m(1+|m|)^k e^{4|m|}
       \sup_{|x|\le1}e^{-\lambda(1+|m|)|x|}|f_m(x)|,
 \qquad k=0,1.
 \tag{J.6}
$$
可先在稍小闭盘定义再取单调极限。完整卷积给
$\|fg\|_{\mathcal B^0}\le e^\lambda\|f\|_{\mathcal B^0}
\|g\|_{\mathcal B^0}<2\|f\|\|g\|$，且
$\|f_\theta\|_{\mathcal B^0}\le\|f\|_{\mathcal B^1}$。
证明前一式时，频率三角不等式留下
$e^{-(4-\lambda|x|)(|m_1|+|m_2|-|m_1+m_2|)}\le1$；
没有把径向上确界和 Fourier 求和交换。

写 (J.5) 的右侧为 $\mathscr F$。在
$\|(P,K)\|_{\mathcal B^1}\le r_0=2^{-16}$ 上，
$|A|<2,|E|<2$ 及完整商法则给
$$
 \|J-1\|_{\mathcal B^0}\le2r_0,\quad
 \|J^{-1}\|_{\mathcal B^0}<2,\quad
 \|\mathscr F(W)-\mathscr F(\widetilde W)\|_{\mathcal B^0}
             <64\|W-\widetilde W\|_{\mathcal B^1}.
 \tag{J.7}
$$
为逐项说明常数：第二行分子 norm 小于 $5r_0$，其 Lipschitz
常数小于5；$J^{-1}$ 的 Lipschitz 常数小于32。乘法费用后
第二行常数小于 $20+320r_0<21$，第一行小于3，所以64
留有余量。这里 $\mathscr F(0)=0$。

对径向 Volterra 算子
$\mathcal V f=(\varsigma/b)\int_0^x f(s)ds$，每个完整模给
$$
 \frac{1+|m|}{b}\int_0^{|x|}
 e^{-\lambda(1+|m|)(|x|-s)}ds\le\frac1{b\lambda}=2^{-12}.
$$
因此 $\mathcal V:\mathcal B^0\to\mathcal B^1$ 的 norm
至多 $2^{-12}$。映射
$W\mapsto W(t_e)+\mathcal V\mathscr F(W)$ 在
$\|W\|_{\mathcal B^1}\le2n_j$ 上是常数至多 $1/64$ 的
严格收缩。其完整解在整个 $|x|\le1,|\operatorname{Im}\theta|\le3$
上满足
$$
 \|(P,K,U,V)\|_{\mathcal A_3}<4n_j.
 \tag{J.8}
$$
所有 Fourier 模同时参与 Banach 收缩，没有有限模余尾待补。
原全标签解在真实径向段满足同一个积分方程和强小球，故由唯一性
就是这一联合解析解的实限制。

由第一行 $\langle P\rangle_t=-(A+1)\langle P\rangle$，高度
相容条件保持。完整 holonomy 恒等式在零 Darboux 源时给
$M_t=0$，所以真 $M=1$ 和它所决定的 $K_0$ 全程保持。
独立高度常数通过 $h_t=a_{\rm phys}wK$ 积分保留。

同一个严格收缩在完整复 $\Gamma$ 盒和上述复标签球统一，故
这一延拓对所有参数联合全纯。这里没有以实径向有限 jets 代替
联合复域，也没有越过只 $C^2$ 的径向接缝。

## 3. 真 inverse labels 及根点可去除的 $z^3$

记
$$
 D=1-w^2(2K+K^2+EP^2),\qquad
 d=E(V-P)/J,\qquad \upsilon=\sqrt D/J.
 \tag{J.9}
$$
由 (J.8)，在上述复域内 $\|d\|,\|\upsilon-1\|<32n_j$。
令 $x=z^2$，并从 $z=0$ 解两个真正的 inverse characteristic
labels：
$$
 (S_\pm)_z+
 \frac{2\varsigma z}{b}
   [-d\pm z\sqrt{B_0(z^2)}\upsilon](S_\pm)_\theta=0,
 \qquad S_\pm(0,\theta)=\theta.
 \tag{J.10}
$$
平方根在0处取1。$S_\pm-\theta$ 是四重周期函数；没有将两支
图作有限 Fourier 投影。

在 $|z|\le3/4,|\operatorname{Im}\theta|\le2$ 上，系数的绝对
值小于 $4/b$，与其径向参考之差及所需角导小于 $2^8n_j/b$。
正向流在宽 $5/2$ 内移动小于 $4/b$；其角 Jacobian 与1之差
小于 $2^9n_j/b$。积分后取真实 inverse，得到
$$
 S_\pm^0=\theta\mp\frac{2\varsigma}{b}
             \int_0^z u^2\sqrt{B_0(u^2)}du,
 \qquad |S_\pm-S_\pm^0|<2^{10}n_j/b.
 \tag{J.11}
$$
这些流和逆由同一复 ODE 的 Picard 收缩构造；上述小位移付清
角复合所需余宽。

准确对称性为 $S_+(-z,\theta)=S_-(z,\theta)$。
两支在 $z=0$ 的一、二阶差为0，故
$$
 T(x,\theta)=\frac{3\varsigma b}{4z^3}(S_--S_+)
 \tag{J.12}
$$
是 $x=z^2$ 的解析函数；$T(0,\theta)=\upsilon_e(\theta)$。
参考值是
$$
 T_0(x)=\frac32\int_0^1 s^{1/2}\sqrt{B_0(sx)}ds.
$$
在 $|z|=3/4$ 使用 (J.11)，再对可去商用最大原则，得到
$$
 |T-T_0|<2^{12}n_j\quad(|x|\le9/16).
 \tag{J.13}
$$
这里的准确因子为 $(3/4)(4/3)^3\cdot2^{11}<2^{12}$；
没有对根点写一个发散的 $1/z^3$ 上界。

取在参考处连续的 $2/3$ 幂，并定义
$$
 R=T^{2/3},\qquad \xi=xR,\qquad
 \phi=\frac{S_++S_-}{2}.
 \tag{J.14}
$$
于是两个真相位准确为
$$
 S_\pm=\phi\mp\frac{2\varsigma}{3b}\xi^{3/2}.
 \tag{J.15}
$$
等式首先在负侧解释，再由 $z$ 解析式定义根点及正侧；
$(\xi,\phi)$ 本身是 $x,\theta$ 的单值解析函数。

## 4. 真 Jacobian、逆域和全部参数

记 $\xi_0=xT_0^{2/3}$、$g_0=(\xi_0)_x$。
在 $|x|\le1/4,|\operatorname{Im}\theta|\le3/2$ 上，
(J.11)--(J.13) 与 Cauchy 给
$$
 |\xi-\xi_0|<2^{13}n_j,\quad
 |\xi_x-g_0|<2^{15}n_j,\quad|\xi_\theta|<2^{14}n_j,
$$
$$
 |\phi-\theta|<2^{10}n_j/b,\quad
 |\phi_x|<2^{12}n_j/b,\quad
 |\phi_\theta-1|<2^{11}n_j/b.
 \tag{J.16}
$$
设
$$
 \mathfrak J=\varsigma\det D_{t,\theta}(\xi,\phi).
$$
它在实域为正，并且
$$
 |\mathfrak J/b-g_0|<2^{17}n_j,\qquad
 3/4<\mathfrak J/b<5/4.
 \tag{J.17}
$$
后一不等式仅在实域使用；复域使用第一式和非零性。

真正的解析逆覆盖
$$
 |\xi|\le1/16,\quad |\operatorname{Im}\phi|\le1,
 \qquad |x|<1/8,\quad|\operatorname{Im}\theta|<5/4.
 \tag{J.18}
$$
具体地，以参考逆 $x_0(\xi)=\xi_0^{-1}(\xi)$ 写
$x=x_0(\xi-(\xi(x,\theta)-\xi_0(x)))$、
$\theta=\phi-(\phi(x,\theta)-\theta)$。由 $|g_0-1|<1/8$，
这个两变量映射把上述小乘积域严格映入自身，导数行和小于
$2^{18}n_j<1/2$。因此它的唯一固定点给实际逆，且
$$
 |x-x_0(\xi)|<2^{14}n_j,\qquad
 |\theta-\phi|<2^{11}n_j/b.
 \tag{J.19}
$$
在根点特别有
$$
 \xi_x=\upsilon_e^{2/3},\quad\xi_\theta=0,\quad
 \phi=\theta,\quad\phi_\theta=1,\quad\phi_t=d_e.
 \tag{J.20}
$$
这些是准确值，不是 $O(n_j)$ 的替代式。

上述全部图、逆和 Jacobian 在完整复参数域统一构造。若
$\|\mathbf a\|\le2^{-10}$、$\|\Gamma\|_\infty\le2^{-16}$，
沿任一满足
$\max(2^{16}\|\dot\Gamma\|_\infty,
2^{10}\|\dot{\mathbf a}\|_{224})\le1$ 的复方向，半径1的
参数盘仍留在已付复域。因此每个显示上界按该盘的上确界乘
$q!$ 就给沿该方向的第 $q$ 阶导数；多方向导数由通常极化
或较小乘积盘得到。不存在一个未付的“只对固定标签”例外。
例如 $\|X\|<16\|\mathbf a\|$ 使该参数盘上
$n_j< N_j/8$。这也给下面完整势差的显式参数导数界。

共同材料坐标中的参考 $\rho$ 只在物理半径中出现。若改为
固定 $a_{\rm phys}$ 微分，必须同时代入
$\dot t=-\dot{\log\rho}$；移动物理根还带
$\dot a_e=a_e\dot{\log\rho}$。本篇不把这两种微分混同。

## 5. 完整 Jacobi 密度及完整 potential

本节使用 raw 高度 Jacobi 场 $h$；它不是 grounded 高度。
其准确散度矩阵及 ordinary Darboux 密度源为
$$
 G=\mu
 \begin{pmatrix}1&-d\\-d&d^2-Q\upsilon^2\end{pmatrix},
 \qquad \mu=\frac{w}{a_{\rm phys}}JD^{-3/2},
 \qquad f=w^2JD^{-3/2}e.
 \tag{J.21}
$$
这与原 ray 篇 (A.7) 的 raw conormal、source 单位完全一致。
设 $\Psi=(\xi,\phi)$。使用正密度 Jacobian $\mathfrak J$，
准确坐标变换是
$$
 G_c=\left[\mathfrak J^{-1}D\Psi\,G(D\Psi)^T\right]
                              \circ\Psi^{-1}.
$$
(J.15) 的两个 covector 都为 null；相减给 $G_c^{\xi\phi}=0$，
相加给 $G_c^{\phi\phi}=-(\xi/b^2)G_c^{\xi\xi}$。
二维 contravariant 密度的行列式不变，故完整准确矩阵为
$$
 \boxed{\quad
 G_c=\alpha\begin{pmatrix}1&0\\0&-\xi/b^2\end{pmatrix},
 \qquad
 \alpha=\left[\frac{b\mu\sqrt Q\upsilon}{\sqrt\xi}\right]
                  \circ\Psi^{-1}
 =\left[b\frac{w}{a_{\rm phys}}D^{-1}
                    \sqrt{B_0/R}\right]\circ\Psi^{-1}.
 \quad}                                                     \tag{J.22}
$$
最后一个式子在整个联合复域解析且非零，包含根点和正侧。
没有用只在 $\xi>0$ 有意义的平方根商来定义该延拓。

令 $\ell=\log\alpha$，$u=\sqrt\alpha\,h\circ\Psi^{-1}$。
完整高度共轭准确为
$$
 \alpha^{-1/2}\operatorname{div}(G_c\nabla(\alpha^{-1/2}u))
    =u_{\xi\xi}-\frac{\xi}{b^2}u_{\phi\phi}+Vu,
$$
$$
 \boxed{\quad
 V=-\frac12\ell_{\xi\xi}-\frac14\ell_\xi^2
       +\frac{\xi}{2b^2}\ell_{\phi\phi}
       +\frac{\xi}{4b^2}\ell_\phi^2.
 \quad}                                                     \tag{J.23}
$$
这里完整二阶密度和全部角导均保留。

径向参考为 $\alpha_0=b\mu_0(x_0)g_0(x_0)$，
$\mu_0=w/a_{\rm phys}$。其 $V_0$ 正是参考篇 (F.11)，
故 $|V_0|<16$，而 $|\partial_\xi\log\alpha_0|<8$。
令 $l=\log(\alpha/\alpha_0)$，在相同 $(\xi,\phi)$ 点比较。
(J.22)、(J.19) 和 $g_0=\sqrt{B_0/T_0^{2/3}}$ 给
$$
 |l|<2^{20}n_j\qquad
 (|\xi|\le1/16,\ |\operatorname{Im}\phi|\le1).
 \tag{J.24}
$$
例如 $\partial_x\log(\mu_0g_0)$ 小于4，故逆图移动项
小于 $2^{16}n_j$；$-\log D$ 小于 $2n_j$，
$-\tfrac12\log(R/T_0^{2/3})$ 小于 $2^{13}n_j$。
这证明的是完整解析函数的上界，不是二阶 Taylor 系数的外推。

在 $|\xi|\le1/32,|\operatorname{Im}\phi|\le1/2$ 上，Cauchy 给
$$
 |l_\xi|<2^{25}n_j,\quad|l_{\xi\xi}|<2^{31}n_j,
 \quad |l_\phi|<2^{21}n_j,\quad|l_{\phi\phi}|<2^{23}n_j.
$$
把它们代入准确差式
$$
 V-V_0=-\tfrac12l_{\xi\xi}
 -\tfrac12(\log\alpha_0)_\xi l_\xi-\tfrac14l_\xi^2
 +\frac{\xi}{2b^2}l_{\phi\phi}
 +\frac{\xi}{4b^2}l_\phi^2
$$
得到
$$
 \boxed{\quad|V-V_0|<2^{32}n_j.\quad}                    \tag{J.25}
$$
参考 $\alpha_0$ 中 $\rho^{-1}$ 是一个径向常数，所以不进入
$V_0$；它仍留在实际高度和 conormal 端口中。

宽 $1/2$ 的 Fourier 尾给完整乘法界
$$
 \|M_{V-V_0}\|_{H^s\to H^s}<2^{52}n_j,
                      \qquad |s|\le4.                   \tag{J.26}
$$
具体使用 $(1+|m|)^s/(1+|n|)^s\le(1+|m-n|)^{|s|}$ 和
$1+2\sum_{k\ge1}(1+4k)^4e^{-2k}<2^{20}$。
mean 和正负全部 Fourier 模都在同一次卷积中。

## 6. 同一个 Sobolev 空间中的实际根 Cauchy 比较

在负侧 $0\le\xi\le1/64$，定义所有 $m\in4\mathbb Z$ 的
真实两行权
$$
 \kappa_m=|m|/b,\qquad
 s_m(\xi)=(1+\kappa_m^{4/3}+\kappa_m^2\xi)^{1/2},
 \qquad
 Y_m=\begin{pmatrix}\sqrt{s_m}\,u_m\\
                      s_m^{-1/2}(u_\xi)_m\end{pmatrix}.
 \tag{J.27}
$$
参考完整两行 Airy 证明在 $\kappa_m\ge1$ 给双向 propagator
$<2^{2182}$。在 $0\le\kappa_m<1$，包括 $m=0$，
这个加权两行 generator 的 norm 小于20，长度为 $1/64$，
故双向 bound 小于2。统一取
$$
 \|\mathcal U_0(\xi,\eta)\|_{H^s\oplus H^s\to H^s\oplus H^s}
                    <K_R:=2^{2184}.
 \tag{J.28}
$$
所有权导数都在这个参考 generator 中，未冻结 $s_m$。

实际相对于参考的唯一 generator 差是完整下左块
$$
 -s^{-1/2}M_{V-V_0}s^{-1/2}.
 \tag{J.29}
$$
两个外侧 Fourier 乘子在同一个 $H^s$ 上均为收缩。
所以 (J.26) 是真正的**同空间算子 norm**；这里没有使用
“小角位移使 pullback 与恒等的同宽 norm 小”这一错误命题。
准确 interaction picture 的积分不超过
$$
 \frac1{64}K_R^2\,2^{52}n_j=2^{4414}n_j.
 \tag{J.30}
$$
当 $n_j\le2^{-4424}$ 时，完整 Volterra 级数在同一空间收敛，
任意两截面的实际相对传播满足
$$
 \boxed{\quad
 \|\mathcal U_0(\eta,\xi)\mathcal U(\xi,\eta)-I\|
          <2^{4420}n_j,\qquad |s|\le4.
 \quad}                                                     \tag{J.31}
$$
Jacobi 方向可以为复；背景此处取真实解。下左卷积把 mean 与
非mean 耦合，未删除任何一条 mean 状态。

由 (J.4)，真实小 $X$ 条件使所有根同时满足本节条件，并给
$$
 \sum_e 2^{4420}n_e
       <2^{164424}\|X\|_{\mathcal X_{224}}
       \le2^{-97720}.
 \tag{J.32}
$$
这只是已定义的实际 root canonical block 误差和；没有把不同
根的物理端口识别费用隐藏进这个求和。

## 7. Ordinary 与弱源的准确完整变换

现在允许完整 raw 方程
$$
 \operatorname{div}(G\nabla h)=f-\operatorname{div}\mathbf F.
 \tag{J.33}
$$
ordinary Darboux 源时 $f$ 必须使用 (J.21)；一般 metric 源
还必须先由真实 tensor-to-scalar 转换产生，不能任选一个 scalar
来代替它。正 Jacobian 的 Piola 公式给
$$
 \widetilde f=(f/\mathfrak J)\circ\Psi^{-1},\qquad
 \widetilde{\mathbf F}=
    (\mathfrak J^{-1}D\Psi\,\mathbf F)\circ\Psi^{-1}.
 \tag{J.34}
$$
高度共轭后，完整两个弱源和 ordinary 修正是
$$
 \mathbf F_c=\alpha^{-1/2}\widetilde{\mathbf F},\qquad
 f_c=\alpha^{-1/2}
       (\widetilde f-\tfrac12\nabla\ell\cdot
                                    \widetilde{\mathbf F}),
$$
$$
 u_{\xi\xi}-\frac\xi{b^2}u_{\phi\phi}+Vu
                  =f_c-\operatorname{div}\mathbf F_c.
 \tag{J.35}
$$
特别第二项的负号来自对 $\alpha^{-1/2}$ 分部积分；不能删除
这个 weak-source 产生的 ordinary height 修正。

以完整 total canonical flux
$\pi=u_\xi+F_c^\xi$ 作第二状态，则
$$
 u_\xi=\pi-F_c^\xi,\qquad
 \pi_\xi=\frac\xi{b^2}u_{\phi\phi}-Vu+f_c-\partial_\phi F_c^\phi.
 \tag{J.36}
$$
因此 (J.27) 的完整源对准确为
$$
 \mathcal E_c=
 \begin{pmatrix}-s^{1/2}F_c^\xi\\
 s^{-1/2}(f_c-\partial_\phi F_c^\phi)\end{pmatrix}.
 \tag{J.37}
$$
在 $L^1_\xi(H^s\oplus H^s)$ 中提供这一实际源对后，(J.28)--
(J.30) 的完整 Duhamel 给实际有源解，费用至多 $2K_R$。
它包括 mean source，且弱源第一分量没有错误地除以 $s^{1/2}$。

本篇**不**从原 $L^2_tH^s_\theta$ 的 norm 单独推出 (J.37)
的 norm：$t=t(\xi,\phi)$ 是混合图，原源没有径向角混合
正则性时，这一步需要真实 producer、对偶能量或另一条固定径向
证明。准确变换已经给出，但它不自行授予一个没有证明的源 norm。

## 8. 两个完整迹、mean、法向负荷与参数微分

在任一 constant $\xi$ 截面，原 raw 高度及向正 $\xi$ 的
conormal 密度准确恢复为
$$
 \widetilde h=\alpha^{-1/2}u,\qquad
 \widetilde p=\sqrt\alpha
                  (u_\xi-\tfrac12\ell_\xi u).
 \tag{J.38}
$$
总物理密度通量再加 $\widetilde F^\xi$。
若 (J.36) 使用 total flux，则恢复 bare $u_\xi$ 需要
$F_c^\xi$ 的真实端点迹。(J.37) 的体源 norm 本身不保证这一
端点迹存在或有界；不能把 weak total-DN 合同升级为 bare
Jacobi/Airy 端口合同。

在真实 root $t=t_e$，(J.20) 给特别简洁而准确的两迹：
$$
 h_e=\alpha_e^{-1/2}u_e,\qquad
 p_e:=\mu(h_t-dh_\theta)|_e
       =\varsigma\sqrt{\alpha_e}
                    (u_\xi-\tfrac12\ell_\xi u)|_e.
 \tag{J.39}
$$
右根的 $\varsigma=-1$ 不能省略。由于此处 $\phi=\theta$，
实际 mean 两行分别为
$$
 \langle h_e\rangle_\theta=\langle\alpha_e^{-1/2}u_e\rangle_\phi,
 \quad
 \langle p_e\rangle_\theta=
 \varsigma\langle\sqrt{\alpha_e}
                     (u_\xi-\tfrac12\ell_\xi u)\rangle_\phi.
 \tag{J.40}
$$
一般 $\alpha_e$ 非径向；物理常高度方向是
$u=\sqrt\alpha\times\text{常数}$，不能用 canonical 的纯零模
代替它。ordinary 源的平均法向负荷在原域仍严格为
$\partial_t\langle p\rangle=\langle f\rangle$；完整
$\dot M_t=w^2\langle JD^{-3/2}e\rangle$ 及其原积分常数保留。
水平重建的周期条件和 raw-to-grounded normal/shear 仍使用原
真实公式；本篇没有把 raw $p_e$ 改名为 grounded 动量。

为明确参数或标签微分没有丢掉图变化，设
$Z=(D\Psi)^{-1}\dot\Psi$，则
$$
 \dot\Psi^{-1}=-Z\circ\Psi^{-1},\qquad
 \dot{\log\mathfrak J}=
                  \operatorname{tr}((D\Psi)^{-1}D\dot\Psi).
 \tag{J.41}
$$
例如 ordinary 源的完整微分为
$$
 \dot{\widetilde f}=
 \left[\frac{\dot f-Z\cdot\nabla f
       -f(\dot{\log\mathfrak J}-Z\cdot\nabla\log\mathfrak J)}
                 {\mathfrak J}\right]\circ\Psi^{-1}.
 \tag{J.42}
$$
weak 源则直接对
$(D\Psi\,\mathbf F/\mathfrak J)\circ\Psi^{-1}$ 微分，保留
$\dot D\Psi$、$\dot{\mathfrak J}$、$\dot{\mathbf F}$ 和
$-Z\cdot\nabla(D\Psi\,\mathbf F/\mathfrak J)$ 四项。
所有端口和 height 乘子同样微分。(J.41)--(J.42) 与第4节
真实复域一起支付图/系数的参数依赖；源本身所需的微分空间
仍由其实际 producer 提供，不凭公式虚授径向导数。

## 9. 得到的算子与下一真实缺口

本篇将一个明确的缺口变成了真正有证明的算子：对实际非零标签
背景，真根内部的完整势差已在固定 $H^s\oplus H^s$ 中付清，
并保全两支、两迹、mean 和所有源变换。根处联合解析性的依据是
实际 quintic 内的 CK 解，而非把全尾仅 $C^2$ 的径向拼接误称
解析。这项比较使用实际相位坐标作为端口预条件。

还需把 constant $\xi=1/64$ 的真实径向图接回保原 $t$ 的
strict density 流，重建新公共度量上的真正联立 KAM、正型完整
两端 DN 和全 mixed 高输入逆。特别主相位的微小变化并没有因此
变成所有 $m$ 上的小相位；全 return 仍要实际共轭或参数选择。
原各向异性 ordinary/weak 源及法向端点迹也须按第7--8节消费。
这些范围不由 (J.32) 自动扩大。

## 10. 可复跑证据

脚本 `scripts/fourfold_actual_joint_analytic_root_20261113.py`
对实际新规范的三个区段端点、CK 代数、完整 characteristic
消因子、两变量逆、density/height/source 恒等式及同空间两行
费用作精确有理和 Arb256 核验。报告为
`notes/2026-11-13-R119-actual-joint-analytic-root-budget.json`。
完整无限模量词来自第2节的全卷积收缩和第6节的有界算子
Volterra 级数，不以有限频率采样代替。
