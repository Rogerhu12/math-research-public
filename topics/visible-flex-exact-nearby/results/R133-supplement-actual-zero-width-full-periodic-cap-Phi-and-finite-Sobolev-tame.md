# R133 续篇：实际零宽全周期帽图、完整 Taylor 核与有限 Sobolev 高度读出

2026-11-15，visible-exact / tail_connector。

**已证明并独立核对。** 本篇从已经实际成立的修补 M32 正帽
不变球，先补齐一般四重周期数据的真实 $B_0$ 端列，再在零角宽
重新构造同一个帽--long 图。由同时平移已知物理背景和已知内数据的
辅助族，逐个多线性张量证明完整 Fourier 核界，随后才作
$\ell^2$ 卷积估计。单个 $A^0$ 算子范数不被直接称为矩阵绝对和。

新图接受低阶小、高有限的非解析 $f_B$。它不需要用原 ac1 的极小
高 Sobolev 邻球覆盖实际约 $3\,10^{-6}$ 的帽校正。
对象仍固定 $\eta_0,\delta=0$、原440866连续修补、
$r\in[9/10,25/8]$ 和同一个真实长段。未知变量始终在物理角
$\theta$ 中，不对未知零宽函数作复角取值或 moving pullback。

## 1. 已成实际门与完整零宽空间

采用
[X：实际全模帽](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)、
[E：加权端点不变球](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md)、
[H：真实小宽高度读出](R133-supplement-small-positive-width-true-cap-to-long-height-readout.md)。
X 所引运行43695160055/1的21门已通过，完整
$q_w<3.561348304031\,10^{-6}<10^{-5}$；这里不重跑旧科学数据。

保留
$$
 \sigma_0=2^{-13},\quad \rho=3\,10^{-6},\quad
 \zeta=9.9\,10^{-10},\quad r_Z=10^{-9},\quad
 r_B=2^{-60},\quad r_f=10^{-8}.
 \tag{F.1}
$$
取整个 $4\mathbb Z$，定义
$$
 \|x\|_{X_0}
 =\sum_m\sup_I|b_m|+\sum_m\sup_I|c_m|,\qquad
 {\cal B}_0=\{x:\|x\|_{X_0}\le\rho,\
                     \|c_{\ne0}(R)\|_{A^0}\le\zeta\}.
 \tag{F.2}
$$
压缩始终使用两个分量的 block-sum 范数，逐个 signed 模的正核及
joint $\ell^1$ 乘法与 E 相同；不在 (F.7) 的反馈常数内插入
$\sqrt2$。只有最后改读标准 Hilbert pair norm时才付等价费用，
该费用已包含在 (F.22)、(F.28) 的宽常数中。
两 mean都在这个空间中。先固定已知非mean内输入
$\gamma\in A_{\sigma_0}^0$、$\|\gamma\|<10^{-9}$，允许一般
四重周期复数据；未知远端非mean高度满足
$$
              f_B\in\dot A_0^2,\qquad \|f_B\|_{\dot A_0^2}<r_B .
 \tag{F.3}
$$
原反射数据将由唯一性识别，而不是用反射删去辅助方向。

由 E 的全部逐 signed 模核、joint卷积和端点评价，
把角权从 $\sigma_0$ 改为0只减小已知费用。
普通源、两个 mean、完整尾和真正的 endpoint 保持式不变。
下节补齐唯一原来由反射设零的右 $B_0$ 输出。

## 2. 当前物理帽上的真实 B mean 补充

使用[全周期 mean 篇](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md)
(B.5)、(B.8)--(B.18) 的准确恒等式，而不转授其旧 $L_0=3/2$
加权帽的数值。当前 unweighted 帽 $[9/10,R]$ 的参考 mean列
另由原全模物理 Green 保留。

长段两端非mean数据在 (F.3) 与 $\|f_*\|_{\dot A^2}<r_f$ 内。
其完整零宽解和 holonomy mean满足
$H<6F,\ F=r_f+r_B<2^{-26}$。
在右端，记 $K$ 含其真正 mean、$V=K_\theta$，则
$$
 B_0^{\rm long}
 =\chi_R\left\langle(V-P)(D^{-1/2}-1)\right\rangle,\qquad
 D=1-w_R^2(2K+K^2+(1+w_R^2)P^2).
 \tag{F.4}
$$
一阶项由 $\langle V-P\rangle=0$ 准确消掉。
原 $w_R^2<2^{-39}$、$\chi_R<1/5$、状态和 $<24F$
及完整二项式级数给
$$
 |B_0^{\rm long}|<q_BF^2<2^{-80},\quad q_B=2^{-28},\qquad
 \|D_ZB_0^{\rm long}\|<2^{-49}.
 \tag{F.5}
$$
独立 $f_B$ 列仍满足
$\|D_{f_B}B_0^{\rm long}\|<2^{-25}F$。
这里 $Z=C_{\ne0}(R)-C_{{\rm ref},\ne0}$。
原线性 $\mathcal L_C^{-1}$ 在零宽仍小于9；
完整非线性高度读出满足 $\|D_Z\Phi\|\le9.013290638<10$。
(F.5) 的 $2^{-49}$ 已使用后者的完整费用。
原 (B.9)--(B.18) 只使用完整 Fourier代数，所有实际 mean都保留。

帽内准确有
$$
             B_0'=-2\beta B_0,\qquad
 B_0(r)=\frac{a(R)^2}{a(r)^2}\,B_0(R).
 \tag{F.6}
$$
全周期篇 §8 对当前 ac1 物理帽保留的原参考 mean $B$ 右端
输入增益为1，连续修补只改变未知 $Q$ 系数而不改变该径向 ODE，且
$a(R)^2/a(r)^2\le1$；它不经过旧加权 $W_0(R)$ 的缩放。
在 E 的映射中增加 (F.6) 的真实右端值。
因此主体球像至多增加 $2^{-80}$，主体 Lipschitz至多增加 $2^{-49}$：
$$
 \|\mathcal T x\|
 <3.23\,10^{-7}+.879\rho+208\rho^2+2^{-80}<.99\rho,
$$
$$
       {\rm Lip}\,\mathcal T<.879+416\rho+2^{-49}<.881.
 \tag{F.7}
$$
这个纯 mean lift 的 $C_{\ne0}(R)$ 分量准确为0。
它通过线性 $Q$ 和二次 $Q$ 产生的后续耦合已经在 E 的
完整未知 $x$ 球中，不能再重复加一次。
故 E 的 $<.9\zeta$ 端点保持式原样成立。

于是 (F.2)--(F.3) 上有唯一完整四重周期解 $W=\widehat W+x$，
包含真实 $B_0,C_0$ 外反馈。共同反射数据时 (F.4) 准确为0，
唯一性将这个解识别为已发布的 X 解，不改变科学背景。

## 3. 零宽高度图与真实端输出

H 的同一个全频 $\mathcal L_C^{-1}$ 加完整非线性反馈在零宽给
$$
 \Phi_\gamma(f_B)=f_*,\qquad
 \|\Phi_\gamma(f_B)\|_{\dot A_0^2}<r_f .
 \tag{F.8}
$$
它与 (F.7) 在同一实际 $Z=Z_0+c_{\ne0}(R)$ 上求值。
$\|Z\|<3\,10^{-13}+\zeta<r_Z$，
所以所有 fixed-point 迭代都在真实 outer定义域中。

这两个统一收缩给 $\Phi_\gamma$ 和 $x$ 关于
$f_B\in\dot A_0^2$ 的 Banach值全纯性。
不同允许角宽上的图由零宽唯一性相同；特别解析输入时等于 H/X 的图。
不是先对未知零宽函数作复角延拓再声称解有高阶正则。

曲率的两个 mean、任意 cut 的完整 $B,C$ traces 均包含在 $x\in X_0$
及已知 $\widehat W$ 中。long 的 mean由准确小根 $\kappa(t)$ 给出。
取 $\kappa_*=2^{-36}$，原 $|\kappa|\le256(6F)^2$ 和
$\int_0^L aw\,dt\le a_Rw_R/2$ 还给
$$
 |\kappa(0)|,|\kappa(L)|<\kappa_*,
 \quad
 \left|\frac{v_0(L)-v_0(0)}{a_Rw_R}\right|<\kappa_* .
 \tag{F.9}
$$
物理 mean slopes 是各端的 $w\kappa$；不能把 $\kappa$ 当作裸 flux。
平均高度跨度不带 $\varepsilon_L$，只使用一个整体 $\lambda$。

一般数据的周期 frame 与位置按原全周期篇 (B.7) 构造：
完整连接的径向角常数沿同一积分保留，四个 quarter 的
$1,i,-1,-i$ 取消水平平移周期。
本篇将该真实规范保作输出；不在每个半径重新设 phase=0。
内帽 $B(L)$、$C_0(L)$、位置/mean-height/phase仍未被指定为 body 的值。

## 4. 只平移已知数据的辅助族

令
$$
                         h=2^{-15}=\sigma_0/4.
 \tag{F.10}
$$
在 $|\Im z|<2h$，只将已知物理中心、其准确已知 residual、
全部非径向已知系数和固定 $\gamma$ 替成
$T_z a(\theta)=a(\theta+z)$。
原 radial reference核、intrinsic数据和端点不变。
已知量原有 $A_{\sigma_0}$ joint界；这些平移量在
$A_{\sigma_0/2}$ 中不超过原界，因此 (F.7) 全部标量门统一成立。
原 $B_0$ 的准确已知 residual为0，角平移保持它为0；
未知 $B_0$ 仍由 (F.4)--(F.6) 求出。

在这个辅助族中，未知输入 $f_B$ 始终是未平移的零宽元素。
不要求 $f_B(\theta+z)$ 对复 $z$ 有意义。
每个已知系数在 $z$ 上全纯，统一压缩给一个全纯族
$\Phi_z,x_z$，对每个零宽输入均有相同值域。

对实 $t$，原物理方程、真 mean小根和唯一性才给协变式
$$
 \Phi_t(T_t f)=T_t\Phi_0(f),\qquad
 x_t(T_t f)=T_t x_0(f).
 \tag{F.11}
$$
这里同时平移中心与 $\gamma$；只平移未知函数而固定背景不是此式。
下节从 (F.11) 推出张量系数的协变，再在已知参数 $z$ 上作
唯一的解析延拓。没有对未知函数作复角 pullback。

## 5. 归一化完整值域及每个多线性张量

令 $D=\partial_\theta$，只在非zero输入上用 $|D|^2$，置
$$
 U=\frac{|D|^2 f_B}{r_B},\qquad
 {\cal V}_z(U)=
 \left(\frac{x_z}{\rho},\
       \frac{|D|^2\Phi_z}{r_f},\
       \frac{Z_z}{r_Z},\
       \frac{\kappa_z(0)}{\kappa_*},\
       \frac{\kappa_z(L)}{\kappa_*},\
       \frac{\Delta v_{0,z}}{a_Rw_R\kappa_*}\right).
 \tag{F.12}
$$
输出空间取所示 joint $A^0$ norm、$X_0$ norm和 scalar绝对值的最大值。
scalar看作 Fourier频率0；$x$ 的两个 mean正常保留。
由 (F.7)--(F.9)，$\|{\cal V}_z(U)\|<1$ 对 $\|U\|_{A^0}<1$ 统一成立。
非mean $\Phi,Z$ 仍按定义投影，未删除其它输出的 mean。

在零输入作完整 Banach Taylor展开
$$
 {\cal V}_z(U)=\sum_{k=0}^{\infty}T_{k,z}[U,\ldots,U].
 \tag{F.13}
$$
$T_k$ 已包括 $1/k!$，是对称连续 $k$ 线性张量。
圆盘 Cauchy 和复极化给
$$
 \|T_{k,z}\|\le k^k/k!\le e^k<4^k\quad(k\ge1),
 \qquad \|T_{0,z}\|<1.
 \tag{F.14}
$$
这一步是完整 multilinear norm，尚未将其当作任意矩阵和。

令 $e_n=e^{in\theta}$，$n\in4\mathbb Z\setminus\{0\}$。
对一个输出分量定义真正系数
$T_k(m;n_1,\ldots,n_k)$；在 $x$ 分量中其绝对值指整个 $r$ 区间
的 supremum。由 (F.11)，对实 $t$，
$$
 T_{k,t}(m;n_1,\ldots,n_k)
 =e^{it(m-\sum n_i)}T_{k,0}(m;n_1,\ldots,n_k).
 \tag{F.15}
$$
两边都是 $z$ 的全纯函数，故这个准确式也在 $|\Im z|<2h$ 成立。
分别代入 $z=ih,-ih$，并对对应的 signed lag半轴求和。
(F.14) 的完整输出 $A^0$ norm于是给
$$
 \boxed{\quad
 \sum_m e^{h|m-\sum n_i|}
       |T_k(m;n_1,\ldots,n_k)|\le2\,4^k .
 \quad}                                                   \tag{F.16}
$$
$k=0$ 同样成立，空输入和为0。
这个列和是从两个实际辅助值域 norm 推出来的，
不是单体 $A^0$ 算子界的无证明升级。

## 6. 完整核到 one-high Hilbert估计

(F.16) 的每项给
$$
 |T_k(m;n_1,\ldots,n_k)|
      \le2\,4^k e^{-h|m-\sum n_i|}.
 \tag{F.17}
$$
因此对任意输入序列，整个多重绝对和被真正卷积
$2\,4^k K_h*|U_1|*\cdots*|U_k|$ 控制，
$K_h(\ell)=e^{-h|\ell|}$。
这允许使用 $\ell^2$ Young，所有输入频率及输出 mean都参加。
不存在把 supremum从径向与 Fourier和之间交换的步骤。

记 $\Lambda_m=(1+m^2)^{1/2}$。对 $q\ge0$，
$$
 \Lambda_{\ell+\sum n_i}^q
 \le(k+1)^q\left(\Lambda_\ell^q+\sum_i\Lambda_{n_i}^q\right).
 \tag{F.18}
$$
将最高权逐项放在恰好一个因子，得到
$$
 \begin{split}
 \|T_k[U_1,\ldots,U_k]\|_{\mathscr H_q}
 \le2\,4^k(k+1)^q\{&
 \|\Lambda^qK_h\|_{\ell^1}\prod_i\|U_i\|_{A^0}\\
 &+\|K_h\|_{\ell^1}
       \sum_i\|U_i\|_{H^q}\prod_{j\ne i}\|U_j\|_{A^0}\}.
 \end{split}
 \tag{F.19}
$$
对于帽分量，
$\mathscr H_q^2=\sum_m\Lambda_m^{2q}\sup_I|x_m|^2$；
它强于 $L^\infty_rH^q_\theta$，而且是本式真正证明的 joint量。
scalar输出用频率0的 norm，端点评价的 norm不超过1。

一个显式全 signed模矩为
$$
 \|\Lambda^qK_h\|_{\ell^1}
 \le2^{q+3}q!\,h^{-q-1},\qquad q\in\mathbb N_0 .
 \tag{F.20}
$$
例如先用
$(1+|m|)^q e^{-h|m|/2}\le e^{h/2}q!(2/h)^q$，
再对剩余指数作完整几何和即可；在频率 $4\mathbb Z$ 上该宽界更强。

取 $\|U\|_{A^0},\|V\|_{A^0}\le1/16$。
于是 $4\|U\|,4\|V\|\le1/4$。
完整 $k$ 和只用
$$
 \sum_{k\ge0}(k+1)^p4^{-k}
        \le p!(4/3)^{p+1}<2^{p+1}p! .
 \tag{F.21}
$$
导数、二次余项和两个输入差至多再添 $k^2$，
可统一把 $p$ 宽成 $q+4$。
对 $q\le8160$，所有阶乘阶数小于8192，使用
$r!\le2^{13r}$、$h^{-1}=2^{15}$ 后，
(F.19)--(F.21) 连同完整固定个数的输出分量远小于
$$
                  C_q=2^{\,96(q+32)+16384}.
 \tag{F.22}
$$
例如最坏两阶乘和指数矩只收
$13q+13(q+4)+15(q+1)+(q+3)+(q+5)$，
再付有限极化/差分/物理四倍角费，仍小于 $64(q+8)+8192$。
没有将整个大常数按卷积因子重复相乘。

## 7. 实际 finite-Sobolev 图、导数与余项

在同一实际零宽值图上，$0\le q\le8160$，
(F.19)--(F.22) 给
$$
 \|{\cal V}_0(U)\|_{\mathscr H_q}
              \le C_q(1+\|U\|_{H^q}),
$$
$$
 \|D{\cal V}_0(U)[H]\|_{\mathscr H_q}
 \le C_q\{\|H\|_{H^q}+(1+\|U\|_{H^q})\|H\|_{A^0}\},
 \tag{F.23}
$$
以及同一个低球内的
$$
 \begin{split}
 \|{\cal V}(U+H)-{\cal V}(U)-D{\cal V}(U)[H]\|_{\mathscr H_q}
 \le C_q\{&
       \|H\|_{A^0}\|H\|_{H^q}\\
       &+(1+\|U\|_{H^q})\|H\|_{A^0}^2\}.
 \end{split}
 \tag{F.24}
$$
一次导数差和两个背景差有相同 one-high结构，分别以
$H^q$ 差或 $A^0$ 差占唯一高因子。
这里高 norm只要求有限，不进入小分母或压缩门。
$A^0$ 低门可由 $\|U\|_{A^0}\le2\|U\|_{H^1}$ 支付；
本篇不声称 $H^0$ 自动嵌入 $A^0$。

从 Fourier截断 $S_NU$ 出发，(F.23) 的差估计给在每个实际
$H^q$ 中的收敛，零宽唯一性识别其极限。
不要求原 uniform径向最高 norm中的有限 Fourier多项式稠密。
由此得到非解析数据的真正有限正则解，而不只是形式的导数估计。

恢复未归一单位，例如
$$
 \|x(f)\|_{\mathscr H_q}
       \le\rho C_q(1+r_B^{-1}\|f\|_{H^{q+2}}),\qquad
 \|\Phi_\gamma(f)\|_{H^{q+2}}
       \le2r_f C_q(1+r_B^{-1}\|f\|_{H^{q+2}}).
 \tag{F.25}
$$
$|D|^2$ 与 $\Lambda^2$ 在非zero $4\mathbb Z$ 上的转换小于2。
所有方向式均按 (F.12) 的实际 $\rho,r_f,r_B,r_Z,\kappa_*$ 读回；
若输入改为物理高度 $s_Bf$，另保 $s_B^{-1}$。
最高所给高度阶是8162，足盖当前网络外调用8144及相应两导，
不提高既有全层输出窗口。

## 8. 低有限 jets 下的真实半阶方向窗

半阶方向不能只从 (F.23) 的 $A^0$ 方向门猜出。
在当前实际背景另要求
$$
 \|U\|_{A^0}\le1/16,\qquad
       \sum_{j=1}^4\|\partial_\theta^jU\|_{A^0}\le1 .
 \tag{F.26}
$$
这只是一项固定低阶条件，足由当前 tail的低1856门支付；
它与高 $H^q$ 小无关。

构造真正的参数多项式
$U^{[4]}(z)=\sum_{j=0}^4z^j\partial_\theta^jU/j!$。
在 $|z|<h$，其零宽 norm小于1/8。
令
$\mathcal A(z)=D{\cal V}_z(U^{[4]}(z))$。
在该圆盘内，完整输入 Cauchy给
$\|\mathcal A(z):A^0\to\mathscr A^0\|<4$。
由实平移协变，$\mathcal A$ 的0--4阶 jets准确是
$\operatorname{ad}_{\partial_\theta}^j D{\cal V}_0(U)$。
这里只比较有限 jets，未假定未知 $U$ 有真正复角值。

所以对每个输出/输入 signed模有
$$
 |(D{\cal V})_{mn}|\le
              2^{70}\Lambda_{m-n}^{-4}.
 \tag{F.27}
$$
其中所有 scalar输出正常取 $m=0$；对 $\Phi$ 的均值只按其定义为0。
这个逐条目界来自真实的有限 commutator算子圆盘，
不是把任意有界矩阵误作绝对可和。

恢复 $f$ 的两个输入导数和 $\Phi$ 的两个输出导数，
半阶权比至多 $2\Lambda_{m-n}^{3/2}$。
完整两向 Schur和收敛：
$\sum_{\ell\in4\mathbb Z}\Lambda_\ell^{-5/2}<4$。
用 $r_f/r_B<2^{34}$、$\rho/r_B<2^{42}$、
$\kappa_*/r_B=2^{24}$，可统一取
$$
 \|D\Phi_\gamma:H^{1/2}_{\ne0}\to H^{1/2}_{\ne0}\|<2^{128},
$$
$$
 \|D_fx:H^{1/2}_{\ne0}\to
                L^\infty_rH^{-3/2}_\theta\|<2^{128}.
 \tag{F.28}
$$
第二式同时控制所有固定真实 cut的全部曲率 traces及其 mean。
(F.9) 的归一 mean slopes和平均高度跨度的方向 functional
也小于同一个 $2^{128}$；读回时仍乘相应 $w$、$a_Rw_R$。
各 Hilbert伴随由同一完整矩阵的反向 Schur得到，
或准确取 dual；不需要假定 $\Phi$ 或 cap传播酉。

## 9. 实际 PDE、端点和外部接口范围

对于 $q$ 足够给两角导的实际输入，(F.23)--(F.25) 得真曲率的有限
角正则，Codazzi等式逐片恢复其所需径向导。
中心的人工 cubic residual与 correction 源准确相消，原真实
target/graft接口保其已给正则，不把 broken高导自动称作全局高导。
Gauss分母仍因 $\|c/\widehat C\|<6\rho$ 可逆。

所有固定 cut 的物理 $B,C$ 与其两个 mean均由同一个解读出。
$C_{\ne0}(L)-\widehat C_{\ne0}(L)=\gamma$ 是输入；
$B(L),C_0(L)$、mean-height、角规范与空间 frame是输出。
在任意 cut重新规定 mean、phase或平移会改变这个图。
原一般物理 mean源/jumps若另给，仍应加入真正两个 mean ODE及其
相应端行；本篇的 homogeneous值图不把它们设为零或改成
$\Pi_A$ 相容 source。

对 long，完整 $C_R$ 逆、$B_0,C_0$ 和 (F.9) 的高度积分保持。
与另一段在同一点对齐一个位置/frame后，原全物理 trace匹配
可继续输运；本篇不据此宣称原 body/waist 已与内端输出相同。
$\nu$ 在帽 intrinsic的直接列为0仍只由真实支集给出，
其内端输入及 far-height变化列不为0。

(F.28) 给的是当前真实零宽帽图的实际物理半阶输入列。
将它送到 far $B$ 端时，必须继续由完整 long 的两端 Green
消费筛选、ordinary/weak 源、true adjoint和 mean-height列；
不能给全部输出统一乘一个 $\varepsilon_L$。
(F.23)--(F.25) 给其 high有限 tame值/导数。
这些是全网络更新外行所需的真实新接口，不改原1734 source损失、
1796背景窗口，也未独自证明全部端口的 onto Schur。

本篇没有把有限 Sobolev $f_B$ 变成解析标签，
也没有假设它在未知 complex角上可评价。
反射存在性子类由完整辅助图的唯一性准确保持；
全4Z辅助方向及其真实两 mean使 Fourier核证明具备合法的输入域。
