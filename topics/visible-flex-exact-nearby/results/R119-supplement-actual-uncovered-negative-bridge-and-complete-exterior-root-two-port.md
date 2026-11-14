# R119 续篇：未覆盖外负分量的完整 Cauchy 桥与真实根口双端响应

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 本篇处理原内部指标集之外的真实分量
$(129,2)$。它从真实根口 $e_X$ 到 $D=\mathrm{cut128}$，
没有把 cut128 当作一个 simple 根，也没有在这里增加可调反射。
在同一实际非径向背景上，它给出全频、含两个 mean 的 onto
$J$-unitary Cauchy 传递及其双向 norm 界。接上已经证明的
$D\to C\to B$ 完整双端组件后，得到原 $e_X,B$ 两端的真实
$L^2$ 酉 scattering。这里的 $B$ 仍是原双 bump 外端。

$J$-unitary 只表示保持不定 Green 型。本篇另用正定能量支付
Cauchy 的双向界，绝不把它的 $L^2$ norm 当作1。
真正 norm1 的对象是最后的 incoming/outgoing scattering。
实际 returned 方程的逆仍须另证；本篇不以外组件酉性代替它。

## 1. 同一个外负分量、当前标签域与实际几何

采用
[原内部枚举](R119-supplement-joint-actual-negative-band-return-kam.md)
(K.3) 的定义：完整内部集合为
$\{(j,1):j\ge129\}\cup\{(j,2):j\ge130\}$，
而 $(129,2)$ 在 cut128 截断，其下降参数固定为0。
$e_X$ 是这段的真实根端，即第129胞元第二个上升 quintic 的外根。
本篇仅对这个原来未覆盖的区间重做估计，不援引“全部内部分量”
的量词将它自动纳入。

背景与
[开放内部逆](R119-supplement-open-radial-network-fractional-moment-and-actual-nonmean-inverse.md)、
[完整 mean 商](R119-supplement-flat-mean-Green-domain-and-complete-open-internal-inverse.md)
及
[真实外双端组件](R119-supplement-actual-positive-cross-port-smoothing-and-exterior-unitary-two-port.md)
相同。所有已经选定的 profile、五盒、$\Gamma^*$、固定停止长度和
外 bump 参数保持不变。使用这些证明的真实工作域
$$
 \mathcal X=\|X\|_{\mathcal X_{224}}\le2^{-8388608}.
 \tag{X.1}
$$
这仍是当前反演对象的明确输入，不把它称为非线性匹配方程已解。

置 $\delta=\delta_{129}=(2/25)2^{-129}$、$J=133<2^8$，
$\delta^{-1}<2^{133}$。共同材料时间为 $t=\log r$。
真实 profile 在此片没有新增控制支集；以原
[实际胞元参数](R119-supplement-actual-negative-band-metric-parameters.md)
(M.1)--(M.4) 的记号，
$$
 \mu_0=w_{\rm ref}/a_{\rm phys}
       =C_{\rm phys}\,\delta^6p_*(r)/r^8,\qquad
       \delta/2<p_*<64/\delta,\qquad 1\le r\le2 .
 \tag{X.2}
$$
$C_{\rm phys}>0$ 是原固定尺度常数，不删除它。
原末平台 $p_*=64$ 与 $\delta_{128}^6=64\delta_{129}^6$
准确相接；因此 cut128 处的真密度就是原 connector 密度。
任意两点的径向密度比由 (X.2) 给
$$
       \max(\mu_0(t)/\mu_0(s),\mu_0(s)/\mu_0(t))
                         <2^{15}\delta^{-2}.
 \tag{X.3}
$$

从 $e_X$ 先到已固定的根外 strict 切口 $t_*$：
它是参考 canonical $\xi_*=1/64$ 所定义的原径向切口，
实际 canonical 图与它之间的差由原根图定理消费。
在 $I_*=[t_*,t_D]$ 上，
$$
 Q=-A>1/128,\quad q=\sqrt Q>1/16,\qquad
 Q_{\max}<2^{12}J\delta^{-3/2}<2^{220},\qquad
 |Q_t|<2^{18}J\delta^{-3}<2^{425}.
 \tag{X.4}
$$
这些是原 quintic 的直接导数界；根外下界见参考 (F.9)。
从此根到 cut128，$Q$ 依次沿上升 quintic 的末段增至7，
在第二下降 quintic 上从7增到单个峰后降回7，随后为常数7。
$\gamma_{129,2}=0$，故没有插入额外峰。因而
$$
 \operatorname{TV}_{I_*}(\log Q)<3\log(128Q_{\max})
                                            <681\log2.
 \tag{X.5}
$$
同时 $(\log\mu_0)_t=-1-Q$，所以
$$
 \int_{I_*}(1+Q)\,dt
 =\log{\mu_0(t_*)\over\mu_0(t_D)}
                                      <281\log2.
 \tag{X.6}
$$
这里不需要 $Q(t_D)=0$。原两个简单根的内部总定理没有被用于
这个缺少第二简单根的片段。

## 2. 完整物理状态和独立高度 mean

使用
[实际 strict 密度恒等式](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
(S.5)--(S.9) 的同一真实系数。为与端点 $D$ 区分，将其判别式
记为 $\mathfrak d$：
$$
 \mu=\mu_0 J_0\mathfrak d^{-3/2},\quad
 v={\sqrt{\mathfrak d}\over J_0},\quad
 \nu=qv,\quad d={E(V-P)\over J_0},\quad
 J_0=1+K+EU .
$$
这里 $J_0$ 是背景分母，不是上节的整数 $J=133$。
$K$ 包含原独立 even mean。置
$$
 \lambda=\sqrt{\mu\nu}
       =\sqrt{\mu_0q/\mathfrak d},\qquad
 \lambda_0=\sqrt{\mu_0q},\qquad
 \ell_0=\log(\mu_0q).
 \tag{X.7}
$$

对完整 raw 方程
$$
 \operatorname{div}(G\nabla h)=f-\partial_tF^t-\partial_\theta F^\theta,
 \quad
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix},
$$
始终使用 total 通量
$$
          \pi=\mu(h_t-dh_\theta)+F^t .
 \tag{X.8}
$$
齐次时令
$$
 Y_1=\lambda h_\theta,\quad Y_2=\pi/\lambda,\quad
 c_0=\lambda_0\langle h\rangle,\qquad
 \mathcal E_-^2=\|Y_1\|_{H^{-1/2}}^2+
                \|Y_2\|_{H^{-1/2}}^2+|c_0|^2 .
 \tag{X.9}
$$
在四重圆周上 $I_\theta=\partial_\theta^{-1}(I-\Pi_0)$。
完整重建为
$$
 \langle\sqrt{\mathfrak d}\,Y_1\rangle=0,\qquad
 h={c_0+I_\theta(\sqrt{\mathfrak d}\,Y_1)\over\lambda_0},
 \qquad \pi=\lambda Y_2 .
 \tag{X.10}
$$
第一式是准确的高度周期约束，不把 $Y_1$ 的裸零模设为0。
第二个真实 mean 是 $\langle\pi\rangle=\langle\lambda Y_2\rangle$；
它不是 $Y_{2,0}$。齐次时它守恒。$c_0$ 则满足下面的独立方程，
没有以守恒通量代替高度常数。

原完整四态图给本片宽4上的界
$n_*=4N_{129}\mathcal X$，
$N_{129}<2^{-30}$，因而 $n_*<2^{-28}\mathcal X$。
实际系数、倒数和平方根在原同一小球内。以下交换子只用这些
背景的角余宽，不从未知 Jacobi 数据额外索取角正则性。

## 3. 真对称主部及有限负片的同空间能量

直接从 (X.8) 得到齐次守恒式
$$
 (h_\theta)_t=\partial_\theta(dh_\theta+\mu^{-1}\pi),
 \qquad
 \pi_t=\partial_\theta(d\pi+\mu\nu^2h_\theta).
 \tag{X.11}
$$
因此 $Y=(Y_1,Y_2)^T$ 的完整系统为
$$
 Y_t=\mathsf A Y_\theta+\mathsf C Y,\qquad
 \mathsf A=\begin{pmatrix}d&\nu\\\nu&d\end{pmatrix},
$$
$$
 \mathsf C=
 \begin{pmatrix}
 d_\theta+a&
   \frac12\nu_\theta-\frac12\nu(\log\mu)_\theta\\
 \frac32\nu_\theta+\frac12\nu(\log\mu)_\theta&
 d_\theta-a
 \end{pmatrix},\qquad
 a=(\partial_t-d\partial_\theta)\log\lambda .
 \tag{X.12}
$$
由原准确
$\mathfrak d_t-d\mathfrak d_\theta
=-2Qw_{\rm ref}^2\mathfrak d U/J_0$，
$$
 a=\frac12\ell_{0,t}+{Qw_{\rm ref}^2U\over J_0},
 \qquad
 \ell_{0,t}=-1-Q+{Q_t\over2Q}.
 \tag{X.13}
$$
所以 $\mathsf C-\frac12\ell_{0,t}\operatorname{diag}(1,-1)$
的非径向部分只收 $n_*(1+Q)$；没有偷偷忽略 $Q_t/Q$，
而是把它完整留在径向对角矩阵。

对 $s=-1/2$，Fourier 矩阵直接给
$$
 \|[\Lambda_\theta^s,M_b]\partial_\theta
                       \Lambda_\theta^{-s}\|_{2\to2}
 \le2\sum_k(1+|k|)^{3/2}|\widehat b(k)|,
 \qquad
 \Lambda_\theta=(1-\partial_\theta^2)^{1/2}.
 \tag{X.14}
$$
例如令 $k=m-n$，其单项比是
$|n||\sqrt{\langle n\rangle/\langle m\rangle}-1|$，
小于 $|k|\sqrt{1+|k|}$。
径向常数项的交换子准确为0。
乘法本身同样由半阶 Fourier 权比控制。

原宽4到宽1的完整绝对 Fourier 和、(S.9) 的商法则以及
$|\mathfrak d^{-1}|,|J_0^{-1}|<2$，于是足以取
$$
 \|\mathsf C-\tfrac12\ell_{0,t}\operatorname{diag}(1,-1)
                       :H^{-1/2}\to H^{-1/2}\|
 +\|[\Lambda_\theta^{-1/2},\mathsf A]
              \partial_\theta\Lambda_\theta^{1/2}\|
 +\|\mathsf A_\theta\|_\infty
                 <2^{48}n_*(1+Q).
 \tag{X.15}
$$
这个宽常数可直接由 (X.12)--(X.13) 检查：
$d,\nu-q$ 的每个所需角 moment 分别小于
$2^{12}n_*,2^{12}qn_*$；
$(\log\mu)_\theta$ 及其所需 moment 小于 $2^{12}n_*$；
$Qw_{\rm ref}^2U/J_0$ 的 moment 小于 $2^{12}Qn_*$。
三项矩阵乘积、两个分量和 (X.14) 都严格落在显示余量内。

高度 mean 的准确方程是
$$
 (c_0)_t=\tfrac12\ell_{0,t}c_0+
 \left\langle d\sqrt{\mathfrak d}\,Y_1+
                    q{\mathfrak d\over J_0}Y_2\right\rangle .
 \tag{X.16}
$$
径向项在最后的 functional 中是 $qY_{2,0}$。
非径向项由同一 $H^{1/2}$ 对偶 moment 支付；
利用 $2q\le1+Q$ 及 (X.1)，该 functional 的 norm 小于 $1+Q$。

对 $\Lambda_\theta^{-1/2}Y$ 的正定 $L^2$ 能量积分分部，
$\mathsf A$ 的实对称性消去整个主导角项。
结合 (X.15)--(X.16)，两个时间方向都满足
$$
 \left|{d\over dt}\mathcal E_-^2\right|
 \le\left[4(1+Q)+{|Q_t|\over2Q}\right]\mathcal E_-^2 .
 \tag{X.17}
$$
(X.5)--(X.6) 因而给
$$
 \|\mathcal U_*(t,s)\|,\ \|\mathcal U_*(t,s)^{-1}\|
 \le\exp\!\left(2\!\int_{I_*}(1+Q)dt+
                    \tfrac14\operatorname{TV}_{I_*}\log Q\right)
 <2^{1024}.
 \tag{X.18}
$$
准确 bits 上界是 $562+681/4<733$，余量包含有限状态 norm
的等价费用。它与未知频率无关。

可先在完整 Fourier 压缩上构造。交换子门和正定能量不依赖截断，
故给同空间强极限、唯一解与反向解。
(X.11) 保持 (X.10) 的约束；完整初值逼近后同样在极限保持。
因此这是真正 constrained 三态空间上的 onto Cauchy，
并非仅对一条特定解的能量上界。

## 4. 原 Airy 根口、真实两迹和 cut128 的全部固定费用

唯一的 simple 根仍用
[真实联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
(J.27)--(J.40) 和
[根图](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
(G.14)--(G.32)。它们的原量词是每个 $j\ge129$ simple 根，
故确实覆盖 $e_X$。

记真实斜率 $b=|Q_t(e_X)|$。原宽界给
$$
 b<2^{32}\sqrt J\,\delta^{-9/4}<2^{336}.
 \tag{X.19}
$$
从 balanced root 两态到固定原 $t_*$ 的完整 density 三态，
使用已证明的准确有序乘积
$L_e=J_H\mathcal T_g\mathcal A_*\mathcal U_R$，
正逆 norm 均小于 $2^{2300}\sqrt b<2^{2468}$。
这只调用
[完整物理 Q7 证明](R119-supplement-complete-physical-Q7-network-difference-and-weighted-middle.md)
(D.15)--(D.20) 的单根接线，
不调用该文随后才限定的内部网络总量词。

在根 $\xi=0$，原自由 Airy 两列与 balanced 两态的固定变换
$F_{0,e}^{\pm1}$ 均小于 $2^{20}b^{1/3}<2^{132}$；
见
[完整根波证明](R119-supplement-complete-root-wave-network-and-high-Schur-difference.md)
(V.13)。原共同 Green 常数及规定的支交换在内。
这里没有再次使用
[已经勘误的旧 H.17](R119-supplement-complete-free-Airy-two-row-frame-and-low-frequency-erratum.md)
低模 $\sqrt b$ 界。

说明从原 density 三态到 (X.9) 的完整费用。
置 $\ell=\log(\mu\nu)=\ell_0-\log\mathfrak d$。
若 $W=\lambda h$、$\zeta=\pi/\lambda+
(\ell_t-d\ell_\theta)W/(2\nu)$、$y_\pm=(W_\theta\pm\zeta)/2$，
则
$$
 Y_1=W_\theta-(\log\lambda)_\theta W,\qquad
 Y_2=\zeta-{\ell_t-d\ell_\theta\over2\nu}W,\qquad
 c_0=\langle\sqrt{\mathfrak d}\,W\rangle .
 \tag{X.20}
$$
反向则由 (X.10) 恢复 $W=\mathfrak d^{-1/2}
[c_0+I_\theta(\sqrt{\mathfrak d}Y_1)]$，再恢复 $\zeta,y_\pm$。
两端都保留 mean，而 $I_\theta$ 只作用于已验证的零平均项。

由 (X.4)，$|\ell_{0,t}|<2^{432}$，$1/(2\nu)<2^4$；
径向 shear 的乘法 norm 小于 $2^{436}$。
非径向差的完整半阶乘法 norm由 (X.1)、(X.13) 吸收于同一界。
$\|I_\theta:H^{-1/2}_0\to H^{1/2}_0\|<2$，
故 (X.20) 及其 inverse 均可取 $2^{444}$。

在 $D$，$Q=7$，原接缝 radial jets 完全固定。
令 $\mu_*=\mu_0(C)$，用三阶证明的真流 $\Phi_D$、密度
$j_D=(\Phi_D)_\theta$。外双端定理的真实波准确是
$$
 x_D=\sqrt{\mu_*}\Lambda_D^{1/2}(h\circ\Phi_D),\qquad
 y_D=-\mu_*^{-1/2}\Lambda_D^{-1/2}
                              [j_D(\pi\circ\Phi_D)] .
 \tag{X.21}
$$
负号是该外组件内端的外法向；没有改变原 $\pi$。
$\mu_0(D)/\mu_*\in(1/2,2)$，$q_D=\sqrt7$，
$\mathfrak d,J_0$ 的角乘子及逆在同一小球中，
$\Phi_D^{\pm1}$ 的函数和密度 pullback 在
$H^{\pm1/2}$ 上均有小于4的界。
由 (X.10) 和原角链式法则，(X.9) 与 (X.21) 的双向转换
可保守取 $2^{32}$。这里实际 $\mu_*^{\pm1/2}$ 成对相消，
没有把微小绝对密度误称为1。

下表列出真正顺序和双向费用，包含全部低频与 mean：

| 因素 | 双向 norm 上界 |
|---|---:|
| 原 Airy 波至 balanced 根态，含共同 Green 归一 | $2^{132}$ |
| 唯一 simple 根、真实 graph、物理 fixed strict 端口 | $2^{2468}$ |
| 完整 density 三态至 (X.9) | $2^{444}$ |
| 实际 $(129,2)$ strict 片，所有 Fourier 模 | $2^{1024}$ |
| cut128 的真角、物理密度、波及固定支次序 | $2^{32}$ |

总 bits 小于4101；额外有限直和、Bessel 权等价和单位波常数
远小于剩余余量。因此准确的根至 cut128 波传递 $\mathcal T_X$
满足
$$
 \boxed{\quad
 \|\mathcal T_X\|,\ \|\mathcal T_X^{-1}\|<K_X:=2^{8192}.
 \quad}
 \tag{X.22}
$$
定义根波 $\alpha_X,\beta_X$ 时沿用原完整 Airy 单位及外组件的
外法向，故
$(\alpha_D,\beta_D)^T=\mathcal T_X(\alpha_X,\beta_X)^T$。
与内部 positive 组件相接时使用原规定的反向法向支交换。
由原完整物理 Green 恒等式和上述各精确变换，
$$
 \mathcal T_X^*\mathsf J\mathcal T_X=\mathsf J,\qquad
 \mathcal T_X\mathsf J\mathcal T_X^*=\mathsf J,\qquad
                       \mathsf J=\operatorname{diag}(I,-I).
 \tag{X.23}
$$
第二式由真实 onto inverse 得到；仅第一式不足以代替这一步。
(X.22) 而非 (X.23) 支付正定 norm。

## 5. 普通源、weak 两行、两个 mean 和真实原子

(X.11)--(X.16) 在一般 source 下增加的三态源准确为
$$
 G_1=-\lambda\partial_\theta(\mu^{-1}F^t),\qquad
 G_2=\lambda^{-1}[f-\partial_\theta(F^\theta+dF^t)],\qquad
 g_0=-\lambda_0\langle\mu^{-1}F^t\rangle .
 \tag{X.24}
$$
定义它们在真实 $t$ 上的 vector Radon-measure norm
$$
 \mathfrak S_*=
 \|(G_1,G_2,g_0)\|_{\mathcal M_t
               (H^{-1/2}\oplus H^{-1/2}\oplus\mathbb C)} .
 \tag{X.25}
$$
(X.18) 的 Duhamel 给零初值输出小于 $2^{1024}\mathfrak S_*$。
没有出现 $F^t_t$，没有丢掉高度 mean 的最后一项。
原 Darboux ordinary 源 $f=w_{\rm ref}^2J_0\mathfrak d^{-3/2}e$
给准确第二行
$$
 G_2={a_{\rm phys}^{1/2}w_{\rm ref}^{3/2}J_0
                       \over\sqrt q\,\mathfrak d}\,e .
 \tag{X.26}
$$
其物理径向权须保留；$L^2_t$ 消费另外使用这条真权的
Cauchy--Schwarz，不能改为无权单位源。

若要求某一内部界面上高度跳 $u$ 和 total 通量跳 $v$，
可用完整原子
$$
 F^t=-\mu u\,\delta_{t_0},\quad
 F^\theta=d\mu u\,\delta_{t_0},\quad f=v\,\delta_{t_0}.
 \tag{X.27}
$$
(X.24) 给跳
$(\lambda u_\theta,\lambda^{-1}v,\lambda_0\langle u\rangle)$，
恰是 (X.9) 的真实跳。背景在原接缝连续，使用其同一真迹。
解类是 BV 和单侧迹；齐次连续性不冒用于原子源。

根 collar 的源继续按原 J.34--J.37 的准确 Piola/height
映射，以及 G.30--G.32 的实际 graph 路径与端点修正消费。
可取
$$
 \mathfrak S_R=\int\|\mathcal E_c\|_{L^2\oplus L^2}\,d\xi
       +D_e\mathfrak S_e+\|\mathcal B_g\|_{\mathcal V_{-1/2}},
 \tag{X.28}
$$
并保留选择 bare 迹时所需的真实 weak endpoint 列。
$D_e,\mathfrak S_e,\mathcal B_g$ 均是原根图定理中的实际量，
不是人为端口数据。原有序费用和上表给根至 $D$ 的 affine 项
$\tau_X$：
$$
             \|\tau_X\|_{L^2\oplus L^2}
                   <2^{8192}(\mathfrak S_R+\mathfrak S_*).
 \tag{X.29}
$$
这是明确强源合同。一般只给原
$L^2_tH^s_\theta$ 的粗源仍不自动提供 (X.28)；
混合径向图需要的联合正则性没有被本篇删除。

对当前真实尾标签列，root germ 的 ordinary/weak 体源本来就是0。
$\Gamma^*$ 两列和其它参数仍通过完整 incoming/Cauchy 状态传递；
若其真实体源支集落在本段，则按 (X.24)、(X.28) 计入。
原 $\nu$ 列也按它的真实支集及进入此段的端荷处理。
“本片体源为0”不等于删除整个参数响应列。

## 6. 与实际三阶/正区组件合成，不另选外反射

[真实外双端定理](R119-supplement-actual-positive-cross-port-smoothing-and-exterior-unitary-two-port.md)
(S.18)--(S.24) 已给
$$
 \beta_{D,B}=\mathscr S_{\rm ext}\alpha_{D,B}+b_{\rm ext},
 \qquad \mathscr S_{\rm ext}\text{ onto unitary}.
$$
它完整保留正区四个 DN 块、两个 mean、原 $B$ 的
$H^1/H^{-1}$ 波和真实强源。令
$\mathscr T=\mathcal T_X^{-1}\oplus I_B$，按 incoming/outgoing
次序写为
$\mathscr T=\left(\begin{smallmatrix}A&B_1\\C&D_1\end{smallmatrix}\right)$。
则 $\|\mathscr T^{\pm1}\|<K_X$，且它 onto $J$-unitary。

置
$$
 F=A+B_1\mathscr S_{\rm ext},\qquad
 \mathscr S_{XB}=(C+D_1\mathscr S_{\rm ext})F^{-1}.
 \tag{X.30}
$$
完整 $J$-unitary 恒等式给 $A$ 双向可逆和
$\|A^{-1}B_1\|<1$，从而 $F$ 满射可逆；
对 null graph 使用 $\|\mathscr T^{-1}\|<K_X$ 还给
$\|F^{-1}\|<K_X$。反向相同构造给
$$
 \boxed{\quad
 \mathscr S_{XB}:L^2_{e_X}\oplus L^2_B
           \longrightarrow L^2_{e_X}\oplus L^2_B
       \ \text{onto unitary}.\quad}
 \tag{X.31}
$$
所有块都是真实完整算子，不假定 Fourier 对角或有限秩。
这里没有倒除正区指数小的 transmission。

若反向 affine Cauchy 位移为 $c=(c_1,c_2)$，
则实际 source 输出准确为
$$
 b_{XB}=(D_1-\mathscr S_{XB}B_1)b_{\rm ext}
                       +c_2-\mathscr S_{XB}c_1,
 \qquad
 \|c\|\le K_X\|\tau_X\|.
 \tag{X.32}
$$
因此
$\|b_{XB}\|\le2K_X(\|b_{\rm ext}\|+\|\tau_X\|)$。
原外双端的 $2^{1024}$ 强 physical-source 门与 (X.29)
可统一收在 $2^{24576}$ 内，前提正是各显示的真实源范数。
所有 raw mean、$\Gamma^*$ 两列、weak 端点和外 affine 列都在
(X.32)，不通过选择一个新反射将它们归零。

## 7. 已闭合的外桥与尚需消费的 returned 方程

这给出开放内部的真正 $e_X$ 到原 $B$ 的完整外侧组件。
$e_X$、cut128、三阶根 $C$、原 $B$ 四个不同端点现已逐段接通，
未知高频没有被截去。对齐次问题，这是全空间双端 scattering；
对强 ordinary/weak 源，这是带真实物理单位的 affine 组件。

若进一步消去 $B$ 或接入 body 的原响应，必须使用该响应的
真实端口方程。把 (X.31) 的相应块记为 $R_{XX},R_{XB},R_{BX},R_{BB}$，
准确两行仍为
$$
 \beta_X=R_{XX}\alpha_X+R_{XB}\alpha_B+b_X,\qquad
 \beta_B=R_{BX}\alpha_X+R_{BB}\alpha_B+b_B .
 \tag{X.33}
$$
内部完整逆、mean 商和外端实际条件必须在这两行上联立；
不能由 $\|\mathscr S_{XB}\|=1$ 推出
$I-R_{\rm int}R_{XX}$ 可逆。
原标签权及 source-to-label 映射也要在其实际输入、输出上消费。
这些是下一项真实缺口，不以辅助圆周参数、未付的 smooth inverse
或一个已删除 mean 的外模型替代。
