# R149 补篇：真实正侧反馈进入原 graph 高块的精确约消与物理96列

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

**新的解析结论是两个实际接线公式。** 原 common source4 的完整正侧反馈，进入 WGB graph 时可以先作相邻真逆的精确约消，再付 same-window norm；这给新高压缩费 $2^{199}C_+\Lambda_J^{-1/3}$。另外，PN56 的第9号物理 root-even96 port 是整个96维输入的联合范数，能直接为真实物理96列付费，不需从 unsigned 表恢复 signed 矩阵。两项都使用已登记的原坐标与已付旧范数。

这里 $C_+$ 指 future common6 的 **WPL receiver 上界**，不是旧 PC 也记作 $C_+$ 的 source 常数。为防混淆，以下正式写成 $C_{\rm add}$。当前 source4 已完成，但 actual32、common6 和 PN56 尚未完成；因此本篇尚不宣称任何新的耦合高门已经通过。原 WDH 的 selected homogeneous 高逆保持原 scope。

## CG1. 同一个实际高列与新的完整物理列

沿 [CX](R149-supplement-common-high-WPN-source-unit-ball.md) 和 [CXN](R149-supplement-actual-common-high-negative-receiver-execution.md)，真实 common 输入是
$$
x\in X_{\rm fr}^{-4/3},\qquad
(F_x,e_x)=
\left(V_0\Phi x,-(V_{0,R}\Phi-B_R^H\Upsilon)x\right).
\tag{CG.1}
$$
完整 actual physical gate 与两 WPN 行若已完成，给同一 $DF(Q_{\delta_*})$ 的正侧 square inverse，含全部 radial $L^2$、真实外端 B/Cmean、height、jump 和 physical root 条件。将 (CG.1) 交该逆，指定独立 physical root-even96 为零、独立 high stable 为零，得到唯一返回的低／高 correction。它的负侧 continuation 使用原 full SP/PW equation。

记其完整腰密度为 $\Delta Yx$。新的物理 primitive 追加为
$$
\Delta_\partial x=\mathcal R_\partial\Delta Yx,\qquad
\mathcal R_\partial=
\tfrac12U_{\mathcal H^{-1}}(1,1)Q_{R,y}\pi_y .
\tag{CG.2}
$$
$\pi_y$ 仅取原两个 nonmean primitive 分量；两 physical density means 在完整 $\Delta Yx$ 和其独立方程中保留。由原 reflection 身份，(CG.2) 的目标是同一 $Y_a^0$。原实际 row 因而有完整算子恒等式
$$
\mathcal B_{\partial,\rm coupled}
 =\mathcal B_{\partial,0}+\Delta_\partial
 \quad\hbox{在 }X_{\rm fr}^{-4/3}.
\tag{CG.3}
$$
这是 [WHS.38](R133-supplement-rough-stable-inputs-and-complete-positive-head-feedback.md) 的同列追加，现用完整 positive square inverse 代替旧 WHR 的未付 generalized inverse。它没有再保留一个未知正侧 radial kernel/cokernel；若本 actual positive inverse 尚未完成，就不能提前使用这个消元结论。

源的 $N_i$ 已在 $\Phi,\Upsilon$ 里出现一次。$F_x(r_*)=0$ 给物理 $c_*=0$，不等于 auxiliary $E_c^*e_x=0$。完整状态诱发的 outer mean 仍在 $e_x$；独立 rough high baseline 仍是 $\mathcal B_{\partial,0}$ 原对象的一部分，不能被赋予一个无资格的 mixed-root bound。

实际 common6 的正式记录
`common_high_WPL_physical_primitive_upper`
若已完成，才提供
$$
\|\Delta_\partial:X_{\rm fr}^{-4/3}\to Y_a^0\|
 \le C_{\rm add}.
\tag{CG.4}
$$
这里不使用 common6 的 joint incoming/outgoing receiver 球代替 WPL 球，也不从 source4 的 $P,T$ 本身直接推 (CG.4)。

另一方面，对每个原 raw root-even96 输入 $c\in\mathbb R^{96}$，令 complete positive inverse 接收其真实 prescribed root 值、其余独立 positive 输入为零，再作同一负侧 homogeneous continuation 与 $\mathcal R_\partial$。记此实际完整列算子为
$$
H_{96}^{\partial}:\mathbb R^{96}\longrightarrow Y_a^0 .
\tag{CG.5}
$$
它是未来 PN56 的第9号 port，输入 norm 为原 raw Euclidean 96 范数；不把96个坐标当作96个互不相干的列 budget。其正式记录
`negative_port_09_WPL_physical_primitive_upper`
给
$$
\|H_{96}^{\partial}\|_{\ell^2\to Y_a^0}\le D_{96}.
\tag{CG.6}
$$
(CG.5) 定义的是真正 physical Poisson/readout operator，不是 WGB reference complement $C_Q$。实际 signed entries 仍需各自计算；(CG.6) 已足以付下面的完整 operator norm。

## CG2. 保持原 graph、三种投影与所有坐标顺序

使用 [WDH](R133-supplement-explicit-dyadic-high-block-gate-from-complete-waist-error.md) 与 [WBP](R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md) 的同一 selected 函数、实反射线和 complete maps：
$$
\mathcal A=Id-\mathcal T_\alpha I,\qquad
\mathcal B=Id+\mathcal T_w I,\qquad
\mathcal S=U_{\mathcal H^{-1}}U_{X_-}.
$$
$\mathcal W$ 是原完整 WIT density intertwiner。$\mathcal B$ 是 WBP target normalizer，不能换成 old CN 或另一个 target inverse。$\mathcal A,\mathcal W$ 也不是已经放入 $\Phi,\Upsilon$ 的 $N_i$。

同一个 transported source projector 为
$$
\widetilde P=
\mathcal A^{-1}\mathcal W\mathcal S P_{97}
 \mathcal S^{-1}\mathcal W^{-1}\mathcal A .
\tag{CG.7}
$$
$P_{97}$ 是原 natural/model Fourier cutoff，$\widetilde P$ 是同一 real reflected source 上的真 idempotent。另有 target 的 ordinary Fourier cutoff $P_J$；它们从不互换。

保持 WFI/WGB 的完整 graph
$$
\overline M=M_\nu P_{97}+L_{\rm low}Q_{97},\qquad
\overline G=\overline M^{-1}:Y_a^0\to\mathcal D,\qquad
\mathcal D_{\rm true}=\widetilde P\mathcal D .
$$
$\mathcal D$ 的 graph norm、真实96个 constraints 与 low comparison 定义不变。$L_{\rm low}$ 是分析 reference，不是 (CG.5)。

将 (CG.3) 按完整原顺序转换后，新 strong difference 是
$$
\Delta_{\rm ss}
 =\mathcal B^{-1}\Delta_\partial\mathcal W^{-1}\mathcal A
 \quad\hbox{在 }\widetilde X_{-4/3}.
\tag{CG.8}
$$
reference extension 的新 compact 项因此准确为
$$
K_+
 =\mathcal B^{-1}\Delta_\partial
      \mathcal W^{-1}\mathcal A\widetilde P\overline G.
\tag{CG.9}
$$
$\overline G$ 先把 target datum 送入 model graph；随后才允许实际 source projection。$\Delta_\partial$ 只作用于它已付的 $X_{\rm fr}$，没有扩为一个任意 full-circle 算子。

## CG3. 相邻真逆先约消，不重复支付 transported projection

对原整件算子直接代入 (CG.7)，得到
$$
\boxed{\quad
\mathcal W^{-1}\mathcal A\widetilde P
 =\mathcal S P_{97}\mathcal S^{-1}
     \mathcal W^{-1}\mathcal A .
\quad}
\tag{CG.10}
$$
这只用了相邻的 $\mathcal A\mathcal A^{-1}=Id$ 和
$\mathcal W^{-1}\mathcal W=Id$。没有移动 $P_{97}$、$P_J$、sign、density map、primitive 或 model inverse；原真实 full-mean part 也包含在这两个 same-operator inverse identity 中。

设
$$
\mathcal R_{\rm src}
 =\mathcal S P_{97}\mathcal S^{-1}\mathcal W^{-1}\mathcal A .
$$
(CG.7) 的既有 domain 身份给
$\mathcal R_{\rm src}(X_b^{-4/3})\subset X_{\rm fr}^{-4/3}$。
单看 $\mathcal SP_{97}$ 的名字不足以推出这个真实 reflected range；此处用的是已经证明的 transported projection 等式。

WDH 已读完整旧对象给如下有理 dyadic envelopes：
$$
\|\mathcal B^{-1}\|_0<2^8,\quad
\|\mathcal S\|_{-4/3}<2^{29},\quad
\|\mathcal S^{-1}\|_{-4/3}<2^{19},\quad
\|\mathcal W^{-1}\|_{-4/3}<2^{120},\quad
\|\mathcal A\|_{-4/3}<2^{14}.
\tag{CG.11}
$$
原 $P_{97}$ 在 inherited Bessel window 的范数为1，故
$$
\|\mathcal R_{\rm src}\|_{H^{-4/3}\to H^{-4/3}}
 <2^{29+19+120+14}=2^{182}.
\tag{CG.12}
$$
这是完整有序源 map 的上界，不声称其输出仍为 ordinary Fourier high。

WGT/WDH 的唯一高频 gain 来自
$$
\|\overline G P_J:L^2\to H^{-4/3}\|
 \le2K_{\rm CY}\Lambda_J^{-1/3}
 =2^9\Lambda_J^{-1/3},\qquad K_{\rm CY}=256 .
\tag{CG.13}
$$
它发生在 variable coordinates 之前。于是对所有 $J\ge97$，
$$
\boxed{\quad
\|P_JK_+P_J\|
 \le2^{199}C_{\rm add}\Lambda_J^{-1/3}.
\quad}
\tag{CG.14}
$$
相同界也控制 $\|K_+P_J\|$。因为 $\mathcal D\to H^{-1}\hookrightarrow H^{-4/3}$ 的后一个嵌入 compact，$K_+$ 是完整 target $L^2$ 上的 compact operator；不必把正侧 radial head 当有限维。

若把 $\mathcal W^{-1}\mathcal A$ 和 $\widetilde P$ 的旧 separate uppers 独立相乘，会得到 $2^{467}C_{\rm add}\Lambda_J^{-1/3}$。式 (CG.14) 少的268个二进指数来自准确邻接约消，不是从两个 norm upper 相减。原 WDH 的其他旧项没有因此被改写成一个更小的未付 record。

## CG4. 原固定 $J=2^{4608}$ 上的 complete coupled high gate

令 $K_0$ 是 WDH 的完整 reference-extension remainder，保其全部 old physical error、mean ranks、root/finite terms 与 $K_{\rm ref}$。WDH 已证明
$$
\|P_{J_\dagger}K_0P_{J_\dagger}\|<2^{-44},
\qquad J_\dagger=2^{4608}.
$$
本式的下标0仅表示原 homogeneous row，不能与旧 source 常数或 Volterra operator 混同。

正侧 full feedback 后
$$
K_{\rm coupled}=K_0+K_+,\qquad
H_{\rm coupled}=Id+P_{J_\dagger}K_{\rm coupled}P_{J_\dagger}.
$$
由 $\Lambda_J\ge J$，
$$
\boxed{\quad
\|H_{\rm coupled}-Id\|
 <2^{-44}+2^{-1337}C_{\rm add}.
\quad}
\tag{CG.15}
$$
一个便于实际 whole-ball 消费的充分条件是
$$
C_{\rm add}\le2^{1335}.
\tag{CG.16}
$$
在此条件下 (CG.15) 小于 $1/2$，故同一个 graph target 上
$$
\|H_{\rm coupled}^{-1}\|<2.
\tag{CG.17}
$$
(CG.16) 必须核未来 common6 的 **完整正式球上端**，包含其保存半径；当前不能从 source4 的 $P\approx2.15\,10^{37}$ 预判它通过。原 cutoff 不会使一个未付 receiver 自动有界，也不会使一个 huge finite matrix 自动可逆。

## CG5. 真实96物理列的左变换与完整 finite factor

在 WGB 的 normalized target 上，
$$
H_{\rm phys}=\mathcal B^{-1}H_{96}^{\partial}.
\tag{CG.18}
$$
它只收左 target factor，不能右乘 $\mathcal W^{-1}\mathcal A$ 或 $N_i$。选其 $c$ 正是原 physical raw root-even96 坐标。原 transported reference maps 仍为
$$
\mathcal U=\mathcal A^{-1}\mathcal W\mathcal S D_+,\qquad
C_Q=\mathcal U E_{96},\qquad
V_Q=E_{96}^*\mathcal U^{-1},\qquad
\Theta=V_Q\overline G .
\tag{CG.19}
$$
$D_+$ 与 $E_{96}$ 的原 phase/reflection 规范保留，$E_{96}$ 是96维 Euclidean norm 的 isometry。更明确地，WDH.3 的 $D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-$ 在非均值 Fourier 载体上只有模长一的符号，因此 $D_+$ 及 $D_+^{-1}$ 都与 Bessel 权交换，且在 $s=0,-1,-4/3$ 每个所用同阶窗口的算子范数恰为一；这也就是 WFI4 使用的 fixed unitary。

这给一个真正定义完的 primitive square
$$
\mathcal L_{\rm phys}^{\sharp}\overline G
 =Id+K_{\rm coupled}+U_{\rm phys}\Theta,\qquad
U_{\rm phys}=H_{\rm phys}-\overline M C_Q .
\tag{CG.20}
$$
(CG.20) 来自 WGB.25–27 的 complete coordinate isomorphism，而不是把 reference columns 改名为 physical columns。实际 positive square 唯一性使这里的正侧 head 与外端状态均已消去；独立 prescribed positive ordinary/jump sources 仍进入完整右侧。原负侧/腰/mean/parameter 条件没有被这个正侧消元删除。

原 norm bound $B_i<4$ 控制 $\|v_i\|_\infty$，$W_0<2^9$ 控制 $\|w\|_\infty$。因此
$$
\|\alpha\|_\infty<4+512<2^{10},\qquad
\|\mathcal A^{-1}\|_0\le1+\|\alpha\|_\infty/4<2^9 .
$$
同一个 whole WX execution 中，
`complete_selected_common_input_conclusion.complete_common_input_L2_upper`
的原球为
~~~json
{"ball":"[5.262867547817867306879019910803827331274181821819889 +/- 1.46e-52]"}
~~~
故 $\|\mathcal S\|_0<2^3$。这是从整件 old WX 直接读取的 forward bound，不是由 inverse 或 source product 反解。配合原 $\|\mathcal W\|_0<2^{120}$，
$$
\|C_Q\|_{\ell^2\to L^2}<2^{132},\qquad
\|\overline M C_Q\|<2^{137}.
\tag{CG.21}
$$
后一式使用 WFI.7–11、WGB.8 的完整 reference 界
$$
\|\overline M\|_0
 \le\max\{\|M_\nu P_{97}\|_0,\|L_{\rm low}Q_{97}\|_0\}
 \le\max\{1+|\nu_i|/4,1\}
 =1+|\nu_i|/4<2^5 .
$$
这里 $L_{\rm low}$ 按 WFI.10 把同一归一化源基向量送到对应目标基向量，范数为一；源和目标的 low/high 块在 $L^2$ 都正交。因此这个界包含全部 $L_{\rm low}Q_{97}$，并非只给主模型 high 分支的估计。
于是
$$
\|U_{\rm phys}\|\le2^8D_{96}+2^{137}.
\tag{CG.22}
$$
这里对 exact operator difference 使用 norm 的和，不相减两个 upper。

再由
$\mathcal U^{-1}=D_+^{-1}\mathcal S^{-1}\mathcal W^{-1}\mathcal A$，
以及 $\Lambda_{96}<2^9$，
$$
\|\Theta P_J\|
 \le 2^{19+120+14}\,\Lambda_{96}^{4/3}\,
       2^9\Lambda_J^{-1/3}
 <2^{174}\Lambda_J^{-1/3}.
\tag{CG.23}
$$
这里仅在 Fourier 抽取 $E_{96}^*$ 的原位置使用 $\Lambda_{96}^{4/3}<2^{12}$。没有把 transported row 当作 ordinary low-support row。

因此，若实际要直接吸收这个 genuine finite factor，它的完整高压缩满足
$$
\|P_{J_\dagger}U_{\rm phys}\Theta P_{J_\dagger}\|
 \le 2^{-1354}D_{96}+2^{-1225}.
\tag{CG.24}
$$
特别是同时有
$$
C_{\rm add}\le2^{1334},\qquad
D_{96}\le2^{1351}
\tag{CG.25}
$$
时，完整 **physical96 augmented primitive square** 的高/high block 有
$$
\|H_{\rm phys,high}-Id\|
 <2^{-44}+\tfrac18+\tfrac18+2^{-1225}<\tfrac12,
\qquad
\|H_{\rm phys,high}^{-1}\|<2.
\tag{CG.26}
$$
(CG.25) 是两个未来实际正式上端的 sufficient tests，当前均未支付。并且这个直接吸收是可选的：原 WGB 将 $z=\Theta u$ 留为辅助变量时，无需任何 $PU_{\rm phys}\Theta P$ 小量条件，仍可先使用 (CG.17)。

## CG6. 精确留下的 finite/mean/metric 方程

若使用 auxiliary 格式，保
$$
(Id+K_{\rm coupled})u+U_{\rm phys}z+g\kappa=f,\qquad
z=\Theta u,\qquad
\ell u+\omega\kappa=f_\nu .
\tag{CG.27}
$$
其 high elimination 使用 (CG.17)，全部 $(q,z,\kappa)$ blocks 正好是 WGB.30–34，以完整 $K_{\rm coupled}$ 代入。若改用 (CG.26) 直接吸收 $U_{\rm phys}\Theta$，则 ordinary target 的完整 low complement $Q_{J_\dagger}Y_a^0$ 仍有 $J_\dagger-1$ 个实坐标；没有剩下一个已解的96维 determinant。

没有添加 physical96 columns 的 homogeneous problem 仍须保 $\Theta u=0$；它们只有在 (CG.20) 的真正 source augmentation 中才按 coordinate isomorphism 被编码。两种系统不得混用，也不得把 $\Theta$ 的未算 row 当零。

其他独立 finite physical 坐标、mean、height、真实 $\nu$/phase 行仍在原 full square 中；projection 应为 $P_J\oplus0_{\mathbb F}$。auxiliary scalar Fourier mean 与两 physical density means 不是同一个量。参数变化的完整 body/cap/waist/mean/jump column 和 frozen-chart defect derivative 保持原 RNS 规范。

本篇新高结论属于右 graph inverse 后的 $L^2$ primitive target realization，其高 gain 是 $\Lambda_J^{-1/3}$。它不把此结果改名为 RNS 原 principal-preconditioned $\Lambda_J^{-4/3}$ 门，不宣称一个未指定完整 square 的 incoming 逆，也不供应 all-$s$ 或全参数 tame inverse。

## CG7. 消费边界与本次没有重做的量

纯 adapter 为
[fourfold_codazzi_coupled_positive_graph_high_math.py](../scripts/fourfold_codazzi_coupled_positive_graph_high_math.py)。
它消费完整 actual common6 与 PN56 的指定正式球，先形成 $\delta_+$ 与 coupled $\chi$，再形成 physical96 高费与 complete augmented $\chi$；每个 dependent 值由 caller 完整保存并读回之后才参与下一式。actual gate 与 execution 的整件准入由未来实际 owner 负责；纯函数输出本身不是公开科学证书。本次未生成其 manifest/workflow，也没有运行新 scalar。

原 WDH 的五份 old whole 文件与九个界不重算。新增使用的唯一 old scalar 是上述 WX 同一 whole execution 的 $L^2$ forward 因子；其 full file 为
`notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json`，
Git blob `5121a599896025d90e2861450756a256aaba659d`，
43753 bytes，SHA256
`e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12`。
common6 的 NIF→WX full-file bridge保证这是同一 selected chart。

原 source4 的完整实际 run45783842857/1、四球、state-induced outer mean 以及全部18槽按原文件保留。它单独不证明 (CG.4) 或 (CG.6)。actual58/224/32、common6、PN56 真正完成后，以上两个新 norm input 才有资格进入本篇测试。任何 false sufficient test 仅保留其本义，不作为 BVP 奇异证据，也不修改原 homogeneous WDH 的成功。
