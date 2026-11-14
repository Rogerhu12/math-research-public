# R119 续篇：保原径向的真双射线振幅及全层可积耦合差

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在已经联立选定的真实无限尾上，保持原径向
$t$ 不变，把两个实际 Riemann 振幅分别沿自己的真实特征角图
传输。其完整耦合算子与同一预选径向参考耦合之差，在全部内部
负型分量上的径向积分之和小于
$$
 \boxed{\quad 2^{-652}\,\overline X(a).\quad}                \tag{A.1}
$$
这里每个分量的实际角宽费用明确为 $h_j/64$；全 Fourier 空间
包括 mean，不使用同宽角复合的小算子差。估计对两个转向端
保持可积，且真实 log-quintic 坡肩的费用已经计算。

这个结果是**完整一阶耦合生成元的比较**。Riemann 振幅本身在
转向端带有真实 $q^{-1/2}$ 权；(A.1) 不自动给出相应 Airy
端口空间中的全传播逆或整个 mixed-tail 高输入相对逆。
末节明确留下该项，而不把转向端的两个振幅当成任意有界边值。

## 1. 实际对象与唯一一次角宽支出

沿用
[联立 KAM](R119-supplement-joint-actual-negative-band-return-kam.md)、
[双端二维图的准确密度](R119-supplement-two-ended-negative-characteristic-chart-and-densities.md)
的真实对象，但本篇始终不把 $t$ 混入角变量。
对 $i=(j,k)\in\mathcal I$ 写
$$
 q=\sqrt{-A_{\Gamma^*(a)}},\quad q_0=\sqrt{-A_{\Gamma^0}},
 \quad S_0(t)=\int_{t_-}^tq_0,\quad L_0=S_0(t_+),
$$
$$
 \widehat\varepsilon_i=2^{80}(j+4)\delta_j^{443/256}e^{-640},
 \quad
 \gamma_i^{\rm D}=\kappa_i/64,\quad
 \overline X(a)=\frac{13}{4}\|a\|_{\ell^1_{224}}<1.
 \tag{A.2}
$$
全部非径向状态和度量参数均是真实无限尾图的输出。
$\Gamma^0$ 与目标角在最初一次选定后固定。
实际 $\Gamma^*(a)$ 仍保留所有标签及层之间的交叉依赖。

本篇首先支付一个确切的较宽角域，帽号费用不能与前篇窄域
$e^{-896}$ 的费用混用。将 R72 的基绝对宽度统一增加64，
把剩余标签权改记为160：若原规范状态和标签为 $X,a$，
新规范是 $X_m^{\rm new}=e^{64|m|}X_m$、
$a_m^{\rm new}=e^{64|m|}a_m$，所以
$$
 \|a^{\rm new}\|_{\ell^1_{160}}=\|a\|_{\ell^1_{224}}.
$$
总角规范 $\tau_j+64+160=\tau_j+224$ 准确相同。
R72 的局部证明与统一参数图只用代数乘法和已列出的宽度差，
故它们在这套基宽上是同一个物理解，而不是新增一个更宽的
输入标签球。相应真实四态在角宽 $64+3$ 上满足
$$
 n_j\le2^{64}\delta_j^{443/256}e^{-640}\overline X.
$$
把前篇 KAM 的每个物理角宽也增加64，标准圆 $x=4\xi$
的每个角宽增加256，所有宽度差与 Newton 常数不变。
其实际小除数比仍有
$$
 \sup_i\frac{\widehat\varepsilon_i}{(\gamma_i^{\rm D})^2}
 <2^{132}e^{-640}<2^{-508}<2^{-64}.
$$
故同一 KAM 迭代在物理宽 $64+3/8$ 收敛。
每个迭代的 Fourier 逆、平均行、完整参数 Neumann 逆及
规范均与原窄域迭代相同；限制到交叠角域后逐步相等。
所以得到的是原来同一个 $k,\Gamma^*$ 的较宽延拓，
并未另选度量参数或另选目标相位。

R72 的真实逐层宽度差为
$$
 h_j=\frac9{100}\ (129\le j\le4096),\qquad
 h_j=8\delta_j^{1/256}\ (j\ge4097).
$$
本篇逐分量采用
$$
 \hbar_i=h_j/64,\qquad 0\le s\le64+1/16.                     \tag{A.3}
$$
算子从 $\mathcal A_{s+\hbar_i}$ 到 $\mathcal A_s$，所有
$m\in4\mathbb Z$ 均保留。两个负分量各使用一次这个宽差，
跨胞分量使用两层较小的 $h_j$，因为 $h_j\le h_{j-1}$。
完整无限次单向经过的宽差之和真正满足
$$
 \sum_{i\in\mathcal I}\hbar_i
 <\frac1{32}\left(3968\frac9{100}+\frac1{16}\right)<12.
$$
这个总费用从刚证明的64角宽余量中支付，例如从宽64开始后
仍大于宽52；不需要把只有窄域定义的圆周图冒充 R72 的任意
大绝对角宽图。本篇不把一次经过的费用当成任意多次 Newton
迭代都不再耗宽的同宽逆。

## 2. 判别式的额外准确输运恒等式

使用原相对变量
$$
 E=1+w^2,\quad J=1+K+EU,\quad
 D=1-w^2(2K+K^2+EP^2),\quad
 d=\frac{E(V-P)}J,\quad v=\frac{\sqrt D}J,
$$
$$
 N=(1+K)V+EPU .
$$
原完整方程为
$$
 P_t=V-(A+1)P,\qquad
 K_t=
 \frac{-A(2K+U+K^2+KU+w^2P^2)+E(V-P)^2}{J}.
 \tag{A.4}
$$
直接微分判别式，保留 $w_t=Aw$、$E_t=2Aw^2$，
得到
$$
 \boxed{\quad D_\theta=-2w^2N,\qquad
                  D_t-dD_\theta=\frac{2Aw^2DU}{J}.\quad}
 \tag{A.5}
$$
例如令 $Z=1+K$，把 $K_t$ 代入 $D_t$ 后，$A$ 的分子
准确含
$$
 U\,[E(Z^2-1+w^2P^2)-Z^2]=-DU.
$$
其余 $E(V-P)$ 项准确为 $dN$。所以 (A.5) 没有留下一个
独立的 $A_t$ 或二阶径向状态。

在 hodograph 角 $\xi$ 中，仍记同名的复合函数，
$\mathscr D=\partial_t-b\partial_\xi$，
$b=d\chi_\theta-\chi_t$、$\chi_\theta=c/v$。于是
$$
 \mathscr D\log D=2Aw^2U/J,\qquad
 cq\,(\log D)_\xi=-2qw^2N/(J\sqrt D).
 \tag{A.6}
$$
这两个式子是在实际背景上准确成立的有限代数恒等式。

## 3. 完整 Riemann 振幅方程

记 $\widehat h=h\circ\chi^{-1}$，并设
$$
 z=\widehat h_\xi,\quad
 p=\widehat\mu(\widehat h_t-b\widehat h_\xi),\qquad
 \widehat\mu=\frac{w/a_{\rm phys}}{cD},\quad
 \widehat s=\frac{w^2e}{cD}.
$$
这里 $p$ 是准确 raw conormal 密度，不是 grounded 通量。
完整弱方程等价于
$$
 z_t=\partial_\xi\left(bz+\frac p{\widehat\mu}\right),
 \qquad
 p_t=\partial_\xi\left(bp+\widehat\mu c^2q^2z\right)
                                                    +\widehat s.
 \tag{A.7}
$$
在开负型段置
$$
 \mathfrak k=\widehat\mu\,c q
       =\frac{w}{a_{\rm phys}}\frac qD,\qquad
 W_\sigma=\frac{p+\sigma\mathfrak k z}{\sqrt{2\mathfrak k}},
 \quad \sigma=\pm1.
 \tag{A.8}
$$
注意 $c$ 在真实密度中准确相消。
将 (A.7) 逐项代入，得到完整方程
$$
 (W_\sigma)_t
  =\partial_\xi[(b+\sigma cq)W_\sigma]
       +\left(-\frac{g_\Gamma}{2}+\mathcal R_\sigma\right)
                      W_{-\sigma}
       +\frac{\widehat s}{\sqrt{2\mathfrak k}},
 \tag{A.9}
$$
$$
 g_\Gamma=A_\Gamma-1+\frac{q_t}{q},\qquad
 \boxed{\quad
 \mathcal R_\sigma
       =\frac{Aw^2U}{J}
          -\sigma\frac{qw^2N}{J\sqrt D}.
 \quad}                                                    \tag{A.10}
$$
一种直接核对方法是先不代入 (A.6)：非对角系数为
$-\tfrac12[\mathscr D\log\mathfrak k+
\sigma cq(\log\mathfrak k)_\xi]$，对角项恰为 $b_\xi$，
它已经包含在 (A.9) 的散度内。
再用
$(\log(w/a_{\rm phys}))_t=A-1$
及 (A.6)，即得 (A.10)。
因此没有遗漏 $b_\xi$、$c_t$ 或一个径向 Jacobian；
$c_t$ 在这个准确密度归一化中确实不出现。

由于 $n\le1/256$、$J^{-1},D^{-1/2}<2$、$\|N\|\le2n$，
在已支付的原解析角域缩到宽 $64+1/8$ 后有
$$
 \|\mathcal R_\sigma(t)\|_{\mathcal A_{64+1/8}}
       \le16w^2(1+|A|)n.
 \tag{A.11}
$$
转向处 $A=-q^2$，所以 $\mathcal R_\sigma$ 真实趋0。
这里没有把无因子的常数项在转向平衡中放大。

## 4. 各支的真角图与完整密度 pullback

令 $k(\eta)=h_i(4\eta)/4$ 为同一个真实 KAM 图，
$$
 \Theta_\sigma(t,\eta)=F_\sigma(t,k(\eta)),\qquad
 J_\sigma=(\Theta_\sigma)_\eta,\qquad
 Z_\sigma=J_\sigma W_\sigma(t,\Theta_\sigma).
 \tag{A.12}
$$
两个 $\Theta_\sigma$ 都保留原 $t$。
在实背景上 $J_\sigma>0$，且
$(J_\sigma)_t=-(b_\xi\circ\Theta_\sigma)J_\sigma$。
因而 (A.9) 的整个 principal 散度被准确消去。

定义实际部分往返
$$
 C_\sigma(t)=\Theta_{-\sigma}(t)^{-1}\circ\Theta_\sigma(t).
 \tag{A.13}
$$
完整方程成为
$$
 (Z_\sigma)_t=\mathcal C_\sigma(t)Z_{-\sigma}+F_\sigma,
$$
$$
 \mathcal C_\sigma(t)f
 =C_\sigma'
  \left[-\frac{g_\Gamma(t)}2+
                    \mathcal R_\sigma(t,\Theta_\sigma)\right]
                                                f\circ C_\sigma,
$$
$$
 F_\sigma=
   J_\sigma\,\frac{\widehat s\circ\Theta_\sigma}
                        {\sqrt{2\mathfrak k\circ\Theta_\sigma}} .
 \tag{A.14}
$$
特别 $C_\sigma'$ 是实际密度因子，不能删除。
每个固定 $t$ 的所有函数仍在真实解析角域内，
没有跨越原仅 $C^2$ 径向接缝的角复合。

## 5. 部分往返的时间导数：共同漂移准确相消

微分
$\Theta_{-\sigma}(t,C_\sigma(t,\eta))=\Theta_\sigma(t,\eta)$，
真实速度中的共同 $b$ 在同一终点上准确相消，给
$$
 \boxed{\quad
 \partial_t C_\sigma(t,\eta)
   =-\frac{2\sigma c(t)q(t)}
       {J_{-\sigma}(t,C_\sigma(t,\eta))}.
 \quad}                                                    \tag{A.15}
$$
与只估计两条独立流的绝对位移相比，这个式子保留了转向所需的
完整 $q$ 因子。
联立 KAM 的两端恒等式给
$$
 C_\sigma(t_-)=\mathrm{id},\qquad
 C_\sigma(t_+)=T_{-2\sigma L_0}.
 \tag{A.16}
$$

前篇 Newton 各步的逐行 (K.24) 还给局部而非仅上确界的
$$
 \|k'-1\|_{\mathcal A_{64+3/8}}
 <K_i:=2^{18}
       \frac{\widehat\varepsilon_i}{\gamma_i^{\rm D}}\overline X.
 \tag{A.17}
$$
确实
$32\sum_{n\ge0}2^{-8n}(2^{-n-4})^{-3}<2^{18}$；
物理缩放 $k(\eta)=h_i(4\eta)/4$ 对一阶导没有额外因子。
同一求和也界住 $k-\mathrm{id}$。
实际流的积分 $b_\xi$ 小于 $\widehat\varepsilon_i\overline X/64$，
所以在宽 $64+5/16$ 上
$$
 \|J_\sigma-1\|<3K_i.                                    \tag{A.18}
$$
所有复合的角像均在已付宽 $64+3/8$ 内，留有至少 $1/32$
的固定余量。

真实参数修正满足
$$
 |\Delta\gamma_i|
 :=|\Gamma_i^*(a)-\Gamma_i^0|
 <2^{-14}\frac{\widehat\varepsilon_i}{\kappa_i}\overline X
 =2^{-20}\frac{\widehat\varepsilon_i}{\gamma_i^{\rm D}}\overline X.
 \tag{A.19}
$$
在参数支集上，$q/q_0-1$ 由
$|\psi_x|\le96$、$S'\ge135/128$、$\Delta_i>j/2$
直接控制；支集外准确为0。结合完整 mean 已付的
$|c-1|\le256N_i^2$、(A.18)，(A.15) 给
$$
 \|\partial_t C_\sigma+2\sigma q_0\|_{\mathcal A_{64+1/4}}
       \le r_i q_0,\qquad
 r_i=2^{22}\frac{\widehat\varepsilon_i}{\gamma_i^{\rm D}}\overline X.
 \tag{A.20}
$$
例如 $J_\sigma^{-1}$ 的误差不超过 $6K_i$，
$cq/q_0-1$ 的误差小于 $K_i$，整式用 $16K_i=r_i$
已有严格余量。

从左右两端分别积分同一式子，使用 (A.16)，得到关键真界
$$
 \boxed{\quad
 \|C_\sigma-T_{-2\sigma S_0(t)}\|_{\mathcal A_{64+1/4}}
  \le r_i\,\min\{S_0(t),L_0-S_0(t)\}.
 \quad}                                                    \tag{A.21}
$$
这不是把任意小位移的高频相对相位当作小量；下一节将明确支付
它所作用的角导数。两个端点的 vanishing 都来自实际的完整
return 匹配。

## 6. 真实坡肩及转向的加权径向费用

令 $g_0=A_{\Gamma^0}-1+q_{0,t}/q_0$。
实际每个完整负型分量上的 $q_0$ 是先不减、后不增的单峰
函数。理由逐段可见：上升 quintic 的负型末段由0升到
$\sqrt7$；平台为 $\sqrt7$；下降 quintic 先增后减；
参数支集只在其严格增加部分，且原 (M.9) 保留导数符号；
最后的上升 quintic 负型首段由 $\sqrt7$ 降到0。
跨胞接缝也只有同值的 $\sqrt7$ 平台。

完整几何给下面三个实际界：
$$
 |I_i|<4\delta_j,\qquad
 L_0>\delta_j/2,\qquad
 L_0<4\sqrt{\eta_j\Delta_i},\quad
 \frac{L_0}{\kappa_i}<2^{29}(j+4).
 \tag{A.22}
$$
前两个界使用两个相邻胞元总长
$(9\delta_j+24\eta_j)/\sqrt{12}$，
$\eta_j/\delta_j<1/64$，及其中至少一个完整
$q_0=\sqrt7$、长 $\delta_j/\sqrt{12}$ 的平台。
第三个界在下降段用
$q_0^2\le7+2\sqrt{12}\Delta_i/\eta_j$，其余负段
$q_0\le\sqrt7$；$12\delta_j<\sqrt{\eta_j\Delta_i}$。
最后代入 $\kappa_i=2^{-25}\sqrt{\eta_j/\Delta_i}$、
$\Delta_i<3j$ 即得。

准确峰值为
$q_{\max}^2=7+(15/8)\sqrt{12}\Delta_i/\eta_j$，
因为参数支集不触及 $x=1/2$。特别
$$
 q_{\max}^2<256j\delta_j^{-3/2},\qquad
 \log q_{\max}<j+4.                                      \tag{A.23}
$$
后一式由 $\log2<3/4$、
$|\log\delta_j|<3j/4+3$、$\log j<j/4$ 给出。

记 $s_*(t)=\min(S_0,L_0-S_0)$。在左侧 $q_0\le1$
的单调段，有 $S_0\le(t-t_-)q_0$，故
$\int(q_{0,t}/q_0)S_0\le$ 该段长度；右端相同。
在 $q_0\ge1$ 的其余段，
$\int|q_{0,t}/q_0|=2\log q_{\max}$，而 $s_*\le L_0/2$。
因此
$$
 \int_{I_i}\left|\frac{q_{0,t}}{q_0}\right|s_*\,dt
 \le |I_i|+L_0\log q_{\max}.
$$
再用已付的
$\int(1+|A_{\Gamma^0}|)<8(j+4)$，得到
$$
 \boxed{\quad
 \int_{I_i}|g_0(t)|s_*(t)\,dt<16(j+4)L_0.
 \quad}                                                    \tag{A.24}
$$
这个证明完整包含 $q_0$ 的极陡非转向坡肩；
它不使用 $q_{0,t}$ 的点态上界或 $A_{tt}$。

另一个准确可积项是 $g_\Gamma-g_0$。它仅支撑在实际参数
bump 内。写
$$
 H_0=7\eta_j/\sqrt{12}+\Delta_i S'-\Gamma_i^0\psi_x,
 \qquad
 r=-\Delta\gamma_i\,\psi_x/H_0.
$$
在这个支集上，
$H_0>\Delta_i$、$|H_0'|<7\Delta_i$，
所以 $|r'|\le6816|\Delta\gamma_i|/\Delta_i$。
支集长 $1/8$，且 $|r|<1/2$。于是
$$
 \int |( \log(q/q_0))_t|\,dt
       \le852|\Delta\gamma_i|/\Delta_i,\qquad
 \int|A_\Gamma-A_{\Gamma^0}|\,dt=2|\Delta\gamma_i|.
$$
特别，对全部 $j\ge129$，
$$
 \int|g_\Gamma-g_0|\,dt<64|\Delta\gamma_i|.
 \tag{A.25}
$$
这里保留参数修调造成的真实径向振幅变化，没有只重调相位后
把它删掉。

## 7. 全 Fourier 密度复合的真实宽差估计

若 $C(\eta)=\eta+\alpha+\Delta(\eta)$，$\alpha$ 为实数，
$\|\Delta\|_{\mathcal A_{64+1/4}}\le d$、$d<\hbar/4$，
且 $s+\hbar<64+1/8$，则 Wiener 代数逐频展开给
$$
 \|f\circ C-f\circ T_\alpha\|_{\mathcal A_s}
       \le2d\,\hbar^{-1}\|f\|_{\mathcal A_{s+\hbar}}.
$$
这是保留全部 $m$ 的
$|e^{im\Delta}-1|\le |m|d\,e^{|m|d}$，
不是一个同宽 operator norm 断言。
宽 $64+1/4$ 到 $64+1/8$ 的角导给 $\|C'-1\|\le8d$，故
$$
 \|C'f\circ C\|_{\mathcal A_s}
            \le2\|f\|_{\mathcal A_{s+\hbar}},
$$
$$
 \boxed{\quad
 \|C'f\circ C-f\circ T_\alpha\|_{\mathcal A_s}
       \le16d\,\hbar^{-1}\|f\|_{\mathcal A_{s+\hbar}}.
 \quad}                                                    \tag{A.26}
$$
相同公式对完整复标签域成立：固定实平移外的复小位移全部包含
在 $\Delta$ 内，已有严格的像域余量。

本篇真正使用的是
$d=r_i s_*(t)$、$\hbar=\hbar_i$。
(A.22) 与 (A.2) 给全层
$$
 r_iL_0/\hbar_i<2^{-704}\overline X<1/4.
 \tag{A.27}
$$
因此 (A.26) 的前提已经用实际深度、实际参数窗和实际角宽
验证，不是再假设一条未授予的宽标签球。

## 8. 两个完整耦合的全层积分比较

同一固定目标的径向参考生成元定义为
$$
 \mathcal C_\sigma^0(t)f
        =-\frac{g_0(t)}2\,f\circ T_{-2\sigma S_0(t)}.
 \tag{A.28}
$$
其参考密度取
$\mathfrak k_0=w_{\Gamma^0}q_0/(\rho(\Gamma)e^t)$，
即使用同一个当前物理尺度；这个常数尺度不改变 $g_0$，
但在最后恢复真实端口时仍保留。
把 (A.14) 与此式相减。参数振幅项按 (A.25) 支付；
真实 density pullback 差按 (A.21)、(A.24)、(A.26)
支付；非径向真实余项按 (A.11) 支付。得到
$$
 \int_{I_i}
 \|\mathcal C_\sigma-\mathcal C_\sigma^0\|_
         {\mathcal A_{s+\hbar_i}\to\mathcal A_s}\,dt
 \le
 64|\Delta\gamma_i|
 +\frac{128r_i(j+4)L_0}{\hbar_i}
 +32\int_{I_i}w^2(1+|A|)n\,dt.
 \tag{A.29}
$$
右侧对两支同时有效。完整两态矩阵只有两个非对角块，
在两分量最大范数或和范数下均用同一个上界。
已付
$\int(1+|A|)n<2^{70}(j+4)\delta_j^{443/256}e^{-640}\overline X$
及 $w<1$，给
$$
 \boxed{\quad
 \int_{I_i}\|\mathcal C-\mathcal C^0\|\,dt
 <
 \left[
   2^{-8}\frac{\widehat\varepsilon_i}{\kappa_i}
  +2^{70}(j+4)^2\frac{\widehat\varepsilon_i}{h_j}
  +\frac{\widehat\varepsilon_i}{32}
 \right]\overline X.
 \quad}                                                    \tag{A.30}
$$
两端附近，(A.21) 为 $O(s^{3/2})$，
$g_0=O(s^{-1})$，而 $\mathcal R_\sigma=O(\sqrt s)$。
所以实际算子差是 $O(\sqrt s)$，不是仅有一个形式上可消的
无穷大。两端奇异 residue 与参考准确一致。

现在对全部无限分量求和。原真实窗满足
$$
 \kappa_i^2>2^{-55}\delta_j^{3/2}/j,\qquad
 h_j>2^{-4}\delta_j^{1/256}.
$$
于是 (A.30) 三项逐一小于
$$
 2^{100}(j+4)\sqrt j\,
        \delta_j^{251/256}e^{-640},\qquad
 2^{154}(j+4)^3\delta_j^{442/256}e^{-640},\qquad
 2^{75}(j+4)\delta_j^{443/256}e^{-640}.
 \tag{A.31}
$$
在 $j=129$，$\delta_{129}<2^{-132}$，
三个值分别小于 $2^{-657}$、$2^{-689}$、$2^{-785}$。
相邻层比值分别严格小于 $3/4,1/2,1/2$，其多项式比值随
$j$ 继续下降。每层至多两个分量，所以全部求和小于
$$
 2^{-654}+2^{-687}+2^{-783}<2^{-652}.
 \tag{A.32}
$$
这证明 (A.1)，包括4096/4097的真实宽度改变；第二个
全层宽度下界已经覆盖该跳变，没有靠有限样本外推。

全部实际流、KAM 选择和这些差算子对复标签局部全纯，
上式又是可积的共同控制。因此在
$\|a\|_{\ell^1_{224}}\le1/8$ 上，作为
$\ell^1_iL^1_t\mathcal B(\mathcal A_{s+\hbar_i},\mathcal A_s)$
值函数，其全 Fréchet 导数满足
$$
 \|D(\mathcal C-\mathcal C^0)\|<2^{-649},\qquad
 \|D^2(\mathcal C-\mathcal C^0)\|<2^{-644}.
 \tag{A.33}
$$
这里一阶 Cauchy 半径为 $1/8$；对二阶多线性方向各用
$1/16$，所以费用为 $16^2$。
这些导数包含实际 $\Gamma^*(a)$ 和两支角图的全部变化，
不是只微分显式小矩阵。

## 9. 全部 ordinary source、mean 与两个转向迹

(A.14) 的 $F_\sigma$ 是本坐标中的准确 ordinary-source
列。它没有把连续源替换成端口跳量。
需要的 source 范数可以明确写成
$$
 \sum_{\sigma=\pm}
 \int_{I_i}
  \left\|
  J_\sigma\,
  \frac{\widehat s\circ\Theta_\sigma}
       {\sqrt{2\mathfrak k\circ\Theta_\sigma}}
  \right\|_{\mathcal A_s}dt.
 \tag{A.34}
$$
这个合同还有可直接消费的真实单位界。在两胞可能跨接的
$I_i$ 上，单调实际 profile 给
$$
 \frac{\epsilon_{\rm tail}\delta_j^7}{256}
       \le w\le2^{11}\epsilon_{\rm tail}\delta_j^5,\qquad
 a_{\rm phys}\le2\rho(\Gamma).
$$
实际 $\int q^{-1}dt<4\delta_j$ 也可以直接支付。除两个
上升 ramp 的负型端片以外，均有 $q\ge\sqrt7$。
在一个端片写 $q^2=7-30\Lambda x^2(1-x)^2$，
真实 $\Lambda>32$ 保证型别根 $x_0<1/8$。
令 $y=x(1-x)$，则 $dx/dy\le4/3$，所以
$$
 \int_0^{x_0}\frac{dx}{q}
 \le\frac{2\pi}{3\sqrt{30\Lambda}}<1.
$$
另一端片相同，乘回各自真实 $\eta/\sqrt{12}$ 后，
两个端片之和小于 $4\eta_j$；其余段不超过
$|I_i|/\sqrt7<2\delta_j$。故上述 $4\delta_j$ 确有严格余量。
因此
$$
 \int_{I_i}\frac{a_{\rm phys}}{wq}\,dt
 <2^{11}\frac{\rho(\Gamma)}{\epsilon_{\rm tail}}\delta_j^{-6}.
 \tag{A.34a}
$$

下面 (A.34b) 的 $e$ 范数明确在原物理角 $\theta$ 上取值。
因此必须同时支付 hodograph 逆图，不能先付 $\Theta_\sigma$
的宽差后再免费复合 $\chi^{-1}$。
实际 hodograph 小球证明在本篇平移后的角域上原样给
$\|\chi^{-1}-\mathrm{id}\|_{\mathcal A_{64+1/2}}\le64N_i<K_i$。
另一方面，$K_i/\hbar_i<2^{-614}$，每条
$\Theta_\sigma$ 减去其真实标量平移后的角位移小于 $2K_i$。
所以原物理 source 使用的总图
$\chi^{-1}(t,\Theta_\sigma(t,\eta))$
相对于同一个标量平移的位移小于
$3K_i<\hbar_i/4$。这在同一个 $\hbar_i$ 内支付全部复合。
若 $\widehat s$ 已在 hodograph 角给定，结合
$J_\sigma<2$、$\|\sqrt D\|<2$，Cauchy–Schwarz 给
$$
 \sum_{\sigma=\pm}\|F_\sigma\|_{L^1_t\mathcal A_s}
 \le 8
  \left(\int_{I_i}\frac{a_{\rm phys}}{wq}\,dt\right)^{1/2}
        \|\widehat s\|_{L^2_t\mathcal A_{s+\hbar_i}}.
$$
对原物理 $e$ 则直接使用准确的总复合式
$$
 F_\sigma
 =\frac{J_\sigma w^2}{c}
     \sqrt{\frac{a_{\rm phys}}{2wq}}\,
       (D^{-1/2}e)\circ(\chi^{-1}\circ\Theta_\sigma).
$$
已付的小球给 $\|(c\sqrt D)^{-1}\|<2$。由上述总图的同一个
宽差，两个源的和至多
$16w_{\max}^2(\int a_{\rm phys}/(wq))^{1/2}
\|e\|_{L^2\mathcal A_{s+\hbar_i}}$。
这不经过一个未经支付的同宽
$e\mapsto\widehat s$ 复合估计。于是得到原 ordinary Darboux
source 单位中的全频真实合同
$$
 \boxed{\quad
 \sum_{\sigma=\pm}\|F_\sigma\|_{L^1_t\mathcal A_s}
 <2^{32}\epsilon_{\rm tail}^{3/2}\rho(\Gamma)^{1/2}
       \delta_j^7\,\|e\|_{L^2_t\mathcal A_{s+\hbar_i}} .
 \quad}                                                     \tag{A.34b}
$$
对无限多个分量可直接对右端求和；这是明确的实际加权
source 合同，而不是声称未加权 $L^2$ 具有一个与层无关的
免费逆。它仍不是经过缺失 Airy/positive-network Green
之后的强 source norm。

从两支振幅准确恢复
$$
 p=\sqrt{\mathfrak k/2}(W_++W_-),\qquad
 z=(W_+-W_-)/\sqrt{2\mathfrak k}.
 \tag{A.35}
$$
在原 $t,\xi$ 截面，
$$
 \langle p\rangle
 =\frac1{\sqrt2}\sum_{\sigma=\pm}
      \left\langle
       (\sqrt{\mathfrak k}\circ\Theta_\sigma)Z_\sigma
      \right\rangle=\dot M,
$$
$$
 \langle z\rangle
 =\frac1{\sqrt2}
  \left[
   \left\langle(\mathfrak k^{-1/2}\circ\Theta_+)Z_+\right\rangle
  -\left\langle(\mathfrak k^{-1/2}\circ\Theta_-)Z_-\right\rangle
  \right]=0 .
 \tag{A.36}
$$
第一行的导数仍是 $\partial_t\langle p\rangle=\langle\widehat s\rangle$。
第二行是完整高度兼容条件；不能把两支各自的未加权零模设为0。
独立平均高度还必须从
$\widehat h_t=bz+p/\widehat\mu$ 积分恢复。

在转向端，(A.35) 要求的是
$\sqrt{\mathfrak k}(W_++W_-)$ 与
$(W_+-W_-)/\sqrt{\mathfrak k}$ 的真实有限迹，
而不是 $W_+$、$W_-$ 分别有任意有界极限。
右端使用 (A.16) 的准确相位对齐两支后再取这些组合。
完整原 raw 高度与 flux 因而保留；原 grounded
normal/shear 与水平重建仍由同一物理两迹公式恢复。
度量参数改变时，还须保留前篇给出的
$A_\Gamma\delta\ell$ 尺度源及 mean 的移动切口项。

## 10. 本结果之后真正剩下的算子任务

本篇已经支付以下困难：实际非径向漂移保真；
完整 Riemann 密度及 source 正确；
两支真正往返在两端准确匹配；
原仅 $C^2$ 径向接缝不会被混入角；
急坡肩和 $q_t/q$ 的转向奇性均进入实际可积界；
所有角频的复合差消耗明确的 $h_j/64$，而不是同宽小量。

仍须证明的是：在同一完整网络的 Airy 两迹空间中，
把 (A.29) 的扰动作用在参考转向 Green 上之后，具有足够的
**相对**范数，并与相邻正型段的完整双端 DN、最外有限
connector、所有 ordinary/metric source 及 mean 一起接合。
参考 $\mathcal C^0$ 本身含不可直接作无权 $L^1$ Gronwall
的转向 residue，所以不能由 (A.1) 直接声称这个结论。
本篇也不将生成元的一次角宽费用偷换为已经闭合的无限次
Newton 宽度账。

[完整代数与全层门程序](../scripts/fourfold_actual_ray_amplitude_20261113.py)
以及
[可重跑报告](../notes/2026-11-13-R119-actual-ray-amplitude-budget.json)
保存此次结论的真实输入、分段/全层预算和依赖哈希。
