# R119 续篇：同一固定 stop 新对象的小宽帽输入与完整 94 步预处理链

2026-11-15，visible-exact / tail_connector。

**已证明并独立核对。** 本文在已经定义的新 simple-root、
固定 stop 对象上，在下文明定的共同反射复标签子空间中重新构造
incoming 固定点及 94 次全频修正。
不用旧重停对象的标签、曲面或最后残差。
帽输入只具有物理角宽 $1/8192$；大角宽由同一真实长段的
完整 Dirichlet Green 单独产生，非零远端数据的 mixed 项另行支付。

加权帽篇 (E.12) 的 $q_w<10^{-5}$ 已由公开运行43695160055/1的
完整21门实际通过；[X：实际全模帽](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)
已登记同修补 M32、固定 $\eta_0,\delta=0$ 的真实帽解。
其输入严格限于同一轴上的复偶 $\gamma,f_B$，本文不把这条范围
扩大成任意标签。结论是有限链及其真实非mean斜率残差，
不是全部端点已经匹配，也不是有限 Nash 的 augmented 初始入口
已经满足。

## 1. 精确固定的对象与参数

使用[新固定 stop 对象](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md)
(S.1)--(S.29)，保持 $R=25/8$、原 intrinsic 数据、$a_*,w_*,\omega$、
自然 graft、$B=2^{24}-25/8$ 与
$$
 L=\omega B,\qquad 7/5<\omega<3/2 .
 \tag{P.1}
$$
新 $q=2\to-8$ quintic 和最后 $q=-8$ 平台的长度 $\ell^0$
已经固定，不依赖标签或 $\Gamma$；$\rho,\epsilon$ 始终采用该对象
(S.16) 的实际数。旧 $q=-1$ 重停长度及其导数不进入本文。

一次选定[新完整五盒](R119-supplement-new-outer-five-cube-generator-and-complete-radial-spectral-weights.md)
(C.18) 的公共真实 profile 和外参数 $t_0$。
该同一好集同时包含 root-wave、$Q=7$ 两个网络与新 fixed-stop
对每个 profile 的外 good-angle 条件，测度大于 $1-93/16384$。
以后不根据非zero标签重新选择 $t_0$ 或五盒坐标。

在该点使用[新完整联合两相位](R119-supplement-new-outer-joint-two-phase-scalar-normal-form-and-high-feedback.md)
(J.1)--(J.18) 的同一个 $\Gamma^*(a)$，包括外行 $(129,2)$。
它固定所有真实 principal 目标和完整第二相位目标。
记 $\Gamma^0=\Gamma^*(0)$。这里“同一对象”指这一个 fixed-stop
构造及其已授权的 $\Gamma$ 族；不同有限修正的真实 $\Gamma^*(a)$
可以不同，不能把一次变化度量的预处理称为固定度量方程迭代。

## 2. 真实标签、物理角和有限迹

物理频率 $m\in4\mathbb Z$。原 $\|a\|_\beta$ 是真实尾标签
$\ell^1_\beta$ norm，含原 $b_m$、逐层 $\zeta_j$ 及原
$\sum_m\sup_j$ 次序。它不是 $B$ 端高度 norm。
令
$$
 \beta_H=262144,\qquad \beta_{\min}=65536,\qquad
 s_\beta=\beta-\frac{88823}{400}.
 \tag{P.2}
$$
$\mathfrak Z_s=\dot A^1_s$，高度用 $\dot A^2_s$；指数 $s$ 是
同一物理角 $\theta$ 的宽度。所有 norm 都保留完整正负 Fourier 模。
标签没有独立 Fourier mean；实际高度、曲率和通量的 mean 另行保留。

**共同反射域。** 从这里起，本文所有标签球、方向、线段和辅助
Cauchy 圆盘都取在闭复线性子空间
$$
 {\cal A}^{\rm ev}_\beta
 =\{a\in\ell^1_\beta:\ a_{-m}=a_m,\quad m\in4\mathbb Z\setminus\{0\}\}.
 \tag{P.2a}
$$
这是复线性反射条件，不是实共轭条件；norm仍对全部正负频率求和，
不将两份相容系数只计一次。固定的帽内输入 $\gamma$ 也满足
$\gamma(-\theta)=\gamma(\theta)$，反射轴与实际帽背景相同。

准确依据是[完整 controlled-profile 图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
(C.8)、(C.24)、(C.29) 以及
[真实反射接口](R133-supplement-exact-reflection-sector-and-original-moving-cap-tail-bridge.md)
§5。原 canonical 两行与标签归一只依 $m^2,|m|$，
所以该子空间正是高度 $h$ 偶、$P$ 奇、$K$ 偶、$U$ 偶、$V$ 奇的
相容标签。真实 Darboux 方程、holonomy 小根和完整强修正均保持它。
所有 $\Gamma$ bump、五盒形状与 fixed-stop 系数是径向的，因此
这一保持性对每一个允许复 $\Gamma$ 都成立，包括
$\Gamma=\Gamma^*(a)$；无需额外假定参数图对任意非反射标签的行为。
原完整解唯一性及实际物理角规范于是给
$f(a),k(a)$ 均为同一物理角的偶函数。

新候选 (S.25) 的 balanced 四态、raw/grounded 转换及同一复
$\Gamma$ 盒给真正的有限迹
$$
 f(a)=f_B^{\Gamma^*(a),t_0}(a),\qquad
 k(a)=k_B^{\Gamma^*(a),t_0}(a),
$$
$$
 \|f(a)\|_{\dot A^2_{s_\beta}}+
 \|k(a)\|_{\mathfrak Z_{s_\beta}}
                 <2^{-443}\|a\|_\beta,\qquad \|a\|_\beta<1/64 .
 \tag{P.3}
$$
该费用是 $2^{-447}\mathcal X_\beta$ 与
$\mathcal X_\beta\le16\|a\|_\beta$ 的准确组合。
新末段重新支付的角费仍为 $14825/64$、零阶增长小于 $2^{20}$，
raw 前的余量 $2683/800>3$。由于 stop 固定，复参数只改变原真实
尾系数；不需要沿只有有限径向正则性的接缝作复时间移动。

(P.3) 是全纯 map 的界。原有限 Fourier 构造、完整统一 majorant
和极限唯一性适用于同一新 fixed-stop，不能只由实参数连续性推此结论。
对整个上述复球，
$$
 \|a\|_{224}\le e^{-4(\beta-224)}\|a\|_\beta,\qquad
 16\|a\|_{224}<2^{-365000}<2^{-262144}.
 \tag{P.4}
$$
故新联合 $\Gamma$ 的解析标签域覆盖这个辅助 Cauchy 球。
此球只用于真实值和 Cauchy 导数，不用于需要
$\mathcal X\le2^{-8388608}$ 的网络逆。

对全部复 $\Gamma$ 有 $f^\Gamma(0)=k^\Gamma(0)=0$；
新联合篇也已证明 $D_a\Gamma^*(0)=0$。
于是
$$
 D_0=D[k+C_Lf](0),\qquad
 \|D_0^{-1}g\|_\beta
       \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}}
 \tag{P.5}
$$
准确是新候选 (S.26) 在 $(\Gamma^0,t_0)$ 的全频逆。
$C_{L,m}=|m|\coth(|m|L)$。这里保留真实 1850 宽差；
不会因后续长段筛选很强而把它改成同宽逆。

$D_0$ 是依 $|m|$ 的真实径向 Fourier 乘子，故与
$m\leftrightarrow-m$ 交换；(P.5) 的全频唯一逆亦如此。
限制到 (P.2a) 后，其 norm不增加，输入空间是相应复偶
$\mathfrak Z^{\rm ev}_{\beta+1850}$。因此以下各步实际调用的
$D_0^{-1}$ 均返回 (P.2a)，没有借全标签逆制造奇方向。

## 3. 当前帽给出的唯一小正宽输入

固定 (P.2a) 所述允许的复偶内帽物理非mean曲率 $\gamma$。使用
[小正宽真实高度读出](R133-supplement-small-positive-width-true-cap-to-long-height-readout.md)
(H.18)--(H.21)，取
$$
 \sigma_0=1/8192,\qquad r_f=10^{-8},\qquad r_B=2^{-60}.
$$
由已实际通过的 E 门及 X 的同对象存在性，同一物理帽解给
复偶数据子空间上的全纯 map
$$
 f_*=\Phi_\gamma(f_B),\qquad
 \|\Phi_\gamma(f_B)\|_{\dot A^2_{\sigma_0}}<r_f ,
 \quad \|f_B\|_{\dot A^2_{\sigma_0}}<r_B,
$$
$$
 \|D_{f_B}\Phi_\gamma\|<2^{35}
       \quad\text{在 }\|f_B\|_{\dot A^2_{\sigma_0}}\le2^{-61}\text{ 上}.
 \tag{P.6}
$$
这已包括帽的完整反馈，不再额外加入一次 $D C_R$。
$f_*$ 是 $R$ 处的归一化非mean高度；真实高度是 $a_Rw_Rf_*$。
$C_0(R)$、$B_0(R)$、内端曲率 mean、内端高度和相位保留为真实输出。
(P.6) 不授大物理角宽或强标签。

由 (P.3)，本文使用的全部 $f(a)$，甚至辅助 $1/64$ 标签球上的
$f(a)$，都进入 (P.6) 的严格半球。
帽部分不因长段的某个较大 Cauchy 圆盘而被扩域。
尤其 $1/64$ 辅助球的 (P.4) 及以下所有 Cauchy 导数均限制在
(P.2a)；从未向帽输入任意 full-parity 的复方向。

## 4. 从小宽真实高度构造大宽 incoming 列

直接在[真实长段](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
及[完整长段筛选](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)
的相同方程中重新取基础宽度 $\sigma_0$。
其 Green 逐模对角，完整卷积权次乘，mean 权为1。
因此下列构造不使用原文较大的特定基础宽度。

当 $f_B=0$，在变角宽
$\sigma(t)=\sigma_0+\frac7{16}(L-t)$ 的完整强空间中解真实
Dirichlet 问题。全部径向 supremum 仍在逐 Fourier 模求和之前。
完整 Green 小于160，内端 lift 小于16，
非线性源及导数分别小于 $512H^2$、$2048r_*$
（此节 $r_*=2^{-20}$ 是长段状态球，区别帽高度 $r_f$）。
球像与压缩率满足
$$
 16r_f+160\cdot512r_*^2<r_*,
 \qquad160\cdot2048r_*=5/16 .
$$
holonomy mean 由同一个小根重建；其反馈已经包括在源中。
加权解落入原零宽球，故由原 Dirichlet 唯一性，它就是同一个
真实物理解。取
$$
 S=\sigma_0+\frac{7L}{16},\qquad
 g_*(f_*)=K_{B,\perp}(0,f_*).
$$
原完整边界导数核于是给
$$
 \|g_*(f_*)\|_{\mathfrak Z_S}<18\|f_*\|_{\dot A^2_{\sigma_0}},
 \qquad \|Dg_*\|<24 .
 \tag{P.7}
$$
这是新构造出的实际宽度，不是预先给 $\Phi_\gamma$ 加宽。
mean 斜率另按径向权估计；mean 高度仍按真实积分。

由 (P.1)，$L>23000000$。仅用 $\log2<7/10$ 即得
$$
 E_H=4(S-\beta_H-1850)>39194024>39000000,
$$
$$
 \frac98e^{-E_H}<2^{-55000000},\qquad
 \frac32e^{-E_H}<2^{1-55000000},\qquad
 \varepsilon_L=e^{-7L/4}<2^{-57000000}.
 \tag{P.8}
$$
这些保守整数比较不沿用旧基础宽度的十进制下界。

## 5. 同一新对象上的 incoming 固定点

取
$$
 R_a=2^{-55000000},\qquad
 \mathcal I_\gamma(a)=D_0^{-1}g_*(\Phi_\gamma(f(a))).
 \tag{P.9}
$$
(P.3) 的 Cauchy 导数在 $\|a\|_\beta\le1/256$ 上给
$\|Df\|<2^{-442}$。由 (P.5)--(P.8)，
$$
 \|\mathcal I_\gamma(a)\|_{\beta_H}<R_ar_f,\qquad
 \operatorname{Lip}\mathcal I_\gamma
                 <2R_a\,2^{35}2^{-442}=2^{-55000406}.
 \tag{P.10}
$$
因此有唯一实际标签 $a_0$：
$$
 D_0a_0=g_*(\Phi_\gamma(f(a_0))),\qquad
                     \|a_0\|_{\beta_H}<R_ar_f .
 \tag{P.11}
$$
其尾、有限 connector、帽和 long 都在同一个
$\Gamma^*(a_0)$ 输入及同一固定 stop 下定义。
$g_*$ 保持偶数据，故 (P.9) 准确是 (P.2a) 到自身的压缩；其
存在性并非先在更大的、帽未定义的标签空间证明。
没有先在 $\Gamma^0$ 解出一个标签再忽略真实 $\Gamma$ 回代。

## 6. 非零远端数据的完整 mixed 构造

对任意 $\beta$ 在 (P.2) 的范围中，令
$$
 \alpha_\beta=\frac{s_\beta-\sigma_0}{L},\qquad
 0<\alpha_\beta<1/32 .
 \tag{P.12}
$$
在真正的宽度 $\sigma_0+\alpha_\beta(L-t)$ 中解长段。
两个输入分别是已经证明的
$f(a)\in\dot A^2_{s_\beta}$ 与
$\Phi_\gamma(f(a))\in\dot A^2_{\sigma_0}$。
不向任意窄宽 $f_B$ 免费授予这个域。

先按完整变角宽代数构造背景解。再对固定 $f_B$ 的内端差增加
径向权 $e^{\nu(L-t)}$，$\nu=7/4$。
对每个 $M=|m|\ge4$，有
$$
 \frac{2}{1-[\alpha_\beta+(2+\nu)/M]^2}
       \le\frac{2048}{63},\qquad \|G_D\|<320 .
 \tag{P.13}
$$
原平方为零 Banach module 对这个完整差空间给
$D\mathcal Q\le2048r_*$ 和 $D\kappa\le1024r_*$；
压缩常数为 $320\cdot2048r_*=5/8$。
整个背景本身不需要带径向衰减小量。
因此
$$
 \|\Delta h\|_{\mathcal Y_{\alpha_\beta,\nu}}
                 \le\frac{128}{3}\|f_*\|,\qquad
 \|\Delta\kappa\|_{C^0_\nu}\le\frac1{24}\|f_*\|,
$$
$$
 \|\Delta K_{B,\perp}(f_B,f_*)\|_{\mathfrak Z_{s_\beta}}
              +|\Delta K_{B,0}|<44\varepsilon_L\|f_*\|.
 \tag{P.14}
$$
两端 lift、全部 modes、独立 mean 与真实积分方向均在 (P.13)
的同一 Green 中，不能由一个单向传播界替代。

定义精确 mixed 项
$$
 M_B(f_B,f_*)=K_B(f_B,f_*)-K_B(f_B,0)-K_B(0,f_*).
 \tag{P.15}
$$
零输入的 $K_B(0,0)=0$。只对长段，在每个实际
$\|f_B\|\le2^{-60}$ 周围取半径 $\delta_B=2^{-27}$，
因为 $\delta_B+2^{-60}+r_f<2^{-25}$，完整长段仍在同一个已证球中。
(P.14) 的 Cauchy 估计给
$$
 \|(M_B)_\perp\|_{\mathfrak Z_{s_\beta}}+|(M_B)_0|
    <44\,2^{27}\varepsilon_Lr_f\|f_B\|_{\dot A^2_{s_\beta}} .
 \tag{P.16}
$$
这个较大圆盘只属于长段，绝不是扩大帽 (P.6) 的圆盘。
所有解由原实圈 Dirichlet 唯一性识别。

## 7. 完整 far 方程的真实导数

令
$$
 \mathcal F_\gamma(a)
       =k(a)-K_{B,\perp}(f(a),\Phi_\gamma(f(a))).
 \tag{P.17}
$$
它是新对象的真实全频 nonmean 斜率缺陷。
若 $R_T(a)=k(a)+C_Lf(a)-D_0a$，
$E_B(f)=K_{B,\perp}(f,0)+C_Lf$，则准确为
$$
 \mathcal F_\gamma(a)
 =D_0a-g_*(\Phi_\gamma(f(a)))
       +R_T(a)-E_B(f(a))-(M_B)_\perp(f(a),\Phi_\gamma(f(a))).
 \tag{P.18}
$$
每一项现在确在 $\mathfrak Z_{s_\beta}$ 中。
这是原最终 far 行在新对象上的重新实例化，不以原第94标签替换输入。

(P.3) 和 $\coth(4L)<2$ 给
$\|k+C_Lf\|<2^{-442}\|a\|_\beta$。
在半径 $1/64$ 的同一复球上对完整 Taylor 和作 Cauchy，
对 $\|a\|_\beta\le1/256$ 得
$$
 \|D[k+C_Lf](a)-D_0\|<2^{-433}\|a\|_\beta .
 \tag{P.19}
$$
完整长段 self 源给
$\|E_B(f)\|\le2^{22}\|f\|^2$、
$\|DE_B(f)\|\le2^{24}\|f\|$；
复合 $Df$ 后小于 $2^{-861}\|a\|_\beta$。
最后，由 (P.14)、(P.16) 与帽的完整导数 (P.6)，整个 incoming
复合导数小于
$$
 44\varepsilon_L(r_f/\delta_B+2^{35})\,2^{-442}
                                      <2^{-400}\varepsilon_L .
$$
将这三项以原严格余量相加，得到
$$
 \boxed{\ 
 \|[D\mathcal F_\gamma(a)-D_0]b\|_{\mathfrak Z_{s_\beta}}
 <2^{-400}(\|a\|_\beta+\varepsilon_L)\|b\|_\beta .
 \ }
 \tag{P.20}
$$
非zero标签处的两条 $D\Gamma^*$、完整有限尾和帽反馈已经在此
真实复合导数中。固定 stop 的导数准确为0，而不是删掉移动 stop 源。
(P.20) 的输出仍是 $s_\beta$，没有声明同标签权逆。

## 8. 94 次完整修正的存在与残差

在 (P.11) 上，incoming 部分准确消去。
(P.16)、(P.19) 及 $\varepsilon_L<R_a$ 给
$$
 r_0:=\|\mathcal F_\gamma(a_0)\|_{\mathfrak Z_{s_{\beta_H}}}
 <2^{-432}\|a_0\|_{\beta_H}^2
       +2^{-410}\varepsilon_Lr_f\|a_0\|_{\beta_H}
 <2^{-110000400}.
 \tag{P.21}
$$
设 $\beta'=\beta-2080$。准确宽差是
$$
 s_\beta-(\beta'+1850)=3177/400,\qquad
 \frac1{16}e^{-4(3177/400)}<2^{-49}.
 \tag{P.22}
$$
因此定义全频递推
$$
 \beta_n=262144-2080n,\qquad
 b_n=-D_0^{-1}\mathcal F_\gamma(a_n),\qquad
 a_{n+1}=a_n+b_n,\qquad 0\le n<94 .
 \tag{P.23}
$$
每一步重新使用该标签的真实 $\Gamma^*(a_n)$、真实有限迹、
$\Phi_\gamma(f(a_n))$ 及完整长段解；不冻结任何反馈列。
原固定 stop、五盒 profile 和 $t_0$ 则始终不变。
由 (P.2a)、真实方程的反射保持性及 (P.5) 的限制逆，
$\mathcal F_\gamma(a_n)$、$b_n$、$a_{n+1}$ 和全部积分线段均为复偶。
因此94步和其方向 Cauchy 估计始终合法消费 (P.6)。

(P.22) 给 $\|b_n\|_{\beta_{n+1}}<2^{-49}r_n$。
从 (P.21) 开始的几何和小于 $R_a/8$，而
$\|a_0\|<R_ar_f<R_a/8$，故全部连接线留在
$\|a\|_{\beta_{n+1}}<R_a/4$。
必须在 $\beta_{n+1}$ 上消费 (P.20)：
$$
 \mathcal F_\gamma(a_{n+1})
 =\int_0^1[D\mathcal F_\gamma(a_n+s b_n)-D_0]b_n\,\mathrm ds .
 \tag{P.24}
$$
由 $\varepsilon_L<R_a$ 得统一严格界
$$
 r_{n+1}<2^{-55000440}r_n,\qquad
 r_n<2^{-[110000400+55000440n]} .
 \tag{P.25}
$$
这里有至少8 bits 的额外余量；并非把更新后的较窄 norm 当作旧 norm。
最终
$$
 \boxed{\ 
 \beta_{94}=66624>65536,\qquad
 \|\mathcal F_\gamma(a_{94})\|_{\mathfrak Z_{s_{66624}}}
                          <2^{-5280041760}.
 \ }
 \tag{P.26}
$$
这94步是全频 Banach 算子的准确应用，不是94模截断或一个数值收据。
本篇没有执行新的目标、Fourier residual 或 native 积分。

## 9. 全部 mean、height 与参数身份

每一步的 tail/finite 曲面和 long/cap 曲面各自满足真实
holonomy-one 方程。在 $B$ 它们具有同一个非mean高度 $f(a_n)$，
但其非mean斜率差仅被 (P.25) 控制，尚未置0。
两个 $\kappa_B$ 由各自全部 Cauchy 数据求得；只有斜率完全匹配后，
同一个 holonomy 小根唯一性才给它们相等。本文不把该 mean差先删掉。

物理单位准确为
$$
 v_\perp(B)=a_Bw_B f(a_n),\qquad
 (v_a)_\perp(B)=w_B k(a_n)
 \quad\hbox{或}\quad w_BK_{B,\perp}(f(a_n),f_{*,n}),
$$
$$
 (v_a)_0=w_B\kappa_B,\qquad
 v_0(L)-v_0(0)=\int_0^L aw\kappa\,\mathrm dt .
 \tag{P.27}
$$
北帽的几何高度为 $Z_{\rm ref}-v$，所以其物理导数缺陷是
$-w_B\mathcal F_\gamma(a_n)$；此负号和 $w_B$ 都不能省去。
mean高度跨度不带 $\varepsilon_L$，也不能在两个端点各设一个
平移常数。整条构造只允许一个共同 $\lambda$。

共同反射在 (P.2a) 已作为全过程的定义域限制并逐步验证。
若固定数据还满足实共轭，唯一性再保持该实结构；不能把实结构与
复线性反射子空间混为一谈。
同时平移整个帽数据、背景与尾标签时，$\Gamma^*$ 平移不变；
不能只平移帽未知函数而固定一个不同的非径向背景轴。
内帽 $B$、$C_0$、平均高度及 phase，原 $\nu$ 列和任何独立外
flux/height 荷，仍是后续 augmented 系统必须匹配的端列。

在最终 $a_{94}$ 处可以固定其真实 $\Gamma_2^*(a_{94})$，
然后用已证有限 Sobolev principal 值图在同一点识别
$\Gamma_1$：两者固定相同目标并由真实第一 inverse 唯一性一致。
这只识别种子及其实际度量。后续迭代若使用固定 $\Gamma_2$ 的
有限 Sobolev 图，不得继续冒用本文每步同时重选两相位的规则；
也不得把该图宣称为原解析强标签图的无损延拓。

## 10. 可向有限 Nash 传递的内容与尚缺的入口

由 (P.23) 直接有 $\|a_{94}\|_{224}\le\|a_{94}\|_{66624}<R_a/4$，
所以真实 $\mathcal X\le16\|a_{94}\|_{224}$ 远小于网络工作球
$2^{-8388608}$。原全标签图给同一新物理安装下的局部真解和真实迹。
这些事实可以作为 graph 入口验证的输入，不能跳过该验证。

(P.26) 控制的是 $\mathfrak Z_{s_{66624}}$ 中的 far 斜率。
在其实际频率上转成任意固定有限角导是合法的完整 Fourier 估计；
但它不等于参考 graph 的 $\mathcal N_s^{[3]}$ norm，
更不等于 augmented 边界数据的范数。仍须：

1. 在同一实际段作界面 lifting，支付物理 $w_B$、
   新 $\rho,\epsilon$、全部有限径向导和真实 cutoff 源；
   不能只比较两个很大的二进制指数。
2. 以真实 holonomy 重建 mean，保留一个整体高度规范和其余
   两端 height/flux/phase/内帽曲率输出；它们不是 (P.26) 的推论。
3. 将所得同一状态放入已证参考 graph 空间，并核实际
   $\mathcal E_{1856}$ 低球、有限高 norm、普通三径源和全部端口
   初始阈值，才可消费已发布 finite Nash 的入口。
4. 使用同一完整 nonlinear 外行与全部端列的 onto Schur；
   body 残差极小不使这些独立条件自动成立。

因此本文新增的是利用已经实际成立的复偶小宽帽图、在同一新
fixed-stop 对象及 (P.2a) 标签子空间上的完整有限链。它修复了“旧94步能否直接搬到新对象”的身份
问题；它未将未匹配的帽内端、mean高度或有限 Nash 的完整初值门
隐藏在一个残差数值后面。
