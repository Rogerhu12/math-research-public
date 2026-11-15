# R119 续篇：真实非线性普通源、两 Γ 的参考高度 lift 与原源域

2026-11-15，visible-exact / tail_connector。

**状态：解析结论。** 本篇在已证明的同一实际非零尾上，明确把
固定 metric 的非线性 Taylor 余项和两条实际 $\Gamma$ 方向写成
[K 固定径向普通源定理](R119-supplement-fixed-radial-root-sources-and-complete-ordinary-C2-inverse.md)
可读的源。参数方向先保留可显式积分的真实参考高度变化；不把它
误当成一个随标签二次小的 ordinary 源。

对已经给定的原强标签方向，所有无限层 ordinary 源 norm 和
两均值均有界。本篇不从 K 的有限 Sobolev / $C^2$ 输出反推原
$\ell^1_{224}$ 标签，因而不将该输入定理称为非线性 Newton 已闭合。

## 1. 同一个高度、同一个材料截面和原完整方程

固定当前 $\Omega$、$\Gamma$、$\rho$，物理半径
$a_{\rm ph}=\rho r$、$t=\log r$。令 $z=z_{\rm ref}+u$ 为原正向
高度，$(z_{\rm ref})_t=a_{\rm ph}w$；北面采用的整体高度号在最终
原几何映射中照旧。记
$$
 P={z_\theta\over a_{\rm ph}w},\qquad
 K={z_t\over a_{\rm ph}w}-1,\qquad
 U=P_\theta,\quad V=K_\theta,\quad q=w^2,\quad E=1+q,
$$
$$
 A=(\log w)_t,\qquad
 J=1+K+EU,\qquad
 T=2K+U+K^2+KU+qP^2,\qquad
 \mathcal F={-AT+E(V-P)^2\over J}.
 \tag{Q.1}
$$
这里 $q=w^2$ 不表示 strict 区的 $\sqrt Q$，$K$ 是相对高度态。
原准确全频方程为
$$
 P_t=V-(A+1)P,\qquad K_t=\mathcal F(A,q;P,K,U,V).
 \tag{Q.2}
$$
它就是 [实际末端延拓](R119-actual-final-connector-all-label-continuation.md)
119.7--119.10 和原联合根 J.5。平均 $K_0$ 是真正 holonomy
方程的均值；本篇没有把它设成零。

对固定 metric 的物理高度方向 $h$ 定义
$$
 p={h_\theta\over a_{\rm ph}w},\qquad
 k={h_t\over a_{\rm ph}w},\qquad
 Y=(p,k,p_\theta,k_\theta),\quad W=(P,K,U,V).
 \tag{Q.3}
$$
其第一行恒有 $p_t=k_\theta-(A+1)p$，不带一个另造的源。
因此
$$
 k_t-D_W\mathcal F[Y]=e
 \quad\Longleftrightarrow\quad
 \operatorname{div}(G\nabla h)
           =w^2JD^{-3/2}e,\qquad
 D=1-q(2K+K^2+EP^2).
 \tag{Q.4}
$$
这是原 strict S.5 / hodograph H.13 的同一个 scalar source 单位。
右侧是 ordinary 密度，不是将两分量 weak 源微分后重新命名。
K.29 的原 source 正是
$$
 N={\mu_jp_*^2\over12r^{10}}e,\qquad
 \mu_j=\varepsilon_s m_j,\qquad
 w={\mu_jp_*\over r^7}.
 \tag{Q.5}
$$
所有公式在固定 $t$ 评价；不先把未知 $e$ 拉到混合根图。

## 2. 固定 metric 的完整 Taylor 源

将 (Q.1) 的分子记为 $\mathcal N$。$J$ 对四态仿射，
$\mathcal N$ 对四态次数至多2。令
$$
 j_Y=k+E p_\theta,\qquad
 \mathcal N_2[Y]
 =-A(k^2+k p_\theta+q p^2)+E(k_\theta-p)^2 .
$$
准确 Taylor 余项为
$$
 \boxed{\quad
 \mathcal E_W(Y):=
 \mathcal F(W+Y)-\mathcal F(W)-D\mathcal F(W)Y
 ={\,\mathcal N_2[Y]-j_YD\mathcal F(W)Y\,\over J+j_Y}.
 \quad} \tag{Q.6}
$$
证明只需用
$D\mathcal N[Y]=J\,D\mathcal F[Y]+\mathcal F j_Y$ 展开分子。
所以 (Q.6) 保留所有 mixed 二次项和微分分母的项，
包括其零 Fourier 系数。

若当前残差为 $r=K_t-\mathcal F(W)$，对原物理高度加 $h$ 后，
$$
 r_{\rm new}=r+\{k_t-D\mathcal F(W)Y\}-\mathcal E_W(Y).
 \tag{Q.7}
$$
这固定了用于 Newton 的源号。若所消费的线性方程右边是 $-r$，
新残差是 $-\mathcal E_W(Y)$。本节只识别它为真正普通源，
没有把它的平均或通量兼容量强行清零。

明确约定 $\|f\|_{\mathcal A_s}=\sum_{m\in4\mathbb Z}
 e^{s|m|}|f_m|$，向量取分量和；$s$ 是角解析宽度，不是导数阶数。
在 $\|W\|_{\mathcal A_4},\|Y\|_{\mathcal A_4}<2^{-16}$、
$|q|<1$ 的实际球内，$J$、$J+j_Y$ 的 inverse norm均小于2。
逐项商法则给
$$
 \|D\mathcal F(W)Y\|_{\mathcal A_2}
       <2^7(1+|A|)\|Y\|_{\mathcal A_4},\qquad
 \|\mathcal E_W(Y)\|_{\mathcal A_2}
       <2^{12}(1+|A|)\|Y\|_{\mathcal A_4}^2 .
 \tag{Q.8}
$$
例如 $\|\mathcal N_2\|\le8(1+|A|)\|Y\|^2$、
$\|j_Y\|\le2\|Y\|$ 已足；这里宽4到2只留余量，
没有角向 Fourier 截断。

## 3. 原逐层权确实消费这些普通源

保持 [控制 profile 全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.2、C.24、C.32 的全部分段规范，写
$$
 C_j=2^{200}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},
 \quad C_j^\#=C_j+\mathbf1_{j\ge130}C_{j-1},
 \quad J_j=j+5,\quad
 K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}.
 \tag{Q.9}
$$
它就是原 $N_j^c$，换字母仅为避免和 ordinary $N$ 混淆。
两处全局因子 $\delta_{4096}^{-3/2}$、
$\delta_{8192}^{-485/4}$ 不变。原完整预算为
$$
 \sum_{j\ge129}(K_j^{\rm ref})^2C_j<2^{160016}.
 \tag{Q.10}
$$
设一个实际方向在整胞上的四态满足
$$
 \|Y\|_{\mathcal A_4(I_j)}\le4C_j^\#\,Y_*,
 \tag{Q.11}
$$
并处于 (Q.8) 的真实球。对原强图的方向，这就是原局部 C.23、
全图 C.31 的完整状态控制；使用 (Q.11) 时必须给出那个实际方向，
不由有限 Sobolev 结论自动授予它。

全 profile 原界给
$$
 |p_*|\le2^{128}\delta_j^{-1},\quad
 1+|A|\le2^{13}J_j\delta_j^{-3/2},\quad
 h_j^{-5}\le2^{18}\delta_j^{-5/256},\quad
 C_j^\#<2^{128}C_j .
 \tag{Q.12}
$$
最后一式逐个分段读取：$C_j$ 的浅段幂为 $7/4$；
4096以后的中段为 $13/4-5/256$；
8192以后的深段为 $249/2-5/256$，两处连续规范保留，
所以相邻比均小于 $2^{127}$。不把不同行的 $C_j$ 当作常数。

对任何完整 $\mathcal A_2$ 函数，
$\|f\|_{H^{1026}}\le2^{16384}\|f\|_{\mathcal A_2}$。
将 (Q.8)、(Q.11)--(Q.12) 代入 K.29，得
$$
 {\delta_j^4\over\zeta_j}
 \left\|{\mu_jp_*^2\over12r^{10}}\mathcal E_W(Y)\right\|_{H^{1026}}
 <2^{17128}J_jh_j^{-5}\delta_j^{-3/2}C_j\,Y_*^2.
 \tag{Q.13}
$$
其中一次 $C_j$ 用 (Q.9) 消掉 $\mu_j/\zeta_j$，
另一次保留为实际的逐层小量；两个 $C_j^\#$ 的邻胞费均已支付。
由
$J_jh_j^{-5}\delta_j^{-3/2}<2^{18}(K_j^{\rm ref})^2$
和 (Q.10)，得到完整普通源门
$$
 \boxed{\qquad
      \mathcal S_t[\mathcal E_W(Y)]<2^{200000}Y_*^2 .
 \qquad} \tag{Q.14}
$$
全 $129$--$8192$ 前缀与无限深尾都包含在 (Q.10) 中。
所有 Fourier 模及 source mean 均包含；没有 $\sup\sum$ 与
$\sum\sup$ 的交换。

因此，对原强图中已经给定的真实方向，非线性余项可以直接进入
K 的 fixed-$t$ ordinary source 定理。所需角阶由已给的宽2提供，
不要求 $1026$ 阶径向导数；源的径向连续性来自原 profile
$C^2$ 和该实际方向的完整二 jet。

## 4. 两 Γ 的 metric 方向：先区分总高度与相对态

现在固定材料半径和 $\rho$，只改变原两个径向 bump。
记
$$
 \psi=\dot{\log w}=\dot{\log p_*},\qquad
 \dot A=\psi_t,\qquad \dot q=2q\psi .
 \tag{Q.15}
$$
这一步固定 $\Omega$，故两 bump 的支集端点不移动。
若 $h=\dot z$ 是**总物理高度**的变分，而 $Y$ 仍按 (Q.3) 定义，
准确有
$$
 \dot P=p-\psi P,\quad
 \dot K=k-\psi(1+K),\quad
 \dot U=p_\theta-\psi U,\quad
 \dot V=k_\theta-\psi V .
 \tag{Q.16}
$$
$\dot K$ 的 $1$ 不能删。直接微分 (Q.2)，第一行仍为 (Q.3) 的
无源运动学式，第二行给完整 ordinary metric 源
$$
 \boxed{\quad
 e_\psi=(1+K+\mathcal F_A)\psi_t+
  \{\mathcal F-D\mathcal F[W+(0,1,0,0)]+2q\mathcal F_q\}\psi .
 \quad} \tag{Q.17}
$$
这是非零背景的完整公式，不是把径向 C.50 的 $\delta G$
直接代入实际 Jacobi 系数。

此式还可以完全化简。设 $L=1+K$、$b=V-P$，则
$J=L+EU$、
$\mathcal N=-A(L^2-1+LU+qP^2)+Eb^2$。
在 $(L,P,U,V)$ 的准确 Euler 方向上，
$D\mathcal N=2(\mathcal N-A)$、$DJ=J$。
因此
$$
 \mathcal F-D\mathcal F[W+(0,1,0,0)]={2A\over J},\qquad
 \mathcal F_q={b^2-AP^2-\mathcal F U\over J},
$$
$$
 e_\psi=
 {1+q(LU-P^2)\over J}\,\psi_t
 +{2\{A+q(b^2-AP^2-\mathcal F U)\}\over J}\,\psi .
 \tag{Q.18}
$$
在径向零标签处它正是 $e_\psi=\psi_t+2A\psi$，
并不随标签趋零。若直接把这一项当作 $O(\|X\|\dot\Gamma)$，
会漏掉实际参考高度变化。

## 5. 准确参考高度 lift 及剩余小普通源

定义一个已知径向高度，固定平端常数为0：
$$
 (h_\psi)_t=a_{\rm ph}w\psi,\qquad
 h_\psi(t)=\int_{t_f}^t a_{\rm ph}(s)w(s)\psi(s)\,ds .
 \tag{Q.19}
$$
此有向积分按实际平端 $t_f$ 读取。其相对 Jacobi 四态为
$(0,\psi,0,0)$，所以在当前实际背景上
$$
 e_{\rm lift}=\psi_t-\mathcal F_K\psi,\qquad
 h=h_\psi+\widetilde h,\qquad
 \boxed{\quad
 e_{\rm rem}=(K+\mathcal F_A)\psi_t+
       \{\mathcal F-D\mathcal F[W]+2q\mathcal F_q\}\psi .
 \quad} \tag{Q.20}
$$
完整恒等式是 $e_\psi=e_{\rm lift}+e_{\rm rem}$。

这里 $\mathcal F_A=-T/J$，故
$\|K+\mathcal F_A\|_{\mathcal A_2}<16\|W\|_{\mathcal A_4}$。
由原准确式 119.10，
$\mathcal F+A(2K+U)$ 从二次开始，且其分母仍是 $J$；
$\mathcal F_q$ 也从二次开始。逐项微分得
$$
 \|e_{\rm rem}\|_{\mathcal A_2}
 <2^{12}\left\{\|W\|_{\mathcal A_4}|\psi_t|
        +(1+|A|)\|W\|_{\mathcal A_4}^2|\psi|\right\}.
 \tag{Q.21}
$$
所以 $\psi_t$ 项确为一次背景小量，$\psi$ 项为二次背景小量。
本式是完整 scalar ordinary 源，mean不删。

原两 bump 为
$\psi_1=64z_1^3(1-z_1)^3$、
$\psi_2=64z_2^3(1-z_2)^3$，分别采用
$z_1=8(x-1/4)$、$z_2=32(x-3/16)$。
[双参数重建](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
U.1、U.5 给 $|\psi_s|\le1$、$|\partial_x\psi_s|\le384$；
$dt=(\eta_j/\sqrt{12})dx$、
$\eta_j=\delta_j^{3/2}/(4\sqrt2)$。
若 $g_j$ 是该胞及必要邻胞所有实际 $\dot\gamma_1,\dot\gamma_2$
绝对值之和，则
$$
 |\psi|\le g_j,\qquad
 |\psi_t|<2^{13}\delta_j^{-3/2}g_j .
 \tag{Q.22}
$$
两支集的端点0、1、2阶 jet 准确为零，所以这些已知项不在
真实 cell/root 接口产生值跳或新的 Dirac。

取当前 $\|W\|_{\mathcal A_4(I_j)}\le4C_j^\#\mathcal X$。
由 (Q.10) 的 $K_j^{\rm ref}>1$ 得 $4C_j^\#\mathcal X
 <2^{160019}\mathcal X<1$；真实球更满足 (Q.8)。
这允许下式将 (Q.21) 的第二项保守吸收入一次背景小量。
用 (Q.5)、(Q.12)、(Q.21)--(Q.22)，保守得到
$$
 \mathcal S_t[e_{\rm rem}]
 \le2^{18000}\mathcal X\,\mathfrak M(\dot\Gamma),\qquad
 \mathfrak M(\dot\Gamma)=
       \sup_{j\ge129}J_jh_j^{-5}\delta_j^{-3/2}g_j .
 \tag{Q.23}
$$
这是真实 metric 方向所需的明确条件。任意无层衰减的
$\ell^\infty$ 参数方向不自动满足它。

参考 lift 的高度与通量同样保留：
$$
 \pi_\psi=\mu(h_\psi)_t=w^2JD^{-3/2}\psi,\qquad
 h_\psi(t_2)-h_\psi(t_1)=\int_{t_1}^{t_2}a_{\rm ph}w\psi\,dt .
 \tag{Q.24}
$$
在 bump 支集外 $\pi_\psi=0$，但 $h_\psi$ 一般是一个非零常数。
各真实端点的这些高度、原单位常数列和外 trace必须进入已有
有序 source 合同；不能在每个胞元各重置一次高度常数。

即使 $g_j$ 仅有界，原 $|w|<2^{129}\mu_j\delta_j^{-1}$、
$|A|<2^{13}J_j\delta_j^{-3/2}$ 与 (Q.22) 给
$|(h_\psi)_t|\le C\mu_j\delta_j^{-1}g_j$、
$|(h_\psi)_{tt}|\le C J_j\mu_j\delta_j^{-5/2}g_j$，
其中 $C$ 含实际固定 $\rho$ 和原 $r\le2$。
深处 $\mu_j=\varepsilon_s\delta_{4096}^{3/2}\delta_j^{9/2}$
使上述二 jet 都趋0，且 (Q.19) 绝对收敛。
所以这个 lift 是显式可重建的真实 $C^2$ 参考几何变化，
不是一个未知普通源 inverse。

### 固定材料坐标中的整体尺度

若另有一个真实整体 homothety $\dot\rho/\rho=\kappa$，并仍使用
相同材料 $r$，则 $\dot a_{\rm ph}/a_{\rm ph}=\kappa$。
$\dot w$ 由 (Q.15) 另计，不能把这一尺度错塞进 $\psi$。
在 (Q.16) 中，分母 $a_{\rm ph}w$ 的相对变化变为
$\kappa+\psi$。因为 $\kappa_t=0$，第一行仍无源，第二行只增加
$$
 e_\rho={2\kappa A\over J},\qquad
 h_\rho=\kappa z,\qquad
 (k_\rho)_t-D\mathcal F[Y_\rho]={2\kappa A\over J}.
 \tag{Q.24a}
$$
最后等号由 $Y_\rho=\kappa(P,1+K,U,V)$ 和
$K_t=\mathcal F$ 直接给出。这是同一真实高度的显式 homothety
方向，包含其非mean分量，不是用径向参考代替非径向 $z$。
其高度、total flux 与所有真实物理端点的尺度导数一并保留。

若改变的是参考斜率的全局乘数 $\varepsilon_s$ 而材料尺度不动，
则 $\psi=\dot\varepsilon_s/\varepsilon_s$ 为常数。
(Q.20) 的 $\psi_t$ 项准确为0，(Q.21) 及同一个 (Q.13) 预算给
$$
 \mathcal S_t[e_{\rm rem}]<
       2^{200000}\mathcal X^2
                   |\dot\varepsilon_s/\varepsilon_s|.
 \tag{Q.24b}
$$
参考 lift仍为 (Q.19)。以上只覆盖实际整体尺度，不涵盖随 $t$
变化的任意材料重参数化；移动切口的真实端项仍按原几何合同处理。

## 6. 真联合 Γ*(a) 方向满足显示的逐层门

使用 [真实双相位联立](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
N.1、N.8--N.15，以及
[新增外行的同一次联合选择](R119-supplement-new-outer-joint-two-phase-scalar-normal-form-and-high-feedback.md)
J.1、J.11--J.18 和新外同表示 Y.7。
须先支付 Y.7 的真实六项邻胞和。其原定义是
[完整负窗 P.3](R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md)：
$$
 \mathcal N_{i|j}
   =\sum_{k=j-1}^{j+1}(C_k+C_{k-1})
   =C_{j+1}+2C_j+2C_{j-1}+C_{j-2},
$$
$$
 \mathcal N_{i|j}<2^{132}C_j^\# . \tag{Q.24c}
$$
不实际存在的浅端项按原枚举省去。
(Q.12) 给后向相邻比 $<2^{127}$；
前向比除4097的 $h$ 切换外小于1，而该切换
$(h_{4096}/h_{4097})^5<2^{50}$，
故前向比统一小于 $2^{64}$。逐项代入即得 (Q.24c)。
这里没有把六项和直接改名为单层 $C_j^\#$。

固定已经选定的 $\Omega$，
$\Gamma^*(0,\Omega)=\bar\Gamma(\Omega)$；整个复标签球
$\|a\|_{224}<A_*=2^{-262148}$ 上，该完整联合解全纯且逐行满足
$$
 |\Gamma_i^*(a)-\bar\Gamma_i|
 <2^{340}J_j^4\delta_j^{-6}C_j^\#\|a\|_{224}.
 \tag{Q.25}
$$
这保持所有其它行的联合反馈；不是只对一个孤立坡微分。
当前 $\mathcal X\le2^{-8388608}$ 严格在该球的四分之一以内。
在半径 $A_*/2$ 的真实复方向盘上 Cauchy，连同胞元内两坡、
两参数及至多一个邻胞的有限计数（另付邻胞 $2^{128}$），可取
$$
 g_j\le2^{480}J_j^4\delta_j^{-6}C_j^\#
                                      \|\dot a\|_{224}.
 \tag{Q.26}
$$
这里 Cauchy 的真实 $A_*^{-1}$ 已由 (Q.25) 的 $A_*$ 抵消，
没有把原盘半径当成1，也没有逐列求导漏掉联合 $\ell^\infty$ 方向。

由 (Q.10)、(Q.12)，
$$
 \mathfrak M(D_a\Gamma^*[\dot a])
 <2^{160768}\|\dot a\|_{224}.
$$
例如待控制的逐层量是
$2^{480+128}J_j^5h_j^{-5}\delta_j^{-15/2}C_j$，
而 $J_j^5h_j^{-5}\delta_j^{-15/2}
 <2^{18}(K_j^{\rm ref})^2$ 对全部 $j\ge129$ 成立。
所以完整两 $\Gamma^*$ 的实际小 remainder 确满足
$$
 \boxed{\quad
 \mathcal S_t[e_{\rm rem}(D_a\Gamma^*[\dot a])]
       <2^{200000}\mathcal X\|\dot a\|_{224}.
 \quad} \tag{Q.27}
$$
所有根 germ 内 $\psi=0$，所以额外 metric ordinary 源在根内准确为0；
源在原 fixed-$t$ 支集处理，根端只接真正齐次端口。
(Q.27) 加上 (Q.19)、(Q.24) 的已知参考列，才是完整参数方向。

新增有限外两参数仍按 F/J/C 的真正有限几何和 source 合同进入
$\mathcal G_{\rm ext}$。本篇不把有限外编号冒作某个深层 $j$，
也不把其固定 stop、$\delta\rho$、移动材料切口或
$\delta(a_Bw_B)$ 置零。若改变 $\Omega$ 的坡平移，或作非恒定材料重参数化，须另外使用原 C.37、C.49--C.51 的实际
几何导数；整体 $\rho$ 只按 (Q.24a) 的准确 homothety 处理，
不能继续原样使用固定 $a_{\rm ph}$ 的 (Q.15)。

## 7. 源域已付的范围及非线性闭合仍需的一个实际输入

(Q.6)、(Q.17)--(Q.20) 均是完整 mean 在内的恒等式。
在反射成员，$P,V$ 奇、$K,U$ 偶，$Y$ 同类，径向 $\psi$ 不变，
因此这几个 scalar ordinary 源都为偶。它们合法进入刚付的
实际反射帽--尾原方程接口，但其 total-flux 兼容量、holonomy
线性残差和唯一辅助荷仍须沿原 Z/K 联立，不能由“偶”推成零。

固定 metric 的 (Q.14) 和选定 $\Gamma^*$ 的 (Q.27)
解决的是**给定真实强方向时** ordinary 源属于 K 输入域的问题。
当 intrinsic $\nu$ 或其它控制只在有限主体/connector支集改变时，
其在无限 R119 胞元的源准确为0；有限体源、边界 mean和实际
归一化项仍由各自已有消费者负责。本篇不将这样的有限支集声明
转授给一个同时改变无限参考 profile 的尺度参数。

非线性迭代还有明确的一步：K 的解须进入能够重用 (Q.11) 的
真实状态邻域，或另建在有限光滑邻域中统一成立的 tame inverse。
现有 $H^{1024}$ 与逐胞物理 $C^2$ 界本身不蕴含 (Q.11)。
并且 (Q.6) 含 $p_\theta,k_\theta$ 的二次积，
其 $H^{1026}$ source norm不能仅从一个 $C^2$ norm推出。
本篇没有把已经给定的强方向假设偷偷换成新 inverse 的结论。

因此，目前两 $\Gamma$ 的普通源及已知参考几何列已经明确分离并
支付；原解析标签输出、或实际可迭代的有限光滑状态域仍是后继门。
最终公共 metric 必须先选定再固定，不能用参数方向恒等式把一条
变动 metric 的路径称为同一 metric 上的等距弯曲族。

全部新增结论由上述准确公式和已经发布的原预算推出；
没有新增数学实验、浮点假设或旧 native 重算。
