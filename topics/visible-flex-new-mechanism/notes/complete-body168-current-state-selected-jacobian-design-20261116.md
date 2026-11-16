# 完整 body168 当前场 selected Jacobian 设计

日期：2026-11-16。状态：仅纸面公式与源码接口设计；未实现新科学入口，未运行、编译、导入待写模块或执行检查。

## 1. 目的与不可混淆的两种导数

本设计接 [R490 的完整新族](../results/R490-fixed-metric-intrinsic-curvature-bound-and-a-nested-complete-body-extension.md) 和 [R497 的原函数响应](../results/R497-complete-angular-primitive-and-axis-metric-curvature-response.md)。

旧九维纤维将旧159坐标冻结，只改变新增9坐标。将来若转全168联合问题，必须对同一当前完整场的原 scalar rows 求导。设

$$
q=(q_{\rm old},\alpha,\beta,\gamma)\in\mathbb R^{168},\qquad
{\cal R}(q)=\text{原完整 scalar rows 在 }X(q)\text{ 的值}.
$$

所需是 $D{\cal R}(q)$，而不是把旧场 $X(q_{\rm old},0)$ 的159列和新场 $X(q)$ 的9列拼接。

即便旧 $u,v$ 的标量基函数未变，其切向导数中的 $T_u,T_v$ 及其径向导数必须在当前 $(u,v)$ 上评价。即便仅 $\gamma\ne0$ 而 $T$ 没变，当前 $X,X_s,X_{ss}$ 已变，metric/shape/curvature 的外层标量收缩也一般变化。因此“相同旧159参数”不是复用旧最终 Jacobian 的充分条件。

本设计不假定目前九纤维成功或失败，不指定将来的优化点、预算、最优收益或实际候选。当前运行源不改。

## 2. 已读原来源与坐标顺序

本设计静读的是 source commit 09f498cac5d2fad47a35f007b68fe66218420d98 对应源码，后继若改变源须重新显式绑定：

- [frame_complete_body_extension168.py](../scripts/frame_complete_body_extension168.py)：CompleteBody168Field、_Body168Grid.fields、scalar_frame、validate_bound、radial_columns、angular_columns。
- [frame_complete_body_extension168_selected.py](../scripts/frame_complete_body_extension168_selected.py)：已实现的新9 selected 与 metric jets。
- [frame_selected_row_radial_jacobian.py](../scripts/frame_selected_row_radial_jacobian.py)：_families、angular_kernels、virtual_selected_jets、expand_radial_rows、selected_null_height_jets。
- [frame_selected_row_metric_observables.py](../scripts/frame_selected_row_metric_observables.py)：同一次虚拟 jet 收缩中同时得到原 scalar row 与真实 $de,df$ 的方法。
- [frame_entry_single_q.py](../scripts/frame_entry_single_q.py)：complete_tangent_parameter_jets、SingleQGrid 的原 $Q$ 列。
- [frame_entry_paired_repair.py](../scripts/frame_entry_paired_repair.py)：原 paired entry 的 $W_2/W_5$ 径向权。
- [frame_height_null_coordinates.py](../scripts/frame_height_null_coordinates.py)：原精确五高度基及159到163仿射映射。
- [frame_metric_spectral_recovery.py](../scripts/frame_metric_spectral_recovery.py)、[frame_metric_budget_restoration_rows.py](../scripts/frame_metric_budget_restoration_rows.py)、[frame_curvature_psd.py](../scripts/frame_curvature_psd.py)：当前完整 geometry 上的原 scalar contraction。

独立坐标的0-based切片严格为：

| 切片 | 列数 | 物理含义 |
|---|---:|---|
| 0:81 | 81 | 旧 $u$：9径向、9角模，radial-major/mode-minor |
| 81:153 | 72 | 旧 $v$：9径向、8角模，同上 |
| 153:154 | 1 | 原独立 normalized $Q$ 列 |
| 154:159 | 5 | 原 exact-null 高度坐标 |
| 159:163 | 4 | 新 $\alpha_j$，$P_5\sin(2j\theta)$ |
| 163:167 | 4 | 新 $\beta_j$，$P_8\sin(2j\theta)$ |
| 167:168 | 1 | 新 $\gamma$，$\Delta z=\ell\gamma P_8$ |

物理172顺序仍是原163完整物理系数，随后9个新系数。旧159到163的五高度仿射映射不改变，新9为直接和恒等映射。

## 3. 一份当前 scalar frame，三个原角核族

每个所需径向批次先调用当前场的 scalar_frame：

    grid, fields, frame = field168.scalar_frame(q168, radial_query, theta)

其中 _Body168Grid.fields 先用原 reference_evaluation_state(q168[:159]) 保留永久参考高度，再加入当前 $\alpha,\beta$ 的完整四种标量 jet。高度 $\gamma$ 不进入 frame，但进入调用者提供的当前 ordinary。

以下旧基函数只能从 grid.original_grid 读取，不能再让旧159 evaluator 从旧 state 重建 frame：

1. $u$ 原9个角函数及其角导，原9个径向基乘 $W_2$；
2. $v$ 原8个角函数及其角导，原9个径向基乘 $W_5$；
3. normalized $Q$ 的原角函数、角导及单个原径向列。

原径向基 $B_i$ 和权 $w$ 的完整三 jet 为

$$
R_i=wB_i,\quad
R_i'=w'B_i+wB_i',\quad
R_i''=w''B_i+2w'B_i'+wB_i''.
\tag{1}
$$

原 _families 已明确这三个族；新设计只把这段纯基函数读取独立提取，不调用旧 SelectedRadialJacobian 的 constructor/evaluate 或旧 ordinary replay。

原当前布局的 $\theta$ 基先列 $\sin(2j\theta)$，$j=1,\ldots,5$；随后为 material-angle 模及 $u$ 的 core 模。故新增 $j=1,\ldots,4$ 是原 $u,v$ 角模的前四列。这个包含关系必须由冻结的 fold、角模数量、列顺序与源码身份绑定，不能仅由总列数猜测。

因此：

- 计算当前 $u$ 的9-mode角核后，可同时用于旧81列和新4个 $\alpha$ 列；
- 计算当前 $v$ 的8-mode角核后，可同时用于旧72列和新4个 $\beta$ 列；
- normalized $Q$ 保持独立1-mode族。

新增8个切向列不需要额外角 Fourier 原函数。只需将同一角核配到不同径向基。

## 4. 当前场上完整的六 jet 链式导数

设一个标量族为 $w=u$ 或 $w=v$，一个参数方向为

$$
\delta w=R(s)A(\theta).
$$

原 angular_kernels 用当前 fields/frame 调用 complete_tangent_parameter_jets，在虚拟径向值 $R=1,R'=R''=0$ 下产生

$$
F_0=\delta T,\quad F_1=\delta T_s,\quad
F_2=\delta T_{ss},\quad F_\theta=\delta T_\theta,
\qquad P_i=\Pi F_i.
$$

这里 $F_i$ 包含当前两个标量场的所有链式系数，包括当前新8列造成的 $u,v,u_s,v_s,u_{ss},v_{ss}$。随后恢复真实径向基：

$$
\begin{aligned}
\delta T&=R F_0,\\
\delta T_s&=R F_1+R'F_0,\\
\delta T_{ss}&=R F_2+2R'F_1+R''F_0,\\
\delta T_\theta&=R F_\theta.
\end{aligned}
\tag{2}
$$

固定 $a$ 时，完整位置变分为

$$
\begin{aligned}
\delta X&=aRP_0,\\
\delta X_s&=R(a_sP_0+aP_1)+R'aP_0,\\
\delta X_{ss}
 &=R(a_{ss}P_0+2a_sP_1+aP_2)
   +2R'(a_sP_0+aP_1)+R''aP_0,\\
\delta X_\theta&=aRF_0,\\
\delta X_{s\theta}&=R(a_sF_0+aF_1)+R'aF_0,\\
\delta X_{\theta\theta}&=aRF_\theta.
\end{aligned}
\tag{3}
$$

式 (3) 正是原 virtual_selected_jets 的三个虚拟径向 jet。先在完整原角圈求 $\Pi$，再选所需的角点；不得先取点再积分，也不得在 floating 接口中把 $D_\theta\Pi$ 偷换成恒等。

原 scalar row 是当前完整 ordinary 和上述变分的收缩。对同一角模，收缩结果可写成

$$
L_0 R+L_1 R'+L_2 R''.
\tag{4}
$$

原 expand_radial_rows 已实现 (4)，保持 radial-major/mode-minor 原顺序。当前的 $L_i$ 一次计算后：

- 配 (1) 得原81或72列；
- 取角模前4列，配新 $P_5$ 或 $P_8$ 的三物理径向 jet，得新增4列；
- $Q$ 单列按原径向三 jet 展开。

这是原所有 mixed 链式项的完整恢复，不是给旧 Jacobian 加一个 leading correction。

## 5. 六个高度列和准确物理映射

旧五高度列直接用原 exact-null 基：

$$
C_\ell(s)=\text{null_basis.values}(s)_\ell,\qquad
Z_\ell(s)=\text{null_basis.values}(s,\text{integral=True})_\ell.
$$

其变化为

$$
\delta X=Z_\ell e_3,\quad
\delta X_s=C_\ell e_3,\quad
\delta X_{ss}=C_\ell'e_3,\quad
\delta T=\delta X_\theta=\delta X_{s\theta}=\delta X_{\theta\theta}=0.
\tag{5}
$$

新高度列同理取

$$
Z_\gamma=\ell P_8,\quad C_\gamma=P_{8,\xi},\quad
C_\gamma'=P_{8,\xi\xi}/\ell.
\tag{6}
$$

这六列可以作为最后6个小虚拟方向统一收缩，但须 scatter 回154:159和167:168，不能改变坐标顺序。

几何方向 (5)—(6) 不依赖当前幅度；**原 scalar row 的导数仍依赖当前 ordinary**。因此高度列的最终 scalar Jacobian 也不能跨点复用。

原精确物理线性映射为

$$
M_{172,168}=\operatorname{diag}(M_{163,159},I_9).
\tag{7}
$$

所有172物理盒行和任何定义在物理系数上的范数都应使用 (7)。若将来选物理正尺度 $d_{172}$，对应范数为

$$
\|\operatorname{diag}(d_{172})^{-1}M_{172,168}\delta q\|_\infty
\quad\text{或相应 }L^1.
$$

当前九维纤维的 $\delta_{\rm new}=0.25z$、$\|z\|_\infty$ 规范不自动成为全168的规范。本导数模块不选择优化尺度。原九高度系数的有理仿射值仍用于精确物理盒，不能先四舍五入成163向量再判断或求几何。

## 6. 最小 public API

建议新增独立 import-only 模块：

    scripts/frame_complete_body_extension168_joint_selected.py

既有正在运行的 field/new9/helper 源保持不动。建议主函数：

    current_168_selected_rows(
        field, state168, radial, theta, row_ids, bound, cfg,
        *,
        side,
        owned_width=16,
        wall=None,
        need_observables=False,
        paid_zero_old159=None,
    ) -> (J168, diagnostics, observables)

接口语义：

- field 必须是完整 CompleteBody168Field，不伪装成旧 FiveHeightField。
- bound 由原 field.bind_ordinary/validate_bound 精确绑定当前168状态、真实网格、永久参考和完整六 jet。函数内不调用 ordinary。
- row_ids 保原11组编码；输出逐项保持调用者顺序和重复项。
- hard rows 只在存在 groups7—10 时构建第二阶核。selected软行若请求，仍用原 spectral row，而非 Schur 行。
- observables 只对请求中的 group0/1，返回原 row_positions、row_ids、groups、e、f、de168、df168。
- 当前 e/f 来自同一 bound ordinary。导数为
  $de=2X_s\cdot\delta X_s$，
  $df=T\cdot\delta X_s+X_s\cdot\delta T$。
  不从某一 scalar 分支除以 $f$ 反求 observable 导数。
- cfg/side/原 curvature scale/PSD四行公式不改。参数输出轴变为168不授权更换任何旧 row 定义。
- grid theta 使用调用者已绑定的原 binary64 数组，包括真实 fine 数组；不按另一个等价数学表达式重造。
- wall 只用于外部账本 deadline。所有新导数调用和耗时由上层 ledger 明确拥有；本模块不另开预算。

拟实现骨架只需：

1. 校验当前 bound，按原 IDs 分径向批次；
2. 每批在完整 theta 上构造一次当前 scalar frame；
3. 从 original_grid 读取原三个基族；
4. 依次构建当前 u9、v8、Q1角核；
5. 每族先原 scalar 收缩，再按旧径向基展开；u/v同次收缩取前4角模另展开新增列；
6. 最后收缩6高度列；
7. 保原 ID 覆盖及有限结果，返回绑定和账目诊断。

不需要通过继承旧 SelectedRadialJacobian 来放宽其159类型检查，也不需要修改其源码中的 N=159。

## 7. 唯一允许的旧最终 J 复用分支

paid_zero_old159 是可选的**已付原输入**，不是“相近点缓存”。

将原159列直接复用，只在以下条件全部满足时允许：

1. 当前 state168[159:168] 全为 literal zero；
2. 当前 state168[:159] 与已付旧 state159 的完整 binary64 一致；
3. 原 exact 物理163身份、159坐标映射、永久参考 $c^*$、固定 $g,b_0$、原 height-null 基均一致；
4. radial/theta 的数组形状、dtype、每个 binary64 值及原角锚一致；
5. 原 scalar source、group/branch定义、cfg、side、尺度和 row 身份一致；
6. 所需原 IDs 在已付 J 中有明确的源位置映射，逐项保留输出顺序及重复项；
7. 原输入有真实 run/job/source/record/hash 收据，不以重新标记 source accepted index 代替。

在这个零嵌入上，

$$
X_{168}(q_{\rm old},0)=X_{159}(q_{\rm old}),\qquad
D_{q_{\rm old}}{\cal R}_{168}(q_{\rm old},0)
=D{\cal R}_{159}(q_{\rm old}).
\tag{8}
$$

因此 (8) 是准确复用证明，新增9列另外计算即可。非零新系数不走该分支；仅 $\gamma\ne0$ 也不能复用旧最终 scalar J。

如果原已付记录只有 scalar J 而没有请求的 $de159,df159$，不把二者视为免费已有输入。可只复用其 scalar 部分，对真正缺失的 observable 输出另记必要新成本，或让本次请求不索取这些输出。

当前已知54完整 MODEL 与55点不同；54的159列不能拿来构成55的全168模型。55曾保存的 U/T/e/f 也不是55的旧159 Jacobian。本文不预判正在运行任务将交付哪些可复用记录。

反过来，如果未来在同一当前点已付新9 selected J，也可按同一严格身份复用那9个最终输出；这不授权任何跨点复用旧159列。没有匹配记录时，按第3—6节完整当前场公式新算所需导数。

## 8. 全网分离优先用方向 jet，不铺全网168列

selected hard J168 只解决有限约束模型。将来完整 metric 分离不必保存两个全网的每点168梯度。

建议第二个纯接口：

    current_168_metric_direction(
        field, state168, direction168,
        radial, theta, first_jet_bound,
        *,
        owned_width=16,
        wall=None,
    ) -> (arrays, diagnostics)

arrays 只含同一当前点的一维展开 e/f/de/df，附 grid/state/direction 绑定。first_jet_bound 是同一当前 ordinary 绑定的只读 U/T/e/f 子记录，或有同样完整状态/网格/参考身份的已付 first-jet 输入；不能把另一点的 U/T 缓存当当前场。该接口不调用要求七数组的完整 bound validator 冒充一阶输入，而须使用明确的一阶 schema。做法是先把 direction168 按原线性 scalar 基合成为

$$
\dot u,\dot v,\dot u_s,\dot v_s,\dot u_{ss},\dot v_{ss},
\dot u_\theta,\dot v_\theta
$$

中实际需要的部分；metric一阶只需值及一次径向变化。然后在当前 frame 上一次得到 $\dot T,\dot T_s$，使用同一完整 $\Pi$ 形成

$$
\dot X_s=a_s\Pi\dot T+a\Pi\dot T_s+
\left(\sum_{\ell=1}^5 C_\ell\,\dot q_{154+\ell-1}
     +P_{8,\xi}\dot\gamma\right)e_3.
\tag{9}
$$

再与当前已绑定 $X_s,T$ 收缩。没有旧159轴逐一 full-grid 求导，也没有把新9当旧方向。

若某新 attainer 需要完整168梯度，使用第6节单个/少量原 ID 的 selected observable API，在同一基点求一次并绑定该原 tag。不允许同一原 tag 在未知另一个切点求导后仍冒充原基点切平面。

完整分离的两个不同预测保持区分：

- finite master：$\phi_i(q)+D\phi_i(q)\delta q$ 的全原行最大值；
- scalar line：$\phi(e+\alpha\,de,f+\alpha\,df)$ 的 affine-observable 预测。

它们都不是真实新 ordinary。真实候选仍须原完整两网 ordinary 和全部 gates，另行付费。

## 9. 算量和记录结构

对 owned_width不超过16的原径向批次，完整角查询保原零节点及末节点，所以查询径向行不超过18。

原三个角核族共有 $9+8+1=18$ 个角模。逐族处理时最大只有9模；新增8列复用前4模，因此：

- 最大 selected 虚拟参数轴仍为 $3\times9=27$，不是168；
- 曲率批次保 $F_0,F_1,F_2,F_\theta,P_0,P_1,P_2$，一阶批次可不生成 $F_2,P_2$；
- 角核内存按 $O(18N_\theta\cdot3\cdot9)$ 乘固定数组数计；
- 最终输出仅为 $m_{\rm selected}\times168$；
- 径向 expand 只增加新8列和高度1列的少量输出，不增加三个原角族之外的 FFT；
- 不形成 $N_rN_\theta\times3\times168$ 的完整位置 Jacobian，更不同时保存六个这样的数组。

这是结构性算量说明，不是未经运行的秒数、加速比或预算承诺。

diagnostics 至少保：

- 当前168 state、物理172、field/reference/g/b0、cfg、radial/theta及 row IDs 的绑定；
- 当前 frame 构造批次、原三个 family kernel 次数、最大mode/virtual轴；
- selected scalar contraction与径向展开/6height contraction耗时；
- 是否实际复用了旧159或新9输出、对应源收据及 ID映射；
- 本函数内 ordinary调用数严格0；
- 当前 derivative来源是完整新场，未调用旧159 evaluate；
- 所有有限失败及外部deadline，不吞掉部分成本。

没有新增开发门、重复旧秩/优化/全网检查。本设计仅把将来全168联合模型所需的真实数学接口落实为一个小而完整的当前场求导路径；是否启动、采用哪个真实点及预算由后续明确任务决定。
