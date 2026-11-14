# R119 续篇：低缩放段的实际全频局部非径向正定型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对同一个当前非径向尾解、同一个固定
$\Gamma$，在第67束真实未使用区间内部，本篇将完整 Sym2 正定
方向转为实际 Jacobi 的局部控制型。中心输入可同时含
$m=\pm M$ 的任意高度和通量；真实输出含全部 Fourier 模和
两个 mean。固定标签的实际 gauged 背景响应在整个所用小区间
上积分，未只在方向支集上取值。

在原标签球 $\mathcal X\le2^{-262144}$ 和
$2^{-40}\delta_j^{-1/8}\le M\le\sqrt B$ 下，全部误差与第67束
$d_*=2^{-22000}M^{50}B^{-39}\Delta^{-103}$ 的比小于
$2^{-33000}$。所以局部真实控制型在完整单模两态上大于
$d_*/8$。它不是只对某一 rank-one 或 cos 相位的结论。

**准确范围：** 此处保持当前 $\Gamma$ 固定，使用真实
$D_\psi X$。小区间外的背景响应、沿实际联立选择支的
$D_\psi\Gamma^*$ 两列、完整 pocket 端图和不同 $M$ 的近共振簇
仍须另外接合。本篇没有把这个内部正定型称为整个
$S_i$、全网络或 $\mathcal F$ 的逆。

## 1. 实际对象、两迹及中心输入

保持[控制后真实全图](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
的同一背景、同一个实参数点。令 $j\ge8193$，
$I\subset[7/16,15/32]$ 为真正尚未使用的区间，
$Q=7+Bf(x)$、$dt=a_r\,dx$、$a_r=\Delta/B$。
本篇写 $a_r$ 以区别实际逆密度 $a=\mu^{-1}$。
两个先前补偿 bump 和其它形状的支集离开 $I$。

令
$$
 n=\sup_I w^{-1}
       (\|p\|_{\mathcal A_2^2}+\|k\|_{\mathcal A_2^2}),
 \quad {\cal N}_j=(N_j^c)^\#=N_j^c+N_{j-1}^c,\quad
 n\le4{\cal N}_j\mathcal X,
$$
$$
 N_j^c=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2}.
                                                               \tag{L.1}
$$
整个内部片位于第 $j$ 个胞元，不把跨两个胞元的 whole pocket
另一个贡献偷偷并入 (L.1)。

使用[完整 canonical 变分](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
的原物理角 $\theta$、真实高度和 total flux：
$$
 Y=(h,\pi),\quad
 h_t=dh_\theta+a\pi,\quad
 \pi_t=\partial_\theta(d\pi)+Q\partial_\theta(c h_\theta).
                                                               \tag{L.2}
$$
$\mu_0=w/r$ 为同一当前径向参考，令
$u=\sqrt{\mu_0}h$、$v=\pi/\sqrt{\mu_0}$。
在中心 $t_c$ 用一个固定的参考坐标来量输入：
$$
 Z_M=\left(\sqrt{k_M}\,u,\,
       \frac{v-(1+Q(t_c))u/2}{\sqrt{k_M}}\right),
 \qquad k_M=\sqrt{7M^2-16}.                            \tag{L.3}
$$
这是当前物理两迹的明确线性变换。对参考解其第二项是
$u_t/\sqrt{k_M}$；对非径向解，不把它误写成实际 $u_t/\sqrt{k_M}$。

令 $\mathcal E_M$ 为两个物理迹同时支持在 $m=\pm M$ 的空间。
可以取实或复数据；不限定两迹比例、cos/sin 相位或实部/虚部。
以下 $\|Z_M\|_2^2$ 是两个角模式和两个状态的完整和。

## 2. 新质量项支付低缩放的全部输出

置
$$
 \Omega_M=B+M\sqrt B,\qquad
 \gamma=1+\Delta+a_rM\sqrt B,\qquad
 J_0=\{|x-c|\le r_0\},\quad
 r_0=\min(\ell/8,2^{-12}/\gamma).
                                                               \tag{L.4}
$$
对 $0\le k\le3$ 采用完整空间 norm
$$
 \begin{aligned}
 \|Y\|_{\mathcal N_{M,k}}^2
 =\sum_{l=0}^k M^{-2l}\{&
  \Omega_M\|\partial_\theta^l u\|_2^2+
  (B/\Omega_M)\|\partial_\theta^{l+1}u\|_2^2\\
 &+\Omega_M^{-1}\|\partial_\theta^l v\|_2^2\}.
 \end{aligned}                                                \tag{L.5}
$$
这里 $M$ 只是当前比较尺度，输出不投影到这个频带。高度 mean
有正的 $\Omega_M$ 权，通量 mean 有正的 $\Omega_M^{-1}$ 权。

准确能量为
$$
 E_{M,0}=\langle cQ|h_\theta|^2+a|\pi|^2+
                         \mu_0\Omega_M^2|h|^2\rangle,
 \qquad
 E_{M,k}=\sum_{l=0}^kM^{-2l}E_{M,0}(\partial_\theta^lY).
                                                               \tag{L.6}
$$
由原有理系数及角宽2到1，
$$
 \tfrac12<a\mu_0,c/\mu_0<2,\quad
 \sum_{l=0}^4\big(
 \|\partial_\theta^l(a\mu_0-1)\|_\infty+
 \|\partial_\theta^l(c/\mu_0-1)\|_\infty+
 \|\partial_\theta^ld\|_\infty\big)<2^{24}n .
                                                               \tag{L.7}
$$
同时 $7B/4<Q<2B$、$|Q_t|/Q<2/a_r$。所以
$$
 \tfrac12\|Y\|_{\mathcal N_{M,k}}^2
       < E_{M,k}/\Omega_M
       <4\|Y\|_{\mathcal N_{M,k}}^2.                  \tag{L.8}
$$

第62束 (W.7)--(W.10) 的完整分部积分依然准确成立。
新质量的对数径向导数仍是 $-1-Q$；其两状态交叉费现在小于
$3\Omega_M$。角导交换子的两个波动方向付
$2^{40}nM\sqrt B$；新质量与 $a_\theta\pi$ 等项的交换子另付
$2^{40}n\Omega_M$，不能仍用旧高缩放质量的费用代替。
两者合计小于 $2^{41}n\Omega_M$。于是对全部 $k\le3$，
$$
 |(E_{M,k})_t|
 \le(3\Omega_M+8B+|Q_t|/Q+
                      2^{41}n\Omega_M)E_{M,k}
 <16\Omega_ME_{M,k}.                                 \tag{L.9}
$$
此处用实际 $n<2^{-4096}$，它在第6节由原球直接核实。
特别没有要求 $M\ge\sqrt B$。

$a_r\Omega_M=\gamma-1$，故整个 $J_0$ 的物理长度小于
$2^{-11}/\Omega_M$。由 (L.8)--(L.9)，同一个当前实际算子、
其正反演化和同一径向参考都满足
$$
       \|C(t,s)\|_{\mathcal N_{M,k}\to\mathcal N_{M,k}}<8,
       \qquad s,t\in J_0,\quad0\le k\le3.              \tag{L.10}
$$
这是整个 Fourier 空间的能量证明，未用低输入的有限维性
来假设输出也低频。

## 3. 同物理中心数据的真实 Cauchy 差

令 $Y,Y^0$ 分别是真实和参考解，具有相同中心两迹，中心可先
取在 $M\le|m|\le2M$。它们的差满足真实齐次系统加
$$
 F=dh^0_\theta+(a-a_0)\pi^0,\qquad
 G=\partial_\theta(d\pi^0)
               +Q\partial_\theta[(c-c_0)h^0_\theta]. \tag{L.11}
$$
源 norm 同时含 $F,\partial_\theta F,G$，即把 $(F,G)$ 按
(L.5) 的状态位置逐项量取。完整角乘积和 (L.7) 给
$$
       \|(F,G)\|_{\mathcal N_{M,k}}
       <2^{40}n\Omega_M
                            \|Y^0\|_{\mathcal N_{M,k}}
                    \quad(0\le k\le2).               \tag{L.12}
$$
例如 $(a-a_0)\pi^0$ 的高度源费用为 $\Omega_M n$；
通量中的 $(c-c_0)h^0_{\theta\theta}$ 付
$BM^2/\Omega_M\le M\sqrt B\le\Omega_M$。
没有在这里漏掉低缩放下的 $B$ 项。

一次真正 Duhamel、两个 (L.10) 和完整长度给
$$
 \|Y(t)-Y^0(t)\|_{\mathcal N_{M,k}}
      <2^{64}n\|Y(t_c)\|_{\mathcal N_{M,k}},
                  \qquad t\in J_0,\quad0\le k\le2.    \tag{L.13}
$$
未取整费用 $8^2\,2^{40}\,2^{-11}=2^{35}$。
输出产生的 mean、相反锥及无限 Fourier 尾都在此式中。

## 4. 在真两迹中比较整个控制型

使用第61束的准确 $\mathcal K_{\rm act}$、
$\mathcal K_0$ 和 $\mathcal H_{\widehat z}$。从 (L.5) 直接有
$$
 \|u_\theta\|\le\sqrt{\Omega_M/B}\|Y\|_{\mathcal N_{M,0}},
 \quad\|v\|\le\sqrt{\Omega_M}\|Y\|_{\mathcal N_{M,0}},
 \quad\|v_\theta\|\le M\sqrt{\Omega_M}\|Y\|_{\mathcal N_{M,1}}.
$$
所以混合项 $u_\theta v_\theta$ 付
$M\Omega_M/\sqrt B$，不先粗替成两个各向同性平方。
令 $H_M=(\sqrt B+M)^2$。准确式 (J.13) 及其商式导数给
$$
 |\mathcal K_{\rm act}(Y)-\mathcal K_0(Y)|
          <2^{24}nH_M\|Y\|_{\mathcal N_{M,1}}^2,
$$
$$
 |\mathcal K_0(Y)-\mathcal K_0(Y^0)|
 <8H_M(\|Y\|_{\mathcal N_{M,1}}+
                    \|Y^0\|_{\mathcal N_{M,1}})
                              \|Y-Y^0\|_{\mathcal N_{M,1}} .
                                                               \tag{L.14}
$$
这里 $\mathcal K_0$ 对任意全频场按
$\|u_\theta\|^2+\|v\|^2-2\operatorname{Re}
\langle u_\theta,v_\theta\rangle$ 计算。

中心 band 输入有 $\|Y_c\|_{\mathcal N_{M,1}}\le
\sqrt5\|Y_c\|_{\mathcal N_{M,0}}$。
由 (L.10)、(L.13) 可统一放宽为
$2^{96}nH_M\|Y_c\|_{\mathcal N_{M,0}}^2$ 的点态差。
对于 $\mathcal E_M$ 上的完整两迹，(L.3) 准确给
$$
 \|Y_c\|_{\mathcal N_{M,0}}^2
     <16(B/M+\sqrt B)\|Z_M\|_2^2.                     \tag{L.15}
$$
其中 $v=\sqrt{k_M}(Z_M)_2+
(1+Q)(Z_M)_1/(2\sqrt{k_M})$；所以真实 normal shear 已计入。

取第67束的全部 Sym2 方向 $\psi$，支集尺度
$$
 \rho=2^{-2204}M^5B^{-4}\Delta^{-11},\qquad M^2\le B .
$$
它满足 $\int|\psi|dt\le2a_r\rho^5$，因此整个实际差有
$$
 \left|\int_{J_0}\psi[
       \mathcal K_{\rm act}(Y)-\mathcal K_0(Y^0)]dt\right|
 <2^{112}a_r n\,\frac{B^2}{M}
       (1+\sqrt\kappa)^3\rho^5\|Z_M\|_2^2 .           \tag{L.16}
$$
此式同时包括实际系数变化和真实解离开参考模后的一切反馈。

对固定标签的真实 gauged 背景响应
$\widehat z=D_\psi(p,k)-\psi F_1$，写
$$
 \widehat n=\sup_{J_0}w^{-1}
       (\|\widehat p\|_{\mathcal A_2^2}
                         +\|\widehat k\|_{\mathcal A_2^2}).
$$
准确商法则分别给
$Q\widehat c|h_\theta|^2$ 与
$\widehat a|\pi|^2$ 的相对费用；不得把第一个 $Q$ 乘到后者。
由 (J.14) 有
$$
       |\mathcal H_{\widehat z}(Y)|
       <2^{24}\widehat n\,\Omega_M
                              \|Y\|_{\mathcal N_{M,0}}^2 .
$$
在整个 $J_0$ 积分而不是只在 $\operatorname{supp}\psi$ 积分，
得到
$$
 \left|\int_{J_0}\mathcal H_{\widehat z}(Y)\,dt\right|
       <2^{40}\widehat n\|Y_c\|_{\mathcal N_{M,0}}^2
       <2^{45}\widehat n(B/M)\|Z_M\|_2^2.              \tag{L.17}
$$
最后一步此时使用 $\kappa\le1$。
第60束的完整两分量、前两角导响应在本方向上准确适用：
$$
 \widehat n<2^{832}{\cal N}_j\mathcal X
                  P_j\rho^5,\qquad
 P_j=h_j^{-14}\delta_j^{-7/4}.                        \tag{L.18}
$$
因为新方向的 $0,\ldots,4$ 阶 $L^1$、$L^\infty$ 预算正是
$2\rho^{5-l}$、$\rho^{4-l}$，原局部响应门的输入没有改变。

## 5. 对完整单模两态的实际正定性

第67束给同一个 $\psi$：
$$
 \int_{J_0}\psi\mathcal K_0(Y^0)\,dt
       =\langle Z_M,L_\psi Z_M\rangle,\qquad
       L_\psi=(d_*/4)I,\quad
 d_*=2^{-22000}M^{50}B^{-39}\Delta^{-103}.
                                                               \tag{L.19}
$$
对 $m=\pm M$ 两个角模式分别成立，正交性将它们相加；
任意复两态也由同一个实对称正矩阵控制。

定义完整内部实际型
$$
 \mathfrak G_{J_0}(Y_c)
   =\int_{J_0}\{\psi\mathcal K_{\rm act}(Y)
                       -\mathcal H_{\widehat z}(Y)\}\,dt.       \tag{L.20}
$$
所有 actual outputs 都由 (L.2) 产生，不在积分中投回
$\mathcal E_M$。它就是第61束 (J.15) 在这两个实际截面之间的
真实 Cauchy 变分 pairing；$\psi$ 在两端为零，因此局部 shear
gauge 没有隐藏的端项。

将 (L.16)--(L.18) 除以完整 $d_*$，使用
$a_r=\Delta/B$、$\rho^5=2^{-11020}M^{25}B^{-20}\Delta^{-55}$，
得到以下共同充分界：
$$
 \frac{|\mathfrak G_{J_0}(Y_c)
               -(d_*/4)\|Z_M\|_2^2|}
                       {d_*\|Z_M\|_2^2}
 <2^{14000}{\cal N}_j\mathcal X
                          J^{70}\delta_j^{-3655/128}.           \tag{L.21}
$$
这里逐项的幂如下。直接项先为
$2^{11095}nB^{20}\Delta^{49}M^{-26}$；
响应项先为
$2^{11857}{\cal N}_j\mathcal XP_jB^{20}\Delta^{48}M^{-26}$。
用 $n\le4{\cal N}_j\mathcal X$、
$B<2^7J\delta^{-3/2}$、$\Delta<3J$、
$M^{-26}\le2^{1040}\delta^{13/4}$，
直接项的 $\delta$ 费是 $107/4$。
深尾 $h_j=8\delta_j^{1/256}$，故
$$
 P_j=2^{-42}\delta_j^{-231/128},\qquad
 107/4+231/128=3655/128.
$$
两个完整常数均低于 (L.21)，没有除一个未实际归一的极小 trace。

## 6. 原真实标签球支付全部无限层

必须保留原两个全局因子。它们在第8192层准确给
$$
 N_{8192}^c
   =2^{185}\delta_{4096}^{-3/2}\delta_{8192}^{827/256}
   <2^{-20138}.                                             \tag{L.22}
$$
这一步使用原 $\zeta=\epsilon\delta^{39/4}$、
$\mu=\epsilon\delta_{4096}^{3/2}\delta^{9/2}$，
没有把 $\delta_{4096}^{-3/2}$ 删除。
仅用 $3<\log_2(25/2)<4$，其对数上界已经是
$-5155505/256<-20138$。

对 $j=8193+q$，新 $\zeta$ 的
$\delta_{8192}^{-485/4}$ 恰保证第8192层匹配，因此准确有
$$
 N_j^c=N_{8192}^c\,2^{-(31867/256)(j-8192)},\qquad
 {\cal N}_j<2^{-19997}\,2^{-(31867/256)q}.              \tag{L.23}
$$
这里显式向上放宽了数个二倍因子，不以原高层粗 sup 替代真实
深层衰减。由此 $n<2^{-4096}$，先前能量门的输入真实满足。

在 $j=8193$，$J<2^{14}$、$\delta_j^{-1}<2^{8197}$ 和
$\mathcal X\le2^{-262144}$ 给 (L.21) 的二进制指数上界
$$
 14000-19997-262144+14\cdot70+8197\cdot3655/128
                      =-4236573/128<-33098.            \tag{L.24}
$$
每前进一层，$J^{70}$ 的比小于 $2^{1/64}$；
这是
$(1+1/8198)^{70}<97/96$ 与 $(97/96)^{64}<2$
的真实有理门。其余比例为
$2^{-(31867/256-3655/128)}$，合起来小于 $2^{-95}$。
因此整个无限深尾都有
$$
 \boxed{\quad
 \mathfrak G_{J_0}(Y_c)>
                 \frac{d_*}{8}\|Z_M\|_2^2
              \quad(Y_c\in\mathcal E_M).\quad}         \tag{L.25}
$$
这次吸收使用同一原标签球，不要求重新选较小的抽象球，
也没有把 $M^{-1891}$ 与绝对算子差相乘。

## 7. 完整 source、mean 及没有授予的外部行

若有实际 ordinary $g$ 和 weak $(F^t,F^\theta)$，原状态源是
$$
 (F,G)=(-aF^t,\;g-\partial_\theta(F^\theta+dF^t)).
                                                               \tag{L.26}
$$
只要将该完整向量按 (L.5) 的两个状态位置及所需角导量取，
(L.10) 的真实 Duhamel 给
$$
 \|Y(t)\|_{\mathcal N_{M,k}}
 \le8\left(\|Y(s)\|_{\mathcal N_{M,k}}
             +\int_{\min(s,t)}^{\max(s,t)}
                         \|(F,G)\|_{\mathcal N_{M,k}}\,d\tau\right).
                                                               \tag{L.27}
$$
这里不要求 $F^t_t$。mean 准确为
$\pi_{0,t}=g_0$、
$h_{0,t}=\langle dh_\theta+a\pi-aF^t\rangle$；
并且 bare flux 的两端恢复仍为 $\pi-F^t$，若消费者需要它，
必须另有实际 $F^t$ 端迹，不能由积分 norm 自动得到。

对参数源还保留原 $\dot s-\psi\mathsf Bs$，与 (L.26)
按同一有序两行共同进入。仿射源、两个 mean 和非零初值没有
被正定性命题规定为零。

最后，(L.20) 的背景响应只在 $J_0$ 积分。完整 pocket 的
变分还含 $I_i\setminus J_0$ 上的 $\widehat{\mathsf A}$、当前
principal 端图以及两条 $D_\psi\Gamma^*$ 响应。不同频率的
输入也未因 (L.25) 而被正交化：实际非径向算子会混频，
本篇只证明其在明确中心空间 $\mathcal E_M$ 上的整个型。
这些是下一次全网络近簇接线的真实剩余。

实际必要有理预算：

- [源码](../scripts/fourfold_actual_low_scaled_nonradial_positive_form_20261114.py)；
- [原生记录](../notes/2026-11-14-R119-actual-low-scaled-nonradial-form-budget.json)。
