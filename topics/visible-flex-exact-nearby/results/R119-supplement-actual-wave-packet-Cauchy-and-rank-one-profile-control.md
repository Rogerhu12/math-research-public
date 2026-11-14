# R119 续篇：实际波长小区间的全频 Cauchy 比较与真实 rank-one 控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在第61束的真实物理 height/total-flux
坐标中支付一个小区间的完整传播，不以裸角 pullback 的 norm 小差
代替它。输入可以在一个频带，输出始终含全部 Fourier 模和两个
mean。在这个实际非径向算子的局部控制型上，第56束的多项式
rank-one 下界保持，且包括第60束的真实固定标签背景响应。

结论是**同一个当前 $\Gamma$、一个真正内部小区间的控制型**。
它不将单模 rank-one 控制升级为整个非径向近共振簇的正定型，也不
删除小区间以外的背景响应或联立 $D_\Omega\Gamma^*$ 两列。

## 1. 真正支集、频率及同物理中心数据

本篇仅取第56束的深尾 $j\ge8193$。在该层取尚未使用区间
$I\subset[7/16,15/32]$，其原 profile
在真实邻域准确为
$$
 Q=7+Bf(x),\quad f(x)=30x^2(1-x)^2,\quad
 dt=a_r\,dx,\quad B=\Delta/a_r,\quad \Delta>80.
$$
$a_r$ 是实际坡长；本篇逆密度仍记 $a=\mu^{-1}$。
令
$$
 M\ge4,\qquad r_*={\sqrt B\over M}\le2^{-512},\qquad
 N=a_rM\sqrt B,\qquad N|I|\ge32 .                       \tag{W.1}
$$
这比第56束的支集宽度门稍强，并在本篇就地保留；未声称覆盖原所有
中频。取 $x_c$ 为 $I$ 中点，使用实际内部小区间
$$
 J_M=\{|x-x_c|\le8/N\}\Subset I,
 \qquad t_c=t(x_c),\qquad \rho=2^{-72}/N .              \tag{W.2}
$$
区间上已选旧形状与两个补偿 bump 均为0。物理角仍为原 $\theta$。
实际非径向背景满足第60束的真实完整角条带界；写
$$
 n=\sup_{J_M}w^{-1}(\|p\|_{\mathcal A_2^2}+\|k\|_{\mathcal A_2^2}),
 \qquad n<2^{-4096}.                                    \tag{W.3}
$$
最后的严格小量由实际标签球支付，见第6节，不是新增的未核输入。

使用第61束的同一 $a,c,d,\mu$，参考 $\mu_0=w/r$。对任意真实
Jacobi 两迹 $Y=(h,\pi)$ 置
$$
 u=\sqrt{\mu_0}h,\qquad v=\pi/\sqrt{\mu_0},
$$
$$
 \|Y\|_{\mathcal N_{M,k}}^2
 =\sum_{l=0}^k M^{-2l}\left(
 M\sqrt B\|\partial_\theta^l u\|_2^2
 +{\sqrt B\over M}\|\partial_\theta^{l+1}u\|_2^2
 +{1\over M\sqrt B}\|\partial_\theta^l v\|_2^2\right),
 \quad 0\le k\le3 .                                    \tag{W.4}
$$
这个 norm 包含任意低输出和两个 mean。尤其高度 mean 具有真实
$M\sqrt B$ 权，没有从波动能量中漏掉。

## 2. 完整真实能量，不对输出作频带投影

写 $L_c=\partial_\theta(c\partial_\theta)$。齐次两迹方程为
$$
 h_t=dh_\theta+a\pi,\qquad
 \pi_t=\partial_\theta(d\pi)+QL_ch .                    \tag{W.5}
$$
定义真正正能量
$$
 E_{M,0}(Y)=\langle cQ|h_\theta|^2+a|\pi|^2
                           +\mu_0BM^2|h|^2\rangle,
 \quad E_{M,k}=\sum_{l=0}^kM^{-2l}E_{M,0}(\partial_\theta^lY).
 \tag{W.6}
$$
实系数的完整分部积分给
$$
 \begin{split}
 {d\over dt}\langle cQ|h_\theta|^2+a|\pi|^2\rangle
 ={}&\langle[(cQ)_t+d_\theta cQ-d(cQ)_\theta]|h_\theta|^2\rangle\\
 &+\langle[a_t+d_\theta a-da_\theta]|\pi|^2\rangle .
 \end{split}                                               \tag{W.7}
$$
特别所有 $h_\theta\pi_\theta$ 和 $a_\theta\pi h_\theta$ 项
准确相消；这不是丢掉交叉项的不等式。
第61束 (J.7)–(J.8) 及同一 $a$ 的商法则给
$$
 {(cQ)_t+d_\theta cQ-d(cQ)_\theta\over cQ}
       =-Q{\mathcal Bc\over c}-1-d^2/E+Q_t/Q,
$$
$$
 {a_t+d_\theta a-da_\theta\over a}=1-d^2/E-Qf_k .        \tag{W.8}
$$
这里 $E=1+w^2$，不是能量。未出现 $Q_{tt}$ 或背景径向高导数。

真实小球和 quartic 给
$$
 {7B\over4}<Q<2B,\quad |Q_t|/Q<2/a_r,\quad
 |\mathcal Bc/c|<2,\quad |f_k|<2,
$$
$$
 \tfrac12<a\mu_0,c/\mu_0<2,\qquad
 \sum_{l=0}^4\bigl(\|\partial_\theta^l(a\mu_0-1)\|_\infty
 +\|\partial_\theta^l(c/\mu_0-1)\|_\infty
 +\|\partial_\theta^l d\|_\infty\bigr)<2^{24}n .          \tag{W.9}
$$
最后一行是第61束完整有理系数在角宽2到1的 Cauchy；至4阶的
阶乘总和为34，所取常数覆盖两分量及商法则。

质量项 $b_M|h|^2$，$b_M=\mu_0BM^2$，满足
$$
 {d\over dt}\langle b_M|h|^2\rangle
 =\langle(b_{M,t}-b_Md_\theta)|h|^2
                           +2b_Ma\operatorname{Re}(\overline h\pi)\rangle.
$$
其中 $b_{M,t}/b_M=-1-Q$，交叉项用
$2\sqrt{b_Ma}<3M\sqrt B$ 支付。

对 $1\le l\le3$，完整 differentiated 方程的余项为
$$
 F_l=\sum_{r=1}^l{l\choose r}
  [(\partial_\theta^r d)h_{l+1-r}
                   +(\partial_\theta^ra)\pi_{l-r}],
$$
$$
 G_l=\sum_{r=1}^l{l\choose r}\partial_\theta
  [(\partial_\theta^rd)\pi_{l-r}
                    +Q(\partial_\theta^rc)h_{l+1-r}].    \tag{W.10}
$$
没有截断这些乘积。将 (W.10) 代 (W.6)，先保留 $\partial_\theta F_l$，
再用 $M^{-l}$ 的相对权。最高出现 $h_{l+1},\pi_l$，都已在同一个
$E_{M,k}$ 内。每个系数由 (W.9) 控制；$
\sqrt{cQ}\,a/\sqrt a<4\sqrt B$ 和
$\sqrt a\,Qc/\sqrt{cQ}<4\sqrt B$ 支付两个波动方向。
所有二项系数总和小于16，三阶求和及 $2xy\le x^2+y^2$ 再付
$2^{10}$ 已足够；统一用 $2^{40}nM\sqrt B$ 向上放宽。

因此对 $k=0,1,2,3$ 同时有
$$
 |(E_{M,k})_t|
 \le\{3M\sqrt B+8B+|Q_t|/Q+2^{40}nM\sqrt B\}E_{M,k}.
 \tag{W.11}
$$
由 $N=\Delta/r_*>80\,2^{512}$、(W.3)，花括号小于
$4M\sqrt B$。整个 $J_M$ 的长度为 $16/(M\sqrt B)$。
同时
$$
 \tfrac12\|Y\|_{\mathcal N_{M,k}}^2
 <{E_{M,k}(Y)\over M\sqrt B}<4\|Y\|_{\mathcal N_{M,k}}^2.
$$
所以任意两个真实截面之间，正反 Cauchy 和同一径向参考均满足
$$
 \boxed{\quad
 \|C(t,s)\|_{\mathcal N_{M,k}\to\mathcal N_{M,k}}<2^{56},
 \quad s,t\in J_M,\quad0\le k\le3 .\quad}             \tag{W.12}
$$
这里 $e^{32}\sqrt8<2^{49}$，$2^{56}$ 保留余量。
它控制全部频率，而不只控制输入频带。

## 3. 输入频带、全部输出的实际比较

令 $Y,Y^0$ 分别为实际和同一当前径向参考的解，并在物理中心
$t_c$ 具有相同两迹。只假设中心输入支持
$M\le|m|\le2M$；原 $Y^0$ 在演化中保持此频带。
真实 $Y$ 不作这种假设。

差 $Z=Y-Y^0$ 满足实际齐次系统加完整源
$$
 F=dh^0_\theta+(a-a_0)\pi^0,\qquad
 G=\partial_\theta(d\pi^0)+Q\partial_\theta[(c-c_0)h^0_\theta].
 \tag{W.13}
$$
能量源 norm 同时含 $F,\partial_\theta F,G$，故没有遗漏第一行源。
用 (W.9)、$\|\partial_\theta^lY^0\|\le(2M)^l\|Y^0\|$
以及实际能量的两个权，逐项得到
$$
 \|(F,G)\|_{\mathcal N_{M,k}}
      <2^{40}nM\sqrt B\|Y^0\|_{\mathcal N_{M,k}},
 \qquad0\le k\le2 .                                    \tag{W.14}
$$
例如 $Q(c-c_0)h^0_{\theta\theta}$ 的通量源权除以
$h^0_\theta$ 的能量权正比 $M\sqrt B$；没有剩下一个未付的 $M^2$。
每个角乘积都以其完整系数界估计，不将 (W.13) 投回输入频带。

一次真实 Duhamel、(W.12) 及完整长度于是给
$$
 \boxed{\quad
 \|Y(t)-Y^0(t)\|_{\mathcal N_{M,k}}
       <2^{160}n\|Y(t_c)\|_{\mathcal N_{M,k}},
 \quad t\in J_M,\quad0\le k\le2 .\quad}               \tag{W.15}
$$
实际未取整费用为 $2^{56+40+56+4}<2^{160}$。
特别输出 mean 和所有高频尾均在 (W.15) 中，未由径向对角性外推。

## 4. 在同一个短支集上比较完整控制型

取任意第56束方向，支持在 $J_M$ 中、尺度 $\rho=2^{-72}/N$。
它满足 $\int|\psi|dt\le2a_r\rho^5$。
令
$\mathcal K_{\rm act},\mathcal K_0,\mathcal H_{\widehat z}$
是第61束 (J.13)–(J.14) 的实际完整二次型。
不能先用 $\|v_\theta\|^2+\|u_\theta\|^2$ 把交叉项统收：
本篇保留其真实各向异性权。

从 (W.4) 直接有
$$
 \|u_\theta\|\le(M/\sqrt B)^{1/2}\|Y\|_{\mathcal N_{M,0}},\quad
 \|v\|\le(M\sqrt B)^{1/2}\|Y\|_{\mathcal N_{M,0}},
$$
$$
 \|v_\theta\|\le M(M\sqrt B)^{1/2}\|Y\|_{\mathcal N_{M,1}}.
$$
因此 $u_\theta v_\theta$ 的费用是 $M^2$，而非 $M^3\sqrt B$。
利用 $M\ge\sqrt B$、(J.17) 的全部系数，得
$$
 |\mathcal K_{\rm act}(Y)-\mathcal K_0(Y)|
        <2^{20}nM^2\|Y\|_{\mathcal N_{M,1}}^2,
$$
$$
 |\mathcal K_0(Y)-\mathcal K_0(Y^0)|
 <4M^2(\|Y\|_{\mathcal N_{M,1}}+\|Y^0\|_{\mathcal N_{M,1}})
                         \|Y-Y^0\|_{\mathcal N_{M,1}} .
$$
频带中心数据满足
$\|Y(t_c)\|_{\mathcal N_{M,1}}\le\sqrt5\|Y(t_c)\|_{\mathcal N_{M,0}}$。
(W.12)、(W.15) 于是给安全的完整有源型比较
$$
 \left|\int\psi[\mathcal K_{\rm act}(Y)-\mathcal K_0(Y^0)]dt\right|
 <2^{232}n a_rM^2\rho^5\|Y(t_c)\|_{\mathcal N_{M,0}}^2
 =2^{160}n{M\rho^4\over\sqrt B}\|Y(t_c)\|_{\mathcal N_{M,0}}^2 .
 \tag{W.16}
$$
最后一步准确使用 $a_rM\sqrt B\rho=2^{-72}$。
这里已经比较真实传播后的全部输出，不只比较同截面的系数。

对第60束的 actual gauged 响应，仍按 (J.14) 分别估计
$Q\widehat c|h_\theta|^2$ 与 $\widehat a|\pi|^2$，不把前者的 $Q$
错误乘到后者。得到
$$
 |\mathcal H_{\widehat z}(Y)|
      <2^{16}\widehat n M\sqrt B\|Y\|_{\mathcal N_{M,0}}^2,
$$
$$
 \left|\int_{J_M}\mathcal H_{\widehat z}(Y)dt\right|
           <2^{136}\widehat n\|Y(t_c)\|_{\mathcal N_{M,0}}^2 .
 \tag{W.17}
$$
此处 $\widehat n$ 是**整个 $J_M$** 上的实际响应，不只在
$\operatorname{supp}\psi$ 上取值。

## 5. 实际局部算子上的多项式 rank-one 下界

现在中心输入是一个真正单模 rank-one 态：
$$
 h(t_c,\theta)=H\varphi_m(\theta),\qquad
 \pi(t_c,\theta)=P\varphi_m(\theta),\qquad
 H,P\in\mathbb R,\quad(H,P)\ne0,
 \quad\|\varphi_m\|_2=1,\quad |m|=M .                   \tag{W.18}
$$
同一实 $\varphi_m$ 可以是任意 cos/sin 相位。真实传播允许此后
所有模式出现。对同中心径向参考用第56束 (H.6)–(H.17) 构造方向。
其真实振荡见证在 $|x-x_c|\le2/N$，整个方向支集在 $J_M$ 内。
方向保持径向两 phase，且满足原全部 $C^4$ 和 $\rho$ 账。

在中心设 $y=u$、$z=u_t/(M\sqrt B)$，第56束能量为
$E_c=z^2+q_cy^2$，$3/2<q_c<3$。
因为 $v=u_t+(1+Q)u/2$，$\sqrt B/M\le2^{-512}$，准确有
$$
 \|Y(t_c)\|_{\mathcal N_{M,0}}^2
 =2M\sqrt B\,y^2+{v^2\over M\sqrt B}
 <4M\sqrt B\,E_c .                                    \tag{W.19}
$$
第56束原测度下的完整 pairing 因而给，选择 $\psi$ 的号后，
$$
 \int\psi\mathcal K_0(Y^0)dt
 >2^{-2039}M^2E_cN^{-4}
 >2^{-1753}{M\rho^4\over\sqrt B}
                         \|Y(t_c)\|_{\mathcal N_{M,0}}^2 .
 \tag{W.20}
$$
这是中心真实两迹的归一，不再重复乘整个 pocket 的 $K_j$。

定义完整实际小区间控制型
$$
 \mathscr G_\psi(Y_c)=\int_{J_M}
          [\psi\mathcal K_{\rm act}(Y)-\mathcal H_{\widehat z}(Y)]dt .
 \tag{W.21}
$$
它由第61束 (J.15) 准确给出本小区间的物理 symplectic variation，
不包含一个未经支付的端点图替代。下一节支付实际输入后，
(W.16)–(W.20) 证明
$$
 \boxed{\quad
 \mathscr G_\psi(Y_c)
 >2^{-1801}{M\rho^4\over\sqrt B}
                     \|Y_c\|_{\mathcal N_{M,0}}^2 .\quad}
 \tag{W.22}
$$
这已经是实际非零背景、实际固定内部标签响应的结论。
偏导仍固定当前 $\Gamma$；径向 phase-annihilator 并不令非径向
$D_\Omega\Gamma^*$ 两列为0。

## 6. 用实际全标签解支付小量，而非新假设

令 $X_*\le2^{-262144}$ 为当前真标签解，
$N_j^\#=(N_j^c)^\#$，$P_j=h_j^{-14}\delta_j^{-7/4}$。
完整前缀和全局规范因子已经给
$$
 \sum_iN_i^\#<2^{160017},\qquad
 n\le4N_j^\#X_*<2^{160019}X_*<2^{-4096},
$$
$$
 \widehat n<2^{832}N_j^\#X_*P_j\rho^5 .                \tag{W.23}
$$
这里 (W.23) 后一式正是第60束，未把裸 $\psi F_1$ 放回。

还需支付 $P_j$，不能由 $n$ 小直接删掉它。
对 $j\ge8193$，$h_j=8\delta_j^{1/256}$，所以
$$
 P_j=2^{-42}\delta_j^{-231/128}.
$$
在 $j=8193$，$\delta_j>2^{-8197}$，故 $P_{8193}<2^{14800}$。
$j=8194$ 时至多再乘 $2^{231/128}<4$。
之后 $N_j^cP_j$ 的准确深尾幂是
$$
 {31867\over256}-{231\over128}={31405\over256}>0,
$$
相邻层严格递减，邻项 $N_{j-1}^cP_j$ 有同一比率。
因此整个真实深尾统一满足
$$
               N_j^\#P_jX_*<2^{175000}X_* .             \tag{W.24}
$$
这使用了原 $\delta_{8192}^{-485/4}\delta_{4096}^{-3/2}$ 两个
全局因子已包含的总界，并未重新归一标签。

相对于向下放宽的径向下界
$L_c=2^{-1800}M\rho^4/\sqrt B$，(W.16) 的比例小于
$2^{1960}n<2^{161979}X_*<1/8$。
由 $a_rM^2\ge2^{1024}\Delta$，(W.17)、(W.23) 的比例小于
$$
 2^{136+832+1800}N_j^\#X_*P_j\,{\rho\sqrt B\over M}
 ={2^{2696}N_j^\#X_*P_j\over a_rM^2}
 <2^{1672}N_j^\#X_*P_j
 <2^{176672}X_*<1/8 .                                   \tag{W.25}
$$
原始径向下界 (W.20) 比 $L_c$ 更强，故两项误差相减后仍严格大于
$L_c/2$，证明 (W.22)。没有用抽象可任选小球代替已达到的真实输入。

## 7. 两 mean、完整源及明确还缺的簇步骤

(W.6)–(W.15) 对独立高度/通量 mean 都有效。齐次物理通量 mean
守恒；实际高度 mean 可以由非 mean 输入产生，始终留在质量项中。
本文 (W.18) 的单模输入不授权在任意后续 operator 空间删除 mean。

ordinary 和 weak 源从第61束准确的
$s=(-aF^t,g-\partial_\theta(F^\theta+dF^t))$
进入相同能量。若令 $\mathfrak s_{M,k}(t)$ 为 (W.4) 对该完整
两分量的 norm，则真实 Duhamel 给
$$
 \|Y(t)\|_{\mathcal N_{M,k}}
 <2^{56}\left(\|Y(s)\|_{\mathcal N_{M,k}}
                         +\int_{J_M}\mathfrak s_{M,k}\,dt\right).
$$
第一分量的角导和全部 weak angular divergence 按该 norm 明确收费。
若原源只有更弱正则，应在相应 dual-energy 空间配对；本篇不授予
未给定的角导，也不引入 $F^t_t$。
参数源仍使用第61束 (J.26)，bare/total 两端仍相差真实 $F^t_e$。

(W.22) 是输入为一个实 rank-one 角模时，**实际小区间**的可选方向
下界。它没有证明对任意多频向量存在同一正定方向；一个模式的
复两迹可能含两个独立实解，已经需要完整 Sym2。
完整 global variation 还含 $J_M$ 之外的
$-\mathcal H_{\widehat z}$ 积分、真实外状态质量及当前
$D_\Omega\Gamma^*$ 两列。不能由局部端口归一消去这些项。
下一步须隔离实际 near-resonant 簇或支付完整 Sym2 多项式方向，
再在全网络中消费，不能以径向指数 gap 乘绝对小差作 Neumann。

[新准确能量与预算程序](../scripts/fourfold_actual_wave_packet_profile_control_20261114.py)
及[实际执行记录](../notes/2026-11-14-R119-actual-wave-packet-profile-control-budget.json)
保存本次必要代数和全部明确有理费用。
