# R119 续篇：有限径向正则的两根首相位及固定第二参数的完整标量间隙

2026-11-15，visible-exact / tail_connector。

**状态：已证明的有限径向子域结论。** 本篇在有限角 principal 图的一个明确
径向正则子域中，定义完整两根密度有限部，并与实际几何散度返回的首相位
认同。所有 Fourier 模和两根都参加；不要求未知背景角解析。
固定原第二 metric 参数后，第一参数仍由新的 principal 图真实选择。
足够小球内，原首相位算术间隙是开放条件，不必每一步重新把第二
标量调回原值。

这里的几何算子是新 O 篇的 $\mathcal J_W$。
非解背景的真实 $\mathcal L_W$ 与它之间仍有 O.9--O.17 的
完整 residual 一阶差；本文不把二者混同，也不删除第二 metric 的
外部给定方向。全网络变化背景逆及最终非线性迭代继续是独立任务。

## 1. 同一对象及增加的真实径向输入

采用 [有限 Sobolev principal 图](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md)
的 P.1--P.8，固定同一个 $\Omega$、第二参数
$\gamma_{2,i}=\bar\gamma_{2,i}+\mathfrak q_i$ 和实际 fixed stop。
仍用 $R_*=2^{-2097152}$。以下只收窄新的辅助函数域，
不改原 $\mu_j,\zeta_j,C_j$ 或几何 profile。

置
$$
 J_j=j+5,\qquad
 \ell_j=2^{-64}J_j^{-2}\delta_j^4,\qquad
 \ell_o=2^{-1024}.
 \tag{B.1}
$$
对 P.5 的四态 $Z_0=(P_0,K_{\perp,0},U_0,V_0)$ 定义
$$
 \|u_\perp\|_{\mathscr H^{[4]}}
 =
 \max\left\{
 \sup_j C_j^{-1}
      \max_{0\le a\le4}\ell_j^a
           \sup_{I_j}\|\partial_t^a Z_0\|_{H^{8196}},
 \quad
 2^{440}\max_{0\le a\le4}\ell_o^a
      \sup_{\mathrm{cut128}\to e_0}
                           \|\partial_t^a Z_0\|_{H^{8196}}
 \right\}.
 \tag{B.2}
$$
导数在原真实径向分片内取值；所有四态及其一阶径向迹在真实接缝
相等。根 collar 内使用同一侧的完整 $C^4_t$ 状态，不能把两个
不同 germ 的 jets 拼成一个根图。若只给本篇首有限部而不做第5节
的返回认同，二阶径向态已经足够；四阶是为实际 root/strict
有限阶算子证明预留的明确输入。

$\mathscr H^{[4]}$ 是新 norm。P.5 的 $C_tH^{8196}$、
前篇 R 的 $Y_{64}$、普通源的单个上确界都不自动给 (B.2)。
特别不能从本篇声称一个 arbitrary ordinary/BV 源已经具有四阶
径向导数。以下取
$$
                  R=\|u_\perp\|_{\mathscr H^{[4]}}\le R_*.
 \tag{B.3}
$$
用 P 的唯一第一参数 $\gamma_1^*(u_\perp)$，
再按同一 M 小根和物理高度积分补全 $K_0$ 与 $\lambda$。
所有参数 bump 的支集仍离根，且固定的两根位置及斜率不变。

由原完整径向表，
$$
 |Q|\le2^{12}J_j\delta_j^{-3/2},\quad
 |Q_t|\le2^{18}J_j\delta_j^{-3},\quad
 |Q_{tt}|\le2^{26}J_j\delta_j^{-9/2},\quad
 |Q_{ttt}|\le2^{40}J_j\delta_j^{-6}.
 \tag{B.4}
$$
参考根 F.6 还给
$\delta_j^{-9/4}<b_e<2^{16}\sqrt{J_j}\delta_j^{-9/4}$。
新增根取自己的 $2^{28}<b_0<2^{29}$，
不能使用旧 quartic 公式。
这些界给所有本篇实际分片，第四 shape 在其支集上仅用已经保留的
$C^4$ 范数。根处另有下述独立的准确 polynomial germ 输入，
不能由一般 $C^4$ profile 免费推出 $B_0=Q/x$ 的第四导数。

具体地，[参考 Airy 证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
(F.4)--(F.7) 给旧根
$B_0=1+(14d_e-1/28)x-d_ex^2-7d_e^2x^3$，
$0<d_e<2^{-10}$，故 $B_0^{(4)}=0$；
最近真实接缝的 $x$ 距离大于13。
[新 simple 根证明](R119-supplement-new-fixed-stop-simple-root-full-analytic-chart-and-sources.md)
(A.3)--(A.4) 给新增根的完整四次 $B_0$ 及全部四个准确系数。
在 $|x|\le1/2$，该式还直接给
$|B_0'''|<1/128$、$|B_0^{(4)}|<1/512$。
两类根均有 $|B_0-1|<1/16$；逐次对平方根求导，
其前四阶导数可统一放宽为 $2^{12}$。
所有参数 bump 和第四 shape 的支集与这些 germ 分离。
本篇根处使用这项准确多项式信息，不新增一个全 profile 的第五导数假设。

## 2. 原固定物理根坐标中的完整有限部

对同一几何矩阵
$$
 G=\mu
 \begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix},\quad
 \mu=\frac w{a_{\rm ph}}JD^{-3/2},\quad
 \Lambda=\sqrt{-\det G}
              =\frac w{a_{\rm ph}}\frac{\sqrt Q}{D},
 \qquad
 \kappa=\Lambda^{-1/2}
                   \operatorname{div}(G\nabla\Lambda^{-1/2}),
 \tag{B.5}
$$
所有 $P,K,U,V$ 和 mean 均为当前背景的真值。
$\kappa$ 只在负型区定义，不把正型区的平方根换成绝对值后混入。

固定一根，用原 $x=\varsigma b_e(t-t_e)>0$ 向负侧，
并作准确正密度 Piola 变换得到 $G_e$。
在此坐标 $\Lambda_e=a_e(x,\theta)\sqrt x$，
$a_e>0$；令 $h_e=a_e^{-1/2}$。
不需要任何 mixed root 图即可直接求导：
$$
 \kappa_e=A_e x^{-5/2}+B_e x^{-3/2}+C_e x^{-1/2},
$$
$$
 \begin{aligned}
 A_e&=\frac5{16}(G_e)^{xx}h_e^2,\\
 B_e&=-\frac12h_e\{(G_e)^{xx}(h_e)_x+
                             (G_e)^{x\theta}(h_e)_\theta\}\\
    &\hspace{1em}
        -\frac14\{\partial_x(G_e)^{xx}
                     +\partial_\theta(G_e)^{x\theta}\}h_e^2,\\
 C_e&=h_e\,\operatorname{div}(G_e\nabla h_e).
 \end{aligned}                                             \tag{B.6}
$$
所有交叉项及 coefficient 的导数完整保留。
定义
$$
 A_{e,0}=A_e(0,\theta),\qquad
 B_{e,0}^{\rm tot}=(A_e)_x(0,\theta)+B_e(0,\theta),
$$
$$
 R_e(x,\theta)=
 \int_0^1(1-s)(A_e)_{xx}(sx,\theta)\,ds
       +\int_0^1(B_e)_x(sx,\theta)\,ds+C_e(x,\theta).
$$
则在 $0<x\le H:=1/128$，
$$
 \kappa_e=A_{e,0}x^{-5/2}
                  +B_{e,0}^{\rm tot}x^{-3/2}+R_ex^{-1/2}.
 \tag{B.7}
$$
所以这个真实 collar 的有限部准确为
$$
 \operatorname{FP}\int_0^H\langle\kappa_e\rangle\,dx
 =-\frac23\langle A_{e,0}\rangle H^{-3/2}
       -2\langle B_{e,0}^{\rm tot}\rangle H^{-1/2}
       +\int_0^H\langle R_e\rangle x^{-1/2}\,dx .
 \tag{B.8}
$$
角平均始终是完整圆周的归一积分。
(B.8) 的全部右端是普通有限积分和真实两阶 traces，
不存在两个发散积分相减的误差估计。

在两个固定 $x=H$ 根 cut 之间积分原 $\kappa$，
再加入两式 (B.8)，定义
$$
 \boxed{\qquad
 \beta_i(W,\Gamma)
    =-\frac14\operatorname{FP}
                   \int_{I_i}\langle\kappa\rangle\,dt .
 \qquad}                                                   \tag{B.9}
$$
整体乘 $G$ 一个正的径向常数不改变 $\kappa$，
所以原 $\rho,\varepsilon_s$ 的共同物理密度尺度准确消去；
这些尺度仍留在原高度、total conormal 和 source 中。

## 3. cutoff 不变量及真实负侧 canonical 图

二维 contravariant 密度的准确 Piola 恒等式给
$\Lambda_c=\Lambda\circ\Psi^{-1}$、
$\kappa_c=(\kappa/|\det D\Psi|)\circ\Psi^{-1}$。
因此 $\kappa\,dt\,d\theta$ 是准确密度。

这里 cutoff 不变量需要真实正则性。若新根坐标
$\xi=a(\theta)x+b(\theta)x^2+O(x^3)$，
$a>0$，角图也是 $C^3$，则把原 cutoff 换成 $\xi=\epsilon$
只改变 $\epsilon^{-3/2},\epsilon^{-1/2}$ 两个发散系数和趋零项，
不产生常数项。这由 (B.7) 逐项积分及逆 Taylor 公式得到。
一般仅 $C^2$ 坐标可能有 $x^{5/2}$ 项，不能据此免费断言有限部不变；
本篇使用 (B.2) 支付所需第三阶。

真实负侧图可直接由实 ODE 构造，无需复角延拓。
写 $Q=xB_0(x)$、$d,v$ 为当前系数，令
$$
 (S_\pm)_x+\frac{\varsigma}{b_e}
               (-d\pm\sqrt x\sqrt{B_0}\,v)(S_\pm)_\theta=0,
 \qquad S_\pm(0,\theta)=\theta .
$$
置
$$
 X=\frac{S_++S_-}{2},\qquad
 T=\frac{3\varsigma b_e}{4x^{3/2}}(S_--S_+).
$$
其准确可去系统是
$$
 X_x-\frac{\varsigma d}{b_e}X_\theta
             -\frac{2x^2}{3b_e^2}\sqrt{B_0}v\,T_\theta=0,
$$
$$
 xT_x+\frac32T-\frac{\varsigma d}{b_e}xT_\theta
                       =\frac32\sqrt{B_0}v\,X_\theta .
 \tag{B.10}
$$
沿第一条的 drift 流，第二条乘 $x^{3/2}$ 后作真实积分。
每取 $k$ 阶 $x$ 导，左侧准确为
$x\partial_x+k+3/2$ 加同一 drift，
故其 Volterra 逆的常数至多 $(k+3/2)^{-1}$。
与第一条联立，利用 $x^2/b_e^2$、B.4 后独立支付的
$\sqrt{B_0}$ 前四阶导数及足够多已给角导数，
得到 $T,X$ 的所需四阶实 jets；没有对 $x^{-3/2}$ 作发散点值估计。
对于 (B.2) 的小球，各 root 上相对径向图的四阶差由
$2^{4096}\max_{a\le4}\|\partial_x^a Z\|_{C^8_\theta}$ 支付。
原 profile 和 $R_*$ 使该数小于 $2^{-100}$；
所有实际 root Jacobian 保持参考的严格正下界。

取 $\xi=xT^{2/3}$、$\phi=X$。
两个真实 null labels 给
$$
 G_c=\alpha
  \begin{pmatrix}1&0\\0&-\xi/b_e^2\end{pmatrix},
 \qquad
 \alpha=
 \left[b_e\frac w{a_{\rm ph}}D^{-1}
                    \sqrt{B_0/T^{2/3}}\right]\circ\Psi^{-1}.
 \tag{B.11}
$$
这是实负侧的准确恒等式；没有宣称有限光滑输入被解析延拓到正侧。
在这个真图中，$A_e=5b_e/16$ 为常数、$B_e=0$，
而 height 共轭后的 $V$ 给
$$
 \kappa_c=b_e\left\{\frac5{16\xi^{5/2}}
                            +\frac{V}{\sqrt\xi}\right\}.
 \tag{B.12}
$$
(B.8)--(B.12) 因而准确等于旧完整有限部
$\frac12\int\kappa-\sum_e5b_e/(48\epsilon^{3/2})$
再乘 $-1/2$，包括旧两个根和新 simple 根。

## 4. 原完整 profile 上的有限部差与真径向费用

本节先固定两个 metric 参数，令 $\beta_i^{\rm rad}$ 是同一 metric
下的径向值。所有 scalar 费用只需 (B.2) 中到二阶的部分，
不消费8196阶角导。由 $H^4(\mathbb T)\hookrightarrow C^2(\mathbb T)$
和完整商法则，当前态、方向态的 $C^2_{x,\theta}$ 界分别是
$2^{1024}C_j^\# R\max(1,(b_e\ell_j)^{-2})$
和把 $R$ 换为方向 norm 的同式。
四阶根图的小量也可明确由
$$
 2^{6000}J_j^8\delta_j^{-16}C_j^\#R
 \tag{B.13}
$$
支付。原 $\sum_j(K_j^{\rm ref})^2C_j<2^{160016}$、
$K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}$
及准确邻层比，给 (B.13) 的根总和小于 $2^{165000}R$。
新增 connector 的同一门小于 $2^{12288}R$。
这些是 B.10 中实际 $2^{-100}$ 的来源。

为核根费用的物理归一，令
$r_0(x)=\mu_0(x)/\mu_0(0)$、$\mu_0=w/a_{\rm ph}$。
把 $G_e$ 除以径向常数 $b_e\mu_0(0)$ 后，
$$
 \overline G_e=r_0JD^{-3/2}
 \begin{pmatrix}
 1&-\varsigma d/b_e\\
 -\varsigma d/b_e&(d^2-Qv^2)/b_e^2
 \end{pmatrix},\qquad
 {h_e\over\sqrt{b_e}}
             =r_0^{-1/2}B_0^{-1/4}D^{1/2}.
 \tag{B.14}
$$
(B.14) 中的 $h_e$ 指该归一后重新定义的 $a_e^{-1/2}$；
常数归一不改变 $\kappa_e$。
在 $|x|\le1/128$，$r_0,B_0$ 及其前两导都有固定界和正下界。
(B.6)--(B.8) 的一、二次差分别不超过
$$
 2^{4096}b_e\max(1,(b_e\ell_j)^{-2})\,C_j^\# R,\qquad
 2^{4096}b_e\max(1,(b_e\ell_j)^{-2})\,
                         (C_j^\#)^2R_1R_2 .
 \tag{B.15}
$$
例如每个根余项的积分权是
$\int_0^Hx^{-1/2}dx=2\sqrt H$，
两个有限端项另付 $H^{-3/2}=2^{21/2}$ 和 $H^{-1/2}$；
这些已在4096内。
这里没有把 $\mu_0(0)$ 的极小量取逆当作算子费。

在完整 strict 段，仍使用准确恒等式
$$
 T=G/\Lambda,\quad l=\log\Lambda,\qquad
 \kappa=-\frac12\operatorname{div}(T\nabla l)
                       -\frac14\,\nabla l\cdot T\nabla l .
 \tag{B.16}
$$
原固定 $x=H$ cut 外有 $Q>2^{-9}$；
compact 控制只在原严格正下界的支集内改变 $Q$。
(B.4) 直接给
$\ell_j|(\log\Lambda_0)_t|<1/8$、
$\ell_j^2|(\log\Lambda_0)_{tt}|<1/8$。
当前差 $l-l_0=-\log D$，
$T-T_0$ 则只用原 $d,v-1$；
它们的各二阶 scaled jet 由 $2^{1024}C_j^\#R$ 支付。
逐项代入 (B.16)，再用 $|I_i|<4\delta_j$、
$|Q|\le2^{12}J_j\delta_j^{-3/2}$，
得到每个内部完整分量的保守统一门
$$
 \begin{aligned}
 |\beta_i(W,\Gamma)-\beta_i^{\rm rad}(\Gamma)|
     &\le L_i C_j^\#R,\\
 |D_u^2\beta_i(W,\Gamma)[u_1,u_2]|
     &\le L_i(C_j^\#)^2
                       \|u_1\|_{\mathscr H^{[4]}}
                       \|u_2\|_{\mathscr H^{[4]}},\\
 L_i&=2^{16384}J_j^5\delta_j^{-11}.
 \end{aligned}                                             \tag{B.17}
$$
根项的径向幂最多为 $9/4+8=41/4<11$，
strict 项最多为 $3/2+8-1=17/2<11$；
$J_j$ 次数分别小于5和等于5。
(B.17) 的16384 bits覆盖 B.15、完整 mean 小根的二阶差、
Sobolev嵌入、最多两个相邻胞和两个根。
这不是把旧角解析 Cauchy 门用于有限光滑背景。

新增完整外分量由第129胞尾段及固定 connector 拼成。
其第一段用刚才的实际 $j=129$，
第二段用 $\ell_o^{-2}=2^{2048}$、
$2^{28}<b_0<2^{29}$、原完整负段长度和
$\int(1+Q)<282\log2$。
同一个推导给外行
$$
 |\beta_o-\beta_o^{\rm rad}|\le2^{32768}R,\qquad
 |D_u^2\beta_o[u_1,u_2]|
       \le2^{32768}\|u_1\|_{\mathscr H^{[4]}}
                    \|u_2\|_{\mathscr H^{[4]}} .
 \tag{B.18}
$$
未将该段按内部 $4\delta_{129}$ 的短长度收费。

在固定 metric 下，(B.9) 对真实角平移不变。
零背景处，非mean高度方向的四态平均为0，
且 M 的真 mean 根一阶导也为0；
因此 $D_u\beta_i(0,\Gamma)=0$。
由 (B.17)--(B.18) 的真实二阶差，
$$
 |\beta_i(W,\Gamma)-\beta_i^{\rm rad}(\Gamma)|
       \le L_i(C_j^\#)^2 R^2,\qquad
 |\beta_o-\beta_o^{\rm rad}|\le2^{32768}R^2 .
 \tag{B.19}
$$
此处未以“非mean变量”删除二次产生的 mean。

## 5. 有限光滑背景上的实际首相位认同

本节证明的是给定**同一个完整实背景**的几何散度返回，
所需真实正区仍使用其完整双端正 form；涉及外 returned 图时，
须为同一实背景已经给出的 selfadjoint、非负且保原 coercive 端口门的
完整图。任意独立 $C_R$ 并不自动满足此假设，
也不能用一个任意 Dirichlet 数替代。
若只提供 (B.2) 的负侧数据而未提供其正侧实际背景/图，
则 (B.9) 已有定义，但不能据本节宣称正端口已被构造。

负侧的准确 B.11 图和 height 共轭给
$u_{\xi\xi}-\xi b_e^{-2}u_{\phi\phi}+Vu=0$。
只用实有限 jets，$V,V_\xi$ 及所需有限角导有界。
对固定 $|s|\le64$，完整 Airy 核
$$
 F_m(\xi)^{-1}
 \begin{pmatrix}0&0\\-V_{m-n}(\xi)&0\end{pmatrix}F_n(\xi)
 \tag{B.20}
$$
保正负全部模和 mean。
在 $|m-n|\le|n|/2$ 上，原同支一次项是
$\frac{i\sigma b_e}{2}\int_0^H
 V(\xi,\phi+\sigma2\xi^{3/2}/(3b_e))\xi^{-1/2}d\xi\,D_\phi^{-1}$。
完整 Airy 两行、$\xi\sim(|n|/b_e)^{-2/3}$ 的根层切分
和一次真实径向分部，给余项的 $4/3$ 增益。

这里远 lag 不使用角解析性：
以至多 $2|s|+32\le160$ 个已给角导，
$|V_l|+|(V_\xi)_l|\le C\langle l\rangle^{-160}$。
在远 lag 上，Airy 两频率比例、完整 Sobolev 权比及两行多项式费
均由这个幂的可和余量支付。
二次及以上的完整 Volterra 每次给 $2/3$，
按原两侧 Schur 将两个增益分别分配到有序两项。
有限模和两 mean 使用原自由完整两行，
不把 $D^{-1}$ 或 $b_e/|m|$ 代入 $m=0$。

正侧不需要有限光滑函数的非法复角求值。
将 B.11 真负侧坐标取至四阶、密度取至三阶的根 jets，
在正侧作同一根处的实 Taylor 延拓。
用 $y=-\xi>0$，在足够小的固定 collar，
归一后的准确正区散度矩阵可写成
$$
 \alpha_J\operatorname{diag}(1,y/b_e^2)+E,\qquad
 |E_{yy}|+b_e|E_{y\phi}|+b_e^2|E_{\phi\phi}|
                                  \le C\,y^3\alpha_J ,
 \tag{B.21}
$$
并有相应的一阶导数 $Cy^2$ 界。
原因是原两侧背景具有同一真实前三阶 root jets，
故负侧已准确为零的交叉及 principal 差的0、1、2阶 jets
在正侧也为零。Taylor 延拓的 Jacobian 保持严格正。
这只用根附近的真实 jets；没有跨越原径向 seam
把两个不同背景解析粘合。

对每个高输入令 $\lambda=|m|/b_e$，
取完整截断 Ai trial，另端 trial 为0。
$E$ 的 residual 必须完整展开并收费。
在 Airy 层 $y\sim\lambda^{-2/3}$，其三个二阶项的大小分别为
$$
 y^3\partial_y^2:\ \lambda^{-2/3},\qquad
 (y^3/b_e)\partial_y\partial_\phi:\ \lambda^{-1/3},\qquad
 (y^3/b_e^2)\partial_\phi^2:\ 1 .
 \tag{B.22}
$$
这里使用真实 normal-trace 输入的 Ai 归一：
$u_m(y)=c_{\rm Ai}\lambda^{-1/3}
\operatorname{Ai}(\lambda^{2/3}y)z_m$，
其中固定 $c_{\rm Ai}$ 由原 Airy 两行归一确定。
例如最差的 $y^3\lambda^2u_m$ 项，
将 $z=\lambda^{2/3}y$ 代入完整平方积分，
其 $L^2_y$ 范数是 $O(\lambda^{-2/3})|z_m|$；
再乘真实 $H^{-2/3}_\lambda$ 权即为
$O(\lambda^{-4/3})|z_m|$。
cross、$yy$ 及一阶 coefficient 导数项的指数更好；
所有 $\operatorname{Ai}$、$\operatorname{Ai}'$、
$\operatorname{Ai}''$ 的带多项式平方矩完整积分。
height 共轭产生的其余项更低。
因此它们同 $V_J$ trial、$2\chi'U'_0$、$\chi''U_0$
一起，满足原完整 contact residual
$L^2\to L^2_yH^{-2/3}_\lambda$ 在右乘
$\langle\lambda\rangle^{4/3}$ 后有界的门。
证明逐项在真实正轴积分 Ai 及 Ai' 的完整平方矩，
再作有限角卷积；(B.22) 是这个积分换元的指数，非只取层中点。
cutoff 外的正轴指数尾包括全部导数。

同一真实正 form 的试验能量、trace 不等式和 Poisson 对偶，
于是给包含两端 cross 的 $R_++I$ 的右 $4/3$ 增益。
完整 Green 酉性及伴随给左侧同窗。
上述 true form 保 $m=0$ 的两状态和真实正能量 mean 核；
低输入另以有限阶平滑列保留，不以 trial 指定反射值。
所以正侧不贡献一个新的 $1/m$ 首相位。

strict 部分沿两真流使用原准确 density transport。
同支首系数平均正好是
$\frac{i\sigma}{2}\int\langle\kappa\rangle dt$；
跨支用真正非零相速度差作一次径向分部，
保所有原有限 seam 及其跳幅。
(B.2)、(B.4) 使完整系数的所需总变差有限，
没有对 unknown body source 作径向微分。
在角远锥也只用前面实际有限导数的可和界。

最后按原完整负/正 ordered word 搬运两迹。
primitive 恒等式必须保完整 mean 修正，
$D^{-1}\mathcal D_H=C_HD^{-1}+\text{mean correction}$；
normal shear、height 和密度因子保持真顺序。
首系数的平均在真实角图下是密度积分，因而不变。
正锥物理频率 $m$ 的首相位是
$-\operatorname{FP}\int\langle\kappa\rangle dt/m$。
改成标准频率 $m=4n$，正好给 (B.9)。
因此在 P 的真实 principal 共轭后，
$$
 I+\mathcal U_{\omega_i}
     [I+i\operatorname{Op}(B_i(x)/n)]+\mathcal R_i,\qquad
 \langle B_i\rangle=\beta_i,\qquad
 \mathcal R_i:H^s\to H^{s+4/3},\quad |s|\le64 .
 \tag{B.23}
$$
这里每个完整分量的有限常数确实存在。
本文尚未把这些新有限光滑 root/strict 常数的**全层权和**
代入完整 closed Schur；这一步不能从 (B.23) 省略。

## 6. 固定第二参数后，原标量间隙仍有统一余量

先给纯径向第一参数的实际费用，避免把它当成免费 phase。
两个 bump 的原严格支集上，
$Q\ge\mathcal B_i/2>\delta_j^{-3/2}/2$、
支集长度小于 $2\eta_j$，
$\eta_j=\delta_j^{3/2}/(4\sqrt2)$，
并且
$|\partial_t^a\psi_s|<2^{12a+8}\eta_j^{-a}$，$1\le a\le3$。
它们完全不改变 root germs。
对原准确公式
$$
 \kappa_0=
 \frac{Q_t}{2\sqrt Q}-\frac{(1+Q)^2}{4\sqrt Q}
             +\frac{5Q_t^2}{16Q^{5/2}}
             -\frac{Q_{tt}}{4Q^{3/2}}
$$
取 $\dot Q=-\partial_t\psi_s$。
完整导数中的积分项分别含
$\dot Q_t/\sqrt Q$、$Q_t\dot Q/Q^{3/2}$、
$(1+Q)\dot Q/\sqrt Q$、
$Q_t\dot Q_t/Q^{5/2}$、
$Q_t^2\dot Q/Q^{7/2}$、
$\dot Q_{tt}/Q^{3/2}$ 或
$Q_{tt}\dot Q/Q^{5/2}$。
(B.4) 与真实长度给共同 $\delta_j^{-3/4}$ 幂。
放宽即得
$$
 |\partial_{\gamma_s}\beta_i^{\rm rad}|
                  <2^{128}J_j^2\delta_j^{-1}\quad(s=1,2).
 \tag{B.24}
$$
新增外行的两个支集仍是同一真实支集，
故可取 $2^{400}$；新增根、平台和 fixed stop 只加常数相位。
没有在此处重置它们。

记 $\gamma_1^{\rm rad}=\gamma_1^*(0)$。
P.39 的准确物理第一参数导数及其二次值界，连同
(B.19)、(B.24)，给
$$
 \begin{aligned}
 |\beta_i(u_\perp,\gamma_1^*(u_\perp),\gamma_2)
             -\beta_i(0,\gamma_1^{\rm rad},\gamma_2)|
 &\le2^{1050200}J_j^5\delta_j^{-11}C_j^\#R^2 ,
                 &&i\ne o,\\
 |\beta_o(u_\perp,\gamma_1^*(u_\perp),\gamma_2)
             -\beta_o(0,\gamma_1^{\rm rad},\gamma_2)|
 &\le2^{1050500}R^2 .
 \end{aligned}                                             \tag{B.25}
$$
第一行的两项分别是固定 metric 的二次 nonmean 费用与
$2^{128}J_j^2\delta_j^{-1}$ 乘真实 $\Delta\gamma_1$。
用了 $\sup C_j^\#<1$，没有删除 $\Gamma_1$ 导致的径向相位变化。

现在选一个**已知实际成员** $u_\perp^\flat$，
其 $\|u_\perp^\flat\|_{\mathscr H^{[4]}}\le R_*$，
且原实际双相位选择给
$\beta_i(u_\perp^\flat)=\beta_i^0$。
从这时起冻结其真实 $\gamma_2^\flat$；
以后仅以 P 的第一反项保持全部 $\omega_i$。
新图不声称在其它输入处仍等于旧 $\Gamma^*(a)$，
也不把“冻结”解释为删除外部给定的第二 metric 方向。

原完整算术 Q.14 与新增 J.3 给
$$
 N_i<2^{160}J_j^3\delta_j^{-13/2}\quad(i\ne o),
                       \qquad N_o<2^{1325}.
 \tag{B.26}
$$
因为 $J_j^8\delta_j^{-35/2}C_j^\#$ 被原
$(K_j^{\rm ref})^2C_j$ 的全层和控制，
两个邻层的 $2^{21}$ 比例、$j+5$ 与 $j+4$ 的差以及两分量计数
总可收 $2^{33}$，
(B.25)--(B.26) 给
$$
 \sum_{i\in\mathcal I_+}
 N_i\,|\beta_i(u_\perp)-\beta_i(u_\perp^\flat)|
 \le2^{1211001}R_*^2 .
 \tag{B.27}
$$
特别
$$
 128\sup_i N_i|\beta_i(u_\perp)-\beta_i^0|
 \le2^{1211008-4194304}<2^{-2980000}.
 \tag{B.28}
$$
这里使用完整三段 profile 求和，包含129--8192前缀和两个大常数
$\delta_{4096}^{-3/2}$、$\delta_{8192}^{-485/4}$。
不是仅用深尾最终正幂得出统一半径。

令
$$
 D_i^0(n)=1+e^{i(n\omega_i+\beta_i^0/n)},\qquad
 D_i^W(n)=1+e^{i(n\omega_i+\beta_i(W)/n)} .
$$
对每个实际 $n\ne0$，
$|D_i^W-D_i^0|\le|\beta_i(W)-\beta_i^0|/|n|$。
因此
$$
 \boxed{\quad
 |D_i^W(n)|>\frac1{256N_i|n|},\qquad
 \sup_{i,n\ne0}
 \left|\frac{D_i^W(n)-D_i^0(n)}{D_i^0(n)}\right|
                                      <2^{-2980000}.
 \quad}                                                   \tag{B.29}
$$
这是所有无限层与所有非zero频率的共同门，
不是先在有限窗口选择新目标。
在物理 $M=4|n|$ 中相应 inverse 小于 $64N_iM$。

(B.29) 的比值是准确的对角乘子，
所以在任何已定义的对角层权、角 Sobolev 权及 $\ell^p$ 和上
都有同一个上界。
这句话只针对该**标量模型比值**：
把实际完整返回放到这个表示的真角图、normal shear、
低输入和外端 source，仍须各自收费。
两个 mean 不代入 $\beta/n$，它们仍是原完整两状态系统。

## 7. 首同调、已知成员及源列的范围

P 的 principal 共轭在本篇子域仍是其原 $C^{8188}$ 真共轭。
(B.23) 中的零均值首系数用同一准确除数解
$$
 q_i(x)-q_i(x-\omega_i)=\beta_i-B_i(x),\qquad\langle q_i\rangle=0 .
 \tag{B.30}
$$
$|e^{in\omega_i}-1|>\kappa_i/(4096|n|)$
使每个有限 Sobolev 行的损失至多一阶。
实际系数和 P 共轭的有限角余量远大于第5节所需窗口。
取真实 selfadjoint order $-1$ 的 $Q_i$，
保 mean 为0，再用 $e^{iQ_i}$ 的完整有序共轭，
同支首项准确化为 $\exp(i\beta_i D_x^{-1})$，
其余项至少是 $4/3$ 阶。
低频的可逆行变换可以只在足够高的实际块反解，
所有低行与跨行留在完整余项；这里没有预设低 Schur 可逆。
由此 (B.29) 确实是第5节同一几何返回的标量主模型，
而非任意指定的 $\beta$。

为说明已知成员确实进入新增径向域，
旧 controlled C.22--C.24 先给每胞至少
$\tau_{128}+224>236$ 的完整物理角宽，
新增 connector 用 S.25 的 $2683/800>3$。
在其真实 nonlinear 方程上连续取四次 $t$ 导：
对 $(P,K)$ 最高只需已付 $Q_{ttt}$ 和四次角导；
四态还含 $U=P_\theta,V=K_\theta$，故统一支付到第五次角导。
每次原方程的 $(1+|Q|)$ 因子及 (B.4) 均由
$\ell_j$ 的相应次数支付；在 connector 用 $\ell_o$。
先在原更宽 Wiener 角域作这些有限次微分：
完整商法则和五次各预留 $1/8$ 的角宽给
$\max_{a\le4}\ell_j^a\|\partial_t^a Z\|_{\mathcal A_2}
\le2^{1024}C_j^\#\mathcal X$；
相同 connector 项用其原 $2^{-447}\mathcal X$。
这是普通有限次微分，所有所需 $Q_{ttt}$ 已在 (B.4)；
未在第五阶继续。再嵌入 $H^{8196}$，
所需 Fourier 因子可放宽为 $2^{131072}$。
完整 mean 用同一未投影方程，不以 Galerkin mean 代替。
连同四次商法则、六邻胞与 $w/w_0$ 的真实乘子，
安全地得到
$$
 \|u_\perp^{\rm old}\|_{\mathscr H^{[4]}}
                         \le2^{133000}\mathcal X<R_* .
 \tag{B.31}
$$
真实接缝只作原分片导数；没有宣称 $C^4$ 的 profile 跨缝解析。
这是对**已知解析成员**的识别。
一般 R 的 $Y_{64}$ 校正仍不自动具有这些角/径向输入，
必须在真正的 smoothing/tame inverse 中另付。

ordinary/weak source、两个 mean、独立 height gauge、
外 $C_R/B_0$、$\nu$ 及所有 metric 列没有进入 (B.29) 后消失。
未知源继续在原固定 $t$ 中给定；
只有齐次端口使用本篇根图，未声称 mixed pullback 对原源 norm
无损。非解背景的真实线性化应使用已经证明的
$$
 c_{\rm phys}\mathcal L_W h
 =c_{\rm phys}\mathcal J_W h-\mathcal E_N[h],
 \qquad
 \mathcal E_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np ,
$$
以及完整 metric 式
$c_{\rm phys}(\mathcal J_W\widetilde h-e_{\psi,\rm rem})
+\psi N-\mathcal E_N[\widetilde h]$。
其中 O 篇的 $\alpha,\beta,\gamma$ 是 residual 系数，
不是本篇的首相位 $\beta_i$。

本篇关闭的是：有限径向/角背景中同一两根首相位的真实定义与认同，
以及固定第二参数时其完整算术模型的开放余量。
变化背景的全层 $4/3$ 余项、真实所有中低窗及帽反馈，
仍须在同一个有限角强径向域中给出完整费用；
没有由局部有限常数或 (B.29) 单独授予 closed inverse。
