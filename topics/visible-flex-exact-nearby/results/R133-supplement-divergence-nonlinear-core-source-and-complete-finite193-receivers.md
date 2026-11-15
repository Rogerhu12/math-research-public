# R133：同一 selected 中心的散度型非线性源与完整 finite193 接收式

2026-11-15。状态：下述代数恒等、范数估计及有条件接收式已证明；本篇不计算新数值，不把未知解差或实际帽逆的尚未通过条件改为已通过。

固定 [D 的同参数主体](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)、[R 的完整 selected 残差](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md)、[MC 的 raw mean 更正](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md) 与 [F 的实际 finite193 反馈](R133-supplement-actual-selected-parameter-finite193-feedback-and-cap-difference-threshold.md)。所有 moving 角均为原 $\phi$，积分归一化，径向测度为真实 $dr$。本文没有将物理曲率输入、moving even mean 或两个半区间的未知态相互替代。

## NF1. 固定对象与完整 Taylor 余项

在同一内禀参数 $\nu_\delta$ 上记
$$
 \bar Q=Q_\delta=(\bar u,\bar v),\qquad
 h=Q-\bar Q,\qquad
 D_K=\operatorname{diag}(1,K),\qquad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
 \tag{NF.1}
$$
这里 $\bar Q$ 是原连续 canonical 方向给出的完整 selected 中心，不是 mean-completed 的另一个 trial。原 moving 场为
$$
 \mathcal F(Q)=
 -\beta I(S_Q)Q_\phi
 +G\langle v\rangle J(K)Q_\phi
 +\beta(-u,v)-\beta S_QQ,\qquad
 S_Q=u^2+Kv^2.
 \tag{NF.2}
$$
$I=\partial_\phi^{-1}P_{\ne0}$ 保持原零均值规范；$G,\beta,K$ 都是径向标量。帽上的 $G$ 是原 $\gamma_{\rm rad}$，不是内端物理曲率参数 $\gamma$。

定义
$$
 B_h=\bar Q^tD_Kh,\quad
 S_h=h^tD_Kh,\quad C_h=2B_h+S_h,\quad m_h=\langle h_2\rangle .
 \tag{NF.3}
$$
若 $\mathcal A_\delta=D\mathcal F(\bar Q)$，则完整非线性余项
$$
 \mathcal N_\delta(h)
 =\mathcal F(\bar Q+h)-\mathcal F(\bar Q)-\mathcal A_\delta h
$$
准确等于
$$
 \boxed{\quad
 \mathcal N_\delta(h)=\partial_\phi\mathcal V_\delta(h)
 -\beta\{\langle C_h\rangle h+\langle S_h\rangle\bar Q\},
 \quad}
 \tag{NF.4}
$$
其中
$$
 \mathcal V_\delta(h)
 =-\beta\{I(C_h)h+I(S_h)\bar Q\}
       +Gm_hJ(K)h .
 \tag{NF.5}
$$
此式包括两个分量及全部 mean，不需 $h$ 有额外角导。其分布意义在下列乘积有定义时仍成立。

直接展开可核：transport 的二阶以上项是
$-\beta[I(C_h)h_\phi+I(S_h)\bar Q_\phi]$；reaction 是
$-\beta[C_hh+S_h\bar Q]$。在 (NF.5) 中应用
$\partial_\phi I=P_{\ne0}$，两者之间恰留下 (NF.4) 的两个 mean 项。holonomy 项的二阶余项是
$Gm_hJ(K)h_\phi$，正是 (NF.5) 最后一项的角导。原线性 $\beta(-u,v)$ 不产生 Taylor 余项。

特别地，
$$
 \langle\mathcal N_\delta(h)\rangle
 =-\beta\{\langle C_h\rangle\langle h\rangle+
                         \langle S_h\rangle\langle\bar Q\rangle\}.
 \tag{NF.6}
$$
不能因为 (NF.5) 是散度势就删除 (NF.6)，也不能把 independent moving even mean 改成零。

## NF2. 同一 Euclidean pair 范数的值估计

以下在每个固定 $r$ 使用 normalized-circle Euclidean pair $L^2$。取真实有效界
$$
 |\bar Q(r,\phi)|\le M(r),\quad |h(r,\phi)|\le\rho(r),\quad
 k(r)\ge\max(1,|K(r)|),\quad b(r)\ge|\beta(r)|,\quad g(r)\ge|G(r)|.
 \tag{NF.7}
$$
记 $H(r)=\|h(r)\|_2$。在周期 $\pi/2$ 上，
$$
 \|I f\|_\infty\le(\pi/8)\|f\|_\infty,\qquad
 \|I f\|_2\le\frac14\|f\|_2 .
 \tag{NF.8}
$$
第一式直接作用完整 $f$；不先以 $2\|f\|_\infty$ 估其去均值部分。

由 $|C_h|\le k(2M+\rho)|h|$、$|S_h|\le k\rho|h|$、$|m_h|\le H$，得到
$$
 \|\mathcal V_\delta(h)\|_2
 \le k\rho\left\{
 b\left[\frac{\pi}{8}(2M+\rho)+\frac M4\right]+g
 \right\}H,
 \tag{NF.9}
$$
$$
 \|\beta[\langle C_h\rangle h+\langle S_h\rangle\bar Q]\|_2
 \le bk\rho(3M+\rho)H .
 \tag{NF.10}
$$
(NF.9) 中 $I(C_h)h$ 使用 $L^\infty$ primitive；$I(S_h)\bar Q$ 使用 $L^2$ primitive；holonomy 使用 $|m_h|\le H$ 和 $\|h\|_\infty\le\rho$。两个 norm 的 $1/4$ 与 $\pi/8$ 没有混用。

令 $\Pi_J$ 为原 signed $4\mathbb Z$ 的完整 $|j|\le J$ 投影，包括 mean。则
$$
 \|\Pi_J\mathcal N_\delta(h)(r)\|_2
 \le\lambda_J(r)\|h(r)\|_2,
$$
$$
 \boxed{\quad
 \lambda_J=k\rho\left\{
 4J\left[b\left(\frac{\pi}{8}(2M+\rho)+\frac M4\right)+g\right]
       +b(3M+\rho)\right\}.
 \quad}\tag{NF.11}
$$
这是对完整 $\mathcal V_\delta(h)$ 先作 $\Pi_J\partial_\phi$，只收已知频率 $4J$。没有使用未知 $\|h_\phi\|_2$。对 $J=96$，该因子为384，mean 项仍按 (NF.10) 独立收费。

## NF3. 真差分估计；不把值常数改名为 Lipschitz 常数

设同一点背景上的两个差 $h,\tilde h$ 都满足 (NF.7)，$\Delta h=h-\tilde h$。逐项相减给
$$
 \|\mathcal V_\delta(h)-\mathcal V_\delta(\tilde h)\|_2
 \le k\rho\left\{
 b\left[\frac{\pi}{8}(2M+\rho)+M+\frac\rho2\right]+2g
 \right\}\|\Delta h\|_2,
 \tag{NF.12}
$$
$$
 \|\beta[\langle C_h\rangle h+\langle S_h\rangle\bar Q
      -\langle C_{\tilde h}\rangle\tilde h
      -\langle S_{\tilde h}\rangle\bar Q]\|_2
 \le bk\rho(6M+3\rho)\|\Delta h\|_2 .
 \tag{NF.13}
$$
例如 $I(C_h)h-I(C_{\tilde h})\tilde h$ 的两费分别为
$(\pi/8)k\rho(2M+\rho)$ 和 $k\rho(M+\rho)/2$；
$I(S_h-S_{\tilde h})\bar Q$ 再给 $k\rho M/2$。
holonomy 的两个差各给 $gk\rho\|\Delta h\|_2$。
mean reaction 的三项分别给
$bk\rho(2M+\rho)$、$bk\rho(2M+2\rho)$、$2bkM\rho$。
因此上述常数在同一 pair 范数内成立。

将 (NF.12) 乘 $4J$ 再加 (NF.13)，才是对应投影余项的差分常数。所有式都是同一固定背景、同一半径域中的估计；不宣称未知解已经进入此域。

## NF4. 原 finite193 方程真正消费的 ordinary 源

在全内体 $I_-=[0,9/10]$ 置 $\Pi=\Pi_{96}$，
$h_L=\Pi h$、$h_H=(I-\Pi)h$，保原 odd96/even97 正交坐标。
若
$$
 f_\delta=\bar Q_r-\mathcal F(\bar Q),\qquad
 f_Q=Q_r-\mathcal F(Q),
$$
则准确有
$$
 (\partial_r-\Pi\mathcal A_\delta\Pi)h_L
 =-\Pi f_\delta+\Pi f_Q+\Pi\mathcal N_\delta(h)
                         +\Pi\mathcal A_\delta h_H .
 \tag{NF.14}
$$
真解时 $f_Q=0$；对近似态不得删除它。真实值跳若存在，也按原独立 jump 数据保留，不能并入普通 $L^2dr$ 源。

若 (NF.7) 在整个 $I_-$ 有效，定义
$\lambda=\operatorname*{ess\,sup}_{I_-}\lambda_{96}$。于是
$$
 \|\Pi\mathcal N_\delta(h)\|_{L^2(I_-;L^2_\phi)}
 \le\lambda\,\|h\|_{L^2(I_-;L^2_\phi)} .
 \tag{NF.15}
$$
这没有把帽的正 $K$、帽上的 $C^0$ 或 collar 系数移到整个 mixed core。若只在 collar 已付 (NF.7)，(NF.15) 也只能在该 collar 使用；whole-body 接收式须另有同对象全内体系数。

$\bar Q$ 的 Fourier degree 为96，$\mathcal A_\delta$ 的角系数最高 degree192，故
$$
             \Pi_{96}\mathcal A_\delta H_{288}=0.
 \tag{NF.16}
$$
这是线性高输入的有限支撑恒等。$\mathcal N_\delta(h)$ 中两个未知高频相乘可产生低频，不服从 (NF.16)。旧 specialised $a_Y$ 只针对其原 raw high-body 通道；使用 F 的 selected 版本时，其另付 $\Delta\mathcal A$ 的97--288通道必须同时保留，不能拿旧97--160作用替代。

R/MC 已纠正的完整 $f_\delta$ 包括原中心残差、raw response mean、canonical 连续 offset 和选参积分。F.13 是额外 $\nu$ 列的 $\Delta F_\nu+\Delta\mathcal A Z$，不是完整 $f_\delta$，不得重复加入或拿它替掉 R/MC 的源。

## NF5. 固定中心残差坐标中的完整 97 边界行

以下固定同一外部数据 $f_B$、内禀量和反射定相位。若改变 $f_B$，其独立源列须另加。令实际物理帽图的两个输出为 $\Gamma_B(\gamma,f_B)$ 和 $\Gamma_C^0(\gamma,f_B)$，后者是独立 physical even mean。对于处在原帽定义域的 cut 状态 $Q$，沿用 Cdelta.5--12 的完整 $\Theta_Q,\Phi_Q,B_Q,C_Q$，并置
$$
 \gamma_Q=P_{\perp,\theta}(C_Q-\widehat C),\qquad
 S_\delta b=v_\delta(b\circ\Theta_\delta).
 \tag{NF.17}
$$
$S_\delta$ 在以下残差中固定，不随试探态 $Q$ 变化：
$$
 \mathcal R_{\partial,\delta}(Q)=
 \left(
 P_{\mathrm o,96}S_\delta[B_Q-\Gamma_B(\gamma_Q,f_B)],\
 \langle C_Q\rangle_\theta-\Gamma_C^0(\gamma_Q,f_B)
 \right).
 \tag{NF.18}
$$
这是 96 个低 odd 条件和原独立 scalar mean；高 odd matching 仍是另一个必要条件。全 physical matching 蕴含 (NF.18) 为零，只解这 97 行并不反推全函数 matching。

记 $\bar Q=Q_\delta(L)$，$K_*=
D_\gamma(\Gamma_B,\Gamma_C^0)(\gamma_{\bar Q},f_B)$，其中原帽图的微分和弱延拓域仍须满足。由 $D B_Qh=C_QV_Qh_1+H_{B,Q}h_2$、$D C_Qh=H_{C,Q}h_2$ 以及 $\langle C_Q\rangle_\theta=m_Q^{-1}$ 得
$$
 D\mathcal R_{\partial,\delta}(\bar Q)h
       =\mathcal B_\delta^*h
       :=\mathcal B_{Q_\delta}^{K_*}h .
 \tag{NF.19}
$$
特别地，第一项 $S_\delta C_\delta V_\delta h_1=h_1$，scalar mean 微分仍为 $-m_\delta^{-2}\langle h_2\rangle_\phi$。没有 $D S_Qh$ 乘非零基点残差的遗漏：此处选用的残差坐标就是固定 $S_\delta$。如果另改用随态变化的 $S_Q$，必须另付那一项。

令 $\mathcal B_\delta^0=\mathcal B_{Q_\delta}^{K_0}$ 使用 F 已成功的固定原 physical cap operator；$K_0$ 仍包括其 scalar mean 输出。定义完整非线性边界余项和 affine 数据
$$
 \begin{split}
 b_\delta&=-\mathcal R_{\partial,\delta}(\bar Q),\\
 \mathcal N_{\partial,\delta}(h)&=
 \mathcal R_{\partial,\delta}(\bar Q+h)
 -\mathcal R_{\partial,\delta}(\bar Q)-\mathcal B_\delta^*h,\\
 \Delta\mathcal B_\delta&=\mathcal B_\delta^*-\mathcal B_\delta^0 .
 \end{split}
$$
若真实 97 行匹配，则准确有
$$
 \mathcal B_\delta^0 h_L(L)
 =b_\delta-\mathcal N_{\partial,\delta}(h(L))
       -\Delta\mathcal B_\delta h(L)
       -\mathcal B_\delta^0h_H(L).
 \tag{NF.20}
$$
$\Delta\mathcal B_\delta$ 作用的是全 $h_L+h_H$，不能只收其中一块。F 的已成 $c_Y$ 列仅消费最后一项，不能再代替其余三项。当前 $\kappa=1/5$ 的充分逆门未过，不妨碍把已成功的 $\mathcal B_\delta^0$ BVP 作为 (NF.20) 的参考，但也不授实际帽 inverse。

## NF6. 原 96 waist 行及不重算 Green 的显式左 lifting

左端约束是原 odd trace。其正交坐标记为 $U=(I_{96},0)$；非均值实 sine/cosine 振幅按 $1/\sqrt2$ 转为 normalized-circle 正交坐标，真实 even mean 不作这项转换。这里没有 $\alpha$，也不再乘一个 radial $\rho$。这与原 source 的 $U(Rh_{\rm orth})=Uh_{\rm orth}$ 完全一致。原两 primary 是：

- [完整已知 response 边界源](../scripts/fourfold_codazzi_known_response_true_boundary_sources.py)，blob7ead1dbd63f575cea2b7ebe21cd42f7a89aaf537，15495B，SHA256 79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204；
- [原完整 weighted 两边界](../scripts/fourfold_codazzi_regular_cut_true_weighted_boundaries.py)，blob15d4f7cce469d1bece169b6efa0e08a6ddced0f5，11817B，SHA256 32bea27df55fa79eeb29355da3f05a37d0e2eb00bf2a1a8954e193fe9b5429d9。

若实际腰条件为 $UQ(0)=0$，则
$$
 Uh_L(0)=b_{0,\delta}:=-UQ_\delta(0).
 \tag{NF.21}
$$
$Uh_H=0$ 只是这个有限输出投影的恒等；高 odd 腰条件仍须在高块保留。不能据此把 $b_{0,\delta}$ 设为零，或假定旧近似态与 selected 态均已满足真实腰条件。

可用一个新的解析 lifting 直接由已成 F 的 ordinary 列控制此独立左端数据，无需重做任何 Green、frame 或 Poisson 产品。设 $E=U^t$，$L=9/10$，$\psi(r)=1-r/L$，并记
$$
 \mathcal D_\delta=\partial_r-\Pi_{96}\mathcal A_\delta\Pi_{96},
 \qquad W_{b_0}(r)=\psi(r)E b_0 .
$$
则 $UW_{b_0}(0)=b_0$，$W_{b_0}(L)=0$。
设 $M_1(r)\ge|\partial_\phi Q_\delta(r,\phi)|$，而 $M,b,g,k$ 如 NF.7；此处 $M_1$ 是已知中心导数界，绝非未知 $h_\phi$。D.4 的每项分别给
$$
 \begin{split}
 a_{96}(r)={}&384\{b(\pi/8)kM^2+gkM\}
              +b(1+3kM^2)\\
             &+\tfrac12bkMM_1+gkM_1,\\
 \|\Pi_{96}\mathcal A_\delta\Pi_{96}v\|_2
       &\le a_{96}(r)\|v\|_2 .
 \end{split}
 \tag{NF.22}
$$
这里保留完整 mean principal 和 rank-one mean。$k\ge\max(1,|K|)$，所以不要求 mixed core 的 $K$ 为正。于是
$$
 \|\mathcal D_\delta W_{b_0}\|_{L^2_rL^2_\phi}
 \le \ell_0\|b_0\|,\qquad
 \ell_0=L^{-1/2}+
     \left(\int_0^L\psi(r)^2a_{96}(r)^2\,dr\right)^{1/2}.
 \tag{NF.23}
$$
若只有全区间 $a_{96}\le a_*$，也可取 $\ell_0=L^{-1/2}+a_*\sqrt{L/3}$。这些都是完整真实 $dr$ 费用。

用 $\bar G_\delta$ 表示 F 已通过的 $\kappa=0$ selected ordinary inverse，即原 96 waist 行和固定原 physical cap 所形成的 $\mathcal B_\delta^0$ 右行均为齐次。
$$
 \mathcal W_{0,\delta}b_0
       :=W_{b_0}-\bar G_\delta\mathcal D_\delta W_{b_0}
$$
准确满足 $\mathcal D_\delta\mathcal W_{0,\delta}b_0=0$、$U\mathcal W_{0,\delta}b_0(0)=b_0$ 及 $\mathcal B_\delta^0\mathcal W_{0,\delta}b_0(L)=0$。对 F 的三输出 $Y=B,N,C$，记其 ordinary 列为 $\bar g_Y$，则
$$
 \begin{array}{c|c}
 Y&\|\mathcal W_{0,\delta}\|_{\ell^2_{96}\to Y}\le\bar w_Y\\ \hline
 B&\sqrt{L/3}+\bar g_B\ell_0\\
 N&\left(\int_0^{r_+}\psi(r)^2\,dr\right)^{1/2}+\bar g_N\ell_0\\
 C&\bar g_C\ell_0
 \end{array}
 \tag{NF.24}
$$
其中 $r_+=2383968743003/10^{13}$ 是原固定 negative 输出窗端点。此 lifting 的真实状态连续，没有新 value jump；所有已成 Green 内的原 frame interface 和 virtual waist jump 仍由该完整 inverse 承担，不能从原证明中删掉。没有计算新的 $\ell_0$ 或 $\bar w_Y$ 数值。

## NF7. 五个独立输入的完整 finite193 接收式

令 $\bar g_Y,\bar p_Y,\bar a_Y,\bar c_Y$ 为 F 的 $\kappa=0$ 实际四列，$\bar w_Y$ 为 (NF.24)。设
$$
 \begin{gathered}
 x_Y=\|h_L\|_Y,\qquad y_B=\|h_H\|_B,\quad y_C=\|h_H(L)\|_2,\\
 r_\delta=\|-\Pi f_\delta+\Pi f_Q\|_{L^2([0,L];L^2_\phi)},\qquad
 n_\delta(h)=\|\Pi\mathcal N_\delta(h)\|_{L^2([0,L];L^2_\phi)},\\
 q_\delta(h)=\|b_\delta-\mathcal N_{\partial,\delta}(h(L))
                     -\Delta\mathcal B_\delta h(L)\|_{\ell^2_{97}} .
 \end{gathered}
 \tag{NF.25}
$$
对同一状态的完整方程、waist 和 97 右行，在没有额外真实 value jump 的情形，(NF.14)、(NF.20) 和 (NF.21) 准确重建为
$$
 \boxed{\quad
 x_Y\le
 \bar g_Y[r_\delta+n_\delta(h)]
   +\bar p_Yq_\delta(h)
   +\bar a_Yy_B+\bar c_Yy_C
   +\bar w_Y\|b_{0,\delta}\|_{\ell^2_{96}},
 \qquad Y=B,N,C .
 \quad}
 \tag{NF.26}
$$
若有真实 value jump，另加完整原 jump-to-$Y$ 列；不并入 $r_\delta$ 的普通 $L^2dr$ 范数。$\bar a_Y$ 已含其 selected $\Delta\mathcal A$ 费，$\bar c_Y$ 已含固定 $K_0$ 的 selected 坐标费，不能再加一次旧 load。二者不被 generic $\bar g_Y$ 代替。

原 Fourier 投影正交，故可保留准确关系
$$
 \|h\|_B=(x_B^2+y_B^2)^{1/2},\qquad
 \|h(L)\|_2=(x_C^2+y_C^2)^{1/2}.
$$
若另已付同对象全体域、$\lambda$ 及 $\|\Delta\mathcal B_\delta\|\le\epsilon_*$，则
$$
 \begin{split}
 n_\delta(h)&\le\lambda(x_B^2+y_B^2)^{1/2},\\
 q_\delta(h)&\le\|b_\delta\|+
  \|\mathcal N_{\partial,\delta}(h(L))\|
   +\epsilon_*(x_C^2+y_C^2)^{1/2}.
 \end{split}
 \tag{NF.27}
$$
NF.12--13 给 ordinary 部分真正的差分费；边界非线性值/差分、真实 $\epsilon_*$ 和 same-state 高块仍须独立支付。只读 $\kappa=0$ 成功四列并不使 (NF.27) 自动成为收缩式。

NG 剩余低迹中的 $c_L$ 正是这里的 $x_C$，不是 whole-body 的迹上界替身。NF.26 给其合法输入类型；它没有证明 NG 数值门已过。完整高块 inverse、所有高 matching、真实 $\nu$ phase、whole-core $C^0$ 半径域、独立 $H^{8193}$ 域及最终单个闭曲面仍需完成。
