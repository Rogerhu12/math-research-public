# R133：既成正区组件界与高频 collar coercivity

2026-11-15。解析合同，供独立核对。新消费者只读取原4650个完整闭行，并在同一正 collar 上形成新的局部组件上界和条件型能量常数。旧 target、Fourier、trial、convolution、residual、repair、mean-flow、积分和 Green 一律不重算。

本篇使用 [E 真正两侧能量](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md)、[PE 正交投影主部](R133-supplement-projected-principal-collar-energy-and-sharper-three-band-trace.md)、[SB selected 分带](R133-supplement-selected-reference-band-splitting-with-complete-small-source.md) 以及 [V 全部连续修补](R133-supplement-exact-continuous-repair-of-final-centre.md)。它不改已成 MA/NR/WC/RW 数字，不预判下述新 gate 的实际结果。

## 1. 固定域和原保存字段

固定
$$
 I=[17/20,19/20],\quad c=9/10,\quad |\delta|\le10^{-10},
 \quad Q_\delta=Q_0+\delta Z_{\rm can}.
 \tag{LC.1}
$$
这里 $Q_0$ 是同一个 degree32 连续修补中心，$Z_{\rm can}$ 是完整 degree96 canonical 连续方向。此正 collar 避开 intrinsic $\nu$ bump，故 intrinsic 系数不因 $\delta$ 改变。

实际假设是同一个真实、连续、两侧 $H^1$ 状态 $Q$，
$$
 Q_r=\mathcal F(Q),\qquad
 \|Q-Q_\delta\|_{C^0_{\rm pair}(I\times\mathbb T)}\le\rho.
 \tag{LC.2}
$$
六个候选半径为 $10^{-4},2^{-20},2^{-24},2^{-28},2^{-32},2^{-36}$。
这是宽窗 ordinary 能量的域；独立窄窗 MA 的同态高阶域仍需另外满足。

原完整 producer
`scripts/fourfold_codazzi_current_positive_complete_coefficients.py`
SHA256 `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c`
的 `full_fields` / `coefficient_row`，特别第128--200行，明确给出：

| 原 `bounds` 字段 | 准确单位 |
|---|---|
| `U_A0`, `V_A0` | 完整 physical moving $u,v$ 的 $A^0_\phi$；$v$ 包含真实径向 $s$ 与 even mean |
| `U_phi_A0`, `V_phi_A0` | 同一真 moving 角的一阶完整导数范数 |
| `V_nonmean_A0` | 先保全部 Fourier 系数，再去真实零频率的 $v$ 范数 |
| `mean_v` | 完整实际 moving mean 的有向球 |
| `drift_A0`, `drift_phi_A0` | 由原完整 $S=u^2+Kv^2$ 卷积支付的 drift 与角导 |
| `full_S_mean` | 原完整卷积的真实零频率；不是 intrinsic $s$ |

原 `full_fields` 已经乘物理 $\alpha$，并给 $v_0=s+\alpha V_0$。
本次不再次乘 $\alpha$，不将原 amplitude 当正交 Fourier 坐标，也不删 mean。

原4650行 native 是6,223,338 B，SHA256
`ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`，
原四个 parts manifest SHA256
`32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3`。
先核整个 $[0.2384058742994,25/8]$ 的有理覆盖，再取与 (LC.1) 的真交段。
每个原闭球覆盖整个原行，故限制交段时仍直接使用该完整球；不重估原多项式。

旧 source 已在所需区间给出 `same_intrinsic_cap_v2` 或
`new_true_intrinsic_closed_box` 的原 provenance。后者是**已成原闭行**，
并不允许本次调用 target。每条原 `actual_scalar_germ` 必须包住完整原行。
所有 original row identities、mean/primitive/support flags 必须完整保留。

## 2. 完整 repair 与局部组件

V.6 的全区间 physical pair 界给
$$
 E_Q=3.861\,10^{-18},\qquad E_{Q,\phi}=1.970\,10^{-17},
 \qquad E_{Q,m}=5.842\,10^{-21}.
 \tag{LC.3}
$$
第一角导小于 V 的 inhomogeneous $A^1$，所以第二个数可直接使用。
这些是 original raw centre 到 $Q_0$ 的完整 degree32 offset；
不涉及 response 的径向 mean-completion 流。

在每个原闭行，记原组件上界为 $U,V,U_1,V_1,V_{\ne0}$，
真实 mean 球为 $\boldsymbol m$，完整平方 mean 球为 $\boldsymbol S$。
置
$$
 p_1=K_-^{-1/4},\quad p_2=K_+^{1/4},\quad p=\max(p_1,p_2),
 \quad k=\max(1,K_+),\quad R=U+V .
 \tag{LC.4}
$$
局部 $K_\pm$ 是同一行严格正的 intrinsic 球端点。
原 $P=\operatorname{diag}(K^{-1/4},K^{1/4})$ 没有改变。

以下 Euclidean 向量界均可逐行成立：
$$
 \begin{aligned}
 M_0&=\sqrt{(p_1U)^2+(p_2V)^2}+pE_Q,\\
 M_1&=\sqrt{(p_1U_1)^2+(p_2V_1)^2}+pE_{Q,\phi},\\
 N_0&=\sqrt{(p_1U)^2+(p_2V_{\ne0})^2}+pE_Q,\\
 M_{\rm av}&=p_2(\sup|\boldsymbol m|+E_{Q,m}).
 \end{aligned}\tag{LC.5}
$$
$Q_0$ 的真实 $u$ 为 odd，因此其 mean 为零；$M_{\rm av}$ 保留完整 even mean。
$N_0$ 来自原保存的 nonmean 字段，绝不以两个独立 norm 上界相减得到。
$M_1$ 同时是 SB 所需 $N_1$ 的合法上界。

同一行 selected reference 以及未知差使用
$$
 E_0=19p\,10^{-10},\quad E_1=83p\,10^{-10},\quad
 M_\delta=M_0+E_0,\quad M_{\delta,1}=M_1+E_1,\quad\eta=p\rho.
 \tag{LC.6}
$$
$19,83$ 是已经成功的完整 canonical 方向界，包含完整 mean 及连续 offset。
这里只形成新组合，不重新算方向范数。

## 3. 实际 mean、平方 mean 和 drift

设
$$
 \epsilon=E_Q+19\,10^{-10}+\rho,\qquad
 m_-=-\sup\boldsymbol m-E_{Q,m}-19\,10^{-10}-\rho.
 \tag{LC.7}
$$
只有 $m_->0$ 才得到实际 $m<0$ 和
$$
 a_-\ge G_-\sqrt{K_-}\,m_- .
 \tag{LC.8}
$$
mean 的三个补费各自保留；intrinsic $s$ 未替代 $\boldsymbol m$。

逐点平方差给完整 actual mean 球
$$
 \langle S(Q)\rangle\in
 [\inf\boldsymbol S-\Delta_S,\ \sup\boldsymbol S+\Delta_S],
 \qquad
 \Delta_S=k(2R\epsilon+\epsilon^2).
 \tag{LC.9}
$$
因 $K>0$ 且状态真实，左端可以再与0取最大。这里没有重新做卷积。

已成 D 的 `complete_original_collar_intrinsic_conclusion` 在准确同窗支付
$L_G\ge|G_r/G|$ 与 $L_K\ge|K_r/K|$。该完整小 execution 为
40,659 B，SHA256
`6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071`。
它的140个原 third-jet 行不重新恢复或计算。

E.7 给真解的局部 logarithmic-speed 上界
$$
 L=L_G+\tfrac12L_K+|\beta|_+
 \max\{|1-S_-|,|1-S_+|\}.
 \tag{LC.10}
$$
对近似态必须另外加 $\|\langle f_2\rangle/m\|_\infty$；
本次 (LC.2) 的数值表不能直接用于没有该 mean-residual 门的迭代态。

记原 `drift_A0` 上界为 $d_{\rm raw}$，$\epsilon_k=E_Q+19\,10^{-10}$。
完整已知 Wiener 修补和未知 $C^0$ 差分开支付：
$$
 \begin{aligned}
 d_0^+&=d_{\rm raw}+\frac{|\beta|_+k}{4}(2RE_Q+E_Q^2),\\
 d_\delta^+&=d_{\rm raw}+\frac{|\beta|_+k}{4}(2R\epsilon_k+\epsilon_k^2),\\
 D_{\rm ref,\delta}
 &=\frac{|\beta|_+k}{4}
       \{2(R+E_Q)19\,10^{-10}+(19\,10^{-10})^2\},\\
 D_{\rm nl}
 &=\frac{\pi|\beta|_+k}{8}\rho\{2(R+\epsilon_k)+\rho\},\\
 d_+&=d_\delta^++D_{\rm nl}.
 \end{aligned}\tag{LC.11}
$$
前两项与 known $\delta$ 项使用真正 $A^0$ primitive 的 $1/4$；
未知 $C^0$ 项使用完整 sawtooth $L^\infty$ 常数 $\pi/8$。不把后二者混换。

## 4. selected 两个低输入列和真实 high 列

设逐行
$$
 b_+=|\beta|_+\sqrt{K_+},\quad
 \alpha_+=|\beta|_++L_K/4,\quad
 g_+=G_+K_+^{1/4}.
$$
SB 给完整投影后的 known/reference 和 nonlinear 差：
$$
 \begin{aligned}
 A_{\rm ref,\delta}^{>J}
 &=b_+(6M_0E_0+3E_0^2)
   +\tfrac{b_+}{2}(M_1E_0+M_0E_1+E_0E_1),\\
 A_{\rm nl}
 &=b_+\eta(3M_\delta+\eta+M_{\delta,1}/4),\\
 A_{\rm mix}
 &=b_+(6M_{\rm av}N_0+3N_0^2)
   +\tfrac{b_+}{2}M_1(M_{\rm av}+N_0).
 \end{aligned}\tag{LC.12}
$$
这里 $J=96$ 或288；$g\langle u_2\rangle J_0W_{\delta,\phi}$ 的输出止于96，
所以在最终 $H_J$ 后准确为零。它没有从原 equation 或 mean 条件中删除。

完整 actual high-input 行还可直接由 E.13 得到
$$
 A_H=\alpha_+
   +b_+(3M_\delta^2+3M_\delta\eta+\eta^2)
   +\frac{b_+}{4}M_{\delta,1}(2M_\delta+\eta).
 \tag{LC.13}
$$
证明保持 $|W|\le M_\delta+\eta$、$|W_\delta|\le M_\delta$，
对 cubic 的三项及 primitive 逐一收费。high 输入的 mean 为零；
且前述有限 rank 输出在 $H_J$ 后为零，所以 (LC.13) 不需 $g_+M_{\delta,1}$。

定义每行的两条完整低输入系数
$$
 C_{S,J}=A_{\rm mix}+4Jd_0^+,\qquad
 C_{L,J}=A_{\rm ref,\delta}^{>J}+A_{\rm nl}
                     +4J(D_{\rm ref,\delta}+D_{\rm nl}).
 \tag{LC.14}
$$
所有量逐行形成完整上界后再取最大；$a_-$ 取完整下端最小。
这样没有拆开 operator 的不同部分任意取 entrywise minimum。

## 5. 直接保留真实频率的平方能量

令 $u=H_Ju$，$n_J=4(J+1)$，且 $u$ 在径向两端零。
PE.3 的准确恒等为
$$
 \|\mathcal L_Hu\|_2^2
 =\|u_r-H_J(du_\phi)\|_2^2+\|au_\phi\|_2^2
 -\int a_r\operatorname{Re}\langle u,J_0u_\phi\rangle\,dr .
 \tag{LC.15}
$$
在每个真实 $r$ 截面，完整高频 Poincare 界给
$\|u\|_{L^2_\phi}\le n_J^{-1}\|u_\phi\|_{L^2_\phi}$。因 $a$ 径向，
$$
 \left|\int a_r\operatorname{Re}\langle u,J_0u_\phi\rangle\right|
 \le\tau_J\|au_\phi\|_2^2,\qquad
 \tau_J=\frac{L}{a_-n_J}.
 \tag{LC.16}
$$
若 $\tau_J<1$，则
$$
 \begin{aligned}
 c_{p,J}^{\#}&=\frac1{a_-\sqrt{1-\tau_J}},&
 c_{r,J}^{\#}&=1+d_+c_{p,J}^{\#},\\
 \|u_\phi\|_2&\le c_{p,J}^{\#}\|\mathcal L_Hu\|_2,&
 \|u_r\|_2&\le c_{r,J}^{\#}\|\mathcal L_Hu\|_2 .
 \end{aligned}\tag{LC.17}
$$
此处 $L$ 已在准确 cross 中收费，不能再机械加一个 $L\|u\|_2$；
若 (LC.16) 未通过，原 PE.5 宽界仍可用，但不宣称 (LC.17)。

进一步设
$$
 \mathcal L_Hu=H_J\mathcal A_Hu+g,\qquad
 \|H_J\mathcal A_Hu\|_2\le A_H\|u\|_2.
$$
若
$$
 t_J=\frac{c_{p,J}^{\#}A_H}{n_J}<1 ,
 \tag{LC.18}
$$
则完整同态估计为
$$
 \|u_\phi\|_2\le\bar c_{p,J}\|g\|_2,\qquad
 \|u_r\|_2\le\bar c_{r,J}\|g\|_2,\qquad
 \bar c_{p,J}=\frac{c_{p,J}^{\#}}{1-t_J},\
 \bar c_{r,J}=\frac{c_{r,J}^{\#}}{1-t_J}.
 \tag{LC.19}
$$
这是对 already stated high equation 的直接能量吸收，不是全 BVP 逆存在性。

## 6. 同 cut 的完整源与条件迹

取原宽窗的 continuous triangular cutoff $\chi$，
$\chi(c)=1$、两端零、$|\chi'|\le20$。
对同一个 selected $z=P(Q-Q_\delta)$ 定义
$$
 z_L=\Pi_Jz,\quad z_S=(\Pi_J-\Pi_{J-64})z,\quad z_H=H_Jz.
$$
SB.11 中的 high 列由 (LC.13) 收入左侧，其余完整源可付
$$
 \|g\|_2\le
 F_J+C_{S,J}\|z_S\|_2+C_{L,J}\|z_L\|_2+20\|z_H\|_2,
 \quad F_J=\|H_JP(f-f_\delta)\|_2 .
 \tag{LC.20}
$$
所有范数是同窗普通 $L^2(dr\,d\phi)$，完整低输入仍含 mean。
径向 cutoff 与全部 primitive/mean/角投影交换；没有除以 $\chi$。
最后一项是实际 $\chi' z_H$ 源，不能因高频吸收而省略。

令 $\kappa_J=\sqrt{1+n_J^{-2}}$。
同一两端 FTC 的 half trace 给
$$
 \|H_J(Q-Q_\delta)(c)\|_{H^{1/2}_\phi}
 \le p_c\sqrt{\kappa_J\bar c_{p,J}\bar c_{r,J}}\,
 \bigl(F_J+C_{S,J}\|z_S\|_2+
             C_{L,J}\|z_L\|_2+20\|z_H\|_2\bigr).
 \tag{LC.21}
$$
可安全取 $p_c\le\sup_I\max(K^{-1/4},K^{1/4})$，只付一次。

真解时 $F_{96}$ 可以用原同窗 NR/WC 的已成完整界，$F_{288}=0$；
原 raw mean 的 MC 修正保持原样，只在正确高投影中准确消去。
消费者**不重新积分这些源**。近似态仍必须保留 $H_JPf$，
并在 (LC.10) 补实际 residual mean 的径向上界。

若同一状态另满足窄 MA 五例之一，则 LC.21 可进入原三带 half-trace 与
8193阶插值，仍使用 selected bound $2^{377903}$。本篇没有扩大窄高域，
不把某个低 $\rho$ 候选自动授给实际解。

## 7. 新消费的完整记录

新源只做：

1. 按原四个 parts 精确恢复旧4650容器，核全部 SHA、原身份和全覆盖；
   对 (LC.1) 取真交段，读取原完整字段。
2. 读取已成小 D execution 的同窗 ratio 界及 V 的完整修补常数；
   不恢复 D 的7721个旧行。
3. 逐行形成 LC.4--14，保持取得每个极值的原行、原球及有理交段。
4. 对六个声明 $\rho$，在 $J=96,288$ 两个真实频率门逐个记录
   $\tau_J,t_J$、成功或失败及完整条件输出。
5. 完整保留 all mean、修补费、真实参数域、旧 source 不重算标志。
   失败候选不给正的 (LC.19) 结论，结构完整的科学输出仍可 complete。

全量逐行审计只在 runner 临时目录；小 conclusion 保完整极值、十二个门与精确
输入/审计 SHA。它不包含真实未知 cut/body 值，不声明 core 存在、右帽 matching、
actual low-curvature selfmap 或某个 candidate 已适用于未证明的未知状态。
