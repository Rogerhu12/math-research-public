# R653 离解归一位置的真实竖直接柱、端部余量与正图邻域

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

**已证明。** 在原固定 $E$、真种子与全角正速度的源合同下，
[R643](R643-fixed-metric-unsolved-mean-height-and-periodic-position-system.md)
的实际周期位置即使在主体没有解出 $F,G,S=0$，仍可 $C^2$ 接到它自己在
$r=R$ 的竖直柱。下面由原真实 basis 推出所需端部二阶估计，并给一个可检验的
边缘余量。该余量严格为正即有实际正平面 Jacobian 的开邻域。对准确连续硬迹，
这个余量就是严格正的核心速度下界；有限角求得的硬迹可直接用其实际误差计算。
不移动外缘，也不将端点极限宣称为已知宽度的认证。

## 1. 正则函数类与两个需要保留的比

置 $\delta=R-r,\ L=1/W$，$1/2<\alpha<1$。本真实背景在充分近外缘处为
\[
 W=\delta^{-\alpha} w_0(\delta)+w_1(\delta),\quad w_0(0)>0,        \tag{1}
\]
$w_0,w_1$ 在那里光滑。原 core onset cutoff 在此恒为一；
$r576$ 的真实项为
$k t^\beta/[(1-t)(1+t)]^\alpha,\ t=1-\delta/(R-r_{\rm start})$，
其余是原光滑 finite slope。这给 $L\asymp\delta^\alpha$、
$L'=O(\delta^{\alpha-1}), L''=O(\delta^{\alpha-2})$，
$L'/L=-\alpha/\delta+O(\delta^{\alpha-1})$。这里及下文撇指 $r$ 导数。
根本不需要将 $L$ 的一阶导数错误当作有界。

记 $\mathcal J$ 为有 $C^1$ 外端延伸且 $|\partial_r^2 f|\le C/\delta$
的函数，角导数统一到所用阶数，分段样条在最后一个结点之后取其真实多项式。
$\mathcal J$ 对加乘与紧正域内的光滑复合封闭：二阶导数里两个一阶因子的乘积
有界，一项二阶导数最多 $O(1/\delta)$。角均值和连续零均值原函数 $\Pi$
是有界线性算子，也保持此类。$L^2\in\mathcal J$，因为
$(L^2)'=O(\delta^{2\alpha-1})\to0$ 且 $(L^2)''=O(\delta^{2\alpha-2})$。
这里用到了 $\alpha>1/2$。

真实高度 $Z$ 在 $R$ 是常数，定义总通量
\[
 C=W(Z_r+W),\quad C_0=C(R,\theta),\ C_1=C_r(R,\theta),\qquad
 p=Z_r=-1/L+LC,\quad q=Z_\theta,\quad t=Z_{\theta\theta}.        \tag{2}
\]
$C$ 包含固定种子与自由 mean 的真实贡献，不是仅含角模的 $P$。
第2、3节将对原场证明 $C\in\mathcal J$。有此输入时，对 $D=C_\theta$ 或
$C_{\theta\theta}$ 定义
\[
 I_D=-\int_r^R L(x)D(x)\,dx,\qquad J_D=I_D/L .
\]
分别是 $q$ 或 $t$ 及其除 $L$ 的比。由(1)和 $D\to D_0$，
\[
 I_D=O(\delta^{1+\alpha}),\quad
 J_D=-D_0\,\delta/(1+\alpha)+o(\delta),\qquad
 (J_D)_r=D-(L'/L)J_D\longrightarrow D_0/(1+\alpha).
\]
再求导，用 $(L'/L)'=O(\delta^{-2})$，得 $(J_D)_{rr}=O(\delta^{-1})$。
原 $I_D$ 也在 $\mathcal J$。上述极限在角圆上一致。因此 $q,t,q/L,t/L$
均在 $\mathcal J$，并有
\[
 pq=(-1+L^2C)q/L,\qquad pt=(-1+L^2C)t/L \quad\hbox{属于 }\mathcal J. \tag{3}
\]

## 2. 原高度源的三阶代价

原实际 $\bar f$ 代表 reference、固定 seed 或试值的角高度。对原每一齐次 core
germ $f(R)=0$，[R597](R597-nonlinear-core-trace-and-realizable-free-order.md)
给 $P=Wf_r$ 的 $C^1$ 延伸。其准确方程为 $rP'=j^2W'f$，所以
\[
 P''=j^2(W''f/r+W'f_r/r-W'f/r^2)=O(\delta^{-1}).                \tag{4}
\]
这里 $W''=O(\delta^{-\alpha-2})$、$f=O(\delta^{1+\alpha})$、
$f_r=O(\delta^\alpha)$。因 $f_r=LP$，还得到齐次 germ 的
$f_{rr}=O(\delta^{\alpha-1}),\,f_{rrr}=O(\delta^{\alpha-2})$。
真 $r$-ODE 在外缘邻域成立；旧两侧组合的 cutoff 与此邻域有正距离。
具体连接/归一的有限数值误差仍是原源误差。

对原 post-tanh 的 forced $j=4$ 不可使用齐次式。原
r576_body_forced_j4_height_20261126.py 的真实强迫满足
$rP'_4=16W'f_4+B_4$。近核心 cutoff 为一，以原齐次 $j=2$ 场 $f$、
$\mu=4$、$e_0=1+W^2$ 表示，
\[
\begin{split}
2B_4={}&(r f_r-\mu e_0 f)f_{rr}+\mu W W' f f_r\\
       &+\mu e_0(f_r-f/r)^2-\mu W W'f^2/r .
\end{split}                                                       \tag{5}
\]
用(4)的各阶以及 $|W^{(d)}|=O(\delta^{-\alpha-d})$（$d\le2$），
(5)右端逐乘积为 $O(1)$，对各项取一次径向导数均为 $O(\delta^{-1})$。
例如 $W^2 f f_{rr}=O(1)$，$W^2 f f_{rrr}=O(\delta^{-1})$；
$W W'f f_r=O(1)$，其导数使用 $W''$ 与原 $f_{rr}$。
故 $B_4'=O(\delta^{-1})$，在原真实 $C^1$ 通量端迹下同样有
$P_4''=O(\delta^{-1})$。其真实系数、归一和源 $B_4(R)$ 均保留。

其余真实项逐类如下。

- 原四个 pre-tanh germ，平方和加
  $e^{-\gamma/(r-r_c)^4}\delta^{2+2\alpha}$ 的 envelope，及原 quintic
  spline 最后一段：germ 用(4)。envelope 及其 $d\le3$ 阶逐项为
  $O(\delta^{2+2\alpha-d})$，最后结点段各多项式导数有界。其通量的二阶
  为 $O(\delta^{\alpha-1})$。不接触核心的 local-extra 在此支撑为零。
- 对原 $\sigma\tanh(V/\sigma)$，$V=O(\delta^{1+\alpha})$ 且前三导依次减幂；
  饱和项与 $V$ 的差为 $O(\delta^{3+3\alpha})$，前三导依次减少相应幂次。
  原 canonical512 同步减均值因是有限固定线性和而保持这组界。原十条
  post、十条响应齐次 germ 与(5)的固定 forced 项全部保留。
- 原61条 bulk 每条近 $R$ 是有界光滑函数乘 $\delta^{\alpha+2}$，
  对应 $Wf_r=O(\delta)$，其一阶有极限，二阶 $O(\delta^{\alpha-1})+O(1)$。
  既有 dependent $P_1$ 和 $2J$ 核心修正同阶。原第一迹 lift 是准确积分
  $A_0=-\int_r^R L$，故在该邻域 $WA_0'=1$。第二迹 lift
  $B_0=\delta^{\alpha+2}/[k(\alpha+2)]$，$k=w_0(0)$，
  有 $WB_0'=-\delta(1+O(\delta^\alpha))$ 和外端一阶迹 $1$。
  此处(1)的余项连同其导数一起使用。
- 原 compact 角列和真实 inner Gaussian 在近外缘支撑为零。94条独立 mean 中，
  61条是上述 bulk 去除第二迹 lift，28条 compact、4条 Gaussian 也在这里为零，
  最后一条 plateau 在这里恒为一，保留核心高度值、其斜率为零。
  所有从属 mean 第一、二迹 lift 仍按其真实系数加入。

由此各实际角场的 $P=W\bar f_r\in\mathcal J$，且 $\bar f(R)$ 无角依赖。
原 seed mean 仍须按其自己定义单独求得，不能把上述有限角系数表当作其值。

## 3. 固定 e 与固定 seed 均值的二阶界

写冻结 $E=W^2+e$。真实稳定式为
\[
 b^2=r^2-q^2,\quad N=r/b+r^2pt/b^3,\quad
 v^2=e+2C-L^2C^2-(pq/b)^2,\quad a=N/v.                          \tag{6}
\]
这由 $E-p^2$ 先消精确 $W^2$ 项得到，对离解场也是恒等式。
求固定 reference 时 $C=P^0$ 已由第2节给出。把 $e$ 当成独立标量，
在端点正支 $e+2P^0_0>0$ 上，(3)(6)对 $r$ 属 $\mathcal J$；
混合 $r,e$ 一阶和两阶纯 $e$ 导数有界。设 $B=\langle a\rangle-1$，
\[
 B_e(R)=-\tfrac12\langle(e_R+2P^0_0)^{-3/2}\rangle<0 .
\]
原同一转角根的 $C^1$ 端延伸见 R587/R618；也可直接对(6)用单侧隐函数定理。
再对实际隐式关系 $B(r,e(r))=0$ 求导，
$e''=-(B_{rr}+2B_{re}e'+B_{ee}(e')^2)/B_e=O(\delta^{-1})$。
这里是固定的连续 $e$，没有重新拟合 $E$。

固定 seed 令 $C=P^s+\zeta_*$，$\zeta_*=W m_*'$。其角导数
完全来自 $P^s$，所以 $q,t,q/L,t/L$ 已事先由第2节控制，
不依赖待选标量 $\zeta$。将已得 $e$ 放入(6)，在原连续 seed 分支上用
$\langle a\rangle=1$ 对 $\zeta$ 求导；$N_\zeta(R)=0$、
$(v^2)_\zeta(R)=2$，故 $B_\zeta(R)=-\langle v_R^{-3}\rangle<0$。
与上一段相同的二阶隐式公式给 $\zeta_*''=O(\delta^{-1})$，
$\zeta_*\in\mathcal J$。这是外端正的核心隐式分母，与内帽退化不同。
对试值，令 $\Delta m$ 为独立 mean 与从属 mean lift 的总高度修正，则
$C=W\bar f_r+\zeta_*+W(\Delta m)'$。第2节给出各项均在
$\mathcal J$，不用对试值再解隐均值。

## 4. 真实归一位置的全部二阶端迹

假设试值外端 $v_0^2=e_R+2C_0>0$ 全角严格成立。由连续性和(6)，
在真外缘内侧 $b,v,N>0$，且 $v,N,a,\mathcal A=\langle a\rangle$ 属
$\mathcal J$（$\mathcal A>0$）。保持 R643 的准确归一
\[
 \phi=\theta+\Pi a/\mathcal A,\quad n=(\cos\phi,\sin\phi),\
 T=(-\sin\phi,\cos\phi),\quad Y=\Pi(bT),\quad Y_\theta=bT.
\]
故 $Y_r$ 在外缘有连续极限且 $Y_{rr}=O(1/\delta)$，对角圆一致。
这从真实位置的定义给出，在主体并未使用 $S=0$。

用同一目标弧长 $ds=\sqrt E\,dr$；它在外缘有限，因为 $\alpha<1$。
\[
 \chi=dr/ds=\frac L{\sqrt{1+eL^2}}=O(\delta^\alpha),\qquad
 \chi\chi_r=O(\delta^{2\alpha-1}),\qquad
 Z_s=\frac{-1+L^2C}{\sqrt{1+eL^2}}\longrightarrow-1 .
\]
$Z_s\in\mathcal J$，故 $Z_{ss}=\chi(Z_s)_r\to0$。又有
\[
 Y_s=\chi Y_r\to0,\qquad
 Y_{ss}=\chi\chi_rY_r+\chi^2Y_{rr}=O(\delta^{2\alpha-1})\to0,
 \qquad X_{s\theta}\to0.                                       \tag{7}
\]
混合导数的水平项为 $\chi(b_rT+b\phi_r JT)$，竖直项为 $\chi LC_\theta$；
这两项均趋零。$Y_\theta\to RT_0$，
$Y_{\theta\theta}\to-Rk_0 n_0$，$k_0=(1/v_0)/\mathcal A_0>0$；
$q,t\to0$。所以接 $X(s_R+\xi,\theta)=(Y_R(\theta),Z_R-\xi)$ 时，
位置、两条切向与全部二阶偏导都连续匹配。真实边缘曲线以角参数速度 $R$
走一周，严格正转向与其 $\pi$ 对称性给闭合严格凸曲线。
R649 的真实法向趋 $n_0$，两主曲率趋
\[
 \{\,0,\ -k_0/R\,\}=\{\,0,\ -1/(R\mathcal A_0 v_0)\,\}.           \tag{8}
\]
这是实际闭合曲线的柱面。有限转角误差若使 $\mathcal A_0\ne1$，
不能在端点直接把 $k_0$ 认成 $1/v_0$。

## 5. 完整离解残差的外端值与内侧严格正图

(3)及(6)给 $N_r(R)=-C_{0,\theta\theta}/[R(1+\alpha)]$，
$(v^2)_r(R)=e'_R+2C_1$。R643 的 $K=r^2p(p_\theta-q/r)/(vb^3)$
则趋 $-C_{0,\theta}/(R v_0)$，其角导数也收敛。
用 $R_{\rm conn}=a_r-K_\theta$ 而非相减发散项，得到
\[
 \boxed{\ R_{\rm conn}(R,\theta)=\frac{D_0(\theta)}{R v_0^3},\qquad
 D_0=-R C_1+\frac{\alpha}{1+\alpha}v_0^2 C_{0,\theta\theta}
               -(C_{0,\theta})^2-\frac R2 e'_R.\ }                 \tag{9}
\]
$F_0=\mathcal A_0-1,\ G_0=\langle R_{\rm conn}(R)\rangle$ 是准确端值。
$\mathcal H$ 仍取 R643 的完整原平面向量。由于 $v_T=-pq/b\to0$，
$v_\theta\to C_{0,\theta}/v_0$，
\[
 Y_r(R)=v_0 n_0+\Pi\mathcal H_0,\qquad
 \mathcal H_0=\frac{F_0}{\mathcal A_0}(T_0+v_{0,\theta}JT_0)
 +\frac R{\mathcal A_0}\{\Pi R_{\rm conn,0}
                 -(\Pi a_0)G_0/\mathcal A_0\}JT_0 .                \tag{10}
\]
所以 $\sqrt E\,S=\Pi\mathcal H\to\Pi\mathcal H_0$；仅用 $S\to0$
会漏掉边缘的一个有限物理缺陷。

令 $u_-=\min v_0>0$（有证下界亦可）、$A_->0$ 是 $\mathcal A_0$ 下界；
$D_+$ 包围 $\sup|D_0|$。置 $J=D_+/(R u_-^3)$，
$p_a=(\pi/4)(1/u_- -1/u_+)$，其中 $u_+$ 是 $v_0$ 的上界；
该 $p_a$ 来自先减去常数 $1/u_+$ 再取标量周期原函数。则
\[
 \Delta=\frac{\pi}{2}\left[
 \frac{|F_0|}{A_-}\left(1+\|C_{0,\theta}\|_\infty/u_-\right)
 +\frac R{A_-}\left\{\frac{\pi}4 J+\frac{p_a J}{A_-}\right\}\right]
 \ \ge\|\Pi\mathcal H_0\|_\infty .                               \tag{11}
\]
标量 $\Pi$ 用 $\pi$ 周期；外层向量用 $2\pi$ 周期。若
$u_--\Delta>0$，真实 $Y_r\cdot n$ 在**某一整圈内侧邻域**上严格为正；
依据是 $Y_r,n$ 的一致连续端延伸。因
$\det(Y_r,Y_\theta)=b(Y_r\cdot n)$，这给真实平面正 Jacobian。
各闭曲线严格凸，固定外法角时支撑函数的 $r$ 导数正是 $Y_r\cdot n$，
所以此邻域的各截面也严格嵌套。弧长坐标处的 Jacobian 乘 $\chi$，
在边缘趋零，正是竖直接柱所需。

若实际输入确有 R618 的**准确连续**全硬迹 $C_0=P_0+\zeta_R$、
$C_1=P^*_1+\zeta'_R$，原非线性式逐项给 $D_0=0$；同一准确核心转角根给
$\mathcal A_0=1$。于是(10)化为 $Y_r(R)=v_0 n_0$。对任何有严格
曲率余量 $\max_\theta k_0/R<1/\tau$ 的该实际边缘，(7)(8)的连续性
还给某一内侧邻域中的同一曲率门。上述结论没有给出数值宽度。
$D_0,F_0$ 均可非零时，(7)及实际曲率极限(8)仍成立；用(11)
或直接包围(10)来检验正图即可。

## 6. 实际有限全模的端部消费者

scripts/r653_actual_vertical_core_rim_20261128.py 消费同一真实候选的
$e_R,e'_R,C_0,C_1$，包含所有独立与从属余弦系数及两条真实均值迹。
写 $\hat C_k$ 为双侧 Laurent 系数，常数项不减半。由(9)，二次项的
系数只需在 $k+j=n$ 上求和
\[
 \sum_{k+j=n}(jk-2c_\alpha k^2)\hat C_k\hat C_j,\qquad c_\alpha=\alpha/(1+\alpha).
\]
另加 $-R\hat C_{1,n}-c_\alpha e_R n^2\hat C_n$ 和常数 $-R e'_R/2$。
先在同一模内相加再求全模绝对值和，以保留硬迹的抵消。这是有限全模卷积；
不会把在某个有限角网观测到的零赋予整个角圆。

若有同场已付连续 $\mathcal A_0,v_0^2$ 区间，可直接复用。否则已有正能量
区间 $0<a\le v_0^2\le b$ 时，取 $d=(a+b)/2$、
$\lambda=\sup|v_0^2/d-1|<1$。$(1+x)^{-1/2}$ 前 $K$ 阶各项的均值
由有限 Laurent 幂的零模准确给出；乘 $d^{-1/2}$ 后加上
$\lambda^{K+1}/[(1-\lambda)\sqrt d]$ 的绝对尾界。其证明是二项式系数
绝对值至多一。若只用速度区间也总有 $1/\sqrt b\le\mathcal A_0\le1/\sqrt a$。
该计算只支付必要的端部代数；没有新 ODE、隐根、FFT 或位置样本。

本文没有将分片 ODE/有限 seed 归一、连续转角与 canonical 数值根的差、
有限求积、舍入及其余原源误差消去。用数值 trace 时保留这些条件。
本条与 [R650](R650-true-tail-fixed-reference-second-derivative-and-actual-curvature.md)
分属实际场的外缘与内帽。主体及两个邻域之间的连续覆盖、规定的全闭面 reach、
同一固定度量的求解与宏观变化均须在同一候选上完成。
