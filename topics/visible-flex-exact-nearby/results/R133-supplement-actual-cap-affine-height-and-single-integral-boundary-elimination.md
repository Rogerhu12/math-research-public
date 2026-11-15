# R133：实际帽图的一次积分消元、完整仿射项与独立高度列

2026-11-15。状态：以下准确恒等与有条件算子界已证明；没有新增数值运行。本篇不授未知 core 的物理角准入、曲率 chart 的未付 Taylor 界或全局解。CP 的成功新回执来自 run 43741463694/1；首次失败且未保存科学结论的 run 43740644806/1 保留原失败历史。以下不从首次失败推断任何数学结论。

引用 [CP 加权内端差](R133-supplement-weighted-actual-cap-Poisson-difference-and-complete-inner-receiver.md)、[CPA 实际两域结论](R133-supplement-actual-weighted-cap-inner-difference-and-finite193-inverse.md)、[M 两输入实际帽](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)、[I 完整 Hilbert 响应](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md)、[R 固定旧 reference 与全 height 球](R133-supplement-actual-inner-cap-complete-tail-height-feedback-and-97-interface.md)、[NF 固定残差坐标](R133-supplement-divergence-nonlinear-core-source-and-complete-finite193-receivers.md)、[W 已知形状及未知 scalar 迹入口](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md)、[RB 两角和两 mean](R133-supplement-actual-right-cap-body-and-nonlinear-moving-L2-comparison.md)、[RA 已成加权完整值](R133-supplement-actual-radial-weighted-cap-and-complete-left-receivers.md)。

## AR1. 固定坐标、实际 product 域与一个旧线性算子

保持同一个帽内禀 metric、同一 physical $\theta$、同一反射轴和同一连续中心 $\widehat W$。实际输入为
$$
 \gamma\in A^0_{\theta,\mathrm e,\perp},\quad
 \|\gamma\|_{A^0}<r_\gamma,\qquad
 f\in\dot A^2_{\theta,\mathrm e,\perp},\quad
 \|f\|_{\dot A^2}<r_B=2^{-60}.
 \tag{AR.1}
$$
取 $r_\gamma=10^{-9}$，或其已明确的小球 $10^{-9}/128$。定义两个真实 inner 输出
$$
 \Gamma(\gamma,f)=\big(\Gamma_B(\gamma,f),\Gamma_C^0(\gamma,f)\big)
 \in L^2_{\theta,\mathrm o}\oplus_1\mathbb R .
$$
$\Gamma_C^0$ 是实际 physical $C$ mean，不能改成零。
固定原缓存的
$K_0=(K_{B,0},K_{0,0})$；它由旧 $f_B^{\rm old}$ 定义，不因当前 $f$ 或当前 $\gamma$ 改变。

以下允许任意已经合法证明的统一数 $\kappa$ 满足
$$
 \sup_{(\gamma,f)\ {\rm in}\ (AR.1)}
 \|D_\gamma\Gamma(\gamma,f)-K_0\|
 _{L^2_{\theta,\mathrm e,\perp}\to L^2_{\theta,\mathrm o}\oplus_1\mathbb R}
 \le\kappa .
 \tag{AR.2}
$$
R.13b 的旧 $1/5$ 已给一种这样的上界；CPA 的实际完整 Hilbert component 与严格分母门现已通过。对两个对应的真实物理输入球，可分别取 CPA.5、CPA.6 的有向上端作为 $\kappa$：full 球约 $0.001995250213304$，tail 球约 $0.001965078425370$。这里的近似小数只作定位，实际定义使用 CPA 的完整有向球；本篇不重新计算它们，也不将其解释为 unweighted whole-cap 差。

## AR2. 完整帽非线性的一次积分，不另付第二个 $\kappa$

对固定 $f$ 置
$$
 E_f(\gamma)=\Gamma(\gamma,f)-\Gamma(0,f)-K_0\gamma .
 \tag{AR.3}
$$
对同一凸球内的 $\gamma_0,\gamma_1$，原 M 的 $A^0\times\dot A^2$ 解析图保证线段上的普通 Banach 微分存在。方向 $\gamma_1-\gamma_0$ 属于 $A^0\subset L^2$；其真实微分与 I/CP 的 Hilbert 延拓相同。因此只沿这个已存在图积分，得
$$
 E_f(\gamma_1)-E_f(\gamma_0)
 =\int_0^1 [D_\gamma\Gamma(\gamma_0+t(\gamma_1-\gamma_0),f)-K_0]
                       (\gamma_1-\gamma_0)\,dt ,
$$
$$
 \boxed{\quad
 \|E_f(\gamma_1)-E_f(\gamma_0)\|_{L^2\oplus_1\mathbb R}
 \le\kappa\|\gamma_1-\gamma_0\|_2 .
 \quad}\tag{AR.4}
$$
不需要在一个 rough Hilbert 开球上另授 Banach inverse theorem，也不需要 $\Gamma$ 的二阶微分或 $\kappa$ 的再次 Cauchy 放大。这里只证明原真实 $A^0$ 图上的 $L^2$ 差分估计。

## AR3. 未知 cut 必须经过真实 physical chart

设 $\bar Q=Q_\delta(L)$，$Q=\bar Q+h$。使用 NF.17 的真实
$\Psi(Q)=(B_Q,C_Q)$，并始终固定
$$
 S_\delta b=v_\delta(b\circ\Theta_\delta),\qquad
 \gamma_Q=P_{\perp,\theta}(C_Q-\widehat C),\qquad
 \bar\gamma=\gamma_{\bar Q}.
 \tag{AR.5}
$$
假定这些真实实角 chart 已存在，且两个 physical 输入落在 (AR.1) 的同一球内。
角平移很小或 whole $C^0$ 球本身均不推出这个假定。

原 W 的实际 scalar 条件是一种具体入口：在它列明的定相位和已知基点门下，
$$
 |\delta|\le d=10^{-10},\qquad
 \|h_2\|_{H^1_\phi}<\frac{63}{320}d
 \quad\Longrightarrow\quad
 \|\gamma_Q\|_{A^0_\theta}<\frac{10^{-9}}{128}.
 \tag{AR.6}
$$
同时 $\|\bar\gamma\|_{A^0_\theta}\le13|\delta|/200$。
因而 AR.4 使用的 physical $\gamma$ 直线段确实留在同一个凸球。
(AR.6) 是未知 scalar $v$ 迹门，不是把 complete moving Euclidean pair 范数或任意低频 cutoff 自动认作已经满足的实际数据。

定义准确 chart 余项
$$
 R_\Psi(h)=(R_B(h),R_C(h))
 =\Psi(\bar Q+h)-\Psi(\bar Q)-D\Psi(\bar Q)h .
 \tag{AR.7}
$$
它含真实 inverse-angle composition。下文保留这个实际函数，不以小角位移免费估计 composition-minus-identity，也不声称未知 $C_\theta$ 或未知高频角导已经受控。

有一个不需要额外角导的独立 mean 恒等。设
$m_\delta=\langle v_\delta\rangle_\phi$、$\mu=\langle h_2\rangle_\phi$，则
$$
 \boxed{\quad
 \langle R_C(h)\rangle_\theta
 =\frac1{m_\delta+\mu}-\frac1{m_\delta}+\frac{\mu}{m_\delta^2}
 =\frac{\mu^2}{m_\delta^2(m_\delta+\mu)} .
 \quad}\tag{AR.8}
$$
它使用完整关系 $\langle C_Q\rangle_\theta=1/\langle v_Q\rangle_\phi$，并非误换测度。
在 W 的 $|m_\delta|>25/8$、$|\mu|\le2^{-10}$ 门下，
$$
 |\langle R_C(h)\rangle_\theta|\le|\mu|^2/27 .
 \tag{AR.9}
$$
$\mu=0$ 时使用非严格等号；independent even mean 没有被删除。

## AR4. 固定 $S_\delta$ 下的准确 97 行消元

定义
$$
 T_\delta(b,c)=\big(P_{\mathrm o,96}S_\delta b,\langle c\rangle_\theta\big),
 \qquad
 J_\delta(b,c_0)=\big(P_{\mathrm o,96}S_\delta b,c_0\big).
$$
以原 Euclidean 97 行范数读取这两个输出。令
$$
 A_{\rm chart}(h)
 =T_\delta R_\Psi(h)-J_\delta K_0P_{\perp,\theta}R_C(h).
 \tag{AR.10}
$$
原 $\mathcal B_\delta^0=\mathcal B_{Q_\delta}^{K_0}$ 全部坐标和 mean 保持。对固定 $f$，准确代回 NF.18 得
$$
 \begin{aligned}
 \mathcal R_{\partial,\delta}^{\,f}(\bar Q+h)
 ={}&\mathcal R_{\partial,\delta}^{\,f}(\bar Q)
       +\mathcal B_\delta^0h +A_{\rm chart}(h)\\
 &-J_\delta\{E_f(\gamma_Q)-E_f(\bar\gamma)\}.
 \end{aligned}\tag{AR.11}
$$
原因是
$\gamma_Q-\bar\gamma=P_\perp H_{C,\delta}h_2+P_\perp R_C(h)$；
$K_0P_\perp R_C$ 必须保留。$S_\delta$ 在整式中固定，故没有遗漏
$DS_Qh$ 乘非零基点残差。

与 NF.20 相比，
$$
 \boxed{\quad
 \mathcal N_{\partial,\delta}(h)+\Delta\mathcal B_\delta h
 =A_{\rm chart}(h)
       -J_\delta\{E_f(\gamma_Q)-E_f(\bar\gamma)\}.
 \quad}\tag{AR.12}
$$
这是把两个真实项合并的一次帽图作用，不是将其中一个项设为零。
因此真实 97 行匹配给
$$
 \mathcal B_\delta^0h_L
 =b_\delta^{\,f}-A_{\rm chart}(h)
      +J_\delta\{E_f(\gamma_Q)-E_f(\bar\gamma)\}
      -\mathcal B_\delta^0h_H,\qquad
 b_\delta^{\,f}=-\mathcal R_{\partial,\delta}^{\,f}(\bar Q).
 \tag{AR.13}
$$
全 $h_L+h_H$ 仍进入 actual chart 和帽差。只解 97 行不等于全 high odd trace 匹配。

已知 $|m_\delta|<6$、$j_\delta\le9/8$ 给
$\|S_\delta\|^2\le m_\delta^2\|j_\delta\|_\infty<81/2<49$。
故 $\|J_\delta\|\le7$。
结合 $\|K_0\|_{\rm inner-pair}<14$ 与 (AR.9)，得具体保守界
$$
 \|A_{\rm chart}(h)\|_{97}
 \le7\{\|R_B(h)\|_2+14\|P_\perp R_C(h)\|_2\}
                                      +|\mu|^2/27 .
 \tag{AR.14}
$$
若以 F 已成全输入系数 $c_{\rm cap}$ 支配
$\|J_\delta K P_\perp H_{C,\delta}\|\le c_{\rm cap}\|K\|$，
则整个合并项满足
$$
 \boxed{\begin{aligned}
 \|\mathcal N_{\partial,\delta}(h)+\Delta\mathcal B_\delta h\|_{97}
 \le{}&c_{\rm cap}\kappa\|h\|_{L^2_\phi\oplus_2L^2_\phi}\\
 &+7\{\|R_B(h)\|_2+(14+\kappa)\|P_\perp R_C(h)\|_2\}
                                      +|\mu|^2/27 .
 \end{aligned}}\tag{AR.15}
$$
为直接应用同一 $c_{\rm cap}$，对 (AR.4) 的 physical 直线段定义
$\mathcal K_{01}u=\int_0^1[D_\gamma\Gamma(\gamma_t,f)-K_0]u\,dt$。
先对 $u\in A^0$ 定义，再按统一界延拓到 $L^2$，得
$\|\mathcal K_{01}\|\le\kappa$。
于是先用
$\Delta\gamma=P_\perp H_{C,\delta}h_2+P_\perp R_C(h)$
再分别收费，便准确得到 (AR.15)，无需假设 chart 余项为线性。
第一行正是 CP/F 的一次完整 cap perturbation fee；不能再添加另一份同样的 $\kappa$。
第二行是尚须由真实 H1/primitive tame 或直接数据支付的非mean chart 余项。
本篇没有把该项改成 whole $C^0$ 小量。

## AR5. 两个实际非mean高度输入的完整差

I.16 的独立 normalized nonmean height 微分在整个 M product 域上满足
$$
 \|D_f\Gamma(\gamma,f)\dot f\|_{L^2_\theta\oplus_1\mathbb R}
 \le\frac1{25}\|\dot f\|_{\dot H^2_\theta}.
$$
沿两真实 $f_0,f_1\in\dot A^2$ 之间的凸线段积分，得
$$
 \boxed{\quad
 \|\Gamma(\gamma,f_1)-\Gamma(\gamma,f_0)\|_{\rm inner-pair}
 \le\frac1{25}\|f_1-f_0\|_{\dot H^2_\theta}.
 \quad}\tag{AR.16}
$$
这保留 Cmean 输出。它只处理 normalized nonmean height，且本节始终固定原 $s_B$。
若另改变 physical height $y_B=s_Bf_B$ 与 $s_B$，方向必须恢复为
$\dot f_B=(\dot y_B-f_B\dot s_B)/s_B$，不能把 $\dot y_B$ 免费当 $\dot f_B$。
单一整体 height gauge、$\lambda$、实际 height span 和 waist 荷不在此式中。

取任意固定 $f_{\rm ref}$ 于原球，令
$$
 H_f(Q)=\Gamma(\gamma_Q,f)-\Gamma(\gamma_Q,f_{\rm ref}).
$$
以 $b_\delta^{\,f_{\rm ref}}$ 为 affine 源时，(AR.13) 的右侧恰再加
$J_\delta H_f(Q)$，并把 $E_f$ 改为 $E_{f_{\rm ref}}$。
因为 $\dot A^2$ 控制 $\dot H^2$，两个原 $2^{-60}$ 球内高度给
$$
 \|J_\delta H_f(Q)\|_{97}
 \le\frac7{25}\|f-f_{\rm ref}\|_{\dot H^2}
 <\frac{14}{25}\,2^{-60}<2^{-60}.
 \tag{AR.17}
$$
这是完整 97 行的一个已付独立 source 上界，不需把实际 tail 选解 $f(\gamma)$ 宣称为 $C^1$，也不把 fixed-background proxy 的极小切向列冒成实际选解导数。
若后续消费 F 的真实 right-row Poisson 列，其 source 单位就是 (AR.17)；
尚未闭合的无限 high 与非线性 body 不会由此自动消失。

## AR6. 实际仿射项仍非零；一条可直接消费的原值预算

取 RW/RA 同一已成功 $\kappa_w=1/2$ 行的四个完整值记录
$$
 A_B=\text{inner B nonmean affine},\quad
 A_m=\text{inner Cmean affine},\qquad
 L_B=\text{inner B nonmean gamma gain},\quad
 L_m=\text{inner Cmean gamma gain}.
$$
它们来自完整 source、Q、true outer 与独立 Cmean 的已闭实际帽值，不是本篇 $\kappa$ derivative 的推论。原值预算在整个 $f$ 球上给
$$
 \|\Gamma_B(\bar\gamma,f)-\widehat B(L)\|_{A^0}
       +|\Gamma_C^0(\bar\gamma,f)-\langle\widehat C(L)\rangle|
 \le A_B+A_m+(L_B+L_m)\|\bar\gamma\|_{A^0}.
 \tag{AR.18}
$$
RB 的两个全域分量 supremum 之和给
$\|\bar W-\widehat W\|_{L^\infty_{\theta}\oplus_1L^\infty_\theta}
\le10|\delta|$；W 给 $\|\bar\gamma\|_{A^0}\le13|\delta|/200$。
因此
$$
 \boxed{\quad
 \|b_\delta^{\,f}\|_{97}
 \le7\left\{A_B+A_m+
          (L_B+L_m)\frac{13|\delta|}{200}+10|\delta|\right\}.
 \quad}\tag{AR.19}
$$
四个字段必须整行读取：
`posterior_bounds.inner_B_nonmean_affine`、
`inner_Cmean_affine`、
`inner_B_nonmean_gamma_gain`、
`inner_Cmean_gamma_gain`。
原 source identity 和完整均值与 CP 相同，不需要重算任何原积分。
这里不给新的实际小数，也不宣称 (AR.19) 已达到所需 low-cut 预算。

(AR.19) 已对当前 $f$ 使用完整原 height 球，故不能再为同一个 $f$ 重复加 (AR.17)。
另一种合法接线是先支付特定 $f_{\rm ref}$ 的真实 affine 源，再只加 (AR.17) 的实际高度差。
只有取得同一 actual source 的新 signed 证据，才可将这些 positive bounds 中的项作相消；不能因 $\gamma$ 小或 $\kappa$ 小就删除 $A_B,A_m$。

## AR7. 到 NF 的用途与仍然真实存在的门

本篇具体支付了 cap 差的全图 Lipschitz 消元、独立非mean高度的完整 97 source 费、独立 scalar chart mean 余项和可复用的 affine 值预算。
对 NF 的接线使用 (AR.13)--(AR.17)；同一 $h_L,h_H$ 与实际 ordinary/divergence body 源、原 96 waist source 全部不变。

仍须保持：
真实 $\gamma_Q$ 准入；非mean $R_B,P_\perp R_C$ 的实际估计；
same-state 的 low/shell/cut 数据；无限 high inverse 与真实 high odd matching；
全部 affine、mean、waist 及独立物理端口。现有 whole $C^0$ 球不代付这些门。
一个只求得 body 方程或只满足 97 行的态，仍不等于已经闭合的全域曲面。
