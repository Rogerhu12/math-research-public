# R714 实施后继：同调用完整 detached 阶段矩阵的可复用边界

## 1. 状态和实际源码

这是独立源码分析及可执行接线设计；尚未实现或执行矩阵缓存。它不修改已经锁定的 C1/frame-value 完整入口，也不是新的 envelope 入口的运行前门。没有本地科学计算、速度或重复率结论。

实际已逐函数读取的完整 operator 为 so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py，95,491 bytes，SHA-256 a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd。其 _stage_control_jets、_stage_constraints、_stage_jacobian、_stage_jet_jacobian、_finish_stage_jets、_solve_stage、_run_chain、_get_roots、_implicit_jet_value 是本分析的实际接口。

原完整 frame helper 为 normal_frame_c1_reuse.py，34,905 bytes，SHA-256 ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9。它已经有同调用的 detached frame 值复用及 active 一阶重接。这里讨论的是另一个函数的 detached 矩阵数值，不把 frame 缓存当作矩阵缓存已经实现。

## 2. 固定阶段的完整方程

固定某角及其原数据，令 p_j 为前一阶段的六控制第 j 角导数，B_j 为前一阶段 normal frame 的第 j 角导数，尺寸 3×6；eta_j 为本阶段三增量的角导数。原代码的完整控制 jet 为

$$
u_0=p_0+B_0^T\eta_0,
$$
$$
u_1=p_1+B_1^T\eta_0+B_0^T\eta_1,
$$
$$
u_2=p_2+B_2^T\eta_0+2B_1^T\eta_1+B_0^T\eta_2.
$$

这里 B_j 在“对当前 eta 的局部偏导”中固定，但在原外参数隐式链中绝不固定。设 f 是源码 _closure_jets 所代表的完整中心化 closure，则原阶段约束为

$$
G_j(\eta)=D_\phi^j f(u(\phi),\phi)-(1-\tau)z_j,\qquad j=0,1,2,
$$

其中 z_j 是同完整点的零控制 closure jet。tau 为该阶段已声明的共同辅助分割值，不是物理弯曲参数。

对局部 eta 求偏导时，tau、z、p、B 及 data 都固定。因此

$$
D_\eta G =D_\eta(D_\phi^j f),
$$

与仅出现在加法右端的 tau 和 z 独立。这个结论不删除原 G；原每阶段 residual、Armijo、控制域、原物理容差与最终闭合复读仍必须使用该阶段的实际 tau、z。

同一个 eta 在两个不同 tau 上可能满足完全不同的方程。矩阵可相同不意味着根、解方向、接受状态或残差可复用。

## 3. 完整 3/6/9 块及所需信息

在实际控制 jet u 处写

$$
C_0=f_u,\quad
C_1=D_\phi(f_u),\quad
C_2=D_\phi^2(f_u),
$$

其中 C1、C2 包含 u1、u2 的完整 total-angular 链。定义

$$
M_0=C_0B_0^T,
$$
$$
M_1=C_1B_0^T+C_0B_1^T,
$$
$$
M_2=C_2B_0^T+2C_1B_1^T+C_0B_2^T.
$$

由完整控制式逐项微分，准确局部矩阵为

$$
J_3=M_0,\qquad
J_6=\begin{pmatrix}M_0&0\\M_1&M_0\end{pmatrix},
$$
$$
J_9=\begin{pmatrix}
M_0&0&0\\M_1&M_0&0\\M_2&2M_1&M_0
\end{pmatrix}.
$$

这说明它依赖当前 data、p、B、eta 及所请求角阶。仅匹配 p0、eta0 不足：若 u1/u2 或 B1/B2 不同，完整 J6/J9 可以改变。也不能只匹配 u，因为同一 u 对应不同 B 时，当前法向增量的坐标映射不同。

本后继不建议用上述结构重拼浮点矩阵，不从另一个阶数裁切或补零推定工作值。首版可只缓存原 _stage_jacobian / _stage_jet_jacobian 真正返回的完整 J3/J6/J9。kind 和角阶分开，完整数组的字、形状和布局进入键，已有源码允许的 same-branch jet upgrade 逻辑保持原样。

## 4. 实际源码中的数值导数边界

原 _stage_jacobian 先把 eta detach/clone 成一个新的局部叶，然后调用完整 _stage_constraints(order=0)，逐行 autograd.grad(create_graph=False)，最后 detach 完整矩阵。原 _stage_jet_jacobian 对 eta 的 1 或 2 角 jet 做相同操作，分别输出 6×6 或 9×9 全体。

因此原实现本来就把这些矩阵作为数值系数。_implicit_jet_value 保留完整原 residual 的 active 图，以这些 detached 矩阵做各阶段零值隐式修正；完整上游 data、previous、frame、zero-target、eta 和 control 的一次外参数链仍从原 residual 保留。对相同完整输入复用同一数值矩阵不需要再做 R714 的 C1 重接，也不得用这个事实去 detach 原 residual。

_get_roots 的 linearization 部分可能在外部 grad-enabled 环境中调用，但它在进入矩阵计算前已 _detach_data，并从完整 cached 根的 numpy 字构造 previous、frame、eta、zero。是否安全取决于这些实际输入均无 active 图，不等同于只检查全局 torch.is_grad_enabled() 为 false。

矩阵值不能从另一 active graph 偷取。即便新 scope 所处全局 grad mode 为 true，它消费的局部矩阵输入也必须逐项证实 detached，结果也仍为原 detached 完整矩阵。反过来，若 data、previous 或 frame 留有参数图，本后继直接拒绝数值缓存路径，而不是假装矩阵的高阶外导已经被支付。

## 5. 最窄接线只需两处

可以保持下面三个原完整方法字节和 AST 不变：

- _solve_stage；
- _stage_jacobian；
- _stage_jet_jacobian。

也不需要把方法临时 monkey-patch 成另一个来源。拟在两个现有调用点显式传给独立 scope：

1. _run_chain 在完整原 _solve_stage 真正返回成功后，原本再次调用 _stage_jacobian，取得给角 jet solve 的 returned-value J3。仅在这个调用点尝试同 scope 数值复用。
2. _get_roots 的 need_linearization 分支，在同一个 detached subset 上逐 stage 构造完整 J6/J9。仅包住这次完整 for-stage 循环尝试复用。

原 _solve_stage 内 Newton 的所有矩阵计算仍原样，首版不缓存它们。因而原失败记录 last_evaluated_plane_matrix 仍准确代表该次 Newton 点的真正原公式计算，不会被悄悄改成来自另一个 stage 的值。若以后要覆盖内层 Newton，必须另改完整记录语义和 source guard，不能在本首版说明中冒称已经覆盖。

这两处本来在 ba3d 的九个完整方法 AST 之外。由此可以不松开现 ba3d 对 _solve_stage、两 Jacobian 和完整 closure/frame/control/constraint 的守卫。新的 operator/schema、独立 calibration schema、geometry/driver/reader 仍须作为完整新来源闭包派生，不可直接改 a62c 原字节。

## 6. 完整 scope / key 合同

拟独立组件为 CompleteDetachedStageMatrices，接口草案：

- scope(data, literal_phi_hex_keys, order, phase)；
- scalar(eta, previous, frame, zero, tau, stage_index)；
- angular(eta_jets, previous, frame, zero, tau, stage_index, order)；
- close()。

scope 只跨一次 _run_chain 的 returned-value 请求或一次 _get_roots 的需要 linearization 的完整子循环，不跨二者，不跨调用、当前点、batch、角顺序或 source。

它至少绑定：

- 当前 operator/base/calibration 的完整实际 source 和 canonical model identity；
- _stage_constraints、_stage_control_jets、_closure_jets、_corrected_jets、_total、两原 Jacobian 的完整 codefile 与 AST；
- 当前完整 free point 摘要；完整 phi 原顺序及所有 literal hex；
- data 的完整递归结构、Tensor 对象/version/dtype/device/shape/stride/storage offset，并确认全部 detached；
- 本次 q.S 的 binary64 字、J、integration_order、完整 mesh 与 gauss_w 原字及实际 _total 来源；
- 每次 previous 的全部 3×6 字、frame 的全部 3×3×6 字；
- scalar 请求的全部 eta0 字，或 angular 请求的全部 3×3 eta jet 字；
- 对这些请求数组的 shape/dtype/device/stride 等工作表示；kind/角阶；本次共同阶段分割和真实 stage 顺序。

全部实际 words 包含 signed zero；不使用近似距离、根容差、数值秩或“预期零根”匹配。scope 不把另一 order 的缺少 jet 填零之后冒充完整键。tau 不作为矩阵等价键，但每次仍核它是本 stage 的实际共同分割载体；zero 的本次完整字与来源绑定、实际方程仍照读，不能从自由输入省掉它。

上述额外 mesh/weight 字绑定是因为 _total 实际读取 np.diff(q.mesh)、q.gauss_w 和 integration_order；不能只凭 data 张量相同而忘掉外部积分载体。

## 7. 数值、计数、失败与回退

缓存第一次 miss 必须原样调用原完整矩阵函数。只有有限的完整结果才保存独立克隆；每个 hit 返回克隆，防止当前 solve 或保存代码修改缓存。可选保存/克隆的 MemoryError 或 RuntimeError 只使当前键回原公式或返回刚刚真正算出的原值；身份、shape、source 错误不吞。

缓存失败不改变 root tolerance、不加 ridge/jitter、不截断矩阵秩、不替换 solve，也不把先前阶段成功搬到本阶段。原三/六/九维 solve 和所有 stage 的原约束、物理域、接受/拒绝、终点真复读照旧执行。

原矩阵函数内部的 actual normal_counts 只在真正执行原函数时增加。cache hit 不能假增 stage_matrix_angle_evaluations、stage_angular_matrix_angle_evaluations、actual_implicit_matrix_angle_rows，亦不能假增其内部 _closure_jets / _stage_constraints 计算次数。

应另设实际逻辑请求数、真实原公式计算数、hit、保存/clone 回退、各尺寸角块数和 payload bytes；记录每个逻辑请求来自哪个同 scope 的首 miss、first stage、kind、order、完整 key 摘要。某阶段使用了旧矩阵值应称“同输入原矩阵值复用”，不称“该阶段重新计算了原 Jacobian”。

完整 root stages 中保存的 J/jacobian 仍有该阶段实际使用的完整值。reader 必须区分数值来源与该阶段实际 residual 记录，保旧根/trace/current-point 责任，不由 cache hit 推出 stage 或场成功。

## 8. 准确结论和未支付范围

在上述全输入相等条件下，准确数学矩阵是同一矩阵；省去重复生成这个 detached 数值系数不会删掉一次完整隐式链。这个结论不要求初点残差为零，也不要求 normal 的全部阶段为零根。

实际返回的浮点矩阵是一份既有工作读数。复用它可保持该字串；不能由源码分析保证另一次执行在任意硬件、并行库、调度或不同 batch 布局中都会逐字产生相同结果。本设计因此完整绑定同调用、布局、CPU float64 和原算术来源，也仍明确不提供舍入或误差包围。

共享输入不存在时走原完整路径。尚未有实际 hit、加速或主要耗时占比证据；尤其不能用此前长运行推断 J9 必定是首要瓶颈。新缓存也不能证明矩阵可逆、法向路径全程可行或最终闭合。准确所有阶段仍由原 source 对每阶段自己承担。

这份分析足以支持一个范围明确的独立实现；本次没有改动已锁 full entry，也没有把它添加成 envelope 新科学方向的先决条件。

