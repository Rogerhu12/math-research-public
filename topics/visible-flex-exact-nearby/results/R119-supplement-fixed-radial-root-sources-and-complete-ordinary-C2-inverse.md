# R119 续篇：固定径向根源的完整两行能量、两端仿射接线与原普通源 C²

2026-11-15，visible-exact / tail_connector。

**状态：解析结论已证。** 本篇接
[完整有源二 jet](R119-supplement-complete-deep-source-particular-jets-and-actual-coordinate-ordinary-inverse.md)
P.1--P.31，关闭其中 ordinary 源必须先给混合根图 norm 的限制。
只在每个相同径向截面上改变角坐标；真实源不作径向—角混合
pullback。所有频率、两个物理 mean、total 通量及 weak 两分量保留。

本篇使用 R119 同一个已经选定的内部根、完整 $\Gamma^*$、五盒
参数与实际背景。R133 根 Cauchy 的正 Fourier 权提供算法参考，
但不移用其 M32 数值或系数门。这里重新给出全部 R119 系数、
源位置到两端的有序公式和常数。最外未覆盖的有限元件仍使用
P.31 的独立真实外源列，不以其编号推断本篇内部 root germ。

## 1. 原物理散度式和仅改变角坐标的真规范

在一个实际内部负根 collar 上，原方程是
$$
 \partial_t p-\partial_\theta(d p+\mu Qv^2h_\theta)
              =f-\partial_tF^t-\partial_\theta F^\theta,
 \qquad p=\mu(h_t-dh_\theta).
 \tag{K.1}
$$
采用
[真实 strict 密度](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
S.5、S.9--S.10 的相同四态，记
$$
 \mu_0={w_{\rm ref}\over a_{\rm phys}}
       ={\varepsilon_s m_jp_*\over\rho r^8},\qquad
 \mu=\mu_0JD^{-3/2},\quad v={\sqrt D\over J},\quad
 {\mu_{0,t}\over\mu_0}=-1-Q .
 \tag{K.2}
$$
真实参数下 $\mu_0,v,D,J$ 均正；线性数据可以复数。
$Q$ 是原径向函数，未因改变角规范而修改。

令归一圆平均为 $\Pi$，$I=\partial_\phi^{-1}(1-\Pi)$。定义
$$
 \eta(t)=\langle v(t,\cdot)^{-1}\rangle_\theta^{-1},\quad
 \phi(t,\theta)=\theta+
       I_\theta\left({\eta(t)\over v(t,\theta)}-1\right),\quad
 \theta=\Phi(t,\phi).
 \tag{K.3}
$$
$\phi-\theta$ 采用原零 mean primitive；
$\phi_\theta=\eta/v$，故每个 $t$ 上是次数1的真实圆微分同胚。
这里从来没有把 $t$ 换成一个依赖角的变量。
写
$$
 u=h\circ\Phi,\quad
 \bar d=\left({\eta d\over v}-\phi_t\right)\circ\Phi,\quad
 \chi=(D^{-1})\circ\Phi,\quad
 \bar\mu=(\mu v/\eta)\circ\Phi={\mu_0\chi\over\eta}.
 \tag{K.4}
$$
特别 $\bar\mu\eta=\mu_0\chi$ 是准确恒等式。

源的同截面 Piola 公式为
$$
 \bar f=\Phi_\phi(f\circ\Phi),\quad
 \bar F^t=\Phi_\phi(F^t\circ\Phi),\quad
 \bar F^\phi=(F^\theta-\Phi_tF^t)\circ\Phi.
 \tag{K.5}
$$
因此 $\langle\bar f\rangle_\phi=\langle f\rangle_\theta$，
且有一个在后面有用的准确消去
$$
             \bar F^\phi+\bar d\bar F^t
                       =(F^\theta+dF^t)\circ\Phi.
 \tag{K.6}
$$
不能只取 $\bar F^\phi$ 而丢掉右边的 $dF^t$。

## 2. 完整两行及真实的两条 mean

在新角中令
$$
 \bar\pi=\bar\mu(u_t-\bar d u_\phi)+\bar F^t,\quad
 p_0=\langle\bar\pi\rangle,\quad
 c={p_0\over\mu_0},\quad
 z={I\bar\pi\over\mu_0\chi}.
 \tag{K.7}
$$
这个 $z$ 是角通量 primitive 除以实际密度，不是 Jacobi 高度。
准确反解为
$$
 \bar\pi=\partial_\phi(\mu_0\chi z)+\mu_0c,\qquad
                      \langle\chi z\rangle=0 .
 \tag{K.8}
$$
$u$ 的 mean 保留在完整第二行；$c$ 是独立实际 total-flux mean。
约束 (K.8) 排除给 $z$ 任加常数所造成的第三个假 mean。

令 $P=1-\Pi$，$r_\chi=\chi_\phi/\chi$。完整方程准确等价于
$$
 \begin{split}
 z_t={}&\bar d z_\phi+Q\eta u_\phi+
               \left(1+Q-2Q(w_{\rm ref}^2U/J)\circ\Phi\right)z\\
       &+\chi^{-1}\langle\bar d_\phi\chi z\rangle
          +Q\eta\chi^{-1}\langle\chi_\phi u\rangle
          +c\chi^{-1}(\bar d-\langle\bar d\rangle)\\
       &+{\chi^{-1}\over\mu_0}
              [I\bar f-P(\bar F^\phi+\bar d\bar F^t)],\\
 u_t={}&\bar d u_\phi+\eta z_\phi+\eta r_\chi z
                 +\eta\chi^{-1}c-{\eta\chi^{-1}\over\mu_0}\bar F^t,\\
 c_t={}&(1+Q)c+\mu_0^{-1}\langle\bar f\rangle .
 \end{split}
 \tag{K.9}
$$
所有平均均在当前 $\phi$ 测度。证明先对
$\bar\pi_t=\partial_\phi(\bar d\bar\pi+\mu_0\chi Q\eta u_\phi)
+\bar f-\partial_\phi(\bar F^\phi+\bar d\bar F^t)$ 应用 $I$。
把 $\langle\bar d(\mu_0\chi z)_\phi\rangle$ 和
$\langle\mu_0\chi Q\eta u_\phi\rangle$ 分部积分，得到所显示两个
rank-one 行。剩下的 diagonal 精确使用
$$
 \bar d\,{\chi_\phi\over\chi}-{\chi_t\over\chi}
 ={D_t-dD_\theta\over D}\circ\Phi
                  =-2Q(w_{\rm ref}^2U/J)\circ\Phi .
 \tag{K.10}
$$
这直接来自原 S.9。没有 $Q_t/Q$，也不产生 $Q_{tt}$。
由推导可知 $(\mu_0\langle\chi z\rangle)_t=0$，
所以初始 (K.8) 在完整有源演化中保持。

## 3. 同一实际 collar 的显式系数门

写原根坐标
$$
 x=\varsigma b(t-t_e),\qquad b=|Q_t(t_e)|,\qquad
                  0\le x\le x_*\le1/32 .
 \tag{K.11}
$$
$x_*$ 是原固定径向 strict 切口对应的值。
[真实根图](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
J.1--J.8 给准确 $Q=xB_0(x)$。
由其显示的 quartic 系数，在此完整区间有
$$
 Q(0)=0,\quad Q_x\ge1/2,\quad0\le Q<1/16,\quad
 b>\delta_j^{-9/4}>2^{200},\quad b\le\lambda_j
                    =2^{32}\sqrt J\,\delta_j^{-9/4}.
 \tag{K.12}
$$
原 fixed cut 还满足 $Q(x_*)>1/128$。以上包含真实两种端根，
$\varsigma=-1$ 时仍由 $x$ 增大指向负区。

以原完整四态上界 $n=4(N_j^c)^\#\mathcal X$ 记非径向量。
S.9--S.10 在根上不除以 $q$ 的前五个界，及 J.8 的完整角域，
给在复角宽 $1/2$ 上的安全界
$$
 \begin{split}
 &|\eta-1|+|\eta_t|+
 \|\phi-\mathrm{id}\|+\|\Phi-\mathrm{id}\|+
 \|\bar d\|+\|\bar d_\phi\|\\
 &\quad+\|\chi-1\|+\|\chi^{-1}-1\|
       +\|\chi_\phi\|+\|\chi_\phi/\chi\|
       +\|2Qw_{\rm ref}^2U/J\|<2^{32}n .
 \end{split}
 \tag{K.13}
$$
每个 norm 均为完整 Fourier Wiener norm；常数径向部分已在左边
明确减去。具体地 $|v-1|,|v_\theta|<2^5n$，
$|v_t|<2^{11}n$，所以 $\eta_t=\eta^2\langle v_t/v^2\rangle$
及 $\phi_t=I_\theta(\eta_t/v-\eta v_t/v^2)$ 先小于 $2^{16}n$。
逆图、$\bar d$ 和 $D^{-1}$ 再在原较宽域使用一次商法则和
真实角 pullback，$2^{32}$ 覆盖全部显示项。
没有用一个没有径向意义的复角平移去更改源。

对 $0\le s\le1026$，U.6 的有限展开和至多1088阶的完整
Fourier moments，给这些小系数的 Sobolev 乘法、primitive
和 transport commutator 共同费用不超过
$$
                        B_sn,\qquad B_s=2^{65584}.
 \tag{K.14}
$$
U.8 的真实 $X$ 和三段 $N_j^c$ 保证 $B_sn<1$；
浅前缀和两个接缝均包含其中。
每个实际同截面角 pullback及逆的 $H^s$ norm小于2。
这后一结论用真实 density transport commutator，
不是声称 $C_\Phi-I$ 同阶小。

## 4. 根向外的完整 Fourier 能量

令物理频率 $\Lambda_m=(1+m^2)^{1/2}$，包括 $m=0$，定义
$$
 y_m=x\Lambda_m^{2/3}/4,\quad
 w_m^2=Q+\Lambda_m^{-2/3}e^{-y_m},\quad
 \vartheta_m=\exp[-(8/b)(1-e^{-y_m})],
$$
$$
 \mathcal M=\operatorname{diag}(\vartheta/w,\vartheta),\qquad
 Z_s=\Lambda^s\mathcal M(z,u).
 \tag{K.15}
$$
由 (K.12)，
$$
 (w^2)_x=Q_x-\tfrac14e^{-y}\ge\tfrac14,\quad
 w\ge\Lambda^{-1/3},\quad w<2,\quad
                    \vartheta^{-1}<2 .
 \tag{K.16}
$$
例如 $Q\Lambda^{2/3}\ge2y$，而 $2y+e^{-y}\ge1$。
因此没有在真根处取一个发散的 $1/\sqrt Q$。

$x$ 方向的径向 principal 部分在此架中准确是
$$
 {\varsigma\eta w\over b}
      \begin{pmatrix}0&1\\1&0\end{pmatrix}\partial_\phi
 -
 \begin{pmatrix}
 0&{\varsigma\eta\over b}
       \Lambda^{-2/3}e^{-y}w^{-1}\partial_\phi\\0&0
 \end{pmatrix}.
 \tag{K.17}
$$
第一项在归一圆 $L^2$ 中 skew-adjoint。
第二项的 norm逐频率不超过
$(2/b)\Lambda^{2/3}e^{-y}$，其能量增长由两行共同的
$$
          \vartheta_x/\vartheta=-(2/b)\Lambda^{2/3}e^{-y}
$$
支付；另有第一行 $-w_x/w\le0$。
符号 $\varsigma$ 不影响这一能量不等式。
没有把 $\sup_m\Lambda_m^{2/3}e^{-x\Lambda_m^{2/3}/4}$
拿到径向积分外再制造一个发散。

为完整支付 $\bar d$ 和非径向反应，直接微分有
$$
 -1/3\le\partial_{\log\Lambda}\log w\le0,\qquad
 -1/3\le\partial_{\log\Lambda}\log\vartheta\le0,
 \qquad
 |\partial_{\log\Lambda}\log\mathcal M_\nu|\le1/3.
 \tag{K.18}
$$
第一式用 $(1+y)e^{-y}\le2y+e^{-y}$；
第二式用 $(16/(3b))ye^{-y}<1/3$。
在第一行两个导数符号相反，故不是把两个绝对值相加。
加入 $\Lambda^s$ 后，完整 kernel ratio由
$(1+|\ell|)^{s+1/3}$ 控制，
transport commutator由
$(s+1)(1+|\ell|)^{s+4/3}|\ell|$ 控制。
对所有 signed lag 与完整 mean行列求和后，(K.14) 即支付它们。
rank-one 行的输出 $\chi^{-1}$ 是常数1加解析小量，
其输入 functional 有原 $\bar d_\phi\chi$ 或 $\chi_\phi$；
故按同一完整 Fourier 和估计，不丢 mean，也不索取未知函数
一点求值。

设
$$
 \mathcal F_s(t)=\mu_0^{-1}\left[
   \|I\bar f-P(\bar F^\phi+\bar d\bar F^t)\|_{H^{s+1/3}}
       +\|\bar F^t\|_{H^s}+|\langle\bar f\rangle|\right].
 \tag{K.19}
$$
乘 $\chi^{-1}$ 的完整费用小于2，$\eta<2$。
(K.9)、(K.14)--(K.18) 于是给
$$
 {d\over dx}\left(\|Z_s\|_2^2+|c|^2\right)^{1/2}
 \le {9\over b}\left(\|Z_s\|_2^2+|c|^2\right)^{1/2}
                     +{4\over b}\mathcal F_s(t(x)).
 \tag{K.20}
$$
径向常数 $(1+Q)$、$\eta c$ 与 $c$ 自身的增长被 $8/b$
覆盖；所有其余同阶项合计小于 $1/b$。
普通源 $F=0$ 时，$I:H^s\to H^{s+1/3}$ 的 norm
为 $17^{1/6}/4<1/2$，所以
$$
                  \mathcal F_s(t)
                    <2\mu_0^{-1}\|\bar f(t)\|_{H^s}.
 \tag{K.21}
$$
这是完整普通源，包括 mean；没有要求它的径向导数。

对任意 $0\le x_0\le x_1\le x_*$，(K.20) 给
$$
 \sup_{[x_0,x_1]}
       (\|z\|_{H^s}+\|u\|_{H^s}+|c|)
 \le2^8\left[
   (\|Z_s(x_0)\|_2^2+|c(x_0)|^2)^{1/2}
       +\int_{t([x_0,x_1])}\mathcal F_s(t)\,|dt|\right].
 \tag{K.22}
$$
根处第一项准确为
$(\|z(0)\|_{H^{s+1/3}}^2+\|u(0)\|_{H^s}^2+|c(0)|^2)^{1/2}$。
同样的有序式处理任意内部 source impulse，收费它的真实
$\Lambda^s\mathcal M$ 加 $c$ 跳；物理端原子不能因此变成 $C^2$。

先在 Fourier Galerkin 系统证明 (K.20)，所有投影与
$\Lambda,\mathcal M,I,\Pi$ 交换。完整 kernel 行列和统一控制
非径向项。弱极限、逐固定模 ODE 和稠密性给全频解；
零源能量给唯一性。极限方程准确推出 (K.8) 的约束保持，
故没有添加第三条 mean。已定义源在固定 $t$ 上可仅径向可积；
ordinary 连续时再使用原散度式取得 classical 正则性。

## 5. 任意根源位置到真实两端：不反用单向能量

只取 ordinary 源时，在每个根 collar 构造真实零根 Cauchy
particular：$h_e=\pi_e=0$，用 (K.9) 沿 $x$ 增大走到原固定
径向 cut。设其完整 strict 平衡状态为 $g_e$。
原 S.14--S.18 的
$(c_d,\alpha,|D|^{-1/2}Z_+,|D|^{-1/2}Z_-)$
在 cut 由 $(u,z,c)$ 准确恢复。下文的 $\mathcal F_s$
专指这个两条非mean行已经乘 $|D|^{-1/2}$ 的 $H^s$ 平衡范数，
不是把原 S.18 的未平衡指数照搬。
cut 的 $1/128<Q<1/16$、$|Q_t|<2b$，
$\Lambda=\mu_0q/D$ 和真实 $T=\mu(\log\Lambda)_D/2$ 给
$$
 \|g_e\|_{\mathcal F_s}
 \le2^{1024}b\sqrt{\mu_{0,e}}\,
                 (\|u\|_{H^{s+1}}+\|z\|_{H^{s+1}}+|c|).
 \tag{K.23}
$$
这里 $\mu_{0,e}=\mu_0(t_e)$，且整个 collar 上
$\mu_0/\mu_{0,e}\in[1/2,2]$。
具体 $\partial_\theta w_d$ 和 $\pi/\sqrt\Lambda$ 各只要半个角导；
$T/\sqrt\Lambda$ 的低模及两 mean 至多再乘 $2^{32}b$。
显示的 $H^{s+1}$ 同时支付半阶、真实角恢复和完整 mean。
原低非mean 自由架的错误 $b^{1/2}$ 界没有被使用。

由 (K.21)--(K.23)，对 $s\le1025$，
$$
 \|g_e\|_{\mathcal F_s}
 \le2^{1040}{b\over\sqrt{\mu_{0,e}}}
          \int_{\text{该 root collar}}\|\bar f(t)\|_{H^{s+1}}\,|dt|.
 \tag{K.24}
$$
积分对任意源位置有效，包括根附近的任意小子区间。
$\bar f$ 是同一个 $t$ 上的纯角 pullback。

下面明确反向因素的位置。令 $U_L,U_R$ 为已有**齐次**真 root
从左右根 Airy两行到各自真实 fixed-$t$ strict cut 的完整映射，
$B_{\rm st}$ 为实际 strict 传递。左、右 collar 的零根 particular
输出分别为 $g_L,g_R$，strict source 为 $g_{\rm st}$。
完整两端关系准确为
$$
 U_R a_R+g_R=B_{\rm st}(U_La_L+g_L)+g_{\rm st},
$$
$$
 a_R=U_R^{-1}B_{\rm st}U_La_L+
          U_R^{-1}(B_{\rm st}g_L+g_{\rm st}-g_R).
 \tag{K.25}
$$
右根的源在其原方程中已有 $\varsigma=-1$；
这里的 $-g_R$ 是匹配产生的另一个准确负号。
没有把 (K.22) 当成反向耗散。

$U_R^{-1}$ 和 $U_R^{-1}B_{\rm st}$ 使用
[完整负 word](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
W.26、U.6--U.11 的完整齐次连续子乘积；所需的
1025阶按 P.§7.2 已显示的1030阶有限展开和1088阶 moments重付。
其在所需窗中的 norm不超过 $2^{8192}\lambda_j^{12}$。
所含 graph 是齐次 map：仅作用已给的 fixed-cut 数据，
没有取未知 source 在一条混合曲线上的迹。
最后 W.43 的真实 $B^{-1},DB^{-1}$ 各小于2，给完整散射仿射列。
因此所有 source到两根及两输出的费用都在 (K.24)--(K.25) 内；
两条 mean、真正反向因素与 half-order架均未遗漏。

对 weak 源，(K.19)--(K.22) 原样成立，但 root Airy架使用 bare
通量时须先把实际 $\bar F^t|_e$ 加入初始 total data，并在 cut
减去相应 bare/total 向量。正是 P.6/P.17 的真实弱端列。
仅有 (K.19) 的积分 norm不提供这两个端迹，故不把它们设为0。

## 6. 同固定径向源的胞内物理二 jet

对 ordinary 零根 particular，(K.22) 在 $s=8$ 给
$(u,z,c)$ 的完整角 norm。
回原角后，一阶径向导数使用准确的
$$
 h_t=d h_\theta+
 \left[\eta z_\phi+\eta(\chi_\phi/\chi)z
                              +\eta\chi^{-1}c\right]\circ\phi .
 \tag{K.26}
$$
没有二次微分一个含 $\sqrt Q$ 的角图。二阶径向导直接使用
D.22 的原 raw 方程，其右边是 $f/\mu$；
在此根域 $Q<1/16$、S.9 给的实际 $a_1,a_2$ 和所需角导
均小于 $2^{64}$。这些系数不含 $Q_t$。

令 $H=\sqrt{\varepsilon_s/\rho}\,h$。
对第 $j$ 胞各根定义完全已知的 ordinary 费用
$$
 \begin{split}
 \mathfrak Q_e={}&
 b\sqrt{\mu_{0,e}}\int\mu_0^{-1}
                      \|\bar f\|_{H^{10}}\,|dt|\\
 &+\sqrt{\varepsilon_s/\rho}\left[
       \int\mu_0^{-1}\|\bar f\|_{H^{10}}\,|dt|
                    +\|f/\mu\|_{C_tH^4}\right].
 \end{split}
 \tag{K.27}
$$
(K.23)--(K.26) 给 root particular 二 jet和其cut drive的完整
共同上界 $2^{2048}\mathfrak Q_e$。
所有规范高度尺度都显示在 (K.27)，不设为1。

以这些 $\mathfrak Q_e$ 取代 P.17 的 root/graph 源项，
strict 和完整 positive 的 ordinary 项仍按 P.11--P.16 取值，
记得到的总和为 $\mathfrak P_j^{\,t}$。
这是一个新的、只含 fixed-$t$ 源的费用；
没有宣称它等于或控制旧混合图的 $\mathfrak P_j$。
(K.25) 的实际接线和 P.18 的同一 strict/physical重建给
$$
 \|H\|_{C^2(I_j)}
 <2^{131072}J^{12}\delta_j^{-32}
                     (A_j^{\rm in}+\mathfrak P_j^{\,t}).
 \tag{K.28}
$$
在正型分量仍是完整双端零迹 particular加真实齐次高度，
没有新加边界条件；共同常高度和两个 total outward mean保留。

## 7. 原 fixed-$t$ 普通源空间及全层收费

保持 P.21 的原单位
$N=\varepsilon_s m_jp_*^2e/(12r^{10})$ 和 P.22 的全部真实
$\zeta_j$。定义
$$
 \mathcal S_t=
  \sup_{j\ge129}{\delta_j^4\over\zeta_j}
             \sup_{t\in I_j}\|N(t,\cdot)\|_{H^{1026}},
 \qquad f=w_{\rm ref}^2JD^{-3/2}e,\quad F=0.
 \tag{K.29}
$$
相邻两层按真实 source位置加入常数，未改变 $\zeta$ 的定义。
要求所需有限片上 $N$ 连续；不要求任何 $1026$ 阶径向导数。

本篇所有角图保持 $t$，其 $H^{1026}$ norm小于2。
由 $p_*\ge\delta/2$、$r\le2$，
$\|e\|_{C_tH^{10}}<2^{32}\zeta_j
(\varepsilon_s m_j)^{-1}\delta_j^{-6}\mathcal S_t$。
$\mu_{0,e}/\mu_0<2$，真实 collar 长度 $<1/(32b)$，
以及原 C.2 的 $m_j=\delta_j^6$（浅层）或
$m_j=\delta_{4096}^{3/2}\delta_j^{9/2}$（深层），均满足
$m_j\le\delta_j$，给
$$
 \mathfrak P_j^{\,t}
 <2^{8192}\sqrt{\rho\varepsilon_s}\,
                         \zeta_j\delta_j^{-7}\mathcal S_t.
 \tag{K.30}
$$
例如 (K.27) 第一项由
$f/\sqrt{\mu_0}
 =\varepsilon_s\sqrt{\rho\varepsilon_s}\,
 m_j^{3/2}p_*^{3/2}r^{-10}JD^{-3/2}e$
和 collar 的 $b^{-1}$ 准确抵消得到；
$m_j^{1/2}p_*^{3/2}\le2^{192}\delta_j^{-1}$。
另两项使用 P.25 的准确 $f/\mu$，不需根图 source producer。

同样，(K.24) 用 $f=12\varepsilon_s m_jr^{-4}JD^{-3/2}N$
后给 root cut 列至多
$2^{4096}C_{\rho,\varepsilon}\delta_j^{-1/2}
 \|N\|_{C_tH^{1026}}$，其中
$C_{\rho,\varepsilon}=\rho+\varepsilon_s+2\sqrt{\rho\varepsilon_s}$。
乘 (K.25) 的完整剩余 word，最坏参数幂
$\lambda^{12}\delta^{-1/2}$ 比 P.28 的
$\lambda^{13}\delta^{-1/2}$ 更小。
strict、positive source不改，所以原 P.28--P.30 的更宽界完整保留：
$$
 \|\widehat g_j^{\rm body}\|_{H^{1025}}
   <2^{262144}J^{16}\delta_j^{-32}
         C_{\rho,\varepsilon}\|N\|_{C_tH^{1026}},
 \qquad
 \mathcal G_{\rm body}
   <2^{1600000}\varepsilon_s C_{\rho,\varepsilon}\mathcal S_t.
 \tag{K.31}
$$
这里仍逐一消费所有129--8192浅前缀。
两权的浅段负幂为 $105.25$、$69.78125$，
深段正幂为16、$1647/32$，全 $J^{4189}$ 与
$\delta_{8192}^{-485/4}$ 因子按已付 P.30 原样保留。

由 (K.30)，$wF^{-2}\mathfrak P^{\,t}$ 的全深平方和仍小于
$2^{430000}\varepsilon_s C_{\rho,\varepsilon}\mathcal S_t$。
D 的完整 source-space唯一性识别同一个已有逆：
不是新造一个可能不同的物理解。故在真实通量兼容
$\mathcal L_a k=0$、指定物理高度 gauge 和 P.31 的相同外源下，
$$
 \boxed{\quad
 \|H-\lambda\|_{C^2_{r,\theta}(I_j)}
 <2^{3400002}J^{20}\delta_j^{22}
   \big(\mathcal G_{\rm ext}
           +\varepsilon_s C_{\rho,\varepsilon}\mathcal S_t\big).
 \quad}
 \tag{K.32}
$$
不兼容时仍保原唯一辅助荷，不偷偷改变 mean方程。
原 ambient Cartesian尺度仍为
$2^8\sqrt{\rho/\varepsilon_s}\max(1,\rho^{-2})$。
连续 ordinary源在真实接缝满足原散度匹配，
所以整个平端的二阶延拓与 P.20 相同。

## 8. 从原解析普通源 norm 到本篇有限阶输入

这里可以消费一个真正原定义的源 norm，而不移换名字。
[强全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
U.2 的 $\zeta_j$ 正是 P.22；
$\tau_{128}=5177/400$，故 $\sigma=\tau_{128}-1>1$。
[控制 profile 完整源](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.43--C.47 的原 ordinary norm为
$$
 \mathcal S_{2,\beta}
 =\sum_{m\in4\mathbb Z}\sup_j
       {\delta_j^4\over\zeta_j}e^{|m|(\sigma+\beta)}
                      \sup_{t\in I_j}|N_m(t)|,\qquad\beta\ge0 .
 \tag{K.33}
$$
包括 $m=0$。三角不等式及完整 signed Fourier和给
$$
 \mathcal S_t\le
   \sup_{x\ge0}(1+x)^{1026}e^{-\sigma x}\,
                   \mathcal S_{2,\beta}
                  <2^{16384}\mathcal S_{2,\beta}.
 \tag{K.34}
$$
例如 $\sigma>1$ 时 $(1+x)^{1026}e^{-x}\le e\,1026!$，
$1026!<2^{11\cdot1026}$ 已足够。
因此本篇确实得到原固定径向 ordinary源的完整有限阶逆与物理
平端 $C^2$，不需要另给 P.22 的混合根图 source norm。

这个 source embedding 是单向的。
输出是已明确的有限 Sobolev/强层状态及物理 $C^2$，
没有由 (K.34) 推断输出标签属于原 $\ell^1_{224}$。
所有原两 $\Gamma^*$、metric weak列和独立外帽源仍保其真实
source合同；(K.19) 可直接消费它们的 fixed-$t$ 两分量及mean，
但要求 bare端口或 classical二jet时仍须给真实弱端迹和
P.3 的普通分布密度。moving/full-$\delta$ 帽转授、真正 $\nu$
Schur及非线性闭合也不由本篇自动得到。

全部结论为显示恒等式、实际旧核与解析角费用的演绎；
没有新增数值实验或重算任何旧科学源。
