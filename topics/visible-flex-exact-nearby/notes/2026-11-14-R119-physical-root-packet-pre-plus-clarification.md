# R119 续篇：真实物理根端口低频包到完整中心正型的接线

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对同一当前非径向背景和同一
$\Gamma^*(\mathbf a,\Omega)$，任一真实负窗的左、右物理根端口
到第73--74束中心的完整 Cauchy map，在明确相同的两迹 norm 中
满足
$$
 \|\mathcal C-\mathcal C_0\|_{\mathscr H^5\to\mathscr H^4}
 <2^{12000}J^{22}\delta^{-40}\mathcal N_{i|j}\mathcal X.
 \tag{P.1}
$$
这里恰有一阶角导损失，$\mathcal C_0$ 是同一当前径向参考。
没有把真实端角图设为恒等或声称裸 pullback 同阶小。

如果完整根端口的两条物理输入迹只含
$4\le|m|\le\sqrt B/4$ 和两个 mean，它的真实中心像满足第74束
明确的带外定位门，因而同一 compact 方向对该实际像严格正。
传播后的输出保留全部频率。这个结论提供一条真实、已支付的
物理端口子空间；它尚未证明全网络的每个近核都在该子空间内。
所有 ordinary/weak 源和两条 mean 行继续保留。

## 1. 同一物理两迹与不变的尺度

沿用[第74束](R119-supplement-complete-low-cone-and-explicit-exterior-crossing-form.md)
的全部参数、anchor 盒及 $\mathcal X\le2^{-1048576}$。令
$I_i=[t_-,t_+]$ 为真实整个负分量，$c$ 为原未用 quartic 区间
的中心。四态给
$$
 n_i\le4\mathcal N_{i|j}\mathcal X,\qquad
 \mathcal N_{i|j}<2^{-20010}
                      2^{-(31867/256)(j-8193)}.
 \tag{P.2}
$$
所有实际相交胞元及邻胞已包含在此六项和中。

用材料单位 $\mu_0=w/r$、真实 raw 高度 $h$ 和 total flux $\pi$，
记
$$
 u=\sqrt{\mu_0}h,\qquad v=\pi/\sqrt{\mu_0}.
$$
物理尺度为 $a_{\rm phys}=\rho_{\rm waist}r$；与根证明的物理单位
互换时，同时乘散度密度、total flux 和全部源以
$\rho_{\rm waist}$。当前 fixed-stop 的这个尺度固定。
本文不单独删掉一个 $\rho_{\rm waist}$ 因子。

令 $q(t)=\sqrt{Q(t)}$，定义一组物理、径向、与背景角变量无关的权
$$
 s_m(t)=\big(1+|m|^{4/3}+Q(t)m^2\big)^{1/2},\qquad
 \mathcal Z(t)=
       \big(s(D,t)^{1/2}u,\ s(D,t)^{-1/2}v\big).
 \tag{P.3}
$$
包括 $m=0$，此时 $s_0=1$。两个状态用同一个 $H^s\oplus H^s$
norm，角权为 $(1+|m|)^s$。根端口在准确 $t=t_e$，因此
$Q(t_e)=0$，并未把它移成某个正或负的近似截面。

中心输出采用第74束原 wave 坐标
$$
 Z_m(c)=\left(\sqrt{k_m}u_m,\
 \frac{v_m-(1+Q(c))u_m/2}{\sqrt{k_m}}\right),\qquad
 k_m=\sqrt{7m^2-16},\quad m\ne0 .
 \tag{P.4}
$$
mean 先保完整 $(u_0,v_0)$。为了读取 crossing form，可在每个
截面以 $h_0=0$ 取常物理高度商空间的代表元；flux mean 仍保留。
准确常高度解是 $h=\mathrm{const},\pi=0$，所以这个商与真实传播
相容。完整高度 mean 另由原积分恢复，不把它等同 canonical 零模。

## 2. 一条全频强差恒等式，不含额外径向导数

准确物理系统是
$$
 \begin{aligned}
 u_t&=-\tfrac12(1+Q)u+d u_\theta+A v,\\
 v_t&=\partial_\theta(dv)+Q\partial_\theta(Cu_\theta)
                                    +\tfrac12(1+Q)v,\\
 A&=a_{\rm Jac}\mu_0,\qquad C=c_{\rm Jac}/\mu_0 .
 \end{aligned}
 \tag{P.5}
$$
在同一径向参考 $A=C=1,d=0$。所以完整 generator 差准确为
$$
 \Delta\mathsf A=
 \begin{pmatrix}
 M_d\partial_\theta&M_{A-1}\\
 Q\partial_\theta M_{C-1}\partial_\theta&\partial_\theta M_d
 \end{pmatrix}.
 \tag{P.6}
$$
下右项是 $\partial_\theta M_d$，不能改成 $d\partial_\theta$；
mean 输入在这一行一般会产生非零输出。
共同的 $\mu_0$ 径向对数导数已经消去。对两方程使用同一 (P.3)
后，权的 $s_t$ 项也准确相消。因此没有新增
$Q_t,Q_{tt}$、$A_t$ 或弱源的 $F^t_t$。

以下直接证明完整 Fourier norm，含所有 lag 和两个 mean。
设 $m,n\ne0$、$\ell=1+|m-n|$。则
$$
 s_m/s_n\le\ell,\qquad
 s_n\le(2+q)(1+|n|),\qquad s_n\ge q|n|.
$$
第一式来自 $|m|\le\ell|n|$，同时用于权内的三项。
上下非对角块及两个 drift 块的频率因子分别满足
$$
 \begin{array}{c|c}
 \sqrt{s_ms_n}&(2+q)\ell^{1/2}(1+|n|)\\
 Q|mn|/\sqrt{s_ms_n}&q\ell^{1/2}(1+|n|)\\
 |n|\sqrt{s_m/s_n}&\ell^{1/2}(1+|n|)\\
 |m|\sqrt{s_n/s_m}&\ell^{3/2}(1+|n|).
 \end{array}
 \tag{P.7}
$$
当 $Q=0$，第二块准确为0，不能用一个发散的 $1/q$ 上界。
当 $m=0$ 或 $n=0$，有导数的零因子原样保留；剩余 upper-right
和 lower-right mean 列分别由
$(2+q)\ell(1+|n|)$ 与 $\ell^2(1+|n|)$ 控制。
特别没有对 mean 使用 $|m|^{-1}$。

Peetre 权再付 $\ell^{|s|}$。原完整有理系数在角宽1有
$\|A-1\|_{\mathcal A_1}+\|C-1\|_{\mathcal A_1}
\|d\|_{\mathcal A_1}<2^{12}n_i$；
$\sup_{\ell\ge1}\ell^6e^{-(\ell-1)}<2^{20}$。
因此一次 $\ell^1*\ell^2$ 给
$$
 \boxed{\quad
 \|\Delta\mathsf A_{\rm bal}(t)\|_{H^{s+1}\oplus H^{s+1}
                                        \to H^s\oplus H^s}
           <2^{48}n_i(1+q(t)),\qquad |s|\le4 .
 \quad}
 \tag{P.8}
$$
它是强一阶差，不是同阶小差。参考 Fourier 对角性将在下面
只用于右侧输入传播；实际输出始终不截断。

## 3. 原严格切口之间的真实物理传播

删去两根 $\xi_*=1/64$ collar 后，原物理 strict 区有
$q>1/16$。第70束、原 strict 证明的完整 density 状态
$\mathcal F_{s-1/2}$ 与 (P.3) 的双向转换满足
$$
 \|\mathcal T(t)\|,\ \|\mathcal T(t)^{-1}\|
                    <2^{128}J\delta^{-3},\qquad |s|\le4 .
 \tag{P.9}
$$
说明这个费用的全部项。在物理角先用
$$
 w_d=\sqrt{q/D}\,u,\qquad
 \zeta_d=\sqrt{D/q}\left[v+\frac{T}{\mu_0}u\right],
 \qquad T/\mu_0=
 \frac{\mu}{2\mu_0}(\ell_t-d\ell_\theta).
 \tag{P.10}
$$
物理 $w_d$ 的一阶角导与 $\zeta_d$ 给两 density 行；
非零高度由完整 $\partial_\theta^{-1}$ 恢复，mean 单独取积分。
因为 $s_m\ge q|m|$，且
$s_m\le(2+q)(1+|m|)$，半阶频率比不产生频率损失。
$q_{\max}<2^8\sqrt J\,\delta^{-3/4}$、
$|\ell_{0,t}|<2^{29}J\delta^{-3}$，实际系数的角宽余量给
同一乘子界。所有真实 $H_\sigma$ 及其逆、primitive 和两个
mean 的费用分别不超过原 $2^{20},2^{22}$；相加仍低于128 bits。
这给 (P.9)，不是以裸 pullback 减恒等估计其 norm。

实际 strict Cauchy 在 $\mathcal F_{s-1/2}$ 的双向 norm
小于 $2^{1100}J^5\delta^{-10}$。因而
$$
 \|\mathcal C_{\rm st}(t,s)\|_{H^s_{\rm bal}\to H^s_{\rm bal}},
 \ \|\mathcal C_{0,\rm st}(t,s)\|
                 <K_{\rm st}:=2^{1400}J^7\delta^{-16}.
 \tag{P.11}
$$
参考是准确逐模对角，所以其同一个 norm 界在所有 Sobolev
指数成立，特别在下面右端用到的 $H^5$；这不扩张实际输出
只已支付到 $H^4$ 的窗。

在固定物理 $t$ 上写真正 Duhamel 恒等式
$$
 \mathcal C_{\rm st}-\mathcal C_{0,\rm st}
 =\int \mathcal C_{\rm st}(t,r)
       \Delta\mathsf A_{\rm bal}(r)
                       \mathcal C_{0,\rm st}(r,s)\,dr .
 \tag{P.12}
$$
用 $\int(1+q)dt<2$、(P.2)、(P.8)--(P.11)，得到
$$
 \|\mathcal C_{\rm st}-\mathcal C_{0,\rm st}\|_{H^5\to H^4}
      <2^{3000}J^{14}\delta^{-32}
                              \mathcal N_{i|j}\mathcal X .
 \tag{P.13}
$$
未放宽 bits 为2851。公式同时适用于两个方向；积分方向的
负号不改变此界。没有通过两个不同实际角图分别冻结时间。

## 4. 两个真正 root 端口：height、normal shear 和角图全保留

现在将原物理 $t=t_e$ 接到同一侧的原 strict 切口 $t_*$。
设 $b=|Q_t(t_e)|$，真实根图使用自己的
$\varsigma=\operatorname{sgn}(x/(t-t_e))$。已付完整 quartic
germ 和邻胞费用给
$$
             1<b<2^{19}\sqrt J\,\delta^{-9/4}.
 \tag{P.14}
$$
本节每一个 map 都是完整两状态及两个 mean 的 map。

在 root 本身，准确 $\phi=\theta,\xi_\theta=0,\phi_t=d$，
所以端口没有隐含的角导数：
$$
 h_e=\alpha_e^{-1/2}U_e,\qquad
 \pi_e=\varsigma\sqrt{\alpha_e}
                 (U_\xi-\tfrac12\ell_\xi U)_e .
 \tag{P.15}
$$
这里是齐次场；有源 total 行在第7节加回。
$\alpha_e/(b\mu_0)=D_e^{-1}\upsilon_e^{-1/3}$，
$|\ell_\xi|<9$，而其与参考的差及所需角乘子小于
$2^{32}n_i$。与 canonical
$\widehat s_m=(1+(|m|/b)^{4/3})^{1/2}$ 比较，
(P.15) 的两个方向在 $H^4$ 上均小于 $2^{100}\sqrt b$；
相对于参考的差小于 $2^{180}\sqrt b\,n_i$。
例如 $s_m(0)/\widehat s_m\le b^{2/3}$，逆比至多1；
mean 使用 $s_0=\widehat s_0=1$。shear 项用
$s_m,\widehat s_m\ge1$ 单独支付。

在另一端 $t_*$，用第70束 (P.12) 的准确物理 density/conormal
换元，再用[原 graph 证明](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
的 $\mathcal A_g,\mathcal T_g,\mathcal A_*$。物理 (P.3) 到
完整 graph density 空间的双向 map norm 可取
$$
                 2^{128}b.
 \tag{P.16}
$$
其相对参考的强差，在物理 $H^{s+1}_{\rm bal}\to
\mathcal E_{s-1/2}$ 和反向
$\mathcal E_{s+1/2}\to H^s_{\rm bal}$ 窗均小于 $2^{256}bn_i$。
这可直接由 (P.10) 证明：此处
$1/128<Q<1/32$、$|Q_t|<2b$，故 $|T/\mu_0|<2^{12}b$；
系数差小于 $2^{40}bn_i$。实际角图满足
$\|H-\mathrm{id}\|_{C^8}<2^{32}n_i/b$，用一次参数积分
$\partial_\lambda C_{H_\lambda}
=M_{H-H_0}C_{H_\lambda}\partial_\theta$ 支付完整一阶损失。
密度行的 $H'$ 同时微分。均值按真实 Jacobian 积分，不
另设为0。这些乘积和链式法则费用落在显示的256 bits内。

同一个 canonical 平衡到完整 graph density 的
$\mathcal A_*$ 及逆小于 $2^{20}\sqrt b$。
真正 graph map 是
$$
 \mathcal T_g=\mathcal P_g+\mathcal E_g,\qquad
 \|\mathcal E_g\|<2^{112}bn_i,\qquad
 \|\mathcal P_g\|,\|\mathcal P_g^{-1}\|<2^{20},
 \tag{P.17}
$$
其中 $\mathcal P_g$ 有两条不同的真实 density pullback。
它们与径向参考恒等的强差小于 $2^{80}n_i/b$，来自
$L_\sigma-\mathrm{id}=O(n_i/b)$ 的完整 $C^8$ 预算。
不使用 $\|\mathcal P_g-I\|_{H^s\to H^s}\ll1$。

canonical core 的实际双向 Cauchy 小于 $2^{2185}$，
同阶差小于 $2^{6605}n_i$。把 (P.15)--(P.17) 和它按真实
次序相乘，得到整段 physical root map 及逆
$$
 \|\mathcal C_{\rm rt}\|,\|\mathcal C_{0,\rm rt}\|
                         <2^{2800}b^2 .
 \tag{P.18}
$$
四个物理/graph/core 因子的 bits 和低于2454，$b$ 幂为2。
整个强差的安全统一界是
$$
 \|\mathcal C_{\rm rt}-\mathcal C_{0,\rm rt}\|_{H^5\to H^4}
                         <2^{8000}b^4n_i .
 \tag{P.19}
$$
为明确算子顺序，逐项使用
$A_n\cdots A_1-B_n\cdots B_1
=\sum_k A_n\cdots A_{k+1}(A_k-B_k)B_{k-1}\cdots B_1$。
每一项的右因子全部是径向参考，故可在输入 $H^5$ 上使用
其逐模界；左侧实际因子只在输出 $H^4$ 上使用。
core 差给 $2^{6605+269}b^2n_i$，graph 差至多多一 $b$，
两个端 frame 的强差按 (P.15)--(P.16) 支付。
显示的 $2^{8000}b^4$ 覆盖全部有限和及逆方向公式。
这里没有偷偷把实际闭窗扩到 $H^5$。

本节只穿过同一个已付联合解析 root germ；没有在仅 $C^2$
的径向接缝上作复求值。所有 smallness
$b^2n_i<2^{-512}$、$n_i<2^{-4424}$ 均由 (P.2) 和 (E.1)
逐层严格满足。

## 5. 真物理 root 到原中心的完整强比较

在中心，从 (P.3) 到 (P.4) 及逆都是径向 Fourier 乘子，且
$$
                  \|\mathcal T_c^{\pm1}\|<2^8B^{3/4}.
 \tag{P.20}
$$
这是直接比较 $\sqrt{k_m/s_m}$、$\sqrt{s_m/k_m}$ 及
$(1+Q)/(2\sqrt{k_ms_m})$；其中 $M\ge4$，
$\sqrt B<q(c)<2\sqrt B$，mean 保原两状态。

从任一物理 root 到 $c$ 只需一个 root map 和一段 strict
map。由 (P.11)、(P.14)、(P.18)、(P.20) 及
$B<2^7J\delta^{-3/2}$，完整双向界可取
$$
 \|\mathcal C^{\pm1}\|,\|\mathcal C_0^{\pm1}\|
 <K_{\rm pc}:=2^{8000}J^{14}\delta^{-24}.
 \tag{P.21}
$$
实际指数未放宽前为
$16+9/2+9/8=173/8<24$，$J$ 次数小于9。
此界在实际输出 $|s|\le4$ 成立；径向参考对所有指数成立。

将 (P.13)、(P.19) 以同一有序展开相接，得到 (P.1)。
其两种 $\delta$ 费用分别是
$32+9/2+9/8=301/8<40$ 和
$16+9+9/8=209/8<40$，bits 均低于12000，$J$ 次数低于22。
任一 mean 也在上述完整矩阵内。
这些比较始终固定同一当前 $\Gamma$，不是改变参考相位后
比较两个不同算子。

投到常物理高度商空间时，输入、输出选取代表元的投影在各自
上述 norm 中均为收缩；准确常高度解使商 map 及其逆相容。
所以 (P.1)、(P.21) 也适用于第74束保 flux mean 的完整商空间。

## 6. 一个实际端口子空间进入第74束定位门

在任一物理根端口，取完整两迹数据 $f$，其非零频率满足
$$
                 |m|\le\sqrt B/4 .
 \tag{P.22}
$$
保 flux mean，先取常高度商代表元；任意常物理高度最后加回。
这里对输入两行同时施加 (P.22)，而不对输出作截断。
径向参考 $\mathcal C_0f$ 准确逐模，因此中心
$\Pi_j^\perp\mathcal C_0f=0$。
由 (P.1)，实际 $Z=\mathcal C f$ 满足
$$
 \|Z_>\|_{\mathscr H^4}
 \le D_{\rm pc}B^{5/2}\|f\|_{\mathscr H^0},\qquad
 D_{\rm pc}=2^{12000}J^{22}\delta^{-40}
                                  \mathcal N_{i|j}\mathcal X .
 \tag{P.23}
$$
因为 $1+\sqrt B/4<\sqrt B$，这正是 $H^5$ 输入费用。
完整角漂移造成的相反锥、mean 回填及无限 Fourier 尾都在左边。

同一参考逆给
$$
 \|f\|\le K_{\rm pc}
       [\|Z_<\|+D_{\rm pc}B^{5/2}\|f\|].
$$
实际数据有 $K_{\rm pc}D_{\rm pc}B^{5/2}<1/2$，故吸收后
$$
 \frac{\|Z_>\|_{\mathscr H^4}}{\|Z_<\|_{\mathscr H^0}}
 <2^{20100}J^{39}\delta^{-68}
                               \mathcal N_{i|j}\mathcal X .
 \tag{P.24}
$$
当 $f=0$ 时按连续性读取；非零商数据的分母不为0。
未放宽的 bits 为20019，$\delta$ 次数为 $271/4<68$。

与第74束真正定位阈值比较，准确余项比小于
$$
 2^{32700}J^{81}\delta^{-106}
                                  \mathcal N_{i|j}\mathcal X .
 \tag{P.25}
$$
首层对数小于 $-160000$，以后每层再衰减超过18 bits。
全部原全局接缝因子仍在 $\mathcal N_{i|j}$ 中。
因此同一实际物理包的完整中心像确实满足
$$
 \|Z_>\|_{\mathscr H^4}
 <2^{-12600}J^{-42}\delta^{38}\|Z_<\|_{\mathscr H^0}.
$$
第74束 (E.22)--(E.24) 于是授予这个真实像
$$
                 \mathfrak G_\psi(Z)
                  >\frac{d_\ell}{16}\|Z_<\|_{\mathscr H^0}^2 .
 \tag{P.26}
$$
它对任意输入包内混频、两迹比例、两个实分量及 flux mean 同时
成立。两端 root 的方向号和端口尺度分别使用本身的真实值。

## 7. 完整源与这一步没有自动解决的网络问题

strict 物理原坐标中的完整源对，经 (P.3) 后准确为
$$
 \mathfrak s_{\rm ph}=
 \begin{pmatrix}
 -s^{1/2}(a_{\rm Jac}\mu_0)(F^t/\sqrt{\mu_0})\\
 s^{-1/2}\mu_0^{-1/2}
                [g-\partial_\theta(F^\theta+dF^t)]
 \end{pmatrix}.
 \tag{P.27}
$$
在实际 $L^1_t(H^4\oplus H^4)$ norm 提供此输入时，
(P.11) 给完整有序 Duhamel 费用 $K_{\rm st}$。
它包含真实 $a_{\rm Jac},\mu_0$、两条 weak 列和 mean ordinary
负荷；不含 $F^t_t$。

root 源仍使用原准确 Piola。明确记
$\widetilde f=(f/\mathfrak J)\circ\Psi^{-1}$、
$\widetilde F=(D\Psi F/\mathfrak J)\circ\Psi^{-1}$，则
$$
 F_c=\alpha^{-1/2}\widetilde F,\qquad
 f_c=\alpha^{-1/2}
       \left(\widetilde f-\tfrac12\nabla\log\alpha\cdot\widetilde F\right),
$$
及 canonical 两态
$(-\widehat s^{1/2}F_c^\xi,\
\widehat s^{-1/2}(f_c-\partial_\phi F_c^\phi))$。
真实根图的体源 norm 和两端 normal charge 按原合同另付。
不能从原各向异性 $L^2$ 单独推出混合图上的同阶源 norm。
要求 bare 通量时仍另需 $F^t$ 的两端真实迹。

均值准确满足
$\pi_{0,t}=g_0$、
$h_{0,t}=\langle dh_\theta+a_{\rm Jac}\pi-a_{\rm Jac}F^t\rangle$。
所谓常高度商只用于齐次 crossing form；未删除有源高度常数、
mean flux、电阻积分或端口 mean 匹配行。

本篇把一种明确物理低频输入的真实像接入了共同正型。实际
whole-network 的近核通常由 incoming/outgoing 与正片反馈共同
决定，不自动满足两条 Cauchy 迹都在 (P.22) 的条件。带外物理
端口、不同窗口的共同参数、正片的所有 cross、端图的参数
导数及 source-to-original-label 原像仍须继续处理。
这些缺口不能由径向公共逆乘一个绝对误差跳过，也不能从
(P.26) 直接宣布完整非线性 $\mathcal F$ 可逆。

新增严格预算：
[源码](../scripts/fourfold_physical_root_packet_localization_20261114.py)、
[实际记录](../notes/2026-11-14-R119-physical-root-packet-localization-budget.json)。
