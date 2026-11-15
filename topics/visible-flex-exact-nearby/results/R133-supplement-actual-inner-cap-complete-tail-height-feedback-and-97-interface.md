# R133：实际帽内输入经完整尾部返回的低阶列与原97接口

2026-11-15，visible-exact-astra-0df9。

**已证明的解析结论；root全文及独立原式核对。** 在[O实际两输入cap--long图](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md)
的明确O21域内，将独立帽内曲率输入先化为真正的物理B源，再经过
[D完整尾部逆和双向端口](R119-supplement-actual-outer-row-to-complete-mixed-weighted-Schur.md)，
得到新的实际低阶列
$$
 \|\mathcal F_\gamma:H^0_\perp\longrightarrow H^2_\perp\|
                           <2^{-52000000}.
 \tag{R.1}
$$
这里输出是归一化B非mean高度，原物理$s_B$在两个正确位置相消。
独立mean斜率、帽内Cmean和未screen的height span没有被删掉。

本篇固定所有背景和metric参数，使用完整、相容的tail Jacobi
proxy。它不是整个Darboux reduced derivative的逆，
没有把第一参数反馈、$\mathcal E_N$、$H_p$或独立设计源设零。
将这些列加入完整增广问题仍按它们自己的合同处理。

## 1. 同一个实际对象和所有输入单位

使用O的真实
$\Phi_\gamma(f_B)$、$\mathscr K_\gamma(f_B)$、$\mu_L,d_L$
和同一short背景$\mu_T,d_T$。当前背景满足O21，特别
$$
 \epsilon=e^{-7L/4}<2^{-57000000},\qquad
 C_{64}^{\rm act}=2^{299008},\qquad
 \mathcal D_{64}<2^{1048577}.
 \tag{R.2}
$$
最后一式由
$\mathcal D_{64}=1+g_{64}+2^{60}f_{64}+64n_{64}$、
$g_{64}\le g_{1824}\le2^{1048576}$ 和O21的真实小state界得到。
这不将高范数仅有限误读为小，也不要求gamma的未知复角值。

$\dot\gamma$ 是原帽内非mean物理C曲率方向，不是$\dot f_*$
或physical高度。实际帽的低A0输入域和O21的高输入门是背景
条件；先对光滑$\dot\gamma$构造下面的线性列，再连续延拓到H0。
这不是对任意distribution数据的非线性存在结论。

本篇的尾部列使用同一个固定metric下的完整Jacobi proxy：
所有high、deep、canonical mean和真实物理height gauge都保留。
其$B$边界行是
$\mathcal T_1=\mathcal N_B-\mathcal E_B$，已经包含
$D_f\Phi_\gamma(f_B)$。与它组成的$\mathcal F_\gamma$不再额外
插入一次相同的$f_B\mapsto f_*$反馈。

## 2. 先核outward列与正t总通量的符号

原[长段mean商](R119-supplement-actual-long-mean-quotient-and-unmatched-exterior-return.md)
R.2、R.7与R.24规定
$$
 \pi_L=\mu_L(H_t-d_LH_\theta)+F_L^t,\qquad
 \text{left outward conormal}=-\pi_L(B).
 \tag{R.3}
$$
所以O25的列
$$
 b_\gamma=-\mu_Ls_B
       D_g\mathcal K(f_B,\Phi_\gamma(f_B))
                  D_\gamma\Phi_\gamma(f_B)\dot\gamma
 \tag{R.4}
$$
是left outward列；正t通量的独立列是$-b_\gamma$。

为单独读取这个方向，令其余独立body、weak、jump、metric和mean
输入为0。这个列的准确short-side affine源及mean斜率输出是
$$
 \boxed{\quad
 \beta_\gamma=-P_{\mu_T}(r_\mu b_\gamma),\qquad
 c_{B,\gamma}=
       {\langle r_\mu b_\gamma\rangle\over\langle\mu_T\rangle},
 \qquad r_\mu=\mu_T/\mu_L .
 \quad} \tag{R.5}
$$
它直接来自原R.21--26和P.27--28的
$\pi_{\rm tmp}=-r_\mu b_\gamma$、$q_T=0$。
不是将outward DN与正t的$\pi_L$混名后猜测符号。
独立$c_{B,\gamma}$使用raw高度径导单位；若写成normalized K，
须除以$s_B$。

O20完整holonomy微分给$\langle b_\gamma\rangle=0$。
但$r_\mu$一般非常数，所以
$\langle r_\mu b_\gamma\rangle$并非预先为零。
(R.5)保留实际rank-one输出及$c_{B,\gamma}$；只在真正匹配、
$r_\mu=1$时，该单独mean差才随完整holonomy恒等式消去。

## 3. 原低阶窗口、完整转换和相容性

O26的低窗及真正adjoint给
$H^{q-1/2}_\perp\to H^{q+1/2}$，$0\le q\le64$，
常数$C_{64}^{\rm act}s_B\epsilon\mathcal D_{64}$。
在整数相邻窗之间使用同一Hilbert插值，取$q=1/2$：
$$
 \|b_\gamma\|_{H^1}
 \le C_{64}^{\rm act}s_B\epsilon\mathcal D_{64}
                                      \|\dot\gamma\|_{H^0}.
 \tag{R.6}
$$
输入和输出均是完整$4\mathbb Z$空间，没有有限97物理cutoff；
gamma本身非mean是其定义，非预先删除输出mean。

在O21的同一个低域，真实$\mu_L,\mu_T$均接近
$\mu_0\in(1/6,1/4)$，其低阶商及
$\langle\mu_T\rangle^{-1}$有严格下界。
O的系数估计、完整H1乘法与K20的rank-one读取，给安全宽界
$$
 \|\beta_\gamma\|_{H^1}+|c_{B,\gamma}|
                        \le2^{131072}\|b_\gamma\|_{H^1}.
 \tag{R.7}
$$
这个固定低费可以直接由$H^2$系数范数证明：
$r_\mu-1$及$\mu_T/\langle\mu_T\rangle-1$的完整低范数，
由O21、O15乘真实small budget而仍小于1；
$H^1$乘法只需这些完整$H^2$范数和固定Fourier包含常数。
scalar分母大于$1/12$。因此(R.7)余量包含两个乘法、
一个mean functional和完整rank-one输出，并不含$s_B^{-1}$。
这里没有将最大单列和冒作Hilbert算子norm。

由(R.5)，$\langle\beta_\gamma\rangle=0$准确成立。
在只有该物理B源、其余独立源均为0的通道中，原完整Green恒等式
把closed-tail的total-flux兼容性写成这一个物理总荷。
因而本列属于D27的相容源域。选一次整体height gauge后即可
使用其真实完整inverse，不需加入辅助不相容荷。

如果另外给定$q_A,\int g_0,F_L^t,F_T^t,b_\perp$、独立metric
或$\Gamma/H_p$列，则必须先按K20/P27--28完整叠加它们，
再核总physical兼容性。不能把本单列的零总荷用于清除那些输入。
在canonical wave表示中的两个mean也仍由真实source嵌入保留。

## 4. 全tail反向读出，物理单位只抵消一次

D27以$q=3/2$给完整相容tail响应
$$
 \|\mathcal T_{B,\rm tail}\beta\|_{H^2_\perp}
       <{2^{3100000}\over s_B}\|\beta\|_{H^1}.
 \tag{R.8}
$$
这里的$f_B$是归一化非mean高度；fixed physical B角、全部finite
connector、high/deep恢复、两canonical mean及唯一height规范均在
同一映射中。只有局部screening而没有(R.8)不能得到下式。

定义
$$
 \mathcal F_\gamma\dot\gamma=
            \mathcal T_{B,\rm tail}\beta_\gamma .
 \tag{R.9}
$$
由(R.2)、(R.6)--(R.8)，准确$s_B^{-1}s_B$相消后有
$$
 \|\mathcal F_\gamma\|
 <2^{3100000+131072+299008+1048577}\epsilon
 <2^{-52421343}<2^{-52000000}.
 \tag{R.10}
$$
没有用浮点下溢的0代替这个严格正上界。
原D27已经解过包含$D_f\Phi$的真实边界行，
所以(R.9)没有第二个未付分母或重复的相同反馈。

## 5. 实际帽内B/Cmean读出的新增列

记[I完整actual帽Poisson](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md)
的$\mathcal K_*$为固定$f_B$的inner gamma响应，
$\mathcal L_*$为独立normalized height响应。
它们用同一真实cap状态和完整Hilbert径向module；
$\mathcal L_*:\dot H^2_\perp\to\mathfrak M_\Sigma$的norm小于$1/25$。

在I的原反射sector中，完整固定参数cap响应接上(R.9)后是
$$
 \mathcal K_{\rm right}^{\rm proxy}
       =\mathcal K_*+\mathcal L_*\mathcal F_\gamma .
 \tag{R.11}
$$
两个项先在同一物理pair中相加；它们同时给inner B和独立Cmean。
由(R.1)及$I$的endpoint-evaluation模块，
$$
 \|\mathcal K_{\rm right}^{\rm proxy}-\mathcal K_*\|
             _{H^0_{\rm e,\perp}\to\mathfrak M_\Sigma}
                           <2^{-52000000}.
 \tag{R.12}
$$
特别同一上界控制两个inner输出差的norm之和，
不是逐行取最大后丢掉Cmean。

这里可以进一步解除I为保守起见写下的“新旧$f_B$同值”限制。
准确的扩展是：**固定同一个intrinsic metric、物理角、修补中心和
旧缓存reference；允许新$f_B$在M原整个height球内变化。**
它不将当前moving角或metric变化识别成旧坐标。

固定旧$f_B^0$以及由它定义的$D_0,\mathcal H_0,G,\widetilde G,
\mathcal K_0(f_B^0)$，令新高度为任意$f_B^1$。
X/M的共同中心始终是同一个$\widehat W$，不是按$f_B$重新定中心：
$$
 W_*(\gamma,f_B^1)=\widehat W+x_*(\gamma,f_B^1),\qquad
 \|x_*(\gamma,f_B^1)\|_{X_0}\le\rho .
 \tag{R.13a}
$$
M.2--4和I.9的平方零Hilbert模块界在完整product域上统一成立。
取$\partial_\gamma$时仅令$\delta f_B^1=0$，准确端点差现在是
$$
 \Delta T=D_Zd(Z_*,f_B^1)-D_Zd(Z_0,f_B^0),\qquad
 \Delta C_0=D_Zc_0(Z_*,f_B^1)-D_Zc_0(Z_0,f_B^0).
$$
分别对两个完整算子用I.9和I.10，仍有
$\|\Delta T\|<.006006,\ \|\Delta C_0\|<.000751$。
这个triangle估计无需$f_B^1=f_B^0$，也不需把两个高度之差当小扰动。

新bulk仍是$D_0-\mathcal V T_Q(x_*)$；旧$\mathcal H_0$仍是
锁定reference的非zero residual Hessian，绝不随新height重定义。
所以I.14的两坐标界、I.20的准确ordered identity以及I.21的全部
有理上界逐字成立。得到真正统一的结论
$$
 \sup_{(\gamma,f_B^1)\ {\rm in\ the\ original\ product}}
 \|\mathcal K_*(\gamma,f_B^1)-\mathcal K_0(f_B^0)\|
 _{H^0_{\mathrm e,\perp}\to\mathfrak M_\Sigma}<1/5 .
 \tag{R.13b}
$$
上确界仅在原reflection sector取，原$D\Psi_0,S_0,H_{B,0},H_{C,0}$
和缓存identity全固定。I.26--29的完整97读出因而也适用于此扩展。

在同时满足O21的背景上，将(R.12)加上这个统一界，严格得到
$$
 \|\mathcal K_{\rm right}^{\rm proxy}
             -\mathcal K_0(f_B^0)\|<1/5+2^{-52000000}.
 \tag{R.13}
$$
height改变引起的value affine mismatch仍由实际$x_*$读出；
独立导数$\mathcal L_*\delta f_B$和联动列
$\mathcal L_*\mathcal F_\gamma$也都保留。此引理没有改动或重算旧缓存，
没有把不同metric、反射轴或当前moving角之间的差免费设为0。

在原97 moving输入中仍是先取$P_\perp H_{C,0}u$，
再经(R.11)的全物理输出及原$S_0$和mean行。
从小反馈到moving边界误差要准确乘
$\max(\|S_0\|,1)\|H_{C,0}\|$，或未来已实际支付的同输入Gram。
没有把一条full physical界直接冒为97协方差，
也未删low--high/high--low/unknown high回馈。

(R.1)的typed全周期源界可对非反射方向使用。
但I提供与旧97缓存的$1/5$比较，只在其明确反射sector成立；
非反射Bmean仍按M的真正full4Z输出处理。

## 6. 仍保留的输出与增广接口

(R.7)的$c_{B,\gamma}$是raw平均径导差，不能拿它代替
帽内$C_0(L)$或帽端$B_0,C_0$曲率mean。
这些输出使用M的真实代数图；它们的直接gamma响应不带
$\epsilon$。这里只证明其经远端$f_B$返回的附加列很小。

long的平均高度跨度仍是原
$\int_0^Law\,D\kappa\,\dot h\,dt$，
纯远端incoming列保$aw(L)/165$，不乘screening。
帽内/外高度和单一$\lambda$必须用同一真实重建积分。
不同端的height span不是可另行规范的常数。

本篇的fixed-background tail proxy与实际Darboux reduced derivative
之间，还存在已列出的$\mathcal E_N$、第一metric参数/残差投影、
$H_p$端值和相关commutator；这些都按A/N原接口保留。
本列并未证明任何未支付的augmented Schur或非线性tail解，
也不声称未知inner gamma已经由全局匹配选进O21域。

真正后继是把(R.11)连同完整affine cap mismatch、所有设计参数、
mean、height、frame和ordinary/weak源放入同一个实际系统。
之后单个精确闭$G$及原几何门若真正成立，
固定metric族由已付几何相位与真实静态marker构造，
不需要一个虚构的变动$\nu$族。
