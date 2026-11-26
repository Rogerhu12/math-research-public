# R149 补篇：完整正侧逆接入真负侧与同输入 incoming 的原空间

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本文给出新实际正侧路线与 RNS/BT/FC 的准确连接。它消去的是整个正侧径向低头未知，不是只消掉一个角向有限矩阵。真正根部迹经过原 PW/SP 负侧传播后，产生完整腰部密度及两个物理均值；rough baseline 仍留在它原先已证明的观察域内。

本文没有新的数值执行。下文用到的低逆、58 量实际 physical 门、224 量端口表与 32 量 WPN 表必须全部实际完成；原 R142 的旧门真假及 R149 的独立 coercivity 身份保持原样。当前这些前置的缺失不能由本文设为成功。本文的新增内容是精确算子识别、可直接消费保存表的完整 receiver 公式，以及被该实际逆真正消掉的旧义务。

## PN1. 已有证明及同一算子的范围

最小相关读取如下；表中原结果只消费，不重算。

| 原件 | 本文使用的位置 |
|---|---|
| [R141 完整物理端口](R141-supplement-original-seven-ports-after-the-physical-gate.md)，P.6–P.16 | 真实 physical 条件、14 输入和 16 输出、原 high mixed-root 单位。 |
| [R141 精确 WOB/WPN 提升](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md)，L.1–L.16、L.24–L.25 | 完整 $DF(Q_\delta)$、一般 $L^2$ 提升、两 WPN 行和全部物理源符号。 |
| [WOB](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md)，WOB.2–WOB.4、WOB.24–WOB.33 | 真正 $\Phi,\Upsilon$、完整 physical Robin/mean 外图、原 square。 |
| [WHS](R133-supplement-rough-stable-inputs-and-complete-positive-head-feedback.md)，WHS.2–WHS.3、WHS.13、WHS.28–WHS.38 | 原粗 stable 观察、零 stable 正侧返回、物理 primitive 与 WGB 的原有顺序。 |
| [PW](R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md)，PW.7–PW.16 | 原混合根窗、负根区间、strict 区间、完整腰密度及两 mean。 |
| [PW 实际结果](R133-supplement-actual-seven-positive-ports-to-complete-waist-density.md)，run 43734233535/1 | 全部旧 receiver 的真实完成身份；$C_R,C_O,C_1,C_2$ 原球不变。 |
| [WY](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md)，WY.11–WY.14、WY.33–WY.35、WY.48–WY.49 | 原两有序波分支、完整 mean realization 与同输入角的左侧取消。 |
| [RNS](R133-supplement-actual-root-faithfulness-and-complete-incoming-parameter-Schur-reduction.md)，RNS.2–RNS.12 | 已付 root97 faithfulness、真正 rest 空间、完整 incoming 的原类型。 |
| [BT](R133-supplement-concrete-transported-head-factors-and-retained-operator-audit.md) 与 [BF](R133-supplement-retained-finite-factors-and-complete-bordered-incoming.md) | 原运输有限因子、无限算子与完整有限 Schur 的区别。 |

固定同一 selected member、同一 $Q_\delta$、真实 $r_*$ 和固定 intrinsic $\eta_0$。R141 的 hybrid 加已付完整 family differences 后才是 $DF(Q_\delta)$；共享 principal 不能重复添加。所有原有序 primitive、独立 moving mean、方向 mean rank、physical-angle/DN/height/Robin/mean 及真接缝都保持在原方程。

WOB 的 $\Phi,\Upsilon$ 已经以同一 $N_i$ 将原 Ai 输入改成 frozen common 输入 $x\in X^{\rm fr}_{-4/3}$。其上界中原 $N_i$ 已支付一次。下面消费该输入时不再另乘一次 $N_i$，也不因本正侧逆成立而宣称 whole rough baseline 有一个新的 raw bulk 或 mixed-root 范数。

## PN2. 正侧 square 被完整消去，物理 root96 仍为输入

沿 WOB/L 定义 $\mathscr A_c$。若实际 physical inverse 与 L.7–L.16 的完整响应均已成功，记得到的真实双侧逆为
$$
\mathscr G_c=\mathscr A_c^{-1}:
 L^2(I_+;E_L)\oplus E_L
 \longrightarrow L^2(I_+;E_L)\oplus\mathbb R^{97}\oplus\mathbb R^{96}.
\tag{PN.1}
$$
输出最后96坐标使用原 $\Theta b$ norm；第一坐标的认证范数使用同一 $S$。这只是原 Hilbert 坐标，不改变实际函数方程。

L.7–L.16 的双向代入证明 (PN.1) 作用于任意完整 $L^2$ 右端。其输入经原 $N=24480$ 投影拆成 finite 与完整 radial tail，只是同一 Hilbert 空间的正交拆分。因此 WHR/WHS 中为组织未知正侧径向头而引入的 $G,U_0,W_0,m_H$、radial auxiliary unknowns 及其未定正侧 cokernel，不再是这条新路线的未付前置。也无需先通过旧 WHVA4096、finite-$\rho$ 或旧 WJK trial 门。

准确消去的是求解变量 $(a,d,b)$。被规定的物理 root-even96 值 $c_*$ 保持独立输入，其全 source pair 是
$$
(F_c,e_c)=(C_*E_cc_*,-E_cc_*).
\tag{PN.2}
$$
L.24 的精确取消给该输入恰为 P224 的第9列。完整正侧齐次 regular 解图因此由原 high stable 输入和这个物理 $c_*$ 参数化；在同一原兼容 smooth core 上没有额外正侧 kernel/cokernel。

证明如下。先从 high stable 数据及独立给定源构造原 given-head 高图；由其完整 $\Phi,\Upsilon$ 和 affine 路径形成 WOB.31 的两行。应用 $\mathscr G_c$ 后恢复全部 low/high 方程及真实外条件。两解具有相同 stable 输入和 $c_*$ 时，其差的 source pair 为零，(PN.1) 的单射性使差为零。逆向取任一原完整正侧解，其真实 low head、root97 与 outer96 满足同一两行，故由唯一性得到同一个构造。这个论证同时证明正侧原 $\ell=0$，以及固定 high stable 后正侧自由物理列恰为96列。

这不删除负侧 waist matching、两个物理密度 mean、原 root/input 运输产生的 finite factors 或真正 $\nu$ 行。也不把一个独立给定的径向 source function 叫作有限维；它仍按原输入空间作为右端消费。

## PN3. 真正物理根迹与一般 lifting 的根迹不同

令
$$
c=E_c^*e,\qquad k=F+C_*E_cc,\qquad a=k+w .
\tag{PN.3}
$$
对任意一般 $L^2$ pair，只能使用原合法 $H^1$ 解的迹
$$
w(r_*)=-E_cc+E_dd.
\tag{PN.4}
$$
一般 $F,k,a$ 没有端点迹。特别地 $-E_cc$ 不是实际 prescribed $c_*$。

但对于 L.24 的完整物理来源，所有 ordinary Volterra 项在真实根为零；真正内部 jumps 以根右侧的同一 trace convention 计入，根处独立 mismatch 另作真实根/接缝资料。因此实际有
$$
F(r_*+)=E_cc_*,
\qquad
a(r_*+)=E_cc_*+E_dd.
\tag{PN.5}
$$
若存在根处 jump，则先按其原有符号决定送入负侧的左迹，或将其完整 mixed norm 放入原 PW 根区间 impulse 栏；不得把该 jump 同时放在两个位置或删去。若实际 source 尚未证明 (PN.5)，只能使用一般 WPN Hilbert 输出，不能运行本文的物理根 receiver。

原 low finite mixed 权重逐频不超过1，$E_c,E_d$ 正交；low 与 high 在原 Fourier 圈中也正交。所以令
$$
C\ge|c_*|,\quad D\ge|d|,\quad
Z\ge\|P_Hh(r_*)\|_{H^{-2/3}\oplus H^{-1}},
$$
即得到整个真根的混合范数
$$
B_{\rm root}\le\sqrt{C^2+D^2+Z^2}.
\tag{PN.6}
$$
这里的平方和是输出 Hilbert 子空间的正交性，与三项是否由同一输入驱动无关。两 mean 在负侧密度中仍由原完整变换传播；low 的一个 moving mean 不是那两个物理 mean 的替代品。

## PN4. 完整224表直接给14个真腰响应

令 $P_{\alpha j}$ 是完整保存并读回的224表。本文实际使用的两行如下。

| 原零基输出行 | code | 确切单位 |
|---:|---|---|
| 3 | low_root97 | 真 root odd96 与独立 moving mean，normalized raw Euclidean norm。 |
| 15 | high_root_mixed | 真 high 根的 $H^{-2/3}\oplus H^{-1}$ norm，已经包括本列 stable 输入及原 factor9。 |

不从 body 范数取迹，不再乘一次9，也不把 $\Theta$ 或 $S$ 施加于这两行。第 $j$ 列的实际 root-even 输入大小是 $\mathbf1_{\{j=9\}}$，故
$$
B_j=\sqrt{\mathbf1_{\{j=9\}}+
              P_{{\rm low\_root97},j}^2+
              P_{{\rm high\_root\_mixed},j}^2},
\qquad
D_j=C_RB_j .
\tag{PN.7}
$$
$D_j$ 给该完整 positive 输入、加齐次负侧方程后的真腰密度 norm。$C_R$ 直接读取原 SP/PW 已成记录，已经包括全负根 Cauchy、strict propagation、原真实 $n_g,T(q)$、primitive 与两个密度 mean。

对于任意同一物理 source 的14个分量，先按原 source identity 注入，再取 $\sum_j D_jd_j$。原 high ordinary 的 collar/body 是同一 source 在两个不交径向区间的限制时，才可以对该输入分割使用 Cauchy–Schwarz。不能因为有14列就宣布14个解输出正交。

原独立 low jumps 应用 L.24–L.25 的完整 step/endpoint pair 或另有真实响应证明；不将 Dirac 放进第7列 ordinary $L^2$。height/Robin/mean 既有高 affine 路径也有低97路径，它们已经在对应 P224 列里，不能只取其中一条。

## PN5. 两个32表 receiver 与物理 pair 的真实尺度

一般 WPN 输出的第3行仍是原独立 $d$，由 $w$ 的合法迹取得；第15行只包括
$$
h_{\rm ret}=\mathcal P_aa+\mathcal P_bb
\tag{PN.8}
$$
的真 high mixed root。该返回的 root stable 分量为零。它没有包括独立高 particular baseline $v_p$ 或 rough stable baseline。

记完整32表的两列为 $U_{\alpha,f},U_{\alpha,t}$。若一个完整物理 pair 已经给出
$$
F_f\ge\|(E_N^*SF,e)\|,
\qquad T\ge\|Q_NSF\|,
\tag{PN.9}
$$
则
$$
D=U_{{\rm low\_root97},f}F_f+
       U_{{\rm low\_root97},t}T,
\quad
Z_{\rm ret}=U_{{\rm high\_root\_mixed},f}F_f+
       U_{{\rm high\_root\_mixed},t}T .
\tag{PN.10}
$$
两行都使用实际保存的 whole upper。$F_f,T$ 来自同一 pair，所以此处使用三角，不对相应解输出赋予正交性。

现有纯模块 physical_WPN_source_pair 的第3个记录
actual_source_complete_WPN_pair_rhs_upper 同时支配 finite norm 及 joint finite-plus-tail norm；将其用于 $F_f$ 合法但可能较宽。第4记录是整个原 $Q_NSF$ tail。这里不从这两个上界反推出一个更小的 finite norm，也不将 tail 设置为零。

由 (PN.5)–(PN.6)，该 low 加 zero-stable return 的完整负侧贡献满足
$$
D_{\rm ret}\le C_R\sqrt{C^2+D^2+Z_{\rm ret}^2}.
\tag{PN.11}
$$
若还有一个**已具 mixed-root 资格**的独立高 baseline，界为 $Z_p$，则整个根的界为
$$
B_{\rm root}\le
 \sqrt{C^2+D^2+(Z_{\rm ret}+Z_p)^2}.
\tag{PN.12}
$$
两个 high 输出在同一子空间，必须先取三角再与 low 正交合并。原 negative-one 七端口的完整 root 行可以为其原普通 source/exterior/jump baseline 提供 $Z_p$；rough $H^{-3/2}$ stable 输入本身不能代入该栏。

## PN6. 给 frozen common high 的真正 strong addition

对一个原 common high 输入 $x$，准确 pair 是
$$
\mathcal L_xx=
\left(
 V_0\Phi x,\,
 -(V_{0,R}\Phi-B_R^H\Upsilon)x
\right),
\qquad c_*=0.
\tag{PN.13}
$$
它保留 outer mean 行；$B_R^H$ 只有 even 非均值96投影为零，mean 不能删去。给此 pair 的实际 source bounds 后，(PN.10)–(PN.11) 定义一个有界线性 correction
$$
\mathcal K_+:X^{\rm fr}_{-4/3}\longrightarrow
\mathcal Y_0=L^2_{\phi,0}(\mathbb C^2)\oplus\mathbb C^2,
\qquad
\|\mathcal K_+\|
 \le C_R\sqrt{D_x^2+Z_x^2}.
\tag{PN.14}
$$
这是完整 true negative homogeneous continuation 施加于新 low 和 zero-stable high 根迹的结果。先在原 smooth core 上由真实方程、trace 与唯一性识别，再由已付 whole $\Phi,\Upsilon$ 及 (PN.14) 延拓。它不需要给 rough baseline 一个新的 bulk norm。

该 extension 是同一真正耦合后的正侧解：在 smooth core 上，给定头为零的原 Ai baseline 加 (PN.8) 与 low head，满足完整 low/high 方程和 physical 外条件。新返回的 high stable 数据为零，故 RNS 的输入关系 $y=C_sx$ 原样保留。于是完整耦合图也有同一个 faithful high coordinate；FC 的 repair columns 仍因原 root97 定理恰为空。旧的任意径向头现在由 $\mathscr G_c\mathcal L_x$ 确定，不能再作为未解的正侧 rest unknown 重复保留。

不应把 (PN.14) 宣称为有限秩。$x$ 是无限维输入，源的径向积分也不是有限秩的理由。它已经具有所需 $H^{-4/3}\to\mathcal Y_0$ strong 类型，下一步应在完整 incoming 中按真正算子把它加一次。

## PN7. 同 common 输入的有序 incoming/outgoing 与均值

对已经包含原 $N_i=\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}$ 的 common 输入，WY.34 给两个准确左 receiver
$$
\begin{aligned}
\mathcal R_i&=
 U_{\mathcal H^{-1}}\mathscr J_+\widehat T_0^{-1},\\
\mathcal R_o&=
 U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}
       \mathscr J_-\widehat T_0^{-1}.
\end{aligned}
\tag{PN.15}
$$
因此新增项是 $\mathcal R_i\mathcal K_+$、
$\mathcal R_o\mathcal K_+$。同一 $x$ 的右 normalization 已在 (PN.13) 中，不再乘 $K_{\Lambda_\sigma}$ 或 $N_i$；原 common outgoing principal 的 Maslov/sign 顺序保持不变，没有把 $Z^{\mathcal S}$ 跨过 circle map。

设 $B_{H,0}$ 和 $K_{W,0}\ge1$ 是同 selected 真腰、同 fixed normalizer 的已付 bound。旋转等距，$\mathscr J$ 是包含两个 mean 的等距编码，故
$$
\|(\mathcal R_i,\mathcal R_o)Y\|_{L^2\oplus L^2}
 \le B_{H,0}K_{W,0}\|Y\|_{\mathcal Y_0}.
\tag{PN.16}
$$
这里两个波分量使用同一个 matrix normalizer 后再取行；没有额外 $\sqrt2$，也不把两行在取 normalizer 前拆开。每个 branch 当然服从同一上界。两个 physical-density mean 的联合输出由 $\|Y\|$ 控制，仍应保留其真实匹配方程。

若使用 WPL 的实际物理 primitive row，则它自己的 receiver 是 WHS.31，费用为
$$
\|\Delta_\partial\|
 \le {B_{H,0}\over\sqrt2}\|\mathcal K_+\|.
\tag{PN.17}
$$
这是不同的真实 readout，不能混用 WY 的 branch bound。WGB 的 high row 仍按
$$
\Delta_{\rm WGB}
 =B_{\rm tgt}^{-1}\Delta_\partial W^{-1}A_{\rm src}
\tag{PN.18}
$$
排列，左右费分别作用于原 $L^2$、$H^{-4/3}$ 窗。独立物理 root96 列只有自己的左 receiver/target normalization，不另乘 high input 的 $W^{-1}A_{\rm src}$。

对14个原 physical ports，(PN.15)–(PN.17) 只改变左输出坐标；其输入仍逐列采用 P224 的原 source/boundary 空间。不能把这些列全部称为 common $H^{-4/3}$ strong 输入，也不对它们添加或取消 $N_i$。只有 (PN.13) 的真正 $\Phi/\Upsilon$ common $x$ pair 获得 (PN.14) 的 strong-addition 资格。

这些公式提供完整 raw waist 和规范化 incoming 的 bounds。它们没有恢复任何 signed finite matrix entry；也没有把输入方程、两 mean、true phase 或 $\nu$ Schur 宣布为可逆。

## PN8. 真负侧 ordinary/impulse 源的原 domain

采用 PW 的原根 bracket、$r_c=r_+-1/200$、ordinary $dr$ 以及整个 strict 区间。对整个实际根 trace，原已证明的完整源接收是
$$
D_W\le
 C_R(B_{\rm root}+J_-)+C_OF_-+
 C_1J_{\rm st}+C_kF_{{\rm st},k},
\qquad k=1\text{ 或 }2.
\tag{PN.19}
$$
$J_-$ 为完整 mixed-root impulse norm 的和；$J_{\rm st}$ 为 strict $H^{-1}\oplus H^{-1}$ impulse norm 的和。$F_{{\rm st},1}$ 和 $F_{{\rm st},2}$ 是同一个完整 source 的 $L^1_r$ 或 $L^2_r$ 两种选择，只取一种。

原 PW 文本中 $F_-$ 的声明域是第一分量 $L^2_rH^{-2/3}_\phi$、第二分量为角向常数的独立 $L^2_r$ 源；该文字本身不能被悄悄改名。另一方面，[原 large-root Cauchy 的 E.6–E.12](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md) 及其 [完整实际结果](R133-supplement-actual-full-real-large-root-Cauchy-energies.md) 已有完整双源域。[完整双源及 signed 列补篇](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md) 将其准确接入同一个 N cut readout 和 SP。其依据是同一真实能量 source 变换
$$
\|\Lambda^{-1}Mg\|_{L^2\oplus L^2}
 \le\|(g_1,g_2)\|_{H^{-2/3}\oplus H^{-1}},
\qquad M=\operatorname{diag}(\theta/w,\theta),
\tag{PN.19a}
$$
因为 $w\ge\Lambda^{-1/3}$、$0<\theta\le1$；增长预算、完整两 mean、ordinary radial integration 和 N/SP 线性 readout 均未改变。故同一个旧 $C_O$ 也接收
$$
F_-=\|f\|_{L^2_r(H^{-2/3}\oplus H^{-1})},
\tag{PN.19b}
$$
而已公布的 isotropic $H^{-2/3}$ pair 是其合法子域。这里只转授原已付完整 source 估计，不重新生产增长常数或积分。

因此原 raw ordinary $L^2_rL^2_\phi$ pair 可以直接进入这个已明确证明的扩展，两分量及 mean 均保留。若同一个 negative ordinary source 的 whole norm 是 $F_{\rm neg}$，在根窗与 strict 区间按真实 $dr$ 分割，得到
$$
D_{W,{\rm neg\ source}}
 \le \sqrt{C_O^2+C_2^2}\,F_{\rm neg}.
\tag{PN.19c}
$$
该平方和只使用不交径向输入的正交性与输出三角。R147 的 same-selected proposal 源因此有一个可实际消费的完整 negative-source-to-waist 位置；式 (PN.19c) 本身尚未在本文运行新的 scalar 组合，也不单独给真正 $\nu$ 逆或其 $0.005$ 门。

纯入口区分原常数第二源、原 isotropic 双源和上述 anisotropic 双源三个标签。后两者须明确绑定同 E/N/SP 的完整转授；未提供该资格时拒绝接收，不能丢弃第二非均值源。

对于真正 $\nu$ 或 Newton 源，正区 compact bump 的局部零事实不删除负区、germ、height、mean、接口或 phase 行。R147 的 selected ordinary proposal 源仍是一个需要与真逆配对的已知 residual；正侧传播、根迹以及完整 incoming inverse 均需按实际对象保留。一般 unsolved $Q_\delta$ 也不能删除其 mean residual 变分项。

## PN9. 完整 incoming 里真正留下什么

在同一个实际 square realization 中，原 bookkeeping 现在可精确改写为
$$
B_{\rm coupled}
 =T+E_{\rm old,paid}+E_{\rm other}
       +\mathcal R_i\mathcal K_+
       +L_{\rm actual}V_{\rm actual}.
\tag{PN.20}
$$
式中是算子相加，不是从旧 norm 上界中相减。若旧 paid subtotal 已按一个不同的 entire operator 定义，必须先用其原 equality 指出各项属于哪里；不以文字重命名造成重复或遗漏。

| 对象 | 完整正侧新逆成功后的真实状态 |
|---|---|
| 未知 $a\in L^2_rE_L$、内部 $d,b$ 以及为其引入的 radial finite/tail auxiliary variables | 已由 (PN.1) 在整个原空间消去。旧 WHR restricted inverse 和 positive cokernel 参数不是本路线剩余条件。 |
| 真实 prescribed-root96 齐次列 | 由 P224 第9列的真正正侧解定义；经本篇原负侧 receiver 得到 actual finite-column norm。其 signed waist entries 仍须实际计算。 |
| frozen common high 对正侧低头的反馈 | 正是 (PN.13)–(PN.16) 的完整 strong addition；一般仍为无限秩。 |
| 原两个 physical means、真实 metric/phase matching、旧运输 finite/head 和 primitive/density ranks | 保留准确行列；若某项已 paid，仍只付一次。一个 mean 观察界不替代 mean 方程。 |
| 全部 opposite-sign、全局 Maslov/transported sign、真正独立的第二函数输入 | 保留其原无限空间或已证明的 strong 类型。root faithfulness 与 positive inverse 都不自动删去它们。 |
| 负侧 source、全部 true jumps、真正 $\nu$ 非齐次列 | 按 (PN.19) 与准确 signed reconstruction 消费；不设零。 |
| 完整 incoming 的 high inverse、实际 finite Schur、true $\nu$/phase Schur、非线性邻域与迭代 | 仍须原完整证明及实际严格门。本篇不将正侧可逆误称为全题完成。 |

特别地，未来 signed physical96 matrix 的直接认证可以使用新正侧逆作为误差 receiver，无需先选择一个巨大 principal 截断。应对每个真实 trial 列形成完整 low/high ordinary 源、stable/root/outer/height/mean/jump residual，再用 P224 或 WPN pair receiver；负侧 residual 用其真实合格源域和 (PN.19)。这给 complete waist-column error，随后才与实际 signed rows 配对。仅有 unsigned224/32表不能生成 signed matrix。若该 matrix 要作为 BF 的最终 Schur 使用，还必须包含真实 high elimination 的全部 cross terms；一个物理96主块不是完整 Schur。

## PN10. 纯公式实现及实际消费范围

新纯模块为
[scripts/fourfold_codazzi_positive_inverse_negative_receivers_math.py](../scripts/fourfold_codazzi_positive_inverse_negative_receivers_math.py)。

它实现：

- 全14个完整 P224 positive 输入的 true full-root 与 homogeneous-negative waist bounds；
- 完整实际 WPN source pair 经32表的 $d$、zero-stable mixed high root 与 (PN.11)；
- 只对已经具有原 mixed-root 资格的 independent high baseline 作 (PN.12)；
- 原明确 source domain 及同 E/N/SP 完整双源转授下的 (PN.19)，并拒绝未具资格的第二源；
- (PN.15)–(PN.18) 的 ordered 左输出 observations；每个 physical port 保留自己的输入域，common high strong 资格只属于真正 (PN.13) 的输入。

实现不 import 数值库、不读写文件、不生成假 actual、manifest 或 workflow，不执行任何旧成功 target。它返回有向算术结果，未来 public owner 必须先核 whole actual 低逆/58/224/32/source 文件和同 $DF$、root、physical rows、SP/PW、WTA/WX 的身份，再按一个明确新目标保存整球、读回、核方向。缺任何实际前置时，没有新数值结论。

本篇完成新的原空间算子接线。它留下的数值工作是实际消费已完成的新输入，以及真正 signed finite/negative/incoming 的验证；不再把已由新正侧完整 inverse 消去的径向头记作未解问题。
