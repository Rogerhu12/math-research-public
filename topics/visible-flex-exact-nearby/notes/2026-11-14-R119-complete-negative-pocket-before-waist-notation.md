# R119 续篇：整个真实负窗的固定参数低缩放正定控制型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇把第69束只在 $J_0$ 内积分的实际控制型
延伸到包含两个真实转向根的**整个负分量**。保持同一个当前
$\Gamma$、同一个真实内部标签和背景解；中心的两条物理迹允许
$m=\pm M$ 的任意实或复数据。传播后保留全部 Fourier 输出、
两个 mean、实际密度、normal shear 和两端原物理角。

第67束同一个 compact 方向在整个负窗上的真实 Green 变分型仍
大于 $d_*/8$。为支付远离控制支集的完整背景响应，本文使用
$\mathcal X\le2^{-1048576}$。这不是没有 producer 的抽象小球：
同一 fixed-stop 对象上的实际 incoming 首消已经给
$\|\mathbf a^{\rm inc}\|_{224}<2^{-60000000}10^{-8}$、
$\mathcal X<16\|\mathbf a^{\rm inc}\|_{224}$，严格位于这个邻域中。
本篇没有据此声称剩余外方程已经为零。

**范围。** 结论是固定当前 $\Gamma$ 的完整 physical Cauchy
crossing form，在明确的中心单频两迹子空间上成立。沿实际选择支的
$D_\psi\Gamma^*$、随参数移动的 principal 端口识别，以及不同
$M$ 的完整近共振簇仍须接合。本文既不将局部角图改为恒等，
也不把这个型称为全网络或 $\mathcal F$ 的逆。

## 1. 同一个实际负窗与完整方向

采用[第69束](R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md)
的 $j\ge8193$、$J=j+5$、$\delta=\delta_j$、
$Q=7+Bf(x)$、$dt=a_rdx$、$a_r=\Delta/B$、
$\kappa=M^2/B\le1$。假设
$$
 2^{-40}\delta^{-1/8}\le M\le\sqrt B,\qquad
 80<\Delta<3J,\qquad B<2^7J\delta^{-3/2}.
 \tag{P.1}
$$
控制支集位于第67束真正尚未使用的区间；其它 compact 控制及
两个补偿 bump 均在该区间外。第67束给出同一个实方向 $\psi$，
$$
 \rho=2^{-2204}M^5B^{-4}\Delta^{-11},\qquad
 d_*=2^{-22000}M^{50}B^{-39}\Delta^{-103},
$$
$$
 \|\psi^{(l)}\|_\infty\le\rho^{4-l},\qquad
 \|\psi^{(l)}\|_{L^1_x}\le2\rho^{5-l}\quad(0\le l\le4),
 \qquad L_\psi=(d_*/4)I .
 \tag{P.2}
$$
方向准确消去原两个径向 phase 变分。这里没有用该消去替代
非径向 $\Gamma^*$ 的真实链式法则。

令 $I_i=[t_-,t_+]$ 是包含这个支集的**整个**负分量，两个端点
为原材料 $t$ 的 simple 根。它至多相交两个胞元。为不依赖
左右编号习惯，统一用
$$
 \mathcal N_{i|j}:=\sum_{k=j-1}^{j+1}(N_k^c+N_{k-1}^c),\qquad
 N_k^c=2^{200}h_k^{-5}\frac{\zeta_k}{\mu_k\delta_k^2}.
 \tag{P.3}
$$
这包括所有实际相交胞元及其完整邻胞费用；没有只计控制所在胞元。

原 physical 方程及 total-flux 两态是
$$
 h_t=dh_\theta+a\pi,\qquad
 \pi_t=\partial_\theta(d\pi)+Q\partial_\theta(c h_\theta),
 \qquad a=\mu^{-1}.
 \tag{P.4}
$$
仍令 $u=\sqrt{\mu_0}h$、$v=\pi/\sqrt{\mu_0}$，
$\mu_0=w/r$ 为同一当前径向参考。在支集中心定义
$$
 Z_M(c)=\left(\sqrt{k_M}u_c,
 \frac{v_c-(1+Q(c))u_c/2}{\sqrt{k_M}}\right),
 \qquad k_M=\sqrt{7M^2-16}.
 \tag{P.5}
$$
两条输入迹都只支持在 $\pm M$；此后从不作输出投影。
对实际背景，第二分量仍是显示的参考 trace functional，
不把它改写成实际 $u_t/\sqrt{k_M}$。

这里与第61束使用同一材料密度规范。引用以
$a_{\rm phys}=\rho r$ 写出的 root 证明时，将其散度矩阵、total
通量及 ordinary/weak 密度源同时乘固定正数 $\rho$，即
$\mu=\rho\mu_{\rm phys}$、$\alpha=\rho\alpha_{\rm phys}$、
$U=\sqrt\rho U_{\rm phys}$。当前 fixed-stop 的 $\rho$ 固定，
compact 方向不改变它；所有对数导数、$\alpha/\mu_0$ 和两行相对
费用因此不变。这个统一换元没有删掉一个物理尺度或源因子。

## 2. 从中心到整个严格部分的完整空间

使用[真实 strict 密度证明](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
(S.14)--(S.18) 的准确变量
$$
 \Lambda=\mu q\upsilon=\mu_0q/D,\quad w_d=\sqrt\Lambda h,
 \quad \zeta_d=(\pi+Th)/\sqrt\Lambda,\quad
 T=\mu(\ell_t-d\ell_\theta)/2,\quad \ell=\log\Lambda,
$$
$$
 y_\sigma=((w_d)_\theta+\sigma\zeta_d)/2,\qquad
 \mathcal F_s=\mathbb C^2\oplus H^s_0\oplus H^s_0 .
 \tag{P.6}
$$
其中两个有限维分量是完整高度和密度通量 mean。
真实流从中心出发定义，仍可向两边解；原 (S.28)、(S.31)
本来对任意两个 strict 截面成立。

本篇取 $s=5/2$，准确落在原 $[-9/2,7/2]$ 窗内。
[当前受控对象的重实例化](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
(N.2)--(N.4)、(N.14)--(N.16) 保留相同完整 Cauchy 窗。
两个可能邻胞的 $\delta$ 至多相差2，$J$ 比小于2；因此可统一取
$$
 \|\mathcal U_{\rm st}(t,s)\|_{\mathcal F_{5/2}}<2^{1100}J^5\delta^{-10}.
 \tag{P.7}
$$
具体地，原真实 strict 费用 $2^{1024}(k+5)^5\delta_k^{-10}$
乘 $2^{15}$ 已覆盖邻胞改变；(P.7) 还留61 bits。这里不使用
一个尚未证明的 arbitrary-source Green。

中心输入到这个真实空间的费用为
$$
 \|Y_c\|_{\mathcal F_{5/2}}^2
       <2^{128}B^{7/2}\|Z_M(c)\|_2^2 .
 \tag{P.8}
$$
以下说明频率和 shear，避免隐藏一次 $M$ 损失。
在中心，$\sqrt B<q<2\sqrt B$，$2M<k_M<3M$。
径向主式为
$$
 w_d=\sqrt q\,u,\qquad
 \zeta_d=q^{-1/2}[v+\ell_{0,t}u/2],\qquad
 \ell_{0,t}=-1-Q+Q_t/(2Q).
$$
代 (P.5) 后，第二项的剪切准确剩 $Q_tu/(4Q)$。
由 $|Q_t/Q|<2B/\Delta<B$，得到
$$
 \|(w_d)_\theta\|_2^2+\|\zeta_d\|_2^2+\|w_d\|_2^2
             <2^{10}B^{3/2}M^{-1}\|Z_M(c)\|_2^2 .
$$
实际系数相对这些径向乘子在角宽2的完整 Wiener norm 和
前三角导之和小于 $2^{30}n_i$，由原 (S.10)、
$\mu/\mu_0=JD^{-3/2}$、$\Lambda/\mu_0=q/D$ 直接给出。
Peetre 比 $\langle m+n\rangle^s/\langle m\rangle^s
\le(1+|n|)^{|s|}$ 支付所有输出 lag。包括两个 mean、四个状态
求和及真实 $H^s$ 权习惯的转换，费用小于 $2^{96}$。
再用 $(1+M)^5<4M^5$ 和 $M^4\le B^2$ 即得 (P.8)。
这里没有把乘子产生的高输出删去。

在任一 strict 截面，准确重建式 (S.16)、(S.39) 给
$$
 \|u\|_{H^1}^2+Q\|u_\theta\|_2^2+\|v\|_2^2
  <2^{128}J^2\delta^{-6}\|Y\|_{\mathcal F_0}^2 .
 \tag{P.9}
$$
确实 $q>1/16$，$q_{\max}<2^8\sqrt J\delta^{-3/4}$，
$|\ell_{0,t}|<2^{29}J\delta^{-3}$，实际角乘子用同一 (S.10)。
$w_d=R_HY$、$\zeta_d$ 的 norm 分别小于
$2^{22}\|Y\|$、$2^{20}\|Y\|$。
代 $u=\sqrt D\,q^{-1/2}w_d$ 和
$$
 v=\sqrt{q/D}\,\zeta_d
   -\frac{\mu}{\mu_0}\frac{\ell_t-d\ell_\theta}{2\sqrt{q/D}}w_d
$$
逐项平方即可得 (P.9)。特别该式还控制无 $Q$ 权的
$\|u_\theta\|^2$，根附近的交叉响应以后需要它。

## 3. 两个真实根的物理状态，含变图取值

每个根使用[联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
的 $x=\varsigma b(t-t_e)$、$\Psi=(\xi,\phi)$、
$\alpha$ 和 canonical 高度 $U=\sqrt\alpha h\circ\Psi^{-1}$。
负侧方程为
$$
 U_{\xi\xi}-\frac{\xi}{b^2}U_{\phi\phi}+VU=0,\qquad
 |V_0|<16,\quad\|M_{V-V_0}\|_{H^s\to H^s}<2^{52}n_i .
 \tag{P.10}
$$
取 $H=1/64$。原平衡
$$
 s_m(\xi)=(1+(|m|/b)^{4/3}+(|m|/b)^2\xi)^{1/2},\quad
 \mathcal Y=(s^{1/2}U,s^{-1/2}U_\xi)
 \tag{P.11}
$$
在 $0\le\xi\le H$ 的真实双向 $H^3$ Cauchy norm 小于
$2^{2185}$；mean 的权为1。

后面只需将该范围扩到 $2H$，不能默认变图仍在 $\xi\le H$。
在 $H\le\xi\le2H$ 另用
$\lambda_m=(1+(m/b)^2\xi)^{1/2}$ 的两行。
主部交叉的未抵消项为 $1/\lambda_m$，径向权对数总变差小于
$\log2/2$；势的完整 $H^3$ 乘子 norm 小于18。
所以这一短段双向能量放大小于2。
并且
$$
 1\le s_m/\lambda_m<5,\qquad H\le\xi\le2H,\quad m\in4\mathbb Z.
$$
例如令 $z=(|m|/b)^{2/3}$，
$z^2/(1+Hz^3)\le H^{-2/3}$，故比值平方小于
$1+H^{-2/3}<25$。往返框架合计小于8。
因此在 $0\le\xi\le2H$ 可安全使用 $2^{2196}$。

从严格物理截面到 $\xi=H$ 的转换准确保留其端角图。
将物理 $w_d,\zeta_d$ 拉到 graph 上，得到
$$
 w_d=W\circ H_e,\qquad
 y_{\sigma,\rm phys}=\mathcal D_{H_e}Y_{\varsigma\sigma}.
 \tag{P.12}
$$
这是 normalized divergence density 的真实 conormal 换元：
$\Lambda=\alpha\sqrt\xi/b$ 为二维判别式密度不变量。
因此 (P.12) 没有额外未保留的 shear；若直接使用 raw 通量，
它恰由原 (G.24)--(G.25) 的 $s_g$ 与物理 $T$ 相消。
方向号 $\varsigma$ 和两支交换均保留。

原 graph 证明 (G.17)--(G.23) 给：真实端角及其逆的费用
$2^{20}$，完整 graph 逆费用小于 $2^{21}$，
$\mathcal A_*^{-1}:\mathcal E_{5/2}\to H^3\oplus H^3$
小于 $2^{20}\sqrt b$。高度 mean 用完整 pullback 求平均，
再加 (S.16) 的恢复费，(P.12) 总计不超过 $2^{60}$。
与 (P.7) 和上述 root Cauchy 合并，得到
$$
 \sup_{0\le\xi\le2H}\|\mathcal Y(\xi)\|_{H^3\oplus H^3}
       <2^{3500}\sqrt b\,J^5\delta^{-10}
                                      \|Y_c\|_{\mathcal F_{5/2}}.
 \tag{P.13}
$$
这个费用对任一根成立；从中心到该根只经过相应一侧 strict
部分及一个根转换，没有把整条负窗重复传播两次。

还须真正支付在 $t=\mathrm{constant}$ 的变图上取值。
对每个实际 $x$，写 $\xi=g_x(\phi)$、$\phi=H_x(\theta)$。
联合根证明给 $0\le g_x\le2H$、$1/2<H_x'<2$，并有
$$
 \frac b2<\frac{\alpha(\Psi(t,\theta))}{\mu_0(t)}<2b,\qquad
 |\xi_t-d\xi_\theta|<2b,\quad|\phi_t-d\phi_\theta|<1 .
$$
相同完整复域的 Cauchy 给
$|\xi_\theta|<1$、$|\phi_\theta|<2$、
$|(\partial_t-d\partial_\theta)\log\alpha|<2^{10}b$、
$|\partial_\theta\log\alpha|<1$。
这些是原 (J.16)、(J.22)--(J.25) 的直接真实域后果。

不用裸 graph pullback 的同空间小差。对任意 $F(\xi,\phi)$，
径向基本定理和 Cauchy--Schwarz 直接给
$$
 \int\sup_{0\le\xi\le2H}|F(\xi,\phi)|^2d\phi
 \le2\|F(0)\|_2^2+4H\int_0^{2H}\|F_\xi\|_2^2d\xi .
 \tag{P.14}
$$
将它分别用于 $U,U_\phi,U_\xi$。由 (P.11)
$\|U\|_{H^3}\le\|\mathcal Y\|_{H^3}$、
$\|U_\xi\|_{H^{5/2}}\le2\|\mathcal Y\|_{H^3}$，
以及准确方程 (P.10) 控制 $U_{\xi\xi}$，可得三种图迹的
$L^2$ 平方之和小于 $2^{14}\sup\|\mathcal Y\|_{H^3}^2$。
这里明确多用了输出角导；不存在有限输入使输出自动有限的论证。

最后 $h=\alpha^{-1/2}U\circ\Psi$，
$\pi=\mu(\partial_t-d\partial_\theta)h$。
代入上述完整系数和 $H_x'$，得到
$$
 \|u\|_{H^1}^2+Q\|u_\theta\|_2^2+\|v\|_2^2
       <2^{80}b\sup_{0\le\xi\le2H}\|\mathcal Y\|_{H^3}^2.
 \tag{P.15}
$$
根处使用同一个公式的连续限制；没有除以 $q=0$。
两个 mean 均在 (P.11)--(P.15) 中，物理常高度也未被误当成
canonical 的纯零模。

## 4. 整窗真实物理能量

两个邻胞的根满足 $b^2<2^{38}J\delta^{-9/2}$。
由 (P.8)、(P.13)、(P.15)，根区的总指数不超过
$$
 2^{80+7000+128+38+25}J^{29/2}\delta^{-119/4}
                                      \|Z_M(c)\|_2^2 .
$$
这里 $B^{7/2}<2^{25}J^{7/2}\delta^{-21/4}$，
所以 $20+9/2+21/4=119/4$。
strict 区由 (P.7)--(P.9) 得 $\delta$ 费 $125/4<32$、
$J$ 费小于16。统一安全地有
$$
 \boxed{\quad
 \sup_{t\in I_i}
 [\|u(t)\|_{H^1}^2+Q(t)\|u_\theta(t)\|_2^2+\|v(t)\|_2^2]
 <2^{7800}J^{16}\delta^{-32}\|Z_M(c)\|_2^2 .\quad}
 \tag{P.16}
$$
此处没有将极小的 $\mu_0$ 当成无权有界乘子；它始终准确
留在 $u,v$ 和原物理两迹 (P.5) 中。

## 5. 支集外的完整 gauged 响应

固定当前 $\Gamma$ 和全部真实内部标签，记
$\widehat z=D_\psi(p,k)-\psi F_1$。
[第60束](R119-supplement-actual-compact-profile-label-response.md)
的完整传播适用于整条尾，因此在本负分量有
$$
 \widehat n_i<2^{832}\mathcal N_{i|j}\mathcal X
                 P_j\rho^5,\qquad
 P_j=h_j^{-14}\delta_j^{-7/4}
                  =2^{-42}\delta_j^{-231/128}.
 \tag{P.17}
$$
$\widehat n_i$ 是两个分量及前两个角导的真实求和，不是逐项 max。
本式只含 gauged 场；没有把 $\psi F_1$ 的 $\rho^4$ 项塞回去。

第61束实际二次型为
$$
 \mathcal H_{\widehat z}(Y)
 =\langle Q\widehat c|h_\theta|^2+\widehat a|\pi|^2\rangle
       +2\operatorname{Re}\langle\overline\pi\widehat d h_\theta\rangle.
$$
完整商法则和 $2ab\le a^2+b^2$ 给
$$
 |\mathcal H_{\widehat z}(Y)|
 <2^{24}\widehat n_i
 [\|u\|_{H^1}^2+Q\|u_\theta\|^2+\|v\|^2].
 \tag{P.18}
$$
这里没有错误地把第一个 $Q$ 乘到通量项；也没有在根处用
$Q^{-1}$ 吸收最后的交叉项。无 $Q$ 权的角导正是 (P.16)
另外保留的那一行。

由 $|I_i|<8\delta<1$，得到**整个**支集外响应
$$
 \left|\int_{I_i\setminus J_0}\mathcal H_{\widehat z}(Y)dt\right|
 <2^{8700}\mathcal N_{i|j}\mathcal XP_j\rho^5
               J^{16}\delta^{-32}\|Z_M(c)\|_2^2 .
 \tag{P.19}
$$
实际总方向没有在其它径向点清零；(P.19) 正是此前缺少的那一项。

## 6. 真归一、原全局因子及可达邻域

准确有
$$
 \rho^5/d_*=2^{10980}M^{-25}B^{19}\Delta^{48}.
$$
使用 (P.1)、$M^{-25}\le2^{1000}\delta^{25/8}$，
$B^{19}<2^{133}J^{19}\delta^{-57/2}$、
$\Delta^{48}<2^{77}J^{48}$，(P.19) 除以 $d_*$ 后小于
$$
 2^{21000}\mathcal N_{i|j}\mathcal XJ^{84}\delta^{-60}.
 \tag{P.20}
$$
未放宽前的 $\delta$ 费用为
$32+57/2-25/8+231/128=7575/128<60$，
二进制常数为 $8700+10980+133+77+1000-42=20848<21000$，
$J$ 次数为83。没有使用径向 $M^{1894}$ 逆乘一个绝对误差。

原强尾的两个全局因子不能删除。第69束已准确给
$$
 N_{8192}^c<2^{-20138},\qquad
 N_k^c=N_{8192}^c2^{-\alpha(k-8192)}\ (k\ge8192),\qquad
 \alpha=31867/256.
$$
在 $k=8191$，旧完整幂是 $827/256<4$，故
$N_{8191}^c<16N_{8192}^c$。由 (P.3) 的六项完整和，
对 $j=8193+q$ 可统一取
$$
 \mathcal N_{i|j}<2^{-20010}2^{-\alpha q}.
 \tag{P.21}
$$
当 $q=0$，六项和小于 $32N_{8192}^c$；当 $q\ge1$，
最浅项为 $N_{8192}^c2^{-\alpha(q-1)}$，其它五项的总比
小于2，且 $\alpha+1<128$，均落入 (P.21)。

取 $\mathcal X\le2^{-1048576}$。首层 (P.20) 的指数至多
$$
 21000-20010-1048576+14\cdot84+8197\cdot60
            =-554590<-550000 .
 \tag{P.22}
$$
层比满足 $(8199/8198)^{84}<97/96$、$(97/96)^{64}<2$，
且 $\alpha-60-1/64>64$。因此完整无限深尾的 (P.19) 相对
费用均小于 $2^{-550000}$，逐层和也保留这一宽余量。

该球有真正输入：[fixed-stop 全 incoming](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.30)、(D.34) 给
$$
 \|\mathbf a^{\rm inc}\|_{224}<2^{-60000000}10^{-8},\qquad
 \mathcal X^{\rm inc}<16\|\mathbf a^{\rm inc}\|_{224}
                                    <2^{-1048576}.
 \tag{P.23}
$$
并且标签球 $\|\mathbf a\|_{224}<2^{-1048580}$ 是原完整
$A_*$ 球中的开邻域，全部已有全图可直接限制到它。
这里没有声称对任意原 $A_*$ 数据都已得到 (P.22)。

## 7. 整个负窗的实际 Green 变分型

令 $Y(t)$ 是 (P.4) 的真实齐次解。定义
$$
 \mathfrak G_{I_i}(Y_c)
   =\int_{I_i}\{\psi\mathcal K_{\rm act}(Y)
                         -\mathcal H_{\widehat z}(Y)\}dt.
 \tag{P.24}
$$
第61束的准确 canonical gauge 恒等式表明，这是固定原物理
截面的完整 Cauchy crossing form。$\psi$ 及其端 jets 在两根
附近均为0，故局部 gauge 没有任何未列出的端项。
原 Jacobi 高度与 total conormal 始终是同一对物理状态。

第69束 (L.19)--(L.24) 控制 $J_0$ 内全部直接项和响应；
它在更小的实际球中当然仍成立。(P.19)--(P.22) 控制其余全部
径向点。因此
$$
 \boxed{\quad
 \mathfrak G_{I_i}(Y_c)>
          \frac{d_*}{8}\|Z_M(c)\|_2^2,\qquad
 Y_c\in\mathcal E_M,\quad M^2\le B.\quad}
 \tag{P.25}
$$
这是整个真实负窗的固定参数型，不是只对参考解或其某个实
rank-one 分支的导数。输出无限尾、相反 Fourier 锥和两 mean
均经过 (P.7)--(P.16) 后参加积分。

## 8. 全源、两 mean 和实际剩余的权限

一般 ordinary $g$、weak $(F^t,F^\theta)$ 的原状态源仍准确是
$$
 s=(-aF^t, g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat{\dot Y}_t=\mathsf A\widehat{\dot Y}
       +(\widehat{\mathsf A}+\psi\mathsf R)Y
       +\dot s-\psi\mathsf Bs.
 \tag{P.26}
$$
没有 $F^t_t$。所有仿射列按同一有序 Duhamel 加入，不能因
(P.25) 是齐次二次型而把它们置零。
strict 部分使用原 (S.35)--(S.36) 的实际源 norm；root 部分
使用联合根 (J.34)--(J.37) 的真 Jacobian/height/Piola 源对，
物理变图端口使用 (G.30)--(G.37) 的联合源及 weak 法向迹。
本篇 (P.14) 对齐次 Jacobi 场所付的角导不自动授予任意粗源
联合径向正则性；没有将原 $L^2_tH^s_\theta$ 免费搬到一张变图上。

对当前标签方向及支集在 strict 内的本材料 metric 方向，两个
root germ 的额外 metric ordinary/weak 体源准确为0；真实背景
响应仍通过 (P.17)--(P.19) 保留。
物理 mean 和 bare 通量始终满足
$$
 \pi_{0,t}=g_0,\qquad
 h_{0,t}=\langle dh_\theta+a\pi-aF^t\rangle,\qquad
 p_{\rm bare}=\pi-F^t.
 \tag{P.27}
$$
bare 端口另需真实 $F^t$ 两端迹；相应 producer 不存在时仅授
total-flux 结论。高度常数与 holonomy mean 未被设置为0。

下一步仍是将 (P.25) 接到实际 $D_\psi\Gamma^*$ 两列和参数
依赖的 physical principal 端图，再处理完整混频近共振簇。
一个中心单频子空间上的全型不等于整个混频矩阵正定；本文不
跳过这个量词差，也不从已可达小球推出非线性外方程已解。

必要有理预算见
[源码](../scripts/fourfold_complete_negative_pocket_fixed_parameter_20261114.py)
和[实际记录](../notes/2026-11-14-R119-complete-negative-pocket-fixed-parameter-budget.json)。
