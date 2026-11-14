# R119 续篇：浅前缀的真实五盒、固定 stop 重建与全部非零模谱选择

2026-11-14，visible-exact / tail_connector。

**状态：已独立核对的解析结论。** 本篇把实际五个 compact
坐标扩展到第129至8192层的完整内部负窗，逐项重付该扩展的
全标签图、第四允许线、固定 connector、joint 相位和全源入口。
深层已有五盒保持不变。最外未完整的 $(129,2)$ 分量仍属于外接口，
不为它安装一个未经定义的内部反项。

这项扩展随后消除旧五盒谱选择的 $M\ge M_*$ 限制：同一个
公共实际 profile 和同一个外参数，对每个 $M\in4\mathbb N$
都给真正有限 retained 网络的带权径向 inverse。无限低尾仍取
它的真实允许线和 affine 源。窗口数包括全部有限浅前缀，不把
低频时仍然无限的 low 窗计成有限个。

新的逐窗权只比已选谱权缩小一个固定常数：
$$
 (\mathcal W_M^{\rm all})_i^2
       =2^{-80}J_i^{-3}M^{-17/16}D_{i,M},\qquad
 \underline v_j=2^{-432016}J^{-4165}\delta_j^{1073/32}.
 \tag{P.1}
$$
$D_{i,M}$ 仍是原三段实际 generator 下界，见 (P.15)；
特别没有把已经支付的 $\delta^{1073/32}$ 层权换回早期较有利的权。

本篇的径向 inverse 使用原外边界接线。实际非径向高/低消元的
内部差比较另保第9节的准确范围；一个开放内部压缩不被自动
等同于已经接入外边界的径向有限矩阵。真正物理 mean、外接口
反馈和原 source-to-label 两向识别继续保留。

## 1. 明确的新参数族

采用原
[双参数全标签重建](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
(U.1)--(U.13) 及
[深层受控全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
的同一数据：
$$
 \delta_j=(2/25)2^{-j},\quad \eta_j=\delta_j^{3/2}/(4\sqrt2),\quad
 J=j+5,\quad
 K_j=\begin{cases}64,&j\le8192,\\2^{128},&j>8192,\end{cases}
$$
$$
 c_j=\begin{cases}64,&j\le4096,\\16\sqrt2,&j>4096,\end{cases}
 \qquad
 \mu_j=\begin{cases}\epsilon\delta_j^6,&j\le4096,\\
 \epsilon\delta_{4096}^{3/2}\delta_j^{9/2},&j>4096.\end{cases}
 \tag{P.2}
$$
$h_j,\tau_j,\zeta_j$、两个真实规范接缝及原标签层 $b_m$ 不变。
两个旧 bump 的复半径仍为 $2^{-15},2^{-29}$，实半径分别
为其一半。深层允许原来已经支付的平移和完整形状球。

仅在 $129\le j\le8192$ 的完整内部下降坡新增
$$
 \log p_*=\log p_{\rm left}-\Delta S(x)
        +\gamma_1\psi_1(x)+\gamma_2\psi_2(x)+\Xi(x),
 \qquad
 \Xi\in C^4_0(J_x),\quad J_x=(7/16,15/32),
 \tag{P.3}
$$
其中浅层形状实半径为 $2^{-80}$，复半径为 $2^{-79}$。
浅层不新增坡平移。旧两个 bump 支集、所有平台长度、端值、
端 jets、根 germ 以及完整正片准确不变。

这个额外参数盒先用于重建同一个新几何对象；下面的五盒是它的
明确子族。不能只因为深层曾有一个更大的 $C^4$ 球，就把第53束的
深层结论直接赋予这些浅胞元。

## 2. 浅层完整局部图的所有输入保持原数值

在 $J_x$ 上，原 quintic 满足
$$
 7/4<S'<15/8-1/128,\qquad 7/8<S''<2,\qquad\Delta>80.
 \tag{P.4}
$$
因此复盒中的 $|p_*|$ 仍严格单调，并且
$$
 |(\log p_*)_x|<(15/8)\Delta,\qquad
 |(\log p_*)_{xx}|<6\Delta .
 \tag{P.5}
$$
这里第一式留有 $\Delta/128>5/8$ 的实际余量，新增项只有
$2^{-79}$。第二式有 $4\Delta$ 的余量。实 profile 的 $Q$
在该支集仍沿原方向严格单调，峰点及其邻域未动，所以整个负片
仍只有原来的一个峰。

各段的模长端值不变。故时间有序 Dyson/Gauss 证明的全部
$p,p^{-1}$ 面积上界保持原表，不需要复面积有正号。
每个浅胞两个新支集的总附加 log 变差至多
$2|J_x|2^{-79}=2^{-83}$。原旧 bump 与新支集相离，故逐点
$$
 |\log(p_*/p_{\rm unperturbed})|\le2^{-15}.
$$
原双 bump 材料积分乘 $\delta^2$ 后小于11；新增变差贡献小于
$$
 \delta^2\,2^{-83}(1+4\delta^{-2})<2^{-80}.
$$
因此完整的原门仍为
$$
 \int(1+|\lambda|)(1+|p_*|^{-2})\,dy<64\delta^{-2},
 \qquad \lambda=(\log p_*)_y-7/\sqrt{12}.
 \tag{P.6}
$$
不是采用深层放宽后的128来替代浅层64。

[原统一实际参数图](R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md)
§§3--4 的局部证明只消费：同一模长单调性、有序面积表、
(P.5) 的各段 $m_*$、(P.6) 和同一正平方根邻域。这些输入逐项
保持。所以浅层原完整低窗误差、内部双向流和全部非线性局部球
仍取原值：
$$
 \|B_{m,j}-B^\infty_{m,j}\|_\infty
                 \le32768M^8\sqrt{\delta_j},\qquad j\le8192.
 \tag{P.7}
$$
其使用范围仍是原 $\widehat M_j$，不延长低窗。窗外继续使用真实
矩阵；原复全频 scalar 能量使用的 $m_*$、完整 log 变差和八次
规范换算未变，故原真实高块 $<1/4$ 不变。

新 $\Xi$ 在完整坡内部零延拓为 $C^4$。它没有增加旧的径向
状态转换，也不增加 $Q_{ttt}$ 的接缝原子。
新增最高所需项满足
$$
 |\Delta Q_{ttt}|
 \le 2^{-79}(\sqrt{12}/\eta)^4
 =147456\,2^{-79}\delta^{-6}<2^{-61}\delta^{-6}.
 \tag{P.8}
$$
原 $2^{40}J\delta^{-6}$ 宽门因而保持。其余三阶以下门更强。
这里没有给任意 $C^4$ 形状假设统一的第五阶径向导数。

两种 $K$ 的理想特征基、两个实际接缝和全部43个浅低模门
因此都未改变；深层仍用原 $2^{272}M^8\sqrt\delta$ 及真正高块。
规范后的低误差依然是双 bump 篇 (U.9)，所以其完整强 Green
和 nonlinear 收缩原样重新得到
$$
 \|\mathcal G_\Pi\|<2^{16},\quad\|\mathcal H_\Pi\|<9,\quad
 \|X_\Pi(a)\|_{\mathcal X_\beta}<16\|a\|_\beta,\qquad
 \|a\|_\beta<1/64,\quad 2^{16}K_*<2^{-52}.
 \tag{P.9}
$$
所有 mean 小根、完整 high 修正和两迹匹配在此构造中保留。

浅层参数只有有限个，深层规范误差和 physical 二 jet 包络仍
趋零，故原乘积连续性和真实 $C^2$ 平盘接合也保持。全参数
Cauchy 的归一方向范数须增加
$2^{80}\|\dot\Xi_{\rm shallow}\|_{\ell^\infty(C^4)}$；
不能沿用深层 $2^{21}$ 半径来收费这个新变量。

## 3. 第四真线与同一个 fixed-stop

对 $M=4$，(P.7) 准确变为双 bump 篇 (U.14) 的
$$
 B^\infty_4=
 \begin{pmatrix}-1299&325/16\\1235/64&-309/1024\end{pmatrix},
 \quad\det B_j=1/64,\quad
 \|B_j-B^\infty_4\|_\infty\le e_j=2^{31}\sqrt{\delta_j}.
 \tag{P.10}
$$
深处的真实允许线及两个基接缝仍给 cut4096 的 $|s|<1/16$。
从4096到128的3968个真正 Möbius map 现在随新 $\Xi$ 更新，
但 (P.10) 的数值完全相同。其分母 $>1297$、
导数 $<2^{-26}$ 以及
$|T_j(s_4)-s_4|<e_j/1000$ 逐项仍成立。
于是重新得到
$$
 |s_{128}-s_4|<e_{129}/999+\tfrac18\,2^{-26\cdot3968},
 \qquad
 |d_4-d_4^{\rm ideal}|<2^{-38},\qquad14<d_4<15 .
 \tag{P.11}
$$
这是实际整条无限尾的允许线，不是把理想深线直接作为末端数据。

固定 stop 的原基点也满足同一 $2^{-38}$ 管，因此新的完整实族
相对于该同一基点满足
$$
 |d_{4,\Pi}-d_4^{\rm base}|<2^{-37}<2^{-35}.
 \tag{P.12}
$$
这里不再引用“只在8193以后改变”才有的 $2^{-193532}$ 屏蔽。

[固定 stop 全端口篇](R133-supplement-fixed-stop-connector-and-complete-regular-ports.md)
(F.5)--(F.23) 的后续证明仅要求 (P.12)、$14<d_4<15$、
同一个固定 connector 和所有切口 jets。它们现在已经重付。
故 $\ell^0,\rho,H_e,\omega_e$、有限主体和长段均保持同一个值；
完整反向 Riccati、正 bump 和长段给
$$
 \frac{|\lambda_4+4\omega|}{4\omega}<2^{-27}e^{-8L},
 \quad
 |\lambda_m+M\omega|<2^{41}M\omega e^{-2ML},
 \quad |q_m-q_*|<2^{-512}.
 \tag{P.13}
$$
仍须为新 profile 选择外好参数；其条件 good-$t$ 测度
至少 $1-83/16384$。不能直接沿用旧的一个 $t$，也不对其选择
函数求导。相反，在所有参数和 $t$ 的产品盒里选择一次，之后
固定 $t$，正是下面的做法。

原 raw404 论证使用的全频矩阵上包络、真低锥、规范和浅/深
接缝都由 (P.5)--(P.9) 保持。因此同样的有序逐模账给
$1/9<\mathfrak w_m<e^{391M}$、$\tau_{128}+391<404$。
结合 (P.12)--(P.13)，
[fixed-stop 的完整 D0/source/incoming](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.5)--(D.38) 在新对象上逐项重新满足输入：
真实 $\mathcal H,\mathcal G$、raw404、全部有限段几何、完整两迹、
真实第四行 $t_4>0$ 和其余新好角。故1850宽差、
同宽完整边界投影和原 ordinary/weak 源收费均保持，
并仍有真正 incoming 的
$\|a^{\rm inc}\|_{224}<2^{-60000000}10^{-8}$。
这保证本篇以后使用的 $\mathcal X\le2^{-8388608}$ 是真实可达范围，
但不把原未消去的 $\mathcal F$ 余项置零。

## 4. 五个实际坐标在每个完整浅窗的安装

对新浅层取明确未用区间
$$
 I=[29/64-1/2048,\ 29/64+1/2048],\qquad \ell=1/1024,
$$
并以 $c-\ell/4,c,c+\ell/4$ 放置低、高、紧三组支集。
它们均严格在 $J_x$ 内，邻域与原两个 bump 不交。
深层继续采用原已经选择的 $I$。

两个实际 log 跳幅满足 $80<\Delta<3J$；
上界可用 $\Delta<2|\log\delta|+\log(2K_j)$ 直接核对。
又 $\sqrt{\delta_{129}}=2^{-64}/5$，故对所有 $j\ge129$
$$
 a_r=\eta/\sqrt{12}=\delta^{3/2}/(8\sqrt6),\quad
 B=\Delta/a_r>2^{190},\quad e=B^{-1}<2^{-190}.
$$
因此原有限 $e$ 五函数 Wronskian、低区两个真 null 因子和高区
完整两态估计的实际代数假设全部成立。那些证明在局部使用的
$j$ 只通过这些不等式、$\ell>2^{-31}J^{-2}$ 和各显式半径进入；
不把其原全局深层入口直接转授。

为明确有限 $e$ 入口，以下均只使用
$0<e<2^{-190}$、$0<\tau=1/\Delta<1/80$，不要求
$e$ 小于任何支集半径。在
[实际五函数 Wronskian](R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md)
(F.10)--(F.13)，两个 finite-$e$ 差商的完整系数绝对和分别
小于 $2^{180}$、$2^{80}$；该 $e$ 门直接给
$W_{\rm res}>\Delta^6$、$W_p>\Delta^2$，
从而 (F.17) 的完整三态行列式大于 $2^{-80}\Delta^4$。
[共同低方向](R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md)
(M.14)--(M.17) 先准确除去 $\kappa(\kappa-e)$，再用
$|P_e-P_0|<2^{90}e$ 和
$|(C_e)_{22}-(C_0)_{22}|<2^{55}e$；
故在 $16e\le\kappa\le1/4$ 有 $C_e>2^{-48}\kappa^2I$，
没有 $e/\kappa^2$ 或 $e/\rho_\ell$ 误差。
[低区实际有限盒](R119-supplement-low-scaled-exact-phase-curve-and-current-mixed-form.md)
(L.16)--(L.20) 保留同两个真 null 后，在 $|\kappa|=1/2$
上比较可去商，仍只使用此 $e$ 门。

[紧区三维图](R119-supplement-compact-scaled-three-parameter-phase-chart.md)
(N.5)--(N.10) 使用 $\kappa-e>\kappa/2$ 及上述完整有限
$e$ 逆；(N.19)--(N.27) 的支集半径只支付局部 flow、
jets 和相位补偿。
[第三相位](R119-supplement-exact-third-phase-kernel-and-local-two-phase-curve.md)
(T.20)--(T.21) 从同一个 finite-$e$ residual Wronskian 得
$\mathcal A g_2>2^{-85}$，(T.35) 在该 $e$ 范围留有
$7/4<F<31/16$ 的真模余量。
[完整高区振荡核](R119-supplement-exact-two-phase-curve-complete-oscillatory-generator.md)
(O.12)--(O.16) 在势及其导数中保留全部 $e$ 项，给
$A=2^{128}$、$H=2^{512}\rho_h^{-3}$；其高阈值约束
$\kappa$，不再缩小 $e$。
特别是以下极小的 $\rho_c$ 不增加 $e\ll\rho_c$ 条件，
上述局部证明没有使用 $j\ge8193$。

采用原低曲线、紧三维图和高曲线的同一半径
$$
 \rho_\ell=2^{-1024}J^{-8},\quad
 r_\ell=2^{-1000}\Delta^2\rho_\ell^9,\qquad
 \rho_h=2^{-40}J^{-2},\quad r_h=2^{-1000}\rho_h^{13},
$$
$$
 K_*=2^{4000}J^{40},\ L_*=1+K_*,\qquad
 \rho_c=2^{-2240}J^{-2}\Delta^{-11}L_*^{-10},
 \quad R_c=2^{-2300}\Delta^{-5}L_*^{-5}\rho_c^{10}.
 \tag{P.14}
$$
坐标为 $\alpha_\ell=r_\ell\vartheta_\ell$、
$q=(R_c/3)\vartheta_c$、$\alpha_h=r_h\vartheta_h$，
$\vartheta\in[-1,1]^5$。三个组的相位补偿也在各自支集内，
总 phase 准确相加为零。它们在 $\|\vartheta\|_\infty<2$
有同一个复延拓；总 $C^4$ 远小于 $2^{-80}$。
故这是真正 (P.3) 的子族。

这些局部证明的两个完整状态、支集长度和当前补偿项均不变。
从中心到两个真实 root 的原完整 Cauchy 可用
$K_i=2^{6000}J^8\delta^{-16}$：
根 germ 和正片完全未改，strict 的 $Q,Q_t,Q_{tt},Q_{ttt}$、
单峰性及密度比满足原显示宽门；完整两行转换使用已经勘误的
自由 Airy 端架，不使用旧的低非mean $b^{1/2}$ 断言。
也可从完整 root-wave 篇 (V.6),(V.9)--(V.13) 逐项读取同一
更宽 $K_i$。它同时保反向流、mean 和 source 的原两分量。

对每个固定 $M\ge4$，$\kappa=M^2/B$，在五盒内取原固定方向
$v_{i,M}$：低区用低坐标，紧区用原三维 $v(\kappa)$，
高区用高坐标。它沿整条参数弦不更新，
$\|v_{i,M}\|_1\le1$。完整负窗的实际径向 generator 仍满足
$$
 -iS_{i,M}^*D_{v_{i,M}}S_{i,M}>D_{i,M}I_2,\qquad
 D_{i,M}=
 \begin{cases}
 2^{-31400}J^{-160}\delta^{73/2}M^5,&\kappa\le1/4,\\
 2^{-861000}J^{-8300}\delta^{131/4},&1/4<\kappa<K_*,\\
 2^{-14800}J^{-64}\delta^{61/2}M^{-3},&\kappa\ge K_* .
 \end{cases}
 \tag{P.15}
$$
其全部半径和物理 $B\Delta$ 费用就是
[五盒谱选择](R119-supplement-five-local-parameter-cube-and-complete-radial-network-selection.md)
(Q.5)--(Q.8) 的逐项乘积，已由以上新入口重新支付。
其它组只影响到真实端口的传播，已由同一个 $K_i$ 收费。

非径向 joint 图也需重新实例化。原
[控制后联立相位](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
(N.2)--(N.16) 的输入分别是完整状态界、
$Q$ 至第三径向导、同一个 radial 两 bump Jacobian、固定复
$\gamma$ 域及真求和。前两项已在 (P.5)--(P.9) 证明；
后两 bump 支集未动，五盒准确保持两个 radial phase，
故 $\bar\Gamma$ 和两行 Jacobian 原值不变。
状态权仍准确是
$$
 N_j^c=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \qquad
 \sum_{j\ge129}(K_j^{\rm ref})^2N_j^c<2^{160016},
$$
包含两个全局逆幂和整个浅前缀。故原 principal KAM 与第二
无限行收缩重新成立于相同小标签球。这里 $D\Gamma^*$ 两列
仍由实际联立方程给出，不因 $D\bar\Gamma=0$ 而消失。
对规范五坐标可使用上述复半径2的 Cauchy 圆；一般浅形状
方向则按第2节的 $2^{80}$ 真实参数范数收费。

## 5. 每个 M 的全部 retained 窗，含浅层

仍令
$$
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 T_j=2^{65664}J^2\delta_j^{-9},\qquad M_*=A_{8193}.
$$
现在对每个 $M\in4\mathbb N$ 保留以下完整内部窗口：
$$
 \mathcal I_M^{\rm all}=
 \{i:129\le j(i)\le8192,\ M\le T_{j(i)}\}
 \ \cup\
 \{i:j(i)\ge8193,\ A_{j(i)}\le M\le T_{j(i)}\}.
 \tag{P.16}
$$
每个根/负窗按原实际拓扑编号；最外未完整分量不在此集合。

所有被删的浅层窗口确实满足高阈值。深于 retained 链的无限
低区使用原真正允许线和完整 affine 源；它不是有限截断。
其它固定前片也用其完整真传递。对固定 $M$ 只有一个有限
连续 retained 链。若该集合为空，就只有原真外传播问题；
实际四重频率下它非空，因为相邻阈值严格重叠，且首浅层已经
覆盖 $4\le M\le T_{129}$。

写 $x=\log_2M\ge2$、$n_M=|\mathcal I_M^{\rm all}|$、
$d_M=2n_M$。不再使用原只在 $x>984$ 成立的 $d_M<M$。
真正的统一计数是
$$
 n_M<16770+16x,\qquad
 J_i<2^{14}(1+x),\qquad
 \delta_i^{-1}<2^{8196}M^8 .
 \tag{P.17}
$$
第一式直接支付最多16128个浅窗以及
$2(8x+321)$ 个深层上包络；后两式分别取浅层
$j\le8192$ 和深层 $A_j\le M$ 的较大上界。

把真实固定部分准确消去后，仍有原有限酉网络
$U_M=P_M\bigoplus_{i\in\mathcal I_M^{\rm all}}S_{i,M}$。
在 $v_M=\bigoplus v_{i,M}$ 的整条弦上，所有这些窗以外的
profile 和固定外参数 $t$ 不变，故 $D_{v_M}P_M=0$。
固定 stop 在此是必要的；本篇没有对随 profile 重停的外线
谎称该导数为零。

## 6. 同一个 cube 的谱计数与一次公共选择

原五盒篇 (Q.10)--(Q.18) 的无极点 local Cayley 图逐窗仍成立：
低/紧控制片的完整近恒等门只用 (P.14) 的短片长度，
高片使用同一真光学区间、完整两行 Duhamel 和准确两 phase。
固定接线可以有 Cayley 极点，继续作为 selfadjoint relation
保留，压到其真实 domain 后有
$P_E C'(s)|_E>0$。所以对每个固定目标圆点，整条弦的
交点总重数至多 $d_M$。这个结论不需要 $d_M<M$，
也不要求各原物理传递矩阵条件数小。

定义
$$
 a_M=\min_iD_{i,M},\quad
 \varepsilon_M=(2^{16}n_Md_MM^{17/16})^{-1},\quad
 \xi_M=a_M\varepsilon_M,\quad L_M=1+\log(8/\xi_M),
$$
$$
 \mathcal T_M=2^{16}n_Md_MM^{17/16}L_M .
 \tag{P.18}
$$
同一个真实谱流变量代换及 cube 入流面 Jacobian
$\|v_M\|_1/2\le n_M/2$ 给
$$
 \mathbb P\left\{
 \operatorname{dist}(1,\sigma U_M)<\xi_M
 \ \text{或}\
 \|D_M^{1/2}(I-U_M)^{-1}D_M^{1/2}\|>\mathcal T_M
 \right\}<2^{-14}M^{-17/16}.
 \tag{P.19}
$$
全部五坐标同时只占一个实际 cube；不按模式重新分配参数半径。

可以同时对原 Q=7 单位网络及完整 root-wave 单位网络作这次选择。
后者使用同一个已付 $K_i$，局部 Cayley 计数不依赖这些固定
symplectic 单位的 norm。对每个频率取两份坏事件，再加
原 fixed-stop 外好角条件，由
$\sum_{M\in4\mathbb N}M^{-17/16}<5$ 得公共好集测度严格大于
$$
                         1-93/16384>0 .
 \tag{P.20}
$$
两个网络各自仍保自己的真实源单位。负频率由实共轭同时取得。

无限参数盒的产品连续性由 (P.9) 给出；新浅参数只有有限个，
不改变深尾一致收敛。闭间隙和闭 inverse 条件的可数交集是
非空紧好集。可以按固定坐标次序取其最小截面来指定一个公共点；
这不是声称已经数值枚举无限参数序列。

## 7. 全频数目转换为每窗自己的权

由 (P.15) 和 $M\le T_j$，三个范围统一满足
$$
 D_{i,M}>2^{-862000}J_i^{-8300}\delta_i^{115/2}.
$$
代 (P.17) 得
$$
                a_M^{-1}<2^{1500000}(1+x)^{8300}M^{460}.
 \tag{P.21}
$$
例如二进制常数逐项为
$862000+8196(115/2)+14(8300)=1449470<1500000$；
这里确实支付了所有低频浅层，而非套用旧 $A_j\le M$。

对任一个 retained 层，$M\le T_j$ 给
$$
 x<65664+2\log_2J+9(J-1)<512J,\qquad J\ge134 .
$$
因此 (P.17) 给 $n_M<2^{14}J,d_M<2^{15}J$。
又 $\log(1+512J)<J/8$，由 (P.18),(P.21) 及
$\log2<7/10$ 逐项得到
$$
 L_M<2^{18}J,\qquad
 \mathcal T_M<2^{63}J^3M^{17/16}<2^{80}J^3M^{17/16}.
 \tag{P.22}
$$
可直接核 logarithm 余量：常数项小于 $7840J$，
$8300\log(1+x)<1038J$，频率项小于 $165245J$，
其余两窗口计数和常数小于 $2J$；总和小于 $2^{18}J$。

于是公共点上对全部 $M\ge4$ 真正有
$$
 \boxed{\quad
 \|\mathcal W_M^{\rm all}(I-U_M)^{-1}
                         \mathcal W_M^{\rm all}\|\le1 .
 \quad} \tag{P.23}
$$
权正是 (P.1)。与旧五盒权准确相比
$\mathcal W^{\rm all}=2^{-16}\mathcal W$，
统一包络为
$$
 (\mathcal W_M^{\rm all})_i^{-2}
       <2^{864032}J^{8330}\delta^{-1073/16}
       =\underline v_j^{-2}.
 \tag{P.24}
$$
这是实际支付有限浅前缀后的新固定常数，而不是新取一个未证明的
$\delta$ 幂。真正不同层的 $D_{i,M}$ 仍在 (P.1) 保留。

另一个便于消费的全频粗 bound 是
$$
                  \|(I-U_M)^{-1}\|<2^{1700000}M^{466}.
 \tag{P.25}
$$
证明使用 $(1+x)^{8300}\le8300!e^{1+x}
<2^{116202}M^2$，以及
$J^3<2^{42}(1+x)^3<2^{47}M^2$。
将它们代入 (P.21)--(P.22)，总二进制常数小于1616329，
频率次方为 $462+49/16<466$。这里没有借 $n_M,d_M<M$。

## 8. 原角宽和完整源

原 $h_j,\zeta_j,b_m$ 未变。对 $M\ge M_*$，
深层 retained 窗仍有 $M\ge A_j$，原
$e^{2^{-800}Mh_j}$ 对谱权的支付留有巨大余量；
新的32 bits不会改变该不等式。
对浅窗，此时 $h_j\ge h_{8192}$、$M_*>2^{984}$，
所以 $2^{-800}Mh_j>2^{154}$，也直接超过 (P.24)
在 $j\le8192$ 的全部 logarithm 费用。

对剩下的 $4\le M<M_*<2^{985}$，只有有限浅窗。
由 (P.25) 可以取同一个明确常数 $2^{2200000}$。
故在**不改变**原角权
$W_{i,M}=\exp(2^{-800}Mh_i)$ 的条件下，
$$
                 \|W_M^{-1}(I-U_M)^{-1}W_M^{-1}\|
                                      <2^{2200000}
 \tag{P.26}
$$
对全部非零四重模成立；$M\ge M_*$ 时原右端1仍可用。
本式付了一个新的固定前缀常数，不把低频浅窗的角收益说成免费。

对原 incoming 源 $g_M$，(P.23) 的准确合同是
$$
       \|\mathcal W_M^{\rm all}x_M\|
               \le\|(\mathcal W_M^{\rm all})^{-1}g_M\|.
 \tag{P.27}
$$
$g_M$ 包含每个负窗两个 particular、positive 全 DN 的 cross
和 affine 项、固定外片两迹、high 前片及无限 low 尾的真实源。
这里没有将 arbitrary ordinary/weak RHS 直接赋予该 incoming norm。

在原固定物理角和 $t=\log r$ 中，总通量仍为
$\pi=\mu_0h_t+F^t$，完整 canonical 两态源仍是
$$
 \binom{-\nu_mr^4F^t/(\sqrt{12}\mu_jp_*)}
       {r^4(f-imF^\theta+M^2F^t)/(12\mu_j)} .
 \tag{P.28}
$$
ordinary 第二行仍为 $\mu_jp_*^2e/(12r^{10})$。
bare flux 另加真实 $F^t$ 端荷，不要求径向微分 $F^t_t$。
所有参数列由当前 profile、真实 $D\Gamma^*$ 和完整材料
Duhamel 进入这同一源合同。

独立物理 mean 保留
$\pi_0(t)=\pi_0(t_0)+\int_{t_0}^t f_0$ 及唯一整体高度积分。
非径向时高度平均的准确式是
$\partial_t\langle h\rangle
 =\langle dh_\theta+\mu^{-1}\pi-\mu^{-1}F^t\rangle$；
不能用径向电阻积分删去那些乘积。
(P.23) 未把 mean 当作一个非零模，也未将其每胞高度分别指定。

固定 stop 后的参数几何源为
$\delta w^{\rm phys}=D_\Pi\bar w_\Pi(a/\rho)[\delta\Pi]$、
$\delta g_{aa}=2w^{\rm phys}\delta w^{\rm phys}$。
$\rho,\ell^0$ 固定；真实 profile 和高度平移源仍保留。
如果另改变外 $t$，必须加入该独立源，不对好点选择函数求导。

## 9. 当前 mixed 接线的已付范围与准确剩余

新浅形状的 $Q$ jets、完整 nonlinear 状态及 $\Gamma^*-\bar\Gamma$
仍满足第4节逐项重新取得的原门。
因此完整 root-wave 篇 (V.1)--(V.24) 和
[真正 deep-low Green/Poisson](R119-supplement-complete-deep-low-Green-Poisson-and-mixed-elimination.md)
(L.1)--(L.25) 的逐点算子比较可以在此家族重新实例化。
这里不需要对外好参数作导数；它始终固定。
8192邻胞仍使用真实 $K=64$，上述新增形状已经包含在它的
同一有序短段估计中。

高外的层权门对任意相邻块比不超过 $2^{256}$ 的正权成立；
$\underline v=2^{-16}v$ 不改变比。deep-low 的相应加权源
$F_j=2^{4096}J^4\delta_j^{-5}$ 和两侧 Poisson 原样保持。
actual 与 radial 的内部剩余差因而满足
$$
 \|\underline v^{-1}(S_{\rm rem,a}-S_{\rm rem,0})
                         \underline v^{-1}\|
 <2^{32-6000000}<2^{-5999900}.                            \tag{P.29}
$$
原全部 mean、未覆盖外源列以及高外 inverse 所需一阶源正则性
均照原范围保留；没有把长程高消元误称为有限邻接。

(P.29) 是已经付清新参数族的实际小差。
(P.23) 则给已经接入原径向外边界的全部非零 retained 有限网络。
在把两者合成真正全逆以前，必须明确同一个物理 mean 商、
完整外条件和 source-to-label 两向映射；开放内部压缩与接入外
反射后的矩阵不能仅因都记作 remaining 就直接识别。
这些识别及完整 $\mathcal F=0$ 不由本篇提前宣告。

本篇关闭的是浅前缀参数权限、全部真实非零频率的有限谱窗口数、
同一个公共参数选择及逐层谱权。全部论证为显示的解析不等式，
复用了已完成的完整前置证明；没有新本地数学实验，也没有
未实际运行的数值通过声明。
