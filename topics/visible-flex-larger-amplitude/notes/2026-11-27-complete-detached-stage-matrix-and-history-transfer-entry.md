# 完整 detached stage-matrix 复用入口与跨来源地址、变量继承

日期：2026-11-27。状态：完整源码、纯源码再生器与未选初点的参数计划；没有运行本入口的科学计算，也没有缓存命中率、加速、根收敛或新场几何结论。

本实现应用已登记 R714 的同调用缓存原则，并保留 R715 的完整参考中心化六 jet。它接在完整材料包络入口 cc0a 之后。已准入的 cc0a 来源不变，新来源独立声明模型、校准 helper、几何入口、驱动器与纯读数器。完整参数计划没有可直接排入队列的 steps；实际前驱终态和初点选择尚未绑定。

## 0. 未执行来源的两处计数键修订

此完整交付为独立 revision2。前一份未执行 helper 29c634f2bcffd110bdba875bbc6df44b20298da8525de8f3397f97861f2cd339 中，NORMAL_COUNTER_KEYS 已含 actual_implicit_matrix_angle_rows，但原方法计数累计与 pure validator 各有一处机械再加 actual_ 前缀，导致访问不存在的 actual_actual_implicit_matrix_angle_rows。该问题在最终纯源码检查时被发现；没有将首次矩阵调用成功或科学失败当作已发生事实。

revision2 仅将这两个目标表达式改为：已有 actual_ 前缀则直接用原键，否则增加该前缀。反向替换两处可逐字恢复旧29c完整SHA。全部五个源计数名与目标键一一对应，scalar/angular 两个动态目标也静态逐项核到实际完整初始化表。原矩阵、公式、scope、检查、回退及数值返回均不改变；后继算子/几何/driver/launcher/reader只更新实际依赖SHA。

旧稿的AST/compile和定点审查没有覆盖这个动态键错误，不应说成它当时已闭合全部counter。此修订保留旧完整源码与原交付身份，新增来源与参数计划重新锁定；当前已准入cc0a入口没有被修改。

## 1. 本次范围与完整父来源

本次仅给两个既有的 detached 矩阵读取位置增加同一次调用内的复用。Newton 内部矩阵、每一阶段原方程、控制域、线性解、回溯、残差复读、全阶段角 jet 链、原 QP 与 Phase I、全部真几何筛查仍按原源码执行。

原 normal 算子完整来源为 a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd；原 C1 helper 为 ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9；原校准 helper 为 3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991。

原完整材料包络驱动器是 cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5，原完整纯读数器是 104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7。这两个真实父来源用于验证前驱报告；没有把旧报告改为新 schema。

完整材料责任仍由 c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152 消费，行选择仍用 729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7。全部已知显式地点及其已知保护标记、旧/新完整径向角网格、两主曲率分支及两符号 witness 责任保留。未知旧保护标记或优先次序没有被重建或声称重建。

本入口没有修改固定参考 seed、准确标量目标、固定材料角图、原自由变量布局、固定 Q 的十八个字、支持区间、gamma 形状、共同 normal 分割或 H² 范数。新模型增加明确的数值复用政策和新的实际来源身份。准确算术中相同方程，不意味着未经执行的新旧浮点场逐字相同。

## 2. 为什么阶段矩阵可在声明条件下复用

固定一个完整径向数据批和角批，记上一阶段控制的三组角 jet 为 $p_0,p_1,p_2$，上一阶段 normal frame 的三组角 jet 为 $B_0,B_1,B_2$。阶段增量为 $\eta_0,\eta_1,\eta_2$。原控制装配为

$$
u_0=p_0+B_0^T\eta_0,
$$

$$
u_1=p_1+B_1^T\eta_0+B_0^T\eta_1,
$$

$$
u_2=p_2+B_2^T\eta_0+2B_1^T\eta_1+B_0^T\eta_2.
$$

设 $f$ 为当前完整的无量纲、参考中心化端点映射。原阶段方程的第 $j$ 个角 jet 是

$$
G_j=D_\phi^j f(u,\phi)-(1-\tau_i)z_j,\qquad j=0,1,2.
$$

这里 $z_j$ 是同一完整自由点上零控制目标的角 jet。局部求矩阵时，$\eta$ 是唯一被微分的局部变量，$p,B,z,\tau_i$ 与完整数据保持固定。因此 $-(1-\tau_i)z_j$ 对所有局部 $\eta$ 的偏导严格为零。

写 $C_j=D_\phi^j f_u$，则

$$
M_0=C_0B_0^T,\quad
M_1=C_1B_0^T+C_0B_1^T,
$$

$$
M_2=C_2B_0^T+2C_1B_1^T+C_0B_2^T.
$$

相应原矩阵是

$$
J_3=M_0,\qquad
J_6=\begin{pmatrix}M_0&0\\M_1&M_0\end{pmatrix},
$$

$$
J_9=\begin{pmatrix}
M_0&0&0\\
M_1&M_0&0\\
M_2&2M_1&M_0
\end{pmatrix}.
$$

这证明局部矩阵在固定完整输入下不依赖 $\tau_i$ 或零目标右端。它不允许把完整外参数链中的 $p_x,B_x,z_x$ 删去，也不允许省略每个阶段自身的 $G_j$ 复读。实际 active 隐式链继续使用全部这些导数。

实现并不按上述块公式重排矩阵，也不截取另一类矩阵：一次首次请求调用原完整 J3、J6 或 J9 方法，保存实际返回的整个数值矩阵；以后只有完整相等条件满足才克隆该原矩阵。没有声称未执行的新 AD 调用一定产生逐字相同结果。相同字的缓存定义、原运算来源、不同阶段的残差与根责任在报告中分别记录。

## 3. 两个明确且互不混用的调用范围

完整 helper 的类为 CompleteDetachedStageMatrices。构造时绑定当前完整 q、完整模型 identity、实际算子/校准/C1 来源以及九个原方法的 AST。

公开数值接口是：

    kernel.scope(data, keys, order, phase)
    scope.scalar(eta, previous, frame, zero, tau, stage_index)
    scope.angular(increments, previous, frame, zero, tau, stage_index, order)
    kernel.metadata()

phase 只有两个声明值：

- returned_value_J3：原新根链中每次原 _solve_stage 成功之后，调用方原本另外读取的完整 J3。
- complete_angular_J6_J9：_get_roots 在固定 detached 子批、固定角阶下，为全部原阶段准备一阶或二阶角 jet 的完整矩阵。

第一范围仅在 existing is None 的全新链上创建。对同一已选分支从一角阶升级到二角阶时，原 eta0/eta1、control0/control1、已有 J3 的字继续使用；该路径不创建新的 returned-value scope，也不重跑原根而选择另一支。

第二范围保留同一完整子批，按原顺序处理全部声明阶段，每个实际角仍保存本阶段的完整矩阵。J6 与 J9 的请求类型、角阶和完整形状分别绑定，不能互相裁切替代。

两个 scope 不共享缓存。helper 不缓存 active 输入图，不把一个调用结束后的数据或矩阵传到下一点、下一批、下一次线筛或另一个模型。close 清理缓存、data、x 和其它可能持有图的引用；长期对象只保数值计数和有界的本次 provenance。

## 4. 完整相等条件与失败行为

scope 绑定以下实际输入，不以形状或相近浮点值代替身份：

1. 完整当前自由向量的字、摘要、对象、版本、形状和布局，以及完整当前 q/model/source。
2. 有序完整 literal 角批和当前 requested order。
3. 所有原 data 的递归身份、对象/版本/形状/stride，完整 mesh、Gauss 权重、积分阶与实际径向载体字。
4. 每次请求的 previous 三 jet、frame 三 jet，以及 scalar eta 或完整增量三 jet 的全部字和布局。
5. 原 zero 目标的同对象、版本与全部字；其数值没有因矩阵数学上不依赖它而被当作可省略输入。
6. 当前准确共同分割、阶段序号与实际 tau carrier。tau 不进入矩阵相等键，但每次仍按原阶段和完整分割核实。

所以逐角数值相同不能跨不同子批形状命中；一角阶也不能假填第三 jet 为零来复用二角阶结果。正负零与所有 literal words 都属于真实等值条件，不采用容差。

缓存 miss 调原完整方法。hit 返回已存整个矩阵的独立 clone。可选等值键、摘要、clone 或存储发生 MemoryError/RuntimeError 时，回到原方法或返回刚已由原方法得到的完整值，同时记录失败。来源不符、布局不符或强 identity 检查失败仍如实抛错，不冒称所有内存失败都会静默恢复。

## 5. 保留原物理及导数主体的源码证据

完整再生器逐个完整源读取，核实输入 SHA256，进行有计数的文本替换，再验证整个输出。它不是依赖仓库外补丁的运行 shim，全部派生文件均为独立完整正文。

normal 算子只改变 __init__、_run_chain、_get_roots、metadata 四个类方法。九个关键原方法的 AST 保持完全相同：

_total、_corrected_jets、_closure_jets、_normal_frame_jets、_stage_jacobian、_stage_jet_jacobian、_solve_stage、_stage_control_jets、_stage_constraints。

active _implicit_jet_value 及完整六 jet、原 J/J* 接口都未改变。原 Newton 内每一步仍计算自己的原矩阵；缓存没有包裹 _solve_stage。原阶段真实残差、域判断、解、回溯、轨迹、全32阶段链与最终复读也未删除。

构造次序明确为：加入完整新数值政策 → 计算新模型 canonical identity → calibration.bind_field → 原 frame kernel → 新 matrix kernel。新校准文件仅更换独立 ENDPOINT_SCHEMA；全部七个方法 AST 相同，严格 callback/source 守卫没有放宽。

新 geometry 仅改变构造来源守卫；从 _set_x 起全部正文与原 bd1a 相同。全部网格/永久点真读、原192行前缀、原幅度行、包络新增行和原位缓存扩容继续保留。

新 driver 从 def save_report(): 到文件末尾，与实际 cc0a 完整来源逐字相同。该共同后缀 SHA256 为 3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5。它已经包含每次保存 fresh envelope.metadata() 的原包络改动；不把它冒称为更早的未加此行来源。

## 6. 矩阵的实际计数与纯读数器

logical_matrix_requests 与真正 original_matrix_attempts/returns/failures 分开。每个 hit 指向同 scope、同完整等值键、先前真正 original return 的 request index 和矩阵字摘要。原方法返回所产生的 stage/closure/implicit 计数增量，继续从原 q 真实计数差取得；hit 不伪增这些原始调用数。

每个 scope 有自己的当前点摘要和完成状态。纯读数器不会把最后 scope 的点改为当前最终点，也不会把一个矩阵请求或 scope 全部完成当作端点根成功、全场成功、可行性或曲率证书。

读数器通过完整 pinned helper 的 stdlib AST 片段取得 definition 与 validate_metadata。其 __file__ 指向 helper 实际来源，不把源身份变为 reader。完整计数、阶段顺序、矩阵类型/形状、tau carrier、origin 引用与实际增量同时核对。初场失败时没有的字段保留 None，不能用其它点填补。

time/counter 只报告实际成本。完整 x/载体字检查自身有开销；本次没有科学执行，不能声称具体命中率、瓶颈比例、运行时间改善或舍入误差下降。

## 7. 跨新模型的全部地址和 typed 行责任

原 c79 loader 的普通 manifest 能导入完整地点，但它的 strict same-model restore 不允许跨模型恢复 typed 行。新增独立 transfer helper 处理这个明确边界，原两方法及其守卫不变。

fresh entry 必须显式给实际原 cc0a terminal report。每一报告先捕获完整字与 hash，再交原104e完整 reader 核来源、模型和报告；结束时重新核同一字。只接受完整预算终态，或原驱动器明确记载的首次完整场读取失败终态。仍在运行或没有闭合终态的 partial report 不被当作未来事实。

旧/新模型作完整比较。只允许独立新 schema/source、明确新增的 detached_stage_matrix_reuse，以及校准 source/endpoint-source 字段的声明差异。所有剩余完整定义、当前实际 base/reference/profile/chart/自由空间/支持/共同分割/积分载体及包络政策必须相等。cap 和 active_band 也不能借换来源重置。

全部父报告先追加到原完整 walker 的 manifest，独立核三类角色的实际集合包含关系：curvature、radius、protected-curvature。新报告将完整初始三类地址数组序列化到 runner raw，不能只写计数；所以后续同来源重启能继续保已知角色与保护。

每个旧 typed 条目按实际顺序恢复 family、location、partner、branch、sign，整集合不受 near-active cap 限制。旧 first-discovery point/source/report/ordinal 保为旧 provenance；没有把旧 discovery token 写成新场真扫描。重复条目保首次已存在 provenance，再追加来源链。全部 imported typed 行作为初始不可删除 prefix，由纯 reader 逐字核到后续 envelope state 中。

原同模型 restore 会规范化行记录；独立 helper 在已严格通过同模型 restore 后恢复同来源 provenance annotation，不把新模型偷塞进旧 restore。旧 g、Phi、场值、根、J、可行性和连续证书没有被迁移。

公开 Git 只保存完整小源、参数和说明。实际地址数组、每行 provenance、报告、矩阵和检查点仅在 runner，不能把大 raw 加入仓库。

## 8. 显式旧完整 final 变量种子

为避免换缓存来源后无意丢掉已经得到的实际方向，新 driver/launcher 提供成对选项：

    --material-envelope-seed-checkpoint ACTUAL_FINAL_NPZ
    --material-envelope-seed-report ACTUAL_CC0A_TERMINAL_REPORT

报告必须也列在本次完整 material-envelope-parent-report 输入中，且已经完成上一节的全部责任迁移。此选项与同来源 restart 或其它 seed 互斥。它是显式选择，不自动猜测尚未返回的前驱结果。

完整104e再次以 verify_final_bundle=True 核旧报告及原真实 final 文件。独立 helper 读取原保存格式全部13个 NPZ member，核 old schema、完整 old model、base/固定标量/working integration/endpoint policy、mesh、固定 chart/core。全部数值数组必须是对应有限 binary64 形状。

随后从完整 core、共享 quintic omega jets、H 的原 free-layout 提取所有变量，调用当前完整 unpack，再逐 byte 核重构的完整 core/omega/H 等于原保存数组。固定槽也包含在这项核对中。提取点摘要必须同时等于旧末完整 metadata 和旧末完整 geometry 的真实点摘要。

这个步骤不构造旧算子、不读取旧 root cache、不加载旧隐式矩阵。当前 q.model、原 base.initial() 和 reference_point_sha256 前后保持相同。实际初点和来源记录在第一次 F 前写入本次报告；随后仍按完整原循环读本源初 Phi、六 jet、根和全部历史几何，旧 Phi 不作新比较基线。

纯 reader 核完整 seed record、旧报告关系、所有数组/布局身份、当前初点摘要和初场 snapshot；实际旧 accepted direction 数与旧 sampled feasibility 只作为来源描述。完整预算 final 不被自动升级成接受过的方向，新场也不会因此被宣布可行。

若实际前驱首次场读取失败或没有完整可用 final，可以显式选择原固定 reference 初点；此前实际地址和 typed 责任仍完整迁移。当前参数计划没有替这两种情况预作决定。

## 9. 完整 API 和来源

transfer 接口为：

    load_memory(args, preparation, q, history,
        memory=..., current_driver_source=...,
        restart=None, source_report_path=None)
        -> witnesses, radius_witnesses, history_record, envelope, transfer_record

    seed_from_complete_prior_final(args, q,
        current_driver_source=..., transfer_record=...)
        -> optional_complete_free_point, optional_source_record

    validate_metadata(...)
    validate_seed_metadata(...)

load_memory 内部始终调用原 c79 loader。driver 在首次 F 前完整保存 transfer_record 和 optional seed record；每次原 save_report 继续取新 envelope snapshot。

本完整新增 runtime 为下表八件；所有文件小于100000B。

|文件|字节|SHA256|
|---|---:|---|
|detached_normal_stage_matrix_reuse.py|47222|375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59|
|transfer_material_envelope_memory.py|47308|d5e74a6ee160e7ee5a70f53fb96b497e2ff1eacef070757f32ccf8d9226da3eb|
|reference_centred_stage_cached_smooth_triangle_calibration.py|11906|803ff897445b390ec2ba96ed84a0c7598d49ff9756e38077556074d025cce15d|
|so3_reference_centred_stage_cached_smooth_triangle_normal_lift_operator.py|96949|d461f660063bfa2aeecc724050d71c6ef98143b9129f7cfe34f22e4043488a7f|
|so3_reference_centred_stage_cached_material_envelope_geometry.py|67099|bdf212da59c48dfdee86160178e4b8f91177796f4a62fca7f4a1ce9510b9a9f5|
|fullclosed_reference_centred_stage_cached_material_envelope_so3_qp.py|71990|1d1530c3a613d5b0721470139bce338ba950eaf561f51f921b562fb774cbedb2|
|launch_reference_centred_stage_cached_material_envelope_so3_actions.py|19566|0625733b252205e20e98c53b372bfaf27fdae5cd421c6b38551a9d538d1025e5|
|read_reference_centred_stage_cached_material_envelope_so3_report.py|91395|954721008b83c8550b4e0016cf0ec5351e46572dcccccca96f20b180f3cb5f0b|

完整 pure deriver 为 derive_detached_stage_matrix_entry.py，32557B，SHA256 19496677401348aaf29d3b95350f4da9c69c0089079018e6748d49e06626da6e。它锁全部八个输出 hash，支持 --verify-existing，不需导入数值模块。

driver 的 SOURCE_PINS 明列全部37个完整运行来源，包含旧完整 parent reader/driver/operator/calibration/geometry 证据。新几何与 pure reader 对这些真实来源逐项核实，不把 guard 改为只核大小或临时白名单。

## 10. 完整但未选初点的参数计划

文件 detached-stage-matrix-full-envelope-pending-parent-parameter-plan.json 保留全部原数值参数和两个完整 step 模板，并加入新 transfer/可选变量种子合同。它明确：

- executed=False、entry_admitted_or_executed=False。
- complete_source_and_parameter_closure_ready=False；仅静态完整源/参数规格齐。
- 前驱报告路径为 reference-centred-c1-material-envelope-normal-lift-first/report.json，但其 actual hash、终态及 final path 均未预填。
- 没有 steps 键；完整模板置于 unselected_complete_step_templates，须在真实返回后选择初点并构造最终队列。
- 有真实完整 final 时保留继续其全部变量的选项；没有可用 final 时才显式考虑原 reference 初点。不把换 cache source 当作重跑已得方向的理由。
- 所有介于前驱与后继之间真正新增的地址/typed 责任也须加入；当前计划不假定未来没有新的报告。

已知实际 carrier-binding 输入仍为 run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json，其实返 SHA256 aaa65a5ecac807e97cf771a08dd57d2ac26b48adf6acc9592025c0c706581c8e。原/current 整载体由原消费者重新完整核读，不单信 producer 的 true 字段。

模板保 N=2048、全部M=160/J=923自由变量、共同32阶段、1×16 metric、4×64 restoration、15条真回溯、mu=.01、完整 H² jet-sum 参数 .05/24、原正混合权、192已知前缀、全幅度与全部typed行。seed 径向每准确分片使用当前实际参数8点；profile是十二片、每片16点共192词。没有把 provider 的另一默认阶数冒充这套实际 argv。

纯 reader 的 parent_bundle 仍为真实 reference，不依赖一个失败时不存在的 future final。summary selectors 仅标量 dot-path；完整矩阵/provenance/地址和批次数组不进入公共小卷。

## 11. 已做的静态验证及未付责任

实际只做完整文本/字节/hash、AST、compile、py_compile、重复literal key/keyword、尾空白检查、完整纯来源再生与 --verify-existing。驱动/launcher 全部参数解析相同；其既有科学后缀与 cc0a 逐字相等。没有导入 Torch/NumPy/SciPy 来执行任何科学函数，没有构造测试场或数值 fixture。

solver 独立读了 matrix helper 的 scope/key/origin/回退、pure validator、完整 transfer 和新增 final-variable 分支。geometry 独立核了 tau 的局部偏导范围、整个批/字边界、两处调用 hook、同分支升级和新模型绑定顺序。以上均是源码/解析审查，不能替代实际运行返回。

本次不支付积分、逆图、AD、矩阵/解舍入或连续全角误差；不证明矩阵可逆、normal 分支覆盖、参考或候选嵌入、剩余两 Gram 分量、最终幅度与 marked reach。原真实全场读数和严格连续费用链继续各负其责。没有把源实现齐或局部矩阵复用当作任务的数学完成标准。


## 12. root 完整复核与正式发表边界

root 已核完整 source-only 再生器、完整 typed/地址转移及13 member变量继承正文、新增 pure validator 和所有数值调用差异；对 revision2 在独立 scratch 只执行 stdlib 源构造，八个 runtime 全部与表中原字节一致。37个实际运行角色逐项全SHA匹配；原九个数学方法 AST、全部校准方法、geometry 从 `_set_x` 后缀以及 driver 从 `save_report` 后缀均由完整源直接比较。五个原 counter 键和 scalar/angular 动态键另经独立 AST 初始化表核对，两处前缀修订反向替换恰还原旧 helper SHA。

根对完整科学 argv 的逐项差异只见新 outdir 和显式 `--material-envelope-parent-report` 一对；原全部数值参数保持。正式给出的计划没有 `steps`，未选择初点、未加入活动队列，亦不更改正在执行的 cc0a。等待其实际终态仅为了真实选择父点；其它费用、几何及后续输入工作同时继续。实际有完整可用 final 时应延续其全部变量并重读本源初场；不把更换缓存来源作为丢失已有接受方向的理由。

本次普通提交只收入完整 revision2 可再生源码、完整参数计划与本说明。旧29c是未执行的审查稿，§0准确保存其缺陷、完整身份及两处可逆修改；不把暂存/未引用 blob 声称为另一已运行、已准入或永久归档的科学来源。所有实际矩阵命中、时间改善、舍入误差、根与几何效果仍等待公开 Actions，本文没有补造它们。
