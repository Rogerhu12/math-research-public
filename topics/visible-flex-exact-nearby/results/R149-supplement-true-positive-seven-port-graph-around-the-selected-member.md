# SPN：真实 selected 邻域中的强正图、已知高源及完整负窗

固定 $Q=Q_c+\delta_* Z$、$\nu=\nu_0+\delta_*$，其中 $Q_c$ 是原连续 M32 修补，而非另一个 exact-mean compact centre。设 $T=Q+p$，用真实物理 Fourier 频率 $k=4j$ 的两分量和
$$
 \sup_{[0,25/8]}\|p\|_{A^3}\le\rho\le10^{-7},\qquad
 \|p(25/8)\|_{A^3}\le9\,10^{-10}.
$$
外 height 背景保持原 $\sigma\ge1/16,\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$。无穷支集的 $p$ 允许任意符合上述界的真实角形状。对这个 $T$ 的真正线性化，整正区的 given-head 强、弱 high 图均存在，实际 strong $L^2_rH^{1/3}\to L^2_{r,\phi}$、weak $L^2_rH^{-2/3}\to L^2_rH^{-1}$ 的七端口可采用 [QN.39–43](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md) 原行。这里证明围绕另一个物理中心的邻域，不能直接把 $Q-Q_*$ 当成小的 $A^3$ 误差。

令 $e=q_\nu(T)-Z$，$b=\|P_Le(r_*^+)\|_{H^{1/3}\oplus L^2}$。$s$ 是实际 high 根 stable 迹在 $T$ 原真 frame 的范数。在完整强图中，先分出给定 $P_Hs(T)$ 和 proposal 的两项外残差 $r_B^Z(T),r_C^Z(T)$，其中 $s(T)=F_\nu(T)+A(T)Z-Z_r$。令 $u_0,v_0$ 分别界剩余全部物理输入产生的根 outgoing、collar frame sup，包含 head-to-high、外端 low、height、原每一种跳和根 stable。设 $X_0=(b^2+9.00002^2(s^2+u_0^2))^{1/2}$。$J_r,J_s,J_p$ 分别是 NRO.6 的根段 mixed、严格段 ordinary、正窄段 low 实际跳，包括任何根匹配差一次。由下述各个真项得
$$
 \boxed{\|q_\nu(T)-Z\|_{L^2([0,r_+];L^2)}
 \le25.95X_0+2.86\,10^{-6}v_0+1.774\,10^{-5}
     +5530\rho+25.944J_r+3.973J_s+9.54\,10^{-7}J_p.}          \tag{SPN.1}
$$
例如连续时 $X_0\le.000169,v_0\le1$ 即达到 $.005$。这仍要求同一真实全 PDE 产生上述端口以及许可的 $p$。下述数字构造了显式中心外的真正 high inverse 和真高体源界，未取得整个有限/无限物理匹配的实际根界。

## 重新比较真正 principal

在正区 $I=[r_*,R]$，两者 intrinsic 完全相同。用 $T$ 自身 $a_T=-\gamma\Pi T_2$ 构造 $p_N^T,g_N^T$，其 terminal $p_N^T(R)=q_*/(-\Pi T_2(R))$，初始 $g_N^T(r_*)=N^{-1/3}$。旧 selected $|\Pi Q_2|>1.068-3.861\,10^{-18}-19\,10^{-10}$；故两光速及其倒数的相对变化均小于 $\rho$（$\rho=0$ 时等号）。端点相对变化以 $\min(\rho,9\,10^{-10})/(5.8-9\,10^{-10})$ 控制，小于 $\rho$。由 [PH.4–7](R144-supplement-actual-positive-high-graph-for-compact-centres.md)，可取两帧相对参数 $\tau=10^{-7}$、damping 损失 $\sigma=2\,10^{-7}$。没有对未知主部角导作 ordinary source 估计。原 collar 速度包围仅变 $1.12\rho$，仍在 $(1/2,1.26)$，故保有原根斜率 $29<K_s<122$、$K/W<1$、mixed 根比较 9、真实 collar 原态重构 3；body 有 $K/W<181$。

QN 的全频核 $w(\ell)=(1+|\ell|/388)^{5/3}$ 对 $Q_c$ 及其角导仍可用同一 QN.13 四项（[PH.8](R144-supplement-actual-positive-high-graph-for-compact-centres.md) 的 degree32 各项上界）。把小系数部分取为 $T-Q_c=\delta_*Z+p$。对所有 $|k|\le384$，$w(k)<3.2$，而无限 $p$ 的 $A_w$ 与角导 $A_w$ 都由 $\rho$ 支配。因此
$$
 \|T-Q_c\|_{A_w}\le3.2\,19|\delta_*|+\rho<10^{-6},\quad
 \|\partial_\phi(T-Q_c)\|_{A_w}\le3.2\,83|\delta_*|+\rho<10^{-6}.
$$
这正是 QN.9–15 非局部核实际使用的两个条件。写 $\rho_0=10^{-6}$。PH.10 中的 $Q_c$ 部分在新帧的每个正主项至多增为原来的 $(1-\tau)^{-1}$，旧含非负 M96 费用，且 $E_s^o\ge2|\beta|$。所以新整核至多 $\lambda E_s^o$，$\lambda=(1-\tau)^{-1}+9000\rho_0$。collar 在上述原粗 reference 条件下对 degree32 有 $144,432.18$ 两窗界，另加 QN.15 的 $92\rho_0$，保有原两个 collar resolvent。

在真实外端 $Q_*(R)=Q_{\rm raw}(R)$。整修补与真实方向端点有
$$
 \|T(R)-Q_{\rm raw}(R)\|_{A^3}\le9\,10^{-10}
 +129^3(3.861\,10^{-18})+385^3|\delta_*|[\|Z_1(R)\|_{A^0}+\|Z_2(R)\|_{A^0}]<10^{-9}.
$$
因此 QN.18–40 的完整零宽物理角、DN、两种 mean、height 及 affine 行可直接用于该端点。将每个旧 body 内核乘 $\lambda/(1-2\sigma)$，再加真实外反射 $<.0025$，两实际反馈小于 $.310,.801$。其余 source、frame、jump 的增加因子在 PH.14–17 中随 $\tau,\sigma$ 单调；它们均小于 QN 所用值。按同一正 resolvent 公式 QN.43 即有它原两张表与所有强弱端口。使用更新的 genuine 根帧；若需要回到原 selected 帧，保留 QN.44 的完整三角坐标转换，不将两组有符号根分量逐点认成一样。

## 改变真实背景的已知强高源费小于 $9\rho$

因为 $F_\nu$ 在整个正区为零，变化为 $(A(T)-A(Q))Z$。写 $C(a,b;h)=-\beta[I(a_1b_1+Ka_2b_2)h_\phi+(a_1b_1+Ka_2b_2)h]$。令 $P=p/\rho$（$\rho=0$ 直接取零），变化的三线性部分除以 $\rho$ 后恰为
$$
 2C(Q,P;Z)+2C(P,Z;Q)+2C(Q,Z;P)+\rho C(P,P;Z)+2\rho C(P,Z;P).
$$
角常项 $\gamma\Pi P_2 JZ_\phi$ 支集至96；$\gamma\Pi Z_2 JP_\phi$ 的 high 输出费至多 $14\cdot19\cdot389^{-5/3}$。包括独立 mean 的一般低方程中两项仍都存在。

用 $\mathcal W=A^{1/3}$，三个 factor 均截到 $|j|\le32$ 时每个高三乘积为零。对每个 $C(a,b;h)$ 在真实高投影中逐槽作差；写 $a,b,h,h'$ 为整项 $\mathcal W$ 界、下标 $t$ 表示其 $|j|\ge33$ 尾，$b_K=|\beta|\max(1,|K|)$。则该项完整费用是
$$
 b_K[(a_tb+ab_t)(h+h'/4)+ab(h_t+h'_t/4)].
$$
无须将未知 $P$ 赋有限支集。由 [NBE.3](R149-supplement-nonlinear-background-negative-ordinary-response.md)，$Q,Z,P$ 的 $\mathcal W$ 状态/角导可依序取 $(33,28),(139,606),(1,1)$。$P$ 的两个尾分别由 $133^{-8/3}<3\,10^{-6}$、$133^{-5/3}<3\,10^{-4}$ 支配。整个 $I$ 上 $K=K_0$。[WP.3–4](R144-supplement-actual-whole-positive-raw-hybrid-fees.md) 拼接两个原区间。在 $[0,9/10]$，WLA run 43749764738/1 完整结论的 `complete_positive_product_conclusion.B_star,G_star` 分别给 $4.729885,13.861872$ 的严格上界，适用于整个选定参数窗。在 $[9/10,25/8]$，cap run 43674917925/1 的全部 1346 个闭行正性与覆盖门给 $K>0$，`complete_cap_intrinsic_constants` 中 $k_*=1$、$b_*,g_*<5.639201$。因此 $b_K<6,|\gamma|\max(1,|K|)<14$。reader 直接以两个原域上界的最大值支付下式的 $P$ 尾和均值秩项。由 [NHT.2](R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md) 的原非负整行 $T_{\rm old}$ 及 $A>1$，
$$
 b_K Z_t\le(7.28/3)T_{\rm old},\quad
 b_K Z'_t\le4(7.28)T_{\rm old},\qquad Q_t=|\delta_*|Z_t,\quad Q'_t=|\delta_*|Z'_t
$$
（最后两式指对应尾范数）。这不用除以可能为零的 $b_K$。五个词各用上述整行式，$P$ 尾乘 $6$，其它尾以原 $\|T_{\rm old}\|_{L^2}<1.456147\,10^{-10}$ 支付；常项乘 $\sqrt{|I|}<1.768$。直接有理比较给
$$
 \|P_H[s(T)-s(Q)]\|_{L^2(I;H^{1/3})}<9\rho.                  \tag{SPN.2}
$$
零修正时差准确为零。这与完整 $P_Hs(Q)$ 的 NHT 球相加，直接作为新 genuine strong 两段 ordinary 源；此处不要求 $e_\phi$ 有界。

## 真物理 exterior 及 low/high 正窄段

沿用 QN.19 的 $U_a,W_a,U_1,V_1$、$C_0=1/5.84$、原 composition norm $c=1.000001$。它们给实际 $T(R)$ 的 $A^2$ 乘子及正负 Sobolev chart。原完整 $Z(R)=(\xi,\zeta)$ 仍是已知 direction。设 $X,Y$ 分别为其 $A_{1/32}$ 整球乘 $3/2$，支配真实 moving $H^{1/6}$。令 $m_Z=\Pi\zeta$ 和 $I_*=[Y+|m_Z|(1+W_a/5.8)]/4$。对 NP.11 的真实同角微分，$\dot\phi\circ\theta=-I(\zeta-m_Z v/m)/v$。所以
$$
 D_C=c(C_0^2Y+V_1C_0^3 I_*),\qquad
 D_B=c[C_0X+U_aC_0^2Y+(U_1C_0^2+U_aV_1C_0^3)I_*]
$$
支配 $\dot C,\dot B$ 在真物理 $H^{1/6}$ 的范数。QN 的实际 DN 与 mean 行遂给 $\|r_B^Z(T)\|_{H^{1/6}}<1.23\,10^{-11},|r_C^Z(T)|<9.1\,10^{-16}$（含 $|m_Z|/5.84^2$）。故 $23\|r_B^Z\|+28|r_C^Z|<3\,10^{-10}$。独立 height 方向与真实 head 外列另进 QN.39。设
$$
 D=.2[1.254870\,10^{-9}+9\rho]+1.5(3\,10^{-10}).
$$
由 QN 强表 root outgoing 的三系数及 strong ordinary 两段的径向正交，这些已分项对同一根 outgoing 与 collar sup 各至多 $D$。后一个观察准确来自 QN.43 中 $S_c-U_a=(q_c-r_c)s=s$，本 particular 的 stable 坐标为零。于是全 mixed 根至多 $X_0+9.00002D$，collar sup 至多 $v_0+D$。这不把完整 stable 设为零。

在 $w=r_+-r_- =9\,10^{-13}$ 的正窄段，原 $\|A_{LL}\|<500,\|A_{LH}\|<11.6$。NBE 的 $A^0$ 差给 $m_1=.53(15)/4+7.3,m_0=3(.53)15+.53(14)/2+7.3$。低导数至多384，故真实 low-to-low $<501$。对 high-to-low 的新一阶项，角常 principal 无 cross；把 drift 角导移到低试验函数，漂移导数至多 $.53(15)\rho$，漂移本身至多 $.53(15)\rho/4$。加 $m_0\rho$ 即给整 cross $<12$，适用于无限高频。由真 low 初值问题，给定的 low ordinary 源在此段 $L^2$ 至多 $1.307204\,10^{-6}+28000\rho\sqrt w$（NBE.4 在整个窄窗 compact 已消失）。如 NRO.5 使用 $E=1.005>e^{501w}$，在 NBE.1 中加实际正窄段普通积分，得到完整根费用 $<25.95$，原 collar sup 费用 $<2.86\,10^{-6}$，该段真 low 跳费用 $<9.54\,10^{-7}$。代入上述 $D$ 并用 $t\le\rho$ 即为 (SPN.1)。其余数值皆为原真负 Cauchy 和真实改变后的主部估计。

[整件有理 reader](../scripts/fourfold_codazzi_selected_nearby_strong_graph_saved_bounds.py) 验上述新增比较。$X_0,v_0$ 中的物理 head 端值、height、waist 与 holonomy 必须按完整耦合算子继续；真非线性背景的存在与其上述半径仍须整体证明。
