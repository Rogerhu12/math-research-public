# R133：完整四重周期帽—长段图与真实 B 均值反馈

2026-11-15，visible-exact / tail_connector。

**状态：已证明的解析接口，原完整数值预算复用。** 本篇在原真实旋转正帽
$L_0=3/2\le r\le R=25/8$ 和同一实际有限长径向段上，取消
[周期帽—长段接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
中的共同偶反射限制。数据包含完整实 $4\mathbb Z$ 模；在一个固定非径向背景处，
允许所有四重周期变化方向。原平均 $B$ 行不被设零，而采用长段准确输出。
其额外 $w_R^2$ 因子使新增反馈严格可收缩。

本篇完成这个实际接口及其完整 Jacobi 端口。它不从 fixed-$C_R$ 的弱根逆
推导原强标签可达性，也不消去 waist 的平均 $B$ 条件、标量 $\nu$ 行或最终
nonlinear tail residual。所有 source、独立 mean 高度和原物理单位均保留。

## 1. 对象、真正输入空间和原数据身份

使用原 R133 全参数旋转目标，$\nu$ 的 compact metric bump 在
$r\ge .18$ 准确为零；因此它不直接改变本篇帽和长段的 intrinsic coefficients。
保留原 $|\eta|\le10^{-9}$ 区间、全部 primitive 尾以及完整真 $q_m$ regular
参考线，不换用有限配点或零反射近似。

记 $C=C_{\rm ref}+c$、$C_{\rm ref}<0$，$\ell=K/C_{\rm ref}^2>0$。
原加权帽空间为
$$
 W_m(r)=\left({a(r)\over a(L_0)}\right)^{3/2+|m|/128},
 \qquad
 \|U\|_{\mathcal X}
 =\sum_{m\in4\mathbb Z}\left[
 \sup_r{|\widehat B_m(r)|\over W_m(r)}
 +\sup_r{|c_m(r)|\over W_m(r)}\right].
 \tag{B.1}
$$
这是逐 Fourier 系数先取径向 supremum 的完整 Banach 空间。
令
$$
 \sigma={1\over128}\log{a(L_0)\over a(R)},\qquad
 \zeta=c_{\ne0}(L_0),\quad
 \|\zeta\|_{A^0}\le6.600816124\cdot10^{-5},\quad\zeta\in A^2,
$$
$$
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60},\quad
 r_Z=10^{-9},\quad r_f=10^{-8},\quad
 \rho={1\over2500},\quad F=r_f+2^{-60}.
 \tag{B.2}
$$
$\zeta,f_B$ 任意实四重周期，未要求共同反射，也未要求有限角支集。
$A^2$ 的有限性保证到内边界的强二阶角正则；其范数无需小于上述 $A^0$ 上界。
非zero高度用齐次 $M^2$ 权，$M=|m|\ge4$；mean 高度独立。

[真实加权帽](R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)
S.5--S.14 与
[完整驱动帽](R133-supplement-complete-nonzero-centred-cap-with-interface-jumps.md)
N.1--N.7、N.13--N.17 给
$$
 \begin{gathered}
 H_C<2.059751811,\quad H_D<69.189285,\quad K_Q<89.930493,\\
 K_D<1.051862,\quad K_0<.293223,\quad
 C_*>.1705338016608,\quad \Lambda<1.097170317,\\
 1.7262957358\cdot10^{-6}<W_0(R)<1.758698709\cdot10^{-6}.
 \end{gathered}
 \tag{B.3}
$$
这些核是逐 signed $m$ 证明的完整 Fourier 核；原驱动帽明确保留
$B_0(R)$ 这一独立端口。其适用性不是由反射子空间的逆猜测出来。

具体说，令 $b_m=i\operatorname{sgn}(m)B_m$、$d_m=b_m+q_mc_m$。
非线性始终是物理
$$
 Q(B,c)={B^2+\ell c^2\over C_{\rm ref}+c};
 \tag{B.4}
$$
不能将其中 $B^2$ 换成 $b^2$。$B_0$、$c_0$ 的准确方程为
$$
 B_0'=-2\beta B_0,\qquad
 c_0'=-\beta(\ell+1)c_0+\beta Q_0.
 \tag{B.5}
$$
两行均从给定右端值向内解。除去反射限制后，(B.4) 的完整卷积、
各非zero正核及 (B.5) 完全相同。

## 2. 长段的全四重 Dirichlet 解与不能遗漏的径向角规范

[实际长径向 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
D.6--D.25 的收缩在完整复 Fourier 代数上成立。其 mean 小根
$\mu_t(h)$ 由原 holonomy-one 方程决定，不以反射为前提。
由 (B.2)，全部 $2F$ Cauchy 圆盘均落在原 $2^{-25}$ 数据域。
因此真正 $h$ 及 mean 高度满足
$$
 \|h\|_{\mathcal Y_\sigma}<6F,\qquad
 v_0(t)=\lambda+\int_0^t a(s)w(s)\mu_s(h)\,ds .
 \tag{B.6}
$$
非mean、mean 源和两端有限长反射均与原定理相同。

需要另说明原“反射固定角规范”在一般数据上的替代。
在真实数据上，水平 metric
$\widehat g=g-dZ^2$ 严格正定；完整 Darboux 方程使它平坦。
取原 Darboux 重建所用、与径向参考同向同 homotopy 的四重周期正 coframe，
复记为 $\eta$，按
$d\eta=-i\omega\wedge\eta$ 定义平面连接。
平坦性给 $d\omega=0$，原 mean 小根给
$\int_0^{2\pi}\omega_\theta\,d\theta=2\pi$。
故可在圆周的 universal cover 上取
$$
 d\vartheta=\omega,\qquad
 \vartheta(t,\theta+2\pi)=\vartheta(t,\theta)+2\pi .
 \tag{B.7}
$$
固定一个点的 $\vartheta$ 后，径向规范由同一 $\omega_t$ 积分。
尤其不能在每个 $t$ 重新令角常数为零而漏掉
$\partial_t\langle\vartheta-\theta\rangle=\langle\omega_t\rangle$。

因为连接和原 coframe 都是四重周期，
$\vartheta(t,\theta+\pi/2)-\vartheta(t,\theta)=\pi/2$。
于是闭合复一形式 $e^{i\vartheta}\eta$ 的四个 quarter 周期积分分别相差
$1,i,-1,-i$，其完整平移周期准确为零。它在 cylinder 上是 exact，
积分得到真正单值的水平位置。连同 $Z$，这构造实际周期 $C^2$ 浸入，
不需要共同反射。实际接合之前，不把单独的驱动曲率帽称为周期浸入。

此处只授完整位置和 frame 的周期性及局部 $C^2$ 重建。最终全局嵌入、
固定位置标记和 reach 仍须按原几何定理消费真实误差，未从 (B.7) 自动取得。

## 3. 真实 B 均值：精确消一阶项后再估计

在准确外端，保留原
[物理曲率公式](R119-supplement-Codazzi-boundary-from-actual-regular-tail.md)
C.4--C.10：
$$
 \begin{gathered}
 P=f_{*,\theta},\quad U=f_{*,\theta\theta},\quad
 \mathcal K=\mu(h)+2f_*+h_t(L),\quad V=\mathcal K_\theta,\\
 D=1-w_R^2(2\mathcal K+\mathcal K^2+EP^2),\qquad
 J=1+\mathcal K+EU,\\
 B=\chi{V-P\over\sqrt D},\qquad
 C=-\chi{J\over\sqrt E\sqrt D}.
 \end{gathered}
 \tag{B.8}
$$
$\chi=w/a$、$E=1+w^2$ 及所有 outward 方向均是原物理量。
原实际门有 $w_R<1/800000$、$\chi<1/5$，
以及 $N=\|P\|+\|\mathcal K\|+\|U\|+\|V\|<4\|h\|<24F$。

完整 signed Fourier mean 准确有 $\langle V-P\rangle=0$。因此
$$
 b_0^{\rm long}
 =B_0(R)
 =\chi\left\langle(V-P)(D^{-1/2}-1)\right\rangle .
 \tag{B.9}
$$
这是一般四重周期数据的真实输出；本式未给出将它设零的权限。

令 $x=w_R^2(2\mathcal K+\mathcal K^2+EP^2)$。
在原完整复球中 $\|x\|<3w_R^2N<1/4$，
Binomial 级数给 $\|(1-x)^{-1/2}-1\|\le\|x\|$。
于是
$$
 |b_0^{\rm long}|
 <{3\over5}w_R^2N^2
 <2^9 w_R^2F^2
 <2^{-30}F^2
 <q_BF^2,\qquad q_B=2^{-28}.
 \tag{B.10}
$$
最后使用 $w_R^2<2^{-39}$。这里没有对未知大角导取样，也没有减两个
独立上界来制造抵消；均值一阶项在 (B.9) 先准确消去。

(B.10) 是同一完整复数据球上的二次界。
对两 Dirichlet 数据取实际半径 $F$ 的 Cauchy 圆，得
$$
 \|D b_0^{\rm long}\|_{\partial\to\mathbb C}
 \le4q_BF .
 \tag{B.11}
$$
$\partial$ 是原两端 $\dot A^2_\sigma$ 和范数；
这是完整 mean functional，作用于所有 signed 模。

后文使用其物理 $L^2$ 导数时必须另付 module。
[完整 L2 外图](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
L.1--L.7 已给真正平方零 Banach 代数
$\mathfrak A\oplus\varepsilon\mathfrak M$：
背景为逐系数径向 sup 后 $\ell^1$，方向为相同 sup 后 $\ell^2$，
乘法 $(a,x)(b,y)=(ab,ay+bx)$，norm 为两项之和。
全部 mean 读取、Binomial 级数、真实 holonomy 根，以及逐模
$32$ Green 和 $5/3$ 两端 lift 都在该代数中有相同界。
故 (B.9)--(B.10) 逐项在此代数中仍成立。
给一个 $\dot H^2$ 单位方向，取平方零分量的复幅度 $|\varepsilon|\le F$；
完整输入 norm 不超过 $2F$，输出的方向系数因此不超过
$q_B(2F)^2/F=4q_BF$。
这重新证明了 (B.11) 的
$\dot H^2\oplus\dot H^2\to\mathbb C$ 版本，
没有从 $A^0$ 导数范数直接推 $L^2$ 方向权限。
同一 module 的逐频 $\mathcal L_C^{-1}$ 和真 $\Phi$ 方程又给
(B.13)--(B.14) 的 $L^2_{\ne0}\to\dot H^2$ 版本。
因此 (B.17) 也是真实物理 $L^2_{\ne0}\to\mathbb C$ functional 界。

## 4. 同一个 C_R 逆，新增的 mean 列不改其定义

设 $Z=(C-C_{\rm ref})_{\ne0}(R)$。原实际
$C_R\mapsto f_*=\Phi(Z,f_B)$ 仍由完整
$$
 f_*=\mathcal L_C^{-1}
 [Z-\chi\sqrt E\,S_Lf_B-\mathcal R_C(f_B,f_*)]
 \tag{B.12}
$$
定义。$\mathcal L_C^{-1}$ 的同宽范数小于9，
$\|\mathcal R_C\|\le2^{12}F^2$；全部非zero $M\ge4$ 保留。
原 M.16--M.19 因而给
$$
 \|\Phi\|_{\dot A^2_\sigma}<r_f,\qquad
 \|D_Z\Phi\|<J_f:=9.013290638 .
 \tag{B.13}
$$
它们的证明只用完整代数与逐 signed 模核，未使用反射删除任何项。

为明确独立另一端列，也可直接微分 (B.12)：
$$
 \|D_{f_B}\Phi\|
 \le{\epsilon_s+\lambda_f\over1-\lambda_f}
 <{1\over256},\qquad
 \lambda_f=9\cdot4\cdot2^{12}F<.001474561,\quad
 \epsilon_s=2e^{-6L}.
 \tag{B.14}
$$
原 $L>2^{24}$，故 $\epsilon_s<2^{-100}$ 足够。
这是同一全频反射加 nonlinear 列的界；未将 $f_B$ 置零。

现在将真正三个右端输出全部定义为
$$
 \begin{aligned}
 d_m(Z,f_B)&=i\operatorname{sgn}(m)B_m^{\rm long}+q_m(R)Z_m,\quad m\ne0,\\
 b_0(Z,f_B)&=b_0^{\rm long},\\
 c_0(Z,f_B)&=C_0^{\rm long}-C_{\rm ref}.
 \end{aligned}
 \tag{B.15}
$$
原 M.20--M.22 的 $e_d,e_0,L_d,L_0$ 不变：
$$
 \begin{gathered}
 \|d\|<1.638400001\cdot10^{-12},\qquad
 |c_0|<2.048000001\cdot10^{-13},\\
 \|D_Zd\|<.005906951,\qquad
 \|D_Zc_0\|<.000738369 .
 \end{gathered}
 \tag{B.16}
$$
新增且准确保留的第四行满足
$$
 |b_0|\le e_B:=q_BF^2<2^{-80},\qquad
 \|D_Zb_0\|\le L_B:=4q_BFJ_f<2^{-49}.
 \tag{B.17}
$$
首界用 $F<2^{-26}$；末界用
$F<(7/10)2^{-26}$、$J_f<10$ 和 $4\cdot7\cdot10/10=28<32$。
对独立 $f_B$，
$$
 \|D_{f_B}b_0\|\le4q_BF(1+1/256)<2^{-25}F .
 \tag{B.18}
$$
$B_0$ 的实际值和导数都保留，不用它们的小上界冒作精确零。

## 5. 在完整帽空间同时关闭三个右端反馈

完整驱动帽的 mean $B$ 右端列在 (B.1) 中的范数是
$|b_0|/W_0(R)$：其加权方程
$\bar B_0'=-(2+3/2)\beta\bar B_0$ 从右端向内有核不超过1。
其余列为原 $H_D\|d\|/W_0(R)$ 和 $|c_0|/W_0(R)$。
因此在帽球 $\|U\|_{\mathcal X}\le\rho$ 中令
$Z_U=c_{\ne0}(R)$，并使用
$$
 \mathcal T(U)=\mathcal H_C\zeta+
 \mathcal H_D d(Z_U,f_B)+
 \mathcal H_{B0}b_0(Z_U,f_B)+
 \mathcal H_{C0}c_0(Z_U,f_B)+\mathcal G_QQ(U).
 \tag{B.19}
$$
这里 $\mathcal H_D$ 是真正输入列，而非仅其范数 $H_D$；
三个右端列使用完全相同的物理端点与 $q_m$。

所有 $\|U\|\le\rho$ 都有
$\|Z_U\|_{A^0_\sigma}\le W_0(R)\rho<7.034794836\cdot10^{-10}<r_Z$，
所以 (B.12) 在整球中合法。原实际球像 M.24 连同 (B.17) 给
$$
 \|\mathcal T(U)\|
 <.000294537492+{2^{-80}\over W_0(R)}
 <.000295<\rho .
 \tag{B.20}
$$
(B.2) 采用原 M.24 已付的完整入口上界 $6.600816124\cdot10^{-5}$，
因此球像覆盖原 scientific 成员及该全 $4\mathbb Z$ 输入球；
这里没有借旧某个中心的实际小输出替任意新输入支付球像。

在同一 norm 中，端点评价贡献的 $W_0(R)$ 与右端 lift 的
$W_0(R)^{-1}$ **准确相消**。完整导数因而满足
$$
 \begin{aligned}
 \|D\mathcal T\|
 &\le .464505257+
 69.189285\cdot.005906951+.000738369+2^{-49}\\
 &< {9\over10}.
 \end{aligned}
 \tag{B.21}
$$
这可用已付有理上界逐项比较：后三项小于 $.410$，前项小于
$.465$，总和小于 $.875+2^{-49}<.9$。
没有多收或漏收 $W_+/W_-$；没有把 long 的长度乘入正核质量。

Banach 收缩给 (B.19) 唯一完整 $4\mathbb Z$ 小解。
它和 (B.12) 在同一真实 $Z_U$ 上求值，故全部非zero $B,C$、
$B_0$ 与 $C_0$ 在 $R$ 准确匹配。$C$ 保持不为零，所以
$A=(K+B^2)/C$ 也准确一致。

由第2节的真正周期长段，在一点对齐位置和 Euclidean frame，
再用[完整物理迹匹配](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)
M.3--M.7 向内重建，帽也成为真正周期 $C^2$ 浸入。
输入 $A^2$ 时，原完整角平移差商和 $(I-D\mathcal T)^{-1}$ 给两次强角导；
所有 curvature means 仍在方程中。没有将逐模光滑当完整 $A^2$ 收敛。

在原共同反射数据上，准确 $b_0=0$，同一个收缩唯一性把本篇解
识别为原 M/U 图。因而既有成功 native 的背景身份不变；
新结论是该同一背景周围的完整方向扩张，未重选科学候选。

## 6. 完整线性源与真实 mean 外列

在本篇实际联合解处微分 (B.19)。由 (B.21)，
$$
 \|(I-D\mathcal T)^{-1}\|_{\mathcal X\to\mathcal X}<10 .
 \tag{B.22}
$$
任意已付帽源 $s_{\rm cap}$、输入 $\delta\zeta$、
独立物理 Robin/mean 荷 $(e_D,e_B,e_0)$ 及原 long particular
均须先形成完整右边，再乘这个同空间 inverse。一个明确的合同是
$$
 \|\delta U\|_{\mathcal X}
 \le10\left[
 H_C\|\delta\zeta\|+
 {H_D\|e_D\|+|e_B|+|e_0|\over W_0(R)}
 +\|\mathcal G_{\rm vec}s_{\rm cap}\|_{\mathcal X}
 +\|\mathcal H_{\rm long}s_{\rm long}\|_{\mathcal X}
 +\|\mathcal H_{f_B}\delta f_B\|_{\mathcal X}
 \right].
 \tag{B.23}
$$
这里的 source 项以真实 Green/lift 后的 $\mathcal X$ norm 读取；
它不是新宣称任意原源范数都已连续进入这个空间。
$\mathcal G_{\rm vec}$ 保普通 pair 源、角散度源、全部 jumps 与两 mean；
不能拿 $K_Q$ 代替一般 pair 源费。原 S 的加权核或 N 的未加权核
必须在各自真正源域使用，不跨空间免费转授。
没有把任意 $L^2$ 径向源命名为 coefficientwise supremum 输入，
也没有从内体源给裸 weak 边界迹。
每个 long 源须先经过其准确 Dirichlet particular、
$D\Phi$、两曲率输出和 total/bare 通量转换。

例如源为零、只改变内侧 $\zeta$ 时，
$$
 \|D_\zeta U\|_{\mathcal X}<32,\qquad
 \|D_\zeta Z_U\|_{A^0_\sigma}
 <32W_0(R)<2^{-14}.
 \tag{B.24}
$$
$D_{f_B}$、$D_\eta$、$D\Gamma^*$ 通过相同完整式；
$\nu$ 的直接 intrinsic cap 列为零是其真实 compact support 的结果，
但 $D_\nu\zeta$、$D_\nu f_B$ 和原 body/source 列均不得删除。
若某参数还改变物理尺度、切口或 long 系数，则先加入它们的真实导数，
不以本篇 fixed-coefficient 公式省略。

所有实际高度与 frame 输出仍按 (B.6)、原 M.26--M.27 恢复。
两个 mean curvature 不取代 mean 高度，固定一个整体高度 gauge
也不消去实际两端高度差。

## 7. mean B 的守恒量与仍需满足的 waist 行

由完整 Codazzi 方程，不作反射假设就有
$$
 (a^2 B_0)'=0
 \tag{B.25}
$$
于每个真实无源径向段。因此本篇联合解的内侧 mean 是准确的
$$
 B_0(L_0)={a(R)^2\over a(L_0)^2}\,b_0(Z_U,f_B),
 \qquad {a(R)^2\over a(L_0)^2}<2^{-25}.
 \tag{B.26}
$$
这是一个真实外响应行，不能用“小于某数”改成零。
若最终 body 的腰条件要求 $B(0,\theta)=0$，则其 $B_0$ 输入为0；
若从真正平盘通过全部已匹配尾段传播，也得到零守恒量。
在这些完整物理解上，必须且只需另满足
$b_0(Z_U,f_B)=0$。本篇未用尚未解的这一条件循环证明 (B.19)。

有物理 mean 源或 jumps 时，准确改为
$$
 [a^2B_0]_{r_1}^{r_2}
 =\int_{r_1}^{r_2}a^2(F_B)_0\,dr+
   \sum_i a(r_i)^2[j_B]_0 .
 \tag{B.27}
$$
端点方向沿同一物理 $r$ 读取。该行和 Z 篇的 Darboux
mean total-flux 兼容在完整几何转换前不能互相改名；
实际转换若使它们等价，仍须证明对应的 Noether 恒等式及源单位。

## 8. 当前实际 M32 物理帽的独立 B0 列如何关闭

[当前全模物理帽 Green](R133-supplement-actual-final-all-mode-physical-cap-Green.md)
C.19--C.28 已给当前 ac1d5b98… 同一物理中心上的全模连续 inverse，
其中 $B_0(R)$ 一直是独立输入，未被省略。
它使用真 $C_R$ 外图的 $d,c_0$ 导数，完整反馈小于 $.820523$；
其未闭 $B_0$ 输入增益为1。

在本篇对应的外输入小球，增加完整
$\delta B_0(R)=D_Zb_0\,\delta C_{\ne0}(R)+e_B$
后，额外反馈至多 $L_B<2^{-49}$。所以
$$
 \chi_{\rm all}<.820523+2^{-49}<.821<1,\qquad
 (1-\chi_{\rm all})^{-1}<6 .
 \tag{B.28}
$$
原 C.18--C.25 的全部 ordinary、角 divergence、physical jump、
head、外 $f_B$、mean/source 列分别乘这个安全因子6即可。
不重新计算任何旧 cap kernel、候选 Fourier 系数或 residual。

这里的来源和范围必须严格区分：它给**同一物理中心**与其真外图的
全方向 Jacobi 端口。若消费的是 repaired M32、非零 $\delta$ 家族或
moving 方程，仍须用已经逐项支付的相应 coefficient transfer、
residual-sensitive bridge、true boundary error 和原 mean map。
本篇不将旧中心的数值费用自动转授给新对象，也不把独立高 cap trace 消去。

## 9. 已完成与真正后继

本篇支付了原反射匹配中缺失的真实 $B_0$ 反馈：
完整 signed Fourier 的 nonlinear $C_R$ 图、所有 mean 的 actual matching、
径向角规范和周期位置重建，以及同一实际背景的全方向 Jacobi 端口。
原 successful symmetric 成员由唯一性保持，不需重跑旧科学源。

fixed-$C_R$ 尾 inverse 可因此与一个真正 full-$4\mathbb Z$ 的 cap 图联立，
但接线时仍需：原 strong ordinary/weak source 和标签的双向映射；
(B.27) 与 Darboux mean charge 的准确关系；全部 $\nu$/双 $\Gamma^*$
参数列；内 body 和未知 high/cap 的实际 Schur；最终 nonlinear 剩余。
未将本条接口完成写成 README 的最终完成声明。
